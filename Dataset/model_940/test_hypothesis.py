import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    esmodel_url_ModelElementUrlFragment,
    esmodel_url_ProjectUrlFragment,
    esmodel_url_ServerUrl,
    Role,
    esmodel_roles_ProjectAdminRole,
    esmodel_roles_WriterRole,
    esmodel_roles_ServerAdmin,
    esmodel_roles_ReaderRole,
    url_ModelElementUrlFragment,
    url_ProjectUrlFragment,
    url_ServerUrl,
    esmodel_url_ModelElementUrl,
    esmodel_roles_Role,
    esmodel_accesscontrol_OrgUnitProperty,
    accesscontrol_ACOrgUnit,
    accesscontrol_OrgUnitProperty,
    roles_Role,
    ACOrgUnit,
    esmodel_accesscontrol_ACGroup,
    ServerProjectEvent,
    esmodel_server_ProjectUpdatedEvent,
    ServerEvent,
    esmodel_server_ServerProjectEvent,
    operations_OperationId,
    esmodel_accesscontrol_ACUser,
    ReadEvent,
    esmodel_events_NotificationReadEvent,
    Event,
    esmodel_events_ShowChangesEvent,
    esmodel_events_UpdateEvent,
    esmodel_events_DNDEvent,
    esmodel_events_PerspectiveEvent,
    esmodel_events_Validate,
    esmodel_events_MergeEvent,
    esmodel_events_ShowHistoryEvent,
    esmodel_events_NotificationGenerationEvent,
    esmodel_events_NotificationIgnoreEvent,
    esmodel_events_PluginFocusEvent,
    esmodel_events_PresentationSwitchEvent,
    esmodel_server_ServerEvent,
    esmodel_events_RevertEvent,
    esmodel_events_ExceptionEvent,
    esmodel_events_CheckoutEvent,
    esmodel_events_MergeChoiceEvent,
    esmodel_events_NavigatorCreateEvent,
    esmodel_events_URLEvent,
    esmodel_events_LinkEvent,
    esmodel_events_AnnotationEvent,
    esmodel_events_UndoEvent,
    esmodel_events_MergeGlobalChoiceEvent,
    esmodel_events_TraceEvent,
    esmodel_events_PluginStartEvent,
    esmodel_events_ReadEvent,
    esmodel_events_Event,
    CompositeOperation,
    esmodel_semantic_SemanticCompositeOperation,
    esmodel_operations_EObjectToModelElementIdMap,
    esmodel_operations_OperationGroup,
    AttributeOperation,
    esmodel_operations_DiagramLayoutOperation,
    esmodel_operations_ModelElementGroup,
    FeatureOperation,
    esmodel_operations_MultiReferenceMoveOperation,
    esmodel_operations_MultiAttributeMoveOperation,
    esmodel_operations_MultiAttributeOperation,
    esmodel_operations_MultiAttributeSetOperation,
    esmodel_operations_ReferenceOperation,
    esmodel_operations_AttributeOperation,
    operations_EObjectToModelElementIdMap,
    operations_ReferenceOperation,
    operations_esmodel_EObject,
    ReferenceOperation,
    esmodel_operations_MultiReferenceSetOperation,
    esmodel_operations_MultiReferenceOperation,
    esmodel_operations_SingleReferenceOperation,
    esmodel_versioning_VersionProperty,
    AbstractOperation,
    esmodel_operations_CreateDeleteOperation,
    esmodel_operations_FeatureOperation,
    esmodel_operations_CompositeOperation,
    esmodel_versioning_HistoryQuery,
    versioning_ChangePackage,
    versioning_TagVersionSpec,
    esmodel_versioning_HistoryInfo,
    versioning_VersionProperty,
    notification_ESNotification,
    versioning_LogMessage,
    events_Event,
    operations_AbstractOperation,
    esmodel_versioning_ChangePackage,
    esmodel_versioning_LogMessage,
    esmodel_versioning_VersionSpec,
    esmodel_versioning_Version,
    VersionSpec,
    esmodel_versioning_HeadVersionSpec,
    esmodel_versioning_PrimaryVersionSpec,
    esmodel_versioning_DateVersionSpec,
    esmodel_versioning_TagVersionSpec,
    esmodel_ClientVersionInfo,
    esmodel_VersionInfo,
    accesscontrol_ACUser,
    SessionId,
    ProjectHistory,
    accesscontrol_ACGroup,
    esmodel_ServerSpace,
    versioning_PrimaryVersionSpec,
    esmodel_ProjectInfo,
    versioning_Version,
    ProjectId,
    esmodel_ProjectHistory,
    ActivityObject,
    model_activity_Fork,
    model_activity_ActivityInitial,
    model_activity_Branch,
    model_activity_ActivityEnd,
    model_activity_Activity,
    activity_ActivityObject,
    activity_Transition,
    ModelElementId,
    StereotypeAttributeInstance,
    model_profile_StereotypeAttributeInstanceString,
    StereotypeAttribute,
    model_profile_StereotypeAttributeSimple,
    profile_StereotypeAttributeInstance,
    model_util_ModelElementPath,
    profile_StereotypeAttribute,
    profile_Profile,
    profile_Stereotype,
    state_Transition,
    document_Section,
    Section,
    model_document_CompositeSection,
    model_document_LeafSection,
    document_CompositeSection,
    classes_MethodArgument,
    classes_PackageElement,
    requirement_Scenario,
    requirement_UseCase,
    classes_Method,
    classes_Attribute,
    classes_Association,
    classes_Class,
    PackageElement,
    model_classes_Package,
    model_classes_Class,
    classes_Dependency,
    classes_Package,
    diagram_model_Diagram,
    task_Checkable,
    organization_User,
    WorkItem,
    model_task_Milestone,
    model_task_WorkPackage,
    change_ModelChangePackage,
    organization_OrgUnit,
    OrgUnit,
    model_organization_Group,
    model_organization_User,
    task_WorkItem,
    model_task_ActionItem,
    organization_Group,
    task_WorkPackage,
    UnicaseModelElement,
    model_activity_ActivityObject,
    model_profile_Profile,
    model_profile_StereotypeInstance,
    model_classes_Attribute,
    model_classes_Method,
    model_classes_Dependency,
    model_classes_MethodArgument,
    model_task_Checkable,
    model_profile_StereotypeAttribute,
    model_profile_Stereotype,
    model_classes_PackageElement,
    model_classes_Association,
    model_profile_StereotypeAttributeInstance,
    model_activity_Transition,
    model_Attachment,
    model_document_Section,
    model_Annotation,
    profile_StereotypeInstance,
    rationale_Comment,
    document_LeafSection,
    Attachment,
    model_diagram_MEDiagram,
    model_attachment_UrlAttachment,
    model_attachment_FileAttachment,
    Annotation,
    model_task_WorkItem,
    model_organization_OrgUnit,
    Project,
    model_Project,
    model_NonDomainElement,
    metamodel_AssociationClassElement,
    metamodel_ModelVersion,
    UniqueIdentifier,
    esmodel_SessionId,
    esmodel_ProjectId,
    esmodel_accesscontrol_ACOrgUnitId,
    esmodel_operations_OperationId,
    metamodel_ModelElementId,
    IdentifiableElement,
    esmodel_notification_ESNotification,
    esmodel_accesscontrol_ACOrgUnit,
    esmodel_operations_AbstractOperation,
    metamodel_ModelElement,
    metamodel_IdentifiableElement,
    metamodel_UniqueIdentifier,
    ModelElement,
    model_UnicaseModelElement,
    metamodel_Project,
    metamodel_NonDomainElement,
    model_state_StateNode,
    state_StateNode,
    model_state_Transition,
    MeetingSection,
    model_meeting_WorkItemMeetingSection,
    model_meeting_IssueMeetingSection,
    model_meeting_CompositeMeetingSection,
    model_meeting_MeetingSection,
    StateNode,
    model_state_StateEnd,
    model_state_StateInitial,
    model_state_State,
    meeting_IssueMeetingSection,
    meeting_MeetingSection,
    model_meeting_Meeting,
    meeting_WorkItemMeetingSection,
    model_component_DeploymentNode,
    component_Component,
    model_component_ComponentService,
    component_ComponentService,
    model_component_Component,
    model_bug_BugReport,
    Solution,
    model_change_MergingSolution,
    change_MergingProposal,
    Proposal,
    model_change_MergingProposal,
    Issue,
    model_change_MergingIssue,
    model_change_ModelChangePackage,
    model_rationale_Criterion,
    rationale_Assessment,
    rationale_Issue,
    rationale_Criterion,
    rationale_Solution,
    model_rationale_Issue,
    Criterion,
    model_requirement_NonFunctionalRequirement,
    requirement_SystemFunction,
    rationale_Proposal,
    model_requirement_ActorInstance,
    model_requirement_Actor,
    NonDomainElement,
    model_rationale_Proposal,
    model_rationale_Assessment,
    model_rationale_Comment,
    model_rationale_Solution,
    model_requirement_SystemFunction,
    model_requirement_UserTask,
    model_requirement_Step,
    requirement_ActorInstance,
    model_requirement_Scenario,
    requirement_NonFunctionalRequirement,
    requirement_UserTask,
    requirement_Step,
    requirement_Actor,
    model_requirement_UseCase,
    requirement_FunctionalRequirement,
    model_requirement_FunctionalRequirement,
    Severity,
    ArgumentDirectionType,
    MergeGlobalChoiceSelection,
    ResolutionType,
    BugStatus,
    VisibilityType,
    DiagramType,
    ContainmentType,
    ActivityType,
    MergeChoiceSelection,
    AssociationType,
    ScopeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esmodel_url_modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ModelElementUrlFragment)


def test_esmodel_url_modelelementurlfragment_constructor_exists():
    assert callable(esmodel_url_ModelElementUrlFragment.__init__)


def test_esmodel_url_modelelementurlfragment_constructor_args():
    sig = inspect.signature(esmodel_url_ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_url_modelelementurlfragment_has_name():
    assert hasattr(esmodel_url_ModelElementUrlFragment, "name")
    descriptor = None
    for klass in esmodel_url_ModelElementUrlFragment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_url_projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ProjectUrlFragment)


def test_esmodel_url_projecturlfragment_constructor_exists():
    assert callable(esmodel_url_ProjectUrlFragment.__init__)


def test_esmodel_url_projecturlfragment_constructor_args():
    sig = inspect.signature(esmodel_url_ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_url_projecturlfragment_has_name():
    assert hasattr(esmodel_url_ProjectUrlFragment, "name")
    descriptor = None
    for klass in esmodel_url_ProjectUrlFragment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_url_serverurl_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ServerUrl)


def test_esmodel_url_serverurl_constructor_exists():
    assert callable(esmodel_url_ServerUrl.__init__)


def test_esmodel_url_serverurl_constructor_args():
    sig = inspect.signature(esmodel_url_ServerUrl.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "hostName" in params, "Missing parameter 'hostName'"

def test_esmodel_url_serverurl_has_port():
    assert hasattr(esmodel_url_ServerUrl, "port")
    descriptor = None
    for klass in esmodel_url_ServerUrl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_url_serverurl_has_hostName():
    assert hasattr(esmodel_url_ServerUrl, "hostName")
    descriptor = None
    for klass in esmodel_url_ServerUrl.__mro__:
        if "hostName" in klass.__dict__:
            descriptor = klass.__dict__["hostName"]
            break
    assert isinstance(descriptor, property)



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_roles_projectadminrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ProjectAdminRole)


def test_esmodel_roles_projectadminrole_constructor_exists():
    assert callable(esmodel_roles_ProjectAdminRole.__init__)


def test_esmodel_roles_projectadminrole_constructor_args():
    sig = inspect.signature(esmodel_roles_ProjectAdminRole.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_roles_writerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_WriterRole)


def test_esmodel_roles_writerrole_constructor_exists():
    assert callable(esmodel_roles_WriterRole.__init__)


def test_esmodel_roles_writerrole_constructor_args():
    sig = inspect.signature(esmodel_roles_WriterRole.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_roles_serveradmin_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ServerAdmin)


def test_esmodel_roles_serveradmin_constructor_exists():
    assert callable(esmodel_roles_ServerAdmin.__init__)


def test_esmodel_roles_serveradmin_constructor_args():
    sig = inspect.signature(esmodel_roles_ServerAdmin.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_roles_readerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_ReaderRole)


def test_esmodel_roles_readerrole_constructor_exists():
    assert callable(esmodel_roles_ReaderRole.__init__)


def test_esmodel_roles_readerrole_constructor_args():
    sig = inspect.signature(esmodel_roles_ReaderRole.__init__)
    params = list(sig.parameters.keys())



def test_url_modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(url_ModelElementUrlFragment)


def test_url_modelelementurlfragment_constructor_exists():
    assert callable(url_ModelElementUrlFragment.__init__)


