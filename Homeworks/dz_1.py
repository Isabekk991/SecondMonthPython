class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'my name {self.full_name}, I am {self.age}')


class Student(Person):
    def __init__(self, full_name, age, marks):
        super().__init__(full_name, age, is_married=False)
        self.marks = marks

    def Summa(self):
        return sum(self.marks.values())

    def CenterMarks(self):
        total_marks = self.Summa()
        return total_marks / len(self.marks)


class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
        self.salary = Teacher.base_salary

    def adjust_salary(self):
        if self.experience > 3:
            increase_years = self.experience - 2
            self.salary = Teacher.base_salary * (1 + 0.3 * increase_years)

    def get_info(self):
        print(f'Teacher {self.full_name}, experience {self.experience}, salary {self.salary}')


def create_students():
    students = []
    student1 = Student('Mike', 15, {"math": 98, "history": 87, "PE": 69})
    student2 = Student('Diana', 12, {"math": 45, "history": 98, "PE": 80})
    student3 = Student('Daniel', 20, {"math": 56, "history": 34, "PE": 67})
    students.extend([student1, student2, student3])
    return students


teacher = Teacher(full_name='Asan', age=47, is_married=True, experience=4)
teacher.adjust_salary()
teacher.get_info()

students_list = create_students()
for student in students_list:
    print(f"student {student.full_name}, age {student.age}, marks {student.marks}")  
    average_marks = student.CenterMarks()
    print(f"average_marks {average_marks:.2f}")
