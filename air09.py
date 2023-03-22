import sys


def to_left():
    argument = sys.argv[1:]
    new_string = ""
    changed_word = ""
    for word in argument:
        if word != argument[0]:
            new_string += word + " "
        else:
            changed_word = word
            if new_string == argument[1:]:
                new_string += changed_word
    return new_string

new_string = to_left()
print(new_string)