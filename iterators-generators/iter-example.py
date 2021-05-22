def PowTwo(maximum):
    print('init')
    n = 0
    while n < maximum:
        res = 2**n
        n += 1
        print('returning result')
        yield res
        print('next iteration')
    print('coming out')


res = PowTwo(5)
print(next(res))
print(next(res))
print(next(res))

