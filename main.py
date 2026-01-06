score = 0

print ("Welcome to the Programming Quiz!\n")

#Question 1
print ("1. What is the output?")
print("print '5' + '5'")
print("A. 10 ")
print("B. 55")
print("C. Error")
print("D. 5 + 5")

answer = input("Your answer: ").upper()

if answer == "B":
    print ("Correct Answer!")
    score +=1
else:
    print ("Wrong. The correct choice was B")
