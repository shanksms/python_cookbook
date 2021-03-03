"""
Reversed iteration only works if the object in question has a size that can be determined or
 if the object implements a _reversed_() special method.
 If neither of these can be satisfied, you’ll have to convert the object into a list first. For example:
"""
f = open('test.txt')
for line in reversed(list(f)):
    print(line)
f.close()
"""
Be aware that turning an iterable into a list as shown could consume a lot of memory if it’s large.
"""