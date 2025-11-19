import re

email = "test@gmail.com"

pattern = r"^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,3}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
