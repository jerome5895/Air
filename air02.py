import sys

# Function to concatenete array to a string
def array_to_string(array, separateur):
    new_string = ""
    for string in array:
        new_string += string + separateur
    return new_string

# Function to manage IndexErrors
def if_errors():
    if len(sys.argv) < 4:
        print("Invalid input. Please provide at least two arguments and one separation.")
        sys.exit()

# Call functions and convert globales variables
if_errors()
array = sys.argv[1:-1]
separateur = sys.argv[-1]
new_string = array_to_string(array, separateur)

# Print out result
print(new_string)