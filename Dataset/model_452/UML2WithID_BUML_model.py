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
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public")
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

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="composite"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared")
    }
)

CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent"),
			EnumerationLiteral(name="sequential")
    }
)

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="found"),
			EnumerationLiteral(name="lost"),
			EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="complete")
    }
)

MessageSort: Enumeration = Enumeration(
    name="MessageSort",
    literals={
            EnumerationLiteral(name="synchSignal"),
			EnumerationLiteral(name="synchCall"),
			EnumerationLiteral(name="asynchCall"),
			EnumerationLiteral(name="asynchSignal")
    }
)

ExpansionKind: Enumeration = Enumeration(
    name="ExpansionKind",
    literals={
            EnumerationLiteral(name="stream"),
			EnumerationLiteral(name="parallel"),
			EnumerationLiteral(name="iterative")
    }
)

InteractionOperator: Enumeration = Enumeration(
    name="InteractionOperator",
    literals={
            EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="neg"),
			EnumerationLiteral(name="critical"),
			EnumerationLiteral(name="consider"),
			EnumerationLiteral(name="par"),
			EnumerationLiteral(name="opt"),
			EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="alt"),
			EnumerationLiteral(name="break"),
			EnumerationLiteral(name="assert"),
			EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="seq")
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
            EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="entryPoint")
    }
)

ConnectorKind: Enumeration = Enumeration(
    name="ConnectorKind",
    literals={
            EnumerationLiteral(name="delegation"),
			EnumerationLiteral(name="assembly")
    }
)

ParameterEffectKind: Enumeration = Enumeration(
    name="ParameterEffectKind",
    literals={
            EnumerationLiteral(name="update"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="create")
    }
)

ObjectNodeOrderingKind: Enumeration = Enumeration(
    name="ObjectNodeOrderingKind",
    literals={
            EnumerationLiteral(name="FIFO"),
			EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered"),
			EnumerationLiteral(name="LIFO")
    }
)

