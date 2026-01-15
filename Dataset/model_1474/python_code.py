from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class GraphElement:

    pass
class Graph_DirectedArc(GraphElement):

    def __init__(self, weight: int, Graph_DirectedArc: "Graph_Node" = None, Graph_DirectedArc4: "Graph_Node" = None):
        self.weight = weight
        self.Graph_DirectedArc = Graph_DirectedArc
        self.Graph_DirectedArc4 = Graph_DirectedArc4
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def Graph_DirectedArc(self):
        return self.__Graph_DirectedArc

    @Graph_DirectedArc.setter
    def Graph_DirectedArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_DirectedArc__Graph_DirectedArc", None)
        self.__Graph_DirectedArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Node"):
                opp_val = getattr(old_value, "Graph_Node", None)
                if opp_val == self:
                    setattr(old_value, "Graph_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Node"):
                opp_val = getattr(value, "Graph_Node", None)
                setattr(value, "Graph_Node", self)

    @property
    def Graph_DirectedArc4(self):
        return self.__Graph_DirectedArc4

    @Graph_DirectedArc4.setter
    def Graph_DirectedArc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_DirectedArc__Graph_DirectedArc4", None)
        self.__Graph_DirectedArc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Node5"):
                opp_val = getattr(old_value, "Graph_Node5", None)
                if opp_val == self:
                    setattr(old_value, "Graph_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Node5"):
                opp_val = getattr(value, "Graph_Node5", None)
                setattr(value, "Graph_Node5", self)

class Graph_Node(GraphElement):

    def __init__(self, shape: str, style: str, Graph_Node: "Graph_DirectedArc" = None, Graph_Node5: "Graph_DirectedArc" = None):
        self.shape = shape
        self.style = style
        self.Graph_Node = Graph_Node
        self.Graph_Node5 = Graph_Node5
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def Graph_Node(self):
        return self.__Graph_Node

    @Graph_Node.setter
    def Graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Graph_Node", None)
        self.__Graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_DirectedArc"):
                opp_val = getattr(old_value, "Graph_DirectedArc", None)
                if opp_val == self:
                    setattr(old_value, "Graph_DirectedArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_DirectedArc"):
                opp_val = getattr(value, "Graph_DirectedArc", None)
                setattr(value, "Graph_DirectedArc", self)

    @property
    def Graph_Node5(self):
        return self.__Graph_Node5

    @Graph_Node5.setter
    def Graph_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Graph_Node5", None)
        self.__Graph_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_DirectedArc4"):
                opp_val = getattr(old_value, "Graph_DirectedArc4", None)
                if opp_val == self:
                    setattr(old_value, "Graph_DirectedArc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_DirectedArc4"):
                opp_val = getattr(value, "Graph_DirectedArc4", None)
                setattr(value, "Graph_DirectedArc4", self)

class Graph_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class Graph_GraphElement(NamedElement):

    def __init__(self, label: str, color: str, GraphElement: "Graph_Graph" = None, contents: "Graph_Graph" = None):
        self.label = label
        self.color = color
        self.GraphElement = GraphElement
        self.contents = contents
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_GraphElement__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def GraphElement(self):
        return self.__GraphElement

    @GraphElement.setter
    def GraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_GraphElement__GraphElement", None)
        self.__GraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_Graph(NamedElement):

    pass