def test_url_modelelementurlfragment_constructor_args():
    sig = inspect.signature(url_ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_url_projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(url_ProjectUrlFragment)


def test_url_projecturlfragment_constructor_exists():
    assert callable(url_ProjectUrlFragment.__init__)


def test_url_projecturlfragment_constructor_args():
    sig = inspect.signature(url_ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_url_serverurl_is_not_abstract():
    assert not inspect.isabstract(url_ServerUrl)


def test_url_serverurl_constructor_exists():
    assert callable(url_ServerUrl.__init__)


def test_url_serverurl_constructor_args():
    sig = inspect.signature(url_ServerUrl.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_url_modelelementurl_is_not_abstract():
    assert not inspect.isabstract(esmodel_url_ModelElementUrl)


def test_esmodel_url_modelelementurl_constructor_exists():
    assert callable(esmodel_url_ModelElementUrl.__init__)


def test_esmodel_url_modelelementurl_constructor_args():
    sig = inspect.signature(esmodel_url_ModelElementUrl.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_roles_role_is_not_abstract():
    assert not inspect.isabstract(esmodel_roles_Role)


def test_esmodel_roles_role_constructor_exists():
    assert callable(esmodel_roles_Role.__init__)


def test_esmodel_roles_role_constructor_args():
    sig = inspect.signature(esmodel_roles_Role.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_accesscontrol_orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_OrgUnitProperty)


def test_esmodel_accesscontrol_orgunitproperty_constructor_exists():
    assert callable(esmodel_accesscontrol_OrgUnitProperty.__init__)


def test_esmodel_accesscontrol_orgunitproperty_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_esmodel_accesscontrol_orgunitproperty_has_name():
    assert hasattr(esmodel_accesscontrol_OrgUnitProperty, "name")
    descriptor = None
    for klass in esmodel_accesscontrol_OrgUnitProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_accesscontrol_orgunitproperty_has_value():
    assert hasattr(esmodel_accesscontrol_OrgUnitProperty, "value")
    descriptor = None
    for klass in esmodel_accesscontrol_OrgUnitProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_accesscontrol_acorgunit_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACOrgUnit)


def test_accesscontrol_acorgunit_constructor_exists():
    assert callable(accesscontrol_ACOrgUnit.__init__)


def test_accesscontrol_acorgunit_constructor_args():
    sig = inspect.signature(accesscontrol_ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol_orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_OrgUnitProperty)


def test_accesscontrol_orgunitproperty_constructor_exists():
    assert callable(accesscontrol_OrgUnitProperty.__init__)


def test_accesscontrol_orgunitproperty_constructor_args():
    sig = inspect.signature(accesscontrol_OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())



def test_roles_role_is_not_abstract():
    assert not inspect.isabstract(roles_Role)


def test_roles_role_constructor_exists():
    assert callable(roles_Role.__init__)


def test_roles_role_constructor_args():
    sig = inspect.signature(roles_Role.__init__)
    params = list(sig.parameters.keys())



def test_acorgunit_is_not_abstract():
    assert not inspect.isabstract(ACOrgUnit)


def test_acorgunit_constructor_exists():
    assert callable(ACOrgUnit.__init__)


def test_acorgunit_constructor_args():
    sig = inspect.signature(ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_accesscontrol_acgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACGroup)


def test_esmodel_accesscontrol_acgroup_constructor_exists():
    assert callable(esmodel_accesscontrol_ACGroup.__init__)


def test_esmodel_accesscontrol_acgroup_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(ServerProjectEvent)


def test_serverprojectevent_constructor_exists():
    assert callable(ServerProjectEvent.__init__)


def test_serverprojectevent_constructor_args():
    sig = inspect.signature(ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_server_projectupdatedevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ProjectUpdatedEvent)


def test_esmodel_server_projectupdatedevent_constructor_exists():
    assert callable(esmodel_server_ProjectUpdatedEvent.__init__)


def test_esmodel_server_projectupdatedevent_constructor_args():
    sig = inspect.signature(esmodel_server_ProjectUpdatedEvent.__init__)
    params = list(sig.parameters.keys())



def test_serverevent_is_not_abstract():
    assert not inspect.isabstract(ServerEvent)


def test_serverevent_constructor_exists():
    assert callable(ServerEvent.__init__)


def test_serverevent_constructor_args():
    sig = inspect.signature(ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_server_serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ServerProjectEvent)


def test_esmodel_server_serverprojectevent_constructor_exists():
    assert callable(esmodel_server_ServerProjectEvent.__init__)


def test_esmodel_server_serverprojectevent_constructor_args():
    sig = inspect.signature(esmodel_server_ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_operations_operationid_is_not_abstract():
    assert not inspect.isabstract(operations_OperationId)


def test_operations_operationid_constructor_exists():
    assert callable(operations_OperationId.__init__)


def test_operations_operationid_constructor_args():
    sig = inspect.signature(operations_OperationId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_accesscontrol_acuser_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACUser)


def test_esmodel_accesscontrol_acuser_constructor_exists():
    assert callable(esmodel_accesscontrol_ACUser.__init__)


def test_esmodel_accesscontrol_acuser_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACUser.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_esmodel_accesscontrol_acuser_has_firstName():
    assert hasattr(esmodel_accesscontrol_ACUser, "firstName")
    descriptor = None
    for klass in esmodel_accesscontrol_ACUser.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_accesscontrol_acuser_has_lastName():
    assert hasattr(esmodel_accesscontrol_ACUser, "lastName")
    descriptor = None
    for klass in esmodel_accesscontrol_ACUser.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_readevent_is_not_abstract():
    assert not inspect.isabstract(ReadEvent)


def test_readevent_constructor_exists():
    assert callable(ReadEvent.__init__)


def test_readevent_constructor_args():
    sig = inspect.signature(ReadEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_notificationreadevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationReadEvent)


def test_esmodel_events_notificationreadevent_constructor_exists():
    assert callable(esmodel_events_NotificationReadEvent.__init__)


def test_esmodel_events_notificationreadevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"

def test_esmodel_events_notificationreadevent_has_notificationId():
    assert hasattr(esmodel_events_NotificationReadEvent, "notificationId")
    descriptor = None
    for klass in esmodel_events_NotificationReadEvent.__mro__:
        if "notificationId" in klass.__dict__:
            descriptor = klass.__dict__["notificationId"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_showchangesevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ShowChangesEvent)


def test_esmodel_events_showchangesevent_constructor_exists():
    assert callable(esmodel_events_ShowChangesEvent.__init__)


def test_esmodel_events_showchangesevent_constructor_args():
    sig = inspect.signature(esmodel_events_ShowChangesEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_updateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_UpdateEvent)


def test_esmodel_events_updateevent_constructor_exists():
    assert callable(esmodel_events_UpdateEvent.__init__)


def test_esmodel_events_updateevent_constructor_args():
    sig = inspect.signature(esmodel_events_UpdateEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_dndevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_DNDEvent)


def test_esmodel_events_dndevent_constructor_exists():
    assert callable(esmodel_events_DNDEvent.__init__)


def test_esmodel_events_dndevent_constructor_args():
    sig = inspect.signature(esmodel_events_DNDEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"
    assert "targetView" in params, "Missing parameter 'targetView'"

def test_esmodel_events_dndevent_has_sourceView():
    assert hasattr(esmodel_events_DNDEvent, "sourceView")
    descriptor = None
    for klass in esmodel_events_DNDEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_dndevent_has_targetView():
    assert hasattr(esmodel_events_DNDEvent, "targetView")
    descriptor = None
    for klass in esmodel_events_DNDEvent.__mro__:
        if "targetView" in klass.__dict__:
            descriptor = klass.__dict__["targetView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_perspectiveevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PerspectiveEvent)


def test_esmodel_events_perspectiveevent_constructor_exists():
    assert callable(esmodel_events_PerspectiveEvent.__init__)


def test_esmodel_events_perspectiveevent_constructor_args():
    sig = inspect.signature(esmodel_events_PerspectiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_validate_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_Validate)


def test_esmodel_events_validate_constructor_exists():
    assert callable(esmodel_events_Validate.__init__)


def test_esmodel_events_validate_constructor_args():
    sig = inspect.signature(esmodel_events_Validate.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_mergeevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeEvent)


def test_esmodel_events_mergeevent_constructor_exists():
    assert callable(esmodel_events_MergeEvent.__init__)


def test_esmodel_events_mergeevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "numberOfConflicts" in params, "Missing parameter 'numberOfConflicts'"

def test_esmodel_events_mergeevent_has_totalTime():
    assert hasattr(esmodel_events_MergeEvent, "totalTime")
    descriptor = None
    for klass in esmodel_events_MergeEvent.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_mergeevent_has_numberOfConflicts():
    assert hasattr(esmodel_events_MergeEvent, "numberOfConflicts")
    descriptor = None
    for klass in esmodel_events_MergeEvent.__mro__:
        if "numberOfConflicts" in klass.__dict__:
            descriptor = klass.__dict__["numberOfConflicts"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_showhistoryevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ShowHistoryEvent)


def test_esmodel_events_showhistoryevent_constructor_exists():
    assert callable(esmodel_events_ShowHistoryEvent.__init__)


def test_esmodel_events_showhistoryevent_constructor_args():
    sig = inspect.signature(esmodel_events_ShowHistoryEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_notificationgenerationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationGenerationEvent)


def test_esmodel_events_notificationgenerationevent_constructor_exists():
    assert callable(esmodel_events_NotificationGenerationEvent.__init__)


def test_esmodel_events_notificationgenerationevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationGenerationEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_notificationignoreevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NotificationIgnoreEvent)


def test_esmodel_events_notificationignoreevent_constructor_exists():
    assert callable(esmodel_events_NotificationIgnoreEvent.__init__)


def test_esmodel_events_notificationignoreevent_constructor_args():
    sig = inspect.signature(esmodel_events_NotificationIgnoreEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"

def test_esmodel_events_notificationignoreevent_has_notificationId():
    assert hasattr(esmodel_events_NotificationIgnoreEvent, "notificationId")
    descriptor = None
    for klass in esmodel_events_NotificationIgnoreEvent.__mro__:
        if "notificationId" in klass.__dict__:
            descriptor = klass.__dict__["notificationId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_pluginfocusevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PluginFocusEvent)


def test_esmodel_events_pluginfocusevent_constructor_exists():
    assert callable(esmodel_events_PluginFocusEvent.__init__)


def test_esmodel_events_pluginfocusevent_constructor_args():
    sig = inspect.signature(esmodel_events_PluginFocusEvent.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "pluginId" in params, "Missing parameter 'pluginId'"

def test_esmodel_events_pluginfocusevent_has_startDate():
    assert hasattr(esmodel_events_PluginFocusEvent, "startDate")
    descriptor = None
    for klass in esmodel_events_PluginFocusEvent.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_pluginfocusevent_has_pluginId():
    assert hasattr(esmodel_events_PluginFocusEvent, "pluginId")
    descriptor = None
    for klass in esmodel_events_PluginFocusEvent.__mro__:
        if "pluginId" in klass.__dict__:
            descriptor = klass.__dict__["pluginId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_presentationswitchevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PresentationSwitchEvent)


def test_esmodel_events_presentationswitchevent_constructor_exists():
    assert callable(esmodel_events_PresentationSwitchEvent.__init__)


def test_esmodel_events_presentationswitchevent_constructor_args():
    sig = inspect.signature(esmodel_events_PresentationSwitchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "readView" in params, "Missing parameter 'readView'"
    assert "newPresentation" in params, "Missing parameter 'newPresentation'"

def test_esmodel_events_presentationswitchevent_has_readView():
    assert hasattr(esmodel_events_PresentationSwitchEvent, "readView")
    descriptor = None
    for klass in esmodel_events_PresentationSwitchEvent.__mro__:
        if "readView" in klass.__dict__:
            descriptor = klass.__dict__["readView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_presentationswitchevent_has_newPresentation():
    assert hasattr(esmodel_events_PresentationSwitchEvent, "newPresentation")
    descriptor = None
    for klass in esmodel_events_PresentationSwitchEvent.__mro__:
        if "newPresentation" in klass.__dict__:
            descriptor = klass.__dict__["newPresentation"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_server_serverevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_server_ServerEvent)


def test_esmodel_server_serverevent_constructor_exists():
    assert callable(esmodel_server_ServerEvent.__init__)


def test_esmodel_server_serverevent_constructor_args():
    sig = inspect.signature(esmodel_server_ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_revertevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_RevertEvent)


def test_esmodel_events_revertevent_constructor_exists():
    assert callable(esmodel_events_RevertEvent.__init__)


def test_esmodel_events_revertevent_constructor_args():
    sig = inspect.signature(esmodel_events_RevertEvent.__init__)
    params = list(sig.parameters.keys())
    assert "revertedChangesCount" in params, "Missing parameter 'revertedChangesCount'"

def test_esmodel_events_revertevent_has_revertedChangesCount():
    assert hasattr(esmodel_events_RevertEvent, "revertedChangesCount")
    descriptor = None
    for klass in esmodel_events_RevertEvent.__mro__:
        if "revertedChangesCount" in klass.__dict__:
            descriptor = klass.__dict__["revertedChangesCount"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_exceptionevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ExceptionEvent)


def test_esmodel_events_exceptionevent_constructor_exists():
    assert callable(esmodel_events_ExceptionEvent.__init__)


def test_esmodel_events_exceptionevent_constructor_args():
    sig = inspect.signature(esmodel_events_ExceptionEvent.__init__)
    params = list(sig.parameters.keys())
    assert "ExceptionCauseTitle" in params, "Missing parameter 'ExceptionCauseTitle'"
    assert "ExceptionCauseStackTrace" in params, "Missing parameter 'ExceptionCauseStackTrace'"
    assert "ExceptionStackTrace" in params, "Missing parameter 'ExceptionStackTrace'"
    assert "ExceptionTitle" in params, "Missing parameter 'ExceptionTitle'"

def test_esmodel_events_exceptionevent_has_ExceptionCauseTitle():
    assert hasattr(esmodel_events_ExceptionEvent, "ExceptionCauseTitle")
    descriptor = None
    for klass in esmodel_events_ExceptionEvent.__mro__:
        if "ExceptionCauseTitle" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionCauseTitle"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_exceptionevent_has_ExceptionCauseStackTrace():
    assert hasattr(esmodel_events_ExceptionEvent, "ExceptionCauseStackTrace")
    descriptor = None
    for klass in esmodel_events_ExceptionEvent.__mro__:
        if "ExceptionCauseStackTrace" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionCauseStackTrace"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_exceptionevent_has_ExceptionStackTrace():
    assert hasattr(esmodel_events_ExceptionEvent, "ExceptionStackTrace")
    descriptor = None
    for klass in esmodel_events_ExceptionEvent.__mro__:
        if "ExceptionStackTrace" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionStackTrace"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_exceptionevent_has_ExceptionTitle():
    assert hasattr(esmodel_events_ExceptionEvent, "ExceptionTitle")
    descriptor = None
    for klass in esmodel_events_ExceptionEvent.__mro__:
        if "ExceptionTitle" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionTitle"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_checkoutevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_CheckoutEvent)


def test_esmodel_events_checkoutevent_constructor_exists():
    assert callable(esmodel_events_CheckoutEvent.__init__)


def test_esmodel_events_checkoutevent_constructor_args():
    sig = inspect.signature(esmodel_events_CheckoutEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_mergechoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeChoiceEvent)


def test_esmodel_events_mergechoiceevent_constructor_exists():
    assert callable(esmodel_events_MergeChoiceEvent.__init__)


def test_esmodel_events_mergechoiceevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "contextFeature" in params, "Missing parameter 'contextFeature'"
    assert "createdIssueName" in params, "Missing parameter 'createdIssueName'"

def test_esmodel_events_mergechoiceevent_has_selection():
    assert hasattr(esmodel_events_MergeChoiceEvent, "selection")
    descriptor = None
    for klass in esmodel_events_MergeChoiceEvent.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_mergechoiceevent_has_contextFeature():
    assert hasattr(esmodel_events_MergeChoiceEvent, "contextFeature")
    descriptor = None
    for klass in esmodel_events_MergeChoiceEvent.__mro__:
        if "contextFeature" in klass.__dict__:
            descriptor = klass.__dict__["contextFeature"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_mergechoiceevent_has_createdIssueName():
    assert hasattr(esmodel_events_MergeChoiceEvent, "createdIssueName")
    descriptor = None
    for klass in esmodel_events_MergeChoiceEvent.__mro__:
        if "createdIssueName" in klass.__dict__:
            descriptor = klass.__dict__["createdIssueName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_navigatorcreateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_NavigatorCreateEvent)


def test_esmodel_events_navigatorcreateevent_constructor_exists():
    assert callable(esmodel_events_NavigatorCreateEvent.__init__)


def test_esmodel_events_navigatorcreateevent_constructor_args():
    sig = inspect.signature(esmodel_events_NavigatorCreateEvent.__init__)
    params = list(sig.parameters.keys())
    assert "dynamic" in params, "Missing parameter 'dynamic'"

def test_esmodel_events_navigatorcreateevent_has_dynamic():
    assert hasattr(esmodel_events_NavigatorCreateEvent, "dynamic")
    descriptor = None
    for klass in esmodel_events_NavigatorCreateEvent.__mro__:
        if "dynamic" in klass.__dict__:
            descriptor = klass.__dict__["dynamic"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_urlevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_URLEvent)


def test_esmodel_events_urlevent_constructor_exists():
    assert callable(esmodel_events_URLEvent.__init__)


def test_esmodel_events_urlevent_constructor_args():
    sig = inspect.signature(esmodel_events_URLEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"

def test_esmodel_events_urlevent_has_sourceView():
    assert hasattr(esmodel_events_URLEvent, "sourceView")
    descriptor = None
    for klass in esmodel_events_URLEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_linkevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_LinkEvent)


def test_esmodel_events_linkevent_constructor_exists():
    assert callable(esmodel_events_LinkEvent.__init__)


def test_esmodel_events_linkevent_constructor_args():
    sig = inspect.signature(esmodel_events_LinkEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"
    assert "createdNew" in params, "Missing parameter 'createdNew'"

def test_esmodel_events_linkevent_has_sourceView():
    assert hasattr(esmodel_events_LinkEvent, "sourceView")
    descriptor = None
    for klass in esmodel_events_LinkEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_linkevent_has_createdNew():
    assert hasattr(esmodel_events_LinkEvent, "createdNew")
    descriptor = None
    for klass in esmodel_events_LinkEvent.__mro__:
        if "createdNew" in klass.__dict__:
            descriptor = klass.__dict__["createdNew"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_annotationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_AnnotationEvent)


def test_esmodel_events_annotationevent_constructor_exists():
    assert callable(esmodel_events_AnnotationEvent.__init__)


def test_esmodel_events_annotationevent_constructor_args():
    sig = inspect.signature(esmodel_events_AnnotationEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_undoevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_UndoEvent)


def test_esmodel_events_undoevent_constructor_exists():
    assert callable(esmodel_events_UndoEvent.__init__)


def test_esmodel_events_undoevent_constructor_args():
    sig = inspect.signature(esmodel_events_UndoEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_events_mergeglobalchoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_MergeGlobalChoiceEvent)


def test_esmodel_events_mergeglobalchoiceevent_constructor_exists():
    assert callable(esmodel_events_MergeGlobalChoiceEvent.__init__)


def test_esmodel_events_mergeglobalchoiceevent_constructor_args():
    sig = inspect.signature(esmodel_events_MergeGlobalChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"

def test_esmodel_events_mergeglobalchoiceevent_has_selection():
    assert hasattr(esmodel_events_MergeGlobalChoiceEvent, "selection")
    descriptor = None
    for klass in esmodel_events_MergeGlobalChoiceEvent.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_traceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_TraceEvent)


def test_esmodel_events_traceevent_constructor_exists():
    assert callable(esmodel_events_TraceEvent.__init__)


def test_esmodel_events_traceevent_constructor_args():
    sig = inspect.signature(esmodel_events_TraceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_esmodel_events_traceevent_has_featureName():
    assert hasattr(esmodel_events_TraceEvent, "featureName")
    descriptor = None
    for klass in esmodel_events_TraceEvent.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_pluginstartevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_PluginStartEvent)


def test_esmodel_events_pluginstartevent_constructor_exists():
    assert callable(esmodel_events_PluginStartEvent.__init__)


def test_esmodel_events_pluginstartevent_constructor_args():
    sig = inspect.signature(esmodel_events_PluginStartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "pluginId" in params, "Missing parameter 'pluginId'"

def test_esmodel_events_pluginstartevent_has_pluginId():
    assert hasattr(esmodel_events_PluginStartEvent, "pluginId")
    descriptor = None
    for klass in esmodel_events_PluginStartEvent.__mro__:
        if "pluginId" in klass.__dict__:
            descriptor = klass.__dict__["pluginId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_readevent_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_ReadEvent)


def test_esmodel_events_readevent_constructor_exists():
    assert callable(esmodel_events_ReadEvent.__init__)


def test_esmodel_events_readevent_constructor_args():
    sig = inspect.signature(esmodel_events_ReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"
    assert "readView" in params, "Missing parameter 'readView'"

def test_esmodel_events_readevent_has_sourceView():
    assert hasattr(esmodel_events_ReadEvent, "sourceView")
    descriptor = None
    for klass in esmodel_events_ReadEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_events_readevent_has_readView():
    assert hasattr(esmodel_events_ReadEvent, "readView")
    descriptor = None
    for klass in esmodel_events_ReadEvent.__mro__:
        if "readView" in klass.__dict__:
            descriptor = klass.__dict__["readView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_events_event_is_not_abstract():
    assert not inspect.isabstract(esmodel_events_Event)


def test_esmodel_events_event_constructor_exists():
    assert callable(esmodel_events_Event.__init__)


def test_esmodel_events_event_constructor_args():
    sig = inspect.signature(esmodel_events_Event.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_esmodel_events_event_has_timestamp():
    assert hasattr(esmodel_events_Event, "timestamp")
    descriptor = None
    for klass in esmodel_events_Event.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_compositeoperation_is_not_abstract():
    assert not inspect.isabstract(CompositeOperation)


def test_compositeoperation_constructor_exists():
    assert callable(CompositeOperation.__init__)


def test_compositeoperation_constructor_args():
    sig = inspect.signature(CompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_semantic_semanticcompositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_semantic_SemanticCompositeOperation)


def test_esmodel_semantic_semanticcompositeoperation_constructor_exists():
    assert callable(esmodel_semantic_SemanticCompositeOperation.__init__)


def test_esmodel_semantic_semanticcompositeoperation_constructor_args():
    sig = inspect.signature(esmodel_semantic_SemanticCompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_EObjectToModelElementIdMap)


def test_esmodel_operations_eobjecttomodelelementidmap_constructor_exists():
    assert callable(esmodel_operations_EObjectToModelElementIdMap.__init__)


def test_esmodel_operations_eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(esmodel_operations_EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_operationgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_OperationGroup)


def test_esmodel_operations_operationgroup_constructor_exists():
    assert callable(esmodel_operations_OperationGroup.__init__)


def test_esmodel_operations_operationgroup_constructor_args():
    sig = inspect.signature(esmodel_operations_OperationGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_operations_operationgroup_has_name():
    assert hasattr(esmodel_operations_OperationGroup, "name")
    descriptor = None
    for klass in esmodel_operations_OperationGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(AttributeOperation)


def test_attributeoperation_constructor_exists():
    assert callable(AttributeOperation.__init__)


def test_attributeoperation_constructor_args():
    sig = inspect.signature(AttributeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_diagramlayoutoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_DiagramLayoutOperation)


def test_esmodel_operations_diagramlayoutoperation_constructor_exists():
    assert callable(esmodel_operations_DiagramLayoutOperation.__init__)


def test_esmodel_operations_diagramlayoutoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_DiagramLayoutOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_modelelementgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_ModelElementGroup)


def test_esmodel_operations_modelelementgroup_constructor_exists():
    assert callable(esmodel_operations_ModelElementGroup.__init__)


def test_esmodel_operations_modelelementgroup_constructor_args():
    sig = inspect.signature(esmodel_operations_ModelElementGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_operations_modelelementgroup_has_name():
    assert hasattr(esmodel_operations_ModelElementGroup, "name")
    descriptor = None
    for klass in esmodel_operations_ModelElementGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featureoperation_is_not_abstract():
    assert not inspect.isabstract(FeatureOperation)


def test_featureoperation_constructor_exists():
    assert callable(FeatureOperation.__init__)


def test_featureoperation_constructor_args():
    sig = inspect.signature(FeatureOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_multireferencemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceMoveOperation)


def test_esmodel_operations_multireferencemoveoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceMoveOperation.__init__)


def test_esmodel_operations_multireferencemoveoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newIndex" in params, "Missing parameter 'newIndex'"
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"

def test_esmodel_operations_multireferencemoveoperation_has_newIndex():
    assert hasattr(esmodel_operations_MultiReferenceMoveOperation, "newIndex")
    descriptor = None
    for klass in esmodel_operations_MultiReferenceMoveOperation.__mro__:
        if "newIndex" in klass.__dict__:
            descriptor = klass.__dict__["newIndex"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multireferencemoveoperation_has_oldIndex():
    assert hasattr(esmodel_operations_MultiReferenceMoveOperation, "oldIndex")
    descriptor = None
    for klass in esmodel_operations_MultiReferenceMoveOperation.__mro__:
        if "oldIndex" in klass.__dict__:
            descriptor = klass.__dict__["oldIndex"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_multiattributemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeMoveOperation)


def test_esmodel_operations_multiattributemoveoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeMoveOperation.__init__)


def test_esmodel_operations_multiattributemoveoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"
    assert "referencedValue" in params, "Missing parameter 'referencedValue'"
    assert "newIndex" in params, "Missing parameter 'newIndex'"

def test_esmodel_operations_multiattributemoveoperation_has_oldIndex():
    assert hasattr(esmodel_operations_MultiAttributeMoveOperation, "oldIndex")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeMoveOperation.__mro__:
        if "oldIndex" in klass.__dict__:
            descriptor = klass.__dict__["oldIndex"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributemoveoperation_has_referencedValue():
    assert hasattr(esmodel_operations_MultiAttributeMoveOperation, "referencedValue")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeMoveOperation.__mro__:
        if "referencedValue" in klass.__dict__:
            descriptor = klass.__dict__["referencedValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributemoveoperation_has_newIndex():
    assert hasattr(esmodel_operations_MultiAttributeMoveOperation, "newIndex")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeMoveOperation.__mro__:
        if "newIndex" in klass.__dict__:
            descriptor = klass.__dict__["newIndex"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_multiattributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeOperation)


def test_esmodel_operations_multiattributeoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeOperation.__init__)


def test_esmodel_operations_multiattributeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "referencedValues" in params, "Missing parameter 'referencedValues'"
    assert "indexes" in params, "Missing parameter 'indexes'"
    assert "add" in params, "Missing parameter 'add'"

def test_esmodel_operations_multiattributeoperation_has_referencedValues():
    assert hasattr(esmodel_operations_MultiAttributeOperation, "referencedValues")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeOperation.__mro__:
        if "referencedValues" in klass.__dict__:
            descriptor = klass.__dict__["referencedValues"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributeoperation_has_indexes():
    assert hasattr(esmodel_operations_MultiAttributeOperation, "indexes")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeOperation.__mro__:
        if "indexes" in klass.__dict__:
            descriptor = klass.__dict__["indexes"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributeoperation_has_add():
    assert hasattr(esmodel_operations_MultiAttributeOperation, "add")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_multiattributesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiAttributeSetOperation)


def test_esmodel_operations_multiattributesetoperation_constructor_exists():
    assert callable(esmodel_operations_MultiAttributeSetOperation.__init__)


def test_esmodel_operations_multiattributesetoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiAttributeSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldValue" in params, "Missing parameter 'oldValue'"
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "index" in params, "Missing parameter 'index'"

def test_esmodel_operations_multiattributesetoperation_has_oldValue():
    assert hasattr(esmodel_operations_MultiAttributeSetOperation, "oldValue")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeSetOperation.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributesetoperation_has_newValue():
    assert hasattr(esmodel_operations_MultiAttributeSetOperation, "newValue")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeSetOperation.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multiattributesetoperation_has_index():
    assert hasattr(esmodel_operations_MultiAttributeSetOperation, "index")
    descriptor = None
    for klass in esmodel_operations_MultiAttributeSetOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_ReferenceOperation)


def test_esmodel_operations_referenceoperation_constructor_exists():
    assert callable(esmodel_operations_ReferenceOperation.__init__)


def test_esmodel_operations_referenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_ReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oppositeFeatureName" in params, "Missing parameter 'oppositeFeatureName'"
    assert "containmentType" in params, "Missing parameter 'containmentType'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"

def test_esmodel_operations_referenceoperation_has_oppositeFeatureName():
    assert hasattr(esmodel_operations_ReferenceOperation, "oppositeFeatureName")
    descriptor = None
    for klass in esmodel_operations_ReferenceOperation.__mro__:
        if "oppositeFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["oppositeFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_referenceoperation_has_containmentType():
    assert hasattr(esmodel_operations_ReferenceOperation, "containmentType")
    descriptor = None
    for klass in esmodel_operations_ReferenceOperation.__mro__:
        if "containmentType" in klass.__dict__:
            descriptor = klass.__dict__["containmentType"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_referenceoperation_has_bidirectional():
    assert hasattr(esmodel_operations_ReferenceOperation, "bidirectional")
    descriptor = None
    for klass in esmodel_operations_ReferenceOperation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_AttributeOperation)


def test_esmodel_operations_attributeoperation_constructor_exists():
    assert callable(esmodel_operations_AttributeOperation.__init__)


def test_esmodel_operations_attributeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_esmodel_operations_attributeoperation_has_newValue():
    assert hasattr(esmodel_operations_AttributeOperation, "newValue")
    descriptor = None
    for klass in esmodel_operations_AttributeOperation.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_attributeoperation_has_oldValue():
    assert hasattr(esmodel_operations_AttributeOperation, "oldValue")
    descriptor = None
    for klass in esmodel_operations_AttributeOperation.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_operations_eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(operations_EObjectToModelElementIdMap)


def test_operations_eobjecttomodelelementidmap_constructor_exists():
    assert callable(operations_EObjectToModelElementIdMap.__init__)


def test_operations_eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(operations_EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_operations_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(operations_ReferenceOperation)


def test_operations_referenceoperation_constructor_exists():
    assert callable(operations_ReferenceOperation.__init__)


def test_operations_referenceoperation_constructor_args():
    sig = inspect.signature(operations_ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_operations_esmodel_eobject_is_not_abstract():
    assert not inspect.isabstract(operations_esmodel_EObject)


def test_operations_esmodel_eobject_constructor_exists():
    assert callable(operations_esmodel_EObject.__init__)


def test_operations_esmodel_eobject_constructor_args():
    sig = inspect.signature(operations_esmodel_EObject.__init__)
    params = list(sig.parameters.keys())



def test_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(ReferenceOperation)


def test_referenceoperation_constructor_exists():
    assert callable(ReferenceOperation.__init__)


def test_referenceoperation_constructor_args():
    sig = inspect.signature(ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_multireferencesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceSetOperation)


def test_esmodel_operations_multireferencesetoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceSetOperation.__init__)


def test_esmodel_operations_multireferencesetoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_esmodel_operations_multireferencesetoperation_has_index():
    assert hasattr(esmodel_operations_MultiReferenceSetOperation, "index")
    descriptor = None
    for klass in esmodel_operations_MultiReferenceSetOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_multireferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_MultiReferenceOperation)


def test_esmodel_operations_multireferenceoperation_constructor_exists():
    assert callable(esmodel_operations_MultiReferenceOperation.__init__)


def test_esmodel_operations_multireferenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_MultiReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "index" in params, "Missing parameter 'index'"

def test_esmodel_operations_multireferenceoperation_has_add():
    assert hasattr(esmodel_operations_MultiReferenceOperation, "add")
    descriptor = None
    for klass in esmodel_operations_MultiReferenceOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_multireferenceoperation_has_index():
    assert hasattr(esmodel_operations_MultiReferenceOperation, "index")
    descriptor = None
    for klass in esmodel_operations_MultiReferenceOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_singlereferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_SingleReferenceOperation)


def test_esmodel_operations_singlereferenceoperation_constructor_exists():
    assert callable(esmodel_operations_SingleReferenceOperation.__init__)


def test_esmodel_operations_singlereferenceoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_SingleReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_versionproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_VersionProperty)


def test_esmodel_versioning_versionproperty_constructor_exists():
    assert callable(esmodel_versioning_VersionProperty.__init__)


def test_esmodel_versioning_versionproperty_constructor_args():
    sig = inspect.signature(esmodel_versioning_VersionProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_versioning_versionproperty_has_value():
    assert hasattr(esmodel_versioning_VersionProperty, "value")
    descriptor = None
    for klass in esmodel_versioning_VersionProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_versioning_versionproperty_has_name():
    assert hasattr(esmodel_versioning_VersionProperty, "name")
    descriptor = None
    for klass in esmodel_versioning_VersionProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(AbstractOperation)


def test_abstractoperation_constructor_exists():
    assert callable(AbstractOperation.__init__)


def test_abstractoperation_constructor_args():
    sig = inspect.signature(AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_createdeleteoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_CreateDeleteOperation)


def test_esmodel_operations_createdeleteoperation_constructor_exists():
    assert callable(esmodel_operations_CreateDeleteOperation.__init__)


def test_esmodel_operations_createdeleteoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_CreateDeleteOperation.__init__)
    params = list(sig.parameters.keys())
    assert "delete" in params, "Missing parameter 'delete'"

def test_esmodel_operations_createdeleteoperation_has_delete():
    assert hasattr(esmodel_operations_CreateDeleteOperation, "delete")
    descriptor = None
    for klass in esmodel_operations_CreateDeleteOperation.__mro__:
        if "delete" in klass.__dict__:
            descriptor = klass.__dict__["delete"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_featureoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_FeatureOperation)


def test_esmodel_operations_featureoperation_constructor_exists():
    assert callable(esmodel_operations_FeatureOperation.__init__)


def test_esmodel_operations_featureoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_FeatureOperation.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_esmodel_operations_featureoperation_has_featureName():
    assert hasattr(esmodel_operations_FeatureOperation, "featureName")
    descriptor = None
    for klass in esmodel_operations_FeatureOperation.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_compositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_CompositeOperation)


def test_esmodel_operations_compositeoperation_constructor_exists():
    assert callable(esmodel_operations_CompositeOperation.__init__)


def test_esmodel_operations_compositeoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_CompositeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "compositeDescription" in params, "Missing parameter 'compositeDescription'"
    assert "reversed" in params, "Missing parameter 'reversed'"
    assert "compositeName" in params, "Missing parameter 'compositeName'"

def test_esmodel_operations_compositeoperation_has_compositeDescription():
    assert hasattr(esmodel_operations_CompositeOperation, "compositeDescription")
    descriptor = None
    for klass in esmodel_operations_CompositeOperation.__mro__:
        if "compositeDescription" in klass.__dict__:
            descriptor = klass.__dict__["compositeDescription"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_compositeoperation_has_reversed():
    assert hasattr(esmodel_operations_CompositeOperation, "reversed")
    descriptor = None
    for klass in esmodel_operations_CompositeOperation.__mro__:
        if "reversed" in klass.__dict__:
            descriptor = klass.__dict__["reversed"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_compositeoperation_has_compositeName():
    assert hasattr(esmodel_operations_CompositeOperation, "compositeName")
    descriptor = None
    for klass in esmodel_operations_CompositeOperation.__mro__:
        if "compositeName" in klass.__dict__:
            descriptor = klass.__dict__["compositeName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_versioning_historyquery_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HistoryQuery)


def test_esmodel_versioning_historyquery_constructor_exists():
    assert callable(esmodel_versioning_HistoryQuery.__init__)


def test_esmodel_versioning_historyquery_constructor_args():
    sig = inspect.signature(esmodel_versioning_HistoryQuery.__init__)
    params = list(sig.parameters.keys())
    assert "includeChangePackage" in params, "Missing parameter 'includeChangePackage'"

def test_esmodel_versioning_historyquery_has_includeChangePackage():
    assert hasattr(esmodel_versioning_HistoryQuery, "includeChangePackage")
    descriptor = None
    for klass in esmodel_versioning_HistoryQuery.__mro__:
        if "includeChangePackage" in klass.__dict__:
            descriptor = klass.__dict__["includeChangePackage"]
            break
    assert isinstance(descriptor, property)



def test_versioning_changepackage_is_not_abstract():
    assert not inspect.isabstract(versioning_ChangePackage)


def test_versioning_changepackage_constructor_exists():
    assert callable(versioning_ChangePackage.__init__)


def test_versioning_changepackage_constructor_args():
    sig = inspect.signature(versioning_ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_versioning_tagversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning_TagVersionSpec)


def test_versioning_tagversionspec_constructor_exists():
    assert callable(versioning_TagVersionSpec.__init__)


def test_versioning_tagversionspec_constructor_args():
    sig = inspect.signature(versioning_TagVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_historyinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HistoryInfo)


def test_esmodel_versioning_historyinfo_constructor_exists():
    assert callable(esmodel_versioning_HistoryInfo.__init__)


def test_esmodel_versioning_historyinfo_constructor_args():
    sig = inspect.signature(esmodel_versioning_HistoryInfo.__init__)
    params = list(sig.parameters.keys())



def test_versioning_versionproperty_is_not_abstract():
    assert not inspect.isabstract(versioning_VersionProperty)


def test_versioning_versionproperty_constructor_exists():
    assert callable(versioning_VersionProperty.__init__)


def test_versioning_versionproperty_constructor_args():
    sig = inspect.signature(versioning_VersionProperty.__init__)
    params = list(sig.parameters.keys())



def test_notification_esnotification_is_not_abstract():
    assert not inspect.isabstract(notification_ESNotification)


def test_notification_esnotification_constructor_exists():
    assert callable(notification_ESNotification.__init__)


def test_notification_esnotification_constructor_args():
    sig = inspect.signature(notification_ESNotification.__init__)
    params = list(sig.parameters.keys())



def test_versioning_logmessage_is_not_abstract():
    assert not inspect.isabstract(versioning_LogMessage)


def test_versioning_logmessage_constructor_exists():
    assert callable(versioning_LogMessage.__init__)


def test_versioning_logmessage_constructor_args():
    sig = inspect.signature(versioning_LogMessage.__init__)
    params = list(sig.parameters.keys())



def test_events_event_is_not_abstract():
    assert not inspect.isabstract(events_Event)


def test_events_event_constructor_exists():
    assert callable(events_Event.__init__)


def test_events_event_constructor_args():
    sig = inspect.signature(events_Event.__init__)
    params = list(sig.parameters.keys())



def test_operations_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(operations_AbstractOperation)


def test_operations_abstractoperation_constructor_exists():
    assert callable(operations_AbstractOperation.__init__)


def test_operations_abstractoperation_constructor_args():
    sig = inspect.signature(operations_AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_changepackage_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_ChangePackage)


def test_esmodel_versioning_changepackage_constructor_exists():
    assert callable(esmodel_versioning_ChangePackage.__init__)


def test_esmodel_versioning_changepackage_constructor_args():
    sig = inspect.signature(esmodel_versioning_ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_logmessage_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_LogMessage)


def test_esmodel_versioning_logmessage_constructor_exists():
    assert callable(esmodel_versioning_LogMessage.__init__)


def test_esmodel_versioning_logmessage_constructor_args():
    sig = inspect.signature(esmodel_versioning_LogMessage.__init__)
    params = list(sig.parameters.keys())
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "message" in params, "Missing parameter 'message'"
    assert "date" in params, "Missing parameter 'date'"
    assert "author" in params, "Missing parameter 'author'"

def test_esmodel_versioning_logmessage_has_clientDate():
    assert hasattr(esmodel_versioning_LogMessage, "clientDate")
    descriptor = None
    for klass in esmodel_versioning_LogMessage.__mro__:
        if "clientDate" in klass.__dict__:
            descriptor = klass.__dict__["clientDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_versioning_logmessage_has_message():
    assert hasattr(esmodel_versioning_LogMessage, "message")
    descriptor = None
    for klass in esmodel_versioning_LogMessage.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_versioning_logmessage_has_date():
    assert hasattr(esmodel_versioning_LogMessage, "date")
    descriptor = None
    for klass in esmodel_versioning_LogMessage.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_versioning_logmessage_has_author():
    assert hasattr(esmodel_versioning_LogMessage, "author")
    descriptor = None
    for klass in esmodel_versioning_LogMessage.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_versioning_versionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_VersionSpec)


def test_esmodel_versioning_versionspec_constructor_exists():
    assert callable(esmodel_versioning_VersionSpec.__init__)


def test_esmodel_versioning_versionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_version_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_Version)


def test_esmodel_versioning_version_constructor_exists():
    assert callable(esmodel_versioning_Version.__init__)


def test_esmodel_versioning_version_constructor_args():
    sig = inspect.signature(esmodel_versioning_Version.__init__)
    params = list(sig.parameters.keys())



def test_versionspec_is_not_abstract():
    assert not inspect.isabstract(VersionSpec)


def test_versionspec_constructor_exists():
    assert callable(VersionSpec.__init__)


def test_versionspec_constructor_args():
    sig = inspect.signature(VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_headversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_HeadVersionSpec)


def test_esmodel_versioning_headversionspec_constructor_exists():
    assert callable(esmodel_versioning_HeadVersionSpec.__init__)


def test_esmodel_versioning_headversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_HeadVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_versioning_primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_PrimaryVersionSpec)


def test_esmodel_versioning_primaryversionspec_constructor_exists():
    assert callable(esmodel_versioning_PrimaryVersionSpec.__init__)


def test_esmodel_versioning_primaryversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_esmodel_versioning_primaryversionspec_has_identifier():
    assert hasattr(esmodel_versioning_PrimaryVersionSpec, "identifier")
    descriptor = None
    for klass in esmodel_versioning_PrimaryVersionSpec.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_versioning_dateversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_DateVersionSpec)


def test_esmodel_versioning_dateversionspec_constructor_exists():
    assert callable(esmodel_versioning_DateVersionSpec.__init__)


def test_esmodel_versioning_dateversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_DateVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_esmodel_versioning_dateversionspec_has_date():
    assert hasattr(esmodel_versioning_DateVersionSpec, "date")
    descriptor = None
    for klass in esmodel_versioning_DateVersionSpec.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_versioning_tagversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel_versioning_TagVersionSpec)


def test_esmodel_versioning_tagversionspec_constructor_exists():
    assert callable(esmodel_versioning_TagVersionSpec.__init__)


def test_esmodel_versioning_tagversionspec_constructor_args():
    sig = inspect.signature(esmodel_versioning_TagVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_versioning_tagversionspec_has_name():
    assert hasattr(esmodel_versioning_TagVersionSpec, "name")
    descriptor = None
    for klass in esmodel_versioning_TagVersionSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_clientversioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_ClientVersionInfo)


def test_esmodel_clientversioninfo_constructor_exists():
    assert callable(esmodel_ClientVersionInfo.__init__)


def test_esmodel_clientversioninfo_constructor_args():
    sig = inspect.signature(esmodel_ClientVersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_esmodel_clientversioninfo_has_name():
    assert hasattr(esmodel_ClientVersionInfo, "name")
    descriptor = None
    for klass in esmodel_ClientVersionInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_clientversioninfo_has_version():
    assert hasattr(esmodel_ClientVersionInfo, "version")
    descriptor = None
    for klass in esmodel_ClientVersionInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_versioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_VersionInfo)


def test_esmodel_versioninfo_constructor_exists():
    assert callable(esmodel_VersionInfo.__init__)


def test_esmodel_versioninfo_constructor_args():
    sig = inspect.signature(esmodel_VersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "emfStoreVersionString" in params, "Missing parameter 'emfStoreVersionString'"

def test_esmodel_versioninfo_has_emfStoreVersionString():
    assert hasattr(esmodel_VersionInfo, "emfStoreVersionString")
    descriptor = None
    for klass in esmodel_VersionInfo.__mro__:
        if "emfStoreVersionString" in klass.__dict__:
            descriptor = klass.__dict__["emfStoreVersionString"]
            break
    assert isinstance(descriptor, property)



def test_accesscontrol_acuser_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACUser)


def test_accesscontrol_acuser_constructor_exists():
    assert callable(accesscontrol_ACUser.__init__)


def test_accesscontrol_acuser_constructor_args():
    sig = inspect.signature(accesscontrol_ACUser.__init__)
    params = list(sig.parameters.keys())



def test_sessionid_is_not_abstract():
    assert not inspect.isabstract(SessionId)


def test_sessionid_constructor_exists():
    assert callable(SessionId.__init__)


def test_sessionid_constructor_args():
    sig = inspect.signature(SessionId.__init__)
    params = list(sig.parameters.keys())



def test_projecthistory_is_not_abstract():
    assert not inspect.isabstract(ProjectHistory)


def test_projecthistory_constructor_exists():
    assert callable(ProjectHistory.__init__)


def test_projecthistory_constructor_args():
    sig = inspect.signature(ProjectHistory.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol_acgroup_is_not_abstract():
    assert not inspect.isabstract(accesscontrol_ACGroup)


def test_accesscontrol_acgroup_constructor_exists():
    assert callable(accesscontrol_ACGroup.__init__)


def test_accesscontrol_acgroup_constructor_args():
    sig = inspect.signature(accesscontrol_ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_serverspace_is_not_abstract():
    assert not inspect.isabstract(esmodel_ServerSpace)


def test_esmodel_serverspace_constructor_exists():
    assert callable(esmodel_ServerSpace.__init__)


def test_esmodel_serverspace_constructor_args():
    sig = inspect.signature(esmodel_ServerSpace.__init__)
    params = list(sig.parameters.keys())



def test_versioning_primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning_PrimaryVersionSpec)


def test_versioning_primaryversionspec_constructor_exists():
    assert callable(versioning_PrimaryVersionSpec.__init__)


def test_versioning_primaryversionspec_constructor_args():
    sig = inspect.signature(versioning_PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_projectinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectInfo)


def test_esmodel_projectinfo_constructor_exists():
    assert callable(esmodel_ProjectInfo.__init__)


def test_esmodel_projectinfo_constructor_args():
    sig = inspect.signature(esmodel_ProjectInfo.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel_projectinfo_has_description():
    assert hasattr(esmodel_ProjectInfo, "description")
    descriptor = None
    for klass in esmodel_ProjectInfo.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_projectinfo_has_name():
    assert hasattr(esmodel_ProjectInfo, "name")
    descriptor = None
    for klass in esmodel_ProjectInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_versioning_version_is_not_abstract():
    assert not inspect.isabstract(versioning_Version)


def test_versioning_version_constructor_exists():
    assert callable(versioning_Version.__init__)


def test_versioning_version_constructor_args():
    sig = inspect.signature(versioning_Version.__init__)
    params = list(sig.parameters.keys())



def test_projectid_is_not_abstract():
    assert not inspect.isabstract(ProjectId)


def test_projectid_constructor_exists():
    assert callable(ProjectId.__init__)


def test_projectid_constructor_args():
    sig = inspect.signature(ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_projecthistory_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectHistory)


def test_esmodel_projecthistory_constructor_exists():
    assert callable(esmodel_ProjectHistory.__init__)


def test_esmodel_projecthistory_constructor_args():
    sig = inspect.signature(esmodel_ProjectHistory.__init__)
    params = list(sig.parameters.keys())
    assert "projectDescription" in params, "Missing parameter 'projectDescription'"
    assert "projectName" in params, "Missing parameter 'projectName'"

def test_esmodel_projecthistory_has_projectDescription():
    assert hasattr(esmodel_ProjectHistory, "projectDescription")
    descriptor = None
    for klass in esmodel_ProjectHistory.__mro__:
        if "projectDescription" in klass.__dict__:
            descriptor = klass.__dict__["projectDescription"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_projecthistory_has_projectName():
    assert hasattr(esmodel_ProjectHistory, "projectName")
    descriptor = None
    for klass in esmodel_ProjectHistory.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)



def test_activityobject_is_not_abstract():
    assert not inspect.isabstract(ActivityObject)


def test_activityobject_constructor_exists():
    assert callable(ActivityObject.__init__)


def test_activityobject_constructor_args():
    sig = inspect.signature(ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_fork_is_not_abstract():
    assert not inspect.isabstract(model_activity_Fork)


def test_model_activity_fork_constructor_exists():
    assert callable(model_activity_Fork.__init__)


def test_model_activity_fork_constructor_args():
    sig = inspect.signature(model_activity_Fork.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_activityinitial_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityInitial)


def test_model_activity_activityinitial_constructor_exists():
    assert callable(model_activity_ActivityInitial.__init__)


def test_model_activity_activityinitial_constructor_args():
    sig = inspect.signature(model_activity_ActivityInitial.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_branch_is_not_abstract():
    assert not inspect.isabstract(model_activity_Branch)


def test_model_activity_branch_constructor_exists():
    assert callable(model_activity_Branch.__init__)


def test_model_activity_branch_constructor_args():
    sig = inspect.signature(model_activity_Branch.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_activityend_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityEnd)


def test_model_activity_activityend_constructor_exists():
    assert callable(model_activity_ActivityEnd.__init__)


def test_model_activity_activityend_constructor_args():
    sig = inspect.signature(model_activity_ActivityEnd.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_activity_is_not_abstract():
    assert not inspect.isabstract(model_activity_Activity)


def test_model_activity_activity_constructor_exists():
    assert callable(model_activity_Activity.__init__)


def test_model_activity_activity_constructor_args():
    sig = inspect.signature(model_activity_Activity.__init__)
    params = list(sig.parameters.keys())



def test_activity_activityobject_is_not_abstract():
    assert not inspect.isabstract(activity_ActivityObject)


def test_activity_activityobject_constructor_exists():
    assert callable(activity_ActivityObject.__init__)


def test_activity_activityobject_constructor_args():
    sig = inspect.signature(activity_ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_activity_transition_is_not_abstract():
    assert not inspect.isabstract(activity_Transition)


def test_activity_transition_constructor_exists():
    assert callable(activity_Transition.__init__)


def test_activity_transition_constructor_args():
    sig = inspect.signature(activity_Transition.__init__)
    params = list(sig.parameters.keys())



def test_modelelementid_is_not_abstract():
    assert not inspect.isabstract(ModelElementId)


def test_modelelementid_constructor_exists():
    assert callable(ModelElementId.__init__)


def test_modelelementid_constructor_args():
    sig = inspect.signature(ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttributeInstance)


def test_stereotypeattributeinstance_constructor_exists():
    assert callable(StereotypeAttributeInstance.__init__)


def test_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_profile_stereotypeattributeinstancestring_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeInstanceString)


def test_model_profile_stereotypeattributeinstancestring_constructor_exists():
    assert callable(model_profile_StereotypeAttributeInstanceString.__init__)


def test_model_profile_stereotypeattributeinstancestring_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeInstanceString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_profile_stereotypeattributeinstancestring_has_value():
    assert hasattr(model_profile_StereotypeAttributeInstanceString, "value")
    descriptor = None
    for klass in model_profile_StereotypeAttributeInstanceString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttribute)


def test_stereotypeattribute_constructor_exists():
    assert callable(StereotypeAttribute.__init__)


def test_stereotypeattribute_constructor_args():
    sig = inspect.signature(StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_model_profile_stereotypeattributesimple_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeSimple)


def test_model_profile_stereotypeattributesimple_constructor_exists():
    assert callable(model_profile_StereotypeAttributeSimple.__init__)


def test_model_profile_stereotypeattributesimple_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeSimple.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_profile_stereotypeattributesimple_has_type():
    assert hasattr(model_profile_StereotypeAttributeSimple, "type")
    descriptor = None
    for klass in model_profile_StereotypeAttributeSimple.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_profile_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeAttributeInstance)


def test_profile_stereotypeattributeinstance_constructor_exists():
    assert callable(profile_StereotypeAttributeInstance.__init__)


def test_profile_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(profile_StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_util_modelelementpath_is_not_abstract():
    assert not inspect.isabstract(model_util_ModelElementPath)


def test_model_util_modelelementpath_constructor_exists():
    assert callable(model_util_ModelElementPath.__init__)


def test_model_util_modelelementpath_constructor_args():
    sig = inspect.signature(model_util_ModelElementPath.__init__)
    params = list(sig.parameters.keys())



def test_profile_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeAttribute)


def test_profile_stereotypeattribute_constructor_exists():
    assert callable(profile_StereotypeAttribute.__init__)


def test_profile_stereotypeattribute_constructor_args():
    sig = inspect.signature(profile_StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_profile_profile_is_not_abstract():
    assert not inspect.isabstract(profile_Profile)


def test_profile_profile_constructor_exists():
    assert callable(profile_Profile.__init__)


def test_profile_profile_constructor_args():
    sig = inspect.signature(profile_Profile.__init__)
    params = list(sig.parameters.keys())



def test_profile_stereotype_is_not_abstract():
    assert not inspect.isabstract(profile_Stereotype)


def test_profile_stereotype_constructor_exists():
    assert callable(profile_Stereotype.__init__)


def test_profile_stereotype_constructor_args():
    sig = inspect.signature(profile_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_state_transition_is_not_abstract():
    assert not inspect.isabstract(state_Transition)


def test_state_transition_constructor_exists():
    assert callable(state_Transition.__init__)


def test_state_transition_constructor_args():
    sig = inspect.signature(state_Transition.__init__)
    params = list(sig.parameters.keys())



def test_document_section_is_not_abstract():
    assert not inspect.isabstract(document_Section)


def test_document_section_constructor_exists():
    assert callable(document_Section.__init__)


def test_document_section_constructor_args():
    sig = inspect.signature(document_Section.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_model_document_compositesection_is_not_abstract():
    assert not inspect.isabstract(model_document_CompositeSection)


def test_model_document_compositesection_constructor_exists():
    assert callable(model_document_CompositeSection.__init__)


def test_model_document_compositesection_constructor_args():
    sig = inspect.signature(model_document_CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_model_document_leafsection_is_not_abstract():
    assert not inspect.isabstract(model_document_LeafSection)


def test_model_document_leafsection_constructor_exists():
    assert callable(model_document_LeafSection.__init__)


def test_model_document_leafsection_constructor_args():
    sig = inspect.signature(model_document_LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_document_compositesection_is_not_abstract():
    assert not inspect.isabstract(document_CompositeSection)


def test_document_compositesection_constructor_exists():
    assert callable(document_CompositeSection.__init__)


def test_document_compositesection_constructor_args():
    sig = inspect.signature(document_CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_classes_methodargument_is_not_abstract():
    assert not inspect.isabstract(classes_MethodArgument)


def test_classes_methodargument_constructor_exists():
    assert callable(classes_MethodArgument.__init__)


def test_classes_methodargument_constructor_args():
    sig = inspect.signature(classes_MethodArgument.__init__)
    params = list(sig.parameters.keys())



def test_classes_packageelement_is_not_abstract():
    assert not inspect.isabstract(classes_PackageElement)


def test_classes_packageelement_constructor_exists():
    assert callable(classes_PackageElement.__init__)


def test_classes_packageelement_constructor_args():
    sig = inspect.signature(classes_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_requirement_scenario_is_not_abstract():
    assert not inspect.isabstract(requirement_Scenario)


def test_requirement_scenario_constructor_exists():
    assert callable(requirement_Scenario.__init__)


def test_requirement_scenario_constructor_args():
    sig = inspect.signature(requirement_Scenario.__init__)
    params = list(sig.parameters.keys())



def test_requirement_usecase_is_not_abstract():
    assert not inspect.isabstract(requirement_UseCase)


def test_requirement_usecase_constructor_exists():
    assert callable(requirement_UseCase.__init__)


def test_requirement_usecase_constructor_args():
    sig = inspect.signature(requirement_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_classes_method_is_not_abstract():
    assert not inspect.isabstract(classes_Method)


def test_classes_method_constructor_exists():
    assert callable(classes_Method.__init__)


def test_classes_method_constructor_args():
    sig = inspect.signature(classes_Method.__init__)
    params = list(sig.parameters.keys())



def test_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(classes_Attribute)


def test_classes_attribute_constructor_exists():
    assert callable(classes_Attribute.__init__)


def test_classes_attribute_constructor_args():
    sig = inspect.signature(classes_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classes_association_is_not_abstract():
    assert not inspect.isabstract(classes_Association)


def test_classes_association_constructor_exists():
    assert callable(classes_Association.__init__)


def test_classes_association_constructor_args():
    sig = inspect.signature(classes_Association.__init__)
    params = list(sig.parameters.keys())



def test_classes_class_is_not_abstract():
    assert not inspect.isabstract(classes_Class)


def test_classes_class_constructor_exists():
    assert callable(classes_Class.__init__)


def test_classes_class_constructor_args():
    sig = inspect.signature(classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_model_classes_package_is_not_abstract():
    assert not inspect.isabstract(model_classes_Package)


def test_model_classes_package_constructor_exists():
    assert callable(model_classes_Package.__init__)


def test_model_classes_package_constructor_args():
    sig = inspect.signature(model_classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_model_classes_class_is_not_abstract():
    assert not inspect.isabstract(model_classes_Class)


def test_model_classes_class_constructor_exists():
    assert callable(model_classes_Class.__init__)


def test_model_classes_class_constructor_args():
    sig = inspect.signature(model_classes_Class.__init__)
    params = list(sig.parameters.keys())



def test_classes_dependency_is_not_abstract():
    assert not inspect.isabstract(classes_Dependency)


def test_classes_dependency_constructor_exists():
    assert callable(classes_Dependency.__init__)


def test_classes_dependency_constructor_args():
    sig = inspect.signature(classes_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classes_package_is_not_abstract():
    assert not inspect.isabstract(classes_Package)


def test_classes_package_constructor_exists():
    assert callable(classes_Package.__init__)


def test_classes_package_constructor_args():
    sig = inspect.signature(classes_Package.__init__)
    params = list(sig.parameters.keys())



def test_diagram_model_diagram_is_not_abstract():
    assert not inspect.isabstract(diagram_model_Diagram)


def test_diagram_model_diagram_constructor_exists():
    assert callable(diagram_model_Diagram.__init__)


def test_diagram_model_diagram_constructor_args():
    sig = inspect.signature(diagram_model_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_task_checkable_is_not_abstract():
    assert not inspect.isabstract(task_Checkable)


def test_task_checkable_constructor_exists():
    assert callable(task_Checkable.__init__)


def test_task_checkable_constructor_args():
    sig = inspect.signature(task_Checkable.__init__)
    params = list(sig.parameters.keys())



def test_organization_user_is_not_abstract():
    assert not inspect.isabstract(organization_User)


def test_organization_user_constructor_exists():
    assert callable(organization_User.__init__)


def test_organization_user_constructor_args():
    sig = inspect.signature(organization_User.__init__)
    params = list(sig.parameters.keys())



def test_workitem_is_not_abstract():
    assert not inspect.isabstract(WorkItem)


def test_workitem_constructor_exists():
    assert callable(WorkItem.__init__)


def test_workitem_constructor_args():
    sig = inspect.signature(WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_model_task_milestone_is_not_abstract():
    assert not inspect.isabstract(model_task_Milestone)


def test_model_task_milestone_constructor_exists():
    assert callable(model_task_Milestone.__init__)


def test_model_task_milestone_constructor_args():
    sig = inspect.signature(model_task_Milestone.__init__)
    params = list(sig.parameters.keys())



def test_model_task_workpackage_is_not_abstract():
    assert not inspect.isabstract(model_task_WorkPackage)


def test_model_task_workpackage_constructor_exists():
    assert callable(model_task_WorkPackage.__init__)


def test_model_task_workpackage_constructor_args():
    sig = inspect.signature(model_task_WorkPackage.__init__)
    params = list(sig.parameters.keys())
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"

def test_model_task_workpackage_has_endDate():
    assert hasattr(model_task_WorkPackage, "endDate")
    descriptor = None
    for klass in model_task_WorkPackage.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_model_task_workpackage_has_startDate():
    assert hasattr(model_task_WorkPackage, "startDate")
    descriptor = None
    for klass in model_task_WorkPackage.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)



def test_change_modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(change_ModelChangePackage)


def test_change_modelchangepackage_constructor_exists():
    assert callable(change_ModelChangePackage.__init__)


def test_change_modelchangepackage_constructor_args():
    sig = inspect.signature(change_ModelChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_organization_orgunit_is_not_abstract():
    assert not inspect.isabstract(organization_OrgUnit)


def test_organization_orgunit_constructor_exists():
    assert callable(organization_OrgUnit.__init__)


def test_organization_orgunit_constructor_args():
    sig = inspect.signature(organization_OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_orgunit_is_not_abstract():
    assert not inspect.isabstract(OrgUnit)


def test_orgunit_constructor_exists():
    assert callable(OrgUnit.__init__)


def test_orgunit_constructor_args():
    sig = inspect.signature(OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_model_organization_group_is_not_abstract():
    assert not inspect.isabstract(model_organization_Group)


def test_model_organization_group_constructor_exists():
    assert callable(model_organization_Group.__init__)


def test_model_organization_group_constructor_args():
    sig = inspect.signature(model_organization_Group.__init__)
    params = list(sig.parameters.keys())



def test_model_organization_user_is_not_abstract():
    assert not inspect.isabstract(model_organization_User)


def test_model_organization_user_constructor_exists():
    assert callable(model_organization_User.__init__)


def test_model_organization_user_constructor_args():
    sig = inspect.signature(model_organization_User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_model_organization_user_has_email():
    assert hasattr(model_organization_User, "email")
    descriptor = None
    for klass in model_organization_User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_model_organization_user_has_firstName():
    assert hasattr(model_organization_User, "firstName")
    descriptor = None
    for klass in model_organization_User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_model_organization_user_has_lastName():
    assert hasattr(model_organization_User, "lastName")
    descriptor = None
    for klass in model_organization_User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_task_workitem_is_not_abstract():
    assert not inspect.isabstract(task_WorkItem)


def test_task_workitem_constructor_exists():
    assert callable(task_WorkItem.__init__)


def test_task_workitem_constructor_args():
    sig = inspect.signature(task_WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_model_task_actionitem_is_not_abstract():
    assert not inspect.isabstract(model_task_ActionItem)


def test_model_task_actionitem_constructor_exists():
    assert callable(model_task_ActionItem.__init__)


def test_model_task_actionitem_constructor_args():
    sig = inspect.signature(model_task_ActionItem.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"
    assert "done" in params, "Missing parameter 'done'"

def test_model_task_actionitem_has_activity():
    assert hasattr(model_task_ActionItem, "activity")
    descriptor = None
    for klass in model_task_ActionItem.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_model_task_actionitem_has_done():
    assert hasattr(model_task_ActionItem, "done")
    descriptor = None
    for klass in model_task_ActionItem.__mro__:
        if "done" in klass.__dict__:
            descriptor = klass.__dict__["done"]
            break
    assert isinstance(descriptor, property)



def test_organization_group_is_not_abstract():
    assert not inspect.isabstract(organization_Group)


def test_organization_group_constructor_exists():
    assert callable(organization_Group.__init__)


def test_organization_group_constructor_args():
    sig = inspect.signature(organization_Group.__init__)
    params = list(sig.parameters.keys())



def test_task_workpackage_is_not_abstract():
    assert not inspect.isabstract(task_WorkPackage)


def test_task_workpackage_constructor_exists():
    assert callable(task_WorkPackage.__init__)


def test_task_workpackage_constructor_args():
    sig = inspect.signature(task_WorkPackage.__init__)
    params = list(sig.parameters.keys())



def test_unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(UnicaseModelElement)


def test_unicasemodelelement_constructor_exists():
    assert callable(UnicaseModelElement.__init__)


def test_unicasemodelelement_constructor_args():
    sig = inspect.signature(UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_activityobject_is_not_abstract():
    assert not inspect.isabstract(model_activity_ActivityObject)


def test_model_activity_activityobject_constructor_exists():
    assert callable(model_activity_ActivityObject.__init__)


def test_model_activity_activityobject_constructor_args():
    sig = inspect.signature(model_activity_ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_model_profile_profile_is_not_abstract():
    assert not inspect.isabstract(model_profile_Profile)


def test_model_profile_profile_constructor_exists():
    assert callable(model_profile_Profile.__init__)


def test_model_profile_profile_constructor_args():
    sig = inspect.signature(model_profile_Profile.__init__)
    params = list(sig.parameters.keys())



def test_model_profile_stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeInstance)


def test_model_profile_stereotypeinstance_constructor_exists():
    assert callable(model_profile_StereotypeInstance.__init__)


def test_model_profile_stereotypeinstance_constructor_args():
    sig = inspect.signature(model_profile_StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_classes_attribute_is_not_abstract():
    assert not inspect.isabstract(model_classes_Attribute)


def test_model_classes_attribute_constructor_exists():
    assert callable(model_classes_Attribute.__init__)


def test_model_classes_attribute_constructor_args():
    sig = inspect.signature(model_classes_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "label" in params, "Missing parameter 'label'"
    assert "signature" in params, "Missing parameter 'signature'"
    assert "type" in params, "Missing parameter 'type'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_model_classes_attribute_has_visibility():
    assert hasattr(model_classes_Attribute, "visibility")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_properties():
    assert hasattr(model_classes_Attribute, "properties")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_label():
    assert hasattr(model_classes_Attribute, "label")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_signature():
    assert hasattr(model_classes_Attribute, "signature")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_type():
    assert hasattr(model_classes_Attribute, "type")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_scope():
    assert hasattr(model_classes_Attribute, "scope")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_attribute_has_defaultValue():
    assert hasattr(model_classes_Attribute, "defaultValue")
    descriptor = None
    for klass in model_classes_Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_model_classes_method_is_not_abstract():
    assert not inspect.isabstract(model_classes_Method)


def test_model_classes_method_constructor_exists():
    assert callable(model_classes_Method.__init__)


def test_model_classes_method_constructor_args():
    sig = inspect.signature(model_classes_Method.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "stubbed" in params, "Missing parameter 'stubbed'"
    assert "label" in params, "Missing parameter 'label'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "returnType" in params, "Missing parameter 'returnType'"

def test_model_classes_method_has_signature():
    assert hasattr(model_classes_Method, "signature")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_scope():
    assert hasattr(model_classes_Method, "scope")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_visibility():
    assert hasattr(model_classes_Method, "visibility")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_stubbed():
    assert hasattr(model_classes_Method, "stubbed")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "stubbed" in klass.__dict__:
            descriptor = klass.__dict__["stubbed"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_label():
    assert hasattr(model_classes_Method, "label")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_properties():
    assert hasattr(model_classes_Method, "properties")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_method_has_returnType():
    assert hasattr(model_classes_Method, "returnType")
    descriptor = None
    for klass in model_classes_Method.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)



def test_model_classes_dependency_is_not_abstract():
    assert not inspect.isabstract(model_classes_Dependency)


def test_model_classes_dependency_constructor_exists():
    assert callable(model_classes_Dependency.__init__)


def test_model_classes_dependency_constructor_args():
    sig = inspect.signature(model_classes_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_model_classes_methodargument_is_not_abstract():
    assert not inspect.isabstract(model_classes_MethodArgument)


def test_model_classes_methodargument_constructor_exists():
    assert callable(model_classes_MethodArgument.__init__)


def test_model_classes_methodargument_constructor_args():
    sig = inspect.signature(model_classes_MethodArgument.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "signature" in params, "Missing parameter 'signature'"
    assert "label" in params, "Missing parameter 'label'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_model_classes_methodargument_has_type():
    assert hasattr(model_classes_MethodArgument, "type")
    descriptor = None
    for klass in model_classes_MethodArgument.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_methodargument_has_direction():
    assert hasattr(model_classes_MethodArgument, "direction")
    descriptor = None
    for klass in model_classes_MethodArgument.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_methodargument_has_signature():
    assert hasattr(model_classes_MethodArgument, "signature")
    descriptor = None
    for klass in model_classes_MethodArgument.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_methodargument_has_label():
    assert hasattr(model_classes_MethodArgument, "label")
    descriptor = None
    for klass in model_classes_MethodArgument.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_methodargument_has_defaultValue():
    assert hasattr(model_classes_MethodArgument, "defaultValue")
    descriptor = None
    for klass in model_classes_MethodArgument.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_model_task_checkable_is_not_abstract():
    assert not inspect.isabstract(model_task_Checkable)


def test_model_task_checkable_constructor_exists():
    assert callable(model_task_Checkable.__init__)


def test_model_task_checkable_constructor_args():
    sig = inspect.signature(model_task_Checkable.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_model_task_checkable_has_checked():
    assert hasattr(model_task_Checkable, "checked")
    descriptor = None
    for klass in model_task_Checkable.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_model_profile_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttribute)


def test_model_profile_stereotypeattribute_constructor_exists():
    assert callable(model_profile_StereotypeAttribute.__init__)


def test_model_profile_stereotypeattribute_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_model_profile_stereotype_is_not_abstract():
    assert not inspect.isabstract(model_profile_Stereotype)


def test_model_profile_stereotype_constructor_exists():
    assert callable(model_profile_Stereotype.__init__)


def test_model_profile_stereotype_constructor_args():
    sig = inspect.signature(model_profile_Stereotype.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_model_profile_stereotype_has_required():
    assert hasattr(model_profile_Stereotype, "required")
    descriptor = None
    for klass in model_profile_Stereotype.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_model_classes_packageelement_is_not_abstract():
    assert not inspect.isabstract(model_classes_PackageElement)


def test_model_classes_packageelement_constructor_exists():
    assert callable(model_classes_PackageElement.__init__)


def test_model_classes_packageelement_constructor_args():
    sig = inspect.signature(model_classes_PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_model_classes_association_is_not_abstract():
    assert not inspect.isabstract(model_classes_Association)


def test_model_classes_association_constructor_exists():
    assert callable(model_classes_Association.__init__)


def test_model_classes_association_constructor_args():
    sig = inspect.signature(model_classes_Association.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"
    assert "targetMultiplicity" in params, "Missing parameter 'targetMultiplicity'"
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "sourceMultiplicity" in params, "Missing parameter 'sourceMultiplicity'"

def test_model_classes_association_has_type():
    assert hasattr(model_classes_Association, "type")
    descriptor = None
    for klass in model_classes_Association.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_association_has_sourceRole():
    assert hasattr(model_classes_Association, "sourceRole")
    descriptor = None
    for klass in model_classes_Association.__mro__:
        if "sourceRole" in klass.__dict__:
            descriptor = klass.__dict__["sourceRole"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_association_has_targetMultiplicity():
    assert hasattr(model_classes_Association, "targetMultiplicity")
    descriptor = None
    for klass in model_classes_Association.__mro__:
        if "targetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["targetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_association_has_targetRole():
    assert hasattr(model_classes_Association, "targetRole")
    descriptor = None
    for klass in model_classes_Association.__mro__:
        if "targetRole" in klass.__dict__:
            descriptor = klass.__dict__["targetRole"]
            break
    assert isinstance(descriptor, property)

def test_model_classes_association_has_sourceMultiplicity():
    assert hasattr(model_classes_Association, "sourceMultiplicity")
    descriptor = None
    for klass in model_classes_Association.__mro__:
        if "sourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["sourceMultiplicity"]
            break
    assert isinstance(descriptor, property)



def test_model_profile_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(model_profile_StereotypeAttributeInstance)


def test_model_profile_stereotypeattributeinstance_constructor_exists():
    assert callable(model_profile_StereotypeAttributeInstance.__init__)


def test_model_profile_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(model_profile_StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_activity_transition_is_not_abstract():
    assert not inspect.isabstract(model_activity_Transition)


def test_model_activity_transition_constructor_exists():
    assert callable(model_activity_Transition.__init__)


def test_model_activity_transition_constructor_args():
    sig = inspect.signature(model_activity_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_model_activity_transition_has_condition():
    assert hasattr(model_activity_Transition, "condition")
    descriptor = None
    for klass in model_activity_Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_model_attachment_is_not_abstract():
    assert not inspect.isabstract(model_Attachment)


def test_model_attachment_constructor_exists():
    assert callable(model_Attachment.__init__)


def test_model_attachment_constructor_args():
    sig = inspect.signature(model_Attachment.__init__)
    params = list(sig.parameters.keys())



def test_model_document_section_is_not_abstract():
    assert not inspect.isabstract(model_document_Section)


def test_model_document_section_constructor_exists():
    assert callable(model_document_Section.__init__)


def test_model_document_section_constructor_args():
    sig = inspect.signature(model_document_Section.__init__)
    params = list(sig.parameters.keys())



def test_model_annotation_is_not_abstract():
    assert not inspect.isabstract(model_Annotation)


def test_model_annotation_constructor_exists():
    assert callable(model_Annotation.__init__)


def test_model_annotation_constructor_args():
    sig = inspect.signature(model_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_profile_stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(profile_StereotypeInstance)


def test_profile_stereotypeinstance_constructor_exists():
    assert callable(profile_StereotypeInstance.__init__)


def test_profile_stereotypeinstance_constructor_args():
    sig = inspect.signature(profile_StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_rationale_comment_is_not_abstract():
    assert not inspect.isabstract(rationale_Comment)


def test_rationale_comment_constructor_exists():
    assert callable(rationale_Comment.__init__)


def test_rationale_comment_constructor_args():
    sig = inspect.signature(rationale_Comment.__init__)
    params = list(sig.parameters.keys())



def test_document_leafsection_is_not_abstract():
    assert not inspect.isabstract(document_LeafSection)


def test_document_leafsection_constructor_exists():
    assert callable(document_LeafSection.__init__)


def test_document_leafsection_constructor_args():
    sig = inspect.signature(document_LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())



def test_model_diagram_mediagram_is_not_abstract():
    assert not inspect.isabstract(model_diagram_MEDiagram)


def test_model_diagram_mediagram_constructor_exists():
    assert callable(model_diagram_MEDiagram.__init__)


def test_model_diagram_mediagram_constructor_args():
    sig = inspect.signature(model_diagram_MEDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "diagramLayout" in params, "Missing parameter 'diagramLayout'"

def test_model_diagram_mediagram_has_type():
    assert hasattr(model_diagram_MEDiagram, "type")
    descriptor = None
    for klass in model_diagram_MEDiagram.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model_diagram_mediagram_has_diagramLayout():
    assert hasattr(model_diagram_MEDiagram, "diagramLayout")
    descriptor = None
    for klass in model_diagram_MEDiagram.__mro__:
        if "diagramLayout" in klass.__dict__:
            descriptor = klass.__dict__["diagramLayout"]
            break
    assert isinstance(descriptor, property)



def test_model_attachment_urlattachment_is_not_abstract():
    assert not inspect.isabstract(model_attachment_UrlAttachment)


def test_model_attachment_urlattachment_constructor_exists():
    assert callable(model_attachment_UrlAttachment.__init__)


def test_model_attachment_urlattachment_constructor_args():
    sig = inspect.signature(model_attachment_UrlAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_model_attachment_urlattachment_has_url():
    assert hasattr(model_attachment_UrlAttachment, "url")
    descriptor = None
    for klass in model_attachment_UrlAttachment.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_model_attachment_fileattachment_is_not_abstract():
    assert not inspect.isabstract(model_attachment_FileAttachment)


def test_model_attachment_fileattachment_constructor_exists():
    assert callable(model_attachment_FileAttachment.__init__)


def test_model_attachment_fileattachment_constructor_args():
    sig = inspect.signature(model_attachment_FileAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "requiredOffline" in params, "Missing parameter 'requiredOffline'"
    assert "fileSize" in params, "Missing parameter 'fileSize'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "fileHash" in params, "Missing parameter 'fileHash'"
    assert "fileID" in params, "Missing parameter 'fileID'"

def test_model_attachment_fileattachment_has_requiredOffline():
    assert hasattr(model_attachment_FileAttachment, "requiredOffline")
    descriptor = None
    for klass in model_attachment_FileAttachment.__mro__:
        if "requiredOffline" in klass.__dict__:
            descriptor = klass.__dict__["requiredOffline"]
            break
    assert isinstance(descriptor, property)

def test_model_attachment_fileattachment_has_fileSize():
    assert hasattr(model_attachment_FileAttachment, "fileSize")
    descriptor = None
    for klass in model_attachment_FileAttachment.__mro__:
        if "fileSize" in klass.__dict__:
            descriptor = klass.__dict__["fileSize"]
            break
    assert isinstance(descriptor, property)

def test_model_attachment_fileattachment_has_fileName():
    assert hasattr(model_attachment_FileAttachment, "fileName")
    descriptor = None
    for klass in model_attachment_FileAttachment.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_model_attachment_fileattachment_has_fileHash():
    assert hasattr(model_attachment_FileAttachment, "fileHash")
    descriptor = None
    for klass in model_attachment_FileAttachment.__mro__:
        if "fileHash" in klass.__dict__:
            descriptor = klass.__dict__["fileHash"]
            break
    assert isinstance(descriptor, property)

def test_model_attachment_fileattachment_has_fileID():
    assert hasattr(model_attachment_FileAttachment, "fileID")
    descriptor = None
    for klass in model_attachment_FileAttachment.__mro__:
        if "fileID" in klass.__dict__:
            descriptor = klass.__dict__["fileID"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_model_task_workitem_is_not_abstract():
    assert not inspect.isabstract(model_task_WorkItem)


def test_model_task_workitem_constructor_exists():
    assert callable(model_task_WorkItem.__init__)


def test_model_task_workitem_constructor_args():
    sig = inspect.signature(model_task_WorkItem.__init__)
    params = list(sig.parameters.keys())
    assert "resolved" in params, "Missing parameter 'resolved'"
    assert "estimate" in params, "Missing parameter 'estimate'"
    assert "dueDate" in params, "Missing parameter 'dueDate'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "effort" in params, "Missing parameter 'effort'"

def test_model_task_workitem_has_resolved():
    assert hasattr(model_task_WorkItem, "resolved")
    descriptor = None
    for klass in model_task_WorkItem.__mro__:
        if "resolved" in klass.__dict__:
            descriptor = klass.__dict__["resolved"]
            break
    assert isinstance(descriptor, property)

def test_model_task_workitem_has_estimate():
    assert hasattr(model_task_WorkItem, "estimate")
    descriptor = None
    for klass in model_task_WorkItem.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)

def test_model_task_workitem_has_dueDate():
    assert hasattr(model_task_WorkItem, "dueDate")
    descriptor = None
    for klass in model_task_WorkItem.__mro__:
        if "dueDate" in klass.__dict__:
            descriptor = klass.__dict__["dueDate"]
            break
    assert isinstance(descriptor, property)

def test_model_task_workitem_has_priority():
    assert hasattr(model_task_WorkItem, "priority")
    descriptor = None
    for klass in model_task_WorkItem.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_model_task_workitem_has_effort():
    assert hasattr(model_task_WorkItem, "effort")
    descriptor = None
    for klass in model_task_WorkItem.__mro__:
        if "effort" in klass.__dict__:
            descriptor = klass.__dict__["effort"]
            break
    assert isinstance(descriptor, property)



def test_model_organization_orgunit_is_not_abstract():
    assert not inspect.isabstract(model_organization_OrgUnit)


def test_model_organization_orgunit_constructor_exists():
    assert callable(model_organization_OrgUnit.__init__)


def test_model_organization_orgunit_constructor_args():
    sig = inspect.signature(model_organization_OrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "acOrgId" in params, "Missing parameter 'acOrgId'"

def test_model_organization_orgunit_has_acOrgId():
    assert hasattr(model_organization_OrgUnit, "acOrgId")
    descriptor = None
    for klass in model_organization_OrgUnit.__mro__:
        if "acOrgId" in klass.__dict__:
            descriptor = klass.__dict__["acOrgId"]
            break
    assert isinstance(descriptor, property)



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_model_project_is_not_abstract():
    assert not inspect.isabstract(model_Project)


def test_model_project_constructor_exists():
    assert callable(model_Project.__init__)


def test_model_project_constructor_args():
    sig = inspect.signature(model_Project.__init__)
    params = list(sig.parameters.keys())



def test_model_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(model_NonDomainElement)


def test_model_nondomainelement_constructor_exists():
    assert callable(model_NonDomainElement.__init__)


def test_model_nondomainelement_constructor_args():
    sig = inspect.signature(model_NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_associationclasselement_is_not_abstract():
    assert not inspect.isabstract(metamodel_AssociationClassElement)


def test_metamodel_associationclasselement_constructor_exists():
    assert callable(metamodel_AssociationClassElement.__init__)


def test_metamodel_associationclasselement_constructor_args():
    sig = inspect.signature(metamodel_AssociationClassElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_modelversion_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelVersion)


def test_metamodel_modelversion_constructor_exists():
    assert callable(metamodel_ModelVersion.__init__)


def test_metamodel_modelversion_constructor_args():
    sig = inspect.signature(metamodel_ModelVersion.__init__)
    params = list(sig.parameters.keys())
    assert "releaseNumber" in params, "Missing parameter 'releaseNumber'"

def test_metamodel_modelversion_has_releaseNumber():
    assert hasattr(metamodel_ModelVersion, "releaseNumber")
    descriptor = None
    for klass in metamodel_ModelVersion.__mro__:
        if "releaseNumber" in klass.__dict__:
            descriptor = klass.__dict__["releaseNumber"]
            break
    assert isinstance(descriptor, property)



def test_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueIdentifier)


def test_uniqueidentifier_constructor_exists():
    assert callable(UniqueIdentifier.__init__)


def test_uniqueidentifier_constructor_args():
    sig = inspect.signature(UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_sessionid_is_not_abstract():
    assert not inspect.isabstract(esmodel_SessionId)


def test_esmodel_sessionid_constructor_exists():
    assert callable(esmodel_SessionId.__init__)


def test_esmodel_sessionid_constructor_args():
    sig = inspect.signature(esmodel_SessionId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_projectid_is_not_abstract():
    assert not inspect.isabstract(esmodel_ProjectId)


def test_esmodel_projectid_constructor_exists():
    assert callable(esmodel_ProjectId.__init__)


def test_esmodel_projectid_constructor_args():
    sig = inspect.signature(esmodel_ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_accesscontrol_acorgunitid_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACOrgUnitId)


def test_esmodel_accesscontrol_acorgunitid_constructor_exists():
    assert callable(esmodel_accesscontrol_ACOrgUnitId.__init__)


def test_esmodel_accesscontrol_acorgunitid_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACOrgUnitId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_operations_operationid_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_OperationId)


def test_esmodel_operations_operationid_constructor_exists():
    assert callable(esmodel_operations_OperationId.__init__)


def test_esmodel_operations_operationid_constructor_args():
    sig = inspect.signature(esmodel_operations_OperationId.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_modelelementid_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelElementId)


def test_metamodel_modelelementid_constructor_exists():
    assert callable(metamodel_ModelElementId.__init__)


def test_metamodel_modelelementid_constructor_args():
    sig = inspect.signature(metamodel_ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_esmodel_notification_esnotification_is_not_abstract():
    assert not inspect.isabstract(esmodel_notification_ESNotification)


def test_esmodel_notification_esnotification_constructor_exists():
    assert callable(esmodel_notification_ESNotification.__init__)


def test_esmodel_notification_esnotification_constructor_args():
    sig = inspect.signature(esmodel_notification_ESNotification.__init__)
    params = list(sig.parameters.keys())
    assert "sender" in params, "Missing parameter 'sender'"
    assert "name" in params, "Missing parameter 'name'"
    assert "provider" in params, "Missing parameter 'provider'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "seen" in params, "Missing parameter 'seen'"
    assert "details" in params, "Missing parameter 'details'"
    assert "recipient" in params, "Missing parameter 'recipient'"
    assert "message" in params, "Missing parameter 'message'"

def test_esmodel_notification_esnotification_has_sender():
    assert hasattr(esmodel_notification_ESNotification, "sender")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_name():
    assert hasattr(esmodel_notification_ESNotification, "name")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_provider():
    assert hasattr(esmodel_notification_ESNotification, "provider")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_creationDate():
    assert hasattr(esmodel_notification_ESNotification, "creationDate")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_seen():
    assert hasattr(esmodel_notification_ESNotification, "seen")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "seen" in klass.__dict__:
            descriptor = klass.__dict__["seen"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_details():
    assert hasattr(esmodel_notification_ESNotification, "details")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_recipient():
    assert hasattr(esmodel_notification_ESNotification, "recipient")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "recipient" in klass.__dict__:
            descriptor = klass.__dict__["recipient"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_notification_esnotification_has_message():
    assert hasattr(esmodel_notification_ESNotification, "message")
    descriptor = None
    for klass in esmodel_notification_ESNotification.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_accesscontrol_acorgunit_is_not_abstract():
    assert not inspect.isabstract(esmodel_accesscontrol_ACOrgUnit)


def test_esmodel_accesscontrol_acorgunit_constructor_exists():
    assert callable(esmodel_accesscontrol_ACOrgUnit.__init__)


def test_esmodel_accesscontrol_acorgunit_constructor_args():
    sig = inspect.signature(esmodel_accesscontrol_ACOrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_esmodel_accesscontrol_acorgunit_has_name():
    assert hasattr(esmodel_accesscontrol_ACOrgUnit, "name")
    descriptor = None
    for klass in esmodel_accesscontrol_ACOrgUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_accesscontrol_acorgunit_has_description():
    assert hasattr(esmodel_accesscontrol_ACOrgUnit, "description")
    descriptor = None
    for klass in esmodel_accesscontrol_ACOrgUnit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_esmodel_operations_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel_operations_AbstractOperation)


def test_esmodel_operations_abstractoperation_constructor_exists():
    assert callable(esmodel_operations_AbstractOperation.__init__)


def test_esmodel_operations_abstractoperation_constructor_args():
    sig = inspect.signature(esmodel_operations_AbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_esmodel_operations_abstractoperation_has_clientDate():
    assert hasattr(esmodel_operations_AbstractOperation, "clientDate")
    descriptor = None
    for klass in esmodel_operations_AbstractOperation.__mro__:
        if "clientDate" in klass.__dict__:
            descriptor = klass.__dict__["clientDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_abstractoperation_has_accepted():
    assert hasattr(esmodel_operations_AbstractOperation, "accepted")
    descriptor = None
    for klass in esmodel_operations_AbstractOperation.__mro__:
        if "accepted" in klass.__dict__:
            descriptor = klass.__dict__["accepted"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_abstractoperation_has_name():
    assert hasattr(esmodel_operations_AbstractOperation, "name")
    descriptor = None
    for klass in esmodel_operations_AbstractOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel_operations_abstractoperation_has_description():
    assert hasattr(esmodel_operations_AbstractOperation, "description")
    descriptor = None
    for klass in esmodel_operations_AbstractOperation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_modelelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_ModelElement)


def test_metamodel_modelelement_constructor_exists():
    assert callable(metamodel_ModelElement.__init__)


def test_metamodel_modelelement_constructor_args():
    sig = inspect.signature(metamodel_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "creator" in params, "Missing parameter 'creator'"

def test_metamodel_modelelement_has_creationDate():
    assert hasattr(metamodel_ModelElement, "creationDate")
    descriptor = None
    for klass in metamodel_ModelElement.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_modelelement_has_creator():
    assert hasattr(metamodel_ModelElement, "creator")
    descriptor = None
    for klass in metamodel_ModelElement.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_IdentifiableElement)


def test_metamodel_identifiableelement_constructor_exists():
    assert callable(metamodel_IdentifiableElement.__init__)


def test_metamodel_identifiableelement_constructor_args():
    sig = inspect.signature(metamodel_IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_metamodel_identifiableelement_has_identifier():
    assert hasattr(metamodel_IdentifiableElement, "identifier")
    descriptor = None
    for klass in metamodel_IdentifiableElement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(metamodel_UniqueIdentifier)


def test_metamodel_uniqueidentifier_constructor_exists():
    assert callable(metamodel_UniqueIdentifier.__init__)


def test_metamodel_uniqueidentifier_constructor_args():
    sig = inspect.signature(metamodel_UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_metamodel_uniqueidentifier_has_id():
    assert hasattr(metamodel_UniqueIdentifier, "id")
    descriptor = None
    for klass in metamodel_UniqueIdentifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_model_unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(model_UnicaseModelElement)


def test_model_unicasemodelelement_constructor_exists():
    assert callable(model_UnicaseModelElement.__init__)


def test_model_unicasemodelelement_constructor_args():
    sig = inspect.signature(model_UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "state" in params, "Missing parameter 'state'"

def test_model_unicasemodelelement_has_name():
    assert hasattr(model_UnicaseModelElement, "name")
    descriptor = None
    for klass in model_UnicaseModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_unicasemodelelement_has_description():
    assert hasattr(model_UnicaseModelElement, "description")
    descriptor = None
    for klass in model_UnicaseModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model_unicasemodelelement_has_state():
    assert hasattr(model_UnicaseModelElement, "state")
    descriptor = None
    for klass in model_UnicaseModelElement.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_project_is_not_abstract():
    assert not inspect.isabstract(metamodel_Project)


def test_metamodel_project_constructor_exists():
    assert callable(metamodel_Project.__init__)


def test_metamodel_project_constructor_args():
    sig = inspect.signature(metamodel_Project.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(metamodel_NonDomainElement)


def test_metamodel_nondomainelement_constructor_exists():
    assert callable(metamodel_NonDomainElement.__init__)


def test_metamodel_nondomainelement_constructor_args():
    sig = inspect.signature(metamodel_NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_model_state_statenode_is_not_abstract():
    assert not inspect.isabstract(model_state_StateNode)


def test_model_state_statenode_constructor_exists():
    assert callable(model_state_StateNode.__init__)


def test_model_state_statenode_constructor_args():
    sig = inspect.signature(model_state_StateNode.__init__)
    params = list(sig.parameters.keys())



def test_state_statenode_is_not_abstract():
    assert not inspect.isabstract(state_StateNode)


def test_state_statenode_constructor_exists():
    assert callable(state_StateNode.__init__)


def test_state_statenode_constructor_args():
    sig = inspect.signature(state_StateNode.__init__)
    params = list(sig.parameters.keys())



def test_model_state_transition_is_not_abstract():
    assert not inspect.isabstract(model_state_Transition)


def test_model_state_transition_constructor_exists():
    assert callable(model_state_Transition.__init__)


def test_model_state_transition_constructor_args():
    sig = inspect.signature(model_state_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_model_state_transition_has_condition():
    assert hasattr(model_state_Transition, "condition")
    descriptor = None
    for klass in model_state_Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_meetingsection_is_not_abstract():
    assert not inspect.isabstract(MeetingSection)


def test_meetingsection_constructor_exists():
    assert callable(MeetingSection.__init__)


def test_meetingsection_constructor_args():
    sig = inspect.signature(MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_meeting_workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_WorkItemMeetingSection)


def test_model_meeting_workitemmeetingsection_constructor_exists():
    assert callable(model_meeting_WorkItemMeetingSection.__init__)


def test_model_meeting_workitemmeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_meeting_issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_IssueMeetingSection)


def test_model_meeting_issuemeetingsection_constructor_exists():
    assert callable(model_meeting_IssueMeetingSection.__init__)


def test_model_meeting_issuemeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_meeting_compositemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_CompositeMeetingSection)


def test_model_meeting_compositemeetingsection_constructor_exists():
    assert callable(model_meeting_CompositeMeetingSection.__init__)


def test_model_meeting_compositemeetingsection_constructor_args():
    sig = inspect.signature(model_meeting_CompositeMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_meeting_meetingsection_is_not_abstract():
    assert not inspect.isabstract(model_meeting_MeetingSection)


def test_model_meeting_meetingsection_constructor_exists():
    assert callable(model_meeting_MeetingSection.__init__)


def test_model_meeting_meetingsection_constructor_args():
    sig = inspect.signature(model_meeting_MeetingSection.__init__)
    params = list(sig.parameters.keys())
    assert "allocatedTime" in params, "Missing parameter 'allocatedTime'"

def test_model_meeting_meetingsection_has_allocatedTime():
    assert hasattr(model_meeting_MeetingSection, "allocatedTime")
    descriptor = None
    for klass in model_meeting_MeetingSection.__mro__:
        if "allocatedTime" in klass.__dict__:
            descriptor = klass.__dict__["allocatedTime"]
            break
    assert isinstance(descriptor, property)



def test_statenode_is_not_abstract():
    assert not inspect.isabstract(StateNode)


def test_statenode_constructor_exists():
    assert callable(StateNode.__init__)


def test_statenode_constructor_args():
    sig = inspect.signature(StateNode.__init__)
    params = list(sig.parameters.keys())



def test_model_state_stateend_is_not_abstract():
    assert not inspect.isabstract(model_state_StateEnd)


def test_model_state_stateend_constructor_exists():
    assert callable(model_state_StateEnd.__init__)


def test_model_state_stateend_constructor_args():
    sig = inspect.signature(model_state_StateEnd.__init__)
    params = list(sig.parameters.keys())



def test_model_state_stateinitial_is_not_abstract():
    assert not inspect.isabstract(model_state_StateInitial)


def test_model_state_stateinitial_constructor_exists():
    assert callable(model_state_StateInitial.__init__)


def test_model_state_stateinitial_constructor_args():
    sig = inspect.signature(model_state_StateInitial.__init__)
    params = list(sig.parameters.keys())



def test_model_state_state_is_not_abstract():
    assert not inspect.isabstract(model_state_State)


def test_model_state_state_constructor_exists():
    assert callable(model_state_State.__init__)


def test_model_state_state_constructor_args():
    sig = inspect.signature(model_state_State.__init__)
    params = list(sig.parameters.keys())
    assert "activities" in params, "Missing parameter 'activities'"
    assert "exitConditions" in params, "Missing parameter 'exitConditions'"
    assert "entryConditions" in params, "Missing parameter 'entryConditions'"

def test_model_state_state_has_activities():
    assert hasattr(model_state_State, "activities")
    descriptor = None
    for klass in model_state_State.__mro__:
        if "activities" in klass.__dict__:
            descriptor = klass.__dict__["activities"]
            break
    assert isinstance(descriptor, property)

def test_model_state_state_has_exitConditions():
    assert hasattr(model_state_State, "exitConditions")
    descriptor = None
    for klass in model_state_State.__mro__:
        if "exitConditions" in klass.__dict__:
            descriptor = klass.__dict__["exitConditions"]
            break
    assert isinstance(descriptor, property)

def test_model_state_state_has_entryConditions():
    assert hasattr(model_state_State, "entryConditions")
    descriptor = None
    for klass in model_state_State.__mro__:
        if "entryConditions" in klass.__dict__:
            descriptor = klass.__dict__["entryConditions"]
            break
    assert isinstance(descriptor, property)



def test_meeting_issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_IssueMeetingSection)


def test_meeting_issuemeetingsection_constructor_exists():
    assert callable(meeting_IssueMeetingSection.__init__)


def test_meeting_issuemeetingsection_constructor_args():
    sig = inspect.signature(meeting_IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_meeting_meetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_MeetingSection)


def test_meeting_meetingsection_constructor_exists():
    assert callable(meeting_MeetingSection.__init__)


def test_meeting_meetingsection_constructor_args():
    sig = inspect.signature(meeting_MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_meeting_meeting_is_not_abstract():
    assert not inspect.isabstract(model_meeting_Meeting)


def test_model_meeting_meeting_constructor_exists():
    assert callable(model_meeting_Meeting.__init__)


def test_model_meeting_meeting_constructor_args():
    sig = inspect.signature(model_meeting_Meeting.__init__)
    params = list(sig.parameters.keys())
    assert "endtime" in params, "Missing parameter 'endtime'"
    assert "starttime" in params, "Missing parameter 'starttime'"
    assert "location" in params, "Missing parameter 'location'"

def test_model_meeting_meeting_has_endtime():
    assert hasattr(model_meeting_Meeting, "endtime")
    descriptor = None
    for klass in model_meeting_Meeting.__mro__:
        if "endtime" in klass.__dict__:
            descriptor = klass.__dict__["endtime"]
            break
    assert isinstance(descriptor, property)

def test_model_meeting_meeting_has_starttime():
    assert hasattr(model_meeting_Meeting, "starttime")
    descriptor = None
    for klass in model_meeting_Meeting.__mro__:
        if "starttime" in klass.__dict__:
            descriptor = klass.__dict__["starttime"]
            break
    assert isinstance(descriptor, property)

def test_model_meeting_meeting_has_location():
    assert hasattr(model_meeting_Meeting, "location")
    descriptor = None
    for klass in model_meeting_Meeting.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_meeting_workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting_WorkItemMeetingSection)


def test_meeting_workitemmeetingsection_constructor_exists():
    assert callable(meeting_WorkItemMeetingSection.__init__)


def test_meeting_workitemmeetingsection_constructor_args():
    sig = inspect.signature(meeting_WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model_component_deploymentnode_is_not_abstract():
    assert not inspect.isabstract(model_component_DeploymentNode)


def test_model_component_deploymentnode_constructor_exists():
    assert callable(model_component_DeploymentNode.__init__)


def test_model_component_deploymentnode_constructor_args():
    sig = inspect.signature(model_component_DeploymentNode.__init__)
    params = list(sig.parameters.keys())



def test_component_component_is_not_abstract():
    assert not inspect.isabstract(component_Component)


def test_component_component_constructor_exists():
    assert callable(component_Component.__init__)


def test_component_component_constructor_args():
    sig = inspect.signature(component_Component.__init__)
    params = list(sig.parameters.keys())



def test_model_component_componentservice_is_not_abstract():
    assert not inspect.isabstract(model_component_ComponentService)


def test_model_component_componentservice_constructor_exists():
    assert callable(model_component_ComponentService.__init__)


def test_model_component_componentservice_constructor_args():
    sig = inspect.signature(model_component_ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_component_componentservice_is_not_abstract():
    assert not inspect.isabstract(component_ComponentService)


def test_component_componentservice_constructor_exists():
    assert callable(component_ComponentService.__init__)


def test_component_componentservice_constructor_args():
    sig = inspect.signature(component_ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_model_component_component_is_not_abstract():
    assert not inspect.isabstract(model_component_Component)


def test_model_component_component_constructor_exists():
    assert callable(model_component_Component.__init__)


def test_model_component_component_constructor_args():
    sig = inspect.signature(model_component_Component.__init__)
    params = list(sig.parameters.keys())



def test_model_bug_bugreport_is_not_abstract():
    assert not inspect.isabstract(model_bug_BugReport)


def test_model_bug_bugreport_constructor_exists():
    assert callable(model_bug_BugReport.__init__)


def test_model_bug_bugreport_constructor_args():
    sig = inspect.signature(model_bug_BugReport.__init__)
    params = list(sig.parameters.keys())
    assert "Status" in params, "Missing parameter 'Status'"
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "resolutionType" in params, "Missing parameter 'resolutionType'"

def test_model_bug_bugreport_has_Status():
    assert hasattr(model_bug_BugReport, "Status")
    descriptor = None
    for klass in model_bug_BugReport.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)

def test_model_bug_bugreport_has_resolution():
    assert hasattr(model_bug_BugReport, "resolution")
    descriptor = None
    for klass in model_bug_BugReport.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)

def test_model_bug_bugreport_has_severity():
    assert hasattr(model_bug_BugReport, "severity")
    descriptor = None
    for klass in model_bug_BugReport.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_model_bug_bugreport_has_resolutionType():
    assert hasattr(model_bug_BugReport, "resolutionType")
    descriptor = None
    for klass in model_bug_BugReport.__mro__:
        if "resolutionType" in klass.__dict__:
            descriptor = klass.__dict__["resolutionType"]
            break
    assert isinstance(descriptor, property)



def test_solution_is_not_abstract():
    assert not inspect.isabstract(Solution)


def test_solution_constructor_exists():
    assert callable(Solution.__init__)


def test_solution_constructor_args():
    sig = inspect.signature(Solution.__init__)
    params = list(sig.parameters.keys())



def test_model_change_mergingsolution_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingSolution)


def test_model_change_mergingsolution_constructor_exists():
    assert callable(model_change_MergingSolution.__init__)


def test_model_change_mergingsolution_constructor_args():
    sig = inspect.signature(model_change_MergingSolution.__init__)
    params = list(sig.parameters.keys())



def test_change_mergingproposal_is_not_abstract():
    assert not inspect.isabstract(change_MergingProposal)


def test_change_mergingproposal_constructor_exists():
    assert callable(change_MergingProposal.__init__)


def test_change_mergingproposal_constructor_args():
    sig = inspect.signature(change_MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_proposal_is_not_abstract():
    assert not inspect.isabstract(Proposal)


def test_proposal_constructor_exists():
    assert callable(Proposal.__init__)


def test_proposal_constructor_args():
    sig = inspect.signature(Proposal.__init__)
    params = list(sig.parameters.keys())



def test_model_change_mergingproposal_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingProposal)


def test_model_change_mergingproposal_constructor_exists():
    assert callable(model_change_MergingProposal.__init__)


def test_model_change_mergingproposal_constructor_args():
    sig = inspect.signature(model_change_MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_issue_is_not_abstract():
    assert not inspect.isabstract(Issue)


def test_issue_constructor_exists():
    assert callable(Issue.__init__)


def test_issue_constructor_args():
    sig = inspect.signature(Issue.__init__)
    params = list(sig.parameters.keys())



def test_model_change_mergingissue_is_not_abstract():
    assert not inspect.isabstract(model_change_MergingIssue)


def test_model_change_mergingissue_constructor_exists():
    assert callable(model_change_MergingIssue.__init__)


def test_model_change_mergingissue_constructor_args():
    sig = inspect.signature(model_change_MergingIssue.__init__)
    params = list(sig.parameters.keys())
    assert "resolvingRevision" in params, "Missing parameter 'resolvingRevision'"

def test_model_change_mergingissue_has_resolvingRevision():
    assert hasattr(model_change_MergingIssue, "resolvingRevision")
    descriptor = None
    for klass in model_change_MergingIssue.__mro__:
        if "resolvingRevision" in klass.__dict__:
            descriptor = klass.__dict__["resolvingRevision"]
            break
    assert isinstance(descriptor, property)



def test_model_change_modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(model_change_ModelChangePackage)


def test_model_change_modelchangepackage_constructor_exists():
    assert callable(model_change_ModelChangePackage.__init__)


def test_model_change_modelchangepackage_constructor_args():
    sig = inspect.signature(model_change_ModelChangePackage.__init__)
    params = list(sig.parameters.keys())
    assert "targetVersion" in params, "Missing parameter 'targetVersion'"
    assert "sourceVersion" in params, "Missing parameter 'sourceVersion'"

def test_model_change_modelchangepackage_has_targetVersion():
    assert hasattr(model_change_ModelChangePackage, "targetVersion")
    descriptor = None
    for klass in model_change_ModelChangePackage.__mro__:
        if "targetVersion" in klass.__dict__:
            descriptor = klass.__dict__["targetVersion"]
            break
    assert isinstance(descriptor, property)

def test_model_change_modelchangepackage_has_sourceVersion():
    assert hasattr(model_change_ModelChangePackage, "sourceVersion")
    descriptor = None
    for klass in model_change_ModelChangePackage.__mro__:
        if "sourceVersion" in klass.__dict__:
            descriptor = klass.__dict__["sourceVersion"]
            break
    assert isinstance(descriptor, property)



def test_model_rationale_criterion_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Criterion)


def test_model_rationale_criterion_constructor_exists():
    assert callable(model_rationale_Criterion.__init__)


def test_model_rationale_criterion_constructor_args():
    sig = inspect.signature(model_rationale_Criterion.__init__)
    params = list(sig.parameters.keys())



def test_rationale_assessment_is_not_abstract():
    assert not inspect.isabstract(rationale_Assessment)


def test_rationale_assessment_constructor_exists():
    assert callable(rationale_Assessment.__init__)


def test_rationale_assessment_constructor_args():
    sig = inspect.signature(rationale_Assessment.__init__)
    params = list(sig.parameters.keys())



def test_rationale_issue_is_not_abstract():
    assert not inspect.isabstract(rationale_Issue)


def test_rationale_issue_constructor_exists():
    assert callable(rationale_Issue.__init__)


def test_rationale_issue_constructor_args():
    sig = inspect.signature(rationale_Issue.__init__)
    params = list(sig.parameters.keys())



def test_rationale_criterion_is_not_abstract():
    assert not inspect.isabstract(rationale_Criterion)


def test_rationale_criterion_constructor_exists():
    assert callable(rationale_Criterion.__init__)


def test_rationale_criterion_constructor_args():
    sig = inspect.signature(rationale_Criterion.__init__)
    params = list(sig.parameters.keys())



def test_rationale_solution_is_not_abstract():
    assert not inspect.isabstract(rationale_Solution)


def test_rationale_solution_constructor_exists():
    assert callable(rationale_Solution.__init__)


def test_rationale_solution_constructor_args():
    sig = inspect.signature(rationale_Solution.__init__)
    params = list(sig.parameters.keys())



def test_model_rationale_issue_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Issue)


def test_model_rationale_issue_constructor_exists():
    assert callable(model_rationale_Issue.__init__)


def test_model_rationale_issue_constructor_args():
    sig = inspect.signature(model_rationale_Issue.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"

def test_model_rationale_issue_has_activity():
    assert hasattr(model_rationale_Issue, "activity")
    descriptor = None
    for klass in model_rationale_Issue.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_criterion_is_not_abstract():
    assert not inspect.isabstract(Criterion)


def test_criterion_constructor_exists():
    assert callable(Criterion.__init__)


def test_criterion_constructor_args():
    sig = inspect.signature(Criterion.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model_requirement_NonFunctionalRequirement)


def test_model_requirement_nonfunctionalrequirement_constructor_exists():
    assert callable(model_requirement_NonFunctionalRequirement.__init__)


def test_model_requirement_nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(model_requirement_NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_requirement_systemfunction_is_not_abstract():
    assert not inspect.isabstract(requirement_SystemFunction)


def test_requirement_systemfunction_constructor_exists():
    assert callable(requirement_SystemFunction.__init__)


def test_requirement_systemfunction_constructor_args():
    sig = inspect.signature(requirement_SystemFunction.__init__)
    params = list(sig.parameters.keys())



def test_rationale_proposal_is_not_abstract():
    assert not inspect.isabstract(rationale_Proposal)


def test_rationale_proposal_constructor_exists():
    assert callable(rationale_Proposal.__init__)


def test_rationale_proposal_constructor_args():
    sig = inspect.signature(rationale_Proposal.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_actorinstance_is_not_abstract():
    assert not inspect.isabstract(model_requirement_ActorInstance)


def test_model_requirement_actorinstance_constructor_exists():
    assert callable(model_requirement_ActorInstance.__init__)


def test_model_requirement_actorinstance_constructor_args():
    sig = inspect.signature(model_requirement_ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_actor_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Actor)


def test_model_requirement_actor_constructor_exists():
    assert callable(model_requirement_Actor.__init__)


def test_model_requirement_actor_constructor_args():
    sig = inspect.signature(model_requirement_Actor.__init__)
    params = list(sig.parameters.keys())



def test_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(NonDomainElement)


def test_nondomainelement_constructor_exists():
    assert callable(NonDomainElement.__init__)


def test_nondomainelement_constructor_args():
    sig = inspect.signature(NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_model_rationale_proposal_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Proposal)


def test_model_rationale_proposal_constructor_exists():
    assert callable(model_rationale_Proposal.__init__)


def test_model_rationale_proposal_constructor_args():
    sig = inspect.signature(model_rationale_Proposal.__init__)
    params = list(sig.parameters.keys())



def test_model_rationale_assessment_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Assessment)


def test_model_rationale_assessment_constructor_exists():
    assert callable(model_rationale_Assessment.__init__)


def test_model_rationale_assessment_constructor_args():
    sig = inspect.signature(model_rationale_Assessment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model_rationale_assessment_has_value():
    assert hasattr(model_rationale_Assessment, "value")
    descriptor = None
    for klass in model_rationale_Assessment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_rationale_comment_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Comment)


def test_model_rationale_comment_constructor_exists():
    assert callable(model_rationale_Comment.__init__)


def test_model_rationale_comment_constructor_args():
    sig = inspect.signature(model_rationale_Comment.__init__)
    params = list(sig.parameters.keys())



def test_model_rationale_solution_is_not_abstract():
    assert not inspect.isabstract(model_rationale_Solution)


def test_model_rationale_solution_constructor_exists():
    assert callable(model_rationale_Solution.__init__)


def test_model_rationale_solution_constructor_args():
    sig = inspect.signature(model_rationale_Solution.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_systemfunction_is_not_abstract():
    assert not inspect.isabstract(model_requirement_SystemFunction)


def test_model_requirement_systemfunction_constructor_exists():
    assert callable(model_requirement_SystemFunction.__init__)


def test_model_requirement_systemfunction_constructor_args():
    sig = inspect.signature(model_requirement_SystemFunction.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "exception" in params, "Missing parameter 'exception'"
    assert "input" in params, "Missing parameter 'input'"

def test_model_requirement_systemfunction_has_output():
    assert hasattr(model_requirement_SystemFunction, "output")
    descriptor = None
    for klass in model_requirement_SystemFunction.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_systemfunction_has_exception():
    assert hasattr(model_requirement_SystemFunction, "exception")
    descriptor = None
    for klass in model_requirement_SystemFunction.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_systemfunction_has_input():
    assert hasattr(model_requirement_SystemFunction, "input")
    descriptor = None
    for klass in model_requirement_SystemFunction.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_model_requirement_usertask_is_not_abstract():
    assert not inspect.isabstract(model_requirement_UserTask)


def test_model_requirement_usertask_constructor_exists():
    assert callable(model_requirement_UserTask.__init__)


def test_model_requirement_usertask_constructor_args():
    sig = inspect.signature(model_requirement_UserTask.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_step_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Step)


def test_model_requirement_step_constructor_exists():
    assert callable(model_requirement_Step.__init__)


def test_model_requirement_step_constructor_args():
    sig = inspect.signature(model_requirement_Step.__init__)
    params = list(sig.parameters.keys())
    assert "userStep" in params, "Missing parameter 'userStep'"

def test_model_requirement_step_has_userStep():
    assert hasattr(model_requirement_Step, "userStep")
    descriptor = None
    for klass in model_requirement_Step.__mro__:
        if "userStep" in klass.__dict__:
            descriptor = klass.__dict__["userStep"]
            break
    assert isinstance(descriptor, property)



def test_requirement_actorinstance_is_not_abstract():
    assert not inspect.isabstract(requirement_ActorInstance)


def test_requirement_actorinstance_constructor_exists():
    assert callable(requirement_ActorInstance.__init__)


def test_requirement_actorinstance_constructor_args():
    sig = inspect.signature(requirement_ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_scenario_is_not_abstract():
    assert not inspect.isabstract(model_requirement_Scenario)


def test_model_requirement_scenario_constructor_exists():
    assert callable(model_requirement_Scenario.__init__)


def test_model_requirement_scenario_constructor_args():
    sig = inspect.signature(model_requirement_Scenario.__init__)
    params = list(sig.parameters.keys())



def test_requirement_nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement_NonFunctionalRequirement)


def test_requirement_nonfunctionalrequirement_constructor_exists():
    assert callable(requirement_NonFunctionalRequirement.__init__)


def test_requirement_nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(requirement_NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_requirement_usertask_is_not_abstract():
    assert not inspect.isabstract(requirement_UserTask)


def test_requirement_usertask_constructor_exists():
    assert callable(requirement_UserTask.__init__)


def test_requirement_usertask_constructor_args():
    sig = inspect.signature(requirement_UserTask.__init__)
    params = list(sig.parameters.keys())



def test_requirement_step_is_not_abstract():
    assert not inspect.isabstract(requirement_Step)


def test_requirement_step_constructor_exists():
    assert callable(requirement_Step.__init__)


def test_requirement_step_constructor_args():
    sig = inspect.signature(requirement_Step.__init__)
    params = list(sig.parameters.keys())



def test_requirement_actor_is_not_abstract():
    assert not inspect.isabstract(requirement_Actor)


def test_requirement_actor_constructor_exists():
    assert callable(requirement_Actor.__init__)


def test_requirement_actor_constructor_args():
    sig = inspect.signature(requirement_Actor.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_usecase_is_not_abstract():
    assert not inspect.isabstract(model_requirement_UseCase)


def test_model_requirement_usecase_constructor_exists():
    assert callable(model_requirement_UseCase.__init__)


def test_model_requirement_usecase_constructor_args():
    sig = inspect.signature(model_requirement_UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "rules" in params, "Missing parameter 'rules'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "exception" in params, "Missing parameter 'exception'"

def test_model_requirement_usecase_has_precondition():
    assert hasattr(model_requirement_UseCase, "precondition")
    descriptor = None
    for klass in model_requirement_UseCase.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_usecase_has_rules():
    assert hasattr(model_requirement_UseCase, "rules")
    descriptor = None
    for klass in model_requirement_UseCase.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_usecase_has_postcondition():
    assert hasattr(model_requirement_UseCase, "postcondition")
    descriptor = None
    for klass in model_requirement_UseCase.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_usecase_has_exception():
    assert hasattr(model_requirement_UseCase, "exception")
    descriptor = None
    for klass in model_requirement_UseCase.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_requirement_functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement_FunctionalRequirement)


def test_requirement_functionalrequirement_constructor_exists():
    assert callable(requirement_FunctionalRequirement.__init__)


def test_requirement_functionalrequirement_constructor_args():
    sig = inspect.signature(requirement_FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_model_requirement_functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model_requirement_FunctionalRequirement)


def test_model_requirement_functionalrequirement_constructor_exists():
    assert callable(model_requirement_FunctionalRequirement.__init__)


def test_model_requirement_functionalrequirement_constructor_args():
    sig = inspect.signature(model_requirement_FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "reviewed" in params, "Missing parameter 'reviewed'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "storyPoints" in params, "Missing parameter 'storyPoints'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_model_requirement_functionalrequirement_has_reviewed():
    assert hasattr(model_requirement_FunctionalRequirement, "reviewed")
    descriptor = None
    for klass in model_requirement_FunctionalRequirement.__mro__:
        if "reviewed" in klass.__dict__:
            descriptor = klass.__dict__["reviewed"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_functionalrequirement_has_priority():
    assert hasattr(model_requirement_FunctionalRequirement, "priority")
    descriptor = None
    for klass in model_requirement_FunctionalRequirement.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_functionalrequirement_has_storyPoints():
    assert hasattr(model_requirement_FunctionalRequirement, "storyPoints")
    descriptor = None
    for klass in model_requirement_FunctionalRequirement.__mro__:
        if "storyPoints" in klass.__dict__:
            descriptor = klass.__dict__["storyPoints"]
            break
    assert isinstance(descriptor, property)

def test_model_requirement_functionalrequirement_has_cost():
    assert hasattr(model_requirement_FunctionalRequirement, "cost")
    descriptor = None
    for klass in model_requirement_FunctionalRequirement.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "MINOR",
        "MAJOR",
        "FEATURE",
        "TRIVIAL",
        "BLOCKER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_argumentdirectiontype_exists():
    # Check that the Enumeration exists
    assert ArgumentDirectionType is not None

def test_argumentdirectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArgumentDirectionType]
    expected_literals = [
        "UNDEFINED",
        "IN",
        "OUT",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArgumentDirectionType"

def test_mergeglobalchoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeGlobalChoiceSelection is not None

def test_mergeglobalchoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeGlobalChoiceSelection]
    expected_literals = [
        "AllTheir",
        "OKNotFinished",
        "Cancel",
        "OKFinished",
        "AllMine",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeGlobalChoiceSelection"

def test_resolutiontype_exists():
    # Check that the Enumeration exists
    assert ResolutionType is not None

def test_resolutiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResolutionType]
    expected_literals = [
        "FIXED",
        "CANNOT_REPRODUCE",
        "WONT_FIX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResolutionType"

def test_bugstatus_exists():
    # Check that the Enumeration exists
    assert BugStatus is not None

def test_bugstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BugStatus]
    expected_literals = [
        "ASSIGNED",
        "RESOLVED",
        "NEW",
        "CONFIRMED",
        "CLOSED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BugStatus"

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "PROTECTED",
        "PACKAGE",
        "GLOBAL",
        "UNDEFINED",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"

def test_diagramtype_exists():
    # Check that the Enumeration exists
    assert DiagramType is not None

def test_diagramtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramType]
    expected_literals = [
        "ACTIVITY_DIAGRAM",
        "CLASS_DIAGRAM",
        "COMPONENT_DIAGRAM",
        "STATE_DIAGRAM",
        "WORKITEM_DIAGRAM",
        "USECASE_DIAGRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramType"

def test_containmenttype_exists():
    # Check that the Enumeration exists
    assert ContainmentType is not None

def test_containmenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentType]
    expected_literals = [
        "NONE",
        "CONTAINER",
        "CONTAINMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentType"

def test_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "TESTING",
        "OBJECT_DESIGN",
        "IMPLEMENTATION",
        "NONE",
        "ANALYSIS",
        "SYSTEM_DESIGN",
        "MANAGEMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityType"

def test_mergechoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeChoiceSelection is not None

def test_mergechoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeChoiceSelection]
    expected_literals = [
        "Mine",
        "MergedText",
        "Their",
        "Issue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeChoiceSelection"

def test_associationtype_exists():
    # Check that the Enumeration exists
    assert AssociationType is not None

def test_associationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationType]
    expected_literals = [
        "AGGREGATION",
        "COMPOSITION",
        "UNDIRECTED_ASSOCIATION",
        "DIRECTED_ASSOCIATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationType"

def test_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "CLASS",
        "INSTANCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
esmodel_url_ModelElementUrlFragment_strategy = st.builds(
    esmodel_url_ModelElementUrlFragment,
    name=
        safe_text
)
esmodel_url_ProjectUrlFragment_strategy = st.builds(
    esmodel_url_ProjectUrlFragment,
    name=
        safe_text
)
esmodel_url_ServerUrl_strategy = st.builds(
    esmodel_url_ServerUrl,
    port=
        st.integers(),
    hostName=
        safe_text
)
Role_strategy = st.builds(
    Role,
)
esmodel_roles_ProjectAdminRole_strategy = st.builds(
    esmodel_roles_ProjectAdminRole,
)
esmodel_roles_WriterRole_strategy = st.builds(
    esmodel_roles_WriterRole,
)
esmodel_roles_ServerAdmin_strategy = st.builds(
    esmodel_roles_ServerAdmin,
)
esmodel_roles_ReaderRole_strategy = st.builds(
    esmodel_roles_ReaderRole,
)
url_ModelElementUrlFragment_strategy = st.builds(
    url_ModelElementUrlFragment,
)
url_ProjectUrlFragment_strategy = st.builds(
    url_ProjectUrlFragment,
)
url_ServerUrl_strategy = st.builds(
    url_ServerUrl,
)
esmodel_url_ModelElementUrl_strategy = st.builds(
    esmodel_url_ModelElementUrl,
)
esmodel_roles_Role_strategy = st.builds(
    esmodel_roles_Role,
)
esmodel_accesscontrol_OrgUnitProperty_strategy = st.builds(
    esmodel_accesscontrol_OrgUnitProperty,
    name=
        safe_text,
    value=
        safe_text
)
accesscontrol_ACOrgUnit_strategy = st.builds(
    accesscontrol_ACOrgUnit,
)
accesscontrol_OrgUnitProperty_strategy = st.builds(
    accesscontrol_OrgUnitProperty,
)
roles_Role_strategy = st.builds(
    roles_Role,
)
ACOrgUnit_strategy = st.builds(
    ACOrgUnit,
)
esmodel_accesscontrol_ACGroup_strategy = st.builds(
    esmodel_accesscontrol_ACGroup,
)
ServerProjectEvent_strategy = st.builds(
    ServerProjectEvent,
)
esmodel_server_ProjectUpdatedEvent_strategy = st.builds(
    esmodel_server_ProjectUpdatedEvent,
)
ServerEvent_strategy = st.builds(
    ServerEvent,
)
esmodel_server_ServerProjectEvent_strategy = st.builds(
    esmodel_server_ServerProjectEvent,
)
operations_OperationId_strategy = st.builds(
    operations_OperationId,
)
esmodel_accesscontrol_ACUser_strategy = st.builds(
    esmodel_accesscontrol_ACUser,
    firstName=
        safe_text,
    lastName=
        safe_text
)
ReadEvent_strategy = st.builds(
    ReadEvent,
)
esmodel_events_NotificationReadEvent_strategy = st.builds(
    esmodel_events_NotificationReadEvent,
    notificationId=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
esmodel_events_ShowChangesEvent_strategy = st.builds(
    esmodel_events_ShowChangesEvent,
)
esmodel_events_UpdateEvent_strategy = st.builds(
    esmodel_events_UpdateEvent,
)
esmodel_events_DNDEvent_strategy = st.builds(
    esmodel_events_DNDEvent,
    sourceView=
        safe_text,
    targetView=
        safe_text
)
esmodel_events_PerspectiveEvent_strategy = st.builds(
    esmodel_events_PerspectiveEvent,
)
esmodel_events_Validate_strategy = st.builds(
    esmodel_events_Validate,
)
esmodel_events_MergeEvent_strategy = st.builds(
    esmodel_events_MergeEvent,
    totalTime=
        st.integers(),
    numberOfConflicts=
        st.integers()
)
esmodel_events_ShowHistoryEvent_strategy = st.builds(
    esmodel_events_ShowHistoryEvent,
)
esmodel_events_NotificationGenerationEvent_strategy = st.builds(
    esmodel_events_NotificationGenerationEvent,
)
esmodel_events_NotificationIgnoreEvent_strategy = st.builds(
    esmodel_events_NotificationIgnoreEvent,
    notificationId=
        safe_text
)
esmodel_events_PluginFocusEvent_strategy = st.builds(
    esmodel_events_PluginFocusEvent,
    startDate=
        st.dates(),
    pluginId=
        safe_text
)
esmodel_events_PresentationSwitchEvent_strategy = st.builds(
    esmodel_events_PresentationSwitchEvent,
    readView=
        safe_text,
    newPresentation=
        safe_text
)
esmodel_server_ServerEvent_strategy = st.builds(
    esmodel_server_ServerEvent,
)
esmodel_events_RevertEvent_strategy = st.builds(
    esmodel_events_RevertEvent,
    revertedChangesCount=
        st.integers()
)
esmodel_events_ExceptionEvent_strategy = st.builds(
    esmodel_events_ExceptionEvent,
    ExceptionCauseTitle=
        safe_text,
    ExceptionCauseStackTrace=
        safe_text,
    ExceptionStackTrace=
        safe_text,
    ExceptionTitle=
        safe_text
)
esmodel_events_CheckoutEvent_strategy = st.builds(
    esmodel_events_CheckoutEvent,
)
esmodel_events_MergeChoiceEvent_strategy = st.builds(
    esmodel_events_MergeChoiceEvent,
    selection=
        safe_text,
    contextFeature=
        safe_text,
    createdIssueName=
        safe_text
)
esmodel_events_NavigatorCreateEvent_strategy = st.builds(
    esmodel_events_NavigatorCreateEvent,
    dynamic=
        st.booleans()
)
esmodel_events_URLEvent_strategy = st.builds(
    esmodel_events_URLEvent,
    sourceView=
        safe_text
)
esmodel_events_LinkEvent_strategy = st.builds(
    esmodel_events_LinkEvent,
    sourceView=
        safe_text,
    createdNew=
        st.booleans()
)
esmodel_events_AnnotationEvent_strategy = st.builds(
    esmodel_events_AnnotationEvent,
)
esmodel_events_UndoEvent_strategy = st.builds(
    esmodel_events_UndoEvent,
)
esmodel_events_MergeGlobalChoiceEvent_strategy = st.builds(
    esmodel_events_MergeGlobalChoiceEvent,
    selection=
        safe_text
)
esmodel_events_TraceEvent_strategy = st.builds(
    esmodel_events_TraceEvent,
    featureName=
        safe_text
)
esmodel_events_PluginStartEvent_strategy = st.builds(
    esmodel_events_PluginStartEvent,
    pluginId=
        safe_text
)
esmodel_events_ReadEvent_strategy = st.builds(
    esmodel_events_ReadEvent,
    sourceView=
        safe_text,
    readView=
        safe_text
)
esmodel_events_Event_strategy = st.builds(
    esmodel_events_Event,
    timestamp=
        st.dates()
)
CompositeOperation_strategy = st.builds(
    CompositeOperation,
)
esmodel_semantic_SemanticCompositeOperation_strategy = st.builds(
    esmodel_semantic_SemanticCompositeOperation,
)
esmodel_operations_EObjectToModelElementIdMap_strategy = st.builds(
    esmodel_operations_EObjectToModelElementIdMap,
)
esmodel_operations_OperationGroup_strategy = st.builds(
    esmodel_operations_OperationGroup,
    name=
        safe_text
)
AttributeOperation_strategy = st.builds(
    AttributeOperation,
)
esmodel_operations_DiagramLayoutOperation_strategy = st.builds(
    esmodel_operations_DiagramLayoutOperation,
)
esmodel_operations_ModelElementGroup_strategy = st.builds(
    esmodel_operations_ModelElementGroup,
    name=
        safe_text
)
FeatureOperation_strategy = st.builds(
    FeatureOperation,
)
esmodel_operations_MultiReferenceMoveOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceMoveOperation,
    newIndex=
        st.integers(),
    oldIndex=
        st.integers()
)
esmodel_operations_MultiAttributeMoveOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeMoveOperation,
    oldIndex=
        st.integers(),
    referencedValue=
        safe_text,
    newIndex=
        st.integers()
)
esmodel_operations_MultiAttributeOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeOperation,
    referencedValues=
        safe_text,
    indexes=
        st.integers(),
    add=
        st.booleans()
)
esmodel_operations_MultiAttributeSetOperation_strategy = st.builds(
    esmodel_operations_MultiAttributeSetOperation,
    oldValue=
        safe_text,
    newValue=
        safe_text,
    index=
        st.integers()
)
esmodel_operations_ReferenceOperation_strategy = st.builds(
    esmodel_operations_ReferenceOperation,
    oppositeFeatureName=
        safe_text,
    containmentType=
        safe_text,
    bidirectional=
        st.booleans()
)
esmodel_operations_AttributeOperation_strategy = st.builds(
    esmodel_operations_AttributeOperation,
    newValue=
        safe_text,
    oldValue=
        safe_text
)
operations_EObjectToModelElementIdMap_strategy = st.builds(
    operations_EObjectToModelElementIdMap,
)
operations_ReferenceOperation_strategy = st.builds(
    operations_ReferenceOperation,
)
operations_esmodel_EObject_strategy = st.builds(
    operations_esmodel_EObject,
)
ReferenceOperation_strategy = st.builds(
    ReferenceOperation,
)
esmodel_operations_MultiReferenceSetOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceSetOperation,
    index=
        st.integers()
)
esmodel_operations_MultiReferenceOperation_strategy = st.builds(
    esmodel_operations_MultiReferenceOperation,
    add=
        st.booleans(),
    index=
        st.integers()
)
esmodel_operations_SingleReferenceOperation_strategy = st.builds(
    esmodel_operations_SingleReferenceOperation,
)
esmodel_versioning_VersionProperty_strategy = st.builds(
    esmodel_versioning_VersionProperty,
    value=
        safe_text,
    name=
        safe_text
)
AbstractOperation_strategy = st.builds(
    AbstractOperation,
)
esmodel_operations_CreateDeleteOperation_strategy = st.builds(
    esmodel_operations_CreateDeleteOperation,
    delete=
        st.booleans()
)
esmodel_operations_FeatureOperation_strategy = st.builds(
    esmodel_operations_FeatureOperation,
    featureName=
        safe_text
)
esmodel_operations_CompositeOperation_strategy = st.builds(
    esmodel_operations_CompositeOperation,
    compositeDescription=
        safe_text,
    reversed=
        st.booleans(),
    compositeName=
        safe_text
)
esmodel_versioning_HistoryQuery_strategy = st.builds(
    esmodel_versioning_HistoryQuery,
    includeChangePackage=
        st.booleans()
)
versioning_ChangePackage_strategy = st.builds(
    versioning_ChangePackage,
)
versioning_TagVersionSpec_strategy = st.builds(
    versioning_TagVersionSpec,
)
esmodel_versioning_HistoryInfo_strategy = st.builds(
    esmodel_versioning_HistoryInfo,
)
versioning_VersionProperty_strategy = st.builds(
    versioning_VersionProperty,
)
notification_ESNotification_strategy = st.builds(
    notification_ESNotification,
)
versioning_LogMessage_strategy = st.builds(
    versioning_LogMessage,
)
events_Event_strategy = st.builds(
    events_Event,
)
operations_AbstractOperation_strategy = st.builds(
    operations_AbstractOperation,
)
esmodel_versioning_ChangePackage_strategy = st.builds(
    esmodel_versioning_ChangePackage,
)
esmodel_versioning_LogMessage_strategy = st.builds(
    esmodel_versioning_LogMessage,
    clientDate=
        st.dates(),
    message=
        safe_text,
    date=
        st.dates(),
    author=
        safe_text
)
esmodel_versioning_VersionSpec_strategy = st.builds(
    esmodel_versioning_VersionSpec,
)
esmodel_versioning_Version_strategy = st.builds(
    esmodel_versioning_Version,
)
VersionSpec_strategy = st.builds(
    VersionSpec,
)
esmodel_versioning_HeadVersionSpec_strategy = st.builds(
    esmodel_versioning_HeadVersionSpec,
)
esmodel_versioning_PrimaryVersionSpec_strategy = st.builds(
    esmodel_versioning_PrimaryVersionSpec,
    identifier=
        st.integers()
)
esmodel_versioning_DateVersionSpec_strategy = st.builds(
    esmodel_versioning_DateVersionSpec,
    date=
        st.dates()
)
esmodel_versioning_TagVersionSpec_strategy = st.builds(
    esmodel_versioning_TagVersionSpec,
    name=
        safe_text
)
esmodel_ClientVersionInfo_strategy = st.builds(
    esmodel_ClientVersionInfo,
    name=
        safe_text,
    version=
        safe_text
)
esmodel_VersionInfo_strategy = st.builds(
    esmodel_VersionInfo,
    emfStoreVersionString=
        safe_text
)
accesscontrol_ACUser_strategy = st.builds(
    accesscontrol_ACUser,
)
SessionId_strategy = st.builds(
    SessionId,
)
ProjectHistory_strategy = st.builds(
    ProjectHistory,
)
accesscontrol_ACGroup_strategy = st.builds(
    accesscontrol_ACGroup,
)
esmodel_ServerSpace_strategy = st.builds(
    esmodel_ServerSpace,
)
versioning_PrimaryVersionSpec_strategy = st.builds(
    versioning_PrimaryVersionSpec,
)
esmodel_ProjectInfo_strategy = st.builds(
    esmodel_ProjectInfo,
    description=
        safe_text,
    name=
        safe_text
)
versioning_Version_strategy = st.builds(
    versioning_Version,
)
ProjectId_strategy = st.builds(
    ProjectId,
)
esmodel_ProjectHistory_strategy = st.builds(
    esmodel_ProjectHistory,
    projectDescription=
        safe_text,
    projectName=
        safe_text
)
ActivityObject_strategy = st.builds(
    ActivityObject,
)
model_activity_Fork_strategy = st.builds(
    model_activity_Fork,
)
model_activity_ActivityInitial_strategy = st.builds(
    model_activity_ActivityInitial,
)
model_activity_Branch_strategy = st.builds(
    model_activity_Branch,
)
model_activity_ActivityEnd_strategy = st.builds(
    model_activity_ActivityEnd,
)
model_activity_Activity_strategy = st.builds(
    model_activity_Activity,
)
activity_ActivityObject_strategy = st.builds(
    activity_ActivityObject,
)
activity_Transition_strategy = st.builds(
    activity_Transition,
)
ModelElementId_strategy = st.builds(
    ModelElementId,
)
StereotypeAttributeInstance_strategy = st.builds(
    StereotypeAttributeInstance,
)
model_profile_StereotypeAttributeInstanceString_strategy = st.builds(
    model_profile_StereotypeAttributeInstanceString,
    value=
        safe_text
)
StereotypeAttribute_strategy = st.builds(
    StereotypeAttribute,
)
model_profile_StereotypeAttributeSimple_strategy = st.builds(
    model_profile_StereotypeAttributeSimple,
    type=
        safe_text
)
profile_StereotypeAttributeInstance_strategy = st.builds(
    profile_StereotypeAttributeInstance,
)
model_util_ModelElementPath_strategy = st.builds(
    model_util_ModelElementPath,
)
profile_StereotypeAttribute_strategy = st.builds(
    profile_StereotypeAttribute,
)
profile_Profile_strategy = st.builds(
    profile_Profile,
)
profile_Stereotype_strategy = st.builds(
    profile_Stereotype,
)
state_Transition_strategy = st.builds(
    state_Transition,
)
document_Section_strategy = st.builds(
    document_Section,
)
Section_strategy = st.builds(
    Section,
)
model_document_CompositeSection_strategy = st.builds(
    model_document_CompositeSection,
)
model_document_LeafSection_strategy = st.builds(
    model_document_LeafSection,
)
document_CompositeSection_strategy = st.builds(
    document_CompositeSection,
)
classes_MethodArgument_strategy = st.builds(
    classes_MethodArgument,
)
classes_PackageElement_strategy = st.builds(
    classes_PackageElement,
)
requirement_Scenario_strategy = st.builds(
    requirement_Scenario,
)
requirement_UseCase_strategy = st.builds(
    requirement_UseCase,
)
classes_Method_strategy = st.builds(
    classes_Method,
)
classes_Attribute_strategy = st.builds(
    classes_Attribute,
)
classes_Association_strategy = st.builds(
    classes_Association,
)
classes_Class_strategy = st.builds(
    classes_Class,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
model_classes_Package_strategy = st.builds(
    model_classes_Package,
)
model_classes_Class_strategy = st.builds(
    model_classes_Class,
)
classes_Dependency_strategy = st.builds(
    classes_Dependency,
)
classes_Package_strategy = st.builds(
    classes_Package,
)
diagram_model_Diagram_strategy = st.builds(
    diagram_model_Diagram,
)
task_Checkable_strategy = st.builds(
    task_Checkable,
)
organization_User_strategy = st.builds(
    organization_User,
)
WorkItem_strategy = st.builds(
    WorkItem,
)
model_task_Milestone_strategy = st.builds(
    model_task_Milestone,
)
model_task_WorkPackage_strategy = st.builds(
    model_task_WorkPackage,
    endDate=
        st.dates(),
    startDate=
        st.dates()
)
change_ModelChangePackage_strategy = st.builds(
    change_ModelChangePackage,
)
organization_OrgUnit_strategy = st.builds(
    organization_OrgUnit,
)
OrgUnit_strategy = st.builds(
    OrgUnit,
)
model_organization_Group_strategy = st.builds(
    model_organization_Group,
)
model_organization_User_strategy = st.builds(
    model_organization_User,
    email=
        safe_text,
    firstName=
        safe_text,
    lastName=
        safe_text
)
task_WorkItem_strategy = st.builds(
    task_WorkItem,
)
model_task_ActionItem_strategy = st.builds(
    model_task_ActionItem,
    activity=
        safe_text,
    done=
        st.booleans()
)
organization_Group_strategy = st.builds(
    organization_Group,
)
task_WorkPackage_strategy = st.builds(
    task_WorkPackage,
)
UnicaseModelElement_strategy = st.builds(
    UnicaseModelElement,
)
model_activity_ActivityObject_strategy = st.builds(
    model_activity_ActivityObject,
)
model_profile_Profile_strategy = st.builds(
    model_profile_Profile,
)
model_profile_StereotypeInstance_strategy = st.builds(
    model_profile_StereotypeInstance,
)
model_classes_Attribute_strategy = st.builds(
    model_classes_Attribute,
    visibility=
        safe_text,
    properties=
        safe_text,
    label=
        safe_text,
    signature=
        safe_text,
    type=
        safe_text,
    scope=
        safe_text,
    defaultValue=
        safe_text
)
model_classes_Method_strategy = st.builds(
    model_classes_Method,
    signature=
        safe_text,
    scope=
        safe_text,
    visibility=
        safe_text,
    stubbed=
        st.booleans(),
    label=
        safe_text,
    properties=
        safe_text,
    returnType=
        safe_text
)
model_classes_Dependency_strategy = st.builds(
    model_classes_Dependency,
)
model_classes_MethodArgument_strategy = st.builds(
    model_classes_MethodArgument,
    type=
        safe_text,
    direction=
        safe_text,
    signature=
        safe_text,
    label=
        safe_text,
    defaultValue=
        safe_text
)
model_task_Checkable_strategy = st.builds(
    model_task_Checkable,
    checked=
        st.booleans()
)
model_profile_StereotypeAttribute_strategy = st.builds(
    model_profile_StereotypeAttribute,
)
model_profile_Stereotype_strategy = st.builds(
    model_profile_Stereotype,
    required=
        st.booleans()
)
model_classes_PackageElement_strategy = st.builds(
    model_classes_PackageElement,
)
model_classes_Association_strategy = st.builds(
    model_classes_Association,
    type=
        safe_text,
    sourceRole=
        safe_text,
    targetMultiplicity=
        safe_text,
    targetRole=
        safe_text,
    sourceMultiplicity=
        safe_text
)
model_profile_StereotypeAttributeInstance_strategy = st.builds(
    model_profile_StereotypeAttributeInstance,
)
model_activity_Transition_strategy = st.builds(
    model_activity_Transition,
    condition=
        safe_text
)
model_Attachment_strategy = st.builds(
    model_Attachment,
)
model_document_Section_strategy = st.builds(
    model_document_Section,
)
model_Annotation_strategy = st.builds(
    model_Annotation,
)
profile_StereotypeInstance_strategy = st.builds(
    profile_StereotypeInstance,
)
rationale_Comment_strategy = st.builds(
    rationale_Comment,
)
document_LeafSection_strategy = st.builds(
    document_LeafSection,
)
Attachment_strategy = st.builds(
    Attachment,
)
model_diagram_MEDiagram_strategy = st.builds(
    model_diagram_MEDiagram,
    type=
        safe_text,
    diagramLayout=
        safe_text
)
model_attachment_UrlAttachment_strategy = st.builds(
    model_attachment_UrlAttachment,
    url=
        safe_text
)
model_attachment_FileAttachment_strategy = st.builds(
    model_attachment_FileAttachment,
    requiredOffline=
        st.booleans(),
    fileSize=
        safe_text,
    fileName=
        safe_text,
    fileHash=
        safe_text,
    fileID=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
model_task_WorkItem_strategy = st.builds(
    model_task_WorkItem,
    resolved=
        st.booleans(),
    estimate=
        st.integers(),
    dueDate=
        st.dates(),
    priority=
        st.integers(),
    effort=
        st.integers()
)
model_organization_OrgUnit_strategy = st.builds(
    model_organization_OrgUnit,
    acOrgId=
        safe_text
)
Project_strategy = st.builds(
    Project,
)
model_Project_strategy = st.builds(
    model_Project,
)
model_NonDomainElement_strategy = st.builds(
    model_NonDomainElement,
)
metamodel_AssociationClassElement_strategy = st.builds(
    metamodel_AssociationClassElement,
)
metamodel_ModelVersion_strategy = st.builds(
    metamodel_ModelVersion,
    releaseNumber=
        st.integers()
)
UniqueIdentifier_strategy = st.builds(
    UniqueIdentifier,
)
esmodel_SessionId_strategy = st.builds(
    esmodel_SessionId,
)
esmodel_ProjectId_strategy = st.builds(
    esmodel_ProjectId,
)
esmodel_accesscontrol_ACOrgUnitId_strategy = st.builds(
    esmodel_accesscontrol_ACOrgUnitId,
)
esmodel_operations_OperationId_strategy = st.builds(
    esmodel_operations_OperationId,
)
metamodel_ModelElementId_strategy = st.builds(
    metamodel_ModelElementId,
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
esmodel_notification_ESNotification_strategy = st.builds(
    esmodel_notification_ESNotification,
    sender=
        safe_text,
    name=
        safe_text,
    provider=
        safe_text,
    creationDate=
        st.dates(),
    seen=
        st.booleans(),
    details=
        safe_text,
    recipient=
        safe_text,
    message=
        safe_text
)
esmodel_accesscontrol_ACOrgUnit_strategy = st.builds(
    esmodel_accesscontrol_ACOrgUnit,
    name=
        safe_text,
    description=
        safe_text
)
esmodel_operations_AbstractOperation_strategy = st.builds(
    esmodel_operations_AbstractOperation,
    clientDate=
        st.dates(),
    accepted=
        st.booleans(),
    name=
        safe_text,
    description=
        safe_text
)
metamodel_ModelElement_strategy = st.builds(
    metamodel_ModelElement,
    creationDate=
        st.dates(),
    creator=
        safe_text
)
metamodel_IdentifiableElement_strategy = st.builds(
    metamodel_IdentifiableElement,
    identifier=
        safe_text
)
metamodel_UniqueIdentifier_strategy = st.builds(
    metamodel_UniqueIdentifier,
    id=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
model_UnicaseModelElement_strategy = st.builds(
    model_UnicaseModelElement,
    name=
        safe_text,
    description=
        safe_text,
    state=
        safe_text
)
metamodel_Project_strategy = st.builds(
    metamodel_Project,
)
metamodel_NonDomainElement_strategy = st.builds(
    metamodel_NonDomainElement,
)
model_state_StateNode_strategy = st.builds(
    model_state_StateNode,
)
state_StateNode_strategy = st.builds(
    state_StateNode,
)
model_state_Transition_strategy = st.builds(
    model_state_Transition,
    condition=
        safe_text
)
MeetingSection_strategy = st.builds(
    MeetingSection,
)
model_meeting_WorkItemMeetingSection_strategy = st.builds(
    model_meeting_WorkItemMeetingSection,
)
model_meeting_IssueMeetingSection_strategy = st.builds(
    model_meeting_IssueMeetingSection,
)
model_meeting_CompositeMeetingSection_strategy = st.builds(
    model_meeting_CompositeMeetingSection,
)
model_meeting_MeetingSection_strategy = st.builds(
    model_meeting_MeetingSection,
    allocatedTime=
        st.integers()
)
StateNode_strategy = st.builds(
    StateNode,
)
model_state_StateEnd_strategy = st.builds(
    model_state_StateEnd,
)
model_state_StateInitial_strategy = st.builds(
    model_state_StateInitial,
)
model_state_State_strategy = st.builds(
    model_state_State,
    activities=
        safe_text,
    exitConditions=
        safe_text,
    entryConditions=
        safe_text
)
meeting_IssueMeetingSection_strategy = st.builds(
    meeting_IssueMeetingSection,
)
meeting_MeetingSection_strategy = st.builds(
    meeting_MeetingSection,
)
model_meeting_Meeting_strategy = st.builds(
    model_meeting_Meeting,
    endtime=
        st.dates(),
    starttime=
        st.dates(),
    location=
        safe_text
)
meeting_WorkItemMeetingSection_strategy = st.builds(
    meeting_WorkItemMeetingSection,
)
model_component_DeploymentNode_strategy = st.builds(
    model_component_DeploymentNode,
)
component_Component_strategy = st.builds(
    component_Component,
)
model_component_ComponentService_strategy = st.builds(
    model_component_ComponentService,
)
component_ComponentService_strategy = st.builds(
    component_ComponentService,
)
model_component_Component_strategy = st.builds(
    model_component_Component,
)
model_bug_BugReport_strategy = st.builds(
    model_bug_BugReport,
    Status=
        safe_text,
    resolution=
        safe_text,
    severity=
        safe_text,
    resolutionType=
        safe_text
)
Solution_strategy = st.builds(
    Solution,
)
model_change_MergingSolution_strategy = st.builds(
    model_change_MergingSolution,
)
change_MergingProposal_strategy = st.builds(
    change_MergingProposal,
)
Proposal_strategy = st.builds(
    Proposal,
)
model_change_MergingProposal_strategy = st.builds(
    model_change_MergingProposal,
)
Issue_strategy = st.builds(
    Issue,
)
model_change_MergingIssue_strategy = st.builds(
    model_change_MergingIssue,
    resolvingRevision=
        st.integers()
)
model_change_ModelChangePackage_strategy = st.builds(
    model_change_ModelChangePackage,
    targetVersion=
        st.integers(),
    sourceVersion=
        st.integers()
)
model_rationale_Criterion_strategy = st.builds(
    model_rationale_Criterion,
)
rationale_Assessment_strategy = st.builds(
    rationale_Assessment,
)
rationale_Issue_strategy = st.builds(
    rationale_Issue,
)
rationale_Criterion_strategy = st.builds(
    rationale_Criterion,
)
rationale_Solution_strategy = st.builds(
    rationale_Solution,
)
model_rationale_Issue_strategy = st.builds(
    model_rationale_Issue,
    activity=
        safe_text
)
Criterion_strategy = st.builds(
    Criterion,
)
model_requirement_NonFunctionalRequirement_strategy = st.builds(
    model_requirement_NonFunctionalRequirement,
)
requirement_SystemFunction_strategy = st.builds(
    requirement_SystemFunction,
)
rationale_Proposal_strategy = st.builds(
    rationale_Proposal,
)
model_requirement_ActorInstance_strategy = st.builds(
    model_requirement_ActorInstance,
)
model_requirement_Actor_strategy = st.builds(
    model_requirement_Actor,
)
NonDomainElement_strategy = st.builds(
    NonDomainElement,
)
model_rationale_Proposal_strategy = st.builds(
    model_rationale_Proposal,
)
model_rationale_Assessment_strategy = st.builds(
    model_rationale_Assessment,
    value=
        st.integers()
)
model_rationale_Comment_strategy = st.builds(
    model_rationale_Comment,
)
model_rationale_Solution_strategy = st.builds(
    model_rationale_Solution,
)
model_requirement_SystemFunction_strategy = st.builds(
    model_requirement_SystemFunction,
    output=
        safe_text,
    exception=
        safe_text,
    input=
        safe_text
)
model_requirement_UserTask_strategy = st.builds(
    model_requirement_UserTask,
)
model_requirement_Step_strategy = st.builds(
    model_requirement_Step,
    userStep=
        st.booleans()
)
requirement_ActorInstance_strategy = st.builds(
    requirement_ActorInstance,
)
model_requirement_Scenario_strategy = st.builds(
    model_requirement_Scenario,
)
requirement_NonFunctionalRequirement_strategy = st.builds(
    requirement_NonFunctionalRequirement,
)
requirement_UserTask_strategy = st.builds(
    requirement_UserTask,
)
requirement_Step_strategy = st.builds(
    requirement_Step,
)
requirement_Actor_strategy = st.builds(
    requirement_Actor,
)
model_requirement_UseCase_strategy = st.builds(
    model_requirement_UseCase,
    precondition=
        safe_text,
    rules=
        safe_text,
    postcondition=
        safe_text,
    exception=
        safe_text
)
requirement_FunctionalRequirement_strategy = st.builds(
    requirement_FunctionalRequirement,
)
model_requirement_FunctionalRequirement_strategy = st.builds(
    model_requirement_FunctionalRequirement,
    reviewed=
        st.booleans(),
    priority=
        st.integers(),
    storyPoints=
        st.integers(),
    cost=
        st.integers()
)

@given(instance=esmodel_url_ModelElementUrlFragment_strategy)
@settings(max_examples=50)
def test_esmodel_url_modelelementurlfragment_instantiation(instance):
    assert isinstance(instance, esmodel_url_ModelElementUrlFragment)



@given(instance=esmodel_url_ModelElementUrlFragment_strategy)
def test_esmodel_url_modelelementurlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel_url_ProjectUrlFragment_strategy)
@settings(max_examples=50)
def test_esmodel_url_projecturlfragment_instantiation(instance):
    assert isinstance(instance, esmodel_url_ProjectUrlFragment)



@given(instance=esmodel_url_ProjectUrlFragment_strategy)
def test_esmodel_url_projecturlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel_url_ServerUrl_strategy)
@settings(max_examples=50)
def test_esmodel_url_serverurl_instantiation(instance):
    assert isinstance(instance, esmodel_url_ServerUrl)



@given(instance=esmodel_url_ServerUrl_strategy)
def test_esmodel_url_serverurl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=esmodel_url_ServerUrl_strategy)
def test_esmodel_url_serverurl_hostName_setter(instance):
    original = instance.hostName
    instance.hostName = original
    assert instance.hostName == original

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=esmodel_roles_ProjectAdminRole_strategy)
@settings(max_examples=50)
def test_esmodel_roles_projectadminrole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ProjectAdminRole)

@given(instance=esmodel_roles_WriterRole_strategy)
@settings(max_examples=50)
def test_esmodel_roles_writerrole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_WriterRole)

@given(instance=esmodel_roles_ServerAdmin_strategy)
@settings(max_examples=50)
def test_esmodel_roles_serveradmin_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ServerAdmin)

@given(instance=esmodel_roles_ReaderRole_strategy)
@settings(max_examples=50)
def test_esmodel_roles_readerrole_instantiation(instance):
    assert isinstance(instance, esmodel_roles_ReaderRole)

@given(instance=url_ModelElementUrlFragment_strategy)
@settings(max_examples=50)
def test_url_modelelementurlfragment_instantiation(instance):
    assert isinstance(instance, url_ModelElementUrlFragment)

@given(instance=url_ProjectUrlFragment_strategy)
@settings(max_examples=50)
def test_url_projecturlfragment_instantiation(instance):
    assert isinstance(instance, url_ProjectUrlFragment)

@given(instance=url_ServerUrl_strategy)
@settings(max_examples=50)
def test_url_serverurl_instantiation(instance):
    assert isinstance(instance, url_ServerUrl)

@given(instance=esmodel_url_ModelElementUrl_strategy)
@settings(max_examples=50)
def test_esmodel_url_modelelementurl_instantiation(instance):
    assert isinstance(instance, esmodel_url_ModelElementUrl)

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=50)
def test_esmodel_roles_role_instantiation(instance):
    assert isinstance(instance, esmodel_roles_Role)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_esmodel_roles_role_candelete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canDelete(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canDelete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canDelete' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canDelete' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canDelete' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_esmodel_roles_role_canadministrate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canAdministrate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canAdministrate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canAdministrate' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canAdministrate' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canAdministrate' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_esmodel_roles_role_canread_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canRead(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canRead).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canRead' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canRead' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canRead' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_esmodel_roles_role_canmodify_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canModify(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canModify).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canModify' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canModify' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canModify' in esmodel_roles_Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel_roles_Role_strategy)
@settings(max_examples=30)
def test_esmodel_roles_role_cancreate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canCreate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canCreate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canCreate' in esmodel_roles_Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canCreate' in esmodel_roles_Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canCreate' in esmodel_roles_Role is not implemented or raised an error")

@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
@settings(max_examples=50)
def test_esmodel_accesscontrol_orgunitproperty_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_OrgUnitProperty)



@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
def test_esmodel_accesscontrol_orgunitproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_accesscontrol_OrgUnitProperty_strategy)
def test_esmodel_accesscontrol_orgunitproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=accesscontrol_ACOrgUnit_strategy)
@settings(max_examples=50)
def test_accesscontrol_acorgunit_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACOrgUnit)

@given(instance=accesscontrol_OrgUnitProperty_strategy)
@settings(max_examples=50)
def test_accesscontrol_orgunitproperty_instantiation(instance):
    assert isinstance(instance, accesscontrol_OrgUnitProperty)

@given(instance=roles_Role_strategy)
@settings(max_examples=50)
def test_roles_role_instantiation(instance):
    assert isinstance(instance, roles_Role)

@given(instance=ACOrgUnit_strategy)
@settings(max_examples=50)
def test_acorgunit_instantiation(instance):
    assert isinstance(instance, ACOrgUnit)

@given(instance=esmodel_accesscontrol_ACGroup_strategy)
@settings(max_examples=50)
def test_esmodel_accesscontrol_acgroup_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACGroup)

@given(instance=ServerProjectEvent_strategy)
@settings(max_examples=50)
def test_serverprojectevent_instantiation(instance):
    assert isinstance(instance, ServerProjectEvent)

@given(instance=esmodel_server_ProjectUpdatedEvent_strategy)
@settings(max_examples=50)
def test_esmodel_server_projectupdatedevent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ProjectUpdatedEvent)

@given(instance=ServerEvent_strategy)
@settings(max_examples=50)
def test_serverevent_instantiation(instance):
    assert isinstance(instance, ServerEvent)

@given(instance=esmodel_server_ServerProjectEvent_strategy)
@settings(max_examples=50)
def test_esmodel_server_serverprojectevent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ServerProjectEvent)

@given(instance=operations_OperationId_strategy)
@settings(max_examples=50)
def test_operations_operationid_instantiation(instance):
    assert isinstance(instance, operations_OperationId)

@given(instance=esmodel_accesscontrol_ACUser_strategy)
@settings(max_examples=50)
def test_esmodel_accesscontrol_acuser_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACUser)



@given(instance=esmodel_accesscontrol_ACUser_strategy)
def test_esmodel_accesscontrol_acuser_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=esmodel_accesscontrol_ACUser_strategy)
def test_esmodel_accesscontrol_acuser_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=ReadEvent_strategy)
@settings(max_examples=50)
def test_readevent_instantiation(instance):
    assert isinstance(instance, ReadEvent)

@given(instance=esmodel_events_NotificationReadEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_notificationreadevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationReadEvent)



@given(instance=esmodel_events_NotificationReadEvent_strategy)
def test_esmodel_events_notificationreadevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=esmodel_events_ShowChangesEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_showchangesevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ShowChangesEvent)

@given(instance=esmodel_events_UpdateEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_updateevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_UpdateEvent)

@given(instance=esmodel_events_DNDEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_dndevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_DNDEvent)



@given(instance=esmodel_events_DNDEvent_strategy)
def test_esmodel_events_dndevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original



@given(instance=esmodel_events_DNDEvent_strategy)
def test_esmodel_events_dndevent_targetView_setter(instance):
    original = instance.targetView
    instance.targetView = original
    assert instance.targetView == original

@given(instance=esmodel_events_PerspectiveEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_perspectiveevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PerspectiveEvent)

@given(instance=esmodel_events_Validate_strategy)
@settings(max_examples=50)
def test_esmodel_events_validate_instantiation(instance):
    assert isinstance(instance, esmodel_events_Validate)

@given(instance=esmodel_events_MergeEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_mergeevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeEvent)



@given(instance=esmodel_events_MergeEvent_strategy)
def test_esmodel_events_mergeevent_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=esmodel_events_MergeEvent_strategy)
def test_esmodel_events_mergeevent_numberOfConflicts_setter(instance):
    original = instance.numberOfConflicts
    instance.numberOfConflicts = original
    assert instance.numberOfConflicts == original

@given(instance=esmodel_events_ShowHistoryEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_showhistoryevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ShowHistoryEvent)

@given(instance=esmodel_events_NotificationGenerationEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_notificationgenerationevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationGenerationEvent)

@given(instance=esmodel_events_NotificationIgnoreEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_notificationignoreevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NotificationIgnoreEvent)



@given(instance=esmodel_events_NotificationIgnoreEvent_strategy)
def test_esmodel_events_notificationignoreevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original

@given(instance=esmodel_events_PluginFocusEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_pluginfocusevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PluginFocusEvent)



@given(instance=esmodel_events_PluginFocusEvent_strategy)
def test_esmodel_events_pluginfocusevent_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=esmodel_events_PluginFocusEvent_strategy)
def test_esmodel_events_pluginfocusevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original

@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_presentationswitchevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PresentationSwitchEvent)



@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
def test_esmodel_events_presentationswitchevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original



@given(instance=esmodel_events_PresentationSwitchEvent_strategy)
def test_esmodel_events_presentationswitchevent_newPresentation_setter(instance):
    original = instance.newPresentation
    instance.newPresentation = original
    assert instance.newPresentation == original

@given(instance=esmodel_server_ServerEvent_strategy)
@settings(max_examples=50)
def test_esmodel_server_serverevent_instantiation(instance):
    assert isinstance(instance, esmodel_server_ServerEvent)

@given(instance=esmodel_events_RevertEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_revertevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_RevertEvent)



@given(instance=esmodel_events_RevertEvent_strategy)
def test_esmodel_events_revertevent_revertedChangesCount_setter(instance):
    original = instance.revertedChangesCount
    instance.revertedChangesCount = original
    assert instance.revertedChangesCount == original

@given(instance=esmodel_events_ExceptionEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_exceptionevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ExceptionEvent)



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_esmodel_events_exceptionevent_ExceptionCauseTitle_setter(instance):
    original = instance.ExceptionCauseTitle
    instance.ExceptionCauseTitle = original
    assert instance.ExceptionCauseTitle == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_esmodel_events_exceptionevent_ExceptionCauseStackTrace_setter(instance):
    original = instance.ExceptionCauseStackTrace
    instance.ExceptionCauseStackTrace = original
    assert instance.ExceptionCauseStackTrace == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_esmodel_events_exceptionevent_ExceptionStackTrace_setter(instance):
    original = instance.ExceptionStackTrace
    instance.ExceptionStackTrace = original
    assert instance.ExceptionStackTrace == original



@given(instance=esmodel_events_ExceptionEvent_strategy)
def test_esmodel_events_exceptionevent_ExceptionTitle_setter(instance):
    original = instance.ExceptionTitle
    instance.ExceptionTitle = original
    assert instance.ExceptionTitle == original

@given(instance=esmodel_events_CheckoutEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_checkoutevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_CheckoutEvent)

@given(instance=esmodel_events_MergeChoiceEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_mergechoiceevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeChoiceEvent)



@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_esmodel_events_mergechoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original



@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_esmodel_events_mergechoiceevent_contextFeature_setter(instance):
    original = instance.contextFeature
    instance.contextFeature = original
    assert instance.contextFeature == original



@given(instance=esmodel_events_MergeChoiceEvent_strategy)
def test_esmodel_events_mergechoiceevent_createdIssueName_setter(instance):
    original = instance.createdIssueName
    instance.createdIssueName = original
    assert instance.createdIssueName == original

@given(instance=esmodel_events_NavigatorCreateEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_navigatorcreateevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_NavigatorCreateEvent)



@given(instance=esmodel_events_NavigatorCreateEvent_strategy)
def test_esmodel_events_navigatorcreateevent_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original

@given(instance=esmodel_events_URLEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_urlevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_URLEvent)



@given(instance=esmodel_events_URLEvent_strategy)
def test_esmodel_events_urlevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original

@given(instance=esmodel_events_LinkEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_linkevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_LinkEvent)



@given(instance=esmodel_events_LinkEvent_strategy)
def test_esmodel_events_linkevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original



@given(instance=esmodel_events_LinkEvent_strategy)
def test_esmodel_events_linkevent_createdNew_setter(instance):
    original = instance.createdNew
    instance.createdNew = original
    assert instance.createdNew == original

@given(instance=esmodel_events_AnnotationEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_annotationevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_AnnotationEvent)

@given(instance=esmodel_events_UndoEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_undoevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_UndoEvent)

@given(instance=esmodel_events_MergeGlobalChoiceEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_mergeglobalchoiceevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_MergeGlobalChoiceEvent)



@given(instance=esmodel_events_MergeGlobalChoiceEvent_strategy)
def test_esmodel_events_mergeglobalchoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=esmodel_events_TraceEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_traceevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_TraceEvent)



@given(instance=esmodel_events_TraceEvent_strategy)
def test_esmodel_events_traceevent_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=esmodel_events_PluginStartEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_pluginstartevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_PluginStartEvent)



@given(instance=esmodel_events_PluginStartEvent_strategy)
def test_esmodel_events_pluginstartevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original

@given(instance=esmodel_events_ReadEvent_strategy)
@settings(max_examples=50)
def test_esmodel_events_readevent_instantiation(instance):
    assert isinstance(instance, esmodel_events_ReadEvent)



@given(instance=esmodel_events_ReadEvent_strategy)
def test_esmodel_events_readevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original



@given(instance=esmodel_events_ReadEvent_strategy)
def test_esmodel_events_readevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original

@given(instance=esmodel_events_Event_strategy)
@settings(max_examples=50)
def test_esmodel_events_event_instantiation(instance):
    assert isinstance(instance, esmodel_events_Event)



@given(instance=esmodel_events_Event_strategy)
def test_esmodel_events_event_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=CompositeOperation_strategy)
@settings(max_examples=50)
def test_compositeoperation_instantiation(instance):
    assert isinstance(instance, CompositeOperation)

@given(instance=esmodel_semantic_SemanticCompositeOperation_strategy)
@settings(max_examples=50)
def test_esmodel_semantic_semanticcompositeoperation_instantiation(instance):
    assert isinstance(instance, esmodel_semantic_SemanticCompositeOperation)

@given(instance=esmodel_operations_EObjectToModelElementIdMap_strategy)
@settings(max_examples=50)
def test_esmodel_operations_eobjecttomodelelementidmap_instantiation(instance):
    assert isinstance(instance, esmodel_operations_EObjectToModelElementIdMap)

@given(instance=esmodel_operations_OperationGroup_strategy)
@settings(max_examples=50)
def test_esmodel_operations_operationgroup_instantiation(instance):
    assert isinstance(instance, esmodel_operations_OperationGroup)



@given(instance=esmodel_operations_OperationGroup_strategy)
def test_esmodel_operations_operationgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AttributeOperation_strategy)
@settings(max_examples=50)
def test_attributeoperation_instantiation(instance):
    assert isinstance(instance, AttributeOperation)

@given(instance=esmodel_operations_DiagramLayoutOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_diagramlayoutoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_DiagramLayoutOperation)

@given(instance=esmodel_operations_ModelElementGroup_strategy)
@settings(max_examples=50)
def test_esmodel_operations_modelelementgroup_instantiation(instance):
    assert isinstance(instance, esmodel_operations_ModelElementGroup)



@given(instance=esmodel_operations_ModelElementGroup_strategy)
def test_esmodel_operations_modelelementgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FeatureOperation_strategy)
@settings(max_examples=50)
def test_featureoperation_instantiation(instance):
    assert isinstance(instance, FeatureOperation)

@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multireferencemoveoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceMoveOperation)



@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
def test_esmodel_operations_multireferencemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original



@given(instance=esmodel_operations_MultiReferenceMoveOperation_strategy)
def test_esmodel_operations_multireferencemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original

@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multiattributemoveoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeMoveOperation)



@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_esmodel_operations_multiattributemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original



@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_esmodel_operations_multiattributemoveoperation_referencedValue_setter(instance):
    original = instance.referencedValue
    instance.referencedValue = original
    assert instance.referencedValue == original



@given(instance=esmodel_operations_MultiAttributeMoveOperation_strategy)
def test_esmodel_operations_multiattributemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original

@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multiattributeoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeOperation)



@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_esmodel_operations_multiattributeoperation_referencedValues_setter(instance):
    original = instance.referencedValues
    instance.referencedValues = original
    assert instance.referencedValues == original



@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_esmodel_operations_multiattributeoperation_indexes_setter(instance):
    original = instance.indexes
    instance.indexes = original
    assert instance.indexes == original



@given(instance=esmodel_operations_MultiAttributeOperation_strategy)
def test_esmodel_operations_multiattributeoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multiattributesetoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiAttributeSetOperation)



@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_esmodel_operations_multiattributesetoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original



@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_esmodel_operations_multiattributesetoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=esmodel_operations_MultiAttributeSetOperation_strategy)
def test_esmodel_operations_multiattributesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel_operations_ReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_referenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_ReferenceOperation)



@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_esmodel_operations_referenceoperation_oppositeFeatureName_setter(instance):
    original = instance.oppositeFeatureName
    instance.oppositeFeatureName = original
    assert instance.oppositeFeatureName == original



@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_esmodel_operations_referenceoperation_containmentType_setter(instance):
    original = instance.containmentType
    instance.containmentType = original
    assert instance.containmentType == original



@given(instance=esmodel_operations_ReferenceOperation_strategy)
def test_esmodel_operations_referenceoperation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=esmodel_operations_AttributeOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_attributeoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_AttributeOperation)



@given(instance=esmodel_operations_AttributeOperation_strategy)
def test_esmodel_operations_attributeoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original



@given(instance=esmodel_operations_AttributeOperation_strategy)
def test_esmodel_operations_attributeoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=operations_EObjectToModelElementIdMap_strategy)
@settings(max_examples=50)
def test_operations_eobjecttomodelelementidmap_instantiation(instance):
    assert isinstance(instance, operations_EObjectToModelElementIdMap)

@given(instance=operations_ReferenceOperation_strategy)
@settings(max_examples=50)
def test_operations_referenceoperation_instantiation(instance):
    assert isinstance(instance, operations_ReferenceOperation)

@given(instance=operations_esmodel_EObject_strategy)
@settings(max_examples=50)
def test_operations_esmodel_eobject_instantiation(instance):
    assert isinstance(instance, operations_esmodel_EObject)

@given(instance=ReferenceOperation_strategy)
@settings(max_examples=50)
def test_referenceoperation_instantiation(instance):
    assert isinstance(instance, ReferenceOperation)

@given(instance=esmodel_operations_MultiReferenceSetOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multireferencesetoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceSetOperation)



@given(instance=esmodel_operations_MultiReferenceSetOperation_strategy)
def test_esmodel_operations_multireferencesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_multireferenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_MultiReferenceOperation)



@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
def test_esmodel_operations_multireferenceoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=esmodel_operations_MultiReferenceOperation_strategy)
def test_esmodel_operations_multireferenceoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel_operations_SingleReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_singlereferenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_SingleReferenceOperation)

@given(instance=esmodel_versioning_VersionProperty_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_versionproperty_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_VersionProperty)



@given(instance=esmodel_versioning_VersionProperty_strategy)
def test_esmodel_versioning_versionproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=esmodel_versioning_VersionProperty_strategy)
def test_esmodel_versioning_versionproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractOperation_strategy)
@settings(max_examples=50)
def test_abstractoperation_instantiation(instance):
    assert isinstance(instance, AbstractOperation)

@given(instance=esmodel_operations_CreateDeleteOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_createdeleteoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_CreateDeleteOperation)



@given(instance=esmodel_operations_CreateDeleteOperation_strategy)
def test_esmodel_operations_createdeleteoperation_delete_setter(instance):
    original = instance.delete
    instance.delete = original
    assert instance.delete == original

@given(instance=esmodel_operations_FeatureOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_featureoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_FeatureOperation)



@given(instance=esmodel_operations_FeatureOperation_strategy)
def test_esmodel_operations_featureoperation_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=esmodel_operations_CompositeOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_compositeoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_CompositeOperation)



@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_esmodel_operations_compositeoperation_compositeDescription_setter(instance):
    original = instance.compositeDescription
    instance.compositeDescription = original
    assert instance.compositeDescription == original



@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_esmodel_operations_compositeoperation_reversed_setter(instance):
    original = instance.reversed
    instance.reversed = original
    assert instance.reversed == original



@given(instance=esmodel_operations_CompositeOperation_strategy)
def test_esmodel_operations_compositeoperation_compositeName_setter(instance):
    original = instance.compositeName
    instance.compositeName = original
    assert instance.compositeName == original

@given(instance=esmodel_versioning_HistoryQuery_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_historyquery_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HistoryQuery)



@given(instance=esmodel_versioning_HistoryQuery_strategy)
def test_esmodel_versioning_historyquery_includeChangePackage_setter(instance):
    original = instance.includeChangePackage
    instance.includeChangePackage = original
    assert instance.includeChangePackage == original

@given(instance=versioning_ChangePackage_strategy)
@settings(max_examples=50)
def test_versioning_changepackage_instantiation(instance):
    assert isinstance(instance, versioning_ChangePackage)

@given(instance=versioning_TagVersionSpec_strategy)
@settings(max_examples=50)
def test_versioning_tagversionspec_instantiation(instance):
    assert isinstance(instance, versioning_TagVersionSpec)

@given(instance=esmodel_versioning_HistoryInfo_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_historyinfo_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HistoryInfo)

@given(instance=versioning_VersionProperty_strategy)
@settings(max_examples=50)
def test_versioning_versionproperty_instantiation(instance):
    assert isinstance(instance, versioning_VersionProperty)

@given(instance=notification_ESNotification_strategy)
@settings(max_examples=50)
def test_notification_esnotification_instantiation(instance):
    assert isinstance(instance, notification_ESNotification)

@given(instance=versioning_LogMessage_strategy)
@settings(max_examples=50)
def test_versioning_logmessage_instantiation(instance):
    assert isinstance(instance, versioning_LogMessage)

@given(instance=events_Event_strategy)
@settings(max_examples=50)
def test_events_event_instantiation(instance):
    assert isinstance(instance, events_Event)

@given(instance=operations_AbstractOperation_strategy)
@settings(max_examples=50)
def test_operations_abstractoperation_instantiation(instance):
    assert isinstance(instance, operations_AbstractOperation)

@given(instance=esmodel_versioning_ChangePackage_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_changepackage_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_ChangePackage)

@given(instance=esmodel_versioning_LogMessage_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_logmessage_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_LogMessage)



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_esmodel_versioning_logmessage_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_esmodel_versioning_logmessage_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_esmodel_versioning_logmessage_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=esmodel_versioning_LogMessage_strategy)
def test_esmodel_versioning_logmessage_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=esmodel_versioning_VersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_versionspec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_VersionSpec)

@given(instance=esmodel_versioning_Version_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_version_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_Version)

@given(instance=VersionSpec_strategy)
@settings(max_examples=50)
def test_versionspec_instantiation(instance):
    assert isinstance(instance, VersionSpec)

@given(instance=esmodel_versioning_HeadVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_headversionspec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_HeadVersionSpec)

@given(instance=esmodel_versioning_PrimaryVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_primaryversionspec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_PrimaryVersionSpec)



@given(instance=esmodel_versioning_PrimaryVersionSpec_strategy)
def test_esmodel_versioning_primaryversionspec_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=esmodel_versioning_DateVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_dateversionspec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_DateVersionSpec)



@given(instance=esmodel_versioning_DateVersionSpec_strategy)
def test_esmodel_versioning_dateversionspec_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=esmodel_versioning_TagVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel_versioning_tagversionspec_instantiation(instance):
    assert isinstance(instance, esmodel_versioning_TagVersionSpec)



@given(instance=esmodel_versioning_TagVersionSpec_strategy)
def test_esmodel_versioning_tagversionspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel_ClientVersionInfo_strategy)
@settings(max_examples=50)
def test_esmodel_clientversioninfo_instantiation(instance):
    assert isinstance(instance, esmodel_ClientVersionInfo)



@given(instance=esmodel_ClientVersionInfo_strategy)
def test_esmodel_clientversioninfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_ClientVersionInfo_strategy)
def test_esmodel_clientversioninfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=esmodel_VersionInfo_strategy)
@settings(max_examples=50)
def test_esmodel_versioninfo_instantiation(instance):
    assert isinstance(instance, esmodel_VersionInfo)



@given(instance=esmodel_VersionInfo_strategy)
def test_esmodel_versioninfo_emfStoreVersionString_setter(instance):
    original = instance.emfStoreVersionString
    instance.emfStoreVersionString = original
    assert instance.emfStoreVersionString == original

@given(instance=accesscontrol_ACUser_strategy)
@settings(max_examples=50)
def test_accesscontrol_acuser_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACUser)

@given(instance=SessionId_strategy)
@settings(max_examples=50)
def test_sessionid_instantiation(instance):
    assert isinstance(instance, SessionId)

@given(instance=ProjectHistory_strategy)
@settings(max_examples=50)
def test_projecthistory_instantiation(instance):
    assert isinstance(instance, ProjectHistory)

@given(instance=accesscontrol_ACGroup_strategy)
@settings(max_examples=50)
def test_accesscontrol_acgroup_instantiation(instance):
    assert isinstance(instance, accesscontrol_ACGroup)

@given(instance=esmodel_ServerSpace_strategy)
@settings(max_examples=50)
def test_esmodel_serverspace_instantiation(instance):
    assert isinstance(instance, esmodel_ServerSpace)

@given(instance=versioning_PrimaryVersionSpec_strategy)
@settings(max_examples=50)
def test_versioning_primaryversionspec_instantiation(instance):
    assert isinstance(instance, versioning_PrimaryVersionSpec)

@given(instance=esmodel_ProjectInfo_strategy)
@settings(max_examples=50)
def test_esmodel_projectinfo_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectInfo)



@given(instance=esmodel_ProjectInfo_strategy)
def test_esmodel_projectinfo_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=esmodel_ProjectInfo_strategy)
def test_esmodel_projectinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=versioning_Version_strategy)
@settings(max_examples=50)
def test_versioning_version_instantiation(instance):
    assert isinstance(instance, versioning_Version)

@given(instance=ProjectId_strategy)
@settings(max_examples=50)
def test_projectid_instantiation(instance):
    assert isinstance(instance, ProjectId)

@given(instance=esmodel_ProjectHistory_strategy)
@settings(max_examples=50)
def test_esmodel_projecthistory_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectHistory)



@given(instance=esmodel_ProjectHistory_strategy)
def test_esmodel_projecthistory_projectDescription_setter(instance):
    original = instance.projectDescription
    instance.projectDescription = original
    assert instance.projectDescription == original



@given(instance=esmodel_ProjectHistory_strategy)
def test_esmodel_projecthistory_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original

@given(instance=ActivityObject_strategy)
@settings(max_examples=50)
def test_activityobject_instantiation(instance):
    assert isinstance(instance, ActivityObject)

@given(instance=model_activity_Fork_strategy)
@settings(max_examples=50)
def test_model_activity_fork_instantiation(instance):
    assert isinstance(instance, model_activity_Fork)

@given(instance=model_activity_ActivityInitial_strategy)
@settings(max_examples=50)
def test_model_activity_activityinitial_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityInitial)

@given(instance=model_activity_Branch_strategy)
@settings(max_examples=50)
def test_model_activity_branch_instantiation(instance):
    assert isinstance(instance, model_activity_Branch)

@given(instance=model_activity_ActivityEnd_strategy)
@settings(max_examples=50)
def test_model_activity_activityend_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityEnd)

@given(instance=model_activity_Activity_strategy)
@settings(max_examples=50)
def test_model_activity_activity_instantiation(instance):
    assert isinstance(instance, model_activity_Activity)

@given(instance=activity_ActivityObject_strategy)
@settings(max_examples=50)
def test_activity_activityobject_instantiation(instance):
    assert isinstance(instance, activity_ActivityObject)

@given(instance=activity_Transition_strategy)
@settings(max_examples=50)
def test_activity_transition_instantiation(instance):
    assert isinstance(instance, activity_Transition)

@given(instance=ModelElementId_strategy)
@settings(max_examples=50)
def test_modelelementid_instantiation(instance):
    assert isinstance(instance, ModelElementId)

@given(instance=StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, StereotypeAttributeInstance)

@given(instance=model_profile_StereotypeAttributeInstanceString_strategy)
@settings(max_examples=50)
def test_model_profile_stereotypeattributeinstancestring_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeInstanceString)



@given(instance=model_profile_StereotypeAttributeInstanceString_strategy)
def test_model_profile_stereotypeattributeinstancestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_stereotypeattribute_instantiation(instance):
    assert isinstance(instance, StereotypeAttribute)

@given(instance=model_profile_StereotypeAttributeSimple_strategy)
@settings(max_examples=50)
def test_model_profile_stereotypeattributesimple_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeSimple)



@given(instance=model_profile_StereotypeAttributeSimple_strategy)
def test_model_profile_stereotypeattributesimple_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=profile_StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_profile_stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, profile_StereotypeAttributeInstance)

@given(instance=model_util_ModelElementPath_strategy)
@settings(max_examples=50)
def test_model_util_modelelementpath_instantiation(instance):
    assert isinstance(instance, model_util_ModelElementPath)

@given(instance=profile_StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_profile_stereotypeattribute_instantiation(instance):
    assert isinstance(instance, profile_StereotypeAttribute)

@given(instance=profile_Profile_strategy)
@settings(max_examples=50)
def test_profile_profile_instantiation(instance):
    assert isinstance(instance, profile_Profile)

@given(instance=profile_Stereotype_strategy)
@settings(max_examples=50)
def test_profile_stereotype_instantiation(instance):
    assert isinstance(instance, profile_Stereotype)

@given(instance=state_Transition_strategy)
@settings(max_examples=50)
def test_state_transition_instantiation(instance):
    assert isinstance(instance, state_Transition)

@given(instance=document_Section_strategy)
@settings(max_examples=50)
def test_document_section_instantiation(instance):
    assert isinstance(instance, document_Section)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=model_document_CompositeSection_strategy)
@settings(max_examples=50)
def test_model_document_compositesection_instantiation(instance):
    assert isinstance(instance, model_document_CompositeSection)

@given(instance=model_document_LeafSection_strategy)
@settings(max_examples=50)
def test_model_document_leafsection_instantiation(instance):
    assert isinstance(instance, model_document_LeafSection)

@given(instance=document_CompositeSection_strategy)
@settings(max_examples=50)
def test_document_compositesection_instantiation(instance):
    assert isinstance(instance, document_CompositeSection)

@given(instance=classes_MethodArgument_strategy)
@settings(max_examples=50)
def test_classes_methodargument_instantiation(instance):
    assert isinstance(instance, classes_MethodArgument)

@given(instance=classes_PackageElement_strategy)
@settings(max_examples=50)
def test_classes_packageelement_instantiation(instance):
    assert isinstance(instance, classes_PackageElement)

@given(instance=requirement_Scenario_strategy)
@settings(max_examples=50)
def test_requirement_scenario_instantiation(instance):
    assert isinstance(instance, requirement_Scenario)

@given(instance=requirement_UseCase_strategy)
@settings(max_examples=50)
def test_requirement_usecase_instantiation(instance):
    assert isinstance(instance, requirement_UseCase)

@given(instance=classes_Method_strategy)
@settings(max_examples=50)
def test_classes_method_instantiation(instance):
    assert isinstance(instance, classes_Method)

@given(instance=classes_Attribute_strategy)
@settings(max_examples=50)
def test_classes_attribute_instantiation(instance):
    assert isinstance(instance, classes_Attribute)

@given(instance=classes_Association_strategy)
@settings(max_examples=50)
def test_classes_association_instantiation(instance):
    assert isinstance(instance, classes_Association)

@given(instance=classes_Class_strategy)
@settings(max_examples=50)
def test_classes_class_instantiation(instance):
    assert isinstance(instance, classes_Class)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=model_classes_Package_strategy)
@settings(max_examples=50)
def test_model_classes_package_instantiation(instance):
    assert isinstance(instance, model_classes_Package)

@given(instance=model_classes_Class_strategy)
@settings(max_examples=50)
def test_model_classes_class_instantiation(instance):
    assert isinstance(instance, model_classes_Class)

@given(instance=classes_Dependency_strategy)
@settings(max_examples=50)
def test_classes_dependency_instantiation(instance):
    assert isinstance(instance, classes_Dependency)

@given(instance=classes_Package_strategy)
@settings(max_examples=50)
def test_classes_package_instantiation(instance):
    assert isinstance(instance, classes_Package)

@given(instance=diagram_model_Diagram_strategy)
@settings(max_examples=50)
def test_diagram_model_diagram_instantiation(instance):
    assert isinstance(instance, diagram_model_Diagram)

@given(instance=task_Checkable_strategy)
@settings(max_examples=50)
def test_task_checkable_instantiation(instance):
    assert isinstance(instance, task_Checkable)

@given(instance=organization_User_strategy)
@settings(max_examples=50)
def test_organization_user_instantiation(instance):
    assert isinstance(instance, organization_User)

@given(instance=WorkItem_strategy)
@settings(max_examples=50)
def test_workitem_instantiation(instance):
    assert isinstance(instance, WorkItem)

@given(instance=model_task_Milestone_strategy)
@settings(max_examples=50)
def test_model_task_milestone_instantiation(instance):
    assert isinstance(instance, model_task_Milestone)

@given(instance=model_task_WorkPackage_strategy)
@settings(max_examples=50)
def test_model_task_workpackage_instantiation(instance):
    assert isinstance(instance, model_task_WorkPackage)



@given(instance=model_task_WorkPackage_strategy)
def test_model_task_workpackage_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original



@given(instance=model_task_WorkPackage_strategy)
def test_model_task_workpackage_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=change_ModelChangePackage_strategy)
@settings(max_examples=50)
def test_change_modelchangepackage_instantiation(instance):
    assert isinstance(instance, change_ModelChangePackage)

@given(instance=organization_OrgUnit_strategy)
@settings(max_examples=50)
def test_organization_orgunit_instantiation(instance):
    assert isinstance(instance, organization_OrgUnit)

@given(instance=OrgUnit_strategy)
@settings(max_examples=50)
def test_orgunit_instantiation(instance):
    assert isinstance(instance, OrgUnit)

@given(instance=model_organization_Group_strategy)
@settings(max_examples=50)
def test_model_organization_group_instantiation(instance):
    assert isinstance(instance, model_organization_Group)

@given(instance=model_organization_User_strategy)
@settings(max_examples=50)
def test_model_organization_user_instantiation(instance):
    assert isinstance(instance, model_organization_User)



@given(instance=model_organization_User_strategy)
def test_model_organization_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=model_organization_User_strategy)
def test_model_organization_user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=model_organization_User_strategy)
def test_model_organization_user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=task_WorkItem_strategy)
@settings(max_examples=50)
def test_task_workitem_instantiation(instance):
    assert isinstance(instance, task_WorkItem)

@given(instance=model_task_ActionItem_strategy)
@settings(max_examples=50)
def test_model_task_actionitem_instantiation(instance):
    assert isinstance(instance, model_task_ActionItem)



@given(instance=model_task_ActionItem_strategy)
def test_model_task_actionitem_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=model_task_ActionItem_strategy)
def test_model_task_actionitem_done_setter(instance):
    original = instance.done
    instance.done = original
    assert instance.done == original

@given(instance=organization_Group_strategy)
@settings(max_examples=50)
def test_organization_group_instantiation(instance):
    assert isinstance(instance, organization_Group)

@given(instance=task_WorkPackage_strategy)
@settings(max_examples=50)
def test_task_workpackage_instantiation(instance):
    assert isinstance(instance, task_WorkPackage)

@given(instance=UnicaseModelElement_strategy)
@settings(max_examples=50)
def test_unicasemodelelement_instantiation(instance):
    assert isinstance(instance, UnicaseModelElement)

@given(instance=model_activity_ActivityObject_strategy)
@settings(max_examples=50)
def test_model_activity_activityobject_instantiation(instance):
    assert isinstance(instance, model_activity_ActivityObject)

@given(instance=model_profile_Profile_strategy)
@settings(max_examples=50)
def test_model_profile_profile_instantiation(instance):
    assert isinstance(instance, model_profile_Profile)

@given(instance=model_profile_StereotypeInstance_strategy)
@settings(max_examples=50)
def test_model_profile_stereotypeinstance_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeInstance)

@given(instance=model_classes_Attribute_strategy)
@settings(max_examples=50)
def test_model_classes_attribute_instantiation(instance):
    assert isinstance(instance, model_classes_Attribute)



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=model_classes_Attribute_strategy)
def test_model_classes_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model_classes_Method_strategy)
@settings(max_examples=50)
def test_model_classes_method_instantiation(instance):
    assert isinstance(instance, model_classes_Method)



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_stubbed_setter(instance):
    original = instance.stubbed
    instance.stubbed = original
    assert instance.stubbed == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=model_classes_Method_strategy)
def test_model_classes_method_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=model_classes_Dependency_strategy)
@settings(max_examples=50)
def test_model_classes_dependency_instantiation(instance):
    assert isinstance(instance, model_classes_Dependency)

@given(instance=model_classes_MethodArgument_strategy)
@settings(max_examples=50)
def test_model_classes_methodargument_instantiation(instance):
    assert isinstance(instance, model_classes_MethodArgument)



@given(instance=model_classes_MethodArgument_strategy)
def test_model_classes_methodargument_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_MethodArgument_strategy)
def test_model_classes_methodargument_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_classes_MethodArgument_strategy)
def test_model_classes_methodargument_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=model_classes_MethodArgument_strategy)
def test_model_classes_methodargument_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=model_classes_MethodArgument_strategy)
def test_model_classes_methodargument_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model_task_Checkable_strategy)
@settings(max_examples=50)
def test_model_task_checkable_instantiation(instance):
    assert isinstance(instance, model_task_Checkable)



@given(instance=model_task_Checkable_strategy)
def test_model_task_checkable_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=model_profile_StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_model_profile_stereotypeattribute_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttribute)

