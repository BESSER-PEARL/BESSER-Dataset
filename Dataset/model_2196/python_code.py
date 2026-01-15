from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_DoorsTreeNode(ABC):

    def __init__(self, name: str, fullName: str, fullNameSegments: str, DoorsTreeNode6: "model_DoorsTreeNode" = None, children: "model_DoorsTreeNode" = None, model_DoorsTreeNode: set["model_AttributeMap"] = None, DoorsTreeNode: "model_DoorsTreeNode" = None, parent: set["model_DoorsTreeNode"] = None):
        self.name = name
        self.fullName = fullName
        self.fullNameSegments = fullNameSegments
        self.DoorsTreeNode6 = DoorsTreeNode6
        self.children = children
        self.model_DoorsTreeNode = model_DoorsTreeNode if model_DoorsTreeNode is not None else set()
        self.DoorsTreeNode = DoorsTreeNode
        self.parent = parent if parent is not None else set()
        
    @property
    def fullNameSegments(self) -> str:
        return self.__fullNameSegments

    @fullNameSegments.setter
    def fullNameSegments(self, fullNameSegments: str):
        self.__fullNameSegments = fullNameSegments

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsTreeNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DoorsTreeNode6"):
                opp_val = getattr(old_value, "DoorsTreeNode6", None)
                if opp_val == self:
                    setattr(old_value, "DoorsTreeNode6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DoorsTreeNode6"):
                opp_val = getattr(value, "DoorsTreeNode6", None)
                setattr(value, "DoorsTreeNode6", self)

    @property
    def model_DoorsTreeNode(self):
        return self.__model_DoorsTreeNode

    @model_DoorsTreeNode.setter
    def model_DoorsTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsTreeNode__model_DoorsTreeNode", None)
        self.__model_DoorsTreeNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_AttributeMap"):
                    opp_val = getattr(item, "model_AttributeMap", None)
                    
                    if opp_val == self:
                        setattr(item, "model_AttributeMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_AttributeMap"):
                    opp_val = getattr(item, "model_AttributeMap", None)
                    
                    setattr(item, "model_AttributeMap", self)
                    

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsTreeNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DoorsTreeNode"):
                    opp_val = getattr(item, "DoorsTreeNode", None)
                    
                    if opp_val == self:
                        setattr(item, "DoorsTreeNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DoorsTreeNode"):
                    opp_val = getattr(item, "DoorsTreeNode", None)
                    
                    setattr(item, "DoorsTreeNode", self)
                    

    @property
    def DoorsTreeNode6(self):
        return self.__DoorsTreeNode6

    @DoorsTreeNode6.setter
    def DoorsTreeNode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsTreeNode__DoorsTreeNode6", None)
        self.__DoorsTreeNode6 = value
        
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
    def DoorsTreeNode(self):
        return self.__DoorsTreeNode

    @DoorsTreeNode.setter
    def DoorsTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsTreeNode__DoorsTreeNode", None)
        self.__DoorsTreeNode = value
        
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

    def removeTag(self, tag: str):
        # TODO: Implement removeTag method
        pass

    def hasTag(self, pattern: str) -> bool:
        # TODO: Implement hasTag method
        pass

    def hasTag(self, tag: str) -> bool:
        # TODO: Implement hasTag method
        pass

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

    def getTags(self) -> str:
        # TODO: Implement getTags method
        pass

    def getChild(self, name: str) -> DoorsTreeNode:
        # TODO: Implement getChild method
        pass

    def setTag(self, tag: str):
        # TODO: Implement setTag method
        pass

    def canCopyFrom(self, node: DoorsTreeNode) -> bool:
        # TODO: Implement canCopyFrom method
        pass

    def removeTag(self, pattern: str):
        # TODO: Implement removeTag method
        pass

