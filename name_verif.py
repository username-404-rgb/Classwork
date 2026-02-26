import re

def sanitize():
    user_input = input("Enter your username: ")
    sanitized = re.sub(r'<script.*?>.*?</script>', '', user_input, flags=re.IGNORECASE | re.DOTALL)
    sanitized = sanitized.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    print (sanitized)
    
def valid_name():
    try:
        username = input("Enter your username: ")
        if 0 <= age_input <= 120:
            print('Your username has been set to', username)
            quit()
        else:
            raise ValueError("Age must be between 0 and 120.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None
sanitize()

#print(f"Welcome, {username}!")

