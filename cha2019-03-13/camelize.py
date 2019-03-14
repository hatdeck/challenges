import string

def camelize(str_):
    s = str_.translate(string.maketrans(string.punctuation, " " * len(string.punctuation)))
    return "".join(word.capitalize() for word in s.split(" "))
