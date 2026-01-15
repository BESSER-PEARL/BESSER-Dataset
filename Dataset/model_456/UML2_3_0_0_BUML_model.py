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

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="found"),
			EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="lost")
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
uml3_0_0_Package = Class(name="uml3::0::0::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
TemplateableElement = Class(name="TemplateableElement")
uml3_0_0_Type = Class(name="uml3::0::0::Type", is_abstract=True)
uml3_0_0_PackageMerge = Class(name="uml3::0::0::PackageMerge")
uml3_0_0_PackageableElement = Class(name="uml3::0::0::PackageableElement", is_abstract=True)
uml3_0_0_Comment = Class(name="uml3::0::0::Comment")
Element = Class(name="Element")
uml3_0_0_Element = Class(name="uml3::0::0::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
uml3_0_0_Namespace = Class(name="uml3::0::0::Namespace", is_abstract=True)
uml3_0_0_StringExpression = Class(name="uml3::0::0::StringExpression")
DirectedRelationship = Class(name="DirectedRelationship")
uml3_0_0_DirectedRelationship = Class(name="uml3::0::0::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
uml3_0_0_Relationship = Class(name="uml3::0::0::Relationship", is_abstract=True)
uml3_0_0_ProfileApplication = Class(name="uml3::0::0::ProfileApplication")
NamedElement = Class(name="NamedElement")
ParameterableElement = Class(name="ParameterableElement")
uml3_0_0_NamedElement = Class(name="uml3::0::0::NamedElement", is_abstract=True)
uml3_0_0_Dependency = Class(name="uml3::0::0::Dependency")
uml3_0_0_ElementImport = Class(name="uml3::0::0::ElementImport")
uml3_0_0_PackageImport = Class(name="uml3::0::0::PackageImport")
uml3_0_0_Constraint = Class(name="uml3::0::0::Constraint")
uml3_0_0_Association = Class(name="uml3::0::0::Association")
Classifier = Class(name="Classifier")
uml3_0_0_Property = Class(name="uml3::0::0::Property")
uml3_0_0_Classifier = Class(name="uml3::0::0::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
uml3_0_0_Generalization = Class(name="uml3::0::0::Generalization")
uml3_0_0_GeneralizationSet = Class(name="uml3::0::0::GeneralizationSet")
uml3_0_0_Feature = Class(name="uml3::0::0::Feature", is_abstract=True)
uml3_0_0_ValueSpecification = Class(name="uml3::0::0::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
uml3_0_0_TypedElement = Class(name="uml3::0::0::TypedElement", is_abstract=True)
uml3_0_0_CollaborationUse = Class(name="uml3::0::0::CollaborationUse")
uml3_0_0_UseCase = Class(name="uml3::0::0::UseCase")
uml3_0_0_RedefinableElement = Class(name="uml3::0::0::RedefinableElement", is_abstract=True)
uml3_0_0_TemplateableElement = Class(name="uml3::0::0::TemplateableElement", is_abstract=True)
uml3_0_0_TemplateBinding = Class(name="uml3::0::0::TemplateBinding")
uml3_0_0_TemplateSignature = Class(name="uml3::0::0::TemplateSignature")
uml3_0_0_Substitution = Class(name="uml3::0::0::Substitution")
uml3_0_0_ParameterableElement = Class(name="uml3::0::0::ParameterableElement", is_abstract=True)
uml3_0_0_TemplateParameterSubstitution = Class(name="uml3::0::0::TemplateParameterSubstitution")
uml3_0_0_TemplateParameter = Class(name="uml3::0::0::TemplateParameter")
Realization = Class(name="Realization")
ConnectableElement = Class(name="ConnectableElement")
MultiplicityElement = Class(name="MultiplicityElement")
uml3_0_0_ParameterSet = Class(name="uml3::0::0::ParameterSet")
uml3_0_0_Operation = Class(name="uml3::0::0::Operation")
uml3_0_0_MultiplicityElement = Class(name="uml3::0::0::MultiplicityElement", is_abstract=True)
uml3_0_0_Realization = Class(name="uml3::0::0::Realization")
Abstraction = Class(name="Abstraction")
uml3_0_0_Abstraction = Class(name="uml3::0::0::Abstraction")
Dependency = Class(name="Dependency")
uml3_0_0_OpaqueExpression = Class(name="uml3::0::0::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
uml3_0_0_Parameter = Class(name="uml3::0::0::Parameter")
uml3_0_0_Behavior = Class(name="uml3::0::0::Behavior", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
DeploymentTarget = Class(name="DeploymentTarget")
uml3_0_0_Class = Class(name="uml3::0::0::Class")
uml3_0_0_DataType = Class(name="uml3::0::0::DataType")
uml3_0_0_ConnectableElement = Class(name="uml3::0::0::ConnectableElement", is_abstract=True)
uml3_0_0_ConnectorEnd = Class(name="uml3::0::0::ConnectorEnd")
uml3_0_0_DeploymentTarget = Class(name="uml3::0::0::DeploymentTarget", is_abstract=True)
uml3_0_0_Deployment = Class(name="uml3::0::0::Deployment")
uml3_0_0_DeployedArtifact = Class(name="uml3::0::0::DeployedArtifact", is_abstract=True)
uml3_0_0_DeploymentSpecification = Class(name="uml3::0::0::DeploymentSpecification")
Artifact = Class(name="Artifact")
uml3_0_0_Artifact = Class(name="uml3::0::0::Artifact")
DeployedArtifact = Class(name="DeployedArtifact")
uml3_0_0_Manifestation = Class(name="uml3::0::0::Manifestation")
BehavioralFeature = Class(name="BehavioralFeature")
uml3_0_0_Interface = Class(name="uml3::0::0::Interface")
uml3_0_0_BehavioralFeature = Class(name="uml3::0::0::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
Class_ = Class(name="Class")
uml3_0_0_BehavioredClassifier = Class(name="uml3::0::0::BehavioredClassifier", is_abstract=True)
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
uml3_0_0_Reception = Class(name="uml3::0::0::Reception")
uml3_0_0_Extension = Class(name="uml3::0::0::Extension")
uml3_0_0_InterfaceRealization = Class(name="uml3::0::0::InterfaceRealization")
uml3_0_0_Trigger = Class(name="uml3::0::0::Trigger")
uml3_0_0_ProtocolStateMachine = Class(name="uml3::0::0::ProtocolStateMachine")
uml3_0_0_Signal = Class(name="uml3::0::0::Signal")
StateMachine = Class(name="StateMachine")
uml3_0_0_ProtocolConformance = Class(name="uml3::0::0::ProtocolConformance")
uml3_0_0_Region = Class(name="uml3::0::0::Region")
uml3_0_0_State = Class(name="uml3::0::0::State")
uml3_0_0_Pseudostate = Class(name="uml3::0::0::Pseudostate")
uml3_0_0_Vertex = Class(name="uml3::0::0::Vertex", is_abstract=True)
uml3_0_0_Transition = Class(name="uml3::0::0::Transition")
uml3_0_0_StateMachine = Class(name="uml3::0::0::StateMachine")
Behavior = Class(name="Behavior")
uml3_0_0_Event = Class(name="uml3::0::0::Event", is_abstract=True)
uml3_0_0_Port = Class(name="uml3::0::0::Port")
Property_ = Class(name="Property")
Vertex = Class(name="Vertex")
uml3_0_0_ConnectionPointReference = Class(name="uml3::0::0::ConnectionPointReference")
uml3_0_0_StructuredClassifier = Class(name="uml3::0::0::StructuredClassifier", is_abstract=True)
uml3_0_0_Connector = Class(name="uml3::0::0::Connector")
Association = Class(name="Association")
uml3_0_0_EncapsulatedClassifier = Class(name="uml3::0::0::EncapsulatedClassifier", is_abstract=True)
StructuredClassifier = Class(name="StructuredClassifier")
uml3_0_0_Image = Class(name="uml3::0::0::Image")
uml3_0_0_Profile = Class(name="uml3::0::0::Profile")
Package = Class(name="Package")
uml3_0_0_Model = Class(name="uml3::0::0::Model")
uml3_0_0_ExtensionEnd = Class(name="uml3::0::0::ExtensionEnd")
uml3_0_0_Stereotype = Class(name="uml3::0::0::Stereotype")
uml3_0_0_ConnectableElementTemplateParameter = Class(name="uml3::0::0::ConnectableElementTemplateParameter")
uml3_0_0_Collaboration = Class(name="uml3::0::0::Collaboration")
uml3_0_0_Include = Class(name="uml3::0::0::Include")
uml3_0_0_Extend = Class(name="uml3::0::0::Extend")
uml3_0_0_ExtensionPoint = Class(name="uml3::0::0::ExtensionPoint")
uml3_0_0_OperationTemplateParameter = Class(name="uml3::0::0::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
uml3_0_0_StructuralFeature = Class(name="uml3::0::0::StructuralFeature", is_abstract=True)
uml3_0_0_RedefinableTemplateSignature = Class(name="uml3::0::0::RedefinableTemplateSignature")
TemplateSignature = Class(name="TemplateSignature")
uml3_0_0_ClassifierTemplateParameter = Class(name="uml3::0::0::ClassifierTemplateParameter")
uml3_0_0_Expression = Class(name="uml3::0::0::Expression")
uml3_0_0_Usage = Class(name="uml3::0::0::Usage")
uml3_0_0_Enumeration = Class(name="uml3::0::0::Enumeration")
DataType = Class(name="DataType")
uml3_0_0_EnumerationLiteral = Class(name="uml3::0::0::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
uml3_0_0_InstanceSpecification = Class(name="uml3::0::0::InstanceSpecification")
Expression = Class(name="Expression")
uml3_0_0_Slot = Class(name="uml3::0::0::Slot")
uml3_0_0_PrimitiveType = Class(name="uml3::0::0::PrimitiveType")
uml3_0_0_LiteralSpecification = Class(name="uml3::0::0::LiteralSpecification", is_abstract=True)
uml3_0_0_LiteralInteger = Class(name="uml3::0::0::LiteralInteger")
LiteralSpecification = Class(name="LiteralSpecification")
uml3_0_0_LiteralString = Class(name="uml3::0::0::LiteralString")
uml3_0_0_LiteralBoolean = Class(name="uml3::0::0::LiteralBoolean")
uml3_0_0_LiteralNull = Class(name="uml3::0::0::LiteralNull")
uml3_0_0_InstanceValue = Class(name="uml3::0::0::InstanceValue")
uml3_0_0_FunctionBehavior = Class(name="uml3::0::0::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
uml3_0_0_OpaqueAction = Class(name="uml3::0::0::OpaqueAction")
Action = Class(name="Action")
uml3_0_0_InputPin = Class(name="uml3::0::0::InputPin")
uml3_0_0_OutputPin = Class(name="uml3::0::0::OutputPin")
uml3_0_0_Action = Class(name="uml3::0::0::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
uml3_0_0_ExecutableNode = Class(name="uml3::0::0::ExecutableNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
uml3_0_0_ExceptionHandler = Class(name="uml3::0::0::ExceptionHandler")
uml3_0_0_LiteralUnlimitedNatural = Class(name="uml3::0::0::LiteralUnlimitedNatural")
uml3_0_0_Activity = Class(name="uml3::0::0::Activity")
uml3_0_0_OpaqueBehavior = Class(name="uml3::0::0::OpaqueBehavior")
uml3_0_0_ActivityEdge = Class(name="uml3::0::0::ActivityEdge", is_abstract=True)
uml3_0_0_ActivityPartition = Class(name="uml3::0::0::ActivityPartition")
uml3_0_0_InterruptibleActivityRegion = Class(name="uml3::0::0::InterruptibleActivityRegion")
uml3_0_0_ActivityGroup = Class(name="uml3::0::0::ActivityGroup", is_abstract=True)
ActivityGroup = Class(name="ActivityGroup")
uml3_0_0_Variable = Class(name="uml3::0::0::Variable")
uml3_0_0_ActivityNode = Class(name="uml3::0::0::ActivityNode", is_abstract=True)
uml3_0_0_StructuredActivityNode = Class(name="uml3::0::0::StructuredActivityNode")
uml3_0_0_ObjectNode = Class(name="uml3::0::0::ObjectNode", is_abstract=True)
Pin = Class(name="Pin")
uml3_0_0_Pin = Class(name="uml3::0::0::Pin")
ObjectNode = Class(name="ObjectNode")
uml3_0_0_CallAction = Class(name="uml3::0::0::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
uml3_0_0_InvocationAction = Class(name="uml3::0::0::InvocationAction", is_abstract=True)
uml3_0_0_SendSignalAction = Class(name="uml3::0::0::SendSignalAction")
uml3_0_0_CallOperationAction = Class(name="uml3::0::0::CallOperationAction")
CallAction = Class(name="CallAction")
uml3_0_0_CallBehaviorAction = Class(name="uml3::0::0::CallBehaviorAction")
uml3_0_0_ControlNode = Class(name="uml3::0::0::ControlNode", is_abstract=True)
uml3_0_0_ControlFlow = Class(name="uml3::0::0::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
uml3_0_0_InitialNode = Class(name="uml3::0::0::InitialNode")
ControlNode = Class(name="ControlNode")
uml3_0_0_ActivityParameterNode = Class(name="uml3::0::0::ActivityParameterNode")
uml3_0_0_ValuePin = Class(name="uml3::0::0::ValuePin")
InputPin = Class(name="InputPin")
uml3_0_0_Message = Class(name="uml3::0::0::Message")
uml3_0_0_MessageEnd = Class(name="uml3::0::0::MessageEnd", is_abstract=True)
uml3_0_0_Interaction = Class(name="uml3::0::0::Interaction")
uml3_0_0_SequenceNode = Class(name="uml3::0::0::SequenceNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
InteractionFragment = Class(name="InteractionFragment")
uml3_0_0_Lifeline = Class(name="uml3::0::0::Lifeline")
uml3_0_0_InteractionFragment = Class(name="uml3::0::0::InteractionFragment", is_abstract=True)
uml3_0_0_Gate = Class(name="uml3::0::0::Gate")
uml3_0_0_GeneralOrdering = Class(name="uml3::0::0::GeneralOrdering")
uml3_0_0_PartDecomposition = Class(name="uml3::0::0::PartDecomposition")
InteractionUse = Class(name="InteractionUse")
uml3_0_0_InteractionUse = Class(name="uml3::0::0::InteractionUse")
uml3_0_0_InteractionOperand = Class(name="uml3::0::0::InteractionOperand")
MessageEnd = Class(name="MessageEnd")
uml3_0_0_OccurrenceSpecification = Class(name="uml3::0::0::OccurrenceSpecification")
uml3_0_0_InteractionConstraint = Class(name="uml3::0::0::InteractionConstraint")
Constraint = Class(name="Constraint")
uml3_0_0_ExecutionSpecification = Class(name="uml3::0::0::ExecutionSpecification", is_abstract=True)
uml3_0_0_StateInvariant = Class(name="uml3::0::0::StateInvariant")
uml3_0_0_ActionExecutionSpecification = Class(name="uml3::0::0::ActionExecutionSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
uml3_0_0_BehaviorExecutionSpecification = Class(name="uml3::0::0::BehaviorExecutionSpecification")
uml3_0_0_ExecutionEvent = Class(name="uml3::0::0::ExecutionEvent")
Event = Class(name="Event")
uml3_0_0_CreationEvent = Class(name="uml3::0::0::CreationEvent")
uml3_0_0_DestructionEvent = Class(name="uml3::0::0::DestructionEvent")
uml3_0_0_SendOperationEvent = Class(name="uml3::0::0::SendOperationEvent")
MessageEvent = Class(name="MessageEvent")
uml3_0_0_MessageEvent = Class(name="uml3::0::0::MessageEvent", is_abstract=True)
uml3_0_0_SendSignalEvent = Class(name="uml3::0::0::SendSignalEvent")
uml3_0_0_MessageOccurrenceSpecification = Class(name="uml3::0::0::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
uml3_0_0_ExecutionOccurrenceSpecification = Class(name="uml3::0::0::ExecutionOccurrenceSpecification")
uml3_0_0_ReceiveOperationEvent = Class(name="uml3::0::0::ReceiveOperationEvent")
uml3_0_0_ReceiveSignalEvent = Class(name="uml3::0::0::ReceiveSignalEvent")
uml3_0_0_Actor = Class(name="uml3::0::0::Actor")
uml3_0_0_CallEvent = Class(name="uml3::0::0::CallEvent")
uml3_0_0_ChangeEvent = Class(name="uml3::0::0::ChangeEvent")
uml3_0_0_SignalEvent = Class(name="uml3::0::0::SignalEvent")
uml3_0_0_AnyReceiveEvent = Class(name="uml3::0::0::AnyReceiveEvent")
uml3_0_0_ForkNode = Class(name="uml3::0::0::ForkNode")
uml3_0_0_FlowFinalNode = Class(name="uml3::0::0::FlowFinalNode")
FinalNode = Class(name="FinalNode")
uml3_0_0_FinalNode = Class(name="uml3::0::0::FinalNode", is_abstract=True)
uml3_0_0_CentralBufferNode = Class(name="uml3::0::0::CentralBufferNode")
uml3_0_0_MergeNode = Class(name="uml3::0::0::MergeNode")
uml3_0_0_DecisionNode = Class(name="uml3::0::0::DecisionNode")
uml3_0_0_ObjectFlow = Class(name="uml3::0::0::ObjectFlow")
uml3_0_0_ActivityFinalNode = Class(name="uml3::0::0::ActivityFinalNode")
uml3_0_0_ComponentRealization = Class(name="uml3::0::0::ComponentRealization")
uml3_0_0_Component = Class(name="uml3::0::0::Component")
uml3_0_0_Node = Class(name="uml3::0::0::Node")
uml3_0_0_CommunicationPath = Class(name="uml3::0::0::CommunicationPath")
uml3_0_0_Device = Class(name="uml3::0::0::Device")
Node = Class(name="Node")
uml3_0_0_ExecutionEnvironment = Class(name="uml3::0::0::ExecutionEnvironment")
uml3_0_0_CombinedFragment = Class(name="uml3::0::0::CombinedFragment")
uml3_0_0_Continuation = Class(name="uml3::0::0::Continuation")
uml3_0_0_ConsiderIgnoreFragment = Class(name="uml3::0::0::ConsiderIgnoreFragment")
CombinedFragment = Class(name="CombinedFragment")
uml3_0_0_CreateObjectAction = Class(name="uml3::0::0::CreateObjectAction")
uml3_0_0_DestroyObjectAction = Class(name="uml3::0::0::DestroyObjectAction")
uml3_0_0_TestIdentityAction = Class(name="uml3::0::0::TestIdentityAction")
uml3_0_0_ReadSelfAction = Class(name="uml3::0::0::ReadSelfAction")
uml3_0_0_StructuralFeatureAction = Class(name="uml3::0::0::StructuralFeatureAction", is_abstract=True)
uml3_0_0_ReadStructuralFeatureAction = Class(name="uml3::0::0::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
uml3_0_0_WriteStructuralFeatureAction = Class(name="uml3::0::0::WriteStructuralFeatureAction", is_abstract=True)
uml3_0_0_ClearStructuralFeatureAction = Class(name="uml3::0::0::ClearStructuralFeatureAction")
uml3_0_0_RemoveStructuralFeatureValueAction = Class(name="uml3::0::0::RemoveStructuralFeatureValueAction")
uml3_0_0_AddStructuralFeatureValueAction = Class(name="uml3::0::0::AddStructuralFeatureValueAction")
uml3_0_0_LinkAction = Class(name="uml3::0::0::LinkAction", is_abstract=True)
uml3_0_0_LinkEndData = Class(name="uml3::0::0::LinkEndData")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
uml3_0_0_QualifierValue = Class(name="uml3::0::0::QualifierValue")
uml3_0_0_ReadLinkAction = Class(name="uml3::0::0::ReadLinkAction")
LinkAction = Class(name="LinkAction")
uml3_0_0_LinkEndCreationData = Class(name="uml3::0::0::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
uml3_0_0_CreateLinkAction = Class(name="uml3::0::0::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
uml3_0_0_WriteLinkAction = Class(name="uml3::0::0::WriteLinkAction", is_abstract=True)
uml3_0_0_DestroyLinkAction = Class(name="uml3::0::0::DestroyLinkAction")
uml3_0_0_LinkEndDestructionData = Class(name="uml3::0::0::LinkEndDestructionData")
uml3_0_0_ClearAssociationAction = Class(name="uml3::0::0::ClearAssociationAction")
uml3_0_0_BroadcastSignalAction = Class(name="uml3::0::0::BroadcastSignalAction")
uml3_0_0_SendObjectAction = Class(name="uml3::0::0::SendObjectAction")
uml3_0_0_ValueSpecificationAction = Class(name="uml3::0::0::ValueSpecificationAction")
uml3_0_0_TimeExpression = Class(name="uml3::0::0::TimeExpression")
uml3_0_0_Observation = Class(name="uml3::0::0::Observation", is_abstract=True)
uml3_0_0_Duration = Class(name="uml3::0::0::Duration")
uml3_0_0_DurationInterval = Class(name="uml3::0::0::DurationInterval")
Interval = Class(name="Interval")
uml3_0_0_Interval = Class(name="uml3::0::0::Interval")
uml3_0_0_TimeConstraint = Class(name="uml3::0::0::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
uml3_0_0_IntervalConstraint = Class(name="uml3::0::0::IntervalConstraint")
uml3_0_0_TimeInterval = Class(name="uml3::0::0::TimeInterval")
uml3_0_0_DurationConstraint = Class(name="uml3::0::0::DurationConstraint")
uml3_0_0_TimeObservation = Class(name="uml3::0::0::TimeObservation")
Observation = Class(name="Observation")
uml3_0_0_DurationObservation = Class(name="uml3::0::0::DurationObservation")
uml3_0_0_FinalState = Class(name="uml3::0::0::FinalState")
State = Class(name="State")
uml3_0_0_TimeEvent = Class(name="uml3::0::0::TimeEvent")
uml3_0_0_VariableAction = Class(name="uml3::0::0::VariableAction", is_abstract=True)
uml3_0_0_WriteVariableAction = Class(name="uml3::0::0::WriteVariableAction", is_abstract=True)
uml3_0_0_ClearVariableAction = Class(name="uml3::0::0::ClearVariableAction")
uml3_0_0_AddVariableValueAction = Class(name="uml3::0::0::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
uml3_0_0_RemoveVariableValueAction = Class(name="uml3::0::0::RemoveVariableValueAction")
uml3_0_0_RaiseExceptionAction = Class(name="uml3::0::0::RaiseExceptionAction")
uml3_0_0_ActionInputPin = Class(name="uml3::0::0::ActionInputPin")
uml3_0_0_InformationItem = Class(name="uml3::0::0::InformationItem")
uml3_0_0_ReadVariableAction = Class(name="uml3::0::0::ReadVariableAction")
VariableAction = Class(name="VariableAction")
uml3_0_0_ReadExtentAction = Class(name="uml3::0::0::ReadExtentAction")
uml3_0_0_ReclassifyObjectAction = Class(name="uml3::0::0::ReclassifyObjectAction")
uml3_0_0_InformationFlow = Class(name="uml3::0::0::InformationFlow")
uml3_0_0_ReadIsClassifiedObjectAction = Class(name="uml3::0::0::ReadIsClassifiedObjectAction")
uml3_0_0_StartClassifierBehaviorAction = Class(name="uml3::0::0::StartClassifierBehaviorAction")
uml3_0_0_ReadLinkObjectEndAction = Class(name="uml3::0::0::ReadLinkObjectEndAction")
uml3_0_0_ReadLinkObjectEndQualifierAction = Class(name="uml3::0::0::ReadLinkObjectEndQualifierAction")
uml3_0_0_CreateLinkObjectAction = Class(name="uml3::0::0::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
uml3_0_0_AcceptEventAction = Class(name="uml3::0::0::AcceptEventAction")
uml3_0_0_AcceptCallAction = Class(name="uml3::0::0::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
uml3_0_0_ReplyAction = Class(name="uml3::0::0::ReplyAction")
uml3_0_0_UnmarshallAction = Class(name="uml3::0::0::UnmarshallAction")
uml3_0_0_ReduceAction = Class(name="uml3::0::0::ReduceAction")
uml3_0_0_StartObjectBehaviorAction = Class(name="uml3::0::0::StartObjectBehaviorAction")
uml3_0_0_JoinNode = Class(name="uml3::0::0::JoinNode")
uml3_0_0_DataStoreNode = Class(name="uml3::0::0::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
uml3_0_0_ConditionalNode = Class(name="uml3::0::0::ConditionalNode")
uml3_0_0_Clause = Class(name="uml3::0::0::Clause")
uml3_0_0_ExpansionNode = Class(name="uml3::0::0::ExpansionNode")
uml3_0_0_ExpansionRegion = Class(name="uml3::0::0::ExpansionRegion")
uml3_0_0_LoopNode = Class(name="uml3::0::0::LoopNode")
uml3_0_0_ProtocolTransition = Class(name="uml3::0::0::ProtocolTransition")
Transition = Class(name="Transition")
uml3_0_0_AssociationClass = Class(name="uml3::0::0::AssociationClass")

# uml3_0_0_Package class attributes and methods

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# TemplateableElement class attributes and methods

# uml3_0_0_Type class attributes and methods

# uml3_0_0_PackageMerge class attributes and methods

# uml3_0_0_PackageableElement class attributes and methods

# uml3_0_0_Comment class attributes and methods
uml3_0_0_Comment_body: Property = Property(name="body", type=StringType)
uml3_0_0_Comment.attributes={uml3_0_0_Comment_body}

# Element class attributes and methods

# uml3_0_0_Element class attributes and methods

# EModelElement class attributes and methods

# uml3_0_0_Namespace class attributes and methods

# uml3_0_0_StringExpression class attributes and methods

# DirectedRelationship class attributes and methods

# uml3_0_0_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# uml3_0_0_Relationship class attributes and methods

# uml3_0_0_ProfileApplication class attributes and methods
uml3_0_0_ProfileApplication_isStrict: Property = Property(name="isStrict", type=StringType)
uml3_0_0_ProfileApplication.attributes={uml3_0_0_ProfileApplication_isStrict}

# NamedElement class attributes and methods

# ParameterableElement class attributes and methods

# uml3_0_0_NamedElement class attributes and methods
uml3_0_0_NamedElement_name: Property = Property(name="name", type=StringType)
uml3_0_0_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml3_0_0_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
uml3_0_0_NamedElement.attributes={uml3_0_0_NamedElement_visibility, uml3_0_0_NamedElement_qualifiedName, uml3_0_0_NamedElement_name}

# uml3_0_0_Dependency class attributes and methods

# uml3_0_0_ElementImport class attributes and methods
uml3_0_0_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
uml3_0_0_ElementImport_alias: Property = Property(name="alias", type=StringType)
uml3_0_0_ElementImport.attributes={uml3_0_0_ElementImport_alias, uml3_0_0_ElementImport_visibility}

# uml3_0_0_PackageImport class attributes and methods
uml3_0_0_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
uml3_0_0_PackageImport.attributes={uml3_0_0_PackageImport_visibility}

# uml3_0_0_Constraint class attributes and methods

# uml3_0_0_Association class attributes and methods
uml3_0_0_Association_isDerived: Property = Property(name="isDerived", type=StringType)
uml3_0_0_Association.attributes={uml3_0_0_Association_isDerived}

# Classifier class attributes and methods

# uml3_0_0_Property class attributes and methods
uml3_0_0_Property_isDerived: Property = Property(name="isDerived", type=StringType)
uml3_0_0_Property_aggregation: Property = Property(name="aggregation", type=StringType)
uml3_0_0_Property_isComposite: Property = Property(name="isComposite", type=StringType)
uml3_0_0_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
uml3_0_0_Property_default: Property = Property(name="default", type=StringType)
uml3_0_0_Property.attributes={uml3_0_0_Property_default, uml3_0_0_Property_isComposite, uml3_0_0_Property_isDerivedUnion, uml3_0_0_Property_isDerived, uml3_0_0_Property_aggregation}

# uml3_0_0_Classifier class attributes and methods
uml3_0_0_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml3_0_0_Classifier.attributes={uml3_0_0_Classifier_isAbstract}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# uml3_0_0_Generalization class attributes and methods
uml3_0_0_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
uml3_0_0_Generalization.attributes={uml3_0_0_Generalization_isSubstitutable}

# uml3_0_0_GeneralizationSet class attributes and methods
uml3_0_0_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
uml3_0_0_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
uml3_0_0_GeneralizationSet.attributes={uml3_0_0_GeneralizationSet_isDisjoint, uml3_0_0_GeneralizationSet_isCovering}

# uml3_0_0_Feature class attributes and methods
uml3_0_0_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
uml3_0_0_Feature.attributes={uml3_0_0_Feature_isStatic}

# uml3_0_0_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# uml3_0_0_TypedElement class attributes and methods

# uml3_0_0_CollaborationUse class attributes and methods

# uml3_0_0_UseCase class attributes and methods

# uml3_0_0_RedefinableElement class attributes and methods
uml3_0_0_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
uml3_0_0_RedefinableElement.attributes={uml3_0_0_RedefinableElement_isLeaf}

# uml3_0_0_TemplateableElement class attributes and methods

# uml3_0_0_TemplateBinding class attributes and methods

# uml3_0_0_TemplateSignature class attributes and methods

# uml3_0_0_Substitution class attributes and methods

# uml3_0_0_ParameterableElement class attributes and methods

# uml3_0_0_TemplateParameterSubstitution class attributes and methods

# uml3_0_0_TemplateParameter class attributes and methods

# Realization class attributes and methods

# ConnectableElement class attributes and methods

# MultiplicityElement class attributes and methods

# uml3_0_0_ParameterSet class attributes and methods

# uml3_0_0_Operation class attributes and methods
uml3_0_0_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
uml3_0_0_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml3_0_0_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
uml3_0_0_Operation_lower: Property = Property(name="lower", type=StringType)
uml3_0_0_Operation_upper: Property = Property(name="upper", type=StringType)
uml3_0_0_Operation.attributes={uml3_0_0_Operation_isOrdered, uml3_0_0_Operation_isQuery, uml3_0_0_Operation_lower, uml3_0_0_Operation_upper, uml3_0_0_Operation_isUnique}

# uml3_0_0_MultiplicityElement class attributes and methods
uml3_0_0_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml3_0_0_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
uml3_0_0_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
uml3_0_0_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
uml3_0_0_MultiplicityElement.attributes={uml3_0_0_MultiplicityElement_lower, uml3_0_0_MultiplicityElement_upper, uml3_0_0_MultiplicityElement_isOrdered, uml3_0_0_MultiplicityElement_isUnique}

# uml3_0_0_Realization class attributes and methods

# Abstraction class attributes and methods

# uml3_0_0_Abstraction class attributes and methods

# Dependency class attributes and methods

# uml3_0_0_OpaqueExpression class attributes and methods
uml3_0_0_OpaqueExpression_body: Property = Property(name="body", type=StringType)
uml3_0_0_OpaqueExpression_language: Property = Property(name="language", type=StringType)
uml3_0_0_OpaqueExpression.attributes={uml3_0_0_OpaqueExpression_language, uml3_0_0_OpaqueExpression_body}

# ValueSpecification class attributes and methods

# uml3_0_0_Parameter class attributes and methods
uml3_0_0_Parameter_direction: Property = Property(name="direction", type=StringType)
uml3_0_0_Parameter_default: Property = Property(name="default", type=StringType)
uml3_0_0_Parameter_isException: Property = Property(name="isException", type=StringType)
uml3_0_0_Parameter_isStream: Property = Property(name="isStream", type=StringType)
uml3_0_0_Parameter_effect: Property = Property(name="effect", type=StringType)
uml3_0_0_Parameter.attributes={uml3_0_0_Parameter_isException, uml3_0_0_Parameter_default, uml3_0_0_Parameter_direction, uml3_0_0_Parameter_effect, uml3_0_0_Parameter_isStream}

# uml3_0_0_Behavior class attributes and methods
uml3_0_0_Behavior_isReentrant: Property = Property(name="isReentrant", type=StringType)
uml3_0_0_Behavior.attributes={uml3_0_0_Behavior_isReentrant}

# StructuralFeature class attributes and methods

# DeploymentTarget class attributes and methods

# uml3_0_0_Class class attributes and methods
uml3_0_0_Class_isActive: Property = Property(name="isActive", type=StringType)
uml3_0_0_Class.attributes={uml3_0_0_Class_isActive}

# uml3_0_0_DataType class attributes and methods

# uml3_0_0_ConnectableElement class attributes and methods

# uml3_0_0_ConnectorEnd class attributes and methods

# uml3_0_0_DeploymentTarget class attributes and methods

# uml3_0_0_Deployment class attributes and methods

# uml3_0_0_DeployedArtifact class attributes and methods

# uml3_0_0_DeploymentSpecification class attributes and methods
uml3_0_0_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
uml3_0_0_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
uml3_0_0_DeploymentSpecification.attributes={uml3_0_0_DeploymentSpecification_deploymentLocation, uml3_0_0_DeploymentSpecification_executionLocation}

# Artifact class attributes and methods

# uml3_0_0_Artifact class attributes and methods
uml3_0_0_Artifact_fileName: Property = Property(name="fileName", type=StringType)
uml3_0_0_Artifact.attributes={uml3_0_0_Artifact_fileName}

# DeployedArtifact class attributes and methods

# uml3_0_0_Manifestation class attributes and methods

# BehavioralFeature class attributes and methods

# uml3_0_0_Interface class attributes and methods

# uml3_0_0_BehavioralFeature class attributes and methods
uml3_0_0_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml3_0_0_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
uml3_0_0_BehavioralFeature.attributes={uml3_0_0_BehavioralFeature_isAbstract, uml3_0_0_BehavioralFeature_concurrency}

# Feature class attributes and methods

# Class class attributes and methods

# uml3_0_0_BehavioredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# BehavioredClassifier class attributes and methods

# uml3_0_0_Reception class attributes and methods

# uml3_0_0_Extension class attributes and methods
uml3_0_0_Extension_isRequired: Property = Property(name="isRequired", type=StringType)
uml3_0_0_Extension.attributes={uml3_0_0_Extension_isRequired}

# uml3_0_0_InterfaceRealization class attributes and methods

# uml3_0_0_Trigger class attributes and methods

# uml3_0_0_ProtocolStateMachine class attributes and methods

# uml3_0_0_Signal class attributes and methods

# StateMachine class attributes and methods

# uml3_0_0_ProtocolConformance class attributes and methods

# uml3_0_0_Region class attributes and methods

# uml3_0_0_State class attributes and methods
uml3_0_0_State_isComposite: Property = Property(name="isComposite", type=StringType)
uml3_0_0_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
uml3_0_0_State_isSimple: Property = Property(name="isSimple", type=StringType)
uml3_0_0_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
uml3_0_0_State.attributes={uml3_0_0_State_isOrthogonal, uml3_0_0_State_isSimple, uml3_0_0_State_isComposite, uml3_0_0_State_isSubmachineState}

# uml3_0_0_Pseudostate class attributes and methods
uml3_0_0_Pseudostate_kind: Property = Property(name="kind", type=StringType)
uml3_0_0_Pseudostate.attributes={uml3_0_0_Pseudostate_kind}

# uml3_0_0_Vertex class attributes and methods

# uml3_0_0_Transition class attributes and methods
uml3_0_0_Transition_kind: Property = Property(name="kind", type=StringType)
uml3_0_0_Transition.attributes={uml3_0_0_Transition_kind}

# uml3_0_0_StateMachine class attributes and methods

# Behavior class attributes and methods

# uml3_0_0_Event class attributes and methods

# uml3_0_0_Port class attributes and methods
uml3_0_0_Port_isBehavior: Property = Property(name="isBehavior", type=StringType)
uml3_0_0_Port_isService: Property = Property(name="isService", type=StringType)
uml3_0_0_Port.attributes={uml3_0_0_Port_isService, uml3_0_0_Port_isBehavior}

# Property class attributes and methods

# Vertex class attributes and methods

# uml3_0_0_ConnectionPointReference class attributes and methods

# uml3_0_0_StructuredClassifier class attributes and methods

# uml3_0_0_Connector class attributes and methods
uml3_0_0_Connector_kind: Property = Property(name="kind", type=StringType)
uml3_0_0_Connector.attributes={uml3_0_0_Connector_kind}

# Association class attributes and methods

# uml3_0_0_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# uml3_0_0_Image class attributes and methods
uml3_0_0_Image_content: Property = Property(name="content", type=StringType)
uml3_0_0_Image_location: Property = Property(name="location", type=StringType)
uml3_0_0_Image_format: Property = Property(name="format", type=StringType)
uml3_0_0_Image.attributes={uml3_0_0_Image_format, uml3_0_0_Image_location, uml3_0_0_Image_content}

# uml3_0_0_Profile class attributes and methods

# Package class attributes and methods

# uml3_0_0_Model class attributes and methods
uml3_0_0_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
uml3_0_0_Model.attributes={uml3_0_0_Model_viewpoint}

# uml3_0_0_ExtensionEnd class attributes and methods

# uml3_0_0_Stereotype class attributes and methods

# uml3_0_0_ConnectableElementTemplateParameter class attributes and methods

# uml3_0_0_Collaboration class attributes and methods

# uml3_0_0_Include class attributes and methods

# uml3_0_0_Extend class attributes and methods

# uml3_0_0_ExtensionPoint class attributes and methods

# uml3_0_0_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# uml3_0_0_StructuralFeature class attributes and methods
uml3_0_0_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
uml3_0_0_StructuralFeature.attributes={uml3_0_0_StructuralFeature_isReadOnly}

# uml3_0_0_RedefinableTemplateSignature class attributes and methods

# TemplateSignature class attributes and methods

# uml3_0_0_ClassifierTemplateParameter class attributes and methods
uml3_0_0_ClassifierTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=StringType)
uml3_0_0_ClassifierTemplateParameter.attributes={uml3_0_0_ClassifierTemplateParameter_allowSubstitutable}

# uml3_0_0_Expression class attributes and methods
uml3_0_0_Expression_symbol: Property = Property(name="symbol", type=StringType)
uml3_0_0_Expression.attributes={uml3_0_0_Expression_symbol}

# uml3_0_0_Usage class attributes and methods

# uml3_0_0_Enumeration class attributes and methods

# DataType class attributes and methods

# uml3_0_0_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# uml3_0_0_InstanceSpecification class attributes and methods

# Expression class attributes and methods

# uml3_0_0_Slot class attributes and methods

# uml3_0_0_PrimitiveType class attributes and methods

# uml3_0_0_LiteralSpecification class attributes and methods

# uml3_0_0_LiteralInteger class attributes and methods
uml3_0_0_LiteralInteger_value: Property = Property(name="value", type=StringType)
uml3_0_0_LiteralInteger.attributes={uml3_0_0_LiteralInteger_value}

# LiteralSpecification class attributes and methods

# uml3_0_0_LiteralString class attributes and methods
uml3_0_0_LiteralString_value: Property = Property(name="value", type=StringType)
uml3_0_0_LiteralString.attributes={uml3_0_0_LiteralString_value}

# uml3_0_0_LiteralBoolean class attributes and methods
uml3_0_0_LiteralBoolean_value: Property = Property(name="value", type=StringType)
uml3_0_0_LiteralBoolean.attributes={uml3_0_0_LiteralBoolean_value}

# uml3_0_0_LiteralNull class attributes and methods

# uml3_0_0_InstanceValue class attributes and methods

# uml3_0_0_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# uml3_0_0_OpaqueAction class attributes and methods
uml3_0_0_OpaqueAction_body: Property = Property(name="body", type=StringType)
uml3_0_0_OpaqueAction_language: Property = Property(name="language", type=StringType)
uml3_0_0_OpaqueAction.attributes={uml3_0_0_OpaqueAction_language, uml3_0_0_OpaqueAction_body}

# Action class attributes and methods

# uml3_0_0_InputPin class attributes and methods

# uml3_0_0_OutputPin class attributes and methods

# uml3_0_0_Action class attributes and methods

# ExecutableNode class attributes and methods

# uml3_0_0_ExecutableNode class attributes and methods

# ActivityNode class attributes and methods

# uml3_0_0_ExceptionHandler class attributes and methods

# uml3_0_0_LiteralUnlimitedNatural class attributes and methods
uml3_0_0_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
uml3_0_0_LiteralUnlimitedNatural.attributes={uml3_0_0_LiteralUnlimitedNatural_value}

# uml3_0_0_Activity class attributes and methods
uml3_0_0_Activity_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
uml3_0_0_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=StringType)
uml3_0_0_Activity.attributes={uml3_0_0_Activity_isSingleExecution, uml3_0_0_Activity_isReadOnly}

# uml3_0_0_OpaqueBehavior class attributes and methods
uml3_0_0_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
uml3_0_0_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
uml3_0_0_OpaqueBehavior.attributes={uml3_0_0_OpaqueBehavior_body, uml3_0_0_OpaqueBehavior_language}

# uml3_0_0_ActivityEdge class attributes and methods

# uml3_0_0_ActivityPartition class attributes and methods
uml3_0_0_ActivityPartition_isDimension: Property = Property(name="isDimension", type=StringType)
uml3_0_0_ActivityPartition_isExternal: Property = Property(name="isExternal", type=StringType)
uml3_0_0_ActivityPartition.attributes={uml3_0_0_ActivityPartition_isExternal, uml3_0_0_ActivityPartition_isDimension}

# uml3_0_0_InterruptibleActivityRegion class attributes and methods

# uml3_0_0_ActivityGroup class attributes and methods

# ActivityGroup class attributes and methods

# uml3_0_0_Variable class attributes and methods

# uml3_0_0_ActivityNode class attributes and methods

# uml3_0_0_StructuredActivityNode class attributes and methods
uml3_0_0_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=StringType)
uml3_0_0_StructuredActivityNode.attributes={uml3_0_0_StructuredActivityNode_mustIsolate}

# uml3_0_0_ObjectNode class attributes and methods
uml3_0_0_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
uml3_0_0_ObjectNode_isControlType: Property = Property(name="isControlType", type=StringType)
uml3_0_0_ObjectNode.attributes={uml3_0_0_ObjectNode_ordering, uml3_0_0_ObjectNode_isControlType}

# Pin class attributes and methods

# uml3_0_0_Pin class attributes and methods
uml3_0_0_Pin_isControl: Property = Property(name="isControl", type=StringType)
uml3_0_0_Pin.attributes={uml3_0_0_Pin_isControl}

# ObjectNode class attributes and methods

# uml3_0_0_CallAction class attributes and methods
uml3_0_0_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=StringType)
uml3_0_0_CallAction.attributes={uml3_0_0_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# uml3_0_0_InvocationAction class attributes and methods

# uml3_0_0_SendSignalAction class attributes and methods

# uml3_0_0_CallOperationAction class attributes and methods

# CallAction class attributes and methods

# uml3_0_0_CallBehaviorAction class attributes and methods

# uml3_0_0_ControlNode class attributes and methods

# uml3_0_0_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# uml3_0_0_InitialNode class attributes and methods

# ControlNode class attributes and methods

# uml3_0_0_ActivityParameterNode class attributes and methods

# uml3_0_0_ValuePin class attributes and methods

# InputPin class attributes and methods

# uml3_0_0_Message class attributes and methods
uml3_0_0_Message_messageKind: Property = Property(name="messageKind", type=StringType)
uml3_0_0_Message_messageSort: Property = Property(name="messageSort", type=StringType)
uml3_0_0_Message.attributes={uml3_0_0_Message_messageSort, uml3_0_0_Message_messageKind}

# uml3_0_0_MessageEnd class attributes and methods

# uml3_0_0_Interaction class attributes and methods

# uml3_0_0_SequenceNode class attributes and methods

# StructuredActivityNode class attributes and methods

# InteractionFragment class attributes and methods

# uml3_0_0_Lifeline class attributes and methods

# uml3_0_0_InteractionFragment class attributes and methods

# uml3_0_0_Gate class attributes and methods

# uml3_0_0_GeneralOrdering class attributes and methods

# uml3_0_0_PartDecomposition class attributes and methods

# InteractionUse class attributes and methods

# uml3_0_0_InteractionUse class attributes and methods

# uml3_0_0_InteractionOperand class attributes and methods

# MessageEnd class attributes and methods

# uml3_0_0_OccurrenceSpecification class attributes and methods

# uml3_0_0_InteractionConstraint class attributes and methods

# Constraint class attributes and methods

# uml3_0_0_ExecutionSpecification class attributes and methods

# uml3_0_0_StateInvariant class attributes and methods

# uml3_0_0_ActionExecutionSpecification class attributes and methods

# ExecutionSpecification class attributes and methods

# uml3_0_0_BehaviorExecutionSpecification class attributes and methods

# uml3_0_0_ExecutionEvent class attributes and methods

# Event class attributes and methods

# uml3_0_0_CreationEvent class attributes and methods

# uml3_0_0_DestructionEvent class attributes and methods

# uml3_0_0_SendOperationEvent class attributes and methods

# MessageEvent class attributes and methods

# uml3_0_0_MessageEvent class attributes and methods

# uml3_0_0_SendSignalEvent class attributes and methods

# uml3_0_0_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# uml3_0_0_ExecutionOccurrenceSpecification class attributes and methods

# uml3_0_0_ReceiveOperationEvent class attributes and methods

# uml3_0_0_ReceiveSignalEvent class attributes and methods

# uml3_0_0_Actor class attributes and methods

# uml3_0_0_CallEvent class attributes and methods

# uml3_0_0_ChangeEvent class attributes and methods

# uml3_0_0_SignalEvent class attributes and methods

# uml3_0_0_AnyReceiveEvent class attributes and methods

# uml3_0_0_ForkNode class attributes and methods

# uml3_0_0_FlowFinalNode class attributes and methods

# FinalNode class attributes and methods

# uml3_0_0_FinalNode class attributes and methods

# uml3_0_0_CentralBufferNode class attributes and methods

# uml3_0_0_MergeNode class attributes and methods

# uml3_0_0_DecisionNode class attributes and methods

# uml3_0_0_ObjectFlow class attributes and methods
uml3_0_0_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=StringType)
uml3_0_0_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=StringType)
uml3_0_0_ObjectFlow.attributes={uml3_0_0_ObjectFlow_isMulticast, uml3_0_0_ObjectFlow_isMultireceive}

# uml3_0_0_ActivityFinalNode class attributes and methods

# uml3_0_0_ComponentRealization class attributes and methods

# uml3_0_0_Component class attributes and methods
uml3_0_0_Component_isIndirectlyInstantiated: Property = Property(name="isIndirectlyInstantiated", type=StringType)
uml3_0_0_Component.attributes={uml3_0_0_Component_isIndirectlyInstantiated}

# uml3_0_0_Node class attributes and methods

# uml3_0_0_CommunicationPath class attributes and methods

# uml3_0_0_Device class attributes and methods

# Node class attributes and methods

# uml3_0_0_ExecutionEnvironment class attributes and methods

# uml3_0_0_CombinedFragment class attributes and methods
uml3_0_0_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
uml3_0_0_CombinedFragment.attributes={uml3_0_0_CombinedFragment_interactionOperator}

# uml3_0_0_Continuation class attributes and methods
uml3_0_0_Continuation_setting: Property = Property(name="setting", type=StringType)
uml3_0_0_Continuation.attributes={uml3_0_0_Continuation_setting}

# uml3_0_0_ConsiderIgnoreFragment class attributes and methods

# CombinedFragment class attributes and methods

# uml3_0_0_CreateObjectAction class attributes and methods

# uml3_0_0_DestroyObjectAction class attributes and methods
uml3_0_0_DestroyObjectAction_isDestroyLinks: Property = Property(name="isDestroyLinks", type=StringType)
uml3_0_0_DestroyObjectAction_isDestroyOwnedObjects: Property = Property(name="isDestroyOwnedObjects", type=StringType)
uml3_0_0_DestroyObjectAction.attributes={uml3_0_0_DestroyObjectAction_isDestroyOwnedObjects, uml3_0_0_DestroyObjectAction_isDestroyLinks}

# uml3_0_0_TestIdentityAction class attributes and methods

# uml3_0_0_ReadSelfAction class attributes and methods

# uml3_0_0_StructuralFeatureAction class attributes and methods

# uml3_0_0_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# uml3_0_0_WriteStructuralFeatureAction class attributes and methods

# uml3_0_0_ClearStructuralFeatureAction class attributes and methods

# uml3_0_0_RemoveStructuralFeatureValueAction class attributes and methods
uml3_0_0_RemoveStructuralFeatureValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
uml3_0_0_RemoveStructuralFeatureValueAction.attributes={uml3_0_0_RemoveStructuralFeatureValueAction_isRemoveDuplicates}

# uml3_0_0_AddStructuralFeatureValueAction class attributes and methods
uml3_0_0_AddStructuralFeatureValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml3_0_0_AddStructuralFeatureValueAction.attributes={uml3_0_0_AddStructuralFeatureValueAction_isReplaceAll}

# uml3_0_0_LinkAction class attributes and methods

# uml3_0_0_LinkEndData class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# uml3_0_0_QualifierValue class attributes and methods

# uml3_0_0_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# uml3_0_0_LinkEndCreationData class attributes and methods
uml3_0_0_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml3_0_0_LinkEndCreationData.attributes={uml3_0_0_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# uml3_0_0_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# uml3_0_0_WriteLinkAction class attributes and methods

# uml3_0_0_DestroyLinkAction class attributes and methods

# uml3_0_0_LinkEndDestructionData class attributes and methods
uml3_0_0_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=StringType)
uml3_0_0_LinkEndDestructionData.attributes={uml3_0_0_LinkEndDestructionData_isDestroyDuplicates}

# uml3_0_0_ClearAssociationAction class attributes and methods

# uml3_0_0_BroadcastSignalAction class attributes and methods

# uml3_0_0_SendObjectAction class attributes and methods

# uml3_0_0_ValueSpecificationAction class attributes and methods

# uml3_0_0_TimeExpression class attributes and methods

# uml3_0_0_Observation class attributes and methods

# uml3_0_0_Duration class attributes and methods

# uml3_0_0_DurationInterval class attributes and methods

# Interval class attributes and methods

# uml3_0_0_Interval class attributes and methods

# uml3_0_0_TimeConstraint class attributes and methods
uml3_0_0_TimeConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml3_0_0_TimeConstraint.attributes={uml3_0_0_TimeConstraint_firstEvent}

# IntervalConstraint class attributes and methods

# uml3_0_0_IntervalConstraint class attributes and methods

# uml3_0_0_TimeInterval class attributes and methods

# uml3_0_0_DurationConstraint class attributes and methods
uml3_0_0_DurationConstraint_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml3_0_0_DurationConstraint.attributes={uml3_0_0_DurationConstraint_firstEvent}

# uml3_0_0_TimeObservation class attributes and methods
uml3_0_0_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml3_0_0_TimeObservation.attributes={uml3_0_0_TimeObservation_firstEvent}

# Observation class attributes and methods

# uml3_0_0_DurationObservation class attributes and methods
uml3_0_0_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=StringType)
uml3_0_0_DurationObservation.attributes={uml3_0_0_DurationObservation_firstEvent}

# uml3_0_0_FinalState class attributes and methods

# State class attributes and methods

# uml3_0_0_TimeEvent class attributes and methods
uml3_0_0_TimeEvent_isRelative: Property = Property(name="isRelative", type=StringType)
uml3_0_0_TimeEvent.attributes={uml3_0_0_TimeEvent_isRelative}

# uml3_0_0_VariableAction class attributes and methods

# uml3_0_0_WriteVariableAction class attributes and methods

# uml3_0_0_ClearVariableAction class attributes and methods

# uml3_0_0_AddVariableValueAction class attributes and methods
uml3_0_0_AddVariableValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml3_0_0_AddVariableValueAction.attributes={uml3_0_0_AddVariableValueAction_isReplaceAll}

# WriteVariableAction class attributes and methods

# uml3_0_0_RemoveVariableValueAction class attributes and methods
uml3_0_0_RemoveVariableValueAction_isRemoveDuplicates: Property = Property(name="isRemoveDuplicates", type=StringType)
uml3_0_0_RemoveVariableValueAction.attributes={uml3_0_0_RemoveVariableValueAction_isRemoveDuplicates}

# uml3_0_0_RaiseExceptionAction class attributes and methods

# uml3_0_0_ActionInputPin class attributes and methods

# uml3_0_0_InformationItem class attributes and methods

# uml3_0_0_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# uml3_0_0_ReadExtentAction class attributes and methods

# uml3_0_0_ReclassifyObjectAction class attributes and methods
uml3_0_0_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=StringType)
uml3_0_0_ReclassifyObjectAction.attributes={uml3_0_0_ReclassifyObjectAction_isReplaceAll}

# uml3_0_0_InformationFlow class attributes and methods

# uml3_0_0_ReadIsClassifiedObjectAction class attributes and methods
uml3_0_0_ReadIsClassifiedObjectAction_isDirect: Property = Property(name="isDirect", type=StringType)
uml3_0_0_ReadIsClassifiedObjectAction.attributes={uml3_0_0_ReadIsClassifiedObjectAction_isDirect}

# uml3_0_0_StartClassifierBehaviorAction class attributes and methods

# uml3_0_0_ReadLinkObjectEndAction class attributes and methods

# uml3_0_0_ReadLinkObjectEndQualifierAction class attributes and methods

# uml3_0_0_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# uml3_0_0_AcceptEventAction class attributes and methods
uml3_0_0_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=StringType)
uml3_0_0_AcceptEventAction.attributes={uml3_0_0_AcceptEventAction_isUnmarshall}

# uml3_0_0_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# uml3_0_0_ReplyAction class attributes and methods

# uml3_0_0_UnmarshallAction class attributes and methods

# uml3_0_0_ReduceAction class attributes and methods
uml3_0_0_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml3_0_0_ReduceAction.attributes={uml3_0_0_ReduceAction_isOrdered}

# uml3_0_0_StartObjectBehaviorAction class attributes and methods

# uml3_0_0_JoinNode class attributes and methods
uml3_0_0_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=StringType)
uml3_0_0_JoinNode.attributes={uml3_0_0_JoinNode_isCombineDuplicate}

# uml3_0_0_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# uml3_0_0_ConditionalNode class attributes and methods
uml3_0_0_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=StringType)
uml3_0_0_ConditionalNode_isAssured: Property = Property(name="isAssured", type=StringType)
uml3_0_0_ConditionalNode.attributes={uml3_0_0_ConditionalNode_isDeterminate, uml3_0_0_ConditionalNode_isAssured}

# uml3_0_0_Clause class attributes and methods

# uml3_0_0_ExpansionNode class attributes and methods

# uml3_0_0_ExpansionRegion class attributes and methods
uml3_0_0_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
uml3_0_0_ExpansionRegion.attributes={uml3_0_0_ExpansionRegion_mode}

# uml3_0_0_LoopNode class attributes and methods
uml3_0_0_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=StringType)
uml3_0_0_LoopNode.attributes={uml3_0_0_LoopNode_isTestedFirst}

# uml3_0_0_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# uml3_0_0_AssociationClass class attributes and methods

# Relationships
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml3_0_0_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=uml3_0_0_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="uml3_0_0_Comment8", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Element7", type=uml3_0_0_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType9: BinaryAssociation = BinaryAssociation(
    name="ownedType9",
    ends={
        Property(name="Type", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=uml3_0_0_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge10: BinaryAssociation = BinaryAssociation(
    name="packageMerge10",
    ends={
        Property(name="PackageMerge", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=uml3_0_0_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement11: BinaryAssociation = BinaryAssociation(
    name="packagedElement11",
    ends={
        Property(name="uml3_0_0_PackageableElement", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Package", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage13: BinaryAssociation = BinaryAssociation(
    name="nestedPackage13",
    ends={
        Property(name="Package", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=uml3_0_0_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage15: BinaryAssociation = BinaryAssociation(
    name="nestingPackage15",
    ends={
        Property(name="Package16", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=uml3_0_0_Package, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement0: BinaryAssociation = BinaryAssociation(
    name="annotatedElement0",
    ends={
        Property(name="uml3_0_0_Element", type=uml3_0_0_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Comment", type=uml3_0_0_Element, multiplicity=Multiplicity(0, 9999))
    }
)
namespace19: BinaryAssociation = BinaryAssociation(
    name="namespace19",
    ends={
        Property(name="Namespace", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=uml3_0_0_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
nameExpression20: BinaryAssociation = BinaryAssociation(
    name="nameExpression20",
    ends={
        Property(name="uml3_0_0_StringExpression", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_NamedElement", type=uml3_0_0_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supplier21: BinaryAssociation = BinaryAssociation(
    name="supplier21",
    ends={
        Property(name="uml3_0_0_NamedElement22", type=uml3_0_0_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Dependency", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client23: BinaryAssociation = BinaryAssociation(
    name="client23",
    ends={
        Property(name="NamedElement", type=uml3_0_0_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="uml3_0_0_Element25", type=uml3_0_0_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DirectedRelationship", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="uml3_0_0_Element28", type=uml3_0_0_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DirectedRelationship27", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 9999))
    }
)
profileApplication17: BinaryAssociation = BinaryAssociation(
    name="profileApplication17",
    ends={
        Property(name="ProfileApplication", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="applyingPackage", type=uml3_0_0_ProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clientDependency18: BinaryAssociation = BinaryAssociation(
    name="clientDependency18",
    ends={
        Property(name="Dependency", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=uml3_0_0_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember37: BinaryAssociation = BinaryAssociation(
    name="importedMember37",
    ends={
        Property(name="uml3_0_0_PackageableElement39", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Namespace38", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember40: BinaryAssociation = BinaryAssociation(
    name="ownedMember40",
    ends={
        Property(name="NamedElement41", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement42: BinaryAssociation = BinaryAssociation(
    name="importedElement42",
    ends={
        Property(name="uml3_0_0_PackageableElement43", type=uml3_0_0_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ElementImport", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace44: BinaryAssociation = BinaryAssociation(
    name="importingNamespace44",
    ends={
        Property(name="Namespace45", type=uml3_0_0_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage46: BinaryAssociation = BinaryAssociation(
    name="importedPackage46",
    ends={
        Property(name="uml3_0_0_Package47", type=uml3_0_0_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_PackageImport", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace48: BinaryAssociation = BinaryAssociation(
    name="importingNamespace48",
    ends={
        Property(name="Namespace49", type=uml3_0_0_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement50: BinaryAssociation = BinaryAssociation(
    name="constrainedElement50",
    ends={
        Property(name="uml3_0_0_Element51", type=uml3_0_0_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Constraint", type=uml3_0_0_Element, multiplicity=Multiplicity(0, 9999))
    }
)
relatedElement29: BinaryAssociation = BinaryAssociation(
    name="relatedElement29",
    ends={
        Property(name="uml3_0_0_Element30", type=uml3_0_0_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Relationship", type=uml3_0_0_Element, multiplicity=Multiplicity(1, 9999))
    }
)
elementImport31: BinaryAssociation = BinaryAssociation(
    name="elementImport31",
    ends={
        Property(name="ElementImport", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=uml3_0_0_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport32: BinaryAssociation = BinaryAssociation(
    name="packageImport32",
    ends={
        Property(name="PackageImport", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace33", type=uml3_0_0_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule34: BinaryAssociation = BinaryAssociation(
    name="ownedRule34",
    ends={
        Property(name="Constraint", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member35: BinaryAssociation = BinaryAssociation(
    name="member35",
    ends={
        Property(name="uml3_0_0_NamedElement36", type=uml3_0_0_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Namespace", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd59: BinaryAssociation = BinaryAssociation(
    name="ownedEnd59",
    ends={
        Property(name="Property", type=uml3_0_0_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd60: BinaryAssociation = BinaryAssociation(
    name="memberEnd60",
    ends={
        Property(name="Property61", type=uml3_0_0_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=uml3_0_0_Property, multiplicity=Multiplicity(2, 9999))
    }
)
endType62: BinaryAssociation = BinaryAssociation(
    name="endType62",
    ends={
        Property(name="uml3_0_0_Type63", type=uml3_0_0_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Association", type=uml3_0_0_Type, multiplicity=Multiplicity(1, 9999))
    }
)
navigableOwnedEnd64: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd64",
    ends={
        Property(name="uml3_0_0_Property", type=uml3_0_0_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Association65", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999))
    }
)
generalization66: BinaryAssociation = BinaryAssociation(
    name="generalization66",
    ends={
        Property(name="Generalization", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=uml3_0_0_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent67: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent67",
    ends={
        Property(name="GeneralizationSet", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=uml3_0_0_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
feature68: BinaryAssociation = BinaryAssociation(
    name="feature68",
    ends={
        Property(name="Feature", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=uml3_0_0_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
specification52: BinaryAssociation = BinaryAssociation(
    name="specification52",
    ends={
        Property(name="uml3_0_0_ValueSpecification", type=uml3_0_0_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Constraint53", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context54: BinaryAssociation = BinaryAssociation(
    name="context54",
    ends={
        Property(name="Namespace55", type=uml3_0_0_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=uml3_0_0_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="uml3_0_0_Type", type=uml3_0_0_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TypedElement", type=uml3_0_0_Type, multiplicity=Multiplicity(0, 1))
    }
)
package57: BinaryAssociation = BinaryAssociation(
    name="package57",
    ends={
        Property(name="Package58", type=uml3_0_0_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=uml3_0_0_Package, multiplicity=Multiplicity(0, 1))
    }
)
representation81: BinaryAssociation = BinaryAssociation(
    name="representation81",
    ends={
        Property(name="uml3_0_0_CollaborationUse", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier82", type=uml3_0_0_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
collaborationUse83: BinaryAssociation = BinaryAssociation(
    name="collaborationUse83",
    ends={
        Property(name="uml3_0_0_CollaborationUse85", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier84", type=uml3_0_0_CollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUseCase86: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase86",
    ends={
        Property(name="uml3_0_0_UseCase", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier87", type=uml3_0_0_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase88: BinaryAssociation = BinaryAssociation(
    name="useCase88",
    ends={
        Property(name="UseCase", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=uml3_0_0_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement90: BinaryAssociation = BinaryAssociation(
    name="redefinedElement90",
    ends={
        Property(name="uml3_0_0_RedefinableElement", type=uml3_0_0_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RedefinableElement89", type=uml3_0_0_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext91: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext91",
    ends={
        Property(name="uml3_0_0_Classifier93", type=uml3_0_0_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RedefinableElement92", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
templateBinding94: BinaryAssociation = BinaryAssociation(
    name="templateBinding94",
    ends={
        Property(name="TemplateBinding", type=uml3_0_0_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=uml3_0_0_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature95: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature95",
    ends={
        Property(name="TemplateSignature", type=uml3_0_0_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inheritedMember69: BinaryAssociation = BinaryAssociation(
    name="inheritedMember69",
    ends={
        Property(name="uml3_0_0_NamedElement70", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier72: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier72",
    ends={
        Property(name="uml3_0_0_Classifier73", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier71", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general75: BinaryAssociation = BinaryAssociation(
    name="general75",
    ends={
        Property(name="uml3_0_0_Classifier76", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier74", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
substitution77: BinaryAssociation = BinaryAssociation(
    name="substitution77",
    ends={
        Property(name="Substitution", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=uml3_0_0_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute78: BinaryAssociation = BinaryAssociation(
    name="attribute78",
    ends={
        Property(name="uml3_0_0_Property80", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Classifier79", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999))
    }
)
template103: BinaryAssociation = BinaryAssociation(
    name="template103",
    ends={
        Property(name="TemplateableElement104", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=uml3_0_0_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature105: BinaryAssociation = BinaryAssociation(
    name="signature105",
    ends={
        Property(name="TemplateSignature106", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameteredElement107: BinaryAssociation = BinaryAssociation(
    name="parameteredElement107",
    ends={
        Property(name="ParameterableElement", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement108: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement108",
    ends={
        Property(name="ParameterableElement109", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateParameter", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default110: BinaryAssociation = BinaryAssociation(
    name="default110",
    ends={
        Property(name="uml3_0_0_ParameterableElement", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateParameter111", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault112: BinaryAssociation = BinaryAssociation(
    name="ownedDefault112",
    ends={
        Property(name="uml3_0_0_ParameterableElement114", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateParameter113", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningTemplateParameter115: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter115",
    ends={
        Property(name="TemplateParameter116", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameteredElement", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter117: BinaryAssociation = BinaryAssociation(
    name="templateParameter117",
    ends={
        Property(name="TemplateParameter118", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
formal119: BinaryAssociation = BinaryAssociation(
    name="formal119",
    ends={
        Property(name="uml3_0_0_TemplateParameter120", type=uml3_0_0_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateParameterSubstitution", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
signature96: BinaryAssociation = BinaryAssociation(
    name="signature96",
    ends={
        Property(name="uml3_0_0_TemplateSignature", type=uml3_0_0_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateBinding", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution97: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution97",
    ends={
        Property(name="TemplateParameterSubstitution", type=uml3_0_0_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=uml3_0_0_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundElement98: BinaryAssociation = BinaryAssociation(
    name="boundElement98",
    ends={
        Property(name="TemplateableElement", type=uml3_0_0_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding99", type=uml3_0_0_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
parameter100: BinaryAssociation = BinaryAssociation(
    name="parameter100",
    ends={
        Property(name="uml3_0_0_TemplateParameter", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateSignature101", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameter102: BinaryAssociation = BinaryAssociation(
    name="ownedParameter102",
    ends={
        Property(name="TemplateParameter", type=uml3_0_0_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizationSet131: BinaryAssociation = BinaryAssociation(
    name="generalizationSet131",
    ends={
        Property(name="generalization", type=uml3_0_0_GeneralizationSet, multiplicity=Multiplicity(0, 9999)),
        Property(name="GeneralizationSet132", type=uml3_0_0_Generalization, multiplicity=Multiplicity(1, 1))
    }
)
specific133: BinaryAssociation = BinaryAssociation(
    name="specific133",
    ends={
        Property(name="Classifier", type=uml3_0_0_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization134", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
powertype135: BinaryAssociation = BinaryAssociation(
    name="powertype135",
    ends={
        Property(name="Classifier136", type=uml3_0_0_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization137: BinaryAssociation = BinaryAssociation(
    name="generalization137",
    ends={
        Property(name="Generalization138", type=uml3_0_0_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=uml3_0_0_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier139: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier139",
    ends={
        Property(name="Classifier140", type=uml3_0_0_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
contract141: BinaryAssociation = BinaryAssociation(
    name="contract141",
    ends={
        Property(name="uml3_0_0_Classifier142", type=uml3_0_0_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Substitution", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier143: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier143",
    ends={
        Property(name="Classifier144", type=uml3_0_0_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
actual121: BinaryAssociation = BinaryAssociation(
    name="actual121",
    ends={
        Property(name="uml3_0_0_ParameterableElement123", type=uml3_0_0_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateParameterSubstitution122", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual124: BinaryAssociation = BinaryAssociation(
    name="ownedActual124",
    ends={
        Property(name="uml3_0_0_ParameterableElement126", type=uml3_0_0_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TemplateParameterSubstitution125", type=uml3_0_0_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding127: BinaryAssociation = BinaryAssociation(
    name="templateBinding127",
    ends={
        Property(name="TemplateBinding128", type=uml3_0_0_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=uml3_0_0_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
general129: BinaryAssociation = BinaryAssociation(
    name="general129",
    ends={
        Property(name="uml3_0_0_Classifier130", type=uml3_0_0_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Generalization", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
parameterSet150: BinaryAssociation = BinaryAssociation(
    name="parameterSet150",
    ends={
        Property(name="ParameterSet", type=uml3_0_0_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=uml3_0_0_ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
operation151: BinaryAssociation = BinaryAssociation(
    name="operation151",
    ends={
        Property(name="uml3_0_0_Operation", type=uml3_0_0_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Parameter152", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue153: BinaryAssociation = BinaryAssociation(
    name="defaultValue153",
    ends={
        Property(name="uml3_0_0_ValueSpecification155", type=uml3_0_0_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Parameter154", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapping145: BinaryAssociation = BinaryAssociation(
    name="mapping145",
    ends={
        Property(name="uml3_0_0_OpaqueExpression", type=uml3_0_0_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Abstraction", type=uml3_0_0_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result146: BinaryAssociation = BinaryAssociation(
    name="result146",
    ends={
        Property(name="uml3_0_0_Parameter", type=uml3_0_0_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_OpaqueExpression147", type=uml3_0_0_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior148: BinaryAssociation = BinaryAssociation(
    name="behavior148",
    ends={
        Property(name="uml3_0_0_Behavior", type=uml3_0_0_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_OpaqueExpression149", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
end161: BinaryAssociation = BinaryAssociation(
    name="end161",
    ends={
        Property(name="uml3_0_0_ConnectorEnd", type=uml3_0_0_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectableElement", type=uml3_0_0_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
definingEnd162: BinaryAssociation = BinaryAssociation(
    name="definingEnd162",
    ends={
        Property(name="uml3_0_0_Property164", type=uml3_0_0_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectorEnd163", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 1))
    }
)
role165: BinaryAssociation = BinaryAssociation(
    name="role165",
    ends={
        Property(name="uml3_0_0_ConnectableElement167", type=uml3_0_0_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectorEnd166", type=uml3_0_0_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
partWithPort168: BinaryAssociation = BinaryAssociation(
    name="partWithPort168",
    ends={
        Property(name="uml3_0_0_Property170", type=uml3_0_0_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectorEnd169", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 1))
    }
)
class171: BinaryAssociation = BinaryAssociation(
    name="class171",
    ends={
        Property(name="uml3_0_0_Class", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property172", type=uml3_0_0_Class, multiplicity=Multiplicity(0, 1))
    }
)
upperValue156: BinaryAssociation = BinaryAssociation(
    name="upperValue156",
    ends={
        Property(name="uml3_0_0_ValueSpecification157", type=uml3_0_0_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_MultiplicityElement", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datatype173: BinaryAssociation = BinaryAssociation(
    name="datatype173",
    ends={
        Property(name="DataType", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=uml3_0_0_DataType, multiplicity=Multiplicity(0, 1))
    }
)
lowerValue158: BinaryAssociation = BinaryAssociation(
    name="lowerValue158",
    ends={
        Property(name="uml3_0_0_ValueSpecification160", type=uml3_0_0_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_MultiplicityElement159", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedProperty175: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty175",
    ends={
        Property(name="uml3_0_0_Property176", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property174", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999))
    }
)
owningAssociation177: BinaryAssociation = BinaryAssociation(
    name="owningAssociation177",
    ends={
        Property(name="Association", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=uml3_0_0_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue178: BinaryAssociation = BinaryAssociation(
    name="defaultValue178",
    ends={
        Property(name="uml3_0_0_ValueSpecification180", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property179", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite182: BinaryAssociation = BinaryAssociation(
    name="opposite182",
    ends={
        Property(name="uml3_0_0_Property183", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property181", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty185: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty185",
    ends={
        Property(name="uml3_0_0_Property186", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property184", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999))
    }
)
association187: BinaryAssociation = BinaryAssociation(
    name="association187",
    ends={
        Property(name="Association188", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=uml3_0_0_Association, multiplicity=Multiplicity(0, 1))
    }
)
associationEnd193: BinaryAssociation = BinaryAssociation(
    name="associationEnd193",
    ends={
        Property(name="Property194", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 1))
    }
)
deployment195: BinaryAssociation = BinaryAssociation(
    name="deployment195",
    ends={
        Property(name="Deployment", type=uml3_0_0_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=uml3_0_0_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement196: BinaryAssociation = BinaryAssociation(
    name="deployedElement196",
    ends={
        Property(name="uml3_0_0_PackageableElement197", type=uml3_0_0_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DeploymentTarget", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployedArtifact198: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact198",
    ends={
        Property(name="uml3_0_0_DeployedArtifact", type=uml3_0_0_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Deployment", type=uml3_0_0_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
configuration199: BinaryAssociation = BinaryAssociation(
    name="configuration199",
    ends={
        Property(name="DeploymentSpecification", type=uml3_0_0_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="deployment", type=uml3_0_0_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location200: BinaryAssociation = BinaryAssociation(
    name="location200",
    ends={
        Property(name="DeploymentTarget", type=uml3_0_0_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="deployment201", type=uml3_0_0_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
qualifier190: BinaryAssociation = BinaryAssociation(
    name="qualifier190",
    ends={
        Property(name="Property191", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployment202: BinaryAssociation = BinaryAssociation(
    name="deployment202",
    ends={
        Property(name="Deployment203", type=uml3_0_0_DeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=uml3_0_0_Deployment, multiplicity=Multiplicity(0, 1))
    }
)
nestedArtifact205: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact205",
    ends={
        Property(name="uml3_0_0_Artifact", type=uml3_0_0_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Artifact204", type=uml3_0_0_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation206: BinaryAssociation = BinaryAssociation(
    name="manifestation206",
    ends={
        Property(name="uml3_0_0_Manifestation", type=uml3_0_0_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Artifact207", type=uml3_0_0_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation208: BinaryAssociation = BinaryAssociation(
    name="ownedOperation208",
    ends={
        Property(name="uml3_0_0_Operation210", type=uml3_0_0_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Artifact209", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute211: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute211",
    ends={
        Property(name="uml3_0_0_Property213", type=uml3_0_0_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Artifact212", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface217: BinaryAssociation = BinaryAssociation(
    name="interface217",
    ends={
        Property(name="Interface", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 1))
    }
)
class218: BinaryAssociation = BinaryAssociation(
    name="class218",
    ends={
        Property(name="Class", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation219", type=uml3_0_0_Class, multiplicity=Multiplicity(0, 1))
    }
)
precondition220: BinaryAssociation = BinaryAssociation(
    name="precondition220",
    ends={
        Property(name="uml3_0_0_Constraint222", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Operation221", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition223: BinaryAssociation = BinaryAssociation(
    name="postcondition223",
    ends={
        Property(name="uml3_0_0_Constraint225", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Operation224", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
utilizedElement214: BinaryAssociation = BinaryAssociation(
    name="utilizedElement214",
    ends={
        Property(name="uml3_0_0_PackageableElement216", type=uml3_0_0_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Manifestation215", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
datatype229: BinaryAssociation = BinaryAssociation(
    name="datatype229",
    ends={
        Property(name="DataType231", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation230", type=uml3_0_0_DataType, multiplicity=Multiplicity(0, 1))
    }
)
bodyCondition232: BinaryAssociation = BinaryAssociation(
    name="bodyCondition232",
    ends={
        Property(name="uml3_0_0_Constraint234", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Operation233", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
type235: BinaryAssociation = BinaryAssociation(
    name="type235",
    ends={
        Property(name="uml3_0_0_Type237", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Operation236", type=uml3_0_0_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter238: BinaryAssociation = BinaryAssociation(
    name="ownedParameter238",
    ends={
        Property(name="uml3_0_0_Parameter239", type=uml3_0_0_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioralFeature", type=uml3_0_0_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method240: BinaryAssociation = BinaryAssociation(
    name="method240",
    ends={
        Property(name="Behavior", type=uml3_0_0_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException241: BinaryAssociation = BinaryAssociation(
    name="raisedException241",
    ends={
        Property(name="uml3_0_0_Type243", type=uml3_0_0_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioralFeature242", type=uml3_0_0_Type, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation227: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation227",
    ends={
        Property(name="uml3_0_0_Operation228", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Operation226", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet244: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet244",
    ends={
        Property(name="uml3_0_0_ParameterSet", type=uml3_0_0_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioralFeature245", type=uml3_0_0_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedBehavior247: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior247",
    ends={
        Property(name="uml3_0_0_Behavior248", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior246", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter249: BinaryAssociation = BinaryAssociation(
    name="ownedParameter249",
    ends={
        Property(name="uml3_0_0_Parameter251", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior250", type=uml3_0_0_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context252: BinaryAssociation = BinaryAssociation(
    name="context252",
    ends={
        Property(name="uml3_0_0_BehavioredClassifier", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior253", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
precondition254: BinaryAssociation = BinaryAssociation(
    name="precondition254",
    ends={
        Property(name="uml3_0_0_Constraint256", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior255", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition257: BinaryAssociation = BinaryAssociation(
    name="postcondition257",
    ends={
        Property(name="uml3_0_0_Constraint259", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior258", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet260: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet260",
    ends={
        Property(name="uml3_0_0_ParameterSet262", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Behavior261", type=uml3_0_0_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier264: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier264",
    ends={
        Property(name="uml3_0_0_Classifier266", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Class265", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation267: BinaryAssociation = BinaryAssociation(
    name="ownedOperation267",
    ends={
        Property(name="Operation", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass269: BinaryAssociation = BinaryAssociation(
    name="superClass269",
    ends={
        Property(name="uml3_0_0_Class270", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Class268", type=uml3_0_0_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception271: BinaryAssociation = BinaryAssociation(
    name="ownedReception271",
    ends={
        Property(name="uml3_0_0_Reception", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Class272", type=uml3_0_0_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension273: BinaryAssociation = BinaryAssociation(
    name="extension273",
    ends={
        Property(name="Extension", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="metaclass", type=uml3_0_0_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
specification263: BinaryAssociation = BinaryAssociation(
    name="specification263",
    ends={
        Property(name="BehavioralFeature", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=uml3_0_0_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
classifierBehavior277: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior277",
    ends={
        Property(name="uml3_0_0_Behavior279", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioredClassifier278", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
interfaceRealization280: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization280",
    ends={
        Property(name="InterfaceRealization", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=uml3_0_0_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTrigger281: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger281",
    ends={
        Property(name="uml3_0_0_Trigger", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioredClassifier282", type=uml3_0_0_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract283: BinaryAssociation = BinaryAssociation(
    name="contract283",
    ends={
        Property(name="uml3_0_0_Interface", type=uml3_0_0_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InterfaceRealization", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier284: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier284",
    ends={
        Property(name="BehavioredClassifier", type=uml3_0_0_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaceRealization", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute285: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute285",
    ends={
        Property(name="uml3_0_0_Property287", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interface286", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation288: BinaryAssociation = BinaryAssociation(
    name="ownedOperation288",
    ends={
        Property(name="Operation289", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior274: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior274",
    ends={
        Property(name="uml3_0_0_Behavior276", type=uml3_0_0_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehavioredClassifier275", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedInterface294: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface294",
    ends={
        Property(name="uml3_0_0_Interface295", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interface293", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception296: BinaryAssociation = BinaryAssociation(
    name="ownedReception296",
    ends={
        Property(name="uml3_0_0_Reception298", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interface297", type=uml3_0_0_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol299: BinaryAssociation = BinaryAssociation(
    name="protocol299",
    ends={
        Property(name="uml3_0_0_ProtocolStateMachine", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interface300", type=uml3_0_0_ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signal301: BinaryAssociation = BinaryAssociation(
    name="signal301",
    ends={
        Property(name="uml3_0_0_Signal", type=uml3_0_0_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Reception302", type=uml3_0_0_Signal, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute303: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute303",
    ends={
        Property(name="uml3_0_0_Property305", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Signal304", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformance306: BinaryAssociation = BinaryAssociation(
    name="conformance306",
    ends={
        Property(name="ProtocolConformance", type=uml3_0_0_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="specificMachine", type=uml3_0_0_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier290: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier290",
    ends={
        Property(name="uml3_0_0_Classifier292", type=uml3_0_0_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interface291", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region307: BinaryAssociation = BinaryAssociation(
    name="region307",
    ends={
        Property(name="Region", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
submachineState308: BinaryAssociation = BinaryAssociation(
    name="submachineState308",
    ends={
        Property(name="State", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=uml3_0_0_State, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint309: BinaryAssociation = BinaryAssociation(
    name="connectionPoint309",
    ends={
        Property(name="Pseudostate", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine310", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedStateMachine312: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine312",
    ends={
        Property(name="uml3_0_0_StateMachine", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StateMachine311", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex313: BinaryAssociation = BinaryAssociation(
    name="subvertex313",
    ends={
        Property(name="Vertex", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uml3_0_0_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition314: BinaryAssociation = BinaryAssociation(
    name="transition314",
    ends={
        Property(name="Transition", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container315", type=uml3_0_0_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state316: BinaryAssociation = BinaryAssociation(
    name="state316",
    ends={
        Property(name="State317", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=uml3_0_0_State, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine320: BinaryAssociation = BinaryAssociation(
    name="stateMachine320",
    ends={
        Property(name="StateMachine", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region321", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoing322: BinaryAssociation = BinaryAssociation(
    name="outgoing322",
    ends={
        Property(name="uml3_0_0_Transition", type=uml3_0_0_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Vertex", type=uml3_0_0_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming323: BinaryAssociation = BinaryAssociation(
    name="incoming323",
    ends={
        Property(name="uml3_0_0_Transition325", type=uml3_0_0_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Vertex324", type=uml3_0_0_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container326: BinaryAssociation = BinaryAssociation(
    name="container326",
    ends={
        Property(name="Region327", type=uml3_0_0_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=uml3_0_0_Region, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion319: BinaryAssociation = BinaryAssociation(
    name="extendedRegion319",
    ends={
        Property(name="uml3_0_0_Region", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Region318", type=uml3_0_0_Region, multiplicity=Multiplicity(0, 1))
    }
)
container328: BinaryAssociation = BinaryAssociation(
    name="container328",
    ends={
        Property(name="Region329", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=uml3_0_0_Region, multiplicity=Multiplicity(1, 1))
    }
)
source330: BinaryAssociation = BinaryAssociation(
    name="source330",
    ends={
        Property(name="uml3_0_0_Vertex332", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition331", type=uml3_0_0_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target333: BinaryAssociation = BinaryAssociation(
    name="target333",
    ends={
        Property(name="uml3_0_0_Vertex335", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition334", type=uml3_0_0_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
guard339: BinaryAssociation = BinaryAssociation(
    name="guard339",
    ends={
        Property(name="uml3_0_0_Constraint341", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition340", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
effect342: BinaryAssociation = BinaryAssociation(
    name="effect342",
    ends={
        Property(name="uml3_0_0_Behavior344", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition343", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger345: BinaryAssociation = BinaryAssociation(
    name="trigger345",
    ends={
        Property(name="uml3_0_0_Trigger347", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition346", type=uml3_0_0_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event348: BinaryAssociation = BinaryAssociation(
    name="event348",
    ends={
        Property(name="uml3_0_0_Event", type=uml3_0_0_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Trigger349", type=uml3_0_0_Event, multiplicity=Multiplicity(1, 1))
    }
)
port350: BinaryAssociation = BinaryAssociation(
    name="port350",
    ends={
        Property(name="uml3_0_0_Port", type=uml3_0_0_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Trigger351", type=uml3_0_0_Port, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedTransition337: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition337",
    ends={
        Property(name="uml3_0_0_Transition338", type=uml3_0_0_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Transition336", type=uml3_0_0_Transition, multiplicity=Multiplicity(0, 1))
    }
)
required352: BinaryAssociation = BinaryAssociation(
    name="required352",
    ends={
        Property(name="uml3_0_0_Interface354", type=uml3_0_0_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Port353", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort356: BinaryAssociation = BinaryAssociation(
    name="redefinedPort356",
    ends={
        Property(name="uml3_0_0_Port357", type=uml3_0_0_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Port355", type=uml3_0_0_Port, multiplicity=Multiplicity(0, 9999))
    }
)
provided358: BinaryAssociation = BinaryAssociation(
    name="provided358",
    ends={
        Property(name="uml3_0_0_Interface360", type=uml3_0_0_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Port359", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocol361: BinaryAssociation = BinaryAssociation(
    name="protocol361",
    ends={
        Property(name="uml3_0_0_ProtocolStateMachine363", type=uml3_0_0_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Port362", type=uml3_0_0_ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
connection366: BinaryAssociation = BinaryAssociation(
    name="connection366",
    ends={
        Property(name="ConnectionPointReference", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=uml3_0_0_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint367: BinaryAssociation = BinaryAssociation(
    name="connectionPoint367",
    ends={
        Property(name="Pseudostate369", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state368", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState371: BinaryAssociation = BinaryAssociation(
    name="redefinedState371",
    ends={
        Property(name="uml3_0_0_State", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State370", type=uml3_0_0_State, multiplicity=Multiplicity(0, 1))
    }
)
stateInvariant372: BinaryAssociation = BinaryAssociation(
    name="stateInvariant372",
    ends={
        Property(name="uml3_0_0_Constraint374", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State373", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry375: BinaryAssociation = BinaryAssociation(
    name="entry375",
    ends={
        Property(name="uml3_0_0_Behavior377", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State376", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit378: BinaryAssociation = BinaryAssociation(
    name="exit378",
    ends={
        Property(name="uml3_0_0_Behavior380", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State379", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity381: BinaryAssociation = BinaryAssociation(
    name="doActivity381",
    ends={
        Property(name="uml3_0_0_Behavior383", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State382", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachine364: BinaryAssociation = BinaryAssociation(
    name="submachine364",
    ends={
        Property(name="StateMachine365", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region387: BinaryAssociation = BinaryAssociation(
    name="region387",
    ends={
        Property(name="Region389", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state388", type=uml3_0_0_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry390: BinaryAssociation = BinaryAssociation(
    name="entry390",
    ends={
        Property(name="uml3_0_0_Pseudostate", type=uml3_0_0_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectionPointReference", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit391: BinaryAssociation = BinaryAssociation(
    name="exit391",
    ends={
        Property(name="uml3_0_0_Pseudostate393", type=uml3_0_0_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConnectionPointReference392", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
state394: BinaryAssociation = BinaryAssociation(
    name="state394",
    ends={
        Property(name="State395", type=uml3_0_0_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=uml3_0_0_State, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine396: BinaryAssociation = BinaryAssociation(
    name="stateMachine396",
    ends={
        Property(name="StateMachine397", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=uml3_0_0_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state398: BinaryAssociation = BinaryAssociation(
    name="state398",
    ends={
        Property(name="State400", type=uml3_0_0_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint399", type=uml3_0_0_State, multiplicity=Multiplicity(0, 1))
    }
)
generalMachine401: BinaryAssociation = BinaryAssociation(
    name="generalMachine401",
    ends={
        Property(name="uml3_0_0_ProtocolStateMachine402", type=uml3_0_0_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ProtocolConformance", type=uml3_0_0_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
specificMachine403: BinaryAssociation = BinaryAssociation(
    name="specificMachine403",
    ends={
        Property(name="ProtocolStateMachine", type=uml3_0_0_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="conformance", type=uml3_0_0_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
deferrableTrigger384: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger384",
    ends={
        Property(name="uml3_0_0_Trigger386", type=uml3_0_0_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_State385", type=uml3_0_0_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPort404: BinaryAssociation = BinaryAssociation(
    name="ownedPort404",
    ends={
        Property(name="uml3_0_0_Port405", type=uml3_0_0_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_EncapsulatedClassifier", type=uml3_0_0_Port, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute406: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute406",
    ends={
        Property(name="uml3_0_0_Property407", type=uml3_0_0_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuredClassifier", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part408: BinaryAssociation = BinaryAssociation(
    name="part408",
    ends={
        Property(name="uml3_0_0_Property410", type=uml3_0_0_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuredClassifier409", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999))
    }
)
role411: BinaryAssociation = BinaryAssociation(
    name="role411",
    ends={
        Property(name="uml3_0_0_ConnectableElement413", type=uml3_0_0_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuredClassifier412", type=uml3_0_0_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector414: BinaryAssociation = BinaryAssociation(
    name="ownedConnector414",
    ends={
        Property(name="uml3_0_0_Connector", type=uml3_0_0_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuredClassifier415", type=uml3_0_0_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type416: BinaryAssociation = BinaryAssociation(
    name="type416",
    ends={
        Property(name="uml3_0_0_Association418", type=uml3_0_0_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Connector417", type=uml3_0_0_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConnector420: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector420",
    ends={
        Property(name="uml3_0_0_Connector421", type=uml3_0_0_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Connector419", type=uml3_0_0_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
end422: BinaryAssociation = BinaryAssociation(
    name="end422",
    ends={
        Property(name="uml3_0_0_ConnectorEnd424", type=uml3_0_0_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Connector423", type=uml3_0_0_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract425: BinaryAssociation = BinaryAssociation(
    name="contract425",
    ends={
        Property(name="uml3_0_0_Behavior427", type=uml3_0_0_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Connector426", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
metaclass428: BinaryAssociation = BinaryAssociation(
    name="metaclass428",
    ends={
        Property(name="Class429", type=uml3_0_0_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=uml3_0_0_Class, multiplicity=Multiplicity(1, 1))
    }
)
icon430: BinaryAssociation = BinaryAssociation(
    name="icon430",
    ends={
        Property(name="uml3_0_0_Image", type=uml3_0_0_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Stereotype", type=uml3_0_0_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStereotype431: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype431",
    ends={
        Property(name="uml3_0_0_Stereotype432", type=uml3_0_0_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Profile", type=uml3_0_0_Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
metaclassReference433: BinaryAssociation = BinaryAssociation(
    name="metaclassReference433",
    ends={
        Property(name="uml3_0_0_ElementImport435", type=uml3_0_0_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Profile434", type=uml3_0_0_ElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference436: BinaryAssociation = BinaryAssociation(
    name="metamodelReference436",
    ends={
        Property(name="uml3_0_0_PackageImport438", type=uml3_0_0_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Profile437", type=uml3_0_0_PackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
parameter439: BinaryAssociation = BinaryAssociation(
    name="parameter439",
    ends={
        Property(name="Parameter", type=uml3_0_0_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSet", type=uml3_0_0_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
condition440: BinaryAssociation = BinaryAssociation(
    name="condition440",
    ends={
        Property(name="uml3_0_0_Constraint442", type=uml3_0_0_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ParameterSet441", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute443: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute443",
    ends={
        Property(name="Property444", type=uml3_0_0_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=uml3_0_0_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation445: BinaryAssociation = BinaryAssociation(
    name="ownedOperation445",
    ends={
        Property(name="Operation447", type=uml3_0_0_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype446", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type448: BinaryAssociation = BinaryAssociation(
    name="type448",
    ends={
        Property(name="uml3_0_0_Collaboration", type=uml3_0_0_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CollaborationUse449", type=uml3_0_0_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding450: BinaryAssociation = BinaryAssociation(
    name="roleBinding450",
    ends={
        Property(name="uml3_0_0_Dependency452", type=uml3_0_0_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CollaborationUse451", type=uml3_0_0_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationRole453: BinaryAssociation = BinaryAssociation(
    name="collaborationRole453",
    ends={
        Property(name="uml3_0_0_ConnectableElement455", type=uml3_0_0_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Collaboration454", type=uml3_0_0_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
include456: BinaryAssociation = BinaryAssociation(
    name="include456",
    ends={
        Property(name="Include", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="includingCase", type=uml3_0_0_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend457: BinaryAssociation = BinaryAssociation(
    name="extend457",
    ends={
        Property(name="Extend", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension458", type=uml3_0_0_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint459: BinaryAssociation = BinaryAssociation(
    name="extensionPoint459",
    ends={
        Property(name="ExtensionPoint", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=uml3_0_0_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject460: BinaryAssociation = BinaryAssociation(
    name="subject460",
    ends={
        Property(name="Classifier462", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase461", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
includingCase465: BinaryAssociation = BinaryAssociation(
    name="includingCase465",
    ends={
        Property(name="UseCase466", type=uml3_0_0_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extendedCase467: BinaryAssociation = BinaryAssociation(
    name="extendedCase467",
    ends={
        Property(name="uml3_0_0_UseCase468", type=uml3_0_0_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Extend", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition469: BinaryAssociation = BinaryAssociation(
    name="condition469",
    ends={
        Property(name="uml3_0_0_Constraint471", type=uml3_0_0_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Extend470", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionLocation472: BinaryAssociation = BinaryAssociation(
    name="extensionLocation472",
    ends={
        Property(name="uml3_0_0_ExtensionPoint", type=uml3_0_0_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Extend473", type=uml3_0_0_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension474: BinaryAssociation = BinaryAssociation(
    name="extension474",
    ends={
        Property(name="UseCase475", type=uml3_0_0_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase476: BinaryAssociation = BinaryAssociation(
    name="useCase476",
    ends={
        Property(name="UseCase477", type=uml3_0_0_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extendedSignature479: BinaryAssociation = BinaryAssociation(
    name="extendedSignature479",
    ends={
        Property(name="uml3_0_0_RedefinableTemplateSignature", type=uml3_0_0_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RedefinableTemplateSignature478", type=uml3_0_0_RedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedParameter480: BinaryAssociation = BinaryAssociation(
    name="inheritedParameter480",
    ends={
        Property(name="uml3_0_0_TemplateParameter482", type=uml3_0_0_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RedefinableTemplateSignature481", type=uml3_0_0_TemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
classifier483: BinaryAssociation = BinaryAssociation(
    name="classifier483",
    ends={
        Property(name="uml3_0_0_Classifier485", type=uml3_0_0_RedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RedefinableTemplateSignature484", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
constrainingClassifier486: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier486",
    ends={
        Property(name="uml3_0_0_Classifier487", type=uml3_0_0_ClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ClassifierTemplateParameter", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
addition463: BinaryAssociation = BinaryAssociation(
    name="addition463",
    ends={
        Property(name="uml3_0_0_UseCase464", type=uml3_0_0_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Include", type=uml3_0_0_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
owningExpression491: BinaryAssociation = BinaryAssociation(
    name="owningExpression491",
    ends={
        Property(name="StringExpression492", type=uml3_0_0_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=uml3_0_0_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand493: BinaryAssociation = BinaryAssociation(
    name="operand493",
    ends={
        Property(name="uml3_0_0_ValueSpecification494", type=uml3_0_0_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Expression", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mergedPackage495: BinaryAssociation = BinaryAssociation(
    name="mergedPackage495",
    ends={
        Property(name="uml3_0_0_Package496", type=uml3_0_0_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_PackageMerge", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage497: BinaryAssociation = BinaryAssociation(
    name="receivingPackage497",
    ends={
        Property(name="Package498", type=uml3_0_0_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1))
    }
)
appliedProfile499: BinaryAssociation = BinaryAssociation(
    name="appliedProfile499",
    ends={
        Property(name="uml3_0_0_Profile500", type=uml3_0_0_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ProfileApplication", type=uml3_0_0_Profile, multiplicity=Multiplicity(1, 1))
    }
)
applyingPackage501: BinaryAssociation = BinaryAssociation(
    name="applyingPackage501",
    ends={
        Property(name="Package502", type=uml3_0_0_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="profileApplication", type=uml3_0_0_Package, multiplicity=Multiplicity(1, 1))
    }
)
ownedLiteral503: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral503",
    ends={
        Property(name="EnumerationLiteral", type=uml3_0_0_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=uml3_0_0_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration504: BinaryAssociation = BinaryAssociation(
    name="enumeration504",
    ends={
        Property(name="Enumeration", type=uml3_0_0_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=uml3_0_0_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
subExpression489: BinaryAssociation = BinaryAssociation(
    name="subExpression489",
    ends={
        Property(name="StringExpression", type=uml3_0_0_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=uml3_0_0_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slot507: BinaryAssociation = BinaryAssociation(
    name="slot507",
    ends={
        Property(name="Slot", type=uml3_0_0_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=uml3_0_0_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification508: BinaryAssociation = BinaryAssociation(
    name="specification508",
    ends={
        Property(name="uml3_0_0_ValueSpecification510", type=uml3_0_0_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InstanceSpecification509", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingFeature511: BinaryAssociation = BinaryAssociation(
    name="definingFeature511",
    ends={
        Property(name="uml3_0_0_StructuralFeature", type=uml3_0_0_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Slot", type=uml3_0_0_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value512: BinaryAssociation = BinaryAssociation(
    name="value512",
    ends={
        Property(name="uml3_0_0_ValueSpecification514", type=uml3_0_0_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Slot513", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance515: BinaryAssociation = BinaryAssociation(
    name="owningInstance515",
    ends={
        Property(name="InstanceSpecification", type=uml3_0_0_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=uml3_0_0_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance516: BinaryAssociation = BinaryAssociation(
    name="instance516",
    ends={
        Property(name="uml3_0_0_InstanceSpecification517", type=uml3_0_0_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InstanceValue", type=uml3_0_0_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
classifier505: BinaryAssociation = BinaryAssociation(
    name="classifier505",
    ends={
        Property(name="uml3_0_0_Classifier506", type=uml3_0_0_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InstanceSpecification", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
inputValue518: BinaryAssociation = BinaryAssociation(
    name="inputValue518",
    ends={
        Property(name="uml3_0_0_InputPin", type=uml3_0_0_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_OpaqueAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputValue519: BinaryAssociation = BinaryAssociation(
    name="outputValue519",
    ends={
        Property(name="uml3_0_0_OutputPin", type=uml3_0_0_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_OpaqueAction520", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output521: BinaryAssociation = BinaryAssociation(
    name="output521",
    ends={
        Property(name="uml3_0_0_OutputPin522", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Action", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
input523: BinaryAssociation = BinaryAssociation(
    name="input523",
    ends={
        Property(name="uml3_0_0_InputPin525", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Action524", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context526: BinaryAssociation = BinaryAssociation(
    name="context526",
    ends={
        Property(name="uml3_0_0_Classifier528", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Action527", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
localPrecondition529: BinaryAssociation = BinaryAssociation(
    name="localPrecondition529",
    ends={
        Property(name="uml3_0_0_Constraint531", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Action530", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition532: BinaryAssociation = BinaryAssociation(
    name="localPostcondition532",
    ends={
        Property(name="uml3_0_0_Constraint534", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Action533", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler535: BinaryAssociation = BinaryAssociation(
    name="handler535",
    ends={
        Property(name="ExceptionHandler", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedNode", type=uml3_0_0_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity537: BinaryAssociation = BinaryAssociation(
    name="activity537",
    ends={
        Property(name="Activity", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node538", type=uml3_0_0_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing539: BinaryAssociation = BinaryAssociation(
    name="outgoing539",
    ends={
        Property(name="ActivityEdge", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming540: BinaryAssociation = BinaryAssociation(
    name="incoming540",
    ends={
        Property(name="ActivityEdge541", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition542: BinaryAssociation = BinaryAssociation(
    name="inPartition542",
    ends={
        Property(name="ActivityPartition", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node543", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion544: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion544",
    ends={
        Property(name="InterruptibleActivityRegion", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node545", type=uml3_0_0_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup546: BinaryAssociation = BinaryAssociation(
    name="inGroup546",
    ends={
        Property(name="ActivityGroup", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode548: BinaryAssociation = BinaryAssociation(
    name="redefinedNode548",
    ends={
        Property(name="uml3_0_0_ActivityNode", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityNode547", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable549: BinaryAssociation = BinaryAssociation(
    name="variable549",
    ends={
        Property(name="Variable", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=uml3_0_0_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge550: BinaryAssociation = BinaryAssociation(
    name="edge550",
    ends={
        Property(name="ActivityEdge551", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node552: BinaryAssociation = BinaryAssociation(
    name="node552",
    ends={
        Property(name="ActivityNode", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode553", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgroup555: BinaryAssociation = BinaryAssociation(
    name="subgroup555",
    ends={
        Property(name="ActivityGroup556", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="superGroup", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode536: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode536",
    ends={
        Property(name="StructuredActivityNode", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inActivity560: BinaryAssociation = BinaryAssociation(
    name="inActivity560",
    ends={
        Property(name="Activity561", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=uml3_0_0_Activity, multiplicity=Multiplicity(0, 1))
    }
)
containedEdge562: BinaryAssociation = BinaryAssociation(
    name="containedEdge562",
    ends={
        Property(name="ActivityEdge563", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode564: BinaryAssociation = BinaryAssociation(
    name="containedNode564",
    ends={
        Property(name="ActivityNode566", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="inGroup565", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode567: BinaryAssociation = BinaryAssociation(
    name="structuredNode567",
    ends={
        Property(name="uml3_0_0_StructuredActivityNode", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Activity", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable568: BinaryAssociation = BinaryAssociation(
    name="variable568",
    ends={
        Property(name="Variable569", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityScope", type=uml3_0_0_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node570: BinaryAssociation = BinaryAssociation(
    name="node570",
    ends={
        Property(name="ActivityNode571", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge572: BinaryAssociation = BinaryAssociation(
    name="edge572",
    ends={
        Property(name="ActivityEdge574", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity573", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition575: BinaryAssociation = BinaryAssociation(
    name="partition575",
    ends={
        Property(name="uml3_0_0_ActivityPartition", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Activity576", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
group577: BinaryAssociation = BinaryAssociation(
    name="group577",
    ends={
        Property(name="ActivityGroup578", type=uml3_0_0_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="inActivity", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scope579: BinaryAssociation = BinaryAssociation(
    name="scope579",
    ends={
        Property(name="StructuredActivityNode580", type=uml3_0_0_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activityScope581: BinaryAssociation = BinaryAssociation(
    name="activityScope581",
    ends={
        Property(name="Activity583", type=uml3_0_0_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable582", type=uml3_0_0_Activity, multiplicity=Multiplicity(0, 1))
    }
)
superGroup558: BinaryAssociation = BinaryAssociation(
    name="superGroup558",
    ends={
        Property(name="ActivityGroup559", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="subgroup", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
target586: BinaryAssociation = BinaryAssociation(
    name="target586",
    ends={
        Property(name="ActivityNode587", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge589: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge589",
    ends={
        Property(name="uml3_0_0_ActivityEdge", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityEdge588", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition590: BinaryAssociation = BinaryAssociation(
    name="inPartition590",
    ends={
        Property(name="ActivityPartition591", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
guard592: BinaryAssociation = BinaryAssociation(
    name="guard592",
    ends={
        Property(name="uml3_0_0_ValueSpecification594", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityEdge593", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
weight595: BinaryAssociation = BinaryAssociation(
    name="weight595",
    ends={
        Property(name="uml3_0_0_ValueSpecification597", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityEdge596", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts598: BinaryAssociation = BinaryAssociation(
    name="interrupts598",
    ends={
        Property(name="InterruptibleActivityRegion599", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="interruptingEdge", type=uml3_0_0_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode600: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode600",
    ends={
        Property(name="StructuredActivityNode602", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge601", type=uml3_0_0_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inGroup603: BinaryAssociation = BinaryAssociation(
    name="inGroup603",
    ends={
        Property(name="ActivityGroup604", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge", type=uml3_0_0_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
activity605: BinaryAssociation = BinaryAssociation(
    name="activity605",
    ends={
        Property(name="Activity607", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge606", type=uml3_0_0_Activity, multiplicity=Multiplicity(0, 1))
    }
)
node608: BinaryAssociation = BinaryAssociation(
    name="node608",
    ends={
        Property(name="ActivityNode609", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition611: BinaryAssociation = BinaryAssociation(
    name="subpartition611",
    ends={
        Property(name="ActivityPartition612", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="superPartition", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source584: BinaryAssociation = BinaryAssociation(
    name="source584",
    ends={
        Property(name="ActivityNode585", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
represents616: BinaryAssociation = BinaryAssociation(
    name="represents616",
    ends={
        Property(name="uml3_0_0_Element618", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityPartition617", type=uml3_0_0_Element, multiplicity=Multiplicity(0, 1))
    }
)
edge619: BinaryAssociation = BinaryAssociation(
    name="edge619",
    ends={
        Property(name="ActivityEdge621", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition620", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node622: BinaryAssociation = BinaryAssociation(
    name="node622",
    ends={
        Property(name="ActivityNode623", type=uml3_0_0_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="inInterruptibleRegion", type=uml3_0_0_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
interruptingEdge624: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge624",
    ends={
        Property(name="ActivityEdge625", type=uml3_0_0_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="interrupts", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
handlerBody626: BinaryAssociation = BinaryAssociation(
    name="handlerBody626",
    ends={
        Property(name="uml3_0_0_ExecutableNode", type=uml3_0_0_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExceptionHandler", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput627: BinaryAssociation = BinaryAssociation(
    name="exceptionInput627",
    ends={
        Property(name="uml3_0_0_ObjectNode", type=uml3_0_0_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExceptionHandler628", type=uml3_0_0_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType629: BinaryAssociation = BinaryAssociation(
    name="exceptionType629",
    ends={
        Property(name="uml3_0_0_Classifier631", type=uml3_0_0_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExceptionHandler630", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
protectedNode632: BinaryAssociation = BinaryAssociation(
    name="protectedNode632",
    ends={
        Property(name="ExecutableNode", type=uml3_0_0_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handler", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
upperBound633: BinaryAssociation = BinaryAssociation(
    name="upperBound633",
    ends={
        Property(name="uml3_0_0_ValueSpecification635", type=uml3_0_0_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ObjectNode634", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inState636: BinaryAssociation = BinaryAssociation(
    name="inState636",
    ends={
        Property(name="uml3_0_0_State638", type=uml3_0_0_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ObjectNode637", type=uml3_0_0_State, multiplicity=Multiplicity(0, 9999))
    }
)
superPartition614: BinaryAssociation = BinaryAssociation(
    name="superPartition614",
    ends={
        Property(name="ActivityPartition615", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="subpartition", type=uml3_0_0_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
result642: BinaryAssociation = BinaryAssociation(
    name="result642",
    ends={
        Property(name="uml3_0_0_OutputPin643", type=uml3_0_0_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CallAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument644: BinaryAssociation = BinaryAssociation(
    name="argument644",
    ends={
        Property(name="uml3_0_0_InputPin645", type=uml3_0_0_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InvocationAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onPort646: BinaryAssociation = BinaryAssociation(
    name="onPort646",
    ends={
        Property(name="uml3_0_0_Port648", type=uml3_0_0_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InvocationAction647", type=uml3_0_0_Port, multiplicity=Multiplicity(0, 1))
    }
)
target649: BinaryAssociation = BinaryAssociation(
    name="target649",
    ends={
        Property(name="uml3_0_0_InputPin650", type=uml3_0_0_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendSignalAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal651: BinaryAssociation = BinaryAssociation(
    name="signal651",
    ends={
        Property(name="uml3_0_0_Signal653", type=uml3_0_0_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendSignalAction652", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation654: BinaryAssociation = BinaryAssociation(
    name="operation654",
    ends={
        Property(name="uml3_0_0_Operation655", type=uml3_0_0_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CallOperationAction", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target656: BinaryAssociation = BinaryAssociation(
    name="target656",
    ends={
        Property(name="uml3_0_0_InputPin658", type=uml3_0_0_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CallOperationAction657", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selection639: BinaryAssociation = BinaryAssociation(
    name="selection639",
    ends={
        Property(name="uml3_0_0_Behavior641", type=uml3_0_0_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ObjectNode640", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
executableNode661: BinaryAssociation = BinaryAssociation(
    name="executableNode661",
    ends={
        Property(name="uml3_0_0_ExecutableNode662", type=uml3_0_0_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SequenceNode", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter663: BinaryAssociation = BinaryAssociation(
    name="parameter663",
    ends={
        Property(name="uml3_0_0_Parameter664", type=uml3_0_0_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActivityParameterNode", type=uml3_0_0_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value665: BinaryAssociation = BinaryAssociation(
    name="value665",
    ends={
        Property(name="uml3_0_0_ValueSpecification666", type=uml3_0_0_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ValuePin", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiveEvent667: BinaryAssociation = BinaryAssociation(
    name="receiveEvent667",
    ends={
        Property(name="uml3_0_0_MessageEnd", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Message", type=uml3_0_0_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent668: BinaryAssociation = BinaryAssociation(
    name="sendEvent668",
    ends={
        Property(name="uml3_0_0_MessageEnd670", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Message669", type=uml3_0_0_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
connector671: BinaryAssociation = BinaryAssociation(
    name="connector671",
    ends={
        Property(name="uml3_0_0_Connector673", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Message672", type=uml3_0_0_Connector, multiplicity=Multiplicity(0, 1))
    }
)
interaction674: BinaryAssociation = BinaryAssociation(
    name="interaction674",
    ends={
        Property(name="Interaction", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
argument675: BinaryAssociation = BinaryAssociation(
    name="argument675",
    ends={
        Property(name="uml3_0_0_ValueSpecification677", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Message676", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature678: BinaryAssociation = BinaryAssociation(
    name="signature678",
    ends={
        Property(name="uml3_0_0_NamedElement680", type=uml3_0_0_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Message679", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
behavior659: BinaryAssociation = BinaryAssociation(
    name="behavior659",
    ends={
        Property(name="uml3_0_0_Behavior660", type=uml3_0_0_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CallBehaviorAction", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
message681: BinaryAssociation = BinaryAssociation(
    name="message681",
    ends={
        Property(name="uml3_0_0_Message683", type=uml3_0_0_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_MessageEnd682", type=uml3_0_0_Message, multiplicity=Multiplicity(0, 1))
    }
)
lifeline684: BinaryAssociation = BinaryAssociation(
    name="lifeline684",
    ends={
        Property(name="Lifeline", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragment685: BinaryAssociation = BinaryAssociation(
    name="fragment685",
    ends={
        Property(name="InteractionFragment", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingInteraction", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action686: BinaryAssociation = BinaryAssociation(
    name="action686",
    ends={
        Property(name="uml3_0_0_Action687", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interaction", type=uml3_0_0_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate688: BinaryAssociation = BinaryAssociation(
    name="formalGate688",
    ends={
        Property(name="uml3_0_0_Gate", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interaction689", type=uml3_0_0_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message690: BinaryAssociation = BinaryAssociation(
    name="message690",
    ends={
        Property(name="Message", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction691", type=uml3_0_0_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered692: BinaryAssociation = BinaryAssociation(
    name="covered692",
    ends={
        Property(name="Lifeline693", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering694: BinaryAssociation = BinaryAssociation(
    name="generalOrdering694",
    ends={
        Property(name="uml3_0_0_GeneralOrdering", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionFragment", type=uml3_0_0_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingInteraction695: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction695",
    ends={
        Property(name="Interaction696", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment", type=uml3_0_0_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
represents699: BinaryAssociation = BinaryAssociation(
    name="represents699",
    ends={
        Property(name="uml3_0_0_ConnectableElement700", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Lifeline", type=uml3_0_0_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
interaction701: BinaryAssociation = BinaryAssociation(
    name="interaction701",
    ends={
        Property(name="Interaction702", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="lifeline", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
selector703: BinaryAssociation = BinaryAssociation(
    name="selector703",
    ends={
        Property(name="uml3_0_0_ValueSpecification705", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Lifeline704", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs706: BinaryAssociation = BinaryAssociation(
    name="decomposedAs706",
    ends={
        Property(name="uml3_0_0_PartDecomposition", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Lifeline707", type=uml3_0_0_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy708: BinaryAssociation = BinaryAssociation(
    name="coveredBy708",
    ends={
        Property(name="InteractionFragment709", type=uml3_0_0_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
enclosingOperand697: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand697",
    ends={
        Property(name="InteractionOperand", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment698", type=uml3_0_0_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
actualGate712: BinaryAssociation = BinaryAssociation(
    name="actualGate712",
    ends={
        Property(name="uml3_0_0_Gate714", type=uml3_0_0_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionUse713", type=uml3_0_0_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument715: BinaryAssociation = BinaryAssociation(
    name="argument715",
    ends={
        Property(name="uml3_0_0_Action717", type=uml3_0_0_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionUse716", type=uml3_0_0_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
before718: BinaryAssociation = BinaryAssociation(
    name="before718",
    ends={
        Property(name="OccurrenceSpecification", type=uml3_0_0_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toAfter", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
after719: BinaryAssociation = BinaryAssociation(
    name="after719",
    ends={
        Property(name="OccurrenceSpecification720", type=uml3_0_0_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toBefore", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
toBefore721: BinaryAssociation = BinaryAssociation(
    name="toBefore721",
    ends={
        Property(name="GeneralOrdering", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="after", type=uml3_0_0_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
event722: BinaryAssociation = BinaryAssociation(
    name="event722",
    ends={
        Property(name="uml3_0_0_Event723", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_OccurrenceSpecification", type=uml3_0_0_Event, multiplicity=Multiplicity(1, 1))
    }
)
refersTo710: BinaryAssociation = BinaryAssociation(
    name="refersTo710",
    ends={
        Property(name="uml3_0_0_Interaction711", type=uml3_0_0_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionUse", type=uml3_0_0_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
guard726: BinaryAssociation = BinaryAssociation(
    name="guard726",
    ends={
        Property(name="uml3_0_0_InteractionConstraint", type=uml3_0_0_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionOperand", type=uml3_0_0_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragment727: BinaryAssociation = BinaryAssociation(
    name="fragment727",
    ends={
        Property(name="InteractionFragment728", type=uml3_0_0_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingOperand", type=uml3_0_0_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minint729: BinaryAssociation = BinaryAssociation(
    name="minint729",
    ends={
        Property(name="uml3_0_0_ValueSpecification731", type=uml3_0_0_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionConstraint730", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxint732: BinaryAssociation = BinaryAssociation(
    name="maxint732",
    ends={
        Property(name="uml3_0_0_ValueSpecification734", type=uml3_0_0_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InteractionConstraint733", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start735: BinaryAssociation = BinaryAssociation(
    name="start735",
    ends={
        Property(name="uml3_0_0_OccurrenceSpecification736", type=uml3_0_0_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExecutionSpecification", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
toAfter724: BinaryAssociation = BinaryAssociation(
    name="toAfter724",
    ends={
        Property(name="GeneralOrdering725", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="before", type=uml3_0_0_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
invariant740: BinaryAssociation = BinaryAssociation(
    name="invariant740",
    ends={
        Property(name="uml3_0_0_Constraint741", type=uml3_0_0_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StateInvariant", type=uml3_0_0_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action742: BinaryAssociation = BinaryAssociation(
    name="action742",
    ends={
        Property(name="uml3_0_0_Action743", type=uml3_0_0_ActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActionExecutionSpecification", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1))
    }
)
behavior744: BinaryAssociation = BinaryAssociation(
    name="behavior744",
    ends={
        Property(name="uml3_0_0_Behavior745", type=uml3_0_0_BehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BehaviorExecutionSpecification", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
operation746: BinaryAssociation = BinaryAssociation(
    name="operation746",
    ends={
        Property(name="uml3_0_0_Operation747", type=uml3_0_0_SendOperationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendOperationEvent", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1))
    }
)
finish737: BinaryAssociation = BinaryAssociation(
    name="finish737",
    ends={
        Property(name="uml3_0_0_OccurrenceSpecification739", type=uml3_0_0_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExecutionSpecification738", type=uml3_0_0_OccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
execution750: BinaryAssociation = BinaryAssociation(
    name="execution750",
    ends={
        Property(name="uml3_0_0_ExecutionSpecification751", type=uml3_0_0_ExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ExecutionOccurrenceSpecification", type=uml3_0_0_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
operation752: BinaryAssociation = BinaryAssociation(
    name="operation752",
    ends={
        Property(name="uml3_0_0_Operation753", type=uml3_0_0_ReceiveOperationEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReceiveOperationEvent", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal754: BinaryAssociation = BinaryAssociation(
    name="signal754",
    ends={
        Property(name="uml3_0_0_Signal755", type=uml3_0_0_ReceiveSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReceiveSignalEvent", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation756: BinaryAssociation = BinaryAssociation(
    name="operation756",
    ends={
        Property(name="uml3_0_0_Operation757", type=uml3_0_0_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CallEvent", type=uml3_0_0_Operation, multiplicity=Multiplicity(1, 1))
    }
)
signal748: BinaryAssociation = BinaryAssociation(
    name="signal748",
    ends={
        Property(name="uml3_0_0_Signal749", type=uml3_0_0_SendSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendSignalEvent", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression758: BinaryAssociation = BinaryAssociation(
    name="changeExpression758",
    ends={
        Property(name="uml3_0_0_ChangeEvent", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="uml3_0_0_ValueSpecification759", type=uml3_0_0_ChangeEvent, multiplicity=Multiplicity(1, 1))
    }
)
signal760: BinaryAssociation = BinaryAssociation(
    name="signal760",
    ends={
        Property(name="uml3_0_0_Signal761", type=uml3_0_0_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SignalEvent", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1))
    }
)
decisionInput762: BinaryAssociation = BinaryAssociation(
    name="decisionInput762",
    ends={
        Property(name="uml3_0_0_Behavior763", type=uml3_0_0_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DecisionNode", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow764: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow764",
    ends={
        Property(name="uml3_0_0_ObjectFlow", type=uml3_0_0_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DecisionNode765", type=uml3_0_0_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
transformation766: BinaryAssociation = BinaryAssociation(
    name="transformation766",
    ends={
        Property(name="uml3_0_0_Behavior768", type=uml3_0_0_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ObjectFlow767", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection769: BinaryAssociation = BinaryAssociation(
    name="selection769",
    ends={
        Property(name="uml3_0_0_Behavior771", type=uml3_0_0_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ObjectFlow770", type=uml3_0_0_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
abstraction772: BinaryAssociation = BinaryAssociation(
    name="abstraction772",
    ends={
        Property(name="Component", type=uml3_0_0_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="realization", type=uml3_0_0_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier773: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier773",
    ends={
        Property(name="uml3_0_0_Classifier774", type=uml3_0_0_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ComponentRealization", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
required775: BinaryAssociation = BinaryAssociation(
    name="required775",
    ends={
        Property(name="uml3_0_0_Interface776", type=uml3_0_0_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Component", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided777: BinaryAssociation = BinaryAssociation(
    name="provided777",
    ends={
        Property(name="uml3_0_0_Interface779", type=uml3_0_0_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Component778", type=uml3_0_0_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement780: BinaryAssociation = BinaryAssociation(
    name="packagedElement780",
    ends={
        Property(name="uml3_0_0_PackageableElement782", type=uml3_0_0_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Component781", type=uml3_0_0_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realization783: BinaryAssociation = BinaryAssociation(
    name="realization783",
    ends={
        Property(name="ComponentRealization", type=uml3_0_0_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="abstraction", type=uml3_0_0_ComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedNode785: BinaryAssociation = BinaryAssociation(
    name="nestedNode785",
    ends={
        Property(name="uml3_0_0_Node", type=uml3_0_0_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Node784", type=uml3_0_0_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cfragmentGate788: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate788",
    ends={
        Property(name="uml3_0_0_Gate790", type=uml3_0_0_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CombinedFragment789", type=uml3_0_0_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message791: BinaryAssociation = BinaryAssociation(
    name="message791",
    ends={
        Property(name="uml3_0_0_NamedElement792", type=uml3_0_0_ConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConsiderIgnoreFragment", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
classifier793: BinaryAssociation = BinaryAssociation(
    name="classifier793",
    ends={
        Property(name="uml3_0_0_Classifier794", type=uml3_0_0_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CreateObjectAction", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operand786: BinaryAssociation = BinaryAssociation(
    name="operand786",
    ends={
        Property(name="uml3_0_0_InteractionOperand787", type=uml3_0_0_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CombinedFragment", type=uml3_0_0_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result795: BinaryAssociation = BinaryAssociation(
    name="result795",
    ends={
        Property(name="uml3_0_0_OutputPin797", type=uml3_0_0_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CreateObjectAction796", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target798: BinaryAssociation = BinaryAssociation(
    name="target798",
    ends={
        Property(name="uml3_0_0_InputPin799", type=uml3_0_0_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DestroyObjectAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first800: BinaryAssociation = BinaryAssociation(
    name="first800",
    ends={
        Property(name="uml3_0_0_InputPin801", type=uml3_0_0_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TestIdentityAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second802: BinaryAssociation = BinaryAssociation(
    name="second802",
    ends={
        Property(name="uml3_0_0_InputPin804", type=uml3_0_0_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TestIdentityAction803", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result805: BinaryAssociation = BinaryAssociation(
    name="result805",
    ends={
        Property(name="uml3_0_0_OutputPin807", type=uml3_0_0_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TestIdentityAction806", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result808: BinaryAssociation = BinaryAssociation(
    name="result808",
    ends={
        Property(name="uml3_0_0_OutputPin809", type=uml3_0_0_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadSelfAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature810: BinaryAssociation = BinaryAssociation(
    name="structuralFeature810",
    ends={
        Property(name="uml3_0_0_StructuralFeature811", type=uml3_0_0_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuralFeatureAction", type=uml3_0_0_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object812: BinaryAssociation = BinaryAssociation(
    name="object812",
    ends={
        Property(name="uml3_0_0_InputPin814", type=uml3_0_0_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StructuralFeatureAction813", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result815: BinaryAssociation = BinaryAssociation(
    name="result815",
    ends={
        Property(name="uml3_0_0_OutputPin816", type=uml3_0_0_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadStructuralFeatureAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value817: BinaryAssociation = BinaryAssociation(
    name="value817",
    ends={
        Property(name="uml3_0_0_InputPin818", type=uml3_0_0_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_WriteStructuralFeatureAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result819: BinaryAssociation = BinaryAssociation(
    name="result819",
    ends={
        Property(name="uml3_0_0_OutputPin821", type=uml3_0_0_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_WriteStructuralFeatureAction820", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result822: BinaryAssociation = BinaryAssociation(
    name="result822",
    ends={
        Property(name="uml3_0_0_OutputPin823", type=uml3_0_0_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ClearStructuralFeatureAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt824: BinaryAssociation = BinaryAssociation(
    name="removeAt824",
    ends={
        Property(name="uml3_0_0_InputPin825", type=uml3_0_0_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RemoveStructuralFeatureValueAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt826: BinaryAssociation = BinaryAssociation(
    name="insertAt826",
    ends={
        Property(name="uml3_0_0_InputPin827", type=uml3_0_0_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_AddStructuralFeatureValueAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endData828: BinaryAssociation = BinaryAssociation(
    name="endData828",
    ends={
        Property(name="uml3_0_0_LinkEndData", type=uml3_0_0_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkAction", type=uml3_0_0_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue829: BinaryAssociation = BinaryAssociation(
    name="inputValue829",
    ends={
        Property(name="uml3_0_0_InputPin831", type=uml3_0_0_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkAction830", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value832: BinaryAssociation = BinaryAssociation(
    name="value832",
    ends={
        Property(name="uml3_0_0_InputPin834", type=uml3_0_0_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkEndData833", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end835: BinaryAssociation = BinaryAssociation(
    name="end835",
    ends={
        Property(name="uml3_0_0_LinkEndData836", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Property837", type=uml3_0_0_LinkEndData, multiplicity=Multiplicity(1, 1))
    }
)
qualifier838: BinaryAssociation = BinaryAssociation(
    name="qualifier838",
    ends={
        Property(name="uml3_0_0_QualifierValue", type=uml3_0_0_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkEndData839", type=uml3_0_0_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier840: BinaryAssociation = BinaryAssociation(
    name="qualifier840",
    ends={
        Property(name="uml3_0_0_Property842", type=uml3_0_0_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_QualifierValue841", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1))
    }
)
value843: BinaryAssociation = BinaryAssociation(
    name="value843",
    ends={
        Property(name="uml3_0_0_InputPin845", type=uml3_0_0_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_QualifierValue844", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
result846: BinaryAssociation = BinaryAssociation(
    name="result846",
    ends={
        Property(name="uml3_0_0_OutputPin847", type=uml3_0_0_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt848: BinaryAssociation = BinaryAssociation(
    name="insertAt848",
    ends={
        Property(name="uml3_0_0_InputPin849", type=uml3_0_0_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkEndCreationData", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt850: BinaryAssociation = BinaryAssociation(
    name="destroyAt850",
    ends={
        Property(name="uml3_0_0_InputPin851", type=uml3_0_0_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LinkEndDestructionData", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
object852: BinaryAssociation = BinaryAssociation(
    name="object852",
    ends={
        Property(name="uml3_0_0_InputPin853", type=uml3_0_0_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ClearAssociationAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association854: BinaryAssociation = BinaryAssociation(
    name="association854",
    ends={
        Property(name="uml3_0_0_Association856", type=uml3_0_0_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ClearAssociationAction855", type=uml3_0_0_Association, multiplicity=Multiplicity(1, 1))
    }
)
signal857: BinaryAssociation = BinaryAssociation(
    name="signal857",
    ends={
        Property(name="uml3_0_0_Signal858", type=uml3_0_0_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_BroadcastSignalAction", type=uml3_0_0_Signal, multiplicity=Multiplicity(1, 1))
    }
)
target859: BinaryAssociation = BinaryAssociation(
    name="target859",
    ends={
        Property(name="uml3_0_0_InputPin860", type=uml3_0_0_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendObjectAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request861: BinaryAssociation = BinaryAssociation(
    name="request861",
    ends={
        Property(name="uml3_0_0_InputPin863", type=uml3_0_0_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_SendObjectAction862", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value864: BinaryAssociation = BinaryAssociation(
    name="value864",
    ends={
        Property(name="uml3_0_0_ValueSpecification865", type=uml3_0_0_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ValueSpecificationAction", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result866: BinaryAssociation = BinaryAssociation(
    name="result866",
    ends={
        Property(name="uml3_0_0_OutputPin868", type=uml3_0_0_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ValueSpecificationAction867", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr869: BinaryAssociation = BinaryAssociation(
    name="expr869",
    ends={
        Property(name="uml3_0_0_ValueSpecification870", type=uml3_0_0_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TimeExpression", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation871: BinaryAssociation = BinaryAssociation(
    name="observation871",
    ends={
        Property(name="uml3_0_0_Observation", type=uml3_0_0_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TimeExpression872", type=uml3_0_0_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
expr873: BinaryAssociation = BinaryAssociation(
    name="expr873",
    ends={
        Property(name="uml3_0_0_ValueSpecification874", type=uml3_0_0_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Duration", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation875: BinaryAssociation = BinaryAssociation(
    name="observation875",
    ends={
        Property(name="uml3_0_0_Observation877", type=uml3_0_0_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Duration876", type=uml3_0_0_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
min878: BinaryAssociation = BinaryAssociation(
    name="min878",
    ends={
        Property(name="uml3_0_0_ValueSpecification879", type=uml3_0_0_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interval", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
max880: BinaryAssociation = BinaryAssociation(
    name="max880",
    ends={
        Property(name="uml3_0_0_ValueSpecification882", type=uml3_0_0_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Interval881", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
event883: BinaryAssociation = BinaryAssociation(
    name="event883",
    ends={
        Property(name="uml3_0_0_NamedElement884", type=uml3_0_0_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TimeObservation", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event885: BinaryAssociation = BinaryAssociation(
    name="event885",
    ends={
        Property(name="uml3_0_0_NamedElement886", type=uml3_0_0_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_DurationObservation", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
when887: BinaryAssociation = BinaryAssociation(
    name="when887",
    ends={
        Property(name="uml3_0_0_TimeExpression888", type=uml3_0_0_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_TimeEvent", type=uml3_0_0_TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable889: BinaryAssociation = BinaryAssociation(
    name="variable889",
    ends={
        Property(name="uml3_0_0_Variable", type=uml3_0_0_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_VariableAction", type=uml3_0_0_Variable, multiplicity=Multiplicity(1, 1))
    }
)
result890: BinaryAssociation = BinaryAssociation(
    name="result890",
    ends={
        Property(name="uml3_0_0_OutputPin891", type=uml3_0_0_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadVariableAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value892: BinaryAssociation = BinaryAssociation(
    name="value892",
    ends={
        Property(name="uml3_0_0_InputPin893", type=uml3_0_0_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_WriteVariableAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt894: BinaryAssociation = BinaryAssociation(
    name="insertAt894",
    ends={
        Property(name="uml3_0_0_InputPin895", type=uml3_0_0_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_AddVariableValueAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt896: BinaryAssociation = BinaryAssociation(
    name="removeAt896",
    ends={
        Property(name="uml3_0_0_InputPin897", type=uml3_0_0_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RemoveVariableValueAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception898: BinaryAssociation = BinaryAssociation(
    name="exception898",
    ends={
        Property(name="uml3_0_0_InputPin899", type=uml3_0_0_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_RaiseExceptionAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromAction900: BinaryAssociation = BinaryAssociation(
    name="fromAction900",
    ends={
        Property(name="uml3_0_0_Action901", type=uml3_0_0_ActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ActionInputPin", type=uml3_0_0_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
represented902: BinaryAssociation = BinaryAssociation(
    name="represented902",
    ends={
        Property(name="uml3_0_0_Classifier903", type=uml3_0_0_InformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationItem", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
realization904: BinaryAssociation = BinaryAssociation(
    name="realization904",
    ends={
        Property(name="uml3_0_0_Relationship905", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow", type=uml3_0_0_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed906: BinaryAssociation = BinaryAssociation(
    name="conveyed906",
    ends={
        Property(name="uml3_0_0_Classifier908", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow907", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
informationSource909: BinaryAssociation = BinaryAssociation(
    name="informationSource909",
    ends={
        Property(name="uml3_0_0_NamedElement911", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow910", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
informationTarget912: BinaryAssociation = BinaryAssociation(
    name="informationTarget912",
    ends={
        Property(name="uml3_0_0_NamedElement914", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow913", type=uml3_0_0_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
realizingActivityEdge915: BinaryAssociation = BinaryAssociation(
    name="realizingActivityEdge915",
    ends={
        Property(name="uml3_0_0_ActivityEdge917", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow916", type=uml3_0_0_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
realizingConnector918: BinaryAssociation = BinaryAssociation(
    name="realizingConnector918",
    ends={
        Property(name="uml3_0_0_Connector920", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow919", type=uml3_0_0_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
realizingMessage921: BinaryAssociation = BinaryAssociation(
    name="realizingMessage921",
    ends={
        Property(name="uml3_0_0_Message923", type=uml3_0_0_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_InformationFlow922", type=uml3_0_0_Message, multiplicity=Multiplicity(0, 9999))
    }
)
result924: BinaryAssociation = BinaryAssociation(
    name="result924",
    ends={
        Property(name="uml3_0_0_OutputPin925", type=uml3_0_0_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadExtentAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier926: BinaryAssociation = BinaryAssociation(
    name="classifier926",
    ends={
        Property(name="uml3_0_0_Classifier928", type=uml3_0_0_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadExtentAction927", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
oldClassifier929: BinaryAssociation = BinaryAssociation(
    name="oldClassifier929",
    ends={
        Property(name="uml3_0_0_Classifier930", type=uml3_0_0_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReclassifyObjectAction", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier931: BinaryAssociation = BinaryAssociation(
    name="newClassifier931",
    ends={
        Property(name="uml3_0_0_Classifier933", type=uml3_0_0_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReclassifyObjectAction932", type=uml3_0_0_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object934: BinaryAssociation = BinaryAssociation(
    name="object934",
    ends={
        Property(name="uml3_0_0_InputPin936", type=uml3_0_0_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReclassifyObjectAction935", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier937: BinaryAssociation = BinaryAssociation(
    name="classifier937",
    ends={
        Property(name="uml3_0_0_Classifier938", type=uml3_0_0_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadIsClassifiedObjectAction", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result939: BinaryAssociation = BinaryAssociation(
    name="result939",
    ends={
        Property(name="uml3_0_0_OutputPin941", type=uml3_0_0_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadIsClassifiedObjectAction940", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object942: BinaryAssociation = BinaryAssociation(
    name="object942",
    ends={
        Property(name="uml3_0_0_InputPin944", type=uml3_0_0_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadIsClassifiedObjectAction943", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object945: BinaryAssociation = BinaryAssociation(
    name="object945",
    ends={
        Property(name="uml3_0_0_InputPin946", type=uml3_0_0_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StartClassifierBehaviorAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object947: BinaryAssociation = BinaryAssociation(
    name="object947",
    ends={
        Property(name="uml3_0_0_InputPin948", type=uml3_0_0_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end949: BinaryAssociation = BinaryAssociation(
    name="end949",
    ends={
        Property(name="uml3_0_0_Property951", type=uml3_0_0_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndAction950", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1))
    }
)
result952: BinaryAssociation = BinaryAssociation(
    name="result952",
    ends={
        Property(name="uml3_0_0_OutputPin954", type=uml3_0_0_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndAction953", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object955: BinaryAssociation = BinaryAssociation(
    name="object955",
    ends={
        Property(name="uml3_0_0_InputPin956", type=uml3_0_0_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndQualifierAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier960: BinaryAssociation = BinaryAssociation(
    name="qualifier960",
    ends={
        Property(name="uml3_0_0_Property962", type=uml3_0_0_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndQualifierAction961", type=uml3_0_0_Property, multiplicity=Multiplicity(1, 1))
    }
)
result963: BinaryAssociation = BinaryAssociation(
    name="result963",
    ends={
        Property(name="uml3_0_0_OutputPin964", type=uml3_0_0_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_CreateLinkObjectAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result965: BinaryAssociation = BinaryAssociation(
    name="result965",
    ends={
        Property(name="uml3_0_0_OutputPin966", type=uml3_0_0_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_AcceptEventAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger967: BinaryAssociation = BinaryAssociation(
    name="trigger967",
    ends={
        Property(name="uml3_0_0_Trigger969", type=uml3_0_0_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_AcceptEventAction968", type=uml3_0_0_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnInformation970: BinaryAssociation = BinaryAssociation(
    name="returnInformation970",
    ends={
        Property(name="uml3_0_0_OutputPin971", type=uml3_0_0_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_AcceptCallAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyToCall972: BinaryAssociation = BinaryAssociation(
    name="replyToCall972",
    ends={
        Property(name="uml3_0_0_Trigger973", type=uml3_0_0_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReplyAction", type=uml3_0_0_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
returnInformation974: BinaryAssociation = BinaryAssociation(
    name="returnInformation974",
    ends={
        Property(name="uml3_0_0_InputPin976", type=uml3_0_0_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReplyAction975", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue977: BinaryAssociation = BinaryAssociation(
    name="replyValue977",
    ends={
        Property(name="uml3_0_0_InputPin979", type=uml3_0_0_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReplyAction978", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result980: BinaryAssociation = BinaryAssociation(
    name="result980",
    ends={
        Property(name="uml3_0_0_OutputPin981", type=uml3_0_0_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_UnmarshallAction", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result957: BinaryAssociation = BinaryAssociation(
    name="result957",
    ends={
        Property(name="uml3_0_0_OutputPin959", type=uml3_0_0_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReadLinkObjectEndQualifierAction958", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object985: BinaryAssociation = BinaryAssociation(
    name="object985",
    ends={
        Property(name="uml3_0_0_InputPin987", type=uml3_0_0_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_UnmarshallAction986", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer988: BinaryAssociation = BinaryAssociation(
    name="reducer988",
    ends={
        Property(name="uml3_0_0_Behavior989", type=uml3_0_0_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReduceAction", type=uml3_0_0_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result990: BinaryAssociation = BinaryAssociation(
    name="result990",
    ends={
        Property(name="uml3_0_0_OutputPin992", type=uml3_0_0_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReduceAction991", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection993: BinaryAssociation = BinaryAssociation(
    name="collection993",
    ends={
        Property(name="uml3_0_0_InputPin995", type=uml3_0_0_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ReduceAction994", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object996: BinaryAssociation = BinaryAssociation(
    name="object996",
    ends={
        Property(name="uml3_0_0_InputPin997", type=uml3_0_0_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_StartObjectBehaviorAction", type=uml3_0_0_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
joinSpec998: BinaryAssociation = BinaryAssociation(
    name="joinSpec998",
    ends={
        Property(name="uml3_0_0_ValueSpecification999", type=uml3_0_0_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_JoinNode", type=uml3_0_0_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unmarshallType982: BinaryAssociation = BinaryAssociation(
    name="unmarshallType982",
    ends={
        Property(name="uml3_0_0_Classifier984", type=uml3_0_0_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_UnmarshallAction983", type=uml3_0_0_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result1001: BinaryAssociation = BinaryAssociation(
    name="result1001",
    ends={
        Property(name="uml3_0_0_ConditionalNode1002", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml3_0_0_OutputPin1003", type=uml3_0_0_ConditionalNode, multiplicity=Multiplicity(1, 1))
    }
)
test1004: BinaryAssociation = BinaryAssociation(
    name="test1004",
    ends={
        Property(name="uml3_0_0_ExecutableNode1006", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Clause1005", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
body1007: BinaryAssociation = BinaryAssociation(
    name="body1007",
    ends={
        Property(name="uml3_0_0_ExecutableNode1009", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Clause1008", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause1011: BinaryAssociation = BinaryAssociation(
    name="predecessorClause1011",
    ends={
        Property(name="Clause", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=uml3_0_0_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause1013: BinaryAssociation = BinaryAssociation(
    name="successorClause1013",
    ends={
        Property(name="Clause1014", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=uml3_0_0_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider1015: BinaryAssociation = BinaryAssociation(
    name="decider1015",
    ends={
        Property(name="uml3_0_0_OutputPin1017", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Clause1016", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput1038: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1038",
    ends={
        Property(name="uml3_0_0_OutputPin1040", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1039", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput1041: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput1041",
    ends={
        Property(name="uml3_0_0_InputPin1043", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1042", type=uml3_0_0_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput1044: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput1044",
    ends={
        Property(name="ExpansionRegion", type=uml3_0_0_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=uml3_0_0_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput1045: BinaryAssociation = BinaryAssociation(
    name="regionAsInput1045",
    ends={
        Property(name="ExpansionRegion1046", type=uml3_0_0_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=uml3_0_0_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
clause1000: BinaryAssociation = BinaryAssociation(
    name="clause1000",
    ends={
        Property(name="uml3_0_0_Clause", type=uml3_0_0_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ConditionalNode", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bodyOutput1018: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1018",
    ends={
        Property(name="uml3_0_0_OutputPin1020", type=uml3_0_0_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_Clause1019", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart1021: BinaryAssociation = BinaryAssociation(
    name="bodyPart1021",
    ends={
        Property(name="uml3_0_0_ExecutableNode1022", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart1023: BinaryAssociation = BinaryAssociation(
    name="setupPart1023",
    ends={
        Property(name="uml3_0_0_ExecutableNode1025", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1024", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
decider1026: BinaryAssociation = BinaryAssociation(
    name="decider1026",
    ends={
        Property(name="uml3_0_0_OutputPin1028", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1027", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test1029: BinaryAssociation = BinaryAssociation(
    name="test1029",
    ends={
        Property(name="uml3_0_0_ExecutableNode1031", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1030", type=uml3_0_0_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result1032: BinaryAssociation = BinaryAssociation(
    name="result1032",
    ends={
        Property(name="uml3_0_0_OutputPin1034", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1033", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable1035: BinaryAssociation = BinaryAssociation(
    name="loopVariable1035",
    ends={
        Property(name="uml3_0_0_OutputPin1037", type=uml3_0_0_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_LoopNode1036", type=uml3_0_0_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement1047: BinaryAssociation = BinaryAssociation(
    name="inputElement1047",
    ends={
        Property(name="ExpansionNode", type=uml3_0_0_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=uml3_0_0_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement1048: BinaryAssociation = BinaryAssociation(
    name="outputElement1048",
    ends={
        Property(name="ExpansionNode1049", type=uml3_0_0_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=uml3_0_0_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
postCondition1050: BinaryAssociation = BinaryAssociation(
    name="postCondition1050",
    ends={
        Property(name="uml3_0_0_Constraint1051", type=uml3_0_0_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ProtocolTransition", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
referred1052: BinaryAssociation = BinaryAssociation(
    name="referred1052",
    ends={
        Property(name="uml3_0_0_Operation1054", type=uml3_0_0_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ProtocolTransition1053", type=uml3_0_0_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
preCondition1055: BinaryAssociation = BinaryAssociation(
    name="preCondition1055",
    ends={
        Property(name="uml3_0_0_Constraint1057", type=uml3_0_0_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml3_0_0_ProtocolTransition1056", type=uml3_0_0_Constraint, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uml3_0_0_Package_Namespace = Generalization(general=Namespace, specific=uml3_0_0_Package)
gen_uml3_0_0_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Package)
gen_uml3_0_0_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=uml3_0_0_Package)
gen_uml3_0_0_Comment_Element = Generalization(general=Element, specific=uml3_0_0_Comment)
gen_uml3_0_0_Element_EModelElement = Generalization(general=EModelElement, specific=uml3_0_0_Element)
gen_uml3_0_0_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Dependency)
gen_uml3_0_0_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_Dependency)
gen_uml3_0_0_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=uml3_0_0_DirectedRelationship)
gen_uml3_0_0_Relationship_Element = Generalization(general=Element, specific=uml3_0_0_Relationship)
gen_uml3_0_0_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_PackageableElement)
gen_uml3_0_0_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml3_0_0_PackageableElement)
gen_uml3_0_0_NamedElement_Element = Generalization(general=Element, specific=uml3_0_0_NamedElement)
gen_uml3_0_0_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_ElementImport)
gen_uml3_0_0_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_PackageImport)
gen_uml3_0_0_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Constraint)
gen_uml3_0_0_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Namespace)
gen_uml3_0_0_Association_Classifier = Generalization(general=Classifier, specific=uml3_0_0_Association)
gen_uml3_0_0_Association_Relationship = Generalization(general=Relationship, specific=uml3_0_0_Association)
gen_uml3_0_0_Classifier_Namespace = Generalization(general=Namespace, specific=uml3_0_0_Classifier)
gen_uml3_0_0_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_Classifier)
gen_uml3_0_0_Classifier_Type = Generalization(general=Type, specific=uml3_0_0_Classifier)
gen_uml3_0_0_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=uml3_0_0_Classifier)
gen_uml3_0_0_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_ValueSpecification)
gen_uml3_0_0_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=uml3_0_0_ValueSpecification)
gen_uml3_0_0_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_TypedElement)
gen_uml3_0_0_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Type)
gen_uml3_0_0_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_RedefinableElement)
gen_uml3_0_0_TemplateableElement_Element = Generalization(general=Element, specific=uml3_0_0_TemplateableElement)
gen_uml3_0_0_TemplateParameter_Element = Generalization(general=Element, specific=uml3_0_0_TemplateParameter)
gen_uml3_0_0_ParameterableElement_Element = Generalization(general=Element, specific=uml3_0_0_ParameterableElement)
gen_uml3_0_0_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=uml3_0_0_TemplateParameterSubstitution)
gen_uml3_0_0_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_TemplateBinding)
gen_uml3_0_0_TemplateSignature_Element = Generalization(general=Element, specific=uml3_0_0_TemplateSignature)
gen_uml3_0_0_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_GeneralizationSet)
gen_uml3_0_0_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_Feature)
gen_uml3_0_0_Substitution_Realization = Generalization(general=Realization, specific=uml3_0_0_Substitution)
gen_uml3_0_0_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_Generalization)
gen_uml3_0_0_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=uml3_0_0_Parameter)
gen_uml3_0_0_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml3_0_0_Parameter)
gen_uml3_0_0_MultiplicityElement_Element = Generalization(general=Element, specific=uml3_0_0_MultiplicityElement)
gen_uml3_0_0_Realization_Abstraction = Generalization(general=Abstraction, specific=uml3_0_0_Realization)
gen_uml3_0_0_Abstraction_Dependency = Generalization(general=Dependency, specific=uml3_0_0_Abstraction)
gen_uml3_0_0_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_OpaqueExpression)
gen_uml3_0_0_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml3_0_0_ConnectorEnd)
gen_uml3_0_0_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=uml3_0_0_Property)
gen_uml3_0_0_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=uml3_0_0_Property)
gen_uml3_0_0_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml3_0_0_Property)
gen_uml3_0_0_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=uml3_0_0_ConnectableElement)
gen_uml3_0_0_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml3_0_0_ConnectableElement)
gen_uml3_0_0_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_DeploymentTarget)
gen_uml3_0_0_Deployment_Dependency = Generalization(general=Dependency, specific=uml3_0_0_Deployment)
gen_uml3_0_0_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=uml3_0_0_DeploymentSpecification)
gen_uml3_0_0_Artifact_Classifier = Generalization(general=Classifier, specific=uml3_0_0_Artifact)
gen_uml3_0_0_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=uml3_0_0_Artifact)
gen_uml3_0_0_Manifestation_Abstraction = Generalization(general=Abstraction, specific=uml3_0_0_Manifestation)
gen_uml3_0_0_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_DeployedArtifact)
gen_uml3_0_0_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml3_0_0_Operation)
gen_uml3_0_0_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=uml3_0_0_Operation)
gen_uml3_0_0_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=uml3_0_0_Operation)
gen_uml3_0_0_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=uml3_0_0_BehavioralFeature)
gen_uml3_0_0_BehavioralFeature_Feature = Generalization(general=Feature, specific=uml3_0_0_BehavioralFeature)
gen_uml3_0_0_Behavior_Class = Generalization(general=Class_, specific=uml3_0_0_Behavior)
gen_uml3_0_0_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=uml3_0_0_Class)
gen_uml3_0_0_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml3_0_0_Class)
gen_uml3_0_0_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=uml3_0_0_BehavioredClassifier)
gen_uml3_0_0_InterfaceRealization_Realization = Generalization(general=Realization, specific=uml3_0_0_InterfaceRealization)
gen_uml3_0_0_Interface_Classifier = Generalization(general=Classifier, specific=uml3_0_0_Interface)
gen_uml3_0_0_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml3_0_0_Reception)
gen_uml3_0_0_Signal_Classifier = Generalization(general=Classifier, specific=uml3_0_0_Signal)
gen_uml3_0_0_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=uml3_0_0_ProtocolStateMachine)
gen_uml3_0_0_Region_Namespace = Generalization(general=Namespace, specific=uml3_0_0_Region)
gen_uml3_0_0_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_Region)
gen_uml3_0_0_StateMachine_Behavior = Generalization(general=Behavior, specific=uml3_0_0_StateMachine)
gen_uml3_0_0_Vertex_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Vertex)
gen_uml3_0_0_Transition_Namespace = Generalization(general=Namespace, specific=uml3_0_0_Transition)
gen_uml3_0_0_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_Transition)
gen_uml3_0_0_Trigger_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Trigger)
gen_uml3_0_0_Event_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Event)
gen_uml3_0_0_Port_Property = Generalization(general=Property_, specific=uml3_0_0_Port)
gen_uml3_0_0_State_Namespace = Generalization(general=Namespace, specific=uml3_0_0_State)
gen_uml3_0_0_State_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_State)
gen_uml3_0_0_State_Vertex = Generalization(general=Vertex, specific=uml3_0_0_State)
gen_uml3_0_0_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=uml3_0_0_ConnectionPointReference)
gen_uml3_0_0_Pseudostate_Vertex = Generalization(general=Vertex, specific=uml3_0_0_Pseudostate)
gen_uml3_0_0_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_ProtocolConformance)
gen_uml3_0_0_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=uml3_0_0_StructuredClassifier)
gen_uml3_0_0_Connector_Feature = Generalization(general=Feature, specific=uml3_0_0_Connector)
gen_uml3_0_0_Extension_Association = Generalization(general=Association, specific=uml3_0_0_Extension)
gen_uml3_0_0_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml3_0_0_EncapsulatedClassifier)
gen_uml3_0_0_Image_Element = Generalization(general=Element, specific=uml3_0_0_Image)
gen_uml3_0_0_Profile_Package = Generalization(general=Package, specific=uml3_0_0_Profile)
gen_uml3_0_0_Model_Package = Generalization(general=Package, specific=uml3_0_0_Model)
gen_uml3_0_0_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_ParameterSet)
gen_uml3_0_0_DataType_Classifier = Generalization(general=Classifier, specific=uml3_0_0_DataType)
gen_uml3_0_0_ExtensionEnd_Property = Generalization(general=Property_, specific=uml3_0_0_ExtensionEnd)
gen_uml3_0_0_Stereotype_Class = Generalization(general=Class_, specific=uml3_0_0_Stereotype)
gen_uml3_0_0_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml3_0_0_ConnectableElementTemplateParameter)
gen_uml3_0_0_CollaborationUse_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_CollaborationUse)
gen_uml3_0_0_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml3_0_0_Collaboration)
gen_uml3_0_0_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml3_0_0_Collaboration)
gen_uml3_0_0_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml3_0_0_UseCase)
gen_uml3_0_0_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml3_0_0_OperationTemplateParameter)
gen_uml3_0_0_StructuralFeature_Feature = Generalization(general=Feature, specific=uml3_0_0_StructuralFeature)
gen_uml3_0_0_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=uml3_0_0_StructuralFeature)
gen_uml3_0_0_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml3_0_0_StructuralFeature)
gen_uml3_0_0_Extend_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Extend)
gen_uml3_0_0_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_Extend)
gen_uml3_0_0_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_ExtensionPoint)
gen_uml3_0_0_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_RedefinableTemplateSignature)
gen_uml3_0_0_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=uml3_0_0_RedefinableTemplateSignature)
gen_uml3_0_0_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=uml3_0_0_ClassifierTemplateParameter)
gen_uml3_0_0_Include_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Include)
gen_uml3_0_0_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_Include)
gen_uml3_0_0_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_Expression)
gen_uml3_0_0_Usage_Dependency = Generalization(general=Dependency, specific=uml3_0_0_Usage)
gen_uml3_0_0_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_PackageMerge)
gen_uml3_0_0_ProfileApplication_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_ProfileApplication)
gen_uml3_0_0_Enumeration_DataType = Generalization(general=DataType, specific=uml3_0_0_Enumeration)
gen_uml3_0_0_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=uml3_0_0_EnumerationLiteral)
gen_uml3_0_0_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml3_0_0_InstanceSpecification)
gen_uml3_0_0_StringExpression_Expression = Generalization(general=Expression, specific=uml3_0_0_StringExpression)
gen_uml3_0_0_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=uml3_0_0_StringExpression)
gen_uml3_0_0_Slot_Element = Generalization(general=Element, specific=uml3_0_0_Slot)
gen_uml3_0_0_PrimitiveType_DataType = Generalization(general=DataType, specific=uml3_0_0_PrimitiveType)
gen_uml3_0_0_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_LiteralSpecification)
gen_uml3_0_0_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml3_0_0_LiteralInteger)
gen_uml3_0_0_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml3_0_0_LiteralString)
gen_uml3_0_0_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml3_0_0_LiteralBoolean)
gen_uml3_0_0_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml3_0_0_LiteralNull)
gen_uml3_0_0_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_InstanceValue)
gen_uml3_0_0_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_InstanceSpecification)
gen_uml3_0_0_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=uml3_0_0_InstanceSpecification)
gen_uml3_0_0_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=uml3_0_0_OpaqueBehavior)
gen_uml3_0_0_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=uml3_0_0_FunctionBehavior)
gen_uml3_0_0_OpaqueAction_Action = Generalization(general=Action, specific=uml3_0_0_OpaqueAction)
gen_uml3_0_0_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=uml3_0_0_Action)
gen_uml3_0_0_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=uml3_0_0_ExecutableNode)
gen_uml3_0_0_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=uml3_0_0_LiteralUnlimitedNatural)
gen_uml3_0_0_StructuredActivityNode_Action = Generalization(general=Action, specific=uml3_0_0_StructuredActivityNode)
gen_uml3_0_0_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=uml3_0_0_StructuredActivityNode)
gen_uml3_0_0_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=uml3_0_0_StructuredActivityNode)
gen_uml3_0_0_ActivityGroup_Element = Generalization(general=Element, specific=uml3_0_0_ActivityGroup)
gen_uml3_0_0_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_ActivityNode)
gen_uml3_0_0_Activity_Behavior = Generalization(general=Behavior, specific=uml3_0_0_Activity)
gen_uml3_0_0_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=uml3_0_0_Variable)
gen_uml3_0_0_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml3_0_0_Variable)
gen_uml3_0_0_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_ActivityPartition)
gen_uml3_0_0_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=uml3_0_0_ActivityPartition)
gen_uml3_0_0_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=uml3_0_0_ActivityEdge)
gen_uml3_0_0_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=uml3_0_0_InterruptibleActivityRegion)
gen_uml3_0_0_ExceptionHandler_Element = Generalization(general=Element, specific=uml3_0_0_ExceptionHandler)
gen_uml3_0_0_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=uml3_0_0_ObjectNode)
gen_uml3_0_0_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=uml3_0_0_ObjectNode)
gen_uml3_0_0_OutputPin_Pin = Generalization(general=Pin, specific=uml3_0_0_OutputPin)
gen_uml3_0_0_Pin_ObjectNode = Generalization(general=ObjectNode, specific=uml3_0_0_Pin)
gen_uml3_0_0_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml3_0_0_Pin)
gen_uml3_0_0_InputPin_Pin = Generalization(general=Pin, specific=uml3_0_0_InputPin)
gen_uml3_0_0_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=uml3_0_0_CallAction)
gen_uml3_0_0_InvocationAction_Action = Generalization(general=Action, specific=uml3_0_0_InvocationAction)
gen_uml3_0_0_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=uml3_0_0_SendSignalAction)
gen_uml3_0_0_CallOperationAction_CallAction = Generalization(general=CallAction, specific=uml3_0_0_CallOperationAction)
gen_uml3_0_0_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=uml3_0_0_CallBehaviorAction)
gen_uml3_0_0_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=uml3_0_0_ControlNode)
gen_uml3_0_0_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml3_0_0_ControlFlow)
gen_uml3_0_0_InitialNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_InitialNode)
gen_uml3_0_0_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=uml3_0_0_ActivityParameterNode)
gen_uml3_0_0_ValuePin_InputPin = Generalization(general=InputPin, specific=uml3_0_0_ValuePin)
gen_uml3_0_0_Message_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Message)
gen_uml3_0_0_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml3_0_0_SequenceNode)
gen_uml3_0_0_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_MessageEnd)
gen_uml3_0_0_Interaction_Behavior = Generalization(general=Behavior, specific=uml3_0_0_Interaction)
gen_uml3_0_0_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_Interaction)
gen_uml3_0_0_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_InteractionFragment)
gen_uml3_0_0_Lifeline_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_Lifeline)
gen_uml3_0_0_PartDecomposition_InteractionUse = Generalization(general=InteractionUse, specific=uml3_0_0_PartDecomposition)
gen_uml3_0_0_InteractionUse_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_InteractionUse)
gen_uml3_0_0_Gate_MessageEnd = Generalization(general=MessageEnd, specific=uml3_0_0_Gate)
gen_uml3_0_0_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=uml3_0_0_GeneralOrdering)
gen_uml3_0_0_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_OccurrenceSpecification)
gen_uml3_0_0_InteractionOperand_Namespace = Generalization(general=Namespace, specific=uml3_0_0_InteractionOperand)
gen_uml3_0_0_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_InteractionOperand)
gen_uml3_0_0_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=uml3_0_0_InteractionConstraint)
gen_uml3_0_0_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_ExecutionSpecification)
gen_uml3_0_0_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_StateInvariant)
gen_uml3_0_0_ActionExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=uml3_0_0_ActionExecutionSpecification)
gen_uml3_0_0_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=uml3_0_0_BehaviorExecutionSpecification)
gen_uml3_0_0_ExecutionEvent_Event = Generalization(general=Event, specific=uml3_0_0_ExecutionEvent)
gen_uml3_0_0_CreationEvent_Event = Generalization(general=Event, specific=uml3_0_0_CreationEvent)
gen_uml3_0_0_DestructionEvent_Event = Generalization(general=Event, specific=uml3_0_0_DestructionEvent)
gen_uml3_0_0_SendOperationEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_SendOperationEvent)
gen_uml3_0_0_MessageEvent_Event = Generalization(general=Event, specific=uml3_0_0_MessageEvent)
gen_uml3_0_0_SendSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_SendSignalEvent)
gen_uml3_0_0_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=uml3_0_0_MessageOccurrenceSpecification)
gen_uml3_0_0_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=uml3_0_0_MessageOccurrenceSpecification)
gen_uml3_0_0_ExecutionOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=uml3_0_0_ExecutionOccurrenceSpecification)
gen_uml3_0_0_ReceiveOperationEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_ReceiveOperationEvent)
gen_uml3_0_0_ReceiveSignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_ReceiveSignalEvent)
gen_uml3_0_0_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml3_0_0_Actor)
gen_uml3_0_0_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_CallEvent)
gen_uml3_0_0_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_SignalEvent)
gen_uml3_0_0_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=uml3_0_0_AnyReceiveEvent)
gen_uml3_0_0_ForkNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_ForkNode)
gen_uml3_0_0_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=uml3_0_0_FlowFinalNode)
gen_uml3_0_0_FinalNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_FinalNode)
gen_uml3_0_0_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=uml3_0_0_CentralBufferNode)
gen_uml3_0_0_MergeNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_MergeNode)
gen_uml3_0_0_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_DecisionNode)
gen_uml3_0_0_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=uml3_0_0_ObjectFlow)
gen_uml3_0_0_ChangeEvent_Event = Generalization(general=Event, specific=uml3_0_0_ChangeEvent)
gen_uml3_0_0_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=uml3_0_0_ActivityFinalNode)
gen_uml3_0_0_ComponentRealization_Realization = Generalization(general=Realization, specific=uml3_0_0_ComponentRealization)
gen_uml3_0_0_Component_Class = Generalization(general=Class_, specific=uml3_0_0_Component)
gen_uml3_0_0_Node_Class = Generalization(general=Class_, specific=uml3_0_0_Node)
gen_uml3_0_0_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml3_0_0_Node)
gen_uml3_0_0_CommunicationPath_Association = Generalization(general=Association, specific=uml3_0_0_CommunicationPath)
gen_uml3_0_0_Device_Node = Generalization(general=Node, specific=uml3_0_0_Device)
gen_uml3_0_0_ExecutionEnvironment_Node = Generalization(general=Node, specific=uml3_0_0_ExecutionEnvironment)
gen_uml3_0_0_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_CombinedFragment)
gen_uml3_0_0_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=uml3_0_0_Continuation)
gen_uml3_0_0_ConsiderIgnoreFragment_CombinedFragment = Generalization(general=CombinedFragment, specific=uml3_0_0_ConsiderIgnoreFragment)
gen_uml3_0_0_CreateObjectAction_Action = Generalization(general=Action, specific=uml3_0_0_CreateObjectAction)
gen_uml3_0_0_DestroyObjectAction_Action = Generalization(general=Action, specific=uml3_0_0_DestroyObjectAction)
gen_uml3_0_0_TestIdentityAction_Action = Generalization(general=Action, specific=uml3_0_0_TestIdentityAction)
gen_uml3_0_0_ReadSelfAction_Action = Generalization(general=Action, specific=uml3_0_0_ReadSelfAction)
gen_uml3_0_0_StructuralFeatureAction_Action = Generalization(general=Action, specific=uml3_0_0_StructuralFeatureAction)
gen_uml3_0_0_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml3_0_0_ReadStructuralFeatureAction)
gen_uml3_0_0_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml3_0_0_WriteStructuralFeatureAction)
gen_uml3_0_0_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=uml3_0_0_ClearStructuralFeatureAction)
gen_uml3_0_0_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=uml3_0_0_AddStructuralFeatureValueAction)
gen_uml3_0_0_LinkAction_Action = Generalization(general=Action, specific=uml3_0_0_LinkAction)
gen_uml3_0_0_LinkEndData_Element = Generalization(general=Element, specific=uml3_0_0_LinkEndData)
gen_uml3_0_0_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=uml3_0_0_RemoveStructuralFeatureValueAction)
gen_uml3_0_0_QualifierValue_Element = Generalization(general=Element, specific=uml3_0_0_QualifierValue)
gen_uml3_0_0_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=uml3_0_0_ReadLinkAction)
gen_uml3_0_0_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=uml3_0_0_LinkEndCreationData)
gen_uml3_0_0_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=uml3_0_0_CreateLinkAction)
gen_uml3_0_0_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=uml3_0_0_WriteLinkAction)
gen_uml3_0_0_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=uml3_0_0_DestroyLinkAction)
gen_uml3_0_0_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=uml3_0_0_LinkEndDestructionData)
gen_uml3_0_0_ClearAssociationAction_Action = Generalization(general=Action, specific=uml3_0_0_ClearAssociationAction)
gen_uml3_0_0_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=uml3_0_0_BroadcastSignalAction)
gen_uml3_0_0_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=uml3_0_0_SendObjectAction)
gen_uml3_0_0_ValueSpecificationAction_Action = Generalization(general=Action, specific=uml3_0_0_ValueSpecificationAction)
gen_uml3_0_0_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_TimeExpression)
gen_uml3_0_0_Observation_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_Observation)
gen_uml3_0_0_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_Duration)
gen_uml3_0_0_DurationInterval_Interval = Generalization(general=Interval, specific=uml3_0_0_DurationInterval)
gen_uml3_0_0_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=uml3_0_0_Interval)
gen_uml3_0_0_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=uml3_0_0_TimeConstraint)
gen_uml3_0_0_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=uml3_0_0_IntervalConstraint)
gen_uml3_0_0_TimeInterval_Interval = Generalization(general=Interval, specific=uml3_0_0_TimeInterval)
gen_uml3_0_0_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=uml3_0_0_DurationConstraint)
gen_uml3_0_0_TimeObservation_Observation = Generalization(general=Observation, specific=uml3_0_0_TimeObservation)
gen_uml3_0_0_DurationObservation_Observation = Generalization(general=Observation, specific=uml3_0_0_DurationObservation)
gen_uml3_0_0_FinalState_State = Generalization(general=State, specific=uml3_0_0_FinalState)
gen_uml3_0_0_TimeEvent_Event = Generalization(general=Event, specific=uml3_0_0_TimeEvent)
gen_uml3_0_0_VariableAction_Action = Generalization(general=Action, specific=uml3_0_0_VariableAction)
gen_uml3_0_0_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml3_0_0_WriteVariableAction)
gen_uml3_0_0_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml3_0_0_ClearVariableAction)
gen_uml3_0_0_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=uml3_0_0_AddVariableValueAction)
gen_uml3_0_0_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=uml3_0_0_RemoveVariableValueAction)
gen_uml3_0_0_RaiseExceptionAction_Action = Generalization(general=Action, specific=uml3_0_0_RaiseExceptionAction)
gen_uml3_0_0_ActionInputPin_InputPin = Generalization(general=InputPin, specific=uml3_0_0_ActionInputPin)
gen_uml3_0_0_InformationItem_Classifier = Generalization(general=Classifier, specific=uml3_0_0_InformationItem)
gen_uml3_0_0_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=uml3_0_0_ReadVariableAction)
gen_uml3_0_0_ReadExtentAction_Action = Generalization(general=Action, specific=uml3_0_0_ReadExtentAction)
gen_uml3_0_0_ReclassifyObjectAction_Action = Generalization(general=Action, specific=uml3_0_0_ReclassifyObjectAction)
gen_uml3_0_0_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=uml3_0_0_InformationFlow)
gen_uml3_0_0_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml3_0_0_InformationFlow)
gen_uml3_0_0_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=uml3_0_0_ReadIsClassifiedObjectAction)
gen_uml3_0_0_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=uml3_0_0_StartClassifierBehaviorAction)
gen_uml3_0_0_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=uml3_0_0_ReadLinkObjectEndAction)
gen_uml3_0_0_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=uml3_0_0_ReadLinkObjectEndQualifierAction)
gen_uml3_0_0_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=uml3_0_0_CreateLinkObjectAction)
gen_uml3_0_0_AcceptEventAction_Action = Generalization(general=Action, specific=uml3_0_0_AcceptEventAction)
gen_uml3_0_0_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=uml3_0_0_AcceptCallAction)
gen_uml3_0_0_ReplyAction_Action = Generalization(general=Action, specific=uml3_0_0_ReplyAction)
gen_uml3_0_0_UnmarshallAction_Action = Generalization(general=Action, specific=uml3_0_0_UnmarshallAction)
gen_uml3_0_0_ReduceAction_Action = Generalization(general=Action, specific=uml3_0_0_ReduceAction)
gen_uml3_0_0_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=uml3_0_0_StartObjectBehaviorAction)
gen_uml3_0_0_JoinNode_ControlNode = Generalization(general=ControlNode, specific=uml3_0_0_JoinNode)
gen_uml3_0_0_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=uml3_0_0_DataStoreNode)
gen_uml3_0_0_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml3_0_0_ConditionalNode)
gen_uml3_0_0_Clause_Element = Generalization(general=Element, specific=uml3_0_0_Clause)
gen_uml3_0_0_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=uml3_0_0_ExpansionNode)
gen_uml3_0_0_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml3_0_0_ExpansionRegion)
gen_uml3_0_0_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=uml3_0_0_LoopNode)
gen_uml3_0_0_ProtocolTransition_Transition = Generalization(general=Transition, specific=uml3_0_0_ProtocolTransition)
gen_uml3_0_0_AssociationClass_Class = Generalization(general=Class_, specific=uml3_0_0_AssociationClass)
gen_uml3_0_0_AssociationClass_Association = Generalization(general=Association, specific=uml3_0_0_AssociationClass)

# Domain Model
domain_model = DomainModel(
    name="uml3_0_0",
    types={uml3_0_0_Package, Namespace, PackageableElement, TemplateableElement, uml3_0_0_Type, uml3_0_0_PackageMerge, uml3_0_0_PackageableElement, uml3_0_0_Comment, Element, uml3_0_0_Element, EModelElement, uml3_0_0_Namespace, uml3_0_0_StringExpression, DirectedRelationship, uml3_0_0_DirectedRelationship, Relationship, uml3_0_0_Relationship, uml3_0_0_ProfileApplication, NamedElement, ParameterableElement, uml3_0_0_NamedElement, uml3_0_0_Dependency, uml3_0_0_ElementImport, uml3_0_0_PackageImport, uml3_0_0_Constraint, uml3_0_0_Association, Classifier, uml3_0_0_Property, uml3_0_0_Classifier, RedefinableElement, Type, uml3_0_0_Generalization, uml3_0_0_GeneralizationSet, uml3_0_0_Feature, uml3_0_0_ValueSpecification, TypedElement, uml3_0_0_TypedElement, uml3_0_0_CollaborationUse, uml3_0_0_UseCase, uml3_0_0_RedefinableElement, uml3_0_0_TemplateableElement, uml3_0_0_TemplateBinding, uml3_0_0_TemplateSignature, uml3_0_0_Substitution, uml3_0_0_ParameterableElement, uml3_0_0_TemplateParameterSubstitution, uml3_0_0_TemplateParameter, Realization, ConnectableElement, MultiplicityElement, uml3_0_0_ParameterSet, uml3_0_0_Operation, uml3_0_0_MultiplicityElement, uml3_0_0_Realization, Abstraction, uml3_0_0_Abstraction, Dependency, uml3_0_0_OpaqueExpression, ValueSpecification, uml3_0_0_Parameter, uml3_0_0_Behavior, StructuralFeature, DeploymentTarget, uml3_0_0_Class, uml3_0_0_DataType, uml3_0_0_ConnectableElement, uml3_0_0_ConnectorEnd, uml3_0_0_DeploymentTarget, uml3_0_0_Deployment, uml3_0_0_DeployedArtifact, uml3_0_0_DeploymentSpecification, Artifact, uml3_0_0_Artifact, DeployedArtifact, uml3_0_0_Manifestation, BehavioralFeature, uml3_0_0_Interface, uml3_0_0_BehavioralFeature, Feature, Class_, uml3_0_0_BehavioredClassifier, EncapsulatedClassifier, BehavioredClassifier, uml3_0_0_Reception, uml3_0_0_Extension, uml3_0_0_InterfaceRealization, uml3_0_0_Trigger, uml3_0_0_ProtocolStateMachine, uml3_0_0_Signal, StateMachine, uml3_0_0_ProtocolConformance, uml3_0_0_Region, uml3_0_0_State, uml3_0_0_Pseudostate, uml3_0_0_Vertex, uml3_0_0_Transition, uml3_0_0_StateMachine, Behavior, uml3_0_0_Event, uml3_0_0_Port, Property_, Vertex, uml3_0_0_ConnectionPointReference, uml3_0_0_StructuredClassifier, uml3_0_0_Connector, Association, uml3_0_0_EncapsulatedClassifier, StructuredClassifier, uml3_0_0_Image, uml3_0_0_Profile, Package, uml3_0_0_Model, uml3_0_0_ExtensionEnd, uml3_0_0_Stereotype, uml3_0_0_ConnectableElementTemplateParameter, uml3_0_0_Collaboration, uml3_0_0_Include, uml3_0_0_Extend, uml3_0_0_ExtensionPoint, uml3_0_0_OperationTemplateParameter, TemplateParameter, uml3_0_0_StructuralFeature, uml3_0_0_RedefinableTemplateSignature, TemplateSignature, uml3_0_0_ClassifierTemplateParameter, uml3_0_0_Expression, uml3_0_0_Usage, uml3_0_0_Enumeration, DataType, uml3_0_0_EnumerationLiteral, InstanceSpecification, uml3_0_0_InstanceSpecification, Expression, uml3_0_0_Slot, uml3_0_0_PrimitiveType, uml3_0_0_LiteralSpecification, uml3_0_0_LiteralInteger, LiteralSpecification, uml3_0_0_LiteralString, uml3_0_0_LiteralBoolean, uml3_0_0_LiteralNull, uml3_0_0_InstanceValue, uml3_0_0_FunctionBehavior, OpaqueBehavior, uml3_0_0_OpaqueAction, Action, uml3_0_0_InputPin, uml3_0_0_OutputPin, uml3_0_0_Action, ExecutableNode, uml3_0_0_ExecutableNode, ActivityNode, uml3_0_0_ExceptionHandler, uml3_0_0_LiteralUnlimitedNatural, uml3_0_0_Activity, uml3_0_0_OpaqueBehavior, uml3_0_0_ActivityEdge, uml3_0_0_ActivityPartition, uml3_0_0_InterruptibleActivityRegion, uml3_0_0_ActivityGroup, ActivityGroup, uml3_0_0_Variable, uml3_0_0_ActivityNode, uml3_0_0_StructuredActivityNode, uml3_0_0_ObjectNode, Pin, uml3_0_0_Pin, ObjectNode, uml3_0_0_CallAction, InvocationAction, uml3_0_0_InvocationAction, uml3_0_0_SendSignalAction, uml3_0_0_CallOperationAction, CallAction, uml3_0_0_CallBehaviorAction, uml3_0_0_ControlNode, uml3_0_0_ControlFlow, ActivityEdge, uml3_0_0_InitialNode, ControlNode, uml3_0_0_ActivityParameterNode, uml3_0_0_ValuePin, InputPin, uml3_0_0_Message, uml3_0_0_MessageEnd, uml3_0_0_Interaction, uml3_0_0_SequenceNode, StructuredActivityNode, InteractionFragment, uml3_0_0_Lifeline, uml3_0_0_InteractionFragment, uml3_0_0_Gate, uml3_0_0_GeneralOrdering, uml3_0_0_PartDecomposition, InteractionUse, uml3_0_0_InteractionUse, uml3_0_0_InteractionOperand, MessageEnd, uml3_0_0_OccurrenceSpecification, uml3_0_0_InteractionConstraint, Constraint, uml3_0_0_ExecutionSpecification, uml3_0_0_StateInvariant, uml3_0_0_ActionExecutionSpecification, ExecutionSpecification, uml3_0_0_BehaviorExecutionSpecification, uml3_0_0_ExecutionEvent, Event, uml3_0_0_CreationEvent, uml3_0_0_DestructionEvent, uml3_0_0_SendOperationEvent, MessageEvent, uml3_0_0_MessageEvent, uml3_0_0_SendSignalEvent, uml3_0_0_MessageOccurrenceSpecification, OccurrenceSpecification, uml3_0_0_ExecutionOccurrenceSpecification, uml3_0_0_ReceiveOperationEvent, uml3_0_0_ReceiveSignalEvent, uml3_0_0_Actor, uml3_0_0_CallEvent, uml3_0_0_ChangeEvent, uml3_0_0_SignalEvent, uml3_0_0_AnyReceiveEvent, uml3_0_0_ForkNode, uml3_0_0_FlowFinalNode, FinalNode, uml3_0_0_FinalNode, uml3_0_0_CentralBufferNode, uml3_0_0_MergeNode, uml3_0_0_DecisionNode, uml3_0_0_ObjectFlow, uml3_0_0_ActivityFinalNode, uml3_0_0_ComponentRealization, uml3_0_0_Component, uml3_0_0_Node, uml3_0_0_CommunicationPath, uml3_0_0_Device, Node, uml3_0_0_ExecutionEnvironment, uml3_0_0_CombinedFragment, uml3_0_0_Continuation, uml3_0_0_ConsiderIgnoreFragment, CombinedFragment, uml3_0_0_CreateObjectAction, uml3_0_0_DestroyObjectAction, uml3_0_0_TestIdentityAction, uml3_0_0_ReadSelfAction, uml3_0_0_StructuralFeatureAction, uml3_0_0_ReadStructuralFeatureAction, StructuralFeatureAction, uml3_0_0_WriteStructuralFeatureAction, uml3_0_0_ClearStructuralFeatureAction, uml3_0_0_RemoveStructuralFeatureValueAction, uml3_0_0_AddStructuralFeatureValueAction, uml3_0_0_LinkAction, uml3_0_0_LinkEndData, WriteStructuralFeatureAction, uml3_0_0_QualifierValue, uml3_0_0_ReadLinkAction, LinkAction, uml3_0_0_LinkEndCreationData, LinkEndData, uml3_0_0_CreateLinkAction, WriteLinkAction, uml3_0_0_WriteLinkAction, uml3_0_0_DestroyLinkAction, uml3_0_0_LinkEndDestructionData, uml3_0_0_ClearAssociationAction, uml3_0_0_BroadcastSignalAction, uml3_0_0_SendObjectAction, uml3_0_0_ValueSpecificationAction, uml3_0_0_TimeExpression, uml3_0_0_Observation, uml3_0_0_Duration, uml3_0_0_DurationInterval, Interval, uml3_0_0_Interval, uml3_0_0_TimeConstraint, IntervalConstraint, uml3_0_0_IntervalConstraint, uml3_0_0_TimeInterval, uml3_0_0_DurationConstraint, uml3_0_0_TimeObservation, Observation, uml3_0_0_DurationObservation, uml3_0_0_FinalState, State, uml3_0_0_TimeEvent, uml3_0_0_VariableAction, uml3_0_0_WriteVariableAction, uml3_0_0_ClearVariableAction, uml3_0_0_AddVariableValueAction, WriteVariableAction, uml3_0_0_RemoveVariableValueAction, uml3_0_0_RaiseExceptionAction, uml3_0_0_ActionInputPin, uml3_0_0_InformationItem, uml3_0_0_ReadVariableAction, VariableAction, uml3_0_0_ReadExtentAction, uml3_0_0_ReclassifyObjectAction, uml3_0_0_InformationFlow, uml3_0_0_ReadIsClassifiedObjectAction, uml3_0_0_StartClassifierBehaviorAction, uml3_0_0_ReadLinkObjectEndAction, uml3_0_0_ReadLinkObjectEndQualifierAction, uml3_0_0_CreateLinkObjectAction, CreateLinkAction, uml3_0_0_AcceptEventAction, uml3_0_0_AcceptCallAction, AcceptEventAction, uml3_0_0_ReplyAction, uml3_0_0_UnmarshallAction, uml3_0_0_ReduceAction, uml3_0_0_StartObjectBehaviorAction, uml3_0_0_JoinNode, uml3_0_0_DataStoreNode, CentralBufferNode, uml3_0_0_ConditionalNode, uml3_0_0_Clause, uml3_0_0_ExpansionNode, uml3_0_0_ExpansionRegion, uml3_0_0_LoopNode, uml3_0_0_ProtocolTransition, Transition, uml3_0_0_AssociationClass, VisibilityKind, TransitionKind, PseudostateKind, ConnectorKind, CallConcurrencyKind, AggregationKind, ParameterDirectionKind, ParameterEffectKind, ObjectNodeOrderingKind, MessageSort, MessageKind, InteractionOperatorKind, ExpansionKind},
    associations={ownedElement2, owner4, ownedComment6, ownedType9, packageMerge10, packagedElement11, nestedPackage13, nestingPackage15, annotatedElement0, namespace19, nameExpression20, supplier21, client23, source24, target26, profileApplication17, clientDependency18, importedMember37, ownedMember40, importedElement42, importingNamespace44, importedPackage46, importingNamespace48, constrainedElement50, relatedElement29, elementImport31, packageImport32, ownedRule34, member35, ownedEnd59, memberEnd60, endType62, navigableOwnedEnd64, generalization66, powertypeExtent67, feature68, specification52, context54, type56, package57, representation81, collaborationUse83, ownedUseCase86, useCase88, redefinedElement90, redefinitionContext91, templateBinding94, ownedTemplateSignature95, inheritedMember69, redefinedClassifier72, general75, substitution77, attribute78, template103, signature105, parameteredElement107, ownedParameteredElement108, default110, ownedDefault112, owningTemplateParameter115, templateParameter117, formal119, signature96, parameterSubstitution97, boundElement98, parameter100, ownedParameter102, generalizationSet131, specific133, powertype135, generalization137, featuringClassifier139, contract141, substitutingClassifier143, actual121, ownedActual124, templateBinding127, general129, parameterSet150, operation151, defaultValue153, mapping145, result146, behavior148, end161, definingEnd162, role165, partWithPort168, class171, upperValue156, datatype173, lowerValue158, redefinedProperty175, owningAssociation177, defaultValue178, opposite182, subsettedProperty185, association187, associationEnd193, deployment195, deployedElement196, deployedArtifact198, configuration199, location200, qualifier190, deployment202, nestedArtifact205, manifestation206, ownedOperation208, ownedAttribute211, interface217, class218, precondition220, postcondition223, utilizedElement214, datatype229, bodyCondition232, type235, ownedParameter238, method240, raisedException241, redefinedOperation227, ownedParameterSet244, redefinedBehavior247, ownedParameter249, context252, precondition254, postcondition257, ownedParameterSet260, nestedClassifier264, ownedOperation267, superClass269, ownedReception271, extension273, specification263, classifierBehavior277, interfaceRealization280, ownedTrigger281, contract283, implementingClassifier284, ownedAttribute285, ownedOperation288, ownedBehavior274, redefinedInterface294, ownedReception296, protocol299, signal301, ownedAttribute303, conformance306, nestedClassifier290, region307, submachineState308, connectionPoint309, extendedStateMachine312, subvertex313, transition314, state316, stateMachine320, outgoing322, incoming323, container326, extendedRegion319, container328, source330, target333, guard339, effect342, trigger345, event348, port350, redefinedTransition337, required352, redefinedPort356, provided358, protocol361, connection366, connectionPoint367, redefinedState371, stateInvariant372, entry375, exit378, doActivity381, submachine364, region387, entry390, exit391, state394, stateMachine396, state398, generalMachine401, specificMachine403, deferrableTrigger384, ownedPort404, ownedAttribute406, part408, role411, ownedConnector414, type416, redefinedConnector420, end422, contract425, metaclass428, icon430, ownedStereotype431, metaclassReference433, metamodelReference436, parameter439, condition440, ownedAttribute443, ownedOperation445, type448, roleBinding450, collaborationRole453, include456, extend457, extensionPoint459, subject460, includingCase465, extendedCase467, condition469, extensionLocation472, extension474, useCase476, extendedSignature479, inheritedParameter480, classifier483, constrainingClassifier486, addition463, owningExpression491, operand493, mergedPackage495, receivingPackage497, appliedProfile499, applyingPackage501, ownedLiteral503, enumeration504, subExpression489, slot507, specification508, definingFeature511, value512, owningInstance515, instance516, classifier505, inputValue518, outputValue519, output521, input523, context526, localPrecondition529, localPostcondition532, handler535, activity537, outgoing539, incoming540, inPartition542, inInterruptibleRegion544, inGroup546, redefinedNode548, variable549, edge550, node552, subgroup555, inStructuredNode536, inActivity560, containedEdge562, containedNode564, structuredNode567, variable568, node570, edge572, partition575, group577, scope579, activityScope581, superGroup558, target586, redefinedEdge589, inPartition590, guard592, weight595, interrupts598, inStructuredNode600, inGroup603, activity605, node608, subpartition611, source584, represents616, edge619, node622, interruptingEdge624, handlerBody626, exceptionInput627, exceptionType629, protectedNode632, upperBound633, inState636, superPartition614, result642, argument644, onPort646, target649, signal651, operation654, target656, selection639, executableNode661, parameter663, value665, receiveEvent667, sendEvent668, connector671, interaction674, argument675, signature678, behavior659, message681, lifeline684, fragment685, action686, formalGate688, message690, covered692, generalOrdering694, enclosingInteraction695, represents699, interaction701, selector703, decomposedAs706, coveredBy708, enclosingOperand697, actualGate712, argument715, before718, after719, toBefore721, event722, refersTo710, guard726, fragment727, minint729, maxint732, start735, toAfter724, invariant740, action742, behavior744, operation746, finish737, execution750, operation752, signal754, operation756, signal748, changeExpression758, signal760, decisionInput762, decisionInputFlow764, transformation766, selection769, abstraction772, realizingClassifier773, required775, provided777, packagedElement780, realization783, nestedNode785, cfragmentGate788, message791, classifier793, operand786, result795, target798, first800, second802, result805, result808, structuralFeature810, object812, result815, value817, result819, result822, removeAt824, insertAt826, endData828, inputValue829, value832, end835, qualifier838, qualifier840, value843, result846, insertAt848, destroyAt850, object852, association854, signal857, target859, request861, value864, result866, expr869, observation871, expr873, observation875, min878, max880, event883, event885, when887, variable889, result890, value892, insertAt894, removeAt896, exception898, fromAction900, represented902, realization904, conveyed906, informationSource909, informationTarget912, realizingActivityEdge915, realizingConnector918, realizingMessage921, result924, classifier926, oldClassifier929, newClassifier931, object934, classifier937, result939, object942, object945, object947, end949, result952, object955, qualifier960, result963, result965, trigger967, returnInformation970, replyToCall972, returnInformation974, replyValue977, result980, result957, object985, reducer988, result990, collection993, object996, joinSpec998, unmarshallType982, result1001, test1004, body1007, predecessorClause1011, successorClause1013, decider1015, bodyOutput1038, loopVariableInput1041, regionAsOutput1044, regionAsInput1045, clause1000, bodyOutput1018, bodyPart1021, setupPart1023, decider1026, test1029, result1032, loopVariable1035, inputElement1047, outputElement1048, postCondition1050, referred1052, preCondition1055},
    generalizations={gen_uml3_0_0_Package_Namespace, gen_uml3_0_0_Package_PackageableElement, gen_uml3_0_0_Package_TemplateableElement, gen_uml3_0_0_Comment_Element, gen_uml3_0_0_Element_EModelElement, gen_uml3_0_0_Dependency_PackageableElement, gen_uml3_0_0_Dependency_DirectedRelationship, gen_uml3_0_0_DirectedRelationship_Relationship, gen_uml3_0_0_Relationship_Element, gen_uml3_0_0_PackageableElement_NamedElement, gen_uml3_0_0_PackageableElement_ParameterableElement, gen_uml3_0_0_NamedElement_Element, gen_uml3_0_0_ElementImport_DirectedRelationship, gen_uml3_0_0_PackageImport_DirectedRelationship, gen_uml3_0_0_Constraint_PackageableElement, gen_uml3_0_0_Namespace_NamedElement, gen_uml3_0_0_Association_Classifier, gen_uml3_0_0_Association_Relationship, gen_uml3_0_0_Classifier_Namespace, gen_uml3_0_0_Classifier_RedefinableElement, gen_uml3_0_0_Classifier_Type, gen_uml3_0_0_Classifier_TemplateableElement, gen_uml3_0_0_ValueSpecification_PackageableElement, gen_uml3_0_0_ValueSpecification_TypedElement, gen_uml3_0_0_TypedElement_NamedElement, gen_uml3_0_0_Type_PackageableElement, gen_uml3_0_0_RedefinableElement_NamedElement, gen_uml3_0_0_TemplateableElement_Element, gen_uml3_0_0_TemplateParameter_Element, gen_uml3_0_0_ParameterableElement_Element, gen_uml3_0_0_TemplateParameterSubstitution_Element, gen_uml3_0_0_TemplateBinding_DirectedRelationship, gen_uml3_0_0_TemplateSignature_Element, gen_uml3_0_0_GeneralizationSet_PackageableElement, gen_uml3_0_0_Feature_RedefinableElement, gen_uml3_0_0_Substitution_Realization, gen_uml3_0_0_Generalization_DirectedRelationship, gen_uml3_0_0_Parameter_ConnectableElement, gen_uml3_0_0_Parameter_MultiplicityElement, gen_uml3_0_0_MultiplicityElement_Element, gen_uml3_0_0_Realization_Abstraction, gen_uml3_0_0_Abstraction_Dependency, gen_uml3_0_0_OpaqueExpression_ValueSpecification, gen_uml3_0_0_ConnectorEnd_MultiplicityElement, gen_uml3_0_0_Property_StructuralFeature, gen_uml3_0_0_Property_ConnectableElement, gen_uml3_0_0_Property_DeploymentTarget, gen_uml3_0_0_ConnectableElement_TypedElement, gen_uml3_0_0_ConnectableElement_ParameterableElement, gen_uml3_0_0_DeploymentTarget_NamedElement, gen_uml3_0_0_Deployment_Dependency, gen_uml3_0_0_DeploymentSpecification_Artifact, gen_uml3_0_0_Artifact_Classifier, gen_uml3_0_0_Artifact_DeployedArtifact, gen_uml3_0_0_Manifestation_Abstraction, gen_uml3_0_0_DeployedArtifact_NamedElement, gen_uml3_0_0_Operation_BehavioralFeature, gen_uml3_0_0_Operation_ParameterableElement, gen_uml3_0_0_Operation_TemplateableElement, gen_uml3_0_0_BehavioralFeature_Namespace, gen_uml3_0_0_BehavioralFeature_Feature, gen_uml3_0_0_Behavior_Class, gen_uml3_0_0_Class_EncapsulatedClassifier, gen_uml3_0_0_Class_BehavioredClassifier, gen_uml3_0_0_BehavioredClassifier_Classifier, gen_uml3_0_0_InterfaceRealization_Realization, gen_uml3_0_0_Interface_Classifier, gen_uml3_0_0_Reception_BehavioralFeature, gen_uml3_0_0_Signal_Classifier, gen_uml3_0_0_ProtocolStateMachine_StateMachine, gen_uml3_0_0_Region_Namespace, gen_uml3_0_0_Region_RedefinableElement, gen_uml3_0_0_StateMachine_Behavior, gen_uml3_0_0_Vertex_NamedElement, gen_uml3_0_0_Transition_Namespace, gen_uml3_0_0_Transition_RedefinableElement, gen_uml3_0_0_Trigger_NamedElement, gen_uml3_0_0_Event_PackageableElement, gen_uml3_0_0_Port_Property, gen_uml3_0_0_State_Namespace, gen_uml3_0_0_State_RedefinableElement, gen_uml3_0_0_State_Vertex, gen_uml3_0_0_ConnectionPointReference_Vertex, gen_uml3_0_0_Pseudostate_Vertex, gen_uml3_0_0_ProtocolConformance_DirectedRelationship, gen_uml3_0_0_StructuredClassifier_Classifier, gen_uml3_0_0_Connector_Feature, gen_uml3_0_0_Extension_Association, gen_uml3_0_0_EncapsulatedClassifier_StructuredClassifier, gen_uml3_0_0_Image_Element, gen_uml3_0_0_Profile_Package, gen_uml3_0_0_Model_Package, gen_uml3_0_0_ParameterSet_NamedElement, gen_uml3_0_0_DataType_Classifier, gen_uml3_0_0_ExtensionEnd_Property, gen_uml3_0_0_Stereotype_Class, gen_uml3_0_0_ConnectableElementTemplateParameter_TemplateParameter, gen_uml3_0_0_CollaborationUse_NamedElement, gen_uml3_0_0_Collaboration_BehavioredClassifier, gen_uml3_0_0_Collaboration_StructuredClassifier, gen_uml3_0_0_UseCase_BehavioredClassifier, gen_uml3_0_0_OperationTemplateParameter_TemplateParameter, gen_uml3_0_0_StructuralFeature_Feature, gen_uml3_0_0_StructuralFeature_TypedElement, gen_uml3_0_0_StructuralFeature_MultiplicityElement, gen_uml3_0_0_Extend_NamedElement, gen_uml3_0_0_Extend_DirectedRelationship, gen_uml3_0_0_ExtensionPoint_RedefinableElement, gen_uml3_0_0_RedefinableTemplateSignature_RedefinableElement, gen_uml3_0_0_RedefinableTemplateSignature_TemplateSignature, gen_uml3_0_0_ClassifierTemplateParameter_TemplateParameter, gen_uml3_0_0_Include_NamedElement, gen_uml3_0_0_Include_DirectedRelationship, gen_uml3_0_0_Expression_ValueSpecification, gen_uml3_0_0_Usage_Dependency, gen_uml3_0_0_PackageMerge_DirectedRelationship, gen_uml3_0_0_ProfileApplication_DirectedRelationship, gen_uml3_0_0_Enumeration_DataType, gen_uml3_0_0_EnumerationLiteral_InstanceSpecification, gen_uml3_0_0_InstanceSpecification_DeploymentTarget, gen_uml3_0_0_StringExpression_Expression, gen_uml3_0_0_StringExpression_TemplateableElement, gen_uml3_0_0_Slot_Element, gen_uml3_0_0_PrimitiveType_DataType, gen_uml3_0_0_LiteralSpecification_ValueSpecification, gen_uml3_0_0_LiteralInteger_LiteralSpecification, gen_uml3_0_0_LiteralString_LiteralSpecification, gen_uml3_0_0_LiteralBoolean_LiteralSpecification, gen_uml3_0_0_LiteralNull_LiteralSpecification, gen_uml3_0_0_InstanceValue_ValueSpecification, gen_uml3_0_0_InstanceSpecification_PackageableElement, gen_uml3_0_0_InstanceSpecification_DeployedArtifact, gen_uml3_0_0_OpaqueBehavior_Behavior, gen_uml3_0_0_FunctionBehavior_OpaqueBehavior, gen_uml3_0_0_OpaqueAction_Action, gen_uml3_0_0_Action_ExecutableNode, gen_uml3_0_0_ExecutableNode_ActivityNode, gen_uml3_0_0_LiteralUnlimitedNatural_LiteralSpecification, gen_uml3_0_0_StructuredActivityNode_Action, gen_uml3_0_0_StructuredActivityNode_Namespace, gen_uml3_0_0_StructuredActivityNode_ActivityGroup, gen_uml3_0_0_ActivityGroup_Element, gen_uml3_0_0_ActivityNode_RedefinableElement, gen_uml3_0_0_Activity_Behavior, gen_uml3_0_0_Variable_ConnectableElement, gen_uml3_0_0_Variable_MultiplicityElement, gen_uml3_0_0_ActivityPartition_NamedElement, gen_uml3_0_0_ActivityPartition_ActivityGroup, gen_uml3_0_0_ActivityEdge_RedefinableElement, gen_uml3_0_0_InterruptibleActivityRegion_ActivityGroup, gen_uml3_0_0_ExceptionHandler_Element, gen_uml3_0_0_ObjectNode_ActivityNode, gen_uml3_0_0_ObjectNode_TypedElement, gen_uml3_0_0_OutputPin_Pin, gen_uml3_0_0_Pin_ObjectNode, gen_uml3_0_0_Pin_MultiplicityElement, gen_uml3_0_0_InputPin_Pin, gen_uml3_0_0_CallAction_InvocationAction, gen_uml3_0_0_InvocationAction_Action, gen_uml3_0_0_SendSignalAction_InvocationAction, gen_uml3_0_0_CallOperationAction_CallAction, gen_uml3_0_0_CallBehaviorAction_CallAction, gen_uml3_0_0_ControlNode_ActivityNode, gen_uml3_0_0_ControlFlow_ActivityEdge, gen_uml3_0_0_InitialNode_ControlNode, gen_uml3_0_0_ActivityParameterNode_ObjectNode, gen_uml3_0_0_ValuePin_InputPin, gen_uml3_0_0_Message_NamedElement, gen_uml3_0_0_SequenceNode_StructuredActivityNode, gen_uml3_0_0_MessageEnd_NamedElement, gen_uml3_0_0_Interaction_Behavior, gen_uml3_0_0_Interaction_InteractionFragment, gen_uml3_0_0_InteractionFragment_NamedElement, gen_uml3_0_0_Lifeline_NamedElement, gen_uml3_0_0_PartDecomposition_InteractionUse, gen_uml3_0_0_InteractionUse_InteractionFragment, gen_uml3_0_0_Gate_MessageEnd, gen_uml3_0_0_GeneralOrdering_NamedElement, gen_uml3_0_0_OccurrenceSpecification_InteractionFragment, gen_uml3_0_0_InteractionOperand_Namespace, gen_uml3_0_0_InteractionOperand_InteractionFragment, gen_uml3_0_0_InteractionConstraint_Constraint, gen_uml3_0_0_ExecutionSpecification_InteractionFragment, gen_uml3_0_0_StateInvariant_InteractionFragment, gen_uml3_0_0_ActionExecutionSpecification_ExecutionSpecification, gen_uml3_0_0_BehaviorExecutionSpecification_ExecutionSpecification, gen_uml3_0_0_ExecutionEvent_Event, gen_uml3_0_0_CreationEvent_Event, gen_uml3_0_0_DestructionEvent_Event, gen_uml3_0_0_SendOperationEvent_MessageEvent, gen_uml3_0_0_MessageEvent_Event, gen_uml3_0_0_SendSignalEvent_MessageEvent, gen_uml3_0_0_MessageOccurrenceSpecification_OccurrenceSpecification, gen_uml3_0_0_MessageOccurrenceSpecification_MessageEnd, gen_uml3_0_0_ExecutionOccurrenceSpecification_OccurrenceSpecification, gen_uml3_0_0_ReceiveOperationEvent_MessageEvent, gen_uml3_0_0_ReceiveSignalEvent_MessageEvent, gen_uml3_0_0_Actor_BehavioredClassifier, gen_uml3_0_0_CallEvent_MessageEvent, gen_uml3_0_0_SignalEvent_MessageEvent, gen_uml3_0_0_AnyReceiveEvent_MessageEvent, gen_uml3_0_0_ForkNode_ControlNode, gen_uml3_0_0_FlowFinalNode_FinalNode, gen_uml3_0_0_FinalNode_ControlNode, gen_uml3_0_0_CentralBufferNode_ObjectNode, gen_uml3_0_0_MergeNode_ControlNode, gen_uml3_0_0_DecisionNode_ControlNode, gen_uml3_0_0_ObjectFlow_ActivityEdge, gen_uml3_0_0_ChangeEvent_Event, gen_uml3_0_0_ActivityFinalNode_FinalNode, gen_uml3_0_0_ComponentRealization_Realization, gen_uml3_0_0_Component_Class, gen_uml3_0_0_Node_Class, gen_uml3_0_0_Node_DeploymentTarget, gen_uml3_0_0_CommunicationPath_Association, gen_uml3_0_0_Device_Node, gen_uml3_0_0_ExecutionEnvironment_Node, gen_uml3_0_0_CombinedFragment_InteractionFragment, gen_uml3_0_0_Continuation_InteractionFragment, gen_uml3_0_0_ConsiderIgnoreFragment_CombinedFragment, gen_uml3_0_0_CreateObjectAction_Action, gen_uml3_0_0_DestroyObjectAction_Action, gen_uml3_0_0_TestIdentityAction_Action, gen_uml3_0_0_ReadSelfAction_Action, gen_uml3_0_0_StructuralFeatureAction_Action, gen_uml3_0_0_ReadStructuralFeatureAction_StructuralFeatureAction, gen_uml3_0_0_WriteStructuralFeatureAction_StructuralFeatureAction, gen_uml3_0_0_ClearStructuralFeatureAction_StructuralFeatureAction, gen_uml3_0_0_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_uml3_0_0_LinkAction_Action, gen_uml3_0_0_LinkEndData_Element, gen_uml3_0_0_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_uml3_0_0_QualifierValue_Element, gen_uml3_0_0_ReadLinkAction_LinkAction, gen_uml3_0_0_LinkEndCreationData_LinkEndData, gen_uml3_0_0_CreateLinkAction_WriteLinkAction, gen_uml3_0_0_WriteLinkAction_LinkAction, gen_uml3_0_0_DestroyLinkAction_WriteLinkAction, gen_uml3_0_0_LinkEndDestructionData_LinkEndData, gen_uml3_0_0_ClearAssociationAction_Action, gen_uml3_0_0_BroadcastSignalAction_InvocationAction, gen_uml3_0_0_SendObjectAction_InvocationAction, gen_uml3_0_0_ValueSpecificationAction_Action, gen_uml3_0_0_TimeExpression_ValueSpecification, gen_uml3_0_0_Observation_PackageableElement, gen_uml3_0_0_Duration_ValueSpecification, gen_uml3_0_0_DurationInterval_Interval, gen_uml3_0_0_Interval_ValueSpecification, gen_uml3_0_0_TimeConstraint_IntervalConstraint, gen_uml3_0_0_IntervalConstraint_Constraint, gen_uml3_0_0_TimeInterval_Interval, gen_uml3_0_0_DurationConstraint_IntervalConstraint, gen_uml3_0_0_TimeObservation_Observation, gen_uml3_0_0_DurationObservation_Observation, gen_uml3_0_0_FinalState_State, gen_uml3_0_0_TimeEvent_Event, gen_uml3_0_0_VariableAction_Action, gen_uml3_0_0_WriteVariableAction_VariableAction, gen_uml3_0_0_ClearVariableAction_VariableAction, gen_uml3_0_0_AddVariableValueAction_WriteVariableAction, gen_uml3_0_0_RemoveVariableValueAction_WriteVariableAction, gen_uml3_0_0_RaiseExceptionAction_Action, gen_uml3_0_0_ActionInputPin_InputPin, gen_uml3_0_0_InformationItem_Classifier, gen_uml3_0_0_ReadVariableAction_VariableAction, gen_uml3_0_0_ReadExtentAction_Action, gen_uml3_0_0_ReclassifyObjectAction_Action, gen_uml3_0_0_InformationFlow_PackageableElement, gen_uml3_0_0_InformationFlow_DirectedRelationship, gen_uml3_0_0_ReadIsClassifiedObjectAction_Action, gen_uml3_0_0_StartClassifierBehaviorAction_Action, gen_uml3_0_0_ReadLinkObjectEndAction_Action, gen_uml3_0_0_ReadLinkObjectEndQualifierAction_Action, gen_uml3_0_0_CreateLinkObjectAction_CreateLinkAction, gen_uml3_0_0_AcceptEventAction_Action, gen_uml3_0_0_AcceptCallAction_AcceptEventAction, gen_uml3_0_0_ReplyAction_Action, gen_uml3_0_0_UnmarshallAction_Action, gen_uml3_0_0_ReduceAction_Action, gen_uml3_0_0_StartObjectBehaviorAction_CallAction, gen_uml3_0_0_JoinNode_ControlNode, gen_uml3_0_0_DataStoreNode_CentralBufferNode, gen_uml3_0_0_ConditionalNode_StructuredActivityNode, gen_uml3_0_0_Clause_Element, gen_uml3_0_0_ExpansionNode_ObjectNode, gen_uml3_0_0_ExpansionRegion_StructuredActivityNode, gen_uml3_0_0_LoopNode_StructuredActivityNode, gen_uml3_0_0_ProtocolTransition_Transition, gen_uml3_0_0_AssociationClass_Class, gen_uml3_0_0_AssociationClass_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)