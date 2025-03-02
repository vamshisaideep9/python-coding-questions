"""
1. Shallow Copy: A shallow copy creates a new object, but it does not
create copies of nested objects. Instead it copies references.


--> Changes in shallow copy affects the original

2. Deep copy: Creates a completely independent copy of the original
object and all of its nested objects. 

--> Changes in deep copy doesnt affect the original copy
"""

import copy

original = [[1,2,3],[4,5,6]]
shallow_copied = copy.copy(original)


shallow_copied[0][0] = 99

print(original)
print(shallow_copied)