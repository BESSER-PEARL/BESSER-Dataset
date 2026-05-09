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
            EnumerationLiteral(name="CLASS_DIAGRAM"),
			EnumerationLiteral(name="USECASE_DIAGRAM"),
			EnumerationLiteral(name="COMPONENT_DIAGRAM"),
			EnumerationLiteral(name="STATE_DIAGRAM"),
			EnumerationLiteral(name="ACTIVITY_DIAGRAM"),
			EnumerationLiteral(name="WORKITEM_DIAGRAM")
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

BugStatus: Enumeration = Enumeration(
    name="BugStatus",
    literals={
            EnumerationLiteral(name="NEW"),
			EnumerationLiteral(name="CONFIRMED"),
			EnumerationLiteral(name="RESOLVED"),
			EnumerationLiteral(name="CLOSED"),
			EnumerationLiteral(name="ASSIGNED")
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
model_UnicaseModelElement = Class(name="model_UnicaseModelElement", is_abstract=True)
Annotation = Class(name="Annotation")
Attachment = Class(name="Attachment")
document_LeafSection = Class(name="document_LeafSection")
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
model_organization_OrgUnit = Class(name="model_organization_OrgUnit", is_abstract=True)
organization_Group = Class(name="organization_Group")
task_WorkItem = Class(name="task_WorkItem")
model_organization_User = Class(name="model_organization_User")
OrgUnit = Class(name="OrgUnit")
rationale_Comment = Class(name="rationale_Comment")
profile_StereotypeInstance = Class(name="profile_StereotypeInstance")
model_Annotation = Class(name="model_Annotation", is_abstract=True)
UnicaseModelElement = Class(name="UnicaseModelElement")
model_Attachment = Class(name="model_Attachment", is_abstract=True)
model_NonDomainElement = Class(name="model_NonDomainElement", is_abstract=True)
model_Project = Class(name="model_Project")
Project = Class(name="Project")
change_ModelChangePackage = Class(name="change_ModelChangePackage")
model_task_WorkPackage = Class(name="model_task_WorkPackage")
WorkItem = Class(name="WorkItem")
model_organization_Group = Class(name="model_organization_Group")
organization_OrgUnit = Class(name="organization_OrgUnit")
model_task_WorkItem = Class(name="model_task_WorkItem", is_abstract=True)
task_WorkPackage = Class(name="task_WorkPackage")
organization_User = Class(name="organization_User")
task_Checkable = Class(name="task_Checkable")
model_diagram_MEDiagram = Class(name="model_diagram_MEDiagram")
diagram_model_Diagram = Class(name="diagram_model_Diagram")
model_task_Milestone = Class(name="model_task_Milestone")
model_task_Checkable = Class(name="model_task_Checkable", is_abstract=True)
model_task_ActionItem = Class(name="model_task_ActionItem")
classes_Class = Class(name="classes_Class")
classes_Association = Class(name="classes_Association")
classes_Attribute = Class(name="classes_Attribute")
classes_Method = Class(name="classes_Method")
requirement_UseCase = Class(name="requirement_UseCase")
model_classes_PackageElement = Class(name="model_classes_PackageElement", is_abstract=True)
requirement_Scenario = Class(name="requirement_Scenario")
classes_Package = Class(name="classes_Package")
classes_Dependency = Class(name="classes_Dependency")
model_classes_Class = Class(name="model_classes_Class")
PackageElement = Class(name="PackageElement")
model_classes_Attribute = Class(name="model_classes_Attribute")
model_classes_Package = Class(name="model_classes_Package")
classes_PackageElement = Class(name="classes_PackageElement")
model_classes_Association = Class(name="model_classes_Association")
model_classes_Method = Class(name="model_classes_Method")
model_classes_MethodArgument = Class(name="model_classes_MethodArgument")
model_classes_Dependency = Class(name="model_classes_Dependency")
classes_MethodArgument = Class(name="classes_MethodArgument")
model_document_CompositeSection = Class(name="model_document_CompositeSection")
document_Section = Class(name="document_Section")
model_requirement_FunctionalRequirement = Class(name="model_requirement_FunctionalRequirement")
requirement_FunctionalRequirement = Class(name="requirement_FunctionalRequirement")
model_document_Section = Class(name="model_document_Section", is_abstract=True)
document_CompositeSection = Class(name="document_CompositeSection")
model_document_LeafSection = Class(name="model_document_LeafSection")
Section = Class(name="Section")
model_requirement_UseCase = Class(name="model_requirement_UseCase")
requirement_Actor = Class(name="requirement_Actor")
requirement_NonFunctionalRequirement = Class(name="requirement_NonFunctionalRequirement")
model_requirement_Scenario = Class(name="model_requirement_Scenario")
requirement_Step = Class(name="requirement_Step")
requirement_UserTask = Class(name="requirement_UserTask")
model_requirement_Actor = Class(name="model_requirement_Actor")
model_requirement_ActorInstance = Class(name="model_requirement_ActorInstance")
requirement_ActorInstance = Class(name="requirement_ActorInstance")
model_requirement_Step = Class(name="model_requirement_Step")
NonDomainElement = Class(name="NonDomainElement")
requirement_SystemFunction = Class(name="requirement_SystemFunction")
model_requirement_SystemFunction = Class(name="model_requirement_SystemFunction")
model_requirement_UserTask = Class(name="model_requirement_UserTask")
model_requirement_NonFunctionalRequirement = Class(name="model_requirement_NonFunctionalRequirement")
Criterion = Class(name="Criterion")
model_rationale_Issue = Class(name="model_rationale_Issue")
rationale_Solution = Class(name="rationale_Solution")
rationale_Criterion = Class(name="rationale_Criterion")
model_rationale_Proposal = Class(name="model_rationale_Proposal")
rationale_Issue = Class(name="rationale_Issue")
rationale_Assessment = Class(name="rationale_Assessment")
model_rationale_Solution = Class(name="model_rationale_Solution")
model_rationale_Criterion = Class(name="model_rationale_Criterion")
model_rationale_Assessment = Class(name="model_rationale_Assessment")
rationale_Proposal = Class(name="rationale_Proposal")
model_rationale_Comment = Class(name="model_rationale_Comment")
model_change_ModelChangePackage = Class(name="model_change_ModelChangePackage")
model_change_MergingIssue = Class(name="model_change_MergingIssue")
Issue = Class(name="Issue")
model_change_MergingProposal = Class(name="model_change_MergingProposal")
Proposal = Class(name="Proposal")
change_MergingProposal = Class(name="change_MergingProposal")
model_change_MergingSolution = Class(name="model_change_MergingSolution")
Solution = Class(name="Solution")
model_bug_BugReport = Class(name="model_bug_BugReport")
model_component_Component = Class(name="model_component_Component")
component_ComponentService = Class(name="component_ComponentService")
model_component_ComponentService = Class(name="model_component_ComponentService")
component_Component = Class(name="component_Component")
model_component_DeploymentNode = Class(name="model_component_DeploymentNode")
model_meeting_Meeting = Class(name="model_meeting_Meeting")
meeting_MeetingSection = Class(name="meeting_MeetingSection")
meeting_IssueMeetingSection = Class(name="meeting_IssueMeetingSection")
meeting_WorkItemMeetingSection = Class(name="meeting_WorkItemMeetingSection")
model_meeting_MeetingSection = Class(name="model_meeting_MeetingSection", is_abstract=True)
model_meeting_CompositeMeetingSection = Class(name="model_meeting_CompositeMeetingSection")
MeetingSection = Class(name="MeetingSection")
model_meeting_IssueMeetingSection = Class(name="model_meeting_IssueMeetingSection")
model_state_Transition = Class(name="model_state_Transition")
state_StateNode = Class(name="state_StateNode")
model_state_StateNode = Class(name="model_state_StateNode", is_abstract=True)
state_Transition = Class(name="state_Transition")
model_state_State = Class(name="model_state_State")
StateNode = Class(name="StateNode")
model_state_StateInitial = Class(name="model_state_StateInitial")
model_state_StateEnd = Class(name="model_state_StateEnd")
model_attachment_UrlAttachment = Class(name="model_attachment_UrlAttachment")
model_attachment_FileAttachment = Class(name="model_attachment_FileAttachment")
model_meeting_WorkItemMeetingSection = Class(name="model_meeting_WorkItemMeetingSection")
profile_Stereotype = Class(name="profile_Stereotype")
model_profile_Stereotype = Class(name="model_profile_Stereotype")
profile_Profile = Class(name="profile_Profile")
profile_StereotypeAttribute = Class(name="profile_StereotypeAttribute")
model_profile_StereotypeInstance = Class(name="model_profile_StereotypeInstance")
profile_StereotypeAttributeInstance = Class(name="profile_StereotypeAttributeInstance")
model_profile_StereotypeAttribute = Class(name="model_profile_StereotypeAttribute", is_abstract=True)
model_profile_StereotypeAttributeSimple = Class(name="model_profile_StereotypeAttributeSimple")
StereotypeAttribute = Class(name="StereotypeAttribute")
model_profile_StereotypeAttributeInstance = Class(name="model_profile_StereotypeAttributeInstance", is_abstract=True)
model_profile_Profile = Class(name="model_profile_Profile")
model_profile_StereotypeAttributeInstanceString = Class(name="model_profile_StereotypeAttributeInstanceString")
StereotypeAttributeInstance = Class(name="StereotypeAttributeInstance")
model_util_ModelElementPath = Class(name="model_util_ModelElementPath")
ModelElementId = Class(name="ModelElementId")
model_activity_ActivityObject = Class(name="model_activity_ActivityObject", is_abstract=True)
activity_Transition = Class(name="activity_Transition")
model_activity_Transition = Class(name="model_activity_Transition")
activity_ActivityObject = Class(name="activity_ActivityObject")
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
esmodel_ProjectId = Class(name="esmodel_ProjectId")
esmodel_VersionInfo = Class(name="esmodel_VersionInfo")
esmodel_ClientVersionInfo = Class(name="esmodel_ClientVersionInfo")
esmodel_versioning_TagVersionSpec = Class(name="esmodel_versioning_TagVersionSpec")
VersionSpec = Class(name="VersionSpec")
esmodel_versioning_DateVersionSpec = Class(name="esmodel_versioning_DateVersionSpec")
esmodel_versioning_PrimaryVersionSpec = Class(name="esmodel_versioning_PrimaryVersionSpec")
esmodel_versioning_ChangePackage = Class(name="esmodel_versioning_ChangePackage")
operations_AbstractOperation = Class(name="operations_AbstractOperation")
events_Event = Class(name="events_Event")
versioning_LogMessage = Class(name="versioning_LogMessage")
notification_ESNotification = Class(name="notification_ESNotification")
versioning_VersionProperty = Class(name="versioning_VersionProperty")
esmodel_versioning_HistoryInfo = Class(name="esmodel_versioning_HistoryInfo")
versioning_TagVersionSpec = Class(name="versioning_TagVersionSpec")
versioning_ChangePackage = Class(name="versioning_ChangePackage")
esmodel_versioning_HistoryQuery = Class(name="esmodel_versioning_HistoryQuery")
esmodel_versioning_Version = Class(name="esmodel_versioning_Version")
esmodel_versioning_HeadVersionSpec = Class(name="esmodel_versioning_HeadVersionSpec")
esmodel_versioning_VersionSpec = Class(name="esmodel_versioning_VersionSpec", is_abstract=True)
esmodel_versioning_VersionProperty = Class(name="esmodel_versioning_VersionProperty")
esmodel_versioning_LogMessage = Class(name="esmodel_versioning_LogMessage")
esmodel_operations_AbstractOperation = Class(name="esmodel_operations_AbstractOperation", is_abstract=True)
esmodel_operations_CompositeOperation = Class(name="esmodel_operations_CompositeOperation")
AbstractOperation = Class(name="AbstractOperation")
esmodel_operations_FeatureOperation = Class(name="esmodel_operations_FeatureOperation", is_abstract=True)
esmodel_operations_CreateDeleteOperation = Class(name="esmodel_operations_CreateDeleteOperation")
operations_esmodel_EObject = Class(name="operations_esmodel_EObject")
operations_ReferenceOperation = Class(name="operations_ReferenceOperation")
operations_EObjectToModelElementIdMap = Class(name="operations_EObjectToModelElementIdMap")
esmodel_operations_AttributeOperation = Class(name="esmodel_operations_AttributeOperation")
FeatureOperation = Class(name="FeatureOperation")
esmodel_operations_MultiAttributeOperation = Class(name="esmodel_operations_MultiAttributeOperation")
esmodel_operations_MultiAttributeMoveOperation = Class(name="esmodel_operations_MultiAttributeMoveOperation")
esmodel_operations_SingleReferenceOperation = Class(name="esmodel_operations_SingleReferenceOperation")
ReferenceOperation = Class(name="ReferenceOperation")
esmodel_operations_MultiReferenceSetOperation = Class(name="esmodel_operations_MultiReferenceSetOperation")
esmodel_operations_MultiReferenceOperation = Class(name="esmodel_operations_MultiReferenceOperation")
esmodel_operations_MultiReferenceMoveOperation = Class(name="esmodel_operations_MultiReferenceMoveOperation")
esmodel_operations_ReferenceOperation = Class(name="esmodel_operations_ReferenceOperation", is_abstract=True)
esmodel_operations_DiagramLayoutOperation = Class(name="esmodel_operations_DiagramLayoutOperation")
AttributeOperation = Class(name="AttributeOperation")
esmodel_operations_OperationId = Class(name="esmodel_operations_OperationId")
esmodel_operations_OperationGroup = Class(name="esmodel_operations_OperationGroup")
esmodel_operations_MultiAttributeSetOperation = Class(name="esmodel_operations_MultiAttributeSetOperation")
esmodel_operations_EObjectToModelElementIdMap = Class(name="esmodel_operations_EObjectToModelElementIdMap")
esmodel_semantic_SemanticCompositeOperation = Class(name="esmodel_semantic_SemanticCompositeOperation", is_abstract=True)
CompositeOperation = Class(name="CompositeOperation")
esmodel_events_Event = Class(name="esmodel_events_Event")
esmodel_events_ReadEvent = Class(name="esmodel_events_ReadEvent")
Event = Class(name="Event")
esmodel_events_MergeEvent = Class(name="esmodel_events_MergeEvent")
esmodel_events_CheckoutEvent = Class(name="esmodel_events_CheckoutEvent")
esmodel_events_ExceptionEvent = Class(name="esmodel_events_ExceptionEvent")
esmodel_events_PluginStartEvent = Class(name="esmodel_events_PluginStartEvent")
esmodel_operations_ModelElementGroup = Class(name="esmodel_operations_ModelElementGroup")
esmodel_events_AnnotationEvent = Class(name="esmodel_events_AnnotationEvent")
esmodel_events_RevertEvent = Class(name="esmodel_events_RevertEvent")
esmodel_events_UpdateEvent = Class(name="esmodel_events_UpdateEvent")
esmodel_events_ShowHistoryEvent = Class(name="esmodel_events_ShowHistoryEvent")
esmodel_events_PerspectiveEvent = Class(name="esmodel_events_PerspectiveEvent")
esmodel_events_DNDEvent = Class(name="esmodel_events_DNDEvent")
esmodel_events_LinkEvent = Class(name="esmodel_events_LinkEvent")
esmodel_events_TraceEvent = Class(name="esmodel_events_TraceEvent")
esmodel_events_NavigatorCreateEvent = Class(name="esmodel_events_NavigatorCreateEvent")
esmodel_events_PluginFocusEvent = Class(name="esmodel_events_PluginFocusEvent")
esmodel_events_PresentationSwitchEvent = Class(name="esmodel_events_PresentationSwitchEvent")
esmodel_events_UndoEvent = Class(name="esmodel_events_UndoEvent")
esmodel_events_Validate = Class(name="esmodel_events_Validate")
esmodel_events_ShowChangesEvent = Class(name="esmodel_events_ShowChangesEvent")
esmodel_events_NotificationReadEvent = Class(name="esmodel_events_NotificationReadEvent")
ReadEvent = Class(name="ReadEvent")
esmodel_events_NotificationGenerationEvent = Class(name="esmodel_events_NotificationGenerationEvent")
esmodel_server_ServerEvent = Class(name="esmodel_server_ServerEvent", is_abstract=True)
esmodel_events_NotificationIgnoreEvent = Class(name="esmodel_events_NotificationIgnoreEvent")
esmodel_server_ServerProjectEvent = Class(name="esmodel_server_ServerProjectEvent", is_abstract=True)
ServerEvent = Class(name="ServerEvent")
esmodel_events_URLEvent = Class(name="esmodel_events_URLEvent")
esmodel_server_ProjectUpdatedEvent = Class(name="esmodel_server_ProjectUpdatedEvent")
ServerProjectEvent = Class(name="ServerProjectEvent")
esmodel_accesscontrol_ACUser = Class(name="esmodel_accesscontrol_ACUser")
ACOrgUnit = Class(name="ACOrgUnit")
esmodel_events_MergeChoiceEvent = Class(name="esmodel_events_MergeChoiceEvent")
operations_OperationId = Class(name="operations_OperationId")
esmodel_accesscontrol_ACOrgUnit = Class(name="esmodel_accesscontrol_ACOrgUnit")
esmodel_events_MergeGlobalChoiceEvent = Class(name="esmodel_events_MergeGlobalChoiceEvent")
esmodel_roles_Role = Class(name="esmodel_roles_Role", is_abstract=True)
esmodel_roles_ReaderRole = Class(name="esmodel_roles_ReaderRole")
Role = Class(name="Role")
esmodel_roles_WriterRole = Class(name="esmodel_roles_WriterRole")
roles_Role = Class(name="roles_Role")
accesscontrol_OrgUnitProperty = Class(name="accesscontrol_OrgUnitProperty")
esmodel_accesscontrol_ACGroup = Class(name="esmodel_accesscontrol_ACGroup")
accesscontrol_ACOrgUnit = Class(name="accesscontrol_ACOrgUnit")
esmodel_accesscontrol_ACOrgUnitId = Class(name="esmodel_accesscontrol_ACOrgUnitId")
esmodel_accesscontrol_OrgUnitProperty = Class(name="esmodel_accesscontrol_OrgUnitProperty")
esmodel_url_ServerUrl = Class(name="esmodel_url_ServerUrl")
esmodel_url_ProjectUrlFragment = Class(name="esmodel_url_ProjectUrlFragment")
esmodel_url_ModelElementUrlFragment = Class(name="esmodel_url_ModelElementUrlFragment")
esmodel_roles_ProjectAdminRole = Class(name="esmodel_roles_ProjectAdminRole")
esmodel_roles_ServerAdmin = Class(name="esmodel_roles_ServerAdmin")
esmodel_notification_ESNotification = Class(name="esmodel_notification_ESNotification")
esmodel_url_ModelElementUrl = Class(name="esmodel_url_ModelElementUrl")
url_ServerUrl = Class(name="url_ServerUrl")
url_ProjectUrlFragment = Class(name="url_ProjectUrlFragment")
url_ModelElementUrlFragment = Class(name="url_ModelElementUrlFragment")

# model_UnicaseModelElement class attributes and methods
model_UnicaseModelElement_name: Property = Property(name="name", type=StringType)
model_UnicaseModelElement_description: Property = Property(name="description", type=StringType)
model_UnicaseModelElement_state: Property = Property(name="state", type=StringType)
model_UnicaseModelElement.attributes={model_UnicaseModelElement_state, model_UnicaseModelElement_description, model_UnicaseModelElement_name}

# Annotation class attributes and methods

# Attachment class attributes and methods

# document_LeafSection class attributes and methods

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
metamodel_ModelElement.attributes={metamodel_ModelElement_creationDate, metamodel_ModelElement_creator}

# IdentifiableElement class attributes and methods

# metamodel_ModelElementId class attributes and methods

# UniqueIdentifier class attributes and methods

# metamodel_ModelVersion class attributes and methods
metamodel_ModelVersion_releaseNumber: Property = Property(name="releaseNumber", type=IntegerType)
metamodel_ModelVersion.attributes={metamodel_ModelVersion_releaseNumber}

# metamodel_NonDomainElement class attributes and methods

# metamodel_AssociationClassElement class attributes and methods

# model_organization_OrgUnit class attributes and methods
model_organization_OrgUnit_acOrgId: Property = Property(name="acOrgId", type=StringType)
model_organization_OrgUnit.attributes={model_organization_OrgUnit_acOrgId}

# organization_Group class attributes and methods

# task_WorkItem class attributes and methods

# model_organization_User class attributes and methods
model_organization_User_email: Property = Property(name="email", type=StringType)
model_organization_User_firstName: Property = Property(name="firstName", type=StringType)
model_organization_User_lastName: Property = Property(name="lastName", type=StringType)
model_organization_User.attributes={model_organization_User_firstName, model_organization_User_lastName, model_organization_User_email}

# OrgUnit class attributes and methods

# rationale_Comment class attributes and methods

# profile_StereotypeInstance class attributes and methods

# model_Annotation class attributes and methods

# UnicaseModelElement class attributes and methods

# model_Attachment class attributes and methods

# model_NonDomainElement class attributes and methods

# model_Project class attributes and methods

# Project class attributes and methods

# change_ModelChangePackage class attributes and methods

# model_task_WorkPackage class attributes and methods
model_task_WorkPackage_startDate: Property = Property(name="startDate", type=DateType)
model_task_WorkPackage_endDate: Property = Property(name="endDate", type=DateType)
model_task_WorkPackage.attributes={model_task_WorkPackage_startDate, model_task_WorkPackage_endDate}

# WorkItem class attributes and methods

# model_organization_Group class attributes and methods

# organization_OrgUnit class attributes and methods

# model_task_WorkItem class attributes and methods
model_task_WorkItem_dueDate: Property = Property(name="dueDate", type=DateType)
model_task_WorkItem_estimate: Property = Property(name="estimate", type=IntegerType)
model_task_WorkItem_effort: Property = Property(name="effort", type=IntegerType)
model_task_WorkItem_priority: Property = Property(name="priority", type=IntegerType)
model_task_WorkItem_resolved: Property = Property(name="resolved", type=BooleanType)
model_task_WorkItem.attributes={model_task_WorkItem_effort, model_task_WorkItem_resolved, model_task_WorkItem_priority, model_task_WorkItem_estimate, model_task_WorkItem_dueDate}

# task_WorkPackage class attributes and methods

# organization_User class attributes and methods

# task_Checkable class attributes and methods

# model_diagram_MEDiagram class attributes and methods
model_diagram_MEDiagram_diagramLayout: Property = Property(name="diagramLayout", type=StringType)
model_diagram_MEDiagram_type: Property = Property(name="type", type=StringType)
model_diagram_MEDiagram.attributes={model_diagram_MEDiagram_diagramLayout, model_diagram_MEDiagram_type}

# diagram_model_Diagram class attributes and methods

# model_task_Milestone class attributes and methods

# model_task_Checkable class attributes and methods
model_task_Checkable_checked: Property = Property(name="checked", type=BooleanType)
model_task_Checkable.attributes={model_task_Checkable_checked}

# model_task_ActionItem class attributes and methods
model_task_ActionItem_done: Property = Property(name="done", type=BooleanType)
model_task_ActionItem_activity: Property = Property(name="activity", type=StringType)
model_task_ActionItem.attributes={model_task_ActionItem_done, model_task_ActionItem_activity}

# classes_Class class attributes and methods

# classes_Association class attributes and methods

# classes_Attribute class attributes and methods

# classes_Method class attributes and methods

# requirement_UseCase class attributes and methods

# model_classes_PackageElement class attributes and methods

# requirement_Scenario class attributes and methods

# classes_Package class attributes and methods

# classes_Dependency class attributes and methods

# model_classes_Class class attributes and methods

# PackageElement class attributes and methods

# model_classes_Attribute class attributes and methods
model_classes_Attribute_signature: Property = Property(name="signature", type=StringType)
model_classes_Attribute_type: Property = Property(name="type", type=StringType)
model_classes_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_Attribute_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Attribute_scope: Property = Property(name="scope", type=StringType)
model_classes_Attribute_properties: Property = Property(name="properties", type=StringType)
model_classes_Attribute_label: Property = Property(name="label", type=StringType)
model_classes_Attribute.attributes={model_classes_Attribute_label, model_classes_Attribute_defaultValue, model_classes_Attribute_scope, model_classes_Attribute_type, model_classes_Attribute_signature, model_classes_Attribute_properties, model_classes_Attribute_visibility}

# model_classes_Package class attributes and methods

# classes_PackageElement class attributes and methods

# model_classes_Association class attributes and methods
model_classes_Association_sourceMultiplicity: Property = Property(name="sourceMultiplicity", type=StringType)
model_classes_Association_targetMultiplicity: Property = Property(name="targetMultiplicity", type=StringType)
model_classes_Association_sourceRole: Property = Property(name="sourceRole", type=StringType)
model_classes_Association_targetRole: Property = Property(name="targetRole", type=StringType)
model_classes_Association_type: Property = Property(name="type", type=StringType)
model_classes_Association.attributes={model_classes_Association_sourceMultiplicity, model_classes_Association_targetRole, model_classes_Association_type, model_classes_Association_targetMultiplicity, model_classes_Association_sourceRole}

# model_classes_Method class attributes and methods
model_classes_Method_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Method_scope: Property = Property(name="scope", type=StringType)
model_classes_Method_returnType: Property = Property(name="returnType", type=StringType)
model_classes_Method_signature: Property = Property(name="signature", type=StringType)
model_classes_Method_properties: Property = Property(name="properties", type=StringType)
model_classes_Method_label: Property = Property(name="label", type=StringType)
model_classes_Method_stubbed: Property = Property(name="stubbed", type=BooleanType)
model_classes_Method.attributes={model_classes_Method_properties, model_classes_Method_signature, model_classes_Method_returnType, model_classes_Method_visibility, model_classes_Method_scope, model_classes_Method_label, model_classes_Method_stubbed}

# model_classes_MethodArgument class attributes and methods
model_classes_MethodArgument_type: Property = Property(name="type", type=StringType)
model_classes_MethodArgument_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_MethodArgument_signature: Property = Property(name="signature", type=StringType)
model_classes_MethodArgument_label: Property = Property(name="label", type=StringType)
model_classes_MethodArgument_direction: Property = Property(name="direction", type=StringType)
model_classes_MethodArgument.attributes={model_classes_MethodArgument_type, model_classes_MethodArgument_signature, model_classes_MethodArgument_direction, model_classes_MethodArgument_defaultValue, model_classes_MethodArgument_label}

# model_classes_Dependency class attributes and methods

# classes_MethodArgument class attributes and methods

# model_document_CompositeSection class attributes and methods

# document_Section class attributes and methods

# model_requirement_FunctionalRequirement class attributes and methods
model_requirement_FunctionalRequirement_storyPoints: Property = Property(name="storyPoints", type=IntegerType)
model_requirement_FunctionalRequirement_priority: Property = Property(name="priority", type=IntegerType)
model_requirement_FunctionalRequirement_reviewed: Property = Property(name="reviewed", type=BooleanType)
model_requirement_FunctionalRequirement_cost: Property = Property(name="cost", type=IntegerType)
model_requirement_FunctionalRequirement.attributes={model_requirement_FunctionalRequirement_priority, model_requirement_FunctionalRequirement_reviewed, model_requirement_FunctionalRequirement_cost, model_requirement_FunctionalRequirement_storyPoints}

# requirement_FunctionalRequirement class attributes and methods

# model_document_Section class attributes and methods

# document_CompositeSection class attributes and methods

# model_document_LeafSection class attributes and methods

# Section class attributes and methods

# model_requirement_UseCase class attributes and methods
model_requirement_UseCase_precondition: Property = Property(name="precondition", type=StringType)
model_requirement_UseCase_postcondition: Property = Property(name="postcondition", type=StringType)
model_requirement_UseCase_rules: Property = Property(name="rules", type=StringType)
model_requirement_UseCase_exception: Property = Property(name="exception", type=StringType)
model_requirement_UseCase.attributes={model_requirement_UseCase_exception, model_requirement_UseCase_rules, model_requirement_UseCase_postcondition, model_requirement_UseCase_precondition}

# requirement_Actor class attributes and methods

# requirement_NonFunctionalRequirement class attributes and methods

# model_requirement_Scenario class attributes and methods

# requirement_Step class attributes and methods

# requirement_UserTask class attributes and methods

# model_requirement_Actor class attributes and methods

# model_requirement_ActorInstance class attributes and methods

# requirement_ActorInstance class attributes and methods

# model_requirement_Step class attributes and methods
model_requirement_Step_userStep: Property = Property(name="userStep", type=BooleanType)
model_requirement_Step.attributes={model_requirement_Step_userStep}

# NonDomainElement class attributes and methods

# requirement_SystemFunction class attributes and methods

# model_requirement_SystemFunction class attributes and methods
model_requirement_SystemFunction_input: Property = Property(name="input", type=StringType)
model_requirement_SystemFunction_output: Property = Property(name="output", type=StringType)
model_requirement_SystemFunction_exception: Property = Property(name="exception", type=StringType)
model_requirement_SystemFunction.attributes={model_requirement_SystemFunction_output, model_requirement_SystemFunction_input, model_requirement_SystemFunction_exception}

# model_requirement_UserTask class attributes and methods

# model_requirement_NonFunctionalRequirement class attributes and methods

# Criterion class attributes and methods

# model_rationale_Issue class attributes and methods
model_rationale_Issue_activity: Property = Property(name="activity", type=StringType)
model_rationale_Issue.attributes={model_rationale_Issue_activity}

# rationale_Solution class attributes and methods

# rationale_Criterion class attributes and methods

# model_rationale_Proposal class attributes and methods

# rationale_Issue class attributes and methods

# rationale_Assessment class attributes and methods

# model_rationale_Solution class attributes and methods

# model_rationale_Criterion class attributes and methods

# model_rationale_Assessment class attributes and methods
model_rationale_Assessment_value: Property = Property(name="value", type=IntegerType)
model_rationale_Assessment.attributes={model_rationale_Assessment_value}

# rationale_Proposal class attributes and methods

# model_rationale_Comment class attributes and methods

# model_change_ModelChangePackage class attributes and methods
model_change_ModelChangePackage_sourceVersion: Property = Property(name="sourceVersion", type=IntegerType)
model_change_ModelChangePackage_targetVersion: Property = Property(name="targetVersion", type=IntegerType)
model_change_ModelChangePackage.attributes={model_change_ModelChangePackage_sourceVersion, model_change_ModelChangePackage_targetVersion}

# model_change_MergingIssue class attributes and methods
model_change_MergingIssue_resolvingRevision: Property = Property(name="resolvingRevision", type=IntegerType)
model_change_MergingIssue.attributes={model_change_MergingIssue_resolvingRevision}

# Issue class attributes and methods

# model_change_MergingProposal class attributes and methods

# Proposal class attributes and methods

# change_MergingProposal class attributes and methods

# model_change_MergingSolution class attributes and methods

# Solution class attributes and methods

# model_bug_BugReport class attributes and methods
model_bug_BugReport_resolution: Property = Property(name="resolution", type=StringType)
model_bug_BugReport_Status: Property = Property(name="Status", type=StringType)
model_bug_BugReport_severity: Property = Property(name="severity", type=StringType)
model_bug_BugReport_resolutionType: Property = Property(name="resolutionType", type=StringType)
model_bug_BugReport.attributes={model_bug_BugReport_resolutionType, model_bug_BugReport_severity, model_bug_BugReport_Status, model_bug_BugReport_resolution}

# model_component_Component class attributes and methods

# component_ComponentService class attributes and methods

# model_component_ComponentService class attributes and methods

# component_Component class attributes and methods

# model_component_DeploymentNode class attributes and methods

# model_meeting_Meeting class attributes and methods
model_meeting_Meeting_location: Property = Property(name="location", type=StringType)
model_meeting_Meeting_starttime: Property = Property(name="starttime", type=DateType)
model_meeting_Meeting_endtime: Property = Property(name="endtime", type=DateType)
model_meeting_Meeting.attributes={model_meeting_Meeting_starttime, model_meeting_Meeting_endtime, model_meeting_Meeting_location}

# meeting_MeetingSection class attributes and methods

# meeting_IssueMeetingSection class attributes and methods

# meeting_WorkItemMeetingSection class attributes and methods

# model_meeting_MeetingSection class attributes and methods
model_meeting_MeetingSection_allocatedTime: Property = Property(name="allocatedTime", type=IntegerType)
model_meeting_MeetingSection.attributes={model_meeting_MeetingSection_allocatedTime}

# model_meeting_CompositeMeetingSection class attributes and methods

# MeetingSection class attributes and methods

# model_meeting_IssueMeetingSection class attributes and methods

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
model_state_State.attributes={model_state_State_activities, model_state_State_exitConditions, model_state_State_entryConditions}

# StateNode class attributes and methods

# model_state_StateInitial class attributes and methods

# model_state_StateEnd class attributes and methods

# model_attachment_UrlAttachment class attributes and methods
model_attachment_UrlAttachment_url: Property = Property(name="url", type=StringType)
model_attachment_UrlAttachment.attributes={model_attachment_UrlAttachment_url}

# model_attachment_FileAttachment class attributes and methods
model_attachment_FileAttachment_fileName: Property = Property(name="fileName", type=StringType)
model_attachment_FileAttachment_fileHash: Property = Property(name="fileHash", type=StringType)
model_attachment_FileAttachment_fileID: Property = Property(name="fileID", type=StringType)
model_attachment_FileAttachment_fileSize: Property = Property(name="fileSize", type=StringType)
model_attachment_FileAttachment.attributes={model_attachment_FileAttachment_fileName, model_attachment_FileAttachment_fileID, model_attachment_FileAttachment_fileSize, model_attachment_FileAttachment_fileHash}

# model_meeting_WorkItemMeetingSection class attributes and methods

# profile_Stereotype class attributes and methods

# model_profile_Stereotype class attributes and methods
model_profile_Stereotype_required: Property = Property(name="required", type=BooleanType)
model_profile_Stereotype.attributes={model_profile_Stereotype_required}

# profile_Profile class attributes and methods

# profile_StereotypeAttribute class attributes and methods

# model_profile_StereotypeInstance class attributes and methods

# profile_StereotypeAttributeInstance class attributes and methods

# model_profile_StereotypeAttribute class attributes and methods

# model_profile_StereotypeAttributeSimple class attributes and methods
model_profile_StereotypeAttributeSimple_type: Property = Property(name="type", type=StringType)
model_profile_StereotypeAttributeSimple.attributes={model_profile_StereotypeAttributeSimple_type}

# StereotypeAttribute class attributes and methods

# model_profile_StereotypeAttributeInstance class attributes and methods

# model_profile_Profile class attributes and methods

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
esmodel_ProjectInfo.attributes={esmodel_ProjectInfo_name, esmodel_ProjectInfo_description}

# versioning_PrimaryVersionSpec class attributes and methods

# esmodel_SessionId class attributes and methods

# esmodel_ServerSpace class attributes and methods

# accesscontrol_ACGroup class attributes and methods

# ProjectHistory class attributes and methods

# SessionId class attributes and methods

# accesscontrol_ACUser class attributes and methods

# esmodel_ProjectId class attributes and methods

# esmodel_VersionInfo class attributes and methods
esmodel_VersionInfo_emfStoreVersionString: Property = Property(name="emfStoreVersionString", type=StringType)
esmodel_VersionInfo.attributes={esmodel_VersionInfo_emfStoreVersionString}

# esmodel_ClientVersionInfo class attributes and methods
esmodel_ClientVersionInfo_version: Property = Property(name="version", type=StringType)
esmodel_ClientVersionInfo_name: Property = Property(name="name", type=StringType)
esmodel_ClientVersionInfo.attributes={esmodel_ClientVersionInfo_version, esmodel_ClientVersionInfo_name}

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

# esmodel_versioning_ChangePackage class attributes and methods

# operations_AbstractOperation class attributes and methods

# events_Event class attributes and methods

# versioning_LogMessage class attributes and methods

# notification_ESNotification class attributes and methods

# versioning_VersionProperty class attributes and methods

# esmodel_versioning_HistoryInfo class attributes and methods

# versioning_TagVersionSpec class attributes and methods

# versioning_ChangePackage class attributes and methods

# esmodel_versioning_HistoryQuery class attributes and methods
esmodel_versioning_HistoryQuery_includeChangePackage: Property = Property(name="includeChangePackage", type=BooleanType)
esmodel_versioning_HistoryQuery.attributes={esmodel_versioning_HistoryQuery_includeChangePackage}

# esmodel_versioning_Version class attributes and methods

# esmodel_versioning_HeadVersionSpec class attributes and methods

# esmodel_versioning_VersionSpec class attributes and methods

# esmodel_versioning_VersionProperty class attributes and methods
esmodel_versioning_VersionProperty_name: Property = Property(name="name", type=StringType)
esmodel_versioning_VersionProperty_value: Property = Property(name="value", type=StringType)
esmodel_versioning_VersionProperty.attributes={esmodel_versioning_VersionProperty_name, esmodel_versioning_VersionProperty_value}

# esmodel_versioning_LogMessage class attributes and methods
esmodel_versioning_LogMessage_date: Property = Property(name="date", type=DateType)
esmodel_versioning_LogMessage_clientDate: Property = Property(name="clientDate", type=DateType)
esmodel_versioning_LogMessage_author: Property = Property(name="author", type=StringType)
esmodel_versioning_LogMessage_message: Property = Property(name="message", type=StringType)
esmodel_versioning_LogMessage.attributes={esmodel_versioning_LogMessage_clientDate, esmodel_versioning_LogMessage_date, esmodel_versioning_LogMessage_message, esmodel_versioning_LogMessage_author}

# esmodel_operations_AbstractOperation class attributes and methods
esmodel_operations_AbstractOperation_name: Property = Property(name="name", type=StringType)
esmodel_operations_AbstractOperation_description: Property = Property(name="description", type=StringType)
esmodel_operations_AbstractOperation_accepted: Property = Property(name="accepted", type=BooleanType)
esmodel_operations_AbstractOperation_clientDate: Property = Property(name="clientDate", type=DateType)
esmodel_operations_AbstractOperation.attributes={esmodel_operations_AbstractOperation_clientDate, esmodel_operations_AbstractOperation_name, esmodel_operations_AbstractOperation_description, esmodel_operations_AbstractOperation_accepted}

# esmodel_operations_CompositeOperation class attributes and methods
esmodel_operations_CompositeOperation_compositeName: Property = Property(name="compositeName", type=StringType)
esmodel_operations_CompositeOperation_compositeDescription: Property = Property(name="compositeDescription", type=StringType)
esmodel_operations_CompositeOperation_reversed: Property = Property(name="reversed", type=BooleanType)
esmodel_operations_CompositeOperation.attributes={esmodel_operations_CompositeOperation_reversed, esmodel_operations_CompositeOperation_compositeName, esmodel_operations_CompositeOperation_compositeDescription}

# AbstractOperation class attributes and methods

# esmodel_operations_FeatureOperation class attributes and methods
esmodel_operations_FeatureOperation_featureName: Property = Property(name="featureName", type=StringType)
esmodel_operations_FeatureOperation.attributes={esmodel_operations_FeatureOperation_featureName}

# esmodel_operations_CreateDeleteOperation class attributes and methods
esmodel_operations_CreateDeleteOperation_delete: Property = Property(name="delete", type=BooleanType)
esmodel_operations_CreateDeleteOperation.attributes={esmodel_operations_CreateDeleteOperation_delete}

# operations_esmodel_EObject class attributes and methods

# operations_ReferenceOperation class attributes and methods

# operations_EObjectToModelElementIdMap class attributes and methods

# esmodel_operations_AttributeOperation class attributes and methods
esmodel_operations_AttributeOperation_oldValue: Property = Property(name="oldValue", type=StringType)
esmodel_operations_AttributeOperation_newValue: Property = Property(name="newValue", type=StringType)
esmodel_operations_AttributeOperation.attributes={esmodel_operations_AttributeOperation_oldValue, esmodel_operations_AttributeOperation_newValue}

# FeatureOperation class attributes and methods

# esmodel_operations_MultiAttributeOperation class attributes and methods
esmodel_operations_MultiAttributeOperation_add: Property = Property(name="add", type=BooleanType)
esmodel_operations_MultiAttributeOperation_indexes: Property = Property(name="indexes", type=IntegerType)
esmodel_operations_MultiAttributeOperation_referencedValues: Property = Property(name="referencedValues", type=StringType)
esmodel_operations_MultiAttributeOperation.attributes={esmodel_operations_MultiAttributeOperation_add, esmodel_operations_MultiAttributeOperation_referencedValues, esmodel_operations_MultiAttributeOperation_indexes}

# esmodel_operations_MultiAttributeMoveOperation class attributes and methods
esmodel_operations_MultiAttributeMoveOperation_oldIndex: Property = Property(name="oldIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_newIndex: Property = Property(name="newIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_referencedValue: Property = Property(name="referencedValue", type=StringType)
esmodel_operations_MultiAttributeMoveOperation.attributes={esmodel_operations_MultiAttributeMoveOperation_referencedValue, esmodel_operations_MultiAttributeMoveOperation_oldIndex, esmodel_operations_MultiAttributeMoveOperation_newIndex}

# esmodel_operations_SingleReferenceOperation class attributes and methods

# ReferenceOperation class attributes and methods

# esmodel_operations_MultiReferenceSetOperation class attributes and methods
esmodel_operations_MultiReferenceSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiReferenceSetOperation.attributes={esmodel_operations_MultiReferenceSetOperation_index}

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
esmodel_operations_ReferenceOperation.attributes={esmodel_operations_ReferenceOperation_containmentType, esmodel_operations_ReferenceOperation_oppositeFeatureName, esmodel_operations_ReferenceOperation_bidirectional}

# esmodel_operations_DiagramLayoutOperation class attributes and methods

# AttributeOperation class attributes and methods

# esmodel_operations_OperationId class attributes and methods

# esmodel_operations_OperationGroup class attributes and methods
esmodel_operations_OperationGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_OperationGroup.attributes={esmodel_operations_OperationGroup_name}

# esmodel_operations_MultiAttributeSetOperation class attributes and methods
esmodel_operations_MultiAttributeSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiAttributeSetOperation_oldValue: Property = Property(name="oldValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation_newValue: Property = Property(name="newValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation.attributes={esmodel_operations_MultiAttributeSetOperation_newValue, esmodel_operations_MultiAttributeSetOperation_index, esmodel_operations_MultiAttributeSetOperation_oldValue}

# esmodel_operations_EObjectToModelElementIdMap class attributes and methods

# esmodel_semantic_SemanticCompositeOperation class attributes and methods

# CompositeOperation class attributes and methods

# esmodel_events_Event class attributes and methods
esmodel_events_Event_timestamp: Property = Property(name="timestamp", type=DateType)
esmodel_events_Event.attributes={esmodel_events_Event_timestamp}

# esmodel_events_ReadEvent class attributes and methods
esmodel_events_ReadEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_ReadEvent_readView: Property = Property(name="readView", type=StringType)
esmodel_events_ReadEvent.attributes={esmodel_events_ReadEvent_sourceView, esmodel_events_ReadEvent_readView}

# Event class attributes and methods

# esmodel_events_MergeEvent class attributes and methods
esmodel_events_MergeEvent_numberOfConflicts: Property = Property(name="numberOfConflicts", type=IntegerType)
esmodel_events_MergeEvent_totalTime: Property = Property(name="totalTime", type=IntegerType)
esmodel_events_MergeEvent.attributes={esmodel_events_MergeEvent_totalTime, esmodel_events_MergeEvent_numberOfConflicts}

# esmodel_events_CheckoutEvent class attributes and methods

# esmodel_events_ExceptionEvent class attributes and methods
esmodel_events_ExceptionEvent_ExceptionTitle: Property = Property(name="ExceptionTitle", type=StringType)
esmodel_events_ExceptionEvent_ExceptionStackTrace: Property = Property(name="ExceptionStackTrace", type=StringType)
esmodel_events_ExceptionEvent_ExceptionCauseTitle: Property = Property(name="ExceptionCauseTitle", type=StringType)
esmodel_events_ExceptionEvent_ExceptionCauseStackTrace: Property = Property(name="ExceptionCauseStackTrace", type=StringType)
esmodel_events_ExceptionEvent.attributes={esmodel_events_ExceptionEvent_ExceptionStackTrace, esmodel_events_ExceptionEvent_ExceptionCauseTitle, esmodel_events_ExceptionEvent_ExceptionTitle, esmodel_events_ExceptionEvent_ExceptionCauseStackTrace}

# esmodel_events_PluginStartEvent class attributes and methods
esmodel_events_PluginStartEvent_pluginId: Property = Property(name="pluginId", type=StringType)
esmodel_events_PluginStartEvent.attributes={esmodel_events_PluginStartEvent_pluginId}

# esmodel_operations_ModelElementGroup class attributes and methods
esmodel_operations_ModelElementGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_ModelElementGroup.attributes={esmodel_operations_ModelElementGroup_name}

# esmodel_events_AnnotationEvent class attributes and methods

# esmodel_events_RevertEvent class attributes and methods
esmodel_events_RevertEvent_revertedChangesCount: Property = Property(name="revertedChangesCount", type=IntegerType)
esmodel_events_RevertEvent.attributes={esmodel_events_RevertEvent_revertedChangesCount}

# esmodel_events_UpdateEvent class attributes and methods

# esmodel_events_ShowHistoryEvent class attributes and methods

# esmodel_events_PerspectiveEvent class attributes and methods

# esmodel_events_DNDEvent class attributes and methods
esmodel_events_DNDEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_DNDEvent_targetView: Property = Property(name="targetView", type=StringType)
esmodel_events_DNDEvent.attributes={esmodel_events_DNDEvent_sourceView, esmodel_events_DNDEvent_targetView}

# esmodel_events_LinkEvent class attributes and methods
esmodel_events_LinkEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_LinkEvent_createdNew: Property = Property(name="createdNew", type=BooleanType)
esmodel_events_LinkEvent.attributes={esmodel_events_LinkEvent_createdNew, esmodel_events_LinkEvent_sourceView}

# esmodel_events_TraceEvent class attributes and methods
esmodel_events_TraceEvent_featureName: Property = Property(name="featureName", type=StringType)
esmodel_events_TraceEvent.attributes={esmodel_events_TraceEvent_featureName}

# esmodel_events_NavigatorCreateEvent class attributes and methods
esmodel_events_NavigatorCreateEvent_dynamic: Property = Property(name="dynamic", type=BooleanType)
esmodel_events_NavigatorCreateEvent.attributes={esmodel_events_NavigatorCreateEvent_dynamic}

# esmodel_events_PluginFocusEvent class attributes and methods
esmodel_events_PluginFocusEvent_pluginId: Property = Property(name="pluginId", type=StringType)
esmodel_events_PluginFocusEvent_startDate: Property = Property(name="startDate", type=DateType)
esmodel_events_PluginFocusEvent.attributes={esmodel_events_PluginFocusEvent_pluginId, esmodel_events_PluginFocusEvent_startDate}

# esmodel_events_PresentationSwitchEvent class attributes and methods
esmodel_events_PresentationSwitchEvent_readView: Property = Property(name="readView", type=StringType)
esmodel_events_PresentationSwitchEvent_newPresentation: Property = Property(name="newPresentation", type=StringType)
esmodel_events_PresentationSwitchEvent.attributes={esmodel_events_PresentationSwitchEvent_readView, esmodel_events_PresentationSwitchEvent_newPresentation}

# esmodel_events_UndoEvent class attributes and methods

# esmodel_events_Validate class attributes and methods

# esmodel_events_ShowChangesEvent class attributes and methods

# esmodel_events_NotificationReadEvent class attributes and methods
esmodel_events_NotificationReadEvent_notificationId: Property = Property(name="notificationId", type=StringType)
esmodel_events_NotificationReadEvent.attributes={esmodel_events_NotificationReadEvent_notificationId}

# ReadEvent class attributes and methods

# esmodel_events_NotificationGenerationEvent class attributes and methods

# esmodel_server_ServerEvent class attributes and methods

# esmodel_events_NotificationIgnoreEvent class attributes and methods
esmodel_events_NotificationIgnoreEvent_notificationId: Property = Property(name="notificationId", type=StringType)
esmodel_events_NotificationIgnoreEvent.attributes={esmodel_events_NotificationIgnoreEvent_notificationId}

# esmodel_server_ServerProjectEvent class attributes and methods

# ServerEvent class attributes and methods

# esmodel_events_URLEvent class attributes and methods
esmodel_events_URLEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_URLEvent.attributes={esmodel_events_URLEvent_sourceView}

# esmodel_server_ProjectUpdatedEvent class attributes and methods

# ServerProjectEvent class attributes and methods

# esmodel_accesscontrol_ACUser class attributes and methods
esmodel_accesscontrol_ACUser_firstName: Property = Property(name="firstName", type=StringType)
esmodel_accesscontrol_ACUser_lastName: Property = Property(name="lastName", type=StringType)
esmodel_accesscontrol_ACUser.attributes={esmodel_accesscontrol_ACUser_firstName, esmodel_accesscontrol_ACUser_lastName}

# ACOrgUnit class attributes and methods

# esmodel_events_MergeChoiceEvent class attributes and methods
esmodel_events_MergeChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeChoiceEvent_contextFeature: Property = Property(name="contextFeature", type=StringType)
esmodel_events_MergeChoiceEvent_createdIssueName: Property = Property(name="createdIssueName", type=StringType)
esmodel_events_MergeChoiceEvent.attributes={esmodel_events_MergeChoiceEvent_createdIssueName, esmodel_events_MergeChoiceEvent_contextFeature, esmodel_events_MergeChoiceEvent_selection}

# operations_OperationId class attributes and methods

# esmodel_accesscontrol_ACOrgUnit class attributes and methods
esmodel_accesscontrol_ACOrgUnit_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_ACOrgUnit_description: Property = Property(name="description", type=StringType)
esmodel_accesscontrol_ACOrgUnit_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
esmodel_accesscontrol_ACOrgUnit.attributes={esmodel_accesscontrol_ACOrgUnit_description, esmodel_accesscontrol_ACOrgUnit_name}
esmodel_accesscontrol_ACOrgUnit.methods={esmodel_accesscontrol_ACOrgUnit_m_getId}

# esmodel_events_MergeGlobalChoiceEvent class attributes and methods
esmodel_events_MergeGlobalChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeGlobalChoiceEvent.attributes={esmodel_events_MergeGlobalChoiceEvent_selection}

# esmodel_roles_Role class attributes and methods
esmodel_roles_Role_m_canAdministrate: Method = Method(name="canAdministrate", parameters={Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canCreate: Method = Method(name="canCreate", parameters={Parameter(name='esmodel_projectId', type=StringType), Parameter(name='esmodel_modelElement', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canDelete: Method = Method(name="canDelete", parameters={Parameter(name='esmodel_projectId', type=StringType), Parameter(name='esmodel_modelElement', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canModify: Method = Method(name="canModify", parameters={Parameter(name='esmodel_modelElement', type=StringType), Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role_m_canRead: Method = Method(name="canRead", parameters={Parameter(name='esmodel_modelElement', type=StringType), Parameter(name='esmodel_projectId', type=StringType)}, type=BooleanType)
esmodel_roles_Role.methods={esmodel_roles_Role_m_canDelete, esmodel_roles_Role_m_canCreate, esmodel_roles_Role_m_canRead, esmodel_roles_Role_m_canAdministrate, esmodel_roles_Role_m_canModify}

# esmodel_roles_ReaderRole class attributes and methods

# Role class attributes and methods

# esmodel_roles_WriterRole class attributes and methods

# roles_Role class attributes and methods

# accesscontrol_OrgUnitProperty class attributes and methods

# esmodel_accesscontrol_ACGroup class attributes and methods

# accesscontrol_ACOrgUnit class attributes and methods

# esmodel_accesscontrol_ACOrgUnitId class attributes and methods

# esmodel_accesscontrol_OrgUnitProperty class attributes and methods
esmodel_accesscontrol_OrgUnitProperty_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_OrgUnitProperty_value: Property = Property(name="value", type=StringType)
esmodel_accesscontrol_OrgUnitProperty.attributes={esmodel_accesscontrol_OrgUnitProperty_name, esmodel_accesscontrol_OrgUnitProperty_value}

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

# esmodel_roles_ProjectAdminRole class attributes and methods

# esmodel_roles_ServerAdmin class attributes and methods

# esmodel_notification_ESNotification class attributes and methods
esmodel_notification_ESNotification_recipient: Property = Property(name="recipient", type=StringType)
esmodel_notification_ESNotification_name: Property = Property(name="name", type=StringType)
esmodel_notification_ESNotification_message: Property = Property(name="message", type=StringType)
esmodel_notification_ESNotification_details: Property = Property(name="details", type=StringType)
esmodel_notification_ESNotification_seen: Property = Property(name="seen", type=BooleanType)
esmodel_notification_ESNotification_creationDate: Property = Property(name="creationDate", type=DateType)
esmodel_notification_ESNotification_provider: Property = Property(name="provider", type=StringType)
esmodel_notification_ESNotification_sender: Property = Property(name="sender", type=StringType)
esmodel_notification_ESNotification.attributes={esmodel_notification_ESNotification_seen, esmodel_notification_ESNotification_provider, esmodel_notification_ESNotification_creationDate, esmodel_notification_ESNotification_message, esmodel_notification_ESNotification_recipient, esmodel_notification_ESNotification_name, esmodel_notification_ESNotification_details, esmodel_notification_ESNotification_sender}

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
groupMemberships14: BinaryAssociation = BinaryAssociation(
    name="groupMemberships14",
    ends={
        Property(name="Group", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="orgUnits", type=organization_Group, multiplicity=Multiplicity(0, 9999))
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
workItemsToReview18: BinaryAssociation = BinaryAssociation(
    name="workItemsToReview18",
    ends={
        Property(name="WorkItem19", type=model_organization_User, multiplicity=Multiplicity(1, 1)),
        Property(name="reviewer", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
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
participants29: BinaryAssociation = BinaryAssociation(
    name="participants29",
    ends={
        Property(name="OrgUnit30", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="participations", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
associatedChangePackages31: BinaryAssociation = BinaryAssociation(
    name="associatedChangePackages31",
    ends={
        Property(name="change_ModelChangePackage", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_task_WorkItem", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
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
reviewer28: BinaryAssociation = BinaryAssociation(
    name="reviewer28",
    ends={
        Property(name="User", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="workItemsToReview", type=organization_User, multiplicity=Multiplicity(0, 1))
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
attributes55: BinaryAssociation = BinaryAssociation(
    name="attributes55",
    ends={
        Property(name="Attribute", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="definingClass", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
definingClass68: BinaryAssociation = BinaryAssociation(
    name="definingClass68",
    ends={
        Property(name="Class69", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
arguments74: BinaryAssociation = BinaryAssociation(
    name="arguments74",
    ends={
        Property(name="model_classes_Method", type=classes_MethodArgument, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="classes_MethodArgument", type=model_classes_Method, multiplicity=Multiplicity(1, 1))
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
includedUseCases100: BinaryAssociation = BinaryAssociation(
    name="includedUseCases100",
    ends={
        Property(name="requirement_UseCase", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_UseCase", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
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
instantiatedUseCases113: BinaryAssociation = BinaryAssociation(
    name="instantiatedUseCases113",
    ends={
        Property(name="UseCase114", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarios", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
functionalRequirements115: BinaryAssociation = BinaryAssociation(
    name="functionalRequirements115",
    ends={
        Property(name="FunctionalRequirement117", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="scenarios116", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
participatingMethods118: BinaryAssociation = BinaryAssociation(
    name="participatingMethods118",
    ends={
        Property(name="Method119", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="demoParticipations", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
useCaseSteps110: BinaryAssociation = BinaryAssociation(
    name="useCaseSteps110",
    ends={
        Property(name="Step", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps126: BinaryAssociation = BinaryAssociation(
    name="steps126",
    ends={
        Property(name="requirement_Step", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Scenario", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFunctionalRequirements127: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements127",
    ends={
        Property(name="NonFunctionalRequirement128", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictedScenarios", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedUseCases129: BinaryAssociation = BinaryAssociation(
    name="initiatedUseCases129",
    ends={
        Property(name="UseCase130", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActor", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
participatedUseCases131: BinaryAssociation = BinaryAssociation(
    name="participatedUseCases131",
    ends={
        Property(name="UseCase132", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActors", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
instances133: BinaryAssociation = BinaryAssociation(
    name="instances133",
    ends={
        Property(name="ActorInstance134", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiatedActor", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
participatedUserTasks135: BinaryAssociation = BinaryAssociation(
    name="participatedUserTasks135",
    ends={
        Property(name="UserTask136", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActor", type=requirement_UserTask, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedUserTask137: BinaryAssociation = BinaryAssociation(
    name="initiatedUserTask137",
    ends={
        Property(name="UserTask139", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActor138", type=requirement_UserTask, multiplicity=Multiplicity(0, 1))
    }
)
initiatedScenarios140: BinaryAssociation = BinaryAssociation(
    name="initiatedScenarios140",
    ends={
        Property(name="Scenario141", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatingActorInstance", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
participatingClasses120: BinaryAssociation = BinaryAssociation(
    name="participatingClasses120",
    ends={
        Property(name="Class122", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="demoParticipations121", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActorInstance123: BinaryAssociation = BinaryAssociation(
    name="initiatingActorInstance123",
    ends={
        Property(name="ActorInstance", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedScenarios", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 1))
    }
)
participatingActorInstances124: BinaryAssociation = BinaryAssociation(
    name="participatingActorInstances124",
    ends={
        Property(name="ActorInstance125", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedScenarios", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
includedUseCase146: BinaryAssociation = BinaryAssociation(
    name="includedUseCase146",
    ends={
        Property(name="requirement_UseCase147", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
useCase148: BinaryAssociation = BinaryAssociation(
    name="useCase148",
    ends={
        Property(name="UseCase149", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="useCaseSteps", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
includedSystemFunction150: BinaryAssociation = BinaryAssociation(
    name="includedSystemFunction150",
    ends={
        Property(name="requirement_SystemFunction", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step151", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 1))
    }
)
initiatingActor152: BinaryAssociation = BinaryAssociation(
    name="initiatingActor152",
    ends={
        Property(name="Actor153", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedUserTask", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
participatingActor154: BinaryAssociation = BinaryAssociation(
    name="participatingActor154",
    ends={
        Property(name="Actor155", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="participatedUserTasks", type=requirement_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
realizingUseCases156: BinaryAssociation = BinaryAssociation(
    name="realizingUseCases156",
    ends={
        Property(name="UseCase157", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedUserTask", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedUseCases158: BinaryAssociation = BinaryAssociation(
    name="restrictedUseCases158",
    ends={
        Property(name="UseCase159", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirements", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedScenarios160: BinaryAssociation = BinaryAssociation(
    name="restrictedScenarios160",
    ends={
        Property(name="Scenario162", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="nonFunctionalRequirements161", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
participatedScenarios142: BinaryAssociation = BinaryAssociation(
    name="participatedScenarios142",
    ends={
        Property(name="Scenario143", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="participatingActorInstances", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
instantiatedActor144: BinaryAssociation = BinaryAssociation(
    name="instantiatedActor144",
    ends={
        Property(name="Actor145", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
solution164: BinaryAssociation = BinaryAssociation(
    name="solution164",
    ends={
        Property(name="Solution", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue165", type=rationale_Solution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
criteria166: BinaryAssociation = BinaryAssociation(
    name="criteria166",
    ends={
        Property(name="rationale_Criterion", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Issue", type=rationale_Criterion, multiplicity=Multiplicity(0, 9999))
    }
)
issue167: BinaryAssociation = BinaryAssociation(
    name="issue167",
    ends={
        Property(name="Issue", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="proposals", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
assessments168: BinaryAssociation = BinaryAssociation(
    name="assessments168",
    ends={
        Property(name="Assessment", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="proposal", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
underlyingProposals169: BinaryAssociation = BinaryAssociation(
    name="underlyingProposals169",
    ends={
        Property(name="rationale_Proposal", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Solution", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999))
    }
)
issue170: BinaryAssociation = BinaryAssociation(
    name="issue170",
    ends={
        Property(name="Issue171", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="solution", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
assessments172: BinaryAssociation = BinaryAssociation(
    name="assessments172",
    ends={
        Property(name="Assessment173", type=model_rationale_Criterion, multiplicity=Multiplicity(1, 1)),
        Property(name="criterion", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999))
    }
)
proposals163: BinaryAssociation = BinaryAssociation(
    name="proposals163",
    ends={
        Property(name="Proposal", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="issue", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sender178: BinaryAssociation = BinaryAssociation(
    name="sender178",
    ends={
        Property(name="organization_OrgUnit179", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
recipients180: BinaryAssociation = BinaryAssociation(
    name="recipients180",
    ends={
        Property(name="organization_OrgUnit182", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment181", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
commentedElement183: BinaryAssociation = BinaryAssociation(
    name="commentedElement183",
    ends={
        Property(name="UnicaseModelElement184", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
conflictingProposals185: BinaryAssociation = BinaryAssociation(
    name="conflictingProposals185",
    ends={
        Property(name="change_MergingProposal", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal", type=change_MergingProposal, multiplicity=Multiplicity(0, 9999))
    }
)
pendingChanges186: BinaryAssociation = BinaryAssociation(
    name="pendingChanges186",
    ends={
        Property(name="change_ModelChangePackage188", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal187", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 1))
    }
)
appliedChanges189: BinaryAssociation = BinaryAssociation(
    name="appliedChanges189",
    ends={
        Property(name="change_ModelChangePackage190", type=model_change_MergingSolution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingSolution", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
    }
)
proposal174: BinaryAssociation = BinaryAssociation(
    name="proposal174",
    ends={
        Property(name="Proposal175", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessments", type=rationale_Proposal, multiplicity=Multiplicity(0, 1))
    }
)
criterion176: BinaryAssociation = BinaryAssociation(
    name="criterion176",
    ends={
        Property(name="Criterion", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessments177", type=rationale_Criterion, multiplicity=Multiplicity(0, 1))
    }
)
packages191: BinaryAssociation = BinaryAssociation(
    name="packages191",
    ends={
        Property(name="classes_Package", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
subsystems192: BinaryAssociation = BinaryAssociation(
    name="subsystems192",
    ends={
        Property(name="classes_Package194", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component193", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
offeredServices195: BinaryAssociation = BinaryAssociation(
    name="offeredServices195",
    ends={
        Property(name="ComponentService", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="offeringComponent", type=component_ComponentService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumedServices196: BinaryAssociation = BinaryAssociation(
    name="consumedServices196",
    ends={
        Property(name="ComponentService197", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="consumingComponents", type=component_ComponentService, multiplicity=Multiplicity(0, 9999))
    }
)
offeringComponent198: BinaryAssociation = BinaryAssociation(
    name="offeringComponent198",
    ends={
        Property(name="Component", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="offeredServices", type=component_Component, multiplicity=Multiplicity(0, 1))
    }
)
consumingComponents199: BinaryAssociation = BinaryAssociation(
    name="consumingComponents199",
    ends={
        Property(name="Component200", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="consumedServices", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
components201: BinaryAssociation = BinaryAssociation(
    name="components201",
    ends={
        Property(name="component_Component", type=model_component_DeploymentNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_DeploymentNode", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
facilitator202: BinaryAssociation = BinaryAssociation(
    name="facilitator202",
    ends={
        Property(name="organization_User", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
minutetaker203: BinaryAssociation = BinaryAssociation(
    name="minutetaker203",
    ends={
        Property(name="organization_User205", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting204", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
timekeeper206: BinaryAssociation = BinaryAssociation(
    name="timekeeper206",
    ends={
        Property(name="organization_User208", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting207", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
participants209: BinaryAssociation = BinaryAssociation(
    name="participants209",
    ends={
        Property(name="organization_OrgUnit211", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting210", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
sections212: BinaryAssociation = BinaryAssociation(
    name="sections212",
    ends={
        Property(name="meeting_MeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting213", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiedIssuesSection214: BinaryAssociation = BinaryAssociation(
    name="identifiedIssuesSection214",
    ends={
        Property(name="meeting_IssueMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting215", type=meeting_IssueMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
identifiedWorkItemsSection216: BinaryAssociation = BinaryAssociation(
    name="identifiedWorkItemsSection216",
    ends={
        Property(name="meeting_WorkItemMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting217", type=meeting_WorkItemMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
subsections218: BinaryAssociation = BinaryAssociation(
    name="subsections218",
    ends={
        Property(name="meeting_MeetingSection219", type=model_meeting_CompositeMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_CompositeMeetingSection", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedIssues220: BinaryAssociation = BinaryAssociation(
    name="includedIssues220",
    ends={
        Property(name="rationale_Issue", type=model_meeting_IssueMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_IssueMeetingSection", type=rationale_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
includedWorkItems221: BinaryAssociation = BinaryAssociation(
    name="includedWorkItems221",
    ends={
        Property(name="task_WorkItem", type=model_meeting_WorkItemMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_WorkItemMeetingSection", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
source222: BinaryAssociation = BinaryAssociation(
    name="source222",
    ends={
        Property(name="StateNode", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
target223: BinaryAssociation = BinaryAssociation(
    name="target223",
    ends={
        Property(name="StateNode224", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions225: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions225",
    ends={
        Property(name="Transition", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source226", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions227: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions227",
    ends={
        Property(name="Transition229", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target228", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypes232: BinaryAssociation = BinaryAssociation(
    name="stereotypes232",
    ends={
        Property(name="Stereotype", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="profile", type=profile_Stereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
profile233: BinaryAssociation = BinaryAssociation(
    name="profile233",
    ends={
        Property(name="Profile", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypes", type=profile_Profile, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeInstances234: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstances234",
    ends={
        Property(name="StereotypeInstance235", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeAttributes236: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributes236",
    ends={
        Property(name="StereotypeAttribute", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype237", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype238: BinaryAssociation = BinaryAssociation(
    name="stereotype238",
    ends={
        Property(name="Stereotype239", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeInstances", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
modelElement240: BinaryAssociation = BinaryAssociation(
    name="modelElement240",
    ends={
        Property(name="UnicaseModelElement241", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedStereotypeInstances", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances242: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances242",
    ends={
        Property(name="StereotypeAttributeInstance", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeInstance", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype243: BinaryAssociation = BinaryAssociation(
    name="stereotype243",
    ends={
        Property(name="Stereotype244", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributes", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances245: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances245",
    ends={
        Property(name="StereotypeAttributeInstance246", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttribute", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeInstance247: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstance247",
    ends={
        Property(name="StereotypeInstance248", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributeInstances", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 1))
    }
)
affectedContainers230: BinaryAssociation = BinaryAssociation(
    name="affectedContainers230",
    ends={
        Property(name="UnicaseModelElement231", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_profile_Profile", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
source252: BinaryAssociation = BinaryAssociation(
    name="source252",
    ends={
        Property(name="ModelElementId", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target253: BinaryAssociation = BinaryAssociation(
    name="target253",
    ends={
        Property(name="ModelElementId255", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath254", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path256: BinaryAssociation = BinaryAssociation(
    name="path256",
    ends={
        Property(name="ModelElementId258", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath257", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions259: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions259",
    ends={
        Property(name="Transition261", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="source260", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions262: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions262",
    ends={
        Property(name="Transition264", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="target263", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source265: BinaryAssociation = BinaryAssociation(
    name="source265",
    ends={
        Property(name="ActivityObject", type=model_activity_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions266", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1))
    }
)
target267: BinaryAssociation = BinaryAssociation(
    name="target267",
    ends={
        Property(name="ActivityObject269", type=model_activity_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions268", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1))
    }
)
projectId270: BinaryAssociation = BinaryAssociation(
    name="projectId270",
    ends={
        Property(name="ProjectId", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
versions271: BinaryAssociation = BinaryAssociation(
    name="versions271",
    ends={
        Property(name="versioning_Version", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory272", type=versioning_Version, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stereotypeAttribute249: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttribute249",
    ends={
        Property(name="StereotypeAttribute251", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeAttributeInstances250", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
projectId273: BinaryAssociation = BinaryAssociation(
    name="projectId273",
    ends={
        Property(name="ProjectId274", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo", type=ProjectId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
version275: BinaryAssociation = BinaryAssociation(
    name="version275",
    ends={
        Property(name="versioning_PrimaryVersionSpec", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo276", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups277: BinaryAssociation = BinaryAssociation(
    name="groups277",
    ends={
        Property(name="accesscontrol_ACGroup", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace", type=accesscontrol_ACGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects278: BinaryAssociation = BinaryAssociation(
    name="projects278",
    ends={
        Property(name="ProjectHistory", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace279", type=ProjectHistory, multiplicity=Multiplicity(0, 9999))
    }
)
openSessions280: BinaryAssociation = BinaryAssociation(
    name="openSessions280",
    ends={
        Property(name="SessionId", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace281", type=SessionId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users282: BinaryAssociation = BinaryAssociation(
    name="users282",
    ends={
        Property(name="accesscontrol_ACUser", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace283", type=accesscontrol_ACUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations284: BinaryAssociation = BinaryAssociation(
    name="operations284",
    ends={
        Property(name="operations_AbstractOperation", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events285: BinaryAssociation = BinaryAssociation(
    name="events285",
    ends={
        Property(name="events_Event", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage286", type=events_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logMessage287: BinaryAssociation = BinaryAssociation(
    name="logMessage287",
    ends={
        Property(name="versioning_LogMessage", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage288", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications289: BinaryAssociation = BinaryAssociation(
    name="notifications289",
    ends={
        Property(name="notification_ESNotification", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage290", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties291: BinaryAssociation = BinaryAssociation(
    name="versionProperties291",
    ends={
        Property(name="versioning_VersionProperty", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage292", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primerySpec293: BinaryAssociation = BinaryAssociation(
    name="primerySpec293",
    ends={
        Property(name="versioning_PrimaryVersionSpec294", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
logMessage295: BinaryAssociation = BinaryAssociation(
    name="logMessage295",
    ends={
        Property(name="versioning_LogMessage297", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo296", type=versioning_LogMessage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs298: BinaryAssociation = BinaryAssociation(
    name="tagSpecs298",
    ends={
        Property(name="versioning_TagVersionSpec", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo299", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties300: BinaryAssociation = BinaryAssociation(
    name="versionProperties300",
    ends={
        Property(name="versioning_VersionProperty302", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo301", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changePackage303: BinaryAssociation = BinaryAssociation(
    name="changePackage303",
    ends={
        Property(name="versioning_ChangePackage", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo304", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source305: BinaryAssociation = BinaryAssociation(
    name="source305",
    ends={
        Property(name="versioning_PrimaryVersionSpec306", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target307: BinaryAssociation = BinaryAssociation(
    name="target307",
    ends={
        Property(name="versioning_PrimaryVersionSpec309", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery308", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElements310: BinaryAssociation = BinaryAssociation(
    name="modelElements310",
    ends={
        Property(name="ModelElementId312", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery311", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectState313: BinaryAssociation = BinaryAssociation(
    name="projectState313",
    ends={
        Property(name="Project", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version", type=Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primarySpec314: BinaryAssociation = BinaryAssociation(
    name="primarySpec314",
    ends={
        Property(name="versioning_PrimaryVersionSpec316", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version315", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs317: BinaryAssociation = BinaryAssociation(
    name="tagSpecs317",
    ends={
        Property(name="versioning_TagVersionSpec319", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version318", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextVersion320: BinaryAssociation = BinaryAssociation(
    name="nextVersion320",
    ends={
        Property(name="Version", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="previousVersion", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
previousVersion321: BinaryAssociation = BinaryAssociation(
    name="previousVersion321",
    ends={
        Property(name="Version322", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="nextVersion", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
changes323: BinaryAssociation = BinaryAssociation(
    name="changes323",
    ends={
        Property(name="versioning_ChangePackage325", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version324", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logMessage326: BinaryAssociation = BinaryAssociation(
    name="logMessage326",
    ends={
        Property(name="versioning_LogMessage328", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version327", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId329: BinaryAssociation = BinaryAssociation(
    name="modelElementId329",
    ends={
        Property(name="ModelElementId330", type=esmodel_operations_AbstractOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_AbstractOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subOperations331: BinaryAssociation = BinaryAssociation(
    name="subOperations331",
    ends={
        Property(name="operations_AbstractOperation332", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainOperation333: BinaryAssociation = BinaryAssociation(
    name="mainOperation333",
    ends={
        Property(name="operations_AbstractOperation335", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation334", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1))
    }
)
modelElement336: BinaryAssociation = BinaryAssociation(
    name="modelElement336",
    ends={
        Property(name="operations_esmodel_EObject", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subOperations337: BinaryAssociation = BinaryAssociation(
    name="subOperations337",
    ends={
        Property(name="operations_ReferenceOperation", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation338", type=operations_ReferenceOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eObjectToIdMap339: BinaryAssociation = BinaryAssociation(
    name="eObjectToIdMap339",
    ends={
        Property(name="operations_EObjectToModelElementIdMap", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation340", type=operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oldValue341: BinaryAssociation = BinaryAssociation(
    name="oldValue341",
    ends={
        Property(name="ModelElementId342", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue343: BinaryAssociation = BinaryAssociation(
    name="newValue343",
    ends={
        Property(name="ModelElementId345", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation344", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oldValue346: BinaryAssociation = BinaryAssociation(
    name="oldValue346",
    ends={
        Property(name="ModelElementId347", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue348: BinaryAssociation = BinaryAssociation(
    name="newValue348",
    ends={
        Property(name="ModelElementId350", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation349", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedModelElements351: BinaryAssociation = BinaryAssociation(
    name="referencedModelElements351",
    ends={
        Property(name="ModelElementId352", type=esmodel_operations_MultiReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModelElementId353: BinaryAssociation = BinaryAssociation(
    name="referencedModelElementId353",
    ends={
        Property(name="ModelElementId354", type=esmodel_operations_MultiReferenceMoveOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceMoveOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations355: BinaryAssociation = BinaryAssociation(
    name="operations355",
    ends={
        Property(name="operations_AbstractOperation356", type=esmodel_operations_OperationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_OperationGroup", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999))
    }
)
key359: BinaryAssociation = BinaryAssociation(
    name="key359",
    ends={
        Property(name="operations_esmodel_EObject360", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value361: BinaryAssociation = BinaryAssociation(
    name="value361",
    ends={
        Property(name="ModelElementId363", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap362", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement364: BinaryAssociation = BinaryAssociation(
    name="modelElement364",
    ends={
        Property(name="ModelElementId365", type=esmodel_events_ReadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ReadEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseVersion366: BinaryAssociation = BinaryAssociation(
    name="baseVersion366",
    ends={
        Property(name="versioning_PrimaryVersionSpec367", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion368: BinaryAssociation = BinaryAssociation(
    name="targetVersion368",
    ends={
        Property(name="versioning_PrimaryVersionSpec370", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent369", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localChanges371: BinaryAssociation = BinaryAssociation(
    name="localChanges371",
    ends={
        Property(name="operations_AbstractOperation373", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent372", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseVersion374: BinaryAssociation = BinaryAssociation(
    name="baseVersion374",
    ends={
        Property(name="versioning_PrimaryVersionSpec375", type=esmodel_events_CheckoutEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_CheckoutEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElements357: BinaryAssociation = BinaryAssociation(
    name="modelElements357",
    ends={
        Property(name="ModelElementId358", type=esmodel_operations_ModelElementGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_ModelElementGroup", type=ModelElementId, multiplicity=Multiplicity(0, 9999))
    }
)
baseVersion376: BinaryAssociation = BinaryAssociation(
    name="baseVersion376",
    ends={
        Property(name="versioning_PrimaryVersionSpec377", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion378: BinaryAssociation = BinaryAssociation(
    name="targetVersion378",
    ends={
        Property(name="versioning_PrimaryVersionSpec380", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent379", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotatedElement381: BinaryAssociation = BinaryAssociation(
    name="annotatedElement381",
    ends={
        Property(name="ModelElementId382", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation383: BinaryAssociation = BinaryAssociation(
    name="annotation383",
    ends={
        Property(name="ModelElementId385", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent384", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion386: BinaryAssociation = BinaryAssociation(
    name="sourceVersion386",
    ends={
        Property(name="versioning_PrimaryVersionSpec387", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion388: BinaryAssociation = BinaryAssociation(
    name="targetVersion388",
    ends={
        Property(name="versioning_PrimaryVersionSpec390", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent389", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement391: BinaryAssociation = BinaryAssociation(
    name="modelElement391",
    ends={
        Property(name="ModelElementId393", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent392", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dragSourceElement394: BinaryAssociation = BinaryAssociation(
    name="dragSourceElement394",
    ends={
        Property(name="ModelElementId395", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropTargetElement396: BinaryAssociation = BinaryAssociation(
    name="dropTargetElement396",
    ends={
        Property(name="ModelElementId398", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent397", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElement399: BinaryAssociation = BinaryAssociation(
    name="sourceElement399",
    ends={
        Property(name="ModelElementId400", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetElement401: BinaryAssociation = BinaryAssociation(
    name="targetElement401",
    ends={
        Property(name="ModelElementId403", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent402", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElement404: BinaryAssociation = BinaryAssociation(
    name="sourceElement404",
    ends={
        Property(name="ModelElementId405", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_TraceEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetElement406: BinaryAssociation = BinaryAssociation(
    name="targetElement406",
    ends={
        Property(name="ModelElementId408", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_TraceEvent407", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createdElement409: BinaryAssociation = BinaryAssociation(
    name="createdElement409",
    ends={
        Property(name="ModelElementId410", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceSection411: BinaryAssociation = BinaryAssociation(
    name="sourceSection411",
    ends={
        Property(name="ModelElementId413", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent412", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation414: BinaryAssociation = BinaryAssociation(
    name="operation414",
    ends={
        Property(name="operations_AbstractOperation415", type=esmodel_events_UndoEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UndoEvent", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion416: BinaryAssociation = BinaryAssociation(
    name="sourceVersion416",
    ends={
        Property(name="versioning_PrimaryVersionSpec417", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion418: BinaryAssociation = BinaryAssociation(
    name="targetVersion418",
    ends={
        Property(name="versioning_PrimaryVersionSpec420", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent419", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectId435: BinaryAssociation = BinaryAssociation(
    name="projectId435",
    ends={
        Property(name="ProjectId436", type=esmodel_server_ServerProjectEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ServerProjectEvent", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceModelElement423: BinaryAssociation = BinaryAssociation(
    name="sourceModelElement423",
    ends={
        Property(name="ModelElementId424", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newVersion437: BinaryAssociation = BinaryAssociation(
    name="newVersion437",
    ends={
        Property(name="versioning_PrimaryVersionSpec438", type=esmodel_server_ProjectUpdatedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ProjectUpdatedEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceURL425: BinaryAssociation = BinaryAssociation(
    name="sourceURL425",
    ends={
        Property(name="ModelElementId427", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent426", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myAcceptedChanges428: BinaryAssociation = BinaryAssociation(
    name="myAcceptedChanges428",
    ends={
        Property(name="operations_OperationId", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theirRejectedChanges429: BinaryAssociation = BinaryAssociation(
    name="theirRejectedChanges429",
    ends={
        Property(name="operations_OperationId431", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent430", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextModelElement432: BinaryAssociation = BinaryAssociation(
    name="contextModelElement432",
    ends={
        Property(name="ModelElementId434", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent433", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications421: BinaryAssociation = BinaryAssociation(
    name="notifications421",
    ends={
        Property(name="notification_ESNotification422", type=esmodel_events_NotificationGenerationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NotificationGenerationEvent", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project443: BinaryAssociation = BinaryAssociation(
    name="project443",
    ends={
        Property(name="esmodel_accesscontrol_OrgUnitProperty", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ProjectId444", type=esmodel_accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(1, 1))
    }
)
projects445: BinaryAssociation = BinaryAssociation(
    name="projects445",
    ends={
        Property(name="ProjectId446", type=esmodel_roles_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_roles_Role", type=ProjectId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles439: BinaryAssociation = BinaryAssociation(
    name="roles439",
    ends={
        Property(name="roles_Role", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit", type=roles_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties440: BinaryAssociation = BinaryAssociation(
    name="properties440",
    ends={
        Property(name="accesscontrol_OrgUnitProperty", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit441", type=accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members442: BinaryAssociation = BinaryAssociation(
    name="members442",
    ends={
        Property(name="accesscontrol_ACOrgUnit", type=esmodel_accesscontrol_ACGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACGroup", type=accesscontrol_ACOrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
project447: BinaryAssociation = BinaryAssociation(
    name="project447",
    ends={
        Property(name="ProjectId448", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relatedModelElements449: BinaryAssociation = BinaryAssociation(
    name="relatedModelElements449",
    ends={
        Property(name="ModelElementId451", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification450", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedOperations452: BinaryAssociation = BinaryAssociation(
    name="relatedOperations452",
    ends={
        Property(name="operations_OperationId454", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification453", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectId455: BinaryAssociation = BinaryAssociation(
    name="projectId455",
    ends={
        Property(name="ProjectId456", type=esmodel_url_ProjectUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ProjectUrlFragment", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId457: BinaryAssociation = BinaryAssociation(
    name="modelElementId457",
    ends={
        Property(name="ModelElementId458", type=esmodel_url_ModelElementUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrlFragment", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serverUrl459: BinaryAssociation = BinaryAssociation(
    name="serverUrl459",
    ends={
        Property(name="url_ServerUrl", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl", type=url_ServerUrl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectUrlFragment460: BinaryAssociation = BinaryAssociation(
    name="projectUrlFragment460",
    ends={
        Property(name="url_ProjectUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl461", type=url_ProjectUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementUrlFragment462: BinaryAssociation = BinaryAssociation(
    name="modelElementUrlFragment462",
    ends={
        Property(name="url_ModelElementUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl463", type=url_ModelElementUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_UnicaseModelElement_ModelElement = Generalization(general=ModelElement, specific=model_UnicaseModelElement)
gen_metamodel_ModelElement_IdentifiableElement = Generalization(general=IdentifiableElement, specific=metamodel_ModelElement)
gen_metamodel_ModelElementId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=metamodel_ModelElementId)
gen_model_organization_OrgUnit_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_organization_OrgUnit)
gen_model_organization_User_OrgUnit = Generalization(general=OrgUnit, specific=model_organization_User)
gen_model_Annotation_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_Annotation)
gen_model_Attachment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_Attachment)
gen_model_Project_Project = Generalization(general=Project, specific=model_Project)
gen_model_task_WorkPackage_WorkItem = Generalization(general=WorkItem, specific=model_task_WorkPackage)
gen_model_organization_Group_OrgUnit = Generalization(general=OrgUnit, specific=model_organization_Group)
gen_model_task_WorkItem_Annotation = Generalization(general=Annotation, specific=model_task_WorkItem)
gen_model_task_ActionItem_task_Checkable = Generalization(general=task_Checkable, specific=model_task_ActionItem)
gen_model_diagram_MEDiagram_Attachment = Generalization(general=Attachment, specific=model_diagram_MEDiagram)
gen_model_task_Milestone_WorkItem = Generalization(general=WorkItem, specific=model_task_Milestone)
gen_model_task_Checkable_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_task_Checkable)
gen_model_task_ActionItem_task_WorkItem = Generalization(general=task_WorkItem, specific=model_task_ActionItem)
gen_model_classes_PackageElement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_PackageElement)
gen_model_classes_Class_PackageElement = Generalization(general=PackageElement, specific=model_classes_Class)
gen_model_classes_Association_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Association)
gen_model_classes_Attribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Attribute)
gen_model_classes_Package_PackageElement = Generalization(general=PackageElement, specific=model_classes_Package)
gen_model_classes_Method_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Method)
gen_model_classes_MethodArgument_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_MethodArgument)
gen_model_classes_Dependency_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Dependency)
gen_model_document_CompositeSection_Section = Generalization(general=Section, specific=model_document_CompositeSection)
gen_model_requirement_FunctionalRequirement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_FunctionalRequirement)
gen_model_document_Section_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_document_Section)
gen_model_document_LeafSection_Section = Generalization(general=Section, specific=model_document_LeafSection)
gen_model_requirement_UseCase_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UseCase)
gen_model_requirement_Scenario_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Scenario)
gen_model_requirement_Actor_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Actor)
gen_model_requirement_ActorInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_ActorInstance)
gen_model_requirement_Step_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Step)
gen_model_requirement_Step_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_Step)
gen_model_requirement_SystemFunction_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_SystemFunction)
gen_model_requirement_SystemFunction_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_SystemFunction)
gen_model_requirement_UserTask_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UserTask)
gen_model_requirement_UserTask_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_UserTask)
gen_model_requirement_NonFunctionalRequirement_Criterion = Generalization(general=Criterion, specific=model_requirement_NonFunctionalRequirement)
gen_model_rationale_Issue_Annotation = Generalization(general=Annotation, specific=model_rationale_Issue)
gen_model_rationale_Issue_task_Checkable = Generalization(general=task_Checkable, specific=model_rationale_Issue)
gen_model_rationale_Issue_task_WorkItem = Generalization(general=task_WorkItem, specific=model_rationale_Issue)
gen_model_rationale_Proposal_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Proposal)
gen_model_rationale_Proposal_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Proposal)
gen_model_rationale_Solution_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Solution)
gen_model_rationale_Solution_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Solution)
gen_model_rationale_Criterion_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Criterion)
gen_model_rationale_Assessment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Assessment)
gen_model_rationale_Assessment_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Assessment)
gen_model_rationale_Comment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Comment)
gen_model_change_ModelChangePackage_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_change_ModelChangePackage)
gen_model_change_MergingIssue_Issue = Generalization(general=Issue, specific=model_change_MergingIssue)
gen_model_change_MergingProposal_Proposal = Generalization(general=Proposal, specific=model_change_MergingProposal)
gen_model_change_MergingSolution_Solution = Generalization(general=Solution, specific=model_change_MergingSolution)
gen_model_bug_BugReport_task_WorkItem = Generalization(general=task_WorkItem, specific=model_bug_BugReport)
gen_model_bug_BugReport_task_Checkable = Generalization(general=task_Checkable, specific=model_bug_BugReport)
gen_model_component_Component_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_Component)
gen_model_component_ComponentService_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_ComponentService)
gen_model_component_DeploymentNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_DeploymentNode)
gen_model_meeting_Meeting_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_Meeting)
gen_model_meeting_MeetingSection_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_MeetingSection)
gen_model_meeting_CompositeMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_CompositeMeetingSection)
gen_model_meeting_IssueMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_IssueMeetingSection)
gen_model_state_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_Transition)
gen_model_state_StateNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_StateNode)
gen_model_state_State_StateNode = Generalization(general=StateNode, specific=model_state_State)
gen_model_state_StateInitial_StateNode = Generalization(general=StateNode, specific=model_state_StateInitial)
gen_model_state_StateEnd_StateNode = Generalization(general=StateNode, specific=model_state_StateEnd)
gen_model_attachment_UrlAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_UrlAttachment)
gen_model_attachment_FileAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_FileAttachment)
gen_model_meeting_WorkItemMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_WorkItemMeetingSection)
gen_model_profile_Stereotype_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Stereotype)
gen_model_profile_StereotypeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeInstance)
gen_model_profile_StereotypeAttribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttribute)
gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute = Generalization(general=StereotypeAttribute, specific=model_profile_StereotypeAttributeSimple)
gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttributeInstance)
gen_model_profile_Profile_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Profile)
gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance = Generalization(general=StereotypeAttributeInstance, specific=model_profile_StereotypeAttributeInstanceString)
gen_model_activity_ActivityObject_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_ActivityObject)
gen_model_activity_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_Transition)
gen_model_activity_Activity_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Activity)
gen_model_activity_Fork_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Fork)
gen_model_activity_Branch_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Branch)
gen_model_activity_ActivityInitial_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityInitial)
gen_model_activity_ActivityEnd_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityEnd)
gen_esmodel_SessionId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_SessionId)
gen_esmodel_ProjectId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_ProjectId)
gen_esmodel_versioning_TagVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_TagVersionSpec)
gen_esmodel_versioning_DateVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_DateVersionSpec)
gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_PrimaryVersionSpec)
gen_esmodel_versioning_HeadVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_HeadVersionSpec)
gen_esmodel_operations_AbstractOperation_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_operations_AbstractOperation)
gen_esmodel_operations_CompositeOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CompositeOperation)
gen_esmodel_operations_FeatureOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_FeatureOperation)
gen_esmodel_operations_CreateDeleteOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CreateDeleteOperation)
gen_esmodel_operations_AttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_AttributeOperation)
gen_esmodel_operations_MultiAttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeOperation)
gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeMoveOperation)
gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_SingleReferenceOperation)
gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceSetOperation)
gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceOperation)
gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiReferenceMoveOperation)
gen_esmodel_operations_ReferenceOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_ReferenceOperation)
gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation = Generalization(general=AttributeOperation, specific=esmodel_operations_DiagramLayoutOperation)
gen_esmodel_operations_OperationId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_operations_OperationId)
gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeSetOperation)
gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation = Generalization(general=CompositeOperation, specific=esmodel_semantic_SemanticCompositeOperation)
gen_esmodel_events_ReadEvent_Event = Generalization(general=Event, specific=esmodel_events_ReadEvent)
gen_esmodel_events_MergeEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeEvent)
gen_esmodel_events_CheckoutEvent_Event = Generalization(general=Event, specific=esmodel_events_CheckoutEvent)
gen_esmodel_events_ExceptionEvent_Event = Generalization(general=Event, specific=esmodel_events_ExceptionEvent)
gen_esmodel_events_PluginStartEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginStartEvent)
gen_esmodel_events_AnnotationEvent_Event = Generalization(general=Event, specific=esmodel_events_AnnotationEvent)
gen_esmodel_events_RevertEvent_Event = Generalization(general=Event, specific=esmodel_events_RevertEvent)
gen_esmodel_events_UpdateEvent_Event = Generalization(general=Event, specific=esmodel_events_UpdateEvent)
gen_esmodel_events_ShowHistoryEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowHistoryEvent)
gen_esmodel_events_PerspectiveEvent_Event = Generalization(general=Event, specific=esmodel_events_PerspectiveEvent)
gen_esmodel_events_DNDEvent_Event = Generalization(general=Event, specific=esmodel_events_DNDEvent)
gen_esmodel_events_LinkEvent_Event = Generalization(general=Event, specific=esmodel_events_LinkEvent)
gen_esmodel_events_TraceEvent_Event = Generalization(general=Event, specific=esmodel_events_TraceEvent)
gen_esmodel_events_NavigatorCreateEvent_Event = Generalization(general=Event, specific=esmodel_events_NavigatorCreateEvent)
gen_esmodel_events_PluginFocusEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginFocusEvent)
gen_esmodel_events_PresentationSwitchEvent_Event = Generalization(general=Event, specific=esmodel_events_PresentationSwitchEvent)
gen_esmodel_events_UndoEvent_Event = Generalization(general=Event, specific=esmodel_events_UndoEvent)
gen_esmodel_events_Validate_Event = Generalization(general=Event, specific=esmodel_events_Validate)
gen_esmodel_events_ShowChangesEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowChangesEvent)
gen_esmodel_events_NotificationReadEvent_ReadEvent = Generalization(general=ReadEvent, specific=esmodel_events_NotificationReadEvent)
gen_esmodel_events_NotificationGenerationEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationGenerationEvent)
gen_esmodel_server_ServerEvent_Event = Generalization(general=Event, specific=esmodel_server_ServerEvent)
gen_esmodel_events_NotificationIgnoreEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationIgnoreEvent)
gen_esmodel_server_ServerProjectEvent_ServerEvent = Generalization(general=ServerEvent, specific=esmodel_server_ServerProjectEvent)
gen_esmodel_events_URLEvent_Event = Generalization(general=Event, specific=esmodel_events_URLEvent)
gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent = Generalization(general=ServerProjectEvent, specific=esmodel_server_ProjectUpdatedEvent)
gen_esmodel_accesscontrol_ACUser_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACUser)
gen_esmodel_events_MergeChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeChoiceEvent)
gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_accesscontrol_ACOrgUnit)
gen_esmodel_events_MergeGlobalChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeGlobalChoiceEvent)
gen_esmodel_roles_ReaderRole_Role = Generalization(general=Role, specific=esmodel_roles_ReaderRole)
gen_esmodel_accesscontrol_ACGroup_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACGroup)
gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_accesscontrol_ACOrgUnitId)
gen_esmodel_roles_WriterRole_Role = Generalization(general=Role, specific=esmodel_roles_WriterRole)
gen_esmodel_roles_ProjectAdminRole_Role = Generalization(general=Role, specific=esmodel_roles_ProjectAdminRole)
gen_esmodel_roles_ServerAdmin_Role = Generalization(general=Role, specific=esmodel_roles_ServerAdmin)
gen_esmodel_notification_ESNotification_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_notification_ESNotification)

# Domain Model
domain_model = DomainModel(
    name="esmodel",
    types={model_UnicaseModelElement, Annotation, Attachment, document_LeafSection, metamodel_Project, ModelElement, metamodel_UniqueIdentifier, metamodel_IdentifiableElement, metamodel_ModelElement, IdentifiableElement, metamodel_ModelElementId, UniqueIdentifier, metamodel_ModelVersion, metamodel_NonDomainElement, metamodel_AssociationClassElement, model_organization_OrgUnit, organization_Group, task_WorkItem, model_organization_User, OrgUnit, rationale_Comment, profile_StereotypeInstance, model_Annotation, UnicaseModelElement, model_Attachment, model_NonDomainElement, model_Project, Project, change_ModelChangePackage, model_task_WorkPackage, WorkItem, model_organization_Group, organization_OrgUnit, model_task_WorkItem, task_WorkPackage, organization_User, task_Checkable, model_diagram_MEDiagram, diagram_model_Diagram, model_task_Milestone, model_task_Checkable, model_task_ActionItem, classes_Class, classes_Association, classes_Attribute, classes_Method, requirement_UseCase, model_classes_PackageElement, requirement_Scenario, classes_Package, classes_Dependency, model_classes_Class, PackageElement, model_classes_Attribute, model_classes_Package, classes_PackageElement, model_classes_Association, model_classes_Method, model_classes_MethodArgument, model_classes_Dependency, classes_MethodArgument, model_document_CompositeSection, document_Section, model_requirement_FunctionalRequirement, requirement_FunctionalRequirement, model_document_Section, document_CompositeSection, model_document_LeafSection, Section, model_requirement_UseCase, requirement_Actor, requirement_NonFunctionalRequirement, model_requirement_Scenario, requirement_Step, requirement_UserTask, model_requirement_Actor, model_requirement_ActorInstance, requirement_ActorInstance, model_requirement_Step, NonDomainElement, requirement_SystemFunction, model_requirement_SystemFunction, model_requirement_UserTask, model_requirement_NonFunctionalRequirement, Criterion, model_rationale_Issue, rationale_Solution, rationale_Criterion, model_rationale_Proposal, rationale_Issue, rationale_Assessment, model_rationale_Solution, model_rationale_Criterion, model_rationale_Assessment, rationale_Proposal, model_rationale_Comment, model_change_ModelChangePackage, model_change_MergingIssue, Issue, model_change_MergingProposal, Proposal, change_MergingProposal, model_change_MergingSolution, Solution, model_bug_BugReport, model_component_Component, component_ComponentService, model_component_ComponentService, component_Component, model_component_DeploymentNode, model_meeting_Meeting, meeting_MeetingSection, meeting_IssueMeetingSection, meeting_WorkItemMeetingSection, model_meeting_MeetingSection, model_meeting_CompositeMeetingSection, MeetingSection, model_meeting_IssueMeetingSection, model_state_Transition, state_StateNode, model_state_StateNode, state_Transition, model_state_State, StateNode, model_state_StateInitial, model_state_StateEnd, model_attachment_UrlAttachment, model_attachment_FileAttachment, model_meeting_WorkItemMeetingSection, profile_Stereotype, model_profile_Stereotype, profile_Profile, profile_StereotypeAttribute, model_profile_StereotypeInstance, profile_StereotypeAttributeInstance, model_profile_StereotypeAttribute, model_profile_StereotypeAttributeSimple, StereotypeAttribute, model_profile_StereotypeAttributeInstance, model_profile_Profile, model_profile_StereotypeAttributeInstanceString, StereotypeAttributeInstance, model_util_ModelElementPath, ModelElementId, model_activity_ActivityObject, activity_Transition, model_activity_Transition, activity_ActivityObject, model_activity_Activity, ActivityObject, model_activity_Fork, model_activity_Branch, model_activity_ActivityInitial, model_activity_ActivityEnd, esmodel_ProjectHistory, ProjectId, versioning_Version, esmodel_ProjectInfo, versioning_PrimaryVersionSpec, esmodel_SessionId, esmodel_ServerSpace, accesscontrol_ACGroup, ProjectHistory, SessionId, accesscontrol_ACUser, esmodel_ProjectId, esmodel_VersionInfo, esmodel_ClientVersionInfo, esmodel_versioning_TagVersionSpec, VersionSpec, esmodel_versioning_DateVersionSpec, esmodel_versioning_PrimaryVersionSpec, esmodel_versioning_ChangePackage, operations_AbstractOperation, events_Event, versioning_LogMessage, notification_ESNotification, versioning_VersionProperty, esmodel_versioning_HistoryInfo, versioning_TagVersionSpec, versioning_ChangePackage, esmodel_versioning_HistoryQuery, esmodel_versioning_Version, esmodel_versioning_HeadVersionSpec, esmodel_versioning_VersionSpec, esmodel_versioning_VersionProperty, esmodel_versioning_LogMessage, esmodel_operations_AbstractOperation, esmodel_operations_CompositeOperation, AbstractOperation, esmodel_operations_FeatureOperation, esmodel_operations_CreateDeleteOperation, operations_esmodel_EObject, operations_ReferenceOperation, operations_EObjectToModelElementIdMap, esmodel_operations_AttributeOperation, FeatureOperation, esmodel_operations_MultiAttributeOperation, esmodel_operations_MultiAttributeMoveOperation, esmodel_operations_SingleReferenceOperation, ReferenceOperation, esmodel_operations_MultiReferenceSetOperation, esmodel_operations_MultiReferenceOperation, esmodel_operations_MultiReferenceMoveOperation, esmodel_operations_ReferenceOperation, esmodel_operations_DiagramLayoutOperation, AttributeOperation, esmodel_operations_OperationId, esmodel_operations_OperationGroup, esmodel_operations_MultiAttributeSetOperation, esmodel_operations_EObjectToModelElementIdMap, esmodel_semantic_SemanticCompositeOperation, CompositeOperation, esmodel_events_Event, esmodel_events_ReadEvent, Event, esmodel_events_MergeEvent, esmodel_events_CheckoutEvent, esmodel_events_ExceptionEvent, esmodel_events_PluginStartEvent, esmodel_operations_ModelElementGroup, esmodel_events_AnnotationEvent, esmodel_events_RevertEvent, esmodel_events_UpdateEvent, esmodel_events_ShowHistoryEvent, esmodel_events_PerspectiveEvent, esmodel_events_DNDEvent, esmodel_events_LinkEvent, esmodel_events_TraceEvent, esmodel_events_NavigatorCreateEvent, esmodel_events_PluginFocusEvent, esmodel_events_PresentationSwitchEvent, esmodel_events_UndoEvent, esmodel_events_Validate, esmodel_events_ShowChangesEvent, esmodel_events_NotificationReadEvent, ReadEvent, esmodel_events_NotificationGenerationEvent, esmodel_server_ServerEvent, esmodel_events_NotificationIgnoreEvent, esmodel_server_ServerProjectEvent, ServerEvent, esmodel_events_URLEvent, esmodel_server_ProjectUpdatedEvent, ServerProjectEvent, esmodel_accesscontrol_ACUser, ACOrgUnit, esmodel_events_MergeChoiceEvent, operations_OperationId, esmodel_accesscontrol_ACOrgUnit, esmodel_events_MergeGlobalChoiceEvent, esmodel_roles_Role, esmodel_roles_ReaderRole, Role, esmodel_roles_WriterRole, roles_Role, accesscontrol_OrgUnitProperty, esmodel_accesscontrol_ACGroup, accesscontrol_ACOrgUnit, esmodel_accesscontrol_ACOrgUnitId, esmodel_accesscontrol_OrgUnitProperty, esmodel_url_ServerUrl, esmodel_url_ProjectUrlFragment, esmodel_url_ModelElementUrlFragment, esmodel_roles_ProjectAdminRole, esmodel_roles_ServerAdmin, esmodel_notification_ESNotification, esmodel_url_ModelElementUrl, url_ServerUrl, url_ProjectUrlFragment, url_ModelElementUrlFragment, ActivityType, DiagramType, AssociationType, VisibilityType, ScopeType, ArgumentDirectionType, BugStatus, Severity, ResolutionType, ContainmentType, MergeChoiceSelection, MergeGlobalChoiceSelection},
    associations={annotations4, attachments5, leafSection6, incomingDocumentReferences7, modelElements0, cutElements1, groupMemberships14, participations15, assignments16, workItemsToReview18, comments9, appliedStereotypeInstances10, annotatedModelElements11, referringModelElements12, participants29, associatedChangePackages31, orgUnits20, containingWorkpackage21, successors22, predecessors24, assignee26, reviewer28, elements36, gmfdiagram38, newElements40, containedWorkItems32, containedModelElements34, subClasses47, superClasses48, outgoingAssociations50, incomingAssociations52, attributes55, methods56, participatedUseCases58, demoParticipations59, parentPackage43, outgoingDependencies44, incomingDependencies45, source62, target64, definingClass66, facadeClass60, containedPackageElements61, definingClass68, arguments74, demoParticipations75, source77, target79, calledMethods70, callingMethods72, referencedModelElements84, subsections86, refiningRequirements87, refinedRequirement88, stakeholder90, parent81, modelElements82, functionalRequirements96, identifiedClasses98, includedUseCases100, extendedUseCases101, scenarios104, initiatingActor106, participatingActors107, useCases91, scenarios93, realizedUserTask111, nonFunctionalRequirements112, instantiatedUseCases113, functionalRequirements115, participatingMethods118, useCaseSteps110, steps126, nonFunctionalRequirements127, initiatedUseCases129, participatedUseCases131, instances133, participatedUserTasks135, initiatedUserTask137, initiatedScenarios140, participatingClasses120, initiatingActorInstance123, participatingActorInstances124, includedUseCase146, useCase148, includedSystemFunction150, initiatingActor152, participatingActor154, realizingUseCases156, restrictedUseCases158, restrictedScenarios160, participatedScenarios142, instantiatedActor144, solution164, criteria166, issue167, assessments168, underlyingProposals169, issue170, assessments172, proposals163, sender178, recipients180, commentedElement183, conflictingProposals185, pendingChanges186, appliedChanges189, proposal174, criterion176, packages191, subsystems192, offeredServices195, consumedServices196, offeringComponent198, consumingComponents199, components201, facilitator202, minutetaker203, timekeeper206, participants209, sections212, identifiedIssuesSection214, identifiedWorkItemsSection216, subsections218, includedIssues220, includedWorkItems221, source222, target223, outgoingTransitions225, incomingTransitions227, stereotypes232, profile233, stereotypeInstances234, stereotypeAttributes236, stereotype238, modelElement240, stereotypeAttributeInstances242, stereotype243, stereotypeAttributeInstances245, stereotypeInstance247, affectedContainers230, source252, target253, path256, outgoingTransitions259, incomingTransitions262, source265, target267, projectId270, versions271, stereotypeAttribute249, projectId273, version275, groups277, projects278, openSessions280, users282, operations284, events285, logMessage287, notifications289, versionProperties291, primerySpec293, logMessage295, tagSpecs298, versionProperties300, changePackage303, source305, target307, modelElements310, projectState313, primarySpec314, tagSpecs317, nextVersion320, previousVersion321, changes323, logMessage326, modelElementId329, subOperations331, mainOperation333, modelElement336, subOperations337, eObjectToIdMap339, oldValue341, newValue343, oldValue346, newValue348, referencedModelElements351, referencedModelElementId353, operations355, key359, value361, modelElement364, baseVersion366, targetVersion368, localChanges371, baseVersion374, modelElements357, baseVersion376, targetVersion378, annotatedElement381, annotation383, sourceVersion386, targetVersion388, modelElement391, dragSourceElement394, dropTargetElement396, sourceElement399, targetElement401, sourceElement404, targetElement406, createdElement409, sourceSection411, operation414, sourceVersion416, targetVersion418, projectId435, sourceModelElement423, newVersion437, sourceURL425, myAcceptedChanges428, theirRejectedChanges429, contextModelElement432, notifications421, project443, projects445, roles439, properties440, members442, project447, relatedModelElements449, relatedOperations452, projectId455, modelElementId457, serverUrl459, projectUrlFragment460, modelElementUrlFragment462},
    generalizations={gen_model_UnicaseModelElement_ModelElement, gen_metamodel_ModelElement_IdentifiableElement, gen_metamodel_ModelElementId_UniqueIdentifier, gen_model_organization_OrgUnit_UnicaseModelElement, gen_model_organization_User_OrgUnit, gen_model_Annotation_UnicaseModelElement, gen_model_Attachment_UnicaseModelElement, gen_model_Project_Project, gen_model_task_WorkPackage_WorkItem, gen_model_organization_Group_OrgUnit, gen_model_task_WorkItem_Annotation, gen_model_task_ActionItem_task_Checkable, gen_model_diagram_MEDiagram_Attachment, gen_model_task_Milestone_WorkItem, gen_model_task_Checkable_UnicaseModelElement, gen_model_task_ActionItem_task_WorkItem, gen_model_classes_PackageElement_UnicaseModelElement, gen_model_classes_Class_PackageElement, gen_model_classes_Association_UnicaseModelElement, gen_model_classes_Attribute_UnicaseModelElement, gen_model_classes_Package_PackageElement, gen_model_classes_Method_UnicaseModelElement, gen_model_classes_MethodArgument_UnicaseModelElement, gen_model_classes_Dependency_UnicaseModelElement, gen_model_document_CompositeSection_Section, gen_model_requirement_FunctionalRequirement_UnicaseModelElement, gen_model_document_Section_UnicaseModelElement, gen_model_document_LeafSection_Section, gen_model_requirement_UseCase_UnicaseModelElement, gen_model_requirement_Scenario_UnicaseModelElement, gen_model_requirement_Actor_UnicaseModelElement, gen_model_requirement_ActorInstance_UnicaseModelElement, gen_model_requirement_Step_UnicaseModelElement, gen_model_requirement_Step_NonDomainElement, gen_model_requirement_SystemFunction_UnicaseModelElement, gen_model_requirement_SystemFunction_NonDomainElement, gen_model_requirement_UserTask_UnicaseModelElement, gen_model_requirement_UserTask_NonDomainElement, gen_model_requirement_NonFunctionalRequirement_Criterion, gen_model_rationale_Issue_Annotation, gen_model_rationale_Issue_task_Checkable, gen_model_rationale_Issue_task_WorkItem, gen_model_rationale_Proposal_UnicaseModelElement, gen_model_rationale_Proposal_NonDomainElement, gen_model_rationale_Solution_UnicaseModelElement, gen_model_rationale_Solution_NonDomainElement, gen_model_rationale_Criterion_UnicaseModelElement, gen_model_rationale_Assessment_UnicaseModelElement, gen_model_rationale_Assessment_NonDomainElement, gen_model_rationale_Comment_UnicaseModelElement, gen_model_change_ModelChangePackage_UnicaseModelElement, gen_model_change_MergingIssue_Issue, gen_model_change_MergingProposal_Proposal, gen_model_change_MergingSolution_Solution, gen_model_bug_BugReport_task_WorkItem, gen_model_bug_BugReport_task_Checkable, gen_model_component_Component_UnicaseModelElement, gen_model_component_ComponentService_UnicaseModelElement, gen_model_component_DeploymentNode_UnicaseModelElement, gen_model_meeting_Meeting_UnicaseModelElement, gen_model_meeting_MeetingSection_UnicaseModelElement, gen_model_meeting_CompositeMeetingSection_MeetingSection, gen_model_meeting_IssueMeetingSection_MeetingSection, gen_model_state_Transition_UnicaseModelElement, gen_model_state_StateNode_UnicaseModelElement, gen_model_state_State_StateNode, gen_model_state_StateInitial_StateNode, gen_model_state_StateEnd_StateNode, gen_model_attachment_UrlAttachment_Attachment, gen_model_attachment_FileAttachment_Attachment, gen_model_meeting_WorkItemMeetingSection_MeetingSection, gen_model_profile_Stereotype_UnicaseModelElement, gen_model_profile_StereotypeInstance_UnicaseModelElement, gen_model_profile_StereotypeAttribute_UnicaseModelElement, gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute, gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement, gen_model_profile_Profile_UnicaseModelElement, gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance, gen_model_activity_ActivityObject_UnicaseModelElement, gen_model_activity_Transition_UnicaseModelElement, gen_model_activity_Activity_ActivityObject, gen_model_activity_Fork_ActivityObject, gen_model_activity_Branch_ActivityObject, gen_model_activity_ActivityInitial_ActivityObject, gen_model_activity_ActivityEnd_ActivityObject, gen_esmodel_SessionId_UniqueIdentifier, gen_esmodel_ProjectId_UniqueIdentifier, gen_esmodel_versioning_TagVersionSpec_VersionSpec, gen_esmodel_versioning_DateVersionSpec_VersionSpec, gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec, gen_esmodel_versioning_HeadVersionSpec_VersionSpec, gen_esmodel_operations_AbstractOperation_IdentifiableElement, gen_esmodel_operations_CompositeOperation_AbstractOperation, gen_esmodel_operations_FeatureOperation_AbstractOperation, gen_esmodel_operations_CreateDeleteOperation_AbstractOperation, gen_esmodel_operations_AttributeOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation, gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation, gen_esmodel_operations_ReferenceOperation_FeatureOperation, gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation, gen_esmodel_operations_OperationId_UniqueIdentifier, gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation, gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation, gen_esmodel_events_ReadEvent_Event, gen_esmodel_events_MergeEvent_Event, gen_esmodel_events_CheckoutEvent_Event, gen_esmodel_events_ExceptionEvent_Event, gen_esmodel_events_PluginStartEvent_Event, gen_esmodel_events_AnnotationEvent_Event, gen_esmodel_events_RevertEvent_Event, gen_esmodel_events_UpdateEvent_Event, gen_esmodel_events_ShowHistoryEvent_Event, gen_esmodel_events_PerspectiveEvent_Event, gen_esmodel_events_DNDEvent_Event, gen_esmodel_events_LinkEvent_Event, gen_esmodel_events_TraceEvent_Event, gen_esmodel_events_NavigatorCreateEvent_Event, gen_esmodel_events_PluginFocusEvent_Event, gen_esmodel_events_PresentationSwitchEvent_Event, gen_esmodel_events_UndoEvent_Event, gen_esmodel_events_Validate_Event, gen_esmodel_events_ShowChangesEvent_Event, gen_esmodel_events_NotificationReadEvent_ReadEvent, gen_esmodel_events_NotificationGenerationEvent_Event, gen_esmodel_server_ServerEvent_Event, gen_esmodel_events_NotificationIgnoreEvent_Event, gen_esmodel_server_ServerProjectEvent_ServerEvent, gen_esmodel_events_URLEvent_Event, gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent, gen_esmodel_accesscontrol_ACUser_ACOrgUnit, gen_esmodel_events_MergeChoiceEvent_Event, gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement, gen_esmodel_events_MergeGlobalChoiceEvent_Event, gen_esmodel_roles_ReaderRole_Role, gen_esmodel_accesscontrol_ACGroup_ACOrgUnit, gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier, gen_esmodel_roles_WriterRole_Role, gen_esmodel_roles_ProjectAdminRole_Role, gen_esmodel_roles_ServerAdmin_Role, gen_esmodel_notification_ESNotification_IdentifiableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)