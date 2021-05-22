'''
Method TypesSome data (attributes) and functions (methods)are part of theclass itself,
and some are part of the objectsthat are created from that class.
When you see an initialself argument in methodswithin a class definition,
it’s an instance method.These are the types of methodsthat you would normally writewhen creating your
 own classes.The first parameter of an instance method is self,and Python passes the object to the methodwhen
 you call it.In contrast, a class method affects the class as a whole.Any change you make to the classaffects
  all of its objects.Within a class definition,a preceding @classmethod decoratorindicates that that following
   function is a class method.Also, the first parameter to the methodis the class itself.The Python tradition
   is tocall the parameter cls, because class is a reservedword and can’t be used here.Let’s define a class
    method for A that counts how manyobject instances have been made from it:
'''

class A:
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print('I am in A!!!')
    @classmethod
    def object_count(cls):
        #cls.count === A.count
        print('number of objects ', cls.count)
    '''
    A third type of method in a class definitionaffects neither 
    the class nor its objects;it’s just in there for convenienceinstead of 
    floating around on its own.It’s a static method, preceded by a@staticmethod 
    decorator,with no initial self or class parameter.Here’s an example that serves as
     a commercialfor the class CoyoteWeapon:
    '''
    @staticmethod
    def stat_method():
        print('you in a static method')

if __name__ == '__main__':
    a1 = A()
    a2 = A()
    A.object_count()
    A.stat_method()