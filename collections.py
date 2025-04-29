# collections/containers
# 
# Theses are out complex data types
# different ways to store data. 

# lists - ordered-(indexed), mutable, a collection of values
# [5-index-postion-0, 6, 7, 7, True, "hello", [{}, {}, ()]] 
# lowest performance. 

# tuples - ordered, immutable, 
# () or nothing x = 1, 2, 3 
# boost to memory and speed. 

# sets - {} - collection of unique values, unordered, mutable.
# deduping data. 
# mathatical and logical structure. 

# dictionaries mutable, unordered, key:value pairs.
# {"key": "value"} 

#x = hash("hello2")
#print(x)

#y = x % 116

#print(y)

#fixed array() buckets
#1 2 4 8 16 32 64 128

#written to precise 

#logic to read is same as logic to write. 

# example

#import time

#large_list = list(range(10_000_000))
#large_dictionary = {num: True for num in range(10_000_000)}

#x = 99_00_000

#starts = time.time()
#y_list = x in large_list
#ends = time.time()
#print(f"list lookup took {ends - starts:.6f}")

#starts = time.time()
#y_dict = x in large_dictionary
#ends = time.time()
#print(f"dictionary lookup took {ends - starts:.6f}")

# lists:

# index pos  0        1      2        3/-1
# colours = ["blue", "green", "red", "yellow"]

#print(colours[2])

# slicing

#print(colours[0:2])
#print(colours[1: ])

#colours[0] = "orange"
#print(colours)

#del colours[0]
#print(colours)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1],combined[1][1])

# methods:

#colours = ["red", "yellow", "blue", "green"]

#colours.sort(key=len) # high order/ high level function - wrapper funntion.
#print(colours)

# join 

#x = ", ".join(colours)
#print(x) 

# dictionaries - keys are unique - values can be anything. 

drinks = {"fizzy": "sprite", "hot": "coffee", "still": "water", "alcoholic": "wine"}

#print(drinks)

# direct access
# Can only query by keys

#print(drinks["fizzy"])

#drinks["non-alcoholic"] = "water"
#print(drinks)

# methods

#print(drinks.keys())
#print(drinks.values())
#print(drinks.items())

# get

#print(drinks["fizzzy"])
#print(drinks.get("fizzzy", ))

# Exercise

# make a dictionary, 3 authors + multiple books per author. 
# Have an input for author name
# return a STRING of the books. ie not a list
# error handling for incorrect keys (get)