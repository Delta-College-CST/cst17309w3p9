# This program performs a statistical analysis of a
# set of positive integer values.  It reads the data from
# an external file and stores it in an array.  The specific
# statistical operations are managed via functions.

FILENAME = "data.txt"

# Open file for reading
def buildListFromFile(thelist):
    datafile = open(FILENAME, "r")
    for inputStrItem in datafile:
        element = int(inputStrItem)
        thelist.append(element)
    datafile.close()
    return thelist

# Calculate average value in a list of integers
def calcAverage(dataList):
    sum = 0
    for item in dataList:
         sum += item
    ave = sum / len(dataList)
    return ave

# Determine largest value in list of integers
def getMax(dataList):
    max = -99999999
    for item in dataList:
         if item > max:
             max = item
    return max

# - - - - - - - - -  MAIN ROUTINE  - - - - - - - - - #
list = []
list = buildListFromFile(list)

average = calcAverage(list)
print("Average: %6.2f" % (average))

maxValue = getMax(list)
print("Maximum:",maxValue)

