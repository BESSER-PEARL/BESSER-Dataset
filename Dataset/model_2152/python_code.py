from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class jgrapht_Graph:

    pass
class jgrapht_Vertex:

    def __init__(self, name: str, jgrapht_Vertex: "jgrapht_Graph" = None, jgrapht_Vertex5: "jgrapht_Edge" = None, jgrapht_Vertex8: "jgrapht_Edge" = None):
        self.name = name
        self.jgrapht_Vertex = jgrapht_Vertex
        self.jgrapht_Vertex5 = jgrapht_Vertex5
        self.jgrapht_Vertex8 = jgrapht_Vertex8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jgrapht_Vertex5(self):
        return self.__jgrapht_Vertex5

    @jgrapht_Vertex5.setter
    def jgrapht_Vertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Vertex__jgrapht_Vertex5", None)
        self.__jgrapht_Vertex5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Edge4"):
                opp_val = getattr(old_value, "jgrapht_Edge4", None)
                if opp_val == self:
                    setattr(old_value, "jgrapht_Edge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Edge4"):
                opp_val = getattr(value, "jgrapht_Edge4", None)
                setattr(value, "jgrapht_Edge4", self)

    @property
    def jgrapht_Vertex8(self):
        return self.__jgrapht_Vertex8

    @jgrapht_Vertex8.setter
    def jgrapht_Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Vertex__jgrapht_Vertex8", None)
        self.__jgrapht_Vertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Edge7"):
                opp_val = getattr(old_value, "jgrapht_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "jgrapht_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Edge7"):
                opp_val = getattr(value, "jgrapht_Edge7", None)
                setattr(value, "jgrapht_Edge7", self)

    @property
    def jgrapht_Vertex(self):
        return self.__jgrapht_Vertex

    @jgrapht_Vertex.setter
    def jgrapht_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Vertex__jgrapht_Vertex", None)
        self.__jgrapht_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Graph2"):
                opp_val = getattr(old_value, "jgrapht_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Graph2"):
                opp_val = getattr(value, "jgrapht_Graph2", None)
                if opp_val is None:
                    setattr(value, "jgrapht_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jgrapht_Edge:

    def __init__(self, relation: str, jgrapht_Edge: "jgrapht_Graph" = None, jgrapht_Edge4: "jgrapht_Vertex" = None, jgrapht_Edge7: "jgrapht_Vertex" = None):
        self.relation = relation
        self.jgrapht_Edge = jgrapht_Edge
        self.jgrapht_Edge4 = jgrapht_Edge4
        self.jgrapht_Edge7 = jgrapht_Edge7
        
    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def jgrapht_Edge4(self):
        return self.__jgrapht_Edge4

    @jgrapht_Edge4.setter
    def jgrapht_Edge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Edge__jgrapht_Edge4", None)
        self.__jgrapht_Edge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Vertex5"):
                opp_val = getattr(old_value, "jgrapht_Vertex5", None)
                if opp_val == self:
                    setattr(old_value, "jgrapht_Vertex5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Vertex5"):
                opp_val = getattr(value, "jgrapht_Vertex5", None)
                setattr(value, "jgrapht_Vertex5", self)

    @property
    def jgrapht_Edge(self):
        return self.__jgrapht_Edge

    @jgrapht_Edge.setter
    def jgrapht_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Edge__jgrapht_Edge", None)
        self.__jgrapht_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Graph"):
                opp_val = getattr(old_value, "jgrapht_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Graph"):
                opp_val = getattr(value, "jgrapht_Graph", None)
                if opp_val is None:
                    setattr(value, "jgrapht_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jgrapht_Edge7(self):
        return self.__jgrapht_Edge7

    @jgrapht_Edge7.setter
    def jgrapht_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jgrapht_Edge__jgrapht_Edge7", None)
        self.__jgrapht_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jgrapht_Vertex8"):
                opp_val = getattr(old_value, "jgrapht_Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "jgrapht_Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jgrapht_Vertex8"):
                opp_val = getattr(value, "jgrapht_Vertex8", None)
                setattr(value, "jgrapht_Vertex8", self)
