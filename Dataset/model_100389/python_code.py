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
    initial = "initial"
    shallowHistory = "shallowHistory"
    deepHistory = "deepHistory"


############################################
# Definition of Classes
############################################

class SpecificationElement:

    pass
class sgraph_CompositeElement(ABC):

    pass
class NamedElement:

    pass
class sgraph_Region(NamedElement):

    pass
class sgraph_Vertex(NamedElement):

    pass
class Vertex:

    pass
class sgraph_RegularState(Vertex):

    pass
class sgraph_Scope:

    pass
class sgraph_Declaration(NamedElement):

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
                if hasattr(item, "sgraph_Scope27"):
                    opp_val = getattr(item, "sgraph_Scope27", None)
                    
                    if opp_val == self:
                        setattr(item, "sgraph_Scope27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sgraph_Scope27"):
                    opp_val = getattr(item, "sgraph_Scope27", None)
                    
                    setattr(item, "sgraph_Scope27", self)
                    

class sgraph_Reaction(ABC):

    pass
class sgraph_ReactiveElement(ABC):

    pass
class sgraph_ReactionProperty:

    pass
class sgraph_Effect(ABC):

    pass
class sgraph_Trigger(ABC):

    pass
class Declaration:

    pass
class sgraph_Event(Declaration):

    pass
class sgraph_ImportDeclaration(Declaration):

    pass
class sgraph_Variable(Declaration):

    pass
class RegularState:

    pass
class sgraph_FinalState(RegularState):

    pass
class sgraph_Import:

    def __init__(self, importedNamespace: str, sgraph_Import: "sgraph_Statechart" = None):
        self.importedNamespace = importedNamespace
        self.sgraph_Import = sgraph_Import
        
        pass
    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


    @property
    def sgraph_Import(self):
        return self.__sgraph_Import

    @sgraph_Import.setter
    def sgraph_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sgraph_Import__sgraph_Import", None)
        self.__sgraph_Import = value
        
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

class CompositeElement:

    pass
class ScopedElement:

    pass
class ReactiveElement:

    pass
class Pseudostate:

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


class sgraph_Synchronization(Pseudostate):

    pass
class DocumentedElement:

    pass
class sgraph_State(RegularState, CompositeElement, ScopedElement, ReactiveElement, SpecificationElement, DocumentedElement):

    def __init__(self, subchart: bool, simple: bool, composite: bool, leaf: bool, orthogonal: bool, substatechartId: str, sgraph_State: "sgraph_Statechart" = None):
        self.subchart = subchart
        self.simple = simple
        self.composite = composite
        self.leaf = leaf
        self.orthogonal = orthogonal
        self.substatechartId = substatechartId
        self.sgraph_State = sgraph_State
        
        pass
    @property
    def composite(self):
        return self.__composite

    @composite.setter
    def composite(self, composite: bool):
        self.__composite = composite


    @property
    def leaf(self):
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf


    @property
    def subchart(self):
        return self.__subchart

    @subchart.setter
    def subchart(self, subchart: bool):
        self.__subchart = subchart


    @property
    def simple(self):
        return self.__simple

    @simple.setter
    def simple(self, simple: bool):
        self.__simple = simple


    @property
    def orthogonal(self):
        return self.__orthogonal

    @orthogonal.setter
    def orthogonal(self, orthogonal: bool):
        self.__orthogonal = orthogonal


    @property
    def substatechartId(self):
        return self.__substatechartId

    @substatechartId.setter
    def substatechartId(self, substatechartId: str):
        self.__substatechartId = substatechartId


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
            if hasattr(old_value, "sgraph_Statechart29"):
                opp_val = getattr(old_value, "sgraph_Statechart29", None)
                if opp_val == self:
                    setattr(old_value, "sgraph_Statechart29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sgraph_Statechart29"):
                opp_val = getattr(value, "sgraph_Statechart29", None)
                setattr(value, "sgraph_Statechart29", self)

class sgraph_Statechart(CompositeElement, NamedElement, ScopedElement, ReactiveElement, SpecificationElement, DocumentedElement):

    pass
class Reaction:

    pass
class sgraph_Transition(SpecificationElement, DocumentedElement, Reaction):

    pass
class sgraph_Pseudostate(Vertex):

    pass