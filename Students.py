from tkinter.font import names


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def average_score (self, sum_rate=0, len_rate = 0):
        for key, grad in enumerate(self.grades):
            sum_rate += sum(self.grades[grad])
            len_rate += len(self.grades[grad])
            average_score = sum_rate/len_rate
        return average_score

    def __str__ (self):
        return (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за домашние задания: {self.average_score} \n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')

    # def __eq__(self, other):


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__ (self, sum_rate=0, len_rate = 0):
        for key, grad in enumerate(self.grades):
            sum_rate += sum(self.grades[grad])
            len_rate += len(self.grades[grad])
        return (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за домашние лекции: {sum_rate/len_rate}')

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__ (self):
        return (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}

reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 6)
student.courses_in_progress +=['C++']
student.finished_courses+=['Pascal']
reviewer.rate_hw(student, 'C++', 10)

print(student)
print(lecturer)
print(reviewer)