class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}



    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        for value in self.grades.values():
            return round(sum(value)/len(value),1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._middle_grade()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить!')
            return
        return self._middle_grade() < other._middle_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}
    def _middle_rate(self):
        for value in self.grades1.values():
            return round(sum(value) / len(value),1)


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._middle_rate()}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить!')
            return
        return self._middle_rate() < other._middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя = {self.name}\n'
                f'Фамилия = {self.surname}')


Ivan_student = Student('Ivan', 'Ivanov', 'Male')
Petr_student = Student('Petr', 'Petrov', 'Male')
Ivan_student.finished_courses += ['Введение в программирование']
Ivan_student.courses_in_progress += ['Python', 'Git']
Petr_student.finished_courses += ['Введение в программирование', 'Git']
Petr_student.courses_in_progress += ['Python']

Dima_mentor = Mentor('Dima', 'Medvedev')
Volodya_mentor = Mentor('Volodya', 'Pupkin')

Alex_lecturer = Lecturer('Alex', 'Alexeev')
Oleg_lecturer = Lecturer('Oleg', 'Olegov')
Alex_lecturer.courses_attached += ['Python', 'Git']
Oleg_lecturer.courses_attached += ['Python', 'Git']

Igor_reviewer = Reviewer('Igor', 'Igorev')
Sveta_reviewer = Reviewer('Sveta', 'Svetaeva')
Igor_reviewer.courses_attached += ['Python', 'Git']
Sveta_reviewer.courses_attached += ['Python', 'Git']

Ivan_student.rate_hw_lecturer(Alex_lecturer, 'Python', 5)
Ivan_student.rate_hw_lecturer(Oleg_lecturer, 'Python', 6)
Petr_student.rate_hw_lecturer(Oleg_lecturer, 'Python', 3)
Petr_student.rate_hw_lecturer(Alex_lecturer, 'Python', 8)

Igor_reviewer.rate_hw(Ivan_student, 'Python', 7)
Igor_reviewer.rate_hw(Petr_student, 'Python', 9)
Igor_reviewer.rate_hw(Petr_student, 'Git', 7)
Sveta_reviewer.rate_hw(Petr_student, 'Python', 10)
Sveta_reviewer.rate_hw(Ivan_student, 'Python', 8)
Sveta_reviewer.rate_hw(Ivan_student, 'Python', 9)


Ivan_student._middle_grade()
Petr_student._middle_grade()
print(Ivan_student < Petr_student)
print(Ivan_student)
print(Petr_student)

Alex_lecturer._middle_rate()
Oleg_lecturer._middle_rate()
print(Alex_lecturer < Oleg_lecturer)
print(Alex_lecturer)
print(Oleg_lecturer)

print(Igor_reviewer)
print(Sveta_reviewer)

student_list = [Ivan_student, Petr_student]


def grade_middle_student(student_list, course):
    sum = 0
    count = 0
    for man in student_list:
        for i in man.grades[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


lecturer_list = [Alex_lecturer, Oleg_lecturer]


def grade_middle_lecturer(lecturer_list, course):
    sum = 0
    count = 0
    for man in lecturer_list:
        for i in man.grades1[course]:
            sum += i
            count += 1
    return round(sum / count, 1)


print(grade_middle_student(student_list, 'Python'))
print(grade_middle_lecturer(lecturer_list, 'Python'))