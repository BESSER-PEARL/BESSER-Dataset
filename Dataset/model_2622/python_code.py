from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class Dot_GraphElement(NamedElement):

    def __init__(self, label: str, color: str, GraphElement: "Dot_Graph" = None, contents: "Dot_Graph" = None):
        self.label = label
        self.color = color
        self.GraphElement = GraphElement
        self.contents = contents
        
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
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dot_GraphElement__contents", None)
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
        old_value = getattr(self, f"_Dot_GraphElement__GraphElement", None)
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

class Dot_Graph(NamedElement):

    pass
class Dot_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class GraphElement:

    pass
class Dot_DirectedArc(GraphElement):

    pass
class Dot_Node(GraphElement):

    def __init__(self, shape: str, style: str, Dot_Node: "Dot_DirectedArc" = None, Dot_Node5: "Dot_DirectedArc" = None):
        self.shape = shape
        self.style = style
        self.Dot_Node = Dot_Node
        self.Dot_Node5 = Dot_Node5
        
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
    def Dot_Node5(self):
        return self.__Dot_Node5

    @Dot_Node5.setter
    def Dot_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dot_Node__Dot_Node5", None)
        self.__Dot_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dot_DirectedArc4"):
                opp_val = getattr(old_value, "Dot_DirectedArc4", None)
                if opp_val == self:
                    setattr(old_value, "Dot_DirectedArc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dot_DirectedArc4"):
                opp_val = getattr(value, "Dot_DirectedArc4", None)
                setattr(value, "Dot_DirectedArc4", self)

    @property
    def Dot_Node(self):
        return self.__Dot_Node

    @Dot_Node.setter
    def Dot_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dot_Node__Dot_Node", None)
        self.__Dot_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dot_DirectedArc"):
                opp_val = getattr(old_value, "Dot_DirectedArc", None)
                if opp_val == self:
                    setattr(old_value, "Dot_DirectedArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dot_DirectedArc"):
                opp_val = getattr(value, "Dot_DirectedArc", None)
                setattr(value, "Dot_DirectedArc", self)
