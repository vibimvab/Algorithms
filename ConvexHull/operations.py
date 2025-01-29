from typing import List


def orientation_test(initial: List[int], terminal: List[int], point: List[int]) -> int:
    """
    :param initial: initial point of the directed line segment
    :param terminal: terminal point
    :param point:

    :return: 1 if the point is on left of the line segment, -1 if on the right, 0 if three points are in line
    """
    vector_a = [terminal[0] - initial[0], terminal[1] - initial[1]]
    vector_b = [point[0] - initial[0], point[1] - initial[1]]
    cross_product = vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]

    if cross_product > 0:
        return 1
    elif cross_product == 0:
        return 0
    else:
        return -1


def identical_points(a: List[int], b: List[int]):
    return a[0] == b[0] and a[1] == b[1]


if __name__ == '__main__':
    print(orientation_test([1,1], [-1,-1], [1,1]))
