import sys

# Function to sort a list of integers by Quicksort
def quicksort(liste):
    if len(sys.argv) <= 2:
        return liste
    pivot = liste.pop()
    petit = []
    grand = []
    for number in liste:
        if number < pivot:
            petit.append(number)
        else:
            grand.append(number)
    return quicksort(petit)+[pivot]+quicksort(grand)

def without_bracket(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# Convert globales variables
liste = sys.argv[1:]

# Resolution
array = quicksort(liste)
without_bracket(array)

# Print out result
print(array)