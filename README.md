# 🎵 MSMS v3 (Music School Management System)

**MSMS v3** is a small console application for managing a music school.  
It was developed as part of **FIT1056 – Programming Fundamentals (Semester 2, 2025)**.

The project demonstrates an **object-oriented design** with:
- **Model layer** → `User`, `StudentUser`, `TeacherUser`, `Course`
- **Controller layer** → `ScheduleManager` (business logic, persistence)
- **View layer** → `main.py` (user interface / menu)

---

## 📂 Project Structure

pst 3/
├── main.py # View layer (menu + input/output)
├── app/
│ ├── init.py
│ ├── user.py # Base User class
│ ├── student.py # StudentUser class
│ ├── teacher.py # TeacherUser + Course
│ └── schedule.py # ScheduleManager (controller)
└── data/
└── msms.json # JSON database (students, teachers, courses, attendance)
