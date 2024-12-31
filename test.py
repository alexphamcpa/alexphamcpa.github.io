import pandas as pd
import collections

def findDuplicateCharacters(s):
    return [item for item, count in collections.Counter(s).items() if count > 1]

def main():
    s = "Hello World"
    duplicates = findDuplicateCharacters(s)
    print("There are character duplicates in the string '{}': {}".format(s, duplicates))

if __name__ == "__main__":
    main()

# generate a function to validate email addresses        
import re
def isValidEmail(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

