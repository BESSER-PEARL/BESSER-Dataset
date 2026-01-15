from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StyleKind(Enum):
    Style1 = "Style1"
    Style2 = "Style2"


############################################
# Definition of Classes
############################################

class D3_B:

    pass
class B:

    pass
class D3:

    pass
class abcd_D3_B(B, D3):

    pass
class D:

    pass
class abcd_D2(D):

    def __init__(self, commonOfD: str):
        self.commonOfD = commonOfD
        
    @property
    def commonOfD(self) -> str:
        return self.__commonOfD

    @commonOfD.setter
    def commonOfD(self, commonOfD: str):
        self.__commonOfD = commonOfD

class abcd_D1(D):

    def __init__(self, commonOfD: str):
        self.commonOfD = commonOfD
        
    @property
    def commonOfD(self) -> str:
        return self.__commonOfD

    @commonOfD.setter
    def commonOfD(self, commonOfD: str):
        self.__commonOfD = commonOfD

class C:

    pass
class abcd_D3_B_C(D3_B, C):

    pass
class abcd_C2(C):

    def __init__(self, propOfC2: str):
        self.propOfC2 = propOfC2
        
    @property
    def propOfC2(self) -> str:
        return self.__propOfC2

    @propOfC2.setter
    def propOfC2(self, propOfC2: str):
        self.__propOfC2 = propOfC2

class abcd_C1(C):

    def __init__(self, propOfC1: str):
        self.propOfC1 = propOfC1
        
    @property
    def propOfC1(self) -> str:
        return self.__propOfC1

    @propOfC1.setter
    def propOfC1(self, propOfC1: str):
        self.__propOfC1 = propOfC1

class A:

    pass
class abcd_D3(D):

    def __init__(self, commonOfD: str):
        self.commonOfD = commonOfD
        
    @property
    def commonOfD(self) -> str:
        return self.__commonOfD

    @commonOfD.setter
    def commonOfD(self, commonOfD: str):
        self.__commonOfD = commonOfD

class abcd_D(A):

    def __init__(self, propOfD: str, abcd_D: "abcd_Model" = None):
        self.propOfD = propOfD
        self.abcd_D = abcd_D
        
    @property
    def propOfD(self) -> str:
        return self.__propOfD

    @propOfD.setter
    def propOfD(self, propOfD: str):
        self.__propOfD = propOfD

    @property
    def abcd_D(self):
        return self.__abcd_D

    @abcd_D.setter
    def abcd_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_D__abcd_D", None)
        self.__abcd_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_Model11"):
                opp_val = getattr(old_value, "abcd_Model11", None)
                if opp_val == self:
                    setattr(old_value, "abcd_Model11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_Model11"):
                opp_val = getattr(value, "abcd_Model11", None)
                setattr(value, "abcd_Model11", self)

class abcd_C(A):

    def __init__(self, propOfC: str, abcd_C: "abcd_Model" = None):
        self.propOfC = propOfC
        self.abcd_C = abcd_C
        
    @property
    def propOfC(self) -> str:
        return self.__propOfC

    @propOfC.setter
    def propOfC(self, propOfC: str):
        self.__propOfC = propOfC

    @property
    def abcd_C(self):
        return self.__abcd_C

    @abcd_C.setter
    def abcd_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_C__abcd_C", None)
        self.__abcd_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_Model9"):
                opp_val = getattr(old_value, "abcd_Model9", None)
                if opp_val == self:
                    setattr(old_value, "abcd_Model9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_Model9"):
                opp_val = getattr(value, "abcd_Model9", None)
                setattr(value, "abcd_Model9", self)

class abcd_B(A):

    def __init__(self, propOfB: str, abcd_B: "abcd_Model" = None):
        self.propOfB = propOfB
        self.abcd_B = abcd_B
        
    @property
    def propOfB(self) -> str:
        return self.__propOfB

    @propOfB.setter
    def propOfB(self, propOfB: str):
        self.__propOfB = propOfB

    @property
    def abcd_B(self):
        return self.__abcd_B

    @abcd_B.setter
    def abcd_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_B__abcd_B", None)
        self.__abcd_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_Model7"):
                opp_val = getattr(old_value, "abcd_Model7", None)
                if opp_val == self:
                    setattr(old_value, "abcd_Model7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_Model7"):
                opp_val = getattr(value, "abcd_Model7", None)
                setattr(value, "abcd_Model7", self)

class NamedElt:

    pass
