def test(a, b, c=99, *d, e, f=100, **g):
    print(a, b, c, d, e, f, g)


if __name__ == "__main__":
    test(1, 2, e=3)
    test(1, 2, 3, e=4)
    test(1, 2, 3, 4, e=5)