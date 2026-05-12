from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EntryKind(Enum):
    initial = "initial"
    shallowHistory = "shallowHistory"
    deepHistory = "deepHistory"


############################################
# Definition of Classes
############################################

class sgraph_ScopedElement(ABC):

    pass
class sgraph_Scope:

    pass
class sgraph_Statement:

    pass
class sgraph_ReactiveElement(ABC):

    pass
class sgraph_Reaction(ABC):

    pass
class sgraph_ExpressionElement(ABC):

    def __init__(self, expression: str):
        self.expression = expression
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class sgraph_Effect(ABC):

    pass
class sgraph_Trigger(ABC):

    pass
class ScopedElement:

    pass
class ReactiveElement:

    pass
class Pseudostate:

    pass
class sgraph_Synchronization(Pseudostate):

    pass
class sgraph_Exit(Pseudostate):

    pass
class sgraph_Entry(Pseudostate):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class sgraph_Choice(Pseudostate):

    pass
class sgraph_Junction(Pseudostate):

    pass
class Declaration:

    pass
class sgraph_Event(Declaration):

    pass
class sgraph_Variable(Declaration):

    pass
class Reaction:

    pass
class ExpressionElement:

    pass
class sgraph_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class sgraph_Transition(Reaction, ExpressionElement):

    def __init__(self, priority: int, Transition: "sgraph_Vertex" = None, Transition3: "sgraph_Vertex" = None, incomingTransitions: "sgraph_Vertex" = None, outgoingTransitions: "sgraph_Vertex" = None):
        self.priority = priority
        self.Transition = Transition
        self.Transition3 = Transition3
        self.incomingTransitions = incomingTransitions
        self.outgoingTransitions = outgoingTransitions
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex8"):
                opp_val = getattr(old_value, "Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex8"):
                opp_val = getattr(value, "Vertex8", None)
                setattr(value, "Vertex8", self)

    @property
    def Transition3(self):
        return self.__Transition3

    @Transition3.setter
    def Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__Transition3", None)
        self.__Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex6"):
                opp_val = getattr(old_value, "Vertex6", None)
                if opp_val == self:
                    setattr(old_value, "Vertex6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex6"):
                opp_val = getattr(value, "Vertex6", None)
                setattr(value, "Vertex6", self)

class NamedElement:

    pass
class sgraph_Statechart(NamedElement, ReactiveElement, ExpressionElement, ScopedElement):

    pass
class sgraph_Region(NamedElement):

    def __init__(self, priority: int, Region: "sgraph_Vertex" = None, parentRegion: set["sgraph_Vertex"] = None, sgraph_Region: "sgraph_Statechart" = None, sgraph_Region26: "sgraph_State" = None):
        self.priority = priority
        self.Region = Region
        self.parentRegion = parentRegion if parentRegion is not None else set()
        self.sgraph_Region = sgraph_Region
        self.sgraph_Region26 = sgraph_Region26
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def parentRegion(self):
        return self.__parentRegion

    @parentRegion.setter
    def parentRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__parentRegion", None)
        self.__parentRegion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    setattr(item, "Vertex", self)
                    

    @property
    def sgraph_Region26(self):
        return self.__sgraph_Region26

    @sgraph_Region26.setter
    def sgraph_Region26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__sgraph_Region26", None)
        self.__sgraph_Region26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgraph_State"):
                opp_val = getattr(old_value, "sgraph_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgraph_State"):
                opp_val = getattr(value, "sgraph_State", None)
                if opp_val is None:
                    setattr(value, "sgraph_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Region(self):
        return self.__Region

    @Region.setter
    def Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__Region", None)
        self.__Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vertices"):
                opp_val = getattr(old_value, "vertices", None)
                if opp_val == self:
                    setattr(old_value, "vertices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vertices"):
                opp_val = getattr(value, "vertices", None)
                setattr(value, "vertices", self)

    @property
    def sgraph_Region(self):
        return self.__sgraph_Region

    @sgraph_Region.setter
    def sgraph_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__sgraph_Region", None)
        self.__sgraph_Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgraph_Statechart"):
                opp_val = getattr(old_value, "sgraph_Statechart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgraph_Statechart"):
                opp_val = getattr(value, "sgraph_Statechart", None)
                if opp_val is None:
                    setattr(value, "sgraph_Statechart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sgraph_Declaration(NamedElement):

    pass
class sgraph_Vertex(NamedElement):

    pass
class Vertex:

    pass
class sgraph_FinalState(Vertex):

    pass
class sgraph_State(Vertex, ReactiveElement, ExpressionElement, ScopedElement):

    def __init__(self, orthogonal: bool, submachine: bool, simple: bool, composite: bool, leaf: bool, sgraph_State: set["sgraph_Region"] = None, sgraph_State28: "sgraph_Statechart" = None):
        self.orthogonal = orthogonal
        self.submachine = submachine
        self.simple = simple
        self.composite = composite
        self.leaf = leaf
        self.sgraph_State = sgraph_State if sgraph_State is not None else set()
        self.sgraph_State28 = sgraph_State28
        
        pass
    @property
    def orthogonal(self):
        return self.__orthogonal

    @orthogonal.setter
    def orthogonal(self, orthogonal: bool):
        self.__orthogonal = orthogonal


    @property
    def submachine(self):
        return self.__submachine

    @submachine.setter
    def submachine(self, submachine: bool):
        self.__submachine = submachine


    @property
    def composite(self):
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite


    @property
    def simple(self):
        return self.__simple

    @simple.setter
    def simple(self, simple: bool):
        self.__simple = simple


    @property
    def leaf(self):
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf


    @property
    def sgraph_State28(self):
        return self.__sgraph_State28

    @sgraph_State28.setter
    def sgraph_State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_State__sgraph_State28", None)
        self.__sgraph_State28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgraph_Statechart29"):
                opp_val = getattr(old_value, "sgraph_Statechart29", None)
                if opp_val == self:
                    setattr(old_value, "sgraph_Statechart29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgraph_Statechart29"):
                opp_val = getattr(value, "sgraph_Statechart29", None)
                setattr(value, "sgraph_Statechart29", self)

    @property
    def sgraph_State(self):
        return self.__sgraph_State

    @sgraph_State.setter
    def sgraph_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_State__sgraph_State", None)
        self.__sgraph_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgraph_Region26"):
                    opp_val = getattr(item, "sgraph_Region26", None)
                    
                    if opp_val == self:
                        setattr(item, "sgraph_Region26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgraph_Region26"):
                    opp_val = getattr(item, "sgraph_Region26", None)
                    
                    setattr(item, "sgraph_Region26", self)
                    

class sgraph_Pseudostate(Vertex):

    pass