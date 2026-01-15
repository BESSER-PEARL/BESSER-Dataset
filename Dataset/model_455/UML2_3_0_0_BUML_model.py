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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate")
    }
)

ConnectorKind: Enumeration = Enumeration(
    name="ConnectorKind",
    literals={
            EnumerationLiteral(name="assembly"),
			EnumerationLiteral(name="delegation")
    }
)

CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

ParameterEffectKind: Enumeration = Enumeration(
    name="ParameterEffectKind",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
    }
)

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="lost"),
			EnumerationLiteral(name="found"),
			EnumerationLiteral(name="unknown")
    }
)

MessageSort: Enumeration = Enumeration(
    name="MessageSort",
    literals={
            EnumerationLiteral(name="synchCall"),
			EnumerationLiteral(name="asynchCall"),
			EnumerationLiteral(name="asynchSignal"),
			EnumerationLiteral(name="createMessage"),
			EnumerationLiteral(name="deleteMessage"),
			EnumerationLiteral(name="reply")
    }
)

InteractionOperatorKind: Enumeration = Enumeration(
    name="InteractionOperatorKind",
    literals={
            EnumerationLiteral(name="seq"),
			EnumerationLiteral(name="alt"),
			EnumerationLiteral(name="opt"),
			EnumerationLiteral(name="break"),
			EnumerationLiteral(name="par"),
			EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="critical"),
			EnumerationLiteral(name="neg"),
			EnumerationLiteral(name="assert"),
			EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="consider")
    }
)

ExpansionKind: Enumeration = Enumeration(
    name="ExpansionKind",
    literals={
            EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="iterative"),
			EnumerationLiteral(name="stream")
    }
)

