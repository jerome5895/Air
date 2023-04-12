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

# Function to manage value errors
def if_only_numb(array):
    for x in array:
        if not isinstance(x, int):
            print("Invalid input. Please provide only numbers.")
            sys.exit()
    return array

# Function to manage index errors
def if_index_err():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two numbers.")
        sys.exit()

# Function to print out without "" or ", "
def without_bracket(new_array):
    for i in range(len(new_array)):
        print(new_array[i], end=" ")
    print()

# Convert globales variables
array = [int(array) for array in sys.argv[1:]]

# Resolution
if_index_err()
array = if_only_numb(array)
new_array = quicksort(array)

# Print out result
without_bracket(new_array)