import unittest


class TestString(unittest.TestCase):
    def test_split(self):
        string_to_cut = "Bonjour les gars"
        separators = [' ', '\t', '\n']
        words = []
        current_word = ""
        for char in string_to_cut:
            if char in separators:
                if current_word:
                    words.append(current_word)
                    current_word = ''    
            else:
                current_word += char
        if current_word:
            words.append(current_word)
        return words
        

if __name__ == "__main__":
    if words == ["Bonjour", "les", "gars"]
    unittest.main()
