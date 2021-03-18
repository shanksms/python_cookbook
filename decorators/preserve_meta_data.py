import time
from functools import wraps
'''
Copying decorator metadata is an important part of writing decorators. 
If you forget to use @wraps, you’ll find that the decorated function loses all sorts of useful information. 
For instance, if omitted, the metadata in the last example would look like this:

>>> countdown.__name__
'wrapper'
>>> countdown.__doc__
>>> countdown.__annotations__
{}
>>>
'''
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n : int):
    '''
    count down
    :param n:
    :return:
    '''
    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(10)
    countdown.__name__
    countdown.__annotations__
    countdown.__doc__
