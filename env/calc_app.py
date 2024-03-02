from flask import Flask
class Student:
    #class attributes varibale for all class objects shared among all objects
    #like static in c++
    no_of_students = 0
    def __init__(self,name , age = 0 , courses = 'none'):
        #instance attributes or object attributes
        self.__name = name
        self.__age = age
        self.__courses =  courses
        Student.no_of_students += 1
    
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name
        
    def get_age(self):
        return self.__age
    
    def set_name(self,new_age):
        self.__name = new_age
    
    # 1 - instance method
    def describe(self):
        print(f'student name is: {self.__name} \n my age is {self.__age}')
    # 2-class method
    @classmethod
    def initfrombirthyear(cls,name,birthyear):
        return "hello"
    
    
    def __repr__(self):
        return f'student name is : {self.__name}'
    
        
    
student_1 = Student("islam",30,['cs','maths']) 
student_1.describe()
