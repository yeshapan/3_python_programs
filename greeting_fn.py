#PYQ Endsem
'''Write a Python function called greet_user that takes two arguments: name and greeting. The
function should print a personalized greeting message using the provided name and default to
"Hello" if greeting is not specified.'''

#user-defined function
def greet_user(name,greeting="Hello"):
    print(greeting,name)

name=input("Enter your name: ")
greeting=input("Enter greeting: ")
greet_user(name,greeting)
greet_user(name)

#Output
'''
Enter your name: Yesha
Enter greeting: Welcome to Hogwarts
Welcome to Hogwarts Yesha
Hello Yesha
'''
