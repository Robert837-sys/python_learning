import re
"""
email=input("What's your email? ").strip()
if "@" in email and "." in email:
  print("valid")
else:
  print("invalid")


email=input("what's your email? ").strip()
username,domain=email.split("@")

if username and "." in domain:
  print("Valid")
else:
  print("Invalid")


email=input("what's your email? ").strip()
username,domain=email.split("@")

if username and domain.endswith(".edu"):
  print("valid")
else:
  print("Invalid")

email=input("what's your email? ").strip()
if re.search(r".+@.+\.edu",email):
  print("Valid")
else:
  print("Invalid")


email=input("what's your email? ").strip()
if re.search(r"^[^@]+@[^@]+\.edu$", email):
  print("valid")
else:
  print("Invalid")
"""

# email=input("what's your email? ").strip()
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#   print("valid")
# else:
#   print("Invalid")

email=input("What's your email? ").strip()
# Notice that \w is the same as [a-zA-Z0-9_]. Thanks, hard-working programmers!
#Notice that [a-zA-Z0-9_] tells the validation that characters must be between a and z, between A and Z, between 0 and 9 and potentially include an _ symbol. Testing the input, you’ll find that many potential user mistakes can be indicated.
"""
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character
"""
# if re.search(r"^\w+@\w+\.edu$",email):
#   print("valid")
# else:
#   print("Invalid")


# if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
#   print("valid")
# else:
#   print("Invalid")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")