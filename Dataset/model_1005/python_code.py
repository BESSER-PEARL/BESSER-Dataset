from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class GraphItem:

    pass
class ZestGraph_GraphConnection(GraphItem):

    def __init__(self, color: str, lineWidth: int, lineStyle: int, GraphConnection: "ZestGraph_GraphNode" = None, GraphConnection7: "ZestGraph_GraphNode" = None, outgoing: "ZestGraph_GraphNode" = None, ingoing: "ZestGraph_GraphNode" = None):
        self.color = color
        self.lineWidth = lineWidth
        self.lineStyle = lineStyle
        self.GraphConnection = GraphConnection
        self.GraphConnection7 = GraphConnection7
        self.outgoing = outgoing
        self.ingoing = ingoing
        
    @property
    def lineStyle(self) -> int:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: int):
        self.__lineStyle = lineStyle

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphConnection__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphNode"):
                opp_val = getattr(old_value, "GraphNode", None)
                if opp_val == self:
                    setattr(old_value, "GraphNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphNode"):
                opp_val = getattr(value, "GraphNode", None)
                setattr(value, "GraphNode", self)

    @property
    def ingoing(self):
        return self.__ingoing

    @ingoing.setter
    def ingoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphConnection__ingoing", None)
        self.__ingoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphNode10"):
                opp_val = getattr(old_value, "GraphNode10", None)
                if opp_val == self:
                    setattr(old_value, "GraphNode10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphNode10"):
                opp_val = getattr(value, "GraphNode10", None)
                setattr(value, "GraphNode10", self)

    @property
    def GraphConnection(self):
        return self.__GraphConnection

    @GraphConnection.setter
    def GraphConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphConnection__GraphConnection", None)
        self.__GraphConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceNode"):
                opp_val = getattr(old_value, "sourceNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceNode"):
                opp_val = getattr(value, "sourceNode", None)
                if opp_val is None:
                    setattr(value, "sourceNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GraphConnection7(self):
        return self.__GraphConnection7

    @GraphConnection7.setter
    def GraphConnection7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphConnection__GraphConnection7", None)
        self.__GraphConnection7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetNode"):
                opp_val = getattr(old_value, "targetNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetNode"):
                opp_val = getattr(value, "targetNode", None)
                if opp_val is None:
                    setattr(value, "targetNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ZestGraph_GraphNode(GraphItem):

    def __init__(self, shape: str, nodeStyle: str, backColor: str, width: float, height: float, sourceNode: set["ZestGraph_GraphConnection"] = None, targetNode: set["ZestGraph_GraphConnection"] = None, GraphNode: "ZestGraph_GraphConnection" = None, GraphNode10: "ZestGraph_GraphConnection" = None, ZestGraph_GraphNode: "ZestGraph_GraphContainer" = None):
        self.shape = shape
        self.nodeStyle = nodeStyle
        self.backColor = backColor
        self.width = width
        self.height = height
        self.sourceNode = sourceNode if sourceNode is not None else set()
        self.targetNode = targetNode if targetNode is not None else set()
        self.GraphNode = GraphNode
        self.GraphNode10 = GraphNode10
        self.ZestGraph_GraphNode = ZestGraph_GraphNode
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def backColor(self) -> str:
        return self.__backColor

    @backColor.setter
    def backColor(self, backColor: str):
        self.__backColor = backColor

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def nodeStyle(self) -> str:
        return self.__nodeStyle

    @nodeStyle.setter
    def nodeStyle(self, nodeStyle: str):
        self.__nodeStyle = nodeStyle

    @property
    def GraphNode(self):
        return self.__GraphNode

    @GraphNode.setter
    def GraphNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphNode__GraphNode", None)
        self.__GraphNode = value
        
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
    def sourceNode(self):
        return self.__sourceNode

    @sourceNode.setter
    def sourceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphNode__sourceNode", None)
        self.__sourceNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphConnection"):
                    opp_val = getattr(item, "GraphConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphConnection"):
                    opp_val = getattr(item, "GraphConnection", None)
                    
                    setattr(item, "GraphConnection", self)
                    

    @property
    def ZestGraph_GraphNode(self):
        return self.__ZestGraph_GraphNode

    @ZestGraph_GraphNode.setter
    def ZestGraph_GraphNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphNode__ZestGraph_GraphNode", None)
        self.__ZestGraph_GraphNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ZestGraph_GraphContainer3"):
                opp_val = getattr(old_value, "ZestGraph_GraphContainer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ZestGraph_GraphContainer3"):
                opp_val = getattr(value, "ZestGraph_GraphContainer3", None)
                if opp_val is None:
                    setattr(value, "ZestGraph_GraphContainer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def targetNode(self):
        return self.__targetNode

    @targetNode.setter
    def targetNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphNode__targetNode", None)
        self.__targetNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphConnection7"):
                    opp_val = getattr(item, "GraphConnection7", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphConnection7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphConnection7"):
                    opp_val = getattr(item, "GraphConnection7", None)
                    
                    setattr(item, "GraphConnection7", self)
                    

    @property
    def GraphNode10(self):
        return self.__GraphNode10

    @GraphNode10.setter
    def GraphNode10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphNode__GraphNode10", None)
        self.__GraphNode10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingoing"):
                opp_val = getattr(old_value, "ingoing", None)
                if opp_val == self:
                    setattr(old_value, "ingoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingoing"):
                opp_val = getattr(value, "ingoing", None)
                setattr(value, "ingoing", self)

class ZestGraph_GraphItem(ABC):

    def __init__(self, text: str, GraphItem: "ZestGraph_ZestGraph" = None, items: "ZestGraph_ZestGraph" = None):
        self.text = text
        self.GraphItem = GraphItem
        self.items = items
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphItem__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ZestGraph"):
                opp_val = getattr(old_value, "ZestGraph", None)
                if opp_val == self:
                    setattr(old_value, "ZestGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ZestGraph"):
                opp_val = getattr(value, "ZestGraph", None)
                setattr(value, "ZestGraph", self)

    @property
    def GraphItem(self):
        return self.__GraphItem

    @GraphItem.setter
    def GraphItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ZestGraph_GraphItem__GraphItem", None)
        self.__GraphItem = value
        
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

class NamedElement:

    pass
class ZestGraph_GraphContainer(NamedElement):

    pass
class ZestGraph_ZestGraph(NamedElement):

    pass
class ZestGraph_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
