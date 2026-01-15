from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scaffolds_Contig:

    def __init__(self, length: int, multiplicity: int, scaffolds_Contig4: set["scaffolds_Vertex"] = None, scaffolds_Contig: "scaffolds_ScaffoldGraph" = None):
        self.length = length
        self.multiplicity = multiplicity
        self.scaffolds_Contig4 = scaffolds_Contig4 if scaffolds_Contig4 is not None else set()
        self.scaffolds_Contig = scaffolds_Contig
        
    @property
    def multiplicity(self) -> int:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def scaffolds_Contig4(self):
        return self.__scaffolds_Contig4

    @scaffolds_Contig4.setter
    def scaffolds_Contig4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Contig__scaffolds_Contig4", None)
        self.__scaffolds_Contig4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scaffolds_Vertex"):
                    opp_val = getattr(item, "scaffolds_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "scaffolds_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scaffolds_Vertex"):
                    opp_val = getattr(item, "scaffolds_Vertex", None)
                    
                    setattr(item, "scaffolds_Vertex", self)
                    

    @property
    def scaffolds_Contig(self):
        return self.__scaffolds_Contig

    @scaffolds_Contig.setter
    def scaffolds_Contig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Contig__scaffolds_Contig", None)
        self.__scaffolds_Contig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scaffolds_ScaffoldGraph"):
                opp_val = getattr(old_value, "scaffolds_ScaffoldGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scaffolds_ScaffoldGraph"):
                opp_val = getattr(value, "scaffolds_ScaffoldGraph", None)
                if opp_val is None:
                    setattr(value, "scaffolds_ScaffoldGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scaffolds_ScaffoldGraph:

    pass
class scaffolds_Vertex:

    def __init__(self, num: int, scaffolds_Vertex: "scaffolds_Contig" = None, Vertex: "scaffolds_Edge" = None, vertices: set["scaffolds_Edge"] = None):
        self.num = num
        self.scaffolds_Vertex = scaffolds_Vertex
        self.Vertex = Vertex
        self.vertices = vertices if vertices is not None else set()
        
    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Vertex__vertices", None)
        self.__vertices = value if value is not None else set()
        
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
    def scaffolds_Vertex(self):
        return self.__scaffolds_Vertex

    @scaffolds_Vertex.setter
    def scaffolds_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Vertex__scaffolds_Vertex", None)
        self.__scaffolds_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scaffolds_Contig4"):
                opp_val = getattr(old_value, "scaffolds_Contig4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scaffolds_Contig4"):
                opp_val = getattr(value, "scaffolds_Contig4", None)
                if opp_val is None:
                    setattr(value, "scaffolds_Contig4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Vertex__Vertex", None)
        self.__Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                if opp_val is None:
                    setattr(value, "edges", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scaffolds_Edge:

    def __init__(self, weight: int, distance: int, scaffolds_Edge: "scaffolds_ScaffoldGraph" = None, edges: set["scaffolds_Vertex"] = None, Edge: "scaffolds_Vertex" = None):
        self.weight = weight
        self.distance = distance
        self.scaffolds_Edge = scaffolds_Edge
        self.edges = edges if edges is not None else set()
        self.Edge = Edge
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vertices"):
                opp_val = getattr(old_value, "vertices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vertices"):
                opp_val = getattr(value, "vertices", None)
                if opp_val is None:
                    setattr(value, "vertices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Edge__edges", None)
        self.__edges = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    setattr(item, "Vertex", self)
                    

    @property
    def scaffolds_Edge(self):
        return self.__scaffolds_Edge

    @scaffolds_Edge.setter
    def scaffolds_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scaffolds_Edge__scaffolds_Edge", None)
        self.__scaffolds_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scaffolds_ScaffoldGraph2"):
                opp_val = getattr(old_value, "scaffolds_ScaffoldGraph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scaffolds_ScaffoldGraph2"):
                opp_val = getattr(value, "scaffolds_ScaffoldGraph2", None)
                if opp_val is None:
                    setattr(value, "scaffolds_ScaffoldGraph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
