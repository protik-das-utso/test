class Student:

    def __init__(self, name, age, dob, address, phone, course):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.phone = phone
        self.course = course
    def show(self):
        return f"Student Name: {self.name}\nAge: {self.age}\nDate of Birth: {self.dob},\nAddress: {self.address}\nPhone: {self.phone}\nCourse: {self.course}"



student = [1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1]
index = 0

def addStudent():
    student[0] = Student(name, age, dob, address, phone, course)




print("1. Add Student\n2. Show Student")
choice = input("Enter Your Choice")

if choice == 1 :
    name = input("Name: ")
    age = input("Age: ")
    dob = input("Date of Birth: ")
    address = input("Address: ")
    phone = input("phone: ")
    course = input("Course: ")
    addStudent(name, age, dob, address, phone, course)
elif choice == 2:
    print(student[0].show())