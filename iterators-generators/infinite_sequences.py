"""
https://realpython.com/introduction-to-python-generators/#example-1-reading-large-files
"""

def infinite_sequence(base):
    num = base
    while True:
        yield num
        num += 1

if __name__ == '__main__':
    #if you run below loop, it will run infinitely
    #for i in infinite_sequence(10):
    #    print(i)
    gen = infinite_sequence(10)
    print(next(gen))
    print(next(gen))
