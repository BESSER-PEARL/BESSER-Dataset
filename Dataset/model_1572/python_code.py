from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ScaffoldGraph_Edge:

    def __init__(self, weight: int, Edge: "ScaffoldGraph_Vertex" = None, Edge5: "ScaffoldGraph_Vertex" = None, VEin: "ScaffoldGraph_Vertex" = None, VEout: "ScaffoldGraph_Vertex" = None, ScaffoldGraph_Edge: "ScaffoldGraph_Graph" = None):
        self.weight = weight
        self.Edge = Edge
        self.Edge5 = Edge5
        self.VEin = VEin
        self.VEout = VEout
        self.ScaffoldGraph_Edge = ScaffoldGraph_Edge
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EVin"):
                opp_val = getattr(old_value, "EVin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EVin"):
                opp_val = getattr(value, "EVin", None)
                if opp_val is None:
                    setattr(value, "EVin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VEout(self):
        return self.__VEout

    @VEout.setter
    def VEout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Edge__VEout", None)
        self.__VEout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex8"):
                opp_val = getattr(old_value, "Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex8"):
                opp_val = getattr(value, "Vertex8", None)
                setattr(value, "Vertex8", self)

    @property
    def VEin(self):
        return self.__VEin

    @VEin.setter
    def VEin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Edge__VEin", None)
        self.__VEin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex"):
                opp_val = getattr(old_value, "Vertex", None)
                if opp_val == self:
                    setattr(old_value, "Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex"):
                opp_val = getattr(value, "Vertex", None)
                setattr(value, "Vertex", self)

    @property
    def Edge5(self):
        return self.__Edge5

    @Edge5.setter
    def Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Edge__Edge5", None)
        self.__Edge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EVout"):
                opp_val = getattr(old_value, "EVout", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EVout"):
                opp_val = getattr(value, "EVout", None)
                if opp_val is None:
                    setattr(value, "EVout", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ScaffoldGraph_Edge(self):
        return self.__ScaffoldGraph_Edge

    @ScaffoldGraph_Edge.setter
    def ScaffoldGraph_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Edge__ScaffoldGraph_Edge", None)
        self.__ScaffoldGraph_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScaffoldGraph_Graph2"):
                opp_val = getattr(old_value, "ScaffoldGraph_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScaffoldGraph_Graph2"):
                opp_val = getattr(value, "ScaffoldGraph_Graph2", None)
                if opp_val is None:
                    setattr(value, "ScaffoldGraph_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ScaffoldGraph_Vertex:

    pass
class ScaffoldGraph_Graph:

    def __init__(self, name: str, ScaffoldGraph_Graph: set["ScaffoldGraph_Vertex"] = None, ScaffoldGraph_Graph2: set["ScaffoldGraph_Edge"] = None):
        self.name = name
        self.ScaffoldGraph_Graph = ScaffoldGraph_Graph if ScaffoldGraph_Graph is not None else set()
        self.ScaffoldGraph_Graph2 = ScaffoldGraph_Graph2 if ScaffoldGraph_Graph2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ScaffoldGraph_Graph(self):
        return self.__ScaffoldGraph_Graph

    @ScaffoldGraph_Graph.setter
    def ScaffoldGraph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Graph__ScaffoldGraph_Graph", None)
        self.__ScaffoldGraph_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScaffoldGraph_Vertex"):
                    opp_val = getattr(item, "ScaffoldGraph_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "ScaffoldGraph_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScaffoldGraph_Vertex"):
                    opp_val = getattr(item, "ScaffoldGraph_Vertex", None)
                    
                    setattr(item, "ScaffoldGraph_Vertex", self)
                    

    @property
    def ScaffoldGraph_Graph2(self):
        return self.__ScaffoldGraph_Graph2

    @ScaffoldGraph_Graph2.setter
    def ScaffoldGraph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScaffoldGraph_Graph__ScaffoldGraph_Graph2", None)
        self.__ScaffoldGraph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScaffoldGraph_Edge"):
                    opp_val = getattr(item, "ScaffoldGraph_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "ScaffoldGraph_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScaffoldGraph_Edge"):
                    opp_val = getattr(item, "ScaffoldGraph_Edge", None)
                    
                    setattr(item, "ScaffoldGraph_Edge", self)
                    
