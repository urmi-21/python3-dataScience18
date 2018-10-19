'''
BCBGSO intermediate Python workshop 10/19/2018
Example reading files

@author urmi
'''

#Note: The function input() lets user give input during runtime
#the number entered by user is stored in the variable "number"
number = int(input("Enter any integer: "))
print ("You entered:" + str(number))

print ("Choose an option below then press enter:")

print ("1. Find square of the number")
print ("2. Find cube of the number")
print ("3. Find any other power of the number")

#the option entered by user is stored in the variable "option"
option = int(input("Enter option (1,2,3): "))

#use if-else statements and determine which code block to execute based on user's input
if option==1:
    print ("Square = "+str(number**2))
elif option==2:
    print ("Cube = "+str(number**3))
elif option==3:
    power = int(input("Enter the power: "))
    if power > 5:
        print ("power is to high...")
    else :
        print (str(number)+" to power "+str(power)+" is = "+str(number**power))
else:
    print ("Not a valid option")
        