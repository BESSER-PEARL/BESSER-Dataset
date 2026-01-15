from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MessageType(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    LOCKED = "LOCKED"
    NO_EDITING_RIGHTS = "NO_EDITING_RIGHTS"
    FILTERED = "FILTERED"
    UPDATE = "UPDATE"
    INFORMATION = "INFORMATION"


############################################
# Definition of Classes
############################################

class btsviewmodel_BTSObjectTypeTreeNode:

    def __init__(self, selected: bool, value: str, btsviewmodel_BTSObjectTypeTreeNode: "btsviewmodel_BTSObjectTypeTreeNode" = None, btsviewmodel_BTSObjectTypeTreeNode7: set["btsviewmodel_BTSObjectTypeTreeNode"] = None, btsviewmodel_BTSObjectTypeTreeNode11: "btsviewmodel_BTSObjectTypeTreeNode" = None, btsviewmodel_BTSObjectTypeTreeNode9: "btsviewmodel_BTSObjectTypeTreeNode" = None):
        self.selected = selected
        self.value = value
        self.btsviewmodel_BTSObjectTypeTreeNode = btsviewmodel_BTSObjectTypeTreeNode
        self.btsviewmodel_BTSObjectTypeTreeNode7 = btsviewmodel_BTSObjectTypeTreeNode7 if btsviewmodel_BTSObjectTypeTreeNode7 is not None else set()
        self.btsviewmodel_BTSObjectTypeTreeNode11 = btsviewmodel_BTSObjectTypeTreeNode11
        self.btsviewmodel_BTSObjectTypeTreeNode9 = btsviewmodel_BTSObjectTypeTreeNode9
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def btsviewmodel_BTSObjectTypeTreeNode11(self):
        return self.__btsviewmodel_BTSObjectTypeTreeNode11

    @btsviewmodel_BTSObjectTypeTreeNode11.setter
    def btsviewmodel_BTSObjectTypeTreeNode11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_BTSObjectTypeTreeNode__btsviewmodel_BTSObjectTypeTreeNode11", None)
        self.__btsviewmodel_BTSObjectTypeTreeNode11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode9"):
                opp_val = getattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode9", None)
                if opp_val == self:
                    setattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_BTSObjectTypeTreeNode9"):
                opp_val = getattr(value, "btsviewmodel_BTSObjectTypeTreeNode9", None)
                setattr(value, "btsviewmodel_BTSObjectTypeTreeNode9", self)

    @property
    def btsviewmodel_BTSObjectTypeTreeNode(self):
        return self.__btsviewmodel_BTSObjectTypeTreeNode

    @btsviewmodel_BTSObjectTypeTreeNode.setter
    def btsviewmodel_BTSObjectTypeTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_BTSObjectTypeTreeNode__btsviewmodel_BTSObjectTypeTreeNode", None)
        self.__btsviewmodel_BTSObjectTypeTreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode7"):
                opp_val = getattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_BTSObjectTypeTreeNode7"):
                opp_val = getattr(value, "btsviewmodel_BTSObjectTypeTreeNode7", None)
                if opp_val is None:
                    setattr(value, "btsviewmodel_BTSObjectTypeTreeNode7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def btsviewmodel_BTSObjectTypeTreeNode9(self):
        return self.__btsviewmodel_BTSObjectTypeTreeNode9

    @btsviewmodel_BTSObjectTypeTreeNode9.setter
    def btsviewmodel_BTSObjectTypeTreeNode9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_BTSObjectTypeTreeNode__btsviewmodel_BTSObjectTypeTreeNode9", None)
        self.__btsviewmodel_BTSObjectTypeTreeNode9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode11"):
                opp_val = getattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode11", None)
                if opp_val == self:
                    setattr(old_value, "btsviewmodel_BTSObjectTypeTreeNode11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_BTSObjectTypeTreeNode11"):
                opp_val = getattr(value, "btsviewmodel_BTSObjectTypeTreeNode11", None)
                setattr(value, "btsviewmodel_BTSObjectTypeTreeNode11", self)

    @property
    def btsviewmodel_BTSObjectTypeTreeNode7(self):
        return self.__btsviewmodel_BTSObjectTypeTreeNode7

    @btsviewmodel_BTSObjectTypeTreeNode7.setter
    def btsviewmodel_BTSObjectTypeTreeNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_BTSObjectTypeTreeNode__btsviewmodel_BTSObjectTypeTreeNode7", None)
        self.__btsviewmodel_BTSObjectTypeTreeNode7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "btsviewmodel_BTSObjectTypeTreeNode"):
                    opp_val = getattr(item, "btsviewmodel_BTSObjectTypeTreeNode", None)
                    
                    if opp_val == self:
                        setattr(item, "btsviewmodel_BTSObjectTypeTreeNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "btsviewmodel_BTSObjectTypeTreeNode"):
                    opp_val = getattr(item, "btsviewmodel_BTSObjectTypeTreeNode", None)
                    
                    setattr(item, "btsviewmodel_BTSObjectTypeTreeNode", self)
                    

class btsviewmodel_StatusMessage:

    def __init__(self, message: str, creationTime: date, userId: str, messageType: str, btsviewmodel_StatusMessage: "btsviewmodel_StatusMessage" = None, btsviewmodel_StatusMessage5: set["btsviewmodel_StatusMessage"] = None):
        self.message = message
        self.creationTime = creationTime
        self.userId = userId
        self.messageType = messageType
        self.btsviewmodel_StatusMessage = btsviewmodel_StatusMessage
        self.btsviewmodel_StatusMessage5 = btsviewmodel_StatusMessage5 if btsviewmodel_StatusMessage5 is not None else set()
        
    @property
    def creationTime(self) -> date:
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: date):
        self.__creationTime = creationTime

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def messageType(self) -> str:
        return self.__messageType

    @messageType.setter
    def messageType(self, messageType: str):
        self.__messageType = messageType

    @property
    def btsviewmodel_StatusMessage(self):
        return self.__btsviewmodel_StatusMessage

    @btsviewmodel_StatusMessage.setter
    def btsviewmodel_StatusMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_StatusMessage__btsviewmodel_StatusMessage", None)
        self.__btsviewmodel_StatusMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_StatusMessage5"):
                opp_val = getattr(old_value, "btsviewmodel_StatusMessage5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_StatusMessage5"):
                opp_val = getattr(value, "btsviewmodel_StatusMessage5", None)
                if opp_val is None:
                    setattr(value, "btsviewmodel_StatusMessage5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def btsviewmodel_StatusMessage5(self):
        return self.__btsviewmodel_StatusMessage5

    @btsviewmodel_StatusMessage5.setter
    def btsviewmodel_StatusMessage5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_StatusMessage__btsviewmodel_StatusMessage5", None)
        self.__btsviewmodel_StatusMessage5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "btsviewmodel_StatusMessage"):
                    opp_val = getattr(item, "btsviewmodel_StatusMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "btsviewmodel_StatusMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "btsviewmodel_StatusMessage"):
                    opp_val = getattr(item, "btsviewmodel_StatusMessage", None)
                    
                    setattr(item, "btsviewmodel_StatusMessage", self)
                    

class btsviewmodel_DBCollectionStatusInformation:

    def __init__(self, dbCollectionName: str, dbDocCount: str, syncStatusToRemote: str, syncStatusFromRemote: str, indexDocCount: str, indexStatus: str, dbDiskSize: str, dbDocDelCount: str, dbPurgeSeq: str, dbUpdateSeq: str, indexUpdateSeq: str):
        self.dbCollectionName = dbCollectionName
        self.dbDocCount = dbDocCount
        self.syncStatusToRemote = syncStatusToRemote
        self.syncStatusFromRemote = syncStatusFromRemote
        self.indexDocCount = indexDocCount
        self.indexStatus = indexStatus
        self.dbDiskSize = dbDiskSize
        self.dbDocDelCount = dbDocDelCount
        self.dbPurgeSeq = dbPurgeSeq
        self.dbUpdateSeq = dbUpdateSeq
        self.indexUpdateSeq = indexUpdateSeq
        
    @property
    def indexDocCount(self) -> str:
        return self.__indexDocCount

    @indexDocCount.setter
    def indexDocCount(self, indexDocCount: str):
        self.__indexDocCount = indexDocCount

    @property
    def indexStatus(self) -> str:
        return self.__indexStatus

    @indexStatus.setter
    def indexStatus(self, indexStatus: str):
        self.__indexStatus = indexStatus

    @property
    def dbDocCount(self) -> str:
        return self.__dbDocCount

    @dbDocCount.setter
    def dbDocCount(self, dbDocCount: str):
        self.__dbDocCount = dbDocCount

    @property
    def dbUpdateSeq(self) -> str:
        return self.__dbUpdateSeq

    @dbUpdateSeq.setter
    def dbUpdateSeq(self, dbUpdateSeq: str):
        self.__dbUpdateSeq = dbUpdateSeq

    @property
    def dbDocDelCount(self) -> str:
        return self.__dbDocDelCount

    @dbDocDelCount.setter
    def dbDocDelCount(self, dbDocDelCount: str):
        self.__dbDocDelCount = dbDocDelCount

    @property
    def indexUpdateSeq(self) -> str:
        return self.__indexUpdateSeq

    @indexUpdateSeq.setter
    def indexUpdateSeq(self, indexUpdateSeq: str):
        self.__indexUpdateSeq = indexUpdateSeq

    @property
    def dbCollectionName(self) -> str:
        return self.__dbCollectionName

    @dbCollectionName.setter
    def dbCollectionName(self, dbCollectionName: str):
        self.__dbCollectionName = dbCollectionName

    @property
    def syncStatusFromRemote(self) -> str:
        return self.__syncStatusFromRemote

    @syncStatusFromRemote.setter
    def syncStatusFromRemote(self, syncStatusFromRemote: str):
        self.__syncStatusFromRemote = syncStatusFromRemote

    @property
    def dbPurgeSeq(self) -> str:
        return self.__dbPurgeSeq

    @dbPurgeSeq.setter
    def dbPurgeSeq(self, dbPurgeSeq: str):
        self.__dbPurgeSeq = dbPurgeSeq

    @property
    def syncStatusToRemote(self) -> str:
        return self.__syncStatusToRemote

    @syncStatusToRemote.setter
    def syncStatusToRemote(self, syncStatusToRemote: str):
        self.__syncStatusToRemote = syncStatusToRemote

    @property
    def dbDiskSize(self) -> str:
        return self.__dbDiskSize

    @dbDiskSize.setter
    def dbDiskSize(self, dbDiskSize: str):
        self.__dbDiskSize = dbDiskSize

class btsviewmodel_TreeNodeWrapper:

    def __init__(self, object: str, propertyChangeSupport: str, childrenLoaded: bool, label: str, parentObject: str, btsviewmodel_TreeNodeWrapper: "btsviewmodel_TreeNodeWrapper" = None, btsviewmodel_TreeNodeWrapper0: "btsviewmodel_TreeNodeWrapper" = None, btsviewmodel_TreeNodeWrapper4: "btsviewmodel_TreeNodeWrapper" = None, btsviewmodel_TreeNodeWrapper2: set["btsviewmodel_TreeNodeWrapper"] = None):
        self.object = object
        self.propertyChangeSupport = propertyChangeSupport
        self.childrenLoaded = childrenLoaded
        self.label = label
        self.parentObject = parentObject
        self.btsviewmodel_TreeNodeWrapper = btsviewmodel_TreeNodeWrapper
        self.btsviewmodel_TreeNodeWrapper0 = btsviewmodel_TreeNodeWrapper0
        self.btsviewmodel_TreeNodeWrapper4 = btsviewmodel_TreeNodeWrapper4
        self.btsviewmodel_TreeNodeWrapper2 = btsviewmodel_TreeNodeWrapper2 if btsviewmodel_TreeNodeWrapper2 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

    @property
    def propertyChangeSupport(self) -> str:
        return self.__propertyChangeSupport

    @propertyChangeSupport.setter
    def propertyChangeSupport(self, propertyChangeSupport: str):
        self.__propertyChangeSupport = propertyChangeSupport

    @property
    def childrenLoaded(self) -> bool:
        return self.__childrenLoaded

    @childrenLoaded.setter
    def childrenLoaded(self, childrenLoaded: bool):
        self.__childrenLoaded = childrenLoaded

    @property
    def parentObject(self) -> str:
        return self.__parentObject

    @parentObject.setter
    def parentObject(self, parentObject: str):
        self.__parentObject = parentObject

    @property
    def btsviewmodel_TreeNodeWrapper2(self):
        return self.__btsviewmodel_TreeNodeWrapper2

    @btsviewmodel_TreeNodeWrapper2.setter
    def btsviewmodel_TreeNodeWrapper2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_TreeNodeWrapper__btsviewmodel_TreeNodeWrapper2", None)
        self.__btsviewmodel_TreeNodeWrapper2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "btsviewmodel_TreeNodeWrapper4"):
                    opp_val = getattr(item, "btsviewmodel_TreeNodeWrapper4", None)
                    
                    if opp_val == self:
                        setattr(item, "btsviewmodel_TreeNodeWrapper4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "btsviewmodel_TreeNodeWrapper4"):
                    opp_val = getattr(item, "btsviewmodel_TreeNodeWrapper4", None)
                    
                    setattr(item, "btsviewmodel_TreeNodeWrapper4", self)
                    

    @property
    def btsviewmodel_TreeNodeWrapper4(self):
        return self.__btsviewmodel_TreeNodeWrapper4

    @btsviewmodel_TreeNodeWrapper4.setter
    def btsviewmodel_TreeNodeWrapper4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_TreeNodeWrapper__btsviewmodel_TreeNodeWrapper4", None)
        self.__btsviewmodel_TreeNodeWrapper4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_TreeNodeWrapper2"):
                opp_val = getattr(old_value, "btsviewmodel_TreeNodeWrapper2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_TreeNodeWrapper2"):
                opp_val = getattr(value, "btsviewmodel_TreeNodeWrapper2", None)
                if opp_val is None:
                    setattr(value, "btsviewmodel_TreeNodeWrapper2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def btsviewmodel_TreeNodeWrapper0(self):
        return self.__btsviewmodel_TreeNodeWrapper0

    @btsviewmodel_TreeNodeWrapper0.setter
    def btsviewmodel_TreeNodeWrapper0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_TreeNodeWrapper__btsviewmodel_TreeNodeWrapper0", None)
        self.__btsviewmodel_TreeNodeWrapper0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_TreeNodeWrapper"):
                opp_val = getattr(old_value, "btsviewmodel_TreeNodeWrapper", None)
                if opp_val == self:
                    setattr(old_value, "btsviewmodel_TreeNodeWrapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_TreeNodeWrapper"):
                opp_val = getattr(value, "btsviewmodel_TreeNodeWrapper", None)
                setattr(value, "btsviewmodel_TreeNodeWrapper", self)

    @property
    def btsviewmodel_TreeNodeWrapper(self):
        return self.__btsviewmodel_TreeNodeWrapper

    @btsviewmodel_TreeNodeWrapper.setter
    def btsviewmodel_TreeNodeWrapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_btsviewmodel_TreeNodeWrapper__btsviewmodel_TreeNodeWrapper", None)
        self.__btsviewmodel_TreeNodeWrapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "btsviewmodel_TreeNodeWrapper0"):
                opp_val = getattr(old_value, "btsviewmodel_TreeNodeWrapper0", None)
                if opp_val == self:
                    setattr(old_value, "btsviewmodel_TreeNodeWrapper0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "btsviewmodel_TreeNodeWrapper0"):
                opp_val = getattr(value, "btsviewmodel_TreeNodeWrapper0", None)
                setattr(value, "btsviewmodel_TreeNodeWrapper0", self)

    def removePropertyChangeListener(self, propertyChangeListener: str):
        # TODO: Implement removePropertyChangeListener method
        pass

    def addPropertyChangeListener(self, propertyChangeListener: str):
        # TODO: Implement addPropertyChangeListener method
        pass
