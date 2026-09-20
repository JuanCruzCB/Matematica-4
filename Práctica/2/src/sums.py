X = [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25]

Y = [
    9.6,
    20.1,
    29.9,
    39.1,
    50.0,
    9.6,
    19.4,
    29.7,
    40.3,
    49.9,
    10.7,
    21.3,
    30.7,
    41.8,
    51.2,
]


def calculate_sums() -> dict[str, float]:  # noqa: D103
    if len(X) != len(Y):
        msg = "The lists X and Y must have the same length"
        raise ValueError(msg)

    sum_x = sum(X)
    sum_y = sum(Y)

    sum_x_squared = sum(x**2 for x in X)
    sum_y_squared = sum(y**2 for y in Y)

    sum_xy = sum(x * y for x, y in zip(X, Y))

    return {
        "Σx": sum_x,
        "Σy": sum_y,
        "Σx²": sum_x_squared,
        "Σy²": sum_y_squared,
        "Σxy": sum_xy,
    }


def print_sums(sums: dict[str, float]) -> None:  # noqa: D103
    print(f"Summation of x_i: {sums['Σx']}")
    print(f"Summation of y_i: {sums['Σy']}")
    print(f"Summation of x_i²: {sums['Σx²']}")
    print(f"Summation of y_i²: {sums['Σy²']}")
    print(f"Summation of x_i * y_i: {sums['Σxy']}")


print_sums(sums=calculate_sums())