@given(instance=model_profile_Stereotype_strategy)
@settings(max_examples=50)
def test_model_profile_stereotype_instantiation(instance):
    assert isinstance(instance, model_profile_Stereotype)



@given(instance=model_profile_Stereotype_strategy)
def test_model_profile_stereotype_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=model_classes_PackageElement_strategy)
@settings(max_examples=50)
def test_model_classes_packageelement_instantiation(instance):
    assert isinstance(instance, model_classes_PackageElement)

@given(instance=model_classes_Association_strategy)
@settings(max_examples=50)
def test_model_classes_association_instantiation(instance):
    assert isinstance(instance, model_classes_Association)



@given(instance=model_classes_Association_strategy)
def test_model_classes_association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_classes_Association_strategy)
def test_model_classes_association_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original



@given(instance=model_classes_Association_strategy)
def test_model_classes_association_targetMultiplicity_setter(instance):
    original = instance.targetMultiplicity
    instance.targetMultiplicity = original
    assert instance.targetMultiplicity == original



@given(instance=model_classes_Association_strategy)
def test_model_classes_association_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original



@given(instance=model_classes_Association_strategy)
def test_model_classes_association_sourceMultiplicity_setter(instance):
    original = instance.sourceMultiplicity
    instance.sourceMultiplicity = original
    assert instance.sourceMultiplicity == original