# Classes
uml_Comment = Class(name="uml::Comment")
Element = Class(name="Element")
TemplateableElement = Class(name="TemplateableElement")
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_PackageMerge = Class(name="uml::PackageMerge")
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
uml_ProfileApplication = Class(name="uml::ProfileApplication")
NamedElement = Class(name="NamedElement")
ParameterableElement = Class(name="ParameterableElement")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
uml_Element = Class(name="uml::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
uml_Package = Class(name="uml::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
DirectedRelationship = Class(name="DirectedRelationship")
uml_DirectedRelationship = Class(name="uml::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
uml_Relationship = Class(name="uml::Relationship", is_abstract=True)
uml_ElementImport = Class(name="uml::ElementImport")
uml_PackageImport = Class(name="uml::PackageImport")
uml_Dependency = Class(name="uml::Dependency")
uml_Namespace = Class(name="uml::Namespace", is_abstract=True)
uml_StringExpression = Class(name="uml::StringExpression")
uml_ValueSpecification = Class(name="uml::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)
uml_Constraint = Class(name="uml::Constraint")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
uml_Generalization = Class(name="uml::Generalization")
uml_GeneralizationSet = Class(name="uml::GeneralizationSet")
uml_Feature = Class(name="uml::Feature", is_abstract=True)
uml_Substitution = Class(name="uml::Substitution")
uml_Association = Class(name="uml::Association")
Classifier = Class(name="Classifier")
uml_Property = Class(name="uml::Property")
uml_CollaborationUse = Class(name="uml::CollaborationUse")
uml_UseCase = Class(name="uml::UseCase")
uml_RedefinableElement = Class(name="uml::RedefinableElement", is_abstract=True)
uml_TemplateableElement = Class(name="uml::TemplateableElement", is_abstract=True)
uml_TemplateBinding = Class(name="uml::TemplateBinding")
uml_TemplateSignature = Class(name="uml::TemplateSignature")
uml_TemplateParameterSubstitution = Class(name="uml::TemplateParameterSubstitution")
uml_ParameterableElement = Class(name="uml::ParameterableElement", is_abstract=True)
uml_TemplateParameter = Class(name="uml::TemplateParameter")
uml_Realization = Class(name="uml::Realization")
Abstraction = Class(name="Abstraction")
uml_Abstraction = Class(name="uml::Abstraction")
Dependency = Class(name="Dependency")
uml_OpaqueExpression = Class(name="uml::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
Realization = Class(name="Realization")
uml_Operation = Class(name="uml::Operation")
uml_MultiplicityElement = Class(name="uml::MultiplicityElement", is_abstract=True)
uml_Parameter = Class(name="uml::Parameter")
uml_Behavior = Class(name="uml::Behavior", is_abstract=True)
ConnectableElement = Class(name="ConnectableElement")
MultiplicityElement = Class(name="MultiplicityElement")
uml_ParameterSet = Class(name="uml::ParameterSet")
uml_ConnectableElement = Class(name="uml::ConnectableElement", is_abstract=True)
uml_ConnectorEnd = Class(name="uml::ConnectorEnd")
uml_DataType = Class(name="uml::DataType")
StructuralFeature = Class(name="StructuralFeature")
DeploymentTarget = Class(name="DeploymentTarget")
uml_Class = Class(name="uml::Class")
uml_DeploymentTarget = Class(name="uml::DeploymentTarget", is_abstract=True)
uml_Deployment = Class(name="uml::Deployment")
Artifact = Class(name="Artifact")
uml_Artifact = Class(name="uml::Artifact")
DeployedArtifact = Class(name="DeployedArtifact")
uml_DeployedArtifact = Class(name="uml::DeployedArtifact", is_abstract=True)
uml_DeploymentSpecification = Class(name="uml::DeploymentSpecification")
BehavioralFeature = Class(name="BehavioralFeature")
uml_Interface = Class(name="uml::Interface")
uml_Manifestation = Class(name="uml::Manifestation")
uml_BehavioralFeature = Class(name="uml::BehavioralFeature", is_abstract=True)
Class_ = Class(name="Class")
uml_BehavioredClassifier = Class(name="uml::BehavioredClassifier", is_abstract=True)
Feature = Class(name="Feature")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
uml_InterfaceRealization = Class(name="uml::InterfaceRealization")
uml_Trigger = Class(name="uml::Trigger")
uml_Reception = Class(name="uml::Reception")
uml_Extension = Class(name="uml::Extension")
uml_ProtocolStateMachine = Class(name="uml::ProtocolStateMachine")
uml_Signal = Class(name="uml::Signal")
StateMachine = Class(name="StateMachine")
uml_ProtocolConformance = Class(name="uml::ProtocolConformance")
uml_Transition = Class(name="uml::Transition")
uml_StateMachine = Class(name="uml::StateMachine")
Behavior = Class(name="Behavior")
uml_Region = Class(name="uml::Region")
uml_State = Class(name="uml::State")
uml_Pseudostate = Class(name="uml::Pseudostate")
uml_Vertex = Class(name="uml::Vertex", is_abstract=True)
uml_Event = Class(name="uml::Event", is_abstract=True)
uml_Port = Class(name="uml::Port")
Property_ = Class(name="Property")
uml_ConnectionPointReference = Class(name="uml::ConnectionPointReference")
Vertex = Class(name="Vertex")
uml_EncapsulatedClassifier = Class(name="uml::EncapsulatedClassifier", is_abstract=True)
StructuredClassifier = Class(name="StructuredClassifier")
uml_StructuredClassifier = Class(name="uml::StructuredClassifier", is_abstract=True)
Association = Class(name="Association")
uml_ExtensionEnd = Class(name="uml::ExtensionEnd")
uml_Stereotype = Class(name="uml::Stereotype")
uml_Image = Class(name="uml::Image")
uml_Connector = Class(name="uml::Connector")
uml_OperationTemplateParameter = Class(name="uml::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
uml_StructuralFeature = Class(name="uml::StructuralFeature", is_abstract=True)
uml_ConnectableElementTemplateParameter = Class(name="uml::ConnectableElementTemplateParameter")
uml_Profile = Class(name="uml::Profile")
Package = Class(name="Package")
uml_Model = Class(name="uml::Model")
uml_Include = Class(name="uml::Include")
uml_Extend = Class(name="uml::Extend")
uml_ExtensionPoint = Class(name="uml::ExtensionPoint")
uml_Collaboration = Class(name="uml::Collaboration")
uml_ClassifierTemplateParameter = Class(name="uml::ClassifierTemplateParameter")
Expression = Class(name="Expression")
uml_Expression = Class(name="uml::Expression")
uml_RedefinableTemplateSignature = Class(name="uml::RedefinableTemplateSignature")
TemplateSignature = Class(name="TemplateSignature")
uml_Enumeration = Class(name="uml::Enumeration")
DataType = Class(name="DataType")
uml_EnumerationLiteral = Class(name="uml::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
uml_InstanceSpecification = Class(name="uml::InstanceSpecification")
uml_Slot = Class(name="uml::Slot")
uml_Usage = Class(name="uml::Usage")
uml_LiteralBoolean = Class(name="uml::LiteralBoolean")
uml_LiteralNull = Class(name="uml::LiteralNull")
uml_InstanceValue = Class(name="uml::InstanceValue")
uml_LiteralUnlimitedNatural = Class(name="uml::LiteralUnlimitedNatural")
uml_OpaqueBehavior = Class(name="uml::OpaqueBehavior")
uml_FunctionBehavior = Class(name="uml::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
uml_OpaqueAction = Class(name="uml::OpaqueAction")
Action = Class(name="Action")
uml_InputPin = Class(name="uml::InputPin")
uml_OutputPin = Class(name="uml::OutputPin")
uml_PrimitiveType = Class(name="uml::PrimitiveType")
uml_LiteralSpecification = Class(name="uml::LiteralSpecification", is_abstract=True)
uml_LiteralInteger = Class(name="uml::LiteralInteger")
LiteralSpecification = Class(name="LiteralSpecification")
uml_LiteralString = Class(name="uml::LiteralString")
uml_ExecutableNode = Class(name="uml::ExecutableNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
uml_ExceptionHandler = Class(name="uml::ExceptionHandler")
uml_ActivityNode = Class(name="uml::ActivityNode", is_abstract=True)
uml_StructuredActivityNode = Class(name="uml::StructuredActivityNode")
uml_Activity = Class(name="uml::Activity")
uml_ActivityEdge = Class(name="uml::ActivityEdge", is_abstract=True)
uml_ActivityPartition = Class(name="uml::ActivityPartition")
uml_InterruptibleActivityRegion = Class(name="uml::InterruptibleActivityRegion")
uml_Action = Class(name="uml::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
uml_ActivityGroup = Class(name="uml::ActivityGroup", is_abstract=True)
ActivityGroup = Class(name="ActivityGroup")
uml_Variable = Class(name="uml::Variable")
uml_ObjectNode = Class(name="uml::ObjectNode", is_abstract=True)
Pin = Class(name="Pin")
uml_Pin = Class(name="uml::Pin")
ObjectNode = Class(name="ObjectNode")
uml_CallAction = Class(name="uml::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
uml_InvocationAction = Class(name="uml::InvocationAction", is_abstract=True)
uml_SequenceNode = Class(name="uml::SequenceNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
uml_ControlNode = Class(name="uml::ControlNode", is_abstract=True)
uml_ControlFlow = Class(name="uml::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
uml_InitialNode = Class(name="uml::InitialNode")
ControlNode = Class(name="ControlNode")
uml_ActivityParameterNode = Class(name="uml::ActivityParameterNode")
uml_ValuePin = Class(name="uml::ValuePin")
InputPin = Class(name="InputPin")
uml_Message = Class(name="uml::Message")
uml_SendSignalAction = Class(name="uml::SendSignalAction")
uml_CallOperationAction = Class(name="uml::CallOperationAction")
CallAction = Class(name="CallAction")
uml_CallBehaviorAction = Class(name="uml::CallBehaviorAction")
InteractionFragment = Class(name="InteractionFragment")
uml_Lifeline = Class(name="uml::Lifeline")
uml_InteractionFragment = Class(name="uml::InteractionFragment", is_abstract=True)
uml_Gate = Class(name="uml::Gate")
uml_MessageEnd = Class(name="uml::MessageEnd", is_abstract=True)
uml_Interaction = Class(name="uml::Interaction")
uml_PartDecomposition = Class(name="uml::PartDecomposition")
InteractionUse = Class(name="InteractionUse")
uml_InteractionUse = Class(name="uml::InteractionUse")
uml_GeneralOrdering = Class(name="uml::GeneralOrdering")
uml_InteractionOperand = Class(name="uml::InteractionOperand")
uml_InteractionConstraint = Class(name="uml::InteractionConstraint")
Constraint = Class(name="Constraint")
uml_ExecutionSpecification = Class(name="uml::ExecutionSpecification", is_abstract=True)
MessageEnd = Class(name="MessageEnd")
uml_OccurrenceSpecification = Class(name="uml::OccurrenceSpecification")
uml_CreationEvent = Class(name="uml::CreationEvent")
uml_DestructionEvent = Class(name="uml::DestructionEvent")
uml_SendOperationEvent = Class(name="uml::SendOperationEvent")
MessageEvent = Class(name="MessageEvent")
uml_MessageEvent = Class(name="uml::MessageEvent", is_abstract=True)
uml_SendSignalEvent = Class(name="uml::SendSignalEvent")
uml_MessageOccurrenceSpecification = Class(name="uml::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
uml_ExecutionOccurrenceSpecification = Class(name="uml::ExecutionOccurrenceSpecification")
uml_ReceiveOperationEvent = Class(name="uml::ReceiveOperationEvent")
uml_ReceiveSignalEvent = Class(name="uml::ReceiveSignalEvent")
uml_StateInvariant = Class(name="uml::StateInvariant")
uml_ActionExecutionSpecification = Class(name="uml::ActionExecutionSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
uml_BehaviorExecutionSpecification = Class(name="uml::BehaviorExecutionSpecification")
uml_ExecutionEvent = Class(name="uml::ExecutionEvent")
Event = Class(name="Event")
uml_FlowFinalNode = Class(name="uml::FlowFinalNode")
FinalNode = Class(name="FinalNode")
uml_FinalNode = Class(name="uml::FinalNode", is_abstract=True)
uml_CentralBufferNode = Class(name="uml::CentralBufferNode")
uml_MergeNode = Class(name="uml::MergeNode")
uml_DecisionNode = Class(name="uml::DecisionNode")
uml_ObjectFlow = Class(name="uml::ObjectFlow")
uml_ActivityFinalNode = Class(name="uml::ActivityFinalNode")
uml_ComponentRealization = Class(name="uml::ComponentRealization")
uml_Component = Class(name="uml::Component")
uml_Actor = Class(name="uml::Actor")
uml_CallEvent = Class(name="uml::CallEvent")
uml_ChangeEvent = Class(name="uml::ChangeEvent")
uml_SignalEvent = Class(name="uml::SignalEvent")
uml_AnyReceiveEvent = Class(name="uml::AnyReceiveEvent")
uml_ForkNode = Class(name="uml::ForkNode")
uml_Node = Class(name="uml::Node")
uml_CommunicationPath = Class(name="uml::CommunicationPath")
uml_Device = Class(name="uml::Device")
Node = Class(name="Node")
uml_ExecutionEnvironment = Class(name="uml::ExecutionEnvironment")
uml_CombinedFragment = Class(name="uml::CombinedFragment")
uml_DestroyObjectAction = Class(name="uml::DestroyObjectAction")
uml_TestIdentityAction = Class(name="uml::TestIdentityAction")
uml_ReadSelfAction = Class(name="uml::ReadSelfAction")
uml_Continuation = Class(name="uml::Continuation")
uml_ConsiderIgnoreFragment = Class(name="uml::ConsiderIgnoreFragment")
CombinedFragment = Class(name="CombinedFragment")
uml_CreateObjectAction = Class(name="uml::CreateObjectAction")
uml_ClearStructuralFeatureAction = Class(name="uml::ClearStructuralFeatureAction")
uml_RemoveStructuralFeatureValueAction = Class(name="uml::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
uml_AddStructuralFeatureValueAction = Class(name="uml::AddStructuralFeatureValueAction")
uml_LinkAction = Class(name="uml::LinkAction", is_abstract=True)
uml_LinkEndData = Class(name="uml::LinkEndData")
uml_StructuralFeatureAction = Class(name="uml::StructuralFeatureAction", is_abstract=True)
uml_ReadStructuralFeatureAction = Class(name="uml::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
uml_WriteStructuralFeatureAction = Class(name="uml::WriteStructuralFeatureAction", is_abstract=True)
uml_ReadLinkAction = Class(name="uml::ReadLinkAction")
LinkAction = Class(name="LinkAction")
uml_LinkEndCreationData = Class(name="uml::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
uml_CreateLinkAction = Class(name="uml::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
uml_WriteLinkAction = Class(name="uml::WriteLinkAction", is_abstract=True)
uml_DestroyLinkAction = Class(name="uml::DestroyLinkAction")
uml_LinkEndDestructionData = Class(name="uml::LinkEndDestructionData")
uml_QualifierValue = Class(name="uml::QualifierValue")
uml_SendObjectAction = Class(name="uml::SendObjectAction")
uml_ValueSpecificationAction = Class(name="uml::ValueSpecificationAction")
uml_TimeExpression = Class(name="uml::TimeExpression")
uml_ClearAssociationAction = Class(name="uml::ClearAssociationAction")
uml_BroadcastSignalAction = Class(name="uml::BroadcastSignalAction")
uml_DurationInterval = Class(name="uml::DurationInterval")
Interval = Class(name="Interval")
uml_Interval = Class(name="uml::Interval")
uml_ReadVariableAction = Class(name="uml::ReadVariableAction")
VariableAction = Class(name="VariableAction")
uml_Observation = Class(name="uml::Observation", is_abstract=True)
uml_TimeConstraint = Class(name="uml::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
uml_Duration = Class(name="uml::Duration")
uml_IntervalConstraint = Class(name="uml::IntervalConstraint")
uml_TimeInterval = Class(name="uml::TimeInterval")
uml_DurationConstraint = Class(name="uml::DurationConstraint")
uml_TimeObservation = Class(name="uml::TimeObservation")
Observation = Class(name="Observation")
uml_DurationObservation = Class(name="uml::DurationObservation")
uml_FinalState = Class(name="uml::FinalState")
State = Class(name="State")
uml_TimeEvent = Class(name="uml::TimeEvent")
uml_VariableAction = Class(name="uml::VariableAction", is_abstract=True)
uml_ActionInputPin = Class(name="uml::ActionInputPin")
uml_WriteVariableAction = Class(name="uml::WriteVariableAction", is_abstract=True)
uml_ClearVariableAction = Class(name="uml::ClearVariableAction")
uml_AddVariableValueAction = Class(name="uml::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
uml_RemoveVariableValueAction = Class(name="uml::RemoveVariableValueAction")
uml_RaiseExceptionAction = Class(name="uml::RaiseExceptionAction")
uml_ReclassifyObjectAction = Class(name="uml::ReclassifyObjectAction")
uml_InformationItem = Class(name="uml::InformationItem")
uml_InformationFlow = Class(name="uml::InformationFlow")
uml_ReadExtentAction = Class(name="uml::ReadExtentAction")
uml_ReadLinkObjectEndQualifierAction = Class(name="uml::ReadLinkObjectEndQualifierAction")
uml_ReadIsClassifiedObjectAction = Class(name="uml::ReadIsClassifiedObjectAction")
uml_StartClassifierBehaviorAction = Class(name="uml::StartClassifierBehaviorAction")
uml_ReadLinkObjectEndAction = Class(name="uml::ReadLinkObjectEndAction")
uml_CreateLinkObjectAction = Class(name="uml::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
uml_AcceptEventAction = Class(name="uml::AcceptEventAction")
uml_AcceptCallAction = Class(name="uml::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
uml_ReplyAction = Class(name="uml::ReplyAction")
uml_DataStoreNode = Class(name="uml::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
uml_ConditionalNode = Class(name="uml::ConditionalNode")
uml_UnmarshallAction = Class(name="uml::UnmarshallAction")
uml_ReduceAction = Class(name="uml::ReduceAction")
uml_StartObjectBehaviorAction = Class(name="uml::StartObjectBehaviorAction")
uml_JoinNode = Class(name="uml::JoinNode")
uml_Clause = Class(name="uml::Clause")
uml_LoopNode = Class(name="uml::LoopNode")
uml_ProtocolTransition = Class(name="uml::ProtocolTransition")
Transition = Class(name="Transition")
uml_ExpansionNode = Class(name="uml::ExpansionNode")
uml_ExpansionRegion = Class(name="uml::ExpansionRegion")
uml_AssociationClass = Class(name="uml::AssociationClass")

# uml_Comment class attributes and methods
uml_Comment_body: Property = Property(name="body", type=StringType)
uml_Comment.attributes={uml_Comment_body}

# Element class attributes and methods

# TemplateableElement class attributes and methods

# uml_Type class attributes and methods

# uml_PackageMerge class attributes and methods

# uml_PackageableElement class attributes and methods

# uml_ProfileApplication class attributes and methods
uml_ProfileApplication_isStrict: Property = Property(name="isStrict", type=StringType)
uml_ProfileApplication.attributes={uml_ProfileApplication_isStrict}

# NamedElement class attributes and methods

# ParameterableElement class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_visibility, uml_NamedElement_name, uml_NamedElement_qualifiedName}

# uml_Element class attributes and methods

# EModelElement class attributes and methods

# uml_Package class attributes and methods

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# DirectedRelationship class attributes and methods

# uml_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# uml_Relationship class attributes and methods

# uml_ElementImport class attributes and methods
uml_ElementImport_alias: Property = Property(name="alias", type=StringType)
uml_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
uml_ElementImport.attributes={uml_ElementImport_alias, uml_ElementImport_visibility}

# uml_PackageImport class attributes and methods
uml_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
uml_PackageImport.attributes={uml_PackageImport_visibility}

# uml_Dependency class attributes and methods

# uml_Namespace class attributes and methods

# uml_StringExpression class attributes and methods

# uml_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# uml_TypedElement class attributes and methods

# uml_Constraint class attributes and methods

# uml_Classifier class attributes and methods
uml_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Classifier.attributes={uml_Classifier_isAbstract}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# uml_Generalization class attributes and methods
uml_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
uml_Generalization.attributes={uml_Generalization_isSubstitutable}

# uml_GeneralizationSet class attributes and methods
uml_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
uml_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
uml_GeneralizationSet.attributes={uml_GeneralizationSet_isDisjoint, uml_GeneralizationSet_isCovering}

# uml_Feature class attributes and methods
uml_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
uml_Feature.attributes={uml_Feature_isStatic}

# uml_Substitution class attributes and methods

# uml_Association class attributes and methods
uml_Association_isDerived: Property = Property(name="isDerived", type=StringType)
uml_Association.attributes={uml_Association_isDerived}

# Classifier class attributes and methods

# uml_Property class attributes and methods
uml_Property_isDerived: Property = Property(name="isDerived", type=StringType)
uml_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
uml_Property_default: Property = Property(name="default", type=StringType)
uml_Property_aggregation: Property = Property(name="aggregation", type=StringType)
uml_Property_isComposite: Property = Property(name="isComposite", type=StringType)
uml_Property.attributes={uml_Property_isDerived, uml_Property_aggregation, uml_Property_default, uml_Property_isComposite, uml_Property_isDerivedUnion}

# uml_CollaborationUse class attributes and methods

# uml_UseCase class attributes and methods

# uml_RedefinableElement class attributes and methods
uml_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
uml_RedefinableElement.attributes={uml_RedefinableElement_isLeaf}

# uml_TemplateableElement class attributes and methods

# uml_TemplateBinding class attributes and methods

# uml_TemplateSignature class attributes and methods

# uml_TemplateParameterSubstitution class attributes and methods

# uml_ParameterableElement class attributes and methods

# uml_TemplateParameter class attributes and methods

# uml_Realization class attributes and methods

# Abstraction class attributes and methods

# uml_Abstraction class attributes and methods

# Dependency class attributes and methods

# uml_OpaqueExpression class attributes and methods
uml_OpaqueExpression_body: Property = Property(name="body", type=StringType)
uml_OpaqueExpression_language: Property = Property(name="language", type=StringType)
uml_OpaqueExpression.attributes={uml_OpaqueExpression_body, uml_OpaqueExpression_language}

# ValueSpecification class attributes and methods

# Realization class attributes and methods

# uml_Operation class attributes and methods
uml_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
uml_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
uml_Operation_lower: Property = Property(name="lower", type=StringType)
uml_Operation_upper: Property = Property(name="upper", type=StringType)
uml_Operation.attributes={uml_Operation_isOrdered, uml_Operation_upper, uml_Operation_isQuery, uml_Operation_isUnique, uml_Operation_lower}

# uml_MultiplicityElement class attributes and methods
uml_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
uml_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
uml_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
uml_MultiplicityElement.attributes={uml_MultiplicityElement_isOrdered, uml_MultiplicityElement_upper, uml_MultiplicityElement_isUnique, uml_MultiplicityElement_lower}

# uml_Parameter class attributes and methods
uml_Parameter_direction: Property = Property(name="direction", type=StringType)
uml_Parameter_default: Property = Property(name="default", type=StringType)
uml_Parameter_isException: Property = Property(name="isException", type=StringType)
uml_Parameter_isStream: Property = Property(name="isStream", type=StringType)
uml_Parameter_effect: Property = Property(name="effect", type=StringType)
uml_Parameter.attributes={uml_Parameter_effect, uml_Parameter_isStream, uml_Parameter_direction, uml_Parameter_isException, uml_Parameter_default}

# uml_Behavior class attributes and methods
uml_Behavior_isReentrant: Property = Property(name="isReentrant", type=StringType)
uml_Behavior.attributes={uml_Behavior_isReentrant}

# ConnectableElement class attributes and methods

# MultiplicityElement class attributes and methods

# uml_ParameterSet class attributes and methods

# uml_ConnectableElement class attributes and methods

# uml_ConnectorEnd class attributes and methods

# uml_DataType class attributes and methods

# StructuralFeature class attributes and methods

# DeploymentTarget class attributes and methods

# uml_Class class attributes and methods
uml_Class_isActive: Property = Property(name="isActive", type=StringType)
uml_Class.attributes={uml_Class_isActive}

# uml_DeploymentTarget class attributes and methods

# uml_Deployment class attributes and methods

# Artifact class attributes and methods

# uml_Artifact class attributes and methods
uml_Artifact_fileName: Property = Property(name="fileName", type=StringType)
uml_Artifact.attributes={uml_Artifact_fileName}

# DeployedArtifact class attributes and methods

# uml_DeployedArtifact class attributes and methods

# uml_DeploymentSpecification class attributes and methods
uml_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
uml_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
uml_DeploymentSpecification.attributes={uml_DeploymentSpecification_deploymentLocation, uml_DeploymentSpecification_executionLocation}

# BehavioralFeature class attributes and methods

# uml_Interface class attributes and methods

# uml_Manifestation class attributes and methods

# uml_BehavioralFeature class attributes and methods
uml_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
uml_BehavioralFeature.attributes={uml_BehavioralFeature_isAbstract, uml_BehavioralFeature_concurrency}

# Class class attributes and methods

# uml_BehavioredClassifier class attributes and methods

# Feature class attributes and methods

# EncapsulatedClassifier class attributes and methods

# BehavioredClassifier class attributes and methods

# uml_InterfaceRealization class attributes and methods

# uml_Trigger class attributes and methods

# uml_Reception class attributes and methods

# uml_Extension class attributes and methods
uml_Extension_isRequired: Property = Property(name="isRequired", type=StringType)
uml_Extension.attributes={uml_Extension_isRequired}

# uml_ProtocolStateMachine class attributes and methods

# uml_Signal class attributes and methods

# StateMachine class attributes and methods

# uml_ProtocolConformance class attributes and methods

# uml_Transition class attributes and methods
uml_Transition_kind: Property = Property(name="kind", type=StringType)
uml_Transition.attributes={uml_Transition_kind}

# uml_StateMachine class attributes and methods

# Behavior class attributes and methods

# uml_Region class attributes and methods

# uml_State class attributes and methods
uml_State_isComposite: Property = Property(name="isComposite", type=StringType)
uml_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
uml_State_isSimple: Property = Property(name="isSimple", type=StringType)
uml_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
uml_State.attributes={uml_State_isOrthogonal, uml_State_isSubmachineState, uml_State_isSimple, uml_State_isComposite}

# uml_Pseudostate class attributes and methods
uml_Pseudostate_kind: Property = Property(name="kind", type=StringType)
uml_Pseudostate.attributes={uml_Pseudostate_kind}

# uml_Vertex class attributes and methods

# uml_Event class attributes and methods

# uml_Port class attributes and methods
uml_Port_isBehavior: Property = Property(name="isBehavior", type=StringType)
uml_Port_isService: Property = Property(name="isService", type=StringType)
uml_Port.attributes={uml_Port_isBehavior, uml_Port_isService}

# Property class attributes and methods

# uml_ConnectionPointReference class attributes and methods

# Vertex class attributes and methods

# uml_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# uml_StructuredClassifier class attributes and methods

# Association class attributes and methods

# uml_ExtensionEnd class attributes and methods

# uml_Stereotype class attributes and methods

# uml_Image class attributes and methods
uml_Image_content: Property = Property(name="content", type=StringType)
uml_Image_location: Property = Property(name="location", type=StringType)
uml_Image_format: Property = Property(name="format", type=StringType)
uml_Image.attributes={uml_Image_format, uml_Image_location, uml_Image_content}

# uml_Connector class attributes and methods
uml_Connector_kind: Property = Property(name="kind", type=StringType)
uml_Connector.attributes={uml_Connector_kind}

# uml_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# uml_StructuralFeature class attributes and methods
uml_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
uml_StructuralFeature.attributes={uml_StructuralFeature_isReadOnly}

# uml_ConnectableElementTemplateParameter class attributes and methods

# uml_Profile class attributes and methods

# Package class attributes and methods

# uml_Model class attributes and methods
uml_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
uml_Model.attributes={uml_Model_viewpoint}

# uml_Include class attributes and methods

# uml_Extend class attributes and methods

# uml_ExtensionPoint class attributes and methods

# uml_Collaboration class attributes and methods

# uml_ClassifierTemplateParameter class attributes and methods
uml_ClassifierTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=StringType)
uml_ClassifierTemplateParameter.attributes={uml_ClassifierTemplateParameter_allowSubstitutable}

# Expression class attributes and methods

# uml_Expression class attributes and methods
uml_Expression_symbol: Property = Property(name="symbol", type=StringType)
uml_Expression.attributes={uml_Expression_symbol}

# uml_RedefinableTemplateSignature class attributes and methods

# TemplateSignature class attributes and methods

# uml_Enumeration class attributes and methods

# DataType class attributes and methods

# uml_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# uml_InstanceSpecification class attributes and methods

# uml_Slot class attributes and methods

# uml_Usage class attributes and methods

# uml_LiteralBoolean class attributes and methods
uml_LiteralBoolean_value: Property = Property(name="value", type=StringType)
uml_LiteralBoolean.attributes={uml_LiteralBoolean_value}

# uml_LiteralNull class attributes and methods

# uml_InstanceValue class attributes and methods

# uml_LiteralUnlimitedNatural class attributes and methods
uml_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
uml_LiteralUnlimitedNatural.attributes={uml_LiteralUnlimitedNatural_value}

# uml_OpaqueBehavior class attributes and methods
uml_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
uml_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
uml_OpaqueBehavior.attributes={uml_OpaqueBehavior_language, uml_OpaqueBehavior_body}

# uml_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# uml_OpaqueAction class attributes and methods
uml_OpaqueAction_body: Property = Property(name="body", type=StringType)
uml_OpaqueAction_language: Property = Property(name="language", type=StringType)
uml_OpaqueAction.attributes={uml_OpaqueAction_language, uml_OpaqueAction_body}

# Action class attributes and methods

# uml_InputPin class attributes and methods

# uml_OutputPin class attributes and methods

# uml_PrimitiveType class attributes and methods

# uml_LiteralSpecification class attributes and methods

# uml_LiteralInteger class attributes and methods
uml_LiteralInteger_value: Property = Property(name="value", type=StringType)
uml_LiteralInteger.attributes={uml_LiteralInteger_value}

# LiteralSpecification class attributes and methods

# uml_LiteralString class attributes and methods
uml_LiteralString_value: Property = Property(name="value", type=StringType)
uml_LiteralString.attributes={uml_LiteralString_value}

# uml_ExecutableNode class attributes and methods

# ActivityNode class attributes and methods

# uml_ExceptionHandler class attributes and methods

# uml_ActivityNode class attributes and methods

# uml_StructuredActivityNode class attributes and methods
uml_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=StringType)
uml_StructuredActivityNode.attributes={uml_StructuredActivityNode_mustIsolate}

# uml_Activity class attributes and methods
uml_Activity_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
uml_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=StringType)
uml_Activity.attributes={uml_Activity_isReadOnly, uml_Activity_isSingleExecution}

# uml_ActivityEdge class attributes and methods

# uml_ActivityPartition class attributes and methods
uml_ActivityPartition_isDimension: Property = Property(name="isDimension", type=StringType)
uml_ActivityPartition_isExternal: Property = Property(name="isExternal", type=StringType)
uml_ActivityPartition.attributes={uml_ActivityPartition_isExternal, uml_ActivityPartition_isDimension}

# uml_InterruptibleActivityRegion class attributes and methods

# uml_Action class attributes and methods

# ExecutableNode class attributes and methods

# uml_ActivityGroup class attributes and methods

# ActivityGroup class attributes and methods

# uml_Variable class attributes and methods

# uml_ObjectNode class attributes and methods
uml_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
uml_ObjectNode_isControlType: Property = Property(name="isControlType", type=StringType)
uml_ObjectNode.attributes={uml_ObjectNode_isControlType, uml_ObjectNode_ordering}

# Pin class attributes and methods

# uml_Pin class attributes and methods
uml_Pin_isControl: Property = Property(name="isControl", type=StringType)
uml_Pin.attributes={uml_Pin_isControl}

# ObjectNode class attributes and methods

# uml_CallAction class attributes and methods
uml_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=StringType)
uml_CallAction.attributes={uml_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# uml_InvocationAction class attributes and methods

# uml_SequenceNode class attributes and methods

# StructuredActivityNode class attributes and methods

# uml_ControlNode class attributes and methods

# uml_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# uml_InitialNode class attributes and methods

# ControlNode class attributes and methods

# uml_ActivityParameterNode class attributes and methods

# uml_ValuePin class attributes and methods

# InputPin class attributes and methods

# uml_Message class attributes and methods
uml_Message_messageKind: Property = Property(name="messageKind", type=StringType)
uml_Message_messageSort: Property = Property(name="messageSort", type=StringType)
uml_Message.attributes={uml_Message_messageSort, uml_Message_messageKind}

# uml_SendSignalAction class attributes and methods

# uml_CallOperationAction class attributes and methods

# CallAction class attributes and methods

# uml_CallBehaviorAction class attributes and methods

# InteractionFragment class attributes and methods

# uml_Lifeline class attributes and methods

# uml_InteractionFragment class attributes and methods

# uml_Gate class attributes and methods

# uml_MessageEnd class attributes and methods

# uml_Interaction class attributes and methods

# uml_PartDecomposition class attributes and methods

# InteractionUse class attributes and methods

# uml_InteractionUse class attributes and methods

# uml_GeneralOrdering class attributes and methods

# uml_InteractionOperand class attributes and methods

# uml_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# uml_ExecutionSpecification class attributes and methods

# MessageEnd class attributes and methods

# uml_OccurrenceSpecification class attributes and methods

# uml_CreationEvent class attributes and methods

# uml_DestructionEvent class attributes and methods

# uml_SendOperationEvent class attributes and methods

# MessageEvent class attributes and methods

# uml_MessageEvent class attributes and methods

# uml_SendSignalEvent class attributes and methods

# uml_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# uml_ExecutionOccurrenceSpecification class attributes and methods

# uml_ReceiveOperationEvent class attributes and methods

# uml_ReceiveSignalEvent class attributes and methods

# uml_StateInvariant class attributes and methods

# uml_ActionExecutionSpecification class attributes and methods

# ExecutionSpecification class attributes and methods

# uml_BehaviorExecutionSpecification class attributes and methods

# uml_ExecutionEvent class attributes and methods

# Event class attributes and methods

# uml_FlowFinalNode class attributes and methods

# FinalNode class attributes and methods

# uml_FinalNode class attributes and methods

# uml_CentralBufferNode class attributes and methods

# uml_MergeNode class attributes and methods

# uml_DecisionNode class attributes and methods

# uml_ObjectFlow class attributes and methods
uml_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=StringType)
uml_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=StringType)
uml_ObjectFlow.attributes={uml_ObjectFlow_isMultireceive, uml_ObjectFlow_isMulticast}

# uml_ActivityFinalNode class attributes and methods

# uml_ComponentRealization class attributes and methods

# uml_Component class attributes and methods
uml_Component_isIndirectlyInstantiated: Property = Property(name="isIndirectlyInstantiated", type=StringType)
uml_Component.attributes={uml_Component_isIndirectlyInstantiated}

# uml_Actor class attributes and methods

# uml_CallEvent class attributes and methods

# uml_ChangeEvent class attributes and methods

# uml_SignalEvent class attributes and methods

# uml_AnyReceiveEvent class attributes and methods

# uml_ForkNode class attributes and methods

# uml_Node class attributes and methods

# uml_CommunicationPath class attributes and methods

# uml_Device class attributes and methods

# Node class attributes and methods

# uml_ExecutionEnvironment class attributes and methods

# uml_CombinedFragment class attributes and methods
uml_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
uml_CombinedFragment.attributes={uml_CombinedFragment_interactionOperator}

# uml_DestroyObjectAction class attributes and methods
uml_DestroyObjectAction_isDestroyLinks: Property = Property(name="isDestroyLinks", type=StringType)
uml_DestroyObjectAction_isDestroyOwnedObjects: Property = Property(name="isDestroyOwnedObjects", type=StringType)
uml_DestroyObjectAction.attributes={uml_DestroyObjectAction_isDestroyOwnedObjects, uml_DestroyObjectAction_isDestroyLinks}

# uml_TestIdentityAction class attributes and methods

# uml_ReadSelfAction class attributes and methods

# uml_Continuation class attributes and methods
uml_Continuation_setting: Property = Property(name="setting", type=StringType)
uml_Continuation.attributes={uml_Continuation_setting}

# uml_ConsiderIgnoreFragment class attributes and methods

# CombinedFragment class attributes and methods

# uml_CreateObjectAction class attributes and methods

# uml_ClearStructuralFeatureAction class attributes and methods

# uml_RemoveStructuralFeatureValueAction class attributes and methods
uml_RemoveStructuralFeatureValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
uml_RemoveStructuralFeatureValueAction.attributes={uml_RemoveStructuralFeatureValueAction_isRemoveDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# uml_AddStructuralFeatureValueAction class attributes and methods
uml_AddStructuralFeatureValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml_AddStructuralFeatureValueAction.attributes={uml_AddStructuralFeatureValueAction_isReplaceAll}

# uml_LinkAction class attributes and methods

# uml_LinkEndData class attributes and methods

# uml_StructuralFeatureAction class attributes and methods

# uml_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# uml_WriteStructuralFeatureAction class attributes and methods

# uml_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# uml_LinkEndCreationData class attributes and methods
uml_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml_LinkEndCreationData.attributes={uml_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# uml_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# uml_WriteLinkAction class attributes and methods

# uml_DestroyLinkAction class attributes and methods

# uml_LinkEndDestructionData class attributes and methods
uml_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=StringType)
uml_LinkEndDestructionData.attributes={uml_LinkEndDestructionData_isDestroyDuplicates}

# uml_QualifierValue class attributes and methods

# uml_SendObjectAction class attributes and methods

# uml_ValueSpecificationAction class attributes and methods

# uml_TimeExpression class attributes and methods

# uml_ClearAssociationAction class attributes and methods

# uml_BroadcastSignalAction class attributes and methods

# uml_DurationInterval class attributes and methods

# Interval class attributes and methods

# uml_Interval class attributes and methods

# uml_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# uml_Observation class attributes and methods

# uml_TimeConstraint class attributes and methods
uml_TimeConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml_TimeConstraint.attributes={uml_TimeConstraint_firstEvent}

# IntervalConstraint class attributes and methods

# uml_Duration class attributes and methods

# uml_IntervalConstraint class attributes and methods

# uml_TimeInterval class attributes and methods

# uml_DurationConstraint class attributes and methods
uml_DurationConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml_DurationConstraint.attributes={uml_DurationConstraint_firstEvent}

# uml_TimeObservation class attributes and methods
uml_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml_TimeObservation.attributes={uml_TimeObservation_firstEvent}

# Observation class attributes and methods

# uml_DurationObservation class attributes and methods
uml_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml_DurationObservation.attributes={uml_DurationObservation_firstEvent}

# uml_FinalState class attributes and methods

# State class attributes and methods

# uml_TimeEvent class attributes and methods
uml_TimeEvent_isRelative: Property = Property(name="isRelative", type=StringType)
uml_TimeEvent.attributes={uml_TimeEvent_isRelative}

# uml_VariableAction class attributes and methods

# uml_ActionInputPin class attributes and methods

# uml_WriteVariableAction class attributes and methods

# uml_ClearVariableAction class attributes and methods

# uml_AddVariableValueAction class attributes and methods
uml_AddVariableValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml_AddVariableValueAction.attributes={uml_AddVariableValueAction_isReplaceAll}

# WriteVariableAction class attributes and methods

# uml_RemoveVariableValueAction class attributes and methods
uml_RemoveVariableValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
uml_RemoveVariableValueAction.attributes={uml_RemoveVariableValueAction_isRemoveDuplicates}

# uml_RaiseExceptionAction class attributes and methods

# uml_ReclassifyObjectAction class attributes and methods
uml_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml_ReclassifyObjectAction.attributes={uml_ReclassifyObjectAction_isReplaceAll}

# uml_InformationItem class attributes and methods

# uml_InformationFlow class attributes and methods

# uml_ReadExtentAction class attributes and methods

# uml_ReadLinkObjectEndQualifierAction class attributes and methods

# uml_ReadIsClassifiedObjectAction class attributes and methods
uml_ReadIsClassifiedObjectAction_isDirect: Property = Property(name="isDirect", type=StringType)
uml_ReadIsClassifiedObjectAction.attributes={uml_ReadIsClassifiedObjectAction_isDirect}

# uml_StartClassifierBehaviorAction class attributes and methods

# uml_ReadLinkObjectEndAction class attributes and methods

# uml_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# uml_AcceptEventAction class attributes and methods
uml_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=StringType)
uml_AcceptEventAction.attributes={uml_AcceptEventAction_isUnmarshall}

# uml_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# uml_ReplyAction class attributes and methods

# uml_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# uml_ConditionalNode class attributes and methods
uml_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=StringType)
uml_ConditionalNode_isAssured: Property = Property(name="isAssured", type=StringType)
uml_ConditionalNode.attributes={uml_ConditionalNode_isDeterminate, uml_ConditionalNode_isAssured}

# uml_UnmarshallAction class attributes and methods

# uml_ReduceAction class attributes and methods
uml_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml_ReduceAction.attributes={uml_ReduceAction_isOrdered}

# uml_StartObjectBehaviorAction class attributes and methods

# uml_JoinNode class attributes and methods
uml_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=StringType)
uml_JoinNode.attributes={uml_JoinNode_isCombineDuplicate}

# uml_Clause class attributes and methods

# uml_LoopNode class attributes and methods
uml_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=StringType)
uml_LoopNode.attributes={uml_LoopNode_isTestedFirst}

# uml_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# uml_ExpansionNode class attributes and methods

# uml_ExpansionRegion class attributes and methods
uml_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
uml_ExpansionRegion.attributes={uml_ExpansionRegion_mode}

# uml_AssociationClass class attributes and methods

# Relationships
ownedType9: BinaryAssociation = BinaryAssociation(
    name="ownedType9",
    ends={
        Property(name="Type", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=uml_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge10: BinaryAssociation = BinaryAssociation(
    name="packageMerge10",
    ends={
        Property(name="PackageMerge", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=uml_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement11: BinaryAssociation = BinaryAssociation(
    name="packagedElement11",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage13: BinaryAssociation = BinaryAssociation(
    name="nestedPackage13",
    ends={
        Property(name="Package", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=uml_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage15: BinaryAssociation = BinaryAssociation(
    name="nestingPackage15",
    ends={
        Property(name="Package16", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=uml_Package, multiplicity=Multiplicity(0, 1))
    }
)
profileApplication17: BinaryAssociation = BinaryAssociation(
    name="profileApplication17",
    ends={
        Property(name="ProfileApplication", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="applyingPackage", type=uml_ProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement0: BinaryAssociation = BinaryAssociation(
    name="annotatedElement0",
    ends={
        Property(name="uml_Element", type=uml_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Comment", type=uml_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=uml_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="uml_Comment8", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Element7", type=uml_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supplier21: BinaryAssociation = BinaryAssociation(
    name="supplier21",
    ends={
        Property(name="uml_NamedElement22", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client23: BinaryAssociation = BinaryAssociation(
    name="client23",
    ends={
        Property(name="NamedElement", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="uml_Element25", type=uml_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DirectedRelationship", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="uml_Element28", type=uml_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DirectedRelationship27", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement29: BinaryAssociation = BinaryAssociation(
    name="relatedElement29",
    ends={
        Property(name="uml_Element30", type=uml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Relationship", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
elementImport31: BinaryAssociation = BinaryAssociation(
    name="elementImport31",
    ends={
        Property(name="ElementImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=uml_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport32: BinaryAssociation = BinaryAssociation(
    name="packageImport32",
    ends={
        Property(name="PackageImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace33", type=uml_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clientDependency18: BinaryAssociation = BinaryAssociation(
    name="clientDependency18",
    ends={
        Property(name="Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=uml_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Namespace", type=uml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=uml_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
nameExpression20: BinaryAssociation = BinaryAssociation(
    name="nameExpression20",
    ends={
        Property(name="uml_StringExpression", type=uml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_NamedElement", type=uml_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedElement42: BinaryAssociation = BinaryAssociation(
    name="importedElement42",
    ends={
        Property(name="uml_PackageableElement43", type=uml_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ElementImport", type=uml_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace44: BinaryAssociation = BinaryAssociation(
    name="importingNamespace44",
    ends={
        Property(name="Namespace45", type=uml_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage46: BinaryAssociation = BinaryAssociation(
    name="importedPackage46",
    ends={
        Property(name="uml_Package47", type=uml_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_PackageImport", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace48: BinaryAssociation = BinaryAssociation(
    name="importingNamespace48",
    ends={
        Property(name="Namespace49", type=uml_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement50: BinaryAssociation = BinaryAssociation(
    name="constrainedElement50",
    ends={
        Property(name="uml_Element51", type=uml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Constraint", type=uml_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification52: BinaryAssociation = BinaryAssociation(
    name="specification52",
    ends={
        Property(name="uml_ValueSpecification", type=uml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Constraint53", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context54: BinaryAssociation = BinaryAssociation(
    name="context54",
    ends={
        Property(name="Namespace55", type=uml_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=uml_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedRule34: BinaryAssociation = BinaryAssociation(
    name="ownedRule34",
    ends={
        Property(name="Constraint", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=uml_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member35: BinaryAssociation = BinaryAssociation(
    name="member35",
    ends={
        Property(name="uml_NamedElement36", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Namespace", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember37: BinaryAssociation = BinaryAssociation(
    name="importedMember37",
    ends={
        Property(name="uml_PackageableElement39", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Namespace38", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember40: BinaryAssociation = BinaryAssociation(
    name="ownedMember40",
    ends={
        Property(name="NamedElement41", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd64: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd64",
    ends={
        Property(name="uml_Property", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association65", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
generalization66: BinaryAssociation = BinaryAssociation(
    name="generalization66",
    ends={
        Property(name="Generalization", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=uml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent67: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent67",
    ends={
        Property(name="GeneralizationSet", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=uml_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
feature68: BinaryAssociation = BinaryAssociation(
    name="feature68",
    ends={
        Property(name="Feature", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=uml_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember69: BinaryAssociation = BinaryAssociation(
    name="inheritedMember69",
    ends={
        Property(name="uml_NamedElement70", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier72: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier72",
    ends={
        Property(name="uml_Classifier73", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier71", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general75: BinaryAssociation = BinaryAssociation(
    name="general75",
    ends={
        Property(name="uml_Classifier76", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier74", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
substitution77: BinaryAssociation = BinaryAssociation(
    name="substitution77",
    ends={
        Property(name="Substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=uml_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
package57: BinaryAssociation = BinaryAssociation(
    name="package57",
    ends={
        Property(name="Package58", type=uml_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=uml_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd59: BinaryAssociation = BinaryAssociation(
    name="ownedEnd59",
    ends={
        Property(name="Property", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd60: BinaryAssociation = BinaryAssociation(
    name="memberEnd60",
    ends={
        Property(name="Property61", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=uml_Property, multiplicity=Multiplicity(2, 9999))
    }
)
endType62: BinaryAssociation = BinaryAssociation(
    name="endType62",
    ends={
        Property(name="uml_Type63", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association", type=uml_Type, multiplicity=Multiplicity(1, 9999))
    }
)
representation81: BinaryAssociation = BinaryAssociation(
    name="representation81",
    ends={
        Property(name="uml_CollaborationUse", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier82", type=uml_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
collaborationUse83: BinaryAssociation = BinaryAssociation(
    name="collaborationUse83",
    ends={
        Property(name="uml_CollaborationUse85", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier84", type=uml_CollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUseCase86: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase86",
    ends={
        Property(name="uml_UseCase", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier87", type=uml_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase88: BinaryAssociation = BinaryAssociation(
    name="useCase88",
    ends={
        Property(name="UseCase", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=uml_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
attribute78: BinaryAssociation = BinaryAssociation(
    name="attribute78",
    ends={
        Property(name="uml_Property80", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier79", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
templateBinding94: BinaryAssociation = BinaryAssociation(
    name="templateBinding94",
    ends={
        Property(name="TemplateBinding", type=uml_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=uml_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature95: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature95",
    ends={
        Property(name="TemplateSignature", type=uml_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=uml_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature96: BinaryAssociation = BinaryAssociation(
    name="signature96",
    ends={
        Property(name="uml_TemplateSignature", type=uml_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateBinding", type=uml_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution97: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution97",
    ends={
        Property(name="TemplateParameterSubstitution", type=uml_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=uml_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedElement90: BinaryAssociation = BinaryAssociation(
    name="redefinedElement90",
    ends={
        Property(name="uml_RedefinableElement", type=uml_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RedefinableElement89", type=uml_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext91: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext91",
    ends={
        Property(name="uml_Classifier93", type=uml_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RedefinableElement92", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
template103: BinaryAssociation = BinaryAssociation(
    name="template103",
    ends={
        Property(name="TemplateableElement104", type=uml_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=uml_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature105: BinaryAssociation = BinaryAssociation(
    name="signature105",
    ends={
        Property(name="TemplateSignature106", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=uml_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameteredElement107: BinaryAssociation = BinaryAssociation(
    name="parameteredElement107",
    ends={
        Property(name="ParameterableElement", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=uml_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement108: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement108",
    ends={
        Property(name="ParameterableElement109", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateParameter", type=uml_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default110: BinaryAssociation = BinaryAssociation(
    name="default110",
    ends={
        Property(name="uml_ParameterableElement", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateParameter111", type=uml_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
boundElement98: BinaryAssociation = BinaryAssociation(
    name="boundElement98",
    ends={
        Property(name="TemplateableElement", type=uml_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding99", type=uml_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
parameter100: BinaryAssociation = BinaryAssociation(
    name="parameter100",
    ends={
        Property(name="uml_TemplateParameter", type=uml_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateSignature101", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameter102: BinaryAssociation = BinaryAssociation(
    name="ownedParameter102",
    ends={
        Property(name="TemplateParameter", type=uml_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=uml_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateParameter117: BinaryAssociation = BinaryAssociation(
    name="templateParameter117",
    ends={
        Property(name="TemplateParameter118", type=uml_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=uml_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
formal119: BinaryAssociation = BinaryAssociation(
    name="formal119",
    ends={
        Property(name="uml_TemplateParameter120", type=uml_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateParameterSubstitution", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
actual121: BinaryAssociation = BinaryAssociation(
    name="actual121",
    ends={
        Property(name="uml_ParameterableElement123", type=uml_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateParameterSubstitution122", type=uml_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual124: BinaryAssociation = BinaryAssociation(
    name="ownedActual124",
    ends={
        Property(name="uml_ParameterableElement126", type=uml_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateParameterSubstitution125", type=uml_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding127: BinaryAssociation = BinaryAssociation(
    name="templateBinding127",
    ends={
        Property(name="TemplateBinding128", type=uml_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=uml_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
ownedDefault112: BinaryAssociation = BinaryAssociation(
    name="ownedDefault112",
    ends={
        Property(name="uml_ParameterableElement114", type=uml_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TemplateParameter113", type=uml_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningTemplateParameter115: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter115",
    ends={
        Property(name="TemplateParameter116", type=uml_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameteredElement", type=uml_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
specific133: BinaryAssociation = BinaryAssociation(
    name="specific133",
    ends={
        Property(name="Classifier", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization134", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
powertype135: BinaryAssociation = BinaryAssociation(
    name="powertype135",
    ends={
        Property(name="Classifier136", type=uml_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=uml_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization137: BinaryAssociation = BinaryAssociation(
    name="generalization137",
    ends={
        Property(name="Generalization138", type=uml_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=uml_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
general129: BinaryAssociation = BinaryAssociation(
    name="general129",
    ends={
        Property(name="uml_Classifier130", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Generalization", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet131: BinaryAssociation = BinaryAssociation(
    name="generalizationSet131",
    ends={
        Property(name="GeneralizationSet132", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=uml_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
substitutingClassifier143: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier143",
    ends={
        Property(name="Classifier144", type=uml_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
mapping145: BinaryAssociation = BinaryAssociation(
    name="mapping145",
    ends={
        Property(name="uml_OpaqueExpression", type=uml_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Abstraction", type=uml_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featuringClassifier139: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier139",
    ends={
        Property(name="Classifier140", type=uml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
contract141: BinaryAssociation = BinaryAssociation(
    name="contract141",
    ends={
        Property(name="uml_Classifier142", type=uml_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operation151: BinaryAssociation = BinaryAssociation(
    name="operation151",
    ends={
        Property(name="uml_Operation", type=uml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Parameter152", type=uml_Operation, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue153: BinaryAssociation = BinaryAssociation(
    name="defaultValue153",
    ends={
        Property(name="uml_ValueSpecification155", type=uml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Parameter154", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result146: BinaryAssociation = BinaryAssociation(
    name="result146",
    ends={
        Property(name="uml_Parameter", type=uml_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_OpaqueExpression147", type=uml_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior148: BinaryAssociation = BinaryAssociation(
    name="behavior148",
    ends={
        Property(name="uml_Behavior", type=uml_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_OpaqueExpression149", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
parameterSet150: BinaryAssociation = BinaryAssociation(
    name="parameterSet150",
    ends={
        Property(name="ParameterSet", type=uml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=uml_ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
upperValue156: BinaryAssociation = BinaryAssociation(
    name="upperValue156",
    ends={
        Property(name="uml_ValueSpecification157", type=uml_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_MultiplicityElement", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue158: BinaryAssociation = BinaryAssociation(
    name="lowerValue158",
    ends={
        Property(name="uml_ValueSpecification160", type=uml_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_MultiplicityElement159", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end161: BinaryAssociation = BinaryAssociation(
    name="end161",
    ends={
        Property(name="uml_ConnectorEnd", type=uml_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectableElement", type=uml_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
definingEnd162: BinaryAssociation = BinaryAssociation(
    name="definingEnd162",
    ends={
        Property(name="uml_Property164", type=uml_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectorEnd163", type=uml_Property, multiplicity=Multiplicity(0, 1))
    }
)
class171: BinaryAssociation = BinaryAssociation(
    name="class171",
    ends={
        Property(name="uml_Class", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Property172", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype173: BinaryAssociation = BinaryAssociation(
    name="datatype173",
    ends={
        Property(name="DataType", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=uml_DataType, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty175: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty175",
    ends={
        Property(name="uml_Property176", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Property174", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
role165: BinaryAssociation = BinaryAssociation(
    name="role165",
    ends={
        Property(name="uml_ConnectableElement167", type=uml_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectorEnd166", type=uml_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
partWithPort168: BinaryAssociation = BinaryAssociation(
    name="partWithPort168",
    ends={
        Property(name="uml_Property170", type=uml_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectorEnd169", type=uml_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty185: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty185",
    ends={
        Property(name="uml_Property184", type=uml_Property, multiplicity=Multiplicity(0, 9999)),
        Property(name="uml_Property186", type=uml_Property, multiplicity=Multiplicity(1, 1))
    }
)
association187: BinaryAssociation = BinaryAssociation(
    name="association187",
    ends={
        Property(name="Association188", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=uml_Association, multiplicity=Multiplicity(0, 1))
    }
)
qualifier190: BinaryAssociation = BinaryAssociation(
    name="qualifier190",
    ends={
        Property(name="Property191", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd193: BinaryAssociation = BinaryAssociation(
    name="associationEnd193",
    ends={
        Property(name="Property194", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=uml_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation177: BinaryAssociation = BinaryAssociation(
    name="owningAssociation177",
    ends={
        Property(name="Association", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=uml_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue178: BinaryAssociation = BinaryAssociation(
    name="defaultValue178",
    ends={
        Property(name="uml_ValueSpecification180", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Property179", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite182: BinaryAssociation = BinaryAssociation(
    name="opposite182",
    ends={
        Property(name="uml_Property183", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Property181", type=uml_Property, multiplicity=Multiplicity(0, 1))
    }
)
configuration199: BinaryAssociation = BinaryAssociation(
    name="configuration199",
    ends={
        Property(name="deployment", type=uml_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="DeploymentSpecification", type=uml_Deployment, multiplicity=Multiplicity(1, 1))
    }
)
location200: BinaryAssociation = BinaryAssociation(
    name="location200",
    ends={
        Property(name="DeploymentTarget", type=uml_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="deployment201", type=uml_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
deployment202: BinaryAssociation = BinaryAssociation(
    name="deployment202",
    ends={
        Property(name="Deployment203", type=uml_DeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=uml_Deployment, multiplicity=Multiplicity(0, 1))
    }
)
deployment195: BinaryAssociation = BinaryAssociation(
    name="deployment195",
    ends={
        Property(name="Deployment", type=uml_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=uml_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement196: BinaryAssociation = BinaryAssociation(
    name="deployedElement196",
    ends={
        Property(name="uml_PackageableElement197", type=uml_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DeploymentTarget", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployedArtifact198: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact198",
    ends={
        Property(name="uml_DeployedArtifact", type=uml_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Deployment", type=uml_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute211: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute211",
    ends={
        Property(name="uml_Property213", type=uml_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Artifact212", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizedElement214: BinaryAssociation = BinaryAssociation(
    name="utilizedElement214",
    ends={
        Property(name="uml_PackageableElement216", type=uml_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Manifestation215", type=uml_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
interface217: BinaryAssociation = BinaryAssociation(
    name="interface217",
    ends={
        Property(name="Interface", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=uml_Interface, multiplicity=Multiplicity(0, 1))
    }
)
class218: BinaryAssociation = BinaryAssociation(
    name="class218",
    ends={
        Property(name="Class", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation219", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
nestedArtifact205: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact205",
    ends={
        Property(name="uml_Artifact", type=uml_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Artifact204", type=uml_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation206: BinaryAssociation = BinaryAssociation(
    name="manifestation206",
    ends={
        Property(name="uml_Manifestation", type=uml_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Artifact207", type=uml_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation208: BinaryAssociation = BinaryAssociation(
    name="ownedOperation208",
    ends={
        Property(name="uml_Operation210", type=uml_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Artifact209", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition223: BinaryAssociation = BinaryAssociation(
    name="postcondition223",
    ends={
        Property(name="uml_Constraint225", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation224", type=uml_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation227: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation227",
    ends={
        Property(name="uml_Operation228", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation226", type=uml_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
datatype229: BinaryAssociation = BinaryAssociation(
    name="datatype229",
    ends={
        Property(name="DataType231", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation230", type=uml_DataType, multiplicity=Multiplicity(0, 1))
    }
)
bodyCondition232: BinaryAssociation = BinaryAssociation(
    name="bodyCondition232",
    ends={
        Property(name="uml_Constraint234", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation233", type=uml_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
type235: BinaryAssociation = BinaryAssociation(
    name="type235",
    ends={
        Property(name="uml_Type237", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation236", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition220: BinaryAssociation = BinaryAssociation(
    name="precondition220",
    ends={
        Property(name="uml_Constraint222", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation221", type=uml_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException241: BinaryAssociation = BinaryAssociation(
    name="raisedException241",
    ends={
        Property(name="uml_Type243", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature242", type=uml_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet244: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet244",
    ends={
        Property(name="uml_ParameterSet", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature245", type=uml_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedBehavior247: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior247",
    ends={
        Property(name="uml_Behavior248", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior246", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter249: BinaryAssociation = BinaryAssociation(
    name="ownedParameter249",
    ends={
        Property(name="uml_Parameter251", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior250", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter238: BinaryAssociation = BinaryAssociation(
    name="ownedParameter238",
    ends={
        Property(name="uml_Parameter239", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method240: BinaryAssociation = BinaryAssociation(
    name="method240",
    ends={
        Property(name="Behavior", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification263: BinaryAssociation = BinaryAssociation(
    name="specification263",
    ends={
        Property(name="BehavioralFeature", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=uml_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier264: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier264",
    ends={
        Property(name="uml_Classifier266", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class265", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation267: BinaryAssociation = BinaryAssociation(
    name="ownedOperation267",
    ends={
        Property(name="Operation", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass269: BinaryAssociation = BinaryAssociation(
    name="superClass269",
    ends={
        Property(name="uml_Class270", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class268", type=uml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
context252: BinaryAssociation = BinaryAssociation(
    name="context252",
    ends={
        Property(name="uml_BehavioredClassifier", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior253", type=uml_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
precondition254: BinaryAssociation = BinaryAssociation(
    name="precondition254",
    ends={
        Property(name="uml_Constraint256", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior255", type=uml_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition257: BinaryAssociation = BinaryAssociation(
    name="postcondition257",
    ends={
        Property(name="uml_Constraint259", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior258", type=uml_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet260: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet260",
    ends={
        Property(name="uml_ParameterSet262", type=uml_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Behavior261", type=uml_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior274: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior274",
    ends={
        Property(name="uml_Behavior276", type=uml_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioredClassifier275", type=uml_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior277: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior277",
    ends={
        Property(name="uml_Behavior279", type=uml_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioredClassifier278", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
interfaceRealization280: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization280",
    ends={
        Property(name="InterfaceRealization", type=uml_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=uml_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTrigger281: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger281",
    ends={
        Property(name="uml_Trigger", type=uml_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioredClassifier282", type=uml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract283: BinaryAssociation = BinaryAssociation(
    name="contract283",
    ends={
        Property(name="uml_Interface", type=uml_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InterfaceRealization", type=uml_Interface, multiplicity=Multiplicity(1, 1))
    }
)
ownedReception271: BinaryAssociation = BinaryAssociation(
    name="ownedReception271",
    ends={
        Property(name="uml_Reception", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class272", type=uml_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension273: BinaryAssociation = BinaryAssociation(
    name="extension273",
    ends={
        Property(name="Extension", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="metaclass", type=uml_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier290: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier290",
    ends={
        Property(name="uml_Classifier292", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interface291", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedInterface294: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface294",
    ends={
        Property(name="uml_Interface295", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interface293", type=uml_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception296: BinaryAssociation = BinaryAssociation(
    name="ownedReception296",
    ends={
        Property(name="uml_Reception298", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interface297", type=uml_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol299: BinaryAssociation = BinaryAssociation(
    name="protocol299",
    ends={
        Property(name="uml_ProtocolStateMachine", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interface300", type=uml_ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signal301: BinaryAssociation = BinaryAssociation(
    name="signal301",
    ends={
        Property(name="uml_Signal", type=uml_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Reception302", type=uml_Signal, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute303: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute303",
    ends={
        Property(name="uml_Property305", type=uml_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Signal304", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformance306: BinaryAssociation = BinaryAssociation(
    name="conformance306",
    ends={
        Property(name="ProtocolConformance", type=uml_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="specificMachine", type=uml_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementingClassifier284: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier284",
    ends={
        Property(name="BehavioredClassifier", type=uml_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaceRealization", type=uml_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute285: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute285",
    ends={
        Property(name="uml_Property287", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interface286", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation288: BinaryAssociation = BinaryAssociation(
    name="ownedOperation288",
    ends={
        Property(name="Operation289", type=uml_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subvertex313: BinaryAssociation = BinaryAssociation(
    name="subvertex313",
    ends={
        Property(name="container", type=uml_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Vertex", type=uml_Region, multiplicity=Multiplicity(1, 1))
    }
)
transition314: BinaryAssociation = BinaryAssociation(
    name="transition314",
    ends={
        Property(name="Transition", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container315", type=uml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state316: BinaryAssociation = BinaryAssociation(
    name="state316",
    ends={
        Property(name="State317", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=uml_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion319: BinaryAssociation = BinaryAssociation(
    name="extendedRegion319",
    ends={
        Property(name="uml_Region", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Region318", type=uml_Region, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine320: BinaryAssociation = BinaryAssociation(
    name="stateMachine320",
    ends={
        Property(name="StateMachine", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region321", type=uml_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoing322: BinaryAssociation = BinaryAssociation(
    name="outgoing322",
    ends={
        Property(name="uml_Transition", type=uml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Vertex", type=uml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming323: BinaryAssociation = BinaryAssociation(
    name="incoming323",
    ends={
        Property(name="uml_Transition325", type=uml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Vertex324", type=uml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container326: BinaryAssociation = BinaryAssociation(
    name="container326",
    ends={
        Property(name="Region327", type=uml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=uml_Region, multiplicity=Multiplicity(0, 1))
    }
)
region307: BinaryAssociation = BinaryAssociation(
    name="region307",
    ends={
        Property(name="Region", type=uml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=uml_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
submachineState308: BinaryAssociation = BinaryAssociation(
    name="submachineState308",
    ends={
        Property(name="State", type=uml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=uml_State, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint309: BinaryAssociation = BinaryAssociation(
    name="connectionPoint309",
    ends={
        Property(name="Pseudostate", type=uml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine310", type=uml_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedStateMachine312: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine312",
    ends={
        Property(name="uml_StateMachine", type=uml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StateMachine311", type=uml_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
effect342: BinaryAssociation = BinaryAssociation(
    name="effect342",
    ends={
        Property(name="uml_Behavior344", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition343", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger345: BinaryAssociation = BinaryAssociation(
    name="trigger345",
    ends={
        Property(name="uml_Trigger347", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition346", type=uml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event348: BinaryAssociation = BinaryAssociation(
    name="event348",
    ends={
        Property(name="uml_Event", type=uml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Trigger349", type=uml_Event, multiplicity=Multiplicity(1, 1))
    }
)
port350: BinaryAssociation = BinaryAssociation(
    name="port350",
    ends={
        Property(name="uml_Port", type=uml_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Trigger351", type=uml_Port, multiplicity=Multiplicity(0, 9999))
    }
)
required352: BinaryAssociation = BinaryAssociation(
    name="required352",
    ends={
        Property(name="uml_Interface354", type=uml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Port353", type=uml_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort356: BinaryAssociation = BinaryAssociation(
    name="redefinedPort356",
    ends={
        Property(name="uml_Port357", type=uml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Port355", type=uml_Port, multiplicity=Multiplicity(0, 9999))
    }
)
container328: BinaryAssociation = BinaryAssociation(
    name="container328",
    ends={
        Property(name="Region329", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=uml_Region, multiplicity=Multiplicity(1, 1))
    }
)
source330: BinaryAssociation = BinaryAssociation(
    name="source330",
    ends={
        Property(name="uml_Vertex332", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition331", type=uml_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target333: BinaryAssociation = BinaryAssociation(
    name="target333",
    ends={
        Property(name="uml_Vertex335", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition334", type=uml_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
redefinedTransition337: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition337",
    ends={
        Property(name="uml_Transition338", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition336", type=uml_Transition, multiplicity=Multiplicity(0, 1))
    }
)
guard339: BinaryAssociation = BinaryAssociation(
    name="guard339",
    ends={
        Property(name="uml_Constraint341", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition340", type=uml_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
submachine364: BinaryAssociation = BinaryAssociation(
    name="submachine364",
    ends={
        Property(name="StateMachine365", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=uml_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
connection366: BinaryAssociation = BinaryAssociation(
    name="connection366",
    ends={
        Property(name="ConnectionPointReference", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=uml_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint367: BinaryAssociation = BinaryAssociation(
    name="connectionPoint367",
    ends={
        Property(name="Pseudostate369", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state368", type=uml_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState371: BinaryAssociation = BinaryAssociation(
    name="redefinedState371",
    ends={
        Property(name="uml_State", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State370", type=uml_State, multiplicity=Multiplicity(0, 1))
    }
)
stateInvariant372: BinaryAssociation = BinaryAssociation(
    name="stateInvariant372",
    ends={
        Property(name="uml_Constraint374", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State373", type=uml_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry375: BinaryAssociation = BinaryAssociation(
    name="entry375",
    ends={
        Property(name="uml_Behavior377", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State376", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit378: BinaryAssociation = BinaryAssociation(
    name="exit378",
    ends={
        Property(name="uml_Behavior380", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State379", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity381: BinaryAssociation = BinaryAssociation(
    name="doActivity381",
    ends={
        Property(name="uml_Behavior383", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State382", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTrigger384: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger384",
    ends={
        Property(name="uml_Trigger386", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State385", type=uml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provided358: BinaryAssociation = BinaryAssociation(
    name="provided358",
    ends={
        Property(name="uml_Interface360", type=uml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Port359", type=uml_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocol361: BinaryAssociation = BinaryAssociation(
    name="protocol361",
    ends={
        Property(name="uml_ProtocolStateMachine363", type=uml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Port362", type=uml_ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine396: BinaryAssociation = BinaryAssociation(
    name="stateMachine396",
    ends={
        Property(name="connectionPoint", type=uml_StateMachine, multiplicity=Multiplicity(0, 1)),
        Property(name="StateMachine397", type=uml_Pseudostate, multiplicity=Multiplicity(1, 1))
    }
)
state398: BinaryAssociation = BinaryAssociation(
    name="state398",
    ends={
        Property(name="State400", type=uml_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint399", type=uml_State, multiplicity=Multiplicity(0, 1))
    }
)
generalMachine401: BinaryAssociation = BinaryAssociation(
    name="generalMachine401",
    ends={
        Property(name="uml_ProtocolStateMachine402", type=uml_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ProtocolConformance", type=uml_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
specificMachine403: BinaryAssociation = BinaryAssociation(
    name="specificMachine403",
    ends={
        Property(name="ProtocolStateMachine", type=uml_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="conformance", type=uml_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
ownedPort404: BinaryAssociation = BinaryAssociation(
    name="ownedPort404",
    ends={
        Property(name="uml_Port405", type=uml_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_EncapsulatedClassifier", type=uml_Port, multiplicity=Multiplicity(0, 9999))
    }
)
region387: BinaryAssociation = BinaryAssociation(
    name="region387",
    ends={
        Property(name="Region389", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state388", type=uml_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry390: BinaryAssociation = BinaryAssociation(
    name="entry390",
    ends={
        Property(name="uml_Pseudostate", type=uml_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectionPointReference", type=uml_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit391: BinaryAssociation = BinaryAssociation(
    name="exit391",
    ends={
        Property(name="uml_Pseudostate393", type=uml_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConnectionPointReference392", type=uml_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
state394: BinaryAssociation = BinaryAssociation(
    name="state394",
    ends={
        Property(name="State395", type=uml_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=uml_State, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConnector420: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector420",
    ends={
        Property(name="uml_Connector421", type=uml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Connector419", type=uml_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
end422: BinaryAssociation = BinaryAssociation(
    name="end422",
    ends={
        Property(name="uml_ConnectorEnd424", type=uml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Connector423", type=uml_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract425: BinaryAssociation = BinaryAssociation(
    name="contract425",
    ends={
        Property(name="uml_Behavior427", type=uml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Connector426", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
metaclass428: BinaryAssociation = BinaryAssociation(
    name="metaclass428",
    ends={
        Property(name="Class429", type=uml_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=uml_Class, multiplicity=Multiplicity(1, 1))
    }
)
icon430: BinaryAssociation = BinaryAssociation(
    name="icon430",
    ends={
        Property(name="uml_Image", type=uml_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Stereotype", type=uml_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute406: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute406",
    ends={
        Property(name="uml_Property407", type=uml_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuredClassifier", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part408: BinaryAssociation = BinaryAssociation(
    name="part408",
    ends={
        Property(name="uml_Property410", type=uml_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuredClassifier409", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
role411: BinaryAssociation = BinaryAssociation(
    name="role411",
    ends={
        Property(name="uml_ConnectableElement413", type=uml_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuredClassifier412", type=uml_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector414: BinaryAssociation = BinaryAssociation(
    name="ownedConnector414",
    ends={
        Property(name="uml_Connector", type=uml_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuredClassifier415", type=uml_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type416: BinaryAssociation = BinaryAssociation(
    name="type416",
    ends={
        Property(name="uml_Association418", type=uml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Connector417", type=uml_Association, multiplicity=Multiplicity(0, 1))
    }
)
parameter439: BinaryAssociation = BinaryAssociation(
    name="parameter439",
    ends={
        Property(name="Parameter", type=uml_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSet", type=uml_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
condition440: BinaryAssociation = BinaryAssociation(
    name="condition440",
    ends={
        Property(name="uml_Constraint442", type=uml_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ParameterSet441", type=uml_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute443: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute443",
    ends={
        Property(name="Property444", type=uml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation445: BinaryAssociation = BinaryAssociation(
    name="ownedOperation445",
    ends={
        Property(name="Operation447", type=uml_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype446", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStereotype431: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype431",
    ends={
        Property(name="uml_Stereotype432", type=uml_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Profile", type=uml_Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
metaclassReference433: BinaryAssociation = BinaryAssociation(
    name="metaclassReference433",
    ends={
        Property(name="uml_ElementImport435", type=uml_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Profile434", type=uml_ElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference436: BinaryAssociation = BinaryAssociation(
    name="metamodelReference436",
    ends={
        Property(name="uml_PackageImport438", type=uml_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Profile437", type=uml_PackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationRole453: BinaryAssociation = BinaryAssociation(
    name="collaborationRole453",
    ends={
        Property(name="uml_Collaboration454", type=uml_ConnectableElement, multiplicity=Multiplicity(0, 9999)),
        Property(name="uml_ConnectableElement455", type=uml_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
include456: BinaryAssociation = BinaryAssociation(
    name="include456",
    ends={
        Property(name="Include", type=uml_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="includingCase", type=uml_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend457: BinaryAssociation = BinaryAssociation(
    name="extend457",
    ends={
        Property(name="Extend", type=uml_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension458", type=uml_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint459: BinaryAssociation = BinaryAssociation(
    name="extensionPoint459",
    ends={
        Property(name="ExtensionPoint", type=uml_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=uml_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject460: BinaryAssociation = BinaryAssociation(
    name="subject460",
    ends={
        Property(name="Classifier462", type=uml_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase461", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
addition463: BinaryAssociation = BinaryAssociation(
    name="addition463",
    ends={
        Property(name="uml_UseCase464", type=uml_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Include", type=uml_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase465: BinaryAssociation = BinaryAssociation(
    name="includingCase465",
    ends={
        Property(name="UseCase466", type=uml_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=uml_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extendedCase467: BinaryAssociation = BinaryAssociation(
    name="extendedCase467",
    ends={
        Property(name="uml_UseCase468", type=uml_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Extend", type=uml_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
type448: BinaryAssociation = BinaryAssociation(
    name="type448",
    ends={
        Property(name="uml_Collaboration", type=uml_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CollaborationUse449", type=uml_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding450: BinaryAssociation = BinaryAssociation(
    name="roleBinding450",
    ends={
        Property(name="uml_Dependency452", type=uml_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CollaborationUse451", type=uml_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritedParameter480: BinaryAssociation = BinaryAssociation(
    name="inheritedParameter480",
    ends={
        Property(name="uml_TemplateParameter482", type=uml_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RedefinableTemplateSignature481", type=uml_TemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
classifier483: BinaryAssociation = BinaryAssociation(
    name="classifier483",
    ends={
        Property(name="uml_Classifier485", type=uml_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RedefinableTemplateSignature484", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
constrainingClassifier486: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier486",
    ends={
        Property(name="uml_Classifier487", type=uml_ClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ClassifierTemplateParameter", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
subExpression489: BinaryAssociation = BinaryAssociation(
    name="subExpression489",
    ends={
        Property(name="StringExpression", type=uml_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=uml_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningExpression491: BinaryAssociation = BinaryAssociation(
    name="owningExpression491",
    ends={
        Property(name="StringExpression492", type=uml_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=uml_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand493: BinaryAssociation = BinaryAssociation(
    name="operand493",
    ends={
        Property(name="uml_ValueSpecification494", type=uml_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Expression", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition469: BinaryAssociation = BinaryAssociation(
    name="condition469",
    ends={
        Property(name="uml_Constraint471", type=uml_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Extend470", type=uml_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionLocation472: BinaryAssociation = BinaryAssociation(
    name="extensionLocation472",
    ends={
        Property(name="uml_ExtensionPoint", type=uml_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Extend473", type=uml_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension474: BinaryAssociation = BinaryAssociation(
    name="extension474",
    ends={
        Property(name="UseCase475", type=uml_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=uml_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase476: BinaryAssociation = BinaryAssociation(
    name="useCase476",
    ends={
        Property(name="UseCase477", type=uml_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=uml_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extendedSignature479: BinaryAssociation = BinaryAssociation(
    name="extendedSignature479",
    ends={
        Property(name="uml_RedefinableTemplateSignature", type=uml_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RedefinableTemplateSignature478", type=uml_RedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral503: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral503",
    ends={
        Property(name="EnumerationLiteral", type=uml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=uml_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration504: BinaryAssociation = BinaryAssociation(
    name="enumeration504",
    ends={
        Property(name="Enumeration", type=uml_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=uml_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
classifier505: BinaryAssociation = BinaryAssociation(
    name="classifier505",
    ends={
        Property(name="uml_Classifier506", type=uml_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InstanceSpecification", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot507: BinaryAssociation = BinaryAssociation(
    name="slot507",
    ends={
        Property(name="Slot", type=uml_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=uml_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification508: BinaryAssociation = BinaryAssociation(
    name="specification508",
    ends={
        Property(name="uml_ValueSpecification510", type=uml_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InstanceSpecification509", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mergedPackage495: BinaryAssociation = BinaryAssociation(
    name="mergedPackage495",
    ends={
        Property(name="uml_Package496", type=uml_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_PackageMerge", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage497: BinaryAssociation = BinaryAssociation(
    name="receivingPackage497",
    ends={
        Property(name="Package498", type=uml_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
appliedProfile499: BinaryAssociation = BinaryAssociation(
    name="appliedProfile499",
    ends={
        Property(name="uml_Profile500", type=uml_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ProfileApplication", type=uml_Profile, multiplicity=Multiplicity(1, 1))
    }
)
applyingPackage501: BinaryAssociation = BinaryAssociation(
    name="applyingPackage501",
    ends={
        Property(name="Package502", type=uml_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="profileApplication", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
instance516: BinaryAssociation = BinaryAssociation(
    name="instance516",
    ends={
        Property(name="uml_InstanceSpecification517", type=uml_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InstanceValue", type=uml_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
inputValue518: BinaryAssociation = BinaryAssociation(
    name="inputValue518",
    ends={
        Property(name="uml_InputPin", type=uml_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_OpaqueAction", type=uml_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature511: BinaryAssociation = BinaryAssociation(
    name="definingFeature511",
    ends={
        Property(name="uml_StructuralFeature", type=uml_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Slot", type=uml_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value512: BinaryAssociation = BinaryAssociation(
    name="value512",
    ends={
        Property(name="uml_ValueSpecification514", type=uml_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Slot513", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance515: BinaryAssociation = BinaryAssociation(
    name="owningInstance515",
    ends={
        Property(name="InstanceSpecification", type=uml_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=uml_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
localPrecondition529: BinaryAssociation = BinaryAssociation(
    name="localPrecondition529",
    ends={
        Property(name="uml_Action530", type=uml_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml_Constraint531", type=uml_Action, multiplicity=Multiplicity(1, 1))
    }
)
localPostcondition532: BinaryAssociation = BinaryAssociation(
    name="localPostcondition532",
    ends={
        Property(name="uml_Constraint534", type=uml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Action533", type=uml_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler535: BinaryAssociation = BinaryAssociation(
    name="handler535",
    ends={
        Property(name="ExceptionHandler", type=uml_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedNode", type=uml_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode536: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode536",
    ends={
        Property(name="StructuredActivityNode", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=uml_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity537: BinaryAssociation = BinaryAssociation(
    name="activity537",
    ends={
        Property(name="Activity", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node538", type=uml_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing539: BinaryAssociation = BinaryAssociation(
    name="outgoing539",
    ends={
        Property(name="ActivityEdge", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming540: BinaryAssociation = BinaryAssociation(
    name="incoming540",
    ends={
        Property(name="ActivityEdge541", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition542: BinaryAssociation = BinaryAssociation(
    name="inPartition542",
    ends={
        Property(name="ActivityPartition", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node543", type=uml_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion544: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion544",
    ends={
        Property(name="InterruptibleActivityRegion", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node545", type=uml_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
outputValue519: BinaryAssociation = BinaryAssociation(
    name="outputValue519",
    ends={
        Property(name="uml_OutputPin", type=uml_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_OpaqueAction520", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output521: BinaryAssociation = BinaryAssociation(
    name="output521",
    ends={
        Property(name="uml_OutputPin522", type=uml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Action", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
input523: BinaryAssociation = BinaryAssociation(
    name="input523",
    ends={
        Property(name="uml_InputPin525", type=uml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Action524", type=uml_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context526: BinaryAssociation = BinaryAssociation(
    name="context526",
    ends={
        Property(name="uml_Classifier528", type=uml_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Action527", type=uml_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
edge550: BinaryAssociation = BinaryAssociation(
    name="edge550",
    ends={
        Property(name="inStructuredNode", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ActivityEdge551", type=uml_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
node552: BinaryAssociation = BinaryAssociation(
    name="node552",
    ends={
        Property(name="ActivityNode", type=uml_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode553", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgroup555: BinaryAssociation = BinaryAssociation(
    name="subgroup555",
    ends={
        Property(name="ActivityGroup556", type=uml_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroup", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
superGroup558: BinaryAssociation = BinaryAssociation(
    name="superGroup558",
    ends={
        Property(name="ActivityGroup559", type=uml_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="subgroup", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity560: BinaryAssociation = BinaryAssociation(
    name="inActivity560",
    ends={
        Property(name="Activity561", type=uml_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=uml_Activity, multiplicity=Multiplicity(0, 1))
    }
)
containedEdge562: BinaryAssociation = BinaryAssociation(
    name="containedEdge562",
    ends={
        Property(name="ActivityEdge563", type=uml_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode564: BinaryAssociation = BinaryAssociation(
    name="containedNode564",
    ends={
        Property(name="ActivityNode566", type=uml_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup565", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup546: BinaryAssociation = BinaryAssociation(
    name="inGroup546",
    ends={
        Property(name="ActivityGroup", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode548: BinaryAssociation = BinaryAssociation(
    name="redefinedNode548",
    ends={
        Property(name="uml_ActivityNode", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityNode547", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable549: BinaryAssociation = BinaryAssociation(
    name="variable549",
    ends={
        Property(name="Variable", type=uml_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=uml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group577: BinaryAssociation = BinaryAssociation(
    name="group577",
    ends={
        Property(name="ActivityGroup578", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="inActivity", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scope579: BinaryAssociation = BinaryAssociation(
    name="scope579",
    ends={
        Property(name="StructuredActivityNode580", type=uml_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=uml_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activityScope581: BinaryAssociation = BinaryAssociation(
    name="activityScope581",
    ends={
        Property(name="Activity583", type=uml_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable582", type=uml_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source584: BinaryAssociation = BinaryAssociation(
    name="source584",
    ends={
        Property(name="ActivityNode585", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target586: BinaryAssociation = BinaryAssociation(
    name="target586",
    ends={
        Property(name="ActivityNode587", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=uml_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge589: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge589",
    ends={
        Property(name="uml_ActivityEdge", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityEdge588", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition590: BinaryAssociation = BinaryAssociation(
    name="inPartition590",
    ends={
        Property(name="ActivityPartition591", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=uml_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
guard592: BinaryAssociation = BinaryAssociation(
    name="guard592",
    ends={
        Property(name="uml_ValueSpecification594", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityEdge593", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuredNode567: BinaryAssociation = BinaryAssociation(
    name="structuredNode567",
    ends={
        Property(name="uml_StructuredActivityNode", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Activity", type=uml_StructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable568: BinaryAssociation = BinaryAssociation(
    name="variable568",
    ends={
        Property(name="Variable569", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityScope", type=uml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node570: BinaryAssociation = BinaryAssociation(
    name="node570",
    ends={
        Property(name="ActivityNode571", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge572: BinaryAssociation = BinaryAssociation(
    name="edge572",
    ends={
        Property(name="ActivityEdge574", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity573", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition575: BinaryAssociation = BinaryAssociation(
    name="partition575",
    ends={
        Property(name="uml_ActivityPartition", type=uml_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Activity576", type=uml_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
interrupts598: BinaryAssociation = BinaryAssociation(
    name="interrupts598",
    ends={
        Property(name="InterruptibleActivityRegion599", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="interruptingEdge", type=uml_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode600: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode600",
    ends={
        Property(name="StructuredActivityNode602", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge601", type=uml_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inGroup603: BinaryAssociation = BinaryAssociation(
    name="inGroup603",
    ends={
        Property(name="ActivityGroup604", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge", type=uml_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
activity605: BinaryAssociation = BinaryAssociation(
    name="activity605",
    ends={
        Property(name="Activity607", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge606", type=uml_Activity, multiplicity=Multiplicity(0, 1))
    }
)
weight595: BinaryAssociation = BinaryAssociation(
    name="weight595",
    ends={
        Property(name="uml_ValueSpecification597", type=uml_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityEdge596", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superPartition614: BinaryAssociation = BinaryAssociation(
    name="superPartition614",
    ends={
        Property(name="ActivityPartition615", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="subpartition", type=uml_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents616: BinaryAssociation = BinaryAssociation(
    name="represents616",
    ends={
        Property(name="uml_Element618", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityPartition617", type=uml_Element, multiplicity=Multiplicity(0, 1))
    }
)
edge619: BinaryAssociation = BinaryAssociation(
    name="edge619",
    ends={
        Property(name="ActivityEdge621", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition620", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node622: BinaryAssociation = BinaryAssociation(
    name="node622",
    ends={
        Property(name="ActivityNode623", type=uml_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="inInterruptibleRegion", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
interruptingEdge624: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge624",
    ends={
        Property(name="ActivityEdge625", type=uml_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="interrupts", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
handlerBody626: BinaryAssociation = BinaryAssociation(
    name="handlerBody626",
    ends={
        Property(name="uml_ExecutableNode", type=uml_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExceptionHandler", type=uml_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput627: BinaryAssociation = BinaryAssociation(
    name="exceptionInput627",
    ends={
        Property(name="uml_ObjectNode", type=uml_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExceptionHandler628", type=uml_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
node608: BinaryAssociation = BinaryAssociation(
    name="node608",
    ends={
        Property(name="ActivityNode609", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition", type=uml_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition611: BinaryAssociation = BinaryAssociation(
    name="subpartition611",
    ends={
        Property(name="ActivityPartition612", type=uml_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="superPartition", type=uml_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selection639: BinaryAssociation = BinaryAssociation(
    name="selection639",
    ends={
        Property(name="uml_Behavior641", type=uml_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ObjectNode640", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
result642: BinaryAssociation = BinaryAssociation(
    name="result642",
    ends={
        Property(name="uml_OutputPin643", type=uml_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CallAction", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument644: BinaryAssociation = BinaryAssociation(
    name="argument644",
    ends={
        Property(name="uml_InputPin645", type=uml_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InvocationAction", type=uml_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onPort646: BinaryAssociation = BinaryAssociation(
    name="onPort646",
    ends={
        Property(name="uml_Port648", type=uml_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InvocationAction647", type=uml_Port, multiplicity=Multiplicity(0, 1))
    }
)
exceptionType629: BinaryAssociation = BinaryAssociation(
    name="exceptionType629",
    ends={
        Property(name="uml_Classifier631", type=uml_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExceptionHandler630", type=uml_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
protectedNode632: BinaryAssociation = BinaryAssociation(
    name="protectedNode632",
    ends={
        Property(name="ExecutableNode", type=uml_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handler", type=uml_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
upperBound633: BinaryAssociation = BinaryAssociation(
    name="upperBound633",
    ends={
        Property(name="uml_ValueSpecification635", type=uml_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ObjectNode634", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inState636: BinaryAssociation = BinaryAssociation(
    name="inState636",
    ends={
        Property(name="uml_State638", type=uml_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ObjectNode637", type=uml_State, multiplicity=Multiplicity(0, 9999))
    }
)
executableNode661: BinaryAssociation = BinaryAssociation(
    name="executableNode661",
    ends={
        Property(name="uml_ExecutableNode662", type=uml_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SequenceNode", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter663: BinaryAssociation = BinaryAssociation(
    name="parameter663",
    ends={
        Property(name="uml_Parameter664", type=uml_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActivityParameterNode", type=uml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value665: BinaryAssociation = BinaryAssociation(
    name="value665",
    ends={
        Property(name="uml_ValueSpecification666", type=uml_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ValuePin", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target649: BinaryAssociation = BinaryAssociation(
    name="target649",
    ends={
        Property(name="uml_InputPin650", type=uml_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendSignalAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal651: BinaryAssociation = BinaryAssociation(
    name="signal651",
    ends={
        Property(name="uml_Signal653", type=uml_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendSignalAction652", type=uml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation654: BinaryAssociation = BinaryAssociation(
    name="operation654",
    ends={
        Property(name="uml_Operation655", type=uml_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CallOperationAction", type=uml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target656: BinaryAssociation = BinaryAssociation(
    name="target656",
    ends={
        Property(name="uml_InputPin658", type=uml_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CallOperationAction657", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
behavior659: BinaryAssociation = BinaryAssociation(
    name="behavior659",
    ends={
        Property(name="uml_Behavior660", type=uml_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CallBehaviorAction", type=uml_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
message681: BinaryAssociation = BinaryAssociation(
    name="message681",
    ends={
        Property(name="uml_Message683", type=uml_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_MessageEnd682", type=uml_Message, multiplicity=Multiplicity(0, 1))
    }
)
lifeline684: BinaryAssociation = BinaryAssociation(
    name="lifeline684",
    ends={
        Property(name="Lifeline", type=uml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=uml_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragment685: BinaryAssociation = BinaryAssociation(
    name="fragment685",
    ends={
        Property(name="InteractionFragment", type=uml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingInteraction", type=uml_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action686: BinaryAssociation = BinaryAssociation(
    name="action686",
    ends={
        Property(name="uml_Action687", type=uml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interaction", type=uml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate688: BinaryAssociation = BinaryAssociation(
    name="formalGate688",
    ends={
        Property(name="uml_Gate", type=uml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interaction689", type=uml_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiveEvent667: BinaryAssociation = BinaryAssociation(
    name="receiveEvent667",
    ends={
        Property(name="uml_MessageEnd", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Message", type=uml_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent668: BinaryAssociation = BinaryAssociation(
    name="sendEvent668",
    ends={
        Property(name="uml_MessageEnd670", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Message669", type=uml_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
connector671: BinaryAssociation = BinaryAssociation(
    name="connector671",
    ends={
        Property(name="uml_Connector673", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Message672", type=uml_Connector, multiplicity=Multiplicity(0, 1))
    }
)
interaction674: BinaryAssociation = BinaryAssociation(
    name="interaction674",
    ends={
        Property(name="Interaction", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=uml_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
argument675: BinaryAssociation = BinaryAssociation(
    name="argument675",
    ends={
        Property(name="uml_ValueSpecification677", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Message676", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature678: BinaryAssociation = BinaryAssociation(
    name="signature678",
    ends={
        Property(name="uml_NamedElement680", type=uml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Message679", type=uml_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
represents699: BinaryAssociation = BinaryAssociation(
    name="represents699",
    ends={
        Property(name="uml_ConnectableElement700", type=uml_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Lifeline", type=uml_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
interaction701: BinaryAssociation = BinaryAssociation(
    name="interaction701",
    ends={
        Property(name="Interaction702", type=uml_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="lifeline", type=uml_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
selector703: BinaryAssociation = BinaryAssociation(
    name="selector703",
    ends={
        Property(name="uml_ValueSpecification705", type=uml_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Lifeline704", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs706: BinaryAssociation = BinaryAssociation(
    name="decomposedAs706",
    ends={
        Property(name="uml_PartDecomposition", type=uml_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Lifeline707", type=uml_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy708: BinaryAssociation = BinaryAssociation(
    name="coveredBy708",
    ends={
        Property(name="InteractionFragment709", type=uml_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=uml_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo710: BinaryAssociation = BinaryAssociation(
    name="refersTo710",
    ends={
        Property(name="uml_Interaction711", type=uml_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionUse", type=uml_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
actualGate712: BinaryAssociation = BinaryAssociation(
    name="actualGate712",
    ends={
        Property(name="uml_Gate714", type=uml_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionUse713", type=uml_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message690: BinaryAssociation = BinaryAssociation(
    name="message690",
    ends={
        Property(name="Message", type=uml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction691", type=uml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered692: BinaryAssociation = BinaryAssociation(
    name="covered692",
    ends={
        Property(name="Lifeline693", type=uml_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=uml_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering694: BinaryAssociation = BinaryAssociation(
    name="generalOrdering694",
    ends={
        Property(name="uml_GeneralOrdering", type=uml_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionFragment", type=uml_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingInteraction695: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction695",
    ends={
        Property(name="Interaction696", type=uml_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment", type=uml_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
enclosingOperand697: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand697",
    ends={
        Property(name="InteractionOperand", type=uml_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment698", type=uml_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
event722: BinaryAssociation = BinaryAssociation(
    name="event722",
    ends={
        Property(name="uml_Event723", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_OccurrenceSpecification", type=uml_Event, multiplicity=Multiplicity(1, 1))
    }
)
toAfter724: BinaryAssociation = BinaryAssociation(
    name="toAfter724",
    ends={
        Property(name="GeneralOrdering725", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="before", type=uml_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
guard726: BinaryAssociation = BinaryAssociation(
    name="guard726",
    ends={
        Property(name="uml_InteractionConstraint", type=uml_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionOperand", type=uml_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragment727: BinaryAssociation = BinaryAssociation(
    name="fragment727",
    ends={
        Property(name="InteractionFragment728", type=uml_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingOperand", type=uml_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minint729: BinaryAssociation = BinaryAssociation(
    name="minint729",
    ends={
        Property(name="uml_ValueSpecification731", type=uml_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionConstraint730", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxint732: BinaryAssociation = BinaryAssociation(
    name="maxint732",
    ends={
        Property(name="uml_ValueSpecification734", type=uml_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionConstraint733", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start735: BinaryAssociation = BinaryAssociation(
    name="start735",
    ends={
        Property(name="uml_OccurrenceSpecification736", type=uml_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExecutionSpecification", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
finish737: BinaryAssociation = BinaryAssociation(
    name="finish737",
    ends={
        Property(name="uml_OccurrenceSpecification739", type=uml_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExecutionSpecification738", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
argument715: BinaryAssociation = BinaryAssociation(
    name="argument715",
    ends={
        Property(name="uml_Action717", type=uml_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InteractionUse716", type=uml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
before718: BinaryAssociation = BinaryAssociation(
    name="before718",
    ends={
        Property(name="OccurrenceSpecification", type=uml_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toAfter", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
after719: BinaryAssociation = BinaryAssociation(
    name="after719",
    ends={
        Property(name="OccurrenceSpecification720", type=uml_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toBefore", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
toBefore721: BinaryAssociation = BinaryAssociation(
    name="toBefore721",
    ends={
        Property(name="GeneralOrdering", type=uml_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="after", type=uml_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
operation746: BinaryAssociation = BinaryAssociation(
    name="operation746",
    ends={
        Property(name="uml_Operation747", type=uml_SendOperationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendOperationEvent", type=uml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal748: BinaryAssociation = BinaryAssociation(
    name="signal748",
    ends={
        Property(name="uml_Signal749", type=uml_SendSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendSignalEvent", type=uml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
execution750: BinaryAssociation = BinaryAssociation(
    name="execution750",
    ends={
        Property(name="uml_ExecutionSpecification751", type=uml_ExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ExecutionOccurrenceSpecification", type=uml_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
operation752: BinaryAssociation = BinaryAssociation(
    name="operation752",
    ends={
        Property(name="uml_Operation753", type=uml_ReceiveOperationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReceiveOperationEvent", type=uml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal754: BinaryAssociation = BinaryAssociation(
    name="signal754",
    ends={
        Property(name="uml_Signal755", type=uml_ReceiveSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReceiveSignalEvent", type=uml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
invariant740: BinaryAssociation = BinaryAssociation(
    name="invariant740",
    ends={
        Property(name="uml_Constraint741", type=uml_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StateInvariant", type=uml_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action742: BinaryAssociation = BinaryAssociation(
    name="action742",
    ends={
        Property(name="uml_Action743", type=uml_ActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActionExecutionSpecification", type=uml_Action, multiplicity=Multiplicity(1, 1))
    }
)
behavior744: BinaryAssociation = BinaryAssociation(
    name="behavior744",
    ends={
        Property(name="uml_Behavior745", type=uml_BehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehaviorExecutionSpecification", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput762: BinaryAssociation = BinaryAssociation(
    name="decisionInput762",
    ends={
        Property(name="uml_Behavior763", type=uml_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DecisionNode", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow764: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow764",
    ends={
        Property(name="uml_ObjectFlow", type=uml_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DecisionNode765", type=uml_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
transformation766: BinaryAssociation = BinaryAssociation(
    name="transformation766",
    ends={
        Property(name="uml_Behavior768", type=uml_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ObjectFlow767", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection769: BinaryAssociation = BinaryAssociation(
    name="selection769",
    ends={
        Property(name="uml_Behavior771", type=uml_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ObjectFlow770", type=uml_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
operation756: BinaryAssociation = BinaryAssociation(
    name="operation756",
    ends={
        Property(name="uml_Operation757", type=uml_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CallEvent", type=uml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression758: BinaryAssociation = BinaryAssociation(
    name="changeExpression758",
    ends={
        Property(name="uml_ValueSpecification759", type=uml_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ChangeEvent", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal760: BinaryAssociation = BinaryAssociation(
    name="signal760",
    ends={
        Property(name="uml_Signal761", type=uml_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SignalEvent", type=uml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement780: BinaryAssociation = BinaryAssociation(
    name="packagedElement780",
    ends={
        Property(name="uml_Component781", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml_PackageableElement782", type=uml_Component, multiplicity=Multiplicity(1, 1))
    }
)
realization783: BinaryAssociation = BinaryAssociation(
    name="realization783",
    ends={
        Property(name="ComponentRealization", type=uml_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="abstraction", type=uml_ComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedNode785: BinaryAssociation = BinaryAssociation(
    name="nestedNode785",
    ends={
        Property(name="uml_Node", type=uml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Node784", type=uml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand786: BinaryAssociation = BinaryAssociation(
    name="operand786",
    ends={
        Property(name="uml_InteractionOperand787", type=uml_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CombinedFragment", type=uml_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cfragmentGate788: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate788",
    ends={
        Property(name="uml_Gate790", type=uml_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CombinedFragment789", type=uml_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstraction772: BinaryAssociation = BinaryAssociation(
    name="abstraction772",
    ends={
        Property(name="Component", type=uml_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="realization", type=uml_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier773: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier773",
    ends={
        Property(name="uml_Classifier774", type=uml_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ComponentRealization", type=uml_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
required775: BinaryAssociation = BinaryAssociation(
    name="required775",
    ends={
        Property(name="uml_Interface776", type=uml_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Component", type=uml_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided777: BinaryAssociation = BinaryAssociation(
    name="provided777",
    ends={
        Property(name="uml_Interface779", type=uml_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Component778", type=uml_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
classifier793: BinaryAssociation = BinaryAssociation(
    name="classifier793",
    ends={
        Property(name="uml_Classifier794", type=uml_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CreateObjectAction", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result795: BinaryAssociation = BinaryAssociation(
    name="result795",
    ends={
        Property(name="uml_OutputPin797", type=uml_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CreateObjectAction796", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target798: BinaryAssociation = BinaryAssociation(
    name="target798",
    ends={
        Property(name="uml_InputPin799", type=uml_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DestroyObjectAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first800: BinaryAssociation = BinaryAssociation(
    name="first800",
    ends={
        Property(name="uml_InputPin801", type=uml_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TestIdentityAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second802: BinaryAssociation = BinaryAssociation(
    name="second802",
    ends={
        Property(name="uml_InputPin804", type=uml_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TestIdentityAction803", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result805: BinaryAssociation = BinaryAssociation(
    name="result805",
    ends={
        Property(name="uml_OutputPin807", type=uml_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TestIdentityAction806", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message791: BinaryAssociation = BinaryAssociation(
    name="message791",
    ends={
        Property(name="uml_NamedElement792", type=uml_ConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConsiderIgnoreFragment", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
value817: BinaryAssociation = BinaryAssociation(
    name="value817",
    ends={
        Property(name="uml_InputPin818", type=uml_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_WriteStructuralFeatureAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result819: BinaryAssociation = BinaryAssociation(
    name="result819",
    ends={
        Property(name="uml_OutputPin821", type=uml_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_WriteStructuralFeatureAction820", type=uml_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result822: BinaryAssociation = BinaryAssociation(
    name="result822",
    ends={
        Property(name="uml_OutputPin823", type=uml_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ClearStructuralFeatureAction", type=uml_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt824: BinaryAssociation = BinaryAssociation(
    name="removeAt824",
    ends={
        Property(name="uml_InputPin825", type=uml_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RemoveStructuralFeatureValueAction", type=uml_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt826: BinaryAssociation = BinaryAssociation(
    name="insertAt826",
    ends={
        Property(name="uml_InputPin827", type=uml_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_AddStructuralFeatureValueAction", type=uml_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endData828: BinaryAssociation = BinaryAssociation(
    name="endData828",
    ends={
        Property(name="uml_LinkEndData", type=uml_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkAction", type=uml_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
result808: BinaryAssociation = BinaryAssociation(
    name="result808",
    ends={
        Property(name="uml_OutputPin809", type=uml_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadSelfAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature810: BinaryAssociation = BinaryAssociation(
    name="structuralFeature810",
    ends={
        Property(name="uml_StructuralFeature811", type=uml_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuralFeatureAction", type=uml_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object812: BinaryAssociation = BinaryAssociation(
    name="object812",
    ends={
        Property(name="uml_InputPin814", type=uml_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuralFeatureAction813", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result815: BinaryAssociation = BinaryAssociation(
    name="result815",
    ends={
        Property(name="uml_OutputPin816", type=uml_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadStructuralFeatureAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier840: BinaryAssociation = BinaryAssociation(
    name="qualifier840",
    ends={
        Property(name="uml_Property842", type=uml_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_QualifierValue841", type=uml_Property, multiplicity=Multiplicity(1, 1))
    }
)
value843: BinaryAssociation = BinaryAssociation(
    name="value843",
    ends={
        Property(name="uml_InputPin845", type=uml_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_QualifierValue844", type=uml_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
result846: BinaryAssociation = BinaryAssociation(
    name="result846",
    ends={
        Property(name="uml_OutputPin847", type=uml_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt848: BinaryAssociation = BinaryAssociation(
    name="insertAt848",
    ends={
        Property(name="uml_InputPin849", type=uml_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkEndCreationData", type=uml_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt850: BinaryAssociation = BinaryAssociation(
    name="destroyAt850",
    ends={
        Property(name="uml_InputPin851", type=uml_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkEndDestructionData", type=uml_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
inputValue829: BinaryAssociation = BinaryAssociation(
    name="inputValue829",
    ends={
        Property(name="uml_InputPin831", type=uml_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkAction830", type=uml_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value832: BinaryAssociation = BinaryAssociation(
    name="value832",
    ends={
        Property(name="uml_InputPin834", type=uml_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkEndData833", type=uml_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end835: BinaryAssociation = BinaryAssociation(
    name="end835",
    ends={
        Property(name="uml_Property837", type=uml_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkEndData836", type=uml_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier838: BinaryAssociation = BinaryAssociation(
    name="qualifier838",
    ends={
        Property(name="uml_QualifierValue", type=uml_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LinkEndData839", type=uml_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target859: BinaryAssociation = BinaryAssociation(
    name="target859",
    ends={
        Property(name="uml_InputPin860", type=uml_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendObjectAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request861: BinaryAssociation = BinaryAssociation(
    name="request861",
    ends={
        Property(name="uml_InputPin863", type=uml_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_SendObjectAction862", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value864: BinaryAssociation = BinaryAssociation(
    name="value864",
    ends={
        Property(name="uml_ValueSpecification865", type=uml_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ValueSpecificationAction", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result866: BinaryAssociation = BinaryAssociation(
    name="result866",
    ends={
        Property(name="uml_OutputPin868", type=uml_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ValueSpecificationAction867", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object852: BinaryAssociation = BinaryAssociation(
    name="object852",
    ends={
        Property(name="uml_InputPin853", type=uml_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ClearAssociationAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association854: BinaryAssociation = BinaryAssociation(
    name="association854",
    ends={
        Property(name="uml_Association856", type=uml_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ClearAssociationAction855", type=uml_Association, multiplicity=Multiplicity(1, 1))
    }
)
signal857: BinaryAssociation = BinaryAssociation(
    name="signal857",
    ends={
        Property(name="uml_Signal858", type=uml_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BroadcastSignalAction", type=uml_Signal, multiplicity=Multiplicity(1, 1))
    }
)
min878: BinaryAssociation = BinaryAssociation(
    name="min878",
    ends={
        Property(name="uml_ValueSpecification879", type=uml_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interval", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
expr869: BinaryAssociation = BinaryAssociation(
    name="expr869",
    ends={
        Property(name="uml_ValueSpecification870", type=uml_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TimeExpression", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result890: BinaryAssociation = BinaryAssociation(
    name="result890",
    ends={
        Property(name="uml_OutputPin891", type=uml_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadVariableAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
max880: BinaryAssociation = BinaryAssociation(
    name="max880",
    ends={
        Property(name="uml_ValueSpecification882", type=uml_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Interval881", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
observation871: BinaryAssociation = BinaryAssociation(
    name="observation871",
    ends={
        Property(name="uml_Observation", type=uml_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TimeExpression872", type=uml_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
expr873: BinaryAssociation = BinaryAssociation(
    name="expr873",
    ends={
        Property(name="uml_ValueSpecification874", type=uml_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Duration", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation875: BinaryAssociation = BinaryAssociation(
    name="observation875",
    ends={
        Property(name="uml_Observation877", type=uml_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Duration876", type=uml_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
event883: BinaryAssociation = BinaryAssociation(
    name="event883",
    ends={
        Property(name="uml_NamedElement884", type=uml_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TimeObservation", type=uml_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event885: BinaryAssociation = BinaryAssociation(
    name="event885",
    ends={
        Property(name="uml_NamedElement886", type=uml_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DurationObservation", type=uml_NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
when887: BinaryAssociation = BinaryAssociation(
    name="when887",
    ends={
        Property(name="uml_TimeExpression888", type=uml_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TimeEvent", type=uml_TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable889: BinaryAssociation = BinaryAssociation(
    name="variable889",
    ends={
        Property(name="uml_Variable", type=uml_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_VariableAction", type=uml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
fromAction900: BinaryAssociation = BinaryAssociation(
    name="fromAction900",
    ends={
        Property(name="uml_Action901", type=uml_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ActionInputPin", type=uml_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value892: BinaryAssociation = BinaryAssociation(
    name="value892",
    ends={
        Property(name="uml_InputPin893", type=uml_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_WriteVariableAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt894: BinaryAssociation = BinaryAssociation(
    name="insertAt894",
    ends={
        Property(name="uml_InputPin895", type=uml_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_AddVariableValueAction", type=uml_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt896: BinaryAssociation = BinaryAssociation(
    name="removeAt896",
    ends={
        Property(name="uml_InputPin897", type=uml_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RemoveVariableValueAction", type=uml_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception898: BinaryAssociation = BinaryAssociation(
    name="exception898",
    ends={
        Property(name="uml_InputPin899", type=uml_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_RaiseExceptionAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier926: BinaryAssociation = BinaryAssociation(
    name="classifier926",
    ends={
        Property(name="uml_Classifier928", type=uml_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadExtentAction927", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
represented902: BinaryAssociation = BinaryAssociation(
    name="represented902",
    ends={
        Property(name="uml_Classifier903", type=uml_InformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationItem", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
realization904: BinaryAssociation = BinaryAssociation(
    name="realization904",
    ends={
        Property(name="uml_Relationship905", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow", type=uml_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed906: BinaryAssociation = BinaryAssociation(
    name="conveyed906",
    ends={
        Property(name="uml_Classifier908", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow907", type=uml_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
informationSource909: BinaryAssociation = BinaryAssociation(
    name="informationSource909",
    ends={
        Property(name="uml_NamedElement911", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow910", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
informationTarget912: BinaryAssociation = BinaryAssociation(
    name="informationTarget912",
    ends={
        Property(name="uml_NamedElement914", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow913", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
realizingActivityEdge915: BinaryAssociation = BinaryAssociation(
    name="realizingActivityEdge915",
    ends={
        Property(name="uml_ActivityEdge917", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow916", type=uml_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
realizingConnector918: BinaryAssociation = BinaryAssociation(
    name="realizingConnector918",
    ends={
        Property(name="uml_Connector920", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow919", type=uml_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
realizingMessage921: BinaryAssociation = BinaryAssociation(
    name="realizingMessage921",
    ends={
        Property(name="uml_Message923", type=uml_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_InformationFlow922", type=uml_Message, multiplicity=Multiplicity(0, 9999))
    }
)
result924: BinaryAssociation = BinaryAssociation(
    name="result924",
    ends={
        Property(name="uml_OutputPin925", type=uml_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadExtentAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end949: BinaryAssociation = BinaryAssociation(
    name="end949",
    ends={
        Property(name="uml_Property951", type=uml_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndAction950", type=uml_Property, multiplicity=Multiplicity(1, 1))
    }
)
result952: BinaryAssociation = BinaryAssociation(
    name="result952",
    ends={
        Property(name="uml_OutputPin954", type=uml_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndAction953", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier929: BinaryAssociation = BinaryAssociation(
    name="oldClassifier929",
    ends={
        Property(name="uml_Classifier930", type=uml_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReclassifyObjectAction", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier931: BinaryAssociation = BinaryAssociation(
    name="newClassifier931",
    ends={
        Property(name="uml_Classifier933", type=uml_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReclassifyObjectAction932", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object934: BinaryAssociation = BinaryAssociation(
    name="object934",
    ends={
        Property(name="uml_InputPin936", type=uml_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReclassifyObjectAction935", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier937: BinaryAssociation = BinaryAssociation(
    name="classifier937",
    ends={
        Property(name="uml_Classifier938", type=uml_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadIsClassifiedObjectAction", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result939: BinaryAssociation = BinaryAssociation(
    name="result939",
    ends={
        Property(name="uml_OutputPin941", type=uml_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadIsClassifiedObjectAction940", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object942: BinaryAssociation = BinaryAssociation(
    name="object942",
    ends={
        Property(name="uml_InputPin944", type=uml_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadIsClassifiedObjectAction943", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object945: BinaryAssociation = BinaryAssociation(
    name="object945",
    ends={
        Property(name="uml_InputPin946", type=uml_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StartClassifierBehaviorAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object947: BinaryAssociation = BinaryAssociation(
    name="object947",
    ends={
        Property(name="uml_InputPin948", type=uml_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnInformation974: BinaryAssociation = BinaryAssociation(
    name="returnInformation974",
    ends={
        Property(name="uml_InputPin976", type=uml_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReplyAction975", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue977: BinaryAssociation = BinaryAssociation(
    name="replyValue977",
    ends={
        Property(name="uml_InputPin979", type=uml_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReplyAction978", type=uml_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object955: BinaryAssociation = BinaryAssociation(
    name="object955",
    ends={
        Property(name="uml_InputPin956", type=uml_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndQualifierAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result957: BinaryAssociation = BinaryAssociation(
    name="result957",
    ends={
        Property(name="uml_OutputPin959", type=uml_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndQualifierAction958", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier960: BinaryAssociation = BinaryAssociation(
    name="qualifier960",
    ends={
        Property(name="uml_Property962", type=uml_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReadLinkObjectEndQualifierAction961", type=uml_Property, multiplicity=Multiplicity(1, 1))
    }
)
result963: BinaryAssociation = BinaryAssociation(
    name="result963",
    ends={
        Property(name="uml_OutputPin964", type=uml_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_CreateLinkObjectAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result965: BinaryAssociation = BinaryAssociation(
    name="result965",
    ends={
        Property(name="uml_OutputPin966", type=uml_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_AcceptEventAction", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger967: BinaryAssociation = BinaryAssociation(
    name="trigger967",
    ends={
        Property(name="uml_Trigger969", type=uml_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_AcceptEventAction968", type=uml_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnInformation970: BinaryAssociation = BinaryAssociation(
    name="returnInformation970",
    ends={
        Property(name="uml_OutputPin971", type=uml_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_AcceptCallAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyToCall972: BinaryAssociation = BinaryAssociation(
    name="replyToCall972",
    ends={
        Property(name="uml_Trigger973", type=uml_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReplyAction", type=uml_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
joinSpec998: BinaryAssociation = BinaryAssociation(
    name="joinSpec998",
    ends={
        Property(name="uml_ValueSpecification999", type=uml_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_JoinNode", type=uml_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result980: BinaryAssociation = BinaryAssociation(
    name="result980",
    ends={
        Property(name="uml_OutputPin981", type=uml_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UnmarshallAction", type=uml_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
unmarshallType982: BinaryAssociation = BinaryAssociation(
    name="unmarshallType982",
    ends={
        Property(name="uml_Classifier984", type=uml_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UnmarshallAction983", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
object985: BinaryAssociation = BinaryAssociation(
    name="object985",
    ends={
        Property(name="uml_InputPin987", type=uml_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_UnmarshallAction986", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer988: BinaryAssociation = BinaryAssociation(
    name="reducer988",
    ends={
        Property(name="uml_Behavior989", type=uml_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReduceAction", type=uml_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result990: BinaryAssociation = BinaryAssociation(
    name="result990",
    ends={
        Property(name="uml_OutputPin992", type=uml_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReduceAction991", type=uml_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection993: BinaryAssociation = BinaryAssociation(
    name="collection993",
    ends={
        Property(name="uml_InputPin995", type=uml_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ReduceAction994", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object996: BinaryAssociation = BinaryAssociation(
    name="object996",
    ends={
        Property(name="uml_InputPin997", type=uml_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StartObjectBehaviorAction", type=uml_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setupPart1023: BinaryAssociation = BinaryAssociation(
    name="setupPart1023",
    ends={
        Property(name="uml_ExecutableNode1025", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1024", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
decider1026: BinaryAssociation = BinaryAssociation(
    name="decider1026",
    ends={
        Property(name="uml_OutputPin1028", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1027", type=uml_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
clause1000: BinaryAssociation = BinaryAssociation(
    name="clause1000",
    ends={
        Property(name="uml_Clause", type=uml_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConditionalNode", type=uml_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result1001: BinaryAssociation = BinaryAssociation(
    name="result1001",
    ends={
        Property(name="uml_OutputPin1003", type=uml_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ConditionalNode1002", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test1004: BinaryAssociation = BinaryAssociation(
    name="test1004",
    ends={
        Property(name="uml_ExecutableNode1006", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Clause1005", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
body1007: BinaryAssociation = BinaryAssociation(
    name="body1007",
    ends={
        Property(name="uml_ExecutableNode1009", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Clause1008", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause1011: BinaryAssociation = BinaryAssociation(
    name="predecessorClause1011",
    ends={
        Property(name="Clause", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=uml_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause1013: BinaryAssociation = BinaryAssociation(
    name="successorClause1013",
    ends={
        Property(name="Clause1014", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=uml_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider1015: BinaryAssociation = BinaryAssociation(
    name="decider1015",
    ends={
        Property(name="uml_OutputPin1017", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Clause1016", type=uml_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput1018: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1018",
    ends={
        Property(name="uml_OutputPin1020", type=uml_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Clause1019", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart1021: BinaryAssociation = BinaryAssociation(
    name="bodyPart1021",
    ends={
        Property(name="uml_ExecutableNode1022", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
postCondition1050: BinaryAssociation = BinaryAssociation(
    name="postCondition1050",
    ends={
        Property(name="uml_Constraint1051", type=uml_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ProtocolTransition", type=uml_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
referred1052: BinaryAssociation = BinaryAssociation(
    name="referred1052",
    ends={
        Property(name="uml_Operation1054", type=uml_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ProtocolTransition1053", type=uml_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
test1029: BinaryAssociation = BinaryAssociation(
    name="test1029",
    ends={
        Property(name="uml_ExecutableNode1031", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1030", type=uml_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result1032: BinaryAssociation = BinaryAssociation(
    name="result1032",
    ends={
        Property(name="uml_OutputPin1034", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1033", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable1035: BinaryAssociation = BinaryAssociation(
    name="loopVariable1035",
    ends={
        Property(name="uml_OutputPin1037", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1036", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput1038: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1038",
    ends={
        Property(name="uml_OutputPin1040", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1039", type=uml_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput1041: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput1041",
    ends={
        Property(name="uml_InputPin1043", type=uml_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_LoopNode1042", type=uml_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput1044: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput1044",
    ends={
        Property(name="ExpansionRegion", type=uml_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=uml_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput1045: BinaryAssociation = BinaryAssociation(
    name="regionAsInput1045",
    ends={
        Property(name="ExpansionRegion1046", type=uml_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=uml_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement1047: BinaryAssociation = BinaryAssociation(
    name="inputElement1047",
    ends={
        Property(name="ExpansionNode", type=uml_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=uml_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement1048: BinaryAssociation = BinaryAssociation(
    name="outputElement1048",
    ends={
        Property(name="ExpansionNode1049", type=uml_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=uml_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
preCondition1055: BinaryAssociation = BinaryAssociation(
    name="preCondition1055",
    ends={
        Property(name="uml_Constraint1057", type=uml_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ProtocolTransition1056", type=uml_Constraint, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uml_Comment_Element = Generalization(general=Element, specific=uml_Comment)
gen_uml_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Package)
gen_uml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml_PackageableElement)
gen_uml_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_PackageableElement)
gen_uml_NamedElement_Element = Generalization(general=Element, specific=uml_NamedElement)
gen_uml_Element_EModelElement = Generalization(general=EModelElement, specific=uml_Element)
gen_uml_Package_Namespace = Generalization(general=Namespace, specific=uml_Package)
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Dependency)
gen_uml_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=uml_DirectedRelationship)
gen_uml_Relationship_Element = Generalization(general=Element, specific=uml_Relationship)
gen_uml_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml_Namespace)
gen_uml_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml_Dependency)
gen_uml_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_PackageImport)
gen_uml_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=uml_Constraint)
gen_uml_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml_ValueSpecification)
gen_uml_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=uml_ValueSpecification)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)
gen_uml_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_ElementImport)
gen_uml_Classifier_Namespace = Generalization(general=Namespace, specific=uml_Classifier)
gen_uml_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Classifier)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Classifier)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_Association_Classifier = Generalization(general=Classifier, specific=uml_Association)
gen_uml_Association_Relationship = Generalization(general=Relationship, specific=uml_Association)
gen_uml_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=uml_RedefinableElement)
gen_uml_TemplateableElement_Element = Generalization(general=Element, specific=uml_TemplateableElement)
gen_uml_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_TemplateBinding)
gen_uml_TemplateParameter_Element = Generalization(general=Element, specific=uml_TemplateParameter)
gen_uml_TemplateSignature_Element = Generalization(general=Element, specific=uml_TemplateSignature)
gen_uml_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=uml_TemplateParameterSubstitution)
gen_uml_ParameterableElement_Element = Generalization(general=Element, specific=uml_ParameterableElement)
gen_uml_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=uml_GeneralizationSet)
gen_uml_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Feature)
gen_uml_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Generalization)
gen_uml_Realization_Abstraction = Generalization(general=Abstraction, specific=uml_Realization)
gen_uml_Abstraction_Dependency = Generalization(general=Dependency, specific=uml_Abstraction)
gen_uml_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_OpaqueExpression)
gen_uml_Substitution_Realization = Generalization(general=Realization, specific=uml_Substitution)
gen_uml_MultiplicityElement_Element = Generalization(general=Element, specific=uml_MultiplicityElement)
gen_uml_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=uml_Parameter)
gen_uml_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_Parameter)
gen_uml_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=uml_ConnectableElement)
gen_uml_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_ConnectableElement)
gen_uml_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_ConnectorEnd)
gen_uml_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_Property)
gen_uml_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=uml_Property)
gen_uml_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml_Property)
gen_uml_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=uml_DeploymentTarget)
gen_uml_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=uml_DeployedArtifact)
gen_uml_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=uml_DeploymentSpecification)
gen_uml_Artifact_Classifier = Generalization(general=Classifier, specific=uml_Artifact)
gen_uml_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=uml_Artifact)
gen_uml_Deployment_Dependency = Generalization(general=Dependency, specific=uml_Deployment)
gen_uml_Manifestation_Abstraction = Generalization(general=Abstraction, specific=uml_Manifestation)
gen_uml_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml_Operation)
gen_uml_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_Operation)
gen_uml_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Operation)
gen_uml_Behavior_Class = Generalization(general=Class_, specific=uml_Behavior)
gen_uml_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=uml_BehavioralFeature)
gen_uml_BehavioralFeature_Feature = Generalization(general=Feature, specific=uml_BehavioralFeature)
gen_uml_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=uml_Class)
gen_uml_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_Class)
gen_uml_InterfaceRealization_Realization = Generalization(general=Realization, specific=uml_InterfaceRealization)
gen_uml_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=uml_BehavioredClassifier)
gen_uml_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml_Reception)
gen_uml_Signal_Classifier = Generalization(general=Classifier, specific=uml_Signal)
gen_uml_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=uml_ProtocolStateMachine)
gen_uml_Interface_Classifier = Generalization(general=Classifier, specific=uml_Interface)
gen_uml_Vertex_NamedElement = Generalization(general=NamedElement, specific=uml_Vertex)
gen_uml_Transition_Namespace = Generalization(general=Namespace, specific=uml_Transition)
gen_uml_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Transition)
gen_uml_StateMachine_Behavior = Generalization(general=Behavior, specific=uml_StateMachine)
gen_uml_Region_Namespace = Generalization(general=Namespace, specific=uml_Region)
gen_uml_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Region)
gen_uml_Trigger_NamedElement = Generalization(general=NamedElement, specific=uml_Trigger)
gen_uml_Event_PackageableElement = Generalization(general=PackageableElement, specific=uml_Event)
gen_uml_Port_Property = Generalization(general=Property_, specific=uml_Port)
gen_uml_State_Namespace = Generalization(general=Namespace, specific=uml_State)
gen_uml_State_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_State)
gen_uml_State_Vertex = Generalization(general=Vertex, specific=uml_State)
gen_uml_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_ProtocolConformance)
gen_uml_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml_EncapsulatedClassifier)
gen_uml_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=uml_StructuredClassifier)
gen_uml_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=uml_ConnectionPointReference)
gen_uml_Pseudostate_Vertex = Generalization(general=Vertex, specific=uml_Pseudostate)
gen_uml_Extension_Association = Generalization(general=Association, specific=uml_Extension)
gen_uml_ExtensionEnd_Property = Generalization(general=Property_, specific=uml_ExtensionEnd)
gen_uml_Stereotype_Class = Generalization(general=Class_, specific=uml_Stereotype)
gen_uml_Image_Element = Generalization(general=Element, specific=uml_Image)
gen_uml_Connector_Feature = Generalization(general=Feature, specific=uml_Connector)
gen_uml_DataType_Classifier = Generalization(general=Classifier, specific=uml_DataType)
gen_uml_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml_OperationTemplateParameter)
gen_uml_StructuralFeature_Feature = Generalization(general=Feature, specific=uml_StructuralFeature)
gen_uml_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=uml_StructuralFeature)
gen_uml_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_StructuralFeature)
gen_uml_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml_ConnectableElementTemplateParameter)
gen_uml_Profile_Package = Generalization(general=Package, specific=uml_Profile)
gen_uml_Model_Package = Generalization(general=Package, specific=uml_Model)
gen_uml_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=uml_ParameterSet)
gen_uml_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_UseCase)
gen_uml_Include_NamedElement = Generalization(general=NamedElement, specific=uml_Include)
gen_uml_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Include)
gen_uml_Extend_NamedElement = Generalization(general=NamedElement, specific=uml_Extend)
gen_uml_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Extend)
gen_uml_CollaborationUse_NamedElement = Generalization(general=NamedElement, specific=uml_CollaborationUse)
gen_uml_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_Collaboration)
gen_uml_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml_Collaboration)
gen_uml_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml_ClassifierTemplateParameter)
gen_uml_StringExpression_Expression = Generalization(general=Expression, specific=uml_StringExpression)
gen_uml_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_StringExpression)
gen_uml_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_Expression)
gen_uml_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_ExtensionPoint)
gen_uml_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_RedefinableTemplateSignature)
gen_uml_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=uml_RedefinableTemplateSignature)
gen_uml_Enumeration_DataType = Generalization(general=DataType, specific=uml_Enumeration)
gen_uml_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=uml_EnumerationLiteral)
gen_uml_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml_InstanceSpecification)
gen_uml_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml_InstanceSpecification)
gen_uml_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=uml_InstanceSpecification)
gen_uml_Slot_Element = Generalization(general=Element, specific=uml_Slot)
gen_uml_Usage_Dependency = Generalization(general=Dependency, specific=uml_Usage)
gen_uml_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_PackageMerge)
gen_uml_ProfileApplication_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_ProfileApplication)
gen_uml_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml_LiteralBoolean)
gen_uml_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml_LiteralNull)
gen_uml_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_InstanceValue)
gen_uml_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml_LiteralUnlimitedNatural)
gen_uml_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=uml_OpaqueBehavior)
gen_uml_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=uml_FunctionBehavior)
gen_uml_OpaqueAction_Action = Generalization(general=Action, specific=uml_OpaqueAction)
gen_uml_PrimitiveType_DataType = Generalization(general=DataType, specific=uml_PrimitiveType)
gen_uml_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_LiteralSpecification)
gen_uml_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml_LiteralInteger)
gen_uml_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml_LiteralString)
gen_uml_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ExecutableNode)
gen_uml_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_ActivityNode)
gen_uml_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=uml_Action)
gen_uml_ActivityGroup_Element = Generalization(general=Element, specific=uml_ActivityGroup)
gen_uml_Activity_Behavior = Generalization(general=Behavior, specific=uml_Activity)
gen_uml_StructuredActivityNode_Action = Generalization(general=Action, specific=uml_StructuredActivityNode)
gen_uml_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=uml_StructuredActivityNode)
gen_uml_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=uml_StructuredActivityNode)
gen_uml_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=uml_Variable)
gen_uml_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_Variable)
gen_uml_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_ActivityEdge)
gen_uml_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=uml_ActivityPartition)
gen_uml_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=uml_InterruptibleActivityRegion)
gen_uml_ExceptionHandler_Element = Generalization(general=Element, specific=uml_ExceptionHandler)
gen_uml_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=uml_ActivityPartition)
gen_uml_OutputPin_Pin = Generalization(general=Pin, specific=uml_OutputPin)
gen_uml_Pin_ObjectNode = Generalization(general=ObjectNode, specific=uml_Pin)
gen_uml_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_Pin)
gen_uml_InputPin_Pin = Generalization(general=Pin, specific=uml_InputPin)
gen_uml_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=uml_CallAction)
gen_uml_InvocationAction_Action = Generalization(general=Action, specific=uml_InvocationAction)
gen_uml_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ObjectNode)
gen_uml_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=uml_ObjectNode)
gen_uml_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml_SequenceNode)
gen_uml_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=uml_ControlNode)
gen_uml_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml_ControlFlow)
gen_uml_InitialNode_ControlNode = Generalization(general=ControlNode, specific=uml_InitialNode)
gen_uml_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=uml_ActivityParameterNode)
gen_uml_ValuePin_InputPin = Generalization(general=InputPin, specific=uml_ValuePin)
gen_uml_Message_NamedElement = Generalization(general=NamedElement, specific=uml_Message)
gen_uml_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=uml_SendSignalAction)
gen_uml_CallOperationAction_CallAction = Generalization(general=CallAction, specific=uml_CallOperationAction)
gen_uml_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=uml_CallBehaviorAction)
gen_uml_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=uml_MessageEnd)
gen_uml_Interaction_Behavior = Generalization(general=Behavior, specific=uml_Interaction)
gen_uml_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_Interaction)
gen_uml_Lifeline_NamedElement = Generalization(general=NamedElement, specific=uml_Lifeline)
gen_uml_PartDecomposition_InteractionUse = Generalization(general=InteractionUse, specific=uml_PartDecomposition)
gen_uml_InteractionUse_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_InteractionUse)
gen_uml_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=uml_InteractionFragment)
gen_uml_InteractionOperand_Namespace = Generalization(general=Namespace, specific=uml_InteractionOperand)
gen_uml_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_InteractionOperand)
gen_uml_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=uml_InteractionConstraint)
gen_uml_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_ExecutionSpecification)
gen_uml_Gate_MessageEnd = Generalization(general=MessageEnd, specific=uml_Gate)
gen_uml_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=uml_GeneralOrdering)
gen_uml_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_OccurrenceSpecification)
gen_uml_CreationEvent_Event = Generalization(general=Event, specific=uml_CreationEvent)
gen_uml_DestructionEvent_Event = Generalization(general=Event, specific=uml_DestructionEvent)
gen_uml_SendOperationEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_SendOperationEvent)
gen_uml_MessageEvent_Event = Generalization(general=Event, specific=uml_MessageEvent)
gen_uml_SendSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_SendSignalEvent)
gen_uml_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=uml_MessageOccurrenceSpecification)
gen_uml_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=uml_MessageOccurrenceSpecification)
gen_uml_ExecutionOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=uml_ExecutionOccurrenceSpecification)
gen_uml_ReceiveOperationEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_ReceiveOperationEvent)
gen_uml_ReceiveSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_ReceiveSignalEvent)
gen_uml_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_StateInvariant)
gen_uml_ActionExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=uml_ActionExecutionSpecification)
gen_uml_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=uml_BehaviorExecutionSpecification)
gen_uml_ExecutionEvent_Event = Generalization(general=Event, specific=uml_ExecutionEvent)
gen_uml_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=uml_FlowFinalNode)
gen_uml_FinalNode_ControlNode = Generalization(general=ControlNode, specific=uml_FinalNode)
gen_uml_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=uml_CentralBufferNode)
gen_uml_MergeNode_ControlNode = Generalization(general=ControlNode, specific=uml_MergeNode)
gen_uml_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=uml_DecisionNode)
gen_uml_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml_ObjectFlow)
gen_uml_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=uml_ActivityFinalNode)
gen_uml_ComponentRealization_Realization = Generalization(general=Realization, specific=uml_ComponentRealization)
gen_uml_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_Actor)
gen_uml_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_CallEvent)
gen_uml_ChangeEvent_Event = Generalization(general=Event, specific=uml_ChangeEvent)
gen_uml_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_SignalEvent)
gen_uml_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml_AnyReceiveEvent)
gen_uml_ForkNode_ControlNode = Generalization(general=ControlNode, specific=uml_ForkNode)
gen_uml_Node_Class = Generalization(general=Class_, specific=uml_Node)
gen_uml_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml_Node)
gen_uml_CommunicationPath_Association = Generalization(general=Association, specific=uml_CommunicationPath)
gen_uml_Device_Node = Generalization(general=Node, specific=uml_Device)
gen_uml_ExecutionEnvironment_Node = Generalization(general=Node, specific=uml_ExecutionEnvironment)
gen_uml_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_CombinedFragment)
gen_uml_Component_Class = Generalization(general=Class_, specific=uml_Component)
gen_uml_CreateObjectAction_Action = Generalization(general=Action, specific=uml_CreateObjectAction)
gen_uml_DestroyObjectAction_Action = Generalization(general=Action, specific=uml_DestroyObjectAction)
gen_uml_TestIdentityAction_Action = Generalization(general=Action, specific=uml_TestIdentityAction)
gen_uml_ReadSelfAction_Action = Generalization(general=Action, specific=uml_ReadSelfAction)
gen_uml_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=uml_Continuation)
gen_uml_ConsiderIgnoreFragment_CombinedFragment = Generalization(general=CombinedFragment, specific=uml_ConsiderIgnoreFragment)
gen_uml_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml_ClearStructuralFeatureAction)
gen_uml_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=uml_RemoveStructuralFeatureValueAction)
gen_uml_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=uml_AddStructuralFeatureValueAction)
gen_uml_LinkAction_Action = Generalization(general=Action, specific=uml_LinkAction)
gen_uml_StructuralFeatureAction_Action = Generalization(general=Action, specific=uml_StructuralFeatureAction)
gen_uml_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml_ReadStructuralFeatureAction)
gen_uml_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml_WriteStructuralFeatureAction)
gen_uml_QualifierValue_Element = Generalization(general=Element, specific=uml_QualifierValue)
gen_uml_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=uml_ReadLinkAction)
gen_uml_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=uml_LinkEndCreationData)
gen_uml_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=uml_CreateLinkAction)
gen_uml_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=uml_WriteLinkAction)
gen_uml_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=uml_DestroyLinkAction)
gen_uml_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=uml_LinkEndDestructionData)
gen_uml_LinkEndData_Element = Generalization(general=Element, specific=uml_LinkEndData)
gen_uml_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=uml_SendObjectAction)
gen_uml_ValueSpecificationAction_Action = Generalization(general=Action, specific=uml_ValueSpecificationAction)
gen_uml_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_TimeExpression)
gen_uml_ClearAssociationAction_Action = Generalization(general=Action, specific=uml_ClearAssociationAction)
gen_uml_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=uml_BroadcastSignalAction)
gen_uml_DurationInterval_Interval = Generalization(general=Interval, specific=uml_DurationInterval)
gen_uml_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_Interval)
gen_uml_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml_ReadVariableAction)
gen_uml_Observation_PackageableElement = Generalization(general=PackageableElement, specific=uml_Observation)
gen_uml_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=uml_TimeConstraint)
gen_uml_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=uml_Duration)
gen_uml_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=uml_IntervalConstraint)
gen_uml_TimeInterval_Interval = Generalization(general=Interval, specific=uml_TimeInterval)
gen_uml_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=uml_DurationConstraint)
gen_uml_TimeObservation_Observation = Generalization(general=Observation, specific=uml_TimeObservation)
gen_uml_DurationObservation_Observation = Generalization(general=Observation, specific=uml_DurationObservation)
gen_uml_FinalState_State = Generalization(general=State, specific=uml_FinalState)
gen_uml_TimeEvent_Event = Generalization(general=Event, specific=uml_TimeEvent)
gen_uml_VariableAction_Action = Generalization(general=Action, specific=uml_VariableAction)
gen_uml_ActionInputPin_InputPin = Generalization(general=InputPin, specific=uml_ActionInputPin)
gen_uml_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml_WriteVariableAction)
gen_uml_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml_ClearVariableAction)
gen_uml_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=uml_AddVariableValueAction)
gen_uml_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=uml_RemoveVariableValueAction)
gen_uml_RaiseExceptionAction_Action = Generalization(general=Action, specific=uml_RaiseExceptionAction)
gen_uml_ReclassifyObjectAction_Action = Generalization(general=Action, specific=uml_ReclassifyObjectAction)
gen_uml_InformationItem_Classifier = Generalization(general=Classifier, specific=uml_InformationItem)
gen_uml_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=uml_InformationFlow)
gen_uml_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_InformationFlow)
gen_uml_ReadExtentAction_Action = Generalization(general=Action, specific=uml_ReadExtentAction)
gen_uml_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=uml_ReadIsClassifiedObjectAction)
gen_uml_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=uml_StartClassifierBehaviorAction)
gen_uml_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=uml_ReadLinkObjectEndAction)
gen_uml_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=uml_ReadLinkObjectEndQualifierAction)
gen_uml_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=uml_CreateLinkObjectAction)
gen_uml_AcceptEventAction_Action = Generalization(general=Action, specific=uml_AcceptEventAction)
gen_uml_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=uml_AcceptCallAction)
gen_uml_ReplyAction_Action = Generalization(general=Action, specific=uml_ReplyAction)
gen_uml_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=uml_DataStoreNode)
gen_uml_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml_ConditionalNode)
gen_uml_UnmarshallAction_Action = Generalization(general=Action, specific=uml_UnmarshallAction)
gen_uml_ReduceAction_Action = Generalization(general=Action, specific=uml_ReduceAction)
gen_uml_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=uml_StartObjectBehaviorAction)
gen_uml_JoinNode_ControlNode = Generalization(general=ControlNode, specific=uml_JoinNode)
gen_uml_Clause_Element = Generalization(general=Element, specific=uml_Clause)
gen_uml_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml_LoopNode)
gen_uml_ProtocolTransition_Transition = Generalization(general=Transition, specific=uml_ProtocolTransition)
gen_uml_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=uml_ExpansionNode)
gen_uml_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml_ExpansionRegion)
gen_uml_AssociationClass_Class = Generalization(general=Class_, specific=uml_AssociationClass)
gen_uml_AssociationClass_Association = Generalization(general=Association, specific=uml_AssociationClass)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Comment, Element, TemplateableElement, uml_Type, uml_PackageMerge, uml_PackageableElement, uml_ProfileApplication, NamedElement, ParameterableElement, uml_NamedElement, uml_Element, EModelElement, uml_Package, Namespace, PackageableElement, DirectedRelationship, uml_DirectedRelationship, Relationship, uml_Relationship, uml_ElementImport, uml_PackageImport, uml_Dependency, uml_Namespace, uml_StringExpression, uml_ValueSpecification, TypedElement, uml_TypedElement, uml_Constraint, uml_Classifier, RedefinableElement, Type, uml_Generalization, uml_GeneralizationSet, uml_Feature, uml_Substitution, uml_Association, Classifier, uml_Property, uml_CollaborationUse, uml_UseCase, uml_RedefinableElement, uml_TemplateableElement, uml_TemplateBinding, uml_TemplateSignature, uml_TemplateParameterSubstitution, uml_ParameterableElement, uml_TemplateParameter, uml_Realization, Abstraction, uml_Abstraction, Dependency, uml_OpaqueExpression, ValueSpecification, Realization, uml_Operation, uml_MultiplicityElement, uml_Parameter, uml_Behavior, ConnectableElement, MultiplicityElement, uml_ParameterSet, uml_ConnectableElement, uml_ConnectorEnd, uml_DataType, StructuralFeature, DeploymentTarget, uml_Class, uml_DeploymentTarget, uml_Deployment, Artifact, uml_Artifact, DeployedArtifact, uml_DeployedArtifact, uml_DeploymentSpecification, BehavioralFeature, uml_Interface, uml_Manifestation, uml_BehavioralFeature, Class_, uml_BehavioredClassifier, Feature, EncapsulatedClassifier, BehavioredClassifier, uml_InterfaceRealization, uml_Trigger, uml_Reception, uml_Extension, uml_ProtocolStateMachine, uml_Signal, StateMachine, uml_ProtocolConformance, uml_Transition, uml_StateMachine, Behavior, uml_Region, uml_State, uml_Pseudostate, uml_Vertex, uml_Event, uml_Port, Property_, uml_ConnectionPointReference, Vertex, uml_EncapsulatedClassifier, StructuredClassifier, uml_StructuredClassifier, Association, uml_ExtensionEnd, uml_Stereotype, uml_Image, uml_Connector, uml_OperationTemplateParameter, TemplateParameter, uml_StructuralFeature, uml_ConnectableElementTemplateParameter, uml_Profile, Package, uml_Model, uml_Include, uml_Extend, uml_ExtensionPoint, uml_Collaboration, uml_ClassifierTemplateParameter, Expression, uml_Expression, uml_RedefinableTemplateSignature, TemplateSignature, uml_Enumeration, DataType, uml_EnumerationLiteral, InstanceSpecification, uml_InstanceSpecification, uml_Slot, uml_Usage, uml_LiteralBoolean, uml_LiteralNull, uml_InstanceValue, uml_LiteralUnlimitedNatural, uml_OpaqueBehavior, uml_FunctionBehavior, OpaqueBehavior, uml_OpaqueAction, Action, uml_InputPin, uml_OutputPin, uml_PrimitiveType, uml_LiteralSpecification, uml_LiteralInteger, LiteralSpecification, uml_LiteralString, uml_ExecutableNode, ActivityNode, uml_ExceptionHandler, uml_ActivityNode, uml_StructuredActivityNode, uml_Activity, uml_ActivityEdge, uml_ActivityPartition, uml_InterruptibleActivityRegion, uml_Action, ExecutableNode, uml_ActivityGroup, ActivityGroup, uml_Variable, uml_ObjectNode, Pin, uml_Pin, ObjectNode, uml_CallAction, InvocationAction, uml_InvocationAction, uml_SequenceNode, StructuredActivityNode, uml_ControlNode, uml_ControlFlow, ActivityEdge, uml_InitialNode, ControlNode, uml_ActivityParameterNode, uml_ValuePin, InputPin, uml_Message, uml_SendSignalAction, uml_CallOperationAction, CallAction, uml_CallBehaviorAction, InteractionFragment, uml_Lifeline, uml_InteractionFragment, uml_Gate, uml_MessageEnd, uml_Interaction, uml_PartDecomposition, InteractionUse, uml_InteractionUse, uml_GeneralOrdering, uml_InteractionOperand, uml_InteractionConstraint, Constraint, uml_ExecutionSpecification, MessageEnd, uml_OccurrenceSpecification, uml_CreationEvent, uml_DestructionEvent, uml_SendOperationEvent, MessageEvent, uml_MessageEvent, uml_SendSignalEvent, uml_MessageOccurrenceSpecification, OccurrenceSpecification, uml_ExecutionOccurrenceSpecification, uml_ReceiveOperationEvent, uml_ReceiveSignalEvent, uml_StateInvariant, uml_ActionExecutionSpecification, ExecutionSpecification, uml_BehaviorExecutionSpecification, uml_ExecutionEvent, Event, uml_FlowFinalNode, FinalNode, uml_FinalNode, uml_CentralBufferNode, uml_MergeNode, uml_DecisionNode, uml_ObjectFlow, uml_ActivityFinalNode, uml_ComponentRealization, uml_Component, uml_Actor, uml_CallEvent, uml_ChangeEvent, uml_SignalEvent, uml_AnyReceiveEvent, uml_ForkNode, uml_Node, uml_CommunicationPath, uml_Device, Node, uml_ExecutionEnvironment, uml_CombinedFragment, uml_DestroyObjectAction, uml_TestIdentityAction, uml_ReadSelfAction, uml_Continuation, uml_ConsiderIgnoreFragment, CombinedFragment, uml_CreateObjectAction, uml_ClearStructuralFeatureAction, uml_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, uml_AddStructuralFeatureValueAction, uml_LinkAction, uml_LinkEndData, uml_StructuralFeatureAction, uml_ReadStructuralFeatureAction, StructuralFeatureAction, uml_WriteStructuralFeatureAction, uml_ReadLinkAction, LinkAction, uml_LinkEndCreationData, LinkEndData, uml_CreateLinkAction, WriteLinkAction, uml_WriteLinkAction, uml_DestroyLinkAction, uml_LinkEndDestructionData, uml_QualifierValue, uml_SendObjectAction, uml_ValueSpecificationAction, uml_TimeExpression, uml_ClearAssociationAction, uml_BroadcastSignalAction, uml_DurationInterval, Interval, uml_Interval, uml_ReadVariableAction, VariableAction, uml_Observation, uml_TimeConstraint, IntervalConstraint, uml_Duration, uml_IntervalConstraint, uml_TimeInterval, uml_DurationConstraint, uml_TimeObservation, Observation, uml_DurationObservation, uml_FinalState, State, uml_TimeEvent, uml_VariableAction, uml_ActionInputPin, uml_WriteVariableAction, uml_ClearVariableAction, uml_AddVariableValueAction, WriteVariableAction, uml_RemoveVariableValueAction, uml_RaiseExceptionAction, uml_ReclassifyObjectAction, uml_InformationItem, uml_InformationFlow, uml_ReadExtentAction, uml_ReadLinkObjectEndQualifierAction, uml_ReadIsClassifiedObjectAction, uml_StartClassifierBehaviorAction, uml_ReadLinkObjectEndAction, uml_CreateLinkObjectAction, CreateLinkAction, uml_AcceptEventAction, uml_AcceptCallAction, AcceptEventAction, uml_ReplyAction, uml_DataStoreNode, CentralBufferNode, uml_ConditionalNode, uml_UnmarshallAction, uml_ReduceAction, uml_StartObjectBehaviorAction, uml_JoinNode, uml_Clause, uml_LoopNode, uml_ProtocolTransition, Transition, uml_ExpansionNode, uml_ExpansionRegion, uml_AssociationClass, VisibilityKind, TransitionKind, PseudostateKind, ConnectorKind, CallConcurrencyKind, AggregationKind, ParameterDirectionKind, ParameterEffectKind, ObjectNodeOrderingKind, MessageKind, MessageSort, InteractionOperatorKind, ExpansionKind},
    associations={ownedType9, packageMerge10, packagedElement11, nestedPackage13, nestingPackage15, profileApplication17, annotatedElement0, ownedElement2, owner4, ownedComment6, supplier21, client23, source24, target26, relatedElement29, elementImport31, packageImport32, clientDependency18, namespace19, nameExpression20, importedElement42, importingNamespace44, importedPackage46, importingNamespace48, constrainedElement50, specification52, context54, ownedRule34, member35, importedMember37, ownedMember40, navigableOwnedEnd64, generalization66, powertypeExtent67, feature68, inheritedMember69, redefinedClassifier72, general75, substitution77, type56, package57, ownedEnd59, memberEnd60, endType62, representation81, collaborationUse83, ownedUseCase86, useCase88, attribute78, templateBinding94, ownedTemplateSignature95, signature96, parameterSubstitution97, redefinedElement90, redefinitionContext91, template103, signature105, parameteredElement107, ownedParameteredElement108, default110, boundElement98, parameter100, ownedParameter102, templateParameter117, formal119, actual121, ownedActual124, templateBinding127, ownedDefault112, owningTemplateParameter115, specific133, powertype135, generalization137, general129, generalizationSet131, substitutingClassifier143, mapping145, featuringClassifier139, contract141, operation151, defaultValue153, result146, behavior148, parameterSet150, upperValue156, lowerValue158, end161, definingEnd162, class171, datatype173, redefinedProperty175, role165, partWithPort168, subsettedProperty185, association187, qualifier190, associationEnd193, owningAssociation177, defaultValue178, opposite182, configuration199, location200, deployment202, deployment195, deployedElement196, deployedArtifact198, ownedAttribute211, utilizedElement214, interface217, class218, nestedArtifact205, manifestation206, ownedOperation208, postcondition223, redefinedOperation227, datatype229, bodyCondition232, type235, precondition220, raisedException241, ownedParameterSet244, redefinedBehavior247, ownedParameter249, ownedParameter238, method240, specification263, nestedClassifier264, ownedOperation267, superClass269, context252, precondition254, postcondition257, ownedParameterSet260, ownedBehavior274, classifierBehavior277, interfaceRealization280, ownedTrigger281, contract283, ownedReception271, extension273, nestedClassifier290, redefinedInterface294, ownedReception296, protocol299, signal301, ownedAttribute303, conformance306, implementingClassifier284, ownedAttribute285, ownedOperation288, subvertex313, transition314, state316, extendedRegion319, stateMachine320, outgoing322, incoming323, container326, region307, submachineState308, connectionPoint309, extendedStateMachine312, effect342, trigger345, event348, port350, required352, redefinedPort356, container328, source330, target333, redefinedTransition337, guard339, submachine364, connection366, connectionPoint367, redefinedState371, stateInvariant372, entry375, exit378, doActivity381, deferrableTrigger384, provided358, protocol361, stateMachine396, state398, generalMachine401, specificMachine403, ownedPort404, region387, entry390, exit391, state394, redefinedConnector420, end422, contract425, metaclass428, icon430, ownedAttribute406, part408, role411, ownedConnector414, type416, parameter439, condition440, ownedAttribute443, ownedOperation445, ownedStereotype431, metaclassReference433, metamodelReference436, collaborationRole453, include456, extend457, extensionPoint459, subject460, addition463, includingCase465, extendedCase467, type448, roleBinding450, inheritedParameter480, classifier483, constrainingClassifier486, subExpression489, owningExpression491, operand493, condition469, extensionLocation472, extension474, useCase476, extendedSignature479, ownedLiteral503, enumeration504, classifier505, slot507, specification508, mergedPackage495, receivingPackage497, appliedProfile499, applyingPackage501, instance516, inputValue518, definingFeature511, value512, owningInstance515, localPrecondition529, localPostcondition532, handler535, inStructuredNode536, activity537, outgoing539, incoming540, inPartition542, inInterruptibleRegion544, outputValue519, output521, input523, context526, edge550, node552, subgroup555, superGroup558, inActivity560, containedEdge562, containedNode564, inGroup546, redefinedNode548, variable549, group577, scope579, activityScope581, source584, target586, redefinedEdge589, inPartition590, guard592, structuredNode567, variable568, node570, edge572, partition575, interrupts598, inStructuredNode600, inGroup603, activity605, weight595, superPartition614, represents616, edge619, node622, interruptingEdge624, handlerBody626, exceptionInput627, node608, subpartition611, selection639, result642, argument644, onPort646, exceptionType629, protectedNode632, upperBound633, inState636, executableNode661, parameter663, value665, target649, signal651, operation654, target656, behavior659, message681, lifeline684, fragment685, action686, formalGate688, receiveEvent667, sendEvent668, connector671, interaction674, argument675, signature678, represents699, interaction701, selector703, decomposedAs706, coveredBy708, refersTo710, actualGate712, message690, covered692, generalOrdering694, enclosingInteraction695, enclosingOperand697, event722, toAfter724, guard726, fragment727, minint729, maxint732, start735, finish737, argument715, before718, after719, toBefore721, operation746, signal748, execution750, operation752, signal754, invariant740, action742, behavior744, decisionInput762, decisionInputFlow764, transformation766, selection769, operation756, changeExpression758, signal760, packagedElement780, realization783, nestedNode785, operand786, cfragmentGate788, abstraction772, realizingClassifier773, required775, provided777, classifier793, result795, target798, first800, second802, result805, message791, value817, result819, result822, removeAt824, insertAt826, endData828, result808, structuralFeature810, object812, result815, qualifier840, value843, result846, insertAt848, destroyAt850, inputValue829, value832, end835, qualifier838, target859, request861, value864, result866, object852, association854, signal857, min878, expr869, result890, max880, observation871, expr873, observation875, event883, event885, when887, variable889, fromAction900, value892, insertAt894, removeAt896, exception898, classifier926, represented902, realization904, conveyed906, informationSource909, informationTarget912, realizingActivityEdge915, realizingConnector918, realizingMessage921, result924, end949, result952, oldClassifier929, newClassifier931, object934, classifier937, result939, object942, object945, object947, returnInformation974, replyValue977, object955, result957, qualifier960, result963, result965, trigger967, returnInformation970, replyToCall972, joinSpec998, result980, unmarshallType982, object985, reducer988, result990, collection993, object996, setupPart1023, decider1026, clause1000, result1001, test1004, body1007, predecessorClause1011, successorClause1013, decider1015, bodyOutput1018, bodyPart1021, postCondition1050, referred1052, test1029, result1032, loopVariable1035, bodyOutput1038, loopVariableInput1041, regionAsOutput1044, regionAsInput1045, inputElement1047, outputElement1048, preCondition1055},
    generalizations={gen_uml_Comment_Element, gen_uml_Package_TemplateableElement, gen_uml_PackageableElement_NamedElement, gen_uml_PackageableElement_ParameterableElement, gen_uml_NamedElement_Element, gen_uml_Element_EModelElement, gen_uml_Package_Namespace, gen_uml_Package_PackageableElement, gen_uml_Dependency_DirectedRelationship, gen_uml_DirectedRelationship_Relationship, gen_uml_Relationship_Element, gen_uml_Namespace_NamedElement, gen_uml_Dependency_PackageableElement, gen_uml_PackageImport_DirectedRelationship, gen_uml_Constraint_PackageableElement, gen_uml_ValueSpecification_PackageableElement, gen_uml_ValueSpecification_TypedElement, gen_uml_TypedElement_NamedElement, gen_uml_ElementImport_DirectedRelationship, gen_uml_Classifier_Namespace, gen_uml_Classifier_RedefinableElement, gen_uml_Classifier_Type, gen_uml_Classifier_TemplateableElement, gen_uml_Type_PackageableElement, gen_uml_Association_Classifier, gen_uml_Association_Relationship, gen_uml_RedefinableElement_NamedElement, gen_uml_TemplateableElement_Element, gen_uml_TemplateBinding_DirectedRelationship, gen_uml_TemplateParameter_Element, gen_uml_TemplateSignature_Element, gen_uml_TemplateParameterSubstitution_Element, gen_uml_ParameterableElement_Element, gen_uml_GeneralizationSet_PackageableElement, gen_uml_Feature_RedefinableElement, gen_uml_Generalization_DirectedRelationship, gen_uml_Realization_Abstraction, gen_uml_Abstraction_Dependency, gen_uml_OpaqueExpression_ValueSpecification, gen_uml_Substitution_Realization, gen_uml_MultiplicityElement_Element, gen_uml_Parameter_ConnectableElement, gen_uml_Parameter_MultiplicityElement, gen_uml_ConnectableElement_TypedElement, gen_uml_ConnectableElement_ParameterableElement, gen_uml_ConnectorEnd_MultiplicityElement, gen_uml_Property_StructuralFeature, gen_uml_Property_ConnectableElement, gen_uml_Property_DeploymentTarget, gen_uml_DeploymentTarget_NamedElement, gen_uml_DeployedArtifact_NamedElement, gen_uml_DeploymentSpecification_Artifact, gen_uml_Artifact_Classifier, gen_uml_Artifact_DeployedArtifact, gen_uml_Deployment_Dependency, gen_uml_Manifestation_Abstraction, gen_uml_Operation_BehavioralFeature, gen_uml_Operation_ParameterableElement, gen_uml_Operation_TemplateableElement, gen_uml_Behavior_Class, gen_uml_BehavioralFeature_Namespace, gen_uml_BehavioralFeature_Feature, gen_uml_Class_EncapsulatedClassifier, gen_uml_Class_BehavioredClassifier, gen_uml_InterfaceRealization_Realization, gen_uml_BehavioredClassifier_Classifier, gen_uml_Reception_BehavioralFeature, gen_uml_Signal_Classifier, gen_uml_ProtocolStateMachine_StateMachine, gen_uml_Interface_Classifier, gen_uml_Vertex_NamedElement, gen_uml_Transition_Namespace, gen_uml_Transition_RedefinableElement, gen_uml_StateMachine_Behavior, gen_uml_Region_Namespace, gen_uml_Region_RedefinableElement, gen_uml_Trigger_NamedElement, gen_uml_Event_PackageableElement, gen_uml_Port_Property, gen_uml_State_Namespace, gen_uml_State_RedefinableElement, gen_uml_State_Vertex, gen_uml_ProtocolConformance_DirectedRelationship, gen_uml_EncapsulatedClassifier_StructuredClassifier, gen_uml_StructuredClassifier_Classifier, gen_uml_ConnectionPointReference_Vertex, gen_uml_Pseudostate_Vertex, gen_uml_Extension_Association, gen_uml_ExtensionEnd_Property, gen_uml_Stereotype_Class, gen_uml_Image_Element, gen_uml_Connector_Feature, gen_uml_DataType_Classifier, gen_uml_OperationTemplateParameter_TemplateParameter, gen_uml_StructuralFeature_Feature, gen_uml_StructuralFeature_TypedElement, gen_uml_StructuralFeature_MultiplicityElement, gen_uml_ConnectableElementTemplateParameter_TemplateParameter, gen_uml_Profile_Package, gen_uml_Model_Package, gen_uml_ParameterSet_NamedElement, gen_uml_UseCase_BehavioredClassifier, gen_uml_Include_NamedElement, gen_uml_Include_DirectedRelationship, gen_uml_Extend_NamedElement, gen_uml_Extend_DirectedRelationship, gen_uml_CollaborationUse_NamedElement, gen_uml_Collaboration_BehavioredClassifier, gen_uml_Collaboration_StructuredClassifier, gen_uml_ClassifierTemplateParameter_TemplateParameter, gen_uml_StringExpression_Expression, gen_uml_StringExpression_TemplateableElement, gen_uml_Expression_ValueSpecification, gen_uml_ExtensionPoint_RedefinableElement, gen_uml_RedefinableTemplateSignature_RedefinableElement, gen_uml_RedefinableTemplateSignature_TemplateSignature, gen_uml_Enumeration_DataType, gen_uml_EnumerationLiteral_InstanceSpecification, gen_uml_InstanceSpecification_DeploymentTarget, gen_uml_InstanceSpecification_PackageableElement, gen_uml_InstanceSpecification_DeployedArtifact, gen_uml_Slot_Element, gen_uml_Usage_Dependency, gen_uml_PackageMerge_DirectedRelationship, gen_uml_ProfileApplication_DirectedRelationship, gen_uml_LiteralBoolean_LiteralSpecification, gen_uml_LiteralNull_LiteralSpecification, gen_uml_InstanceValue_ValueSpecification, gen_uml_LiteralUnlimitedNatural_LiteralSpecification, gen_uml_OpaqueBehavior_Behavior, gen_uml_FunctionBehavior_OpaqueBehavior, gen_uml_OpaqueAction_Action, gen_uml_PrimitiveType_DataType, gen_uml_LiteralSpecification_ValueSpecification, gen_uml_LiteralInteger_LiteralSpecification, gen_uml_LiteralString_LiteralSpecification, gen_uml_ExecutableNode_ActivityNode, gen_uml_ActivityNode_RedefinableElement, gen_uml_Action_ExecutableNode, gen_uml_ActivityGroup_Element, gen_uml_Activity_Behavior, gen_uml_StructuredActivityNode_Action, gen_uml_StructuredActivityNode_Namespace, gen_uml_StructuredActivityNode_ActivityGroup, gen_uml_Variable_ConnectableElement, gen_uml_Variable_MultiplicityElement, gen_uml_ActivityEdge_RedefinableElement, gen_uml_ActivityPartition_NamedElement, gen_uml_InterruptibleActivityRegion_ActivityGroup, gen_uml_ExceptionHandler_Element, gen_uml_ActivityPartition_ActivityGroup, gen_uml_OutputPin_Pin, gen_uml_Pin_ObjectNode, gen_uml_Pin_MultiplicityElement, gen_uml_InputPin_Pin, gen_uml_CallAction_InvocationAction, gen_uml_InvocationAction_Action, gen_uml_ObjectNode_ActivityNode, gen_uml_ObjectNode_TypedElement, gen_uml_SequenceNode_StructuredActivityNode, gen_uml_ControlNode_ActivityNode, gen_uml_ControlFlow_ActivityEdge, gen_uml_InitialNode_ControlNode, gen_uml_ActivityParameterNode_ObjectNode, gen_uml_ValuePin_InputPin, gen_uml_Message_NamedElement, gen_uml_SendSignalAction_InvocationAction, gen_uml_CallOperationAction_CallAction, gen_uml_CallBehaviorAction_CallAction, gen_uml_MessageEnd_NamedElement, gen_uml_Interaction_Behavior, gen_uml_Interaction_InteractionFragment, gen_uml_Lifeline_NamedElement, gen_uml_PartDecomposition_InteractionUse, gen_uml_InteractionUse_InteractionFragment, gen_uml_InteractionFragment_NamedElement, gen_uml_InteractionOperand_Namespace, gen_uml_InteractionOperand_InteractionFragment, gen_uml_InteractionConstraint_Constraint, gen_uml_ExecutionSpecification_InteractionFragment, gen_uml_Gate_MessageEnd, gen_uml_GeneralOrdering_NamedElement, gen_uml_OccurrenceSpecification_InteractionFragment, gen_uml_CreationEvent_Event, gen_uml_DestructionEvent_Event, gen_uml_SendOperationEvent_MessageEvent, gen_uml_MessageEvent_Event, gen_uml_SendSignalEvent_MessageEvent, gen_uml_MessageOccurrenceSpecification_OccurrenceSpecification, gen_uml_MessageOccurrenceSpecification_MessageEnd, gen_uml_ExecutionOccurrenceSpecification_OccurrenceSpecification, gen_uml_ReceiveOperationEvent_MessageEvent, gen_uml_ReceiveSignalEvent_MessageEvent, gen_uml_StateInvariant_InteractionFragment, gen_uml_ActionExecutionSpecification_ExecutionSpecification, gen_uml_BehaviorExecutionSpecification_ExecutionSpecification, gen_uml_ExecutionEvent_Event, gen_uml_FlowFinalNode_FinalNode, gen_uml_FinalNode_ControlNode, gen_uml_CentralBufferNode_ObjectNode, gen_uml_MergeNode_ControlNode, gen_uml_DecisionNode_ControlNode, gen_uml_ObjectFlow_ActivityEdge, gen_uml_ActivityFinalNode_FinalNode, gen_uml_ComponentRealization_Realization, gen_uml_Actor_BehavioredClassifier, gen_uml_CallEvent_MessageEvent, gen_uml_ChangeEvent_Event, gen_uml_SignalEvent_MessageEvent, gen_uml_AnyReceiveEvent_MessageEvent, gen_uml_ForkNode_ControlNode, gen_uml_Node_Class, gen_uml_Node_DeploymentTarget, gen_uml_CommunicationPath_Association, gen_uml_Device_Node, gen_uml_ExecutionEnvironment_Node, gen_uml_CombinedFragment_InteractionFragment, gen_uml_Component_Class, gen_uml_CreateObjectAction_Action, gen_uml_DestroyObjectAction_Action, gen_uml_TestIdentityAction_Action, gen_uml_ReadSelfAction_Action, gen_uml_Continuation_InteractionFragment, gen_uml_ConsiderIgnoreFragment_CombinedFragment, gen_uml_ClearStructuralFeatureAction_StructuralFeatureAction, gen_uml_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_uml_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_uml_LinkAction_Action, gen_uml_StructuralFeatureAction_Action, gen_uml_ReadStructuralFeatureAction_StructuralFeatureAction, gen_uml_WriteStructuralFeatureAction_StructuralFeatureAction, gen_uml_QualifierValue_Element, gen_uml_ReadLinkAction_LinkAction, gen_uml_LinkEndCreationData_LinkEndData, gen_uml_CreateLinkAction_WriteLinkAction, gen_uml_WriteLinkAction_LinkAction, gen_uml_DestroyLinkAction_WriteLinkAction, gen_uml_LinkEndDestructionData_LinkEndData, gen_uml_LinkEndData_Element, gen_uml_SendObjectAction_InvocationAction, gen_uml_ValueSpecificationAction_Action, gen_uml_TimeExpression_ValueSpecification, gen_uml_ClearAssociationAction_Action, gen_uml_BroadcastSignalAction_InvocationAction, gen_uml_DurationInterval_Interval, gen_uml_Interval_ValueSpecification, gen_uml_ReadVariableAction_VariableAction, gen_uml_Observation_PackageableElement, gen_uml_TimeConstraint_IntervalConstraint, gen_uml_Duration_ValueSpecification, gen_uml_IntervalConstraint_Constraint, gen_uml_TimeInterval_Interval, gen_uml_DurationConstraint_IntervalConstraint, gen_uml_TimeObservation_Observation, gen_uml_DurationObservation_Observation, gen_uml_FinalState_State, gen_uml_TimeEvent_Event, gen_uml_VariableAction_Action, gen_uml_ActionInputPin_InputPin, gen_uml_WriteVariableAction_VariableAction, gen_uml_ClearVariableAction_VariableAction, gen_uml_AddVariableValueAction_WriteVariableAction, gen_uml_RemoveVariableValueAction_WriteVariableAction, gen_uml_RaiseExceptionAction_Action, gen_uml_ReclassifyObjectAction_Action, gen_uml_InformationItem_Classifier, gen_uml_InformationFlow_PackageableElement, gen_uml_InformationFlow_DirectedRelationship, gen_uml_ReadExtentAction_Action, gen_uml_ReadIsClassifiedObjectAction_Action, gen_uml_StartClassifierBehaviorAction_Action, gen_uml_ReadLinkObjectEndAction_Action, gen_uml_ReadLinkObjectEndQualifierAction_Action, gen_uml_CreateLinkObjectAction_CreateLinkAction, gen_uml_AcceptEventAction_Action, gen_uml_AcceptCallAction_AcceptEventAction, gen_uml_ReplyAction_Action, gen_uml_DataStoreNode_CentralBufferNode, gen_uml_ConditionalNode_StructuredActivityNode, gen_uml_UnmarshallAction_Action, gen_uml_ReduceAction_Action, gen_uml_StartObjectBehaviorAction_CallAction, gen_uml_JoinNode_ControlNode, gen_uml_Clause_Element, gen_uml_LoopNode_StructuredActivityNode, gen_uml_ProtocolTransition_Transition, gen_uml_ExpansionNode_ObjectNode, gen_uml_ExpansionRegion_StructuredActivityNode, gen_uml_AssociationClass_Class, gen_uml_AssociationClass_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)