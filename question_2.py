score = 0

print ("Welcome to the Programming Quiz(2)!")

#Question 2:
print("What does "==" do in Python?")
print("A. Assigns a value")
print("B. Compares values")
print("C. Checks data type")
print("D. Adds values")

answer =input("Your Answer: ").upper()

if answer == "B" or "B.":
    print("Correct Answer!")
    score +=1
else:
    print("Wrong Answer. The correct answer is B.")