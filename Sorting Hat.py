print("=============")
print("=Sorting Hat=")
print("=============")
print(" ")

Gryffindor = 0
Slytherin = 0
Ravenclaw = 0
Hufflepuff = 0

#Question 1

print("Q1) Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
answer = int(input("Enter your answer (1-2): "))

if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Slytherin += 1
  Hufflepuff += 1
else:
  print("Wrong input.")

#Question 2
print(" ")
print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input("Enter your answer (1, 4): "))

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print("Wrong input.")


#Question 3

print(" ")
print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input("Enter your answer (1, 4): "))

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer == 3:
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print(" ")
if Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
  print("You are a Ravenclaw!")
elif Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff:
  print("You are a Gryffindor!")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
  print("You are a Slytherin!")
elif Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
  print("You are a Hufflepuff!")
else:
  print("Error.")