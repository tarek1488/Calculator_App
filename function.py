def compute_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return 'division by zero'
        else:
            return num1 / num2
    else:
        return 'Invalid operation'

def calc(word):
    expression = word.split()
    
    operations = ['*', '/', '+', '-']
    
    if expression[-1] in operations or expression[0] in operations:
        return "error incomplete expression"
    
    for i in range(len(expression) - 1):
        if expression[i] in operations and expression[i+1] in operations:
            return "error"
    
    num_of_operations = len(expression) // 2
    
    current_result = float(expression[0])
    op_index = 1
    while num_of_operations > 0:
        op = expression[op_index]
        num = float(expression[op_index + 1])
        result = compute_operation(current_result, num, op)
        
        if result == 'division by zero' or result == 'Invalid operation':
            return result
        
        current_result = result
        op_index += 2
        num_of_operations -= 1
    
    return current_result