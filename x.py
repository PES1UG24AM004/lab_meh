"""Module for performing arithmetic addition operations."""


def add(x: int, y: int) -> int:
    """Return the sum of two numbers."""
    return x + y


X = 2
Y = 3
Z = add(X, Y)

if __name__ == "__main__":
    print(Z)
