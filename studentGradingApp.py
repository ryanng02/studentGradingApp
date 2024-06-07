# Final Project: Grading System
class Student:
    def __init__(self, course_name, name):
        self.course_name = course_name
        self.name = name
        self.assignments_list = []
        #stores assignments
    
    #adding assignments into list
    def add_assignment(self, assignment):
        self.assignments_list.append(assignment)

    #edits old score of an assignment
    def update_assignment_score(self, assignment_name, new_score):
        for assignment in self.assignments_list:
            if assignment.title == assignment_name:
                assignment.update_score(new_score)
                break
    
    #removing assignment
    def remove_assignment(self, assignment_name):
        self.assignments_list = [a for a in self.assignments_list if a.title != assignment_name]

    #calculates grade by weighing average
    def compute_grade(self):
        total = sum(a.score for a in self.assignments_list)
        count = len(self.assignments_list) * 100
        try:
            percent = (total / count) * 100
        except ZeroDivisionError:
            return 0, 'N/A'  # No assignments case
        if percent >= 90:
            grade = 'A'
        elif percent >= 80:
            grade = 'B'
        elif percent >= 70:
            grade = 'C'
        elif percent >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return percent, grade

class Assignment:
    def __init__(self, title, type_of_assignment, score):
        self.title = title
        self.type_of_assignment = type_of_assignment
        self.score = score
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")

    #update new score and number value error handling
    def update_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
        else:
            raise ValueError("Score must be between 0 and 100.")

class GradeBook:
    def __init__(self):
        self.students = {}
        #stores student names

    def enroll_student(self, course, student_name):
        self.students[student_name] = Student(course, student_name)

    def log_assignment(self, student_name, title, type_of_assignment, score):
        if student_name in self.students:
            new_assignment = Assignment(title, type_of_assignment, score)
            self.students[student_name].add_assignment(new_assignment)
        else:
            print(f"No record found for {student_name}.")

    def adjust_assignment_score(self, student_name, title, new_score):
        if student_name in self.students:
            self.students[student_name].update_assignment_score(title, new_score)

    def discard_assignment(self, student_name, title):
        if student_name in self.students:
            self.students[student_name].remove_assignment(title)

    def show_grades(self, student_name):
        student = self.students.get(student_name)
        if student:
            print(f"\nShowing Grades for: {student.name} in {student.course_name}")
            for assignment in student.assignments_list:
                print(f"\t{assignment.title} [{assignment.type_of_assignment}]: {assignment.score}/100")
            percent, grade = student.compute_grade()
            print(f"Final Grade: {percent:.2f}% ({grade})")
        else:
            print("Student not found.")

#main menu in CLI
def main():
    book = GradeBook()
    while True:
        print("\nOptions:")
        print("1: Register Student\n2: Add Assignment\n3: Edit Assignment Score\n4: Delete Assignment\n5: Display Grades\n6: Exit")
        selection = input("Choose an option: ")
        if selection == '1':
            print("\n> New Student Registration")
            course = input("Course Name: ")
            name = input("Student Name: ")
            book.enroll_student(course, name)
        elif selection == '2':
            print("\n> Assignment Log")
            student = input("Student Name: ")
            title = input("Assignment Title: ")
            type_of_assignment = "Homework" if input("Type (1 for Homework, 2 for Test): ") == '1' else "Test"
            score = int(input("Score: "))
            book.log_assignment(student, title, type_of_assignment, score)
        elif selection == '3':
            print("\n> Update Assignment Score")
            student = input("Student Name: ")
            title = input("Assignment Title: ")
            new_score = int(input("New Score: "))
            book.adjust_assignment_score(student, title, new_score)
        elif selection == '4':
            print("\n> Remove Assignment")
            student = input("Student Name: ")
            title = input("Assignment Title: ")
            book.discard_assignment(student, title)
        elif selection == '5':
            print("\n> Student Grades")
            student = input("Student Name: ")
            book.show_grades(student)
        elif selection == '6':
            print("Exiting...")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()
