# In mathematics, parity refers to whether a number is either even or odd.

"""x=int(input("What's x? "))

if x % 2==0:
  print("even")
else:
  print("Odd")
  
def main():
  x=int(input("What's x? "))
  if is_even(x):
    print("Even")
  else:
    print("Odd")

def is_even(n):
  if n % 2==0:
    return True
  else:
    return False

main()

name=input("What's your name? ")
if name=="Harry":
  print("Gryffindor")
elif name=="Hermione":
  print("Gryffindor")
elif name=="Ron":
  print("Gryffindor")
elif name=="Draco":
  print("Slytherin")
else:
  print("Who?")
  
name=input("What's your name? ")
if name=="Harry" or name=="Hermione" or name=="Ron":
  print("Gryffindor")
elif name=="Draco":
  print("Slytherin")
else:
  print("Who?")


name=input("What's your name? ")
match name:
  case "Harry":
    print("Gryffindor")
  case "Hermione":
    print("Gryffindor")
  case "Ron":
    print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _:
    print("Who?")
"""

name=input("What's your name? ")
match name:
  case "Harry"|"Hermione"|"Ron":
    print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _:
    print("Who?")