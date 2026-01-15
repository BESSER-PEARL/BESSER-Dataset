from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class A:

    pass
class systemmodel_B(A):

    pass
class ModelElement:

    pass
class systemmodel_C(ModelElement):

    def __init__(self, name: str, systemmodel_C: "systemmodel_A" = None):
        self.name = name
        self.systemmodel_C = systemmodel_C
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def systemmodel_C(self):
        return self.__systemmodel_C

    @systemmodel_C.setter
    def systemmodel_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_C__systemmodel_C", None)
        self.__systemmodel_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemmodel_A17"):
                opp_val = getattr(old_value, "systemmodel_A17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemmodel_A17"):
                opp_val = getattr(value, "systemmodel_A17", None)
                if opp_val is None:
                    setattr(value, "systemmodel_A17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class systemmodel_A(ModelElement):

    def __init__(self, name: str, multiValAtt: str, systemmodel_A: set["systemmodel_B"] = None, systemmodel_A17: set["systemmodel_C"] = None):
        self.name = name
        self.multiValAtt = multiValAtt
        self.systemmodel_A = systemmodel_A if systemmodel_A is not None else set()
        self.systemmodel_A17 = systemmodel_A17 if systemmodel_A17 is not None else set()
        
    @property
    def multiValAtt(self) -> str:
        return self.__multiValAtt

    @multiValAtt.setter
    def multiValAtt(self, multiValAtt: str):
        self.__multiValAtt = multiValAtt

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def systemmodel_A17(self):
        return self.__systemmodel_A17

    @systemmodel_A17.setter
    def systemmodel_A17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_A__systemmodel_A17", None)
        self.__systemmodel_A17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemmodel_C"):
                    opp_val = getattr(item, "systemmodel_C", None)
                    
                    if opp_val == self:
                        setattr(item, "systemmodel_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemmodel_C"):
                    opp_val = getattr(item, "systemmodel_C", None)
                    
                    setattr(item, "systemmodel_C", self)
                    

    @property
    def systemmodel_A(self):
        return self.__systemmodel_A

    @systemmodel_A.setter
    def systemmodel_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_systemmodel_A__systemmodel_A", None)
        self.__systemmodel_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "systemmodel_B"):
                    opp_val = getattr(item, "systemmodel_B", None)
                    
                    if opp_val == self:
                        setattr(item, "systemmodel_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "systemmodel_B"):
                    opp_val = getattr(item, "systemmodel_B", None)
                    
                    setattr(item, "systemmodel_B", self)
                    

class Sum:

    pass
class systemmodel_Sum2(Sum):

    pass
class systemmodel_Sum1(Sum):

    pass
class Block:

    pass
class systemmodel_Test(Block):

    pass
class systemmodel_Sum(Block):

    pass
class systemmodel_SrcBlock(Block):

    pass
class systemmodel_UnitDelay(Block):

    pass
class SMElement:

    pass
class systemmodel_Block(SMElement):

    pass
class systemmodel_Signal(SMElement):

    pass
class systemmodel_Inport(SMElement):

    pass
class systemmodel_Root(SMElement):

    pass
class systemmodel_ModelElement(SMElement):

    pass
class systemmodel_SystemModel(SMElement):

    pass
class systemmodel_SMElement(ABC):

    pass
class systemmodel_Outport(SMElement):

    pass