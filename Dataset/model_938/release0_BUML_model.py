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
			EnumerationLiteral(name="ASSIGNED"),
			EnumerationLiteral(name="RESOLVED"),
			EnumerationLiteral(name="CLOSED")
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
metamodel_Project = Class(name="metamodel::Project")
ModelElement = Class(name="ModelElement")
metamodel_ModelElement = Class(name="metamodel::ModelElement", is_abstract=True)
IdentifiableElement = Class(name="IdentifiableElement")
metamodel_ModelElementId = Class(name="metamodel::ModelElementId")
UniqueIdentifier = Class(name="UniqueIdentifier")
metamodel_ModelVersion = Class(name="metamodel::ModelVersion")
metamodel_NonDomainElement = Class(name="metamodel::NonDomainElement", is_abstract=True)
metamodel_AssociationClassElement = Class(name="metamodel::AssociationClassElement", is_abstract=True)
model_UnicaseModelElement = Class(name="model::UnicaseModelElement", is_abstract=True)
Annotation = Class(name="Annotation")
Attachment = Class(name="Attachment")
document_LeafSection = Class(name="document::LeafSection")
metamodel_UniqueIdentifier = Class(name="metamodel::UniqueIdentifier", is_abstract=True)
metamodel_IdentifiableElement = Class(name="metamodel::IdentifiableElement", is_abstract=True)
model_Annotation = Class(name="model::Annotation", is_abstract=True)
UnicaseModelElement = Class(name="UnicaseModelElement")
model_Attachment = Class(name="model::Attachment", is_abstract=True)
model_NonDomainElement = Class(name="model::NonDomainElement", is_abstract=True)
model_Project = Class(name="model::Project")
Project = Class(name="Project")
model_organization_OrgUnit = Class(name="model::organization::OrgUnit", is_abstract=True)
organization_Group = Class(name="organization::Group")
task_WorkItem = Class(name="task::WorkItem")
model_organization_User = Class(name="model::organization::User")
OrgUnit = Class(name="OrgUnit")
rationale_Comment = Class(name="rationale::Comment")
profile_StereotypeInstance = Class(name="profile::StereotypeInstance")
model_task_WorkItem = Class(name="model::task::WorkItem", is_abstract=True)
task_WorkPackage = Class(name="task::WorkPackage")
organization_User = Class(name="organization::User")
model_organization_Group = Class(name="model::organization::Group")
organization_OrgUnit = Class(name="organization::OrgUnit")
change_ModelChangePackage = Class(name="change::ModelChangePackage")
model_task_WorkPackage = Class(name="model::task::WorkPackage")
WorkItem = Class(name="WorkItem")
model_task_Milestone = Class(name="model::task::Milestone")
model_task_Checkable = Class(name="model::task::Checkable", is_abstract=True)
model_task_ActionItem = Class(name="model::task::ActionItem")
task_Checkable = Class(name="task::Checkable")
model_diagram_MEDiagram = Class(name="model::diagram::MEDiagram")
diagram_model_Diagram = Class(name="diagram::model::Diagram")
model_classes_PackageElement = Class(name="model::classes::PackageElement", is_abstract=True)
classes_Package = Class(name="classes::Package")
classes_Dependency = Class(name="classes::Dependency")
model_classes_Class = Class(name="model::classes::Class")
PackageElement = Class(name="PackageElement")
classes_Class = Class(name="classes::Class")
classes_Association = Class(name="classes::Association")
classes_Attribute = Class(name="classes::Attribute")
classes_Method = Class(name="classes::Method")
requirement_UseCase = Class(name="requirement::UseCase")
requirement_Scenario = Class(name="requirement::Scenario")
model_classes_Package = Class(name="model::classes::Package")
model_classes_Association = Class(name="model::classes::Association")
model_classes_Attribute = Class(name="model::classes::Attribute")
classes_PackageElement = Class(name="classes::PackageElement")
classes_MethodArgument = Class(name="classes::MethodArgument")
model_classes_MethodArgument = Class(name="model::classes::MethodArgument")
model_classes_Method = Class(name="model::classes::Method")
model_document_Section = Class(name="model::document::Section", is_abstract=True)
document_CompositeSection = Class(name="document::CompositeSection")
model_classes_Dependency = Class(name="model::classes::Dependency")
model_document_CompositeSection = Class(name="model::document::CompositeSection")
model_document_LeafSection = Class(name="model::document::LeafSection")
Section = Class(name="Section")
document_Section = Class(name="document::Section")
model_requirement_FunctionalRequirement = Class(name="model::requirement::FunctionalRequirement")
requirement_FunctionalRequirement = Class(name="requirement::FunctionalRequirement")
requirement_Actor = Class(name="requirement::Actor")
model_requirement_UseCase = Class(name="model::requirement::UseCase")
model_requirement_Scenario = Class(name="model::requirement::Scenario")
requirement_Step = Class(name="requirement::Step")
requirement_UserTask = Class(name="requirement::UserTask")
requirement_NonFunctionalRequirement = Class(name="requirement::NonFunctionalRequirement")
model_requirement_Actor = Class(name="model::requirement::Actor")
requirement_ActorInstance = Class(name="requirement::ActorInstance")
requirement_SystemFunction = Class(name="requirement::SystemFunction")
model_requirement_SystemFunction = Class(name="model::requirement::SystemFunction")
model_requirement_UserTask = Class(name="model::requirement::UserTask")
model_requirement_ActorInstance = Class(name="model::requirement::ActorInstance")
model_requirement_Step = Class(name="model::requirement::Step")
NonDomainElement = Class(name="NonDomainElement")
rationale_Proposal = Class(name="rationale::Proposal")
rationale_Solution = Class(name="rationale::Solution")
rationale_Criterion = Class(name="rationale::Criterion")
model_rationale_Proposal = Class(name="model::rationale::Proposal")
rationale_Issue = Class(name="rationale::Issue")
model_requirement_NonFunctionalRequirement = Class(name="model::requirement::NonFunctionalRequirement")
Criterion = Class(name="Criterion")
model_rationale_Issue = Class(name="model::rationale::Issue")
model_rationale_Comment = Class(name="model::rationale::Comment")
rationale_Assessment = Class(name="rationale::Assessment")
model_rationale_Solution = Class(name="model::rationale::Solution")
model_rationale_Criterion = Class(name="model::rationale::Criterion")
model_rationale_Assessment = Class(name="model::rationale::Assessment")
model_change_ModelChangePackage = Class(name="model::change::ModelChangePackage")
model_change_MergingIssue = Class(name="model::change::MergingIssue")
Issue = Class(name="Issue")
model_change_MergingProposal = Class(name="model::change::MergingProposal")
Proposal = Class(name="Proposal")
change_MergingProposal = Class(name="change::MergingProposal")
model_change_MergingSolution = Class(name="model::change::MergingSolution")
Solution = Class(name="Solution")
model_bug_BugReport = Class(name="model::bug::BugReport")
model_meeting_Meeting = Class(name="model::meeting::Meeting")
model_component_Component = Class(name="model::component::Component")
component_ComponentService = Class(name="component::ComponentService")
model_component_ComponentService = Class(name="model::component::ComponentService")
component_Component = Class(name="component::Component")
model_component_DeploymentNode = Class(name="model::component::DeploymentNode")
model_meeting_MeetingSection = Class(name="model::meeting::MeetingSection", is_abstract=True)
model_meeting_CompositeMeetingSection = Class(name="model::meeting::CompositeMeetingSection")
MeetingSection = Class(name="MeetingSection")
model_meeting_IssueMeetingSection = Class(name="model::meeting::IssueMeetingSection")
model_meeting_WorkItemMeetingSection = Class(name="model::meeting::WorkItemMeetingSection")
meeting_MeetingSection = Class(name="meeting::MeetingSection")
meeting_IssueMeetingSection = Class(name="meeting::IssueMeetingSection")
meeting_WorkItemMeetingSection = Class(name="meeting::WorkItemMeetingSection")
model_state_StateInitial = Class(name="model::state::StateInitial")
model_state_StateEnd = Class(name="model::state::StateEnd")
model_attachment_UrlAttachment = Class(name="model::attachment::UrlAttachment")
model_attachment_FileAttachment = Class(name="model::attachment::FileAttachment")
model_state_Transition = Class(name="model::state::Transition")
state_StateNode = Class(name="state::StateNode")
model_state_StateNode = Class(name="model::state::StateNode", is_abstract=True)
state_Transition = Class(name="state::Transition")
model_state_State = Class(name="model::state::State")
StateNode = Class(name="StateNode")
model_profile_Stereotype = Class(name="model::profile::Stereotype")
profile_Profile = Class(name="profile::Profile")
profile_StereotypeAttribute = Class(name="profile::StereotypeAttribute")
model_profile_StereotypeInstance = Class(name="model::profile::StereotypeInstance")
model_profile_Profile = Class(name="model::profile::Profile")
profile_Stereotype = Class(name="profile::Stereotype")
model_profile_StereotypeAttributeSimple = Class(name="model::profile::StereotypeAttributeSimple")
StereotypeAttribute = Class(name="StereotypeAttribute")
model_profile_StereotypeAttributeInstance = Class(name="model::profile::StereotypeAttributeInstance", is_abstract=True)
model_profile_StereotypeAttributeInstanceString = Class(name="model::profile::StereotypeAttributeInstanceString")
StereotypeAttributeInstance = Class(name="StereotypeAttributeInstance")
model_util_ModelElementPath = Class(name="model::util::ModelElementPath")
profile_StereotypeAttributeInstance = Class(name="profile::StereotypeAttributeInstance")
model_profile_StereotypeAttribute = Class(name="model::profile::StereotypeAttribute", is_abstract=True)
model_activity_Activity = Class(name="model::activity::Activity")
ActivityObject = Class(name="ActivityObject")
model_activity_Fork = Class(name="model::activity::Fork")
model_activity_Branch = Class(name="model::activity::Branch")
model_activity_ActivityInitial = Class(name="model::activity::ActivityInitial")
model_activity_ActivityEnd = Class(name="model::activity::ActivityEnd")
esmodel_ProjectHistory = Class(name="esmodel::ProjectHistory")
ProjectId = Class(name="ProjectId")
versioning_Version = Class(name="versioning::Version")
esmodel_ProjectInfo = Class(name="esmodel::ProjectInfo")
ModelElementId = Class(name="ModelElementId")
model_activity_ActivityObject = Class(name="model::activity::ActivityObject", is_abstract=True)
activity_Transition = Class(name="activity::Transition")
model_activity_Transition = Class(name="model::activity::Transition")
activity_ActivityObject = Class(name="activity::ActivityObject")
esmodel_FileIdentifier = Class(name="esmodel::FileIdentifier")
esmodel_versioning_TagVersionSpec = Class(name="esmodel::versioning::TagVersionSpec")
VersionSpec = Class(name="VersionSpec")
esmodel_versioning_DateVersionSpec = Class(name="esmodel::versioning::DateVersionSpec")
esmodel_versioning_PrimaryVersionSpec = Class(name="esmodel::versioning::PrimaryVersionSpec")
esmodel_versioning_VersionSpec = Class(name="esmodel::versioning::VersionSpec", is_abstract=True)
esmodel_versioning_LogMessage = Class(name="esmodel::versioning::LogMessage")
esmodel_versioning_ChangePackage = Class(name="esmodel::versioning::ChangePackage")
operations_AbstractOperation = Class(name="operations::AbstractOperation")
versioning_PrimaryVersionSpec = Class(name="versioning::PrimaryVersionSpec")
esmodel_SessionId = Class(name="esmodel::SessionId")
esmodel_ServerSpace = Class(name="esmodel::ServerSpace")
accesscontrol_ACGroup = Class(name="accesscontrol::ACGroup")
ProjectHistory = Class(name="ProjectHistory")
SessionId = Class(name="SessionId")
accesscontrol_ACUser = Class(name="accesscontrol::ACUser")
esmodel_ProjectId = Class(name="esmodel::ProjectId")
esmodel_VersionInfo = Class(name="esmodel::VersionInfo")
esmodel_ClientVersionInfo = Class(name="esmodel::ClientVersionInfo")
esmodel_versioning_HistoryQuery = Class(name="esmodel::versioning::HistoryQuery")
esmodel_versioning_Version = Class(name="esmodel::versioning::Version")
events_Event = Class(name="events::Event")
versioning_LogMessage = Class(name="versioning::LogMessage")
notification_ESNotification = Class(name="notification::ESNotification")
versioning_VersionProperty = Class(name="versioning::VersionProperty")
esmodel_versioning_HistoryInfo = Class(name="esmodel::versioning::HistoryInfo")
versioning_TagVersionSpec = Class(name="versioning::TagVersionSpec")
versioning_ChangePackage = Class(name="versioning::ChangePackage")
esmodel_operations_FeatureOperation = Class(name="esmodel::operations::FeatureOperation", is_abstract=True)
esmodel_operations_CreateDeleteOperation = Class(name="esmodel::operations::CreateDeleteOperation")
operations_esmodel_EObject = Class(name="operations::esmodel::EObject")
operations_ReferenceOperation = Class(name="operations::ReferenceOperation")
operations_EObjectToModelElementIdMap = Class(name="operations::EObjectToModelElementIdMap")
esmodel_operations_AttributeOperation = Class(name="esmodel::operations::AttributeOperation")
FeatureOperation = Class(name="FeatureOperation")
esmodel_versioning_HeadVersionSpec = Class(name="esmodel::versioning::HeadVersionSpec")
esmodel_versioning_VersionProperty = Class(name="esmodel::versioning::VersionProperty")
esmodel_operations_AbstractOperation = Class(name="esmodel::operations::AbstractOperation", is_abstract=True)
esmodel_operations_CompositeOperation = Class(name="esmodel::operations::CompositeOperation")
AbstractOperation = Class(name="AbstractOperation")
esmodel_operations_MultiAttributeOperation = Class(name="esmodel::operations::MultiAttributeOperation")
esmodel_operations_MultiAttributeSetOperation = Class(name="esmodel::operations::MultiAttributeSetOperation")
esmodel_operations_MultiAttributeMoveOperation = Class(name="esmodel::operations::MultiAttributeMoveOperation")
esmodel_operations_MultiReferenceMoveOperation = Class(name="esmodel::operations::MultiReferenceMoveOperation")
esmodel_operations_ReferenceOperation = Class(name="esmodel::operations::ReferenceOperation", is_abstract=True)
esmodel_operations_DiagramLayoutOperation = Class(name="esmodel::operations::DiagramLayoutOperation")
AttributeOperation = Class(name="AttributeOperation")
esmodel_operations_OperationId = Class(name="esmodel::operations::OperationId")
esmodel_operations_OperationGroup = Class(name="esmodel::operations::OperationGroup")
esmodel_operations_ModelElementGroup = Class(name="esmodel::operations::ModelElementGroup")
esmodel_operations_SingleReferenceOperation = Class(name="esmodel::operations::SingleReferenceOperation")
ReferenceOperation = Class(name="ReferenceOperation")
esmodel_operations_MultiReferenceSetOperation = Class(name="esmodel::operations::MultiReferenceSetOperation")
esmodel_operations_MultiReferenceOperation = Class(name="esmodel::operations::MultiReferenceOperation")
esmodel_events_MergeEvent = Class(name="esmodel::events::MergeEvent")
esmodel_events_CheckoutEvent = Class(name="esmodel::events::CheckoutEvent")
esmodel_events_ExceptionEvent = Class(name="esmodel::events::ExceptionEvent")
esmodel_events_PluginStartEvent = Class(name="esmodel::events::PluginStartEvent")
esmodel_operations_EObjectToModelElementIdMap = Class(name="esmodel::operations::EObjectToModelElementIdMap")
esmodel_semantic_SemanticCompositeOperation = Class(name="esmodel::semantic::SemanticCompositeOperation", is_abstract=True)
CompositeOperation = Class(name="CompositeOperation")
esmodel_events_Event = Class(name="esmodel::events::Event")
esmodel_events_ReadEvent = Class(name="esmodel::events::ReadEvent")
Event = Class(name="Event")
esmodel_events_PerspectiveEvent = Class(name="esmodel::events::PerspectiveEvent")
esmodel_events_DNDEvent = Class(name="esmodel::events::DNDEvent")
esmodel_events_LinkEvent = Class(name="esmodel::events::LinkEvent")
esmodel_events_UpdateEvent = Class(name="esmodel::events::UpdateEvent")
esmodel_events_AnnotationEvent = Class(name="esmodel::events::AnnotationEvent")
esmodel_events_RevertEvent = Class(name="esmodel::events::RevertEvent")
esmodel_events_ShowHistoryEvent = Class(name="esmodel::events::ShowHistoryEvent")
esmodel_events_UndoEvent = Class(name="esmodel::events::UndoEvent")
esmodel_events_Validate = Class(name="esmodel::events::Validate")
esmodel_events_ShowChangesEvent = Class(name="esmodel::events::ShowChangesEvent")
esmodel_events_NotificationReadEvent = Class(name="esmodel::events::NotificationReadEvent")
ReadEvent = Class(name="ReadEvent")
esmodel_events_NotificationGenerationEvent = Class(name="esmodel::events::NotificationGenerationEvent")
esmodel_events_NotificationIgnoreEvent = Class(name="esmodel::events::NotificationIgnoreEvent")
esmodel_events_TraceEvent = Class(name="esmodel::events::TraceEvent")
esmodel_events_NavigatorCreateEvent = Class(name="esmodel::events::NavigatorCreateEvent")
esmodel_events_PluginFocusEvent = Class(name="esmodel::events::PluginFocusEvent")
esmodel_events_PresentationSwitchEvent = Class(name="esmodel::events::PresentationSwitchEvent")
esmodel_events_MergeGlobalChoiceEvent = Class(name="esmodel::events::MergeGlobalChoiceEvent")
esmodel_server_ServerEvent = Class(name="esmodel::server::ServerEvent", is_abstract=True)
esmodel_server_ServerProjectEvent = Class(name="esmodel::server::ServerProjectEvent", is_abstract=True)
ServerEvent = Class(name="ServerEvent")
esmodel_server_ProjectUpdatedEvent = Class(name="esmodel::server::ProjectUpdatedEvent")
ServerProjectEvent = Class(name="ServerProjectEvent")
esmodel_events_URLEvent = Class(name="esmodel::events::URLEvent")
esmodel_events_MergeChoiceEvent = Class(name="esmodel::events::MergeChoiceEvent")
operations_OperationId = Class(name="operations::OperationId")
esmodel_accesscontrol_OrgUnitProperty = Class(name="esmodel::accesscontrol::OrgUnitProperty")
esmodel_roles_Role = Class(name="esmodel::roles::Role", is_abstract=True)
esmodel_accesscontrol_ACUser = Class(name="esmodel::accesscontrol::ACUser")
ACOrgUnit = Class(name="ACOrgUnit")
esmodel_accesscontrol_ACOrgUnit = Class(name="esmodel::accesscontrol::ACOrgUnit")
roles_Role = Class(name="roles::Role")
accesscontrol_OrgUnitProperty = Class(name="accesscontrol::OrgUnitProperty")
esmodel_accesscontrol_ACGroup = Class(name="esmodel::accesscontrol::ACGroup")
accesscontrol_ACOrgUnit = Class(name="accesscontrol::ACOrgUnit")
esmodel_accesscontrol_ACOrgUnitId = Class(name="esmodel::accesscontrol::ACOrgUnitId")
esmodel_url_ServerUrl = Class(name="esmodel::url::ServerUrl")
esmodel_url_ProjectUrlFragment = Class(name="esmodel::url::ProjectUrlFragment")
esmodel_url_ModelElementUrlFragment = Class(name="esmodel::url::ModelElementUrlFragment")
esmodel_url_ModelElementUrl = Class(name="esmodel::url::ModelElementUrl")
url_ServerUrl = Class(name="url::ServerUrl")
url_ProjectUrlFragment = Class(name="url::ProjectUrlFragment")
esmodel_roles_ReaderRole = Class(name="esmodel::roles::ReaderRole")
Role = Class(name="Role")
esmodel_roles_WriterRole = Class(name="esmodel::roles::WriterRole")
esmodel_roles_ProjectAdminRole = Class(name="esmodel::roles::ProjectAdminRole")
esmodel_roles_ServerAdmin = Class(name="esmodel::roles::ServerAdmin")
esmodel_notification_ESNotification = Class(name="esmodel::notification::ESNotification")
url_ModelElementUrlFragment = Class(name="url::ModelElementUrlFragment")

