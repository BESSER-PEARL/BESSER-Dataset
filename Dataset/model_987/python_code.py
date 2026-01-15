from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Model(Enum):
    middle = "middle"
    input = "input"
    output = "output"
class DependencyDirection(Enum):
    input = "input"
    output = "output"


############################################
# Definition of Classes
############################################

class qVTcDataDependencyGraph_Graph:

    def __init__(self, name: str, Graph: "qVTcDataDependencyGraph_Element" = None, graph: set["qVTcDataDependencyGraph_Element"] = None):
        self.name = name
        self.Graph = Graph
        self.graph = graph if graph is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

class qVTcDataDependencyGraph_Element(ABC):

    pass
class Element:

    pass
class qVTcDataDependencyGraph_Node(Element):

    def __init__(self, label: str, target: set["qVTcDataDependencyGraph_Edge"] = None, source: set["qVTcDataDependencyGraph_Edge"] = None, qVTcDataDependencyGraph_Node: "qVTcDataDependencyGraph_EObject" = None, Node: "qVTcDataDependencyGraph_Edge" = None, Node6: "qVTcDataDependencyGraph_Edge" = None):
        self.label = label
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.qVTcDataDependencyGraph_Node = qVTcDataDependencyGraph_Node
        self.Node = Node
        self.Node6 = Node6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Node__Node", None)
        self.__Node = value
        
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
    def qVTcDataDependencyGraph_Node(self):
        return self.__qVTcDataDependencyGraph_Node

    @qVTcDataDependencyGraph_Node.setter
    def qVTcDataDependencyGraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Node__qVTcDataDependencyGraph_Node", None)
        self.__qVTcDataDependencyGraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qVTcDataDependencyGraph_EObject15"):
                opp_val = getattr(old_value, "qVTcDataDependencyGraph_EObject15", None)
                if opp_val == self:
                    setattr(old_value, "qVTcDataDependencyGraph_EObject15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qVTcDataDependencyGraph_EObject15"):
                opp_val = getattr(value, "qVTcDataDependencyGraph_EObject15", None)
                setattr(value, "qVTcDataDependencyGraph_EObject15", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge13"):
                    opp_val = getattr(item, "Edge13", None)
                    
                    setattr(item, "Edge13", self)
                    

    @property
    def Node6(self):
        return self.__Node6

    @Node6.setter
    def Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qVTcDataDependencyGraph_Node__Node6", None)
        self.__Node6 = value
        
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

class qVTcDataDependencyGraph_Edge(Element):

    pass
class Edge:

    pass
class qVTcDataDependencyGraph_DependencyEdge(Edge):

    def __init__(self, derived: bool, multiple: bool, direction: str):
        self.derived = derived
        self.multiple = multiple
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

class qVTcDataDependencyGraph_ContainmentEdge(Edge):

    def __init__(self, model: str):
        self.model = model
        
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

class qVTcDataDependencyGraph_ReferenceEdge(Edge):

    pass
class qVTcDataDependencyGraph_EObject:

    pass
class Node:

    pass
class qVTcDataDependencyGraph_DataTypeNode(Node):

    pass
class qVTcDataDependencyGraph_MappingNode(Node):

    pass
class qVTcDataDependencyGraph_ClassNode(Node):

    def __init__(self, model: str, superTypes: str):
        self.model = model
        self.superTypes = superTypes
        
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def superTypes(self) -> str:
        return self.__superTypes

    @superTypes.setter
    def superTypes(self, superTypes: str):
        self.__superTypes = superTypes
