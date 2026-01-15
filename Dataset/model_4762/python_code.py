from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Sequence:

    pass
class ctrlflow101_And(Sequence):

    pass
class ctrlflow101_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, ctrlflow101_SequenceNode: "ctrlflow101_SequenceNode" = None, ctrlflow101_SequenceNode6: set["ctrlflow101_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.ctrlflow101_SequenceNode = ctrlflow101_SequenceNode
        self.ctrlflow101_SequenceNode6 = ctrlflow101_SequenceNode6 if ctrlflow101_SequenceNode6 is not None else set()
        
    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def ctrlflow101_SequenceNode6(self):
        return self.__ctrlflow101_SequenceNode6

    @ctrlflow101_SequenceNode6.setter
    def ctrlflow101_SequenceNode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctrlflow101_SequenceNode__ctrlflow101_SequenceNode6", None)
        self.__ctrlflow101_SequenceNode6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ctrlflow101_SequenceNode"):
                    opp_val = getattr(item, "ctrlflow101_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ctrlflow101_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ctrlflow101_SequenceNode"):
                    opp_val = getattr(item, "ctrlflow101_SequenceNode", None)
                    
                    setattr(item, "ctrlflow101_SequenceNode", self)
                    

    @property
    def ctrlflow101_SequenceNode(self):
        return self.__ctrlflow101_SequenceNode

    @ctrlflow101_SequenceNode.setter
    def ctrlflow101_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctrlflow101_SequenceNode__ctrlflow101_SequenceNode", None)
        self.__ctrlflow101_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctrlflow101_SequenceNode6"):
                opp_val = getattr(old_value, "ctrlflow101_SequenceNode6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctrlflow101_SequenceNode6"):
                opp_val = getattr(value, "ctrlflow101_SequenceNode6", None)
                if opp_val is None:
                    setattr(value, "ctrlflow101_SequenceNode6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ctrlflow101_Token:

    pass
class ctrlflow101_Loop(Sequence):

    pass
class ctrlflow101_Final(Sequence):

    pass
class ctrlflow101_Start(Sequence):

    pass
class ctrlflow101_Or(Sequence):

    pass
class SequenceNode:

    pass
class ctrlflow101_Sequence(SequenceNode):

    def __init__(self, weight: int, ctrlflow101_Sequence: "ctrlflow101_Function" = None):
        self.weight = weight
        self.ctrlflow101_Sequence = ctrlflow101_Sequence
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def ctrlflow101_Sequence(self):
        return self.__ctrlflow101_Sequence

    @ctrlflow101_Sequence.setter
    def ctrlflow101_Sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ctrlflow101_Sequence__ctrlflow101_Sequence", None)
        self.__ctrlflow101_Sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctrlflow101_Function3"):
                opp_val = getattr(old_value, "ctrlflow101_Function3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctrlflow101_Function3"):
                opp_val = getattr(value, "ctrlflow101_Function3", None)
                if opp_val is None:
                    setattr(value, "ctrlflow101_Function3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ctrlflow101_Function(SequenceNode):

    pass