class model_AttributeMap:

    def __init__(self, key: str, value: str, model_AttributeMap: "model_DoorsTreeNode" = None):
        self.key = key
        self.value = value
        self.model_AttributeMap = model_AttributeMap
        
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
    def model_AttributeMap(self):
        return self.__model_AttributeMap

    @model_AttributeMap.setter
    def model_AttributeMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AttributeMap__model_AttributeMap", None)
        self.__model_AttributeMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DoorsTreeNode"):
                opp_val = getattr(old_value, "model_DoorsTreeNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DoorsTreeNode"):
                opp_val = getattr(value, "model_DoorsTreeNode", None)
                if opp_val is None:
                    setattr(value, "model_DoorsTreeNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DoorsObject:

    pass
class model_DoorsTableRow(DoorsObject):

    pass
class model_DoorsLink:

    def __init__(self, targetModule: str, targetObject: str, DoorsLink: "model_DoorsObject" = None, outgoingLinks: "model_DoorsObject" = None):
        self.targetModule = targetModule
        self.targetObject = targetObject
        self.DoorsLink = DoorsLink
        self.outgoingLinks = outgoingLinks
        
    @property
    def targetModule(self) -> str:
        return self.__targetModule

    @targetModule.setter
    def targetModule(self, targetModule: str):
        self.__targetModule = targetModule

    @property
    def targetObject(self) -> str:
        return self.__targetObject

    @targetObject.setter
    def targetObject(self, targetObject: str):
        self.__targetObject = targetObject

    @property
    def outgoingLinks(self):
        return self.__outgoingLinks

    @outgoingLinks.setter
    def outgoingLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsLink__outgoingLinks", None)
        self.__outgoingLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DoorsObject"):
                opp_val = getattr(old_value, "DoorsObject", None)
                if opp_val == self:
                    setattr(old_value, "DoorsObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DoorsObject"):
                opp_val = getattr(value, "DoorsObject", None)
                setattr(value, "DoorsObject", self)

    @property
    def DoorsLink(self):
        return self.__DoorsLink

    @DoorsLink.setter
    def DoorsLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsLink__DoorsLink", None)
        self.__DoorsLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def resolve(self) -> DoorsObject:
        # TODO: Implement resolve method
        pass

    def resolve(self, sourceOverride: DoorsTreeNode) -> DoorsObject:
        # TODO: Implement resolve method
        pass

    def getLinkStatus(self) -> str:
        # TODO: Implement getLinkStatus method
        pass

class DoorsTreeNode:

    pass
class model_DoorsObject(DoorsTreeNode):

    def __init__(self, objectIdentifier: str, objectNumber: str, objectHeading: str, text: str, absoluteNumber: int, objectText: str, objectShortText: str, source: set["model_DoorsLink"] = None, DoorsObject: "model_DoorsLink" = None):
        self.objectIdentifier = objectIdentifier
        self.objectNumber = objectNumber
        self.objectHeading = objectHeading
        self.text = text
        self.absoluteNumber = absoluteNumber
        self.objectText = objectText
        self.objectShortText = objectShortText
        self.source = source if source is not None else set()
        self.DoorsObject = DoorsObject
        
    @property
    def objectNumber(self) -> str:
        return self.__objectNumber

    @objectNumber.setter
    def objectNumber(self, objectNumber: str):
        self.__objectNumber = objectNumber

    @property
    def objectShortText(self) -> str:
        return self.__objectShortText

    @objectShortText.setter
    def objectShortText(self, objectShortText: str):
        self.__objectShortText = objectShortText

    @property
    def absoluteNumber(self) -> int:
        return self.__absoluteNumber

    @absoluteNumber.setter
    def absoluteNumber(self, absoluteNumber: int):
        self.__absoluteNumber = absoluteNumber

    @property
    def objectHeading(self) -> str:
        return self.__objectHeading

    @objectHeading.setter
    def objectHeading(self, objectHeading: str):
        self.__objectHeading = objectHeading

    @property
    def objectIdentifier(self) -> str:
        return self.__objectIdentifier

    @objectIdentifier.setter
    def objectIdentifier(self, objectIdentifier: str):
        self.__objectIdentifier = objectIdentifier

    @property
    def objectText(self) -> str:
        return self.__objectText

    @objectText.setter
    def objectText(self, objectText: str):
        self.__objectText = objectText

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def DoorsObject(self):
        return self.__DoorsObject

    @DoorsObject.setter
    def DoorsObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsObject__DoorsObject", None)
        self.__DoorsObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingLinks"):
                opp_val = getattr(old_value, "outgoingLinks", None)
                if opp_val == self:
                    setattr(old_value, "outgoingLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingLinks"):
                opp_val = getattr(value, "outgoingLinks", None)
                setattr(value, "outgoingLinks", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DoorsObject__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DoorsLink"):
                    opp_val = getattr(item, "DoorsLink", None)
                    
                    if opp_val == self:
                        setattr(item, "DoorsLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DoorsLink"):
                    opp_val = getattr(item, "DoorsLink", None)
                    
                    setattr(item, "DoorsLink", self)
                    

    def isHeading(self) -> bool:
        # TODO: Implement isHeading method
        pass

    def getObjectLevel(self) -> int:
        # TODO: Implement getObjectLevel method
        pass

class model_DoorsModule(DoorsTreeNode):

    def __init__(self):
        
    def getObjectAttributes(self) -> str:
        # TODO: Implement getObjectAttributes method
        pass

    def setObjectAttributes(self, attrs: str):
        # TODO: Implement setObjectAttributes method
        pass

    def getView(self) -> str:
        # TODO: Implement getView method
        pass

class model_DoorsFolder(DoorsTreeNode):

    def __init__(self, project: bool):
        self.project = project
        
    @property
    def project(self) -> bool:
        return self.__project

    @project.setter
    def project(self, project: bool):
        self.__project = project
