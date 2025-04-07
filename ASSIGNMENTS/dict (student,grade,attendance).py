
student_records = {
    "student1": {"name": "Dishita", "grades": [85, 92, 78], "attendance": 100},
    "student2": {"name": "Vanshita", "grades": [88, 76, 95], "attendance": 100},
    "student3": {"name": "Ankit", "grades": [90, 88, 93], "attendance": 95},
}


def add_or_update_student(student_id, name, grades, attendance):
    student_records[student_id] = {"name": name, "grades": grades, "attendance": attendance}


def display_records():
    for student_id, record in student_records.items():
        print(f"ID: {student_id}, Name: {record['name']}, Grades: {record['grades']}, Attendance: {record['attendance']}")


display_records()
print("\nAdding a new student...\n")
add_or_update_student("student4", "Manav", [89, 92, 85], 90)
display_records()
print("\nUpdating student2...\n")
add_or_update_student("student2", "Shaurya", [30, 35, 40], 19)
display_records()
