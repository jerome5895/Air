import sys


def to_left():
    argument = sys.argv[1:]
    new_string = ""
    changed_word = ""
    for index, word in enumerate(argument):
        if index != 0:
            new_string += word + " "
        else:
            changed_word = word
    new_string += changed_word
    return new_string

new_string = to_left()
print(new_string)