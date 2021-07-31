from functools import lru_cache

@lru_cache
def Test(x):
    print("counting")
    return x**3


if __name__ == "__main__":
    Test(1)
    Test(2)
    Test(2)
    Test(2)