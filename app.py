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
    
    merged=students_df.merge(programming_df,on="students_id")\
                     .merge(soft_skills_df,on="students_id")\
                     .merge(placements_df, on="students_id")
    
    #filtered table
    filtered=merged[
            (merged["problems_solved"] >= min_problems) &
            (merged["communication"] >= min_softskill)&
            (merged["mock_interview_score"]>=min_mock_interview_score)]

    if placement_status != "Any":
        filtered = filtered[filtered["placement_status"] == placement_status]

    st.success(f"{len(filtered)} students matched your criteria.")
    columns_to_show=["students_id","name","age","email","enrollment_year","course_batch","graduation_year","problems_solved","communication","placement_status",
                     "mock_interview_score"]

    filtered_display=filtered[columns_to_show]

    st.dataframe(filtered_display)

#tab2 Insights
with tab2:
    st.header("📊 Insights from Data")

    conn = get_connection()

    st.subheader("1. Average Problems Solved per Batch (Bar Chart)")
    query1 = """
    SELECT course_batch, AVG(problems_solved) AS avg_problems
    FROM students
    JOIN programming USING(students_id)
    GROUP BY course_batch
    ORDER BY course_batch
    """
    avg_problems_df = pd.read_sql_query(query1, conn)
    st.bar_chart(avg_problems_df.set_index("course_batch"))

    st.subheader("2. Top 5 Placement-Ready Students by Mock Interview Score")
    query2 = """
    SELECT s.name AS Name, p.mock_interview_score AS "Mock Interview Score",
           sk.communication AS Communication, sk.presentation AS Presentation
    FROM students s
    JOIN placements p USING(students_id)
    JOIN soft_skills sk USING(students_id)
    WHERE p.placement_status = 'Ready'
    ORDER BY p.mock_interview_score DESC
    LIMIT 5
    """
    top_students_df = pd.read_sql_query(query2, conn)
    st.table(top_students_df)

    st.subheader("3. Bar Chart: Average Problems Solved by Gender")
    query3 = """
    SELECT s.gender, AVG(p.problems_solved) AS total_problems
    FROM students s
    JOIN programming p ON s.students_id = p.students_id
    GROUP BY s.gender
    """
    gender_problems_df = pd.read_sql_query(query3, conn)
    gender_problems_df.set_index("gender", inplace=True)
    st.bar_chart(gender_problems_df)

    st.subheader("4. Average Soft Skill Scores by Course")

    query4 = """
    SELECT s.course_batch AS course, 
           AVG(sk.communication) AS average_communication, 
           AVG(sk.presentation) AS average_presentation
    FROM students s
    JOIN soft_skills sk ON s.students_id = sk.students_id
    GROUP BY s.course_batch
    ORDER BY s.course_batch
    """
    skill_avg_df = pd.read_sql_query(query4, conn)
    st.dataframe(skill_avg_df.style)

    conn.close()