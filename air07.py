import sys

array = [int(array) for array in sys.argv[1:-1]]
new_element = [int(new_element) for new_element in sys.argv[-1]]


def selection_sort(array, new_element):
    new_array = array + new_element
    n = len(new_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if new_array[j] < new_array[min_index]:
                min_index = j
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    return new_array

new_array = selection_sort(array, new_element)

print(new_array)