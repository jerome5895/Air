import sys

# Function to separate argument
def separation():
    string_a_couper = sys.argv[1]
    separateurs = [' ', '\t', '\n']
    words = []
    current_word = ""
    for char in string_a_couper:
        if char in separateurs:
            if current_word:
                words.append(current_word)
                current_word = ''    
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

def without_sep(words):
    nv_separateur = sys.argv[2]
    array = []
    found_separateur = False
    for word in words:
        if word == nv_separateur:
            found_separateur = True
            break
        array.append(word)
    if found_separateur:
        words = words[len(array)+1:]
    else:
        words = []
    return array, words


# Function to print out without []
def without_brackets(array):
    for i in range(len(array)):
        print((array[i]), end=' ')
    print()


words = separation()
array = without_sep(words)
without_brackets(array)