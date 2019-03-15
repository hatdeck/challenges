"""
You must create a method that can convert a string from any format into PascalCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.

For example: (Input --> Output)

"example name" --> "ExampleName"
"your-NaMe-here" --> "YourNameHere"
"testing ABC" --> "TestingAbc"
"""


import string



def camelize(str_):
    s = str_.translate(string.maketrans(string.punctuation, " " * len(string.punctuation)))
    return "".join(word.capitalize() for word in s.split(" "))
