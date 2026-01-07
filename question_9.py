score = 0

print("Welcome to the Programming Quiz(9)!")

print("How do you create a list in Python?")
print("A  {1, 2, 3}")
print("B  (1, 2, 3)")
print("C  [1, 2, 3]")
print("D  <1, 2, 3>")

answer =input("Your Answer: ").upper()

if answer == "C":
    print("Correct Answer!")
    score +=1
else:
    print("Wrong Answer. The Correct Answer was C.")