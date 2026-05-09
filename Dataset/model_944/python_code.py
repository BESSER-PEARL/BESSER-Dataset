from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResolutionType(Enum):
    FIXED = "FIXED"
    CANNOT_REPRODUCE = "CANNOT_REPRODUCE"
    WONT_FIX = "WONT_FIX"
class ScopeType(Enum):
    INSTANCE = "INSTANCE"
    CLASS = "CLASS"
class FileAttachmentType(Enum):
    BINARY = "BINARY"
    IMAGE = "IMAGE"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
class Severity(Enum):
    FEATURE = "FEATURE"
    TRIVIAL = "TRIVIAL"
    MINOR = "MINOR"
    MAJOR = "MAJOR"
    BLOCKER = "BLOCKER"
class MergeGlobalChoiceSelection(Enum):
    AllMine = "AllMine"
    AllTheir = "AllTheir"
    Cancel = "Cancel"
    OKNotFinished = "OKNotFinished"
    OKFinished = "OKFinished"
class ArgumentDirectionType(Enum):
    UNDEFINED = "UNDEFINED"
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class DiagramType(Enum):
    WORKITEM_DIAGRAM = "WORKITEM_DIAGRAM"
    CLASS_DIAGRAM = "CLASS_DIAGRAM"
    USECASE_DIAGRAM = "USECASE_DIAGRAM"
    COMPONENT_DIAGRAM = "COMPONENT_DIAGRAM"
    STATE_DIAGRAM = "STATE_DIAGRAM"
    ACTIVITY_DIAGRAM = "ACTIVITY_DIAGRAM"
class MergeChoiceSelection(Enum):
    Mine = "Mine"
    Their = "Their"
    Issue = "Issue"
    MergedText = "MergedText"
class AssociationType(Enum):
    UNDIRECTED_ASSOCIATION = "UNDIRECTED_ASSOCIATION"
    DIRECTED_ASSOCIATION = "DIRECTED_ASSOCIATION"
    AGGREGATION = "AGGREGATION"
    COMPOSITION = "COMPOSITION"
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
class VisibilityType(Enum):
    UNDEFINED = "UNDEFINED"
    PACKAGE = "PACKAGE"
    PRIVATE = "PRIVATE"
    GLOBAL = "GLOBAL"
    PROTECTED = "PROTECTED"


############################################
# Definition of Classes
############################################

class esmodel_versioning_HistoryQuery:

    def __init__(self, includeChangePackage: bool, esmodel_versioning_HistoryQuery: "versioning_PrimaryVersionSpec" = None, esmodel_versioning_HistoryQuery327: "versioning_PrimaryVersionSpec" = None, esmodel_versioning_HistoryQuery330: set["ModelElementId"] = None):
        self.includeChangePackage = includeChangePackage
        self.esmodel_versioning_HistoryQuery = esmodel_versioning_HistoryQuery
        self.esmodel_versioning_HistoryQuery327 = esmodel_versioning_HistoryQuery327
        self.esmodel_versioning_HistoryQuery330 = esmodel_versioning_HistoryQuery330 if esmodel_versioning_HistoryQuery330 is not None else set()
        
        pass
    @property
    def includeChangePackage(self):
        return self.__includeChangePackage

    @includeChangePackage.setter
    def includeChangePackage(self, includeChangePackage: bool):
        self.__includeChangePackage = includeChangePackage


    @property
    def esmodel_versioning_HistoryQuery330(self):
        return self.__esmodel_versioning_HistoryQuery330

    @esmodel_versioning_HistoryQuery330.setter
    def esmodel_versioning_HistoryQuery330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_versioning_HistoryQuery__esmodel_versioning_HistoryQuery330", None)
        self.__esmodel_versioning_HistoryQuery330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId331"):
                    opp_val = getattr(item, "ModelElementId331", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId331"):
                    opp_val = getattr(item, "ModelElementId331", None)
                    
                    setattr(item, "ModelElementId331", self)
                    

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
            if hasattr(old_value, "versioning_PrimaryVersionSpec325"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec325", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec325", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec325"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec325", None)
                setattr(value, "versioning_PrimaryVersionSpec325", self)

    @property
    def esmodel_versioning_HistoryQuery327(self):
        return self.__esmodel_versioning_HistoryQuery327

    @esmodel_versioning_HistoryQuery327.setter
    def esmodel_versioning_HistoryQuery327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_versioning_HistoryQuery__esmodel_versioning_HistoryQuery327", None)
        self.__esmodel_versioning_HistoryQuery327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec328"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec328", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec328"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec328", None)
                setattr(value, "versioning_PrimaryVersionSpec328", self)

class versioning_ChangePackage:

    pass
class accesscontrol_ACUser:

    pass
class SessionId:

    pass
class ProjectHistory:

    pass
class accesscontrol_ACGroup:

    pass
class esmodel_ServerSpace:

    pass
class versioning_PrimaryVersionSpec:

    pass
class esmodel_ProjectInfo:

    def __init__(self, name: str, description: str, esmodel_ProjectInfo: "ProjectId" = None, esmodel_ProjectInfo295: "versioning_PrimaryVersionSpec" = None):
        self.name = name
        self.description = description
        self.esmodel_ProjectInfo = esmodel_ProjectInfo
        self.esmodel_ProjectInfo295 = esmodel_ProjectInfo295
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def esmodel_ProjectInfo295(self):
        return self.__esmodel_ProjectInfo295

    @esmodel_ProjectInfo295.setter
    def esmodel_ProjectInfo295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectInfo__esmodel_ProjectInfo295", None)
        self.__esmodel_ProjectInfo295 = value
        
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
            if hasattr(old_value, "ProjectId293"):
                opp_val = getattr(old_value, "ProjectId293", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId293"):
                opp_val = getattr(value, "ProjectId293", None)
                setattr(value, "ProjectId293", self)

class versioning_Version:

    pass
class ProjectId:

    pass
class esmodel_ProjectHistory:

    def __init__(self, projectName: str, projectDescription: str, esmodel_ProjectHistory: "ProjectId" = None, esmodel_ProjectHistory291: set["versioning_Version"] = None):
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.esmodel_ProjectHistory = esmodel_ProjectHistory
        self.esmodel_ProjectHistory291 = esmodel_ProjectHistory291 if esmodel_ProjectHistory291 is not None else set()
        
        pass
    @property
    def projectName(self):
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName


    @property
    def projectDescription(self):
        return self.__projectDescription

    @projectDescription.setter
    def projectDescription(self, projectDescription: str):
        self.__projectDescription = projectDescription


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
    def esmodel_ProjectHistory291(self):
        return self.__esmodel_ProjectHistory291

    @esmodel_ProjectHistory291.setter
    def esmodel_ProjectHistory291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_ProjectHistory__esmodel_ProjectHistory291", None)
        self.__esmodel_ProjectHistory291 = value if value is not None else set()
        
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
                    

class ActivityObject:

    pass
class model_activity_Branch(ActivityObject):

    pass
class model_activity_Fork(ActivityObject):

    pass
class model_activity_ActivityEnd(ActivityObject):

    pass
class model_activity_ActivityInitial(ActivityObject):

    pass
class model_activity_Activity(ActivityObject):

    pass
class esmodel_ClientVersionInfo:

    def __init__(self, version: str, name: str):
        self.version = version
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


class esmodel_VersionInfo:

    def __init__(self, emfStoreVersionString: str):
        self.emfStoreVersionString = emfStoreVersionString
        
        pass
    @property
    def emfStoreVersionString(self):
        return self.__emfStoreVersionString

    @emfStoreVersionString.setter
    def emfStoreVersionString(self, emfStoreVersionString: str):
        self.__emfStoreVersionString = emfStoreVersionString


class activity_ActivityObject:

    pass
class activity_Transition:

    pass
class ModelElementId:

    pass
class model_util_ModelElementPath:

    pass
class StereotypeAttributeInstance:

    pass
class model_profile_StereotypeAttributeInstanceString(StereotypeAttributeInstance):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class StereotypeAttribute:

    pass
class model_profile_StereotypeAttributeSimple(StereotypeAttribute):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class profile_StereotypeAttributeInstance:

    pass
class profile_Profile:

    pass
class profile_Stereotype:

    pass
class profile_StereotypeAttribute:

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
        
        pass
    @property
    def entryConditions(self):
        return self.__entryConditions

    @entryConditions.setter
    def entryConditions(self, entryConditions: str):
        self.__entryConditions = entryConditions


    @property
    def exitConditions(self):
        return self.__exitConditions

    @exitConditions.setter
    def exitConditions(self, exitConditions: str):
        self.__exitConditions = exitConditions


    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, activities: str):
        self.__activities = activities


class state_Transition:

    pass
class state_StateNode:

    pass
class url_ModelElementUrlFragment:

    pass
class url_ProjectUrlFragment:

    pass
class url_ServerUrl:

    pass
class esmodel_url_ModelElementUrl:

    pass
class MeetingSection:

    pass
class model_meeting_IssueMeetingSection(MeetingSection):

    pass
class model_meeting_WorkItemMeetingSection(MeetingSection):

    pass
class meeting_WorkItemMeetingSection:

    pass
class meeting_IssueMeetingSection:

    pass
class meeting_MeetingSection:

    pass
class Role:

    pass
class esmodel_roles_ServerAdmin(Role):

    pass
class esmodel_roles_WriterRole(Role):

    pass
class esmodel_roles_ProjectAdminRole(Role):

    pass
class model_meeting_CompositeMeetingSection(MeetingSection):

    pass
class esmodel_roles_ReaderRole(Role):

    pass
class component_Component:

    pass
class esmodel_url_ModelElementUrlFragment:

    def __init__(self, name: str, esmodel_url_ModelElementUrlFragment: "ModelElementId" = None):
        self.name = name
        self.esmodel_url_ModelElementUrlFragment = esmodel_url_ModelElementUrlFragment
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "ModelElementId477"):
                opp_val = getattr(old_value, "ModelElementId477", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId477"):
                opp_val = getattr(value, "ModelElementId477", None)
                setattr(value, "ModelElementId477", self)

class esmodel_url_ProjectUrlFragment:

    def __init__(self, name: str, esmodel_url_ProjectUrlFragment: "ProjectId" = None):
        self.name = name
        self.esmodel_url_ProjectUrlFragment = esmodel_url_ProjectUrlFragment
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "ProjectId475"):
                opp_val = getattr(old_value, "ProjectId475", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId475", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId475"):
                opp_val = getattr(value, "ProjectId475", None)
                setattr(value, "ProjectId475", self)

class component_ComponentService:

    pass
class esmodel_url_ServerUrl:

    def __init__(self, hostName: str, port: int):
        self.hostName = hostName
        self.port = port
        
        pass
    @property
    def hostName(self):
        return self.__hostName

    @hostName.setter
    def hostName(self, hostName: str):
        self.__hostName = hostName


    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port


class roles_Role:

    pass
class ACOrgUnit:

    pass
class change_MergingProposal:

    pass
class esmodel_accesscontrol_ACUser(ACOrgUnit):

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
        pass
    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


class Proposal:

    pass
class ServerProjectEvent:

    pass
class model_change_MergingProposal(Proposal):

    pass
class esmodel_server_ProjectUpdatedEvent(ServerProjectEvent):

    pass
class Issue:

    pass
class ServerEvent:

    pass
class model_change_MergingIssue(Issue):

    def __init__(self, resolvingRevision: int):
        self.resolvingRevision = resolvingRevision
        
        pass
    @property
    def resolvingRevision(self):
        return self.__resolvingRevision

    @resolvingRevision.setter
    def resolvingRevision(self, resolvingRevision: int):
        self.__resolvingRevision = resolvingRevision


class esmodel_server_ServerProjectEvent(ServerEvent):

    pass
class attachment_FileAttachment:

    pass
class model_rationale_AudioComment:

    pass
