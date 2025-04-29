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

# book_dictionary = {
# 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# }

# author = input("Enter the name of the author: ")

# if author in book_dictionary:
# 	print("Books by " + author + ": ")
# 	books = ", ".join(book_dictionary[author])
# 	print(books)
# else:
# 	print("Cannot find any book by the author.")

# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author) or ["sorry no books found"]

# print(", ".join(books))


# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for a, b in record.items():
#     if "book" in a:
#         list_to_print.append(b)

# print(", ".join(list_to_print))

# tuples

#rectangle = 10, 5

#rectangle[0] = 20

#print(rectangle)

# sets

#set1 = {1, 2, 3, 4, 5}
#set2= {4, 5, 6, 7, 8}

#print(set1.union(set2))
#print(set1.intersection(set2))

#print(set1.difference(set2))
#print(set1.symmetric_difference(set2))