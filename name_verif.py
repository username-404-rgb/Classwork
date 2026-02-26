import re

def sanitize():
    user_input = input("Enter your username: ")
    sanitized = re.sub(r'<script.*?>.*?</script>', '', user_input, flags=re.IGNORECASE | re.DOTALL)
    sanitized = sanitized.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    username = sanitized
    if len(username) <= 15:
        if len(username) >= 3:
            if username.isalnum() == True:
                print(f"Welcome, {username}!")
            else:
                print('Only use letters and numbers')
        else:
            print('Too Short')
    else:
        print('Too Long')
    
def valid_name(username):
    if len(username) <= 15:
        if len(username) >= 3:
            if username.isalnum() == True:
                print(username, "!!!")
            else:
                print('Only use letters and numbers')
        else:
            print('Too Long')
    else:
        print('Too Short')
    
sanitize()
