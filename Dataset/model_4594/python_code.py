from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dot_Attribute:

    def __init__(self, weight: int, dot_Attribute18: "dot_DirectedEdge" = None, dot_Attribute: "dot_UnDirectedEdge" = None):
        self.weight = weight
        self.dot_Attribute18 = dot_Attribute18
        self.dot_Attribute = dot_Attribute
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def dot_Attribute(self):
        return self.__dot_Attribute

    @dot_Attribute.setter
    def dot_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute", None)
        self.__dot_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_UnDirectedEdge9"):
                opp_val = getattr(old_value, "dot_UnDirectedEdge9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_UnDirectedEdge9"):
                opp_val = getattr(value, "dot_UnDirectedEdge9", None)
                if opp_val is None:
                    setattr(value, "dot_UnDirectedEdge9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dot_Attribute18(self):
        return self.__dot_Attribute18

    @dot_Attribute18.setter
    def dot_Attribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute18", None)
        self.__dot_Attribute18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_DirectedEdge17"):
                opp_val = getattr(old_value, "dot_DirectedEdge17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_DirectedEdge17"):
                opp_val = getattr(value, "dot_DirectedEdge17", None)
                if opp_val is None:
                    setattr(value, "dot_DirectedEdge17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dot_Node:

    def __init__(self, name: str, dot_Node12: "dot_DirectedEdge" = None, dot_Node15: "dot_DirectedEdge" = None, dot_Node: "dot_UnDirectedEdge" = None, dot_Node7: "dot_UnDirectedEdge" = None):
        self.name = name
        self.dot_Node12 = dot_Node12
        self.dot_Node15 = dot_Node15
        self.dot_Node = dot_Node
        self.dot_Node7 = dot_Node7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_Node7(self):
        return self.__dot_Node7

    @dot_Node7.setter
    def dot_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node7", None)
        self.__dot_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_UnDirectedEdge6"):
                opp_val = getattr(old_value, "dot_UnDirectedEdge6", None)
                if opp_val == self:
                    setattr(old_value, "dot_UnDirectedEdge6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_UnDirectedEdge6"):
                opp_val = getattr(value, "dot_UnDirectedEdge6", None)
                setattr(value, "dot_UnDirectedEdge6", self)

    @property
    def dot_Node(self):
        return self.__dot_Node

    @dot_Node.setter
    def dot_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node", None)
        self.__dot_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_UnDirectedEdge4"):
                opp_val = getattr(old_value, "dot_UnDirectedEdge4", None)
                if opp_val == self:
                    setattr(old_value, "dot_UnDirectedEdge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_UnDirectedEdge4"):
                opp_val = getattr(value, "dot_UnDirectedEdge4", None)
                setattr(value, "dot_UnDirectedEdge4", self)

    @property
    def dot_Node15(self):
        return self.__dot_Node15

    @dot_Node15.setter
    def dot_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node15", None)
        self.__dot_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_DirectedEdge14"):
                opp_val = getattr(old_value, "dot_DirectedEdge14", None)
                if opp_val == self:
                    setattr(old_value, "dot_DirectedEdge14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_DirectedEdge14"):
                opp_val = getattr(value, "dot_DirectedEdge14", None)
                setattr(value, "dot_DirectedEdge14", self)

    @property
    def dot_Node12(self):
        return self.__dot_Node12

    @dot_Node12.setter
    def dot_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Node__dot_Node12", None)
        self.__dot_Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_DirectedEdge11"):
                opp_val = getattr(old_value, "dot_DirectedEdge11", None)
                if opp_val == self:
                    setattr(old_value, "dot_DirectedEdge11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_DirectedEdge11"):
                opp_val = getattr(value, "dot_DirectedEdge11", None)
                setattr(value, "dot_DirectedEdge11", self)

class dot_DirectedEdge:

    pass
class dot_UnDirectedEdge:

    pass
class Graph:

    pass
class dot_DirectedGraph(Graph):

    pass
class dot_UndirectedGraph(Graph):

    pass
class dot_Graph:

    def __init__(self, name: str, dot_Graph: "dot_GraphModel" = None):
        self.name = name
        self.dot_Graph = dot_Graph
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dot_Graph(self):
        return self.__dot_Graph

    @dot_Graph.setter
    def dot_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Graph__dot_Graph", None)
        self.__dot_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_GraphModel"):
                opp_val = getattr(old_value, "dot_GraphModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_GraphModel"):
                opp_val = getattr(value, "dot_GraphModel", None)
                if opp_val is None:
                    setattr(value, "dot_GraphModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dot_GraphModel:

    pass