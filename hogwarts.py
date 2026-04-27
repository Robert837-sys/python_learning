"""
students=["Hermione","Harry","Ron"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

print(students[0])
print(students[1])
print(students[2])


for student in students:
  print(student)

for i in range(len(students)):
  print(i+1,students[i])


students={
  "Hermione":"Gryffindor",
  "Harry":"Gryffindor",
  "Ron":"Gryffindor",
  "Draco":"Slytherin"
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
  print(student,students[student],sep=", ")


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
  print(student["name"],student["house"],student["patronus"],sep=", ")

print("#")
print("#")
print("#")

for _ in range(3):
  print("#")
  
def main():
  print_column(3)
def print_column(height):
  for _ in range(height):
    print("#")

main()

def main():
  print_row(4)
def print_row(width):
  print("?"*width)

main()

def main():
  print_square(3)

def print_square(size):
  for i in range(size):
    for j in range(size):
      print("#",end="")
    print()

main()

"""
def main():
  print_square(3)

def print_square(size):
  for i in range(size):
    print_row(size)

def print_row(width):
  print("#"*width)

main()