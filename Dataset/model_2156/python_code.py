from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graphgrammar_TripleGraph:

    def __init__(self, graphgrammar_TripleGraph: "graphgrammar_Graph" = None, graphgrammar_TripleGraph113: "graphgrammar_Graph" = None, graphgrammar_TripleGraph116: "graphgrammar_Graph" = None, graphgrammar_TripleGraph119: set["graphgrammar_VertexToVertexMap"] = None, graphgrammar_TripleGraph122: set["graphgrammar_VertexToVertexMap"] = None):
        self.graphgrammar_TripleGraph = graphgrammar_TripleGraph
        self.graphgrammar_TripleGraph113 = graphgrammar_TripleGraph113
        self.graphgrammar_TripleGraph116 = graphgrammar_TripleGraph116
        self.graphgrammar_TripleGraph119 = graphgrammar_TripleGraph119 if graphgrammar_TripleGraph119 is not None else set()
        self.graphgrammar_TripleGraph122 = graphgrammar_TripleGraph122 if graphgrammar_TripleGraph122 is not None else set()
        
    @property
    def graphgrammar_TripleGraph113(self):
        return self.__graphgrammar_TripleGraph113

    @graphgrammar_TripleGraph113.setter
    def graphgrammar_TripleGraph113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGraph__graphgrammar_TripleGraph113", None)
        self.__graphgrammar_TripleGraph113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph114"):
                opp_val = getattr(old_value, "graphgrammar_Graph114", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Graph114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph114"):
                opp_val = getattr(value, "graphgrammar_Graph114", None)
                setattr(value, "graphgrammar_Graph114", self)

    @property
    def graphgrammar_TripleGraph(self):
        return self.__graphgrammar_TripleGraph

    @graphgrammar_TripleGraph.setter
    def graphgrammar_TripleGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGraph__graphgrammar_TripleGraph", None)
        self.__graphgrammar_TripleGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph111"):
                opp_val = getattr(old_value, "graphgrammar_Graph111", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Graph111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph111"):
                opp_val = getattr(value, "graphgrammar_Graph111", None)
                setattr(value, "graphgrammar_Graph111", self)

    @property
    def graphgrammar_TripleGraph116(self):
        return self.__graphgrammar_TripleGraph116

    @graphgrammar_TripleGraph116.setter
    def graphgrammar_TripleGraph116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGraph__graphgrammar_TripleGraph116", None)
        self.__graphgrammar_TripleGraph116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph117"):
                opp_val = getattr(old_value, "graphgrammar_Graph117", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Graph117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph117"):
                opp_val = getattr(value, "graphgrammar_Graph117", None)
                setattr(value, "graphgrammar_Graph117", self)

    @property
    def graphgrammar_TripleGraph119(self):
        return self.__graphgrammar_TripleGraph119

    @graphgrammar_TripleGraph119.setter
    def graphgrammar_TripleGraph119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGraph__graphgrammar_TripleGraph119", None)
        self.__graphgrammar_TripleGraph119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_VertexToVertexMap120"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap120", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_VertexToVertexMap120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_VertexToVertexMap120"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap120", None)
                    
                    setattr(item, "graphgrammar_VertexToVertexMap120", self)
                    

    @property
    def graphgrammar_TripleGraph122(self):
        return self.__graphgrammar_TripleGraph122

    @graphgrammar_TripleGraph122.setter
    def graphgrammar_TripleGraph122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGraph__graphgrammar_TripleGraph122", None)
        self.__graphgrammar_TripleGraph122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_VertexToVertexMap123"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap123", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_VertexToVertexMap123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_VertexToVertexMap123"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap123", None)
                    
                    setattr(item, "graphgrammar_VertexToVertexMap123", self)
                    

    def invMs(self, sourceVertex: Vertex) -> Vertex:
        # TODO: Implement invMs method
        pass

    def invMt(self, targetVertex: Vertex) -> Vertex:
        # TODO: Implement invMt method
        pass

class graphgrammar_TripleRule:

    def __init__(self, graphgrammar_TripleRule105: set["graphgrammar_VertexToVertexMap"] = None, graphgrammar_TripleRule108: set["graphgrammar_VertexToVertexMap"] = None, graphgrammar_TripleRule: "graphgrammar_TripleGrammar" = None, graphgrammar_TripleRule96: "graphgrammar_Rule" = None, graphgrammar_TripleRule99: "graphgrammar_Rule" = None, graphgrammar_TripleRule102: "graphgrammar_Rule" = None):
        self.graphgrammar_TripleRule105 = graphgrammar_TripleRule105 if graphgrammar_TripleRule105 is not None else set()
        self.graphgrammar_TripleRule108 = graphgrammar_TripleRule108 if graphgrammar_TripleRule108 is not None else set()
        self.graphgrammar_TripleRule = graphgrammar_TripleRule
        self.graphgrammar_TripleRule96 = graphgrammar_TripleRule96
        self.graphgrammar_TripleRule99 = graphgrammar_TripleRule99
        self.graphgrammar_TripleRule102 = graphgrammar_TripleRule102
        
    @property
    def graphgrammar_TripleRule105(self):
        return self.__graphgrammar_TripleRule105

    @graphgrammar_TripleRule105.setter
    def graphgrammar_TripleRule105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule105", None)
        self.__graphgrammar_TripleRule105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_VertexToVertexMap106"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap106", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_VertexToVertexMap106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_VertexToVertexMap106"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap106", None)
                    
                    setattr(item, "graphgrammar_VertexToVertexMap106", self)
                    

    @property
    def graphgrammar_TripleRule99(self):
        return self.__graphgrammar_TripleRule99

    @graphgrammar_TripleRule99.setter
    def graphgrammar_TripleRule99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule99", None)
        self.__graphgrammar_TripleRule99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule100"):
                opp_val = getattr(old_value, "graphgrammar_Rule100", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Rule100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule100"):
                opp_val = getattr(value, "graphgrammar_Rule100", None)
                setattr(value, "graphgrammar_Rule100", self)

    @property
    def graphgrammar_TripleRule(self):
        return self.__graphgrammar_TripleRule

    @graphgrammar_TripleRule.setter
    def graphgrammar_TripleRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule", None)
        self.__graphgrammar_TripleRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGrammar91"):
                opp_val = getattr(old_value, "graphgrammar_TripleGrammar91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGrammar91"):
                opp_val = getattr(value, "graphgrammar_TripleGrammar91", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_TripleGrammar91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_TripleRule96(self):
        return self.__graphgrammar_TripleRule96

    @graphgrammar_TripleRule96.setter
    def graphgrammar_TripleRule96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule96", None)
        self.__graphgrammar_TripleRule96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule97"):
                opp_val = getattr(old_value, "graphgrammar_Rule97", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Rule97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule97"):
                opp_val = getattr(value, "graphgrammar_Rule97", None)
                setattr(value, "graphgrammar_Rule97", self)

    @property
    def graphgrammar_TripleRule108(self):
        return self.__graphgrammar_TripleRule108

    @graphgrammar_TripleRule108.setter
    def graphgrammar_TripleRule108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule108", None)
        self.__graphgrammar_TripleRule108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_VertexToVertexMap109"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap109", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_VertexToVertexMap109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_VertexToVertexMap109"):
                    opp_val = getattr(item, "graphgrammar_VertexToVertexMap109", None)
                    
                    setattr(item, "graphgrammar_VertexToVertexMap109", self)
                    

    @property
    def graphgrammar_TripleRule102(self):
        return self.__graphgrammar_TripleRule102

    @graphgrammar_TripleRule102.setter
    def graphgrammar_TripleRule102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleRule__graphgrammar_TripleRule102", None)
        self.__graphgrammar_TripleRule102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule103"):
                opp_val = getattr(old_value, "graphgrammar_Rule103", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Rule103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule103"):
                opp_val = getattr(value, "graphgrammar_Rule103", None)
                setattr(value, "graphgrammar_Rule103", self)

    def invMt(self, targetVertex: Vertex) -> Vertex:
        # TODO: Implement invMt method
        pass

    def invMs(self, sourceVertex: Vertex) -> Vertex:
        # TODO: Implement invMs method
        pass

class graphgrammar_TripleGrammar:

    def __init__(self, name: str, graphgrammar_TripleGrammar: set["graphgrammar_Symbol"] = None, graphgrammar_TripleGrammar85: set["graphgrammar_Symbol"] = None, graphgrammar_TripleGrammar88: set["graphgrammar_Symbol"] = None, graphgrammar_TripleGrammar91: set["graphgrammar_TripleRule"] = None, graphgrammar_TripleGrammar93: "graphgrammar_Symbol" = None):
        self.name = name
        self.graphgrammar_TripleGrammar = graphgrammar_TripleGrammar if graphgrammar_TripleGrammar is not None else set()
        self.graphgrammar_TripleGrammar85 = graphgrammar_TripleGrammar85 if graphgrammar_TripleGrammar85 is not None else set()
        self.graphgrammar_TripleGrammar88 = graphgrammar_TripleGrammar88 if graphgrammar_TripleGrammar88 is not None else set()
        self.graphgrammar_TripleGrammar91 = graphgrammar_TripleGrammar91 if graphgrammar_TripleGrammar91 is not None else set()
        self.graphgrammar_TripleGrammar93 = graphgrammar_TripleGrammar93
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphgrammar_TripleGrammar88(self):
        return self.__graphgrammar_TripleGrammar88

    @graphgrammar_TripleGrammar88.setter
    def graphgrammar_TripleGrammar88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGrammar__graphgrammar_TripleGrammar88", None)
        self.__graphgrammar_TripleGrammar88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol89"):
                    opp_val = getattr(item, "graphgrammar_Symbol89", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol89"):
                    opp_val = getattr(item, "graphgrammar_Symbol89", None)
                    
                    setattr(item, "graphgrammar_Symbol89", self)
                    

    @property
    def graphgrammar_TripleGrammar91(self):
        return self.__graphgrammar_TripleGrammar91

    @graphgrammar_TripleGrammar91.setter
    def graphgrammar_TripleGrammar91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGrammar__graphgrammar_TripleGrammar91", None)
        self.__graphgrammar_TripleGrammar91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_TripleRule"):
                    opp_val = getattr(item, "graphgrammar_TripleRule", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_TripleRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_TripleRule"):
                    opp_val = getattr(item, "graphgrammar_TripleRule", None)
                    
                    setattr(item, "graphgrammar_TripleRule", self)
                    

    @property
    def graphgrammar_TripleGrammar85(self):
        return self.__graphgrammar_TripleGrammar85

    @graphgrammar_TripleGrammar85.setter
    def graphgrammar_TripleGrammar85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGrammar__graphgrammar_TripleGrammar85", None)
        self.__graphgrammar_TripleGrammar85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol86"):
                    opp_val = getattr(item, "graphgrammar_Symbol86", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol86"):
                    opp_val = getattr(item, "graphgrammar_Symbol86", None)
                    
                    setattr(item, "graphgrammar_Symbol86", self)
                    

    @property
    def graphgrammar_TripleGrammar(self):
        return self.__graphgrammar_TripleGrammar

    @graphgrammar_TripleGrammar.setter
    def graphgrammar_TripleGrammar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGrammar__graphgrammar_TripleGrammar", None)
        self.__graphgrammar_TripleGrammar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol83"):
                    opp_val = getattr(item, "graphgrammar_Symbol83", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol83"):
                    opp_val = getattr(item, "graphgrammar_Symbol83", None)
                    
                    setattr(item, "graphgrammar_Symbol83", self)
                    

    @property
    def graphgrammar_TripleGrammar93(self):
        return self.__graphgrammar_TripleGrammar93

    @graphgrammar_TripleGrammar93.setter
    def graphgrammar_TripleGrammar93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_TripleGrammar__graphgrammar_TripleGrammar93", None)
        self.__graphgrammar_TripleGrammar93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Symbol94"):
                opp_val = getattr(old_value, "graphgrammar_Symbol94", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Symbol94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Symbol94"):
                opp_val = getattr(value, "graphgrammar_Symbol94", None)
                setattr(value, "graphgrammar_Symbol94", self)

    def produce(self, forward: bool, tripleGraph: str, derivationStep: str, resolution: str) -> str:
        # TODO: Implement produce method
        pass

    def resolve(self, resolutionStep: str, resolution: str, forward: bool, tripleGraph: str):
        # TODO: Implement resolve method
        pass

class Vertex:

    pass
class graphgrammar_Edge:

    def __init__(self, graphgrammar_Edge74: "graphgrammar_Vertex" = None, graphgrammar_Edge77: "graphgrammar_Vertex" = None, graphgrammar_Edge: "graphgrammar_Graph" = None, graphgrammar_Edge80: "graphgrammar_Symbol" = None):
        self.graphgrammar_Edge74 = graphgrammar_Edge74
        self.graphgrammar_Edge77 = graphgrammar_Edge77
        self.graphgrammar_Edge = graphgrammar_Edge
        self.graphgrammar_Edge80 = graphgrammar_Edge80
        
    @property
    def graphgrammar_Edge80(self):
        return self.__graphgrammar_Edge80

    @graphgrammar_Edge80.setter
    def graphgrammar_Edge80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Edge__graphgrammar_Edge80", None)
        self.__graphgrammar_Edge80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Symbol81"):
                opp_val = getattr(old_value, "graphgrammar_Symbol81", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Symbol81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Symbol81"):
                opp_val = getattr(value, "graphgrammar_Symbol81", None)
                setattr(value, "graphgrammar_Symbol81", self)

    @property
    def graphgrammar_Edge77(self):
        return self.__graphgrammar_Edge77

    @graphgrammar_Edge77.setter
    def graphgrammar_Edge77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Edge__graphgrammar_Edge77", None)
        self.__graphgrammar_Edge77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Vertex78"):
                opp_val = getattr(old_value, "graphgrammar_Vertex78", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Vertex78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Vertex78"):
                opp_val = getattr(value, "graphgrammar_Vertex78", None)
                setattr(value, "graphgrammar_Vertex78", self)

    @property
    def graphgrammar_Edge(self):
        return self.__graphgrammar_Edge

    @graphgrammar_Edge.setter
    def graphgrammar_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Edge__graphgrammar_Edge", None)
        self.__graphgrammar_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph63"):
                opp_val = getattr(old_value, "graphgrammar_Graph63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph63"):
                opp_val = getattr(value, "graphgrammar_Graph63", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Graph63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Edge74(self):
        return self.__graphgrammar_Edge74

    @graphgrammar_Edge74.setter
    def graphgrammar_Edge74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Edge__graphgrammar_Edge74", None)
        self.__graphgrammar_Edge74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Vertex75"):
                opp_val = getattr(old_value, "graphgrammar_Vertex75", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Vertex75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Vertex75"):
                opp_val = getattr(value, "graphgrammar_Vertex75", None)
                setattr(value, "graphgrammar_Vertex75", self)

    def compareTo(self, other: str) -> int:
        # TODO: Implement compareTo method
        pass

class graphgrammar_StringToVertexMap:

    def __init__(self, key: str, graphgrammar_StringToVertexMap: "graphgrammar_Resolution" = None, graphgrammar_StringToVertexMap134: "graphgrammar_Vertex" = None):
        self.key = key
        self.graphgrammar_StringToVertexMap = graphgrammar_StringToVertexMap
        self.graphgrammar_StringToVertexMap134 = graphgrammar_StringToVertexMap134
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graphgrammar_StringToVertexMap134(self):
        return self.__graphgrammar_StringToVertexMap134

    @graphgrammar_StringToVertexMap134.setter
    def graphgrammar_StringToVertexMap134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_StringToVertexMap__graphgrammar_StringToVertexMap134", None)
        self.__graphgrammar_StringToVertexMap134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Vertex135"):
                opp_val = getattr(old_value, "graphgrammar_Vertex135", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Vertex135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Vertex135"):
                opp_val = getattr(value, "graphgrammar_Vertex135", None)
                setattr(value, "graphgrammar_Vertex135", self)

    @property
    def graphgrammar_StringToVertexMap(self):
        return self.__graphgrammar_StringToVertexMap

    @graphgrammar_StringToVertexMap.setter
    def graphgrammar_StringToVertexMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_StringToVertexMap__graphgrammar_StringToVertexMap", None)
        self.__graphgrammar_StringToVertexMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Resolution"):
                opp_val = getattr(old_value, "graphgrammar_Resolution", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Resolution"):
                opp_val = getattr(value, "graphgrammar_Resolution", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Resolution", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphgrammar_Resolution:

    pass
class graphgrammar_VertexToStringMap:

    def __init__(self, value: str, graphgrammar_VertexToStringMap: "graphgrammar_ResolutionStep" = None, graphgrammar_VertexToStringMap131: "graphgrammar_Vertex" = None):
        self.value = value
        self.graphgrammar_VertexToStringMap = graphgrammar_VertexToStringMap
        self.graphgrammar_VertexToStringMap131 = graphgrammar_VertexToStringMap131
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def graphgrammar_VertexToStringMap131(self):
        return self.__graphgrammar_VertexToStringMap131

    @graphgrammar_VertexToStringMap131.setter
    def graphgrammar_VertexToStringMap131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_VertexToStringMap__graphgrammar_VertexToStringMap131", None)
        self.__graphgrammar_VertexToStringMap131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Vertex132"):
                opp_val = getattr(old_value, "graphgrammar_Vertex132", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Vertex132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Vertex132"):
                opp_val = getattr(value, "graphgrammar_Vertex132", None)
                setattr(value, "graphgrammar_Vertex132", self)

    @property
    def graphgrammar_VertexToStringMap(self):
        return self.__graphgrammar_VertexToStringMap

    @graphgrammar_VertexToStringMap.setter
    def graphgrammar_VertexToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_VertexToStringMap__graphgrammar_VertexToStringMap", None)
        self.__graphgrammar_VertexToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ResolutionStep"):
                opp_val = getattr(old_value, "graphgrammar_ResolutionStep", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ResolutionStep"):
                opp_val = getattr(value, "graphgrammar_ResolutionStep", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_ResolutionStep", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphgrammar_ResolutionStep:

    pass
class graphgrammar_ZoneVertex(Vertex):

    def __init__(self, graphgrammar_ZoneVertex: "graphgrammar_ParsingTree" = None, graphgrammar_ZoneVertex68: set["graphgrammar_Vertex"] = None, graphgrammar_ZoneVertex71: set["graphgrammar_Vertex"] = None):
        self.graphgrammar_ZoneVertex = graphgrammar_ZoneVertex
        self.graphgrammar_ZoneVertex68 = graphgrammar_ZoneVertex68 if graphgrammar_ZoneVertex68 is not None else set()
        self.graphgrammar_ZoneVertex71 = graphgrammar_ZoneVertex71 if graphgrammar_ZoneVertex71 is not None else set()
        
    @property
    def graphgrammar_ZoneVertex(self):
        return self.__graphgrammar_ZoneVertex

    @graphgrammar_ZoneVertex.setter
    def graphgrammar_ZoneVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ZoneVertex__graphgrammar_ZoneVertex", None)
        self.__graphgrammar_ZoneVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ParsingTree"):
                opp_val = getattr(old_value, "graphgrammar_ParsingTree", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_ParsingTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ParsingTree"):
                opp_val = getattr(value, "graphgrammar_ParsingTree", None)
                setattr(value, "graphgrammar_ParsingTree", self)

    @property
    def graphgrammar_ZoneVertex68(self):
        return self.__graphgrammar_ZoneVertex68

    @graphgrammar_ZoneVertex68.setter
    def graphgrammar_ZoneVertex68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ZoneVertex__graphgrammar_ZoneVertex68", None)
        self.__graphgrammar_ZoneVertex68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Vertex69"):
                    opp_val = getattr(item, "graphgrammar_Vertex69", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Vertex69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Vertex69"):
                    opp_val = getattr(item, "graphgrammar_Vertex69", None)
                    
                    setattr(item, "graphgrammar_Vertex69", self)
                    

    @property
    def graphgrammar_ZoneVertex71(self):
        return self.__graphgrammar_ZoneVertex71

    @graphgrammar_ZoneVertex71.setter
    def graphgrammar_ZoneVertex71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ZoneVertex__graphgrammar_ZoneVertex71", None)
        self.__graphgrammar_ZoneVertex71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Vertex72"):
                    opp_val = getattr(item, "graphgrammar_Vertex72", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Vertex72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Vertex72"):
                    opp_val = getattr(item, "graphgrammar_Vertex72", None)
                    
                    setattr(item, "graphgrammar_Vertex72", self)
                    

    def equivalates(self, other: str) -> bool:
        # TODO: Implement equivalates method
        pass

class graphgrammar_ParsingTree:

    def __init__(self, graphgrammar_ParsingTree: "graphgrammar_ZoneVertex" = None, graphgrammar_ParsingTree49: "graphgrammar_DerivationStep" = None, graphgrammar_ParsingTree53: "graphgrammar_ParsingTree" = None, graphgrammar_ParsingTree51: set["graphgrammar_ParsingTree"] = None):
        self.graphgrammar_ParsingTree = graphgrammar_ParsingTree
        self.graphgrammar_ParsingTree49 = graphgrammar_ParsingTree49
        self.graphgrammar_ParsingTree53 = graphgrammar_ParsingTree53
        self.graphgrammar_ParsingTree51 = graphgrammar_ParsingTree51 if graphgrammar_ParsingTree51 is not None else set()
        
    @property
    def graphgrammar_ParsingTree51(self):
        return self.__graphgrammar_ParsingTree51

    @graphgrammar_ParsingTree51.setter
    def graphgrammar_ParsingTree51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ParsingTree__graphgrammar_ParsingTree51", None)
        self.__graphgrammar_ParsingTree51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_ParsingTree53"):
                    opp_val = getattr(item, "graphgrammar_ParsingTree53", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_ParsingTree53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_ParsingTree53"):
                    opp_val = getattr(item, "graphgrammar_ParsingTree53", None)
                    
                    setattr(item, "graphgrammar_ParsingTree53", self)
                    

    @property
    def graphgrammar_ParsingTree49(self):
        return self.__graphgrammar_ParsingTree49

    @graphgrammar_ParsingTree49.setter
    def graphgrammar_ParsingTree49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ParsingTree__graphgrammar_ParsingTree49", None)
        self.__graphgrammar_ParsingTree49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_DerivationStep50"):
                opp_val = getattr(old_value, "graphgrammar_DerivationStep50", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_DerivationStep50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_DerivationStep50"):
                opp_val = getattr(value, "graphgrammar_DerivationStep50", None)
                setattr(value, "graphgrammar_DerivationStep50", self)

    @property
    def graphgrammar_ParsingTree(self):
        return self.__graphgrammar_ParsingTree

    @graphgrammar_ParsingTree.setter
    def graphgrammar_ParsingTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ParsingTree__graphgrammar_ParsingTree", None)
        self.__graphgrammar_ParsingTree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ZoneVertex"):
                opp_val = getattr(old_value, "graphgrammar_ZoneVertex", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_ZoneVertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ZoneVertex"):
                opp_val = getattr(value, "graphgrammar_ZoneVertex", None)
                setattr(value, "graphgrammar_ZoneVertex", self)

    @property
    def graphgrammar_ParsingTree53(self):
        return self.__graphgrammar_ParsingTree53

    @graphgrammar_ParsingTree53.setter
    def graphgrammar_ParsingTree53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_ParsingTree__graphgrammar_ParsingTree53", None)
        self.__graphgrammar_ParsingTree53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ParsingTree51"):
                opp_val = getattr(old_value, "graphgrammar_ParsingTree51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ParsingTree51"):
                opp_val = getattr(value, "graphgrammar_ParsingTree51", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_ParsingTree51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def derivation(self) -> str:
        # TODO: Implement derivation method
        pass

class graphgrammar_DerivationStep:

    pass
class graphgrammar_SymbolSymbolsPair:

    pass
class graphgrammar_Derivation:

    pass
class graphgrammar_Graph:

    def __init__(self, graphgrammar_Graph: "graphgrammar_Rule" = None, graphgrammar_Graph42: "graphgrammar_DerivationStep" = None, graphgrammar_Graph39: "graphgrammar_DerivationStep" = None, graphgrammar_Graph60: set["graphgrammar_Vertex"] = None, graphgrammar_Graph63: set["graphgrammar_Edge"] = None, graphgrammar_Graph111: "graphgrammar_TripleGraph" = None, graphgrammar_Graph114: "graphgrammar_TripleGraph" = None, graphgrammar_Graph117: "graphgrammar_TripleGraph" = None):
        self.graphgrammar_Graph = graphgrammar_Graph
        self.graphgrammar_Graph42 = graphgrammar_Graph42
        self.graphgrammar_Graph39 = graphgrammar_Graph39
        self.graphgrammar_Graph60 = graphgrammar_Graph60 if graphgrammar_Graph60 is not None else set()
        self.graphgrammar_Graph63 = graphgrammar_Graph63 if graphgrammar_Graph63 is not None else set()
        self.graphgrammar_Graph111 = graphgrammar_Graph111
        self.graphgrammar_Graph114 = graphgrammar_Graph114
        self.graphgrammar_Graph117 = graphgrammar_Graph117
        
    @property
    def graphgrammar_Graph(self):
        return self.__graphgrammar_Graph

    @graphgrammar_Graph.setter
    def graphgrammar_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph", None)
        self.__graphgrammar_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule16"):
                opp_val = getattr(old_value, "graphgrammar_Rule16", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Rule16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule16"):
                opp_val = getattr(value, "graphgrammar_Rule16", None)
                setattr(value, "graphgrammar_Rule16", self)

    @property
    def graphgrammar_Graph114(self):
        return self.__graphgrammar_Graph114

    @graphgrammar_Graph114.setter
    def graphgrammar_Graph114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph114", None)
        self.__graphgrammar_Graph114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGraph113"):
                opp_val = getattr(old_value, "graphgrammar_TripleGraph113", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleGraph113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGraph113"):
                opp_val = getattr(value, "graphgrammar_TripleGraph113", None)
                setattr(value, "graphgrammar_TripleGraph113", self)

    @property
    def graphgrammar_Graph117(self):
        return self.__graphgrammar_Graph117

    @graphgrammar_Graph117.setter
    def graphgrammar_Graph117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph117", None)
        self.__graphgrammar_Graph117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGraph116"):
                opp_val = getattr(old_value, "graphgrammar_TripleGraph116", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleGraph116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGraph116"):
                opp_val = getattr(value, "graphgrammar_TripleGraph116", None)
                setattr(value, "graphgrammar_TripleGraph116", self)

    @property
    def graphgrammar_Graph42(self):
        return self.__graphgrammar_Graph42

    @graphgrammar_Graph42.setter
    def graphgrammar_Graph42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph42", None)
        self.__graphgrammar_Graph42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_DerivationStep41"):
                opp_val = getattr(old_value, "graphgrammar_DerivationStep41", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_DerivationStep41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_DerivationStep41"):
                opp_val = getattr(value, "graphgrammar_DerivationStep41", None)
                setattr(value, "graphgrammar_DerivationStep41", self)

    @property
    def graphgrammar_Graph63(self):
        return self.__graphgrammar_Graph63

    @graphgrammar_Graph63.setter
    def graphgrammar_Graph63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph63", None)
        self.__graphgrammar_Graph63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Edge"):
                    opp_val = getattr(item, "graphgrammar_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Edge"):
                    opp_val = getattr(item, "graphgrammar_Edge", None)
                    
                    setattr(item, "graphgrammar_Edge", self)
                    

    @property
    def graphgrammar_Graph39(self):
        return self.__graphgrammar_Graph39

    @graphgrammar_Graph39.setter
    def graphgrammar_Graph39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph39", None)
        self.__graphgrammar_Graph39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_DerivationStep38"):
                opp_val = getattr(old_value, "graphgrammar_DerivationStep38", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_DerivationStep38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_DerivationStep38"):
                opp_val = getattr(value, "graphgrammar_DerivationStep38", None)
                setattr(value, "graphgrammar_DerivationStep38", self)

    @property
    def graphgrammar_Graph111(self):
        return self.__graphgrammar_Graph111

    @graphgrammar_Graph111.setter
    def graphgrammar_Graph111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph111", None)
        self.__graphgrammar_Graph111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGraph"):
                opp_val = getattr(old_value, "graphgrammar_TripleGraph", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGraph"):
                opp_val = getattr(value, "graphgrammar_TripleGraph", None)
                setattr(value, "graphgrammar_TripleGraph", self)

    @property
    def graphgrammar_Graph60(self):
        return self.__graphgrammar_Graph60

    @graphgrammar_Graph60.setter
    def graphgrammar_Graph60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Graph__graphgrammar_Graph60", None)
        self.__graphgrammar_Graph60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Vertex61"):
                    opp_val = getattr(item, "graphgrammar_Vertex61", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Vertex61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Vertex61"):
                    opp_val = getattr(item, "graphgrammar_Vertex61", None)
                    
                    setattr(item, "graphgrammar_Vertex61", self)
                    

    def neighborhood(self, vertex: str) -> str:
        # TODO: Implement neighborhood method
        pass

    def isomorphism(self, other: str) -> str:
        # TODO: Implement isomorphism method
        pass

    def edges(self, vertex: str) -> str:
        # TODO: Implement edges method
        pass

    def neighborhood(self, vertices: str) -> str:
        # TODO: Implement neighborhood method
        pass

    def inEdges(self, vertex: str) -> str:
        # TODO: Implement inEdges method
        pass

    def outEdges(self, vertex: str) -> str:
        # TODO: Implement outEdges method
        pass

    def isomorphicTo(self, other: str) -> bool:
        # TODO: Implement isomorphicTo method
        pass

class graphgrammar_Vertex:

    def __init__(self, id: str, graphgrammar_Vertex: "graphgrammar_Rule" = None, graphgrammar_Vertex28: "graphgrammar_VertexToSymbolSymbolsPairMap" = None, graphgrammar_Vertex36: "graphgrammar_DerivationStep" = None, graphgrammar_Vertex78: "graphgrammar_Edge" = None, graphgrammar_Vertex61: "graphgrammar_Graph" = None, graphgrammar_Vertex65: "graphgrammar_Symbol" = None, graphgrammar_Vertex69: "graphgrammar_ZoneVertex" = None, graphgrammar_Vertex72: "graphgrammar_ZoneVertex" = None, graphgrammar_Vertex75: "graphgrammar_Edge" = None, graphgrammar_Vertex126: "graphgrammar_VertexToVertexMap" = None, graphgrammar_Vertex129: "graphgrammar_VertexToVertexMap" = None, graphgrammar_Vertex132: "graphgrammar_VertexToStringMap" = None, graphgrammar_Vertex135: "graphgrammar_StringToVertexMap" = None):
        self.id = id
        self.graphgrammar_Vertex = graphgrammar_Vertex
        self.graphgrammar_Vertex28 = graphgrammar_Vertex28
        self.graphgrammar_Vertex36 = graphgrammar_Vertex36
        self.graphgrammar_Vertex78 = graphgrammar_Vertex78
        self.graphgrammar_Vertex61 = graphgrammar_Vertex61
        self.graphgrammar_Vertex65 = graphgrammar_Vertex65
        self.graphgrammar_Vertex69 = graphgrammar_Vertex69
        self.graphgrammar_Vertex72 = graphgrammar_Vertex72
        self.graphgrammar_Vertex75 = graphgrammar_Vertex75
        self.graphgrammar_Vertex126 = graphgrammar_Vertex126
        self.graphgrammar_Vertex129 = graphgrammar_Vertex129
        self.graphgrammar_Vertex132 = graphgrammar_Vertex132
        self.graphgrammar_Vertex135 = graphgrammar_Vertex135
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def graphgrammar_Vertex69(self):
        return self.__graphgrammar_Vertex69

    @graphgrammar_Vertex69.setter
    def graphgrammar_Vertex69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex69", None)
        self.__graphgrammar_Vertex69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ZoneVertex68"):
                opp_val = getattr(old_value, "graphgrammar_ZoneVertex68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ZoneVertex68"):
                opp_val = getattr(value, "graphgrammar_ZoneVertex68", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_ZoneVertex68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Vertex78(self):
        return self.__graphgrammar_Vertex78

    @graphgrammar_Vertex78.setter
    def graphgrammar_Vertex78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex78", None)
        self.__graphgrammar_Vertex78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Edge77"):
                opp_val = getattr(old_value, "graphgrammar_Edge77", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Edge77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Edge77"):
                opp_val = getattr(value, "graphgrammar_Edge77", None)
                setattr(value, "graphgrammar_Edge77", self)

    @property
    def graphgrammar_Vertex61(self):
        return self.__graphgrammar_Vertex61

    @graphgrammar_Vertex61.setter
    def graphgrammar_Vertex61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex61", None)
        self.__graphgrammar_Vertex61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph60"):
                opp_val = getattr(old_value, "graphgrammar_Graph60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph60"):
                opp_val = getattr(value, "graphgrammar_Graph60", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Graph60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Vertex(self):
        return self.__graphgrammar_Vertex

    @graphgrammar_Vertex.setter
    def graphgrammar_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex", None)
        self.__graphgrammar_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule20"):
                opp_val = getattr(old_value, "graphgrammar_Rule20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule20"):
                opp_val = getattr(value, "graphgrammar_Rule20", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Rule20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Vertex126(self):
        return self.__graphgrammar_Vertex126

    @graphgrammar_Vertex126.setter
    def graphgrammar_Vertex126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex126", None)
        self.__graphgrammar_Vertex126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_VertexToVertexMap125"):
                opp_val = getattr(old_value, "graphgrammar_VertexToVertexMap125", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_VertexToVertexMap125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_VertexToVertexMap125"):
                opp_val = getattr(value, "graphgrammar_VertexToVertexMap125", None)
                setattr(value, "graphgrammar_VertexToVertexMap125", self)

    @property
    def graphgrammar_Vertex129(self):
        return self.__graphgrammar_Vertex129

    @graphgrammar_Vertex129.setter
    def graphgrammar_Vertex129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex129", None)
        self.__graphgrammar_Vertex129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_VertexToVertexMap128"):
                opp_val = getattr(old_value, "graphgrammar_VertexToVertexMap128", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_VertexToVertexMap128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_VertexToVertexMap128"):
                opp_val = getattr(value, "graphgrammar_VertexToVertexMap128", None)
                setattr(value, "graphgrammar_VertexToVertexMap128", self)

    @property
    def graphgrammar_Vertex65(self):
        return self.__graphgrammar_Vertex65

    @graphgrammar_Vertex65.setter
    def graphgrammar_Vertex65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex65", None)
        self.__graphgrammar_Vertex65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Symbol66"):
                opp_val = getattr(old_value, "graphgrammar_Symbol66", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Symbol66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Symbol66"):
                opp_val = getattr(value, "graphgrammar_Symbol66", None)
                setattr(value, "graphgrammar_Symbol66", self)

    @property
    def graphgrammar_Vertex132(self):
        return self.__graphgrammar_Vertex132

    @graphgrammar_Vertex132.setter
    def graphgrammar_Vertex132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex132", None)
        self.__graphgrammar_Vertex132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_VertexToStringMap131"):
                opp_val = getattr(old_value, "graphgrammar_VertexToStringMap131", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_VertexToStringMap131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_VertexToStringMap131"):
                opp_val = getattr(value, "graphgrammar_VertexToStringMap131", None)
                setattr(value, "graphgrammar_VertexToStringMap131", self)

    @property
    def graphgrammar_Vertex36(self):
        return self.__graphgrammar_Vertex36

    @graphgrammar_Vertex36.setter
    def graphgrammar_Vertex36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex36", None)
        self.__graphgrammar_Vertex36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_DerivationStep35"):
                opp_val = getattr(old_value, "graphgrammar_DerivationStep35", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_DerivationStep35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_DerivationStep35"):
                opp_val = getattr(value, "graphgrammar_DerivationStep35", None)
                setattr(value, "graphgrammar_DerivationStep35", self)

    @property
    def graphgrammar_Vertex72(self):
        return self.__graphgrammar_Vertex72

    @graphgrammar_Vertex72.setter
    def graphgrammar_Vertex72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex72", None)
        self.__graphgrammar_Vertex72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_ZoneVertex71"):
                opp_val = getattr(old_value, "graphgrammar_ZoneVertex71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_ZoneVertex71"):
                opp_val = getattr(value, "graphgrammar_ZoneVertex71", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_ZoneVertex71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Vertex135(self):
        return self.__graphgrammar_Vertex135

    @graphgrammar_Vertex135.setter
    def graphgrammar_Vertex135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex135", None)
        self.__graphgrammar_Vertex135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_StringToVertexMap134"):
                opp_val = getattr(old_value, "graphgrammar_StringToVertexMap134", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_StringToVertexMap134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_StringToVertexMap134"):
                opp_val = getattr(value, "graphgrammar_StringToVertexMap134", None)
                setattr(value, "graphgrammar_StringToVertexMap134", self)

    @property
    def graphgrammar_Vertex28(self):
        return self.__graphgrammar_Vertex28

    @graphgrammar_Vertex28.setter
    def graphgrammar_Vertex28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex28", None)
        self.__graphgrammar_Vertex28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_VertexToSymbolSymbolsPairMap27"):
                opp_val = getattr(old_value, "graphgrammar_VertexToSymbolSymbolsPairMap27", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_VertexToSymbolSymbolsPairMap27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_VertexToSymbolSymbolsPairMap27"):
                opp_val = getattr(value, "graphgrammar_VertexToSymbolSymbolsPairMap27", None)
                setattr(value, "graphgrammar_VertexToSymbolSymbolsPairMap27", self)

    @property
    def graphgrammar_Vertex75(self):
        return self.__graphgrammar_Vertex75

    @graphgrammar_Vertex75.setter
    def graphgrammar_Vertex75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Vertex__graphgrammar_Vertex75", None)
        self.__graphgrammar_Vertex75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Edge74"):
                opp_val = getattr(old_value, "graphgrammar_Edge74", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Edge74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Edge74"):
                opp_val = getattr(value, "graphgrammar_Edge74", None)
                setattr(value, "graphgrammar_Edge74", self)

    def equivalates(self, other: str) -> bool:
        # TODO: Implement equivalates method
        pass

class graphgrammar_VertexToVertexMap:

    pass
class graphgrammar_VertexToSymbolSymbolsPairMap:

    pass
class graphgrammar_Symbol:

    def __init__(self, name: str, subscript: str, superscript: str, graphgrammar_Symbol3: "graphgrammar_Grammar" = None, graphgrammar_Symbol6: "graphgrammar_Grammar" = None, graphgrammar_Symbol11: "graphgrammar_Grammar" = None, graphgrammar_Symbol: "graphgrammar_Grammar" = None, graphgrammar_Symbol14: "graphgrammar_Rule" = None, graphgrammar_Symbol22: "graphgrammar_SymbolSymbolsPair" = None, graphgrammar_Symbol25: "graphgrammar_SymbolSymbolsPair" = None, graphgrammar_Symbol66: "graphgrammar_Vertex" = None, graphgrammar_Symbol81: "graphgrammar_Edge" = None, graphgrammar_Symbol83: "graphgrammar_TripleGrammar" = None, graphgrammar_Symbol86: "graphgrammar_TripleGrammar" = None, graphgrammar_Symbol89: "graphgrammar_TripleGrammar" = None, graphgrammar_Symbol94: "graphgrammar_TripleGrammar" = None):
        self.name = name
        self.subscript = subscript
        self.superscript = superscript
        self.graphgrammar_Symbol3 = graphgrammar_Symbol3
        self.graphgrammar_Symbol6 = graphgrammar_Symbol6
        self.graphgrammar_Symbol11 = graphgrammar_Symbol11
        self.graphgrammar_Symbol = graphgrammar_Symbol
        self.graphgrammar_Symbol14 = graphgrammar_Symbol14
        self.graphgrammar_Symbol22 = graphgrammar_Symbol22
        self.graphgrammar_Symbol25 = graphgrammar_Symbol25
        self.graphgrammar_Symbol66 = graphgrammar_Symbol66
        self.graphgrammar_Symbol81 = graphgrammar_Symbol81
        self.graphgrammar_Symbol83 = graphgrammar_Symbol83
        self.graphgrammar_Symbol86 = graphgrammar_Symbol86
        self.graphgrammar_Symbol89 = graphgrammar_Symbol89
        self.graphgrammar_Symbol94 = graphgrammar_Symbol94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superscript(self) -> str:
        return self.__superscript

    @superscript.setter
    def superscript(self, superscript: str):
        self.__superscript = superscript

    @property
    def subscript(self) -> str:
        return self.__subscript

    @subscript.setter
    def subscript(self, subscript: str):
        self.__subscript = subscript

    @property
    def graphgrammar_Symbol11(self):
        return self.__graphgrammar_Symbol11

    @graphgrammar_Symbol11.setter
    def graphgrammar_Symbol11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol11", None)
        self.__graphgrammar_Symbol11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Grammar10"):
                opp_val = getattr(old_value, "graphgrammar_Grammar10", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Grammar10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Grammar10"):
                opp_val = getattr(value, "graphgrammar_Grammar10", None)
                setattr(value, "graphgrammar_Grammar10", self)

    @property
    def graphgrammar_Symbol(self):
        return self.__graphgrammar_Symbol

    @graphgrammar_Symbol.setter
    def graphgrammar_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol", None)
        self.__graphgrammar_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Grammar"):
                opp_val = getattr(old_value, "graphgrammar_Grammar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Grammar"):
                opp_val = getattr(value, "graphgrammar_Grammar", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Grammar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol66(self):
        return self.__graphgrammar_Symbol66

    @graphgrammar_Symbol66.setter
    def graphgrammar_Symbol66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol66", None)
        self.__graphgrammar_Symbol66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Vertex65"):
                opp_val = getattr(old_value, "graphgrammar_Vertex65", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Vertex65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Vertex65"):
                opp_val = getattr(value, "graphgrammar_Vertex65", None)
                setattr(value, "graphgrammar_Vertex65", self)

    @property
    def graphgrammar_Symbol22(self):
        return self.__graphgrammar_Symbol22

    @graphgrammar_Symbol22.setter
    def graphgrammar_Symbol22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol22", None)
        self.__graphgrammar_Symbol22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_SymbolSymbolsPair"):
                opp_val = getattr(old_value, "graphgrammar_SymbolSymbolsPair", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_SymbolSymbolsPair", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_SymbolSymbolsPair"):
                opp_val = getattr(value, "graphgrammar_SymbolSymbolsPair", None)
                setattr(value, "graphgrammar_SymbolSymbolsPair", self)

    @property
    def graphgrammar_Symbol89(self):
        return self.__graphgrammar_Symbol89

    @graphgrammar_Symbol89.setter
    def graphgrammar_Symbol89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol89", None)
        self.__graphgrammar_Symbol89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGrammar88"):
                opp_val = getattr(old_value, "graphgrammar_TripleGrammar88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGrammar88"):
                opp_val = getattr(value, "graphgrammar_TripleGrammar88", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_TripleGrammar88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol83(self):
        return self.__graphgrammar_Symbol83

    @graphgrammar_Symbol83.setter
    def graphgrammar_Symbol83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol83", None)
        self.__graphgrammar_Symbol83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGrammar"):
                opp_val = getattr(old_value, "graphgrammar_TripleGrammar", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGrammar"):
                opp_val = getattr(value, "graphgrammar_TripleGrammar", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_TripleGrammar", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol86(self):
        return self.__graphgrammar_Symbol86

    @graphgrammar_Symbol86.setter
    def graphgrammar_Symbol86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol86", None)
        self.__graphgrammar_Symbol86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGrammar85"):
                opp_val = getattr(old_value, "graphgrammar_TripleGrammar85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGrammar85"):
                opp_val = getattr(value, "graphgrammar_TripleGrammar85", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_TripleGrammar85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol14(self):
        return self.__graphgrammar_Symbol14

    @graphgrammar_Symbol14.setter
    def graphgrammar_Symbol14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol14", None)
        self.__graphgrammar_Symbol14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Rule13"):
                opp_val = getattr(old_value, "graphgrammar_Rule13", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Rule13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Rule13"):
                opp_val = getattr(value, "graphgrammar_Rule13", None)
                setattr(value, "graphgrammar_Rule13", self)

    @property
    def graphgrammar_Symbol81(self):
        return self.__graphgrammar_Symbol81

    @graphgrammar_Symbol81.setter
    def graphgrammar_Symbol81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol81", None)
        self.__graphgrammar_Symbol81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Edge80"):
                opp_val = getattr(old_value, "graphgrammar_Edge80", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Edge80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Edge80"):
                opp_val = getattr(value, "graphgrammar_Edge80", None)
                setattr(value, "graphgrammar_Edge80", self)

    @property
    def graphgrammar_Symbol3(self):
        return self.__graphgrammar_Symbol3

    @graphgrammar_Symbol3.setter
    def graphgrammar_Symbol3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol3", None)
        self.__graphgrammar_Symbol3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Grammar2"):
                opp_val = getattr(old_value, "graphgrammar_Grammar2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Grammar2"):
                opp_val = getattr(value, "graphgrammar_Grammar2", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Grammar2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol94(self):
        return self.__graphgrammar_Symbol94

    @graphgrammar_Symbol94.setter
    def graphgrammar_Symbol94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol94", None)
        self.__graphgrammar_Symbol94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleGrammar93"):
                opp_val = getattr(old_value, "graphgrammar_TripleGrammar93", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleGrammar93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleGrammar93"):
                opp_val = getattr(value, "graphgrammar_TripleGrammar93", None)
                setattr(value, "graphgrammar_TripleGrammar93", self)

    @property
    def graphgrammar_Symbol25(self):
        return self.__graphgrammar_Symbol25

    @graphgrammar_Symbol25.setter
    def graphgrammar_Symbol25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol25", None)
        self.__graphgrammar_Symbol25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_SymbolSymbolsPair24"):
                opp_val = getattr(old_value, "graphgrammar_SymbolSymbolsPair24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_SymbolSymbolsPair24"):
                opp_val = getattr(value, "graphgrammar_SymbolSymbolsPair24", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_SymbolSymbolsPair24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Symbol6(self):
        return self.__graphgrammar_Symbol6

    @graphgrammar_Symbol6.setter
    def graphgrammar_Symbol6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Symbol__graphgrammar_Symbol6", None)
        self.__graphgrammar_Symbol6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Grammar5"):
                opp_val = getattr(old_value, "graphgrammar_Grammar5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Grammar5"):
                opp_val = getattr(value, "graphgrammar_Grammar5", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Grammar5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def equivalates(self, other: str) -> bool:
        # TODO: Implement equivalates method
        pass

    def compareTo(self, other: str) -> int:
        # TODO: Implement compareTo method
        pass

class graphgrammar_Grammar:

    def __init__(self, name: str, graphgrammar_Grammar2: set["graphgrammar_Symbol"] = None, graphgrammar_Grammar5: set["graphgrammar_Symbol"] = None, graphgrammar_Grammar8: set["graphgrammar_Rule"] = None, graphgrammar_Grammar10: "graphgrammar_Symbol" = None, graphgrammar_Grammar: set["graphgrammar_Symbol"] = None):
        self.name = name
        self.graphgrammar_Grammar2 = graphgrammar_Grammar2 if graphgrammar_Grammar2 is not None else set()
        self.graphgrammar_Grammar5 = graphgrammar_Grammar5 if graphgrammar_Grammar5 is not None else set()
        self.graphgrammar_Grammar8 = graphgrammar_Grammar8 if graphgrammar_Grammar8 is not None else set()
        self.graphgrammar_Grammar10 = graphgrammar_Grammar10
        self.graphgrammar_Grammar = graphgrammar_Grammar if graphgrammar_Grammar is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphgrammar_Grammar8(self):
        return self.__graphgrammar_Grammar8

    @graphgrammar_Grammar8.setter
    def graphgrammar_Grammar8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Grammar__graphgrammar_Grammar8", None)
        self.__graphgrammar_Grammar8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Rule"):
                    opp_val = getattr(item, "graphgrammar_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Rule"):
                    opp_val = getattr(item, "graphgrammar_Rule", None)
                    
                    setattr(item, "graphgrammar_Rule", self)
                    

    @property
    def graphgrammar_Grammar2(self):
        return self.__graphgrammar_Grammar2

    @graphgrammar_Grammar2.setter
    def graphgrammar_Grammar2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Grammar__graphgrammar_Grammar2", None)
        self.__graphgrammar_Grammar2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol3"):
                    opp_val = getattr(item, "graphgrammar_Symbol3", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol3"):
                    opp_val = getattr(item, "graphgrammar_Symbol3", None)
                    
                    setattr(item, "graphgrammar_Symbol3", self)
                    

    @property
    def graphgrammar_Grammar(self):
        return self.__graphgrammar_Grammar

    @graphgrammar_Grammar.setter
    def graphgrammar_Grammar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Grammar__graphgrammar_Grammar", None)
        self.__graphgrammar_Grammar = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol"):
                    opp_val = getattr(item, "graphgrammar_Symbol", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol"):
                    opp_val = getattr(item, "graphgrammar_Symbol", None)
                    
                    setattr(item, "graphgrammar_Symbol", self)
                    

    @property
    def graphgrammar_Grammar5(self):
        return self.__graphgrammar_Grammar5

    @graphgrammar_Grammar5.setter
    def graphgrammar_Grammar5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Grammar__graphgrammar_Grammar5", None)
        self.__graphgrammar_Grammar5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Symbol6"):
                    opp_val = getattr(item, "graphgrammar_Symbol6", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Symbol6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Symbol6"):
                    opp_val = getattr(item, "graphgrammar_Symbol6", None)
                    
                    setattr(item, "graphgrammar_Symbol6", self)
                    

    @property
    def graphgrammar_Grammar10(self):
        return self.__graphgrammar_Grammar10

    @graphgrammar_Grammar10.setter
    def graphgrammar_Grammar10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Grammar__graphgrammar_Grammar10", None)
        self.__graphgrammar_Grammar10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Symbol11"):
                opp_val = getattr(old_value, "graphgrammar_Symbol11", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Symbol11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Symbol11"):
                opp_val = getattr(value, "graphgrammar_Symbol11", None)
                setattr(value, "graphgrammar_Symbol11", self)

    def derives(self, vertex: str, next: str, rhs: str, prev: str) -> str:
        # TODO: Implement derives method
        pass

class graphgrammar_Rule:

    def __init__(self, id: str, name: str, graphgrammar_Rule: "graphgrammar_Grammar" = None, graphgrammar_Rule16: "graphgrammar_Graph" = None, graphgrammar_Rule18: set["graphgrammar_VertexToSymbolSymbolsPairMap"] = None, graphgrammar_Rule13: "graphgrammar_Symbol" = None, graphgrammar_Rule20: set["graphgrammar_Vertex"] = None, graphgrammar_Rule33: "graphgrammar_DerivationStep" = None, graphgrammar_Rule97: "graphgrammar_TripleRule" = None, graphgrammar_Rule100: "graphgrammar_TripleRule" = None, graphgrammar_Rule103: "graphgrammar_TripleRule" = None):
        self.id = id
        self.name = name
        self.graphgrammar_Rule = graphgrammar_Rule
        self.graphgrammar_Rule16 = graphgrammar_Rule16
        self.graphgrammar_Rule18 = graphgrammar_Rule18 if graphgrammar_Rule18 is not None else set()
        self.graphgrammar_Rule13 = graphgrammar_Rule13
        self.graphgrammar_Rule20 = graphgrammar_Rule20 if graphgrammar_Rule20 is not None else set()
        self.graphgrammar_Rule33 = graphgrammar_Rule33
        self.graphgrammar_Rule97 = graphgrammar_Rule97
        self.graphgrammar_Rule100 = graphgrammar_Rule100
        self.graphgrammar_Rule103 = graphgrammar_Rule103
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def graphgrammar_Rule97(self):
        return self.__graphgrammar_Rule97

    @graphgrammar_Rule97.setter
    def graphgrammar_Rule97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule97", None)
        self.__graphgrammar_Rule97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleRule96"):
                opp_val = getattr(old_value, "graphgrammar_TripleRule96", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleRule96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleRule96"):
                opp_val = getattr(value, "graphgrammar_TripleRule96", None)
                setattr(value, "graphgrammar_TripleRule96", self)

    @property
    def graphgrammar_Rule33(self):
        return self.__graphgrammar_Rule33

    @graphgrammar_Rule33.setter
    def graphgrammar_Rule33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule33", None)
        self.__graphgrammar_Rule33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_DerivationStep"):
                opp_val = getattr(old_value, "graphgrammar_DerivationStep", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_DerivationStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_DerivationStep"):
                opp_val = getattr(value, "graphgrammar_DerivationStep", None)
                setattr(value, "graphgrammar_DerivationStep", self)

    @property
    def graphgrammar_Rule13(self):
        return self.__graphgrammar_Rule13

    @graphgrammar_Rule13.setter
    def graphgrammar_Rule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule13", None)
        self.__graphgrammar_Rule13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Symbol14"):
                opp_val = getattr(old_value, "graphgrammar_Symbol14", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Symbol14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Symbol14"):
                opp_val = getattr(value, "graphgrammar_Symbol14", None)
                setattr(value, "graphgrammar_Symbol14", self)

    @property
    def graphgrammar_Rule18(self):
        return self.__graphgrammar_Rule18

    @graphgrammar_Rule18.setter
    def graphgrammar_Rule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule18", None)
        self.__graphgrammar_Rule18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap"):
                    opp_val = getattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap"):
                    opp_val = getattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap", None)
                    
                    setattr(item, "graphgrammar_VertexToSymbolSymbolsPairMap", self)
                    

    @property
    def graphgrammar_Rule103(self):
        return self.__graphgrammar_Rule103

    @graphgrammar_Rule103.setter
    def graphgrammar_Rule103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule103", None)
        self.__graphgrammar_Rule103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleRule102"):
                opp_val = getattr(old_value, "graphgrammar_TripleRule102", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleRule102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleRule102"):
                opp_val = getattr(value, "graphgrammar_TripleRule102", None)
                setattr(value, "graphgrammar_TripleRule102", self)

    @property
    def graphgrammar_Rule100(self):
        return self.__graphgrammar_Rule100

    @graphgrammar_Rule100.setter
    def graphgrammar_Rule100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule100", None)
        self.__graphgrammar_Rule100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_TripleRule99"):
                opp_val = getattr(old_value, "graphgrammar_TripleRule99", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_TripleRule99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_TripleRule99"):
                opp_val = getattr(value, "graphgrammar_TripleRule99", None)
                setattr(value, "graphgrammar_TripleRule99", self)

    @property
    def graphgrammar_Rule(self):
        return self.__graphgrammar_Rule

    @graphgrammar_Rule.setter
    def graphgrammar_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule", None)
        self.__graphgrammar_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Grammar8"):
                opp_val = getattr(old_value, "graphgrammar_Grammar8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Grammar8"):
                opp_val = getattr(value, "graphgrammar_Grammar8", None)
                if opp_val is None:
                    setattr(value, "graphgrammar_Grammar8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphgrammar_Rule16(self):
        return self.__graphgrammar_Rule16

    @graphgrammar_Rule16.setter
    def graphgrammar_Rule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule16", None)
        self.__graphgrammar_Rule16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphgrammar_Graph"):
                opp_val = getattr(old_value, "graphgrammar_Graph", None)
                if opp_val == self:
                    setattr(old_value, "graphgrammar_Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphgrammar_Graph"):
                opp_val = getattr(value, "graphgrammar_Graph", None)
                setattr(value, "graphgrammar_Graph", self)

    @property
    def graphgrammar_Rule20(self):
        return self.__graphgrammar_Rule20

    @graphgrammar_Rule20.setter
    def graphgrammar_Rule20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphgrammar_Rule__graphgrammar_Rule20", None)
        self.__graphgrammar_Rule20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphgrammar_Vertex"):
                    opp_val = getattr(item, "graphgrammar_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "graphgrammar_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphgrammar_Vertex"):
                    opp_val = getattr(item, "graphgrammar_Vertex", None)
                    
                    setattr(item, "graphgrammar_Vertex", self)
                    

    def apply(self, vertex: str, graph: str, pacs: bool) -> str:
        # TODO: Implement apply method
        pass

    def derive(self, vertex: str, graph: str) -> str:
        # TODO: Implement derive method
        pass

    def embed(self, edges: str, vertex: str, pacs: bool, graph: str, unifier: str) -> str:
        # TODO: Implement embed method
        pass
