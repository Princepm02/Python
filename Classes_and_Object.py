# class and object

class Test:
    x = 5

t1 = Test()
print("Value of X : ", t1.x)

#delete object
del t1

class New:
    def __init__(self, name, age):
        self.name = name
        self.age = age

n1 = New("Joe",6)
print("\nName : ",n1.name)
print("Age : ", n1.age)

del n1


# function and variables
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def methods(self):
       print("\nHi! My name is", self.name,"\nAge is",self.age)

h1 = Human("Prince",21)
h2 = Human("Rahul",50)
h1.methods()
h2.methods()

del h1,h2

# we can't make empty class we will get error but we can do the following
class Bird:
    pass    # Due to this we won't get error
