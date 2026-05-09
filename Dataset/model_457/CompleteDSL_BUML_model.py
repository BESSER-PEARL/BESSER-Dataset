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
            EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package"),
			EnumerationLiteral(name="public")
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
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="external")
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
			EnumerationLiteral(name="break_"),
			EnumerationLiteral(name="par"),
			EnumerationLiteral(name="strict"),
			EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="critical"),
			EnumerationLiteral(name="neg"),
			EnumerationLiteral(name="assert_"),
			EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="consider")
    }
)

# Classes
NamedElement = Class(name="NamedElement")
CompleteDSLPckg_Element = Class(name="CompleteDSLPckg_Element", is_abstract=True)
CompleteDSLPckg_Comment = Class(name="CompleteDSLPckg_Comment")
CompleteDSLPckg_NamedElement = Class(name="CompleteDSLPckg_NamedElement", is_abstract=True)
Element = Class(name="Element")
CompleteDSLPckg_Namespace = Class(name="CompleteDSLPckg_Namespace")
CompleteDSLPckg_Dependency = Class(name="CompleteDSLPckg_Dependency")
CompleteDSLPckg_PackageableElement = Class(name="CompleteDSLPckg_PackageableElement")
CompleteDSLPckg_ElementImport = Class(name="CompleteDSLPckg_ElementImport")
CompleteDSLPckg_PackageImport = Class(name="CompleteDSLPckg_PackageImport")
CompleteDSLPckg_Constraint = Class(name="CompleteDSLPckg_Constraint")
DirectedRelationship = Class(name="DirectedRelationship")
CompleteDSLPckg_Package = Class(name="CompleteDSLPckg_Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
CompleteDSLPckg_Type = Class(name="CompleteDSLPckg_Type", is_abstract=True)
CompleteDSLPckg_PackageMerge = Class(name="CompleteDSLPckg_PackageMerge")
CompleteDSLPckg_Relationship = Class(name="CompleteDSLPckg_Relationship", is_abstract=True)
CompleteDSLPckg_DirectedRelationship = Class(name="CompleteDSLPckg_DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
CompleteDSLPckg_MultiplicityElement = Class(name="CompleteDSLPckg_MultiplicityElement", is_abstract=True)
CompleteDSLPckg_ValueSpecification = Class(name="CompleteDSLPckg_ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
CompleteDSLPckg_Slot = Class(name="CompleteDSLPckg_Slot")
CompleteDSLPckg_InstanceSpecification = Class(name="CompleteDSLPckg_InstanceSpecification")
CompleteDSLPckg_TypedElement = Class(name="CompleteDSLPckg_TypedElement", is_abstract=True)
CompleteDSLPckg_Expression = Class(name="CompleteDSLPckg_Expression")
ValueSpecification = Class(name="ValueSpecification")
CompleteDSLPckg_OpaqueExpression = Class(name="CompleteDSLPckg_OpaqueExpression")
CompleteDSLPckg_Parameter = Class(name="CompleteDSLPckg_Parameter")
CompleteDSLPckg_Behavior = Class(name="CompleteDSLPckg_Behavior", is_abstract=True)
CompleteDSLPckg_LiteralSpecification = Class(name="CompleteDSLPckg_LiteralSpecification", is_abstract=True)
CompleteDSLPckg_LiteralNull = Class(name="CompleteDSLPckg_LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
CompleteDSLPckg_LiteralBoolean = Class(name="CompleteDSLPckg_LiteralBoolean")
CompleteDSLPckg_LiteralInteger = Class(name="CompleteDSLPckg_LiteralInteger")
CompleteDSLPckg_LiteralReal = Class(name="CompleteDSLPckg_LiteralReal")
CompleteDSLPckg_LiteralString = Class(name="CompleteDSLPckg_LiteralString")
CompleteDSLPckg_LiteralUnilimitedNatural = Class(name="CompleteDSLPckg_LiteralUnilimitedNatural")
CompleteDSLPckg_InstanceValue = Class(name="CompleteDSLPckg_InstanceValue")
CompleteDSLPckg_Classifier = Class(name="CompleteDSLPckg_Classifier", is_abstract=True)
CompleteDSLPckg_StructuralFeature = Class(name="CompleteDSLPckg_StructuralFeature", is_abstract=True)
CompleteDSLPckg_RedefinableElement = Class(name="CompleteDSLPckg_RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
CompleteDSLPckg_Feature = Class(name="CompleteDSLPckg_Feature", is_abstract=True)
CompleteDSLPckg_Property = Class(name="CompleteDSLPckg_Property")
CompleteDSLPckg_Generalization = Class(name="CompleteDSLPckg_Generalization")
CompleteDSLPckg_Substitution = Class(name="CompleteDSLPckg_Substitution")
CompleteDSLPckg_GeneralizationSet = Class(name="CompleteDSLPckg_GeneralizationSet")
CompleteDSLPckg_CollaborationUse = Class(name="CompleteDSLPckg_CollaborationUse")
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
CompleteDSLPckg_Class = Class(name="CompleteDSLPckg_Class")
CompleteDSLPckg_Association = Class(name="CompleteDSLPckg_Association")
CompleteDSLPckg_DataType = Class(name="CompleteDSLPckg_DataType")
CompleteDSLPckg_Interface = Class(name="CompleteDSLPckg_Interface")
CompleteDSLPckg_BehavioralFeature = Class(name="CompleteDSLPckg_BehavioralFeature", is_abstract=True)
CompleteDSLPckg_Operation = Class(name="CompleteDSLPckg_Operation")
BehavioralFeature = Class(name="BehavioralFeature")
Classifier = Class(name="Classifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
CompleteDSLPckg_Reception = Class(name="CompleteDSLPckg_Reception")
CompleteDSLPckg_PrimitiveType = Class(name="CompleteDSLPckg_PrimitiveType")
DataType = Class(name="DataType")
CompleteDSLPckg_Enumeration = Class(name="CompleteDSLPckg_Enumeration")
CompleteDSLPckg_EnumerationLiteral = Class(name="CompleteDSLPckg_EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
CompleteDSLPckg_Usage = Class(name="CompleteDSLPckg_Usage")
Dependency = Class(name="Dependency")
CompleteDSLPckg_Abstraction = Class(name="CompleteDSLPckg_Abstraction")
CompleteDSLPckg_Realization = Class(name="CompleteDSLPckg_Realization")
Abstraction = Class(name="Abstraction")
Realization = Class(name="Realization")
CompleteDSLPckg_InterfaceRealization = Class(name="CompleteDSLPckg_InterfaceRealization")
CompleteDSLPckg_BehavioredClassifier = Class(name="CompleteDSLPckg_BehavioredClassifier", is_abstract=True)
CompleteDSLPckg_AssociationClass = Class(name="CompleteDSLPckg_AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
CompleteDSLPckg_Event = Class(name="CompleteDSLPckg_Event", is_abstract=True)
CompleteDSLPckg_OpaqueBehavior = Class(name="CompleteDSLPckg_OpaqueBehavior")
Behavior = Class(name="Behavior")
CompleteDSLPckg_FunctionBehavior = Class(name="CompleteDSLPckg_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
CompleteDSLPckg_Signal = Class(name="CompleteDSLPckg_Signal")
CompleteDSLPckg_Trigger = Class(name="CompleteDSLPckg_Trigger")
CompleteDSLPckg_Interval = Class(name="CompleteDSLPckg_Interval")
CompleteDSLPckg_MessageEvent = Class(name="CompleteDSLPckg_MessageEvent", is_abstract=True)
Event = Class(name="Event")
CompleteDSLPckg_AnyReceiveEvent = Class(name="CompleteDSLPckg_AnyReceiveEvent")
MessageEvent = Class(name="MessageEvent")
CompleteDSLPckg_SignalEvent = Class(name="CompleteDSLPckg_SignalEvent")
CompleteDSLPckg_CallEvent = Class(name="CompleteDSLPckg_CallEvent")
CompleteDSLPckg_ChangeEvent = Class(name="CompleteDSLPckg_ChangeEvent")
CompleteDSLPckg_TimeEvent = Class(name="CompleteDSLPckg_TimeEvent")
CompleteDSLPckg_TimeExpression = Class(name="CompleteDSLPckg_TimeExpression")
CompleteDSLPckg_Observation = Class(name="CompleteDSLPckg_Observation", is_abstract=True)
CompleteDSLPckg_TimeObservation = Class(name="CompleteDSLPckg_TimeObservation")
Observation = Class(name="Observation")
CompleteDSLPckg_DurationObservation = Class(name="CompleteDSLPckg_DurationObservation")
CompleteDSLPckg_Duration = Class(name="CompleteDSLPckg_Duration")
CompleteDSLPckg_TimeInterval = Class(name="CompleteDSLPckg_TimeInterval")
Interval = Class(name="Interval")
CompleteDSLPckg_DurationInterval = Class(name="CompleteDSLPckg_DurationInterval")
CompleteDSLPckg_IntervalConstraint = Class(name="CompleteDSLPckg_IntervalConstraint")
Constraint = Class(name="Constraint")
CompleteDSLPckg_TimeConstraint = Class(name="CompleteDSLPckg_TimeConstraint")
IntervalConstraint = Class(name="IntervalConstraint")
CompleteDSLPckg_DurationConstraint = Class(name="CompleteDSLPckg_DurationConstraint")
CompleteDSLPckg_Component = Class(name="CompleteDSLPckg_Component")
CompleteDSLPckg_ComponentRealization = Class(name="CompleteDSLPckg_ComponentRealization")
CompleteDSLPckg_Port = Class(name="CompleteDSLPckg_Port")
Property_ = Class(name="Property")
CompleteDSLPckg_Connector = Class(name="CompleteDSLPckg_Connector")
CompleteDSLPckg_ConnectorEnd = Class(name="CompleteDSLPckg_ConnectorEnd")
CompleteDSLPckg_ConnectableElement = Class(name="CompleteDSLPckg_ConnectableElement", is_abstract=True)
CompleteDSLPckg_StructuredClassifier = Class(name="CompleteDSLPckg_StructuredClassifier")
CompleteDSLPckg_Manifestation = Class(name="CompleteDSLPckg_Manifestation")
CompleteDSLPckg_EncapsulatedClassifier = Class(name="CompleteDSLPckg_EncapsulatedClassifier", is_abstract=True)
CompleteDSLPckg_Collaboration = Class(name="CompleteDSLPckg_Collaboration")
CompleteDSLPckg_InvocationAction = Class(name="CompleteDSLPckg_InvocationAction", is_abstract=True)
CompleteDSLPckg_Variable = Class(name="CompleteDSLPckg_Variable")
CompleteDSLPckg_Artifact = Class(name="CompleteDSLPckg_Artifact")
DeployedArtifact = Class(name="DeployedArtifact")
CompleteDSLPckg_OutputPin = Class(name="CompleteDSLPckg_OutputPin")
CompleteDSLPckg_Node = Class(name="CompleteDSLPckg_Node")
CompleteDSLPckg_Device = Class(name="CompleteDSLPckg_Device")
Node = Class(name="Node")
CompleteDSLPckg_ExecutionEnvironment = Class(name="CompleteDSLPckg_ExecutionEnvironment")
CompleteDSLPckg_CommunicationPath = Class(name="CompleteDSLPckg_CommunicationPath")
CompleteDSLPckg_DeploymentTarget = Class(name="CompleteDSLPckg_DeploymentTarget", is_abstract=True)
CompleteDSLPckg_Deployment = Class(name="CompleteDSLPckg_Deployment")
CompleteDSLPckg_DeployedArtifact = Class(name="CompleteDSLPckg_DeployedArtifact", is_abstract=True)
CompleteDSLPckg_DeploymentSpecification = Class(name="CompleteDSLPckg_DeploymentSpecification")
Artifact = Class(name="Artifact")
CompleteDSLPckg_Action = Class(name="CompleteDSLPckg_Action", is_abstract=True)
CompleteDSLPckg_InputPin = Class(name="CompleteDSLPckg_InputPin")
CompleteDSLPckg_SendObjectAction = Class(name="CompleteDSLPckg_SendObjectAction")
CompleteDSLPckg_OpaqueAction = Class(name="CompleteDSLPckg_OpaqueAction")
Action = Class(name="Action")
Pin = Class(name="Pin")
CompleteDSLPckg_Pin = Class(name="CompleteDSLPckg_Pin", is_abstract=True)
CompleteDSLPckg_ValuePin = Class(name="CompleteDSLPckg_ValuePin")
InputPin = Class(name="InputPin")
CompleteDSLPckg_CallAction = Class(name="CompleteDSLPckg_CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
CompleteDSLPckg_CallBehaviorAction = Class(name="CompleteDSLPckg_CallBehaviorAction")
CallAction = Class(name="CallAction")
CompleteDSLPckg_CallOperationAction = Class(name="CompleteDSLPckg_CallOperationAction")
CompleteDSLPckg_SendSignalAction = Class(name="CompleteDSLPckg_SendSignalAction")
CompleteDSLPckg_BroadcastSignalAction = Class(name="CompleteDSLPckg_BroadcastSignalAction")
CompleteDSLPckg_ReadStructuralFeatureAction = Class(name="CompleteDSLPckg_ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
CompleteDSLPckg_CreateObjectAction = Class(name="CompleteDSLPckg_CreateObjectAction")
CompleteDSLPckg_DestroyObjectAction = Class(name="CompleteDSLPckg_DestroyObjectAction")
CompleteDSLPckg_TestIdentityAction = Class(name="CompleteDSLPckg_TestIdentityAction")
CompleteDSLPckg_ReadSelfAction = Class(name="CompleteDSLPckg_ReadSelfAction")
CompleteDSLPckg_ValueSpecificationAction = Class(name="CompleteDSLPckg_ValueSpecificationAction")
CompleteDSLPckg_StructuralFeatureAction = Class(name="CompleteDSLPckg_StructuralFeatureAction", is_abstract=True)
CompleteDSLPckg_CreateLinkAction = Class(name="CompleteDSLPckg_CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
CompleteDSLPckg_LinkEndCreationData = Class(name="CompleteDSLPckg_LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
CompleteDSLPckg_WriteStructuralFeatureAction = Class(name="CompleteDSLPckg_WriteStructuralFeatureAction", is_abstract=True)
CompleteDSLPckg_AddStructuralFeatureValueAction = Class(name="CompleteDSLPckg_AddStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
CompleteDSLPckg_RemoveStructuralFeatureValueAction = Class(name="CompleteDSLPckg_RemoveStructuralFeatureValueAction")
CompleteDSLPckg_ClearStructuralFeatureAction = Class(name="CompleteDSLPckg_ClearStructuralFeatureAction")
CompleteDSLPckg_LinkAction = Class(name="CompleteDSLPckg_LinkAction")
CompleteDSLPckg_LinkEndData = Class(name="CompleteDSLPckg_LinkEndData", is_abstract=True)
CompleteDSLPckg_QualifierValue = Class(name="CompleteDSLPckg_QualifierValue")
CompleteDSLPckg_ReadLinkAction = Class(name="CompleteDSLPckg_ReadLinkAction")
LinkAction = Class(name="LinkAction")
CompleteDSLPckg_WriteLinkAction = Class(name="CompleteDSLPckg_WriteLinkAction", is_abstract=True)
AcceptEventAction = Class(name="AcceptEventAction")
CompleteDSLPckg_DestroyLinkAction = Class(name="CompleteDSLPckg_DestroyLinkAction")
CompleteDSLPckg_LinkEndDestructionData = Class(name="CompleteDSLPckg_LinkEndDestructionData")
CompleteDSLPckg_ReplyAction = Class(name="CompleteDSLPckg_ReplyAction")
CompleteDSLPckg_UnmarshallAction = Class(name="CompleteDSLPckg_UnmarshallAction")
CompleteDSLPckg_AcceptEventAction = Class(name="CompleteDSLPckg_AcceptEventAction")
CompleteDSLPckg_AcceptCallAction = Class(name="CompleteDSLPckg_AcceptCallAction")
CompleteDSLPckg_ReadExtendAction = Class(name="CompleteDSLPckg_ReadExtendAction")
CompleteDSLPckg_ReclassifyObjectAction = Class(name="CompleteDSLPckg_ReclassifyObjectAction")
CompleteDSLPckg_ReadlsClassifiedObjectAction = Class(name="CompleteDSLPckg_ReadlsClassifiedObjectAction")
CompleteDSLPckg_StartClassifierBehaviorAction = Class(name="CompleteDSLPckg_StartClassifierBehaviorAction")
CompleteDSLPckg_StartObjectBehaviorAction = Class(name="CompleteDSLPckg_StartObjectBehaviorAction")
CompleteDSLPckg_ReadLinkObjectEndAction = Class(name="CompleteDSLPckg_ReadLinkObjectEndAction")
CompleteDSLPckg_ReadLinkObjectEndQualifierAction = Class(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction")
CompleteDSLPckg_CreateLinkObjectAction = Class(name="CompleteDSLPckg_CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
CompleteDSLPckg_VariableAction = Class(name="CompleteDSLPckg_VariableAction", is_abstract=True)
CompleteDSLPckg_ReduceAction = Class(name="CompleteDSLPckg_ReduceAction")
CompleteDSLPckg_StateMachine = Class(name="CompleteDSLPckg_StateMachine")
CompleteDSLPckg_Region = Class(name="CompleteDSLPckg_Region")
CompleteDSLPckg_Pseudostate = Class(name="CompleteDSLPckg_Pseudostate")
CompleteDSLPckg_ReadVariableAction = Class(name="CompleteDSLPckg_ReadVariableAction")
VariableAction = Class(name="VariableAction")
CompleteDSLPckg_WriteVariableAction = Class(name="CompleteDSLPckg_WriteVariableAction")
CompleteDSLPckg_AddVariableValueAction = Class(name="CompleteDSLPckg_AddVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
CompleteDSLPckg_RemoveVariableValueAction = Class(name="CompleteDSLPckg_RemoveVariableValueAction")
CompleteDSLPckg_ClearVariableAction = Class(name="CompleteDSLPckg_ClearVariableAction")
CompleteDSLPckg_RaiseExceptionAction = Class(name="CompleteDSLPckg_RaiseExceptionAction")
CompleteDSLPckg_ActionInputPin = Class(name="CompleteDSLPckg_ActionInputPin")
CompleteDSLPckg_State = Class(name="CompleteDSLPckg_State")
CompleteDSLPckg_Vertex = Class(name="CompleteDSLPckg_Vertex", is_abstract=True)
CompleteDSLPckg_Transition = Class(name="CompleteDSLPckg_Transition")
Vertex = Class(name="Vertex")
CompleteDSLPckg_ConnectionPointReference = Class(name="CompleteDSLPckg_ConnectionPointReference")
CompleteDSLPckg_FinalState = Class(name="CompleteDSLPckg_FinalState")
State = Class(name="State")
CompleteDSLPckg_ProtocolStateMachine = Class(name="CompleteDSLPckg_ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
CompleteDSLPckg_ProtocolConformance = Class(name="CompleteDSLPckg_ProtocolConformance")
CompleteDSLPckg_InterruptibleActivityRegion = Class(name="CompleteDSLPckg_InterruptibleActivityRegion")
CompleteDSLPckg_ProtocolTransition = Class(name="CompleteDSLPckg_ProtocolTransition")
Transition = Class(name="Transition")
CompleteDSLPckg_Activity = Class(name="CompleteDSLPckg_Activity")
CompleteDSLPckg_ActivityNode = Class(name="CompleteDSLPckg_ActivityNode", is_abstract=True)
CompleteDSLPckg_ActivityGroup = Class(name="CompleteDSLPckg_ActivityGroup", is_abstract=True)
CompleteDSLPckg_ActivityEdge = Class(name="CompleteDSLPckg_ActivityEdge", is_abstract=True)
CompleteDSLPckg_ActivityPartition = Class(name="CompleteDSLPckg_ActivityPartition")
CompleteDSLPckg_StructuredActivityNode = Class(name="CompleteDSLPckg_StructuredActivityNode")
CompleteDSLPckg_ObjectNode = Class(name="CompleteDSLPckg_ObjectNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
CompleteDSLPckg_ActivityParameterNode = Class(name="CompleteDSLPckg_ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
CompleteDSLPckg_ControlNode = Class(name="CompleteDSLPckg_ControlNode", is_abstract=True)
CompleteDSLPckg_ActivityFinalNode = Class(name="CompleteDSLPckg_ActivityFinalNode")
ControlNode = Class(name="ControlNode")
FinalNode = Class(name="FinalNode")
CompleteDSLPckg_InitialNode = Class(name="CompleteDSLPckg_InitialNode")
ActivityGroup = Class(name="ActivityGroup")
CompleteDSLPckg_ControlFlow = Class(name="CompleteDSLPckg_ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
CompleteDSLPckg_ObjectFlow = Class(name="CompleteDSLPckg_ObjectFlow")
CompleteDSLPckg_CentralBufferNode = Class(name="CompleteDSLPckg_CentralBufferNode")
CompleteDSLPckg_FinalNode = Class(name="CompleteDSLPckg_FinalNode", is_abstract=True)
CompleteDSLPckg_FlowFinalNode = Class(name="CompleteDSLPckg_FlowFinalNode")
CompleteDSLPckg_ForkNode = Class(name="CompleteDSLPckg_ForkNode")
CompleteDSLPckg_JoinNode = Class(name="CompleteDSLPckg_JoinNode")
CompleteDSLPckg_MergeNode = Class(name="CompleteDSLPckg_MergeNode")
CompleteDSLPckg_DecisionNode = Class(name="CompleteDSLPckg_DecisionNode")
CompleteDSLPckg_ExecutableNode = Class(name="CompleteDSLPckg_ExecutableNode")
CompleteDSLPckg_ExceptionHandler = Class(name="CompleteDSLPckg_ExceptionHandler")
CompleteDSLPckg_LoopNode = Class(name="CompleteDSLPckg_LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
CompleteDSLPckg_DataStoreNode = Class(name="CompleteDSLPckg_DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
CompleteDSLPckg_ParameterSet = Class(name="CompleteDSLPckg_ParameterSet")
ExecutableNode = Class(name="ExecutableNode")
CompleteDSLPckg_SequenceNode = Class(name="CompleteDSLPckg_SequenceNode")
CompleteDSLPckg_ConditionalNode = Class(name="CompleteDSLPckg_ConditionalNode")
CompleteDSLPckg_Clause = Class(name="CompleteDSLPckg_Clause")
CompleteDSLPckg_ExpansionRegion = Class(name="CompleteDSLPckg_ExpansionRegion")
CompleteDSLPckg_ExpansionNode = Class(name="CompleteDSLPckg_ExpansionNode")
CompleteDSLPckg_Gate = Class(name="CompleteDSLPckg_Gate")
CompleteDSLPckg_InteractionFragment = Class(name="CompleteDSLPckg_InteractionFragment", is_abstract=True)
CompleteDSLPckg_Lifeline = Class(name="CompleteDSLPckg_Lifeline")
CompleteDSLPckg_GeneralOrdering = Class(name="CompleteDSLPckg_GeneralOrdering")
CompleteDSLPckg_InteractionOperand = Class(name="CompleteDSLPckg_InteractionOperand")
CompleteDSLPckg_ExecutionSpecification = Class(name="CompleteDSLPckg_ExecutionSpecification", is_abstract=True)
InteractionFragment = Class(name="InteractionFragment")
CompleteDSLPckg_OccurenceSpecification = Class(name="CompleteDSLPckg_OccurenceSpecification")
CompleteDSLPckg_StateInvariant = Class(name="CompleteDSLPckg_StateInvariant")
CompleteDSLPckg_Interaction = Class(name="CompleteDSLPckg_Interaction")
CompleteDSLPckg_ExecutionOccurrenceSpecification = Class(name="CompleteDSLPckg_ExecutionOccurrenceSpecification")
OccurenceSpecification = Class(name="OccurenceSpecification")
CompleteDSLPckg_MessageOccurrenceSpecification = Class(name="CompleteDSLPckg_MessageOccurrenceSpecification")
CompleteDSLPckg_DestructionOccurrenceSpecification = Class(name="CompleteDSLPckg_DestructionOccurrenceSpecification")
MessageOccurrenceSpecification = Class(name="MessageOccurrenceSpecification")
CompleteDSLPckg_BehaviorExecutionSpecification = Class(name="CompleteDSLPckg_BehaviorExecutionSpecification")
ExecutionSpecification = Class(name="ExecutionSpecification")
CompleteDSLPckg_PartDecomposition = Class(name="CompleteDSLPckg_PartDecomposition")
CompleteDSLPckg_Message = Class(name="CompleteDSLPckg_Message")
CompleteDSLPckg_MessageEnd = Class(name="CompleteDSLPckg_MessageEnd", is_abstract=True)
CompleteDSLPckg_Continuation = Class(name="CompleteDSLPckg_Continuation")
CompleteDSLPckg_ActionExecutionSpecification = Class(name="CompleteDSLPckg_ActionExecutionSpecification")
CompleteDSLPckg_InteractionConstraint = Class(name="CompleteDSLPckg_InteractionConstraint")
CompleteDSLPckg_CombinedFragment = Class(name="CompleteDSLPckg_CombinedFragment")
CompleteDSLPckg_ConsiderIgnoreFragment = Class(name="CompleteDSLPckg_ConsiderIgnoreFragment")
CombinedFragment = Class(name="CombinedFragment")
MessageEnd = Class(name="MessageEnd")
CompleteDSLPckg_InteractionUse = Class(name="CompleteDSLPckg_InteractionUse")
InteractionUse = Class(name="InteractionUse")
CompleteDSLPckg_Actor = Class(name="CompleteDSLPckg_Actor")
CompleteDSLPckg_UseCase = Class(name="CompleteDSLPckg_UseCase")
CompleteDSLPckg_ExtensionPoint = Class(name="CompleteDSLPckg_ExtensionPoint")
CompleteDSLPckg_Extend = Class(name="CompleteDSLPckg_Extend")
CompleteDSLPckg_Include = Class(name="CompleteDSLPckg_Include")

# NamedElement class attributes and methods

# CompleteDSLPckg_Element class attributes and methods

# CompleteDSLPckg_Comment class attributes and methods
CompleteDSLPckg_Comment_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_Comment.attributes={CompleteDSLPckg_Comment_body}

# CompleteDSLPckg_NamedElement class attributes and methods
CompleteDSLPckg_NamedElement_name: Property = Property(name="name", type=StringType)
CompleteDSLPckg_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
CompleteDSLPckg_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_NamedElement.attributes={CompleteDSLPckg_NamedElement_name, CompleteDSLPckg_NamedElement_visibility, CompleteDSLPckg_NamedElement_qualifiedName}

# Element class attributes and methods

# CompleteDSLPckg_Namespace class attributes and methods

# CompleteDSLPckg_Dependency class attributes and methods

# CompleteDSLPckg_PackageableElement class attributes and methods

# CompleteDSLPckg_ElementImport class attributes and methods
CompleteDSLPckg_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_ElementImport_alias: Property = Property(name="alias", type=StringType)
CompleteDSLPckg_ElementImport.attributes={CompleteDSLPckg_ElementImport_alias, CompleteDSLPckg_ElementImport_visibility}

# CompleteDSLPckg_PackageImport class attributes and methods
CompleteDSLPckg_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
CompleteDSLPckg_PackageImport.attributes={CompleteDSLPckg_PackageImport_visibility}

# CompleteDSLPckg_Constraint class attributes and methods

# DirectedRelationship class attributes and methods

# CompleteDSLPckg_Package class attributes and methods
CompleteDSLPckg_Package_URI: Property = Property(name="URI", type=StringType)
CompleteDSLPckg_Package.attributes={CompleteDSLPckg_Package_URI}

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# CompleteDSLPckg_Type class attributes and methods

# CompleteDSLPckg_PackageMerge class attributes and methods

# CompleteDSLPckg_Relationship class attributes and methods

# CompleteDSLPckg_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# CompleteDSLPckg_MultiplicityElement class attributes and methods
CompleteDSLPckg_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
CompleteDSLPckg_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
CompleteDSLPckg_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
CompleteDSLPckg_MultiplicityElement.attributes={CompleteDSLPckg_MultiplicityElement_isOrdered, CompleteDSLPckg_MultiplicityElement_lower, CompleteDSLPckg_MultiplicityElement_upper, CompleteDSLPckg_MultiplicityElement_isUnique}

# CompleteDSLPckg_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# CompleteDSLPckg_Slot class attributes and methods

# CompleteDSLPckg_InstanceSpecification class attributes and methods

# CompleteDSLPckg_TypedElement class attributes and methods

# CompleteDSLPckg_Expression class attributes and methods
CompleteDSLPckg_Expression_symbol: Property = Property(name="symbol", type=StringType)
CompleteDSLPckg_Expression.attributes={CompleteDSLPckg_Expression_symbol}

# ValueSpecification class attributes and methods

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

# CompleteDSLPckg_LiteralInteger class attributes and methods

# CompleteDSLPckg_LiteralReal class attributes and methods

# CompleteDSLPckg_LiteralString class attributes and methods

# CompleteDSLPckg_LiteralUnilimitedNatural class attributes and methods

# CompleteDSLPckg_InstanceValue class attributes and methods

# CompleteDSLPckg_Classifier class attributes and methods
CompleteDSLPckg_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
CompleteDSLPckg_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=BooleanType)
CompleteDSLPckg_Classifier.attributes={CompleteDSLPckg_Classifier_isFinalSpecialization, CompleteDSLPckg_Classifier_isAbstract}

# CompleteDSLPckg_StructuralFeature class attributes and methods
CompleteDSLPckg_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
CompleteDSLPckg_StructuralFeature.attributes={CompleteDSLPckg_StructuralFeature_isReadOnly}

# CompleteDSLPckg_RedefinableElement class attributes and methods
CompleteDSLPckg_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
CompleteDSLPckg_RedefinableElement.attributes={CompleteDSLPckg_RedefinableElement_isLeaf}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# CompleteDSLPckg_Feature class attributes and methods
CompleteDSLPckg_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
CompleteDSLPckg_Feature.attributes={CompleteDSLPckg_Feature_isStatic}

# CompleteDSLPckg_Property class attributes and methods
CompleteDSLPckg_Property_aggregation: Property = Property(name="aggregation", type=StringType)
CompleteDSLPckg_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
CompleteDSLPckg_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
CompleteDSLPckg_Property_default: Property = Property(name="default", type=StringType)
CompleteDSLPckg_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
CompleteDSLPckg_Property_isID: Property = Property(name="isID", type=BooleanType)
CompleteDSLPckg_Property.attributes={CompleteDSLPckg_Property_aggregation, CompleteDSLPckg_Property_isDerivedUnion, CompleteDSLPckg_Property_isID, CompleteDSLPckg_Property_isDerived, CompleteDSLPckg_Property_isComposite, CompleteDSLPckg_Property_default}

# CompleteDSLPckg_Generalization class attributes and methods
CompleteDSLPckg_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
CompleteDSLPckg_Generalization.attributes={CompleteDSLPckg_Generalization_isSubstitutable}

# CompleteDSLPckg_Substitution class attributes and methods

# CompleteDSLPckg_GeneralizationSet class attributes and methods
CompleteDSLPckg_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
CompleteDSLPckg_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
CompleteDSLPckg_GeneralizationSet.attributes={CompleteDSLPckg_GeneralizationSet_isDisjoint, CompleteDSLPckg_GeneralizationSet_isCovering}

# CompleteDSLPckg_CollaborationUse class attributes and methods

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# CompleteDSLPckg_Class class attributes and methods

# CompleteDSLPckg_Association class attributes and methods
CompleteDSLPckg_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
CompleteDSLPckg_Association.attributes={CompleteDSLPckg_Association_isDerived}

# CompleteDSLPckg_DataType class attributes and methods

# CompleteDSLPckg_Interface class attributes and methods

# CompleteDSLPckg_BehavioralFeature class attributes and methods

# CompleteDSLPckg_Operation class attributes and methods
CompleteDSLPckg_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
CompleteDSLPckg_Operation_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_Operation_isUnique: Property = Property(name="isUnique", type=BooleanType)
CompleteDSLPckg_Operation_upper: Property = Property(name="upper", type=IntegerType)
CompleteDSLPckg_Operation_lower: Property = Property(name="lower", type=IntegerType)
CompleteDSLPckg_Operation.attributes={CompleteDSLPckg_Operation_isUnique, CompleteDSLPckg_Operation_lower, CompleteDSLPckg_Operation_upper, CompleteDSLPckg_Operation_isOrdered, CompleteDSLPckg_Operation_isQuery}

# BehavioralFeature class attributes and methods

# Classifier class attributes and methods

# BehavioredClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# CompleteDSLPckg_Reception class attributes and methods

# CompleteDSLPckg_PrimitiveType class attributes and methods

# DataType class attributes and methods

# CompleteDSLPckg_Enumeration class attributes and methods

# CompleteDSLPckg_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# CompleteDSLPckg_Usage class attributes and methods

# Dependency class attributes and methods

# CompleteDSLPckg_Abstraction class attributes and methods

# CompleteDSLPckg_Realization class attributes and methods

# Abstraction class attributes and methods

# Realization class attributes and methods

# CompleteDSLPckg_InterfaceRealization class attributes and methods

# CompleteDSLPckg_BehavioredClassifier class attributes and methods

# CompleteDSLPckg_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# CompleteDSLPckg_Event class attributes and methods

# CompleteDSLPckg_OpaqueBehavior class attributes and methods
CompleteDSLPckg_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
CompleteDSLPckg_OpaqueBehavior.attributes={CompleteDSLPckg_OpaqueBehavior_language, CompleteDSLPckg_OpaqueBehavior_body}

# Behavior class attributes and methods

# CompleteDSLPckg_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# CompleteDSLPckg_Signal class attributes and methods

# CompleteDSLPckg_Trigger class attributes and methods

# CompleteDSLPckg_Interval class attributes and methods

# CompleteDSLPckg_MessageEvent class attributes and methods

# Event class attributes and methods

# CompleteDSLPckg_AnyReceiveEvent class attributes and methods

# MessageEvent class attributes and methods

# CompleteDSLPckg_SignalEvent class attributes and methods

# CompleteDSLPckg_CallEvent class attributes and methods

# CompleteDSLPckg_ChangeEvent class attributes and methods

# CompleteDSLPckg_TimeEvent class attributes and methods
CompleteDSLPckg_TimeEvent_isRelative: Property = Property(name="isRelative", type=BooleanType)
CompleteDSLPckg_TimeEvent.attributes={CompleteDSLPckg_TimeEvent_isRelative}

# CompleteDSLPckg_TimeExpression class attributes and methods

# CompleteDSLPckg_Observation class attributes and methods

# CompleteDSLPckg_TimeObservation class attributes and methods
CompleteDSLPckg_TimeObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_TimeObservation.attributes={CompleteDSLPckg_TimeObservation_firstEvent}

# Observation class attributes and methods

# CompleteDSLPckg_DurationObservation class attributes and methods
CompleteDSLPckg_DurationObservation_firstEvent: Property = Property(name="firstEvent", type=BooleanType)
CompleteDSLPckg_DurationObservation.attributes={CompleteDSLPckg_DurationObservation_firstEvent}

# CompleteDSLPckg_Duration class attributes and methods

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

# CompleteDSLPckg_ComponentRealization class attributes and methods

# CompleteDSLPckg_Port class attributes and methods
CompleteDSLPckg_Port_isBehavior: Property = Property(name="isBehavior", type=BooleanType)
CompleteDSLPckg_Port_isService: Property = Property(name="isService", type=BooleanType)
CompleteDSLPckg_Port_isConjugated: Property = Property(name="isConjugated", type=BooleanType)
CompleteDSLPckg_Port.attributes={CompleteDSLPckg_Port_isConjugated, CompleteDSLPckg_Port_isService, CompleteDSLPckg_Port_isBehavior}

# Property class attributes and methods

# CompleteDSLPckg_Connector class attributes and methods
CompleteDSLPckg_Connector_kind: Property = Property(name="kind", type=StringType)
CompleteDSLPckg_Connector.attributes={CompleteDSLPckg_Connector_kind}

# CompleteDSLPckg_ConnectorEnd class attributes and methods

# CompleteDSLPckg_ConnectableElement class attributes and methods

# CompleteDSLPckg_StructuredClassifier class attributes and methods

# CompleteDSLPckg_Manifestation class attributes and methods

# CompleteDSLPckg_EncapsulatedClassifier class attributes and methods

# CompleteDSLPckg_Collaboration class attributes and methods

# CompleteDSLPckg_InvocationAction class attributes and methods

# CompleteDSLPckg_Variable class attributes and methods

# CompleteDSLPckg_Artifact class attributes and methods
CompleteDSLPckg_Artifact_fileName: Property = Property(name="fileName", type=StringType)
CompleteDSLPckg_Artifact.attributes={CompleteDSLPckg_Artifact_fileName}

# DeployedArtifact class attributes and methods

# CompleteDSLPckg_OutputPin class attributes and methods

# CompleteDSLPckg_Node class attributes and methods

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

# CompleteDSLPckg_Action class attributes and methods

# CompleteDSLPckg_InputPin class attributes and methods

# CompleteDSLPckg_SendObjectAction class attributes and methods

# CompleteDSLPckg_OpaqueAction class attributes and methods
CompleteDSLPckg_OpaqueAction_body: Property = Property(name="body", type=StringType)
CompleteDSLPckg_OpaqueAction_language: Property = Property(name="language", type=StringType)
CompleteDSLPckg_OpaqueAction.attributes={CompleteDSLPckg_OpaqueAction_body, CompleteDSLPckg_OpaqueAction_language}

# Action class attributes and methods

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

# CompleteDSLPckg_BroadcastSignalAction class attributes and methods

# CompleteDSLPckg_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# CompleteDSLPckg_CreateObjectAction class attributes and methods

# CompleteDSLPckg_DestroyObjectAction class attributes and methods

# CompleteDSLPckg_TestIdentityAction class attributes and methods

# CompleteDSLPckg_ReadSelfAction class attributes and methods

# CompleteDSLPckg_ValueSpecificationAction class attributes and methods

# CompleteDSLPckg_StructuralFeatureAction class attributes and methods

# CompleteDSLPckg_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# CompleteDSLPckg_LinkEndCreationData class attributes and methods
CompleteDSLPckg_LinkEndCreationData_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
CompleteDSLPckg_LinkEndCreationData.attributes={CompleteDSLPckg_LinkEndCreationData_isReplaceAll}

# LinkEndData class attributes and methods

# CompleteDSLPckg_WriteStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_AddStructuralFeatureValueAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_RemoveStructuralFeatureValueAction class attributes and methods

# CompleteDSLPckg_ClearStructuralFeatureAction class attributes and methods

# CompleteDSLPckg_LinkAction class attributes and methods

# CompleteDSLPckg_LinkEndData class attributes and methods

# CompleteDSLPckg_QualifierValue class attributes and methods

# CompleteDSLPckg_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# CompleteDSLPckg_WriteLinkAction class attributes and methods

# AcceptEventAction class attributes and methods

# CompleteDSLPckg_DestroyLinkAction class attributes and methods

# CompleteDSLPckg_LinkEndDestructionData class attributes and methods
CompleteDSLPckg_LinkEndDestructionData_isDestroyDuplicates: Property = Property(name="isDestroyDuplicates", type=BooleanType)
CompleteDSLPckg_LinkEndDestructionData.attributes={CompleteDSLPckg_LinkEndDestructionData_isDestroyDuplicates}

# CompleteDSLPckg_ReplyAction class attributes and methods

# CompleteDSLPckg_UnmarshallAction class attributes and methods

# CompleteDSLPckg_AcceptEventAction class attributes and methods
CompleteDSLPckg_AcceptEventAction_isUnmarshall: Property = Property(name="isUnmarshall", type=BooleanType)
CompleteDSLPckg_AcceptEventAction.attributes={CompleteDSLPckg_AcceptEventAction_isUnmarshall}

# CompleteDSLPckg_AcceptCallAction class attributes and methods

# CompleteDSLPckg_ReadExtendAction class attributes and methods

# CompleteDSLPckg_ReclassifyObjectAction class attributes and methods
CompleteDSLPckg_ReclassifyObjectAction_isReplaceAll: Property = Property(name="isReplaceAll", type=BooleanType)
CompleteDSLPckg_ReclassifyObjectAction.attributes={CompleteDSLPckg_ReclassifyObjectAction_isReplaceAll}

# CompleteDSLPckg_ReadlsClassifiedObjectAction class attributes and methods

# CompleteDSLPckg_StartClassifierBehaviorAction class attributes and methods

# CompleteDSLPckg_StartObjectBehaviorAction class attributes and methods

# CompleteDSLPckg_ReadLinkObjectEndAction class attributes and methods

# CompleteDSLPckg_ReadLinkObjectEndQualifierAction class attributes and methods

# CompleteDSLPckg_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# CompleteDSLPckg_VariableAction class attributes and methods

# CompleteDSLPckg_ReduceAction class attributes and methods
CompleteDSLPckg_ReduceAction_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
CompleteDSLPckg_ReduceAction.attributes={CompleteDSLPckg_ReduceAction_isOrdered}

# CompleteDSLPckg_StateMachine class attributes and methods

# CompleteDSLPckg_Region class attributes and methods

# CompleteDSLPckg_Pseudostate class attributes and methods

# CompleteDSLPckg_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# CompleteDSLPckg_WriteVariableAction class attributes and methods

# CompleteDSLPckg_AddVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# CompleteDSLPckg_RemoveVariableValueAction class attributes and methods

# CompleteDSLPckg_ClearVariableAction class attributes and methods

# CompleteDSLPckg_RaiseExceptionAction class attributes and methods

# CompleteDSLPckg_ActionInputPin class attributes and methods

# CompleteDSLPckg_State class attributes and methods
CompleteDSLPckg_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
CompleteDSLPckg_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
CompleteDSLPckg_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
CompleteDSLPckg_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
CompleteDSLPckg_State.attributes={CompleteDSLPckg_State_isSubmachineState, CompleteDSLPckg_State_isSimple, CompleteDSLPckg_State_isComposite, CompleteDSLPckg_State_isOrthogonal}

# CompleteDSLPckg_Vertex class attributes and methods

# CompleteDSLPckg_Transition class attributes and methods
CompleteDSLPckg_Transition_kind: Property = Property(name="kind", type=StringType)
CompleteDSLPckg_Transition.attributes={CompleteDSLPckg_Transition_kind}

# Vertex class attributes and methods

# CompleteDSLPckg_ConnectionPointReference class attributes and methods

# CompleteDSLPckg_FinalState class attributes and methods

# State class attributes and methods

# CompleteDSLPckg_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# CompleteDSLPckg_ProtocolConformance class attributes and methods

# CompleteDSLPckg_InterruptibleActivityRegion class attributes and methods

# CompleteDSLPckg_ProtocolTransition class attributes and methods

# Transition class attributes and methods

# CompleteDSLPckg_Activity class attributes and methods
CompleteDSLPckg_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
CompleteDSLPckg_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
CompleteDSLPckg_Activity.attributes={CompleteDSLPckg_Activity_isReadOnly, CompleteDSLPckg_Activity_isSingleExecution}

# CompleteDSLPckg_ActivityNode class attributes and methods

# CompleteDSLPckg_ActivityGroup class attributes and methods

# CompleteDSLPckg_ActivityEdge class attributes and methods

# CompleteDSLPckg_ActivityPartition class attributes and methods

# CompleteDSLPckg_StructuredActivityNode class attributes and methods
CompleteDSLPckg_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
CompleteDSLPckg_StructuredActivityNode.attributes={CompleteDSLPckg_StructuredActivityNode_mustIsolate}

# CompleteDSLPckg_ObjectNode class attributes and methods

# ActivityNode class attributes and methods

# CompleteDSLPckg_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# CompleteDSLPckg_ControlNode class attributes and methods

# CompleteDSLPckg_ActivityFinalNode class attributes and methods

# ControlNode class attributes and methods

# FinalNode class attributes and methods

# CompleteDSLPckg_InitialNode class attributes and methods

# ActivityGroup class attributes and methods

# CompleteDSLPckg_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# CompleteDSLPckg_ObjectFlow class attributes and methods
CompleteDSLPckg_ObjectFlow_isMulticast: Property = Property(name="isMulticast", type=BooleanType)
CompleteDSLPckg_ObjectFlow_isMultireceive: Property = Property(name="isMultireceive", type=BooleanType)
CompleteDSLPckg_ObjectFlow_ordering: Property = Property(name="ordering", type=StringType)
CompleteDSLPckg_ObjectFlow_isControlType: Property = Property(name="isControlType", type=BooleanType)
CompleteDSLPckg_ObjectFlow.attributes={CompleteDSLPckg_ObjectFlow_isMultireceive, CompleteDSLPckg_ObjectFlow_ordering, CompleteDSLPckg_ObjectFlow_isMulticast, CompleteDSLPckg_ObjectFlow_isControlType}

# CompleteDSLPckg_CentralBufferNode class attributes and methods

# CompleteDSLPckg_FinalNode class attributes and methods

# CompleteDSLPckg_FlowFinalNode class attributes and methods

# CompleteDSLPckg_ForkNode class attributes and methods

# CompleteDSLPckg_JoinNode class attributes and methods
CompleteDSLPckg_JoinNode_isCombineDuplicate: Property = Property(name="isCombineDuplicate", type=BooleanType)
CompleteDSLPckg_JoinNode.attributes={CompleteDSLPckg_JoinNode_isCombineDuplicate}

# CompleteDSLPckg_MergeNode class attributes and methods

# CompleteDSLPckg_DecisionNode class attributes and methods

# CompleteDSLPckg_ExecutableNode class attributes and methods

# CompleteDSLPckg_ExceptionHandler class attributes and methods

# CompleteDSLPckg_LoopNode class attributes and methods
CompleteDSLPckg_LoopNode_isTestedFirst: Property = Property(name="isTestedFirst", type=BooleanType)
CompleteDSLPckg_LoopNode.attributes={CompleteDSLPckg_LoopNode_isTestedFirst}

# StructuredActivityNode class attributes and methods

# CompleteDSLPckg_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# CompleteDSLPckg_ParameterSet class attributes and methods

# ExecutableNode class attributes and methods

# CompleteDSLPckg_SequenceNode class attributes and methods

# CompleteDSLPckg_ConditionalNode class attributes and methods
CompleteDSLPckg_ConditionalNode_isDeterminate: Property = Property(name="isDeterminate", type=BooleanType)
CompleteDSLPckg_ConditionalNode_isAssumed: Property = Property(name="isAssumed", type=BooleanType)
CompleteDSLPckg_ConditionalNode.attributes={CompleteDSLPckg_ConditionalNode_isDeterminate, CompleteDSLPckg_ConditionalNode_isAssumed}

# CompleteDSLPckg_Clause class attributes and methods

# CompleteDSLPckg_ExpansionRegion class attributes and methods
CompleteDSLPckg_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
CompleteDSLPckg_ExpansionRegion.attributes={CompleteDSLPckg_ExpansionRegion_mode}

# CompleteDSLPckg_ExpansionNode class attributes and methods

# CompleteDSLPckg_Gate class attributes and methods

# CompleteDSLPckg_InteractionFragment class attributes and methods

# CompleteDSLPckg_Lifeline class attributes and methods

# CompleteDSLPckg_GeneralOrdering class attributes and methods

# CompleteDSLPckg_InteractionOperand class attributes and methods

# CompleteDSLPckg_ExecutionSpecification class attributes and methods

# InteractionFragment class attributes and methods

# CompleteDSLPckg_OccurenceSpecification class attributes and methods

# CompleteDSLPckg_StateInvariant class attributes and methods

# CompleteDSLPckg_Interaction class attributes and methods

# CompleteDSLPckg_ExecutionOccurrenceSpecification class attributes and methods

# OccurenceSpecification class attributes and methods

# CompleteDSLPckg_MessageOccurrenceSpecification class attributes and methods

# CompleteDSLPckg_DestructionOccurrenceSpecification class attributes and methods

# MessageOccurrenceSpecification class attributes and methods

# CompleteDSLPckg_BehaviorExecutionSpecification class attributes and methods

# ExecutionSpecification class attributes and methods

# CompleteDSLPckg_PartDecomposition class attributes and methods

# CompleteDSLPckg_Message class attributes and methods
CompleteDSLPckg_Message_messageKind: Property = Property(name="messageKind", type=StringType)
CompleteDSLPckg_Message_messageSort: Property = Property(name="messageSort", type=StringType)
CompleteDSLPckg_Message.attributes={CompleteDSLPckg_Message_messageSort, CompleteDSLPckg_Message_messageKind}

# CompleteDSLPckg_MessageEnd class attributes and methods

# CompleteDSLPckg_Continuation class attributes and methods
CompleteDSLPckg_Continuation_setting: Property = Property(name="setting", type=BooleanType)
CompleteDSLPckg_Continuation.attributes={CompleteDSLPckg_Continuation_setting}

# CompleteDSLPckg_ActionExecutionSpecification class attributes and methods

# CompleteDSLPckg_InteractionConstraint class attributes and methods

# CompleteDSLPckg_CombinedFragment class attributes and methods
CompleteDSLPckg_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
CompleteDSLPckg_CombinedFragment.attributes={CompleteDSLPckg_CombinedFragment_interactionOperator}

# CompleteDSLPckg_ConsiderIgnoreFragment class attributes and methods

# CombinedFragment class attributes and methods

# MessageEnd class attributes and methods

# CompleteDSLPckg_InteractionUse class attributes and methods

# InteractionUse class attributes and methods

# CompleteDSLPckg_Actor class attributes and methods

# CompleteDSLPckg_UseCase class attributes and methods

# CompleteDSLPckg_ExtensionPoint class attributes and methods

# CompleteDSLPckg_Extend class attributes and methods

# CompleteDSLPckg_Include class attributes and methods

# Relationships
ownedComment0: BinaryAssociation = BinaryAssociation(
    name="ownedComment0",
    ends={
        Property(name="Comment", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
namespace6: BinaryAssociation = BinaryAssociation(
    name="namespace6",
    ends={
        Property(name="Namespace", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency7: BinaryAssociation = BinaryAssociation(
    name="clientDependency7",
    ends={
        Property(name="Dependency", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage26: BinaryAssociation = BinaryAssociation(
    name="nestingPackage26",
    ends={
        Property(name="Package27", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 1))
    }
)
importedMember8: BinaryAssociation = BinaryAssociation(
    name="importedMember8",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Namespace", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member9: BinaryAssociation = BinaryAssociation(
    name="member9",
    ends={
        Property(name="CompleteDSLPckg_NamedElement", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Namespace10", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember11: BinaryAssociation = BinaryAssociation(
    name="ownedMember11",
    ends={
        Property(name="NamedElement", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport12: BinaryAssociation = BinaryAssociation(
    name="elementImport12",
    ends={
        Property(name="ElementImport", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport13: BinaryAssociation = BinaryAssociation(
    name="packageImport13",
    ends={
        Property(name="PackageImport", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace14", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule15: BinaryAssociation = BinaryAssociation(
    name="ownedRule15",
    ends={
        Property(name="Constraint", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement16: BinaryAssociation = BinaryAssociation(
    name="importedElement16",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement17", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ElementImport", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace18: BinaryAssociation = BinaryAssociation(
    name="importingNamespace18",
    ends={
        Property(name="Namespace19", type=CompleteDSLPckg_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage20: BinaryAssociation = BinaryAssociation(
    name="importedPackage20",
    ends={
        Property(name="CompleteDSLPckg_Package", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_PackageImport", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace21: BinaryAssociation = BinaryAssociation(
    name="importingNamespace21",
    ends={
        Property(name="Namespace22", type=CompleteDSLPckg_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage24: BinaryAssociation = BinaryAssociation(
    name="nestedPackage24",
    ends={
        Property(name="Package", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningUpper46: BinaryAssociation = BinaryAssociation(
    name="owningUpper46",
    ends={
        Property(name="MultiplicityElement", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="upperValue", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningLower47: BinaryAssociation = BinaryAssociation(
    name="owningLower47",
    ends={
        Property(name="MultiplicityElement48", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="lowerValue", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement28: BinaryAssociation = BinaryAssociation(
    name="packagedElement28",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement30", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Package29", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType31: BinaryAssociation = BinaryAssociation(
    name="ownedType31",
    ends={
        Property(name="Type", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge32: BinaryAssociation = BinaryAssociation(
    name="packageMerge32",
    ends={
        Property(name="PackageMerge", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningElement33: BinaryAssociation = BinaryAssociation(
    name="owningElement33",
    ends={
        Property(name="Element34", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedComment", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement35: BinaryAssociation = BinaryAssociation(
    name="annotatedElement35",
    ends={
        Property(name="CompleteDSLPckg_Element", type=CompleteDSLPckg_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Comment", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999))
    }
)
relatedElement36: BinaryAssociation = BinaryAssociation(
    name="relatedElement36",
    ends={
        Property(name="CompleteDSLPckg_Element37", type=CompleteDSLPckg_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Relationship", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="CompleteDSLPckg_Element39", type=CompleteDSLPckg_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DirectedRelationship", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="CompleteDSLPckg_Element42", type=CompleteDSLPckg_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DirectedRelationship41", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(1, 9999))
    }
)
upperValue43: BinaryAssociation = BinaryAssociation(
    name="upperValue43",
    ends={
        Property(name="ValueSpecification", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningUpper", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue44: BinaryAssociation = BinaryAssociation(
    name="lowerValue44",
    ends={
        Property(name="ValueSpecification45", type=CompleteDSLPckg_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLower", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification64: BinaryAssociation = BinaryAssociation(
    name="specification64",
    ends={
        Property(name="ValueSpecification65", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstanceSpec", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningConstraint49: BinaryAssociation = BinaryAssociation(
    name="owningConstraint49",
    ends={
        Property(name="Constraint50", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
owningSlot51: BinaryAssociation = BinaryAssociation(
    name="owningSlot51",
    ends={
        Property(name="Slot", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(0, 1))
    }
)
owningInstanceSpec52: BinaryAssociation = BinaryAssociation(
    name="owningInstanceSpec52",
    ends={
        Property(name="InstanceSpecification", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification53", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="CompleteDSLPckg_Type", type=CompleteDSLPckg_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TypedElement", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
package55: BinaryAssociation = BinaryAssociation(
    name="package55",
    ends={
        Property(name="Package56", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(0, 1))
    }
)
operand57: BinaryAssociation = BinaryAssociation(
    name="operand57",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Expression", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result58: BinaryAssociation = BinaryAssociation(
    name="result58",
    ends={
        Property(name="CompleteDSLPckg_Parameter", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueExpression", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
behavior59: BinaryAssociation = BinaryAssociation(
    name="behavior59",
    ends={
        Property(name="CompleteDSLPckg_Behavior", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueExpression60", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
instance61: BinaryAssociation = BinaryAssociation(
    name="instance61",
    ends={
        Property(name="CompleteDSLPckg_InstanceSpecification", type=CompleteDSLPckg_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InstanceValue", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot62: BinaryAssociation = BinaryAssociation(
    name="slot62",
    ends={
        Property(name="Slot63", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstace", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedClassifier91: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier91",
    ends={
        Property(name="CompleteDSLPckg_Classifier92", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier90", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
classifier66: BinaryAssociation = BinaryAssociation(
    name="classifier66",
    ends={
        Property(name="CompleteDSLPckg_Classifier", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InstanceSpecification67", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context68: BinaryAssociation = BinaryAssociation(
    name="context68",
    ends={
        Property(name="Namespace69", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=CompleteDSLPckg_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement70: BinaryAssociation = BinaryAssociation(
    name="constrainedElement70",
    ends={
        Property(name="CompleteDSLPckg_Element71", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Constraint", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification72: BinaryAssociation = BinaryAssociation(
    name="specification72",
    ends={
        Property(name="ValueSpecification73", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="owningConstraint", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningInstace74: BinaryAssociation = BinaryAssociation(
    name="owningInstace74",
    ends={
        Property(name="InstanceSpecification75", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=CompleteDSLPckg_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value76: BinaryAssociation = BinaryAssociation(
    name="value76",
    ends={
        Property(name="ValueSpecification77", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSlot", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature78: BinaryAssociation = BinaryAssociation(
    name="definingFeature78",
    ends={
        Property(name="CompleteDSLPckg_StructuralFeature", type=CompleteDSLPckg_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Slot", type=CompleteDSLPckg_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement80: BinaryAssociation = BinaryAssociation(
    name="redefinedElement80",
    ends={
        Property(name="CompleteDSLPckg_RedefinableElement", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RedefinableElement79", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext81: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext81",
    ends={
        Property(name="CompleteDSLPckg_Classifier83", type=CompleteDSLPckg_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RedefinableElement82", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember84: BinaryAssociation = BinaryAssociation(
    name="inheritedMember84",
    ends={
        Property(name="CompleteDSLPckg_NamedElement86", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier85", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature87: BinaryAssociation = BinaryAssociation(
    name="feature87",
    ends={
        Property(name="Feature", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=CompleteDSLPckg_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute88: BinaryAssociation = BinaryAssociation(
    name="attribute88",
    ends={
        Property(name="CompleteDSLPckg_Property", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier89", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general94: BinaryAssociation = BinaryAssociation(
    name="general94",
    ends={
        Property(name="CompleteDSLPckg_Classifier95", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier93", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization96: BinaryAssociation = BinaryAssociation(
    name="generalization96",
    ends={
        Property(name="Generalization", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution97: BinaryAssociation = BinaryAssociation(
    name="substitution97",
    ends={
        Property(name="Substitution", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent98: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent98",
    ends={
        Property(name="GeneralizationSet", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationUse99: BinaryAssociation = BinaryAssociation(
    name="collaborationUse99",
    ends={
        Property(name="CompleteDSLPckg_CollaborationUse", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier100", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representation101: BinaryAssociation = BinaryAssociation(
    name="representation101",
    ends={
        Property(name="CompleteDSLPckg_CollaborationUse103", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Classifier102", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier104: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier104",
    ends={
        Property(name="Classifier", type=CompleteDSLPckg_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter137: BinaryAssociation = BinaryAssociation(
    name="ownedParameter137",
    ends={
        Property(name="CompleteDSLPckg_Parameter138", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioralFeature", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_105: BinaryAssociation = BinaryAssociation(
    name="class_105",
    ends={
        Property(name="Class", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty107: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty107",
    ends={
        Property(name="CompleteDSLPckg_Property108", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property106", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue109: BinaryAssociation = BinaryAssociation(
    name="defaultValue109",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification111", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property110", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite113: BinaryAssociation = BinaryAssociation(
    name="opposite113",
    ends={
        Property(name="CompleteDSLPckg_Property114", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property112", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty116: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty116",
    ends={
        Property(name="CompleteDSLPckg_Property117", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Property115", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
association118: BinaryAssociation = BinaryAssociation(
    name="association118",
    ends={
        Property(name="Association", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation119: BinaryAssociation = BinaryAssociation(
    name="owningAssociation119",
    ends={
        Property(name="Association120", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
dataType121: BinaryAssociation = BinaryAssociation(
    name="dataType121",
    ends={
        Property(name="DataType", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute122", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface123: BinaryAssociation = BinaryAssociation(
    name="interface123",
    ends={
        Property(name="Interface", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute124", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 1))
    }
)
qualifier126: BinaryAssociation = BinaryAssociation(
    name="qualifier126",
    ends={
        Property(name="Property", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd128: BinaryAssociation = BinaryAssociation(
    name="associationEnd128",
    ends={
        Property(name="Property129", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
general130: BinaryAssociation = BinaryAssociation(
    name="general130",
    ends={
        Property(name="CompleteDSLPckg_Classifier131", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Generalization", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific132: BinaryAssociation = BinaryAssociation(
    name="specific132",
    ends={
        Property(name="Classifier133", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet134: BinaryAssociation = BinaryAssociation(
    name="generalizationSet134",
    ends={
        Property(name="GeneralizationSet136", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization135", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
dataType161: BinaryAssociation = BinaryAssociation(
    name="dataType161",
    ends={
        Property(name="DataType163", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation162", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(0, 1))
    }
)
raisedException139: BinaryAssociation = BinaryAssociation(
    name="raisedException139",
    ends={
        Property(name="CompleteDSLPckg_Type141", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioralFeature140", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedFormalParam142: BinaryAssociation = BinaryAssociation(
    name="ownedFormalParam142",
    ends={
        Property(name="CompleteDSLPckg_BehavioralFeature144", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Parameter143", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue145: BinaryAssociation = BinaryAssociation(
    name="defaultValue145",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification147", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Parameter146", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type148: BinaryAssociation = BinaryAssociation(
    name="type148",
    ends={
        Property(name="CompleteDSLPckg_Type149", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation", type=CompleteDSLPckg_Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition150: BinaryAssociation = BinaryAssociation(
    name="precondition150",
    ends={
        Property(name="CompleteDSLPckg_Constraint152", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation151", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition153: BinaryAssociation = BinaryAssociation(
    name="bodyCondition153",
    ends={
        Property(name="CompleteDSLPckg_Constraint155", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation154", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition156: BinaryAssociation = BinaryAssociation(
    name="postcondition156",
    ends={
        Property(name="CompleteDSLPckg_Constraint158", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Operation157", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_159: BinaryAssociation = BinaryAssociation(
    name="class_159",
    ends={
        Property(name="Class160", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 1))
    }
)
navigableOwnedEnd178: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd178",
    ends={
        Property(name="CompleteDSLPckg_Association", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999)),
        Property(name="CompleteDSLPckg_Property179", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1))
    }
)
interface164: BinaryAssociation = BinaryAssociation(
    name="interface164",
    ends={
        Property(name="Interface166", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation165", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier167: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier167",
    ends={
        Property(name="CompleteDSLPckg_Classifier168", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation169: BinaryAssociation = BinaryAssociation(
    name="ownedOperation169",
    ends={
        Property(name="Operation", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass171: BinaryAssociation = BinaryAssociation(
    name="superClass171",
    ends={
        Property(name="CompleteDSLPckg_Class172", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class170", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute173: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute173",
    ends={
        Property(name="Property175", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_174", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception176: BinaryAssociation = BinaryAssociation(
    name="ownedReception176",
    ends={
        Property(name="CompleteDSLPckg_Reception", type=CompleteDSLPckg_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Class177", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapping199: BinaryAssociation = BinaryAssociation(
    name="mapping199",
    ends={
        Property(name="CompleteDSLPckg_OpaqueExpression200", type=CompleteDSLPckg_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Abstraction", type=CompleteDSLPckg_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberEnd180: BinaryAssociation = BinaryAssociation(
    name="memberEnd180",
    ends={
        Property(name="Property181", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd182: BinaryAssociation = BinaryAssociation(
    name="ownedEnd182",
    ends={
        Property(name="Property183", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute184: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute184",
    ends={
        Property(name="Property185", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataType", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation186: BinaryAssociation = BinaryAssociation(
    name="ownedOperation186",
    ends={
        Property(name="Operation188", type=CompleteDSLPckg_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataType187", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral189: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral189",
    ends={
        Property(name="EnumerationLiteral", type=CompleteDSLPckg_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=CompleteDSLPckg_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration190: BinaryAssociation = BinaryAssociation(
    name="enumeration190",
    ends={
        Property(name="Enumeration", type=CompleteDSLPckg_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=CompleteDSLPckg_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage191: BinaryAssociation = BinaryAssociation(
    name="receivingPackage191",
    ends={
        Property(name="Package192", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage193: BinaryAssociation = BinaryAssociation(
    name="mergedPackage193",
    ends={
        Property(name="CompleteDSLPckg_Package194", type=CompleteDSLPckg_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_PackageMerge", type=CompleteDSLPckg_Package, multiplicity=Multiplicity(1, 1))
    }
)
client195: BinaryAssociation = BinaryAssociation(
    name="client195",
    ends={
        Property(name="NamedElement196", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier197: BinaryAssociation = BinaryAssociation(
    name="supplier197",
    ends={
        Property(name="CompleteDSLPckg_NamedElement198", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Dependency", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
substitutingClassifier201: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier201",
    ends={
        Property(name="Classifier202", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract203: BinaryAssociation = BinaryAssociation(
    name="contract203",
    ends={
        Property(name="CompleteDSLPckg_Classifier204", type=CompleteDSLPckg_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Substitution", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
nestedClassifier205: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier205",
    ends={
        Property(name="CompleteDSLPckg_Classifier206", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedInterface208: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface208",
    ends={
        Property(name="CompleteDSLPckg_Interface209", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface207", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute210: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute210",
    ends={
        Property(name="Property211", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation212: BinaryAssociation = BinaryAssociation(
    name="ownedOperation212",
    ends={
        Property(name="Operation214", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface213", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReception215: BinaryAssociation = BinaryAssociation(
    name="ownedReception215",
    ends={
        Property(name="CompleteDSLPckg_Reception217", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interface216", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementingClassifier218: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier218",
    ends={
        Property(name="BehavioredClassifier", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaceRealization", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
contract219: BinaryAssociation = BinaryAssociation(
    name="contract219",
    ends={
        Property(name="CompleteDSLPckg_Interface220", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterfaceRealization", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRealization221: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization221",
    ends={
        Property(name="InterfaceRealization", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=CompleteDSLPckg_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBehavior222: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior222",
    ends={
        Property(name="CompleteDSLPckg_Behavior223", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioredClassifier", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior224: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior224",
    ends={
        Property(name="CompleteDSLPckg_Behavior226", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehavioredClassifier225", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
event254: BinaryAssociation = BinaryAssociation(
    name="event254",
    ends={
        Property(name="CompleteDSLPckg_Event", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Trigger", type=CompleteDSLPckg_Event, multiplicity=Multiplicity(1, 1))
    }
)
powertype227: BinaryAssociation = BinaryAssociation(
    name="powertype227",
    ends={
        Property(name="Classifier228", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization229: BinaryAssociation = BinaryAssociation(
    name="generalization229",
    ends={
        Property(name="Generalization230", type=CompleteDSLPckg_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=CompleteDSLPckg_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
context231: BinaryAssociation = BinaryAssociation(
    name="context231",
    ends={
        Property(name="CompleteDSLPckg_BehavioredClassifier233", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior232", type=CompleteDSLPckg_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
redefinedBehavior235: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior235",
    ends={
        Property(name="CompleteDSLPckg_Behavior236", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior234", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
specification237: BinaryAssociation = BinaryAssociation(
    name="specification237",
    ends={
        Property(name="CompleteDSLPckg_BehavioralFeature239", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior238", type=CompleteDSLPckg_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter240: BinaryAssociation = BinaryAssociation(
    name="ownedParameter240",
    ends={
        Property(name="CompleteDSLPckg_Parameter242", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior241", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition243: BinaryAssociation = BinaryAssociation(
    name="precondition243",
    ends={
        Property(name="CompleteDSLPckg_Constraint245", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior244", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition246: BinaryAssociation = BinaryAssociation(
    name="postcondition246",
    ends={
        Property(name="CompleteDSLPckg_Constraint248", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Behavior247", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute249: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute249",
    ends={
        Property(name="CompleteDSLPckg_Property250", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Signal", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal251: BinaryAssociation = BinaryAssociation(
    name="signal251",
    ends={
        Property(name="CompleteDSLPckg_Signal253", type=CompleteDSLPckg_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Reception252", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
observation273: BinaryAssociation = BinaryAssociation(
    name="observation273",
    ends={
        Property(name="CompleteDSLPckg_Observation275", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Duration274", type=CompleteDSLPckg_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
signal255: BinaryAssociation = BinaryAssociation(
    name="signal255",
    ends={
        Property(name="CompleteDSLPckg_Signal256", type=CompleteDSLPckg_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SignalEvent", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation257: BinaryAssociation = BinaryAssociation(
    name="operation257",
    ends={
        Property(name="CompleteDSLPckg_Operation258", type=CompleteDSLPckg_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallEvent", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1))
    }
)
changeExpression259: BinaryAssociation = BinaryAssociation(
    name="changeExpression259",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification260", type=CompleteDSLPckg_ChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ChangeEvent", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
when261: BinaryAssociation = BinaryAssociation(
    name="when261",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression", type=CompleteDSLPckg_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeEvent", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr262: BinaryAssociation = BinaryAssociation(
    name="expr262",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification264", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeExpression263", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
observation265: BinaryAssociation = BinaryAssociation(
    name="observation265",
    ends={
        Property(name="CompleteDSLPckg_Observation", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeExpression266", type=CompleteDSLPckg_Observation, multiplicity=Multiplicity(0, 9999))
    }
)
event267: BinaryAssociation = BinaryAssociation(
    name="event267",
    ends={
        Property(name="CompleteDSLPckg_NamedElement268", type=CompleteDSLPckg_TimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeObservation", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
event269: BinaryAssociation = BinaryAssociation(
    name="event269",
    ends={
        Property(name="CompleteDSLPckg_NamedElement270", type=CompleteDSLPckg_DurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationObservation", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(1, 2))
    }
)
expr271: BinaryAssociation = BinaryAssociation(
    name="expr271",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification272", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Duration", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max276: BinaryAssociation = BinaryAssociation(
    name="max276",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification277", type=CompleteDSLPckg_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interval", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
min278: BinaryAssociation = BinaryAssociation(
    name="min278",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification280", type=CompleteDSLPckg_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interval279", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
timeMax281: BinaryAssociation = BinaryAssociation(
    name="timeMax281",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression282", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeInterval", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
timeMin283: BinaryAssociation = BinaryAssociation(
    name="timeMin283",
    ends={
        Property(name="CompleteDSLPckg_TimeExpression285", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeInterval284", type=CompleteDSLPckg_TimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
durationMax286: BinaryAssociation = BinaryAssociation(
    name="durationMax286",
    ends={
        Property(name="CompleteDSLPckg_Duration287", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationInterval", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1))
    }
)
durationMin288: BinaryAssociation = BinaryAssociation(
    name="durationMin288",
    ends={
        Property(name="CompleteDSLPckg_Duration290", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationInterval289", type=CompleteDSLPckg_Duration, multiplicity=Multiplicity(1, 1))
    }
)
timeSpecification291: BinaryAssociation = BinaryAssociation(
    name="timeSpecification291",
    ends={
        Property(name="CompleteDSLPckg_TimeInterval292", type=CompleteDSLPckg_TimeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TimeConstraint", type=CompleteDSLPckg_TimeInterval, multiplicity=Multiplicity(1, 1))
    }
)
durationSpecification293: BinaryAssociation = BinaryAssociation(
    name="durationSpecification293",
    ends={
        Property(name="CompleteDSLPckg_DurationInterval294", type=CompleteDSLPckg_DurationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DurationConstraint", type=CompleteDSLPckg_DurationInterval, multiplicity=Multiplicity(1, 1))
    }
)
required295: BinaryAssociation = BinaryAssociation(
    name="required295",
    ends={
        Property(name="CompleteDSLPckg_Interface296", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided297: BinaryAssociation = BinaryAssociation(
    name="provided297",
    ends={
        Property(name="CompleteDSLPckg_Interface299", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component298", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
realization300: BinaryAssociation = BinaryAssociation(
    name="realization300",
    ends={
        Property(name="CompleteDSLPckg_ComponentRealization", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component301", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement302: BinaryAssociation = BinaryAssociation(
    name="packagedElement302",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement304", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Component303", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstraction305: BinaryAssociation = BinaryAssociation(
    name="abstraction305",
    ends={
        Property(name="CompleteDSLPckg_Component307", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ComponentRealization306", type=CompleteDSLPckg_Component, multiplicity=Multiplicity(0, 1))
    }
)
realizingClassifier308: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier308",
    ends={
        Property(name="CompleteDSLPckg_Classifier310", type=CompleteDSLPckg_ComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ComponentRealization309", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
end311: BinaryAssociation = BinaryAssociation(
    name="end311",
    ends={
        Property(name="CompleteDSLPckg_ConnectorEnd", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
contract312: BinaryAssociation = BinaryAssociation(
    name="contract312",
    ends={
        Property(name="CompleteDSLPckg_Behavior314", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector313", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedConnector316: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector316",
    ends={
        Property(name="CompleteDSLPckg_Connector317", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Connector315", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 9999))
    }
)
partWithPort318: BinaryAssociation = BinaryAssociation(
    name="partWithPort318",
    ends={
        Property(name="CompleteDSLPckg_Property320", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd319", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
role321: BinaryAssociation = BinaryAssociation(
    name="role321",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd322", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
type323: BinaryAssociation = BinaryAssociation(
    name="type323",
    ends={
        Property(name="CompleteDSLPckg_Association325", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd324", type=CompleteDSLPckg_Association, multiplicity=Multiplicity(0, 1))
    }
)
definingEnd326: BinaryAssociation = BinaryAssociation(
    name="definingEnd326",
    ends={
        Property(name="CompleteDSLPckg_Property328", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectorEnd327", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
end329: BinaryAssociation = BinaryAssociation(
    name="end329",
    ends={
        Property(name="CompleteDSLPckg_ConnectorEnd331", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectableElement330", type=CompleteDSLPckg_ConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector332: BinaryAssociation = BinaryAssociation(
    name="ownedConnector332",
    ends={
        Property(name="CompleteDSLPckg_Connector333", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role334: BinaryAssociation = BinaryAssociation(
    name="role334",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement336", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier335", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
structuredOwnedAttribute337: BinaryAssociation = BinaryAssociation(
    name="structuredOwnedAttribute337",
    ends={
        Property(name="CompleteDSLPckg_Property339", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier338", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part340: BinaryAssociation = BinaryAssociation(
    name="part340",
    ends={
        Property(name="CompleteDSLPckg_Property342", type=CompleteDSLPckg_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredClassifier341", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999))
    }
)
manifestation371: BinaryAssociation = BinaryAssociation(
    name="manifestation371",
    ends={
        Property(name="CompleteDSLPckg_Manifestation", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact372", type=CompleteDSLPckg_Manifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required343: BinaryAssociation = BinaryAssociation(
    name="required343",
    ends={
        Property(name="CompleteDSLPckg_Interface344", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
provided345: BinaryAssociation = BinaryAssociation(
    name="provided345",
    ends={
        Property(name="CompleteDSLPckg_Interface347", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port346", type=CompleteDSLPckg_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort349: BinaryAssociation = BinaryAssociation(
    name="redefinedPort349",
    ends={
        Property(name="CompleteDSLPckg_Port350", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Port348", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPort351: BinaryAssociation = BinaryAssociation(
    name="ownedPort351",
    ends={
        Property(name="CompleteDSLPckg_Port352", type=CompleteDSLPckg_EncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_EncapsulatedClassifier", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborationRole353: BinaryAssociation = BinaryAssociation(
    name="collaborationRole353",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement354", type=CompleteDSLPckg_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Collaboration", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
type355: BinaryAssociation = BinaryAssociation(
    name="type355",
    ends={
        Property(name="CompleteDSLPckg_Collaboration357", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CollaborationUse356", type=CompleteDSLPckg_Collaboration, multiplicity=Multiplicity(1, 1))
    }
)
roleBinding358: BinaryAssociation = BinaryAssociation(
    name="roleBinding358",
    ends={
        Property(name="CompleteDSLPckg_Dependency360", type=CompleteDSLPckg_CollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CollaborationUse359", type=CompleteDSLPckg_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onPort361: BinaryAssociation = BinaryAssociation(
    name="onPort361",
    ends={
        Property(name="CompleteDSLPckg_Port362", type=CompleteDSLPckg_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InvocationAction", type=CompleteDSLPckg_Port, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperation363: BinaryAssociation = BinaryAssociation(
    name="ownedOperation363",
    ends={
        Property(name="CompleteDSLPckg_Operation364", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute365: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute365",
    ends={
        Property(name="CompleteDSLPckg_Property367", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact366", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedArtifact369: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact369",
    ends={
        Property(name="CompleteDSLPckg_Artifact370", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Artifact368", type=CompleteDSLPckg_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input394: BinaryAssociation = BinaryAssociation(
    name="input394",
    ends={
        Property(name="CompleteDSLPckg_Action395", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="CompleteDSLPckg_InputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1))
    }
)
output396: BinaryAssociation = BinaryAssociation(
    name="output396",
    ends={
        Property(name="CompleteDSLPckg_OutputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Action397", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizedElement373: BinaryAssociation = BinaryAssociation(
    name="utilizedElement373",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement375", type=CompleteDSLPckg_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Manifestation374", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
nestedNode377: BinaryAssociation = BinaryAssociation(
    name="nestedNode377",
    ends={
        Property(name="CompleteDSLPckg_Node", type=CompleteDSLPckg_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Node376", type=CompleteDSLPckg_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployedElement378: BinaryAssociation = BinaryAssociation(
    name="deployedElement378",
    ends={
        Property(name="CompleteDSLPckg_PackageableElement379", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentTarget", type=CompleteDSLPckg_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployment380: BinaryAssociation = BinaryAssociation(
    name="deployment380",
    ends={
        Property(name="CompleteDSLPckg_Deployment", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentTarget381", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location382: BinaryAssociation = BinaryAssociation(
    name="location382",
    ends={
        Property(name="CompleteDSLPckg_DeploymentTarget384", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment383", type=CompleteDSLPckg_DeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
deployedArtifact385: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact385",
    ends={
        Property(name="CompleteDSLPckg_DeployedArtifact", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment386", type=CompleteDSLPckg_DeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
configuration387: BinaryAssociation = BinaryAssociation(
    name="configuration387",
    ends={
        Property(name="CompleteDSLPckg_DeploymentSpecification", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Deployment388", type=CompleteDSLPckg_DeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployment389: BinaryAssociation = BinaryAssociation(
    name="deployment389",
    ends={
        Property(name="CompleteDSLPckg_Deployment391", type=CompleteDSLPckg_DeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DeploymentSpecification390", type=CompleteDSLPckg_Deployment, multiplicity=Multiplicity(0, 1))
    }
)
context392: BinaryAssociation = BinaryAssociation(
    name="context392",
    ends={
        Property(name="CompleteDSLPckg_Classifier393", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Action", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
signal419: BinaryAssociation = BinaryAssociation(
    name="signal419",
    ends={
        Property(name="CompleteDSLPckg_Signal420", type=CompleteDSLPckg_BroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BroadcastSignalAction", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
inputValue398: BinaryAssociation = BinaryAssociation(
    name="inputValue398",
    ends={
        Property(name="CompleteDSLPckg_InputPin399", type=CompleteDSLPckg_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputValue400: BinaryAssociation = BinaryAssociation(
    name="outputValue400",
    ends={
        Property(name="CompleteDSLPckg_OutputPin402", type=CompleteDSLPckg_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OpaqueAction401", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value403: BinaryAssociation = BinaryAssociation(
    name="value403",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification404", type=CompleteDSLPckg_ValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValuePin", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
result405: BinaryAssociation = BinaryAssociation(
    name="result405",
    ends={
        Property(name="CompleteDSLPckg_OutputPin406", type=CompleteDSLPckg_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior407: BinaryAssociation = BinaryAssociation(
    name="behavior407",
    ends={
        Property(name="CompleteDSLPckg_Behavior408", type=CompleteDSLPckg_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallBehaviorAction", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation409: BinaryAssociation = BinaryAssociation(
    name="operation409",
    ends={
        Property(name="CompleteDSLPckg_Operation410", type=CompleteDSLPckg_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallOperationAction", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target411: BinaryAssociation = BinaryAssociation(
    name="target411",
    ends={
        Property(name="CompleteDSLPckg_InputPin413", type=CompleteDSLPckg_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CallOperationAction412", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target414: BinaryAssociation = BinaryAssociation(
    name="target414",
    ends={
        Property(name="CompleteDSLPckg_InputPin415", type=CompleteDSLPckg_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendSignalAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal416: BinaryAssociation = BinaryAssociation(
    name="signal416",
    ends={
        Property(name="CompleteDSLPckg_Signal418", type=CompleteDSLPckg_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendSignalAction417", type=CompleteDSLPckg_Signal, multiplicity=Multiplicity(1, 1))
    }
)
object450: BinaryAssociation = BinaryAssociation(
    name="object450",
    ends={
        Property(name="CompleteDSLPckg_StructuralFeatureAction451", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CompleteDSLPckg_InputPin452", type=CompleteDSLPckg_StructuralFeatureAction, multiplicity=Multiplicity(1, 1))
    }
)
target421: BinaryAssociation = BinaryAssociation(
    name="target421",
    ends={
        Property(name="CompleteDSLPckg_InputPin422", type=CompleteDSLPckg_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request423: BinaryAssociation = BinaryAssociation(
    name="request423",
    ends={
        Property(name="CompleteDSLPckg_InputPin425", type=CompleteDSLPckg_SendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SendObjectAction424", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier426: BinaryAssociation = BinaryAssociation(
    name="classifier426",
    ends={
        Property(name="CompleteDSLPckg_Classifier427", type=CompleteDSLPckg_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateObjectAction", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result428: BinaryAssociation = BinaryAssociation(
    name="result428",
    ends={
        Property(name="CompleteDSLPckg_OutputPin430", type=CompleteDSLPckg_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateObjectAction429", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target431: BinaryAssociation = BinaryAssociation(
    name="target431",
    ends={
        Property(name="CompleteDSLPckg_InputPin432", type=CompleteDSLPckg_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DestroyObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result433: BinaryAssociation = BinaryAssociation(
    name="result433",
    ends={
        Property(name="CompleteDSLPckg_OutputPin434", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first435: BinaryAssociation = BinaryAssociation(
    name="first435",
    ends={
        Property(name="CompleteDSLPckg_InputPin437", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction436", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second438: BinaryAssociation = BinaryAssociation(
    name="second438",
    ends={
        Property(name="CompleteDSLPckg_InputPin440", type=CompleteDSLPckg_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_TestIdentityAction439", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result441: BinaryAssociation = BinaryAssociation(
    name="result441",
    ends={
        Property(name="CompleteDSLPckg_OutputPin442", type=CompleteDSLPckg_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadSelfAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result443: BinaryAssociation = BinaryAssociation(
    name="result443",
    ends={
        Property(name="CompleteDSLPckg_OutputPin444", type=CompleteDSLPckg_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValueSpecificationAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value445: BinaryAssociation = BinaryAssociation(
    name="value445",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification447", type=CompleteDSLPckg_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ValueSpecificationAction446", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuralFeature448: BinaryAssociation = BinaryAssociation(
    name="structuralFeature448",
    ends={
        Property(name="CompleteDSLPckg_StructuralFeature449", type=CompleteDSLPckg_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuralFeatureAction", type=CompleteDSLPckg_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
result453: BinaryAssociation = BinaryAssociation(
    name="result453",
    ends={
        Property(name="CompleteDSLPckg_OutputPin454", type=CompleteDSLPckg_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadStructuralFeatureAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value455: BinaryAssociation = BinaryAssociation(
    name="value455",
    ends={
        Property(name="CompleteDSLPckg_InputPin456", type=CompleteDSLPckg_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteStructuralFeatureAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result457: BinaryAssociation = BinaryAssociation(
    name="result457",
    ends={
        Property(name="CompleteDSLPckg_OutputPin459", type=CompleteDSLPckg_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteStructuralFeatureAction458", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt460: BinaryAssociation = BinaryAssociation(
    name="insertAt460",
    ends={
        Property(name="CompleteDSLPckg_InputPin461", type=CompleteDSLPckg_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AddStructuralFeatureValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt462: BinaryAssociation = BinaryAssociation(
    name="removeAt462",
    ends={
        Property(name="CompleteDSLPckg_InputPin463", type=CompleteDSLPckg_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RemoveStructuralFeatureValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result464: BinaryAssociation = BinaryAssociation(
    name="result464",
    ends={
        Property(name="CompleteDSLPckg_OutputPin465", type=CompleteDSLPckg_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ClearStructuralFeatureAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValue466: BinaryAssociation = BinaryAssociation(
    name="inputValue466",
    ends={
        Property(name="CompleteDSLPckg_InputPin467", type=CompleteDSLPckg_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
endData468: BinaryAssociation = BinaryAssociation(
    name="endData468",
    ends={
        Property(name="CompleteDSLPckg_LinkEndData", type=CompleteDSLPckg_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkAction469", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
value470: BinaryAssociation = BinaryAssociation(
    name="value470",
    ends={
        Property(name="CompleteDSLPckg_InputPin472", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData471", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end473: BinaryAssociation = BinaryAssociation(
    name="end473",
    ends={
        Property(name="CompleteDSLPckg_Property475", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData474", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
qualifier476: BinaryAssociation = BinaryAssociation(
    name="qualifier476",
    ends={
        Property(name="CompleteDSLPckg_QualifierValue", type=CompleteDSLPckg_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndData477", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result478: BinaryAssociation = BinaryAssociation(
    name="result478",
    ends={
        Property(name="CompleteDSLPckg_OutputPin479", type=CompleteDSLPckg_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnInformation505: BinaryAssociation = BinaryAssociation(
    name="returnInformation505",
    ends={
        Property(name="CompleteDSLPckg_OutputPin506", type=CompleteDSLPckg_AcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptCallAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt480: BinaryAssociation = BinaryAssociation(
    name="insertAt480",
    ends={
        Property(name="CompleteDSLPckg_InputPin481", type=CompleteDSLPckg_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndCreationData", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destroyAt482: BinaryAssociation = BinaryAssociation(
    name="destroyAt482",
    ends={
        Property(name="CompleteDSLPckg_InputPin483", type=CompleteDSLPckg_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LinkEndDestructionData", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnInformation484: BinaryAssociation = BinaryAssociation(
    name="returnInformation484",
    ends={
        Property(name="CompleteDSLPckg_InputPin485", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyValue486: BinaryAssociation = BinaryAssociation(
    name="replyValue486",
    ends={
        Property(name="CompleteDSLPckg_InputPin488", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction487", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replyToCall489: BinaryAssociation = BinaryAssociation(
    name="replyToCall489",
    ends={
        Property(name="CompleteDSLPckg_Trigger491", type=CompleteDSLPckg_ReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReplyAction490", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
object492: BinaryAssociation = BinaryAssociation(
    name="object492",
    ends={
        Property(name="CompleteDSLPckg_InputPin493", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unmarshallType494: BinaryAssociation = BinaryAssociation(
    name="unmarshallType494",
    ends={
        Property(name="CompleteDSLPckg_Classifier496", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction495", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result497: BinaryAssociation = BinaryAssociation(
    name="result497",
    ends={
        Property(name="CompleteDSLPckg_OutputPin499", type=CompleteDSLPckg_UnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UnmarshallAction498", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result500: BinaryAssociation = BinaryAssociation(
    name="result500",
    ends={
        Property(name="CompleteDSLPckg_OutputPin501", type=CompleteDSLPckg_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptEventAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger502: BinaryAssociation = BinaryAssociation(
    name="trigger502",
    ends={
        Property(name="CompleteDSLPckg_Trigger504", type=CompleteDSLPckg_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AcceptEventAction503", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
qualifier529: BinaryAssociation = BinaryAssociation(
    name="qualifier529",
    ends={
        Property(name="CompleteDSLPckg_Property531", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_QualifierValue530", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
result507: BinaryAssociation = BinaryAssociation(
    name="result507",
    ends={
        Property(name="CompleteDSLPckg_OutputPin508", type=CompleteDSLPckg_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadExtendAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier509: BinaryAssociation = BinaryAssociation(
    name="classifier509",
    ends={
        Property(name="CompleteDSLPckg_Classifier511", type=CompleteDSLPckg_ReadExtendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadExtendAction510", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
object512: BinaryAssociation = BinaryAssociation(
    name="object512",
    ends={
        Property(name="CompleteDSLPckg_InputPin513", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier514: BinaryAssociation = BinaryAssociation(
    name="oldClassifier514",
    ends={
        Property(name="CompleteDSLPckg_Classifier516", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction515", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier517: BinaryAssociation = BinaryAssociation(
    name="newClassifier517",
    ends={
        Property(name="CompleteDSLPckg_Classifier519", type=CompleteDSLPckg_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReclassifyObjectAction518", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
result520: BinaryAssociation = BinaryAssociation(
    name="result520",
    ends={
        Property(name="CompleteDSLPckg_OutputPin521", type=CompleteDSLPckg_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadlsClassifiedObjectAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object522: BinaryAssociation = BinaryAssociation(
    name="object522",
    ends={
        Property(name="CompleteDSLPckg_InputPin524", type=CompleteDSLPckg_ReadlsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadlsClassifiedObjectAction523", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object525: BinaryAssociation = BinaryAssociation(
    name="object525",
    ends={
        Property(name="CompleteDSLPckg_InputPin526", type=CompleteDSLPckg_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StartClassifierBehaviorAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object527: BinaryAssociation = BinaryAssociation(
    name="object527",
    ends={
        Property(name="CompleteDSLPckg_InputPin528", type=CompleteDSLPckg_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StartObjectBehaviorAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result551: BinaryAssociation = BinaryAssociation(
    name="result551",
    ends={
        Property(name="CompleteDSLPckg_OutputPin552", type=CompleteDSLPckg_CreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CreateLinkObjectAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value532: BinaryAssociation = BinaryAssociation(
    name="value532",
    ends={
        Property(name="CompleteDSLPckg_InputPin534", type=CompleteDSLPckg_QualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_QualifierValue533", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1))
    }
)
end535: BinaryAssociation = BinaryAssociation(
    name="end535",
    ends={
        Property(name="CompleteDSLPckg_Property536", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
object537: BinaryAssociation = BinaryAssociation(
    name="object537",
    ends={
        Property(name="CompleteDSLPckg_InputPin539", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction538", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result540: BinaryAssociation = BinaryAssociation(
    name="result540",
    ends={
        Property(name="CompleteDSLPckg_OutputPin542", type=CompleteDSLPckg_ReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndAction541", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object543: BinaryAssociation = BinaryAssociation(
    name="object543",
    ends={
        Property(name="CompleteDSLPckg_InputPin544", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result545: BinaryAssociation = BinaryAssociation(
    name="result545",
    ends={
        Property(name="CompleteDSLPckg_OutputPin547", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction546", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier548: BinaryAssociation = BinaryAssociation(
    name="qualifier548",
    ends={
        Property(name="CompleteDSLPckg_Property550", type=CompleteDSLPckg_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadLinkObjectEndQualifierAction549", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(1, 1))
    }
)
reducer558: BinaryAssociation = BinaryAssociation(
    name="reducer558",
    ends={
        Property(name="CompleteDSLPckg_Behavior560", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction559", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
variable561: BinaryAssociation = BinaryAssociation(
    name="variable561",
    ends={
        Property(name="CompleteDSLPckg_Variable", type=CompleteDSLPckg_VariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_VariableAction", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(1, 1))
    }
)
result553: BinaryAssociation = BinaryAssociation(
    name="result553",
    ends={
        Property(name="CompleteDSLPckg_OutputPin554", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection555: BinaryAssociation = BinaryAssociation(
    name="collection555",
    ends={
        Property(name="CompleteDSLPckg_InputPin557", type=CompleteDSLPckg_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReduceAction556", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fromAction572: BinaryAssociation = BinaryAssociation(
    name="fromAction572",
    ends={
        Property(name="CompleteDSLPckg_ActionInputPin", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CompleteDSLPckg_Action573", type=CompleteDSLPckg_ActionInputPin, multiplicity=Multiplicity(1, 1))
    }
)
region574: BinaryAssociation = BinaryAssociation(
    name="region574",
    ends={
        Property(name="CompleteDSLPckg_Region", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint575: BinaryAssociation = BinaryAssociation(
    name="connectionPoint575",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine576", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result562: BinaryAssociation = BinaryAssociation(
    name="result562",
    ends={
        Property(name="CompleteDSLPckg_OutputPin563", type=CompleteDSLPckg_ReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ReadVariableAction", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value564: BinaryAssociation = BinaryAssociation(
    name="value564",
    ends={
        Property(name="CompleteDSLPckg_InputPin565", type=CompleteDSLPckg_WriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_WriteVariableAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt566: BinaryAssociation = BinaryAssociation(
    name="insertAt566",
    ends={
        Property(name="CompleteDSLPckg_InputPin567", type=CompleteDSLPckg_AddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AddVariableValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt568: BinaryAssociation = BinaryAssociation(
    name="removeAt568",
    ends={
        Property(name="CompleteDSLPckg_InputPin569", type=CompleteDSLPckg_RemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RemoveVariableValueAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception570: BinaryAssociation = BinaryAssociation(
    name="exception570",
    ends={
        Property(name="CompleteDSLPckg_InputPin571", type=CompleteDSLPckg_RaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RaiseExceptionAction", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
incoming598: BinaryAssociation = BinaryAssociation(
    name="incoming598",
    ends={
        Property(name="CompleteDSLPckg_Transition600", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex599", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container601: BinaryAssociation = BinaryAssociation(
    name="container601",
    ends={
        Property(name="CompleteDSLPckg_Region603", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex602", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
source604: BinaryAssociation = BinaryAssociation(
    name="source604",
    ends={
        Property(name="CompleteDSLPckg_Vertex606", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition605", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
submachineState577: BinaryAssociation = BinaryAssociation(
    name="submachineState577",
    ends={
        Property(name="CompleteDSLPckg_State", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine578", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine580: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine580",
    ends={
        Property(name="CompleteDSLPckg_StateMachine581", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine579", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex582: BinaryAssociation = BinaryAssociation(
    name="subvertex582",
    ends={
        Property(name="CompleteDSLPckg_Vertex", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region583", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine584: BinaryAssociation = BinaryAssociation(
    name="stateMachine584",
    ends={
        Property(name="CompleteDSLPckg_StateMachine586", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region585", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition587: BinaryAssociation = BinaryAssociation(
    name="transition587",
    ends={
        Property(name="CompleteDSLPckg_Transition", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region588", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state589: BinaryAssociation = BinaryAssociation(
    name="state589",
    ends={
        Property(name="CompleteDSLPckg_State591", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region590", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion593: BinaryAssociation = BinaryAssociation(
    name="extendedRegion593",
    ends={
        Property(name="CompleteDSLPckg_Region594", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region592", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing595: BinaryAssociation = BinaryAssociation(
    name="outgoing595",
    ends={
        Property(name="CompleteDSLPckg_Transition597", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Vertex596", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
state625: BinaryAssociation = BinaryAssociation(
    name="state625",
    ends={
        Property(name="CompleteDSLPckg_State627", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Pseudostate626", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
exit628: BinaryAssociation = BinaryAssociation(
    name="exit628",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate629", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
entry630: BinaryAssociation = BinaryAssociation(
    name="entry630",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate632", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference631", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
target607: BinaryAssociation = BinaryAssociation(
    name="target607",
    ends={
        Property(name="CompleteDSLPckg_Vertex609", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition608", type=CompleteDSLPckg_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
effect610: BinaryAssociation = BinaryAssociation(
    name="effect610",
    ends={
        Property(name="CompleteDSLPckg_Behavior612", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition611", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger613: BinaryAssociation = BinaryAssociation(
    name="trigger613",
    ends={
        Property(name="CompleteDSLPckg_Trigger615", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition614", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard616: BinaryAssociation = BinaryAssociation(
    name="guard616",
    ends={
        Property(name="CompleteDSLPckg_Constraint618", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition617", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container619: BinaryAssociation = BinaryAssociation(
    name="container619",
    ends={
        Property(name="CompleteDSLPckg_Region621", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition620", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 1))
    }
)
redefinedTransition623: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition623",
    ends={
        Property(name="CompleteDSLPckg_Transition624", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition622", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 1))
    }
)
conformance666: BinaryAssociation = BinaryAssociation(
    name="conformance666",
    ends={
        Property(name="CompleteDSLPckg_ProtocolConformance", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolStateMachine", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificMachine667: BinaryAssociation = BinaryAssociation(
    name="specificMachine667",
    ends={
        Property(name="CompleteDSLPckg_ProtocolStateMachine669", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolConformance668", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine670: BinaryAssociation = BinaryAssociation(
    name="generalMachine670",
    ends={
        Property(name="CompleteDSLPckg_ProtocolStateMachine672", type=CompleteDSLPckg_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolConformance671", type=CompleteDSLPckg_ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
state633: BinaryAssociation = BinaryAssociation(
    name="state633",
    ends={
        Property(name="CompleteDSLPckg_State635", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConnectionPointReference634", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
connection636: BinaryAssociation = BinaryAssociation(
    name="connection636",
    ends={
        Property(name="CompleteDSLPckg_ConnectionPointReference638", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State637", type=CompleteDSLPckg_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint639: BinaryAssociation = BinaryAssociation(
    name="connectionPoint639",
    ends={
        Property(name="CompleteDSLPckg_Pseudostate641", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State640", type=CompleteDSLPckg_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine642: BinaryAssociation = BinaryAssociation(
    name="submachine642",
    ends={
        Property(name="CompleteDSLPckg_StateMachine644", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State643", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region645: BinaryAssociation = BinaryAssociation(
    name="region645",
    ends={
        Property(name="CompleteDSLPckg_Region647", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State646", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableTrigger648: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger648",
    ends={
        Property(name="CompleteDSLPckg_Trigger650", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State649", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit651: BinaryAssociation = BinaryAssociation(
    name="exit651",
    ends={
        Property(name="CompleteDSLPckg_Behavior653", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State652", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity654: BinaryAssociation = BinaryAssociation(
    name="doActivity654",
    ends={
        Property(name="CompleteDSLPckg_Behavior656", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State655", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry657: BinaryAssociation = BinaryAssociation(
    name="entry657",
    ends={
        Property(name="CompleteDSLPckg_Behavior659", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State658", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant660: BinaryAssociation = BinaryAssociation(
    name="stateInvariant660",
    ends={
        Property(name="CompleteDSLPckg_Constraint662", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State661", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState664: BinaryAssociation = BinaryAssociation(
    name="redefinedState664",
    ends={
        Property(name="CompleteDSLPckg_State665", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State663", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming699: BinaryAssociation = BinaryAssociation(
    name="incoming699",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge701", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode700", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing702: BinaryAssociation = BinaryAssociation(
    name="outgoing702",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge704", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode703", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition705: BinaryAssociation = BinaryAssociation(
    name="inPartition705",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition707", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode706", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion708: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion708",
    ends={
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode709", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
preCondition673: BinaryAssociation = BinaryAssociation(
    name="preCondition673",
    ends={
        Property(name="CompleteDSLPckg_Constraint674", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postCondition675: BinaryAssociation = BinaryAssociation(
    name="postCondition675",
    ends={
        Property(name="CompleteDSLPckg_Constraint677", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition676", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred678: BinaryAssociation = BinaryAssociation(
    name="referred678",
    ends={
        Property(name="CompleteDSLPckg_Operation680", type=CompleteDSLPckg_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ProtocolTransition679", type=CompleteDSLPckg_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
node681: BinaryAssociation = BinaryAssociation(
    name="node681",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group682: BinaryAssociation = BinaryAssociation(
    name="group682",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity683", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge684: BinaryAssociation = BinaryAssociation(
    name="edge684",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity685", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition686: BinaryAssociation = BinaryAssociation(
    name="partition686",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity687", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode688: BinaryAssociation = BinaryAssociation(
    name="structuredNode688",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity689", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable690: BinaryAssociation = BinaryAssociation(
    name="variable690",
    ends={
        Property(name="CompleteDSLPckg_Variable692", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Activity691", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inGroup693: BinaryAssociation = BinaryAssociation(
    name="inGroup693",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup695", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode694", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode697: BinaryAssociation = BinaryAssociation(
    name="redefinedNode697",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode698", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode696", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
guard742: BinaryAssociation = BinaryAssociation(
    name="guard742",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification744", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge743", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inPartition745: BinaryAssociation = BinaryAssociation(
    name="inPartition745",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition747", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge746", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
weight748: BinaryAssociation = BinaryAssociation(
    name="weight748",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification750", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge749", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interrupts751: BinaryAssociation = BinaryAssociation(
    name="interrupts751",
    ends={
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion753", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge752", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode754: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode754",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode756", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge755", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode710: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode710",
    ends={
        Property(name="CompleteDSLPckg_StructuredActivityNode712", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityNode711", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
subgroup714: BinaryAssociation = BinaryAssociation(
    name="subgroup714",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup715", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup713", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superGroup717: BinaryAssociation = BinaryAssociation(
    name="superGroup717",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup718", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup716", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
inActivity719: BinaryAssociation = BinaryAssociation(
    name="inActivity719",
    ends={
        Property(name="CompleteDSLPckg_Activity721", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup720", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(0, 1))
    }
)
containedNode722: BinaryAssociation = BinaryAssociation(
    name="containedNode722",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode724", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup723", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
containedEdge725: BinaryAssociation = BinaryAssociation(
    name="containedEdge725",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge727", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityGroup726", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
parameter728: BinaryAssociation = BinaryAssociation(
    name="parameter728",
    ends={
        Property(name="CompleteDSLPckg_Parameter729", type=CompleteDSLPckg_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityParameterNode", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
target730: BinaryAssociation = BinaryAssociation(
    name="target730",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode732", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge731", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source733: BinaryAssociation = BinaryAssociation(
    name="source733",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode735", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge734", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge737: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge737",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge738", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge736", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inGroup739: BinaryAssociation = BinaryAssociation(
    name="inGroup739",
    ends={
        Property(name="CompleteDSLPckg_ActivityGroup741", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityEdge740", type=CompleteDSLPckg_ActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
edge772: BinaryAssociation = BinaryAssociation(
    name="edge772",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge774", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition773", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
subpartition776: BinaryAssociation = BinaryAssociation(
    name="subpartition776",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition777", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition775", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superPartition779: BinaryAssociation = BinaryAssociation(
    name="superPartition779",
    ends={
        Property(name="CompleteDSLPckg_ActivityPartition780", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition778", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
represents781: BinaryAssociation = BinaryAssociation(
    name="represents781",
    ends={
        Property(name="CompleteDSLPckg_Element783", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition782", type=CompleteDSLPckg_Element, multiplicity=Multiplicity(0, 1))
    }
)
node784: BinaryAssociation = BinaryAssociation(
    name="node784",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode786", type=CompleteDSLPckg_ActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActivityPartition785", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
transformation757: BinaryAssociation = BinaryAssociation(
    name="transformation757",
    ends={
        Property(name="CompleteDSLPckg_Behavior758", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
selection759: BinaryAssociation = BinaryAssociation(
    name="selection759",
    ends={
        Property(name="CompleteDSLPckg_Behavior761", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow760", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
inState762: BinaryAssociation = BinaryAssociation(
    name="inState762",
    ends={
        Property(name="CompleteDSLPckg_State764", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ObjectFlow763", type=CompleteDSLPckg_State, multiplicity=Multiplicity(0, 9999))
    }
)
joinSpec765: BinaryAssociation = BinaryAssociation(
    name="joinSpec765",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification766", type=CompleteDSLPckg_JoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_JoinNode", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
decisionInputFlow767: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow767",
    ends={
        Property(name="CompleteDSLPckg_ObjectFlow768", type=CompleteDSLPckg_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DecisionNode", type=CompleteDSLPckg_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput769: BinaryAssociation = BinaryAssociation(
    name="decisionInput769",
    ends={
        Property(name="CompleteDSLPckg_Behavior771", type=CompleteDSLPckg_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_DecisionNode770", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
edge810: BinaryAssociation = BinaryAssociation(
    name="edge810",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge812", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode811", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput813: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput813",
    ends={
        Property(name="CompleteDSLPckg_OutputPin815", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode814", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler816: BinaryAssociation = BinaryAssociation(
    name="handler816",
    ends={
        Property(name="CompleteDSLPckg_ExceptionHandler", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutableNode", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter787: BinaryAssociation = BinaryAssociation(
    name="parameter787",
    ends={
        Property(name="CompleteDSLPckg_Parameter788", type=CompleteDSLPckg_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ParameterSet", type=CompleteDSLPckg_Parameter, multiplicity=Multiplicity(1, 9999))
    }
)
condition789: BinaryAssociation = BinaryAssociation(
    name="condition789",
    ends={
        Property(name="CompleteDSLPckg_Constraint791", type=CompleteDSLPckg_ParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ParameterSet790", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interruptingEdge792: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge792",
    ends={
        Property(name="CompleteDSLPckg_ActivityEdge794", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion793", type=CompleteDSLPckg_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node795: BinaryAssociation = BinaryAssociation(
    name="node795",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode797", type=CompleteDSLPckg_InterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InterruptibleActivityRegion796", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
activity798: BinaryAssociation = BinaryAssociation(
    name="activity798",
    ends={
        Property(name="CompleteDSLPckg_Activity800", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode799", type=CompleteDSLPckg_Activity, multiplicity=Multiplicity(0, 1))
    }
)
variable801: BinaryAssociation = BinaryAssociation(
    name="variable801",
    ends={
        Property(name="CompleteDSLPckg_Variable803", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode802", type=CompleteDSLPckg_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node804: BinaryAssociation = BinaryAssociation(
    name="node804",
    ends={
        Property(name="CompleteDSLPckg_ActivityNode806", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode805", type=CompleteDSLPckg_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput807: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput807",
    ends={
        Property(name="CompleteDSLPckg_InputPin809", type=CompleteDSLPckg_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StructuredActivityNode808", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessorClause851: BinaryAssociation = BinaryAssociation(
    name="predecessorClause851",
    ends={
        Property(name="CompleteDSLPckg_Clause852", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause850", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
sucessorClause854: BinaryAssociation = BinaryAssociation(
    name="sucessorClause854",
    ends={
        Property(name="CompleteDSLPckg_Clause855", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause853", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider856: BinaryAssociation = BinaryAssociation(
    name="decider856",
    ends={
        Property(name="CompleteDSLPckg_OutputPin858", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Clause857", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
executableNode859: BinaryAssociation = BinaryAssociation(
    name="executableNode859",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode860", type=CompleteDSLPckg_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_SequenceNode", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupPart817: BinaryAssociation = BinaryAssociation(
    name="setupPart817",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode818", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart819: BinaryAssociation = BinaryAssociation(
    name="bodyPart819",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode821", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode820", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test822: BinaryAssociation = BinaryAssociation(
    name="test822",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode824", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode823", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
decider825: BinaryAssociation = BinaryAssociation(
    name="decider825",
    ends={
        Property(name="CompleteDSLPckg_OutputPin827", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode826", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
loopVariableInput828: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput828",
    ends={
        Property(name="CompleteDSLPckg_InputPin830", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode829", type=CompleteDSLPckg_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable831: BinaryAssociation = BinaryAssociation(
    name="loopVariable831",
    ends={
        Property(name="CompleteDSLPckg_OutputPin833", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode832", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput834: BinaryAssociation = BinaryAssociation(
    name="bodyOutput834",
    ends={
        Property(name="CompleteDSLPckg_OutputPin836", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode835", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result837: BinaryAssociation = BinaryAssociation(
    name="result837",
    ends={
        Property(name="CompleteDSLPckg_OutputPin839", type=CompleteDSLPckg_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_LoopNode838", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clause840: BinaryAssociation = BinaryAssociation(
    name="clause840",
    ends={
        Property(name="CompleteDSLPckg_Clause", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode", type=CompleteDSLPckg_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
test841: BinaryAssociation = BinaryAssociation(
    name="test841",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode843", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode842", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body844: BinaryAssociation = BinaryAssociation(
    name="body844",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode846", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode845", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
result847: BinaryAssociation = BinaryAssociation(
    name="result847",
    ends={
        Property(name="CompleteDSLPckg_OutputPin849", type=CompleteDSLPckg_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConditionalNode848", type=CompleteDSLPckg_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputElement872: BinaryAssociation = BinaryAssociation(
    name="inputElement872",
    ends={
        Property(name="CompleteDSLPckg_ExpansionNode", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionRegion", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement873: BinaryAssociation = BinaryAssociation(
    name="outputElement873",
    ends={
        Property(name="CompleteDSLPckg_ExpansionNode875", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionRegion874", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
handlerBody861: BinaryAssociation = BinaryAssociation(
    name="handlerBody861",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode863", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler862", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode864: BinaryAssociation = BinaryAssociation(
    name="protectedNode864",
    ends={
        Property(name="CompleteDSLPckg_ExecutableNode866", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler865", type=CompleteDSLPckg_ExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput867: BinaryAssociation = BinaryAssociation(
    name="exceptionInput867",
    ends={
        Property(name="CompleteDSLPckg_ObjectNode", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler868", type=CompleteDSLPckg_ObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType869: BinaryAssociation = BinaryAssociation(
    name="exceptionType869",
    ends={
        Property(name="CompleteDSLPckg_Classifier871", type=CompleteDSLPckg_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExceptionHandler870", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
fragment899: BinaryAssociation = BinaryAssociation(
    name="fragment899",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment900", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeline901: BinaryAssociation = BinaryAssociation(
    name="lifeline901",
    ends={
        Property(name="CompleteDSLPckg_Lifeline903", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction902", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action904: BinaryAssociation = BinaryAssociation(
    name="action904",
    ends={
        Property(name="CompleteDSLPckg_Action906", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction905", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGate907: BinaryAssociation = BinaryAssociation(
    name="formalGate907",
    ends={
        Property(name="CompleteDSLPckg_Gate", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Interaction908", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coveredBy909: BinaryAssociation = BinaryAssociation(
    name="coveredBy909",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment911", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline910", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
regionAsInput876: BinaryAssociation = BinaryAssociation(
    name="regionAsInput876",
    ends={
        Property(name="CompleteDSLPckg_ExpansionRegion878", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionNode877", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput879: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput879",
    ends={
        Property(name="CompleteDSLPckg_ExpansionRegion881", type=CompleteDSLPckg_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExpansionNode880", type=CompleteDSLPckg_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
covered882: BinaryAssociation = BinaryAssociation(
    name="covered882",
    ends={
        Property(name="CompleteDSLPckg_Lifeline", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(0, 9999))
    }
)
generalOrdering883: BinaryAssociation = BinaryAssociation(
    name="generalOrdering883",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment884", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enclosingOperand885: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand885",
    ends={
        Property(name="CompleteDSLPckg_InteractionOperand", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionFragment886", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
start887: BinaryAssociation = BinaryAssociation(
    name="start887",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionSpecification", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
finish888: BinaryAssociation = BinaryAssociation(
    name="finish888",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification890", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionSpecification889", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
toBefore891: BinaryAssociation = BinaryAssociation(
    name="toBefore891",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering893", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OccurenceSpecification892", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
toAfter894: BinaryAssociation = BinaryAssociation(
    name="toAfter894",
    ends={
        Property(name="CompleteDSLPckg_GeneralOrdering896", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OccurenceSpecification895", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
invariant897: BinaryAssociation = BinaryAssociation(
    name="invariant897",
    ends={
        Property(name="CompleteDSLPckg_Constraint898", type=CompleteDSLPckg_StateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateInvariant", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message936: BinaryAssociation = BinaryAssociation(
    name="message936",
    ends={
        Property(name="CompleteDSLPckg_Message938", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_MessageEnd937", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(0, 1))
    }
)
execution939: BinaryAssociation = BinaryAssociation(
    name="execution939",
    ends={
        Property(name="CompleteDSLPckg_ExecutionSpecification940", type=CompleteDSLPckg_ExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExecutionOccurrenceSpecification", type=CompleteDSLPckg_ExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
interaction912: BinaryAssociation = BinaryAssociation(
    name="interaction912",
    ends={
        Property(name="CompleteDSLPckg_Interaction914", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline913", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
represents915: BinaryAssociation = BinaryAssociation(
    name="represents915",
    ends={
        Property(name="CompleteDSLPckg_ConnectableElement917", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline916", type=CompleteDSLPckg_ConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
selector918: BinaryAssociation = BinaryAssociation(
    name="selector918",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification920", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline919", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decomposedAs921: BinaryAssociation = BinaryAssociation(
    name="decomposedAs921",
    ends={
        Property(name="CompleteDSLPckg_PartDecomposition", type=CompleteDSLPckg_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Lifeline922", type=CompleteDSLPckg_PartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
argument923: BinaryAssociation = BinaryAssociation(
    name="argument923",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification924", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector925: BinaryAssociation = BinaryAssociation(
    name="connector925",
    ends={
        Property(name="CompleteDSLPckg_Connector927", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message926", type=CompleteDSLPckg_Connector, multiplicity=Multiplicity(0, 1))
    }
)
signature928: BinaryAssociation = BinaryAssociation(
    name="signature928",
    ends={
        Property(name="CompleteDSLPckg_NamedElement930", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message929", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent931: BinaryAssociation = BinaryAssociation(
    name="sendEvent931",
    ends={
        Property(name="CompleteDSLPckg_MessageEnd", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message932", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
receiveEvent933: BinaryAssociation = BinaryAssociation(
    name="receiveEvent933",
    ends={
        Property(name="CompleteDSLPckg_MessageEnd935", type=CompleteDSLPckg_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Message934", type=CompleteDSLPckg_MessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
message961: BinaryAssociation = BinaryAssociation(
    name="message961",
    ends={
        Property(name="CompleteDSLPckg_NamedElement962", type=CompleteDSLPckg_ConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ConsiderIgnoreFragment", type=CompleteDSLPckg_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
maxint963: BinaryAssociation = BinaryAssociation(
    name="maxint963",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification965", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionConstraint964", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minint966: BinaryAssociation = BinaryAssociation(
    name="minint966",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification968", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionConstraint967", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavior941: BinaryAssociation = BinaryAssociation(
    name="behavior941",
    ends={
        Property(name="CompleteDSLPckg_Behavior942", type=CompleteDSLPckg_BehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_BehaviorExecutionSpecification", type=CompleteDSLPckg_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
action943: BinaryAssociation = BinaryAssociation(
    name="action943",
    ends={
        Property(name="CompleteDSLPckg_Action944", type=CompleteDSLPckg_ActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ActionExecutionSpecification", type=CompleteDSLPckg_Action, multiplicity=Multiplicity(1, 1))
    }
)
after945: BinaryAssociation = BinaryAssociation(
    name="after945",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification947", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_GeneralOrdering946", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
before948: BinaryAssociation = BinaryAssociation(
    name="before948",
    ends={
        Property(name="CompleteDSLPckg_OccurenceSpecification950", type=CompleteDSLPckg_GeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_GeneralOrdering949", type=CompleteDSLPckg_OccurenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
fragment951: BinaryAssociation = BinaryAssociation(
    name="fragment951",
    ends={
        Property(name="CompleteDSLPckg_InteractionFragment953", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionOperand952", type=CompleteDSLPckg_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard954: BinaryAssociation = BinaryAssociation(
    name="guard954",
    ends={
        Property(name="CompleteDSLPckg_InteractionConstraint", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionOperand955", type=CompleteDSLPckg_InteractionConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand956: BinaryAssociation = BinaryAssociation(
    name="operand956",
    ends={
        Property(name="CompleteDSLPckg_InteractionOperand957", type=CompleteDSLPckg_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CombinedFragment", type=CompleteDSLPckg_InteractionOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cfragmentGate958: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate958",
    ends={
        Property(name="CompleteDSLPckg_Gate960", type=CompleteDSLPckg_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_CombinedFragment959", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionLocation994: BinaryAssociation = BinaryAssociation(
    name="extensionLocation994",
    ends={
        Property(name="CompleteDSLPckg_ExtensionPoint996", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend995", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension997: BinaryAssociation = BinaryAssociation(
    name="extension997",
    ends={
        Property(name="CompleteDSLPckg_UseCase999", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend998", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition1000: BinaryAssociation = BinaryAssociation(
    name="condition1000",
    ends={
        Property(name="CompleteDSLPckg_Constraint1002", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1001", type=CompleteDSLPckg_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedCase1003: BinaryAssociation = BinaryAssociation(
    name="extendedCase1003",
    ends={
        Property(name="CompleteDSLPckg_UseCase1005", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Extend1004", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
actualGate969: BinaryAssociation = BinaryAssociation(
    name="actualGate969",
    ends={
        Property(name="CompleteDSLPckg_Gate970", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse", type=CompleteDSLPckg_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument971: BinaryAssociation = BinaryAssociation(
    name="argument971",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification973", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse972", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue974: BinaryAssociation = BinaryAssociation(
    name="returnValue974",
    ends={
        Property(name="CompleteDSLPckg_ValueSpecification976", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse975", type=CompleteDSLPckg_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValueRecipient977: BinaryAssociation = BinaryAssociation(
    name="returnValueRecipient977",
    ends={
        Property(name="CompleteDSLPckg_Property979", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse978", type=CompleteDSLPckg_Property, multiplicity=Multiplicity(0, 1))
    }
)
refersTo980: BinaryAssociation = BinaryAssociation(
    name="refersTo980",
    ends={
        Property(name="CompleteDSLPckg_Interaction982", type=CompleteDSLPckg_InteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_InteractionUse981", type=CompleteDSLPckg_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
subject983: BinaryAssociation = BinaryAssociation(
    name="subject983",
    ends={
        Property(name="CompleteDSLPckg_Classifier984", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase", type=CompleteDSLPckg_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint985: BinaryAssociation = BinaryAssociation(
    name="extensionPoint985",
    ends={
        Property(name="CompleteDSLPckg_ExtensionPoint", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase986", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend987: BinaryAssociation = BinaryAssociation(
    name="extend987",
    ends={
        Property(name="CompleteDSLPckg_Extend", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase988", type=CompleteDSLPckg_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include989: BinaryAssociation = BinaryAssociation(
    name="include989",
    ends={
        Property(name="CompleteDSLPckg_Include", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_UseCase990", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(0, 9999))
    }
)
useCase991: BinaryAssociation = BinaryAssociation(
    name="useCase991",
    ends={
        Property(name="CompleteDSLPckg_UseCase993", type=CompleteDSLPckg_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ExtensionPoint992", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase1006: BinaryAssociation = BinaryAssociation(
    name="includingCase1006",
    ends={
        Property(name="CompleteDSLPckg_UseCase1008", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Include1007", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
addition1009: BinaryAssociation = BinaryAssociation(
    name="addition1009",
    ends={
        Property(name="CompleteDSLPckg_UseCase1011", type=CompleteDSLPckg_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Include1010", type=CompleteDSLPckg_UseCase, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CompleteDSLPckg_Namespace_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Namespace)
gen_CompleteDSLPckg_NamedElement_Element = Generalization(general=Element, specific=CompleteDSLPckg_NamedElement)
gen_CompleteDSLPckg_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_PackageableElement)
gen_CompleteDSLPckg_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_ElementImport)
gen_CompleteDSLPckg_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_PackageImport)
gen_CompleteDSLPckg_Package_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Package)
gen_CompleteDSLPckg_Package_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Package)
gen_CompleteDSLPckg_Comment_Element = Generalization(general=Element, specific=CompleteDSLPckg_Comment)
gen_CompleteDSLPckg_Relationship_Element = Generalization(general=Element, specific=CompleteDSLPckg_Relationship)
gen_CompleteDSLPckg_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=CompleteDSLPckg_DirectedRelationship)
gen_CompleteDSLPckg_MultiplicityElement_Element = Generalization(general=Element, specific=CompleteDSLPckg_MultiplicityElement)
gen_CompleteDSLPckg_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ValueSpecification)
gen_CompleteDSLPckg_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_ValueSpecification)
gen_CompleteDSLPckg_TypedElement_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_TypedElement)
gen_CompleteDSLPckg_Type_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Type)
gen_CompleteDSLPckg_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Expression)
gen_CompleteDSLPckg_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_OpaqueExpression)
gen_CompleteDSLPckg_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_LiteralSpecification)
gen_CompleteDSLPckg_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralNull)
gen_CompleteDSLPckg_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralBoolean)
gen_CompleteDSLPckg_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralInteger)
gen_CompleteDSLPckg_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralReal)
gen_CompleteDSLPckg_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralString)
gen_CompleteDSLPckg_LiteralUnilimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=CompleteDSLPckg_LiteralUnilimitedNatural)
gen_CompleteDSLPckg_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_InstanceSpecification)
gen_CompleteDSLPckg_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Constraint)
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
gen_CompleteDSLPckg_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Generalization)
gen_CompleteDSLPckg_BehavioralFeature_Feature = Generalization(general=Feature, specific=CompleteDSLPckg_BehavioralFeature)
gen_CompleteDSLPckg_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_BehavioralFeature)
gen_CompleteDSLPckg_Parameter_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Parameter)
gen_CompleteDSLPckg_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CompleteDSLPckg_Operation)
gen_CompleteDSLPckg_Class_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=CompleteDSLPckg_Class)
gen_CompleteDSLPckg_Association_Relationship = Generalization(general=Relationship, specific=CompleteDSLPckg_Association)
gen_CompleteDSLPckg_Association_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Association)
gen_CompleteDSLPckg_DataType_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_DataType)
gen_CompleteDSLPckg_PrimitiveType_DataType = Generalization(general=DataType, specific=CompleteDSLPckg_PrimitiveType)
gen_CompleteDSLPckg_Enumeration_DataType = Generalization(general=DataType, specific=CompleteDSLPckg_Enumeration)
gen_CompleteDSLPckg_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=CompleteDSLPckg_EnumerationLiteral)
gen_CompleteDSLPckg_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_PackageMerge)
gen_CompleteDSLPckg_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Dependency)
gen_CompleteDSLPckg_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Dependency)
gen_CompleteDSLPckg_Usage_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Usage)
gen_CompleteDSLPckg_Abstraction_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Abstraction)
gen_CompleteDSLPckg_Realization_Abstraction = Generalization(general=Abstraction, specific=CompleteDSLPckg_Realization)
gen_CompleteDSLPckg_Substitution_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_Substitution)
gen_CompleteDSLPckg_Interface_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Interface)
gen_CompleteDSLPckg_InterfaceRealization_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_InterfaceRealization)
gen_CompleteDSLPckg_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_BehavioredClassifier)
gen_CompleteDSLPckg_AssociationClass_Class = Generalization(general=Class_, specific=CompleteDSLPckg_AssociationClass)
gen_CompleteDSLPckg_AssociationClass_Association = Generalization(general=Association, specific=CompleteDSLPckg_AssociationClass)
gen_CompleteDSLPckg_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_GeneralizationSet)
gen_CompleteDSLPckg_Event_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Event)
gen_CompleteDSLPckg_Behavior_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Behavior)
gen_CompleteDSLPckg_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_OpaqueBehavior)
gen_CompleteDSLPckg_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=CompleteDSLPckg_FunctionBehavior)
gen_CompleteDSLPckg_Signal_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Signal)
gen_CompleteDSLPckg_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=CompleteDSLPckg_Reception)
gen_CompleteDSLPckg_Trigger_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Trigger)
gen_CompleteDSLPckg_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Interval)
gen_CompleteDSLPckg_MessageEvent_Event = Generalization(general=Event, specific=CompleteDSLPckg_MessageEvent)
gen_CompleteDSLPckg_AnyReceiveEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_AnyReceiveEvent)
gen_CompleteDSLPckg_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_SignalEvent)
gen_CompleteDSLPckg_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=CompleteDSLPckg_CallEvent)
gen_CompleteDSLPckg_ChangeEvent_Event = Generalization(general=Event, specific=CompleteDSLPckg_ChangeEvent)
gen_CompleteDSLPckg_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_TimeExpression)
gen_CompleteDSLPckg_Observation_PackageableElement = Generalization(general=PackageableElement, specific=CompleteDSLPckg_Observation)
gen_CompleteDSLPckg_TimeObservation_Observation = Generalization(general=Observation, specific=CompleteDSLPckg_TimeObservation)
gen_CompleteDSLPckg_DurationObservation_Observation = Generalization(general=Observation, specific=CompleteDSLPckg_DurationObservation)
gen_CompleteDSLPckg_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=CompleteDSLPckg_Duration)
gen_CompleteDSLPckg_ComponentRealization_Realization = Generalization(general=Realization, specific=CompleteDSLPckg_ComponentRealization)
gen_CompleteDSLPckg_TimeInterval_Interval = Generalization(general=Interval, specific=CompleteDSLPckg_TimeInterval)
gen_CompleteDSLPckg_DurationInterval_Interval = Generalization(general=Interval, specific=CompleteDSLPckg_DurationInterval)
gen_CompleteDSLPckg_IntervalConstraint_Constraint = Generalization(general=Constraint, specific=CompleteDSLPckg_IntervalConstraint)
gen_CompleteDSLPckg_TimeConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CompleteDSLPckg_TimeConstraint)
gen_CompleteDSLPckg_DurationConstraint_IntervalConstraint = Generalization(general=IntervalConstraint, specific=CompleteDSLPckg_DurationConstraint)
gen_CompleteDSLPckg_Component_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Component)
gen_CompleteDSLPckg_Component_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Component)
gen_CompleteDSLPckg_Port_Property = Generalization(general=Property_, specific=CompleteDSLPckg_Port)
gen_CompleteDSLPckg_Connector_Feature = Generalization(general=Feature, specific=CompleteDSLPckg_Connector)
gen_CompleteDSLPckg_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ConnectableElement)
gen_CompleteDSLPckg_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_StructuredClassifier)
gen_CompleteDSLPckg_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_EncapsulatedClassifier)
gen_CompleteDSLPckg_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=CompleteDSLPckg_Collaboration)
gen_CompleteDSLPckg_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Collaboration)
gen_CompleteDSLPckg_CollaborationUse_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_CollaborationUse)
gen_CompleteDSLPckg_Variable_ConnectableElement = Generalization(general=ConnectableElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Variable_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Variable)
gen_CompleteDSLPckg_Artifact_Classifier = Generalization(general=Classifier, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Artifact_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Artifact_DeployedArtifact = Generalization(general=DeployedArtifact, specific=CompleteDSLPckg_Artifact)
gen_CompleteDSLPckg_Manifestation_Abstraction = Generalization(general=Abstraction, specific=CompleteDSLPckg_Manifestation)
gen_CompleteDSLPckg_Node_Class = Generalization(general=Class_, specific=CompleteDSLPckg_Node)
gen_CompleteDSLPckg_Node_DeploymentTarget = Generalization(general=DeploymentTarget, specific=CompleteDSLPckg_Node)
gen_CompleteDSLPckg_Device_Node = Generalization(general=Node, specific=CompleteDSLPckg_Device)
gen_CompleteDSLPckg_ExecutionEnvironment_Node = Generalization(general=Node, specific=CompleteDSLPckg_ExecutionEnvironment)
gen_CompleteDSLPckg_CommunicationPath_Association = Generalization(general=Association, specific=CompleteDSLPckg_CommunicationPath)
gen_CompleteDSLPckg_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_DeploymentTarget)
gen_CompleteDSLPckg_Deployment_Dependency = Generalization(general=Dependency, specific=CompleteDSLPckg_Deployment)
gen_CompleteDSLPckg_DeployedArtifact_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_DeployedArtifact)
gen_CompleteDSLPckg_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=CompleteDSLPckg_DeploymentSpecification)
gen_CompleteDSLPckg_Action_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Action)
gen_CompleteDSLPckg_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_SendObjectAction)
gen_CompleteDSLPckg_OpaqueAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_OpaqueAction)
gen_CompleteDSLPckg_InputPin_Pin = Generalization(general=Pin, specific=CompleteDSLPckg_InputPin)
gen_CompleteDSLPckg_OutputPin_Pin = Generalization(general=Pin, specific=CompleteDSLPckg_OutputPin)
gen_CompleteDSLPckg_Pin_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_Pin)
gen_CompleteDSLPckg_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=CompleteDSLPckg_Pin)
gen_CompleteDSLPckg_ValuePin_InputPin = Generalization(general=InputPin, specific=CompleteDSLPckg_ValuePin)
gen_CompleteDSLPckg_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_CallAction)
gen_CompleteDSLPckg_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=CompleteDSLPckg_CallBehaviorAction)
gen_CompleteDSLPckg_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_SendSignalAction)
gen_CompleteDSLPckg_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=CompleteDSLPckg_BroadcastSignalAction)
gen_CompleteDSLPckg_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_ReadStructuralFeatureAction)
gen_CompleteDSLPckg_CreateObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_CreateObjectAction)
gen_CompleteDSLPckg_DestroyObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_DestroyObjectAction)
gen_CompleteDSLPckg_TestIdentityAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_TestIdentityAction)
gen_CompleteDSLPckg_ReadSelfAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadSelfAction)
gen_CompleteDSLPckg_ValueSpecificationAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ValueSpecificationAction)
gen_CompleteDSLPckg_StructuralFeatureAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_StructuralFeatureAction)
gen_CompleteDSLPckg_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=CompleteDSLPckg_CreateLinkAction)
gen_CompleteDSLPckg_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=CompleteDSLPckg_LinkEndCreationData)
gen_CompleteDSLPckg_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_WriteStructuralFeatureAction)
gen_CompleteDSLPckg_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=CompleteDSLPckg_AddStructuralFeatureValueAction)
gen_CompleteDSLPckg_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=CompleteDSLPckg_RemoveStructuralFeatureValueAction)
gen_CompleteDSLPckg_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=CompleteDSLPckg_ClearStructuralFeatureAction)
gen_CompleteDSLPckg_LinkAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_LinkAction)
gen_CompleteDSLPckg_LinkEndData_Element = Generalization(general=Element, specific=CompleteDSLPckg_LinkEndData)
gen_CompleteDSLPckg_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=CompleteDSLPckg_ReadLinkAction)
gen_CompleteDSLPckg_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=CompleteDSLPckg_WriteLinkAction)
gen_CompleteDSLPckg_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=CompleteDSLPckg_AcceptCallAction)
gen_CompleteDSLPckg_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=CompleteDSLPckg_DestroyLinkAction)
gen_CompleteDSLPckg_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=CompleteDSLPckg_LinkEndDestructionData)
gen_CompleteDSLPckg_ReplyAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReplyAction)
gen_CompleteDSLPckg_UnmarshallAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_UnmarshallAction)
gen_CompleteDSLPckg_AcceptEventAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_AcceptEventAction)
gen_CompleteDSLPckg_QualifierValue_Element = Generalization(general=Element, specific=CompleteDSLPckg_QualifierValue)
gen_CompleteDSLPckg_ReadExtendAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadExtendAction)
gen_CompleteDSLPckg_ReclassifyObjectAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReclassifyObjectAction)
gen_CompleteDSLPckg_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_StartClassifierBehaviorAction)
gen_CompleteDSLPckg_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=CompleteDSLPckg_StartObjectBehaviorAction)
gen_CompleteDSLPckg_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadLinkObjectEndAction)
gen_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReadLinkObjectEndQualifierAction)
gen_CompleteDSLPckg_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=CompleteDSLPckg_CreateLinkObjectAction)
gen_CompleteDSLPckg_VariableAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_VariableAction)
gen_CompleteDSLPckg_ReduceAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_ReduceAction)
gen_CompleteDSLPckg_StateMachine_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_StateMachine)
gen_CompleteDSLPckg_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_ReadVariableAction)
gen_CompleteDSLPckg_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_WriteVariableAction)
gen_CompleteDSLPckg_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=CompleteDSLPckg_AddVariableValueAction)
gen_CompleteDSLPckg_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=CompleteDSLPckg_RemoveVariableValueAction)
gen_CompleteDSLPckg_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=CompleteDSLPckg_ClearVariableAction)
gen_CompleteDSLPckg_RaiseExceptionAction_Action = Generalization(general=Action, specific=CompleteDSLPckg_RaiseExceptionAction)
gen_CompleteDSLPckg_ActionInputPin_InputPin = Generalization(general=InputPin, specific=CompleteDSLPckg_ActionInputPin)
gen_CompleteDSLPckg_Transition_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Transition)
gen_CompleteDSLPckg_Transition_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Transition)
gen_CompleteDSLPckg_Region_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_Region)
gen_CompleteDSLPckg_Region_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_Region)
gen_CompleteDSLPckg_Vertex_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Vertex)
gen_CompleteDSLPckg_Pseudostate_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_Pseudostate)
gen_CompleteDSLPckg_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_ConnectionPointReference)
gen_CompleteDSLPckg_FinalState_State = Generalization(general=State, specific=CompleteDSLPckg_FinalState)
gen_CompleteDSLPckg_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=CompleteDSLPckg_ProtocolStateMachine)
gen_CompleteDSLPckg_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_ProtocolConformance)
gen_CompleteDSLPckg_State_Vertex = Generalization(general=Vertex, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_State_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_State_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_ProtocolTransition_Transition = Generalization(general=Transition, specific=CompleteDSLPckg_ProtocolTransition)
gen_CompleteDSLPckg_Activity_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_Activity)
gen_CompleteDSLPckg_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ActivityNode)
gen_CompleteDSLPckg_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ActivityNode)
gen_CompleteDSLPckg_ActivityGroup_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ActivityGroup)
gen_CompleteDSLPckg_ObjectNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ObjectNode)
gen_CompleteDSLPckg_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=CompleteDSLPckg_ObjectNode)
gen_CompleteDSLPckg_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_ActivityParameterNode)
gen_CompleteDSLPckg_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ControlNode)
gen_CompleteDSLPckg_ActivityFinalNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_ActivityFinalNode)
gen_CompleteDSLPckg_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=CompleteDSLPckg_ActivityFinalNode)
gen_CompleteDSLPckg_InitialNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_InitialNode)
gen_CompleteDSLPckg_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ActivityEdge)
gen_CompleteDSLPckg_ActivityPartition_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_ActivityPartition)
gen_CompleteDSLPckg_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=CompleteDSLPckg_ControlFlow)
gen_CompleteDSLPckg_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=CompleteDSLPckg_ObjectFlow)
gen_CompleteDSLPckg_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_CentralBufferNode)
gen_CompleteDSLPckg_FinalNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_FinalNode)
gen_CompleteDSLPckg_FlowFinalNode_FinalNode = Generalization(general=FinalNode, specific=CompleteDSLPckg_FlowFinalNode)
gen_CompleteDSLPckg_ForkNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_ForkNode)
gen_CompleteDSLPckg_JoinNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_JoinNode)
gen_CompleteDSLPckg_MergeNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_MergeNode)
gen_CompleteDSLPckg_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=CompleteDSLPckg_DecisionNode)
gen_CompleteDSLPckg_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=CompleteDSLPckg_ExecutableNode)
gen_CompleteDSLPckg_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_LoopNode)
gen_CompleteDSLPckg_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=CompleteDSLPckg_DataStoreNode)
gen_CompleteDSLPckg_ParameterSet_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_ParameterSet)
gen_CompleteDSLPckg_InterruptibleActivityRegion_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_InterruptibleActivityRegion)
gen_CompleteDSLPckg_StructuredActivityNode_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_ExecutableNode = Generalization(general=ExecutableNode, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_ActivityGroup = Generalization(general=ActivityGroup, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_StructuredActivityNode_Action = Generalization(general=Action, specific=CompleteDSLPckg_StructuredActivityNode)
gen_CompleteDSLPckg_Clause_Element = Generalization(general=Element, specific=CompleteDSLPckg_Clause)
gen_CompleteDSLPckg_SequenceNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_SequenceNode)
gen_CompleteDSLPckg_ExceptionHandler_Element = Generalization(general=Element, specific=CompleteDSLPckg_ExceptionHandler)
gen_CompleteDSLPckg_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_ConditionalNode)
gen_CompleteDSLPckg_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=CompleteDSLPckg_ExpansionRegion)
gen_CompleteDSLPckg_Lifeline_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Lifeline)
gen_CompleteDSLPckg_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=CompleteDSLPckg_ExpansionNode)
gen_CompleteDSLPckg_InteractionFragment_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_InteractionFragment)
gen_CompleteDSLPckg_ExecutionSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_ExecutionSpecification)
gen_CompleteDSLPckg_OccurenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_OccurenceSpecification)
gen_CompleteDSLPckg_StateInvariant_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_StateInvariant)
gen_CompleteDSLPckg_Interaction_Behavior = Generalization(general=Behavior, specific=CompleteDSLPckg_Interaction)
gen_CompleteDSLPckg_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_Interaction)
gen_CompleteDSLPckg_MessageEnd_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_MessageEnd)
gen_CompleteDSLPckg_ExecutionOccurrenceSpecification_OccurenceSpecification = Generalization(general=OccurenceSpecification, specific=CompleteDSLPckg_ExecutionOccurrenceSpecification)
gen_CompleteDSLPckg_MessageOccurrenceSpecification_OccurenceSpecification = Generalization(general=OccurenceSpecification, specific=CompleteDSLPckg_MessageOccurrenceSpecification)
gen_CompleteDSLPckg_DestructionOccurrenceSpecification_MessageOccurrenceSpecification = Generalization(general=MessageOccurrenceSpecification, specific=CompleteDSLPckg_DestructionOccurrenceSpecification)
gen_CompleteDSLPckg_BehaviorExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=CompleteDSLPckg_BehaviorExecutionSpecification)
gen_CompleteDSLPckg_Message_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Message)
gen_CompleteDSLPckg_Continuation_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_Continuation)
gen_CompleteDSLPckg_InteractionConstraint_Constraint = Generalization(general=Constraint, specific=CompleteDSLPckg_InteractionConstraint)
gen_CompleteDSLPckg_ActionExecutionSpecification_ExecutionSpecification = Generalization(general=ExecutionSpecification, specific=CompleteDSLPckg_ActionExecutionSpecification)
gen_CompleteDSLPckg_GeneralOrdering_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_GeneralOrdering)
gen_CompleteDSLPckg_InteractionOperand_Namespace = Generalization(general=Namespace, specific=CompleteDSLPckg_InteractionOperand)
gen_CompleteDSLPckg_ConsiderIgnoreFragment_CombinedFragment = Generalization(general=CombinedFragment, specific=CompleteDSLPckg_ConsiderIgnoreFragment)
gen_CompleteDSLPckg_Include_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Include)
gen_CompleteDSLPckg_Include_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Include)
gen_CompleteDSLPckg_Gate_MessageEnd = Generalization(general=MessageEnd, specific=CompleteDSLPckg_Gate)
gen_CompleteDSLPckg_InteractionUse_InteractionFragment = Generalization(general=InteractionFragment, specific=CompleteDSLPckg_InteractionUse)
gen_CompleteDSLPckg_PartDecomposition_InteractionUse = Generalization(general=InteractionUse, specific=CompleteDSLPckg_PartDecomposition)
gen_CompleteDSLPckg_Actor_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_Actor)
gen_CompleteDSLPckg_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=CompleteDSLPckg_UseCase)
gen_CompleteDSLPckg_ExtensionPoint_RedefinableElement = Generalization(general=RedefinableElement, specific=CompleteDSLPckg_ExtensionPoint)
gen_CompleteDSLPckg_Extend_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Extend)
gen_CompleteDSLPckg_Extend_DirectedRelationship = Generalization(general=DirectedRelationship, specific=CompleteDSLPckg_Extend)

# Domain Model
domain_model = DomainModel(
    name="CompleteDSLPckg",
    types={NamedElement, CompleteDSLPckg_Element, CompleteDSLPckg_Comment, CompleteDSLPckg_NamedElement, Element, CompleteDSLPckg_Namespace, CompleteDSLPckg_Dependency, CompleteDSLPckg_PackageableElement, CompleteDSLPckg_ElementImport, CompleteDSLPckg_PackageImport, CompleteDSLPckg_Constraint, DirectedRelationship, CompleteDSLPckg_Package, Namespace, PackageableElement, CompleteDSLPckg_Type, CompleteDSLPckg_PackageMerge, CompleteDSLPckg_Relationship, CompleteDSLPckg_DirectedRelationship, Relationship, CompleteDSLPckg_MultiplicityElement, CompleteDSLPckg_ValueSpecification, TypedElement, CompleteDSLPckg_Slot, CompleteDSLPckg_InstanceSpecification, CompleteDSLPckg_TypedElement, CompleteDSLPckg_Expression, ValueSpecification, CompleteDSLPckg_OpaqueExpression, CompleteDSLPckg_Parameter, CompleteDSLPckg_Behavior, CompleteDSLPckg_LiteralSpecification, CompleteDSLPckg_LiteralNull, LiteralSpecification, CompleteDSLPckg_LiteralBoolean, CompleteDSLPckg_LiteralInteger, CompleteDSLPckg_LiteralReal, CompleteDSLPckg_LiteralString, CompleteDSLPckg_LiteralUnilimitedNatural, CompleteDSLPckg_InstanceValue, CompleteDSLPckg_Classifier, CompleteDSLPckg_StructuralFeature, CompleteDSLPckg_RedefinableElement, RedefinableElement, Type, CompleteDSLPckg_Feature, CompleteDSLPckg_Property, CompleteDSLPckg_Generalization, CompleteDSLPckg_Substitution, CompleteDSLPckg_GeneralizationSet, CompleteDSLPckg_CollaborationUse, Feature, MultiplicityElement, StructuralFeature, ConnectableElement, DeploymentTarget, CompleteDSLPckg_Class, CompleteDSLPckg_Association, CompleteDSLPckg_DataType, CompleteDSLPckg_Interface, CompleteDSLPckg_BehavioralFeature, CompleteDSLPckg_Operation, BehavioralFeature, Classifier, BehavioredClassifier, StructuredClassifier, EncapsulatedClassifier, CompleteDSLPckg_Reception, CompleteDSLPckg_PrimitiveType, DataType, CompleteDSLPckg_Enumeration, CompleteDSLPckg_EnumerationLiteral, InstanceSpecification, CompleteDSLPckg_Usage, Dependency, CompleteDSLPckg_Abstraction, CompleteDSLPckg_Realization, Abstraction, Realization, CompleteDSLPckg_InterfaceRealization, CompleteDSLPckg_BehavioredClassifier, CompleteDSLPckg_AssociationClass, Class_, Association, CompleteDSLPckg_Event, CompleteDSLPckg_OpaqueBehavior, Behavior, CompleteDSLPckg_FunctionBehavior, OpaqueBehavior, CompleteDSLPckg_Signal, CompleteDSLPckg_Trigger, CompleteDSLPckg_Interval, CompleteDSLPckg_MessageEvent, Event, CompleteDSLPckg_AnyReceiveEvent, MessageEvent, CompleteDSLPckg_SignalEvent, CompleteDSLPckg_CallEvent, CompleteDSLPckg_ChangeEvent, CompleteDSLPckg_TimeEvent, CompleteDSLPckg_TimeExpression, CompleteDSLPckg_Observation, CompleteDSLPckg_TimeObservation, Observation, CompleteDSLPckg_DurationObservation, CompleteDSLPckg_Duration, CompleteDSLPckg_TimeInterval, Interval, CompleteDSLPckg_DurationInterval, CompleteDSLPckg_IntervalConstraint, Constraint, CompleteDSLPckg_TimeConstraint, IntervalConstraint, CompleteDSLPckg_DurationConstraint, CompleteDSLPckg_Component, CompleteDSLPckg_ComponentRealization, CompleteDSLPckg_Port, Property_, CompleteDSLPckg_Connector, CompleteDSLPckg_ConnectorEnd, CompleteDSLPckg_ConnectableElement, CompleteDSLPckg_StructuredClassifier, CompleteDSLPckg_Manifestation, CompleteDSLPckg_EncapsulatedClassifier, CompleteDSLPckg_Collaboration, CompleteDSLPckg_InvocationAction, CompleteDSLPckg_Variable, CompleteDSLPckg_Artifact, DeployedArtifact, CompleteDSLPckg_OutputPin, CompleteDSLPckg_Node, CompleteDSLPckg_Device, Node, CompleteDSLPckg_ExecutionEnvironment, CompleteDSLPckg_CommunicationPath, CompleteDSLPckg_DeploymentTarget, CompleteDSLPckg_Deployment, CompleteDSLPckg_DeployedArtifact, CompleteDSLPckg_DeploymentSpecification, Artifact, CompleteDSLPckg_Action, CompleteDSLPckg_InputPin, CompleteDSLPckg_SendObjectAction, CompleteDSLPckg_OpaqueAction, Action, Pin, CompleteDSLPckg_Pin, CompleteDSLPckg_ValuePin, InputPin, CompleteDSLPckg_CallAction, InvocationAction, CompleteDSLPckg_CallBehaviorAction, CallAction, CompleteDSLPckg_CallOperationAction, CompleteDSLPckg_SendSignalAction, CompleteDSLPckg_BroadcastSignalAction, CompleteDSLPckg_ReadStructuralFeatureAction, StructuralFeatureAction, CompleteDSLPckg_CreateObjectAction, CompleteDSLPckg_DestroyObjectAction, CompleteDSLPckg_TestIdentityAction, CompleteDSLPckg_ReadSelfAction, CompleteDSLPckg_ValueSpecificationAction, CompleteDSLPckg_StructuralFeatureAction, CompleteDSLPckg_CreateLinkAction, WriteLinkAction, CompleteDSLPckg_LinkEndCreationData, LinkEndData, CompleteDSLPckg_WriteStructuralFeatureAction, CompleteDSLPckg_AddStructuralFeatureValueAction, WriteStructuralFeatureAction, CompleteDSLPckg_RemoveStructuralFeatureValueAction, CompleteDSLPckg_ClearStructuralFeatureAction, CompleteDSLPckg_LinkAction, CompleteDSLPckg_LinkEndData, CompleteDSLPckg_QualifierValue, CompleteDSLPckg_ReadLinkAction, LinkAction, CompleteDSLPckg_WriteLinkAction, AcceptEventAction, CompleteDSLPckg_DestroyLinkAction, CompleteDSLPckg_LinkEndDestructionData, CompleteDSLPckg_ReplyAction, CompleteDSLPckg_UnmarshallAction, CompleteDSLPckg_AcceptEventAction, CompleteDSLPckg_AcceptCallAction, CompleteDSLPckg_ReadExtendAction, CompleteDSLPckg_ReclassifyObjectAction, CompleteDSLPckg_ReadlsClassifiedObjectAction, CompleteDSLPckg_StartClassifierBehaviorAction, CompleteDSLPckg_StartObjectBehaviorAction, CompleteDSLPckg_ReadLinkObjectEndAction, CompleteDSLPckg_ReadLinkObjectEndQualifierAction, CompleteDSLPckg_CreateLinkObjectAction, CreateLinkAction, CompleteDSLPckg_VariableAction, CompleteDSLPckg_ReduceAction, CompleteDSLPckg_StateMachine, CompleteDSLPckg_Region, CompleteDSLPckg_Pseudostate, CompleteDSLPckg_ReadVariableAction, VariableAction, CompleteDSLPckg_WriteVariableAction, CompleteDSLPckg_AddVariableValueAction, WriteVariableAction, CompleteDSLPckg_RemoveVariableValueAction, CompleteDSLPckg_ClearVariableAction, CompleteDSLPckg_RaiseExceptionAction, CompleteDSLPckg_ActionInputPin, CompleteDSLPckg_State, CompleteDSLPckg_Vertex, CompleteDSLPckg_Transition, Vertex, CompleteDSLPckg_ConnectionPointReference, CompleteDSLPckg_FinalState, State, CompleteDSLPckg_ProtocolStateMachine, StateMachine, CompleteDSLPckg_ProtocolConformance, CompleteDSLPckg_InterruptibleActivityRegion, CompleteDSLPckg_ProtocolTransition, Transition, CompleteDSLPckg_Activity, CompleteDSLPckg_ActivityNode, CompleteDSLPckg_ActivityGroup, CompleteDSLPckg_ActivityEdge, CompleteDSLPckg_ActivityPartition, CompleteDSLPckg_StructuredActivityNode, CompleteDSLPckg_ObjectNode, ActivityNode, CompleteDSLPckg_ActivityParameterNode, ObjectNode, CompleteDSLPckg_ControlNode, CompleteDSLPckg_ActivityFinalNode, ControlNode, FinalNode, CompleteDSLPckg_InitialNode, ActivityGroup, CompleteDSLPckg_ControlFlow, ActivityEdge, CompleteDSLPckg_ObjectFlow, CompleteDSLPckg_CentralBufferNode, CompleteDSLPckg_FinalNode, CompleteDSLPckg_FlowFinalNode, CompleteDSLPckg_ForkNode, CompleteDSLPckg_JoinNode, CompleteDSLPckg_MergeNode, CompleteDSLPckg_DecisionNode, CompleteDSLPckg_ExecutableNode, CompleteDSLPckg_ExceptionHandler, CompleteDSLPckg_LoopNode, StructuredActivityNode, CompleteDSLPckg_DataStoreNode, CentralBufferNode, CompleteDSLPckg_ParameterSet, ExecutableNode, CompleteDSLPckg_SequenceNode, CompleteDSLPckg_ConditionalNode, CompleteDSLPckg_Clause, CompleteDSLPckg_ExpansionRegion, CompleteDSLPckg_ExpansionNode, CompleteDSLPckg_Gate, CompleteDSLPckg_InteractionFragment, CompleteDSLPckg_Lifeline, CompleteDSLPckg_GeneralOrdering, CompleteDSLPckg_InteractionOperand, CompleteDSLPckg_ExecutionSpecification, InteractionFragment, CompleteDSLPckg_OccurenceSpecification, CompleteDSLPckg_StateInvariant, CompleteDSLPckg_Interaction, CompleteDSLPckg_ExecutionOccurrenceSpecification, OccurenceSpecification, CompleteDSLPckg_MessageOccurrenceSpecification, CompleteDSLPckg_DestructionOccurrenceSpecification, MessageOccurrenceSpecification, CompleteDSLPckg_BehaviorExecutionSpecification, ExecutionSpecification, CompleteDSLPckg_PartDecomposition, CompleteDSLPckg_Message, CompleteDSLPckg_MessageEnd, CompleteDSLPckg_Continuation, CompleteDSLPckg_ActionExecutionSpecification, CompleteDSLPckg_InteractionConstraint, CompleteDSLPckg_CombinedFragment, CompleteDSLPckg_ConsiderIgnoreFragment, CombinedFragment, MessageEnd, CompleteDSLPckg_InteractionUse, InteractionUse, CompleteDSLPckg_Actor, CompleteDSLPckg_UseCase, CompleteDSLPckg_ExtensionPoint, CompleteDSLPckg_Extend, CompleteDSLPckg_Include, VisibilityKind, AggregationKind, CallConcurrencyFeature, ConnectorKind, TransitionKind, ObjectNodeOrderingKind, ParameterEffectKind, ExpansionKind, MessageKind, MessageSort, InteractionOperandKind},
    associations={ownedComment0, ownedElement2, owner4, namespace6, clientDependency7, nestingPackage26, importedMember8, member9, ownedMember11, elementImport12, packageImport13, ownedRule15, importedElement16, importingNamespace18, importedPackage20, importingNamespace21, nestedPackage24, owningUpper46, owningLower47, packagedElement28, ownedType31, packageMerge32, owningElement33, annotatedElement35, relatedElement36, target38, source40, upperValue43, lowerValue44, specification64, owningConstraint49, owningSlot51, owningInstanceSpec52, type54, package55, operand57, result58, behavior59, instance61, slot62, redefinedClassifier91, classifier66, context68, constrainedElement70, specification72, owningInstace74, value76, definingFeature78, redefinedElement80, redefinitionContext81, inheritedMember84, feature87, attribute88, general94, generalization96, substitution97, powertypeExtent98, collaborationUse99, representation101, featuringClassifier104, ownedParameter137, class_105, redefinedProperty107, defaultValue109, opposite113, subsettedProperty116, association118, owningAssociation119, dataType121, interface123, qualifier126, associationEnd128, general130, specific132, generalizationSet134, dataType161, raisedException139, ownedFormalParam142, defaultValue145, type148, precondition150, bodyCondition153, postcondition156, class_159, navigableOwnedEnd178, interface164, nestedClassifier167, ownedOperation169, superClass171, ownedAttribute173, ownedReception176, mapping199, memberEnd180, ownedEnd182, ownedAttribute184, ownedOperation186, ownedLiteral189, enumeration190, receivingPackage191, mergedPackage193, client195, supplier197, substitutingClassifier201, contract203, nestedClassifier205, redefinedInterface208, ownedAttribute210, ownedOperation212, ownedReception215, implementingClassifier218, contract219, interfaceRealization221, ownedBehavior222, classifierBehavior224, event254, powertype227, generalization229, context231, redefinedBehavior235, specification237, ownedParameter240, precondition243, postcondition246, ownedAttribute249, signal251, observation273, signal255, operation257, changeExpression259, when261, expr262, observation265, event267, event269, expr271, max276, min278, timeMax281, timeMin283, durationMax286, durationMin288, timeSpecification291, durationSpecification293, required295, provided297, realization300, packagedElement302, abstraction305, realizingClassifier308, end311, contract312, redefinedConnector316, partWithPort318, role321, type323, definingEnd326, end329, ownedConnector332, role334, structuredOwnedAttribute337, part340, manifestation371, required343, provided345, redefinedPort349, ownedPort351, collaborationRole353, type355, roleBinding358, onPort361, ownedOperation363, ownedAttribute365, nestedArtifact369, input394, output396, utilizedElement373, nestedNode377, deployedElement378, deployment380, location382, deployedArtifact385, configuration387, deployment389, context392, signal419, inputValue398, outputValue400, value403, result405, behavior407, operation409, target411, target414, signal416, object450, target421, request423, classifier426, result428, target431, result433, first435, second438, result441, result443, value445, structuralFeature448, result453, value455, result457, insertAt460, removeAt462, result464, inputValue466, endData468, value470, end473, qualifier476, result478, returnInformation505, insertAt480, destroyAt482, returnInformation484, replyValue486, replyToCall489, object492, unmarshallType494, result497, result500, trigger502, qualifier529, result507, classifier509, object512, oldClassifier514, newClassifier517, result520, object522, object525, object527, result551, value532, end535, object537, result540, object543, result545, qualifier548, reducer558, variable561, result553, collection555, fromAction572, region574, connectionPoint575, result562, value564, insertAt566, removeAt568, exception570, incoming598, container601, source604, submachineState577, extendedStateMachine580, subvertex582, stateMachine584, transition587, state589, extendedRegion593, outgoing595, state625, exit628, entry630, target607, effect610, trigger613, guard616, container619, redefinedTransition623, conformance666, specificMachine667, generalMachine670, state633, connection636, connectionPoint639, submachine642, region645, deferrableTrigger648, exit651, doActivity654, entry657, stateInvariant660, redefinedState664, incoming699, outgoing702, inPartition705, inInterruptibleRegion708, preCondition673, postCondition675, referred678, node681, group682, edge684, partition686, structuredNode688, variable690, inGroup693, redefinedNode697, guard742, inPartition745, weight748, interrupts751, inStructuredNode754, inStructuredNode710, subgroup714, superGroup717, inActivity719, containedNode722, containedEdge725, parameter728, target730, source733, redefinedEdge737, inGroup739, edge772, subpartition776, superPartition779, represents781, node784, transformation757, selection759, inState762, joinSpec765, decisionInputFlow767, decisionInput769, edge810, structuredNodeOutput813, handler816, parameter787, condition789, interruptingEdge792, node795, activity798, variable801, node804, structuredNodeInput807, predecessorClause851, sucessorClause854, decider856, executableNode859, setupPart817, bodyPart819, test822, decider825, loopVariableInput828, loopVariable831, bodyOutput834, result837, clause840, test841, body844, result847, inputElement872, outputElement873, handlerBody861, protectedNode864, exceptionInput867, exceptionType869, fragment899, lifeline901, action904, formalGate907, coveredBy909, regionAsInput876, regionAsOutput879, covered882, generalOrdering883, enclosingOperand885, start887, finish888, toBefore891, toAfter894, invariant897, message936, execution939, interaction912, represents915, selector918, decomposedAs921, argument923, connector925, signature928, sendEvent931, receiveEvent933, message961, maxint963, minint966, behavior941, action943, after945, before948, fragment951, guard954, operand956, cfragmentGate958, extensionLocation994, extension997, condition1000, extendedCase1003, actualGate969, argument971, returnValue974, returnValueRecipient977, refersTo980, subject983, extensionPoint985, extend987, include989, useCase991, includingCase1006, addition1009},
    generalizations={gen_CompleteDSLPckg_Namespace_NamedElement, gen_CompleteDSLPckg_NamedElement_Element, gen_CompleteDSLPckg_PackageableElement_NamedElement, gen_CompleteDSLPckg_ElementImport_DirectedRelationship, gen_CompleteDSLPckg_PackageImport_DirectedRelationship, gen_CompleteDSLPckg_Package_Namespace, gen_CompleteDSLPckg_Package_PackageableElement, gen_CompleteDSLPckg_Comment_Element, gen_CompleteDSLPckg_Relationship_Element, gen_CompleteDSLPckg_DirectedRelationship_Relationship, gen_CompleteDSLPckg_MultiplicityElement_Element, gen_CompleteDSLPckg_ValueSpecification_TypedElement, gen_CompleteDSLPckg_ValueSpecification_PackageableElement, gen_CompleteDSLPckg_TypedElement_NamedElement, gen_CompleteDSLPckg_Type_PackageableElement, gen_CompleteDSLPckg_Expression_ValueSpecification, gen_CompleteDSLPckg_OpaqueExpression_ValueSpecification, gen_CompleteDSLPckg_LiteralSpecification_ValueSpecification, gen_CompleteDSLPckg_LiteralNull_LiteralSpecification, gen_CompleteDSLPckg_LiteralBoolean_LiteralSpecification, gen_CompleteDSLPckg_LiteralInteger_LiteralSpecification, gen_CompleteDSLPckg_LiteralReal_LiteralSpecification, gen_CompleteDSLPckg_LiteralString_LiteralSpecification, gen_CompleteDSLPckg_LiteralUnilimitedNatural_LiteralSpecification, gen_CompleteDSLPckg_InstanceSpecification_PackageableElement, gen_CompleteDSLPckg_Constraint_PackageableElement, gen_CompleteDSLPckg_Slot_Element, gen_CompleteDSLPckg_RedefinableElement_NamedElement, gen_CompleteDSLPckg_Classifier_RedefinableElement, gen_CompleteDSLPckg_Classifier_Namespace, gen_CompleteDSLPckg_Classifier_Type, gen_CompleteDSLPckg_Feature_RedefinableElement, gen_CompleteDSLPckg_StructuralFeature_Feature, gen_CompleteDSLPckg_StructuralFeature_MultiplicityElement, gen_CompleteDSLPckg_StructuralFeature_TypedElement, gen_CompleteDSLPckg_Property_StructuralFeature, gen_CompleteDSLPckg_Property_ConnectableElement, gen_CompleteDSLPckg_Property_DeploymentTarget, gen_CompleteDSLPckg_Generalization_DirectedRelationship, gen_CompleteDSLPckg_BehavioralFeature_Feature, gen_CompleteDSLPckg_BehavioralFeature_Namespace, gen_CompleteDSLPckg_Parameter_TypedElement, gen_CompleteDSLPckg_Operation_BehavioralFeature, gen_CompleteDSLPckg_Class_Classifier, gen_CompleteDSLPckg_Class_BehavioredClassifier, gen_CompleteDSLPckg_Class_StructuredClassifier, gen_CompleteDSLPckg_Class_EncapsulatedClassifier, gen_CompleteDSLPckg_Association_Relationship, gen_CompleteDSLPckg_Association_Classifier, gen_CompleteDSLPckg_DataType_Classifier, gen_CompleteDSLPckg_PrimitiveType_DataType, gen_CompleteDSLPckg_Enumeration_DataType, gen_CompleteDSLPckg_EnumerationLiteral_InstanceSpecification, gen_CompleteDSLPckg_PackageMerge_DirectedRelationship, gen_CompleteDSLPckg_Dependency_PackageableElement, gen_CompleteDSLPckg_Dependency_DirectedRelationship, gen_CompleteDSLPckg_Usage_Dependency, gen_CompleteDSLPckg_Abstraction_Dependency, gen_CompleteDSLPckg_Realization_Abstraction, gen_CompleteDSLPckg_Substitution_Realization, gen_CompleteDSLPckg_Interface_Classifier, gen_CompleteDSLPckg_InterfaceRealization_Realization, gen_CompleteDSLPckg_BehavioredClassifier_Classifier, gen_CompleteDSLPckg_AssociationClass_Class, gen_CompleteDSLPckg_AssociationClass_Association, gen_CompleteDSLPckg_GeneralizationSet_PackageableElement, gen_CompleteDSLPckg_Event_PackageableElement, gen_CompleteDSLPckg_Behavior_Class, gen_CompleteDSLPckg_OpaqueBehavior_Behavior, gen_CompleteDSLPckg_FunctionBehavior_OpaqueBehavior, gen_CompleteDSLPckg_Signal_Classifier, gen_CompleteDSLPckg_Reception_BehavioralFeature, gen_CompleteDSLPckg_Trigger_NamedElement, gen_CompleteDSLPckg_Interval_ValueSpecification, gen_CompleteDSLPckg_MessageEvent_Event, gen_CompleteDSLPckg_AnyReceiveEvent_MessageEvent, gen_CompleteDSLPckg_SignalEvent_MessageEvent, gen_CompleteDSLPckg_CallEvent_MessageEvent, gen_CompleteDSLPckg_ChangeEvent_Event, gen_CompleteDSLPckg_TimeExpression_ValueSpecification, gen_CompleteDSLPckg_Observation_PackageableElement, gen_CompleteDSLPckg_TimeObservation_Observation, gen_CompleteDSLPckg_DurationObservation_Observation, gen_CompleteDSLPckg_Duration_ValueSpecification, gen_CompleteDSLPckg_ComponentRealization_Realization, gen_CompleteDSLPckg_TimeInterval_Interval, gen_CompleteDSLPckg_DurationInterval_Interval, gen_CompleteDSLPckg_IntervalConstraint_Constraint, gen_CompleteDSLPckg_TimeConstraint_IntervalConstraint, gen_CompleteDSLPckg_DurationConstraint_IntervalConstraint, gen_CompleteDSLPckg_Component_Class, gen_CompleteDSLPckg_Component_NamedElement, gen_CompleteDSLPckg_Port_Property, gen_CompleteDSLPckg_Connector_Feature, gen_CompleteDSLPckg_ConnectableElement_TypedElement, gen_CompleteDSLPckg_StructuredClassifier_Classifier, gen_CompleteDSLPckg_EncapsulatedClassifier_StructuredClassifier, gen_CompleteDSLPckg_Collaboration_StructuredClassifier, gen_CompleteDSLPckg_Collaboration_BehavioredClassifier, gen_CompleteDSLPckg_CollaborationUse_NamedElement, gen_CompleteDSLPckg_Variable_ConnectableElement, gen_CompleteDSLPckg_Variable_MultiplicityElement, gen_CompleteDSLPckg_Variable_TypedElement, gen_CompleteDSLPckg_Artifact_Classifier, gen_CompleteDSLPckg_Artifact_NamedElement, gen_CompleteDSLPckg_Artifact_DeployedArtifact, gen_CompleteDSLPckg_Manifestation_Abstraction, gen_CompleteDSLPckg_Node_Class, gen_CompleteDSLPckg_Node_DeploymentTarget, gen_CompleteDSLPckg_Device_Node, gen_CompleteDSLPckg_ExecutionEnvironment_Node, gen_CompleteDSLPckg_CommunicationPath_Association, gen_CompleteDSLPckg_DeploymentTarget_NamedElement, gen_CompleteDSLPckg_Deployment_Dependency, gen_CompleteDSLPckg_DeployedArtifact_NamedElement, gen_CompleteDSLPckg_DeploymentSpecification_Artifact, gen_CompleteDSLPckg_Action_NamedElement, gen_CompleteDSLPckg_SendObjectAction_InvocationAction, gen_CompleteDSLPckg_OpaqueAction_Action, gen_CompleteDSLPckg_InputPin_Pin, gen_CompleteDSLPckg_OutputPin_Pin, gen_CompleteDSLPckg_Pin_TypedElement, gen_CompleteDSLPckg_Pin_MultiplicityElement, gen_CompleteDSLPckg_ValuePin_InputPin, gen_CompleteDSLPckg_CallAction_InvocationAction, gen_CompleteDSLPckg_CallBehaviorAction_CallAction, gen_CompleteDSLPckg_SendSignalAction_InvocationAction, gen_CompleteDSLPckg_BroadcastSignalAction_InvocationAction, gen_CompleteDSLPckg_ReadStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_CreateObjectAction_Action, gen_CompleteDSLPckg_DestroyObjectAction_Action, gen_CompleteDSLPckg_TestIdentityAction_Action, gen_CompleteDSLPckg_ReadSelfAction_Action, gen_CompleteDSLPckg_ValueSpecificationAction_Action, gen_CompleteDSLPckg_StructuralFeatureAction_Action, gen_CompleteDSLPckg_CreateLinkAction_WriteLinkAction, gen_CompleteDSLPckg_LinkEndCreationData_LinkEndData, gen_CompleteDSLPckg_WriteStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_CompleteDSLPckg_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_CompleteDSLPckg_ClearStructuralFeatureAction_StructuralFeatureAction, gen_CompleteDSLPckg_LinkAction_Action, gen_CompleteDSLPckg_LinkEndData_Element, gen_CompleteDSLPckg_ReadLinkAction_LinkAction, gen_CompleteDSLPckg_WriteLinkAction_LinkAction, gen_CompleteDSLPckg_AcceptCallAction_AcceptEventAction, gen_CompleteDSLPckg_DestroyLinkAction_WriteLinkAction, gen_CompleteDSLPckg_LinkEndDestructionData_LinkEndData, gen_CompleteDSLPckg_ReplyAction_Action, gen_CompleteDSLPckg_UnmarshallAction_Action, gen_CompleteDSLPckg_AcceptEventAction_Action, gen_CompleteDSLPckg_QualifierValue_Element, gen_CompleteDSLPckg_ReadExtendAction_Action, gen_CompleteDSLPckg_ReclassifyObjectAction_Action, gen_CompleteDSLPckg_StartClassifierBehaviorAction_Action, gen_CompleteDSLPckg_StartObjectBehaviorAction_CallAction, gen_CompleteDSLPckg_ReadLinkObjectEndAction_Action, gen_CompleteDSLPckg_ReadLinkObjectEndQualifierAction_Action, gen_CompleteDSLPckg_CreateLinkObjectAction_CreateLinkAction, gen_CompleteDSLPckg_VariableAction_Action, gen_CompleteDSLPckg_ReduceAction_Action, gen_CompleteDSLPckg_StateMachine_Behavior, gen_CompleteDSLPckg_ReadVariableAction_VariableAction, gen_CompleteDSLPckg_WriteVariableAction_VariableAction, gen_CompleteDSLPckg_AddVariableValueAction_WriteVariableAction, gen_CompleteDSLPckg_RemoveVariableValueAction_WriteVariableAction, gen_CompleteDSLPckg_ClearVariableAction_VariableAction, gen_CompleteDSLPckg_RaiseExceptionAction_Action, gen_CompleteDSLPckg_ActionInputPin_InputPin, gen_CompleteDSLPckg_Transition_Namespace, gen_CompleteDSLPckg_Transition_RedefinableElement, gen_CompleteDSLPckg_Region_Namespace, gen_CompleteDSLPckg_Region_RedefinableElement, gen_CompleteDSLPckg_Vertex_NamedElement, gen_CompleteDSLPckg_Pseudostate_Vertex, gen_CompleteDSLPckg_ConnectionPointReference_Vertex, gen_CompleteDSLPckg_FinalState_State, gen_CompleteDSLPckg_ProtocolStateMachine_StateMachine, gen_CompleteDSLPckg_ProtocolConformance_DirectedRelationship, gen_CompleteDSLPckg_State_Vertex, gen_CompleteDSLPckg_State_RedefinableElement, gen_CompleteDSLPckg_State_Namespace, gen_CompleteDSLPckg_ProtocolTransition_Transition, gen_CompleteDSLPckg_Activity_Behavior, gen_CompleteDSLPckg_ActivityNode_NamedElement, gen_CompleteDSLPckg_ActivityNode_RedefinableElement, gen_CompleteDSLPckg_ActivityGroup_NamedElement, gen_CompleteDSLPckg_ObjectNode_ActivityNode, gen_CompleteDSLPckg_ObjectNode_TypedElement, gen_CompleteDSLPckg_ActivityParameterNode_ObjectNode, gen_CompleteDSLPckg_ControlNode_ActivityNode, gen_CompleteDSLPckg_ActivityFinalNode_ControlNode, gen_CompleteDSLPckg_ActivityFinalNode_FinalNode, gen_CompleteDSLPckg_InitialNode_ControlNode, gen_CompleteDSLPckg_ActivityEdge_RedefinableElement, gen_CompleteDSLPckg_ActivityPartition_ActivityGroup, gen_CompleteDSLPckg_ControlFlow_ActivityEdge, gen_CompleteDSLPckg_ObjectFlow_ActivityEdge, gen_CompleteDSLPckg_CentralBufferNode_ObjectNode, gen_CompleteDSLPckg_FinalNode_ControlNode, gen_CompleteDSLPckg_FlowFinalNode_FinalNode, gen_CompleteDSLPckg_ForkNode_ControlNode, gen_CompleteDSLPckg_JoinNode_ControlNode, gen_CompleteDSLPckg_MergeNode_ControlNode, gen_CompleteDSLPckg_DecisionNode_ControlNode, gen_CompleteDSLPckg_ExecutableNode_ActivityNode, gen_CompleteDSLPckg_LoopNode_StructuredActivityNode, gen_CompleteDSLPckg_DataStoreNode_CentralBufferNode, gen_CompleteDSLPckg_ParameterSet_NamedElement, gen_CompleteDSLPckg_InterruptibleActivityRegion_ActivityGroup, gen_CompleteDSLPckg_StructuredActivityNode_Namespace, gen_CompleteDSLPckg_StructuredActivityNode_ExecutableNode, gen_CompleteDSLPckg_StructuredActivityNode_ActivityGroup, gen_CompleteDSLPckg_StructuredActivityNode_Action, gen_CompleteDSLPckg_Clause_Element, gen_CompleteDSLPckg_SequenceNode_StructuredActivityNode, gen_CompleteDSLPckg_ExceptionHandler_Element, gen_CompleteDSLPckg_ConditionalNode_StructuredActivityNode, gen_CompleteDSLPckg_ExpansionRegion_StructuredActivityNode, gen_CompleteDSLPckg_Lifeline_NamedElement, gen_CompleteDSLPckg_ExpansionNode_ObjectNode, gen_CompleteDSLPckg_InteractionFragment_NamedElement, gen_CompleteDSLPckg_ExecutionSpecification_InteractionFragment, gen_CompleteDSLPckg_OccurenceSpecification_InteractionFragment, gen_CompleteDSLPckg_StateInvariant_InteractionFragment, gen_CompleteDSLPckg_Interaction_Behavior, gen_CompleteDSLPckg_Interaction_InteractionFragment, gen_CompleteDSLPckg_MessageEnd_NamedElement, gen_CompleteDSLPckg_ExecutionOccurrenceSpecification_OccurenceSpecification, gen_CompleteDSLPckg_MessageOccurrenceSpecification_OccurenceSpecification, gen_CompleteDSLPckg_DestructionOccurrenceSpecification_MessageOccurrenceSpecification, gen_CompleteDSLPckg_BehaviorExecutionSpecification_ExecutionSpecification, gen_CompleteDSLPckg_Message_NamedElement, gen_CompleteDSLPckg_Continuation_InteractionFragment, gen_CompleteDSLPckg_InteractionConstraint_Constraint, gen_CompleteDSLPckg_ActionExecutionSpecification_ExecutionSpecification, gen_CompleteDSLPckg_GeneralOrdering_NamedElement, gen_CompleteDSLPckg_InteractionOperand_Namespace, gen_CompleteDSLPckg_ConsiderIgnoreFragment_CombinedFragment, gen_CompleteDSLPckg_Include_DirectedRelationship, gen_CompleteDSLPckg_Include_NamedElement, gen_CompleteDSLPckg_Gate_MessageEnd, gen_CompleteDSLPckg_InteractionUse_InteractionFragment, gen_CompleteDSLPckg_PartDecomposition_InteractionUse, gen_CompleteDSLPckg_Actor_BehavioredClassifier, gen_CompleteDSLPckg_UseCase_BehavioredClassifier, gen_CompleteDSLPckg_ExtensionPoint_RedefinableElement, gen_CompleteDSLPckg_Extend_NamedElement, gen_CompleteDSLPckg_Extend_DirectedRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)