from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class grapho_GraphElement(ABC):

    def __init__(self, name: str, grapho_GraphElement: "grapho_GraphO" = None):
        self.name = name
        self.grapho_GraphElement = grapho_GraphElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def grapho_GraphElement(self):
        return self.__grapho_GraphElement

    @grapho_GraphElement.setter
    def grapho_GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapho_GraphElement__grapho_GraphElement", None)
        self.__grapho_GraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapho_GraphO"):
                opp_val = getattr(old_value, "grapho_GraphO", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapho_GraphO"):
                opp_val = getattr(value, "grapho_GraphO", None)
                if opp_val is None:
                    setattr(value, "grapho_GraphO", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphElement:

    pass
class grapho_Node(GraphElement):

    def __init__(self, style: str, color: str, shape: str, label: str, grapho_Node: "grapho_Edge" = None, grapho_Node4: "grapho_Edge" = None):
        self.style = style
        self.color = color
        self.shape = shape
        self.label = label
        self.grapho_Node = grapho_Node
        self.grapho_Node4 = grapho_Node4
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def grapho_Node4(self):
        return self.__grapho_Node4

    @grapho_Node4.setter
    def grapho_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapho_Node__grapho_Node4", None)
        self.__grapho_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapho_Edge3"):
                opp_val = getattr(old_value, "grapho_Edge3", None)
                if opp_val == self:
                    setattr(old_value, "grapho_Edge3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapho_Edge3"):
                opp_val = getattr(value, "grapho_Edge3", None)
                setattr(value, "grapho_Edge3", self)

    @property
    def grapho_Node(self):
        return self.__grapho_Node

    @grapho_Node.setter
    def grapho_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapho_Node__grapho_Node", None)
        self.__grapho_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapho_Edge"):
                opp_val = getattr(old_value, "grapho_Edge", None)
                if opp_val == self:
                    setattr(old_value, "grapho_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapho_Edge"):
                opp_val = getattr(value, "grapho_Edge", None)
                setattr(value, "grapho_Edge", self)

class grapho_Edge(GraphElement):

    def __init__(self, color: str, style: str, constraintRank: bool, grapho_Edge: "grapho_Node" = None, grapho_Edge3: "grapho_Node" = None):
        self.color = color
        self.style = style
        self.constraintRank = constraintRank
        self.grapho_Edge = grapho_Edge
        self.grapho_Edge3 = grapho_Edge3
        
    @property
    def constraintRank(self) -> bool:
        return self.__constraintRank

    @constraintRank.setter
    def constraintRank(self, constraintRank: bool):
        self.__constraintRank = constraintRank

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def grapho_Edge(self):
        return self.__grapho_Edge

    @grapho_Edge.setter
    def grapho_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapho_Edge__grapho_Edge", None)
        self.__grapho_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapho_Node"):
                opp_val = getattr(old_value, "grapho_Node", None)
                if opp_val == self:
                    setattr(old_value, "grapho_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapho_Node"):
                opp_val = getattr(value, "grapho_Node", None)
                setattr(value, "grapho_Node", self)

    @property
    def grapho_Edge3(self):
        return self.__grapho_Edge3

    @grapho_Edge3.setter
    def grapho_Edge3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapho_Edge__grapho_Edge3", None)
        self.__grapho_Edge3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapho_Node4"):
                opp_val = getattr(old_value, "grapho_Node4", None)
                if opp_val == self:
                    setattr(old_value, "grapho_Node4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapho_Node4"):
                opp_val = getattr(value, "grapho_Node4", None)
                setattr(value, "grapho_Node4", self)

class grapho_GraphO(GraphElement):

    pass