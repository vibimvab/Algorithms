import matplotlib.pyplot as plt


def turn_90_left(vector):
    return [-vector[1], vector[0]]


def turn_90_right(vector):
    return [vector[1], -vector[0]]


def to_vectors(vertices):
    vectors = []
    for i in range(len(vertices)-1):
        # find inward vectors to a polygon
        vectors.append(turn_90_left((vertices[i + 1][0] - vertices[i][0], vertices[i + 1][1] - vertices[i][1])))

    # convert to unit vectors
    for vector in vectors:
        length = (vector[0]**2 + vector[1]**2)**(1/2)
        vector[0] /= length
        vector[1] /= length

    return vectors


def find_translation_vector(vertices):
    vectors = to_vectors(vertices)
    if not vectors:
        return

    # for vector in vectors:
    #     plt.plot((0, vector[0] * 5), (0, vector[1] * 5))

    left_margin = [-1, 0]
    right_margin = [1, 0]
    for vector in vectors:
        if turn_90_left(vector)[1] > 0 and turn_90_left(vector)[0] > left_margin[0]:
            left_margin = turn_90_left(vector)

        if turn_90_right(vector)[1] > 0 and turn_90_right(vector)[0] < right_margin[0]:
            right_margin = turn_90_right(vector)

    if left_margin[0] > right_margin[0]:
        plt.xlabel('no casting translation vector exists')
        return

    m = (vertices[-1][0] - vertices[0][0])/2
    plt.plot((0, left_margin[0] * m), (0, left_margin[1] * m))
    plt.plot((0, right_margin[0] * m), (0, right_margin[1] * m))


def plot_vertices(vertices):
    for i in range(len(vertices)):
        plt.plot((vertices[i][0], vertices[i - 1][0]), (vertices[i][1], vertices[i - 1][1]), color='green')
    plt.axis('equal')
    plt.show()


def main():
    vertices = [(-10, 0), (-8, -5), (-5, -20), (0, -15), (3, -6), (10, 0)]
    find_translation_vector(vertices)
    plot_vertices(vertices)

    vertices = [(-5, 0), (-3.48, -1.59), (-3.46, -4.41), (-1.52, -3.89), (-0.86, -6.21), (1.68, -3.17), (2.4, -0.89), (2.64, 0)]
    find_translation_vector(vertices)
    plot_vertices(vertices)

    vertices = [(-3.72, 0), (-2.6, -1.58), (-2.18, -2.94), (-0.44, -1.88), (-0.36, -3.16), (1.14, -1.98), (1, 0)]
    find_translation_vector(vertices)
    plot_vertices(vertices)

    vertices = [(-502, 0), (-286, -142), (42, -308), (254, -298), (98, -158), (-20, -56), (152, -74), (226, 0)]
    find_translation_vector(vertices)
    plot_vertices(vertices)

    vertices = [(-372, 0), (-198, -118), (-0.72, -344), (184, -348), (232, -192), (138, -100), (226, -0)]
    find_translation_vector(vertices)
    plot_vertices(vertices)


if __name__ == '__main__':
    main()
