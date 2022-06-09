# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
# -- > "./story.txt"

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        lines = f.read()
    
    return lines


def count_words(filename):
    text = read_file_content(filename) 
    # [assignment] Add your code here
    # Creating an empty dictionary
    freq = {}

    # split string to individual word
    for item in text.split():
 
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
   # for key, value in freq.items():
         
    return (freq)

filepath= input("Enter file path ")
print(count_words(filepath))