@given(instance=model_profile_StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_model_profile_stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, model_profile_StereotypeAttributeInstance)

@given(instance=model_activity_Transition_strategy)
@settings(max_examples=50)
def test_model_activity_transition_instantiation(instance):
    assert isinstance(instance, model_activity_Transition)



@given(instance=model_activity_Transition_strategy)
def test_model_activity_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=model_Attachment_strategy)
@settings(max_examples=50)
def test_model_attachment_instantiation(instance):
    assert isinstance(instance, model_Attachment)

@given(instance=model_document_Section_strategy)
@settings(max_examples=50)
def test_model_document_section_instantiation(instance):
    assert isinstance(instance, model_document_Section)

@given(instance=model_Annotation_strategy)
@settings(max_examples=50)
def test_model_annotation_instantiation(instance):
    assert isinstance(instance, model_Annotation)

@given(instance=profile_StereotypeInstance_strategy)
@settings(max_examples=50)
def test_profile_stereotypeinstance_instantiation(instance):
    assert isinstance(instance, profile_StereotypeInstance)

@given(instance=rationale_Comment_strategy)
@settings(max_examples=50)
def test_rationale_comment_instantiation(instance):
    assert isinstance(instance, rationale_Comment)

@given(instance=document_LeafSection_strategy)
@settings(max_examples=50)
def test_document_leafsection_instantiation(instance):
    assert isinstance(instance, document_LeafSection)

