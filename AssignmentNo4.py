def fact(n):
    if n == 0: return 1
    else: return n * fact(n-1)

print("Enter a number to calculate its factorial")
num = int(input())
print("The factorial of", num, "is", fact(num))