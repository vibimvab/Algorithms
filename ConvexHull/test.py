import random
from typing import List


def generate_input(n) -> List[List[int]]:
    """
    :param n: number of test cases
    :return: list of n number of pairs
    """
    minimum = -n*5
    maximum = n*5
    output = [[random.randint(minimum, maximum) for _ in range(2)] for _ in range(n)]
    # output.extend([[-n*5-1, -n*5-1], [-n*5-1, n*5+1], [n*5+1, -n*5-1], [n*5+1, n*5+1]])
    return output
