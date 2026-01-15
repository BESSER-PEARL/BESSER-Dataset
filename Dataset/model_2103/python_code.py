from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MocaTree_TreeElement(ABC):

    def __init__(self, index: int, name: str, MocaTree_TreeElement: "MocaTree_Link" = None, MocaTree_TreeElement22: set["MocaTree_Link"] = None):
        self.index = index
        self.name = name
        self.MocaTree_TreeElement = MocaTree_TreeElement
        self.MocaTree_TreeElement22 = MocaTree_TreeElement22 if MocaTree_TreeElement22 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def MocaTree_TreeElement(self):
        return self.__MocaTree_TreeElement

    @MocaTree_TreeElement.setter
    def MocaTree_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_TreeElement__MocaTree_TreeElement", None)
        self.__MocaTree_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MocaTree_Link"):
                opp_val = getattr(old_value, "MocaTree_Link", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MocaTree_Link"):
                opp_val = getattr(value, "MocaTree_Link", None)
                if opp_val is None:
                    setattr(value, "MocaTree_Link", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MocaTree_TreeElement22(self):
        return self.__MocaTree_TreeElement22

    @MocaTree_TreeElement22.setter
    def MocaTree_TreeElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_TreeElement__MocaTree_TreeElement22", None)
        self.__MocaTree_TreeElement22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MocaTree_Link23"):
                    opp_val = getattr(item, "MocaTree_Link23", None)
                    
                    if opp_val == self:
                        setattr(item, "MocaTree_Link23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MocaTree_Link23"):
                    opp_val = getattr(item, "MocaTree_Link23", None)
                    
                    setattr(item, "MocaTree_Link23", self)
                    

class Text:

    pass
class TreeElement:

    pass
class MocaTree_Text(TreeElement):

    pass
class MocaTree_File(TreeElement):

    pass
class MocaTree_Link(TreeElement):

    pass
class MocaTree_Folder(TreeElement):

    pass
class MocaTree_Attribute(TreeElement):

    def __init__(self, value: str, attribute: "MocaTree_Node" = None, MocaTree_Attribute: "MocaTree_Link" = None, Attribute: "MocaTree_Node" = None):
        self.value = value
        self.attribute = attribute
        self.MocaTree_Attribute = MocaTree_Attribute
        self.Attribute = Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def MocaTree_Attribute(self):
        return self.__MocaTree_Attribute

    @MocaTree_Attribute.setter
    def MocaTree_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Attribute__MocaTree_Attribute", None)
        self.__MocaTree_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MocaTree_Link14"):
                opp_val = getattr(old_value, "MocaTree_Link14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MocaTree_Link14"):
                opp_val = getattr(value, "MocaTree_Link14", None)
                if opp_val is None:
                    setattr(value, "MocaTree_Link14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Attribute__attribute", None)
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
        old_value = getattr(self, f"_MocaTree_Attribute__Attribute", None)
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

class MocaTree_Node(Text):

    def __init__(self, stopIndex: int, stopLineIndex: int, startIndex: int, startLineIndex: int, Node: "MocaTree_Attribute" = None, Node4: "MocaTree_File" = None, rootNode: "MocaTree_File" = None, Node20: "MocaTree_Text" = None, parentNode: set["MocaTree_Text"] = None, node: set["MocaTree_Attribute"] = None):
        self.stopIndex = stopIndex
        self.stopLineIndex = stopLineIndex
        self.startIndex = startIndex
        self.startLineIndex = startLineIndex
        self.Node = Node
        self.Node4 = Node4
        self.rootNode = rootNode
        self.Node20 = Node20
        self.parentNode = parentNode if parentNode is not None else set()
        self.node = node if node is not None else set()
        
    @property
    def startLineIndex(self) -> int:
        return self.__startLineIndex

    @startLineIndex.setter
    def startLineIndex(self, startLineIndex: int):
        self.__startLineIndex = startLineIndex

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
    def rootNode(self):
        return self.__rootNode

    @rootNode.setter
    def rootNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Node__rootNode", None)
        self.__rootNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File16"):
                opp_val = getattr(old_value, "File16", None)
                if opp_val == self:
                    setattr(old_value, "File16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File16"):
                opp_val = getattr(value, "File16", None)
                setattr(value, "File16", self)

    @property
    def parentNode(self):
        return self.__parentNode

    @parentNode.setter
    def parentNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Node__parentNode", None)
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
        old_value = getattr(self, f"_MocaTree_Node__node", None)
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
    def Node20(self):
        return self.__Node20

    @Node20.setter
    def Node20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Node__Node20", None)
        self.__Node20 = value
        
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
        old_value = getattr(self, f"_MocaTree_Node__Node", None)
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

    @property
    def Node4(self):
        return self.__Node4

    @Node4.setter
    def Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MocaTree_Node__Node4", None)
        self.__Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "file3"):
                opp_val = getattr(old_value, "file3", None)
                if opp_val == self:
                    setattr(old_value, "file3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "file3"):
                opp_val = getattr(value, "file3", None)
                setattr(value, "file3", self)
