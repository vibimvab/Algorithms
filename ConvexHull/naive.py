from typing import List
from test import generate_input
from operations import orientation_test, identical_points
from sklearn.metrics import r2_score
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def naive_convex_hull(points: List[List[int]]) -> List[List[int]]:
    """
    :parameter points: set of points, each element is a point [x, y]
    :return: points in convex hull

    time complexity
    average: O(n^2)
    worst: O(n^3)
    """
    convex_hull = set()
    for i, first_point in enumerate(points):
        if i in convex_hull:
            continue

        for j, second_point in enumerate(points[i+1:]):
            j = i+j+1
            if j in convex_hull:
                continue

            if identical_points(first_point, second_point):
                continue

            sign = 0
            for k, third_point in enumerate(points):
                if i == k or j == k:
                    continue
                orientation = orientation_test(first_point, second_point, third_point)
                if orientation > 0:
                    if sign < 0:
                        break
                    elif sign == 0:
                        sign = 1
                elif orientation < 0:
                    if sign > 0:
                        break
                    elif sign == 0:
                        sign = -1
            else:
                convex_hull.add(i)
                convex_hull.add(j)

    return [points[i] for i in convex_hull]


if __name__ == '__main__':
    x = np.array([n for n in range(20, 1001, 50)])
    y = []
    test_count = 300

    for n in x:
        print(n)
        test_cases = [generate_input(n) for _ in range(test_count)]

        start = time.time()
        for test_case in test_cases:
            naive_convex_hull(test_case)
        end = time.time()

        y.append((end - start)/test_count)

    y = np.array(y)
    plt.plot(x, y, label="naive")

    coefficients_deg_2 = np.polyfit(x, y, 2)
    coefficients_deg_3 = np.polyfit(x, y, 3)
    coefficients_deg_4 = np.polyfit(x, y, 4)
    y_fit_deg_2 = np.polyval(coefficients_deg_2, x)
    y_fit_deg_3 = np.polyval(coefficients_deg_3, x)
    y_fit_deg_4 = np.polyval(coefficients_deg_4, x)
    # plt.plot(x, y_fit_deg_2, label="degree 2")
    # plt.plot(x, y_fit_deg_3, label="degree 3")
    # plt.plot(x, y_fit_deg_4, label="degree 4")

    # Compute R² values
    r2_deg_2 = r2_score(y, y_fit_deg_2)
    r2_deg_3 = r2_score(y, y_fit_deg_3)
    r2_deg_4 = r2_score(y, y_fit_deg_4)

    # Print coefficients and R² values
    print(f"Quadratic Fit Coefficients: {coefficients_deg_2}, R²: {r2_deg_2:.6f}")
    print(f"Cubic Fit Coefficients: {coefficients_deg_3}, R²: {r2_deg_3:.6f}")
    print(f"4th Degree Fit Coefficients: {coefficients_deg_4}, R²: {r2_deg_4:.6f}")

    # Plot the data and fits
    plt.plot(x, y, 'o', label="Original Data")
    plt.plot(x, y_fit_deg_2, label=f"Degree 2 (R²={r2_deg_2:.4f})")
    plt.plot(x, y_fit_deg_3, label=f"Degree 3 (R²={r2_deg_3:.4f})")
    plt.plot(x, y_fit_deg_4, label=f"Degree 4 (R²={r2_deg_4:.4f})")

    plt.legend()
    plt.show()
    print(coefficients_deg_2)
    print(coefficients_deg_3)
    print(coefficients_deg_4)
