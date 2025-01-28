from typing import List
from operations import orientation_test
from test import generate_input
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def find_start_point(points: List[List[int]]) -> (List[int], int):
    left_most = points[0]
    index = 0
    for i, point in enumerate(points[1:]):
        if left_most[0] > point[0] or (left_most[0] == point[0] and left_most[1] < point[1]):
            left_most = point
            index = i+1

    return left_most, index


def find_right_most(pivot: List[int], pivot_index: int, points: List[List[int]], convex_hull: List[List[int]])\
        -> (List[int], int):
    if pivot_index == 0:
        right_most: List[int] = points[1]
        right_most_index = 1
    else:
        right_most: List[int] = points[0]
        right_most_index = 0

    for i, point in enumerate(points):
        if i == pivot_index or i == right_most_index:
            continue

        orientation = orientation_test(pivot, right_most, point)
        if orientation < 0:
            right_most = point
            right_most_index = i
        elif orientation == 0:
            if pivot[0] == point[0] and pivot[1] == point[1]:
                # if two points are the same
                continue

            # if points are in line
            dist_to_right_most = (right_most[0] - pivot[0]) ** 2 + (right_most[1] - pivot[1]) ** 2
            dist_to_new = (point[0] - pivot[0]) ** 2 + (point[1] - pivot[1]) ** 2
            if dist_to_right_most >= dist_to_new:
                convex_hull.append(point.copy())
            else:
                convex_hull.append(right_most.copy())
                right_most = point
                right_most_index = i

    convex_hull.append(right_most.copy())
    return right_most, right_most_index


def gift_wrapping_convex_hull(points: List[List[int]]) -> List[List[int]]:
    start, current_index = find_start_point(points)
    current = start

    convex_hull: List[List[int]] = [start]
    while True:
        current, current_index = find_right_most(current, current_index, points, convex_hull)
        if current[0] == start[0] and current[1] == start[1]:
            return convex_hull[:-1]


if __name__ == '__main__':
    # test_case = generate_input(20)
    # print(test_case)
    # test_case = [[-67, 28], [-40, -87], [12, -89], [88, -42], [91, 33], [87, 85], [86, 88], [-20, 71], [-65, 33]]
    # print(gift_wrapping_convex_hull(test_case))

    x = np.array([n for n in range(100, 2001, 100)])
    y = []
    test_count = 1000

    for n in x:
        print(n)
        test_cases = [generate_input(n) for _ in range(test_count)]

        start = time.time()
        for test_case in test_cases:
            gift_wrapping_convex_hull(test_case)
        end = time.time()

        y.append((end - start)/test_count)

    y = np.array(y)
    plt.plot(x, y, label="gift wrapping")

    coefficients_deg_1 = np.polyfit(x, y, 1)
    coefficients_deg_2 = np.polyfit(x, y, 2)
    # coefficients_deg_3 = np.polyfit(x, y, 3)
    y_fit_deg_1 = np.polyval(coefficients_deg_1, x)
    y_fit_deg_2 = np.polyval(coefficients_deg_2, x)
    # y_fit_deg_3 = np.polyval(coefficients_deg_3, x)
    plt.plot(x, y_fit_deg_1, label="degree 1")
    plt.plot(x, y_fit_deg_2, label="degree 2")
    # plt.plot(x, y_fit_deg_3, label="degree 3")

    plt.legend()
    plt.show()
