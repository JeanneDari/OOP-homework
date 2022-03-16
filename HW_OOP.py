class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade in range(11):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Оценки по 10-бальной шкале!')
        else:
            return 'Ошибка'

    def __str__(self):
        name = 'Имя: ' + self.name
        surname = f"Фамилия: {self.surname}"
        grade = f"Средняя оценка за домашние задания: {sum(sum(list(self.grades.values()),[]))/len(sum(list(self.grades.values()),[]))}"
        courses_in_progress = f"Курсы в процессе обучения: {str(self.courses_in_progress)[1:-1]}"
        finished_courses = f"Завершенные курсы: {str(self.finished_courses)[1:-1]}"
        return name + "\n" + surname + "\n" + str(grade) + "\n" + courses_in_progress + "\n" + finished_courses

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.__av_lecturer_grade()}\n'
        return res

    def __av_lecturer_grade(self):
        av_sum_grade = 0
        num_grades = 0
        for course in self.grades:
            av_sum_grade += sum(self.grades[course])
            num_grades += len(self.grades[course])
        if num_grades > 0:
            return round(av_sum_grade / num_grades, 2)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__av_lecturer_grade() < other.__av_lecturer_grade()

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
        name = 'Имя: ' + self.name
        surname = f"Фамилия: {self.surname}"
        return name + "\n" + surname


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']
best_student.add_courses('SQL')
#print(best_student.__dict__)
new_student = Student('Jeanne', 'Dari', 'female')
new_student.courses_in_progress += ['Python']
new_student.courses_in_progress += ['JS']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['JS']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'JS', 8)
cool_reviewer.rate_hw(new_student, 'Python', 8)
cool_reviewer.rate_hw(new_student, 'Python', 8)
cool_reviewer.rate_hw(new_student, 'JS', 8)
best_lecturer = Lecturer('Anna', 'Lee')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['JS']
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 5)
best_student.rate_lecturer(best_lecturer, 'JS', 7)

new_lecturer = Lecturer('Sonya', 'Kim')
new_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['JS']
best_student.rate_lecturer(new_lecturer, 'Python', 9)
best_student.rate_lecturer(new_lecturer, 'Python', 8)
best_student.rate_lecturer(new_lecturer, 'JS', 7)
#print(best_lecturer.courses_attached)
#print(best_lecturer.__str__())
#print(new_lecturer.__str__())
#print(best_lecturer.__lt__(new_lecturer))
#print(best_lecturer.name, best_lecturer.surname, best_lecturer.courses_attached, best_lecturer.grades)
#print(best_student.name, best_student.surname, best_student.finished_courses, best_student.courses_in_progress, best_student.grades)
#print(len(best_lecturer.grades))

def av_grade_all_lecturers(list_lecturers, course):
    av_sum_grade = 0
    num_grades = 0
    for lecturer in list_lecturers:
        if course in lecturer.grades:
            av_sum_grade += sum(lecturer.grades[course])
            num_grades += len(lecturer.grades[course])
    if num_grades > 0:
        return round(av_sum_grade / num_grades, 2)
    else:
        return 0

lecturers_list = [new_lecturer]
course_specific = 'JS'
print(
    f'Средняя оценка за лекции всех лекторов в рамках курса {course_specific}: {av_grade_all_lecturers(lecturers_list, course_specific)}')


def av_grade_all_students(list_students, course):
    av_sum_grade = 0
    num_grades = 0
    for student in list_students:
        if course in student.grades:
            av_sum_grade += sum(student.grades[course])
            num_grades += len(student.grades[course])
    if num_grades > 0:
        return round(av_sum_grade / num_grades, 2)
    else:
        return 0

students_list = [best_student, new_student]
course_specific = 'Python'
print(
    f'Средняя оценка за ДЗ по всем студентам в рамках курса {course_specific}: {av_grade_all_lecturers(lecturers_list, course_specific)}')
