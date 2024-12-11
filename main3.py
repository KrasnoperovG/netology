class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        list_grades = []
        for course, grade in self.grades.items():
            list_grades += grade
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum(list_grades)/len(list_grades)}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):        
        pass
     
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        list_grades = []
        for course in self.courses_attached:
            list_grades += self.grades.get(course, [])
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(list_grades)/len(list_grades)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python'] # Добавляем курс лектору

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python'] + ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student.rate_lecturer(some_lecturer, 'Python', 8) # Студент выставляет оценку лектору
some_student.rate_lecturer(some_lecturer, 'Python', 5) # Студент выставляет оценку лектору

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python'] 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)



print(some_reviewer)
print(some_lecturer)
print(some_student)
pass