# metamodel_Project class attributes and methods

# ModelElement class attributes and methods

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
model_UnicaseModelElement_name: Property = Property(name="name", type=StringType)
model_UnicaseModelElement_description: Property = Property(name="description", type=StringType)
model_UnicaseModelElement_state: Property = Property(name="state", type=StringType)
model_UnicaseModelElement.attributes={model_UnicaseModelElement_description, model_UnicaseModelElement_name, model_UnicaseModelElement_state}

# Annotation class attributes and methods

# Attachment class attributes and methods

# document_LeafSection class attributes and methods

# metamodel_UniqueIdentifier class attributes and methods
metamodel_UniqueIdentifier_id: Property = Property(name="id", type=StringType)
metamodel_UniqueIdentifier.attributes={metamodel_UniqueIdentifier_id}

# metamodel_IdentifiableElement class attributes and methods
metamodel_IdentifiableElement_identifier: Property = Property(name="identifier", type=StringType)
metamodel_IdentifiableElement.attributes={metamodel_IdentifiableElement_identifier}

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

# task_WorkItem class attributes and methods

# model_organization_User class attributes and methods
model_organization_User_email: Property = Property(name="email", type=StringType)
model_organization_User_firstName: Property = Property(name="firstName", type=StringType)
model_organization_User_lastName: Property = Property(name="lastName", type=StringType)
model_organization_User.attributes={model_organization_User_email, model_organization_User_firstName, model_organization_User_lastName}

# OrgUnit class attributes and methods

# rationale_Comment class attributes and methods

# profile_StereotypeInstance class attributes and methods

# model_task_WorkItem class attributes and methods
model_task_WorkItem_dueDate: Property = Property(name="dueDate", type=DateType)
model_task_WorkItem_resolved: Property = Property(name="resolved", type=BooleanType)
model_task_WorkItem_estimate: Property = Property(name="estimate", type=IntegerType)
model_task_WorkItem_effort: Property = Property(name="effort", type=IntegerType)
model_task_WorkItem_priority: Property = Property(name="priority", type=IntegerType)
model_task_WorkItem.attributes={model_task_WorkItem_dueDate, model_task_WorkItem_resolved, model_task_WorkItem_estimate, model_task_WorkItem_effort, model_task_WorkItem_priority}

# task_WorkPackage class attributes and methods

# organization_User class attributes and methods

# model_organization_Group class attributes and methods

# organization_OrgUnit class attributes and methods

# change_ModelChangePackage class attributes and methods

# model_task_WorkPackage class attributes and methods
model_task_WorkPackage_startDate: Property = Property(name="startDate", type=DateType)
model_task_WorkPackage_endDate: Property = Property(name="endDate", type=DateType)
model_task_WorkPackage.attributes={model_task_WorkPackage_endDate, model_task_WorkPackage_startDate}

# WorkItem class attributes and methods

# model_task_Milestone class attributes and methods

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
model_diagram_MEDiagram.attributes={model_diagram_MEDiagram_type, model_diagram_MEDiagram_diagramLayout}

# diagram_model_Diagram class attributes and methods

# model_classes_PackageElement class attributes and methods

# classes_Package class attributes and methods

# classes_Dependency class attributes and methods

# model_classes_Class class attributes and methods

# PackageElement class attributes and methods

# classes_Class class attributes and methods

# classes_Association class attributes and methods

# classes_Attribute class attributes and methods

# classes_Method class attributes and methods

# requirement_UseCase class attributes and methods

# requirement_Scenario class attributes and methods

# model_classes_Package class attributes and methods

# model_classes_Association class attributes and methods
model_classes_Association_sourceMultiplicity: Property = Property(name="sourceMultiplicity", type=StringType)
model_classes_Association_targetMultiplicity: Property = Property(name="targetMultiplicity", type=StringType)
model_classes_Association_sourceRole: Property = Property(name="sourceRole", type=StringType)
model_classes_Association_targetRole: Property = Property(name="targetRole", type=StringType)
model_classes_Association_type: Property = Property(name="type", type=StringType)
model_classes_Association.attributes={model_classes_Association_targetRole, model_classes_Association_sourceMultiplicity, model_classes_Association_sourceRole, model_classes_Association_targetMultiplicity, model_classes_Association_type}

# model_classes_Attribute class attributes and methods
model_classes_Attribute_signature: Property = Property(name="signature", type=StringType)
model_classes_Attribute_properties: Property = Property(name="properties", type=StringType)
model_classes_Attribute_label: Property = Property(name="label", type=StringType)
model_classes_Attribute_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Attribute_scope: Property = Property(name="scope", type=StringType)
model_classes_Attribute_type: Property = Property(name="type", type=StringType)
model_classes_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_Attribute.attributes={model_classes_Attribute_defaultValue, model_classes_Attribute_visibility, model_classes_Attribute_type, model_classes_Attribute_scope, model_classes_Attribute_properties, model_classes_Attribute_signature, model_classes_Attribute_label}

# classes_PackageElement class attributes and methods

# classes_MethodArgument class attributes and methods

# model_classes_MethodArgument class attributes and methods
model_classes_MethodArgument_type: Property = Property(name="type", type=StringType)
model_classes_MethodArgument_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_classes_MethodArgument_signature: Property = Property(name="signature", type=StringType)
model_classes_MethodArgument_label: Property = Property(name="label", type=StringType)
model_classes_MethodArgument_direction: Property = Property(name="direction", type=StringType)
model_classes_MethodArgument.attributes={model_classes_MethodArgument_label, model_classes_MethodArgument_signature, model_classes_MethodArgument_direction, model_classes_MethodArgument_type, model_classes_MethodArgument_defaultValue}

# model_classes_Method class attributes and methods
model_classes_Method_visibility: Property = Property(name="visibility", type=StringType)
model_classes_Method_scope: Property = Property(name="scope", type=StringType)
model_classes_Method_returnType: Property = Property(name="returnType", type=StringType)
model_classes_Method_signature: Property = Property(name="signature", type=StringType)
model_classes_Method_properties: Property = Property(name="properties", type=StringType)
model_classes_Method_label: Property = Property(name="label", type=StringType)
model_classes_Method_stubbed: Property = Property(name="stubbed", type=BooleanType)
model_classes_Method.attributes={model_classes_Method_stubbed, model_classes_Method_scope, model_classes_Method_label, model_classes_Method_properties, model_classes_Method_visibility, model_classes_Method_returnType, model_classes_Method_signature}

# model_document_Section class attributes and methods

# document_CompositeSection class attributes and methods

# model_classes_Dependency class attributes and methods

# model_document_CompositeSection class attributes and methods

# model_document_LeafSection class attributes and methods

# Section class attributes and methods

# document_Section class attributes and methods

# model_requirement_FunctionalRequirement class attributes and methods
model_requirement_FunctionalRequirement_reviewed: Property = Property(name="reviewed", type=BooleanType)
model_requirement_FunctionalRequirement_cost: Property = Property(name="cost", type=IntegerType)
model_requirement_FunctionalRequirement_storyPoints: Property = Property(name="storyPoints", type=IntegerType)
model_requirement_FunctionalRequirement_priority: Property = Property(name="priority", type=IntegerType)
model_requirement_FunctionalRequirement.attributes={model_requirement_FunctionalRequirement_storyPoints, model_requirement_FunctionalRequirement_reviewed, model_requirement_FunctionalRequirement_priority, model_requirement_FunctionalRequirement_cost}

# requirement_FunctionalRequirement class attributes and methods

# requirement_Actor class attributes and methods

# model_requirement_UseCase class attributes and methods
model_requirement_UseCase_precondition: Property = Property(name="precondition", type=StringType)
model_requirement_UseCase_postcondition: Property = Property(name="postcondition", type=StringType)
model_requirement_UseCase_rules: Property = Property(name="rules", type=StringType)
model_requirement_UseCase_exception: Property = Property(name="exception", type=StringType)
model_requirement_UseCase.attributes={model_requirement_UseCase_exception, model_requirement_UseCase_rules, model_requirement_UseCase_postcondition, model_requirement_UseCase_precondition}

# model_requirement_Scenario class attributes and methods

# requirement_Step class attributes and methods

# requirement_UserTask class attributes and methods

# requirement_NonFunctionalRequirement class attributes and methods

# model_requirement_Actor class attributes and methods

# requirement_ActorInstance class attributes and methods

# requirement_SystemFunction class attributes and methods

# model_requirement_SystemFunction class attributes and methods
model_requirement_SystemFunction_input: Property = Property(name="input", type=StringType)
model_requirement_SystemFunction_output: Property = Property(name="output", type=StringType)
model_requirement_SystemFunction_exception: Property = Property(name="exception", type=StringType)
model_requirement_SystemFunction.attributes={model_requirement_SystemFunction_exception, model_requirement_SystemFunction_input, model_requirement_SystemFunction_output}

# model_requirement_UserTask class attributes and methods

# model_requirement_ActorInstance class attributes and methods

# model_requirement_Step class attributes and methods
model_requirement_Step_userStep: Property = Property(name="userStep", type=BooleanType)
model_requirement_Step.attributes={model_requirement_Step_userStep}

# NonDomainElement class attributes and methods

# rationale_Proposal class attributes and methods

# rationale_Solution class attributes and methods

# rationale_Criterion class attributes and methods

# model_rationale_Proposal class attributes and methods

# rationale_Issue class attributes and methods

# model_requirement_NonFunctionalRequirement class attributes and methods

# Criterion class attributes and methods

# model_rationale_Issue class attributes and methods
model_rationale_Issue_activity: Property = Property(name="activity", type=StringType)
model_rationale_Issue.attributes={model_rationale_Issue_activity}

# model_rationale_Comment class attributes and methods

# rationale_Assessment class attributes and methods

# model_rationale_Solution class attributes and methods

# model_rationale_Criterion class attributes and methods

# model_rationale_Assessment class attributes and methods
model_rationale_Assessment_value: Property = Property(name="value", type=IntegerType)
model_rationale_Assessment.attributes={model_rationale_Assessment_value}

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

# Solution class attributes and methods

# model_bug_BugReport class attributes and methods
model_bug_BugReport_severity: Property = Property(name="severity", type=StringType)
model_bug_BugReport_resolutionType: Property = Property(name="resolutionType", type=StringType)
model_bug_BugReport_resolution: Property = Property(name="resolution", type=StringType)
model_bug_BugReport_Status: Property = Property(name="Status", type=StringType)
model_bug_BugReport.attributes={model_bug_BugReport_resolutionType, model_bug_BugReport_Status, model_bug_BugReport_resolution, model_bug_BugReport_severity}

