
class Car:
    def exclaim(self):
        print('i am a car!!!')

if __name__ == '__main__':
    car = Car()
    #Both below calls are same
    '''
    Here’s what Python actually does, under the hood:
    Look up the class (Car) of the object car.
    Pass the object car to the exclaim() methodof the Car class as the self parameter.
    Just for fun,you can even run it this way yourself and
     it willwork the same as the normal (car.exclaim()) syntax:
    '''
    car.exclaim()
    Car.exclaim(car)