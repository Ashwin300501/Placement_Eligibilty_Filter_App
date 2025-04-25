import streamlit as st
import sqlite3
import pandas as pd

#Connection to database
def get_connection():
    return sqlite3.connect("students.db")

#load data function
def load_data():
    conn=get_connection()
    students=pd.read_sql("SELECT * FROM students",conn)
    programming = pd.read_sql("SELECT * FROM programming", conn)
    soft_skills = pd.read_sql("SELECT * FROM soft_skills", conn)
    placements = pd.read_sql("SELECT * FROM placements", conn)
    conn.close()
    return students, programming, soft_skills, placements

#ui setup
st.set_page_config(page_title="Student Placement Dashboard", layout="wide")
st.title("Student Placement Dashboard")

tab1,tab2=st.tabs(["Eligibility Fiter","Insights"])
students_df, programming_df, soft_skills_df, placements_df = load_data()

#tab1 filters

#filers
with tab1:
    st.header("Filter Students by Eligibility Criteria")
    col1,col2,col3,col4=st.columns(4)

    with col1:
        min_problems=st.number_input("Min problem solved",0,200)
    with col2:
        min_softskill=st.number_input("Min communication score",0,100)
    with col3:
        placement_status=st.selectbox("Placement status",options=["Any","Ready","Not Ready","Placed"])
    with col4:
        min_mock_interview_score=st.number_input("Min mock interview score",0,100)
    
    merged=students_df.merge(programming_df,on="student_id")\
                     .merge(soft_skills_df,on="student_id")\
                     .merge(placements_df, on="student_id")
    
#filtered table
filtered=merged[
        (merged["problems_solved"] >= min_problems) &
        (merged["communication"] >= min_softskill)&
        (merged["mock_interview_score"]>=min_mock_interview_score)]

if placement_status!="Any":
    filtered=filtered[filtered["placement_status"]==placement_status]

    st.success(f"{len(filtered)} students matched your criteria.")
    columns_to_show=["student_id","name","age","email","enrollment_year","course_batch","graduation_year","problems_solved","communication","placement_status","mock_interview_score"]

    filtered_display=filtered[columns_to_show]

    st.dataframe(filtered_display)