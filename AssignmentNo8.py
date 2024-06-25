def read_integer_from_user():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            num = int(user_input)
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")


integer = read_integer_from_user()
print("You entered:", integer)
