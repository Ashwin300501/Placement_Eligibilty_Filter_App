from faker import Faker
import pandas as pd
import random as r

fake=Faker()

students_num=100 #total number of data we want
batches=["B1","B2","B3","B4"]
languages=["Python","SQL","JAVA","Ruby"]

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