# Classes
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)
UML2WithID_Comment = Class(name="UML2WithID::Comment")
UML2WithID_MultiplicityElement = Class(name="UML2WithID::MultiplicityElement", is_abstract=True)
Element = Class(name="Element")
UML2WithID_ValueSpecification = Class(name="UML2WithID::ValueSpecification", is_abstract=True)
UML2WithID_NamedElement = Class(name="UML2WithID::NamedElement", is_abstract=True)
TemplateableElement = Class(name="TemplateableElement")
UML2WithID_Dependency = Class(name="UML2WithID::Dependency")
UML2WithID_StringExpression = Class(name="UML2WithID::StringExpression")
UML2WithID_Namespace = Class(name="UML2WithID::Namespace", is_abstract=True)
NamedElement = Class(name="NamedElement")
UML2WithID_Constraint = Class(name="UML2WithID::Constraint")
UML2WithID_PackageableElement = Class(name="UML2WithID::PackageableElement", is_abstract=True)
UML2WithID_ElementImport = Class(name="UML2WithID::ElementImport")
UML2WithID_PackageImport = Class(name="UML2WithID::PackageImport")
UML2WithID_OpaqueExpression = Class(name="UML2WithID::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
UML2WithID_Parameter = Class(name="UML2WithID::Parameter")
UML2WithID_Behavior = Class(name="UML2WithID::Behavior", is_abstract=True)
TypedElement = Class(name="TypedElement")
ParameterableElement = Class(name="ParameterableElement")
UML2WithID_Expression = Class(name="UML2WithID::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2WithID_DirectedRelationship = Class(name="UML2WithID::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
UML2WithID_Relationship = Class(name="UML2WithID::Relationship", is_abstract=True)
UML2WithID_Class = Class(name="UML2WithID::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2WithID_Operation = Class(name="UML2WithID::Operation")
UML2WithID_Extension = Class(name="UML2WithID::Extension")
UML2WithID_Classifier = Class(name="UML2WithID::Classifier", is_abstract=True)
UML2WithID_Reception = Class(name="UML2WithID::Reception")
UML2WithID_Type = Class(name="UML2WithID::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
UML2WithID_Package = Class(name="UML2WithID::Package")
UML2WithID_Property = Class(name="UML2WithID::Property")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
UML2WithID_Association = Class(name="UML2WithID::Association")
UML2WithID_DataType = Class(name="UML2WithID::DataType")
BehavioralFeature = Class(name="BehavioralFeature")
MultiplicityElement = Class(name="MultiplicityElement")
UML2WithID_TypedElement = Class(name="UML2WithID::TypedElement", is_abstract=True)
UML2WithID_ParameterSet = Class(name="UML2WithID::ParameterSet")
Namespace = Class(name="Namespace")
UML2WithID_PackageMerge = Class(name="UML2WithID::PackageMerge")
UML2WithID_ProfileApplication = Class(name="UML2WithID::ProfileApplication")
UML2WithID_Enumeration = Class(name="UML2WithID::Enumeration")
DataType = Class(name="DataType")
UML2WithID_EnumerationLiteral = Class(name="UML2WithID::EnumerationLiteral")
Classifier = Class(name="Classifier")
InstanceSpecification = Class(name="InstanceSpecification")
UML2WithID_PrimitiveType = Class(name="UML2WithID::PrimitiveType")
Type = Class(name="Type")
RedefinableElement = Class(name="RedefinableElement")
UML2WithID_Feature = Class(name="UML2WithID::Feature", is_abstract=True)
UML2WithID_Generalization = Class(name="UML2WithID::Generalization")
UML2WithID_Substitution = Class(name="UML2WithID::Substitution")
UML2WithID_GeneralizationSet = Class(name="UML2WithID::GeneralizationSet")
UML2WithID_UseCase = Class(name="UML2WithID::UseCase")
UML2WithID_CollaborationOccurrence = Class(name="UML2WithID::CollaborationOccurrence")
UML2WithID_Slot = Class(name="UML2WithID::Slot")
UML2WithID_LiteralBoolean = Class(name="UML2WithID::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
UML2WithID_LiteralSpecification = Class(name="UML2WithID::LiteralSpecification", is_abstract=True)
UML2WithID_LiteralString = Class(name="UML2WithID::LiteralString")
UML2WithID_LiteralNull = Class(name="UML2WithID::LiteralNull")
UML2WithID_LiteralInteger = Class(name="UML2WithID::LiteralInteger")
UML2WithID_LiteralUnlimitedNatural = Class(name="UML2WithID::LiteralUnlimitedNatural")
UML2WithID_BehavioralFeature = Class(name="UML2WithID::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
UML2WithID_StructuralFeature = Class(name="UML2WithID::StructuralFeature", is_abstract=True)
UML2WithID_InstanceSpecification = Class(name="UML2WithID::InstanceSpecification")
DeployedArtifact = Class(name="DeployedArtifact")
UML2WithID_RedefinableElement = Class(name="UML2WithID::RedefinableElement", is_abstract=True)
UML2WithID_InstanceValue = Class(name="UML2WithID::InstanceValue")
DirectedRelationship = Class(name="DirectedRelationship")
UML2WithID_Stereotype = Class(name="UML2WithID::Stereotype")
Class_ = Class(name="Class")
UML2WithID_Profile = Class(name="UML2WithID::Profile")
Package = Class(name="Package")
PackageImport = Class(name="PackageImport")
Association = Class(name="Association")
UML2WithID_ExtensionEnd = Class(name="UML2WithID::ExtensionEnd")
Property_ = Class(name="Property")
UML2WithID_BehavioredClassifier = Class(name="UML2WithID::BehavioredClassifier", is_abstract=True)
UML2WithID_Action = Class(name="UML2WithID::Action")
UML2WithID_StructuredActivityNode = Class(name="UML2WithID::StructuredActivityNode")
UML2WithID_Permission = Class(name="UML2WithID::Permission")
Dependency = Class(name="Dependency")
UML2WithID_Usage = Class(name="UML2WithID::Usage")
UML2WithID_Implementation = Class(name="UML2WithID::Implementation")
UML2WithID_Trigger = Class(name="UML2WithID::Trigger", is_abstract=True)
UML2WithID_StateMachine = Class(name="UML2WithID::StateMachine")
UML2WithID_Activity = Class(name="UML2WithID::Activity")
Behavior = Class(name="Behavior")
UML2WithID_ActivityEdge = Class(name="UML2WithID::ActivityEdge", is_abstract=True)
UML2WithID_ActivityGroup = Class(name="UML2WithID::ActivityGroup", is_abstract=True)
UML2WithID_ActivityNode = Class(name="UML2WithID::ActivityNode", is_abstract=True)
UML2WithID_InformationItem = Class(name="UML2WithID::InformationItem")
UML2WithID_InformationFlow = Class(name="UML2WithID::InformationFlow")
UML2WithID_Model = Class(name="UML2WithID::Model")
UML2WithID_ConnectorEnd = Class(name="UML2WithID::ConnectorEnd")
UML2WithID_Abstraction = Class(name="UML2WithID::Abstraction")
UML2WithID_Realization = Class(name="UML2WithID::Realization")
Abstraction = Class(name="Abstraction")
UML2WithID_Component = Class(name="UML2WithID::Component")
Realization = Class(name="Realization")
UML2WithID_AssociationClass = Class(name="UML2WithID::AssociationClass")
UML2WithID_ConnectableElement = Class(name="UML2WithID::ConnectableElement", is_abstract=True)
UML2WithID_Connector = Class(name="UML2WithID::Connector")
UML2WithID_StructuredClassifier = Class(name="UML2WithID::StructuredClassifier", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
UML2WithID_OutputPin = Class(name="UML2WithID::OutputPin")
UML2WithID_ActivityPartition = Class(name="UML2WithID::ActivityPartition")
UML2WithID_InterruptibleActivityRegion = Class(name="UML2WithID::InterruptibleActivityRegion")
UML2WithID_InitialNode = Class(name="UML2WithID::InitialNode")
ControlNode = Class(name="ControlNode")
UML2WithID_FinalNode = Class(name="UML2WithID::FinalNode", is_abstract=True)
UML2WithID_ActivityFinalNode = Class(name="UML2WithID::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
UML2WithID_DecisionNode = Class(name="UML2WithID::DecisionNode")
UML2WithID_MergeNode = Class(name="UML2WithID::MergeNode")
UML2WithID_ExecutableNode = Class(name="UML2WithID::ExecutableNode", is_abstract=True)
UML2WithID_ExceptionHandler = Class(name="UML2WithID::ExceptionHandler")
Pin = Class(name="Pin")
UML2WithID_InputPin = Class(name="UML2WithID::InputPin")
UML2WithID_ObjectNode = Class(name="UML2WithID::ObjectNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
UML2WithID_State = Class(name="UML2WithID::State")
UML2WithID_ControlNode = Class(name="UML2WithID::ControlNode", is_abstract=True)
UML2WithID_ControlFlow = Class(name="UML2WithID::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
UML2WithID_ObjectFlow = Class(name="UML2WithID::ObjectFlow")
UML2WithID_Artifact = Class(name="UML2WithID::Artifact")
UML2WithID_Manifestation = Class(name="UML2WithID::Manifestation")
UML2WithID_Pin = Class(name="UML2WithID::Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
UML2WithID_ActivityParameterNode = Class(name="UML2WithID::ActivityParameterNode")
UML2WithID_ValuePin = Class(name="UML2WithID::ValuePin")
InputPin = Class(name="InputPin")
UML2WithID_Interface = Class(name="UML2WithID::Interface")
UML2WithID_ProtocolStateMachine = Class(name="UML2WithID::ProtocolStateMachine")
UML2WithID_Collaboration = Class(name="UML2WithID::Collaboration")
StructuredClassifier = Class(name="StructuredClassifier")
UML2WithID_Port = Class(name="UML2WithID::Port")
UML2WithID_Actor = Class(name="UML2WithID::Actor")
UML2WithID_Extend = Class(name="UML2WithID::Extend")
UML2WithID_ExtensionPoint = Class(name="UML2WithID::ExtensionPoint")
UML2WithID_Include = Class(name="UML2WithID::Include")
UML2WithID_Signal = Class(name="UML2WithID::Signal")
UML2WithID_SignalTrigger = Class(name="UML2WithID::SignalTrigger")
UML2WithID_TimeTrigger = Class(name="UML2WithID::TimeTrigger")
UML2WithID_EncapsulatedClassifier = Class(name="UML2WithID::EncapsulatedClassifier", is_abstract=True)
UML2WithID_CallTrigger = Class(name="UML2WithID::CallTrigger")
MessageTrigger = Class(name="MessageTrigger")
UML2WithID_MessageTrigger = Class(name="UML2WithID::MessageTrigger", is_abstract=True)
Trigger = Class(name="Trigger")
UML2WithID_ChangeTrigger = Class(name="UML2WithID::ChangeTrigger")
UML2WithID_LoopNode = Class(name="UML2WithID::LoopNode")
UML2WithID_AnyTrigger = Class(name="UML2WithID::AnyTrigger")
UML2WithID_Variable = Class(name="UML2WithID::Variable")
Action = Class(name="Action")
ActivityGroup = Class(name="ActivityGroup")
UML2WithID_ConditionalNode = Class(name="UML2WithID::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
UML2WithID_Clause = Class(name="UML2WithID::Clause")
UML2WithID_InteractionFragment = Class(name="UML2WithID::InteractionFragment", is_abstract=True)
UML2WithID_Gate = Class(name="UML2WithID::Gate")
UML2WithID_GeneralOrdering = Class(name="UML2WithID::GeneralOrdering")
UML2WithID_InteractionOperand = Class(name="UML2WithID::InteractionOperand")
UML2WithID_Interaction = Class(name="UML2WithID::Interaction")
InteractionFragment = Class(name="InteractionFragment")
UML2WithID_Lifeline = Class(name="UML2WithID::Lifeline")
UML2WithID_Message = Class(name="UML2WithID::Message")
UML2WithID_EventOccurrence = Class(name="UML2WithID::EventOccurrence")
UML2WithID_PartDecomposition = Class(name="UML2WithID::PartDecomposition")
UML2WithID_MessageEnd = Class(name="UML2WithID::MessageEnd", is_abstract=True)
UML2WithID_Stop = Class(name="UML2WithID::Stop")
EventOccurrence = Class(name="EventOccurrence")
UML2WithID_TemplateSignature = Class(name="UML2WithID::TemplateSignature")
UML2WithID_TemplateParameter = Class(name="UML2WithID::TemplateParameter")
UML2WithID_TemplateableElement = Class(name="UML2WithID::TemplateableElement", is_abstract=True)
MessageEnd = Class(name="MessageEnd")
UML2WithID_ExecutionOccurrence = Class(name="UML2WithID::ExecutionOccurrence")
UML2WithID_StateInvariant = Class(name="UML2WithID::StateInvariant")
UML2WithID_TemplateParameterSubstitution = Class(name="UML2WithID::TemplateParameterSubstitution")
UML2WithID_ParameterableElement = Class(name="UML2WithID::ParameterableElement", is_abstract=True)
UML2WithID_TemplateBinding = Class(name="UML2WithID::TemplateBinding")
UML2WithID_FlowFinalNode = Class(name="UML2WithID::FlowFinalNode")
UML2WithID_OperationTemplateParameter = Class(name="UML2WithID::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
UML2WithID_ClassifierTemplateParameter = Class(name="UML2WithID::ClassifierTemplateParameter")
UML2WithID_ParameterableClassifier = Class(name="UML2WithID::ParameterableClassifier", is_abstract=True)
UML2WithID_RedefinableTemplateSignature = Class(name="UML2WithID::RedefinableTemplateSignature")
TemplateSignature = Class(name="TemplateSignature")
UML2WithID_TemplateableClassifier = Class(name="UML2WithID::TemplateableClassifier", is_abstract=True)
UML2WithID_ConnectableElementTemplateParameter = Class(name="UML2WithID::ConnectableElementTemplateParameter")
UML2WithID_ForkNode = Class(name="UML2WithID::ForkNode")
UML2WithID_JoinNode = Class(name="UML2WithID::JoinNode")
UML2WithID_ExpansionNode = Class(name="UML2WithID::ExpansionNode")
UML2WithID_ExpansionRegion = Class(name="UML2WithID::ExpansionRegion")
UML2WithID_CentralBufferNode = Class(name="UML2WithID::CentralBufferNode")
UML2WithID_InteractionOccurrence = Class(name="UML2WithID::InteractionOccurrence")
UML2WithID_CombinedFragment = Class(name="UML2WithID::CombinedFragment")
UML2WithID_Continuation = Class(name="UML2WithID::Continuation")
UML2WithID_Region = Class(name="UML2WithID::Region")
UML2WithID_Pseudostate = Class(name="UML2WithID::Pseudostate")
InteractionOccurrence = Class(name="InteractionOccurrence")
UML2WithID_InteractionConstraint = Class(name="UML2WithID::InteractionConstraint")
Constraint = Class(name="Constraint")
UML2WithID_ConnectionPointReference = Class(name="UML2WithID::ConnectionPointReference")
UML2WithID_Vertex = Class(name="UML2WithID::Vertex", is_abstract=True)
UML2WithID_Transition = Class(name="UML2WithID::Transition")
Vertex = Class(name="Vertex")
UML2WithID_ReadSelfAction = Class(name="UML2WithID::ReadSelfAction")
UML2WithID_StructuralFeatureAction = Class(name="UML2WithID::StructuralFeatureAction", is_abstract=True)
UML2WithID_ReadStructuralFeatureAction = Class(name="UML2WithID::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UML2WithID_WriteStructuralFeatureAction = Class(name="UML2WithID::WriteStructuralFeatureAction", is_abstract=True)
UML2WithID_ClearStructuralFeatureAction = Class(name="UML2WithID::ClearStructuralFeatureAction")
UML2WithID_FinalState = Class(name="UML2WithID::FinalState")
State = Class(name="State")
UML2WithID_CreateObjectAction = Class(name="UML2WithID::CreateObjectAction")
UML2WithID_DestroyObjectAction = Class(name="UML2WithID::DestroyObjectAction")
UML2WithID_TestIdentityAction = Class(name="UML2WithID::TestIdentityAction")
UML2WithID_LinkEndCreationData = Class(name="UML2WithID::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UML2WithID_CreateLinkAction = Class(name="UML2WithID::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UML2WithID_WriteLinkAction = Class(name="UML2WithID::WriteLinkAction", is_abstract=True)
UML2WithID_DestroyLinkAction = Class(name="UML2WithID::DestroyLinkAction")
UML2WithID_ClearAssociationAction = Class(name="UML2WithID::ClearAssociationAction")
UML2WithID_VariableAction = Class(name="UML2WithID::VariableAction", is_abstract=True)
UML2WithID_ReadVariableAction = Class(name="UML2WithID::ReadVariableAction")
VariableAction = Class(name="VariableAction")
UML2WithID_RemoveStructuralFeatureValueAction = Class(name="UML2WithID::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UML2WithID_AddStructuralFeatureValueAction = Class(name="UML2WithID::AddStructuralFeatureValueAction")
UML2WithID_LinkAction = Class(name="UML2WithID::LinkAction", is_abstract=True)
UML2WithID_LinkEndData = Class(name="UML2WithID::LinkEndData")
UML2WithID_QualifierValue = Class(name="UML2WithID::QualifierValue")
UML2WithID_ReadLinkAction = Class(name="UML2WithID::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UML2WithID_CallAction = Class(name="UML2WithID::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
UML2WithID_InvocationAction = Class(name="UML2WithID::InvocationAction", is_abstract=True)
UML2WithID_SendSignalAction = Class(name="UML2WithID::SendSignalAction")
UML2WithID_BroadcastSignalAction = Class(name="UML2WithID::BroadcastSignalAction")
UML2WithID_WriteVariableAction = Class(name="UML2WithID::WriteVariableAction", is_abstract=True)
UML2WithID_ClearVariableAction = Class(name="UML2WithID::ClearVariableAction")
UML2WithID_AddVariableValueAction = Class(name="UML2WithID::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UML2WithID_RemoveVariableValueAction = Class(name="UML2WithID::RemoveVariableValueAction")
UML2WithID_ApplyFunctionAction = Class(name="UML2WithID::ApplyFunctionAction")
UML2WithID_PrimitiveFunction = Class(name="UML2WithID::PrimitiveFunction")
UML2WithID_Duration = Class(name="UML2WithID::Duration")
UML2WithID_TimeObservationAction = Class(name="UML2WithID::TimeObservationAction")
UML2WithID_DurationInterval = Class(name="UML2WithID::DurationInterval")
Interval = Class(name="Interval")
UML2WithID_Interval = Class(name="UML2WithID::Interval")
UML2WithID_TimeConstraint = Class(name="UML2WithID::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UML2WithID_IntervalConstraint = Class(name="UML2WithID::IntervalConstraint")
UML2WithID_TimeInterval = Class(name="UML2WithID::TimeInterval")
UML2WithID_SendObjectAction = Class(name="UML2WithID::SendObjectAction")
UML2WithID_CallOperationAction = Class(name="UML2WithID::CallOperationAction")
CallAction = Class(name="CallAction")
UML2WithID_CallBehaviorAction = Class(name="UML2WithID::CallBehaviorAction")
UML2WithID_TimeExpression = Class(name="UML2WithID::TimeExpression")
UML2WithID_Deployment = Class(name="UML2WithID::Deployment")
UML2WithID_DeployedArtifact = Class(name="UML2WithID::DeployedArtifact", is_abstract=True)
UML2WithID_DurationObservationAction = Class(name="UML2WithID::DurationObservationAction")
UML2WithID_DurationConstraint = Class(name="UML2WithID::DurationConstraint")
UML2WithID_DataStoreNode = Class(name="UML2WithID::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2WithID_ProtocolConformance = Class(name="UML2WithID::ProtocolConformance")
StateMachine = Class(name="StateMachine")
UML2WithID_ProtocolTransition = Class(name="UML2WithID::ProtocolTransition")
Transition = Class(name="Transition")
UML2WithID_ReadExtentAction = Class(name="UML2WithID::ReadExtentAction")
UML2WithID_DeploymentTarget = Class(name="UML2WithID::DeploymentTarget", is_abstract=True)
UML2WithID_DeploymentSpecification = Class(name="UML2WithID::DeploymentSpecification")
UML2WithID_Node = Class(name="UML2WithID::Node")
UML2WithID_Device = Class(name="UML2WithID::Device")
Node = Class(name="Node")
UML2WithID_ExecutionEnvironment = Class(name="UML2WithID::ExecutionEnvironment")
UML2WithID_CommunicationPath = Class(name="UML2WithID::CommunicationPath")
UML2WithID_StartOwnedBehaviorAction = Class(name="UML2WithID::StartOwnedBehaviorAction")
UML2WithID_ReadLinkObjectEndAction = Class(name="UML2WithID::ReadLinkObjectEndAction")
UML2WithID_ReclassifyObjectAction = Class(name="UML2WithID::ReclassifyObjectAction")
UML2WithID_ReadIsClassifiedObjectAction = Class(name="UML2WithID::ReadIsClassifiedObjectAction")
UML2WithID_AcceptCallAction = Class(name="UML2WithID::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UML2WithID_ReplyAction = Class(name="UML2WithID::ReplyAction")
UML2WithID_ReadLinkObjectEndQualifierAction = Class(name="UML2WithID::ReadLinkObjectEndQualifierAction")
UML2WithID_CreateLinkObjectAction = Class(name="UML2WithID::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UML2WithID_AcceptEventAction = Class(name="UML2WithID::AcceptEventAction")
UML2WithID_RaiseExceptionAction = Class(name="UML2WithID::RaiseExceptionAction")
Artifact = Class(name="Artifact")

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# UML2WithID_Comment class attributes and methods
UML2WithID_Comment_body: Property = Property(name="body", type=StringType)
UML2WithID_Comment.attributes={UML2WithID_Comment_body}

# UML2WithID_MultiplicityElement class attributes and methods
UML2WithID_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
UML2WithID_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
UML2WithID_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
UML2WithID_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
UML2WithID_MultiplicityElement.attributes={UML2WithID_MultiplicityElement_upper, UML2WithID_MultiplicityElement_isOrdered, UML2WithID_MultiplicityElement_lower, UML2WithID_MultiplicityElement_isUnique}

# Element class attributes and methods

# UML2WithID_ValueSpecification class attributes and methods

# UML2WithID_NamedElement class attributes and methods
UML2WithID_NamedElement_name: Property = Property(name="name", type=StringType)
UML2WithID_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
UML2WithID_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
UML2WithID_NamedElement.attributes={UML2WithID_NamedElement_qualifiedName, UML2WithID_NamedElement_name, UML2WithID_NamedElement_visibility}

# TemplateableElement class attributes and methods

# UML2WithID_Dependency class attributes and methods

# UML2WithID_StringExpression class attributes and methods

# UML2WithID_Namespace class attributes and methods

# NamedElement class attributes and methods

# UML2WithID_Constraint class attributes and methods

# UML2WithID_PackageableElement class attributes and methods
UML2WithID_PackageableElement_packageableElement_visibility: Property = Property(name="packageableElement_visibility", type=StringType)
UML2WithID_PackageableElement.attributes={UML2WithID_PackageableElement_packageableElement_visibility}

# UML2WithID_ElementImport class attributes and methods
UML2WithID_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
UML2WithID_ElementImport_alias: Property = Property(name="alias", type=StringType)
UML2WithID_ElementImport.attributes={UML2WithID_ElementImport_alias, UML2WithID_ElementImport_visibility}

# UML2WithID_PackageImport class attributes and methods
UML2WithID_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
UML2WithID_PackageImport.attributes={UML2WithID_PackageImport_visibility}

# UML2WithID_OpaqueExpression class attributes and methods
UML2WithID_OpaqueExpression_bodies: Property = Property(name="bodies", type=StringType)
UML2WithID_OpaqueExpression_language: Property = Property(name="language", type=StringType)
UML2WithID_OpaqueExpression.attributes={UML2WithID_OpaqueExpression_bodies, UML2WithID_OpaqueExpression_language}

# ValueSpecification class attributes and methods

# UML2WithID_Parameter class attributes and methods
UML2WithID_Parameter_default: Property = Property(name="default", type=StringType)
UML2WithID_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2WithID_Parameter_isException: Property = Property(name="isException", type=BooleanType)
UML2WithID_Parameter_isStream: Property = Property(name="isStream", type=BooleanType)
UML2WithID_Parameter_effect: Property = Property(name="effect", type=StringType)
UML2WithID_Parameter.attributes={UML2WithID_Parameter_effect, UML2WithID_Parameter_isStream, UML2WithID_Parameter_isException, UML2WithID_Parameter_direction, UML2WithID_Parameter_default}

# UML2WithID_Behavior class attributes and methods
UML2WithID_Behavior_isReentrant: Property = Property(name="isReentrant", type=BooleanType)
UML2WithID_Behavior.attributes={UML2WithID_Behavior_isReentrant}

# TypedElement class attributes and methods

# ParameterableElement class attributes and methods

# UML2WithID_Expression class attributes and methods
UML2WithID_Expression_symbol: Property = Property(name="symbol", type=StringType)
UML2WithID_Expression.attributes={UML2WithID_Expression_symbol}

# OpaqueExpression class attributes and methods

# UML2WithID_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# UML2WithID_Relationship class attributes and methods

# UML2WithID_Class class attributes and methods
UML2WithID_Class_isActive: Property = Property(name="isActive", type=BooleanType)
UML2WithID_Class.attributes={UML2WithID_Class_isActive}

# BehavioredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2WithID_Operation class attributes and methods
UML2WithID_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
UML2WithID_Operation.attributes={UML2WithID_Operation_isQuery}

# UML2WithID_Extension class attributes and methods
UML2WithID_Extension_isRequired: Property = Property(name="isRequired", type=BooleanType)
UML2WithID_Extension.attributes={UML2WithID_Extension_isRequired}

# UML2WithID_Classifier class attributes and methods
UML2WithID_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2WithID_Classifier.attributes={UML2WithID_Classifier_isAbstract}

# UML2WithID_Reception class attributes and methods

# UML2WithID_Type class attributes and methods

# PackageableElement class attributes and methods

# UML2WithID_Package class attributes and methods

# UML2WithID_Property class attributes and methods
UML2WithID_Property_default: Property = Property(name="default", type=StringType)
UML2WithID_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2WithID_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2WithID_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
UML2WithID_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UML2WithID_Property.attributes={UML2WithID_Property_isDerivedUnion, UML2WithID_Property_default, UML2WithID_Property_isDerived, UML2WithID_Property_isComposite, UML2WithID_Property_aggregation}

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# UML2WithID_Association class attributes and methods
UML2WithID_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2WithID_Association.attributes={UML2WithID_Association_isDerived}

# UML2WithID_DataType class attributes and methods

# BehavioralFeature class attributes and methods

# MultiplicityElement class attributes and methods

# UML2WithID_TypedElement class attributes and methods

# UML2WithID_ParameterSet class attributes and methods

# Namespace class attributes and methods

# UML2WithID_PackageMerge class attributes and methods

# UML2WithID_ProfileApplication class attributes and methods

# UML2WithID_Enumeration class attributes and methods

# DataType class attributes and methods

# UML2WithID_EnumerationLiteral class attributes and methods

# Classifier class attributes and methods

# InstanceSpecification class attributes and methods

# UML2WithID_PrimitiveType class attributes and methods

# Type class attributes and methods

# RedefinableElement class attributes and methods

# UML2WithID_Feature class attributes and methods
UML2WithID_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
UML2WithID_Feature.attributes={UML2WithID_Feature_isStatic}

# UML2WithID_Generalization class attributes and methods
UML2WithID_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
UML2WithID_Generalization.attributes={UML2WithID_Generalization_isSubstitutable}

# UML2WithID_Substitution class attributes and methods

# UML2WithID_GeneralizationSet class attributes and methods
UML2WithID_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
UML2WithID_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
UML2WithID_GeneralizationSet.attributes={UML2WithID_GeneralizationSet_isCovering, UML2WithID_GeneralizationSet_isDisjoint}

# UML2WithID_UseCase class attributes and methods

# UML2WithID_CollaborationOccurrence class attributes and methods

# UML2WithID_Slot class attributes and methods

# UML2WithID_LiteralBoolean class attributes and methods
UML2WithID_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
UML2WithID_LiteralBoolean.attributes={UML2WithID_LiteralBoolean_value}

# LiteralSpecification class attributes and methods

# UML2WithID_LiteralSpecification class attributes and methods

# UML2WithID_LiteralString class attributes and methods
UML2WithID_LiteralString_value: Property = Property(name="value", type=StringType)
UML2WithID_LiteralString.attributes={UML2WithID_LiteralString_value}

# UML2WithID_LiteralNull class attributes and methods

# UML2WithID_LiteralInteger class attributes and methods
UML2WithID_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
UML2WithID_LiteralInteger.attributes={UML2WithID_LiteralInteger_value}

# UML2WithID_LiteralUnlimitedNatural class attributes and methods
UML2WithID_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
UML2WithID_LiteralUnlimitedNatural.attributes={UML2WithID_LiteralUnlimitedNatural_value}

# UML2WithID_BehavioralFeature class attributes and methods
UML2WithID_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2WithID_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
UML2WithID_BehavioralFeature.attributes={UML2WithID_BehavioralFeature_isAbstract, UML2WithID_BehavioralFeature_concurrency}

# Feature class attributes and methods

# UML2WithID_StructuralFeature class attributes and methods
UML2WithID_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
UML2WithID_StructuralFeature.attributes={UML2WithID_StructuralFeature_isReadOnly}

# UML2WithID_InstanceSpecification class attributes and methods

# DeployedArtifact class attributes and methods

# UML2WithID_RedefinableElement class attributes and methods
UML2WithID_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
UML2WithID_RedefinableElement.attributes={UML2WithID_RedefinableElement_isLeaf}

# UML2WithID_InstanceValue class attributes and methods

# DirectedRelationship class attributes and methods

# UML2WithID_Stereotype class attributes and methods

# Class class attributes and methods

# UML2WithID_Profile class attributes and methods

# Package class attributes and methods

# PackageImport class attributes and methods

# Association class attributes and methods

# UML2WithID_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2WithID_BehavioredClassifier class attributes and methods

# UML2WithID_Action class attributes and methods
UML2WithID_Action_effect: Property = Property(name="effect", type=StringType)
UML2WithID_Action.attributes={UML2WithID_Action_effect}

# UML2WithID_StructuredActivityNode class attributes and methods
UML2WithID_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
UML2WithID_StructuredActivityNode.attributes={UML2WithID_StructuredActivityNode_mustIsolate}

# UML2WithID_Permission class attributes and methods

# Dependency class attributes and methods

# UML2WithID_Usage class attributes and methods

# UML2WithID_Implementation class attributes and methods

# UML2WithID_Trigger class attributes and methods

# UML2WithID_StateMachine class attributes and methods

# UML2WithID_Activity class attributes and methods
UML2WithID_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
UML2WithID_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
UML2WithID_Activity_body: Property = Property(name="body", type=StringType)
UML2WithID_Activity_language: Property = Property(name="language", type=StringType)
UML2WithID_Activity.attributes={UML2WithID_Activity_isSingleExecution, UML2WithID_Activity_language, UML2WithID_Activity_body, UML2WithID_Activity_isReadOnly}

# Behavior class attributes and methods

# UML2WithID_ActivityEdge class attributes and methods

# UML2WithID_ActivityGroup class attributes and methods

# UML2WithID_ActivityNode class attributes and methods

# UML2WithID_InformationItem class attributes and methods

# UML2WithID_InformationFlow class attributes and methods

# UML2WithID_Model class attributes and methods
UML2WithID_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
UML2WithID_Model.attributes={UML2WithID_Model_viewpoint}

# UML2WithID_ConnectorEnd class attributes and methods

# UML2WithID_Abstraction class attributes and methods

# UML2WithID_Realization class attributes and methods

# Abstraction class attributes and methods

# UML2WithID_Component class attributes and methods
UML2WithID_Component_isIndirectlyInstantiated: Property = Property(name="isIndirectlyInstantiated", type=BooleanType)
UML2WithID_Component.attributes={UML2WithID_Component_isIndirectlyInstantiated}

# Realization class attributes and methods

# UML2WithID_AssociationClass class attributes and methods

# UML2WithID_ConnectableElement class attributes and methods

# UML2WithID_Connector class attributes and methods
UML2WithID_Connector_kind: Property = Property(name="kind", type=StringType)
UML2WithID_Connector.attributes={UML2WithID_Connector_kind}

# UML2WithID_StructuredClassifier class attributes and methods

# ExecutableNode class attributes and methods

# UML2WithID_OutputPin class attributes and methods

# UML2WithID_ActivityPartition class attributes and methods
UML2WithID_ActivityPartition_isDimension: Property = Property(name="isDimension", type=BooleanType)
UML2WithID_ActivityPartition_isExternal: Property = Property(name="isExternal", type=BooleanType)
UML2WithID_ActivityPartition.attributes={UML2WithID_ActivityPartition_isExternal, UML2WithID_ActivityPartition_isDimension}

# UML2WithID_InterruptibleActivityRegion class attributes and methods

# UML2WithID_InitialNode class attributes and methods

# ControlNode class attributes and methods

# UML2WithID_FinalNode class attributes and methods

# UML2WithID_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# UML2WithID_DecisionNode class attributes and methods

# UML2WithID_MergeNode class attributes and methods

# UML2WithID_ExecutableNode class attributes and methods

# UML2WithID_ExceptionHandler class attributes and methods

# Pin class attributes and methods

# UML2WithID_InputPin class attributes and methods

# UML2WithID_ObjectNode class attributes and methods
UML2WithID_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
UML2WithID_ObjectNode.attributes={UML2WithID_ObjectNode_ordering}

# ActivityNode class attributes and methods

# UML2WithID_State class attributes and methods
UML2WithID_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2WithID_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
UML2WithID_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
UML2WithID_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
UML2WithID_State.attributes={UML2WithID_State_isSubmachineState, UML2WithID_State_isComposite, UML2WithID_State_isSimple, UML2WithID_State_isOrthogonal}

# UML2WithID_ControlNode class attributes and methods

# UML2WithID_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# UML2WithID_ObjectFlow class attributes and methods
UML2WithID_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
UML2WithID_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
UML2WithID_ObjectFlow.attributes={UML2WithID_ObjectFlow_isMultireceive, UML2WithID_ObjectFlow_isMulticast}

# UML2WithID_Artifact class attributes and methods
UML2WithID_Artifact_fileName: Property = Property(name="fileName", type=StringType)
UML2WithID_Artifact.attributes={UML2WithID_Artifact_fileName}

# UML2WithID_Manifestation class attributes and methods

# UML2WithID_Pin class attributes and methods

# ObjectNode class attributes and methods

# UML2WithID_ActivityParameterNode class attributes and methods

# UML2WithID_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2WithID_Interface class attributes and methods

# UML2WithID_ProtocolStateMachine class attributes and methods

# UML2WithID_Collaboration class attributes and methods

# StructuredClassifier class attributes and methods

# UML2WithID_Port class attributes and methods
UML2WithID_Port_isBehavior: Property = Property(name="isBehavior", type=BooleanType)
UML2WithID_Port_isService: Property = Property(name="isService", type=BooleanType)
UML2WithID_Port.attributes={UML2WithID_Port_isBehavior, UML2WithID_Port_isService}

# UML2WithID_Actor class attributes and methods

# UML2WithID_Extend class attributes and methods

# UML2WithID_ExtensionPoint class attributes and methods

# UML2WithID_Include class attributes and methods

# UML2WithID_Signal class attributes and methods

# UML2WithID_SignalTrigger class attributes and methods

# UML2WithID_TimeTrigger class attributes and methods
UML2WithID_TimeTrigger_isRelative: Property = Property(name="isRelative", type=BooleanType)
UML2WithID_TimeTrigger.attributes={UML2WithID_TimeTrigger_isRelative}

# UML2WithID_EncapsulatedClassifier class attributes and methods

# UML2WithID_CallTrigger class attributes and methods

# MessageTrigger class attributes and methods

# UML2WithID_MessageTrigger class attributes and methods

# Trigger class attributes and methods

# UML2WithID_ChangeTrigger class attributes and methods

# UML2WithID_LoopNode class attributes and methods
UML2WithID_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
UML2WithID_LoopNode.attributes={UML2WithID_LoopNode_isTestedFirst}

# UML2WithID_AnyTrigger class attributes and methods

# UML2WithID_Variable class attributes and methods

# Action class attributes and methods

# ActivityGroup class attributes and methods

# UML2WithID_ConditionalNode class attributes and methods
UML2WithID_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
UML2WithID_ConditionalNode_isAssured: Property = Property(name="isAssured", type=BooleanType)
UML2WithID_ConditionalNode.attributes={UML2WithID_ConditionalNode_isAssured, UML2WithID_ConditionalNode_isDeterminate}

# StructuredActivityNode class attributes and methods

# UML2WithID_Clause class attributes and methods

# UML2WithID_InteractionFragment class attributes and methods

# UML2WithID_Gate class attributes and methods

# UML2WithID_GeneralOrdering class attributes and methods

# UML2WithID_InteractionOperand class attributes and methods

# UML2WithID_Interaction class attributes and methods

# InteractionFragment class attributes and methods

# UML2WithID_Lifeline class attributes and methods

# UML2WithID_Message class attributes and methods
UML2WithID_Message_messageKind: Property = Property(name="messageKind", type=StringType)
UML2WithID_Message_messageSort: Property = Property(name="messageSort", type=StringType)
UML2WithID_Message.attributes={UML2WithID_Message_messageKind, UML2WithID_Message_messageSort}

# UML2WithID_EventOccurrence class attributes and methods

# UML2WithID_PartDecomposition class attributes and methods

# UML2WithID_MessageEnd class attributes and methods

# UML2WithID_Stop class attributes and methods

# EventOccurrence class attributes and methods

# UML2WithID_TemplateSignature class attributes and methods

# UML2WithID_TemplateParameter class attributes and methods

# UML2WithID_TemplateableElement class attributes and methods

# MessageEnd class attributes and methods

# UML2WithID_ExecutionOccurrence class attributes and methods

# UML2WithID_StateInvariant class attributes and methods

# UML2WithID_TemplateParameterSubstitution class attributes and methods

# UML2WithID_ParameterableElement class attributes and methods

# UML2WithID_TemplateBinding class attributes and methods

# UML2WithID_FlowFinalNode class attributes and methods

# UML2WithID_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# UML2WithID_ClassifierTemplateParameter class attributes and methods
UML2WithID_ClassifierTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=BooleanType)
UML2WithID_ClassifierTemplateParameter.attributes={UML2WithID_ClassifierTemplateParameter_allowSubstitutable}

# UML2WithID_ParameterableClassifier class attributes and methods

# UML2WithID_RedefinableTemplateSignature class attributes and methods

# TemplateSignature class attributes and methods

# UML2WithID_TemplateableClassifier class attributes and methods

# UML2WithID_ConnectableElementTemplateParameter class attributes and methods

# UML2WithID_ForkNode class attributes and methods

# UML2WithID_JoinNode class attributes and methods
UML2WithID_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
UML2WithID_JoinNode.attributes={UML2WithID_JoinNode_isCombineDuplicate}

# UML2WithID_ExpansionNode class attributes and methods

# UML2WithID_ExpansionRegion class attributes and methods
UML2WithID_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
UML2WithID_ExpansionRegion.attributes={UML2WithID_ExpansionRegion_mode}

# UML2WithID_CentralBufferNode class attributes and methods

# UML2WithID_InteractionOccurrence class attributes and methods

# UML2WithID_CombinedFragment class attributes and methods
UML2WithID_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
UML2WithID_CombinedFragment.attributes={UML2WithID_CombinedFragment_interactionOperator}

# UML2WithID_Continuation class attributes and methods
UML2WithID_Continuation_setting: Property = Property(name="setting", type=BooleanType)
UML2WithID_Continuation.attributes={UML2WithID_Continuation_setting}

# UML2WithID_Region class attributes and methods

# UML2WithID_Pseudostate class attributes and methods
UML2WithID_Pseudostate_kind: Property = Property(name="kind", type=StringType)
UML2WithID_Pseudostate.attributes={UML2WithID_Pseudostate_kind}

# InteractionOccurrence class attributes and methods

# UML2WithID_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# UML2WithID_ConnectionPointReference class attributes and methods

# UML2WithID_Vertex class attributes and methods

# UML2WithID_Transition class attributes and methods
UML2WithID_Transition_kind: Property = Property(name="kind", type=StringType)
UML2WithID_Transition.attributes={UML2WithID_Transition_kind}

# Vertex class attributes and methods

# UML2WithID_ReadSelfAction class attributes and methods

# UML2WithID_StructuralFeatureAction class attributes and methods

# UML2WithID_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UML2WithID_WriteStructuralFeatureAction class attributes and methods

# UML2WithID_ClearStructuralFeatureAction class attributes and methods

# UML2WithID_FinalState class attributes and methods

# State class attributes and methods

# UML2WithID_CreateObjectAction class attributes and methods

# UML2WithID_DestroyObjectAction class attributes and methods
UML2WithID_DestroyObjectAction_isDestroyLinks: Property = Property(name="isDestroyLinks", type=BooleanType)
UML2WithID_DestroyObjectAction_isDestroyOwnedObjects: Property = Property(name="isDestroyOwnedObjects", type=BooleanType)
UML2WithID_DestroyObjectAction.attributes={UML2WithID_DestroyObjectAction_isDestroyLinks, UML2WithID_DestroyObjectAction_isDestroyOwnedObjects}

# UML2WithID_TestIdentityAction class attributes and methods

# UML2WithID_LinkEndCreationData class attributes and methods
UML2WithID_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2WithID_LinkEndCreationData.attributes={UML2WithID_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# UML2WithID_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UML2WithID_WriteLinkAction class attributes and methods

# UML2WithID_DestroyLinkAction class attributes and methods

# UML2WithID_ClearAssociationAction class attributes and methods

# UML2WithID_VariableAction class attributes and methods

# UML2WithID_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# UML2WithID_RemoveStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# UML2WithID_AddStructuralFeatureValueAction class attributes and methods
UML2WithID_AddStructuralFeatureValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2WithID_AddStructuralFeatureValueAction.attributes={UML2WithID_AddStructuralFeatureValueAction_isReplaceAll}

# UML2WithID_LinkAction class attributes and methods

# UML2WithID_LinkEndData class attributes and methods

# UML2WithID_QualifierValue class attributes and methods

# UML2WithID_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UML2WithID_CallAction class attributes and methods
UML2WithID_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=BooleanType)
UML2WithID_CallAction.attributes={UML2WithID_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# UML2WithID_InvocationAction class attributes and methods

# UML2WithID_SendSignalAction class attributes and methods

# UML2WithID_BroadcastSignalAction class attributes and methods

# UML2WithID_WriteVariableAction class attributes and methods

# UML2WithID_ClearVariableAction class attributes and methods

# UML2WithID_AddVariableValueAction class attributes and methods
UML2WithID_AddVariableValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2WithID_AddVariableValueAction.attributes={UML2WithID_AddVariableValueAction_isReplaceAll}

# WriteVariableAction class attributes and methods

# UML2WithID_RemoveVariableValueAction class attributes and methods

# UML2WithID_ApplyFunctionAction class attributes and methods

# UML2WithID_PrimitiveFunction class attributes and methods
UML2WithID_PrimitiveFunction_body: Property = Property(name="body", type=StringType)
UML2WithID_PrimitiveFunction_language: Property = Property(name="language", type=StringType)
UML2WithID_PrimitiveFunction.attributes={UML2WithID_PrimitiveFunction_body, UML2WithID_PrimitiveFunction_language}

# UML2WithID_Duration class attributes and methods
UML2WithID_Duration_firstTime: Property = Property(name="firstTime", type=BooleanType)
UML2WithID_Duration.attributes={UML2WithID_Duration_firstTime}

# UML2WithID_TimeObservationAction class attributes and methods

# UML2WithID_DurationInterval class attributes and methods

# Interval class attributes and methods

# UML2WithID_Interval class attributes and methods

# UML2WithID_TimeConstraint class attributes and methods

# IntervalConstraint class attributes and methods

# UML2WithID_IntervalConstraint class attributes and methods

# UML2WithID_TimeInterval class attributes and methods

# UML2WithID_SendObjectAction class attributes and methods

# UML2WithID_CallOperationAction class attributes and methods

# CallAction class attributes and methods

# UML2WithID_CallBehaviorAction class attributes and methods

# UML2WithID_TimeExpression class attributes and methods
UML2WithID_TimeExpression_firstTime: Property = Property(name="firstTime", type=BooleanType)
UML2WithID_TimeExpression.attributes={UML2WithID_TimeExpression_firstTime}

# UML2WithID_Deployment class attributes and methods

# UML2WithID_DeployedArtifact class attributes and methods

# UML2WithID_DurationObservationAction class attributes and methods

# UML2WithID_DurationConstraint class attributes and methods

# UML2WithID_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2WithID_ProtocolConformance class attributes and methods

# StateMachine class attributes and methods

# UML2WithID_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# UML2WithID_ReadExtentAction class attributes and methods

# UML2WithID_DeploymentTarget class attributes and methods

# UML2WithID_DeploymentSpecification class attributes and methods
UML2WithID_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
UML2WithID_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
UML2WithID_DeploymentSpecification.attributes={UML2WithID_DeploymentSpecification_executionLocation, UML2WithID_DeploymentSpecification_deploymentLocation}

# UML2WithID_Node class attributes and methods

# UML2WithID_Device class attributes and methods

# Node class attributes and methods

# UML2WithID_ExecutionEnvironment class attributes and methods

# UML2WithID_CommunicationPath class attributes and methods

# UML2WithID_StartOwnedBehaviorAction class attributes and methods

# UML2WithID_ReadLinkObjectEndAction class attributes and methods

# UML2WithID_ReclassifyObjectAction class attributes and methods
UML2WithID_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2WithID_ReclassifyObjectAction.attributes={UML2WithID_ReclassifyObjectAction_isReplaceAll}

# UML2WithID_ReadIsClassifiedObjectAction class attributes and methods
UML2WithID_ReadIsClassifiedObjectAction_isDirect: Property = Property(name="isDirect", type=BooleanType)
UML2WithID_ReadIsClassifiedObjectAction.attributes={UML2WithID_ReadIsClassifiedObjectAction_isDirect}

# UML2WithID_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UML2WithID_ReplyAction class attributes and methods

# UML2WithID_ReadLinkObjectEndQualifierAction class attributes and methods

# UML2WithID_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UML2WithID_AcceptEventAction class attributes and methods

# UML2WithID_RaiseExceptionAction class attributes and methods

# Artifact class attributes and methods

# Relationships
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Element", type=UML2WithID_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=UML2WithID_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Element4", type=UML2WithID_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=UML2WithID_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="UML2WithID_Comment", type=UML2WithID_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Element", type=UML2WithID_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperValue6: BinaryAssociation = BinaryAssociation(
    name="upperValue6",
    ends={
        Property(name="UML2WithID_ValueSpecification", type=UML2WithID_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_MultiplicityElement", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue7: BinaryAssociation = BinaryAssociation(
    name="lowerValue7",
    ends={
        Property(name="UML2WithID_ValueSpecification9", type=UML2WithID_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_MultiplicityElement8", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clientDependency10: BinaryAssociation = BinaryAssociation(
    name="clientDependency10",
    ends={
        Property(name="Dependency", type=UML2WithID_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=UML2WithID_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
nameExpression11: BinaryAssociation = BinaryAssociation(
    name="nameExpression11",
    ends={
        Property(name="UML2WithID_StringExpression", type=UML2WithID_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_NamedElement", type=UML2WithID_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="UML2WithID_NamedElement13", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Namespace", type=UML2WithID_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRule14: BinaryAssociation = BinaryAssociation(
    name="ownedRule14",
    ends={
        Property(name="Constraint", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember15: BinaryAssociation = BinaryAssociation(
    name="importedMember15",
    ends={
        Property(name="UML2WithID_PackageableElement", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Namespace16", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport17: BinaryAssociation = BinaryAssociation(
    name="elementImport17",
    ends={
        Property(name="ElementImport", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=UML2WithID_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport18: BinaryAssociation = BinaryAssociation(
    name="packageImport18",
    ends={
        Property(name="PackageImport", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace19", type=UML2WithID_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result20: BinaryAssociation = BinaryAssociation(
    name="result20",
    ends={
        Property(name="UML2WithID_Parameter", type=UML2WithID_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_OpaqueExpression", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior21: BinaryAssociation = BinaryAssociation(
    name="behavior21",
    ends={
        Property(name="UML2WithID_Behavior", type=UML2WithID_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_OpaqueExpression22", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
class_47: BinaryAssociation = BinaryAssociation(
    name="class_47",
    ends={
        Property(name="UML2WithID_Property", type=UML2WithID_Class, multiplicity=Multiplicity(0, 1)),
        Property(name="UML2WithID_Class48", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1))
    }
)
operand23: BinaryAssociation = BinaryAssociation(
    name="operand23",
    ends={
        Property(name="UML2WithID_ValueSpecification24", type=UML2WithID_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Expression", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement25: BinaryAssociation = BinaryAssociation(
    name="annotatedElement25",
    ends={
        Property(name="UML2WithID_Element27", type=UML2WithID_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Comment26", type=UML2WithID_Element, multiplicity=Multiplicity(0, 9999))
    }
)
bodyExpression28: BinaryAssociation = BinaryAssociation(
    name="bodyExpression28",
    ends={
        Property(name="UML2WithID_StringExpression30", type=UML2WithID_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Comment29", type=UML2WithID_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="UML2WithID_Element32", type=UML2WithID_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DirectedRelationship", type=UML2WithID_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="UML2WithID_Element35", type=UML2WithID_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DirectedRelationship34", type=UML2WithID_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement36: BinaryAssociation = BinaryAssociation(
    name="relatedElement36",
    ends={
        Property(name="UML2WithID_Element37", type=UML2WithID_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Relationship", type=UML2WithID_Element, multiplicity=Multiplicity(1, 9999))
    }
)
ownedOperation38: BinaryAssociation = BinaryAssociation(
    name="ownedOperation38",
    ends={
        Property(name="Operation", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass40: BinaryAssociation = BinaryAssociation(
    name="superClass40",
    ends={
        Property(name="UML2WithID_Class", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Class39", type=UML2WithID_Class, multiplicity=Multiplicity(0, 9999))
    }
)
extension41: BinaryAssociation = BinaryAssociation(
    name="extension41",
    ends={
        Property(name="Extension", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="metaclass", type=UML2WithID_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier42: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier42",
    ends={
        Property(name="UML2WithID_Classifier", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Class43", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception44: BinaryAssociation = BinaryAssociation(
    name="ownedReception44",
    ends={
        Property(name="UML2WithID_Reception", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Class45", type=UML2WithID_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package46: BinaryAssociation = BinaryAssociation(
    name="package46",
    ends={
        Property(name="Package", type=UML2WithID_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=UML2WithID_Package, multiplicity=Multiplicity(0, 1))
    }
)
opposite50: BinaryAssociation = BinaryAssociation(
    name="opposite50",
    ends={
        Property(name="UML2WithID_Property51", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Property49", type=UML2WithID_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation52: BinaryAssociation = BinaryAssociation(
    name="owningAssociation52",
    ends={
        Property(name="Association", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=UML2WithID_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty54: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty54",
    ends={
        Property(name="UML2WithID_Property55", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Property53", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty57: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty57",
    ends={
        Property(name="UML2WithID_Property58", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Property56", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999))
    }
)
datatype59: BinaryAssociation = BinaryAssociation(
    name="datatype59",
    ends={
        Property(name="DataType", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=UML2WithID_DataType, multiplicity=Multiplicity(0, 1))
    }
)
association60: BinaryAssociation = BinaryAssociation(
    name="association60",
    ends={
        Property(name="Association61", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=UML2WithID_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue62: BinaryAssociation = BinaryAssociation(
    name="defaultValue62",
    ends={
        Property(name="UML2WithID_ValueSpecification64", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Property63", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier66: BinaryAssociation = BinaryAssociation(
    name="qualifier66",
    ends={
        Property(name="Property", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd68: BinaryAssociation = BinaryAssociation(
    name="associationEnd68",
    ends={
        Property(name="Property69", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=UML2WithID_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter70: BinaryAssociation = BinaryAssociation(
    name="ownedParameter70",
    ends={
        Property(name="Parameter", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_71: BinaryAssociation = BinaryAssociation(
    name="class_71",
    ends={
        Property(name="Class", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=UML2WithID_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype72: BinaryAssociation = BinaryAssociation(
    name="datatype72",
    ends={
        Property(name="DataType74", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation73", type=UML2WithID_DataType, multiplicity=Multiplicity(0, 1))
    }
)
precondition75: BinaryAssociation = BinaryAssociation(
    name="precondition75",
    ends={
        Property(name="UML2WithID_Constraint", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Operation", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition76: BinaryAssociation = BinaryAssociation(
    name="postcondition76",
    ends={
        Property(name="UML2WithID_Constraint78", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Operation77", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation80: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation80",
    ends={
        Property(name="UML2WithID_Operation81", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Operation79", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
bodyCondition82: BinaryAssociation = BinaryAssociation(
    name="bodyCondition82",
    ends={
        Property(name="UML2WithID_Constraint84", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Operation83", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="UML2WithID_Type", type=UML2WithID_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TypedElement", type=UML2WithID_Type, multiplicity=Multiplicity(0, 1))
    }
)
operation86: BinaryAssociation = BinaryAssociation(
    name="operation86",
    ends={
        Property(name="Operation87", type=UML2WithID_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue88: BinaryAssociation = BinaryAssociation(
    name="defaultValue88",
    ends={
        Property(name="UML2WithID_ValueSpecification90", type=UML2WithID_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Parameter89", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterSet91: BinaryAssociation = BinaryAssociation(
    name="parameterSet91",
    ends={
        Property(name="ParameterSet", type=UML2WithID_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=UML2WithID_ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage93: BinaryAssociation = BinaryAssociation(
    name="nestedPackage93",
    ends={
        Property(name="Package94", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=UML2WithID_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage96: BinaryAssociation = BinaryAssociation(
    name="nestingPackage96",
    ends={
        Property(name="Package97", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=UML2WithID_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType98: BinaryAssociation = BinaryAssociation(
    name="ownedType98",
    ends={
        Property(name="Type", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=UML2WithID_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember99: BinaryAssociation = BinaryAssociation(
    name="ownedMember99",
    ends={
        Property(name="UML2WithID_PackageableElement100", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Package", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge101: BinaryAssociation = BinaryAssociation(
    name="packageMerge101",
    ends={
        Property(name="PackageMerge", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="mergingPackage", type=UML2WithID_PackageMerge, multiplicity=Multiplicity(0, 9999))
    }
)
appliedProfile102: BinaryAssociation = BinaryAssociation(
    name="appliedProfile102",
    ends={
        Property(name="UML2WithID_ProfileApplication", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Package103", type=UML2WithID_ProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
packageExtension104: BinaryAssociation = BinaryAssociation(
    name="packageExtension104",
    ends={
        Property(name="UML2WithID_PackageMerge", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Package105", type=UML2WithID_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral106: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral106",
    ends={
        Property(name="EnumerationLiteral", type=UML2WithID_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=UML2WithID_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute107: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute107",
    ends={
        Property(name="Property108", type=UML2WithID_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation109: BinaryAssociation = BinaryAssociation(
    name="ownedOperation109",
    ends={
        Property(name="Operation111", type=UML2WithID_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype110", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration112: BinaryAssociation = BinaryAssociation(
    name="enumeration112",
    ends={
        Property(name="Enumeration", type=UML2WithID_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=UML2WithID_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
feature113: BinaryAssociation = BinaryAssociation(
    name="feature113",
    ends={
        Property(name="Feature", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=UML2WithID_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember114: BinaryAssociation = BinaryAssociation(
    name="inheritedMember114",
    ends={
        Property(name="UML2WithID_NamedElement116", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier115", type=UML2WithID_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
general118: BinaryAssociation = BinaryAssociation(
    name="general118",
    ends={
        Property(name="UML2WithID_Classifier119", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier117", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization120: BinaryAssociation = BinaryAssociation(
    name="generalization120",
    ends={
        Property(name="Generalization", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=UML2WithID_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute121: BinaryAssociation = BinaryAssociation(
    name="attribute121",
    ends={
        Property(name="UML2WithID_Property123", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier122", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier125: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier125",
    ends={
        Property(name="UML2WithID_Classifier126", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier124", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
substitution127: BinaryAssociation = BinaryAssociation(
    name="substitution127",
    ends={
        Property(name="Substitution", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=UML2WithID_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent128: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent128",
    ends={
        Property(name="GeneralizationSet", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=UML2WithID_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUseCase129: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase129",
    ends={
        Property(name="UML2WithID_UseCase", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier130", type=UML2WithID_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase131: BinaryAssociation = BinaryAssociation(
    name="useCase131",
    ends={
        Property(name="UseCase", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=UML2WithID_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
representation132: BinaryAssociation = BinaryAssociation(
    name="representation132",
    ends={
        Property(name="UML2WithID_CollaborationOccurrence", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier133", type=UML2WithID_CollaborationOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
occurrence134: BinaryAssociation = BinaryAssociation(
    name="occurrence134",
    ends={
        Property(name="UML2WithID_CollaborationOccurrence136", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier135", type=UML2WithID_CollaborationOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuringClassifier137: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier137",
    ends={
        Property(name="Classifier", type=UML2WithID_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context138: BinaryAssociation = BinaryAssociation(
    name="context138",
    ends={
        Property(name="UML2WithID_Namespace140", type=UML2WithID_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Constraint139", type=UML2WithID_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
namespace141: BinaryAssociation = BinaryAssociation(
    name="namespace141",
    ends={
        Property(name="Namespace", type=UML2WithID_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=UML2WithID_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
specification142: BinaryAssociation = BinaryAssociation(
    name="specification142",
    ends={
        Property(name="UML2WithID_ValueSpecification144", type=UML2WithID_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Constraint143", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedElement145: BinaryAssociation = BinaryAssociation(
    name="constrainedElement145",
    ends={
        Property(name="UML2WithID_Element147", type=UML2WithID_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Constraint146", type=UML2WithID_Element, multiplicity=Multiplicity(0, 9999))
    }
)
parameter148: BinaryAssociation = BinaryAssociation(
    name="parameter148",
    ends={
        Property(name="UML2WithID_Parameter149", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioralFeature", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
formalParameter150: BinaryAssociation = BinaryAssociation(
    name="formalParameter150",
    ends={
        Property(name="UML2WithID_Parameter152", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioralFeature151", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnResult153: BinaryAssociation = BinaryAssociation(
    name="returnResult153",
    ends={
        Property(name="UML2WithID_Parameter155", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioralFeature154", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException156: BinaryAssociation = BinaryAssociation(
    name="raisedException156",
    ends={
        Property(name="UML2WithID_Type158", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioralFeature157", type=UML2WithID_Type, multiplicity=Multiplicity(0, 9999))
    }
)
method159: BinaryAssociation = BinaryAssociation(
    name="method159",
    ends={
        Property(name="Behavior", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
slot160: BinaryAssociation = BinaryAssociation(
    name="slot160",
    ends={
        Property(name="Slot", type=UML2WithID_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=UML2WithID_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinitionContext173: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext173",
    ends={
        Property(name="UML2WithID_Classifier174", type=UML2WithID_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_RedefinableElement", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
classifier161: BinaryAssociation = BinaryAssociation(
    name="classifier161",
    ends={
        Property(name="UML2WithID_Classifier162", type=UML2WithID_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InstanceSpecification", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specification163: BinaryAssociation = BinaryAssociation(
    name="specification163",
    ends={
        Property(name="UML2WithID_ValueSpecification165", type=UML2WithID_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InstanceSpecification164", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningInstance166: BinaryAssociation = BinaryAssociation(
    name="owningInstance166",
    ends={
        Property(name="InstanceSpecification", type=UML2WithID_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=UML2WithID_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value167: BinaryAssociation = BinaryAssociation(
    name="value167",
    ends={
        Property(name="UML2WithID_ValueSpecification168", type=UML2WithID_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Slot", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature169: BinaryAssociation = BinaryAssociation(
    name="definingFeature169",
    ends={
        Property(name="UML2WithID_StructuralFeature", type=UML2WithID_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Slot170", type=UML2WithID_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
instance171: BinaryAssociation = BinaryAssociation(
    name="instance171",
    ends={
        Property(name="UML2WithID_InstanceSpecification172", type=UML2WithID_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InstanceValue", type=UML2WithID_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
mergingPackage196: BinaryAssociation = BinaryAssociation(
    name="mergingPackage196",
    ends={
        Property(name="Package197", type=UML2WithID_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage198: BinaryAssociation = BinaryAssociation(
    name="mergedPackage198",
    ends={
        Property(name="UML2WithID_Package200", type=UML2WithID_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_PackageMerge199", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1))
    }
)
specific175: BinaryAssociation = BinaryAssociation(
    name="specific175",
    ends={
        Property(name="Classifier176", type=UML2WithID_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
general177: BinaryAssociation = BinaryAssociation(
    name="general177",
    ends={
        Property(name="UML2WithID_Classifier178", type=UML2WithID_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Generalization", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet179: BinaryAssociation = BinaryAssociation(
    name="generalizationSet179",
    ends={
        Property(name="GeneralizationSet181", type=UML2WithID_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization180", type=UML2WithID_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement182: BinaryAssociation = BinaryAssociation(
    name="importedElement182",
    ends={
        Property(name="UML2WithID_PackageableElement183", type=UML2WithID_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ElementImport", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace184: BinaryAssociation = BinaryAssociation(
    name="importingNamespace184",
    ends={
        Property(name="Namespace185", type=UML2WithID_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage186: BinaryAssociation = BinaryAssociation(
    name="importedPackage186",
    ends={
        Property(name="UML2WithID_Package187", type=UML2WithID_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_PackageImport", type=UML2WithID_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace188: BinaryAssociation = BinaryAssociation(
    name="importingNamespace188",
    ends={
        Property(name="Namespace189", type=UML2WithID_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=UML2WithID_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
ownedEnd190: BinaryAssociation = BinaryAssociation(
    name="ownedEnd190",
    ends={
        Property(name="Property191", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endType192: BinaryAssociation = BinaryAssociation(
    name="endType192",
    ends={
        Property(name="UML2WithID_Type193", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Association", type=UML2WithID_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd194: BinaryAssociation = BinaryAssociation(
    name="memberEnd194",
    ends={
        Property(name="Property195", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML2WithID_Property, multiplicity=Multiplicity(2, 9999))
    }
)
redefinedBehavior215: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior215",
    ends={
        Property(name="UML2WithID_Behavior216", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior214", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification217: BinaryAssociation = BinaryAssociation(
    name="specification217",
    ends={
        Property(name="BehavioralFeature", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
parameter218: BinaryAssociation = BinaryAssociation(
    name="parameter218",
    ends={
        Property(name="UML2WithID_Parameter220", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior219", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameter221: BinaryAssociation = BinaryAssociation(
    name="formalParameter221",
    ends={
        Property(name="UML2WithID_Parameter223", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior222", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStereotype201: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype201",
    ends={
        Property(name="UML2WithID_Stereotype", type=UML2WithID_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Profile", type=UML2WithID_Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
returnResult224: BinaryAssociation = BinaryAssociation(
    name="returnResult224",
    ends={
        Property(name="UML2WithID_Parameter226", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior225", type=UML2WithID_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
precondition227: BinaryAssociation = BinaryAssociation(
    name="precondition227",
    ends={
        Property(name="UML2WithID_Constraint229", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior228", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
metaclassReference202: BinaryAssociation = BinaryAssociation(
    name="metaclassReference202",
    ends={
        Property(name="UML2WithID_ElementImport204", type=UML2WithID_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Profile203", type=UML2WithID_ElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition230: BinaryAssociation = BinaryAssociation(
    name="postcondition230",
    ends={
        Property(name="UML2WithID_Constraint232", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior231", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference205: BinaryAssociation = BinaryAssociation(
    name="metamodelReference205",
    ends={
        Property(name="UML2WithID_PackageImport207", type=UML2WithID_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Profile206", type=UML2WithID_PackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
importedProfile208: BinaryAssociation = BinaryAssociation(
    name="importedProfile208",
    ends={
        Property(name="UML2WithID_Profile210", type=UML2WithID_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ProfileApplication209", type=UML2WithID_Profile, multiplicity=Multiplicity(1, 1))
    }
)
metaclass211: BinaryAssociation = BinaryAssociation(
    name="metaclass211",
    ends={
        Property(name="Class212", type=UML2WithID_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=UML2WithID_Class, multiplicity=Multiplicity(1, 1))
    }
)
context213: BinaryAssociation = BinaryAssociation(
    name="context213",
    ends={
        Property(name="BehavioredClassifier", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBehavior", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
action247: BinaryAssociation = BinaryAssociation(
    name="action247",
    ends={
        Property(name="UML2WithID_Action", type=UML2WithID_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Activity", type=UML2WithID_Action, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode248: BinaryAssociation = BinaryAssociation(
    name="structuredNode248",
    ends={
        Property(name="UML2WithID_StructuredActivityNode", type=UML2WithID_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Activity249", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
client250: BinaryAssociation = BinaryAssociation(
    name="client250",
    ends={
        Property(name="NamedElement", type=UML2WithID_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=UML2WithID_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier251: BinaryAssociation = BinaryAssociation(
    name="supplier251",
    ends={
        Property(name="UML2WithID_NamedElement252", type=UML2WithID_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Dependency", type=UML2WithID_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameterSet233: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet233",
    ends={
        Property(name="UML2WithID_ParameterSet", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior234", type=UML2WithID_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior235: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior235",
    ends={
        Property(name="Behavior236", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior237: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior237",
    ends={
        Property(name="UML2WithID_Behavior238", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioredClassifier", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
implementation239: BinaryAssociation = BinaryAssociation(
    name="implementation239",
    ends={
        Property(name="Implementation", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=UML2WithID_Implementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTrigger240: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger240",
    ends={
        Property(name="UML2WithID_Trigger", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioredClassifier241", type=UML2WithID_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStateMachine242: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachine242",
    ends={
        Property(name="StateMachine", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_redefinitionContext", type=UML2WithID_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge243: BinaryAssociation = BinaryAssociation(
    name="edge243",
    ends={
        Property(name="ActivityEdge", type=UML2WithID_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group244: BinaryAssociation = BinaryAssociation(
    name="group244",
    ends={
        Property(name="ActivityGroup", type=UML2WithID_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityGroup_activity", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node245: BinaryAssociation = BinaryAssociation(
    name="node245",
    ends={
        Property(name="ActivityNode", type=UML2WithID_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity246", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
represented266: BinaryAssociation = BinaryAssociation(
    name="represented266",
    ends={
        Property(name="UML2WithID_Classifier267", type=UML2WithID_InformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InformationItem", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
realization268: BinaryAssociation = BinaryAssociation(
    name="realization268",
    ends={
        Property(name="UML2WithID_Relationship269", type=UML2WithID_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InformationFlow", type=UML2WithID_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed270: BinaryAssociation = BinaryAssociation(
    name="conveyed270",
    ends={
        Property(name="UML2WithID_Classifier272", type=UML2WithID_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InformationFlow271", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
definingEnd273: BinaryAssociation = BinaryAssociation(
    name="definingEnd273",
    ends={
        Property(name="UML2WithID_Property274", type=UML2WithID_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConnectorEnd", type=UML2WithID_Property, multiplicity=Multiplicity(0, 1))
    }
)
mapping253: BinaryAssociation = BinaryAssociation(
    name="mapping253",
    ends={
        Property(name="UML2WithID_OpaqueExpression254", type=UML2WithID_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Abstraction", type=UML2WithID_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstraction255: BinaryAssociation = BinaryAssociation(
    name="abstraction255",
    ends={
        Property(name="Component", type=UML2WithID_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="realization", type=UML2WithID_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier256: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier256",
    ends={
        Property(name="UML2WithID_Classifier257", type=UML2WithID_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Realization", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract258: BinaryAssociation = BinaryAssociation(
    name="contract258",
    ends={
        Property(name="UML2WithID_Classifier259", type=UML2WithID_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Substitution", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier260: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier260",
    ends={
        Property(name="Classifier261", type=UML2WithID_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
powertype262: BinaryAssociation = BinaryAssociation(
    name="powertype262",
    ends={
        Property(name="Classifier263", type=UML2WithID_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization264: BinaryAssociation = BinaryAssociation(
    name="generalization264",
    ends={
        Property(name="Generalization265", type=UML2WithID_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=UML2WithID_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector298: BinaryAssociation = BinaryAssociation(
    name="ownedConnector298",
    ends={
        Property(name="UML2WithID_Connector300", type=UML2WithID_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuredClassifier299", type=UML2WithID_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity301: BinaryAssociation = BinaryAssociation(
    name="activity301",
    ends={
        Property(name="Activity", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source302: BinaryAssociation = BinaryAssociation(
    name="source302",
    ends={
        Property(name="ActivityNode303", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target304: BinaryAssociation = BinaryAssociation(
    name="target304",
    ends={
        Property(name="ActivityNode305", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inGroup306: BinaryAssociation = BinaryAssociation(
    name="inGroup306",
    ends={
        Property(name="UML2WithID_ActivityGroup", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityEdge", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
guard307: BinaryAssociation = BinaryAssociation(
    name="guard307",
    ends={
        Property(name="UML2WithID_ValueSpecification309", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityEdge308", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
role275: BinaryAssociation = BinaryAssociation(
    name="role275",
    ends={
        Property(name="ConnectableElement", type=UML2WithID_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=UML2WithID_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
partWithPort276: BinaryAssociation = BinaryAssociation(
    name="partWithPort276",
    ends={
        Property(name="UML2WithID_Property278", type=UML2WithID_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConnectorEnd277", type=UML2WithID_Property, multiplicity=Multiplicity(0, 1))
    }
)
end279: BinaryAssociation = BinaryAssociation(
    name="end279",
    ends={
        Property(name="ConnectorEnd", type=UML2WithID_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=UML2WithID_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
type280: BinaryAssociation = BinaryAssociation(
    name="type280",
    ends={
        Property(name="UML2WithID_Association281", type=UML2WithID_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Connector", type=UML2WithID_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConnector283: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector283",
    ends={
        Property(name="UML2WithID_Connector284", type=UML2WithID_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Connector282", type=UML2WithID_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
end285: BinaryAssociation = BinaryAssociation(
    name="end285",
    ends={
        Property(name="UML2WithID_ConnectorEnd287", type=UML2WithID_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Connector286", type=UML2WithID_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract288: BinaryAssociation = BinaryAssociation(
    name="contract288",
    ends={
        Property(name="UML2WithID_Behavior290", type=UML2WithID_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Connector289", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute291: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute291",
    ends={
        Property(name="UML2WithID_Property292", type=UML2WithID_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuredClassifier", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part293: BinaryAssociation = BinaryAssociation(
    name="part293",
    ends={
        Property(name="UML2WithID_Property295", type=UML2WithID_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuredClassifier294", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999))
    }
)
role296: BinaryAssociation = BinaryAssociation(
    name="role296",
    ends={
        Property(name="UML2WithID_ConnectableElement", type=UML2WithID_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuredClassifier297", type=UML2WithID_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup329: BinaryAssociation = BinaryAssociation(
    name="inGroup329",
    ends={
        Property(name="UML2WithID_ActivityGroup330", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityNode", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
activity331: BinaryAssociation = BinaryAssociation(
    name="activity331",
    ends={
        Property(name="Activity332", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement334: BinaryAssociation = BinaryAssociation(
    name="redefinedElement334",
    ends={
        Property(name="UML2WithID_ActivityNode335", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityNode333", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode336: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode336",
    ends={
        Property(name="StructuredActivityNode337", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inPartition338: BinaryAssociation = BinaryAssociation(
    name="inPartition338",
    ends={
        Property(name="ActivityPartition340", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode339", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion341: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion341",
    ends={
        Property(name="InterruptibleActivityRegion343", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode342", type=UML2WithID_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
output344: BinaryAssociation = BinaryAssociation(
    name="output344",
    ends={
        Property(name="UML2WithID_OutputPin", type=UML2WithID_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Action345", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement311: BinaryAssociation = BinaryAssociation(
    name="redefinedElement311",
    ends={
        Property(name="UML2WithID_ActivityEdge312", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityEdge310", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode313: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode313",
    ends={
        Property(name="StructuredActivityNode", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inPartition314: BinaryAssociation = BinaryAssociation(
    name="inPartition314",
    ends={
        Property(name="ActivityPartition", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge315", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
weight316: BinaryAssociation = BinaryAssociation(
    name="weight316",
    ends={
        Property(name="UML2WithID_ValueSpecification318", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityEdge317", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts319: BinaryAssociation = BinaryAssociation(
    name="interrupts319",
    ends={
        Property(name="InterruptibleActivityRegion", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="interruptingEdge", type=UML2WithID_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
superGroup321: BinaryAssociation = BinaryAssociation(
    name="superGroup321",
    ends={
        Property(name="UML2WithID_ActivityGroup322", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityGroup320", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
activityGroup_activity323: BinaryAssociation = BinaryAssociation(
    name="activityGroup_activity323",
    ends={
        Property(name="Activity324", type=UML2WithID_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing325: BinaryAssociation = BinaryAssociation(
    name="outgoing325",
    ends={
        Property(name="ActivityEdge326", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming327: BinaryAssociation = BinaryAssociation(
    name="incoming327",
    ends={
        Property(name="ActivityEdge328", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
transformation364: BinaryAssociation = BinaryAssociation(
    name="transformation364",
    ends={
        Property(name="UML2WithID_Behavior365", type=UML2WithID_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ObjectFlow", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection366: BinaryAssociation = BinaryAssociation(
    name="selection366",
    ends={
        Property(name="UML2WithID_Behavior368", type=UML2WithID_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ObjectFlow367", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput369: BinaryAssociation = BinaryAssociation(
    name="decisionInput369",
    ends={
        Property(name="UML2WithID_Behavior370", type=UML2WithID_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DecisionNode", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
handler371: BinaryAssociation = BinaryAssociation(
    name="handler371",
    ends={
        Property(name="ExceptionHandler", type=UML2WithID_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedNode", type=UML2WithID_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input346: BinaryAssociation = BinaryAssociation(
    name="input346",
    ends={
        Property(name="UML2WithID_InputPin", type=UML2WithID_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Action347", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context_348: BinaryAssociation = BinaryAssociation(
    name="context_348",
    ends={
        Property(name="UML2WithID_Classifier350", type=UML2WithID_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Action349", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
localPrecondition351: BinaryAssociation = BinaryAssociation(
    name="localPrecondition351",
    ends={
        Property(name="UML2WithID_Constraint353", type=UML2WithID_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Action352", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition354: BinaryAssociation = BinaryAssociation(
    name="localPostcondition354",
    ends={
        Property(name="UML2WithID_Constraint356", type=UML2WithID_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Action355", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperBound357: BinaryAssociation = BinaryAssociation(
    name="upperBound357",
    ends={
        Property(name="UML2WithID_ValueSpecification358", type=UML2WithID_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ObjectNode", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inState359: BinaryAssociation = BinaryAssociation(
    name="inState359",
    ends={
        Property(name="UML2WithID_State", type=UML2WithID_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ObjectNode360", type=UML2WithID_State, multiplicity=Multiplicity(0, 9999))
    }
)
selection361: BinaryAssociation = BinaryAssociation(
    name="selection361",
    ends={
        Property(name="UML2WithID_Behavior363", type=UML2WithID_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ObjectNode362", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
contract392: BinaryAssociation = BinaryAssociation(
    name="contract392",
    ends={
        Property(name="UML2WithID_Interface393", type=UML2WithID_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Implementation", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier394: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier394",
    ends={
        Property(name="BehavioredClassifier395", type=UML2WithID_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementation", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
nestedArtifact397: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact397",
    ends={
        Property(name="UML2WithID_Artifact", type=UML2WithID_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Artifact396", type=UML2WithID_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation398: BinaryAssociation = BinaryAssociation(
    name="manifestation398",
    ends={
        Property(name="UML2WithID_Manifestation", type=UML2WithID_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Artifact399", type=UML2WithID_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation400: BinaryAssociation = BinaryAssociation(
    name="ownedOperation400",
    ends={
        Property(name="UML2WithID_Operation402", type=UML2WithID_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Artifact401", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute403: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute403",
    ends={
        Property(name="UML2WithID_Property405", type=UML2WithID_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Artifact404", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter372: BinaryAssociation = BinaryAssociation(
    name="parameter372",
    ends={
        Property(name="UML2WithID_Parameter373", type=UML2WithID_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityParameterNode", type=UML2WithID_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value374: BinaryAssociation = BinaryAssociation(
    name="value374",
    ends={
        Property(name="UML2WithID_ValueSpecification375", type=UML2WithID_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ValuePin", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedAttribute376: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute376",
    ends={
        Property(name="UML2WithID_Property377", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation378: BinaryAssociation = BinaryAssociation(
    name="ownedOperation378",
    ends={
        Property(name="UML2WithID_Operation380", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface379", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedInterface382: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface382",
    ends={
        Property(name="UML2WithID_Interface383", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface381", type=UML2WithID_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier384: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier384",
    ends={
        Property(name="UML2WithID_Classifier386", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface385", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception387: BinaryAssociation = BinaryAssociation(
    name="ownedReception387",
    ends={
        Property(name="UML2WithID_Reception389", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface388", type=UML2WithID_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol390: BinaryAssociation = BinaryAssociation(
    name="protocol390",
    ends={
        Property(name="UML2WithID_ProtocolStateMachine", type=UML2WithID_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interface391", type=UML2WithID_ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
useCase425: BinaryAssociation = BinaryAssociation(
    name="useCase425",
    ends={
        Property(name="UseCase426", type=UML2WithID_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase427: BinaryAssociation = BinaryAssociation(
    name="includingCase427",
    ends={
        Property(name="UseCase428", type=UML2WithID_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
addition429: BinaryAssociation = BinaryAssociation(
    name="addition429",
    ends={
        Property(name="UML2WithID_UseCase430", type=UML2WithID_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Include", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
type431: BinaryAssociation = BinaryAssociation(
    name="type431",
    ends={
        Property(name="UML2WithID_Collaboration", type=UML2WithID_CollaborationOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CollaborationOccurrence432", type=UML2WithID_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding433: BinaryAssociation = BinaryAssociation(
    name="roleBinding433",
    ends={
        Property(name="UML2WithID_Dependency435", type=UML2WithID_CollaborationOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CollaborationOccurrence434", type=UML2WithID_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationRole436: BinaryAssociation = BinaryAssociation(
    name="collaborationRole436",
    ends={
        Property(name="UML2WithID_ConnectableElement438", type=UML2WithID_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Collaboration437", type=UML2WithID_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
utilizedElement406: BinaryAssociation = BinaryAssociation(
    name="utilizedElement406",
    ends={
        Property(name="UML2WithID_PackageableElement408", type=UML2WithID_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Manifestation407", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
extendedCase409: BinaryAssociation = BinaryAssociation(
    name="extendedCase409",
    ends={
        Property(name="UML2WithID_UseCase410", type=UML2WithID_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Extend", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension411: BinaryAssociation = BinaryAssociation(
    name="extension411",
    ends={
        Property(name="UseCase412", type=UML2WithID_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition413: BinaryAssociation = BinaryAssociation(
    name="condition413",
    ends={
        Property(name="UML2WithID_Constraint415", type=UML2WithID_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Extend414", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionLocation416: BinaryAssociation = BinaryAssociation(
    name="extensionLocation416",
    ends={
        Property(name="UML2WithID_ExtensionPoint", type=UML2WithID_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Extend417", type=UML2WithID_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
include418: BinaryAssociation = BinaryAssociation(
    name="include418",
    ends={
        Property(name="Include", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="includingCase", type=UML2WithID_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend419: BinaryAssociation = BinaryAssociation(
    name="extend419",
    ends={
        Property(name="Extend", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension420", type=UML2WithID_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint421: BinaryAssociation = BinaryAssociation(
    name="extensionPoint421",
    ends={
        Property(name="ExtensionPoint", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=UML2WithID_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject422: BinaryAssociation = BinaryAssociation(
    name="subject422",
    ends={
        Property(name="Classifier424", type=UML2WithID_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase423", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
port456: BinaryAssociation = BinaryAssociation(
    name="port456",
    ends={
        Property(name="UML2WithID_Port458", type=UML2WithID_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Trigger457", type=UML2WithID_Port, multiplicity=Multiplicity(0, 9999))
    }
)
signal459: BinaryAssociation = BinaryAssociation(
    name="signal459",
    ends={
        Property(name="UML2WithID_Signal", type=UML2WithID_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Reception460", type=UML2WithID_Signal, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute461: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute461",
    ends={
        Property(name="UML2WithID_Property463", type=UML2WithID_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Signal462", type=UML2WithID_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal464: BinaryAssociation = BinaryAssociation(
    name="signal464",
    ends={
        Property(name="UML2WithID_Signal465", type=UML2WithID_SignalTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_SignalTrigger", type=UML2WithID_Signal, multiplicity=Multiplicity(0, 9999))
    }
)
when466: BinaryAssociation = BinaryAssociation(
    name="when466",
    ends={
        Property(name="UML2WithID_ValueSpecification467", type=UML2WithID_TimeTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TimeTrigger", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
required439: BinaryAssociation = BinaryAssociation(
    name="required439",
    ends={
        Property(name="UML2WithID_Interface440", type=UML2WithID_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Port", type=UML2WithID_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort442: BinaryAssociation = BinaryAssociation(
    name="redefinedPort442",
    ends={
        Property(name="UML2WithID_Port443", type=UML2WithID_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Port441", type=UML2WithID_Port, multiplicity=Multiplicity(0, 9999))
    }
)
provided444: BinaryAssociation = BinaryAssociation(
    name="provided444",
    ends={
        Property(name="UML2WithID_Interface446", type=UML2WithID_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Port445", type=UML2WithID_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocol447: BinaryAssociation = BinaryAssociation(
    name="protocol447",
    ends={
        Property(name="UML2WithID_ProtocolStateMachine449", type=UML2WithID_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Port448", type=UML2WithID_ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
ownedPort450: BinaryAssociation = BinaryAssociation(
    name="ownedPort450",
    ends={
        Property(name="UML2WithID_Port451", type=UML2WithID_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_EncapsulatedClassifier", type=UML2WithID_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation452: BinaryAssociation = BinaryAssociation(
    name="operation452",
    ends={
        Property(name="UML2WithID_Operation453", type=UML2WithID_CallTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CallTrigger", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression454: BinaryAssociation = BinaryAssociation(
    name="changeExpression454",
    ends={
        Property(name="UML2WithID_ValueSpecification455", type=UML2WithID_ChangeTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ChangeTrigger", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result477: BinaryAssociation = BinaryAssociation(
    name="result477",
    ends={
        Property(name="UML2WithID_OutputPin479", type=UML2WithID_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConditionalNode478", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test480: BinaryAssociation = BinaryAssociation(
    name="test480",
    ends={
        Property(name="UML2WithID_ActivityNode482", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Clause481", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
body483: BinaryAssociation = BinaryAssociation(
    name="body483",
    ends={
        Property(name="UML2WithID_ActivityNode485", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Clause484", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause487: BinaryAssociation = BinaryAssociation(
    name="predecessorClause487",
    ends={
        Property(name="Clause", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=UML2WithID_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause489: BinaryAssociation = BinaryAssociation(
    name="successorClause489",
    ends={
        Property(name="Clause490", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=UML2WithID_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider491: BinaryAssociation = BinaryAssociation(
    name="decider491",
    ends={
        Property(name="UML2WithID_OutputPin493", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Clause492", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput494: BinaryAssociation = BinaryAssociation(
    name="bodyOutput494",
    ends={
        Property(name="UML2WithID_OutputPin496", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Clause495", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
scope468: BinaryAssociation = BinaryAssociation(
    name="scope468",
    ends={
        Property(name="StructuredActivityNode469", type=UML2WithID_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
variable470: BinaryAssociation = BinaryAssociation(
    name="variable470",
    ends={
        Property(name="Variable", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=UML2WithID_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedNode471: BinaryAssociation = BinaryAssociation(
    name="containedNode471",
    ends={
        Property(name="ActivityNode472", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedEdge473: BinaryAssociation = BinaryAssociation(
    name="containedEdge473",
    ends={
        Property(name="ActivityEdge475", type=UML2WithID_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode474", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause476: BinaryAssociation = BinaryAssociation(
    name="clause476",
    ends={
        Property(name="UML2WithID_Clause", type=UML2WithID_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConditionalNode", type=UML2WithID_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fragment523: BinaryAssociation = BinaryAssociation(
    name="fragment523",
    ends={
        Property(name="InteractionFragment", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingInteraction", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate524: BinaryAssociation = BinaryAssociation(
    name="formalGate524",
    ends={
        Property(name="UML2WithID_Gate", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interaction", type=UML2WithID_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered525: BinaryAssociation = BinaryAssociation(
    name="covered525",
    ends={
        Property(name="Lifeline526", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=UML2WithID_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering527: BinaryAssociation = BinaryAssociation(
    name="generalOrdering527",
    ends={
        Property(name="UML2WithID_GeneralOrdering", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionFragment", type=UML2WithID_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingInteraction528: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction528",
    ends={
        Property(name="Interaction", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment", type=UML2WithID_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
enclosingOperand529: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand529",
    ends={
        Property(name="InteractionOperand", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment530", type=UML2WithID_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
bodyPart497: BinaryAssociation = BinaryAssociation(
    name="bodyPart497",
    ends={
        Property(name="UML2WithID_ActivityNode498", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart499: BinaryAssociation = BinaryAssociation(
    name="setupPart499",
    ends={
        Property(name="UML2WithID_ActivityNode501", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode500", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
decider502: BinaryAssociation = BinaryAssociation(
    name="decider502",
    ends={
        Property(name="UML2WithID_OutputPin504", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode503", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test505: BinaryAssociation = BinaryAssociation(
    name="test505",
    ends={
        Property(name="UML2WithID_ActivityNode507", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode506", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
result508: BinaryAssociation = BinaryAssociation(
    name="result508",
    ends={
        Property(name="UML2WithID_OutputPin510", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode509", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable511: BinaryAssociation = BinaryAssociation(
    name="loopVariable511",
    ends={
        Property(name="UML2WithID_OutputPin513", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode512", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyOutput514: BinaryAssociation = BinaryAssociation(
    name="bodyOutput514",
    ends={
        Property(name="UML2WithID_OutputPin516", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode515", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput517: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput517",
    ends={
        Property(name="UML2WithID_InputPin519", type=UML2WithID_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LoopNode518", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeline520: BinaryAssociation = BinaryAssociation(
    name="lifeline520",
    ends={
        Property(name="Lifeline", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=UML2WithID_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message521: BinaryAssociation = BinaryAssociation(
    name="message521",
    ends={
        Property(name="Message", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction522", type=UML2WithID_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument552: BinaryAssociation = BinaryAssociation(
    name="argument552",
    ends={
        Property(name="UML2WithID_ValueSpecification554", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Message553", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
before555: BinaryAssociation = BinaryAssociation(
    name="before555",
    ends={
        Property(name="EventOccurrence", type=UML2WithID_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toAfter", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
after556: BinaryAssociation = BinaryAssociation(
    name="after556",
    ends={
        Property(name="EventOccurrence557", type=UML2WithID_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toBefore", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
receiveMessage558: BinaryAssociation = BinaryAssociation(
    name="receiveMessage558",
    ends={
        Property(name="Message559", type=UML2WithID_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="receiveEvent", type=UML2WithID_Message, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy531: BinaryAssociation = BinaryAssociation(
    name="coveredBy531",
    ends={
        Property(name="InteractionFragment532", type=UML2WithID_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
represents533: BinaryAssociation = BinaryAssociation(
    name="represents533",
    ends={
        Property(name="UML2WithID_ConnectableElement534", type=UML2WithID_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Lifeline", type=UML2WithID_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
interaction535: BinaryAssociation = BinaryAssociation(
    name="interaction535",
    ends={
        Property(name="Interaction536", type=UML2WithID_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="lifeline", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
selector537: BinaryAssociation = BinaryAssociation(
    name="selector537",
    ends={
        Property(name="UML2WithID_OpaqueExpression539", type=UML2WithID_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Lifeline538", type=UML2WithID_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs540: BinaryAssociation = BinaryAssociation(
    name="decomposedAs540",
    ends={
        Property(name="UML2WithID_PartDecomposition", type=UML2WithID_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Lifeline541", type=UML2WithID_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
receiveEvent542: BinaryAssociation = BinaryAssociation(
    name="receiveEvent542",
    ends={
        Property(name="MessageEnd", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="receiveMessage", type=UML2WithID_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent543: BinaryAssociation = BinaryAssociation(
    name="sendEvent543",
    ends={
        Property(name="MessageEnd544", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sendMessage", type=UML2WithID_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
connector545: BinaryAssociation = BinaryAssociation(
    name="connector545",
    ends={
        Property(name="UML2WithID_Connector546", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Message", type=UML2WithID_Connector, multiplicity=Multiplicity(0, 1))
    }
)
interaction547: BinaryAssociation = BinaryAssociation(
    name="interaction547",
    ends={
        Property(name="Interaction548", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
signature549: BinaryAssociation = BinaryAssociation(
    name="signature549",
    ends={
        Property(name="UML2WithID_NamedElement551", type=UML2WithID_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Message550", type=UML2WithID_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
parameter576: BinaryAssociation = BinaryAssociation(
    name="parameter576",
    ends={
        Property(name="UML2WithID_TemplateParameter", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateSignature", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameter577: BinaryAssociation = BinaryAssociation(
    name="ownedParameter577",
    ends={
        Property(name="TemplateParameter", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedSignature579: BinaryAssociation = BinaryAssociation(
    name="nestedSignature579",
    ends={
        Property(name="TemplateSignature", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingSignature", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
nestingSignature581: BinaryAssociation = BinaryAssociation(
    name="nestingSignature581",
    ends={
        Property(name="TemplateSignature582", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedSignature", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
template583: BinaryAssociation = BinaryAssociation(
    name="template583",
    ends={
        Property(name="TemplateableElement", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=UML2WithID_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature584: BinaryAssociation = BinaryAssociation(
    name="signature584",
    ends={
        Property(name="TemplateSignature586", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter585", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
sendMessage560: BinaryAssociation = BinaryAssociation(
    name="sendMessage560",
    ends={
        Property(name="Message561", type=UML2WithID_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sendEvent", type=UML2WithID_Message, multiplicity=Multiplicity(0, 1))
    }
)
startExec562: BinaryAssociation = BinaryAssociation(
    name="startExec562",
    ends={
        Property(name="ExecutionOccurrence", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="start", type=UML2WithID_ExecutionOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
finishExec563: BinaryAssociation = BinaryAssociation(
    name="finishExec563",
    ends={
        Property(name="ExecutionOccurrence564", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="finish", type=UML2WithID_ExecutionOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
toAfter565: BinaryAssociation = BinaryAssociation(
    name="toAfter565",
    ends={
        Property(name="GeneralOrdering", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="before", type=UML2WithID_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
toBefore566: BinaryAssociation = BinaryAssociation(
    name="toBefore566",
    ends={
        Property(name="GeneralOrdering567", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="after", type=UML2WithID_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
start568: BinaryAssociation = BinaryAssociation(
    name="start568",
    ends={
        Property(name="EventOccurrence569", type=UML2WithID_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="startExec", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
finish570: BinaryAssociation = BinaryAssociation(
    name="finish570",
    ends={
        Property(name="EventOccurrence571", type=UML2WithID_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="finishExec", type=UML2WithID_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
behavior572: BinaryAssociation = BinaryAssociation(
    name="behavior572",
    ends={
        Property(name="UML2WithID_Behavior573", type=UML2WithID_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ExecutionOccurrence", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
invariant574: BinaryAssociation = BinaryAssociation(
    name="invariant574",
    ends={
        Property(name="UML2WithID_Constraint575", type=UML2WithID_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StateInvariant", type=UML2WithID_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningParameter605: BinaryAssociation = BinaryAssociation(
    name="owningParameter605",
    ends={
        Property(name="ownedParameteredElement", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(0, 1)),
        Property(name="TemplateParameter606", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
boundElement607: BinaryAssociation = BinaryAssociation(
    name="boundElement607",
    ends={
        Property(name="TemplateableElement608", type=UML2WithID_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=UML2WithID_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature609: BinaryAssociation = BinaryAssociation(
    name="signature609",
    ends={
        Property(name="UML2WithID_TemplateSignature610", type=UML2WithID_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateBinding", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution611: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution611",
    ends={
        Property(name="TemplateParameterSubstitution", type=UML2WithID_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding612", type=UML2WithID_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formal613: BinaryAssociation = BinaryAssociation(
    name="formal613",
    ends={
        Property(name="UML2WithID_TemplateParameter614", type=UML2WithID_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateParameterSubstitution", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
templateBinding615: BinaryAssociation = BinaryAssociation(
    name="templateBinding615",
    ends={
        Property(name="TemplateBinding616", type=UML2WithID_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=UML2WithID_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
actual617: BinaryAssociation = BinaryAssociation(
    name="actual617",
    ends={
        Property(name="UML2WithID_ParameterableElement619", type=UML2WithID_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateParameterSubstitution618", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(1, 9999))
    }
)
parameteredElement587: BinaryAssociation = BinaryAssociation(
    name="parameteredElement587",
    ends={
        Property(name="ParameterableElement", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement588: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement588",
    ends={
        Property(name="ParameterableElement589", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningParameter", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default590: BinaryAssociation = BinaryAssociation(
    name="default590",
    ends={
        Property(name="UML2WithID_ParameterableElement", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateParameter591", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault592: BinaryAssociation = BinaryAssociation(
    name="ownedDefault592",
    ends={
        Property(name="UML2WithID_ParameterableElement594", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateParameter593", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding595: BinaryAssociation = BinaryAssociation(
    name="templateBinding595",
    ends={
        Property(name="TemplateBinding", type=UML2WithID_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=UML2WithID_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature596: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature596",
    ends={
        Property(name="TemplateSignature597", type=UML2WithID_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=UML2WithID_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subExpression599: BinaryAssociation = BinaryAssociation(
    name="subExpression599",
    ends={
        Property(name="StringExpression", type=UML2WithID_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=UML2WithID_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningExpression601: BinaryAssociation = BinaryAssociation(
    name="owningExpression601",
    ends={
        Property(name="StringExpression602", type=UML2WithID_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=UML2WithID_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter603: BinaryAssociation = BinaryAssociation(
    name="templateParameter603",
    ends={
        Property(name="TemplateParameter604", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=UML2WithID_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
joinSpec623: BinaryAssociation = BinaryAssociation(
    name="joinSpec623",
    ends={
        Property(name="UML2WithID_ValueSpecification624", type=UML2WithID_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_JoinNode", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedActual620: BinaryAssociation = BinaryAssociation(
    name="ownedActual620",
    ends={
        Property(name="UML2WithID_ParameterableElement622", type=UML2WithID_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TemplateParameterSubstitution621", type=UML2WithID_ParameterableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgroup631: BinaryAssociation = BinaryAssociation(
    name="subgroup631",
    ends={
        Property(name="ActivityPartition632", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="superPartition", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition634: BinaryAssociation = BinaryAssociation(
    name="superPartition634",
    ends={
        Property(name="ActivityPartition635", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="subgroup", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents636: BinaryAssociation = BinaryAssociation(
    name="represents636",
    ends={
        Property(name="UML2WithID_Element637", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ActivityPartition", type=UML2WithID_Element, multiplicity=Multiplicity(0, 1))
    }
)
containedEdge625: BinaryAssociation = BinaryAssociation(
    name="containedEdge625",
    ends={
        Property(name="ActivityEdge626", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode627: BinaryAssociation = BinaryAssociation(
    name="containedNode627",
    ends={
        Property(name="ActivityNode629", type=UML2WithID_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition628", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
protectedNode644: BinaryAssociation = BinaryAssociation(
    name="protectedNode644",
    ends={
        Property(name="ExecutableNode", type=UML2WithID_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handler", type=UML2WithID_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
handlerBody645: BinaryAssociation = BinaryAssociation(
    name="handlerBody645",
    ends={
        Property(name="UML2WithID_ExecutableNode", type=UML2WithID_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ExceptionHandler", type=UML2WithID_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput646: BinaryAssociation = BinaryAssociation(
    name="exceptionInput646",
    ends={
        Property(name="UML2WithID_ObjectNode648", type=UML2WithID_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ExceptionHandler647", type=UML2WithID_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType649: BinaryAssociation = BinaryAssociation(
    name="exceptionType649",
    ends={
        Property(name="UML2WithID_Classifier651", type=UML2WithID_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ExceptionHandler650", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
refersTo652: BinaryAssociation = BinaryAssociation(
    name="refersTo652",
    ends={
        Property(name="UML2WithID_Interaction653", type=UML2WithID_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionOccurrence", type=UML2WithID_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
actualGate654: BinaryAssociation = BinaryAssociation(
    name="actualGate654",
    ends={
        Property(name="UML2WithID_Gate656", type=UML2WithID_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionOccurrence655", type=UML2WithID_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput638: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput638",
    ends={
        Property(name="ExpansionRegion", type=UML2WithID_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=UML2WithID_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput639: BinaryAssociation = BinaryAssociation(
    name="regionAsInput639",
    ends={
        Property(name="ExpansionRegion640", type=UML2WithID_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=UML2WithID_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
outputElement641: BinaryAssociation = BinaryAssociation(
    name="outputElement641",
    ends={
        Property(name="ExpansionNode", type=UML2WithID_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=UML2WithID_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement642: BinaryAssociation = BinaryAssociation(
    name="inputElement642",
    ends={
        Property(name="ExpansionNode643", type=UML2WithID_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=UML2WithID_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
operand669: BinaryAssociation = BinaryAssociation(
    name="operand669",
    ends={
        Property(name="UML2WithID_InteractionOperand670", type=UML2WithID_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CombinedFragment", type=UML2WithID_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cfragmentGate671: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate671",
    ends={
        Property(name="UML2WithID_Gate673", type=UML2WithID_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CombinedFragment672", type=UML2WithID_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region674: BinaryAssociation = BinaryAssociation(
    name="region674",
    ends={
        Property(name="Region", type=UML2WithID_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=UML2WithID_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
argument657: BinaryAssociation = BinaryAssociation(
    name="argument657",
    ends={
        Property(name="UML2WithID_InputPin659", type=UML2WithID_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionOccurrence658", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard660: BinaryAssociation = BinaryAssociation(
    name="guard660",
    ends={
        Property(name="UML2WithID_InteractionConstraint", type=UML2WithID_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionOperand", type=UML2WithID_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragment661: BinaryAssociation = BinaryAssociation(
    name="fragment661",
    ends={
        Property(name="InteractionFragment662", type=UML2WithID_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingOperand", type=UML2WithID_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minint663: BinaryAssociation = BinaryAssociation(
    name="minint663",
    ends={
        Property(name="UML2WithID_ValueSpecification665", type=UML2WithID_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionConstraint664", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxint666: BinaryAssociation = BinaryAssociation(
    name="maxint666",
    ends={
        Property(name="UML2WithID_ValueSpecification668", type=UML2WithID_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InteractionConstraint667", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachine690: BinaryAssociation = BinaryAssociation(
    name="submachine690",
    ends={
        Property(name="UML2WithID_StateMachine692", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State691", type=UML2WithID_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
connection693: BinaryAssociation = BinaryAssociation(
    name="connection693",
    ends={
        Property(name="UML2WithID_ConnectionPointReference", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State694", type=UML2WithID_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState696: BinaryAssociation = BinaryAssociation(
    name="redefinedState696",
    ends={
        Property(name="UML2WithID_State697", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State695", type=UML2WithID_State, multiplicity=Multiplicity(0, 1))
    }
)
deferrableTrigger698: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger698",
    ends={
        Property(name="UML2WithID_Trigger700", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State699", type=UML2WithID_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
region701: BinaryAssociation = BinaryAssociation(
    name="region701",
    ends={
        Property(name="Region702", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=UML2WithID_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry703: BinaryAssociation = BinaryAssociation(
    name="entry703",
    ends={
        Property(name="UML2WithID_Activity705", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State704", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectionPoint675: BinaryAssociation = BinaryAssociation(
    name="connectionPoint675",
    ends={
        Property(name="UML2WithID_Pseudostate", type=UML2WithID_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StateMachine", type=UML2WithID_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit706: BinaryAssociation = BinaryAssociation(
    name="exit706",
    ends={
        Property(name="UML2WithID_Activity708", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State707", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedStateMachine677: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine677",
    ends={
        Property(name="UML2WithID_StateMachine678", type=UML2WithID_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StateMachine676", type=UML2WithID_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine_redefinitionContext679: BinaryAssociation = BinaryAssociation(
    name="stateMachine_redefinitionContext679",
    ends={
        Property(name="BehavioredClassifier680", type=UML2WithID_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStateMachine", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subvertex681: BinaryAssociation = BinaryAssociation(
    name="subvertex681",
    ends={
        Property(name="Vertex", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=UML2WithID_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition682: BinaryAssociation = BinaryAssociation(
    name="transition682",
    ends={
        Property(name="Transition", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container683", type=UML2WithID_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine684: BinaryAssociation = BinaryAssociation(
    name="stateMachine684",
    ends={
        Property(name="StateMachine685", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=UML2WithID_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state686: BinaryAssociation = BinaryAssociation(
    name="state686",
    ends={
        Property(name="State", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region687", type=UML2WithID_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion689: BinaryAssociation = BinaryAssociation(
    name="extendedRegion689",
    ends={
        Property(name="UML2WithID_Region", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Region688", type=UML2WithID_Region, multiplicity=Multiplicity(0, 1))
    }
)
container729: BinaryAssociation = BinaryAssociation(
    name="container729",
    ends={
        Property(name="Region730", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=UML2WithID_Region, multiplicity=Multiplicity(1, 1))
    }
)
source731: BinaryAssociation = BinaryAssociation(
    name="source731",
    ends={
        Property(name="Vertex733", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing732", type=UML2WithID_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target734: BinaryAssociation = BinaryAssociation(
    name="target734",
    ends={
        Property(name="Vertex736", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming735", type=UML2WithID_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
redefinedTransition738: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition738",
    ends={
        Property(name="UML2WithID_Transition", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Transition737", type=UML2WithID_Transition, multiplicity=Multiplicity(0, 1))
    }
)
trigger739: BinaryAssociation = BinaryAssociation(
    name="trigger739",
    ends={
        Property(name="UML2WithID_Trigger741", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Transition740", type=UML2WithID_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
guard742: BinaryAssociation = BinaryAssociation(
    name="guard742",
    ends={
        Property(name="UML2WithID_Constraint744", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Transition743", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect745: BinaryAssociation = BinaryAssociation(
    name="effect745",
    ends={
        Property(name="UML2WithID_Activity747", type=UML2WithID_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Transition746", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity709: BinaryAssociation = BinaryAssociation(
    name="doActivity709",
    ends={
        Property(name="UML2WithID_Activity711", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State710", type=UML2WithID_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant712: BinaryAssociation = BinaryAssociation(
    name="stateInvariant712",
    ends={
        Property(name="UML2WithID_Constraint714", type=UML2WithID_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_State713", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container715: BinaryAssociation = BinaryAssociation(
    name="container715",
    ends={
        Property(name="Region716", type=UML2WithID_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=UML2WithID_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing717: BinaryAssociation = BinaryAssociation(
    name="outgoing717",
    ends={
        Property(name="Transition719", type=UML2WithID_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source718", type=UML2WithID_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming720: BinaryAssociation = BinaryAssociation(
    name="incoming720",
    ends={
        Property(name="Transition722", type=UML2WithID_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target721", type=UML2WithID_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry723: BinaryAssociation = BinaryAssociation(
    name="entry723",
    ends={
        Property(name="UML2WithID_Pseudostate725", type=UML2WithID_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConnectionPointReference724", type=UML2WithID_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit726: BinaryAssociation = BinaryAssociation(
    name="exit726",
    ends={
        Property(name="UML2WithID_Pseudostate728", type=UML2WithID_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ConnectionPointReference727", type=UML2WithID_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
second757: BinaryAssociation = BinaryAssociation(
    name="second757",
    ends={
        Property(name="UML2WithID_InputPin759", type=UML2WithID_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TestIdentityAction758", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result760: BinaryAssociation = BinaryAssociation(
    name="result760",
    ends={
        Property(name="UML2WithID_OutputPin762", type=UML2WithID_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TestIdentityAction761", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result763: BinaryAssociation = BinaryAssociation(
    name="result763",
    ends={
        Property(name="UML2WithID_OutputPin764", type=UML2WithID_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadSelfAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature765: BinaryAssociation = BinaryAssociation(
    name="structuralFeature765",
    ends={
        Property(name="UML2WithID_StructuralFeature766", type=UML2WithID_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuralFeatureAction", type=UML2WithID_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object767: BinaryAssociation = BinaryAssociation(
    name="object767",
    ends={
        Property(name="UML2WithID_InputPin769", type=UML2WithID_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StructuralFeatureAction768", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result770: BinaryAssociation = BinaryAssociation(
    name="result770",
    ends={
        Property(name="UML2WithID_OutputPin771", type=UML2WithID_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadStructuralFeatureAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value772: BinaryAssociation = BinaryAssociation(
    name="value772",
    ends={
        Property(name="UML2WithID_InputPin773", type=UML2WithID_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_WriteStructuralFeatureAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier748: BinaryAssociation = BinaryAssociation(
    name="classifier748",
    ends={
        Property(name="UML2WithID_Classifier749", type=UML2WithID_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CreateObjectAction", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result750: BinaryAssociation = BinaryAssociation(
    name="result750",
    ends={
        Property(name="UML2WithID_OutputPin752", type=UML2WithID_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CreateObjectAction751", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target753: BinaryAssociation = BinaryAssociation(
    name="target753",
    ends={
        Property(name="UML2WithID_InputPin754", type=UML2WithID_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DestroyObjectAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first755: BinaryAssociation = BinaryAssociation(
    name="first755",
    ends={
        Property(name="UML2WithID_InputPin756", type=UML2WithID_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TestIdentityAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result785: BinaryAssociation = BinaryAssociation(
    name="result785",
    ends={
        Property(name="UML2WithID_OutputPin786", type=UML2WithID_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt787: BinaryAssociation = BinaryAssociation(
    name="insertAt787",
    ends={
        Property(name="UML2WithID_InputPin788", type=UML2WithID_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LinkEndCreationData", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
object789: BinaryAssociation = BinaryAssociation(
    name="object789",
    ends={
        Property(name="UML2WithID_InputPin790", type=UML2WithID_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ClearAssociationAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association791: BinaryAssociation = BinaryAssociation(
    name="association791",
    ends={
        Property(name="UML2WithID_Association793", type=UML2WithID_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ClearAssociationAction792", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1))
    }
)
variable794: BinaryAssociation = BinaryAssociation(
    name="variable794",
    ends={
        Property(name="UML2WithID_Variable", type=UML2WithID_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_VariableAction", type=UML2WithID_Variable, multiplicity=Multiplicity(1, 1))
    }
)
result795: BinaryAssociation = BinaryAssociation(
    name="result795",
    ends={
        Property(name="UML2WithID_OutputPin796", type=UML2WithID_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadVariableAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt774: BinaryAssociation = BinaryAssociation(
    name="insertAt774",
    ends={
        Property(name="UML2WithID_InputPin775", type=UML2WithID_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_AddStructuralFeatureValueAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endData776: BinaryAssociation = BinaryAssociation(
    name="endData776",
    ends={
        Property(name="UML2WithID_LinkEndData", type=UML2WithID_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LinkAction", type=UML2WithID_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value777: BinaryAssociation = BinaryAssociation(
    name="value777",
    ends={
        Property(name="UML2WithID_InputPin779", type=UML2WithID_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LinkEndData778", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end780: BinaryAssociation = BinaryAssociation(
    name="end780",
    ends={
        Property(name="UML2WithID_Property782", type=UML2WithID_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LinkEndData781", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier783: BinaryAssociation = BinaryAssociation(
    name="qualifier783",
    ends={
        Property(name="UML2WithID_QualifierValue", type=UML2WithID_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_LinkEndData784", type=UML2WithID_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result805: BinaryAssociation = BinaryAssociation(
    name="result805",
    ends={
        Property(name="UML2WithID_OutputPin807", type=UML2WithID_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ApplyFunctionAction806", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result808: BinaryAssociation = BinaryAssociation(
    name="result808",
    ends={
        Property(name="UML2WithID_OutputPin809", type=UML2WithID_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CallAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument810: BinaryAssociation = BinaryAssociation(
    name="argument810",
    ends={
        Property(name="UML2WithID_InputPin811", type=UML2WithID_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InvocationAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onPort812: BinaryAssociation = BinaryAssociation(
    name="onPort812",
    ends={
        Property(name="UML2WithID_Port814", type=UML2WithID_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_InvocationAction813", type=UML2WithID_Port, multiplicity=Multiplicity(0, 1))
    }
)
target815: BinaryAssociation = BinaryAssociation(
    name="target815",
    ends={
        Property(name="UML2WithID_InputPin816", type=UML2WithID_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_SendSignalAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal817: BinaryAssociation = BinaryAssociation(
    name="signal817",
    ends={
        Property(name="UML2WithID_Signal819", type=UML2WithID_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_SendSignalAction818", type=UML2WithID_Signal, multiplicity=Multiplicity(1, 1))
    }
)
value797: BinaryAssociation = BinaryAssociation(
    name="value797",
    ends={
        Property(name="UML2WithID_InputPin798", type=UML2WithID_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_WriteVariableAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt799: BinaryAssociation = BinaryAssociation(
    name="insertAt799",
    ends={
        Property(name="UML2WithID_InputPin800", type=UML2WithID_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_AddVariableValueAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function801: BinaryAssociation = BinaryAssociation(
    name="function801",
    ends={
        Property(name="UML2WithID_PrimitiveFunction", type=UML2WithID_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ApplyFunctionAction", type=UML2WithID_PrimitiveFunction, multiplicity=Multiplicity(1, 1))
    }
)
argument802: BinaryAssociation = BinaryAssociation(
    name="argument802",
    ends={
        Property(name="UML2WithID_InputPin804", type=UML2WithID_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ApplyFunctionAction803", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event834: BinaryAssociation = BinaryAssociation(
    name="event834",
    ends={
        Property(name="UML2WithID_NamedElement835", type=UML2WithID_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TimeExpression", type=UML2WithID_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
event836: BinaryAssociation = BinaryAssociation(
    name="event836",
    ends={
        Property(name="UML2WithID_NamedElement837", type=UML2WithID_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Duration", type=UML2WithID_NamedElement, multiplicity=Multiplicity(0, 2))
    }
)
now838: BinaryAssociation = BinaryAssociation(
    name="now838",
    ends={
        Property(name="UML2WithID_TimeExpression839", type=UML2WithID_TimeObservationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_TimeObservationAction", type=UML2WithID_TimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
min840: BinaryAssociation = BinaryAssociation(
    name="min840",
    ends={
        Property(name="UML2WithID_ValueSpecification841", type=UML2WithID_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interval", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
max842: BinaryAssociation = BinaryAssociation(
    name="max842",
    ends={
        Property(name="UML2WithID_ValueSpecification844", type=UML2WithID_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Interval843", type=UML2WithID_ValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
signal820: BinaryAssociation = BinaryAssociation(
    name="signal820",
    ends={
        Property(name="UML2WithID_Signal821", type=UML2WithID_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BroadcastSignalAction", type=UML2WithID_Signal, multiplicity=Multiplicity(1, 1))
    }
)
target822: BinaryAssociation = BinaryAssociation(
    name="target822",
    ends={
        Property(name="UML2WithID_InputPin823", type=UML2WithID_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_SendObjectAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request824: BinaryAssociation = BinaryAssociation(
    name="request824",
    ends={
        Property(name="UML2WithID_InputPin826", type=UML2WithID_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_SendObjectAction825", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation827: BinaryAssociation = BinaryAssociation(
    name="operation827",
    ends={
        Property(name="UML2WithID_Operation828", type=UML2WithID_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CallOperationAction", type=UML2WithID_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target829: BinaryAssociation = BinaryAssociation(
    name="target829",
    ends={
        Property(name="UML2WithID_InputPin831", type=UML2WithID_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CallOperationAction830", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
behavior832: BinaryAssociation = BinaryAssociation(
    name="behavior832",
    ends={
        Property(name="UML2WithID_Behavior833", type=UML2WithID_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CallBehaviorAction", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
parameter851: BinaryAssociation = BinaryAssociation(
    name="parameter851",
    ends={
        Property(name="Parameter852", type=UML2WithID_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSet", type=UML2WithID_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
condition853: BinaryAssociation = BinaryAssociation(
    name="condition853",
    ends={
        Property(name="UML2WithID_Constraint855", type=UML2WithID_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ParameterSet854", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required856: BinaryAssociation = BinaryAssociation(
    name="required856",
    ends={
        Property(name="UML2WithID_Interface857", type=UML2WithID_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Component", type=UML2WithID_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided858: BinaryAssociation = BinaryAssociation(
    name="provided858",
    ends={
        Property(name="UML2WithID_Interface860", type=UML2WithID_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Component859", type=UML2WithID_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
realization861: BinaryAssociation = BinaryAssociation(
    name="realization861",
    ends={
        Property(name="Realization", type=UML2WithID_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="abstraction", type=UML2WithID_Realization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMember862: BinaryAssociation = BinaryAssociation(
    name="ownedMember862",
    ends={
        Property(name="UML2WithID_PackageableElement864", type=UML2WithID_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Component863", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedArtifact865: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact865",
    ends={
        Property(name="UML2WithID_DeployedArtifact", type=UML2WithID_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Deployment", type=UML2WithID_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
duration845: BinaryAssociation = BinaryAssociation(
    name="duration845",
    ends={
        Property(name="UML2WithID_Duration846", type=UML2WithID_DurationObservationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DurationObservationAction", type=UML2WithID_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge847: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge847",
    ends={
        Property(name="ActivityEdge848", type=UML2WithID_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="interrupts", type=UML2WithID_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode849: BinaryAssociation = BinaryAssociation(
    name="containedNode849",
    ends={
        Property(name="ActivityNode850", type=UML2WithID_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="inInterruptibleRegion", type=UML2WithID_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
specificMachine874: BinaryAssociation = BinaryAssociation(
    name="specificMachine874",
    ends={
        Property(name="ProtocolStateMachine", type=UML2WithID_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="conformance", type=UML2WithID_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine875: BinaryAssociation = BinaryAssociation(
    name="generalMachine875",
    ends={
        Property(name="UML2WithID_ProtocolStateMachine876", type=UML2WithID_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ProtocolConformance", type=UML2WithID_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
conformance877: BinaryAssociation = BinaryAssociation(
    name="conformance877",
    ends={
        Property(name="ProtocolConformance", type=UML2WithID_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="specificMachine", type=UML2WithID_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postCondition878: BinaryAssociation = BinaryAssociation(
    name="postCondition878",
    ends={
        Property(name="UML2WithID_Constraint879", type=UML2WithID_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ProtocolTransition", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred880: BinaryAssociation = BinaryAssociation(
    name="referred880",
    ends={
        Property(name="UML2WithID_Operation882", type=UML2WithID_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ProtocolTransition881", type=UML2WithID_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
preCondition883: BinaryAssociation = BinaryAssociation(
    name="preCondition883",
    ends={
        Property(name="UML2WithID_Constraint885", type=UML2WithID_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ProtocolTransition884", type=UML2WithID_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
result886: BinaryAssociation = BinaryAssociation(
    name="result886",
    ends={
        Property(name="UML2WithID_OutputPin887", type=UML2WithID_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadExtentAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location866: BinaryAssociation = BinaryAssociation(
    name="location866",
    ends={
        Property(name="DeploymentTarget", type=UML2WithID_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="deployment", type=UML2WithID_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
configuration867: BinaryAssociation = BinaryAssociation(
    name="configuration867",
    ends={
        Property(name="UML2WithID_DeploymentSpecification", type=UML2WithID_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Deployment868", type=UML2WithID_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployment869: BinaryAssociation = BinaryAssociation(
    name="deployment869",
    ends={
        Property(name="Deployment", type=UML2WithID_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=UML2WithID_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement870: BinaryAssociation = BinaryAssociation(
    name="deployedElement870",
    ends={
        Property(name="UML2WithID_PackageableElement871", type=UML2WithID_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_DeploymentTarget", type=UML2WithID_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
nestedNode873: BinaryAssociation = BinaryAssociation(
    name="nestedNode873",
    ends={
        Property(name="UML2WithID_Node", type=UML2WithID_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Node872", type=UML2WithID_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier899: BinaryAssociation = BinaryAssociation(
    name="classifier899",
    ends={
        Property(name="UML2WithID_Classifier900", type=UML2WithID_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadIsClassifiedObjectAction", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result901: BinaryAssociation = BinaryAssociation(
    name="result901",
    ends={
        Property(name="UML2WithID_OutputPin903", type=UML2WithID_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadIsClassifiedObjectAction902", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object904: BinaryAssociation = BinaryAssociation(
    name="object904",
    ends={
        Property(name="UML2WithID_InputPin906", type=UML2WithID_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadIsClassifiedObjectAction905", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object907: BinaryAssociation = BinaryAssociation(
    name="object907",
    ends={
        Property(name="UML2WithID_InputPin908", type=UML2WithID_StartOwnedBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_StartOwnedBehaviorAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier909: BinaryAssociation = BinaryAssociation(
    name="qualifier909",
    ends={
        Property(name="UML2WithID_Property911", type=UML2WithID_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_QualifierValue910", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1))
    }
)
value912: BinaryAssociation = BinaryAssociation(
    name="value912",
    ends={
        Property(name="UML2WithID_InputPin914", type=UML2WithID_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_QualifierValue913", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
object915: BinaryAssociation = BinaryAssociation(
    name="object915",
    ends={
        Property(name="UML2WithID_InputPin916", type=UML2WithID_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier888: BinaryAssociation = BinaryAssociation(
    name="classifier888",
    ends={
        Property(name="UML2WithID_Classifier890", type=UML2WithID_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadExtentAction889", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
oldClassifier891: BinaryAssociation = BinaryAssociation(
    name="oldClassifier891",
    ends={
        Property(name="UML2WithID_Classifier892", type=UML2WithID_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReclassifyObjectAction", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier893: BinaryAssociation = BinaryAssociation(
    name="newClassifier893",
    ends={
        Property(name="UML2WithID_Classifier895", type=UML2WithID_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReclassifyObjectAction894", type=UML2WithID_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object896: BinaryAssociation = BinaryAssociation(
    name="object896",
    ends={
        Property(name="UML2WithID_InputPin898", type=UML2WithID_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReclassifyObjectAction897", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger933: BinaryAssociation = BinaryAssociation(
    name="trigger933",
    ends={
        Property(name="UML2WithID_Trigger934", type=UML2WithID_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_AcceptEventAction", type=UML2WithID_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
result935: BinaryAssociation = BinaryAssociation(
    name="result935",
    ends={
        Property(name="UML2WithID_OutputPin937", type=UML2WithID_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_AcceptEventAction936", type=UML2WithID_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation938: BinaryAssociation = BinaryAssociation(
    name="returnInformation938",
    ends={
        Property(name="UML2WithID_OutputPin939", type=UML2WithID_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_AcceptCallAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
replyToCall940: BinaryAssociation = BinaryAssociation(
    name="replyToCall940",
    ends={
        Property(name="UML2WithID_CallTrigger941", type=UML2WithID_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReplyAction", type=UML2WithID_CallTrigger, multiplicity=Multiplicity(1, 1))
    }
)
replyValue942: BinaryAssociation = BinaryAssociation(
    name="replyValue942",
    ends={
        Property(name="UML2WithID_InputPin944", type=UML2WithID_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReplyAction943", type=UML2WithID_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation945: BinaryAssociation = BinaryAssociation(
    name="returnInformation945",
    ends={
        Property(name="UML2WithID_InputPin947", type=UML2WithID_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReplyAction946", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
end917: BinaryAssociation = BinaryAssociation(
    name="end917",
    ends={
        Property(name="UML2WithID_Property919", type=UML2WithID_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndAction918", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1))
    }
)
result920: BinaryAssociation = BinaryAssociation(
    name="result920",
    ends={
        Property(name="UML2WithID_OutputPin922", type=UML2WithID_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndAction921", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object923: BinaryAssociation = BinaryAssociation(
    name="object923",
    ends={
        Property(name="UML2WithID_InputPin924", type=UML2WithID_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndQualifierAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result925: BinaryAssociation = BinaryAssociation(
    name="result925",
    ends={
        Property(name="UML2WithID_OutputPin927", type=UML2WithID_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndQualifierAction926", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier928: BinaryAssociation = BinaryAssociation(
    name="qualifier928",
    ends={
        Property(name="UML2WithID_Property930", type=UML2WithID_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_ReadLinkObjectEndQualifierAction929", type=UML2WithID_Property, multiplicity=Multiplicity(1, 1))
    }
)
result931: BinaryAssociation = BinaryAssociation(
    name="result931",
    ends={
        Property(name="UML2WithID_OutputPin932", type=UML2WithID_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_CreateLinkObjectAction", type=UML2WithID_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception948: BinaryAssociation = BinaryAssociation(
    name="exception948",
    ends={
        Property(name="UML2WithID_InputPin949", type=UML2WithID_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_RaiseExceptionAction", type=UML2WithID_InputPin, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UML2WithID_MultiplicityElement_Element = Generalization(general=Element, specific=UML2WithID_MultiplicityElement)
gen_UML2WithID_NamedElement_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2WithID_NamedElement)
gen_UML2WithID_Namespace_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Namespace)
gen_UML2WithID_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_OpaqueExpression)
gen_UML2WithID_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_ValueSpecification)
gen_UML2WithID_ValueSpecification_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2WithID_ValueSpecification)
gen_UML2WithID_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2WithID_Expression)
gen_UML2WithID_Comment_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2WithID_Comment)
gen_UML2WithID_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UML2WithID_DirectedRelationship)
gen_UML2WithID_Relationship_Element = Generalization(general=Element, specific=UML2WithID_Relationship)
gen_UML2WithID_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Type_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Type)
gen_UML2WithID_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2WithID_Property)
gen_UML2WithID_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Property)
gen_UML2WithID_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_Property)
gen_UML2WithID_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Parameter)
gen_UML2WithID_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2WithID_Operation)
gen_UML2WithID_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_TypedElement)
gen_UML2WithID_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Parameter)
gen_UML2WithID_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_Parameter)
gen_UML2WithID_Package_Namespace = Generalization(general=Namespace, specific=UML2WithID_Package)
gen_UML2WithID_Package_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Package)
gen_UML2WithID_Enumeration_DataType = Generalization(general=DataType, specific=UML2WithID_Enumeration)
gen_UML2WithID_DataType_Classifier = Generalization(general=Classifier, specific=UML2WithID_DataType)
gen_UML2WithID_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=UML2WithID_EnumerationLiteral)
gen_UML2WithID_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2WithID_PrimitiveType)
gen_UML2WithID_Classifier_Namespace = Generalization(general=Namespace, specific=UML2WithID_Classifier)
gen_UML2WithID_Classifier_Type = Generalization(general=Type, specific=UML2WithID_Classifier)
gen_UML2WithID_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Classifier)
gen_UML2WithID_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Feature)
gen_UML2WithID_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Constraint)
gen_UML2WithID_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralBoolean)
gen_UML2WithID_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_LiteralSpecification)
gen_UML2WithID_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralString)
gen_UML2WithID_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralNull)
gen_UML2WithID_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralInteger)
gen_UML2WithID_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2WithID_LiteralUnlimitedNatural)
gen_UML2WithID_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_BehavioralFeature_Feature = Generalization(general=Feature, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_StructuralFeature_Feature = Generalization(general=Feature, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_StructuralFeature)
gen_UML2WithID_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2WithID_InstanceSpecification)
gen_UML2WithID_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_RedefinableElement)
gen_UML2WithID_Slot_Element = Generalization(general=Element, specific=UML2WithID_Slot)
gen_UML2WithID_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_InstanceValue)
gen_UML2WithID_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_Generalization)
gen_UML2WithID_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_PackageableElement)
gen_UML2WithID_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2WithID_PackageableElement)
gen_UML2WithID_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_ElementImport)
gen_UML2WithID_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_PackageImport)
gen_UML2WithID_Association_Classifier = Generalization(general=Classifier, specific=UML2WithID_Association)
gen_UML2WithID_Association_Relationship = Generalization(general=Relationship, specific=UML2WithID_Association)
gen_UML2WithID_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_PackageMerge)
gen_UML2WithID_Stereotype_Class = Generalization(general=Class_, specific=UML2WithID_Stereotype)
gen_UML2WithID_Profile_Package = Generalization(general=Package, specific=UML2WithID_Profile)
gen_UML2WithID_ProfileApplication_PackageImport = Generalization(general=PackageImport, specific=UML2WithID_ProfileApplication)
gen_UML2WithID_Extension_Association = Generalization(general=Association, specific=UML2WithID_Extension)
gen_UML2WithID_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_Behavior_Class = Generalization(general=Class_, specific=UML2WithID_Behavior)
gen_UML2WithID_Permission_Dependency = Generalization(general=Dependency, specific=UML2WithID_Permission)
gen_UML2WithID_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_Dependency)
gen_UML2WithID_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_Dependency)
gen_UML2WithID_Usage_Dependency = Generalization(general=Dependency, specific=UML2WithID_Usage)
gen_UML2WithID_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_Activity_Behavior = Generalization(general=Behavior, specific=UML2WithID_Activity)
gen_UML2WithID_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2WithID_InformationItem)
gen_UML2WithID_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_InformationFlow)
gen_UML2WithID_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_InformationFlow)
gen_UML2WithID_Model_Package = Generalization(general=Package, specific=UML2WithID_Model)
gen_UML2WithID_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_ConnectorEnd)
gen_UML2WithID_Abstraction_Dependency = Generalization(general=Dependency, specific=UML2WithID_Abstraction)
gen_UML2WithID_Realization_Abstraction = Generalization(general=Abstraction, specific=UML2WithID_Realization)
gen_UML2WithID_Substitution_Realization = Generalization(general=Realization, specific=UML2WithID_Substitution)
gen_UML2WithID_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_GeneralizationSet)
gen_UML2WithID_AssociationClass_Class = Generalization(general=Class_, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Association = Generalization(general=Association, specific=UML2WithID_AssociationClass)
gen_UML2WithID_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ActivityEdge)
gen_UML2WithID_ConnectableElement_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ConnectableElement)
gen_UML2WithID_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2WithID_ConnectableElement)
gen_UML2WithID_Connector_Feature = Generalization(general=Feature, specific=UML2WithID_Connector)
gen_UML2WithID_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_StructuredClassifier)
gen_UML2WithID_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=UML2WithID_Action)
gen_UML2WithID_ActivityGroup_Element = Generalization(general=Element, specific=UML2WithID_ActivityGroup)
gen_UML2WithID_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ActivityNode)
gen_UML2WithID_InitialNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_InitialNode)
gen_UML2WithID_FinalNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_FinalNode)
gen_UML2WithID_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2WithID_ActivityFinalNode)
gen_UML2WithID_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_DecisionNode)
gen_UML2WithID_MergeNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_MergeNode)
gen_UML2WithID_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ExecutableNode)
gen_UML2WithID_OutputPin_Pin = Generalization(general=Pin, specific=UML2WithID_OutputPin)
gen_UML2WithID_InputPin_Pin = Generalization(general=Pin, specific=UML2WithID_InputPin)
gen_UML2WithID_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ObjectNode)
gen_UML2WithID_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_ObjectNode)
gen_UML2WithID_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2WithID_ControlNode)
gen_UML2WithID_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2WithID_ControlFlow)
gen_UML2WithID_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2WithID_ObjectFlow)
gen_UML2WithID_Artifact_Classifier = Generalization(general=Classifier, specific=UML2WithID_Artifact)
gen_UML2WithID_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2WithID_Artifact)
gen_UML2WithID_Manifestation_Abstraction = Generalization(general=Abstraction, specific=UML2WithID_Manifestation)
gen_UML2WithID_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_Pin)
gen_UML2WithID_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_Pin)
gen_UML2WithID_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_ActivityParameterNode)
gen_UML2WithID_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2WithID_ValuePin)
gen_UML2WithID_Interface_Classifier = Generalization(general=Classifier, specific=UML2WithID_Interface)
gen_UML2WithID_Implementation_Realization = Generalization(general=Realization, specific=UML2WithID_Implementation)
gen_UML2WithID_Include_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Include)
gen_UML2WithID_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_Include)
gen_UML2WithID_CollaborationOccurrence_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_CollaborationOccurrence)
gen_UML2WithID_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Actor_Classifier = Generalization(general=Classifier, specific=UML2WithID_Actor)
gen_UML2WithID_Extend_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Extend)
gen_UML2WithID_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_Extend)
gen_UML2WithID_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_UseCase)
gen_UML2WithID_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_ExtensionPoint)
gen_UML2WithID_Trigger_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Trigger)
gen_UML2WithID_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Reception)
gen_UML2WithID_Signal_Classifier = Generalization(general=Classifier, specific=UML2WithID_Signal)
gen_UML2WithID_SignalTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_SignalTrigger)
gen_UML2WithID_TimeTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_TimeTrigger)
gen_UML2WithID_Port_Property = Generalization(general=Property_, specific=UML2WithID_Port)
gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_EncapsulatedClassifier)
gen_UML2WithID_CallTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_CallTrigger)
gen_UML2WithID_MessageTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_MessageTrigger)
gen_UML2WithID_ChangeTrigger_Trigger = Generalization(general=Trigger, specific=UML2WithID_ChangeTrigger)
gen_UML2WithID_Clause_Element = Generalization(general=Element, specific=UML2WithID_Clause)
gen_UML2WithID_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_LoopNode)
gen_UML2WithID_AnyTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2WithID_AnyTrigger)
gen_UML2WithID_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2WithID_Variable)
gen_UML2WithID_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2WithID_Variable)
gen_UML2WithID_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2WithID_Variable)
gen_UML2WithID_StructuredActivityNode_Action = Generalization(general=Action, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2WithID_StructuredActivityNode)
gen_UML2WithID_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_ConditionalNode)
gen_UML2WithID_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_InteractionFragment)
gen_UML2WithID_Lifeline_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Lifeline)
gen_UML2WithID_Interaction_Behavior = Generalization(general=Behavior, specific=UML2WithID_Interaction)
gen_UML2WithID_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_Interaction)
gen_UML2WithID_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_GeneralOrdering)
gen_UML2WithID_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_MessageEnd)
gen_UML2WithID_Message_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Message)
gen_UML2WithID_Stop_EventOccurrence = Generalization(general=EventOccurrence, specific=UML2WithID_Stop)
gen_UML2WithID_TemplateSignature_Element = Generalization(general=Element, specific=UML2WithID_TemplateSignature)
gen_UML2WithID_TemplateParameter_Element = Generalization(general=Element, specific=UML2WithID_TemplateParameter)
gen_UML2WithID_EventOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_EventOccurrence)
gen_UML2WithID_EventOccurrence_MessageEnd = Generalization(general=MessageEnd, specific=UML2WithID_EventOccurrence)
gen_UML2WithID_ExecutionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_ExecutionOccurrence)
gen_UML2WithID_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_StateInvariant)
gen_UML2WithID_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_TemplateBinding)
gen_UML2WithID_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=UML2WithID_TemplateParameterSubstitution)
gen_UML2WithID_TemplateableElement_Element = Generalization(general=Element, specific=UML2WithID_TemplateableElement)
gen_UML2WithID_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2WithID_StringExpression)
gen_UML2WithID_ParameterableElement_Element = Generalization(general=Element, specific=UML2WithID_ParameterableElement)
gen_UML2WithID_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2WithID_FlowFinalNode)
gen_UML2WithID_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2WithID_OperationTemplateParameter)
gen_UML2WithID_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2WithID_ClassifierTemplateParameter)
gen_UML2WithID_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_ParameterableClassifier)
gen_UML2WithID_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_RedefinableTemplateSignature)
gen_UML2WithID_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=UML2WithID_RedefinableTemplateSignature)
gen_UML2WithID_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_TemplateableClassifier)
gen_UML2WithID_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2WithID_ConnectableElementTemplateParameter)
gen_UML2WithID_ForkNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_ForkNode)
gen_UML2WithID_JoinNode_ControlNode = Generalization(general=ControlNode, specific=UML2WithID_JoinNode)
gen_UML2WithID_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_ExpansionNode)
gen_UML2WithID_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2WithID_CentralBufferNode)
gen_UML2WithID_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ActivityPartition)
gen_UML2WithID_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2WithID_ActivityPartition)
gen_UML2WithID_ExceptionHandler_Element = Generalization(general=Element, specific=UML2WithID_ExceptionHandler)
gen_UML2WithID_InteractionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_InteractionOccurrence)
gen_UML2WithID_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2WithID_ExpansionRegion)
gen_UML2WithID_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_CombinedFragment)
gen_UML2WithID_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_Continuation)
gen_UML2WithID_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2WithID_StateMachine)
gen_UML2WithID_Gate_MessageEnd = Generalization(general=MessageEnd, specific=UML2WithID_Gate)
gen_UML2WithID_PartDecomposition_InteractionOccurrence = Generalization(general=InteractionOccurrence, specific=UML2WithID_PartDecomposition)
gen_UML2WithID_InteractionOperand_Namespace = Generalization(general=Namespace, specific=UML2WithID_InteractionOperand)
gen_UML2WithID_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2WithID_InteractionOperand)
gen_UML2WithID_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UML2WithID_InteractionConstraint)
gen_UML2WithID_State_Vertex = Generalization(general=Vertex, specific=UML2WithID_State)
gen_UML2WithID_Region_Namespace = Generalization(general=Namespace, specific=UML2WithID_Region)
gen_UML2WithID_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Region)
gen_UML2WithID_Pseudostate_Vertex = Generalization(general=Vertex, specific=UML2WithID_Pseudostate)
gen_UML2WithID_State_Namespace = Generalization(general=Namespace, specific=UML2WithID_State)
gen_UML2WithID_State_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_State)
gen_UML2WithID_Vertex_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_Vertex)
gen_UML2WithID_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=UML2WithID_ConnectionPointReference)
gen_UML2WithID_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2WithID_Transition)
gen_UML2WithID_ReadSelfAction_Action = Generalization(general=Action, specific=UML2WithID_ReadSelfAction)
gen_UML2WithID_StructuralFeatureAction_Action = Generalization(general=Action, specific=UML2WithID_StructuralFeatureAction)
gen_UML2WithID_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_ReadStructuralFeatureAction)
gen_UML2WithID_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_WriteStructuralFeatureAction)
gen_UML2WithID_FinalState_State = Generalization(general=State, specific=UML2WithID_FinalState)
gen_UML2WithID_CreateObjectAction_Action = Generalization(general=Action, specific=UML2WithID_CreateObjectAction)
gen_UML2WithID_DestroyObjectAction_Action = Generalization(general=Action, specific=UML2WithID_DestroyObjectAction)
gen_UML2WithID_TestIdentityAction_Action = Generalization(general=Action, specific=UML2WithID_TestIdentityAction)
gen_UML2WithID_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UML2WithID_LinkEndCreationData)
gen_UML2WithID_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2WithID_CreateLinkAction)
gen_UML2WithID_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2WithID_WriteLinkAction)
gen_UML2WithID_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2WithID_DestroyLinkAction)
gen_UML2WithID_ClearAssociationAction_Action = Generalization(general=Action, specific=UML2WithID_ClearAssociationAction)
gen_UML2WithID_VariableAction_Action = Generalization(general=Action, specific=UML2WithID_VariableAction)
gen_UML2WithID_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_ReadVariableAction)
gen_UML2WithID_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2WithID_ClearStructuralFeatureAction)
gen_UML2WithID_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_RemoveStructuralFeatureValueAction)
gen_UML2WithID_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_AddStructuralFeatureValueAction)
gen_UML2WithID_LinkAction_Action = Generalization(general=Action, specific=UML2WithID_LinkAction)
gen_UML2WithID_LinkEndData_Element = Generalization(general=Element, specific=UML2WithID_LinkEndData)
gen_UML2WithID_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2WithID_ReadLinkAction)
gen_UML2WithID_PrimitiveFunction_PackageableElement = Generalization(general=PackageableElement, specific=UML2WithID_PrimitiveFunction)
gen_UML2WithID_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_CallAction)
gen_UML2WithID_InvocationAction_Action = Generalization(general=Action, specific=UML2WithID_InvocationAction)
gen_UML2WithID_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_SendSignalAction)
gen_UML2WithID_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_BroadcastSignalAction)
gen_UML2WithID_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_WriteVariableAction)
gen_UML2WithID_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2WithID_ClearVariableAction)
gen_UML2WithID_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2WithID_AddVariableValueAction)
gen_UML2WithID_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2WithID_RemoveVariableValueAction)
gen_UML2WithID_ApplyFunctionAction_Action = Generalization(general=Action, specific=UML2WithID_ApplyFunctionAction)
gen_UML2WithID_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_Duration)
gen_UML2WithID_TimeObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_TimeObservationAction)
gen_UML2WithID_DurationInterval_Interval = Generalization(general=Interval, specific=UML2WithID_DurationInterval)
gen_UML2WithID_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_Interval)
gen_UML2WithID_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2WithID_TimeConstraint)
gen_UML2WithID_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UML2WithID_IntervalConstraint)
gen_UML2WithID_TimeInterval_Interval = Generalization(general=Interval, specific=UML2WithID_TimeInterval)
gen_UML2WithID_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2WithID_SendObjectAction)
gen_UML2WithID_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UML2WithID_CallOperationAction)
gen_UML2WithID_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UML2WithID_CallBehaviorAction)
gen_UML2WithID_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2WithID_TimeExpression)
gen_UML2WithID_Component_Class = Generalization(general=Class_, specific=UML2WithID_Component)
gen_UML2WithID_Deployment_Dependency = Generalization(general=Dependency, specific=UML2WithID_Deployment)
gen_UML2WithID_DurationObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2WithID_DurationObservationAction)
gen_UML2WithID_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2WithID_DurationConstraint)
gen_UML2WithID_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2WithID_DataStoreNode)
gen_UML2WithID_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2WithID_InterruptibleActivityRegion)
gen_UML2WithID_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_ParameterSet)
gen_UML2WithID_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2WithID_ProtocolConformance)
gen_UML2WithID_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_ProtocolTransition_Transition = Generalization(general=Transition, specific=UML2WithID_ProtocolTransition)
gen_UML2WithID_ReadExtentAction_Action = Generalization(general=Action, specific=UML2WithID_ReadExtentAction)
gen_UML2WithID_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_DeployedArtifact)
gen_UML2WithID_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UML2WithID_DeploymentTarget)
gen_UML2WithID_Node_Class = Generalization(general=Class_, specific=UML2WithID_Node)
gen_UML2WithID_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2WithID_Node)
gen_UML2WithID_Device_Node = Generalization(general=Node, specific=UML2WithID_Device)
gen_UML2WithID_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_CommunicationPath_Association = Generalization(general=Association, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_StartOwnedBehaviorAction_Action = Generalization(general=Action, specific=UML2WithID_StartOwnedBehaviorAction)
gen_UML2WithID_QualifierValue_Element = Generalization(general=Element, specific=UML2WithID_QualifierValue)
gen_UML2WithID_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UML2WithID_ReadLinkObjectEndAction)
gen_UML2WithID_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UML2WithID_ReclassifyObjectAction)
gen_UML2WithID_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UML2WithID_ReadIsClassifiedObjectAction)
gen_UML2WithID_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UML2WithID_AcceptCallAction)
gen_UML2WithID_ReplyAction_Action = Generalization(general=Action, specific=UML2WithID_ReplyAction)
gen_UML2WithID_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UML2WithID_ReadLinkObjectEndQualifierAction)
gen_UML2WithID_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UML2WithID_CreateLinkObjectAction)
gen_UML2WithID_AcceptEventAction_Action = Generalization(general=Action, specific=UML2WithID_AcceptEventAction)
gen_UML2WithID_RaiseExceptionAction_Action = Generalization(general=Action, specific=UML2WithID_RaiseExceptionAction)
gen_UML2WithID_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2WithID_DeploymentSpecification)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={UML2WithID_Element, UML2WithID_Comment, UML2WithID_MultiplicityElement, Element, UML2WithID_ValueSpecification, UML2WithID_NamedElement, TemplateableElement, UML2WithID_Dependency, UML2WithID_StringExpression, UML2WithID_Namespace, NamedElement, UML2WithID_Constraint, UML2WithID_PackageableElement, UML2WithID_ElementImport, UML2WithID_PackageImport, UML2WithID_OpaqueExpression, ValueSpecification, UML2WithID_Parameter, UML2WithID_Behavior, TypedElement, ParameterableElement, UML2WithID_Expression, OpaqueExpression, UML2WithID_DirectedRelationship, Relationship, UML2WithID_Relationship, UML2WithID_Class, BehavioredClassifier, EncapsulatedClassifier, UML2WithID_Operation, UML2WithID_Extension, UML2WithID_Classifier, UML2WithID_Reception, UML2WithID_Type, PackageableElement, UML2WithID_Package, UML2WithID_Property, StructuralFeature, ConnectableElement, DeploymentTarget, UML2WithID_Association, UML2WithID_DataType, BehavioralFeature, MultiplicityElement, UML2WithID_TypedElement, UML2WithID_ParameterSet, Namespace, UML2WithID_PackageMerge, UML2WithID_ProfileApplication, UML2WithID_Enumeration, DataType, UML2WithID_EnumerationLiteral, Classifier, InstanceSpecification, UML2WithID_PrimitiveType, Type, RedefinableElement, UML2WithID_Feature, UML2WithID_Generalization, UML2WithID_Substitution, UML2WithID_GeneralizationSet, UML2WithID_UseCase, UML2WithID_CollaborationOccurrence, UML2WithID_Slot, UML2WithID_LiteralBoolean, LiteralSpecification, UML2WithID_LiteralSpecification, UML2WithID_LiteralString, UML2WithID_LiteralNull, UML2WithID_LiteralInteger, UML2WithID_LiteralUnlimitedNatural, UML2WithID_BehavioralFeature, Feature, UML2WithID_StructuralFeature, UML2WithID_InstanceSpecification, DeployedArtifact, UML2WithID_RedefinableElement, UML2WithID_InstanceValue, DirectedRelationship, UML2WithID_Stereotype, Class_, UML2WithID_Profile, Package, PackageImport, Association, UML2WithID_ExtensionEnd, Property_, UML2WithID_BehavioredClassifier, UML2WithID_Action, UML2WithID_StructuredActivityNode, UML2WithID_Permission, Dependency, UML2WithID_Usage, UML2WithID_Implementation, UML2WithID_Trigger, UML2WithID_StateMachine, UML2WithID_Activity, Behavior, UML2WithID_ActivityEdge, UML2WithID_ActivityGroup, UML2WithID_ActivityNode, UML2WithID_InformationItem, UML2WithID_InformationFlow, UML2WithID_Model, UML2WithID_ConnectorEnd, UML2WithID_Abstraction, UML2WithID_Realization, Abstraction, UML2WithID_Component, Realization, UML2WithID_AssociationClass, UML2WithID_ConnectableElement, UML2WithID_Connector, UML2WithID_StructuredClassifier, ExecutableNode, UML2WithID_OutputPin, UML2WithID_ActivityPartition, UML2WithID_InterruptibleActivityRegion, UML2WithID_InitialNode, ControlNode, UML2WithID_FinalNode, UML2WithID_ActivityFinalNode, FinalNode, UML2WithID_DecisionNode, UML2WithID_MergeNode, UML2WithID_ExecutableNode, UML2WithID_ExceptionHandler, Pin, UML2WithID_InputPin, UML2WithID_ObjectNode, ActivityNode, UML2WithID_State, UML2WithID_ControlNode, UML2WithID_ControlFlow, ActivityEdge, UML2WithID_ObjectFlow, UML2WithID_Artifact, UML2WithID_Manifestation, UML2WithID_Pin, ObjectNode, UML2WithID_ActivityParameterNode, UML2WithID_ValuePin, InputPin, UML2WithID_Interface, UML2WithID_ProtocolStateMachine, UML2WithID_Collaboration, StructuredClassifier, UML2WithID_Port, UML2WithID_Actor, UML2WithID_Extend, UML2WithID_ExtensionPoint, UML2WithID_Include, UML2WithID_Signal, UML2WithID_SignalTrigger, UML2WithID_TimeTrigger, UML2WithID_EncapsulatedClassifier, UML2WithID_CallTrigger, MessageTrigger, UML2WithID_MessageTrigger, Trigger, UML2WithID_ChangeTrigger, UML2WithID_LoopNode, UML2WithID_AnyTrigger, UML2WithID_Variable, Action, ActivityGroup, UML2WithID_ConditionalNode, StructuredActivityNode, UML2WithID_Clause, UML2WithID_InteractionFragment, UML2WithID_Gate, UML2WithID_GeneralOrdering, UML2WithID_InteractionOperand, UML2WithID_Interaction, InteractionFragment, UML2WithID_Lifeline, UML2WithID_Message, UML2WithID_EventOccurrence, UML2WithID_PartDecomposition, UML2WithID_MessageEnd, UML2WithID_Stop, EventOccurrence, UML2WithID_TemplateSignature, UML2WithID_TemplateParameter, UML2WithID_TemplateableElement, MessageEnd, UML2WithID_ExecutionOccurrence, UML2WithID_StateInvariant, UML2WithID_TemplateParameterSubstitution, UML2WithID_ParameterableElement, UML2WithID_TemplateBinding, UML2WithID_FlowFinalNode, UML2WithID_OperationTemplateParameter, TemplateParameter, UML2WithID_ClassifierTemplateParameter, UML2WithID_ParameterableClassifier, UML2WithID_RedefinableTemplateSignature, TemplateSignature, UML2WithID_TemplateableClassifier, UML2WithID_ConnectableElementTemplateParameter, UML2WithID_ForkNode, UML2WithID_JoinNode, UML2WithID_ExpansionNode, UML2WithID_ExpansionRegion, UML2WithID_CentralBufferNode, UML2WithID_InteractionOccurrence, UML2WithID_CombinedFragment, UML2WithID_Continuation, UML2WithID_Region, UML2WithID_Pseudostate, InteractionOccurrence, UML2WithID_InteractionConstraint, Constraint, UML2WithID_ConnectionPointReference, UML2WithID_Vertex, UML2WithID_Transition, Vertex, UML2WithID_ReadSelfAction, UML2WithID_StructuralFeatureAction, UML2WithID_ReadStructuralFeatureAction, StructuralFeatureAction, UML2WithID_WriteStructuralFeatureAction, UML2WithID_ClearStructuralFeatureAction, UML2WithID_FinalState, State, UML2WithID_CreateObjectAction, UML2WithID_DestroyObjectAction, UML2WithID_TestIdentityAction, UML2WithID_LinkEndCreationData, LinkEndData, UML2WithID_CreateLinkAction, WriteLinkAction, UML2WithID_WriteLinkAction, UML2WithID_DestroyLinkAction, UML2WithID_ClearAssociationAction, UML2WithID_VariableAction, UML2WithID_ReadVariableAction, VariableAction, UML2WithID_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, UML2WithID_AddStructuralFeatureValueAction, UML2WithID_LinkAction, UML2WithID_LinkEndData, UML2WithID_QualifierValue, UML2WithID_ReadLinkAction, LinkAction, UML2WithID_CallAction, InvocationAction, UML2WithID_InvocationAction, UML2WithID_SendSignalAction, UML2WithID_BroadcastSignalAction, UML2WithID_WriteVariableAction, UML2WithID_ClearVariableAction, UML2WithID_AddVariableValueAction, WriteVariableAction, UML2WithID_RemoveVariableValueAction, UML2WithID_ApplyFunctionAction, UML2WithID_PrimitiveFunction, UML2WithID_Duration, UML2WithID_TimeObservationAction, UML2WithID_DurationInterval, Interval, UML2WithID_Interval, UML2WithID_TimeConstraint, IntervalConstraint, UML2WithID_IntervalConstraint, UML2WithID_TimeInterval, UML2WithID_SendObjectAction, UML2WithID_CallOperationAction, CallAction, UML2WithID_CallBehaviorAction, UML2WithID_TimeExpression, UML2WithID_Deployment, UML2WithID_DeployedArtifact, UML2WithID_DurationObservationAction, UML2WithID_DurationConstraint, UML2WithID_DataStoreNode, CentralBufferNode, UML2WithID_ProtocolConformance, StateMachine, UML2WithID_ProtocolTransition, Transition, UML2WithID_ReadExtentAction, UML2WithID_DeploymentTarget, UML2WithID_DeploymentSpecification, UML2WithID_Node, UML2WithID_Device, Node, UML2WithID_ExecutionEnvironment, UML2WithID_CommunicationPath, UML2WithID_StartOwnedBehaviorAction, UML2WithID_ReadLinkObjectEndAction, UML2WithID_ReclassifyObjectAction, UML2WithID_ReadIsClassifiedObjectAction, UML2WithID_AcceptCallAction, AcceptEventAction, UML2WithID_ReplyAction, UML2WithID_ReadLinkObjectEndQualifierAction, UML2WithID_CreateLinkObjectAction, CreateLinkAction, UML2WithID_AcceptEventAction, UML2WithID_RaiseExceptionAction, Artifact, VisibilityKind, ParameterDirectionKind, AggregationKind, CallConcurrencyKind, MessageKind, MessageSort, ExpansionKind, InteractionOperator, TransitionKind, PseudostateKind, ConnectorKind, ParameterEffectKind, ObjectNodeOrderingKind},
    associations={ownedElement1, owner3, ownedComment5, upperValue6, lowerValue7, clientDependency10, nameExpression11, member12, ownedRule14, importedMember15, elementImport17, packageImport18, result20, behavior21, class_47, operand23, annotatedElement25, bodyExpression28, source31, target33, relatedElement36, ownedOperation38, superClass40, extension41, nestedClassifier42, ownedReception44, package46, opposite50, owningAssociation52, redefinedProperty54, subsettedProperty57, datatype59, association60, defaultValue62, qualifier66, associationEnd68, ownedParameter70, class_71, datatype72, precondition75, postcondition76, redefinedOperation80, bodyCondition82, type85, operation86, defaultValue88, parameterSet91, nestedPackage93, nestingPackage96, ownedType98, ownedMember99, packageMerge101, appliedProfile102, packageExtension104, ownedLiteral106, ownedAttribute107, ownedOperation109, enumeration112, feature113, inheritedMember114, general118, generalization120, attribute121, redefinedClassifier125, substitution127, powertypeExtent128, ownedUseCase129, useCase131, representation132, occurrence134, featuringClassifier137, context138, namespace141, specification142, constrainedElement145, parameter148, formalParameter150, returnResult153, raisedException156, method159, slot160, redefinitionContext173, classifier161, specification163, owningInstance166, value167, definingFeature169, instance171, mergingPackage196, mergedPackage198, specific175, general177, generalizationSet179, importedElement182, importingNamespace184, importedPackage186, importingNamespace188, ownedEnd190, endType192, memberEnd194, redefinedBehavior215, specification217, parameter218, formalParameter221, ownedStereotype201, returnResult224, precondition227, metaclassReference202, postcondition230, metamodelReference205, importedProfile208, metaclass211, context213, action247, structuredNode248, client250, supplier251, ownedParameterSet233, ownedBehavior235, classifierBehavior237, implementation239, ownedTrigger240, ownedStateMachine242, edge243, group244, node245, represented266, realization268, conveyed270, definingEnd273, mapping253, abstraction255, realizingClassifier256, contract258, substitutingClassifier260, powertype262, generalization264, ownedConnector298, activity301, source302, target304, inGroup306, guard307, role275, partWithPort276, end279, type280, redefinedConnector283, end285, contract288, ownedAttribute291, part293, role296, inGroup329, activity331, redefinedElement334, inStructuredNode336, inPartition338, inInterruptibleRegion341, output344, redefinedElement311, inStructuredNode313, inPartition314, weight316, interrupts319, superGroup321, activityGroup_activity323, outgoing325, incoming327, transformation364, selection366, decisionInput369, handler371, input346, context_348, localPrecondition351, localPostcondition354, upperBound357, inState359, selection361, contract392, implementingClassifier394, nestedArtifact397, manifestation398, ownedOperation400, ownedAttribute403, parameter372, value374, ownedAttribute376, ownedOperation378, redefinedInterface382, nestedClassifier384, ownedReception387, protocol390, useCase425, includingCase427, addition429, type431, roleBinding433, collaborationRole436, utilizedElement406, extendedCase409, extension411, condition413, extensionLocation416, include418, extend419, extensionPoint421, subject422, port456, signal459, ownedAttribute461, signal464, when466, required439, redefinedPort442, provided444, protocol447, ownedPort450, operation452, changeExpression454, result477, test480, body483, predecessorClause487, successorClause489, decider491, bodyOutput494, scope468, variable470, containedNode471, containedEdge473, clause476, fragment523, formalGate524, covered525, generalOrdering527, enclosingInteraction528, enclosingOperand529, bodyPart497, setupPart499, decider502, test505, result508, loopVariable511, bodyOutput514, loopVariableInput517, lifeline520, message521, argument552, before555, after556, receiveMessage558, coveredBy531, represents533, interaction535, selector537, decomposedAs540, receiveEvent542, sendEvent543, connector545, interaction547, signature549, parameter576, ownedParameter577, nestedSignature579, nestingSignature581, template583, signature584, sendMessage560, startExec562, finishExec563, toAfter565, toBefore566, start568, finish570, behavior572, invariant574, owningParameter605, boundElement607, signature609, parameterSubstitution611, formal613, templateBinding615, actual617, parameteredElement587, ownedParameteredElement588, default590, ownedDefault592, templateBinding595, ownedTemplateSignature596, subExpression599, owningExpression601, templateParameter603, joinSpec623, ownedActual620, subgroup631, superPartition634, represents636, containedEdge625, containedNode627, protectedNode644, handlerBody645, exceptionInput646, exceptionType649, refersTo652, actualGate654, regionAsOutput638, regionAsInput639, outputElement641, inputElement642, operand669, cfragmentGate671, region674, argument657, guard660, fragment661, minint663, maxint666, submachine690, connection693, redefinedState696, deferrableTrigger698, region701, entry703, connectionPoint675, exit706, extendedStateMachine677, stateMachine_redefinitionContext679, subvertex681, transition682, stateMachine684, state686, extendedRegion689, container729, source731, target734, redefinedTransition738, trigger739, guard742, effect745, doActivity709, stateInvariant712, container715, outgoing717, incoming720, entry723, exit726, second757, result760, result763, structuralFeature765, object767, result770, value772, classifier748, result750, target753, first755, result785, insertAt787, object789, association791, variable794, result795, insertAt774, endData776, value777, end780, qualifier783, result805, result808, argument810, onPort812, target815, signal817, value797, insertAt799, function801, argument802, event834, event836, now838, min840, max842, signal820, target822, request824, operation827, target829, behavior832, parameter851, condition853, required856, provided858, realization861, ownedMember862, deployedArtifact865, duration845, interruptingEdge847, containedNode849, specificMachine874, generalMachine875, conformance877, postCondition878, referred880, preCondition883, result886, location866, configuration867, deployment869, deployedElement870, nestedNode873, classifier899, result901, object904, object907, qualifier909, value912, object915, classifier888, oldClassifier891, newClassifier893, object896, trigger933, result935, returnInformation938, replyToCall940, replyValue942, returnInformation945, end917, result920, object923, result925, qualifier928, result931, exception948},
    generalizations={gen_UML2WithID_MultiplicityElement_Element, gen_UML2WithID_NamedElement_TemplateableElement, gen_UML2WithID_Namespace_NamedElement, gen_UML2WithID_OpaqueExpression_ValueSpecification, gen_UML2WithID_ValueSpecification_TypedElement, gen_UML2WithID_ValueSpecification_ParameterableElement, gen_UML2WithID_Expression_OpaqueExpression, gen_UML2WithID_Comment_TemplateableElement, gen_UML2WithID_DirectedRelationship_Relationship, gen_UML2WithID_Relationship_Element, gen_UML2WithID_Class_BehavioredClassifier, gen_UML2WithID_Class_EncapsulatedClassifier, gen_UML2WithID_Type_PackageableElement, gen_UML2WithID_Property_StructuralFeature, gen_UML2WithID_Property_ConnectableElement, gen_UML2WithID_Property_DeploymentTarget, gen_UML2WithID_Parameter_ConnectableElement, gen_UML2WithID_Operation_BehavioralFeature, gen_UML2WithID_Operation_TypedElement, gen_UML2WithID_Operation_MultiplicityElement, gen_UML2WithID_Operation_ParameterableElement, gen_UML2WithID_TypedElement_NamedElement, gen_UML2WithID_Parameter_TypedElement, gen_UML2WithID_Parameter_MultiplicityElement, gen_UML2WithID_Package_Namespace, gen_UML2WithID_Package_PackageableElement, gen_UML2WithID_Enumeration_DataType, gen_UML2WithID_DataType_Classifier, gen_UML2WithID_EnumerationLiteral_InstanceSpecification, gen_UML2WithID_PrimitiveType_DataType, gen_UML2WithID_Classifier_Namespace, gen_UML2WithID_Classifier_Type, gen_UML2WithID_Classifier_RedefinableElement, gen_UML2WithID_Feature_RedefinableElement, gen_UML2WithID_Constraint_PackageableElement, gen_UML2WithID_LiteralBoolean_LiteralSpecification, gen_UML2WithID_LiteralSpecification_ValueSpecification, gen_UML2WithID_LiteralString_LiteralSpecification, gen_UML2WithID_LiteralNull_LiteralSpecification, gen_UML2WithID_LiteralInteger_LiteralSpecification, gen_UML2WithID_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2WithID_BehavioralFeature_Namespace, gen_UML2WithID_BehavioralFeature_Feature, gen_UML2WithID_StructuralFeature_Feature, gen_UML2WithID_StructuralFeature_TypedElement, gen_UML2WithID_StructuralFeature_MultiplicityElement, gen_UML2WithID_InstanceSpecification_PackageableElement, gen_UML2WithID_InstanceSpecification_DeploymentTarget, gen_UML2WithID_InstanceSpecification_DeployedArtifact, gen_UML2WithID_RedefinableElement_NamedElement, gen_UML2WithID_Slot_Element, gen_UML2WithID_InstanceValue_ValueSpecification, gen_UML2WithID_Generalization_DirectedRelationship, gen_UML2WithID_PackageableElement_NamedElement, gen_UML2WithID_PackageableElement_ParameterableElement, gen_UML2WithID_ElementImport_DirectedRelationship, gen_UML2WithID_PackageImport_DirectedRelationship, gen_UML2WithID_Association_Classifier, gen_UML2WithID_Association_Relationship, gen_UML2WithID_PackageMerge_DirectedRelationship, gen_UML2WithID_Stereotype_Class, gen_UML2WithID_Profile_Package, gen_UML2WithID_ProfileApplication_PackageImport, gen_UML2WithID_Extension_Association, gen_UML2WithID_ExtensionEnd_Property, gen_UML2WithID_Behavior_Class, gen_UML2WithID_Permission_Dependency, gen_UML2WithID_Dependency_PackageableElement, gen_UML2WithID_Dependency_DirectedRelationship, gen_UML2WithID_Usage_Dependency, gen_UML2WithID_BehavioredClassifier_Classifier, gen_UML2WithID_Activity_Behavior, gen_UML2WithID_InformationItem_Classifier, gen_UML2WithID_InformationFlow_PackageableElement, gen_UML2WithID_InformationFlow_DirectedRelationship, gen_UML2WithID_Model_Package, gen_UML2WithID_ConnectorEnd_MultiplicityElement, gen_UML2WithID_Abstraction_Dependency, gen_UML2WithID_Realization_Abstraction, gen_UML2WithID_Substitution_Realization, gen_UML2WithID_GeneralizationSet_PackageableElement, gen_UML2WithID_AssociationClass_Class, gen_UML2WithID_AssociationClass_Association, gen_UML2WithID_ActivityEdge_RedefinableElement, gen_UML2WithID_ConnectableElement_NamedElement, gen_UML2WithID_ConnectableElement_ParameterableElement, gen_UML2WithID_Connector_Feature, gen_UML2WithID_StructuredClassifier_Classifier, gen_UML2WithID_Action_ExecutableNode, gen_UML2WithID_ActivityGroup_Element, gen_UML2WithID_ActivityNode_RedefinableElement, gen_UML2WithID_InitialNode_ControlNode, gen_UML2WithID_FinalNode_ControlNode, gen_UML2WithID_ActivityFinalNode_FinalNode, gen_UML2WithID_DecisionNode_ControlNode, gen_UML2WithID_MergeNode_ControlNode, gen_UML2WithID_ExecutableNode_ActivityNode, gen_UML2WithID_OutputPin_Pin, gen_UML2WithID_InputPin_Pin, gen_UML2WithID_ObjectNode_ActivityNode, gen_UML2WithID_ObjectNode_TypedElement, gen_UML2WithID_ControlNode_ActivityNode, gen_UML2WithID_ControlFlow_ActivityEdge, gen_UML2WithID_ObjectFlow_ActivityEdge, gen_UML2WithID_Artifact_Classifier, gen_UML2WithID_Artifact_DeployedArtifact, gen_UML2WithID_Manifestation_Abstraction, gen_UML2WithID_Pin_ObjectNode, gen_UML2WithID_Pin_MultiplicityElement, gen_UML2WithID_ActivityParameterNode_ObjectNode, gen_UML2WithID_ValuePin_InputPin, gen_UML2WithID_Interface_Classifier, gen_UML2WithID_Implementation_Realization, gen_UML2WithID_Include_NamedElement, gen_UML2WithID_Include_DirectedRelationship, gen_UML2WithID_CollaborationOccurrence_NamedElement, gen_UML2WithID_Collaboration_BehavioredClassifier, gen_UML2WithID_Collaboration_StructuredClassifier, gen_UML2WithID_Actor_Classifier, gen_UML2WithID_Extend_NamedElement, gen_UML2WithID_Extend_DirectedRelationship, gen_UML2WithID_UseCase_BehavioredClassifier, gen_UML2WithID_ExtensionPoint_RedefinableElement, gen_UML2WithID_Trigger_NamedElement, gen_UML2WithID_Reception_BehavioralFeature, gen_UML2WithID_Signal_Classifier, gen_UML2WithID_SignalTrigger_MessageTrigger, gen_UML2WithID_TimeTrigger_Trigger, gen_UML2WithID_Port_Property, gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier, gen_UML2WithID_CallTrigger_MessageTrigger, gen_UML2WithID_MessageTrigger_Trigger, gen_UML2WithID_ChangeTrigger_Trigger, gen_UML2WithID_Clause_Element, gen_UML2WithID_LoopNode_StructuredActivityNode, gen_UML2WithID_AnyTrigger_MessageTrigger, gen_UML2WithID_Variable_ConnectableElement, gen_UML2WithID_Variable_TypedElement, gen_UML2WithID_Variable_MultiplicityElement, gen_UML2WithID_StructuredActivityNode_Action, gen_UML2WithID_StructuredActivityNode_Namespace, gen_UML2WithID_StructuredActivityNode_ActivityGroup, gen_UML2WithID_ConditionalNode_StructuredActivityNode, gen_UML2WithID_InteractionFragment_NamedElement, gen_UML2WithID_Lifeline_NamedElement, gen_UML2WithID_Interaction_Behavior, gen_UML2WithID_Interaction_InteractionFragment, gen_UML2WithID_GeneralOrdering_NamedElement, gen_UML2WithID_MessageEnd_NamedElement, gen_UML2WithID_Message_NamedElement, gen_UML2WithID_Stop_EventOccurrence, gen_UML2WithID_TemplateSignature_Element, gen_UML2WithID_TemplateParameter_Element, gen_UML2WithID_EventOccurrence_InteractionFragment, gen_UML2WithID_EventOccurrence_MessageEnd, gen_UML2WithID_ExecutionOccurrence_InteractionFragment, gen_UML2WithID_StateInvariant_InteractionFragment, gen_UML2WithID_TemplateBinding_DirectedRelationship, gen_UML2WithID_TemplateParameterSubstitution_Element, gen_UML2WithID_TemplateableElement_Element, gen_UML2WithID_StringExpression_TemplateableElement, gen_UML2WithID_ParameterableElement_Element, gen_UML2WithID_FlowFinalNode_FinalNode, gen_UML2WithID_OperationTemplateParameter_TemplateParameter, gen_UML2WithID_ClassifierTemplateParameter_TemplateParameter, gen_UML2WithID_ParameterableClassifier_Classifier, gen_UML2WithID_RedefinableTemplateSignature_RedefinableElement, gen_UML2WithID_RedefinableTemplateSignature_TemplateSignature, gen_UML2WithID_TemplateableClassifier_Classifier, gen_UML2WithID_ConnectableElementTemplateParameter_TemplateParameter, gen_UML2WithID_ForkNode_ControlNode, gen_UML2WithID_JoinNode_ControlNode, gen_UML2WithID_ExpansionNode_ObjectNode, gen_UML2WithID_CentralBufferNode_ObjectNode, gen_UML2WithID_ActivityPartition_NamedElement, gen_UML2WithID_ActivityPartition_ActivityGroup, gen_UML2WithID_ExceptionHandler_Element, gen_UML2WithID_InteractionOccurrence_InteractionFragment, gen_UML2WithID_ExpansionRegion_StructuredActivityNode, gen_UML2WithID_CombinedFragment_InteractionFragment, gen_UML2WithID_Continuation_InteractionFragment, gen_UML2WithID_StateMachine_Behavior, gen_UML2WithID_Gate_MessageEnd, gen_UML2WithID_PartDecomposition_InteractionOccurrence, gen_UML2WithID_InteractionOperand_Namespace, gen_UML2WithID_InteractionOperand_InteractionFragment, gen_UML2WithID_InteractionConstraint_Constraint, gen_UML2WithID_State_Vertex, gen_UML2WithID_Region_Namespace, gen_UML2WithID_Region_RedefinableElement, gen_UML2WithID_Pseudostate_Vertex, gen_UML2WithID_State_Namespace, gen_UML2WithID_State_RedefinableElement, gen_UML2WithID_Vertex_NamedElement, gen_UML2WithID_ConnectionPointReference_Vertex, gen_UML2WithID_Transition_RedefinableElement, gen_UML2WithID_ReadSelfAction_Action, gen_UML2WithID_StructuralFeatureAction_Action, gen_UML2WithID_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_WriteStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_FinalState_State, gen_UML2WithID_CreateObjectAction_Action, gen_UML2WithID_DestroyObjectAction_Action, gen_UML2WithID_TestIdentityAction_Action, gen_UML2WithID_LinkEndCreationData_LinkEndData, gen_UML2WithID_CreateLinkAction_WriteLinkAction, gen_UML2WithID_WriteLinkAction_LinkAction, gen_UML2WithID_DestroyLinkAction_WriteLinkAction, gen_UML2WithID_ClearAssociationAction_Action, gen_UML2WithID_VariableAction_Action, gen_UML2WithID_ReadVariableAction_VariableAction, gen_UML2WithID_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UML2WithID_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2WithID_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2WithID_LinkAction_Action, gen_UML2WithID_LinkEndData_Element, gen_UML2WithID_ReadLinkAction_LinkAction, gen_UML2WithID_PrimitiveFunction_PackageableElement, gen_UML2WithID_CallAction_InvocationAction, gen_UML2WithID_InvocationAction_Action, gen_UML2WithID_SendSignalAction_InvocationAction, gen_UML2WithID_BroadcastSignalAction_InvocationAction, gen_UML2WithID_WriteVariableAction_VariableAction, gen_UML2WithID_ClearVariableAction_VariableAction, gen_UML2WithID_AddVariableValueAction_WriteVariableAction, gen_UML2WithID_RemoveVariableValueAction_WriteVariableAction, gen_UML2WithID_ApplyFunctionAction_Action, gen_UML2WithID_Duration_ValueSpecification, gen_UML2WithID_TimeObservationAction_WriteStructuralFeatureAction, gen_UML2WithID_DurationInterval_Interval, gen_UML2WithID_Interval_ValueSpecification, gen_UML2WithID_TimeConstraint_IntervalConstraint, gen_UML2WithID_IntervalConstraint_Constraint, gen_UML2WithID_TimeInterval_Interval, gen_UML2WithID_SendObjectAction_InvocationAction, gen_UML2WithID_CallOperationAction_CallAction, gen_UML2WithID_CallBehaviorAction_CallAction, gen_UML2WithID_TimeExpression_ValueSpecification, gen_UML2WithID_Component_Class, gen_UML2WithID_Deployment_Dependency, gen_UML2WithID_DurationObservationAction_WriteStructuralFeatureAction, gen_UML2WithID_DurationConstraint_IntervalConstraint, gen_UML2WithID_DataStoreNode_CentralBufferNode, gen_UML2WithID_InterruptibleActivityRegion_ActivityGroup, gen_UML2WithID_ParameterSet_NamedElement, gen_UML2WithID_ProtocolConformance_DirectedRelationship, gen_UML2WithID_ProtocolStateMachine_StateMachine, gen_UML2WithID_ProtocolTransition_Transition, gen_UML2WithID_ReadExtentAction_Action, gen_UML2WithID_DeployedArtifact_NamedElement, gen_UML2WithID_DeploymentTarget_NamedElement, gen_UML2WithID_Node_Class, gen_UML2WithID_Node_DeploymentTarget, gen_UML2WithID_Device_Node, gen_UML2WithID_ExecutionEnvironment_Node, gen_UML2WithID_CommunicationPath_Association, gen_UML2WithID_StartOwnedBehaviorAction_Action, gen_UML2WithID_QualifierValue_Element, gen_UML2WithID_ReadLinkObjectEndAction_Action, gen_UML2WithID_ReclassifyObjectAction_Action, gen_UML2WithID_ReadIsClassifiedObjectAction_Action, gen_UML2WithID_AcceptCallAction_AcceptEventAction, gen_UML2WithID_ReplyAction_Action, gen_UML2WithID_ReadLinkObjectEndQualifierAction_Action, gen_UML2WithID_CreateLinkObjectAction_CreateLinkAction, gen_UML2WithID_AcceptEventAction_Action, gen_UML2WithID_RaiseExceptionAction_Action, gen_UML2WithID_DeploymentSpecification_Artifact},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)