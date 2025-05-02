# classes
# 
# blueprint of methods(functions) and attributes(vars) 
# We can make instances of the class.
# 
# Classese extend the language. 
#
# We want to describe an object that python currently doesnt describe. 
#
# 4 oop principles:
# - polymorphism: different ways of implementing the same method. 
# - abstraction: i dont want to see the code.
# - inheritance: inherit from a parent class. 
# - encapsulation: privacy. 

#class Example:
  #  name = "chris" #Attribute

    # method
 #   def speak(self):
 #       print("hello")


#person = Example()

#print(person.name)
#person.speak()
#person.name = "john"
#print(person.name)

#class Students:
#    pass

#student1 = Students()
#student2 = Students()

#student1.name = "john"
#student1.age = 10
#student2.group = "group 1"

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

# student1 = Students("john", "smith", 10)

# print(student1.age)

# class Students:

#     # full = ""

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.full = first + " " + last

# student1 = Students("john", "smith", 10)

# print(student1.full)

# from types import MethodType
# import builtins

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#     def fullName(self):
#         return self.first + " " + self.last
       

# student1 = Students("john", "smith", 10)

# def outside_function(self):
#     print(f"{self.first} called me")

# student1.outside_function = MethodType(outside_function, student1)
# student1.outside_function()
# print(student1.fullName())

# self class variable
# class Students:

#     age_increase_amount = 20

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#     def fullName(self):
#         return self.first + " " + self.last

#     def change_age(self):
#         self.age = self.age + self.age_increase_amount


#student1 = Students("john", "smith", 10)
#student2 = Students("sam", "smith", 12)

#student1.change_age()
#print(student1.age, student2.age)

# __dict__
#print(student1.__dict__)
#print(student2.__dict__)
#print(Students.__dict__)

#student1.age_increase_amount = 100

#student1.change_age()

#print(student1.__dict__)
#print(student2.__dict__)

# non self class variables

# class Students:

#     age_increase_amount = 20
#     __num_of_students = 0 # name mangling

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#         Students.__num_of_students += 1 

#     def fullName(self):
#         return self.first + " " + self.last

#     def change_age(self):
#         self.age = self.age + self.age_increase_amount

#     @classmethod
#     def get_num_of_students(cls):
#         return cls.__num_of_students

# student1 = Students("john", "smith", 10)
# student1 = Students("john", "smith", 10)
# #print(Students._Student__num_of_students)
# print(Students.get_num_of_students())


# inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    def meow(self):
        print("meow")

    def __str__(self):
        return super().__str__() + f" - {self.breed}"
    
my_cat = Cat("w", "y", "z")

print(my_cat)



# TODO:

# optional:

# class lab

#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle


#2. Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account.

#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes.

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

# RPS app into a class based design. 

# library system. 