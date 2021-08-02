import weakref

class Item:
    pass

class A:
    def __init__(self) -> None:
        self.m_ins_ref = None

    def GetIns(self):
        if self.m_ins_ref is None:
            ins = Item()
            self.m_ins_ref = weakref.ref(ins)
            return ins
        else:
            return self.m_ins_ref()

    def ins(self):
        print(self.m_ins_ref)

if __name__ == "__main__":
    a = A()
    a.ins()
    b = a.GetIns()
    a.ins()
    b = 99
    a.ins()
    c = a.GetIns()
    a.ins()