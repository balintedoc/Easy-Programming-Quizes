score = 0

print("Welcome to the Programming Quiz(4)!")

#Question 4:
print("Which keyword is used to handle errors?")
print("A. catch")
print("B. error")
print("C. try")
print("D. fix")

answer =input("Your Answer: ").upper()

if answer == "C" or "C.":
    print("Correct Answer!")
    score +=1
    print("Your score is: 1")
else:
    print("Wrong Answer. The correct Answer is C.")