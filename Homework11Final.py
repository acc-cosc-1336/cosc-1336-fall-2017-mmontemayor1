
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
class Student(Person):
    def __init__(self, student_id, first_name, last_name, enroll_date):
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.enroll_date = enroll_date

class Professor(Person):
    def __init__(self, professor_id, first_name, last_name, hire_date):
        Person.__init__(self, first_name, last_name)
        self.hire_date = hire_date
        self.professor_id = professor_id

class Course:
    def __init__(self, course_id, title, cred_hr, professor):
        self.course_id = course_id
        self.title = title
        self.cred_hr = cred_hr
        self.professor = professor

class Enrollment:
    def __init__(self, enroll_id, student, course):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student
        self.grade = ''

    def display(self):
        print(self.enroll_id, format(self.student.first_name, '10'), format(self.student.last_name, '16'),
            format(self.course.title, '20'), format(self.grade, '20'))

class Transcript:
    def __init__(self, enrollments):
        self.enrollments = enrollments

    def print_transcript(self, student):
        self.letter_grades = ['A', 'B', 'C', 'D', 'F']
        
        print("Student: ", student.first_name, student.last_name)
        credit_points = 0
        grade_points = 0
        total_grade_pts = 0
        total_cred_hrs = 0

        print("Course", " "*10, "Credit Hours ", "Credit Points ", "Grade Points ", "Grade")

        for c in self.enrollments.values():
            if c.student.student_id == student.student_id:
                if c.grade in self.letter_grades:
                    total_cred_hrs += c.course.cred_hr

                credit_points = self.grade_to_points(c.grade)
                grade_points = c.course.cred_hr * credit_points

                total_grade_pts += grade_points

                print(format(c.course.title, '15'), format(c.course.cred_hr, '14'), format(credit_points, '13'),
                      format(grade_points, '14'), c.grade)

        print(" "*28, total_cred_hrs, " "*26, total_grade_pts)

        if total_cred_hrs >= 1:
            gpa = total_grade_pts / total_cred_hrs
            print("GPA:  ", format(gpa, '.2f'))
            
                

    def grade_to_points(self, letter_grade):

        credit_points = 0

        if letter_grade == 'A':
            credit_points = 4
        elif letter_grade == 'B':
            credit_points = 3
        elif letter_grade == 'C':
            credit_points = 2
        elif letter_grade == 'D':
            credit_points = 1

        return credit_points
                
                
            
        

class GradeBook:
    def __init__(self):
        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexande#r", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s

        self.professors = {}
        
        #professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11") 
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06") 
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01") 
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12") 
        self.professors[p.professor_id] = p


        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, self.professors[5])
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3, self.professors[2])
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4, self.professors[2])
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

    def main(self):

        more_enteries = 'y'

        while more_enteries == 'y':
            student_key = int(input("Enter enroll id: "))

            if student_key in self.enrollments:
                confirm = self.enrollments.get(student_key)

                student_grade = input("Enter a grade: ")
                confirm.grade = student_grade
            else:
                print("Invalid enroll id.")

            more_enteries = input("Type y to continue")
            
        student_key = int(input("Enter student ID: "))

        if student_key in self.students:
            student = self.students.get(student_key)
            script = Transcript(self.enrollments)
            script.print_transcript(student)
                
        else:
            print("Invalid student ID.")
            

done = GradeBook()
done.main()

        