# model_meeting_Meeting class attributes and methods
model_meeting_Meeting_location: Property = Property(name="location", type=StringType)
model_meeting_Meeting_starttime: Property = Property(name="starttime", type=DateType)
model_meeting_Meeting_endtime: Property = Property(name="endtime", type=DateType)
model_meeting_Meeting.attributes={model_meeting_Meeting_endtime, model_meeting_Meeting_location, model_meeting_Meeting_starttime}

# model_component_Component class attributes and methods

# component_ComponentService class attributes and methods

# model_component_ComponentService class attributes and methods

# component_Component class attributes and methods

# model_component_DeploymentNode class attributes and methods

# model_meeting_MeetingSection class attributes and methods
model_meeting_MeetingSection_allocatedTime: Property = Property(name="allocatedTime", type=IntegerType)
model_meeting_MeetingSection.attributes={model_meeting_MeetingSection_allocatedTime}

# model_meeting_CompositeMeetingSection class attributes and methods

# MeetingSection class attributes and methods

# model_meeting_IssueMeetingSection class attributes and methods

# model_meeting_WorkItemMeetingSection class attributes and methods

# meeting_MeetingSection class attributes and methods

# meeting_IssueMeetingSection class attributes and methods

# meeting_WorkItemMeetingSection class attributes and methods

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
model_attachment_FileAttachment.attributes={model_attachment_FileAttachment_fileHash, model_attachment_FileAttachment_fileSize, model_attachment_FileAttachment_fileID, model_attachment_FileAttachment_fileName}

# model_state_Transition class attributes and methods
model_state_Transition_condition: Property = Property(name="condition", type=StringType)
model_state_Transition.attributes={model_state_Transition_condition}

# state_StateNode class attributes and methods

# model_state_StateNode class attributes and methods

# state_Transition class attributes and methods

# model_state_State class attributes and methods
model_state_State_entryConditions: Property = Property(name="entryConditions", type=StringType)
model_state_State_exitConditions: Property = Property(name="exitConditions", type=StringType)
model_state_State_activities: Property = Property(name="activities", type=StringType)
model_state_State.attributes={model_state_State_entryConditions, model_state_State_activities, model_state_State_exitConditions}

# StateNode class attributes and methods

# model_profile_Stereotype class attributes and methods
model_profile_Stereotype_required: Property = Property(name="required", type=BooleanType)
model_profile_Stereotype.attributes={model_profile_Stereotype_required}

# profile_Profile class attributes and methods

# profile_StereotypeAttribute class attributes and methods

# model_profile_StereotypeInstance class attributes and methods

# model_profile_Profile class attributes and methods

# profile_Stereotype class attributes and methods

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

# profile_StereotypeAttributeInstance class attributes and methods

# model_profile_StereotypeAttribute class attributes and methods

# model_activity_Activity class attributes and methods

# ActivityObject class attributes and methods

# model_activity_Fork class attributes and methods

# model_activity_Branch class attributes and methods

# model_activity_ActivityInitial class attributes and methods

# model_activity_ActivityEnd class attributes and methods

# esmodel_ProjectHistory class attributes and methods
esmodel_ProjectHistory_projectName: Property = Property(name="projectName", type=StringType)
esmodel_ProjectHistory_projectDescription: Property = Property(name="projectDescription", type=StringType)
esmodel_ProjectHistory.attributes={esmodel_ProjectHistory_projectDescription, esmodel_ProjectHistory_projectName}

# ProjectId class attributes and methods

# versioning_Version class attributes and methods

# esmodel_ProjectInfo class attributes and methods
esmodel_ProjectInfo_name: Property = Property(name="name", type=StringType)
esmodel_ProjectInfo_description: Property = Property(name="description", type=StringType)
esmodel_ProjectInfo.attributes={esmodel_ProjectInfo_description, esmodel_ProjectInfo_name}

# ModelElementId class attributes and methods

# model_activity_ActivityObject class attributes and methods

# activity_Transition class attributes and methods

# model_activity_Transition class attributes and methods
model_activity_Transition_condition: Property = Property(name="condition", type=StringType)
model_activity_Transition.attributes={model_activity_Transition_condition}

# activity_ActivityObject class attributes and methods

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
esmodel_versioning_LogMessage.attributes={esmodel_versioning_LogMessage_message, esmodel_versioning_LogMessage_date, esmodel_versioning_LogMessage_clientDate, esmodel_versioning_LogMessage_author}

# esmodel_versioning_ChangePackage class attributes and methods

# operations_AbstractOperation class attributes and methods

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

# esmodel_versioning_HistoryQuery class attributes and methods
esmodel_versioning_HistoryQuery_includeChangePackage: Property = Property(name="includeChangePackage", type=BooleanType)
esmodel_versioning_HistoryQuery.attributes={esmodel_versioning_HistoryQuery_includeChangePackage}

# esmodel_versioning_Version class attributes and methods

# events_Event class attributes and methods

# versioning_LogMessage class attributes and methods

# notification_ESNotification class attributes and methods

# versioning_VersionProperty class attributes and methods

# esmodel_versioning_HistoryInfo class attributes and methods

# versioning_TagVersionSpec class attributes and methods

# versioning_ChangePackage class attributes and methods

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
esmodel_operations_AttributeOperation.attributes={esmodel_operations_AttributeOperation_newValue, esmodel_operations_AttributeOperation_oldValue}

# FeatureOperation class attributes and methods

# esmodel_versioning_HeadVersionSpec class attributes and methods

# esmodel_versioning_VersionProperty class attributes and methods
esmodel_versioning_VersionProperty_name: Property = Property(name="name", type=StringType)
esmodel_versioning_VersionProperty_value: Property = Property(name="value", type=StringType)
esmodel_versioning_VersionProperty.attributes={esmodel_versioning_VersionProperty_name, esmodel_versioning_VersionProperty_value}

# esmodel_operations_AbstractOperation class attributes and methods
esmodel_operations_AbstractOperation_name: Property = Property(name="name", type=StringType)
esmodel_operations_AbstractOperation_description: Property = Property(name="description", type=StringType)
esmodel_operations_AbstractOperation_accepted: Property = Property(name="accepted", type=BooleanType)
esmodel_operations_AbstractOperation_clientDate: Property = Property(name="clientDate", type=DateType)
esmodel_operations_AbstractOperation.attributes={esmodel_operations_AbstractOperation_accepted, esmodel_operations_AbstractOperation_name, esmodel_operations_AbstractOperation_description, esmodel_operations_AbstractOperation_clientDate}

# esmodel_operations_CompositeOperation class attributes and methods
esmodel_operations_CompositeOperation_compositeName: Property = Property(name="compositeName", type=StringType)
esmodel_operations_CompositeOperation_compositeDescription: Property = Property(name="compositeDescription", type=StringType)
esmodel_operations_CompositeOperation_reversed: Property = Property(name="reversed", type=BooleanType)
esmodel_operations_CompositeOperation.attributes={esmodel_operations_CompositeOperation_compositeName, esmodel_operations_CompositeOperation_compositeDescription, esmodel_operations_CompositeOperation_reversed}

# AbstractOperation class attributes and methods

# esmodel_operations_MultiAttributeOperation class attributes and methods
esmodel_operations_MultiAttributeOperation_add: Property = Property(name="add", type=BooleanType)
esmodel_operations_MultiAttributeOperation_indexes: Property = Property(name="indexes", type=IntegerType)
esmodel_operations_MultiAttributeOperation_referencedValues: Property = Property(name="referencedValues", type=StringType)
esmodel_operations_MultiAttributeOperation.attributes={esmodel_operations_MultiAttributeOperation_referencedValues, esmodel_operations_MultiAttributeOperation_indexes, esmodel_operations_MultiAttributeOperation_add}

