####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
ActivityType: Enumeration = Enumeration(
    name="ActivityType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="ANALYSIS"),
			EnumerationLiteral(name="SYSTEM_DESIGN"),
			EnumerationLiteral(name="OBJECT_DESIGN"),
			EnumerationLiteral(name="IMPLEMENTATION"),
			EnumerationLiteral(name="TESTING"),
			EnumerationLiteral(name="MANAGEMENT")
    }
)

DiagramType: Enumeration = Enumeration(
    name="DiagramType",
    literals={
            EnumerationLiteral(name="WORKITEM_DIAGRAM"),
			EnumerationLiteral(name="CLASS_DIAGRAM"),
			EnumerationLiteral(name="USECASE_DIAGRAM"),
			EnumerationLiteral(name="COMPONENT_DIAGRAM"),
			EnumerationLiteral(name="STATE_DIAGRAM"),
			EnumerationLiteral(name="ACTIVITY_DIAGRAM")
    }
)

AssociationType: Enumeration = Enumeration(
    name="AssociationType",
    literals={
            EnumerationLiteral(name="UNDIRECTED_ASSOCIATION"),
			EnumerationLiteral(name="DIRECTED_ASSOCIATION"),
			EnumerationLiteral(name="AGGREGATION"),
			EnumerationLiteral(name="COMPOSITION")
    }
)

VisibilityType: Enumeration = Enumeration(
    name="VisibilityType",
    literals={
            EnumerationLiteral(name="UNDEFINED"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="GLOBAL"),
			EnumerationLiteral(name="PROTECTED")
    }
)

ScopeType: Enumeration = Enumeration(
    name="ScopeType",
    literals={
            EnumerationLiteral(name="INSTANCE"),
			EnumerationLiteral(name="CLASS")
    }
)

