class A(object):
    def __init__(self, w, h) -> None:
        super().__init__()
        self.m_width = w
        self.m_height = h
        print("this is A")

    def run(self):
        print("w = ", self.m_width, " h = ", self.m_height)


class A1(A):
    def __init__(self, w, h) -> None:
        super().__init__(w, h)
        self.m_width = w + 5
        self.m_height += 5
        print("this is A1")


class A2(A):
    def __init__(self, w, h, r) -> None:
        super().__init__(w, h)
        self.m_width = w + 3
        self.m_height += 9
        self.m_resize = r
        print("this is A2")


class B(A1, A2):
    # 多继承时父类的初始化参数不一致，此时如何使用相关的super

    # def __init__(self, w, h, r) -> None:
    #     super().__init__(w, h, r)
        # self.m_width = w ** 3
        # self.m_height = h ** 3
        # print("this is B")

    def run2(self):
        print("w = ", self.m_width, " h = ", self.m_height)


class Base(object):
    def __init__(self, w, h) -> None:
        self.m_width = w
        self.m_height = h
        print("init Base")


class Base1(Base):
    def __init__(self, w, h, r) -> None:
        super().__init__(w, h)
        self.m_width = w
        self.m_height = h
        print("init Base1")


class Base2(object):
    def __init__(*args) -> None:
        print("init Base2")

    def test(self):
        print(100)


class subClass(Base1, Base2):
    def __init__(self, *args):
        super(subClass, self).__init__(*args)
        print("init subClass")
        print(subClass.__mro__)

    def info(self):
        print("w = ", self.m_width, " h = ", self.m_height)


if __name__ == "__main__":
    # b = B(2, 2, 2)
    # b.run()
    # b.run2()

    test = subClass(2, 3, 1000)
    test.info()
    test.test()