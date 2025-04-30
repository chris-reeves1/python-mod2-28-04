# while loops + for loops 
# saves time and code duplication. 

# while

# we need a condition to start a while loop
# we need a condition to be met to end the loop. 
# otherwise continues foerver. 

# x = 0 

# while x < 101:
#     print(x)
#     x += 1 


# break and continue

# i = 0

# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# i = 0

# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# for loops
# for iterating through an iterable.

#my_fruits = ["apple", "pear", "kiwi", "orange"]

# for item in iterable:
#     code...

# for fruit in my_fruits:
#     print(fruit)

# l = 0
# while l < len(my_fruits):
#     print(my_fruits[l])
#     l += 1

# range

#for a in range(1, 10, 2):
#    print(a)

# string

# for letter in "hello world".split():
#     print(letter)

# List comp - make or change a list. 
        # expression    #item    #iterable
#result = [x**2        for  x in range(5)]
#print(result)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        #expression  #item     #iterable       #condition
#even_squared_numbers = [number**2 for number in numbers if number % 2 == 0]

#print(even_squared_numbers)

# dictionaries

# for i in {"drink": "cola"}:
#     print(i)

# for i, y in {"drink": "cola"}.items():
#     print(i, y)

# nested for loops

# for i in range(1,3):
#     for j in range(1,4):
#         print(i, "x", j, "=", i*j)

#num = 30
#num1 = 20

# if num > num1:
#     print(num)
# else:
#     print(num1)

# result = (num > num1) * num + (num <= num1) * num1
# print(result)

#result = num1 + (num - num1) * (num >= num1)
#print(result)

# exercise:
# 
# loop to take 5 name as input and print name + is cool

# while loop
# for loop
# list comp
# list comp one line only

# inner list
#[input("enter a name: ") for x in range(5)]

# outer list
#[print(f"{name} is cool") for name in iterable]

# combined:
# x = [print(f"{name} is cool") for name in [input("enter a name: ") for x in range(5)]]

# print(x)

# y = print("hello")
# print(y)
# # side effect:
# def print(*args, **kwrags):
#     # send to std.out
#     return None