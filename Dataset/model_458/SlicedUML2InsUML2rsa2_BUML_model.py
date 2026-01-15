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
UML2_AcceptCallAction = Class(name="UML2::AcceptCallAction")
AcceptEventAction = Class(name="AcceptEventAction")
UML2_ReadStructuralFeatureAction = Class(name="UML2::ReadStructuralFeatureAction")
StructuralFeatureAction = Class(name="StructuralFeatureAction")
UML2_DataType = Class(name="UML2::DataType")
Classifier = Class(name="Classifier")
UML2_StructuredActivityNode = Class(name="UML2::StructuredActivityNode")
Action = Class(name="Action")
UML2_TimeObservationAction = Class(name="UML2::TimeObservationAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
UML2_ReadSelfAction = Class(name="UML2::ReadSelfAction")
UML2_OutputPin = Class(name="UML2::OutputPin")
UML2_DataStoreNode = Class(name="UML2::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2_ReadIsClassifiedObjectAction = Class(name="UML2::ReadIsClassifiedObjectAction")
UML2_Interval = Class(name="UML2::Interval")
ValueSpecification = Class(name="ValueSpecification")
UML2_InputPin = Class(name="UML2::InputPin")
Pin = Class(name="Pin")
UML2_ReadLinkObjectEndQualifierAction = Class(name="UML2::ReadLinkObjectEndQualifierAction")
UML2_EncapsulatedClassifier = Class(name="UML2::EncapsulatedClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
UML2_CreateObjectAction = Class(name="UML2::CreateObjectAction")
UML2_DurationObservationAction = Class(name="UML2::DurationObservationAction")
UML2_BroadcastSignalAction = Class(name="UML2::BroadcastSignalAction")
InvocationAction = Class(name="InvocationAction")
UML2_SendSignalAction = Class(name="UML2::SendSignalAction")
UML2_ActivityParameterNode = Class(name="UML2::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
UML2_ReadVariableAction = Class(name="UML2::ReadVariableAction")
VariableAction = Class(name="VariableAction")
UML2_Port = Class(name="UML2::Port")
Property_ = Class(name="Property")
UML2_Extension = Class(name="UML2::Extension")
Association = Class(name="Association")
UML2_LiteralSpecification = Class(name="UML2::LiteralSpecification")
UML2_ReadLinkAction = Class(name="UML2::ReadLinkAction")
LinkAction = Class(name="LinkAction")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
Class_ = Class(name="Class")
UML2_StateMachine = Class(name="UML2::StateMachine")
Behavior = Class(name="Behavior")
UML2_Device = Class(name="UML2::Device")
Node = Class(name="Node")
UML2_DestroyObjectAction = Class(name="UML2::DestroyObjectAction")
UML2_CallOperationAction = Class(name="UML2::CallOperationAction")
CallAction = Class(name="CallAction")
UML2_StartOwnedBehaviorAction = Class(name="UML2::StartOwnedBehaviorAction")
UML2_StructuralFeature = Class(name="UML2::StructuralFeature")
UML2_AddStructuralFeatureValueAction = Class(name="UML2::AddStructuralFeatureValueAction")
UML2_Operation = Class(name="UML2::Operation")
UML2_VariableAction = Class(name="UML2::VariableAction")
UML2_Enumeration = Class(name="UML2::Enumeration")
UML2_CreateLinkAction = Class(name="UML2::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
UML2_Activity = Class(name="UML2::Activity")
UML2_CallAction = Class(name="UML2::CallAction")
UML2_StructuralFeatureAction = Class(name="UML2::StructuralFeatureAction")
UML2_RemoveStructuralFeatureValueAction = Class(name="UML2::RemoveStructuralFeatureValueAction")
UML2_ValueSpecification = Class(name="UML2::ValueSpecification")
UML2_LinkAction = Class(name="UML2::LinkAction")
UML2_LiteralNull = Class(name="UML2::LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
UML2_Pin = Class(name="UML2::Pin")
UML2_Class = Class(name="UML2::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2_DestroyLinkAction = Class(name="UML2::DestroyLinkAction")
UML2_AcceptEventAction = Class(name="UML2::AcceptEventAction")
UML2_RaiseExceptionAction = Class(name="UML2::RaiseExceptionAction")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_RemoveVariableValueAction = Class(name="UML2::RemoveVariableValueAction")
WriteVariableAction = Class(name="WriteVariableAction")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_TemplateableClassifier = Class(name="UML2::TemplateableClassifier")
UML2_AddVariableValueAction = Class(name="UML2::AddVariableValueAction")
UML2_ReadLinkObjectEndAction = Class(name="UML2::ReadLinkObjectEndAction")
UML2_Classifier = Class(name="UML2::Classifier")
Type = Class(name="Type")
UML2_ReadExtentAction = Class(name="UML2::ReadExtentAction")
UML2_ClearAssociationAction = Class(name="UML2::ClearAssociationAction")
UML2_ApplyFunctionAction = Class(name="UML2::ApplyFunctionAction")
UML2_ConditionalNode = Class(name="UML2::ConditionalNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
UML2_LiteralString = Class(name="UML2::LiteralString")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier")
UML2_Signal = Class(name="UML2::Signal")
UML2_TimeInterval = Class(name="UML2::TimeInterval")
Interval = Class(name="Interval")
UML2_ReclassifyObjectAction = Class(name="UML2::ReclassifyObjectAction")
UML2_Component = Class(name="UML2::Component")
UML2_Interface = Class(name="UML2::Interface")
TypedElement = Class(name="TypedElement")
UML2_Variable = Class(name="UML2::Variable")
UML2_PrimitiveType = Class(name="UML2::PrimitiveType")
DataType = Class(name="DataType")
UML2_Actor = Class(name="UML2::Actor")
UML2_Artifact = Class(name="UML2::Artifact")
UML2_ClearStructuralFeatureAction = Class(name="UML2::ClearStructuralFeatureAction")
UML2_LoopNode = Class(name="UML2::LoopNode")
UML2_Parameter = Class(name="UML2::Parameter")
UML2_Property = Class(name="UML2::Property")
StructuralFeature = Class(name="StructuralFeature")
UML2_Duration = Class(name="UML2::Duration")
UML2_CallBehaviorAction = Class(name="UML2::CallBehaviorAction")
UML2_ParameterableClassifier = Class(name="UML2::ParameterableClassifier")
UML2_DurationInterval = Class(name="UML2::DurationInterval")
UML2_OpaqueExpression = Class(name="UML2::OpaqueExpression")
UML2_WriteVariableAction = Class(name="UML2::WriteVariableAction")
UML2_InvocationAction = Class(name="UML2::InvocationAction")
UML2_ObjectNode = Class(name="UML2::ObjectNode")
UML2_TypedElement = Class(name="UML2::TypedElement")
UML2_Type = Class(name="UML2::Type")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
UML2_WriteStructuralFeatureAction = Class(name="UML2::WriteStructuralFeatureAction")
UML2_LiteralInteger = Class(name="UML2::LiteralInteger")
UML2_Association = Class(name="UML2::Association")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_TestIdentityAction = Class(name="UML2::TestIdentityAction")
UML2_CreateLinkObjectAction = Class(name="UML2::CreateLinkObjectAction")
CreateLinkAction = Class(name="CreateLinkAction")
UML2_ClearVariableAction = Class(name="UML2::ClearVariableAction")
UML2_InformationItem = Class(name="UML2::InformationItem")
UML2_LiteralUnlimitedNatural = Class(name="UML2::LiteralUnlimitedNatural")
UML2_WriteLinkAction = Class(name="UML2::WriteLinkAction")
UML2_Interaction = Class(name="UML2::Interaction")
UML2_ExpansionNode = Class(name="UML2::ExpansionNode")
UML2_ValuePin = Class(name="UML2::ValuePin")
InputPin = Class(name="InputPin")
UML2_Expression = Class(name="UML2::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2_ReplyAction = Class(name="UML2::ReplyAction")
UML2_LiteralBoolean = Class(name="UML2::LiteralBoolean")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
UML2_Node = Class(name="UML2::Node")
UML2_CentralBufferNode = Class(name="UML2::CentralBufferNode")
UML2_DeploymentSpecification = Class(name="UML2::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2_InstanceValue = Class(name="UML2::InstanceValue")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_ExpansionRegion = Class(name="UML2::ExpansionRegion")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
UML2_Collaboration = Class(name="UML2::Collaboration")
UML2_StructuredClassifier = Class(name="UML2::StructuredClassifier")
UML2_TimeExpression = Class(name="UML2::TimeExpression")
UML2_SendObjectAction = Class(name="UML2::SendObjectAction")
UML2_Action = Class(name="UML2::Action")

# UML2_AcceptCallAction class attributes and methods

# AcceptEventAction class attributes and methods

# UML2_ReadStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# UML2_DataType class attributes and methods

# Classifier class attributes and methods

# UML2_StructuredActivityNode class attributes and methods

# Action class attributes and methods

# UML2_TimeObservationAction class attributes and methods

# WriteStructuralFeatureAction class attributes and methods

# UML2_ReadSelfAction class attributes and methods

# UML2_OutputPin class attributes and methods

# UML2_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2_ReadIsClassifiedObjectAction class attributes and methods

# UML2_Interval class attributes and methods

# ValueSpecification class attributes and methods

# UML2_InputPin class attributes and methods

# Pin class attributes and methods

# UML2_ReadLinkObjectEndQualifierAction class attributes and methods

# UML2_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# UML2_CreateObjectAction class attributes and methods

# UML2_DurationObservationAction class attributes and methods

# UML2_BroadcastSignalAction class attributes and methods

# InvocationAction class attributes and methods

# UML2_SendSignalAction class attributes and methods

# UML2_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# UML2_ReadVariableAction class attributes and methods

# VariableAction class attributes and methods

# UML2_Port class attributes and methods

# Property class attributes and methods

# UML2_Extension class attributes and methods

# Association class attributes and methods

# UML2_LiteralSpecification class attributes and methods

# UML2_ReadLinkAction class attributes and methods

# LinkAction class attributes and methods

# UML2_AssociationClass class attributes and methods

# Class class attributes and methods

# UML2_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2_Device class attributes and methods

# Node class attributes and methods

# UML2_DestroyObjectAction class attributes and methods

# UML2_CallOperationAction class attributes and methods

# CallAction class attributes and methods

# UML2_StartOwnedBehaviorAction class attributes and methods

# UML2_StructuralFeature class attributes and methods

# UML2_AddStructuralFeatureValueAction class attributes and methods

# UML2_Operation class attributes and methods

# UML2_VariableAction class attributes and methods

# UML2_Enumeration class attributes and methods

# UML2_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# UML2_Activity class attributes and methods

# UML2_CallAction class attributes and methods

# UML2_StructuralFeatureAction class attributes and methods

# UML2_RemoveStructuralFeatureValueAction class attributes and methods

# UML2_ValueSpecification class attributes and methods

# UML2_LinkAction class attributes and methods

# UML2_LiteralNull class attributes and methods

# LiteralSpecification class attributes and methods

# UML2_Pin class attributes and methods

# UML2_Class class attributes and methods

# BehavioredClassifier class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2_DestroyLinkAction class attributes and methods

# UML2_AcceptEventAction class attributes and methods

# UML2_RaiseExceptionAction class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_RemoveVariableValueAction class attributes and methods

# WriteVariableAction class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_TemplateableClassifier class attributes and methods

# UML2_AddVariableValueAction class attributes and methods

# UML2_ReadLinkObjectEndAction class attributes and methods

# UML2_Classifier class attributes and methods

# Type class attributes and methods

# UML2_ReadExtentAction class attributes and methods

# UML2_ClearAssociationAction class attributes and methods

# UML2_ApplyFunctionAction class attributes and methods

# UML2_ConditionalNode class attributes and methods

# StructuredActivityNode class attributes and methods

# UML2_LiteralString class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# UML2_Signal class attributes and methods

# UML2_TimeInterval class attributes and methods

# Interval class attributes and methods

# UML2_ReclassifyObjectAction class attributes and methods

# UML2_Component class attributes and methods

# UML2_Interface class attributes and methods

# TypedElement class attributes and methods

# UML2_Variable class attributes and methods

# UML2_PrimitiveType class attributes and methods

# DataType class attributes and methods

# UML2_Actor class attributes and methods

# UML2_Artifact class attributes and methods

# UML2_ClearStructuralFeatureAction class attributes and methods

# UML2_LoopNode class attributes and methods

# UML2_Parameter class attributes and methods

# UML2_Property class attributes and methods

# StructuralFeature class attributes and methods

# UML2_Duration class attributes and methods

# UML2_CallBehaviorAction class attributes and methods

# UML2_ParameterableClassifier class attributes and methods

# UML2_DurationInterval class attributes and methods

# UML2_OpaqueExpression class attributes and methods

# UML2_WriteVariableAction class attributes and methods

# UML2_InvocationAction class attributes and methods

# UML2_ObjectNode class attributes and methods

# UML2_TypedElement class attributes and methods

# UML2_Type class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# UML2_WriteStructuralFeatureAction class attributes and methods

# UML2_LiteralInteger class attributes and methods

# UML2_Association class attributes and methods

# UML2_UseCase class attributes and methods

# UML2_TestIdentityAction class attributes and methods

# UML2_CreateLinkObjectAction class attributes and methods

# CreateLinkAction class attributes and methods

# UML2_ClearVariableAction class attributes and methods

# UML2_InformationItem class attributes and methods

# UML2_LiteralUnlimitedNatural class attributes and methods

# UML2_WriteLinkAction class attributes and methods

# UML2_Interaction class attributes and methods

# UML2_ExpansionNode class attributes and methods

# UML2_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2_Expression class attributes and methods

# OpaqueExpression class attributes and methods

# UML2_ReplyAction class attributes and methods

# UML2_LiteralBoolean class attributes and methods

# UML2_CommunicationPath class attributes and methods

# UML2_Node class attributes and methods

# UML2_CentralBufferNode class attributes and methods

# UML2_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2_InstanceValue class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_ExpansionRegion class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# UML2_Collaboration class attributes and methods

# UML2_StructuredClassifier class attributes and methods

# UML2_TimeExpression class attributes and methods

# UML2_SendObjectAction class attributes and methods

# UML2_Action class attributes and methods

# Relationships
result0: BinaryAssociation = BinaryAssociation(
    name="result0",
    ends={
        Property(name="UML2_OutputPin", type=UML2_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_ReadSelfAction", type=UML2_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="UML2_Type", type=UML2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TypedElement", type=UML2_Type, multiplicity=Multiplicity(0, 1))
    }
)
context_2: BinaryAssociation = BinaryAssociation(
    name="context_2",
    ends={
        Property(name="UML2_Classifier", type=UML2_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Action", type=UML2_Classifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML2_AcceptCallAction_AcceptEventAction = Generalization(general=AcceptEventAction, specific=UML2_AcceptCallAction)
gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ReadStructuralFeatureAction)
gen_UML2_DataType_Classifier = Generalization(general=Classifier, specific=UML2_DataType)
gen_UML2_StructuredActivityNode_Action = Generalization(general=Action, specific=UML2_StructuredActivityNode)
gen_UML2_TimeObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_TimeObservationAction)
gen_UML2_ReadSelfAction_Action = Generalization(general=Action, specific=UML2_ReadSelfAction)
gen_UML2_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2_DataStoreNode)
gen_UML2_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=UML2_ReadIsClassifiedObjectAction)
gen_UML2_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Interval)
gen_UML2_InputPin_Pin = Generalization(general=Pin, specific=UML2_InputPin)
gen_UML2_ReadLinkObjectEndQualifierAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndQualifierAction)
gen_UML2_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_EncapsulatedClassifier)
gen_UML2_CreateObjectAction_Action = Generalization(general=Action, specific=UML2_CreateObjectAction)
gen_UML2_DurationObservationAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_DurationObservationAction)
gen_UML2_BroadcastSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_BroadcastSignalAction)
gen_UML2_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendSignalAction)
gen_UML2_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ActivityParameterNode)
gen_UML2_ReadVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ReadVariableAction)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_LiteralSpecification)
gen_UML2_OutputPin_Pin = Generalization(general=Pin, specific=UML2_OutputPin)
gen_UML2_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_ReadLinkAction)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_DestroyObjectAction_Action = Generalization(general=Action, specific=UML2_DestroyObjectAction)
gen_UML2_CallOperationAction_CallAction = Generalization(general=CallAction, specific=UML2_CallOperationAction)
gen_UML2_StartOwnedBehaviorAction_Action = Generalization(general=Action, specific=UML2_StartOwnedBehaviorAction)
gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_AddStructuralFeatureValueAction)
gen_UML2_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2_Operation)
gen_UML2_VariableAction_Action = Generalization(general=Action, specific=UML2_VariableAction)
gen_UML2_Enumeration_DataType = Generalization(general=DataType, specific=UML2_Enumeration)
gen_UML2_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_CreateLinkAction)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_CallAction)
gen_UML2_StructuralFeatureAction_Action = Generalization(general=Action, specific=UML2_StructuralFeatureAction)
gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=UML2_RemoveStructuralFeatureValueAction)
gen_UML2_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2_ValueSpecification)
gen_UML2_LinkAction_Action = Generalization(general=Action, specific=UML2_LinkAction)
gen_UML2_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralNull)
gen_UML2_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2_Pin)
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2_Class)
gen_UML2_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=UML2_DestroyLinkAction)
gen_UML2_AcceptEventAction_Action = Generalization(general=Action, specific=UML2_AcceptEventAction)
gen_UML2_RaiseExceptionAction_Action = Generalization(general=Action, specific=UML2_RaiseExceptionAction)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_RemoveVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_RemoveVariableValueAction)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_TemplateableClassifier)
gen_UML2_AddVariableValueAction_WriteVariableAction = Generalization(general=WriteVariableAction, specific=UML2_AddVariableValueAction)
gen_UML2_ReadLinkObjectEndAction_Action = Generalization(general=Action, specific=UML2_ReadLinkObjectEndAction)
gen_UML2_Classifier_Type = Generalization(general=Type, specific=UML2_Classifier)
gen_UML2_ReadExtentAction_Action = Generalization(general=Action, specific=UML2_ReadExtentAction)
gen_UML2_ClearAssociationAction_Action = Generalization(general=Action, specific=UML2_ClearAssociationAction)
gen_UML2_ApplyFunctionAction_Action = Generalization(general=Action, specific=UML2_ApplyFunctionAction)
gen_UML2_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ConditionalNode)
gen_UML2_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralString)
gen_UML2_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_BehavioredClassifier)
gen_UML2_Signal_Classifier = Generalization(general=Classifier, specific=UML2_Signal)
gen_UML2_TimeInterval_Interval = Generalization(general=Interval, specific=UML2_TimeInterval)
gen_UML2_ReclassifyObjectAction_Action = Generalization(general=Action, specific=UML2_ReclassifyObjectAction)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)
gen_UML2_Interface_Classifier = Generalization(general=Classifier, specific=UML2_Interface)
gen_UML2_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2_StructuralFeature)
gen_UML2_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2_Variable)
gen_UML2_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2_PrimitiveType)
gen_UML2_Actor_Classifier = Generalization(general=Classifier, specific=UML2_Actor)
gen_UML2_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_Collaboration)
gen_UML2_Artifact_Classifier = Generalization(general=Classifier, specific=UML2_Artifact)
gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_ClearStructuralFeatureAction)
gen_UML2_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_LoopNode)
gen_UML2_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2_Parameter)
gen_UML2_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2_Property)
gen_UML2_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Duration)
gen_UML2_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=UML2_CallBehaviorAction)
gen_UML2_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_ParameterableClassifier)
gen_UML2_DurationInterval_Interval = Generalization(general=Interval, specific=UML2_DurationInterval)
gen_UML2_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_OpaqueExpression)
gen_UML2_WriteVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_WriteVariableAction)
gen_UML2_InvocationAction_Action = Generalization(general=Action, specific=UML2_InvocationAction)
gen_UML2_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2_ObjectNode)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=UML2_WriteStructuralFeatureAction)
gen_UML2_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralInteger)
gen_UML2_Association_Classifier = Generalization(general=Classifier, specific=UML2_Association)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_TestIdentityAction_Action = Generalization(general=Action, specific=UML2_TestIdentityAction)
gen_UML2_CreateLinkObjectAction_CreateLinkAction = Generalization(general=CreateLinkAction, specific=UML2_CreateLinkObjectAction)
gen_UML2_ClearVariableAction_VariableAction = Generalization(general=VariableAction, specific=UML2_ClearVariableAction)
gen_UML2_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2_InformationItem)
gen_UML2_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralUnlimitedNatural)
gen_UML2_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=UML2_WriteLinkAction)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ExpansionNode)
gen_UML2_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2_ValuePin)
gen_UML2_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2_Expression)
gen_UML2_ReplyAction_Action = Generalization(general=Action, specific=UML2_ReplyAction)
gen_UML2_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralBoolean)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_CentralBufferNode)
gen_UML2_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2_DeploymentSpecification)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=UML2_ExpansionRegion)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_StructuredClassifier)
gen_UML2_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_TimeExpression)
gen_UML2_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_InstanceValue)
gen_UML2_SendObjectAction_InvocationAction = Generalization(general=InvocationAction, specific=UML2_SendObjectAction)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_AcceptCallAction, AcceptEventAction, UML2_ReadStructuralFeatureAction, StructuralFeatureAction, UML2_DataType, Classifier, UML2_StructuredActivityNode, Action, UML2_TimeObservationAction, WriteStructuralFeatureAction, UML2_ReadSelfAction, UML2_OutputPin, UML2_DataStoreNode, CentralBufferNode, UML2_ReadIsClassifiedObjectAction, UML2_Interval, ValueSpecification, UML2_InputPin, Pin, UML2_ReadLinkObjectEndQualifierAction, UML2_EncapsulatedClassifier, StructuredClassifier, UML2_CreateObjectAction, UML2_DurationObservationAction, UML2_BroadcastSignalAction, InvocationAction, UML2_SendSignalAction, UML2_ActivityParameterNode, ObjectNode, UML2_ReadVariableAction, VariableAction, UML2_Port, Property_, UML2_Extension, Association, UML2_LiteralSpecification, UML2_ReadLinkAction, LinkAction, UML2_AssociationClass, Class_, UML2_StateMachine, Behavior, UML2_Device, Node, UML2_DestroyObjectAction, UML2_CallOperationAction, CallAction, UML2_StartOwnedBehaviorAction, UML2_StructuralFeature, UML2_AddStructuralFeatureValueAction, UML2_Operation, UML2_VariableAction, UML2_Enumeration, UML2_CreateLinkAction, WriteLinkAction, UML2_Activity, UML2_CallAction, UML2_StructuralFeatureAction, UML2_RemoveStructuralFeatureValueAction, UML2_ValueSpecification, UML2_LinkAction, UML2_LiteralNull, LiteralSpecification, UML2_Pin, UML2_Class, BehavioredClassifier, EncapsulatedClassifier, UML2_DestroyLinkAction, UML2_AcceptEventAction, UML2_RaiseExceptionAction, UML2_ProtocolStateMachine, StateMachine, UML2_RemoveVariableValueAction, WriteVariableAction, UML2_Behavior, UML2_TemplateableClassifier, UML2_AddVariableValueAction, UML2_ReadLinkObjectEndAction, UML2_Classifier, Type, UML2_ReadExtentAction, UML2_ClearAssociationAction, UML2_ApplyFunctionAction, UML2_ConditionalNode, StructuredActivityNode, UML2_LiteralString, UML2_BehavioredClassifier, UML2_Signal, UML2_TimeInterval, Interval, UML2_ReclassifyObjectAction, UML2_Component, UML2_Interface, TypedElement, UML2_Variable, UML2_PrimitiveType, DataType, UML2_Actor, UML2_Artifact, UML2_ClearStructuralFeatureAction, UML2_LoopNode, UML2_Parameter, UML2_Property, StructuralFeature, UML2_Duration, UML2_CallBehaviorAction, UML2_ParameterableClassifier, UML2_DurationInterval, UML2_OpaqueExpression, UML2_WriteVariableAction, UML2_InvocationAction, UML2_ObjectNode, UML2_TypedElement, UML2_Type, UML2_ExecutionEnvironment, UML2_WriteStructuralFeatureAction, UML2_LiteralInteger, UML2_Association, UML2_UseCase, UML2_TestIdentityAction, UML2_CreateLinkObjectAction, CreateLinkAction, UML2_ClearVariableAction, UML2_InformationItem, UML2_LiteralUnlimitedNatural, UML2_WriteLinkAction, UML2_Interaction, UML2_ExpansionNode, UML2_ValuePin, InputPin, UML2_Expression, OpaqueExpression, UML2_ReplyAction, UML2_LiteralBoolean, UML2_CommunicationPath, UML2_Node, UML2_CentralBufferNode, UML2_DeploymentSpecification, Artifact, UML2_InstanceValue, UML2_Stereotype, UML2_ExpansionRegion, UML2_ExtensionEnd, UML2_Collaboration, UML2_StructuredClassifier, UML2_TimeExpression, UML2_SendObjectAction, UML2_Action},
    associations={result0, type1, context_2},
    generalizations={gen_UML2_AcceptCallAction_AcceptEventAction, gen_UML2_ReadStructuralFeatureAction_StructuralFeatureAction, gen_UML2_DataType_Classifier, gen_UML2_StructuredActivityNode_Action, gen_UML2_TimeObservationAction_WriteStructuralFeatureAction, gen_UML2_ReadSelfAction_Action, gen_UML2_DataStoreNode_CentralBufferNode, gen_UML2_ReadIsClassifiedObjectAction_Action, gen_UML2_Interval_ValueSpecification, gen_UML2_InputPin_Pin, gen_UML2_ReadLinkObjectEndQualifierAction_Action, gen_UML2_EncapsulatedClassifier_StructuredClassifier, gen_UML2_CreateObjectAction_Action, gen_UML2_DurationObservationAction_WriteStructuralFeatureAction, gen_UML2_BroadcastSignalAction_InvocationAction, gen_UML2_SendSignalAction_InvocationAction, gen_UML2_ActivityParameterNode_ObjectNode, gen_UML2_ReadVariableAction_VariableAction, gen_UML2_Port_Property, gen_UML2_Extension_Association, gen_UML2_LiteralSpecification_ValueSpecification, gen_UML2_OutputPin_Pin, gen_UML2_ReadLinkAction_LinkAction, gen_UML2_AssociationClass_Class, gen_UML2_AssociationClass_Association, gen_UML2_StateMachine_Behavior, gen_UML2_Device_Node, gen_UML2_DestroyObjectAction_Action, gen_UML2_CallOperationAction_CallAction, gen_UML2_StartOwnedBehaviorAction_Action, gen_UML2_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_Operation_TypedElement, gen_UML2_VariableAction_Action, gen_UML2_Enumeration_DataType, gen_UML2_CreateLinkAction_WriteLinkAction, gen_UML2_Activity_Behavior, gen_UML2_CallAction_InvocationAction, gen_UML2_StructuralFeatureAction_Action, gen_UML2_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_UML2_ValueSpecification_TypedElement, gen_UML2_LinkAction_Action, gen_UML2_LiteralNull_LiteralSpecification, gen_UML2_Pin_ObjectNode, gen_UML2_Class_BehavioredClassifier, gen_UML2_Class_EncapsulatedClassifier, gen_UML2_DestroyLinkAction_WriteLinkAction, gen_UML2_AcceptEventAction_Action, gen_UML2_RaiseExceptionAction_Action, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_RemoveVariableValueAction_WriteVariableAction, gen_UML2_Behavior_Class, gen_UML2_TemplateableClassifier_Classifier, gen_UML2_AddVariableValueAction_WriteVariableAction, gen_UML2_ReadLinkObjectEndAction_Action, gen_UML2_Classifier_Type, gen_UML2_ReadExtentAction_Action, gen_UML2_ClearAssociationAction_Action, gen_UML2_ApplyFunctionAction_Action, gen_UML2_ConditionalNode_StructuredActivityNode, gen_UML2_LiteralString_LiteralSpecification, gen_UML2_BehavioredClassifier_Classifier, gen_UML2_Signal_Classifier, gen_UML2_TimeInterval_Interval, gen_UML2_ReclassifyObjectAction_Action, gen_UML2_Component_Class, gen_UML2_Interface_Classifier, gen_UML2_StructuralFeature_TypedElement, gen_UML2_Variable_TypedElement, gen_UML2_PrimitiveType_DataType, gen_UML2_Actor_Classifier, gen_UML2_Collaboration_StructuredClassifier, gen_UML2_Artifact_Classifier, gen_UML2_ClearStructuralFeatureAction_StructuralFeatureAction, gen_UML2_LoopNode_StructuredActivityNode, gen_UML2_Parameter_TypedElement, gen_UML2_Property_StructuralFeature, gen_UML2_Duration_ValueSpecification, gen_UML2_CallBehaviorAction_CallAction, gen_UML2_ParameterableClassifier_Classifier, gen_UML2_DurationInterval_Interval, gen_UML2_OpaqueExpression_ValueSpecification, gen_UML2_WriteVariableAction_VariableAction, gen_UML2_InvocationAction_Action, gen_UML2_ObjectNode_TypedElement, gen_UML2_ExecutionEnvironment_Node, gen_UML2_WriteStructuralFeatureAction_StructuralFeatureAction, gen_UML2_LiteralInteger_LiteralSpecification, gen_UML2_Association_Classifier, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_TestIdentityAction_Action, gen_UML2_CreateLinkObjectAction_CreateLinkAction, gen_UML2_ClearVariableAction_VariableAction, gen_UML2_InformationItem_Classifier, gen_UML2_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2_WriteLinkAction_LinkAction, gen_UML2_Interaction_Behavior, gen_UML2_ExpansionNode_ObjectNode, gen_UML2_ValuePin_InputPin, gen_UML2_Expression_OpaqueExpression, gen_UML2_ReplyAction_Action, gen_UML2_LiteralBoolean_LiteralSpecification, gen_UML2_CommunicationPath_Association, gen_UML2_Node_Class, gen_UML2_CentralBufferNode_ObjectNode, gen_UML2_DeploymentSpecification_Artifact, gen_UML2_Stereotype_Class, gen_UML2_ExpansionRegion_StructuredActivityNode, gen_UML2_ExtensionEnd_Property, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_StructuredClassifier_Classifier, gen_UML2_TimeExpression_ValueSpecification, gen_UML2_InstanceValue_ValueSpecification, gen_UML2_SendObjectAction_InvocationAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)