import datetime

class Person:
    # Class Attribuate
    schoolName = "Test School !"
    
    # init method or constructor 
    def __init__(self, name, age, gender):
        self.name = name # Attribuate
        self.age = age
        self.gender = gender
        
    # .............................................Instance method
    def introduce(self):
        return f"My name is {self.name}"
    
    # ..............................................Class Method
    @classmethod
    def get_school_name(cls):
        return Person.schoolName
        # return datetime.datetime.now()
    
person1 = Person("Protik", 23, "Male")
print(person1.name, person1.age, person1.gender)
print(person1.introduce())
print(Person.get_school_name())



class TimeUtilityManeger:
    #  ..............................................Static Method
    @staticmethod
    def get_current_time():
        return datetime.datetime.now()
    
print(TimeUtilityManeger.get_current_time())