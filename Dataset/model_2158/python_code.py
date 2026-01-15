from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class behavior_BehaviorMixEntry:

    def __init__(self, behaviorModelName: str, relativeFrequency: float, behavior_BehaviorMixEntry17: "behavior_BehaviorModelRelative" = None, behavior_BehaviorMixEntry: "behavior_BehaviorMix" = None):
        self.behaviorModelName = behaviorModelName
        self.relativeFrequency = relativeFrequency
        self.behavior_BehaviorMixEntry17 = behavior_BehaviorMixEntry17
        self.behavior_BehaviorMixEntry = behavior_BehaviorMixEntry
        
    @property
    def relativeFrequency(self) -> float:
        return self.__relativeFrequency

    @relativeFrequency.setter
    def relativeFrequency(self, relativeFrequency: float):
        self.__relativeFrequency = relativeFrequency

    @property
    def behaviorModelName(self) -> str:
        return self.__behaviorModelName

    @behaviorModelName.setter
    def behaviorModelName(self, behaviorModelName: str):
        self.__behaviorModelName = behaviorModelName

    @property
    def behavior_BehaviorMixEntry(self):
        return self.__behavior_BehaviorMixEntry

    @behavior_BehaviorMixEntry.setter
    def behavior_BehaviorMixEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_BehaviorMixEntry__behavior_BehaviorMixEntry", None)
        self.__behavior_BehaviorMixEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_BehaviorMix"):
                opp_val = getattr(old_value, "behavior_BehaviorMix", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_BehaviorMix"):
                opp_val = getattr(value, "behavior_BehaviorMix", None)
                if opp_val is None:
                    setattr(value, "behavior_BehaviorMix", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_BehaviorMixEntry17(self):
        return self.__behavior_BehaviorMixEntry17

    @behavior_BehaviorMixEntry17.setter
    def behavior_BehaviorMixEntry17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_BehaviorMixEntry__behavior_BehaviorMixEntry17", None)
        self.__behavior_BehaviorMixEntry17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_BehaviorModelRelative"):
                opp_val = getattr(old_value, "behavior_BehaviorModelRelative", None)
                if opp_val == self:
                    setattr(old_value, "behavior_BehaviorModelRelative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_BehaviorModelRelative"):
                opp_val = getattr(value, "behavior_BehaviorModelRelative", None)
                setattr(value, "behavior_BehaviorModelRelative", self)

class behavior_BehaviorMix:

    pass
class AbstractBehaviorModelGraph:

    pass
class behavior_BehaviorModelRelative(AbstractBehaviorModelGraph):

    pass
class behavior_BehaviorModelAbsolute(AbstractBehaviorModelGraph):

    pass
class behavior_Transition:

    def __init__(self, value: float, timeDiffs: str, thinkTimeParams: str, behavior_Transition: "behavior_Vertex" = None, behavior_Transition10: "behavior_Vertex" = None, behavior_Transition13: "behavior_Vertex" = None):
        self.value = value
        self.timeDiffs = timeDiffs
        self.thinkTimeParams = thinkTimeParams
        self.behavior_Transition = behavior_Transition
        self.behavior_Transition10 = behavior_Transition10
        self.behavior_Transition13 = behavior_Transition13
        
    @property
    def thinkTimeParams(self) -> str:
        return self.__thinkTimeParams

    @thinkTimeParams.setter
    def thinkTimeParams(self, thinkTimeParams: str):
        self.__thinkTimeParams = thinkTimeParams

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def timeDiffs(self) -> str:
        return self.__timeDiffs

    @timeDiffs.setter
    def timeDiffs(self, timeDiffs: str):
        self.__timeDiffs = timeDiffs

    @property
    def behavior_Transition13(self):
        return self.__behavior_Transition13

    @behavior_Transition13.setter
    def behavior_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Transition__behavior_Transition13", None)
        self.__behavior_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Vertex14"):
                opp_val = getattr(old_value, "behavior_Vertex14", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Vertex14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Vertex14"):
                opp_val = getattr(value, "behavior_Vertex14", None)
                setattr(value, "behavior_Vertex14", self)

    @property
    def behavior_Transition(self):
        return self.__behavior_Transition

    @behavior_Transition.setter
    def behavior_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Transition__behavior_Transition", None)
        self.__behavior_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Vertex8"):
                opp_val = getattr(old_value, "behavior_Vertex8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Vertex8"):
                opp_val = getattr(value, "behavior_Vertex8", None)
                if opp_val is None:
                    setattr(value, "behavior_Vertex8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Transition10(self):
        return self.__behavior_Transition10

    @behavior_Transition10.setter
    def behavior_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Transition__behavior_Transition10", None)
        self.__behavior_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Vertex11"):
                opp_val = getattr(old_value, "behavior_Vertex11", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Vertex11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Vertex11"):
                opp_val = getattr(value, "behavior_Vertex11", None)
                setattr(value, "behavior_Vertex11", self)

class behavior_UseCase:

    def __init__(self, name: str, id: str, behavior_UseCase: "behavior_UseCaseRepository" = None, behavior_UseCase5: "behavior_AbstractUseCaseExecution" = None):
        self.name = name
        self.id = id
        self.behavior_UseCase = behavior_UseCase
        self.behavior_UseCase5 = behavior_UseCase5
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def behavior_UseCase5(self):
        return self.__behavior_UseCase5

    @behavior_UseCase5.setter
    def behavior_UseCase5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_UseCase__behavior_UseCase5", None)
        self.__behavior_UseCase5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_AbstractUseCaseExecution"):
                opp_val = getattr(old_value, "behavior_AbstractUseCaseExecution", None)
                if opp_val == self:
                    setattr(old_value, "behavior_AbstractUseCaseExecution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_AbstractUseCaseExecution"):
                opp_val = getattr(value, "behavior_AbstractUseCaseExecution", None)
                setattr(value, "behavior_AbstractUseCaseExecution", self)

    @property
    def behavior_UseCase(self):
        return self.__behavior_UseCase

    @behavior_UseCase.setter
    def behavior_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_UseCase__behavior_UseCase", None)
        self.__behavior_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_UseCaseRepository"):
                opp_val = getattr(old_value, "behavior_UseCaseRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_UseCaseRepository"):
                opp_val = getattr(value, "behavior_UseCaseRepository", None)
                if opp_val is None:
                    setattr(value, "behavior_UseCaseRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class behavior_AbstractBehaviorModelGraph(ABC):

    def __init__(self, transactionType: str, behavior_AbstractBehaviorModelGraph: set["behavior_Vertex"] = None):
        self.transactionType = transactionType
        self.behavior_AbstractBehaviorModelGraph = behavior_AbstractBehaviorModelGraph if behavior_AbstractBehaviorModelGraph is not None else set()
        
    @property
    def transactionType(self) -> str:
        return self.__transactionType

    @transactionType.setter
    def transactionType(self, transactionType: str):
        self.__transactionType = transactionType

    @property
    def behavior_AbstractBehaviorModelGraph(self):
        return self.__behavior_AbstractBehaviorModelGraph

    @behavior_AbstractBehaviorModelGraph.setter
    def behavior_AbstractBehaviorModelGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_AbstractBehaviorModelGraph__behavior_AbstractBehaviorModelGraph", None)
        self.__behavior_AbstractBehaviorModelGraph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Vertex"):
                    opp_val = getattr(item, "behavior_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Vertex"):
                    opp_val = getattr(item, "behavior_Vertex", None)
                    
                    setattr(item, "behavior_Vertex", self)
                    

class behavior_AbstractUseCaseExecution(ABC):

    pass
class AbstractUseCaseExecution:

    pass
class behavior_Vertex(AbstractUseCaseExecution):

    pass
class behavior_ObservedUseCaseExecution(AbstractUseCaseExecution):

    def __init__(self, startTime: str, endTime: str, behavior_ObservedUseCaseExecution: "behavior_Session" = None):
        self.startTime = startTime
        self.endTime = endTime
        self.behavior_ObservedUseCaseExecution = behavior_ObservedUseCaseExecution
        
    @property
    def startTime(self) -> str:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def endTime(self) -> str:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def behavior_ObservedUseCaseExecution(self):
        return self.__behavior_ObservedUseCaseExecution

    @behavior_ObservedUseCaseExecution.setter
    def behavior_ObservedUseCaseExecution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_ObservedUseCaseExecution__behavior_ObservedUseCaseExecution", None)
        self.__behavior_ObservedUseCaseExecution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Session3"):
                opp_val = getattr(old_value, "behavior_Session3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Session3"):
                opp_val = getattr(value, "behavior_Session3", None)
                if opp_val is None:
                    setattr(value, "behavior_Session3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class behavior_Session:

    def __init__(self, id: str, startTime: str, endTime: str, transactionType: str, behavior_Session: "behavior_SessionRepository" = None, behavior_Session3: set["behavior_ObservedUseCaseExecution"] = None):
        self.id = id
        self.startTime = startTime
        self.endTime = endTime
        self.transactionType = transactionType
        self.behavior_Session = behavior_Session
        self.behavior_Session3 = behavior_Session3 if behavior_Session3 is not None else set()
        
    @property
    def startTime(self) -> str:
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def endTime(self) -> str:
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def transactionType(self) -> str:
        return self.__transactionType

    @transactionType.setter
    def transactionType(self, transactionType: str):
        self.__transactionType = transactionType

    @property
    def behavior_Session(self):
        return self.__behavior_Session

    @behavior_Session.setter
    def behavior_Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Session__behavior_Session", None)
        self.__behavior_Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_SessionRepository"):
                opp_val = getattr(old_value, "behavior_SessionRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_SessionRepository"):
                opp_val = getattr(value, "behavior_SessionRepository", None)
                if opp_val is None:
                    setattr(value, "behavior_SessionRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behavior_Session3(self):
        return self.__behavior_Session3

    @behavior_Session3.setter
    def behavior_Session3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavior_Session__behavior_Session3", None)
        self.__behavior_Session3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_ObservedUseCaseExecution"):
                    opp_val = getattr(item, "behavior_ObservedUseCaseExecution", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_ObservedUseCaseExecution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_ObservedUseCaseExecution"):
                    opp_val = getattr(item, "behavior_ObservedUseCaseExecution", None)
                    
                    setattr(item, "behavior_ObservedUseCaseExecution", self)
                    

class behavior_SessionRepository:

    pass
class behavior_UseCaseRepository:

    pass