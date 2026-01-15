from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dag_Edge:

    def __init__(self, id: str, Edge: "dag_Vertex" = None, Edge5: "dag_Vertex" = None, outgoing: "dag_Vertex" = None, incoming: "dag_Vertex" = None, dag_Edge: "dag_DAG" = None):
        self.id = id
        self.Edge = Edge
        self.Edge5 = Edge5
        self.outgoing = outgoing
        self.incoming = incoming
        self.dag_Edge = dag_Edge
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge5(self):
        return self.__Edge5

    @Edge5.setter
    def Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Edge__Edge5", None)
        self.__Edge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dag_Edge(self):
        return self.__dag_Edge

    @dag_Edge.setter
    def dag_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Edge__dag_Edge", None)
        self.__dag_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dag_DAG2"):
                opp_val = getattr(old_value, "dag_DAG2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dag_DAG2"):
                opp_val = getattr(value, "dag_DAG2", None)
                if opp_val is None:
                    setattr(value, "dag_DAG2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Edge__outgoing", None)
        self.__outgoing = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Edge__incoming", None)
        self.__incoming = value
        
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

class dag_Vertex:

    def __init__(self, id: str, from: set["dag_Edge"] = None, to: set["dag_Edge"] = None, Vertex: "dag_Edge" = None, Vertex8: "dag_Edge" = None, dag_Vertex: "dag_DAG" = None):
        self.id = id
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.Vertex = Vertex
        self.Vertex8 = Vertex8
        self.dag_Vertex = dag_Vertex
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Vertex8(self):
        return self.__Vertex8

    @Vertex8.setter
    def Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Vertex__Vertex8", None)
        self.__Vertex8 = value
        
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Vertex__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    setattr(item, "Edge5", self)
                    

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Vertex__Vertex", None)
        self.__Vertex = value
        
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

    @property
    def dag_Vertex(self):
        return self.__dag_Vertex

    @dag_Vertex.setter
    def dag_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Vertex__dag_Vertex", None)
        self.__dag_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dag_DAG"):
                opp_val = getattr(old_value, "dag_DAG", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dag_DAG"):
                opp_val = getattr(value, "dag_DAG", None)
                if opp_val is None:
                    setattr(value, "dag_DAG", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dag_Vertex__from", None)
        self.__from = value if value is not None else set()
        
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
                    

class dag_DAG:

    pass