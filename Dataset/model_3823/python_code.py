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
class ChoiceKind(Enum):
    dynamic = "dynamic"
    static = "static"


############################################
# Definition of Classes
############################################

class Declaration:

    pass
class sgraph_ImportDeclaration(Declaration):

    pass
class sgraph_ScopedElement(ABC):

    def __init__(self, namespace: str, sgraph_ScopedElement: set["sgraph_Scope"] = None):
        self.namespace = namespace
        self.sgraph_ScopedElement = sgraph_ScopedElement if sgraph_ScopedElement is not None else set()
        
    @property
    def namespace(self) -> str:
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
                if hasattr(item, "sgraph_Scope26"):
                    opp_val = getattr(item, "sgraph_Scope26", None)
                    
                    if opp_val == self:
                        setattr(item, "sgraph_Scope26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgraph_Scope26"):
                    opp_val = getattr(item, "sgraph_Scope26", None)
                    
                    setattr(item, "sgraph_Scope26", self)
                    

class sgraph_Property:

    pass
class sgraph_Event:

    pass
class sgraph_Declaration:

    pass
class sgraph_Scope:

    pass
class sgraph_SpecificationElement(ABC):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class sgraph_ReactionProperty:

    pass
class sgraph_Effect(ABC):

    pass
class sgraph_Trigger(ABC):

    pass
class sgraph_Reaction(ABC):

    pass
class sgraph_ReactiveElement(ABC):

    pass
class DomainElement:

    pass
class CompositeElement:

    pass
class ScopedElement:

    pass
class ReactiveElement:

    pass
class Pseudostate:

    pass
class sgraph_Exit(Pseudostate):

    pass
class sgraph_Entry(Pseudostate):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class sgraph_Synchronization(Pseudostate):

    pass
class sgraph_Choice(Pseudostate):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
class sgraph_State(SpecificationElement, DocumentedElement, RegularState, ScopedElement, ReactiveElement, CompositeElement):

    def __init__(self, orthogonal: bool, simple: bool, composite: bool, leaf: bool):
        self.orthogonal = orthogonal
        self.simple = simple
        self.composite = composite
        self.leaf = leaf
        
    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def simple(self) -> bool:
        return self.__simple

    @simple.setter
    def simple(self, simple: bool):
        self.__simple = simple

    @property
    def orthogonal(self) -> bool:
        return self.__orthogonal

    @orthogonal.setter
    def orthogonal(self, orthogonal: bool):
        self.__orthogonal = orthogonal

    @property
    def composite(self) -> bool:
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite

class sgraph_CompositeElement(ABC):

    pass
class sgraph_Transition(Reaction, DocumentedElement, SpecificationElement):

    pass
class NamedElement:

    pass
class sgraph_Statechart(NamedElement, SpecificationElement, DocumentedElement, ReactiveElement, ScopedElement, DomainElement, CompositeElement):

    pass
class sgraph_Region(NamedElement):

    pass
class sgraph_Vertex(NamedElement):

    pass
class Vertex:

    pass
class sgraph_RegularState(Vertex):

    pass
class sgraph_Pseudostate(Vertex):

    pass