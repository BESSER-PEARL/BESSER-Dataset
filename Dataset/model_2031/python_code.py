from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Pseudokind(Enum):
    Initial = "Initial"
    End = "End"
    Exit = "Exit"
    DeepHistory = "DeepHistory"
    ShallowHistory = "ShallowHistory"


############################################
# Definition of Classes
############################################

class Vertex:

    pass
class MySM_Vertex:

    pass
class MySM_Pseudostate(Vertex):

    def __init__(self, psId: str, kind: str, MySM_Pseudostate: "MySM_Region" = None):
        self.psId = psId
        self.kind = kind
        self.MySM_Pseudostate = MySM_Pseudostate
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def psId(self) -> str:
        return self.__psId

    @psId.setter
    def psId(self, psId: str):
        self.__psId = psId

    @property
    def MySM_Pseudostate(self):
        return self.__MySM_Pseudostate

    @MySM_Pseudostate.setter
    def MySM_Pseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Pseudostate__MySM_Pseudostate", None)
        self.__MySM_Pseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Region5"):
                opp_val = getattr(old_value, "MySM_Region5", None)
                if opp_val == self:
                    setattr(old_value, "MySM_Region5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Region5"):
                opp_val = getattr(value, "MySM_Region5", None)
                setattr(value, "MySM_Region5", self)

class Transition:

    pass
class MySM_LabeledTransition(Transition):

    pass
class State:

    pass
class MySM_ComplexSate(State):

    pass
class Region:

    pass
class MySM_Statemachine(Region):

    pass
class MySM_State(Vertex):

    def __init__(self, name: str, MySM_State: "MySM_Region" = None):
        self.name = name
        self.MySM_State = MySM_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MySM_State(self):
        return self.__MySM_State

    @MySM_State.setter
    def MySM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_State__MySM_State", None)
        self.__MySM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Region"):
                opp_val = getattr(old_value, "MySM_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Region"):
                opp_val = getattr(value, "MySM_Region", None)
                if opp_val is None:
                    setattr(value, "MySM_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MySM_Region:

    def __init__(self, name: str, MySM_Region: set["MySM_State"] = None, MySM_Region9: "MySM_ComplexSate" = None, MySM_Region5: "MySM_Pseudostate" = None):
        self.name = name
        self.MySM_Region = MySM_Region if MySM_Region is not None else set()
        self.MySM_Region9 = MySM_Region9
        self.MySM_Region5 = MySM_Region5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MySM_Region5(self):
        return self.__MySM_Region5

    @MySM_Region5.setter
    def MySM_Region5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Region__MySM_Region5", None)
        self.__MySM_Region5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Pseudostate"):
                opp_val = getattr(old_value, "MySM_Pseudostate", None)
                if opp_val == self:
                    setattr(old_value, "MySM_Pseudostate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Pseudostate"):
                opp_val = getattr(value, "MySM_Pseudostate", None)
                setattr(value, "MySM_Pseudostate", self)

    @property
    def MySM_Region9(self):
        return self.__MySM_Region9

    @MySM_Region9.setter
    def MySM_Region9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Region__MySM_Region9", None)
        self.__MySM_Region9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_ComplexSate"):
                opp_val = getattr(old_value, "MySM_ComplexSate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_ComplexSate"):
                opp_val = getattr(value, "MySM_ComplexSate", None)
                if opp_val is None:
                    setattr(value, "MySM_ComplexSate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MySM_Region(self):
        return self.__MySM_Region

    @MySM_Region.setter
    def MySM_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Region__MySM_Region", None)
        self.__MySM_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MySM_State"):
                    opp_val = getattr(item, "MySM_State", None)
                    
                    if opp_val == self:
                        setattr(item, "MySM_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MySM_State"):
                    opp_val = getattr(item, "MySM_State", None)
                    
                    setattr(item, "MySM_State", self)
                    

class MySM_Action:

    def __init__(self, name: str, MySM_Action: "MySM_Statemachine" = None, MySM_Action17: "MySM_LabeledTransition" = None):
        self.name = name
        self.MySM_Action = MySM_Action
        self.MySM_Action17 = MySM_Action17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MySM_Action17(self):
        return self.__MySM_Action17

    @MySM_Action17.setter
    def MySM_Action17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Action__MySM_Action17", None)
        self.__MySM_Action17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_LabeledTransition"):
                opp_val = getattr(old_value, "MySM_LabeledTransition", None)
                if opp_val == self:
                    setattr(old_value, "MySM_LabeledTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_LabeledTransition"):
                opp_val = getattr(value, "MySM_LabeledTransition", None)
                setattr(value, "MySM_LabeledTransition", self)

    @property
    def MySM_Action(self):
        return self.__MySM_Action

    @MySM_Action.setter
    def MySM_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Action__MySM_Action", None)
        self.__MySM_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Statemachine2"):
                opp_val = getattr(old_value, "MySM_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Statemachine2"):
                opp_val = getattr(value, "MySM_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "MySM_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MySM_Transition:

    def __init__(self, tId: str, MySM_Transition: "MySM_Statemachine" = None, MySM_Transition11: "MySM_Vertex" = None, MySM_Transition14: "MySM_Vertex" = None, MySM_Transition7: "MySM_Vertex" = None):
        self.tId = tId
        self.MySM_Transition = MySM_Transition
        self.MySM_Transition11 = MySM_Transition11
        self.MySM_Transition14 = MySM_Transition14
        self.MySM_Transition7 = MySM_Transition7
        
    @property
    def tId(self) -> str:
        return self.__tId

    @tId.setter
    def tId(self, tId: str):
        self.__tId = tId

    @property
    def MySM_Transition11(self):
        return self.__MySM_Transition11

    @MySM_Transition11.setter
    def MySM_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Transition__MySM_Transition11", None)
        self.__MySM_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Vertex12"):
                opp_val = getattr(old_value, "MySM_Vertex12", None)
                if opp_val == self:
                    setattr(old_value, "MySM_Vertex12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Vertex12"):
                opp_val = getattr(value, "MySM_Vertex12", None)
                setattr(value, "MySM_Vertex12", self)

    @property
    def MySM_Transition7(self):
        return self.__MySM_Transition7

    @MySM_Transition7.setter
    def MySM_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Transition__MySM_Transition7", None)
        self.__MySM_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Vertex"):
                opp_val = getattr(old_value, "MySM_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Vertex"):
                opp_val = getattr(value, "MySM_Vertex", None)
                if opp_val is None:
                    setattr(value, "MySM_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MySM_Transition(self):
        return self.__MySM_Transition

    @MySM_Transition.setter
    def MySM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Transition__MySM_Transition", None)
        self.__MySM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Statemachine"):
                opp_val = getattr(old_value, "MySM_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Statemachine"):
                opp_val = getattr(value, "MySM_Statemachine", None)
                if opp_val is None:
                    setattr(value, "MySM_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MySM_Transition14(self):
        return self.__MySM_Transition14

    @MySM_Transition14.setter
    def MySM_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MySM_Transition__MySM_Transition14", None)
        self.__MySM_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MySM_Vertex15"):
                opp_val = getattr(old_value, "MySM_Vertex15", None)
                if opp_val == self:
                    setattr(old_value, "MySM_Vertex15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MySM_Vertex15"):
                opp_val = getattr(value, "MySM_Vertex15", None)
                setattr(value, "MySM_Vertex15", self)
