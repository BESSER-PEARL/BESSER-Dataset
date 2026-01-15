from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"


############################################
# Definition of Classes
############################################

class ProcessElement:

    pass
class simplepdl_Ressource(ProcessElement):

    def __init__(self, quantity: int, name: str, simplepdl_Ressource: "simplepdl_RessourceLink" = None):
        self.quantity = quantity
        self.name = name
        self.simplepdl_Ressource = simplepdl_Ressource
        
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Ressource(self):
        return self.__simplepdl_Ressource

    @simplepdl_Ressource.setter
    def simplepdl_Ressource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Ressource__simplepdl_Ressource", None)
        self.__simplepdl_Ressource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_RessourceLink11"):
                opp_val = getattr(old_value, "simplepdl_RessourceLink11", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceLink11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceLink11"):
                opp_val = getattr(value, "simplepdl_RessourceLink11", None)
                setattr(value, "simplepdl_RessourceLink11", self)

class simplepdl_Guidance(ProcessElement):

    def __init__(self, text: str, simplepdl_Guidance: set["simplepdl_ProcessElement"] = None):
        self.text = text
        self.simplepdl_Guidance = simplepdl_Guidance if simplepdl_Guidance is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def simplepdl_Guidance(self):
        return self.__simplepdl_Guidance

    @simplepdl_Guidance.setter
    def simplepdl_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Guidance__simplepdl_Guidance", None)
        self.__simplepdl_Guidance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_ProcessElement8"):
                    opp_val = getattr(item, "simplepdl_ProcessElement8", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement8"):
                    opp_val = getattr(item, "simplepdl_ProcessElement8", None)
                    
                    setattr(item, "simplepdl_ProcessElement8", self)
                    

class simplepdl_RessourceLink(ProcessElement):

    def __init__(self, weight: int, simplepdl_RessourceLink: "simplepdl_WorkDefinition" = None, simplepdl_RessourceLink11: "simplepdl_Ressource" = None):
        self.weight = weight
        self.simplepdl_RessourceLink = simplepdl_RessourceLink
        self.simplepdl_RessourceLink11 = simplepdl_RessourceLink11
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def simplepdl_RessourceLink11(self):
        return self.__simplepdl_RessourceLink11

    @simplepdl_RessourceLink11.setter
    def simplepdl_RessourceLink11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceLink__simplepdl_RessourceLink11", None)
        self.__simplepdl_RessourceLink11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Ressource"):
                opp_val = getattr(old_value, "simplepdl_Ressource", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Ressource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Ressource"):
                opp_val = getattr(value, "simplepdl_Ressource", None)
                setattr(value, "simplepdl_Ressource", self)

    @property
    def simplepdl_RessourceLink(self):
        return self.__simplepdl_RessourceLink

    @simplepdl_RessourceLink.setter
    def simplepdl_RessourceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_RessourceLink__simplepdl_RessourceLink", None)
        self.__simplepdl_RessourceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_WorkDefinition"):
                opp_val = getattr(old_value, "simplepdl_WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_WorkDefinition"):
                opp_val = getattr(value, "simplepdl_WorkDefinition", None)
                setattr(value, "simplepdl_WorkDefinition", self)

class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence3: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None, WorkSequence: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence3 = WorkSequence3
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        self.WorkSequence = WorkSequence
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def WorkSequence3(self):
        return self.__WorkSequence3

    @WorkSequence3.setter
    def WorkSequence3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence3", None)
        self.__WorkSequence3 = value
        
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
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition6"):
                opp_val = getattr(old_value, "WorkDefinition6", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition6"):
                opp_val = getattr(value, "WorkDefinition6", None)
                setattr(value, "WorkDefinition6", self)

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
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
    def linksToSuccessors(self):
        return self.__linksToSuccessors

    @linksToSuccessors.setter
    def linksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToSuccessors", None)
        self.__linksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition"):
                opp_val = getattr(old_value, "WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition"):
                opp_val = getattr(value, "WorkDefinition", None)
                setattr(value, "WorkDefinition", self)

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, min_time: int, max_time: int, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition6: "simplepdl_WorkSequence" = None, simplepdl_WorkDefinition: "simplepdl_RessourceLink" = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition6 = WorkDefinition6
        self.simplepdl_WorkDefinition = simplepdl_WorkDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition", None)
        self.__WorkDefinition = value
        
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
    def simplepdl_WorkDefinition(self):
        return self.__simplepdl_WorkDefinition

    @simplepdl_WorkDefinition.setter
    def simplepdl_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__simplepdl_WorkDefinition", None)
        self.__simplepdl_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_RessourceLink"):
                opp_val = getattr(old_value, "simplepdl_RessourceLink", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_RessourceLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_RessourceLink"):
                opp_val = getattr(value, "simplepdl_RessourceLink", None)
                setattr(value, "simplepdl_RessourceLink", self)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    setattr(item, "WorkSequence", self)
                    

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence3"):
                    opp_val = getattr(item, "WorkSequence3", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence3"):
                    opp_val = getattr(item, "WorkSequence3", None)
                    
                    setattr(item, "WorkSequence3", self)
                    

    @property
    def WorkDefinition6(self):
        return self.__WorkDefinition6

    @WorkDefinition6.setter
    def WorkDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition6", None)
        self.__WorkDefinition6 = value
        
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

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_ProcessElement"] = None):
        self.name = name
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Process(self):
        return self.__simplepdl_Process

    @simplepdl_Process.setter
    def simplepdl_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process", None)
        self.__simplepdl_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_ProcessElement"):
                    opp_val = getattr(item, "simplepdl_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement"):
                    opp_val = getattr(item, "simplepdl_ProcessElement", None)
                    
                    setattr(item, "simplepdl_ProcessElement", self)
                    
