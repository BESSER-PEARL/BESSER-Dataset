from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NodeShape(Enum):
    circle = "circle"
    doublecircle = "doublecircle"
    record = "record"
class DrawType(Enum):
    diagram = "diagram"
class NodeType(Enum):
    node = "node"
    markednode = "markednode"
class NodeStyle(Enum):
    none = "none"
    italic = "italic"
    underline = "underline"
class NodeColor(Enum):
    gray95 = "gray95"
class Decoration(Enum):
    none = "none"
    triangle = "triangle"
    diamond = "diamond"
    odiamond = "odiamond"
    open = "open"
    empty = "empty"


############################################
# Definition of Classes
############################################

class modeldraw_Enumerator:

    def __init__(self, value: str, modeldraw_Enumerator38: "modeldraw_EEnumLiteral" = None, modeldraw_Enumerator: "modeldraw_NodeEnumerator" = None):
        self.value = value
        self.modeldraw_Enumerator38 = modeldraw_Enumerator38
        self.modeldraw_Enumerator = modeldraw_Enumerator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def modeldraw_Enumerator(self):
        return self.__modeldraw_Enumerator

    @modeldraw_Enumerator.setter
    def modeldraw_Enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Enumerator__modeldraw_Enumerator", None)
        self.__modeldraw_Enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_NodeEnumerator36"):
                opp_val = getattr(old_value, "modeldraw_NodeEnumerator36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_NodeEnumerator36"):
                opp_val = getattr(value, "modeldraw_NodeEnumerator36", None)
                if opp_val is None:
                    setattr(value, "modeldraw_NodeEnumerator36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modeldraw_Enumerator38(self):
        return self.__modeldraw_Enumerator38

    @modeldraw_Enumerator38.setter
    def modeldraw_Enumerator38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Enumerator__modeldraw_Enumerator38", None)
        self.__modeldraw_Enumerator38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EEnumLiteral"):
                opp_val = getattr(old_value, "modeldraw_EEnumLiteral", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EEnumLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EEnumLiteral"):
                opp_val = getattr(value, "modeldraw_EEnumLiteral", None)
                setattr(value, "modeldraw_EEnumLiteral", self)

class Relation:

    pass
class modeldraw_Level(Relation):

    pass
class modeldraw_Edge(Relation):

    pass
class modeldraw_EReference:

    pass
class NamedItem:

    pass
class modeldraw_EAttribute:

    pass
class modeldraw_EEnumLiteral:

    pass
class modeldraw_Relation(NamedItem):

    def __init__(self, src_decoration: str, tar_decoration: str, modeldraw_Relation: "modeldraw_MutatorDraw" = None, modeldraw_Relation15: "modeldraw_EReference" = None, modeldraw_Relation18: "modeldraw_EAttribute" = None, modeldraw_Relation21: "modeldraw_EAttribute" = None, modeldraw_Relation24: "modeldraw_EAttribute" = None):
        self.src_decoration = src_decoration
        self.tar_decoration = tar_decoration
        self.modeldraw_Relation = modeldraw_Relation
        self.modeldraw_Relation15 = modeldraw_Relation15
        self.modeldraw_Relation18 = modeldraw_Relation18
        self.modeldraw_Relation21 = modeldraw_Relation21
        self.modeldraw_Relation24 = modeldraw_Relation24
        
    @property
    def src_decoration(self) -> str:
        return self.__src_decoration

    @src_decoration.setter
    def src_decoration(self, src_decoration: str):
        self.__src_decoration = src_decoration

    @property
    def tar_decoration(self) -> str:
        return self.__tar_decoration

    @tar_decoration.setter
    def tar_decoration(self, tar_decoration: str):
        self.__tar_decoration = tar_decoration

    @property
    def modeldraw_Relation24(self):
        return self.__modeldraw_Relation24

    @modeldraw_Relation24.setter
    def modeldraw_Relation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Relation__modeldraw_Relation24", None)
        self.__modeldraw_Relation24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EAttribute25"):
                opp_val = getattr(old_value, "modeldraw_EAttribute25", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EAttribute25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EAttribute25"):
                opp_val = getattr(value, "modeldraw_EAttribute25", None)
                setattr(value, "modeldraw_EAttribute25", self)

    @property
    def modeldraw_Relation18(self):
        return self.__modeldraw_Relation18

    @modeldraw_Relation18.setter
    def modeldraw_Relation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Relation__modeldraw_Relation18", None)
        self.__modeldraw_Relation18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EAttribute19"):
                opp_val = getattr(old_value, "modeldraw_EAttribute19", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EAttribute19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EAttribute19"):
                opp_val = getattr(value, "modeldraw_EAttribute19", None)
                setattr(value, "modeldraw_EAttribute19", self)

    @property
    def modeldraw_Relation15(self):
        return self.__modeldraw_Relation15

    @modeldraw_Relation15.setter
    def modeldraw_Relation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Relation__modeldraw_Relation15", None)
        self.__modeldraw_Relation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EReference16"):
                opp_val = getattr(old_value, "modeldraw_EReference16", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EReference16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EReference16"):
                opp_val = getattr(value, "modeldraw_EReference16", None)
                setattr(value, "modeldraw_EReference16", self)

    @property
    def modeldraw_Relation21(self):
        return self.__modeldraw_Relation21

    @modeldraw_Relation21.setter
    def modeldraw_Relation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Relation__modeldraw_Relation21", None)
        self.__modeldraw_Relation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EAttribute22"):
                opp_val = getattr(old_value, "modeldraw_EAttribute22", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EAttribute22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EAttribute22"):
                opp_val = getattr(value, "modeldraw_EAttribute22", None)
                setattr(value, "modeldraw_EAttribute22", self)

    @property
    def modeldraw_Relation(self):
        return self.__modeldraw_Relation

    @modeldraw_Relation.setter
    def modeldraw_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Relation__modeldraw_Relation", None)
        self.__modeldraw_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_MutatorDraw3"):
                opp_val = getattr(old_value, "modeldraw_MutatorDraw3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_MutatorDraw3"):
                opp_val = getattr(value, "modeldraw_MutatorDraw3", None)
                if opp_val is None:
                    setattr(value, "modeldraw_MutatorDraw3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class modeldraw_Node(NamedItem):

    def __init__(self, type: str, shape: str, color: str, style: str, modeldraw_Node: "modeldraw_MutatorDraw" = None, modeldraw_Node10: set["modeldraw_BooleanAttribute"] = None, modeldraw_Node13: set["modeldraw_EReference"] = None):
        self.type = type
        self.shape = shape
        self.color = color
        self.style = style
        self.modeldraw_Node = modeldraw_Node
        self.modeldraw_Node10 = modeldraw_Node10 if modeldraw_Node10 is not None else set()
        self.modeldraw_Node13 = modeldraw_Node13 if modeldraw_Node13 is not None else set()
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def modeldraw_Node13(self):
        return self.__modeldraw_Node13

    @modeldraw_Node13.setter
    def modeldraw_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Node__modeldraw_Node13", None)
        self.__modeldraw_Node13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_EReference"):
                    opp_val = getattr(item, "modeldraw_EReference", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_EReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_EReference"):
                    opp_val = getattr(item, "modeldraw_EReference", None)
                    
                    setattr(item, "modeldraw_EReference", self)
                    

    @property
    def modeldraw_Node(self):
        return self.__modeldraw_Node

    @modeldraw_Node.setter
    def modeldraw_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Node__modeldraw_Node", None)
        self.__modeldraw_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_MutatorDraw"):
                opp_val = getattr(old_value, "modeldraw_MutatorDraw", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_MutatorDraw"):
                opp_val = getattr(value, "modeldraw_MutatorDraw", None)
                if opp_val is None:
                    setattr(value, "modeldraw_MutatorDraw", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modeldraw_Node10(self):
        return self.__modeldraw_Node10

    @modeldraw_Node10.setter
    def modeldraw_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Node__modeldraw_Node10", None)
        self.__modeldraw_Node10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_BooleanAttribute11"):
                    opp_val = getattr(item, "modeldraw_BooleanAttribute11", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_BooleanAttribute11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_BooleanAttribute11"):
                    opp_val = getattr(item, "modeldraw_BooleanAttribute11", None)
                    
                    setattr(item, "modeldraw_BooleanAttribute11", self)
                    

class Item:

    pass
class modeldraw_BooleanAttribute(Item):

    def __init__(self, negation: bool, modeldraw_BooleanAttribute: "modeldraw_EAttribute" = None, modeldraw_BooleanAttribute11: "modeldraw_Node" = None):
        self.negation = negation
        self.modeldraw_BooleanAttribute = modeldraw_BooleanAttribute
        self.modeldraw_BooleanAttribute11 = modeldraw_BooleanAttribute11
        
    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def modeldraw_BooleanAttribute11(self):
        return self.__modeldraw_BooleanAttribute11

    @modeldraw_BooleanAttribute11.setter
    def modeldraw_BooleanAttribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_BooleanAttribute__modeldraw_BooleanAttribute11", None)
        self.__modeldraw_BooleanAttribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_Node10"):
                opp_val = getattr(old_value, "modeldraw_Node10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_Node10"):
                opp_val = getattr(value, "modeldraw_Node10", None)
                if opp_val is None:
                    setattr(value, "modeldraw_Node10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modeldraw_BooleanAttribute(self):
        return self.__modeldraw_BooleanAttribute

    @modeldraw_BooleanAttribute.setter
    def modeldraw_BooleanAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_BooleanAttribute__modeldraw_BooleanAttribute", None)
        self.__modeldraw_BooleanAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_EAttribute8"):
                opp_val = getattr(old_value, "modeldraw_EAttribute8", None)
                if opp_val == self:
                    setattr(old_value, "modeldraw_EAttribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_EAttribute8"):
                opp_val = getattr(value, "modeldraw_EAttribute8", None)
                setattr(value, "modeldraw_EAttribute8", self)

class modeldraw_NodeEnumerator(Item):

    pass
class modeldraw_Information(Item):

    pass
class modeldraw_MutatorDraw(Item):

    def __init__(self, metamodel: str, type: str, modeldraw_MutatorDraw5: set["modeldraw_Content"] = None, modeldraw_MutatorDraw: set["modeldraw_Node"] = None, modeldraw_MutatorDraw3: set["modeldraw_Relation"] = None):
        self.metamodel = metamodel
        self.type = type
        self.modeldraw_MutatorDraw5 = modeldraw_MutatorDraw5 if modeldraw_MutatorDraw5 is not None else set()
        self.modeldraw_MutatorDraw = modeldraw_MutatorDraw if modeldraw_MutatorDraw is not None else set()
        self.modeldraw_MutatorDraw3 = modeldraw_MutatorDraw3 if modeldraw_MutatorDraw3 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def modeldraw_MutatorDraw(self):
        return self.__modeldraw_MutatorDraw

    @modeldraw_MutatorDraw.setter
    def modeldraw_MutatorDraw(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_MutatorDraw__modeldraw_MutatorDraw", None)
        self.__modeldraw_MutatorDraw = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_Node"):
                    opp_val = getattr(item, "modeldraw_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_Node"):
                    opp_val = getattr(item, "modeldraw_Node", None)
                    
                    setattr(item, "modeldraw_Node", self)
                    

    @property
    def modeldraw_MutatorDraw5(self):
        return self.__modeldraw_MutatorDraw5

    @modeldraw_MutatorDraw5.setter
    def modeldraw_MutatorDraw5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_MutatorDraw__modeldraw_MutatorDraw5", None)
        self.__modeldraw_MutatorDraw5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_Content"):
                    opp_val = getattr(item, "modeldraw_Content", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_Content", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_Content"):
                    opp_val = getattr(item, "modeldraw_Content", None)
                    
                    setattr(item, "modeldraw_Content", self)
                    

    @property
    def modeldraw_MutatorDraw3(self):
        return self.__modeldraw_MutatorDraw3

    @modeldraw_MutatorDraw3.setter
    def modeldraw_MutatorDraw3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_MutatorDraw__modeldraw_MutatorDraw3", None)
        self.__modeldraw_MutatorDraw3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_Relation"):
                    opp_val = getattr(item, "modeldraw_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_Relation"):
                    opp_val = getattr(item, "modeldraw_Relation", None)
                    
                    setattr(item, "modeldraw_Relation", self)
                    

class modeldraw_EClass:

    pass
class modeldraw_Item(ABC):

    pass
class modeldraw_NamedItem(Item):

    pass
class modeldraw_Content(NamedItem):

    def __init__(self, symbol: str, modeldraw_Content: "modeldraw_MutatorDraw" = None, modeldraw_Content45: set["modeldraw_NodeEnumerator"] = None, modeldraw_Content48: set["modeldraw_Information"] = None):
        self.symbol = symbol
        self.modeldraw_Content = modeldraw_Content
        self.modeldraw_Content45 = modeldraw_Content45 if modeldraw_Content45 is not None else set()
        self.modeldraw_Content48 = modeldraw_Content48 if modeldraw_Content48 is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def modeldraw_Content(self):
        return self.__modeldraw_Content

    @modeldraw_Content.setter
    def modeldraw_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Content__modeldraw_Content", None)
        self.__modeldraw_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeldraw_MutatorDraw5"):
                opp_val = getattr(old_value, "modeldraw_MutatorDraw5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeldraw_MutatorDraw5"):
                opp_val = getattr(value, "modeldraw_MutatorDraw5", None)
                if opp_val is None:
                    setattr(value, "modeldraw_MutatorDraw5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modeldraw_Content45(self):
        return self.__modeldraw_Content45

    @modeldraw_Content45.setter
    def modeldraw_Content45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Content__modeldraw_Content45", None)
        self.__modeldraw_Content45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_NodeEnumerator46"):
                    opp_val = getattr(item, "modeldraw_NodeEnumerator46", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_NodeEnumerator46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_NodeEnumerator46"):
                    opp_val = getattr(item, "modeldraw_NodeEnumerator46", None)
                    
                    setattr(item, "modeldraw_NodeEnumerator46", self)
                    

    @property
    def modeldraw_Content48(self):
        return self.__modeldraw_Content48

    @modeldraw_Content48.setter
    def modeldraw_Content48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modeldraw_Content__modeldraw_Content48", None)
        self.__modeldraw_Content48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeldraw_Information49"):
                    opp_val = getattr(item, "modeldraw_Information49", None)
                    
                    if opp_val == self:
                        setattr(item, "modeldraw_Information49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeldraw_Information49"):
                    opp_val = getattr(item, "modeldraw_Information49", None)
                    
                    setattr(item, "modeldraw_Information49", self)
                    
