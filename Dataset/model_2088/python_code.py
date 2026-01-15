from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventType(Enum):
    Basic = "Basic"
    External = "External"
    Intermediate = "Intermediate"
    Undeveloped = "Undeveloped"
class LogicOperation(Enum):
    Or = "Or"
    And = "And"
    Xor = "Xor"
    PriorityAnd = "PriorityAnd"
    kOf = "kOf"
    kOrmore = "kOrmore"
    kOrless = "kOrless"
class FaultTreeType(Enum):
    FaultTree = "FaultTree"
    FaultTrace = "FaultTrace"
    MinimalCutSet = "MinimalCutSet"
    CompositeParts = "CompositeParts"


############################################
# Definition of Classes
############################################

class FaultTree_FaultTree:

    def __init__(self, name: str, message: str, faultTreeType: str, FaultTree_FaultTree: "FaultTree_Event" = None, FaultTree_FaultTree4: set["FaultTree_Event"] = None, FaultTree_FaultTree2: "FaultTree_EObject" = None):
        self.name = name
        self.message = message
        self.faultTreeType = faultTreeType
        self.FaultTree_FaultTree = FaultTree_FaultTree
        self.FaultTree_FaultTree4 = FaultTree_FaultTree4 if FaultTree_FaultTree4 is not None else set()
        self.FaultTree_FaultTree2 = FaultTree_FaultTree2
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def faultTreeType(self) -> str:
        return self.__faultTreeType

    @faultTreeType.setter
    def faultTreeType(self, faultTreeType: str):
        self.__faultTreeType = faultTreeType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FaultTree_FaultTree4(self):
        return self.__FaultTree_FaultTree4

    @FaultTree_FaultTree4.setter
    def FaultTree_FaultTree4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_FaultTree__FaultTree_FaultTree4", None)
        self.__FaultTree_FaultTree4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FaultTree_Event5"):
                    opp_val = getattr(item, "FaultTree_Event5", None)
                    
                    if opp_val == self:
                        setattr(item, "FaultTree_Event5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FaultTree_Event5"):
                    opp_val = getattr(item, "FaultTree_Event5", None)
                    
                    setattr(item, "FaultTree_Event5", self)
                    

    @property
    def FaultTree_FaultTree2(self):
        return self.__FaultTree_FaultTree2

    @FaultTree_FaultTree2.setter
    def FaultTree_FaultTree2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_FaultTree__FaultTree_FaultTree2", None)
        self.__FaultTree_FaultTree2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_EObject"):
                opp_val = getattr(old_value, "FaultTree_EObject", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_EObject"):
                opp_val = getattr(value, "FaultTree_EObject", None)
                setattr(value, "FaultTree_EObject", self)

    @property
    def FaultTree_FaultTree(self):
        return self.__FaultTree_FaultTree

    @FaultTree_FaultTree.setter
    def FaultTree_FaultTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_FaultTree__FaultTree_FaultTree", None)
        self.__FaultTree_FaultTree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_Event"):
                opp_val = getattr(old_value, "FaultTree_Event", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_Event"):
                opp_val = getattr(value, "FaultTree_Event", None)
                setattr(value, "FaultTree_Event", self)

class FaultTree_EObject:

    pass
class FaultTree_Event:

    def __init__(self, name: str, message: str, k: int, assignedProbability: str, computedProbability: str, referenceCount: int, type: str, subEventLogic: str, scale: str, FaultTree_Event: "FaultTree_FaultTree" = None, FaultTree_Event5: "FaultTree_FaultTree" = None, FaultTree_Event6: set["FaultTree_Event"] = None, FaultTree_Event10: "FaultTree_EObject" = None, FaultTree_Event13: "FaultTree_EObject" = None, FaultTree_Event8: "FaultTree_Event" = None, FaultTree_Event16: "FaultTree_EObject" = None):
        self.name = name
        self.message = message
        self.k = k
        self.assignedProbability = assignedProbability
        self.computedProbability = computedProbability
        self.referenceCount = referenceCount
        self.type = type
        self.subEventLogic = subEventLogic
        self.scale = scale
        self.FaultTree_Event = FaultTree_Event
        self.FaultTree_Event5 = FaultTree_Event5
        self.FaultTree_Event6 = FaultTree_Event6 if FaultTree_Event6 is not None else set()
        self.FaultTree_Event10 = FaultTree_Event10
        self.FaultTree_Event13 = FaultTree_Event13
        self.FaultTree_Event8 = FaultTree_Event8
        self.FaultTree_Event16 = FaultTree_Event16
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def computedProbability(self) -> str:
        return self.__computedProbability

    @computedProbability.setter
    def computedProbability(self, computedProbability: str):
        self.__computedProbability = computedProbability

    @property
    def assignedProbability(self) -> str:
        return self.__assignedProbability

    @assignedProbability.setter
    def assignedProbability(self, assignedProbability: str):
        self.__assignedProbability = assignedProbability

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def subEventLogic(self) -> str:
        return self.__subEventLogic

    @subEventLogic.setter
    def subEventLogic(self, subEventLogic: str):
        self.__subEventLogic = subEventLogic

    @property
    def referenceCount(self) -> int:
        return self.__referenceCount

    @referenceCount.setter
    def referenceCount(self, referenceCount: int):
        self.__referenceCount = referenceCount

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def k(self) -> int:
        return self.__k

    @k.setter
    def k(self, k: int):
        self.__k = k

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FaultTree_Event(self):
        return self.__FaultTree_Event

    @FaultTree_Event.setter
    def FaultTree_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event", None)
        self.__FaultTree_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_FaultTree"):
                opp_val = getattr(old_value, "FaultTree_FaultTree", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_FaultTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_FaultTree"):
                opp_val = getattr(value, "FaultTree_FaultTree", None)
                setattr(value, "FaultTree_FaultTree", self)

    @property
    def FaultTree_Event8(self):
        return self.__FaultTree_Event8

    @FaultTree_Event8.setter
    def FaultTree_Event8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event8", None)
        self.__FaultTree_Event8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_Event6"):
                opp_val = getattr(old_value, "FaultTree_Event6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_Event6"):
                opp_val = getattr(value, "FaultTree_Event6", None)
                if opp_val is None:
                    setattr(value, "FaultTree_Event6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FaultTree_Event13(self):
        return self.__FaultTree_Event13

    @FaultTree_Event13.setter
    def FaultTree_Event13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event13", None)
        self.__FaultTree_Event13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_EObject14"):
                opp_val = getattr(old_value, "FaultTree_EObject14", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_EObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_EObject14"):
                opp_val = getattr(value, "FaultTree_EObject14", None)
                setattr(value, "FaultTree_EObject14", self)

    @property
    def FaultTree_Event6(self):
        return self.__FaultTree_Event6

    @FaultTree_Event6.setter
    def FaultTree_Event6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event6", None)
        self.__FaultTree_Event6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FaultTree_Event8"):
                    opp_val = getattr(item, "FaultTree_Event8", None)
                    
                    if opp_val == self:
                        setattr(item, "FaultTree_Event8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FaultTree_Event8"):
                    opp_val = getattr(item, "FaultTree_Event8", None)
                    
                    setattr(item, "FaultTree_Event8", self)
                    

    @property
    def FaultTree_Event16(self):
        return self.__FaultTree_Event16

    @FaultTree_Event16.setter
    def FaultTree_Event16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event16", None)
        self.__FaultTree_Event16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_EObject17"):
                opp_val = getattr(old_value, "FaultTree_EObject17", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_EObject17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_EObject17"):
                opp_val = getattr(value, "FaultTree_EObject17", None)
                setattr(value, "FaultTree_EObject17", self)

    @property
    def FaultTree_Event10(self):
        return self.__FaultTree_Event10

    @FaultTree_Event10.setter
    def FaultTree_Event10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event10", None)
        self.__FaultTree_Event10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_EObject11"):
                opp_val = getattr(old_value, "FaultTree_EObject11", None)
                if opp_val == self:
                    setattr(old_value, "FaultTree_EObject11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_EObject11"):
                opp_val = getattr(value, "FaultTree_EObject11", None)
                setattr(value, "FaultTree_EObject11", self)

    @property
    def FaultTree_Event5(self):
        return self.__FaultTree_Event5

    @FaultTree_Event5.setter
    def FaultTree_Event5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FaultTree_Event__FaultTree_Event5", None)
        self.__FaultTree_Event5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FaultTree_FaultTree4"):
                opp_val = getattr(old_value, "FaultTree_FaultTree4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FaultTree_FaultTree4"):
                opp_val = getattr(value, "FaultTree_FaultTree4", None)
                if opp_val is None:
                    setattr(value, "FaultTree_FaultTree4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getProbability(self) -> str:
        # TODO: Implement getProbability method
        pass
