from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BendPoint:

    pass
class notation_AbsoluteBendPoint(BendPoint):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

class notation_RelativeBendPoint(BendPoint):

    def __init__(self, sourceX: int, sourceY: int, targetX: int, targetY: int):
        self.sourceX = sourceX
        self.sourceY = sourceY
        self.targetX = targetX
        self.targetY = targetY
        
    @property
    def targetY(self) -> int:
        return self.__targetY

    @targetY.setter
    def targetY(self, targetY: int):
        self.__targetY = targetY

    @property
    def targetX(self) -> int:
        return self.__targetX

    @targetX.setter
    def targetX(self, targetX: int):
        self.__targetX = targetX

    @property
    def sourceY(self) -> int:
        return self.__sourceY

    @sourceY.setter
    def sourceY(self, sourceY: int):
        self.__sourceY = sourceY

    @property
    def sourceX(self) -> int:
        return self.__sourceX

    @sourceX.setter
    def sourceX(self, sourceX: int):
        self.__sourceX = sourceX

class Node:

    pass
class notation_BendPoint(ABC):

    pass
class notation_Anchor:

    def __init__(self, x: int, y: int, notation_Anchor: "notation_Edge" = None, notation_Anchor13: "notation_Edge" = None):
        self.x = x
        self.y = y
        self.notation_Anchor = notation_Anchor
        self.notation_Anchor13 = notation_Anchor13
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def notation_Anchor(self):
        return self.__notation_Anchor

    @notation_Anchor.setter
    def notation_Anchor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Anchor__notation_Anchor", None)
        self.__notation_Anchor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Edge"):
                opp_val = getattr(old_value, "notation_Edge", None)
                if opp_val == self:
                    setattr(old_value, "notation_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Edge"):
                opp_val = getattr(value, "notation_Edge", None)
                setattr(value, "notation_Edge", self)

    @property
    def notation_Anchor13(self):
        return self.__notation_Anchor13

    @notation_Anchor13.setter
    def notation_Anchor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Anchor__notation_Anchor13", None)
        self.__notation_Anchor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Edge12"):
                opp_val = getattr(old_value, "notation_Edge12", None)
                if opp_val == self:
                    setattr(old_value, "notation_Edge12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Edge12"):
                opp_val = getattr(value, "notation_Edge12", None)
                setattr(value, "notation_Edge12", self)

class notation_HierarchicalNode(Node):

    pass
class DiagramElement:

    pass
class notation_Edge(DiagramElement):

    pass
class notation_Node(DiagramElement):

    def __init__(self, x: int, y: int, width: int, height: int, source: set["notation_Edge"] = None, target: set["notation_Edge"] = None, nodes: "notation_HierarchicalNode" = None, Node: "notation_Edge" = None, Node7: "notation_Edge" = None, Node16: "notation_HierarchicalNode" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.Node = Node
        self.Node7 = Node7
        self.Node16 = Node16
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge3"):
                    opp_val = getattr(item, "Edge3", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge3"):
                    opp_val = getattr(item, "Edge3", None)
                    
                    setattr(item, "Edge3", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__source", None)
        self.__source = value if value is not None else set()
        
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
    def Node16(self):
        return self.__Node16

    @Node16.setter
    def Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__Node16", None)
        self.__Node16 = value
        
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

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__Node", None)
        self.__Node = value
        
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
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HierarchicalNode"):
                opp_val = getattr(old_value, "HierarchicalNode", None)
                if opp_val == self:
                    setattr(old_value, "HierarchicalNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HierarchicalNode"):
                opp_val = getattr(value, "HierarchicalNode", None)
                setattr(value, "HierarchicalNode", self)

    @property
    def Node7(self):
        return self.__Node7

    @Node7.setter
    def Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Node__Node7", None)
        self.__Node7 = value
        
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

class notation_EObject:

    pass
class Identifier:

    pass
class notation_DiagramElement(Identifier):

    def __init__(self, visible: bool, persistent: bool, notation_DiagramElement: "notation_EObject" = None):
        self.visible = visible
        self.persistent = persistent
        self.notation_DiagramElement = notation_DiagramElement
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def persistent(self) -> bool:
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent

    @property
    def notation_DiagramElement(self):
        return self.__notation_DiagramElement

    @notation_DiagramElement.setter
    def notation_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_DiagramElement__notation_DiagramElement", None)
        self.__notation_DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_EObject"):
                opp_val = getattr(old_value, "notation_EObject", None)
                if opp_val == self:
                    setattr(old_value, "notation_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_EObject"):
                opp_val = getattr(value, "notation_EObject", None)
                setattr(value, "notation_EObject", self)
