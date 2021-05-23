class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
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
       return "Имя: " + self.name + '\nФамилия:' + self.surname




class Lecturer(Mentor):
    def __init__(self, name, surname, average_value):
        Mentor.__init__(self, name, surname)
        self.average_value = average_value
    def __str__(self):
        return "Имя: " + self.name + '\nФамилия:' + self.surname + '\nСредняя оценка за лекции: ' + self.average_value



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

basic_student = Student('Johar', 'Buzuluk', 'helicopter')
basic_student.courses_in_progress += ['Git']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)

basic_reviewer = Reviewer('Slender' , 'Man')
basic_reviewer.courses_attached += ['Git']
basic_reviewer.rate_hw(basic_student, 'Git', 7)

cool_lecturer = Lecturer('Son', 'Tzy', '7')
cool_lecturer.courses_attached += ['Art of War']





print(best_student.grades)
print(cool_reviewer)
print(cool_lecturer)