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
            EnumerationLiteral(name="package"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
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

CallConcurrencyFeature: Enumeration = Enumeration(
    name="CallConcurrencyFeature",
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

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="external"),
			EnumerationLiteral(name="internal")
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

ParameterEffectKind: Enumeration = Enumeration(
    name="ParameterEffectKind",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
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

InteractionOperandKind: Enumeration = Enumeration(
    name="InteractionOperandKind",
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

# Classes
CompleteDSLPckg_Element = Class(name="CompleteDSLPckg::Element", is_abstract=True)
CompleteDSLPckg_Comment = Class(name="CompleteDSLPckg::Comment")
CompleteDSLPckg_NamedElement = Class(name="CompleteDSLPckg::NamedElement", is_abstract=True)
Element = Class(name="Element")
CompleteDSLPckg_Namespace = Class(name="CompleteDSLPckg::Namespace")
CompleteDSLPckg_Constraint = Class(name="CompleteDSLPckg::Constraint")
DirectedRelationship = Class(name="DirectedRelationship")
CompleteDSLPckg_Package = Class(name="CompleteDSLPckg::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
CompleteDSLPckg_Dependency = Class(name="CompleteDSLPckg::Dependency")
NamedElement = Class(name="NamedElement")
CompleteDSLPckg_PackageableElement = Class(name="CompleteDSLPckg::PackageableElement")
CompleteDSLPckg_ElementImport = Class(name="CompleteDSLPckg::ElementImport")
CompleteDSLPckg_PackageImport = Class(name="CompleteDSLPckg::PackageImport")
CompleteDSLPckg_DirectedRelationship = Class(name="CompleteDSLPckg::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
CompleteDSLPckg_MultiplicityElement = Class(name="CompleteDSLPckg::MultiplicityElement", is_abstract=True)
CompleteDSLPckg_ValueSpecification = Class(name="CompleteDSLPckg::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
CompleteDSLPckg_Type = Class(name="CompleteDSLPckg::Type", is_abstract=True)
CompleteDSLPckg_PackageMerge = Class(name="CompleteDSLPckg::PackageMerge")
CompleteDSLPckg_Relationship = Class(name="CompleteDSLPckg::Relationship", is_abstract=True)
CompleteDSLPckg_InstanceSpecification = Class(name="CompleteDSLPckg::InstanceSpecification")
CompleteDSLPckg_TypedElement = Class(name="CompleteDSLPckg::TypedElement", is_abstract=True)
CompleteDSLPckg_Expression = Class(name="CompleteDSLPckg::Expression")
ValueSpecification = Class(name="ValueSpecification")
CompleteDSLPckg_Slot = Class(name="CompleteDSLPckg::Slot")
CompleteDSLPckg_LiteralInteger = Class(name="CompleteDSLPckg::LiteralInteger")
CompleteDSLPckg_LiteralReal = Class(name="CompleteDSLPckg::LiteralReal")
CompleteDSLPckg_LiteralString = Class(name="CompleteDSLPckg::LiteralString")
CompleteDSLPckg_LiteralUnilimitedNatural = Class(name="CompleteDSLPckg::LiteralUnilimitedNatural")
CompleteDSLPckg_InstanceValue = Class(name="CompleteDSLPckg::InstanceValue")
CompleteDSLPckg_Classifier = Class(name="CompleteDSLPckg::Classifier", is_abstract=True)
CompleteDSLPckg_OpaqueExpression = Class(name="CompleteDSLPckg::OpaqueExpression")
CompleteDSLPckg_Parameter = Class(name="CompleteDSLPckg::Parameter")
CompleteDSLPckg_Behavior = Class(name="CompleteDSLPckg::Behavior", is_abstract=True)
CompleteDSLPckg_LiteralSpecification = Class(name="CompleteDSLPckg::LiteralSpecification", is_abstract=True)
CompleteDSLPckg_LiteralNull = Class(name="CompleteDSLPckg::LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
CompleteDSLPckg_LiteralBoolean = Class(name="CompleteDSLPckg::LiteralBoolean")
CompleteDSLPckg_Feature = Class(name="CompleteDSLPckg::Feature", is_abstract=True)
CompleteDSLPckg_Property = Class(name="CompleteDSLPckg::Property")
CompleteDSLPckg_Generalization = Class(name="CompleteDSLPckg::Generalization")
CompleteDSLPckg_Substitution = Class(name="CompleteDSLPckg::Substitution")
CompleteDSLPckg_GeneralizationSet = Class(name="CompleteDSLPckg::GeneralizationSet")
CompleteDSLPckg_StructuralFeature = Class(name="CompleteDSLPckg::StructuralFeature", is_abstract=True)
CompleteDSLPckg_RedefinableElement = Class(name="CompleteDSLPckg::RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
CompleteDSLPckg_Class = Class(name="CompleteDSLPckg::Class")
CompleteDSLPckg_Association = Class(name="CompleteDSLPckg::Association")
CompleteDSLPckg_DataType = Class(name="CompleteDSLPckg::DataType")
CompleteDSLPckg_Interface = Class(name="CompleteDSLPckg::Interface")
CompleteDSLPckg_CollaborationUse = Class(name="CompleteDSLPckg::CollaborationUse")
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
CompleteDSLPckg_Operation = Class(name="CompleteDSLPckg::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
CompleteDSLPckg_BehavioralFeature = Class(name="CompleteDSLPckg::BehavioralFeature", is_abstract=True)
CompleteDSLPckg_PrimitiveType = Class(name="CompleteDSLPckg::PrimitiveType")
DataType = Class(name="DataType")
CompleteDSLPckg_Enumeration = Class(name="CompleteDSLPckg::Enumeration")
CompleteDSLPckg_EnumerationLiteral = Class(name="CompleteDSLPckg::EnumerationLiteral")
Classifier = Class(name="Classifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
CompleteDSLPckg_Reception = Class(name="CompleteDSLPckg::Reception")
CompleteDSLPckg_Realization = Class(name="CompleteDSLPckg::Realization")
Abstraction = Class(name="Abstraction")
Realization = Class(name="Realization")
CompleteDSLPckg_InterfaceRealization = Class(name="CompleteDSLPckg::InterfaceRealization")
InstanceSpecification = Class(name="InstanceSpecification")
CompleteDSLPckg_Usage = Class(name="CompleteDSLPckg::Usage")
Dependency = Class(name="Dependency")
CompleteDSLPckg_Abstraction = Class(name="CompleteDSLPckg::Abstraction")
CompleteDSLPckg_OpaqueBehavior = Class(name="CompleteDSLPckg::OpaqueBehavior")
Behavior = Class(name="Behavior")
CompleteDSLPckg_BehavioredClassifier = Class(name="CompleteDSLPckg::BehavioredClassifier", is_abstract=True)
CompleteDSLPckg_AssociationClass = Class(name="CompleteDSLPckg::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
CompleteDSLPckg_Trigger = Class(name="CompleteDSLPckg::Trigger")
CompleteDSLPckg_Event = Class(name="CompleteDSLPckg::Event", is_abstract=True)
CompleteDSLPckg_FunctionBehavior = Class(name="CompleteDSLPckg::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
CompleteDSLPckg_Signal = Class(name="CompleteDSLPckg::Signal")
CompleteDSLPckg_TimeEvent = Class(name="CompleteDSLPckg::TimeEvent")
CompleteDSLPckg_TimeExpression = Class(name="CompleteDSLPckg::TimeExpression")
CompleteDSLPckg_Observation = Class(name="CompleteDSLPckg::Observation", is_abstract=True)
CompleteDSLPckg_TimeObservation = Class(name="CompleteDSLPckg::TimeObservation")
Observation = Class(name="Observation")
CompleteDSLPckg_MessageEvent = Class(name="CompleteDSLPckg::MessageEvent", is_abstract=True)
Event = Class(name="Event")
CompleteDSLPckg_AnyReceiveEvent = Class(name="CompleteDSLPckg::AnyReceiveEvent")
MessageEvent = Class(name="MessageEvent")
CompleteDSLPckg_SignalEvent = Class(name="CompleteDSLPckg::SignalEvent")
CompleteDSLPckg_CallEvent = Class(name="CompleteDSLPckg::CallEvent")
CompleteDSLPckg_ChangeEvent = Class(name="CompleteDSLPckg::ChangeEvent")
CompleteDSLPckg_TimeInterval = Class(name="CompleteDSLPckg::TimeInterval")
Interval = Class(name="Interval")
CompleteDSLPckg_DurationInterval = Class(name="CompleteDSLPckg::DurationInterval")
CompleteDSLPckg_IntervalConstraint = Class(name="CompleteDSLPckg::IntervalConstraint")
Constraint = Class(name="Constraint")
CompleteDSLPckg_TimeConstraint = Class(name="CompleteDSLPckg::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
CompleteDSLPckg_DurationConstraint = Class(name="CompleteDSLPckg::DurationConstraint")
CompleteDSLPckg_Component = Class(name="CompleteDSLPckg::Component")
CompleteDSLPckg_DurationObservation = Class(name="CompleteDSLPckg::DurationObservation")
CompleteDSLPckg_Duration = Class(name="CompleteDSLPckg::Duration")
CompleteDSLPckg_Interval = Class(name="CompleteDSLPckg::Interval")
CompleteDSLPckg_ConnectorEnd = Class(name="CompleteDSLPckg::ConnectorEnd")
CompleteDSLPckg_ConnectableElement = Class(name="CompleteDSLPckg::ConnectableElement", is_abstract=True)
CompleteDSLPckg_StructuredClassifier = Class(name="CompleteDSLPckg::StructuredClassifier")
CompleteDSLPckg_ComponentRealization = Class(name="CompleteDSLPckg::ComponentRealization")
CompleteDSLPckg_Connector = Class(name="CompleteDSLPckg::Connector")
CompleteDSLPckg_EncapsulatedClassifier = Class(name="CompleteDSLPckg::EncapsulatedClassifier", is_abstract=True)
CompleteDSLPckg_Collaboration = Class(name="CompleteDSLPckg::Collaboration")
CompleteDSLPckg_InvocationAction = Class(name="CompleteDSLPckg::InvocationAction", is_abstract=True)
CompleteDSLPckg_Variable = Class(name="CompleteDSLPckg::Variable")
CompleteDSLPckg_Port = Class(name="CompleteDSLPckg::Port")
Property_ = Class(name="Property")
CompleteDSLPckg_Device = Class(name="CompleteDSLPckg::Device")
Node = Class(name="Node")
CompleteDSLPckg_ExecutionEnvironment = Class(name="CompleteDSLPckg::ExecutionEnvironment")
CompleteDSLPckg_CommunicationPath = Class(name="CompleteDSLPckg::CommunicationPath")
CompleteDSLPckg_DeploymentTarget = Class(name="CompleteDSLPckg::DeploymentTarget", is_abstract=True)
CompleteDSLPckg_Deployment = Class(name="CompleteDSLPckg::Deployment")
CompleteDSLPckg_DeployedArtifact = Class(name="CompleteDSLPckg::DeployedArtifact", is_abstract=True)
CompleteDSLPckg_DeploymentSpecification = Class(name="CompleteDSLPckg::DeploymentSpecification")
Artifact = Class(name="Artifact")
CompleteDSLPckg_Artifact = Class(name="CompleteDSLPckg::Artifact")
DeployedArtifact = Class(name="DeployedArtifact")
CompleteDSLPckg_Manifestation = Class(name="CompleteDSLPckg::Manifestation")
CompleteDSLPckg_Node = Class(name="CompleteDSLPckg::Node")
Pin = Class(name="Pin")
CompleteDSLPckg_Pin = Class(name="CompleteDSLPckg::Pin", is_abstract=True)
CompleteDSLPckg_ValuePin = Class(name="CompleteDSLPckg::ValuePin")
InputPin = Class(name="InputPin")
CompleteDSLPckg_CallAction = Class(name="CompleteDSLPckg::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
CompleteDSLPckg_CallBehaviorAction = Class(name="CompleteDSLPckg::CallBehaviorAction")
CallAction = Class(name="CallAction")
CompleteDSLPckg_CallOperationAction = Class(name="CompleteDSLPckg::CallOperationAction")
CompleteDSLPckg_SendSignalAction = Class(name="CompleteDSLPckg::SendSignalAction")
CompleteDSLPckg_Action = Class(name="CompleteDSLPckg::Action", is_abstract=True)
CompleteDSLPckg_InputPin = Class(name="CompleteDSLPckg::InputPin")
CompleteDSLPckg_OutputPin = Class(name="CompleteDSLPckg::OutputPin")
CompleteDSLPckg_OpaqueAction = Class(name="CompleteDSLPckg::OpaqueAction")
Action = Class(name="Action")
CompleteDSLPckg_DestroyObjectAction = Class(name="CompleteDSLPckg::DestroyObjectAction")
CompleteDSLPckg_TestIdentityAction = Class(name="CompleteDSLPckg::TestIdentityAction")
CompleteDSLPckg_ReadSelfAction = Class(name="CompleteDSLPckg::ReadSelfAction")
CompleteDSLPckg_ValueSpecificationAction = Class(name="CompleteDSLPckg::ValueSpecificationAction")
CompleteDSLPckg_StructuralFeatureAction = Class(name="CompleteDSLPckg::StructuralFeatureAction", is_abstract=True)
CompleteDSLPckg_BroadcastSignalAction = Class(name="CompleteDSLPckg::BroadcastSignalAction")
CompleteDSLPckg_SendObjectAction = Class(name="CompleteDSLPckg::SendObjectAction")
CompleteDSLPckg_CreateObjectAction = Class(name="CompleteDSLPckg::CreateObjectAction")
CompleteDSLPckg_ClearStructuralFeatureAction = Class(name="CompleteDSLPckg::ClearStructuralFeatureAction")
CompleteDSLPckg_LinkAction = Class(name="CompleteDSLPckg::LinkAction")
CompleteDSLPckg_LinkEndData = Class(name="CompleteDSLPckg::LinkEndData", is_abstract=True)
CompleteDSLPckg_QualifierValue = Class(name="CompleteDSLPckg::QualifierValue")
CompleteDSLPckg_ReadLinkAction = Class(name="CompleteDSLPckg::ReadLinkAction")
LinkAction = Class(name="LinkAction")
CompleteDSLPckg_ReadStructuralFeatureAction = Class(name="CompleteDSLPckg::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
CompleteDSLPckg_WriteStructuralFeatureAction = Class(name="CompleteDSLPckg::WriteStructuralFeatureAction", is_abstract=True)
CompleteDSLPckg_AddStructuralFeatureValueAction = Class(name="CompleteDSLPckg::AddStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
CompleteDSLPckg_RemoveStructuralFeatureValueAction = Class(name="CompleteDSLPckg::RemoveStructuralFeatureValueAction")
CompleteDSLPckg_UnmarshallAction = Class(name="CompleteDSLPckg::UnmarshallAction")
CompleteDSLPckg_WriteLinkAction = Class(name="CompleteDSLPckg::WriteLinkAction", is_abstract=True)
CompleteDSLPckg_CreateLinkAction = Class(name="CompleteDSLPckg::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
CompleteDSLPckg_LinkEndCreationData = Class(name="CompleteDSLPckg::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
CompleteDSLPckg_DestroyLinkAction = Class(name="CompleteDSLPckg::DestroyLinkAction")
CompleteDSLPckg_LinkEndDestructionData = Class(name="CompleteDSLPckg::LinkEndDestructionData")
CompleteDSLPckg_ReplyAction = Class(name="CompleteDSLPckg::ReplyAction")
CompleteDSLPckg_ReclassifyObjectAction = Class(name="CompleteDSLPckg::ReclassifyObjectAction")
CompleteDSLPckg_ReadlsClassifiedObjectAction = Class(name="CompleteDSLPckg::ReadlsClassifiedObjectAction")
CompleteDSLPckg_StartClassifierBehaviorAction = Class(name="CompleteDSLPckg::StartClassifierBehaviorAction")
CompleteDSLPckg_StartObjectBehaviorAction = Class(name="CompleteDSLPckg::StartObjectBehaviorAction")
CompleteDSLPckg_AcceptEventAction = Class(name="CompleteDSLPckg::AcceptEventAction")
CompleteDSLPckg_AcceptCallAction = Class(name="CompleteDSLPckg::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
CompleteDSLPckg_ReadExtendAction = Class(name="CompleteDSLPckg::ReadExtendAction")
CompleteDSLPckg_ReadLinkObjectEndQualifierAction = Class(name="CompleteDSLPckg::ReadLinkObjectEndQualifierAction")
CompleteDSLPckg_CreateLinkObjectAction = Class(name="CompleteDSLPckg::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
CompleteDSLPckg_ReduceAction = Class(name="CompleteDSLPckg::ReduceAction")
CompleteDSLPckg_ReadLinkObjectEndAction = Class(name="CompleteDSLPckg::ReadLinkObjectEndAction")
CompleteDSLPckg_AddVariableValueAction = Class(name="CompleteDSLPckg::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
CompleteDSLPckg_RemoveVariableValueAction = Class(name="CompleteDSLPckg::RemoveVariableValueAction")
CompleteDSLPckg_ClearVariableAction = Class(name="CompleteDSLPckg::ClearVariableAction")
CompleteDSLPckg_RaiseExceptionAction = Class(name="CompleteDSLPckg::RaiseExceptionAction")
CompleteDSLPckg_ActionInputPin = Class(name="CompleteDSLPckg::ActionInputPin")
CompleteDSLPckg_StateMachine = Class(name="CompleteDSLPckg::StateMachine")
CompleteDSLPckg_Region = Class(name="CompleteDSLPckg::Region")
CompleteDSLPckg_Pseudostate = Class(name="CompleteDSLPckg::Pseudostate")
CompleteDSLPckg_State = Class(name="CompleteDSLPckg::State")
CompleteDSLPckg_VariableAction = Class(name="CompleteDSLPckg::VariableAction", is_abstract=True)
CompleteDSLPckg_ReadVariableAction = Class(name="CompleteDSLPckg::ReadVariableAction")
VariableAction = Class(name="VariableAction")
CompleteDSLPckg_WriteVariableAction = Class(name="CompleteDSLPckg::WriteVariableAction")
CompleteDSLPckg_Vertex = Class(name="CompleteDSLPckg::Vertex", is_abstract=True)
CompleteDSLPckg_Transition = Class(name="CompleteDSLPckg::Transition")
Vertex = Class(name="Vertex")
CompleteDSLPckg_ConnectionPointReference = Class(name="CompleteDSLPckg::ConnectionPointReference")
CompleteDSLPckg_Activity = Class(name="CompleteDSLPckg::Activity")
CompleteDSLPckg_ActivityNode = Class(name="CompleteDSLPckg::ActivityNode", is_abstract=True)
CompleteDSLPckg_ActivityGroup = Class(name="CompleteDSLPckg::ActivityGroup", is_abstract=True)
CompleteDSLPckg_ActivityEdge = Class(name="CompleteDSLPckg::ActivityEdge", is_abstract=True)
CompleteDSLPckg_ActivityPartition = Class(name="CompleteDSLPckg::ActivityPartition")
CompleteDSLPckg_StructuredActivityNode = Class(name="CompleteDSLPckg::StructuredActivityNode")
CompleteDSLPckg_FinalState = Class(name="CompleteDSLPckg::FinalState")
State = Class(name="State")
CompleteDSLPckg_ProtocolStateMachine = Class(name="CompleteDSLPckg::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
CompleteDSLPckg_ProtocolConformance = Class(name="CompleteDSLPckg::ProtocolConformance")
CompleteDSLPckg_ProtocolTransition = Class(name="CompleteDSLPckg::ProtocolTransition")
Transition = Class(name="Transition")
CompleteDSLPckg_InterruptibleActivityRegion = Class(name="CompleteDSLPckg::InterruptibleActivityRegion")
CompleteDSLPckg_ControlFlow = Class(name="CompleteDSLPckg::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
CompleteDSLPckg_ObjectFlow = Class(name="CompleteDSLPckg::ObjectFlow")
CompleteDSLPckg_ObjectNode = Class(name="CompleteDSLPckg::ObjectNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
CompleteDSLPckg_ActivityParameterNode = Class(name="CompleteDSLPckg::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
CompleteDSLPckg_ControlNode = Class(name="CompleteDSLPckg::ControlNode", is_abstract=True)
CompleteDSLPckg_ActivityFinalNode = Class(name="CompleteDSLPckg::ActivityFinalNode")
ControlNode = Class(name="ControlNode")
FinalNode = Class(name="FinalNode")
CompleteDSLPckg_InitialNode = Class(name="CompleteDSLPckg::InitialNode")
CompleteDSLPckg_ForkNode = Class(name="CompleteDSLPckg::ForkNode")
CompleteDSLPckg_JoinNode = Class(name="CompleteDSLPckg::JoinNode")
CompleteDSLPckg_MergeNode = Class(name="CompleteDSLPckg::MergeNode")
CompleteDSLPckg_DecisionNode = Class(name="CompleteDSLPckg::DecisionNode")
ActivityGroup = Class(name="ActivityGroup")
CompleteDSLPckg_CentralBufferNode = Class(name="CompleteDSLPckg::CentralBufferNode")
CompleteDSLPckg_FinalNode = Class(name="CompleteDSLPckg::FinalNode", is_abstract=True)
CompleteDSLPckg_FlowFinalNode = Class(name="CompleteDSLPckg::FlowFinalNode")
ExecutableNode = Class(name="ExecutableNode")
CompleteDSLPckg_DataStoreNode = Class(name="CompleteDSLPckg::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
CompleteDSLPckg_ParameterSet = Class(name="CompleteDSLPckg::ParameterSet")
CompleteDSLPckg_ConditionalNode = Class(name="CompleteDSLPckg::ConditionalNode")
CompleteDSLPckg_Clause = Class(name="CompleteDSLPckg::Clause")
CompleteDSLPckg_ExecutableNode = Class(name="CompleteDSLPckg::ExecutableNode")
CompleteDSLPckg_ExceptionHandler = Class(name="CompleteDSLPckg::ExceptionHandler")
CompleteDSLPckg_LoopNode = Class(name="CompleteDSLPckg::LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
CompleteDSLPckg_ExpansionRegion = Class(name="CompleteDSLPckg::ExpansionRegion")
CompleteDSLPckg_ExpansionNode = Class(name="CompleteDSLPckg::ExpansionNode")
CompleteDSLPckg_SequenceNode = Class(name="CompleteDSLPckg::SequenceNode")
CompleteDSLPckg_StateInvariant = Class(name="CompleteDSLPckg::StateInvariant")
CompleteDSLPckg_Interaction = Class(name="CompleteDSLPckg::Interaction")
CompleteDSLPckg_Gate = Class(name="CompleteDSLPckg::Gate")
CompleteDSLPckg_InteractionFragment = Class(name="CompleteDSLPckg::InteractionFragment", is_abstract=True)
CompleteDSLPckg_Lifeline = Class(name="CompleteDSLPckg::Lifeline")
CompleteDSLPckg_GeneralOrdering = Class(name="CompleteDSLPckg::GeneralOrdering")
CompleteDSLPckg_InteractionOperand = Class(name="CompleteDSLPckg::InteractionOperand")
CompleteDSLPckg_ExecutionSpecification = Class(name="CompleteDSLPckg::ExecutionSpecification", is_abstract=True)
InteractionFragment = Class(name="InteractionFragment")
CompleteDSLPckg_OccurenceSpecification = Class(name="CompleteDSLPckg::OccurenceSpecification")
CompleteDSLPckg_MessageEnd = Class(name="CompleteDSLPckg::MessageEnd", is_abstract=True)
CompleteDSLPckg_ExecutionOccurrenceSpecification = Class(name="CompleteDSLPckg::ExecutionOccurrenceSpecification")
OccurenceSpecification = Class(name="OccurenceSpecification")
CompleteDSLPckg_PartDecomposition = Class(name="CompleteDSLPckg::PartDecomposition")
CompleteDSLPckg_Message = Class(name="CompleteDSLPckg::Message")
CompleteDSLPckg_InteractionConstraint = Class(name="CompleteDSLPckg::InteractionConstraint")
CompleteDSLPckg_CombinedFragment = Class(name="CompleteDSLPckg::CombinedFragment")
CompleteDSLPckg_ConsiderIgnoreFragment = Class(name="CompleteDSLPckg::ConsiderIgnoreFragment")
CombinedFragment = Class(name="CombinedFragment")
CompleteDSLPckg_MessageOccurrenceSpecification = Class(name="CompleteDSLPckg::MessageOccurrenceSpecification")
CompleteDSLPckg_DestructionOccurrenceSpecification = Class(name="CompleteDSLPckg::DestructionOccurrenceSpecification")
MessageOccurrenceSpecification = Class(name="MessageOccurrenceSpecification")
CompleteDSLPckg_BehaviorExecutionSpecification = Class(name="CompleteDSLPckg::BehaviorExecutionSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
CompleteDSLPckg_ActionExecutionSpecification = Class(name="CompleteDSLPckg::ActionExecutionSpecification")
InteractionUse = Class(name="InteractionUse")
CompleteDSLPckg_Actor = Class(name="CompleteDSLPckg::Actor")
CompleteDSLPckg_UseCase = Class(name="CompleteDSLPckg::UseCase")
CompleteDSLPckg_ExtensionPoint = Class(name="CompleteDSLPckg::ExtensionPoint")
CompleteDSLPckg_Extend = Class(name="CompleteDSLPckg::Extend")
CompleteDSLPckg_Include = Class(name="CompleteDSLPckg::Include")
CompleteDSLPckg_Continuation = Class(name="CompleteDSLPckg::Continuation")
MessageEnd = Class(name="MessageEnd")
CompleteDSLPckg_InteractionUse = Class(name="CompleteDSLPckg::InteractionUse")

# CompleteDSLPckg_Element class attributes and methods

# CompleteDSLPckg_Comment class attributes and methods
CompleteDSLPckg_Comment_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_Comment.attributes={CompleteDSLPckg_Comment_body}

# CompleteDSLPckg_NamedElement class attributes and methods
CompleteDSLPckg_NamedElement_name: Property = Property(name="name", type=StringType)
CompleteDSLPckg_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
CompleteDSLPckg_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_NamedElement.attributes={CompleteDSLPckg_NamedElement_name, CompleteDSLPckg_NamedElement_qualifiedName, CompleteDSLPckg_NamedElement_visibility}

# Element class attributes and methods

# CompleteDSLPckg_Namespace class attributes and methods

# CompleteDSLPckg_Constraint class attributes and methods

# DirectedRelationship class attributes and methods

# CompleteDSLPckg_Package class attributes and methods
CompleteDSLPckg_Package_URI: Property = Property(name="URI", type=StringType)
CompleteDSLPckg_Package.attributes={CompleteDSLPckg_Package_URI}

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# CompleteDSLPckg_Dependency class attributes and methods

# NamedElement class attributes and methods

# CompleteDSLPckg_PackageableElement class attributes and methods

# CompleteDSLPckg_ElementImport class attributes and methods
CompleteDSLPckg_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_ElementImport_alias: Property = Property(name="alias", type=StringType)
CompleteDSLPckg_ElementImport.attributes={CompleteDSLPckg_ElementImport_visibility, CompleteDSLPckg_ElementImport_alias}

# CompleteDSLPckg_PackageImport class attributes and methods
CompleteDSLPckg_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_PackageImport.attributes={CompleteDSLPckg_PackageImport_visibility}

# CompleteDSLPckg_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# CompleteDSLPckg_MultiplicityElement class attributes and methods
CompleteDSLPckg_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
CompleteDSLPckg_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
CompleteDSLPckg_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
CompleteDSLPckg_MultiplicityElement.attributes={CompleteDSLPckg_MultiplicityElement_isUnique, CompleteDSLPckg_MultiplicityElement_lower, CompleteDSLPckg_MultiplicityElement_isOrdered, CompleteDSLPckg_MultiplicityElement_upper}

# CompleteDSLPckg_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# CompleteDSLPckg_Type class attributes and methods

# CompleteDSLPckg_PackageMerge class attributes and methods

# CompleteDSLPckg_Relationship class attributes and methods

# CompleteDSLPckg_InstanceSpecification class attributes and methods

# CompleteDSLPckg_TypedElement class attributes and methods

# CompleteDSLPckg_Expression class attributes and methods
CompleteDSLPckg_Expression_symbol: Property = Property(name="symbol", type=StringType)
CompleteDSLPckg_Expression.attributes={CompleteDSLPckg_Expression_symbol}

# ValueSpecification class attributes and methods

# CompleteDSLPckg_Slot class attributes and methods

# CompleteDSLPckg_LiteralInteger class attributes and methods

# CompleteDSLPckg_LiteralReal class attributes and methods

# CompleteDSLPckg_LiteralString class attributes and methods

# CompleteDSLPckg_LiteralUnilimitedNatural class attributes and methods

# CompleteDSLPckg_InstanceValue class attributes and methods

# CompleteDSLPckg_Classifier class attributes and methods
CompleteDSLPckg_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
CompleteDSLPckg_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=BooleanType)
CompleteDSLPckg_Classifier.attributes={CompleteDSLPckg_Classifier_isFinalSpecialization, CompleteDSLPckg_Classifier_isAbstract}

# CompleteDSLPckg_OpaqueExpression class attributes and methods
CompleteDSLPckg_OpaqueExpression_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_OpaqueExpression_language: Property = Property(name="language", type=StringType)
CompleteDSLPckg_OpaqueExpression.attributes={CompleteDSLPckg_OpaqueExpression_body, CompleteDSLPckg_OpaqueExpression_language}

# CompleteDSLPckg_Parameter class attributes and methods
CompleteDSLPckg_Parameter_default: Property = Property(name="default", type=StringType)
CompleteDSLPckg_Parameter.attributes={CompleteDSLPckg_Parameter_default}

# CompleteDSLPckg_Behavior class attributes and methods
CompleteDSLPckg_Behavior_isReentrant: Property = Property(name="isReentrant", type=BooleanType)
CompleteDSLPckg_Behavior.attributes={CompleteDSLPckg_Behavior_isReentrant}

# CompleteDSLPckg_LiteralSpecification class attributes and methods

# CompleteDSLPckg_LiteralNull class attributes and methods

# LiteralSpecification class attributes and methods

# CompleteDSLPckg_LiteralBoolean class attributes and methods

# CompleteDSLPckg_Feature class attributes and methods
CompleteDSLPckg_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
CompleteDSLPckg_Feature.attributes={CompleteDSLPckg_Feature_isStatic}

# CompleteDSLPckg_Property class attributes and methods
CompleteDSLPckg_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
CompleteDSLPckg_Property_isID: Property = Property(name="isID", type=BooleanType)
CompleteDSLPckg_Property_aggregation: Property = Property(name="aggregation", type=StringType)
CompleteDSLPckg_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
CompleteDSLPckg_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
CompleteDSLPckg_Property_default: Property = Property(name="default", type=StringType)
CompleteDSLPckg_Property.attributes={CompleteDSLPckg_Property_isDerived, CompleteDSLPckg_Property_isDerivedUnion, CompleteDSLPckg_Property_default, CompleteDSLPckg_Property_isID, CompleteDSLPckg_Property_isComposite, CompleteDSLPckg_Property_aggregation}

# CompleteDSLPckg_Generalization class attributes and methods
CompleteDSLPckg_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
CompleteDSLPckg_Generalization.attributes={CompleteDSLPckg_Generalization_isSubstitutable}

# CompleteDSLPckg_Substitution class attributes and methods

# CompleteDSLPckg_GeneralizationSet class attributes and methods
CompleteDSLPckg_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
CompleteDSLPckg_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
CompleteDSLPckg_GeneralizationSet.attributes={CompleteDSLPckg_GeneralizationSet_isDisjoint, CompleteDSLPckg_GeneralizationSet_isCovering}

# CompleteDSLPckg_StructuralFeature class attributes and methods
CompleteDSLPckg_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
CompleteDSLPckg_StructuralFeature.attributes={CompleteDSLPckg_StructuralFeature_isReadOnly}

# CompleteDSLPckg_RedefinableElement class attributes and methods
CompleteDSLPckg_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
CompleteDSLPckg_RedefinableElement.attributes={CompleteDSLPckg_RedefinableElement_isLeaf}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# CompleteDSLPckg_Class class attributes and methods

# CompleteDSLPckg_Association class attributes and methods
CompleteDSLPckg_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
CompleteDSLPckg_Association.attributes={CompleteDSLPckg_Association_isDerived}

# CompleteDSLPckg_DataType class attributes and methods

# CompleteDSLPckg_Interface class attributes and methods

# CompleteDSLPckg_CollaborationUse class attributes and methods

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# CompleteDSLPckg_Operation class attributes and methods
CompleteDSLPckg_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
CompleteDSLPckg_Operation_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_Operation_isUnique: Property = Property(name="isUnique", type=BooleanType)
CompleteDSLPckg_Operation_upper: Property = Property(name="upper", type=IntegerType)
CompleteDSLPckg_Operation_lower: Property = Property(name="lower", type=IntegerType)
CompleteDSLPckg_Operation.attributes={CompleteDSLPckg_Operation_isUnique, CompleteDSLPckg_Operation_isOrdered, CompleteDSLPckg_Operation_lower, CompleteDSLPckg_Operation_isQuery, CompleteDSLPckg_Operation_upper}

# BehavioralFeature class attributes and methods

# CompleteDSLPckg_BehavioralFeature class attributes and methods

# CompleteDSLPckg_PrimitiveType class attributes and methods

# DataType class attributes and methods

# CompleteDSLPckg_Enumeration class attributes and methods

# CompleteDSLPckg_EnumerationLiteral class attributes and methods

# Classifier class attributes and methods

# BehavioredClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# CompleteDSLPckg_Reception class attributes and methods

# CompleteDSLPckg_Realization class attributes and methods

# Abstraction class attributes and methods

# Realization class attributes and methods

# CompleteDSLPckg_InterfaceRealization class attributes and methods

# InstanceSpecification class attributes and methods

# CompleteDSLPckg_Usage class attributes and methods

# Dependency class attributes and methods

# CompleteDSLPckg_Abstraction class attributes and methods

# CompleteDSLPckg_OpaqueBehavior class attributes and methods
CompleteDSLPckg_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
CompleteDSLPckg_OpaqueBehavior.attributes={CompleteDSLPckg_OpaqueBehavior_language, CompleteDSLPckg_OpaqueBehavior_body}

# Behavior class attributes and methods

# CompleteDSLPckg_BehavioredClassifier class attributes and methods

# CompleteDSLPckg_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# CompleteDSLPckg_Trigger class attributes and methods

# CompleteDSLPckg_Event class attributes and methods

# CompleteDSLPckg_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# CompleteDSLPckg_Signal class attributes and methods

# CompleteDSLPckg_TimeEvent class attributes and methods
CompleteDSLPckg_TimeEvent_isRelative: Property = Property(name="isRelative", type=BooleanType)
CompleteDSLPckg_TimeEvent.attributes={CompleteDSLPckg_TimeEvent_isRelative}

# CompleteDSLPckg_TimeExpression class attributes and methods

# CompleteDSLPckg_Observation class attributes and methods

# CompleteDSLPckg_TimeObservation class attributes and methods
CompleteDSLPckg_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_TimeObservation.attributes={CompleteDSLPckg_TimeObservation_firstEvent}

# Observation class attributes and methods

# CompleteDSLPckg_MessageEvent class attributes and methods

# Event class attributes and methods

# CompleteDSLPckg_AnyReceiveEvent class attributes and methods

# MessageEvent class attributes and methods

# CompleteDSLPckg_SignalEvent class attributes and methods

# CompleteDSLPckg_CallEvent class attributes and methods

# CompleteDSLPckg_ChangeEvent class attributes and methods

# CompleteDSLPckg_TimeInterval class attributes and methods

# Interval class attributes and methods

# CompleteDSLPckg_DurationInterval class attributes and methods

# CompleteDSLPckg_IntervalConstraint class attributes and methods

# Constraint class attributes and methods

# CompleteDSLPckg_TimeConstraint class attributes and methods
CompleteDSLPckg_TimeConstraint_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_TimeConstraint.attributes={CompleteDSLPckg_TimeConstraint_firstEvent}

# IntervalConstraint class attributes and methods

# CompleteDSLPckg_DurationConstraint class attributes and methods
CompleteDSLPckg_DurationConstraint_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_DurationConstraint.attributes={CompleteDSLPckg_DurationConstraint_firstEvent}

# CompleteDSLPckg_Component class attributes and methods
CompleteDSLPckg_Component_isIndirectlyInstantiated: Property = Property(name="isIndirectlyInstantiated", type=BooleanType)
CompleteDSLPckg_Component.attributes={CompleteDSLPckg_Component_isIndirectlyInstantiated}

# CompleteDSLPckg_DurationObservation class attributes and methods
CompleteDSLPckg_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_DurationObservation.attributes={CompleteDSLPckg_DurationObservation_firstEvent}

# CompleteDSLPckg_Duration class attributes and methods

# CompleteDSLPckg_Interval class attributes and methods

# CompleteDSLPckg_ConnectorEnd class attributes and methods

# CompleteDSLPckg_ConnectableElement class attributes and methods

# CompleteDSLPckg_StructuredClassifier class attributes and methods

# CompleteDSLPckg_ComponentRealization class attributes and methods

# CompleteDSLPckg_Connector class attributes and methods
CompleteDSLPckg_Connector_kind: Property = Property(name="kind", type=StringType)
CompleteDSLPckg_Connector.attributes={CompleteDSLPckg_Connector_kind}

# CompleteDSLPckg_EncapsulatedClassifier class attributes and methods

# CompleteDSLPckg_Collaboration class attributes and methods

# CompleteDSLPckg_InvocationAction class attributes and methods

# CompleteDSLPckg_Variable class attributes and methods

# CompleteDSLPckg_Port class attributes and methods
CompleteDSLPckg_Port_isBehavior: Property = Property(name="isBehavior", type=BooleanType)
CompleteDSLPckg_Port_isService: Property = Property(name="isService", type=BooleanType)
CompleteDSLPckg_Port_isConjugated: Property = Property(name="isConjugated", type=BooleanType)
CompleteDSLPckg_Port.attributes={CompleteDSLPckg_Port_isService, CompleteDSLPckg_Port_isBehavior, CompleteDSLPckg_Port_isConjugated}

# Property class attributes and methods

# CompleteDSLPckg_Device class attributes and methods

# Node class attributes and methods

# CompleteDSLPckg_ExecutionEnvironment class attributes and methods

# CompleteDSLPckg_CommunicationPath class attributes and methods

# CompleteDSLPckg_DeploymentTarget class attributes and methods

# CompleteDSLPckg_Deployment class attributes and methods

# CompleteDSLPckg_DeployedArtifact class attributes and methods

# CompleteDSLPckg_DeploymentSpecification class attributes and methods
CompleteDSLPckg_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
CompleteDSLPckg_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
CompleteDSLPckg_DeploymentSpecification.attributes={CompleteDSLPckg_DeploymentSpecification_executionLocation, CompleteDSLPckg_DeploymentSpecification_deploymentLocation}

# Artifact class attributes and methods

# CompleteDSLPckg_Artifact class attributes and methods
CompleteDSLPckg_Artifact_fileName: Property = Property(name="fileName", type=StringType)
CompleteDSLPckg_Artifact.attributes={CompleteDSLPckg_Artifact_fileName}

# DeployedArtifact class attributes and methods

# CompleteDSLPckg_Manifestation class attributes and methods

# CompleteDSLPckg_Node class attributes and methods

# Pin class attributes and methods

# CompleteDSLPckg_Pin class attributes and methods

# CompleteDSLPckg_ValuePin class attributes and methods

# InputPin class attributes and methods

# CompleteDSLPckg_CallAction class attributes and methods
CompleteDSLPckg_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=BooleanType)
CompleteDSLPckg_CallAction.attributes={CompleteDSLPckg_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# CompleteDSLPckg_CallBehaviorAction class attributes and methods

# CallAction class attributes and methods

# CompleteDSLPckg_CallOperationAction class attributes and methods

# CompleteDSLPckg_SendSignalAction class attributes and methods

# CompleteDSLPckg_Action class attributes and methods

# CompleteDSLPckg_InputPin class attributes and methods

# CompleteDSLPckg_OutputPin class attributes and methods

# CompleteDSLPckg_OpaqueAction class attributes and methods
CompleteDSLPckg_OpaqueAction_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_OpaqueAction_language: Property = Property(name="language", type=StringType)
CompleteDSLPckg_OpaqueAction.attributes={CompleteDSLPckg_OpaqueAction_body, CompleteDSLPckg_OpaqueAction_language}

# Action class attributes and methods

# CompleteDSLPckg_DestroyObjectAction class attributes and methods

# CompleteDSLPckg_TestIdentityAction class attributes and methods

# CompleteDSLPckg_ReadSelfAction class attributes and methods

# CompleteDSLPckg_ValueSpecificationAction class attributes and methods

# CompleteDSLPckg_StructuralFeatureAction class attributes and methods

# CompleteDSLPckg_BroadcastSignalAction class attributes and methods

# CompleteDSLPckg_SendObjectAction class attributes and methods

# CompleteDSLPckg_CreateObjectAction class attributes and methods

# CompleteDSLPckg_ClearStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_LinkAction class attributes and methods

# CompleteDSLPckg_LinkEndData class attributes and methods

# CompleteDSLPckg_QualifierValue class attributes and methods

# CompleteDSLPckg_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# CompleteDSLPckg_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# CompleteDSLPckg_WriteStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_AddStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_RemoveStructuralFeatureValueAction class attributes and methods

# CompleteDSLPckg_UnmarshallAction class attributes and methods

# CompleteDSLPckg_WriteLinkAction class attributes and methods

# CompleteDSLPckg_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# CompleteDSLPckg_LinkEndCreationData class attributes and methods
CompleteDSLPckg_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
CompleteDSLPckg_LinkEndCreationData.attributes={CompleteDSLPckg_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# CompleteDSLPckg_DestroyLinkAction class attributes and methods

# CompleteDSLPckg_LinkEndDestructionData class attributes and methods
CompleteDSLPckg_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=BooleanType)
CompleteDSLPckg_LinkEndDestructionData.attributes={CompleteDSLPckg_LinkEndDestructionData_isDestroyDuplicates}

# CompleteDSLPckg_ReplyAction class attributes and methods

# CompleteDSLPckg_ReclassifyObjectAction class attributes and methods
CompleteDSLPckg_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
CompleteDSLPckg_ReclassifyObjectAction.attributes={CompleteDSLPckg_ReclassifyObjectAction_isReplaceAll}

# CompleteDSLPckg_ReadlsClassifiedObjectAction class attributes and methods

# CompleteDSLPckg_StartClassifierBehaviorAction class attributes and methods

# CompleteDSLPckg_StartObjectBehaviorAction class attributes and methods

# CompleteDSLPckg_AcceptEventAction class attributes and methods
CompleteDSLPckg_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=BooleanType)
CompleteDSLPckg_AcceptEventAction.attributes={CompleteDSLPckg_AcceptEventAction_isUnmarshall}

# CompleteDSLPckg_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# CompleteDSLPckg_ReadExtendAction class attributes and methods

# CompleteDSLPckg_ReadLinkObjectEndQualifierAction class attributes and methods

# CompleteDSLPckg_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# CompleteDSLPckg_ReduceAction class attributes and methods
CompleteDSLPckg_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_ReduceAction.attributes={CompleteDSLPckg_ReduceAction_isOrdered}

# CompleteDSLPckg_ReadLinkObjectEndAction class attributes and methods

# CompleteDSLPckg_AddVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# CompleteDSLPckg_RemoveVariableValueAction class attributes and methods

# CompleteDSLPckg_ClearVariableAction class attributes and methods

# CompleteDSLPckg_RaiseExceptionAction class attributes and methods

# CompleteDSLPckg_ActionInputPin class attributes and methods

# CompleteDSLPckg_StateMachine class attributes and methods

# CompleteDSLPckg_Region class attributes and methods

# CompleteDSLPckg_Pseudostate class attributes and methods

# CompleteDSLPckg_State class attributes and methods
CompleteDSLPckg_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
CompleteDSLPckg_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
CompleteDSLPckg_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
CompleteDSLPckg_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
CompleteDSLPckg_State.attributes={CompleteDSLPckg_State_isOrthogonal, CompleteDSLPckg_State_isSubmachineState, CompleteDSLPckg_State_isSimple, CompleteDSLPckg_State_isComposite}

# CompleteDSLPckg_VariableAction class attributes and methods

# CompleteDSLPckg_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# CompleteDSLPckg_WriteVariableAction class attributes and methods

# CompleteDSLPckg_Vertex class attributes and methods

# CompleteDSLPckg_Transition class attributes and methods
CompleteDSLPckg_Transition_kind: Property = Property(name="kind", type=StringType)
CompleteDSLPckg_Transition.attributes={CompleteDSLPckg_Transition_kind}

# Vertex class attributes and methods

# CompleteDSLPckg_ConnectionPointReference class attributes and methods

# CompleteDSLPckg_Activity class attributes and methods
CompleteDSLPckg_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
CompleteDSLPckg_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
CompleteDSLPckg_Activity.attributes={CompleteDSLPckg_Activity_isSingleExecution, CompleteDSLPckg_Activity_isReadOnly}

# CompleteDSLPckg_ActivityNode class attributes and methods

# CompleteDSLPckg_ActivityGroup class attributes and methods

# CompleteDSLPckg_ActivityEdge class attributes and methods

# CompleteDSLPckg_ActivityPartition class attributes and methods

# CompleteDSLPckg_StructuredActivityNode class attributes and methods
CompleteDSLPckg_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
CompleteDSLPckg_StructuredActivityNode.attributes={CompleteDSLPckg_StructuredActivityNode_mustIsolate}

# CompleteDSLPckg_FinalState class attributes and methods

# State class attributes and methods

# CompleteDSLPckg_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# CompleteDSLPckg_ProtocolConformance class attributes and methods

# CompleteDSLPckg_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# CompleteDSLPckg_InterruptibleActivityRegion class attributes and methods

# CompleteDSLPckg_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# CompleteDSLPckg_ObjectFlow class attributes and methods
CompleteDSLPckg_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
CompleteDSLPckg_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
CompleteDSLPckg_ObjectFlow_ordering: Property = Property(name="ordering", type=StringType)
CompleteDSLPckg_ObjectFlow_isControlType: Property = Property(name="isControlType", type=BooleanType)
CompleteDSLPckg_ObjectFlow.attributes={CompleteDSLPckg_ObjectFlow_isControlType, CompleteDSLPckg_ObjectFlow_isMulticast, CompleteDSLPckg_ObjectFlow_ordering, CompleteDSLPckg_ObjectFlow_isMultireceive}

# CompleteDSLPckg_ObjectNode class attributes and methods

# ActivityNode class attributes and methods

# CompleteDSLPckg_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# CompleteDSLPckg_ControlNode class attributes and methods

# CompleteDSLPckg_ActivityFinalNode class attributes and methods

# ControlNode class attributes and methods

# FinalNode class attributes and methods

# CompleteDSLPckg_InitialNode class attributes and methods

# CompleteDSLPckg_ForkNode class attributes and methods

# CompleteDSLPckg_JoinNode class attributes and methods
CompleteDSLPckg_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
CompleteDSLPckg_JoinNode.attributes={CompleteDSLPckg_JoinNode_isCombineDuplicate}

# CompleteDSLPckg_MergeNode class attributes and methods

# CompleteDSLPckg_DecisionNode class attributes and methods

# ActivityGroup class attributes and methods

# CompleteDSLPckg_CentralBufferNode class attributes and methods

# CompleteDSLPckg_FinalNode class attributes and methods

# CompleteDSLPckg_FlowFinalNode class attributes and methods

# ExecutableNode class attributes and methods

# CompleteDSLPckg_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# CompleteDSLPckg_ParameterSet class attributes and methods

# CompleteDSLPckg_ConditionalNode class attributes and methods
CompleteDSLPckg_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
CompleteDSLPckg_ConditionalNode_isAssumed: Property = Property(name="isAssumed", type=BooleanType)
CompleteDSLPckg_ConditionalNode.attributes={CompleteDSLPckg_ConditionalNode_isDeterminate, CompleteDSLPckg_ConditionalNode_isAssumed}

# CompleteDSLPckg_Clause class attributes and methods

# CompleteDSLPckg_ExecutableNode class attributes and methods

# CompleteDSLPckg_ExceptionHandler class attributes and methods

# CompleteDSLPckg_LoopNode class attributes and methods
CompleteDSLPckg_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
CompleteDSLPckg_LoopNode.attributes={CompleteDSLPckg_LoopNode_isTestedFirst}

# StructuredActivityNode class attributes and methods

# CompleteDSLPckg_ExpansionRegion class attributes and methods
CompleteDSLPckg_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
CompleteDSLPckg_ExpansionRegion.attributes={CompleteDSLPckg_ExpansionRegion_mode}

# CompleteDSLPckg_ExpansionNode class attributes and methods

# CompleteDSLPckg_SequenceNode class attributes and methods

# CompleteDSLPckg_StateInvariant class attributes and methods

# CompleteDSLPckg_Interaction class attributes and methods

# CompleteDSLPckg_Gate class attributes and methods

# CompleteDSLPckg_InteractionFragment class attributes and methods

# CompleteDSLPckg_Lifeline class attributes and methods

# CompleteDSLPckg_GeneralOrdering class attributes and methods

# CompleteDSLPckg_InteractionOperand class attributes and methods

# CompleteDSLPckg_ExecutionSpecification class attributes and methods

# InteractionFragment class attributes and methods

# CompleteDSLPckg_OccurenceSpecification class attributes and methods

# CompleteDSLPckg_MessageEnd class attributes and methods

# CompleteDSLPckg_ExecutionOccurrenceSpecification class attributes and methods

# OccurenceSpecification class attributes and methods

# CompleteDSLPckg_PartDecomposition class attributes and methods

# CompleteDSLPckg_Message class attributes and methods
CompleteDSLPckg_Message_messageKind: Property = Property(name="messageKind", type=StringType)
CompleteDSLPckg_Message_messageSort: Property = Property(name="messageSort", type=StringType)
CompleteDSLPckg_Message.attributes={CompleteDSLPckg_Message_messageKind, CompleteDSLPckg_Message_messageSort}

# CompleteDSLPckg_InteractionConstraint class attributes and methods

# CompleteDSLPckg_CombinedFragment class attributes and methods
CompleteDSLPckg_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
CompleteDSLPckg_CombinedFragment.attributes={CompleteDSLPckg_CombinedFragment_interactionOperator}

# CompleteDSLPckg_ConsiderIgnoreFragment class attributes and methods

# CombinedFragment class attributes and methods

# CompleteDSLPckg_MessageOccurrenceSpecification class attributes and methods

# CompleteDSLPckg_DestructionOccurrenceSpecification class attributes and methods

# MessageOccurrenceSpecification class attributes and methods

# CompleteDSLPckg_BehaviorExecutionSpecification class attributes and methods

# ExecutionSpecification class attributes and methods

# CompleteDSLPckg_ActionExecutionSpecification class attributes and methods

# InteractionUse class attributes and methods

# CompleteDSLPckg_Actor class attributes and methods

# CompleteDSLPckg_UseCase class attributes and methods

# CompleteDSLPckg_ExtensionPoint class attributes and methods

# CompleteDSLPckg_Extend class attributes and methods

# CompleteDSLPckg_Include class attributes and methods

# CompleteDSLPckg_Continuation class attributes and methods
CompleteDSLPckg_Continuation_setting: Property = Property(name="setting", type=BooleanType)
CompleteDSLPckg_Continuation.attributes={CompleteDSLPckg_Continuation_setting}

# MessageEnd class attributes and methods

# CompleteDSLPckg_InteractionUse class attributes and methods

# Relationships
ownedComment0: BinaryAssociation = BinaryAssociation(
    name="ownedComment0",
    ends={
        Property(name="1", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement3: BinaryAssociation = BinaryAssociation(
    name="ownedElement3",
    ends={
        Property(name="5", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="9", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
namespace10: BinaryAssociation = BinaryAssociation(
    name="namespace10",
    ends={
        Property(name="12", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedRule28: BinaryAssociation = BinaryAssociation(
    name="ownedRule28",
    ends={
        Property(name="30", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="29", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement31: BinaryAssociation = BinaryAssociation(
    name="importedElement31",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement32", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ElementImport", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace33: BinaryAssociation = BinaryAssociation(
    name="importingNamespace33",
    ends={
        Property(name="35", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="34", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage36: BinaryAssociation = BinaryAssociation(
    name="importedPackage36",
    ends={
        Property(name="CompleteDSLPckg_Package", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_PackageImport", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace37: BinaryAssociation = BinaryAssociation(
    name="importingNamespace37",
    ends={
        Property(name="39", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="38", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage41: BinaryAssociation = BinaryAssociation(
    name="nestedPackage41",
    ends={
        Property(name="43", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="42", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clientDependency13: BinaryAssociation = BinaryAssociation(
    name="clientDependency13",
    ends={
        Property(name="15", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember16: BinaryAssociation = BinaryAssociation(
    name="importedMember16",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Namespace", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member17: BinaryAssociation = BinaryAssociation(
    name="member17",
    ends={
        Property(name="CompleteDSLPckg_NamedElement", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Namespace18", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember19: BinaryAssociation = BinaryAssociation(
    name="ownedMember19",
    ends={
        Property(name="21", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport22: BinaryAssociation = BinaryAssociation(
    name="elementImport22",
    ends={
        Property(name="24", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport25: BinaryAssociation = BinaryAssociation(
    name="packageImport25",
    ends={
        Property(name="27", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="26", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target63: BinaryAssociation = BinaryAssociation(
    name="target63",
    ends={
        Property(name="CompleteDSLPckg_Element64", type=CompleteDSLPckg_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DirectedRelationship", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="CompleteDSLPckg_Element67", type=CompleteDSLPckg_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DirectedRelationship66", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
upperValue68: BinaryAssociation = BinaryAssociation(
    name="upperValue68",
    ends={
        Property(name="70", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="69", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue71: BinaryAssociation = BinaryAssociation(
    name="lowerValue71",
    ends={
        Property(name="73", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="72", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningUpper74: BinaryAssociation = BinaryAssociation(
    name="owningUpper74",
    ends={
        Property(name="76", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="75", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningLower77: BinaryAssociation = BinaryAssociation(
    name="owningLower77",
    ends={
        Property(name="79", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="78", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningConstraint80: BinaryAssociation = BinaryAssociation(
    name="owningConstraint80",
    ends={
        Property(name="82", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="81", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
nestingPackage45: BinaryAssociation = BinaryAssociation(
    name="nestingPackage45",
    ends={
        Property(name="47", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="46", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement48: BinaryAssociation = BinaryAssociation(
    name="packagedElement48",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement50", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Package49", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType51: BinaryAssociation = BinaryAssociation(
    name="ownedType51",
    ends={
        Property(name="53", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="52", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge54: BinaryAssociation = BinaryAssociation(
    name="packageMerge54",
    ends={
        Property(name="56", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="55", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningElement57: BinaryAssociation = BinaryAssociation(
    name="owningElement57",
    ends={
        Property(name="59", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="58", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement60: BinaryAssociation = BinaryAssociation(
    name="annotatedElement60",
    ends={
        Property(name="CompleteDSLPckg_Element", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Comment", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999))
    }
)
relatedElement61: BinaryAssociation = BinaryAssociation(
    name="relatedElement61",
    ends={
        Property(name="CompleteDSLPckg_Element62", type=CompleteDSLPckg_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Relationship", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
owningInstanceSpec86: BinaryAssociation = BinaryAssociation(
    name="owningInstanceSpec86",
    ends={
        Property(name="88", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="87", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
type89: BinaryAssociation = BinaryAssociation(
    name="type89",
    ends={
        Property(name="CompleteDSLPckg_Type", type=CompleteDSLPckg_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TypedElement", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
package90: BinaryAssociation = BinaryAssociation(
    name="package90",
    ends={
        Property(name="92", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="91", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 1))
    }
)
owningSlot83: BinaryAssociation = BinaryAssociation(
    name="owningSlot83",
    ends={
        Property(name="85", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="84", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(0, 1))
    }
)
instance97: BinaryAssociation = BinaryAssociation(
    name="instance97",
    ends={
        Property(name="CompleteDSLPckg_InstanceSpecification", type=CompleteDSLPckg_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InstanceValue", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot98: BinaryAssociation = BinaryAssociation(
    name="slot98",
    ends={
        Property(name="100", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="99", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification101: BinaryAssociation = BinaryAssociation(
    name="specification101",
    ends={
        Property(name="103", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="102", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier104: BinaryAssociation = BinaryAssociation(
    name="classifier104",
    ends={
        Property(name="CompleteDSLPckg_Classifier", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InstanceSpecification105", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context106: BinaryAssociation = BinaryAssociation(
    name="context106",
    ends={
        Property(name="108", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="107", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement109: BinaryAssociation = BinaryAssociation(
    name="constrainedElement109",
    ends={
        Property(name="CompleteDSLPckg_Element110", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Constraint", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999))
    }
)
operand93: BinaryAssociation = BinaryAssociation(
    name="operand93",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Expression", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result94: BinaryAssociation = BinaryAssociation(
    name="result94",
    ends={
        Property(name="CompleteDSLPckg_Parameter", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueExpression", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior95: BinaryAssociation = BinaryAssociation(
    name="behavior95",
    ends={
        Property(name="CompleteDSLPckg_Behavior", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueExpression96", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
inheritedMember126: BinaryAssociation = BinaryAssociation(
    name="inheritedMember126",
    ends={
        Property(name="CompleteDSLPckg_NamedElement128", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier127", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature129: BinaryAssociation = BinaryAssociation(
    name="feature129",
    ends={
        Property(name="131", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="130", type=CompleteDSLPckg_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute132: BinaryAssociation = BinaryAssociation(
    name="attribute132",
    ends={
        Property(name="CompleteDSLPckg_Property", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier133", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier135: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier135",
    ends={
        Property(name="CompleteDSLPckg_Classifier136", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier134", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general138: BinaryAssociation = BinaryAssociation(
    name="general138",
    ends={
        Property(name="CompleteDSLPckg_Classifier139", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier137", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization140: BinaryAssociation = BinaryAssociation(
    name="generalization140",
    ends={
        Property(name="142", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="141", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution143: BinaryAssociation = BinaryAssociation(
    name="substitution143",
    ends={
        Property(name="145", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="144", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent146: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent146",
    ends={
        Property(name="148", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="147", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
specification111: BinaryAssociation = BinaryAssociation(
    name="specification111",
    ends={
        Property(name="113", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="112", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningInstace114: BinaryAssociation = BinaryAssociation(
    name="owningInstace114",
    ends={
        Property(name="116", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="115", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value117: BinaryAssociation = BinaryAssociation(
    name="value117",
    ends={
        Property(name="119", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="118", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature120: BinaryAssociation = BinaryAssociation(
    name="definingFeature120",
    ends={
        Property(name="CompleteDSLPckg_StructuralFeature", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Slot", type=CompleteDSLPckg_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement122: BinaryAssociation = BinaryAssociation(
    name="redefinedElement122",
    ends={
        Property(name="CompleteDSLPckg_RedefinableElement", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RedefinableElement121", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext123: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext123",
    ends={
        Property(name="CompleteDSLPckg_Classifier125", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RedefinableElement124", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
class157: BinaryAssociation = BinaryAssociation(
    name="class157",
    ends={
        Property(name="159", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="158", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty161: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty161",
    ends={
        Property(name="CompleteDSLPckg_Property162", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property160", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue163: BinaryAssociation = BinaryAssociation(
    name="defaultValue163",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification165", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property164", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite167: BinaryAssociation = BinaryAssociation(
    name="opposite167",
    ends={
        Property(name="CompleteDSLPckg_Property168", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property166", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty170: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty170",
    ends={
        Property(name="CompleteDSLPckg_Property171", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property169", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
association172: BinaryAssociation = BinaryAssociation(
    name="association172",
    ends={
        Property(name="174", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="173", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation175: BinaryAssociation = BinaryAssociation(
    name="owningAssociation175",
    ends={
        Property(name="177", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="176", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
dataType178: BinaryAssociation = BinaryAssociation(
    name="dataType178",
    ends={
        Property(name="180", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="179", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface181: BinaryAssociation = BinaryAssociation(
    name="interface181",
    ends={
        Property(name="183", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="182", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 1))
    }
)
collaborationUse149: BinaryAssociation = BinaryAssociation(
    name="collaborationUse149",
    ends={
        Property(name="CompleteDSLPckg_CollaborationUse", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier150", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representation151: BinaryAssociation = BinaryAssociation(
    name="representation151",
    ends={
        Property(name="CompleteDSLPckg_CollaborationUse153", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier152", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier154: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier154",
    ends={
        Property(name="156", type=CompleteDSLPckg_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="155", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedFormalParam205: BinaryAssociation = BinaryAssociation(
    name="ownedFormalParam205",
    ends={
        Property(name="CompleteDSLPckg_BehavioralFeature207", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Parameter206", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue208: BinaryAssociation = BinaryAssociation(
    name="defaultValue208",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification210", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Parameter209", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type211: BinaryAssociation = BinaryAssociation(
    name="type211",
    ends={
        Property(name="CompleteDSLPckg_Type212", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition213: BinaryAssociation = BinaryAssociation(
    name="precondition213",
    ends={
        Property(name="CompleteDSLPckg_Constraint215", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation214", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition216: BinaryAssociation = BinaryAssociation(
    name="bodyCondition216",
    ends={
        Property(name="CompleteDSLPckg_Constraint218", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation217", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition219: BinaryAssociation = BinaryAssociation(
    name="postcondition219",
    ends={
        Property(name="CompleteDSLPckg_Constraint221", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation220", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class222: BinaryAssociation = BinaryAssociation(
    name="class222",
    ends={
        Property(name="224", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="223", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 1))
    }
)
qualifier185: BinaryAssociation = BinaryAssociation(
    name="qualifier185",
    ends={
        Property(name="187", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="186", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd189: BinaryAssociation = BinaryAssociation(
    name="associationEnd189",
    ends={
        Property(name="191", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="190", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
general192: BinaryAssociation = BinaryAssociation(
    name="general192",
    ends={
        Property(name="CompleteDSLPckg_Classifier193", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Generalization", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific194: BinaryAssociation = BinaryAssociation(
    name="specific194",
    ends={
        Property(name="196", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="195", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet197: BinaryAssociation = BinaryAssociation(
    name="generalizationSet197",
    ends={
        Property(name="199", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="198", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter200: BinaryAssociation = BinaryAssociation(
    name="ownedParameter200",
    ends={
        Property(name="CompleteDSLPckg_Parameter201", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioralFeature", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException202: BinaryAssociation = BinaryAssociation(
    name="raisedException202",
    ends={
        Property(name="CompleteDSLPckg_Type204", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioralFeature203", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
navigableOwnedEnd244: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd244",
    ends={
        Property(name="CompleteDSLPckg_Property245", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Association", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
memberEnd246: BinaryAssociation = BinaryAssociation(
    name="memberEnd246",
    ends={
        Property(name="248", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="247", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd249: BinaryAssociation = BinaryAssociation(
    name="ownedEnd249",
    ends={
        Property(name="251", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="250", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute252: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute252",
    ends={
        Property(name="254", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="253", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation255: BinaryAssociation = BinaryAssociation(
    name="ownedOperation255",
    ends={
        Property(name="257", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="256", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral258: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral258",
    ends={
        Property(name="260", type=CompleteDSLPckg_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="259", type=CompleteDSLPckg_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType225: BinaryAssociation = BinaryAssociation(
    name="dataType225",
    ends={
        Property(name="227", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="226", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface228: BinaryAssociation = BinaryAssociation(
    name="interface228",
    ends={
        Property(name="230", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="229", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier231: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier231",
    ends={
        Property(name="CompleteDSLPckg_Classifier232", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation233: BinaryAssociation = BinaryAssociation(
    name="ownedOperation233",
    ends={
        Property(name="235", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="234", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass237: BinaryAssociation = BinaryAssociation(
    name="superClass237",
    ends={
        Property(name="CompleteDSLPckg_Class238", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class236", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute239: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute239",
    ends={
        Property(name="241", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="240", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception242: BinaryAssociation = BinaryAssociation(
    name="ownedReception242",
    ends={
        Property(name="CompleteDSLPckg_Reception", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class243", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapping274: BinaryAssociation = BinaryAssociation(
    name="mapping274",
    ends={
        Property(name="CompleteDSLPckg_OpaqueExpression275", type=CompleteDSLPckg_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Abstraction", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substitutingClassifier276: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier276",
    ends={
        Property(name="278", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="277", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract279: BinaryAssociation = BinaryAssociation(
    name="contract279",
    ends={
        Property(name="CompleteDSLPckg_Classifier280", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Substitution", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
nestedClassifier281: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier281",
    ends={
        Property(name="CompleteDSLPckg_Classifier282", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedInterface284: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface284",
    ends={
        Property(name="CompleteDSLPckg_Interface285", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface283", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute286: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute286",
    ends={
        Property(name="288", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="287", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation289: BinaryAssociation = BinaryAssociation(
    name="ownedOperation289",
    ends={
        Property(name="291", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="290", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception292: BinaryAssociation = BinaryAssociation(
    name="ownedReception292",
    ends={
        Property(name="CompleteDSLPckg_Reception294", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface293", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration261: BinaryAssociation = BinaryAssociation(
    name="enumeration261",
    ends={
        Property(name="263", type=CompleteDSLPckg_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="262", type=CompleteDSLPckg_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage264: BinaryAssociation = BinaryAssociation(
    name="receivingPackage264",
    ends={
        Property(name="266", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="265", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage267: BinaryAssociation = BinaryAssociation(
    name="mergedPackage267",
    ends={
        Property(name="CompleteDSLPckg_Package268", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_PackageMerge", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
client269: BinaryAssociation = BinaryAssociation(
    name="client269",
    ends={
        Property(name="271", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="270", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier272: BinaryAssociation = BinaryAssociation(
    name="supplier272",
    ends={
        Property(name="CompleteDSLPckg_NamedElement273", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Dependency", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
generalization311: BinaryAssociation = BinaryAssociation(
    name="generalization311",
    ends={
        Property(name="313", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="312", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
context314: BinaryAssociation = BinaryAssociation(
    name="context314",
    ends={
        Property(name="CompleteDSLPckg_BehavioredClassifier316", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior315", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
redefinedBehavior318: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior318",
    ends={
        Property(name="CompleteDSLPckg_Behavior319", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior317", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification320: BinaryAssociation = BinaryAssociation(
    name="specification320",
    ends={
        Property(name="CompleteDSLPckg_BehavioralFeature322", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior321", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter323: BinaryAssociation = BinaryAssociation(
    name="ownedParameter323",
    ends={
        Property(name="CompleteDSLPckg_Parameter325", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior324", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition326: BinaryAssociation = BinaryAssociation(
    name="precondition326",
    ends={
        Property(name="CompleteDSLPckg_Constraint328", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior327", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition329: BinaryAssociation = BinaryAssociation(
    name="postcondition329",
    ends={
        Property(name="CompleteDSLPckg_Constraint331", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior330", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementingClassifier295: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier295",
    ends={
        Property(name="297", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="296", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
contract298: BinaryAssociation = BinaryAssociation(
    name="contract298",
    ends={
        Property(name="CompleteDSLPckg_Interface299", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterfaceRealization", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRealization300: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization300",
    ends={
        Property(name="302", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="301", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior303: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior303",
    ends={
        Property(name="CompleteDSLPckg_Behavior304", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioredClassifier", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior305: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior305",
    ends={
        Property(name="CompleteDSLPckg_Behavior307", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioredClassifier306", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
powertype308: BinaryAssociation = BinaryAssociation(
    name="powertype308",
    ends={
        Property(name="310", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="309", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute332: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute332",
    ends={
        Property(name="CompleteDSLPckg_Signal", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="CompleteDSLPckg_Property333", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal334: BinaryAssociation = BinaryAssociation(
    name="signal334",
    ends={
        Property(name="CompleteDSLPckg_Signal336", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Reception335", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
event337: BinaryAssociation = BinaryAssociation(
    name="event337",
    ends={
        Property(name="CompleteDSLPckg_Event", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Trigger", type=CompleteDSLPckg_Event, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression342: BinaryAssociation = BinaryAssociation(
    name="changeExpression342",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification343", type=CompleteDSLPckg_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ChangeEvent", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
when344: BinaryAssociation = BinaryAssociation(
    name="when344",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression", type=CompleteDSLPckg_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeEvent", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr345: BinaryAssociation = BinaryAssociation(
    name="expr345",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification347", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeExpression346", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation348: BinaryAssociation = BinaryAssociation(
    name="observation348",
    ends={
        Property(name="CompleteDSLPckg_Observation", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeExpression349", type=CompleteDSLPckg_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
signal338: BinaryAssociation = BinaryAssociation(
    name="signal338",
    ends={
        Property(name="CompleteDSLPckg_Signal339", type=CompleteDSLPckg_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SignalEvent", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation340: BinaryAssociation = BinaryAssociation(
    name="operation340",
    ends={
        Property(name="CompleteDSLPckg_Operation341", type=CompleteDSLPckg_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallEvent", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1))
    }
)
timeMax364: BinaryAssociation = BinaryAssociation(
    name="timeMax364",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression365", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeInterval", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
timeMin366: BinaryAssociation = BinaryAssociation(
    name="timeMin366",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression368", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeInterval367", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
durationMax369: BinaryAssociation = BinaryAssociation(
    name="durationMax369",
    ends={
        Property(name="CompleteDSLPckg_Duration370", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationInterval", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1))
    }
)
durationMin371: BinaryAssociation = BinaryAssociation(
    name="durationMin371",
    ends={
        Property(name="CompleteDSLPckg_Duration373", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationInterval372", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1))
    }
)
timeSpecification374: BinaryAssociation = BinaryAssociation(
    name="timeSpecification374",
    ends={
        Property(name="CompleteDSLPckg_TimeInterval375", type=CompleteDSLPckg_TimeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeConstraint", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1))
    }
)
durationSpecification376: BinaryAssociation = BinaryAssociation(
    name="durationSpecification376",
    ends={
        Property(name="CompleteDSLPckg_DurationInterval377", type=CompleteDSLPckg_DurationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationConstraint", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1))
    }
)
event350: BinaryAssociation = BinaryAssociation(
    name="event350",
    ends={
        Property(name="CompleteDSLPckg_NamedElement351", type=CompleteDSLPckg_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeObservation", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event352: BinaryAssociation = BinaryAssociation(
    name="event352",
    ends={
        Property(name="CompleteDSLPckg_NamedElement353", type=CompleteDSLPckg_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationObservation", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
expr354: BinaryAssociation = BinaryAssociation(
    name="expr354",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification355", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Duration", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation356: BinaryAssociation = BinaryAssociation(
    name="observation356",
    ends={
        Property(name="CompleteDSLPckg_Observation358", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Duration357", type=CompleteDSLPckg_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
max359: BinaryAssociation = BinaryAssociation(
    name="max359",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification360", type=CompleteDSLPckg_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interval", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
min361: BinaryAssociation = BinaryAssociation(
    name="min361",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification363", type=CompleteDSLPckg_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interval362", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
end394: BinaryAssociation = BinaryAssociation(
    name="end394",
    ends={
        Property(name="CompleteDSLPckg_ConnectorEnd", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract395: BinaryAssociation = BinaryAssociation(
    name="contract395",
    ends={
        Property(name="CompleteDSLPckg_Behavior397", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector396", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedConnector399: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector399",
    ends={
        Property(name="CompleteDSLPckg_Connector400", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector398", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
partWithPort401: BinaryAssociation = BinaryAssociation(
    name="partWithPort401",
    ends={
        Property(name="CompleteDSLPckg_Property403", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd402", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
role404: BinaryAssociation = BinaryAssociation(
    name="role404",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd405", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
type406: BinaryAssociation = BinaryAssociation(
    name="type406",
    ends={
        Property(name="CompleteDSLPckg_Association408", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd407", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
definingEnd409: BinaryAssociation = BinaryAssociation(
    name="definingEnd409",
    ends={
        Property(name="CompleteDSLPckg_Property411", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd410", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
end412: BinaryAssociation = BinaryAssociation(
    name="end412",
    ends={
        Property(name="CompleteDSLPckg_ConnectorEnd414", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectableElement413", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
required378: BinaryAssociation = BinaryAssociation(
    name="required378",
    ends={
        Property(name="CompleteDSLPckg_Interface379", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided380: BinaryAssociation = BinaryAssociation(
    name="provided380",
    ends={
        Property(name="CompleteDSLPckg_Interface382", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component381", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
realization383: BinaryAssociation = BinaryAssociation(
    name="realization383",
    ends={
        Property(name="CompleteDSLPckg_ComponentRealization", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component384", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement385: BinaryAssociation = BinaryAssociation(
    name="packagedElement385",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement387", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component386", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstraction388: BinaryAssociation = BinaryAssociation(
    name="abstraction388",
    ends={
        Property(name="CompleteDSLPckg_Component390", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ComponentRealization389", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier391: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier391",
    ends={
        Property(name="CompleteDSLPckg_Classifier393", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ComponentRealization392", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
provided428: BinaryAssociation = BinaryAssociation(
    name="provided428",
    ends={
        Property(name="CompleteDSLPckg_Interface430", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port429", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort432: BinaryAssociation = BinaryAssociation(
    name="redefinedPort432",
    ends={
        Property(name="CompleteDSLPckg_Port433", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port431", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPort434: BinaryAssociation = BinaryAssociation(
    name="ownedPort434",
    ends={
        Property(name="CompleteDSLPckg_Port435", type=CompleteDSLPckg_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_EncapsulatedClassifier", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationRole436: BinaryAssociation = BinaryAssociation(
    name="collaborationRole436",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement437", type=CompleteDSLPckg_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Collaboration", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
type438: BinaryAssociation = BinaryAssociation(
    name="type438",
    ends={
        Property(name="CompleteDSLPckg_Collaboration440", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CollaborationUse439", type=CompleteDSLPckg_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding441: BinaryAssociation = BinaryAssociation(
    name="roleBinding441",
    ends={
        Property(name="CompleteDSLPckg_Dependency443", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CollaborationUse442", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onPort444: BinaryAssociation = BinaryAssociation(
    name="onPort444",
    ends={
        Property(name="CompleteDSLPckg_Port445", type=CompleteDSLPckg_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InvocationAction", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 1))
    }
)
ownedConnector415: BinaryAssociation = BinaryAssociation(
    name="ownedConnector415",
    ends={
        Property(name="CompleteDSLPckg_Connector416", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role417: BinaryAssociation = BinaryAssociation(
    name="role417",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement419", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier418", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
structuredOwnedAttribute420: BinaryAssociation = BinaryAssociation(
    name="structuredOwnedAttribute420",
    ends={
        Property(name="CompleteDSLPckg_Property422", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier421", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part423: BinaryAssociation = BinaryAssociation(
    name="part423",
    ends={
        Property(name="CompleteDSLPckg_Property425", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier424", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
required426: BinaryAssociation = BinaryAssociation(
    name="required426",
    ends={
        Property(name="CompleteDSLPckg_Interface427", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
nestedNode460: BinaryAssociation = BinaryAssociation(
    name="nestedNode460",
    ends={
        Property(name="CompleteDSLPckg_Node", type=CompleteDSLPckg_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Node459", type=CompleteDSLPckg_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement461: BinaryAssociation = BinaryAssociation(
    name="deployedElement461",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement462", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentTarget", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployment463: BinaryAssociation = BinaryAssociation(
    name="deployment463",
    ends={
        Property(name="CompleteDSLPckg_Deployment", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentTarget464", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location465: BinaryAssociation = BinaryAssociation(
    name="location465",
    ends={
        Property(name="CompleteDSLPckg_DeploymentTarget467", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment466", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
deployedArtifact468: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact468",
    ends={
        Property(name="CompleteDSLPckg_DeployedArtifact", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment469", type=CompleteDSLPckg_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
configuration470: BinaryAssociation = BinaryAssociation(
    name="configuration470",
    ends={
        Property(name="CompleteDSLPckg_DeploymentSpecification", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment471", type=CompleteDSLPckg_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation446: BinaryAssociation = BinaryAssociation(
    name="ownedOperation446",
    ends={
        Property(name="CompleteDSLPckg_Operation447", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute448: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute448",
    ends={
        Property(name="CompleteDSLPckg_Property450", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact449", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedArtifact452: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact452",
    ends={
        Property(name="CompleteDSLPckg_Artifact453", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact451", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation454: BinaryAssociation = BinaryAssociation(
    name="manifestation454",
    ends={
        Property(name="CompleteDSLPckg_Manifestation", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact455", type=CompleteDSLPckg_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizedElement456: BinaryAssociation = BinaryAssociation(
    name="utilizedElement456",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement458", type=CompleteDSLPckg_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Manifestation457", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
outputValue483: BinaryAssociation = BinaryAssociation(
    name="outputValue483",
    ends={
        Property(name="CompleteDSLPckg_OpaqueAction484", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="CompleteDSLPckg_OutputPin485", type=CompleteDSLPckg_OpaqueAction, multiplicity=Multiplicity(1, 1))
    }
)
value486: BinaryAssociation = BinaryAssociation(
    name="value486",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification487", type=CompleteDSLPckg_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValuePin", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
result488: BinaryAssociation = BinaryAssociation(
    name="result488",
    ends={
        Property(name="CompleteDSLPckg_OutputPin489", type=CompleteDSLPckg_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior490: BinaryAssociation = BinaryAssociation(
    name="behavior490",
    ends={
        Property(name="CompleteDSLPckg_Behavior491", type=CompleteDSLPckg_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallBehaviorAction", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation492: BinaryAssociation = BinaryAssociation(
    name="operation492",
    ends={
        Property(name="CompleteDSLPckg_Operation493", type=CompleteDSLPckg_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallOperationAction", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target494: BinaryAssociation = BinaryAssociation(
    name="target494",
    ends={
        Property(name="CompleteDSLPckg_InputPin496", type=CompleteDSLPckg_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallOperationAction495", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
deployment472: BinaryAssociation = BinaryAssociation(
    name="deployment472",
    ends={
        Property(name="CompleteDSLPckg_Deployment474", type=CompleteDSLPckg_DeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentSpecification473", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(0, 1))
    }
)
context475: BinaryAssociation = BinaryAssociation(
    name="context475",
    ends={
        Property(name="CompleteDSLPckg_Classifier476", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Action", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
input477: BinaryAssociation = BinaryAssociation(
    name="input477",
    ends={
        Property(name="CompleteDSLPckg_InputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Action478", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output479: BinaryAssociation = BinaryAssociation(
    name="output479",
    ends={
        Property(name="CompleteDSLPckg_OutputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Action480", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputValue481: BinaryAssociation = BinaryAssociation(
    name="inputValue481",
    ends={
        Property(name="CompleteDSLPckg_InputPin482", type=CompleteDSLPckg_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target514: BinaryAssociation = BinaryAssociation(
    name="target514",
    ends={
        Property(name="CompleteDSLPckg_InputPin515", type=CompleteDSLPckg_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DestroyObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result516: BinaryAssociation = BinaryAssociation(
    name="result516",
    ends={
        Property(name="CompleteDSLPckg_OutputPin517", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first518: BinaryAssociation = BinaryAssociation(
    name="first518",
    ends={
        Property(name="CompleteDSLPckg_InputPin520", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction519", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second521: BinaryAssociation = BinaryAssociation(
    name="second521",
    ends={
        Property(name="CompleteDSLPckg_InputPin523", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction522", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result524: BinaryAssociation = BinaryAssociation(
    name="result524",
    ends={
        Property(name="CompleteDSLPckg_OutputPin525", type=CompleteDSLPckg_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadSelfAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result526: BinaryAssociation = BinaryAssociation(
    name="result526",
    ends={
        Property(name="CompleteDSLPckg_OutputPin527", type=CompleteDSLPckg_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValueSpecificationAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value528: BinaryAssociation = BinaryAssociation(
    name="value528",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification530", type=CompleteDSLPckg_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValueSpecificationAction529", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target497: BinaryAssociation = BinaryAssociation(
    name="target497",
    ends={
        Property(name="CompleteDSLPckg_InputPin498", type=CompleteDSLPckg_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendSignalAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal499: BinaryAssociation = BinaryAssociation(
    name="signal499",
    ends={
        Property(name="CompleteDSLPckg_Signal501", type=CompleteDSLPckg_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendSignalAction500", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal502: BinaryAssociation = BinaryAssociation(
    name="signal502",
    ends={
        Property(name="CompleteDSLPckg_Signal503", type=CompleteDSLPckg_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BroadcastSignalAction", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
target504: BinaryAssociation = BinaryAssociation(
    name="target504",
    ends={
        Property(name="CompleteDSLPckg_InputPin505", type=CompleteDSLPckg_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request506: BinaryAssociation = BinaryAssociation(
    name="request506",
    ends={
        Property(name="CompleteDSLPckg_InputPin508", type=CompleteDSLPckg_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendObjectAction507", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier509: BinaryAssociation = BinaryAssociation(
    name="classifier509",
    ends={
        Property(name="CompleteDSLPckg_Classifier510", type=CompleteDSLPckg_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateObjectAction", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result511: BinaryAssociation = BinaryAssociation(
    name="result511",
    ends={
        Property(name="CompleteDSLPckg_OutputPin513", type=CompleteDSLPckg_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateObjectAction512", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
removeAt545: BinaryAssociation = BinaryAssociation(
    name="removeAt545",
    ends={
        Property(name="CompleteDSLPckg_RemoveStructuralFeatureValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="CompleteDSLPckg_InputPin546", type=CompleteDSLPckg_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1))
    }
)
result547: BinaryAssociation = BinaryAssociation(
    name="result547",
    ends={
        Property(name="CompleteDSLPckg_OutputPin548", type=CompleteDSLPckg_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ClearStructuralFeatureAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValue549: BinaryAssociation = BinaryAssociation(
    name="inputValue549",
    ends={
        Property(name="CompleteDSLPckg_InputPin550", type=CompleteDSLPckg_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
endData551: BinaryAssociation = BinaryAssociation(
    name="endData551",
    ends={
        Property(name="CompleteDSLPckg_LinkEndData", type=CompleteDSLPckg_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkAction552", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value553: BinaryAssociation = BinaryAssociation(
    name="value553",
    ends={
        Property(name="CompleteDSLPckg_InputPin555", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData554", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end556: BinaryAssociation = BinaryAssociation(
    name="end556",
    ends={
        Property(name="CompleteDSLPckg_Property558", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData557", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier559: BinaryAssociation = BinaryAssociation(
    name="qualifier559",
    ends={
        Property(name="CompleteDSLPckg_QualifierValue", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData560", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result561: BinaryAssociation = BinaryAssociation(
    name="result561",
    ends={
        Property(name="CompleteDSLPckg_OutputPin562", type=CompleteDSLPckg_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature531: BinaryAssociation = BinaryAssociation(
    name="structuralFeature531",
    ends={
        Property(name="CompleteDSLPckg_StructuralFeature532", type=CompleteDSLPckg_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuralFeatureAction", type=CompleteDSLPckg_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object533: BinaryAssociation = BinaryAssociation(
    name="object533",
    ends={
        Property(name="CompleteDSLPckg_InputPin535", type=CompleteDSLPckg_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuralFeatureAction534", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result536: BinaryAssociation = BinaryAssociation(
    name="result536",
    ends={
        Property(name="CompleteDSLPckg_OutputPin537", type=CompleteDSLPckg_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadStructuralFeatureAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value538: BinaryAssociation = BinaryAssociation(
    name="value538",
    ends={
        Property(name="CompleteDSLPckg_InputPin539", type=CompleteDSLPckg_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteStructuralFeatureAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result540: BinaryAssociation = BinaryAssociation(
    name="result540",
    ends={
        Property(name="CompleteDSLPckg_OutputPin542", type=CompleteDSLPckg_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteStructuralFeatureAction541", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt543: BinaryAssociation = BinaryAssociation(
    name="insertAt543",
    ends={
        Property(name="CompleteDSLPckg_InputPin544", type=CompleteDSLPckg_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AddStructuralFeatureValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
replyValue569: BinaryAssociation = BinaryAssociation(
    name="replyValue569",
    ends={
        Property(name="CompleteDSLPckg_InputPin571", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction570", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replyToCall572: BinaryAssociation = BinaryAssociation(
    name="replyToCall572",
    ends={
        Property(name="CompleteDSLPckg_Trigger574", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction573", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
object575: BinaryAssociation = BinaryAssociation(
    name="object575",
    ends={
        Property(name="CompleteDSLPckg_InputPin576", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unmarshallType577: BinaryAssociation = BinaryAssociation(
    name="unmarshallType577",
    ends={
        Property(name="CompleteDSLPckg_Classifier579", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction578", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result580: BinaryAssociation = BinaryAssociation(
    name="result580",
    ends={
        Property(name="CompleteDSLPckg_OutputPin582", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction581", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
insertAt563: BinaryAssociation = BinaryAssociation(
    name="insertAt563",
    ends={
        Property(name="CompleteDSLPckg_InputPin564", type=CompleteDSLPckg_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndCreationData", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destroyAt565: BinaryAssociation = BinaryAssociation(
    name="destroyAt565",
    ends={
        Property(name="CompleteDSLPckg_InputPin566", type=CompleteDSLPckg_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndDestructionData", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnInformation567: BinaryAssociation = BinaryAssociation(
    name="returnInformation567",
    ends={
        Property(name="CompleteDSLPckg_InputPin568", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object595: BinaryAssociation = BinaryAssociation(
    name="object595",
    ends={
        Property(name="CompleteDSLPckg_InputPin596", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier597: BinaryAssociation = BinaryAssociation(
    name="oldClassifier597",
    ends={
        Property(name="CompleteDSLPckg_Classifier599", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction598", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier600: BinaryAssociation = BinaryAssociation(
    name="newClassifier600",
    ends={
        Property(name="CompleteDSLPckg_Classifier602", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction601", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
result603: BinaryAssociation = BinaryAssociation(
    name="result603",
    ends={
        Property(name="CompleteDSLPckg_OutputPin604", type=CompleteDSLPckg_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadlsClassifiedObjectAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object605: BinaryAssociation = BinaryAssociation(
    name="object605",
    ends={
        Property(name="CompleteDSLPckg_InputPin607", type=CompleteDSLPckg_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadlsClassifiedObjectAction606", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object608: BinaryAssociation = BinaryAssociation(
    name="object608",
    ends={
        Property(name="CompleteDSLPckg_InputPin609", type=CompleteDSLPckg_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StartClassifierBehaviorAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result583: BinaryAssociation = BinaryAssociation(
    name="result583",
    ends={
        Property(name="CompleteDSLPckg_OutputPin584", type=CompleteDSLPckg_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptEventAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger585: BinaryAssociation = BinaryAssociation(
    name="trigger585",
    ends={
        Property(name="CompleteDSLPckg_Trigger587", type=CompleteDSLPckg_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptEventAction586", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnInformation588: BinaryAssociation = BinaryAssociation(
    name="returnInformation588",
    ends={
        Property(name="CompleteDSLPckg_OutputPin589", type=CompleteDSLPckg_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptCallAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result590: BinaryAssociation = BinaryAssociation(
    name="result590",
    ends={
        Property(name="CompleteDSLPckg_OutputPin591", type=CompleteDSLPckg_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadExtendAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier592: BinaryAssociation = BinaryAssociation(
    name="classifier592",
    ends={
        Property(name="CompleteDSLPckg_Classifier594", type=CompleteDSLPckg_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadExtendAction593", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
object626: BinaryAssociation = BinaryAssociation(
    name="object626",
    ends={
        Property(name="CompleteDSLPckg_InputPin627", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result628: BinaryAssociation = BinaryAssociation(
    name="result628",
    ends={
        Property(name="CompleteDSLPckg_OutputPin630", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction629", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier631: BinaryAssociation = BinaryAssociation(
    name="qualifier631",
    ends={
        Property(name="CompleteDSLPckg_Property633", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction632", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
result634: BinaryAssociation = BinaryAssociation(
    name="result634",
    ends={
        Property(name="CompleteDSLPckg_OutputPin635", type=CompleteDSLPckg_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateLinkObjectAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result636: BinaryAssociation = BinaryAssociation(
    name="result636",
    ends={
        Property(name="CompleteDSLPckg_OutputPin637", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection638: BinaryAssociation = BinaryAssociation(
    name="collection638",
    ends={
        Property(name="CompleteDSLPckg_InputPin640", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction639", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object610: BinaryAssociation = BinaryAssociation(
    name="object610",
    ends={
        Property(name="CompleteDSLPckg_InputPin611", type=CompleteDSLPckg_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StartObjectBehaviorAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier612: BinaryAssociation = BinaryAssociation(
    name="qualifier612",
    ends={
        Property(name="CompleteDSLPckg_Property614", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_QualifierValue613", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
value615: BinaryAssociation = BinaryAssociation(
    name="value615",
    ends={
        Property(name="CompleteDSLPckg_InputPin617", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_QualifierValue616", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
end618: BinaryAssociation = BinaryAssociation(
    name="end618",
    ends={
        Property(name="CompleteDSLPckg_Property619", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
object620: BinaryAssociation = BinaryAssociation(
    name="object620",
    ends={
        Property(name="CompleteDSLPckg_InputPin622", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction621", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result623: BinaryAssociation = BinaryAssociation(
    name="result623",
    ends={
        Property(name="CompleteDSLPckg_OutputPin625", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction624", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt649: BinaryAssociation = BinaryAssociation(
    name="insertAt649",
    ends={
        Property(name="CompleteDSLPckg_InputPin650", type=CompleteDSLPckg_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AddVariableValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt651: BinaryAssociation = BinaryAssociation(
    name="removeAt651",
    ends={
        Property(name="CompleteDSLPckg_InputPin652", type=CompleteDSLPckg_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RemoveVariableValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception653: BinaryAssociation = BinaryAssociation(
    name="exception653",
    ends={
        Property(name="CompleteDSLPckg_InputPin654", type=CompleteDSLPckg_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RaiseExceptionAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromAction655: BinaryAssociation = BinaryAssociation(
    name="fromAction655",
    ends={
        Property(name="CompleteDSLPckg_Action656", type=CompleteDSLPckg_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActionInputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
region657: BinaryAssociation = BinaryAssociation(
    name="region657",
    ends={
        Property(name="CompleteDSLPckg_Region", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint658: BinaryAssociation = BinaryAssociation(
    name="connectionPoint658",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine659", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reducer641: BinaryAssociation = BinaryAssociation(
    name="reducer641",
    ends={
        Property(name="CompleteDSLPckg_Behavior643", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction642", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
variable644: BinaryAssociation = BinaryAssociation(
    name="variable644",
    ends={
        Property(name="CompleteDSLPckg_Variable", type=CompleteDSLPckg_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_VariableAction", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(1, 1))
    }
)
result645: BinaryAssociation = BinaryAssociation(
    name="result645",
    ends={
        Property(name="CompleteDSLPckg_OutputPin646", type=CompleteDSLPckg_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadVariableAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value647: BinaryAssociation = BinaryAssociation(
    name="value647",
    ends={
        Property(name="CompleteDSLPckg_InputPin648", type=CompleteDSLPckg_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteVariableAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incoming681: BinaryAssociation = BinaryAssociation(
    name="incoming681",
    ends={
        Property(name="CompleteDSLPckg_Transition683", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex682", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container684: BinaryAssociation = BinaryAssociation(
    name="container684",
    ends={
        Property(name="CompleteDSLPckg_Region686", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex685", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
source687: BinaryAssociation = BinaryAssociation(
    name="source687",
    ends={
        Property(name="CompleteDSLPckg_Vertex689", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition688", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target690: BinaryAssociation = BinaryAssociation(
    name="target690",
    ends={
        Property(name="CompleteDSLPckg_Vertex692", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition691", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
effect693: BinaryAssociation = BinaryAssociation(
    name="effect693",
    ends={
        Property(name="CompleteDSLPckg_Behavior695", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition694", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger696: BinaryAssociation = BinaryAssociation(
    name="trigger696",
    ends={
        Property(name="CompleteDSLPckg_Trigger698", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition697", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard699: BinaryAssociation = BinaryAssociation(
    name="guard699",
    ends={
        Property(name="CompleteDSLPckg_Constraint701", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition700", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container702: BinaryAssociation = BinaryAssociation(
    name="container702",
    ends={
        Property(name="CompleteDSLPckg_Region704", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition703", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
submachineState660: BinaryAssociation = BinaryAssociation(
    name="submachineState660",
    ends={
        Property(name="CompleteDSLPckg_State", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine661", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine663: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine663",
    ends={
        Property(name="CompleteDSLPckg_StateMachine664", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine662", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex665: BinaryAssociation = BinaryAssociation(
    name="subvertex665",
    ends={
        Property(name="CompleteDSLPckg_Vertex", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region666", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine667: BinaryAssociation = BinaryAssociation(
    name="stateMachine667",
    ends={
        Property(name="CompleteDSLPckg_StateMachine669", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region668", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition670: BinaryAssociation = BinaryAssociation(
    name="transition670",
    ends={
        Property(name="CompleteDSLPckg_Transition", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region671", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state672: BinaryAssociation = BinaryAssociation(
    name="state672",
    ends={
        Property(name="CompleteDSLPckg_State674", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region673", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion676: BinaryAssociation = BinaryAssociation(
    name="extendedRegion676",
    ends={
        Property(name="CompleteDSLPckg_Region677", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region675", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing678: BinaryAssociation = BinaryAssociation(
    name="outgoing678",
    ends={
        Property(name="CompleteDSLPckg_Transition680", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex679", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
connection719: BinaryAssociation = BinaryAssociation(
    name="connection719",
    ends={
        Property(name="CompleteDSLPckg_ConnectionPointReference721", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State720", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint722: BinaryAssociation = BinaryAssociation(
    name="connectionPoint722",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate724", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State723", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine725: BinaryAssociation = BinaryAssociation(
    name="submachine725",
    ends={
        Property(name="CompleteDSLPckg_StateMachine727", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State726", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region728: BinaryAssociation = BinaryAssociation(
    name="region728",
    ends={
        Property(name="CompleteDSLPckg_Region730", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State729", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableTrigger731: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger731",
    ends={
        Property(name="CompleteDSLPckg_Trigger733", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State732", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit734: BinaryAssociation = BinaryAssociation(
    name="exit734",
    ends={
        Property(name="CompleteDSLPckg_Behavior736", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State735", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity737: BinaryAssociation = BinaryAssociation(
    name="doActivity737",
    ends={
        Property(name="CompleteDSLPckg_Behavior739", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State738", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry740: BinaryAssociation = BinaryAssociation(
    name="entry740",
    ends={
        Property(name="CompleteDSLPckg_Behavior742", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State741", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedTransition706: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition706",
    ends={
        Property(name="CompleteDSLPckg_Transition707", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition705", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 1))
    }
)
state708: BinaryAssociation = BinaryAssociation(
    name="state708",
    ends={
        Property(name="CompleteDSLPckg_State710", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Pseudostate709", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
exit711: BinaryAssociation = BinaryAssociation(
    name="exit711",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate712", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
entry713: BinaryAssociation = BinaryAssociation(
    name="entry713",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate715", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference714", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
state716: BinaryAssociation = BinaryAssociation(
    name="state716",
    ends={
        Property(name="CompleteDSLPckg_State718", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference717", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
preCondition756: BinaryAssociation = BinaryAssociation(
    name="preCondition756",
    ends={
        Property(name="CompleteDSLPckg_Constraint757", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postCondition758: BinaryAssociation = BinaryAssociation(
    name="postCondition758",
    ends={
        Property(name="CompleteDSLPckg_Constraint760", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition759", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred761: BinaryAssociation = BinaryAssociation(
    name="referred761",
    ends={
        Property(name="CompleteDSLPckg_Operation763", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition762", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
node764: BinaryAssociation = BinaryAssociation(
    name="node764",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group765: BinaryAssociation = BinaryAssociation(
    name="group765",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity766", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge767: BinaryAssociation = BinaryAssociation(
    name="edge767",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity768", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition769: BinaryAssociation = BinaryAssociation(
    name="partition769",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity770", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
stateInvariant743: BinaryAssociation = BinaryAssociation(
    name="stateInvariant743",
    ends={
        Property(name="CompleteDSLPckg_Constraint745", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State744", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState747: BinaryAssociation = BinaryAssociation(
    name="redefinedState747",
    ends={
        Property(name="CompleteDSLPckg_State748", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State746", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
conformance749: BinaryAssociation = BinaryAssociation(
    name="conformance749",
    ends={
        Property(name="CompleteDSLPckg_ProtocolConformance", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolStateMachine", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificMachine750: BinaryAssociation = BinaryAssociation(
    name="specificMachine750",
    ends={
        Property(name="CompleteDSLPckg_ProtocolStateMachine752", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolConformance751", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine753: BinaryAssociation = BinaryAssociation(
    name="generalMachine753",
    ends={
        Property(name="CompleteDSLPckg_ProtocolStateMachine755", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolConformance754", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
redefinedNode780: BinaryAssociation = BinaryAssociation(
    name="redefinedNode780",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode781", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode779", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
incoming782: BinaryAssociation = BinaryAssociation(
    name="incoming782",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge784", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode783", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing785: BinaryAssociation = BinaryAssociation(
    name="outgoing785",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge787", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode786", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition788: BinaryAssociation = BinaryAssociation(
    name="inPartition788",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition790", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode789", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion791: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion791",
    ends={
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode792", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode793: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode793",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode795", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode794", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
subgroup797: BinaryAssociation = BinaryAssociation(
    name="subgroup797",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup798", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup796", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superGroup800: BinaryAssociation = BinaryAssociation(
    name="superGroup800",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup801", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup799", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity802: BinaryAssociation = BinaryAssociation(
    name="inActivity802",
    ends={
        Property(name="CompleteDSLPckg_Activity804", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup803", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(0, 1))
    }
)
structuredNode771: BinaryAssociation = BinaryAssociation(
    name="structuredNode771",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity772", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable773: BinaryAssociation = BinaryAssociation(
    name="variable773",
    ends={
        Property(name="CompleteDSLPckg_Variable775", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity774", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inGroup776: BinaryAssociation = BinaryAssociation(
    name="inGroup776",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup778", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode777", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
source816: BinaryAssociation = BinaryAssociation(
    name="source816",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode818", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge817", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge820: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge820",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge821", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge819", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup822: BinaryAssociation = BinaryAssociation(
    name="inGroup822",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup824", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge823", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
guard825: BinaryAssociation = BinaryAssociation(
    name="guard825",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification827", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge826", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPartition828: BinaryAssociation = BinaryAssociation(
    name="inPartition828",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition830", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge829", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
weight831: BinaryAssociation = BinaryAssociation(
    name="weight831",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification833", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge832", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts834: BinaryAssociation = BinaryAssociation(
    name="interrupts834",
    ends={
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion836", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge835", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode837: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode837",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode839", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge838", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
containedNode805: BinaryAssociation = BinaryAssociation(
    name="containedNode805",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode807", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup806", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
containedEdge808: BinaryAssociation = BinaryAssociation(
    name="containedEdge808",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge810", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup809", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
parameter811: BinaryAssociation = BinaryAssociation(
    name="parameter811",
    ends={
        Property(name="CompleteDSLPckg_Parameter812", type=CompleteDSLPckg_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityParameterNode", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
target813: BinaryAssociation = BinaryAssociation(
    name="target813",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode815", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge814", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
joinSpec848: BinaryAssociation = BinaryAssociation(
    name="joinSpec848",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification849", type=CompleteDSLPckg_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_JoinNode", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decisionInputFlow850: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow850",
    ends={
        Property(name="CompleteDSLPckg_ObjectFlow851", type=CompleteDSLPckg_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DecisionNode", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput852: BinaryAssociation = BinaryAssociation(
    name="decisionInput852",
    ends={
        Property(name="CompleteDSLPckg_Behavior854", type=CompleteDSLPckg_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DecisionNode853", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
edge855: BinaryAssociation = BinaryAssociation(
    name="edge855",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge857", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition856", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition859: BinaryAssociation = BinaryAssociation(
    name="subpartition859",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition860", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition858", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition862: BinaryAssociation = BinaryAssociation(
    name="superPartition862",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition863", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition861", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
transformation840: BinaryAssociation = BinaryAssociation(
    name="transformation840",
    ends={
        Property(name="CompleteDSLPckg_Behavior841", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection842: BinaryAssociation = BinaryAssociation(
    name="selection842",
    ends={
        Property(name="CompleteDSLPckg_Behavior844", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow843", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
inState845: BinaryAssociation = BinaryAssociation(
    name="inState845",
    ends={
        Property(name="CompleteDSLPckg_State847", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow846", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 9999))
    }
)
node878: BinaryAssociation = BinaryAssociation(
    name="node878",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode880", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion879", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
activity881: BinaryAssociation = BinaryAssociation(
    name="activity881",
    ends={
        Property(name="CompleteDSLPckg_Activity883", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode882", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(0, 1))
    }
)
variable884: BinaryAssociation = BinaryAssociation(
    name="variable884",
    ends={
        Property(name="CompleteDSLPckg_Variable886", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode885", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node887: BinaryAssociation = BinaryAssociation(
    name="node887",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode889", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode888", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput890: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput890",
    ends={
        Property(name="CompleteDSLPckg_InputPin892", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode891", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge893: BinaryAssociation = BinaryAssociation(
    name="edge893",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge895", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode894", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
represents864: BinaryAssociation = BinaryAssociation(
    name="represents864",
    ends={
        Property(name="CompleteDSLPckg_Element866", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition865", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
node867: BinaryAssociation = BinaryAssociation(
    name="node867",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode869", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition868", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parameter870: BinaryAssociation = BinaryAssociation(
    name="parameter870",
    ends={
        Property(name="CompleteDSLPckg_Parameter871", type=CompleteDSLPckg_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ParameterSet", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
condition872: BinaryAssociation = BinaryAssociation(
    name="condition872",
    ends={
        Property(name="CompleteDSLPckg_Constraint874", type=CompleteDSLPckg_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ParameterSet873", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge875: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge875",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge877", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion876", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput911: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput911",
    ends={
        Property(name="CompleteDSLPckg_InputPin913", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode912", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable914: BinaryAssociation = BinaryAssociation(
    name="loopVariable914",
    ends={
        Property(name="CompleteDSLPckg_OutputPin916", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode915", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput917: BinaryAssociation = BinaryAssociation(
    name="bodyOutput917",
    ends={
        Property(name="CompleteDSLPckg_OutputPin919", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode918", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result920: BinaryAssociation = BinaryAssociation(
    name="result920",
    ends={
        Property(name="CompleteDSLPckg_OutputPin922", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode921", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause923: BinaryAssociation = BinaryAssociation(
    name="clause923",
    ends={
        Property(name="CompleteDSLPckg_Clause", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
test924: BinaryAssociation = BinaryAssociation(
    name="test924",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode926", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode925", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body927: BinaryAssociation = BinaryAssociation(
    name="body927",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode929", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode928", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
structuredNodeOutput896: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput896",
    ends={
        Property(name="CompleteDSLPckg_OutputPin898", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode897", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler899: BinaryAssociation = BinaryAssociation(
    name="handler899",
    ends={
        Property(name="CompleteDSLPckg_ExceptionHandler", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutableNode", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupPart900: BinaryAssociation = BinaryAssociation(
    name="setupPart900",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode901", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart902: BinaryAssociation = BinaryAssociation(
    name="bodyPart902",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode904", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode903", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test905: BinaryAssociation = BinaryAssociation(
    name="test905",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode907", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode906", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
decider908: BinaryAssociation = BinaryAssociation(
    name="decider908",
    ends={
        Property(name="CompleteDSLPckg_OutputPin910", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode909", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode947: BinaryAssociation = BinaryAssociation(
    name="protectedNode947",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode949", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler948", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput950: BinaryAssociation = BinaryAssociation(
    name="exceptionInput950",
    ends={
        Property(name="CompleteDSLPckg_ObjectNode", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler951", type=CompleteDSLPckg_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType952: BinaryAssociation = BinaryAssociation(
    name="exceptionType952",
    ends={
        Property(name="CompleteDSLPckg_Classifier954", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler953", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
inputElement955: BinaryAssociation = BinaryAssociation(
    name="inputElement955",
    ends={
        Property(name="CompleteDSLPckg_ExpansionNode", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionRegion", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement956: BinaryAssociation = BinaryAssociation(
    name="outputElement956",
    ends={
        Property(name="CompleteDSLPckg_ExpansionNode958", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionRegion957", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
regionAsInput959: BinaryAssociation = BinaryAssociation(
    name="regionAsInput959",
    ends={
        Property(name="CompleteDSLPckg_ExpansionRegion961", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionNode960", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
result930: BinaryAssociation = BinaryAssociation(
    name="result930",
    ends={
        Property(name="CompleteDSLPckg_OutputPin932", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode931", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessorClause934: BinaryAssociation = BinaryAssociation(
    name="predecessorClause934",
    ends={
        Property(name="CompleteDSLPckg_Clause935", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause933", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
sucessorClause937: BinaryAssociation = BinaryAssociation(
    name="sucessorClause937",
    ends={
        Property(name="CompleteDSLPckg_Clause938", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause936", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider939: BinaryAssociation = BinaryAssociation(
    name="decider939",
    ends={
        Property(name="CompleteDSLPckg_OutputPin941", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause940", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
executableNode942: BinaryAssociation = BinaryAssociation(
    name="executableNode942",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode943", type=CompleteDSLPckg_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SequenceNode", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handlerBody944: BinaryAssociation = BinaryAssociation(
    name="handlerBody944",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode946", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler945", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
toBefore974: BinaryAssociation = BinaryAssociation(
    name="toBefore974",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering976", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OccurenceSpecification975", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
toAfter977: BinaryAssociation = BinaryAssociation(
    name="toAfter977",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering979", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OccurenceSpecification978", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
invariant980: BinaryAssociation = BinaryAssociation(
    name="invariant980",
    ends={
        Property(name="CompleteDSLPckg_Constraint981", type=CompleteDSLPckg_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateInvariant", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragment982: BinaryAssociation = BinaryAssociation(
    name="fragment982",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment983", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeline984: BinaryAssociation = BinaryAssociation(
    name="lifeline984",
    ends={
        Property(name="CompleteDSLPckg_Lifeline986", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction985", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action987: BinaryAssociation = BinaryAssociation(
    name="action987",
    ends={
        Property(name="CompleteDSLPckg_Action989", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction988", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate990: BinaryAssociation = BinaryAssociation(
    name="formalGate990",
    ends={
        Property(name="CompleteDSLPckg_Gate", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction991", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput962: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput962",
    ends={
        Property(name="CompleteDSLPckg_ExpansionRegion964", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionNode963", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
covered965: BinaryAssociation = BinaryAssociation(
    name="covered965",
    ends={
        Property(name="CompleteDSLPckg_Lifeline", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering966: BinaryAssociation = BinaryAssociation(
    name="generalOrdering966",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment967", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingOperand968: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand968",
    ends={
        Property(name="CompleteDSLPckg_InteractionOperand", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment969", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
start970: BinaryAssociation = BinaryAssociation(
    name="start970",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionSpecification", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
finish971: BinaryAssociation = BinaryAssociation(
    name="finish971",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification973", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionSpecification972", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
signature1011: BinaryAssociation = BinaryAssociation(
    name="signature1011",
    ends={
        Property(name="CompleteDSLPckg_NamedElement1013", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message1012", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent1014: BinaryAssociation = BinaryAssociation(
    name="sendEvent1014",
    ends={
        Property(name="CompleteDSLPckg_MessageEnd", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message1015", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
receiveEvent1016: BinaryAssociation = BinaryAssociation(
    name="receiveEvent1016",
    ends={
        Property(name="CompleteDSLPckg_MessageEnd1018", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message1017", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
message1019: BinaryAssociation = BinaryAssociation(
    name="message1019",
    ends={
        Property(name="CompleteDSLPckg_Message1021", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_MessageEnd1020", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy992: BinaryAssociation = BinaryAssociation(
    name="coveredBy992",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment994", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline993", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
interaction995: BinaryAssociation = BinaryAssociation(
    name="interaction995",
    ends={
        Property(name="CompleteDSLPckg_Interaction997", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline996", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
represents998: BinaryAssociation = BinaryAssociation(
    name="represents998",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement1000", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline999", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
selector1001: BinaryAssociation = BinaryAssociation(
    name="selector1001",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1003", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline1002", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs1004: BinaryAssociation = BinaryAssociation(
    name="decomposedAs1004",
    ends={
        Property(name="CompleteDSLPckg_PartDecomposition", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline1005", type=CompleteDSLPckg_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
argument1006: BinaryAssociation = BinaryAssociation(
    name="argument1006",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1007", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector1008: BinaryAssociation = BinaryAssociation(
    name="connector1008",
    ends={
        Property(name="CompleteDSLPckg_Connector1010", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message1009", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 1))
    }
)
fragment1034: BinaryAssociation = BinaryAssociation(
    name="fragment1034",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment1036", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionOperand1035", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard1037: BinaryAssociation = BinaryAssociation(
    name="guard1037",
    ends={
        Property(name="CompleteDSLPckg_InteractionConstraint", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionOperand1038", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand1039: BinaryAssociation = BinaryAssociation(
    name="operand1039",
    ends={
        Property(name="CompleteDSLPckg_InteractionOperand1040", type=CompleteDSLPckg_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CombinedFragment", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cfragmentGate1041: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate1041",
    ends={
        Property(name="CompleteDSLPckg_Gate1043", type=CompleteDSLPckg_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CombinedFragment1042", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
execution1022: BinaryAssociation = BinaryAssociation(
    name="execution1022",
    ends={
        Property(name="CompleteDSLPckg_ExecutionSpecification1023", type=CompleteDSLPckg_ExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionOccurrenceSpecification", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
behavior1024: BinaryAssociation = BinaryAssociation(
    name="behavior1024",
    ends={
        Property(name="CompleteDSLPckg_Behavior1025", type=CompleteDSLPckg_BehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehaviorExecutionSpecification", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
action1026: BinaryAssociation = BinaryAssociation(
    name="action1026",
    ends={
        Property(name="CompleteDSLPckg_Action1027", type=CompleteDSLPckg_ActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActionExecutionSpecification", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1))
    }
)
after1028: BinaryAssociation = BinaryAssociation(
    name="after1028",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification1030", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_GeneralOrdering1029", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
before1031: BinaryAssociation = BinaryAssociation(
    name="before1031",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification1033", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_GeneralOrdering1032", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
returnValue1057: BinaryAssociation = BinaryAssociation(
    name="returnValue1057",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1059", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse1058", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValueRecipient1060: BinaryAssociation = BinaryAssociation(
    name="returnValueRecipient1060",
    ends={
        Property(name="CompleteDSLPckg_Property1062", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse1061", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
refersTo1063: BinaryAssociation = BinaryAssociation(
    name="refersTo1063",
    ends={
        Property(name="CompleteDSLPckg_Interaction1065", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse1064", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
subject1066: BinaryAssociation = BinaryAssociation(
    name="subject1066",
    ends={
        Property(name="CompleteDSLPckg_Classifier1067", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint1068: BinaryAssociation = BinaryAssociation(
    name="extensionPoint1068",
    ends={
        Property(name="CompleteDSLPckg_ExtensionPoint", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase1069", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend1070: BinaryAssociation = BinaryAssociation(
    name="extend1070",
    ends={
        Property(name="CompleteDSLPckg_Extend", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase1071", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include1072: BinaryAssociation = BinaryAssociation(
    name="include1072",
    ends={
        Property(name="CompleteDSLPckg_Include", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase1073", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(0, 9999))
    }
)
message1044: BinaryAssociation = BinaryAssociation(
    name="message1044",
    ends={
        Property(name="CompleteDSLPckg_NamedElement1045", type=CompleteDSLPckg_ConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConsiderIgnoreFragment", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maxint1046: BinaryAssociation = BinaryAssociation(
    name="maxint1046",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1048", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionConstraint1047", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minint1049: BinaryAssociation = BinaryAssociation(
    name="minint1049",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1051", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionConstraint1050", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualGate1052: BinaryAssociation = BinaryAssociation(
    name="actualGate1052",
    ends={
        Property(name="CompleteDSLPckg_Gate1053", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument1054: BinaryAssociation = BinaryAssociation(
    name="argument1054",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification1056", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse1055", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includingCase1089: BinaryAssociation = BinaryAssociation(
    name="includingCase1089",
    ends={
        Property(name="CompleteDSLPckg_UseCase1091", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Include1090", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
addition1092: BinaryAssociation = BinaryAssociation(
    name="addition1092",
    ends={
        Property(name="CompleteDSLPckg_UseCase1094", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Include1093", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase1074: BinaryAssociation = BinaryAssociation(
    name="useCase1074",
    ends={
        Property(name="CompleteDSLPckg_UseCase1076", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExtensionPoint1075", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionLocation1077: BinaryAssociation = BinaryAssociation(
    name="extensionLocation1077",
    ends={
        Property(name="CompleteDSLPckg_ExtensionPoint1079", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1078", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension1080: BinaryAssociation = BinaryAssociation(
    name="extension1080",
    ends={
        Property(name="CompleteDSLPckg_UseCase1082", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1081", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition1083: BinaryAssociation = BinaryAssociation(
    name="condition1083",
    ends={
        Property(name="CompleteDSLPckg_Constraint1085", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1084", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedCase1086: BinaryAssociation = BinaryAssociation(
    name="extendedCase1086",
    ends={
        Property(name="CompleteDSLPckg_UseCase1088", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1087", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CompleteDSLPckg_NamedElement_Element = Generalization(general=Element, specific=CompleteDSLPckg_NamedElement)
gen_CompleteDSLPckg_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_PackageableElement)
gen_CompleteDSLPckg_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_ElementImport)
gen_CompleteDSLPckg_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_PackageImport)
gen_CompleteDSLPckg_Package_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Package)
gen_CompleteDSLPckg_Package_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Package)
gen_CompleteDSLPckg_Namespace_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Namespace)
gen_CompleteDSLPckg_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=CompleteDSLPckg_DirectedRelationship)
gen_CompleteDSLPckg_MultiplicityElement_Element = Generalization(general=Element, specific=CompleteDSLPckg_MultiplicityElement)
gen_CompleteDSLPckg_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ValueSpecification)
gen_CompleteDSLPckg_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_ValueSpecification)
gen_CompleteDSLPckg_Comment_Element = Generalization(general=Element, specific=CompleteDSLPckg_Comment)
gen_CompleteDSLPckg_Relationship_Element = Generalization(general=Element, specific=CompleteDSLPckg_Relationship)
gen_CompleteDSLPckg_TypedElement_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_TypedElement)
gen_CompleteDSLPckg_Type_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Type)
gen_CompleteDSLPckg_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Expression)
gen_CompleteDSLPckg_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralInteger)
gen_CompleteDSLPckg_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralReal)
gen_CompleteDSLPckg_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralString)
gen_CompleteDSLPckg_LiteralUnilimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralUnilimitedNatural)
gen_CompleteDSLPckg_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_InstanceSpecification)
gen_CompleteDSLPckg_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Constraint)
gen_CompleteDSLPckg_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_OpaqueExpression)
gen_CompleteDSLPckg_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_LiteralSpecification)
gen_CompleteDSLPckg_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralNull)
gen_CompleteDSLPckg_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralBoolean)
gen_CompleteDSLPckg_Slot_Element = Generalization(general=Element, specific=CompleteDSLPckg_Slot)
gen_CompleteDSLPckg_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_RedefinableElement)
gen_CompleteDSLPckg_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Classifier)
gen_CompleteDSLPckg_Classifier_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Classifier)
gen_CompleteDSLPckg_Classifier_Type = Generalization(general=Type, specific=CompleteDSLPckg_Classifier)
gen_CompleteDSLPckg_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Feature)
gen_CompleteDSLPckg_StructuralFeature_Feature = Generalization(general=Feature, specific=CompleteDSLPckg_StructuralFeature)
gen_CompleteDSLPckg_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=CompleteDSLPckg_StructuralFeature)
gen_CompleteDSLPckg_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_StructuralFeature)
gen_CompleteDSLPckg_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=CompleteDSLPckg_Property)
gen_CompleteDSLPckg_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=CompleteDSLPckg_Property)
gen_CompleteDSLPckg_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=CompleteDSLPckg_Property)
gen_CompleteDSLPckg_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CompleteDSLPckg_Operation)
gen_CompleteDSLPckg_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Generalization)
gen_CompleteDSLPckg_BehavioralFeature_Feature = Generalization(general=Feature, specific=CompleteDSLPckg_BehavioralFeature)
gen_CompleteDSLPckg_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_BehavioralFeature)
gen_CompleteDSLPckg_Parameter_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Parameter)
gen_CompleteDSLPckg_Association_Relationship = Generalization(general=Relationship, specific=CompleteDSLPckg_Association)
gen_CompleteDSLPckg_Association_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Association)
gen_CompleteDSLPckg_DataType_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_DataType)
gen_CompleteDSLPckg_PrimitiveType_DataType = Generalization(general=DataType, specific=CompleteDSLPckg_PrimitiveType)
gen_CompleteDSLPckg_Enumeration_DataType = Generalization(general=DataType, specific=CompleteDSLPckg_Enumeration)
gen_CompleteDSLPckg_Class_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Abstraction_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Abstraction)
gen_CompleteDSLPckg_Realization_Abstraction = Generalization(general=Abstraction, specific=CompleteDSLPckg_Realization)
gen_CompleteDSLPckg_Substitution_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_Substitution)
gen_CompleteDSLPckg_Interface_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Interface)
gen_CompleteDSLPckg_InterfaceRealization_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_InterfaceRealization)
gen_CompleteDSLPckg_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=CompleteDSLPckg_EnumerationLiteral)
gen_CompleteDSLPckg_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_PackageMerge)
gen_CompleteDSLPckg_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Dependency)
gen_CompleteDSLPckg_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Dependency)
gen_CompleteDSLPckg_Usage_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Usage)
gen_CompleteDSLPckg_Behavior_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Behavior)
gen_CompleteDSLPckg_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_OpaqueBehavior)
gen_CompleteDSLPckg_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_BehavioredClassifier)
gen_CompleteDSLPckg_AssociationClass_Class = Generalization(general=Class_, specific=CompleteDSLPckg_AssociationClass)
gen_CompleteDSLPckg_AssociationClass_Association = Generalization(general=Association, specific=CompleteDSLPckg_AssociationClass)
gen_CompleteDSLPckg_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_GeneralizationSet)
gen_CompleteDSLPckg_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CompleteDSLPckg_Reception)
gen_CompleteDSLPckg_Trigger_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Trigger)
gen_CompleteDSLPckg_Event_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Event)
gen_CompleteDSLPckg_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=CompleteDSLPckg_FunctionBehavior)
gen_CompleteDSLPckg_Signal_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Signal)
gen_CompleteDSLPckg_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_TimeExpression)
gen_CompleteDSLPckg_Observation_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Observation)
gen_CompleteDSLPckg_TimeObservation_Observation = Generalization(general=Observation, specific=CompleteDSLPckg_TimeObservation)
gen_CompleteDSLPckg_MessageEvent_Event = Generalization(general=Event, specific=CompleteDSLPckg_MessageEvent)
gen_CompleteDSLPckg_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_AnyReceiveEvent)
gen_CompleteDSLPckg_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_SignalEvent)
gen_CompleteDSLPckg_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_CallEvent)
gen_CompleteDSLPckg_ChangeEvent_Event = Generalization(general=Event, specific=CompleteDSLPckg_ChangeEvent)
gen_CompleteDSLPckg_TimeInterval_Interval = Generalization(general=Interval, specific=CompleteDSLPckg_TimeInterval)
gen_CompleteDSLPckg_DurationInterval_Interval = Generalization(general=Interval, specific=CompleteDSLPckg_DurationInterval)
gen_CompleteDSLPckg_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=CompleteDSLPckg_IntervalConstraint)
gen_CompleteDSLPckg_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CompleteDSLPckg_TimeConstraint)
gen_CompleteDSLPckg_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CompleteDSLPckg_DurationConstraint)
gen_CompleteDSLPckg_Component_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Component)
gen_CompleteDSLPckg_DurationObservation_Observation = Generalization(general=Observation, specific=CompleteDSLPckg_DurationObservation)
gen_CompleteDSLPckg_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Duration)
gen_CompleteDSLPckg_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Interval)
gen_CompleteDSLPckg_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ConnectableElement)
gen_CompleteDSLPckg_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_StructuredClassifier)
gen_CompleteDSLPckg_Component_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Component)
gen_CompleteDSLPckg_ComponentRealization_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_ComponentRealization)
gen_CompleteDSLPckg_Connector_Feature = Generalization(general=Feature, specific=CompleteDSLPckg_Connector)
gen_CompleteDSLPckg_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_EncapsulatedClassifier)
gen_CompleteDSLPckg_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_Collaboration)
gen_CompleteDSLPckg_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Collaboration)
gen_CompleteDSLPckg_CollaborationUse_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_CollaborationUse)
gen_CompleteDSLPckg_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Variable_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Port_Property = Generalization(general=Property_, specific=CompleteDSLPckg_Port)
gen_CompleteDSLPckg_Device_Node = Generalization(general=Node, specific=CompleteDSLPckg_Device)
gen_CompleteDSLPckg_ExecutionEnvironment_Node = Generalization(general=Node, specific=CompleteDSLPckg_ExecutionEnvironment)
gen_CompleteDSLPckg_CommunicationPath_Association = Generalization(general=Association, specific=CompleteDSLPckg_CommunicationPath)
gen_CompleteDSLPckg_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_DeploymentTarget)
gen_CompleteDSLPckg_Deployment_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Deployment)
gen_CompleteDSLPckg_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_DeployedArtifact)
gen_CompleteDSLPckg_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=CompleteDSLPckg_DeploymentSpecification)
gen_CompleteDSLPckg_Artifact_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Artifact_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Manifestation_Abstraction = Generalization(general=Abstraction, specific=CompleteDSLPckg_Manifestation)
gen_CompleteDSLPckg_Node_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Node)
gen_CompleteDSLPckg_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=CompleteDSLPckg_Node)
gen_CompleteDSLPckg_InputPin_Pin = Generalization(general=Pin, specific=CompleteDSLPckg_InputPin)
gen_CompleteDSLPckg_OutputPin_Pin = Generalization(general=Pin, specific=CompleteDSLPckg_OutputPin)
gen_CompleteDSLPckg_Pin_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Pin)
gen_CompleteDSLPckg_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=CompleteDSLPckg_Pin)
gen_CompleteDSLPckg_ValuePin_InputPin = Generalization(general=InputPin, specific=CompleteDSLPckg_ValuePin)
gen_CompleteDSLPckg_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_CallAction)
gen_CompleteDSLPckg_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=CompleteDSLPckg_CallBehaviorAction)
gen_CompleteDSLPckg_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_SendSignalAction)
gen_CompleteDSLPckg_Action_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Action)
gen_CompleteDSLPckg_OpaqueAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_OpaqueAction)
gen_CompleteDSLPckg_DestroyObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_DestroyObjectAction)
gen_CompleteDSLPckg_TestIdentityAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_TestIdentityAction)
gen_CompleteDSLPckg_ReadSelfAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadSelfAction)
gen_CompleteDSLPckg_ValueSpecificationAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ValueSpecificationAction)
gen_CompleteDSLPckg_StructuralFeatureAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_StructuralFeatureAction)
gen_CompleteDSLPckg_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_BroadcastSignalAction)
gen_CompleteDSLPckg_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_SendObjectAction)
gen_CompleteDSLPckg_CreateObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_CreateObjectAction)
gen_CompleteDSLPckg_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_ClearStructuralFeatureAction)
gen_CompleteDSLPckg_LinkAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_LinkAction)
gen_CompleteDSLPckg_LinkEndData_Element = Generalization(general=Element, specific=CompleteDSLPckg_LinkEndData)
gen_CompleteDSLPckg_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=CompleteDSLPckg_ReadLinkAction)
gen_CompleteDSLPckg_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_ReadStructuralFeatureAction)
gen_CompleteDSLPckg_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_WriteStructuralFeatureAction)
gen_CompleteDSLPckg_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=CompleteDSLPckg_AddStructuralFeatureValueAction)
gen_CompleteDSLPckg_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=CompleteDSLPckg_RemoveStructuralFeatureValueAction)
gen_CompleteDSLPckg_UnmarshallAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_UnmarshallAction)
gen_CompleteDSLPckg_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=CompleteDSLPckg_WriteLinkAction)
gen_CompleteDSLPckg_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=CompleteDSLPckg_CreateLinkAction)
gen_CompleteDSLPckg_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=CompleteDSLPckg_LinkEndCreationData)
gen_CompleteDSLPckg_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=CompleteDSLPckg_DestroyLinkAction)
gen_CompleteDSLPckg_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=CompleteDSLPckg_LinkEndDestructionData)
gen_CompleteDSLPckg_ReplyAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReplyAction)
gen_CompleteDSLPckg_ReclassifyObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReclassifyObjectAction)
gen_CompleteDSLPckg_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_StartClassifierBehaviorAction)
gen_CompleteDSLPckg_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=CompleteDSLPckg_StartObjectBehaviorAction)
gen_CompleteDSLPckg_AcceptEventAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_AcceptEventAction)
gen_CompleteDSLPckg_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=CompleteDSLPckg_AcceptCallAction)
gen_CompleteDSLPckg_ReadExtendAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadExtendAction)
gen_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadLinkObjectEndQualifierAction)
gen_CompleteDSLPckg_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=CompleteDSLPckg_CreateLinkObjectAction)
gen_CompleteDSLPckg_ReduceAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReduceAction)
gen_CompleteDSLPckg_QualifierValue_Element = Generalization(general=Element, specific=CompleteDSLPckg_QualifierValue)
gen_CompleteDSLPckg_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadLinkObjectEndAction)
gen_CompleteDSLPckg_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=CompleteDSLPckg_AddVariableValueAction)
gen_CompleteDSLPckg_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=CompleteDSLPckg_RemoveVariableValueAction)
gen_CompleteDSLPckg_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_ClearVariableAction)
gen_CompleteDSLPckg_RaiseExceptionAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_RaiseExceptionAction)
gen_CompleteDSLPckg_ActionInputPin_InputPin = Generalization(general=InputPin, specific=CompleteDSLPckg_ActionInputPin)
gen_CompleteDSLPckg_StateMachine_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_StateMachine)
gen_CompleteDSLPckg_VariableAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_VariableAction)
gen_CompleteDSLPckg_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_ReadVariableAction)
gen_CompleteDSLPckg_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_WriteVariableAction)
gen_CompleteDSLPckg_Transition_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Transition)
gen_CompleteDSLPckg_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Transition)
gen_CompleteDSLPckg_Region_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Region)
gen_CompleteDSLPckg_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Region)
gen_CompleteDSLPckg_Vertex_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Vertex)
gen_CompleteDSLPckg_Pseudostate_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_Pseudostate)
gen_CompleteDSLPckg_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_ConnectionPointReference)
gen_CompleteDSLPckg_State_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_State_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_State_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_Activity_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_Activity)
gen_CompleteDSLPckg_FinalState_State = Generalization(general=State, specific=CompleteDSLPckg_FinalState)
gen_CompleteDSLPckg_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=CompleteDSLPckg_ProtocolStateMachine)
gen_CompleteDSLPckg_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_ProtocolConformance)
gen_CompleteDSLPckg_ProtocolTransition_Transition = Generalization(general=Transition, specific=CompleteDSLPckg_ProtocolTransition)
gen_CompleteDSLPckg_ActivityGroup_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ActivityGroup)
gen_CompleteDSLPckg_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ActivityNode)
gen_CompleteDSLPckg_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ActivityNode)
gen_CompleteDSLPckg_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=CompleteDSLPckg_ControlFlow)
gen_CompleteDSLPckg_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=CompleteDSLPckg_ObjectFlow)
gen_CompleteDSLPckg_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ObjectNode)
gen_CompleteDSLPckg_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ObjectNode)
gen_CompleteDSLPckg_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_ActivityParameterNode)
gen_CompleteDSLPckg_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ControlNode)
gen_CompleteDSLPckg_ActivityFinalNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_ActivityFinalNode)
gen_CompleteDSLPckg_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=CompleteDSLPckg_ActivityFinalNode)
gen_CompleteDSLPckg_InitialNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_InitialNode)
gen_CompleteDSLPckg_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ActivityEdge)
gen_CompleteDSLPckg_ForkNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_ForkNode)
gen_CompleteDSLPckg_JoinNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_JoinNode)
gen_CompleteDSLPckg_MergeNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_MergeNode)
gen_CompleteDSLPckg_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_DecisionNode)
gen_CompleteDSLPckg_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_ActivityPartition)
gen_CompleteDSLPckg_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_CentralBufferNode)
gen_CompleteDSLPckg_FinalNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_FinalNode)
gen_CompleteDSLPckg_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=CompleteDSLPckg_FlowFinalNode)
gen_CompleteDSLPckg_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_ExecutableNode = Generalization(general=ExecutableNode, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_Action = Generalization(general=Action, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=CompleteDSLPckg_DataStoreNode)
gen_CompleteDSLPckg_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ParameterSet)
gen_CompleteDSLPckg_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_InterruptibleActivityRegion)
gen_CompleteDSLPckg_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_ConditionalNode)
gen_CompleteDSLPckg_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ExecutableNode)
gen_CompleteDSLPckg_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_LoopNode)
gen_CompleteDSLPckg_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_ExpansionRegion)
gen_CompleteDSLPckg_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_ExpansionNode)
gen_CompleteDSLPckg_Clause_Element = Generalization(general=Element, specific=CompleteDSLPckg_Clause)
gen_CompleteDSLPckg_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_SequenceNode)
gen_CompleteDSLPckg_ExceptionHandler_Element = Generalization(general=Element, specific=CompleteDSLPckg_ExceptionHandler)
gen_CompleteDSLPckg_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_StateInvariant)
gen_CompleteDSLPckg_Interaction_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_Interaction)
gen_CompleteDSLPckg_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_Interaction)
gen_CompleteDSLPckg_Lifeline_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Lifeline)
gen_CompleteDSLPckg_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_InteractionFragment)
gen_CompleteDSLPckg_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_ExecutionSpecification)
gen_CompleteDSLPckg_OccurenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_OccurenceSpecification)
gen_CompleteDSLPckg_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_MessageEnd)
gen_CompleteDSLPckg_ExecutionOccurrenceSpecification_OccurenceSpecification = Generalization(general=OccurenceSpecification, specific=CompleteDSLPckg_ExecutionOccurrenceSpecification)
gen_CompleteDSLPckg_Message_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Message)
gen_CompleteDSLPckg_ConsiderIgnoreFragment_CombinedFragment = Generalization(general=CombinedFragment, specific=CompleteDSLPckg_ConsiderIgnoreFragment)
gen_CompleteDSLPckg_MessageOccurrenceSpecification_OccurenceSpecification = Generalization(general=OccurenceSpecification, specific=CompleteDSLPckg_MessageOccurrenceSpecification)
gen_CompleteDSLPckg_DestructionOccurrenceSpecification_MessageOccurrenceSpecification = Generalization(general=MessageOccurrenceSpecification, specific=CompleteDSLPckg_DestructionOccurrenceSpecification)
gen_CompleteDSLPckg_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=CompleteDSLPckg_BehaviorExecutionSpecification)
gen_CompleteDSLPckg_ActionExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=CompleteDSLPckg_ActionExecutionSpecification)
gen_CompleteDSLPckg_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_GeneralOrdering)
gen_CompleteDSLPckg_InteractionOperand_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_InteractionOperand)
gen_CompleteDSLPckg_PartDecomposition_InteractionUse = Generalization(general=InteractionUse, specific=CompleteDSLPckg_PartDecomposition)
gen_CompleteDSLPckg_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Actor)
gen_CompleteDSLPckg_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_UseCase)
gen_CompleteDSLPckg_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_Continuation)
gen_CompleteDSLPckg_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=CompleteDSLPckg_InteractionConstraint)
gen_CompleteDSLPckg_Gate_MessageEnd = Generalization(general=MessageEnd, specific=CompleteDSLPckg_Gate)
gen_CompleteDSLPckg_InteractionUse_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_InteractionUse)
gen_CompleteDSLPckg_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Include)
gen_CompleteDSLPckg_Include_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Include)
gen_CompleteDSLPckg_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ExtensionPoint)
gen_CompleteDSLPckg_Extend_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Extend)
gen_CompleteDSLPckg_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Extend)

# Domain Model
domain_model = DomainModel(
    name="CompleteDSLPckg",
    types={CompleteDSLPckg_Element, CompleteDSLPckg_Comment, CompleteDSLPckg_NamedElement, Element, CompleteDSLPckg_Namespace, CompleteDSLPckg_Constraint, DirectedRelationship, CompleteDSLPckg_Package, Namespace, PackageableElement, CompleteDSLPckg_Dependency, NamedElement, CompleteDSLPckg_PackageableElement, CompleteDSLPckg_ElementImport, CompleteDSLPckg_PackageImport, CompleteDSLPckg_DirectedRelationship, Relationship, CompleteDSLPckg_MultiplicityElement, CompleteDSLPckg_ValueSpecification, TypedElement, CompleteDSLPckg_Type, CompleteDSLPckg_PackageMerge, CompleteDSLPckg_Relationship, CompleteDSLPckg_InstanceSpecification, CompleteDSLPckg_TypedElement, CompleteDSLPckg_Expression, ValueSpecification, CompleteDSLPckg_Slot, CompleteDSLPckg_LiteralInteger, CompleteDSLPckg_LiteralReal, CompleteDSLPckg_LiteralString, CompleteDSLPckg_LiteralUnilimitedNatural, CompleteDSLPckg_InstanceValue, CompleteDSLPckg_Classifier, CompleteDSLPckg_OpaqueExpression, CompleteDSLPckg_Parameter, CompleteDSLPckg_Behavior, CompleteDSLPckg_LiteralSpecification, CompleteDSLPckg_LiteralNull, LiteralSpecification, CompleteDSLPckg_LiteralBoolean, CompleteDSLPckg_Feature, CompleteDSLPckg_Property, CompleteDSLPckg_Generalization, CompleteDSLPckg_Substitution, CompleteDSLPckg_GeneralizationSet, CompleteDSLPckg_StructuralFeature, CompleteDSLPckg_RedefinableElement, RedefinableElement, Type, CompleteDSLPckg_Class, CompleteDSLPckg_Association, CompleteDSLPckg_DataType, CompleteDSLPckg_Interface, CompleteDSLPckg_CollaborationUse, Feature, MultiplicityElement, StructuralFeature, ConnectableElement, DeploymentTarget, CompleteDSLPckg_Operation, BehavioralFeature, CompleteDSLPckg_BehavioralFeature, CompleteDSLPckg_PrimitiveType, DataType, CompleteDSLPckg_Enumeration, CompleteDSLPckg_EnumerationLiteral, Classifier, BehavioredClassifier, StructuredClassifier, EncapsulatedClassifier, CompleteDSLPckg_Reception, CompleteDSLPckg_Realization, Abstraction, Realization, CompleteDSLPckg_InterfaceRealization, InstanceSpecification, CompleteDSLPckg_Usage, Dependency, CompleteDSLPckg_Abstraction, CompleteDSLPckg_OpaqueBehavior, Behavior, CompleteDSLPckg_BehavioredClassifier, CompleteDSLPckg_AssociationClass, Class_, Association, CompleteDSLPckg_Trigger, CompleteDSLPckg_Event, CompleteDSLPckg_FunctionBehavior, OpaqueBehavior, CompleteDSLPckg_Signal, CompleteDSLPckg_TimeEvent, CompleteDSLPckg_TimeExpression, CompleteDSLPckg_Observation, CompleteDSLPckg_TimeObservation, Observation, CompleteDSLPckg_MessageEvent, Event, CompleteDSLPckg_AnyReceiveEvent, MessageEvent, CompleteDSLPckg_SignalEvent, CompleteDSLPckg_CallEvent, CompleteDSLPckg_ChangeEvent, CompleteDSLPckg_TimeInterval, Interval, CompleteDSLPckg_DurationInterval, CompleteDSLPckg_IntervalConstraint, Constraint, CompleteDSLPckg_TimeConstraint, IntervalConstraint, CompleteDSLPckg_DurationConstraint, CompleteDSLPckg_Component, CompleteDSLPckg_DurationObservation, CompleteDSLPckg_Duration, CompleteDSLPckg_Interval, CompleteDSLPckg_ConnectorEnd, CompleteDSLPckg_ConnectableElement, CompleteDSLPckg_StructuredClassifier, CompleteDSLPckg_ComponentRealization, CompleteDSLPckg_Connector, CompleteDSLPckg_EncapsulatedClassifier, CompleteDSLPckg_Collaboration, CompleteDSLPckg_InvocationAction, CompleteDSLPckg_Variable, CompleteDSLPckg_Port, Property_, CompleteDSLPckg_Device, Node, CompleteDSLPckg_ExecutionEnvironment, CompleteDSLPckg_CommunicationPath, CompleteDSLPckg_DeploymentTarget, CompleteDSLPckg_Deployment, CompleteDSLPckg_DeployedArtifact, CompleteDSLPckg_DeploymentSpecification, Artifact, CompleteDSLPckg_Artifact, DeployedArtifact, CompleteDSLPckg_Manifestation, CompleteDSLPckg_Node, Pin, CompleteDSLPckg_Pin, CompleteDSLPckg_ValuePin, InputPin, CompleteDSLPckg_CallAction, InvocationAction, CompleteDSLPckg_CallBehaviorAction, CallAction, CompleteDSLPckg_CallOperationAction, CompleteDSLPckg_SendSignalAction, CompleteDSLPckg_Action, CompleteDSLPckg_InputPin, CompleteDSLPckg_OutputPin, CompleteDSLPckg_OpaqueAction, Action, CompleteDSLPckg_DestroyObjectAction, CompleteDSLPckg_TestIdentityAction, CompleteDSLPckg_ReadSelfAction, CompleteDSLPckg_ValueSpecificationAction, CompleteDSLPckg_StructuralFeatureAction, CompleteDSLPckg_BroadcastSignalAction, CompleteDSLPckg_SendObjectAction, CompleteDSLPckg_CreateObjectAction, CompleteDSLPckg_ClearStructuralFeatureAction, CompleteDSLPckg_LinkAction, CompleteDSLPckg_LinkEndData, CompleteDSLPckg_QualifierValue, CompleteDSLPckg_ReadLinkAction, LinkAction, CompleteDSLPckg_ReadStructuralFeatureAction, StructuralFeatureAction, CompleteDSLPckg_WriteStructuralFeatureAction, CompleteDSLPckg_AddStructuralFeatureValueAction, WriteStructuralFeatureAction, CompleteDSLPckg_RemoveStructuralFeatureValueAction, CompleteDSLPckg_UnmarshallAction, CompleteDSLPckg_WriteLinkAction, CompleteDSLPckg_CreateLinkAction, WriteLinkAction, CompleteDSLPckg_LinkEndCreationData, LinkEndData, CompleteDSLPckg_DestroyLinkAction, CompleteDSLPckg_LinkEndDestructionData, CompleteDSLPckg_ReplyAction, CompleteDSLPckg_ReclassifyObjectAction, CompleteDSLPckg_ReadlsClassifiedObjectAction, CompleteDSLPckg_StartClassifierBehaviorAction, CompleteDSLPckg_StartObjectBehaviorAction, CompleteDSLPckg_AcceptEventAction, CompleteDSLPckg_AcceptCallAction, AcceptEventAction, CompleteDSLPckg_ReadExtendAction, CompleteDSLPckg_ReadLinkObjectEndQualifierAction, CompleteDSLPckg_CreateLinkObjectAction, CreateLinkAction, CompleteDSLPckg_ReduceAction, CompleteDSLPckg_ReadLinkObjectEndAction, CompleteDSLPckg_AddVariableValueAction, WriteVariableAction, CompleteDSLPckg_RemoveVariableValueAction, CompleteDSLPckg_ClearVariableAction, CompleteDSLPckg_RaiseExceptionAction, CompleteDSLPckg_ActionInputPin, CompleteDSLPckg_StateMachine, CompleteDSLPckg_Region, CompleteDSLPckg_Pseudostate, CompleteDSLPckg_State, CompleteDSLPckg_VariableAction, CompleteDSLPckg_ReadVariableAction, VariableAction, CompleteDSLPckg_WriteVariableAction, CompleteDSLPckg_Vertex, CompleteDSLPckg_Transition, Vertex, CompleteDSLPckg_ConnectionPointReference, CompleteDSLPckg_Activity, CompleteDSLPckg_ActivityNode, CompleteDSLPckg_ActivityGroup, CompleteDSLPckg_ActivityEdge, CompleteDSLPckg_ActivityPartition, CompleteDSLPckg_StructuredActivityNode, CompleteDSLPckg_FinalState, State, CompleteDSLPckg_ProtocolStateMachine, StateMachine, CompleteDSLPckg_ProtocolConformance, CompleteDSLPckg_ProtocolTransition, Transition, CompleteDSLPckg_InterruptibleActivityRegion, CompleteDSLPckg_ControlFlow, ActivityEdge, CompleteDSLPckg_ObjectFlow, CompleteDSLPckg_ObjectNode, ActivityNode, CompleteDSLPckg_ActivityParameterNode, ObjectNode, CompleteDSLPckg_ControlNode, CompleteDSLPckg_ActivityFinalNode, ControlNode, FinalNode, CompleteDSLPckg_InitialNode, CompleteDSLPckg_ForkNode, CompleteDSLPckg_JoinNode, CompleteDSLPckg_MergeNode, CompleteDSLPckg_DecisionNode, ActivityGroup, CompleteDSLPckg_CentralBufferNode, CompleteDSLPckg_FinalNode, CompleteDSLPckg_FlowFinalNode, ExecutableNode, CompleteDSLPckg_DataStoreNode, CentralBufferNode, CompleteDSLPckg_ParameterSet, CompleteDSLPckg_ConditionalNode, CompleteDSLPckg_Clause, CompleteDSLPckg_ExecutableNode, CompleteDSLPckg_ExceptionHandler, CompleteDSLPckg_LoopNode, StructuredActivityNode, CompleteDSLPckg_ExpansionRegion, CompleteDSLPckg_ExpansionNode, CompleteDSLPckg_SequenceNode, CompleteDSLPckg_StateInvariant, CompleteDSLPckg_Interaction, CompleteDSLPckg_Gate, CompleteDSLPckg_InteractionFragment, CompleteDSLPckg_Lifeline, CompleteDSLPckg_GeneralOrdering, CompleteDSLPckg_InteractionOperand, CompleteDSLPckg_ExecutionSpecification, InteractionFragment, CompleteDSLPckg_OccurenceSpecification, CompleteDSLPckg_MessageEnd, CompleteDSLPckg_ExecutionOccurrenceSpecification, OccurenceSpecification, CompleteDSLPckg_PartDecomposition, CompleteDSLPckg_Message, CompleteDSLPckg_InteractionConstraint, CompleteDSLPckg_CombinedFragment, CompleteDSLPckg_ConsiderIgnoreFragment, CombinedFragment, CompleteDSLPckg_MessageOccurrenceSpecification, CompleteDSLPckg_DestructionOccurrenceSpecification, MessageOccurrenceSpecification, CompleteDSLPckg_BehaviorExecutionSpecification, ExecutionSpecification, CompleteDSLPckg_ActionExecutionSpecification, InteractionUse, CompleteDSLPckg_Actor, CompleteDSLPckg_UseCase, CompleteDSLPckg_ExtensionPoint, CompleteDSLPckg_Extend, CompleteDSLPckg_Include, CompleteDSLPckg_Continuation, MessageEnd, CompleteDSLPckg_InteractionUse, VisibilityKind, AggregationKind, CallConcurrencyFeature, ConnectorKind, TransitionKind, ObjectNodeOrderingKind, ParameterEffectKind, ExpansionKind, MessageKind, MessageSort, InteractionOperandKind},
    associations={ownedComment0, ownedElement3, owner7, namespace10, ownedRule28, importedElement31, importingNamespace33, importedPackage36, importingNamespace37, nestedPackage41, clientDependency13, importedMember16, member17, ownedMember19, elementImport22, packageImport25, target63, source65, upperValue68, lowerValue71, owningUpper74, owningLower77, owningConstraint80, nestingPackage45, packagedElement48, ownedType51, packageMerge54, owningElement57, annotatedElement60, relatedElement61, owningInstanceSpec86, type89, package90, owningSlot83, instance97, slot98, specification101, classifier104, context106, constrainedElement109, operand93, result94, behavior95, inheritedMember126, feature129, attribute132, redefinedClassifier135, general138, generalization140, substitution143, powertypeExtent146, specification111, owningInstace114, value117, definingFeature120, redefinedElement122, redefinitionContext123, class157, redefinedProperty161, defaultValue163, opposite167, subsettedProperty170, association172, owningAssociation175, dataType178, interface181, collaborationUse149, representation151, featuringClassifier154, ownedFormalParam205, defaultValue208, type211, precondition213, bodyCondition216, postcondition219, class222, qualifier185, associationEnd189, general192, specific194, generalizationSet197, ownedParameter200, raisedException202, navigableOwnedEnd244, memberEnd246, ownedEnd249, ownedAttribute252, ownedOperation255, ownedLiteral258, dataType225, interface228, nestedClassifier231, ownedOperation233, superClass237, ownedAttribute239, ownedReception242, mapping274, substitutingClassifier276, contract279, nestedClassifier281, redefinedInterface284, ownedAttribute286, ownedOperation289, ownedReception292, enumeration261, receivingPackage264, mergedPackage267, client269, supplier272, generalization311, context314, redefinedBehavior318, specification320, ownedParameter323, precondition326, postcondition329, implementingClassifier295, contract298, interfaceRealization300, ownedBehavior303, classifierBehavior305, powertype308, ownedAttribute332, signal334, event337, changeExpression342, when344, expr345, observation348, signal338, operation340, timeMax364, timeMin366, durationMax369, durationMin371, timeSpecification374, durationSpecification376, event350, event352, expr354, observation356, max359, min361, end394, contract395, redefinedConnector399, partWithPort401, role404, type406, definingEnd409, end412, required378, provided380, realization383, packagedElement385, abstraction388, realizingClassifier391, provided428, redefinedPort432, ownedPort434, collaborationRole436, type438, roleBinding441, onPort444, ownedConnector415, role417, structuredOwnedAttribute420, part423, required426, nestedNode460, deployedElement461, deployment463, location465, deployedArtifact468, configuration470, ownedOperation446, ownedAttribute448, nestedArtifact452, manifestation454, utilizedElement456, outputValue483, value486, result488, behavior490, operation492, target494, deployment472, context475, input477, output479, inputValue481, target514, result516, first518, second521, result524, result526, value528, target497, signal499, signal502, target504, request506, classifier509, result511, removeAt545, result547, inputValue549, endData551, value553, end556, qualifier559, result561, structuralFeature531, object533, result536, value538, result540, insertAt543, replyValue569, replyToCall572, object575, unmarshallType577, result580, insertAt563, destroyAt565, returnInformation567, object595, oldClassifier597, newClassifier600, result603, object605, object608, result583, trigger585, returnInformation588, result590, classifier592, object626, result628, qualifier631, result634, result636, collection638, object610, qualifier612, value615, end618, object620, result623, insertAt649, removeAt651, exception653, fromAction655, region657, connectionPoint658, reducer641, variable644, result645, value647, incoming681, container684, source687, target690, effect693, trigger696, guard699, container702, submachineState660, extendedStateMachine663, subvertex665, stateMachine667, transition670, state672, extendedRegion676, outgoing678, connection719, connectionPoint722, submachine725, region728, deferrableTrigger731, exit734, doActivity737, entry740, redefinedTransition706, state708, exit711, entry713, state716, preCondition756, postCondition758, referred761, node764, group765, edge767, partition769, stateInvariant743, redefinedState747, conformance749, specificMachine750, generalMachine753, redefinedNode780, incoming782, outgoing785, inPartition788, inInterruptibleRegion791, inStructuredNode793, subgroup797, superGroup800, inActivity802, structuredNode771, variable773, inGroup776, source816, redefinedEdge820, inGroup822, guard825, inPartition828, weight831, interrupts834, inStructuredNode837, containedNode805, containedEdge808, parameter811, target813, joinSpec848, decisionInputFlow850, decisionInput852, edge855, subpartition859, superPartition862, transformation840, selection842, inState845, node878, activity881, variable884, node887, structuredNodeInput890, edge893, represents864, node867, parameter870, condition872, interruptingEdge875, loopVariableInput911, loopVariable914, bodyOutput917, result920, clause923, test924, body927, structuredNodeOutput896, handler899, setupPart900, bodyPart902, test905, decider908, protectedNode947, exceptionInput950, exceptionType952, inputElement955, outputElement956, regionAsInput959, result930, predecessorClause934, sucessorClause937, decider939, executableNode942, handlerBody944, toBefore974, toAfter977, invariant980, fragment982, lifeline984, action987, formalGate990, regionAsOutput962, covered965, generalOrdering966, enclosingOperand968, start970, finish971, signature1011, sendEvent1014, receiveEvent1016, message1019, coveredBy992, interaction995, represents998, selector1001, decomposedAs1004, argument1006, connector1008, fragment1034, guard1037, operand1039, cfragmentGate1041, execution1022, behavior1024, action1026, after1028, before1031, returnValue1057, returnValueRecipient1060, refersTo1063, subject1066, extensionPoint1068, extend1070, include1072, message1044, maxint1046, minint1049, actualGate1052, argument1054, includingCase1089, addition1092, useCase1074, extensionLocation1077, extension1080, condition1083, extendedCase1086},
    generalizations={gen_CompleteDSLPckg_NamedElement_Element, gen_CompleteDSLPckg_PackageableElement_NamedElement, gen_CompleteDSLPckg_ElementImport_DirectedRelationship, gen_CompleteDSLPckg_PackageImport_DirectedRelationship, gen_CompleteDSLPckg_Package_Namespace, gen_CompleteDSLPckg_Package_PackageableElement, gen_CompleteDSLPckg_Namespace_NamedElement, gen_CompleteDSLPckg_DirectedRelationship_Relationship, gen_CompleteDSLPckg_MultiplicityElement_Element, gen_CompleteDSLPckg_ValueSpecification_TypedElement, gen_CompleteDSLPckg_ValueSpecification_PackageableElement, gen_CompleteDSLPckg_Comment_Element, gen_CompleteDSLPckg_Relationship_Element, gen_CompleteDSLPckg_TypedElement_NamedElement, gen_CompleteDSLPckg_Type_PackageableElement, gen_CompleteDSLPckg_Expression_ValueSpecification, gen_CompleteDSLPckg_LiteralInteger_LiteralSpecification, gen_CompleteDSLPckg_LiteralReal_LiteralSpecification, gen_CompleteDSLPckg_LiteralString_LiteralSpecification, gen_CompleteDSLPckg_LiteralUnilimitedNatural_LiteralSpecification, gen_CompleteDSLPckg_InstanceSpecification_PackageableElement, gen_CompleteDSLPckg_Constraint_PackageableElement, gen_CompleteDSLPckg_OpaqueExpression_ValueSpecification, gen_CompleteDSLPckg_LiteralSpecification_ValueSpecification, gen_CompleteDSLPckg_LiteralNull_LiteralSpecification, gen_CompleteDSLPckg_LiteralBoolean_LiteralSpecification, gen_CompleteDSLPckg_Slot_Element, gen_CompleteDSLPckg_RedefinableElement_NamedElement, gen_CompleteDSLPckg_Classifier_RedefinableElement, gen_CompleteDSLPckg_Classifier_Namespace, gen_CompleteDSLPckg_Classifier_Type, gen_CompleteDSLPckg_Feature_RedefinableElement, gen_CompleteDSLPckg_StructuralFeature_Feature, gen_CompleteDSLPckg_StructuralFeature_MultiplicityElement, gen_CompleteDSLPckg_StructuralFeature_TypedElement, gen_CompleteDSLPckg_Property_StructuralFeature, gen_CompleteDSLPckg_Property_ConnectableElement, gen_CompleteDSLPckg_Property_DeploymentTarget, gen_CompleteDSLPckg_Operation_BehavioralFeature, gen_CompleteDSLPckg_Generalization_DirectedRelationship, gen_CompleteDSLPckg_BehavioralFeature_Feature, gen_CompleteDSLPckg_BehavioralFeature_Namespace, gen_CompleteDSLPckg_Parameter_TypedElement, gen_CompleteDSLPckg_Association_Relationship, gen_CompleteDSLPckg_Association_Classifier, gen_CompleteDSLPckg_DataType_Classifier, gen_CompleteDSLPckg_PrimitiveType_DataType, gen_CompleteDSLPckg_Enumeration_DataType, gen_CompleteDSLPckg_Class_Classifier, gen_CompleteDSLPckg_Class_BehavioredClassifier, gen_CompleteDSLPckg_Class_StructuredClassifier, gen_CompleteDSLPckg_Class_EncapsulatedClassifier, gen_CompleteDSLPckg_Abstraction_Dependency, gen_CompleteDSLPckg_Realization_Abstraction, gen_CompleteDSLPckg_Substitution_Realization, gen_CompleteDSLPckg_Interface_Classifier, gen_CompleteDSLPckg_InterfaceRealization_Realization, gen_CompleteDSLPckg_EnumerationLiteral_InstanceSpecification, gen_CompleteDSLPckg_PackageMerge_DirectedRelationship, gen_CompleteDSLPckg_Dependency_PackageableElement, gen_CompleteDSLPckg_Dependency_DirectedRelationship, gen_CompleteDSLPckg_Usage_Dependency, gen_CompleteDSLPckg_Behavior_Class, gen_CompleteDSLPckg_OpaqueBehavior_Behavior, gen_CompleteDSLPckg_BehavioredClassifier_Classifier, gen_CompleteDSLPckg_AssociationClass_Class, gen_CompleteDSLPckg_AssociationClass_Association, gen_CompleteDSLPckg_GeneralizationSet_PackageableElement, gen_CompleteDSLPckg_Reception_BehavioralFeature, gen_CompleteDSLPckg_Trigger_NamedElement, gen_CompleteDSLPckg_Event_PackageableElement, gen_CompleteDSLPckg_FunctionBehavior_OpaqueBehavior, gen_CompleteDSLPckg_Signal_Classifier, gen_CompleteDSLPckg_TimeExpression_ValueSpecification, gen_CompleteDSLPckg_Observation_PackageableElement, gen_CompleteDSLPckg_TimeObservation_Observation, gen_CompleteDSLPckg_MessageEvent_Event, gen_CompleteDSLPckg_AnyReceiveEvent_MessageEvent, gen_CompleteDSLPckg_SignalEvent_MessageEvent, gen_CompleteDSLPckg_CallEvent_MessageEvent, gen_CompleteDSLPckg_ChangeEvent_Event, gen_CompleteDSLPckg_TimeInterval_Interval, gen_CompleteDSLPckg_DurationInterval_Interval, gen_CompleteDSLPckg_IntervalConstraint_Constraint, gen_CompleteDSLPckg_TimeConstraint_IntervalConstraint, gen_CompleteDSLPckg_DurationConstraint_IntervalConstraint, gen_CompleteDSLPckg_Component_Class, gen_CompleteDSLPckg_DurationObservation_Observation, gen_CompleteDSLPckg_Duration_ValueSpecification, gen_CompleteDSLPckg_Interval_ValueSpecification, gen_CompleteDSLPckg_ConnectableElement_TypedElement, gen_CompleteDSLPckg_StructuredClassifier_Classifier, gen_CompleteDSLPckg_Component_NamedElement, gen_CompleteDSLPckg_ComponentRealization_Realization, gen_CompleteDSLPckg_Connector_Feature, gen_CompleteDSLPckg_EncapsulatedClassifier_StructuredClassifier, gen_CompleteDSLPckg_Collaboration_StructuredClassifier, gen_CompleteDSLPckg_Collaboration_BehavioredClassifier, gen_CompleteDSLPckg_CollaborationUse_NamedElement, gen_CompleteDSLPckg_Variable_ConnectableElement, gen_CompleteDSLPckg_Variable_MultiplicityElement, gen_CompleteDSLPckg_Variable_TypedElement, gen_CompleteDSLPckg_Port_Property, gen_CompleteDSLPckg_Device_Node, gen_CompleteDSLPckg_ExecutionEnvironment_Node, gen_CompleteDSLPckg_CommunicationPath_Association, gen_CompleteDSLPckg_DeploymentTarget_NamedElement, gen_CompleteDSLPckg_Deployment_Dependency, gen_CompleteDSLPckg_DeployedArtifact_NamedElement, gen_CompleteDSLPckg_DeploymentSpecification_Artifact, gen_CompleteDSLPckg_Artifact_Classifier, gen_CompleteDSLPckg_Artifact_NamedElement, gen_CompleteDSLPckg_Artifact_DeployedArtifact, gen_CompleteDSLPckg_Manifestation_Abstraction, gen_CompleteDSLPckg_Node_Class, gen_CompleteDSLPckg_Node_DeploymentTarget, gen_CompleteDSLPckg_InputPin_Pin, gen_CompleteDSLPckg_OutputPin_Pin, gen_CompleteDSLPckg_Pin_TypedElement, gen_CompleteDSLPckg_Pin_MultiplicityElement, gen_CompleteDSLPckg_ValuePin_InputPin, gen_CompleteDSLPckg_CallAction_InvocationAction, gen_CompleteDSLPckg_CallBehaviorAction_CallAction, gen_CompleteDSLPckg_SendSignalAction_InvocationAction, gen_CompleteDSLPckg_Action_NamedElement, gen_CompleteDSLPckg_OpaqueAction_Action, gen_CompleteDSLPckg_DestroyObjectAction_Action, gen_CompleteDSLPckg_TestIdentityAction_Action, gen_CompleteDSLPckg_ReadSelfAction_Action, gen_CompleteDSLPckg_ValueSpecificationAction_Action, gen_CompleteDSLPckg_StructuralFeatureAction_Action, gen_CompleteDSLPckg_BroadcastSignalAction_InvocationAction, gen_CompleteDSLPckg_SendObjectAction_InvocationAction, gen_CompleteDSLPckg_CreateObjectAction_Action, gen_CompleteDSLPckg_ClearStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_LinkAction_Action, gen_CompleteDSLPckg_LinkEndData_Element, gen_CompleteDSLPckg_ReadLinkAction_LinkAction, gen_CompleteDSLPckg_ReadStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_WriteStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_CompleteDSLPckg_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_CompleteDSLPckg_UnmarshallAction_Action, gen_CompleteDSLPckg_WriteLinkAction_LinkAction, gen_CompleteDSLPckg_CreateLinkAction_WriteLinkAction, gen_CompleteDSLPckg_LinkEndCreationData_LinkEndData, gen_CompleteDSLPckg_DestroyLinkAction_WriteLinkAction, gen_CompleteDSLPckg_LinkEndDestructionData_LinkEndData, gen_CompleteDSLPckg_ReplyAction_Action, gen_CompleteDSLPckg_ReclassifyObjectAction_Action, gen_CompleteDSLPckg_StartClassifierBehaviorAction_Action, gen_CompleteDSLPckg_StartObjectBehaviorAction_CallAction, gen_CompleteDSLPckg_AcceptEventAction_Action, gen_CompleteDSLPckg_AcceptCallAction_AcceptEventAction, gen_CompleteDSLPckg_ReadExtendAction_Action, gen_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_Action, gen_CompleteDSLPckg_CreateLinkObjectAction_CreateLinkAction, gen_CompleteDSLPckg_ReduceAction_Action, gen_CompleteDSLPckg_QualifierValue_Element, gen_CompleteDSLPckg_ReadLinkObjectEndAction_Action, gen_CompleteDSLPckg_AddVariableValueAction_WriteVariableAction, gen_CompleteDSLPckg_RemoveVariableValueAction_WriteVariableAction, gen_CompleteDSLPckg_ClearVariableAction_VariableAction, gen_CompleteDSLPckg_RaiseExceptionAction_Action, gen_CompleteDSLPckg_ActionInputPin_InputPin, gen_CompleteDSLPckg_StateMachine_Behavior, gen_CompleteDSLPckg_VariableAction_Action, gen_CompleteDSLPckg_ReadVariableAction_VariableAction, gen_CompleteDSLPckg_WriteVariableAction_VariableAction, gen_CompleteDSLPckg_Transition_Namespace, gen_CompleteDSLPckg_Transition_RedefinableElement, gen_CompleteDSLPckg_Region_Namespace, gen_CompleteDSLPckg_Region_RedefinableElement, gen_CompleteDSLPckg_Vertex_NamedElement, gen_CompleteDSLPckg_Pseudostate_Vertex, gen_CompleteDSLPckg_ConnectionPointReference_Vertex, gen_CompleteDSLPckg_State_Vertex, gen_CompleteDSLPckg_State_RedefinableElement, gen_CompleteDSLPckg_State_Namespace, gen_CompleteDSLPckg_Activity_Behavior, gen_CompleteDSLPckg_FinalState_State, gen_CompleteDSLPckg_ProtocolStateMachine_StateMachine, gen_CompleteDSLPckg_ProtocolConformance_DirectedRelationship, gen_CompleteDSLPckg_ProtocolTransition_Transition, gen_CompleteDSLPckg_ActivityGroup_NamedElement, gen_CompleteDSLPckg_ActivityNode_NamedElement, gen_CompleteDSLPckg_ActivityNode_RedefinableElement, gen_CompleteDSLPckg_ControlFlow_ActivityEdge, gen_CompleteDSLPckg_ObjectFlow_ActivityEdge, gen_CompleteDSLPckg_ObjectNode_ActivityNode, gen_CompleteDSLPckg_ObjectNode_TypedElement, gen_CompleteDSLPckg_ActivityParameterNode_ObjectNode, gen_CompleteDSLPckg_ControlNode_ActivityNode, gen_CompleteDSLPckg_ActivityFinalNode_ControlNode, gen_CompleteDSLPckg_ActivityFinalNode_FinalNode, gen_CompleteDSLPckg_InitialNode_ControlNode, gen_CompleteDSLPckg_ActivityEdge_RedefinableElement, gen_CompleteDSLPckg_ForkNode_ControlNode, gen_CompleteDSLPckg_JoinNode_ControlNode, gen_CompleteDSLPckg_MergeNode_ControlNode, gen_CompleteDSLPckg_DecisionNode_ControlNode, gen_CompleteDSLPckg_ActivityPartition_ActivityGroup, gen_CompleteDSLPckg_CentralBufferNode_ObjectNode, gen_CompleteDSLPckg_FinalNode_ControlNode, gen_CompleteDSLPckg_FlowFinalNode_FinalNode, gen_CompleteDSLPckg_StructuredActivityNode_Namespace, gen_CompleteDSLPckg_StructuredActivityNode_ExecutableNode, gen_CompleteDSLPckg_StructuredActivityNode_ActivityGroup, gen_CompleteDSLPckg_StructuredActivityNode_Action, gen_CompleteDSLPckg_DataStoreNode_CentralBufferNode, gen_CompleteDSLPckg_ParameterSet_NamedElement, gen_CompleteDSLPckg_InterruptibleActivityRegion_ActivityGroup, gen_CompleteDSLPckg_ConditionalNode_StructuredActivityNode, gen_CompleteDSLPckg_ExecutableNode_ActivityNode, gen_CompleteDSLPckg_LoopNode_StructuredActivityNode, gen_CompleteDSLPckg_ExpansionRegion_StructuredActivityNode, gen_CompleteDSLPckg_ExpansionNode_ObjectNode, gen_CompleteDSLPckg_Clause_Element, gen_CompleteDSLPckg_SequenceNode_StructuredActivityNode, gen_CompleteDSLPckg_ExceptionHandler_Element, gen_CompleteDSLPckg_StateInvariant_InteractionFragment, gen_CompleteDSLPckg_Interaction_Behavior, gen_CompleteDSLPckg_Interaction_InteractionFragment, gen_CompleteDSLPckg_Lifeline_NamedElement, gen_CompleteDSLPckg_InteractionFragment_NamedElement, gen_CompleteDSLPckg_ExecutionSpecification_InteractionFragment, gen_CompleteDSLPckg_OccurenceSpecification_InteractionFragment, gen_CompleteDSLPckg_MessageEnd_NamedElement, gen_CompleteDSLPckg_ExecutionOccurrenceSpecification_OccurenceSpecification, gen_CompleteDSLPckg_Message_NamedElement, gen_CompleteDSLPckg_ConsiderIgnoreFragment_CombinedFragment, gen_CompleteDSLPckg_MessageOccurrenceSpecification_OccurenceSpecification, gen_CompleteDSLPckg_DestructionOccurrenceSpecification_MessageOccurrenceSpecification, gen_CompleteDSLPckg_BehaviorExecutionSpecification_ExecutionSpecification, gen_CompleteDSLPckg_ActionExecutionSpecification_ExecutionSpecification, gen_CompleteDSLPckg_GeneralOrdering_NamedElement, gen_CompleteDSLPckg_InteractionOperand_Namespace, gen_CompleteDSLPckg_PartDecomposition_InteractionUse, gen_CompleteDSLPckg_Actor_BehavioredClassifier, gen_CompleteDSLPckg_UseCase_BehavioredClassifier, gen_CompleteDSLPckg_Continuation_InteractionFragment, gen_CompleteDSLPckg_InteractionConstraint_Constraint, gen_CompleteDSLPckg_Gate_MessageEnd, gen_CompleteDSLPckg_InteractionUse_InteractionFragment, gen_CompleteDSLPckg_Include_DirectedRelationship, gen_CompleteDSLPckg_Include_NamedElement, gen_CompleteDSLPckg_ExtensionPoint_RedefinableElement, gen_CompleteDSLPckg_Extend_NamedElement, gen_CompleteDSLPckg_Extend_DirectedRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)