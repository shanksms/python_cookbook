class Countdown():

    def __init__(self, start):
        self.start = start
    """
    below is a forward iterator
    """
    def __iter__(self):
        i = 0
        while i < self.start:
            yield i
            i += 1
    def __reversed__(self):
        i = self.start
        while i > 0:
            yield i
            i -= 1

if __name__ == '__main__':
    countdown = Countdown(4)
    for i in countdown:
        print(i, end='\n')
    for i in reversed(countdown):
        print(i, end='\n')
