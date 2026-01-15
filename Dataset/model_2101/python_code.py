from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Text:

    pass
class SimpleTree_TreeElement(ABC):

    def __init__(self, index: int, name: str, SimpleTree_TreeElement: "SimpleTree_File" = None):
        self.index = index
        self.name = name
        self.SimpleTree_TreeElement = SimpleTree_TreeElement
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleTree_TreeElement(self):
        return self.__SimpleTree_TreeElement

    @SimpleTree_TreeElement.setter
    def SimpleTree_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_TreeElement__SimpleTree_TreeElement", None)
        self.__SimpleTree_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleTree_File"):
                opp_val = getattr(old_value, "SimpleTree_File", None)
                if opp_val == self:
                    setattr(old_value, "SimpleTree_File", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleTree_File"):
                opp_val = getattr(value, "SimpleTree_File", None)
                setattr(value, "SimpleTree_File", self)

class SimpleTree_Node(Text):

    def __init__(self, startLineIndex: int, stopIndex: int, startIndex: int, stopLineIndex: int, Node: "SimpleTree_Attribute" = None, parentNode: set["SimpleTree_Text"] = None, node: set["SimpleTree_Attribute"] = None, Node13: "SimpleTree_Text" = None):
        self.startLineIndex = startLineIndex
        self.stopIndex = stopIndex
        self.startIndex = startIndex
        self.stopLineIndex = stopLineIndex
        self.Node = Node
        self.parentNode = parentNode if parentNode is not None else set()
        self.node = node if node is not None else set()
        self.Node13 = Node13
        
    @property
    def stopIndex(self) -> int:
        return self.__stopIndex

    @stopIndex.setter
    def stopIndex(self, stopIndex: int):
        self.__stopIndex = stopIndex

    @property
    def stopLineIndex(self) -> int:
        return self.__stopLineIndex

    @stopLineIndex.setter
    def stopLineIndex(self, stopLineIndex: int):
        self.__stopLineIndex = stopLineIndex

    @property
    def startLineIndex(self) -> int:
        return self.__startLineIndex

    @startLineIndex.setter
    def startLineIndex(self, startLineIndex: int):
        self.__startLineIndex = startLineIndex

    @property
    def startIndex(self) -> int:
        return self.__startIndex

    @startIndex.setter
    def startIndex(self, startIndex: int):
        self.__startIndex = startIndex

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Node__parentNode", None)
        self.__parentNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Text"):
                    opp_val = getattr(item, "Text", None)
                    
                    if opp_val == self:
                        setattr(item, "Text", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Text"):
                    opp_val = getattr(item, "Text", None)
                    
                    setattr(item, "Text", self)
                    

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Node__Node13", None)
        self.__Node13 = value
        
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
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Node__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

class TreeElement:

    pass
class SimpleTree_Folder(TreeElement):

    pass
class SimpleTree_Text(TreeElement):

    pass
class SimpleTree_File(TreeElement):

    pass
class SimpleTree_Attribute(TreeElement):

    def __init__(self, value: str, attribute: "SimpleTree_Node" = None, Attribute: "SimpleTree_Node" = None):
        self.value = value
        self.attribute = attribute
        self.Attribute = Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTree_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)
