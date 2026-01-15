from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simplegraph2graph_Node:

    pass
class simplegraph2graph_Edge:

    pass
class Element2Element:

    pass
class simplegraph2graph_Node2Node(Element2Element):

    def __init__(self, label: str, simplegraph2graph_Node2Node: "simplegraph2graph_Edge2Edge" = None, simplegraph2graph_Node2Node14: "simplegraph2graph_Edge2Edge" = None, simplegraph2graph_Node2Node16: "simplegraph2graph_Node" = None, simplegraph2graph_Node2Node18: "simplegraph2graph_Node" = None):
        self.label = label
        self.simplegraph2graph_Node2Node = simplegraph2graph_Node2Node
        self.simplegraph2graph_Node2Node14 = simplegraph2graph_Node2Node14
        self.simplegraph2graph_Node2Node16 = simplegraph2graph_Node2Node16
        self.simplegraph2graph_Node2Node18 = simplegraph2graph_Node2Node18
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def simplegraph2graph_Node2Node18(self):
        return self.__simplegraph2graph_Node2Node18

    @simplegraph2graph_Node2Node18.setter
    def simplegraph2graph_Node2Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Node2Node__simplegraph2graph_Node2Node18", None)
        self.__simplegraph2graph_Node2Node18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Node19"):
                opp_val = getattr(old_value, "simplegraph2graph_Node19", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Node19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Node19"):
                opp_val = getattr(value, "simplegraph2graph_Node19", None)
                setattr(value, "simplegraph2graph_Node19", self)

    @property
    def simplegraph2graph_Node2Node16(self):
        return self.__simplegraph2graph_Node2Node16

    @simplegraph2graph_Node2Node16.setter
    def simplegraph2graph_Node2Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Node2Node__simplegraph2graph_Node2Node16", None)
        self.__simplegraph2graph_Node2Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Node"):
                opp_val = getattr(old_value, "simplegraph2graph_Node", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Node"):
                opp_val = getattr(value, "simplegraph2graph_Node", None)
                setattr(value, "simplegraph2graph_Node", self)

    @property
    def simplegraph2graph_Node2Node(self):
        return self.__simplegraph2graph_Node2Node

    @simplegraph2graph_Node2Node.setter
    def simplegraph2graph_Node2Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Node2Node__simplegraph2graph_Node2Node", None)
        self.__simplegraph2graph_Node2Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Edge2Edge11"):
                opp_val = getattr(old_value, "simplegraph2graph_Edge2Edge11", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Edge2Edge11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Edge2Edge11"):
                opp_val = getattr(value, "simplegraph2graph_Edge2Edge11", None)
                setattr(value, "simplegraph2graph_Edge2Edge11", self)

    @property
    def simplegraph2graph_Node2Node14(self):
        return self.__simplegraph2graph_Node2Node14

    @simplegraph2graph_Node2Node14.setter
    def simplegraph2graph_Node2Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Node2Node__simplegraph2graph_Node2Node14", None)
        self.__simplegraph2graph_Node2Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Edge2Edge13"):
                opp_val = getattr(old_value, "simplegraph2graph_Edge2Edge13", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Edge2Edge13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Edge2Edge13"):
                opp_val = getattr(value, "simplegraph2graph_Edge2Edge13", None)
                setattr(value, "simplegraph2graph_Edge2Edge13", self)

class simplegraph2graph_Edge2Edge(Element2Element):

    pass
class simplegraph2graph_Element2Element(ABC):

    pass
class simplegraph2graph_Graph:

    pass
class simplegraph2graph_Graph2Graph:

    def __init__(self, name: str, simplegraph2graph_Graph2Graph: "simplegraph2graph_Graph" = None, simplegraph2graph_Graph2Graph2: "simplegraph2graph_Graph" = None, owner: set["simplegraph2graph_Element2Element"] = None, Graph2Graph: "simplegraph2graph_Element2Element" = None):
        self.name = name
        self.simplegraph2graph_Graph2Graph = simplegraph2graph_Graph2Graph
        self.simplegraph2graph_Graph2Graph2 = simplegraph2graph_Graph2Graph2
        self.owner = owner if owner is not None else set()
        self.Graph2Graph = Graph2Graph
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Graph2Graph__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element2Element"):
                    opp_val = getattr(item, "Element2Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element2Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element2Element"):
                    opp_val = getattr(item, "Element2Element", None)
                    
                    setattr(item, "Element2Element", self)
                    

    @property
    def simplegraph2graph_Graph2Graph2(self):
        return self.__simplegraph2graph_Graph2Graph2

    @simplegraph2graph_Graph2Graph2.setter
    def simplegraph2graph_Graph2Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Graph2Graph__simplegraph2graph_Graph2Graph2", None)
        self.__simplegraph2graph_Graph2Graph2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Graph3"):
                opp_val = getattr(old_value, "simplegraph2graph_Graph3", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Graph3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Graph3"):
                opp_val = getattr(value, "simplegraph2graph_Graph3", None)
                setattr(value, "simplegraph2graph_Graph3", self)

    @property
    def simplegraph2graph_Graph2Graph(self):
        return self.__simplegraph2graph_Graph2Graph

    @simplegraph2graph_Graph2Graph.setter
    def simplegraph2graph_Graph2Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Graph2Graph__simplegraph2graph_Graph2Graph", None)
        self.__simplegraph2graph_Graph2Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph2graph_Graph"):
                opp_val = getattr(old_value, "simplegraph2graph_Graph", None)
                if opp_val == self:
                    setattr(old_value, "simplegraph2graph_Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph2graph_Graph"):
                opp_val = getattr(value, "simplegraph2graph_Graph", None)
                setattr(value, "simplegraph2graph_Graph", self)

    @property
    def Graph2Graph(self):
        return self.__Graph2Graph

    @Graph2Graph.setter
    def Graph2Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph2graph_Graph2Graph__Graph2Graph", None)
        self.__Graph2Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element2Element"):
                opp_val = getattr(old_value, "element2Element", None)
                if opp_val == self:
                    setattr(old_value, "element2Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element2Element"):
                opp_val = getattr(value, "element2Element", None)
                setattr(value, "element2Element", self)
