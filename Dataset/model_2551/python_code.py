from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectState(Enum):
    NEW = "NEW"
    PRODUCTION = "PRODUCTION"
    MODIFICATION = "MODIFICATION"
    DELETION = "DELETION"


############################################
# Definition of Classes
############################################

class BasicNotificationDefinition:

    pass
class model_NotificationDefinition(BasicNotificationDefinition):

    def __init__(self, includeFilter: str, excludeFilter: str, template: bool):
        self.includeFilter = includeFilter
        self.excludeFilter = excludeFilter
        self.template = template
        
    @property
    def excludeFilter(self) -> str:
        return self.__excludeFilter

    @excludeFilter.setter
    def excludeFilter(self, excludeFilter: str):
        self.__excludeFilter = excludeFilter

    @property
    def template(self) -> bool:
        return self.__template

    @template.setter
    def template(self, template: bool):
        self.__template = template

    @property
    def includeFilter(self) -> str:
        return self.__includeFilter

    @includeFilter.setter
    def includeFilter(self, includeFilter: str):
        self.__includeFilter = includeFilter

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class model_NotificationParticipant:

    def __init__(self, mailAddress: str, id: str, groupId: str, model_NotificationParticipant: "model_ObjectRef" = None, model_NotificationParticipant10: "model_BasicNotificationDefinition" = None, model_NotificationParticipant13: "model_BasicNotificationDefinition" = None, model_NotificationParticipant16: "model_BasicNotificationDefinition" = None, model_NotificationParticipant19: "model_BasicNotificationDefinition" = None):
        self.mailAddress = mailAddress
        self.id = id
        self.groupId = groupId
        self.model_NotificationParticipant = model_NotificationParticipant
        self.model_NotificationParticipant10 = model_NotificationParticipant10
        self.model_NotificationParticipant13 = model_NotificationParticipant13
        self.model_NotificationParticipant16 = model_NotificationParticipant16
        self.model_NotificationParticipant19 = model_NotificationParticipant19
        
    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def mailAddress(self) -> str:
        return self.__mailAddress

    @mailAddress.setter
    def mailAddress(self, mailAddress: str):
        self.__mailAddress = mailAddress

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def model_NotificationParticipant16(self):
        return self.__model_NotificationParticipant16

    @model_NotificationParticipant16.setter
    def model_NotificationParticipant16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_NotificationParticipant__model_NotificationParticipant16", None)
        self.__model_NotificationParticipant16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicNotificationDefinition15"):
                opp_val = getattr(old_value, "model_BasicNotificationDefinition15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicNotificationDefinition15"):
                opp_val = getattr(value, "model_BasicNotificationDefinition15", None)
                if opp_val is None:
                    setattr(value, "model_BasicNotificationDefinition15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_NotificationParticipant10(self):
        return self.__model_NotificationParticipant10

    @model_NotificationParticipant10.setter
    def model_NotificationParticipant10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_NotificationParticipant__model_NotificationParticipant10", None)
        self.__model_NotificationParticipant10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicNotificationDefinition"):
                opp_val = getattr(old_value, "model_BasicNotificationDefinition", None)
                if opp_val == self:
                    setattr(old_value, "model_BasicNotificationDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicNotificationDefinition"):
                opp_val = getattr(value, "model_BasicNotificationDefinition", None)
                setattr(value, "model_BasicNotificationDefinition", self)

    @property
    def model_NotificationParticipant13(self):
        return self.__model_NotificationParticipant13

    @model_NotificationParticipant13.setter
    def model_NotificationParticipant13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_NotificationParticipant__model_NotificationParticipant13", None)
        self.__model_NotificationParticipant13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicNotificationDefinition12"):
                opp_val = getattr(old_value, "model_BasicNotificationDefinition12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicNotificationDefinition12"):
                opp_val = getattr(value, "model_BasicNotificationDefinition12", None)
                if opp_val is None:
                    setattr(value, "model_BasicNotificationDefinition12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_NotificationParticipant19(self):
        return self.__model_NotificationParticipant19

    @model_NotificationParticipant19.setter
    def model_NotificationParticipant19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_NotificationParticipant__model_NotificationParticipant19", None)
        self.__model_NotificationParticipant19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicNotificationDefinition18"):
                opp_val = getattr(old_value, "model_BasicNotificationDefinition18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicNotificationDefinition18"):
                opp_val = getattr(value, "model_BasicNotificationDefinition18", None)
                if opp_val is None:
                    setattr(value, "model_BasicNotificationDefinition18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_NotificationParticipant(self):
        return self.__model_NotificationParticipant

    @model_NotificationParticipant.setter
    def model_NotificationParticipant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_NotificationParticipant__model_NotificationParticipant", None)
        self.__model_NotificationParticipant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ObjectRef8"):
                opp_val = getattr(old_value, "model_ObjectRef8", None)
                if opp_val == self:
                    setattr(old_value, "model_ObjectRef8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ObjectRef8"):
                opp_val = getattr(value, "model_ObjectRef8", None)
                setattr(value, "model_ObjectRef8", self)

class model_CodeEntry:

    def __init__(self, id: str, key: str, value: str, model_CodeEntry: "model_BasicCode" = None):
        self.id = id
        self.key = key
        self.value = value
        self.model_CodeEntry = model_CodeEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def model_CodeEntry(self):
        return self.__model_CodeEntry

    @model_CodeEntry.setter
    def model_CodeEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CodeEntry__model_CodeEntry", None)
        self.__model_CodeEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicCode6"):
                opp_val = getattr(old_value, "model_BasicCode6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicCode6"):
                opp_val = getattr(value, "model_BasicCode6", None)
                if opp_val is None:
                    setattr(value, "model_BasicCode6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BasicCode:

    pass
class model_Category(BasicCode):

    def __init__(self, classifier: str, associatedClassifier: str):
        self.classifier = classifier
        self.associatedClassifier = associatedClassifier
        
    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

    @property
    def associatedClassifier(self) -> str:
        return self.__associatedClassifier

    @associatedClassifier.setter
    def associatedClassifier(self, associatedClassifier: str):
        self.__associatedClassifier = associatedClassifier

class model_Code(BasicCode):

    pass
class model_BasicCode(ABC):

    def __init__(self, id: str, sortHint: int, domain: int, active: bool, structure: bool, names: str, descriptions: str, model_BasicCode: "model_BasicCode" = None, model_BasicCode3: "model_BasicCode" = None, model_BasicCode6: set["model_CodeEntry"] = None):
        self.id = id
        self.sortHint = sortHint
        self.domain = domain
        self.active = active
        self.structure = structure
        self.names = names
        self.descriptions = descriptions
        self.model_BasicCode = model_BasicCode
        self.model_BasicCode3 = model_BasicCode3
        self.model_BasicCode6 = model_BasicCode6 if model_BasicCode6 is not None else set()
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def structure(self) -> bool:
        return self.__structure

    @structure.setter
    def structure(self, structure: bool):
        self.__structure = structure

    @property
    def sortHint(self) -> int:
        return self.__sortHint

    @sortHint.setter
    def sortHint(self, sortHint: int):
        self.__sortHint = sortHint

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def domain(self) -> int:
        return self.__domain

    @domain.setter
    def domain(self, domain: int):
        self.__domain = domain

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def descriptions(self) -> str:
        return self.__descriptions

    @descriptions.setter
    def descriptions(self, descriptions: str):
        self.__descriptions = descriptions

    @property
    def model_BasicCode6(self):
        return self.__model_BasicCode6

    @model_BasicCode6.setter
    def model_BasicCode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicCode__model_BasicCode6", None)
        self.__model_BasicCode6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_CodeEntry"):
                    opp_val = getattr(item, "model_CodeEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "model_CodeEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_CodeEntry"):
                    opp_val = getattr(item, "model_CodeEntry", None)
                    
                    setattr(item, "model_CodeEntry", self)
                    

    @property
    def model_BasicCode3(self):
        return self.__model_BasicCode3

    @model_BasicCode3.setter
    def model_BasicCode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicCode__model_BasicCode3", None)
        self.__model_BasicCode3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicCode"):
                opp_val = getattr(old_value, "model_BasicCode", None)
                if opp_val == self:
                    setattr(old_value, "model_BasicCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicCode"):
                opp_val = getattr(value, "model_BasicCode", None)
                setattr(value, "model_BasicCode", self)

    @property
    def model_BasicCode(self):
        return self.__model_BasicCode

    @model_BasicCode.setter
    def model_BasicCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicCode__model_BasicCode", None)
        self.__model_BasicCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicCode3"):
                opp_val = getattr(old_value, "model_BasicCode3", None)
                if opp_val == self:
                    setattr(old_value, "model_BasicCode3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicCode3"):
                opp_val = getattr(value, "model_BasicCode3", None)
                setattr(value, "model_BasicCode3", self)

    def getSegments(self) -> str:
        # TODO: Implement getSegments method
        pass

    def getLastSegment(self) -> str:
        # TODO: Implement getLastSegment method
        pass

    def getFirstSegment(self) -> str:
        # TODO: Implement getFirstSegment method
        pass

    def setParentPath(self, parent: str):
        # TODO: Implement setParentPath method
        pass

    def getPureLastSegment(self) -> str:
        # TODO: Implement getPureLastSegment method
        pass

class model_TreeNodeChild:

    def __init__(self, nodeId: str, TreeNodeChild: "model_TreeNode" = None, childs: "model_TreeNode" = None):
        self.nodeId = nodeId
        self.TreeNodeChild = TreeNodeChild
        self.childs = childs
        
    @property
    def nodeId(self) -> str:
        return self.__nodeId

    @nodeId.setter
    def nodeId(self, nodeId: str):
        self.__nodeId = nodeId

    @property
    def TreeNodeChild(self):
        return self.__TreeNodeChild

    @TreeNodeChild.setter
    def TreeNodeChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TreeNodeChild__TreeNodeChild", None)
        self.__TreeNodeChild = value
        
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
    def childs(self):
        return self.__childs

    @childs.setter
    def childs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TreeNodeChild__childs", None)
        self.__childs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeNode"):
                opp_val = getattr(old_value, "TreeNode", None)
                if opp_val == self:
                    setattr(old_value, "TreeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeNode"):
                opp_val = getattr(value, "TreeNode", None)
                setattr(value, "TreeNode", self)

class model_BasicObject(ABC):

    def __init__(self, domain: int, locale: str, id: str):
        self.domain = domain
        self.locale = locale
        self.id = id
        
    @property
    def locale(self) -> str:
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale

    @property
    def domain(self) -> int:
        return self.__domain

    @domain.setter
    def domain(self, domain: int):
        self.__domain = domain

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class model_ObjectRef:

    def __init__(self, nature: str, id: str, domain: int, state: str, labels: str, appId: str, type: str, model_ObjectRef: "model_TreeNode" = None, model_ObjectRef8: "model_NotificationParticipant" = None):
        self.nature = nature
        self.id = id
        self.domain = domain
        self.state = state
        self.labels = labels
        self.appId = appId
        self.type = type
        self.model_ObjectRef = model_ObjectRef
        self.model_ObjectRef8 = model_ObjectRef8
        
    @property
    def domain(self) -> int:
        return self.__domain

    @domain.setter
    def domain(self, domain: int):
        self.__domain = domain

    @property
    def appId(self) -> str:
        return self.__appId

    @appId.setter
    def appId(self, appId: str):
        self.__appId = appId

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def labels(self) -> str:
        return self.__labels

    @labels.setter
    def labels(self, labels: str):
        self.__labels = labels

    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_ObjectRef(self):
        return self.__model_ObjectRef

    @model_ObjectRef.setter
    def model_ObjectRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ObjectRef__model_ObjectRef", None)
        self.__model_ObjectRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TreeNode"):
                opp_val = getattr(old_value, "model_TreeNode", None)
                if opp_val == self:
                    setattr(old_value, "model_TreeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TreeNode"):
                opp_val = getattr(value, "model_TreeNode", None)
                setattr(value, "model_TreeNode", self)

    @property
    def model_ObjectRef8(self):
        return self.__model_ObjectRef8

    @model_ObjectRef8.setter
    def model_ObjectRef8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ObjectRef__model_ObjectRef8", None)
        self.__model_ObjectRef8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_NotificationParticipant"):
                opp_val = getattr(old_value, "model_NotificationParticipant", None)
                if opp_val == self:
                    setattr(old_value, "model_NotificationParticipant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_NotificationParticipant"):
                opp_val = getattr(value, "model_NotificationParticipant", None)
                setattr(value, "model_NotificationParticipant", self)

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

    def getWorkingId(self) -> str:
        # TODO: Implement getWorkingId method
        pass

    def getDefaultLocale(self) -> str:
        # TODO: Implement getDefaultLocale method
        pass

    def getDefaultLabel(self) -> str:
        # TODO: Implement getDefaultLabel method
        pass

class BasicObject:

    pass
class model_BasicNotificationDefinition(BasicObject):

    def __init__(self, notificationEventId: str, identifier: str, active: bool, description: str, model_BasicNotificationDefinition18: set["model_NotificationParticipant"] = None, model_BasicNotificationDefinition21: "model_Code" = None, model_BasicNotificationDefinition: "model_NotificationParticipant" = None, model_BasicNotificationDefinition12: set["model_NotificationParticipant"] = None, model_BasicNotificationDefinition15: set["model_NotificationParticipant"] = None):
        self.notificationEventId = notificationEventId
        self.identifier = identifier
        self.active = active
        self.description = description
        self.model_BasicNotificationDefinition18 = model_BasicNotificationDefinition18 if model_BasicNotificationDefinition18 is not None else set()
        self.model_BasicNotificationDefinition21 = model_BasicNotificationDefinition21
        self.model_BasicNotificationDefinition = model_BasicNotificationDefinition
        self.model_BasicNotificationDefinition12 = model_BasicNotificationDefinition12 if model_BasicNotificationDefinition12 is not None else set()
        self.model_BasicNotificationDefinition15 = model_BasicNotificationDefinition15 if model_BasicNotificationDefinition15 is not None else set()
        
    @property
    def notificationEventId(self) -> str:
        return self.__notificationEventId

    @notificationEventId.setter
    def notificationEventId(self, notificationEventId: str):
        self.__notificationEventId = notificationEventId

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def model_BasicNotificationDefinition(self):
        return self.__model_BasicNotificationDefinition

    @model_BasicNotificationDefinition.setter
    def model_BasicNotificationDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicNotificationDefinition__model_BasicNotificationDefinition", None)
        self.__model_BasicNotificationDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_NotificationParticipant10"):
                opp_val = getattr(old_value, "model_NotificationParticipant10", None)
                if opp_val == self:
                    setattr(old_value, "model_NotificationParticipant10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_NotificationParticipant10"):
                opp_val = getattr(value, "model_NotificationParticipant10", None)
                setattr(value, "model_NotificationParticipant10", self)

    @property
    def model_BasicNotificationDefinition18(self):
        return self.__model_BasicNotificationDefinition18

    @model_BasicNotificationDefinition18.setter
    def model_BasicNotificationDefinition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicNotificationDefinition__model_BasicNotificationDefinition18", None)
        self.__model_BasicNotificationDefinition18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_NotificationParticipant19"):
                    opp_val = getattr(item, "model_NotificationParticipant19", None)
                    
                    if opp_val == self:
                        setattr(item, "model_NotificationParticipant19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_NotificationParticipant19"):
                    opp_val = getattr(item, "model_NotificationParticipant19", None)
                    
                    setattr(item, "model_NotificationParticipant19", self)
                    

    @property
    def model_BasicNotificationDefinition21(self):
        return self.__model_BasicNotificationDefinition21

    @model_BasicNotificationDefinition21.setter
    def model_BasicNotificationDefinition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicNotificationDefinition__model_BasicNotificationDefinition21", None)
        self.__model_BasicNotificationDefinition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Code"):
                opp_val = getattr(old_value, "model_Code", None)
                if opp_val == self:
                    setattr(old_value, "model_Code", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Code"):
                opp_val = getattr(value, "model_Code", None)
                setattr(value, "model_Code", self)

    @property
    def model_BasicNotificationDefinition15(self):
        return self.__model_BasicNotificationDefinition15

    @model_BasicNotificationDefinition15.setter
    def model_BasicNotificationDefinition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicNotificationDefinition__model_BasicNotificationDefinition15", None)
        self.__model_BasicNotificationDefinition15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_NotificationParticipant16"):
                    opp_val = getattr(item, "model_NotificationParticipant16", None)
                    
                    if opp_val == self:
                        setattr(item, "model_NotificationParticipant16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_NotificationParticipant16"):
                    opp_val = getattr(item, "model_NotificationParticipant16", None)
                    
                    setattr(item, "model_NotificationParticipant16", self)
                    

    @property
    def model_BasicNotificationDefinition12(self):
        return self.__model_BasicNotificationDefinition12

    @model_BasicNotificationDefinition12.setter
    def model_BasicNotificationDefinition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BasicNotificationDefinition__model_BasicNotificationDefinition12", None)
        self.__model_BasicNotificationDefinition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_NotificationParticipant13"):
                    opp_val = getattr(item, "model_NotificationParticipant13", None)
                    
                    if opp_val == self:
                        setattr(item, "model_NotificationParticipant13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_NotificationParticipant13"):
                    opp_val = getattr(item, "model_NotificationParticipant13", None)
                    
                    setattr(item, "model_NotificationParticipant13", self)
                    

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class model_TreeNode(BasicObject):

    def __init__(self, name: str, parent: set["model_TreeNodeChild"] = None, model_TreeNode: "model_ObjectRef" = None, TreeNode: "model_TreeNodeChild" = None):
        self.name = name
        self.parent = parent if parent is not None else set()
        self.model_TreeNode = model_TreeNode
        self.TreeNode = TreeNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TreeNode(self):
        return self.__TreeNode

    @TreeNode.setter
    def TreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TreeNode__TreeNode", None)
        self.__TreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childs"):
                opp_val = getattr(old_value, "childs", None)
                if opp_val == self:
                    setattr(old_value, "childs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childs"):
                opp_val = getattr(value, "childs", None)
                setattr(value, "childs", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TreeNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeNodeChild"):
                    opp_val = getattr(item, "TreeNodeChild", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeNodeChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeNodeChild"):
                    opp_val = getattr(item, "TreeNodeChild", None)
                    
                    setattr(item, "TreeNodeChild", self)
                    

    @property
    def model_TreeNode(self):
        return self.__model_TreeNode

    @model_TreeNode.setter
    def model_TreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TreeNode__model_TreeNode", None)
        self.__model_TreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ObjectRef"):
                opp_val = getattr(old_value, "model_ObjectRef", None)
                if opp_val == self:
                    setattr(old_value, "model_ObjectRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ObjectRef"):
                opp_val = getattr(value, "model_ObjectRef", None)
                setattr(value, "model_ObjectRef", self)

class model_Attachment(BasicObject):

    def __init__(self, key: str, objectId: str, data: str):
        self.key = key
        self.objectId = objectId
        self.data = data
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def objectId(self) -> str:
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: str):
        self.__objectId = objectId

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data
