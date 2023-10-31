# This reads parallel arrays containing Delta CST course codes.
# The user can enter a course code and access the course name.

courseid       = []    
coursedescript = []

# Load course info to parallel arrays
coursefile = open("cstcourses.txt", "r")   
for courseinfoline in coursefile:
    incode, indescript = courseinfoline.split(",")
    courseid.append(incode)
    coursedescript.append(indescript)

doAgain = "y"
while doAgain == "y":
    
    # Validate existence of user ID
    targetID = input("Enter Delta CST Course ID: ")

    # Seek index of course ID
    listLength = len(courseid)    # Get limit for searching
    index = -1
    for i in range(listLength):
        if courseid[i] == targetID:
            index = i

    # If course ID found, return course name.  Otherwise an error msg.
    if index >= 0:
        resultOutput = targetID + ": " + coursedescript[index]
    else:
        resultOutput = "Course ID not found"

    # Write output
    print()
    print(resultOutput)

    doAgain = input("Do you wish to search again (y or n)? ")
    print()

print("Thanks for you interest in Delta CST")

                


