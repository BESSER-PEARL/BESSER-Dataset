from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class atomic_ATargetEdge:

    pass
class XAnnotable:

    pass
class atomic_ANode(XAnnotable):

    pass
class ANode:

    pass
class atomic_XAnnotable(ABC):

    pass
class atomic_AEdge:

    pass
class atomic_AStructured(ANode):

    pass
class atomic_AToken(ANode):

    def __init__(self, text: str, AToken: "atomic_AGraph" = None, AToken7: "atomic_AToken" = None, previous: "atomic_AToken" = None, AToken10: "atomic_AToken" = None, next: "atomic_AToken" = None, tokens: "atomic_AGraph" = None):
        self.text = text
        self.AToken = AToken
        self.AToken7 = AToken7
        self.previous = previous
        self.AToken10 = AToken10
        self.next = next
        self.tokens = tokens
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def AToken(self):
        return self.__AToken

    @AToken.setter
    def AToken(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__AToken", None)
        self.__AToken = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AToken10(self):
        return self.__AToken10

    @AToken10.setter
    def AToken10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__AToken10", None)
        self.__AToken10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "next"):
                opp_val = getattr(old_value, "next", None)
                if opp_val == self:
                    setattr(old_value, "next", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "next"):
                opp_val = getattr(value, "next", None)
                setattr(value, "next", self)

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__previous", None)
        self.__previous = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AToken7"):
                opp_val = getattr(old_value, "AToken7", None)
                if opp_val == self:
                    setattr(old_value, "AToken7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AToken7"):
                opp_val = getattr(value, "AToken7", None)
                setattr(value, "AToken7", self)

    @property
    def AToken7(self):
        return self.__AToken7

    @AToken7.setter
    def AToken7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__AToken7", None)
        self.__AToken7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "previous"):
                opp_val = getattr(old_value, "previous", None)
                if opp_val == self:
                    setattr(old_value, "previous", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "previous"):
                opp_val = getattr(value, "previous", None)
                setattr(value, "previous", self)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__next", None)
        self.__next = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AToken10"):
                opp_val = getattr(old_value, "AToken10", None)
                if opp_val == self:
                    setattr(old_value, "AToken10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AToken10"):
                opp_val = getattr(value, "AToken10", None)
                setattr(value, "AToken10", self)

    @property
    def tokens(self):
        return self.__tokens

    @tokens.setter
    def tokens(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AToken__tokens", None)
        self.__tokens = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AGraph"):
                opp_val = getattr(old_value, "AGraph", None)
                if opp_val == self:
                    setattr(old_value, "AGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AGraph"):
                opp_val = getattr(value, "AGraph", None)
                setattr(value, "AGraph", self)

class atomic_AGraph:

    def __init__(self, corpus: str, graph: set["atomic_AToken"] = None, graph2: set["atomic_AStructured"] = None, graph4: set["atomic_AEdge"] = None, AGraph14: "atomic_AStructured" = None, AGraph16: "atomic_AEdge" = None, atomic_AGraph: "atomic_ATargetEdge" = None, AGraph: "atomic_AToken" = None):
        self.corpus = corpus
        self.graph = graph if graph is not None else set()
        self.graph2 = graph2 if graph2 is not None else set()
        self.graph4 = graph4 if graph4 is not None else set()
        self.AGraph14 = AGraph14
        self.AGraph16 = AGraph16
        self.atomic_AGraph = atomic_AGraph
        self.AGraph = AGraph
        
    @property
    def corpus(self) -> str:
        return self.__corpus

    @corpus.setter
    def corpus(self, corpus: str):
        self.__corpus = corpus

    @property
    def graph4(self):
        return self.__graph4

    @graph4.setter
    def graph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__graph4", None)
        self.__graph4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AEdge"):
                    opp_val = getattr(item, "AEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "AEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AEdge"):
                    opp_val = getattr(item, "AEdge", None)
                    
                    setattr(item, "AEdge", self)
                    

    @property
    def AGraph(self):
        return self.__AGraph

    @AGraph.setter
    def AGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__AGraph", None)
        self.__AGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tokens"):
                opp_val = getattr(old_value, "tokens", None)
                if opp_val == self:
                    setattr(old_value, "tokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tokens"):
                opp_val = getattr(value, "tokens", None)
                setattr(value, "tokens", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AToken"):
                    opp_val = getattr(item, "AToken", None)
                    
                    if opp_val == self:
                        setattr(item, "AToken", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AToken"):
                    opp_val = getattr(item, "AToken", None)
                    
                    setattr(item, "AToken", self)
                    

    @property
    def AGraph14(self):
        return self.__AGraph14

    @AGraph14.setter
    def AGraph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__AGraph14", None)
        self.__AGraph14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structures"):
                opp_val = getattr(old_value, "structures", None)
                if opp_val == self:
                    setattr(old_value, "structures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structures"):
                opp_val = getattr(value, "structures", None)
                setattr(value, "structures", self)

    @property
    def AGraph16(self):
        return self.__AGraph16

    @AGraph16.setter
    def AGraph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__AGraph16", None)
        self.__AGraph16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def atomic_AGraph(self):
        return self.__atomic_AGraph

    @atomic_AGraph.setter
    def atomic_AGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__atomic_AGraph", None)
        self.__atomic_AGraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atomic_ATargetEdge26"):
                opp_val = getattr(old_value, "atomic_ATargetEdge26", None)
                if opp_val == self:
                    setattr(old_value, "atomic_ATargetEdge26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atomic_ATargetEdge26"):
                opp_val = getattr(value, "atomic_ATargetEdge26", None)
                setattr(value, "atomic_ATargetEdge26", self)

    @property
    def graph2(self):
        return self.__graph2

    @graph2.setter
    def graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atomic_AGraph__graph2", None)
        self.__graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AStructured"):
                    opp_val = getattr(item, "AStructured", None)
                    
                    if opp_val == self:
                        setattr(item, "AStructured", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AStructured"):
                    opp_val = getattr(item, "AStructured", None)
                    
                    setattr(item, "AStructured", self)
                    
