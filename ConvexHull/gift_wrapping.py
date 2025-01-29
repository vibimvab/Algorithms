from typing import List
from operations import orientation_test, identical_points
from test import generate_input
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def find_start_point(points: List[List[int]]) -> List[int]:
    left_most = points[0]
    for i, point in enumerate(points[1:]):
        if left_most[0] > point[0] or (left_most[0] == point[0] and left_most[1] < point[1]):
            left_most = point

    return left_most


def find_right_most(pivot: List[int], points: List[List[int]], convex_hull: List[List[int]]) -> List[int]:
    right_most = []
    for i, point in enumerate(points):
        if not right_most:  # if right most is not yet assigned
            if not identical_points(point, pivot):
                right_most = point
            continue

        if identical_points(point, pivot) or identical_points(point, right_most):
            continue

        orientation = orientation_test(pivot, right_most, point)
        if orientation < 0:
            right_most = point
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

    convex_hull.append(right_most.copy())
    return right_most


def gift_wrapping_convex_hull(points: List[List[int]]) -> List[List[int]]:
    start = find_start_point(points)
    current = start

    convex_hull: List[List[int]] = [start]
    while True:
        current = find_right_most(current, points, convex_hull)
        if current[0] == start[0] and current[1] == start[1]:
            return convex_hull[:-1]


if __name__ == '__main__':
    # test_case = generate_input(20)
    # print(test_case)
    # test_case = [[-67, 28], [-40, -87], [12, -89], [88, -42], [91, 33], [87, 85], [86, 88], [-20, 71], [-65, 33]]
    test_case = [[-12, 25], [10, 35], [21, -20], [-1, -22], [-34, -47], [-42, 43], [6, -16], [-46, 45], [-12, -16],
                 [-16, 2]]
    test_case = test_case + test_case + test_case
    print(gift_wrapping_convex_hull(test_case))

    # x = np.array([n for n in range(100, 1001, 100)])
    # y = []
    # test_count = 1000
    #
    # for n in x:
    #     print(n)
    #     test_cases = [generate_input(n) for _ in range(test_count)]
    #
    #     start = time.time()
    #     for test_case in test_cases:
    #         gift_wrapping_convex_hull(test_case)
    #     end = time.time()
    #
    #     y.append((end - start)/test_count)
    #
    # y = np.array(y)
    # plt.plot(x, y, label="gift wrapping")
    #
    # coefficients_deg_1 = np.polyfit(x, y, 1)
    # coefficients_deg_2 = np.polyfit(x, y, 2)
    # # coefficients_deg_3 = np.polyfit(x, y, 3)
    # y_fit_deg_1 = np.polyval(coefficients_deg_1, x)
    # y_fit_deg_2 = np.polyval(coefficients_deg_2, x)
    # # y_fit_deg_3 = np.polyval(coefficients_deg_3, x)
    # plt.plot(x, y_fit_deg_1, label="degree 1")
    # plt.plot(x, y_fit_deg_2, label="degree 2")
    # # plt.plot(x, y_fit_deg_3, label="degree 3")
    #
    # plt.legend()
    # plt.show()
