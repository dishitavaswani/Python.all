'''Create a Python code to demonstrate the use of sets and perform set
operations (union, intersection, difference) to manage student enrollments
in multiple courses / appearing for multiple entrance exams like CET,
JEE, NEET etc 
'''

def input_students(exam_name):
    n = int(input(f"Enter the number of students giving {exam_name}:"))
    student_set = set()

    for _ in range(n):
        student = input("Student Name:")
        student_set.add(student)
        
    return student_set
        


cet_students = input_students("CET")
jee_students = input_students("JEE")
neet_students = input_students("NEET")


all_students = cet_students | jee_students | neet_students  
common_students = cet_students & jee_students & neet_students 
cet_only = cet_students - (jee_students | neet_students)  
jee_only = jee_students - (cet_students | neet_students)
neet_only = neet_students - (jee_students | cet_students)
jee_neet_common = jee_students & neet_students  
jee_cet_common = jee_students & cet_students
neet_cet_common = neet_students & cet_students

print("\nAll unique students appearing for at least one exam:", all_students)
print("\nStudents appearing for all three exams (CET, JEE, NEET):", common_students)
print("\nStudents appearing only for CET:", cet_only)
print("\nStudents appearing only for JEE:", jee_only)
print("\nStudents appearing only for NEET:", neet_only)
print("\nStudents appearing for both JEE and NEET:", jee_neet_common)
print("\nStudents appearing for both JEE and CET:", jee_cet_common)
print("\nStudents appearing for both NEET and CET:", neet_cet_common)

