import sys

# Function to sort a list of integers by Quicksort
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = []
    right = []
    for x in array[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)

# Function to print out without "" or ", "
def without_bracket(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# Convert globales variables
array = [int(liste) for liste in sys.argv[1:]]

# Resolution
array = quicksort(array)

# Print out result
without_bracket(array)