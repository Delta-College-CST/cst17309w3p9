# This program simulates a lottery game that selects
# 6 numbers randomly from the range 1..47

import random

selectiondomain  = 47
numberSelections = 6

# Create an array containing 1..selectionDomain.  Note
# initially index range is 0..selectionDomain-1 
selections = []
for n in range (selectiondomain):
    selections.append(n+1)
    
# Loop to pick desired number of lottery choices. Pick using
# a random index.  Once picked, the number at the index is
# removed.
for picks in range(numberSelections):
    index   = random.randrange(0,len(selections))
    print(selections[index]);
    selections.pop(index)

    
