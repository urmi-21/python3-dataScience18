'''
BCBGSO Basic Python workshop 3/23/2018
Functions

@author urmi
'''

#####These are my function definitions#####

#this function takes no argument, returns None
def printWelcome():
    print ("Hi, Welcome!")
#this function takes no argument, returns a str object
def getName():
    name=input("Please Enter your name: ")
    return name
#this function takes a str object, returns None
def printMessage(name):
    print ("How are you, "+name)
#this function takes no argument, returns None
def printGoodbye():
    print ("Goodbye...")




#####Call the functions######
printWelcome()
user=getName()
printMessage(user)
printGoodbye()

##usage of lamda function
def mult(n):
    return lambda x: x*n

double=mult(2)
double(3)
triple=mult(4)
triple(4)

