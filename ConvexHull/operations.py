from typing import List


def orientation_test(initial: List[int], terminal: List[int], point: List[int]) -> int:
    vector_a = [terminal[0] - initial[0], terminal[1] - initial[1]]
    vector_b = [point[0] - initial[0], point[1] - initial[1]]
    cross_product = vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]

    if cross_product > 0:
        return 1
    elif cross_product == 0:
        return 0
    else:
        return -1


if __name__ == '__main__':
    print(orientation_test([1,1], [-1,-1], [1,1]))
