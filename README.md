# 🎓 Student Placement Dashboard

A complete data generation, storage, and visualization system for student performance and placement readiness using **Python**, **SQLite**, and **Streamlit**.

---

## 📁 Project Modules

### ✅ Module 1: Data Generation
Generates fake student data using the `Faker` library for:
- Students
- Programming skills
- Soft skills
- Placement information

The generated data is stored in four separate tables in a SQLite database (`students.db`).

### ✅ Module 2: Database Management
Contains a reusable `DatabaseManager` class that:
- Creates SQLite tables with appropriate schema and relationships.
- Supports inserting Pandas DataFrames into the database.

### ✅ Module 3: Streamlit Dashboard
A web-based interactive dashboard that:
- Filters students based on eligibility criteria.
- Visualizes insights with charts and tables.
- Uses SQL queries and Pandas for analysis.

---

## 📦 Requirements

Install required packages using pip:

```bash
pip install faker pandas streamlit
