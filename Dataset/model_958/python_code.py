from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Vertex:

    pass
class graph_Graph(Vertex):

    pass
class Adaptable:

    pass
class Attributable:

    pass
class graph_Edge(Attributable):

    def __init__(self, label: str, Edge: "graph_Vertex" = None, Edge5: "graph_Vertex" = None, graph_Edge8: "graph_Vertex" = None, outgoing: "graph_Vertex" = None, incoming: "graph_Vertex" = None, graph_Edge: "graph_Graph" = None):
        self.label = label
        self.Edge = Edge
        self.Edge5 = Edge5
        self.graph_Edge8 = graph_Edge8
        self.outgoing = outgoing
        self.incoming = incoming
        self.graph_Edge = graph_Edge
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__outgoing", None)
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
    def graph_Edge8(self):
        return self.__graph_Edge8

    @graph_Edge8.setter
    def graph_Edge8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge8", None)
        self.__graph_Edge8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex7"):
                opp_val = getattr(old_value, "graph_Vertex7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex7"):
                opp_val = getattr(value, "graph_Vertex7", None)
                if opp_val is None:
                    setattr(value, "graph_Vertex7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex20"):
                opp_val = getattr(old_value, "Vertex20", None)
                if opp_val == self:
                    setattr(old_value, "Vertex20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex20"):
                opp_val = getattr(value, "Vertex20", None)
                setattr(value, "Vertex20", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__Edge", None)
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

    @property
    def Edge5(self):
        return self.__Edge5

    @Edge5.setter
    def Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__Edge5", None)
        self.__Edge5 = value
        
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

class graph_Vertex(Adaptable, Attributable):

    def __init__(self, label: str, number: int, target: set["graph_Edge"] = None, source: set["graph_Edge"] = None, graph_Vertex7: set["graph_Edge"] = None, graph_Vertex11: "graph_Vertex" = None, graph_Vertex9: set["graph_Vertex"] = None, graph_Vertex14: "graph_Vertex" = None, graph_Vertex12: set["graph_Vertex"] = None, graph_Vertex17: "graph_Vertex" = None, graph_Vertex15: set["graph_Vertex"] = None, Vertex: "graph_Edge" = None, Vertex20: "graph_Edge" = None, graph_Vertex: "graph_Graph" = None):
        self.label = label
        self.number = number
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.graph_Vertex7 = graph_Vertex7 if graph_Vertex7 is not None else set()
        self.graph_Vertex11 = graph_Vertex11
        self.graph_Vertex9 = graph_Vertex9 if graph_Vertex9 is not None else set()
        self.graph_Vertex14 = graph_Vertex14
        self.graph_Vertex12 = graph_Vertex12 if graph_Vertex12 is not None else set()
        self.graph_Vertex17 = graph_Vertex17
        self.graph_Vertex15 = graph_Vertex15 if graph_Vertex15 is not None else set()
        self.Vertex = Vertex
        self.Vertex20 = Vertex20
        self.graph_Vertex = graph_Vertex
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__source", None)
        self.__source = value if value is not None else set()
        
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
    def graph_Vertex7(self):
        return self.__graph_Vertex7

    @graph_Vertex7.setter
    def graph_Vertex7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex7", None)
        self.__graph_Vertex7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge8"):
                    opp_val = getattr(item, "graph_Edge8", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge8"):
                    opp_val = getattr(item, "graph_Edge8", None)
                    
                    setattr(item, "graph_Edge8", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__target", None)
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
    def graph_Vertex(self):
        return self.__graph_Vertex

    @graph_Vertex.setter
    def graph_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex", None)
        self.__graph_Vertex = value
        
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
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__Vertex", None)
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
    def graph_Vertex12(self):
        return self.__graph_Vertex12

    @graph_Vertex12.setter
    def graph_Vertex12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex12", None)
        self.__graph_Vertex12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Vertex14"):
                    opp_val = getattr(item, "graph_Vertex14", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Vertex14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Vertex14"):
                    opp_val = getattr(item, "graph_Vertex14", None)
                    
                    setattr(item, "graph_Vertex14", self)
                    

    @property
    def Vertex20(self):
        return self.__Vertex20

    @Vertex20.setter
    def Vertex20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__Vertex20", None)
        self.__Vertex20 = value
        
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
    def graph_Vertex11(self):
        return self.__graph_Vertex11

    @graph_Vertex11.setter
    def graph_Vertex11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex11", None)
        self.__graph_Vertex11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex9"):
                opp_val = getattr(old_value, "graph_Vertex9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex9"):
                opp_val = getattr(value, "graph_Vertex9", None)
                if opp_val is None:
                    setattr(value, "graph_Vertex9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Vertex9(self):
        return self.__graph_Vertex9

    @graph_Vertex9.setter
    def graph_Vertex9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex9", None)
        self.__graph_Vertex9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Vertex11"):
                    opp_val = getattr(item, "graph_Vertex11", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Vertex11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Vertex11"):
                    opp_val = getattr(item, "graph_Vertex11", None)
                    
                    setattr(item, "graph_Vertex11", self)
                    

    @property
    def graph_Vertex15(self):
        return self.__graph_Vertex15

    @graph_Vertex15.setter
    def graph_Vertex15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex15", None)
        self.__graph_Vertex15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Vertex17"):
                    opp_val = getattr(item, "graph_Vertex17", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Vertex17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Vertex17"):
                    opp_val = getattr(item, "graph_Vertex17", None)
                    
                    setattr(item, "graph_Vertex17", self)
                    

    @property
    def graph_Vertex17(self):
        return self.__graph_Vertex17

    @graph_Vertex17.setter
    def graph_Vertex17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex17", None)
        self.__graph_Vertex17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex15"):
                opp_val = getattr(old_value, "graph_Vertex15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex15"):
                opp_val = getattr(value, "graph_Vertex15", None)
                if opp_val is None:
                    setattr(value, "graph_Vertex15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Vertex14(self):
        return self.__graph_Vertex14

    @graph_Vertex14.setter
    def graph_Vertex14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex14", None)
        self.__graph_Vertex14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex12"):
                opp_val = getattr(old_value, "graph_Vertex12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex12"):
                opp_val = getattr(value, "graph_Vertex12", None)
                if opp_val is None:
                    setattr(value, "graph_Vertex12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
