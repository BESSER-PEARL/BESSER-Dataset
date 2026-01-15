from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"
class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishTofinish = "finishTofinish"


############################################
# Definition of Classes
############################################

class WorkDefinition:

    pass
class simplePDL_Activity(WorkDefinition):

    pass
class simplePDL_SubProcess(WorkDefinition):

    pass
class simplePDL_WorkProduct:

    def __init__(self, name: str, simplePDL_WorkProduct: "simplePDL_WorkDefinitionParameter" = None):
        self.name = name
        self.simplePDL_WorkProduct = simplePDL_WorkProduct
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplePDL_WorkProduct(self):
        return self.__simplePDL_WorkProduct

    @simplePDL_WorkProduct.setter
    def simplePDL_WorkProduct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkProduct__simplePDL_WorkProduct", None)
        self.__simplePDL_WorkProduct = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplePDL_WorkDefinitionParameter12"):
                opp_val = getattr(old_value, "simplePDL_WorkDefinitionParameter12", None)
                if opp_val == self:
                    setattr(old_value, "simplePDL_WorkDefinitionParameter12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplePDL_WorkDefinitionParameter12"):
                opp_val = getattr(value, "simplePDL_WorkDefinitionParameter12", None)
                setattr(value, "simplePDL_WorkDefinitionParameter12", self)

