from faker import Faker
import pandas as pd
import random as r

fake=Faker()

students_num=100 #total number of data we want
batches=["B1","B2","B3","B4"]
languages=["Python","SQL","JAVA","Ruby"]
Status=["Ready","Not ready","Placed"]

#Creating the students table
students=[]
for i in range(students_num):
    enrollment_year=r.randint(2020,2024)
    graduation_year=r.randint(enrollment_year,enrollment_year+4)
    students.append({
        "students_id":i+1,
        "name":fake.name(),
        "age":r.randint(18,25),
        "gender":r.choice(["Male","Female",]),
        "email":fake.email(),
        "phone":fake.phone_number(),
        "enrollment_year":enrollment_year,
        "course_batch":r.choice(batches),
        "city":fake.city(),
        "graduation_year":graduation_year
    })

#creating programming table
programming=[]
for i in range(students_num):
    programming.append({
        "programming_id":i+1,
        "students_id":i+1,
        "language":r.choice(languages),
        "problems_solved":r.randint(10,200),
        "assessments_completed":r.randint(0,10),
        "mini_projects":r.randint(0,5),
        "certifications_earned":r.randint(0,3),
        "latest_project_score":r.randint(0,100)
    })

#creating softskill table
soft_skills=[]
for i in range(students_num):
    soft_skills.append({
        "soft_skill_id": i + 1,
        "student_id": i + 1,
        "communication": r.randint(50, 100),
        "teamwork": r.randint(50, 100),
        "presentation": r.randint(50, 100),
        "leadership": r.randint(50, 100),
        "critical_thinking": r.randint(50, 100),
        "interpersonal_skills": r.randint(50, 100)
    })

# creating Placement table
placements = []
for i in range(students_num):
    status = r.choice(Status)
    company = fake.company() if status == 'Placed' else None
    package = r.randint(40000, 150000) if status == 'Placed' else None
    placement_date = fake.date_between(start_date='-1y', end_date='today') if status == 'Placed' else None

    placements.append({
        "placement_id": i + 1,
        "student_id": i + 1,
        "mock_interview_score": r.randint(0, 100),
        "internships_completed": r.randint(0, 3),
        "placement_status": status,
        "company_name": company,
        "placement_package": package,
        "interview_rounds_cleared": r.randint(0, 5),
        "placement_date": placement_date
    })

#converting all the data generated in to dataframe
students_df=pd.DataFrame(students)
programming_df=pd.DataFrame(programming)
soft_skills_df=pd.DataFrame(soft_skills)
placements_df=pd.DataFrame(placements)

#importing Databasemanager
from To_Database import DatabaseManager

db=DatabaseManager
db.create_tables()
db.insert_dataframe(students_df, "students")
db.insert_dataframe(programming_df, "programming")
db.insert_dataframe(soft_skills_df, "soft_skills")
db.insert_dataframe(placements_df, "placements")
db.close()

print("Data inserted to the database")