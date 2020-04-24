import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time1 = time.time()
duplicates = []  # Return the list of duplicates in this data structure

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
end_time1 = time.time()
print (f"{len(duplicates)} duplicates | runtime for original: {end_time1 - start_time1} seconds")

# My new code
start_time2 = time.time()
duplicates = []
bst = BinarySearchTree('duplicate_names')
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time2 = time.time()
print (f"{len(duplicates)} duplicates | runtime for binary search tree: {end_time2 - start_time2} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time3 = time.time()
duplicates = []
dict = {}
for name in names_1:
    dict[name] = None
for name in names_2:
    if name in dict:
        duplicates.append(name)
end_time3 = time.time()
print (f"{len(duplicates)} duplicates | runtime for dict stretch: {end_time3 - start_time3} seconds")

start_time4 = time.time()
fast_duplicates = set(names_1+names_2)
end_time4 = time.time()
print (f"{len(duplicates)} duplicates | runtime for set stretch: {end_time4 - start_time4} seconds")

start_time5 = time.time()
duplicates = []
for name in names_1:
    if names_2.count(name) >= 1:
        duplicates.append(name)
end_time5 = time.time()
print (f"{len(duplicates)} duplicates | runtime for array stretch: {end_time5 - start_time5} seconds")