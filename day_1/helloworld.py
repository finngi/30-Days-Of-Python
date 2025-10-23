#Exercise 3

"""
Write an example for different Python data types such as 
Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)
"""
# Different Python Data Types
# Number
integer = 20
floating_point = 20.44
complex_number = 2 + 3j
# String
string_example = "Hello, World!"
# Boolean
boolean_example = True
# List
list_example = [1, 2, 3, 4, 5]
# Tuple
tuple_example = (1, 2, 3, 4, 5)
# Set
set_example = {1, 2, 3, 4, 5}
# Dictionary
dictionary_example = {"name": "Alice", "age": 30}
# Finding Euclidean distance between (2, 3) and (10, 8)
import math
p = (2, 3)
q = (10, 8)

euclidean_distance = math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

print(f"Euclidean distance between {p} and {q} is {euclidean_distance}")