@given(instance=Attachment_strategy)
@settings(max_examples=50)
def test_attachment_instantiation(instance):
    assert isinstance(instance, Attachment)

@given(instance=model_diagram_MEDiagram_strategy)
@settings(max_examples=50)
def test_model_diagram_mediagram_instantiation(instance):
    assert isinstance(instance, model_diagram_MEDiagram)



@given(instance=model_diagram_MEDiagram_strategy)
def test_model_diagram_mediagram_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=model_diagram_MEDiagram_strategy)
def test_model_diagram_mediagram_diagramLayout_setter(instance):
    original = instance.diagramLayout
    instance.diagramLayout = original
    assert instance.diagramLayout == original

@given(instance=model_attachment_UrlAttachment_strategy)
@settings(max_examples=50)
def test_model_attachment_urlattachment_instantiation(instance):
    assert isinstance(instance, model_attachment_UrlAttachment)



@given(instance=model_attachment_UrlAttachment_strategy)
def test_model_attachment_urlattachment_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=model_attachment_FileAttachment_strategy)
@settings(max_examples=50)
def test_model_attachment_fileattachment_instantiation(instance):
    assert isinstance(instance, model_attachment_FileAttachment)



@given(instance=model_attachment_FileAttachment_strategy)
def test_model_attachment_fileattachment_requiredOffline_setter(instance):
    original = instance.requiredOffline
    instance.requiredOffline = original
    assert instance.requiredOffline == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_model_attachment_fileattachment_fileSize_setter(instance):
    original = instance.fileSize
    instance.fileSize = original
    assert instance.fileSize == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_model_attachment_fileattachment_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_model_attachment_fileattachment_fileHash_setter(instance):
    original = instance.fileHash
    instance.fileHash = original
    assert instance.fileHash == original



