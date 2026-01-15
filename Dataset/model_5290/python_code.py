from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BitSeq:

    pass
class BinaryCalculator_Bit(BitSeq):

    def __init__(self, value: str, BinaryCalculator_Bit: "BinaryCalculator_L" = None):
        self.value = value
        self.BinaryCalculator_Bit = BinaryCalculator_Bit
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def BinaryCalculator_Bit(self):
        return self.__BinaryCalculator_Bit

    @BinaryCalculator_Bit.setter
    def BinaryCalculator_Bit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BinaryCalculator_Bit__BinaryCalculator_Bit", None)
        self.__BinaryCalculator_Bit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BinaryCalculator_L8"):
                opp_val = getattr(old_value, "BinaryCalculator_L8", None)
                if opp_val == self:
                    setattr(old_value, "BinaryCalculator_L8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BinaryCalculator_L8"):
                opp_val = getattr(value, "BinaryCalculator_L8", None)
                setattr(value, "BinaryCalculator_L8", self)

class BinaryCalculator_L(BitSeq):

    pass
class BinaryCalculator_Value:

    def __init__(self, value: str, BinaryCalculator_Value: "BinaryCalculator_BinaryCalculator" = None):
        self.value = value
        self.BinaryCalculator_Value = BinaryCalculator_Value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def BinaryCalculator_Value(self):
        return self.__BinaryCalculator_Value

    @BinaryCalculator_Value.setter
    def BinaryCalculator_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BinaryCalculator_Value__BinaryCalculator_Value", None)
        self.__BinaryCalculator_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BinaryCalculator_BinaryCalculator4"):
                opp_val = getattr(old_value, "BinaryCalculator_BinaryCalculator4", None)
                if opp_val == self:
                    setattr(old_value, "BinaryCalculator_BinaryCalculator4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BinaryCalculator_BinaryCalculator4"):
                opp_val = getattr(value, "BinaryCalculator_BinaryCalculator4", None)
                setattr(value, "BinaryCalculator_BinaryCalculator4", self)

class BinaryCalculator_BitSeq(ABC):

    pass
class BinaryCalculator_BinaryCalculator:

    def __init__(self, description: str, BinaryCalculator_BinaryCalculator: "BinaryCalculator_Model" = None, BinaryCalculator_BinaryCalculator2: "BinaryCalculator_BitSeq" = None, BinaryCalculator_BinaryCalculator4: "BinaryCalculator_Value" = None):
        self.description = description
        self.BinaryCalculator_BinaryCalculator = BinaryCalculator_BinaryCalculator
        self.BinaryCalculator_BinaryCalculator2 = BinaryCalculator_BinaryCalculator2
        self.BinaryCalculator_BinaryCalculator4 = BinaryCalculator_BinaryCalculator4
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def BinaryCalculator_BinaryCalculator(self):
        return self.__BinaryCalculator_BinaryCalculator

    @BinaryCalculator_BinaryCalculator.setter
    def BinaryCalculator_BinaryCalculator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BinaryCalculator_BinaryCalculator__BinaryCalculator_BinaryCalculator", None)
        self.__BinaryCalculator_BinaryCalculator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BinaryCalculator_Model"):
                opp_val = getattr(old_value, "BinaryCalculator_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BinaryCalculator_Model"):
                opp_val = getattr(value, "BinaryCalculator_Model", None)
                if opp_val is None:
                    setattr(value, "BinaryCalculator_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BinaryCalculator_BinaryCalculator2(self):
        return self.__BinaryCalculator_BinaryCalculator2

    @BinaryCalculator_BinaryCalculator2.setter
    def BinaryCalculator_BinaryCalculator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BinaryCalculator_BinaryCalculator__BinaryCalculator_BinaryCalculator2", None)
        self.__BinaryCalculator_BinaryCalculator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BinaryCalculator_BitSeq"):
                opp_val = getattr(old_value, "BinaryCalculator_BitSeq", None)
                if opp_val == self:
                    setattr(old_value, "BinaryCalculator_BitSeq", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BinaryCalculator_BitSeq"):
                opp_val = getattr(value, "BinaryCalculator_BitSeq", None)
                setattr(value, "BinaryCalculator_BitSeq", self)

    @property
    def BinaryCalculator_BinaryCalculator4(self):
        return self.__BinaryCalculator_BinaryCalculator4

    @BinaryCalculator_BinaryCalculator4.setter
    def BinaryCalculator_BinaryCalculator4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BinaryCalculator_BinaryCalculator__BinaryCalculator_BinaryCalculator4", None)
        self.__BinaryCalculator_BinaryCalculator4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BinaryCalculator_Value"):
                opp_val = getattr(old_value, "BinaryCalculator_Value", None)
                if opp_val == self:
                    setattr(old_value, "BinaryCalculator_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BinaryCalculator_Value"):
                opp_val = getattr(value, "BinaryCalculator_Value", None)
                setattr(value, "BinaryCalculator_Value", self)

class BinaryCalculator_Model:

    pass