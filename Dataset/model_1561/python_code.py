from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EdgeLabel:

    pass
class graph_SanityChecker(ABC):

    pass
class graph_URIToIdentifiableMapEntry:

    def __init__(self, key: str, graph_URIToIdentifiableMapEntry: "graph_Identifiable" = None):
        self.key = key
        self.graph_URIToIdentifiableMapEntry = graph_URIToIdentifiableMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_URIToIdentifiableMapEntry(self):
        return self.__graph_URIToIdentifiableMapEntry

    @graph_URIToIdentifiableMapEntry.setter
    def graph_URIToIdentifiableMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToIdentifiableMapEntry__graph_URIToIdentifiableMapEntry", None)
        self.__graph_URIToIdentifiableMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable45"):
                opp_val = getattr(old_value, "graph_Identifiable45", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable45"):
                opp_val = getattr(value, "graph_Identifiable45", None)
                setattr(value, "graph_Identifiable45", self)

class SanityChecker:

    pass
class graph_Identifiable:

    pass
class StaticLabel:

    pass
class graph_StaticEdgeLabel(EdgeLabel, StaticLabel):

    pass
class graph_UnresolvedIdentifiable:

    def __init__(self, unresolvedURI: str, fieldName: str, graph_UnresolvedIdentifiable: "graph_Graph" = None, graph_UnresolvedIdentifiable33: "graph_Identifiable" = None, graph_UnresolvedIdentifiable36: "graph_Identifiable" = None, graph_UnresolvedIdentifiable39: "graph_Identifiable" = None, graph_UnresolvedIdentifiable42: "graph_Identifiable" = None):
        self.unresolvedURI = unresolvedURI
        self.fieldName = fieldName
        self.graph_UnresolvedIdentifiable = graph_UnresolvedIdentifiable
        self.graph_UnresolvedIdentifiable33 = graph_UnresolvedIdentifiable33
        self.graph_UnresolvedIdentifiable36 = graph_UnresolvedIdentifiable36
        self.graph_UnresolvedIdentifiable39 = graph_UnresolvedIdentifiable39
        self.graph_UnresolvedIdentifiable42 = graph_UnresolvedIdentifiable42
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def unresolvedURI(self) -> str:
        return self.__unresolvedURI

    @unresolvedURI.setter
    def unresolvedURI(self, unresolvedURI: str):
        self.__unresolvedURI = unresolvedURI

    @property
    def graph_UnresolvedIdentifiable(self):
        return self.__graph_UnresolvedIdentifiable

    @graph_UnresolvedIdentifiable.setter
    def graph_UnresolvedIdentifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_UnresolvedIdentifiable__graph_UnresolvedIdentifiable", None)
        self.__graph_UnresolvedIdentifiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph18"):
                opp_val = getattr(old_value, "graph_Graph18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph18"):
                opp_val = getattr(value, "graph_Graph18", None)
                if opp_val is None:
                    setattr(value, "graph_Graph18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_UnresolvedIdentifiable33(self):
        return self.__graph_UnresolvedIdentifiable33

    @graph_UnresolvedIdentifiable33.setter
    def graph_UnresolvedIdentifiable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_UnresolvedIdentifiable__graph_UnresolvedIdentifiable33", None)
        self.__graph_UnresolvedIdentifiable33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable34"):
                opp_val = getattr(old_value, "graph_Identifiable34", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable34"):
                opp_val = getattr(value, "graph_Identifiable34", None)
                setattr(value, "graph_Identifiable34", self)

    @property
    def graph_UnresolvedIdentifiable36(self):
        return self.__graph_UnresolvedIdentifiable36

    @graph_UnresolvedIdentifiable36.setter
    def graph_UnresolvedIdentifiable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_UnresolvedIdentifiable__graph_UnresolvedIdentifiable36", None)
        self.__graph_UnresolvedIdentifiable36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable37"):
                opp_val = getattr(old_value, "graph_Identifiable37", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable37"):
                opp_val = getattr(value, "graph_Identifiable37", None)
                setattr(value, "graph_Identifiable37", self)

    @property
    def graph_UnresolvedIdentifiable42(self):
        return self.__graph_UnresolvedIdentifiable42

    @graph_UnresolvedIdentifiable42.setter
    def graph_UnresolvedIdentifiable42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_UnresolvedIdentifiable__graph_UnresolvedIdentifiable42", None)
        self.__graph_UnresolvedIdentifiable42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable43"):
                opp_val = getattr(old_value, "graph_Identifiable43", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable43"):
                opp_val = getattr(value, "graph_Identifiable43", None)
                setattr(value, "graph_Identifiable43", self)

    @property
    def graph_UnresolvedIdentifiable39(self):
        return self.__graph_UnresolvedIdentifiable39

    @graph_UnresolvedIdentifiable39.setter
    def graph_UnresolvedIdentifiable39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_UnresolvedIdentifiable__graph_UnresolvedIdentifiable39", None)
        self.__graph_UnresolvedIdentifiable39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable40"):
                opp_val = getattr(old_value, "graph_Identifiable40", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable40"):
                opp_val = getattr(value, "graph_Identifiable40", None)
                setattr(value, "graph_Identifiable40", self)

class graph_URIToNodeLabelMapEntry:

    def __init__(self, key: str, graph_URIToNodeLabelMapEntry: "graph_Graph" = None, graph_URIToNodeLabelMapEntry57: "graph_NodeLabel" = None):
        self.key = key
        self.graph_URIToNodeLabelMapEntry = graph_URIToNodeLabelMapEntry
        self.graph_URIToNodeLabelMapEntry57 = graph_URIToNodeLabelMapEntry57
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_URIToNodeLabelMapEntry(self):
        return self.__graph_URIToNodeLabelMapEntry

    @graph_URIToNodeLabelMapEntry.setter
    def graph_URIToNodeLabelMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToNodeLabelMapEntry__graph_URIToNodeLabelMapEntry", None)
        self.__graph_URIToNodeLabelMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph13"):
                opp_val = getattr(old_value, "graph_Graph13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph13"):
                opp_val = getattr(value, "graph_Graph13", None)
                if opp_val is None:
                    setattr(value, "graph_Graph13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_URIToNodeLabelMapEntry57(self):
        return self.__graph_URIToNodeLabelMapEntry57

    @graph_URIToNodeLabelMapEntry57.setter
    def graph_URIToNodeLabelMapEntry57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToNodeLabelMapEntry__graph_URIToNodeLabelMapEntry57", None)
        self.__graph_URIToNodeLabelMapEntry57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_NodeLabel"):
                opp_val = getattr(old_value, "graph_NodeLabel", None)
                if opp_val == self:
                    setattr(old_value, "graph_NodeLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_NodeLabel"):
                opp_val = getattr(value, "graph_NodeLabel", None)
                setattr(value, "graph_NodeLabel", self)

class graph_URIToLabelMapEntry:

    def __init__(self, key: str, graph_URIToLabelMapEntry: "graph_Graph" = None, graph_URIToLabelMapEntry54: "graph_Label" = None):
        self.key = key
        self.graph_URIToLabelMapEntry = graph_URIToLabelMapEntry
        self.graph_URIToLabelMapEntry54 = graph_URIToLabelMapEntry54
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_URIToLabelMapEntry(self):
        return self.__graph_URIToLabelMapEntry

    @graph_URIToLabelMapEntry.setter
    def graph_URIToLabelMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToLabelMapEntry__graph_URIToLabelMapEntry", None)
        self.__graph_URIToLabelMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph11"):
                opp_val = getattr(old_value, "graph_Graph11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph11"):
                opp_val = getattr(value, "graph_Graph11", None)
                if opp_val is None:
                    setattr(value, "graph_Graph11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_URIToLabelMapEntry54(self):
        return self.__graph_URIToLabelMapEntry54

    @graph_URIToLabelMapEntry54.setter
    def graph_URIToLabelMapEntry54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToLabelMapEntry__graph_URIToLabelMapEntry54", None)
        self.__graph_URIToLabelMapEntry54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Label55"):
                opp_val = getattr(old_value, "graph_Label55", None)
                if opp_val == self:
                    setattr(old_value, "graph_Label55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Label55"):
                opp_val = getattr(value, "graph_Label55", None)
                setattr(value, "graph_Label55", self)

class graph_STEMTime:

    pass
class graph_URIToNodeMapEntry:

    def __init__(self, key: str, graph_URIToNodeMapEntry: "graph_Graph" = None, graph_URIToNodeMapEntry51: "graph_Node" = None):
        self.key = key
        self.graph_URIToNodeMapEntry = graph_URIToNodeMapEntry
        self.graph_URIToNodeMapEntry51 = graph_URIToNodeMapEntry51
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_URIToNodeMapEntry(self):
        return self.__graph_URIToNodeMapEntry

    @graph_URIToNodeMapEntry.setter
    def graph_URIToNodeMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToNodeMapEntry__graph_URIToNodeMapEntry", None)
        self.__graph_URIToNodeMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph9"):
                opp_val = getattr(old_value, "graph_Graph9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph9"):
                opp_val = getattr(value, "graph_Graph9", None)
                if opp_val is None:
                    setattr(value, "graph_Graph9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_URIToNodeMapEntry51(self):
        return self.__graph_URIToNodeMapEntry51

    @graph_URIToNodeMapEntry51.setter
    def graph_URIToNodeMapEntry51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToNodeMapEntry__graph_URIToNodeMapEntry51", None)
        self.__graph_URIToNodeMapEntry51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node52"):
                opp_val = getattr(old_value, "graph_Node52", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node52"):
                opp_val = getattr(value, "graph_Node52", None)
                setattr(value, "graph_Node52", self)

class graph_URIToEdgeMapEntry:

    def __init__(self, key: str, graph_URIToEdgeMapEntry: "graph_Graph" = None, graph_URIToEdgeMapEntry48: "graph_Edge" = None):
        self.key = key
        self.graph_URIToEdgeMapEntry = graph_URIToEdgeMapEntry
        self.graph_URIToEdgeMapEntry48 = graph_URIToEdgeMapEntry48
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_URIToEdgeMapEntry48(self):
        return self.__graph_URIToEdgeMapEntry48

    @graph_URIToEdgeMapEntry48.setter
    def graph_URIToEdgeMapEntry48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToEdgeMapEntry__graph_URIToEdgeMapEntry48", None)
        self.__graph_URIToEdgeMapEntry48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge49"):
                opp_val = getattr(old_value, "graph_Edge49", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge49"):
                opp_val = getattr(value, "graph_Edge49", None)
                setattr(value, "graph_Edge49", self)

    @property
    def graph_URIToEdgeMapEntry(self):
        return self.__graph_URIToEdgeMapEntry

    @graph_URIToEdgeMapEntry.setter
    def graph_URIToEdgeMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_URIToEdgeMapEntry__graph_URIToEdgeMapEntry", None)
        self.__graph_URIToEdgeMapEntry = value
        
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

class Modifiable:

    pass
class Identifiable:

    pass
class graph_Node(Identifiable):

    pass
class graph_Label(Identifiable):

    def __init__(self, uRIOfIdentifiableToBeLabeled: str, graph_Label: "graph_LabelValue" = None, graph_Label26: "graph_Identifiable" = None, graph_Label55: "graph_URIToLabelMapEntry" = None):
        self.uRIOfIdentifiableToBeLabeled = uRIOfIdentifiableToBeLabeled
        self.graph_Label = graph_Label
        self.graph_Label26 = graph_Label26
        self.graph_Label55 = graph_Label55
        
    @property
    def uRIOfIdentifiableToBeLabeled(self) -> str:
        return self.__uRIOfIdentifiableToBeLabeled

    @uRIOfIdentifiableToBeLabeled.setter
    def uRIOfIdentifiableToBeLabeled(self, uRIOfIdentifiableToBeLabeled: str):
        self.__uRIOfIdentifiableToBeLabeled = uRIOfIdentifiableToBeLabeled

    @property
    def graph_Label(self):
        return self.__graph_Label

    @graph_Label.setter
    def graph_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Label__graph_Label", None)
        self.__graph_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_LabelValue24"):
                opp_val = getattr(old_value, "graph_LabelValue24", None)
                if opp_val == self:
                    setattr(old_value, "graph_LabelValue24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_LabelValue24"):
                opp_val = getattr(value, "graph_LabelValue24", None)
                setattr(value, "graph_LabelValue24", self)

    @property
    def graph_Label55(self):
        return self.__graph_Label55

    @graph_Label55.setter
    def graph_Label55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Label__graph_Label55", None)
        self.__graph_Label55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_URIToLabelMapEntry54"):
                opp_val = getattr(old_value, "graph_URIToLabelMapEntry54", None)
                if opp_val == self:
                    setattr(old_value, "graph_URIToLabelMapEntry54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_URIToLabelMapEntry54"):
                opp_val = getattr(value, "graph_URIToLabelMapEntry54", None)
                setattr(value, "graph_URIToLabelMapEntry54", self)

    @property
    def graph_Label26(self):
        return self.__graph_Label26

    @graph_Label26.setter
    def graph_Label26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Label__graph_Label26", None)
        self.__graph_Label26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Identifiable"):
                opp_val = getattr(old_value, "graph_Identifiable", None)
                if opp_val == self:
                    setattr(old_value, "graph_Identifiable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Identifiable"):
                opp_val = getattr(value, "graph_Identifiable", None)
                setattr(value, "graph_Identifiable", self)

class graph_Edge(Identifiable, Modifiable):

    def __init__(self, nodeBURI: str, directed: bool, nodeAURI: str, edge: "graph_EdgeLabel" = None, graph_Edge: "graph_Node" = None, graph_Edge4: "graph_Node" = None, graph_Edge29: "graph_Node" = None, graph_Edge49: "graph_URIToEdgeMapEntry" = None, Edge: "graph_EdgeLabel" = None):
        self.nodeBURI = nodeBURI
        self.directed = directed
        self.nodeAURI = nodeAURI
        self.edge = edge
        self.graph_Edge = graph_Edge
        self.graph_Edge4 = graph_Edge4
        self.graph_Edge29 = graph_Edge29
        self.graph_Edge49 = graph_Edge49
        self.Edge = Edge
        
    @property
    def directed(self) -> bool:
        return self.__directed

    @directed.setter
    def directed(self, directed: bool):
        self.__directed = directed

    @property
    def nodeAURI(self) -> str:
        return self.__nodeAURI

    @nodeAURI.setter
    def nodeAURI(self, nodeAURI: str):
        self.__nodeAURI = nodeAURI

    @property
    def nodeBURI(self) -> str:
        return self.__nodeBURI

    @nodeBURI.setter
    def nodeBURI(self, nodeBURI: str):
        self.__nodeBURI = nodeBURI

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
            if hasattr(old_value, "label"):
                opp_val = getattr(old_value, "label", None)
                if opp_val == self:
                    setattr(old_value, "label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "label"):
                opp_val = getattr(value, "label", None)
                setattr(value, "label", self)

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__edge", None)
        self.__edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeLabel"):
                opp_val = getattr(old_value, "EdgeLabel", None)
                if opp_val == self:
                    setattr(old_value, "EdgeLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeLabel"):
                opp_val = getattr(value, "EdgeLabel", None)
                setattr(value, "EdgeLabel", self)

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
    def graph_Edge49(self):
        return self.__graph_Edge49

    @graph_Edge49.setter
    def graph_Edge49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge49", None)
        self.__graph_Edge49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_URIToEdgeMapEntry48"):
                opp_val = getattr(old_value, "graph_URIToEdgeMapEntry48", None)
                if opp_val == self:
                    setattr(old_value, "graph_URIToEdgeMapEntry48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_URIToEdgeMapEntry48"):
                opp_val = getattr(value, "graph_URIToEdgeMapEntry48", None)
                setattr(value, "graph_URIToEdgeMapEntry48", self)

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
            if hasattr(old_value, "graph_Node"):
                opp_val = getattr(old_value, "graph_Node", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node"):
                opp_val = getattr(value, "graph_Node", None)
                setattr(value, "graph_Node", self)

    @property
    def graph_Edge29(self):
        return self.__graph_Edge29

    @graph_Edge29.setter
    def graph_Edge29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge29", None)
        self.__graph_Edge29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node28"):
                opp_val = getattr(old_value, "graph_Node28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node28"):
                opp_val = getattr(value, "graph_Node28", None)
                if opp_val is None:
                    setattr(value, "graph_Node28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getOtherNode(self, node: str) -> str:
        # TODO: Implement getOtherNode method
        pass

    def isDirectedAt(self, node: str) -> bool:
        # TODO: Implement isDirectedAt method
        pass

class NodeLabel:

    pass
class graph_StaticNodeLabel(NodeLabel, StaticLabel):

    pass
class DynamicLabel:

    pass
class graph_DynamicEdgeLabel(EdgeLabel, DynamicLabel):

    pass
class graph_DynamicNodeLabel(NodeLabel, DynamicLabel):

    pass
class graph_Decorator:

    pass
class graph_Graph(Identifiable):

    def __init__(self, numEdges: int, numNodes: int, numGraphLabels: int, numNodeLabels: int, numDynamicLabels: int, graph_Graph: set["graph_URIToEdgeMapEntry"] = None, graph_Graph9: set["graph_URIToNodeMapEntry"] = None, graph: set["graph_Decorator"] = None, graph_Graph22: "graph_STEMTime" = None, graph_Graph11: set["graph_URIToLabelMapEntry"] = None, graph_Graph13: set["graph_URIToNodeLabelMapEntry"] = None, graph_Graph15: set["graph_DynamicLabel"] = None, graph_Graph18: set["graph_UnresolvedIdentifiable"] = None):
        self.numEdges = numEdges
        self.numNodes = numNodes
        self.numGraphLabels = numGraphLabels
        self.numNodeLabels = numNodeLabels
        self.numDynamicLabels = numDynamicLabels
        self.graph_Graph = graph_Graph if graph_Graph is not None else set()
        self.graph_Graph9 = graph_Graph9 if graph_Graph9 is not None else set()
        self.graph = graph if graph is not None else set()
        self.graph_Graph22 = graph_Graph22
        self.graph_Graph11 = graph_Graph11 if graph_Graph11 is not None else set()
        self.graph_Graph13 = graph_Graph13 if graph_Graph13 is not None else set()
        self.graph_Graph15 = graph_Graph15 if graph_Graph15 is not None else set()
        self.graph_Graph18 = graph_Graph18 if graph_Graph18 is not None else set()
        
    @property
    def numDynamicLabels(self) -> int:
        return self.__numDynamicLabels

    @numDynamicLabels.setter
    def numDynamicLabels(self, numDynamicLabels: int):
        self.__numDynamicLabels = numDynamicLabels

    @property
    def numGraphLabels(self) -> int:
        return self.__numGraphLabels

    @numGraphLabels.setter
    def numGraphLabels(self, numGraphLabels: int):
        self.__numGraphLabels = numGraphLabels

    @property
    def numNodeLabels(self) -> int:
        return self.__numNodeLabels

    @numNodeLabels.setter
    def numNodeLabels(self, numNodeLabels: int):
        self.__numNodeLabels = numNodeLabels

    @property
    def numEdges(self) -> int:
        return self.__numEdges

    @numEdges.setter
    def numEdges(self, numEdges: int):
        self.__numEdges = numEdges

    @property
    def numNodes(self) -> int:
        return self.__numNodes

    @numNodes.setter
    def numNodes(self, numNodes: int):
        self.__numNodes = numNodes

    @property
    def graph_Graph18(self):
        return self.__graph_Graph18

    @graph_Graph18.setter
    def graph_Graph18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph18", None)
        self.__graph_Graph18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_UnresolvedIdentifiable"):
                    opp_val = getattr(item, "graph_UnresolvedIdentifiable", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_UnresolvedIdentifiable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_UnresolvedIdentifiable"):
                    opp_val = getattr(item, "graph_UnresolvedIdentifiable", None)
                    
                    setattr(item, "graph_UnresolvedIdentifiable", self)
                    

    @property
    def graph_Graph15(self):
        return self.__graph_Graph15

    @graph_Graph15.setter
    def graph_Graph15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph15", None)
        self.__graph_Graph15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_DynamicLabel16"):
                    opp_val = getattr(item, "graph_DynamicLabel16", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_DynamicLabel16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_DynamicLabel16"):
                    opp_val = getattr(item, "graph_DynamicLabel16", None)
                    
                    setattr(item, "graph_DynamicLabel16", self)
                    

    @property
    def graph_Graph9(self):
        return self.__graph_Graph9

    @graph_Graph9.setter
    def graph_Graph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph9", None)
        self.__graph_Graph9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_URIToNodeMapEntry"):
                    opp_val = getattr(item, "graph_URIToNodeMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_URIToNodeMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_URIToNodeMapEntry"):
                    opp_val = getattr(item, "graph_URIToNodeMapEntry", None)
                    
                    setattr(item, "graph_URIToNodeMapEntry", self)
                    

    @property
    def graph_Graph13(self):
        return self.__graph_Graph13

    @graph_Graph13.setter
    def graph_Graph13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph13", None)
        self.__graph_Graph13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_URIToNodeLabelMapEntry"):
                    opp_val = getattr(item, "graph_URIToNodeLabelMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_URIToNodeLabelMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_URIToNodeLabelMapEntry"):
                    opp_val = getattr(item, "graph_URIToNodeLabelMapEntry", None)
                    
                    setattr(item, "graph_URIToNodeLabelMapEntry", self)
                    

    @property
    def graph_Graph11(self):
        return self.__graph_Graph11

    @graph_Graph11.setter
    def graph_Graph11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph11", None)
        self.__graph_Graph11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_URIToLabelMapEntry"):
                    opp_val = getattr(item, "graph_URIToLabelMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_URIToLabelMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_URIToLabelMapEntry"):
                    opp_val = getattr(item, "graph_URIToLabelMapEntry", None)
                    
                    setattr(item, "graph_URIToLabelMapEntry", self)
                    

    @property
    def graph_Graph22(self):
        return self.__graph_Graph22

    @graph_Graph22.setter
    def graph_Graph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph22", None)
        self.__graph_Graph22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_STEMTime"):
                opp_val = getattr(old_value, "graph_STEMTime", None)
                if opp_val == self:
                    setattr(old_value, "graph_STEMTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_STEMTime"):
                opp_val = getattr(value, "graph_STEMTime", None)
                setattr(value, "graph_STEMTime", self)

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
                if hasattr(item, "graph_URIToEdgeMapEntry"):
                    opp_val = getattr(item, "graph_URIToEdgeMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_URIToEdgeMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_URIToEdgeMapEntry"):
                    opp_val = getattr(item, "graph_URIToEdgeMapEntry", None)
                    
                    setattr(item, "graph_URIToEdgeMapEntry", self)
                    

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model.ecoreDecorator20"):
                    opp_val = getattr(item, "model.ecoreDecorator20", None)
                    
                    if opp_val == self:
                        setattr(item, "model.ecoreDecorator20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model.ecoreDecorator20"):
                    opp_val = getattr(item, "model.ecoreDecorator20", None)
                    
                    setattr(item, "model.ecoreDecorator20", self)
                    

    def putNode(self, node: str):
        # TODO: Implement putNode method
        pass

    def getEdge(self, uri: str) -> str:
        # TODO: Implement getEdge method
        pass

    def addDynamicLabel(self, dynamiclabel: DynamicLabel):
        # TODO: Implement addDynamicLabel method
        pass

    def getNodeLabelsByTypeURI(self, typeURI: str) -> NodeLabel:
        # TODO: Implement getNodeLabelsByTypeURI method
        pass

    def putGraphLabel(self, label: Label):
        # TODO: Implement putGraphLabel method
        pass

    def getGraphLabel(self, uri: str) -> Label:
        # TODO: Implement getGraphLabel method
        pass

    def switchToNextValue(self, currentTime: str):
        # TODO: Implement switchToNextValue method
        pass

    def getNode(self, uri: str) -> str:
        # TODO: Implement getNode method
        pass

    def getNodeLabel(self, uri: str) -> NodeLabel:
        # TODO: Implement getNodeLabel method
        pass

    def addGraph(self, filter: str, graph: str):
        # TODO: Implement addGraph method
        pass

    def putEdge(self, edge: str):
        # TODO: Implement putEdge method
        pass

    def putNodeLabel(self, label: NodeLabel):
        # TODO: Implement putNodeLabel method
        pass

class graph_LabelValue(SanityChecker):

    def __init__(self, graph_LabelValue: "graph_DynamicLabel" = None, graph_LabelValue24: "graph_Label" = None):
        self.graph_LabelValue = graph_LabelValue
        self.graph_LabelValue24 = graph_LabelValue24
        
    @property
    def graph_LabelValue(self):
        return self.__graph_LabelValue

    @graph_LabelValue.setter
    def graph_LabelValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_LabelValue__graph_LabelValue", None)
        self.__graph_LabelValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_DynamicLabel"):
                opp_val = getattr(old_value, "graph_DynamicLabel", None)
                if opp_val == self:
                    setattr(old_value, "graph_DynamicLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_DynamicLabel"):
                opp_val = getattr(value, "graph_DynamicLabel", None)
                setattr(value, "graph_DynamicLabel", self)

    @property
    def graph_LabelValue24(self):
        return self.__graph_LabelValue24

    @graph_LabelValue24.setter
    def graph_LabelValue24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_LabelValue__graph_LabelValue24", None)
        self.__graph_LabelValue24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Label"):
                opp_val = getattr(old_value, "graph_Label", None)
                if opp_val == self:
                    setattr(old_value, "graph_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Label"):
                opp_val = getattr(value, "graph_Label", None)
                setattr(value, "graph_Label", self)

    def reset(self):
        # TODO: Implement reset method
        pass

class Label:

    pass
class graph_DynamicLabel(Label):

    def __init__(self, nextValueValid: bool, graph_DynamicLabel: "graph_LabelValue" = None, labelsToUpdate: "graph_Decorator" = None, graph_DynamicLabel16: "graph_Graph" = None):
        self.nextValueValid = nextValueValid
        self.graph_DynamicLabel = graph_DynamicLabel
        self.labelsToUpdate = labelsToUpdate
        self.graph_DynamicLabel16 = graph_DynamicLabel16
        
    @property
    def nextValueValid(self) -> bool:
        return self.__nextValueValid

    @nextValueValid.setter
    def nextValueValid(self, nextValueValid: bool):
        self.__nextValueValid = nextValueValid

    @property
    def labelsToUpdate(self):
        return self.__labelsToUpdate

    @labelsToUpdate.setter
    def labelsToUpdate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DynamicLabel__labelsToUpdate", None)
        self.__labelsToUpdate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model.ecoreDecorator"):
                opp_val = getattr(old_value, "model.ecoreDecorator", None)
                if opp_val == self:
                    setattr(old_value, "model.ecoreDecorator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model.ecoreDecorator"):
                opp_val = getattr(value, "model.ecoreDecorator", None)
                setattr(value, "model.ecoreDecorator", self)

    @property
    def graph_DynamicLabel16(self):
        return self.__graph_DynamicLabel16

    @graph_DynamicLabel16.setter
    def graph_DynamicLabel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DynamicLabel__graph_DynamicLabel16", None)
        self.__graph_DynamicLabel16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph15"):
                opp_val = getattr(old_value, "graph_Graph15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph15"):
                opp_val = getattr(value, "graph_Graph15", None)
                if opp_val is None:
                    setattr(value, "graph_Graph15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_DynamicLabel(self):
        return self.__graph_DynamicLabel

    @graph_DynamicLabel.setter
    def graph_DynamicLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_DynamicLabel__graph_DynamicLabel", None)
        self.__graph_DynamicLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_LabelValue"):
                opp_val = getattr(old_value, "graph_LabelValue", None)
                if opp_val == self:
                    setattr(old_value, "graph_LabelValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_LabelValue"):
                opp_val = getattr(value, "graph_LabelValue", None)
                setattr(value, "graph_LabelValue", self)

    def switchToNextValue(self):
        # TODO: Implement switchToNextValue method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass

class graph_NodeLabel(Label):

    pass
class graph_StaticLabel(Modifiable, Label):

    pass
class graph_EdgeLabel(Label):

    pass