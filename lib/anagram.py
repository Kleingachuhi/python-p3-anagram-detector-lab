# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [item for item in word_list if sorted(item) == sorted(self.word)]

perfect_match = Anagram(["listen", "silent", "hippopotamus"])