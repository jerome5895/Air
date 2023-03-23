import sys

list = sys.argv[1:]

if len(list) <= 1:
        print("Invalid input. Please provide at least two numbers.")
        sys.exit()

def quicksort(list):
    pivot = list.pop()
    petit = []
    grand = []
    for number in list:
        if number < pivot:
             petit.append(number)
        else:
             grand.append(number)
    return quicksort(petit) + [pivot] + quicksort(grand)


quicksort(list)