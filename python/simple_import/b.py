from a import funcA

def funcB():
    print("called by funcB in b.py")
    funcA()


if __name__ == "__main__":
    funcB()