class Calculator:
    def __init__(self):
        pass
    @classmethod
    def add(cls,x , y):
        """
        function the take two numbers and return the sum of them 

        Args:
            x (int): first number
            y (int): second number

        Returns:
            int : the sum of x and  y 
        """
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
