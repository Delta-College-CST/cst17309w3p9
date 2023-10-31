# This program magically answers any question asked by the user.

import random

answerlist = []
answerfile = open("answers.txt", "r")     # Open file and load into array
for oneAnswer in answerfile:
    answerlist.append(oneAnswer)
listsize = len(answerlist)                # Retain length of array

keepAsking = "y"                          # Initialize continuation prompt

# Main program loop.  While continuation is "y"
# continue to ask and provide random answers
while keepAsking == "y":
    question = input("Enter any question:  ")
    randIndex = random.randrange(0,listsize)
    print(answerlist[randIndex])

    keepAsking = input("Ask another question (y or n)?  ")

print("Thank you for using the Magic Answering Machine.")



    









