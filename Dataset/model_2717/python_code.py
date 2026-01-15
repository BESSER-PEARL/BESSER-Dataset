from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class L1:

    pass
class k4_L4(L1):

    pass
class k4_L3(L1):

    pass
class J:

    pass
class k4_L2:

    def __init__(self, l1: int, l2: int, k4_L2: "k4_Q" = None, k4_L228: "k4_Q" = None, k4_L231: "k4_K" = None):
        self.l1 = l1
        self.l2 = l2
        self.k4_L2 = k4_L2
        self.k4_L228 = k4_L228
        self.k4_L231 = k4_L231
        
    @property
    def l2(self) -> int:
        return self.__l2

    @l2.setter
    def l2(self, l2: int):
        self.__l2 = l2

    @property
    def l1(self) -> int:
        return self.__l1

    @l1.setter
    def l1(self, l1: int):
        self.__l1 = l1

    @property
    def k4_L228(self):
        return self.__k4_L228

    @k4_L228.setter
    def k4_L228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L2__k4_L228", None)
        self.__k4_L228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_Q29"):
                opp_val = getattr(old_value, "k4_Q29", None)
                if opp_val == self:
                    setattr(old_value, "k4_Q29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_Q29"):
                opp_val = getattr(value, "k4_Q29", None)
                setattr(value, "k4_Q29", self)

    @property
    def k4_L231(self):
        return self.__k4_L231

    @k4_L231.setter
    def k4_L231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L2__k4_L231", None)
        self.__k4_L231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_K32"):
                opp_val = getattr(old_value, "k4_K32", None)
                if opp_val == self:
                    setattr(old_value, "k4_K32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_K32"):
                opp_val = getattr(value, "k4_K32", None)
                setattr(value, "k4_K32", self)

    @property
    def k4_L2(self):
        return self.__k4_L2

    @k4_L2.setter
    def k4_L2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L2__k4_L2", None)
        self.__k4_L2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_Q"):
                opp_val = getattr(old_value, "k4_Q", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_Q"):
                opp_val = getattr(value, "k4_Q", None)
                if opp_val is None:
                    setattr(value, "k4_Q", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class k4_K(J):

    def __init__(self, title: str, k4_K: "k4_P" = None, k4_K32: "k4_L2" = None):
        self.title = title
        self.k4_K = k4_K
        self.k4_K32 = k4_K32
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def k4_K(self):
        return self.__k4_K

    @k4_K.setter
    def k4_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_K__k4_K", None)
        self.__k4_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_P17"):
                opp_val = getattr(old_value, "k4_P17", None)
                if opp_val == self:
                    setattr(old_value, "k4_P17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_P17"):
                opp_val = getattr(value, "k4_P17", None)
                setattr(value, "k4_P17", self)

    @property
    def k4_K32(self):
        return self.__k4_K32

    @k4_K32.setter
    def k4_K32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_K__k4_K32", None)
        self.__k4_K32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_L231"):
                opp_val = getattr(old_value, "k4_L231", None)
                if opp_val == self:
                    setattr(old_value, "k4_L231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_L231"):
                opp_val = getattr(value, "k4_L231", None)
                setattr(value, "k4_L231", self)

class N:

    pass
class P:

    pass
class k4_Q(P):

    pass
class k4_L1:

    def __init__(self, id1: str, id2: int, k4_L1: "k4_M" = None, k4_L122: "k4_C" = None, k4_L125: "k4_M" = None):
        self.id1 = id1
        self.id2 = id2
        self.k4_L1 = k4_L1
        self.k4_L122 = k4_L122
        self.k4_L125 = k4_L125
        
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
    def k4_L122(self):
        return self.__k4_L122

    @k4_L122.setter
    def k4_L122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L1__k4_L122", None)
        self.__k4_L122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_C23"):
                opp_val = getattr(old_value, "k4_C23", None)
                if opp_val == self:
                    setattr(old_value, "k4_C23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_C23"):
                opp_val = getattr(value, "k4_C23", None)
                setattr(value, "k4_C23", self)

    @property
    def k4_L125(self):
        return self.__k4_L125

    @k4_L125.setter
    def k4_L125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L1__k4_L125", None)
        self.__k4_L125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_M26"):
                opp_val = getattr(old_value, "k4_M26", None)
                if opp_val == self:
                    setattr(old_value, "k4_M26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_M26"):
                opp_val = getattr(value, "k4_M26", None)
                setattr(value, "k4_M26", self)

    @property
    def k4_L1(self):
        return self.__k4_L1

    @k4_L1.setter
    def k4_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_L1__k4_L1", None)
        self.__k4_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_M13"):
                opp_val = getattr(old_value, "k4_M13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_M13"):
                opp_val = getattr(value, "k4_M13", None)
                if opp_val is None:
                    setattr(value, "k4_M13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class A:

    pass
class k4_J(A):

    pass
class M:

    pass
class k4_N(M):

    pass
class k4_G(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class k4_P(N):

    pass
class G:

    pass
class k4_M(G):

    pass
class k4_I(G):

    pass
class C:

    pass
class k4_B(C):

    pass
class B:

    pass
class k4_A(B):

    pass
class k4_W:

    def __init__(self, w: str, k4_W: "k4_X" = None):
        self.w = w
        self.k4_W = k4_W
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def k4_W(self):
        return self.__k4_W

    @k4_W.setter
    def k4_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_W__k4_W", None)
        self.__k4_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_X8"):
                opp_val = getattr(old_value, "k4_X8", None)
                if opp_val == self:
                    setattr(old_value, "k4_X8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_X8"):
                opp_val = getattr(value, "k4_X8", None)
                setattr(value, "k4_X8", self)

class k4_Y:

    def __init__(self, y: int, k4_Y: "k4_X" = None):
        self.y = y
        self.k4_Y = k4_Y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def k4_Y(self):
        return self.__k4_Y

    @k4_Y.setter
    def k4_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_Y__k4_Y", None)
        self.__k4_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_X6"):
                opp_val = getattr(old_value, "k4_X6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_X6"):
                opp_val = getattr(value, "k4_X6", None)
                if opp_val is None:
                    setattr(value, "k4_X6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class k4_Z:

    def __init__(self, z1: str, z2: str, z3: str, k4_Z: "k4_X" = None, k4_Z36: "k4_L4" = None):
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.k4_Z = k4_Z
        self.k4_Z36 = k4_Z36
        
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
    def k4_Z(self):
        return self.__k4_Z

    @k4_Z.setter
    def k4_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_Z__k4_Z", None)
        self.__k4_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_X4"):
                opp_val = getattr(old_value, "k4_X4", None)
                if opp_val == self:
                    setattr(old_value, "k4_X4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_X4"):
                opp_val = getattr(value, "k4_X4", None)
                setattr(value, "k4_X4", self)

    @property
    def k4_Z36(self):
        return self.__k4_Z36

    @k4_Z36.setter
    def k4_Z36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k4_Z__k4_Z36", None)
        self.__k4_Z36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k4_L4"):
                opp_val = getattr(old_value, "k4_L4", None)
                if opp_val == self:
                    setattr(old_value, "k4_L4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k4_L4"):
                opp_val = getattr(value, "k4_L4", None)
                setattr(value, "k4_L4", self)

class k4_C(G):

    pass
class k4_X:

    pass