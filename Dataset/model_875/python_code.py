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
class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, name: str, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence5: "simplepdl_WorkDefinition" = None, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.name = name
        self.WorkSequence = WorkSequence
        self.WorkSequence5 = WorkSequence5
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

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
    def WorkSequence5(self):
        return self.__WorkSequence5

    @WorkSequence5.setter
    def WorkSequence5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence5", None)
        self.__WorkSequence5 = value
        
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

class simplepdl_Parameter(ProcessElement):

    def __init__(self, nbNeeds: int, name: str, Parameter: "simplepdl_WorkDefinition" = None, simplepdl_Parameter: "simplepdl_Resource" = None, needs: "simplepdl_WorkDefinition" = None):
        self.nbNeeds = nbNeeds
        self.name = name
        self.Parameter = Parameter
        self.simplepdl_Parameter = simplepdl_Parameter
        self.needs = needs
        
    @property
    def nbNeeds(self) -> int:
        return self.__nbNeeds

    @nbNeeds.setter
    def nbNeeds(self, nbNeeds: int):
        self.__nbNeeds = nbNeeds

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Parameter__needs", None)
        self.__needs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition15"):
                opp_val = getattr(old_value, "WorkDefinition15", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition15"):
                opp_val = getattr(value, "WorkDefinition15", None)
                setattr(value, "WorkDefinition15", self)

    @property
    def simplepdl_Parameter(self):
        return self.__simplepdl_Parameter

    @simplepdl_Parameter.setter
    def simplepdl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Parameter__simplepdl_Parameter", None)
        self.__simplepdl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Resource13"):
                opp_val = getattr(old_value, "simplepdl_Resource13", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Resource13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Resource13"):
                opp_val = getattr(value, "simplepdl_Resource13", None)
                setattr(value, "simplepdl_Resource13", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workDefinition"):
                opp_val = getattr(old_value, "workDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workDefinition"):
                opp_val = getattr(value, "workDefinition", None)
                if opp_val is None:
                    setattr(value, "workDefinition", set([self]))
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

    def __init__(self, min_time: int, max_time: int, name: str, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, workDefinition: set["simplepdl_Parameter"] = None, WorkDefinition15: "simplepdl_Parameter" = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition9: "simplepdl_WorkSequence" = None):
        self.min_time = min_time
        self.max_time = max_time
        self.name = name
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.workDefinition = workDefinition if workDefinition is not None else set()
        self.WorkDefinition15 = WorkDefinition15
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition9 = WorkDefinition9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

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
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    setattr(item, "WorkSequence5", self)
                    

    @property
    def WorkDefinition15(self):
        return self.__WorkDefinition15

    @WorkDefinition15.setter
    def WorkDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition15", None)
        self.__WorkDefinition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "needs"):
                opp_val = getattr(old_value, "needs", None)
                if opp_val == self:
                    setattr(old_value, "needs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "needs"):
                opp_val = getattr(value, "needs", None)
                setattr(value, "needs", self)

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
    def workDefinition(self):
        return self.__workDefinition

    @workDefinition.setter
    def workDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__workDefinition", None)
        self.__workDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

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
                    

class simplepdl_Resource:

    def __init__(self, name: str, marking: int, simplepdl_Resource: "simplepdl_Process" = None, simplepdl_Resource13: "simplepdl_Parameter" = None):
        self.name = name
        self.marking = marking
        self.simplepdl_Resource = simplepdl_Resource
        self.simplepdl_Resource13 = simplepdl_Resource13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

    @property
    def simplepdl_Resource(self):
        return self.__simplepdl_Resource

    @simplepdl_Resource.setter
    def simplepdl_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Resource__simplepdl_Resource", None)
        self.__simplepdl_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Process2"):
                opp_val = getattr(old_value, "simplepdl_Process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Process2"):
                opp_val = getattr(value, "simplepdl_Process2", None)
                if opp_val is None:
                    setattr(value, "simplepdl_Process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplepdl_Resource13(self):
        return self.__simplepdl_Resource13

    @simplepdl_Resource13.setter
    def simplepdl_Resource13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Resource__simplepdl_Resource13", None)
        self.__simplepdl_Resource13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Parameter"):
                opp_val = getattr(old_value, "simplepdl_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Parameter"):
                opp_val = getattr(value, "simplepdl_Parameter", None)
                setattr(value, "simplepdl_Parameter", self)

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_Process:

    def __init__(self, name: str, min_time: int, max_time: int, simplepdl_Process: set["simplepdl_ProcessElement"] = None, simplepdl_Process2: set["simplepdl_Resource"] = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        self.simplepdl_Process2 = simplepdl_Process2 if simplepdl_Process2 is not None else set()
        
    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

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
    def simplepdl_Process2(self):
        return self.__simplepdl_Process2

    @simplepdl_Process2.setter
    def simplepdl_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process2", None)
        self.__simplepdl_Process2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_Resource"):
                    opp_val = getattr(item, "simplepdl_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_Resource"):
                    opp_val = getattr(item, "simplepdl_Resource", None)
                    
                    setattr(item, "simplepdl_Resource", self)
                    
