"""
You want to iterate over a sequence,
but would like to keep track of which element of the sequence is currently being processed
"""

def enumerate_example(my_list):
    for index, value in enumerate(my_list):
        print(index, value)


if __name__ == '__main__':
    enumerate_example(my_list = [1, 2, 3])