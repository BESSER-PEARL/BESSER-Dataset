from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationType(Enum):
    UNDIRECTED_ASSOCIATION = "UNDIRECTED_ASSOCIATION"
    DIRECTED_ASSOCIATION = "DIRECTED_ASSOCIATION"
    AGGREGATION = "AGGREGATION"
    COMPOSITION = "COMPOSITION"
class Severity(Enum):
    FEATURE = "FEATURE"
    TRIVIAL = "TRIVIAL"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    BLOCKER = "BLOCKER"
class ContainmentType(Enum):
    NONE = "NONE"
    CONTAINER = "CONTAINER"
    CONTAINMENT = "CONTAINMENT"
class ActivityType(Enum):
    NONE = "NONE"
    ANALYSIS = "ANALYSIS"
    SYSTEM_DESIGN = "SYSTEM_DESIGN"
    OBJECT_DESIGN = "OBJECT_DESIGN"
    IMPLEMENTATION = "IMPLEMENTATION"
    TESTING = "TESTING"
    MANAGEMENT = "MANAGEMENT"
class ArgumentDirectionType(Enum):
    UNDEFINED = "UNDEFINED"
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class VisibilityType(Enum):
    UNDEFINED = "UNDEFINED"
    PACKAGE = "PACKAGE"
    PRIVATE = "PRIVATE"
    GLOBAL = "GLOBAL"
    PROTECTED = "PROTECTED"
class ResolutionType(Enum):
    FIXED = "FIXED"
    CANNOT_REPRODUCE = "CANNOT_REPRODUCE"
    WONT_FIX = "WONT_FIX"
class MergeGlobalChoiceSelection(Enum):
    AllMine = "AllMine"
    AllTheir = "AllTheir"
    Cancel = "Cancel"
    OKNotFinished = "OKNotFinished"
    OKFinished = "OKFinished"
class DiagramType(Enum):
    CLASS_DIAGRAM = "CLASS_DIAGRAM"
    USECASE_DIAGRAM = "USECASE_DIAGRAM"
    COMPONENT_DIAGRAM = "COMPONENT_DIAGRAM"
    STATE_DIAGRAM = "STATE_DIAGRAM"
    ACTIVITY_DIAGRAM = "ACTIVITY_DIAGRAM"
    WORKITEM_DIAGRAM = "WORKITEM_DIAGRAM"
class FileAttachmentType(Enum):
    BINARY = "BINARY"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
class MergeChoiceSelection(Enum):
    Mine = "Mine"
    Their = "Their"
    Issue = "Issue"
    MergedText = "MergedText"
class ScopeType(Enum):
    INSTANCE = "INSTANCE"
    CLASS = "CLASS"


############################################
# Definition of Classes
############################################

class url_ModelElementUrlFragment:

    pass
class url_ProjectUrlFragment:

    pass
class url_ServerUrl:

    pass
class esmodel_url_ModelElementUrl:

    pass
class esmodel_url_ModelElementUrlFragment:

    def __init__(self, name: str, esmodel_url_ModelElementUrlFragment: "ModelElementId" = None):
        self.name = name
        self.esmodel_url_ModelElementUrlFragment = esmodel_url_ModelElementUrlFragment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_url_ModelElementUrlFragment(self):
        return self.__esmodel_url_ModelElementUrlFragment

    @esmodel_url_ModelElementUrlFragment.setter
    def esmodel_url_ModelElementUrlFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_url_ModelElementUrlFragment__esmodel_url_ModelElementUrlFragment", None)
        self.__esmodel_url_ModelElementUrlFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId615"):
                opp_val = getattr(old_value, "ModelElementId615", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId615", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId615"):
                opp_val = getattr(value, "ModelElementId615", None)
                setattr(value, "ModelElementId615", self)

class esmodel_url_ProjectUrlFragment:

    def __init__(self, name: str, esmodel_url_ProjectUrlFragment: "ProjectId" = None):
        self.name = name
        self.esmodel_url_ProjectUrlFragment = esmodel_url_ProjectUrlFragment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_url_ProjectUrlFragment(self):
        return self.__esmodel_url_ProjectUrlFragment

    @esmodel_url_ProjectUrlFragment.setter
    def esmodel_url_ProjectUrlFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_url_ProjectUrlFragment__esmodel_url_ProjectUrlFragment", None)
        self.__esmodel_url_ProjectUrlFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectId613"):
                opp_val = getattr(old_value, "ProjectId613", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId613", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId613"):
                opp_val = getattr(value, "ProjectId613", None)
                setattr(value, "ProjectId613", self)

class esmodel_url_ServerUrl:

    def __init__(self, hostName: str, port: int):
        self.hostName = hostName
        self.port = port
        
    @property
    def hostName(self) -> str:
        return self.__hostName

    @hostName.setter
    def hostName(self, hostName: str):
        self.__hostName = hostName

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

class roles_Role:

    pass
class Role:

    pass
class esmodel_roles_ProjectAdminRole(Role):

    pass
class esmodel_roles_WriterRole(Role):

    pass
class esmodel_roles_ServerAdmin(Role):

    pass
class esmodel_roles_ReaderRole(Role):

    pass
class esmodel_roles_Role(ABC):

    def __init__(self, esmodel_roles_Role: set["ProjectId"] = None):
        self.esmodel_roles_Role = esmodel_roles_Role if esmodel_roles_Role is not None else set()
        
    @property
    def esmodel_roles_Role(self):
        return self.__esmodel_roles_Role

    @esmodel_roles_Role.setter
    def esmodel_roles_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_roles_Role__esmodel_roles_Role", None)
        self.__esmodel_roles_Role = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProjectId603"):
                    opp_val = getattr(item, "ProjectId603", None)
                    
                    if opp_val == self:
                        setattr(item, "ProjectId603", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProjectId603"):
                    opp_val = getattr(item, "ProjectId603", None)
                    
                    setattr(item, "ProjectId603", self)
                    

    def canDelete(self, modelElement: str, projectId: str) -> bool:
        # TODO: Implement canDelete method
        pass

    def canRead(self, projectId: str, modelElement: str) -> bool:
        # TODO: Implement canRead method
        pass

    def canAdministrate(self, projectId: str) -> bool:
        # TODO: Implement canAdministrate method
        pass

    def canModify(self, projectId: str, modelElement: str) -> bool:
        # TODO: Implement canModify method
        pass

    def canCreate(self, modelElement: str, projectId: str) -> bool:
        # TODO: Implement canCreate method
        pass

class esmodel_accesscontrol_OrgUnitProperty:

    def __init__(self, name: str, value: str, esmodel_accesscontrol_OrgUnitProperty: "ProjectId" = None):
        self.name = name
        self.value = value
        self.esmodel_accesscontrol_OrgUnitProperty = esmodel_accesscontrol_OrgUnitProperty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def esmodel_accesscontrol_OrgUnitProperty(self):
        return self.__esmodel_accesscontrol_OrgUnitProperty

    @esmodel_accesscontrol_OrgUnitProperty.setter
    def esmodel_accesscontrol_OrgUnitProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_accesscontrol_OrgUnitProperty__esmodel_accesscontrol_OrgUnitProperty", None)
        self.__esmodel_accesscontrol_OrgUnitProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectId601"):
                opp_val = getattr(old_value, "ProjectId601", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId601", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId601"):
                opp_val = getattr(value, "ProjectId601", None)
                setattr(value, "ProjectId601", self)

class accesscontrol_ACOrgUnit:

    pass
class accesscontrol_OrgUnitProperty:

    pass
class ACOrgUnit:

    pass
class esmodel_accesscontrol_ACGroup(ACOrgUnit):

    pass
class esmodel_accesscontrol_ACUser(ACOrgUnit):

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

class ServerProjectEvent:

    pass
class esmodel_server_ProjectUpdatedEvent(ServerProjectEvent):

    pass
class ServerEvent:

    pass
class esmodel_server_ServerProjectEvent(ServerEvent):

    pass
class operations_OperationId:

    pass
class ReadEvent:

    pass
class esmodel_events_NotificationReadEvent(ReadEvent):

    def __init__(self, notificationId: str):
        self.notificationId = notificationId
        
    @property
    def notificationId(self) -> str:
        return self.__notificationId

    @notificationId.setter
    def notificationId(self, notificationId: str):
        self.__notificationId = notificationId

class esmodel_events_Event:

    def __init__(self, timestamp: date):
        self.timestamp = timestamp
        
    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

class Event:

    pass
class esmodel_events_ExceptionEvent(Event):

    def __init__(self, ExceptionTitle: str, ExceptionStackTrace: str, ExceptionCauseTitle: str, ExceptionCauseStackTrace: str):
        self.ExceptionTitle = ExceptionTitle
        self.ExceptionStackTrace = ExceptionStackTrace
        self.ExceptionCauseTitle = ExceptionCauseTitle
        self.ExceptionCauseStackTrace = ExceptionCauseStackTrace
        
    @property
    def ExceptionTitle(self) -> str:
        return self.__ExceptionTitle

    @ExceptionTitle.setter
    def ExceptionTitle(self, ExceptionTitle: str):
        self.__ExceptionTitle = ExceptionTitle

    @property
    def ExceptionCauseStackTrace(self) -> str:
        return self.__ExceptionCauseStackTrace

    @ExceptionCauseStackTrace.setter
    def ExceptionCauseStackTrace(self, ExceptionCauseStackTrace: str):
        self.__ExceptionCauseStackTrace = ExceptionCauseStackTrace

    @property
    def ExceptionCauseTitle(self) -> str:
        return self.__ExceptionCauseTitle

    @ExceptionCauseTitle.setter
    def ExceptionCauseTitle(self, ExceptionCauseTitle: str):
        self.__ExceptionCauseTitle = ExceptionCauseTitle

    @property
    def ExceptionStackTrace(self) -> str:
        return self.__ExceptionStackTrace

    @ExceptionStackTrace.setter
    def ExceptionStackTrace(self, ExceptionStackTrace: str):
        self.__ExceptionStackTrace = ExceptionStackTrace

class esmodel_events_Validate(Event):

    pass
class esmodel_events_UndoEvent(Event):

    pass
class esmodel_events_PerspectiveEvent(Event):

    pass
class esmodel_events_PresentationSwitchEvent(Event):

    def __init__(self, readView: str, newPresentation: str):
        self.readView = readView
        self.newPresentation = newPresentation
        
    @property
    def newPresentation(self) -> str:
        return self.__newPresentation

    @newPresentation.setter
    def newPresentation(self, newPresentation: str):
        self.__newPresentation = newPresentation

    @property
    def readView(self) -> str:
        return self.__readView

    @readView.setter
    def readView(self, readView: str):
        self.__readView = readView

class esmodel_events_MergeEvent(Event):

    def __init__(self, numberOfConflicts: int, totalTime: int, esmodel_events_MergeEvent: "versioning_PrimaryVersionSpec" = None, esmodel_events_MergeEvent526: "versioning_PrimaryVersionSpec" = None, esmodel_events_MergeEvent529: set["operations_AbstractOperation"] = None):
        self.numberOfConflicts = numberOfConflicts
        self.totalTime = totalTime
        self.esmodel_events_MergeEvent = esmodel_events_MergeEvent
        self.esmodel_events_MergeEvent526 = esmodel_events_MergeEvent526
        self.esmodel_events_MergeEvent529 = esmodel_events_MergeEvent529 if esmodel_events_MergeEvent529 is not None else set()
        
    @property
    def totalTime(self) -> int:
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: int):
        self.__totalTime = totalTime

    @property
    def numberOfConflicts(self) -> int:
        return self.__numberOfConflicts

    @numberOfConflicts.setter
    def numberOfConflicts(self, numberOfConflicts: int):
        self.__numberOfConflicts = numberOfConflicts

    @property
    def esmodel_events_MergeEvent(self):
        return self.__esmodel_events_MergeEvent

    @esmodel_events_MergeEvent.setter
    def esmodel_events_MergeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeEvent__esmodel_events_MergeEvent", None)
        self.__esmodel_events_MergeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec524"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec524", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec524", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec524"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec524", None)
                setattr(value, "versioning_PrimaryVersionSpec524", self)

    @property
    def esmodel_events_MergeEvent529(self):
        return self.__esmodel_events_MergeEvent529

    @esmodel_events_MergeEvent529.setter
    def esmodel_events_MergeEvent529(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeEvent__esmodel_events_MergeEvent529", None)
        self.__esmodel_events_MergeEvent529 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_AbstractOperation530"):
                    opp_val = getattr(item, "operations_AbstractOperation530", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation530", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation530"):
                    opp_val = getattr(item, "operations_AbstractOperation530", None)
                    
                    setattr(item, "operations_AbstractOperation530", self)
                    

    @property
    def esmodel_events_MergeEvent526(self):
        return self.__esmodel_events_MergeEvent526

    @esmodel_events_MergeEvent526.setter
    def esmodel_events_MergeEvent526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeEvent__esmodel_events_MergeEvent526", None)
        self.__esmodel_events_MergeEvent526 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec527"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec527", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec527"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec527", None)
                setattr(value, "versioning_PrimaryVersionSpec527", self)

class esmodel_events_ShowHistoryEvent(Event):

    pass
