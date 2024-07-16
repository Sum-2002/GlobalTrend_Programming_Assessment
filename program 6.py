def safe_divide(dividend, divisor):
    if divisor == 0:
        return "Error: Cannot divide by zero!"
    else:
        return dividend / divisor

print(safe_divide(10, 2)) 
print(safe_divide(10, 0)) 
