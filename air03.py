import sys

# Function to find any alone argument
def find_alone():
    counts = {}
    count = 0
    for i in range(0, len(array)):
        firstword = array[i]
        for i in range(0, len(array)):
            secondword = array[i]
            if firstword == secondword:
                count += 1
        counts[firstword] = count
        if count == 1:
            print(firstword)
        count = 0
    return array

# Function to manage IndexErrors
def if_errors():
    if len(sys.argv) < 4:
        print("Invalid input. Please provide at least three arguments.")
        sys.exit()

# Convert globales variables
array = sys.argv[1:]

# Call functions and print out
if_errors()
find_alone()