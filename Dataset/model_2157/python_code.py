from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pcg_Resource:

    def __init__(self, id: str, title: str, pcg_Resource: "pcg_Vertex" = None):
        self.id = id
        self.title = title
        self.pcg_Resource = pcg_Resource
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pcg_Resource(self):
        return self.__pcg_Resource

    @pcg_Resource.setter
    def pcg_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcg_Resource__pcg_Resource", None)
        self.__pcg_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pcg_Vertex4"):
                opp_val = getattr(old_value, "pcg_Vertex4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pcg_Vertex4"):
                opp_val = getattr(value, "pcg_Vertex4", None)
                if opp_val is None:
                    setattr(value, "pcg_Vertex4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pcg_Edge:

    def __init__(self, kind: str, pcg_Edge: "pcg_Graph" = None, pcg_Edge6: "pcg_Vertex" = None, pcg_Edge9: "pcg_Vertex" = None):
        self.kind = kind
        self.pcg_Edge = pcg_Edge
        self.pcg_Edge6 = pcg_Edge6
        self.pcg_Edge9 = pcg_Edge9
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def pcg_Edge6(self):
        return self.__pcg_Edge6

    @pcg_Edge6.setter
    def pcg_Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcg_Edge__pcg_Edge6", None)
        self.__pcg_Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pcg_Vertex7"):
                opp_val = getattr(old_value, "pcg_Vertex7", None)
                if opp_val == self:
                    setattr(old_value, "pcg_Vertex7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pcg_Vertex7"):
                opp_val = getattr(value, "pcg_Vertex7", None)
                setattr(value, "pcg_Vertex7", self)

    @property
    def pcg_Edge9(self):
        return self.__pcg_Edge9

    @pcg_Edge9.setter
    def pcg_Edge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcg_Edge__pcg_Edge9", None)
        self.__pcg_Edge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pcg_Vertex10"):
                opp_val = getattr(old_value, "pcg_Vertex10", None)
                if opp_val == self:
                    setattr(old_value, "pcg_Vertex10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pcg_Vertex10"):
                opp_val = getattr(value, "pcg_Vertex10", None)
                setattr(value, "pcg_Vertex10", self)

    @property
    def pcg_Edge(self):
        return self.__pcg_Edge

    @pcg_Edge.setter
    def pcg_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcg_Edge__pcg_Edge", None)
        self.__pcg_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pcg_Graph2"):
                opp_val = getattr(old_value, "pcg_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pcg_Graph2"):
                opp_val = getattr(value, "pcg_Graph2", None)
                if opp_val is None:
                    setattr(value, "pcg_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pcg_Vertex:

    pass
class pcg_Graph:

    pass