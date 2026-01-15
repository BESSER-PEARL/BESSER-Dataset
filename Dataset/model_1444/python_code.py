from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_ElkBendPoint:

    def __init__(self, x: float, y: float, graph_ElkBendPoint: "graph_ElkEdgeSection" = None):
        self.x = x
        self.y = y
        self.graph_ElkBendPoint = graph_ElkBendPoint
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def graph_ElkBendPoint(self):
        return self.__graph_ElkBendPoint

    @graph_ElkBendPoint.setter
    def graph_ElkBendPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkBendPoint__graph_ElkBendPoint", None)
        self.__graph_ElkBendPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ElkEdgeSection"):
                opp_val = getattr(old_value, "graph_ElkEdgeSection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ElkEdgeSection"):
                opp_val = getattr(value, "graph_ElkEdgeSection", None)
                if opp_val is None:
                    setattr(value, "graph_ElkEdgeSection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def set(self, y: float, x: float):
        # TODO: Implement set method
        pass

class ElkConnectableShape:

    pass
class graph_ElkPort(ElkConnectableShape):

    pass
class graph_ElkNode(ElkConnectableShape):

    def __init__(self, hierarchical: bool, parent7: set["graph_ElkPort"] = None, ElkNode: "graph_ElkNode" = None, parent10: set["graph_ElkNode"] = None, ElkNode13: "graph_ElkNode" = None, children: "graph_ElkNode" = None, containingNode: set["graph_ElkEdge"] = None, ElkNode17: "graph_ElkPort" = None, ElkNode19: "graph_ElkEdge" = None):
        self.hierarchical = hierarchical
        self.parent7 = parent7 if parent7 is not None else set()
        self.ElkNode = ElkNode
        self.parent10 = parent10 if parent10 is not None else set()
        self.ElkNode13 = ElkNode13
        self.children = children
        self.containingNode = containingNode if containingNode is not None else set()
        self.ElkNode17 = ElkNode17
        self.ElkNode19 = ElkNode19
        
    @property
    def hierarchical(self) -> bool:
        return self.__hierarchical

    @hierarchical.setter
    def hierarchical(self, hierarchical: bool):
        self.__hierarchical = hierarchical

    @property
    def parent10(self):
        return self.__parent10

    @parent10.setter
    def parent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__parent10", None)
        self.__parent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkNode"):
                    opp_val = getattr(item, "ElkNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkNode"):
                    opp_val = getattr(item, "ElkNode", None)
                    
                    setattr(item, "ElkNode", self)
                    

    @property
    def ElkNode13(self):
        return self.__ElkNode13

    @ElkNode13.setter
    def ElkNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__ElkNode13", None)
        self.__ElkNode13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def containingNode(self):
        return self.__containingNode

    @containingNode.setter
    def containingNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__containingNode", None)
        self.__containingNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkEdge15"):
                    opp_val = getattr(item, "ElkEdge15", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkEdge15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkEdge15"):
                    opp_val = getattr(item, "ElkEdge15", None)
                    
                    setattr(item, "ElkEdge15", self)
                    

    @property
    def parent7(self):
        return self.__parent7

    @parent7.setter
    def parent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__parent7", None)
        self.__parent7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkPort"):
                    opp_val = getattr(item, "ElkPort", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkPort"):
                    opp_val = getattr(item, "ElkPort", None)
                    
                    setattr(item, "ElkPort", self)
                    

    @property
    def ElkNode19(self):
        return self.__ElkNode19

    @ElkNode19.setter
    def ElkNode19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__ElkNode19", None)
        self.__ElkNode19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedEdges"):
                opp_val = getattr(old_value, "containedEdges", None)
                if opp_val == self:
                    setattr(old_value, "containedEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedEdges"):
                opp_val = getattr(value, "containedEdges", None)
                setattr(value, "containedEdges", self)

    @property
    def ElkNode17(self):
        return self.__ElkNode17

    @ElkNode17.setter
    def ElkNode17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__ElkNode17", None)
        self.__ElkNode17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ports"):
                opp_val = getattr(old_value, "ports", None)
                if opp_val == self:
                    setattr(old_value, "ports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ports"):
                opp_val = getattr(value, "ports", None)
                setattr(value, "ports", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElkNode13"):
                opp_val = getattr(old_value, "ElkNode13", None)
                if opp_val == self:
                    setattr(old_value, "ElkNode13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElkNode13"):
                opp_val = getattr(value, "ElkNode13", None)
                setattr(value, "ElkNode13", self)

    @property
    def ElkNode(self):
        return self.__ElkNode

    @ElkNode.setter
    def ElkNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkNode__ElkNode", None)
        self.__ElkNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent10"):
                opp_val = getattr(old_value, "parent10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent10"):
                opp_val = getattr(value, "parent10", None)
                if opp_val is None:
                    setattr(value, "parent10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ElkShape:

    pass
class graph_ElkConnectableShape(ElkShape):

    pass
class ElkGraphElement:

    pass
class graph_ElkEdge(ElkGraphElement):

    def __init__(self, hyperedge: bool, hierarchical: bool, selfloop: bool, connected: bool, ElkEdge: "graph_ElkConnectableShape" = None, ElkEdge5: "graph_ElkConnectableShape" = None, ElkEdge15: "graph_ElkNode" = None, outgoingEdges: set["graph_ElkConnectableShape"] = None, incomingEdges: set["graph_ElkConnectableShape"] = None, parent24: set["graph_ElkEdgeSection"] = None, containedEdges: "graph_ElkNode" = None, ElkEdge27: "graph_ElkEdgeSection" = None):
        self.hyperedge = hyperedge
        self.hierarchical = hierarchical
        self.selfloop = selfloop
        self.connected = connected
        self.ElkEdge = ElkEdge
        self.ElkEdge5 = ElkEdge5
        self.ElkEdge15 = ElkEdge15
        self.outgoingEdges = outgoingEdges if outgoingEdges is not None else set()
        self.incomingEdges = incomingEdges if incomingEdges is not None else set()
        self.parent24 = parent24 if parent24 is not None else set()
        self.containedEdges = containedEdges
        self.ElkEdge27 = ElkEdge27
        
    @property
    def connected(self) -> bool:
        return self.__connected

    @connected.setter
    def connected(self, connected: bool):
        self.__connected = connected

    @property
    def hierarchical(self) -> bool:
        return self.__hierarchical

    @hierarchical.setter
    def hierarchical(self, hierarchical: bool):
        self.__hierarchical = hierarchical

    @property
    def selfloop(self) -> bool:
        return self.__selfloop

    @selfloop.setter
    def selfloop(self, selfloop: bool):
        self.__selfloop = selfloop

    @property
    def hyperedge(self) -> bool:
        return self.__hyperedge

    @hyperedge.setter
    def hyperedge(self, hyperedge: bool):
        self.__hyperedge = hyperedge

    @property
    def ElkEdge(self):
        return self.__ElkEdge

    @ElkEdge.setter
    def ElkEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__ElkEdge", None)
        self.__ElkEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                if opp_val is None:
                    setattr(value, "sources", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__incomingEdges", None)
        self.__incomingEdges = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkConnectableShape22"):
                    opp_val = getattr(item, "ElkConnectableShape22", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkConnectableShape22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkConnectableShape22"):
                    opp_val = getattr(item, "ElkConnectableShape22", None)
                    
                    setattr(item, "ElkConnectableShape22", self)
                    

    @property
    def ElkEdge15(self):
        return self.__ElkEdge15

    @ElkEdge15.setter
    def ElkEdge15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__ElkEdge15", None)
        self.__ElkEdge15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containingNode"):
                opp_val = getattr(old_value, "containingNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containingNode"):
                opp_val = getattr(value, "containingNode", None)
                if opp_val is None:
                    setattr(value, "containingNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containedEdges(self):
        return self.__containedEdges

    @containedEdges.setter
    def containedEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__containedEdges", None)
        self.__containedEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElkNode19"):
                opp_val = getattr(old_value, "ElkNode19", None)
                if opp_val == self:
                    setattr(old_value, "ElkNode19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElkNode19"):
                opp_val = getattr(value, "ElkNode19", None)
                setattr(value, "ElkNode19", self)

    @property
    def outgoingEdges(self):
        return self.__outgoingEdges

    @outgoingEdges.setter
    def outgoingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__outgoingEdges", None)
        self.__outgoingEdges = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkConnectableShape"):
                    opp_val = getattr(item, "ElkConnectableShape", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkConnectableShape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkConnectableShape"):
                    opp_val = getattr(item, "ElkConnectableShape", None)
                    
                    setattr(item, "ElkConnectableShape", self)
                    

    @property
    def parent24(self):
        return self.__parent24

    @parent24.setter
    def parent24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__parent24", None)
        self.__parent24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkEdgeSection"):
                    opp_val = getattr(item, "ElkEdgeSection", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkEdgeSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkEdgeSection"):
                    opp_val = getattr(item, "ElkEdgeSection", None)
                    
                    setattr(item, "ElkEdgeSection", self)
                    

    @property
    def ElkEdge5(self):
        return self.__ElkEdge5

    @ElkEdge5.setter
    def ElkEdge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__ElkEdge5", None)
        self.__ElkEdge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targets"):
                opp_val = getattr(old_value, "targets", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targets"):
                opp_val = getattr(value, "targets", None)
                if opp_val is None:
                    setattr(value, "targets", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ElkEdge27(self):
        return self.__ElkEdge27

    @ElkEdge27.setter
    def ElkEdge27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdge__ElkEdge27", None)
        self.__ElkEdge27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sections"):
                opp_val = getattr(old_value, "sections", None)
                if opp_val == self:
                    setattr(old_value, "sections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sections"):
                opp_val = getattr(value, "sections", None)
                setattr(value, "sections", self)

class graph_ElkShape(ElkGraphElement):

    def __init__(self, height: float, width: float, y: float, x: float):
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    def setLocation(self, y: float, x: float):
        # TODO: Implement setLocation method
        pass

    def setDimensions(self, height: float, width: float):
        # TODO: Implement setDimensions method
        pass

class graph_ElkPropertyToValueMapEntry:

    def __init__(self, value: str, key: str, graph_ElkPropertyToValueMapEntry: "graph_EMapPropertyHolder" = None):
        self.value = value
        self.key = key
        self.graph_ElkPropertyToValueMapEntry = graph_ElkPropertyToValueMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graph_ElkPropertyToValueMapEntry(self):
        return self.__graph_ElkPropertyToValueMapEntry

    @graph_ElkPropertyToValueMapEntry.setter
    def graph_ElkPropertyToValueMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkPropertyToValueMapEntry__graph_ElkPropertyToValueMapEntry", None)
        self.__graph_ElkPropertyToValueMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_EMapPropertyHolder"):
                opp_val = getattr(old_value, "graph_EMapPropertyHolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_EMapPropertyHolder"):
                opp_val = getattr(value, "graph_EMapPropertyHolder", None)
                if opp_val is None:
                    setattr(value, "graph_EMapPropertyHolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_ElkLabel(ElkShape):

    def __init__(self, text: str, ElkLabel: "graph_ElkGraphElement" = None, labels: "graph_ElkGraphElement" = None):
        self.text = text
        self.ElkLabel = ElkLabel
        self.labels = labels
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkLabel__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElkGraphElement"):
                opp_val = getattr(old_value, "ElkGraphElement", None)
                if opp_val == self:
                    setattr(old_value, "ElkGraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElkGraphElement"):
                opp_val = getattr(value, "ElkGraphElement", None)
                setattr(value, "ElkGraphElement", self)

    @property
    def ElkLabel(self):
        return self.__ElkLabel

    @ElkLabel.setter
    def ElkLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkLabel__ElkLabel", None)
        self.__ElkLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EMapPropertyHolder:

    pass
class graph_ElkEdgeSection(EMapPropertyHolder):

    def __init__(self, startX: float, startY: float, endX: float, endY: float, identifier: str, ElkEdgeSection: "graph_ElkEdge" = None, graph_ElkEdgeSection: set["graph_ElkBendPoint"] = None, sections: "graph_ElkEdge" = None, graph_ElkEdgeSection29: "graph_ElkConnectableShape" = None, graph_ElkEdgeSection31: "graph_ElkConnectableShape" = None, ElkEdgeSection35: "graph_ElkEdgeSection" = None, incomingSections: set["graph_ElkEdgeSection"] = None, ElkEdgeSection38: "graph_ElkEdgeSection" = None, outgoingSections: set["graph_ElkEdgeSection"] = None):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.identifier = identifier
        self.ElkEdgeSection = ElkEdgeSection
        self.graph_ElkEdgeSection = graph_ElkEdgeSection if graph_ElkEdgeSection is not None else set()
        self.sections = sections
        self.graph_ElkEdgeSection29 = graph_ElkEdgeSection29
        self.graph_ElkEdgeSection31 = graph_ElkEdgeSection31
        self.ElkEdgeSection35 = ElkEdgeSection35
        self.incomingSections = incomingSections if incomingSections is not None else set()
        self.ElkEdgeSection38 = ElkEdgeSection38
        self.outgoingSections = outgoingSections if outgoingSections is not None else set()
        
    @property
    def endY(self) -> float:
        return self.__endY

    @endY.setter
    def endY(self, endY: float):
        self.__endY = endY

    @property
    def startY(self) -> float:
        return self.__startY

    @startY.setter
    def startY(self, startY: float):
        self.__startY = startY

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def startX(self) -> float:
        return self.__startX

    @startX.setter
    def startX(self, startX: float):
        self.__startX = startX

    @property
    def endX(self) -> float:
        return self.__endX

    @endX.setter
    def endX(self, endX: float):
        self.__endX = endX

    @property
    def outgoingSections(self):
        return self.__outgoingSections

    @outgoingSections.setter
    def outgoingSections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__outgoingSections", None)
        self.__outgoingSections = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkEdgeSection38"):
                    opp_val = getattr(item, "ElkEdgeSection38", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkEdgeSection38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkEdgeSection38"):
                    opp_val = getattr(item, "ElkEdgeSection38", None)
                    
                    setattr(item, "ElkEdgeSection38", self)
                    

    @property
    def ElkEdgeSection(self):
        return self.__ElkEdgeSection

    @ElkEdgeSection.setter
    def ElkEdgeSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__ElkEdgeSection", None)
        self.__ElkEdgeSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent24"):
                opp_val = getattr(old_value, "parent24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent24"):
                opp_val = getattr(value, "parent24", None)
                if opp_val is None:
                    setattr(value, "parent24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingSections(self):
        return self.__incomingSections

    @incomingSections.setter
    def incomingSections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__incomingSections", None)
        self.__incomingSections = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkEdgeSection35"):
                    opp_val = getattr(item, "ElkEdgeSection35", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkEdgeSection35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkEdgeSection35"):
                    opp_val = getattr(item, "ElkEdgeSection35", None)
                    
                    setattr(item, "ElkEdgeSection35", self)
                    

    @property
    def ElkEdgeSection35(self):
        return self.__ElkEdgeSection35

    @ElkEdgeSection35.setter
    def ElkEdgeSection35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__ElkEdgeSection35", None)
        self.__ElkEdgeSection35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingSections"):
                opp_val = getattr(old_value, "incomingSections", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingSections"):
                opp_val = getattr(value, "incomingSections", None)
                if opp_val is None:
                    setattr(value, "incomingSections", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ElkEdgeSection38(self):
        return self.__ElkEdgeSection38

    @ElkEdgeSection38.setter
    def ElkEdgeSection38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__ElkEdgeSection38", None)
        self.__ElkEdgeSection38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingSections"):
                opp_val = getattr(old_value, "outgoingSections", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingSections"):
                opp_val = getattr(value, "outgoingSections", None)
                if opp_val is None:
                    setattr(value, "outgoingSections", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_ElkEdgeSection29(self):
        return self.__graph_ElkEdgeSection29

    @graph_ElkEdgeSection29.setter
    def graph_ElkEdgeSection29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__graph_ElkEdgeSection29", None)
        self.__graph_ElkEdgeSection29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ElkConnectableShape"):
                opp_val = getattr(old_value, "graph_ElkConnectableShape", None)
                if opp_val == self:
                    setattr(old_value, "graph_ElkConnectableShape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ElkConnectableShape"):
                opp_val = getattr(value, "graph_ElkConnectableShape", None)
                setattr(value, "graph_ElkConnectableShape", self)

    @property
    def graph_ElkEdgeSection(self):
        return self.__graph_ElkEdgeSection

    @graph_ElkEdgeSection.setter
    def graph_ElkEdgeSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__graph_ElkEdgeSection", None)
        self.__graph_ElkEdgeSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_ElkBendPoint"):
                    opp_val = getattr(item, "graph_ElkBendPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_ElkBendPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_ElkBendPoint"):
                    opp_val = getattr(item, "graph_ElkBendPoint", None)
                    
                    setattr(item, "graph_ElkBendPoint", self)
                    

    @property
    def sections(self):
        return self.__sections

    @sections.setter
    def sections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__sections", None)
        self.__sections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElkEdge27"):
                opp_val = getattr(old_value, "ElkEdge27", None)
                if opp_val == self:
                    setattr(old_value, "ElkEdge27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElkEdge27"):
                opp_val = getattr(value, "ElkEdge27", None)
                setattr(value, "ElkEdge27", self)

    @property
    def graph_ElkEdgeSection31(self):
        return self.__graph_ElkEdgeSection31

    @graph_ElkEdgeSection31.setter
    def graph_ElkEdgeSection31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkEdgeSection__graph_ElkEdgeSection31", None)
        self.__graph_ElkEdgeSection31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_ElkConnectableShape32"):
                opp_val = getattr(old_value, "graph_ElkConnectableShape32", None)
                if opp_val == self:
                    setattr(old_value, "graph_ElkConnectableShape32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_ElkConnectableShape32"):
                opp_val = getattr(value, "graph_ElkConnectableShape32", None)
                setattr(value, "graph_ElkConnectableShape32", self)

    def setStartLocation(self, y: float, x: float):
        # TODO: Implement setStartLocation method
        pass

    def setEndLocation(self, y: float, x: float):
        # TODO: Implement setEndLocation method
        pass

class graph_ElkGraphElement(EMapPropertyHolder):

    def __init__(self, identifier: str, parent: set["graph_ElkLabel"] = None, ElkGraphElement: "graph_ElkLabel" = None):
        self.identifier = identifier
        self.parent = parent if parent is not None else set()
        self.ElkGraphElement = ElkGraphElement
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ElkGraphElement(self):
        return self.__ElkGraphElement

    @ElkGraphElement.setter
    def ElkGraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkGraphElement__ElkGraphElement", None)
        self.__ElkGraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labels"):
                opp_val = getattr(old_value, "labels", None)
                if opp_val == self:
                    setattr(old_value, "labels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labels"):
                opp_val = getattr(value, "labels", None)
                setattr(value, "labels", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElkGraphElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElkLabel"):
                    opp_val = getattr(item, "ElkLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "ElkLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElkLabel"):
                    opp_val = getattr(item, "ElkLabel", None)
                    
                    setattr(item, "ElkLabel", self)
                    

class IPropertyHolder:

    pass
class graph_EMapPropertyHolder(IPropertyHolder):

    pass
class graph_IPropertyHolder(ABC):

    def __init__(self):
        
    def copyProperties(self, source: str) -> str:
        # TODO: Implement copyProperties method
        pass

    def getProperty(self, property: str):
        # TODO: Implement getProperty method
        pass

    def setProperty(self, value: str, property: str) -> str:
        # TODO: Implement setProperty method
        pass

    def getAllProperties(self):
        # TODO: Implement getAllProperties method
        pass

    def hasProperty(self, property: str) -> bool:
        # TODO: Implement hasProperty method
        pass
