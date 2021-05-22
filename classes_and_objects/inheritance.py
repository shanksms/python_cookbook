class Person:
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    '''
    When you define an __init__() method for your class,you’re replacing
    the __init__() method of its parent class,and the latter is not called automatically anymore.
    As a result, we need to call it explicitly.Here’s what’s happening:
    The super() gets the definition of the parent class,
     Person.The __init__() method calls the Person.__init__() method.
     It takes care of passing the self argument to the superclass,so you just need to give
      it any optional arguments.
      In our case, the only other argument Person() accepts is name.
      The self.email = email line is the new code thatmakes this EmailPerson different from a Person.
    '''
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

if __name__ == '__main__':
    john = EmailPerson('John', 'john.doe@gmail.com')
    print(john.name, john.email)