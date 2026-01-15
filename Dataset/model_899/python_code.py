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
class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"
class TimeState(Enum):
    tooEarly = "tooEarly"
    inTime = "inTime"
    tooLate = "tooLate"


############################################
# Definition of Classes
############################################

class SimplePDLSemantics_TM3SimplePDL_SPDLSimEvent:

    def __init__(self, internal: bool, date: int, name: str):
        self.internal = internal
        self.date = date
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self) -> int:
        return self.__date

    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def internal(self) -> bool:
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
class SimplePDLSemantics_TM3SimplePDL_SPDLScenario:

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
class SimplePDLSemantics_SDMMSimplePDL_DynamicWorkDefinition(WorkDefinition):

    def __init__(self, time: str, timeElapsed: float, state: str, DDMMSimplePDL2: "SimplePDLSemantics_DDMMSimplePDL_Process", DDMMSimplePDL12: "SimplePDLSemantics_DDMMSimplePDL_WorkSequence", DDMMSimplePDL15: "SimplePDLSemantics_DDMMSimplePDL_WorkSequence", WorkDefinition22: "SimplePDLSemantics_EDMMSimplePDL_WorkDefinitionEvent"):
        self.time = time
        self.timeElapsed = timeElapsed
        self.state = state
        
    @property
    def timeElapsed(self) -> float:
        return self.__timeElapsed

    @timeElapsed.setter
    def timeElapsed(self, timeElapsed: float):
        self.__timeElapsed = timeElapsed

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class ProcessElement:

    pass
class SimplePDLSemantics_DDMMSimplePDL_WorkDefinition(ProcessElement):

    def __init__(self, name: str, WorkSequence: set["WorkSequence"] = None, WorkSequence6: set["WorkSequence"] = None, Process: "Process" = None, ProcessElement20: "SimplePDLSemantics_DDMMSimplePDL_Guidance", DDMMSimplePDL: "SimplePDLSemantics_DDMMSimplePDL_Process"):
        self.name = name
        self.WorkSequence = WorkSequence if WorkSequence is not None else set()
        self.WorkSequence6 = WorkSequence6 if WorkSequence6 is not None else set()
        self.Process = Process
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WorkSequence6(self):
        return self.__WorkSequence6

    @WorkSequence6.setter
    def WorkSequence6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__WorkSequence6", None)
        self.__WorkSequence6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMSimplePDL7"):
                    opp_val = getattr(item, "DDMMSimplePDL7", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMSimplePDL7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMSimplePDL7"):
                    opp_val = getattr(item, "DDMMSimplePDL7", None)
                    
                    setattr(item, "DDMMSimplePDL7", self)
                    

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__WorkSequence", None)
        self.__WorkSequence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMSimplePDL4"):
                    opp_val = getattr(item, "DDMMSimplePDL4", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMSimplePDL4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMSimplePDL4"):
                    opp_val = getattr(item, "DDMMSimplePDL4", None)
                    
                    setattr(item, "DDMMSimplePDL4", self)
                    

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkDefinition__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMSimplePDL9"):
                opp_val = getattr(old_value, "DDMMSimplePDL9", None)
                if opp_val == self:
                    setattr(old_value, "DDMMSimplePDL9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMSimplePDL9"):
                opp_val = getattr(value, "DDMMSimplePDL9", None)
                setattr(value, "DDMMSimplePDL9", self)

class SimplePDLSemantics_DDMMSimplePDL_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, WorkDefinition11: "WorkDefinition" = None, WorkDefinition14: "WorkDefinition" = None, ProcessElement20: "SimplePDLSemantics_DDMMSimplePDL_Guidance", DDMMSimplePDL: "SimplePDLSemantics_DDMMSimplePDL_Process"):
        self.linkType = linkType
        self.WorkDefinition11 = WorkDefinition11
        self.WorkDefinition14 = WorkDefinition14
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def WorkDefinition14(self):
        return self.__WorkDefinition14

    @WorkDefinition14.setter
    def WorkDefinition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkSequence__WorkDefinition14", None)
        self.__WorkDefinition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMSimplePDL15"):
                opp_val = getattr(old_value, "DDMMSimplePDL15", None)
                if opp_val == self:
                    setattr(old_value, "DDMMSimplePDL15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMSimplePDL15"):
                opp_val = getattr(value, "DDMMSimplePDL15", None)
                setattr(value, "DDMMSimplePDL15", self)

    @property
    def WorkDefinition11(self):
        return self.__WorkDefinition11

    @WorkDefinition11.setter
    def WorkDefinition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_WorkSequence__WorkDefinition11", None)
        self.__WorkDefinition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMSimplePDL12"):
                opp_val = getattr(old_value, "DDMMSimplePDL12", None)
                if opp_val == self:
                    setattr(old_value, "DDMMSimplePDL12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMSimplePDL12"):
                opp_val = getattr(value, "DDMMSimplePDL12", None)
                setattr(value, "DDMMSimplePDL12", self)

class SimplePDLSemantics_DDMMSimplePDL_Guidance(ProcessElement):

    def __init__(self, text: str, SimplePDLSemantics_DDMMSimplePDL_Guidance: set["ProcessElement"] = None, ProcessElement20: "SimplePDLSemantics_DDMMSimplePDL_Guidance", DDMMSimplePDL: "SimplePDLSemantics_DDMMSimplePDL_Process"):
        self.text = text
        self.SimplePDLSemantics_DDMMSimplePDL_Guidance = SimplePDLSemantics_DDMMSimplePDL_Guidance if SimplePDLSemantics_DDMMSimplePDL_Guidance is not None else set()
        
    @property
    def text(self) -> str:
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
                if hasattr(item, "ProcessElement20"):
                    opp_val = getattr(item, "ProcessElement20", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcessElement20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcessElement20"):
                    opp_val = getattr(item, "ProcessElement20", None)
                    
                    setattr(item, "ProcessElement20", self)
                    

class SimplePDLSemantics_DDMMSimplePDL_Process:

    def __init__(self, name: str, WorkDefinition: "WorkDefinition" = None, ProcessElement: set["ProcessElement"] = None):
        self.name = name
        self.WorkDefinition = WorkDefinition
        self.ProcessElement = ProcessElement if ProcessElement is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_Process__WorkDefinition", None)
        self.__WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMSimplePDL2"):
                opp_val = getattr(old_value, "DDMMSimplePDL2", None)
                if opp_val == self:
                    setattr(old_value, "DDMMSimplePDL2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMSimplePDL2"):
                opp_val = getattr(value, "DDMMSimplePDL2", None)
                setattr(value, "DDMMSimplePDL2", self)

    @property
    def ProcessElement(self):
        return self.__ProcessElement

    @ProcessElement.setter
    def ProcessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplePDLSemantics_DDMMSimplePDL_Process__ProcessElement", None)
        self.__ProcessElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMSimplePDL"):
                    opp_val = getattr(item, "DDMMSimplePDL", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMSimplePDL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMSimplePDL"):
                    opp_val = getattr(item, "DDMMSimplePDL", None)
                    
                    setattr(item, "DDMMSimplePDL", self)
                    
