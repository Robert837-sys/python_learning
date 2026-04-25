"""def hello():
  print("Hello")

name=input("What's your name? ")
hello()
print(name)

def hello(to):
  print("hello,", to)

name=input("What's your name? ")
hello(name)

def hello(to="world"):
  print("hello,",to)

name=input("What's your name? ")
hello(name)
hello()
"""
def main():
  name=input("What's your name? ")
  hello(name)

  hello()

def hello(to="world"):
  print("hello,",to)

main()