ArgumentDirectionType: Enumeration = Enumeration(
    name="ArgumentDirectionType",
    literals={
            EnumerationLiteral(name="UNDEFINED"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

Severity: Enumeration = Enumeration(
    name="Severity",
    literals={
            EnumerationLiteral(name="FEATURE"),
			EnumerationLiteral(name="TRIVIAL"),
			EnumerationLiteral(name="MINOR"),
			EnumerationLiteral(name="MAJOR"),
			EnumerationLiteral(name="BLOCKER")
    }
)

ResolutionType: Enumeration = Enumeration(
    name="ResolutionType",
    literals={
            EnumerationLiteral(name="FIXED"),
			EnumerationLiteral(name="CANNOT_REPRODUCE"),
			EnumerationLiteral(name="WONT_FIX")
    }
)

FileAttachmentType: Enumeration = Enumeration(
    name="FileAttachmentType",
    literals={
            EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="IMAGE"),
			EnumerationLiteral(name="AUDIO"),
			EnumerationLiteral(name="VIDEO")
    }
)

ContainmentType: Enumeration = Enumeration(
    name="ContainmentType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="CONTAINER"),
			EnumerationLiteral(name="CONTAINMENT")
    }
)

MergeChoiceSelection: Enumeration = Enumeration(
    name="MergeChoiceSelection",
    literals={
            EnumerationLiteral(name="Mine"),
			EnumerationLiteral(name="Their"),
			EnumerationLiteral(name="Issue"),
			EnumerationLiteral(name="MergedText")
    }
)

MergeGlobalChoiceSelection: Enumeration = Enumeration(
    name="MergeGlobalChoiceSelection",
    literals={
            EnumerationLiteral(name="AllMine"),
			EnumerationLiteral(name="AllTheir"),
			EnumerationLiteral(name="Cancel"),
			EnumerationLiteral(name="OKNotFinished"),
			EnumerationLiteral(name="OKFinished")
    }
)

# Classes
Annotation = Class(name="Annotation")
metamodel_Project = Class(name="metamodel_Project")
ModelElement = Class(name="ModelElement")
metamodel_UniqueIdentifier = Class(name="metamodel_UniqueIdentifier", is_abstract=True)
metamodel_IdentifiableElement = Class(name="metamodel_IdentifiableElement", is_abstract=True)
metamodel_ModelElement = Class(name="metamodel_ModelElement", is_abstract=True)
IdentifiableElement = Class(name="IdentifiableElement")
metamodel_ModelElementId = Class(name="metamodel_ModelElementId")
UniqueIdentifier = Class(name="UniqueIdentifier")
metamodel_ModelVersion = Class(name="metamodel_ModelVersion")
metamodel_NonDomainElement = Class(name="metamodel_NonDomainElement", is_abstract=True)
metamodel_AssociationClassElement = Class(name="metamodel_AssociationClassElement", is_abstract=True)
model_UnicaseModelElement = Class(name="model_UnicaseModelElement", is_abstract=True)
task_WorkItem = Class(name="task_WorkItem")
Attachment = Class(name="Attachment")
document_LeafSection = Class(name="document_LeafSection")
rationale_Comment = Class(name="rationale_Comment")
profile_StereotypeInstance = Class(name="profile_StereotypeInstance")
model_Annotation = Class(name="model_Annotation", is_abstract=True)
UnicaseModelElement = Class(name="UnicaseModelElement")
model_Attachment = Class(name="model_Attachment", is_abstract=True)
model_NonDomainElement = Class(name="model_NonDomainElement", is_abstract=True)
model_Project = Class(name="model_Project")
Project = Class(name="Project")
model_organization_OrgUnit = Class(name="model_organization_OrgUnit", is_abstract=True)
organization_Group = Class(name="organization_Group")
organization_User = Class(name="organization_User")
model_organization_User = Class(name="model_organization_User")
OrgUnit = Class(name="OrgUnit")
model_organization_Group = Class(name="model_organization_Group")
organization_OrgUnit = Class(name="organization_OrgUnit")
model_task_WorkItem = Class(name="model_task_WorkItem", is_abstract=True)
task_WorkPackage = Class(name="task_WorkPackage")
change_ModelChangePackage = Class(name="change_ModelChangePackage")
model_task_WorkPackage = Class(name="model_task_WorkPackage")
WorkItem = Class(name="WorkItem")
model_task_Milestone = Class(name="model_task_Milestone")
model_classes_PackageElement = Class(name="model_classes_PackageElement", is_abstract=True)
model_task_Checkable = Class(name="model_task_Checkable", is_abstract=True)
model_task_ActionItem = Class(name="model_task_ActionItem")
task_Checkable = Class(name="task_Checkable")
model_diagram_MEDiagram = Class(name="model_diagram_MEDiagram")
diagram_model_Diagram = Class(name="diagram_model_Diagram")
classes_Attribute = Class(name="classes_Attribute")
classes_Package = Class(name="classes_Package")
classes_Dependency = Class(name="classes_Dependency")
model_classes_Class = Class(name="model_classes_Class")
PackageElement = Class(name="PackageElement")
classes_Class = Class(name="classes_Class")
classes_Association = Class(name="classes_Association")
classes_Method = Class(name="classes_Method")
requirement_UseCase = Class(name="requirement_UseCase")
requirement_Scenario = Class(name="requirement_Scenario")
model_classes_Package = Class(name="model_classes_Package")
classes_PackageElement = Class(name="classes_PackageElement")
model_classes_Association = Class(name="model_classes_Association")
model_classes_Attribute = Class(name="model_classes_Attribute")
model_classes_Method = Class(name="model_classes_Method")
classes_MethodArgument = Class(name="classes_MethodArgument")
model_classes_MethodArgument = Class(name="model_classes_MethodArgument")
model_requirement_FunctionalRequirement = Class(name="model_requirement_FunctionalRequirement")
model_classes_Dependency = Class(name="model_classes_Dependency")
model_document_Section = Class(name="model_document_Section", is_abstract=True)
document_CompositeSection = Class(name="document_CompositeSection")
model_document_LeafSection = Class(name="model_document_LeafSection")
Section = Class(name="Section")
model_document_CompositeSection = Class(name="model_document_CompositeSection")
document_Section = Class(name="document_Section")
requirement_FunctionalRequirement = Class(name="requirement_FunctionalRequirement")
model_requirement_UseCase = Class(name="model_requirement_UseCase")
model_requirement_Scenario = Class(name="model_requirement_Scenario")
requirement_Actor = Class(name="requirement_Actor")
requirement_Step = Class(name="requirement_Step")
requirement_UserTask = Class(name="requirement_UserTask")
requirement_NonFunctionalRequirement = Class(name="requirement_NonFunctionalRequirement")
requirement_SystemFunction = Class(name="requirement_SystemFunction")
requirement_ActorInstance = Class(name="requirement_ActorInstance")
model_requirement_Actor = Class(name="model_requirement_Actor")
requirement_Workspace = Class(name="requirement_Workspace")
model_requirement_UserTask = Class(name="model_requirement_UserTask")
model_requirement_ActorInstance = Class(name="model_requirement_ActorInstance")
model_requirement_Step = Class(name="model_requirement_Step")
NonDomainElement = Class(name="NonDomainElement")
model_requirement_SystemFunction = Class(name="model_requirement_SystemFunction")
model_rationale_Issue = Class(name="model_rationale_Issue")
model_requirement_NonFunctionalRequirement = Class(name="model_requirement_NonFunctionalRequirement")
Criterion = Class(name="Criterion")
model_requirement_Workspace = Class(name="model_requirement_Workspace")
model_rationale_Criterion = Class(name="model_rationale_Criterion")
rationale_Proposal = Class(name="rationale_Proposal")
rationale_Solution = Class(name="rationale_Solution")
rationale_Criterion = Class(name="rationale_Criterion")
model_rationale_Proposal = Class(name="model_rationale_Proposal")
rationale_Issue = Class(name="rationale_Issue")
rationale_Assessment = Class(name="rationale_Assessment")
model_rationale_Solution = Class(name="model_rationale_Solution")
Solution = Class(name="Solution")
model_bug_BugReport = Class(name="model_bug_BugReport")
model_rationale_Assessment = Class(name="model_rationale_Assessment")
model_rationale_Comment = Class(name="model_rationale_Comment")
model_rationale_AudioComment = Class(name="model_rationale_AudioComment")
attachment_FileAttachment = Class(name="attachment_FileAttachment")
model_change_ModelChangePackage = Class(name="model_change_ModelChangePackage")
model_change_MergingIssue = Class(name="model_change_MergingIssue")
Issue = Class(name="Issue")
model_change_MergingProposal = Class(name="model_change_MergingProposal")
Proposal = Class(name="Proposal")
change_MergingProposal = Class(name="change_MergingProposal")
model_change_MergingSolution = Class(name="model_change_MergingSolution")
model_component_DeploymentNode = Class(name="model_component_DeploymentNode")
model_component_Component = Class(name="model_component_Component")
component_ComponentService = Class(name="component_ComponentService")
model_component_ComponentService = Class(name="model_component_ComponentService")
component_Component = Class(name="component_Component")
model_meeting_MeetingSection = Class(name="model_meeting_MeetingSection", is_abstract=True)
model_meeting_CompositeMeetingSection = Class(name="model_meeting_CompositeMeetingSection")
model_meeting_Meeting = Class(name="model_meeting_Meeting")
meeting_MeetingSection = Class(name="meeting_MeetingSection")
meeting_IssueMeetingSection = Class(name="meeting_IssueMeetingSection")
meeting_WorkItemMeetingSection = Class(name="meeting_WorkItemMeetingSection")
model_attachment_FileAttachment = Class(name="model_attachment_FileAttachment")
MeetingSection = Class(name="MeetingSection")
model_meeting_IssueMeetingSection = Class(name="model_meeting_IssueMeetingSection")
model_meeting_WorkItemMeetingSection = Class(name="model_meeting_WorkItemMeetingSection")
model_state_Transition = Class(name="model_state_Transition")
state_StateNode = Class(name="state_StateNode")
model_state_StateNode = Class(name="model_state_StateNode", is_abstract=True)
state_Transition = Class(name="state_Transition")
model_state_State = Class(name="model_state_State")
StateNode = Class(name="StateNode")
model_state_StateInitial = Class(name="model_state_StateInitial")
model_state_StateEnd = Class(name="model_state_StateEnd")
model_attachment_UrlAttachment = Class(name="model_attachment_UrlAttachment")
profile_StereotypeAttribute = Class(name="profile_StereotypeAttribute")
model_profile_StereotypeInstance = Class(name="model_profile_StereotypeInstance")
model_profile_Profile = Class(name="model_profile_Profile")
profile_Stereotype = Class(name="profile_Stereotype")
model_profile_Stereotype = Class(name="model_profile_Stereotype")
profile_Profile = Class(name="profile_Profile")
profile_StereotypeAttributeInstance = Class(name="profile_StereotypeAttributeInstance")
model_profile_StereotypeAttribute = Class(name="model_profile_StereotypeAttribute", is_abstract=True)
model_profile_StereotypeAttributeSimple = Class(name="model_profile_StereotypeAttributeSimple")
StereotypeAttribute = Class(name="StereotypeAttribute")
model_profile_StereotypeAttributeInstance = Class(name="model_profile_StereotypeAttributeInstance", is_abstract=True)
model_profile_StereotypeAttributeInstanceString = Class(name="model_profile_StereotypeAttributeInstanceString")
StereotypeAttributeInstance = Class(name="StereotypeAttributeInstance")
model_util_ModelElementPath = Class(name="model_util_ModelElementPath")
ModelElementId = Class(name="ModelElementId")
model_activity_ActivityObject = Class(name="model_activity_ActivityObject", is_abstract=True)
activity_Transition = Class(name="activity_Transition")
model_activity_Transition = Class(name="model_activity_Transition")
activity_ActivityObject = Class(name="activity_ActivityObject")
esmodel_ProjectId = Class(name="esmodel_ProjectId")
esmodel_VersionInfo = Class(name="esmodel_VersionInfo")
esmodel_ClientVersionInfo = Class(name="esmodel_ClientVersionInfo")
model_activity_Activity = Class(name="model_activity_Activity")
ActivityObject = Class(name="ActivityObject")
model_activity_Fork = Class(name="model_activity_Fork")
model_activity_Branch = Class(name="model_activity_Branch")
model_activity_ActivityInitial = Class(name="model_activity_ActivityInitial")
model_activity_ActivityEnd = Class(name="model_activity_ActivityEnd")
esmodel_ProjectHistory = Class(name="esmodel_ProjectHistory")
ProjectId = Class(name="ProjectId")
versioning_Version = Class(name="versioning_Version")
esmodel_ProjectInfo = Class(name="esmodel_ProjectInfo")
versioning_PrimaryVersionSpec = Class(name="versioning_PrimaryVersionSpec")
esmodel_SessionId = Class(name="esmodel_SessionId")
esmodel_ServerSpace = Class(name="esmodel_ServerSpace")
accesscontrol_ACGroup = Class(name="accesscontrol_ACGroup")
ProjectHistory = Class(name="ProjectHistory")
SessionId = Class(name="SessionId")
accesscontrol_ACUser = Class(name="accesscontrol_ACUser")
versioning_ChangePackage = Class(name="versioning_ChangePackage")
esmodel_versioning_HistoryQuery = Class(name="esmodel_versioning_HistoryQuery")
esmodel_FileIdentifier = Class(name="esmodel_FileIdentifier")
esmodel_versioning_TagVersionSpec = Class(name="esmodel_versioning_TagVersionSpec")
VersionSpec = Class(name="VersionSpec")
esmodel_versioning_DateVersionSpec = Class(name="esmodel_versioning_DateVersionSpec")
esmodel_versioning_PrimaryVersionSpec = Class(name="esmodel_versioning_PrimaryVersionSpec")
esmodel_versioning_VersionSpec = Class(name="esmodel_versioning_VersionSpec", is_abstract=True)
esmodel_versioning_LogMessage = Class(name="esmodel_versioning_LogMessage")
esmodel_versioning_ChangePackage = Class(name="esmodel_versioning_ChangePackage")
operations_AbstractOperation = Class(name="operations_AbstractOperation")
events_Event = Class(name="events_Event")
versioning_LogMessage = Class(name="versioning_LogMessage")
notification_ESNotification = Class(name="notification_ESNotification")
versioning_VersionProperty = Class(name="versioning_VersionProperty")
esmodel_versioning_HistoryInfo = Class(name="esmodel_versioning_HistoryInfo")
versioning_TagVersionSpec = Class(name="versioning_TagVersionSpec")
esmodel_operations_FeatureOperation = Class(name="esmodel_operations_FeatureOperation", is_abstract=True)
esmodel_versioning_Version = Class(name="esmodel_versioning_Version")
esmodel_versioning_HeadVersionSpec = Class(name="esmodel_versioning_HeadVersionSpec")
esmodel_versioning_VersionProperty = Class(name="esmodel_versioning_VersionProperty")
esmodel_operations_AbstractOperation = Class(name="esmodel_operations_AbstractOperation", is_abstract=True)
esmodel_operations_CompositeOperation = Class(name="esmodel_operations_CompositeOperation")
AbstractOperation = Class(name="AbstractOperation")
esmodel_operations_MultiAttributeSetOperation = Class(name="esmodel_operations_MultiAttributeSetOperation")
esmodel_operations_MultiAttributeMoveOperation = Class(name="esmodel_operations_MultiAttributeMoveOperation")
esmodel_operations_SingleReferenceOperation = Class(name="esmodel_operations_SingleReferenceOperation")
ReferenceOperation = Class(name="ReferenceOperation")
esmodel_operations_MultiReferenceSetOperation = Class(name="esmodel_operations_MultiReferenceSetOperation")
esmodel_operations_CreateDeleteOperation = Class(name="esmodel_operations_CreateDeleteOperation")
operations_esmodel_EObject = Class(name="operations_esmodel_EObject")
operations_ReferenceOperation = Class(name="operations_ReferenceOperation")
operations_EObjectToModelElementIdMap = Class(name="operations_EObjectToModelElementIdMap")
esmodel_operations_AttributeOperation = Class(name="esmodel_operations_AttributeOperation")
FeatureOperation = Class(name="FeatureOperation")
esmodel_operations_MultiAttributeOperation = Class(name="esmodel_operations_MultiAttributeOperation")
esmodel_operations_ModelElementGroup = Class(name="esmodel_operations_ModelElementGroup")
esmodel_operations_EObjectToModelElementIdMap = Class(name="esmodel_operations_EObjectToModelElementIdMap")
esmodel_semantic_SemanticCompositeOperation = Class(name="esmodel_semantic_SemanticCompositeOperation", is_abstract=True)
esmodel_operations_MultiReferenceOperation = Class(name="esmodel_operations_MultiReferenceOperation")
esmodel_operations_MultiReferenceMoveOperation = Class(name="esmodel_operations_MultiReferenceMoveOperation")
esmodel_operations_ReferenceOperation = Class(name="esmodel_operations_ReferenceOperation", is_abstract=True)
esmodel_operations_DiagramLayoutOperation = Class(name="esmodel_operations_DiagramLayoutOperation")
AttributeOperation = Class(name="AttributeOperation")
esmodel_operations_OperationId = Class(name="esmodel_operations_OperationId")
esmodel_operations_OperationGroup = Class(name="esmodel_operations_OperationGroup")
esmodel_events_PluginStartEvent = Class(name="esmodel_events_PluginStartEvent")
esmodel_events_UpdateEvent = Class(name="esmodel_events_UpdateEvent")
esmodel_events_AnnotationEvent = Class(name="esmodel_events_AnnotationEvent")
esmodel_events_RevertEvent = Class(name="esmodel_events_RevertEvent")
CompositeOperation = Class(name="CompositeOperation")
esmodel_events_ShowHistoryEvent = Class(name="esmodel_events_ShowHistoryEvent")
esmodel_events_Event = Class(name="esmodel_events_Event")
esmodel_events_ReadEvent = Class(name="esmodel_events_ReadEvent")
Event = Class(name="Event")
esmodel_events_MergeEvent = Class(name="esmodel_events_MergeEvent")
esmodel_events_CheckoutEvent = Class(name="esmodel_events_CheckoutEvent")
esmodel_events_ExceptionEvent = Class(name="esmodel_events_ExceptionEvent")
esmodel_events_NavigatorCreateEvent = Class(name="esmodel_events_NavigatorCreateEvent")
esmodel_events_PluginFocusEvent = Class(name="esmodel_events_PluginFocusEvent")
esmodel_events_PresentationSwitchEvent = Class(name="esmodel_events_PresentationSwitchEvent")
esmodel_events_PerspectiveEvent = Class(name="esmodel_events_PerspectiveEvent")
esmodel_events_DNDEvent = Class(name="esmodel_events_DNDEvent")
esmodel_events_LinkEvent = Class(name="esmodel_events_LinkEvent")
esmodel_events_TraceEvent = Class(name="esmodel_events_TraceEvent")
esmodel_events_MergeChoiceEvent = Class(name="esmodel_events_MergeChoiceEvent")
operations_OperationId = Class(name="operations_OperationId")
esmodel_events_UndoEvent = Class(name="esmodel_events_UndoEvent")
esmodel_events_Validate = Class(name="esmodel_events_Validate")
esmodel_events_ShowChangesEvent = Class(name="esmodel_events_ShowChangesEvent")
esmodel_events_NotificationReadEvent = Class(name="esmodel_events_NotificationReadEvent")
ReadEvent = Class(name="ReadEvent")
esmodel_events_NotificationGenerationEvent = Class(name="esmodel_events_NotificationGenerationEvent")
esmodel_events_NotificationIgnoreEvent = Class(name="esmodel_events_NotificationIgnoreEvent")
esmodel_events_URLEvent = Class(name="esmodel_events_URLEvent")
accesscontrol_OrgUnitProperty = Class(name="accesscontrol_OrgUnitProperty")
esmodel_accesscontrol_ACGroup = Class(name="esmodel_accesscontrol_ACGroup")
accesscontrol_ACOrgUnit = Class(name="accesscontrol_ACOrgUnit")
esmodel_accesscontrol_ACOrgUnitId = Class(name="esmodel_accesscontrol_ACOrgUnitId")
esmodel_accesscontrol_OrgUnitProperty = Class(name="esmodel_accesscontrol_OrgUnitProperty")
esmodel_roles_Role = Class(name="esmodel_roles_Role", is_abstract=True)
esmodel_events_MergeGlobalChoiceEvent = Class(name="esmodel_events_MergeGlobalChoiceEvent")
esmodel_server_ServerEvent = Class(name="esmodel_server_ServerEvent", is_abstract=True)
esmodel_server_ServerProjectEvent = Class(name="esmodel_server_ServerProjectEvent", is_abstract=True)
ServerEvent = Class(name="ServerEvent")
esmodel_server_ProjectUpdatedEvent = Class(name="esmodel_server_ProjectUpdatedEvent")
ServerProjectEvent = Class(name="ServerProjectEvent")
esmodel_accesscontrol_ACUser = Class(name="esmodel_accesscontrol_ACUser")
ACOrgUnit = Class(name="ACOrgUnit")
esmodel_accesscontrol_ACOrgUnit = Class(name="esmodel_accesscontrol_ACOrgUnit")
roles_Role = Class(name="roles_Role")
esmodel_url_ServerUrl = Class(name="esmodel_url_ServerUrl")
esmodel_url_ProjectUrlFragment = Class(name="esmodel_url_ProjectUrlFragment")
esmodel_url_ModelElementUrlFragment = Class(name="esmodel_url_ModelElementUrlFragment")
esmodel_roles_ReaderRole = Class(name="esmodel_roles_ReaderRole")
Role = Class(name="Role")
esmodel_roles_WriterRole = Class(name="esmodel_roles_WriterRole")
esmodel_roles_ProjectAdminRole = Class(name="esmodel_roles_ProjectAdminRole")
esmodel_roles_ServerAdmin = Class(name="esmodel_roles_ServerAdmin")
esmodel_notification_ESNotification = Class(name="esmodel_notification_ESNotification")
esmodel_url_ModelElementUrl = Class(name="esmodel_url_ModelElementUrl")
url_ServerUrl = Class(name="url_ServerUrl")
url_ProjectUrlFragment = Class(name="url_ProjectUrlFragment")
url_ModelElementUrlFragment = Class(name="url_ModelElementUrlFragment")

# Annotation class attributes and methods

# metamodel_Project class attributes and methods

# ModelElement class attributes and methods

# metamodel_UniqueIdentifier class attributes and methods
metamodel_UniqueIdentifier_id: Property = Property(name="id", type=StringType)
metamodel_UniqueIdentifier.attributes={metamodel_UniqueIdentifier_id}

# metamodel_IdentifiableElement class attributes and methods
metamodel_IdentifiableElement_identifier: Property = Property(name="identifier", type=StringType)
metamodel_IdentifiableElement.attributes={metamodel_IdentifiableElement_identifier}

# metamodel_ModelElement class attributes and methods
metamodel_ModelElement_creator: Property = Property(name="creator", type=StringType)
metamodel_ModelElement_creationDate: Property = Property(name="creationDate", type=DateType)
metamodel_ModelElement.attributes={metamodel_ModelElement_creator, metamodel_ModelElement_creationDate}

# IdentifiableElement class attributes and methods

# metamodel_ModelElementId class attributes and methods

# UniqueIdentifier class attributes and methods

# metamodel_ModelVersion class attributes and methods
metamodel_ModelVersion_releaseNumber: Property = Property(name="releaseNumber", type=IntegerType)
metamodel_ModelVersion.attributes={metamodel_ModelVersion_releaseNumber}

# metamodel_NonDomainElement class attributes and methods

# metamodel_AssociationClassElement class attributes and methods

# model_UnicaseModelElement class attributes and methods
model_UnicaseModelElement_state: Property = Property(name="state", type=StringType)
model_UnicaseModelElement_name: Property = Property(name="name", type=StringType)
model_UnicaseModelElement_description: Property = Property(name="description", type=StringType)
model_UnicaseModelElement.attributes={model_UnicaseModelElement_state, model_UnicaseModelElement_description, model_UnicaseModelElement_name}

# task_WorkItem class attributes and methods

# Attachment class attributes and methods

# document_LeafSection class attributes and methods

# rationale_Comment class attributes and methods

# profile_StereotypeInstance class attributes and methods

# model_Annotation class attributes and methods

# UnicaseModelElement class attributes and methods

# model_Attachment class attributes and methods

# model_NonDomainElement class attributes and methods

# model_Project class attributes and methods

# Project class attributes and methods

# model_organization_OrgUnit class attributes and methods
model_organization_OrgUnit_acOrgId: Property = Property(name="acOrgId", type=StringType)
model_organization_OrgUnit.attributes={model_organization_OrgUnit_acOrgId}

# organization_Group class attributes and methods

# organization_User class attributes and methods

# model_organization_User class attributes and methods
model_organization_User_email: Property = Property(name="email", type=StringType)
model_organization_User_firstName: Property = Property(name="firstName", type=StringType)
model_organization_User_lastName: Property = Property(name="lastName", type=StringType)
model_organization_User.attributes={model_organization_User_firstName, model_organization_User_lastName, model_organization_User_email}

# OrgUnit class attributes and methods

# model_organization_Group class attributes and methods

# organization_OrgUnit class attributes and methods

# model_task_WorkItem class attributes and methods
model_task_WorkItem_dueDate: Property = Property(name="dueDate", type=DateType)
model_task_WorkItem_estimate: Property = Property(name="estimate", type=IntegerType)
model_task_WorkItem_effort: Property = Property(name="effort", type=IntegerType)
model_task_WorkItem_priority: Property = Property(name="priority", type=IntegerType)
model_task_WorkItem_resolved: Property = Property(name="resolved", type=BooleanType)
model_task_WorkItem.attributes={model_task_WorkItem_priority, model_task_WorkItem_effort, model_task_WorkItem_dueDate, model_task_WorkItem_resolved, model_task_WorkItem_estimate}

# task_WorkPackage class attributes and methods

# change_ModelChangePackage class attributes and methods

# model_task_WorkPackage class attributes and methods
model_task_WorkPackage_startDate: Property = Property(name="startDate", type=DateType)
model_task_WorkPackage_endDate: Property = Property(name="endDate", type=DateType)
model_task_WorkPackage.attributes={model_task_WorkPackage_startDate, model_task_WorkPackage_endDate}

# WorkItem class attributes and methods

# model_task_Milestone class attributes and methods

# model_classes_PackageElement class attributes and methods

# model_task_Checkable class attributes and methods
model_task_Checkable_checked: Property = Property(name="checked", type=BooleanType)
model_task_Checkable.attributes={model_task_Checkable_checked}

# model_task_ActionItem class attributes and methods
model_task_ActionItem_done: Property = Property(name="done", type=BooleanType)
model_task_ActionItem_activity: Property = Property(name="activity", type=StringType)
model_task_ActionItem.attributes={model_task_ActionItem_done, model_task_ActionItem_activity}

# task_Checkable class attributes and methods

# model_diagram_MEDiagram class attributes and methods
model_diagram_MEDiagram_diagramLayout: Property = Property(name="diagramLayout", type=StringType)
model_diagram_MEDiagram_type: Property = Property(name="type", type=StringType)
model_diagram_MEDiagram.attributes={model_diagram_MEDiagram_diagramLayout, model_diagram_MEDiagram_type}

# diagram_model_Diagram class attributes and methods

# classes_Attribute class attributes and methods

# classes_Package class attributes and methods

# classes_Dependency class attributes and methods

# model_classes_Class class attributes and methods

# PackageElement class attributes and methods

# classes_Class class attributes and methods

# classes_Association class attributes and methods

# classes_Method class attributes and methods

# requirement_UseCase class attributes and methods

# requirement_Scenario class attributes and methods

# model_classes_Package class attributes and methods

# classes_PackageElement class attributes and methods

# model_classes_Association class attributes and methods
model_classes_Association_targetMultiplicity: Property = Property(name="targetMultiplicity", type=StringType)
model_classes_Association_sourceRole: Property = Property(name="sourceRole", type=StringType)
model_classes_Association_targetRole: Property = Property(name="targetRole", type=StringType)
model_classes_Association_sourceMultiplicity: Property = Property(name="sourceMultiplicity", type=StringType)
model_classes_Association_type: Property = Property(name="type", type=StringType)
model_classes_Association.attributes={model_classes_Association_targetMultiplicity, model_classes_Association_type, model_classes_Association_sourceRole, model_classes_Association_sourceMultiplicity, model_classes_Association_targetRole}

# model_classes_Attribute class attributes and methods
model_classes_Attribute_signature: Property = Property(name="signature", type=StringType)
model_classes_Attribute_type: Property = Property(name="type", type=StringType)
model_classes_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_Attribute_properties: Property = Property(name="properties", type=StringType)
model_classes_Attribute_label: Property = Property(name="label", type=StringType)
model_classes_Attribute_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Attribute_scope: Property = Property(name="scope", type=StringType)
model_classes_Attribute.attributes={model_classes_Attribute_signature, model_classes_Attribute_label, model_classes_Attribute_type, model_classes_Attribute_scope, model_classes_Attribute_properties, model_classes_Attribute_visibility, model_classes_Attribute_defaultValue}

# model_classes_Method class attributes and methods
model_classes_Method_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Method_scope: Property = Property(name="scope", type=StringType)
model_classes_Method_returnType: Property = Property(name="returnType", type=StringType)
model_classes_Method_signature: Property = Property(name="signature", type=StringType)
model_classes_Method_properties: Property = Property(name="properties", type=StringType)
model_classes_Method_label: Property = Property(name="label", type=StringType)
model_classes_Method_stubbed: Property = Property(name="stubbed", type=BooleanType)
model_classes_Method.attributes={model_classes_Method_visibility, model_classes_Method_stubbed, model_classes_Method_signature, model_classes_Method_returnType, model_classes_Method_properties, model_classes_Method_scope, model_classes_Method_label}

# classes_MethodArgument class attributes and methods

# model_classes_MethodArgument class attributes and methods
model_classes_MethodArgument_signature: Property = Property(name="signature", type=StringType)
model_classes_MethodArgument_label: Property = Property(name="label", type=StringType)
model_classes_MethodArgument_direction: Property = Property(name="direction", type=StringType)
model_classes_MethodArgument_type: Property = Property(name="type", type=StringType)
model_classes_MethodArgument_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_MethodArgument.attributes={model_classes_MethodArgument_direction, model_classes_MethodArgument_defaultValue, model_classes_MethodArgument_signature, model_classes_MethodArgument_type, model_classes_MethodArgument_label}

# model_requirement_FunctionalRequirement class attributes and methods
model_requirement_FunctionalRequirement_storyPoints: Property = Property(name="storyPoints", type=IntegerType)
model_requirement_FunctionalRequirement_priority: Property = Property(name="priority", type=IntegerType)
model_requirement_FunctionalRequirement_reviewed: Property = Property(name="reviewed", type=BooleanType)
model_requirement_FunctionalRequirement_cost: Property = Property(name="cost", type=IntegerType)
model_requirement_FunctionalRequirement.attributes={model_requirement_FunctionalRequirement_reviewed, model_requirement_FunctionalRequirement_cost, model_requirement_FunctionalRequirement_priority, model_requirement_FunctionalRequirement_storyPoints}

# model_classes_Dependency class attributes and methods

# model_document_Section class attributes and methods

# document_CompositeSection class attributes and methods

# model_document_LeafSection class attributes and methods

# Section class attributes and methods

# model_document_CompositeSection class attributes and methods

# document_Section class attributes and methods

# requirement_FunctionalRequirement class attributes and methods

# model_requirement_UseCase class attributes and methods
model_requirement_UseCase_precondition: Property = Property(name="precondition", type=StringType)
model_requirement_UseCase_postcondition: Property = Property(name="postcondition", type=StringType)
model_requirement_UseCase_rules: Property = Property(name="rules", type=StringType)
model_requirement_UseCase_exception: Property = Property(name="exception", type=StringType)
model_requirement_UseCase.attributes={model_requirement_UseCase_exception, model_requirement_UseCase_rules, model_requirement_UseCase_postcondition, model_requirement_UseCase_precondition}

# model_requirement_Scenario class attributes and methods

# requirement_Actor class attributes and methods

# requirement_Step class attributes and methods

# requirement_UserTask class attributes and methods

# requirement_NonFunctionalRequirement class attributes and methods

# requirement_SystemFunction class attributes and methods

# requirement_ActorInstance class attributes and methods

# model_requirement_Actor class attributes and methods

# requirement_Workspace class attributes and methods

# model_requirement_UserTask class attributes and methods

# model_requirement_ActorInstance class attributes and methods

# model_requirement_Step class attributes and methods
model_requirement_Step_userStep: Property = Property(name="userStep", type=BooleanType)
model_requirement_Step.attributes={model_requirement_Step_userStep}

# NonDomainElement class attributes and methods

# model_requirement_SystemFunction class attributes and methods
model_requirement_SystemFunction_input: Property = Property(name="input", type=StringType)
model_requirement_SystemFunction_output: Property = Property(name="output", type=StringType)
model_requirement_SystemFunction_exception: Property = Property(name="exception", type=StringType)
model_requirement_SystemFunction.attributes={model_requirement_SystemFunction_output, model_requirement_SystemFunction_exception, model_requirement_SystemFunction_input}

# model_rationale_Issue class attributes and methods
model_rationale_Issue_activity: Property = Property(name="activity", type=StringType)
model_rationale_Issue.attributes={model_rationale_Issue_activity}

# model_requirement_NonFunctionalRequirement class attributes and methods

# Criterion class attributes and methods

# model_requirement_Workspace class attributes and methods

# model_rationale_Criterion class attributes and methods

# rationale_Proposal class attributes and methods

# rationale_Solution class attributes and methods

# rationale_Criterion class attributes and methods

# model_rationale_Proposal class attributes and methods

# rationale_Issue class attributes and methods

# rationale_Assessment class attributes and methods

# model_rationale_Solution class attributes and methods

# Solution class attributes and methods

# model_bug_BugReport class attributes and methods
model_bug_BugReport_resolution: Property = Property(name="resolution", type=StringType)
model_bug_BugReport_severity: Property = Property(name="severity", type=StringType)
model_bug_BugReport_resolutionType: Property = Property(name="resolutionType", type=StringType)
model_bug_BugReport_done: Property = Property(name="done", type=BooleanType)
model_bug_BugReport.attributes={model_bug_BugReport_resolution, model_bug_BugReport_done, model_bug_BugReport_resolutionType, model_bug_BugReport_severity}

# model_rationale_Assessment class attributes and methods
model_rationale_Assessment_value: Property = Property(name="value", type=IntegerType)
model_rationale_Assessment.attributes={model_rationale_Assessment_value}

# model_rationale_Comment class attributes and methods

# model_rationale_AudioComment class attributes and methods

# attachment_FileAttachment class attributes and methods

# model_change_ModelChangePackage class attributes and methods
model_change_ModelChangePackage_sourceVersion: Property = Property(name="sourceVersion", type=IntegerType)
model_change_ModelChangePackage_targetVersion: Property = Property(name="targetVersion", type=IntegerType)
model_change_ModelChangePackage.attributes={model_change_ModelChangePackage_targetVersion, model_change_ModelChangePackage_sourceVersion}

# model_change_MergingIssue class attributes and methods
model_change_MergingIssue_resolvingRevision: Property = Property(name="resolvingRevision", type=IntegerType)
model_change_MergingIssue.attributes={model_change_MergingIssue_resolvingRevision}

# Issue class attributes and methods

# model_change_MergingProposal class attributes and methods

# Proposal class attributes and methods

# change_MergingProposal class attributes and methods

# model_change_MergingSolution class attributes and methods

# model_component_DeploymentNode class attributes and methods

# model_component_Component class attributes and methods

# component_ComponentService class attributes and methods

# model_component_ComponentService class attributes and methods

# component_Component class attributes and methods

# model_meeting_MeetingSection class attributes and methods
model_meeting_MeetingSection_allocatedTime: Property = Property(name="allocatedTime", type=IntegerType)
model_meeting_MeetingSection.attributes={model_meeting_MeetingSection_allocatedTime}

# model_meeting_CompositeMeetingSection class attributes and methods

# model_meeting_Meeting class attributes and methods
model_meeting_Meeting_location: Property = Property(name="location", type=StringType)
model_meeting_Meeting_starttime: Property = Property(name="starttime", type=DateType)
model_meeting_Meeting_endtime: Property = Property(name="endtime", type=DateType)
model_meeting_Meeting.attributes={model_meeting_Meeting_location, model_meeting_Meeting_endtime, model_meeting_Meeting_starttime}

# meeting_MeetingSection class attributes and methods

# meeting_IssueMeetingSection class attributes and methods

# meeting_WorkItemMeetingSection class attributes and methods

# model_attachment_FileAttachment class attributes and methods
model_attachment_FileAttachment_fileName: Property = Property(name="fileName", type=StringType)
model_attachment_FileAttachment_fileHash: Property = Property(name="fileHash", type=StringType)
model_attachment_FileAttachment_fileID: Property = Property(name="fileID", type=StringType)
model_attachment_FileAttachment_fileSize: Property = Property(name="fileSize", type=StringType)
model_attachment_FileAttachment_requiredOffline: Property = Property(name="requiredOffline", type=BooleanType)
model_attachment_FileAttachment_fileType: Property = Property(name="fileType", type=StringType)
model_attachment_FileAttachment_uploading: Property = Property(name="uploading", type=BooleanType)
model_attachment_FileAttachment_downloading: Property = Property(name="downloading", type=BooleanType)
model_attachment_FileAttachment.attributes={model_attachment_FileAttachment_fileType, model_attachment_FileAttachment_fileName, model_attachment_FileAttachment_fileID, model_attachment_FileAttachment_downloading, model_attachment_FileAttachment_fileHash, model_attachment_FileAttachment_requiredOffline, model_attachment_FileAttachment_uploading, model_attachment_FileAttachment_fileSize}

# MeetingSection class attributes and methods

# model_meeting_IssueMeetingSection class attributes and methods

# model_meeting_WorkItemMeetingSection class attributes and methods

# model_state_Transition class attributes and methods
model_state_Transition_condition: Property = Property(name="condition", type=StringType)
model_state_Transition.attributes={model_state_Transition_condition}

# state_StateNode class attributes and methods

# model_state_StateNode class attributes and methods

# state_Transition class attributes and methods

# model_state_State class attributes and methods
model_state_State_exitConditions: Property = Property(name="exitConditions", type=StringType)
model_state_State_activities: Property = Property(name="activities", type=StringType)
model_state_State_entryConditions: Property = Property(name="entryConditions", type=StringType)
model_state_State.attributes={model_state_State_exitConditions, model_state_State_entryConditions, model_state_State_activities}

# StateNode class attributes and methods

# model_state_StateInitial class attributes and methods

# model_state_StateEnd class attributes and methods

# model_attachment_UrlAttachment class attributes and methods
model_attachment_UrlAttachment_url: Property = Property(name="url", type=StringType)
model_attachment_UrlAttachment.attributes={model_attachment_UrlAttachment_url}

# profile_StereotypeAttribute class attributes and methods

# model_profile_StereotypeInstance class attributes and methods

# model_profile_Profile class attributes and methods

# profile_Stereotype class attributes and methods

# model_profile_Stereotype class attributes and methods
model_profile_Stereotype_required: Property = Property(name="required", type=BooleanType)
model_profile_Stereotype.attributes={model_profile_Stereotype_required}

# profile_Profile class attributes and methods

# profile_StereotypeAttributeInstance class attributes and methods

# model_profile_StereotypeAttribute class attributes and methods

# model_profile_StereotypeAttributeSimple class attributes and methods
model_profile_StereotypeAttributeSimple_type: Property = Property(name="type", type=StringType)
model_profile_StereotypeAttributeSimple.attributes={model_profile_StereotypeAttributeSimple_type}

# StereotypeAttribute class attributes and methods

# model_profile_StereotypeAttributeInstance class attributes and methods

# model_profile_StereotypeAttributeInstanceString class attributes and methods
model_profile_StereotypeAttributeInstanceString_value: Property = Property(name="value", type=StringType)
model_profile_StereotypeAttributeInstanceString.attributes={model_profile_StereotypeAttributeInstanceString_value}

# StereotypeAttributeInstance class attributes and methods

# model_util_ModelElementPath class attributes and methods

# ModelElementId class attributes and methods

# model_activity_ActivityObject class attributes and methods

# activity_Transition class attributes and methods

# model_activity_Transition class attributes and methods
model_activity_Transition_condition: Property = Property(name="condition", type=StringType)
model_activity_Transition.attributes={model_activity_Transition_condition}

# activity_ActivityObject class attributes and methods

# esmodel_ProjectId class attributes and methods

# esmodel_VersionInfo class attributes and methods
esmodel_VersionInfo_emfStoreVersionString: Property = Property(name="emfStoreVersionString", type=StringType)
esmodel_VersionInfo.attributes={esmodel_VersionInfo_emfStoreVersionString}

# esmodel_ClientVersionInfo class attributes and methods
esmodel_ClientVersionInfo_version: Property = Property(name="version", type=StringType)
esmodel_ClientVersionInfo_name: Property = Property(name="name", type=StringType)
esmodel_ClientVersionInfo.attributes={esmodel_ClientVersionInfo_name, esmodel_ClientVersionInfo_version}

# model_activity_Activity class attributes and methods

# ActivityObject class attributes and methods

# model_activity_Fork class attributes and methods

# model_activity_Branch class attributes and methods

# model_activity_ActivityInitial class attributes and methods

# model_activity_ActivityEnd class attributes and methods

# esmodel_ProjectHistory class attributes and methods
esmodel_ProjectHistory_projectName: Property = Property(name="projectName", type=StringType)
esmodel_ProjectHistory_projectDescription: Property = Property(name="projectDescription", type=StringType)
esmodel_ProjectHistory.attributes={esmodel_ProjectHistory_projectName, esmodel_ProjectHistory_projectDescription}

# ProjectId class attributes and methods

# versioning_Version class attributes and methods

# esmodel_ProjectInfo class attributes and methods
esmodel_ProjectInfo_name: Property = Property(name="name", type=StringType)
esmodel_ProjectInfo_description: Property = Property(name="description", type=StringType)
esmodel_ProjectInfo.attributes={esmodel_ProjectInfo_description, esmodel_ProjectInfo_name}

# versioning_PrimaryVersionSpec class attributes and methods

# esmodel_SessionId class attributes and methods

# esmodel_ServerSpace class attributes and methods

# accesscontrol_ACGroup class attributes and methods

# ProjectHistory class attributes and methods

# SessionId class attributes and methods

# accesscontrol_ACUser class attributes and methods

# versioning_ChangePackage class attributes and methods

# esmodel_versioning_HistoryQuery class attributes and methods
esmodel_versioning_HistoryQuery_includeChangePackage: Property = Property(name="includeChangePackage", type=BooleanType)
esmodel_versioning_HistoryQuery.attributes={esmodel_versioning_HistoryQuery_includeChangePackage}

# esmodel_FileIdentifier class attributes and methods

# esmodel_versioning_TagVersionSpec class attributes and methods
esmodel_versioning_TagVersionSpec_name: Property = Property(name="name", type=StringType)
esmodel_versioning_TagVersionSpec.attributes={esmodel_versioning_TagVersionSpec_name}

# VersionSpec class attributes and methods

# esmodel_versioning_DateVersionSpec class attributes and methods
esmodel_versioning_DateVersionSpec_date: Property = Property(name="date", type=DateType)
esmodel_versioning_DateVersionSpec.attributes={esmodel_versioning_DateVersionSpec_date}

# esmodel_versioning_PrimaryVersionSpec class attributes and methods
esmodel_versioning_PrimaryVersionSpec_identifier: Property = Property(name="identifier", type=IntegerType)
esmodel_versioning_PrimaryVersionSpec.attributes={esmodel_versioning_PrimaryVersionSpec_identifier}

# esmodel_versioning_VersionSpec class attributes and methods

# esmodel_versioning_LogMessage class attributes and methods
esmodel_versioning_LogMessage_author: Property = Property(name="author", type=StringType)
esmodel_versioning_LogMessage_message: Property = Property(name="message", type=StringType)
esmodel_versioning_LogMessage_date: Property = Property(name="date", type=DateType)
esmodel_versioning_LogMessage_clientDate: Property = Property(name="clientDate", type=DateType)
esmodel_versioning_LogMessage.attributes={esmodel_versioning_LogMessage_clientDate, esmodel_versioning_LogMessage_date, esmodel_versioning_LogMessage_message, esmodel_versioning_LogMessage_author}

# esmodel_versioning_ChangePackage class attributes and methods

# operations_AbstractOperation class attributes and methods

# events_Event class attributes and methods

# versioning_LogMessage class attributes and methods

# notification_ESNotification class attributes and methods

# versioning_VersionProperty class attributes and methods

# esmodel_versioning_HistoryInfo class attributes and methods

# versioning_TagVersionSpec class attributes and methods

# esmodel_operations_FeatureOperation class attributes and methods
esmodel_operations_FeatureOperation_featureName: Property = Property(name="featureName", type=StringType)
esmodel_operations_FeatureOperation.attributes={esmodel_operations_FeatureOperation_featureName}

# esmodel_versioning_Version class attributes and methods

# esmodel_versioning_HeadVersionSpec class attributes and methods

# esmodel_versioning_VersionProperty class attributes and methods
esmodel_versioning_VersionProperty_name: Property = Property(name="name", type=StringType)
esmodel_versioning_VersionProperty_value: Property = Property(name="value", type=StringType)
esmodel_versioning_VersionProperty.attributes={esmodel_versioning_VersionProperty_value, esmodel_versioning_VersionProperty_name}

# esmodel_operations_AbstractOperation class attributes and methods
esmodel_operations_AbstractOperation_name: Property = Property(name="name", type=StringType)
esmodel_operations_AbstractOperation_description: Property = Property(name="description", type=StringType)
esmodel_operations_AbstractOperation_accepted: Property = Property(name="accepted", type=BooleanType)
esmodel_operations_AbstractOperation_clientDate: Property = Property(name="clientDate", type=DateType)
esmodel_operations_AbstractOperation.attributes={esmodel_operations_AbstractOperation_clientDate, esmodel_operations_AbstractOperation_description, esmodel_operations_AbstractOperation_name, esmodel_operations_AbstractOperation_accepted}

# esmodel_operations_CompositeOperation class attributes and methods
esmodel_operations_CompositeOperation_compositeName: Property = Property(name="compositeName", type=StringType)
esmodel_operations_CompositeOperation_compositeDescription: Property = Property(name="compositeDescription", type=StringType)
esmodel_operations_CompositeOperation_reversed: Property = Property(name="reversed", type=BooleanType)
esmodel_operations_CompositeOperation.attributes={esmodel_operations_CompositeOperation_compositeDescription, esmodel_operations_CompositeOperation_compositeName, esmodel_operations_CompositeOperation_reversed}

# AbstractOperation class attributes and methods

# esmodel_operations_MultiAttributeSetOperation class attributes and methods
esmodel_operations_MultiAttributeSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiAttributeSetOperation_oldValue: Property = Property(name="oldValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation_newValue: Property = Property(name="newValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation.attributes={esmodel_operations_MultiAttributeSetOperation_oldValue, esmodel_operations_MultiAttributeSetOperation_index, esmodel_operations_MultiAttributeSetOperation_newValue}

# esmodel_operations_MultiAttributeMoveOperation class attributes and methods
esmodel_operations_MultiAttributeMoveOperation_oldIndex: Property = Property(name="oldIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_newIndex: Property = Property(name="newIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_referencedValue: Property = Property(name="referencedValue", type=StringType)
esmodel_operations_MultiAttributeMoveOperation.attributes={esmodel_operations_MultiAttributeMoveOperation_newIndex, esmodel_operations_MultiAttributeMoveOperation_referencedValue, esmodel_operations_MultiAttributeMoveOperation_oldIndex}

# esmodel_operations_SingleReferenceOperation class attributes and methods

# ReferenceOperation class attributes and methods

# esmodel_operations_MultiReferenceSetOperation class attributes and methods
esmodel_operations_MultiReferenceSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiReferenceSetOperation.attributes={esmodel_operations_MultiReferenceSetOperation_index}

# esmodel_operations_CreateDeleteOperation class attributes and methods
esmodel_operations_CreateDeleteOperation_delete: Property = Property(name="delete", type=BooleanType)
esmodel_operations_CreateDeleteOperation.attributes={esmodel_operations_CreateDeleteOperation_delete}

# operations_esmodel_EObject class attributes and methods

# operations_ReferenceOperation class attributes and methods

# operations_EObjectToModelElementIdMap class attributes and methods

# esmodel_operations_AttributeOperation class attributes and methods
esmodel_operations_AttributeOperation_oldValue: Property = Property(name="oldValue", type=StringType)
esmodel_operations_AttributeOperation_newValue: Property = Property(name="newValue", type=StringType)
esmodel_operations_AttributeOperation.attributes={esmodel_operations_AttributeOperation_newValue, esmodel_operations_AttributeOperation_oldValue}

# FeatureOperation class attributes and methods

# esmodel_operations_MultiAttributeOperation class attributes and methods
esmodel_operations_MultiAttributeOperation_add: Property = Property(name="add", type=BooleanType)
esmodel_operations_MultiAttributeOperation_indexes: Property = Property(name="indexes", type=IntegerType)
esmodel_operations_MultiAttributeOperation_referencedValues: Property = Property(name="referencedValues", type=StringType)
esmodel_operations_MultiAttributeOperation.attributes={esmodel_operations_MultiAttributeOperation_add, esmodel_operations_MultiAttributeOperation_referencedValues, esmodel_operations_MultiAttributeOperation_indexes}

# esmodel_operations_ModelElementGroup class attributes and methods
esmodel_operations_ModelElementGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_ModelElementGroup.attributes={esmodel_operations_ModelElementGroup_name}

# esmodel_operations_EObjectToModelElementIdMap class attributes and methods

# esmodel_semantic_SemanticCompositeOperation class attributes and methods

# esmodel_operations_MultiReferenceOperation class attributes and methods
esmodel_operations_MultiReferenceOperation_add: Property = Property(name="add", type=BooleanType)
esmodel_operations_MultiReferenceOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiReferenceOperation.attributes={esmodel_operations_MultiReferenceOperation_add, esmodel_operations_MultiReferenceOperation_index}

# esmodel_operations_MultiReferenceMoveOperation class attributes and methods
esmodel_operations_MultiReferenceMoveOperation_oldIndex: Property = Property(name="oldIndex", type=IntegerType)
esmodel_operations_MultiReferenceMoveOperation_newIndex: Property = Property(name="newIndex", type=IntegerType)
esmodel_operations_MultiReferenceMoveOperation.attributes={esmodel_operations_MultiReferenceMoveOperation_oldIndex, esmodel_operations_MultiReferenceMoveOperation_newIndex}

# esmodel_operations_ReferenceOperation class attributes and methods
esmodel_operations_ReferenceOperation_bidirectional: Property = Property(name="bidirectional", type=BooleanType)
esmodel_operations_ReferenceOperation_oppositeFeatureName: Property = Property(name="oppositeFeatureName", type=StringType)
esmodel_operations_ReferenceOperation_containmentType: Property = Property(name="containmentType", type=StringType)
esmodel_operations_ReferenceOperation.attributes={esmodel_operations_ReferenceOperation_bidirectional, esmodel_operations_ReferenceOperation_oppositeFeatureName, esmodel_operations_ReferenceOperation_containmentType}

# esmodel_operations_DiagramLayoutOperation class attributes and methods

# AttributeOperation class attributes and methods

# esmodel_operations_OperationId class attributes and methods

# esmodel_operations_OperationGroup class attributes and methods
esmodel_operations_OperationGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_OperationGroup.attributes={esmodel_operations_OperationGroup_name}

# esmodel_events_PluginStartEvent class attributes and methods
esmodel_events_PluginStartEvent_pluginId: Property = Property(name="pluginId", type=StringType)
esmodel_events_PluginStartEvent.attributes={esmodel_events_PluginStartEvent_pluginId}

# esmodel_events_UpdateEvent class attributes and methods

# esmodel_events_AnnotationEvent class attributes and methods

# esmodel_events_RevertEvent class attributes and methods
esmodel_events_RevertEvent_revertedChangesCount: Property = Property(name="revertedChangesCount", type=IntegerType)
esmodel_events_RevertEvent.attributes={esmodel_events_RevertEvent_revertedChangesCount}

# CompositeOperation class attributes and methods

# esmodel_events_ShowHistoryEvent class attributes and methods

# esmodel_events_Event class attributes and methods
esmodel_events_Event_timestamp: Property = Property(name="timestamp", type=DateType)
esmodel_events_Event.attributes={esmodel_events_Event_timestamp}

# esmodel_events_ReadEvent class attributes and methods
esmodel_events_ReadEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_ReadEvent_readView: Property = Property(name="readView", type=StringType)
esmodel_events_ReadEvent.attributes={esmodel_events_ReadEvent_readView, esmodel_events_ReadEvent_sourceView}

# Event class attributes and methods

# esmodel_events_MergeEvent class attributes and methods
esmodel_events_MergeEvent_numberOfConflicts: Property = Property(name="numberOfConflicts", type=IntegerType)
esmodel_events_MergeEvent_totalTime: Property = Property(name="totalTime", type=IntegerType)
esmodel_events_MergeEvent.attributes={esmodel_events_MergeEvent_totalTime, esmodel_events_MergeEvent_numberOfConflicts}

# esmodel_events_CheckoutEvent class attributes and methods

# esmodel_events_ExceptionEvent class attributes and methods
esmodel_events_ExceptionEvent_ExceptionCauseStackTrace: Property = Property(name="ExceptionCauseStackTrace", type=StringType)
esmodel_events_ExceptionEvent_ExceptionTitle: Property = Property(name="ExceptionTitle", type=StringType)
esmodel_events_ExceptionEvent_ExceptionStackTrace: Property = Property(name="ExceptionStackTrace", type=StringType)
esmodel_events_ExceptionEvent_ExceptionCauseTitle: Property = Property(name="ExceptionCauseTitle", type=StringType)
esmodel_events_ExceptionEvent.attributes={esmodel_events_ExceptionEvent_ExceptionCauseStackTrace, esmodel_events_ExceptionEvent_ExceptionStackTrace, esmodel_events_ExceptionEvent_ExceptionTitle, esmodel_events_ExceptionEvent_ExceptionCauseTitle}

# esmodel_events_NavigatorCreateEvent class attributes and methods
esmodel_events_NavigatorCreateEvent_dynamic: Property = Property(name="dynamic", type=BooleanType)
esmodel_events_NavigatorCreateEvent.attributes={esmodel_events_NavigatorCreateEvent_dynamic}

# esmodel_events_PluginFocusEvent class attributes and methods
esmodel_events_PluginFocusEvent_pluginId: Property = Property(name="pluginId", type=StringType)
esmodel_events_PluginFocusEvent_startDate: Property = Property(name="startDate", type=DateType)
esmodel_events_PluginFocusEvent.attributes={esmodel_events_PluginFocusEvent_startDate, esmodel_events_PluginFocusEvent_pluginId}

# esmodel_events_PresentationSwitchEvent class attributes and methods
esmodel_events_PresentationSwitchEvent_readView: Property = Property(name="readView", type=StringType)
esmodel_events_PresentationSwitchEvent_newPresentation: Property = Property(name="newPresentation", type=StringType)
esmodel_events_PresentationSwitchEvent.attributes={esmodel_events_PresentationSwitchEvent_newPresentation, esmodel_events_PresentationSwitchEvent_readView}

# esmodel_events_PerspectiveEvent class attributes and methods

# esmodel_events_DNDEvent class attributes and methods
esmodel_events_DNDEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_DNDEvent_targetView: Property = Property(name="targetView", type=StringType)
esmodel_events_DNDEvent.attributes={esmodel_events_DNDEvent_sourceView, esmodel_events_DNDEvent_targetView}

# esmodel_events_LinkEvent class attributes and methods
esmodel_events_LinkEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_LinkEvent_createdNew: Property = Property(name="createdNew", type=BooleanType)
esmodel_events_LinkEvent.attributes={esmodel_events_LinkEvent_sourceView, esmodel_events_LinkEvent_createdNew}

# esmodel_events_TraceEvent class attributes and methods
esmodel_events_TraceEvent_featureName: Property = Property(name="featureName", type=StringType)
esmodel_events_TraceEvent.attributes={esmodel_events_TraceEvent_featureName}

# esmodel_events_MergeChoiceEvent class attributes and methods
esmodel_events_MergeChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeChoiceEvent_contextFeature: Property = Property(name="contextFeature", type=StringType)
esmodel_events_MergeChoiceEvent_createdIssueName: Property = Property(name="createdIssueName", type=StringType)
esmodel_events_MergeChoiceEvent.attributes={esmodel_events_MergeChoiceEvent_createdIssueName, esmodel_events_MergeChoiceEvent_selection, esmodel_events_MergeChoiceEvent_contextFeature}

# operations_OperationId class attributes and methods

# esmodel_events_UndoEvent class attributes and methods

# esmodel_events_Validate class attributes and methods

# esmodel_events_ShowChangesEvent class attributes and methods

# esmodel_events_NotificationReadEvent class attributes and methods
esmodel_events_NotificationReadEvent_notificationId: Property = Property(name="notificationId", type=StringType)
esmodel_events_NotificationReadEvent.attributes={esmodel_events_NotificationReadEvent_notificationId}

# ReadEvent class attributes and methods

# esmodel_events_NotificationGenerationEvent class attributes and methods

# esmodel_events_NotificationIgnoreEvent class attributes and methods
esmodel_events_NotificationIgnoreEvent_notificationId: Property = Property(name="notificationId", type=StringType)
esmodel_events_NotificationIgnoreEvent.attributes={esmodel_events_NotificationIgnoreEvent_notificationId}

# esmodel_events_URLEvent class attributes and methods
esmodel_events_URLEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_URLEvent.attributes={esmodel_events_URLEvent_sourceView}

# accesscontrol_OrgUnitProperty class attributes and methods

# esmodel_accesscontrol_ACGroup class attributes and methods

# accesscontrol_ACOrgUnit class attributes and methods

# esmodel_accesscontrol_ACOrgUnitId class attributes and methods

# esmodel_accesscontrol_OrgUnitProperty class attributes and methods
esmodel_accesscontrol_OrgUnitProperty_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_OrgUnitProperty_value: Property = Property(name="value", type=StringType)
esmodel_accesscontrol_OrgUnitProperty.attributes={esmodel_accesscontrol_OrgUnitProperty_name, esmodel_accesscontrol_OrgUnitProperty_value}

# esmodel_roles_Role class attributes and methods
esmodel_roles_Role_m_canAdministrate: Method = Method(name="canAdministrate", parameters={Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canCreate: Method = Method(name="canCreate", parameters={Parameter(name='esmodel_modelElement', type=StringType), Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canDelete: Method = Method(name="canDelete", parameters={Parameter(name='esmodel_projectId', type=StringType), Parameter(name='esmodel_modelElement', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canModify: Method = Method(name="canModify", parameters={Parameter(name='esmodel_projectId', type=StringType), Parameter(name='esmodel_modelElement', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canRead: Method = Method(name="canRead", parameters={Parameter(name='esmodel_modelElement', type=StringType), Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role.methods={esmodel_roles_Role_m_canDelete, esmodel_roles_Role_m_canCreate, esmodel_roles_Role_m_canAdministrate, esmodel_roles_Role_m_canRead, esmodel_roles_Role_m_canModify}

# esmodel_events_MergeGlobalChoiceEvent class attributes and methods
esmodel_events_MergeGlobalChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeGlobalChoiceEvent.attributes={esmodel_events_MergeGlobalChoiceEvent_selection}

# esmodel_server_ServerEvent class attributes and methods

# esmodel_server_ServerProjectEvent class attributes and methods

# ServerEvent class attributes and methods

# esmodel_server_ProjectUpdatedEvent class attributes and methods

# ServerProjectEvent class attributes and methods

# esmodel_accesscontrol_ACUser class attributes and methods
esmodel_accesscontrol_ACUser_firstName: Property = Property(name="firstName", type=StringType)
esmodel_accesscontrol_ACUser_lastName: Property = Property(name="lastName", type=StringType)
esmodel_accesscontrol_ACUser.attributes={esmodel_accesscontrol_ACUser_lastName, esmodel_accesscontrol_ACUser_firstName}

# ACOrgUnit class attributes and methods

# esmodel_accesscontrol_ACOrgUnit class attributes and methods
esmodel_accesscontrol_ACOrgUnit_description: Property = Property(name="description", type=StringType)
esmodel_accesscontrol_ACOrgUnit_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_ACOrgUnit_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
esmodel_accesscontrol_ACOrgUnit.attributes={esmodel_accesscontrol_ACOrgUnit_description, esmodel_accesscontrol_ACOrgUnit_name}
esmodel_accesscontrol_ACOrgUnit.methods={esmodel_accesscontrol_ACOrgUnit_m_getId}

# roles_Role class attributes and methods

# esmodel_url_ServerUrl class attributes and methods
esmodel_url_ServerUrl_hostName: Property = Property(name="hostName", type=StringType)
esmodel_url_ServerUrl_port: Property = Property(name="port", type=IntegerType)
esmodel_url_ServerUrl.attributes={esmodel_url_ServerUrl_hostName, esmodel_url_ServerUrl_port}

# esmodel_url_ProjectUrlFragment class attributes and methods
esmodel_url_ProjectUrlFragment_name: Property = Property(name="name", type=StringType)
esmodel_url_ProjectUrlFragment.attributes={esmodel_url_ProjectUrlFragment_name}

# esmodel_url_ModelElementUrlFragment class attributes and methods
esmodel_url_ModelElementUrlFragment_name: Property = Property(name="name", type=StringType)
esmodel_url_ModelElementUrlFragment.attributes={esmodel_url_ModelElementUrlFragment_name}

# esmodel_roles_ReaderRole class attributes and methods

# Role class attributes and methods

# esmodel_roles_WriterRole class attributes and methods

# esmodel_roles_ProjectAdminRole class attributes and methods

# esmodel_roles_ServerAdmin class attributes and methods

# esmodel_notification_ESNotification class attributes and methods
esmodel_notification_ESNotification_name: Property = Property(name="name", type=StringType)
esmodel_notification_ESNotification_message: Property = Property(name="message", type=StringType)
esmodel_notification_ESNotification_details: Property = Property(name="details", type=StringType)
esmodel_notification_ESNotification_seen: Property = Property(name="seen", type=BooleanType)
esmodel_notification_ESNotification_creationDate: Property = Property(name="creationDate", type=DateType)
esmodel_notification_ESNotification_provider: Property = Property(name="provider", type=StringType)
esmodel_notification_ESNotification_sender: Property = Property(name="sender", type=StringType)
esmodel_notification_ESNotification_recipient: Property = Property(name="recipient", type=StringType)
esmodel_notification_ESNotification.attributes={esmodel_notification_ESNotification_seen, esmodel_notification_ESNotification_message, esmodel_notification_ESNotification_provider, esmodel_notification_ESNotification_name, esmodel_notification_ESNotification_recipient, esmodel_notification_ESNotification_creationDate, esmodel_notification_ESNotification_sender, esmodel_notification_ESNotification_details}

# esmodel_url_ModelElementUrl class attributes and methods

# url_ServerUrl class attributes and methods

# url_ProjectUrlFragment class attributes and methods

# url_ModelElementUrlFragment class attributes and methods

# Relationships
annotations4: BinaryAssociation = BinaryAssociation(
    name="annotations4",
    ends={
        Property(name="Annotation", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedModelElements", type=Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
modelElements0: BinaryAssociation = BinaryAssociation(
    name="modelElements0",
    ends={
        Property(name="ModelElement", type=metamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Project", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cutElements1: BinaryAssociation = BinaryAssociation(
    name="cutElements1",
    ends={
        Property(name="ModelElement3", type=metamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Project2", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participations15: BinaryAssociation = BinaryAssociation(
    name="participations15",
    ends={
        Property(name="WorkItem", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
assignments16: BinaryAssociation = BinaryAssociation(
    name="assignments16",
    ends={
        Property(name="WorkItem17", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="assignee", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
attachments5: BinaryAssociation = BinaryAssociation(
    name="attachments5",
    ends={
        Property(name="Attachment", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referringModelElements", type=Attachment, multiplicity=Multiplicity(0, 9999))
    }
)
leafSection6: BinaryAssociation = BinaryAssociation(
    name="leafSection6",
    ends={
        Property(name="LeafSection", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElements", type=document_LeafSection, multiplicity=Multiplicity(0, 1))
    }
)
incomingDocumentReferences7: BinaryAssociation = BinaryAssociation(
    name="incomingDocumentReferences7",
    ends={
        Property(name="LeafSection8", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedModelElements", type=document_LeafSection, multiplicity=Multiplicity(0, 9999))
    }
)
comments9: BinaryAssociation = BinaryAssociation(
    name="comments9",
    ends={
        Property(name="Comment", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="commentedElement", type=rationale_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appliedStereotypeInstances10: BinaryAssociation = BinaryAssociation(
    name="appliedStereotypeInstances10",
    ends={
        Property(name="StereotypeInstance", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElement", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedModelElements11: BinaryAssociation = BinaryAssociation(
    name="annotatedModelElements11",
    ends={
        Property(name="UnicaseModelElement", type=model_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
referringModelElements12: BinaryAssociation = BinaryAssociation(
    name="referringModelElements12",
    ends={
        Property(name="UnicaseModelElement13", type=model_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="attachments", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
groupMemberships14: BinaryAssociation = BinaryAssociation(
    name="groupMemberships14",
    ends={
        Property(name="Group", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="orgUnits", type=organization_Group, multiplicity=Multiplicity(0, 9999))
    }
)
reviewer28: BinaryAssociation = BinaryAssociation(
    name="reviewer28",
    ends={
        Property(name="User", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="workItemsToReview", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
participants29: BinaryAssociation = BinaryAssociation(
    name="participants29",
    ends={
        Property(name="OrgUnit30", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="participations", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
workItemsToReview18: BinaryAssociation = BinaryAssociation(
    name="workItemsToReview18",
    ends={
        Property(name="WorkItem19", type=model_organization_User, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewer", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
orgUnits20: BinaryAssociation = BinaryAssociation(
    name="orgUnits20",
    ends={
        Property(name="OrgUnit", type=model_organization_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groupMemberships", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containingWorkpackage21: BinaryAssociation = BinaryAssociation(
    name="containingWorkpackage21",
    ends={
        Property(name="WorkPackage", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="containedWorkItems", type=task_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
successors22: BinaryAssociation = BinaryAssociation(
    name="successors22",
    ends={
        Property(name="WorkItem23", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessors", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
predecessors24: BinaryAssociation = BinaryAssociation(
    name="predecessors24",
    ends={
        Property(name="WorkItem25", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="successors", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
assignee26: BinaryAssociation = BinaryAssociation(
    name="assignee26",
    ends={
        Property(name="OrgUnit27", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="assignments", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
associatedChangePackages31: BinaryAssociation = BinaryAssociation(
    name="associatedChangePackages31",
    ends={
        Property(name="change_ModelChangePackage", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_task_WorkItem", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
    }
)
containedWorkItems32: BinaryAssociation = BinaryAssociation(
    name="containedWorkItems32",
    ends={
        Property(name="WorkItem33", type=model_task_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="containingWorkpackage", type=task_WorkItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedModelElements34: BinaryAssociation = BinaryAssociation(
    name="containedModelElements34",
    ends={
        Property(name="UnicaseModelElement35", type=model_task_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="model_task_Milestone", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
elements36: BinaryAssociation = BinaryAssociation(
    name="elements36",
    ends={
        Property(name="UnicaseModelElement37", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
gmfdiagram38: BinaryAssociation = BinaryAssociation(
    name="gmfdiagram38",
    ends={
        Property(name="diagram_model_Diagram", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram39", type=diagram_model_Diagram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newElements40: BinaryAssociation = BinaryAssociation(
    name="newElements40",
    ends={
        Property(name="UnicaseModelElement42", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram41", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes55: BinaryAssociation = BinaryAssociation(
    name="attributes55",
    ends={
        Property(name="Attribute", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="definingClass", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPackage43: BinaryAssociation = BinaryAssociation(
    name="parentPackage43",
    ends={
        Property(name="Package", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="containedPackageElements", type=classes_Package, multiplicity=Multiplicity(0, 1))
    }
)
outgoingDependencies44: BinaryAssociation = BinaryAssociation(
    name="outgoingDependencies44",
    ends={
        Property(name="Dependency", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=classes_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
incomingDependencies45: BinaryAssociation = BinaryAssociation(
    name="incomingDependencies45",
    ends={
        Property(name="Dependency46", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=classes_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
subClasses47: BinaryAssociation = BinaryAssociation(
    name="subClasses47",
    ends={
        Property(name="Class", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="superClasses", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
superClasses48: BinaryAssociation = BinaryAssociation(
    name="superClasses48",
    ends={
        Property(name="Class49", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="subClasses", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingAssociations50: BinaryAssociation = BinaryAssociation(
    name="outgoingAssociations50",
    ends={
        Property(name="Association", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="source51", type=classes_Association, multiplicity=Multiplicity(0, 9999))
    }
)
incomingAssociations52: BinaryAssociation = BinaryAssociation(
    name="incomingAssociations52",
    ends={
        Property(name="Association54", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="target53", type=classes_Association, multiplicity=Multiplicity(0, 9999))
    }
)
methods56: BinaryAssociation = BinaryAssociation(
    name="methods56",
    ends={
        Property(name="Method", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="definingClass57", type=classes_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participatedUseCases58: BinaryAssociation = BinaryAssociation(
    name="participatedUseCases58",
    ends={
        Property(name="UseCase", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="identifiedClasses", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
demoParticipations59: BinaryAssociation = BinaryAssociation(
    name="demoParticipations59",
    ends={
        Property(name="Scenario", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingClasses", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
facadeClass60: BinaryAssociation = BinaryAssociation(
    name="facadeClass60",
    ends={
        Property(name="classes_Class", type=model_classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="model_classes_Package", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
containedPackageElements61: BinaryAssociation = BinaryAssociation(
    name="containedPackageElements61",
    ends={
        Property(name="PackageElement", type=model_classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPackage", type=classes_PackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source62: BinaryAssociation = BinaryAssociation(
    name="source62",
    ends={
        Property(name="Class63", type=model_classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingAssociations", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
target64: BinaryAssociation = BinaryAssociation(
    name="target64",
    ends={
        Property(name="Class65", type=model_classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingAssociations", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
definingClass66: BinaryAssociation = BinaryAssociation(
    name="definingClass66",
    ends={
        Property(name="Class67", type=model_classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
definingClass68: BinaryAssociation = BinaryAssociation(
    name="definingClass68",
    ends={
        Property(name="Class69", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
calledMethods70: BinaryAssociation = BinaryAssociation(
    name="calledMethods70",
    ends={
        Property(name="Method71", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="callingMethods", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
callingMethods72: BinaryAssociation = BinaryAssociation(
    name="callingMethods72",
    ends={
        Property(name="Method73", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="calledMethods", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
arguments74: BinaryAssociation = BinaryAssociation(
    name="arguments74",
    ends={
        Property(name="classes_MethodArgument", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="model_classes_Method", type=classes_MethodArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
demoParticipations75: BinaryAssociation = BinaryAssociation(
    name="demoParticipations75",
    ends={
        Property(name="Scenario76", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingMethods", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
source77: BinaryAssociation = BinaryAssociation(
    name="source77",
    ends={
        Property(name="PackageElement78", type=model_classes_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingDependencies", type=classes_PackageElement, multiplicity=Multiplicity(0, 1))
    }
)
target79: BinaryAssociation = BinaryAssociation(
    name="target79",
    ends={
        Property(name="PackageElement80", type=model_classes_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingDependencies", type=classes_PackageElement, multiplicity=Multiplicity(0, 1))
    }
)
parent81: BinaryAssociation = BinaryAssociation(
    name="parent81",
    ends={
        Property(name="CompositeSection", type=model_document_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="subsections", type=document_CompositeSection, multiplicity=Multiplicity(0, 1))
    }
)
modelElements82: BinaryAssociation = BinaryAssociation(
    name="modelElements82",
    ends={
        Property(name="UnicaseModelElement83", type=model_document_LeafSection, multiplicity=Multiplicity(1, 1)),
        Property(name="leafSection", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModelElements84: BinaryAssociation = BinaryAssociation(
    name="referencedModelElements84",
    ends={
        Property(name="UnicaseModelElement85", type=model_document_LeafSection, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingDocumentReferences", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
subsections86: BinaryAssociation = BinaryAssociation(
    name="subsections86",
    ends={
        Property(name="Section", type=model_document_CompositeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=document_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedUseCases100: BinaryAssociation = BinaryAssociation(
    name="includedUseCases100",
    ends={
        Property(name="requirement_UseCase", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_UseCase", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
refiningRequirements87: BinaryAssociation = BinaryAssociation(
    name="refiningRequirements87",
    ends={
        Property(name="FunctionalRequirement", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="refinedRequirement", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinedRequirement88: BinaryAssociation = BinaryAssociation(
    name="refinedRequirement88",
    ends={
        Property(name="FunctionalRequirement89", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="refiningRequirements", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
stakeholder90: BinaryAssociation = BinaryAssociation(
    name="stakeholder90",
    ends={
        Property(name="organization_OrgUnit", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_FunctionalRequirement", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
useCases91: BinaryAssociation = BinaryAssociation(
    name="useCases91",
    ends={
        Property(name="UseCase92", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="functionalRequirements", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
scenarios93: BinaryAssociation = BinaryAssociation(
    name="scenarios93",
    ends={
        Property(name="Scenario95", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="functionalRequirements94", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
functionalRequirements96: BinaryAssociation = BinaryAssociation(
    name="functionalRequirements96",
    ends={
        Property(name="FunctionalRequirement97", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCases", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
identifiedClasses98: BinaryAssociation = BinaryAssociation(
    name="identifiedClasses98",
    ends={
        Property(name="Class99", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedUseCases", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
instantiatedUseCases114: BinaryAssociation = BinaryAssociation(
    name="instantiatedUseCases114",
    ends={
        Property(name="UseCase115", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarios", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
extendedUseCases101: BinaryAssociation = BinaryAssociation(
    name="extendedUseCases101",
    ends={
        Property(name="requirement_UseCase103", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_UseCase102", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
scenarios104: BinaryAssociation = BinaryAssociation(
    name="scenarios104",
    ends={
        Property(name="Scenario105", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiatedUseCases", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActor106: BinaryAssociation = BinaryAssociation(
    name="initiatingActor106",
    ends={
        Property(name="Actor", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedUseCases", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
participatingActors107: BinaryAssociation = BinaryAssociation(
    name="participatingActors107",
    ends={
        Property(name="Actor109", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedUseCases108", type=requirement_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
useCaseSteps110: BinaryAssociation = BinaryAssociation(
    name="useCaseSteps110",
    ends={
        Property(name="Step", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedUserTask111: BinaryAssociation = BinaryAssociation(
    name="realizedUserTask111",
    ends={
        Property(name="UserTask", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="realizingUseCases", type=requirement_UserTask, multiplicity=Multiplicity(0, 1))
    }
)
nonFunctionalRequirements112: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements112",
    ends={
        Property(name="NonFunctionalRequirement", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictedUseCases", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
systemFunctions113: BinaryAssociation = BinaryAssociation(
    name="systemFunctions113",
    ends={
        Property(name="SystemFunction", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="usecases", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 9999))
    }
)
instances134: BinaryAssociation = BinaryAssociation(
    name="instances134",
    ends={
        Property(name="instantiatedActor", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999)),
        Property(name="ActorInstance135", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1))
    }
)
participatedUserTasks136: BinaryAssociation = BinaryAssociation(
    name="participatedUserTasks136",
    ends={
        Property(name="UserTask138", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActors137", type=requirement_UserTask, multiplicity=Multiplicity(0, 9999))
    }
)
functionalRequirements116: BinaryAssociation = BinaryAssociation(
    name="functionalRequirements116",
    ends={
        Property(name="FunctionalRequirement118", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarios117", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
participatingMethods119: BinaryAssociation = BinaryAssociation(
    name="participatingMethods119",
    ends={
        Property(name="Method120", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="demoParticipations", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
participatingClasses121: BinaryAssociation = BinaryAssociation(
    name="participatingClasses121",
    ends={
        Property(name="Class123", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="demoParticipations122", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActorInstance124: BinaryAssociation = BinaryAssociation(
    name="initiatingActorInstance124",
    ends={
        Property(name="ActorInstance", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedScenarios", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 1))
    }
)
participatingActorInstances125: BinaryAssociation = BinaryAssociation(
    name="participatingActorInstances125",
    ends={
        Property(name="ActorInstance126", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedScenarios", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
steps127: BinaryAssociation = BinaryAssociation(
    name="steps127",
    ends={
        Property(name="requirement_Step", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Scenario", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFunctionalRequirements128: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements128",
    ends={
        Property(name="NonFunctionalRequirement129", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictedScenarios", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedUseCases130: BinaryAssociation = BinaryAssociation(
    name="initiatedUseCases130",
    ends={
        Property(name="UseCase131", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActor", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
participatedUseCases132: BinaryAssociation = BinaryAssociation(
    name="participatedUseCases132",
    ends={
        Property(name="UseCase133", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActors", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
workspace159: BinaryAssociation = BinaryAssociation(
    name="workspace159",
    ends={
        Property(name="Workspace", type=model_requirement_SystemFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="systemFunctions160", type=requirement_Workspace, multiplicity=Multiplicity(0, 1))
    }
)
initiatedUserTask139: BinaryAssociation = BinaryAssociation(
    name="initiatedUserTask139",
    ends={
        Property(name="UserTask141", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActor140", type=requirement_UserTask, multiplicity=Multiplicity(0, 1))
    }
)
initiatedScenarios142: BinaryAssociation = BinaryAssociation(
    name="initiatedScenarios142",
    ends={
        Property(name="Scenario143", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActorInstance", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
participatedScenarios144: BinaryAssociation = BinaryAssociation(
    name="participatedScenarios144",
    ends={
        Property(name="Scenario145", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActorInstances", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
instantiatedActor146: BinaryAssociation = BinaryAssociation(
    name="instantiatedActor146",
    ends={
        Property(name="Actor147", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
includedUseCase148: BinaryAssociation = BinaryAssociation(
    name="includedUseCase148",
    ends={
        Property(name="requirement_UseCase149", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
useCase150: BinaryAssociation = BinaryAssociation(
    name="useCase150",
    ends={
        Property(name="UseCase151", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCaseSteps", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
includedSystemFunction152: BinaryAssociation = BinaryAssociation(
    name="includedSystemFunction152",
    ends={
        Property(name="requirement_SystemFunction", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step153", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 1))
    }
)
nonFunctionalRequirement154: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirement154",
    ends={
        Property(name="NonFunctionalRequirement155", type=model_requirement_SystemFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="systemFunctions", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
usecases156: BinaryAssociation = BinaryAssociation(
    name="usecases156",
    ends={
        Property(name="UseCase158", type=model_requirement_SystemFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="systemFunctions157", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
systemFunctions179: BinaryAssociation = BinaryAssociation(
    name="systemFunctions179",
    ends={
        Property(name="SystemFunction180", type=model_requirement_Workspace, multiplicity=Multiplicity(1, 1)),
        Property(name="workspace", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActor161: BinaryAssociation = BinaryAssociation(
    name="initiatingActor161",
    ends={
        Property(name="Actor162", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedUserTask", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
participatingActors163: BinaryAssociation = BinaryAssociation(
    name="participatingActors163",
    ends={
        Property(name="Actor164", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedUserTasks", type=requirement_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
realizingUseCases165: BinaryAssociation = BinaryAssociation(
    name="realizingUseCases165",
    ends={
        Property(name="UseCase166", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedUserTask", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
nonFunctionalRequirements167: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements167",
    ends={
        Property(name="NonFunctionalRequirement168", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="userTasks", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedUseCases169: BinaryAssociation = BinaryAssociation(
    name="restrictedUseCases169",
    ends={
        Property(name="UseCase170", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirements", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedScenarios171: BinaryAssociation = BinaryAssociation(
    name="restrictedScenarios171",
    ends={
        Property(name="Scenario173", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirements172", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
systemFunctions174: BinaryAssociation = BinaryAssociation(
    name="systemFunctions174",
    ends={
        Property(name="SystemFunction175", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirement", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 9999))
    }
)
userTasks176: BinaryAssociation = BinaryAssociation(
    name="userTasks176",
    ends={
        Property(name="UserTask178", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirements177", type=requirement_UserTask, multiplicity=Multiplicity(0, 9999))
    }
)
issue188: BinaryAssociation = BinaryAssociation(
    name="issue188",
    ends={
        Property(name="Issue189", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="solution", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
assessments190: BinaryAssociation = BinaryAssociation(
    name="assessments190",
    ends={
        Property(name="Assessment191", type=model_rationale_Criterion, multiplicity=Multiplicity(1, 1)),
        Property(name="criterion", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999))
    }
)
proposals181: BinaryAssociation = BinaryAssociation(
    name="proposals181",
    ends={
        Property(name="Proposal", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solution182: BinaryAssociation = BinaryAssociation(
    name="solution182",
    ends={
        Property(name="Solution", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue183", type=rationale_Solution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
criteria184: BinaryAssociation = BinaryAssociation(
    name="criteria184",
    ends={
        Property(name="rationale_Criterion", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Issue", type=rationale_Criterion, multiplicity=Multiplicity(0, 9999))
    }
)
issue185: BinaryAssociation = BinaryAssociation(
    name="issue185",
    ends={
        Property(name="Issue", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="proposals", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
assessments186: BinaryAssociation = BinaryAssociation(
    name="assessments186",
    ends={
        Property(name="Assessment", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="proposal", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
underlyingProposals187: BinaryAssociation = BinaryAssociation(
    name="underlyingProposals187",
    ends={
        Property(name="rationale_Proposal", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Solution", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999))
    }
)
appliedChanges208: BinaryAssociation = BinaryAssociation(
    name="appliedChanges208",
    ends={
        Property(name="change_ModelChangePackage209", type=model_change_MergingSolution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingSolution", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
    }
)
proposal192: BinaryAssociation = BinaryAssociation(
    name="proposal192",
    ends={
        Property(name="Proposal193", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessments", type=rationale_Proposal, multiplicity=Multiplicity(0, 1))
    }
)
criterion194: BinaryAssociation = BinaryAssociation(
    name="criterion194",
    ends={
        Property(name="Criterion", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessments195", type=rationale_Criterion, multiplicity=Multiplicity(0, 1))
    }
)
sender196: BinaryAssociation = BinaryAssociation(
    name="sender196",
    ends={
        Property(name="organization_OrgUnit197", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
recipients198: BinaryAssociation = BinaryAssociation(
    name="recipients198",
    ends={
        Property(name="organization_OrgUnit200", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment199", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
commentedElement201: BinaryAssociation = BinaryAssociation(
    name="commentedElement201",
    ends={
        Property(name="UnicaseModelElement202", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
audioFile203: BinaryAssociation = BinaryAssociation(
    name="audioFile203",
    ends={
        Property(name="attachment_FileAttachment", type=model_rationale_AudioComment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_AudioComment", type=attachment_FileAttachment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conflictingProposals204: BinaryAssociation = BinaryAssociation(
    name="conflictingProposals204",
    ends={
        Property(name="change_MergingProposal", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal", type=change_MergingProposal, multiplicity=Multiplicity(0, 9999))
    }
)
pendingChanges205: BinaryAssociation = BinaryAssociation(
    name="pendingChanges205",
    ends={
        Property(name="change_ModelChangePackage207", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal206", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 1))
    }
)
components220: BinaryAssociation = BinaryAssociation(
    name="components220",
    ends={
        Property(name="component_Component", type=model_component_DeploymentNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_DeploymentNode", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
packages210: BinaryAssociation = BinaryAssociation(
    name="packages210",
    ends={
        Property(name="classes_Package", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
subsystems211: BinaryAssociation = BinaryAssociation(
    name="subsystems211",
    ends={
        Property(name="classes_Package213", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component212", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
offeredServices214: BinaryAssociation = BinaryAssociation(
    name="offeredServices214",
    ends={
        Property(name="ComponentService", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="offeringComponent", type=component_ComponentService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumedServices215: BinaryAssociation = BinaryAssociation(
    name="consumedServices215",
    ends={
        Property(name="ComponentService216", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="consumingComponents", type=component_ComponentService, multiplicity=Multiplicity(0, 9999))
    }
)
offeringComponent217: BinaryAssociation = BinaryAssociation(
    name="offeringComponent217",
    ends={
        Property(name="Component", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="offeredServices", type=component_Component, multiplicity=Multiplicity(0, 1))
    }
)
consumingComponents218: BinaryAssociation = BinaryAssociation(
    name="consumingComponents218",
    ends={
        Property(name="Component219", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="consumedServices", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
facilitator221: BinaryAssociation = BinaryAssociation(
    name="facilitator221",
    ends={
        Property(name="organization_User", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
minutetaker222: BinaryAssociation = BinaryAssociation(
    name="minutetaker222",
    ends={
        Property(name="organization_User224", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting223", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
timekeeper225: BinaryAssociation = BinaryAssociation(
    name="timekeeper225",
    ends={
        Property(name="organization_User227", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting226", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
participants228: BinaryAssociation = BinaryAssociation(
    name="participants228",
    ends={
        Property(name="organization_OrgUnit230", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting229", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
sections231: BinaryAssociation = BinaryAssociation(
    name="sections231",
    ends={
        Property(name="meeting_MeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting232", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiedIssuesSection233: BinaryAssociation = BinaryAssociation(
    name="identifiedIssuesSection233",
    ends={
        Property(name="meeting_IssueMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting234", type=meeting_IssueMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
identifiedWorkItemsSection235: BinaryAssociation = BinaryAssociation(
    name="identifiedWorkItemsSection235",
    ends={
        Property(name="meeting_WorkItemMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting236", type=meeting_WorkItemMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
subsections237: BinaryAssociation = BinaryAssociation(
    name="subsections237",
    ends={
        Property(name="meeting_MeetingSection238", type=model_meeting_CompositeMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_CompositeMeetingSection", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedIssues239: BinaryAssociation = BinaryAssociation(
    name="includedIssues239",
    ends={
        Property(name="rationale_Issue", type=model_meeting_IssueMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_IssueMeetingSection", type=rationale_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
includedWorkItems240: BinaryAssociation = BinaryAssociation(
    name="includedWorkItems240",
    ends={
        Property(name="task_WorkItem", type=model_meeting_WorkItemMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_WorkItemMeetingSection", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
source241: BinaryAssociation = BinaryAssociation(
    name="source241",
    ends={
        Property(name="StateNode", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
target242: BinaryAssociation = BinaryAssociation(
    name="target242",
    ends={
        Property(name="StateNode243", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions244: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions244",
    ends={
        Property(name="Transition", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source245", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions246: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions246",
    ends={
        Property(name="Transition248", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target247", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeAttributes255: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributes255",
    ends={
        Property(name="StereotypeAttribute", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype256", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
affectedContainers249: BinaryAssociation = BinaryAssociation(
    name="affectedContainers249",
    ends={
        Property(name="UnicaseModelElement250", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_profile_Profile", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypes251: BinaryAssociation = BinaryAssociation(
    name="stereotypes251",
    ends={
        Property(name="Stereotype", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="profile", type=profile_Stereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
profile252: BinaryAssociation = BinaryAssociation(
    name="profile252",
    ends={
        Property(name="Profile", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypes", type=profile_Profile, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeInstances253: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstances253",
    ends={
        Property(name="StereotypeInstance254", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
target272: BinaryAssociation = BinaryAssociation(
    name="target272",
    ends={
        Property(name="ModelElementId274", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath273", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path275: BinaryAssociation = BinaryAssociation(
    name="path275",
    ends={
        Property(name="ModelElementId277", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath276", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype257: BinaryAssociation = BinaryAssociation(
    name="stereotype257",
    ends={
        Property(name="Stereotype258", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeInstances", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
modelElement259: BinaryAssociation = BinaryAssociation(
    name="modelElement259",
    ends={
        Property(name="UnicaseModelElement260", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedStereotypeInstances", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances261: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances261",
    ends={
        Property(name="StereotypeAttributeInstance", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeInstance", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype262: BinaryAssociation = BinaryAssociation(
    name="stereotype262",
    ends={
        Property(name="Stereotype263", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributes", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances264: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances264",
    ends={
        Property(name="StereotypeAttributeInstance265", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttribute", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeInstance266: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstance266",
    ends={
        Property(name="StereotypeInstance267", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributeInstances", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttribute268: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttribute268",
    ends={
        Property(name="StereotypeAttribute270", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributeInstances269", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
source271: BinaryAssociation = BinaryAssociation(
    name="source271",
    ends={
        Property(name="ModelElementId", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingTransitions278: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions278",
    ends={
        Property(name="Transition280", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="source279", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions281: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions281",
    ends={
        Property(name="Transition283", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="target282", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source284: BinaryAssociation = BinaryAssociation(
    name="source284",
    ends={
        Property(name="ActivityObject", type=model_activity_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions285", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1))
    }
)
target286: BinaryAssociation = BinaryAssociation(
    name="target286",
    ends={
        Property(name="ActivityObject288", type=model_activity_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions287", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1))
    }
)
projectId289: BinaryAssociation = BinaryAssociation(
    name="projectId289",
    ends={
        Property(name="ProjectId", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
versions290: BinaryAssociation = BinaryAssociation(
    name="versions290",
    ends={
        Property(name="versioning_Version", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory291", type=versioning_Version, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
projectId292: BinaryAssociation = BinaryAssociation(
    name="projectId292",
    ends={
        Property(name="ProjectId293", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo", type=ProjectId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
version294: BinaryAssociation = BinaryAssociation(
    name="version294",
    ends={
        Property(name="versioning_PrimaryVersionSpec", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo295", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups296: BinaryAssociation = BinaryAssociation(
    name="groups296",
    ends={
        Property(name="accesscontrol_ACGroup", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace", type=accesscontrol_ACGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects297: BinaryAssociation = BinaryAssociation(
    name="projects297",
    ends={
        Property(name="ProjectHistory", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace298", type=ProjectHistory, multiplicity=Multiplicity(0, 9999))
    }
)
openSessions299: BinaryAssociation = BinaryAssociation(
    name="openSessions299",
    ends={
        Property(name="SessionId", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace300", type=SessionId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users301: BinaryAssociation = BinaryAssociation(
    name="users301",
    ends={
        Property(name="accesscontrol_ACUser", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace302", type=accesscontrol_ACUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changePackage322: BinaryAssociation = BinaryAssociation(
    name="changePackage322",
    ends={
        Property(name="versioning_ChangePackage", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo323", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source324: BinaryAssociation = BinaryAssociation(
    name="source324",
    ends={
        Property(name="versioning_PrimaryVersionSpec325", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target326: BinaryAssociation = BinaryAssociation(
    name="target326",
    ends={
        Property(name="versioning_PrimaryVersionSpec328", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery327", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations303: BinaryAssociation = BinaryAssociation(
    name="operations303",
    ends={
        Property(name="operations_AbstractOperation", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events304: BinaryAssociation = BinaryAssociation(
    name="events304",
    ends={
        Property(name="events_Event", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage305", type=events_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logMessage306: BinaryAssociation = BinaryAssociation(
    name="logMessage306",
    ends={
        Property(name="versioning_LogMessage", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage307", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications308: BinaryAssociation = BinaryAssociation(
    name="notifications308",
    ends={
        Property(name="notification_ESNotification", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage309", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties310: BinaryAssociation = BinaryAssociation(
    name="versionProperties310",
    ends={
        Property(name="versioning_VersionProperty", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage311", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primerySpec312: BinaryAssociation = BinaryAssociation(
    name="primerySpec312",
    ends={
        Property(name="versioning_PrimaryVersionSpec313", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
logMessage314: BinaryAssociation = BinaryAssociation(
    name="logMessage314",
    ends={
        Property(name="versioning_LogMessage316", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo315", type=versioning_LogMessage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs317: BinaryAssociation = BinaryAssociation(
    name="tagSpecs317",
    ends={
        Property(name="versioning_TagVersionSpec", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo318", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties319: BinaryAssociation = BinaryAssociation(
    name="versionProperties319",
    ends={
        Property(name="versioning_VersionProperty321", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo320", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElements329: BinaryAssociation = BinaryAssociation(
    name="modelElements329",
    ends={
        Property(name="ModelElementId331", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery330", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectState332: BinaryAssociation = BinaryAssociation(
    name="projectState332",
    ends={
        Property(name="Project", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version", type=Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primarySpec333: BinaryAssociation = BinaryAssociation(
    name="primarySpec333",
    ends={
        Property(name="versioning_PrimaryVersionSpec335", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version334", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs336: BinaryAssociation = BinaryAssociation(
    name="tagSpecs336",
    ends={
        Property(name="versioning_TagVersionSpec338", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version337", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextVersion339: BinaryAssociation = BinaryAssociation(
    name="nextVersion339",
    ends={
        Property(name="Version", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="previousVersion", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
previousVersion340: BinaryAssociation = BinaryAssociation(
    name="previousVersion340",
    ends={
        Property(name="Version341", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="nextVersion", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
changes342: BinaryAssociation = BinaryAssociation(
    name="changes342",
    ends={
        Property(name="versioning_ChangePackage344", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version343", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logMessage345: BinaryAssociation = BinaryAssociation(
    name="logMessage345",
    ends={
        Property(name="versioning_LogMessage347", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version346", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId348: BinaryAssociation = BinaryAssociation(
    name="modelElementId348",
    ends={
        Property(name="ModelElementId349", type=esmodel_operations_AbstractOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_AbstractOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subOperations350: BinaryAssociation = BinaryAssociation(
    name="subOperations350",
    ends={
        Property(name="operations_AbstractOperation351", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainOperation352: BinaryAssociation = BinaryAssociation(
    name="mainOperation352",
    ends={
        Property(name="operations_AbstractOperation354", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation353", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1))
    }
)
oldValue360: BinaryAssociation = BinaryAssociation(
    name="oldValue360",
    ends={
        Property(name="ModelElementId361", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue362: BinaryAssociation = BinaryAssociation(
    name="newValue362",
    ends={
        Property(name="ModelElementId364", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation363", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement355: BinaryAssociation = BinaryAssociation(
    name="modelElement355",
    ends={
        Property(name="operations_esmodel_EObject", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subOperations356: BinaryAssociation = BinaryAssociation(
    name="subOperations356",
    ends={
        Property(name="operations_ReferenceOperation", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation357", type=operations_ReferenceOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eObjectToIdMap358: BinaryAssociation = BinaryAssociation(
    name="eObjectToIdMap358",
    ends={
        Property(name="operations_EObjectToModelElementIdMap", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation359", type=operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElements376: BinaryAssociation = BinaryAssociation(
    name="modelElements376",
    ends={
        Property(name="ModelElementId377", type=esmodel_operations_ModelElementGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_ModelElementGroup", type=ModelElementId, multiplicity=Multiplicity(0, 9999))
    }
)
key378: BinaryAssociation = BinaryAssociation(
    name="key378",
    ends={
        Property(name="operations_esmodel_EObject379", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value380: BinaryAssociation = BinaryAssociation(
    name="value380",
    ends={
        Property(name="ModelElementId382", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap381", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oldValue365: BinaryAssociation = BinaryAssociation(
    name="oldValue365",
    ends={
        Property(name="ModelElementId366", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue367: BinaryAssociation = BinaryAssociation(
    name="newValue367",
    ends={
        Property(name="ModelElementId369", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation368", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedModelElements370: BinaryAssociation = BinaryAssociation(
    name="referencedModelElements370",
    ends={
        Property(name="ModelElementId371", type=esmodel_operations_MultiReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModelElementId372: BinaryAssociation = BinaryAssociation(
    name="referencedModelElementId372",
    ends={
        Property(name="ModelElementId373", type=esmodel_operations_MultiReferenceMoveOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceMoveOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations374: BinaryAssociation = BinaryAssociation(
    name="operations374",
    ends={
        Property(name="operations_AbstractOperation375", type=esmodel_operations_OperationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_OperationGroup", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999))
    }
)
baseVersion395: BinaryAssociation = BinaryAssociation(
    name="baseVersion395",
    ends={
        Property(name="versioning_PrimaryVersionSpec396", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion397: BinaryAssociation = BinaryAssociation(
    name="targetVersion397",
    ends={
        Property(name="versioning_PrimaryVersionSpec399", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent398", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotatedElement400: BinaryAssociation = BinaryAssociation(
    name="annotatedElement400",
    ends={
        Property(name="ModelElementId401", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation402: BinaryAssociation = BinaryAssociation(
    name="annotation402",
    ends={
        Property(name="ModelElementId404", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent403", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement383: BinaryAssociation = BinaryAssociation(
    name="modelElement383",
    ends={
        Property(name="ModelElementId384", type=esmodel_events_ReadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ReadEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseVersion385: BinaryAssociation = BinaryAssociation(
    name="baseVersion385",
    ends={
        Property(name="versioning_PrimaryVersionSpec386", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion387: BinaryAssociation = BinaryAssociation(
    name="targetVersion387",
    ends={
        Property(name="versioning_PrimaryVersionSpec389", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent388", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localChanges390: BinaryAssociation = BinaryAssociation(
    name="localChanges390",
    ends={
        Property(name="operations_AbstractOperation392", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent391", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseVersion393: BinaryAssociation = BinaryAssociation(
    name="baseVersion393",
    ends={
        Property(name="versioning_PrimaryVersionSpec394", type=esmodel_events_CheckoutEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_CheckoutEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElement423: BinaryAssociation = BinaryAssociation(
    name="sourceElement423",
    ends={
        Property(name="esmodel_events_TraceEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ModelElementId424", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1))
    }
)
targetElement425: BinaryAssociation = BinaryAssociation(
    name="targetElement425",
    ends={
        Property(name="ModelElementId427", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_TraceEvent426", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createdElement428: BinaryAssociation = BinaryAssociation(
    name="createdElement428",
    ends={
        Property(name="ModelElementId429", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceSection430: BinaryAssociation = BinaryAssociation(
    name="sourceSection430",
    ends={
        Property(name="ModelElementId432", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent431", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion405: BinaryAssociation = BinaryAssociation(
    name="sourceVersion405",
    ends={
        Property(name="versioning_PrimaryVersionSpec406", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion407: BinaryAssociation = BinaryAssociation(
    name="targetVersion407",
    ends={
        Property(name="versioning_PrimaryVersionSpec409", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent408", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement410: BinaryAssociation = BinaryAssociation(
    name="modelElement410",
    ends={
        Property(name="ModelElementId412", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent411", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dragSourceElement413: BinaryAssociation = BinaryAssociation(
    name="dragSourceElement413",
    ends={
        Property(name="ModelElementId414", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropTargetElement415: BinaryAssociation = BinaryAssociation(
    name="dropTargetElement415",
    ends={
        Property(name="ModelElementId417", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent416", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElement418: BinaryAssociation = BinaryAssociation(
    name="sourceElement418",
    ends={
        Property(name="ModelElementId419", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetElement420: BinaryAssociation = BinaryAssociation(
    name="targetElement420",
    ends={
        Property(name="ModelElementId422", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent421", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myAcceptedChanges447: BinaryAssociation = BinaryAssociation(
    name="myAcceptedChanges447",
    ends={
        Property(name="operations_OperationId", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theirRejectedChanges448: BinaryAssociation = BinaryAssociation(
    name="theirRejectedChanges448",
    ends={
        Property(name="operations_OperationId450", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent449", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextModelElement451: BinaryAssociation = BinaryAssociation(
    name="contextModelElement451",
    ends={
        Property(name="ModelElementId453", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent452", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation433: BinaryAssociation = BinaryAssociation(
    name="operation433",
    ends={
        Property(name="operations_AbstractOperation434", type=esmodel_events_UndoEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UndoEvent", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion435: BinaryAssociation = BinaryAssociation(
    name="sourceVersion435",
    ends={
        Property(name="versioning_PrimaryVersionSpec436", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion437: BinaryAssociation = BinaryAssociation(
    name="targetVersion437",
    ends={
        Property(name="versioning_PrimaryVersionSpec439", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent438", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications440: BinaryAssociation = BinaryAssociation(
    name="notifications440",
    ends={
        Property(name="notification_ESNotification441", type=esmodel_events_NotificationGenerationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NotificationGenerationEvent", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceModelElement442: BinaryAssociation = BinaryAssociation(
    name="sourceModelElement442",
    ends={
        Property(name="ModelElementId443", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceURL444: BinaryAssociation = BinaryAssociation(
    name="sourceURL444",
    ends={
        Property(name="ModelElementId446", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent445", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties459: BinaryAssociation = BinaryAssociation(
    name="properties459",
    ends={
        Property(name="accesscontrol_OrgUnitProperty", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit460", type=accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members461: BinaryAssociation = BinaryAssociation(
    name="members461",
    ends={
        Property(name="accesscontrol_ACOrgUnit", type=esmodel_accesscontrol_ACGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACGroup", type=accesscontrol_ACOrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
project462: BinaryAssociation = BinaryAssociation(
    name="project462",
    ends={
        Property(name="ProjectId463", type=esmodel_accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_OrgUnitProperty", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectId454: BinaryAssociation = BinaryAssociation(
    name="projectId454",
    ends={
        Property(name="ProjectId455", type=esmodel_server_ServerProjectEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ServerProjectEvent", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newVersion456: BinaryAssociation = BinaryAssociation(
    name="newVersion456",
    ends={
        Property(name="versioning_PrimaryVersionSpec457", type=esmodel_server_ProjectUpdatedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ProjectUpdatedEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles458: BinaryAssociation = BinaryAssociation(
    name="roles458",
    ends={
        Property(name="roles_Role", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit", type=roles_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedModelElements468: BinaryAssociation = BinaryAssociation(
    name="relatedModelElements468",
    ends={
        Property(name="ModelElementId470", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification469", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedOperations471: BinaryAssociation = BinaryAssociation(
    name="relatedOperations471",
    ends={
        Property(name="operations_OperationId473", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification472", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectId474: BinaryAssociation = BinaryAssociation(
    name="projectId474",
    ends={
        Property(name="ProjectId475", type=esmodel_url_ProjectUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ProjectUrlFragment", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId476: BinaryAssociation = BinaryAssociation(
    name="modelElementId476",
    ends={
        Property(name="ModelElementId477", type=esmodel_url_ModelElementUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrlFragment", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projects464: BinaryAssociation = BinaryAssociation(
    name="projects464",
    ends={
        Property(name="ProjectId465", type=esmodel_roles_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_roles_Role", type=ProjectId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project466: BinaryAssociation = BinaryAssociation(
    name="project466",
    ends={
        Property(name="ProjectId467", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serverUrl478: BinaryAssociation = BinaryAssociation(
    name="serverUrl478",
    ends={
        Property(name="url_ServerUrl", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl", type=url_ServerUrl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectUrlFragment479: BinaryAssociation = BinaryAssociation(
    name="projectUrlFragment479",
    ends={
        Property(name="url_ProjectUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl480", type=url_ProjectUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementUrlFragment481: BinaryAssociation = BinaryAssociation(
    name="modelElementUrlFragment481",
    ends={
        Property(name="url_ModelElementUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl482", type=url_ModelElementUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_metamodel_ModelElement_IdentifiableElement = Generalization(general=IdentifiableElement, specific=metamodel_ModelElement)
gen_metamodel_ModelElementId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=metamodel_ModelElementId)
gen_model_UnicaseModelElement_ModelElement = Generalization(general=ModelElement, specific=model_UnicaseModelElement)
gen_model_Annotation_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_Annotation)
gen_model_Attachment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_Attachment)
gen_model_Project_Project = Generalization(general=Project, specific=model_Project)
gen_model_organization_OrgUnit_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_organization_OrgUnit)
gen_model_organization_User_OrgUnit = Generalization(general=OrgUnit, specific=model_organization_User)
gen_model_organization_Group_OrgUnit = Generalization(general=OrgUnit, specific=model_organization_Group)
gen_model_task_WorkItem_Annotation = Generalization(general=Annotation, specific=model_task_WorkItem)
gen_model_task_WorkPackage_WorkItem = Generalization(general=WorkItem, specific=model_task_WorkPackage)
gen_model_task_Milestone_WorkItem = Generalization(general=WorkItem, specific=model_task_Milestone)
gen_model_classes_PackageElement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_PackageElement)
gen_model_task_Checkable_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_task_Checkable)
gen_model_task_ActionItem_task_WorkItem = Generalization(general=task_WorkItem, specific=model_task_ActionItem)
gen_model_task_ActionItem_task_Checkable = Generalization(general=task_Checkable, specific=model_task_ActionItem)
gen_model_diagram_MEDiagram_Attachment = Generalization(general=Attachment, specific=model_diagram_MEDiagram)
gen_model_classes_Class_PackageElement = Generalization(general=PackageElement, specific=model_classes_Class)
gen_model_classes_Package_PackageElement = Generalization(general=PackageElement, specific=model_classes_Package)
gen_model_classes_Association_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Association)
gen_model_classes_Attribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Attribute)
gen_model_classes_Method_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Method)
gen_model_classes_MethodArgument_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_MethodArgument)
gen_model_requirement_FunctionalRequirement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_FunctionalRequirement)
gen_model_classes_Dependency_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Dependency)
gen_model_document_Section_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_document_Section)
gen_model_document_LeafSection_Section = Generalization(general=Section, specific=model_document_LeafSection)
gen_model_document_CompositeSection_Section = Generalization(general=Section, specific=model_document_CompositeSection)
gen_model_requirement_UseCase_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UseCase)
gen_model_requirement_Scenario_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Scenario)
gen_model_requirement_Actor_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Actor)
gen_model_requirement_UserTask_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UserTask)
gen_model_requirement_ActorInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_ActorInstance)
gen_model_requirement_Step_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Step)
gen_model_requirement_Step_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_Step)
gen_model_requirement_SystemFunction_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_SystemFunction)
gen_model_rationale_Issue_Annotation = Generalization(general=Annotation, specific=model_rationale_Issue)
gen_model_rationale_Issue_task_Checkable = Generalization(general=task_Checkable, specific=model_rationale_Issue)
gen_model_requirement_NonFunctionalRequirement_Criterion = Generalization(general=Criterion, specific=model_requirement_NonFunctionalRequirement)
gen_model_requirement_Workspace_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Workspace)
gen_model_rationale_Criterion_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Criterion)
gen_model_rationale_Issue_task_WorkItem = Generalization(general=task_WorkItem, specific=model_rationale_Issue)
gen_model_rationale_Proposal_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Proposal)
gen_model_rationale_Proposal_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Proposal)
gen_model_rationale_Solution_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Solution)
gen_model_rationale_Solution_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Solution)
gen_model_change_MergingSolution_Solution = Generalization(general=Solution, specific=model_change_MergingSolution)
gen_model_bug_BugReport_task_WorkItem = Generalization(general=task_WorkItem, specific=model_bug_BugReport)
gen_model_bug_BugReport_task_Checkable = Generalization(general=task_Checkable, specific=model_bug_BugReport)
gen_model_rationale_Assessment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Assessment)
gen_model_rationale_Assessment_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Assessment)
gen_model_rationale_Comment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Comment)
gen_model_rationale_Comment_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Comment)
gen_model_change_ModelChangePackage_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_change_ModelChangePackage)
gen_model_change_MergingIssue_Issue = Generalization(general=Issue, specific=model_change_MergingIssue)
gen_model_change_MergingProposal_Proposal = Generalization(general=Proposal, specific=model_change_MergingProposal)
gen_model_component_DeploymentNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_DeploymentNode)
gen_model_component_Component_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_Component)
gen_model_component_ComponentService_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_ComponentService)
gen_model_meeting_MeetingSection_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_MeetingSection)
gen_model_meeting_Meeting_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_Meeting)
gen_model_attachment_FileAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_FileAttachment)
gen_model_meeting_CompositeMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_CompositeMeetingSection)
gen_model_meeting_IssueMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_IssueMeetingSection)
gen_model_meeting_WorkItemMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_WorkItemMeetingSection)
gen_model_state_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_Transition)
gen_model_state_StateNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_StateNode)
gen_model_state_State_StateNode = Generalization(general=StateNode, specific=model_state_State)
gen_model_state_StateInitial_StateNode = Generalization(general=StateNode, specific=model_state_StateInitial)
gen_model_state_StateEnd_StateNode = Generalization(general=StateNode, specific=model_state_StateEnd)
gen_model_attachment_UrlAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_UrlAttachment)
gen_model_profile_StereotypeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeInstance)
gen_model_profile_Profile_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Profile)
gen_model_profile_Stereotype_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Stereotype)
gen_model_profile_StereotypeAttribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttribute)
gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute = Generalization(general=StereotypeAttribute, specific=model_profile_StereotypeAttributeSimple)
gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttributeInstance)
gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance = Generalization(general=StereotypeAttributeInstance, specific=model_profile_StereotypeAttributeInstanceString)
gen_model_activity_ActivityObject_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_ActivityObject)
gen_model_activity_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_Transition)
gen_esmodel_ProjectId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_ProjectId)
gen_model_activity_Activity_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Activity)
gen_model_activity_Fork_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Fork)
gen_model_activity_Branch_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Branch)
gen_model_activity_ActivityInitial_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityInitial)
gen_model_activity_ActivityEnd_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityEnd)
gen_esmodel_SessionId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_SessionId)
gen_esmodel_FileIdentifier_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_FileIdentifier)
gen_esmodel_versioning_TagVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_TagVersionSpec)
gen_esmodel_versioning_DateVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_DateVersionSpec)
gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_PrimaryVersionSpec)
gen_esmodel_operations_FeatureOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_FeatureOperation)
gen_esmodel_versioning_HeadVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_HeadVersionSpec)
gen_esmodel_operations_AbstractOperation_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_operations_AbstractOperation)
gen_esmodel_operations_CompositeOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CompositeOperation)
gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeSetOperation)
gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeMoveOperation)
gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_SingleReferenceOperation)
gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceSetOperation)
gen_esmodel_operations_CreateDeleteOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CreateDeleteOperation)
gen_esmodel_operations_AttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_AttributeOperation)
gen_esmodel_operations_MultiAttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeOperation)
gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceOperation)
gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiReferenceMoveOperation)
gen_esmodel_operations_ReferenceOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_ReferenceOperation)
gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation = Generalization(general=AttributeOperation, specific=esmodel_operations_DiagramLayoutOperation)
gen_esmodel_operations_OperationId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_operations_OperationId)
gen_esmodel_events_PluginStartEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginStartEvent)
gen_esmodel_events_UpdateEvent_Event = Generalization(general=Event, specific=esmodel_events_UpdateEvent)
gen_esmodel_events_AnnotationEvent_Event = Generalization(general=Event, specific=esmodel_events_AnnotationEvent)
gen_esmodel_events_RevertEvent_Event = Generalization(general=Event, specific=esmodel_events_RevertEvent)
gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation = Generalization(general=CompositeOperation, specific=esmodel_semantic_SemanticCompositeOperation)
gen_esmodel_events_ReadEvent_Event = Generalization(general=Event, specific=esmodel_events_ReadEvent)
gen_esmodel_events_MergeEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeEvent)
gen_esmodel_events_CheckoutEvent_Event = Generalization(general=Event, specific=esmodel_events_CheckoutEvent)
gen_esmodel_events_ExceptionEvent_Event = Generalization(general=Event, specific=esmodel_events_ExceptionEvent)
gen_esmodel_events_NavigatorCreateEvent_Event = Generalization(general=Event, specific=esmodel_events_NavigatorCreateEvent)
gen_esmodel_events_PluginFocusEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginFocusEvent)
gen_esmodel_events_PresentationSwitchEvent_Event = Generalization(general=Event, specific=esmodel_events_PresentationSwitchEvent)
gen_esmodel_events_ShowHistoryEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowHistoryEvent)
gen_esmodel_events_PerspectiveEvent_Event = Generalization(general=Event, specific=esmodel_events_PerspectiveEvent)
gen_esmodel_events_DNDEvent_Event = Generalization(general=Event, specific=esmodel_events_DNDEvent)
gen_esmodel_events_LinkEvent_Event = Generalization(general=Event, specific=esmodel_events_LinkEvent)
gen_esmodel_events_TraceEvent_Event = Generalization(general=Event, specific=esmodel_events_TraceEvent)
gen_esmodel_events_MergeChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeChoiceEvent)
gen_esmodel_events_UndoEvent_Event = Generalization(general=Event, specific=esmodel_events_UndoEvent)
gen_esmodel_events_Validate_Event = Generalization(general=Event, specific=esmodel_events_Validate)
gen_esmodel_events_ShowChangesEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowChangesEvent)
gen_esmodel_events_NotificationReadEvent_ReadEvent = Generalization(general=ReadEvent, specific=esmodel_events_NotificationReadEvent)
gen_esmodel_events_NotificationGenerationEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationGenerationEvent)
gen_esmodel_events_NotificationIgnoreEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationIgnoreEvent)
gen_esmodel_events_URLEvent_Event = Generalization(general=Event, specific=esmodel_events_URLEvent)
gen_esmodel_accesscontrol_ACGroup_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACGroup)
gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_accesscontrol_ACOrgUnitId)
gen_esmodel_events_MergeGlobalChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeGlobalChoiceEvent)
gen_esmodel_server_ServerEvent_Event = Generalization(general=Event, specific=esmodel_server_ServerEvent)
gen_esmodel_server_ServerProjectEvent_ServerEvent = Generalization(general=ServerEvent, specific=esmodel_server_ServerProjectEvent)
gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent = Generalization(general=ServerProjectEvent, specific=esmodel_server_ProjectUpdatedEvent)
gen_esmodel_accesscontrol_ACUser_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACUser)
gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_accesscontrol_ACOrgUnit)
gen_esmodel_roles_ReaderRole_Role = Generalization(general=Role, specific=esmodel_roles_ReaderRole)
gen_esmodel_roles_WriterRole_Role = Generalization(general=Role, specific=esmodel_roles_WriterRole)
gen_esmodel_roles_ProjectAdminRole_Role = Generalization(general=Role, specific=esmodel_roles_ProjectAdminRole)
gen_esmodel_roles_ServerAdmin_Role = Generalization(general=Role, specific=esmodel_roles_ServerAdmin)
gen_esmodel_notification_ESNotification_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_notification_ESNotification)

# Domain Model
domain_model = DomainModel(
    name="esmodel",
    types={Annotation, metamodel_Project, ModelElement, metamodel_UniqueIdentifier, metamodel_IdentifiableElement, metamodel_ModelElement, IdentifiableElement, metamodel_ModelElementId, UniqueIdentifier, metamodel_ModelVersion, metamodel_NonDomainElement, metamodel_AssociationClassElement, model_UnicaseModelElement, task_WorkItem, Attachment, document_LeafSection, rationale_Comment, profile_StereotypeInstance, model_Annotation, UnicaseModelElement, model_Attachment, model_NonDomainElement, model_Project, Project, model_organization_OrgUnit, organization_Group, organization_User, model_organization_User, OrgUnit, model_organization_Group, organization_OrgUnit, model_task_WorkItem, task_WorkPackage, change_ModelChangePackage, model_task_WorkPackage, WorkItem, model_task_Milestone, model_classes_PackageElement, model_task_Checkable, model_task_ActionItem, task_Checkable, model_diagram_MEDiagram, diagram_model_Diagram, classes_Attribute, classes_Package, classes_Dependency, model_classes_Class, PackageElement, classes_Class, classes_Association, classes_Method, requirement_UseCase, requirement_Scenario, model_classes_Package, classes_PackageElement, model_classes_Association, model_classes_Attribute, model_classes_Method, classes_MethodArgument, model_classes_MethodArgument, model_requirement_FunctionalRequirement, model_classes_Dependency, model_document_Section, document_CompositeSection, model_document_LeafSection, Section, model_document_CompositeSection, document_Section, requirement_FunctionalRequirement, model_requirement_UseCase, model_requirement_Scenario, requirement_Actor, requirement_Step, requirement_UserTask, requirement_NonFunctionalRequirement, requirement_SystemFunction, requirement_ActorInstance, model_requirement_Actor, requirement_Workspace, model_requirement_UserTask, model_requirement_ActorInstance, model_requirement_Step, NonDomainElement, model_requirement_SystemFunction, model_rationale_Issue, model_requirement_NonFunctionalRequirement, Criterion, model_requirement_Workspace, model_rationale_Criterion, rationale_Proposal, rationale_Solution, rationale_Criterion, model_rationale_Proposal, rationale_Issue, rationale_Assessment, model_rationale_Solution, Solution, model_bug_BugReport, model_rationale_Assessment, model_rationale_Comment, model_rationale_AudioComment, attachment_FileAttachment, model_change_ModelChangePackage, model_change_MergingIssue, Issue, model_change_MergingProposal, Proposal, change_MergingProposal, model_change_MergingSolution, model_component_DeploymentNode, model_component_Component, component_ComponentService, model_component_ComponentService, component_Component, model_meeting_MeetingSection, model_meeting_CompositeMeetingSection, model_meeting_Meeting, meeting_MeetingSection, meeting_IssueMeetingSection, meeting_WorkItemMeetingSection, model_attachment_FileAttachment, MeetingSection, model_meeting_IssueMeetingSection, model_meeting_WorkItemMeetingSection, model_state_Transition, state_StateNode, model_state_StateNode, state_Transition, model_state_State, StateNode, model_state_StateInitial, model_state_StateEnd, model_attachment_UrlAttachment, profile_StereotypeAttribute, model_profile_StereotypeInstance, model_profile_Profile, profile_Stereotype, model_profile_Stereotype, profile_Profile, profile_StereotypeAttributeInstance, model_profile_StereotypeAttribute, model_profile_StereotypeAttributeSimple, StereotypeAttribute, model_profile_StereotypeAttributeInstance, model_profile_StereotypeAttributeInstanceString, StereotypeAttributeInstance, model_util_ModelElementPath, ModelElementId, model_activity_ActivityObject, activity_Transition, model_activity_Transition, activity_ActivityObject, esmodel_ProjectId, esmodel_VersionInfo, esmodel_ClientVersionInfo, model_activity_Activity, ActivityObject, model_activity_Fork, model_activity_Branch, model_activity_ActivityInitial, model_activity_ActivityEnd, esmodel_ProjectHistory, ProjectId, versioning_Version, esmodel_ProjectInfo, versioning_PrimaryVersionSpec, esmodel_SessionId, esmodel_ServerSpace, accesscontrol_ACGroup, ProjectHistory, SessionId, accesscontrol_ACUser, versioning_ChangePackage, esmodel_versioning_HistoryQuery, esmodel_FileIdentifier, esmodel_versioning_TagVersionSpec, VersionSpec, esmodel_versioning_DateVersionSpec, esmodel_versioning_PrimaryVersionSpec, esmodel_versioning_VersionSpec, esmodel_versioning_LogMessage, esmodel_versioning_ChangePackage, operations_AbstractOperation, events_Event, versioning_LogMessage, notification_ESNotification, versioning_VersionProperty, esmodel_versioning_HistoryInfo, versioning_TagVersionSpec, esmodel_operations_FeatureOperation, esmodel_versioning_Version, esmodel_versioning_HeadVersionSpec, esmodel_versioning_VersionProperty, esmodel_operations_AbstractOperation, esmodel_operations_CompositeOperation, AbstractOperation, esmodel_operations_MultiAttributeSetOperation, esmodel_operations_MultiAttributeMoveOperation, esmodel_operations_SingleReferenceOperation, ReferenceOperation, esmodel_operations_MultiReferenceSetOperation, esmodel_operations_CreateDeleteOperation, operations_esmodel_EObject, operations_ReferenceOperation, operations_EObjectToModelElementIdMap, esmodel_operations_AttributeOperation, FeatureOperation, esmodel_operations_MultiAttributeOperation, esmodel_operations_ModelElementGroup, esmodel_operations_EObjectToModelElementIdMap, esmodel_semantic_SemanticCompositeOperation, esmodel_operations_MultiReferenceOperation, esmodel_operations_MultiReferenceMoveOperation, esmodel_operations_ReferenceOperation, esmodel_operations_DiagramLayoutOperation, AttributeOperation, esmodel_operations_OperationId, esmodel_operations_OperationGroup, esmodel_events_PluginStartEvent, esmodel_events_UpdateEvent, esmodel_events_AnnotationEvent, esmodel_events_RevertEvent, CompositeOperation, esmodel_events_ShowHistoryEvent, esmodel_events_Event, esmodel_events_ReadEvent, Event, esmodel_events_MergeEvent, esmodel_events_CheckoutEvent, esmodel_events_ExceptionEvent, esmodel_events_NavigatorCreateEvent, esmodel_events_PluginFocusEvent, esmodel_events_PresentationSwitchEvent, esmodel_events_PerspectiveEvent, esmodel_events_DNDEvent, esmodel_events_LinkEvent, esmodel_events_TraceEvent, esmodel_events_MergeChoiceEvent, operations_OperationId, esmodel_events_UndoEvent, esmodel_events_Validate, esmodel_events_ShowChangesEvent, esmodel_events_NotificationReadEvent, ReadEvent, esmodel_events_NotificationGenerationEvent, esmodel_events_NotificationIgnoreEvent, esmodel_events_URLEvent, accesscontrol_OrgUnitProperty, esmodel_accesscontrol_ACGroup, accesscontrol_ACOrgUnit, esmodel_accesscontrol_ACOrgUnitId, esmodel_accesscontrol_OrgUnitProperty, esmodel_roles_Role, esmodel_events_MergeGlobalChoiceEvent, esmodel_server_ServerEvent, esmodel_server_ServerProjectEvent, ServerEvent, esmodel_server_ProjectUpdatedEvent, ServerProjectEvent, esmodel_accesscontrol_ACUser, ACOrgUnit, esmodel_accesscontrol_ACOrgUnit, roles_Role, esmodel_url_ServerUrl, esmodel_url_ProjectUrlFragment, esmodel_url_ModelElementUrlFragment, esmodel_roles_ReaderRole, Role, esmodel_roles_WriterRole, esmodel_roles_ProjectAdminRole, esmodel_roles_ServerAdmin, esmodel_notification_ESNotification, esmodel_url_ModelElementUrl, url_ServerUrl, url_ProjectUrlFragment, url_ModelElementUrlFragment, ActivityType, DiagramType, AssociationType, VisibilityType, ScopeType, ArgumentDirectionType, Severity, ResolutionType, FileAttachmentType, ContainmentType, MergeChoiceSelection, MergeGlobalChoiceSelection},
    associations={annotations4, modelElements0, cutElements1, participations15, assignments16, attachments5, leafSection6, incomingDocumentReferences7, comments9, appliedStereotypeInstances10, annotatedModelElements11, referringModelElements12, groupMemberships14, reviewer28, participants29, workItemsToReview18, orgUnits20, containingWorkpackage21, successors22, predecessors24, assignee26, associatedChangePackages31, containedWorkItems32, containedModelElements34, elements36, gmfdiagram38, newElements40, attributes55, parentPackage43, outgoingDependencies44, incomingDependencies45, subClasses47, superClasses48, outgoingAssociations50, incomingAssociations52, methods56, participatedUseCases58, demoParticipations59, facadeClass60, containedPackageElements61, source62, target64, definingClass66, definingClass68, calledMethods70, callingMethods72, arguments74, demoParticipations75, source77, target79, parent81, modelElements82, referencedModelElements84, subsections86, includedUseCases100, refiningRequirements87, refinedRequirement88, stakeholder90, useCases91, scenarios93, functionalRequirements96, identifiedClasses98, instantiatedUseCases114, extendedUseCases101, scenarios104, initiatingActor106, participatingActors107, useCaseSteps110, realizedUserTask111, nonFunctionalRequirements112, systemFunctions113, instances134, participatedUserTasks136, functionalRequirements116, participatingMethods119, participatingClasses121, initiatingActorInstance124, participatingActorInstances125, steps127, nonFunctionalRequirements128, initiatedUseCases130, participatedUseCases132, workspace159, initiatedUserTask139, initiatedScenarios142, participatedScenarios144, instantiatedActor146, includedUseCase148, useCase150, includedSystemFunction152, nonFunctionalRequirement154, usecases156, systemFunctions179, initiatingActor161, participatingActors163, realizingUseCases165, nonFunctionalRequirements167, restrictedUseCases169, restrictedScenarios171, systemFunctions174, userTasks176, issue188, assessments190, proposals181, solution182, criteria184, issue185, assessments186, underlyingProposals187, appliedChanges208, proposal192, criterion194, sender196, recipients198, commentedElement201, audioFile203, conflictingProposals204, pendingChanges205, components220, packages210, subsystems211, offeredServices214, consumedServices215, offeringComponent217, consumingComponents218, facilitator221, minutetaker222, timekeeper225, participants228, sections231, identifiedIssuesSection233, identifiedWorkItemsSection235, subsections237, includedIssues239, includedWorkItems240, source241, target242, outgoingTransitions244, incomingTransitions246, stereotypeAttributes255, affectedContainers249, stereotypes251, profile252, stereotypeInstances253, target272, path275, stereotype257, modelElement259, stereotypeAttributeInstances261, stereotype262, stereotypeAttributeInstances264, stereotypeInstance266, stereotypeAttribute268, source271, outgoingTransitions278, incomingTransitions281, source284, target286, projectId289, versions290, projectId292, version294, groups296, projects297, openSessions299, users301, changePackage322, source324, target326, operations303, events304, logMessage306, notifications308, versionProperties310, primerySpec312, logMessage314, tagSpecs317, versionProperties319, modelElements329, projectState332, primarySpec333, tagSpecs336, nextVersion339, previousVersion340, changes342, logMessage345, modelElementId348, subOperations350, mainOperation352, oldValue360, newValue362, modelElement355, subOperations356, eObjectToIdMap358, modelElements376, key378, value380, oldValue365, newValue367, referencedModelElements370, referencedModelElementId372, operations374, baseVersion395, targetVersion397, annotatedElement400, annotation402, modelElement383, baseVersion385, targetVersion387, localChanges390, baseVersion393, sourceElement423, targetElement425, createdElement428, sourceSection430, sourceVersion405, targetVersion407, modelElement410, dragSourceElement413, dropTargetElement415, sourceElement418, targetElement420, myAcceptedChanges447, theirRejectedChanges448, contextModelElement451, operation433, sourceVersion435, targetVersion437, notifications440, sourceModelElement442, sourceURL444, properties459, members461, project462, projectId454, newVersion456, roles458, relatedModelElements468, relatedOperations471, projectId474, modelElementId476, projects464, project466, serverUrl478, projectUrlFragment479, modelElementUrlFragment481},
    generalizations={gen_metamodel_ModelElement_IdentifiableElement, gen_metamodel_ModelElementId_UniqueIdentifier, gen_model_UnicaseModelElement_ModelElement, gen_model_Annotation_UnicaseModelElement, gen_model_Attachment_UnicaseModelElement, gen_model_Project_Project, gen_model_organization_OrgUnit_UnicaseModelElement, gen_model_organization_User_OrgUnit, gen_model_organization_Group_OrgUnit, gen_model_task_WorkItem_Annotation, gen_model_task_WorkPackage_WorkItem, gen_model_task_Milestone_WorkItem, gen_model_classes_PackageElement_UnicaseModelElement, gen_model_task_Checkable_UnicaseModelElement, gen_model_task_ActionItem_task_WorkItem, gen_model_task_ActionItem_task_Checkable, gen_model_diagram_MEDiagram_Attachment, gen_model_classes_Class_PackageElement, gen_model_classes_Package_PackageElement, gen_model_classes_Association_UnicaseModelElement, gen_model_classes_Attribute_UnicaseModelElement, gen_model_classes_Method_UnicaseModelElement, gen_model_classes_MethodArgument_UnicaseModelElement, gen_model_requirement_FunctionalRequirement_UnicaseModelElement, gen_model_classes_Dependency_UnicaseModelElement, gen_model_document_Section_UnicaseModelElement, gen_model_document_LeafSection_Section, gen_model_document_CompositeSection_Section, gen_model_requirement_UseCase_UnicaseModelElement, gen_model_requirement_Scenario_UnicaseModelElement, gen_model_requirement_Actor_UnicaseModelElement, gen_model_requirement_UserTask_UnicaseModelElement, gen_model_requirement_ActorInstance_UnicaseModelElement, gen_model_requirement_Step_UnicaseModelElement, gen_model_requirement_Step_NonDomainElement, gen_model_requirement_SystemFunction_UnicaseModelElement, gen_model_rationale_Issue_Annotation, gen_model_rationale_Issue_task_Checkable, gen_model_requirement_NonFunctionalRequirement_Criterion, gen_model_requirement_Workspace_UnicaseModelElement, gen_model_rationale_Criterion_UnicaseModelElement, gen_model_rationale_Issue_task_WorkItem, gen_model_rationale_Proposal_UnicaseModelElement, gen_model_rationale_Proposal_NonDomainElement, gen_model_rationale_Solution_UnicaseModelElement, gen_model_rationale_Solution_NonDomainElement, gen_model_change_MergingSolution_Solution, gen_model_bug_BugReport_task_WorkItem, gen_model_bug_BugReport_task_Checkable, gen_model_rationale_Assessment_UnicaseModelElement, gen_model_rationale_Assessment_NonDomainElement, gen_model_rationale_Comment_UnicaseModelElement, gen_model_rationale_Comment_NonDomainElement, gen_model_change_ModelChangePackage_UnicaseModelElement, gen_model_change_MergingIssue_Issue, gen_model_change_MergingProposal_Proposal, gen_model_component_DeploymentNode_UnicaseModelElement, gen_model_component_Component_UnicaseModelElement, gen_model_component_ComponentService_UnicaseModelElement, gen_model_meeting_MeetingSection_UnicaseModelElement, gen_model_meeting_Meeting_UnicaseModelElement, gen_model_attachment_FileAttachment_Attachment, gen_model_meeting_CompositeMeetingSection_MeetingSection, gen_model_meeting_IssueMeetingSection_MeetingSection, gen_model_meeting_WorkItemMeetingSection_MeetingSection, gen_model_state_Transition_UnicaseModelElement, gen_model_state_StateNode_UnicaseModelElement, gen_model_state_State_StateNode, gen_model_state_StateInitial_StateNode, gen_model_state_StateEnd_StateNode, gen_model_attachment_UrlAttachment_Attachment, gen_model_profile_StereotypeInstance_UnicaseModelElement, gen_model_profile_Profile_UnicaseModelElement, gen_model_profile_Stereotype_UnicaseModelElement, gen_model_profile_StereotypeAttribute_UnicaseModelElement, gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute, gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement, gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance, gen_model_activity_ActivityObject_UnicaseModelElement, gen_model_activity_Transition_UnicaseModelElement, gen_esmodel_ProjectId_UniqueIdentifier, gen_model_activity_Activity_ActivityObject, gen_model_activity_Fork_ActivityObject, gen_model_activity_Branch_ActivityObject, gen_model_activity_ActivityInitial_ActivityObject, gen_model_activity_ActivityEnd_ActivityObject, gen_esmodel_SessionId_UniqueIdentifier, gen_esmodel_FileIdentifier_IdentifiableElement, gen_esmodel_versioning_TagVersionSpec_VersionSpec, gen_esmodel_versioning_DateVersionSpec_VersionSpec, gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec, gen_esmodel_operations_FeatureOperation_AbstractOperation, gen_esmodel_versioning_HeadVersionSpec_VersionSpec, gen_esmodel_operations_AbstractOperation_IdentifiableElement, gen_esmodel_operations_CompositeOperation_AbstractOperation, gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation, gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation, gen_esmodel_operations_CreateDeleteOperation_AbstractOperation, gen_esmodel_operations_AttributeOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeOperation_FeatureOperation, gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation, gen_esmodel_operations_ReferenceOperation_FeatureOperation, gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation, gen_esmodel_operations_OperationId_UniqueIdentifier, gen_esmodel_events_PluginStartEvent_Event, gen_esmodel_events_UpdateEvent_Event, gen_esmodel_events_AnnotationEvent_Event, gen_esmodel_events_RevertEvent_Event, gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation, gen_esmodel_events_ReadEvent_Event, gen_esmodel_events_MergeEvent_Event, gen_esmodel_events_CheckoutEvent_Event, gen_esmodel_events_ExceptionEvent_Event, gen_esmodel_events_NavigatorCreateEvent_Event, gen_esmodel_events_PluginFocusEvent_Event, gen_esmodel_events_PresentationSwitchEvent_Event, gen_esmodel_events_ShowHistoryEvent_Event, gen_esmodel_events_PerspectiveEvent_Event, gen_esmodel_events_DNDEvent_Event, gen_esmodel_events_LinkEvent_Event, gen_esmodel_events_TraceEvent_Event, gen_esmodel_events_MergeChoiceEvent_Event, gen_esmodel_events_UndoEvent_Event, gen_esmodel_events_Validate_Event, gen_esmodel_events_ShowChangesEvent_Event, gen_esmodel_events_NotificationReadEvent_ReadEvent, gen_esmodel_events_NotificationGenerationEvent_Event, gen_esmodel_events_NotificationIgnoreEvent_Event, gen_esmodel_events_URLEvent_Event, gen_esmodel_accesscontrol_ACGroup_ACOrgUnit, gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier, gen_esmodel_events_MergeGlobalChoiceEvent_Event, gen_esmodel_server_ServerEvent_Event, gen_esmodel_server_ServerProjectEvent_ServerEvent, gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent, gen_esmodel_accesscontrol_ACUser_ACOrgUnit, gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement, gen_esmodel_roles_ReaderRole_Role, gen_esmodel_roles_WriterRole_Role, gen_esmodel_roles_ProjectAdminRole_Role, gen_esmodel_roles_ServerAdmin_Role, gen_esmodel_notification_ESNotification_IdentifiableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)