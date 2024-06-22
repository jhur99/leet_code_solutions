# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, 
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        new_string = ""
        for i in range(length):
            new_string = new_string + word1[i] + word2[i]
        if len(word1) == len(word2):
            return new_string
        if len(word1) < len(word2):
            new_string += word2[length:]
            return new_string
        else:
            new_string += word1[length:]
            return new_string
    
print(mergeAlternately("hola", "mundo"))