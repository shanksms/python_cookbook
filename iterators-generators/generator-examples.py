"""
 Here’s a generator that produces a range of floating-point numbers.
 Below function returns a generator object. A generator object is also an iterator. an Iterator is an Iterable.
 That is why you can use it in while loop.
"""


def frange(start, stop, increment):
    i = start
    while i < stop:
        yield i
        i += increment


'''
The mere presence of the yield statement in a function turns it into a generator. 
Unlike a normal function, a generator only runs in response to iteration. 
Here’s an experiment you can try to see the underlying mechanics of how such a function works:
'''
def countdown(n):
    print('Starting to count from n')
    while n > 0:
        yield n
        n -= 1
    print('Done')

if __name__ == '__main__':
    for x in frange(0, 4, 0.5):
        print(x)
    """
    The key feature is that a generator function only runs in response to "next" operations carried out in iteration.
    Once a generator function returns, iteration stops.
    However, the for statement that’s usually used to iterate takes care of these details,
     so you don’t normally need to worry about them.
    """
    c = countdown(3)
    print('printing c', c)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))

