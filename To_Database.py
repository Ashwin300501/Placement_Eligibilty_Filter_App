import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                gender TEXT,
                email TEXT,
                phone TEXT,
                enrollment_year INTEGER,
                course_batch TEXT,
                city TEXT,
                graduation_year INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS programming (
                programming_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                language TEXT,
                problems_solved INTEGER,
                assessments_completed INTEGER,
                mini_projects INTEGER,
                certifications_earned INTEGER,
                latest_project_score INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS soft_skills (
                soft_skill_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                communication INTEGER,
                teamwork INTEGER,
                presentation INTEGER,
                leadership INTEGER,
                critical_thinking INTEGER,
                interpersonal_skills INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS placements (
                placement_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                mock_interview_score INTEGER,
                internships_completed INTEGER,
                placement_status TEXT,
                company_name TEXT,
                placement_package INTEGER,
                interview_rounds_cleared INTEGER,
                placement_date TEXT,
                FOREIGN KEY(student_id) REFERENCES students(student_id)
            )
        ''')

        self.conn.commit()

    def insert_dataframe(self, df: pd.DataFrame, table_name: str):
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)

    def close(self):
        self.conn.close()