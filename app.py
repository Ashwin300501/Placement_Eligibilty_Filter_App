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