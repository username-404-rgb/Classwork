def loop():
    valid_age()
    loop()
def valid_age():
    try:
        age_input = int(input("Please enter your age: "))
        if 0 <= age_input <= 120:
            print('Your age is', {age_input})
            quit()
        else:
            raise ValueError("Age must be between 0 and 120.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
loop()