class esmodel_events_LinkEvent(Event):

    def __init__(self, sourceView: str, createdNew: bool, esmodel_events_LinkEvent: "ModelElementId" = None, esmodel_events_LinkEvent559: "ModelElementId" = None):
        self.sourceView = sourceView
        self.createdNew = createdNew
        self.esmodel_events_LinkEvent = esmodel_events_LinkEvent
        self.esmodel_events_LinkEvent559 = esmodel_events_LinkEvent559
        
    @property
    def sourceView(self) -> str:
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView

    @property
    def createdNew(self) -> bool:
        return self.__createdNew

    @createdNew.setter
    def createdNew(self, createdNew: bool):
        self.__createdNew = createdNew

    @property
    def esmodel_events_LinkEvent(self):
        return self.__esmodel_events_LinkEvent

    @esmodel_events_LinkEvent.setter
    def esmodel_events_LinkEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_LinkEvent__esmodel_events_LinkEvent", None)
        self.__esmodel_events_LinkEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId557"):
                opp_val = getattr(old_value, "ModelElementId557", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId557", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId557"):
                opp_val = getattr(value, "ModelElementId557", None)
                setattr(value, "ModelElementId557", self)

    @property
    def esmodel_events_LinkEvent559(self):
        return self.__esmodel_events_LinkEvent559

    @esmodel_events_LinkEvent559.setter
    def esmodel_events_LinkEvent559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_LinkEvent__esmodel_events_LinkEvent559", None)
        self.__esmodel_events_LinkEvent559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId560"):
                opp_val = getattr(old_value, "ModelElementId560", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId560", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId560"):
                opp_val = getattr(value, "ModelElementId560", None)
                setattr(value, "ModelElementId560", self)

class esmodel_events_AnnotationEvent(Event):

    pass
