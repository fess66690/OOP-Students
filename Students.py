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
            average = sum_rate/len_rate
        return average

    def __str__ (self):
        return (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за домашние задания: {self.average_score} \n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score


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
        return (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за домашние лекции: {self.average_score}')

    @property
    def average_score(self, sum_rate=0, len_rate=0):
        for key, grad in enumerate(self.grades):
            sum_rate += sum(self.grades[grad])
            len_rate += len(self.grades[grad])
            average = sum_rate / len_rate
        return average

    def __eq__(self, other):
        return self.average_score == other.average_score
    def __lt__(self, other):
        return self.average_score < other.average_score

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

def average_homework_grade(students, course_name):
    total_sum = 0
    total_count = 0

    for student in students:
        if course_name in student.grades:
            total_sum += sum(student.grades[course_name])
            total_count += len(student.grades[course_name])

    if total_count == 0:
        return 0

    return round(total_sum / total_count, 1)


def average_lecture_grade(lecturers, course_name):
    total_sum = 0
    total_count = 0

    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_sum += sum(lecturer.grades[course_name])
            total_count += len(lecturer.grades[course_name])

    if total_count == 0:
        return 0

    return round(total_sum / total_count, 1)



student1 = Student("Иван", "Иванов", "М")
student2 = Student("Светлана", "Лютик", "Ж")

reviewer1 = Reviewer("Первый", "Профессор")
reviewer2 = Reviewer("Второй", "Профессор")

lecturer1 = Lecturer ("Первый", "Лектор")
lecturer2 = Lecturer ("Второй", "Лектор")

student1.courses_in_progress += ['Python', 'C++']
student2.courses_in_progress += ['Python', 'Java']
lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'Java']
reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'Java']

reviewer1.rate_hw(student1,'C++', 10)
reviewer2.rate_hw(student1,'Python', 2)

reviewer1.rate_hw(student2,'Python', 10)
reviewer2.rate_hw(student2,'Java', 2)

student1.rate_lecture(lecturer1,"C++", 8)
student2.rate_lecture(lecturer1, 'Python', 4)
student1.rate_lecture(lecturer2,"Python", 10)
student2.rate_lecture(lecturer2, 'Java', 10)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)
print(student2 == student1)
print(lecturer2 > lecturer1)
print(average_homework_grade([student1,student2], 'Python'))
print(average_lecture_grade([lecturer1,lecturer2], 'Python'))
print(average_lecture_grade([lecturer1,lecturer2], 'Java'))