# esmodel_operations_MultiAttributeSetOperation class attributes and methods
esmodel_operations_MultiAttributeSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiAttributeSetOperation_oldValue: Property = Property(name="oldValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation_newValue: Property = Property(name="newValue", type=StringType)
esmodel_operations_MultiAttributeSetOperation.attributes={esmodel_operations_MultiAttributeSetOperation_newValue, esmodel_operations_MultiAttributeSetOperation_index, esmodel_operations_MultiAttributeSetOperation_oldValue}

# esmodel_operations_MultiAttributeMoveOperation class attributes and methods
esmodel_operations_MultiAttributeMoveOperation_oldIndex: Property = Property(name="oldIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_newIndex: Property = Property(name="newIndex", type=IntegerType)
esmodel_operations_MultiAttributeMoveOperation_referencedValue: Property = Property(name="referencedValue", type=StringType)
esmodel_operations_MultiAttributeMoveOperation.attributes={esmodel_operations_MultiAttributeMoveOperation_oldIndex, esmodel_operations_MultiAttributeMoveOperation_referencedValue, esmodel_operations_MultiAttributeMoveOperation_newIndex}

# esmodel_operations_MultiReferenceMoveOperation class attributes and methods
esmodel_operations_MultiReferenceMoveOperation_oldIndex: Property = Property(name="oldIndex", type=IntegerType)
esmodel_operations_MultiReferenceMoveOperation_newIndex: Property = Property(name="newIndex", type=IntegerType)
esmodel_operations_MultiReferenceMoveOperation.attributes={esmodel_operations_MultiReferenceMoveOperation_oldIndex, esmodel_operations_MultiReferenceMoveOperation_newIndex}

# esmodel_operations_ReferenceOperation class attributes and methods
esmodel_operations_ReferenceOperation_bidirectional: Property = Property(name="bidirectional", type=BooleanType)
esmodel_operations_ReferenceOperation_oppositeFeatureName: Property = Property(name="oppositeFeatureName", type=StringType)
esmodel_operations_ReferenceOperation_containmentType: Property = Property(name="containmentType", type=StringType)
esmodel_operations_ReferenceOperation.attributes={esmodel_operations_ReferenceOperation_oppositeFeatureName, esmodel_operations_ReferenceOperation_bidirectional, esmodel_operations_ReferenceOperation_containmentType}

# esmodel_operations_DiagramLayoutOperation class attributes and methods

# AttributeOperation class attributes and methods

# esmodel_operations_OperationId class attributes and methods

# esmodel_operations_OperationGroup class attributes and methods
esmodel_operations_OperationGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_OperationGroup.attributes={esmodel_operations_OperationGroup_name}

# esmodel_operations_ModelElementGroup class attributes and methods
esmodel_operations_ModelElementGroup_name: Property = Property(name="name", type=StringType)
esmodel_operations_ModelElementGroup.attributes={esmodel_operations_ModelElementGroup_name}

# esmodel_operations_SingleReferenceOperation class attributes and methods

# ReferenceOperation class attributes and methods

# esmodel_operations_MultiReferenceSetOperation class attributes and methods
esmodel_operations_MultiReferenceSetOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiReferenceSetOperation.attributes={esmodel_operations_MultiReferenceSetOperation_index}

# esmodel_operations_MultiReferenceOperation class attributes and methods
esmodel_operations_MultiReferenceOperation_add: Property = Property(name="add", type=BooleanType)
esmodel_operations_MultiReferenceOperation_index: Property = Property(name="index", type=IntegerType)
esmodel_operations_MultiReferenceOperation.attributes={esmodel_operations_MultiReferenceOperation_index, esmodel_operations_MultiReferenceOperation_add}

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
esmodel_events_ExceptionEvent.attributes={esmodel_events_ExceptionEvent_ExceptionStackTrace, esmodel_events_ExceptionEvent_ExceptionTitle, esmodel_events_ExceptionEvent_ExceptionCauseStackTrace, esmodel_events_ExceptionEvent_ExceptionCauseTitle}

# esmodel_events_PluginStartEvent class attributes and methods
esmodel_events_PluginStartEvent_pluginId: Property = Property(name="pluginId", type=StringType)
esmodel_events_PluginStartEvent.attributes={esmodel_events_PluginStartEvent_pluginId}

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

# esmodel_events_PerspectiveEvent class attributes and methods

# esmodel_events_DNDEvent class attributes and methods
esmodel_events_DNDEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_DNDEvent_targetView: Property = Property(name="targetView", type=StringType)
esmodel_events_DNDEvent.attributes={esmodel_events_DNDEvent_targetView, esmodel_events_DNDEvent_sourceView}

# esmodel_events_LinkEvent class attributes and methods
esmodel_events_LinkEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_LinkEvent_createdNew: Property = Property(name="createdNew", type=BooleanType)
esmodel_events_LinkEvent.attributes={esmodel_events_LinkEvent_sourceView, esmodel_events_LinkEvent_createdNew}

# esmodel_events_UpdateEvent class attributes and methods

# esmodel_events_AnnotationEvent class attributes and methods

# esmodel_events_RevertEvent class attributes and methods
esmodel_events_RevertEvent_revertedChangesCount: Property = Property(name="revertedChangesCount", type=IntegerType)
esmodel_events_RevertEvent.attributes={esmodel_events_RevertEvent_revertedChangesCount}

# esmodel_events_ShowHistoryEvent class attributes and methods

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

# esmodel_events_TraceEvent class attributes and methods
esmodel_events_TraceEvent_featureName: Property = Property(name="featureName", type=StringType)
esmodel_events_TraceEvent.attributes={esmodel_events_TraceEvent_featureName}

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

# esmodel_events_MergeGlobalChoiceEvent class attributes and methods
esmodel_events_MergeGlobalChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeGlobalChoiceEvent.attributes={esmodel_events_MergeGlobalChoiceEvent_selection}

# esmodel_server_ServerEvent class attributes and methods

# esmodel_server_ServerProjectEvent class attributes and methods

# ServerEvent class attributes and methods

# esmodel_server_ProjectUpdatedEvent class attributes and methods

# ServerProjectEvent class attributes and methods

# esmodel_events_URLEvent class attributes and methods
esmodel_events_URLEvent_sourceView: Property = Property(name="sourceView", type=StringType)
esmodel_events_URLEvent.attributes={esmodel_events_URLEvent_sourceView}

# esmodel_events_MergeChoiceEvent class attributes and methods
esmodel_events_MergeChoiceEvent_createdIssueName: Property = Property(name="createdIssueName", type=StringType)
esmodel_events_MergeChoiceEvent_selection: Property = Property(name="selection", type=StringType)
esmodel_events_MergeChoiceEvent_contextFeature: Property = Property(name="contextFeature", type=StringType)
esmodel_events_MergeChoiceEvent.attributes={esmodel_events_MergeChoiceEvent_contextFeature, esmodel_events_MergeChoiceEvent_createdIssueName, esmodel_events_MergeChoiceEvent_selection}

# operations_OperationId class attributes and methods

# esmodel_accesscontrol_OrgUnitProperty class attributes and methods
esmodel_accesscontrol_OrgUnitProperty_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_OrgUnitProperty_value: Property = Property(name="value", type=StringType)
esmodel_accesscontrol_OrgUnitProperty.attributes={esmodel_accesscontrol_OrgUnitProperty_value, esmodel_accesscontrol_OrgUnitProperty_name}

# esmodel_roles_Role class attributes and methods
esmodel_roles_Role_m_canAdministrate: Method = Method(name="canAdministrate", parameters={Parameter(name='projectId')}, type=BooleanType)
esmodel_roles_Role_m_canCreate: Method = Method(name="canCreate", parameters={Parameter(name='modelElement'), Parameter(name='projectId')}, type=BooleanType)
esmodel_roles_Role_m_canDelete: Method = Method(name="canDelete", parameters={Parameter(name='projectId'), Parameter(name='modelElement')}, type=BooleanType)
esmodel_roles_Role_m_canModify: Method = Method(name="canModify", parameters={Parameter(name='modelElement'), Parameter(name='projectId')}, type=BooleanType)
esmodel_roles_Role_m_canRead: Method = Method(name="canRead", parameters={Parameter(name='projectId'), Parameter(name='modelElement')}, type=BooleanType)
esmodel_roles_Role.methods={esmodel_roles_Role_m_canModify, esmodel_roles_Role_m_canCreate, esmodel_roles_Role_m_canDelete, esmodel_roles_Role_m_canRead, esmodel_roles_Role_m_canAdministrate}

# esmodel_accesscontrol_ACUser class attributes and methods
esmodel_accesscontrol_ACUser_firstName: Property = Property(name="firstName", type=StringType)
esmodel_accesscontrol_ACUser_lastName: Property = Property(name="lastName", type=StringType)
esmodel_accesscontrol_ACUser.attributes={esmodel_accesscontrol_ACUser_lastName, esmodel_accesscontrol_ACUser_firstName}

# ACOrgUnit class attributes and methods

# esmodel_accesscontrol_ACOrgUnit class attributes and methods
esmodel_accesscontrol_ACOrgUnit_name: Property = Property(name="name", type=StringType)
esmodel_accesscontrol_ACOrgUnit_description: Property = Property(name="description", type=StringType)
esmodel_accesscontrol_ACOrgUnit_m_getId: Method = Method(name="getId", parameters={}, type=StringType)
esmodel_accesscontrol_ACOrgUnit.attributes={esmodel_accesscontrol_ACOrgUnit_name, esmodel_accesscontrol_ACOrgUnit_description}
esmodel_accesscontrol_ACOrgUnit.methods={esmodel_accesscontrol_ACOrgUnit_m_getId}

# roles_Role class attributes and methods

# accesscontrol_OrgUnitProperty class attributes and methods

# esmodel_accesscontrol_ACGroup class attributes and methods

# accesscontrol_ACOrgUnit class attributes and methods

# esmodel_accesscontrol_ACOrgUnitId class attributes and methods

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

# esmodel_url_ModelElementUrl class attributes and methods

# url_ServerUrl class attributes and methods

# url_ProjectUrlFragment class attributes and methods

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
esmodel_notification_ESNotification.attributes={esmodel_notification_ESNotification_provider, esmodel_notification_ESNotification_details, esmodel_notification_ESNotification_creationDate, esmodel_notification_ESNotification_recipient, esmodel_notification_ESNotification_name, esmodel_notification_ESNotification_message, esmodel_notification_ESNotification_sender, esmodel_notification_ESNotification_seen}

# url_ModelElementUrlFragment class attributes and methods

# Relationships
modelElements0: BinaryAssociation = BinaryAssociation(
    name="modelElements0",
    ends={
        Property(name="ModelElement", type=metamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Project", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations4: BinaryAssociation = BinaryAssociation(
    name="annotations4",
    ends={
        Property(name="#", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
attachments5: BinaryAssociation = BinaryAssociation(
    name="attachments5",
    ends={
        Property(name="#7", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=Attachment, multiplicity=Multiplicity(0, 9999))
    }
)
leafSection8: BinaryAssociation = BinaryAssociation(
    name="leafSection8",
    ends={
        Property(name="#10", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=document_LeafSection, multiplicity=Multiplicity(0, 1))
    }
)
incomingDocumentReferences11: BinaryAssociation = BinaryAssociation(
    name="incomingDocumentReferences11",
    ends={
        Property(name="#13", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="112", type=document_LeafSection, multiplicity=Multiplicity(0, 9999))
    }
)
cutElements1: BinaryAssociation = BinaryAssociation(
    name="cutElements1",
    ends={
        Property(name="ModelElement3", type=metamodel_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Project2", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedModelElements20: BinaryAssociation = BinaryAssociation(
    name="annotatedModelElements20",
    ends={
        Property(name="#22", type=model_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="121", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
referringModelElements23: BinaryAssociation = BinaryAssociation(
    name="referringModelElements23",
    ends={
        Property(name="#25", type=model_Attachment, multiplicity=Multiplicity(1, 1)),
        Property(name="124", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
groupMemberships26: BinaryAssociation = BinaryAssociation(
    name="groupMemberships26",
    ends={
        Property(name="#28", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="127", type=organization_Group, multiplicity=Multiplicity(0, 9999))
    }
)
participations29: BinaryAssociation = BinaryAssociation(
    name="participations29",
    ends={
        Property(name="#31", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="130", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
assignments32: BinaryAssociation = BinaryAssociation(
    name="assignments32",
    ends={
        Property(name="#34", type=model_organization_OrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="133", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
comments14: BinaryAssociation = BinaryAssociation(
    name="comments14",
    ends={
        Property(name="#16", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="115", type=rationale_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appliedStereotypeInstances17: BinaryAssociation = BinaryAssociation(
    name="appliedStereotypeInstances17",
    ends={
        Property(name="#19", type=model_UnicaseModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="118", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orgUnits38: BinaryAssociation = BinaryAssociation(
    name="orgUnits38",
    ends={
        Property(name="#40", type=model_organization_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="139", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containingWorkpackage41: BinaryAssociation = BinaryAssociation(
    name="containingWorkpackage41",
    ends={
        Property(name="#43", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="142", type=task_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
successors44: BinaryAssociation = BinaryAssociation(
    name="successors44",
    ends={
        Property(name="#46", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="145", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
predecessors47: BinaryAssociation = BinaryAssociation(
    name="predecessors47",
    ends={
        Property(name="#49", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="148", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
assignee50: BinaryAssociation = BinaryAssociation(
    name="assignee50",
    ends={
        Property(name="#52", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="151", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
reviewer53: BinaryAssociation = BinaryAssociation(
    name="reviewer53",
    ends={
        Property(name="#55", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="154", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
participants56: BinaryAssociation = BinaryAssociation(
    name="participants56",
    ends={
        Property(name="#58", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="157", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
workItemsToReview35: BinaryAssociation = BinaryAssociation(
    name="workItemsToReview35",
    ends={
        Property(name="#37", type=model_organization_User, multiplicity=Multiplicity(1, 1)),
        Property(name="136", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
associatedChangePackages59: BinaryAssociation = BinaryAssociation(
    name="associatedChangePackages59",
    ends={
        Property(name="change_ModelChangePackage", type=model_task_WorkItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_task_WorkItem", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
    }
)
containedWorkItems60: BinaryAssociation = BinaryAssociation(
    name="containedWorkItems60",
    ends={
        Property(name="#62", type=model_task_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="161", type=task_WorkItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedModelElements63: BinaryAssociation = BinaryAssociation(
    name="containedModelElements63",
    ends={
        Property(name="UnicaseModelElement", type=model_task_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="model_task_Milestone", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
elements64: BinaryAssociation = BinaryAssociation(
    name="elements64",
    ends={
        Property(name="UnicaseModelElement65", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
gmfdiagram66: BinaryAssociation = BinaryAssociation(
    name="gmfdiagram66",
    ends={
        Property(name="diagram_model_Diagram", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram67", type=diagram_model_Diagram, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newElements68: BinaryAssociation = BinaryAssociation(
    name="newElements68",
    ends={
        Property(name="UnicaseModelElement70", type=model_diagram_MEDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_diagram_MEDiagram69", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPackage71: BinaryAssociation = BinaryAssociation(
    name="parentPackage71",
    ends={
        Property(name="#73", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="172", type=classes_Package, multiplicity=Multiplicity(0, 1))
    }
)
outgoingDependencies74: BinaryAssociation = BinaryAssociation(
    name="outgoingDependencies74",
    ends={
        Property(name="#76", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="175", type=classes_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
incomingDependencies77: BinaryAssociation = BinaryAssociation(
    name="incomingDependencies77",
    ends={
        Property(name="#79", type=model_classes_PackageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="178", type=classes_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
subClasses80: BinaryAssociation = BinaryAssociation(
    name="subClasses80",
    ends={
        Property(name="#82", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="181", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingAssociations86: BinaryAssociation = BinaryAssociation(
    name="outgoingAssociations86",
    ends={
        Property(name="#88", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="187", type=classes_Association, multiplicity=Multiplicity(0, 9999))
    }
)
incomingAssociations89: BinaryAssociation = BinaryAssociation(
    name="incomingAssociations89",
    ends={
        Property(name="#91", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="190", type=classes_Association, multiplicity=Multiplicity(0, 9999))
    }
)
attributes92: BinaryAssociation = BinaryAssociation(
    name="attributes92",
    ends={
        Property(name="#94", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="193", type=classes_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods95: BinaryAssociation = BinaryAssociation(
    name="methods95",
    ends={
        Property(name="#97", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="196", type=classes_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participatedUseCases98: BinaryAssociation = BinaryAssociation(
    name="participatedUseCases98",
    ends={
        Property(name="#100", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="199", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
demoParticipations101: BinaryAssociation = BinaryAssociation(
    name="demoParticipations101",
    ends={
        Property(name="#103", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="1102", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
facadeClass104: BinaryAssociation = BinaryAssociation(
    name="facadeClass104",
    ends={
        Property(name="classes_Class", type=model_classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="model_classes_Package", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
superClasses83: BinaryAssociation = BinaryAssociation(
    name="superClasses83",
    ends={
        Property(name="#85", type=model_classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="184", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
source108: BinaryAssociation = BinaryAssociation(
    name="source108",
    ends={
        Property(name="#110", type=model_classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="1109", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
target111: BinaryAssociation = BinaryAssociation(
    name="target111",
    ends={
        Property(name="#113", type=model_classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="1112", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
definingClass114: BinaryAssociation = BinaryAssociation(
    name="definingClass114",
    ends={
        Property(name="#116", type=model_classes_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1115", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
containedPackageElements105: BinaryAssociation = BinaryAssociation(
    name="containedPackageElements105",
    ends={
        Property(name="#107", type=model_classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="1106", type=classes_PackageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callingMethods123: BinaryAssociation = BinaryAssociation(
    name="callingMethods123",
    ends={
        Property(name="#125", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="1124", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
arguments126: BinaryAssociation = BinaryAssociation(
    name="arguments126",
    ends={
        Property(name="classes_MethodArgument", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="model_classes_Method", type=classes_MethodArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
demoParticipations127: BinaryAssociation = BinaryAssociation(
    name="demoParticipations127",
    ends={
        Property(name="#129", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="1128", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
definingClass117: BinaryAssociation = BinaryAssociation(
    name="definingClass117",
    ends={
        Property(name="#119", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="1118", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
calledMethods120: BinaryAssociation = BinaryAssociation(
    name="calledMethods120",
    ends={
        Property(name="#122", type=model_classes_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="1121", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
source130: BinaryAssociation = BinaryAssociation(
    name="source130",
    ends={
        Property(name="#132", type=model_classes_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="1131", type=classes_PackageElement, multiplicity=Multiplicity(0, 1))
    }
)
target133: BinaryAssociation = BinaryAssociation(
    name="target133",
    ends={
        Property(name="#135", type=model_classes_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="1134", type=classes_PackageElement, multiplicity=Multiplicity(0, 1))
    }
)
parent136: BinaryAssociation = BinaryAssociation(
    name="parent136",
    ends={
        Property(name="#138", type=model_document_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="1137", type=document_CompositeSection, multiplicity=Multiplicity(0, 1))
    }
)
modelElements139: BinaryAssociation = BinaryAssociation(
    name="modelElements139",
    ends={
        Property(name="1140", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="#141", type=model_document_LeafSection, multiplicity=Multiplicity(1, 1))
    }
)
referencedModelElements142: BinaryAssociation = BinaryAssociation(
    name="referencedModelElements142",
    ends={
        Property(name="#144", type=model_document_LeafSection, multiplicity=Multiplicity(1, 1)),
        Property(name="1143", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
refinedRequirement151: BinaryAssociation = BinaryAssociation(
    name="refinedRequirement151",
    ends={
        Property(name="#153", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1152", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 1))
    }
)
stakeholder154: BinaryAssociation = BinaryAssociation(
    name="stakeholder154",
    ends={
        Property(name="organization_OrgUnit", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_FunctionalRequirement", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
useCases155: BinaryAssociation = BinaryAssociation(
    name="useCases155",
    ends={
        Property(name="#157", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1156", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
subsections145: BinaryAssociation = BinaryAssociation(
    name="subsections145",
    ends={
        Property(name="#147", type=model_document_CompositeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="1146", type=document_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refiningRequirements148: BinaryAssociation = BinaryAssociation(
    name="refiningRequirements148",
    ends={
        Property(name="#150", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1149", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedUseCases167: BinaryAssociation = BinaryAssociation(
    name="includedUseCases167",
    ends={
        Property(name="requirement_UseCase", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_UseCase", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
extendedUseCases168: BinaryAssociation = BinaryAssociation(
    name="extendedUseCases168",
    ends={
        Property(name="requirement_UseCase170", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_UseCase169", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
scenarios171: BinaryAssociation = BinaryAssociation(
    name="scenarios171",
    ends={
        Property(name="#173", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1172", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActor174: BinaryAssociation = BinaryAssociation(
    name="initiatingActor174",
    ends={
        Property(name="#176", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1175", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
scenarios158: BinaryAssociation = BinaryAssociation(
    name="scenarios158",
    ends={
        Property(name="#160", type=model_requirement_FunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1159", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
functionalRequirements161: BinaryAssociation = BinaryAssociation(
    name="functionalRequirements161",
    ends={
        Property(name="#163", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1162", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
identifiedClasses164: BinaryAssociation = BinaryAssociation(
    name="identifiedClasses164",
    ends={
        Property(name="#166", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1165", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
instantiatedUseCases189: BinaryAssociation = BinaryAssociation(
    name="instantiatedUseCases189",
    ends={
        Property(name="#191", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1190", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
functionalRequirements192: BinaryAssociation = BinaryAssociation(
    name="functionalRequirements192",
    ends={
        Property(name="#194", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1193", type=requirement_FunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
participatingActors177: BinaryAssociation = BinaryAssociation(
    name="participatingActors177",
    ends={
        Property(name="#179", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1178", type=requirement_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
useCaseSteps180: BinaryAssociation = BinaryAssociation(
    name="useCaseSteps180",
    ends={
        Property(name="#182", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1181", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedUserTask183: BinaryAssociation = BinaryAssociation(
    name="realizedUserTask183",
    ends={
        Property(name="#185", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1184", type=requirement_UserTask, multiplicity=Multiplicity(0, 1))
    }
)
nonFunctionalRequirements186: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements186",
    ends={
        Property(name="#188", type=model_requirement_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="1187", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedUseCases211: BinaryAssociation = BinaryAssociation(
    name="initiatedUseCases211",
    ends={
        Property(name="#213", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="1212", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
participatedUseCases214: BinaryAssociation = BinaryAssociation(
    name="participatedUseCases214",
    ends={
        Property(name="#216", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="1215", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
instances217: BinaryAssociation = BinaryAssociation(
    name="instances217",
    ends={
        Property(name="#219", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="1218", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
participatingMethods195: BinaryAssociation = BinaryAssociation(
    name="participatingMethods195",
    ends={
        Property(name="#197", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1196", type=classes_Method, multiplicity=Multiplicity(0, 9999))
    }
)
participatingClasses198: BinaryAssociation = BinaryAssociation(
    name="participatingClasses198",
    ends={
        Property(name="#200", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1199", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
initiatingActorInstance201: BinaryAssociation = BinaryAssociation(
    name="initiatingActorInstance201",
    ends={
        Property(name="#203", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1202", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 1))
    }
)
participatingActorInstances204: BinaryAssociation = BinaryAssociation(
    name="participatingActorInstances204",
    ends={
        Property(name="#206", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1205", type=requirement_ActorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
steps207: BinaryAssociation = BinaryAssociation(
    name="steps207",
    ends={
        Property(name="requirement_Step", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Scenario", type=requirement_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonFunctionalRequirements208: BinaryAssociation = BinaryAssociation(
    name="nonFunctionalRequirements208",
    ends={
        Property(name="#210", type=model_requirement_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="1209", type=requirement_NonFunctionalRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
includedUseCase235: BinaryAssociation = BinaryAssociation(
    name="includedUseCase235",
    ends={
        Property(name="requirement_UseCase236", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
useCase237: BinaryAssociation = BinaryAssociation(
    name="useCase237",
    ends={
        Property(name="#239", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="1238", type=requirement_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
includedSystemFunction240: BinaryAssociation = BinaryAssociation(
    name="includedSystemFunction240",
    ends={
        Property(name="requirement_SystemFunction", type=model_requirement_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="model_requirement_Step241", type=requirement_SystemFunction, multiplicity=Multiplicity(0, 1))
    }
)
initiatingActor242: BinaryAssociation = BinaryAssociation(
    name="initiatingActor242",
    ends={
        Property(name="#244", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="1243", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
participatingActor245: BinaryAssociation = BinaryAssociation(
    name="participatingActor245",
    ends={
        Property(name="#247", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="1246", type=requirement_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
participatedUserTasks220: BinaryAssociation = BinaryAssociation(
    name="participatedUserTasks220",
    ends={
        Property(name="#222", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="1221", type=requirement_UserTask, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedUserTask223: BinaryAssociation = BinaryAssociation(
    name="initiatedUserTask223",
    ends={
        Property(name="#225", type=model_requirement_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="1224", type=requirement_UserTask, multiplicity=Multiplicity(0, 1))
    }
)
initiatedScenarios226: BinaryAssociation = BinaryAssociation(
    name="initiatedScenarios226",
    ends={
        Property(name="#228", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1227", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
participatedScenarios229: BinaryAssociation = BinaryAssociation(
    name="participatedScenarios229",
    ends={
        Property(name="#231", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1230", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
instantiatedActor232: BinaryAssociation = BinaryAssociation(
    name="instantiatedActor232",
    ends={
        Property(name="#234", type=model_requirement_ActorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1233", type=requirement_Actor, multiplicity=Multiplicity(0, 1))
    }
)
proposals257: BinaryAssociation = BinaryAssociation(
    name="proposals257",
    ends={
        Property(name="#259", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="1258", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solution260: BinaryAssociation = BinaryAssociation(
    name="solution260",
    ends={
        Property(name="#262", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="1261", type=rationale_Solution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
criteria263: BinaryAssociation = BinaryAssociation(
    name="criteria263",
    ends={
        Property(name="rationale_Criterion", type=model_rationale_Issue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Issue", type=rationale_Criterion, multiplicity=Multiplicity(0, 9999))
    }
)
issue264: BinaryAssociation = BinaryAssociation(
    name="issue264",
    ends={
        Property(name="#266", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="1265", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
realizingUseCases248: BinaryAssociation = BinaryAssociation(
    name="realizingUseCases248",
    ends={
        Property(name="#250", type=model_requirement_UserTask, multiplicity=Multiplicity(1, 1)),
        Property(name="1249", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedUseCases251: BinaryAssociation = BinaryAssociation(
    name="restrictedUseCases251",
    ends={
        Property(name="#253", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1252", type=requirement_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
restrictedScenarios254: BinaryAssociation = BinaryAssociation(
    name="restrictedScenarios254",
    ends={
        Property(name="#256", type=model_requirement_NonFunctionalRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="1255", type=requirement_Scenario, multiplicity=Multiplicity(0, 9999))
    }
)
proposal277: BinaryAssociation = BinaryAssociation(
    name="proposal277",
    ends={
        Property(name="#279", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="1278", type=rationale_Proposal, multiplicity=Multiplicity(0, 1))
    }
)
criterion280: BinaryAssociation = BinaryAssociation(
    name="criterion280",
    ends={
        Property(name="#282", type=model_rationale_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="1281", type=rationale_Criterion, multiplicity=Multiplicity(0, 1))
    }
)
sender283: BinaryAssociation = BinaryAssociation(
    name="sender283",
    ends={
        Property(name="organization_OrgUnit284", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment", type=organization_OrgUnit, multiplicity=Multiplicity(0, 1))
    }
)
recipients285: BinaryAssociation = BinaryAssociation(
    name="recipients285",
    ends={
        Property(name="organization_OrgUnit287", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Comment286", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
commentedElement288: BinaryAssociation = BinaryAssociation(
    name="commentedElement288",
    ends={
        Property(name="#290", type=model_rationale_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="1289", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
assessments267: BinaryAssociation = BinaryAssociation(
    name="assessments267",
    ends={
        Property(name="#269", type=model_rationale_Proposal, multiplicity=Multiplicity(1, 1)),
        Property(name="1268", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
underlyingProposals270: BinaryAssociation = BinaryAssociation(
    name="underlyingProposals270",
    ends={
        Property(name="rationale_Proposal", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_rationale_Solution", type=rationale_Proposal, multiplicity=Multiplicity(0, 9999))
    }
)
issue271: BinaryAssociation = BinaryAssociation(
    name="issue271",
    ends={
        Property(name="#273", type=model_rationale_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="1272", type=rationale_Issue, multiplicity=Multiplicity(0, 1))
    }
)
assessments274: BinaryAssociation = BinaryAssociation(
    name="assessments274",
    ends={
        Property(name="#276", type=model_rationale_Criterion, multiplicity=Multiplicity(1, 1)),
        Property(name="1275", type=rationale_Assessment, multiplicity=Multiplicity(0, 9999))
    }
)
conflictingProposals291: BinaryAssociation = BinaryAssociation(
    name="conflictingProposals291",
    ends={
        Property(name="change_MergingProposal", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal", type=change_MergingProposal, multiplicity=Multiplicity(0, 9999))
    }
)
pendingChanges292: BinaryAssociation = BinaryAssociation(
    name="pendingChanges292",
    ends={
        Property(name="change_ModelChangePackage294", type=model_change_MergingProposal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingProposal293", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 1))
    }
)
appliedChanges295: BinaryAssociation = BinaryAssociation(
    name="appliedChanges295",
    ends={
        Property(name="change_ModelChangePackage296", type=model_change_MergingSolution, multiplicity=Multiplicity(1, 1)),
        Property(name="model_change_MergingSolution", type=change_ModelChangePackage, multiplicity=Multiplicity(0, 9999))
    }
)
components313: BinaryAssociation = BinaryAssociation(
    name="components313",
    ends={
        Property(name="component_Component", type=model_component_DeploymentNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_DeploymentNode", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
facilitator314: BinaryAssociation = BinaryAssociation(
    name="facilitator314",
    ends={
        Property(name="organization_User", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
packages297: BinaryAssociation = BinaryAssociation(
    name="packages297",
    ends={
        Property(name="classes_Package", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
subsystems298: BinaryAssociation = BinaryAssociation(
    name="subsystems298",
    ends={
        Property(name="classes_Package300", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component299", type=classes_Package, multiplicity=Multiplicity(0, 9999))
    }
)
offeredServices301: BinaryAssociation = BinaryAssociation(
    name="offeredServices301",
    ends={
        Property(name="#303", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="1302", type=component_ComponentService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
consumedServices304: BinaryAssociation = BinaryAssociation(
    name="consumedServices304",
    ends={
        Property(name="#306", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="1305", type=component_ComponentService, multiplicity=Multiplicity(0, 9999))
    }
)
offeringComponent307: BinaryAssociation = BinaryAssociation(
    name="offeringComponent307",
    ends={
        Property(name="#309", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="1308", type=component_Component, multiplicity=Multiplicity(0, 1))
    }
)
consumingComponents310: BinaryAssociation = BinaryAssociation(
    name="consumingComponents310",
    ends={
        Property(name="#312", type=model_component_ComponentService, multiplicity=Multiplicity(1, 1)),
        Property(name="1311", type=component_Component, multiplicity=Multiplicity(0, 9999))
    }
)
identifiedWorkItemsSection328: BinaryAssociation = BinaryAssociation(
    name="identifiedWorkItemsSection328",
    ends={
        Property(name="meeting_WorkItemMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting329", type=meeting_WorkItemMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
subsections330: BinaryAssociation = BinaryAssociation(
    name="subsections330",
    ends={
        Property(name="meeting_MeetingSection331", type=model_meeting_CompositeMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_CompositeMeetingSection", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedIssues332: BinaryAssociation = BinaryAssociation(
    name="includedIssues332",
    ends={
        Property(name="rationale_Issue", type=model_meeting_IssueMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_IssueMeetingSection", type=rationale_Issue, multiplicity=Multiplicity(0, 9999))
    }
)
minutetaker315: BinaryAssociation = BinaryAssociation(
    name="minutetaker315",
    ends={
        Property(name="organization_User317", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting316", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
timekeeper318: BinaryAssociation = BinaryAssociation(
    name="timekeeper318",
    ends={
        Property(name="organization_User320", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting319", type=organization_User, multiplicity=Multiplicity(0, 1))
    }
)
participants321: BinaryAssociation = BinaryAssociation(
    name="participants321",
    ends={
        Property(name="organization_OrgUnit323", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting322", type=organization_OrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
sections324: BinaryAssociation = BinaryAssociation(
    name="sections324",
    ends={
        Property(name="meeting_MeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting325", type=meeting_MeetingSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiedIssuesSection326: BinaryAssociation = BinaryAssociation(
    name="identifiedIssuesSection326",
    ends={
        Property(name="meeting_IssueMeetingSection", type=model_meeting_Meeting, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_Meeting327", type=meeting_IssueMeetingSection, multiplicity=Multiplicity(0, 1))
    }
)
includedWorkItems333: BinaryAssociation = BinaryAssociation(
    name="includedWorkItems333",
    ends={
        Property(name="task_WorkItem", type=model_meeting_WorkItemMeetingSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_meeting_WorkItemMeetingSection", type=task_WorkItem, multiplicity=Multiplicity(0, 9999))
    }
)
source334: BinaryAssociation = BinaryAssociation(
    name="source334",
    ends={
        Property(name="#336", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="1335", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
target337: BinaryAssociation = BinaryAssociation(
    name="target337",
    ends={
        Property(name="#339", type=model_state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="1338", type=state_StateNode, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions340: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions340",
    ends={
        Property(name="#342", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="1341", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions343: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions343",
    ends={
        Property(name="#345", type=model_state_StateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="1344", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
profile351: BinaryAssociation = BinaryAssociation(
    name="profile351",
    ends={
        Property(name="#353", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="1352", type=profile_Profile, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeInstances354: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstances354",
    ends={
        Property(name="#356", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="1355", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeAttributes357: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributes357",
    ends={
        Property(name="#359", type=model_profile_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="1358", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype360: BinaryAssociation = BinaryAssociation(
    name="stereotype360",
    ends={
        Property(name="#362", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1361", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
affectedContainers346: BinaryAssociation = BinaryAssociation(
    name="affectedContainers346",
    ends={
        Property(name="UnicaseModelElement347", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_profile_Profile", type=UnicaseModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypes348: BinaryAssociation = BinaryAssociation(
    name="stereotypes348",
    ends={
        Property(name="#350", type=model_profile_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="1349", type=profile_Stereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype369: BinaryAssociation = BinaryAssociation(
    name="stereotype369",
    ends={
        Property(name="#371", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1370", type=profile_Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances372: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances372",
    ends={
        Property(name="#374", type=model_profile_StereotypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="1373", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeInstance375: BinaryAssociation = BinaryAssociation(
    name="stereotypeInstance375",
    ends={
        Property(name="#377", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1376", type=profile_StereotypeInstance, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttribute378: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttribute378",
    ends={
        Property(name="#380", type=model_profile_StereotypeAttributeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1379", type=profile_StereotypeAttribute, multiplicity=Multiplicity(0, 1))
    }
)
modelElement363: BinaryAssociation = BinaryAssociation(
    name="modelElement363",
    ends={
        Property(name="#365", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1364", type=UnicaseModelElement, multiplicity=Multiplicity(0, 1))
    }
)
stereotypeAttributeInstances366: BinaryAssociation = BinaryAssociation(
    name="stereotypeAttributeInstances366",
    ends={
        Property(name="#368", type=model_profile_StereotypeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="1367", type=profile_StereotypeAttributeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target397: BinaryAssociation = BinaryAssociation(
    name="target397",
    ends={
        Property(name="1398", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1)),
        Property(name="#399", type=model_activity_Transition, multiplicity=Multiplicity(1, 1))
    }
)
projectId400: BinaryAssociation = BinaryAssociation(
    name="projectId400",
    ends={
        Property(name="ProjectId", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
versions401: BinaryAssociation = BinaryAssociation(
    name="versions401",
    ends={
        Property(name="versioning_Version", type=esmodel_ProjectHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectHistory402", type=versioning_Version, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source381: BinaryAssociation = BinaryAssociation(
    name="source381",
    ends={
        Property(name="ModelElementId", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target382: BinaryAssociation = BinaryAssociation(
    name="target382",
    ends={
        Property(name="ModelElementId384", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath383", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path385: BinaryAssociation = BinaryAssociation(
    name="path385",
    ends={
        Property(name="ModelElementId387", type=model_util_ModelElementPath, multiplicity=Multiplicity(1, 1)),
        Property(name="model_util_ModelElementPath386", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions388: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions388",
    ends={
        Property(name="#390", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="1389", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions391: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions391",
    ends={
        Property(name="#393", type=model_activity_ActivityObject, multiplicity=Multiplicity(1, 1)),
        Property(name="1392", type=activity_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source394: BinaryAssociation = BinaryAssociation(
    name="source394",
    ends={
        Property(name="#396", type=model_activity_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="1395", type=activity_ActivityObject, multiplicity=Multiplicity(0, 1))
    }
)
operations414: BinaryAssociation = BinaryAssociation(
    name="operations414",
    ends={
        Property(name="operations_AbstractOperation", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectId403: BinaryAssociation = BinaryAssociation(
    name="projectId403",
    ends={
        Property(name="ProjectId404", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo", type=ProjectId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
version405: BinaryAssociation = BinaryAssociation(
    name="version405",
    ends={
        Property(name="versioning_PrimaryVersionSpec", type=esmodel_ProjectInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ProjectInfo406", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups407: BinaryAssociation = BinaryAssociation(
    name="groups407",
    ends={
        Property(name="accesscontrol_ACGroup", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace", type=accesscontrol_ACGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects408: BinaryAssociation = BinaryAssociation(
    name="projects408",
    ends={
        Property(name="ProjectHistory", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace409", type=ProjectHistory, multiplicity=Multiplicity(0, 9999))
    }
)
openSessions410: BinaryAssociation = BinaryAssociation(
    name="openSessions410",
    ends={
        Property(name="SessionId", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace411", type=SessionId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users412: BinaryAssociation = BinaryAssociation(
    name="users412",
    ends={
        Property(name="accesscontrol_ACUser", type=esmodel_ServerSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_ServerSpace413", type=accesscontrol_ACUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changePackage433: BinaryAssociation = BinaryAssociation(
    name="changePackage433",
    ends={
        Property(name="esmodel_versioning_HistoryInfo434", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="versioning_ChangePackage", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1))
    }
)
source435: BinaryAssociation = BinaryAssociation(
    name="source435",
    ends={
        Property(name="versioning_PrimaryVersionSpec436", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target437: BinaryAssociation = BinaryAssociation(
    name="target437",
    ends={
        Property(name="versioning_PrimaryVersionSpec439", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery438", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElements440: BinaryAssociation = BinaryAssociation(
    name="modelElements440",
    ends={
        Property(name="ModelElementId442", type=esmodel_versioning_HistoryQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryQuery441", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectState443: BinaryAssociation = BinaryAssociation(
    name="projectState443",
    ends={
        Property(name="Project", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version", type=Project, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primarySpec444: BinaryAssociation = BinaryAssociation(
    name="primarySpec444",
    ends={
        Property(name="versioning_PrimaryVersionSpec446", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version445", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs447: BinaryAssociation = BinaryAssociation(
    name="tagSpecs447",
    ends={
        Property(name="versioning_TagVersionSpec449", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version448", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextVersion450: BinaryAssociation = BinaryAssociation(
    name="nextVersion450",
    ends={
        Property(name="#451", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="2", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
events415: BinaryAssociation = BinaryAssociation(
    name="events415",
    ends={
        Property(name="events_Event", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage416", type=events_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logMessage417: BinaryAssociation = BinaryAssociation(
    name="logMessage417",
    ends={
        Property(name="versioning_LogMessage", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage418", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications419: BinaryAssociation = BinaryAssociation(
    name="notifications419",
    ends={
        Property(name="notification_ESNotification", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage420", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties421: BinaryAssociation = BinaryAssociation(
    name="versionProperties421",
    ends={
        Property(name="versioning_VersionProperty", type=esmodel_versioning_ChangePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_ChangePackage422", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primerySpec423: BinaryAssociation = BinaryAssociation(
    name="primerySpec423",
    ends={
        Property(name="versioning_PrimaryVersionSpec424", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
logMessage425: BinaryAssociation = BinaryAssociation(
    name="logMessage425",
    ends={
        Property(name="versioning_LogMessage427", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo426", type=versioning_LogMessage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tagSpecs428: BinaryAssociation = BinaryAssociation(
    name="tagSpecs428",
    ends={
        Property(name="versioning_TagVersionSpec", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo429", type=versioning_TagVersionSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versionProperties430: BinaryAssociation = BinaryAssociation(
    name="versionProperties430",
    ends={
        Property(name="versioning_VersionProperty432", type=esmodel_versioning_HistoryInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_HistoryInfo431", type=versioning_VersionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subOperations463: BinaryAssociation = BinaryAssociation(
    name="subOperations463",
    ends={
        Property(name="operations_AbstractOperation464", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainOperation465: BinaryAssociation = BinaryAssociation(
    name="mainOperation465",
    ends={
        Property(name="operations_AbstractOperation467", type=esmodel_operations_CompositeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CompositeOperation466", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1))
    }
)
modelElement468: BinaryAssociation = BinaryAssociation(
    name="modelElement468",
    ends={
        Property(name="operations_esmodel_EObject", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subOperations469: BinaryAssociation = BinaryAssociation(
    name="subOperations469",
    ends={
        Property(name="operations_ReferenceOperation", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation470", type=operations_ReferenceOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eObjectToIdMap471: BinaryAssociation = BinaryAssociation(
    name="eObjectToIdMap471",
    ends={
        Property(name="operations_EObjectToModelElementIdMap", type=esmodel_operations_CreateDeleteOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_CreateDeleteOperation472", type=operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
previousVersion452: BinaryAssociation = BinaryAssociation(
    name="previousVersion452",
    ends={
        Property(name="#454", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="2453", type=versioning_Version, multiplicity=Multiplicity(0, 1))
    }
)
changes455: BinaryAssociation = BinaryAssociation(
    name="changes455",
    ends={
        Property(name="versioning_ChangePackage457", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version456", type=versioning_ChangePackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logMessage458: BinaryAssociation = BinaryAssociation(
    name="logMessage458",
    ends={
        Property(name="versioning_LogMessage460", type=esmodel_versioning_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_versioning_Version459", type=versioning_LogMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId461: BinaryAssociation = BinaryAssociation(
    name="modelElementId461",
    ends={
        Property(name="ModelElementId462", type=esmodel_operations_AbstractOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_AbstractOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedModelElements483: BinaryAssociation = BinaryAssociation(
    name="referencedModelElements483",
    ends={
        Property(name="ModelElementId484", type=esmodel_operations_MultiReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedModelElementId485: BinaryAssociation = BinaryAssociation(
    name="referencedModelElementId485",
    ends={
        Property(name="ModelElementId486", type=esmodel_operations_MultiReferenceMoveOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceMoveOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations487: BinaryAssociation = BinaryAssociation(
    name="operations487",
    ends={
        Property(name="operations_AbstractOperation488", type=esmodel_operations_OperationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_OperationGroup", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999))
    }
)
modelElements489: BinaryAssociation = BinaryAssociation(
    name="modelElements489",
    ends={
        Property(name="ModelElementId490", type=esmodel_operations_ModelElementGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_ModelElementGroup", type=ModelElementId, multiplicity=Multiplicity(0, 9999))
    }
)
oldValue473: BinaryAssociation = BinaryAssociation(
    name="oldValue473",
    ends={
        Property(name="ModelElementId474", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue475: BinaryAssociation = BinaryAssociation(
    name="newValue475",
    ends={
        Property(name="ModelElementId477", type=esmodel_operations_SingleReferenceOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_SingleReferenceOperation476", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oldValue478: BinaryAssociation = BinaryAssociation(
    name="oldValue478",
    ends={
        Property(name="ModelElementId479", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue480: BinaryAssociation = BinaryAssociation(
    name="newValue480",
    ends={
        Property(name="ModelElementId482", type=esmodel_operations_MultiReferenceSetOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_MultiReferenceSetOperation481", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseVersion498: BinaryAssociation = BinaryAssociation(
    name="baseVersion498",
    ends={
        Property(name="versioning_PrimaryVersionSpec499", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion500: BinaryAssociation = BinaryAssociation(
    name="targetVersion500",
    ends={
        Property(name="versioning_PrimaryVersionSpec502", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent501", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localChanges503: BinaryAssociation = BinaryAssociation(
    name="localChanges503",
    ends={
        Property(name="operations_AbstractOperation505", type=esmodel_events_MergeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeEvent504", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseVersion506: BinaryAssociation = BinaryAssociation(
    name="baseVersion506",
    ends={
        Property(name="versioning_PrimaryVersionSpec507", type=esmodel_events_CheckoutEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_CheckoutEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key491: BinaryAssociation = BinaryAssociation(
    name="key491",
    ends={
        Property(name="operations_esmodel_EObject492", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap", type=operations_esmodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)
value493: BinaryAssociation = BinaryAssociation(
    name="value493",
    ends={
        Property(name="ModelElementId495", type=esmodel_operations_EObjectToModelElementIdMap, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_operations_EObjectToModelElementIdMap494", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement496: BinaryAssociation = BinaryAssociation(
    name="modelElement496",
    ends={
        Property(name="ModelElementId497", type=esmodel_events_ReadEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ReadEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement523: BinaryAssociation = BinaryAssociation(
    name="modelElement523",
    ends={
        Property(name="ModelElementId525", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent524", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dragSourceElement526: BinaryAssociation = BinaryAssociation(
    name="dragSourceElement526",
    ends={
        Property(name="ModelElementId527", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dropTargetElement528: BinaryAssociation = BinaryAssociation(
    name="dropTargetElement528",
    ends={
        Property(name="ModelElementId530", type=esmodel_events_DNDEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_DNDEvent529", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElement531: BinaryAssociation = BinaryAssociation(
    name="sourceElement531",
    ends={
        Property(name="ModelElementId532", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetElement533: BinaryAssociation = BinaryAssociation(
    name="targetElement533",
    ends={
        Property(name="ModelElementId535", type=esmodel_events_LinkEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_LinkEvent534", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseVersion508: BinaryAssociation = BinaryAssociation(
    name="baseVersion508",
    ends={
        Property(name="versioning_PrimaryVersionSpec509", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion510: BinaryAssociation = BinaryAssociation(
    name="targetVersion510",
    ends={
        Property(name="versioning_PrimaryVersionSpec512", type=esmodel_events_UpdateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UpdateEvent511", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotatedElement513: BinaryAssociation = BinaryAssociation(
    name="annotatedElement513",
    ends={
        Property(name="ModelElementId514", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotation515: BinaryAssociation = BinaryAssociation(
    name="annotation515",
    ends={
        Property(name="ModelElementId517", type=esmodel_events_AnnotationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_AnnotationEvent516", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion518: BinaryAssociation = BinaryAssociation(
    name="sourceVersion518",
    ends={
        Property(name="versioning_PrimaryVersionSpec519", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion520: BinaryAssociation = BinaryAssociation(
    name="targetVersion520",
    ends={
        Property(name="versioning_PrimaryVersionSpec522", type=esmodel_events_ShowHistoryEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowHistoryEvent521", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation546: BinaryAssociation = BinaryAssociation(
    name="operation546",
    ends={
        Property(name="operations_AbstractOperation547", type=esmodel_events_UndoEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_UndoEvent", type=operations_AbstractOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceVersion548: BinaryAssociation = BinaryAssociation(
    name="sourceVersion548",
    ends={
        Property(name="versioning_PrimaryVersionSpec549", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVersion550: BinaryAssociation = BinaryAssociation(
    name="targetVersion550",
    ends={
        Property(name="versioning_PrimaryVersionSpec552", type=esmodel_events_ShowChangesEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_ShowChangesEvent551", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notifications553: BinaryAssociation = BinaryAssociation(
    name="notifications553",
    ends={
        Property(name="notification_ESNotification554", type=esmodel_events_NotificationGenerationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NotificationGenerationEvent", type=notification_ESNotification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceElement536: BinaryAssociation = BinaryAssociation(
    name="sourceElement536",
    ends={
        Property(name="ModelElementId537", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_TraceEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetElement538: BinaryAssociation = BinaryAssociation(
    name="targetElement538",
    ends={
        Property(name="ModelElementId540", type=esmodel_events_TraceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_TraceEvent539", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createdElement541: BinaryAssociation = BinaryAssociation(
    name="createdElement541",
    ends={
        Property(name="ModelElementId542", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceSection543: BinaryAssociation = BinaryAssociation(
    name="sourceSection543",
    ends={
        Property(name="ModelElementId545", type=esmodel_events_NavigatorCreateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_NavigatorCreateEvent544", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectId567: BinaryAssociation = BinaryAssociation(
    name="projectId567",
    ends={
        Property(name="ProjectId568", type=esmodel_server_ServerProjectEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ServerProjectEvent", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceModelElement555: BinaryAssociation = BinaryAssociation(
    name="sourceModelElement555",
    ends={
        Property(name="ModelElementId556", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceURL557: BinaryAssociation = BinaryAssociation(
    name="sourceURL557",
    ends={
        Property(name="ModelElementId559", type=esmodel_events_URLEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_URLEvent558", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
myAcceptedChanges560: BinaryAssociation = BinaryAssociation(
    name="myAcceptedChanges560",
    ends={
        Property(name="operations_OperationId", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theirRejectedChanges561: BinaryAssociation = BinaryAssociation(
    name="theirRejectedChanges561",
    ends={
        Property(name="operations_OperationId563", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent562", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextModelElement564: BinaryAssociation = BinaryAssociation(
    name="contextModelElement564",
    ends={
        Property(name="ModelElementId566", type=esmodel_events_MergeChoiceEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_events_MergeChoiceEvent565", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project575: BinaryAssociation = BinaryAssociation(
    name="project575",
    ends={
        Property(name="ProjectId576", type=esmodel_accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_OrgUnitProperty", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newVersion569: BinaryAssociation = BinaryAssociation(
    name="newVersion569",
    ends={
        Property(name="versioning_PrimaryVersionSpec570", type=esmodel_server_ProjectUpdatedEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_server_ProjectUpdatedEvent", type=versioning_PrimaryVersionSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles571: BinaryAssociation = BinaryAssociation(
    name="roles571",
    ends={
        Property(name="roles_Role", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit", type=roles_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties572: BinaryAssociation = BinaryAssociation(
    name="properties572",
    ends={
        Property(name="accesscontrol_OrgUnitProperty", type=esmodel_accesscontrol_ACOrgUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACOrgUnit573", type=accesscontrol_OrgUnitProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members574: BinaryAssociation = BinaryAssociation(
    name="members574",
    ends={
        Property(name="accesscontrol_ACOrgUnit", type=esmodel_accesscontrol_ACGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_accesscontrol_ACGroup", type=accesscontrol_ACOrgUnit, multiplicity=Multiplicity(0, 9999))
    }
)
relatedModelElements581: BinaryAssociation = BinaryAssociation(
    name="relatedModelElements581",
    ends={
        Property(name="ModelElementId583", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification582", type=ModelElementId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedOperations584: BinaryAssociation = BinaryAssociation(
    name="relatedOperations584",
    ends={
        Property(name="operations_OperationId586", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification585", type=operations_OperationId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectId587: BinaryAssociation = BinaryAssociation(
    name="projectId587",
    ends={
        Property(name="ProjectId588", type=esmodel_url_ProjectUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ProjectUrlFragment", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementId589: BinaryAssociation = BinaryAssociation(
    name="modelElementId589",
    ends={
        Property(name="ModelElementId590", type=esmodel_url_ModelElementUrlFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrlFragment", type=ModelElementId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serverUrl591: BinaryAssociation = BinaryAssociation(
    name="serverUrl591",
    ends={
        Property(name="url_ServerUrl", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl", type=url_ServerUrl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projects577: BinaryAssociation = BinaryAssociation(
    name="projects577",
    ends={
        Property(name="ProjectId578", type=esmodel_roles_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_roles_Role", type=ProjectId, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project579: BinaryAssociation = BinaryAssociation(
    name="project579",
    ends={
        Property(name="ProjectId580", type=esmodel_notification_ESNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_notification_ESNotification", type=ProjectId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projectUrlFragment592: BinaryAssociation = BinaryAssociation(
    name="projectUrlFragment592",
    ends={
        Property(name="url_ProjectUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl593", type=url_ProjectUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElementUrlFragment594: BinaryAssociation = BinaryAssociation(
    name="modelElementUrlFragment594",
    ends={
        Property(name="url_ModelElementUrlFragment", type=esmodel_url_ModelElementUrl, multiplicity=Multiplicity(1, 1)),
        Property(name="esmodel_url_ModelElementUrl595", type=url_ModelElementUrlFragment, multiplicity=Multiplicity(0, 1), is_composite=True)
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
gen_model_task_WorkItem_Annotation = Generalization(general=Annotation, specific=model_task_WorkItem)
gen_model_organization_Group_OrgUnit = Generalization(general=OrgUnit, specific=model_organization_Group)
gen_model_task_WorkPackage_WorkItem = Generalization(general=WorkItem, specific=model_task_WorkPackage)
gen_model_task_Milestone_WorkItem = Generalization(general=WorkItem, specific=model_task_Milestone)
gen_model_task_Checkable_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_task_Checkable)
gen_model_task_ActionItem_task_WorkItem = Generalization(general=task_WorkItem, specific=model_task_ActionItem)
gen_model_task_ActionItem_task_Checkable = Generalization(general=task_Checkable, specific=model_task_ActionItem)
gen_model_diagram_MEDiagram_Attachment = Generalization(general=Attachment, specific=model_diagram_MEDiagram)
gen_model_classes_PackageElement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_PackageElement)
gen_model_classes_Class_PackageElement = Generalization(general=PackageElement, specific=model_classes_Class)
gen_model_classes_Package_PackageElement = Generalization(general=PackageElement, specific=model_classes_Package)
gen_model_classes_Association_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Association)
gen_model_classes_Attribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Attribute)
gen_model_classes_MethodArgument_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_MethodArgument)
gen_model_classes_Method_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Method)
gen_model_document_Section_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_document_Section)
gen_model_classes_Dependency_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_classes_Dependency)
gen_model_document_CompositeSection_Section = Generalization(general=Section, specific=model_document_CompositeSection)
gen_model_document_LeafSection_Section = Generalization(general=Section, specific=model_document_LeafSection)
gen_model_requirement_FunctionalRequirement_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_FunctionalRequirement)
gen_model_requirement_UseCase_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UseCase)
gen_model_requirement_Scenario_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Scenario)
gen_model_requirement_Actor_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Actor)
gen_model_requirement_SystemFunction_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_SystemFunction)
gen_model_requirement_SystemFunction_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_SystemFunction)
gen_model_requirement_UserTask_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_UserTask)
gen_model_requirement_UserTask_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_UserTask)
gen_model_requirement_ActorInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_ActorInstance)
gen_model_requirement_Step_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_requirement_Step)
gen_model_requirement_Step_NonDomainElement = Generalization(general=NonDomainElement, specific=model_requirement_Step)
gen_model_rationale_Proposal_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Proposal)
gen_model_rationale_Proposal_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Proposal)
gen_model_requirement_NonFunctionalRequirement_Criterion = Generalization(general=Criterion, specific=model_requirement_NonFunctionalRequirement)
gen_model_rationale_Issue_Annotation = Generalization(general=Annotation, specific=model_rationale_Issue)
gen_model_rationale_Issue_task_Checkable = Generalization(general=task_Checkable, specific=model_rationale_Issue)
gen_model_rationale_Issue_task_WorkItem = Generalization(general=task_WorkItem, specific=model_rationale_Issue)
gen_model_rationale_Comment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Comment)
gen_model_rationale_Solution_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Solution)
gen_model_rationale_Solution_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Solution)
gen_model_rationale_Criterion_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Criterion)
gen_model_rationale_Assessment_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_rationale_Assessment)
gen_model_rationale_Assessment_NonDomainElement = Generalization(general=NonDomainElement, specific=model_rationale_Assessment)
gen_model_change_ModelChangePackage_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_change_ModelChangePackage)
gen_model_change_MergingIssue_Issue = Generalization(general=Issue, specific=model_change_MergingIssue)
gen_model_change_MergingProposal_Proposal = Generalization(general=Proposal, specific=model_change_MergingProposal)
gen_model_change_MergingSolution_Solution = Generalization(general=Solution, specific=model_change_MergingSolution)
gen_model_bug_BugReport_task_WorkItem = Generalization(general=task_WorkItem, specific=model_bug_BugReport)
gen_model_bug_BugReport_task_Checkable = Generalization(general=task_Checkable, specific=model_bug_BugReport)
gen_model_meeting_Meeting_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_Meeting)
gen_model_component_Component_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_Component)
gen_model_component_ComponentService_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_ComponentService)
gen_model_component_DeploymentNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_component_DeploymentNode)
gen_model_meeting_MeetingSection_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_meeting_MeetingSection)
gen_model_meeting_CompositeMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_CompositeMeetingSection)
gen_model_meeting_IssueMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_IssueMeetingSection)
gen_model_meeting_WorkItemMeetingSection_MeetingSection = Generalization(general=MeetingSection, specific=model_meeting_WorkItemMeetingSection)
gen_model_state_StateInitial_StateNode = Generalization(general=StateNode, specific=model_state_StateInitial)
gen_model_state_StateEnd_StateNode = Generalization(general=StateNode, specific=model_state_StateEnd)
gen_model_attachment_UrlAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_UrlAttachment)
gen_model_attachment_FileAttachment_Attachment = Generalization(general=Attachment, specific=model_attachment_FileAttachment)
gen_model_state_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_Transition)
gen_model_state_StateNode_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_state_StateNode)
gen_model_state_State_StateNode = Generalization(general=StateNode, specific=model_state_State)
gen_model_profile_Stereotype_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Stereotype)
gen_model_profile_StereotypeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeInstance)
gen_model_profile_Profile_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_Profile)
gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute = Generalization(general=StereotypeAttribute, specific=model_profile_StereotypeAttributeSimple)
gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttributeInstance)
gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance = Generalization(general=StereotypeAttributeInstance, specific=model_profile_StereotypeAttributeInstanceString)
gen_model_profile_StereotypeAttribute_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_profile_StereotypeAttribute)
gen_model_activity_Activity_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Activity)
gen_model_activity_Fork_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Fork)
gen_model_activity_Branch_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_Branch)
gen_model_activity_ActivityInitial_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityInitial)
gen_model_activity_ActivityEnd_ActivityObject = Generalization(general=ActivityObject, specific=model_activity_ActivityEnd)
gen_model_activity_ActivityObject_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_ActivityObject)
gen_model_activity_Transition_UnicaseModelElement = Generalization(general=UnicaseModelElement, specific=model_activity_Transition)
gen_esmodel_FileIdentifier_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_FileIdentifier)
gen_esmodel_versioning_TagVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_TagVersionSpec)
gen_esmodel_versioning_DateVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_DateVersionSpec)
gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_PrimaryVersionSpec)
gen_esmodel_SessionId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_SessionId)
gen_esmodel_ProjectId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_ProjectId)
gen_esmodel_operations_CompositeOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CompositeOperation)
gen_esmodel_operations_FeatureOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_FeatureOperation)
gen_esmodel_operations_CreateDeleteOperation_AbstractOperation = Generalization(general=AbstractOperation, specific=esmodel_operations_CreateDeleteOperation)
gen_esmodel_operations_AttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_AttributeOperation)
gen_esmodel_versioning_HeadVersionSpec_VersionSpec = Generalization(general=VersionSpec, specific=esmodel_versioning_HeadVersionSpec)
gen_esmodel_operations_AbstractOperation_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_operations_AbstractOperation)
gen_esmodel_operations_MultiAttributeOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeOperation)
gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeSetOperation)
gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiAttributeMoveOperation)
gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_MultiReferenceMoveOperation)
gen_esmodel_operations_ReferenceOperation_FeatureOperation = Generalization(general=FeatureOperation, specific=esmodel_operations_ReferenceOperation)
gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation = Generalization(general=AttributeOperation, specific=esmodel_operations_DiagramLayoutOperation)
gen_esmodel_operations_OperationId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_operations_OperationId)
gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_SingleReferenceOperation)
gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceSetOperation)
gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation = Generalization(general=ReferenceOperation, specific=esmodel_operations_MultiReferenceOperation)
gen_esmodel_events_MergeEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeEvent)
gen_esmodel_events_CheckoutEvent_Event = Generalization(general=Event, specific=esmodel_events_CheckoutEvent)
gen_esmodel_events_ExceptionEvent_Event = Generalization(general=Event, specific=esmodel_events_ExceptionEvent)
gen_esmodel_events_PluginStartEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginStartEvent)
gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation = Generalization(general=CompositeOperation, specific=esmodel_semantic_SemanticCompositeOperation)
gen_esmodel_events_ReadEvent_Event = Generalization(general=Event, specific=esmodel_events_ReadEvent)
gen_esmodel_events_PerspectiveEvent_Event = Generalization(general=Event, specific=esmodel_events_PerspectiveEvent)
gen_esmodel_events_DNDEvent_Event = Generalization(general=Event, specific=esmodel_events_DNDEvent)
gen_esmodel_events_LinkEvent_Event = Generalization(general=Event, specific=esmodel_events_LinkEvent)
gen_esmodel_events_UpdateEvent_Event = Generalization(general=Event, specific=esmodel_events_UpdateEvent)
gen_esmodel_events_AnnotationEvent_Event = Generalization(general=Event, specific=esmodel_events_AnnotationEvent)
gen_esmodel_events_RevertEvent_Event = Generalization(general=Event, specific=esmodel_events_RevertEvent)
gen_esmodel_events_ShowHistoryEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowHistoryEvent)
gen_esmodel_events_UndoEvent_Event = Generalization(general=Event, specific=esmodel_events_UndoEvent)
gen_esmodel_events_Validate_Event = Generalization(general=Event, specific=esmodel_events_Validate)
gen_esmodel_events_ShowChangesEvent_Event = Generalization(general=Event, specific=esmodel_events_ShowChangesEvent)
gen_esmodel_events_NotificationReadEvent_ReadEvent = Generalization(general=ReadEvent, specific=esmodel_events_NotificationReadEvent)
gen_esmodel_events_NotificationGenerationEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationGenerationEvent)
gen_esmodel_events_TraceEvent_Event = Generalization(general=Event, specific=esmodel_events_TraceEvent)
gen_esmodel_events_NavigatorCreateEvent_Event = Generalization(general=Event, specific=esmodel_events_NavigatorCreateEvent)
gen_esmodel_events_PluginFocusEvent_Event = Generalization(general=Event, specific=esmodel_events_PluginFocusEvent)
gen_esmodel_events_PresentationSwitchEvent_Event = Generalization(general=Event, specific=esmodel_events_PresentationSwitchEvent)
gen_esmodel_events_MergeGlobalChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeGlobalChoiceEvent)
gen_esmodel_server_ServerEvent_Event = Generalization(general=Event, specific=esmodel_server_ServerEvent)
gen_esmodel_server_ServerProjectEvent_ServerEvent = Generalization(general=ServerEvent, specific=esmodel_server_ServerProjectEvent)
gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent = Generalization(general=ServerProjectEvent, specific=esmodel_server_ProjectUpdatedEvent)
gen_esmodel_events_NotificationIgnoreEvent_Event = Generalization(general=Event, specific=esmodel_events_NotificationIgnoreEvent)
gen_esmodel_events_URLEvent_Event = Generalization(general=Event, specific=esmodel_events_URLEvent)
gen_esmodel_events_MergeChoiceEvent_Event = Generalization(general=Event, specific=esmodel_events_MergeChoiceEvent)
gen_esmodel_accesscontrol_ACUser_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACUser)
gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_accesscontrol_ACOrgUnit)
gen_esmodel_accesscontrol_ACGroup_ACOrgUnit = Generalization(general=ACOrgUnit, specific=esmodel_accesscontrol_ACGroup)
gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier = Generalization(general=UniqueIdentifier, specific=esmodel_accesscontrol_ACOrgUnitId)
gen_esmodel_roles_ReaderRole_Role = Generalization(general=Role, specific=esmodel_roles_ReaderRole)
gen_esmodel_roles_WriterRole_Role = Generalization(general=Role, specific=esmodel_roles_WriterRole)
gen_esmodel_roles_ProjectAdminRole_Role = Generalization(general=Role, specific=esmodel_roles_ProjectAdminRole)
gen_esmodel_roles_ServerAdmin_Role = Generalization(general=Role, specific=esmodel_roles_ServerAdmin)
gen_esmodel_notification_ESNotification_IdentifiableElement = Generalization(general=IdentifiableElement, specific=esmodel_notification_ESNotification)

# Domain Model
domain_model = DomainModel(
    name="esmodel",
    types={metamodel_Project, ModelElement, metamodel_ModelElement, IdentifiableElement, metamodel_ModelElementId, UniqueIdentifier, metamodel_ModelVersion, metamodel_NonDomainElement, metamodel_AssociationClassElement, model_UnicaseModelElement, Annotation, Attachment, document_LeafSection, metamodel_UniqueIdentifier, metamodel_IdentifiableElement, model_Annotation, UnicaseModelElement, model_Attachment, model_NonDomainElement, model_Project, Project, model_organization_OrgUnit, organization_Group, task_WorkItem, model_organization_User, OrgUnit, rationale_Comment, profile_StereotypeInstance, model_task_WorkItem, task_WorkPackage, organization_User, model_organization_Group, organization_OrgUnit, change_ModelChangePackage, model_task_WorkPackage, WorkItem, model_task_Milestone, model_task_Checkable, model_task_ActionItem, task_Checkable, model_diagram_MEDiagram, diagram_model_Diagram, model_classes_PackageElement, classes_Package, classes_Dependency, model_classes_Class, PackageElement, classes_Class, classes_Association, classes_Attribute, classes_Method, requirement_UseCase, requirement_Scenario, model_classes_Package, model_classes_Association, model_classes_Attribute, classes_PackageElement, classes_MethodArgument, model_classes_MethodArgument, model_classes_Method, model_document_Section, document_CompositeSection, model_classes_Dependency, model_document_CompositeSection, model_document_LeafSection, Section, document_Section, model_requirement_FunctionalRequirement, requirement_FunctionalRequirement, requirement_Actor, model_requirement_UseCase, model_requirement_Scenario, requirement_Step, requirement_UserTask, requirement_NonFunctionalRequirement, model_requirement_Actor, requirement_ActorInstance, requirement_SystemFunction, model_requirement_SystemFunction, model_requirement_UserTask, model_requirement_ActorInstance, model_requirement_Step, NonDomainElement, rationale_Proposal, rationale_Solution, rationale_Criterion, model_rationale_Proposal, rationale_Issue, model_requirement_NonFunctionalRequirement, Criterion, model_rationale_Issue, model_rationale_Comment, rationale_Assessment, model_rationale_Solution, model_rationale_Criterion, model_rationale_Assessment, model_change_ModelChangePackage, model_change_MergingIssue, Issue, model_change_MergingProposal, Proposal, change_MergingProposal, model_change_MergingSolution, Solution, model_bug_BugReport, model_meeting_Meeting, model_component_Component, component_ComponentService, model_component_ComponentService, component_Component, model_component_DeploymentNode, model_meeting_MeetingSection, model_meeting_CompositeMeetingSection, MeetingSection, model_meeting_IssueMeetingSection, model_meeting_WorkItemMeetingSection, meeting_MeetingSection, meeting_IssueMeetingSection, meeting_WorkItemMeetingSection, model_state_StateInitial, model_state_StateEnd, model_attachment_UrlAttachment, model_attachment_FileAttachment, model_state_Transition, state_StateNode, model_state_StateNode, state_Transition, model_state_State, StateNode, model_profile_Stereotype, profile_Profile, profile_StereotypeAttribute, model_profile_StereotypeInstance, model_profile_Profile, profile_Stereotype, model_profile_StereotypeAttributeSimple, StereotypeAttribute, model_profile_StereotypeAttributeInstance, model_profile_StereotypeAttributeInstanceString, StereotypeAttributeInstance, model_util_ModelElementPath, profile_StereotypeAttributeInstance, model_profile_StereotypeAttribute, model_activity_Activity, ActivityObject, model_activity_Fork, model_activity_Branch, model_activity_ActivityInitial, model_activity_ActivityEnd, esmodel_ProjectHistory, ProjectId, versioning_Version, esmodel_ProjectInfo, ModelElementId, model_activity_ActivityObject, activity_Transition, model_activity_Transition, activity_ActivityObject, esmodel_FileIdentifier, esmodel_versioning_TagVersionSpec, VersionSpec, esmodel_versioning_DateVersionSpec, esmodel_versioning_PrimaryVersionSpec, esmodel_versioning_VersionSpec, esmodel_versioning_LogMessage, esmodel_versioning_ChangePackage, operations_AbstractOperation, versioning_PrimaryVersionSpec, esmodel_SessionId, esmodel_ServerSpace, accesscontrol_ACGroup, ProjectHistory, SessionId, accesscontrol_ACUser, esmodel_ProjectId, esmodel_VersionInfo, esmodel_ClientVersionInfo, esmodel_versioning_HistoryQuery, esmodel_versioning_Version, events_Event, versioning_LogMessage, notification_ESNotification, versioning_VersionProperty, esmodel_versioning_HistoryInfo, versioning_TagVersionSpec, versioning_ChangePackage, esmodel_operations_FeatureOperation, esmodel_operations_CreateDeleteOperation, operations_esmodel_EObject, operations_ReferenceOperation, operations_EObjectToModelElementIdMap, esmodel_operations_AttributeOperation, FeatureOperation, esmodel_versioning_HeadVersionSpec, esmodel_versioning_VersionProperty, esmodel_operations_AbstractOperation, esmodel_operations_CompositeOperation, AbstractOperation, esmodel_operations_MultiAttributeOperation, esmodel_operations_MultiAttributeSetOperation, esmodel_operations_MultiAttributeMoveOperation, esmodel_operations_MultiReferenceMoveOperation, esmodel_operations_ReferenceOperation, esmodel_operations_DiagramLayoutOperation, AttributeOperation, esmodel_operations_OperationId, esmodel_operations_OperationGroup, esmodel_operations_ModelElementGroup, esmodel_operations_SingleReferenceOperation, ReferenceOperation, esmodel_operations_MultiReferenceSetOperation, esmodel_operations_MultiReferenceOperation, esmodel_events_MergeEvent, esmodel_events_CheckoutEvent, esmodel_events_ExceptionEvent, esmodel_events_PluginStartEvent, esmodel_operations_EObjectToModelElementIdMap, esmodel_semantic_SemanticCompositeOperation, CompositeOperation, esmodel_events_Event, esmodel_events_ReadEvent, Event, esmodel_events_PerspectiveEvent, esmodel_events_DNDEvent, esmodel_events_LinkEvent, esmodel_events_UpdateEvent, esmodel_events_AnnotationEvent, esmodel_events_RevertEvent, esmodel_events_ShowHistoryEvent, esmodel_events_UndoEvent, esmodel_events_Validate, esmodel_events_ShowChangesEvent, esmodel_events_NotificationReadEvent, ReadEvent, esmodel_events_NotificationGenerationEvent, esmodel_events_NotificationIgnoreEvent, esmodel_events_TraceEvent, esmodel_events_NavigatorCreateEvent, esmodel_events_PluginFocusEvent, esmodel_events_PresentationSwitchEvent, esmodel_events_MergeGlobalChoiceEvent, esmodel_server_ServerEvent, esmodel_server_ServerProjectEvent, ServerEvent, esmodel_server_ProjectUpdatedEvent, ServerProjectEvent, esmodel_events_URLEvent, esmodel_events_MergeChoiceEvent, operations_OperationId, esmodel_accesscontrol_OrgUnitProperty, esmodel_roles_Role, esmodel_accesscontrol_ACUser, ACOrgUnit, esmodel_accesscontrol_ACOrgUnit, roles_Role, accesscontrol_OrgUnitProperty, esmodel_accesscontrol_ACGroup, accesscontrol_ACOrgUnit, esmodel_accesscontrol_ACOrgUnitId, esmodel_url_ServerUrl, esmodel_url_ProjectUrlFragment, esmodel_url_ModelElementUrlFragment, esmodel_url_ModelElementUrl, url_ServerUrl, url_ProjectUrlFragment, esmodel_roles_ReaderRole, Role, esmodel_roles_WriterRole, esmodel_roles_ProjectAdminRole, esmodel_roles_ServerAdmin, esmodel_notification_ESNotification, url_ModelElementUrlFragment, ActivityType, DiagramType, AssociationType, VisibilityType, ScopeType, ArgumentDirectionType, BugStatus, Severity, ResolutionType, ContainmentType, MergeChoiceSelection, MergeGlobalChoiceSelection},
    associations={modelElements0, annotations4, attachments5, leafSection8, incomingDocumentReferences11, cutElements1, annotatedModelElements20, referringModelElements23, groupMemberships26, participations29, assignments32, comments14, appliedStereotypeInstances17, orgUnits38, containingWorkpackage41, successors44, predecessors47, assignee50, reviewer53, participants56, workItemsToReview35, associatedChangePackages59, containedWorkItems60, containedModelElements63, elements64, gmfdiagram66, newElements68, parentPackage71, outgoingDependencies74, incomingDependencies77, subClasses80, outgoingAssociations86, incomingAssociations89, attributes92, methods95, participatedUseCases98, demoParticipations101, facadeClass104, superClasses83, source108, target111, definingClass114, containedPackageElements105, callingMethods123, arguments126, demoParticipations127, definingClass117, calledMethods120, source130, target133, parent136, modelElements139, referencedModelElements142, refinedRequirement151, stakeholder154, useCases155, subsections145, refiningRequirements148, includedUseCases167, extendedUseCases168, scenarios171, initiatingActor174, scenarios158, functionalRequirements161, identifiedClasses164, instantiatedUseCases189, functionalRequirements192, participatingActors177, useCaseSteps180, realizedUserTask183, nonFunctionalRequirements186, initiatedUseCases211, participatedUseCases214, instances217, participatingMethods195, participatingClasses198, initiatingActorInstance201, participatingActorInstances204, steps207, nonFunctionalRequirements208, includedUseCase235, useCase237, includedSystemFunction240, initiatingActor242, participatingActor245, participatedUserTasks220, initiatedUserTask223, initiatedScenarios226, participatedScenarios229, instantiatedActor232, proposals257, solution260, criteria263, issue264, realizingUseCases248, restrictedUseCases251, restrictedScenarios254, proposal277, criterion280, sender283, recipients285, commentedElement288, assessments267, underlyingProposals270, issue271, assessments274, conflictingProposals291, pendingChanges292, appliedChanges295, components313, facilitator314, packages297, subsystems298, offeredServices301, consumedServices304, offeringComponent307, consumingComponents310, identifiedWorkItemsSection328, subsections330, includedIssues332, minutetaker315, timekeeper318, participants321, sections324, identifiedIssuesSection326, includedWorkItems333, source334, target337, outgoingTransitions340, incomingTransitions343, profile351, stereotypeInstances354, stereotypeAttributes357, stereotype360, affectedContainers346, stereotypes348, stereotype369, stereotypeAttributeInstances372, stereotypeInstance375, stereotypeAttribute378, modelElement363, stereotypeAttributeInstances366, target397, projectId400, versions401, source381, target382, path385, outgoingTransitions388, incomingTransitions391, source394, operations414, projectId403, version405, groups407, projects408, openSessions410, users412, changePackage433, source435, target437, modelElements440, projectState443, primarySpec444, tagSpecs447, nextVersion450, events415, logMessage417, notifications419, versionProperties421, primerySpec423, logMessage425, tagSpecs428, versionProperties430, subOperations463, mainOperation465, modelElement468, subOperations469, eObjectToIdMap471, previousVersion452, changes455, logMessage458, modelElementId461, referencedModelElements483, referencedModelElementId485, operations487, modelElements489, oldValue473, newValue475, oldValue478, newValue480, baseVersion498, targetVersion500, localChanges503, baseVersion506, key491, value493, modelElement496, modelElement523, dragSourceElement526, dropTargetElement528, sourceElement531, targetElement533, baseVersion508, targetVersion510, annotatedElement513, annotation515, sourceVersion518, targetVersion520, operation546, sourceVersion548, targetVersion550, notifications553, sourceElement536, targetElement538, createdElement541, sourceSection543, projectId567, sourceModelElement555, sourceURL557, myAcceptedChanges560, theirRejectedChanges561, contextModelElement564, project575, newVersion569, roles571, properties572, members574, relatedModelElements581, relatedOperations584, projectId587, modelElementId589, serverUrl591, projects577, project579, projectUrlFragment592, modelElementUrlFragment594},
    generalizations={gen_metamodel_ModelElement_IdentifiableElement, gen_metamodel_ModelElementId_UniqueIdentifier, gen_model_UnicaseModelElement_ModelElement, gen_model_Annotation_UnicaseModelElement, gen_model_Attachment_UnicaseModelElement, gen_model_Project_Project, gen_model_organization_OrgUnit_UnicaseModelElement, gen_model_organization_User_OrgUnit, gen_model_task_WorkItem_Annotation, gen_model_organization_Group_OrgUnit, gen_model_task_WorkPackage_WorkItem, gen_model_task_Milestone_WorkItem, gen_model_task_Checkable_UnicaseModelElement, gen_model_task_ActionItem_task_WorkItem, gen_model_task_ActionItem_task_Checkable, gen_model_diagram_MEDiagram_Attachment, gen_model_classes_PackageElement_UnicaseModelElement, gen_model_classes_Class_PackageElement, gen_model_classes_Package_PackageElement, gen_model_classes_Association_UnicaseModelElement, gen_model_classes_Attribute_UnicaseModelElement, gen_model_classes_MethodArgument_UnicaseModelElement, gen_model_classes_Method_UnicaseModelElement, gen_model_document_Section_UnicaseModelElement, gen_model_classes_Dependency_UnicaseModelElement, gen_model_document_CompositeSection_Section, gen_model_document_LeafSection_Section, gen_model_requirement_FunctionalRequirement_UnicaseModelElement, gen_model_requirement_UseCase_UnicaseModelElement, gen_model_requirement_Scenario_UnicaseModelElement, gen_model_requirement_Actor_UnicaseModelElement, gen_model_requirement_SystemFunction_UnicaseModelElement, gen_model_requirement_SystemFunction_NonDomainElement, gen_model_requirement_UserTask_UnicaseModelElement, gen_model_requirement_UserTask_NonDomainElement, gen_model_requirement_ActorInstance_UnicaseModelElement, gen_model_requirement_Step_UnicaseModelElement, gen_model_requirement_Step_NonDomainElement, gen_model_rationale_Proposal_UnicaseModelElement, gen_model_rationale_Proposal_NonDomainElement, gen_model_requirement_NonFunctionalRequirement_Criterion, gen_model_rationale_Issue_Annotation, gen_model_rationale_Issue_task_Checkable, gen_model_rationale_Issue_task_WorkItem, gen_model_rationale_Comment_UnicaseModelElement, gen_model_rationale_Solution_UnicaseModelElement, gen_model_rationale_Solution_NonDomainElement, gen_model_rationale_Criterion_UnicaseModelElement, gen_model_rationale_Assessment_UnicaseModelElement, gen_model_rationale_Assessment_NonDomainElement, gen_model_change_ModelChangePackage_UnicaseModelElement, gen_model_change_MergingIssue_Issue, gen_model_change_MergingProposal_Proposal, gen_model_change_MergingSolution_Solution, gen_model_bug_BugReport_task_WorkItem, gen_model_bug_BugReport_task_Checkable, gen_model_meeting_Meeting_UnicaseModelElement, gen_model_component_Component_UnicaseModelElement, gen_model_component_ComponentService_UnicaseModelElement, gen_model_component_DeploymentNode_UnicaseModelElement, gen_model_meeting_MeetingSection_UnicaseModelElement, gen_model_meeting_CompositeMeetingSection_MeetingSection, gen_model_meeting_IssueMeetingSection_MeetingSection, gen_model_meeting_WorkItemMeetingSection_MeetingSection, gen_model_state_StateInitial_StateNode, gen_model_state_StateEnd_StateNode, gen_model_attachment_UrlAttachment_Attachment, gen_model_attachment_FileAttachment_Attachment, gen_model_state_Transition_UnicaseModelElement, gen_model_state_StateNode_UnicaseModelElement, gen_model_state_State_StateNode, gen_model_profile_Stereotype_UnicaseModelElement, gen_model_profile_StereotypeInstance_UnicaseModelElement, gen_model_profile_Profile_UnicaseModelElement, gen_model_profile_StereotypeAttributeSimple_StereotypeAttribute, gen_model_profile_StereotypeAttributeInstance_UnicaseModelElement, gen_model_profile_StereotypeAttributeInstanceString_StereotypeAttributeInstance, gen_model_profile_StereotypeAttribute_UnicaseModelElement, gen_model_activity_Activity_ActivityObject, gen_model_activity_Fork_ActivityObject, gen_model_activity_Branch_ActivityObject, gen_model_activity_ActivityInitial_ActivityObject, gen_model_activity_ActivityEnd_ActivityObject, gen_model_activity_ActivityObject_UnicaseModelElement, gen_model_activity_Transition_UnicaseModelElement, gen_esmodel_FileIdentifier_IdentifiableElement, gen_esmodel_versioning_TagVersionSpec_VersionSpec, gen_esmodel_versioning_DateVersionSpec_VersionSpec, gen_esmodel_versioning_PrimaryVersionSpec_VersionSpec, gen_esmodel_SessionId_UniqueIdentifier, gen_esmodel_ProjectId_UniqueIdentifier, gen_esmodel_operations_CompositeOperation_AbstractOperation, gen_esmodel_operations_FeatureOperation_AbstractOperation, gen_esmodel_operations_CreateDeleteOperation_AbstractOperation, gen_esmodel_operations_AttributeOperation_FeatureOperation, gen_esmodel_versioning_HeadVersionSpec_VersionSpec, gen_esmodel_operations_AbstractOperation_IdentifiableElement, gen_esmodel_operations_MultiAttributeOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeSetOperation_FeatureOperation, gen_esmodel_operations_MultiAttributeMoveOperation_FeatureOperation, gen_esmodel_operations_MultiReferenceMoveOperation_FeatureOperation, gen_esmodel_operations_ReferenceOperation_FeatureOperation, gen_esmodel_operations_DiagramLayoutOperation_AttributeOperation, gen_esmodel_operations_OperationId_UniqueIdentifier, gen_esmodel_operations_SingleReferenceOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceSetOperation_ReferenceOperation, gen_esmodel_operations_MultiReferenceOperation_ReferenceOperation, gen_esmodel_events_MergeEvent_Event, gen_esmodel_events_CheckoutEvent_Event, gen_esmodel_events_ExceptionEvent_Event, gen_esmodel_events_PluginStartEvent_Event, gen_esmodel_semantic_SemanticCompositeOperation_CompositeOperation, gen_esmodel_events_ReadEvent_Event, gen_esmodel_events_PerspectiveEvent_Event, gen_esmodel_events_DNDEvent_Event, gen_esmodel_events_LinkEvent_Event, gen_esmodel_events_UpdateEvent_Event, gen_esmodel_events_AnnotationEvent_Event, gen_esmodel_events_RevertEvent_Event, gen_esmodel_events_ShowHistoryEvent_Event, gen_esmodel_events_UndoEvent_Event, gen_esmodel_events_Validate_Event, gen_esmodel_events_ShowChangesEvent_Event, gen_esmodel_events_NotificationReadEvent_ReadEvent, gen_esmodel_events_NotificationGenerationEvent_Event, gen_esmodel_events_TraceEvent_Event, gen_esmodel_events_NavigatorCreateEvent_Event, gen_esmodel_events_PluginFocusEvent_Event, gen_esmodel_events_PresentationSwitchEvent_Event, gen_esmodel_events_MergeGlobalChoiceEvent_Event, gen_esmodel_server_ServerEvent_Event, gen_esmodel_server_ServerProjectEvent_ServerEvent, gen_esmodel_server_ProjectUpdatedEvent_ServerProjectEvent, gen_esmodel_events_NotificationIgnoreEvent_Event, gen_esmodel_events_URLEvent_Event, gen_esmodel_events_MergeChoiceEvent_Event, gen_esmodel_accesscontrol_ACUser_ACOrgUnit, gen_esmodel_accesscontrol_ACOrgUnit_IdentifiableElement, gen_esmodel_accesscontrol_ACGroup_ACOrgUnit, gen_esmodel_accesscontrol_ACOrgUnitId_UniqueIdentifier, gen_esmodel_roles_ReaderRole_Role, gen_esmodel_roles_WriterRole_Role, gen_esmodel_roles_ProjectAdminRole_Role, gen_esmodel_roles_ServerAdmin_Role, gen_esmodel_notification_ESNotification_IdentifiableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)