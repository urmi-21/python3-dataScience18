'''
BCBGSO intermediate Python workshop 10/19/2018
Example reading files

@author urmi
'''

#read the file names.txt
#f is the file object
with open('../data/names.txt','r') as f:
    names= f.read().splitlines()    #read().splitlines removes any trainling \n or \r

print ("total names =",str(len(names)))

#How many names contain '3'
names_3=[]
for x in names:
    if '3' in x:
        #add the names to list names_3
        names_3.append(x)
print ("Names containing 3:",str(len(names_3)))

#write the names to file "names_with_3.txt"
#opens the file, f is the file object but for the new file "names_with_3.txt"
f=open('names_with_3.txt','w')
for x in names_3:
    #f.write writes to the file
    f.write(str(x)+"\n")
f.close()
