from faker import Faker
import pandas as pd
import random as r

fake=Faker()

students_num=100 #total number of data we want
batches=["B1","B2","B3","B4"]

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