class simplePDL_WorkDefinitionParameter:

    def __init__(self, parameterKind: str, simplePDL_WorkDefinitionParameter: "simplePDL_WorkDefinition" = None, simplePDL_WorkDefinitionParameter12: "simplePDL_WorkProduct" = None):
        self.parameterKind = parameterKind
        self.simplePDL_WorkDefinitionParameter = simplePDL_WorkDefinitionParameter
        self.simplePDL_WorkDefinitionParameter12 = simplePDL_WorkDefinitionParameter12
        
    @property
    def parameterKind(self) -> str:
        return self.__parameterKind

    @parameterKind.setter
    def parameterKind(self, parameterKind: str):
        self.__parameterKind = parameterKind

    @property
    def simplePDL_WorkDefinitionParameter(self):
        return self.__simplePDL_WorkDefinitionParameter

    @simplePDL_WorkDefinitionParameter.setter
    def simplePDL_WorkDefinitionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinitionParameter__simplePDL_WorkDefinitionParameter", None)
        self.__simplePDL_WorkDefinitionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplePDL_WorkDefinition7"):
                opp_val = getattr(old_value, "simplePDL_WorkDefinition7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplePDL_WorkDefinition7"):
                opp_val = getattr(value, "simplePDL_WorkDefinition7", None)
                if opp_val is None:
                    setattr(value, "simplePDL_WorkDefinition7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplePDL_WorkDefinitionParameter12(self):
        return self.__simplePDL_WorkDefinitionParameter12

    @simplePDL_WorkDefinitionParameter12.setter
    def simplePDL_WorkDefinitionParameter12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinitionParameter__simplePDL_WorkDefinitionParameter12", None)
        self.__simplePDL_WorkDefinitionParameter12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplePDL_WorkProduct"):
                opp_val = getattr(old_value, "simplePDL_WorkProduct", None)
                if opp_val == self:
                    setattr(old_value, "simplePDL_WorkProduct", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplePDL_WorkProduct"):
                opp_val = getattr(value, "simplePDL_WorkProduct", None)
                setattr(value, "simplePDL_WorkProduct", self)

class simplePDL_WorkSequence:

    def __init__(self, linkType: str, simplePDL_WorkSequence: "simplePDL_Process" = None, WorkSequence: "simplePDL_WorkDefinition" = None, WorkSequence5: "simplePDL_WorkDefinition" = None, predecessor: set["simplePDL_WorkDefinition"] = None, successor: set["simplePDL_WorkDefinition"] = None):
        self.linkType = linkType
        self.simplePDL_WorkSequence = simplePDL_WorkSequence
        self.WorkSequence = WorkSequence
        self.WorkSequence5 = WorkSequence5
        self.predecessor = predecessor if predecessor is not None else set()
        self.successor = successor if successor is not None else set()
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def WorkSequence5(self):
        return self.__WorkSequence5

    @WorkSequence5.setter
    def WorkSequence5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkSequence__WorkSequence5", None)
        self.__WorkSequence5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToPredecessors"):
                opp_val = getattr(old_value, "linksToPredecessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToPredecessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToPredecessors"):
                opp_val = getattr(value, "linksToPredecessors", None)
                setattr(value, "linksToPredecessors", self)

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkSequence__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkDefinition"):
                    opp_val = getattr(item, "WorkDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkDefinition"):
                    opp_val = getattr(item, "WorkDefinition", None)
                    
                    setattr(item, "WorkDefinition", self)
                    

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToSuccessors"):
                opp_val = getattr(old_value, "linksToSuccessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToSuccessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToSuccessors"):
                opp_val = getattr(value, "linksToSuccessors", None)
                setattr(value, "linksToSuccessors", self)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkSequence__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkDefinition10"):
                    opp_val = getattr(item, "WorkDefinition10", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkDefinition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkDefinition10"):
                    opp_val = getattr(item, "WorkDefinition10", None)
                    
                    setattr(item, "WorkDefinition10", self)
                    

    @property
    def simplePDL_WorkSequence(self):
        return self.__simplePDL_WorkSequence

    @simplePDL_WorkSequence.setter
    def simplePDL_WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkSequence__simplePDL_WorkSequence", None)
        self.__simplePDL_WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplePDL_Process2"):
                opp_val = getattr(old_value, "simplePDL_Process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplePDL_Process2"):
                opp_val = getattr(value, "simplePDL_Process2", None)
                if opp_val is None:
                    setattr(value, "simplePDL_Process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplePDL_WorkDefinition(ABC):

    def __init__(self, name: str, simplePDL_WorkDefinition: "simplePDL_Process" = None, linksToSuccessors: "simplePDL_WorkSequence" = None, linksToPredecessors: "simplePDL_WorkSequence" = None, WorkDefinition: "simplePDL_WorkSequence" = None, WorkDefinition10: "simplePDL_WorkSequence" = None, simplePDL_WorkDefinition7: set["simplePDL_WorkDefinitionParameter"] = None):
        self.name = name
        self.simplePDL_WorkDefinition = simplePDL_WorkDefinition
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition10 = WorkDefinition10
        self.simplePDL_WorkDefinition7 = simplePDL_WorkDefinition7 if simplePDL_WorkDefinition7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplePDL_WorkDefinition7(self):
        return self.__simplePDL_WorkDefinition7

    @simplePDL_WorkDefinition7.setter
    def simplePDL_WorkDefinition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__simplePDL_WorkDefinition7", None)
        self.__simplePDL_WorkDefinition7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplePDL_WorkDefinitionParameter"):
                    opp_val = getattr(item, "simplePDL_WorkDefinitionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "simplePDL_WorkDefinitionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplePDL_WorkDefinitionParameter"):
                    opp_val = getattr(item, "simplePDL_WorkDefinitionParameter", None)
                    
                    setattr(item, "simplePDL_WorkDefinitionParameter", self)
                    

    @property
    def WorkDefinition10(self):
        return self.__WorkDefinition10

    @WorkDefinition10.setter
    def WorkDefinition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__WorkDefinition10", None)
        self.__WorkDefinition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkSequence5"):
                opp_val = getattr(old_value, "WorkSequence5", None)
                if opp_val == self:
                    setattr(old_value, "WorkSequence5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkSequence5"):
                opp_val = getattr(value, "WorkSequence5", None)
                setattr(value, "WorkSequence5", self)

    @property
    def simplePDL_WorkDefinition(self):
        return self.__simplePDL_WorkDefinition

    @simplePDL_WorkDefinition.setter
    def simplePDL_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__simplePDL_WorkDefinition", None)
        self.__simplePDL_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplePDL_Process"):
                opp_val = getattr(old_value, "simplePDL_Process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplePDL_Process"):
                opp_val = getattr(value, "simplePDL_Process", None)
                if opp_val is None:
                    setattr(value, "simplePDL_Process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__WorkDefinition", None)
        self.__WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToSuccessors(self):
        return self.__linksToSuccessors

    @linksToSuccessors.setter
    def linksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_WorkDefinition__linksToSuccessors", None)
        self.__linksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkSequence"):
                opp_val = getattr(old_value, "WorkSequence", None)
                if opp_val == self:
                    setattr(old_value, "WorkSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkSequence"):
                opp_val = getattr(value, "WorkSequence", None)
                setattr(value, "WorkSequence", self)

class simplePDL_Process:

    def __init__(self, name: str, simplePDL_Process: set["simplePDL_WorkDefinition"] = None, simplePDL_Process2: set["simplePDL_WorkSequence"] = None):
        self.name = name
        self.simplePDL_Process = simplePDL_Process if simplePDL_Process is not None else set()
        self.simplePDL_Process2 = simplePDL_Process2 if simplePDL_Process2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplePDL_Process(self):
        return self.__simplePDL_Process

    @simplePDL_Process.setter
    def simplePDL_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_Process__simplePDL_Process", None)
        self.__simplePDL_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplePDL_WorkDefinition"):
                    opp_val = getattr(item, "simplePDL_WorkDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "simplePDL_WorkDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplePDL_WorkDefinition"):
                    opp_val = getattr(item, "simplePDL_WorkDefinition", None)
                    
                    setattr(item, "simplePDL_WorkDefinition", self)
                    

    @property
    def simplePDL_Process2(self):
        return self.__simplePDL_Process2

    @simplePDL_Process2.setter
    def simplePDL_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplePDL_Process__simplePDL_Process2", None)
        self.__simplePDL_Process2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplePDL_WorkSequence"):
                    opp_val = getattr(item, "simplePDL_WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "simplePDL_WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplePDL_WorkSequence"):
                    opp_val = getattr(item, "simplePDL_WorkSequence", None)
                    
                    setattr(item, "simplePDL_WorkSequence", self)
                    