class abcd_A(NamedElt):

    def __init__(self, anIntegerAttr: int, aBooleanAttr: str, abcd_A: "abcd_Model" = None, abcd_A5: "abcd_Model" = None, abcd_A14: "abcd_A" = None, abcd_A12: set["abcd_A"] = None):
        self.anIntegerAttr = anIntegerAttr
        self.aBooleanAttr = aBooleanAttr
        self.abcd_A = abcd_A
        self.abcd_A5 = abcd_A5
        self.abcd_A14 = abcd_A14
        self.abcd_A12 = abcd_A12 if abcd_A12 is not None else set()
        
    @property
    def anIntegerAttr(self) -> int:
        return self.__anIntegerAttr

    @anIntegerAttr.setter
    def anIntegerAttr(self, anIntegerAttr: int):
        self.__anIntegerAttr = anIntegerAttr

    @property
    def aBooleanAttr(self) -> str:
        return self.__aBooleanAttr

    @aBooleanAttr.setter
    def aBooleanAttr(self, aBooleanAttr: str):
        self.__aBooleanAttr = aBooleanAttr

    @property
    def abcd_A12(self):
        return self.__abcd_A12

    @abcd_A12.setter
    def abcd_A12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_A__abcd_A12", None)
        self.__abcd_A12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abcd_A14"):
                    opp_val = getattr(item, "abcd_A14", None)
                    
                    if opp_val == self:
                        setattr(item, "abcd_A14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abcd_A14"):
                    opp_val = getattr(item, "abcd_A14", None)
                    
                    setattr(item, "abcd_A14", self)
                    

    @property
    def abcd_A5(self):
        return self.__abcd_A5

    @abcd_A5.setter
    def abcd_A5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_A__abcd_A5", None)
        self.__abcd_A5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_Model4"):
                opp_val = getattr(old_value, "abcd_Model4", None)
                if opp_val == self:
                    setattr(old_value, "abcd_Model4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_Model4"):
                opp_val = getattr(value, "abcd_Model4", None)
                setattr(value, "abcd_Model4", self)

    @property
    def abcd_A14(self):
        return self.__abcd_A14

    @abcd_A14.setter
    def abcd_A14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_A__abcd_A14", None)
        self.__abcd_A14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_A12"):
                opp_val = getattr(old_value, "abcd_A12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_A12"):
                opp_val = getattr(value, "abcd_A12", None)
                if opp_val is None:
                    setattr(value, "abcd_A12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def abcd_A(self):
        return self.__abcd_A

    @abcd_A.setter
    def abcd_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_A__abcd_A", None)
        self.__abcd_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_Model"):
                opp_val = getattr(old_value, "abcd_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_Model"):
                opp_val = getattr(value, "abcd_Model", None)
                if opp_val is None:
                    setattr(value, "abcd_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abcd_Other(NamedElt):

    pass
class abcd_Model(NamedElt):

    def __init__(self, style: str, abcd_Model: set["abcd_A"] = None, abcd_Model2: set["abcd_Other"] = None, abcd_Model4: "abcd_A" = None, abcd_Model7: "abcd_B" = None, abcd_Model9: "abcd_C" = None, abcd_Model11: "abcd_D" = None):
        self.style = style
        self.abcd_Model = abcd_Model if abcd_Model is not None else set()
        self.abcd_Model2 = abcd_Model2 if abcd_Model2 is not None else set()
        self.abcd_Model4 = abcd_Model4
        self.abcd_Model7 = abcd_Model7
        self.abcd_Model9 = abcd_Model9
        self.abcd_Model11 = abcd_Model11
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def abcd_Model(self):
        return self.__abcd_Model

    @abcd_Model.setter
    def abcd_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model", None)
        self.__abcd_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abcd_A"):
                    opp_val = getattr(item, "abcd_A", None)
                    
                    if opp_val == self:
                        setattr(item, "abcd_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abcd_A"):
                    opp_val = getattr(item, "abcd_A", None)
                    
                    setattr(item, "abcd_A", self)
                    

    @property
    def abcd_Model2(self):
        return self.__abcd_Model2

    @abcd_Model2.setter
    def abcd_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model2", None)
        self.__abcd_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abcd_Other"):
                    opp_val = getattr(item, "abcd_Other", None)
                    
                    if opp_val == self:
                        setattr(item, "abcd_Other", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abcd_Other"):
                    opp_val = getattr(item, "abcd_Other", None)
                    
                    setattr(item, "abcd_Other", self)
                    

    @property
    def abcd_Model9(self):
        return self.__abcd_Model9

    @abcd_Model9.setter
    def abcd_Model9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model9", None)
        self.__abcd_Model9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_C"):
                opp_val = getattr(old_value, "abcd_C", None)
                if opp_val == self:
                    setattr(old_value, "abcd_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_C"):
                opp_val = getattr(value, "abcd_C", None)
                setattr(value, "abcd_C", self)

    @property
    def abcd_Model7(self):
        return self.__abcd_Model7

    @abcd_Model7.setter
    def abcd_Model7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model7", None)
        self.__abcd_Model7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_B"):
                opp_val = getattr(old_value, "abcd_B", None)
                if opp_val == self:
                    setattr(old_value, "abcd_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_B"):
                opp_val = getattr(value, "abcd_B", None)
                setattr(value, "abcd_B", self)

    @property
    def abcd_Model4(self):
        return self.__abcd_Model4

    @abcd_Model4.setter
    def abcd_Model4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model4", None)
        self.__abcd_Model4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_A5"):
                opp_val = getattr(old_value, "abcd_A5", None)
                if opp_val == self:
                    setattr(old_value, "abcd_A5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_A5"):
                opp_val = getattr(value, "abcd_A5", None)
                setattr(value, "abcd_A5", self)

    @property
    def abcd_Model11(self):
        return self.__abcd_Model11

    @abcd_Model11.setter
    def abcd_Model11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abcd_Model__abcd_Model11", None)
        self.__abcd_Model11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abcd_D"):
                opp_val = getattr(old_value, "abcd_D", None)
                if opp_val == self:
                    setattr(old_value, "abcd_D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abcd_D"):
                opp_val = getattr(value, "abcd_D", None)
                setattr(value, "abcd_D", self)

class abcd_NamedElt(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
