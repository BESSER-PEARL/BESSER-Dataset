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

# Classes
InvocationAction = Class(name="InvocationAction")
Element = Class(name="Element")
UML2WithID_ConnectableElement = Class(name="UML2WithID::ConnectableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
UML2WithID_DeploymentSpecification = Class(name="UML2WithID::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2WithID_SendSignalAction = Class(name="UML2WithID::SendSignalAction")
UML2WithID_OutputPin = Class(name="UML2WithID::OutputPin")
Pin = Class(name="Pin")
UML2WithID_ConditionalNode = Class(name="UML2WithID::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
UML2WithID_Dependency = Class(name="UML2WithID::Dependency")
PackageableElement = Class(name="PackageableElement")
UML2WithID_MessageEnd = Class(name="UML2WithID::MessageEnd", is_abstract=True)
UML2WithID_ExecutableNode = Class(name="UML2WithID::ExecutableNode", is_abstract=True)
UML2WithID_ReadExtentAction = Class(name="UML2WithID::ReadExtentAction")
Action = Class(name="Action")
UML2WithID_Permission = Class(name="UML2WithID::Permission")
Dependency = Class(name="Dependency")
UML2WithID_CreateLinkObjectAction = Class(name="UML2WithID::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UML2WithID_Interaction = Class(name="UML2WithID::Interaction")
Behavior = Class(name="Behavior")
InteractionFragment = Class(name="InteractionFragment")
UML2WithID_Action = Class(name="UML2WithID::Action")
ExecutableNode = Class(name="ExecutableNode")
UML2WithID_ObjectFlow = Class(name="UML2WithID::ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
UML2WithID_DurationObservationAction = Class(name="UML2WithID::DurationObservationAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UML2WithID_ReadLinkAction = Class(name="UML2WithID::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UML2WithID_LiteralSpecification = Class(name="UML2WithID::LiteralSpecification", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
UML2WithID_InstanceValue = Class(name="UML2WithID::InstanceValue")
UML2WithID_AnyTrigger = Class(name="UML2WithID::AnyTrigger")
MessageTrigger = Class(name="MessageTrigger")
UML2WithID_StateMachine = Class(name="UML2WithID::StateMachine")
UML2WithID_StartOwnedBehaviorAction = Class(name="UML2WithID::StartOwnedBehaviorAction")
UML2WithID_RedefinableTemplateSignature = Class(name="UML2WithID::RedefinableTemplateSignature")
RedefinableElement = Class(name="RedefinableElement")
UML2WithID_Parameter = Class(name="UML2WithID::Parameter")
ConnectableElement = Class(name="ConnectableElement")
UML2WithID_MergeNode = Class(name="UML2WithID::MergeNode")
TypedElement = Class(name="TypedElement")
ControlNode = Class(name="ControlNode")
UML2WithID_Extension = Class(name="UML2WithID::Extension")
UML2WithID_InteractionConstraint = Class(name="UML2WithID::InteractionConstraint")
Constraint = Class(name="Constraint")
ActivityNode = Class(name="ActivityNode")
UML2WithID_DestroyLinkAction = Class(name="UML2WithID::DestroyLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UML2WithID_Stop = Class(name="UML2WithID::Stop")
EventOccurrence = Class(name="EventOccurrence")
UML2WithID_OpaqueExpression = Class(name="UML2WithID::OpaqueExpression")
UML2WithID_DataType = Class(name="UML2WithID::DataType")
Classifier = Class(name="Classifier")
UML2WithID_ReadLinkObjectEndAction = Class(name="UML2WithID::ReadLinkObjectEndAction")
UML2WithID_ProtocolStateMachine = Class(name="UML2WithID::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2WithID_InstanceSpecification = Class(name="UML2WithID::InstanceSpecification")
DeploymentTarget = Class(name="DeploymentTarget")
DeployedArtifact = Class(name="DeployedArtifact")
UML2WithID_DecisionNode = Class(name="UML2WithID::DecisionNode")
UML2WithID_DurationConstraint = Class(name="UML2WithID::DurationConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UML2WithID_DeployedArtifact = Class(name="UML2WithID::DeployedArtifact", is_abstract=True)
UML2WithID_Gate = Class(name="UML2WithID::Gate")
MessageEnd = Class(name="MessageEnd")
UML2WithID_CallBehaviorAction = Class(name="UML2WithID::CallBehaviorAction")
CallAction = Class(name="CallAction")
UML2WithID_Interface = Class(name="UML2WithID::Interface")
UML2WithID_Device = Class(name="UML2WithID::Device")
Node = Class(name="Node")
UML2WithID_AssociationClass = Class(name="UML2WithID::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
UML2WithID_Port = Class(name="UML2WithID::Port")
Property_ = Class(name="Property")
UML2WithID_UseCase = Class(name="UML2WithID::UseCase")
BehavioredClassifier = Class(name="BehavioredClassifier")
UML2WithID_BehavioredClassifier = Class(name="UML2WithID::BehavioredClassifier", is_abstract=True)
UML2WithID_CreateObjectAction = Class(name="UML2WithID::CreateObjectAction")
UML2WithID_Interval = Class(name="UML2WithID::Interval")
UML2WithID_BehavioralFeature = Class(name="UML2WithID::BehavioralFeature", is_abstract=True)
Namespace = Class(name="Namespace")
Feature = Class(name="Feature")
UML2WithID_ClearVariableAction = Class(name="UML2WithID::ClearVariableAction")
VariableAction = Class(name="VariableAction")
UML2WithID_IntervalConstraint = Class(name="UML2WithID::IntervalConstraint")
UML2WithID_FinalNode = Class(name="UML2WithID::FinalNode", is_abstract=True)
UML2WithID_ActivityEdge = Class(name="UML2WithID::ActivityEdge", is_abstract=True)
UML2WithID_Signal = Class(name="UML2WithID::Signal")
UML2WithID_TimeInterval = Class(name="UML2WithID::TimeInterval")
Interval = Class(name="Interval")
UML2WithID_ExpansionNode = Class(name="UML2WithID::ExpansionNode")
ObjectNode = Class(name="ObjectNode")
UML2WithID_Association = Class(name="UML2WithID::Association")
UML2WithID_StructuredActivityNode = Class(name="UML2WithID::StructuredActivityNode")
UML2WithID_CombinedFragment = Class(name="UML2WithID::CombinedFragment")
UML2WithID_ExpansionRegion = Class(name="UML2WithID::ExpansionRegion")
UML2WithID_CallAction = Class(name="UML2WithID::CallAction", is_abstract=True)
UML2WithID_Deployment = Class(name="UML2WithID::Deployment")
UML2WithID_InteractionFragment = Class(name="UML2WithID::InteractionFragment", is_abstract=True)
UML2WithID_AddStructuralFeatureValueAction = Class(name="UML2WithID::AddStructuralFeatureValueAction")
UML2WithID_ReadIsClassifiedObjectAction = Class(name="UML2WithID::ReadIsClassifiedObjectAction")
UML2WithID_ConnectionPointReference = Class(name="UML2WithID::ConnectionPointReference")
UML2WithID_InteractionOccurrence = Class(name="UML2WithID::InteractionOccurrence")
UML2WithID_TemplateableClassifier = Class(name="UML2WithID::TemplateableClassifier", is_abstract=True)
UML2WithID_Duration = Class(name="UML2WithID::Duration")
UML2WithID_State = Class(name="UML2WithID::State")
Vertex = Class(name="Vertex")
UML2WithID_LiteralString = Class(name="UML2WithID::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
UML2WithID_Namespace = Class(name="UML2WithID::Namespace", is_abstract=True)
UML2WithID_Trigger = Class(name="UML2WithID::Trigger", is_abstract=True)
UML2WithID_Realization = Class(name="UML2WithID::Realization")
Abstraction = Class(name="Abstraction")
UML2WithID_Stereotype = Class(name="UML2WithID::Stereotype")
UML2WithID_CentralBufferNode = Class(name="UML2WithID::CentralBufferNode")
UML2WithID_DataStoreNode = Class(name="UML2WithID::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2WithID_ReadVariableAction = Class(name="UML2WithID::ReadVariableAction")
UML2WithID_TypedElement = Class(name="UML2WithID::TypedElement", is_abstract=True)
UML2WithID_FinalState = Class(name="UML2WithID::FinalState")
State = Class(name="State")
UML2WithID_ApplyFunctionAction = Class(name="UML2WithID::ApplyFunctionAction")
UML2WithID_Feature = Class(name="UML2WithID::Feature", is_abstract=True)
UML2WithID_DurationInterval = Class(name="UML2WithID::DurationInterval")
UML2WithID_DeploymentTarget = Class(name="UML2WithID::DeploymentTarget", is_abstract=True)
UML2WithID_Behavior = Class(name="UML2WithID::Behavior", is_abstract=True)
UML2WithID_VariableAction = Class(name="UML2WithID::VariableAction", is_abstract=True)
UML2WithID_Continuation = Class(name="UML2WithID::Continuation")
UML2WithID_TimeExpression = Class(name="UML2WithID::TimeExpression")
UML2WithID_TimeObservationAction = Class(name="UML2WithID::TimeObservationAction")
UML2WithID_Constraint = Class(name="UML2WithID::Constraint")
UML2WithID_AcceptCallAction = Class(name="UML2WithID::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UML2WithID_ControlNode = Class(name="UML2WithID::ControlNode", is_abstract=True)
UML2WithID_LiteralNull = Class(name="UML2WithID::LiteralNull")
UML2WithID_ExecutionOccurrence = Class(name="UML2WithID::ExecutionOccurrence")
UML2WithID_InformationFlow = Class(name="UML2WithID::InformationFlow")
UML2WithID_ReadLinkObjectEndQualifierAction = Class(name="UML2WithID::ReadLinkObjectEndQualifierAction")
UML2WithID_Manifestation = Class(name="UML2WithID::Manifestation")
UML2WithID_DestroyObjectAction = Class(name="UML2WithID::DestroyObjectAction")
UML2WithID_ReplyAction = Class(name="UML2WithID::ReplyAction")
UML2WithID_CallTrigger = Class(name="UML2WithID::CallTrigger")
UML2WithID_Pseudostate = Class(name="UML2WithID::Pseudostate")
UML2WithID_Lifeline = Class(name="UML2WithID::Lifeline")
UML2WithID_RemoveStructuralFeatureValueAction = Class(name="UML2WithID::RemoveStructuralFeatureValueAction")
UML2WithID_InputPin = Class(name="UML2WithID::InputPin")
UML2WithID_TimeConstraint = Class(name="UML2WithID::TimeConstraint")
UML2WithID_NamedElement = Class(name="UML2WithID::NamedElement", is_abstract=True)
UML2WithID_Package = Class(name="UML2WithID::Package")
UML2WithID_StructuralFeature = Class(name="UML2WithID::StructuralFeature", is_abstract=True)
UML2WithID_GeneralOrdering = Class(name="UML2WithID::GeneralOrdering")
UML2WithID_Actor = Class(name="UML2WithID::Actor")
UML2WithID_LiteralInteger = Class(name="UML2WithID::LiteralInteger")
UML2WithID_InvocationAction = Class(name="UML2WithID::InvocationAction", is_abstract=True)
UML2WithID_RedefinableElement = Class(name="UML2WithID::RedefinableElement", is_abstract=True)
UML2WithID_Include = Class(name="UML2WithID::Include")
UML2WithID_MessageTrigger = Class(name="UML2WithID::MessageTrigger", is_abstract=True)
Trigger = Class(name="Trigger")
UML2WithID_Class = Class(name="UML2WithID::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2WithID_PartDecomposition = Class(name="UML2WithID::PartDecomposition")
InteractionOccurrence = Class(name="InteractionOccurrence")
UML2WithID_ParameterableClassifier = Class(name="UML2WithID::ParameterableClassifier", is_abstract=True)
UML2WithID_AcceptEventAction = Class(name="UML2WithID::AcceptEventAction")
UML2WithID_Substitution = Class(name="UML2WithID::Substitution")
Realization = Class(name="Realization")
UML2WithID_InformationItem = Class(name="UML2WithID::InformationItem")
UML2WithID_TimeTrigger = Class(name="UML2WithID::TimeTrigger")
UML2WithID_Collaboration = Class(name="UML2WithID::Collaboration")
StructuredClassifier = Class(name="StructuredClassifier")
UML2WithID_AddVariableValueAction = Class(name="UML2WithID::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UML2WithID_ChangeTrigger = Class(name="UML2WithID::ChangeTrigger")
UML2WithID_ControlFlow = Class(name="UML2WithID::ControlFlow")
UML2WithID_PrimitiveType = Class(name="UML2WithID::PrimitiveType")
DataType = Class(name="DataType")
UML2WithID_EncapsulatedClassifier = Class(name="UML2WithID::EncapsulatedClassifier", is_abstract=True)
UML2WithID_Artifact = Class(name="UML2WithID::Artifact")
UML2WithID_ExecutionEnvironment = Class(name="UML2WithID::ExecutionEnvironment")
UML2WithID_ForkNode = Class(name="UML2WithID::ForkNode")
UML2WithID_Property = Class(name="UML2WithID::Property")
StructuralFeature = Class(name="StructuralFeature")
UML2WithID_Variable = Class(name="UML2WithID::Variable")
UML2WithID_Profile = Class(name="UML2WithID::Profile")
Package = Class(name="Package")
UML2WithID_ClearStructuralFeatureAction = Class(name="UML2WithID::ClearStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UML2WithID_Expression = Class(name="UML2WithID::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2WithID_TestIdentityAction = Class(name="UML2WithID::TestIdentityAction")
UML2WithID_CreateLinkAction = Class(name="UML2WithID::CreateLinkAction")
UML2WithID_ProtocolTransition = Class(name="UML2WithID::ProtocolTransition")
Transition = Class(name="Transition")
UML2WithID_ActivityNode = Class(name="UML2WithID::ActivityNode", is_abstract=True)
UML2WithID_Pin = Class(name="UML2WithID::Pin", is_abstract=True)
UML2WithID_ExtensionEnd = Class(name="UML2WithID::ExtensionEnd")
UML2WithID_SignalTrigger = Class(name="UML2WithID::SignalTrigger")
UML2WithID_WriteLinkAction = Class(name="UML2WithID::WriteLinkAction", is_abstract=True)
UML2WithID_WriteVariableAction = Class(name="UML2WithID::WriteVariableAction", is_abstract=True)
UML2WithID_ReclassifyObjectAction = Class(name="UML2WithID::ReclassifyObjectAction")
UML2WithID_RemoveVariableValueAction = Class(name="UML2WithID::RemoveVariableValueAction")
UML2WithID_BroadcastSignalAction = Class(name="UML2WithID::BroadcastSignalAction")
UML2WithID_Node = Class(name="UML2WithID::Node")
UML2WithID_ActivityFinalNode = Class(name="UML2WithID::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
UML2WithID_ObjectNode = Class(name="UML2WithID::ObjectNode", is_abstract=True)
UML2WithID_Vertex = Class(name="UML2WithID::Vertex", is_abstract=True)
UML2WithID_Type = Class(name="UML2WithID::Type", is_abstract=True)
UML2WithID_ParameterSet = Class(name="UML2WithID::ParameterSet")
UML2WithID_EventOccurrence = Class(name="UML2WithID::EventOccurrence")
UML2WithID_StateInvariant = Class(name="UML2WithID::StateInvariant")
UML2WithID_WriteStructuralFeatureAction = Class(name="UML2WithID::WriteStructuralFeatureAction", is_abstract=True)
UML2WithID_LiteralUnlimitedNatural = Class(name="UML2WithID::LiteralUnlimitedNatural")
UML2WithID_LinkAction = Class(name="UML2WithID::LinkAction", is_abstract=True)
UML2WithID_ValuePin = Class(name="UML2WithID::ValuePin")
InputPin = Class(name="InputPin")
UML2WithID_EnumerationLiteral = Class(name="UML2WithID::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
UML2WithID_Reception = Class(name="UML2WithID::Reception")
BehavioralFeature = Class(name="BehavioralFeature")
UML2WithID_InteractionOperand = Class(name="UML2WithID::InteractionOperand")
UML2WithID_ValueSpecification = Class(name="UML2WithID::ValueSpecification", is_abstract=True)
UML2WithID_Component = Class(name="UML2WithID::Component")
UML2WithID_Message = Class(name="UML2WithID::Message")
UML2WithID_Enumeration = Class(name="UML2WithID::Enumeration")
UML2WithID_FlowFinalNode = Class(name="UML2WithID::FlowFinalNode")
UML2WithID_SendObjectAction = Class(name="UML2WithID::SendObjectAction")
UML2WithID_ActivityParameterNode = Class(name="UML2WithID::ActivityParameterNode")
UML2WithID_InitialNode = Class(name="UML2WithID::InitialNode")
UML2WithID_JoinNode = Class(name="UML2WithID::JoinNode")
UML2WithID_Classifier = Class(name="UML2WithID::Classifier", is_abstract=True)
Type = Class(name="Type")
UML2WithID_Region = Class(name="UML2WithID::Region")
UML2WithID_LoopNode = Class(name="UML2WithID::LoopNode")
UML2WithID_PrimitiveFunction = Class(name="UML2WithID::PrimitiveFunction")
UML2WithID_Operation = Class(name="UML2WithID::Operation")
UML2WithID_CommunicationPath = Class(name="UML2WithID::CommunicationPath")
UML2WithID_LiteralBoolean = Class(name="UML2WithID::LiteralBoolean")
UML2WithID_PackageableElement = Class(name="UML2WithID::PackageableElement", is_abstract=True)
UML2WithID_CallOperationAction = Class(name="UML2WithID::CallOperationAction")
UML2WithID_Implementation = Class(name="UML2WithID::Implementation")
UML2WithID_ReadStructuralFeatureAction = Class(name="UML2WithID::ReadStructuralFeatureAction")
UML2WithID_Activity = Class(name="UML2WithID::Activity")
UML2WithID_ExtensionPoint = Class(name="UML2WithID::ExtensionPoint")
UML2WithID_Connector = Class(name="UML2WithID::Connector")
UML2WithID_CollaborationOccurrence = Class(name="UML2WithID::CollaborationOccurrence")
UML2WithID_GeneralizationSet = Class(name="UML2WithID::GeneralizationSet")
UML2WithID_Transition = Class(name="UML2WithID::Transition")
UML2WithID_StructuralFeatureAction = Class(name="UML2WithID::StructuralFeatureAction", is_abstract=True)
UML2WithID_RaiseExceptionAction = Class(name="UML2WithID::RaiseExceptionAction")
UML2WithID_ReadSelfAction = Class(name="UML2WithID::ReadSelfAction")
UML2WithID_ClearAssociationAction = Class(name="UML2WithID::ClearAssociationAction")
UML2WithID_Extend = Class(name="UML2WithID::Extend")
UML2WithID_StructuredClassifier = Class(name="UML2WithID::StructuredClassifier", is_abstract=True)
UML2WithID_Usage = Class(name="UML2WithID::Usage")
UML2WithID_ActivityPartition = Class(name="UML2WithID::ActivityPartition")
UML2WithID_Model = Class(name="UML2WithID::Model")
UML2WithID_Abstraction = Class(name="UML2WithID::Abstraction")
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)

# InvocationAction class attributes and methods

# Element class attributes and methods

# UML2WithID_ConnectableElement class attributes and methods

# NamedElement class attributes and methods

# UML2WithID_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2WithID_SendSignalAction class attributes and methods

# UML2WithID_OutputPin class attributes and methods

# Pin class attributes and methods

# UML2WithID_ConditionalNode class attributes and methods

# StructuredActivityNode class attributes and methods

# UML2WithID_Dependency class attributes and methods

# PackageableElement class attributes and methods

# UML2WithID_MessageEnd class attributes and methods

# UML2WithID_ExecutableNode class attributes and methods

# UML2WithID_ReadExtentAction class attributes and methods

# Action class attributes and methods

# UML2WithID_Permission class attributes and methods

# Dependency class attributes and methods

# UML2WithID_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UML2WithID_Interaction class attributes and methods

# Behavior class attributes and methods

# InteractionFragment class attributes and methods

# UML2WithID_Action class attributes and methods

# ExecutableNode class attributes and methods

# UML2WithID_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# UML2WithID_DurationObservationAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# UML2WithID_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UML2WithID_LiteralSpecification class attributes and methods

# ValueSpecification class attributes and methods

# UML2WithID_InstanceValue class attributes and methods

# UML2WithID_AnyTrigger class attributes and methods

# MessageTrigger class attributes and methods

# UML2WithID_StateMachine class attributes and methods

# UML2WithID_StartOwnedBehaviorAction class attributes and methods

# UML2WithID_RedefinableTemplateSignature class attributes and methods

# RedefinableElement class attributes and methods

# UML2WithID_Parameter class attributes and methods

# ConnectableElement class attributes and methods

# UML2WithID_MergeNode class attributes and methods

# TypedElement class attributes and methods

# ControlNode class attributes and methods

# UML2WithID_Extension class attributes and methods

# UML2WithID_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# ActivityNode class attributes and methods

# UML2WithID_DestroyLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UML2WithID_Stop class attributes and methods

# EventOccurrence class attributes and methods

# UML2WithID_OpaqueExpression class attributes and methods

# UML2WithID_DataType class attributes and methods

# Classifier class attributes and methods

# UML2WithID_ReadLinkObjectEndAction class attributes and methods

# UML2WithID_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2WithID_InstanceSpecification class attributes and methods

# DeploymentTarget class attributes and methods

# DeployedArtifact class attributes and methods

# UML2WithID_DecisionNode class attributes and methods

# UML2WithID_DurationConstraint class attributes and methods

# IntervalConstraint class attributes and methods

# UML2WithID_DeployedArtifact class attributes and methods

# UML2WithID_Gate class attributes and methods

# MessageEnd class attributes and methods

# UML2WithID_CallBehaviorAction class attributes and methods

# CallAction class attributes and methods

# UML2WithID_Interface class attributes and methods

# UML2WithID_Device class attributes and methods

# Node class attributes and methods

# UML2WithID_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# UML2WithID_Port class attributes and methods

# Property class attributes and methods

# UML2WithID_UseCase class attributes and methods

# BehavioredClassifier class attributes and methods

# UML2WithID_BehavioredClassifier class attributes and methods

# UML2WithID_CreateObjectAction class attributes and methods

# UML2WithID_Interval class attributes and methods

# UML2WithID_BehavioralFeature class attributes and methods

# Namespace class attributes and methods

# Feature class attributes and methods

# UML2WithID_ClearVariableAction class attributes and methods

# VariableAction class attributes and methods

# UML2WithID_IntervalConstraint class attributes and methods

# UML2WithID_FinalNode class attributes and methods

# UML2WithID_ActivityEdge class attributes and methods

# UML2WithID_Signal class attributes and methods

# UML2WithID_TimeInterval class attributes and methods

# Interval class attributes and methods

# UML2WithID_ExpansionNode class attributes and methods

# ObjectNode class attributes and methods

# UML2WithID_Association class attributes and methods

# UML2WithID_StructuredActivityNode class attributes and methods

# UML2WithID_CombinedFragment class attributes and methods

# UML2WithID_ExpansionRegion class attributes and methods

# UML2WithID_CallAction class attributes and methods

# UML2WithID_Deployment class attributes and methods

# UML2WithID_InteractionFragment class attributes and methods

# UML2WithID_AddStructuralFeatureValueAction class attributes and methods

# UML2WithID_ReadIsClassifiedObjectAction class attributes and methods

# UML2WithID_ConnectionPointReference class attributes and methods

# UML2WithID_InteractionOccurrence class attributes and methods

# UML2WithID_TemplateableClassifier class attributes and methods

# UML2WithID_Duration class attributes and methods

# UML2WithID_State class attributes and methods

# Vertex class attributes and methods

# UML2WithID_LiteralString class attributes and methods

# LiteralSpecification class attributes and methods

# UML2WithID_Namespace class attributes and methods

# UML2WithID_Trigger class attributes and methods

# UML2WithID_Realization class attributes and methods

# Abstraction class attributes and methods

# UML2WithID_Stereotype class attributes and methods

# UML2WithID_CentralBufferNode class attributes and methods

# UML2WithID_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2WithID_ReadVariableAction class attributes and methods

# UML2WithID_TypedElement class attributes and methods

# UML2WithID_FinalState class attributes and methods

# State class attributes and methods

# UML2WithID_ApplyFunctionAction class attributes and methods

# UML2WithID_Feature class attributes and methods

# UML2WithID_DurationInterval class attributes and methods

# UML2WithID_DeploymentTarget class attributes and methods

# UML2WithID_Behavior class attributes and methods

# UML2WithID_VariableAction class attributes and methods

# UML2WithID_Continuation class attributes and methods

# UML2WithID_TimeExpression class attributes and methods

# UML2WithID_TimeObservationAction class attributes and methods

# UML2WithID_Constraint class attributes and methods

# UML2WithID_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UML2WithID_ControlNode class attributes and methods

# UML2WithID_LiteralNull class attributes and methods

# UML2WithID_ExecutionOccurrence class attributes and methods

# UML2WithID_InformationFlow class attributes and methods

# UML2WithID_ReadLinkObjectEndQualifierAction class attributes and methods

# UML2WithID_Manifestation class attributes and methods

# UML2WithID_DestroyObjectAction class attributes and methods

# UML2WithID_ReplyAction class attributes and methods

# UML2WithID_CallTrigger class attributes and methods

# UML2WithID_Pseudostate class attributes and methods

# UML2WithID_Lifeline class attributes and methods

# UML2WithID_RemoveStructuralFeatureValueAction class attributes and methods

# UML2WithID_InputPin class attributes and methods

# UML2WithID_TimeConstraint class attributes and methods

# UML2WithID_NamedElement class attributes and methods
UML2WithID_NamedElement_name: Property = Property(name="name", type=StringType)
UML2WithID_NamedElement.attributes={UML2WithID_NamedElement_name}

# UML2WithID_Package class attributes and methods

# UML2WithID_StructuralFeature class attributes and methods

# UML2WithID_GeneralOrdering class attributes and methods

# UML2WithID_Actor class attributes and methods

# UML2WithID_LiteralInteger class attributes and methods

# UML2WithID_InvocationAction class attributes and methods

# UML2WithID_RedefinableElement class attributes and methods

# UML2WithID_Include class attributes and methods

# UML2WithID_MessageTrigger class attributes and methods

# Trigger class attributes and methods

# UML2WithID_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2WithID_PartDecomposition class attributes and methods

# InteractionOccurrence class attributes and methods

# UML2WithID_ParameterableClassifier class attributes and methods

# UML2WithID_AcceptEventAction class attributes and methods

# UML2WithID_Substitution class attributes and methods

# Realization class attributes and methods

# UML2WithID_InformationItem class attributes and methods

# UML2WithID_TimeTrigger class attributes and methods

# UML2WithID_Collaboration class attributes and methods

# StructuredClassifier class attributes and methods

# UML2WithID_AddVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# UML2WithID_ChangeTrigger class attributes and methods

# UML2WithID_ControlFlow class attributes and methods

# UML2WithID_PrimitiveType class attributes and methods

# DataType class attributes and methods

# UML2WithID_EncapsulatedClassifier class attributes and methods

# UML2WithID_Artifact class attributes and methods

# UML2WithID_ExecutionEnvironment class attributes and methods

# UML2WithID_ForkNode class attributes and methods

# UML2WithID_Property class attributes and methods

# StructuralFeature class attributes and methods

# UML2WithID_Variable class attributes and methods

# UML2WithID_Profile class attributes and methods

# Package class attributes and methods

# UML2WithID_ClearStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UML2WithID_Expression class attributes and methods

# OpaqueExpression class attributes and methods

# UML2WithID_TestIdentityAction class attributes and methods

# UML2WithID_CreateLinkAction class attributes and methods

# UML2WithID_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# UML2WithID_ActivityNode class attributes and methods

# UML2WithID_Pin class attributes and methods

# UML2WithID_ExtensionEnd class attributes and methods

# UML2WithID_SignalTrigger class attributes and methods

# UML2WithID_WriteLinkAction class attributes and methods

# UML2WithID_WriteVariableAction class attributes and methods

# UML2WithID_ReclassifyObjectAction class attributes and methods

# UML2WithID_RemoveVariableValueAction class attributes and methods

# UML2WithID_BroadcastSignalAction class attributes and methods

# UML2WithID_Node class attributes and methods

# UML2WithID_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# UML2WithID_ObjectNode class attributes and methods

# UML2WithID_Vertex class attributes and methods

# UML2WithID_Type class attributes and methods

# UML2WithID_ParameterSet class attributes and methods

# UML2WithID_EventOccurrence class attributes and methods

# UML2WithID_StateInvariant class attributes and methods

# UML2WithID_WriteStructuralFeatureAction class attributes and methods

# UML2WithID_LiteralUnlimitedNatural class attributes and methods

# UML2WithID_LinkAction class attributes and methods

# UML2WithID_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2WithID_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# UML2WithID_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# UML2WithID_InteractionOperand class attributes and methods

# UML2WithID_ValueSpecification class attributes and methods

# UML2WithID_Component class attributes and methods

# UML2WithID_Message class attributes and methods

# UML2WithID_Enumeration class attributes and methods

# UML2WithID_FlowFinalNode class attributes and methods

# UML2WithID_SendObjectAction class attributes and methods

# UML2WithID_ActivityParameterNode class attributes and methods

# UML2WithID_InitialNode class attributes and methods

# UML2WithID_JoinNode class attributes and methods

# UML2WithID_Classifier class attributes and methods

# Type class attributes and methods

# UML2WithID_Region class attributes and methods

# UML2WithID_LoopNode class attributes and methods

# UML2WithID_PrimitiveFunction class attributes and methods

# UML2WithID_Operation class attributes and methods

# UML2WithID_CommunicationPath class attributes and methods

# UML2WithID_LiteralBoolean class attributes and methods

# UML2WithID_PackageableElement class attributes and methods

# UML2WithID_CallOperationAction class attributes and methods

# UML2WithID_Implementation class attributes and methods

# UML2WithID_ReadStructuralFeatureAction class attributes and methods

# UML2WithID_Activity class attributes and methods

# UML2WithID_ExtensionPoint class attributes and methods

# UML2WithID_Connector class attributes and methods

# UML2WithID_CollaborationOccurrence class attributes and methods

# UML2WithID_GeneralizationSet class attributes and methods

# UML2WithID_Transition class attributes and methods

# UML2WithID_StructuralFeatureAction class attributes and methods

# UML2WithID_RaiseExceptionAction class attributes and methods

# UML2WithID_ReadSelfAction class attributes and methods

# UML2WithID_ClearAssociationAction class attributes and methods

# UML2WithID_Extend class attributes and methods

# UML2WithID_StructuredClassifier class attributes and methods

# UML2WithID_Usage class attributes and methods

# UML2WithID_ActivityPartition class attributes and methods

# UML2WithID_Model class attributes and methods

# UML2WithID_Abstraction class attributes and methods

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# Relationships
subsettedProperty1: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty1",
    ends={
        Property(name="UML2WithID_Property", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Property0", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_UML2WithID_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_SendSignalAction)
gen_UML2WithID_SendSignalAction_Element = Generalization(general=Element, specific=UML2WithID_SendSignalAction)
gen_UML2WithID_ConnectableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ConnectableElement)
gen_UML2WithID_ConnectableElement_Element = Generalization(general=Element, specific=UML2WithID_ConnectableElement)
gen_UML2WithID_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2WithID_DeploymentSpecification)
gen_UML2WithID_DeploymentSpecification_Element = Generalization(general=Element, specific=UML2WithID_DeploymentSpecification)
gen_UML2WithID_MergeNode_Element = Generalization(general=Element, specific=UML2WithID_MergeNode)
gen_UML2WithID_OutputPin_Pin = Generalization(general=Pin, specific=UML2WithID_OutputPin)
gen_UML2WithID_OutputPin_Element = Generalization(general=Element, specific=UML2WithID_OutputPin)
gen_UML2WithID_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_ConditionalNode)
gen_UML2WithID_ConditionalNode_Element = Generalization(general=Element, specific=UML2WithID_ConditionalNode)
gen_UML2WithID_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Dependency)
gen_UML2WithID_Dependency_Element = Generalization(general=Element, specific=UML2WithID_Dependency)
gen_UML2WithID_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_MessageEnd)
gen_UML2WithID_MessageEnd_Element = Generalization(general=Element, specific=UML2WithID_MessageEnd)
gen_UML2WithID_ReadExtentAction_Action = Generalization(general=Action, specific=UML2WithID_ReadExtentAction)
gen_UML2WithID_ReadExtentAction_Element = Generalization(general=Element, specific=UML2WithID_ReadExtentAction)
gen_UML2WithID_Permission_Dependency = Generalization(general=Dependency, specific=UML2WithID_Permission)
gen_UML2WithID_Permission_Element = Generalization(general=Element, specific=UML2WithID_Permission)
gen_UML2WithID_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UML2WithID_CreateLinkObjectAction)
gen_UML2WithID_CreateLinkObjectAction_Element = Generalization(general=Element, specific=UML2WithID_CreateLinkObjectAction)
gen_UML2WithID_Interaction_Behavior = Generalization(general=Behavior, specific=UML2WithID_Interaction)
gen_UML2WithID_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_Interaction)
gen_UML2WithID_Interaction_Element = Generalization(general=Element, specific=UML2WithID_Interaction)
gen_UML2WithID_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=UML2WithID_Action)
gen_UML2WithID_Action_Element = Generalization(general=Element, specific=UML2WithID_Action)
gen_UML2WithID_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2WithID_ObjectFlow)
gen_UML2WithID_ObjectFlow_Element = Generalization(general=Element, specific=UML2WithID_ObjectFlow)
gen_UML2WithID_DurationObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_DurationObservationAction)
gen_UML2WithID_DurationObservationAction_Element = Generalization(general=Element, specific=UML2WithID_DurationObservationAction)
gen_UML2WithID_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2WithID_ReadLinkAction)
gen_UML2WithID_ReadLinkAction_Element = Generalization(general=Element, specific=UML2WithID_ReadLinkAction)
gen_UML2WithID_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_LiteralSpecification)
gen_UML2WithID_LiteralSpecification_Element = Generalization(general=Element, specific=UML2WithID_LiteralSpecification)
gen_UML2WithID_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_InstanceValue)
gen_UML2WithID_InstanceValue_Element = Generalization(general=Element, specific=UML2WithID_InstanceValue)
gen_UML2WithID_AnyTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_AnyTrigger)
gen_UML2WithID_AnyTrigger_Element = Generalization(general=Element, specific=UML2WithID_AnyTrigger)
gen_UML2WithID_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2WithID_StateMachine)
gen_UML2WithID_StateMachine_Element = Generalization(general=Element, specific=UML2WithID_StateMachine)
gen_UML2WithID_StartOwnedBehaviorAction_Action = Generalization(general=Action, specific=UML2WithID_StartOwnedBehaviorAction)
gen_UML2WithID_StartOwnedBehaviorAction_Element = Generalization(general=Element, specific=UML2WithID_StartOwnedBehaviorAction)
gen_UML2WithID_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_RedefinableTemplateSignature)
gen_UML2WithID_RedefinableTemplateSignature_Element = Generalization(general=Element, specific=UML2WithID_RedefinableTemplateSignature)
gen_UML2WithID_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Parameter)
gen_UML2WithID_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Parameter)
gen_UML2WithID_MergeNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_MergeNode)
gen_UML2WithID_Parameter_Element = Generalization(general=Element, specific=UML2WithID_Parameter)
gen_UML2WithID_Extension_Association = Generalization(general=Association, specific=UML2WithID_Extension)
gen_UML2WithID_Extension_Element = Generalization(general=Element, specific=UML2WithID_Extension)
gen_UML2WithID_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UML2WithID_InteractionConstraint)
gen_UML2WithID_InteractionConstraint_Element = Generalization(general=Element, specific=UML2WithID_InteractionConstraint)
gen_UML2WithID_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ExecutableNode)
gen_UML2WithID_ExecutableNode_Element = Generalization(general=Element, specific=UML2WithID_ExecutableNode)
gen_UML2WithID_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2WithID_DestroyLinkAction)
gen_UML2WithID_DestroyLinkAction_Element = Generalization(general=Element, specific=UML2WithID_DestroyLinkAction)
gen_UML2WithID_Stop_EventOccurrence = Generalization(general=EventOccurrence, specific=UML2WithID_Stop)
gen_UML2WithID_Stop_Element = Generalization(general=Element, specific=UML2WithID_Stop)
gen_UML2WithID_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_OpaqueExpression)
gen_UML2WithID_OpaqueExpression_Element = Generalization(general=Element, specific=UML2WithID_OpaqueExpression)
gen_UML2WithID_DataType_Classifier = Generalization(general=Classifier, specific=UML2WithID_DataType)
gen_UML2WithID_DataType_Element = Generalization(general=Element, specific=UML2WithID_DataType)
gen_UML2WithID_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UML2WithID_ReadLinkObjectEndAction)
gen_UML2WithID_ReadLinkObjectEndAction_Element = Generalization(general=Element, specific=UML2WithID_ReadLinkObjectEndAction)
gen_UML2WithID_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_ProtocolStateMachine_Element = Generalization(general=Element, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_InstanceSpecification_Element = Generalization(general=Element, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_DecisionNode)
gen_UML2WithID_DecisionNode_Element = Generalization(general=Element, specific=UML2WithID_DecisionNode)
gen_UML2WithID_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2WithID_DurationConstraint)
gen_UML2WithID_DurationConstraint_Element = Generalization(general=Element, specific=UML2WithID_DurationConstraint)
gen_UML2WithID_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_DeployedArtifact)
gen_UML2WithID_DeployedArtifact_Element = Generalization(general=Element, specific=UML2WithID_DeployedArtifact)
gen_UML2WithID_Gate_MessageEnd = Generalization(general=MessageEnd, specific=UML2WithID_Gate)
gen_UML2WithID_Gate_Element = Generalization(general=Element, specific=UML2WithID_Gate)
gen_UML2WithID_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UML2WithID_CallBehaviorAction)
gen_UML2WithID_CallBehaviorAction_Element = Generalization(general=Element, specific=UML2WithID_CallBehaviorAction)
gen_UML2WithID_Interface_Classifier = Generalization(general=Classifier, specific=UML2WithID_Interface)
gen_UML2WithID_Interface_Element = Generalization(general=Element, specific=UML2WithID_Interface)
gen_UML2WithID_Device_Node = Generalization(general=Node, specific=UML2WithID_Device)
gen_UML2WithID_Device_Element = Generalization(general=Element, specific=UML2WithID_Device)
gen_UML2WithID_AssociationClass_Class = Generalization(general=Class_, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Association = Generalization(general=Association, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Element = Generalization(general=Element, specific=UML2WithID_AssociationClass)
gen_UML2WithID_Port_Property = Generalization(general=Property_, specific=UML2WithID_Port)
gen_UML2WithID_Port_Element = Generalization(general=Element, specific=UML2WithID_Port)
gen_UML2WithID_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_UseCase)
gen_UML2WithID_UseCase_Element = Generalization(general=Element, specific=UML2WithID_UseCase)
gen_UML2WithID_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_BehavioredClassifier_Element = Generalization(general=Element, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_CreateObjectAction_Action = Generalization(general=Action, specific=UML2WithID_CreateObjectAction)
gen_UML2WithID_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_Interval)
gen_UML2WithID_Interval_Element = Generalization(general=Element, specific=UML2WithID_Interval)
gen_UML2WithID_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_BehavioralFeature_Feature = Generalization(general=Feature, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_BehavioralFeature_Element = Generalization(general=Element, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_ClearVariableAction)
gen_UML2WithID_ClearVariableAction_Element = Generalization(general=Element, specific=UML2WithID_ClearVariableAction)
gen_UML2WithID_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UML2WithID_IntervalConstraint)
gen_UML2WithID_IntervalConstraint_Element = Generalization(general=Element, specific=UML2WithID_IntervalConstraint)
gen_UML2WithID_FinalNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_FinalNode)
gen_UML2WithID_FinalNode_Element = Generalization(general=Element, specific=UML2WithID_FinalNode)
gen_UML2WithID_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ActivityEdge)
gen_UML2WithID_ActivityEdge_Element = Generalization(general=Element, specific=UML2WithID_ActivityEdge)
gen_UML2WithID_Signal_Classifier = Generalization(general=Classifier, specific=UML2WithID_Signal)
gen_UML2WithID_Signal_Element = Generalization(general=Element, specific=UML2WithID_Signal)
gen_UML2WithID_TimeInterval_Interval = Generalization(general=Interval, specific=UML2WithID_TimeInterval)
gen_UML2WithID_TimeInterval_Element = Generalization(general=Element, specific=UML2WithID_TimeInterval)
gen_UML2WithID_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_ExpansionNode)
gen_UML2WithID_ExpansionNode_Element = Generalization(general=Element, specific=UML2WithID_ExpansionNode)
gen_UML2WithID_Association_Classifier = Generalization(general=Classifier, specific=UML2WithID_Association)
gen_UML2WithID_Association_Element = Generalization(general=Element, specific=UML2WithID_Association)
gen_UML2WithID_StructuredActivityNode_Action = Generalization(general=Action, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_StructuredActivityNode_Element = Generalization(general=Element, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_CombinedFragment)
gen_UML2WithID_CombinedFragment_Element = Generalization(general=Element, specific=UML2WithID_CombinedFragment)
gen_UML2WithID_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_ExpansionRegion)
gen_UML2WithID_ExpansionRegion_Element = Generalization(general=Element, specific=UML2WithID_ExpansionRegion)
gen_UML2WithID_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_CallAction)
gen_UML2WithID_CallAction_Element = Generalization(general=Element, specific=UML2WithID_CallAction)
gen_UML2WithID_Deployment_Dependency = Generalization(general=Dependency, specific=UML2WithID_Deployment)
gen_UML2WithID_Deployment_Element = Generalization(general=Element, specific=UML2WithID_Deployment)
gen_UML2WithID_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_InteractionFragment)
gen_UML2WithID_InteractionFragment_Element = Generalization(general=Element, specific=UML2WithID_InteractionFragment)
gen_UML2WithID_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_AddStructuralFeatureValueAction)
gen_UML2WithID_AddStructuralFeatureValueAction_Element = Generalization(general=Element, specific=UML2WithID_AddStructuralFeatureValueAction)
gen_UML2WithID_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UML2WithID_ReadIsClassifiedObjectAction)
gen_UML2WithID_ReadIsClassifiedObjectAction_Element = Generalization(general=Element, specific=UML2WithID_ReadIsClassifiedObjectAction)
gen_UML2WithID_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=UML2WithID_ConnectionPointReference)
gen_UML2WithID_ConnectionPointReference_Element = Generalization(general=Element, specific=UML2WithID_ConnectionPointReference)
gen_UML2WithID_CreateObjectAction_Element = Generalization(general=Element, specific=UML2WithID_CreateObjectAction)
gen_UML2WithID_InteractionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_InteractionOccurrence)
gen_UML2WithID_InteractionOccurrence_Element = Generalization(general=Element, specific=UML2WithID_InteractionOccurrence)
gen_UML2WithID_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_TemplateableClassifier)
gen_UML2WithID_TemplateableClassifier_Element = Generalization(general=Element, specific=UML2WithID_TemplateableClassifier)
gen_UML2WithID_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_Duration)
gen_UML2WithID_Duration_Element = Generalization(general=Element, specific=UML2WithID_Duration)
gen_UML2WithID_State_Namespace = Generalization(general=Namespace, specific=UML2WithID_State)
gen_UML2WithID_State_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_State)
gen_UML2WithID_State_Vertex = Generalization(general=Vertex, specific=UML2WithID_State)
gen_UML2WithID_State_Element = Generalization(general=Element, specific=UML2WithID_State)
gen_UML2WithID_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralString)
gen_UML2WithID_LiteralString_Element = Generalization(general=Element, specific=UML2WithID_LiteralString)
gen_UML2WithID_Namespace_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Namespace)
gen_UML2WithID_Namespace_Element = Generalization(general=Element, specific=UML2WithID_Namespace)
gen_UML2WithID_Trigger_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Trigger)
gen_UML2WithID_Trigger_Element = Generalization(general=Element, specific=UML2WithID_Trigger)
gen_UML2WithID_Realization_Abstraction = Generalization(general=Abstraction, specific=UML2WithID_Realization)
gen_UML2WithID_Realization_Element = Generalization(general=Element, specific=UML2WithID_Realization)
gen_UML2WithID_Stereotype_Class = Generalization(general=Class_, specific=UML2WithID_Stereotype)
gen_UML2WithID_Stereotype_Element = Generalization(general=Element, specific=UML2WithID_Stereotype)
gen_UML2WithID_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_CentralBufferNode)
gen_UML2WithID_CentralBufferNode_Element = Generalization(general=Element, specific=UML2WithID_CentralBufferNode)
gen_UML2WithID_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2WithID_DataStoreNode)
gen_UML2WithID_DataStoreNode_Element = Generalization(general=Element, specific=UML2WithID_DataStoreNode)
gen_UML2WithID_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_ReadVariableAction)
gen_UML2WithID_ReadVariableAction_Element = Generalization(general=Element, specific=UML2WithID_ReadVariableAction)
gen_UML2WithID_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_TypedElement)
gen_UML2WithID_TypedElement_Element = Generalization(general=Element, specific=UML2WithID_TypedElement)
gen_UML2WithID_FinalState_State = Generalization(general=State, specific=UML2WithID_FinalState)
gen_UML2WithID_FinalState_Element = Generalization(general=Element, specific=UML2WithID_FinalState)
gen_UML2WithID_ApplyFunctionAction_Action = Generalization(general=Action, specific=UML2WithID_ApplyFunctionAction)
gen_UML2WithID_ApplyFunctionAction_Element = Generalization(general=Element, specific=UML2WithID_ApplyFunctionAction)
gen_UML2WithID_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Feature)
gen_UML2WithID_Feature_Element = Generalization(general=Element, specific=UML2WithID_Feature)
gen_UML2WithID_DurationInterval_Interval = Generalization(general=Interval, specific=UML2WithID_DurationInterval)
gen_UML2WithID_DurationInterval_Element = Generalization(general=Element, specific=UML2WithID_DurationInterval)
gen_UML2WithID_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_DeploymentTarget)
gen_UML2WithID_DeploymentTarget_Element = Generalization(general=Element, specific=UML2WithID_DeploymentTarget)
gen_UML2WithID_Behavior_Class = Generalization(general=Class_, specific=UML2WithID_Behavior)
gen_UML2WithID_VariableAction_Action = Generalization(general=Action, specific=UML2WithID_VariableAction)
gen_UML2WithID_VariableAction_Element = Generalization(general=Element, specific=UML2WithID_VariableAction)
gen_UML2WithID_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_Continuation)
gen_UML2WithID_Continuation_Element = Generalization(general=Element, specific=UML2WithID_Continuation)
gen_UML2WithID_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_TimeExpression)
gen_UML2WithID_TimeExpression_Element = Generalization(general=Element, specific=UML2WithID_TimeExpression)
gen_UML2WithID_TimeObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_TimeObservationAction)
gen_UML2WithID_TimeObservationAction_Element = Generalization(general=Element, specific=UML2WithID_TimeObservationAction)
gen_UML2WithID_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Constraint)
gen_UML2WithID_Constraint_Element = Generalization(general=Element, specific=UML2WithID_Constraint)
gen_UML2WithID_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UML2WithID_AcceptCallAction)
gen_UML2WithID_AcceptCallAction_Element = Generalization(general=Element, specific=UML2WithID_AcceptCallAction)
gen_UML2WithID_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ControlNode)
gen_UML2WithID_ControlNode_Element = Generalization(general=Element, specific=UML2WithID_ControlNode)
gen_UML2WithID_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralNull)
gen_UML2WithID_LiteralNull_Element = Generalization(general=Element, specific=UML2WithID_LiteralNull)
gen_UML2WithID_ExecutionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_ExecutionOccurrence)
gen_UML2WithID_ExecutionOccurrence_Element = Generalization(general=Element, specific=UML2WithID_ExecutionOccurrence)
gen_UML2WithID_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_InformationFlow)
gen_UML2WithID_InformationFlow_Element = Generalization(general=Element, specific=UML2WithID_InformationFlow)
gen_UML2WithID_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UML2WithID_ReadLinkObjectEndQualifierAction)
gen_UML2WithID_ReadLinkObjectEndQualifierAction_Element = Generalization(general=Element, specific=UML2WithID_ReadLinkObjectEndQualifierAction)
gen_UML2WithID_Manifestation_Abstraction = Generalization(general=Abstraction, specific=UML2WithID_Manifestation)
gen_UML2WithID_Manifestation_Element = Generalization(general=Element, specific=UML2WithID_Manifestation)
gen_UML2WithID_DestroyObjectAction_Action = Generalization(general=Action, specific=UML2WithID_DestroyObjectAction)
gen_UML2WithID_DestroyObjectAction_Element = Generalization(general=Element, specific=UML2WithID_DestroyObjectAction)
gen_UML2WithID_ReplyAction_Action = Generalization(general=Action, specific=UML2WithID_ReplyAction)
gen_UML2WithID_ReplyAction_Element = Generalization(general=Element, specific=UML2WithID_ReplyAction)
gen_UML2WithID_CallTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_CallTrigger)
gen_UML2WithID_CallTrigger_Element = Generalization(general=Element, specific=UML2WithID_CallTrigger)
gen_UML2WithID_PartDecomposition_InteractionOccurrence = Generalization(general=InteractionOccurrence, specific=UML2WithID_PartDecomposition)
gen_UML2WithID_PartDecomposition_Element = Generalization(general=Element, specific=UML2WithID_PartDecomposition)
gen_UML2WithID_Pseudostate_Vertex = Generalization(general=Vertex, specific=UML2WithID_Pseudostate)
gen_UML2WithID_Pseudostate_Element = Generalization(general=Element, specific=UML2WithID_Pseudostate)
gen_UML2WithID_Lifeline_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Lifeline)
gen_UML2WithID_Lifeline_Element = Generalization(general=Element, specific=UML2WithID_Lifeline)
gen_UML2WithID_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_RemoveStructuralFeatureValueAction)
gen_UML2WithID_RemoveStructuralFeatureValueAction_Element = Generalization(general=Element, specific=UML2WithID_RemoveStructuralFeatureValueAction)
gen_UML2WithID_InputPin_Pin = Generalization(general=Pin, specific=UML2WithID_InputPin)
gen_UML2WithID_InputPin_Element = Generalization(general=Element, specific=UML2WithID_InputPin)
gen_UML2WithID_Behavior_Element = Generalization(general=Element, specific=UML2WithID_Behavior)
gen_UML2WithID_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2WithID_TimeConstraint)
gen_UML2WithID_TimeConstraint_Element = Generalization(general=Element, specific=UML2WithID_TimeConstraint)
gen_UML2WithID_NamedElement_Element = Generalization(general=Element, specific=UML2WithID_NamedElement)
gen_UML2WithID_Package_Namespace = Generalization(general=Namespace, specific=UML2WithID_Package)
gen_UML2WithID_Package_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Package)
gen_UML2WithID_Package_Element = Generalization(general=Element, specific=UML2WithID_Package)
gen_UML2WithID_StructuralFeature_Feature = Generalization(general=Feature, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_StructuralFeature_Element = Generalization(general=Element, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_GeneralOrdering)
gen_UML2WithID_GeneralOrdering_Element = Generalization(general=Element, specific=UML2WithID_GeneralOrdering)
gen_UML2WithID_Actor_Classifier = Generalization(general=Classifier, specific=UML2WithID_Actor)
gen_UML2WithID_Actor_Element = Generalization(general=Element, specific=UML2WithID_Actor)
gen_UML2WithID_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralInteger)
gen_UML2WithID_LiteralInteger_Element = Generalization(general=Element, specific=UML2WithID_LiteralInteger)
gen_UML2WithID_InvocationAction_Action = Generalization(general=Action, specific=UML2WithID_InvocationAction)
gen_UML2WithID_InvocationAction_Element = Generalization(general=Element, specific=UML2WithID_InvocationAction)
gen_UML2WithID_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_RedefinableElement)
gen_UML2WithID_RedefinableElement_Element = Generalization(general=Element, specific=UML2WithID_RedefinableElement)
gen_UML2WithID_Include_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Include)
gen_UML2WithID_Include_Element = Generalization(general=Element, specific=UML2WithID_Include)
gen_UML2WithID_MessageTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_MessageTrigger)
gen_UML2WithID_MessageTrigger_Element = Generalization(general=Element, specific=UML2WithID_MessageTrigger)
gen_UML2WithID_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_Element = Generalization(general=Element, specific=UML2WithID_Class)
gen_UML2WithID_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Property)
gen_UML2WithID_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_Property)
gen_UML2WithID_Property_Element = Generalization(general=Element, specific=UML2WithID_Property)
gen_UML2WithID_AcceptEventAction_Action = Generalization(general=Action, specific=UML2WithID_AcceptEventAction)
gen_UML2WithID_AcceptEventAction_Element = Generalization(general=Element, specific=UML2WithID_AcceptEventAction)
gen_UML2WithID_Substitution_Realization = Generalization(general=Realization, specific=UML2WithID_Substitution)
gen_UML2WithID_Substitution_Element = Generalization(general=Element, specific=UML2WithID_Substitution)
gen_UML2WithID_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2WithID_InformationItem)
gen_UML2WithID_InformationItem_Element = Generalization(general=Element, specific=UML2WithID_InformationItem)
gen_UML2WithID_TimeTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_TimeTrigger)
gen_UML2WithID_TimeTrigger_Element = Generalization(general=Element, specific=UML2WithID_TimeTrigger)
gen_UML2WithID_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_Element = Generalization(general=Element, specific=UML2WithID_Collaboration)
gen_UML2WithID_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2WithID_AddVariableValueAction)
gen_UML2WithID_AddVariableValueAction_Element = Generalization(general=Element, specific=UML2WithID_AddVariableValueAction)
gen_UML2WithID_ChangeTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_ChangeTrigger)
gen_UML2WithID_ChangeTrigger_Element = Generalization(general=Element, specific=UML2WithID_ChangeTrigger)
gen_UML2WithID_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2WithID_ControlFlow)
gen_UML2WithID_ControlFlow_Element = Generalization(general=Element, specific=UML2WithID_ControlFlow)
gen_UML2WithID_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2WithID_PrimitiveType)
gen_UML2WithID_PrimitiveType_Element = Generalization(general=Element, specific=UML2WithID_PrimitiveType)
gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_EncapsulatedClassifier)
gen_UML2WithID_EncapsulatedClassifier_Element = Generalization(general=Element, specific=UML2WithID_EncapsulatedClassifier)
gen_UML2WithID_Artifact_Classifier = Generalization(general=Classifier, specific=UML2WithID_Artifact)
gen_UML2WithID_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2WithID_Artifact)
gen_UML2WithID_Artifact_Element = Generalization(general=Element, specific=UML2WithID_Artifact)
gen_UML2WithID_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_ExecutionEnvironment_Element = Generalization(general=Element, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_ForkNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_ForkNode)
gen_UML2WithID_ForkNode_Element = Generalization(general=Element, specific=UML2WithID_ForkNode)
gen_UML2WithID_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2WithID_Property)
gen_UML2WithID_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Variable)
gen_UML2WithID_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Variable)
gen_UML2WithID_Variable_Element = Generalization(general=Element, specific=UML2WithID_Variable)
gen_UML2WithID_Profile_Package = Generalization(general=Package, specific=UML2WithID_Profile)
gen_UML2WithID_Profile_Element = Generalization(general=Element, specific=UML2WithID_Profile)
gen_UML2WithID_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_ClearStructuralFeatureAction)
gen_UML2WithID_ClearStructuralFeatureAction_Element = Generalization(general=Element, specific=UML2WithID_ClearStructuralFeatureAction)
gen_UML2WithID_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2WithID_Expression)
gen_UML2WithID_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_ParameterableClassifier)
gen_UML2WithID_ParameterableClassifier_Element = Generalization(general=Element, specific=UML2WithID_ParameterableClassifier)
gen_UML2WithID_TestIdentityAction_Action = Generalization(general=Action, specific=UML2WithID_TestIdentityAction)
gen_UML2WithID_TestIdentityAction_Element = Generalization(general=Element, specific=UML2WithID_TestIdentityAction)
gen_UML2WithID_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2WithID_CreateLinkAction)
gen_UML2WithID_CreateLinkAction_Element = Generalization(general=Element, specific=UML2WithID_CreateLinkAction)
gen_UML2WithID_ProtocolTransition_Transition = Generalization(general=Transition, specific=UML2WithID_ProtocolTransition)
gen_UML2WithID_ProtocolTransition_Element = Generalization(general=Element, specific=UML2WithID_ProtocolTransition)
gen_UML2WithID_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ActivityNode)
gen_UML2WithID_ActivityNode_Element = Generalization(general=Element, specific=UML2WithID_ActivityNode)
gen_UML2WithID_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_Pin)
gen_UML2WithID_Pin_Element = Generalization(general=Element, specific=UML2WithID_Pin)
gen_UML2WithID_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_ExtensionEnd_Element = Generalization(general=Element, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_SignalTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_SignalTrigger)
gen_UML2WithID_SignalTrigger_Element = Generalization(general=Element, specific=UML2WithID_SignalTrigger)
gen_UML2WithID_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2WithID_WriteLinkAction)
gen_UML2WithID_WriteLinkAction_Element = Generalization(general=Element, specific=UML2WithID_WriteLinkAction)
gen_UML2WithID_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_WriteVariableAction)
gen_UML2WithID_WriteVariableAction_Element = Generalization(general=Element, specific=UML2WithID_WriteVariableAction)
gen_UML2WithID_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UML2WithID_ReclassifyObjectAction)
gen_UML2WithID_ReclassifyObjectAction_Element = Generalization(general=Element, specific=UML2WithID_ReclassifyObjectAction)
gen_UML2WithID_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2WithID_RemoveVariableValueAction)
gen_UML2WithID_RemoveVariableValueAction_Element = Generalization(general=Element, specific=UML2WithID_RemoveVariableValueAction)
gen_UML2WithID_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_BroadcastSignalAction)
gen_UML2WithID_BroadcastSignalAction_Element = Generalization(general=Element, specific=UML2WithID_BroadcastSignalAction)
gen_UML2WithID_Node_Class = Generalization(general=Class_, specific=UML2WithID_Node)
gen_UML2WithID_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_Node)
gen_UML2WithID_Node_Element = Generalization(general=Element, specific=UML2WithID_Node)
gen_UML2WithID_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2WithID_ActivityFinalNode)
gen_UML2WithID_ActivityFinalNode_Element = Generalization(general=Element, specific=UML2WithID_ActivityFinalNode)
gen_UML2WithID_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ObjectNode)
gen_UML2WithID_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_ObjectNode)
gen_UML2WithID_ObjectNode_Element = Generalization(general=Element, specific=UML2WithID_ObjectNode)
gen_UML2WithID_Vertex_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Vertex)
gen_UML2WithID_Vertex_Element = Generalization(general=Element, specific=UML2WithID_Vertex)
gen_UML2WithID_Expression_Element = Generalization(general=Element, specific=UML2WithID_Expression)
gen_UML2WithID_Type_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Type)
gen_UML2WithID_Type_Element = Generalization(general=Element, specific=UML2WithID_Type)
gen_UML2WithID_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ParameterSet)
gen_UML2WithID_ParameterSet_Element = Generalization(general=Element, specific=UML2WithID_ParameterSet)
gen_UML2WithID_EventOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_EventOccurrence)
gen_UML2WithID_EventOccurrence_MessageEnd = Generalization(general=MessageEnd, specific=UML2WithID_EventOccurrence)
gen_UML2WithID_EventOccurrence_Element = Generalization(general=Element, specific=UML2WithID_EventOccurrence)
gen_UML2WithID_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_StateInvariant)
gen_UML2WithID_StateInvariant_Element = Generalization(general=Element, specific=UML2WithID_StateInvariant)
gen_UML2WithID_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_WriteStructuralFeatureAction)
gen_UML2WithID_WriteStructuralFeatureAction_Element = Generalization(general=Element, specific=UML2WithID_WriteStructuralFeatureAction)
gen_UML2WithID_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralUnlimitedNatural)
gen_UML2WithID_LiteralUnlimitedNatural_Element = Generalization(general=Element, specific=UML2WithID_LiteralUnlimitedNatural)
gen_UML2WithID_LinkAction_Action = Generalization(general=Action, specific=UML2WithID_LinkAction)
gen_UML2WithID_LinkAction_Element = Generalization(general=Element, specific=UML2WithID_LinkAction)
gen_UML2WithID_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2WithID_ValuePin)
gen_UML2WithID_ValuePin_Element = Generalization(general=Element, specific=UML2WithID_ValuePin)
gen_UML2WithID_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=UML2WithID_EnumerationLiteral)
gen_UML2WithID_EnumerationLiteral_Element = Generalization(general=Element, specific=UML2WithID_EnumerationLiteral)
gen_UML2WithID_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Reception)
gen_UML2WithID_Reception_Element = Generalization(general=Element, specific=UML2WithID_Reception)
gen_UML2WithID_InteractionOperand_Namespace = Generalization(general=Namespace, specific=UML2WithID_InteractionOperand)
gen_UML2WithID_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_InteractionOperand)
gen_UML2WithID_InteractionOperand_Element = Generalization(general=Element, specific=UML2WithID_InteractionOperand)
gen_UML2WithID_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_ValueSpecification)
gen_UML2WithID_ValueSpecification_Element = Generalization(general=Element, specific=UML2WithID_ValueSpecification)
gen_UML2WithID_Component_Class = Generalization(general=Class_, specific=UML2WithID_Component)
gen_UML2WithID_Component_Element = Generalization(general=Element, specific=UML2WithID_Component)
gen_UML2WithID_Implementation_Element = Generalization(general=Element, specific=UML2WithID_Implementation)
gen_UML2WithID_Message_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Message)
gen_UML2WithID_Message_Element = Generalization(general=Element, specific=UML2WithID_Message)
gen_UML2WithID_Enumeration_DataType = Generalization(general=DataType, specific=UML2WithID_Enumeration)
gen_UML2WithID_Enumeration_Element = Generalization(general=Element, specific=UML2WithID_Enumeration)
gen_UML2WithID_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2WithID_FlowFinalNode)
gen_UML2WithID_FlowFinalNode_Element = Generalization(general=Element, specific=UML2WithID_FlowFinalNode)
gen_UML2WithID_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_ActivityParameterNode)
gen_UML2WithID_ActivityParameterNode_Element = Generalization(general=Element, specific=UML2WithID_ActivityParameterNode)
gen_UML2WithID_InitialNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_InitialNode)
gen_UML2WithID_InitialNode_Element = Generalization(general=Element, specific=UML2WithID_InitialNode)
gen_UML2WithID_JoinNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_JoinNode)
gen_UML2WithID_JoinNode_Element = Generalization(general=Element, specific=UML2WithID_JoinNode)
gen_UML2WithID_Classifier_Namespace = Generalization(general=Namespace, specific=UML2WithID_Classifier)
gen_UML2WithID_Classifier_Type = Generalization(general=Type, specific=UML2WithID_Classifier)
gen_UML2WithID_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Classifier)
gen_UML2WithID_Classifier_Element = Generalization(general=Element, specific=UML2WithID_Classifier)
gen_UML2WithID_Region_Namespace = Generalization(general=Namespace, specific=UML2WithID_Region)
gen_UML2WithID_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Region)
gen_UML2WithID_Region_Element = Generalization(general=Element, specific=UML2WithID_Region)
gen_UML2WithID_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_LoopNode)
gen_UML2WithID_LoopNode_Element = Generalization(general=Element, specific=UML2WithID_LoopNode)
gen_UML2WithID_PrimitiveFunction_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_PrimitiveFunction)
gen_UML2WithID_PrimitiveFunction_Element = Generalization(general=Element, specific=UML2WithID_PrimitiveFunction)
gen_UML2WithID_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_Element = Generalization(general=Element, specific=UML2WithID_Operation)
gen_UML2WithID_CommunicationPath_Association = Generalization(general=Association, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_CommunicationPath_Element = Generalization(general=Element, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralBoolean)
gen_UML2WithID_LiteralBoolean_Element = Generalization(general=Element, specific=UML2WithID_LiteralBoolean)
gen_UML2WithID_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_PackageableElement)
gen_UML2WithID_PackageableElement_Element = Generalization(general=Element, specific=UML2WithID_PackageableElement)
gen_UML2WithID_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UML2WithID_CallOperationAction)
gen_UML2WithID_CallOperationAction_Element = Generalization(general=Element, specific=UML2WithID_CallOperationAction)
gen_UML2WithID_Implementation_Realization = Generalization(general=Realization, specific=UML2WithID_Implementation)
gen_UML2WithID_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_ReadStructuralFeatureAction)
gen_UML2WithID_ReadStructuralFeatureAction_Element = Generalization(general=Element, specific=UML2WithID_ReadStructuralFeatureAction)
gen_UML2WithID_Activity_Behavior = Generalization(general=Behavior, specific=UML2WithID_Activity)
gen_UML2WithID_Activity_Element = Generalization(general=Element, specific=UML2WithID_Activity)
gen_UML2WithID_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ExtensionPoint)
gen_UML2WithID_ExtensionPoint_Element = Generalization(general=Element, specific=UML2WithID_ExtensionPoint)
gen_UML2WithID_Connector_Feature = Generalization(general=Feature, specific=UML2WithID_Connector)
gen_UML2WithID_Connector_Element = Generalization(general=Element, specific=UML2WithID_Connector)
gen_UML2WithID_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_SendObjectAction)
gen_UML2WithID_SendObjectAction_Element = Generalization(general=Element, specific=UML2WithID_SendObjectAction)
gen_UML2WithID_CollaborationOccurrence_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_CollaborationOccurrence)
gen_UML2WithID_CollaborationOccurrence_Element = Generalization(general=Element, specific=UML2WithID_CollaborationOccurrence)
gen_UML2WithID_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_GeneralizationSet)
gen_UML2WithID_GeneralizationSet_Element = Generalization(general=Element, specific=UML2WithID_GeneralizationSet)
gen_UML2WithID_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Transition)
gen_UML2WithID_Transition_Element = Generalization(general=Element, specific=UML2WithID_Transition)
gen_UML2WithID_StructuralFeatureAction_Action = Generalization(general=Action, specific=UML2WithID_StructuralFeatureAction)
gen_UML2WithID_StructuralFeatureAction_Element = Generalization(general=Element, specific=UML2WithID_StructuralFeatureAction)
gen_UML2WithID_RaiseExceptionAction_Action = Generalization(general=Action, specific=UML2WithID_RaiseExceptionAction)
gen_UML2WithID_RaiseExceptionAction_Element = Generalization(general=Element, specific=UML2WithID_RaiseExceptionAction)
gen_UML2WithID_ReadSelfAction_Action = Generalization(general=Action, specific=UML2WithID_ReadSelfAction)
gen_UML2WithID_ReadSelfAction_Element = Generalization(general=Element, specific=UML2WithID_ReadSelfAction)
gen_UML2WithID_ClearAssociationAction_Action = Generalization(general=Action, specific=UML2WithID_ClearAssociationAction)
gen_UML2WithID_ClearAssociationAction_Element = Generalization(general=Element, specific=UML2WithID_ClearAssociationAction)
gen_UML2WithID_Extend_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Extend)
gen_UML2WithID_Extend_Element = Generalization(general=Element, specific=UML2WithID_Extend)
gen_UML2WithID_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_StructuredClassifier)
gen_UML2WithID_StructuredClassifier_Element = Generalization(general=Element, specific=UML2WithID_StructuredClassifier)
gen_UML2WithID_Usage_Dependency = Generalization(general=Dependency, specific=UML2WithID_Usage)
gen_UML2WithID_Usage_Element = Generalization(general=Element, specific=UML2WithID_Usage)
gen_UML2WithID_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ActivityPartition)
gen_UML2WithID_ActivityPartition_Element = Generalization(general=Element, specific=UML2WithID_ActivityPartition)
gen_UML2WithID_Model_Package = Generalization(general=Package, specific=UML2WithID_Model)
gen_UML2WithID_Model_Element = Generalization(general=Element, specific=UML2WithID_Model)
gen_UML2WithID_Abstraction_Dependency = Generalization(general=Dependency, specific=UML2WithID_Abstraction)
gen_UML2WithID_Abstraction_Element = Generalization(general=Element, specific=UML2WithID_Abstraction)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={InvocationAction, Element, UML2WithID_ConnectableElement, NamedElement, UML2WithID_DeploymentSpecification, Artifact, UML2WithID_SendSignalAction, UML2WithID_OutputPin, Pin, UML2WithID_ConditionalNode, StructuredActivityNode, UML2WithID_Dependency, PackageableElement, UML2WithID_MessageEnd, UML2WithID_ExecutableNode, UML2WithID_ReadExtentAction, Action, UML2WithID_Permission, Dependency, UML2WithID_CreateLinkObjectAction, CreateLinkAction, UML2WithID_Interaction, Behavior, InteractionFragment, UML2WithID_Action, ExecutableNode, UML2WithID_ObjectFlow, ActivityEdge, UML2WithID_DurationObservationAction, WriteStructuralFeatureAction, UML2WithID_ReadLinkAction, LinkAction, UML2WithID_LiteralSpecification, ValueSpecification, UML2WithID_InstanceValue, UML2WithID_AnyTrigger, MessageTrigger, UML2WithID_StateMachine, UML2WithID_StartOwnedBehaviorAction, UML2WithID_RedefinableTemplateSignature, RedefinableElement, UML2WithID_Parameter, ConnectableElement, UML2WithID_MergeNode, TypedElement, ControlNode, UML2WithID_Extension, UML2WithID_InteractionConstraint, Constraint, ActivityNode, UML2WithID_DestroyLinkAction, WriteLinkAction, UML2WithID_Stop, EventOccurrence, UML2WithID_OpaqueExpression, UML2WithID_DataType, Classifier, UML2WithID_ReadLinkObjectEndAction, UML2WithID_ProtocolStateMachine, StateMachine, UML2WithID_InstanceSpecification, DeploymentTarget, DeployedArtifact, UML2WithID_DecisionNode, UML2WithID_DurationConstraint, IntervalConstraint, UML2WithID_DeployedArtifact, UML2WithID_Gate, MessageEnd, UML2WithID_CallBehaviorAction, CallAction, UML2WithID_Interface, UML2WithID_Device, Node, UML2WithID_AssociationClass, Class_, Association, UML2WithID_Port, Property_, UML2WithID_UseCase, BehavioredClassifier, UML2WithID_BehavioredClassifier, UML2WithID_CreateObjectAction, UML2WithID_Interval, UML2WithID_BehavioralFeature, Namespace, Feature, UML2WithID_ClearVariableAction, VariableAction, UML2WithID_IntervalConstraint, UML2WithID_FinalNode, UML2WithID_ActivityEdge, UML2WithID_Signal, UML2WithID_TimeInterval, Interval, UML2WithID_ExpansionNode, ObjectNode, UML2WithID_Association, UML2WithID_StructuredActivityNode, UML2WithID_CombinedFragment, UML2WithID_ExpansionRegion, UML2WithID_CallAction, UML2WithID_Deployment, UML2WithID_InteractionFragment, UML2WithID_AddStructuralFeatureValueAction, UML2WithID_ReadIsClassifiedObjectAction, UML2WithID_ConnectionPointReference, UML2WithID_InteractionOccurrence, UML2WithID_TemplateableClassifier, UML2WithID_Duration, UML2WithID_State, Vertex, UML2WithID_LiteralString, LiteralSpecification, UML2WithID_Namespace, UML2WithID_Trigger, UML2WithID_Realization, Abstraction, UML2WithID_Stereotype, UML2WithID_CentralBufferNode, UML2WithID_DataStoreNode, CentralBufferNode, UML2WithID_ReadVariableAction, UML2WithID_TypedElement, UML2WithID_FinalState, State, UML2WithID_ApplyFunctionAction, UML2WithID_Feature, UML2WithID_DurationInterval, UML2WithID_DeploymentTarget, UML2WithID_Behavior, UML2WithID_VariableAction, UML2WithID_Continuation, UML2WithID_TimeExpression, UML2WithID_TimeObservationAction, UML2WithID_Constraint, UML2WithID_AcceptCallAction, AcceptEventAction, UML2WithID_ControlNode, UML2WithID_LiteralNull, UML2WithID_ExecutionOccurrence, UML2WithID_InformationFlow, UML2WithID_ReadLinkObjectEndQualifierAction, UML2WithID_Manifestation, UML2WithID_DestroyObjectAction, UML2WithID_ReplyAction, UML2WithID_CallTrigger, UML2WithID_Pseudostate, UML2WithID_Lifeline, UML2WithID_RemoveStructuralFeatureValueAction, UML2WithID_InputPin, UML2WithID_TimeConstraint, UML2WithID_NamedElement, UML2WithID_Package, UML2WithID_StructuralFeature, UML2WithID_GeneralOrdering, UML2WithID_Actor, UML2WithID_LiteralInteger, UML2WithID_InvocationAction, UML2WithID_RedefinableElement, UML2WithID_Include, UML2WithID_MessageTrigger, Trigger, UML2WithID_Class, EncapsulatedClassifier, UML2WithID_PartDecomposition, InteractionOccurrence, UML2WithID_ParameterableClassifier, UML2WithID_AcceptEventAction, UML2WithID_Substitution, Realization, UML2WithID_InformationItem, UML2WithID_TimeTrigger, UML2WithID_Collaboration, StructuredClassifier, UML2WithID_AddVariableValueAction, WriteVariableAction, UML2WithID_ChangeTrigger, UML2WithID_ControlFlow, UML2WithID_PrimitiveType, DataType, UML2WithID_EncapsulatedClassifier, UML2WithID_Artifact, UML2WithID_ExecutionEnvironment, UML2WithID_ForkNode, UML2WithID_Property, StructuralFeature, UML2WithID_Variable, UML2WithID_Profile, Package, UML2WithID_ClearStructuralFeatureAction, StructuralFeatureAction, UML2WithID_Expression, OpaqueExpression, UML2WithID_TestIdentityAction, UML2WithID_CreateLinkAction, UML2WithID_ProtocolTransition, Transition, UML2WithID_ActivityNode, UML2WithID_Pin, UML2WithID_ExtensionEnd, UML2WithID_SignalTrigger, UML2WithID_WriteLinkAction, UML2WithID_WriteVariableAction, UML2WithID_ReclassifyObjectAction, UML2WithID_RemoveVariableValueAction, UML2WithID_BroadcastSignalAction, UML2WithID_Node, UML2WithID_ActivityFinalNode, FinalNode, UML2WithID_ObjectNode, UML2WithID_Vertex, UML2WithID_Type, UML2WithID_ParameterSet, UML2WithID_EventOccurrence, UML2WithID_StateInvariant, UML2WithID_WriteStructuralFeatureAction, UML2WithID_LiteralUnlimitedNatural, UML2WithID_LinkAction, UML2WithID_ValuePin, InputPin, UML2WithID_EnumerationLiteral, InstanceSpecification, UML2WithID_Reception, BehavioralFeature, UML2WithID_InteractionOperand, UML2WithID_ValueSpecification, UML2WithID_Component, UML2WithID_Message, UML2WithID_Enumeration, UML2WithID_FlowFinalNode, UML2WithID_SendObjectAction, UML2WithID_ActivityParameterNode, UML2WithID_InitialNode, UML2WithID_JoinNode, UML2WithID_Classifier, Type, UML2WithID_Region, UML2WithID_LoopNode, UML2WithID_PrimitiveFunction, UML2WithID_Operation, UML2WithID_CommunicationPath, UML2WithID_LiteralBoolean, UML2WithID_PackageableElement, UML2WithID_CallOperationAction, UML2WithID_Implementation, UML2WithID_ReadStructuralFeatureAction, UML2WithID_Activity, UML2WithID_ExtensionPoint, UML2WithID_Connector, UML2WithID_CollaborationOccurrence, UML2WithID_GeneralizationSet, UML2WithID_Transition, UML2WithID_StructuralFeatureAction, UML2WithID_RaiseExceptionAction, UML2WithID_ReadSelfAction, UML2WithID_ClearAssociationAction, UML2WithID_Extend, UML2WithID_StructuredClassifier, UML2WithID_Usage, UML2WithID_ActivityPartition, UML2WithID_Model, UML2WithID_Abstraction, UML2WithID_Element},
    associations={subsettedProperty1},
    generalizations={gen_UML2WithID_SendSignalAction_InvocationAction, gen_UML2WithID_SendSignalAction_Element, gen_UML2WithID_ConnectableElement_NamedElement, gen_UML2WithID_ConnectableElement_Element, gen_UML2WithID_DeploymentSpecification_Artifact, gen_UML2WithID_DeploymentSpecification_Element, gen_UML2WithID_MergeNode_Element, gen_UML2WithID_OutputPin_Pin, gen_UML2WithID_OutputPin_Element, gen_UML2WithID_ConditionalNode_StructuredActivityNode, gen_UML2WithID_ConditionalNode_Element, gen_UML2WithID_Dependency_PackageableElement, gen_UML2WithID_Dependency_Element, gen_UML2WithID_MessageEnd_NamedElement, gen_UML2WithID_MessageEnd_Element, gen_UML2WithID_ReadExtentAction_Action, gen_UML2WithID_ReadExtentAction_Element, gen_UML2WithID_Permission_Dependency, gen_UML2WithID_Permission_Element, gen_UML2WithID_CreateLinkObjectAction_CreateLinkAction, gen_UML2WithID_CreateLinkObjectAction_Element, gen_UML2WithID_Interaction_Behavior, gen_UML2WithID_Interaction_InteractionFragment, gen_UML2WithID_Interaction_Element, gen_UML2WithID_Action_ExecutableNode, gen_UML2WithID_Action_Element, gen_UML2WithID_ObjectFlow_ActivityEdge, gen_UML2WithID_ObjectFlow_Element, gen_UML2WithID_DurationObservationAction_WriteStructuralFeatureAction, gen_UML2WithID_DurationObservationAction_Element, gen_UML2WithID_ReadLinkAction_LinkAction, gen_UML2WithID_ReadLinkAction_Element, gen_UML2WithID_LiteralSpecification_ValueSpecification, gen_UML2WithID_LiteralSpecification_Element, gen_UML2WithID_InstanceValue_ValueSpecification, gen_UML2WithID_InstanceValue_Element, gen_UML2WithID_AnyTrigger_MessageTrigger, gen_UML2WithID_AnyTrigger_Element, gen_UML2WithID_StateMachine_Behavior, gen_UML2WithID_StateMachine_Element, gen_UML2WithID_StartOwnedBehaviorAction_Action, gen_UML2WithID_StartOwnedBehaviorAction_Element, gen_UML2WithID_RedefinableTemplateSignature_RedefinableElement, gen_UML2WithID_RedefinableTemplateSignature_Element, gen_UML2WithID_Parameter_ConnectableElement, gen_UML2WithID_Parameter_TypedElement, gen_UML2WithID_MergeNode_ControlNode, gen_UML2WithID_Parameter_Element, gen_UML2WithID_Extension_Association, gen_UML2WithID_Extension_Element, gen_UML2WithID_InteractionConstraint_Constraint, gen_UML2WithID_InteractionConstraint_Element, gen_UML2WithID_ExecutableNode_ActivityNode, gen_UML2WithID_ExecutableNode_Element, gen_UML2WithID_DestroyLinkAction_WriteLinkAction, gen_UML2WithID_DestroyLinkAction_Element, gen_UML2WithID_Stop_EventOccurrence, gen_UML2WithID_Stop_Element, gen_UML2WithID_OpaqueExpression_ValueSpecification, gen_UML2WithID_OpaqueExpression_Element, gen_UML2WithID_DataType_Classifier, gen_UML2WithID_DataType_Element, gen_UML2WithID_ReadLinkObjectEndAction_Action, gen_UML2WithID_ReadLinkObjectEndAction_Element, gen_UML2WithID_ProtocolStateMachine_StateMachine, gen_UML2WithID_ProtocolStateMachine_Element, gen_UML2WithID_InstanceSpecification_PackageableElement, gen_UML2WithID_InstanceSpecification_DeploymentTarget, gen_UML2WithID_InstanceSpecification_DeployedArtifact, gen_UML2WithID_InstanceSpecification_Element, gen_UML2WithID_DecisionNode_ControlNode, gen_UML2WithID_DecisionNode_Element, gen_UML2WithID_DurationConstraint_IntervalConstraint, gen_UML2WithID_DurationConstraint_Element, gen_UML2WithID_DeployedArtifact_NamedElement, gen_UML2WithID_DeployedArtifact_Element, gen_UML2WithID_Gate_MessageEnd, gen_UML2WithID_Gate_Element, gen_UML2WithID_CallBehaviorAction_CallAction, gen_UML2WithID_CallBehaviorAction_Element, gen_UML2WithID_Interface_Classifier, gen_UML2WithID_Interface_Element, gen_UML2WithID_Device_Node, gen_UML2WithID_Device_Element, gen_UML2WithID_AssociationClass_Class, gen_UML2WithID_AssociationClass_Association, gen_UML2WithID_AssociationClass_Element, gen_UML2WithID_Port_Property, gen_UML2WithID_Port_Element, gen_UML2WithID_UseCase_BehavioredClassifier, gen_UML2WithID_UseCase_Element, gen_UML2WithID_BehavioredClassifier_Classifier, gen_UML2WithID_BehavioredClassifier_Element, gen_UML2WithID_CreateObjectAction_Action, gen_UML2WithID_Interval_ValueSpecification, gen_UML2WithID_Interval_Element, gen_UML2WithID_BehavioralFeature_Namespace, gen_UML2WithID_BehavioralFeature_Feature, gen_UML2WithID_BehavioralFeature_Element, gen_UML2WithID_ClearVariableAction_VariableAction, gen_UML2WithID_ClearVariableAction_Element, gen_UML2WithID_IntervalConstraint_Constraint, gen_UML2WithID_IntervalConstraint_Element, gen_UML2WithID_FinalNode_ControlNode, gen_UML2WithID_FinalNode_Element, gen_UML2WithID_ActivityEdge_RedefinableElement, gen_UML2WithID_ActivityEdge_Element, gen_UML2WithID_Signal_Classifier, gen_UML2WithID_Signal_Element, gen_UML2WithID_TimeInterval_Interval, gen_UML2WithID_TimeInterval_Element, gen_UML2WithID_ExpansionNode_ObjectNode, gen_UML2WithID_ExpansionNode_Element, gen_UML2WithID_Association_Classifier, gen_UML2WithID_Association_Element, gen_UML2WithID_StructuredActivityNode_Action, gen_UML2WithID_StructuredActivityNode_Namespace, gen_UML2WithID_StructuredActivityNode_Element, gen_UML2WithID_CombinedFragment_InteractionFragment, gen_UML2WithID_CombinedFragment_Element, gen_UML2WithID_ExpansionRegion_StructuredActivityNode, gen_UML2WithID_ExpansionRegion_Element, gen_UML2WithID_CallAction_InvocationAction, gen_UML2WithID_CallAction_Element, gen_UML2WithID_Deployment_Dependency, gen_UML2WithID_Deployment_Element, gen_UML2WithID_InteractionFragment_NamedElement, gen_UML2WithID_InteractionFragment_Element, gen_UML2WithID_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2WithID_AddStructuralFeatureValueAction_Element, gen_UML2WithID_ReadIsClassifiedObjectAction_Action, gen_UML2WithID_ReadIsClassifiedObjectAction_Element, gen_UML2WithID_ConnectionPointReference_Vertex, gen_UML2WithID_ConnectionPointReference_Element, gen_UML2WithID_CreateObjectAction_Element, gen_UML2WithID_InteractionOccurrence_InteractionFragment, gen_UML2WithID_InteractionOccurrence_Element, gen_UML2WithID_TemplateableClassifier_Classifier, gen_UML2WithID_TemplateableClassifier_Element, gen_UML2WithID_Duration_ValueSpecification, gen_UML2WithID_Duration_Element, gen_UML2WithID_State_Namespace, gen_UML2WithID_State_RedefinableElement, gen_UML2WithID_State_Vertex, gen_UML2WithID_State_Element, gen_UML2WithID_LiteralString_LiteralSpecification, gen_UML2WithID_LiteralString_Element, gen_UML2WithID_Namespace_NamedElement, gen_UML2WithID_Namespace_Element, gen_UML2WithID_Trigger_NamedElement, gen_UML2WithID_Trigger_Element, gen_UML2WithID_Realization_Abstraction, gen_UML2WithID_Realization_Element, gen_UML2WithID_Stereotype_Class, gen_UML2WithID_Stereotype_Element, gen_UML2WithID_CentralBufferNode_ObjectNode, gen_UML2WithID_CentralBufferNode_Element, gen_UML2WithID_DataStoreNode_CentralBufferNode, gen_UML2WithID_DataStoreNode_Element, gen_UML2WithID_ReadVariableAction_VariableAction, gen_UML2WithID_ReadVariableAction_Element, gen_UML2WithID_TypedElement_NamedElement, gen_UML2WithID_TypedElement_Element, gen_UML2WithID_FinalState_State, gen_UML2WithID_FinalState_Element, gen_UML2WithID_ApplyFunctionAction_Action, gen_UML2WithID_ApplyFunctionAction_Element, gen_UML2WithID_Feature_RedefinableElement, gen_UML2WithID_Feature_Element, gen_UML2WithID_DurationInterval_Interval, gen_UML2WithID_DurationInterval_Element, gen_UML2WithID_DeploymentTarget_NamedElement, gen_UML2WithID_DeploymentTarget_Element, gen_UML2WithID_Behavior_Class, gen_UML2WithID_VariableAction_Action, gen_UML2WithID_VariableAction_Element, gen_UML2WithID_Continuation_InteractionFragment, gen_UML2WithID_Continuation_Element, gen_UML2WithID_TimeExpression_ValueSpecification, gen_UML2WithID_TimeExpression_Element, gen_UML2WithID_TimeObservationAction_WriteStructuralFeatureAction, gen_UML2WithID_TimeObservationAction_Element, gen_UML2WithID_Constraint_PackageableElement, gen_UML2WithID_Constraint_Element, gen_UML2WithID_AcceptCallAction_AcceptEventAction, gen_UML2WithID_AcceptCallAction_Element, gen_UML2WithID_ControlNode_ActivityNode, gen_UML2WithID_ControlNode_Element, gen_UML2WithID_LiteralNull_LiteralSpecification, gen_UML2WithID_LiteralNull_Element, gen_UML2WithID_ExecutionOccurrence_InteractionFragment, gen_UML2WithID_ExecutionOccurrence_Element, gen_UML2WithID_InformationFlow_PackageableElement, gen_UML2WithID_InformationFlow_Element, gen_UML2WithID_ReadLinkObjectEndQualifierAction_Action, gen_UML2WithID_ReadLinkObjectEndQualifierAction_Element, gen_UML2WithID_Manifestation_Abstraction, gen_UML2WithID_Manifestation_Element, gen_UML2WithID_DestroyObjectAction_Action, gen_UML2WithID_DestroyObjectAction_Element, gen_UML2WithID_ReplyAction_Action, gen_UML2WithID_ReplyAction_Element, gen_UML2WithID_CallTrigger_MessageTrigger, gen_UML2WithID_CallTrigger_Element, gen_UML2WithID_PartDecomposition_InteractionOccurrence, gen_UML2WithID_PartDecomposition_Element, gen_UML2WithID_Pseudostate_Vertex, gen_UML2WithID_Pseudostate_Element, gen_UML2WithID_Lifeline_NamedElement, gen_UML2WithID_Lifeline_Element, gen_UML2WithID_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2WithID_RemoveStructuralFeatureValueAction_Element, gen_UML2WithID_InputPin_Pin, gen_UML2WithID_InputPin_Element, gen_UML2WithID_Behavior_Element, gen_UML2WithID_TimeConstraint_IntervalConstraint, gen_UML2WithID_TimeConstraint_Element, gen_UML2WithID_NamedElement_Element, gen_UML2WithID_Package_Namespace, gen_UML2WithID_Package_PackageableElement, gen_UML2WithID_Package_Element, gen_UML2WithID_StructuralFeature_Feature, gen_UML2WithID_StructuralFeature_TypedElement, gen_UML2WithID_StructuralFeature_Element, gen_UML2WithID_GeneralOrdering_NamedElement, gen_UML2WithID_GeneralOrdering_Element, gen_UML2WithID_Actor_Classifier, gen_UML2WithID_Actor_Element, gen_UML2WithID_LiteralInteger_LiteralSpecification, gen_UML2WithID_LiteralInteger_Element, gen_UML2WithID_InvocationAction_Action, gen_UML2WithID_InvocationAction_Element, gen_UML2WithID_RedefinableElement_NamedElement, gen_UML2WithID_RedefinableElement_Element, gen_UML2WithID_Include_NamedElement, gen_UML2WithID_Include_Element, gen_UML2WithID_MessageTrigger_Trigger, gen_UML2WithID_MessageTrigger_Element, gen_UML2WithID_Class_BehavioredClassifier, gen_UML2WithID_Class_EncapsulatedClassifier, gen_UML2WithID_Class_Element, gen_UML2WithID_Property_ConnectableElement, gen_UML2WithID_Property_DeploymentTarget, gen_UML2WithID_Property_Element, gen_UML2WithID_AcceptEventAction_Action, gen_UML2WithID_AcceptEventAction_Element, gen_UML2WithID_Substitution_Realization, gen_UML2WithID_Substitution_Element, gen_UML2WithID_InformationItem_Classifier, gen_UML2WithID_InformationItem_Element, gen_UML2WithID_TimeTrigger_Trigger, gen_UML2WithID_TimeTrigger_Element, gen_UML2WithID_Collaboration_BehavioredClassifier, gen_UML2WithID_Collaboration_StructuredClassifier, gen_UML2WithID_Collaboration_Element, gen_UML2WithID_AddVariableValueAction_WriteVariableAction, gen_UML2WithID_AddVariableValueAction_Element, gen_UML2WithID_ChangeTrigger_Trigger, gen_UML2WithID_ChangeTrigger_Element, gen_UML2WithID_ControlFlow_ActivityEdge, gen_UML2WithID_ControlFlow_Element, gen_UML2WithID_PrimitiveType_DataType, gen_UML2WithID_PrimitiveType_Element, gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier, gen_UML2WithID_EncapsulatedClassifier_Element, gen_UML2WithID_Artifact_Classifier, gen_UML2WithID_Artifact_DeployedArtifact, gen_UML2WithID_Artifact_Element, gen_UML2WithID_ExecutionEnvironment_Node, gen_UML2WithID_ExecutionEnvironment_Element, gen_UML2WithID_ForkNode_ControlNode, gen_UML2WithID_ForkNode_Element, gen_UML2WithID_Property_StructuralFeature, gen_UML2WithID_Variable_ConnectableElement, gen_UML2WithID_Variable_TypedElement, gen_UML2WithID_Variable_Element, gen_UML2WithID_Profile_Package, gen_UML2WithID_Profile_Element, gen_UML2WithID_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_ClearStructuralFeatureAction_Element, gen_UML2WithID_Expression_OpaqueExpression, gen_UML2WithID_ParameterableClassifier_Classifier, gen_UML2WithID_ParameterableClassifier_Element, gen_UML2WithID_TestIdentityAction_Action, gen_UML2WithID_TestIdentityAction_Element, gen_UML2WithID_CreateLinkAction_WriteLinkAction, gen_UML2WithID_CreateLinkAction_Element, gen_UML2WithID_ProtocolTransition_Transition, gen_UML2WithID_ProtocolTransition_Element, gen_UML2WithID_ActivityNode_RedefinableElement, gen_UML2WithID_ActivityNode_Element, gen_UML2WithID_Pin_ObjectNode, gen_UML2WithID_Pin_Element, gen_UML2WithID_ExtensionEnd_Property, gen_UML2WithID_ExtensionEnd_Element, gen_UML2WithID_SignalTrigger_MessageTrigger, gen_UML2WithID_SignalTrigger_Element, gen_UML2WithID_WriteLinkAction_LinkAction, gen_UML2WithID_WriteLinkAction_Element, gen_UML2WithID_WriteVariableAction_VariableAction, gen_UML2WithID_WriteVariableAction_Element, gen_UML2WithID_ReclassifyObjectAction_Action, gen_UML2WithID_ReclassifyObjectAction_Element, gen_UML2WithID_RemoveVariableValueAction_WriteVariableAction, gen_UML2WithID_RemoveVariableValueAction_Element, gen_UML2WithID_BroadcastSignalAction_InvocationAction, gen_UML2WithID_BroadcastSignalAction_Element, gen_UML2WithID_Node_Class, gen_UML2WithID_Node_DeploymentTarget, gen_UML2WithID_Node_Element, gen_UML2WithID_ActivityFinalNode_FinalNode, gen_UML2WithID_ActivityFinalNode_Element, gen_UML2WithID_ObjectNode_ActivityNode, gen_UML2WithID_ObjectNode_TypedElement, gen_UML2WithID_ObjectNode_Element, gen_UML2WithID_Vertex_NamedElement, gen_UML2WithID_Vertex_Element, gen_UML2WithID_Expression_Element, gen_UML2WithID_Type_PackageableElement, gen_UML2WithID_Type_Element, gen_UML2WithID_ParameterSet_NamedElement, gen_UML2WithID_ParameterSet_Element, gen_UML2WithID_EventOccurrence_InteractionFragment, gen_UML2WithID_EventOccurrence_MessageEnd, gen_UML2WithID_EventOccurrence_Element, gen_UML2WithID_StateInvariant_InteractionFragment, gen_UML2WithID_StateInvariant_Element, gen_UML2WithID_WriteStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_WriteStructuralFeatureAction_Element, gen_UML2WithID_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2WithID_LiteralUnlimitedNatural_Element, gen_UML2WithID_LinkAction_Action, gen_UML2WithID_LinkAction_Element, gen_UML2WithID_ValuePin_InputPin, gen_UML2WithID_ValuePin_Element, gen_UML2WithID_EnumerationLiteral_InstanceSpecification, gen_UML2WithID_EnumerationLiteral_Element, gen_UML2WithID_Reception_BehavioralFeature, gen_UML2WithID_Reception_Element, gen_UML2WithID_InteractionOperand_Namespace, gen_UML2WithID_InteractionOperand_InteractionFragment, gen_UML2WithID_InteractionOperand_Element, gen_UML2WithID_ValueSpecification_TypedElement, gen_UML2WithID_ValueSpecification_Element, gen_UML2WithID_Component_Class, gen_UML2WithID_Component_Element, gen_UML2WithID_Implementation_Element, gen_UML2WithID_Message_NamedElement, gen_UML2WithID_Message_Element, gen_UML2WithID_Enumeration_DataType, gen_UML2WithID_Enumeration_Element, gen_UML2WithID_FlowFinalNode_FinalNode, gen_UML2WithID_FlowFinalNode_Element, gen_UML2WithID_ActivityParameterNode_ObjectNode, gen_UML2WithID_ActivityParameterNode_Element, gen_UML2WithID_InitialNode_ControlNode, gen_UML2WithID_InitialNode_Element, gen_UML2WithID_JoinNode_ControlNode, gen_UML2WithID_JoinNode_Element, gen_UML2WithID_Classifier_Namespace, gen_UML2WithID_Classifier_Type, gen_UML2WithID_Classifier_RedefinableElement, gen_UML2WithID_Classifier_Element, gen_UML2WithID_Region_Namespace, gen_UML2WithID_Region_RedefinableElement, gen_UML2WithID_Region_Element, gen_UML2WithID_LoopNode_StructuredActivityNode, gen_UML2WithID_LoopNode_Element, gen_UML2WithID_PrimitiveFunction_PackageableElement, gen_UML2WithID_PrimitiveFunction_Element, gen_UML2WithID_Operation_BehavioralFeature, gen_UML2WithID_Operation_TypedElement, gen_UML2WithID_Operation_Element, gen_UML2WithID_CommunicationPath_Association, gen_UML2WithID_CommunicationPath_Element, gen_UML2WithID_LiteralBoolean_LiteralSpecification, gen_UML2WithID_LiteralBoolean_Element, gen_UML2WithID_PackageableElement_NamedElement, gen_UML2WithID_PackageableElement_Element, gen_UML2WithID_CallOperationAction_CallAction, gen_UML2WithID_CallOperationAction_Element, gen_UML2WithID_Implementation_Realization, gen_UML2WithID_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_ReadStructuralFeatureAction_Element, gen_UML2WithID_Activity_Behavior, gen_UML2WithID_Activity_Element, gen_UML2WithID_ExtensionPoint_RedefinableElement, gen_UML2WithID_ExtensionPoint_Element, gen_UML2WithID_Connector_Feature, gen_UML2WithID_Connector_Element, gen_UML2WithID_SendObjectAction_InvocationAction, gen_UML2WithID_SendObjectAction_Element, gen_UML2WithID_CollaborationOccurrence_NamedElement, gen_UML2WithID_CollaborationOccurrence_Element, gen_UML2WithID_GeneralizationSet_PackageableElement, gen_UML2WithID_GeneralizationSet_Element, gen_UML2WithID_Transition_RedefinableElement, gen_UML2WithID_Transition_Element, gen_UML2WithID_StructuralFeatureAction_Action, gen_UML2WithID_StructuralFeatureAction_Element, gen_UML2WithID_RaiseExceptionAction_Action, gen_UML2WithID_RaiseExceptionAction_Element, gen_UML2WithID_ReadSelfAction_Action, gen_UML2WithID_ReadSelfAction_Element, gen_UML2WithID_ClearAssociationAction_Action, gen_UML2WithID_ClearAssociationAction_Element, gen_UML2WithID_Extend_NamedElement, gen_UML2WithID_Extend_Element, gen_UML2WithID_StructuredClassifier_Classifier, gen_UML2WithID_StructuredClassifier_Element, gen_UML2WithID_Usage_Dependency, gen_UML2WithID_Usage_Element, gen_UML2WithID_ActivityPartition_NamedElement, gen_UML2WithID_ActivityPartition_Element, gen_UML2WithID_Model_Package, gen_UML2WithID_Model_Element, gen_UML2WithID_Abstraction_Dependency, gen_UML2WithID_Abstraction_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)