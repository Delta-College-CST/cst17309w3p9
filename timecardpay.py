# This solution includes a list of shift hours worked over various days.  
# It iterates through the list to accumulate total pay.

salary = 12.95     # Per hour wage

# List of shifts worked (hours)
timecard = [3, 7, 5, 12, 4, 2, 3, 1, 8]

# Loop through and accumulate total hours worked
totalHours = 0
for shift in timecard:
    totalHours += shift
	
# Determine total payment

pay = totalHours * salary

# Output
print("$%6.2f" % (pay))