class esmodel_roles_Role(ABC):

    def __init__(self, esmodel_roles_Role: set["ProjectId"] = None):
        self.esmodel_roles_Role = esmodel_roles_Role if esmodel_roles_Role is not None else set()
        
        pass
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
                if hasattr(item, "ProjectId465"):
                    opp_val = getattr(item, "ProjectId465", None)
                    
                    if opp_val == self:
                        setattr(item, "ProjectId465", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProjectId465"):
                    opp_val = getattr(item, "ProjectId465", None)
                    
                    setattr(item, "ProjectId465", self)
                    

    def canModify(self, esmodel_projectId, esmodel_modelElement) :
        # TODO: Implement canModify method
        pass

    def canAdministrate(self, esmodel_projectId) :
        # TODO: Implement canAdministrate method
        pass

    def canRead(self, esmodel_projectId, esmodel_modelElement) :
        # TODO: Implement canRead method
        pass

    def canDelete(self, esmodel_projectId, esmodel_modelElement) :
        # TODO: Implement canDelete method
        pass

    def canCreate(self, esmodel_projectId, esmodel_modelElement) :
        # TODO: Implement canCreate method
        pass

class esmodel_accesscontrol_OrgUnitProperty:

    def __init__(self, name: str, value: str, esmodel_accesscontrol_OrgUnitProperty: "ProjectId" = None):
        self.name = name
        self.value = value
        self.esmodel_accesscontrol_OrgUnitProperty = esmodel_accesscontrol_OrgUnitProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
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
            if hasattr(old_value, "ProjectId463"):
                opp_val = getattr(old_value, "ProjectId463", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId463"):
                opp_val = getattr(value, "ProjectId463", None)
                setattr(value, "ProjectId463", self)

class accesscontrol_ACOrgUnit:

    pass
class esmodel_accesscontrol_ACGroup(ACOrgUnit):

    pass
class accesscontrol_OrgUnitProperty:

    pass
class ReadEvent:

    pass
class esmodel_events_NotificationReadEvent(ReadEvent):

    def __init__(self, notificationId: str):
        self.notificationId = notificationId
        
        pass
    @property
    def notificationId(self):
        return self.__notificationId

    @notificationId.setter
    def notificationId(self, notificationId: str):
        self.__notificationId = notificationId


class operations_OperationId:

    pass
class Solution:

    pass
class model_change_MergingSolution(Solution):

    pass
class rationale_Assessment:

    pass
class rationale_Issue:

    pass
class rationale_Criterion:

    pass
class Event:

    pass
class esmodel_events_CheckoutEvent(Event):

    pass
class esmodel_events_MergeGlobalChoiceEvent(Event):

    def __init__(self, selection: str):
        self.selection = selection
        
        pass
    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection


class esmodel_events_TraceEvent(Event):

    def __init__(self, featureName: str, esmodel_events_TraceEvent: "ModelElementId" = None, esmodel_events_TraceEvent426: "ModelElementId" = None):
        self.featureName = featureName
        self.esmodel_events_TraceEvent = esmodel_events_TraceEvent
        self.esmodel_events_TraceEvent426 = esmodel_events_TraceEvent426
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def esmodel_events_TraceEvent426(self):
        return self.__esmodel_events_TraceEvent426

    @esmodel_events_TraceEvent426.setter
    def esmodel_events_TraceEvent426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_TraceEvent__esmodel_events_TraceEvent426", None)
        self.__esmodel_events_TraceEvent426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId427"):
                opp_val = getattr(old_value, "ModelElementId427", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId427"):
                opp_val = getattr(value, "ModelElementId427", None)
                setattr(value, "ModelElementId427", self)

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
            if hasattr(old_value, "ModelElementId424"):
                opp_val = getattr(old_value, "ModelElementId424", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId424"):
                opp_val = getattr(value, "ModelElementId424", None)
                setattr(value, "ModelElementId424", self)

class esmodel_events_ExceptionEvent(Event):

    def __init__(self, ExceptionCauseStackTrace: str, ExceptionTitle: str, ExceptionStackTrace: str, ExceptionCauseTitle: str):
        self.ExceptionCauseStackTrace = ExceptionCauseStackTrace
        self.ExceptionTitle = ExceptionTitle
        self.ExceptionStackTrace = ExceptionStackTrace
        self.ExceptionCauseTitle = ExceptionCauseTitle
        
        pass
    @property
    def ExceptionStackTrace(self):
        return self.__ExceptionStackTrace

    @ExceptionStackTrace.setter
    def ExceptionStackTrace(self, ExceptionStackTrace: str):
        self.__ExceptionStackTrace = ExceptionStackTrace


    @property
    def ExceptionCauseTitle(self):
        return self.__ExceptionCauseTitle

    @ExceptionCauseTitle.setter
    def ExceptionCauseTitle(self, ExceptionCauseTitle: str):
        self.__ExceptionCauseTitle = ExceptionCauseTitle


    @property
    def ExceptionCauseStackTrace(self):
        return self.__ExceptionCauseStackTrace

    @ExceptionCauseStackTrace.setter
    def ExceptionCauseStackTrace(self, ExceptionCauseStackTrace: str):
        self.__ExceptionCauseStackTrace = ExceptionCauseStackTrace


    @property
    def ExceptionTitle(self):
        return self.__ExceptionTitle

    @ExceptionTitle.setter
    def ExceptionTitle(self, ExceptionTitle: str):
        self.__ExceptionTitle = ExceptionTitle


class esmodel_events_Validate(Event):

    pass
class esmodel_events_MergeChoiceEvent(Event):

    def __init__(self, selection: str, contextFeature: str, createdIssueName: str, esmodel_events_MergeChoiceEvent449: set["operations_OperationId"] = None, esmodel_events_MergeChoiceEvent452: "ModelElementId" = None, esmodel_events_MergeChoiceEvent: set["operations_OperationId"] = None):
        self.selection = selection
        self.contextFeature = contextFeature
        self.createdIssueName = createdIssueName
        self.esmodel_events_MergeChoiceEvent449 = esmodel_events_MergeChoiceEvent449 if esmodel_events_MergeChoiceEvent449 is not None else set()
        self.esmodel_events_MergeChoiceEvent452 = esmodel_events_MergeChoiceEvent452
        self.esmodel_events_MergeChoiceEvent = esmodel_events_MergeChoiceEvent if esmodel_events_MergeChoiceEvent is not None else set()
        
        pass
    @property
    def createdIssueName(self):
        return self.__createdIssueName

    @createdIssueName.setter
    def createdIssueName(self, createdIssueName: str):
        self.__createdIssueName = createdIssueName


    @property
    def contextFeature(self):
        return self.__contextFeature

    @contextFeature.setter
    def contextFeature(self, contextFeature: str):
        self.__contextFeature = contextFeature


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection


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
                    

    @property
    def esmodel_events_MergeChoiceEvent452(self):
        return self.__esmodel_events_MergeChoiceEvent452

    @esmodel_events_MergeChoiceEvent452.setter
    def esmodel_events_MergeChoiceEvent452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeChoiceEvent__esmodel_events_MergeChoiceEvent452", None)
        self.__esmodel_events_MergeChoiceEvent452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId453"):
                opp_val = getattr(old_value, "ModelElementId453", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId453"):
                opp_val = getattr(value, "ModelElementId453", None)
                setattr(value, "ModelElementId453", self)

    @property
    def esmodel_events_MergeChoiceEvent449(self):
        return self.__esmodel_events_MergeChoiceEvent449

    @esmodel_events_MergeChoiceEvent449.setter
    def esmodel_events_MergeChoiceEvent449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeChoiceEvent__esmodel_events_MergeChoiceEvent449", None)
        self.__esmodel_events_MergeChoiceEvent449 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_OperationId450"):
                    opp_val = getattr(item, "operations_OperationId450", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_OperationId450", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_OperationId450"):
                    opp_val = getattr(item, "operations_OperationId450", None)
                    
                    setattr(item, "operations_OperationId450", self)
                    

class esmodel_server_ServerEvent(Event):

    pass
class esmodel_events_URLEvent(Event):

    def __init__(self, sourceView: str, esmodel_events_URLEvent: "ModelElementId" = None, esmodel_events_URLEvent445: "ModelElementId" = None):
        self.sourceView = sourceView
        self.esmodel_events_URLEvent = esmodel_events_URLEvent
        self.esmodel_events_URLEvent445 = esmodel_events_URLEvent445
        
        pass
    @property
    def sourceView(self):
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView


    @property
    def esmodel_events_URLEvent445(self):
        return self.__esmodel_events_URLEvent445

    @esmodel_events_URLEvent445.setter
    def esmodel_events_URLEvent445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_URLEvent__esmodel_events_URLEvent445", None)
        self.__esmodel_events_URLEvent445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId446"):
                opp_val = getattr(old_value, "ModelElementId446", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId446"):
                opp_val = getattr(value, "ModelElementId446", None)
                setattr(value, "ModelElementId446", self)

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
            if hasattr(old_value, "ModelElementId443"):
                opp_val = getattr(old_value, "ModelElementId443", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId443", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId443"):
                opp_val = getattr(value, "ModelElementId443", None)
                setattr(value, "ModelElementId443", self)

class esmodel_events_MergeEvent(Event):

    def __init__(self, numberOfConflicts: int, totalTime: int, esmodel_events_MergeEvent: "versioning_PrimaryVersionSpec" = None, esmodel_events_MergeEvent388: "versioning_PrimaryVersionSpec" = None, esmodel_events_MergeEvent391: set["operations_AbstractOperation"] = None):
        self.numberOfConflicts = numberOfConflicts
        self.totalTime = totalTime
        self.esmodel_events_MergeEvent = esmodel_events_MergeEvent
        self.esmodel_events_MergeEvent388 = esmodel_events_MergeEvent388
        self.esmodel_events_MergeEvent391 = esmodel_events_MergeEvent391 if esmodel_events_MergeEvent391 is not None else set()
        
        pass
    @property
    def numberOfConflicts(self):
        return self.__numberOfConflicts

    @numberOfConflicts.setter
    def numberOfConflicts(self, numberOfConflicts: int):
        self.__numberOfConflicts = numberOfConflicts


    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, totalTime: int):
        self.__totalTime = totalTime


    @property
    def esmodel_events_MergeEvent391(self):
        return self.__esmodel_events_MergeEvent391

    @esmodel_events_MergeEvent391.setter
    def esmodel_events_MergeEvent391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeEvent__esmodel_events_MergeEvent391", None)
        self.__esmodel_events_MergeEvent391 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_AbstractOperation392"):
                    opp_val = getattr(item, "operations_AbstractOperation392", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation392", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation392"):
                    opp_val = getattr(item, "operations_AbstractOperation392", None)
                    
                    setattr(item, "operations_AbstractOperation392", self)
                    

    @property
    def esmodel_events_MergeEvent388(self):
        return self.__esmodel_events_MergeEvent388

    @esmodel_events_MergeEvent388.setter
    def esmodel_events_MergeEvent388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_MergeEvent__esmodel_events_MergeEvent388", None)
        self.__esmodel_events_MergeEvent388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versioning_PrimaryVersionSpec389"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec389", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec389"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec389", None)
                setattr(value, "versioning_PrimaryVersionSpec389", self)

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
            if hasattr(old_value, "versioning_PrimaryVersionSpec386"):
                opp_val = getattr(old_value, "versioning_PrimaryVersionSpec386", None)
                if opp_val == self:
                    setattr(old_value, "versioning_PrimaryVersionSpec386", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versioning_PrimaryVersionSpec386"):
                opp_val = getattr(value, "versioning_PrimaryVersionSpec386", None)
                setattr(value, "versioning_PrimaryVersionSpec386", self)

class esmodel_events_PresentationSwitchEvent(Event):

    def __init__(self, readView: str, newPresentation: str):
        self.readView = readView
        self.newPresentation = newPresentation
        
        pass
    @property
    def readView(self):
        return self.__readView

    @readView.setter
    def readView(self, readView: str):
        self.__readView = readView


    @property
    def newPresentation(self):
        return self.__newPresentation

    @newPresentation.setter
    def newPresentation(self, newPresentation: str):
        self.__newPresentation = newPresentation


class esmodel_events_PerspectiveEvent(Event):

    pass
class esmodel_events_DNDEvent(Event):

    def __init__(self, sourceView: str, targetView: str, esmodel_events_DNDEvent: "ModelElementId" = None, esmodel_events_DNDEvent416: "ModelElementId" = None):
        self.sourceView = sourceView
        self.targetView = targetView
        self.esmodel_events_DNDEvent = esmodel_events_DNDEvent
        self.esmodel_events_DNDEvent416 = esmodel_events_DNDEvent416
        
        pass
    @property
    def sourceView(self):
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView


    @property
    def targetView(self):
        return self.__targetView

    @targetView.setter
    def targetView(self, targetView: str):
        self.__targetView = targetView


    @property
    def esmodel_events_DNDEvent416(self):
        return self.__esmodel_events_DNDEvent416

    @esmodel_events_DNDEvent416.setter
    def esmodel_events_DNDEvent416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_DNDEvent__esmodel_events_DNDEvent416", None)
        self.__esmodel_events_DNDEvent416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId417"):
                opp_val = getattr(old_value, "ModelElementId417", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId417"):
                opp_val = getattr(value, "ModelElementId417", None)
                setattr(value, "ModelElementId417", self)

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
            if hasattr(old_value, "ModelElementId414"):
                opp_val = getattr(old_value, "ModelElementId414", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId414"):
                opp_val = getattr(value, "ModelElementId414", None)
                setattr(value, "ModelElementId414", self)

class esmodel_events_NotificationIgnoreEvent(Event):

    def __init__(self, notificationId: str):
        self.notificationId = notificationId
        
        pass
    @property
    def notificationId(self):
        return self.__notificationId

    @notificationId.setter
    def notificationId(self, notificationId: str):
        self.__notificationId = notificationId


class esmodel_events_ShowChangesEvent(Event):

    pass
class esmodel_events_NotificationGenerationEvent(Event):

    pass
class esmodel_events_NavigatorCreateEvent(Event):

    def __init__(self, dynamic: bool, esmodel_events_NavigatorCreateEvent: "ModelElementId" = None, esmodel_events_NavigatorCreateEvent431: "ModelElementId" = None):
        self.dynamic = dynamic
        self.esmodel_events_NavigatorCreateEvent = esmodel_events_NavigatorCreateEvent
        self.esmodel_events_NavigatorCreateEvent431 = esmodel_events_NavigatorCreateEvent431
        
        pass
    @property
    def dynamic(self):
        return self.__dynamic

    @dynamic.setter
    def dynamic(self, dynamic: bool):
        self.__dynamic = dynamic


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
            if hasattr(old_value, "ModelElementId429"):
                opp_val = getattr(old_value, "ModelElementId429", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId429"):
                opp_val = getattr(value, "ModelElementId429", None)
                setattr(value, "ModelElementId429", self)

    @property
    def esmodel_events_NavigatorCreateEvent431(self):
        return self.__esmodel_events_NavigatorCreateEvent431

    @esmodel_events_NavigatorCreateEvent431.setter
    def esmodel_events_NavigatorCreateEvent431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_NavigatorCreateEvent__esmodel_events_NavigatorCreateEvent431", None)
        self.__esmodel_events_NavigatorCreateEvent431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId432"):
                opp_val = getattr(old_value, "ModelElementId432", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId432"):
                opp_val = getattr(value, "ModelElementId432", None)
                setattr(value, "ModelElementId432", self)

class esmodel_events_UndoEvent(Event):

    pass
class esmodel_events_PluginFocusEvent(Event):

    def __init__(self, pluginId: str, startDate: date):
        self.pluginId = pluginId
        self.startDate = startDate
        
        pass
    @property
    def pluginId(self):
        return self.__pluginId

    @pluginId.setter
    def pluginId(self, pluginId: str):
        self.__pluginId = pluginId


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


class esmodel_events_LinkEvent(Event):

    def __init__(self, sourceView: str, createdNew: bool, esmodel_events_LinkEvent: "ModelElementId" = None, esmodel_events_LinkEvent421: "ModelElementId" = None):
        self.sourceView = sourceView
        self.createdNew = createdNew
        self.esmodel_events_LinkEvent = esmodel_events_LinkEvent
        self.esmodel_events_LinkEvent421 = esmodel_events_LinkEvent421
        
        pass
    @property
    def sourceView(self):
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView


    @property
    def createdNew(self):
        return self.__createdNew

    @createdNew.setter
    def createdNew(self, createdNew: bool):
        self.__createdNew = createdNew


    @property
    def esmodel_events_LinkEvent421(self):
        return self.__esmodel_events_LinkEvent421

    @esmodel_events_LinkEvent421.setter
    def esmodel_events_LinkEvent421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_events_LinkEvent__esmodel_events_LinkEvent421", None)
        self.__esmodel_events_LinkEvent421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId422"):
                opp_val = getattr(old_value, "ModelElementId422", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId422"):
                opp_val = getattr(value, "ModelElementId422", None)
                setattr(value, "ModelElementId422", self)

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
            if hasattr(old_value, "ModelElementId419"):
                opp_val = getattr(old_value, "ModelElementId419", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId419"):
                opp_val = getattr(value, "ModelElementId419", None)
                setattr(value, "ModelElementId419", self)

class rationale_Solution:

    pass
class esmodel_events_ReadEvent(Event):

    def __init__(self, sourceView: str, readView: str, esmodel_events_ReadEvent: "ModelElementId" = None):
        self.sourceView = sourceView
        self.readView = readView
        self.esmodel_events_ReadEvent = esmodel_events_ReadEvent
        
        pass
    @property
    def sourceView(self):
        return self.__sourceView

    @sourceView.setter
    def sourceView(self, sourceView: str):
        self.__sourceView = sourceView


    @property
    def readView(self):
        return self.__readView

    @readView.setter
    def readView(self, readView: str):
        self.__readView = readView


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
            if hasattr(old_value, "ModelElementId384"):
                opp_val = getattr(old_value, "ModelElementId384", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId384"):
                opp_val = getattr(value, "ModelElementId384", None)
                setattr(value, "ModelElementId384", self)

class rationale_Proposal:

    pass
class esmodel_events_Event:

    def __init__(self, timestamp: date):
        self.timestamp = timestamp
        
        pass
    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp


class esmodel_events_ShowHistoryEvent(Event):

    pass
class CompositeOperation:

    pass
class Criterion:

    pass
class esmodel_events_RevertEvent(Event):

    def __init__(self, revertedChangesCount: int):
        self.revertedChangesCount = revertedChangesCount
        
        pass
    @property
    def revertedChangesCount(self):
        return self.__revertedChangesCount

    @revertedChangesCount.setter
    def revertedChangesCount(self, revertedChangesCount: int):
        self.__revertedChangesCount = revertedChangesCount


class model_requirement_NonFunctionalRequirement(Criterion):

    pass
class esmodel_events_AnnotationEvent(Event):

    pass
class esmodel_events_UpdateEvent(Event):

    pass
class NonDomainElement:

    pass
class esmodel_events_PluginStartEvent(Event):

    def __init__(self, pluginId: str):
        self.pluginId = pluginId
        
        pass
    @property
    def pluginId(self):
        return self.__pluginId

    @pluginId.setter
    def pluginId(self, pluginId: str):
        self.__pluginId = pluginId


class esmodel_operations_OperationGroup:

    def __init__(self, name: str, esmodel_operations_OperationGroup: set["operations_AbstractOperation"] = None):
        self.name = name
        self.esmodel_operations_OperationGroup = esmodel_operations_OperationGroup if esmodel_operations_OperationGroup is not None else set()
        
        pass
    @property
    def name(self):
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
                if hasattr(item, "operations_AbstractOperation375"):
                    opp_val = getattr(item, "operations_AbstractOperation375", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation375", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation375"):
                    opp_val = getattr(item, "operations_AbstractOperation375", None)
                    
                    setattr(item, "operations_AbstractOperation375", self)
                    

class requirement_Workspace:

    pass
class requirement_ActorInstance:

    pass
class requirement_SystemFunction:

    pass
class requirement_NonFunctionalRequirement:

    pass
class requirement_UserTask:

    pass
class requirement_Step:

    pass
class requirement_Actor:

    pass
class AttributeOperation:

    pass
class requirement_FunctionalRequirement:

    pass
class esmodel_operations_DiagramLayoutOperation(AttributeOperation):

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
class classes_Attribute:

    pass
class diagram_model_Diagram:

    pass
class task_Checkable:

    pass
class esmodel_semantic_SemanticCompositeOperation(CompositeOperation):

    pass
class esmodel_operations_EObjectToModelElementIdMap:

    pass
class esmodel_operations_ModelElementGroup:

    def __init__(self, name: str, esmodel_operations_ModelElementGroup: set["ModelElementId"] = None):
        self.name = name
        self.esmodel_operations_ModelElementGroup = esmodel_operations_ModelElementGroup if esmodel_operations_ModelElementGroup is not None else set()
        
        pass
    @property
    def name(self):
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
                if hasattr(item, "ModelElementId377"):
                    opp_val = getattr(item, "ModelElementId377", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId377", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId377"):
                    opp_val = getattr(item, "ModelElementId377", None)
                    
                    setattr(item, "ModelElementId377", self)
                    

class FeatureOperation:

    pass
class esmodel_operations_MultiAttributeOperation(FeatureOperation):

    def __init__(self, add: bool, indexes: int, referencedValues: str):
        self.add = add
        self.indexes = indexes
        self.referencedValues = referencedValues
        
        pass
    @property
    def add(self):
        return self.__add

    @add.setter
    def add(self, add: bool):
        self.__add = add


    @property
    def indexes(self):
        return self.__indexes

    @indexes.setter
    def indexes(self, indexes: int):
        self.__indexes = indexes


    @property
    def referencedValues(self):
        return self.__referencedValues

    @referencedValues.setter
    def referencedValues(self, referencedValues: str):
        self.__referencedValues = referencedValues


class esmodel_operations_ReferenceOperation(FeatureOperation):

    def __init__(self, bidirectional: bool, oppositeFeatureName: str, containmentType: str):
        self.bidirectional = bidirectional
        self.oppositeFeatureName = oppositeFeatureName
        self.containmentType = containmentType
        
        pass
    @property
    def oppositeFeatureName(self):
        return self.__oppositeFeatureName

    @oppositeFeatureName.setter
    def oppositeFeatureName(self, oppositeFeatureName: str):
        self.__oppositeFeatureName = oppositeFeatureName


    @property
    def bidirectional(self):
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: bool):
        self.__bidirectional = bidirectional


    @property
    def containmentType(self):
        return self.__containmentType

    @containmentType.setter
    def containmentType(self, containmentType: str):
        self.__containmentType = containmentType


class esmodel_operations_MultiReferenceMoveOperation(FeatureOperation):

    def __init__(self, oldIndex: int, newIndex: int, esmodel_operations_MultiReferenceMoveOperation: "ModelElementId" = None):
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.esmodel_operations_MultiReferenceMoveOperation = esmodel_operations_MultiReferenceMoveOperation
        
        pass
    @property
    def oldIndex(self):
        return self.__oldIndex

    @oldIndex.setter
    def oldIndex(self, oldIndex: int):
        self.__oldIndex = oldIndex


    @property
    def newIndex(self):
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex


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
            if hasattr(old_value, "ModelElementId373"):
                opp_val = getattr(old_value, "ModelElementId373", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId373"):
                opp_val = getattr(value, "ModelElementId373", None)
                setattr(value, "ModelElementId373", self)

class esmodel_operations_AttributeOperation(FeatureOperation):

    def __init__(self, oldValue: str, newValue: str):
        self.oldValue = oldValue
        self.newValue = newValue
        
        pass
    @property
    def oldValue(self):
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue


    @property
    def newValue(self):
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
class ReferenceOperation:

    pass
class esmodel_operations_MultiReferenceOperation(ReferenceOperation):

    def __init__(self, add: bool, index: int, esmodel_operations_MultiReferenceOperation: set["ModelElementId"] = None):
        self.add = add
        self.index = index
        self.esmodel_operations_MultiReferenceOperation = esmodel_operations_MultiReferenceOperation if esmodel_operations_MultiReferenceOperation is not None else set()
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


    @property
    def add(self):
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
                if hasattr(item, "ModelElementId371"):
                    opp_val = getattr(item, "ModelElementId371", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId371", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId371"):
                    opp_val = getattr(item, "ModelElementId371", None)
                    
                    setattr(item, "ModelElementId371", self)
                    

class esmodel_operations_MultiReferenceSetOperation(ReferenceOperation):

    def __init__(self, index: int, esmodel_operations_MultiReferenceSetOperation: "ModelElementId" = None, esmodel_operations_MultiReferenceSetOperation368: "ModelElementId" = None):
        self.index = index
        self.esmodel_operations_MultiReferenceSetOperation = esmodel_operations_MultiReferenceSetOperation
        self.esmodel_operations_MultiReferenceSetOperation368 = esmodel_operations_MultiReferenceSetOperation368
        
        pass
    @property
    def index(self):
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
            if hasattr(old_value, "ModelElementId366"):
                opp_val = getattr(old_value, "ModelElementId366", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId366", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId366"):
                opp_val = getattr(value, "ModelElementId366", None)
                setattr(value, "ModelElementId366", self)

    @property
    def esmodel_operations_MultiReferenceSetOperation368(self):
        return self.__esmodel_operations_MultiReferenceSetOperation368

    @esmodel_operations_MultiReferenceSetOperation368.setter
    def esmodel_operations_MultiReferenceSetOperation368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_MultiReferenceSetOperation__esmodel_operations_MultiReferenceSetOperation368", None)
        self.__esmodel_operations_MultiReferenceSetOperation368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementId369"):
                opp_val = getattr(old_value, "ModelElementId369", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId369", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId369"):
                opp_val = getattr(value, "ModelElementId369", None)
                setattr(value, "ModelElementId369", self)

class esmodel_operations_SingleReferenceOperation(ReferenceOperation):

    pass
class esmodel_operations_MultiAttributeMoveOperation(FeatureOperation):

    def __init__(self, oldIndex: int, newIndex: int, referencedValue: str):
        self.oldIndex = oldIndex
        self.newIndex = newIndex
        self.referencedValue = referencedValue
        
        pass
    @property
    def newIndex(self):
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex


    @property
    def oldIndex(self):
        return self.__oldIndex

    @oldIndex.setter
    def oldIndex(self, oldIndex: int):
        self.__oldIndex = oldIndex


    @property
    def referencedValue(self):
        return self.__referencedValue

    @referencedValue.setter
    def referencedValue(self, referencedValue: str):
        self.__referencedValue = referencedValue


class esmodel_operations_MultiAttributeSetOperation(FeatureOperation):

    def __init__(self, index: int, oldValue: str, newValue: str):
        self.index = index
        self.oldValue = oldValue
        self.newValue = newValue
        
        pass
    @property
    def newValue(self):
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue


    @property
    def oldValue(self):
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


class AbstractOperation:

    pass
class esmodel_operations_CreateDeleteOperation(AbstractOperation):

    def __init__(self, delete: bool, esmodel_operations_CreateDeleteOperation: "operations_esmodel_EObject" = None, esmodel_operations_CreateDeleteOperation357: set["operations_ReferenceOperation"] = None, esmodel_operations_CreateDeleteOperation359: set["operations_EObjectToModelElementIdMap"] = None):
        self.delete = delete
        self.esmodel_operations_CreateDeleteOperation = esmodel_operations_CreateDeleteOperation
        self.esmodel_operations_CreateDeleteOperation357 = esmodel_operations_CreateDeleteOperation357 if esmodel_operations_CreateDeleteOperation357 is not None else set()
        self.esmodel_operations_CreateDeleteOperation359 = esmodel_operations_CreateDeleteOperation359 if esmodel_operations_CreateDeleteOperation359 is not None else set()
        
        pass
    @property
    def delete(self):
        return self.__delete

    @delete.setter
    def delete(self, delete: bool):
        self.__delete = delete


    @property
    def esmodel_operations_CreateDeleteOperation359(self):
        return self.__esmodel_operations_CreateDeleteOperation359

    @esmodel_operations_CreateDeleteOperation359.setter
    def esmodel_operations_CreateDeleteOperation359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CreateDeleteOperation__esmodel_operations_CreateDeleteOperation359", None)
        self.__esmodel_operations_CreateDeleteOperation359 = value if value is not None else set()
        
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
    def esmodel_operations_CreateDeleteOperation357(self):
        return self.__esmodel_operations_CreateDeleteOperation357

    @esmodel_operations_CreateDeleteOperation357.setter
    def esmodel_operations_CreateDeleteOperation357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CreateDeleteOperation__esmodel_operations_CreateDeleteOperation357", None)
        self.__esmodel_operations_CreateDeleteOperation357 = value if value is not None else set()
        
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

class esmodel_operations_CompositeOperation(AbstractOperation):

    def __init__(self, compositeName: str, compositeDescription: str, reversed: bool, esmodel_operations_CompositeOperation: set["operations_AbstractOperation"] = None, esmodel_operations_CompositeOperation353: "operations_AbstractOperation" = None):
        self.compositeName = compositeName
        self.compositeDescription = compositeDescription
        self.reversed = reversed
        self.esmodel_operations_CompositeOperation = esmodel_operations_CompositeOperation if esmodel_operations_CompositeOperation is not None else set()
        self.esmodel_operations_CompositeOperation353 = esmodel_operations_CompositeOperation353
        
        pass
    @property
    def compositeDescription(self):
        return self.__compositeDescription

    @compositeDescription.setter
    def compositeDescription(self, compositeDescription: str):
        self.__compositeDescription = compositeDescription


    @property
    def compositeName(self):
        return self.__compositeName

    @compositeName.setter
    def compositeName(self, compositeName: str):
        self.__compositeName = compositeName


    @property
    def reversed(self):
        return self.__reversed

    @reversed.setter
    def reversed(self, reversed: bool):
        self.__reversed = reversed


    @property
    def esmodel_operations_CompositeOperation353(self):
        return self.__esmodel_operations_CompositeOperation353

    @esmodel_operations_CompositeOperation353.setter
    def esmodel_operations_CompositeOperation353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_operations_CompositeOperation__esmodel_operations_CompositeOperation353", None)
        self.__esmodel_operations_CompositeOperation353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operations_AbstractOperation354"):
                opp_val = getattr(old_value, "operations_AbstractOperation354", None)
                if opp_val == self:
                    setattr(old_value, "operations_AbstractOperation354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operations_AbstractOperation354"):
                opp_val = getattr(value, "operations_AbstractOperation354", None)
                setattr(value, "operations_AbstractOperation354", self)

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
                if hasattr(item, "operations_AbstractOperation351"):
                    opp_val = getattr(item, "operations_AbstractOperation351", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_AbstractOperation351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_AbstractOperation351"):
                    opp_val = getattr(item, "operations_AbstractOperation351", None)
                    
                    setattr(item, "operations_AbstractOperation351", self)
                    

class esmodel_versioning_VersionProperty:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class esmodel_versioning_Version:

    pass
class esmodel_operations_FeatureOperation(AbstractOperation):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


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
class esmodel_versioning_LogMessage:

    def __init__(self, author: str, message: str, date: date, clientDate: date):
        self.author = author
        self.message = message
        self.date = date
        self.clientDate = clientDate
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def clientDate(self):
        return self.__clientDate

    @clientDate.setter
    def clientDate(self, clientDate: date):
        self.__clientDate = clientDate


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


class esmodel_versioning_VersionSpec(ABC):

    pass
class VersionSpec:

    pass
class esmodel_versioning_DateVersionSpec(VersionSpec):

    def __init__(self, date: date):
        self.date = date
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


class esmodel_versioning_PrimaryVersionSpec(VersionSpec):

    def __init__(self, identifier: int):
        self.identifier = identifier
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: int):
        self.__identifier = identifier


class esmodel_versioning_HeadVersionSpec(VersionSpec):

    pass
class esmodel_versioning_TagVersionSpec(VersionSpec):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class WorkItem:

    pass
class model_task_Milestone(WorkItem):

    pass
class model_task_WorkPackage(WorkItem):

    def __init__(self, startDate: date, endDate: date, containingWorkpackage: set["task_WorkItem"] = None):
        self.startDate = startDate
        self.endDate = endDate
        self.containingWorkpackage = containingWorkpackage if containingWorkpackage is not None else set()
        
        pass
    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate


    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate


    @property
    def containingWorkpackage(self):
        return self.__containingWorkpackage

    @containingWorkpackage.setter
    def containingWorkpackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkPackage__containingWorkpackage", None)
        self.__containingWorkpackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem33"):
                    opp_val = getattr(item, "WorkItem33", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem33"):
                    opp_val = getattr(item, "WorkItem33", None)
                    
                    setattr(item, "WorkItem33", self)
                    

class change_ModelChangePackage:

    pass
class task_WorkPackage:

    pass
class organization_OrgUnit:

    pass
class OrgUnit:

    pass
class model_organization_Group(OrgUnit):

    pass
class model_organization_User(OrgUnit):

    def __init__(self, email: str, firstName: str, lastName: str, reviewer: set["task_WorkItem"] = None):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.reviewer = reviewer if reviewer is not None else set()
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def reviewer(self):
        return self.__reviewer

    @reviewer.setter
    def reviewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_User__reviewer", None)
        self.__reviewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem19"):
                    opp_val = getattr(item, "WorkItem19", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem19"):
                    opp_val = getattr(item, "WorkItem19", None)
                    
                    setattr(item, "WorkItem19", self)
                    

class organization_User:

    pass
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
class model_rationale_Solution(UnicaseModelElement, NonDomainElement):

    pass
class model_task_Checkable(UnicaseModelElement):

    def __init__(self, checked: bool, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.checked = checked
        
        pass
    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked


class model_profile_Profile(UnicaseModelElement):

    pass
class model_activity_ActivityObject(UnicaseModelElement):

    pass
class model_requirement_Actor(UnicaseModelElement):

    pass
class model_component_Component(UnicaseModelElement):

    pass
class model_change_ModelChangePackage(UnicaseModelElement):

    def __init__(self, sourceVersion: int, targetVersion: int, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.sourceVersion = sourceVersion
        self.targetVersion = targetVersion
        
        pass
    @property
    def sourceVersion(self):
        return self.__sourceVersion

    @sourceVersion.setter
    def sourceVersion(self, sourceVersion: int):
        self.__sourceVersion = sourceVersion


    @property
    def targetVersion(self):
        return self.__targetVersion

    @targetVersion.setter
    def targetVersion(self, targetVersion: int):
        self.__targetVersion = targetVersion


class model_state_Transition(UnicaseModelElement):

    def __init__(self, condition: str, outgoingTransitions: "state_StateNode" = None, incomingTransitions: "state_StateNode" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.condition = condition
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateNode"):
                opp_val = getattr(old_value, "StateNode", None)
                if opp_val == self:
                    setattr(old_value, "StateNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateNode"):
                opp_val = getattr(value, "StateNode", None)
                setattr(value, "StateNode", self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_state_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateNode243"):
                opp_val = getattr(old_value, "StateNode243", None)
                if opp_val == self:
                    setattr(old_value, "StateNode243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateNode243"):
                opp_val = getattr(value, "StateNode243", None)
                setattr(value, "StateNode243", self)

class model_profile_StereotypeInstance(UnicaseModelElement):

    pass
class model_meeting_MeetingSection(UnicaseModelElement):

    def __init__(self, allocatedTime: int, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.allocatedTime = allocatedTime
        
        pass
    @property
    def allocatedTime(self):
        return self.__allocatedTime

    @allocatedTime.setter
    def allocatedTime(self, allocatedTime: int):
        self.__allocatedTime = allocatedTime


class model_classes_Association(UnicaseModelElement):

    def __init__(self, targetMultiplicity: str, sourceRole: str, targetRole: str, sourceMultiplicity: str, type: str, outgoingAssociations: "classes_Class" = None, incomingAssociations: "classes_Class" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.targetMultiplicity = targetMultiplicity
        self.sourceRole = sourceRole
        self.targetRole = targetRole
        self.sourceMultiplicity = sourceMultiplicity
        self.type = type
        self.outgoingAssociations = outgoingAssociations
        self.incomingAssociations = incomingAssociations
        
        pass
    @property
    def targetMultiplicity(self):
        return self.__targetMultiplicity

    @targetMultiplicity.setter
    def targetMultiplicity(self, targetMultiplicity: str):
        self.__targetMultiplicity = targetMultiplicity


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def sourceRole(self):
        return self.__sourceRole

    @sourceRole.setter
    def sourceRole(self, sourceRole: str):
        self.__sourceRole = sourceRole


    @property
    def targetRole(self):
        return self.__targetRole

    @targetRole.setter
    def targetRole(self, targetRole: str):
        self.__targetRole = targetRole


    @property
    def sourceMultiplicity(self):
        return self.__sourceMultiplicity

    @sourceMultiplicity.setter
    def sourceMultiplicity(self, sourceMultiplicity: str):
        self.__sourceMultiplicity = sourceMultiplicity


    @property
    def incomingAssociations(self):
        return self.__incomingAssociations

    @incomingAssociations.setter
    def incomingAssociations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Association__incomingAssociations", None)
        self.__incomingAssociations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class65"):
                opp_val = getattr(old_value, "Class65", None)
                if opp_val == self:
                    setattr(old_value, "Class65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class65"):
                opp_val = getattr(value, "Class65", None)
                setattr(value, "Class65", self)

    @property
    def outgoingAssociations(self):
        return self.__outgoingAssociations

    @outgoingAssociations.setter
    def outgoingAssociations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Association__outgoingAssociations", None)
        self.__outgoingAssociations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class63"):
                opp_val = getattr(old_value, "Class63", None)
                if opp_val == self:
                    setattr(old_value, "Class63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class63"):
                opp_val = getattr(value, "Class63", None)
                setattr(value, "Class63", self)

class model_profile_StereotypeAttributeInstance(UnicaseModelElement):

    pass
class model_requirement_Workspace(UnicaseModelElement):

    pass
class model_requirement_FunctionalRequirement(UnicaseModelElement):

    def __init__(self, storyPoints: int, priority: int, reviewed: bool, cost: int, refinedRequirement: set["requirement_FunctionalRequirement"] = None, refiningRequirements: "requirement_FunctionalRequirement" = None, model_requirement_FunctionalRequirement: "organization_OrgUnit" = None, functionalRequirements: set["requirement_UseCase"] = None, functionalRequirements94: set["requirement_Scenario"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.storyPoints = storyPoints
        self.priority = priority
        self.reviewed = reviewed
        self.cost = cost
        self.refinedRequirement = refinedRequirement if refinedRequirement is not None else set()
        self.refiningRequirements = refiningRequirements
        self.model_requirement_FunctionalRequirement = model_requirement_FunctionalRequirement
        self.functionalRequirements = functionalRequirements if functionalRequirements is not None else set()
        self.functionalRequirements94 = functionalRequirements94 if functionalRequirements94 is not None else set()
        
        pass
    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost


    @property
    def storyPoints(self):
        return self.__storyPoints

    @storyPoints.setter
    def storyPoints(self, storyPoints: int):
        self.__storyPoints = storyPoints


    @property
    def reviewed(self):
        return self.__reviewed

    @reviewed.setter
    def reviewed(self, reviewed: bool):
        self.__reviewed = reviewed


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


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
    def refinedRequirement(self):
        return self.__refinedRequirement

    @refinedRequirement.setter
    def refinedRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__refinedRequirement", None)
        self.__refinedRequirement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FunctionalRequirement"):
                    opp_val = getattr(item, "FunctionalRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "FunctionalRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FunctionalRequirement"):
                    opp_val = getattr(item, "FunctionalRequirement", None)
                    
                    setattr(item, "FunctionalRequirement", self)
                    

    @property
    def functionalRequirements94(self):
        return self.__functionalRequirements94

    @functionalRequirements94.setter
    def functionalRequirements94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__functionalRequirements94", None)
        self.__functionalRequirements94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Scenario95"):
                    opp_val = getattr(item, "Scenario95", None)
                    
                    if opp_val == self:
                        setattr(item, "Scenario95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Scenario95"):
                    opp_val = getattr(item, "Scenario95", None)
                    
                    setattr(item, "Scenario95", self)
                    

    @property
    def refiningRequirements(self):
        return self.__refiningRequirements

    @refiningRequirements.setter
    def refiningRequirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__refiningRequirements", None)
        self.__refiningRequirements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FunctionalRequirement89"):
                opp_val = getattr(old_value, "FunctionalRequirement89", None)
                if opp_val == self:
                    setattr(old_value, "FunctionalRequirement89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FunctionalRequirement89"):
                opp_val = getattr(value, "FunctionalRequirement89", None)
                setattr(value, "FunctionalRequirement89", self)

    @property
    def functionalRequirements(self):
        return self.__functionalRequirements

    @functionalRequirements.setter
    def functionalRequirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_FunctionalRequirement__functionalRequirements", None)
        self.__functionalRequirements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase92"):
                    opp_val = getattr(item, "UseCase92", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase92"):
                    opp_val = getattr(item, "UseCase92", None)
                    
                    setattr(item, "UseCase92", self)
                    

class model_state_StateNode(UnicaseModelElement):

    pass
class model_profile_StereotypeAttribute(UnicaseModelElement):

    pass
class model_profile_Stereotype(UnicaseModelElement):

    def __init__(self, required: bool, stereotypes: "profile_Profile" = None, stereotype: set["profile_StereotypeInstance"] = None, stereotype256: set["profile_StereotypeAttribute"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.required = required
        self.stereotypes = stereotypes
        self.stereotype = stereotype if stereotype is not None else set()
        self.stereotype256 = stereotype256 if stereotype256 is not None else set()
        
        pass
    @property
    def required(self):
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required


    @property
    def stereotypes(self):
        return self.__stereotypes

    @stereotypes.setter
    def stereotypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__stereotypes", None)
        self.__stereotypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Profile"):
                opp_val = getattr(old_value, "Profile", None)
                if opp_val == self:
                    setattr(old_value, "Profile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Profile"):
                opp_val = getattr(value, "Profile", None)
                setattr(value, "Profile", self)

    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__stereotype", None)
        self.__stereotype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StereotypeInstance254"):
                    opp_val = getattr(item, "StereotypeInstance254", None)
                    
                    if opp_val == self:
                        setattr(item, "StereotypeInstance254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StereotypeInstance254"):
                    opp_val = getattr(item, "StereotypeInstance254", None)
                    
                    setattr(item, "StereotypeInstance254", self)
                    

    @property
    def stereotype256(self):
        return self.__stereotype256

    @stereotype256.setter
    def stereotype256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_profile_Stereotype__stereotype256", None)
        self.__stereotype256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StereotypeAttribute"):
                    opp_val = getattr(item, "StereotypeAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "StereotypeAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StereotypeAttribute"):
                    opp_val = getattr(item, "StereotypeAttribute", None)
                    
                    setattr(item, "StereotypeAttribute", self)
                    

class model_rationale_Criterion(UnicaseModelElement):

    pass
class model_requirement_ActorInstance(UnicaseModelElement):

    pass
class model_requirement_Scenario(UnicaseModelElement):

    pass
class model_Attachment(UnicaseModelElement):

    pass
class model_requirement_UseCase(UnicaseModelElement):

    def __init__(self, precondition: str, postcondition: str, rules: str, exception: str, model_requirement_UseCase: set["requirement_UseCase"] = None, useCases: set["requirement_FunctionalRequirement"] = None, participatedUseCases: set["classes_Class"] = None, model_requirement_UseCase102: set["requirement_UseCase"] = None, instantiatedUseCases: set["requirement_Scenario"] = None, initiatedUseCases: "requirement_Actor" = None, participatedUseCases108: set["requirement_Actor"] = None, useCase: set["requirement_Step"] = None, realizingUseCases: "requirement_UserTask" = None, restrictedUseCases: set["requirement_NonFunctionalRequirement"] = None, usecases: set["requirement_SystemFunction"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.precondition = precondition
        self.postcondition = postcondition
        self.rules = rules
        self.exception = exception
        self.model_requirement_UseCase = model_requirement_UseCase if model_requirement_UseCase is not None else set()
        self.useCases = useCases if useCases is not None else set()
        self.participatedUseCases = participatedUseCases if participatedUseCases is not None else set()
        self.model_requirement_UseCase102 = model_requirement_UseCase102 if model_requirement_UseCase102 is not None else set()
        self.instantiatedUseCases = instantiatedUseCases if instantiatedUseCases is not None else set()
        self.initiatedUseCases = initiatedUseCases
        self.participatedUseCases108 = participatedUseCases108 if participatedUseCases108 is not None else set()
        self.useCase = useCase if useCase is not None else set()
        self.realizingUseCases = realizingUseCases
        self.restrictedUseCases = restrictedUseCases if restrictedUseCases is not None else set()
        self.usecases = usecases if usecases is not None else set()
        
        pass
    @property
    def precondition(self):
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition


    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception


    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules


    @property
    def postcondition(self):
        return self.__postcondition

    @postcondition.setter
    def postcondition(self, postcondition: str):
        self.__postcondition = postcondition


    @property
    def initiatedUseCases(self):
        return self.__initiatedUseCases

    @initiatedUseCases.setter
    def initiatedUseCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__initiatedUseCases", None)
        self.__initiatedUseCases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Actor"):
                opp_val = getattr(old_value, "Actor", None)
                if opp_val == self:
                    setattr(old_value, "Actor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Actor"):
                opp_val = getattr(value, "Actor", None)
                setattr(value, "Actor", self)

    @property
    def restrictedUseCases(self):
        return self.__restrictedUseCases

    @restrictedUseCases.setter
    def restrictedUseCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__restrictedUseCases", None)
        self.__restrictedUseCases = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NonFunctionalRequirement"):
                    opp_val = getattr(item, "NonFunctionalRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "NonFunctionalRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NonFunctionalRequirement"):
                    opp_val = getattr(item, "NonFunctionalRequirement", None)
                    
                    setattr(item, "NonFunctionalRequirement", self)
                    

    @property
    def participatedUseCases108(self):
        return self.__participatedUseCases108

    @participatedUseCases108.setter
    def participatedUseCases108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__participatedUseCases108", None)
        self.__participatedUseCases108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor109"):
                    opp_val = getattr(item, "Actor109", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor109"):
                    opp_val = getattr(item, "Actor109", None)
                    
                    setattr(item, "Actor109", self)
                    

    @property
    def instantiatedUseCases(self):
        return self.__instantiatedUseCases

    @instantiatedUseCases.setter
    def instantiatedUseCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__instantiatedUseCases", None)
        self.__instantiatedUseCases = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Scenario105"):
                    opp_val = getattr(item, "Scenario105", None)
                    
                    if opp_val == self:
                        setattr(item, "Scenario105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Scenario105"):
                    opp_val = getattr(item, "Scenario105", None)
                    
                    setattr(item, "Scenario105", self)
                    

    @property
    def participatedUseCases(self):
        return self.__participatedUseCases

    @participatedUseCases.setter
    def participatedUseCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__participatedUseCases", None)
        self.__participatedUseCases = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class99"):
                    opp_val = getattr(item, "Class99", None)
                    
                    if opp_val == self:
                        setattr(item, "Class99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class99"):
                    opp_val = getattr(item, "Class99", None)
                    
                    setattr(item, "Class99", self)
                    

    @property
    def realizingUseCases(self):
        return self.__realizingUseCases

    @realizingUseCases.setter
    def realizingUseCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__realizingUseCases", None)
        self.__realizingUseCases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserTask"):
                opp_val = getattr(old_value, "UserTask", None)
                if opp_val == self:
                    setattr(old_value, "UserTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserTask"):
                opp_val = getattr(value, "UserTask", None)
                setattr(value, "UserTask", self)

    @property
    def usecases(self):
        return self.__usecases

    @usecases.setter
    def usecases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__usecases", None)
        self.__usecases = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemFunction"):
                    opp_val = getattr(item, "SystemFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemFunction"):
                    opp_val = getattr(item, "SystemFunction", None)
                    
                    setattr(item, "SystemFunction", self)
                    

    @property
    def useCase(self):
        return self.__useCase

    @useCase.setter
    def useCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__useCase", None)
        self.__useCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Step"):
                    opp_val = getattr(item, "Step", None)
                    
                    if opp_val == self:
                        setattr(item, "Step", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Step"):
                    opp_val = getattr(item, "Step", None)
                    
                    setattr(item, "Step", self)
                    

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
    def model_requirement_UseCase102(self):
        return self.__model_requirement_UseCase102

    @model_requirement_UseCase102.setter
    def model_requirement_UseCase102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__model_requirement_UseCase102", None)
        self.__model_requirement_UseCase102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement_UseCase103"):
                    opp_val = getattr(item, "requirement_UseCase103", None)
                    
                    if opp_val == self:
                        setattr(item, "requirement_UseCase103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement_UseCase103"):
                    opp_val = getattr(item, "requirement_UseCase103", None)
                    
                    setattr(item, "requirement_UseCase103", self)
                    

    @property
    def useCases(self):
        return self.__useCases

    @useCases.setter
    def useCases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_UseCase__useCases", None)
        self.__useCases = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FunctionalRequirement97"):
                    opp_val = getattr(item, "FunctionalRequirement97", None)
                    
                    if opp_val == self:
                        setattr(item, "FunctionalRequirement97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FunctionalRequirement97"):
                    opp_val = getattr(item, "FunctionalRequirement97", None)
                    
                    setattr(item, "FunctionalRequirement97", self)
                    

class model_classes_Dependency(UnicaseModelElement):

    pass
class model_rationale_Assessment(UnicaseModelElement, NonDomainElement):

    def __init__(self, value: int, assessments: "rationale_Proposal" = None, assessments195: "rationale_Criterion" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.value = value
        self.assessments = assessments
        self.assessments195 = assessments195
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def assessments195(self):
        return self.__assessments195

    @assessments195.setter
    def assessments195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Assessment__assessments195", None)
        self.__assessments195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Criterion"):
                opp_val = getattr(old_value, "Criterion", None)
                if opp_val == self:
                    setattr(old_value, "Criterion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Criterion"):
                opp_val = getattr(value, "Criterion", None)
                setattr(value, "Criterion", self)

    @property
    def assessments(self):
        return self.__assessments

    @assessments.setter
    def assessments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Assessment__assessments", None)
        self.__assessments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Proposal193"):
                opp_val = getattr(old_value, "Proposal193", None)
                if opp_val == self:
                    setattr(old_value, "Proposal193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Proposal193"):
                opp_val = getattr(value, "Proposal193", None)
                setattr(value, "Proposal193", self)

class model_requirement_Step(UnicaseModelElement, NonDomainElement):

    def __init__(self, userStep: bool, model_requirement_Step: "requirement_UseCase" = None, useCaseSteps: "requirement_UseCase" = None, model_requirement_Step153: "requirement_SystemFunction" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.userStep = userStep
        self.model_requirement_Step = model_requirement_Step
        self.useCaseSteps = useCaseSteps
        self.model_requirement_Step153 = model_requirement_Step153
        
        pass
    @property
    def userStep(self):
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
            if hasattr(old_value, "requirement_UseCase149"):
                opp_val = getattr(old_value, "requirement_UseCase149", None)
                if opp_val == self:
                    setattr(old_value, "requirement_UseCase149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement_UseCase149"):
                opp_val = getattr(value, "requirement_UseCase149", None)
                setattr(value, "requirement_UseCase149", self)

    @property
    def useCaseSteps(self):
        return self.__useCaseSteps

    @useCaseSteps.setter
    def useCaseSteps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_Step__useCaseSteps", None)
        self.__useCaseSteps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase151"):
                opp_val = getattr(old_value, "UseCase151", None)
                if opp_val == self:
                    setattr(old_value, "UseCase151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase151"):
                opp_val = getattr(value, "UseCase151", None)
                setattr(value, "UseCase151", self)

    @property
    def model_requirement_Step153(self):
        return self.__model_requirement_Step153

    @model_requirement_Step153.setter
    def model_requirement_Step153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_Step__model_requirement_Step153", None)
        self.__model_requirement_Step153 = value
        
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

class model_classes_PackageElement(UnicaseModelElement):

    pass
class model_activity_Transition(UnicaseModelElement):

    def __init__(self, condition: str, outgoingTransitions285: "activity_ActivityObject" = None, incomingTransitions287: "activity_ActivityObject" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.condition = condition
        self.outgoingTransitions285 = outgoingTransitions285
        self.incomingTransitions287 = incomingTransitions287
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def incomingTransitions287(self):
        return self.__incomingTransitions287

    @incomingTransitions287.setter
    def incomingTransitions287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_activity_Transition__incomingTransitions287", None)
        self.__incomingTransitions287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityObject288"):
                opp_val = getattr(old_value, "ActivityObject288", None)
                if opp_val == self:
                    setattr(old_value, "ActivityObject288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityObject288"):
                opp_val = getattr(value, "ActivityObject288", None)
                setattr(value, "ActivityObject288", self)

    @property
    def outgoingTransitions285(self):
        return self.__outgoingTransitions285

    @outgoingTransitions285.setter
    def outgoingTransitions285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_activity_Transition__outgoingTransitions285", None)
        self.__outgoingTransitions285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityObject"):
                opp_val = getattr(old_value, "ActivityObject", None)
                if opp_val == self:
                    setattr(old_value, "ActivityObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityObject"):
                opp_val = getattr(value, "ActivityObject", None)
                setattr(value, "ActivityObject", self)

class model_classes_Attribute(UnicaseModelElement):

    def __init__(self, signature: str, type: str, defaultValue: str, properties: str, label: str, visibility: str, scope: str, attributes: "classes_Class" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.signature = signature
        self.type = type
        self.defaultValue = defaultValue
        self.properties = properties
        self.label = label
        self.visibility = visibility
        self.scope = scope
        self.attributes = attributes
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class67"):
                opp_val = getattr(old_value, "Class67", None)
                if opp_val == self:
                    setattr(old_value, "Class67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class67"):
                opp_val = getattr(value, "Class67", None)
                setattr(value, "Class67", self)

class model_organization_OrgUnit(UnicaseModelElement):

    def __init__(self, acOrgId: str, participants: set["task_WorkItem"] = None, assignee: set["task_WorkItem"] = None, orgUnits: set["organization_Group"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.acOrgId = acOrgId
        self.participants = participants if participants is not None else set()
        self.assignee = assignee if assignee is not None else set()
        self.orgUnits = orgUnits if orgUnits is not None else set()
        
        pass
    @property
    def acOrgId(self):
        return self.__acOrgId

    @acOrgId.setter
    def acOrgId(self, acOrgId: str):
        self.__acOrgId = acOrgId


    @property
    def orgUnits(self):
        return self.__orgUnits

    @orgUnits.setter
    def orgUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__orgUnits", None)
        self.__orgUnits = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__participants", None)
        self.__participants = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem"):
                    opp_val = getattr(item, "WorkItem", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem"):
                    opp_val = getattr(item, "WorkItem", None)
                    
                    setattr(item, "WorkItem", self)
                    

    @property
    def assignee(self):
        return self.__assignee

    @assignee.setter
    def assignee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_organization_OrgUnit__assignee", None)
        self.__assignee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem17"):
                    opp_val = getattr(item, "WorkItem17", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem17"):
                    opp_val = getattr(item, "WorkItem17", None)
                    
                    setattr(item, "WorkItem17", self)
                    

class model_meeting_Meeting(UnicaseModelElement):

    def __init__(self, location: str, starttime: date, endtime: date, model_meeting_Meeting: "organization_User" = None, model_meeting_Meeting223: "organization_User" = None, model_meeting_Meeting226: "organization_User" = None, model_meeting_Meeting229: set["organization_OrgUnit"] = None, model_meeting_Meeting232: set["meeting_MeetingSection"] = None, model_meeting_Meeting234: "meeting_IssueMeetingSection" = None, model_meeting_Meeting236: "meeting_WorkItemMeetingSection" = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.location = location
        self.starttime = starttime
        self.endtime = endtime
        self.model_meeting_Meeting = model_meeting_Meeting
        self.model_meeting_Meeting223 = model_meeting_Meeting223
        self.model_meeting_Meeting226 = model_meeting_Meeting226
        self.model_meeting_Meeting229 = model_meeting_Meeting229 if model_meeting_Meeting229 is not None else set()
        self.model_meeting_Meeting232 = model_meeting_Meeting232 if model_meeting_Meeting232 is not None else set()
        self.model_meeting_Meeting234 = model_meeting_Meeting234
        self.model_meeting_Meeting236 = model_meeting_Meeting236
        
        pass
    @property
    def starttime(self):
        return self.__starttime

    @starttime.setter
    def starttime(self, starttime: date):
        self.__starttime = starttime


    @property
    def endtime(self):
        return self.__endtime

    @endtime.setter
    def endtime(self, endtime: date):
        self.__endtime = endtime


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def model_meeting_Meeting229(self):
        return self.__model_meeting_Meeting229

    @model_meeting_Meeting229.setter
    def model_meeting_Meeting229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting229", None)
        self.__model_meeting_Meeting229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organization_OrgUnit230"):
                    opp_val = getattr(item, "organization_OrgUnit230", None)
                    
                    if opp_val == self:
                        setattr(item, "organization_OrgUnit230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organization_OrgUnit230"):
                    opp_val = getattr(item, "organization_OrgUnit230", None)
                    
                    setattr(item, "organization_OrgUnit230", self)
                    

    @property
    def model_meeting_Meeting234(self):
        return self.__model_meeting_Meeting234

    @model_meeting_Meeting234.setter
    def model_meeting_Meeting234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting234", None)
        self.__model_meeting_Meeting234 = value
        
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
    def model_meeting_Meeting236(self):
        return self.__model_meeting_Meeting236

    @model_meeting_Meeting236.setter
    def model_meeting_Meeting236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting236", None)
        self.__model_meeting_Meeting236 = value
        
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
    def model_meeting_Meeting226(self):
        return self.__model_meeting_Meeting226

    @model_meeting_Meeting226.setter
    def model_meeting_Meeting226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting226", None)
        self.__model_meeting_Meeting226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_User227"):
                opp_val = getattr(old_value, "organization_User227", None)
                if opp_val == self:
                    setattr(old_value, "organization_User227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_User227"):
                opp_val = getattr(value, "organization_User227", None)
                setattr(value, "organization_User227", self)

    @property
    def model_meeting_Meeting223(self):
        return self.__model_meeting_Meeting223

    @model_meeting_Meeting223.setter
    def model_meeting_Meeting223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting223", None)
        self.__model_meeting_Meeting223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organization_User224"):
                opp_val = getattr(old_value, "organization_User224", None)
                if opp_val == self:
                    setattr(old_value, "organization_User224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organization_User224"):
                opp_val = getattr(value, "organization_User224", None)
                setattr(value, "organization_User224", self)

    @property
    def model_meeting_Meeting232(self):
        return self.__model_meeting_Meeting232

    @model_meeting_Meeting232.setter
    def model_meeting_Meeting232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_meeting_Meeting__model_meeting_Meeting232", None)
        self.__model_meeting_Meeting232 = value if value is not None else set()
        
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
                    

class model_rationale_Proposal(UnicaseModelElement, NonDomainElement):

    pass
class model_document_Section(UnicaseModelElement):

    pass
class model_classes_MethodArgument(UnicaseModelElement):

    def __init__(self, signature: str, label: str, direction: str, type: str, defaultValue: str, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.signature = signature
        self.label = label
        self.direction = direction
        self.type = type
        self.defaultValue = defaultValue
        
        pass
    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


class model_rationale_Comment(UnicaseModelElement, NonDomainElement):

    pass
class model_requirement_SystemFunction(UnicaseModelElement):

    def __init__(self, input: str, output: str, exception: str, systemFunctions160: "requirement_Workspace" = None, systemFunctions: "requirement_NonFunctionalRequirement" = None, systemFunctions157: set["requirement_UseCase"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.input = input
        self.output = output
        self.exception = exception
        self.systemFunctions160 = systemFunctions160
        self.systemFunctions = systemFunctions
        self.systemFunctions157 = systemFunctions157 if systemFunctions157 is not None else set()
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, exception: str):
        self.__exception = exception


    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output


    @property
    def systemFunctions157(self):
        return self.__systemFunctions157

    @systemFunctions157.setter
    def systemFunctions157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__systemFunctions157", None)
        self.__systemFunctions157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UseCase158"):
                    opp_val = getattr(item, "UseCase158", None)
                    
                    if opp_val == self:
                        setattr(item, "UseCase158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UseCase158"):
                    opp_val = getattr(item, "UseCase158", None)
                    
                    setattr(item, "UseCase158", self)
                    

    @property
    def systemFunctions160(self):
        return self.__systemFunctions160

    @systemFunctions160.setter
    def systemFunctions160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__systemFunctions160", None)
        self.__systemFunctions160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workspace"):
                opp_val = getattr(old_value, "Workspace", None)
                if opp_val == self:
                    setattr(old_value, "Workspace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workspace"):
                opp_val = getattr(value, "Workspace", None)
                setattr(value, "Workspace", self)

    @property
    def systemFunctions(self):
        return self.__systemFunctions

    @systemFunctions.setter
    def systemFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_requirement_SystemFunction__systemFunctions", None)
        self.__systemFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NonFunctionalRequirement155"):
                opp_val = getattr(old_value, "NonFunctionalRequirement155", None)
                if opp_val == self:
                    setattr(old_value, "NonFunctionalRequirement155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NonFunctionalRequirement155"):
                opp_val = getattr(value, "NonFunctionalRequirement155", None)
                setattr(value, "NonFunctionalRequirement155", self)

class model_component_ComponentService(UnicaseModelElement):

    pass
class model_classes_Method(UnicaseModelElement):

    def __init__(self, visibility: str, scope: str, returnType: str, signature: str, properties: str, label: str, stubbed: bool, methods: "classes_Class" = None, callingMethods: set["classes_Method"] = None, calledMethods: set["classes_Method"] = None, model_classes_Method: set["classes_MethodArgument"] = None, participatingMethods: set["requirement_Scenario"] = None, UnicaseModelElement250: "model_profile_Profile" = None, UnicaseModelElement83: "model_document_LeafSection" = None, UnicaseModelElement42: "model_diagram_MEDiagram" = None, UnicaseModelElement202: "model_rationale_Comment" = None, UnicaseModelElement: "model_Annotation" = None, UnicaseModelElement260: "model_profile_StereotypeInstance" = None, UnicaseModelElement85: "model_document_LeafSection" = None, UnicaseModelElement13: "model_Attachment" = None, UnicaseModelElement35: "model_task_Milestone" = None, UnicaseModelElement37: "model_diagram_MEDiagram" = None):
        self.visibility = visibility
        self.scope = scope
        self.returnType = returnType
        self.signature = signature
        self.properties = properties
        self.label = label
        self.stubbed = stubbed
        self.methods = methods
        self.callingMethods = callingMethods if callingMethods is not None else set()
        self.calledMethods = calledMethods if calledMethods is not None else set()
        self.model_classes_Method = model_classes_Method if model_classes_Method is not None else set()
        self.participatingMethods = participatingMethods if participatingMethods is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType


    @property
    def signature(self):
        return self.__signature

    @signature.setter
    def signature(self, signature: str):
        self.__signature = signature


    @property
    def stubbed(self):
        return self.__stubbed

    @stubbed.setter
    def stubbed(self, stubbed: bool):
        self.__stubbed = stubbed


    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class69"):
                opp_val = getattr(old_value, "Class69", None)
                if opp_val == self:
                    setattr(old_value, "Class69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class69"):
                opp_val = getattr(value, "Class69", None)
                setattr(value, "Class69", self)

    @property
    def participatingMethods(self):
        return self.__participatingMethods

    @participatingMethods.setter
    def participatingMethods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__participatingMethods", None)
        self.__participatingMethods = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Scenario76"):
                    opp_val = getattr(item, "Scenario76", None)
                    
                    if opp_val == self:
                        setattr(item, "Scenario76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Scenario76"):
                    opp_val = getattr(item, "Scenario76", None)
                    
                    setattr(item, "Scenario76", self)
                    

    @property
    def calledMethods(self):
        return self.__calledMethods

    @calledMethods.setter
    def calledMethods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__calledMethods", None)
        self.__calledMethods = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method73"):
                    opp_val = getattr(item, "Method73", None)
                    
                    if opp_val == self:
                        setattr(item, "Method73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method73"):
                    opp_val = getattr(item, "Method73", None)
                    
                    setattr(item, "Method73", self)
                    

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
    def callingMethods(self):
        return self.__callingMethods

    @callingMethods.setter
    def callingMethods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_classes_Method__callingMethods", None)
        self.__callingMethods = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method71"):
                    opp_val = getattr(item, "Method71", None)
                    
                    if opp_val == self:
                        setattr(item, "Method71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method71"):
                    opp_val = getattr(item, "Method71", None)
                    
                    setattr(item, "Method71", self)
                    

class model_component_DeploymentNode(UnicaseModelElement):

    pass
class model_requirement_UserTask(UnicaseModelElement):

    pass
class model_Annotation(UnicaseModelElement):

    pass
class profile_StereotypeInstance:

    pass
class rationale_Comment:

    pass
class document_LeafSection:

    pass
class Attachment:

    pass
class model_diagram_MEDiagram(Attachment):

    def __init__(self, diagramLayout: str, type: str, model_diagram_MEDiagram: set["UnicaseModelElement"] = None, model_diagram_MEDiagram39: "diagram_model_Diagram" = None, model_diagram_MEDiagram41: set["UnicaseModelElement"] = None, Attachment: "model_UnicaseModelElement" = None):
        self.diagramLayout = diagramLayout
        self.type = type
        self.model_diagram_MEDiagram = model_diagram_MEDiagram if model_diagram_MEDiagram is not None else set()
        self.model_diagram_MEDiagram39 = model_diagram_MEDiagram39
        self.model_diagram_MEDiagram41 = model_diagram_MEDiagram41 if model_diagram_MEDiagram41 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def diagramLayout(self):
        return self.__diagramLayout

    @diagramLayout.setter
    def diagramLayout(self, diagramLayout: str):
        self.__diagramLayout = diagramLayout


    @property
    def model_diagram_MEDiagram41(self):
        return self.__model_diagram_MEDiagram41

    @model_diagram_MEDiagram41.setter
    def model_diagram_MEDiagram41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_diagram_MEDiagram__model_diagram_MEDiagram41", None)
        self.__model_diagram_MEDiagram41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnicaseModelElement42"):
                    opp_val = getattr(item, "UnicaseModelElement42", None)
                    
                    if opp_val == self:
                        setattr(item, "UnicaseModelElement42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnicaseModelElement42"):
                    opp_val = getattr(item, "UnicaseModelElement42", None)
                    
                    setattr(item, "UnicaseModelElement42", self)
                    

    @property
    def model_diagram_MEDiagram39(self):
        return self.__model_diagram_MEDiagram39

    @model_diagram_MEDiagram39.setter
    def model_diagram_MEDiagram39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_diagram_MEDiagram__model_diagram_MEDiagram39", None)
        self.__model_diagram_MEDiagram39 = value
        
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
                if hasattr(item, "UnicaseModelElement37"):
                    opp_val = getattr(item, "UnicaseModelElement37", None)
                    
                    if opp_val == self:
                        setattr(item, "UnicaseModelElement37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnicaseModelElement37"):
                    opp_val = getattr(item, "UnicaseModelElement37", None)
                    
                    setattr(item, "UnicaseModelElement37", self)
                    

class model_attachment_FileAttachment(Attachment):

    def __init__(self, fileName: str, fileHash: str, fileID: str, fileSize: str, requiredOffline: bool, fileType: str, uploading: bool, downloading: bool, Attachment: "model_UnicaseModelElement" = None):
        self.fileName = fileName
        self.fileHash = fileHash
        self.fileID = fileID
        self.fileSize = fileSize
        self.requiredOffline = requiredOffline
        self.fileType = fileType
        self.uploading = uploading
        self.downloading = downloading
        
        pass
    @property
    def downloading(self):
        return self.__downloading

    @downloading.setter
    def downloading(self, downloading: bool):
        self.__downloading = downloading


    @property
    def fileType(self):
        return self.__fileType

    @fileType.setter
    def fileType(self, fileType: str):
        self.__fileType = fileType


    @property
    def uploading(self):
        return self.__uploading

    @uploading.setter
    def uploading(self, uploading: bool):
        self.__uploading = uploading


    @property
    def fileSize(self):
        return self.__fileSize

    @fileSize.setter
    def fileSize(self, fileSize: str):
        self.__fileSize = fileSize


    @property
    def fileID(self):
        return self.__fileID

    @fileID.setter
    def fileID(self, fileID: str):
        self.__fileID = fileID


    @property
    def fileHash(self):
        return self.__fileHash

    @fileHash.setter
    def fileHash(self, fileHash: str):
        self.__fileHash = fileHash


    @property
    def requiredOffline(self):
        return self.__requiredOffline

    @requiredOffline.setter
    def requiredOffline(self, requiredOffline: bool):
        self.__requiredOffline = requiredOffline


    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName


class model_attachment_UrlAttachment(Attachment):

    def __init__(self, url: str, Attachment: "model_UnicaseModelElement" = None):
        self.url = url
        
        pass
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


class task_WorkItem:

    pass
class model_task_ActionItem(task_WorkItem, task_Checkable):

    def __init__(self, done: bool, activity: str, WorkItem: "model_organization_OrgUnit" = None, WorkItem25: "model_task_WorkItem" = None, WorkItem23: "model_task_WorkItem" = None, WorkItem33: "model_task_WorkPackage" = None, task_WorkItem: "model_meeting_WorkItemMeetingSection" = None, WorkItem17: "model_organization_OrgUnit" = None, WorkItem19: "model_organization_User" = None):
        self.done = done
        self.activity = activity
        
        pass
    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity


    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done: bool):
        self.__done = done


class model_bug_BugReport(task_WorkItem, task_Checkable):

    def __init__(self, resolution: str, severity: str, resolutionType: str, done: bool, WorkItem: "model_organization_OrgUnit" = None, WorkItem25: "model_task_WorkItem" = None, WorkItem23: "model_task_WorkItem" = None, WorkItem33: "model_task_WorkPackage" = None, task_WorkItem: "model_meeting_WorkItemMeetingSection" = None, WorkItem17: "model_organization_OrgUnit" = None, WorkItem19: "model_organization_User" = None):
        self.resolution = resolution
        self.severity = severity
        self.resolutionType = resolutionType
        self.done = done
        
        pass
    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done: bool):
        self.__done = done


    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution


    @property
    def resolutionType(self):
        return self.__resolutionType

    @resolutionType.setter
    def resolutionType(self, resolutionType: str):
        self.__resolutionType = resolutionType


class metamodel_AssociationClassElement(ABC):

    pass
class metamodel_NonDomainElement(ABC):

    pass
class metamodel_ModelVersion:

    def __init__(self, releaseNumber: int):
        self.releaseNumber = releaseNumber
        
        pass
    @property
    def releaseNumber(self):
        return self.__releaseNumber

    @releaseNumber.setter
    def releaseNumber(self, releaseNumber: int):
        self.__releaseNumber = releaseNumber


class UniqueIdentifier:

    pass
class esmodel_SessionId(UniqueIdentifier):

    pass
class esmodel_operations_OperationId(UniqueIdentifier):

    pass
class esmodel_accesscontrol_ACOrgUnitId(UniqueIdentifier):

    pass
class esmodel_ProjectId(UniqueIdentifier):

    pass
class metamodel_ModelElementId(UniqueIdentifier):

    pass
class IdentifiableElement:

    pass
class esmodel_FileIdentifier(IdentifiableElement):

    pass
class esmodel_operations_AbstractOperation(IdentifiableElement):

    def __init__(self, name: str, description: str, accepted: bool, clientDate: date, esmodel_operations_AbstractOperation: "ModelElementId" = None):
        self.name = name
        self.description = description
        self.accepted = accepted
        self.clientDate = clientDate
        self.esmodel_operations_AbstractOperation = esmodel_operations_AbstractOperation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def clientDate(self):
        return self.__clientDate

    @clientDate.setter
    def clientDate(self, clientDate: date):
        self.__clientDate = clientDate


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def accepted(self):
        return self.__accepted

    @accepted.setter
    def accepted(self, accepted: bool):
        self.__accepted = accepted


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
            if hasattr(old_value, "ModelElementId349"):
                opp_val = getattr(old_value, "ModelElementId349", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementId349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementId349"):
                opp_val = getattr(value, "ModelElementId349", None)
                setattr(value, "ModelElementId349", self)

class esmodel_accesscontrol_ACOrgUnit(IdentifiableElement):

    def __init__(self, description: str, name: str, esmodel_accesscontrol_ACOrgUnit460: set["accesscontrol_OrgUnitProperty"] = None, esmodel_accesscontrol_ACOrgUnit: set["roles_Role"] = None):
        self.description = description
        self.name = name
        self.esmodel_accesscontrol_ACOrgUnit460 = esmodel_accesscontrol_ACOrgUnit460 if esmodel_accesscontrol_ACOrgUnit460 is not None else set()
        self.esmodel_accesscontrol_ACOrgUnit = esmodel_accesscontrol_ACOrgUnit if esmodel_accesscontrol_ACOrgUnit is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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
                    

    @property
    def esmodel_accesscontrol_ACOrgUnit460(self):
        return self.__esmodel_accesscontrol_ACOrgUnit460

    @esmodel_accesscontrol_ACOrgUnit460.setter
    def esmodel_accesscontrol_ACOrgUnit460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_accesscontrol_ACOrgUnit__esmodel_accesscontrol_ACOrgUnit460", None)
        self.__esmodel_accesscontrol_ACOrgUnit460 = value if value is not None else set()
        
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
                    

    def getId(self) :
        # TODO: Implement getId method
        pass

class esmodel_notification_ESNotification(IdentifiableElement):

    def __init__(self, name: str, message: str, details: str, seen: bool, creationDate: date, provider: str, sender: str, recipient: str, esmodel_notification_ESNotification469: set["ModelElementId"] = None, esmodel_notification_ESNotification472: set["operations_OperationId"] = None, esmodel_notification_ESNotification: "ProjectId" = None):
        self.name = name
        self.message = message
        self.details = details
        self.seen = seen
        self.creationDate = creationDate
        self.provider = provider
        self.sender = sender
        self.recipient = recipient
        self.esmodel_notification_ESNotification469 = esmodel_notification_ESNotification469 if esmodel_notification_ESNotification469 is not None else set()
        self.esmodel_notification_ESNotification472 = esmodel_notification_ESNotification472 if esmodel_notification_ESNotification472 is not None else set()
        self.esmodel_notification_ESNotification = esmodel_notification_ESNotification
        
        pass
    @property
    def seen(self):
        return self.__seen

    @seen.setter
    def seen(self, seen: bool):
        self.__seen = seen


    @property
    def creationDate(self):
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate


    @property
    def recipient(self):
        return self.__recipient

    @recipient.setter
    def recipient(self, recipient: str):
        self.__recipient = recipient


    @property
    def details(self):
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sender(self):
        return self.__sender

    @sender.setter
    def sender(self, sender: str):
        self.__sender = sender


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider


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
            if hasattr(old_value, "ProjectId467"):
                opp_val = getattr(old_value, "ProjectId467", None)
                if opp_val == self:
                    setattr(old_value, "ProjectId467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectId467"):
                opp_val = getattr(value, "ProjectId467", None)
                setattr(value, "ProjectId467", self)

    @property
    def esmodel_notification_ESNotification472(self):
        return self.__esmodel_notification_ESNotification472

    @esmodel_notification_ESNotification472.setter
    def esmodel_notification_ESNotification472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_notification_ESNotification__esmodel_notification_ESNotification472", None)
        self.__esmodel_notification_ESNotification472 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operations_OperationId473"):
                    opp_val = getattr(item, "operations_OperationId473", None)
                    
                    if opp_val == self:
                        setattr(item, "operations_OperationId473", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operations_OperationId473"):
                    opp_val = getattr(item, "operations_OperationId473", None)
                    
                    setattr(item, "operations_OperationId473", self)
                    

    @property
    def esmodel_notification_ESNotification469(self):
        return self.__esmodel_notification_ESNotification469

    @esmodel_notification_ESNotification469.setter
    def esmodel_notification_ESNotification469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esmodel_notification_ESNotification__esmodel_notification_ESNotification469", None)
        self.__esmodel_notification_ESNotification469 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElementId470"):
                    opp_val = getattr(item, "ModelElementId470", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElementId470", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElementId470"):
                    opp_val = getattr(item, "ModelElementId470", None)
                    
                    setattr(item, "ModelElementId470", self)
                    

class metamodel_ModelElement(IdentifiableElement):

    def __init__(self, creator: str, creationDate: date):
        self.creator = creator
        self.creationDate = creationDate
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate


    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator


class metamodel_IdentifiableElement(ABC):

    def __init__(self, identifier: str):
        self.identifier = identifier
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class metamodel_UniqueIdentifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class ModelElement:

    pass
class model_UnicaseModelElement(ModelElement):

    def __init__(self, state: str, name: str, description: str, annotatedModelElements: set["Annotation"] = None, referringModelElements: set["Attachment"] = None, modelElements: "document_LeafSection" = None, referencedModelElements: set["document_LeafSection"] = None, commentedElement: set["rationale_Comment"] = None, modelElement: set["profile_StereotypeInstance"] = None, ModelElement: "metamodel_Project" = None, ModelElement3: "metamodel_Project" = None):
        self.state = state
        self.name = name
        self.description = description
        self.annotatedModelElements = annotatedModelElements if annotatedModelElements is not None else set()
        self.referringModelElements = referringModelElements if referringModelElements is not None else set()
        self.modelElements = modelElements
        self.referencedModelElements = referencedModelElements if referencedModelElements is not None else set()
        self.commentedElement = commentedElement if commentedElement is not None else set()
        self.modelElement = modelElement if modelElement is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def referringModelElements(self):
        return self.__referringModelElements

    @referringModelElements.setter
    def referringModelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__referringModelElements", None)
        self.__referringModelElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attachment"):
                    opp_val = getattr(item, "Attachment", None)
                    
                    if opp_val == self:
                        setattr(item, "Attachment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attachment"):
                    opp_val = getattr(item, "Attachment", None)
                    
                    setattr(item, "Attachment", self)
                    

    @property
    def modelElements(self):
        return self.__modelElements

    @modelElements.setter
    def modelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__modelElements", None)
        self.__modelElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LeafSection"):
                opp_val = getattr(old_value, "LeafSection", None)
                if opp_val == self:
                    setattr(old_value, "LeafSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LeafSection"):
                opp_val = getattr(value, "LeafSection", None)
                setattr(value, "LeafSection", self)

    @property
    def modelElement(self):
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__modelElement", None)
        self.__modelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StereotypeInstance"):
                    opp_val = getattr(item, "StereotypeInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "StereotypeInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StereotypeInstance"):
                    opp_val = getattr(item, "StereotypeInstance", None)
                    
                    setattr(item, "StereotypeInstance", self)
                    

    @property
    def referencedModelElements(self):
        return self.__referencedModelElements

    @referencedModelElements.setter
    def referencedModelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__referencedModelElements", None)
        self.__referencedModelElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LeafSection8"):
                    opp_val = getattr(item, "LeafSection8", None)
                    
                    if opp_val == self:
                        setattr(item, "LeafSection8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LeafSection8"):
                    opp_val = getattr(item, "LeafSection8", None)
                    
                    setattr(item, "LeafSection8", self)
                    

    @property
    def annotatedModelElements(self):
        return self.__annotatedModelElements

    @annotatedModelElements.setter
    def annotatedModelElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__annotatedModelElements", None)
        self.__annotatedModelElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    setattr(item, "Annotation", self)
                    

    @property
    def commentedElement(self):
        return self.__commentedElement

    @commentedElement.setter
    def commentedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_UnicaseModelElement__commentedElement", None)
        self.__commentedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

class metamodel_Project:

    pass
class Annotation:

    pass
class model_rationale_Issue(task_WorkItem, task_Checkable, Annotation):

    def __init__(self, activity: str, issue: set["rationale_Proposal"] = None, issue183: "rationale_Solution" = None, model_rationale_Issue: set["rationale_Criterion"] = None, Annotation: "model_UnicaseModelElement" = None, WorkItem: "model_organization_OrgUnit" = None, WorkItem25: "model_task_WorkItem" = None, WorkItem23: "model_task_WorkItem" = None, WorkItem33: "model_task_WorkPackage" = None, task_WorkItem: "model_meeting_WorkItemMeetingSection" = None, WorkItem17: "model_organization_OrgUnit" = None, WorkItem19: "model_organization_User" = None):
        self.activity = activity
        self.issue = issue if issue is not None else set()
        self.issue183 = issue183
        self.model_rationale_Issue = model_rationale_Issue if model_rationale_Issue is not None else set()
        
        pass
    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity


    @property
    def issue183(self):
        return self.__issue183

    @issue183.setter
    def issue183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Issue__issue183", None)
        self.__issue183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Solution"):
                opp_val = getattr(old_value, "Solution", None)
                if opp_val == self:
                    setattr(old_value, "Solution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Solution"):
                opp_val = getattr(value, "Solution", None)
                setattr(value, "Solution", self)

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
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_rationale_Issue__issue", None)
        self.__issue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Proposal"):
                    opp_val = getattr(item, "Proposal", None)
                    
                    if opp_val == self:
                        setattr(item, "Proposal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Proposal"):
                    opp_val = getattr(item, "Proposal", None)
                    
                    setattr(item, "Proposal", self)
                    

class model_task_WorkItem(Annotation):

    def __init__(self, dueDate: date, estimate: int, effort: int, priority: int, resolved: bool, workItemsToReview: "organization_User" = None, participations: set["organization_OrgUnit"] = None, containedWorkItems: "task_WorkPackage" = None, predecessors: set["task_WorkItem"] = None, successors: set["task_WorkItem"] = None, assignments: "organization_OrgUnit" = None, model_task_WorkItem: set["change_ModelChangePackage"] = None, Annotation: "model_UnicaseModelElement" = None):
        self.dueDate = dueDate
        self.estimate = estimate
        self.effort = effort
        self.priority = priority
        self.resolved = resolved
        self.workItemsToReview = workItemsToReview
        self.participations = participations if participations is not None else set()
        self.containedWorkItems = containedWorkItems
        self.predecessors = predecessors if predecessors is not None else set()
        self.successors = successors if successors is not None else set()
        self.assignments = assignments
        self.model_task_WorkItem = model_task_WorkItem if model_task_WorkItem is not None else set()
        
        pass
    @property
    def effort(self):
        return self.__effort

    @effort.setter
    def effort(self, effort: int):
        self.__effort = effort


    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate: date):
        self.__dueDate = dueDate


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def resolved(self):
        return self.__resolved

    @resolved.setter
    def resolved(self, resolved: bool):
        self.__resolved = resolved


    @property
    def estimate(self):
        return self.__estimate

    @estimate.setter
    def estimate(self, estimate: int):
        self.__estimate = estimate


    @property
    def workItemsToReview(self):
        return self.__workItemsToReview

    @workItemsToReview.setter
    def workItemsToReview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__workItemsToReview", None)
        self.__workItemsToReview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User"):
                opp_val = getattr(old_value, "User", None)
                if opp_val == self:
                    setattr(old_value, "User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User"):
                opp_val = getattr(value, "User", None)
                setattr(value, "User", self)

    @property
    def assignments(self):
        return self.__assignments

    @assignments.setter
    def assignments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__assignments", None)
        self.__assignments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrgUnit27"):
                opp_val = getattr(old_value, "OrgUnit27", None)
                if opp_val == self:
                    setattr(old_value, "OrgUnit27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrgUnit27"):
                opp_val = getattr(value, "OrgUnit27", None)
                setattr(value, "OrgUnit27", self)

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
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__predecessors", None)
        self.__predecessors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem23"):
                    opp_val = getattr(item, "WorkItem23", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem23"):
                    opp_val = getattr(item, "WorkItem23", None)
                    
                    setattr(item, "WorkItem23", self)
                    

    @property
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__successors", None)
        self.__successors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkItem25"):
                    opp_val = getattr(item, "WorkItem25", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkItem25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkItem25"):
                    opp_val = getattr(item, "WorkItem25", None)
                    
                    setattr(item, "WorkItem25", self)
                    

    @property
    def containedWorkItems(self):
        return self.__containedWorkItems

    @containedWorkItems.setter
    def containedWorkItems(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__containedWorkItems", None)
        self.__containedWorkItems = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkPackage"):
                opp_val = getattr(old_value, "WorkPackage", None)
                if opp_val == self:
                    setattr(old_value, "WorkPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkPackage"):
                opp_val = getattr(value, "WorkPackage", None)
                setattr(value, "WorkPackage", self)

    @property
    def participations(self):
        return self.__participations

    @participations.setter
    def participations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_task_WorkItem__participations", None)
        self.__participations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrgUnit30"):
                    opp_val = getattr(item, "OrgUnit30", None)
                    
                    if opp_val == self:
                        setattr(item, "OrgUnit30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrgUnit30"):
                    opp_val = getattr(item, "OrgUnit30", None)
                    
                    setattr(item, "OrgUnit30", self)
                    
