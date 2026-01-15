from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    final = "final"


############################################
# Definition of Classes
############################################

class statemachine_Action:

    def __init__(self, name: str, statemachine_Action20: "statemachine_LabeledTransition" = None, statemachine_Action: "statemachine_Statemachine" = None):
        self.name = name
        self.statemachine_Action20 = statemachine_Action20
        self.statemachine_Action = statemachine_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Action20(self):
        return self.__statemachine_Action20

    @statemachine_Action20.setter
    def statemachine_Action20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Action__statemachine_Action20", None)
        self.__statemachine_Action20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_LabeledTransition"):
                opp_val = getattr(old_value, "statemachine_LabeledTransition", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_LabeledTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_LabeledTransition"):
                opp_val = getattr(value, "statemachine_LabeledTransition", None)
                setattr(value, "statemachine_LabeledTransition", self)

    @property
    def statemachine_Action(self):
        return self.__statemachine_Action

    @statemachine_Action.setter
    def statemachine_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Action__statemachine_Action", None)
        self.__statemachine_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine13"):
                opp_val = getattr(old_value, "statemachine_Statemachine13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine13"):
                opp_val = getattr(value, "statemachine_Statemachine13", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transition:

    pass
class statemachine_LabeledTransition(Transition):

    pass
class Region:

    pass
class statemachine_Statemachine(Region):

    def __init__(self, name: str, statemachine_Statemachine: set["statemachine_Transition"] = None, statemachine_Statemachine13: set["statemachine_Action"] = None):
        self.name = name
        self.statemachine_Statemachine = statemachine_Statemachine if statemachine_Statemachine is not None else set()
        self.statemachine_Statemachine13 = statemachine_Statemachine13 if statemachine_Statemachine13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Statemachine13(self):
        return self.__statemachine_Statemachine13

    @statemachine_Statemachine13.setter
    def statemachine_Statemachine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine13", None)
        self.__statemachine_Statemachine13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Action"):
                    opp_val = getattr(item, "statemachine_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Action"):
                    opp_val = getattr(item, "statemachine_Action", None)
                    
                    setattr(item, "statemachine_Action", self)
                    

    @property
    def statemachine_Statemachine(self):
        return self.__statemachine_Statemachine

    @statemachine_Statemachine.setter
    def statemachine_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine", None)
        self.__statemachine_Statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition11"):
                    opp_val = getattr(item, "statemachine_Transition11", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition11"):
                    opp_val = getattr(item, "statemachine_Transition11", None)
                    
                    setattr(item, "statemachine_Transition11", self)
                    

class statemachine_Region:

    pass
class State:

    pass
class statemachine_ComplexState(State):

    pass
class Vertex:

    pass
class statemachine_Pseudostate(Vertex):

    def __init__(self, kind: str, id: str, statemachine_Pseudostate: "statemachine_Region" = None):
        self.kind = kind
        self.id = id
        self.statemachine_Pseudostate = statemachine_Pseudostate
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def statemachine_Pseudostate(self):
        return self.__statemachine_Pseudostate

    @statemachine_Pseudostate.setter
    def statemachine_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Pseudostate__statemachine_Pseudostate", None)
        self.__statemachine_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Region18"):
                opp_val = getattr(old_value, "statemachine_Region18", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Region18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Region18"):
                opp_val = getattr(value, "statemachine_Region18", None)
                setattr(value, "statemachine_Region18", self)

class statemachine_State(Vertex):

    def __init__(self, name: str, statemachine_State: "statemachine_ComplexState" = None, statemachine_State16: "statemachine_Region" = None):
        self.name = name
        self.statemachine_State = statemachine_State
        self.statemachine_State16 = statemachine_State16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State16(self):
        return self.__statemachine_State16

    @statemachine_State16.setter
    def statemachine_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State16", None)
        self.__statemachine_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Region15"):
                opp_val = getattr(old_value, "statemachine_Region15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Region15"):
                opp_val = getattr(value, "statemachine_Region15", None)
                if opp_val is None:
                    setattr(value, "statemachine_Region15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_ComplexState"):
                opp_val = getattr(old_value, "statemachine_ComplexState", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_ComplexState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_ComplexState"):
                opp_val = getattr(value, "statemachine_ComplexState", None)
                setattr(value, "statemachine_ComplexState", self)

class statemachine_Transition:

    def __init__(self, id: str, statemachine_Transition: "statemachine_Vertex" = None, statemachine_Transition5: "statemachine_Vertex" = None, statemachine_Transition8: "statemachine_Vertex" = None, statemachine_Transition11: "statemachine_Statemachine" = None):
        self.id = id
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition5 = statemachine_Transition5
        self.statemachine_Transition8 = statemachine_Transition8
        self.statemachine_Transition11 = statemachine_Transition11
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def statemachine_Transition11(self):
        return self.__statemachine_Transition11

    @statemachine_Transition11.setter
    def statemachine_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition11", None)
        self.__statemachine_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine"):
                opp_val = getattr(old_value, "statemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine"):
                opp_val = getattr(value, "statemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Transition5(self):
        return self.__statemachine_Transition5

    @statemachine_Transition5.setter
    def statemachine_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition5", None)
        self.__statemachine_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Vertex6"):
                opp_val = getattr(old_value, "statemachine_Vertex6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Vertex6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Vertex6"):
                opp_val = getattr(value, "statemachine_Vertex6", None)
                setattr(value, "statemachine_Vertex6", self)

    @property
    def statemachine_Transition8(self):
        return self.__statemachine_Transition8

    @statemachine_Transition8.setter
    def statemachine_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition8", None)
        self.__statemachine_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Vertex9"):
                opp_val = getattr(old_value, "statemachine_Vertex9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Vertex9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Vertex9"):
                opp_val = getattr(value, "statemachine_Vertex9", None)
                setattr(value, "statemachine_Vertex9", self)

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Vertex"):
                opp_val = getattr(old_value, "statemachine_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Vertex"):
                opp_val = getattr(value, "statemachine_Vertex", None)
                if opp_val is None:
                    setattr(value, "statemachine_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Vertex(ABC):

    pass