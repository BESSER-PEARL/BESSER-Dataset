from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Named:

    pass
class graph_Node(Named):

    def __init__(self, uri: str, type: str, derivedOrNotExists: bool, graph_Node: "graph_Graph" = None, graph_Node5: "graph_Edge" = None, graph_Node8: "graph_Edge" = None, graph_Node11: "graph_Edge" = None):
        self.uri = uri
        self.type = type
        self.derivedOrNotExists = derivedOrNotExists
        self.graph_Node = graph_Node
        self.graph_Node5 = graph_Node5
        self.graph_Node8 = graph_Node8
        self.graph_Node11 = graph_Node11
        
    @property
    def derivedOrNotExists(self) -> bool:
        return self.__derivedOrNotExists

    @derivedOrNotExists.setter
    def derivedOrNotExists(self, derivedOrNotExists: bool):
        self.__derivedOrNotExists = derivedOrNotExists

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def graph_Node(self):
        return self.__graph_Node

    @graph_Node.setter
    def graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node", None)
        self.__graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph"):
                opp_val = getattr(old_value, "graph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph"):
                opp_val = getattr(value, "graph_Graph", None)
                if opp_val is None:
                    setattr(value, "graph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node8(self):
        return self.__graph_Node8

    @graph_Node8.setter
    def graph_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node8", None)
        self.__graph_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge7"):
                opp_val = getattr(old_value, "graph_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge7"):
                opp_val = getattr(value, "graph_Edge7", None)
                setattr(value, "graph_Edge7", self)

    @property
    def graph_Node5(self):
        return self.__graph_Node5

    @graph_Node5.setter
    def graph_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node5", None)
        self.__graph_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge4"):
                opp_val = getattr(old_value, "graph_Edge4", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge4"):
                opp_val = getattr(value, "graph_Edge4", None)
                setattr(value, "graph_Edge4", self)

    @property
    def graph_Node11(self):
        return self.__graph_Node11

    @graph_Node11.setter
    def graph_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node11", None)
        self.__graph_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge10"):
                opp_val = getattr(old_value, "graph_Edge10", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge10"):
                opp_val = getattr(value, "graph_Edge10", None)
                setattr(value, "graph_Edge10", self)

class graph_Edge(Named):

    def __init__(self, exact: bool, pathDiscoveredByHeuristic: str, graph_Edge: "graph_Graph" = None, graph_Edge4: "graph_Node" = None, graph_Edge7: "graph_Node" = None, graph_Edge10: "graph_Node" = None):
        self.exact = exact
        self.pathDiscoveredByHeuristic = pathDiscoveredByHeuristic
        self.graph_Edge = graph_Edge
        self.graph_Edge4 = graph_Edge4
        self.graph_Edge7 = graph_Edge7
        self.graph_Edge10 = graph_Edge10
        
    @property
    def pathDiscoveredByHeuristic(self) -> str:
        return self.__pathDiscoveredByHeuristic

    @pathDiscoveredByHeuristic.setter
    def pathDiscoveredByHeuristic(self, pathDiscoveredByHeuristic: str):
        self.__pathDiscoveredByHeuristic = pathDiscoveredByHeuristic

    @property
    def exact(self) -> bool:
        return self.__exact

    @exact.setter
    def exact(self, exact: bool):
        self.__exact = exact

    @property
    def graph_Edge(self):
        return self.__graph_Edge

    @graph_Edge.setter
    def graph_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge", None)
        self.__graph_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph2"):
                opp_val = getattr(old_value, "graph_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph2"):
                opp_val = getattr(value, "graph_Graph2", None)
                if opp_val is None:
                    setattr(value, "graph_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Edge4(self):
        return self.__graph_Edge4

    @graph_Edge4.setter
    def graph_Edge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge4", None)
        self.__graph_Edge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node5"):
                opp_val = getattr(old_value, "graph_Node5", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node5"):
                opp_val = getattr(value, "graph_Node5", None)
                setattr(value, "graph_Node5", self)

    @property
    def graph_Edge10(self):
        return self.__graph_Edge10

    @graph_Edge10.setter
    def graph_Edge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge10", None)
        self.__graph_Edge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node11"):
                opp_val = getattr(old_value, "graph_Node11", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node11"):
                opp_val = getattr(value, "graph_Node11", None)
                setattr(value, "graph_Node11", self)

    @property
    def graph_Edge7(self):
        return self.__graph_Edge7

    @graph_Edge7.setter
    def graph_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge7", None)
        self.__graph_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node8"):
                opp_val = getattr(old_value, "graph_Node8", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node8"):
                opp_val = getattr(value, "graph_Node8", None)
                setattr(value, "graph_Node8", self)

class graph_Graph(Named):

    def __init__(self, owner: str, graph_Graph: set["graph_Node"] = None, graph_Graph2: set["graph_Edge"] = None):
        self.owner = owner
        self.graph_Graph = graph_Graph if graph_Graph is not None else set()
        self.graph_Graph2 = graph_Graph2 if graph_Graph2 is not None else set()
        
    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def graph_Graph(self):
        return self.__graph_Graph

    @graph_Graph.setter
    def graph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph", None)
        self.__graph_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    setattr(item, "graph_Node", self)
                    

    @property
    def graph_Graph2(self):
        return self.__graph_Graph2

    @graph_Graph2.setter
    def graph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph2", None)
        self.__graph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    setattr(item, "graph_Edge", self)
                    

class graph_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
