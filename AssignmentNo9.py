def safe_divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None


dividend = 10
divisor = 0

result = safe_divide(dividend, divisor)
if result is not None:
    print("Result of division:", result)
else:
    print("Division is not possible.")
