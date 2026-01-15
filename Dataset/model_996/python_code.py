from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    and = "and"
    or = "or"


############################################
# Definition of Classes
############################################

class GraphMetaM_Model:

    def __init__(self, name: str, GraphMetaM_Model: set["GraphMetaM_Graph"] = None):
        self.name = name
        self.GraphMetaM_Model = GraphMetaM_Model if GraphMetaM_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GraphMetaM_Model(self):
        return self.__GraphMetaM_Model

    @GraphMetaM_Model.setter
    def GraphMetaM_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Model__GraphMetaM_Model", None)
        self.__GraphMetaM_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphMetaM_Graph10"):
                    opp_val = getattr(item, "GraphMetaM_Graph10", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphMetaM_Graph10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphMetaM_Graph10"):
                    opp_val = getattr(item, "GraphMetaM_Graph10", None)
                    
                    setattr(item, "GraphMetaM_Graph10", self)
                    

class GraphMetaM_Edge:

    def __init__(self, localPriority: int, rName: str, name: str, async: bool, incoming: "GraphMetaM_Vertex" = None, outgoing: "GraphMetaM_Vertex" = None, GraphMetaM_Edge: "GraphMetaM_Graph" = None, Edge: "GraphMetaM_Vertex" = None, Edge8: "GraphMetaM_Vertex" = None):
        self.localPriority = localPriority
        self.rName = rName
        self.name = name
        self.async = async
        self.incoming = incoming
        self.outgoing = outgoing
        self.GraphMetaM_Edge = GraphMetaM_Edge
        self.Edge = Edge
        self.Edge8 = Edge8
        
    @property
    def rName(self) -> str:
        return self.__rName

    @rName.setter
    def rName(self, rName: str):
        self.__rName = rName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def async(self) -> bool:
        return self.__async

    @async.setter
    def async(self, async: bool):
        self.__async = async

    @property
    def localPriority(self) -> int:
        return self.__localPriority

    @localPriority.setter
    def localPriority(self, localPriority: int):
        self.__localPriority = localPriority

    @property
    def GraphMetaM_Edge(self):
        return self.__GraphMetaM_Edge

    @GraphMetaM_Edge.setter
    def GraphMetaM_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Edge__GraphMetaM_Edge", None)
        self.__GraphMetaM_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphMetaM_Graph2"):
                opp_val = getattr(old_value, "GraphMetaM_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphMetaM_Graph2"):
                opp_val = getattr(value, "GraphMetaM_Graph2", None)
                if opp_val is None:
                    setattr(value, "GraphMetaM_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex5"):
                opp_val = getattr(old_value, "Vertex5", None)
                if opp_val == self:
                    setattr(old_value, "Vertex5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex5"):
                opp_val = getattr(value, "Vertex5", None)
                setattr(value, "Vertex5", self)

    @property
    def Edge8(self):
        return self.__Edge8

    @Edge8.setter
    def Edge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Edge__Edge8", None)
        self.__Edge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Edge__incoming", None)
        self.__incoming = value
        
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
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphMetaM_Vertex:

    def __init__(self, cycles: int, globalPriority: int, activity: str, rName: str, type: str, name: str, Vertex: "GraphMetaM_Edge" = None, Vertex5: "GraphMetaM_Edge" = None, GraphMetaM_Vertex: "GraphMetaM_Graph" = None, target: set["GraphMetaM_Edge"] = None, source: set["GraphMetaM_Edge"] = None):
        self.cycles = cycles
        self.globalPriority = globalPriority
        self.activity = activity
        self.rName = rName
        self.type = type
        self.name = name
        self.Vertex = Vertex
        self.Vertex5 = Vertex5
        self.GraphMetaM_Vertex = GraphMetaM_Vertex
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def globalPriority(self) -> int:
        return self.__globalPriority

    @globalPriority.setter
    def globalPriority(self, globalPriority: int):
        self.__globalPriority = globalPriority

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rName(self) -> str:
        return self.__rName

    @rName.setter
    def rName(self, rName: str):
        self.__rName = rName

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def cycles(self) -> int:
        return self.__cycles

    @cycles.setter
    def cycles(self, cycles: int):
        self.__cycles = cycles

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Vertex__target", None)
        self.__target = value if value is not None else set()
        
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
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Vertex__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge8"):
                    opp_val = getattr(item, "Edge8", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge8"):
                    opp_val = getattr(item, "Edge8", None)
                    
                    setattr(item, "Edge8", self)
                    

    @property
    def Vertex5(self):
        return self.__Vertex5

    @Vertex5.setter
    def Vertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Vertex__Vertex5", None)
        self.__Vertex5 = value
        
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
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Vertex__Vertex", None)
        self.__Vertex = value
        
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
    def GraphMetaM_Vertex(self):
        return self.__GraphMetaM_Vertex

    @GraphMetaM_Vertex.setter
    def GraphMetaM_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Vertex__GraphMetaM_Vertex", None)
        self.__GraphMetaM_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphMetaM_Graph"):
                opp_val = getattr(old_value, "GraphMetaM_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphMetaM_Graph"):
                opp_val = getattr(value, "GraphMetaM_Graph", None)
                if opp_val is None:
                    setattr(value, "GraphMetaM_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphMetaM_Graph:

    def __init__(self, cycles: int, rName: str, name: str, GraphMetaM_Graph: set["GraphMetaM_Vertex"] = None, GraphMetaM_Graph2: set["GraphMetaM_Edge"] = None, GraphMetaM_Graph10: "GraphMetaM_Model" = None):
        self.cycles = cycles
        self.rName = rName
        self.name = name
        self.GraphMetaM_Graph = GraphMetaM_Graph if GraphMetaM_Graph is not None else set()
        self.GraphMetaM_Graph2 = GraphMetaM_Graph2 if GraphMetaM_Graph2 is not None else set()
        self.GraphMetaM_Graph10 = GraphMetaM_Graph10
        
    @property
    def rName(self) -> str:
        return self.__rName

    @rName.setter
    def rName(self, rName: str):
        self.__rName = rName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cycles(self) -> int:
        return self.__cycles

    @cycles.setter
    def cycles(self, cycles: int):
        self.__cycles = cycles

    @property
    def GraphMetaM_Graph2(self):
        return self.__GraphMetaM_Graph2

    @GraphMetaM_Graph2.setter
    def GraphMetaM_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Graph__GraphMetaM_Graph2", None)
        self.__GraphMetaM_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphMetaM_Edge"):
                    opp_val = getattr(item, "GraphMetaM_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphMetaM_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphMetaM_Edge"):
                    opp_val = getattr(item, "GraphMetaM_Edge", None)
                    
                    setattr(item, "GraphMetaM_Edge", self)
                    

    @property
    def GraphMetaM_Graph10(self):
        return self.__GraphMetaM_Graph10

    @GraphMetaM_Graph10.setter
    def GraphMetaM_Graph10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Graph__GraphMetaM_Graph10", None)
        self.__GraphMetaM_Graph10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphMetaM_Model"):
                opp_val = getattr(old_value, "GraphMetaM_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphMetaM_Model"):
                opp_val = getattr(value, "GraphMetaM_Model", None)
                if opp_val is None:
                    setattr(value, "GraphMetaM_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphMetaM_Graph(self):
        return self.__GraphMetaM_Graph

    @GraphMetaM_Graph.setter
    def GraphMetaM_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMetaM_Graph__GraphMetaM_Graph", None)
        self.__GraphMetaM_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphMetaM_Vertex"):
                    opp_val = getattr(item, "GraphMetaM_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphMetaM_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphMetaM_Vertex"):
                    opp_val = getattr(item, "GraphMetaM_Vertex", None)
                    
                    setattr(item, "GraphMetaM_Vertex", self)
                    
