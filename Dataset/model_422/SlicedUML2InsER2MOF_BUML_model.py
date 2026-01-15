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
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="composite"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="package"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public")
    }
)

# Classes
UML2_ParameterSet = Class(name="UML2::ParameterSet")
NamedElement = Class(name="NamedElement")
UML2_TemplateableElement = Class(name="UML2::TemplateableElement")
Element = Class(name="Element")
UML2_ElementImport = Class(name="UML2::ElementImport")
DirectedRelationship = Class(name="DirectedRelationship")
UML2_PackageableElement = Class(name="UML2::PackageableElement")
UML2_ExtensionPoint = Class(name="UML2::ExtensionPoint")
RedefinableElement = Class(name="RedefinableElement")
UML2_CallAction = Class(name="UML2::CallAction")
InvocationAction = Class(name="InvocationAction")
UML2_TimeInterval = Class(name="UML2::TimeInterval")
Interval = Class(name="Interval")
UML2_StructuredClassifier = Class(name="UML2::StructuredClassifier")
Classifier = Class(name="Classifier")
UML2_SendSignalAction = Class(name="UML2::SendSignalAction")
UML2_DataStoreNode = Class(name="UML2::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2_Pseudostate = Class(name="UML2::Pseudostate")
Vertex = Class(name="Vertex")
UML2_DurationInterval = Class(name="UML2::DurationInterval")
UML2_ControlFlow = Class(name="UML2::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
UML2_LiteralString = Class(name="UML2::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
UML2_LinkEndData = Class(name="UML2::LinkEndData")
UML2_InputPin = Class(name="UML2::InputPin")
UML2_Property = Class(name="UML2::Property")
UML2_QualifierValue = Class(name="UML2::QualifierValue")
UML2_PrimitiveFunction = Class(name="UML2::PrimitiveFunction")
PackageableElement = Class(name="PackageableElement")
UML2_DeployedArtifact = Class(name="UML2::DeployedArtifact")
UML2_RemoveStructuralFeatureValueAction = Class(name="UML2::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UML2_Interval = Class(name="UML2::Interval")
ValueSpecification = Class(name="ValueSpecification")
UML2_ClearAssociationAction = Class(name="UML2::ClearAssociationAction")
UML2_Dependency = Class(name="UML2::Dependency")
UML2_RedefinableTemplateSignature = Class(name="UML2::RedefinableTemplateSignature")
TemplateSignature = Class(name="TemplateSignature")
UML2_FlowFinalNode = Class(name="UML2::FlowFinalNode")
FinalNode = Class(name="FinalNode")
UML2_ReadIsClassifiedObjectAction = Class(name="UML2::ReadIsClassifiedObjectAction")
Action = Class(name="Action")
UML2_TimeTrigger = Class(name="UML2::TimeTrigger")
Trigger = Class(name="Trigger")
UML2_Generalization = Class(name="UML2::Generalization")
UML2_Classifier = Class(name="UML2::Classifier")
UML2_ActivityParameterNode = Class(name="UML2::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
UML2_Feature = Class(name="UML2::Feature")
UML2_Parameter = Class(name="UML2::Parameter")
ConnectableElement = Class(name="ConnectableElement")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
UML2_MessageTrigger = Class(name="UML2::MessageTrigger")
UML2_CombinedFragment = Class(name="UML2::CombinedFragment")
InteractionFragment = Class(name="InteractionFragment")
UML2_DestroyObjectAction = Class(name="UML2::DestroyObjectAction")
UML2_CreateObjectAction = Class(name="UML2::CreateObjectAction")
UML2_OutputPin = Class(name="UML2::OutputPin")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
Node = Class(name="Node")
UML2_Gate = Class(name="UML2::Gate")
MessageEnd = Class(name="MessageEnd")
UML2_DurationConstraint = Class(name="UML2::DurationConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UML2_DeploymentSpecification = Class(name="UML2::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2_PrimitiveType = Class(name="UML2::PrimitiveType")
DataType = Class(name="DataType")
UML2_Action = Class(name="UML2::Action")
ExecutableNode = Class(name="ExecutableNode")
UML2_Node = Class(name="UML2::Node")
Class_ = Class(name="Class")
DeploymentTarget = Class(name="DeploymentTarget")
UML2_WriteStructuralFeatureAction = Class(name="UML2::WriteStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UML2_WriteVariableAction = Class(name="UML2::WriteVariableAction")
VariableAction = Class(name="VariableAction")
UML2_InstanceSpecification = Class(name="UML2::InstanceSpecification")
DeployedArtifact = Class(name="DeployedArtifact")
UML2_Slot = Class(name="UML2::Slot")
UML2_Element = Class(name="UML2::Element")
UML2_TemplateableClassifier = Class(name="UML2::TemplateableClassifier")
UML2_FinalNode = Class(name="UML2::FinalNode")
ControlNode = Class(name="ControlNode")
UML2_LiteralUnlimitedNatural = Class(name="UML2::LiteralUnlimitedNatural")
UML2_StructuralFeatureAction = Class(name="UML2::StructuralFeatureAction")
UML2_StructuralFeature = Class(name="UML2::StructuralFeature")
UML2_LiteralBoolean = Class(name="UML2::LiteralBoolean")
UML2_TypedElement = Class(name="UML2::TypedElement")
UML2_Type = Class(name="UML2::Type")
UML2_PartDecomposition = Class(name="UML2::PartDecomposition")
InteractionOccurrence = Class(name="InteractionOccurrence")
UML2_OpaqueExpression = Class(name="UML2::OpaqueExpression")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_ReadExtentAction = Class(name="UML2::ReadExtentAction")
UML2_CentralBufferNode = Class(name="UML2::CentralBufferNode")
UML2_Package = Class(name="UML2::Package")
Namespace = Class(name="Namespace")
UML2_Variable = Class(name="UML2::Variable")
UML2_Manifestation = Class(name="UML2::Manifestation")
Abstraction = Class(name="Abstraction")
UML2_Trigger = Class(name="UML2::Trigger")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_ClearStructuralFeatureAction = Class(name="UML2::ClearStructuralFeatureAction")
UML2_Continuation = Class(name="UML2::Continuation")
UML2_InteractionOccurrence = Class(name="UML2::InteractionOccurrence")
UML2_InteractionConstraint = Class(name="UML2::InteractionConstraint")
Constraint = Class(name="Constraint")
UML2_ReadStructuralFeatureAction = Class(name="UML2::ReadStructuralFeatureAction")
UML2_InstanceValue = Class(name="UML2::InstanceValue")
UML2_JoinNode = Class(name="UML2::JoinNode")
UML2_DataType = Class(name="UML2::DataType")
UML2_Enumeration = Class(name="UML2::Enumeration")
UML2_ReadLinkAction = Class(name="UML2::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UML2_AddStructuralFeatureValueAction = Class(name="UML2::AddStructuralFeatureValueAction")
UML2_InformationItem = Class(name="UML2::InformationItem")
UML2_ActivityPartition = Class(name="UML2::ActivityPartition")
ActivityGroup = Class(name="ActivityGroup")
UML2_ObjectNode = Class(name="UML2::ObjectNode")
ActivityNode = Class(name="ActivityNode")
UML2_Port = Class(name="UML2::Port")
Property_ = Class(name="Property")
UML2_TemplateParameter = Class(name="UML2::TemplateParameter")
UML2_Realization = Class(name="UML2::Realization")
UML2_ReadVariableAction = Class(name="UML2::ReadVariableAction")
UML2_Artifact = Class(name="UML2::Artifact")
UML2_ClassifierTemplateParameter = Class(name="UML2::ClassifierTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
UML2_Pin = Class(name="UML2::Pin")
UML2_ParameterableElement = Class(name="UML2::ParameterableElement")
UML2_Constraint = Class(name="UML2::Constraint")
UML2_Message = Class(name="UML2::Message")
UML2_EnumerationLiteral = Class(name="UML2::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
Feature = Class(name="Feature")
UML2_Association = Class(name="UML2::Association")
Relationship = Class(name="Relationship")
Pin = Class(name="Pin")
UML2_TimeConstraint = Class(name="UML2::TimeConstraint")
UML2_InvocationAction = Class(name="UML2::InvocationAction")
UML2_TestIdentityAction = Class(name="UML2::TestIdentityAction")
UML2_StateMachine = Class(name="UML2::StateMachine")
Behavior = Class(name="Behavior")
UML2_ReadLinkObjectEndAction = Class(name="UML2::ReadLinkObjectEndAction")
UML2_ControlNode = Class(name="UML2::ControlNode")
UML2_DirectedRelationship = Class(name="UML2::DirectedRelationship")
UML2_ConnectableElement = Class(name="UML2::ConnectableElement")
ParameterableElement = Class(name="ParameterableElement")
UML2_Actor = Class(name="UML2::Actor")
UML2_InitialNode = Class(name="UML2::InitialNode")
UML2_Extension = Class(name="UML2::Extension")
UML2_ObjectFlow = Class(name="UML2::ObjectFlow")
UML2_EventOccurrence = Class(name="UML2::EventOccurrence")
UML2_ConditionalNode = Class(name="UML2::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
UML2_ReadLinkObjectEndQualifierAction = Class(name="UML2::ReadLinkObjectEndQualifierAction")
UML2_Include = Class(name="UML2::Include")
UML2_ActivityGroup = Class(name="UML2::ActivityGroup")
UML2_Comment = Class(name="UML2::Comment")
TemplateableElement = Class(name="TemplateableElement")
UML2_AcceptEventAction = Class(name="UML2::AcceptEventAction")
UML2_ExceptionHandler = Class(name="UML2::ExceptionHandler")
UML2_ReplyAction = Class(name="UML2::ReplyAction")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
UML2_Signal = Class(name="UML2::Signal")
UML2_AnyTrigger = Class(name="UML2::AnyTrigger")
MessageTrigger = Class(name="MessageTrigger")
UML2_ParameterableClassifier = Class(name="UML2::ParameterableClassifier")
UML2_InformationFlow = Class(name="UML2::InformationFlow")
UML2_TimeExpression = Class(name="UML2::TimeExpression")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
Association = Class(name="Association")
UML2_RemoveVariableValueAction = Class(name="UML2::RemoveVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UML2_CallTrigger = Class(name="UML2::CallTrigger")
UML2_ForkNode = Class(name="UML2::ForkNode")
UML2_GeneralOrdering = Class(name="UML2::GeneralOrdering")
UML2_BehavioralFeature = Class(name="UML2::BehavioralFeature")
UML2_StartOwnedBehaviorAction = Class(name="UML2::StartOwnedBehaviorAction")
UML2_InteractionFragment = Class(name="UML2::InteractionFragment")
Type = Class(name="Type")
UML2_NamedElement = Class(name="UML2::NamedElement")
UML2_DeploymentTarget = Class(name="UML2::DeploymentTarget")
UML2_PackageMerge = Class(name="UML2::PackageMerge")
UML2_State = Class(name="UML2::State")
UML2_WriteLinkAction = Class(name="UML2::WriteLinkAction")
UML2_CallBehaviorAction = Class(name="UML2::CallBehaviorAction")
CallAction = Class(name="CallAction")
UML2_RaiseExceptionAction = Class(name="UML2::RaiseExceptionAction")
UML2_ExpansionRegion = Class(name="UML2::ExpansionRegion")
UML2_ChangeTrigger = Class(name="UML2::ChangeTrigger")
UML2_ProfileApplication = Class(name="UML2::ProfileApplication")
PackageImport = Class(name="PackageImport")
UML2_ProtocolConformance = Class(name="UML2::ProtocolConformance")
UML2_GeneralizationSet = Class(name="UML2::GeneralizationSet")
StructuralFeature = Class(name="StructuralFeature")
UML2_Activity = Class(name="UML2::Activity")
UML2_Device = Class(name="UML2::Device")
UML2_Region = Class(name="UML2::Region")
UML2_TemplateSignature = Class(name="UML2::TemplateSignature")
UML2_CollaborationOccurrence = Class(name="UML2::CollaborationOccurrence")
UML2_Substitution = Class(name="UML2::Substitution")
Realization = Class(name="Realization")
UML2_TimeObservationAction = Class(name="UML2::TimeObservationAction")
UML2_LoopNode = Class(name="UML2::LoopNode")
UML2_ClearVariableAction = Class(name="UML2::ClearVariableAction")
UML2_ExecutionOccurrence = Class(name="UML2::ExecutionOccurrence")
UML2_ApplyFunctionAction = Class(name="UML2::ApplyFunctionAction")
UML2_Operation = Class(name="UML2::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
UML2_Implementation = Class(name="UML2::Implementation")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
UML2_Expression = Class(name="UML2::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2_ConnectionPointReference = Class(name="UML2::ConnectionPointReference")
UML2_Clause = Class(name="UML2::Clause")
UML2_Reception = Class(name="UML2::Reception")
UML2_CreateLinkObjectAction = Class(name="UML2::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UML2_SignalTrigger = Class(name="UML2::SignalTrigger")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_FinalState = Class(name="UML2::FinalState")
State = Class(name="State")
UML2_Permission = Class(name="UML2::Permission")
Dependency = Class(name="Dependency")
UML2_InteractionOperand = Class(name="UML2::InteractionOperand")
UML2_Connector = Class(name="UML2::Connector")
UML2_ReadSelfAction = Class(name="UML2::ReadSelfAction")
UML2_Usage = Class(name="UML2::Usage")
UML2_EncapsulatedClassifier = Class(name="UML2::EncapsulatedClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
UML2_TemplateParameterSubstitution = Class(name="UML2::TemplateParameterSubstitution")
UML2_RedefinableElement = Class(name="UML2::RedefinableElement")
UML2_InterruptibleActivityRegion = Class(name="UML2::InterruptibleActivityRegion")
UML2_VariableAction = Class(name="UML2::VariableAction")
UML2_LiteralInteger = Class(name="UML2::LiteralInteger")
UML2_ReclassifyObjectAction = Class(name="UML2::ReclassifyObjectAction")
UML2_ConnectorEnd = Class(name="UML2::ConnectorEnd")
UML2_Namespace = Class(name="UML2::Namespace")
UML2_Collaboration = Class(name="UML2::Collaboration")
BehavioredClassifier = Class(name="BehavioredClassifier")
UML2_ActivityNode = Class(name="UML2::ActivityNode")
UML2_Stop = Class(name="UML2::Stop")
EventOccurrence = Class(name="EventOccurrence")
UML2_Transition = Class(name="UML2::Transition")
UML2_Profile = Class(name="UML2::Profile")
Package = Class(name="Package")
UML2_ActivityFinalNode = Class(name="UML2::ActivityFinalNode")
UML2_DecisionNode = Class(name="UML2::DecisionNode")
UML2_TemplateBinding = Class(name="UML2::TemplateBinding")
UML2_ExpansionNode = Class(name="UML2::ExpansionNode")
UML2_DurationObservationAction = Class(name="UML2::DurationObservationAction")
UML2_MessageEnd = Class(name="UML2::MessageEnd")
UML2_Interface = Class(name="UML2::Interface")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier")
UML2_BroadcastSignalAction = Class(name="UML2::BroadcastSignalAction")
UML2_CallOperationAction = Class(name="UML2::CallOperationAction")
UML2_Extend = Class(name="UML2::Extend")
UML2_CreateLinkAction = Class(name="UML2::CreateLinkAction")
UML2_Relationship = Class(name="UML2::Relationship")
UML2_LiteralSpecification = Class(name="UML2::LiteralSpecification")
UML2_LinkEndCreationData = Class(name="UML2::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UML2_Interaction = Class(name="UML2::Interaction")
UML2_ValuePin = Class(name="UML2::ValuePin")
InputPin = Class(name="InputPin")
UML2_LiteralNull = Class(name="UML2::LiteralNull")
UML2_OperationTemplateParameter = Class(name="UML2::OperationTemplateParameter")
UML2_AddVariableValueAction = Class(name="UML2::AddVariableValueAction")
UML2_StringExpression = Class(name="UML2::StringExpression")
UML2_Class = Class(name="UML2::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_Abstraction = Class(name="UML2::Abstraction")
UML2_Deployment = Class(name="UML2::Deployment")
UML2_PackageImport = Class(name="UML2::PackageImport")
UML2_AcceptCallAction = Class(name="UML2::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UML2_MergeNode = Class(name="UML2::MergeNode")
UML2_ConnectableElementTemplateParameter = Class(name="UML2::ConnectableElementTemplateParameter")
UML2_MultiplicityElement = Class(name="UML2::MultiplicityElement")
UML2_StructuredActivityNode = Class(name="UML2::StructuredActivityNode")
UML2_StateInvariant = Class(name="UML2::StateInvariant")
UML2_DestroyLinkAction = Class(name="UML2::DestroyLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UML2_Duration = Class(name="UML2::Duration")
UML2_SendObjectAction = Class(name="UML2::SendObjectAction")
UML2_Model = Class(name="UML2::Model")
UML2_Lifeline = Class(name="UML2::Lifeline")
UML2_IntervalConstraint = Class(name="UML2::IntervalConstraint")
UML2_Vertex = Class(name="UML2::Vertex")
UML2_ProtocolTransition = Class(name="UML2::ProtocolTransition")
Transition = Class(name="Transition")
UML2_ExecutableNode = Class(name="UML2::ExecutableNode")
UML2_ValueSpecification = Class(name="UML2::ValueSpecification")
UML2_LinkAction = Class(name="UML2::LinkAction")
UML2_Component = Class(name="UML2::Component")
UML2_ActivityEdge = Class(name="UML2::ActivityEdge")

# UML2_ParameterSet class attributes and methods

# NamedElement class attributes and methods

# UML2_TemplateableElement class attributes and methods

# Element class attributes and methods

# UML2_ElementImport class attributes and methods

# DirectedRelationship class attributes and methods

# UML2_PackageableElement class attributes and methods

# UML2_ExtensionPoint class attributes and methods

# RedefinableElement class attributes and methods

# UML2_CallAction class attributes and methods

# InvocationAction class attributes and methods

# UML2_TimeInterval class attributes and methods

# Interval class attributes and methods

# UML2_StructuredClassifier class attributes and methods

# Classifier class attributes and methods

# UML2_SendSignalAction class attributes and methods

# UML2_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2_Pseudostate class attributes and methods

# Vertex class attributes and methods

# UML2_DurationInterval class attributes and methods

# UML2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# UML2_LiteralString class attributes and methods

# LiteralSpecification class attributes and methods

# UML2_LinkEndData class attributes and methods

# UML2_InputPin class attributes and methods

# UML2_Property class attributes and methods
UML2_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
UML2_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UML2_Property.attributes={UML2_Property_isDerived, UML2_Property_isComposite, UML2_Property_aggregation, UML2_Property_isDerivedUnion}

# UML2_QualifierValue class attributes and methods

# UML2_PrimitiveFunction class attributes and methods

# PackageableElement class attributes and methods

# UML2_DeployedArtifact class attributes and methods

# UML2_RemoveStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# UML2_Interval class attributes and methods

# ValueSpecification class attributes and methods

# UML2_ClearAssociationAction class attributes and methods

# UML2_Dependency class attributes and methods

# UML2_RedefinableTemplateSignature class attributes and methods

# TemplateSignature class attributes and methods

# UML2_FlowFinalNode class attributes and methods

# FinalNode class attributes and methods

# UML2_ReadIsClassifiedObjectAction class attributes and methods

# Action class attributes and methods

# UML2_TimeTrigger class attributes and methods

# Trigger class attributes and methods

# UML2_Generalization class attributes and methods

# UML2_Classifier class attributes and methods
UML2_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2_Classifier.attributes={UML2_Classifier_isAbstract}

# UML2_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# UML2_Feature class attributes and methods
UML2_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
UML2_Feature.attributes={UML2_Feature_isStatic}

# UML2_Parameter class attributes and methods
UML2_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2_Parameter.attributes={UML2_Parameter_direction}

# ConnectableElement class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# UML2_MessageTrigger class attributes and methods

# UML2_CombinedFragment class attributes and methods

# InteractionFragment class attributes and methods

# UML2_DestroyObjectAction class attributes and methods

# UML2_CreateObjectAction class attributes and methods

# UML2_OutputPin class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# Node class attributes and methods

# UML2_Gate class attributes and methods

# MessageEnd class attributes and methods

# UML2_DurationConstraint class attributes and methods

# IntervalConstraint class attributes and methods

# UML2_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2_PrimitiveType class attributes and methods

# DataType class attributes and methods

# UML2_Action class attributes and methods

# ExecutableNode class attributes and methods

# UML2_Node class attributes and methods

# Class class attributes and methods

# DeploymentTarget class attributes and methods

# UML2_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UML2_WriteVariableAction class attributes and methods

# VariableAction class attributes and methods

# UML2_InstanceSpecification class attributes and methods

# DeployedArtifact class attributes and methods

# UML2_Slot class attributes and methods

# UML2_Element class attributes and methods

# UML2_TemplateableClassifier class attributes and methods

# UML2_FinalNode class attributes and methods

# ControlNode class attributes and methods

# UML2_LiteralUnlimitedNatural class attributes and methods

# UML2_StructuralFeatureAction class attributes and methods

# UML2_StructuralFeature class attributes and methods
UML2_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
UML2_StructuralFeature.attributes={UML2_StructuralFeature_isReadOnly}

# UML2_LiteralBoolean class attributes and methods

# UML2_TypedElement class attributes and methods

# UML2_Type class attributes and methods

# UML2_PartDecomposition class attributes and methods

# InteractionOccurrence class attributes and methods

# UML2_OpaqueExpression class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_ReadExtentAction class attributes and methods

# UML2_CentralBufferNode class attributes and methods

# UML2_Package class attributes and methods

# Namespace class attributes and methods

# UML2_Variable class attributes and methods

# UML2_Manifestation class attributes and methods

# Abstraction class attributes and methods

# UML2_Trigger class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_ClearStructuralFeatureAction class attributes and methods

# UML2_Continuation class attributes and methods

# UML2_InteractionOccurrence class attributes and methods

# UML2_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# UML2_ReadStructuralFeatureAction class attributes and methods

# UML2_InstanceValue class attributes and methods

# UML2_JoinNode class attributes and methods

# UML2_DataType class attributes and methods

# UML2_Enumeration class attributes and methods

# UML2_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UML2_AddStructuralFeatureValueAction class attributes and methods

# UML2_InformationItem class attributes and methods

# UML2_ActivityPartition class attributes and methods

# ActivityGroup class attributes and methods

# UML2_ObjectNode class attributes and methods

# ActivityNode class attributes and methods

# UML2_Port class attributes and methods

# Property class attributes and methods

# UML2_TemplateParameter class attributes and methods

# UML2_Realization class attributes and methods

# UML2_ReadVariableAction class attributes and methods

# UML2_Artifact class attributes and methods

# UML2_ClassifierTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# UML2_Pin class attributes and methods

# UML2_ParameterableElement class attributes and methods

# UML2_Constraint class attributes and methods

# UML2_Message class attributes and methods

# UML2_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Feature class attributes and methods

# UML2_Association class attributes and methods

# Relationship class attributes and methods

# Pin class attributes and methods

# UML2_TimeConstraint class attributes and methods

# UML2_InvocationAction class attributes and methods

# UML2_TestIdentityAction class attributes and methods

# UML2_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2_ReadLinkObjectEndAction class attributes and methods

# UML2_ControlNode class attributes and methods

# UML2_DirectedRelationship class attributes and methods

# UML2_ConnectableElement class attributes and methods

# ParameterableElement class attributes and methods

# UML2_Actor class attributes and methods

# UML2_InitialNode class attributes and methods

# UML2_Extension class attributes and methods

# UML2_ObjectFlow class attributes and methods

# UML2_EventOccurrence class attributes and methods

# UML2_ConditionalNode class attributes and methods

# StructuredActivityNode class attributes and methods

# UML2_ReadLinkObjectEndQualifierAction class attributes and methods

# UML2_Include class attributes and methods

# UML2_ActivityGroup class attributes and methods

# UML2_Comment class attributes and methods

# TemplateableElement class attributes and methods

# UML2_AcceptEventAction class attributes and methods

# UML2_ExceptionHandler class attributes and methods

# UML2_ReplyAction class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# UML2_Signal class attributes and methods

# UML2_AnyTrigger class attributes and methods

# MessageTrigger class attributes and methods

# UML2_ParameterableClassifier class attributes and methods

# UML2_InformationFlow class attributes and methods

# UML2_TimeExpression class attributes and methods

# UML2_AssociationClass class attributes and methods

# Association class attributes and methods

# UML2_RemoveVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# UML2_CallTrigger class attributes and methods

# UML2_ForkNode class attributes and methods

# UML2_GeneralOrdering class attributes and methods

# UML2_BehavioralFeature class attributes and methods

# UML2_StartOwnedBehaviorAction class attributes and methods

# UML2_InteractionFragment class attributes and methods

# Type class attributes and methods

# UML2_NamedElement class attributes and methods
UML2_NamedElement_name: Property = Property(name="name", type=StringType)
UML2_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
UML2_NamedElement.attributes={UML2_NamedElement_visibility, UML2_NamedElement_name}

# UML2_DeploymentTarget class attributes and methods

# UML2_PackageMerge class attributes and methods

# UML2_State class attributes and methods

# UML2_WriteLinkAction class attributes and methods

# UML2_CallBehaviorAction class attributes and methods

# CallAction class attributes and methods

# UML2_RaiseExceptionAction class attributes and methods

# UML2_ExpansionRegion class attributes and methods

# UML2_ChangeTrigger class attributes and methods

# UML2_ProfileApplication class attributes and methods

# PackageImport class attributes and methods

# UML2_ProtocolConformance class attributes and methods

# UML2_GeneralizationSet class attributes and methods

# StructuralFeature class attributes and methods

# UML2_Activity class attributes and methods

# UML2_Device class attributes and methods

# UML2_Region class attributes and methods

# UML2_TemplateSignature class attributes and methods

# UML2_CollaborationOccurrence class attributes and methods

# UML2_Substitution class attributes and methods

# Realization class attributes and methods

# UML2_TimeObservationAction class attributes and methods

# UML2_LoopNode class attributes and methods

# UML2_ClearVariableAction class attributes and methods

# UML2_ExecutionOccurrence class attributes and methods

# UML2_ApplyFunctionAction class attributes and methods

# UML2_Operation class attributes and methods
UML2_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
UML2_Operation.attributes={UML2_Operation_isQuery}

# BehavioralFeature class attributes and methods

# UML2_Implementation class attributes and methods

# UML2_CommunicationPath class attributes and methods

# UML2_Expression class attributes and methods

# OpaqueExpression class attributes and methods

# UML2_ConnectionPointReference class attributes and methods

# UML2_Clause class attributes and methods

# UML2_Reception class attributes and methods

# UML2_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UML2_SignalTrigger class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_FinalState class attributes and methods

# State class attributes and methods

# UML2_Permission class attributes and methods

# Dependency class attributes and methods

# UML2_InteractionOperand class attributes and methods

# UML2_Connector class attributes and methods

# UML2_ReadSelfAction class attributes and methods

# UML2_Usage class attributes and methods

# UML2_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# UML2_TemplateParameterSubstitution class attributes and methods

# UML2_RedefinableElement class attributes and methods

# UML2_InterruptibleActivityRegion class attributes and methods

# UML2_VariableAction class attributes and methods

# UML2_LiteralInteger class attributes and methods

# UML2_ReclassifyObjectAction class attributes and methods

# UML2_ConnectorEnd class attributes and methods

# UML2_Namespace class attributes and methods

# UML2_Collaboration class attributes and methods

# BehavioredClassifier class attributes and methods

# UML2_ActivityNode class attributes and methods

# UML2_Stop class attributes and methods

# EventOccurrence class attributes and methods

# UML2_Transition class attributes and methods

# UML2_Profile class attributes and methods

# Package class attributes and methods

# UML2_ActivityFinalNode class attributes and methods

# UML2_DecisionNode class attributes and methods

# UML2_TemplateBinding class attributes and methods

# UML2_ExpansionNode class attributes and methods

# UML2_DurationObservationAction class attributes and methods

# UML2_MessageEnd class attributes and methods

# UML2_Interface class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# UML2_BroadcastSignalAction class attributes and methods

# UML2_CallOperationAction class attributes and methods

# UML2_Extend class attributes and methods

# UML2_CreateLinkAction class attributes and methods

# UML2_Relationship class attributes and methods

# UML2_LiteralSpecification class attributes and methods

# UML2_LinkEndCreationData class attributes and methods

# LinkEndData class attributes and methods

# UML2_Interaction class attributes and methods

# UML2_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2_LiteralNull class attributes and methods

# UML2_OperationTemplateParameter class attributes and methods

# UML2_AddVariableValueAction class attributes and methods

# UML2_StringExpression class attributes and methods

# UML2_Class class attributes and methods
UML2_Class_isActive: Property = Property(name="isActive", type=BooleanType)
UML2_Class.attributes={UML2_Class_isActive}

# EncapsulatedClassifier class attributes and methods

# UML2_UseCase class attributes and methods

# UML2_Abstraction class attributes and methods

# UML2_Deployment class attributes and methods

# UML2_PackageImport class attributes and methods

# UML2_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UML2_MergeNode class attributes and methods

# UML2_ConnectableElementTemplateParameter class attributes and methods

# UML2_MultiplicityElement class attributes and methods
UML2_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
UML2_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
UML2_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
UML2_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
UML2_MultiplicityElement.attributes={UML2_MultiplicityElement_isUnique, UML2_MultiplicityElement_lower, UML2_MultiplicityElement_upper, UML2_MultiplicityElement_isOrdered}

# UML2_StructuredActivityNode class attributes and methods

# UML2_StateInvariant class attributes and methods

# UML2_DestroyLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UML2_Duration class attributes and methods

# UML2_SendObjectAction class attributes and methods

# UML2_Model class attributes and methods

# UML2_Lifeline class attributes and methods

# UML2_IntervalConstraint class attributes and methods

# UML2_Vertex class attributes and methods

# UML2_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# UML2_ExecutableNode class attributes and methods

# UML2_ValueSpecification class attributes and methods

# UML2_LinkAction class attributes and methods

# UML2_Component class attributes and methods

# UML2_ActivityEdge class attributes and methods

# Relationships
importedElement0: BinaryAssociation = BinaryAssociation(
    name="importedElement0",
    ends={
        Property(name="UML2_PackageableElement", type=UML2_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ElementImport", type=UML2_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="UML2_InputPin", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData", type=UML2_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end2: BinaryAssociation = BinaryAssociation(
    name="end2",
    ends={
        Property(name="UML2_Property", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData3", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier4: BinaryAssociation = BinaryAssociation(
    name="qualifier4",
    ends={
        Property(name="UML2_QualifierValue", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData5", type=UML2_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general6: BinaryAssociation = BinaryAssociation(
    name="general6",
    ends={
        Property(name="UML2_Classifier", type=UML2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Generalization", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
featuringClassifier7: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier7",
    ends={
        Property(name="UML2_Classifier8", type=UML2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Feature", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="UML2_InputPin10", type=UML2_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DestroyObjectAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier11: BinaryAssociation = BinaryAssociation(
    name="classifier11",
    ends={
        Property(name="UML2_Classifier12", type=UML2_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CreateObjectAction", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result13: BinaryAssociation = BinaryAssociation(
    name="result13",
    ends={
        Property(name="UML2_OutputPin", type=UML2_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CreateObjectAction14", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context_15: BinaryAssociation = BinaryAssociation(
    name="context_15",
    ends={
        Property(name="UML2_Classifier16", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action", type=UML2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="UML2_InputPin18", type=UML2_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_WriteStructuralFeatureAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
slot19: BinaryAssociation = BinaryAssociation(
    name="slot19",
    ends={
        Property(name="UML2_Slot", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InstanceSpecification", type=UML2_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier20: BinaryAssociation = BinaryAssociation(
    name="classifier20",
    ends={
        Property(name="UML2_Classifier22", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InstanceSpecification21", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
owner24: BinaryAssociation = BinaryAssociation(
    name="owner24",
    ends={
        Property(name="UML2_Element", type=UML2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Element23", type=UML2_Element, multiplicity=Multiplicity(0, 1))
    }
)
structuralFeature25: BinaryAssociation = BinaryAssociation(
    name="structuralFeature25",
    ends={
        Property(name="UML2_StructuralFeature", type=UML2_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuralFeatureAction", type=UML2_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="UML2_Type", type=UML2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TypedElement", type=UML2_Type, multiplicity=Multiplicity(0, 1))
    }
)
behavior27: BinaryAssociation = BinaryAssociation(
    name="behavior27",
    ends={
        Property(name="UML2_Behavior", type=UML2_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_OpaqueExpression", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd28: BinaryAssociation = BinaryAssociation(
    name="ownedEnd28",
    ends={
        Property(name="UML2_Property29", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Association", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd30: BinaryAssociation = BinaryAssociation(
    name="memberEnd30",
    ends={
        Property(name="UML2_Property32", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Association31", type=UML2_Property, multiplicity=Multiplicity(2, 9999))
    }
)
constrainedElement33: BinaryAssociation = BinaryAssociation(
    name="constrainedElement33",
    ends={
        Property(name="UML2_Element34", type=UML2_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Constraint", type=UML2_Element, multiplicity=Multiplicity(0, 9999))
    }
)
first41: BinaryAssociation = BinaryAssociation(
    name="first41",
    ends={
        Property(name="UML2_InputPin42", type=UML2_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TestIdentityAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second43: BinaryAssociation = BinaryAssociation(
    name="second43",
    ends={
        Property(name="UML2_InputPin45", type=UML2_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TestIdentityAction44", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definingFeature35: BinaryAssociation = BinaryAssociation(
    name="definingFeature35",
    ends={
        Property(name="UML2_StructuralFeature37", type=UML2_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Slot36", type=UML2_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
qualifier38: BinaryAssociation = BinaryAssociation(
    name="qualifier38",
    ends={
        Property(name="UML2_Property40", type=UML2_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_QualifierValue39", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
feature46: BinaryAssociation = BinaryAssociation(
    name="feature46",
    ends={
        Property(name="UML2_Feature48", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier47", type=UML2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember49: BinaryAssociation = BinaryAssociation(
    name="inheritedMember49",
    ends={
        Property(name="UML2_NamedElement", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier50", type=UML2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
generalization51: BinaryAssociation = BinaryAssociation(
    name="generalization51",
    ends={
        Property(name="UML2_Generalization53", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier52", type=UML2_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization54: BinaryAssociation = BinaryAssociation(
    name="generalization54",
    ends={
        Property(name="UML2_Generalization55", type=UML2_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_GeneralizationSet", type=UML2_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
association59: BinaryAssociation = BinaryAssociation(
    name="association59",
    ends={
        Property(name="UML2_Association61", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property60", type=UML2_Association, multiplicity=Multiplicity(0, 1))
    }
)
qualifier63: BinaryAssociation = BinaryAssociation(
    name="qualifier63",
    ends={
        Property(name="UML2_Property64", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property62", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter65: BinaryAssociation = BinaryAssociation(
    name="ownedParameter65",
    ends={
        Property(name="UML2_Parameter", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition66: BinaryAssociation = BinaryAssociation(
    name="bodyCondition66",
    ends={
        Property(name="UML2_Constraint68", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation67", type=UML2_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty57: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty57",
    ends={
        Property(name="UML2_Property58", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property56", type=UML2_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBehavior69: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior69",
    ends={
        Property(name="UML2_Behavior70", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior71: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior71",
    ends={
        Property(name="UML2_Behavior73", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier72", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
result74: BinaryAssociation = BinaryAssociation(
    name="result74",
    ends={
        Property(name="UML2_OutputPin75", type=UML2_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadSelfAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member76: BinaryAssociation = BinaryAssociation(
    name="member76",
    ends={
        Property(name="UML2_NamedElement77", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Namespace", type=UML2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier78: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier78",
    ends={
        Property(name="UML2_Classifier79", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception80: BinaryAssociation = BinaryAssociation(
    name="ownedReception80",
    ends={
        Property(name="UML2_Reception", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class81", type=UML2_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification82: BinaryAssociation = BinaryAssociation(
    name="specification82",
    ends={
        Property(name="UML2_BehavioralFeature", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior83", type=UML2_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameterSet84: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet84",
    ends={
        Property(name="UML2_ParameterSet", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior85", type=UML2_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=UML2_ParameterSet)
gen_UML2_TemplateableElement_Element = Generalization(general=Element, specific=UML2_TemplateableElement)
gen_UML2_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_ElementImport)
gen_UML2_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ExtensionPoint)
gen_UML2_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_CallAction)
gen_UML2_TimeInterval_Interval = Generalization(general=Interval, specific=UML2_TimeInterval)
gen_UML2_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_StructuredClassifier)
gen_UML2_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendSignalAction)
gen_UML2_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2_DataStoreNode)
gen_UML2_Pseudostate_Vertex = Generalization(general=Vertex, specific=UML2_Pseudostate)
gen_UML2_DurationInterval_Interval = Generalization(general=Interval, specific=UML2_DurationInterval)
gen_UML2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2_ControlFlow)
gen_UML2_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralString)
gen_UML2_LinkEndData_Element = Generalization(general=Element, specific=UML2_LinkEndData)
gen_UML2_PrimitiveFunction_PackageableElement = Generalization(general=PackageableElement, specific=UML2_PrimitiveFunction)
gen_UML2_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=UML2_DeployedArtifact)
gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_RemoveStructuralFeatureValueAction)
gen_UML2_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Interval)
gen_UML2_ClearAssociationAction_Action = Generalization(general=Action, specific=UML2_ClearAssociationAction)
gen_UML2_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Dependency)
gen_UML2_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Dependency)
gen_UML2_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_RedefinableTemplateSignature)
gen_UML2_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=UML2_RedefinableTemplateSignature)
gen_UML2_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2_FlowFinalNode)
gen_UML2_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UML2_ReadIsClassifiedObjectAction)
gen_UML2_TimeTrigger_Trigger = Generalization(general=Trigger, specific=UML2_TimeTrigger)
gen_UML2_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Generalization)
gen_UML2_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ActivityParameterNode)
gen_UML2_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Feature)
gen_UML2_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Parameter)
gen_UML2_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2_Parameter)
gen_UML2_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Parameter)
gen_UML2_MessageTrigger_Trigger = Generalization(general=Trigger, specific=UML2_MessageTrigger)
gen_UML2_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_CombinedFragment)
gen_UML2_DestroyObjectAction_Action = Generalization(general=Action, specific=UML2_DestroyObjectAction)
gen_UML2_CreateObjectAction_Action = Generalization(general=Action, specific=UML2_CreateObjectAction)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_Gate_MessageEnd = Generalization(general=MessageEnd, specific=UML2_Gate)
gen_UML2_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_DurationConstraint)
gen_UML2_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2_DeploymentSpecification)
gen_UML2_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2_PrimitiveType)
gen_UML2_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=UML2_Action)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_Node)
gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_WriteStructuralFeatureAction)
gen_UML2_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_WriteVariableAction)
gen_UML2_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UML2_InstanceSpecification)
gen_UML2_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_InstanceSpecification)
gen_UML2_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2_InstanceSpecification)
gen_UML2_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_TemplateableClassifier)
gen_UML2_FinalNode_ControlNode = Generalization(general=ControlNode, specific=UML2_FinalNode)
gen_UML2_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralUnlimitedNatural)
gen_UML2_StructuralFeatureAction_Action = Generalization(general=Action, specific=UML2_StructuralFeatureAction)
gen_UML2_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralBoolean)
gen_UML2_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UML2_TypedElement)
gen_UML2_PartDecomposition_InteractionOccurrence = Generalization(general=InteractionOccurrence, specific=UML2_PartDecomposition)
gen_UML2_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_OpaqueExpression)
gen_UML2_Type_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Type)
gen_UML2_ReadExtentAction_Action = Generalization(general=Action, specific=UML2_ReadExtentAction)
gen_UML2_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_CentralBufferNode)
gen_UML2_Package_Namespace = Generalization(general=Namespace, specific=UML2_Package)
gen_UML2_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Variable)
gen_UML2_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2_Variable)
gen_UML2_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Variable)
gen_UML2_Manifestation_Abstraction = Generalization(general=Abstraction, specific=UML2_Manifestation)
gen_UML2_Trigger_NamedElement = Generalization(general=NamedElement, specific=UML2_Trigger)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ClearStructuralFeatureAction)
gen_UML2_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_Continuation)
gen_UML2_InteractionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_InteractionOccurrence)
gen_UML2_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UML2_InteractionConstraint)
gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ReadStructuralFeatureAction)
gen_UML2_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_InstanceValue)
gen_UML2_JoinNode_ControlNode = Generalization(general=ControlNode, specific=UML2_JoinNode)
gen_UML2_DataType_Classifier = Generalization(general=Classifier, specific=UML2_DataType)
gen_UML2_Enumeration_DataType = Generalization(general=DataType, specific=UML2_Enumeration)
gen_UML2_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_ReadLinkAction)
gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_AddStructuralFeatureValueAction)
gen_UML2_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2_InformationItem)
gen_UML2_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=UML2_ActivityPartition)
gen_UML2_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_ActivityPartition)
gen_UML2_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ObjectNode)
gen_UML2_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2_ObjectNode)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_TemplateParameter_Element = Generalization(general=Element, specific=UML2_TemplateParameter)
gen_UML2_Realization_Abstraction = Generalization(general=Abstraction, specific=UML2_Realization)
gen_UML2_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ReadVariableAction)
gen_UML2_Artifact_Classifier = Generalization(general=Classifier, specific=UML2_Artifact)
gen_UML2_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2_Artifact)
gen_UML2_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_ClassifierTemplateParameter)
gen_UML2_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2_Pin)
gen_UML2_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Pin)
gen_UML2_ParameterableElement_Element = Generalization(general=Element, specific=UML2_ParameterableElement)
gen_UML2_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Constraint)
gen_UML2_Message_NamedElement = Generalization(general=NamedElement, specific=UML2_Message)
gen_UML2_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=UML2_EnumerationLiteral)
gen_UML2_Slot_Element = Generalization(general=Element, specific=UML2_Slot)
gen_UML2_Package_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Package)
gen_UML2_StructuralFeature_Feature = Generalization(general=Feature, specific=UML2_StructuralFeature)
gen_UML2_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2_StructuralFeature)
gen_UML2_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_StructuralFeature)
gen_UML2_Association_Classifier = Generalization(general=Classifier, specific=UML2_Association)
gen_UML2_Association_Relationship = Generalization(general=Relationship, specific=UML2_Association)
gen_UML2_OutputPin_Pin = Generalization(general=Pin, specific=UML2_OutputPin)
gen_UML2_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_TimeConstraint)
gen_UML2_InvocationAction_Action = Generalization(general=Action, specific=UML2_InvocationAction)
gen_UML2_TestIdentityAction_Action = Generalization(general=Action, specific=UML2_TestIdentityAction)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndAction)
gen_UML2_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ControlNode)
gen_UML2_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UML2_DirectedRelationship)
gen_UML2_ConnectableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_ConnectableElement)
gen_UML2_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_ConnectableElement)
gen_UML2_Actor_Classifier = Generalization(general=Classifier, specific=UML2_Actor)
gen_UML2_InitialNode_ControlNode = Generalization(general=ControlNode, specific=UML2_InitialNode)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2_ObjectFlow)
gen_UML2_EventOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_EventOccurrence)
gen_UML2_EventOccurrence_MessageEnd = Generalization(general=MessageEnd, specific=UML2_EventOccurrence)
gen_UML2_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ConditionalNode)
gen_UML2_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndQualifierAction)
gen_UML2_Include_NamedElement = Generalization(general=NamedElement, specific=UML2_Include)
gen_UML2_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Include)
gen_UML2_ActivityGroup_Element = Generalization(general=Element, specific=UML2_ActivityGroup)
gen_UML2_Comment_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_Comment)
gen_UML2_AcceptEventAction_Action = Generalization(general=Action, specific=UML2_AcceptEventAction)
gen_UML2_ExceptionHandler_Element = Generalization(general=Element, specific=UML2_ExceptionHandler)
gen_UML2_ReplyAction_Action = Generalization(general=Action, specific=UML2_ReplyAction)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Signal_Classifier = Generalization(general=Classifier, specific=UML2_Signal)
gen_UML2_AnyTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_AnyTrigger)
gen_UML2_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_ParameterableClassifier)
gen_UML2_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=UML2_InformationFlow)
gen_UML2_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_InformationFlow)
gen_UML2_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_TimeExpression)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_QualifierValue_Element = Generalization(general=Element, specific=UML2_QualifierValue)
gen_UML2_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_RemoveVariableValueAction)
gen_UML2_CallTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_CallTrigger)
gen_UML2_ForkNode_ControlNode = Generalization(general=ControlNode, specific=UML2_ForkNode)
gen_UML2_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=UML2_GeneralOrdering)
gen_UML2_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UML2_BehavioralFeature)
gen_UML2_BehavioralFeature_Feature = Generalization(general=Feature, specific=UML2_BehavioralFeature)
gen_UML2_StartOwnedBehaviorAction_Action = Generalization(general=Action, specific=UML2_StartOwnedBehaviorAction)
gen_UML2_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=UML2_InteractionFragment)
gen_UML2_Classifier_Namespace = Generalization(general=Namespace, specific=UML2_Classifier)
gen_UML2_Classifier_Type = Generalization(general=Type, specific=UML2_Classifier)
gen_UML2_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Classifier)
gen_UML2_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UML2_DeploymentTarget)
gen_UML2_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_PackageMerge)
gen_UML2_State_Namespace = Generalization(general=Namespace, specific=UML2_State)
gen_UML2_State_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_State)
gen_UML2_State_Vertex = Generalization(general=Vertex, specific=UML2_State)
gen_UML2_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_WriteLinkAction)
gen_UML2_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UML2_CallBehaviorAction)
gen_UML2_RaiseExceptionAction_Action = Generalization(general=Action, specific=UML2_RaiseExceptionAction)
gen_UML2_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ExpansionRegion)
gen_UML2_ChangeTrigger_Trigger = Generalization(general=Trigger, specific=UML2_ChangeTrigger)
gen_UML2_ProfileApplication_PackageImport = Generalization(general=PackageImport, specific=UML2_ProfileApplication)
gen_UML2_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_ProtocolConformance)
gen_UML2_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=UML2_GeneralizationSet)
gen_UML2_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2_Property)
gen_UML2_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Property)
gen_UML2_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_Property)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_Region_Namespace = Generalization(general=Namespace, specific=UML2_Region)
gen_UML2_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Region)
gen_UML2_TemplateSignature_Element = Generalization(general=Element, specific=UML2_TemplateSignature)
gen_UML2_CollaborationOccurrence_NamedElement = Generalization(general=NamedElement, specific=UML2_CollaborationOccurrence)
gen_UML2_Substitution_Realization = Generalization(general=Realization, specific=UML2_Substitution)
gen_UML2_TimeObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_TimeObservationAction)
gen_UML2_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_LoopNode)
gen_UML2_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ClearVariableAction)
gen_UML2_ExecutionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_ExecutionOccurrence)
gen_UML2_ApplyFunctionAction_Action = Generalization(general=Action, specific=UML2_ApplyFunctionAction)
gen_UML2_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Operation)
gen_UML2_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2_Operation)
gen_UML2_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Operation)
gen_UML2_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_Operation)
gen_UML2_Implementation_Realization = Generalization(general=Realization, specific=UML2_Implementation)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2_Expression)
gen_UML2_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=UML2_ConnectionPointReference)
gen_UML2_Clause_Element = Generalization(general=Element, specific=UML2_Clause)
gen_UML2_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Reception)
gen_UML2_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UML2_CreateLinkObjectAction)
gen_UML2_SignalTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_SignalTrigger)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_PackageableElement)
gen_UML2_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_PackageableElement)
gen_UML2_FinalState_State = Generalization(general=State, specific=UML2_FinalState)
gen_UML2_Permission_Dependency = Generalization(general=Dependency, specific=UML2_Permission)
gen_UML2_InteractionOperand_Namespace = Generalization(general=Namespace, specific=UML2_InteractionOperand)
gen_UML2_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_InteractionOperand)
gen_UML2_Connector_Feature = Generalization(general=Feature, specific=UML2_Connector)
gen_UML2_ReadSelfAction_Action = Generalization(general=Action, specific=UML2_ReadSelfAction)
gen_UML2_Usage_Dependency = Generalization(general=Dependency, specific=UML2_Usage)
gen_UML2_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_EncapsulatedClassifier)
gen_UML2_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=UML2_TemplateParameterSubstitution)
gen_UML2_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_RedefinableElement)
gen_UML2_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_InterruptibleActivityRegion)
gen_UML2_InputPin_Pin = Generalization(general=Pin, specific=UML2_InputPin)
gen_UML2_VariableAction_Action = Generalization(general=Action, specific=UML2_VariableAction)
gen_UML2_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralInteger)
gen_UML2_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UML2_ReclassifyObjectAction)
gen_UML2_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_ConnectorEnd)
gen_UML2_Namespace_NamedElement = Generalization(general=NamedElement, specific=UML2_Namespace)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_Collaboration)
gen_UML2_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ActivityNode)
gen_UML2_Stop_EventOccurrence = Generalization(general=EventOccurrence, specific=UML2_Stop)
gen_UML2_NamedElement_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_NamedElement)
gen_UML2_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Transition)
gen_UML2_Profile_Package = Generalization(general=Package, specific=UML2_Profile)
gen_UML2_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2_ActivityFinalNode)
gen_UML2_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=UML2_DecisionNode)
gen_UML2_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_TemplateBinding)
gen_UML2_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ExpansionNode)
gen_UML2_DurationObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_DurationObservationAction)
gen_UML2_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=UML2_MessageEnd)
gen_UML2_Interface_Classifier = Generalization(general=Classifier, specific=UML2_Interface)
gen_UML2_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_BehavioredClassifier)
gen_UML2_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_BroadcastSignalAction)
gen_UML2_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UML2_CallOperationAction)
gen_UML2_Extend_NamedElement = Generalization(general=NamedElement, specific=UML2_Extend)
gen_UML2_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Extend)
gen_UML2_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_CreateLinkAction)
gen_UML2_Relationship_Element = Generalization(general=Element, specific=UML2_Relationship)
gen_UML2_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_LiteralSpecification)
gen_UML2_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UML2_LinkEndCreationData)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_Interaction)
gen_UML2_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2_ValuePin)
gen_UML2_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralNull)
gen_UML2_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_OperationTemplateParameter)
gen_UML2_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_AddVariableValueAction)
gen_UML2_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_StringExpression)
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2_Class)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_Abstraction_Dependency = Generalization(general=Dependency, specific=UML2_Abstraction)
gen_UML2_Deployment_Dependency = Generalization(general=Dependency, specific=UML2_Deployment)
gen_UML2_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_PackageImport)
gen_UML2_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UML2_AcceptCallAction)
gen_UML2_MergeNode_ControlNode = Generalization(general=ControlNode, specific=UML2_MergeNode)
gen_UML2_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_ConnectableElementTemplateParameter)
gen_UML2_MultiplicityElement_Element = Generalization(general=Element, specific=UML2_MultiplicityElement)
gen_UML2_StructuredActivityNode_Action = Generalization(general=Action, specific=UML2_StructuredActivityNode)
gen_UML2_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_StateInvariant)
gen_UML2_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=UML2_StructuredActivityNode)
gen_UML2_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_StructuredActivityNode)
gen_UML2_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_DestroyLinkAction)
gen_UML2_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Duration)
gen_UML2_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendObjectAction)
gen_UML2_Model_Package = Generalization(general=Package, specific=UML2_Model)
gen_UML2_Lifeline_NamedElement = Generalization(general=NamedElement, specific=UML2_Lifeline)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UML2_IntervalConstraint)
gen_UML2_Vertex_NamedElement = Generalization(general=NamedElement, specific=UML2_Vertex)
gen_UML2_ProtocolTransition_Transition = Generalization(general=Transition, specific=UML2_ProtocolTransition)
gen_UML2_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ExecutableNode)
gen_UML2_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2_ValueSpecification)
gen_UML2_ValueSpecification_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_ValueSpecification)
gen_UML2_LinkAction_Action = Generalization(general=Action, specific=UML2_LinkAction)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)
gen_UML2_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ActivityEdge)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_ParameterSet, NamedElement, UML2_TemplateableElement, Element, UML2_ElementImport, DirectedRelationship, UML2_PackageableElement, UML2_ExtensionPoint, RedefinableElement, UML2_CallAction, InvocationAction, UML2_TimeInterval, Interval, UML2_StructuredClassifier, Classifier, UML2_SendSignalAction, UML2_DataStoreNode, CentralBufferNode, UML2_Pseudostate, Vertex, UML2_DurationInterval, UML2_ControlFlow, ActivityEdge, UML2_LiteralString, LiteralSpecification, UML2_LinkEndData, UML2_InputPin, UML2_Property, UML2_QualifierValue, UML2_PrimitiveFunction, PackageableElement, UML2_DeployedArtifact, UML2_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, UML2_Interval, ValueSpecification, UML2_ClearAssociationAction, UML2_Dependency, UML2_RedefinableTemplateSignature, TemplateSignature, UML2_FlowFinalNode, FinalNode, UML2_ReadIsClassifiedObjectAction, Action, UML2_TimeTrigger, Trigger, UML2_Generalization, UML2_Classifier, UML2_ActivityParameterNode, ObjectNode, UML2_Feature, UML2_Parameter, ConnectableElement, TypedElement, MultiplicityElement, UML2_MessageTrigger, UML2_CombinedFragment, InteractionFragment, UML2_DestroyObjectAction, UML2_CreateObjectAction, UML2_OutputPin, UML2_ExecutionEnvironment, Node, UML2_Gate, MessageEnd, UML2_DurationConstraint, IntervalConstraint, UML2_DeploymentSpecification, Artifact, UML2_PrimitiveType, DataType, UML2_Action, ExecutableNode, UML2_Node, Class_, DeploymentTarget, UML2_WriteStructuralFeatureAction, StructuralFeatureAction, UML2_WriteVariableAction, VariableAction, UML2_InstanceSpecification, DeployedArtifact, UML2_Slot, UML2_Element, UML2_TemplateableClassifier, UML2_FinalNode, ControlNode, UML2_LiteralUnlimitedNatural, UML2_StructuralFeatureAction, UML2_StructuralFeature, UML2_LiteralBoolean, UML2_TypedElement, UML2_Type, UML2_PartDecomposition, InteractionOccurrence, UML2_OpaqueExpression, UML2_Behavior, UML2_ReadExtentAction, UML2_CentralBufferNode, UML2_Package, Namespace, UML2_Variable, UML2_Manifestation, Abstraction, UML2_Trigger, UML2_ProtocolStateMachine, StateMachine, UML2_ClearStructuralFeatureAction, UML2_Continuation, UML2_InteractionOccurrence, UML2_InteractionConstraint, Constraint, UML2_ReadStructuralFeatureAction, UML2_InstanceValue, UML2_JoinNode, UML2_DataType, UML2_Enumeration, UML2_ReadLinkAction, LinkAction, UML2_AddStructuralFeatureValueAction, UML2_InformationItem, UML2_ActivityPartition, ActivityGroup, UML2_ObjectNode, ActivityNode, UML2_Port, Property_, UML2_TemplateParameter, UML2_Realization, UML2_ReadVariableAction, UML2_Artifact, UML2_ClassifierTemplateParameter, TemplateParameter, UML2_Pin, UML2_ParameterableElement, UML2_Constraint, UML2_Message, UML2_EnumerationLiteral, InstanceSpecification, Feature, UML2_Association, Relationship, Pin, UML2_TimeConstraint, UML2_InvocationAction, UML2_TestIdentityAction, UML2_StateMachine, Behavior, UML2_ReadLinkObjectEndAction, UML2_ControlNode, UML2_DirectedRelationship, UML2_ConnectableElement, ParameterableElement, UML2_Actor, UML2_InitialNode, UML2_Extension, UML2_ObjectFlow, UML2_EventOccurrence, UML2_ConditionalNode, StructuredActivityNode, UML2_ReadLinkObjectEndQualifierAction, UML2_Include, UML2_ActivityGroup, UML2_Comment, TemplateableElement, UML2_AcceptEventAction, UML2_ExceptionHandler, UML2_ReplyAction, UML2_ExtensionEnd, UML2_Signal, UML2_AnyTrigger, MessageTrigger, UML2_ParameterableClassifier, UML2_InformationFlow, UML2_TimeExpression, UML2_AssociationClass, Association, UML2_RemoveVariableValueAction, WriteVariableAction, UML2_CallTrigger, UML2_ForkNode, UML2_GeneralOrdering, UML2_BehavioralFeature, UML2_StartOwnedBehaviorAction, UML2_InteractionFragment, Type, UML2_NamedElement, UML2_DeploymentTarget, UML2_PackageMerge, UML2_State, UML2_WriteLinkAction, UML2_CallBehaviorAction, CallAction, UML2_RaiseExceptionAction, UML2_ExpansionRegion, UML2_ChangeTrigger, UML2_ProfileApplication, PackageImport, UML2_ProtocolConformance, UML2_GeneralizationSet, StructuralFeature, UML2_Activity, UML2_Device, UML2_Region, UML2_TemplateSignature, UML2_CollaborationOccurrence, UML2_Substitution, Realization, UML2_TimeObservationAction, UML2_LoopNode, UML2_ClearVariableAction, UML2_ExecutionOccurrence, UML2_ApplyFunctionAction, UML2_Operation, BehavioralFeature, UML2_Implementation, UML2_CommunicationPath, UML2_Expression, OpaqueExpression, UML2_ConnectionPointReference, UML2_Clause, UML2_Reception, UML2_CreateLinkObjectAction, CreateLinkAction, UML2_SignalTrigger, UML2_Stereotype, UML2_FinalState, State, UML2_Permission, Dependency, UML2_InteractionOperand, UML2_Connector, UML2_ReadSelfAction, UML2_Usage, UML2_EncapsulatedClassifier, StructuredClassifier, UML2_TemplateParameterSubstitution, UML2_RedefinableElement, UML2_InterruptibleActivityRegion, UML2_VariableAction, UML2_LiteralInteger, UML2_ReclassifyObjectAction, UML2_ConnectorEnd, UML2_Namespace, UML2_Collaboration, BehavioredClassifier, UML2_ActivityNode, UML2_Stop, EventOccurrence, UML2_Transition, UML2_Profile, Package, UML2_ActivityFinalNode, UML2_DecisionNode, UML2_TemplateBinding, UML2_ExpansionNode, UML2_DurationObservationAction, UML2_MessageEnd, UML2_Interface, UML2_BehavioredClassifier, UML2_BroadcastSignalAction, UML2_CallOperationAction, UML2_Extend, UML2_CreateLinkAction, UML2_Relationship, UML2_LiteralSpecification, UML2_LinkEndCreationData, LinkEndData, UML2_Interaction, UML2_ValuePin, InputPin, UML2_LiteralNull, UML2_OperationTemplateParameter, UML2_AddVariableValueAction, UML2_StringExpression, UML2_Class, EncapsulatedClassifier, UML2_UseCase, UML2_Abstraction, UML2_Deployment, UML2_PackageImport, UML2_AcceptCallAction, AcceptEventAction, UML2_MergeNode, UML2_ConnectableElementTemplateParameter, UML2_MultiplicityElement, UML2_StructuredActivityNode, UML2_StateInvariant, UML2_DestroyLinkAction, WriteLinkAction, UML2_Duration, UML2_SendObjectAction, UML2_Model, UML2_Lifeline, UML2_IntervalConstraint, UML2_Vertex, UML2_ProtocolTransition, Transition, UML2_ExecutableNode, UML2_ValueSpecification, UML2_LinkAction, UML2_Component, UML2_ActivityEdge, ParameterDirectionKind, AggregationKind, VisibilityKind},
    associations={importedElement0, value1, end2, qualifier4, general6, featuringClassifier7, target9, classifier11, result13, context_15, value17, slot19, classifier20, owner24, structuralFeature25, type26, behavior27, ownedEnd28, memberEnd30, constrainedElement33, first41, second43, definingFeature35, qualifier38, feature46, inheritedMember49, generalization51, generalization54, association59, qualifier63, ownedParameter65, bodyCondition66, subsettedProperty57, ownedBehavior69, classifierBehavior71, result74, member76, nestedClassifier78, ownedReception80, specification82, ownedParameterSet84},
    generalizations={gen_UML2_ParameterSet_NamedElement, gen_UML2_TemplateableElement_Element, gen_UML2_ElementImport_DirectedRelationship, gen_UML2_ExtensionPoint_RedefinableElement, gen_UML2_CallAction_InvocationAction, gen_UML2_TimeInterval_Interval, gen_UML2_StructuredClassifier_Classifier, gen_UML2_SendSignalAction_InvocationAction, gen_UML2_DataStoreNode_CentralBufferNode, gen_UML2_Pseudostate_Vertex, gen_UML2_DurationInterval_Interval, gen_UML2_ControlFlow_ActivityEdge, gen_UML2_LiteralString_LiteralSpecification, gen_UML2_LinkEndData_Element, gen_UML2_PrimitiveFunction_PackageableElement, gen_UML2_DeployedArtifact_NamedElement, gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_Interval_ValueSpecification, gen_UML2_ClearAssociationAction_Action, gen_UML2_Dependency_PackageableElement, gen_UML2_Dependency_DirectedRelationship, gen_UML2_RedefinableTemplateSignature_RedefinableElement, gen_UML2_RedefinableTemplateSignature_TemplateSignature, gen_UML2_FlowFinalNode_FinalNode, gen_UML2_ReadIsClassifiedObjectAction_Action, gen_UML2_TimeTrigger_Trigger, gen_UML2_Generalization_DirectedRelationship, gen_UML2_ActivityParameterNode_ObjectNode, gen_UML2_Feature_RedefinableElement, gen_UML2_Parameter_ConnectableElement, gen_UML2_Parameter_TypedElement, gen_UML2_Parameter_MultiplicityElement, gen_UML2_MessageTrigger_Trigger, gen_UML2_CombinedFragment_InteractionFragment, gen_UML2_DestroyObjectAction_Action, gen_UML2_CreateObjectAction_Action, gen_UML2_ExecutionEnvironment_Node, gen_UML2_Gate_MessageEnd, gen_UML2_DurationConstraint_IntervalConstraint, gen_UML2_DeploymentSpecification_Artifact, gen_UML2_PrimitiveType_DataType, gen_UML2_Action_ExecutableNode, gen_UML2_Node_Class, gen_UML2_Node_DeploymentTarget, gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction, gen_UML2_WriteVariableAction_VariableAction, gen_UML2_InstanceSpecification_PackageableElement, gen_UML2_InstanceSpecification_DeploymentTarget, gen_UML2_InstanceSpecification_DeployedArtifact, gen_UML2_TemplateableClassifier_Classifier, gen_UML2_FinalNode_ControlNode, gen_UML2_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2_StructuralFeatureAction_Action, gen_UML2_LiteralBoolean_LiteralSpecification, gen_UML2_TypedElement_NamedElement, gen_UML2_PartDecomposition_InteractionOccurrence, gen_UML2_OpaqueExpression_ValueSpecification, gen_UML2_Type_PackageableElement, gen_UML2_ReadExtentAction_Action, gen_UML2_CentralBufferNode_ObjectNode, gen_UML2_Package_Namespace, gen_UML2_Variable_ConnectableElement, gen_UML2_Variable_TypedElement, gen_UML2_Variable_MultiplicityElement, gen_UML2_Manifestation_Abstraction, gen_UML2_Trigger_NamedElement, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UML2_Continuation_InteractionFragment, gen_UML2_InteractionOccurrence_InteractionFragment, gen_UML2_InteractionConstraint_Constraint, gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UML2_InstanceValue_ValueSpecification, gen_UML2_JoinNode_ControlNode, gen_UML2_DataType_Classifier, gen_UML2_Enumeration_DataType, gen_UML2_ReadLinkAction_LinkAction, gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_InformationItem_Classifier, gen_UML2_ActivityPartition_NamedElement, gen_UML2_ActivityPartition_ActivityGroup, gen_UML2_ObjectNode_ActivityNode, gen_UML2_ObjectNode_TypedElement, gen_UML2_Port_Property, gen_UML2_TemplateParameter_Element, gen_UML2_Realization_Abstraction, gen_UML2_ReadVariableAction_VariableAction, gen_UML2_Artifact_Classifier, gen_UML2_Artifact_DeployedArtifact, gen_UML2_ClassifierTemplateParameter_TemplateParameter, gen_UML2_Pin_ObjectNode, gen_UML2_Pin_MultiplicityElement, gen_UML2_ParameterableElement_Element, gen_UML2_Constraint_PackageableElement, gen_UML2_Message_NamedElement, gen_UML2_EnumerationLiteral_InstanceSpecification, gen_UML2_Slot_Element, gen_UML2_Package_PackageableElement, gen_UML2_StructuralFeature_Feature, gen_UML2_StructuralFeature_TypedElement, gen_UML2_StructuralFeature_MultiplicityElement, gen_UML2_Association_Classifier, gen_UML2_Association_Relationship, gen_UML2_OutputPin_Pin, gen_UML2_TimeConstraint_IntervalConstraint, gen_UML2_InvocationAction_Action, gen_UML2_TestIdentityAction_Action, gen_UML2_StateMachine_Behavior, gen_UML2_ReadLinkObjectEndAction_Action, gen_UML2_ControlNode_ActivityNode, gen_UML2_DirectedRelationship_Relationship, gen_UML2_ConnectableElement_NamedElement, gen_UML2_ConnectableElement_ParameterableElement, gen_UML2_Actor_Classifier, gen_UML2_InitialNode_ControlNode, gen_UML2_Extension_Association, gen_UML2_ObjectFlow_ActivityEdge, gen_UML2_EventOccurrence_InteractionFragment, gen_UML2_EventOccurrence_MessageEnd, gen_UML2_ConditionalNode_StructuredActivityNode, gen_UML2_ReadLinkObjectEndQualifierAction_Action, gen_UML2_Include_NamedElement, gen_UML2_Include_DirectedRelationship, gen_UML2_ActivityGroup_Element, gen_UML2_Comment_TemplateableElement, gen_UML2_AcceptEventAction_Action, gen_UML2_ExceptionHandler_Element, gen_UML2_ReplyAction_Action, gen_UML2_ExtensionEnd_Property, gen_UML2_Signal_Classifier, gen_UML2_AnyTrigger_MessageTrigger, gen_UML2_ParameterableClassifier_Classifier, gen_UML2_InformationFlow_PackageableElement, gen_UML2_InformationFlow_DirectedRelationship, gen_UML2_TimeExpression_ValueSpecification, gen_UML2_AssociationClass_Class, gen_UML2_AssociationClass_Association, gen_UML2_QualifierValue_Element, gen_UML2_RemoveVariableValueAction_WriteVariableAction, gen_UML2_CallTrigger_MessageTrigger, gen_UML2_ForkNode_ControlNode, gen_UML2_GeneralOrdering_NamedElement, gen_UML2_BehavioralFeature_Namespace, gen_UML2_BehavioralFeature_Feature, gen_UML2_StartOwnedBehaviorAction_Action, gen_UML2_InteractionFragment_NamedElement, gen_UML2_Classifier_Namespace, gen_UML2_Classifier_Type, gen_UML2_Classifier_RedefinableElement, gen_UML2_DeploymentTarget_NamedElement, gen_UML2_PackageMerge_DirectedRelationship, gen_UML2_State_Namespace, gen_UML2_State_RedefinableElement, gen_UML2_State_Vertex, gen_UML2_WriteLinkAction_LinkAction, gen_UML2_CallBehaviorAction_CallAction, gen_UML2_RaiseExceptionAction_Action, gen_UML2_ExpansionRegion_StructuredActivityNode, gen_UML2_ChangeTrigger_Trigger, gen_UML2_ProfileApplication_PackageImport, gen_UML2_ProtocolConformance_DirectedRelationship, gen_UML2_GeneralizationSet_PackageableElement, gen_UML2_Property_StructuralFeature, gen_UML2_Property_ConnectableElement, gen_UML2_Property_DeploymentTarget, gen_UML2_Activity_Behavior, gen_UML2_Device_Node, gen_UML2_Region_Namespace, gen_UML2_Region_RedefinableElement, gen_UML2_TemplateSignature_Element, gen_UML2_CollaborationOccurrence_NamedElement, gen_UML2_Substitution_Realization, gen_UML2_TimeObservationAction_WriteStructuralFeatureAction, gen_UML2_LoopNode_StructuredActivityNode, gen_UML2_ClearVariableAction_VariableAction, gen_UML2_ExecutionOccurrence_InteractionFragment, gen_UML2_ApplyFunctionAction_Action, gen_UML2_Operation_BehavioralFeature, gen_UML2_Operation_TypedElement, gen_UML2_Operation_MultiplicityElement, gen_UML2_Operation_ParameterableElement, gen_UML2_Implementation_Realization, gen_UML2_CommunicationPath_Association, gen_UML2_Expression_OpaqueExpression, gen_UML2_ConnectionPointReference_Vertex, gen_UML2_Clause_Element, gen_UML2_Reception_BehavioralFeature, gen_UML2_CreateLinkObjectAction_CreateLinkAction, gen_UML2_SignalTrigger_MessageTrigger, gen_UML2_Stereotype_Class, gen_UML2_PackageableElement_NamedElement, gen_UML2_PackageableElement_ParameterableElement, gen_UML2_FinalState_State, gen_UML2_Permission_Dependency, gen_UML2_InteractionOperand_Namespace, gen_UML2_InteractionOperand_InteractionFragment, gen_UML2_Connector_Feature, gen_UML2_ReadSelfAction_Action, gen_UML2_Usage_Dependency, gen_UML2_EncapsulatedClassifier_StructuredClassifier, gen_UML2_TemplateParameterSubstitution_Element, gen_UML2_RedefinableElement_NamedElement, gen_UML2_InterruptibleActivityRegion_ActivityGroup, gen_UML2_InputPin_Pin, gen_UML2_VariableAction_Action, gen_UML2_LiteralInteger_LiteralSpecification, gen_UML2_ReclassifyObjectAction_Action, gen_UML2_ConnectorEnd_MultiplicityElement, gen_UML2_Namespace_NamedElement, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_Collaboration_StructuredClassifier, gen_UML2_ActivityNode_RedefinableElement, gen_UML2_Stop_EventOccurrence, gen_UML2_NamedElement_TemplateableElement, gen_UML2_Transition_RedefinableElement, gen_UML2_Profile_Package, gen_UML2_ActivityFinalNode_FinalNode, gen_UML2_DecisionNode_ControlNode, gen_UML2_TemplateBinding_DirectedRelationship, gen_UML2_ExpansionNode_ObjectNode, gen_UML2_DurationObservationAction_WriteStructuralFeatureAction, gen_UML2_MessageEnd_NamedElement, gen_UML2_Interface_Classifier, gen_UML2_BehavioredClassifier_Classifier, gen_UML2_BroadcastSignalAction_InvocationAction, gen_UML2_CallOperationAction_CallAction, gen_UML2_Extend_NamedElement, gen_UML2_Extend_DirectedRelationship, gen_UML2_CreateLinkAction_WriteLinkAction, gen_UML2_Relationship_Element, gen_UML2_LiteralSpecification_ValueSpecification, gen_UML2_LinkEndCreationData_LinkEndData, gen_UML2_Interaction_Behavior, gen_UML2_Interaction_InteractionFragment, gen_UML2_ValuePin_InputPin, gen_UML2_LiteralNull_LiteralSpecification, gen_UML2_OperationTemplateParameter_TemplateParameter, gen_UML2_AddVariableValueAction_WriteVariableAction, gen_UML2_StringExpression_TemplateableElement, gen_UML2_Class_BehavioredClassifier, gen_UML2_Class_EncapsulatedClassifier, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_Abstraction_Dependency, gen_UML2_Deployment_Dependency, gen_UML2_PackageImport_DirectedRelationship, gen_UML2_AcceptCallAction_AcceptEventAction, gen_UML2_MergeNode_ControlNode, gen_UML2_ConnectableElementTemplateParameter_TemplateParameter, gen_UML2_MultiplicityElement_Element, gen_UML2_StructuredActivityNode_Action, gen_UML2_StateInvariant_InteractionFragment, gen_UML2_StructuredActivityNode_Namespace, gen_UML2_StructuredActivityNode_ActivityGroup, gen_UML2_DestroyLinkAction_WriteLinkAction, gen_UML2_Duration_ValueSpecification, gen_UML2_SendObjectAction_InvocationAction, gen_UML2_Model_Package, gen_UML2_Lifeline_NamedElement, gen_UML2_Behavior_Class, gen_UML2_IntervalConstraint_Constraint, gen_UML2_Vertex_NamedElement, gen_UML2_ProtocolTransition_Transition, gen_UML2_ExecutableNode_ActivityNode, gen_UML2_ValueSpecification_TypedElement, gen_UML2_ValueSpecification_ParameterableElement, gen_UML2_LinkAction_Action, gen_UML2_Component_Class, gen_UML2_ActivityEdge_RedefinableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)