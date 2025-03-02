"""
1. Split()
-> The split() method is used to break a string into a list
of substrings based on a specified delimiter

string.split(separator, maxsplit)

2. join()
-> The join() method is used to combine a list of strings into a single string. Inserting a specified separator 
blw them.

"""


text = "Python is easy to learn"
words = text.split()
print(words)

sentence = " ".join(words)
print(sentence)