class Calculator:
    def __init__(self):
        self.experssion =  ''
        return
    @classmethod
    def add(cls,x , y):
        return x + y 
    
    @classmethod
    def subtract(cls,x , y):
        return x - y
    
    @classmethod
    def multiply(cls,x , y):
        return x * y
    
    @classmethod
    def divide(cls,x , y):
        if y == 0:
            return "invalid devision by zero"
        return x / y 
    
    def set_experssion(self,experssion):
        self.experssion = experssion
