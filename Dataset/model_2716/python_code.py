from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class J:

    pass
class L1:

    pass
class k5_L3(L1):

    pass
class k5_L2:

    def __init__(self, l1: int, l2: int, k5_L2: "k5_Q" = None, k5_L231: "k5_Q" = None, k5_L234: "k5_K" = None):
        self.l1 = l1
        self.l2 = l2
        self.k5_L2 = k5_L2
        self.k5_L231 = k5_L231
        self.k5_L234 = k5_L234
        
    @property
    def l1(self) -> int:
        return self.__l1

    @l1.setter
    def l1(self, l1: int):
        self.__l1 = l1

    @property
    def l2(self) -> int:
        return self.__l2

    @l2.setter
    def l2(self, l2: int):
        self.__l2 = l2

    @property
    def k5_L2(self):
        return self.__k5_L2

    @k5_L2.setter
    def k5_L2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L2__k5_L2", None)
        self.__k5_L2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_Q"):
                opp_val = getattr(old_value, "k5_Q", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_Q"):
                opp_val = getattr(value, "k5_Q", None)
                if opp_val is None:
                    setattr(value, "k5_Q", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def k5_L234(self):
        return self.__k5_L234

    @k5_L234.setter
    def k5_L234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L2__k5_L234", None)
        self.__k5_L234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_K35"):
                opp_val = getattr(old_value, "k5_K35", None)
                if opp_val == self:
                    setattr(old_value, "k5_K35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_K35"):
                opp_val = getattr(value, "k5_K35", None)
                setattr(value, "k5_K35", self)

    @property
    def k5_L231(self):
        return self.__k5_L231

    @k5_L231.setter
    def k5_L231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L2__k5_L231", None)
        self.__k5_L231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_Q32"):
                opp_val = getattr(old_value, "k5_Q32", None)
                if opp_val == self:
                    setattr(old_value, "k5_Q32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_Q32"):
                opp_val = getattr(value, "k5_Q32", None)
                setattr(value, "k5_Q32", self)

class P:

    pass
class k5_Q(P):

    pass
class k5_K(J):

    def __init__(self, title: str, k5_K: "k5_P" = None, k5_K35: "k5_L2" = None):
        self.title = title
        self.k5_K = k5_K
        self.k5_K35 = k5_K35
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def k5_K(self):
        return self.__k5_K

    @k5_K.setter
    def k5_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_K__k5_K", None)
        self.__k5_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_P20"):
                opp_val = getattr(old_value, "k5_P20", None)
                if opp_val == self:
                    setattr(old_value, "k5_P20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_P20"):
                opp_val = getattr(value, "k5_P20", None)
                setattr(value, "k5_P20", self)

    @property
    def k5_K35(self):
        return self.__k5_K35

    @k5_K35.setter
    def k5_K35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_K__k5_K35", None)
        self.__k5_K35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_L234"):
                opp_val = getattr(old_value, "k5_L234", None)
                if opp_val == self:
                    setattr(old_value, "k5_L234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_L234"):
                opp_val = getattr(value, "k5_L234", None)
                setattr(value, "k5_L234", self)

class N:

    pass
class k5_G(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class G:

    pass
class k5_M(G):

    pass
class k5_I(G):

    pass
class C:

    pass
class k5_B(C):

    pass
class B:

    pass
class k5_A(B):

    pass
class A:

    pass
class k5_J(A):

    pass
class M:

    pass
class k5_N(M):

    pass
class k5_L1:

    def __init__(self, id1: str, id2: int, k5_L1: "k5_M" = None, k5_L125: "k5_C" = None, k5_L128: "k5_M" = None):
        self.id1 = id1
        self.id2 = id2
        self.k5_L1 = k5_L1
        self.k5_L125 = k5_L125
        self.k5_L128 = k5_L128
        
    @property
    def id2(self) -> int:
        return self.__id2

    @id2.setter
    def id2(self, id2: int):
        self.__id2 = id2

    @property
    def id1(self) -> str:
        return self.__id1

    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def k5_L125(self):
        return self.__k5_L125

    @k5_L125.setter
    def k5_L125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L1__k5_L125", None)
        self.__k5_L125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_C26"):
                opp_val = getattr(old_value, "k5_C26", None)
                if opp_val == self:
                    setattr(old_value, "k5_C26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_C26"):
                opp_val = getattr(value, "k5_C26", None)
                setattr(value, "k5_C26", self)

    @property
    def k5_L128(self):
        return self.__k5_L128

    @k5_L128.setter
    def k5_L128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L1__k5_L128", None)
        self.__k5_L128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_M29"):
                opp_val = getattr(old_value, "k5_M29", None)
                if opp_val == self:
                    setattr(old_value, "k5_M29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_M29"):
                opp_val = getattr(value, "k5_M29", None)
                setattr(value, "k5_M29", self)

    @property
    def k5_L1(self):
        return self.__k5_L1

    @k5_L1.setter
    def k5_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_L1__k5_L1", None)
        self.__k5_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_M16"):
                opp_val = getattr(old_value, "k5_M16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_M16"):
                opp_val = getattr(value, "k5_M16", None)
                if opp_val is None:
                    setattr(value, "k5_M16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class k5_Z:

    def __init__(self, z1: str, z2: str, z3: str, k5_Z: "k5_X" = None, k5_Z37: "k5_L3" = None):
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.k5_Z = k5_Z
        self.k5_Z37 = k5_Z37
        
    @property
    def z3(self) -> str:
        return self.__z3

    @z3.setter
    def z3(self, z3: str):
        self.__z3 = z3

    @property
    def z1(self) -> str:
        return self.__z1

    @z1.setter
    def z1(self, z1: str):
        self.__z1 = z1

    @property
    def z2(self) -> str:
        return self.__z2

    @z2.setter
    def z2(self, z2: str):
        self.__z2 = z2

    @property
    def k5_Z37(self):
        return self.__k5_Z37

    @k5_Z37.setter
    def k5_Z37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_Z__k5_Z37", None)
        self.__k5_Z37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_L3"):
                opp_val = getattr(old_value, "k5_L3", None)
                if opp_val == self:
                    setattr(old_value, "k5_L3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_L3"):
                opp_val = getattr(value, "k5_L3", None)
                setattr(value, "k5_L3", self)

    @property
    def k5_Z(self):
        return self.__k5_Z

    @k5_Z.setter
    def k5_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_Z__k5_Z", None)
        self.__k5_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_X4"):
                opp_val = getattr(old_value, "k5_X4", None)
                if opp_val == self:
                    setattr(old_value, "k5_X4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_X4"):
                opp_val = getattr(value, "k5_X4", None)
                setattr(value, "k5_X4", self)

class k5_P(N):

    pass
class k5_C(G):

    pass
class k5_X:

    pass
class k5_W:

    def __init__(self, w: str, k5_W: "k5_X" = None):
        self.w = w
        self.k5_W = k5_W
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def k5_W(self):
        return self.__k5_W

    @k5_W.setter
    def k5_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_W__k5_W", None)
        self.__k5_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_X8"):
                opp_val = getattr(old_value, "k5_X8", None)
                if opp_val == self:
                    setattr(old_value, "k5_X8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_X8"):
                opp_val = getattr(value, "k5_X8", None)
                setattr(value, "k5_X8", self)

class k5_Y:

    def __init__(self, y: int, k5_Y: "k5_X" = None, k5_Y12: "k5_B" = None):
        self.y = y
        self.k5_Y = k5_Y
        self.k5_Y12 = k5_Y12
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def k5_Y12(self):
        return self.__k5_Y12

    @k5_Y12.setter
    def k5_Y12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_Y__k5_Y12", None)
        self.__k5_Y12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_B11"):
                opp_val = getattr(old_value, "k5_B11", None)
                if opp_val == self:
                    setattr(old_value, "k5_B11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_B11"):
                opp_val = getattr(value, "k5_B11", None)
                setattr(value, "k5_B11", self)

    @property
    def k5_Y(self):
        return self.__k5_Y

    @k5_Y.setter
    def k5_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k5_Y__k5_Y", None)
        self.__k5_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k5_X6"):
                opp_val = getattr(old_value, "k5_X6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k5_X6"):
                opp_val = getattr(value, "k5_X6", None)
                if opp_val is None:
                    setattr(value, "k5_X6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