class esmodel_events_DNDEvent(Event):

    def __init__(self, sourceView: str, targetView: str, esmodel_events_DNDEvent: "ModelElementId" = None, esmodel_events_DNDEvent554: "ModelElementId" = None):
        self.sourceView = sourceView
        self.targetView = targetView
        self.esmodel_events_DNDEvent = esmodel_events_DNDEvent
        self.esmodel_events_DNDEvent554 = esmodel_events_DNDEvent554
        
    @property
    def sourceView(self) -> str:
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView

    @property
    def targetView(self) -> str:
        return self.__targetView

    @targetView.setter
    def targetView(self, targetView: str):
        self.__targetView = targetView

    @property
    def esmodel_events_DNDEvent(self):
        return self.__esmodel_events_DNDEvent

    @esmodel_events_DNDEvent.setter
    def esmodel_events_DNDEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_DNDEvent__esmodel_events_DNDEvent", None)
        self.__esmodel_events_DNDEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId552"):
                opp_val = getattr(old_value, "ModelElementId552", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId552", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId552"):
                opp_val = getattr(value, "ModelElementId552", None)
                setattr(value, "ModelElementId552", self)

    @property
    def esmodel_events_DNDEvent554(self):
        return self.__esmodel_events_DNDEvent554

    @esmodel_events_DNDEvent554.setter
    def esmodel_events_DNDEvent554(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_DNDEvent__esmodel_events_DNDEvent554", None)
        self.__esmodel_events_DNDEvent554 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId555"):
                opp_val = getattr(old_value, "ModelElementId555", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId555", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId555"):
                opp_val = getattr(value, "ModelElementId555", None)
                setattr(value, "ModelElementId555", self)

class esmodel_events_URLEvent(Event):

    def __init__(self, sourceView: str, esmodel_events_URLEvent: "ModelElementId" = None, esmodel_events_URLEvent583: "ModelElementId" = None):
        self.sourceView = sourceView
        self.esmodel_events_URLEvent = esmodel_events_URLEvent
        self.esmodel_events_URLEvent583 = esmodel_events_URLEvent583
        
    @property
    def sourceView(self) -> str:
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView

    @property
    def esmodel_events_URLEvent(self):
        return self.__esmodel_events_URLEvent

    @esmodel_events_URLEvent.setter
    def esmodel_events_URLEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_URLEvent__esmodel_events_URLEvent", None)
        self.__esmodel_events_URLEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId581"):
                opp_val = getattr(old_value, "ModelElementId581", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId581"):
                opp_val = getattr(value, "ModelElementId581", None)
                setattr(value, "ModelElementId581", self)

    @property
    def esmodel_events_URLEvent583(self):
        return self.__esmodel_events_URLEvent583

    @esmodel_events_URLEvent583.setter
    def esmodel_events_URLEvent583(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_URLEvent__esmodel_events_URLEvent583", None)
        self.__esmodel_events_URLEvent583 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId584"):
                opp_val = getattr(old_value, "ModelElementId584", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId584"):
                opp_val = getattr(value, "ModelElementId584", None)
                setattr(value, "ModelElementId584", self)

class esmodel_events_UpdateEvent(Event):

    pass
class esmodel_events_ShowChangesEvent(Event):

    pass
class esmodel_server_ServerEvent(Event):

    pass
class esmodel_events_MergeChoiceEvent(Event):

    def __init__(self, selection: str, contextFeature: str, createdIssueName: str, esmodel_events_MergeChoiceEvent: set["operations_OperationId"] = None, esmodel_events_MergeChoiceEvent587: set["operations_OperationId"] = None, esmodel_events_MergeChoiceEvent590: "ModelElementId" = None):
        self.selection = selection
        self.contextFeature = contextFeature
        self.createdIssueName = createdIssueName
        self.esmodel_events_MergeChoiceEvent = esmodel_events_MergeChoiceEvent if esmodel_events_MergeChoiceEvent is not None else set()
        self.esmodel_events_MergeChoiceEvent587 = esmodel_events_MergeChoiceEvent587 if esmodel_events_MergeChoiceEvent587 is not None else set()
        self.esmodel_events_MergeChoiceEvent590 = esmodel_events_MergeChoiceEvent590
        
    @property
    def createdIssueName(self) -> str:
        return self.__createdIssueName

    @createdIssueName.setter
    def createdIssueName(self, createdIssueName: str):
        self.__createdIssueName = createdIssueName

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def contextFeature(self) -> str:
        return self.__contextFeature

    @contextFeature.setter
    def contextFeature(self, contextFeature: str):
        self.__contextFeature = contextFeature

    @property
    def esmodel_events_MergeChoiceEvent587(self):
        return self.__esmodel_events_MergeChoiceEvent587

    @esmodel_events_MergeChoiceEvent587.setter
    def esmodel_events_MergeChoiceEvent587(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeChoiceEvent__esmodel_events_MergeChoiceEvent587", None)
        self.__esmodel_events_MergeChoiceEvent587 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_OperationId588"):
                    opp_val = getattr(item, "operations_OperationId588", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_OperationId588", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_OperationId588"):
                    opp_val = getattr(item, "operations_OperationId588", None)
                    
                    setattr(item, "operations_OperationId588", self)
                    

    @property
    def esmodel_events_MergeChoiceEvent590(self):
        return self.__esmodel_events_MergeChoiceEvent590

    @esmodel_events_MergeChoiceEvent590.setter
    def esmodel_events_MergeChoiceEvent590(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeChoiceEvent__esmodel_events_MergeChoiceEvent590", None)
        self.__esmodel_events_MergeChoiceEvent590 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId591"):
                opp_val = getattr(old_value, "ModelElementId591", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId591", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId591"):
                opp_val = getattr(value, "ModelElementId591", None)
                setattr(value, "ModelElementId591", self)

    @property
    def esmodel_events_MergeChoiceEvent(self):
        return self.__esmodel_events_MergeChoiceEvent

    @esmodel_events_MergeChoiceEvent.setter
    def esmodel_events_MergeChoiceEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeChoiceEvent__esmodel_events_MergeChoiceEvent", None)
        self.__esmodel_events_MergeChoiceEvent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_OperationId"):
                    opp_val = getattr(item, "operations_OperationId", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_OperationId", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_OperationId"):
                    opp_val = getattr(item, "operations_OperationId", None)
                    
                    setattr(item, "operations_OperationId", self)
                    

class esmodel_events_PluginStartEvent(Event):

    def __init__(self, pluginId: str):
        self.pluginId = pluginId
        
    @property
    def pluginId(self) -> str:
        return self.__pluginId

    @pluginId.setter
    def pluginId(self, pluginId: str):
        self.__pluginId = pluginId

class esmodel_events_NavigatorCreateEvent(Event):

    def __init__(self, dynamic: bool, esmodel_events_NavigatorCreateEvent: "ModelElementId" = None, esmodel_events_NavigatorCreateEvent569: "ModelElementId" = None):
        self.dynamic = dynamic
        self.esmodel_events_NavigatorCreateEvent = esmodel_events_NavigatorCreateEvent
        self.esmodel_events_NavigatorCreateEvent569 = esmodel_events_NavigatorCreateEvent569
        
    @property
    def dynamic(self) -> bool:
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: bool):
        self.__dynamic = dynamic

    @property
    def esmodel_events_NavigatorCreateEvent569(self):
        return self.__esmodel_events_NavigatorCreateEvent569

    @esmodel_events_NavigatorCreateEvent569.setter
    def esmodel_events_NavigatorCreateEvent569(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_NavigatorCreateEvent__esmodel_events_NavigatorCreateEvent569", None)
        self.__esmodel_events_NavigatorCreateEvent569 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId570"):
                opp_val = getattr(old_value, "ModelElementId570", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId570", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId570"):
                opp_val = getattr(value, "ModelElementId570", None)
                setattr(value, "ModelElementId570", self)

    @property
    def esmodel_events_NavigatorCreateEvent(self):
        return self.__esmodel_events_NavigatorCreateEvent

    @esmodel_events_NavigatorCreateEvent.setter
    def esmodel_events_NavigatorCreateEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_NavigatorCreateEvent__esmodel_events_NavigatorCreateEvent", None)
        self.__esmodel_events_NavigatorCreateEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId567"):
                opp_val = getattr(old_value, "ModelElementId567", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId567", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId567"):
                opp_val = getattr(value, "ModelElementId567", None)
                setattr(value, "ModelElementId567", self)

class esmodel_events_MergeGlobalChoiceEvent(Event):

    def __init__(self, selection: str):
        self.selection = selection
        
    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

class esmodel_events_CheckoutEvent(Event):

    pass
class esmodel_events_RevertEvent(Event):

    def __init__(self, revertedChangesCount: int):
        self.revertedChangesCount = revertedChangesCount
        
    @property
    def revertedChangesCount(self) -> int:
        return self.__revertedChangesCount

    @revertedChangesCount.setter
    def revertedChangesCount(self, revertedChangesCount: int):
        self.__revertedChangesCount = revertedChangesCount

class esmodel_events_NotificationIgnoreEvent(Event):

    def __init__(self, notificationId: str):
        self.notificationId = notificationId
        
    @property
    def notificationId(self) -> str:
        return self.__notificationId

    @notificationId.setter
    def notificationId(self, notificationId: str):
        self.__notificationId = notificationId

class esmodel_events_PluginFocusEvent(Event):

    def __init__(self, pluginId: str, startDate: date):
        self.pluginId = pluginId
        self.startDate = startDate
        
    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def pluginId(self) -> str:
        return self.__pluginId

    @pluginId.setter
    def pluginId(self, pluginId: str):
        self.__pluginId = pluginId

class esmodel_events_TraceEvent(Event):

    def __init__(self, featureName: str, esmodel_events_TraceEvent: "ModelElementId" = None, esmodel_events_TraceEvent564: "ModelElementId" = None):
        self.featureName = featureName
        self.esmodel_events_TraceEvent = esmodel_events_TraceEvent
        self.esmodel_events_TraceEvent564 = esmodel_events_TraceEvent564
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def esmodel_events_TraceEvent(self):
        return self.__esmodel_events_TraceEvent

    @esmodel_events_TraceEvent.setter
    def esmodel_events_TraceEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_TraceEvent__esmodel_events_TraceEvent", None)
        self.__esmodel_events_TraceEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId562"):
                opp_val = getattr(old_value, "ModelElementId562", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId562", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId562"):
                opp_val = getattr(value, "ModelElementId562", None)
                setattr(value, "ModelElementId562", self)

    @property
    def esmodel_events_TraceEvent564(self):
        return self.__esmodel_events_TraceEvent564

    @esmodel_events_TraceEvent564.setter
    def esmodel_events_TraceEvent564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_TraceEvent__esmodel_events_TraceEvent564", None)
        self.__esmodel_events_TraceEvent564 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId565"):
                opp_val = getattr(old_value, "ModelElementId565", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId565", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId565"):
                opp_val = getattr(value, "ModelElementId565", None)
                setattr(value, "ModelElementId565", self)

class esmodel_events_NotificationGenerationEvent(Event):

    pass
class esmodel_events_ReadEvent(Event):

    def __init__(self, sourceView: str, readView: str, esmodel_events_ReadEvent: "ModelElementId" = None):
        self.sourceView = sourceView
        self.readView = readView
        self.esmodel_events_ReadEvent = esmodel_events_ReadEvent
        
    @property
    def readView(self) -> str:
        return self.__readView

    @readView.setter
    def readView(self, readView: str):
        self.__readView = readView

    @property
    def sourceView(self) -> str:
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView

    @property
    def esmodel_events_ReadEvent(self):
        return self.__esmodel_events_ReadEvent

    @esmodel_events_ReadEvent.setter
    def esmodel_events_ReadEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_ReadEvent__esmodel_events_ReadEvent", None)
        self.__esmodel_events_ReadEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId522"):
                opp_val = getattr(old_value, "ModelElementId522", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId522", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId522"):
                opp_val = getattr(value, "ModelElementId522", None)
                setattr(value, "ModelElementId522", self)

class CompositeOperation:

    pass
class esmodel_semantic_SemanticCompositeOperation(CompositeOperation):

    pass
class esmodel_operations_EObjectToModelElementIdMap:

    pass
class esmodel_operations_ModelElementGroup:

    def __init__(self, name: str, esmodel_operations_ModelElementGroup: set["ModelElementId"] = None):
        self.name = name
        self.esmodel_operations_ModelElementGroup = esmodel_operations_ModelElementGroup if esmodel_operations_ModelElementGroup is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_operations_ModelElementGroup(self):
        return self.__esmodel_operations_ModelElementGroup

    @esmodel_operations_ModelElementGroup.setter
    def esmodel_operations_ModelElementGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_ModelElementGroup__esmodel_operations_ModelElementGroup", None)
        self.__esmodel_operations_ModelElementGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId515"):
                    opp_val = getattr(item, "ModelElementId515", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId515", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId515"):
                    opp_val = getattr(item, "ModelElementId515", None)
                    
                    setattr(item, "ModelElementId515", self)
                    

class esmodel_operations_OperationGroup:

    def __init__(self, name: str, esmodel_operations_OperationGroup: set["operations_AbstractOperation"] = None):
        self.name = name
        self.esmodel_operations_OperationGroup = esmodel_operations_OperationGroup if esmodel_operations_OperationGroup is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_operations_OperationGroup(self):
        return self.__esmodel_operations_OperationGroup

    @esmodel_operations_OperationGroup.setter
    def esmodel_operations_OperationGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_OperationGroup__esmodel_operations_OperationGroup", None)
        self.__esmodel_operations_OperationGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_AbstractOperation513"):
                    opp_val = getattr(item, "operations_AbstractOperation513", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation513", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation513"):
                    opp_val = getattr(item, "operations_AbstractOperation513", None)
                    
                    setattr(item, "operations_AbstractOperation513", self)
                    

class AttributeOperation:

    pass
class esmodel_operations_DiagramLayoutOperation(AttributeOperation):

    pass
class ReferenceOperation:

    pass
class esmodel_operations_SingleReferenceOperation(ReferenceOperation):

    pass
class esmodel_operations_MultiReferenceOperation(ReferenceOperation):

    def __init__(self, add: bool, index: int, esmodel_operations_MultiReferenceOperation: set["ModelElementId"] = None):
        self.add = add
        self.index = index
        self.esmodel_operations_MultiReferenceOperation = esmodel_operations_MultiReferenceOperation if esmodel_operations_MultiReferenceOperation is not None else set()
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def add(self) -> bool:
        return self.__add

    @add.setter
    def add(self, add: bool):
        self.__add = add

    @property
    def esmodel_operations_MultiReferenceOperation(self):
        return self.__esmodel_operations_MultiReferenceOperation

    @esmodel_operations_MultiReferenceOperation.setter
    def esmodel_operations_MultiReferenceOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_MultiReferenceOperation__esmodel_operations_MultiReferenceOperation", None)
        self.__esmodel_operations_MultiReferenceOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId509"):
                    opp_val = getattr(item, "ModelElementId509", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId509", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId509"):
                    opp_val = getattr(item, "ModelElementId509", None)
                    
                    setattr(item, "ModelElementId509", self)
                    

class esmodel_operations_MultiReferenceSetOperation(ReferenceOperation):

    def __init__(self, index: int, esmodel_operations_MultiReferenceSetOperation: "ModelElementId" = None, esmodel_operations_MultiReferenceSetOperation506: "ModelElementId" = None):
        self.index = index
        self.esmodel_operations_MultiReferenceSetOperation = esmodel_operations_MultiReferenceSetOperation
        self.esmodel_operations_MultiReferenceSetOperation506 = esmodel_operations_MultiReferenceSetOperation506
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def esmodel_operations_MultiReferenceSetOperation(self):
        return self.__esmodel_operations_MultiReferenceSetOperation

    @esmodel_operations_MultiReferenceSetOperation.setter
    def esmodel_operations_MultiReferenceSetOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_MultiReferenceSetOperation__esmodel_operations_MultiReferenceSetOperation", None)
        self.__esmodel_operations_MultiReferenceSetOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId504"):
                opp_val = getattr(old_value, "ModelElementId504", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId504", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId504"):
                opp_val = getattr(value, "ModelElementId504", None)
                setattr(value, "ModelElementId504", self)

    @property
    def esmodel_operations_MultiReferenceSetOperation506(self):
        return self.__esmodel_operations_MultiReferenceSetOperation506

    @esmodel_operations_MultiReferenceSetOperation506.setter
    def esmodel_operations_MultiReferenceSetOperation506(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_MultiReferenceSetOperation__esmodel_operations_MultiReferenceSetOperation506", None)
        self.__esmodel_operations_MultiReferenceSetOperation506 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId507"):
                opp_val = getattr(old_value, "ModelElementId507", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId507", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId507"):
                opp_val = getattr(value, "ModelElementId507", None)
                setattr(value, "ModelElementId507", self)

class FeatureOperation:

    pass
class esmodel_operations_MultiReferenceMoveOperation(FeatureOperation):

    def __init__(self, oldIndex: int, newIndex: int, esmodel_operations_MultiReferenceMoveOperation: "ModelElementId" = None):
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.esmodel_operations_MultiReferenceMoveOperation = esmodel_operations_MultiReferenceMoveOperation
        
    @property
    def newIndex(self) -> int:
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex

    @property
    def oldIndex(self) -> int:
        return self.__oldIndex

    @oldIndex.setter
    def oldIndex(self, oldIndex: int):
        self.__oldIndex = oldIndex

    @property
    def esmodel_operations_MultiReferenceMoveOperation(self):
        return self.__esmodel_operations_MultiReferenceMoveOperation

    @esmodel_operations_MultiReferenceMoveOperation.setter
    def esmodel_operations_MultiReferenceMoveOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_MultiReferenceMoveOperation__esmodel_operations_MultiReferenceMoveOperation", None)
        self.__esmodel_operations_MultiReferenceMoveOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId511"):
                opp_val = getattr(old_value, "ModelElementId511", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId511", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId511"):
                opp_val = getattr(value, "ModelElementId511", None)
                setattr(value, "ModelElementId511", self)

class esmodel_operations_MultiAttributeMoveOperation(FeatureOperation):

    def __init__(self, oldIndex: int, newIndex: int, referencedValue: str):
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.referencedValue = referencedValue
        
    @property
    def referencedValue(self) -> str:
        return self.__referencedValue

    @referencedValue.setter
    def referencedValue(self, referencedValue: str):
        self.__referencedValue = referencedValue

    @property
    def newIndex(self) -> int:
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex

    @property
    def oldIndex(self) -> int:
        return self.__oldIndex

    @oldIndex.setter
    def oldIndex(self, oldIndex: int):
        self.__oldIndex = oldIndex

class esmodel_operations_MultiAttributeOperation(FeatureOperation):

    def __init__(self, add: bool, indexes: int, referencedValues: str):
        self.add = add
        self.indexes = indexes
        self.referencedValues = referencedValues
        
    @property
    def indexes(self) -> int:
        return self.__indexes

    @indexes.setter
    def indexes(self, indexes: int):
        self.__indexes = indexes

    @property
    def add(self) -> bool:
        return self.__add

    @add.setter
    def add(self, add: bool):
        self.__add = add

    @property
    def referencedValues(self) -> str:
        return self.__referencedValues

    @referencedValues.setter
    def referencedValues(self, referencedValues: str):
        self.__referencedValues = referencedValues

class esmodel_operations_ReferenceOperation(FeatureOperation):

    def __init__(self, containmentType: str, bidirectional: bool, oppositeFeatureName: str):
        self.containmentType = containmentType
        self.bidirectional = bidirectional
        self.oppositeFeatureName = oppositeFeatureName
        
    @property
    def oppositeFeatureName(self) -> str:
        return self.__oppositeFeatureName

    @oppositeFeatureName.setter
    def oppositeFeatureName(self, oppositeFeatureName: str):
        self.__oppositeFeatureName = oppositeFeatureName

    @property
    def bidirectional(self) -> bool:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: bool):
        self.__bidirectional = bidirectional

    @property
    def containmentType(self) -> str:
        return self.__containmentType

    @containmentType.setter
    def containmentType(self, containmentType: str):
        self.__containmentType = containmentType

class esmodel_operations_MultiAttributeSetOperation(FeatureOperation):

    def __init__(self, index: int, oldValue: str, newValue: str):
        self.index = index
        self.oldValue = oldValue
        self.newValue = newValue
        
    @property
    def newValue(self) -> str:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def oldValue(self) -> str:
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

class esmodel_operations_AttributeOperation(FeatureOperation):

    def __init__(self, oldValue: str, newValue: str):
        self.oldValue = oldValue
        self.newValue = newValue
        
    @property
    def oldValue(self) -> str:
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue

    @property
    def newValue(self) -> str:
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue

class operations_EObjectToModelElementIdMap:

    pass
class operations_ReferenceOperation:

    pass
class operations_esmodel_EObject:

    pass
class AbstractOperation:

    pass
class esmodel_operations_FeatureOperation(AbstractOperation):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class esmodel_operations_CreateDeleteOperation(AbstractOperation):

    def __init__(self, delete: bool, esmodel_operations_CreateDeleteOperation: "operations_esmodel_EObject" = None, esmodel_operations_CreateDeleteOperation495: set["operations_ReferenceOperation"] = None, esmodel_operations_CreateDeleteOperation497: set["operations_EObjectToModelElementIdMap"] = None):
        self.delete = delete
        self.esmodel_operations_CreateDeleteOperation = esmodel_operations_CreateDeleteOperation
        self.esmodel_operations_CreateDeleteOperation495 = esmodel_operations_CreateDeleteOperation495 if esmodel_operations_CreateDeleteOperation495 is not None else set()
        self.esmodel_operations_CreateDeleteOperation497 = esmodel_operations_CreateDeleteOperation497 if esmodel_operations_CreateDeleteOperation497 is not None else set()
        
    @property
    def delete(self) -> bool:
        return self.__delete

    @delete.setter
    def delete(self, delete: bool):
        self.__delete = delete

    @property
    def esmodel_operations_CreateDeleteOperation497(self):
        return self.__esmodel_operations_CreateDeleteOperation497

    @esmodel_operations_CreateDeleteOperation497.setter
    def esmodel_operations_CreateDeleteOperation497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CreateDeleteOperation__esmodel_operations_CreateDeleteOperation497", None)
        self.__esmodel_operations_CreateDeleteOperation497 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_EObjectToModelElementIdMap"):
                    opp_val = getattr(item, "operations_EObjectToModelElementIdMap", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_EObjectToModelElementIdMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_EObjectToModelElementIdMap"):
                    opp_val = getattr(item, "operations_EObjectToModelElementIdMap", None)
                    
                    setattr(item, "operations_EObjectToModelElementIdMap", self)
                    

    @property
    def esmodel_operations_CreateDeleteOperation(self):
        return self.__esmodel_operations_CreateDeleteOperation

    @esmodel_operations_CreateDeleteOperation.setter
    def esmodel_operations_CreateDeleteOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CreateDeleteOperation__esmodel_operations_CreateDeleteOperation", None)
        self.__esmodel_operations_CreateDeleteOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations_esmodel_EObject"):
                opp_val = getattr(old_value, "operations_esmodel_EObject", None)
                if opp_val == self:
                    setattr(old_value, "operations_esmodel_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations_esmodel_EObject"):
                opp_val = getattr(value, "operations_esmodel_EObject", None)
                setattr(value, "operations_esmodel_EObject", self)

    @property
    def esmodel_operations_CreateDeleteOperation495(self):
        return self.__esmodel_operations_CreateDeleteOperation495

    @esmodel_operations_CreateDeleteOperation495.setter
    def esmodel_operations_CreateDeleteOperation495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CreateDeleteOperation__esmodel_operations_CreateDeleteOperation495", None)
        self.__esmodel_operations_CreateDeleteOperation495 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_ReferenceOperation"):
                    opp_val = getattr(item, "operations_ReferenceOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_ReferenceOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_ReferenceOperation"):
                    opp_val = getattr(item, "operations_ReferenceOperation", None)
                    
                    setattr(item, "operations_ReferenceOperation", self)
                    

class esmodel_operations_CompositeOperation(AbstractOperation):

    def __init__(self, compositeName: str, compositeDescription: str, reversed: bool, esmodel_operations_CompositeOperation: set["operations_AbstractOperation"] = None, esmodel_operations_CompositeOperation491: "operations_AbstractOperation" = None):
        self.compositeName = compositeName
        self.compositeDescription = compositeDescription
        self.reversed = reversed
        self.esmodel_operations_CompositeOperation = esmodel_operations_CompositeOperation if esmodel_operations_CompositeOperation is not None else set()
        self.esmodel_operations_CompositeOperation491 = esmodel_operations_CompositeOperation491
        
    @property
    def compositeDescription(self) -> str:
        return self.__compositeDescription

    @compositeDescription.setter
    def compositeDescription(self, compositeDescription: str):
        self.__compositeDescription = compositeDescription

    @property
    def reversed(self) -> bool:
        return self.__reversed

    @reversed.setter
    def reversed(self, reversed: bool):
        self.__reversed = reversed

    @property
    def compositeName(self) -> str:
        return self.__compositeName

    @compositeName.setter
    def compositeName(self, compositeName: str):
        self.__compositeName = compositeName

    @property
    def esmodel_operations_CompositeOperation491(self):
        return self.__esmodel_operations_CompositeOperation491

    @esmodel_operations_CompositeOperation491.setter
    def esmodel_operations_CompositeOperation491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CompositeOperation__esmodel_operations_CompositeOperation491", None)
        self.__esmodel_operations_CompositeOperation491 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations_AbstractOperation492"):
                opp_val = getattr(old_value, "operations_AbstractOperation492", None)
                if opp_val == self:
                    setattr(old_value, "operations_AbstractOperation492", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations_AbstractOperation492"):
                opp_val = getattr(value, "operations_AbstractOperation492", None)
                setattr(value, "operations_AbstractOperation492", self)

    @property
    def esmodel_operations_CompositeOperation(self):
        return self.__esmodel_operations_CompositeOperation

    @esmodel_operations_CompositeOperation.setter
    def esmodel_operations_CompositeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CompositeOperation__esmodel_operations_CompositeOperation", None)
        self.__esmodel_operations_CompositeOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_AbstractOperation489"):
                    opp_val = getattr(item, "operations_AbstractOperation489", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation489"):
                    opp_val = getattr(item, "operations_AbstractOperation489", None)
                    
                    setattr(item, "operations_AbstractOperation489", self)
                    

class esmodel_versioning_VersionProperty:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class versioning_ChangePackage:

    pass
class esmodel_versioning_Version:

    pass
class esmodel_versioning_HistoryQuery:

    def __init__(self, includeChangePackage: bool, esmodel_versioning_HistoryQuery: "versioning_PrimaryVersionSpec" = None, esmodel_versioning_HistoryQuery463: "versioning_PrimaryVersionSpec" = None, esmodel_versioning_HistoryQuery466: set["ModelElementId"] = None):
        self.includeChangePackage = includeChangePackage
        self.esmodel_versioning_HistoryQuery = esmodel_versioning_HistoryQuery
        self.esmodel_versioning_HistoryQuery463 = esmodel_versioning_HistoryQuery463
        self.esmodel_versioning_HistoryQuery466 = esmodel_versioning_HistoryQuery466 if esmodel_versioning_HistoryQuery466 is not None else set()
        
    @property
    def includeChangePackage(self) -> bool:
        return self.__includeChangePackage

    @includeChangePackage.setter
    def includeChangePackage(self, includeChangePackage: bool):
        self.__includeChangePackage = includeChangePackage

    @property
    def esmodel_versioning_HistoryQuery466(self):
        return self.__esmodel_versioning_HistoryQuery466

    @esmodel_versioning_HistoryQuery466.setter
    def esmodel_versioning_HistoryQuery466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_versioning_HistoryQuery__esmodel_versioning_HistoryQuery466", None)
        self.__esmodel_versioning_HistoryQuery466 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId467"):
                    opp_val = getattr(item, "ModelElementId467", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId467", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId467"):
                    opp_val = getattr(item, "ModelElementId467", None)
                    
                    setattr(item, "ModelElementId467", self)
                    

    @property
    def esmodel_versioning_HistoryQuery463(self):
        return self.__esmodel_versioning_HistoryQuery463

    @esmodel_versioning_HistoryQuery463.setter
    def esmodel_versioning_HistoryQuery463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_versioning_HistoryQuery__esmodel_versioning_HistoryQuery463", None)
        self.__esmodel_versioning_HistoryQuery463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec464"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec464", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec464"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec464", None)
                setattr(value, "versioning_PrimaryVersionSpec464", self)

    @property
    def esmodel_versioning_HistoryQuery(self):
        return self.__esmodel_versioning_HistoryQuery

    @esmodel_versioning_HistoryQuery.setter
    def esmodel_versioning_HistoryQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_versioning_HistoryQuery__esmodel_versioning_HistoryQuery", None)
        self.__esmodel_versioning_HistoryQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec461"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec461", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec461", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec461"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec461", None)
                setattr(value, "versioning_PrimaryVersionSpec461", self)

class esmodel_versioning_LogMessage:

    def __init__(self, message: str, date: date, clientDate: date, author: str):
        self.message = message
        self.date = date
        self.clientDate = clientDate
        self.author = author
        
    @property
    def clientDate(self) -> date:
        return self.__clientDate

    @clientDate.setter
    def clientDate(self, clientDate: date):
        self.__clientDate = clientDate

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

class versioning_TagVersionSpec:

    pass
class esmodel_versioning_HistoryInfo:

    pass
class versioning_VersionProperty:

    pass
class notification_ESNotification:

    pass
class versioning_LogMessage:

    pass
class events_Event:

    pass
class operations_AbstractOperation:

    pass
class esmodel_versioning_ChangePackage:

    pass
class esmodel_ServerSpace:

    pass
class esmodel_versioning_VersionSpec(ABC):

    pass
class VersionSpec:

    pass
class esmodel_versioning_PrimaryVersionSpec(VersionSpec):

    def __init__(self, identifier: int):
        self.identifier = identifier
        
    @property
    def identifier(self) -> int:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: int):
        self.__identifier = identifier

class esmodel_versioning_DateVersionSpec(VersionSpec):

    def __init__(self, date: date):
        self.date = date
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

class esmodel_versioning_HeadVersionSpec(VersionSpec):

    pass
class esmodel_versioning_TagVersionSpec(VersionSpec):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class esmodel_ClientVersionInfo:

    def __init__(self, version: str, name: str):
        self.version = version
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

class esmodel_VersionInfo:

    def __init__(self, emfStoreVersionString: str):
        self.emfStoreVersionString = emfStoreVersionString
        
    @property
    def emfStoreVersionString(self) -> str:
        return self.__emfStoreVersionString

    @emfStoreVersionString.setter
    def emfStoreVersionString(self, emfStoreVersionString: str):
        self.__emfStoreVersionString = emfStoreVersionString

class accesscontrol_ACUser:

    pass
class SessionId:

    pass
class ProjectHistory:

    pass
class accesscontrol_ACGroup:

    pass
class ActivityObject:

    pass
class model_activity_Activity(ActivityObject):

    pass
class versioning_PrimaryVersionSpec:

    pass
class esmodel_ProjectInfo:

    def __init__(self, name: str, description: str, esmodel_ProjectInfo: "ProjectId" = None, esmodel_ProjectInfo431: "versioning_PrimaryVersionSpec" = None):
        self.name = name
        self.description = description
        self.esmodel_ProjectInfo = esmodel_ProjectInfo
        self.esmodel_ProjectInfo431 = esmodel_ProjectInfo431
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_ProjectInfo431(self):
        return self.__esmodel_ProjectInfo431

    @esmodel_ProjectInfo431.setter
    def esmodel_ProjectInfo431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectInfo__esmodel_ProjectInfo431", None)
        self.__esmodel_ProjectInfo431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec", None)
                setattr(value, "versioning_PrimaryVersionSpec", self)

    @property
    def esmodel_ProjectInfo(self):
        return self.__esmodel_ProjectInfo

    @esmodel_ProjectInfo.setter
    def esmodel_ProjectInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectInfo__esmodel_ProjectInfo", None)
        self.__esmodel_ProjectInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectId429"):
                opp_val = getattr(old_value, "ProjectId429", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId429"):
                opp_val = getattr(value, "ProjectId429", None)
                setattr(value, "ProjectId429", self)

class versioning_Version:

    pass
class ProjectId:

    pass
class esmodel_ProjectHistory:

    def __init__(self, projectName: str, projectDescription: str, esmodel_ProjectHistory: "ProjectId" = None, esmodel_ProjectHistory427: set["versioning_Version"] = None):
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.esmodel_ProjectHistory = esmodel_ProjectHistory
        self.esmodel_ProjectHistory427 = esmodel_ProjectHistory427 if esmodel_ProjectHistory427 is not None else set()
        
    @property
    def projectDescription(self) -> str:
        return self.__projectDescription

    @projectDescription.setter
    def projectDescription(self, projectDescription: str):
        self.__projectDescription = projectDescription

    @property
    def projectName(self) -> str:
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName

    @property
    def esmodel_ProjectHistory(self):
        return self.__esmodel_ProjectHistory

    @esmodel_ProjectHistory.setter
    def esmodel_ProjectHistory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectHistory__esmodel_ProjectHistory", None)
        self.__esmodel_ProjectHistory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectId"):
                opp_val = getattr(old_value, "ProjectId", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId"):
                opp_val = getattr(value, "ProjectId", None)
                setattr(value, "ProjectId", self)

    @property
    def esmodel_ProjectHistory427(self):
        return self.__esmodel_ProjectHistory427

    @esmodel_ProjectHistory427.setter
    def esmodel_ProjectHistory427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectHistory__esmodel_ProjectHistory427", None)
        self.__esmodel_ProjectHistory427 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "versioning_Version"):
                    opp_val = getattr(item, "versioning_Version", None)
                    
                    if opp_val == self:
                        setattr(item, "versioning_Version", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "versioning_Version"):
                    opp_val = getattr(item, "versioning_Version", None)
                    
                    setattr(item, "versioning_Version", self)
                    

class model_activity_ActivityEnd(ActivityObject):

    pass
class model_activity_ActivityInitial(ActivityObject):

    pass
class model_activity_Branch(ActivityObject):

    pass
class model_activity_Fork(ActivityObject):

    pass
class StereotypeAttributeInstance:

    pass
class model_profile_StereotypeAttributeInstanceString(StereotypeAttributeInstance):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class activity_ActivityObject:

    pass
class activity_Transition:

    pass
class ModelElementId:

    pass
class model_util_ModelElementPath:

    pass
class StereotypeAttribute:

    pass
class model_profile_StereotypeAttributeSimple(StereotypeAttribute):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class profile_StereotypeAttributeInstance:

    pass
class profile_StereotypeAttribute:

    pass
class profile_Profile:

    pass
class profile_Stereotype:

    pass
class StateNode:

    pass
class model_state_StateInitial(StateNode):

    pass
class model_state_StateEnd(StateNode):

    pass
class model_state_State(StateNode):

    def __init__(self, exitConditions: str, activities: str, entryConditions: str):
        self.exitConditions = exitConditions
        self.activities = activities
        self.entryConditions = entryConditions
        
    @property
    def entryConditions(self) -> str:
        return self.__entryConditions

    @entryConditions.setter
    def entryConditions(self, entryConditions: str):
        self.__entryConditions = entryConditions

    @property
    def activities(self) -> str:
        return self.__activities

    @activities.setter
    def activities(self, activities: str):
        self.__activities = activities

    @property
    def exitConditions(self) -> str:
        return self.__exitConditions

    @exitConditions.setter
    def exitConditions(self, exitConditions: str):
        self.__exitConditions = exitConditions

class state_Transition:

    pass
class state_StateNode:

    pass
class MeetingSection:

    pass
class model_meeting_IssueMeetingSection(MeetingSection):

    pass
class model_meeting_WorkItemMeetingSection(MeetingSection):

    pass
class model_meeting_CompositeMeetingSection(MeetingSection):

    pass
class meeting_WorkItemMeetingSection:

    pass
class meeting_IssueMeetingSection:

    pass
class meeting_MeetingSection:

    pass
class change_MergingProposal:

    pass
class Proposal:

    pass
class model_change_MergingProposal(Proposal):

    pass
class component_Component:

    pass
class component_ComponentService:

    pass
class Solution:

    pass
class model_change_MergingSolution(Solution):

    pass
class Issue:

    pass
class model_change_MergingIssue(Issue):

    def __init__(self, resolvingRevision: int):
        self.resolvingRevision = resolvingRevision
        
    @property
    def resolvingRevision(self) -> int:
        return self.__resolvingRevision

    @resolvingRevision.setter
    def resolvingRevision(self, resolvingRevision: int):
        self.__resolvingRevision = resolvingRevision

class attachment_FileAttachment:

    pass
class model_rationale_AudioComment:

    pass
class rationale_Assessment:

    pass
class rationale_Issue:

    pass
class rationale_Criterion:

    pass
class rationale_Solution:

    pass
class rationale_Proposal:

    pass
class Criterion:

    pass
class model_requirement_NonFunctionalRequirement(Criterion):

    pass
class requirement_Workspace:

    pass
class NonDomainElement:

    pass
class requirement_UserTask:

    pass
class requirement_Step:

    pass
class requirement_ActorInstance:

    pass
class requirement_SystemFunction:

    pass
class requirement_NonFunctionalRequirement:

    pass
class requirement_Actor:

    pass
class requirement_FunctionalRequirement:

    pass
class document_Section:

    pass
class Section:

    pass
class model_document_CompositeSection(Section):

    pass
class model_document_LeafSection(Section):

    pass
class document_CompositeSection:

    pass
class classes_MethodArgument:

    pass
class classes_PackageElement:

    pass
class requirement_Scenario:

    pass
class requirement_UseCase:

    pass
class classes_Method:

    pass
class classes_Attribute:

    pass
class classes_Association:

    pass
class classes_Class:

    pass
class PackageElement:

    pass
class model_classes_Package(PackageElement):

    pass
class model_classes_Class(PackageElement):

    pass
class classes_Dependency:

    pass
class classes_Package:

    pass
class diagram_model_Diagram:

    pass
class task_Checkable:

    pass
class WorkItem:

    pass
class model_task_Milestone(WorkItem):

    pass
class model_task_WorkPackage(WorkItem):

    def __init__(self, startDate: date, endDate: date, 161: set["task_WorkItem"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.161 = 161 if 161 is not None else set()
        
    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def 161(self):
        return self.__161

    @161.setter
    def 161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkPackage__161", None)
        self.__161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#62"):
                    opp_val = getattr(item, "#62", None)
                    
                    if opp_val == self:
                        setattr(item, "#62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#62"):
                    opp_val = getattr(item, "#62", None)
                    
                    setattr(item, "#62", self)
                    

class change_ModelChangePackage:

    pass
class organization_User:

    pass
class OrgUnit:

    pass
class model_organization_User(OrgUnit):

    def __init__(self, firstName: str, lastName: str, email: str, 136: set["task_WorkItem"] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.136 = 136 if 136 is not None else set()
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def 136(self):
        return self.__136

    @136.setter
    def 136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_User__136", None)
        self.__136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#37"):
                    opp_val = getattr(item, "#37", None)
                    
                    if opp_val == self:
                        setattr(item, "#37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#37"):
                    opp_val = getattr(item, "#37", None)
                    
                    setattr(item, "#37", self)
                    

class task_WorkPackage:

    pass
class organization_OrgUnit:

    pass
class model_organization_Group(OrgUnit):

    pass
class task_WorkItem:

    pass
class model_task_ActionItem(task_Checkable, task_WorkItem):

    def __init__(self, done: bool, activity: str, #49: "model_task_WorkItem", #34: "model_organization_OrgUnit", #31: "model_organization_OrgUnit", #37: "model_organization_User", #46: "model_task_WorkItem", #62: "model_task_WorkPackage", task_WorkItem: "model_meeting_WorkItemMeetingSection"):
        self.done = done
        self.activity = activity
        
    @property
    def done(self) -> bool:
        return self.__done

    @done.setter
    def done(self, done: bool):
        self.__done = done

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

class model_bug_BugReport(task_Checkable, task_WorkItem):

    def __init__(self, resolution: str, severity: str, resolutionType: str, done: bool, #49: "model_task_WorkItem", #34: "model_organization_OrgUnit", #31: "model_organization_OrgUnit", #37: "model_organization_User", #46: "model_task_WorkItem", #62: "model_task_WorkPackage", task_WorkItem: "model_meeting_WorkItemMeetingSection"):
        self.resolution = resolution
        self.severity = severity
        self.resolutionType = resolutionType
        self.done = done
        
    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution

    @property
    def done(self) -> bool:
        return self.__done

    @done.setter
    def done(self, done: bool):
        self.__done = done

    @property
    def resolutionType(self) -> str:
        return self.__resolutionType

    @resolutionType.setter
    def resolutionType(self, resolutionType: str):
        self.__resolutionType = resolutionType

    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

class organization_Group:

    pass
class Project:

    pass
class model_Project(Project):

    pass
class model_NonDomainElement(ABC):

    pass
class UnicaseModelElement:

    pass
class model_requirement_ActorInstance(UnicaseModelElement):

    pass
class model_classes_Dependency(UnicaseModelElement):

    pass
class model_profile_StereotypeInstance(UnicaseModelElement):

    pass
class model_requirement_SystemFunction(UnicaseModelElement):

    def __init__(self, exception: str, input: str, output: str, 1246: "requirement_NonFunctionalRequirement" = None, 1249: set["requirement_UseCase"] = None, 1252: "requirement_Workspace" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.exception = exception
        self.input = input
        self.output = output
        self.1246 = 1246
        self.1249 = 1249 if 1249 is not None else set()
        self.1252 = 1252
        
    @property
    def exception(self) -> str:
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def 1246(self):
        return self.__1246

    @1246.setter
    def 1246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__1246", None)
        self.__1246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#247"):
                opp_val = getattr(old_value, "#247", None)
                if opp_val == self:
                    setattr(old_value, "#247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#247"):
                opp_val = getattr(value, "#247", None)
                setattr(value, "#247", self)

    @property
    def 1252(self):
        return self.__1252

    @1252.setter
    def 1252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__1252", None)
        self.__1252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#253"):
                opp_val = getattr(old_value, "#253", None)
                if opp_val == self:
                    setattr(old_value, "#253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#253"):
                opp_val = getattr(value, "#253", None)
                setattr(value, "#253", self)

    @property
    def 1249(self):
        return self.__1249

    @1249.setter
    def 1249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__1249", None)
        self.__1249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#250"):
                    opp_val = getattr(item, "#250", None)
                    
                    if opp_val == self:
                        setattr(item, "#250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#250"):
                    opp_val = getattr(item, "#250", None)
                    
                    setattr(item, "#250", self)
                    

class model_requirement_FunctionalRequirement(UnicaseModelElement):

    def __init__(self, storyPoints: int, priority: int, reviewed: bool, cost: int, 1149: set["requirement_FunctionalRequirement"] = None, 1152: "requirement_FunctionalRequirement" = None, model_requirement_FunctionalRequirement: "organization_OrgUnit" = None, 1159: set["requirement_Scenario"] = None, 1156: set["requirement_UseCase"] = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.storyPoints = storyPoints
        self.priority = priority
        self.reviewed = reviewed
        self.cost = cost
        self.1149 = 1149 if 1149 is not None else set()
        self.1152 = 1152
        self.model_requirement_FunctionalRequirement = model_requirement_FunctionalRequirement
        self.1159 = 1159 if 1159 is not None else set()
        self.1156 = 1156 if 1156 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost

    @property
    def reviewed(self) -> bool:
        return self.__reviewed

    @reviewed.setter
    def reviewed(self, reviewed: bool):
        self.__reviewed = reviewed

    @property
    def storyPoints(self) -> int:
        return self.__storyPoints

    @storyPoints.setter
    def storyPoints(self, storyPoints: int):
        self.__storyPoints = storyPoints

    @property
    def 1156(self):
        return self.__1156

    @1156.setter
    def 1156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__1156", None)
        self.__1156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#157"):
                    opp_val = getattr(item, "#157", None)
                    
                    if opp_val == self:
                        setattr(item, "#157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#157"):
                    opp_val = getattr(item, "#157", None)
                    
                    setattr(item, "#157", self)
                    

    @property
    def 1152(self):
        return self.__1152

    @1152.setter
    def 1152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__1152", None)
        self.__1152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#153"):
                opp_val = getattr(old_value, "#153", None)
                if opp_val == self:
                    setattr(old_value, "#153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#153"):
                opp_val = getattr(value, "#153", None)
                setattr(value, "#153", self)

    @property
    def model_requirement_FunctionalRequirement(self):
        return self.__model_requirement_FunctionalRequirement

    @model_requirement_FunctionalRequirement.setter
    def model_requirement_FunctionalRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__model_requirement_FunctionalRequirement", None)
        self.__model_requirement_FunctionalRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_OrgUnit"):
                opp_val = getattr(old_value, "organization_OrgUnit", None)
                if opp_val == self:
                    setattr(old_value, "organization_OrgUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_OrgUnit"):
                opp_val = getattr(value, "organization_OrgUnit", None)
                setattr(value, "organization_OrgUnit", self)

    @property
    def 1149(self):
        return self.__1149

    @1149.setter
    def 1149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__1149", None)
        self.__1149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#150"):
                    opp_val = getattr(item, "#150", None)
                    
                    if opp_val == self:
                        setattr(item, "#150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#150"):
                    opp_val = getattr(item, "#150", None)
                    
                    setattr(item, "#150", self)
                    

    @property
    def 1159(self):
        return self.__1159

    @1159.setter
    def 1159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__1159", None)
        self.__1159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#160"):
                    opp_val = getattr(item, "#160", None)
                    
                    if opp_val == self:
                        setattr(item, "#160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#160"):
                    opp_val = getattr(item, "#160", None)
                    
                    setattr(item, "#160", self)
                    

class model_activity_ActivityObject(UnicaseModelElement):

    pass
class model_profile_Stereotype(UnicaseModelElement):

    def __init__(self, required: bool, 1377: "profile_Profile" = None, 1380: set["profile_StereotypeInstance"] = None, 1383: set["profile_StereotypeAttribute"] = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.required = required
        self.1377 = 1377
        self.1380 = 1380 if 1380 is not None else set()
        self.1383 = 1383 if 1383 is not None else set()
        
    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def 1377(self):
        return self.__1377

    @1377.setter
    def 1377(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__1377", None)
        self.__1377 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#378"):
                opp_val = getattr(old_value, "#378", None)
                if opp_val == self:
                    setattr(old_value, "#378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#378"):
                opp_val = getattr(value, "#378", None)
                setattr(value, "#378", self)

    @property
    def 1383(self):
        return self.__1383

    @1383.setter
    def 1383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__1383", None)
        self.__1383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#384"):
                    opp_val = getattr(item, "#384", None)
                    
                    if opp_val == self:
                        setattr(item, "#384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#384"):
                    opp_val = getattr(item, "#384", None)
                    
                    setattr(item, "#384", self)
                    

    @property
    def 1380(self):
        return self.__1380

    @1380.setter
    def 1380(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__1380", None)
        self.__1380 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#381"):
                    opp_val = getattr(item, "#381", None)
                    
                    if opp_val == self:
                        setattr(item, "#381", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#381"):
                    opp_val = getattr(item, "#381", None)
                    
                    setattr(item, "#381", self)
                    

class model_rationale_Criterion(UnicaseModelElement):

    pass
class model_requirement_UseCase(UnicaseModelElement):

    def __init__(self, precondition: str, postcondition: str, rules: str, exception: str, 1162: set["requirement_FunctionalRequirement"] = None, 1165: set["classes_Class"] = None, model_requirement_UseCase: set["requirement_UseCase"] = None, model_requirement_UseCase169: set["requirement_UseCase"] = None, 1172: set["requirement_Scenario"] = None, 1175: "requirement_Actor" = None, 1178: set["requirement_Actor"] = None, 1187: set["requirement_NonFunctionalRequirement"] = None, 1190: set["requirement_SystemFunction"] = None, 1181: set["requirement_Step"] = None, 1184: "requirement_UserTask" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.precondition = precondition
        self.postcondition = postcondition
        self.rules = rules
        self.exception = exception
        self.1162 = 1162 if 1162 is not None else set()
        self.1165 = 1165 if 1165 is not None else set()
        self.model_requirement_UseCase = model_requirement_UseCase if model_requirement_UseCase is not None else set()
        self.model_requirement_UseCase169 = model_requirement_UseCase169 if model_requirement_UseCase169 is not None else set()
        self.1172 = 1172 if 1172 is not None else set()
        self.1175 = 1175
        self.1178 = 1178 if 1178 is not None else set()
        self.1187 = 1187 if 1187 is not None else set()
        self.1190 = 1190 if 1190 is not None else set()
        self.1181 = 1181 if 1181 is not None else set()
        self.1184 = 1184
        
    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def exception(self) -> str:
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception

    @property
    def postcondition(self) -> str:
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition

    @property
    def model_requirement_UseCase(self):
        return self.__model_requirement_UseCase

    @model_requirement_UseCase.setter
    def model_requirement_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__model_requirement_UseCase", None)
        self.__model_requirement_UseCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_UseCase"):
                    opp_val = getattr(item, "requirement_UseCase", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_UseCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_UseCase"):
                    opp_val = getattr(item, "requirement_UseCase", None)
                    
                    setattr(item, "requirement_UseCase", self)
                    

    @property
    def 1165(self):
        return self.__1165

    @1165.setter
    def 1165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1165", None)
        self.__1165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#166"):
                    opp_val = getattr(item, "#166", None)
                    
                    if opp_val == self:
                        setattr(item, "#166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#166"):
                    opp_val = getattr(item, "#166", None)
                    
                    setattr(item, "#166", self)
                    

    @property
    def 1187(self):
        return self.__1187

    @1187.setter
    def 1187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1187", None)
        self.__1187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#188"):
                    opp_val = getattr(item, "#188", None)
                    
                    if opp_val == self:
                        setattr(item, "#188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#188"):
                    opp_val = getattr(item, "#188", None)
                    
                    setattr(item, "#188", self)
                    

    @property
    def 1162(self):
        return self.__1162

    @1162.setter
    def 1162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1162", None)
        self.__1162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#163"):
                    opp_val = getattr(item, "#163", None)
                    
                    if opp_val == self:
                        setattr(item, "#163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#163"):
                    opp_val = getattr(item, "#163", None)
                    
                    setattr(item, "#163", self)
                    

    @property
    def 1172(self):
        return self.__1172

    @1172.setter
    def 1172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1172", None)
        self.__1172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#173"):
                    opp_val = getattr(item, "#173", None)
                    
                    if opp_val == self:
                        setattr(item, "#173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#173"):
                    opp_val = getattr(item, "#173", None)
                    
                    setattr(item, "#173", self)
                    

    @property
    def 1181(self):
        return self.__1181

    @1181.setter
    def 1181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1181", None)
        self.__1181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#182"):
                    opp_val = getattr(item, "#182", None)
                    
                    if opp_val == self:
                        setattr(item, "#182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#182"):
                    opp_val = getattr(item, "#182", None)
                    
                    setattr(item, "#182", self)
                    

    @property
    def 1190(self):
        return self.__1190

    @1190.setter
    def 1190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1190", None)
        self.__1190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#191"):
                    opp_val = getattr(item, "#191", None)
                    
                    if opp_val == self:
                        setattr(item, "#191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#191"):
                    opp_val = getattr(item, "#191", None)
                    
                    setattr(item, "#191", self)
                    

    @property
    def model_requirement_UseCase169(self):
        return self.__model_requirement_UseCase169

    @model_requirement_UseCase169.setter
    def model_requirement_UseCase169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__model_requirement_UseCase169", None)
        self.__model_requirement_UseCase169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_UseCase170"):
                    opp_val = getattr(item, "requirement_UseCase170", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_UseCase170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_UseCase170"):
                    opp_val = getattr(item, "requirement_UseCase170", None)
                    
                    setattr(item, "requirement_UseCase170", self)
                    

    @property
    def 1178(self):
        return self.__1178

    @1178.setter
    def 1178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1178", None)
        self.__1178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#179"):
                    opp_val = getattr(item, "#179", None)
                    
                    if opp_val == self:
                        setattr(item, "#179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#179"):
                    opp_val = getattr(item, "#179", None)
                    
                    setattr(item, "#179", self)
                    

    @property
    def 1175(self):
        return self.__1175

    @1175.setter
    def 1175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1175", None)
        self.__1175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#176"):
                opp_val = getattr(old_value, "#176", None)
                if opp_val == self:
                    setattr(old_value, "#176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#176"):
                opp_val = getattr(value, "#176", None)
                setattr(value, "#176", self)

    @property
    def 1184(self):
        return self.__1184

    @1184.setter
    def 1184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__1184", None)
        self.__1184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#185"):
                opp_val = getattr(old_value, "#185", None)
                if opp_val == self:
                    setattr(old_value, "#185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#185"):
                opp_val = getattr(value, "#185", None)
                setattr(value, "#185", self)

class model_component_Component(UnicaseModelElement):

    pass
class model_component_ComponentService(UnicaseModelElement):

    pass
class model_task_Checkable(UnicaseModelElement):

    def __init__(self, checked: bool, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.checked = checked
        
    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

class model_state_StateNode(UnicaseModelElement):

    pass
class model_profile_StereotypeAttributeInstance(UnicaseModelElement):

    pass
class model_classes_Method(UnicaseModelElement):

    def __init__(self, visibility: str, scope: str, returnType: str, stubbed: bool, signature: str, properties: str, label: str, 1118: "classes_Class" = None, 1121: set["classes_Method"] = None, 1124: set["classes_Method"] = None, model_classes_Method: set["classes_MethodArgument"] = None, 1128: set["requirement_Scenario"] = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.visibility = visibility
        self.scope = scope
        self.returnType = returnType
        self.stubbed = stubbed
        self.signature = signature
        self.properties = properties
        self.label = label
        self.1118 = 1118
        self.1121 = 1121 if 1121 is not None else set()
        self.1124 = 1124 if 1124 is not None else set()
        self.model_classes_Method = model_classes_Method if model_classes_Method is not None else set()
        self.1128 = 1128 if 1128 is not None else set()
        
    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def stubbed(self) -> bool:
        return self.__stubbed

    @stubbed.setter
    def stubbed(self, stubbed: bool):
        self.__stubbed = stubbed

    @property
    def 1118(self):
        return self.__1118

    @1118.setter
    def 1118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__1118", None)
        self.__1118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#119"):
                opp_val = getattr(old_value, "#119", None)
                if opp_val == self:
                    setattr(old_value, "#119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#119"):
                opp_val = getattr(value, "#119", None)
                setattr(value, "#119", self)

    @property
    def model_classes_Method(self):
        return self.__model_classes_Method

    @model_classes_Method.setter
    def model_classes_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__model_classes_Method", None)
        self.__model_classes_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_MethodArgument"):
                    opp_val = getattr(item, "classes_MethodArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_MethodArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_MethodArgument"):
                    opp_val = getattr(item, "classes_MethodArgument", None)
                    
                    setattr(item, "classes_MethodArgument", self)
                    

    @property
    def 1124(self):
        return self.__1124

    @1124.setter
    def 1124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__1124", None)
        self.__1124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#125"):
                    opp_val = getattr(item, "#125", None)
                    
                    if opp_val == self:
                        setattr(item, "#125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#125"):
                    opp_val = getattr(item, "#125", None)
                    
                    setattr(item, "#125", self)
                    

    @property
    def 1121(self):
        return self.__1121

    @1121.setter
    def 1121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__1121", None)
        self.__1121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#122"):
                    opp_val = getattr(item, "#122", None)
                    
                    if opp_val == self:
                        setattr(item, "#122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#122"):
                    opp_val = getattr(item, "#122", None)
                    
                    setattr(item, "#122", self)
                    

    @property
    def 1128(self):
        return self.__1128

    @1128.setter
    def 1128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__1128", None)
        self.__1128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#129"):
                    opp_val = getattr(item, "#129", None)
                    
                    if opp_val == self:
                        setattr(item, "#129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#129"):
                    opp_val = getattr(item, "#129", None)
                    
                    setattr(item, "#129", self)
                    

class model_rationale_Proposal(UnicaseModelElement, NonDomainElement):

    pass
class model_change_ModelChangePackage(UnicaseModelElement):

    def __init__(self, sourceVersion: int, targetVersion: int, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.sourceVersion = sourceVersion
        self.targetVersion = targetVersion
        
    @property
    def targetVersion(self) -> int:
        return self.__targetVersion

    @targetVersion.setter
    def targetVersion(self, targetVersion: int):
        self.__targetVersion = targetVersion

    @property
    def sourceVersion(self) -> int:
        return self.__sourceVersion

    @sourceVersion.setter
    def sourceVersion(self, sourceVersion: int):
        self.__sourceVersion = sourceVersion

class model_requirement_UserTask(UnicaseModelElement):

    pass
class model_rationale_Solution(NonDomainElement, UnicaseModelElement):

    pass
class model_meeting_Meeting(UnicaseModelElement):

    def __init__(self, location: str, starttime: date, endtime: date, model_meeting_Meeting: "organization_User" = None, model_meeting_Meeting341: "organization_User" = None, model_meeting_Meeting344: "organization_User" = None, model_meeting_Meeting347: set["organization_OrgUnit"] = None, model_meeting_Meeting350: set["meeting_MeetingSection"] = None, model_meeting_Meeting352: "meeting_IssueMeetingSection" = None, model_meeting_Meeting354: "meeting_WorkItemMeetingSection" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.location = location
        self.starttime = starttime
        self.endtime = endtime
        self.model_meeting_Meeting = model_meeting_Meeting
        self.model_meeting_Meeting341 = model_meeting_Meeting341
        self.model_meeting_Meeting344 = model_meeting_Meeting344
        self.model_meeting_Meeting347 = model_meeting_Meeting347 if model_meeting_Meeting347 is not None else set()
        self.model_meeting_Meeting350 = model_meeting_Meeting350 if model_meeting_Meeting350 is not None else set()
        self.model_meeting_Meeting352 = model_meeting_Meeting352
        self.model_meeting_Meeting354 = model_meeting_Meeting354
        
    @property
    def endtime(self) -> date:
        return self.__endtime

    @endtime.setter
    def endtime(self, endtime: date):
        self.__endtime = endtime

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def starttime(self) -> date:
        return self.__starttime

    @starttime.setter
    def starttime(self, starttime: date):
        self.__starttime = starttime

    @property
    def model_meeting_Meeting(self):
        return self.__model_meeting_Meeting

    @model_meeting_Meeting.setter
    def model_meeting_Meeting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting", None)
        self.__model_meeting_Meeting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_User"):
                opp_val = getattr(old_value, "organization_User", None)
                if opp_val == self:
                    setattr(old_value, "organization_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_User"):
                opp_val = getattr(value, "organization_User", None)
                setattr(value, "organization_User", self)

    @property
    def model_meeting_Meeting347(self):
        return self.__model_meeting_Meeting347

    @model_meeting_Meeting347.setter
    def model_meeting_Meeting347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting347", None)
        self.__model_meeting_Meeting347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organization_OrgUnit348"):
                    opp_val = getattr(item, "organization_OrgUnit348", None)
                    
                    if opp_val == self:
                        setattr(item, "organization_OrgUnit348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organization_OrgUnit348"):
                    opp_val = getattr(item, "organization_OrgUnit348", None)
                    
                    setattr(item, "organization_OrgUnit348", self)
                    

    @property
    def model_meeting_Meeting350(self):
        return self.__model_meeting_Meeting350

    @model_meeting_Meeting350.setter
    def model_meeting_Meeting350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting350", None)
        self.__model_meeting_Meeting350 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "meeting_MeetingSection"):
                    opp_val = getattr(item, "meeting_MeetingSection", None)
                    
                    if opp_val == self:
                        setattr(item, "meeting_MeetingSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "meeting_MeetingSection"):
                    opp_val = getattr(item, "meeting_MeetingSection", None)
                    
                    setattr(item, "meeting_MeetingSection", self)
                    

    @property
    def model_meeting_Meeting352(self):
        return self.__model_meeting_Meeting352

    @model_meeting_Meeting352.setter
    def model_meeting_Meeting352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting352", None)
        self.__model_meeting_Meeting352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "meeting_IssueMeetingSection"):
                opp_val = getattr(old_value, "meeting_IssueMeetingSection", None)
                if opp_val == self:
                    setattr(old_value, "meeting_IssueMeetingSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "meeting_IssueMeetingSection"):
                opp_val = getattr(value, "meeting_IssueMeetingSection", None)
                setattr(value, "meeting_IssueMeetingSection", self)

    @property
    def model_meeting_Meeting354(self):
        return self.__model_meeting_Meeting354

    @model_meeting_Meeting354.setter
    def model_meeting_Meeting354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting354", None)
        self.__model_meeting_Meeting354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "meeting_WorkItemMeetingSection"):
                opp_val = getattr(old_value, "meeting_WorkItemMeetingSection", None)
                if opp_val == self:
                    setattr(old_value, "meeting_WorkItemMeetingSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "meeting_WorkItemMeetingSection"):
                opp_val = getattr(value, "meeting_WorkItemMeetingSection", None)
                setattr(value, "meeting_WorkItemMeetingSection", self)

    @property
    def model_meeting_Meeting344(self):
        return self.__model_meeting_Meeting344

    @model_meeting_Meeting344.setter
    def model_meeting_Meeting344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting344", None)
        self.__model_meeting_Meeting344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_User345"):
                opp_val = getattr(old_value, "organization_User345", None)
                if opp_val == self:
                    setattr(old_value, "organization_User345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_User345"):
                opp_val = getattr(value, "organization_User345", None)
                setattr(value, "organization_User345", self)

    @property
    def model_meeting_Meeting341(self):
        return self.__model_meeting_Meeting341

    @model_meeting_Meeting341.setter
    def model_meeting_Meeting341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting341", None)
        self.__model_meeting_Meeting341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_User342"):
                opp_val = getattr(old_value, "organization_User342", None)
                if opp_val == self:
                    setattr(old_value, "organization_User342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_User342"):
                opp_val = getattr(value, "organization_User342", None)
                setattr(value, "organization_User342", self)

class model_requirement_Scenario(UnicaseModelElement):

    pass
class model_rationale_Comment(NonDomainElement, UnicaseModelElement):

    pass
class model_activity_Transition(UnicaseModelElement):

    def __init__(self, condition: str, 1420: "activity_ActivityObject" = None, 1423: "activity_ActivityObject" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.condition = condition
        self.1420 = 1420
        self.1423 = 1423
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def 1420(self):
        return self.__1420

    @1420.setter
    def 1420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_activity_Transition__1420", None)
        self.__1420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#421"):
                opp_val = getattr(old_value, "#421", None)
                if opp_val == self:
                    setattr(old_value, "#421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#421"):
                opp_val = getattr(value, "#421", None)
                setattr(value, "#421", self)

    @property
    def 1423(self):
        return self.__1423

    @1423.setter
    def 1423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_activity_Transition__1423", None)
        self.__1423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#424"):
                opp_val = getattr(old_value, "#424", None)
                if opp_val == self:
                    setattr(old_value, "#424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#424"):
                opp_val = getattr(value, "#424", None)
                setattr(value, "#424", self)

class model_classes_MethodArgument(UnicaseModelElement):

    def __init__(self, type: str, defaultValue: str, signature: str, label: str, direction: str, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.type = type
        self.defaultValue = defaultValue
        self.signature = signature
        self.label = label
        self.direction = direction
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class model_requirement_Step(NonDomainElement, UnicaseModelElement):

    def __init__(self, userStep: bool, model_requirement_Step: "requirement_UseCase" = None, 1241: "requirement_UseCase" = None, model_requirement_Step244: "requirement_SystemFunction" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.userStep = userStep
        self.model_requirement_Step = model_requirement_Step
        self.1241 = 1241
        self.model_requirement_Step244 = model_requirement_Step244
        
    @property
    def userStep(self) -> bool:
        return self.__userStep

    @userStep.setter
    def userStep(self, userStep: bool):
        self.__userStep = userStep

    @property
    def model_requirement_Step(self):
        return self.__model_requirement_Step

    @model_requirement_Step.setter
    def model_requirement_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_Step__model_requirement_Step", None)
        self.__model_requirement_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_UseCase239"):
                opp_val = getattr(old_value, "requirement_UseCase239", None)
                if opp_val == self:
                    setattr(old_value, "requirement_UseCase239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_UseCase239"):
                opp_val = getattr(value, "requirement_UseCase239", None)
                setattr(value, "requirement_UseCase239", self)

    @property
    def 1241(self):
        return self.__1241

    @1241.setter
    def 1241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_Step__1241", None)
        self.__1241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#242"):
                opp_val = getattr(old_value, "#242", None)
                if opp_val == self:
                    setattr(old_value, "#242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#242"):
                opp_val = getattr(value, "#242", None)
                setattr(value, "#242", self)

    @property
    def model_requirement_Step244(self):
        return self.__model_requirement_Step244

    @model_requirement_Step244.setter
    def model_requirement_Step244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_Step__model_requirement_Step244", None)
        self.__model_requirement_Step244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement_SystemFunction"):
                opp_val = getattr(old_value, "requirement_SystemFunction", None)
                if opp_val == self:
                    setattr(old_value, "requirement_SystemFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_SystemFunction"):
                opp_val = getattr(value, "requirement_SystemFunction", None)
                setattr(value, "requirement_SystemFunction", self)

class model_profile_Profile(UnicaseModelElement):

    pass
class model_requirement_Workspace(UnicaseModelElement):

    pass
class model_classes_Association(UnicaseModelElement):

    def __init__(self, sourceMultiplicity: str, targetMultiplicity: str, sourceRole: str, targetRole: str, type: str, 1109: "classes_Class" = None, 1112: "classes_Class" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.sourceMultiplicity = sourceMultiplicity
        self.targetMultiplicity = targetMultiplicity
        self.sourceRole = sourceRole
        self.targetRole = targetRole
        self.type = type
        self.1109 = 1109
        self.1112 = 1112
        
    @property
    def sourceRole(self) -> str:
        return self.__sourceRole

    @sourceRole.setter
    def sourceRole(self, sourceRole: str):
        self.__sourceRole = sourceRole

    @property
    def sourceMultiplicity(self) -> str:
        return self.__sourceMultiplicity

    @sourceMultiplicity.setter
    def sourceMultiplicity(self, sourceMultiplicity: str):
        self.__sourceMultiplicity = sourceMultiplicity

    @property
    def targetMultiplicity(self) -> str:
        return self.__targetMultiplicity

    @targetMultiplicity.setter
    def targetMultiplicity(self, targetMultiplicity: str):
        self.__targetMultiplicity = targetMultiplicity

    @property
    def targetRole(self) -> str:
        return self.__targetRole

    @targetRole.setter
    def targetRole(self, targetRole: str):
        self.__targetRole = targetRole

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def 1109(self):
        return self.__1109

    @1109.setter
    def 1109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Association__1109", None)
        self.__1109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#110"):
                opp_val = getattr(old_value, "#110", None)
                if opp_val == self:
                    setattr(old_value, "#110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#110"):
                opp_val = getattr(value, "#110", None)
                setattr(value, "#110", self)

    @property
    def 1112(self):
        return self.__1112

    @1112.setter
    def 1112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Association__1112", None)
        self.__1112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#113"):
                opp_val = getattr(old_value, "#113", None)
                if opp_val == self:
                    setattr(old_value, "#113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#113"):
                opp_val = getattr(value, "#113", None)
                setattr(value, "#113", self)

class model_rationale_Assessment(UnicaseModelElement, NonDomainElement):

    def __init__(self, value: int, 1302: "rationale_Proposal" = None, 1305: "rationale_Criterion" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.value = value
        self.1302 = 1302
        self.1305 = 1305
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def 1302(self):
        return self.__1302

    @1302.setter
    def 1302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Assessment__1302", None)
        self.__1302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#303"):
                opp_val = getattr(old_value, "#303", None)
                if opp_val == self:
                    setattr(old_value, "#303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#303"):
                opp_val = getattr(value, "#303", None)
                setattr(value, "#303", self)

    @property
    def 1305(self):
        return self.__1305

    @1305.setter
    def 1305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Assessment__1305", None)
        self.__1305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#306"):
                opp_val = getattr(old_value, "#306", None)
                if opp_val == self:
                    setattr(old_value, "#306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#306"):
                opp_val = getattr(value, "#306", None)
                setattr(value, "#306", self)

class model_profile_StereotypeAttribute(UnicaseModelElement):

    pass
class model_Attachment(UnicaseModelElement):

    pass
class model_organization_OrgUnit(UnicaseModelElement):

    def __init__(self, acOrgId: str, 127: set["organization_Group"] = None, 130: set["task_WorkItem"] = None, 133: set["task_WorkItem"] = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.acOrgId = acOrgId
        self.127 = 127 if 127 is not None else set()
        self.130 = 130 if 130 is not None else set()
        self.133 = 133 if 133 is not None else set()
        
    @property
    def acOrgId(self) -> str:
        return self.__acOrgId

    @acOrgId.setter
    def acOrgId(self, acOrgId: str):
        self.__acOrgId = acOrgId

    @property
    def 127(self):
        return self.__127

    @127.setter
    def 127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__127", None)
        self.__127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#28"):
                    opp_val = getattr(item, "#28", None)
                    
                    if opp_val == self:
                        setattr(item, "#28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#28"):
                    opp_val = getattr(item, "#28", None)
                    
                    setattr(item, "#28", self)
                    

    @property
    def 130(self):
        return self.__130

    @130.setter
    def 130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__130", None)
        self.__130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#31"):
                    opp_val = getattr(item, "#31", None)
                    
                    if opp_val == self:
                        setattr(item, "#31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#31"):
                    opp_val = getattr(item, "#31", None)
                    
                    setattr(item, "#31", self)
                    

    @property
    def 133(self):
        return self.__133

    @133.setter
    def 133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__133", None)
        self.__133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#34"):
                    opp_val = getattr(item, "#34", None)
                    
                    if opp_val == self:
                        setattr(item, "#34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#34"):
                    opp_val = getattr(item, "#34", None)
                    
                    setattr(item, "#34", self)
                    

class model_component_DeploymentNode(UnicaseModelElement):

    pass
class model_classes_Attribute(UnicaseModelElement):

    def __init__(self, signature: str, type: str, defaultValue: str, properties: str, label: str, visibility: str, scope: str, 1115: "classes_Class" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.signature = signature
        self.type = type
        self.defaultValue = defaultValue
        self.properties = properties
        self.label = label
        self.visibility = visibility
        self.scope = scope
        self.1115 = 1115
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def properties(self) -> str:
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def signature(self) -> str:
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def 1115(self):
        return self.__1115

    @1115.setter
    def 1115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Attribute__1115", None)
        self.__1115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#116"):
                opp_val = getattr(old_value, "#116", None)
                if opp_val == self:
                    setattr(old_value, "#116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#116"):
                opp_val = getattr(value, "#116", None)
                setattr(value, "#116", self)

class model_classes_PackageElement(UnicaseModelElement):

    pass
class model_meeting_MeetingSection(UnicaseModelElement):

    def __init__(self, allocatedTime: int, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.allocatedTime = allocatedTime
        
    @property
    def allocatedTime(self) -> int:
        return self.__allocatedTime

    @allocatedTime.setter
    def allocatedTime(self, allocatedTime: int):
        self.__allocatedTime = allocatedTime

class model_state_Transition(UnicaseModelElement):

    def __init__(self, condition: str, 1360: "state_StateNode" = None, 1363: "state_StateNode" = None, #314: "model_rationale_Comment", UnicaseModelElement70: "model_diagram_MEDiagram", #144: "model_document_LeafSection", #141: "model_document_LeafSection", UnicaseModelElement: "model_task_Milestone", #390: "model_profile_StereotypeInstance", #22: "model_Annotation", UnicaseModelElement65: "model_diagram_MEDiagram", #25: "model_Attachment", UnicaseModelElement372: "model_profile_Profile"):
        self.condition = condition
        self.1360 = 1360
        self.1363 = 1363
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def 1360(self):
        return self.__1360

    @1360.setter
    def 1360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_Transition__1360", None)
        self.__1360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#361"):
                opp_val = getattr(old_value, "#361", None)
                if opp_val == self:
                    setattr(old_value, "#361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#361"):
                opp_val = getattr(value, "#361", None)
                setattr(value, "#361", self)

    @property
    def 1363(self):
        return self.__1363

    @1363.setter
    def 1363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_Transition__1363", None)
        self.__1363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#364"):
                opp_val = getattr(old_value, "#364", None)
                if opp_val == self:
                    setattr(old_value, "#364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#364"):
                opp_val = getattr(value, "#364", None)
                setattr(value, "#364", self)

class model_requirement_Actor(UnicaseModelElement):

    pass
class model_document_Section(UnicaseModelElement):

    pass
class model_Annotation(UnicaseModelElement):

    pass
class profile_StereotypeInstance:

    pass
class rationale_Comment:

    pass
class ModelElement:

    pass
class document_LeafSection:

    pass
class Attachment:

    pass
class model_attachment_UrlAttachment(Attachment):

    def __init__(self, url: str, #7: "model_UnicaseModelElement"):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class model_diagram_MEDiagram(Attachment):

    def __init__(self, diagramLayout: str, type: str, model_diagram_MEDiagram: set["UnicaseModelElement"] = None, model_diagram_MEDiagram67: "diagram_model_Diagram" = None, model_diagram_MEDiagram69: set["UnicaseModelElement"] = None, #7: "model_UnicaseModelElement"):
        self.diagramLayout = diagramLayout
        self.type = type
        self.model_diagram_MEDiagram = model_diagram_MEDiagram if model_diagram_MEDiagram is not None else set()
        self.model_diagram_MEDiagram67 = model_diagram_MEDiagram67
        self.model_diagram_MEDiagram69 = model_diagram_MEDiagram69 if model_diagram_MEDiagram69 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def diagramLayout(self) -> str:
        return self.__diagramLayout

    @diagramLayout.setter
    def diagramLayout(self, diagramLayout: str):
        self.__diagramLayout = diagramLayout

    @property
    def model_diagram_MEDiagram69(self):
        return self.__model_diagram_MEDiagram69

    @model_diagram_MEDiagram69.setter
    def model_diagram_MEDiagram69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_diagram_MEDiagram__model_diagram_MEDiagram69", None)
        self.__model_diagram_MEDiagram69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnicaseModelElement70"):
                    opp_val = getattr(item, "UnicaseModelElement70", None)
                    
                    if opp_val == self:
                        setattr(item, "UnicaseModelElement70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnicaseModelElement70"):
                    opp_val = getattr(item, "UnicaseModelElement70", None)
                    
                    setattr(item, "UnicaseModelElement70", self)
                    

    @property
    def model_diagram_MEDiagram67(self):
        return self.__model_diagram_MEDiagram67

    @model_diagram_MEDiagram67.setter
    def model_diagram_MEDiagram67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_diagram_MEDiagram__model_diagram_MEDiagram67", None)
        self.__model_diagram_MEDiagram67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_model_Diagram"):
                opp_val = getattr(old_value, "diagram_model_Diagram", None)
                if opp_val == self:
                    setattr(old_value, "diagram_model_Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_model_Diagram"):
                opp_val = getattr(value, "diagram_model_Diagram", None)
                setattr(value, "diagram_model_Diagram", self)

    @property
    def model_diagram_MEDiagram(self):
        return self.__model_diagram_MEDiagram

    @model_diagram_MEDiagram.setter
    def model_diagram_MEDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_diagram_MEDiagram__model_diagram_MEDiagram", None)
        self.__model_diagram_MEDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnicaseModelElement65"):
                    opp_val = getattr(item, "UnicaseModelElement65", None)
                    
                    if opp_val == self:
                        setattr(item, "UnicaseModelElement65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnicaseModelElement65"):
                    opp_val = getattr(item, "UnicaseModelElement65", None)
                    
                    setattr(item, "UnicaseModelElement65", self)
                    

class model_attachment_FileAttachment(Attachment):

    def __init__(self, fileName: str, fileHash: str, fileID: str, fileSize: str, requiredOffline: bool, fileType: str, uploading: bool, downloading: bool, #7: "model_UnicaseModelElement"):
        self.fileName = fileName
        self.fileHash = fileHash
        self.fileID = fileID
        self.fileSize = fileSize
        self.requiredOffline = requiredOffline
        self.fileType = fileType
        self.uploading = uploading
        self.downloading = downloading
        
    @property
    def uploading(self) -> bool:
        return self.__uploading

    @uploading.setter
    def uploading(self, uploading: bool):
        self.__uploading = uploading

    @property
    def fileType(self) -> str:
        return self.__fileType

    @fileType.setter
    def fileType(self, fileType: str):
        self.__fileType = fileType

    @property
    def requiredOffline(self) -> bool:
        return self.__requiredOffline

    @requiredOffline.setter
    def requiredOffline(self, requiredOffline: bool):
        self.__requiredOffline = requiredOffline

    @property
    def fileHash(self) -> str:
        return self.__fileHash

    @fileHash.setter
    def fileHash(self, fileHash: str):
        self.__fileHash = fileHash

    @property
    def fileID(self) -> str:
        return self.__fileID

    @fileID.setter
    def fileID(self, fileID: str):
        self.__fileID = fileID

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def fileSize(self) -> str:
        return self.__fileSize

    @fileSize.setter
    def fileSize(self, fileSize: str):
        self.__fileSize = fileSize

    @property
    def downloading(self) -> bool:
        return self.__downloading

    @downloading.setter
    def downloading(self, downloading: bool):
        self.__downloading = downloading

class Annotation:

    pass
class model_rationale_Issue(Annotation, task_Checkable, task_WorkItem):

    def __init__(self, activity: str, 1282: set["rationale_Proposal"] = None, 1285: "rationale_Solution" = None, model_rationale_Issue: set["rationale_Criterion"] = None, #: "model_UnicaseModelElement", #49: "model_task_WorkItem", #34: "model_organization_OrgUnit", #31: "model_organization_OrgUnit", #37: "model_organization_User", #46: "model_task_WorkItem", #62: "model_task_WorkPackage", task_WorkItem: "model_meeting_WorkItemMeetingSection"):
        self.activity = activity
        self.1282 = 1282 if 1282 is not None else set()
        self.1285 = 1285
        self.model_rationale_Issue = model_rationale_Issue if model_rationale_Issue is not None else set()
        
    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def model_rationale_Issue(self):
        return self.__model_rationale_Issue

    @model_rationale_Issue.setter
    def model_rationale_Issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Issue__model_rationale_Issue", None)
        self.__model_rationale_Issue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rationale_Criterion"):
                    opp_val = getattr(item, "rationale_Criterion", None)
                    
                    if opp_val == self:
                        setattr(item, "rationale_Criterion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rationale_Criterion"):
                    opp_val = getattr(item, "rationale_Criterion", None)
                    
                    setattr(item, "rationale_Criterion", self)
                    

    @property
    def 1282(self):
        return self.__1282

    @1282.setter
    def 1282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Issue__1282", None)
        self.__1282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#283"):
                    opp_val = getattr(item, "#283", None)
                    
                    if opp_val == self:
                        setattr(item, "#283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#283"):
                    opp_val = getattr(item, "#283", None)
                    
                    setattr(item, "#283", self)
                    

    @property
    def 1285(self):
        return self.__1285

    @1285.setter
    def 1285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Issue__1285", None)
        self.__1285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#286"):
                opp_val = getattr(old_value, "#286", None)
                if opp_val == self:
                    setattr(old_value, "#286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#286"):
                opp_val = getattr(value, "#286", None)
                setattr(value, "#286", self)

class model_task_WorkItem(Annotation):

    def __init__(self, dueDate: date, estimate: int, effort: int, priority: int, resolved: bool, 142: "task_WorkPackage" = None, 145: set["task_WorkItem"] = None, 148: set["task_WorkItem"] = None, 151: "organization_OrgUnit" = None, 154: "organization_User" = None, 157: set["organization_OrgUnit"] = None, model_task_WorkItem: set["change_ModelChangePackage"] = None, #: "model_UnicaseModelElement"):
        self.dueDate = dueDate
        self.estimate = estimate
        self.effort = effort
        self.priority = priority
        self.resolved = resolved
        self.142 = 142
        self.145 = 145 if 145 is not None else set()
        self.148 = 148 if 148 is not None else set()
        self.151 = 151
        self.154 = 154
        self.157 = 157 if 157 is not None else set()
        self.model_task_WorkItem = model_task_WorkItem if model_task_WorkItem is not None else set()
        
    @property
    def estimate(self) -> int:
        return self.__estimate

    @estimate.setter
    def estimate(self, estimate: int):
        self.__estimate = estimate

    @property
    def effort(self) -> int:
        return self.__effort

    @effort.setter
    def effort(self, effort: int):
        self.__effort = effort

    @property
    def resolved(self) -> bool:
        return self.__resolved

    @resolved.setter
    def resolved(self, resolved: bool):
        self.__resolved = resolved

    @property
    def dueDate(self) -> date:
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def 148(self):
        return self.__148

    @148.setter
    def 148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__148", None)
        self.__148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#49"):
                    opp_val = getattr(item, "#49", None)
                    
                    if opp_val == self:
                        setattr(item, "#49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#49"):
                    opp_val = getattr(item, "#49", None)
                    
                    setattr(item, "#49", self)
                    

    @property
    def 151(self):
        return self.__151

    @151.setter
    def 151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__151", None)
        self.__151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#52"):
                opp_val = getattr(old_value, "#52", None)
                if opp_val == self:
                    setattr(old_value, "#52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#52"):
                opp_val = getattr(value, "#52", None)
                setattr(value, "#52", self)

    @property
    def 142(self):
        return self.__142

    @142.setter
    def 142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__142", None)
        self.__142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#43"):
                opp_val = getattr(old_value, "#43", None)
                if opp_val == self:
                    setattr(old_value, "#43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#43"):
                opp_val = getattr(value, "#43", None)
                setattr(value, "#43", self)

    @property
    def model_task_WorkItem(self):
        return self.__model_task_WorkItem

    @model_task_WorkItem.setter
    def model_task_WorkItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__model_task_WorkItem", None)
        self.__model_task_WorkItem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "change_ModelChangePackage"):
                    opp_val = getattr(item, "change_ModelChangePackage", None)
                    
                    if opp_val == self:
                        setattr(item, "change_ModelChangePackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "change_ModelChangePackage"):
                    opp_val = getattr(item, "change_ModelChangePackage", None)
                    
                    setattr(item, "change_ModelChangePackage", self)
                    

    @property
    def 154(self):
        return self.__154

    @154.setter
    def 154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__154", None)
        self.__154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#55"):
                opp_val = getattr(old_value, "#55", None)
                if opp_val == self:
                    setattr(old_value, "#55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#55"):
                opp_val = getattr(value, "#55", None)
                setattr(value, "#55", self)

    @property
    def 157(self):
        return self.__157

    @157.setter
    def 157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__157", None)
        self.__157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#58"):
                    opp_val = getattr(item, "#58", None)
                    
                    if opp_val == self:
                        setattr(item, "#58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#58"):
                    opp_val = getattr(item, "#58", None)
                    
                    setattr(item, "#58", self)
                    

    @property
    def 145(self):
        return self.__145

    @145.setter
    def 145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__145", None)
        self.__145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#46"):
                    opp_val = getattr(item, "#46", None)
                    
                    if opp_val == self:
                        setattr(item, "#46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#46"):
                    opp_val = getattr(item, "#46", None)
                    
                    setattr(item, "#46", self)
                    

class model_UnicaseModelElement(ModelElement):

    def __init__(self, name: str, description: str, state: str, 1: set["Annotation"] = None, 16: set["Attachment"] = None, 19: "document_LeafSection" = None, 115: set["rationale_Comment"] = None, 118: set["profile_StereotypeInstance"] = None, 112: set["document_LeafSection"] = None, ModelElement3: "metamodel_Project", ModelElement: "metamodel_Project"):
        self.name = name
        self.description = description
        self.state = state
        self.1 = 1 if 1 is not None else set()
        self.16 = 16 if 16 is not None else set()
        self.19 = 19
        self.115 = 115 if 115 is not None else set()
        self.118 = 118 if 118 is not None else set()
        self.112 = 112 if 112 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__1", None)
        self.__1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

    @property
    def 112(self):
        return self.__112

    @112.setter
    def 112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__112", None)
        self.__112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#13"):
                    opp_val = getattr(item, "#13", None)
                    
                    if opp_val == self:
                        setattr(item, "#13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#13"):
                    opp_val = getattr(item, "#13", None)
                    
                    setattr(item, "#13", self)
                    

    @property
    def 115(self):
        return self.__115

    @115.setter
    def 115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__115", None)
        self.__115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#16"):
                    opp_val = getattr(item, "#16", None)
                    
                    if opp_val == self:
                        setattr(item, "#16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#16"):
                    opp_val = getattr(item, "#16", None)
                    
                    setattr(item, "#16", self)
                    

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__16", None)
        self.__16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    if opp_val == self:
                        setattr(item, "#7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    setattr(item, "#7", self)
                    

    @property
    def 118(self):
        return self.__118

    @118.setter
    def 118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__118", None)
        self.__118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#19"):
                    opp_val = getattr(item, "#19", None)
                    
                    if opp_val == self:
                        setattr(item, "#19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#19"):
                    opp_val = getattr(item, "#19", None)
                    
                    setattr(item, "#19", self)
                    

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#10"):
                opp_val = getattr(old_value, "#10", None)
                if opp_val == self:
                    setattr(old_value, "#10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#10"):
                opp_val = getattr(value, "#10", None)
                setattr(value, "#10", self)

class metamodel_AssociationClassElement(ABC):

    pass
class metamodel_NonDomainElement(ABC):

    pass
class metamodel_ModelVersion:

    def __init__(self, releaseNumber: int):
        self.releaseNumber = releaseNumber
        
    @property
    def releaseNumber(self) -> int:
        return self.__releaseNumber

    @releaseNumber.setter
    def releaseNumber(self, releaseNumber: int):
        self.__releaseNumber = releaseNumber

class UniqueIdentifier:

    pass
class esmodel_operations_OperationId(UniqueIdentifier):

    pass
class esmodel_accesscontrol_ACOrgUnitId(UniqueIdentifier):

    pass
class esmodel_SessionId(UniqueIdentifier):

    pass
class esmodel_ProjectId(UniqueIdentifier):

    pass
class metamodel_ModelElementId(UniqueIdentifier):

    pass
class IdentifiableElement:

    pass
class esmodel_operations_AbstractOperation(IdentifiableElement):

    def __init__(self, name: str, description: str, accepted: bool, clientDate: date, esmodel_operations_AbstractOperation: "ModelElementId" = None):
        self.name = name
        self.description = description
        self.accepted = accepted
        self.clientDate = clientDate
        self.esmodel_operations_AbstractOperation = esmodel_operations_AbstractOperation
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def clientDate(self) -> date:
        return self.__clientDate

    @clientDate.setter
    def clientDate(self, clientDate: date):
        self.__clientDate = clientDate

    @property
    def accepted(self) -> bool:
        return self.__accepted

    @accepted.setter
    def accepted(self, accepted: bool):
        self.__accepted = accepted

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_operations_AbstractOperation(self):
        return self.__esmodel_operations_AbstractOperation

    @esmodel_operations_AbstractOperation.setter
    def esmodel_operations_AbstractOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_AbstractOperation__esmodel_operations_AbstractOperation", None)
        self.__esmodel_operations_AbstractOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId487"):
                opp_val = getattr(old_value, "ModelElementId487", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId487"):
                opp_val = getattr(value, "ModelElementId487", None)
                setattr(value, "ModelElementId487", self)

class esmodel_notification_ESNotification(IdentifiableElement):

    def __init__(self, name: str, message: str, details: str, seen: bool, creationDate: date, provider: str, sender: str, recipient: str, esmodel_notification_ESNotification: "ProjectId" = None, esmodel_notification_ESNotification607: set["ModelElementId"] = None, esmodel_notification_ESNotification610: set["operations_OperationId"] = None):
        self.name = name
        self.message = message
        self.details = details
        self.seen = seen
        self.creationDate = creationDate
        self.provider = provider
        self.sender = sender
        self.recipient = recipient
        self.esmodel_notification_ESNotification = esmodel_notification_ESNotification
        self.esmodel_notification_ESNotification607 = esmodel_notification_ESNotification607 if esmodel_notification_ESNotification607 is not None else set()
        self.esmodel_notification_ESNotification610 = esmodel_notification_ESNotification610 if esmodel_notification_ESNotification610 is not None else set()
        
    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def recipient(self) -> str:
        return self.__recipient

    @recipient.setter
    def recipient(self, recipient: str):
        self.__recipient = recipient

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def seen(self) -> bool:
        return self.__seen

    @seen.setter
    def seen(self, seen: bool):
        self.__seen = seen

    @property
    def sender(self) -> str:
        return self.__sender

    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def esmodel_notification_ESNotification607(self):
        return self.__esmodel_notification_ESNotification607

    @esmodel_notification_ESNotification607.setter
    def esmodel_notification_ESNotification607(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_notification_ESNotification__esmodel_notification_ESNotification607", None)
        self.__esmodel_notification_ESNotification607 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId608"):
                    opp_val = getattr(item, "ModelElementId608", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId608", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId608"):
                    opp_val = getattr(item, "ModelElementId608", None)
                    
                    setattr(item, "ModelElementId608", self)
                    

    @property
    def esmodel_notification_ESNotification(self):
        return self.__esmodel_notification_ESNotification

    @esmodel_notification_ESNotification.setter
    def esmodel_notification_ESNotification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_notification_ESNotification__esmodel_notification_ESNotification", None)
        self.__esmodel_notification_ESNotification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectId605"):
                opp_val = getattr(old_value, "ProjectId605", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId605", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId605"):
                opp_val = getattr(value, "ProjectId605", None)
                setattr(value, "ProjectId605", self)

    @property
    def esmodel_notification_ESNotification610(self):
        return self.__esmodel_notification_ESNotification610

    @esmodel_notification_ESNotification610.setter
    def esmodel_notification_ESNotification610(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_notification_ESNotification__esmodel_notification_ESNotification610", None)
        self.__esmodel_notification_ESNotification610 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_OperationId611"):
                    opp_val = getattr(item, "operations_OperationId611", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_OperationId611", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_OperationId611"):
                    opp_val = getattr(item, "operations_OperationId611", None)
                    
                    setattr(item, "operations_OperationId611", self)
                    

class esmodel_accesscontrol_ACOrgUnit(IdentifiableElement):

    def __init__(self, description: str, name: str, esmodel_accesscontrol_ACOrgUnit598: set["accesscontrol_OrgUnitProperty"] = None, esmodel_accesscontrol_ACOrgUnit: set["roles_Role"] = None):
        self.description = description
        self.name = name
        self.esmodel_accesscontrol_ACOrgUnit598 = esmodel_accesscontrol_ACOrgUnit598 if esmodel_accesscontrol_ACOrgUnit598 is not None else set()
        self.esmodel_accesscontrol_ACOrgUnit = esmodel_accesscontrol_ACOrgUnit if esmodel_accesscontrol_ACOrgUnit is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def esmodel_accesscontrol_ACOrgUnit598(self):
        return self.__esmodel_accesscontrol_ACOrgUnit598

    @esmodel_accesscontrol_ACOrgUnit598.setter
    def esmodel_accesscontrol_ACOrgUnit598(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_accesscontrol_ACOrgUnit__esmodel_accesscontrol_ACOrgUnit598", None)
        self.__esmodel_accesscontrol_ACOrgUnit598 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accesscontrol_OrgUnitProperty"):
                    opp_val = getattr(item, "accesscontrol_OrgUnitProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "accesscontrol_OrgUnitProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accesscontrol_OrgUnitProperty"):
                    opp_val = getattr(item, "accesscontrol_OrgUnitProperty", None)
                    
                    setattr(item, "accesscontrol_OrgUnitProperty", self)
                    

    @property
    def esmodel_accesscontrol_ACOrgUnit(self):
        return self.__esmodel_accesscontrol_ACOrgUnit

    @esmodel_accesscontrol_ACOrgUnit.setter
    def esmodel_accesscontrol_ACOrgUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_accesscontrol_ACOrgUnit__esmodel_accesscontrol_ACOrgUnit", None)
        self.__esmodel_accesscontrol_ACOrgUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roles_Role"):
                    opp_val = getattr(item, "roles_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "roles_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roles_Role"):
                    opp_val = getattr(item, "roles_Role", None)
                    
                    setattr(item, "roles_Role", self)
                    

    def getId(self) -> str:
        # TODO: Implement getId method
        pass

class metamodel_ModelElement(IdentifiableElement):

    def __init__(self, creator: str, creationDate: date):
        self.creator = creator
        self.creationDate = creationDate
        
    @property
    def creator(self) -> str:
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator

    @property
    def creationDate(self) -> date:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

class metamodel_IdentifiableElement(ABC):

    def __init__(self, identifier: str):
        self.identifier = identifier
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class metamodel_UniqueIdentifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class metamodel_Project:

    pass