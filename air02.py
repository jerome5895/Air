import sys


def array_to_string(array, separateur):
    for string in array:
        string += separateur
    return string



array = sys.argv[1:-2]
separateur = sys.argv[-1]
string = array_to_string(array, separateur)

print(string)
