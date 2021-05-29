class Word:
    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __eq__(self, other):
        return self.__text.lower() == other.text.lower()

    def __repr__(self):
        return 'Word(%s)'.format(self.__text)
    def __str__(self):
        return self.__text
if __name__ == '__main__':
    w1 = Word('Hi')
    w2 = Word('HI')
    print(w1 == w2)
    print(w1)

