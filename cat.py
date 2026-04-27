"""
print("meow")
print("meow")
print("meow")

i=3
while i < 3:
  print("meow")
  i=i+1
  
for i in [0,1,2]:
  print('meow')

for i in range(3):
  print("meow")

print("meow\n"*3,end="")

while True:
  n=int(input("What's n? "))
  if n < 0:
    continue
  else:
    break

for _ in range(n):
  print("meow")

"""
def main():
  meow(get_number())

def get_number():
  while True:
    n=int(input("what's n? "))
    if n>0:
      return n
    
def meow(n):
  for _ in range(n):
    print("meow")

main()
  