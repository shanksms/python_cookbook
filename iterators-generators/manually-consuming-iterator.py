with open('test.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

print()
with open('test.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1, 2, 3]
# get the iterator. invokes __iter__()
it = iter(items)
# get the next element from the iterator. invokes it.__next__()
next(it)
next(it)
next(it)
#this generates an error
next(it)