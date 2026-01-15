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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
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

ConnectorKind: Enumeration = Enumeration(
    name="ConnectorKind",
    literals={
            EnumerationLiteral(name="assembly"),
			EnumerationLiteral(name="delegation")
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

ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
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

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint")
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

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

# Classes
UMLModel_Abstraction = Class(name="UMLModel::Abstraction")
Dependency = Class(name="Dependency")
UMLModel_OpaqueExpression = Class(name="UMLModel::OpaqueExpression")
UMLModel_AcceptCallAction = Class(name="UMLModel::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UMLModel_OutputPin = Class(name="UMLModel::OutputPin")
UMLModel_AcceptEventAction = Class(name="UMLModel::AcceptEventAction")
Action = Class(name="Action")
UMLModel_Trigger = Class(name="UMLModel::Trigger")
UMLModel_Action = Class(name="UMLModel::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
UMLModel_Constraint = Class(name="UMLModel::Constraint")
UMLModel_ActionExecutionSpecification = Class(name="UMLModel::ActionExecutionSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
UMLModel_ActionInputPin = Class(name="UMLModel::ActionInputPin")
InputPin = Class(name="InputPin")
UMLModel_Activity = Class(name="UMLModel::Activity")
Behavior = Class(name="Behavior")
UMLModel_Variable = Class(name="UMLModel::Variable")
UMLModel_ActivityEdge = Class(name="UMLModel::ActivityEdge", is_abstract=True)
UMLModel_ActivityGroup = Class(name="UMLModel::ActivityGroup", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
UMLModel_ValueSpecification = Class(name="UMLModel::ValueSpecification", is_abstract=True)
UMLModel_ActivityFinalNode = Class(name="UMLModel::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
Element = Class(name="Element")
UMLModel_ActivityNode = Class(name="UMLModel::ActivityNode", is_abstract=True)
UMLModel_ActivityParameterNode = Class(name="UMLModel::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
UMLModel_Actor = Class(name="UMLModel::Actor")
BehavioredClassifier = Class(name="BehavioredClassifier")
UMLModel_AddStructuralFeatureValueAction = Class(name="UMLModel::AddStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UMLModel_InputPin = Class(name="UMLModel::InputPin")
UMLModel_AddVariableValueAction = Class(name="UMLModel::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UMLModel_AnyReceiveEvent = Class(name="UMLModel::AnyReceiveEvent")
MessageEvent = Class(name="MessageEvent")
UMLModel_Artifact = Class(name="UMLModel::Artifact")
Classifier = Class(name="Classifier")
DeployedArtifact = Class(name="DeployedArtifact")
UMLModel_Manifestation = Class(name="UMLModel::Manifestation")
UMLModel_Operation = Class(name="UMLModel::Operation")
UMLModel_Property = Class(name="UMLModel::Property")
UMLModel_Association = Class(name="UMLModel::Association")
Relationship = Class(name="Relationship")
UMLModel_ActivityPartition = Class(name="UMLModel::ActivityPartition")
NamedElement = Class(name="NamedElement")
ActivityGroup = Class(name="ActivityGroup")
UMLModel_AssociationClass = Class(name="UMLModel::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
UMLModel_Behavior = Class(name="UMLModel::Behavior", is_abstract=True)
UMLModel_Parameter = Class(name="UMLModel::Parameter")
UMLModel_ParameterSet = Class(name="UMLModel::ParameterSet")
UMLModel_BehaviorExecutionSpecification = Class(name="UMLModel::BehaviorExecutionSpecification")
UMLModel_BehavioralFeature = Class(name="UMLModel::BehavioralFeature", is_abstract=True)
Namespace = Class(name="Namespace")
Feature = Class(name="Feature")
UMLModel_BehavioredClassifier = Class(name="UMLModel::BehavioredClassifier", is_abstract=True)
UMLModel_InterfaceRealization = Class(name="UMLModel::InterfaceRealization")
UMLModel_BroadcastSignalAction = Class(name="UMLModel::BroadcastSignalAction")
InvocationAction = Class(name="InvocationAction")
UMLModel_CallAction = Class(name="UMLModel::CallAction", is_abstract=True)
UMLModel_CallBehaviorAction = Class(name="UMLModel::CallBehaviorAction")
CallAction = Class(name="CallAction")
UMLModel_CallEvent = Class(name="UMLModel::CallEvent")
UMLModel_CallOperationAction = Class(name="UMLModel::CallOperationAction")
UMLModel_ChangeEvent = Class(name="UMLModel::ChangeEvent")
Event = Class(name="Event")
UMLModel_Class = Class(name="UMLModel::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UMLModel_Classifier = Class(name="UMLModel::Classifier", is_abstract=True)
UMLModel_Reception = Class(name="UMLModel::Reception")
Type = Class(name="Type")
TemplateableElement = Class(name="TemplateableElement")
UMLModel_Generalization = Class(name="UMLModel::Generalization")
UMLModel_Substitution = Class(name="UMLModel::Substitution")
UMLModel_UseCase = Class(name="UMLModel::UseCase")
UMLModel_ClassifierTemplateParameter = Class(name="UMLModel::ClassifierTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
UMLModel_Clause = Class(name="UMLModel::Clause")
UMLModel_ClearVariableAction = Class(name="UMLModel::ClearVariableAction")
VariableAction = Class(name="VariableAction")
UMLModel_ClearAssociationAction = Class(name="UMLModel::ClearAssociationAction")
UMLModel_ClearStructuralFeatureAction = Class(name="UMLModel::ClearStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UMLModel_Collaboration = Class(name="UMLModel::Collaboration")
StructuredClassifier = Class(name="StructuredClassifier")
UMLModel_Dependency = Class(name="UMLModel::Dependency")
UMLModel_Comment = Class(name="UMLModel::Comment")
UMLModel_CommunicationPath = Class(name="UMLModel::CommunicationPath")
UMLModel_Component = Class(name="UMLModel::Component")
UMLModel_PackageableElement = Class(name="UMLModel::PackageableElement", is_abstract=True)
UMLModel_ComponentRealization = Class(name="UMLModel::ComponentRealization")
UMLModel_CollaborationUse = Class(name="UMLModel::CollaborationUse")
UMLModel_CombinedFragment = Class(name="UMLModel::CombinedFragment")
InteractionFragment = Class(name="InteractionFragment")
UMLModel_InteractionOperand = Class(name="UMLModel::InteractionOperand")
UMLModel_Gate = Class(name="UMLModel::Gate")
UMLModel_ConditionalNode = Class(name="UMLModel::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
PackageableElement = Class(name="PackageableElement")
UMLModel_ConsiderIgnoreFragment = Class(name="UMLModel::ConsiderIgnoreFragment")
CombinedFragment = Class(name="CombinedFragment")
UMLModel_Continuation = Class(name="UMLModel::Continuation")
UMLModel_ConnectableElement = Class(name="UMLModel::ConnectableElement", is_abstract=True)
TypedElement = Class(name="TypedElement")
ParameterableElement = Class(name="ParameterableElement")
UMLModel_ConnectableElementTemplateParameter = Class(name="UMLModel::ConnectableElementTemplateParameter")
UMLModel_ConnectorEnd = Class(name="UMLModel::ConnectorEnd")
MultiplicityElement = Class(name="MultiplicityElement")
UMLModel_ConnectionPointReference = Class(name="UMLModel::ConnectionPointReference")
Vertex = Class(name="Vertex")
UMLModel_Connector = Class(name="UMLModel::Connector")
Realization = Class(name="Realization")
UMLModel_ControlFlow = Class(name="UMLModel::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
UMLModel_ControlNode = Class(name="UMLModel::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
UMLModel_CreationEvent = Class(name="UMLModel::CreationEvent")
UMLModel_CreateLinkObjectAction = Class(name="UMLModel::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UMLModel_CreateObjectAction = Class(name="UMLModel::CreateObjectAction")
UMLModel_CreateLinkAction = Class(name="UMLModel::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UMLModel_CentralBufferNode = Class(name="UMLModel::CentralBufferNode")
UMLModel_DeployedArtifact = Class(name="UMLModel::DeployedArtifact", is_abstract=True)
Artifact = Class(name="Artifact")
UMLModel_DirectedRelationship = Class(name="UMLModel::DirectedRelationship", is_abstract=True)
UMLModel_Device = Class(name="UMLModel::Device")
Node = Class(name="Node")
UMLModel_DestroyLinkAction = Class(name="UMLModel::DestroyLinkAction")
UMLModel_DestroyObjectAction = Class(name="UMLModel::DestroyObjectAction")
UMLModel_DestructionEvent = Class(name="UMLModel::DestructionEvent")
UMLModel_Duration = Class(name="UMLModel::Duration")
ValueSpecification = Class(name="ValueSpecification")
UMLModel_DataStoreNode = Class(name="UMLModel::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UMLModel_DataType = Class(name="UMLModel::DataType")
UMLModel_DecisionNode = Class(name="UMLModel::DecisionNode")
ControlNode = Class(name="ControlNode")
DirectedRelationship = Class(name="DirectedRelationship")
UMLModel_DeploymentTarget = Class(name="UMLModel::DeploymentTarget", is_abstract=True)
UMLModel_Deployment = Class(name="UMLModel::Deployment")
UMLModel_DeploymentSpecification = Class(name="UMLModel::DeploymentSpecification")
UMLModel_EncapsulatedClassifier = Class(name="UMLModel::EncapsulatedClassifier", is_abstract=True)
UMLModel_Enumeration = Class(name="UMLModel::Enumeration")
DataType = Class(name="DataType")
UMLModel_EnumerationLiteral = Class(name="UMLModel::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
UMLModel_ExceptionHandler = Class(name="UMLModel::ExceptionHandler")
UMLModel_ExecutableNode = Class(name="UMLModel::ExecutableNode", is_abstract=True)
UMLModel_ExecutionEnvironment = Class(name="UMLModel::ExecutionEnvironment")
UMLModel_ExecutionEvent = Class(name="UMLModel::ExecutionEvent")
UMLModel_ExecutionOccurrenceSpecification = Class(name="UMLModel::ExecutionOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
UMLModel_ExecutionSpecification = Class(name="UMLModel::ExecutionSpecification", is_abstract=True)
UMLModel_DurationConstraint = Class(name="UMLModel::DurationConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UMLModel_DurationInterval = Class(name="UMLModel::DurationInterval")
Interval = Class(name="Interval")
UMLModel_DurationObservation = Class(name="UMLModel::DurationObservation")
Observation = Class(name="Observation")
UMLModel_Element = Class(name="UMLModel::Element", is_abstract=True)
UMLBase = Class(name="UMLBase")
UMLModel_ElementImport = Class(name="UMLModel::ElementImport")
UMLModel_ExtensionEnd = Class(name="UMLModel::ExtensionEnd")
Property_ = Class(name="Property")
UMLModel_ExtensionPoint = Class(name="UMLModel::ExtensionPoint")
UMLModel_Expression = Class(name="UMLModel::Expression")
UMLModel_Event = Class(name="UMLModel::Event", is_abstract=True)
UMLModel_Feature = Class(name="UMLModel::Feature", is_abstract=True)
UMLModel_FinalState = Class(name="UMLModel::FinalState")
State = Class(name="State")
UMLModel_ForkNode = Class(name="UMLModel::ForkNode")
UMLModel_FlowFinalNode = Class(name="UMLModel::FlowFinalNode")
UMLModel_FinalNode = Class(name="UMLModel::FinalNode", is_abstract=True)
UMLModel_FunctionBehavior = Class(name="UMLModel::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
MessageEnd = Class(name="MessageEnd")
UMLModel_ExpansionNode = Class(name="UMLModel::ExpansionNode")
UMLModel_ExpansionRegion = Class(name="UMLModel::ExpansionRegion")
UMLModel_Extend = Class(name="UMLModel::Extend")
UMLModel_Extension = Class(name="UMLModel::Extension")
UMLModel_Interface = Class(name="UMLModel::Interface")
UMLModel_ProtocolStateMachine = Class(name="UMLModel::ProtocolStateMachine")
UMLModel_Include = Class(name="UMLModel::Include")
UMLModel_InstanceSpecification = Class(name="UMLModel::InstanceSpecification")
DeploymentTarget = Class(name="DeploymentTarget")
UMLModel_GeneralOrdering = Class(name="UMLModel::GeneralOrdering")
UMLModel_GeneralizationSet = Class(name="UMLModel::GeneralizationSet")
UMLModel_Image = Class(name="UMLModel::Image")
Pin = Class(name="Pin")
UMLModel_InvocationAction = Class(name="UMLModel::InvocationAction", is_abstract=True)
UMLModel_Slot = Class(name="UMLModel::Slot")
UMLModel_InstanceValue = Class(name="UMLModel::InstanceValue")
UMLModel_InterruptibleActivityRegion = Class(name="UMLModel::InterruptibleActivityRegion")
UMLModel_InteractionUse = Class(name="UMLModel::InteractionUse")
UMLModel_InteractionConstraint = Class(name="UMLModel::InteractionConstraint")
Constraint = Class(name="Constraint")
UMLModel_Interval = Class(name="UMLModel::Interval")
UMLModel_InitialNode = Class(name="UMLModel::InitialNode")
UMLModel_Interaction = Class(name="UMLModel::Interaction")
UMLModel_Lifeline = Class(name="UMLModel::Lifeline")
UMLModel_InteractionFragment = Class(name="UMLModel::InteractionFragment", is_abstract=True)
UMLModel_Message = Class(name="UMLModel::Message")
UMLModel_LiteralSpecification = Class(name="UMLModel::LiteralSpecification", is_abstract=True)
UMLModel_LiteralInteger = Class(name="UMLModel::LiteralInteger")
LiteralSpecification = Class(name="LiteralSpecification")
UMLModel_LiteralString = Class(name="UMLModel::LiteralString")
UMLModel_LiteralBoolean = Class(name="UMLModel::LiteralBoolean")
UMLModel_LiteralNull = Class(name="UMLModel::LiteralNull")
UMLModel_LiteralUnlimitedNatural = Class(name="UMLModel::LiteralUnlimitedNatural")
UMLModel_IntervalConstraint = Class(name="UMLModel::IntervalConstraint")
UMLModel_InformationItem = Class(name="UMLModel::InformationItem")
UMLModel_InformationFlow = Class(name="UMLModel::InformationFlow")
UMLModel_JoinNode = Class(name="UMLModel::JoinNode")
UMLModel_LoopNode = Class(name="UMLModel::LoopNode")
Abstraction = Class(name="Abstraction")
UMLModel_LinkAction = Class(name="UMLModel::LinkAction", is_abstract=True)
UMLModel_LinkEndData = Class(name="UMLModel::LinkEndData")
UMLModel_QualifierValue = Class(name="UMLModel::QualifierValue")
UMLModel_LinkEndCreationData = Class(name="UMLModel::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UMLModel_LinkEndDestructionData = Class(name="UMLModel::LinkEndDestructionData")
UMLModel_MessageEnd = Class(name="UMLModel::MessageEnd", is_abstract=True)
UMLModel_MessageEvent = Class(name="UMLModel::MessageEvent", is_abstract=True)
UMLModel_MessageOccurrenceSpecification = Class(name="UMLModel::MessageOccurrenceSpecification")
UMLModel_MergeNode = Class(name="UMLModel::MergeNode")
UMLModel_Model = Class(name="UMLModel::Model")
Package = Class(name="Package")
UMLModel_MultiplicityElement = Class(name="UMLModel::MultiplicityElement", is_abstract=True)
UMLModel_Namespace = Class(name="UMLModel::Namespace", is_abstract=True)
UMLModel_PackageImport = Class(name="UMLModel::PackageImport")
UMLModel_Node = Class(name="UMLModel::Node")
BehavioralFeature = Class(name="BehavioralFeature")
UMLModel_NamedElement = Class(name="UMLModel::NamedElement", is_abstract=True)
UMLModel_StringExpression = Class(name="UMLModel::StringExpression")
UMLModel_OpaqueBehavior = Class(name="UMLModel::OpaqueBehavior")
UMLModel_OccurrenceSpecification = Class(name="UMLModel::OccurrenceSpecification")
UMLModel_OperationTemplateParameter = Class(name="UMLModel::OperationTemplateParameter")
UMLModel_OpaqueAction = Class(name="UMLModel::OpaqueAction")
ConnectableElement = Class(name="ConnectableElement")
UMLModel_ParameterableElement = Class(name="UMLModel::ParameterableElement", is_abstract=True)
UMLModel_Package = Class(name="UMLModel::Package")
UMLModel_PackageMerge = Class(name="UMLModel::PackageMerge")
UMLModel_ObjectFlow = Class(name="UMLModel::ObjectFlow")
UMLModel_Observation = Class(name="UMLModel::Observation", is_abstract=True)
UMLModel_ObjectNode = Class(name="UMLModel::ObjectNode", is_abstract=True)
UMLModel_PartDecomposition = Class(name="UMLModel::PartDecomposition")
InteractionUse = Class(name="InteractionUse")
UMLModel_Pin = Class(name="UMLModel::Pin")
UMLModel_PrimitiveType = Class(name="UMLModel::PrimitiveType")
UMLModel_ProtocolTransition = Class(name="UMLModel::ProtocolTransition")
Transition = Class(name="Transition")
UMLModel_ProfileApplication = Class(name="UMLModel::ProfileApplication")
StateMachine = Class(name="StateMachine")
UMLModel_ProtocolConformance = Class(name="UMLModel::ProtocolConformance")
UMLModel_Port = Class(name="UMLModel::Port")
UMLModel_Profile = Class(name="UMLModel::Profile")
StructuralFeature = Class(name="StructuralFeature")
UMLModel_RaiseExceptionAction = Class(name="UMLModel::RaiseExceptionAction")
UMLModel_ReceiveOperationEvent = Class(name="UMLModel::ReceiveOperationEvent")
UMLModel_ReceiveSignalEvent = Class(name="UMLModel::ReceiveSignalEvent")
UMLModel_ReclassifyObjectAction = Class(name="UMLModel::ReclassifyObjectAction")
UMLModel_ReadIsClassifiedObjectAction = Class(name="UMLModel::ReadIsClassifiedObjectAction")
UMLModel_Pseudostate = Class(name="UMLModel::Pseudostate")
UMLModel_ReadLinkObjectEndQualifierAction = Class(name="UMLModel::ReadLinkObjectEndQualifierAction")
UMLModel_ReadSelfAction = Class(name="UMLModel::ReadSelfAction")
UMLModel_ReadStructuralFeatureAction = Class(name="UMLModel::ReadStructuralFeatureAction")
UMLModel_ReadVariableAction = Class(name="UMLModel::ReadVariableAction")
UMLModel_RedefinableTemplateSignature = Class(name="UMLModel::RedefinableTemplateSignature")
UMLModel_ReadExtentAction = Class(name="UMLModel::ReadExtentAction")
UMLModel_ReadLinkAction = Class(name="UMLModel::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UMLModel_ReadLinkObjectEndAction = Class(name="UMLModel::ReadLinkObjectEndAction")
UMLModel_RemoveVariableValueAction = Class(name="UMLModel::RemoveVariableValueAction")
UMLModel_RemoveStructuralFeatureValueAction = Class(name="UMLModel::RemoveStructuralFeatureValueAction")
UMLModel_RedefinableElement = Class(name="UMLModel::RedefinableElement", is_abstract=True)
UMLModel_Relationship = Class(name="UMLModel::Relationship", is_abstract=True)
TemplateSignature = Class(name="TemplateSignature")
UMLModel_ReduceAction = Class(name="UMLModel::ReduceAction")
UMLModel_ReplyAction = Class(name="UMLModel::ReplyAction")
UMLModel_SequenceNode = Class(name="UMLModel::SequenceNode")
UMLModel_SignalEvent = Class(name="UMLModel::SignalEvent")
UMLModel_StateInvariant = Class(name="UMLModel::StateInvariant")
UMLModel_StartClassifierBehaviorAction = Class(name="UMLModel::StartClassifierBehaviorAction")
UMLModel_SendObjectAction = Class(name="UMLModel::SendObjectAction")
UMLModel_Realization = Class(name="UMLModel::Realization")
UMLModel_Region = Class(name="UMLModel::Region")
UMLModel_Vertex = Class(name="UMLModel::Vertex", is_abstract=True)
UMLModel_Transition = Class(name="UMLModel::Transition")
UMLModel_SendSignalAction = Class(name="UMLModel::SendSignalAction")
UMLModel_SendSignalEvent = Class(name="UMLModel::SendSignalEvent")
UMLModel_StructuralFeature = Class(name="UMLModel::StructuralFeature", is_abstract=True)
UMLModel_StructuralFeatureAction = Class(name="UMLModel::StructuralFeatureAction", is_abstract=True)
UMLModel_Signal = Class(name="UMLModel::Signal")
UMLModel_State = Class(name="UMLModel::State")
Expression = Class(name="Expression")
UMLModel_StructuredActivityNode = Class(name="UMLModel::StructuredActivityNode")
UMLModel_StateMachine = Class(name="UMLModel::StateMachine")
UMLModel_StructuredClassifier = Class(name="UMLModel::StructuredClassifier", is_abstract=True)
UMLModel_TemplateParameter = Class(name="UMLModel::TemplateParameter")
UMLModel_TestIdentityAction = Class(name="UMLModel::TestIdentityAction")
UMLModel_Stereotype = Class(name="UMLModel::Stereotype")
UMLModel_TemplateableElement = Class(name="UMLModel::TemplateableElement", is_abstract=True)
UMLModel_TemplateBinding = Class(name="UMLModel::TemplateBinding")
UMLModel_TemplateSignature = Class(name="UMLModel::TemplateSignature")
UMLModel_TemplateParameterSubstitution = Class(name="UMLModel::TemplateParameterSubstitution")
UMLModel_TimeConstraint = Class(name="UMLModel::TimeConstraint")
UMLModel_TimeEvent = Class(name="UMLModel::TimeEvent")
UMLModel_TimeExpression = Class(name="UMLModel::TimeExpression")
UMLModel_TimeInterval = Class(name="UMLModel::TimeInterval")
UMLModel_TimeObservation = Class(name="UMLModel::TimeObservation")
UMLModel_ValuePin = Class(name="UMLModel::ValuePin")
UMLModel_ValueSpecificationAction = Class(name="UMLModel::ValueSpecificationAction")
UMLModel_TypedElement = Class(name="UMLModel::TypedElement", is_abstract=True)
UMLModel_Type = Class(name="UMLModel::Type", is_abstract=True)
UMLModel_UnmarshallAction = Class(name="UMLModel::UnmarshallAction")
UMLModel_UMLBase = Class(name="UMLModel::UMLBase", is_abstract=True)
EObject = Class(name="EObject")
UMLModel_Usage = Class(name="UMLModel::Usage")
UMLModel_VariableAction = Class(name="UMLModel::VariableAction", is_abstract=True)
UMLModel_WriteLinkAction = Class(name="UMLModel::WriteLinkAction", is_abstract=True)
UMLModel_WriteVariableAction = Class(name="UMLModel::WriteVariableAction", is_abstract=True)
UMLModel_WriteStructuralFeatureAction = Class(name="UMLModel::WriteStructuralFeatureAction", is_abstract=True)

# UMLModel_Abstraction class attributes and methods

# Dependency class attributes and methods

# UMLModel_OpaqueExpression class attributes and methods
UMLModel_OpaqueExpression_body: Property = Property(name="body", type=StringType)
UMLModel_OpaqueExpression_language: Property = Property(name="language", type=StringType)
UMLModel_OpaqueExpression_result: Property = Property(name="result", type=StringType)
UMLModel_OpaqueExpression_behavior: Property = Property(name="behavior", type=StringType)
UMLModel_OpaqueExpression.attributes={UMLModel_OpaqueExpression_language, UMLModel_OpaqueExpression_behavior, UMLModel_OpaqueExpression_body, UMLModel_OpaqueExpression_result}

# UMLModel_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UMLModel_OutputPin class attributes and methods

# UMLModel_AcceptEventAction class attributes and methods
UMLModel_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=StringType)
UMLModel_AcceptEventAction.attributes={UMLModel_AcceptEventAction_isUnmarshall}

# Action class attributes and methods

# UMLModel_Trigger class attributes and methods
UMLModel_Trigger_event: Property = Property(name="event", type=StringType)
UMLModel_Trigger_port: Property = Property(name="port", type=StringType)
UMLModel_Trigger.attributes={UMLModel_Trigger_port, UMLModel_Trigger_event}

# UMLModel_Action class attributes and methods
UMLModel_Action_output: Property = Property(name="output", type=StringType)
UMLModel_Action_input: Property = Property(name="input", type=StringType)
UMLModel_Action_context: Property = Property(name="context", type=StringType)
UMLModel_Action.attributes={UMLModel_Action_output, UMLModel_Action_input, UMLModel_Action_context}

# ExecutableNode class attributes and methods

# UMLModel_Constraint class attributes and methods
UMLModel_Constraint_constrainedElement: Property = Property(name="constrainedElement", type=StringType)
UMLModel_Constraint_context: Property = Property(name="context", type=StringType)
UMLModel_Constraint.attributes={UMLModel_Constraint_constrainedElement, UMLModel_Constraint_context}

# UMLModel_ActionExecutionSpecification class attributes and methods
UMLModel_ActionExecutionSpecification_action: Property = Property(name="action", type=StringType)
UMLModel_ActionExecutionSpecification.attributes={UMLModel_ActionExecutionSpecification_action}

# ExecutionSpecification class attributes and methods

# UMLModel_ActionInputPin class attributes and methods

# InputPin class attributes and methods

# UMLModel_Activity class attributes and methods
UMLModel_Activity_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
UMLModel_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=StringType)
UMLModel_Activity_structuredNode: Property = Property(name="structuredNode", type=StringType)
UMLModel_Activity_partition: Property = Property(name="partition", type=StringType)
UMLModel_Activity.attributes={UMLModel_Activity_isSingleExecution, UMLModel_Activity_partition, UMLModel_Activity_structuredNode, UMLModel_Activity_isReadOnly}

# Behavior class attributes and methods

# UMLModel_Variable class attributes and methods
UMLModel_Variable_scope: Property = Property(name="scope", type=StringType)
UMLModel_Variable_activityScope: Property = Property(name="activityScope", type=StringType)
UMLModel_Variable.attributes={UMLModel_Variable_activityScope, UMLModel_Variable_scope}

# UMLModel_ActivityEdge class attributes and methods
UMLModel_ActivityEdge_source: Property = Property(name="source", type=StringType)
UMLModel_ActivityEdge_target: Property = Property(name="target", type=StringType)
UMLModel_ActivityEdge_redefinedEdge: Property = Property(name="redefinedEdge", type=StringType)
UMLModel_ActivityEdge_inPartition: Property = Property(name="inPartition", type=StringType)
UMLModel_ActivityEdge_interrupts: Property = Property(name="interrupts", type=StringType)
UMLModel_ActivityEdge_inGroup: Property = Property(name="inGroup", type=StringType)
UMLModel_ActivityEdge_activity: Property = Property(name="activity", type=StringType)
UMLModel_ActivityEdge_inStructuredNode: Property = Property(name="inStructuredNode", type=StringType)
UMLModel_ActivityEdge.attributes={UMLModel_ActivityEdge_activity, UMLModel_ActivityEdge_source, UMLModel_ActivityEdge_target, UMLModel_ActivityEdge_inGroup, UMLModel_ActivityEdge_inPartition, UMLModel_ActivityEdge_redefinedEdge, UMLModel_ActivityEdge_inStructuredNode, UMLModel_ActivityEdge_interrupts}

# UMLModel_ActivityGroup class attributes and methods
UMLModel_ActivityGroup_subgroup: Property = Property(name="subgroup", type=StringType)
UMLModel_ActivityGroup_superGroup: Property = Property(name="superGroup", type=StringType)
UMLModel_ActivityGroup_inActivity: Property = Property(name="inActivity", type=StringType)
UMLModel_ActivityGroup.attributes={UMLModel_ActivityGroup_inActivity, UMLModel_ActivityGroup_superGroup, UMLModel_ActivityGroup_subgroup}

# RedefinableElement class attributes and methods

# UMLModel_ValueSpecification class attributes and methods

# UMLModel_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# Element class attributes and methods

# UMLModel_ActivityNode class attributes and methods
UMLModel_ActivityNode_inInterruptibleRegion: Property = Property(name="inInterruptibleRegion", type=StringType)
UMLModel_ActivityNode_outgoing: Property = Property(name="outgoing", type=StringType)
UMLModel_ActivityNode_incoming: Property = Property(name="incoming", type=StringType)
UMLModel_ActivityNode_inPartition: Property = Property(name="inPartition", type=StringType)
UMLModel_ActivityNode_inGroup: Property = Property(name="inGroup", type=StringType)
UMLModel_ActivityNode_redefinedNode: Property = Property(name="redefinedNode", type=StringType)
UMLModel_ActivityNode_activity: Property = Property(name="activity", type=StringType)
UMLModel_ActivityNode_inStructuredNode: Property = Property(name="inStructuredNode", type=StringType)
UMLModel_ActivityNode.attributes={UMLModel_ActivityNode_redefinedNode, UMLModel_ActivityNode_incoming, UMLModel_ActivityNode_inPartition, UMLModel_ActivityNode_inInterruptibleRegion, UMLModel_ActivityNode_inGroup, UMLModel_ActivityNode_activity, UMLModel_ActivityNode_inStructuredNode, UMLModel_ActivityNode_outgoing}

# UMLModel_ActivityParameterNode class attributes and methods
UMLModel_ActivityParameterNode_parameter: Property = Property(name="parameter", type=StringType)
UMLModel_ActivityParameterNode.attributes={UMLModel_ActivityParameterNode_parameter}

# ObjectNode class attributes and methods

# UMLModel_Actor class attributes and methods

# BehavioredClassifier class attributes and methods

# UMLModel_AddStructuralFeatureValueAction class attributes and methods
UMLModel_AddStructuralFeatureValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
UMLModel_AddStructuralFeatureValueAction.attributes={UMLModel_AddStructuralFeatureValueAction_isReplaceAll}

# WriteStructuralFeatureAction class attributes and methods

# UMLModel_InputPin class attributes and methods

# UMLModel_AddVariableValueAction class attributes and methods
UMLModel_AddVariableValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
UMLModel_AddVariableValueAction.attributes={UMLModel_AddVariableValueAction_isReplaceAll}

# WriteVariableAction class attributes and methods

# UMLModel_AnyReceiveEvent class attributes and methods

# MessageEvent class attributes and methods

# UMLModel_Artifact class attributes and methods
UMLModel_Artifact_fileName: Property = Property(name="fileName", type=StringType)
UMLModel_Artifact.attributes={UMLModel_Artifact_fileName}

# Classifier class attributes and methods

# DeployedArtifact class attributes and methods

# UMLModel_Manifestation class attributes and methods
UMLModel_Manifestation_utilizedElement: Property = Property(name="utilizedElement", type=StringType)
UMLModel_Manifestation.attributes={UMLModel_Manifestation_utilizedElement}

# UMLModel_Operation class attributes and methods
UMLModel_Operation_interface: Property = Property(name="interface", type=StringType)
UMLModel_Operation_class: Property = Property(name="class", type=StringType)
UMLModel_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
UMLModel_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
UMLModel_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
UMLModel_Operation_lower: Property = Property(name="lower", type=StringType)
UMLModel_Operation_upper: Property = Property(name="upper", type=StringType)
UMLModel_Operation_precondition: Property = Property(name="precondition", type=StringType)
UMLModel_Operation_postcondition: Property = Property(name="postcondition", type=StringType)
UMLModel_Operation_redefinedOperation: Property = Property(name="redefinedOperation", type=StringType)
UMLModel_Operation_datatype: Property = Property(name="datatype", type=StringType)
UMLModel_Operation_bodyCondition: Property = Property(name="bodyCondition", type=StringType)
UMLModel_Operation_type: Property = Property(name="type", type=StringType)
UMLModel_Operation.attributes={UMLModel_Operation_isQuery, UMLModel_Operation_isUnique, UMLModel_Operation_type, UMLModel_Operation_interface, UMLModel_Operation_postcondition, UMLModel_Operation_redefinedOperation, UMLModel_Operation_class, UMLModel_Operation_isOrdered, UMLModel_Operation_datatype, UMLModel_Operation_lower, UMLModel_Operation_bodyCondition, UMLModel_Operation_precondition, UMLModel_Operation_upper}

# UMLModel_Property class attributes and methods
UMLModel_Property_isComposite: Property = Property(name="isComposite", type=StringType)
UMLModel_Property_redefinedProperty: Property = Property(name="redefinedProperty", type=StringType)
UMLModel_Property_owningAssociation: Property = Property(name="owningAssociation", type=StringType)
UMLModel_Property_opposite: Property = Property(name="opposite", type=StringType)
UMLModel_Property_subsettedProperty: Property = Property(name="subsettedProperty", type=StringType)
UMLModel_Property_association: Property = Property(name="association", type=StringType)
UMLModel_Property_associationEnd: Property = Property(name="associationEnd", type=StringType)
UMLModel_Property_class: Property = Property(name="class", type=StringType)
UMLModel_Property_datatype: Property = Property(name="datatype", type=StringType)
UMLModel_Property_isDerived: Property = Property(name="isDerived", type=StringType)
UMLModel_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
UMLModel_Property_default: Property = Property(name="default", type=StringType)
UMLModel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UMLModel_Property.attributes={UMLModel_Property_opposite, UMLModel_Property_isComposite, UMLModel_Property_associationEnd, UMLModel_Property_redefinedProperty, UMLModel_Property_association, UMLModel_Property_class, UMLModel_Property_datatype, UMLModel_Property_aggregation, UMLModel_Property_owningAssociation, UMLModel_Property_default, UMLModel_Property_subsettedProperty, UMLModel_Property_isDerived, UMLModel_Property_isDerivedUnion}

# UMLModel_Association class attributes and methods
UMLModel_Association_isDerived: Property = Property(name="isDerived", type=StringType)
UMLModel_Association_endType: Property = Property(name="endType", type=StringType)
UMLModel_Association_navigableOwnedEnd: Property = Property(name="navigableOwnedEnd", type=StringType)
UMLModel_Association_memberEnd: Property = Property(name="memberEnd", type=StringType)
UMLModel_Association.attributes={UMLModel_Association_endType, UMLModel_Association_isDerived, UMLModel_Association_navigableOwnedEnd, UMLModel_Association_memberEnd}

# Relationship class attributes and methods

# UMLModel_ActivityPartition class attributes and methods
UMLModel_ActivityPartition_isDimension: Property = Property(name="isDimension", type=StringType)
UMLModel_ActivityPartition_isExternal: Property = Property(name="isExternal", type=StringType)
UMLModel_ActivityPartition_edge: Property = Property(name="edge", type=StringType)
UMLModel_ActivityPartition_represents: Property = Property(name="represents", type=StringType)
UMLModel_ActivityPartition_superPartition: Property = Property(name="superPartition", type=StringType)
UMLModel_ActivityPartition_node: Property = Property(name="node", type=StringType)
UMLModel_ActivityPartition_subpartition: Property = Property(name="subpartition", type=StringType)
UMLModel_ActivityPartition.attributes={UMLModel_ActivityPartition_superPartition, UMLModel_ActivityPartition_isExternal, UMLModel_ActivityPartition_isDimension, UMLModel_ActivityPartition_edge, UMLModel_ActivityPartition_node, UMLModel_ActivityPartition_subpartition, UMLModel_ActivityPartition_represents}

# NamedElement class attributes and methods

# ActivityGroup class attributes and methods

# UMLModel_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# UMLModel_Behavior class attributes and methods
UMLModel_Behavior_isReentrant: Property = Property(name="isReentrant", type=StringType)
UMLModel_Behavior_redefinedBahavior: Property = Property(name="redefinedBahavior", type=StringType)
UMLModel_Behavior_specification: Property = Property(name="specification", type=StringType)
UMLModel_Behavior_context: Property = Property(name="context", type=StringType)
UMLModel_Behavior_postcondition: Property = Property(name="postcondition", type=StringType)
UMLModel_Behavior_precondition: Property = Property(name="precondition", type=StringType)
UMLModel_Behavior.attributes={UMLModel_Behavior_redefinedBahavior, UMLModel_Behavior_specification, UMLModel_Behavior_precondition, UMLModel_Behavior_isReentrant, UMLModel_Behavior_context, UMLModel_Behavior_postcondition}

# UMLModel_Parameter class attributes and methods
UMLModel_Parameter_parameterSet: Property = Property(name="parameterSet", type=StringType)
UMLModel_Parameter_operation: Property = Property(name="operation", type=StringType)
UMLModel_Parameter_direction: Property = Property(name="direction", type=StringType)
UMLModel_Parameter_default: Property = Property(name="default", type=StringType)
UMLModel_Parameter_isException: Property = Property(name="isException", type=StringType)
UMLModel_Parameter_isStream: Property = Property(name="isStream", type=StringType)
UMLModel_Parameter_effect: Property = Property(name="effect", type=StringType)
UMLModel_Parameter.attributes={UMLModel_Parameter_operation, UMLModel_Parameter_default, UMLModel_Parameter_isException, UMLModel_Parameter_isStream, UMLModel_Parameter_direction, UMLModel_Parameter_parameterSet, UMLModel_Parameter_effect}

# UMLModel_ParameterSet class attributes and methods
UMLModel_ParameterSet_parameter: Property = Property(name="parameter", type=StringType)
UMLModel_ParameterSet.attributes={UMLModel_ParameterSet_parameter}

# UMLModel_BehaviorExecutionSpecification class attributes and methods
UMLModel_BehaviorExecutionSpecification_behavior: Property = Property(name="behavior", type=StringType)
UMLModel_BehaviorExecutionSpecification.attributes={UMLModel_BehaviorExecutionSpecification_behavior}

# UMLModel_BehavioralFeature class attributes and methods
UMLModel_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=StringType)
UMLModel_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
UMLModel_BehavioralFeature_raisedException: Property = Property(name="raisedException", type=StringType)
UMLModel_BehavioralFeature_method: Property = Property(name="method", type=StringType)
UMLModel_BehavioralFeature.attributes={UMLModel_BehavioralFeature_isAbstract, UMLModel_BehavioralFeature_method, UMLModel_BehavioralFeature_raisedException, UMLModel_BehavioralFeature_concurrency}

# Namespace class attributes and methods

# Feature class attributes and methods

# UMLModel_BehavioredClassifier class attributes and methods
UMLModel_BehavioredClassifier_classifierBehavior: Property = Property(name="classifierBehavior", type=StringType)
UMLModel_BehavioredClassifier.attributes={UMLModel_BehavioredClassifier_classifierBehavior}

# UMLModel_InterfaceRealization class attributes and methods
UMLModel_InterfaceRealization_contract: Property = Property(name="contract", type=StringType)
UMLModel_InterfaceRealization_realizingClassifier: Property = Property(name="realizingClassifier", type=StringType)
UMLModel_InterfaceRealization.attributes={UMLModel_InterfaceRealization_contract, UMLModel_InterfaceRealization_realizingClassifier}

# UMLModel_BroadcastSignalAction class attributes and methods
UMLModel_BroadcastSignalAction_signal: Property = Property(name="signal", type=StringType)
UMLModel_BroadcastSignalAction.attributes={UMLModel_BroadcastSignalAction_signal}

# InvocationAction class attributes and methods

# UMLModel_CallAction class attributes and methods
UMLModel_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=StringType)
UMLModel_CallAction.attributes={UMLModel_CallAction_isSynchronous}

# UMLModel_CallBehaviorAction class attributes and methods
UMLModel_CallBehaviorAction_behavior: Property = Property(name="behavior", type=StringType)
UMLModel_CallBehaviorAction.attributes={UMLModel_CallBehaviorAction_behavior}

# CallAction class attributes and methods

# UMLModel_CallEvent class attributes and methods
UMLModel_CallEvent_operation: Property = Property(name="operation", type=StringType)
UMLModel_CallEvent.attributes={UMLModel_CallEvent_operation}

# UMLModel_CallOperationAction class attributes and methods
UMLModel_CallOperationAction_operation: Property = Property(name="operation", type=StringType)
UMLModel_CallOperationAction.attributes={UMLModel_CallOperationAction_operation}

# UMLModel_ChangeEvent class attributes and methods

# Event class attributes and methods

# UMLModel_Class class attributes and methods
UMLModel_Class_isActive: Property = Property(name="isActive", type=StringType)
UMLModel_Class_superclass: Property = Property(name="superclass", type=StringType)
UMLModel_Class_extension: Property = Property(name="extension", type=StringType)
UMLModel_Class.attributes={UMLModel_Class_isActive, UMLModel_Class_extension, UMLModel_Class_superclass}

# EncapsulatedClassifier class attributes and methods

# UMLModel_Classifier class attributes and methods
UMLModel_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
UMLModel_Classifier_powertypeExtent: Property = Property(name="powertypeExtent", type=StringType)
UMLModel_Classifier_feature: Property = Property(name="feature", type=StringType)
UMLModel_Classifier_inheritedMember: Property = Property(name="inheritedMember", type=StringType)
UMLModel_Classifier_redefinedClassifier: Property = Property(name="redefinedClassifier", type=StringType)
UMLModel_Classifier_general: Property = Property(name="general", type=StringType)
UMLModel_Classifier_representation: Property = Property(name="representation", type=StringType)
UMLModel_Classifier_attribute: Property = Property(name="attribute", type=StringType)
UMLModel_Classifier_useCase: Property = Property(name="useCase", type=StringType)
UMLModel_Classifier.attributes={UMLModel_Classifier_powertypeExtent, UMLModel_Classifier_useCase, UMLModel_Classifier_attribute, UMLModel_Classifier_representation, UMLModel_Classifier_isAbstract, UMLModel_Classifier_general, UMLModel_Classifier_inheritedMember, UMLModel_Classifier_feature, UMLModel_Classifier_redefinedClassifier}

# UMLModel_Reception class attributes and methods
UMLModel_Reception_signal: Property = Property(name="signal", type=StringType)
UMLModel_Reception.attributes={UMLModel_Reception_signal}

# Type class attributes and methods

# TemplateableElement class attributes and methods

# UMLModel_Generalization class attributes and methods
UMLModel_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
UMLModel_Generalization_general: Property = Property(name="general", type=StringType)
UMLModel_Generalization_generalizationSet: Property = Property(name="generalizationSet", type=StringType)
UMLModel_Generalization_specific: Property = Property(name="specific", type=StringType)
UMLModel_Generalization.attributes={UMLModel_Generalization_generalizationSet, UMLModel_Generalization_specific, UMLModel_Generalization_isSubstitutable, UMLModel_Generalization_general}

# UMLModel_Substitution class attributes and methods
UMLModel_Substitution_contract: Property = Property(name="contract", type=StringType)
UMLModel_Substitution_substitutingClassifier: Property = Property(name="substitutingClassifier", type=StringType)
UMLModel_Substitution.attributes={UMLModel_Substitution_contract, UMLModel_Substitution_substitutingClassifier}

# UMLModel_UseCase class attributes and methods
UMLModel_UseCase_subject: Property = Property(name="subject", type=StringType)
UMLModel_UseCase.attributes={UMLModel_UseCase_subject}

# UMLModel_ClassifierTemplateParameter class attributes and methods
UMLModel_ClassifierTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=StringType)
UMLModel_ClassifierTemplateParameter_defaultClassifier: Property = Property(name="defaultClassifier", type=StringType)
UMLModel_ClassifierTemplateParameter_constrainingClassifier: Property = Property(name="constrainingClassifier", type=StringType)
UMLModel_ClassifierTemplateParameter.attributes={UMLModel_ClassifierTemplateParameter_allowSubstitutable, UMLModel_ClassifierTemplateParameter_constrainingClassifier, UMLModel_ClassifierTemplateParameter_defaultClassifier}

# TemplateParameter class attributes and methods

# UMLModel_Clause class attributes and methods
UMLModel_Clause_predecessorClause: Property = Property(name="predecessorClause", type=StringType)
UMLModel_Clause_successorClause: Property = Property(name="successorClause", type=StringType)
UMLModel_Clause_decider: Property = Property(name="decider", type=StringType)
UMLModel_Clause_bodyOutput: Property = Property(name="bodyOutput", type=StringType)
UMLModel_Clause_test: Property = Property(name="test", type=StringType)
UMLModel_Clause_body: Property = Property(name="body", type=StringType)
UMLModel_Clause.attributes={UMLModel_Clause_bodyOutput, UMLModel_Clause_test, UMLModel_Clause_predecessorClause, UMLModel_Clause_decider, UMLModel_Clause_successorClause, UMLModel_Clause_body}

# UMLModel_ClearVariableAction class attributes and methods

# VariableAction class attributes and methods

# UMLModel_ClearAssociationAction class attributes and methods
UMLModel_ClearAssociationAction_association: Property = Property(name="association", type=StringType)
UMLModel_ClearAssociationAction.attributes={UMLModel_ClearAssociationAction_association}

# UMLModel_ClearStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UMLModel_Collaboration class attributes and methods
UMLModel_Collaboration_collaborationRole: Property = Property(name="collaborationRole", type=StringType)
UMLModel_Collaboration.attributes={UMLModel_Collaboration_collaborationRole}

# StructuredClassifier class attributes and methods

# UMLModel_Dependency class attributes and methods
UMLModel_Dependency_supplier: Property = Property(name="supplier", type=StringType)
UMLModel_Dependency_client: Property = Property(name="client", type=StringType)
UMLModel_Dependency.attributes={UMLModel_Dependency_client, UMLModel_Dependency_supplier}

# UMLModel_Comment class attributes and methods
UMLModel_Comment_body: Property = Property(name="body", type=StringType)
UMLModel_Comment_annotatedElement: Property = Property(name="annotatedElement", type=StringType)
UMLModel_Comment.attributes={UMLModel_Comment_body, UMLModel_Comment_annotatedElement}

# UMLModel_CommunicationPath class attributes and methods

# UMLModel_Component class attributes and methods
UMLModel_Component_indirectlyInstantiated: Property = Property(name="indirectlyInstantiated", type=StringType)
UMLModel_Component_required: Property = Property(name="required", type=StringType)
UMLModel_Component_provided: Property = Property(name="provided", type=StringType)
UMLModel_Component.attributes={UMLModel_Component_required, UMLModel_Component_provided, UMLModel_Component_indirectlyInstantiated}

# UMLModel_PackageableElement class attributes and methods

# UMLModel_ComponentRealization class attributes and methods
UMLModel_ComponentRealization_abstraction: Property = Property(name="abstraction", type=StringType)
UMLModel_ComponentRealization_realizingClassifier: Property = Property(name="realizingClassifier", type=StringType)
UMLModel_ComponentRealization.attributes={UMLModel_ComponentRealization_abstraction, UMLModel_ComponentRealization_realizingClassifier}

# UMLModel_CollaborationUse class attributes and methods
UMLModel_CollaborationUse_type: Property = Property(name="type", type=StringType)
UMLModel_CollaborationUse.attributes={UMLModel_CollaborationUse_type}

# UMLModel_CombinedFragment class attributes and methods
UMLModel_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
UMLModel_CombinedFragment.attributes={UMLModel_CombinedFragment_interactionOperator}

# InteractionFragment class attributes and methods

# UMLModel_InteractionOperand class attributes and methods

# UMLModel_Gate class attributes and methods

# UMLModel_ConditionalNode class attributes and methods
UMLModel_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=StringType)
UMLModel_ConditionalNode_isAssured: Property = Property(name="isAssured", type=StringType)
UMLModel_ConditionalNode.attributes={UMLModel_ConditionalNode_isAssured, UMLModel_ConditionalNode_isDeterminate}

# StructuredActivityNode class attributes and methods

# PackageableElement class attributes and methods

# UMLModel_ConsiderIgnoreFragment class attributes and methods
UMLModel_ConsiderIgnoreFragment_message: Property = Property(name="message", type=StringType)
UMLModel_ConsiderIgnoreFragment.attributes={UMLModel_ConsiderIgnoreFragment_message}

# CombinedFragment class attributes and methods

# UMLModel_Continuation class attributes and methods
UMLModel_Continuation_setting: Property = Property(name="setting", type=StringType)
UMLModel_Continuation.attributes={UMLModel_Continuation_setting}

# UMLModel_ConnectableElement class attributes and methods
UMLModel_ConnectableElement_end: Property = Property(name="end", type=StringType)
UMLModel_ConnectableElement.attributes={UMLModel_ConnectableElement_end}

# TypedElement class attributes and methods

# ParameterableElement class attributes and methods

# UMLModel_ConnectableElementTemplateParameter class attributes and methods

# UMLModel_ConnectorEnd class attributes and methods
UMLModel_ConnectorEnd_definingEnd: Property = Property(name="definingEnd", type=StringType)
UMLModel_ConnectorEnd_partWithPort: Property = Property(name="partWithPort", type=StringType)
UMLModel_ConnectorEnd_role: Property = Property(name="role", type=StringType)
UMLModel_ConnectorEnd.attributes={UMLModel_ConnectorEnd_definingEnd, UMLModel_ConnectorEnd_role, UMLModel_ConnectorEnd_partWithPort}

# MultiplicityElement class attributes and methods

# UMLModel_ConnectionPointReference class attributes and methods
UMLModel_ConnectionPointReference_entry: Property = Property(name="entry", type=StringType)
UMLModel_ConnectionPointReference_exit: Property = Property(name="exit", type=StringType)
UMLModel_ConnectionPointReference_state: Property = Property(name="state", type=StringType)
UMLModel_ConnectionPointReference.attributes={UMLModel_ConnectionPointReference_state, UMLModel_ConnectionPointReference_exit, UMLModel_ConnectionPointReference_entry}

# Vertex class attributes and methods

# UMLModel_Connector class attributes and methods
UMLModel_Connector_redefinedConnector: Property = Property(name="redefinedConnector", type=StringType)
UMLModel_Connector_kind: Property = Property(name="kind", type=StringType)
UMLModel_Connector_contract: Property = Property(name="contract", type=StringType)
UMLModel_Connector_type: Property = Property(name="type", type=StringType)
UMLModel_Connector.attributes={UMLModel_Connector_kind, UMLModel_Connector_type, UMLModel_Connector_contract, UMLModel_Connector_redefinedConnector}

# Realization class attributes and methods

# UMLModel_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# UMLModel_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# UMLModel_CreationEvent class attributes and methods

# UMLModel_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UMLModel_CreateObjectAction class attributes and methods
UMLModel_CreateObjectAction_classifier: Property = Property(name="classifier", type=StringType)
UMLModel_CreateObjectAction.attributes={UMLModel_CreateObjectAction_classifier}

# UMLModel_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UMLModel_CentralBufferNode class attributes and methods

# UMLModel_DeployedArtifact class attributes and methods

# Artifact class attributes and methods

# UMLModel_DirectedRelationship class attributes and methods
UMLModel_DirectedRelationship_source: Property = Property(name="source", type=StringType)
UMLModel_DirectedRelationship_target: Property = Property(name="target", type=StringType)
UMLModel_DirectedRelationship.attributes={UMLModel_DirectedRelationship_target, UMLModel_DirectedRelationship_source}

# UMLModel_Device class attributes and methods

# Node class attributes and methods

# UMLModel_DestroyLinkAction class attributes and methods

# UMLModel_DestroyObjectAction class attributes and methods
UMLModel_DestroyObjectAction_isDestroyLinks: Property = Property(name="isDestroyLinks", type=StringType)
UMLModel_DestroyObjectAction_isDestroyOwnedObjects: Property = Property(name="isDestroyOwnedObjects", type=StringType)
UMLModel_DestroyObjectAction.attributes={UMLModel_DestroyObjectAction_isDestroyOwnedObjects, UMLModel_DestroyObjectAction_isDestroyLinks}

# UMLModel_DestructionEvent class attributes and methods

# UMLModel_Duration class attributes and methods
UMLModel_Duration_expr: Property = Property(name="expr", type=StringType)
UMLModel_Duration_observation: Property = Property(name="observation", type=StringType)
UMLModel_Duration.attributes={UMLModel_Duration_expr, UMLModel_Duration_observation}

# ValueSpecification class attributes and methods

# UMLModel_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UMLModel_DataType class attributes and methods

# UMLModel_DecisionNode class attributes and methods
UMLModel_DecisionNode_decisionInput: Property = Property(name="decisionInput", type=StringType)
UMLModel_DecisionNode.attributes={UMLModel_DecisionNode_decisionInput}

# ControlNode class attributes and methods

# DirectedRelationship class attributes and methods

# UMLModel_DeploymentTarget class attributes and methods
UMLModel_DeploymentTarget_deployedElement: Property = Property(name="deployedElement", type=StringType)
UMLModel_DeploymentTarget.attributes={UMLModel_DeploymentTarget_deployedElement}

# UMLModel_Deployment class attributes and methods
UMLModel_Deployment_location: Property = Property(name="location", type=StringType)
UMLModel_Deployment_deployedArtifact: Property = Property(name="deployedArtifact", type=StringType)
UMLModel_Deployment.attributes={UMLModel_Deployment_location, UMLModel_Deployment_deployedArtifact}

# UMLModel_DeploymentSpecification class attributes and methods
UMLModel_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
UMLModel_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
UMLModel_DeploymentSpecification_deployment: Property = Property(name="deployment", type=StringType)
UMLModel_DeploymentSpecification.attributes={UMLModel_DeploymentSpecification_deploymentLocation, UMLModel_DeploymentSpecification_deployment, UMLModel_DeploymentSpecification_executionLocation}

# UMLModel_EncapsulatedClassifier class attributes and methods
UMLModel_EncapsulatedClassifier_ownedPort: Property = Property(name="ownedPort", type=StringType)
UMLModel_EncapsulatedClassifier.attributes={UMLModel_EncapsulatedClassifier_ownedPort}

# UMLModel_Enumeration class attributes and methods

# DataType class attributes and methods

# UMLModel_EnumerationLiteral class attributes and methods
UMLModel_EnumerationLiteral_enumeration: Property = Property(name="enumeration", type=StringType)
UMLModel_EnumerationLiteral.attributes={UMLModel_EnumerationLiteral_enumeration}

# InstanceSpecification class attributes and methods

# UMLModel_ExceptionHandler class attributes and methods
UMLModel_ExceptionHandler_handlerBody: Property = Property(name="handlerBody", type=StringType)
UMLModel_ExceptionHandler_exceptionInput: Property = Property(name="exceptionInput", type=StringType)
UMLModel_ExceptionHandler_exceptionType: Property = Property(name="exceptionType", type=StringType)
UMLModel_ExceptionHandler_protectedNode: Property = Property(name="protectedNode", type=StringType)
UMLModel_ExceptionHandler.attributes={UMLModel_ExceptionHandler_exceptionInput, UMLModel_ExceptionHandler_handlerBody, UMLModel_ExceptionHandler_protectedNode, UMLModel_ExceptionHandler_exceptionType}

# UMLModel_ExecutableNode class attributes and methods

# UMLModel_ExecutionEnvironment class attributes and methods

# UMLModel_ExecutionEvent class attributes and methods

# UMLModel_ExecutionOccurrenceSpecification class attributes and methods
UMLModel_ExecutionOccurrenceSpecification_execution: Property = Property(name="execution", type=StringType)
UMLModel_ExecutionOccurrenceSpecification.attributes={UMLModel_ExecutionOccurrenceSpecification_execution}

# OccurrenceSpecification class attributes and methods

# UMLModel_ExecutionSpecification class attributes and methods
UMLModel_ExecutionSpecification_start: Property = Property(name="start", type=StringType)
UMLModel_ExecutionSpecification_finish: Property = Property(name="finish", type=StringType)
UMLModel_ExecutionSpecification.attributes={UMLModel_ExecutionSpecification_start, UMLModel_ExecutionSpecification_finish}

# UMLModel_DurationConstraint class attributes and methods
UMLModel_DurationConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
UMLModel_DurationConstraint.attributes={UMLModel_DurationConstraint_firstEvent}

# IntervalConstraint class attributes and methods

# UMLModel_DurationInterval class attributes and methods

# Interval class attributes and methods

# UMLModel_DurationObservation class attributes and methods
UMLModel_DurationObservation_event: Property = Property(name="event", type=StringType)
UMLModel_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
UMLModel_DurationObservation.attributes={UMLModel_DurationObservation_firstEvent, UMLModel_DurationObservation_event}

# Observation class attributes and methods

# UMLModel_Element class attributes and methods
UMLModel_Element_owner: Property = Property(name="owner", type=StringType)
UMLModel_Element_ownedElement: Property = Property(name="ownedElement", type=StringType)
UMLModel_Element_href: Property = Property(name="href", type=StringType)
UMLModel_Element.attributes={UMLModel_Element_href, UMLModel_Element_owner, UMLModel_Element_ownedElement}

# UMLBase class attributes and methods

# UMLModel_ElementImport class attributes and methods
UMLModel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
UMLModel_ElementImport_alias: Property = Property(name="alias", type=StringType)
UMLModel_ElementImport_importingNamespace: Property = Property(name="importingNamespace", type=StringType)
UMLModel_ElementImport.attributes={UMLModel_ElementImport_visibility, UMLModel_ElementImport_importingNamespace, UMLModel_ElementImport_alias}

# UMLModel_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UMLModel_ExtensionPoint class attributes and methods
UMLModel_ExtensionPoint_useCase: Property = Property(name="useCase", type=StringType)
UMLModel_ExtensionPoint.attributes={UMLModel_ExtensionPoint_useCase}

# UMLModel_Expression class attributes and methods
UMLModel_Expression_symbol: Property = Property(name="symbol", type=StringType)
UMLModel_Expression.attributes={UMLModel_Expression_symbol}

# UMLModel_Event class attributes and methods

# UMLModel_Feature class attributes and methods
UMLModel_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
UMLModel_Feature_featuringClassifier: Property = Property(name="featuringClassifier", type=StringType)
UMLModel_Feature.attributes={UMLModel_Feature_featuringClassifier, UMLModel_Feature_isStatic}

# UMLModel_FinalState class attributes and methods

# State class attributes and methods

# UMLModel_ForkNode class attributes and methods

# UMLModel_FlowFinalNode class attributes and methods

# UMLModel_FinalNode class attributes and methods

# UMLModel_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# MessageEnd class attributes and methods

# UMLModel_ExpansionNode class attributes and methods
UMLModel_ExpansionNode_regionAsOutput: Property = Property(name="regionAsOutput", type=StringType)
UMLModel_ExpansionNode_regionAsInput: Property = Property(name="regionAsInput", type=StringType)
UMLModel_ExpansionNode.attributes={UMLModel_ExpansionNode_regionAsInput, UMLModel_ExpansionNode_regionAsOutput}

# UMLModel_ExpansionRegion class attributes and methods
UMLModel_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
UMLModel_ExpansionRegion_inputElement: Property = Property(name="inputElement", type=StringType)
UMLModel_ExpansionRegion_outputElement: Property = Property(name="outputElement", type=StringType)
UMLModel_ExpansionRegion.attributes={UMLModel_ExpansionRegion_outputElement, UMLModel_ExpansionRegion_inputElement, UMLModel_ExpansionRegion_mode}

# UMLModel_Extend class attributes and methods
UMLModel_Extend_extendedCase: Property = Property(name="extendedCase", type=StringType)
UMLModel_Extend_extensionLocation: Property = Property(name="extensionLocation", type=StringType)
UMLModel_Extend_extension: Property = Property(name="extension", type=StringType)
UMLModel_Extend.attributes={UMLModel_Extend_extensionLocation, UMLModel_Extend_extension, UMLModel_Extend_extendedCase}

# UMLModel_Extension class attributes and methods
UMLModel_Extension_isRequired: Property = Property(name="isRequired", type=StringType)
UMLModel_Extension_metaClass: Property = Property(name="metaClass", type=StringType)
UMLModel_Extension.attributes={UMLModel_Extension_metaClass, UMLModel_Extension_isRequired}

# UMLModel_Interface class attributes and methods
UMLModel_Interface_redefinedInterface: Property = Property(name="redefinedInterface", type=StringType)
UMLModel_Interface_isActive: Property = Property(name="isActive", type=BooleanType)
UMLModel_Interface.attributes={UMLModel_Interface_isActive, UMLModel_Interface_redefinedInterface}

# UMLModel_ProtocolStateMachine class attributes and methods

# UMLModel_Include class attributes and methods
UMLModel_Include_addition: Property = Property(name="addition", type=StringType)
UMLModel_Include_includingCase: Property = Property(name="includingCase", type=StringType)
UMLModel_Include.attributes={UMLModel_Include_includingCase, UMLModel_Include_addition}

# UMLModel_InstanceSpecification class attributes and methods
UMLModel_InstanceSpecification_classifier: Property = Property(name="classifier", type=StringType)
UMLModel_InstanceSpecification.attributes={UMLModel_InstanceSpecification_classifier}

# DeploymentTarget class attributes and methods

# UMLModel_GeneralOrdering class attributes and methods
UMLModel_GeneralOrdering_before: Property = Property(name="before", type=StringType)
UMLModel_GeneralOrdering_after: Property = Property(name="after", type=StringType)
UMLModel_GeneralOrdering.attributes={UMLModel_GeneralOrdering_before, UMLModel_GeneralOrdering_after}

# UMLModel_GeneralizationSet class attributes and methods
UMLModel_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
UMLModel_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
UMLModel_GeneralizationSet_generalization: Property = Property(name="generalization", type=StringType)
UMLModel_GeneralizationSet_powerType: Property = Property(name="powerType", type=StringType)
UMLModel_GeneralizationSet.attributes={UMLModel_GeneralizationSet_generalization, UMLModel_GeneralizationSet_isCovering, UMLModel_GeneralizationSet_powerType, UMLModel_GeneralizationSet_isDisjoint}

# UMLModel_Image class attributes and methods
UMLModel_Image_content: Property = Property(name="content", type=StringType)
UMLModel_Image_location: Property = Property(name="location", type=StringType)
UMLModel_Image_format: Property = Property(name="format", type=StringType)
UMLModel_Image.attributes={UMLModel_Image_content, UMLModel_Image_format, UMLModel_Image_location}

# Pin class attributes and methods

# UMLModel_InvocationAction class attributes and methods
UMLModel_InvocationAction_onPort: Property = Property(name="onPort", type=StringType)
UMLModel_InvocationAction.attributes={UMLModel_InvocationAction_onPort}

# UMLModel_Slot class attributes and methods
UMLModel_Slot_definingFeature: Property = Property(name="definingFeature", type=StringType)
UMLModel_Slot_owningInstance: Property = Property(name="owningInstance", type=StringType)
UMLModel_Slot.attributes={UMLModel_Slot_owningInstance, UMLModel_Slot_definingFeature}

# UMLModel_InstanceValue class attributes and methods
UMLModel_InstanceValue_instance: Property = Property(name="instance", type=StringType)
UMLModel_InstanceValue.attributes={UMLModel_InstanceValue_instance}

# UMLModel_InterruptibleActivityRegion class attributes and methods
UMLModel_InterruptibleActivityRegion_interruptingEdge: Property = Property(name="interruptingEdge", type=StringType)
UMLModel_InterruptibleActivityRegion_node: Property = Property(name="node", type=StringType)
UMLModel_InterruptibleActivityRegion.attributes={UMLModel_InterruptibleActivityRegion_node, UMLModel_InterruptibleActivityRegion_interruptingEdge}

# UMLModel_InteractionUse class attributes and methods
UMLModel_InteractionUse_refersTo: Property = Property(name="refersTo", type=StringType)
UMLModel_InteractionUse.attributes={UMLModel_InteractionUse_refersTo}

# UMLModel_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# UMLModel_Interval class attributes and methods
UMLModel_Interval_min: Property = Property(name="min", type=StringType)
UMLModel_Interval_max: Property = Property(name="max", type=StringType)
UMLModel_Interval.attributes={UMLModel_Interval_max, UMLModel_Interval_min}

# UMLModel_InitialNode class attributes and methods

# UMLModel_Interaction class attributes and methods

# UMLModel_Lifeline class attributes and methods
UMLModel_Lifeline_represents: Property = Property(name="represents", type=StringType)
UMLModel_Lifeline_interaction: Property = Property(name="interaction", type=StringType)
UMLModel_Lifeline_decomposedAs: Property = Property(name="decomposedAs", type=StringType)
UMLModel_Lifeline_coveredBy: Property = Property(name="coveredBy", type=StringType)
UMLModel_Lifeline.attributes={UMLModel_Lifeline_coveredBy, UMLModel_Lifeline_decomposedAs, UMLModel_Lifeline_interaction, UMLModel_Lifeline_represents}

# UMLModel_InteractionFragment class attributes and methods
UMLModel_InteractionFragment_enclosingInteraction: Property = Property(name="enclosingInteraction", type=StringType)
UMLModel_InteractionFragment_enclosingOperand: Property = Property(name="enclosingOperand", type=StringType)
UMLModel_InteractionFragment_covered: Property = Property(name="covered", type=StringType)
UMLModel_InteractionFragment.attributes={UMLModel_InteractionFragment_enclosingInteraction, UMLModel_InteractionFragment_enclosingOperand, UMLModel_InteractionFragment_covered}

# UMLModel_Message class attributes and methods
UMLModel_Message_messageKind: Property = Property(name="messageKind", type=StringType)
UMLModel_Message_signature: Property = Property(name="signature", type=StringType)
UMLModel_Message_messageSort: Property = Property(name="messageSort", type=StringType)
UMLModel_Message_receiveEvent: Property = Property(name="receiveEvent", type=StringType)
UMLModel_Message_sendEvent: Property = Property(name="sendEvent", type=StringType)
UMLModel_Message_connector: Property = Property(name="connector", type=StringType)
UMLModel_Message_interaction: Property = Property(name="interaction", type=StringType)
UMLModel_Message.attributes={UMLModel_Message_connector, UMLModel_Message_interaction, UMLModel_Message_sendEvent, UMLModel_Message_messageKind, UMLModel_Message_signature, UMLModel_Message_receiveEvent, UMLModel_Message_messageSort}

# UMLModel_LiteralSpecification class attributes and methods

# UMLModel_LiteralInteger class attributes and methods
UMLModel_LiteralInteger_value: Property = Property(name="value", type=StringType)
UMLModel_LiteralInteger.attributes={UMLModel_LiteralInteger_value}

# LiteralSpecification class attributes and methods

# UMLModel_LiteralString class attributes and methods
UMLModel_LiteralString_value: Property = Property(name="value", type=StringType)
UMLModel_LiteralString.attributes={UMLModel_LiteralString_value}

# UMLModel_LiteralBoolean class attributes and methods
UMLModel_LiteralBoolean_value: Property = Property(name="value", type=StringType)
UMLModel_LiteralBoolean.attributes={UMLModel_LiteralBoolean_value}

# UMLModel_LiteralNull class attributes and methods

# UMLModel_LiteralUnlimitedNatural class attributes and methods
UMLModel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
UMLModel_LiteralUnlimitedNatural.attributes={UMLModel_LiteralUnlimitedNatural_value}

# UMLModel_IntervalConstraint class attributes and methods

# UMLModel_InformationItem class attributes and methods
UMLModel_InformationItem_represented: Property = Property(name="represented", type=StringType)
UMLModel_InformationItem.attributes={UMLModel_InformationItem_represented}

# UMLModel_InformationFlow class attributes and methods
UMLModel_InformationFlow_realization: Property = Property(name="realization", type=StringType)
UMLModel_InformationFlow_conveyed: Property = Property(name="conveyed", type=StringType)
UMLModel_InformationFlow_informationSource: Property = Property(name="informationSource", type=StringType)
UMLModel_InformationFlow_informationTarget: Property = Property(name="informationTarget", type=StringType)
UMLModel_InformationFlow_realizingActivityEdge: Property = Property(name="realizingActivityEdge", type=StringType)
UMLModel_InformationFlow_realizingConnector: Property = Property(name="realizingConnector", type=StringType)
UMLModel_InformationFlow_realizingMessage: Property = Property(name="realizingMessage", type=StringType)
UMLModel_InformationFlow.attributes={UMLModel_InformationFlow_realizingConnector, UMLModel_InformationFlow_realization, UMLModel_InformationFlow_realizingMessage, UMLModel_InformationFlow_conveyed, UMLModel_InformationFlow_informationSource, UMLModel_InformationFlow_informationTarget, UMLModel_InformationFlow_realizingActivityEdge}

# UMLModel_JoinNode class attributes and methods
UMLModel_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=StringType)
UMLModel_JoinNode.attributes={UMLModel_JoinNode_isCombineDuplicate}

# UMLModel_LoopNode class attributes and methods
UMLModel_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=StringType)
UMLModel_LoopNode_bodyPart: Property = Property(name="bodyPart", type=StringType)
UMLModel_LoopNode_setupPart: Property = Property(name="setupPart", type=StringType)
UMLModel_LoopNode_decider: Property = Property(name="decider", type=StringType)
UMLModel_LoopNode_test: Property = Property(name="test", type=StringType)
UMLModel_LoopNode_loopVariable: Property = Property(name="loopVariable", type=StringType)
UMLModel_LoopNode_bodyOutput: Property = Property(name="bodyOutput", type=StringType)
UMLModel_LoopNode.attributes={UMLModel_LoopNode_setupPart, UMLModel_LoopNode_test, UMLModel_LoopNode_decider, UMLModel_LoopNode_bodyOutput, UMLModel_LoopNode_bodyPart, UMLModel_LoopNode_isTestedFirst, UMLModel_LoopNode_loopVariable}

# Abstraction class attributes and methods

# UMLModel_LinkAction class attributes and methods

# UMLModel_LinkEndData class attributes and methods
UMLModel_LinkEndData_value: Property = Property(name="value", type=StringType)
UMLModel_LinkEndData_end: Property = Property(name="end", type=StringType)
UMLModel_LinkEndData.attributes={UMLModel_LinkEndData_value, UMLModel_LinkEndData_end}

# UMLModel_QualifierValue class attributes and methods
UMLModel_QualifierValue_qualifier: Property = Property(name="qualifier", type=StringType)
UMLModel_QualifierValue_value: Property = Property(name="value", type=StringType)
UMLModel_QualifierValue.attributes={UMLModel_QualifierValue_value, UMLModel_QualifierValue_qualifier}

# UMLModel_LinkEndCreationData class attributes and methods
UMLModel_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
UMLModel_LinkEndCreationData_insertAt: Property = Property(name="insertAt", type=StringType)
UMLModel_LinkEndCreationData.attributes={UMLModel_LinkEndCreationData_insertAt, UMLModel_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# UMLModel_LinkEndDestructionData class attributes and methods
UMLModel_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=StringType)
UMLModel_LinkEndDestructionData_destroyAt: Property = Property(name="destroyAt", type=StringType)
UMLModel_LinkEndDestructionData.attributes={UMLModel_LinkEndDestructionData_destroyAt, UMLModel_LinkEndDestructionData_isDestroyDuplicates}

# UMLModel_MessageEnd class attributes and methods
UMLModel_MessageEnd_message: Property = Property(name="message", type=StringType)
UMLModel_MessageEnd.attributes={UMLModel_MessageEnd_message}

# UMLModel_MessageEvent class attributes and methods

# UMLModel_MessageOccurrenceSpecification class attributes and methods

# UMLModel_MergeNode class attributes and methods

# UMLModel_Model class attributes and methods
UMLModel_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
UMLModel_Model.attributes={UMLModel_Model_viewpoint}

# Package class attributes and methods

# UMLModel_MultiplicityElement class attributes and methods
UMLModel_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
UMLModel_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
UMLModel_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
UMLModel_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
UMLModel_MultiplicityElement.attributes={UMLModel_MultiplicityElement_upper, UMLModel_MultiplicityElement_isOrdered, UMLModel_MultiplicityElement_lower, UMLModel_MultiplicityElement_isUnique}

# UMLModel_Namespace class attributes and methods
UMLModel_Namespace_member: Property = Property(name="member", type=StringType)
UMLModel_Namespace_importedMember: Property = Property(name="importedMember", type=StringType)
UMLModel_Namespace_ownedMember: Property = Property(name="ownedMember", type=StringType)
UMLModel_Namespace.attributes={UMLModel_Namespace_member, UMLModel_Namespace_importedMember, UMLModel_Namespace_ownedMember}

# UMLModel_PackageImport class attributes and methods
UMLModel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
UMLModel_PackageImport_importingNamespace: Property = Property(name="importingNamespace", type=StringType)
UMLModel_PackageImport.attributes={UMLModel_PackageImport_visibility, UMLModel_PackageImport_importingNamespace}

# UMLModel_Node class attributes and methods

# BehavioralFeature class attributes and methods

# UMLModel_NamedElement class attributes and methods
UMLModel_NamedElement_name: Property = Property(name="name", type=StringType)
UMLModel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
UMLModel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
UMLModel_NamedElement_clientDependency: Property = Property(name="clientDependency", type=StringType)
UMLModel_NamedElement_namespace: Property = Property(name="namespace", type=StringType)
UMLModel_NamedElement.attributes={UMLModel_NamedElement_qualifiedName, UMLModel_NamedElement_namespace, UMLModel_NamedElement_visibility, UMLModel_NamedElement_name, UMLModel_NamedElement_clientDependency}

# UMLModel_StringExpression class attributes and methods
UMLModel_StringExpression_owningExpression: Property = Property(name="owningExpression", type=StringType)
UMLModel_StringExpression.attributes={UMLModel_StringExpression_owningExpression}

# UMLModel_OpaqueBehavior class attributes and methods
UMLModel_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
UMLModel_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
UMLModel_OpaqueBehavior.attributes={UMLModel_OpaqueBehavior_body, UMLModel_OpaqueBehavior_language}

# UMLModel_OccurrenceSpecification class attributes and methods
UMLModel_OccurrenceSpecification_toBefore: Property = Property(name="toBefore", type=StringType)
UMLModel_OccurrenceSpecification_toAfter: Property = Property(name="toAfter", type=StringType)
UMLModel_OccurrenceSpecification_event: Property = Property(name="event", type=StringType)
UMLModel_OccurrenceSpecification.attributes={UMLModel_OccurrenceSpecification_toBefore, UMLModel_OccurrenceSpecification_toAfter, UMLModel_OccurrenceSpecification_event}

# UMLModel_OperationTemplateParameter class attributes and methods

# UMLModel_OpaqueAction class attributes and methods
UMLModel_OpaqueAction_body: Property = Property(name="body", type=StringType)
UMLModel_OpaqueAction_language: Property = Property(name="language", type=StringType)
UMLModel_OpaqueAction.attributes={UMLModel_OpaqueAction_language, UMLModel_OpaqueAction_body}

# ConnectableElement class attributes and methods

# UMLModel_ParameterableElement class attributes and methods
UMLModel_ParameterableElement_owningTemplateParameter: Property = Property(name="owningTemplateParameter", type=StringType)
UMLModel_ParameterableElement_templateParameter: Property = Property(name="templateParameter", type=StringType)
UMLModel_ParameterableElement.attributes={UMLModel_ParameterableElement_owningTemplateParameter, UMLModel_ParameterableElement_templateParameter}

# UMLModel_Package class attributes and methods
UMLModel_Package_ownedType: Property = Property(name="ownedType", type=StringType)
UMLModel_Package_nestedPackage: Property = Property(name="nestedPackage", type=StringType)
UMLModel_Package_nestingPackage: Property = Property(name="nestingPackage", type=StringType)
UMLModel_Package.attributes={UMLModel_Package_nestingPackage, UMLModel_Package_ownedType, UMLModel_Package_nestedPackage}

# UMLModel_PackageMerge class attributes and methods
UMLModel_PackageMerge_mergedPackage: Property = Property(name="mergedPackage", type=StringType)
UMLModel_PackageMerge_receivingPackage: Property = Property(name="receivingPackage", type=StringType)
UMLModel_PackageMerge.attributes={UMLModel_PackageMerge_receivingPackage, UMLModel_PackageMerge_mergedPackage}

# UMLModel_ObjectFlow class attributes and methods
UMLModel_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=StringType)
UMLModel_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=StringType)
UMLModel_ObjectFlow_transformation: Property = Property(name="transformation", type=StringType)
UMLModel_ObjectFlow_selection: Property = Property(name="selection", type=StringType)
UMLModel_ObjectFlow.attributes={UMLModel_ObjectFlow_transformation, UMLModel_ObjectFlow_isMulticast, UMLModel_ObjectFlow_selection, UMLModel_ObjectFlow_isMultireceive}

# UMLModel_Observation class attributes and methods

# UMLModel_ObjectNode class attributes and methods
UMLModel_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
UMLModel_ObjectNode_isControlType: Property = Property(name="isControlType", type=StringType)
UMLModel_ObjectNode_inState: Property = Property(name="inState", type=StringType)
UMLModel_ObjectNode_selection: Property = Property(name="selection", type=StringType)
UMLModel_ObjectNode.attributes={UMLModel_ObjectNode_inState, UMLModel_ObjectNode_selection, UMLModel_ObjectNode_ordering, UMLModel_ObjectNode_isControlType}

# UMLModel_PartDecomposition class attributes and methods

# InteractionUse class attributes and methods

# UMLModel_Pin class attributes and methods
UMLModel_Pin_isControl: Property = Property(name="isControl", type=StringType)
UMLModel_Pin.attributes={UMLModel_Pin_isControl}

# UMLModel_PrimitiveType class attributes and methods

# UMLModel_ProtocolTransition class attributes and methods
UMLModel_ProtocolTransition_postCondition: Property = Property(name="postCondition", type=StringType)
UMLModel_ProtocolTransition_referred: Property = Property(name="referred", type=StringType)
UMLModel_ProtocolTransition_preCondition: Property = Property(name="preCondition", type=StringType)
UMLModel_ProtocolTransition.attributes={UMLModel_ProtocolTransition_referred, UMLModel_ProtocolTransition_postCondition, UMLModel_ProtocolTransition_preCondition}

# Transition class attributes and methods

# UMLModel_ProfileApplication class attributes and methods
UMLModel_ProfileApplication_appliedProfile: Property = Property(name="appliedProfile", type=StringType)
UMLModel_ProfileApplication_isStrict: Property = Property(name="isStrict", type=StringType)
UMLModel_ProfileApplication_applyingPackage: Property = Property(name="applyingPackage", type=StringType)
UMLModel_ProfileApplication.attributes={UMLModel_ProfileApplication_appliedProfile, UMLModel_ProfileApplication_applyingPackage, UMLModel_ProfileApplication_isStrict}

# StateMachine class attributes and methods

# UMLModel_ProtocolConformance class attributes and methods
UMLModel_ProtocolConformance_generalMachine: Property = Property(name="generalMachine", type=StringType)
UMLModel_ProtocolConformance_specificMachine: Property = Property(name="specificMachine", type=StringType)
UMLModel_ProtocolConformance.attributes={UMLModel_ProtocolConformance_generalMachine, UMLModel_ProtocolConformance_specificMachine}

# UMLModel_Port class attributes and methods
UMLModel_Port_isBehavior: Property = Property(name="isBehavior", type=StringType)
UMLModel_Port_isService: Property = Property(name="isService", type=StringType)
UMLModel_Port_required: Property = Property(name="required", type=StringType)
UMLModel_Port_redefinedPort: Property = Property(name="redefinedPort", type=StringType)
UMLModel_Port_provided: Property = Property(name="provided", type=StringType)
UMLModel_Port_protocol: Property = Property(name="protocol", type=StringType)
UMLModel_Port.attributes={UMLModel_Port_provided, UMLModel_Port_isService, UMLModel_Port_required, UMLModel_Port_protocol, UMLModel_Port_isBehavior, UMLModel_Port_redefinedPort}

# UMLModel_Profile class attributes and methods
UMLModel_Profile_ownedStereotype: Property = Property(name="ownedStereotype", type=StringType)
UMLModel_Profile_metaclassReference: Property = Property(name="metaclassReference", type=StringType)
UMLModel_Profile_metamodelReference: Property = Property(name="metamodelReference", type=StringType)
UMLModel_Profile.attributes={UMLModel_Profile_ownedStereotype, UMLModel_Profile_metamodelReference, UMLModel_Profile_metaclassReference}

# StructuralFeature class attributes and methods

# UMLModel_RaiseExceptionAction class attributes and methods

# UMLModel_ReceiveOperationEvent class attributes and methods
UMLModel_ReceiveOperationEvent_operation: Property = Property(name="operation", type=StringType)
UMLModel_ReceiveOperationEvent.attributes={UMLModel_ReceiveOperationEvent_operation}

# UMLModel_ReceiveSignalEvent class attributes and methods
UMLModel_ReceiveSignalEvent_signal: Property = Property(name="signal", type=StringType)
UMLModel_ReceiveSignalEvent.attributes={UMLModel_ReceiveSignalEvent_signal}

# UMLModel_ReclassifyObjectAction class attributes and methods
UMLModel_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
UMLModel_ReclassifyObjectAction_oldClassifier: Property = Property(name="oldClassifier", type=StringType)
UMLModel_ReclassifyObjectAction_newClassifier: Property = Property(name="newClassifier", type=StringType)
UMLModel_ReclassifyObjectAction.attributes={UMLModel_ReclassifyObjectAction_isReplaceAll, UMLModel_ReclassifyObjectAction_oldClassifier, UMLModel_ReclassifyObjectAction_newClassifier}

# UMLModel_ReadIsClassifiedObjectAction class attributes and methods
UMLModel_ReadIsClassifiedObjectAction_isDirect: Property = Property(name="isDirect", type=StringType)
UMLModel_ReadIsClassifiedObjectAction_classifier: Property = Property(name="classifier", type=StringType)
UMLModel_ReadIsClassifiedObjectAction.attributes={UMLModel_ReadIsClassifiedObjectAction_isDirect, UMLModel_ReadIsClassifiedObjectAction_classifier}

# UMLModel_Pseudostate class attributes and methods
UMLModel_Pseudostate_kind: Property = Property(name="kind", type=StringType)
UMLModel_Pseudostate_stateMachine: Property = Property(name="stateMachine", type=StringType)
UMLModel_Pseudostate_state: Property = Property(name="state", type=StringType)
UMLModel_Pseudostate.attributes={UMLModel_Pseudostate_kind, UMLModel_Pseudostate_state, UMLModel_Pseudostate_stateMachine}

# UMLModel_ReadLinkObjectEndQualifierAction class attributes and methods
UMLModel_ReadLinkObjectEndQualifierAction_qualifier: Property = Property(name="qualifier", type=StringType)
UMLModel_ReadLinkObjectEndQualifierAction.attributes={UMLModel_ReadLinkObjectEndQualifierAction_qualifier}

# UMLModel_ReadSelfAction class attributes and methods

# UMLModel_ReadStructuralFeatureAction class attributes and methods

# UMLModel_ReadVariableAction class attributes and methods

# UMLModel_RedefinableTemplateSignature class attributes and methods
UMLModel_RedefinableTemplateSignature_extendedSignature: Property = Property(name="extendedSignature", type=StringType)
UMLModel_RedefinableTemplateSignature_inheritedParameter: Property = Property(name="inheritedParameter", type=StringType)
UMLModel_RedefinableTemplateSignature_classifier: Property = Property(name="classifier", type=StringType)
UMLModel_RedefinableTemplateSignature.attributes={UMLModel_RedefinableTemplateSignature_extendedSignature, UMLModel_RedefinableTemplateSignature_classifier, UMLModel_RedefinableTemplateSignature_inheritedParameter}

# UMLModel_ReadExtentAction class attributes and methods
UMLModel_ReadExtentAction_classifier: Property = Property(name="classifier", type=StringType)
UMLModel_ReadExtentAction.attributes={UMLModel_ReadExtentAction_classifier}

# UMLModel_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UMLModel_ReadLinkObjectEndAction class attributes and methods
UMLModel_ReadLinkObjectEndAction_end: Property = Property(name="end", type=StringType)
UMLModel_ReadLinkObjectEndAction.attributes={UMLModel_ReadLinkObjectEndAction_end}

# UMLModel_RemoveVariableValueAction class attributes and methods
UMLModel_RemoveVariableValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
UMLModel_RemoveVariableValueAction.attributes={UMLModel_RemoveVariableValueAction_isRemoveDuplicates}

# UMLModel_RemoveStructuralFeatureValueAction class attributes and methods
UMLModel_RemoveStructuralFeatureValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
UMLModel_RemoveStructuralFeatureValueAction.attributes={UMLModel_RemoveStructuralFeatureValueAction_isRemoveDuplicates}

# UMLModel_RedefinableElement class attributes and methods
UMLModel_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
UMLModel_RedefinableElement_redefinedElement: Property = Property(name="redefinedElement", type=StringType)
UMLModel_RedefinableElement_redefinitionContext: Property = Property(name="redefinitionContext", type=StringType)
UMLModel_RedefinableElement.attributes={UMLModel_RedefinableElement_redefinedElement, UMLModel_RedefinableElement_isLeaf, UMLModel_RedefinableElement_redefinitionContext}

# UMLModel_Relationship class attributes and methods
UMLModel_Relationship_relatedElement: Property = Property(name="relatedElement", type=StringType)
UMLModel_Relationship.attributes={UMLModel_Relationship_relatedElement}

# TemplateSignature class attributes and methods

# UMLModel_ReduceAction class attributes and methods
UMLModel_ReduceAction_reducer: Property = Property(name="reducer", type=StringType)
UMLModel_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=StringType)
UMLModel_ReduceAction.attributes={UMLModel_ReduceAction_reducer, UMLModel_ReduceAction_isOrdered}

# UMLModel_ReplyAction class attributes and methods
UMLModel_ReplyAction_replyToCall: Property = Property(name="replyToCall", type=StringType)
UMLModel_ReplyAction.attributes={UMLModel_ReplyAction_replyToCall}

# UMLModel_SequenceNode class attributes and methods

# UMLModel_SignalEvent class attributes and methods
UMLModel_SignalEvent_signal: Property = Property(name="signal", type=StringType)
UMLModel_SignalEvent.attributes={UMLModel_SignalEvent_signal}

# UMLModel_StateInvariant class attributes and methods

# UMLModel_StartClassifierBehaviorAction class attributes and methods

# UMLModel_SendObjectAction class attributes and methods

# UMLModel_Realization class attributes and methods

# UMLModel_Region class attributes and methods
UMLModel_Region_state: Property = Property(name="state", type=StringType)
UMLModel_Region_extendedRegion: Property = Property(name="extendedRegion", type=StringType)
UMLModel_Region_stateMachine: Property = Property(name="stateMachine", type=StringType)
UMLModel_Region.attributes={UMLModel_Region_state, UMLModel_Region_extendedRegion, UMLModel_Region_stateMachine}

# UMLModel_Vertex class attributes and methods
UMLModel_Vertex_incoming: Property = Property(name="incoming", type=StringType)
UMLModel_Vertex_outgoing: Property = Property(name="outgoing", type=StringType)
UMLModel_Vertex_container: Property = Property(name="container", type=StringType)
UMLModel_Vertex.attributes={UMLModel_Vertex_incoming, UMLModel_Vertex_container, UMLModel_Vertex_outgoing}

# UMLModel_Transition class attributes and methods
UMLModel_Transition_kind: Property = Property(name="kind", type=StringType)
UMLModel_Transition_container: Property = Property(name="container", type=StringType)
UMLModel_Transition_redefinedTransition: Property = Property(name="redefinedTransition", type=StringType)
UMLModel_Transition_guard: Property = Property(name="guard", type=StringType)
UMLModel_Transition_target: Property = Property(name="target", type=StringType)
UMLModel_Transition_source: Property = Property(name="source", type=StringType)
UMLModel_Transition.attributes={UMLModel_Transition_guard, UMLModel_Transition_kind, UMLModel_Transition_source, UMLModel_Transition_target, UMLModel_Transition_container, UMLModel_Transition_redefinedTransition}

# UMLModel_SendSignalAction class attributes and methods
UMLModel_SendSignalAction_signal: Property = Property(name="signal", type=StringType)
UMLModel_SendSignalAction.attributes={UMLModel_SendSignalAction_signal}

# UMLModel_SendSignalEvent class attributes and methods
UMLModel_SendSignalEvent_signal: Property = Property(name="signal", type=StringType)
UMLModel_SendSignalEvent.attributes={UMLModel_SendSignalEvent_signal}

# UMLModel_StructuralFeature class attributes and methods
UMLModel_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
UMLModel_StructuralFeature.attributes={UMLModel_StructuralFeature_isReadOnly}

# UMLModel_StructuralFeatureAction class attributes and methods
UMLModel_StructuralFeatureAction_structuralFeature: Property = Property(name="structuralFeature", type=StringType)
UMLModel_StructuralFeatureAction.attributes={UMLModel_StructuralFeatureAction_structuralFeature}

# UMLModel_Signal class attributes and methods

# UMLModel_State class attributes and methods
UMLModel_State_isComposite: Property = Property(name="isComposite", type=StringType)
UMLModel_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
UMLModel_State_isSimple: Property = Property(name="isSimple", type=StringType)
UMLModel_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
UMLModel_State_submachine: Property = Property(name="submachine", type=StringType)
UMLModel_State_redefinedState: Property = Property(name="redefinedState", type=StringType)
UMLModel_State.attributes={UMLModel_State_isComposite, UMLModel_State_isSimple, UMLModel_State_isOrthogonal, UMLModel_State_isSubmachineState, UMLModel_State_redefinedState, UMLModel_State_submachine}

# Expression class attributes and methods

# UMLModel_StructuredActivityNode class attributes and methods
UMLModel_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=StringType)
UMLModel_StructuredActivityNode.attributes={UMLModel_StructuredActivityNode_mustIsolate}

# UMLModel_StateMachine class attributes and methods
UMLModel_StateMachine_submachineState: Property = Property(name="submachineState", type=StringType)
UMLModel_StateMachine_extendedStateMachine: Property = Property(name="extendedStateMachine", type=StringType)
UMLModel_StateMachine.attributes={UMLModel_StateMachine_extendedStateMachine, UMLModel_StateMachine_submachineState}

# UMLModel_StructuredClassifier class attributes and methods
UMLModel_StructuredClassifier_part: Property = Property(name="part", type=StringType)
UMLModel_StructuredClassifier_role: Property = Property(name="role", type=StringType)
UMLModel_StructuredClassifier.attributes={UMLModel_StructuredClassifier_role, UMLModel_StructuredClassifier_part}

# UMLModel_TemplateParameter class attributes and methods
UMLModel_TemplateParameter_signature: Property = Property(name="signature", type=StringType)
UMLModel_TemplateParameter_parameteredElement: Property = Property(name="parameteredElement", type=StringType)
UMLModel_TemplateParameter_default: Property = Property(name="default", type=StringType)
UMLModel_TemplateParameter.attributes={UMLModel_TemplateParameter_default, UMLModel_TemplateParameter_parameteredElement, UMLModel_TemplateParameter_signature}

# UMLModel_TestIdentityAction class attributes and methods

# UMLModel_Stereotype class attributes and methods

# UMLModel_TemplateableElement class attributes and methods

# UMLModel_TemplateBinding class attributes and methods
UMLModel_TemplateBinding_signature: Property = Property(name="signature", type=StringType)
UMLModel_TemplateBinding_boundElement: Property = Property(name="boundElement", type=StringType)
UMLModel_TemplateBinding.attributes={UMLModel_TemplateBinding_boundElement, UMLModel_TemplateBinding_signature}

# UMLModel_TemplateSignature class attributes and methods
UMLModel_TemplateSignature_template: Property = Property(name="template", type=StringType)
UMLModel_TemplateSignature_parameter: Property = Property(name="parameter", type=StringType)
UMLModel_TemplateSignature.attributes={UMLModel_TemplateSignature_parameter, UMLModel_TemplateSignature_template}

# UMLModel_TemplateParameterSubstitution class attributes and methods
UMLModel_TemplateParameterSubstitution_formal: Property = Property(name="formal", type=StringType)
UMLModel_TemplateParameterSubstitution_actual: Property = Property(name="actual", type=StringType)
UMLModel_TemplateParameterSubstitution_templateBinding: Property = Property(name="templateBinding", type=StringType)
UMLModel_TemplateParameterSubstitution.attributes={UMLModel_TemplateParameterSubstitution_formal, UMLModel_TemplateParameterSubstitution_actual, UMLModel_TemplateParameterSubstitution_templateBinding}

# UMLModel_TimeConstraint class attributes and methods
UMLModel_TimeConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
UMLModel_TimeConstraint.attributes={UMLModel_TimeConstraint_firstEvent}

# UMLModel_TimeEvent class attributes and methods
UMLModel_TimeEvent_isRelative: Property = Property(name="isRelative", type=StringType)
UMLModel_TimeEvent.attributes={UMLModel_TimeEvent_isRelative}

# UMLModel_TimeExpression class attributes and methods
UMLModel_TimeExpression_expr: Property = Property(name="expr", type=StringType)
UMLModel_TimeExpression_observation: Property = Property(name="observation", type=StringType)
UMLModel_TimeExpression.attributes={UMLModel_TimeExpression_observation, UMLModel_TimeExpression_expr}

# UMLModel_TimeInterval class attributes and methods

# UMLModel_TimeObservation class attributes and methods
UMLModel_TimeObservation_event: Property = Property(name="event", type=StringType)
UMLModel_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
UMLModel_TimeObservation.attributes={UMLModel_TimeObservation_event, UMLModel_TimeObservation_firstEvent}

# UMLModel_ValuePin class attributes and methods

# UMLModel_ValueSpecificationAction class attributes and methods

# UMLModel_TypedElement class attributes and methods
UMLModel_TypedElement_type: Property = Property(name="type", type=StringType)
UMLModel_TypedElement.attributes={UMLModel_TypedElement_type}

# UMLModel_Type class attributes and methods
UMLModel_Type_package: Property = Property(name="package", type=StringType)
UMLModel_Type.attributes={UMLModel_Type_package}

# UMLModel_UnmarshallAction class attributes and methods
UMLModel_UnmarshallAction_unmarshallType: Property = Property(name="unmarshallType", type=StringType)
UMLModel_UnmarshallAction.attributes={UMLModel_UnmarshallAction_unmarshallType}

# UMLModel_UMLBase class attributes and methods
UMLModel_UMLBase_umlID: Property = Property(name="umlID", type=StringType)
UMLModel_UMLBase.attributes={UMLModel_UMLBase_umlID}

# EObject class attributes and methods

# UMLModel_Usage class attributes and methods

# UMLModel_VariableAction class attributes and methods
UMLModel_VariableAction_variable: Property = Property(name="variable", type=StringType)
UMLModel_VariableAction.attributes={UMLModel_VariableAction_variable}

# UMLModel_WriteLinkAction class attributes and methods

# UMLModel_WriteVariableAction class attributes and methods

# UMLModel_WriteStructuralFeatureAction class attributes and methods

# Relationships
mapping0: BinaryAssociation = BinaryAssociation(
    name="mapping0",
    ends={
        Property(name="UMLModel_OpaqueExpression", type=UMLModel_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Abstraction", type=UMLModel_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnInformation1: BinaryAssociation = BinaryAssociation(
    name="returnInformation1",
    ends={
        Property(name="UMLModel_OutputPin", type=UMLModel_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_AcceptCallAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result2: BinaryAssociation = BinaryAssociation(
    name="result2",
    ends={
        Property(name="UMLModel_OutputPin3", type=UMLModel_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_AcceptEventAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger4: BinaryAssociation = BinaryAssociation(
    name="trigger4",
    ends={
        Property(name="UMLModel_Trigger", type=UMLModel_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_AcceptEventAction5", type=UMLModel_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
localPrecondition6: BinaryAssociation = BinaryAssociation(
    name="localPrecondition6",
    ends={
        Property(name="UMLModel_Constraint", type=UMLModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Action", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition7: BinaryAssociation = BinaryAssociation(
    name="localPostcondition7",
    ends={
        Property(name="UMLModel_Constraint9", type=UMLModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Action8", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromAction10: BinaryAssociation = BinaryAssociation(
    name="fromAction10",
    ends={
        Property(name="UMLModel_Action11", type=UMLModel_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ActionInputPin", type=UMLModel_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable12: BinaryAssociation = BinaryAssociation(
    name="variable12",
    ends={
        Property(name="UMLModel_Variable", type=UMLModel_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Activity", type=UMLModel_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node13: BinaryAssociation = BinaryAssociation(
    name="node13",
    ends={
        Property(name="UMLModel_ActivityNode", type=UMLModel_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Activity14", type=UMLModel_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge15: BinaryAssociation = BinaryAssociation(
    name="edge15",
    ends={
        Property(name="UMLModel_ActivityEdge", type=UMLModel_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Activity16", type=UMLModel_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group17: BinaryAssociation = BinaryAssociation(
    name="group17",
    ends={
        Property(name="UMLModel_ActivityGroup", type=UMLModel_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Activity18", type=UMLModel_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard19: BinaryAssociation = BinaryAssociation(
    name="guard19",
    ends={
        Property(name="UMLModel_ValueSpecification", type=UMLModel_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ActivityEdge20", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
weight21: BinaryAssociation = BinaryAssociation(
    name="weight21",
    ends={
        Property(name="UMLModel_ValueSpecification23", type=UMLModel_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ActivityEdge22", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containedEdge24: BinaryAssociation = BinaryAssociation(
    name="containedEdge24",
    ends={
        Property(name="UMLModel_ActivityEdge26", type=UMLModel_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ActivityGroup25", type=UMLModel_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedNode27: BinaryAssociation = BinaryAssociation(
    name="containedNode27",
    ends={
        Property(name="UMLModel_ActivityNode29", type=UMLModel_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ActivityGroup28", type=UMLModel_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
insertAt30: BinaryAssociation = BinaryAssociation(
    name="insertAt30",
    ends={
        Property(name="UMLModel_InputPin", type=UMLModel_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_AddStructuralFeatureValueAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt31: BinaryAssociation = BinaryAssociation(
    name="insertAt31",
    ends={
        Property(name="UMLModel_InputPin32", type=UMLModel_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_AddVariableValueAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedArtifact34: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact34",
    ends={
        Property(name="UMLModel_Artifact", type=UMLModel_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Artifact33", type=UMLModel_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation35: BinaryAssociation = BinaryAssociation(
    name="manifestation35",
    ends={
        Property(name="UMLModel_Manifestation", type=UMLModel_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Artifact36", type=UMLModel_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation37: BinaryAssociation = BinaryAssociation(
    name="ownedOperation37",
    ends={
        Property(name="UMLModel_Operation", type=UMLModel_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Artifact38", type=UMLModel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute39: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute39",
    ends={
        Property(name="UMLModel_Property", type=UMLModel_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Artifact40", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEnd41: BinaryAssociation = BinaryAssociation(
    name="ownedEnd41",
    ends={
        Property(name="UMLModel_Property42", type=UMLModel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Association", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter43: BinaryAssociation = BinaryAssociation(
    name="ownedParameter43",
    ends={
        Property(name="UMLModel_Parameter", type=UMLModel_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Behavior", type=UMLModel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterSet44: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet44",
    ends={
        Property(name="UMLModel_ParameterSet", type=UMLModel_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Behavior45", type=UMLModel_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter46: BinaryAssociation = BinaryAssociation(
    name="ownedParameter46",
    ends={
        Property(name="UMLModel_Parameter47", type=UMLModel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_BehavioralFeature", type=UMLModel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameterSet48: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet48",
    ends={
        Property(name="UMLModel_ParameterSet50", type=UMLModel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_BehavioralFeature49", type=UMLModel_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior51: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior51",
    ends={
        Property(name="UMLModel_Behavior52", type=UMLModel_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_BehavioredClassifier", type=UMLModel_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceRealization53: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization53",
    ends={
        Property(name="UMLModel_InterfaceRealization", type=UMLModel_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_BehavioredClassifier54", type=UMLModel_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTrigger55: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger55",
    ends={
        Property(name="UMLModel_Trigger57", type=UMLModel_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_BehavioredClassifier56", type=UMLModel_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target60: BinaryAssociation = BinaryAssociation(
    name="target60",
    ends={
        Property(name="UMLModel_InputPin61", type=UMLModel_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CallOperationAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
changeExpression62: BinaryAssociation = BinaryAssociation(
    name="changeExpression62",
    ends={
        Property(name="UMLModel_ValueSpecification63", type=UMLModel_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ChangeEvent", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nestedClassifier64: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier64",
    ends={
        Property(name="UMLModel_Classifier", type=UMLModel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Class", type=UMLModel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation65: BinaryAssociation = BinaryAssociation(
    name="ownedOperation65",
    ends={
        Property(name="UMLModel_Operation67", type=UMLModel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Class66", type=UMLModel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception68: BinaryAssociation = BinaryAssociation(
    name="ownedReception68",
    ends={
        Property(name="UMLModel_Reception", type=UMLModel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Class69", type=UMLModel_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization70: BinaryAssociation = BinaryAssociation(
    name="generalization70",
    ends={
        Property(name="UMLModel_Generalization", type=UMLModel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Classifier71", type=UMLModel_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution72: BinaryAssociation = BinaryAssociation(
    name="substitution72",
    ends={
        Property(name="UMLModel_Substitution", type=UMLModel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Classifier73", type=UMLModel_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result58: BinaryAssociation = BinaryAssociation(
    name="result58",
    ends={
        Property(name="UMLModel_OutputPin59", type=UMLModel_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CallAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUseCase76: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase76",
    ends={
        Property(name="UMLModel_UseCase", type=UMLModel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Classifier77", type=UMLModel_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object78: BinaryAssociation = BinaryAssociation(
    name="object78",
    ends={
        Property(name="UMLModel_InputPin79", type=UMLModel_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ClearAssociationAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
roleBinding80: BinaryAssociation = BinaryAssociation(
    name="roleBinding80",
    ends={
        Property(name="UMLModel_Dependency", type=UMLModel_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CollaborationUse81", type=UMLModel_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement82: BinaryAssociation = BinaryAssociation(
    name="packagedElement82",
    ends={
        Property(name="UMLModel_PackageableElement", type=UMLModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Component", type=UMLModel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realization83: BinaryAssociation = BinaryAssociation(
    name="realization83",
    ends={
        Property(name="UMLModel_ComponentRealization", type=UMLModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Component84", type=UMLModel_ComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationUse74: BinaryAssociation = BinaryAssociation(
    name="collaborationUse74",
    ends={
        Property(name="UMLModel_CollaborationUse", type=UMLModel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Classifier75", type=UMLModel_CollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand85: BinaryAssociation = BinaryAssociation(
    name="operand85",
    ends={
        Property(name="UMLModel_InteractionOperand", type=UMLModel_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CombinedFragment", type=UMLModel_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cfragmentGate86: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate86",
    ends={
        Property(name="UMLModel_Gate", type=UMLModel_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CombinedFragment87", type=UMLModel_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause88: BinaryAssociation = BinaryAssociation(
    name="clause88",
    ends={
        Property(name="UMLModel_Clause", type=UMLModel_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ConditionalNode", type=UMLModel_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result89: BinaryAssociation = BinaryAssociation(
    name="result89",
    ends={
        Property(name="UMLModel_OutputPin91", type=UMLModel_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ConditionalNode90", type=UMLModel_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification92: BinaryAssociation = BinaryAssociation(
    name="specification92",
    ends={
        Property(name="UMLModel_ValueSpecification94", type=UMLModel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Constraint93", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result96: BinaryAssociation = BinaryAssociation(
    name="result96",
    ends={
        Property(name="UMLModel_OutputPin97", type=UMLModel_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CreateLinkObjectAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result98: BinaryAssociation = BinaryAssociation(
    name="result98",
    ends={
        Property(name="UMLModel_OutputPin99", type=UMLModel_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_CreateObjectAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target108: BinaryAssociation = BinaryAssociation(
    name="target108",
    ends={
        Property(name="UMLModel_InputPin109", type=UMLModel_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_DestroyObjectAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end95: BinaryAssociation = BinaryAssociation(
    name="end95",
    ends={
        Property(name="UMLModel_ConnectorEnd", type=UMLModel_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Connector", type=UMLModel_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
ownedAttribute100: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute100",
    ends={
        Property(name="UMLModel_Property101", type=UMLModel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_DataType", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation102: BinaryAssociation = BinaryAssociation(
    name="ownedOperation102",
    ends={
        Property(name="UMLModel_Operation104", type=UMLModel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_DataType103", type=UMLModel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployment105: BinaryAssociation = BinaryAssociation(
    name="deployment105",
    ends={
        Property(name="UMLModel_Deployment", type=UMLModel_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_DeploymentTarget", type=UMLModel_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration106: BinaryAssociation = BinaryAssociation(
    name="configuration106",
    ends={
        Property(name="UMLModel_DeploymentSpecification", type=UMLModel_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Deployment107", type=UMLModel_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral113: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral113",
    ends={
        Property(name="UMLModel_EnumerationLiteral", type=UMLModel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Enumeration", type=UMLModel_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler114: BinaryAssociation = BinaryAssociation(
    name="handler114",
    ends={
        Property(name="UMLModel_ExceptionHandler", type=UMLModel_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ExecutableNode", type=UMLModel_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComment110: BinaryAssociation = BinaryAssociation(
    name="ownedComment110",
    ends={
        Property(name="UMLModel_Comment", type=UMLModel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Element", type=UMLModel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement111: BinaryAssociation = BinaryAssociation(
    name="importedElement111",
    ends={
        Property(name="UMLModel_PackageableElement112", type=UMLModel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ElementImport", type=UMLModel_PackageableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand117: BinaryAssociation = BinaryAssociation(
    name="operand117",
    ends={
        Property(name="UMLModel_ValueSpecification118", type=UMLModel_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Expression", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition115: BinaryAssociation = BinaryAssociation(
    name="condition115",
    ends={
        Property(name="UMLModel_Constraint116", type=UMLModel_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Extend", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAttribute119: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute119",
    ends={
        Property(name="UMLModel_Property120", type=UMLModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interface", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation121: BinaryAssociation = BinaryAssociation(
    name="ownedOperation121",
    ends={
        Property(name="UMLModel_Operation123", type=UMLModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interface122", type=UMLModel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier124: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier124",
    ends={
        Property(name="UMLModel_Classifier126", type=UMLModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interface125", type=UMLModel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception127: BinaryAssociation = BinaryAssociation(
    name="ownedReception127",
    ends={
        Property(name="UMLModel_Reception129", type=UMLModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interface128", type=UMLModel_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol130: BinaryAssociation = BinaryAssociation(
    name="protocol130",
    ends={
        Property(name="UMLModel_ProtocolStateMachine", type=UMLModel_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interface131", type=UMLModel_ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument136: BinaryAssociation = BinaryAssociation(
    name="argument136",
    ends={
        Property(name="UMLModel_InputPin137", type=UMLModel_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InvocationAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slot132: BinaryAssociation = BinaryAssociation(
    name="slot132",
    ends={
        Property(name="UMLModel_Slot", type=UMLModel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InstanceSpecification", type=UMLModel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification133: BinaryAssociation = BinaryAssociation(
    name="specification133",
    ends={
        Property(name="UMLModel_ValueSpecification135", type=UMLModel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InstanceSpecification134", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualGate151: BinaryAssociation = BinaryAssociation(
    name="actualGate151",
    ends={
        Property(name="UMLModel_Gate152", type=UMLModel_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionUse", type=UMLModel_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument153: BinaryAssociation = BinaryAssociation(
    name="argument153",
    ends={
        Property(name="UMLModel_Action155", type=UMLModel_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionUse154", type=UMLModel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard156: BinaryAssociation = BinaryAssociation(
    name="guard156",
    ends={
        Property(name="UMLModel_InteractionConstraint", type=UMLModel_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionOperand157", type=UMLModel_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragment158: BinaryAssociation = BinaryAssociation(
    name="fragment158",
    ends={
        Property(name="UMLModel_InteractionFragment160", type=UMLModel_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionOperand159", type=UMLModel_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minint161: BinaryAssociation = BinaryAssociation(
    name="minint161",
    ends={
        Property(name="UMLModel_ValueSpecification163", type=UMLModel_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionConstraint162", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxint164: BinaryAssociation = BinaryAssociation(
    name="maxint164",
    ends={
        Property(name="UMLModel_ValueSpecification166", type=UMLModel_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionConstraint165", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lifeline138: BinaryAssociation = BinaryAssociation(
    name="lifeline138",
    ends={
        Property(name="UMLModel_Lifeline", type=UMLModel_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interaction", type=UMLModel_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragment139: BinaryAssociation = BinaryAssociation(
    name="fragment139",
    ends={
        Property(name="UMLModel_InteractionFragment", type=UMLModel_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interaction140", type=UMLModel_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action141: BinaryAssociation = BinaryAssociation(
    name="action141",
    ends={
        Property(name="UMLModel_Action143", type=UMLModel_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interaction142", type=UMLModel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate144: BinaryAssociation = BinaryAssociation(
    name="formalGate144",
    ends={
        Property(name="UMLModel_Gate146", type=UMLModel_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interaction145", type=UMLModel_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message147: BinaryAssociation = BinaryAssociation(
    name="message147",
    ends={
        Property(name="UMLModel_Message", type=UMLModel_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Interaction148", type=UMLModel_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalOrdering149: BinaryAssociation = BinaryAssociation(
    name="generalOrdering149",
    ends={
        Property(name="UMLModel_GeneralOrdering", type=UMLModel_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_InteractionFragment150", type=UMLModel_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinSpec167: BinaryAssociation = BinaryAssociation(
    name="joinSpec167",
    ends={
        Property(name="UMLModel_ValueSpecification168", type=UMLModel_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_JoinNode", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selector169: BinaryAssociation = BinaryAssociation(
    name="selector169",
    ends={
        Property(name="UMLModel_ValueSpecification171", type=UMLModel_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Lifeline170", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result178: BinaryAssociation = BinaryAssociation(
    name="result178",
    ends={
        Property(name="UMLModel_OutputPin179", type=UMLModel_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_LoopNode", type=UMLModel_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariableInput180: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput180",
    ends={
        Property(name="UMLModel_InputPin182", type=UMLModel_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_LoopNode181", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endData172: BinaryAssociation = BinaryAssociation(
    name="endData172",
    ends={
        Property(name="UMLModel_LinkEndData", type=UMLModel_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_LinkAction", type=UMLModel_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue173: BinaryAssociation = BinaryAssociation(
    name="inputValue173",
    ends={
        Property(name="UMLModel_InputPin175", type=UMLModel_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_LinkAction174", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
qualifier176: BinaryAssociation = BinaryAssociation(
    name="qualifier176",
    ends={
        Property(name="UMLModel_QualifierValue", type=UMLModel_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_LinkEndData177", type=UMLModel_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument183: BinaryAssociation = BinaryAssociation(
    name="argument183",
    ends={
        Property(name="UMLModel_ValueSpecification185", type=UMLModel_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Message184", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport192: BinaryAssociation = BinaryAssociation(
    name="elementImport192",
    ends={
        Property(name="UMLModel_ElementImport193", type=UMLModel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Namespace", type=UMLModel_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport194: BinaryAssociation = BinaryAssociation(
    name="packageImport194",
    ends={
        Property(name="UMLModel_PackageImport", type=UMLModel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Namespace195", type=UMLModel_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule196: BinaryAssociation = BinaryAssociation(
    name="ownedRule196",
    ends={
        Property(name="UMLModel_Constraint198", type=UMLModel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Namespace197", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedNode200: BinaryAssociation = BinaryAssociation(
    name="nestedNode200",
    ends={
        Property(name="UMLModel_Node", type=UMLModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Node199", type=UMLModel_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperValue186: BinaryAssociation = BinaryAssociation(
    name="upperValue186",
    ends={
        Property(name="UMLModel_ValueSpecification187", type=UMLModel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_MultiplicityElement", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue188: BinaryAssociation = BinaryAssociation(
    name="lowerValue188",
    ends={
        Property(name="UMLModel_ValueSpecification190", type=UMLModel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_MultiplicityElement189", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameExpression191: BinaryAssociation = BinaryAssociation(
    name="nameExpression191",
    ends={
        Property(name="UMLModel_StringExpression", type=UMLModel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_NamedElement", type=UMLModel_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValue201: BinaryAssociation = BinaryAssociation(
    name="inputValue201",
    ends={
        Property(name="UMLModel_InputPin202", type=UMLModel_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_OpaqueAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputValue203: BinaryAssociation = BinaryAssociation(
    name="outputValue203",
    ends={
        Property(name="UMLModel_OutputPin205", type=UMLModel_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_OpaqueAction204", type=UMLModel_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue208: BinaryAssociation = BinaryAssociation(
    name="defaultValue208",
    ends={
        Property(name="UMLModel_ValueSpecification210", type=UMLModel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Parameter209", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageMerge211: BinaryAssociation = BinaryAssociation(
    name="packageMerge211",
    ends={
        Property(name="UMLModel_PackageMerge", type=UMLModel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Package", type=UMLModel_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperBound206: BinaryAssociation = BinaryAssociation(
    name="upperBound206",
    ends={
        Property(name="UMLModel_ValueSpecification207", type=UMLModel_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ObjectNode", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition220: BinaryAssociation = BinaryAssociation(
    name="condition220",
    ends={
        Property(name="UMLModel_Constraint222", type=UMLModel_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ParameterSet221", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement212: BinaryAssociation = BinaryAssociation(
    name="packagedElement212",
    ends={
        Property(name="UMLModel_PackageableElement214", type=UMLModel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Package213", type=UMLModel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
profileApplication215: BinaryAssociation = BinaryAssociation(
    name="profileApplication215",
    ends={
        Property(name="UMLModel_ProfileApplication", type=UMLModel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Package216", type=UMLModel_ProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedPackage217: BinaryAssociation = BinaryAssociation(
    name="importedPackage217",
    ends={
        Property(name="UMLModel_PackageableElement219", type=UMLModel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_PackageImport218", type=UMLModel_PackageableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue223: BinaryAssociation = BinaryAssociation(
    name="defaultValue223",
    ends={
        Property(name="UMLModel_ValueSpecification225", type=UMLModel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Property224", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier227: BinaryAssociation = BinaryAssociation(
    name="qualifier227",
    ends={
        Property(name="UMLModel_Property228", type=UMLModel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Property226", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformance229: BinaryAssociation = BinaryAssociation(
    name="conformance229",
    ends={
        Property(name="UMLModel_ProtocolConformance", type=UMLModel_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ProtocolStateMachine230", type=UMLModel_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception231: BinaryAssociation = BinaryAssociation(
    name="exception231",
    ends={
        Property(name="UMLModel_InputPin232", type=UMLModel_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_RaiseExceptionAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object233: BinaryAssociation = BinaryAssociation(
    name="object233",
    ends={
        Property(name="UMLModel_InputPin234", type=UMLModel_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReclassifyObjectAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object249: BinaryAssociation = BinaryAssociation(
    name="object249",
    ends={
        Property(name="UMLModel_InputPin250", type=UMLModel_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadLinkObjectEndQualifierAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result251: BinaryAssociation = BinaryAssociation(
    name="result251",
    ends={
        Property(name="UMLModel_OutputPin253", type=UMLModel_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadLinkObjectEndQualifierAction252", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result254: BinaryAssociation = BinaryAssociation(
    name="result254",
    ends={
        Property(name="UMLModel_OutputPin255", type=UMLModel_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadSelfAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result256: BinaryAssociation = BinaryAssociation(
    name="result256",
    ends={
        Property(name="UMLModel_OutputPin257", type=UMLModel_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadStructuralFeatureAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result258: BinaryAssociation = BinaryAssociation(
    name="result258",
    ends={
        Property(name="UMLModel_OutputPin259", type=UMLModel_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadVariableAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result235: BinaryAssociation = BinaryAssociation(
    name="result235",
    ends={
        Property(name="UMLModel_OutputPin236", type=UMLModel_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadIsClassifiedObjectAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object237: BinaryAssociation = BinaryAssociation(
    name="object237",
    ends={
        Property(name="UMLModel_InputPin239", type=UMLModel_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadIsClassifiedObjectAction238", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result240: BinaryAssociation = BinaryAssociation(
    name="result240",
    ends={
        Property(name="UMLModel_OutputPin241", type=UMLModel_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadExtentAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result242: BinaryAssociation = BinaryAssociation(
    name="result242",
    ends={
        Property(name="UMLModel_OutputPin243", type=UMLModel_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadLinkAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object244: BinaryAssociation = BinaryAssociation(
    name="object244",
    ends={
        Property(name="UMLModel_InputPin245", type=UMLModel_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadLinkObjectEndAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result246: BinaryAssociation = BinaryAssociation(
    name="result246",
    ends={
        Property(name="UMLModel_OutputPin248", type=UMLModel_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReadLinkObjectEndAction247", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
removeAt270: BinaryAssociation = BinaryAssociation(
    name="removeAt270",
    ends={
        Property(name="UMLModel_InputPin271", type=UMLModel_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_RemoveVariableValueAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt272: BinaryAssociation = BinaryAssociation(
    name="removeAt272",
    ends={
        Property(name="UMLModel_InputPin273", type=UMLModel_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_RemoveStructuralFeatureValueAction", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result260: BinaryAssociation = BinaryAssociation(
    name="result260",
    ends={
        Property(name="UMLModel_OutputPin261", type=UMLModel_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReduceAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection262: BinaryAssociation = BinaryAssociation(
    name="collection262",
    ends={
        Property(name="UMLModel_InputPin264", type=UMLModel_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReduceAction263", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnInformation265: BinaryAssociation = BinaryAssociation(
    name="returnInformation265",
    ends={
        Property(name="UMLModel_InputPin266", type=UMLModel_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReplyAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue267: BinaryAssociation = BinaryAssociation(
    name="replyValue267",
    ends={
        Property(name="UMLModel_InputPin269", type=UMLModel_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ReplyAction268", type=UMLModel_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executableNode279: BinaryAssociation = BinaryAssociation(
    name="executableNode279",
    ends={
        Property(name="UMLModel_ExecutableNode280", type=UMLModel_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_SequenceNode", type=UMLModel_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value281: BinaryAssociation = BinaryAssociation(
    name="value281",
    ends={
        Property(name="UMLModel_ValueSpecification283", type=UMLModel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Slot282", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariant284: BinaryAssociation = BinaryAssociation(
    name="invariant284",
    ends={
        Property(name="UMLModel_Constraint285", type=UMLModel_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StateInvariant", type=UMLModel_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object286: BinaryAssociation = BinaryAssociation(
    name="object286",
    ends={
        Property(name="UMLModel_InputPin287", type=UMLModel_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StartClassifierBehaviorAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subvertex274: BinaryAssociation = BinaryAssociation(
    name="subvertex274",
    ends={
        Property(name="UMLModel_Vertex", type=UMLModel_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Region", type=UMLModel_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition275: BinaryAssociation = BinaryAssociation(
    name="transition275",
    ends={
        Property(name="UMLModel_Transition", type=UMLModel_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Region276", type=UMLModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target277: BinaryAssociation = BinaryAssociation(
    name="target277",
    ends={
        Property(name="UMLModel_InputPin278", type=UMLModel_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_SendSignalAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object304: BinaryAssociation = BinaryAssociation(
    name="object304",
    ends={
        Property(name="UMLModel_InputPin305", type=UMLModel_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuralFeatureAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedAttribute306: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute306",
    ends={
        Property(name="UMLModel_Property307", type=UMLModel_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Signal", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target288: BinaryAssociation = BinaryAssociation(
    name="target288",
    ends={
        Property(name="UMLModel_InputPin289", type=UMLModel_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_SendObjectAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request290: BinaryAssociation = BinaryAssociation(
    name="request290",
    ends={
        Property(name="UMLModel_InputPin292", type=UMLModel_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_SendObjectAction291", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subExpression294: BinaryAssociation = BinaryAssociation(
    name="subExpression294",
    ends={
        Property(name="UMLModel_StringExpression295", type=UMLModel_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StringExpression293", type=UMLModel_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable296: BinaryAssociation = BinaryAssociation(
    name="variable296",
    ends={
        Property(name="UMLModel_Variable297", type=UMLModel_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuredActivityNode", type=UMLModel_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge298: BinaryAssociation = BinaryAssociation(
    name="edge298",
    ends={
        Property(name="UMLModel_ActivityEdge300", type=UMLModel_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuredActivityNode299", type=UMLModel_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node301: BinaryAssociation = BinaryAssociation(
    name="node301",
    ends={
        Property(name="UMLModel_ActivityNode303", type=UMLModel_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuredActivityNode302", type=UMLModel_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity320: BinaryAssociation = BinaryAssociation(
    name="doActivity320",
    ends={
        Property(name="UMLModel_Behavior322", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State321", type=UMLModel_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTrigger323: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger323",
    ends={
        Property(name="UMLModel_Trigger325", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State324", type=UMLModel_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region326: BinaryAssociation = BinaryAssociation(
    name="region326",
    ends={
        Property(name="UMLModel_Region328", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State327", type=UMLModel_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region329: BinaryAssociation = BinaryAssociation(
    name="region329",
    ends={
        Property(name="UMLModel_Region330", type=UMLModel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StateMachine", type=UMLModel_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint331: BinaryAssociation = BinaryAssociation(
    name="connectionPoint331",
    ends={
        Property(name="UMLModel_Pseudostate333", type=UMLModel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StateMachine332", type=UMLModel_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute334: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute334",
    ends={
        Property(name="UMLModel_Property335", type=UMLModel_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuredClassifier", type=UMLModel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection308: BinaryAssociation = BinaryAssociation(
    name="connection308",
    ends={
        Property(name="UMLModel_ConnectionPointReference", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State", type=UMLModel_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint309: BinaryAssociation = BinaryAssociation(
    name="connectionPoint309",
    ends={
        Property(name="UMLModel_Pseudostate", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State310", type=UMLModel_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateInvariant311: BinaryAssociation = BinaryAssociation(
    name="stateInvariant311",
    ends={
        Property(name="UMLModel_Constraint313", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State312", type=UMLModel_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry314: BinaryAssociation = BinaryAssociation(
    name="entry314",
    ends={
        Property(name="UMLModel_Behavior316", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State315", type=UMLModel_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit317: BinaryAssociation = BinaryAssociation(
    name="exit317",
    ends={
        Property(name="UMLModel_Behavior319", type=UMLModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_State318", type=UMLModel_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter345: BinaryAssociation = BinaryAssociation(
    name="ownedParameter345",
    ends={
        Property(name="UMLModel_TemplateParameter", type=UMLModel_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateSignature346", type=UMLModel_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameteredElement347: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement347",
    ends={
        Property(name="UMLModel_ParameterableElement", type=UMLModel_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateParameter348", type=UMLModel_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDefault349: BinaryAssociation = BinaryAssociation(
    name="ownedDefault349",
    ends={
        Property(name="UMLModel_ParameterableElement351", type=UMLModel_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateParameter350", type=UMLModel_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedActual352: BinaryAssociation = BinaryAssociation(
    name="ownedActual352",
    ends={
        Property(name="UMLModel_ParameterableElement354", type=UMLModel_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateParameterSubstitution353", type=UMLModel_ParameterableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConnector336: BinaryAssociation = BinaryAssociation(
    name="ownedConnector336",
    ends={
        Property(name="UMLModel_Connector338", type=UMLModel_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_StructuredClassifier337", type=UMLModel_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icon339: BinaryAssociation = BinaryAssociation(
    name="icon339",
    ends={
        Property(name="UMLModel_Image", type=UMLModel_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Stereotype", type=UMLModel_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateBinding340: BinaryAssociation = BinaryAssociation(
    name="templateBinding340",
    ends={
        Property(name="UMLModel_TemplateBinding", type=UMLModel_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateableElement", type=UMLModel_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature341: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature341",
    ends={
        Property(name="UMLModel_TemplateSignature", type=UMLModel_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateableElement342", type=UMLModel_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterSubstitution343: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution343",
    ends={
        Property(name="UMLModel_TemplateParameterSubstitution", type=UMLModel_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TemplateBinding344", type=UMLModel_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effect365: BinaryAssociation = BinaryAssociation(
    name="effect365",
    ends={
        Property(name="UMLModel_Behavior367", type=UMLModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Transition366", type=UMLModel_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger368: BinaryAssociation = BinaryAssociation(
    name="trigger368",
    ends={
        Property(name="UMLModel_Trigger370", type=UMLModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_Transition369", type=UMLModel_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first355: BinaryAssociation = BinaryAssociation(
    name="first355",
    ends={
        Property(name="UMLModel_InputPin356", type=UMLModel_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TestIdentityAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second357: BinaryAssociation = BinaryAssociation(
    name="second357",
    ends={
        Property(name="UMLModel_InputPin359", type=UMLModel_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TestIdentityAction358", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result360: BinaryAssociation = BinaryAssociation(
    name="result360",
    ends={
        Property(name="UMLModel_OutputPin362", type=UMLModel_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TestIdentityAction361", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
when363: BinaryAssociation = BinaryAssociation(
    name="when363",
    ends={
        Property(name="UMLModel_ValueSpecification364", type=UMLModel_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_TimeEvent", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
include376: BinaryAssociation = BinaryAssociation(
    name="include376",
    ends={
        Property(name="UMLModel_UseCase377", type=UMLModel_Include, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="UMLModel_Include", type=UMLModel_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extend378: BinaryAssociation = BinaryAssociation(
    name="extend378",
    ends={
        Property(name="UMLModel_Extend380", type=UMLModel_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_UseCase379", type=UMLModel_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint381: BinaryAssociation = BinaryAssociation(
    name="extensionPoint381",
    ends={
        Property(name="UMLModel_ExtensionPoint", type=UMLModel_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_UseCase382", type=UMLModel_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value383: BinaryAssociation = BinaryAssociation(
    name="value383",
    ends={
        Property(name="UMLModel_ValueSpecification384", type=UMLModel_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ValuePin", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value385: BinaryAssociation = BinaryAssociation(
    name="value385",
    ends={
        Property(name="UMLModel_ValueSpecification386", type=UMLModel_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ValueSpecificationAction", type=UMLModel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result387: BinaryAssociation = BinaryAssociation(
    name="result387",
    ends={
        Property(name="UMLModel_OutputPin389", type=UMLModel_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_ValueSpecificationAction388", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result371: BinaryAssociation = BinaryAssociation(
    name="result371",
    ends={
        Property(name="UMLModel_OutputPin372", type=UMLModel_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_UnmarshallAction", type=UMLModel_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
object373: BinaryAssociation = BinaryAssociation(
    name="object373",
    ends={
        Property(name="UMLModel_InputPin375", type=UMLModel_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_UnmarshallAction374", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value392: BinaryAssociation = BinaryAssociation(
    name="value392",
    ends={
        Property(name="UMLModel_InputPin393", type=UMLModel_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_WriteStructuralFeatureAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value390: BinaryAssociation = BinaryAssociation(
    name="value390",
    ends={
        Property(name="UMLModel_InputPin391", type=UMLModel_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLModel_WriteVariableAction", type=UMLModel_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_UMLModel_Abstraction_Dependency = Generalization(general=Dependency, specific=UMLModel_Abstraction)
gen_UMLModel_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UMLModel_AcceptCallAction)
gen_UMLModel_AcceptEventAction_Action = Generalization(general=Action, specific=UMLModel_AcceptEventAction)
gen_UMLModel_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=UMLModel_Action)
gen_UMLModel_ActionExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=UMLModel_ActionExecutionSpecification)
gen_UMLModel_ActionInputPin_InputPin = Generalization(general=InputPin, specific=UMLModel_ActionInputPin)
gen_UMLModel_Activity_Behavior = Generalization(general=Behavior, specific=UMLModel_Activity)
gen_UMLModel_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_ActivityEdge)
gen_UMLModel_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=UMLModel_ActivityFinalNode)
gen_UMLModel_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_ActivityNode)
gen_UMLModel_ActivityGroup_Element = Generalization(general=Element, specific=UMLModel_ActivityGroup)
gen_UMLModel_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UMLModel_ActivityParameterNode)
gen_UMLModel_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UMLModel_Actor)
gen_UMLModel_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UMLModel_AddStructuralFeatureValueAction)
gen_UMLModel_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UMLModel_AddVariableValueAction)
gen_UMLModel_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_AnyReceiveEvent)
gen_UMLModel_Artifact_Classifier = Generalization(general=Classifier, specific=UMLModel_Artifact)
gen_UMLModel_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UMLModel_Artifact)
gen_UMLModel_Association_Classifier = Generalization(general=Classifier, specific=UMLModel_Association)
gen_UMLModel_Association_Relationship = Generalization(general=Relationship, specific=UMLModel_Association)
gen_UMLModel_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=UMLModel_ActivityPartition)
gen_UMLModel_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=UMLModel_ActivityPartition)
gen_UMLModel_AssociationClass_Class = Generalization(general=Class_, specific=UMLModel_AssociationClass)
gen_UMLModel_AssociationClass_Association = Generalization(general=Association, specific=UMLModel_AssociationClass)
gen_UMLModel_Behavior_Class = Generalization(general=Class_, specific=UMLModel_Behavior)
gen_UMLModel_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=UMLModel_BehaviorExecutionSpecification)
gen_UMLModel_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UMLModel_BehavioralFeature)
gen_UMLModel_BehavioralFeature_Feature = Generalization(general=Feature, specific=UMLModel_BehavioralFeature)
gen_UMLModel_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UMLModel_BehavioredClassifier)
gen_UMLModel_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UMLModel_BroadcastSignalAction)
gen_UMLModel_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UMLModel_CallAction)
gen_UMLModel_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UMLModel_CallBehaviorAction)
gen_UMLModel_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_CallEvent)
gen_UMLModel_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UMLModel_CallOperationAction)
gen_UMLModel_ChangeEvent_Event = Generalization(general=Event, specific=UMLModel_ChangeEvent)
gen_UMLModel_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UMLModel_Class)
gen_UMLModel_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UMLModel_Class)
gen_UMLModel_Classifier_Namespace = Generalization(general=Namespace, specific=UMLModel_Classifier)
gen_UMLModel_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_Classifier)
gen_UMLModel_Classifier_Type = Generalization(general=Type, specific=UMLModel_Classifier)
gen_UMLModel_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLModel_Classifier)
gen_UMLModel_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UMLModel_ClassifierTemplateParameter)
gen_UMLModel_Clause_Element = Generalization(general=Element, specific=UMLModel_Clause)
gen_UMLModel_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UMLModel_ClearVariableAction)
gen_UMLModel_ClearAssociationAction_Action = Generalization(general=Action, specific=UMLModel_ClearAssociationAction)
gen_UMLModel_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UMLModel_ClearStructuralFeatureAction)
gen_UMLModel_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UMLModel_Collaboration)
gen_UMLModel_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UMLModel_Collaboration)
gen_UMLModel_CollaborationUse_NamedElement = Generalization(general=NamedElement, specific=UMLModel_CollaborationUse)
gen_UMLModel_Comment_Element = Generalization(general=Element, specific=UMLModel_Comment)
gen_UMLModel_CommunicationPath_Association = Generalization(general=Association, specific=UMLModel_CommunicationPath)
gen_UMLModel_Component_Class = Generalization(general=Class_, specific=UMLModel_Component)
gen_UMLModel_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_CombinedFragment)
gen_UMLModel_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UMLModel_ConditionalNode)
gen_UMLModel_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Constraint)
gen_UMLModel_ConsiderIgnoreFragment_CombinedFragment = Generalization(general=CombinedFragment, specific=UMLModel_ConsiderIgnoreFragment)
gen_UMLModel_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_Continuation)
gen_UMLModel_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=UMLModel_ConnectableElement)
gen_UMLModel_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLModel_ConnectableElement)
gen_UMLModel_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UMLModel_ConnectableElementTemplateParameter)
gen_UMLModel_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLModel_ConnectorEnd)
gen_UMLModel_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=UMLModel_ConnectionPointReference)
gen_UMLModel_Connector_Feature = Generalization(general=Feature, specific=UMLModel_Connector)
gen_UMLModel_ComponentRealization_Realization = Generalization(general=Realization, specific=UMLModel_ComponentRealization)
gen_UMLModel_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UMLModel_ControlFlow)
gen_UMLModel_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UMLModel_ControlNode)
gen_UMLModel_CreationEvent_Event = Generalization(general=Event, specific=UMLModel_CreationEvent)
gen_UMLModel_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UMLModel_CreateLinkObjectAction)
gen_UMLModel_CreateObjectAction_Action = Generalization(general=Action, specific=UMLModel_CreateObjectAction)
gen_UMLModel_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UMLModel_CreateLinkAction)
gen_UMLModel_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=UMLModel_DeployedArtifact)
gen_UMLModel_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UMLModel_DeploymentSpecification)
gen_UMLModel_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UMLModel_DirectedRelationship)
gen_UMLModel_Device_Node = Generalization(general=Node, specific=UMLModel_Device)
gen_UMLModel_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UMLModel_DestroyLinkAction)
gen_UMLModel_DestroyObjectAction_Action = Generalization(general=Action, specific=UMLModel_DestroyObjectAction)
gen_UMLModel_DestructionEvent_Event = Generalization(general=Event, specific=UMLModel_DestructionEvent)
gen_UMLModel_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_Duration)
gen_UMLModel_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UMLModel_CentralBufferNode)
gen_UMLModel_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UMLModel_DataStoreNode)
gen_UMLModel_DataType_Classifier = Generalization(general=Classifier, specific=UMLModel_DataType)
gen_UMLModel_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_DecisionNode)
gen_UMLModel_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Dependency)
gen_UMLModel_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_Dependency)
gen_UMLModel_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UMLModel_DeploymentTarget)
gen_UMLModel_Deployment_Dependency = Generalization(general=Dependency, specific=UMLModel_Deployment)
gen_UMLModel_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UMLModel_EncapsulatedClassifier)
gen_UMLModel_Enumeration_DataType = Generalization(general=DataType, specific=UMLModel_Enumeration)
gen_UMLModel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=UMLModel_EnumerationLiteral)
gen_UMLModel_ExceptionHandler_Element = Generalization(general=Element, specific=UMLModel_ExceptionHandler)
gen_UMLModel_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=UMLModel_ExecutableNode)
gen_UMLModel_ExecutionEnvironment_Node = Generalization(general=Node, specific=UMLModel_ExecutionEnvironment)
gen_UMLModel_ExecutionEvent_Event = Generalization(general=Event, specific=UMLModel_ExecutionEvent)
gen_UMLModel_ExecutionOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=UMLModel_ExecutionOccurrenceSpecification)
gen_UMLModel_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_ExecutionSpecification)
gen_UMLModel_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UMLModel_DurationConstraint)
gen_UMLModel_DurationInterval_Interval = Generalization(general=Interval, specific=UMLModel_DurationInterval)
gen_UMLModel_DurationObservation_Observation = Generalization(general=Observation, specific=UMLModel_DurationObservation)
gen_UMLModel_Element_UMLBase = Generalization(general=UMLBase, specific=UMLModel_Element)
gen_UMLModel_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_ElementImport)
gen_UMLModel_ExtensionEnd_Property = Generalization(general=Property_, specific=UMLModel_ExtensionEnd)
gen_UMLModel_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_ExtensionPoint)
gen_UMLModel_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_Expression)
gen_UMLModel_Event_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Event)
gen_UMLModel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_Feature)
gen_UMLModel_FinalState_State = Generalization(general=State, specific=UMLModel_FinalState)
gen_UMLModel_ForkNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_ForkNode)
gen_UMLModel_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=UMLModel_FlowFinalNode)
gen_UMLModel_FinalNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_FinalNode)
gen_UMLModel_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=UMLModel_FunctionBehavior)
gen_UMLModel_Gate_MessageEnd = Generalization(general=MessageEnd, specific=UMLModel_Gate)
gen_UMLModel_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UMLModel_ExpansionNode)
gen_UMLModel_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UMLModel_ExpansionRegion)
gen_UMLModel_Extend_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Extend)
gen_UMLModel_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_Extend)
gen_UMLModel_Extension_Association = Generalization(general=Association, specific=UMLModel_Extension)
gen_UMLModel_Interface_Classifier = Generalization(general=Classifier, specific=UMLModel_Interface)
gen_UMLModel_Include_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Include)
gen_UMLModel_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_Include)
gen_UMLModel_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UMLModel_InstanceSpecification)
gen_UMLModel_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_InstanceSpecification)
gen_UMLModel_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UMLModel_InstanceSpecification)
gen_UMLModel_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=UMLModel_GeneralOrdering)
gen_UMLModel_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_Generalization)
gen_UMLModel_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_GeneralizationSet)
gen_UMLModel_Image_Element = Generalization(general=Element, specific=UMLModel_Image)
gen_UMLModel_InterfaceRealization_Realization = Generalization(general=Realization, specific=UMLModel_InterfaceRealization)
gen_UMLModel_InputPin_Pin = Generalization(general=Pin, specific=UMLModel_InputPin)
gen_UMLModel_InvocationAction_Action = Generalization(general=Action, specific=UMLModel_InvocationAction)
gen_UMLModel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_InstanceValue)
gen_UMLModel_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=UMLModel_InterruptibleActivityRegion)
gen_UMLModel_InteractionUse_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_InteractionUse)
gen_UMLModel_InteractionOperand_Namespace = Generalization(general=Namespace, specific=UMLModel_InteractionOperand)
gen_UMLModel_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_InteractionOperand)
gen_UMLModel_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UMLModel_InteractionConstraint)
gen_UMLModel_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_Interval)
gen_UMLModel_InitialNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_InitialNode)
gen_UMLModel_Interaction_Behavior = Generalization(general=Behavior, specific=UMLModel_Interaction)
gen_UMLModel_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_Interaction)
gen_UMLModel_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=UMLModel_InteractionFragment)
gen_UMLModel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_LiteralSpecification)
gen_UMLModel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UMLModel_LiteralInteger)
gen_UMLModel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UMLModel_LiteralString)
gen_UMLModel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UMLModel_LiteralBoolean)
gen_UMLModel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UMLModel_LiteralNull)
gen_UMLModel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UMLModel_LiteralUnlimitedNatural)
gen_UMLModel_Lifeline_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Lifeline)
gen_UMLModel_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UMLModel_IntervalConstraint)
gen_UMLModel_InformationItem_Classifier = Generalization(general=Classifier, specific=UMLModel_InformationItem)
gen_UMLModel_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_InformationFlow)
gen_UMLModel_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_InformationFlow)
gen_UMLModel_JoinNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_JoinNode)
gen_UMLModel_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UMLModel_LoopNode)
gen_UMLModel_Manifestation_Abstraction = Generalization(general=Abstraction, specific=UMLModel_Manifestation)
gen_UMLModel_Message_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Message)
gen_UMLModel_LinkAction_Action = Generalization(general=Action, specific=UMLModel_LinkAction)
gen_UMLModel_LinkEndData_Element = Generalization(general=Element, specific=UMLModel_LinkEndData)
gen_UMLModel_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UMLModel_LinkEndCreationData)
gen_UMLModel_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=UMLModel_LinkEndDestructionData)
gen_UMLModel_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=UMLModel_MessageEnd)
gen_UMLModel_MessageEvent_Event = Generalization(general=Event, specific=UMLModel_MessageEvent)
gen_UMLModel_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=UMLModel_MessageOccurrenceSpecification)
gen_UMLModel_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=UMLModel_MessageOccurrenceSpecification)
gen_UMLModel_MergeNode_ControlNode = Generalization(general=ControlNode, specific=UMLModel_MergeNode)
gen_UMLModel_Model_Package = Generalization(general=Package, specific=UMLModel_Model)
gen_UMLModel_Namespace_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Namespace)
gen_UMLModel_Node_Class = Generalization(general=Class_, specific=UMLModel_Node)
gen_UMLModel_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UMLModel_Node)
gen_UMLModel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UMLModel_Operation)
gen_UMLModel_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLModel_Operation)
gen_UMLModel_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLModel_Operation)
gen_UMLModel_MultiplicityElement_Element = Generalization(general=Element, specific=UMLModel_MultiplicityElement)
gen_UMLModel_NamedElement_Element = Generalization(general=Element, specific=UMLModel_NamedElement)
gen_UMLModel_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=UMLModel_OpaqueBehavior)
gen_UMLModel_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_OpaqueExpression)
gen_UMLModel_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_OccurrenceSpecification)
gen_UMLModel_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UMLModel_OperationTemplateParameter)
gen_UMLModel_OpaqueAction_Action = Generalization(general=Action, specific=UMLModel_OpaqueAction)
gen_UMLModel_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=UMLModel_Parameter)
gen_UMLModel_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLModel_Parameter)
gen_UMLModel_ParameterableElement_Element = Generalization(general=Element, specific=UMLModel_ParameterableElement)
gen_UMLModel_Package_Namespace = Generalization(general=Namespace, specific=UMLModel_Package)
gen_UMLModel_Package_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Package)
gen_UMLModel_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLModel_Package)
gen_UMLModel_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UMLModel_ObjectFlow)
gen_UMLModel_Observation_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Observation)
gen_UMLModel_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UMLModel_ObjectNode)
gen_UMLModel_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UMLModel_ObjectNode)
gen_UMLModel_OutputPin_Pin = Generalization(general=Pin, specific=UMLModel_OutputPin)
gen_UMLModel_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=UMLModel_ParameterSet)
gen_UMLModel_PartDecomposition_InteractionUse = Generalization(general=InteractionUse, specific=UMLModel_PartDecomposition)
gen_UMLModel_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UMLModel_Pin)
gen_UMLModel_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLModel_Pin)
gen_UMLModel_PrimitiveType_DataType = Generalization(general=DataType, specific=UMLModel_PrimitiveType)
gen_UMLModel_ProtocolTransition_Transition = Generalization(general=Transition, specific=UMLModel_ProtocolTransition)
gen_UMLModel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UMLModel_PackageableElement)
gen_UMLModel_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLModel_PackageableElement)
gen_UMLModel_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_PackageImport)
gen_UMLModel_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_PackageMerge)
gen_UMLModel_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UMLModel_ProtocolStateMachine)
gen_UMLModel_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_ProtocolConformance)
gen_UMLModel_Port_Property = Generalization(general=Property_, specific=UMLModel_Port)
gen_UMLModel_Profile_Package = Generalization(general=Package, specific=UMLModel_Profile)
gen_UMLModel_ProfileApplication_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_ProfileApplication)
gen_UMLModel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UMLModel_Property)
gen_UMLModel_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UMLModel_Property)
gen_UMLModel_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UMLModel_Property)
gen_UMLModel_Property_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLModel_Property)
gen_UMLModel_RaiseExceptionAction_Action = Generalization(general=Action, specific=UMLModel_RaiseExceptionAction)
gen_UMLModel_ReceiveOperationEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_ReceiveOperationEvent)
gen_UMLModel_ReceiveSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_ReceiveSignalEvent)
gen_UMLModel_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UMLModel_ReclassifyObjectAction)
gen_UMLModel_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UMLModel_ReadIsClassifiedObjectAction)
gen_UMLModel_Pseudostate_Vertex = Generalization(general=Vertex, specific=UMLModel_Pseudostate)
gen_UMLModel_QualifierValue_Element = Generalization(general=Element, specific=UMLModel_QualifierValue)
gen_UMLModel_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UMLModel_ReadLinkObjectEndQualifierAction)
gen_UMLModel_ReadSelfAction_Action = Generalization(general=Action, specific=UMLModel_ReadSelfAction)
gen_UMLModel_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UMLModel_ReadStructuralFeatureAction)
gen_UMLModel_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UMLModel_ReadVariableAction)
gen_UMLModel_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_RedefinableTemplateSignature)
gen_UMLModel_ReadExtentAction_Action = Generalization(general=Action, specific=UMLModel_ReadExtentAction)
gen_UMLModel_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UMLModel_ReadLinkAction)
gen_UMLModel_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UMLModel_ReadLinkObjectEndAction)
gen_UMLModel_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UMLModel_RemoveVariableValueAction)
gen_UMLModel_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UMLModel_RemoveStructuralFeatureValueAction)
gen_UMLModel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UMLModel_RedefinableElement)
gen_UMLModel_Relationship_Element = Generalization(general=Element, specific=UMLModel_Relationship)
gen_UMLModel_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=UMLModel_RedefinableTemplateSignature)
gen_UMLModel_ReduceAction_Action = Generalization(general=Action, specific=UMLModel_ReduceAction)
gen_UMLModel_ReplyAction_Action = Generalization(general=Action, specific=UMLModel_ReplyAction)
gen_UMLModel_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UMLModel_SequenceNode)
gen_UMLModel_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_SignalEvent)
gen_UMLModel_Slot_Element = Generalization(general=Element, specific=UMLModel_Slot)
gen_UMLModel_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=UMLModel_StateInvariant)
gen_UMLModel_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=UMLModel_StartClassifierBehaviorAction)
gen_UMLModel_Realization_Abstraction = Generalization(general=Abstraction, specific=UMLModel_Realization)
gen_UMLModel_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UMLModel_Reception)
gen_UMLModel_Region_Namespace = Generalization(general=Namespace, specific=UMLModel_Region)
gen_UMLModel_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_Region)
gen_UMLModel_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UMLModel_SendSignalAction)
gen_UMLModel_SendSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=UMLModel_SendSignalEvent)
gen_UMLModel_StructuralFeature_Feature = Generalization(general=Feature, specific=UMLModel_StructuralFeature)
gen_UMLModel_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UMLModel_StructuralFeature)
gen_UMLModel_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLModel_StructuralFeature)
gen_UMLModel_StructuralFeatureAction_Action = Generalization(general=Action, specific=UMLModel_StructuralFeatureAction)
gen_UMLModel_Substitution_Realization = Generalization(general=Realization, specific=UMLModel_Substitution)
gen_UMLModel_Signal_Classifier = Generalization(general=Classifier, specific=UMLModel_Signal)
gen_UMLModel_State_Namespace = Generalization(general=Namespace, specific=UMLModel_State)
gen_UMLModel_State_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_State)
gen_UMLModel_State_Vertex = Generalization(general=Vertex, specific=UMLModel_State)
gen_UMLModel_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UMLModel_SendObjectAction)
gen_UMLModel_StringExpression_Expression = Generalization(general=Expression, specific=UMLModel_StringExpression)
gen_UMLModel_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLModel_StringExpression)
gen_UMLModel_StructuredActivityNode_Action = Generalization(general=Action, specific=UMLModel_StructuredActivityNode)
gen_UMLModel_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=UMLModel_StructuredActivityNode)
gen_UMLModel_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=UMLModel_StructuredActivityNode)
gen_UMLModel_StateMachine_Behavior = Generalization(general=Behavior, specific=UMLModel_StateMachine)
gen_UMLModel_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UMLModel_StructuredClassifier)
gen_UMLModel_TemplateParameter_Element = Generalization(general=Element, specific=UMLModel_TemplateParameter)
gen_UMLModel_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=UMLModel_TemplateParameterSubstitution)
gen_UMLModel_TestIdentityAction_Action = Generalization(general=Action, specific=UMLModel_TestIdentityAction)
gen_UMLModel_Stereotype_Class = Generalization(general=Class_, specific=UMLModel_Stereotype)
gen_UMLModel_TemplateableElement_Element = Generalization(general=Element, specific=UMLModel_TemplateableElement)
gen_UMLModel_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLModel_TemplateBinding)
gen_UMLModel_TemplateSignature_Element = Generalization(general=Element, specific=UMLModel_TemplateSignature)
gen_UMLModel_TimeObservation_Observation = Generalization(general=Observation, specific=UMLModel_TimeObservation)
gen_UMLModel_Transition_Namespace = Generalization(general=Namespace, specific=UMLModel_Transition)
gen_UMLModel_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLModel_Transition)
gen_UMLModel_Trigger_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Trigger)
gen_UMLModel_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UMLModel_TimeConstraint)
gen_UMLModel_TimeEvent_Event = Generalization(general=Event, specific=UMLModel_TimeEvent)
gen_UMLModel_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UMLModel_TimeExpression)
gen_UMLModel_TimeInterval_Interval = Generalization(general=Interval, specific=UMLModel_TimeInterval)
gen_UMLModel_ValuePin_InputPin = Generalization(general=InputPin, specific=UMLModel_ValuePin)
gen_UMLModel_ValueSpecificationAction_Action = Generalization(general=Action, specific=UMLModel_ValueSpecificationAction)
gen_UMLModel_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_ValueSpecification)
gen_UMLModel_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UMLModel_ValueSpecification)
gen_UMLModel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UMLModel_TypedElement)
gen_UMLModel_Type_PackageableElement = Generalization(general=PackageableElement, specific=UMLModel_Type)
gen_UMLModel_UnmarshallAction_Action = Generalization(general=Action, specific=UMLModel_UnmarshallAction)
gen_UMLModel_UMLBase_EObject = Generalization(general=EObject, specific=UMLModel_UMLBase)
gen_UMLModel_Usage_Dependency = Generalization(general=Dependency, specific=UMLModel_Usage)
gen_UMLModel_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UMLModel_UseCase)
gen_UMLModel_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=UMLModel_Variable)
gen_UMLModel_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLModel_Variable)
gen_UMLModel_VariableAction_Action = Generalization(general=Action, specific=UMLModel_VariableAction)
gen_UMLModel_Vertex_NamedElement = Generalization(general=NamedElement, specific=UMLModel_Vertex)
gen_UMLModel_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UMLModel_WriteLinkAction)
gen_UMLModel_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UMLModel_WriteVariableAction)
gen_UMLModel_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UMLModel_WriteStructuralFeatureAction)

# Domain Model
domain_model = DomainModel(
    name="UMLModel",
    types={UMLModel_Abstraction, Dependency, UMLModel_OpaqueExpression, UMLModel_AcceptCallAction, AcceptEventAction, UMLModel_OutputPin, UMLModel_AcceptEventAction, Action, UMLModel_Trigger, UMLModel_Action, ExecutableNode, UMLModel_Constraint, UMLModel_ActionExecutionSpecification, ExecutionSpecification, UMLModel_ActionInputPin, InputPin, UMLModel_Activity, Behavior, UMLModel_Variable, UMLModel_ActivityEdge, UMLModel_ActivityGroup, RedefinableElement, UMLModel_ValueSpecification, UMLModel_ActivityFinalNode, FinalNode, Element, UMLModel_ActivityNode, UMLModel_ActivityParameterNode, ObjectNode, UMLModel_Actor, BehavioredClassifier, UMLModel_AddStructuralFeatureValueAction, WriteStructuralFeatureAction, UMLModel_InputPin, UMLModel_AddVariableValueAction, WriteVariableAction, UMLModel_AnyReceiveEvent, MessageEvent, UMLModel_Artifact, Classifier, DeployedArtifact, UMLModel_Manifestation, UMLModel_Operation, UMLModel_Property, UMLModel_Association, Relationship, UMLModel_ActivityPartition, NamedElement, ActivityGroup, UMLModel_AssociationClass, Class_, Association, UMLModel_Behavior, UMLModel_Parameter, UMLModel_ParameterSet, UMLModel_BehaviorExecutionSpecification, UMLModel_BehavioralFeature, Namespace, Feature, UMLModel_BehavioredClassifier, UMLModel_InterfaceRealization, UMLModel_BroadcastSignalAction, InvocationAction, UMLModel_CallAction, UMLModel_CallBehaviorAction, CallAction, UMLModel_CallEvent, UMLModel_CallOperationAction, UMLModel_ChangeEvent, Event, UMLModel_Class, EncapsulatedClassifier, UMLModel_Classifier, UMLModel_Reception, Type, TemplateableElement, UMLModel_Generalization, UMLModel_Substitution, UMLModel_UseCase, UMLModel_ClassifierTemplateParameter, TemplateParameter, UMLModel_Clause, UMLModel_ClearVariableAction, VariableAction, UMLModel_ClearAssociationAction, UMLModel_ClearStructuralFeatureAction, StructuralFeatureAction, UMLModel_Collaboration, StructuredClassifier, UMLModel_Dependency, UMLModel_Comment, UMLModel_CommunicationPath, UMLModel_Component, UMLModel_PackageableElement, UMLModel_ComponentRealization, UMLModel_CollaborationUse, UMLModel_CombinedFragment, InteractionFragment, UMLModel_InteractionOperand, UMLModel_Gate, UMLModel_ConditionalNode, StructuredActivityNode, PackageableElement, UMLModel_ConsiderIgnoreFragment, CombinedFragment, UMLModel_Continuation, UMLModel_ConnectableElement, TypedElement, ParameterableElement, UMLModel_ConnectableElementTemplateParameter, UMLModel_ConnectorEnd, MultiplicityElement, UMLModel_ConnectionPointReference, Vertex, UMLModel_Connector, Realization, UMLModel_ControlFlow, ActivityEdge, UMLModel_ControlNode, ActivityNode, UMLModel_CreationEvent, UMLModel_CreateLinkObjectAction, CreateLinkAction, UMLModel_CreateObjectAction, UMLModel_CreateLinkAction, WriteLinkAction, UMLModel_CentralBufferNode, UMLModel_DeployedArtifact, Artifact, UMLModel_DirectedRelationship, UMLModel_Device, Node, UMLModel_DestroyLinkAction, UMLModel_DestroyObjectAction, UMLModel_DestructionEvent, UMLModel_Duration, ValueSpecification, UMLModel_DataStoreNode, CentralBufferNode, UMLModel_DataType, UMLModel_DecisionNode, ControlNode, DirectedRelationship, UMLModel_DeploymentTarget, UMLModel_Deployment, UMLModel_DeploymentSpecification, UMLModel_EncapsulatedClassifier, UMLModel_Enumeration, DataType, UMLModel_EnumerationLiteral, InstanceSpecification, UMLModel_ExceptionHandler, UMLModel_ExecutableNode, UMLModel_ExecutionEnvironment, UMLModel_ExecutionEvent, UMLModel_ExecutionOccurrenceSpecification, OccurrenceSpecification, UMLModel_ExecutionSpecification, UMLModel_DurationConstraint, IntervalConstraint, UMLModel_DurationInterval, Interval, UMLModel_DurationObservation, Observation, UMLModel_Element, UMLBase, UMLModel_ElementImport, UMLModel_ExtensionEnd, Property_, UMLModel_ExtensionPoint, UMLModel_Expression, UMLModel_Event, UMLModel_Feature, UMLModel_FinalState, State, UMLModel_ForkNode, UMLModel_FlowFinalNode, UMLModel_FinalNode, UMLModel_FunctionBehavior, OpaqueBehavior, MessageEnd, UMLModel_ExpansionNode, UMLModel_ExpansionRegion, UMLModel_Extend, UMLModel_Extension, UMLModel_Interface, UMLModel_ProtocolStateMachine, UMLModel_Include, UMLModel_InstanceSpecification, DeploymentTarget, UMLModel_GeneralOrdering, UMLModel_GeneralizationSet, UMLModel_Image, Pin, UMLModel_InvocationAction, UMLModel_Slot, UMLModel_InstanceValue, UMLModel_InterruptibleActivityRegion, UMLModel_InteractionUse, UMLModel_InteractionConstraint, Constraint, UMLModel_Interval, UMLModel_InitialNode, UMLModel_Interaction, UMLModel_Lifeline, UMLModel_InteractionFragment, UMLModel_Message, UMLModel_LiteralSpecification, UMLModel_LiteralInteger, LiteralSpecification, UMLModel_LiteralString, UMLModel_LiteralBoolean, UMLModel_LiteralNull, UMLModel_LiteralUnlimitedNatural, UMLModel_IntervalConstraint, UMLModel_InformationItem, UMLModel_InformationFlow, UMLModel_JoinNode, UMLModel_LoopNode, Abstraction, UMLModel_LinkAction, UMLModel_LinkEndData, UMLModel_QualifierValue, UMLModel_LinkEndCreationData, LinkEndData, UMLModel_LinkEndDestructionData, UMLModel_MessageEnd, UMLModel_MessageEvent, UMLModel_MessageOccurrenceSpecification, UMLModel_MergeNode, UMLModel_Model, Package, UMLModel_MultiplicityElement, UMLModel_Namespace, UMLModel_PackageImport, UMLModel_Node, BehavioralFeature, UMLModel_NamedElement, UMLModel_StringExpression, UMLModel_OpaqueBehavior, UMLModel_OccurrenceSpecification, UMLModel_OperationTemplateParameter, UMLModel_OpaqueAction, ConnectableElement, UMLModel_ParameterableElement, UMLModel_Package, UMLModel_PackageMerge, UMLModel_ObjectFlow, UMLModel_Observation, UMLModel_ObjectNode, UMLModel_PartDecomposition, InteractionUse, UMLModel_Pin, UMLModel_PrimitiveType, UMLModel_ProtocolTransition, Transition, UMLModel_ProfileApplication, StateMachine, UMLModel_ProtocolConformance, UMLModel_Port, UMLModel_Profile, StructuralFeature, UMLModel_RaiseExceptionAction, UMLModel_ReceiveOperationEvent, UMLModel_ReceiveSignalEvent, UMLModel_ReclassifyObjectAction, UMLModel_ReadIsClassifiedObjectAction, UMLModel_Pseudostate, UMLModel_ReadLinkObjectEndQualifierAction, UMLModel_ReadSelfAction, UMLModel_ReadStructuralFeatureAction, UMLModel_ReadVariableAction, UMLModel_RedefinableTemplateSignature, UMLModel_ReadExtentAction, UMLModel_ReadLinkAction, LinkAction, UMLModel_ReadLinkObjectEndAction, UMLModel_RemoveVariableValueAction, UMLModel_RemoveStructuralFeatureValueAction, UMLModel_RedefinableElement, UMLModel_Relationship, TemplateSignature, UMLModel_ReduceAction, UMLModel_ReplyAction, UMLModel_SequenceNode, UMLModel_SignalEvent, UMLModel_StateInvariant, UMLModel_StartClassifierBehaviorAction, UMLModel_SendObjectAction, UMLModel_Realization, UMLModel_Region, UMLModel_Vertex, UMLModel_Transition, UMLModel_SendSignalAction, UMLModel_SendSignalEvent, UMLModel_StructuralFeature, UMLModel_StructuralFeatureAction, UMLModel_Signal, UMLModel_State, Expression, UMLModel_StructuredActivityNode, UMLModel_StateMachine, UMLModel_StructuredClassifier, UMLModel_TemplateParameter, UMLModel_TestIdentityAction, UMLModel_Stereotype, UMLModel_TemplateableElement, UMLModel_TemplateBinding, UMLModel_TemplateSignature, UMLModel_TemplateParameterSubstitution, UMLModel_TimeConstraint, UMLModel_TimeEvent, UMLModel_TimeExpression, UMLModel_TimeInterval, UMLModel_TimeObservation, UMLModel_ValuePin, UMLModel_ValueSpecificationAction, UMLModel_TypedElement, UMLModel_Type, UMLModel_UnmarshallAction, UMLModel_UMLBase, EObject, UMLModel_Usage, UMLModel_VariableAction, UMLModel_WriteLinkAction, UMLModel_WriteVariableAction, UMLModel_WriteStructuralFeatureAction, AggregationKind, CallConcurrencyKind, ConnectorKind, ExpansionKind, InteractionOperatorKind, MessageKind, MessageSort, ObjectNodeOrderingKind, ParameterDirectionKind, ParameterEffectKind, PseudostateKind, TransitionKind, VisibilityKind},
    associations={mapping0, returnInformation1, result2, trigger4, localPrecondition6, localPostcondition7, fromAction10, variable12, node13, edge15, group17, guard19, weight21, containedEdge24, containedNode27, insertAt30, insertAt31, nestedArtifact34, manifestation35, ownedOperation37, ownedAttribute39, ownedEnd41, ownedParameter43, ownedParameterSet44, ownedParameter46, ownedParameterSet48, ownedBehavior51, interfaceRealization53, ownedTrigger55, target60, changeExpression62, nestedClassifier64, ownedOperation65, ownedReception68, generalization70, substitution72, result58, ownedUseCase76, object78, roleBinding80, packagedElement82, realization83, collaborationUse74, operand85, cfragmentGate86, clause88, result89, specification92, result96, result98, target108, end95, ownedAttribute100, ownedOperation102, deployment105, configuration106, ownedLiteral113, handler114, ownedComment110, importedElement111, operand117, condition115, ownedAttribute119, ownedOperation121, nestedClassifier124, ownedReception127, protocol130, argument136, slot132, specification133, actualGate151, argument153, guard156, fragment158, minint161, maxint164, lifeline138, fragment139, action141, formalGate144, message147, generalOrdering149, joinSpec167, selector169, result178, loopVariableInput180, endData172, inputValue173, qualifier176, argument183, elementImport192, packageImport194, ownedRule196, nestedNode200, upperValue186, lowerValue188, nameExpression191, inputValue201, outputValue203, defaultValue208, packageMerge211, upperBound206, condition220, packagedElement212, profileApplication215, importedPackage217, defaultValue223, qualifier227, conformance229, exception231, object233, object249, result251, result254, result256, result258, result235, object237, result240, result242, object244, result246, removeAt270, removeAt272, result260, collection262, returnInformation265, replyValue267, executableNode279, value281, invariant284, object286, subvertex274, transition275, target277, object304, ownedAttribute306, target288, request290, subExpression294, variable296, edge298, node301, doActivity320, deferrableTrigger323, region326, region329, connectionPoint331, ownedAttribute334, connection308, connectionPoint309, stateInvariant311, entry314, exit317, ownedParameter345, ownedParameteredElement347, ownedDefault349, ownedActual352, ownedConnector336, icon339, templateBinding340, ownedTemplateSignature341, parameterSubstitution343, effect365, trigger368, first355, second357, result360, when363, include376, extend378, extensionPoint381, value383, value385, result387, result371, object373, value392, value390},
    generalizations={gen_UMLModel_Abstraction_Dependency, gen_UMLModel_AcceptCallAction_AcceptEventAction, gen_UMLModel_AcceptEventAction_Action, gen_UMLModel_Action_ExecutableNode, gen_UMLModel_ActionExecutionSpecification_ExecutionSpecification, gen_UMLModel_ActionInputPin_InputPin, gen_UMLModel_Activity_Behavior, gen_UMLModel_ActivityEdge_RedefinableElement, gen_UMLModel_ActivityFinalNode_FinalNode, gen_UMLModel_ActivityNode_RedefinableElement, gen_UMLModel_ActivityGroup_Element, gen_UMLModel_ActivityParameterNode_ObjectNode, gen_UMLModel_Actor_BehavioredClassifier, gen_UMLModel_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UMLModel_AddVariableValueAction_WriteVariableAction, gen_UMLModel_AnyReceiveEvent_MessageEvent, gen_UMLModel_Artifact_Classifier, gen_UMLModel_Artifact_DeployedArtifact, gen_UMLModel_Association_Classifier, gen_UMLModel_Association_Relationship, gen_UMLModel_ActivityPartition_NamedElement, gen_UMLModel_ActivityPartition_ActivityGroup, gen_UMLModel_AssociationClass_Class, gen_UMLModel_AssociationClass_Association, gen_UMLModel_Behavior_Class, gen_UMLModel_BehaviorExecutionSpecification_ExecutionSpecification, gen_UMLModel_BehavioralFeature_Namespace, gen_UMLModel_BehavioralFeature_Feature, gen_UMLModel_BehavioredClassifier_Classifier, gen_UMLModel_BroadcastSignalAction_InvocationAction, gen_UMLModel_CallAction_InvocationAction, gen_UMLModel_CallBehaviorAction_CallAction, gen_UMLModel_CallEvent_MessageEvent, gen_UMLModel_CallOperationAction_CallAction, gen_UMLModel_ChangeEvent_Event, gen_UMLModel_Class_EncapsulatedClassifier, gen_UMLModel_Class_BehavioredClassifier, gen_UMLModel_Classifier_Namespace, gen_UMLModel_Classifier_RedefinableElement, gen_UMLModel_Classifier_Type, gen_UMLModel_Classifier_TemplateableElement, gen_UMLModel_ClassifierTemplateParameter_TemplateParameter, gen_UMLModel_Clause_Element, gen_UMLModel_ClearVariableAction_VariableAction, gen_UMLModel_ClearAssociationAction_Action, gen_UMLModel_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UMLModel_Collaboration_BehavioredClassifier, gen_UMLModel_Collaboration_StructuredClassifier, gen_UMLModel_CollaborationUse_NamedElement, gen_UMLModel_Comment_Element, gen_UMLModel_CommunicationPath_Association, gen_UMLModel_Component_Class, gen_UMLModel_CombinedFragment_InteractionFragment, gen_UMLModel_ConditionalNode_StructuredActivityNode, gen_UMLModel_Constraint_PackageableElement, gen_UMLModel_ConsiderIgnoreFragment_CombinedFragment, gen_UMLModel_Continuation_InteractionFragment, gen_UMLModel_ConnectableElement_TypedElement, gen_UMLModel_ConnectableElement_ParameterableElement, gen_UMLModel_ConnectableElementTemplateParameter_TemplateParameter, gen_UMLModel_ConnectorEnd_MultiplicityElement, gen_UMLModel_ConnectionPointReference_Vertex, gen_UMLModel_Connector_Feature, gen_UMLModel_ComponentRealization_Realization, gen_UMLModel_ControlFlow_ActivityEdge, gen_UMLModel_ControlNode_ActivityNode, gen_UMLModel_CreationEvent_Event, gen_UMLModel_CreateLinkObjectAction_CreateLinkAction, gen_UMLModel_CreateObjectAction_Action, gen_UMLModel_CreateLinkAction_WriteLinkAction, gen_UMLModel_DeployedArtifact_NamedElement, gen_UMLModel_DeploymentSpecification_Artifact, gen_UMLModel_DirectedRelationship_Relationship, gen_UMLModel_Device_Node, gen_UMLModel_DestroyLinkAction_WriteLinkAction, gen_UMLModel_DestroyObjectAction_Action, gen_UMLModel_DestructionEvent_Event, gen_UMLModel_Duration_ValueSpecification, gen_UMLModel_CentralBufferNode_ObjectNode, gen_UMLModel_DataStoreNode_CentralBufferNode, gen_UMLModel_DataType_Classifier, gen_UMLModel_DecisionNode_ControlNode, gen_UMLModel_Dependency_PackageableElement, gen_UMLModel_Dependency_DirectedRelationship, gen_UMLModel_DeploymentTarget_NamedElement, gen_UMLModel_Deployment_Dependency, gen_UMLModel_EncapsulatedClassifier_StructuredClassifier, gen_UMLModel_Enumeration_DataType, gen_UMLModel_EnumerationLiteral_InstanceSpecification, gen_UMLModel_ExceptionHandler_Element, gen_UMLModel_ExecutableNode_ActivityNode, gen_UMLModel_ExecutionEnvironment_Node, gen_UMLModel_ExecutionEvent_Event, gen_UMLModel_ExecutionOccurrenceSpecification_OccurrenceSpecification, gen_UMLModel_ExecutionSpecification_InteractionFragment, gen_UMLModel_DurationConstraint_IntervalConstraint, gen_UMLModel_DurationInterval_Interval, gen_UMLModel_DurationObservation_Observation, gen_UMLModel_Element_UMLBase, gen_UMLModel_ElementImport_DirectedRelationship, gen_UMLModel_ExtensionEnd_Property, gen_UMLModel_ExtensionPoint_RedefinableElement, gen_UMLModel_Expression_ValueSpecification, gen_UMLModel_Event_PackageableElement, gen_UMLModel_Feature_RedefinableElement, gen_UMLModel_FinalState_State, gen_UMLModel_ForkNode_ControlNode, gen_UMLModel_FlowFinalNode_FinalNode, gen_UMLModel_FinalNode_ControlNode, gen_UMLModel_FunctionBehavior_OpaqueBehavior, gen_UMLModel_Gate_MessageEnd, gen_UMLModel_ExpansionNode_ObjectNode, gen_UMLModel_ExpansionRegion_StructuredActivityNode, gen_UMLModel_Extend_NamedElement, gen_UMLModel_Extend_DirectedRelationship, gen_UMLModel_Extension_Association, gen_UMLModel_Interface_Classifier, gen_UMLModel_Include_NamedElement, gen_UMLModel_Include_DirectedRelationship, gen_UMLModel_InstanceSpecification_DeploymentTarget, gen_UMLModel_InstanceSpecification_PackageableElement, gen_UMLModel_InstanceSpecification_DeployedArtifact, gen_UMLModel_GeneralOrdering_NamedElement, gen_UMLModel_Generalization_DirectedRelationship, gen_UMLModel_GeneralizationSet_PackageableElement, gen_UMLModel_Image_Element, gen_UMLModel_InterfaceRealization_Realization, gen_UMLModel_InputPin_Pin, gen_UMLModel_InvocationAction_Action, gen_UMLModel_InstanceValue_ValueSpecification, gen_UMLModel_InterruptibleActivityRegion_ActivityGroup, gen_UMLModel_InteractionUse_InteractionFragment, gen_UMLModel_InteractionOperand_Namespace, gen_UMLModel_InteractionOperand_InteractionFragment, gen_UMLModel_InteractionConstraint_Constraint, gen_UMLModel_Interval_ValueSpecification, gen_UMLModel_InitialNode_ControlNode, gen_UMLModel_Interaction_Behavior, gen_UMLModel_Interaction_InteractionFragment, gen_UMLModel_InteractionFragment_NamedElement, gen_UMLModel_LiteralSpecification_ValueSpecification, gen_UMLModel_LiteralInteger_LiteralSpecification, gen_UMLModel_LiteralString_LiteralSpecification, gen_UMLModel_LiteralBoolean_LiteralSpecification, gen_UMLModel_LiteralNull_LiteralSpecification, gen_UMLModel_LiteralUnlimitedNatural_LiteralSpecification, gen_UMLModel_Lifeline_NamedElement, gen_UMLModel_IntervalConstraint_Constraint, gen_UMLModel_InformationItem_Classifier, gen_UMLModel_InformationFlow_PackageableElement, gen_UMLModel_InformationFlow_DirectedRelationship, gen_UMLModel_JoinNode_ControlNode, gen_UMLModel_LoopNode_StructuredActivityNode, gen_UMLModel_Manifestation_Abstraction, gen_UMLModel_Message_NamedElement, gen_UMLModel_LinkAction_Action, gen_UMLModel_LinkEndData_Element, gen_UMLModel_LinkEndCreationData_LinkEndData, gen_UMLModel_LinkEndDestructionData_LinkEndData, gen_UMLModel_MessageEnd_NamedElement, gen_UMLModel_MessageEvent_Event, gen_UMLModel_MessageOccurrenceSpecification_OccurrenceSpecification, gen_UMLModel_MessageOccurrenceSpecification_MessageEnd, gen_UMLModel_MergeNode_ControlNode, gen_UMLModel_Model_Package, gen_UMLModel_Namespace_NamedElement, gen_UMLModel_Node_Class, gen_UMLModel_Node_DeploymentTarget, gen_UMLModel_Operation_BehavioralFeature, gen_UMLModel_Operation_ParameterableElement, gen_UMLModel_Operation_TemplateableElement, gen_UMLModel_MultiplicityElement_Element, gen_UMLModel_NamedElement_Element, gen_UMLModel_OpaqueBehavior_Behavior, gen_UMLModel_OpaqueExpression_ValueSpecification, gen_UMLModel_OccurrenceSpecification_InteractionFragment, gen_UMLModel_OperationTemplateParameter_TemplateParameter, gen_UMLModel_OpaqueAction_Action, gen_UMLModel_Parameter_ConnectableElement, gen_UMLModel_Parameter_MultiplicityElement, gen_UMLModel_ParameterableElement_Element, gen_UMLModel_Package_Namespace, gen_UMLModel_Package_PackageableElement, gen_UMLModel_Package_TemplateableElement, gen_UMLModel_ObjectFlow_ActivityEdge, gen_UMLModel_Observation_PackageableElement, gen_UMLModel_ObjectNode_ActivityNode, gen_UMLModel_ObjectNode_TypedElement, gen_UMLModel_OutputPin_Pin, gen_UMLModel_ParameterSet_NamedElement, gen_UMLModel_PartDecomposition_InteractionUse, gen_UMLModel_Pin_ObjectNode, gen_UMLModel_Pin_MultiplicityElement, gen_UMLModel_PrimitiveType_DataType, gen_UMLModel_ProtocolTransition_Transition, gen_UMLModel_PackageableElement_NamedElement, gen_UMLModel_PackageableElement_ParameterableElement, gen_UMLModel_PackageImport_DirectedRelationship, gen_UMLModel_PackageMerge_DirectedRelationship, gen_UMLModel_ProtocolStateMachine_StateMachine, gen_UMLModel_ProtocolConformance_DirectedRelationship, gen_UMLModel_Port_Property, gen_UMLModel_Profile_Package, gen_UMLModel_ProfileApplication_DirectedRelationship, gen_UMLModel_Property_StructuralFeature, gen_UMLModel_Property_ConnectableElement, gen_UMLModel_Property_DeploymentTarget, gen_UMLModel_Property_TemplateableElement, gen_UMLModel_RaiseExceptionAction_Action, gen_UMLModel_ReceiveOperationEvent_MessageEvent, gen_UMLModel_ReceiveSignalEvent_MessageEvent, gen_UMLModel_ReclassifyObjectAction_Action, gen_UMLModel_ReadIsClassifiedObjectAction_Action, gen_UMLModel_Pseudostate_Vertex, gen_UMLModel_QualifierValue_Element, gen_UMLModel_ReadLinkObjectEndQualifierAction_Action, gen_UMLModel_ReadSelfAction_Action, gen_UMLModel_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UMLModel_ReadVariableAction_VariableAction, gen_UMLModel_RedefinableTemplateSignature_RedefinableElement, gen_UMLModel_ReadExtentAction_Action, gen_UMLModel_ReadLinkAction_LinkAction, gen_UMLModel_ReadLinkObjectEndAction_Action, gen_UMLModel_RemoveVariableValueAction_WriteVariableAction, gen_UMLModel_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UMLModel_RedefinableElement_NamedElement, gen_UMLModel_Relationship_Element, gen_UMLModel_RedefinableTemplateSignature_TemplateSignature, gen_UMLModel_ReduceAction_Action, gen_UMLModel_ReplyAction_Action, gen_UMLModel_SequenceNode_StructuredActivityNode, gen_UMLModel_SignalEvent_MessageEvent, gen_UMLModel_Slot_Element, gen_UMLModel_StateInvariant_InteractionFragment, gen_UMLModel_StartClassifierBehaviorAction_Action, gen_UMLModel_Realization_Abstraction, gen_UMLModel_Reception_BehavioralFeature, gen_UMLModel_Region_Namespace, gen_UMLModel_Region_RedefinableElement, gen_UMLModel_SendSignalAction_InvocationAction, gen_UMLModel_SendSignalEvent_MessageEvent, gen_UMLModel_StructuralFeature_Feature, gen_UMLModel_StructuralFeature_TypedElement, gen_UMLModel_StructuralFeature_MultiplicityElement, gen_UMLModel_StructuralFeatureAction_Action, gen_UMLModel_Substitution_Realization, gen_UMLModel_Signal_Classifier, gen_UMLModel_State_Namespace, gen_UMLModel_State_RedefinableElement, gen_UMLModel_State_Vertex, gen_UMLModel_SendObjectAction_InvocationAction, gen_UMLModel_StringExpression_Expression, gen_UMLModel_StringExpression_TemplateableElement, gen_UMLModel_StructuredActivityNode_Action, gen_UMLModel_StructuredActivityNode_Namespace, gen_UMLModel_StructuredActivityNode_ActivityGroup, gen_UMLModel_StateMachine_Behavior, gen_UMLModel_StructuredClassifier_Classifier, gen_UMLModel_TemplateParameter_Element, gen_UMLModel_TemplateParameterSubstitution_Element, gen_UMLModel_TestIdentityAction_Action, gen_UMLModel_Stereotype_Class, gen_UMLModel_TemplateableElement_Element, gen_UMLModel_TemplateBinding_DirectedRelationship, gen_UMLModel_TemplateSignature_Element, gen_UMLModel_TimeObservation_Observation, gen_UMLModel_Transition_Namespace, gen_UMLModel_Transition_RedefinableElement, gen_UMLModel_Trigger_NamedElement, gen_UMLModel_TimeConstraint_IntervalConstraint, gen_UMLModel_TimeEvent_Event, gen_UMLModel_TimeExpression_ValueSpecification, gen_UMLModel_TimeInterval_Interval, gen_UMLModel_ValuePin_InputPin, gen_UMLModel_ValueSpecificationAction_Action, gen_UMLModel_ValueSpecification_PackageableElement, gen_UMLModel_ValueSpecification_TypedElement, gen_UMLModel_TypedElement_NamedElement, gen_UMLModel_Type_PackageableElement, gen_UMLModel_UnmarshallAction_Action, gen_UMLModel_UMLBase_EObject, gen_UMLModel_Usage_Dependency, gen_UMLModel_UseCase_BehavioredClassifier, gen_UMLModel_Variable_ConnectableElement, gen_UMLModel_Variable_MultiplicityElement, gen_UMLModel_VariableAction_Action, gen_UMLModel_Vertex_NamedElement, gen_UMLModel_WriteLinkAction_LinkAction, gen_UMLModel_WriteVariableAction_VariableAction, gen_UMLModel_WriteStructuralFeatureAction_StructuralFeatureAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)