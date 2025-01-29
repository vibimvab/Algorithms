from typing import List
from operations import orientation_test, identical_points
from test import generate_input
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def merge_sort(points: List[List[int]]) -> List[List[int]]:
    """
    Merge sort algorithm based on https://www.w3schools.com/dsa/dsa_algo_mergesort.php
    slightly modified to compare points
    """
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        else:
            if left[i][1] >= right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def bound_convex_hull(points: List[List[int]]) -> List[List[int]]:
    # pre-processing O(n*log(n))
    points = merge_sort(points)

    # upper bound: O(n)
    # to ignore identical points in the beginning
    start = 0
    while identical_points(points[start], points[start+1]):
        start += 1

    stack_upper = points[start:start+2]
    for point in points[start+2:]:
        # to ignore identical points in the middle
        if identical_points(stack_upper[-1], point):
            continue

        # remove a point on stack on left turn
        while len(stack_upper) > 1 and orientation_test(stack_upper[-2], stack_upper[-1], point) == 1:
            stack_upper.pop()
        stack_upper.append(point)

    # lower bound: O(n)
    # to ignore identical points in the end
    end = -1
    while identical_points(points[end], points[end-1]):
        end -= 1

    stack_lower = points[end:end-2:-1]
    for point in points[end-2::-1]:
        if identical_points(stack_lower[-1], point):
            continue

        # remove a point on stack on left turn
        while len(stack_lower) > 1 and orientation_test(stack_lower[-2], stack_lower[-1], point) == 1:
            stack_lower.pop()
        stack_lower.append(point)

    return stack_upper[:-1] + stack_lower[:-1]


if __name__ == '__main__':
    # test_case = generate_input(10)
    # print(test_case)
    # test_case = [[-12, 25], [10, 35], [21, -20], [-1, -22], [-34, -47], [-42, 43], [6, -16], [-46, 45], [-12, -16],
    #              [-16, 2]]
    # test_case = test_case + test_case + test_case
    # print(bound_convex_hull(test_case))

    x = np.array([n for n in range(50, 1501, 50)])
    y = []
    test_count = 3000

    for n in x:
        print(n)
        test_cases = [generate_input(n) for _ in range(test_count)]

        start = time.time()
        for test_case in test_cases:
            bound_convex_hull(test_case)
        end = time.time()

        y.append((end - start)/test_count)

    y = np.array(y)
    plt.plot(x, y, label="bound")

    coefficients_deg_1 = np.polyfit(x, y, 1)
    # coefficients_deg_2 = np.polyfit(x, y, 2)
    # coefficients_deg_3 = np.polyfit(x, y, 3)
    y_fit_deg_1 = np.polyval(coefficients_deg_1, x)
    # y_fit_deg_2 = np.polyval(coefficients_deg_2, x)
    # y_fit_deg_3 = np.polyval(coefficients_deg_3, x)
    plt.plot(x, y_fit_deg_1, label="degree 1")
    # plt.plot(x, y_fit_deg_2, label="degree 2")
    # plt.plot(x, y_fit_deg_3, label="degree 3")

    plt.legend()
    plt.show()

