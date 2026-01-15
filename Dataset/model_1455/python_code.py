from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class grapheditormodel_Edge:

    def __init__(self, Value: str, grapheditormodel_Edge: "grapheditormodel_Node" = None, grapheditormodel_Edge11: "grapheditormodel_Node" = None, grapheditormodel_Edge13: "grapheditormodel_Node" = None, grapheditormodel_Edge16: "grapheditormodel_Node" = None):
        self.Value = Value
        self.grapheditormodel_Edge = grapheditormodel_Edge
        self.grapheditormodel_Edge11 = grapheditormodel_Edge11
        self.grapheditormodel_Edge13 = grapheditormodel_Edge13
        self.grapheditormodel_Edge16 = grapheditormodel_Edge16
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def grapheditormodel_Edge13(self):
        return self.__grapheditormodel_Edge13

    @grapheditormodel_Edge13.setter
    def grapheditormodel_Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Edge__grapheditormodel_Edge13", None)
        self.__grapheditormodel_Edge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Node14"):
                opp_val = getattr(old_value, "grapheditormodel_Node14", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Node14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Node14"):
                opp_val = getattr(value, "grapheditormodel_Node14", None)
                setattr(value, "grapheditormodel_Node14", self)

    @property
    def grapheditormodel_Edge(self):
        return self.__grapheditormodel_Edge

    @grapheditormodel_Edge.setter
    def grapheditormodel_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Edge__grapheditormodel_Edge", None)
        self.__grapheditormodel_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Node8"):
                opp_val = getattr(old_value, "grapheditormodel_Node8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Node8"):
                opp_val = getattr(value, "grapheditormodel_Node8", None)
                if opp_val is None:
                    setattr(value, "grapheditormodel_Node8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grapheditormodel_Edge16(self):
        return self.__grapheditormodel_Edge16

    @grapheditormodel_Edge16.setter
    def grapheditormodel_Edge16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Edge__grapheditormodel_Edge16", None)
        self.__grapheditormodel_Edge16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Node17"):
                opp_val = getattr(old_value, "grapheditormodel_Node17", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Node17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Node17"):
                opp_val = getattr(value, "grapheditormodel_Node17", None)
                setattr(value, "grapheditormodel_Node17", self)

    @property
    def grapheditormodel_Edge11(self):
        return self.__grapheditormodel_Edge11

    @grapheditormodel_Edge11.setter
    def grapheditormodel_Edge11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Edge__grapheditormodel_Edge11", None)
        self.__grapheditormodel_Edge11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Node10"):
                opp_val = getattr(old_value, "grapheditormodel_Node10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Node10"):
                opp_val = getattr(value, "grapheditormodel_Node10", None)
                if opp_val is None:
                    setattr(value, "grapheditormodel_Node10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class grapheditormodel_Node:

    def __init__(self, Name: str, grapheditormodel_Node: "grapheditormodel_Graph" = None, grapheditormodel_Node3: "grapheditormodel_Graph" = None, grapheditormodel_Node6: "grapheditormodel_Graph" = None, grapheditormodel_Node8: set["grapheditormodel_Edge"] = None, grapheditormodel_Node10: set["grapheditormodel_Edge"] = None, grapheditormodel_Node14: "grapheditormodel_Edge" = None, grapheditormodel_Node17: "grapheditormodel_Edge" = None):
        self.Name = Name
        self.grapheditormodel_Node = grapheditormodel_Node
        self.grapheditormodel_Node3 = grapheditormodel_Node3
        self.grapheditormodel_Node6 = grapheditormodel_Node6
        self.grapheditormodel_Node8 = grapheditormodel_Node8 if grapheditormodel_Node8 is not None else set()
        self.grapheditormodel_Node10 = grapheditormodel_Node10 if grapheditormodel_Node10 is not None else set()
        self.grapheditormodel_Node14 = grapheditormodel_Node14
        self.grapheditormodel_Node17 = grapheditormodel_Node17
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def grapheditormodel_Node(self):
        return self.__grapheditormodel_Node

    @grapheditormodel_Node.setter
    def grapheditormodel_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node", None)
        self.__grapheditormodel_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Graph"):
                opp_val = getattr(old_value, "grapheditormodel_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Graph"):
                opp_val = getattr(value, "grapheditormodel_Graph", None)
                if opp_val is None:
                    setattr(value, "grapheditormodel_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def grapheditormodel_Node10(self):
        return self.__grapheditormodel_Node10

    @grapheditormodel_Node10.setter
    def grapheditormodel_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node10", None)
        self.__grapheditormodel_Node10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "grapheditormodel_Edge11"):
                    opp_val = getattr(item, "grapheditormodel_Edge11", None)
                    
                    if opp_val == self:
                        setattr(item, "grapheditormodel_Edge11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "grapheditormodel_Edge11"):
                    opp_val = getattr(item, "grapheditormodel_Edge11", None)
                    
                    setattr(item, "grapheditormodel_Edge11", self)
                    

    @property
    def grapheditormodel_Node14(self):
        return self.__grapheditormodel_Node14

    @grapheditormodel_Node14.setter
    def grapheditormodel_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node14", None)
        self.__grapheditormodel_Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Edge13"):
                opp_val = getattr(old_value, "grapheditormodel_Edge13", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Edge13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Edge13"):
                opp_val = getattr(value, "grapheditormodel_Edge13", None)
                setattr(value, "grapheditormodel_Edge13", self)

    @property
    def grapheditormodel_Node6(self):
        return self.__grapheditormodel_Node6

    @grapheditormodel_Node6.setter
    def grapheditormodel_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node6", None)
        self.__grapheditormodel_Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Graph5"):
                opp_val = getattr(old_value, "grapheditormodel_Graph5", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Graph5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Graph5"):
                opp_val = getattr(value, "grapheditormodel_Graph5", None)
                setattr(value, "grapheditormodel_Graph5", self)

    @property
    def grapheditormodel_Node8(self):
        return self.__grapheditormodel_Node8

    @grapheditormodel_Node8.setter
    def grapheditormodel_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node8", None)
        self.__grapheditormodel_Node8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "grapheditormodel_Edge"):
                    opp_val = getattr(item, "grapheditormodel_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "grapheditormodel_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "grapheditormodel_Edge"):
                    opp_val = getattr(item, "grapheditormodel_Edge", None)
                    
                    setattr(item, "grapheditormodel_Edge", self)
                    

    @property
    def grapheditormodel_Node3(self):
        return self.__grapheditormodel_Node3

    @grapheditormodel_Node3.setter
    def grapheditormodel_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node3", None)
        self.__grapheditormodel_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Graph2"):
                opp_val = getattr(old_value, "grapheditormodel_Graph2", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Graph2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Graph2"):
                opp_val = getattr(value, "grapheditormodel_Graph2", None)
                setattr(value, "grapheditormodel_Graph2", self)

    @property
    def grapheditormodel_Node17(self):
        return self.__grapheditormodel_Node17

    @grapheditormodel_Node17.setter
    def grapheditormodel_Node17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_grapheditormodel_Node__grapheditormodel_Node17", None)
        self.__grapheditormodel_Node17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "grapheditormodel_Edge16"):
                opp_val = getattr(old_value, "grapheditormodel_Edge16", None)
                if opp_val == self:
                    setattr(old_value, "grapheditormodel_Edge16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "grapheditormodel_Edge16"):
                opp_val = getattr(value, "grapheditormodel_Edge16", None)
                setattr(value, "grapheditormodel_Edge16", self)

class grapheditormodel_Graph:

    pass