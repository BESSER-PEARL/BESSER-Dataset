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

class Parameter:

    pass
class simplepdl_ParameterSWD(Parameter):

    pass
class ProcessElement:

    pass
class simplepdl_Parameter(ProcessElement):

    def __init__(self, name: str, nbNeeds: int, simplepdl_Parameter: "simplepdl_ParameterSWD" = None):
        self.name = name
        self.nbNeeds = nbNeeds
        self.simplepdl_Parameter = simplepdl_Parameter
        
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
    def simplepdl_Parameter(self):
        return self.__simplepdl_Parameter

    @simplepdl_Parameter.setter
    def simplepdl_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Parameter__simplepdl_Parameter", None)
        self.__simplepdl_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ParameterSWD20"):
                opp_val = getattr(old_value, "simplepdl_ParameterSWD20", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ParameterSWD20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ParameterSWD20"):
                opp_val = getattr(value, "simplepdl_ParameterSWD20", None)
                setattr(value, "simplepdl_ParameterSWD20", self)

class simplepdl_Activities(ProcessElement):

    def __init__(self, name: str, min_time: int, max_time: int, Activities7: "simplepdl_WorkSequence" = None, successor: set["simplepdl_WorkSequence"] = None, predecessor: set["simplepdl_WorkSequence"] = None, parent: set["simplepdl_SubWorkDefinition"] = None, Activities: "simplepdl_WorkSequence" = None, Activities14: "simplepdl_SubWorkDefinition" = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.Activities7 = Activities7
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.parent = parent if parent is not None else set()
        self.Activities = Activities
        self.Activities14 = Activities14
        
    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Activities__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SubWorkDefinition"):
                    opp_val = getattr(item, "SubWorkDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "SubWorkDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SubWorkDefinition"):
                    opp_val = getattr(item, "SubWorkDefinition", None)
                    
                    setattr(item, "SubWorkDefinition", self)
                    

    @property
    def Activities14(self):
        return self.__Activities14

    @Activities14.setter
    def Activities14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Activities__Activities14", None)
        self.__Activities14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def Activities(self):
        return self.__Activities

    @Activities.setter
    def Activities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Activities__Activities", None)
        self.__Activities = value
        
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
        old_value = getattr(self, f"_simplepdl_Activities__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence10"):
                    opp_val = getattr(item, "WorkSequence10", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence10"):
                    opp_val = getattr(item, "WorkSequence10", None)
                    
                    setattr(item, "WorkSequence10", self)
                    

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Activities__successor", None)
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
    def Activities7(self):
        return self.__Activities7

    @Activities7.setter
    def Activities7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Activities__Activities7", None)
        self.__Activities7 = value
        
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

class simplepdl_WorkSequence(ProcessElement):

    def __init__(self, name: str, linkType: str, linksToPredecessors: "simplepdl_Activities" = None, WorkSequence: "simplepdl_Activities" = None, WorkSequence10: "simplepdl_Activities" = None, linksToSuccessors: "simplepdl_Activities" = None):
        self.name = name
        self.linkType = linkType
        self.linksToPredecessors = linksToPredecessors
        self.WorkSequence = WorkSequence
        self.WorkSequence10 = WorkSequence10
        self.linksToSuccessors = linksToSuccessors
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WorkSequence10(self):
        return self.__WorkSequence10

    @WorkSequence10.setter
    def WorkSequence10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence10", None)
        self.__WorkSequence10 = value
        
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
            if hasattr(old_value, "Activities"):
                opp_val = getattr(old_value, "Activities", None)
                if opp_val == self:
                    setattr(old_value, "Activities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activities"):
                opp_val = getattr(value, "Activities", None)
                setattr(value, "Activities", self)

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
            if hasattr(old_value, "Activities7"):
                opp_val = getattr(old_value, "Activities7", None)
                if opp_val == self:
                    setattr(old_value, "Activities7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activities7"):
                opp_val = getattr(value, "Activities7", None)
                setattr(value, "Activities7", self)

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
                if hasattr(item, "simplepdl_ProcessElement4"):
                    opp_val = getattr(item, "simplepdl_ProcessElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_ProcessElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_ProcessElement4"):
                    opp_val = getattr(item, "simplepdl_ProcessElement4", None)
                    
                    setattr(item, "simplepdl_ProcessElement4", self)
                    

class simplepdl_Resource:

    def __init__(self, name: str, marking: int, simplepdl_Resource: "simplepdl_Process" = None, simplepdl_Resource17: "simplepdl_ParameterWD" = None):
        self.name = name
        self.marking = marking
        self.simplepdl_Resource = simplepdl_Resource
        self.simplepdl_Resource17 = simplepdl_Resource17
        
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
    def simplepdl_Resource17(self):
        return self.__simplepdl_Resource17

    @simplepdl_Resource17.setter
    def simplepdl_Resource17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Resource__simplepdl_Resource17", None)
        self.__simplepdl_Resource17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_ParameterWD"):
                opp_val = getattr(old_value, "simplepdl_ParameterWD", None)
                if opp_val == self:
                    setattr(old_value, "simplepdl_ParameterWD", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_ParameterWD"):
                opp_val = getattr(value, "simplepdl_ParameterWD", None)
                setattr(value, "simplepdl_ParameterWD", self)

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

class simplepdl_ProcessElement(ABC):

    pass
class simplepdl_ParameterWD(Parameter):

    pass
class Activities:

    pass
class simplepdl_WorkDefinition(Activities):

    pass
class simplepdl_SubWorkDefinition(Activities):

    pass
class simplepdl_Process:

    def __init__(self, name: str, min_time: int, max_time: int, simplepdl_Process: set["simplepdl_ProcessElement"] = None, simplepdl_Process2: set["simplepdl_Resource"] = None):
        self.name = name
        self.min_time = min_time
        self.max_time = max_time
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        self.simplepdl_Process2 = simplepdl_Process2 if simplepdl_Process2 is not None else set()
        
    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

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
                    
