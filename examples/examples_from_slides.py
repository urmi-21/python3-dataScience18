'''
BCBGSO Basic Python workshop 3/23/2018
Functions

@author urmi
'''

i=0
for i in range(10):
    print (i)


#if else
grades=True
gf=False
gaming=True
if (grades and gf and not gaming):
	print ("no money")
elif(grades and gaming and not gf):
	print ("no social life")
elif(not grades and gaming and gf):
	print ("no career")
elif(grades and gf and gaming):
	print ("Impossible")


#break continue
mylist = [1,2,3,4,5,6,7,8]
for i in mylist:
    if (i % 2==0):
        continue
    if (i == 7):
        break
    print (i)

#sum inside loop
n=5
totalsum=0			#important to initialize sum
for x in range(n+1):
    totalsum=totalsum+x		#adds numbers 0 till 5
print (totalsum)


#scopes
x1=10		#a has global scope
def func():
    x2=10
    x1=5
    print ("x2 in func:",x2)	#prints b=10
    print ("x1 in func:",x1)		#prints a=5
    
func()
print ("x1 in main:",x1)		#prints a=10	
print ("x2 in main:",x2	)	#error b is not defined, its scope ended with the function
