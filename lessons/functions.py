# a function returns something or performs a task.
# repeatability

#def greet(name): # params of the function. Takes args. 
#    print(f"hello {name}")

#greet("chris")

#def greet1(first_name, last_name, age=20):
#    print(f"{first_name} {last_name} is {age}")

#greet1("chris", "reeves")

# return

##def greeter(name):
#    return f"hello {name}"

#x = greeter("c")
#print(x)

#print(greeter("c"))

# *args
# if we dont know how many args need to be passed through
# tuple of args is receieved. 

#def fruit_list(*fruits):
 #   print("the unpacked tuple of fruits is:")
 #   for fruit in fruits:
 #       print(fruit)
#fruit_list( )

#def make_pizza(size, *toppings):
  #  print(f"Order for {size}-inch pizza with the following toppings:")
 #   for topping in toppings:
 #       print(topping)

#make_pizza(12, "peppers", "mushrooms")

# kwargs
# order doesnt matter
# send args as key=value 

#def fruit_list(fruit1, fruit2, fruit3):
 #   print(f"fruit 1 is {fruit1} - fruit2 is {fruit2} - fruit3 is {fruit3}")

#fruit_list(fruit3="apple", fruit1="pear", fruit2="kiwi")

# **kwargs
# dont know how many key word args are gonna be passed through.

#def make_order(**items):
#    print("order: ")
#    for x, y in items.items():
#        print(f"{x} - {y}")

#make_order(main="pizza", drink="cola", side="fries")

# combined

#def combined(*args, **kwargs):
 #   print("args: ", args)
 #   print("kwargs: ", kwargs)

#combined(10, d= 2, c=3, a=5)

# /
# introduced python 3. 6/8
# enforced everything before / is a positional arg.
# after can be anything and its not enforced. 
# *
# * enforced keyword args must follow. 

#def example(a, b, /, *, c, d):
 #   print(f"a is {a} b is {b} c is {c} d is {d}")

#example("a", "b", c="c", d="d")

#def maths_function(a, b, /, operation="add", *, decimal_places=4):
   # if operation == "add":
   #     result = a + b
  #  elif operation == "subtract":
  #      result = a - b
 #   else:
 #       raise TypeError("invlaid operation")
 #   return round(result, decimal_places)

#print(maths_function(10, 5, "subtract"))

#print(maths_function(10.245845, 5.2564588, decimal_places=2))

# recurrion

#def factorial(n):
   # if n == 1:
  #      return 1
 #   else:
 #       return n * factorial(n - 1)

#print(factorial(5))
    
# import inspect

# def test_function():
#     print("im in:", inspect.currentframe().f_code.co_name)
#     print("ive been called from:", inspect.stack()[1].function)
#     x = "hello"
#     print(locals())

# def caller():
#     test_function()

# caller()
# print(locals())

#def recursive_sum(n):
#    print(f"→ entering: sum({n})")
    
#    if n == 0:
#        print(f"⤷ base case: return 0")
#        return 0

 #   partial = recursive_sum(n - 1)
 #   result = n + partial
 #   print(f"← returning: {n} + {partial} = {result}")
 #   return result

#total = recursive_sum(5)
#print(f"\nTotal sum: {total}")

# lambdas
# short un-named function
# calculate a single expression.

#lambda arguments : expression (iterable)

#add_lambda = lambda x, y: x + y

#print(add_lambda(5, 8))

#numbers = [1, 2, 3, 4]

#squared = map(lambda x: x**2, numbers)

#print(list(squared))

# higher-order function

#def square(x):
 #   return x * x

#def apply_function(func, value):
#    return func(value)

#print(apply_function(square, 10))

# todo

# rock paper scissor game using function(s)
# app to play rps against the computer. A function to handle the game logic and 
# a loop to handle rounds. keep track of games played, user wins and computer wins.
# Use import random (random choice) to choose the computer moves. 

# labs 5 + 6 optional

# function challenges (optional)