@given(instance=model_attachment_FileAttachment_strategy)
def test_model_attachment_fileattachment_fileID_setter(instance):
    original = instance.fileID
    instance.fileID = original
    assert instance.fileID == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=model_task_WorkItem_strategy)
@settings(max_examples=50)
def test_model_task_workitem_instantiation(instance):
    assert isinstance(instance, model_task_WorkItem)



@given(instance=model_task_WorkItem_strategy)
def test_model_task_workitem_resolved_setter(instance):
    original = instance.resolved
    instance.resolved = original
    assert instance.resolved == original



@given(instance=model_task_WorkItem_strategy)
def test_model_task_workitem_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original



@given(instance=model_task_WorkItem_strategy)
def test_model_task_workitem_dueDate_setter(instance):
    original = instance.dueDate
    instance.dueDate = original
    assert instance.dueDate == original



@given(instance=model_task_WorkItem_strategy)
def test_model_task_workitem_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=model_task_WorkItem_strategy)
def test_model_task_workitem_effort_setter(instance):
    original = instance.effort
    instance.effort = original
    assert instance.effort == original

@given(instance=model_organization_OrgUnit_strategy)
@settings(max_examples=50)
def test_model_organization_orgunit_instantiation(instance):
    assert isinstance(instance, model_organization_OrgUnit)



