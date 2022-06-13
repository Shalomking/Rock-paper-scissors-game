

    #f = open('story.txt', 'r') 

        #print(f.read())

        #f.close()

from ast import If
from enum import unique
from importlib.resources import contents


with open('story.txt', 'r') as f:
    #for line in f:
        #print(line)
         print(f.read())

def read_file_content(filename):
    with open("story.txt") as file_object:
        filename = file_object.read()
        return filename
def count_words():
    text = read_file_content("story.txt")
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count_words())