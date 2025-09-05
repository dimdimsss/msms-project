# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # TODO: Call a method on the manager to get the day's lessons and print them.
    lessons = manager.get_lessons_for_day(day)
    for lesson in lessons:
        print(f"{lesson['time']} - {lesson['course_name']} in room {lesson['room']} (Teacher {lesson['teacher_id']})")

def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    if manager.enroll_student_in_course(student_id=student_id, course_id=to_course_id):
        student = manager._find_student(student_id)
        if from_course_id in student.enrolled_course_ids:
            student.enrolled_course_ids.remove(from_course_id)
        course = manager._find_course(from_course_id)
        if student_id in course.enrolled_student_ids:
            course.enrolled_student_ids.remove(student_id)
        manager._save_data()
        print(f"Student {student_id} switched from course {from_course_id} to {to_course_id}.")
    else:
        print("Switch failed.")

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        # TODO: Create a menu for the new PST3 functions.
        # Get user input and call the appropriate view function, passing 'manager' to it.
        print("1. View daily roster")
        print("2. Switch course")
        print("q. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice == '2':
            sid = int(input("Enter student ID: "))
            from_cid = int(input("Enter course ID to leave: "))
            to_cid = int(input("Enter course ID to join: "))
            switch_course(manager, sid, from_cid, to_cid)
        elif choice.lower() == 'q':
            break
        
if __name__ == "__main__":
    main()
