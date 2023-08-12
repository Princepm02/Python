#First Code
print("Hello world!!")

#list
l=[1, 2, 3]
print("\nList : ",l)

#dictionary
d={1:"MON",2:"Tue"}
print("\nSecond day of week : ",d[2])

#iteration
print("\nIteration")
it=iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #it will produce error as there are only 3 elements to iterate

#Variables
x, y, z="Hello", "hi", 88
print("\nx : ",x)
print("y : ",y)
print("z : ",z)

x = y = z="Bye"
print("\nx : ",x)
print("y : ",y)
print("z : ",z)

#Multiline printing
x="""\nOranges
ARE
Orange in
colour
do you know that!!!
"""
print(x)

#Accessing position in string
x="Hello World!!"
print("Third element of the string (Hello World!!) : ", x[3])
print("Printing Element through loop : ")
for a in x:
    print(a)

print("\nLength of string : ", len(x))

#Membership operator
print("\n'Like' word in Hello World : ", "like" in x)
# print("like" in x)

# Slicing
print("\nSlicing from index 2 to 5 : ", x[2:5]) # It will print excluding 5th element in string
