from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class L1:

    pass
class anol3l4_L4(L1):

    pass
class anol3l4_L3(L1):

    pass
class J:

    pass
class anol3l4_L2:

    def __init__(self, l1: int, l2: int, anol3l4_L2: "anol3l4_Q" = None, anol3l4_L228: "anol3l4_Q" = None, anol3l4_L231: "anol3l4_K" = None):
        self.l1 = l1
        self.l2 = l2
        self.anol3l4_L2 = anol3l4_L2
        self.anol3l4_L228 = anol3l4_L228
        self.anol3l4_L231 = anol3l4_L231
        
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
    def anol3l4_L228(self):
        return self.__anol3l4_L228

    @anol3l4_L228.setter
    def anol3l4_L228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L2__anol3l4_L228", None)
        self.__anol3l4_L228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_Q29"):
                opp_val = getattr(old_value, "anol3l4_Q29", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_Q29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_Q29"):
                opp_val = getattr(value, "anol3l4_Q29", None)
                setattr(value, "anol3l4_Q29", self)

    @property
    def anol3l4_L2(self):
        return self.__anol3l4_L2

    @anol3l4_L2.setter
    def anol3l4_L2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L2__anol3l4_L2", None)
        self.__anol3l4_L2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_Q"):
                opp_val = getattr(old_value, "anol3l4_Q", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_Q"):
                opp_val = getattr(value, "anol3l4_Q", None)
                if opp_val is None:
                    setattr(value, "anol3l4_Q", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def anol3l4_L231(self):
        return self.__anol3l4_L231

    @anol3l4_L231.setter
    def anol3l4_L231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L2__anol3l4_L231", None)
        self.__anol3l4_L231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_K32"):
                opp_val = getattr(old_value, "anol3l4_K32", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_K32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_K32"):
                opp_val = getattr(value, "anol3l4_K32", None)
                setattr(value, "anol3l4_K32", self)

class N:

    pass
class P:

    pass
class anol3l4_Q(P):

    pass
class anol3l4_K(J):

    def __init__(self, title: str, anol3l4_K: "anol3l4_P" = None, anol3l4_K32: "anol3l4_L2" = None):
        self.title = title
        self.anol3l4_K = anol3l4_K
        self.anol3l4_K32 = anol3l4_K32
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def anol3l4_K(self):
        return self.__anol3l4_K

    @anol3l4_K.setter
    def anol3l4_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_K__anol3l4_K", None)
        self.__anol3l4_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_P17"):
                opp_val = getattr(old_value, "anol3l4_P17", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_P17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_P17"):
                opp_val = getattr(value, "anol3l4_P17", None)
                setattr(value, "anol3l4_P17", self)

    @property
    def anol3l4_K32(self):
        return self.__anol3l4_K32

    @anol3l4_K32.setter
    def anol3l4_K32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_K__anol3l4_K32", None)
        self.__anol3l4_K32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_L231"):
                opp_val = getattr(old_value, "anol3l4_L231", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_L231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_L231"):
                opp_val = getattr(value, "anol3l4_L231", None)
                setattr(value, "anol3l4_L231", self)

class anol3l4_L1:

    def __init__(self, id1: str, id2: int, anol3l4_L1: "anol3l4_M" = None, anol3l4_L122: "anol3l4_C" = None, anol3l4_L125: "anol3l4_M" = None):
        self.id1 = id1
        self.id2 = id2
        self.anol3l4_L1 = anol3l4_L1
        self.anol3l4_L122 = anol3l4_L122
        self.anol3l4_L125 = anol3l4_L125
        
    @property
    def id1(self) -> str:
        return self.__id1

    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def id2(self) -> int:
        return self.__id2

    @id2.setter
    def id2(self, id2: int):
        self.__id2 = id2

    @property
    def anol3l4_L125(self):
        return self.__anol3l4_L125

    @anol3l4_L125.setter
    def anol3l4_L125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L1__anol3l4_L125", None)
        self.__anol3l4_L125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_M26"):
                opp_val = getattr(old_value, "anol3l4_M26", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_M26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_M26"):
                opp_val = getattr(value, "anol3l4_M26", None)
                setattr(value, "anol3l4_M26", self)

    @property
    def anol3l4_L1(self):
        return self.__anol3l4_L1

    @anol3l4_L1.setter
    def anol3l4_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L1__anol3l4_L1", None)
        self.__anol3l4_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_M13"):
                opp_val = getattr(old_value, "anol3l4_M13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_M13"):
                opp_val = getattr(value, "anol3l4_M13", None)
                if opp_val is None:
                    setattr(value, "anol3l4_M13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def anol3l4_L122(self):
        return self.__anol3l4_L122

    @anol3l4_L122.setter
    def anol3l4_L122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_L1__anol3l4_L122", None)
        self.__anol3l4_L122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_C23"):
                opp_val = getattr(old_value, "anol3l4_C23", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_C23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_C23"):
                opp_val = getattr(value, "anol3l4_C23", None)
                setattr(value, "anol3l4_C23", self)

class A:

    pass
class anol3l4_J(A):

    pass
class M:

    pass
class anol3l4_N(M):

    pass
class C:

    pass
class anol3l4_B(C):

    pass
class B:

    pass
class anol3l4_A(B):

    pass
class anol3l4_W:

    def __init__(self, w: str, anol3l4_W: "anol3l4_X" = None):
        self.w = w
        self.anol3l4_W = anol3l4_W
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def anol3l4_W(self):
        return self.__anol3l4_W

    @anol3l4_W.setter
    def anol3l4_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_W__anol3l4_W", None)
        self.__anol3l4_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_X8"):
                opp_val = getattr(old_value, "anol3l4_X8", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_X8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_X8"):
                opp_val = getattr(value, "anol3l4_X8", None)
                setattr(value, "anol3l4_X8", self)

class anol3l4_Y:

    def __init__(self, y: int, anol3l4_Y: "anol3l4_X" = None):
        self.y = y
        self.anol3l4_Y = anol3l4_Y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def anol3l4_Y(self):
        return self.__anol3l4_Y

    @anol3l4_Y.setter
    def anol3l4_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_Y__anol3l4_Y", None)
        self.__anol3l4_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_X6"):
                opp_val = getattr(old_value, "anol3l4_X6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_X6"):
                opp_val = getattr(value, "anol3l4_X6", None)
                if opp_val is None:
                    setattr(value, "anol3l4_X6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class anol3l4_G(ABC):

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
class anol3l4_M(G):

    pass
class anol3l4_I(G):

    pass
class anol3l4_Z:

    def __init__(self, z1: str, z2: str, z3: str, anol3l4_Z: "anol3l4_X" = None, anol3l4_Z36: "anol3l4_L4" = None):
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.anol3l4_Z = anol3l4_Z
        self.anol3l4_Z36 = anol3l4_Z36
        
    @property
    def z1(self) -> str:
        return self.__z1

    @z1.setter
    def z1(self, z1: str):
        self.__z1 = z1

    @property
    def z3(self) -> str:
        return self.__z3

    @z3.setter
    def z3(self, z3: str):
        self.__z3 = z3

    @property
    def z2(self) -> str:
        return self.__z2

    @z2.setter
    def z2(self, z2: str):
        self.__z2 = z2

    @property
    def anol3l4_Z(self):
        return self.__anol3l4_Z

    @anol3l4_Z.setter
    def anol3l4_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_Z__anol3l4_Z", None)
        self.__anol3l4_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_X4"):
                opp_val = getattr(old_value, "anol3l4_X4", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_X4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_X4"):
                opp_val = getattr(value, "anol3l4_X4", None)
                setattr(value, "anol3l4_X4", self)

    @property
    def anol3l4_Z36(self):
        return self.__anol3l4_Z36

    @anol3l4_Z36.setter
    def anol3l4_Z36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_anol3l4_Z__anol3l4_Z36", None)
        self.__anol3l4_Z36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "anol3l4_L4"):
                opp_val = getattr(old_value, "anol3l4_L4", None)
                if opp_val == self:
                    setattr(old_value, "anol3l4_L4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "anol3l4_L4"):
                opp_val = getattr(value, "anol3l4_L4", None)
                setattr(value, "anol3l4_L4", self)

class anol3l4_P(N):

    pass
class anol3l4_C(G):

    pass
class anol3l4_X:

    pass