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

MessageSort: Enumeration = Enumeration(
    name="MessageSort",
    literals={
            EnumerationLiteral(name="synchSignal"),
			EnumerationLiteral(name="synchCall"),
			EnumerationLiteral(name="asynchCall"),
			EnumerationLiteral(name="asynchSignal")
    }
)

MessageKind: Enumeration = Enumeration(
    name="MessageKind",
    literals={
            EnumerationLiteral(name="unknown"),
			EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="found"),
			EnumerationLiteral(name="lost")
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

InteractionOperator: Enumeration = Enumeration(
    name="InteractionOperator",
    literals={
            EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="alt"),
			EnumerationLiteral(name="break"),
			EnumerationLiteral(name="assert"),
			EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="seq"),
			EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="neg"),
			EnumerationLiteral(name="critical"),
			EnumerationLiteral(name="consider"),
			EnumerationLiteral(name="par"),
			EnumerationLiteral(name="opt")
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
            EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="deepHistory")
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

ConnectorKind: Enumeration = Enumeration(
    name="ConnectorKind",
    literals={
            EnumerationLiteral(name="delegation"),
			EnumerationLiteral(name="assembly")
    }
)

# Classes
UML2_Element = Class(name="UML2::Element", is_abstract=True)
UML2_Comment = Class(name="UML2::Comment")
UML2_MultiplicityElement = Class(name="UML2::MultiplicityElement", is_abstract=True)
Element = Class(name="Element")
UML2_ValueSpecification = Class(name="UML2::ValueSpecification", is_abstract=True)
UML2_NamedElement = Class(name="UML2::NamedElement", is_abstract=True)
TemplateableElement = Class(name="TemplateableElement")
UML2_Dependency = Class(name="UML2::Dependency")
UML2_StringExpression = Class(name="UML2::StringExpression")
UML2_Namespace = Class(name="UML2::Namespace", is_abstract=True)
NamedElement = Class(name="NamedElement")
UML2_Constraint = Class(name="UML2::Constraint")
UML2_PackageableElement = Class(name="UML2::PackageableElement", is_abstract=True)
UML2_ElementImport = Class(name="UML2::ElementImport")
UML2_PackageImport = Class(name="UML2::PackageImport")
UML2_OpaqueExpression = Class(name="UML2::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
UML2_Parameter = Class(name="UML2::Parameter")
UML2_Behavior = Class(name="UML2::Behavior", is_abstract=True)
TypedElement = Class(name="TypedElement")
ParameterableElement = Class(name="ParameterableElement")
UML2_Expression = Class(name="UML2::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2_DirectedRelationship = Class(name="UML2::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
UML2_Relationship = Class(name="UML2::Relationship", is_abstract=True)
UML2_Class = Class(name="UML2::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2_Operation = Class(name="UML2::Operation")
UML2_Extension = Class(name="UML2::Extension")
UML2_Classifier = Class(name="UML2::Classifier", is_abstract=True)
UML2_Reception = Class(name="UML2::Reception")
UML2_Type = Class(name="UML2::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
UML2_Package = Class(name="UML2::Package")
UML2_Property = Class(name="UML2::Property")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
UML2_Association = Class(name="UML2::Association")
UML2_DataType = Class(name="UML2::DataType")
BehavioralFeature = Class(name="BehavioralFeature")
MultiplicityElement = Class(name="MultiplicityElement")
UML2_TypedElement = Class(name="UML2::TypedElement", is_abstract=True)
UML2_ParameterSet = Class(name="UML2::ParameterSet")
Namespace = Class(name="Namespace")
UML2_PackageMerge = Class(name="UML2::PackageMerge")
UML2_ProfileApplication = Class(name="UML2::ProfileApplication")
UML2_Enumeration = Class(name="UML2::Enumeration")
DataType = Class(name="DataType")
UML2_EnumerationLiteral = Class(name="UML2::EnumerationLiteral")
Classifier = Class(name="Classifier")
UML2_CollaborationOccurrence = Class(name="UML2::CollaborationOccurrence")
InstanceSpecification = Class(name="InstanceSpecification")
UML2_PrimitiveType = Class(name="UML2::PrimitiveType")
Type = Class(name="Type")
RedefinableElement = Class(name="RedefinableElement")
UML2_Feature = Class(name="UML2::Feature", is_abstract=True)
UML2_Generalization = Class(name="UML2::Generalization")
UML2_Substitution = Class(name="UML2::Substitution")
UML2_GeneralizationSet = Class(name="UML2::GeneralizationSet")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_LiteralBoolean = Class(name="UML2::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
UML2_LiteralSpecification = Class(name="UML2::LiteralSpecification", is_abstract=True)
UML2_LiteralString = Class(name="UML2::LiteralString")
UML2_LiteralNull = Class(name="UML2::LiteralNull")
UML2_LiteralInteger = Class(name="UML2::LiteralInteger")
UML2_LiteralUnlimitedNatural = Class(name="UML2::LiteralUnlimitedNatural")
UML2_BehavioralFeature = Class(name="UML2::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
UML2_StructuralFeature = Class(name="UML2::StructuralFeature", is_abstract=True)
UML2_InstanceSpecification = Class(name="UML2::InstanceSpecification")
DeployedArtifact = Class(name="DeployedArtifact")
UML2_Slot = Class(name="UML2::Slot")
DirectedRelationship = Class(name="DirectedRelationship")
UML2_InstanceValue = Class(name="UML2::InstanceValue")
UML2_RedefinableElement = Class(name="UML2::RedefinableElement", is_abstract=True)
UML2_Stereotype = Class(name="UML2::Stereotype")
Class_ = Class(name="Class")
UML2_Profile = Class(name="UML2::Profile")
Package = Class(name="Package")
PackageImport = Class(name="PackageImport")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier", is_abstract=True)
Association = Class(name="Association")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_Activity = Class(name="UML2::Activity")
Behavior = Class(name="Behavior")
UML2_ActivityEdge = Class(name="UML2::ActivityEdge", is_abstract=True)
UML2_ActivityGroup = Class(name="UML2::ActivityGroup", is_abstract=True)
UML2_ActivityNode = Class(name="UML2::ActivityNode", is_abstract=True)
UML2_Action = Class(name="UML2::Action")
UML2_StructuredActivityNode = Class(name="UML2::StructuredActivityNode")
UML2_Permission = Class(name="UML2::Permission")
Dependency = Class(name="Dependency")
UML2_Implementation = Class(name="UML2::Implementation")
UML2_Trigger = Class(name="UML2::Trigger", is_abstract=True)
UML2_StateMachine = Class(name="UML2::StateMachine")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_InformationItem = Class(name="UML2::InformationItem")
UML2_InformationFlow = Class(name="UML2::InformationFlow")
UML2_Usage = Class(name="UML2::Usage")
UML2_Abstraction = Class(name="UML2::Abstraction")
UML2_Realization = Class(name="UML2::Realization")
Abstraction = Class(name="Abstraction")
UML2_Component = Class(name="UML2::Component")
Realization = Class(name="Realization")
UML2_Connector = Class(name="UML2::Connector")
UML2_StructuredClassifier = Class(name="UML2::StructuredClassifier", is_abstract=True)
UML2_Model = Class(name="UML2::Model")
UML2_ConnectorEnd = Class(name="UML2::ConnectorEnd")
UML2_ConnectableElement = Class(name="UML2::ConnectableElement", is_abstract=True)
UML2_ActivityPartition = Class(name="UML2::ActivityPartition")
UML2_InterruptibleActivityRegion = Class(name="UML2::InterruptibleActivityRegion")
ExecutableNode = Class(name="ExecutableNode")
UML2_OutputPin = Class(name="UML2::OutputPin")
UML2_InputPin = Class(name="UML2::InputPin")
UML2_ControlNode = Class(name="UML2::ControlNode", is_abstract=True)
UML2_ControlFlow = Class(name="UML2::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
UML2_ObjectFlow = Class(name="UML2::ObjectFlow")
UML2_InitialNode = Class(name="UML2::InitialNode")
ControlNode = Class(name="ControlNode")
UML2_FinalNode = Class(name="UML2::FinalNode", is_abstract=True)
UML2_ActivityFinalNode = Class(name="UML2::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
UML2_DecisionNode = Class(name="UML2::DecisionNode")
UML2_MergeNode = Class(name="UML2::MergeNode")
UML2_ExecutableNode = Class(name="UML2::ExecutableNode", is_abstract=True)
UML2_ExceptionHandler = Class(name="UML2::ExceptionHandler")
Pin = Class(name="Pin")
UML2_Pin = Class(name="UML2::Pin", is_abstract=True)
ObjectNode = Class(name="ObjectNode")
UML2_ObjectNode = Class(name="UML2::ObjectNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
UML2_State = Class(name="UML2::State")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
UML2_Artifact = Class(name="UML2::Artifact")
UML2_Manifestation = Class(name="UML2::Manifestation")
UML2_ActivityParameterNode = Class(name="UML2::ActivityParameterNode")
UML2_ValuePin = Class(name="UML2::ValuePin")
InputPin = Class(name="InputPin")
UML2_Interface = Class(name="UML2::Interface")
UML2_Actor = Class(name="UML2::Actor")
UML2_Extend = Class(name="UML2::Extend")
UML2_ExtensionPoint = Class(name="UML2::ExtensionPoint")
UML2_Include = Class(name="UML2::Include")
StructuredClassifier = Class(name="StructuredClassifier")
UML2_Port = Class(name="UML2::Port")
UML2_EncapsulatedClassifier = Class(name="UML2::EncapsulatedClassifier", is_abstract=True)
UML2_CallTrigger = Class(name="UML2::CallTrigger")
MessageTrigger = Class(name="MessageTrigger")
UML2_MessageTrigger = Class(name="UML2::MessageTrigger", is_abstract=True)
Trigger = Class(name="Trigger")
UML2_Collaboration = Class(name="UML2::Collaboration")
UML2_Signal = Class(name="UML2::Signal")
UML2_SignalTrigger = Class(name="UML2::SignalTrigger")
UML2_TimeTrigger = Class(name="UML2::TimeTrigger")
UML2_AnyTrigger = Class(name="UML2::AnyTrigger")
UML2_Variable = Class(name="UML2::Variable")
Action = Class(name="Action")
ActivityGroup = Class(name="ActivityGroup")
UML2_ChangeTrigger = Class(name="UML2::ChangeTrigger")
UML2_Clause = Class(name="UML2::Clause")
UML2_LoopNode = Class(name="UML2::LoopNode")
UML2_ConditionalNode = Class(name="UML2::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
UML2_Interaction = Class(name="UML2::Interaction")
InteractionFragment = Class(name="InteractionFragment")
UML2_Lifeline = Class(name="UML2::Lifeline")
UML2_Message = Class(name="UML2::Message")
UML2_InteractionFragment = Class(name="UML2::InteractionFragment", is_abstract=True)
UML2_Gate = Class(name="UML2::Gate")
UML2_GeneralOrdering = Class(name="UML2::GeneralOrdering")
UML2_InteractionOperand = Class(name="UML2::InteractionOperand")
UML2_PartDecomposition = Class(name="UML2::PartDecomposition")
UML2_MessageEnd = Class(name="UML2::MessageEnd", is_abstract=True)
MessageEnd = Class(name="MessageEnd")
UML2_ExecutionOccurrence = Class(name="UML2::ExecutionOccurrence")
UML2_EventOccurrence = Class(name="UML2::EventOccurrence")
UML2_StateInvariant = Class(name="UML2::StateInvariant")
UML2_TemplateableElement = Class(name="UML2::TemplateableElement", is_abstract=True)
UML2_ParameterableElement = Class(name="UML2::ParameterableElement", is_abstract=True)
UML2_Stop = Class(name="UML2::Stop")
EventOccurrence = Class(name="EventOccurrence")
UML2_TemplateSignature = Class(name="UML2::TemplateSignature")
UML2_TemplateParameter = Class(name="UML2::TemplateParameter")
UML2_TemplateBinding = Class(name="UML2::TemplateBinding")
UML2_TemplateParameterSubstitution = Class(name="UML2::TemplateParameterSubstitution")
UML2_OperationTemplateParameter = Class(name="UML2::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
UML2_ClassifierTemplateParameter = Class(name="UML2::ClassifierTemplateParameter")
UML2_ParameterableClassifier = Class(name="UML2::ParameterableClassifier", is_abstract=True)
UML2_RedefinableTemplateSignature = Class(name="UML2::RedefinableTemplateSignature")
TemplateSignature = Class(name="TemplateSignature")
UML2_TemplateableClassifier = Class(name="UML2::TemplateableClassifier", is_abstract=True)
UML2_ConnectableElementTemplateParameter = Class(name="UML2::ConnectableElementTemplateParameter")
UML2_ForkNode = Class(name="UML2::ForkNode")
UML2_JoinNode = Class(name="UML2::JoinNode")
UML2_FlowFinalNode = Class(name="UML2::FlowFinalNode")
UML2_CentralBufferNode = Class(name="UML2::CentralBufferNode")
UML2_ExpansionNode = Class(name="UML2::ExpansionNode")
UML2_ExpansionRegion = Class(name="UML2::ExpansionRegion")
UML2_InteractionOccurrence = Class(name="UML2::InteractionOccurrence")
InteractionOccurrence = Class(name="InteractionOccurrence")
UML2_InteractionConstraint = Class(name="UML2::InteractionConstraint")
UML2_CombinedFragment = Class(name="UML2::CombinedFragment")
UML2_Continuation = Class(name="UML2::Continuation")
UML2_Region = Class(name="UML2::Region")
UML2_Pseudostate = Class(name="UML2::Pseudostate")
Constraint = Class(name="Constraint")
Vertex = Class(name="Vertex")
UML2_ConnectionPointReference = Class(name="UML2::ConnectionPointReference")
UML2_Vertex = Class(name="UML2::Vertex", is_abstract=True)
UML2_Transition = Class(name="UML2::Transition")
UML2_FinalState = Class(name="UML2::FinalState")
State = Class(name="State")
UML2_CreateObjectAction = Class(name="UML2::CreateObjectAction")
UML2_DestroyObjectAction = Class(name="UML2::DestroyObjectAction")
UML2_TestIdentityAction = Class(name="UML2::TestIdentityAction")
UML2_ReadSelfAction = Class(name="UML2::ReadSelfAction")
UML2_StructuralFeatureAction = Class(name="UML2::StructuralFeatureAction", is_abstract=True)
UML2_ReadStructuralFeatureAction = Class(name="UML2::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UML2_WriteStructuralFeatureAction = Class(name="UML2::WriteStructuralFeatureAction", is_abstract=True)
UML2_ClearStructuralFeatureAction = Class(name="UML2::ClearStructuralFeatureAction")
UML2_RemoveStructuralFeatureValueAction = Class(name="UML2::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UML2_AddStructuralFeatureValueAction = Class(name="UML2::AddStructuralFeatureValueAction")
UML2_QualifierValue = Class(name="UML2::QualifierValue")
UML2_ReadLinkAction = Class(name="UML2::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UML2_LinkEndCreationData = Class(name="UML2::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UML2_CreateLinkAction = Class(name="UML2::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UML2_WriteLinkAction = Class(name="UML2::WriteLinkAction", is_abstract=True)
UML2_DestroyLinkAction = Class(name="UML2::DestroyLinkAction")
UML2_ClearAssociationAction = Class(name="UML2::ClearAssociationAction")
UML2_VariableAction = Class(name="UML2::VariableAction", is_abstract=True)
UML2_LinkAction = Class(name="UML2::LinkAction", is_abstract=True)
UML2_LinkEndData = Class(name="UML2::LinkEndData")
UML2_RemoveVariableValueAction = Class(name="UML2::RemoveVariableValueAction")
UML2_ApplyFunctionAction = Class(name="UML2::ApplyFunctionAction")
UML2_PrimitiveFunction = Class(name="UML2::PrimitiveFunction")
UML2_CallAction = Class(name="UML2::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
UML2_InvocationAction = Class(name="UML2::InvocationAction", is_abstract=True)
UML2_ReadVariableAction = Class(name="UML2::ReadVariableAction")
VariableAction = Class(name="VariableAction")
UML2_WriteVariableAction = Class(name="UML2::WriteVariableAction", is_abstract=True)
UML2_ClearVariableAction = Class(name="UML2::ClearVariableAction")
UML2_AddVariableValueAction = Class(name="UML2::AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UML2_SendObjectAction = Class(name="UML2::SendObjectAction")
UML2_CallOperationAction = Class(name="UML2::CallOperationAction")
CallAction = Class(name="CallAction")
UML2_CallBehaviorAction = Class(name="UML2::CallBehaviorAction")
UML2_TimeExpression = Class(name="UML2::TimeExpression")
UML2_Duration = Class(name="UML2::Duration")
UML2_SendSignalAction = Class(name="UML2::SendSignalAction")
UML2_BroadcastSignalAction = Class(name="UML2::BroadcastSignalAction")
UML2_IntervalConstraint = Class(name="UML2::IntervalConstraint")
UML2_TimeInterval = Class(name="UML2::TimeInterval")
UML2_DurationObservationAction = Class(name="UML2::DurationObservationAction")
UML2_DurationConstraint = Class(name="UML2::DurationConstraint")
UML2_DataStoreNode = Class(name="UML2::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2_TimeObservationAction = Class(name="UML2::TimeObservationAction")
UML2_DurationInterval = Class(name="UML2::DurationInterval")
Interval = Class(name="Interval")
UML2_Interval = Class(name="UML2::Interval")
UML2_TimeConstraint = Class(name="UML2::TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
UML2_Deployment = Class(name="UML2::Deployment")
UML2_DeployedArtifact = Class(name="UML2::DeployedArtifact", is_abstract=True)
UML2_DeploymentTarget = Class(name="UML2::DeploymentTarget", is_abstract=True)
UML2_DeploymentSpecification = Class(name="UML2::DeploymentSpecification")
UML2_Node = Class(name="UML2::Node")
UML2_ProtocolTransition = Class(name="UML2::ProtocolTransition")
Transition = Class(name="Transition")
UML2_ReadExtentAction = Class(name="UML2::ReadExtentAction")
UML2_ReclassifyObjectAction = Class(name="UML2::ReclassifyObjectAction")
UML2_Device = Class(name="UML2::Device")
Node = Class(name="Node")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
UML2_ProtocolConformance = Class(name="UML2::ProtocolConformance")
StateMachine = Class(name="StateMachine")
UML2_StartOwnedBehaviorAction = Class(name="UML2::StartOwnedBehaviorAction")
UML2_ReadLinkObjectEndAction = Class(name="UML2::ReadLinkObjectEndAction")
UML2_ReadLinkObjectEndQualifierAction = Class(name="UML2::ReadLinkObjectEndQualifierAction")
UML2_ReadIsClassifiedObjectAction = Class(name="UML2::ReadIsClassifiedObjectAction")
UML2_AcceptCallAction = Class(name="UML2::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UML2_ReplyAction = Class(name="UML2::ReplyAction")
UML2_RaiseExceptionAction = Class(name="UML2::RaiseExceptionAction")
Artifact = Class(name="Artifact")
UML2_CreateLinkObjectAction = Class(name="UML2::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UML2_AcceptEventAction = Class(name="UML2::AcceptEventAction")

# UML2_Element class attributes and methods

# UML2_Comment class attributes and methods
UML2_Comment_body: Property = Property(name="body", type=StringType)
UML2_Comment.attributes={UML2_Comment_body}

# UML2_MultiplicityElement class attributes and methods
UML2_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
UML2_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
UML2_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
UML2_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
UML2_MultiplicityElement.attributes={UML2_MultiplicityElement_isUnique, UML2_MultiplicityElement_isOrdered, UML2_MultiplicityElement_upper, UML2_MultiplicityElement_lower}

# Element class attributes and methods

# UML2_ValueSpecification class attributes and methods

# UML2_NamedElement class attributes and methods
UML2_NamedElement_name: Property = Property(name="name", type=StringType)
UML2_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
UML2_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
UML2_NamedElement.attributes={UML2_NamedElement_visibility, UML2_NamedElement_name, UML2_NamedElement_qualifiedName}

# TemplateableElement class attributes and methods

# UML2_Dependency class attributes and methods

# UML2_StringExpression class attributes and methods

# UML2_Namespace class attributes and methods

# NamedElement class attributes and methods

# UML2_Constraint class attributes and methods

# UML2_PackageableElement class attributes and methods
UML2_PackageableElement_packageableElement_visibility: Property = Property(name="packageableElement_visibility", type=StringType)
UML2_PackageableElement.attributes={UML2_PackageableElement_packageableElement_visibility}

# UML2_ElementImport class attributes and methods
UML2_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
UML2_ElementImport_alias: Property = Property(name="alias", type=StringType)
UML2_ElementImport.attributes={UML2_ElementImport_visibility, UML2_ElementImport_alias}

# UML2_PackageImport class attributes and methods
UML2_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
UML2_PackageImport.attributes={UML2_PackageImport_visibility}

# UML2_OpaqueExpression class attributes and methods
UML2_OpaqueExpression_bodies: Property = Property(name="bodies", type=StringType)
UML2_OpaqueExpression_language: Property = Property(name="language", type=StringType)
UML2_OpaqueExpression.attributes={UML2_OpaqueExpression_language, UML2_OpaqueExpression_bodies}

# ValueSpecification class attributes and methods

# UML2_Parameter class attributes and methods
UML2_Parameter_default: Property = Property(name="default", type=StringType)
UML2_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2_Parameter_isException: Property = Property(name="isException", type=BooleanType)
UML2_Parameter_isStream: Property = Property(name="isStream", type=BooleanType)
UML2_Parameter_effect: Property = Property(name="effect", type=StringType)
UML2_Parameter.attributes={UML2_Parameter_direction, UML2_Parameter_isException, UML2_Parameter_default, UML2_Parameter_effect, UML2_Parameter_isStream}

# UML2_Behavior class attributes and methods
UML2_Behavior_isReentrant: Property = Property(name="isReentrant", type=BooleanType)
UML2_Behavior.attributes={UML2_Behavior_isReentrant}

# TypedElement class attributes and methods

# ParameterableElement class attributes and methods

# UML2_Expression class attributes and methods
UML2_Expression_symbol: Property = Property(name="symbol", type=StringType)
UML2_Expression.attributes={UML2_Expression_symbol}

# OpaqueExpression class attributes and methods

# UML2_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# UML2_Relationship class attributes and methods

# UML2_Class class attributes and methods
UML2_Class_isActive: Property = Property(name="isActive", type=BooleanType)
UML2_Class.attributes={UML2_Class_isActive}

# BehavioredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2_Operation class attributes and methods
UML2_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
UML2_Operation.attributes={UML2_Operation_isQuery}

# UML2_Extension class attributes and methods
UML2_Extension_isRequired: Property = Property(name="isRequired", type=BooleanType)
UML2_Extension.attributes={UML2_Extension_isRequired}

# UML2_Classifier class attributes and methods
UML2_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2_Classifier.attributes={UML2_Classifier_isAbstract}

# UML2_Reception class attributes and methods

# UML2_Type class attributes and methods

# PackageableElement class attributes and methods

# UML2_Package class attributes and methods

# UML2_Property class attributes and methods
UML2_Property_default: Property = Property(name="default", type=StringType)
UML2_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
UML2_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UML2_Property.attributes={UML2_Property_isComposite, UML2_Property_aggregation, UML2_Property_default, UML2_Property_isDerivedUnion, UML2_Property_isDerived}

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# UML2_Association class attributes and methods
UML2_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2_Association.attributes={UML2_Association_isDerived}

# UML2_DataType class attributes and methods

# BehavioralFeature class attributes and methods

# MultiplicityElement class attributes and methods

# UML2_TypedElement class attributes and methods

# UML2_ParameterSet class attributes and methods

# Namespace class attributes and methods

# UML2_PackageMerge class attributes and methods

# UML2_ProfileApplication class attributes and methods

# UML2_Enumeration class attributes and methods

# DataType class attributes and methods

# UML2_EnumerationLiteral class attributes and methods

# Classifier class attributes and methods

# UML2_CollaborationOccurrence class attributes and methods

# InstanceSpecification class attributes and methods

# UML2_PrimitiveType class attributes and methods

# Type class attributes and methods

# RedefinableElement class attributes and methods

# UML2_Feature class attributes and methods
UML2_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
UML2_Feature.attributes={UML2_Feature_isStatic}

# UML2_Generalization class attributes and methods
UML2_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
UML2_Generalization.attributes={UML2_Generalization_isSubstitutable}

# UML2_Substitution class attributes and methods

# UML2_GeneralizationSet class attributes and methods
UML2_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
UML2_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
UML2_GeneralizationSet.attributes={UML2_GeneralizationSet_isDisjoint, UML2_GeneralizationSet_isCovering}

# UML2_UseCase class attributes and methods

# UML2_LiteralBoolean class attributes and methods
UML2_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
UML2_LiteralBoolean.attributes={UML2_LiteralBoolean_value}

# LiteralSpecification class attributes and methods

# UML2_LiteralSpecification class attributes and methods

# UML2_LiteralString class attributes and methods
UML2_LiteralString_value: Property = Property(name="value", type=StringType)
UML2_LiteralString.attributes={UML2_LiteralString_value}

# UML2_LiteralNull class attributes and methods

# UML2_LiteralInteger class attributes and methods
UML2_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
UML2_LiteralInteger.attributes={UML2_LiteralInteger_value}

# UML2_LiteralUnlimitedNatural class attributes and methods
UML2_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
UML2_LiteralUnlimitedNatural.attributes={UML2_LiteralUnlimitedNatural_value}

# UML2_BehavioralFeature class attributes and methods
UML2_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
UML2_BehavioralFeature.attributes={UML2_BehavioralFeature_concurrency, UML2_BehavioralFeature_isAbstract}

# Feature class attributes and methods

# UML2_StructuralFeature class attributes and methods
UML2_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
UML2_StructuralFeature.attributes={UML2_StructuralFeature_isReadOnly}

# UML2_InstanceSpecification class attributes and methods

# DeployedArtifact class attributes and methods

# UML2_Slot class attributes and methods

# DirectedRelationship class attributes and methods

# UML2_InstanceValue class attributes and methods

# UML2_RedefinableElement class attributes and methods
UML2_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
UML2_RedefinableElement.attributes={UML2_RedefinableElement_isLeaf}

# UML2_Stereotype class attributes and methods

# Class class attributes and methods

# UML2_Profile class attributes and methods

# Package class attributes and methods

# PackageImport class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# Association class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_Activity class attributes and methods
UML2_Activity_body: Property = Property(name="body", type=StringType)
UML2_Activity_language: Property = Property(name="language", type=StringType)
UML2_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
UML2_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
UML2_Activity.attributes={UML2_Activity_language, UML2_Activity_isReadOnly, UML2_Activity_body, UML2_Activity_isSingleExecution}

# Behavior class attributes and methods

# UML2_ActivityEdge class attributes and methods

# UML2_ActivityGroup class attributes and methods

# UML2_ActivityNode class attributes and methods

# UML2_Action class attributes and methods
UML2_Action_effect: Property = Property(name="effect", type=StringType)
UML2_Action.attributes={UML2_Action_effect}

# UML2_StructuredActivityNode class attributes and methods
UML2_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
UML2_StructuredActivityNode.attributes={UML2_StructuredActivityNode_mustIsolate}

# UML2_Permission class attributes and methods

# Dependency class attributes and methods

# UML2_Implementation class attributes and methods

# UML2_Trigger class attributes and methods

# UML2_StateMachine class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_InformationItem class attributes and methods

# UML2_InformationFlow class attributes and methods

# UML2_Usage class attributes and methods

# UML2_Abstraction class attributes and methods

# UML2_Realization class attributes and methods

# Abstraction class attributes and methods

# UML2_Component class attributes and methods
UML2_Component_isIndirectlyInstantiated: Property = Property(name="isIndirectlyInstantiated", type=BooleanType)
UML2_Component.attributes={UML2_Component_isIndirectlyInstantiated}

# Realization class attributes and methods

# UML2_Connector class attributes and methods
UML2_Connector_kind: Property = Property(name="kind", type=StringType)
UML2_Connector.attributes={UML2_Connector_kind}

# UML2_StructuredClassifier class attributes and methods

# UML2_Model class attributes and methods
UML2_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
UML2_Model.attributes={UML2_Model_viewpoint}

# UML2_ConnectorEnd class attributes and methods

# UML2_ConnectableElement class attributes and methods

# UML2_ActivityPartition class attributes and methods
UML2_ActivityPartition_isDimension: Property = Property(name="isDimension", type=BooleanType)
UML2_ActivityPartition_isExternal: Property = Property(name="isExternal", type=BooleanType)
UML2_ActivityPartition.attributes={UML2_ActivityPartition_isDimension, UML2_ActivityPartition_isExternal}

# UML2_InterruptibleActivityRegion class attributes and methods

# ExecutableNode class attributes and methods

# UML2_OutputPin class attributes and methods

# UML2_InputPin class attributes and methods

# UML2_ControlNode class attributes and methods

# UML2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# UML2_ObjectFlow class attributes and methods
UML2_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
UML2_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
UML2_ObjectFlow.attributes={UML2_ObjectFlow_isMultireceive, UML2_ObjectFlow_isMulticast}

# UML2_InitialNode class attributes and methods

# ControlNode class attributes and methods

# UML2_FinalNode class attributes and methods

# UML2_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# UML2_DecisionNode class attributes and methods

# UML2_MergeNode class attributes and methods

# UML2_ExecutableNode class attributes and methods

# UML2_ExceptionHandler class attributes and methods

# Pin class attributes and methods

# UML2_Pin class attributes and methods

# ObjectNode class attributes and methods

# UML2_ObjectNode class attributes and methods
UML2_ObjectNode_ordering: Property = Property(name="ordering", type=StringType)
UML2_ObjectNode.attributes={UML2_ObjectNode_ordering}

# ActivityNode class attributes and methods

# UML2_State class attributes and methods
UML2_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
UML2_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
UML2_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
UML2_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
UML2_State.attributes={UML2_State_isComposite, UML2_State_isOrthogonal, UML2_State_isSubmachineState, UML2_State_isSimple}

# UML2_ProtocolStateMachine class attributes and methods

# UML2_Artifact class attributes and methods
UML2_Artifact_fileName: Property = Property(name="fileName", type=StringType)
UML2_Artifact.attributes={UML2_Artifact_fileName}

# UML2_Manifestation class attributes and methods

# UML2_ActivityParameterNode class attributes and methods

# UML2_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2_Interface class attributes and methods

# UML2_Actor class attributes and methods

# UML2_Extend class attributes and methods

# UML2_ExtensionPoint class attributes and methods

# UML2_Include class attributes and methods

# StructuredClassifier class attributes and methods

# UML2_Port class attributes and methods
UML2_Port_isBehavior: Property = Property(name="isBehavior", type=BooleanType)
UML2_Port_isService: Property = Property(name="isService", type=BooleanType)
UML2_Port.attributes={UML2_Port_isService, UML2_Port_isBehavior}

# UML2_EncapsulatedClassifier class attributes and methods

# UML2_CallTrigger class attributes and methods

# MessageTrigger class attributes and methods

# UML2_MessageTrigger class attributes and methods

# Trigger class attributes and methods

# UML2_Collaboration class attributes and methods

# UML2_Signal class attributes and methods

# UML2_SignalTrigger class attributes and methods

# UML2_TimeTrigger class attributes and methods
UML2_TimeTrigger_isRelative: Property = Property(name="isRelative", type=BooleanType)
UML2_TimeTrigger.attributes={UML2_TimeTrigger_isRelative}

# UML2_AnyTrigger class attributes and methods

# UML2_Variable class attributes and methods

# Action class attributes and methods

# ActivityGroup class attributes and methods

# UML2_ChangeTrigger class attributes and methods

# UML2_Clause class attributes and methods

# UML2_LoopNode class attributes and methods
UML2_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
UML2_LoopNode.attributes={UML2_LoopNode_isTestedFirst}

# UML2_ConditionalNode class attributes and methods
UML2_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
UML2_ConditionalNode_isAssured: Property = Property(name="isAssured", type=BooleanType)
UML2_ConditionalNode.attributes={UML2_ConditionalNode_isDeterminate, UML2_ConditionalNode_isAssured}

# StructuredActivityNode class attributes and methods

# UML2_Interaction class attributes and methods

# InteractionFragment class attributes and methods

# UML2_Lifeline class attributes and methods

# UML2_Message class attributes and methods
UML2_Message_messageKind: Property = Property(name="messageKind", type=StringType)
UML2_Message_messageSort: Property = Property(name="messageSort", type=StringType)
UML2_Message.attributes={UML2_Message_messageSort, UML2_Message_messageKind}

# UML2_InteractionFragment class attributes and methods

# UML2_Gate class attributes and methods

# UML2_GeneralOrdering class attributes and methods

# UML2_InteractionOperand class attributes and methods

# UML2_PartDecomposition class attributes and methods

# UML2_MessageEnd class attributes and methods

# MessageEnd class attributes and methods

# UML2_ExecutionOccurrence class attributes and methods

# UML2_EventOccurrence class attributes and methods

# UML2_StateInvariant class attributes and methods

# UML2_TemplateableElement class attributes and methods

# UML2_ParameterableElement class attributes and methods

# UML2_Stop class attributes and methods

# EventOccurrence class attributes and methods

# UML2_TemplateSignature class attributes and methods

# UML2_TemplateParameter class attributes and methods

# UML2_TemplateBinding class attributes and methods

# UML2_TemplateParameterSubstitution class attributes and methods

# UML2_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# UML2_ClassifierTemplateParameter class attributes and methods
UML2_ClassifierTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=BooleanType)
UML2_ClassifierTemplateParameter.attributes={UML2_ClassifierTemplateParameter_allowSubstitutable}

# UML2_ParameterableClassifier class attributes and methods

# UML2_RedefinableTemplateSignature class attributes and methods

# TemplateSignature class attributes and methods

# UML2_TemplateableClassifier class attributes and methods

# UML2_ConnectableElementTemplateParameter class attributes and methods

# UML2_ForkNode class attributes and methods

# UML2_JoinNode class attributes and methods
UML2_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
UML2_JoinNode.attributes={UML2_JoinNode_isCombineDuplicate}

# UML2_FlowFinalNode class attributes and methods

# UML2_CentralBufferNode class attributes and methods

# UML2_ExpansionNode class attributes and methods

# UML2_ExpansionRegion class attributes and methods
UML2_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
UML2_ExpansionRegion.attributes={UML2_ExpansionRegion_mode}

# UML2_InteractionOccurrence class attributes and methods

# InteractionOccurrence class attributes and methods

# UML2_InteractionConstraint class attributes and methods

# UML2_CombinedFragment class attributes and methods
UML2_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
UML2_CombinedFragment.attributes={UML2_CombinedFragment_interactionOperator}

# UML2_Continuation class attributes and methods
UML2_Continuation_setting: Property = Property(name="setting", type=BooleanType)
UML2_Continuation.attributes={UML2_Continuation_setting}

# UML2_Region class attributes and methods

# UML2_Pseudostate class attributes and methods
UML2_Pseudostate_kind: Property = Property(name="kind", type=StringType)
UML2_Pseudostate.attributes={UML2_Pseudostate_kind}

# Constraint class attributes and methods

# Vertex class attributes and methods

# UML2_ConnectionPointReference class attributes and methods

# UML2_Vertex class attributes and methods

# UML2_Transition class attributes and methods
UML2_Transition_kind: Property = Property(name="kind", type=StringType)
UML2_Transition.attributes={UML2_Transition_kind}

# UML2_FinalState class attributes and methods

# State class attributes and methods

# UML2_CreateObjectAction class attributes and methods

# UML2_DestroyObjectAction class attributes and methods
UML2_DestroyObjectAction_isDestroyLinks: Property = Property(name="isDestroyLinks", type=BooleanType)
UML2_DestroyObjectAction_isDestroyOwnedObjects: Property = Property(name="isDestroyOwnedObjects", type=BooleanType)
UML2_DestroyObjectAction.attributes={UML2_DestroyObjectAction_isDestroyOwnedObjects, UML2_DestroyObjectAction_isDestroyLinks}

# UML2_TestIdentityAction class attributes and methods

# UML2_ReadSelfAction class attributes and methods

# UML2_StructuralFeatureAction class attributes and methods

# UML2_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UML2_WriteStructuralFeatureAction class attributes and methods

# UML2_ClearStructuralFeatureAction class attributes and methods

# UML2_RemoveStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# UML2_AddStructuralFeatureValueAction class attributes and methods
UML2_AddStructuralFeatureValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2_AddStructuralFeatureValueAction.attributes={UML2_AddStructuralFeatureValueAction_isReplaceAll}

# UML2_QualifierValue class attributes and methods

# UML2_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UML2_LinkEndCreationData class attributes and methods
UML2_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2_LinkEndCreationData.attributes={UML2_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# UML2_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UML2_WriteLinkAction class attributes and methods

# UML2_DestroyLinkAction class attributes and methods

# UML2_ClearAssociationAction class attributes and methods

# UML2_VariableAction class attributes and methods

# UML2_LinkAction class attributes and methods

# UML2_LinkEndData class attributes and methods

# UML2_RemoveVariableValueAction class attributes and methods

# UML2_ApplyFunctionAction class attributes and methods

# UML2_PrimitiveFunction class attributes and methods
UML2_PrimitiveFunction_body: Property = Property(name="body", type=StringType)
UML2_PrimitiveFunction_language: Property = Property(name="language", type=StringType)
UML2_PrimitiveFunction.attributes={UML2_PrimitiveFunction_language, UML2_PrimitiveFunction_body}

# UML2_CallAction class attributes and methods
UML2_CallAction_isSynchronous: Property = Property(name="isSynchronous", type=BooleanType)
UML2_CallAction.attributes={UML2_CallAction_isSynchronous}

# InvocationAction class attributes and methods

# UML2_InvocationAction class attributes and methods

# UML2_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# UML2_WriteVariableAction class attributes and methods

# UML2_ClearVariableAction class attributes and methods

# UML2_AddVariableValueAction class attributes and methods
UML2_AddVariableValueAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2_AddVariableValueAction.attributes={UML2_AddVariableValueAction_isReplaceAll}

# WriteVariableAction class attributes and methods

# UML2_SendObjectAction class attributes and methods

# UML2_CallOperationAction class attributes and methods

# CallAction class attributes and methods

# UML2_CallBehaviorAction class attributes and methods

# UML2_TimeExpression class attributes and methods
UML2_TimeExpression_firstTime: Property = Property(name="firstTime", type=BooleanType)
UML2_TimeExpression.attributes={UML2_TimeExpression_firstTime}

# UML2_Duration class attributes and methods
UML2_Duration_firstTime: Property = Property(name="firstTime", type=BooleanType)
UML2_Duration.attributes={UML2_Duration_firstTime}

# UML2_SendSignalAction class attributes and methods

# UML2_BroadcastSignalAction class attributes and methods

# UML2_IntervalConstraint class attributes and methods

# UML2_TimeInterval class attributes and methods

# UML2_DurationObservationAction class attributes and methods

# UML2_DurationConstraint class attributes and methods

# UML2_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2_TimeObservationAction class attributes and methods

# UML2_DurationInterval class attributes and methods

# Interval class attributes and methods

# UML2_Interval class attributes and methods

# UML2_TimeConstraint class attributes and methods

# IntervalConstraint class attributes and methods

# UML2_Deployment class attributes and methods

# UML2_DeployedArtifact class attributes and methods

# UML2_DeploymentTarget class attributes and methods

# UML2_DeploymentSpecification class attributes and methods
UML2_DeploymentSpecification_deploymentLocation: Property = Property(name="deploymentLocation", type=StringType)
UML2_DeploymentSpecification_executionLocation: Property = Property(name="executionLocation", type=StringType)
UML2_DeploymentSpecification.attributes={UML2_DeploymentSpecification_executionLocation, UML2_DeploymentSpecification_deploymentLocation}

# UML2_Node class attributes and methods

# UML2_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# UML2_ReadExtentAction class attributes and methods

# UML2_ReclassifyObjectAction class attributes and methods
UML2_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
UML2_ReclassifyObjectAction.attributes={UML2_ReclassifyObjectAction_isReplaceAll}

# UML2_Device class attributes and methods

# Node class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# UML2_CommunicationPath class attributes and methods

# UML2_ProtocolConformance class attributes and methods

# StateMachine class attributes and methods

# UML2_StartOwnedBehaviorAction class attributes and methods

# UML2_ReadLinkObjectEndAction class attributes and methods

# UML2_ReadLinkObjectEndQualifierAction class attributes and methods

# UML2_ReadIsClassifiedObjectAction class attributes and methods
UML2_ReadIsClassifiedObjectAction_isDirect: Property = Property(name="isDirect", type=BooleanType)
UML2_ReadIsClassifiedObjectAction.attributes={UML2_ReadIsClassifiedObjectAction_isDirect}

# UML2_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UML2_ReplyAction class attributes and methods

# UML2_RaiseExceptionAction class attributes and methods

# Artifact class attributes and methods

# UML2_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UML2_AcceptEventAction class attributes and methods

# Relationships
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="UML2_NamedElement13", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Namespace", type=UML2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Element", type=UML2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=UML2_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Element4", type=UML2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=UML2_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="UML2_Comment", type=UML2_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Element", type=UML2_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperValue6: BinaryAssociation = BinaryAssociation(
    name="upperValue6",
    ends={
        Property(name="UML2_ValueSpecification", type=UML2_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_MultiplicityElement", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue7: BinaryAssociation = BinaryAssociation(
    name="lowerValue7",
    ends={
        Property(name="UML2_ValueSpecification9", type=UML2_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_MultiplicityElement8", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clientDependency10: BinaryAssociation = BinaryAssociation(
    name="clientDependency10",
    ends={
        Property(name="Dependency", type=UML2_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=UML2_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
nameExpression11: BinaryAssociation = BinaryAssociation(
    name="nameExpression11",
    ends={
        Property(name="UML2_StringExpression", type=UML2_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_NamedElement", type=UML2_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRule14: BinaryAssociation = BinaryAssociation(
    name="ownedRule14",
    ends={
        Property(name="Constraint", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember15: BinaryAssociation = BinaryAssociation(
    name="importedMember15",
    ends={
        Property(name="UML2_PackageableElement", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Namespace16", type=UML2_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport17: BinaryAssociation = BinaryAssociation(
    name="elementImport17",
    ends={
        Property(name="ElementImport", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=UML2_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport18: BinaryAssociation = BinaryAssociation(
    name="packageImport18",
    ends={
        Property(name="PackageImport", type=UML2_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace19", type=UML2_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result20: BinaryAssociation = BinaryAssociation(
    name="result20",
    ends={
        Property(name="UML2_Parameter", type=UML2_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_OpaqueExpression", type=UML2_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior21: BinaryAssociation = BinaryAssociation(
    name="behavior21",
    ends={
        Property(name="UML2_Behavior", type=UML2_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_OpaqueExpression22", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
operand23: BinaryAssociation = BinaryAssociation(
    name="operand23",
    ends={
        Property(name="UML2_ValueSpecification24", type=UML2_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Expression", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement25: BinaryAssociation = BinaryAssociation(
    name="annotatedElement25",
    ends={
        Property(name="UML2_Element27", type=UML2_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Comment26", type=UML2_Element, multiplicity=Multiplicity(0, 9999))
    }
)
bodyExpression28: BinaryAssociation = BinaryAssociation(
    name="bodyExpression28",
    ends={
        Property(name="UML2_StringExpression30", type=UML2_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Comment29", type=UML2_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source31: BinaryAssociation = BinaryAssociation(
    name="source31",
    ends={
        Property(name="UML2_Element32", type=UML2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DirectedRelationship", type=UML2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="UML2_Element35", type=UML2_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DirectedRelationship34", type=UML2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
redefinedProperty54: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty54",
    ends={
        Property(name="UML2_Property53", type=UML2_Property, multiplicity=Multiplicity(0, 9999)),
        Property(name="UML2_Property55", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
relatedElement36: BinaryAssociation = BinaryAssociation(
    name="relatedElement36",
    ends={
        Property(name="UML2_Element37", type=UML2_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Relationship", type=UML2_Element, multiplicity=Multiplicity(1, 9999))
    }
)
ownedOperation38: BinaryAssociation = BinaryAssociation(
    name="ownedOperation38",
    ends={
        Property(name="Operation", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=UML2_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass40: BinaryAssociation = BinaryAssociation(
    name="superClass40",
    ends={
        Property(name="UML2_Class", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class39", type=UML2_Class, multiplicity=Multiplicity(0, 9999))
    }
)
extension41: BinaryAssociation = BinaryAssociation(
    name="extension41",
    ends={
        Property(name="Extension", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="metaclass", type=UML2_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier42: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier42",
    ends={
        Property(name="UML2_Classifier", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class43", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception44: BinaryAssociation = BinaryAssociation(
    name="ownedReception44",
    ends={
        Property(name="UML2_Reception", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class45", type=UML2_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package46: BinaryAssociation = BinaryAssociation(
    name="package46",
    ends={
        Property(name="Package", type=UML2_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=UML2_Package, multiplicity=Multiplicity(0, 1))
    }
)
class_47: BinaryAssociation = BinaryAssociation(
    name="class_47",
    ends={
        Property(name="UML2_Class48", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property", type=UML2_Class, multiplicity=Multiplicity(0, 1))
    }
)
opposite50: BinaryAssociation = BinaryAssociation(
    name="opposite50",
    ends={
        Property(name="UML2_Property51", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property49", type=UML2_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation52: BinaryAssociation = BinaryAssociation(
    name="owningAssociation52",
    ends={
        Property(name="Association", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=UML2_Association, multiplicity=Multiplicity(0, 1))
    }
)
type85: BinaryAssociation = BinaryAssociation(
    name="type85",
    ends={
        Property(name="UML2_Type", type=UML2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TypedElement", type=UML2_Type, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty57: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty57",
    ends={
        Property(name="UML2_Property58", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property56", type=UML2_Property, multiplicity=Multiplicity(0, 9999))
    }
)
datatype59: BinaryAssociation = BinaryAssociation(
    name="datatype59",
    ends={
        Property(name="DataType", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=UML2_DataType, multiplicity=Multiplicity(0, 1))
    }
)
association60: BinaryAssociation = BinaryAssociation(
    name="association60",
    ends={
        Property(name="Association61", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=UML2_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue62: BinaryAssociation = BinaryAssociation(
    name="defaultValue62",
    ends={
        Property(name="UML2_ValueSpecification64", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property63", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier66: BinaryAssociation = BinaryAssociation(
    name="qualifier66",
    ends={
        Property(name="Property", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd68: BinaryAssociation = BinaryAssociation(
    name="associationEnd68",
    ends={
        Property(name="Property69", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=UML2_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter70: BinaryAssociation = BinaryAssociation(
    name="ownedParameter70",
    ends={
        Property(name="Parameter", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_71: BinaryAssociation = BinaryAssociation(
    name="class_71",
    ends={
        Property(name="Class", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=UML2_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype72: BinaryAssociation = BinaryAssociation(
    name="datatype72",
    ends={
        Property(name="DataType74", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation73", type=UML2_DataType, multiplicity=Multiplicity(0, 1))
    }
)
precondition75: BinaryAssociation = BinaryAssociation(
    name="precondition75",
    ends={
        Property(name="UML2_Constraint", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition76: BinaryAssociation = BinaryAssociation(
    name="postcondition76",
    ends={
        Property(name="UML2_Constraint78", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation77", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation80: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation80",
    ends={
        Property(name="UML2_Operation81", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation79", type=UML2_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
bodyCondition82: BinaryAssociation = BinaryAssociation(
    name="bodyCondition82",
    ends={
        Property(name="UML2_Constraint84", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation83", type=UML2_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute107: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute107",
    ends={
        Property(name="Property108", type=UML2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation86: BinaryAssociation = BinaryAssociation(
    name="operation86",
    ends={
        Property(name="Operation87", type=UML2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=UML2_Operation, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue88: BinaryAssociation = BinaryAssociation(
    name="defaultValue88",
    ends={
        Property(name="UML2_ValueSpecification90", type=UML2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Parameter89", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterSet91: BinaryAssociation = BinaryAssociation(
    name="parameterSet91",
    ends={
        Property(name="ParameterSet", type=UML2_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=UML2_ParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage93: BinaryAssociation = BinaryAssociation(
    name="nestedPackage93",
    ends={
        Property(name="Package94", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=UML2_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage96: BinaryAssociation = BinaryAssociation(
    name="nestingPackage96",
    ends={
        Property(name="Package97", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=UML2_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType98: BinaryAssociation = BinaryAssociation(
    name="ownedType98",
    ends={
        Property(name="Type", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=UML2_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember99: BinaryAssociation = BinaryAssociation(
    name="ownedMember99",
    ends={
        Property(name="UML2_PackageableElement100", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Package", type=UML2_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge101: BinaryAssociation = BinaryAssociation(
    name="packageMerge101",
    ends={
        Property(name="PackageMerge", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="mergingPackage", type=UML2_PackageMerge, multiplicity=Multiplicity(0, 9999))
    }
)
appliedProfile102: BinaryAssociation = BinaryAssociation(
    name="appliedProfile102",
    ends={
        Property(name="UML2_ProfileApplication", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Package103", type=UML2_ProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
packageExtension104: BinaryAssociation = BinaryAssociation(
    name="packageExtension104",
    ends={
        Property(name="UML2_PackageMerge", type=UML2_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Package105", type=UML2_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral106: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral106",
    ends={
        Property(name="EnumerationLiteral", type=UML2_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=UML2_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representation132: BinaryAssociation = BinaryAssociation(
    name="representation132",
    ends={
        Property(name="UML2_CollaborationOccurrence", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier133", type=UML2_CollaborationOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperation109: BinaryAssociation = BinaryAssociation(
    name="ownedOperation109",
    ends={
        Property(name="Operation111", type=UML2_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype110", type=UML2_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration112: BinaryAssociation = BinaryAssociation(
    name="enumeration112",
    ends={
        Property(name="Enumeration", type=UML2_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=UML2_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
feature113: BinaryAssociation = BinaryAssociation(
    name="feature113",
    ends={
        Property(name="Feature", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=UML2_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember114: BinaryAssociation = BinaryAssociation(
    name="inheritedMember114",
    ends={
        Property(name="UML2_NamedElement116", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier115", type=UML2_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
general118: BinaryAssociation = BinaryAssociation(
    name="general118",
    ends={
        Property(name="UML2_Classifier119", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier117", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization120: BinaryAssociation = BinaryAssociation(
    name="generalization120",
    ends={
        Property(name="Generalization", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=UML2_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute121: BinaryAssociation = BinaryAssociation(
    name="attribute121",
    ends={
        Property(name="UML2_Property123", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier122", type=UML2_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier125: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier125",
    ends={
        Property(name="UML2_Classifier126", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier124", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
substitution127: BinaryAssociation = BinaryAssociation(
    name="substitution127",
    ends={
        Property(name="Substitution", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=UML2_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent128: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent128",
    ends={
        Property(name="GeneralizationSet", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=UML2_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUseCase129: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase129",
    ends={
        Property(name="UML2_UseCase", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier130", type=UML2_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
useCase131: BinaryAssociation = BinaryAssociation(
    name="useCase131",
    ends={
        Property(name="UseCase", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=UML2_UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
parameter148: BinaryAssociation = BinaryAssociation(
    name="parameter148",
    ends={
        Property(name="UML2_Parameter149", type=UML2_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioralFeature", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
occurrence134: BinaryAssociation = BinaryAssociation(
    name="occurrence134",
    ends={
        Property(name="UML2_CollaborationOccurrence136", type=UML2_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Classifier135", type=UML2_CollaborationOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuringClassifier137: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier137",
    ends={
        Property(name="Classifier", type=UML2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context138: BinaryAssociation = BinaryAssociation(
    name="context138",
    ends={
        Property(name="UML2_Namespace140", type=UML2_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Constraint139", type=UML2_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
namespace141: BinaryAssociation = BinaryAssociation(
    name="namespace141",
    ends={
        Property(name="Namespace", type=UML2_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=UML2_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
specification142: BinaryAssociation = BinaryAssociation(
    name="specification142",
    ends={
        Property(name="UML2_ValueSpecification144", type=UML2_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Constraint143", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedElement145: BinaryAssociation = BinaryAssociation(
    name="constrainedElement145",
    ends={
        Property(name="UML2_Element147", type=UML2_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Constraint146", type=UML2_Element, multiplicity=Multiplicity(0, 9999))
    }
)
formalParameter150: BinaryAssociation = BinaryAssociation(
    name="formalParameter150",
    ends={
        Property(name="UML2_Parameter152", type=UML2_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioralFeature151", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnResult153: BinaryAssociation = BinaryAssociation(
    name="returnResult153",
    ends={
        Property(name="UML2_Parameter155", type=UML2_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioralFeature154", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException156: BinaryAssociation = BinaryAssociation(
    name="raisedException156",
    ends={
        Property(name="UML2_Type158", type=UML2_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioralFeature157", type=UML2_Type, multiplicity=Multiplicity(0, 9999))
    }
)
method159: BinaryAssociation = BinaryAssociation(
    name="method159",
    ends={
        Property(name="Behavior", type=UML2_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
slot160: BinaryAssociation = BinaryAssociation(
    name="slot160",
    ends={
        Property(name="Slot", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=UML2_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier161: BinaryAssociation = BinaryAssociation(
    name="classifier161",
    ends={
        Property(name="UML2_Classifier162", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InstanceSpecification", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specification163: BinaryAssociation = BinaryAssociation(
    name="specification163",
    ends={
        Property(name="UML2_ValueSpecification165", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InstanceSpecification164", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinitionContext173: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext173",
    ends={
        Property(name="UML2_Classifier174", type=UML2_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_RedefinableElement", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specific175: BinaryAssociation = BinaryAssociation(
    name="specific175",
    ends={
        Property(name="Classifier176", type=UML2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
general177: BinaryAssociation = BinaryAssociation(
    name="general177",
    ends={
        Property(name="UML2_Classifier178", type=UML2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Generalization", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet179: BinaryAssociation = BinaryAssociation(
    name="generalizationSet179",
    ends={
        Property(name="GeneralizationSet181", type=UML2_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization180", type=UML2_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement182: BinaryAssociation = BinaryAssociation(
    name="importedElement182",
    ends={
        Property(name="UML2_PackageableElement183", type=UML2_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ElementImport", type=UML2_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace184: BinaryAssociation = BinaryAssociation(
    name="importingNamespace184",
    ends={
        Property(name="Namespace185", type=UML2_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=UML2_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
owningInstance166: BinaryAssociation = BinaryAssociation(
    name="owningInstance166",
    ends={
        Property(name="InstanceSpecification", type=UML2_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value167: BinaryAssociation = BinaryAssociation(
    name="value167",
    ends={
        Property(name="UML2_ValueSpecification168", type=UML2_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Slot", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature169: BinaryAssociation = BinaryAssociation(
    name="definingFeature169",
    ends={
        Property(name="UML2_StructuralFeature", type=UML2_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Slot170", type=UML2_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
instance171: BinaryAssociation = BinaryAssociation(
    name="instance171",
    ends={
        Property(name="UML2_InstanceSpecification172", type=UML2_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InstanceValue", type=UML2_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
endType192: BinaryAssociation = BinaryAssociation(
    name="endType192",
    ends={
        Property(name="UML2_Type193", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Association", type=UML2_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd194: BinaryAssociation = BinaryAssociation(
    name="memberEnd194",
    ends={
        Property(name="Property195", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML2_Property, multiplicity=Multiplicity(2, 9999))
    }
)
mergingPackage196: BinaryAssociation = BinaryAssociation(
    name="mergingPackage196",
    ends={
        Property(name="Package197", type=UML2_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=UML2_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage198: BinaryAssociation = BinaryAssociation(
    name="mergedPackage198",
    ends={
        Property(name="UML2_Package200", type=UML2_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_PackageMerge199", type=UML2_Package, multiplicity=Multiplicity(1, 1))
    }
)
ownedStereotype201: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype201",
    ends={
        Property(name="UML2_Stereotype", type=UML2_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Profile", type=UML2_Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
metaclassReference202: BinaryAssociation = BinaryAssociation(
    name="metaclassReference202",
    ends={
        Property(name="UML2_ElementImport204", type=UML2_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Profile203", type=UML2_ElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference205: BinaryAssociation = BinaryAssociation(
    name="metamodelReference205",
    ends={
        Property(name="UML2_PackageImport207", type=UML2_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Profile206", type=UML2_PackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
importedProfile208: BinaryAssociation = BinaryAssociation(
    name="importedProfile208",
    ends={
        Property(name="UML2_Profile210", type=UML2_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ProfileApplication209", type=UML2_Profile, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage186: BinaryAssociation = BinaryAssociation(
    name="importedPackage186",
    ends={
        Property(name="UML2_Package187", type=UML2_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_PackageImport", type=UML2_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace188: BinaryAssociation = BinaryAssociation(
    name="importingNamespace188",
    ends={
        Property(name="Namespace189", type=UML2_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=UML2_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
ownedEnd190: BinaryAssociation = BinaryAssociation(
    name="ownedEnd190",
    ends={
        Property(name="Property191", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context213: BinaryAssociation = BinaryAssociation(
    name="context213",
    ends={
        Property(name="BehavioredClassifier", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBehavior", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
redefinedBehavior215: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior215",
    ends={
        Property(name="UML2_Behavior216", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior214", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification217: BinaryAssociation = BinaryAssociation(
    name="specification217",
    ends={
        Property(name="BehavioralFeature", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=UML2_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
parameter218: BinaryAssociation = BinaryAssociation(
    name="parameter218",
    ends={
        Property(name="UML2_Parameter220", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior219", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameter221: BinaryAssociation = BinaryAssociation(
    name="formalParameter221",
    ends={
        Property(name="UML2_Parameter223", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior222", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
returnResult224: BinaryAssociation = BinaryAssociation(
    name="returnResult224",
    ends={
        Property(name="UML2_Parameter226", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior225", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
precondition227: BinaryAssociation = BinaryAssociation(
    name="precondition227",
    ends={
        Property(name="UML2_Constraint229", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior228", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition230: BinaryAssociation = BinaryAssociation(
    name="postcondition230",
    ends={
        Property(name="UML2_Constraint232", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior231", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet233: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet233",
    ends={
        Property(name="UML2_ParameterSet", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior234", type=UML2_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaclass211: BinaryAssociation = BinaryAssociation(
    name="metaclass211",
    ends={
        Property(name="Class212", type=UML2_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=UML2_Class, multiplicity=Multiplicity(1, 1))
    }
)
edge243: BinaryAssociation = BinaryAssociation(
    name="edge243",
    ends={
        Property(name="ActivityEdge", type=UML2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group244: BinaryAssociation = BinaryAssociation(
    name="group244",
    ends={
        Property(name="ActivityGroup", type=UML2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activityGroup_activity", type=UML2_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node245: BinaryAssociation = BinaryAssociation(
    name="node245",
    ends={
        Property(name="ActivityNode", type=UML2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity246", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action247: BinaryAssociation = BinaryAssociation(
    name="action247",
    ends={
        Property(name="UML2_Action", type=UML2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Activity", type=UML2_Action, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode248: BinaryAssociation = BinaryAssociation(
    name="structuredNode248",
    ends={
        Property(name="UML2_StructuredActivityNode", type=UML2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Activity249", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
client250: BinaryAssociation = BinaryAssociation(
    name="client250",
    ends={
        Property(name="NamedElement", type=UML2_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=UML2_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier251: BinaryAssociation = BinaryAssociation(
    name="supplier251",
    ends={
        Property(name="UML2_NamedElement252", type=UML2_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Dependency", type=UML2_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedBehavior235: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior235",
    ends={
        Property(name="Behavior236", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior237: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior237",
    ends={
        Property(name="UML2_Behavior238", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
implementation239: BinaryAssociation = BinaryAssociation(
    name="implementation239",
    ends={
        Property(name="Implementation", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=UML2_Implementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTrigger240: BinaryAssociation = BinaryAssociation(
    name="ownedTrigger240",
    ends={
        Property(name="UML2_Trigger", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier241", type=UML2_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStateMachine242: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachine242",
    ends={
        Property(name="StateMachine", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_redefinitionContext", type=UML2_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract258: BinaryAssociation = BinaryAssociation(
    name="contract258",
    ends={
        Property(name="UML2_Classifier259", type=UML2_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Substitution", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier260: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier260",
    ends={
        Property(name="Classifier261", type=UML2_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
powertype262: BinaryAssociation = BinaryAssociation(
    name="powertype262",
    ends={
        Property(name="Classifier263", type=UML2_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=UML2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization264: BinaryAssociation = BinaryAssociation(
    name="generalization264",
    ends={
        Property(name="Generalization265", type=UML2_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=UML2_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
represented266: BinaryAssociation = BinaryAssociation(
    name="represented266",
    ends={
        Property(name="UML2_Classifier267", type=UML2_InformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InformationItem", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
realization268: BinaryAssociation = BinaryAssociation(
    name="realization268",
    ends={
        Property(name="UML2_Relationship269", type=UML2_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InformationFlow", type=UML2_Relationship, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed270: BinaryAssociation = BinaryAssociation(
    name="conveyed270",
    ends={
        Property(name="UML2_Classifier272", type=UML2_InformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InformationFlow271", type=UML2_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
mapping253: BinaryAssociation = BinaryAssociation(
    name="mapping253",
    ends={
        Property(name="UML2_OpaqueExpression254", type=UML2_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Abstraction", type=UML2_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstraction255: BinaryAssociation = BinaryAssociation(
    name="abstraction255",
    ends={
        Property(name="Component", type=UML2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="realization", type=UML2_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier256: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier256",
    ends={
        Property(name="UML2_Classifier257", type=UML2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Realization", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
end279: BinaryAssociation = BinaryAssociation(
    name="end279",
    ends={
        Property(name="ConnectorEnd", type=UML2_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=UML2_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
type280: BinaryAssociation = BinaryAssociation(
    name="type280",
    ends={
        Property(name="UML2_Association281", type=UML2_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Connector", type=UML2_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConnector283: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector283",
    ends={
        Property(name="UML2_Connector284", type=UML2_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Connector282", type=UML2_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
end285: BinaryAssociation = BinaryAssociation(
    name="end285",
    ends={
        Property(name="UML2_ConnectorEnd287", type=UML2_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Connector286", type=UML2_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract288: BinaryAssociation = BinaryAssociation(
    name="contract288",
    ends={
        Property(name="UML2_Behavior290", type=UML2_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Connector289", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute291: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute291",
    ends={
        Property(name="UML2_Property292", type=UML2_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuredClassifier", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part293: BinaryAssociation = BinaryAssociation(
    name="part293",
    ends={
        Property(name="UML2_Property295", type=UML2_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuredClassifier294", type=UML2_Property, multiplicity=Multiplicity(0, 9999))
    }
)
role296: BinaryAssociation = BinaryAssociation(
    name="role296",
    ends={
        Property(name="UML2_ConnectableElement", type=UML2_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuredClassifier297", type=UML2_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector298: BinaryAssociation = BinaryAssociation(
    name="ownedConnector298",
    ends={
        Property(name="UML2_Connector300", type=UML2_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuredClassifier299", type=UML2_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingEnd273: BinaryAssociation = BinaryAssociation(
    name="definingEnd273",
    ends={
        Property(name="UML2_Property274", type=UML2_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConnectorEnd", type=UML2_Property, multiplicity=Multiplicity(0, 1))
    }
)
role275: BinaryAssociation = BinaryAssociation(
    name="role275",
    ends={
        Property(name="ConnectableElement", type=UML2_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=UML2_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
partWithPort276: BinaryAssociation = BinaryAssociation(
    name="partWithPort276",
    ends={
        Property(name="UML2_Property278", type=UML2_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConnectorEnd277", type=UML2_Property, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement311: BinaryAssociation = BinaryAssociation(
    name="redefinedElement311",
    ends={
        Property(name="UML2_ActivityEdge312", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityEdge310", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode313: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode313",
    ends={
        Property(name="StructuredActivityNode", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inPartition314: BinaryAssociation = BinaryAssociation(
    name="inPartition314",
    ends={
        Property(name="ActivityPartition", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="containedEdge315", type=UML2_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
weight316: BinaryAssociation = BinaryAssociation(
    name="weight316",
    ends={
        Property(name="UML2_ValueSpecification318", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityEdge317", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts319: BinaryAssociation = BinaryAssociation(
    name="interrupts319",
    ends={
        Property(name="InterruptibleActivityRegion", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="interruptingEdge", type=UML2_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
superGroup321: BinaryAssociation = BinaryAssociation(
    name="superGroup321",
    ends={
        Property(name="UML2_ActivityGroup322", type=UML2_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityGroup320", type=UML2_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
activity301: BinaryAssociation = BinaryAssociation(
    name="activity301",
    ends={
        Property(name="Activity", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=UML2_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source302: BinaryAssociation = BinaryAssociation(
    name="source302",
    ends={
        Property(name="ActivityNode303", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target304: BinaryAssociation = BinaryAssociation(
    name="target304",
    ends={
        Property(name="ActivityNode305", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inGroup306: BinaryAssociation = BinaryAssociation(
    name="inGroup306",
    ends={
        Property(name="UML2_ActivityGroup", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityEdge", type=UML2_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
guard307: BinaryAssociation = BinaryAssociation(
    name="guard307",
    ends={
        Property(name="UML2_ValueSpecification309", type=UML2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityEdge308", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activity331: BinaryAssociation = BinaryAssociation(
    name="activity331",
    ends={
        Property(name="Activity332", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=UML2_Activity, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement334: BinaryAssociation = BinaryAssociation(
    name="redefinedElement334",
    ends={
        Property(name="UML2_ActivityNode335", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityNode333", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode336: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode336",
    ends={
        Property(name="StructuredActivityNode337", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inPartition338: BinaryAssociation = BinaryAssociation(
    name="inPartition338",
    ends={
        Property(name="ActivityPartition340", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode339", type=UML2_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion341: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion341",
    ends={
        Property(name="InterruptibleActivityRegion343", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="containedNode342", type=UML2_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
output344: BinaryAssociation = BinaryAssociation(
    name="output344",
    ends={
        Property(name="UML2_OutputPin", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action345", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
input346: BinaryAssociation = BinaryAssociation(
    name="input346",
    ends={
        Property(name="UML2_InputPin", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action347", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context_348: BinaryAssociation = BinaryAssociation(
    name="context_348",
    ends={
        Property(name="UML2_Classifier350", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action349", type=UML2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
localPrecondition351: BinaryAssociation = BinaryAssociation(
    name="localPrecondition351",
    ends={
        Property(name="UML2_Constraint353", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action352", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localPostcondition354: BinaryAssociation = BinaryAssociation(
    name="localPostcondition354",
    ends={
        Property(name="UML2_Constraint356", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action355", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityGroup_activity323: BinaryAssociation = BinaryAssociation(
    name="activityGroup_activity323",
    ends={
        Property(name="Activity324", type=UML2_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=UML2_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing325: BinaryAssociation = BinaryAssociation(
    name="outgoing325",
    ends={
        Property(name="ActivityEdge326", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming327: BinaryAssociation = BinaryAssociation(
    name="incoming327",
    ends={
        Property(name="ActivityEdge328", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup329: BinaryAssociation = BinaryAssociation(
    name="inGroup329",
    ends={
        Property(name="UML2_ActivityGroup330", type=UML2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityNode", type=UML2_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
selection361: BinaryAssociation = BinaryAssociation(
    name="selection361",
    ends={
        Property(name="UML2_Behavior363", type=UML2_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ObjectNode362", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
transformation364: BinaryAssociation = BinaryAssociation(
    name="transformation364",
    ends={
        Property(name="UML2_Behavior365", type=UML2_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ObjectFlow", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection366: BinaryAssociation = BinaryAssociation(
    name="selection366",
    ends={
        Property(name="UML2_Behavior368", type=UML2_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ObjectFlow367", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput369: BinaryAssociation = BinaryAssociation(
    name="decisionInput369",
    ends={
        Property(name="UML2_Behavior370", type=UML2_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DecisionNode", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
handler371: BinaryAssociation = BinaryAssociation(
    name="handler371",
    ends={
        Property(name="ExceptionHandler", type=UML2_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="protectedNode", type=UML2_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperBound357: BinaryAssociation = BinaryAssociation(
    name="upperBound357",
    ends={
        Property(name="UML2_ValueSpecification358", type=UML2_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ObjectNode", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inState359: BinaryAssociation = BinaryAssociation(
    name="inState359",
    ends={
        Property(name="UML2_State", type=UML2_ObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ObjectNode360", type=UML2_State, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute376: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute376",
    ends={
        Property(name="UML2_Property377", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation378: BinaryAssociation = BinaryAssociation(
    name="ownedOperation378",
    ends={
        Property(name="UML2_Operation380", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface379", type=UML2_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedInterface382: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface382",
    ends={
        Property(name="UML2_Interface383", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface381", type=UML2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier384: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier384",
    ends={
        Property(name="UML2_Classifier386", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface385", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception387: BinaryAssociation = BinaryAssociation(
    name="ownedReception387",
    ends={
        Property(name="UML2_Reception389", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface388", type=UML2_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocol390: BinaryAssociation = BinaryAssociation(
    name="protocol390",
    ends={
        Property(name="UML2_ProtocolStateMachine", type=UML2_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interface391", type=UML2_ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contract392: BinaryAssociation = BinaryAssociation(
    name="contract392",
    ends={
        Property(name="UML2_Interface393", type=UML2_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Implementation", type=UML2_Interface, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier394: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier394",
    ends={
        Property(name="BehavioredClassifier395", type=UML2_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementation", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
nestedArtifact397: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact397",
    ends={
        Property(name="UML2_Artifact", type=UML2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Artifact396", type=UML2_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifestation398: BinaryAssociation = BinaryAssociation(
    name="manifestation398",
    ends={
        Property(name="UML2_Manifestation", type=UML2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Artifact399", type=UML2_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter372: BinaryAssociation = BinaryAssociation(
    name="parameter372",
    ends={
        Property(name="UML2_Parameter373", type=UML2_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityParameterNode", type=UML2_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value374: BinaryAssociation = BinaryAssociation(
    name="value374",
    ends={
        Property(name="UML2_ValueSpecification375", type=UML2_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ValuePin", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedCase409: BinaryAssociation = BinaryAssociation(
    name="extendedCase409",
    ends={
        Property(name="UML2_UseCase410", type=UML2_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Extend", type=UML2_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extension411: BinaryAssociation = BinaryAssociation(
    name="extension411",
    ends={
        Property(name="UseCase412", type=UML2_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=UML2_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition413: BinaryAssociation = BinaryAssociation(
    name="condition413",
    ends={
        Property(name="UML2_Constraint415", type=UML2_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Extend414", type=UML2_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionLocation416: BinaryAssociation = BinaryAssociation(
    name="extensionLocation416",
    ends={
        Property(name="UML2_ExtensionPoint", type=UML2_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Extend417", type=UML2_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
include418: BinaryAssociation = BinaryAssociation(
    name="include418",
    ends={
        Property(name="Include", type=UML2_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="includingCase", type=UML2_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend419: BinaryAssociation = BinaryAssociation(
    name="extend419",
    ends={
        Property(name="Extend", type=UML2_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension420", type=UML2_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint421: BinaryAssociation = BinaryAssociation(
    name="extensionPoint421",
    ends={
        Property(name="ExtensionPoint", type=UML2_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=UML2_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject422: BinaryAssociation = BinaryAssociation(
    name="subject422",
    ends={
        Property(name="Classifier424", type=UML2_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase423", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
useCase425: BinaryAssociation = BinaryAssociation(
    name="useCase425",
    ends={
        Property(name="UseCase426", type=UML2_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=UML2_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperation400: BinaryAssociation = BinaryAssociation(
    name="ownedOperation400",
    ends={
        Property(name="UML2_Operation402", type=UML2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Artifact401", type=UML2_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute403: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute403",
    ends={
        Property(name="UML2_Property405", type=UML2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Artifact404", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizedElement406: BinaryAssociation = BinaryAssociation(
    name="utilizedElement406",
    ends={
        Property(name="UML2_PackageableElement408", type=UML2_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Manifestation407", type=UML2_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding433: BinaryAssociation = BinaryAssociation(
    name="roleBinding433",
    ends={
        Property(name="UML2_Dependency435", type=UML2_CollaborationOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CollaborationOccurrence434", type=UML2_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationRole436: BinaryAssociation = BinaryAssociation(
    name="collaborationRole436",
    ends={
        Property(name="UML2_ConnectableElement438", type=UML2_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Collaboration437", type=UML2_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
required439: BinaryAssociation = BinaryAssociation(
    name="required439",
    ends={
        Property(name="UML2_Interface440", type=UML2_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Port", type=UML2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort442: BinaryAssociation = BinaryAssociation(
    name="redefinedPort442",
    ends={
        Property(name="UML2_Port443", type=UML2_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Port441", type=UML2_Port, multiplicity=Multiplicity(0, 9999))
    }
)
provided444: BinaryAssociation = BinaryAssociation(
    name="provided444",
    ends={
        Property(name="UML2_Interface446", type=UML2_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Port445", type=UML2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
protocol447: BinaryAssociation = BinaryAssociation(
    name="protocol447",
    ends={
        Property(name="UML2_ProtocolStateMachine449", type=UML2_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Port448", type=UML2_ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
ownedPort450: BinaryAssociation = BinaryAssociation(
    name="ownedPort450",
    ends={
        Property(name="UML2_Port451", type=UML2_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_EncapsulatedClassifier", type=UML2_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation452: BinaryAssociation = BinaryAssociation(
    name="operation452",
    ends={
        Property(name="UML2_Operation453", type=UML2_CallTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CallTrigger", type=UML2_Operation, multiplicity=Multiplicity(1, 1))
    }
)
includingCase427: BinaryAssociation = BinaryAssociation(
    name="includingCase427",
    ends={
        Property(name="UseCase428", type=UML2_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=UML2_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
addition429: BinaryAssociation = BinaryAssociation(
    name="addition429",
    ends={
        Property(name="UML2_UseCase430", type=UML2_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Include", type=UML2_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
type431: BinaryAssociation = BinaryAssociation(
    name="type431",
    ends={
        Property(name="UML2_Collaboration", type=UML2_CollaborationOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CollaborationOccurrence432", type=UML2_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
signal459: BinaryAssociation = BinaryAssociation(
    name="signal459",
    ends={
        Property(name="UML2_Signal", type=UML2_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Reception460", type=UML2_Signal, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute461: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute461",
    ends={
        Property(name="UML2_Property463", type=UML2_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Signal462", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal464: BinaryAssociation = BinaryAssociation(
    name="signal464",
    ends={
        Property(name="UML2_Signal465", type=UML2_SignalTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_SignalTrigger", type=UML2_Signal, multiplicity=Multiplicity(0, 9999))
    }
)
when466: BinaryAssociation = BinaryAssociation(
    name="when466",
    ends={
        Property(name="UML2_ValueSpecification467", type=UML2_TimeTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TimeTrigger", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scope468: BinaryAssociation = BinaryAssociation(
    name="scope468",
    ends={
        Property(name="StructuredActivityNode469", type=UML2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
variable470: BinaryAssociation = BinaryAssociation(
    name="variable470",
    ends={
        Property(name="Variable", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=UML2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeExpression454: BinaryAssociation = BinaryAssociation(
    name="changeExpression454",
    ends={
        Property(name="UML2_ValueSpecification455", type=UML2_ChangeTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ChangeTrigger", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
port456: BinaryAssociation = BinaryAssociation(
    name="port456",
    ends={
        Property(name="UML2_Port458", type=UML2_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Trigger457", type=UML2_Port, multiplicity=Multiplicity(0, 9999))
    }
)
clause476: BinaryAssociation = BinaryAssociation(
    name="clause476",
    ends={
        Property(name="UML2_Clause", type=UML2_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConditionalNode", type=UML2_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result477: BinaryAssociation = BinaryAssociation(
    name="result477",
    ends={
        Property(name="UML2_OutputPin479", type=UML2_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConditionalNode478", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test480: BinaryAssociation = BinaryAssociation(
    name="test480",
    ends={
        Property(name="UML2_ActivityNode482", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Clause481", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
body483: BinaryAssociation = BinaryAssociation(
    name="body483",
    ends={
        Property(name="UML2_ActivityNode485", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Clause484", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause487: BinaryAssociation = BinaryAssociation(
    name="predecessorClause487",
    ends={
        Property(name="Clause", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=UML2_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause489: BinaryAssociation = BinaryAssociation(
    name="successorClause489",
    ends={
        Property(name="Clause490", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=UML2_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider491: BinaryAssociation = BinaryAssociation(
    name="decider491",
    ends={
        Property(name="UML2_OutputPin493", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Clause492", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput494: BinaryAssociation = BinaryAssociation(
    name="bodyOutput494",
    ends={
        Property(name="UML2_OutputPin496", type=UML2_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Clause495", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart497: BinaryAssociation = BinaryAssociation(
    name="bodyPart497",
    ends={
        Property(name="UML2_ActivityNode498", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart499: BinaryAssociation = BinaryAssociation(
    name="setupPart499",
    ends={
        Property(name="UML2_ActivityNode501", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode500", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode471: BinaryAssociation = BinaryAssociation(
    name="containedNode471",
    ends={
        Property(name="ActivityNode472", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedEdge473: BinaryAssociation = BinaryAssociation(
    name="containedEdge473",
    ends={
        Property(name="ActivityEdge475", type=UML2_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode474", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyOutput514: BinaryAssociation = BinaryAssociation(
    name="bodyOutput514",
    ends={
        Property(name="UML2_OutputPin516", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode515", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput517: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput517",
    ends={
        Property(name="UML2_InputPin519", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode518", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeline520: BinaryAssociation = BinaryAssociation(
    name="lifeline520",
    ends={
        Property(name="Lifeline", type=UML2_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=UML2_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message521: BinaryAssociation = BinaryAssociation(
    name="message521",
    ends={
        Property(name="Message", type=UML2_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction522", type=UML2_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragment523: BinaryAssociation = BinaryAssociation(
    name="fragment523",
    ends={
        Property(name="InteractionFragment", type=UML2_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingInteraction", type=UML2_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate524: BinaryAssociation = BinaryAssociation(
    name="formalGate524",
    ends={
        Property(name="UML2_Gate", type=UML2_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interaction", type=UML2_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered525: BinaryAssociation = BinaryAssociation(
    name="covered525",
    ends={
        Property(name="Lifeline526", type=UML2_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=UML2_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering527: BinaryAssociation = BinaryAssociation(
    name="generalOrdering527",
    ends={
        Property(name="UML2_GeneralOrdering", type=UML2_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionFragment", type=UML2_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingInteraction528: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction528",
    ends={
        Property(name="Interaction", type=UML2_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment", type=UML2_Interaction, multiplicity=Multiplicity(0, 1))
    }
)
enclosingOperand529: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand529",
    ends={
        Property(name="InteractionOperand", type=UML2_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragment530", type=UML2_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
decider502: BinaryAssociation = BinaryAssociation(
    name="decider502",
    ends={
        Property(name="UML2_OutputPin504", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode503", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test505: BinaryAssociation = BinaryAssociation(
    name="test505",
    ends={
        Property(name="UML2_ActivityNode507", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode506", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
result508: BinaryAssociation = BinaryAssociation(
    name="result508",
    ends={
        Property(name="UML2_OutputPin510", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode509", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable511: BinaryAssociation = BinaryAssociation(
    name="loopVariable511",
    ends={
        Property(name="UML2_OutputPin513", type=UML2_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LoopNode512", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coveredBy531: BinaryAssociation = BinaryAssociation(
    name="coveredBy531",
    ends={
        Property(name="covered", type=UML2_InteractionFragment, multiplicity=Multiplicity(0, 9999)),
        Property(name="InteractionFragment532", type=UML2_Lifeline, multiplicity=Multiplicity(1, 1))
    }
)
represents533: BinaryAssociation = BinaryAssociation(
    name="represents533",
    ends={
        Property(name="UML2_ConnectableElement534", type=UML2_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Lifeline", type=UML2_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
interaction535: BinaryAssociation = BinaryAssociation(
    name="interaction535",
    ends={
        Property(name="Interaction536", type=UML2_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="lifeline", type=UML2_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
selector537: BinaryAssociation = BinaryAssociation(
    name="selector537",
    ends={
        Property(name="UML2_OpaqueExpression539", type=UML2_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Lifeline538", type=UML2_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs540: BinaryAssociation = BinaryAssociation(
    name="decomposedAs540",
    ends={
        Property(name="UML2_PartDecomposition", type=UML2_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Lifeline541", type=UML2_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent543: BinaryAssociation = BinaryAssociation(
    name="sendEvent543",
    ends={
        Property(name="MessageEnd544", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sendMessage", type=UML2_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
connector545: BinaryAssociation = BinaryAssociation(
    name="connector545",
    ends={
        Property(name="UML2_Connector546", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Message", type=UML2_Connector, multiplicity=Multiplicity(0, 1))
    }
)
interaction547: BinaryAssociation = BinaryAssociation(
    name="interaction547",
    ends={
        Property(name="Interaction548", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=UML2_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
signature549: BinaryAssociation = BinaryAssociation(
    name="signature549",
    ends={
        Property(name="UML2_NamedElement551", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Message550", type=UML2_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
argument552: BinaryAssociation = BinaryAssociation(
    name="argument552",
    ends={
        Property(name="UML2_ValueSpecification554", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Message553", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiveEvent542: BinaryAssociation = BinaryAssociation(
    name="receiveEvent542",
    ends={
        Property(name="MessageEnd", type=UML2_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="receiveMessage", type=UML2_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
receiveMessage558: BinaryAssociation = BinaryAssociation(
    name="receiveMessage558",
    ends={
        Property(name="Message559", type=UML2_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="receiveEvent", type=UML2_Message, multiplicity=Multiplicity(0, 1))
    }
)
sendMessage560: BinaryAssociation = BinaryAssociation(
    name="sendMessage560",
    ends={
        Property(name="Message561", type=UML2_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sendEvent", type=UML2_Message, multiplicity=Multiplicity(0, 1))
    }
)
startExec562: BinaryAssociation = BinaryAssociation(
    name="startExec562",
    ends={
        Property(name="ExecutionOccurrence", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="start", type=UML2_ExecutionOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
before555: BinaryAssociation = BinaryAssociation(
    name="before555",
    ends={
        Property(name="EventOccurrence", type=UML2_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toAfter", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
after556: BinaryAssociation = BinaryAssociation(
    name="after556",
    ends={
        Property(name="EventOccurrence557", type=UML2_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="toBefore", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
toBefore566: BinaryAssociation = BinaryAssociation(
    name="toBefore566",
    ends={
        Property(name="GeneralOrdering567", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="after", type=UML2_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
start568: BinaryAssociation = BinaryAssociation(
    name="start568",
    ends={
        Property(name="EventOccurrence569", type=UML2_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="startExec", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
finish570: BinaryAssociation = BinaryAssociation(
    name="finish570",
    ends={
        Property(name="EventOccurrence571", type=UML2_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="finishExec", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
behavior572: BinaryAssociation = BinaryAssociation(
    name="behavior572",
    ends={
        Property(name="UML2_Behavior573", type=UML2_ExecutionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ExecutionOccurrence", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
invariant574: BinaryAssociation = BinaryAssociation(
    name="invariant574",
    ends={
        Property(name="UML2_Constraint575", type=UML2_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StateInvariant", type=UML2_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finishExec563: BinaryAssociation = BinaryAssociation(
    name="finishExec563",
    ends={
        Property(name="ExecutionOccurrence564", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="finish", type=UML2_ExecutionOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
toAfter565: BinaryAssociation = BinaryAssociation(
    name="toAfter565",
    ends={
        Property(name="GeneralOrdering", type=UML2_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="before", type=UML2_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter577: BinaryAssociation = BinaryAssociation(
    name="ownedParameter577",
    ends={
        Property(name="TemplateParameter", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=UML2_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedSignature579: BinaryAssociation = BinaryAssociation(
    name="nestedSignature579",
    ends={
        Property(name="TemplateSignature", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingSignature", type=UML2_TemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
nestingSignature581: BinaryAssociation = BinaryAssociation(
    name="nestingSignature581",
    ends={
        Property(name="TemplateSignature582", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedSignature", type=UML2_TemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
template583: BinaryAssociation = BinaryAssociation(
    name="template583",
    ends={
        Property(name="TemplateableElement", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=UML2_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature584: BinaryAssociation = BinaryAssociation(
    name="signature584",
    ends={
        Property(name="TemplateSignature586", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter585", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameteredElement587: BinaryAssociation = BinaryAssociation(
    name="parameteredElement587",
    ends={
        Property(name="ParameterableElement", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=UML2_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
parameter576: BinaryAssociation = BinaryAssociation(
    name="parameter576",
    ends={
        Property(name="UML2_TemplateParameter", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateSignature", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
default590: BinaryAssociation = BinaryAssociation(
    name="default590",
    ends={
        Property(name="UML2_ParameterableElement", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateParameter591", type=UML2_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault592: BinaryAssociation = BinaryAssociation(
    name="ownedDefault592",
    ends={
        Property(name="UML2_ParameterableElement594", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateParameter593", type=UML2_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding595: BinaryAssociation = BinaryAssociation(
    name="templateBinding595",
    ends={
        Property(name="TemplateBinding", type=UML2_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=UML2_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature596: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature596",
    ends={
        Property(name="TemplateSignature597", type=UML2_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=UML2_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subExpression599: BinaryAssociation = BinaryAssociation(
    name="subExpression599",
    ends={
        Property(name="StringExpression", type=UML2_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=UML2_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningExpression601: BinaryAssociation = BinaryAssociation(
    name="owningExpression601",
    ends={
        Property(name="StringExpression602", type=UML2_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=UML2_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameteredElement588: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement588",
    ends={
        Property(name="ParameterableElement589", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningParameter", type=UML2_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningParameter605: BinaryAssociation = BinaryAssociation(
    name="owningParameter605",
    ends={
        Property(name="TemplateParameter606", type=UML2_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameteredElement", type=UML2_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
boundElement607: BinaryAssociation = BinaryAssociation(
    name="boundElement607",
    ends={
        Property(name="TemplateableElement608", type=UML2_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=UML2_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature609: BinaryAssociation = BinaryAssociation(
    name="signature609",
    ends={
        Property(name="UML2_TemplateSignature610", type=UML2_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateBinding", type=UML2_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution611: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution611",
    ends={
        Property(name="TemplateParameterSubstitution", type=UML2_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding612", type=UML2_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formal613: BinaryAssociation = BinaryAssociation(
    name="formal613",
    ends={
        Property(name="UML2_TemplateParameter614", type=UML2_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateParameterSubstitution", type=UML2_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
templateParameter603: BinaryAssociation = BinaryAssociation(
    name="templateParameter603",
    ends={
        Property(name="TemplateParameter604", type=UML2_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=UML2_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
ownedActual620: BinaryAssociation = BinaryAssociation(
    name="ownedActual620",
    ends={
        Property(name="UML2_ParameterableElement622", type=UML2_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateParameterSubstitution621", type=UML2_ParameterableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateBinding615: BinaryAssociation = BinaryAssociation(
    name="templateBinding615",
    ends={
        Property(name="TemplateBinding616", type=UML2_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=UML2_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
actual617: BinaryAssociation = BinaryAssociation(
    name="actual617",
    ends={
        Property(name="UML2_ParameterableElement619", type=UML2_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TemplateParameterSubstitution618", type=UML2_ParameterableElement, multiplicity=Multiplicity(1, 9999))
    }
)
containedEdge625: BinaryAssociation = BinaryAssociation(
    name="containedEdge625",
    ends={
        Property(name="ActivityEdge626", type=UML2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode627: BinaryAssociation = BinaryAssociation(
    name="containedNode627",
    ends={
        Property(name="ActivityNode629", type=UML2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="inPartition628", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
subgroup631: BinaryAssociation = BinaryAssociation(
    name="subgroup631",
    ends={
        Property(name="ActivityPartition632", type=UML2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="superPartition", type=UML2_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinSpec623: BinaryAssociation = BinaryAssociation(
    name="joinSpec623",
    ends={
        Property(name="UML2_ValueSpecification624", type=UML2_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_JoinNode", type=UML2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
regionAsOutput638: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput638",
    ends={
        Property(name="ExpansionRegion", type=UML2_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=UML2_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput639: BinaryAssociation = BinaryAssociation(
    name="regionAsInput639",
    ends={
        Property(name="ExpansionRegion640", type=UML2_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=UML2_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
superPartition634: BinaryAssociation = BinaryAssociation(
    name="superPartition634",
    ends={
        Property(name="ActivityPartition635", type=UML2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="subgroup", type=UML2_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents636: BinaryAssociation = BinaryAssociation(
    name="represents636",
    ends={
        Property(name="UML2_Element637", type=UML2_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ActivityPartition", type=UML2_Element, multiplicity=Multiplicity(0, 1))
    }
)
protectedNode644: BinaryAssociation = BinaryAssociation(
    name="protectedNode644",
    ends={
        Property(name="ExecutableNode", type=UML2_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handler", type=UML2_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
handlerBody645: BinaryAssociation = BinaryAssociation(
    name="handlerBody645",
    ends={
        Property(name="UML2_ExecutableNode", type=UML2_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ExceptionHandler", type=UML2_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput646: BinaryAssociation = BinaryAssociation(
    name="exceptionInput646",
    ends={
        Property(name="UML2_ObjectNode648", type=UML2_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ExceptionHandler647", type=UML2_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType649: BinaryAssociation = BinaryAssociation(
    name="exceptionType649",
    ends={
        Property(name="UML2_Classifier651", type=UML2_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ExceptionHandler650", type=UML2_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
refersTo652: BinaryAssociation = BinaryAssociation(
    name="refersTo652",
    ends={
        Property(name="UML2_Interaction653", type=UML2_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionOccurrence", type=UML2_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
actualGate654: BinaryAssociation = BinaryAssociation(
    name="actualGate654",
    ends={
        Property(name="UML2_Gate656", type=UML2_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionOccurrence655", type=UML2_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument657: BinaryAssociation = BinaryAssociation(
    name="argument657",
    ends={
        Property(name="UML2_InputPin659", type=UML2_InteractionOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionOccurrence658", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard660: BinaryAssociation = BinaryAssociation(
    name="guard660",
    ends={
        Property(name="UML2_InteractionConstraint", type=UML2_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionOperand", type=UML2_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputElement641: BinaryAssociation = BinaryAssociation(
    name="outputElement641",
    ends={
        Property(name="ExpansionNode", type=UML2_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=UML2_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement642: BinaryAssociation = BinaryAssociation(
    name="inputElement642",
    ends={
        Property(name="ExpansionNode643", type=UML2_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=UML2_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
operand669: BinaryAssociation = BinaryAssociation(
    name="operand669",
    ends={
        Property(name="UML2_InteractionOperand670", type=UML2_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CombinedFragment", type=UML2_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cfragmentGate671: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate671",
    ends={
        Property(name="UML2_Gate673", type=UML2_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CombinedFragment672", type=UML2_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region674: BinaryAssociation = BinaryAssociation(
    name="region674",
    ends={
        Property(name="Region", type=UML2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=UML2_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint675: BinaryAssociation = BinaryAssociation(
    name="connectionPoint675",
    ends={
        Property(name="UML2_Pseudostate", type=UML2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StateMachine", type=UML2_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedStateMachine677: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine677",
    ends={
        Property(name="UML2_StateMachine678", type=UML2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StateMachine676", type=UML2_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
fragment661: BinaryAssociation = BinaryAssociation(
    name="fragment661",
    ends={
        Property(name="InteractionFragment662", type=UML2_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="enclosingOperand", type=UML2_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minint663: BinaryAssociation = BinaryAssociation(
    name="minint663",
    ends={
        Property(name="UML2_ValueSpecification665", type=UML2_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionConstraint664", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
maxint666: BinaryAssociation = BinaryAssociation(
    name="maxint666",
    ends={
        Property(name="UML2_ValueSpecification668", type=UML2_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InteractionConstraint667", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state686: BinaryAssociation = BinaryAssociation(
    name="state686",
    ends={
        Property(name="State", type=UML2_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region687", type=UML2_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion689: BinaryAssociation = BinaryAssociation(
    name="extendedRegion689",
    ends={
        Property(name="UML2_Region", type=UML2_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Region688", type=UML2_Region, multiplicity=Multiplicity(0, 1))
    }
)
submachine690: BinaryAssociation = BinaryAssociation(
    name="submachine690",
    ends={
        Property(name="UML2_StateMachine692", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State691", type=UML2_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
connection693: BinaryAssociation = BinaryAssociation(
    name="connection693",
    ends={
        Property(name="UML2_ConnectionPointReference", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State694", type=UML2_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState696: BinaryAssociation = BinaryAssociation(
    name="redefinedState696",
    ends={
        Property(name="UML2_State697", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State695", type=UML2_State, multiplicity=Multiplicity(0, 1))
    }
)
deferrableTrigger698: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger698",
    ends={
        Property(name="UML2_Trigger700", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State699", type=UML2_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
region701: BinaryAssociation = BinaryAssociation(
    name="region701",
    ends={
        Property(name="Region702", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=UML2_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine_redefinitionContext679: BinaryAssociation = BinaryAssociation(
    name="stateMachine_redefinitionContext679",
    ends={
        Property(name="BehavioredClassifier680", type=UML2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStateMachine", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
subvertex681: BinaryAssociation = BinaryAssociation(
    name="subvertex681",
    ends={
        Property(name="Vertex", type=UML2_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=UML2_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition682: BinaryAssociation = BinaryAssociation(
    name="transition682",
    ends={
        Property(name="Transition", type=UML2_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container683", type=UML2_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine684: BinaryAssociation = BinaryAssociation(
    name="stateMachine684",
    ends={
        Property(name="StateMachine685", type=UML2_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=UML2_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
container715: BinaryAssociation = BinaryAssociation(
    name="container715",
    ends={
        Property(name="Region716", type=UML2_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=UML2_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing717: BinaryAssociation = BinaryAssociation(
    name="outgoing717",
    ends={
        Property(name="Transition719", type=UML2_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source718", type=UML2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming720: BinaryAssociation = BinaryAssociation(
    name="incoming720",
    ends={
        Property(name="Transition722", type=UML2_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target721", type=UML2_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry723: BinaryAssociation = BinaryAssociation(
    name="entry723",
    ends={
        Property(name="UML2_Pseudostate725", type=UML2_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConnectionPointReference724", type=UML2_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit726: BinaryAssociation = BinaryAssociation(
    name="exit726",
    ends={
        Property(name="UML2_Pseudostate728", type=UML2_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ConnectionPointReference727", type=UML2_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
container729: BinaryAssociation = BinaryAssociation(
    name="container729",
    ends={
        Property(name="Region730", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=UML2_Region, multiplicity=Multiplicity(1, 1))
    }
)
source731: BinaryAssociation = BinaryAssociation(
    name="source731",
    ends={
        Property(name="Vertex733", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing732", type=UML2_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target734: BinaryAssociation = BinaryAssociation(
    name="target734",
    ends={
        Property(name="Vertex736", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming735", type=UML2_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
redefinedTransition738: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition738",
    ends={
        Property(name="UML2_Transition", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Transition737", type=UML2_Transition, multiplicity=Multiplicity(0, 1))
    }
)
entry703: BinaryAssociation = BinaryAssociation(
    name="entry703",
    ends={
        Property(name="UML2_Activity705", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State704", type=UML2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit706: BinaryAssociation = BinaryAssociation(
    name="exit706",
    ends={
        Property(name="UML2_Activity708", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State707", type=UML2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity709: BinaryAssociation = BinaryAssociation(
    name="doActivity709",
    ends={
        Property(name="UML2_Activity711", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State710", type=UML2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant712: BinaryAssociation = BinaryAssociation(
    name="stateInvariant712",
    ends={
        Property(name="UML2_Constraint714", type=UML2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_State713", type=UML2_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier748: BinaryAssociation = BinaryAssociation(
    name="classifier748",
    ends={
        Property(name="UML2_Classifier749", type=UML2_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CreateObjectAction", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result750: BinaryAssociation = BinaryAssociation(
    name="result750",
    ends={
        Property(name="UML2_OutputPin752", type=UML2_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CreateObjectAction751", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target753: BinaryAssociation = BinaryAssociation(
    name="target753",
    ends={
        Property(name="UML2_InputPin754", type=UML2_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DestroyObjectAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first755: BinaryAssociation = BinaryAssociation(
    name="first755",
    ends={
        Property(name="UML2_InputPin756", type=UML2_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TestIdentityAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second757: BinaryAssociation = BinaryAssociation(
    name="second757",
    ends={
        Property(name="UML2_InputPin759", type=UML2_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TestIdentityAction758", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger739: BinaryAssociation = BinaryAssociation(
    name="trigger739",
    ends={
        Property(name="UML2_Trigger741", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Transition740", type=UML2_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
guard742: BinaryAssociation = BinaryAssociation(
    name="guard742",
    ends={
        Property(name="UML2_Constraint744", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Transition743", type=UML2_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect745: BinaryAssociation = BinaryAssociation(
    name="effect745",
    ends={
        Property(name="UML2_Activity747", type=UML2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Transition746", type=UML2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result760: BinaryAssociation = BinaryAssociation(
    name="result760",
    ends={
        Property(name="UML2_OutputPin762", type=UML2_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TestIdentityAction761", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result763: BinaryAssociation = BinaryAssociation(
    name="result763",
    ends={
        Property(name="UML2_OutputPin764", type=UML2_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadSelfAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature765: BinaryAssociation = BinaryAssociation(
    name="structuralFeature765",
    ends={
        Property(name="UML2_StructuralFeature766", type=UML2_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuralFeatureAction", type=UML2_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object767: BinaryAssociation = BinaryAssociation(
    name="object767",
    ends={
        Property(name="UML2_InputPin769", type=UML2_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StructuralFeatureAction768", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result770: BinaryAssociation = BinaryAssociation(
    name="result770",
    ends={
        Property(name="UML2_OutputPin771", type=UML2_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadStructuralFeatureAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value772: BinaryAssociation = BinaryAssociation(
    name="value772",
    ends={
        Property(name="UML2_InputPin773", type=UML2_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_WriteStructuralFeatureAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier783: BinaryAssociation = BinaryAssociation(
    name="qualifier783",
    ends={
        Property(name="UML2_QualifierValue", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData784", type=UML2_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result785: BinaryAssociation = BinaryAssociation(
    name="result785",
    ends={
        Property(name="UML2_OutputPin786", type=UML2_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt787: BinaryAssociation = BinaryAssociation(
    name="insertAt787",
    ends={
        Property(name="UML2_InputPin788", type=UML2_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndCreationData", type=UML2_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
object789: BinaryAssociation = BinaryAssociation(
    name="object789",
    ends={
        Property(name="UML2_InputPin790", type=UML2_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ClearAssociationAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association791: BinaryAssociation = BinaryAssociation(
    name="association791",
    ends={
        Property(name="UML2_Association793", type=UML2_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ClearAssociationAction792", type=UML2_Association, multiplicity=Multiplicity(1, 1))
    }
)
variable794: BinaryAssociation = BinaryAssociation(
    name="variable794",
    ends={
        Property(name="UML2_Variable", type=UML2_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_VariableAction", type=UML2_Variable, multiplicity=Multiplicity(1, 1))
    }
)
insertAt774: BinaryAssociation = BinaryAssociation(
    name="insertAt774",
    ends={
        Property(name="UML2_InputPin775", type=UML2_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_AddStructuralFeatureValueAction", type=UML2_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endData776: BinaryAssociation = BinaryAssociation(
    name="endData776",
    ends={
        Property(name="UML2_LinkEndData", type=UML2_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkAction", type=UML2_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value777: BinaryAssociation = BinaryAssociation(
    name="value777",
    ends={
        Property(name="UML2_InputPin779", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData778", type=UML2_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end780: BinaryAssociation = BinaryAssociation(
    name="end780",
    ends={
        Property(name="UML2_Property782", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData781", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
insertAt799: BinaryAssociation = BinaryAssociation(
    name="insertAt799",
    ends={
        Property(name="UML2_InputPin800", type=UML2_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_AddVariableValueAction", type=UML2_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function801: BinaryAssociation = BinaryAssociation(
    name="function801",
    ends={
        Property(name="UML2_PrimitiveFunction", type=UML2_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ApplyFunctionAction", type=UML2_PrimitiveFunction, multiplicity=Multiplicity(1, 1))
    }
)
argument802: BinaryAssociation = BinaryAssociation(
    name="argument802",
    ends={
        Property(name="UML2_InputPin804", type=UML2_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ApplyFunctionAction803", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result805: BinaryAssociation = BinaryAssociation(
    name="result805",
    ends={
        Property(name="UML2_OutputPin807", type=UML2_ApplyFunctionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ApplyFunctionAction806", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result808: BinaryAssociation = BinaryAssociation(
    name="result808",
    ends={
        Property(name="UML2_OutputPin809", type=UML2_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CallAction", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument810: BinaryAssociation = BinaryAssociation(
    name="argument810",
    ends={
        Property(name="UML2_InputPin811", type=UML2_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InvocationAction", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result795: BinaryAssociation = BinaryAssociation(
    name="result795",
    ends={
        Property(name="UML2_OutputPin796", type=UML2_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadVariableAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value797: BinaryAssociation = BinaryAssociation(
    name="value797",
    ends={
        Property(name="UML2_InputPin798", type=UML2_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_WriteVariableAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target822: BinaryAssociation = BinaryAssociation(
    name="target822",
    ends={
        Property(name="UML2_InputPin823", type=UML2_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_SendObjectAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request824: BinaryAssociation = BinaryAssociation(
    name="request824",
    ends={
        Property(name="UML2_InputPin826", type=UML2_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_SendObjectAction825", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation827: BinaryAssociation = BinaryAssociation(
    name="operation827",
    ends={
        Property(name="UML2_Operation828", type=UML2_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CallOperationAction", type=UML2_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target829: BinaryAssociation = BinaryAssociation(
    name="target829",
    ends={
        Property(name="UML2_InputPin831", type=UML2_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CallOperationAction830", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
behavior832: BinaryAssociation = BinaryAssociation(
    name="behavior832",
    ends={
        Property(name="UML2_Behavior833", type=UML2_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CallBehaviorAction", type=UML2_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
event834: BinaryAssociation = BinaryAssociation(
    name="event834",
    ends={
        Property(name="UML2_NamedElement835", type=UML2_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TimeExpression", type=UML2_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
event836: BinaryAssociation = BinaryAssociation(
    name="event836",
    ends={
        Property(name="UML2_NamedElement837", type=UML2_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Duration", type=UML2_NamedElement, multiplicity=Multiplicity(0, 2))
    }
)
onPort812: BinaryAssociation = BinaryAssociation(
    name="onPort812",
    ends={
        Property(name="UML2_Port814", type=UML2_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_InvocationAction813", type=UML2_Port, multiplicity=Multiplicity(0, 1))
    }
)
target815: BinaryAssociation = BinaryAssociation(
    name="target815",
    ends={
        Property(name="UML2_InputPin816", type=UML2_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_SendSignalAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal817: BinaryAssociation = BinaryAssociation(
    name="signal817",
    ends={
        Property(name="UML2_Signal819", type=UML2_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_SendSignalAction818", type=UML2_Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal820: BinaryAssociation = BinaryAssociation(
    name="signal820",
    ends={
        Property(name="UML2_Signal821", type=UML2_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BroadcastSignalAction", type=UML2_Signal, multiplicity=Multiplicity(1, 1))
    }
)
duration845: BinaryAssociation = BinaryAssociation(
    name="duration845",
    ends={
        Property(name="UML2_Duration846", type=UML2_DurationObservationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DurationObservationAction", type=UML2_Duration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge847: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge847",
    ends={
        Property(name="ActivityEdge848", type=UML2_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="interrupts", type=UML2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode849: BinaryAssociation = BinaryAssociation(
    name="containedNode849",
    ends={
        Property(name="ActivityNode850", type=UML2_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="inInterruptibleRegion", type=UML2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parameter851: BinaryAssociation = BinaryAssociation(
    name="parameter851",
    ends={
        Property(name="Parameter852", type=UML2_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSet", type=UML2_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
now838: BinaryAssociation = BinaryAssociation(
    name="now838",
    ends={
        Property(name="UML2_TimeExpression839", type=UML2_TimeObservationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TimeObservationAction", type=UML2_TimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
min840: BinaryAssociation = BinaryAssociation(
    name="min840",
    ends={
        Property(name="UML2_ValueSpecification841", type=UML2_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interval", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
max842: BinaryAssociation = BinaryAssociation(
    name="max842",
    ends={
        Property(name="UML2_ValueSpecification844", type=UML2_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Interval843", type=UML2_ValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember862: BinaryAssociation = BinaryAssociation(
    name="ownedMember862",
    ends={
        Property(name="UML2_PackageableElement864", type=UML2_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Component863", type=UML2_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedArtifact865: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact865",
    ends={
        Property(name="UML2_DeployedArtifact", type=UML2_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Deployment", type=UML2_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
location866: BinaryAssociation = BinaryAssociation(
    name="location866",
    ends={
        Property(name="DeploymentTarget", type=UML2_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="deployment", type=UML2_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
configuration867: BinaryAssociation = BinaryAssociation(
    name="configuration867",
    ends={
        Property(name="UML2_DeploymentSpecification", type=UML2_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Deployment868", type=UML2_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployment869: BinaryAssociation = BinaryAssociation(
    name="deployment869",
    ends={
        Property(name="Deployment", type=UML2_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=UML2_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement870: BinaryAssociation = BinaryAssociation(
    name="deployedElement870",
    ends={
        Property(name="UML2_PackageableElement871", type=UML2_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DeploymentTarget", type=UML2_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
nestedNode873: BinaryAssociation = BinaryAssociation(
    name="nestedNode873",
    ends={
        Property(name="UML2_Node", type=UML2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Node872", type=UML2_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition853: BinaryAssociation = BinaryAssociation(
    name="condition853",
    ends={
        Property(name="UML2_Constraint855", type=UML2_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ParameterSet854", type=UML2_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required856: BinaryAssociation = BinaryAssociation(
    name="required856",
    ends={
        Property(name="UML2_Interface857", type=UML2_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Component", type=UML2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided858: BinaryAssociation = BinaryAssociation(
    name="provided858",
    ends={
        Property(name="UML2_Interface860", type=UML2_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Component859", type=UML2_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
realization861: BinaryAssociation = BinaryAssociation(
    name="realization861",
    ends={
        Property(name="Realization", type=UML2_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="abstraction", type=UML2_Realization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postCondition878: BinaryAssociation = BinaryAssociation(
    name="postCondition878",
    ends={
        Property(name="UML2_Constraint879", type=UML2_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ProtocolTransition", type=UML2_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred880: BinaryAssociation = BinaryAssociation(
    name="referred880",
    ends={
        Property(name="UML2_Operation882", type=UML2_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ProtocolTransition881", type=UML2_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
preCondition883: BinaryAssociation = BinaryAssociation(
    name="preCondition883",
    ends={
        Property(name="UML2_Constraint885", type=UML2_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ProtocolTransition884", type=UML2_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
result886: BinaryAssociation = BinaryAssociation(
    name="result886",
    ends={
        Property(name="UML2_OutputPin887", type=UML2_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadExtentAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier888: BinaryAssociation = BinaryAssociation(
    name="classifier888",
    ends={
        Property(name="UML2_Classifier890", type=UML2_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadExtentAction889", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
oldClassifier891: BinaryAssociation = BinaryAssociation(
    name="oldClassifier891",
    ends={
        Property(name="UML2_Classifier892", type=UML2_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReclassifyObjectAction", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier893: BinaryAssociation = BinaryAssociation(
    name="newClassifier893",
    ends={
        Property(name="UML2_Classifier895", type=UML2_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReclassifyObjectAction894", type=UML2_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specificMachine874: BinaryAssociation = BinaryAssociation(
    name="specificMachine874",
    ends={
        Property(name="ProtocolStateMachine", type=UML2_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="conformance", type=UML2_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine875: BinaryAssociation = BinaryAssociation(
    name="generalMachine875",
    ends={
        Property(name="UML2_ProtocolStateMachine876", type=UML2_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ProtocolConformance", type=UML2_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
conformance877: BinaryAssociation = BinaryAssociation(
    name="conformance877",
    ends={
        Property(name="ProtocolConformance", type=UML2_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="specificMachine", type=UML2_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object907: BinaryAssociation = BinaryAssociation(
    name="object907",
    ends={
        Property(name="UML2_InputPin908", type=UML2_StartOwnedBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_StartOwnedBehaviorAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier909: BinaryAssociation = BinaryAssociation(
    name="qualifier909",
    ends={
        Property(name="UML2_Property911", type=UML2_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_QualifierValue910", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
value912: BinaryAssociation = BinaryAssociation(
    name="value912",
    ends={
        Property(name="UML2_InputPin914", type=UML2_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_QualifierValue913", type=UML2_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
object915: BinaryAssociation = BinaryAssociation(
    name="object915",
    ends={
        Property(name="UML2_InputPin916", type=UML2_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end917: BinaryAssociation = BinaryAssociation(
    name="end917",
    ends={
        Property(name="UML2_Property919", type=UML2_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndAction918", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
result920: BinaryAssociation = BinaryAssociation(
    name="result920",
    ends={
        Property(name="UML2_OutputPin922", type=UML2_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndAction921", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object923: BinaryAssociation = BinaryAssociation(
    name="object923",
    ends={
        Property(name="UML2_InputPin924", type=UML2_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndQualifierAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object896: BinaryAssociation = BinaryAssociation(
    name="object896",
    ends={
        Property(name="UML2_InputPin898", type=UML2_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReclassifyObjectAction897", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier899: BinaryAssociation = BinaryAssociation(
    name="classifier899",
    ends={
        Property(name="UML2_Classifier900", type=UML2_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadIsClassifiedObjectAction", type=UML2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result901: BinaryAssociation = BinaryAssociation(
    name="result901",
    ends={
        Property(name="UML2_OutputPin903", type=UML2_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadIsClassifiedObjectAction902", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object904: BinaryAssociation = BinaryAssociation(
    name="object904",
    ends={
        Property(name="UML2_InputPin906", type=UML2_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadIsClassifiedObjectAction905", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger933: BinaryAssociation = BinaryAssociation(
    name="trigger933",
    ends={
        Property(name="UML2_Trigger934", type=UML2_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_AcceptEventAction", type=UML2_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
result935: BinaryAssociation = BinaryAssociation(
    name="result935",
    ends={
        Property(name="UML2_OutputPin937", type=UML2_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_AcceptEventAction936", type=UML2_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation938: BinaryAssociation = BinaryAssociation(
    name="returnInformation938",
    ends={
        Property(name="UML2_OutputPin939", type=UML2_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_AcceptCallAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
replyToCall940: BinaryAssociation = BinaryAssociation(
    name="replyToCall940",
    ends={
        Property(name="UML2_CallTrigger941", type=UML2_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReplyAction", type=UML2_CallTrigger, multiplicity=Multiplicity(1, 1))
    }
)
replyValue942: BinaryAssociation = BinaryAssociation(
    name="replyValue942",
    ends={
        Property(name="UML2_InputPin944", type=UML2_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReplyAction943", type=UML2_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation945: BinaryAssociation = BinaryAssociation(
    name="returnInformation945",
    ends={
        Property(name="UML2_InputPin947", type=UML2_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReplyAction946", type=UML2_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
exception948: BinaryAssociation = BinaryAssociation(
    name="exception948",
    ends={
        Property(name="UML2_InputPin949", type=UML2_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_RaiseExceptionAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
result925: BinaryAssociation = BinaryAssociation(
    name="result925",
    ends={
        Property(name="UML2_OutputPin927", type=UML2_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndQualifierAction926", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier928: BinaryAssociation = BinaryAssociation(
    name="qualifier928",
    ends={
        Property(name="UML2_Property930", type=UML2_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadLinkObjectEndQualifierAction929", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
result931: BinaryAssociation = BinaryAssociation(
    name="result931",
    ends={
        Property(name="UML2_OutputPin932", type=UML2_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_CreateLinkObjectAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_UML2_MultiplicityElement_Element = Generalization(general=Element, specific=UML2_MultiplicityElement)
gen_UML2_NamedElement_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_NamedElement)
gen_UML2_Namespace_NamedElement = Generalization(general=NamedElement, specific=UML2_Namespace)
gen_UML2_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_OpaqueExpression)
gen_UML2_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2_ValueSpecification)
gen_UML2_ValueSpecification_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_ValueSpecification)
gen_UML2_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2_Expression)
gen_UML2_Comment_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_Comment)
gen_UML2_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UML2_DirectedRelationship)
gen_UML2_Relationship_Element = Generalization(general=Element, specific=UML2_Relationship)
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2_Class)
gen_UML2_Type_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Type)
gen_UML2_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2_Property)
gen_UML2_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Property)
gen_UML2_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_Property)
gen_UML2_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Parameter)
gen_UML2_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2_Parameter)
gen_UML2_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Operation)
gen_UML2_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2_Operation)
gen_UML2_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Operation)
gen_UML2_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_Operation)
gen_UML2_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UML2_TypedElement)
gen_UML2_DataType_Classifier = Generalization(general=Classifier, specific=UML2_DataType)
gen_UML2_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Parameter)
gen_UML2_Package_Namespace = Generalization(general=Namespace, specific=UML2_Package)
gen_UML2_Package_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Package)
gen_UML2_Enumeration_DataType = Generalization(general=DataType, specific=UML2_Enumeration)
gen_UML2_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=UML2_EnumerationLiteral)
gen_UML2_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2_PrimitiveType)
gen_UML2_Classifier_Namespace = Generalization(general=Namespace, specific=UML2_Classifier)
gen_UML2_Classifier_Type = Generalization(general=Type, specific=UML2_Classifier)
gen_UML2_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Classifier)
gen_UML2_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Feature)
gen_UML2_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Constraint)
gen_UML2_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralBoolean)
gen_UML2_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_LiteralSpecification)
gen_UML2_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralString)
gen_UML2_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralNull)
gen_UML2_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralInteger)
gen_UML2_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralUnlimitedNatural)
gen_UML2_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UML2_BehavioralFeature)
gen_UML2_BehavioralFeature_Feature = Generalization(general=Feature, specific=UML2_BehavioralFeature)
gen_UML2_StructuralFeature_Feature = Generalization(general=Feature, specific=UML2_StructuralFeature)
gen_UML2_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2_StructuralFeature)
gen_UML2_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_StructuralFeature)
gen_UML2_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=UML2_InstanceSpecification)
gen_UML2_InstanceSpecification_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_InstanceSpecification)
gen_UML2_InstanceSpecification_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2_InstanceSpecification)
gen_UML2_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_RedefinableElement)
gen_UML2_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Generalization)
gen_UML2_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_PackageableElement)
gen_UML2_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_PackageableElement)
gen_UML2_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_ElementImport)
gen_UML2_Slot_Element = Generalization(general=Element, specific=UML2_Slot)
gen_UML2_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_InstanceValue)
gen_UML2_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_PackageMerge)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_Profile_Package = Generalization(general=Package, specific=UML2_Profile)
gen_UML2_ProfileApplication_PackageImport = Generalization(general=PackageImport, specific=UML2_ProfileApplication)
gen_UML2_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_PackageImport)
gen_UML2_Association_Classifier = Generalization(general=Classifier, specific=UML2_Association)
gen_UML2_Association_Relationship = Generalization(general=Relationship, specific=UML2_Association)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_BehavioredClassifier)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_Permission_Dependency = Generalization(general=Dependency, specific=UML2_Permission)
gen_UML2_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UML2_Dependency)
gen_UML2_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Dependency)
gen_UML2_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=UML2_GeneralizationSet)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2_InformationItem)
gen_UML2_InformationFlow_PackageableElement = Generalization(general=PackageableElement, specific=UML2_InformationFlow)
gen_UML2_InformationFlow_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_InformationFlow)
gen_UML2_Usage_Dependency = Generalization(general=Dependency, specific=UML2_Usage)
gen_UML2_Abstraction_Dependency = Generalization(general=Dependency, specific=UML2_Abstraction)
gen_UML2_Realization_Abstraction = Generalization(general=Abstraction, specific=UML2_Realization)
gen_UML2_Substitution_Realization = Generalization(general=Realization, specific=UML2_Substitution)
gen_UML2_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UML2_ConnectableElement)
gen_UML2_Connector_Feature = Generalization(general=Feature, specific=UML2_Connector)
gen_UML2_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_StructuredClassifier)
gen_UML2_Model_Package = Generalization(general=Package, specific=UML2_Model)
gen_UML2_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_ConnectorEnd)
gen_UML2_ConnectableElement_NamedElement = Generalization(general=NamedElement, specific=UML2_ConnectableElement)
gen_UML2_ActivityGroup_Element = Generalization(general=Element, specific=UML2_ActivityGroup)
gen_UML2_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ActivityEdge)
gen_UML2_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=UML2_Action)
gen_UML2_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ActivityNode)
gen_UML2_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ControlNode)
gen_UML2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2_ControlFlow)
gen_UML2_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=UML2_ObjectFlow)
gen_UML2_InitialNode_ControlNode = Generalization(general=ControlNode, specific=UML2_InitialNode)
gen_UML2_FinalNode_ControlNode = Generalization(general=ControlNode, specific=UML2_FinalNode)
gen_UML2_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2_ActivityFinalNode)
gen_UML2_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=UML2_DecisionNode)
gen_UML2_MergeNode_ControlNode = Generalization(general=ControlNode, specific=UML2_MergeNode)
gen_UML2_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ExecutableNode)
gen_UML2_OutputPin_Pin = Generalization(general=Pin, specific=UML2_OutputPin)
gen_UML2_InputPin_Pin = Generalization(general=Pin, specific=UML2_InputPin)
gen_UML2_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2_Pin)
gen_UML2_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Pin)
gen_UML2_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=UML2_ObjectNode)
gen_UML2_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2_ObjectNode)
gen_UML2_Implementation_Realization = Generalization(general=Realization, specific=UML2_Implementation)
gen_UML2_Artifact_Classifier = Generalization(general=Classifier, specific=UML2_Artifact)
gen_UML2_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=UML2_Artifact)
gen_UML2_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ActivityParameterNode)
gen_UML2_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2_ValuePin)
gen_UML2_Interface_Classifier = Generalization(general=Classifier, specific=UML2_Interface)
gen_UML2_Actor_Classifier = Generalization(general=Classifier, specific=UML2_Actor)
gen_UML2_Extend_NamedElement = Generalization(general=NamedElement, specific=UML2_Extend)
gen_UML2_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Extend)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_ExtensionPoint)
gen_UML2_Include_NamedElement = Generalization(general=NamedElement, specific=UML2_Include)
gen_UML2_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_Include)
gen_UML2_Manifestation_Abstraction = Generalization(general=Abstraction, specific=UML2_Manifestation)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_Collaboration)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_EncapsulatedClassifier)
gen_UML2_CallTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_CallTrigger)
gen_UML2_MessageTrigger_Trigger = Generalization(general=Trigger, specific=UML2_MessageTrigger)
gen_UML2_CollaborationOccurrence_NamedElement = Generalization(general=NamedElement, specific=UML2_CollaborationOccurrence)
gen_UML2_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Reception)
gen_UML2_Signal_Classifier = Generalization(general=Classifier, specific=UML2_Signal)
gen_UML2_SignalTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_SignalTrigger)
gen_UML2_TimeTrigger_Trigger = Generalization(general=Trigger, specific=UML2_TimeTrigger)
gen_UML2_AnyTrigger_MessageTrigger = Generalization(general=MessageTrigger, specific=UML2_AnyTrigger)
gen_UML2_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=UML2_Variable)
gen_UML2_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2_Variable)
gen_UML2_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Variable)
gen_UML2_StructuredActivityNode_Action = Generalization(general=Action, specific=UML2_StructuredActivityNode)
gen_UML2_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=UML2_StructuredActivityNode)
gen_UML2_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_StructuredActivityNode)
gen_UML2_ChangeTrigger_Trigger = Generalization(general=Trigger, specific=UML2_ChangeTrigger)
gen_UML2_Trigger_NamedElement = Generalization(general=NamedElement, specific=UML2_Trigger)
gen_UML2_Clause_Element = Generalization(general=Element, specific=UML2_Clause)
gen_UML2_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_LoopNode)
gen_UML2_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ConditionalNode)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_Interaction)
gen_UML2_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=UML2_InteractionFragment)
gen_UML2_Lifeline_NamedElement = Generalization(general=NamedElement, specific=UML2_Lifeline)
gen_UML2_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=UML2_GeneralOrdering)
gen_UML2_Message_NamedElement = Generalization(general=NamedElement, specific=UML2_Message)
gen_UML2_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=UML2_MessageEnd)
gen_UML2_EventOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_EventOccurrence)
gen_UML2_EventOccurrence_MessageEnd = Generalization(general=MessageEnd, specific=UML2_EventOccurrence)
gen_UML2_ExecutionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_ExecutionOccurrence)
gen_UML2_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_StateInvariant)
gen_UML2_TemplateParameter_Element = Generalization(general=Element, specific=UML2_TemplateParameter)
gen_UML2_Stop_EventOccurrence = Generalization(general=EventOccurrence, specific=UML2_Stop)
gen_UML2_TemplateSignature_Element = Generalization(general=Element, specific=UML2_TemplateSignature)
gen_UML2_TemplateableElement_Element = Generalization(general=Element, specific=UML2_TemplateableElement)
gen_UML2_StringExpression_TemplateableElement = Generalization(general=TemplateableElement, specific=UML2_StringExpression)
gen_UML2_TemplateBinding_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_TemplateBinding)
gen_UML2_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=UML2_TemplateParameterSubstitution)
gen_UML2_ParameterableElement_Element = Generalization(general=Element, specific=UML2_ParameterableElement)
gen_UML2_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_OperationTemplateParameter)
gen_UML2_ClassifierTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_ClassifierTemplateParameter)
gen_UML2_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_ParameterableClassifier)
gen_UML2_RedefinableTemplateSignature_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_RedefinableTemplateSignature)
gen_UML2_RedefinableTemplateSignature_TemplateSignature = Generalization(general=TemplateSignature, specific=UML2_RedefinableTemplateSignature)
gen_UML2_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_TemplateableClassifier)
gen_UML2_ConnectableElementTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=UML2_ConnectableElementTemplateParameter)
gen_UML2_ForkNode_ControlNode = Generalization(general=ControlNode, specific=UML2_ForkNode)
gen_UML2_JoinNode_ControlNode = Generalization(general=ControlNode, specific=UML2_JoinNode)
gen_UML2_ActivityPartition_NamedElement = Generalization(general=NamedElement, specific=UML2_ActivityPartition)
gen_UML2_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_ActivityPartition)
gen_UML2_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=UML2_FlowFinalNode)
gen_UML2_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_CentralBufferNode)
gen_UML2_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ExpansionNode)
gen_UML2_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ExpansionRegion)
gen_UML2_InteractionOccurrence_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_InteractionOccurrence)
gen_UML2_Gate_MessageEnd = Generalization(general=MessageEnd, specific=UML2_Gate)
gen_UML2_PartDecomposition_InteractionOccurrence = Generalization(general=InteractionOccurrence, specific=UML2_PartDecomposition)
gen_UML2_InteractionOperand_Namespace = Generalization(general=Namespace, specific=UML2_InteractionOperand)
gen_UML2_InteractionOperand_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_InteractionOperand)
gen_UML2_ExceptionHandler_Element = Generalization(general=Element, specific=UML2_ExceptionHandler)
gen_UML2_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_CombinedFragment)
gen_UML2_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=UML2_Continuation)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=UML2_InteractionConstraint)
gen_UML2_Pseudostate_Vertex = Generalization(general=Vertex, specific=UML2_Pseudostate)
gen_UML2_State_Namespace = Generalization(general=Namespace, specific=UML2_State)
gen_UML2_State_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_State)
gen_UML2_State_Vertex = Generalization(general=Vertex, specific=UML2_State)
gen_UML2_Region_Namespace = Generalization(general=Namespace, specific=UML2_Region)
gen_UML2_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Region)
gen_UML2_Vertex_NamedElement = Generalization(general=NamedElement, specific=UML2_Vertex)
gen_UML2_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=UML2_ConnectionPointReference)
gen_UML2_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=UML2_Transition)
gen_UML2_FinalState_State = Generalization(general=State, specific=UML2_FinalState)
gen_UML2_CreateObjectAction_Action = Generalization(general=Action, specific=UML2_CreateObjectAction)
gen_UML2_DestroyObjectAction_Action = Generalization(general=Action, specific=UML2_DestroyObjectAction)
gen_UML2_TestIdentityAction_Action = Generalization(general=Action, specific=UML2_TestIdentityAction)
gen_UML2_ReadSelfAction_Action = Generalization(general=Action, specific=UML2_ReadSelfAction)
gen_UML2_StructuralFeatureAction_Action = Generalization(general=Action, specific=UML2_StructuralFeatureAction)
gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ReadStructuralFeatureAction)
gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_WriteStructuralFeatureAction)
gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ClearStructuralFeatureAction)
gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_RemoveStructuralFeatureValueAction)
gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_AddStructuralFeatureValueAction)
gen_UML2_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_ReadLinkAction)
gen_UML2_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UML2_LinkEndCreationData)
gen_UML2_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_CreateLinkAction)
gen_UML2_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_WriteLinkAction)
gen_UML2_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_DestroyLinkAction)
gen_UML2_ClearAssociationAction_Action = Generalization(general=Action, specific=UML2_ClearAssociationAction)
gen_UML2_VariableAction_Action = Generalization(general=Action, specific=UML2_VariableAction)
gen_UML2_LinkAction_Action = Generalization(general=Action, specific=UML2_LinkAction)
gen_UML2_LinkEndData_Element = Generalization(general=Element, specific=UML2_LinkEndData)
gen_UML2_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_RemoveVariableValueAction)
gen_UML2_ApplyFunctionAction_Action = Generalization(general=Action, specific=UML2_ApplyFunctionAction)
gen_UML2_PrimitiveFunction_PackageableElement = Generalization(general=PackageableElement, specific=UML2_PrimitiveFunction)
gen_UML2_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_CallAction)
gen_UML2_InvocationAction_Action = Generalization(general=Action, specific=UML2_InvocationAction)
gen_UML2_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ReadVariableAction)
gen_UML2_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_WriteVariableAction)
gen_UML2_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ClearVariableAction)
gen_UML2_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_AddVariableValueAction)
gen_UML2_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendObjectAction)
gen_UML2_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UML2_CallOperationAction)
gen_UML2_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UML2_CallBehaviorAction)
gen_UML2_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_TimeExpression)
gen_UML2_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Duration)
gen_UML2_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendSignalAction)
gen_UML2_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_BroadcastSignalAction)
gen_UML2_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=UML2_IntervalConstraint)
gen_UML2_TimeInterval_Interval = Generalization(general=Interval, specific=UML2_TimeInterval)
gen_UML2_DurationObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_DurationObservationAction)
gen_UML2_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_DurationConstraint)
gen_UML2_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2_DataStoreNode)
gen_UML2_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=UML2_InterruptibleActivityRegion)
gen_UML2_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=UML2_ParameterSet)
gen_UML2_TimeObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_TimeObservationAction)
gen_UML2_DurationInterval_Interval = Generalization(general=Interval, specific=UML2_DurationInterval)
gen_UML2_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Interval)
gen_UML2_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=UML2_TimeConstraint)
gen_UML2_Deployment_Dependency = Generalization(general=Dependency, specific=UML2_Deployment)
gen_UML2_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=UML2_DeployedArtifact)
gen_UML2_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UML2_DeploymentTarget)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UML2_Node)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)
gen_UML2_ProtocolTransition_Transition = Generalization(general=Transition, specific=UML2_ProtocolTransition)
gen_UML2_ReadExtentAction_Action = Generalization(general=Action, specific=UML2_ReadExtentAction)
gen_UML2_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UML2_ReclassifyObjectAction)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UML2_ProtocolConformance)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_StartOwnedBehaviorAction_Action = Generalization(general=Action, specific=UML2_StartOwnedBehaviorAction)
gen_UML2_QualifierValue_Element = Generalization(general=Element, specific=UML2_QualifierValue)
gen_UML2_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndAction)
gen_UML2_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndQualifierAction)
gen_UML2_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UML2_ReadIsClassifiedObjectAction)
gen_UML2_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UML2_AcceptCallAction)
gen_UML2_ReplyAction_Action = Generalization(general=Action, specific=UML2_ReplyAction)
gen_UML2_RaiseExceptionAction_Action = Generalization(general=Action, specific=UML2_RaiseExceptionAction)
gen_UML2_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2_DeploymentSpecification)
gen_UML2_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UML2_CreateLinkObjectAction)
gen_UML2_AcceptEventAction_Action = Generalization(general=Action, specific=UML2_AcceptEventAction)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_Element, UML2_Comment, UML2_MultiplicityElement, Element, UML2_ValueSpecification, UML2_NamedElement, TemplateableElement, UML2_Dependency, UML2_StringExpression, UML2_Namespace, NamedElement, UML2_Constraint, UML2_PackageableElement, UML2_ElementImport, UML2_PackageImport, UML2_OpaqueExpression, ValueSpecification, UML2_Parameter, UML2_Behavior, TypedElement, ParameterableElement, UML2_Expression, OpaqueExpression, UML2_DirectedRelationship, Relationship, UML2_Relationship, UML2_Class, BehavioredClassifier, EncapsulatedClassifier, UML2_Operation, UML2_Extension, UML2_Classifier, UML2_Reception, UML2_Type, PackageableElement, UML2_Package, UML2_Property, StructuralFeature, ConnectableElement, DeploymentTarget, UML2_Association, UML2_DataType, BehavioralFeature, MultiplicityElement, UML2_TypedElement, UML2_ParameterSet, Namespace, UML2_PackageMerge, UML2_ProfileApplication, UML2_Enumeration, DataType, UML2_EnumerationLiteral, Classifier, UML2_CollaborationOccurrence, InstanceSpecification, UML2_PrimitiveType, Type, RedefinableElement, UML2_Feature, UML2_Generalization, UML2_Substitution, UML2_GeneralizationSet, UML2_UseCase, UML2_LiteralBoolean, LiteralSpecification, UML2_LiteralSpecification, UML2_LiteralString, UML2_LiteralNull, UML2_LiteralInteger, UML2_LiteralUnlimitedNatural, UML2_BehavioralFeature, Feature, UML2_StructuralFeature, UML2_InstanceSpecification, DeployedArtifact, UML2_Slot, DirectedRelationship, UML2_InstanceValue, UML2_RedefinableElement, UML2_Stereotype, Class_, UML2_Profile, Package, PackageImport, UML2_BehavioredClassifier, Association, UML2_ExtensionEnd, Property_, UML2_Activity, Behavior, UML2_ActivityEdge, UML2_ActivityGroup, UML2_ActivityNode, UML2_Action, UML2_StructuredActivityNode, UML2_Permission, Dependency, UML2_Implementation, UML2_Trigger, UML2_StateMachine, UML2_AssociationClass, UML2_InformationItem, UML2_InformationFlow, UML2_Usage, UML2_Abstraction, UML2_Realization, Abstraction, UML2_Component, Realization, UML2_Connector, UML2_StructuredClassifier, UML2_Model, UML2_ConnectorEnd, UML2_ConnectableElement, UML2_ActivityPartition, UML2_InterruptibleActivityRegion, ExecutableNode, UML2_OutputPin, UML2_InputPin, UML2_ControlNode, UML2_ControlFlow, ActivityEdge, UML2_ObjectFlow, UML2_InitialNode, ControlNode, UML2_FinalNode, UML2_ActivityFinalNode, FinalNode, UML2_DecisionNode, UML2_MergeNode, UML2_ExecutableNode, UML2_ExceptionHandler, Pin, UML2_Pin, ObjectNode, UML2_ObjectNode, ActivityNode, UML2_State, UML2_ProtocolStateMachine, UML2_Artifact, UML2_Manifestation, UML2_ActivityParameterNode, UML2_ValuePin, InputPin, UML2_Interface, UML2_Actor, UML2_Extend, UML2_ExtensionPoint, UML2_Include, StructuredClassifier, UML2_Port, UML2_EncapsulatedClassifier, UML2_CallTrigger, MessageTrigger, UML2_MessageTrigger, Trigger, UML2_Collaboration, UML2_Signal, UML2_SignalTrigger, UML2_TimeTrigger, UML2_AnyTrigger, UML2_Variable, Action, ActivityGroup, UML2_ChangeTrigger, UML2_Clause, UML2_LoopNode, UML2_ConditionalNode, StructuredActivityNode, UML2_Interaction, InteractionFragment, UML2_Lifeline, UML2_Message, UML2_InteractionFragment, UML2_Gate, UML2_GeneralOrdering, UML2_InteractionOperand, UML2_PartDecomposition, UML2_MessageEnd, MessageEnd, UML2_ExecutionOccurrence, UML2_EventOccurrence, UML2_StateInvariant, UML2_TemplateableElement, UML2_ParameterableElement, UML2_Stop, EventOccurrence, UML2_TemplateSignature, UML2_TemplateParameter, UML2_TemplateBinding, UML2_TemplateParameterSubstitution, UML2_OperationTemplateParameter, TemplateParameter, UML2_ClassifierTemplateParameter, UML2_ParameterableClassifier, UML2_RedefinableTemplateSignature, TemplateSignature, UML2_TemplateableClassifier, UML2_ConnectableElementTemplateParameter, UML2_ForkNode, UML2_JoinNode, UML2_FlowFinalNode, UML2_CentralBufferNode, UML2_ExpansionNode, UML2_ExpansionRegion, UML2_InteractionOccurrence, InteractionOccurrence, UML2_InteractionConstraint, UML2_CombinedFragment, UML2_Continuation, UML2_Region, UML2_Pseudostate, Constraint, Vertex, UML2_ConnectionPointReference, UML2_Vertex, UML2_Transition, UML2_FinalState, State, UML2_CreateObjectAction, UML2_DestroyObjectAction, UML2_TestIdentityAction, UML2_ReadSelfAction, UML2_StructuralFeatureAction, UML2_ReadStructuralFeatureAction, StructuralFeatureAction, UML2_WriteStructuralFeatureAction, UML2_ClearStructuralFeatureAction, UML2_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, UML2_AddStructuralFeatureValueAction, UML2_QualifierValue, UML2_ReadLinkAction, LinkAction, UML2_LinkEndCreationData, LinkEndData, UML2_CreateLinkAction, WriteLinkAction, UML2_WriteLinkAction, UML2_DestroyLinkAction, UML2_ClearAssociationAction, UML2_VariableAction, UML2_LinkAction, UML2_LinkEndData, UML2_RemoveVariableValueAction, UML2_ApplyFunctionAction, UML2_PrimitiveFunction, UML2_CallAction, InvocationAction, UML2_InvocationAction, UML2_ReadVariableAction, VariableAction, UML2_WriteVariableAction, UML2_ClearVariableAction, UML2_AddVariableValueAction, WriteVariableAction, UML2_SendObjectAction, UML2_CallOperationAction, CallAction, UML2_CallBehaviorAction, UML2_TimeExpression, UML2_Duration, UML2_SendSignalAction, UML2_BroadcastSignalAction, UML2_IntervalConstraint, UML2_TimeInterval, UML2_DurationObservationAction, UML2_DurationConstraint, UML2_DataStoreNode, CentralBufferNode, UML2_TimeObservationAction, UML2_DurationInterval, Interval, UML2_Interval, UML2_TimeConstraint, IntervalConstraint, UML2_Deployment, UML2_DeployedArtifact, UML2_DeploymentTarget, UML2_DeploymentSpecification, UML2_Node, UML2_ProtocolTransition, Transition, UML2_ReadExtentAction, UML2_ReclassifyObjectAction, UML2_Device, Node, UML2_ExecutionEnvironment, UML2_CommunicationPath, UML2_ProtocolConformance, StateMachine, UML2_StartOwnedBehaviorAction, UML2_ReadLinkObjectEndAction, UML2_ReadLinkObjectEndQualifierAction, UML2_ReadIsClassifiedObjectAction, UML2_AcceptCallAction, AcceptEventAction, UML2_ReplyAction, UML2_RaiseExceptionAction, Artifact, UML2_CreateLinkObjectAction, CreateLinkAction, UML2_AcceptEventAction, VisibilityKind, ParameterDirectionKind, AggregationKind, CallConcurrencyKind, MessageSort, MessageKind, ExpansionKind, InteractionOperator, TransitionKind, PseudostateKind, ParameterEffectKind, ObjectNodeOrderingKind, ConnectorKind},
    associations={member12, ownedElement1, owner3, ownedComment5, upperValue6, lowerValue7, clientDependency10, nameExpression11, ownedRule14, importedMember15, elementImport17, packageImport18, result20, behavior21, operand23, annotatedElement25, bodyExpression28, source31, target33, redefinedProperty54, relatedElement36, ownedOperation38, superClass40, extension41, nestedClassifier42, ownedReception44, package46, class_47, opposite50, owningAssociation52, type85, subsettedProperty57, datatype59, association60, defaultValue62, qualifier66, associationEnd68, ownedParameter70, class_71, datatype72, precondition75, postcondition76, redefinedOperation80, bodyCondition82, ownedAttribute107, operation86, defaultValue88, parameterSet91, nestedPackage93, nestingPackage96, ownedType98, ownedMember99, packageMerge101, appliedProfile102, packageExtension104, ownedLiteral106, representation132, ownedOperation109, enumeration112, feature113, inheritedMember114, general118, generalization120, attribute121, redefinedClassifier125, substitution127, powertypeExtent128, ownedUseCase129, useCase131, parameter148, occurrence134, featuringClassifier137, context138, namespace141, specification142, constrainedElement145, formalParameter150, returnResult153, raisedException156, method159, slot160, classifier161, specification163, redefinitionContext173, specific175, general177, generalizationSet179, importedElement182, importingNamespace184, owningInstance166, value167, definingFeature169, instance171, endType192, memberEnd194, mergingPackage196, mergedPackage198, ownedStereotype201, metaclassReference202, metamodelReference205, importedProfile208, importedPackage186, importingNamespace188, ownedEnd190, context213, redefinedBehavior215, specification217, parameter218, formalParameter221, returnResult224, precondition227, postcondition230, ownedParameterSet233, metaclass211, edge243, group244, node245, action247, structuredNode248, client250, supplier251, ownedBehavior235, classifierBehavior237, implementation239, ownedTrigger240, ownedStateMachine242, contract258, substitutingClassifier260, powertype262, generalization264, represented266, realization268, conveyed270, mapping253, abstraction255, realizingClassifier256, end279, type280, redefinedConnector283, end285, contract288, ownedAttribute291, part293, role296, ownedConnector298, definingEnd273, role275, partWithPort276, redefinedElement311, inStructuredNode313, inPartition314, weight316, interrupts319, superGroup321, activity301, source302, target304, inGroup306, guard307, activity331, redefinedElement334, inStructuredNode336, inPartition338, inInterruptibleRegion341, output344, input346, context_348, localPrecondition351, localPostcondition354, activityGroup_activity323, outgoing325, incoming327, inGroup329, selection361, transformation364, selection366, decisionInput369, handler371, upperBound357, inState359, ownedAttribute376, ownedOperation378, redefinedInterface382, nestedClassifier384, ownedReception387, protocol390, contract392, implementingClassifier394, nestedArtifact397, manifestation398, parameter372, value374, extendedCase409, extension411, condition413, extensionLocation416, include418, extend419, extensionPoint421, subject422, useCase425, ownedOperation400, ownedAttribute403, utilizedElement406, roleBinding433, collaborationRole436, required439, redefinedPort442, provided444, protocol447, ownedPort450, operation452, includingCase427, addition429, type431, signal459, ownedAttribute461, signal464, when466, scope468, variable470, changeExpression454, port456, clause476, result477, test480, body483, predecessorClause487, successorClause489, decider491, bodyOutput494, bodyPart497, setupPart499, containedNode471, containedEdge473, bodyOutput514, loopVariableInput517, lifeline520, message521, fragment523, formalGate524, covered525, generalOrdering527, enclosingInteraction528, enclosingOperand529, decider502, test505, result508, loopVariable511, coveredBy531, represents533, interaction535, selector537, decomposedAs540, sendEvent543, connector545, interaction547, signature549, argument552, receiveEvent542, receiveMessage558, sendMessage560, startExec562, before555, after556, toBefore566, start568, finish570, behavior572, invariant574, finishExec563, toAfter565, ownedParameter577, nestedSignature579, nestingSignature581, template583, signature584, parameteredElement587, parameter576, default590, ownedDefault592, templateBinding595, ownedTemplateSignature596, subExpression599, owningExpression601, ownedParameteredElement588, owningParameter605, boundElement607, signature609, parameterSubstitution611, formal613, templateParameter603, ownedActual620, templateBinding615, actual617, containedEdge625, containedNode627, subgroup631, joinSpec623, regionAsOutput638, regionAsInput639, superPartition634, represents636, protectedNode644, handlerBody645, exceptionInput646, exceptionType649, refersTo652, actualGate654, argument657, guard660, outputElement641, inputElement642, operand669, cfragmentGate671, region674, connectionPoint675, extendedStateMachine677, fragment661, minint663, maxint666, state686, extendedRegion689, submachine690, connection693, redefinedState696, deferrableTrigger698, region701, stateMachine_redefinitionContext679, subvertex681, transition682, stateMachine684, container715, outgoing717, incoming720, entry723, exit726, container729, source731, target734, redefinedTransition738, entry703, exit706, doActivity709, stateInvariant712, classifier748, result750, target753, first755, second757, trigger739, guard742, effect745, result760, result763, structuralFeature765, object767, result770, value772, qualifier783, result785, insertAt787, object789, association791, variable794, insertAt774, endData776, value777, end780, insertAt799, function801, argument802, result805, result808, argument810, result795, value797, target822, request824, operation827, target829, behavior832, event834, event836, onPort812, target815, signal817, signal820, duration845, interruptingEdge847, containedNode849, parameter851, now838, min840, max842, ownedMember862, deployedArtifact865, location866, configuration867, deployment869, deployedElement870, nestedNode873, condition853, required856, provided858, realization861, postCondition878, referred880, preCondition883, result886, classifier888, oldClassifier891, newClassifier893, specificMachine874, generalMachine875, conformance877, object907, qualifier909, value912, object915, end917, result920, object923, object896, classifier899, result901, object904, trigger933, result935, returnInformation938, replyToCall940, replyValue942, returnInformation945, exception948, result925, qualifier928, result931},
    generalizations={gen_UML2_MultiplicityElement_Element, gen_UML2_NamedElement_TemplateableElement, gen_UML2_Namespace_NamedElement, gen_UML2_OpaqueExpression_ValueSpecification, gen_UML2_ValueSpecification_TypedElement, gen_UML2_ValueSpecification_ParameterableElement, gen_UML2_Expression_OpaqueExpression, gen_UML2_Comment_TemplateableElement, gen_UML2_DirectedRelationship_Relationship, gen_UML2_Relationship_Element, gen_UML2_Class_BehavioredClassifier, gen_UML2_Class_EncapsulatedClassifier, gen_UML2_Type_PackageableElement, gen_UML2_Property_StructuralFeature, gen_UML2_Property_ConnectableElement, gen_UML2_Property_DeploymentTarget, gen_UML2_Parameter_ConnectableElement, gen_UML2_Parameter_TypedElement, gen_UML2_Operation_BehavioralFeature, gen_UML2_Operation_TypedElement, gen_UML2_Operation_MultiplicityElement, gen_UML2_Operation_ParameterableElement, gen_UML2_TypedElement_NamedElement, gen_UML2_DataType_Classifier, gen_UML2_Parameter_MultiplicityElement, gen_UML2_Package_Namespace, gen_UML2_Package_PackageableElement, gen_UML2_Enumeration_DataType, gen_UML2_EnumerationLiteral_InstanceSpecification, gen_UML2_PrimitiveType_DataType, gen_UML2_Classifier_Namespace, gen_UML2_Classifier_Type, gen_UML2_Classifier_RedefinableElement, gen_UML2_Feature_RedefinableElement, gen_UML2_Constraint_PackageableElement, gen_UML2_LiteralBoolean_LiteralSpecification, gen_UML2_LiteralSpecification_ValueSpecification, gen_UML2_LiteralString_LiteralSpecification, gen_UML2_LiteralNull_LiteralSpecification, gen_UML2_LiteralInteger_LiteralSpecification, gen_UML2_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2_BehavioralFeature_Namespace, gen_UML2_BehavioralFeature_Feature, gen_UML2_StructuralFeature_Feature, gen_UML2_StructuralFeature_TypedElement, gen_UML2_StructuralFeature_MultiplicityElement, gen_UML2_InstanceSpecification_PackageableElement, gen_UML2_InstanceSpecification_DeploymentTarget, gen_UML2_InstanceSpecification_DeployedArtifact, gen_UML2_RedefinableElement_NamedElement, gen_UML2_Generalization_DirectedRelationship, gen_UML2_PackageableElement_NamedElement, gen_UML2_PackageableElement_ParameterableElement, gen_UML2_ElementImport_DirectedRelationship, gen_UML2_Slot_Element, gen_UML2_InstanceValue_ValueSpecification, gen_UML2_PackageMerge_DirectedRelationship, gen_UML2_Stereotype_Class, gen_UML2_Profile_Package, gen_UML2_ProfileApplication_PackageImport, gen_UML2_PackageImport_DirectedRelationship, gen_UML2_Association_Classifier, gen_UML2_Association_Relationship, gen_UML2_Behavior_Class, gen_UML2_BehavioredClassifier_Classifier, gen_UML2_Extension_Association, gen_UML2_ExtensionEnd_Property, gen_UML2_Activity_Behavior, gen_UML2_Permission_Dependency, gen_UML2_Dependency_PackageableElement, gen_UML2_Dependency_DirectedRelationship, gen_UML2_GeneralizationSet_PackageableElement, gen_UML2_AssociationClass_Class, gen_UML2_AssociationClass_Association, gen_UML2_InformationItem_Classifier, gen_UML2_InformationFlow_PackageableElement, gen_UML2_InformationFlow_DirectedRelationship, gen_UML2_Usage_Dependency, gen_UML2_Abstraction_Dependency, gen_UML2_Realization_Abstraction, gen_UML2_Substitution_Realization, gen_UML2_ConnectableElement_ParameterableElement, gen_UML2_Connector_Feature, gen_UML2_StructuredClassifier_Classifier, gen_UML2_Model_Package, gen_UML2_ConnectorEnd_MultiplicityElement, gen_UML2_ConnectableElement_NamedElement, gen_UML2_ActivityGroup_Element, gen_UML2_ActivityEdge_RedefinableElement, gen_UML2_Action_ExecutableNode, gen_UML2_ActivityNode_RedefinableElement, gen_UML2_ControlNode_ActivityNode, gen_UML2_ControlFlow_ActivityEdge, gen_UML2_ObjectFlow_ActivityEdge, gen_UML2_InitialNode_ControlNode, gen_UML2_FinalNode_ControlNode, gen_UML2_ActivityFinalNode_FinalNode, gen_UML2_DecisionNode_ControlNode, gen_UML2_MergeNode_ControlNode, gen_UML2_ExecutableNode_ActivityNode, gen_UML2_OutputPin_Pin, gen_UML2_InputPin_Pin, gen_UML2_Pin_ObjectNode, gen_UML2_Pin_MultiplicityElement, gen_UML2_ObjectNode_ActivityNode, gen_UML2_ObjectNode_TypedElement, gen_UML2_Implementation_Realization, gen_UML2_Artifact_Classifier, gen_UML2_Artifact_DeployedArtifact, gen_UML2_ActivityParameterNode_ObjectNode, gen_UML2_ValuePin_InputPin, gen_UML2_Interface_Classifier, gen_UML2_Actor_Classifier, gen_UML2_Extend_NamedElement, gen_UML2_Extend_DirectedRelationship, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_ExtensionPoint_RedefinableElement, gen_UML2_Include_NamedElement, gen_UML2_Include_DirectedRelationship, gen_UML2_Manifestation_Abstraction, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_Collaboration_StructuredClassifier, gen_UML2_Port_Property, gen_UML2_EncapsulatedClassifier_StructuredClassifier, gen_UML2_CallTrigger_MessageTrigger, gen_UML2_MessageTrigger_Trigger, gen_UML2_CollaborationOccurrence_NamedElement, gen_UML2_Reception_BehavioralFeature, gen_UML2_Signal_Classifier, gen_UML2_SignalTrigger_MessageTrigger, gen_UML2_TimeTrigger_Trigger, gen_UML2_AnyTrigger_MessageTrigger, gen_UML2_Variable_ConnectableElement, gen_UML2_Variable_TypedElement, gen_UML2_Variable_MultiplicityElement, gen_UML2_StructuredActivityNode_Action, gen_UML2_StructuredActivityNode_Namespace, gen_UML2_StructuredActivityNode_ActivityGroup, gen_UML2_ChangeTrigger_Trigger, gen_UML2_Trigger_NamedElement, gen_UML2_Clause_Element, gen_UML2_LoopNode_StructuredActivityNode, gen_UML2_ConditionalNode_StructuredActivityNode, gen_UML2_Interaction_Behavior, gen_UML2_Interaction_InteractionFragment, gen_UML2_InteractionFragment_NamedElement, gen_UML2_Lifeline_NamedElement, gen_UML2_GeneralOrdering_NamedElement, gen_UML2_Message_NamedElement, gen_UML2_MessageEnd_NamedElement, gen_UML2_EventOccurrence_InteractionFragment, gen_UML2_EventOccurrence_MessageEnd, gen_UML2_ExecutionOccurrence_InteractionFragment, gen_UML2_StateInvariant_InteractionFragment, gen_UML2_TemplateParameter_Element, gen_UML2_Stop_EventOccurrence, gen_UML2_TemplateSignature_Element, gen_UML2_TemplateableElement_Element, gen_UML2_StringExpression_TemplateableElement, gen_UML2_TemplateBinding_DirectedRelationship, gen_UML2_TemplateParameterSubstitution_Element, gen_UML2_ParameterableElement_Element, gen_UML2_OperationTemplateParameter_TemplateParameter, gen_UML2_ClassifierTemplateParameter_TemplateParameter, gen_UML2_ParameterableClassifier_Classifier, gen_UML2_RedefinableTemplateSignature_RedefinableElement, gen_UML2_RedefinableTemplateSignature_TemplateSignature, gen_UML2_TemplateableClassifier_Classifier, gen_UML2_ConnectableElementTemplateParameter_TemplateParameter, gen_UML2_ForkNode_ControlNode, gen_UML2_JoinNode_ControlNode, gen_UML2_ActivityPartition_NamedElement, gen_UML2_ActivityPartition_ActivityGroup, gen_UML2_FlowFinalNode_FinalNode, gen_UML2_CentralBufferNode_ObjectNode, gen_UML2_ExpansionNode_ObjectNode, gen_UML2_ExpansionRegion_StructuredActivityNode, gen_UML2_InteractionOccurrence_InteractionFragment, gen_UML2_Gate_MessageEnd, gen_UML2_PartDecomposition_InteractionOccurrence, gen_UML2_InteractionOperand_Namespace, gen_UML2_InteractionOperand_InteractionFragment, gen_UML2_ExceptionHandler_Element, gen_UML2_CombinedFragment_InteractionFragment, gen_UML2_Continuation_InteractionFragment, gen_UML2_StateMachine_Behavior, gen_UML2_InteractionConstraint_Constraint, gen_UML2_Pseudostate_Vertex, gen_UML2_State_Namespace, gen_UML2_State_RedefinableElement, gen_UML2_State_Vertex, gen_UML2_Region_Namespace, gen_UML2_Region_RedefinableElement, gen_UML2_Vertex_NamedElement, gen_UML2_ConnectionPointReference_Vertex, gen_UML2_Transition_RedefinableElement, gen_UML2_FinalState_State, gen_UML2_CreateObjectAction_Action, gen_UML2_DestroyObjectAction_Action, gen_UML2_TestIdentityAction_Action, gen_UML2_ReadSelfAction_Action, gen_UML2_StructuralFeatureAction_Action, gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction, gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_ReadLinkAction_LinkAction, gen_UML2_LinkEndCreationData_LinkEndData, gen_UML2_CreateLinkAction_WriteLinkAction, gen_UML2_WriteLinkAction_LinkAction, gen_UML2_DestroyLinkAction_WriteLinkAction, gen_UML2_ClearAssociationAction_Action, gen_UML2_VariableAction_Action, gen_UML2_LinkAction_Action, gen_UML2_LinkEndData_Element, gen_UML2_RemoveVariableValueAction_WriteVariableAction, gen_UML2_ApplyFunctionAction_Action, gen_UML2_PrimitiveFunction_PackageableElement, gen_UML2_CallAction_InvocationAction, gen_UML2_InvocationAction_Action, gen_UML2_ReadVariableAction_VariableAction, gen_UML2_WriteVariableAction_VariableAction, gen_UML2_ClearVariableAction_VariableAction, gen_UML2_AddVariableValueAction_WriteVariableAction, gen_UML2_SendObjectAction_InvocationAction, gen_UML2_CallOperationAction_CallAction, gen_UML2_CallBehaviorAction_CallAction, gen_UML2_TimeExpression_ValueSpecification, gen_UML2_Duration_ValueSpecification, gen_UML2_SendSignalAction_InvocationAction, gen_UML2_BroadcastSignalAction_InvocationAction, gen_UML2_IntervalConstraint_Constraint, gen_UML2_TimeInterval_Interval, gen_UML2_DurationObservationAction_WriteStructuralFeatureAction, gen_UML2_DurationConstraint_IntervalConstraint, gen_UML2_DataStoreNode_CentralBufferNode, gen_UML2_InterruptibleActivityRegion_ActivityGroup, gen_UML2_ParameterSet_NamedElement, gen_UML2_TimeObservationAction_WriteStructuralFeatureAction, gen_UML2_DurationInterval_Interval, gen_UML2_Interval_ValueSpecification, gen_UML2_TimeConstraint_IntervalConstraint, gen_UML2_Deployment_Dependency, gen_UML2_DeployedArtifact_NamedElement, gen_UML2_DeploymentTarget_NamedElement, gen_UML2_Node_Class, gen_UML2_Node_DeploymentTarget, gen_UML2_Component_Class, gen_UML2_ProtocolTransition_Transition, gen_UML2_ReadExtentAction_Action, gen_UML2_ReclassifyObjectAction_Action, gen_UML2_Device_Node, gen_UML2_ExecutionEnvironment_Node, gen_UML2_CommunicationPath_Association, gen_UML2_ProtocolConformance_DirectedRelationship, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_StartOwnedBehaviorAction_Action, gen_UML2_QualifierValue_Element, gen_UML2_ReadLinkObjectEndAction_Action, gen_UML2_ReadLinkObjectEndQualifierAction_Action, gen_UML2_ReadIsClassifiedObjectAction_Action, gen_UML2_AcceptCallAction_AcceptEventAction, gen_UML2_ReplyAction_Action, gen_UML2_RaiseExceptionAction_Action, gen_UML2_DeploymentSpecification_Artifact, gen_UML2_CreateLinkObjectAction_CreateLinkAction, gen_UML2_AcceptEventAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)