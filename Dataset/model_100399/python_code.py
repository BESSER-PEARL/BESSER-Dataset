from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ChoiceKind(Enum):
    dynamic = "dynamic"
    static = "static"
class EntryKind(Enum):
    deepHistory = "deepHistory"
    initial = "initial"
    shallowHistory = "shallowHistory"


############################################
# Definition of Classes
############################################

class sgraph_Statement:

    pass
class sgraph_ScopedElement(ABC):

    def __init__(self, namespace: str, sgraph_ScopedElement: set["sgraph_Scope"] = None):
        self.namespace = namespace
        self.sgraph_ScopedElement = sgraph_ScopedElement if sgraph_ScopedElement is not None else set()
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def sgraph_ScopedElement(self):
        return self.__sgraph_ScopedElement

    @sgraph_ScopedElement.setter
    def sgraph_ScopedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_ScopedElement__sgraph_ScopedElement", None)
        self.__sgraph_ScopedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sgraph_Scope24"):
                    opp_val = getattr(item, "sgraph_Scope24", None)
                    
                    if opp_val == self:
                        setattr(item, "sgraph_Scope24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgraph_Scope24"):
                    opp_val = getattr(item, "sgraph_Scope24", None)
                    
                    setattr(item, "sgraph_Scope24", self)
                    

class sgraph_Scope:

    pass
class sgraph_Reaction(ABC):

    pass
class sgraph_SpecificationElement(ABC):

    def __init__(self, specification: str):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class sgraph_Effect(ABC):

    pass
class sgraph_Trigger(ABC):

    pass
class sgraph_ReactiveElement(ABC):

    pass
class Pseudostate:

    pass
class sgraph_Synchronization(Pseudostate):

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


class sgraph_Exit(Pseudostate):

    pass
class sgraph_Choice(Pseudostate):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class Declaration:

    pass
class sgraph_Event(Declaration):

    pass
class sgraph_Variable(Declaration):

    pass
class RegularState:

    pass
class sgraph_FinalState(RegularState):

    pass
class DocumentedElement:

    pass
class Reaction:

    pass
class SpecificationElement:

    pass
class CompositeElement:

    pass
class ScopedElement:

    pass
class ReactiveElement:

    pass
class sgraph_State(RegularState, SpecificationElement, ScopedElement, CompositeElement, ReactiveElement, DocumentedElement):

    def __init__(self, orthogonal: bool, substatechartId: str, subchart: bool, simple: bool, composite: bool, leaf: bool, sgraph_State: "sgraph_Statechart" = None):
        self.orthogonal = orthogonal
        self.substatechartId = substatechartId
        self.subchart = subchart
        self.simple = simple
        self.composite = composite
        self.leaf = leaf
        self.sgraph_State = sgraph_State
        
        pass
    @property
    def orthogonal(self):
        return self.__orthogonal

    @orthogonal.setter
    def orthogonal(self, orthogonal: bool):
        self.__orthogonal = orthogonal


    @property
    def composite(self):
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite


    @property
    def subchart(self):
        return self.__subchart

    @subchart.setter
    def subchart(self, subchart: bool):
        self.__subchart = subchart


    @property
    def substatechartId(self):
        return self.__substatechartId

    @substatechartId.setter
    def substatechartId(self, substatechartId: str):
        self.__substatechartId = substatechartId


    @property
    def leaf(self):
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf


    @property
    def simple(self):
        return self.__simple

    @simple.setter
    def simple(self, simple: bool):
        self.__simple = simple


    @property
    def sgraph_State(self):
        return self.__sgraph_State

    @sgraph_State.setter
    def sgraph_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_State__sgraph_State", None)
        self.__sgraph_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sgraph_Statechart"):
                opp_val = getattr(old_value, "sgraph_Statechart", None)
                if opp_val == self:
                    setattr(old_value, "sgraph_Statechart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgraph_Statechart"):
                opp_val = getattr(value, "sgraph_Statechart", None)
                setattr(value, "sgraph_Statechart", self)

class sgraph_Transition(Reaction, DocumentedElement, SpecificationElement):

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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex7"):
                opp_val = getattr(old_value, "Vertex7", None)
                if opp_val == self:
                    setattr(old_value, "Vertex7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex7"):
                opp_val = getattr(value, "Vertex7", None)
                setattr(value, "Vertex7", self)

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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex9"):
                opp_val = getattr(old_value, "Vertex9", None)
                if opp_val == self:
                    setattr(old_value, "Vertex9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex9"):
                opp_val = getattr(value, "Vertex9", None)
                setattr(value, "Vertex9", self)

class NamedElement:

    pass
class sgraph_Statechart(NamedElement, SpecificationElement, ScopedElement, CompositeElement, ReactiveElement, DocumentedElement):

    pass
class sgraph_Region(NamedElement):

    def __init__(self, priority: int, Region: "sgraph_Vertex" = None, parentRegion: set["sgraph_Vertex"] = None, regions: "sgraph_CompositeElement" = None, Region27: "sgraph_CompositeElement" = None):
        self.priority = priority
        self.Region = Region
        self.parentRegion = parentRegion if parentRegion is not None else set()
        self.regions = regions
        self.Region27 = Region27
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


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
    def regions(self):
        return self.__regions

    @regions.setter
    def regions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__regions", None)
        self.__regions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeElement"):
                opp_val = getattr(old_value, "CompositeElement", None)
                if opp_val == self:
                    setattr(old_value, "CompositeElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeElement"):
                opp_val = getattr(value, "CompositeElement", None)
                setattr(value, "CompositeElement", self)

    @property
    def Region27(self):
        return self.__Region27

    @Region27.setter
    def Region27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Region__Region27", None)
        self.__Region27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composite"):
                opp_val = getattr(old_value, "composite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composite"):
                opp_val = getattr(value, "composite", None)
                if opp_val is None:
                    setattr(value, "composite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class sgraph_Declaration(NamedElement):

    pass
class sgraph_Vertex(NamedElement):

    pass
class Vertex:

    pass
class sgraph_RegularState(Vertex):

    pass
class sgraph_Pseudostate(Vertex):

    pass
class sgraph_CompositeElement(ABC):

    pass