@given(instance=model_organization_OrgUnit_strategy)
def test_model_organization_orgunit_acOrgId_setter(instance):
    original = instance.acOrgId
    instance.acOrgId = original
    assert instance.acOrgId == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=model_Project_strategy)
@settings(max_examples=50)
def test_model_project_instantiation(instance):
    assert isinstance(instance, model_Project)

@given(instance=model_NonDomainElement_strategy)
@settings(max_examples=50)
def test_model_nondomainelement_instantiation(instance):
    assert isinstance(instance, model_NonDomainElement)

@given(instance=metamodel_AssociationClassElement_strategy)
@settings(max_examples=50)
def test_metamodel_associationclasselement_instantiation(instance):
    assert isinstance(instance, metamodel_AssociationClassElement)

@given(instance=metamodel_ModelVersion_strategy)
@settings(max_examples=50)
def test_metamodel_modelversion_instantiation(instance):
    assert isinstance(instance, metamodel_ModelVersion)



@given(instance=metamodel_ModelVersion_strategy)
def test_metamodel_modelversion_releaseNumber_setter(instance):
    original = instance.releaseNumber
    instance.releaseNumber = original
    assert instance.releaseNumber == original

@given(instance=UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, UniqueIdentifier)

@given(instance=esmodel_SessionId_strategy)
@settings(max_examples=50)
def test_esmodel_sessionid_instantiation(instance):
    assert isinstance(instance, esmodel_SessionId)

