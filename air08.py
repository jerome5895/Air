import sys

# Function to separate argument by string 
def separate(argument):
    separator = "fusion"
    if separator in argument:
        index = argument.index(separator)
        array1 = argument[:index]
        array2 = argument[index+1:]
    else:
        print("Invalid input. No 'fusion' word provided.")
        sys.exit()
    return array1, array2

# Function to sort and concatenate two arrays
def sorted_fusion(array1, array2):
    new_array = array1 + array2
    n = len(new_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if new_array[j] < new_array[min_index]:
                min_index = j
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    return new_array

# Convert globales variables
argument = sys.argv[1:]

# Resolution
array1, array2 = separate(argument)
new_array = sorted_fusion(array1, array2)

# Print out result
print(new_array)