score = 0

print("Welcome to the Programming Quiz(8)!")

#Question 8:
print("What does len([1, 2, 3, 4]) return?")
print("A  3")
print("B  4")
print("C  5")
print("D  Error")

answer =input("Your Answer: ").upper()

if answer == "B":
    print("Correct Answer!")
    score +=1
else:
    print("Wrong Answer. The correct Answer is B")