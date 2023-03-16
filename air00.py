import sys

# Function to separate argument
def separation(string_a_couper, separateurs):
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

# Function to manage argument errors
def errors(string_a_couper):
    if len(sys.argv) != 2:
        print("Invalid input. Please provide one argument.")
        sys.exit()

# Function to print out without []
def without_brackets(words):
    for i in range(len(words)):
        print((words[i]), end='\n')
    print()

# Convert globales variables
string_a_couper = sys.argv[1]
separateurs = [' ', '\t', '\n']

# Resolution
errors(string_a_couper)
words = separation(string_a_couper, separateurs)

# Print out result
without_brackets(words)