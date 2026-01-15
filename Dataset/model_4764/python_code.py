from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionDomain(Enum):
    time = "time"
    space = "space"
    form = "form"


############################################
# Definition of Classes
############################################

class In:

    pass
class DataFlowEdge:

    pass
class effbd2_DataFlowInputEdge(DataFlowEdge):

    pass
class effbd2_DataFlowOutputEdge(DataFlowEdge):

    pass
class effbd2_FunctionDefinition:

    def __init__(self, transformationDefinition: str, effbd2_FunctionDefinition: "effbd2_FunctionSpecification" = None):
        self.transformationDefinition = transformationDefinition
        self.effbd2_FunctionDefinition = effbd2_FunctionDefinition
        
    @property
    def transformationDefinition(self) -> str:
        return self.__transformationDefinition

    @transformationDefinition.setter
    def transformationDefinition(self, transformationDefinition: str):
        self.__transformationDefinition = transformationDefinition

    @property
    def effbd2_FunctionDefinition(self):
        return self.__effbd2_FunctionDefinition

    @effbd2_FunctionDefinition.setter
    def effbd2_FunctionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionDefinition__effbd2_FunctionDefinition", None)
        self.__effbd2_FunctionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd2_FunctionSpecification16"):
                opp_val = getattr(old_value, "effbd2_FunctionSpecification16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd2_FunctionSpecification16"):
                opp_val = getattr(value, "effbd2_FunctionSpecification16", None)
                if opp_val is None:
                    setattr(value, "effbd2_FunctionSpecification16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd2_Resource(In):

    pass
class effbd2_Control(In):

    pass
class effbd2_Input(In):

    pass
class effbd2_DataPort(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class DataPort:

    pass
class effbd2_Out(DataPort):

    pass
class effbd2_In(DataPort):

    pass
class Transformed:

    pass
class effbd2_TriggerItem(Transformed):

    pass
class effbd2_ContinuousFlowItem(Transformed):

    pass
class effbd2_ItemContent:

    def __init__(self, id: str, effbd2_ItemContent: "effbd2_Transformed" = None):
        self.id = id
        self.effbd2_ItemContent = effbd2_ItemContent
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def effbd2_ItemContent(self):
        return self.__effbd2_ItemContent

    @effbd2_ItemContent.setter
    def effbd2_ItemContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_ItemContent__effbd2_ItemContent", None)
        self.__effbd2_ItemContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd2_Transformed"):
                opp_val = getattr(old_value, "effbd2_Transformed", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd2_Transformed"):
                opp_val = getattr(value, "effbd2_Transformed", None)
                if opp_val is None:
                    setattr(value, "effbd2_Transformed", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EffbdNode:

    pass
class effbd2_Transformer(EffbdNode):

    pass
class effbd2_Transformed(EffbdNode):

    pass
class SequenceNode:

    pass
class effbd2_IterationEnd(SequenceNode):

    pass
class effbd2_Final(SequenceNode):

    pass
class effbd2_LoopExit(SequenceNode):

    pass
class effbd2_LoopStart(SequenceNode):

    pass
class effbd2_Start(SequenceNode):

    pass
class effbd2_Decision(SequenceNode):

    pass
class effbd2_LoopEnd(SequenceNode):

    pass
class effbd2_Merge(SequenceNode):

    pass
class effbd2_Join(SequenceNode):

    pass
class effbd2_IterationStart(SequenceNode):

    pass
class effbd2_Fork(SequenceNode):

    pass
class effbd2_EffbdElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Transformer:

    pass
class effbd2_FunctionSpecification(Transformer):

    def __init__(self, domain: str, minDuration: int, maxDuration: int, effbd2_FunctionSpecification: set["effbd2_Input"] = None, effbd2_FunctionSpecification10: set["effbd2_Control"] = None, effbd2_FunctionSpecification12: set["effbd2_Resource"] = None, effbd2_FunctionSpecification14: "effbd2_Out" = None, effbd2_FunctionSpecification16: set["effbd2_FunctionDefinition"] = None):
        self.domain = domain
        self.minDuration = minDuration
        self.maxDuration = maxDuration
        self.effbd2_FunctionSpecification = effbd2_FunctionSpecification if effbd2_FunctionSpecification is not None else set()
        self.effbd2_FunctionSpecification10 = effbd2_FunctionSpecification10 if effbd2_FunctionSpecification10 is not None else set()
        self.effbd2_FunctionSpecification12 = effbd2_FunctionSpecification12 if effbd2_FunctionSpecification12 is not None else set()
        self.effbd2_FunctionSpecification14 = effbd2_FunctionSpecification14
        self.effbd2_FunctionSpecification16 = effbd2_FunctionSpecification16 if effbd2_FunctionSpecification16 is not None else set()
        
    @property
    def minDuration(self) -> int:
        return self.__minDuration

    @minDuration.setter
    def minDuration(self, minDuration: int):
        self.__minDuration = minDuration

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def maxDuration(self) -> int:
        return self.__maxDuration

    @maxDuration.setter
    def maxDuration(self, maxDuration: int):
        self.__maxDuration = maxDuration

    @property
    def effbd2_FunctionSpecification(self):
        return self.__effbd2_FunctionSpecification

    @effbd2_FunctionSpecification.setter
    def effbd2_FunctionSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionSpecification__effbd2_FunctionSpecification", None)
        self.__effbd2_FunctionSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd2_Input"):
                    opp_val = getattr(item, "effbd2_Input", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd2_Input", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd2_Input"):
                    opp_val = getattr(item, "effbd2_Input", None)
                    
                    setattr(item, "effbd2_Input", self)
                    

    @property
    def effbd2_FunctionSpecification14(self):
        return self.__effbd2_FunctionSpecification14

    @effbd2_FunctionSpecification14.setter
    def effbd2_FunctionSpecification14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionSpecification__effbd2_FunctionSpecification14", None)
        self.__effbd2_FunctionSpecification14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd2_Out"):
                opp_val = getattr(old_value, "effbd2_Out", None)
                if opp_val == self:
                    setattr(old_value, "effbd2_Out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd2_Out"):
                opp_val = getattr(value, "effbd2_Out", None)
                setattr(value, "effbd2_Out", self)

    @property
    def effbd2_FunctionSpecification16(self):
        return self.__effbd2_FunctionSpecification16

    @effbd2_FunctionSpecification16.setter
    def effbd2_FunctionSpecification16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionSpecification__effbd2_FunctionSpecification16", None)
        self.__effbd2_FunctionSpecification16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd2_FunctionDefinition"):
                    opp_val = getattr(item, "effbd2_FunctionDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd2_FunctionDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd2_FunctionDefinition"):
                    opp_val = getattr(item, "effbd2_FunctionDefinition", None)
                    
                    setattr(item, "effbd2_FunctionDefinition", self)
                    

    @property
    def effbd2_FunctionSpecification10(self):
        return self.__effbd2_FunctionSpecification10

    @effbd2_FunctionSpecification10.setter
    def effbd2_FunctionSpecification10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionSpecification__effbd2_FunctionSpecification10", None)
        self.__effbd2_FunctionSpecification10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd2_Control"):
                    opp_val = getattr(item, "effbd2_Control", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd2_Control", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd2_Control"):
                    opp_val = getattr(item, "effbd2_Control", None)
                    
                    setattr(item, "effbd2_Control", self)
                    

    @property
    def effbd2_FunctionSpecification12(self):
        return self.__effbd2_FunctionSpecification12

    @effbd2_FunctionSpecification12.setter
    def effbd2_FunctionSpecification12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd2_FunctionSpecification__effbd2_FunctionSpecification12", None)
        self.__effbd2_FunctionSpecification12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd2_Resource"):
                    opp_val = getattr(item, "effbd2_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd2_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd2_Resource"):
                    opp_val = getattr(item, "effbd2_Resource", None)
                    
                    setattr(item, "effbd2_Resource", self)
                    

class effbd2_SequenceNode(Transformer):

    pass
class EffbdElement:

    pass
class effbd2_ControlFlowEdge(EffbdElement):

    pass
class effbd2_EffbdNode(EffbdElement):

    pass
class effbd2_DataFlowEdge(EffbdElement):

    pass
class FunctionSpecification:

    pass
class effbd2_Function(FunctionSpecification):

    pass