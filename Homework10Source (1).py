class Student:
    def __init__(self, student_id, fname, lname, enroll_date):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.enroll_date = enroll_date

class Course:
    def __init__(self, course_id, title, cred_hr):
        self.course_id = course_id
        self.title = title
        self.cred_hr = cred_hr

class Enrollment:
    def __init__(self, enroll_id, course, student):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student

    def display(self):
        for enrollment in self.enrollments.values():
            print(enrollment)
        

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


        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3)
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4)
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4)
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3)
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4)
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
        grade_book = GradeBook()

        while more_enteries == 'y':
            student_key = int(input("Enter enroll id: "))
            student = grade_book.enrollments[student_key]

            student_grade = input("Enter a grade: ")
            student.grade = student_grade
            

            more_enteries = input("Type f to finish")
            
        def __str__(self):
            return str(self.enrollments[enroll_id]) + str(self.enrollments[course]) + str(self.enrollments[student])

        for key in self.enrollments.values():
            print(key)

done = GradeBook()
done.main()

        
