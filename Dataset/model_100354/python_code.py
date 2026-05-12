from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"


############################################
# Definition of Classes
############################################

class State:

    pass
class uml_FinalState(State):

    pass
class Vertex:

    pass
class uml_State(Vertex):

    pass
class uml_Pseudostate(Vertex):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class uml_Region:

    pass
class uml_Vertex(ABC):

    def __init__(self, name: str, uml_Vertex: "uml_Transition" = None, Vertex: "uml_Region" = None, uml_Vertex8: "uml_Transition" = None, subvertex: "uml_Region" = None):
        self.name = name
        self.uml_Vertex = uml_Vertex
        self.Vertex = Vertex
        self.uml_Vertex8 = uml_Vertex8
        self.subvertex = subvertex
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def subvertex(self):
        return self.__subvertex

    @subvertex.setter
    def subvertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Vertex__subvertex", None)
        self.__subvertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Region"):
                opp_val = getattr(old_value, "Region", None)
                if opp_val == self:
                    setattr(old_value, "Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Region"):
                opp_val = getattr(value, "Region", None)
                setattr(value, "Region", self)

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Vertex__Vertex", None)
        self.__Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Vertex8(self):
        return self.__uml_Vertex8

    @uml_Vertex8.setter
    def uml_Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Vertex__uml_Vertex8", None)
        self.__uml_Vertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition7"):
                opp_val = getattr(old_value, "uml_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition7"):
                opp_val = getattr(value, "uml_Transition7", None)
                setattr(value, "uml_Transition7", self)

    @property
    def uml_Vertex(self):
        return self.__uml_Vertex

    @uml_Vertex.setter
    def uml_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Vertex__uml_Vertex", None)
        self.__uml_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition5"):
                opp_val = getattr(old_value, "uml_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition5"):
                opp_val = getattr(value, "uml_Transition5", None)
                setattr(value, "uml_Transition5", self)

class uml_Trigger:

    def __init__(self, name: str, uml_Trigger: "uml_Transition" = None):
        self.name = name
        self.uml_Trigger = uml_Trigger
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def uml_Trigger(self):
        return self.__uml_Trigger

    @uml_Trigger.setter
    def uml_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Trigger__uml_Trigger", None)
        self.__uml_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition3"):
                opp_val = getattr(old_value, "uml_Transition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition3"):
                opp_val = getattr(value, "uml_Transition3", None)
                if opp_val is None:
                    setattr(value, "uml_Transition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_Behavior(ABC):

    def __init__(self, name: str, uml_Behavior: "uml_Transition" = None, uml_Behavior15: "uml_State" = None, uml_Behavior18: "uml_State" = None, uml_Behavior21: "uml_State" = None):
        self.name = name
        self.uml_Behavior = uml_Behavior
        self.uml_Behavior15 = uml_Behavior15
        self.uml_Behavior18 = uml_Behavior18
        self.uml_Behavior21 = uml_Behavior21
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def uml_Behavior15(self):
        return self.__uml_Behavior15

    @uml_Behavior15.setter
    def uml_Behavior15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior15", None)
        self.__uml_Behavior15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State"):
                opp_val = getattr(old_value, "uml_State", None)
                if opp_val == self:
                    setattr(old_value, "uml_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State"):
                opp_val = getattr(value, "uml_State", None)
                setattr(value, "uml_State", self)

    @property
    def uml_Behavior(self):
        return self.__uml_Behavior

    @uml_Behavior.setter
    def uml_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior", None)
        self.__uml_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Transition"):
                opp_val = getattr(old_value, "uml_Transition", None)
                if opp_val == self:
                    setattr(old_value, "uml_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Transition"):
                opp_val = getattr(value, "uml_Transition", None)
                setattr(value, "uml_Transition", self)

    @property
    def uml_Behavior21(self):
        return self.__uml_Behavior21

    @uml_Behavior21.setter
    def uml_Behavior21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior21", None)
        self.__uml_Behavior21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State20"):
                opp_val = getattr(old_value, "uml_State20", None)
                if opp_val == self:
                    setattr(old_value, "uml_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State20"):
                opp_val = getattr(value, "uml_State20", None)
                setattr(value, "uml_State20", self)

    @property
    def uml_Behavior18(self):
        return self.__uml_Behavior18

    @uml_Behavior18.setter
    def uml_Behavior18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Behavior__uml_Behavior18", None)
        self.__uml_Behavior18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_State17"):
                opp_val = getattr(old_value, "uml_State17", None)
                if opp_val == self:
                    setattr(old_value, "uml_State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_State17"):
                opp_val = getattr(value, "uml_State17", None)
                setattr(value, "uml_State17", self)

class uml_Transition:

    def __init__(self, name: str, uml_Transition: "uml_Behavior" = None, uml_Transition3: set["uml_Trigger"] = None, uml_Transition5: "uml_Vertex" = None, uml_Transition12: "uml_Region" = None, uml_Transition7: "uml_Vertex" = None):
        self.name = name
        self.uml_Transition = uml_Transition
        self.uml_Transition3 = uml_Transition3 if uml_Transition3 is not None else set()
        self.uml_Transition5 = uml_Transition5
        self.uml_Transition12 = uml_Transition12
        self.uml_Transition7 = uml_Transition7
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def uml_Transition3(self):
        return self.__uml_Transition3

    @uml_Transition3.setter
    def uml_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition3", None)
        self.__uml_Transition3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_Trigger"):
                    opp_val = getattr(item, "uml_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_Trigger"):
                    opp_val = getattr(item, "uml_Trigger", None)
                    
                    setattr(item, "uml_Trigger", self)
                    

    @property
    def uml_Transition12(self):
        return self.__uml_Transition12

    @uml_Transition12.setter
    def uml_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition12", None)
        self.__uml_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Region11"):
                opp_val = getattr(old_value, "uml_Region11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Region11"):
                opp_val = getattr(value, "uml_Region11", None)
                if opp_val is None:
                    setattr(value, "uml_Region11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_Transition(self):
        return self.__uml_Transition

    @uml_Transition.setter
    def uml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition", None)
        self.__uml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Behavior"):
                opp_val = getattr(old_value, "uml_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "uml_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Behavior"):
                opp_val = getattr(value, "uml_Behavior", None)
                setattr(value, "uml_Behavior", self)

    @property
    def uml_Transition7(self):
        return self.__uml_Transition7

    @uml_Transition7.setter
    def uml_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition7", None)
        self.__uml_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex8"):
                opp_val = getattr(old_value, "uml_Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "uml_Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex8"):
                opp_val = getattr(value, "uml_Vertex8", None)
                setattr(value, "uml_Vertex8", self)

    @property
    def uml_Transition5(self):
        return self.__uml_Transition5

    @uml_Transition5.setter
    def uml_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Transition__uml_Transition5", None)
        self.__uml_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Vertex"):
                opp_val = getattr(old_value, "uml_Vertex", None)
                if opp_val == self:
                    setattr(old_value, "uml_Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Vertex"):
                opp_val = getattr(value, "uml_Vertex", None)
                setattr(value, "uml_Vertex", self)

class Behavior:

    pass
class uml_Activity(Behavior):

    pass
class uml_StateMachine(Behavior):

    pass