
#high level of abstract functions below:
def avg(x): #formula for main calculaing of AVeraGE value of smth
    return sum(x) / len(x)

def get_courses_names(courses):#for output readable format of list of courses (Student class) to print
    result = ''
    for elem in courses:
        result += elem + ', ' #adding space and coma between
    return result.removesuffix(', ')#string method of cutting last suffix

def comp_of_st(c, v):#main comparing function for those classes who have it (average_grade)
    if c.average_grade > v.average_grade:
        return c
    else:
        return v

def getInner(z):#fucntion for unpacking from brackets
    result = []
    for elem in z.values():
        result.extend(elem)
    return result

class Student:#added self.average_grade
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0 #add empty list for containg of grade value

    def rate_lw(self, lecturer, course, rate):#just adapted def rate_hw for class Student to class Lecturer
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
    def __str__(self):#Reloade method __str__
        self.courses_to_print = get_courses_names(self.courses_in_progress)#
        self.courses_to_print_2 = get_courses_names(self.finished_courses)
        return "Имя: " + self.name + '\nФамилия:' + self.surname + \
               '\nКурсы в процессе обучения: ' + self.courses_to_print + \
               '\nСредняя оценка за домашнее задание: ' + self.average_grade.__str__() +\
               '\nЗавершенные курсы: ' + self.courses_to_print_2

    def calc_avg(self):#function
        self.qqq = getInner(self.grades)
        self.average_grade = avg(self.qqq)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                course in student.courses_in_progress:
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
        self.average_grade = 0
    def __str__(self):

        return "\nИмя: " + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' \
               + self.average_grade.__str__()

    def calc_avg(self):#inside calcuclation of rating
        self.qqq = getInner(self.rates)
        self.average_grade = avg(self.qqq)


#new examples of different classe below


cool_lecturer = Lecturer('Son', 'Tzy' )
cool_lecturer.courses_attached += ['Git']

bad_lecturer = Lecturer('Ahmed', 'Exploev' )
bad_lecturer.courses_attached += ['Git']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.rate_lw(cool_lecturer, 'Git', 7)
best_student.rate_lw(bad_lecturer, 'Git', 9)
best_student.finished_courses += ['Введение в программирование']


basic_student = Student('John', 'Buzuluk', 'helicopter')
basic_student.courses_in_progress += ['Git']
basic_student.courses_in_progress += ['Python']
basic_student.rate_lw(cool_lecturer, 'Git', 8)
basic_student.rate_lw(bad_lecturer, 'Git', 5)

# foreign_student = Student('Izekiel', 'Kugelbaum', 'cyborg')
# foreign_student.courses_in_progress += ['Git']
# foreign_student.rate_lw(cool_lecturer, 'Git', 15)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(basic_student, 'Git', 6)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(basic_student, 'Python', 7)


list_of_students = [basic_student, best_student]#sample list for cheking students
list_of_lecturers = [cool_lecturer, bad_lecturer] #sample list for cheking lecturers

def avg_grades_all_students(students, course):  #расчет средней оценки по определнному курсу
    students_on_course = []  #empty list
    for student in students:
        if course in student.courses_in_progress:  #cheking in student class of course type
            for w in student.grades[course]:
                students_on_course.append(w)#add to end of new list
    return avg(students_on_course)#using of average calculation function

def avg_grades_all_lecturers(lecturers, course):  #расчет средней оценки по определнному курсу
    lecturers_on_course = []  #empty list
    for lecturer in lecturers:
        if course in lecturer.courses_attached:  #cheking in  class of attached course type
            for y in lecturer.rates[course]:
                lecturers_on_course.append(y)#add to end of new list
    return avg(lecturers_on_course)#using of average calculation function


best_student.calc_avg()#initialising best student value
basic_student.calc_avg()
cool_lecturer.calc_avg()#initialising cool lecturer value
bad_lecturer.calc_avg()#initialising cool lecturer value


print("\n ________________________")
print(cool_reviewer)
print("\n ________________________")
print(cool_lecturer)
print("\n ________________________")
print(best_student.grades)

print("\n ________________________")
print(best_student)
print("\n ________________________")

print('Сравнение лекторов(лидер): ' + comp_of_st(cool_lecturer, bad_lecturer).__str__())

print("\n ________________________")
print('Сравнение студентов(лидер): \n' + comp_of_st(best_student, basic_student).__str__())
print("\n ________________________")
print("\n Среднее значение оценок студентов - Python")
print(avg_grades_all_students(list_of_students, 'Python'))
print("\n ________________________")
print("\nСреднее значение оценок лекторов - Git")
print(avg_grades_all_lecturers(list_of_lecturers, 'Git'))
print("\n ________________________")
print(cool_lecturer.rates)
print(bad_lecturer.rates)
