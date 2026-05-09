from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ExecutionState(Enum):
    notStarted = "notStarted"
    running = "running"
    finished = "finished"
class TimeState(Enum):
    tooEarly = "tooEarly"
    inTime = "inTime"
    tooLate = "tooLate"
class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"


############################################
# Definition of Classes
############################################

class SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent:

    def __init__(self, internal: bool, date: int, name: str):
        self.internal = internal
        self.date = date
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: int):
        self.__date = date


    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal


class SPDLScenario:

    pass
class SimplePDLSemantics_TM3SimplePDL_SPDLTrace:

    pass
class SPDLTrace:

    pass
class WorkDefinitionEvent:

    pass
class SimplePDLSemantics_EDMMSimplePDL_FinishWD(WorkDefinitionEvent):

    pass
class SimplePDLSemantics_EDMMSimplePDL_StartWD(WorkDefinitionEvent):

    pass
class Event:

    pass
class SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent(Event):

    pass
class SPDLSimEvent:

    pass
class SimplePDLSemantics_EDMMSimplePDL_Event(SPDLSimEvent):

    pass
class SimplePDLSemantics_DDMMSimplePDL_ProcessElement(ABC):

    pass
class Process:

    pass
class WorkSequence:

    pass
class WorkDefinition:

    pass
class SimplePDLSemantics_TM3SimplePDL_SPDLScenario:

    pass
class ProcessElement:

    pass
class SimplePDLSemantics_DDMMSimplePDL_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, linksToSuccessors: "WorkDefinition" = None, linksToPredecessors: "WorkDefinition" = None, ProcessElement13: "SimplePDLSemantics_DDMMSimplePDL_Guidance" = None, ProcessElement: "SimplePDLSemantics_DDMMSimplePDL_Process" = None):
        self.linkType = linkType
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        
        pass
    @property
    def linkType(self):
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
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkSequence__linksToPredecessors", None)
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
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkSequence__linksToSuccessors", None)
        self.__linksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition7"):
                opp_val = getattr(old_value, "WorkDefinition7", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition7"):
                opp_val = getattr(value, "WorkDefinition7", None)
                setattr(value, "WorkDefinition7", self)

class SimplePDLSemantics_DDMMSimplePDL_WorkDefinition(ProcessElement):

    def __init__(self, name: str, successor: set["WorkSequence"] = None, predecessor: set["WorkSequence"] = None, from_: "Process" = None, ProcessElement13: "SimplePDLSemantics_DDMMSimplePDL_Guidance" = None, ProcessElement: "SimplePDLSemantics_DDMMSimplePDL_Process" = None):
        self.name = name
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.from_ = from_
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__from_", None)
        self.__from_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process"):
                opp_val = getattr(old_value, "Process", None)
                if opp_val == self:
                    setattr(old_value, "Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process"):
                opp_val = getattr(value, "Process", None)
                setattr(value, "Process", self)

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    setattr(item, "WorkSequence4", self)
                    

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__successor", None)
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
                    

class SimplePDLSemantics_DDMMSimplePDL_Guidance(ProcessElement):

    def __init__(self, text: str, SimplePDLSemantics_DDMMSimplePDL_Guidance: set["ProcessElement"] = None, ProcessElement13: "SimplePDLSemantics_DDMMSimplePDL_Guidance" = None, ProcessElement: "SimplePDLSemantics_DDMMSimplePDL_Process" = None):
        self.text = text
        self.SimplePDLSemantics_DDMMSimplePDL_Guidance = SimplePDLSemantics_DDMMSimplePDL_Guidance if SimplePDLSemantics_DDMMSimplePDL_Guidance is not None else set()
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def SimplePDLSemantics_DDMMSimplePDL_Guidance(self):
        return self.__SimplePDLSemantics_DDMMSimplePDL_Guidance

    @SimplePDLSemantics_DDMMSimplePDL_Guidance.setter
    def SimplePDLSemantics_DDMMSimplePDL_Guidance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_Guidance__SimplePDLSemantics_DDMMSimplePDL_Guidance", None)
        self.__SimplePDLSemantics_DDMMSimplePDL_Guidance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcessElement13"):
                    opp_val = getattr(item, "ProcessElement13", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessElement13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessElement13"):
                    opp_val = getattr(item, "ProcessElement13", None)
                    
                    setattr(item, "ProcessElement13", self)
                    

class SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition(WorkDefinition):

    def __init__(self, state: str, time: str, timeElapsed: float, WorkDefinition: "SimplePDLSemantics_DDMMSimplePDL_Process" = None, WorkDefinition9: "SimplePDLSemantics_DDMMSimplePDL_WorkSequence" = None, WorkDefinition7: "SimplePDLSemantics_DDMMSimplePDL_WorkSequence" = None, WorkDefinition15: "SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent" = None):
        self.state = state
        self.time = time
        self.timeElapsed = timeElapsed
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def timeElapsed(self):
        return self.__timeElapsed

    @timeElapsed.setter
    def timeElapsed(self, timeElapsed: float):
        self.__timeElapsed = timeElapsed


class SimplePDLSemantics_DDMMSimplePDL_Process:

    def __init__(self, name: str, process: "WorkDefinition" = None, parent: set["ProcessElement"] = None):
        self.name = name
        self.process = process
        self.parent = parent if parent is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_Process__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcessElement"):
                    opp_val = getattr(item, "ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessElement"):
                    opp_val = getattr(item, "ProcessElement", None)
                    
                    setattr(item, "ProcessElement", self)
                    

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_Process__process", None)
        self.__process = value
        
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
