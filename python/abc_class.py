from abc import ABC, ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @abstractmethod
    def write(self):
        pass

class A2(ABC):
    @abstractmethod
    def test(self):
        pass

class B(A):
    def BFunc(self):
        pass

    # def write(self):
    #     print("call write from B")

class C:
    def __init__(self) -> None:
        self.value = 99

    # def write(self):
    #     print("call write from C")

A.register(C)   # 为什么不会检测未实现的接口
A2.register(C)

if __name__ == "__main__":
    b = B()
    c = C()
    c.write()
    assert issubclass(C, A)
    assert issubclass(B, A)