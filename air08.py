import sys

argument = sys.argv[1:]


def separate(argument):
    separator = "fusion"
    if separator in argument:
        index = argument.index(separator)
        array1 = " ".join(argument[:index])
        array2 = " ".join(argument[index+1:])
    else:
        print("Invalid input. No 'fusion' word provided.")
        sys.exit()
    return array1, array2

def concatenete(array1, array2):
    new_list = []
    for list in [array1], [array2]:
        for element in list:
            new_list.append(element)
    return new_list


array1, array2 = separate(argument)
new_list = concatenete(array1, array2)
print(f"{new_list}")