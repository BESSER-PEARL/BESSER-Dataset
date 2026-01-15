from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class T2:

    pass
class k7_DsmlRelation:

    def __init__(self, name: str, mandatory: bool, details: str, k7_DsmlRelation: "k7_T1" = None, k7_DsmlRelation51: "k7_T1" = None, k7_DsmlRelation57: "k7_T1" = None):
        self.name = name
        self.mandatory = mandatory
        self.details = details
        self.k7_DsmlRelation = k7_DsmlRelation
        self.k7_DsmlRelation51 = k7_DsmlRelation51
        self.k7_DsmlRelation57 = k7_DsmlRelation57
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def k7_DsmlRelation51(self):
        return self.__k7_DsmlRelation51

    @k7_DsmlRelation51.setter
    def k7_DsmlRelation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_DsmlRelation__k7_DsmlRelation51", None)
        self.__k7_DsmlRelation51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_T152"):
                opp_val = getattr(old_value, "k7_T152", None)
                if opp_val == self:
                    setattr(old_value, "k7_T152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_T152"):
                opp_val = getattr(value, "k7_T152", None)
                setattr(value, "k7_T152", self)

    @property
    def k7_DsmlRelation57(self):
        return self.__k7_DsmlRelation57

    @k7_DsmlRelation57.setter
    def k7_DsmlRelation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_DsmlRelation__k7_DsmlRelation57", None)
        self.__k7_DsmlRelation57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_T156"):
                opp_val = getattr(old_value, "k7_T156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_T156"):
                opp_val = getattr(value, "k7_T156", None)
                if opp_val is None:
                    setattr(value, "k7_T156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def k7_DsmlRelation(self):
        return self.__k7_DsmlRelation

    @k7_DsmlRelation.setter
    def k7_DsmlRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_DsmlRelation__k7_DsmlRelation", None)
        self.__k7_DsmlRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_T149"):
                opp_val = getattr(old_value, "k7_T149", None)
                if opp_val == self:
                    setattr(old_value, "k7_T149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_T149"):
                opp_val = getattr(value, "k7_T149", None)
                setattr(value, "k7_T149", self)

class k7_T2:

    def __init__(self, id: str, k7_T2: "k7_T1" = None):
        self.id = id
        self.k7_T2 = k7_T2
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def k7_T2(self):
        return self.__k7_T2

    @k7_T2.setter
    def k7_T2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T2__k7_T2", None)
        self.__k7_T2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_T154"):
                opp_val = getattr(old_value, "k7_T154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_T154"):
                opp_val = getattr(value, "k7_T154", None)
                if opp_val is None:
                    setattr(value, "k7_T154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class L1:

    pass
class k7_L3(L1):

    pass
class J:

    pass
class k7_L2:

    def __init__(self, l1: int, l2: int, k7_L2: "k7_Q" = None, k7_L235: "k7_Q" = None, k7_L238: "k7_K" = None):
        self.l1 = l1
        self.l2 = l2
        self.k7_L2 = k7_L2
        self.k7_L235 = k7_L235
        self.k7_L238 = k7_L238
        
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
    def k7_L2(self):
        return self.__k7_L2

    @k7_L2.setter
    def k7_L2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L2__k7_L2", None)
        self.__k7_L2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_Q"):
                opp_val = getattr(old_value, "k7_Q", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_Q"):
                opp_val = getattr(value, "k7_Q", None)
                if opp_val is None:
                    setattr(value, "k7_Q", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def k7_L238(self):
        return self.__k7_L238

    @k7_L238.setter
    def k7_L238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L2__k7_L238", None)
        self.__k7_L238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_K39"):
                opp_val = getattr(old_value, "k7_K39", None)
                if opp_val == self:
                    setattr(old_value, "k7_K39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_K39"):
                opp_val = getattr(value, "k7_K39", None)
                setattr(value, "k7_K39", self)

    @property
    def k7_L235(self):
        return self.__k7_L235

    @k7_L235.setter
    def k7_L235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L2__k7_L235", None)
        self.__k7_L235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_Q36"):
                opp_val = getattr(old_value, "k7_Q36", None)
                if opp_val == self:
                    setattr(old_value, "k7_Q36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_Q36"):
                opp_val = getattr(value, "k7_Q36", None)
                setattr(value, "k7_Q36", self)

class k7_K(J):

    def __init__(self, title: str, k7_K: "k7_P" = None, k7_K39: "k7_L2" = None):
        self.title = title
        self.k7_K = k7_K
        self.k7_K39 = k7_K39
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def k7_K39(self):
        return self.__k7_K39

    @k7_K39.setter
    def k7_K39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_K__k7_K39", None)
        self.__k7_K39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_L238"):
                opp_val = getattr(old_value, "k7_L238", None)
                if opp_val == self:
                    setattr(old_value, "k7_L238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_L238"):
                opp_val = getattr(value, "k7_L238", None)
                setattr(value, "k7_L238", self)

    @property
    def k7_K(self):
        return self.__k7_K

    @k7_K.setter
    def k7_K(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_K__k7_K", None)
        self.__k7_K = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_P24"):
                opp_val = getattr(old_value, "k7_P24", None)
                if opp_val == self:
                    setattr(old_value, "k7_P24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_P24"):
                opp_val = getattr(value, "k7_P24", None)
                setattr(value, "k7_P24", self)

class N:

    pass
class A:

    pass
class k7_J(A):

    pass
class M:

    pass
class k7_N(M):

    pass
class k7_L1:

    def __init__(self, id1: str, id2: int, k7_L1: "k7_M" = None, k7_L129: "k7_C" = None, k7_L132: "k7_M" = None):
        self.id1 = id1
        self.id2 = id2
        self.k7_L1 = k7_L1
        self.k7_L129 = k7_L129
        self.k7_L132 = k7_L132
        
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
    def k7_L1(self):
        return self.__k7_L1

    @k7_L1.setter
    def k7_L1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L1__k7_L1", None)
        self.__k7_L1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_M20"):
                opp_val = getattr(old_value, "k7_M20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_M20"):
                opp_val = getattr(value, "k7_M20", None)
                if opp_val is None:
                    setattr(value, "k7_M20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def k7_L132(self):
        return self.__k7_L132

    @k7_L132.setter
    def k7_L132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L1__k7_L132", None)
        self.__k7_L132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_M33"):
                opp_val = getattr(old_value, "k7_M33", None)
                if opp_val == self:
                    setattr(old_value, "k7_M33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_M33"):
                opp_val = getattr(value, "k7_M33", None)
                setattr(value, "k7_M33", self)

    @property
    def k7_L129(self):
        return self.__k7_L129

    @k7_L129.setter
    def k7_L129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L1__k7_L129", None)
        self.__k7_L129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_C30"):
                opp_val = getattr(old_value, "k7_C30", None)
                if opp_val == self:
                    setattr(old_value, "k7_C30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_C30"):
                opp_val = getattr(value, "k7_C30", None)
                setattr(value, "k7_C30", self)

class k7_G(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class P:

    pass
class k7_Q(P):

    pass
class C:

    pass
class k7_B(C):

    pass
class B:

    pass
class k7_A(B):

    pass
class k7_T1(T2):

    def __init__(self, name: str, k7_T1: "k7_X" = None, k7_T149: "k7_DsmlRelation" = None, k7_T152: "k7_DsmlRelation" = None, k7_T154: set["k7_T2"] = None, k7_T156: set["k7_DsmlRelation"] = None):
        self.name = name
        self.k7_T1 = k7_T1
        self.k7_T149 = k7_T149
        self.k7_T152 = k7_T152
        self.k7_T154 = k7_T154 if k7_T154 is not None else set()
        self.k7_T156 = k7_T156 if k7_T156 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def k7_T156(self):
        return self.__k7_T156

    @k7_T156.setter
    def k7_T156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T1__k7_T156", None)
        self.__k7_T156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "k7_DsmlRelation57"):
                    opp_val = getattr(item, "k7_DsmlRelation57", None)
                    
                    if opp_val == self:
                        setattr(item, "k7_DsmlRelation57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "k7_DsmlRelation57"):
                    opp_val = getattr(item, "k7_DsmlRelation57", None)
                    
                    setattr(item, "k7_DsmlRelation57", self)
                    

    @property
    def k7_T149(self):
        return self.__k7_T149

    @k7_T149.setter
    def k7_T149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T1__k7_T149", None)
        self.__k7_T149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_DsmlRelation"):
                opp_val = getattr(old_value, "k7_DsmlRelation", None)
                if opp_val == self:
                    setattr(old_value, "k7_DsmlRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_DsmlRelation"):
                opp_val = getattr(value, "k7_DsmlRelation", None)
                setattr(value, "k7_DsmlRelation", self)

    @property
    def k7_T154(self):
        return self.__k7_T154

    @k7_T154.setter
    def k7_T154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T1__k7_T154", None)
        self.__k7_T154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "k7_T2"):
                    opp_val = getattr(item, "k7_T2", None)
                    
                    if opp_val == self:
                        setattr(item, "k7_T2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "k7_T2"):
                    opp_val = getattr(item, "k7_T2", None)
                    
                    setattr(item, "k7_T2", self)
                    

    @property
    def k7_T152(self):
        return self.__k7_T152

    @k7_T152.setter
    def k7_T152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T1__k7_T152", None)
        self.__k7_T152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_DsmlRelation51"):
                opp_val = getattr(old_value, "k7_DsmlRelation51", None)
                if opp_val == self:
                    setattr(old_value, "k7_DsmlRelation51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_DsmlRelation51"):
                opp_val = getattr(value, "k7_DsmlRelation51", None)
                setattr(value, "k7_DsmlRelation51", self)

    @property
    def k7_T1(self):
        return self.__k7_T1

    @k7_T1.setter
    def k7_T1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_T1__k7_T1", None)
        self.__k7_T1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_X12"):
                opp_val = getattr(old_value, "k7_X12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_X12"):
                opp_val = getattr(value, "k7_X12", None)
                if opp_val is None:
                    setattr(value, "k7_X12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class k7_L4:

    def __init__(self, id: str, k7_L4: "k7_X" = None, k7_L443: "k7_P" = None, k7_L446: "k7_A" = None):
        self.id = id
        self.k7_L4 = k7_L4
        self.k7_L443 = k7_L443
        self.k7_L446 = k7_L446
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def k7_L443(self):
        return self.__k7_L443

    @k7_L443.setter
    def k7_L443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L4__k7_L443", None)
        self.__k7_L443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_P44"):
                opp_val = getattr(old_value, "k7_P44", None)
                if opp_val == self:
                    setattr(old_value, "k7_P44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_P44"):
                opp_val = getattr(value, "k7_P44", None)
                setattr(value, "k7_P44", self)

    @property
    def k7_L4(self):
        return self.__k7_L4

    @k7_L4.setter
    def k7_L4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L4__k7_L4", None)
        self.__k7_L4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_X10"):
                opp_val = getattr(old_value, "k7_X10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_X10"):
                opp_val = getattr(value, "k7_X10", None)
                if opp_val is None:
                    setattr(value, "k7_X10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def k7_L446(self):
        return self.__k7_L446

    @k7_L446.setter
    def k7_L446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_L4__k7_L446", None)
        self.__k7_L446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_A47"):
                opp_val = getattr(old_value, "k7_A47", None)
                if opp_val == self:
                    setattr(old_value, "k7_A47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_A47"):
                opp_val = getattr(value, "k7_A47", None)
                setattr(value, "k7_A47", self)

class k7_W:

    def __init__(self, w: str, k7_W: "k7_X" = None):
        self.w = w
        self.k7_W = k7_W
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

    @property
    def k7_W(self):
        return self.__k7_W

    @k7_W.setter
    def k7_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_W__k7_W", None)
        self.__k7_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_X8"):
                opp_val = getattr(old_value, "k7_X8", None)
                if opp_val == self:
                    setattr(old_value, "k7_X8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_X8"):
                opp_val = getattr(value, "k7_X8", None)
                setattr(value, "k7_X8", self)

class k7_Y:

    def __init__(self, y: int, k7_Y: "k7_X" = None, k7_Y16: "k7_B" = None):
        self.y = y
        self.k7_Y = k7_Y
        self.k7_Y16 = k7_Y16
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def k7_Y16(self):
        return self.__k7_Y16

    @k7_Y16.setter
    def k7_Y16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_Y__k7_Y16", None)
        self.__k7_Y16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_B15"):
                opp_val = getattr(old_value, "k7_B15", None)
                if opp_val == self:
                    setattr(old_value, "k7_B15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_B15"):
                opp_val = getattr(value, "k7_B15", None)
                setattr(value, "k7_B15", self)

    @property
    def k7_Y(self):
        return self.__k7_Y

    @k7_Y.setter
    def k7_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_Y__k7_Y", None)
        self.__k7_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_X6"):
                opp_val = getattr(old_value, "k7_X6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_X6"):
                opp_val = getattr(value, "k7_X6", None)
                if opp_val is None:
                    setattr(value, "k7_X6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class k7_Z:

    def __init__(self, z1: str, z2: str, z3: str, k7_Z: "k7_X" = None, k7_Z41: "k7_L3" = None):
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.k7_Z = k7_Z
        self.k7_Z41 = k7_Z41
        
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
    def z3(self) -> str:
        return self.__z3

    @z3.setter
    def z3(self, z3: str):
        self.__z3 = z3

    @property
    def k7_Z41(self):
        return self.__k7_Z41

    @k7_Z41.setter
    def k7_Z41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_Z__k7_Z41", None)
        self.__k7_Z41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_L3"):
                opp_val = getattr(old_value, "k7_L3", None)
                if opp_val == self:
                    setattr(old_value, "k7_L3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_L3"):
                opp_val = getattr(value, "k7_L3", None)
                setattr(value, "k7_L3", self)

    @property
    def k7_Z(self):
        return self.__k7_Z

    @k7_Z.setter
    def k7_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_k7_Z__k7_Z", None)
        self.__k7_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "k7_X4"):
                opp_val = getattr(old_value, "k7_X4", None)
                if opp_val == self:
                    setattr(old_value, "k7_X4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "k7_X4"):
                opp_val = getattr(value, "k7_X4", None)
                setattr(value, "k7_X4", self)

class G:

    pass
class k7_I(G):

    pass
class k7_M(G):

    pass
class k7_C(G):

    pass
class k7_X:

    pass
class k7_P(N):

    pass