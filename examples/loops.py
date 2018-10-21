'''
BCBGSO intermediate Python workshop 10/19/2018
Example reading files

@author urmi
'''
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

number = int(input("Enter any integer less than 20: "))
print ("You entered:" + str(number))

print ("Printing first " + str(number)+" primes using for loop")
#Note: the range(n,m) function generates a list of integers in range [n,m)
#e.g. range(0,5): [0, 1, 2, 3, 4]
#range(m) generates list of integers in range [0,m)
#e.g. range(5): [0, 1, 2, 3, 4]
for i in range(0,number): 
    print (primes[i])

print ("Printing first " + str(number)+" primes using while loop")
i=0
while i<number:
    print (primes[i])
    i=i+1

print ("Printing first " + str(number)+" primes using for loop with break")
i=0
for p in primes: 
    print (p)
    i=i+1
    if i == number:
        break

print ("Printing first " + str(number)+" primes using while loop with break")
i=0
while True:
    print (primes[i])
    i=i+1
    if i == number:
        break

#using continue is not efficient in this case as the loop continues to run, doing nothing, until it reaches end of the list
print ("Printing first " + str(number)+" primes using for loop with continue")
i=0
for p in primes:
    if i >= number:
        continue
    print (p)
    i=i+1
    
print ("Printing first " + str(number)+" primes using while loop with continue")
i=0
while i< len(primes):
    #Note: the statement i=i+1. We have to increment i with each iteration otherwise we will no reach the stopping criteria and loop will continue indefinitely !!!
    #If we choose to skip a code block we still must increment i by 1
    if i >= number:
        i=i+1
        continue
    print (primes[i])
    i=i+1
    
