'''
https://realpython.com/introduction-to-python-generators/#example-1-reading-large-files
'''


def csv_reader_inefficient(file_path: str):
    """
    This loads all the content in the file at one go
    :param file_path:
    :return:
    """
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append(line)
    return lines

def csv_reader_efficient(file_path: str):
    """
    This loads all the content in the file at one go
    :param file_path:
    :return:
    """
    lines = []
    with open(file_path) as f:
        for line in f:
            yield line

if __name__ == '__main__':
    csv_gen = csv_reader_inefficient("some_csv.csv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")

    csv_gen = csv_reader_efficient("some_csv.csv")
    '''
    below will print a generator function
    '''
    print(csv_gen)
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")

