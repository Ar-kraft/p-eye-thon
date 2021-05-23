class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
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
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.rates = {}
    def __str__(self):
        return "Имя: " + self.name + '\nФамилия:' + self.surname + '\n Рейтинг'





cool_lecturer = Lecturer('Son', 'Tzy' )
cool_lecturer.courses_attached += ['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

basic_student = Student('John', 'Buzuluk', 'helicopter')
basic_student.courses_in_progress += ['Git']
basic_student.rate_lw(cool_lecturer, 'Git', 13)

foreign_student = Student('Ahmed', 'Kugelbaum', 'cyborg')
foreign_student.courses_in_progress += ['Git']
foreign_student.rate_lw(cool_lecturer, 'Git', 15)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)


def avg(x):
    return sum(x) / len(x)




print(basic_student.grades)
print(best_student.grades)

print(cool_reviewer)
print(cool_lecturer)



print(cool_lecturer.rates)

