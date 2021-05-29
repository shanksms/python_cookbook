'''
ProblemYou have built a custom container object that internally holdsa list,
tuple, or some other iterable.
You would like tomake iteration work with your new container.
SolutionTypically, all you need to do is define an __iter__() method thatdelegates
 iteration to the internally held container.  For example:
'''

class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def __repr__(self):
        return f'Node({self.value})'

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for child in root:
        print(child)
