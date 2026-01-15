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

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process3: "simplepdl_ProcessElement" = None, simplepdl_Process: set["simplepdl_ProcessElement"] = None):
        self.name = name
        self.simplepdl_Process3 = simplepdl_Process3
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
                    

    @property
    def simplepdl_Process3(self):
        return self.__simplepdl_Process3

    @simplepdl_Process3.setter
    def simplepdl_Process3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process3", None)
        self.__simplepdl_Process3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ProcessElement2"):
                opp_val = getattr(old_value, "simplepdl_ProcessElement2", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ProcessElement2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ProcessElement2"):
                opp_val = getattr(value, "simplepdl_ProcessElement2", None)
                setattr(value, "simplepdl_ProcessElement2", self)

class ProcessElement:

    pass
class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence6: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.WorkSequence = WorkSequence
        self.WorkSequence6 = WorkSequence6
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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
            if hasattr(old_value, "WorkDefinition9"):
                opp_val = getattr(old_value, "WorkDefinition9", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition9"):
                opp_val = getattr(value, "WorkDefinition9", None)
                setattr(value, "WorkDefinition9", self)

    @property
    def WorkSequence6(self):
        return self.__WorkSequence6

    @WorkSequence6.setter
    def WorkSequence6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence6", None)
        self.__WorkSequence6 = value
        
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
                if hasattr(item, "simplepdl_ProcessElement11"):
                    opp_val = getattr(item, "simplepdl_ProcessElement11", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement11"):
                    opp_val = getattr(item, "simplepdl_ProcessElement11", None)
                    
                    setattr(item, "simplepdl_ProcessElement11", self)
                    

class simplepdl_WorkDefinition(ProcessElement):

    def __init__(self, name: str, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition9: "simplepdl_WorkSequence" = None):
        self.name = name
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition9 = WorkDefinition9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    setattr(item, "WorkSequence6", self)
                    

    @property
    def WorkDefinition9(self):
        return self.__WorkDefinition9

    @WorkDefinition9.setter
    def WorkDefinition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition9", None)
        self.__WorkDefinition9 = value
        
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
