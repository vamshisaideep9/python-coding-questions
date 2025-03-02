"""
List comprehension: Is a concise way to create lists in python
using a single line of code instead of traditional loops.

"""

new_list = [x for x in range(5)]

labels = ["Even" if x%2==0 else "odd" for x in range(5)]


"""
Dictionary comprehension: Is a concise way to create dictionaries
in python using a single line of code instead of traditional loops.
"""

squares = {x: x**2 for x in range(5)}

number_type = {x: "even" if x%2==0 else "odd" for x in range(5)}