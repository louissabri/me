"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# this is a list
some_words = ["what", "does", "this", "line", "do", "?"]
# this is a loop, it will go through the list and print the word listed
for word in some_words:
    print(word)  # it did that
# Ben said same as above, this is the same just with a different variable name (word vs x)
for x in some_words:
    print(x)
# print the list
print(some_words)
# Len returns the number of items in an object. So if the number of items in a word (string) is greater than 3, it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words") # I was kinda wrong, Amber kindly explained that the Len function is actually counting the number of items in the list, not the number of characters in each individual list item.

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # platform.uname gets information about the current OS. Printing this will print the information. This function will print information about the current operating system.
    print(platform.uname())


usefulFunction() # It did what I thought it would!
