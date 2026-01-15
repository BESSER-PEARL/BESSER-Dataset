from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class VHDLModel_VHDLSpecification:

    def __init__(self, name: str, VHDLModel_VHDLSpecification: set["VHDLModel_CompositeBlock"] = None):
        self.name = name
        self.VHDLModel_VHDLSpecification = VHDLModel_VHDLSpecification if VHDLModel_VHDLSpecification is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VHDLModel_VHDLSpecification(self):
        return self.__VHDLModel_VHDLSpecification

    @VHDLModel_VHDLSpecification.setter
    def VHDLModel_VHDLSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_VHDLSpecification__VHDLModel_VHDLSpecification", None)
        self.__VHDLModel_VHDLSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VHDLModel_CompositeBlock25"):
                    opp_val = getattr(item, "VHDLModel_CompositeBlock25", None)
                    
                    if opp_val == self:
                        setattr(item, "VHDLModel_CompositeBlock25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VHDLModel_CompositeBlock25"):
                    opp_val = getattr(item, "VHDLModel_CompositeBlock25", None)
                    
                    setattr(item, "VHDLModel_CompositeBlock25", self)
                    

class Port:

    pass
class VHDLModel_Signal(Port):

    pass
class VHDLModel_OutputPort(Port):

    pass
class VHDLModel_Port(ABC):

    def __init__(self, name: str, high: bool, VHDLModel_Port: "VHDLModel_ComplexBlock" = None, VHDLModel_Port20: "VHDLModel_Port" = None, VHDLModel_Port18: "VHDLModel_Port" = None, VHDLModel_Port22: "VHDLModel_Block" = None):
        self.name = name
        self.high = high
        self.VHDLModel_Port = VHDLModel_Port
        self.VHDLModel_Port20 = VHDLModel_Port20
        self.VHDLModel_Port18 = VHDLModel_Port18
        self.VHDLModel_Port22 = VHDLModel_Port22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def high(self) -> bool:
        return self.__high

    @high.setter
    def high(self, high: bool):
        self.__high = high

    @property
    def VHDLModel_Port22(self):
        return self.__VHDLModel_Port22

    @VHDLModel_Port22.setter
    def VHDLModel_Port22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Port__VHDLModel_Port22", None)
        self.__VHDLModel_Port22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_Block23"):
                opp_val = getattr(old_value, "VHDLModel_Block23", None)
                if opp_val == self:
                    setattr(old_value, "VHDLModel_Block23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_Block23"):
                opp_val = getattr(value, "VHDLModel_Block23", None)
                setattr(value, "VHDLModel_Block23", self)

    @property
    def VHDLModel_Port20(self):
        return self.__VHDLModel_Port20

    @VHDLModel_Port20.setter
    def VHDLModel_Port20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Port__VHDLModel_Port20", None)
        self.__VHDLModel_Port20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_Port18"):
                opp_val = getattr(old_value, "VHDLModel_Port18", None)
                if opp_val == self:
                    setattr(old_value, "VHDLModel_Port18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_Port18"):
                opp_val = getattr(value, "VHDLModel_Port18", None)
                setattr(value, "VHDLModel_Port18", self)

    @property
    def VHDLModel_Port18(self):
        return self.__VHDLModel_Port18

    @VHDLModel_Port18.setter
    def VHDLModel_Port18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Port__VHDLModel_Port18", None)
        self.__VHDLModel_Port18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_Port20"):
                opp_val = getattr(old_value, "VHDLModel_Port20", None)
                if opp_val == self:
                    setattr(old_value, "VHDLModel_Port20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_Port20"):
                opp_val = getattr(value, "VHDLModel_Port20", None)
                setattr(value, "VHDLModel_Port20", self)

    @property
    def VHDLModel_Port(self):
        return self.__VHDLModel_Port

    @VHDLModel_Port.setter
    def VHDLModel_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Port__VHDLModel_Port", None)
        self.__VHDLModel_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_ComplexBlock"):
                opp_val = getattr(old_value, "VHDLModel_ComplexBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_ComplexBlock"):
                opp_val = getattr(value, "VHDLModel_ComplexBlock", None)
                if opp_val is None:
                    setattr(value, "VHDLModel_ComplexBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComplexBlock:

    pass
class VHDLModel_CompositeBlock(ComplexBlock):

    pass
class VHDLModel_BlockRef(ComplexBlock):

    pass
class VHDLModel_Block(ABC):

    def __init__(self, name: str, VHDLModel_Block: set["VHDLModel_InputPort"] = None, VHDLModel_Block23: "VHDLModel_Port" = None, VHDLModel_Block12: "VHDLModel_CompositeBlock" = None):
        self.name = name
        self.VHDLModel_Block = VHDLModel_Block if VHDLModel_Block is not None else set()
        self.VHDLModel_Block23 = VHDLModel_Block23
        self.VHDLModel_Block12 = VHDLModel_Block12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VHDLModel_Block23(self):
        return self.__VHDLModel_Block23

    @VHDLModel_Block23.setter
    def VHDLModel_Block23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Block__VHDLModel_Block23", None)
        self.__VHDLModel_Block23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_Port22"):
                opp_val = getattr(old_value, "VHDLModel_Port22", None)
                if opp_val == self:
                    setattr(old_value, "VHDLModel_Port22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_Port22"):
                opp_val = getattr(value, "VHDLModel_Port22", None)
                setattr(value, "VHDLModel_Port22", self)

    @property
    def VHDLModel_Block(self):
        return self.__VHDLModel_Block

    @VHDLModel_Block.setter
    def VHDLModel_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Block__VHDLModel_Block", None)
        self.__VHDLModel_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VHDLModel_InputPort7"):
                    opp_val = getattr(item, "VHDLModel_InputPort7", None)
                    
                    if opp_val == self:
                        setattr(item, "VHDLModel_InputPort7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VHDLModel_InputPort7"):
                    opp_val = getattr(item, "VHDLModel_InputPort7", None)
                    
                    setattr(item, "VHDLModel_InputPort7", self)
                    

    @property
    def VHDLModel_Block12(self):
        return self.__VHDLModel_Block12

    @VHDLModel_Block12.setter
    def VHDLModel_Block12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VHDLModel_Block__VHDLModel_Block12", None)
        self.__VHDLModel_Block12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VHDLModel_CompositeBlock11"):
                opp_val = getattr(old_value, "VHDLModel_CompositeBlock11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VHDLModel_CompositeBlock11"):
                opp_val = getattr(value, "VHDLModel_CompositeBlock11", None)
                if opp_val is None:
                    setattr(value, "VHDLModel_CompositeBlock11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VHDLModel_InputPort(Port):

    pass
class Block:

    pass
class VHDLModel_ComplexBlock(Block):

    pass
class VHDLModel_NotGate(Block):

    pass
class VHDLModel_BinaryGate(Block):

    pass
class BinaryGate:

    pass
class VHDLModel_OrGate(BinaryGate):

    pass
class VHDLModel_AndGate(BinaryGate):

    pass