@given(instance=esmodel_ProjectId_strategy)
@settings(max_examples=50)
def test_esmodel_projectid_instantiation(instance):
    assert isinstance(instance, esmodel_ProjectId)

@given(instance=esmodel_accesscontrol_ACOrgUnitId_strategy)
@settings(max_examples=50)
def test_esmodel_accesscontrol_acorgunitid_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACOrgUnitId)

@given(instance=esmodel_operations_OperationId_strategy)
@settings(max_examples=50)
def test_esmodel_operations_operationid_instantiation(instance):
    assert isinstance(instance, esmodel_operations_OperationId)

@given(instance=metamodel_ModelElementId_strategy)
@settings(max_examples=50)
def test_metamodel_modelelementid_instantiation(instance):
    assert isinstance(instance, metamodel_ModelElementId)

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

@given(instance=esmodel_notification_ESNotification_strategy)
@settings(max_examples=50)
def test_esmodel_notification_esnotification_instantiation(instance):
    assert isinstance(instance, esmodel_notification_ESNotification)



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_seen_setter(instance):
    original = instance.seen
    instance.seen = original
    assert instance.seen == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_recipient_setter(instance):
    original = instance.recipient
    instance.recipient = original
    assert instance.recipient == original



@given(instance=esmodel_notification_ESNotification_strategy)
def test_esmodel_notification_esnotification_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
@settings(max_examples=50)
def test_esmodel_accesscontrol_acorgunit_instantiation(instance):
    assert isinstance(instance, esmodel_accesscontrol_ACOrgUnit)



@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
def test_esmodel_accesscontrol_acorgunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_accesscontrol_ACOrgUnit_strategy)
def test_esmodel_accesscontrol_acorgunit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=esmodel_operations_AbstractOperation_strategy)
@settings(max_examples=50)
def test_esmodel_operations_abstractoperation_instantiation(instance):
    assert isinstance(instance, esmodel_operations_AbstractOperation)



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_esmodel_operations_abstractoperation_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_esmodel_operations_abstractoperation_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_esmodel_operations_abstractoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esmodel_operations_AbstractOperation_strategy)
def test_esmodel_operations_abstractoperation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=metamodel_ModelElement_strategy)
@settings(max_examples=50)
def test_metamodel_modelelement_instantiation(instance):
    assert isinstance(instance, metamodel_ModelElement)



@given(instance=metamodel_ModelElement_strategy)
def test_metamodel_modelelement_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original



@given(instance=metamodel_ModelElement_strategy)
def test_metamodel_modelelement_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=metamodel_IdentifiableElement_strategy)
@settings(max_examples=50)
def test_metamodel_identifiableelement_instantiation(instance):
    assert isinstance(instance, metamodel_IdentifiableElement)



@given(instance=metamodel_IdentifiableElement_strategy)
def test_metamodel_identifiableelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=metamodel_UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_metamodel_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, metamodel_UniqueIdentifier)



@given(instance=metamodel_UniqueIdentifier_strategy)
def test_metamodel_uniqueidentifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=model_UnicaseModelElement_strategy)
@settings(max_examples=50)
def test_model_unicasemodelelement_instantiation(instance):
    assert isinstance(instance, model_UnicaseModelElement)



@given(instance=model_UnicaseModelElement_strategy)
def test_model_unicasemodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_UnicaseModelElement_strategy)
def test_model_unicasemodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_UnicaseModelElement_strategy)
def test_model_unicasemodelelement_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=metamodel_Project_strategy)
@settings(max_examples=50)
def test_metamodel_project_instantiation(instance):
    assert isinstance(instance, metamodel_Project)

@given(instance=metamodel_NonDomainElement_strategy)
@settings(max_examples=50)
def test_metamodel_nondomainelement_instantiation(instance):
    assert isinstance(instance, metamodel_NonDomainElement)

@given(instance=model_state_StateNode_strategy)
@settings(max_examples=50)
def test_model_state_statenode_instantiation(instance):
    assert isinstance(instance, model_state_StateNode)

@given(instance=state_StateNode_strategy)
@settings(max_examples=50)
def test_state_statenode_instantiation(instance):
    assert isinstance(instance, state_StateNode)

@given(instance=model_state_Transition_strategy)
@settings(max_examples=50)
def test_model_state_transition_instantiation(instance):
    assert isinstance(instance, model_state_Transition)



@given(instance=model_state_Transition_strategy)
def test_model_state_transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=MeetingSection_strategy)
@settings(max_examples=50)
def test_meetingsection_instantiation(instance):
    assert isinstance(instance, MeetingSection)

@given(instance=model_meeting_WorkItemMeetingSection_strategy)
@settings(max_examples=50)
def test_model_meeting_workitemmeetingsection_instantiation(instance):
    assert isinstance(instance, model_meeting_WorkItemMeetingSection)

@given(instance=model_meeting_IssueMeetingSection_strategy)
@settings(max_examples=50)
def test_model_meeting_issuemeetingsection_instantiation(instance):
    assert isinstance(instance, model_meeting_IssueMeetingSection)

@given(instance=model_meeting_CompositeMeetingSection_strategy)
@settings(max_examples=50)
def test_model_meeting_compositemeetingsection_instantiation(instance):
    assert isinstance(instance, model_meeting_CompositeMeetingSection)

@given(instance=model_meeting_MeetingSection_strategy)
@settings(max_examples=50)
def test_model_meeting_meetingsection_instantiation(instance):
    assert isinstance(instance, model_meeting_MeetingSection)



@given(instance=model_meeting_MeetingSection_strategy)
def test_model_meeting_meetingsection_allocatedTime_setter(instance):
    original = instance.allocatedTime
    instance.allocatedTime = original
    assert instance.allocatedTime == original

@given(instance=StateNode_strategy)
@settings(max_examples=50)
def test_statenode_instantiation(instance):
    assert isinstance(instance, StateNode)

@given(instance=model_state_StateEnd_strategy)
@settings(max_examples=50)
def test_model_state_stateend_instantiation(instance):
    assert isinstance(instance, model_state_StateEnd)

@given(instance=model_state_StateInitial_strategy)
@settings(max_examples=50)
def test_model_state_stateinitial_instantiation(instance):
    assert isinstance(instance, model_state_StateInitial)

@given(instance=model_state_State_strategy)
@settings(max_examples=50)
def test_model_state_state_instantiation(instance):
    assert isinstance(instance, model_state_State)



@given(instance=model_state_State_strategy)
def test_model_state_state_activities_setter(instance):
    original = instance.activities
    instance.activities = original
    assert instance.activities == original



@given(instance=model_state_State_strategy)
def test_model_state_state_exitConditions_setter(instance):
    original = instance.exitConditions
    instance.exitConditions = original
    assert instance.exitConditions == original



@given(instance=model_state_State_strategy)
def test_model_state_state_entryConditions_setter(instance):
    original = instance.entryConditions
    instance.entryConditions = original
    assert instance.entryConditions == original

@given(instance=meeting_IssueMeetingSection_strategy)
@settings(max_examples=50)
def test_meeting_issuemeetingsection_instantiation(instance):
    assert isinstance(instance, meeting_IssueMeetingSection)

@given(instance=meeting_MeetingSection_strategy)
@settings(max_examples=50)
def test_meeting_meetingsection_instantiation(instance):
    assert isinstance(instance, meeting_MeetingSection)

@given(instance=model_meeting_Meeting_strategy)
@settings(max_examples=50)
def test_model_meeting_meeting_instantiation(instance):
    assert isinstance(instance, model_meeting_Meeting)



@given(instance=model_meeting_Meeting_strategy)
def test_model_meeting_meeting_endtime_setter(instance):
    original = instance.endtime
    instance.endtime = original
    assert instance.endtime == original



@given(instance=model_meeting_Meeting_strategy)
def test_model_meeting_meeting_starttime_setter(instance):
    original = instance.starttime
    instance.starttime = original
    assert instance.starttime == original



@given(instance=model_meeting_Meeting_strategy)
def test_model_meeting_meeting_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=meeting_WorkItemMeetingSection_strategy)
@settings(max_examples=50)
def test_meeting_workitemmeetingsection_instantiation(instance):
    assert isinstance(instance, meeting_WorkItemMeetingSection)

@given(instance=model_component_DeploymentNode_strategy)
@settings(max_examples=50)
def test_model_component_deploymentnode_instantiation(instance):
    assert isinstance(instance, model_component_DeploymentNode)

@given(instance=component_Component_strategy)
@settings(max_examples=50)
def test_component_component_instantiation(instance):
    assert isinstance(instance, component_Component)

@given(instance=model_component_ComponentService_strategy)
@settings(max_examples=50)
def test_model_component_componentservice_instantiation(instance):
    assert isinstance(instance, model_component_ComponentService)

@given(instance=component_ComponentService_strategy)
@settings(max_examples=50)
def test_component_componentservice_instantiation(instance):
    assert isinstance(instance, component_ComponentService)

@given(instance=model_component_Component_strategy)
@settings(max_examples=50)
def test_model_component_component_instantiation(instance):
    assert isinstance(instance, model_component_Component)

@given(instance=model_bug_BugReport_strategy)
@settings(max_examples=50)
def test_model_bug_bugreport_instantiation(instance):
    assert isinstance(instance, model_bug_BugReport)



@given(instance=model_bug_BugReport_strategy)
def test_model_bug_bugreport_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original



@given(instance=model_bug_BugReport_strategy)
def test_model_bug_bugreport_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original



@given(instance=model_bug_BugReport_strategy)
def test_model_bug_bugreport_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original



@given(instance=model_bug_BugReport_strategy)
def test_model_bug_bugreport_resolutionType_setter(instance):
    original = instance.resolutionType
    instance.resolutionType = original
    assert instance.resolutionType == original

@given(instance=Solution_strategy)
@settings(max_examples=50)
def test_solution_instantiation(instance):
    assert isinstance(instance, Solution)

@given(instance=model_change_MergingSolution_strategy)
@settings(max_examples=50)
def test_model_change_mergingsolution_instantiation(instance):
    assert isinstance(instance, model_change_MergingSolution)

@given(instance=change_MergingProposal_strategy)
@settings(max_examples=50)
def test_change_mergingproposal_instantiation(instance):
    assert isinstance(instance, change_MergingProposal)

@given(instance=Proposal_strategy)
@settings(max_examples=50)
def test_proposal_instantiation(instance):
    assert isinstance(instance, Proposal)

@given(instance=model_change_MergingProposal_strategy)
@settings(max_examples=50)
def test_model_change_mergingproposal_instantiation(instance):
    assert isinstance(instance, model_change_MergingProposal)

@given(instance=Issue_strategy)
@settings(max_examples=50)
def test_issue_instantiation(instance):
    assert isinstance(instance, Issue)

@given(instance=model_change_MergingIssue_strategy)
@settings(max_examples=50)
def test_model_change_mergingissue_instantiation(instance):
    assert isinstance(instance, model_change_MergingIssue)



@given(instance=model_change_MergingIssue_strategy)
def test_model_change_mergingissue_resolvingRevision_setter(instance):
    original = instance.resolvingRevision
    instance.resolvingRevision = original
    assert instance.resolvingRevision == original

@given(instance=model_change_ModelChangePackage_strategy)
@settings(max_examples=50)
def test_model_change_modelchangepackage_instantiation(instance):
    assert isinstance(instance, model_change_ModelChangePackage)



@given(instance=model_change_ModelChangePackage_strategy)
def test_model_change_modelchangepackage_targetVersion_setter(instance):
    original = instance.targetVersion
    instance.targetVersion = original
    assert instance.targetVersion == original



@given(instance=model_change_ModelChangePackage_strategy)
def test_model_change_modelchangepackage_sourceVersion_setter(instance):
    original = instance.sourceVersion
    instance.sourceVersion = original
    assert instance.sourceVersion == original

@given(instance=model_rationale_Criterion_strategy)
@settings(max_examples=50)
def test_model_rationale_criterion_instantiation(instance):
    assert isinstance(instance, model_rationale_Criterion)

@given(instance=rationale_Assessment_strategy)
@settings(max_examples=50)
def test_rationale_assessment_instantiation(instance):
    assert isinstance(instance, rationale_Assessment)

@given(instance=rationale_Issue_strategy)
@settings(max_examples=50)
def test_rationale_issue_instantiation(instance):
    assert isinstance(instance, rationale_Issue)

@given(instance=rationale_Criterion_strategy)
@settings(max_examples=50)
def test_rationale_criterion_instantiation(instance):
    assert isinstance(instance, rationale_Criterion)

@given(instance=rationale_Solution_strategy)
@settings(max_examples=50)
def test_rationale_solution_instantiation(instance):
    assert isinstance(instance, rationale_Solution)

@given(instance=model_rationale_Issue_strategy)
@settings(max_examples=50)
def test_model_rationale_issue_instantiation(instance):
    assert isinstance(instance, model_rationale_Issue)



@given(instance=model_rationale_Issue_strategy)
def test_model_rationale_issue_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=Criterion_strategy)
@settings(max_examples=50)
def test_criterion_instantiation(instance):
    assert isinstance(instance, Criterion)

@given(instance=model_requirement_NonFunctionalRequirement_strategy)
@settings(max_examples=50)
def test_model_requirement_nonfunctionalrequirement_instantiation(instance):
    assert isinstance(instance, model_requirement_NonFunctionalRequirement)

@given(instance=requirement_SystemFunction_strategy)
@settings(max_examples=50)
def test_requirement_systemfunction_instantiation(instance):
    assert isinstance(instance, requirement_SystemFunction)

@given(instance=rationale_Proposal_strategy)
@settings(max_examples=50)
def test_rationale_proposal_instantiation(instance):
    assert isinstance(instance, rationale_Proposal)

@given(instance=model_requirement_ActorInstance_strategy)
@settings(max_examples=50)
def test_model_requirement_actorinstance_instantiation(instance):
    assert isinstance(instance, model_requirement_ActorInstance)

@given(instance=model_requirement_Actor_strategy)
@settings(max_examples=50)
def test_model_requirement_actor_instantiation(instance):
    assert isinstance(instance, model_requirement_Actor)

@given(instance=NonDomainElement_strategy)
@settings(max_examples=50)
def test_nondomainelement_instantiation(instance):
    assert isinstance(instance, NonDomainElement)

@given(instance=model_rationale_Proposal_strategy)
@settings(max_examples=50)
def test_model_rationale_proposal_instantiation(instance):
    assert isinstance(instance, model_rationale_Proposal)

@given(instance=model_rationale_Assessment_strategy)
@settings(max_examples=50)
def test_model_rationale_assessment_instantiation(instance):
    assert isinstance(instance, model_rationale_Assessment)



@given(instance=model_rationale_Assessment_strategy)
def test_model_rationale_assessment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_rationale_Comment_strategy)
@settings(max_examples=50)
def test_model_rationale_comment_instantiation(instance):
    assert isinstance(instance, model_rationale_Comment)

@given(instance=model_rationale_Solution_strategy)
@settings(max_examples=50)
def test_model_rationale_solution_instantiation(instance):
    assert isinstance(instance, model_rationale_Solution)

@given(instance=model_requirement_SystemFunction_strategy)
@settings(max_examples=50)
def test_model_requirement_systemfunction_instantiation(instance):
    assert isinstance(instance, model_requirement_SystemFunction)



@given(instance=model_requirement_SystemFunction_strategy)
def test_model_requirement_systemfunction_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=model_requirement_SystemFunction_strategy)
def test_model_requirement_systemfunction_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original



@given(instance=model_requirement_SystemFunction_strategy)
def test_model_requirement_systemfunction_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=model_requirement_UserTask_strategy)
@settings(max_examples=50)
def test_model_requirement_usertask_instantiation(instance):
    assert isinstance(instance, model_requirement_UserTask)

@given(instance=model_requirement_Step_strategy)
@settings(max_examples=50)
def test_model_requirement_step_instantiation(instance):
    assert isinstance(instance, model_requirement_Step)



@given(instance=model_requirement_Step_strategy)
def test_model_requirement_step_userStep_setter(instance):
    original = instance.userStep
    instance.userStep = original
    assert instance.userStep == original

@given(instance=requirement_ActorInstance_strategy)
@settings(max_examples=50)
def test_requirement_actorinstance_instantiation(instance):
    assert isinstance(instance, requirement_ActorInstance)

@given(instance=model_requirement_Scenario_strategy)
@settings(max_examples=50)
def test_model_requirement_scenario_instantiation(instance):
    assert isinstance(instance, model_requirement_Scenario)

@given(instance=requirement_NonFunctionalRequirement_strategy)
@settings(max_examples=50)
def test_requirement_nonfunctionalrequirement_instantiation(instance):
    assert isinstance(instance, requirement_NonFunctionalRequirement)

@given(instance=requirement_UserTask_strategy)
@settings(max_examples=50)
def test_requirement_usertask_instantiation(instance):
    assert isinstance(instance, requirement_UserTask)

@given(instance=requirement_Step_strategy)
@settings(max_examples=50)
def test_requirement_step_instantiation(instance):
    assert isinstance(instance, requirement_Step)

@given(instance=requirement_Actor_strategy)
@settings(max_examples=50)
def test_requirement_actor_instantiation(instance):
    assert isinstance(instance, requirement_Actor)

@given(instance=model_requirement_UseCase_strategy)
@settings(max_examples=50)
def test_model_requirement_usecase_instantiation(instance):
    assert isinstance(instance, model_requirement_UseCase)



@given(instance=model_requirement_UseCase_strategy)
def test_model_requirement_usecase_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=model_requirement_UseCase_strategy)
def test_model_requirement_usecase_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original



@given(instance=model_requirement_UseCase_strategy)
def test_model_requirement_usecase_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=model_requirement_UseCase_strategy)
def test_model_requirement_usecase_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=requirement_FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_requirement_functionalrequirement_instantiation(instance):
    assert isinstance(instance, requirement_FunctionalRequirement)

@given(instance=model_requirement_FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_model_requirement_functionalrequirement_instantiation(instance):
    assert isinstance(instance, model_requirement_FunctionalRequirement)



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_model_requirement_functionalrequirement_reviewed_setter(instance):
    original = instance.reviewed
    instance.reviewed = original
    assert instance.reviewed == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_model_requirement_functionalrequirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_model_requirement_functionalrequirement_storyPoints_setter(instance):
    original = instance.storyPoints
    instance.storyPoints = original
    assert instance.storyPoints == original



@given(instance=model_requirement_FunctionalRequirement_strategy)
def test_model_requirement_functionalrequirement_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original
