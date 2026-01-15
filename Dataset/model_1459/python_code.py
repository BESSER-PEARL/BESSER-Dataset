from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graphs_Node:

    def __init__(self, name: str, graphs_Node: "graphs_Graph" = None, graphs_Node7: "graphs_Edge" = None, graphs_Node10: "graphs_Edge" = None, graphs_Node13: "graphs_Edge" = None):
        self.name = name
        self.graphs_Node = graphs_Node
        self.graphs_Node7 = graphs_Node7
        self.graphs_Node10 = graphs_Node10
        self.graphs_Node13 = graphs_Node13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphs_Node10(self):
        return self.__graphs_Node10

    @graphs_Node10.setter
    def graphs_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Node__graphs_Node10", None)
        self.__graphs_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Edge9"):
                opp_val = getattr(old_value, "graphs_Edge9", None)
                if opp_val == self:
                    setattr(old_value, "graphs_Edge9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Edge9"):
                opp_val = getattr(value, "graphs_Edge9", None)
                setattr(value, "graphs_Edge9", self)

    @property
    def graphs_Node(self):
        return self.__graphs_Node

    @graphs_Node.setter
    def graphs_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Node__graphs_Node", None)
        self.__graphs_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Graph"):
                opp_val = getattr(old_value, "graphs_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Graph"):
                opp_val = getattr(value, "graphs_Graph", None)
                if opp_val is None:
                    setattr(value, "graphs_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphs_Node7(self):
        return self.__graphs_Node7

    @graphs_Node7.setter
    def graphs_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Node__graphs_Node7", None)
        self.__graphs_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Edge6"):
                opp_val = getattr(old_value, "graphs_Edge6", None)
                if opp_val == self:
                    setattr(old_value, "graphs_Edge6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Edge6"):
                opp_val = getattr(value, "graphs_Edge6", None)
                setattr(value, "graphs_Edge6", self)

    @property
    def graphs_Node13(self):
        return self.__graphs_Node13

    @graphs_Node13.setter
    def graphs_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Node__graphs_Node13", None)
        self.__graphs_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Edge12"):
                opp_val = getattr(old_value, "graphs_Edge12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Edge12"):
                opp_val = getattr(value, "graphs_Edge12", None)
                if opp_val is None:
                    setattr(value, "graphs_Edge12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def outputs(self) -> str:
        # TODO: Implement outputs method
        pass

    def inputs(self) -> str:
        # TODO: Implement inputs method
        pass

class graphs_Graph:

    pass
class Node:

    pass
class graphs_CompositeNode(Node):

    pass
class graphs_Edge:

    def __init__(self, weight: int, graphs_Edge: "graphs_Graph" = None, graphs_Edge12: set["graphs_Node"] = None, graphs_Edge6: "graphs_Node" = None, graphs_Edge9: "graphs_Node" = None):
        self.weight = weight
        self.graphs_Edge = graphs_Edge
        self.graphs_Edge12 = graphs_Edge12 if graphs_Edge12 is not None else set()
        self.graphs_Edge6 = graphs_Edge6
        self.graphs_Edge9 = graphs_Edge9
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def graphs_Edge12(self):
        return self.__graphs_Edge12

    @graphs_Edge12.setter
    def graphs_Edge12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Edge__graphs_Edge12", None)
        self.__graphs_Edge12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphs_Node13"):
                    opp_val = getattr(item, "graphs_Node13", None)
                    
                    if opp_val == self:
                        setattr(item, "graphs_Node13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphs_Node13"):
                    opp_val = getattr(item, "graphs_Node13", None)
                    
                    setattr(item, "graphs_Node13", self)
                    

    @property
    def graphs_Edge(self):
        return self.__graphs_Edge

    @graphs_Edge.setter
    def graphs_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Edge__graphs_Edge", None)
        self.__graphs_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Graph2"):
                opp_val = getattr(old_value, "graphs_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Graph2"):
                opp_val = getattr(value, "graphs_Graph2", None)
                if opp_val is None:
                    setattr(value, "graphs_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphs_Edge6(self):
        return self.__graphs_Edge6

    @graphs_Edge6.setter
    def graphs_Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Edge__graphs_Edge6", None)
        self.__graphs_Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Node7"):
                opp_val = getattr(old_value, "graphs_Node7", None)
                if opp_val == self:
                    setattr(old_value, "graphs_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Node7"):
                opp_val = getattr(value, "graphs_Node7", None)
                setattr(value, "graphs_Node7", self)

    @property
    def graphs_Edge9(self):
        return self.__graphs_Edge9

    @graphs_Edge9.setter
    def graphs_Edge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphs_Edge__graphs_Edge9", None)
        self.__graphs_Edge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphs_Node10"):
                opp_val = getattr(old_value, "graphs_Node10", None)
                if opp_val == self:
                    setattr(old_value, "graphs_Node10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphs_Node10"):
                opp_val = getattr(value, "graphs_Node10", None)
                setattr(value, "graphs_Node10", self)
