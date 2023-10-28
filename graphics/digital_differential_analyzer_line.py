import matplotlib.pyplot as plt


def digital_differential_analyzer_line(
    x1: int, y1: int, x2: int, y2: int
) -> list[tuple[int, int]]:
    """
    Draws a line between two points using the Digital Differential Analyzer (DDA) algorithm.

    Args:
    - x1, y1: Coordinates of the starting point.
    - x2, y2: Coordinates of the ending point.

    Returns:
    - List of coordinate points that form the line.

    >>> digital_differential_analyzer_line(1, 1, 4, 4)
    [(2, 2), (3, 3), (4, 4)]
    """

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    coordinates = []
    x: float = x1
    y: float = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        coordinates.append((int(round(x)), int(round(y))))
    return coordinates


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    x1 = int(input("Enter the x-coordinate of the starting point: "))
    y1 = int(input("Enter the y-coordinate of the starting point: "))
    x2 = int(input("Enter the x-coordinate of the ending point: "))
    y2 = int(input("Enter the y-coordinate of the ending point: "))
    coordinates = digital_differential_analyzer_line(x1, y1, x2, y2)
    x_points, y_points = zip(*coordinates)
    plt.plot(x_points, y_points, marker="o")
    plt.title("Digital Differential Analyzer Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
