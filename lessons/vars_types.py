# variables + data types + misc


# Variables - a referenece (a name), a selection of memory(location). 
# 

#x = False

#x = 10
#print(hex(id(x)))
#x = 20
#print(hex(id(x)))

# interning (caching)
#-256 -- + 256 is cached and stored in mem
#a = 256
#b = 256

#print(a is b)

#def t1():
#    c = int(str(257))
#    return c
#def t2():
#    d = int(str(257))
#    return d

#print(t1() is t2())


# REMINDER -- TASK - how to force low number not be individual objects.
#          -- Research Traceback and come up with ideas on how to incorporate.
#          -- inspect -- combine with tracebook - make your own tools to help debug. 


# Style

# naming convention

# descriptive, readable, consistancy, simple, comments/doc strings

#PascalCase - class names
#snake_case - vars/funcs/methods
#camelCase - vars/funcs/methods

#note: scope

#bodmas

#input/print/concat

#escap chars

#simple (str) methods

#global_variable = "accessible from anywhere"


#def my_fucntion():
  #  local_variable = "accessible only from inside the function"
 #   print(local_variable) #tight coupling
 #   print(global_variable)

#my_fucntion()

#print(local_variable)


#import traceback

#def function_a():
#    function_b()

#def function_b():
#    fucntion_c()

#def fucntion_c():
#    print("the call stack is: ")
#    traceback.print_stack()

#function_a()


#import inspect

#def example(number_a, number_b):
  #  '''
 #   return number_a + number_b


#print(inspect.getdoc(example))
#print(inspect.signature(example))
#print(inspect.getsource(example))

# in-built

#print("hello")
#input("prompt to be printed: ") # default to string

#import sys

#with open("file.txt", "w") as file:
 #   sys.stdout = file
 #   print("go to file")

#sys.stdout = sys.__stdout__
#print("hello")

# primitive data types:
# string (str) - words, sentances, paragraphs etc. ""
# integers (int) - 5 + - / * //(floor division) %(modulo) 
# floats (float) - decimal numbers.
# boolean: sub class of a int - True or False, 0 or 1, something or nothing.  

# escape chars - \ - take the next char as its literal meaning.  
# \\ backlash, \n - newline, \t - tab, \u unicode, \U extended unicode. 

#print("Person 1: \tHi, how are you?\nPerson 2: \tIm good thanks \U0001f604")

# str concatenation

#name = input("enter name: ")
#age = int(input("enter age: "))

#print(f"your name is {name}, your age is {age}")
#print("your name is", name, "your age is", age)
#print("your name is " + name)

#message = "your name is {}, your age is {}".format(name, age)
#print(message)

# BODMAS
# - Review this and save link. 

# 10 mins reviewing string methods

