from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Text:

    pass
class Simpletree_TreeElement(ABC):

    def __init__(self, index: int, name: str, Simpletree_TreeElement: "Simpletree_File" = None):
        self.index = index
        self.name = name
        self.Simpletree_TreeElement = Simpletree_TreeElement
        
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
    def Simpletree_TreeElement(self):
        return self.__Simpletree_TreeElement

    @Simpletree_TreeElement.setter
    def Simpletree_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_TreeElement__Simpletree_TreeElement", None)
        self.__Simpletree_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Simpletree_File"):
                opp_val = getattr(old_value, "Simpletree_File", None)
                if opp_val == self:
                    setattr(old_value, "Simpletree_File", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Simpletree_File"):
                opp_val = getattr(value, "Simpletree_File", None)
                setattr(value, "Simpletree_File", self)

class Simpletree_Node(Text):

    def __init__(self, startLineIndex: int, stopIndex: int, stopLineIndex: int, startIndex: int, Node: "Simpletree_Attribute" = None, parentNode: set["Simpletree_Text"] = None, node: set["Simpletree_Attribute"] = None, Node13: "Simpletree_Text" = None):
        self.startLineIndex = startLineIndex
        self.stopIndex = stopIndex
        self.stopLineIndex = stopLineIndex
        self.startIndex = startIndex
        self.Node = Node
        self.parentNode = parentNode if parentNode is not None else set()
        self.node = node if node is not None else set()
        self.Node13 = Node13
        
    @property
    def stopLineIndex(self) -> int:
        return self.__stopLineIndex

    @stopLineIndex.setter
    def stopLineIndex(self, stopLineIndex: int):
        self.__stopLineIndex = stopLineIndex

    @property
    def stopIndex(self) -> int:
        return self.__stopIndex

    @stopIndex.setter
    def stopIndex(self, stopIndex: int):
        self.__stopIndex = stopIndex

    @property
    def startIndex(self) -> int:
        return self.__startIndex

    @startIndex.setter
    def startIndex(self, startIndex: int):
        self.__startIndex = startIndex

    @property
    def startLineIndex(self) -> int:
        return self.__startLineIndex

    @startLineIndex.setter
    def startLineIndex(self, startLineIndex: int):
        self.__startLineIndex = startLineIndex

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Node__parentNode", None)
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
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Node__node", None)
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
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Node__Node13", None)
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Node__Node", None)
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
class Simpletree_Attribute(TreeElement):

    def __init__(self, value: str, attribute: "Simpletree_Node" = None, Attribute: "Simpletree_Node" = None):
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
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Attribute__attribute", None)
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

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Simpletree_Attribute__Attribute", None)
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

class Simpletree_Text(TreeElement):

    pass
class Simpletree_File(TreeElement):

    pass
class Simpletree_Folder(TreeElement):

    pass