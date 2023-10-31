# Program receives a 1..12 month code and returns the month
# abbreviation as well as the number of days in the month.

monthdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
months    = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ]

monCode = int(input("Enter month code (1-12): "))

# Access array info
outMon  = months[monCode-1]
outDays = monthdays[monCode-1]

# Print response
print(outMon , "has" , outDays , "days")
