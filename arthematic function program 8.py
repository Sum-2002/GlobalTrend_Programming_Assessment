def arithmetic_operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError("Invalid operator. Must be one of (+, -, *, /).")


print(arithmetic_operation(2, 3, "+")) 
print(arithmetic_operation(4, 2, "-"))  
print(arithmetic_operation(5, 6, "*")) 
print(arithmetic_operation(8, 2, "/"))  
