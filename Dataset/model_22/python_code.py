from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Temp(Enum):
    cold = "cold"
    without = "without"
    hot = "hot"
class Quantor(Enum):
    universal = "universal"
    existencial = "existencial"
class Orientation(Enum):
    normal = "normal"
    anti = "anti"


############################################
# Definition of Classes
############################################

class Arc:

    pass
class adaptiveSystem_ArcToEvent(Arc):

    pass
class adaptiveSystem_ArcToCondition(Arc):

    pass
class Node:

    pass
class adaptiveSystem_Event(Node):

    def __init__(self, saturated: bool, enabled: bool, Event: "adaptiveSystem_Condition" = None, Event17: "adaptiveSystem_Condition" = None, postEvents: set["adaptiveSystem_Condition"] = None, preEvents: set["adaptiveSystem_Condition"] = None, Event32: "adaptiveSystem_ArcToEvent" = None, destination24: set["adaptiveSystem_ArcToEvent"] = None, source27: set["adaptiveSystem_ArcToCondition"] = None, Event35: "adaptiveSystem_ArcToCondition" = None):
        self.saturated = saturated
        self.enabled = enabled
        self.Event = Event
        self.Event17 = Event17
        self.postEvents = postEvents if postEvents is not None else set()
        self.preEvents = preEvents if preEvents is not None else set()
        self.Event32 = Event32
        self.destination24 = destination24 if destination24 is not None else set()
        self.source27 = source27 if source27 is not None else set()
        self.Event35 = Event35
        
    @property
    def saturated(self) -> bool:
        return self.__saturated

    @saturated.setter
    def saturated(self, saturated: bool):
        self.__saturated = saturated

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def preEvents(self):
        return self.__preEvents

    @preEvents.setter
    def preEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__preEvents", None)
        self.__preEvents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition22"):
                    opp_val = getattr(item, "Condition22", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition22"):
                    opp_val = getattr(item, "Condition22", None)
                    
                    setattr(item, "Condition22", self)
                    

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "postConditions"):
                opp_val = getattr(old_value, "postConditions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postConditions"):
                opp_val = getattr(value, "postConditions", None)
                if opp_val is None:
                    setattr(value, "postConditions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Event17(self):
        return self.__Event17

    @Event17.setter
    def Event17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__Event17", None)
        self.__Event17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "preConditions"):
                opp_val = getattr(old_value, "preConditions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "preConditions"):
                opp_val = getattr(value, "preConditions", None)
                if opp_val is None:
                    setattr(value, "preConditions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source27(self):
        return self.__source27

    @source27.setter
    def source27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__source27", None)
        self.__source27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArcToCondition28"):
                    opp_val = getattr(item, "ArcToCondition28", None)
                    
                    if opp_val == self:
                        setattr(item, "ArcToCondition28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArcToCondition28"):
                    opp_val = getattr(item, "ArcToCondition28", None)
                    
                    setattr(item, "ArcToCondition28", self)
                    

    @property
    def Event32(self):
        return self.__Event32

    @Event32.setter
    def Event32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__Event32", None)
        self.__Event32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def postEvents(self):
        return self.__postEvents

    @postEvents.setter
    def postEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__postEvents", None)
        self.__postEvents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition"):
                    opp_val = getattr(item, "Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition"):
                    opp_val = getattr(item, "Condition", None)
                    
                    setattr(item, "Condition", self)
                    

    @property
    def destination24(self):
        return self.__destination24

    @destination24.setter
    def destination24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__destination24", None)
        self.__destination24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArcToEvent25"):
                    opp_val = getattr(item, "ArcToEvent25", None)
                    
                    if opp_val == self:
                        setattr(item, "ArcToEvent25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArcToEvent25"):
                    opp_val = getattr(item, "ArcToEvent25", None)
                    
                    setattr(item, "ArcToEvent25", self)
                    

    @property
    def Event35(self):
        return self.__Event35

    @Event35.setter
    def Event35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Event__Event35", None)
        self.__Event35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing34"):
                opp_val = getattr(old_value, "outgoing34", None)
                if opp_val == self:
                    setattr(old_value, "outgoing34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing34"):
                opp_val = getattr(value, "outgoing34", None)
                setattr(value, "outgoing34", self)

class adaptiveSystem_Condition(Node):

    def __init__(self, token: int, marked: bool, maximal: bool, minimal: bool, adaptiveSystem_Condition: "adaptiveSystem_PreNet" = None, adaptiveSystem_Condition14: "adaptiveSystem_AdaptiveProcess" = None, postConditions: set["adaptiveSystem_Event"] = None, preConditions: set["adaptiveSystem_Event"] = None, destination: set["adaptiveSystem_ArcToCondition"] = None, source: set["adaptiveSystem_ArcToEvent"] = None, Condition: "adaptiveSystem_Event" = None, Condition22: "adaptiveSystem_Event" = None, Condition38: "adaptiveSystem_ArcToCondition" = None, Condition30: "adaptiveSystem_ArcToEvent" = None):
        self.token = token
        self.marked = marked
        self.maximal = maximal
        self.minimal = minimal
        self.adaptiveSystem_Condition = adaptiveSystem_Condition
        self.adaptiveSystem_Condition14 = adaptiveSystem_Condition14
        self.postConditions = postConditions if postConditions is not None else set()
        self.preConditions = preConditions if preConditions is not None else set()
        self.destination = destination if destination is not None else set()
        self.source = source if source is not None else set()
        self.Condition = Condition
        self.Condition22 = Condition22
        self.Condition38 = Condition38
        self.Condition30 = Condition30
        
    @property
    def marked(self) -> bool:
        return self.__marked

    @marked.setter
    def marked(self, marked: bool):
        self.__marked = marked

    @property
    def maximal(self) -> bool:
        return self.__maximal

    @maximal.setter
    def maximal(self, maximal: bool):
        self.__maximal = maximal

    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def minimal(self) -> bool:
        return self.__minimal

    @minimal.setter
    def minimal(self, minimal: bool):
        self.__minimal = minimal

    @property
    def adaptiveSystem_Condition14(self):
        return self.__adaptiveSystem_Condition14

    @adaptiveSystem_Condition14.setter
    def adaptiveSystem_Condition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__adaptiveSystem_Condition14", None)
        self.__adaptiveSystem_Condition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_AdaptiveProcess13"):
                opp_val = getattr(old_value, "adaptiveSystem_AdaptiveProcess13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_AdaptiveProcess13"):
                opp_val = getattr(value, "adaptiveSystem_AdaptiveProcess13", None)
                if opp_val is None:
                    setattr(value, "adaptiveSystem_AdaptiveProcess13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adaptiveSystem_Condition(self):
        return self.__adaptiveSystem_Condition

    @adaptiveSystem_Condition.setter
    def adaptiveSystem_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__adaptiveSystem_Condition", None)
        self.__adaptiveSystem_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_PreNet11"):
                opp_val = getattr(old_value, "adaptiveSystem_PreNet11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_PreNet11"):
                opp_val = getattr(value, "adaptiveSystem_PreNet11", None)
                if opp_val is None:
                    setattr(value, "adaptiveSystem_PreNet11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArcToEvent"):
                    opp_val = getattr(item, "ArcToEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "ArcToEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArcToEvent"):
                    opp_val = getattr(item, "ArcToEvent", None)
                    
                    setattr(item, "ArcToEvent", self)
                    

    @property
    def Condition30(self):
        return self.__Condition30

    @Condition30.setter
    def Condition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__Condition30", None)
        self.__Condition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def Condition22(self):
        return self.__Condition22

    @Condition22.setter
    def Condition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__Condition22", None)
        self.__Condition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "preEvents"):
                opp_val = getattr(old_value, "preEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "preEvents"):
                opp_val = getattr(value, "preEvents", None)
                if opp_val is None:
                    setattr(value, "preEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Condition(self):
        return self.__Condition

    @Condition.setter
    def Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__Condition", None)
        self.__Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "postEvents"):
                opp_val = getattr(old_value, "postEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postEvents"):
                opp_val = getattr(value, "postEvents", None)
                if opp_val is None:
                    setattr(value, "postEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def preConditions(self):
        return self.__preConditions

    @preConditions.setter
    def preConditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__preConditions", None)
        self.__preConditions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event17"):
                    opp_val = getattr(item, "Event17", None)
                    
                    if opp_val == self:
                        setattr(item, "Event17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event17"):
                    opp_val = getattr(item, "Event17", None)
                    
                    setattr(item, "Event17", self)
                    

    @property
    def Condition38(self):
        return self.__Condition38

    @Condition38.setter
    def Condition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__Condition38", None)
        self.__Condition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming37"):
                opp_val = getattr(old_value, "incoming37", None)
                if opp_val == self:
                    setattr(old_value, "incoming37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming37"):
                opp_val = getattr(value, "incoming37", None)
                setattr(value, "incoming37", self)

    @property
    def postConditions(self):
        return self.__postConditions

    @postConditions.setter
    def postConditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__postConditions", None)
        self.__postConditions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Condition__destination", None)
        self.__destination = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArcToCondition"):
                    opp_val = getattr(item, "ArcToCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "ArcToCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArcToCondition"):
                    opp_val = getattr(item, "ArcToCondition", None)
                    
                    setattr(item, "ArcToCondition", self)
                    

class OccurrenceNet:

    pass
class adaptiveSystem_Arc:

    def __init__(self, weight: int, adaptiveSystem_Arc: "adaptiveSystem_OccurrenceNet" = None):
        self.weight = weight
        self.adaptiveSystem_Arc = adaptiveSystem_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def adaptiveSystem_Arc(self):
        return self.__adaptiveSystem_Arc

    @adaptiveSystem_Arc.setter
    def adaptiveSystem_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Arc__adaptiveSystem_Arc", None)
        self.__adaptiveSystem_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_OccurrenceNet9"):
                opp_val = getattr(old_value, "adaptiveSystem_OccurrenceNet9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_OccurrenceNet9"):
                opp_val = getattr(value, "adaptiveSystem_OccurrenceNet9", None)
                if opp_val is None:
                    setattr(value, "adaptiveSystem_OccurrenceNet9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adaptiveSystem_Node(ABC):

    def __init__(self, disabledByConflict: bool, name: str, abstract: bool, temp: str, disabledByAntiOclet: bool, adaptiveSystem_Node: "adaptiveSystem_OccurrenceNet" = None):
        self.disabledByConflict = disabledByConflict
        self.name = name
        self.abstract = abstract
        self.temp = temp
        self.disabledByAntiOclet = disabledByAntiOclet
        self.adaptiveSystem_Node = adaptiveSystem_Node
        
    @property
    def disabledByConflict(self) -> bool:
        return self.__disabledByConflict

    @disabledByConflict.setter
    def disabledByConflict(self, disabledByConflict: bool):
        self.__disabledByConflict = disabledByConflict

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def temp(self) -> str:
        return self.__temp

    @temp.setter
    def temp(self, temp: str):
        self.__temp = temp

    @property
    def disabledByAntiOclet(self) -> bool:
        return self.__disabledByAntiOclet

    @disabledByAntiOclet.setter
    def disabledByAntiOclet(self, disabledByAntiOclet: bool):
        self.__disabledByAntiOclet = disabledByAntiOclet

    @property
    def adaptiveSystem_Node(self):
        return self.__adaptiveSystem_Node

    @adaptiveSystem_Node.setter
    def adaptiveSystem_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Node__adaptiveSystem_Node", None)
        self.__adaptiveSystem_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_OccurrenceNet"):
                opp_val = getattr(old_value, "adaptiveSystem_OccurrenceNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_OccurrenceNet"):
                opp_val = getattr(value, "adaptiveSystem_OccurrenceNet", None)
                if opp_val is None:
                    setattr(value, "adaptiveSystem_OccurrenceNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adaptiveSystem_OccurrenceNet(ABC):

    def __init__(self, name: str, adaptiveSystem_OccurrenceNet: set["adaptiveSystem_Node"] = None, adaptiveSystem_OccurrenceNet9: set["adaptiveSystem_Arc"] = None):
        self.name = name
        self.adaptiveSystem_OccurrenceNet = adaptiveSystem_OccurrenceNet if adaptiveSystem_OccurrenceNet is not None else set()
        self.adaptiveSystem_OccurrenceNet9 = adaptiveSystem_OccurrenceNet9 if adaptiveSystem_OccurrenceNet9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adaptiveSystem_OccurrenceNet(self):
        return self.__adaptiveSystem_OccurrenceNet

    @adaptiveSystem_OccurrenceNet.setter
    def adaptiveSystem_OccurrenceNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_OccurrenceNet__adaptiveSystem_OccurrenceNet", None)
        self.__adaptiveSystem_OccurrenceNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adaptiveSystem_Node"):
                    opp_val = getattr(item, "adaptiveSystem_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "adaptiveSystem_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adaptiveSystem_Node"):
                    opp_val = getattr(item, "adaptiveSystem_Node", None)
                    
                    setattr(item, "adaptiveSystem_Node", self)
                    

    @property
    def adaptiveSystem_OccurrenceNet9(self):
        return self.__adaptiveSystem_OccurrenceNet9

    @adaptiveSystem_OccurrenceNet9.setter
    def adaptiveSystem_OccurrenceNet9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_OccurrenceNet__adaptiveSystem_OccurrenceNet9", None)
        self.__adaptiveSystem_OccurrenceNet9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adaptiveSystem_Arc"):
                    opp_val = getattr(item, "adaptiveSystem_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "adaptiveSystem_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adaptiveSystem_Arc"):
                    opp_val = getattr(item, "adaptiveSystem_Arc", None)
                    
                    setattr(item, "adaptiveSystem_Arc", self)
                    

class adaptiveSystem_PreNet(OccurrenceNet):

    pass
class adaptiveSystem_AdaptiveProcess(OccurrenceNet):

    pass
class adaptiveSystem_Oclet:

    def __init__(self, name: str, orientation: str, quantor: str, wellFormed: bool, adaptiveSystem_Oclet6: "adaptiveSystem_DoNet" = None, adaptiveSystem_Oclet: "adaptiveSystem_AdaptiveSystem" = None, adaptiveSystem_Oclet4: "adaptiveSystem_PreNet" = None):
        self.name = name
        self.orientation = orientation
        self.quantor = quantor
        self.wellFormed = wellFormed
        self.adaptiveSystem_Oclet6 = adaptiveSystem_Oclet6
        self.adaptiveSystem_Oclet = adaptiveSystem_Oclet
        self.adaptiveSystem_Oclet4 = adaptiveSystem_Oclet4
        
    @property
    def wellFormed(self) -> bool:
        return self.__wellFormed

    @wellFormed.setter
    def wellFormed(self, wellFormed: bool):
        self.__wellFormed = wellFormed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def quantor(self) -> str:
        return self.__quantor

    @quantor.setter
    def quantor(self, quantor: str):
        self.__quantor = quantor

    @property
    def adaptiveSystem_Oclet(self):
        return self.__adaptiveSystem_Oclet

    @adaptiveSystem_Oclet.setter
    def adaptiveSystem_Oclet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Oclet__adaptiveSystem_Oclet", None)
        self.__adaptiveSystem_Oclet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_AdaptiveSystem"):
                opp_val = getattr(old_value, "adaptiveSystem_AdaptiveSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_AdaptiveSystem"):
                opp_val = getattr(value, "adaptiveSystem_AdaptiveSystem", None)
                if opp_val is None:
                    setattr(value, "adaptiveSystem_AdaptiveSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adaptiveSystem_Oclet4(self):
        return self.__adaptiveSystem_Oclet4

    @adaptiveSystem_Oclet4.setter
    def adaptiveSystem_Oclet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Oclet__adaptiveSystem_Oclet4", None)
        self.__adaptiveSystem_Oclet4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_PreNet"):
                opp_val = getattr(old_value, "adaptiveSystem_PreNet", None)
                if opp_val == self:
                    setattr(old_value, "adaptiveSystem_PreNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_PreNet"):
                opp_val = getattr(value, "adaptiveSystem_PreNet", None)
                setattr(value, "adaptiveSystem_PreNet", self)

    @property
    def adaptiveSystem_Oclet6(self):
        return self.__adaptiveSystem_Oclet6

    @adaptiveSystem_Oclet6.setter
    def adaptiveSystem_Oclet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_Oclet__adaptiveSystem_Oclet6", None)
        self.__adaptiveSystem_Oclet6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_DoNet"):
                opp_val = getattr(old_value, "adaptiveSystem_DoNet", None)
                if opp_val == self:
                    setattr(old_value, "adaptiveSystem_DoNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_DoNet"):
                opp_val = getattr(value, "adaptiveSystem_DoNet", None)
                setattr(value, "adaptiveSystem_DoNet", self)

class adaptiveSystem_AdaptiveSystem:

    def __init__(self, setWellformednessToOclets: bool, adaptiveSystem_AdaptiveSystem: set["adaptiveSystem_Oclet"] = None, adaptiveSystem_AdaptiveSystem2: "adaptiveSystem_AdaptiveProcess" = None):
        self.setWellformednessToOclets = setWellformednessToOclets
        self.adaptiveSystem_AdaptiveSystem = adaptiveSystem_AdaptiveSystem if adaptiveSystem_AdaptiveSystem is not None else set()
        self.adaptiveSystem_AdaptiveSystem2 = adaptiveSystem_AdaptiveSystem2
        
    @property
    def setWellformednessToOclets(self) -> bool:
        return self.__setWellformednessToOclets

    @setWellformednessToOclets.setter
    def setWellformednessToOclets(self, setWellformednessToOclets: bool):
        self.__setWellformednessToOclets = setWellformednessToOclets

    @property
    def adaptiveSystem_AdaptiveSystem(self):
        return self.__adaptiveSystem_AdaptiveSystem

    @adaptiveSystem_AdaptiveSystem.setter
    def adaptiveSystem_AdaptiveSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_AdaptiveSystem__adaptiveSystem_AdaptiveSystem", None)
        self.__adaptiveSystem_AdaptiveSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adaptiveSystem_Oclet"):
                    opp_val = getattr(item, "adaptiveSystem_Oclet", None)
                    
                    if opp_val == self:
                        setattr(item, "adaptiveSystem_Oclet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adaptiveSystem_Oclet"):
                    opp_val = getattr(item, "adaptiveSystem_Oclet", None)
                    
                    setattr(item, "adaptiveSystem_Oclet", self)
                    

    @property
    def adaptiveSystem_AdaptiveSystem2(self):
        return self.__adaptiveSystem_AdaptiveSystem2

    @adaptiveSystem_AdaptiveSystem2.setter
    def adaptiveSystem_AdaptiveSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adaptiveSystem_AdaptiveSystem__adaptiveSystem_AdaptiveSystem2", None)
        self.__adaptiveSystem_AdaptiveSystem2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adaptiveSystem_AdaptiveProcess"):
                opp_val = getattr(old_value, "adaptiveSystem_AdaptiveProcess", None)
                if opp_val == self:
                    setattr(old_value, "adaptiveSystem_AdaptiveProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adaptiveSystem_AdaptiveProcess"):
                opp_val = getattr(value, "adaptiveSystem_AdaptiveProcess", None)
                setattr(value, "adaptiveSystem_AdaptiveProcess", self)

class adaptiveSystem_DoNet(OccurrenceNet):

    pass