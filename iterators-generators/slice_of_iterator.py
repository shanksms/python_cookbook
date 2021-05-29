import itertools
def count(n):
    while True:
        yield n
        n += 1

if __name__ == '__main__':
    # below will fail
    c = count(0)
    #c[10:20]

    for x in itertools.islice(c, 10, 20):
        print(x)