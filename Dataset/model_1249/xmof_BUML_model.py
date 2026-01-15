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
CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="sequential")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="return")
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
xmof_BasicBehaviors_Behavior = Class(name="xmof::BasicBehaviors::Behavior", is_abstract=True)
BehavioredEClass = Class(name="BehavioredEClass")
Kernel_BehavioredEOperation = Class(name="Kernel::BehavioredEOperation")
xmof_BasicBehaviors_OpaqueBehavior = Class(name="xmof::BasicBehaviors::OpaqueBehavior")
Behavior = Class(name="Behavior")
xmof_Communications_Trigger = Class(name="xmof::Communications::Trigger")
ENamedElement = Class(name="ENamedElement")
Communications_Event = Class(name="Communications::Event")
xmof_Communications_Event = Class(name="xmof::Communications::Event", is_abstract=True)
xmof_Communications_Signal = Class(name="xmof::Communications::Signal")
Communications_xmof_EAttribute = Class(name="Communications::xmof::EAttribute")
Kernel_DirectedParameter = Class(name="Kernel::DirectedParameter")
xmof_Communications_SignalEvent = Class(name="xmof::Communications::SignalEvent")
MessageEvent = Class(name="MessageEvent")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors::BehavioredClassifier")
Communications_Signal = Class(name="Communications::Signal")
xmof_Communications_MessageEvent = Class(name="xmof::Communications::MessageEvent", is_abstract=True)
Event = Class(name="Event")
xmof_BasicBehaviors_BehavioredClassifier = Class(name="xmof::BasicBehaviors::BehavioredClassifier", is_abstract=True)
xmof_Communications_Reception = Class(name="xmof::Communications::Reception")
EClassifier = Class(name="EClassifier")
BehavioredEOperation = Class(name="BehavioredEOperation")
BasicBehaviors_Behavior = Class(name="BasicBehaviors::Behavior")
xmof_BasicBehaviors_FunctionBehavior = Class(name="xmof::BasicBehaviors::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
xmof_Kernel_BehavioredEClass = Class(name="xmof::Kernel::BehavioredEClass")
EClass = Class(name="EClass")
xmof_Kernel_DirectedParameter = Class(name="xmof::Kernel::DirectedParameter")
EParameter = Class(name="EParameter")
xmof_Kernel_EEnumLiteralSpecification = Class(name="xmof::Kernel::EEnumLiteralSpecification")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_xmof_EEnumLiteral = Class(name="Kernel::xmof::EEnumLiteral")
xmof_Kernel_EnumValue = Class(name="xmof::Kernel::EnumValue")
ValueSpecification = Class(name="ValueSpecification")
Kernel_EEnumLiteralSpecification = Class(name="Kernel::EEnumLiteralSpecification")
xmof_Kernel_ValueSpecification = Class(name="xmof::Kernel::ValueSpecification", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
xmof_Kernel_InstanceSpecification = Class(name="xmof::Kernel::InstanceSpecification")
Kernel_xmof_EClassifier = Class(name="Kernel::xmof::EClassifier")
Kernel_Slot = Class(name="Kernel::Slot")
xmof_Kernel_BehavioredEOperation = Class(name="xmof::Kernel::BehavioredEOperation")
EOperation = Class(name="EOperation")
Kernel_InstanceSpecification = Class(name="Kernel::InstanceSpecification")
xmof_Kernel_InstanceValue = Class(name="xmof::Kernel::InstanceValue")
xmof_Kernel_LiteralBoolean = Class(name="xmof::Kernel::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
xmof_Kernel_LiteralSpecification = Class(name="xmof::Kernel::LiteralSpecification", is_abstract=True)
xmof_Kernel_LiteralInteger = Class(name="xmof::Kernel::LiteralInteger")
xmof_Kernel_LiteralNull = Class(name="xmof::Kernel::LiteralNull")
xmof_Kernel_LiteralString = Class(name="xmof::Kernel::LiteralString")
xmof_Kernel_Slot = Class(name="xmof::Kernel::Slot")
EModelElement = Class(name="EModelElement")
Kernel_xmof_EStructuralFeature = Class(name="Kernel::xmof::EStructuralFeature")
Kernel_ValueSpecification = Class(name="Kernel::ValueSpecification")
ActivityEdge = Class(name="ActivityEdge")
xmof_IntermediateActivities_ActivityEdge = Class(name="xmof::IntermediateActivities::ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities::Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities::ActivityNode")
xmof_Kernel_LiteralUnlimitedNatural = Class(name="xmof::Kernel::LiteralUnlimitedNatural")
xmof_Kernel_PrimitiveType = Class(name="xmof::Kernel::PrimitiveType")
EDataType = Class(name="EDataType")
xmof_IntermediateActivities_ObjectFlow = Class(name="xmof::IntermediateActivities::ObjectFlow")
xmof_IntermediateActivities_MergeNode = Class(name="xmof::IntermediateActivities::MergeNode")
ControlNode = Class(name="ControlNode")
xmof_IntermediateActivities_Activity = Class(name="xmof::IntermediateActivities::Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities::ActivityEdge")
xmof_IntermediateActivities_ActivityNode = Class(name="xmof::IntermediateActivities::ActivityNode", is_abstract=True)
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities::StructuredActivityNode")
xmof_IntermediateActivities_ObjectNode = Class(name="xmof::IntermediateActivities::ObjectNode", is_abstract=True)
xmof_IntermediateActivities_ControlNode = Class(name="xmof::IntermediateActivities::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
xmof_IntermediateActivities_JoinNode = Class(name="xmof::IntermediateActivities::JoinNode")
xmof_IntermediateActivities_InitialNode = Class(name="xmof::IntermediateActivities::InitialNode")
xmof_IntermediateActivities_FinalNode = Class(name="xmof::IntermediateActivities::FinalNode", is_abstract=True)
xmof_IntermediateActivities_ForkNode = Class(name="xmof::IntermediateActivities::ForkNode")
xmof_IntermediateActivities_ControlFlow = Class(name="xmof::IntermediateActivities::ControlFlow")
xmof_IntermediateActivities_DecisionNode = Class(name="xmof::IntermediateActivities::DecisionNode")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities::ObjectFlow")
xmof_IntermediateActivities_ActivityFinalNode = Class(name="xmof::IntermediateActivities::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
xmof_IntermediateActivities_ActivityParameterNode = Class(name="xmof::IntermediateActivities::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
xmof_CompleteStructuredActivities_LoopNode = Class(name="xmof::CompleteStructuredActivities::LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions::OutputPin")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities::ExecutableNode")
BasicActions_InputPin = Class(name="BasicActions::InputPin")
xmof_CompleteStructuredActivities_ExecutableNode = Class(name="xmof::CompleteStructuredActivities::ExecutableNode", is_abstract=True)
xmof_CompleteStructuredActivities_Clause = Class(name="xmof::CompleteStructuredActivities::Clause")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities::Clause")
xmof_CompleteStructuredActivities_ConditionalNode = Class(name="xmof::CompleteStructuredActivities::ConditionalNode")
xmof_CompleteStructuredActivities_StructuredActivityNode = Class(name="xmof::CompleteStructuredActivities::StructuredActivityNode")
Action = Class(name="Action")
xmof_IntermediateActions_StructuralFeatureAction = Class(name="xmof::IntermediateActions::StructuralFeatureAction", is_abstract=True)
xmof_ExtraStructuredActivities_ExpansionNode = Class(name="xmof::ExtraStructuredActivities::ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities::ExpansionRegion")
xmof_ExtraStructuredActivities_ExpansionRegion = Class(name="xmof::ExtraStructuredActivities::ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities::ExpansionNode")
xmof_IntermediateActions_WriteLinkAction = Class(name="xmof::IntermediateActions::WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
xmof_IntermediateActions_LinkAction = Class(name="xmof::IntermediateActions::LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions::LinkEndData")
IntermediateActions_xmof_EStructuralFeature = Class(name="IntermediateActions::xmof::EStructuralFeature")
xmof_IntermediateActions_LinkEndData = Class(name="xmof::IntermediateActions::LinkEndData")
xmof_IntermediateActions_TestIdentityAction = Class(name="xmof::IntermediateActions::TestIdentityAction")
xmof_IntermediateActions_ValueSpecificationAction = Class(name="xmof::IntermediateActions::ValueSpecificationAction")
xmof_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="xmof::IntermediateActions::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
xmof_IntermediateActions_ReadLinkAction = Class(name="xmof::IntermediateActions::ReadLinkAction")
IntermediateActions_xmof_EReference = Class(name="IntermediateActions::xmof::EReference")
xmof_IntermediateActions_WriteStructuralFeatureAction = Class(name="xmof::IntermediateActions::WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
xmof_IntermediateActions_LinkEndCreationData = Class(name="xmof::IntermediateActions::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
xmof_IntermediateActions_LinkEndDestructionData = Class(name="xmof::IntermediateActions::LinkEndDestructionData")
xmof_IntermediateActions_ClearAssociationAction = Class(name="xmof::IntermediateActions::ClearAssociationAction")
xmof_IntermediateActions_ReadSelfAction = Class(name="xmof::IntermediateActions::ReadSelfAction")
xmof_IntermediateActions_ReadStructuralFeatureAction = Class(name="xmof::IntermediateActions::ReadStructuralFeatureAction")
xmof_IntermediateActions_CreateObjectAction = Class(name="xmof::IntermediateActions::CreateObjectAction")
IntermediateActions_xmof_EClassifier = Class(name="IntermediateActions::xmof::EClassifier")
xmof_IntermediateActions_DestroyLinkAction = Class(name="xmof::IntermediateActions::DestroyLinkAction")
xmof_IntermediateActions_DestroyObjectAction = Class(name="xmof::IntermediateActions::DestroyObjectAction")
xmof_IntermediateActions_ClearStructuralFeatureAction = Class(name="xmof::IntermediateActions::ClearStructuralFeatureAction")
xmof_IntermediateActions_CreateLinkAction = Class(name="xmof::IntermediateActions::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
xmof_CompleteActions_StartObjectBehaviorAction = Class(name="xmof::CompleteActions::StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
xmof_CompleteActions_ReduceAction = Class(name="xmof::CompleteActions::ReduceAction")
xmof_IntermediateActions_AddStructuralFeatureValueAction = Class(name="xmof::IntermediateActions::AddStructuralFeatureValueAction")
xmof_CompleteActions_StartClassifierBehaviorAction = Class(name="xmof::CompleteActions::StartClassifierBehaviorAction")
xmof_CompleteActions_ReadExtentAction = Class(name="xmof::CompleteActions::ReadExtentAction")
CompleteActions_xmof_EClassifier = Class(name="CompleteActions::xmof::EClassifier")
xmof_CompleteActions_ReadIsClassifiedObjectAction = Class(name="xmof::CompleteActions::ReadIsClassifiedObjectAction")
xmof_CompleteActions_ReclassifyObjectAction = Class(name="xmof::CompleteActions::ReclassifyObjectAction")
xmof_CompleteActions_AcceptEventAction = Class(name="xmof::CompleteActions::AcceptEventAction")
xmof_BasicActions_Pin = Class(name="xmof::BasicActions::Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities::ObjectNode")
xmof_BasicActions_CallAction = Class(name="xmof::BasicActions::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
Communications_Trigger = Class(name="Communications::Trigger")
xmof_BasicActions_Action = Class(name="xmof::BasicActions::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
BasicActions_xmof_EClassifier = Class(name="BasicActions::xmof::EClassifier")
xmof_BasicActions_InputPin = Class(name="xmof::BasicActions::InputPin")
Pin = Class(name="Pin")
xmof_BasicActions_CallBehaviorAction = Class(name="xmof::BasicActions::CallBehaviorAction")
xmof_BasicActions_InvocationAction = Class(name="xmof::BasicActions::InvocationAction", is_abstract=True)
xmof_BasicActions_SendSignalAction = Class(name="xmof::BasicActions::SendSignalAction")
xmof_Kernel_EnumerationValue = Class(name="xmof::Kernel::EnumerationValue")
xmof_BasicActions_CallOperationAction = Class(name="xmof::BasicActions::CallOperationAction")
xmof_BasicActions_OutputPin = Class(name="xmof::BasicActions::OutputPin")
xmof_Kernel_PrimitiveValue = Class(name="xmof::Kernel::PrimitiveValue", is_abstract=True)
Value = Class(name="Value")
Kernel_PrimitiveType = Class(name="Kernel::PrimitiveType")
xmof_Kernel_StringValue = Class(name="xmof::Kernel::StringValue")
PrimitiveValue = Class(name="PrimitiveValue")
xmof_Kernel_IntegerValue = Class(name="xmof::Kernel::IntegerValue")
Kernel_xmof_EEnum = Class(name="Kernel::xmof::EEnum")
xmof_Kernel_BooleanValue = Class(name="xmof::Kernel::BooleanValue")
xmof_Kernel_Value = Class(name="xmof::Kernel::Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")
xmof_Kernel_ObjectValue = Class(name="xmof::Kernel::ObjectValue")
Kernel_xmof_EObject = Class(name="Kernel::xmof::EObject")
xmof_LociL1_SemanticVisitor = Class(name="xmof::LociL1::SemanticVisitor", is_abstract=True)
xmof_BasicBehaviors_ParameterValue = Class(name="xmof::BasicBehaviors::ParameterValue")
Kernel_Value = Class(name="Kernel::Value")
xmof_BasicBehaviors_ParameterValueDefinition = Class(name="xmof::BasicBehaviors::ParameterValueDefinition")
BasicBehaviors_ParameterValue = Class(name="BasicBehaviors::ParameterValue")

# xmof_BasicBehaviors_Behavior class attributes and methods
xmof_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
xmof_BasicBehaviors_Behavior.attributes={xmof_BasicBehaviors_Behavior_reentrant}

# BehavioredEClass class attributes and methods

# Kernel_BehavioredEOperation class attributes and methods

# xmof_BasicBehaviors_OpaqueBehavior class attributes and methods
xmof_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior.attributes={xmof_BasicBehaviors_OpaqueBehavior_language, xmof_BasicBehaviors_OpaqueBehavior_body}

# Behavior class attributes and methods

# xmof_Communications_Trigger class attributes and methods

# ENamedElement class attributes and methods

# Communications_Event class attributes and methods

# xmof_Communications_Event class attributes and methods

# xmof_Communications_Signal class attributes and methods

# Communications_xmof_EAttribute class attributes and methods

# Kernel_DirectedParameter class attributes and methods

# xmof_Communications_SignalEvent class attributes and methods

# MessageEvent class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# Communications_Signal class attributes and methods

# xmof_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# xmof_BasicBehaviors_BehavioredClassifier class attributes and methods

# xmof_Communications_Reception class attributes and methods

# EClassifier class attributes and methods

# BehavioredEOperation class attributes and methods

# BasicBehaviors_Behavior class attributes and methods

# xmof_BasicBehaviors_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# xmof_Kernel_BehavioredEClass class attributes and methods

# EClass class attributes and methods

# xmof_Kernel_DirectedParameter class attributes and methods
xmof_Kernel_DirectedParameter_direction: Property = Property(name="direction", type=StringType)
xmof_Kernel_DirectedParameter.attributes={xmof_Kernel_DirectedParameter_direction}

# EParameter class attributes and methods

# xmof_Kernel_EEnumLiteralSpecification class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_xmof_EEnumLiteral class attributes and methods

# xmof_Kernel_EnumValue class attributes and methods

# ValueSpecification class attributes and methods

# Kernel_EEnumLiteralSpecification class attributes and methods

# xmof_Kernel_ValueSpecification class attributes and methods

# ETypedElement class attributes and methods

# xmof_Kernel_InstanceSpecification class attributes and methods

# Kernel_xmof_EClassifier class attributes and methods

# Kernel_Slot class attributes and methods

# xmof_Kernel_BehavioredEOperation class attributes and methods

# EOperation class attributes and methods

# Kernel_InstanceSpecification class attributes and methods

# xmof_Kernel_InstanceValue class attributes and methods

# xmof_Kernel_LiteralBoolean class attributes and methods
xmof_Kernel_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
xmof_Kernel_LiteralBoolean.attributes={xmof_Kernel_LiteralBoolean_value}

# LiteralSpecification class attributes and methods

# xmof_Kernel_LiteralSpecification class attributes and methods

# xmof_Kernel_LiteralInteger class attributes and methods
xmof_Kernel_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
xmof_Kernel_LiteralInteger.attributes={xmof_Kernel_LiteralInteger_value}

# xmof_Kernel_LiteralNull class attributes and methods

# xmof_Kernel_LiteralString class attributes and methods
xmof_Kernel_LiteralString_value: Property = Property(name="value", type=StringType)
xmof_Kernel_LiteralString.attributes={xmof_Kernel_LiteralString_value}

# xmof_Kernel_Slot class attributes and methods

# EModelElement class attributes and methods

# Kernel_xmof_EStructuralFeature class attributes and methods

# Kernel_ValueSpecification class attributes and methods

# ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# xmof_Kernel_LiteralUnlimitedNatural class attributes and methods
xmof_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
xmof_Kernel_LiteralUnlimitedNatural.attributes={xmof_Kernel_LiteralUnlimitedNatural_value}

# xmof_Kernel_PrimitiveType class attributes and methods

# EDataType class attributes and methods

# xmof_IntermediateActivities_ObjectFlow class attributes and methods

# xmof_IntermediateActivities_MergeNode class attributes and methods

# ControlNode class attributes and methods

# xmof_IntermediateActivities_Activity class attributes and methods
xmof_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
xmof_IntermediateActivities_Activity.attributes={xmof_IntermediateActivities_Activity_readOnly}

# IntermediateActivities_ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# xmof_IntermediateActivities_ObjectNode class attributes and methods

# xmof_IntermediateActivities_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# xmof_IntermediateActivities_JoinNode class attributes and methods

# xmof_IntermediateActivities_InitialNode class attributes and methods

# xmof_IntermediateActivities_FinalNode class attributes and methods

# xmof_IntermediateActivities_ForkNode class attributes and methods

# xmof_IntermediateActivities_ControlFlow class attributes and methods

# xmof_IntermediateActivities_DecisionNode class attributes and methods

# IntermediateActivities_ObjectFlow class attributes and methods

# xmof_IntermediateActivities_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# xmof_IntermediateActivities_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# xmof_CompleteStructuredActivities_LoopNode class attributes and methods
xmof_CompleteStructuredActivities_LoopNode_testedFirst: Property = Property(name="testedFirst", type=BooleanType)
xmof_CompleteStructuredActivities_LoopNode.attributes={xmof_CompleteStructuredActivities_LoopNode_testedFirst}

# StructuredActivityNode class attributes and methods

# BasicActions_OutputPin class attributes and methods

# CompleteStructuredActivities_ExecutableNode class attributes and methods

# BasicActions_InputPin class attributes and methods

# xmof_CompleteStructuredActivities_ExecutableNode class attributes and methods

# xmof_CompleteStructuredActivities_Clause class attributes and methods

# CompleteStructuredActivities_Clause class attributes and methods

# xmof_CompleteStructuredActivities_ConditionalNode class attributes and methods
xmof_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode.attributes={xmof_CompleteStructuredActivities_ConditionalNode_assured, xmof_CompleteStructuredActivities_ConditionalNode_determinate}

# xmof_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
xmof_CompleteStructuredActivities_StructuredActivityNode.attributes={xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# xmof_IntermediateActions_StructuralFeatureAction class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionRegion class attributes and methods
xmof_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
xmof_ExtraStructuredActivities_ExpansionRegion.attributes={xmof_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# xmof_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# xmof_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# IntermediateActions_xmof_EStructuralFeature class attributes and methods

# xmof_IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_TestIdentityAction class attributes and methods

# xmof_IntermediateActions_ValueSpecificationAction class attributes and methods

# xmof_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_ReadLinkAction class attributes and methods

# IntermediateActions_xmof_EReference class attributes and methods

# xmof_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_LinkEndCreationData class attributes and methods
xmof_IntermediateActions_LinkEndCreationData_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_IntermediateActions_LinkEndCreationData.attributes={xmof_IntermediateActions_LinkEndCreationData_replaceAll}

# LinkEndData class attributes and methods

# xmof_IntermediateActions_LinkEndDestructionData class attributes and methods
xmof_IntermediateActions_LinkEndDestructionData_destroyDuplicates: Property = Property(name="destroyDuplicates", type=BooleanType)
xmof_IntermediateActions_LinkEndDestructionData.attributes={xmof_IntermediateActions_LinkEndDestructionData_destroyDuplicates}

# xmof_IntermediateActions_ClearAssociationAction class attributes and methods

# xmof_IntermediateActions_ReadSelfAction class attributes and methods

# xmof_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_CreateObjectAction class attributes and methods

# IntermediateActions_xmof_EClassifier class attributes and methods

# xmof_IntermediateActions_DestroyLinkAction class attributes and methods

# xmof_IntermediateActions_DestroyObjectAction class attributes and methods
xmof_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
xmof_IntermediateActions_DestroyObjectAction.attributes={xmof_IntermediateActions_DestroyObjectAction_destroyLinks, xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects}

# xmof_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# xmof_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# xmof_CompleteActions_ReduceAction class attributes and methods
xmof_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
xmof_CompleteActions_ReduceAction.attributes={xmof_CompleteActions_ReduceAction_ordered}

# xmof_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_IntermediateActions_AddStructuralFeatureValueAction.attributes={xmof_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# xmof_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# xmof_CompleteActions_ReadExtentAction class attributes and methods

# CompleteActions_xmof_EClassifier class attributes and methods

# xmof_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
xmof_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
xmof_CompleteActions_ReadIsClassifiedObjectAction.attributes={xmof_CompleteActions_ReadIsClassifiedObjectAction_direct}

# xmof_CompleteActions_ReclassifyObjectAction class attributes and methods
xmof_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_CompleteActions_ReclassifyObjectAction.attributes={xmof_CompleteActions_ReclassifyObjectAction_replaceAll}

# xmof_CompleteActions_AcceptEventAction class attributes and methods
xmof_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
xmof_CompleteActions_AcceptEventAction.attributes={xmof_CompleteActions_AcceptEventAction_unmarshall}

# xmof_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# xmof_BasicActions_CallAction class attributes and methods
xmof_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
xmof_BasicActions_CallAction.attributes={xmof_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# Communications_Trigger class attributes and methods

# xmof_BasicActions_Action class attributes and methods
xmof_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
xmof_BasicActions_Action.attributes={xmof_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# BasicActions_xmof_EClassifier class attributes and methods

# xmof_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# xmof_BasicActions_CallBehaviorAction class attributes and methods

# xmof_BasicActions_InvocationAction class attributes and methods

# xmof_BasicActions_SendSignalAction class attributes and methods

# xmof_Kernel_EnumerationValue class attributes and methods

# xmof_BasicActions_CallOperationAction class attributes and methods

# xmof_BasicActions_OutputPin class attributes and methods

# xmof_Kernel_PrimitiveValue class attributes and methods

# Value class attributes and methods

# Kernel_PrimitiveType class attributes and methods

# xmof_Kernel_StringValue class attributes and methods
xmof_Kernel_StringValue_value: Property = Property(name="value", type=StringType)
xmof_Kernel_StringValue.attributes={xmof_Kernel_StringValue_value}

# PrimitiveValue class attributes and methods

# xmof_Kernel_IntegerValue class attributes and methods
xmof_Kernel_IntegerValue_value: Property = Property(name="value", type=IntegerType)
xmof_Kernel_IntegerValue.attributes={xmof_Kernel_IntegerValue_value}

# Kernel_xmof_EEnum class attributes and methods

# xmof_Kernel_BooleanValue class attributes and methods
xmof_Kernel_BooleanValue_value: Property = Property(name="value", type=BooleanType)
xmof_Kernel_BooleanValue.attributes={xmof_Kernel_BooleanValue_value}

# xmof_Kernel_Value class attributes and methods

# SemanticVisitor class attributes and methods

# xmof_Kernel_ObjectValue class attributes and methods

# Kernel_xmof_EObject class attributes and methods

# xmof_LociL1_SemanticVisitor class attributes and methods

# xmof_BasicBehaviors_ParameterValue class attributes and methods

# Kernel_Value class attributes and methods

# xmof_BasicBehaviors_ParameterValueDefinition class attributes and methods

# BasicBehaviors_ParameterValue class attributes and methods

# Relationships
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="Syntax", type=xmof_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(0, 1))
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="Communications_Event", type=xmof_Communications_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Communications_Trigger", type=Communications_Event, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute9: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute9",
    ends={
        Property(name="Communications_xmof_EAttribute", type=xmof_Communications_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Communications_Signal", type=Communications_xmof_EAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter1: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1",
    ends={
        Property(name="Kernel_DirectedParameter", type=xmof_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_Behavior", type=Kernel_DirectedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context2: BinaryAssociation = BinaryAssociation(
    name="context2",
    ends={
        Property(name="BasicBehaviors_BehavioredClassifier", type=xmof_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_Behavior3", type=BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
signal10: BinaryAssociation = BinaryAssociation(
    name="signal10",
    ends={
        Property(name="Communications_Signal", type=xmof_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Communications_SignalEvent", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
ownedBehavior4: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior4",
    ends={
        Property(name="BasicBehaviors_Behavior", type=xmof_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_BehavioredClassifier", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior5: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior5",
    ends={
        Property(name="BasicBehaviors_Behavior7", type=xmof_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_BehavioredClassifier6", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
eEnumLiteral15: BinaryAssociation = BinaryAssociation(
    name="eEnumLiteral15",
    ends={
        Property(name="Kernel_xmof_EEnumLiteral", type=xmof_Kernel_EEnumLiteralSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EEnumLiteralSpecification", type=Kernel_xmof_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
eEnumLiteralSpecification16: BinaryAssociation = BinaryAssociation(
    name="eEnumLiteralSpecification16",
    ends={
        Property(name="Kernel_EEnumLiteralSpecification", type=xmof_Kernel_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumValue", type=Kernel_EEnumLiteralSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier17: BinaryAssociation = BinaryAssociation(
    name="classifier17",
    ends={
        Property(name="Kernel_xmof_EClassifier", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceSpecification", type=Kernel_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot18: BinaryAssociation = BinaryAssociation(
    name="slot18",
    ends={
        Property(name="Syntax20", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes19", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal11: BinaryAssociation = BinaryAssociation(
    name="signal11",
    ends={
        Property(name="Communications_Signal12", type=xmof_Communications_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Communications_Reception", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
method13: BinaryAssociation = BinaryAssociation(
    name="method13",
    ends={
        Property(name="Syntax14", type=xmof_Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehaviors", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
owningInstance24: BinaryAssociation = BinaryAssociation(
    name="owningInstance24",
    ends={
        Property(name="Syntax26", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes25", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance27: BinaryAssociation = BinaryAssociation(
    name="instance27",
    ends={
        Property(name="Kernel_InstanceSpecification", type=xmof_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
definingFeature21: BinaryAssociation = BinaryAssociation(
    name="definingFeature21",
    ends={
        Property(name="Kernel_xmof_EStructuralFeature", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot", type=Kernel_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="Kernel_ValueSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot23", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity28: BinaryAssociation = BinaryAssociation(
    name="activity28",
    ends={
        Property(name="Syntax29", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="Syntax32", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities31", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard39: BinaryAssociation = BinaryAssociation(
    name="guard39",
    ends={
        Property(name="Kernel_ValueSpecification40", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node41: BinaryAssociation = BinaryAssociation(
    name="node41",
    ends={
        Property(name="Syntax43", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities42", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge44: BinaryAssociation = BinaryAssociation(
    name="edge44",
    ends={
        Property(name="Syntax46", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities45", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode47: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode47",
    ends={
        Property(name="Syntax49", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities48", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity50: BinaryAssociation = BinaryAssociation(
    name="activity50",
    ends={
        Property(name="Syntax52", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities51", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing53: BinaryAssociation = BinaryAssociation(
    name="outgoing53",
    ends={
        Property(name="Syntax55", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities54", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="Syntax35", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities34", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
incoming56: BinaryAssociation = BinaryAssociation(
    name="incoming56",
    ends={
        Property(name="Syntax58", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities57", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode36: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode36",
    ends={
        Property(name="Syntax38", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities37", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
bodyOutput68: BinaryAssociation = BinaryAssociation(
    name="bodyOutput68",
    ends={
        Property(name="BasicActions_OutputPin70", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode69", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput59: BinaryAssociation = BinaryAssociation(
    name="decisionInput59",
    ends={
        Property(name="BasicBehaviors_Behavior60", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow61: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow61",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode62", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
parameter63: BinaryAssociation = BinaryAssociation(
    name="parameter63",
    ends={
        Property(name="Kernel_DirectedParameter64", type=xmof_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityParameterNode", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
decider65: BinaryAssociation = BinaryAssociation(
    name="decider65",
    ends={
        Property(name="BasicActions_OutputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test66: BinaryAssociation = BinaryAssociation(
    name="test66",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode67", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
successorClause93: BinaryAssociation = BinaryAssociation(
    name="successorClause93",
    ends={
        Property(name="Syntax95", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities94", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput71: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput71",
    ends={
        Property(name="BasicActions_InputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode72", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart73: BinaryAssociation = BinaryAssociation(
    name="bodyPart73",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode75", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode74", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result76: BinaryAssociation = BinaryAssociation(
    name="result76",
    ends={
        Property(name="BasicActions_OutputPin78", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode77", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable79: BinaryAssociation = BinaryAssociation(
    name="loopVariable79",
    ends={
        Property(name="BasicActions_OutputPin81", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode80", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart82: BinaryAssociation = BinaryAssociation(
    name="setupPart82",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode84", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode83", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test85: BinaryAssociation = BinaryAssociation(
    name="test85",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode86", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body87: BinaryAssociation = BinaryAssociation(
    name="body87",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode89", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause88", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause90: BinaryAssociation = BinaryAssociation(
    name="predecessorClause90",
    ends={
        Property(name="Syntax92", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities91", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider96: BinaryAssociation = BinaryAssociation(
    name="decider96",
    ends={
        Property(name="BasicActions_OutputPin98", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause97", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput99: BinaryAssociation = BinaryAssociation(
    name="bodyOutput99",
    ends={
        Property(name="BasicActions_OutputPin101", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause100", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause102: BinaryAssociation = BinaryAssociation(
    name="clause102",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result103: BinaryAssociation = BinaryAssociation(
    name="result103",
    ends={
        Property(name="BasicActions_OutputPin105", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode104", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node106: BinaryAssociation = BinaryAssociation(
    name="node106",
    ends={
        Property(name="Syntax108", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities107", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge109: BinaryAssociation = BinaryAssociation(
    name="edge109",
    ends={
        Property(name="Syntax111", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities110", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput112: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput112",
    ends={
        Property(name="BasicActions_OutputPin113", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput114: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput114",
    ends={
        Property(name="BasicActions_InputPin116", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode115", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputElement126: BinaryAssociation = BinaryAssociation(
    name="outputElement126",
    ends={
        Property(name="Syntax128", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities127", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
regionAsOutput117: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput117",
    ends={
        Property(name="Syntax119", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities118", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput120: BinaryAssociation = BinaryAssociation(
    name="regionAsInput120",
    ends={
        Property(name="Syntax122", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities121", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement123: BinaryAssociation = BinaryAssociation(
    name="inputElement123",
    ends={
        Property(name="Syntax125", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities124", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
result143: BinaryAssociation = BinaryAssociation(
    name="result143",
    ends={
        Property(name="BasicActions_OutputPin145", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction144", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData146: BinaryAssociation = BinaryAssociation(
    name="endData146",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
structuralFeature129: BinaryAssociation = BinaryAssociation(
    name="structuralFeature129",
    ends={
        Property(name="IntermediateActions_xmof_EStructuralFeature", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction", type=IntermediateActions_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
inputValue147: BinaryAssociation = BinaryAssociation(
    name="inputValue147",
    ends={
        Property(name="BasicActions_InputPin149", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction148", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
object130: BinaryAssociation = BinaryAssociation(
    name="object130",
    ends={
        Property(name="BasicActions_InputPin132", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction131", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value150: BinaryAssociation = BinaryAssociation(
    name="value150",
    ends={
        Property(name="BasicActions_InputPin151", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
second133: BinaryAssociation = BinaryAssociation(
    name="second133",
    ends={
        Property(name="BasicActions_InputPin134", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result135: BinaryAssociation = BinaryAssociation(
    name="result135",
    ends={
        Property(name="BasicActions_OutputPin137", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction136", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first138: BinaryAssociation = BinaryAssociation(
    name="first138",
    ends={
        Property(name="BasicActions_InputPin140", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction139", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value141: BinaryAssociation = BinaryAssociation(
    name="value141",
    ends={
        Property(name="Kernel_ValueSpecification142", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value154: BinaryAssociation = BinaryAssociation(
    name="value154",
    ends={
        Property(name="BasicActions_InputPin155", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result156: BinaryAssociation = BinaryAssociation(
    name="result156",
    ends={
        Property(name="BasicActions_OutputPin158", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction157", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt159: BinaryAssociation = BinaryAssociation(
    name="removeAt159",
    ends={
        Property(name="BasicActions_InputPin160", type=xmof_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end152: BinaryAssociation = BinaryAssociation(
    name="end152",
    ends={
        Property(name="IntermediateActions_xmof_EReference", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData153", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
result165: BinaryAssociation = BinaryAssociation(
    name="result165",
    ends={
        Property(name="BasicActions_OutputPin166", type=xmof_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt167: BinaryAssociation = BinaryAssociation(
    name="insertAt167",
    ends={
        Property(name="BasicActions_InputPin168", type=xmof_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt169: BinaryAssociation = BinaryAssociation(
    name="destroyAt169",
    ends={
        Property(name="BasicActions_InputPin170", type=xmof_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
result161: BinaryAssociation = BinaryAssociation(
    name="result161",
    ends={
        Property(name="BasicActions_OutputPin162", type=xmof_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result163: BinaryAssociation = BinaryAssociation(
    name="result163",
    ends={
        Property(name="BasicActions_OutputPin164", type=xmof_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result178: BinaryAssociation = BinaryAssociation(
    name="result178",
    ends={
        Property(name="BasicActions_OutputPin179", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier180: BinaryAssociation = BinaryAssociation(
    name="classifier180",
    ends={
        Property(name="IntermediateActions_xmof_EClassifier", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction181", type=IntermediateActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
target182: BinaryAssociation = BinaryAssociation(
    name="target182",
    ends={
        Property(name="BasicActions_InputPin183", type=xmof_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association171: BinaryAssociation = BinaryAssociation(
    name="association171",
    ends={
        Property(name="IntermediateActions_xmof_EReference172", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
object173: BinaryAssociation = BinaryAssociation(
    name="object173",
    ends={
        Property(name="BasicActions_InputPin175", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction174", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result176: BinaryAssociation = BinaryAssociation(
    name="result176",
    ends={
        Property(name="BasicActions_OutputPin177", type=xmof_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object188: BinaryAssociation = BinaryAssociation(
    name="object188",
    ends={
        Property(name="BasicActions_InputPin189", type=xmof_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer190: BinaryAssociation = BinaryAssociation(
    name="reducer190",
    ends={
        Property(name="BasicBehaviors_Behavior191", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
insertAt184: BinaryAssociation = BinaryAssociation(
    name="insertAt184",
    ends={
        Property(name="BasicActions_InputPin185", type=xmof_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object186: BinaryAssociation = BinaryAssociation(
    name="object186",
    ends={
        Property(name="BasicActions_InputPin187", type=xmof_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection195: BinaryAssociation = BinaryAssociation(
    name="collection195",
    ends={
        Property(name="BasicActions_InputPin197", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction196", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result198: BinaryAssociation = BinaryAssociation(
    name="result198",
    ends={
        Property(name="BasicActions_OutputPin199", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier200: BinaryAssociation = BinaryAssociation(
    name="classifier200",
    ends={
        Property(name="CompleteActions_xmof_EClassifier", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction201", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result192: BinaryAssociation = BinaryAssociation(
    name="result192",
    ends={
        Property(name="BasicActions_OutputPin194", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction193", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier202: BinaryAssociation = BinaryAssociation(
    name="classifier202",
    ends={
        Property(name="CompleteActions_xmof_EClassifier203", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result204: BinaryAssociation = BinaryAssociation(
    name="result204",
    ends={
        Property(name="BasicActions_OutputPin206", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction205", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object207: BinaryAssociation = BinaryAssociation(
    name="object207",
    ends={
        Property(name="BasicActions_InputPin209", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction208", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier210: BinaryAssociation = BinaryAssociation(
    name="oldClassifier210",
    ends={
        Property(name="CompleteActions_xmof_EClassifier211", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
newClassifier215: BinaryAssociation = BinaryAssociation(
    name="newClassifier215",
    ends={
        Property(name="CompleteActions_xmof_EClassifier217", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction216", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
result218: BinaryAssociation = BinaryAssociation(
    name="result218",
    ends={
        Property(name="BasicActions_OutputPin219", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger220: BinaryAssociation = BinaryAssociation(
    name="trigger220",
    ends={
        Property(name="Communications_Trigger", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction221", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output222: BinaryAssociation = BinaryAssociation(
    name="output222",
    ends={
        Property(name="BasicActions_OutputPin223", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context224: BinaryAssociation = BinaryAssociation(
    name="context224",
    ends={
        Property(name="BasicActions_xmof_EClassifier", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action225", type=BasicActions_xmof_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
input226: BinaryAssociation = BinaryAssociation(
    name="input226",
    ends={
        Property(name="BasicActions_InputPin228", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action227", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
object212: BinaryAssociation = BinaryAssociation(
    name="object212",
    ends={
        Property(name="BasicActions_InputPin214", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction213", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result229: BinaryAssociation = BinaryAssociation(
    name="result229",
    ends={
        Property(name="BasicActions_OutputPin230", type=xmof_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument231: BinaryAssociation = BinaryAssociation(
    name="argument231",
    ends={
        Property(name="BasicActions_InputPin232", type=xmof_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target233: BinaryAssociation = BinaryAssociation(
    name="target233",
    ends={
        Property(name="BasicActions_InputPin234", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
behavior238: BinaryAssociation = BinaryAssociation(
    name="behavior238",
    ends={
        Property(name="BasicBehaviors_Behavior239", type=xmof_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
signal235: BinaryAssociation = BinaryAssociation(
    name="signal235",
    ends={
        Property(name="Communications_Signal237", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction236", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
operation240: BinaryAssociation = BinaryAssociation(
    name="operation240",
    ends={
        Property(name="Kernel_BehavioredEOperation", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1))
    }
)
target241: BinaryAssociation = BinaryAssociation(
    name="target241",
    ends={
        Property(name="BasicActions_InputPin243", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction242", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type244: BinaryAssociation = BinaryAssociation(
    name="type244",
    ends={
        Property(name="Kernel_PrimitiveType", type=xmof_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
values252: BinaryAssociation = BinaryAssociation(
    name="values252",
    ends={
        Property(name="Kernel_Value", type=xmof_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValue253", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal245: BinaryAssociation = BinaryAssociation(
    name="literal245",
    ends={
        Property(name="Kernel_xmof_EEnumLiteral246", type=xmof_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumerationValue", type=Kernel_xmof_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type247: BinaryAssociation = BinaryAssociation(
    name="type247",
    ends={
        Property(name="Kernel_xmof_EEnum", type=xmof_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumerationValue248", type=Kernel_xmof_EEnum, multiplicity=Multiplicity(1, 1))
    }
)
eObject249: BinaryAssociation = BinaryAssociation(
    name="eObject249",
    ends={
        Property(name="Kernel_xmof_EObject", type=xmof_Kernel_ObjectValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_ObjectValue", type=Kernel_xmof_EObject, multiplicity=Multiplicity(1, 1))
    }
)
parameter250: BinaryAssociation = BinaryAssociation(
    name="parameter250",
    ends={
        Property(name="Kernel_DirectedParameter251", type=xmof_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValue", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
parameterValues254: BinaryAssociation = BinaryAssociation(
    name="parameterValues254",
    ends={
        Property(name="BasicBehaviors_ParameterValue", type=xmof_BasicBehaviors_ParameterValueDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValueDefinition", type=BasicBehaviors_ParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_xmof_BasicBehaviors_Behavior_BehavioredEClass = Generalization(general=BehavioredEClass, specific=xmof_BasicBehaviors_Behavior)
gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=xmof_BasicBehaviors_OpaqueBehavior)
gen_xmof_Communications_Trigger_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Trigger)
gen_xmof_Communications_Event_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Event)
gen_xmof_Communications_Signal_EClassifier = Generalization(general=EClassifier, specific=xmof_Communications_Signal)
gen_xmof_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=xmof_Communications_SignalEvent)
gen_xmof_Communications_MessageEvent_Event = Generalization(general=Event, specific=xmof_Communications_MessageEvent)
gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier = Generalization(general=EClassifier, specific=xmof_BasicBehaviors_BehavioredClassifier)
gen_xmof_Communications_Reception_BehavioredEOperation = Generalization(general=BehavioredEOperation, specific=xmof_Communications_Reception)
gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=xmof_BasicBehaviors_FunctionBehavior)
gen_xmof_Kernel_BehavioredEClass_EClass = Generalization(general=EClass, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier = Generalization(general=BasicBehaviors_BehavioredClassifier, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_DirectedParameter_EParameter = Generalization(general=EParameter, specific=xmof_Kernel_DirectedParameter)
gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification = Generalization(general=InstanceSpecification, specific=xmof_Kernel_EEnumLiteralSpecification)
gen_xmof_Kernel_EnumValue_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_EnumValue)
gen_xmof_Kernel_ValueSpecification_ETypedElement = Generalization(general=ETypedElement, specific=xmof_Kernel_ValueSpecification)
gen_xmof_Kernel_InstanceSpecification_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Kernel_InstanceSpecification)
gen_xmof_Kernel_BehavioredEOperation_EOperation = Generalization(general=EOperation, specific=xmof_Kernel_BehavioredEOperation)
gen_xmof_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_InstanceValue)
gen_xmof_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralBoolean)
gen_xmof_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_LiteralSpecification)
gen_xmof_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralInteger)
gen_xmof_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralNull)
gen_xmof_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralString)
gen_xmof_Kernel_Slot_EModelElement = Generalization(general=EModelElement, specific=xmof_Kernel_Slot)
gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=xmof_IntermediateActivities_ObjectFlow)
gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityEdge)
gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralUnlimitedNatural)
gen_xmof_Kernel_PrimitiveType_EDataType = Generalization(general=EDataType, specific=xmof_Kernel_PrimitiveType)
gen_xmof_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_MergeNode)
gen_xmof_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=xmof_IntermediateActivities_Activity)
gen_xmof_IntermediateActivities_ActivityNode_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityNode)
gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode = Generalization(general=IntermediateActivities_ActivityNode, specific=xmof_IntermediateActivities_ObjectNode)
gen_xmof_IntermediateActivities_ObjectNode_ETypedElement = Generalization(general=ETypedElement, specific=xmof_IntermediateActivities_ObjectNode)
gen_xmof_IntermediateActivities_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=xmof_IntermediateActivities_ControlNode)
gen_xmof_IntermediateActivities_JoinNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_JoinNode)
gen_xmof_IntermediateActivities_InitialNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_InitialNode)
gen_xmof_IntermediateActivities_FinalNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_FinalNode)
gen_xmof_IntermediateActivities_ForkNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_ForkNode)
gen_xmof_IntermediateActivities_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=xmof_IntermediateActivities_ControlFlow)
gen_xmof_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_DecisionNode)
gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=xmof_IntermediateActivities_ActivityFinalNode)
gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=xmof_IntermediateActivities_ActivityParameterNode)
gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_CompleteStructuredActivities_LoopNode)
gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=xmof_CompleteStructuredActivities_ExecutableNode)
gen_xmof_CompleteStructuredActivities_Clause_EModelElement = Generalization(general=EModelElement, specific=xmof_CompleteStructuredActivities_Clause)
gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_CompleteStructuredActivities_ConditionalNode)
gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=xmof_CompleteStructuredActivities_StructuredActivityNode)
gen_xmof_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_StructuralFeatureAction)
gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=xmof_ExtraStructuredActivities_ExpansionNode)
gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_ExtraStructuredActivities_ExpansionRegion)
gen_xmof_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_WriteLinkAction)
gen_xmof_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_LinkAction)
gen_xmof_IntermediateActions_LinkEndData_EModelElement = Generalization(general=EModelElement, specific=xmof_IntermediateActions_LinkEndData)
gen_xmof_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_TestIdentityAction)
gen_xmof_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ValueSpecificationAction)
gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_xmof_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_ReadLinkAction)
gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_WriteStructuralFeatureAction)
gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndCreationData)
gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndDestructionData)
gen_xmof_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ClearAssociationAction)
gen_xmof_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ReadSelfAction)
gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ReadStructuralFeatureAction)
gen_xmof_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_CreateObjectAction)
gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_DestroyLinkAction)
gen_xmof_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_DestroyObjectAction)
gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ClearStructuralFeatureAction)
gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_CreateLinkAction)
gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_CompleteActions_StartObjectBehaviorAction)
gen_xmof_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReduceAction)
gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_AddStructuralFeatureValueAction)
gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_StartClassifierBehaviorAction)
gen_xmof_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadExtentAction)
gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadIsClassifiedObjectAction)
gen_xmof_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReclassifyObjectAction)
gen_xmof_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_InputPin)
gen_xmof_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_AcceptEventAction)
gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_Pin_ETypedElement = Generalization(general=ETypedElement, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_CallAction)
gen_xmof_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=xmof_BasicActions_Action)
gen_xmof_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=xmof_BasicActions_InvocationAction)
gen_xmof_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_SendSignalAction)
gen_xmof_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=xmof_Kernel_EnumerationValue)
gen_xmof_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallBehaviorAction)
gen_xmof_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallOperationAction)
gen_xmof_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_OutputPin)
gen_xmof_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=xmof_Kernel_PrimitiveValue)
gen_xmof_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_StringValue)
gen_xmof_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_IntegerValue)
gen_xmof_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_BooleanValue)
gen_xmof_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=xmof_Kernel_Value)
gen_xmof_Kernel_ObjectValue_Value = Generalization(general=Value, specific=xmof_Kernel_ObjectValue)

# Domain Model
domain_model = DomainModel(
    name="xmof",
    types={xmof_BasicBehaviors_Behavior, BehavioredEClass, Kernel_BehavioredEOperation, xmof_BasicBehaviors_OpaqueBehavior, Behavior, xmof_Communications_Trigger, ENamedElement, Communications_Event, xmof_Communications_Event, xmof_Communications_Signal, Communications_xmof_EAttribute, Kernel_DirectedParameter, xmof_Communications_SignalEvent, MessageEvent, BasicBehaviors_BehavioredClassifier, Communications_Signal, xmof_Communications_MessageEvent, Event, xmof_BasicBehaviors_BehavioredClassifier, xmof_Communications_Reception, EClassifier, BehavioredEOperation, BasicBehaviors_Behavior, xmof_BasicBehaviors_FunctionBehavior, OpaqueBehavior, xmof_Kernel_BehavioredEClass, EClass, xmof_Kernel_DirectedParameter, EParameter, xmof_Kernel_EEnumLiteralSpecification, InstanceSpecification, Kernel_xmof_EEnumLiteral, xmof_Kernel_EnumValue, ValueSpecification, Kernel_EEnumLiteralSpecification, xmof_Kernel_ValueSpecification, ETypedElement, xmof_Kernel_InstanceSpecification, Kernel_xmof_EClassifier, Kernel_Slot, xmof_Kernel_BehavioredEOperation, EOperation, Kernel_InstanceSpecification, xmof_Kernel_InstanceValue, xmof_Kernel_LiteralBoolean, LiteralSpecification, xmof_Kernel_LiteralSpecification, xmof_Kernel_LiteralInteger, xmof_Kernel_LiteralNull, xmof_Kernel_LiteralString, xmof_Kernel_Slot, EModelElement, Kernel_xmof_EStructuralFeature, Kernel_ValueSpecification, ActivityEdge, xmof_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, xmof_Kernel_LiteralUnlimitedNatural, xmof_Kernel_PrimitiveType, EDataType, xmof_IntermediateActivities_ObjectFlow, xmof_IntermediateActivities_MergeNode, ControlNode, xmof_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, xmof_IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, xmof_IntermediateActivities_ObjectNode, xmof_IntermediateActivities_ControlNode, ActivityNode, xmof_IntermediateActivities_JoinNode, xmof_IntermediateActivities_InitialNode, xmof_IntermediateActivities_FinalNode, xmof_IntermediateActivities_ForkNode, xmof_IntermediateActivities_ControlFlow, xmof_IntermediateActivities_DecisionNode, IntermediateActivities_ObjectFlow, xmof_IntermediateActivities_ActivityFinalNode, FinalNode, xmof_IntermediateActivities_ActivityParameterNode, ObjectNode, xmof_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, xmof_CompleteStructuredActivities_ExecutableNode, xmof_CompleteStructuredActivities_Clause, CompleteStructuredActivities_Clause, xmof_CompleteStructuredActivities_ConditionalNode, xmof_CompleteStructuredActivities_StructuredActivityNode, Action, xmof_IntermediateActions_StructuralFeatureAction, xmof_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, xmof_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, xmof_IntermediateActions_WriteLinkAction, LinkAction, xmof_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, IntermediateActions_xmof_EStructuralFeature, xmof_IntermediateActions_LinkEndData, xmof_IntermediateActions_TestIdentityAction, xmof_IntermediateActions_ValueSpecificationAction, xmof_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, xmof_IntermediateActions_ReadLinkAction, IntermediateActions_xmof_EReference, xmof_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, xmof_IntermediateActions_LinkEndCreationData, LinkEndData, xmof_IntermediateActions_LinkEndDestructionData, xmof_IntermediateActions_ClearAssociationAction, xmof_IntermediateActions_ReadSelfAction, xmof_IntermediateActions_ReadStructuralFeatureAction, xmof_IntermediateActions_CreateObjectAction, IntermediateActions_xmof_EClassifier, xmof_IntermediateActions_DestroyLinkAction, xmof_IntermediateActions_DestroyObjectAction, xmof_IntermediateActions_ClearStructuralFeatureAction, xmof_IntermediateActions_CreateLinkAction, WriteLinkAction, xmof_CompleteActions_StartObjectBehaviorAction, CallAction, xmof_CompleteActions_ReduceAction, xmof_IntermediateActions_AddStructuralFeatureValueAction, xmof_CompleteActions_StartClassifierBehaviorAction, xmof_CompleteActions_ReadExtentAction, CompleteActions_xmof_EClassifier, xmof_CompleteActions_ReadIsClassifiedObjectAction, xmof_CompleteActions_ReclassifyObjectAction, xmof_CompleteActions_AcceptEventAction, xmof_BasicActions_Pin, IntermediateActivities_ObjectNode, xmof_BasicActions_CallAction, InvocationAction, Communications_Trigger, xmof_BasicActions_Action, ExecutableNode, BasicActions_xmof_EClassifier, xmof_BasicActions_InputPin, Pin, xmof_BasicActions_CallBehaviorAction, xmof_BasicActions_InvocationAction, xmof_BasicActions_SendSignalAction, xmof_Kernel_EnumerationValue, xmof_BasicActions_CallOperationAction, xmof_BasicActions_OutputPin, xmof_Kernel_PrimitiveValue, Value, Kernel_PrimitiveType, xmof_Kernel_StringValue, PrimitiveValue, xmof_Kernel_IntegerValue, Kernel_xmof_EEnum, xmof_Kernel_BooleanValue, xmof_Kernel_Value, SemanticVisitor, xmof_Kernel_ObjectValue, Kernel_xmof_EObject, xmof_LociL1_SemanticVisitor, xmof_BasicBehaviors_ParameterValue, Kernel_Value, xmof_BasicBehaviors_ParameterValueDefinition, BasicBehaviors_ParameterValue, CallConcurrencyKind, ParameterDirectionKind, ExpansionKind},
    associations={specification0, event8, ownedAttribute9, ownedParameter1, context2, signal10, ownedBehavior4, classifierBehavior5, eEnumLiteral15, eEnumLiteralSpecification16, classifier17, slot18, signal11, method13, owningInstance24, instance27, definingFeature21, value22, activity28, source30, guard39, node41, edge44, inStructuredNode47, activity50, outgoing53, target33, incoming56, inStructuredNode36, bodyOutput68, decisionInput59, decisionInputFlow61, parameter63, decider65, test66, successorClause93, loopVariableInput71, bodyPart73, result76, loopVariable79, setupPart82, test85, body87, predecessorClause90, decider96, bodyOutput99, clause102, result103, node106, edge109, structuredNodeOutput112, structuredNodeInput114, outputElement126, regionAsOutput117, regionAsInput120, inputElement123, result143, endData146, structuralFeature129, inputValue147, object130, value150, second133, result135, first138, value141, value154, result156, removeAt159, end152, result165, insertAt167, destroyAt169, result161, result163, result178, classifier180, target182, association171, object173, result176, object188, reducer190, insertAt184, object186, collection195, result198, classifier200, result192, classifier202, result204, object207, oldClassifier210, newClassifier215, result218, trigger220, output222, context224, input226, object212, result229, argument231, target233, behavior238, signal235, operation240, target241, type244, values252, literal245, type247, eObject249, parameter250, parameterValues254},
    generalizations={gen_xmof_BasicBehaviors_Behavior_BehavioredEClass, gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior, gen_xmof_Communications_Trigger_ENamedElement, gen_xmof_Communications_Event_ENamedElement, gen_xmof_Communications_Signal_EClassifier, gen_xmof_Communications_SignalEvent_MessageEvent, gen_xmof_Communications_MessageEvent_Event, gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier, gen_xmof_Communications_Reception_BehavioredEOperation, gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_xmof_Kernel_BehavioredEClass_EClass, gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier, gen_xmof_Kernel_DirectedParameter_EParameter, gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification, gen_xmof_Kernel_EnumValue_ValueSpecification, gen_xmof_Kernel_ValueSpecification_ETypedElement, gen_xmof_Kernel_InstanceSpecification_ENamedElement, gen_xmof_Kernel_BehavioredEOperation_EOperation, gen_xmof_Kernel_InstanceValue_ValueSpecification, gen_xmof_Kernel_LiteralBoolean_LiteralSpecification, gen_xmof_Kernel_LiteralSpecification_ValueSpecification, gen_xmof_Kernel_LiteralInteger_LiteralSpecification, gen_xmof_Kernel_LiteralNull_LiteralSpecification, gen_xmof_Kernel_LiteralString_LiteralSpecification, gen_xmof_Kernel_Slot_EModelElement, gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge, gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement, gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_xmof_Kernel_PrimitiveType_EDataType, gen_xmof_IntermediateActivities_MergeNode_ControlNode, gen_xmof_IntermediateActivities_Activity_Behavior, gen_xmof_IntermediateActivities_ActivityNode_ENamedElement, gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_xmof_IntermediateActivities_ObjectNode_ETypedElement, gen_xmof_IntermediateActivities_ControlNode_ActivityNode, gen_xmof_IntermediateActivities_JoinNode_ControlNode, gen_xmof_IntermediateActivities_InitialNode_ControlNode, gen_xmof_IntermediateActivities_FinalNode_ControlNode, gen_xmof_IntermediateActivities_ForkNode_ControlNode, gen_xmof_IntermediateActivities_ControlFlow_ActivityEdge, gen_xmof_IntermediateActivities_DecisionNode_ControlNode, gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode, gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_xmof_CompleteStructuredActivities_Clause_EModelElement, gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action, gen_xmof_IntermediateActions_StructuralFeatureAction_Action, gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_xmof_IntermediateActions_WriteLinkAction_LinkAction, gen_xmof_IntermediateActions_LinkAction_Action, gen_xmof_IntermediateActions_LinkEndData_EModelElement, gen_xmof_IntermediateActions_TestIdentityAction_Action, gen_xmof_IntermediateActions_ValueSpecificationAction_Action, gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_IntermediateActions_ReadLinkAction_LinkAction, gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData, gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_xmof_IntermediateActions_ClearAssociationAction_Action, gen_xmof_IntermediateActions_ReadSelfAction_Action, gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_CreateObjectAction_Action, gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_DestroyObjectAction_Action, gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction, gen_xmof_CompleteActions_ReduceAction_Action, gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action, gen_xmof_CompleteActions_ReadExtentAction_Action, gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_xmof_CompleteActions_ReclassifyObjectAction_Action, gen_xmof_BasicActions_InputPin_Pin, gen_xmof_CompleteActions_AcceptEventAction_Action, gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_xmof_BasicActions_Pin_ETypedElement, gen_xmof_BasicActions_CallAction_InvocationAction, gen_xmof_BasicActions_Action_ExecutableNode, gen_xmof_BasicActions_InvocationAction_Action, gen_xmof_BasicActions_SendSignalAction_InvocationAction, gen_xmof_Kernel_EnumerationValue_Value, gen_xmof_BasicActions_CallBehaviorAction_CallAction, gen_xmof_BasicActions_CallOperationAction_CallAction, gen_xmof_BasicActions_OutputPin_Pin, gen_xmof_Kernel_PrimitiveValue_Value, gen_xmof_Kernel_StringValue_PrimitiveValue, gen_xmof_Kernel_IntegerValue_PrimitiveValue, gen_xmof_Kernel_BooleanValue_PrimitiveValue, gen_xmof_Kernel_Value_SemanticVisitor, gen_xmof_Kernel_ObjectValue_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)