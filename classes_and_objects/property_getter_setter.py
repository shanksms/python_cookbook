'''
Another way to define properties is with decorators.
In this next example, we’ll define two different methods, each called name() but preceded by different decorators:

@property, which goes before the getter method

@name.setter, which goes before the setter method
'''
class Duck:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print('inside getter')
        return self.__name
    @name.setter
    def name(self, name):
        print('inside setter')
        self.__name = name

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def diameter(self):
        return 2*self.__radius

if __name__ == '__main__':
    duck = Duck('Donald')
    print(duck.name)
    duck.name = 'Howard'
    print(duck.name)
    circle = Circle(2)
    print(circle.diameter)
