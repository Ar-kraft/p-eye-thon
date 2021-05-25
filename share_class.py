

def avg(x):
    return sum(x) / len(x)

def get_courses_names(courses):#for output list of courses (student)
    result = ''
    for elem in courses:
        result += elem + ', '
    return result.removesuffix(', ')

def comp_of_st(c, v):#comparing function
    if c.average_grade > v.average_grade:
        return c
    else:
        return v


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0 #adde empty list for containg of grade value

    def rate_lw(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
    def __str__(self):
        self.courses_to_print = get_courses_names(self.courses_in_progress)
        return "Имя: " + self.name + '\nФамилия:' + self.surname + '\nКурсы в процессе обучения: ' + self.courses_to_print + '\n Средняя оценка за домашнее задание: ' + self.average_grade.__str__()

    def calc_avg(self):
        self.qqq = getInner(self.grades)
        self.average_grade = avg(self.qqq)



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

def getInner(z):
    result = []
    for elem in z.values():
        result.extend(elem)
    return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.rates = {}
        self.average_grade = 0
    def __str__(self):

        return "Имя: " + self.name + '\nФамилия:' + self.surname + '\n Средняя оценка за лекции: ' + self.average_grade.__str__()

    def calc_avg(self):#inside calcuclation of rating
        self.qqq = getInner(self.rates)
        self.average_grade = avg(self.qqq)



cool_lecturer = Lecturer('Son', 'Tzy' )
cool_lecturer.courses_attached += ['Git']
bad_lecturer = Lecturer('Ahhhmed', 'Tzy' )
bad_lecturer.courses_attached += ['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

basic_student = Student('John', 'Buzuluk', 'helicopter')
basic_student.courses_in_progress += ['Git']
basic_student.rate_lw(cool_lecturer, 'Git', 13)
basic_student.rate_lw(bad_lecturer, 'Git', 2)

foreign_student = Student('Ahmed', 'Kugelbaum', 'cyborg')
foreign_student.courses_in_progress += ['Git']
foreign_student.rate_lw(cool_lecturer, 'Git', 15)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 8)


list_of_students = [basic_student, best_student]

def avg_grades_all_students(students, course):#рассчет средней оценки по определнному курсу
    students_on_course = []#empty ;ist
    for student in students:
        if course in student.courses_in_progress:#cheking in student class of course type
            for w in student.grades[course]:
                students_on_course.append(w)#add to end of new list
    return avg(students_on_course)#using of average calculation function


print(basic_student.grades)
print(best_student.grades)
best_student.calc_avg()
cool_lecturer.calc_avg()
print(best_student)

print(cool_reviewer)
print(cool_lecturer)

print('Best Lect: ' + comp_of_st(cool_lecturer, bad_lecturer).__str__())

print(avg_grades_all_students(list_of_students, 'Python'))


