score = 0

print("Welcome to the Programming Quiz(6)!")

#Question 6:
print("What does  range(3)  produce?")
print("A. 1, 2, 3")
print("B. 0, 1, 2")
print("C. 0, 1, 2, 3")
print("D. 3")

answer =input("Your Answer: ").upper()

if answer == "B" or "B.":
    print("Correct Answer!")
    score +=1
else:
    print("Wrong Answer. The correct Answer is B.")