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
xmof_BasicBehaviors_OpaqueBehavior = Class(name="xmof::BasicBehaviors::OpaqueBehavior")
Behavior = Class(name="Behavior")
xmof_BasicBehaviors_Behavior = Class(name="xmof::BasicBehaviors::Behavior", is_abstract=True)
BehavioredEClass = Class(name="BehavioredEClass")
Kernel_BehavioredEOperation = Class(name="Kernel::BehavioredEOperation")
Kernel_DirectedParameter = Class(name="Kernel::DirectedParameter")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors::BehavioredClassifier")
xmof_BasicBehaviors_BehavioredClassifier = Class(name="xmof::BasicBehaviors::BehavioredClassifier", is_abstract=True)
EClassifier = Class(name="EClassifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors::Behavior")
xmof_BasicBehaviors_FunctionBehavior = Class(name="xmof::BasicBehaviors::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
xmof_Communications_Trigger = Class(name="xmof::Communications::Trigger")
ENamedElement = Class(name="ENamedElement")
Communications_Event = Class(name="Communications::Event")
xmof_Communications_Event = Class(name="xmof::Communications::Event", is_abstract=True)
xmof_Communications_Signal = Class(name="xmof::Communications::Signal")
Communications_xmof_EAttribute = Class(name="Communications::xmof::EAttribute")
xmof_Communications_SignalEvent = Class(name="xmof::Communications::SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications::Signal")
xmof_Communications_MessageEvent = Class(name="xmof::Communications::MessageEvent", is_abstract=True)
Event = Class(name="Event")
xmof_Communications_Reception = Class(name="xmof::Communications::Reception")
BehavioredEOperation = Class(name="BehavioredEOperation")
xmof_Kernel_BehavioredEOperation = Class(name="xmof::Kernel::BehavioredEOperation")
EOperation = Class(name="EOperation")
xmof_Kernel_BehavioredEClass = Class(name="xmof::Kernel::BehavioredEClass")
EClass = Class(name="EClass")
xmof_Kernel_MainEClass = Class(name="xmof::Kernel::MainEClass")
xmof_Kernel_DirectedParameter = Class(name="xmof::Kernel::DirectedParameter")
EParameter = Class(name="EParameter")
xmof_Kernel_EEnumLiteralSpecification = Class(name="xmof::Kernel::EEnumLiteralSpecification")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_xmof_EEnumLiteral = Class(name="Kernel::xmof::EEnumLiteral")
xmof_Kernel_ValueSpecification = Class(name="xmof::Kernel::ValueSpecification", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
xmof_Kernel_InstanceSpecification = Class(name="xmof::Kernel::InstanceSpecification")
Kernel_xmof_EClassifier = Class(name="Kernel::xmof::EClassifier")
Kernel_Slot = Class(name="Kernel::Slot")
xmof_Kernel_Slot = Class(name="xmof::Kernel::Slot")
EModelElement = Class(name="EModelElement")
Kernel_xmof_EStructuralFeature = Class(name="Kernel::xmof::EStructuralFeature")
Kernel_ValueSpecification = Class(name="Kernel::ValueSpecification")
Kernel_InstanceSpecification = Class(name="Kernel::InstanceSpecification")
xmof_Kernel_InstanceValue = Class(name="xmof::Kernel::InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
xmof_Kernel_LiteralBoolean = Class(name="xmof::Kernel::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
xmof_Kernel_LiteralSpecification = Class(name="xmof::Kernel::LiteralSpecification", is_abstract=True)
xmof_Kernel_LiteralInteger = Class(name="xmof::Kernel::LiteralInteger")
xmof_Kernel_LiteralNull = Class(name="xmof::Kernel::LiteralNull")
xmof_Kernel_LiteralString = Class(name="xmof::Kernel::LiteralString")
xmof_Kernel_LiteralUnlimitedNatural = Class(name="xmof::Kernel::LiteralUnlimitedNatural")
xmof_Kernel_PrimitiveType = Class(name="xmof::Kernel::PrimitiveType")
EDataType = Class(name="EDataType")
xmof_IntermediateActivities_ObjectFlow = Class(name="xmof::IntermediateActivities::ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
xmof_IntermediateActivities_ActivityEdge = Class(name="xmof::IntermediateActivities::ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities::Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities::ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities::StructuredActivityNode")
xmof_IntermediateActivities_Activity = Class(name="xmof::IntermediateActivities::Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities::ActivityEdge")
xmof_IntermediateActivities_ActivityNode = Class(name="xmof::IntermediateActivities::ActivityNode", is_abstract=True)
xmof_IntermediateActivities_ObjectNode = Class(name="xmof::IntermediateActivities::ObjectNode", is_abstract=True)
xmof_IntermediateActivities_MergeNode = Class(name="xmof::IntermediateActivities::MergeNode")
ControlNode = Class(name="ControlNode")
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
xmof_ExtraStructuredActivities_ExpansionNode = Class(name="xmof::ExtraStructuredActivities::ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities::ExpansionRegion")
xmof_ExtraStructuredActivities_ExpansionRegion = Class(name="xmof::ExtraStructuredActivities::ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities::ExpansionNode")
xmof_IntermediateActions_StructuralFeatureAction = Class(name="xmof::IntermediateActions::StructuralFeatureAction", is_abstract=True)
IntermediateActions_xmof_EStructuralFeature = Class(name="IntermediateActions::xmof::EStructuralFeature")
xmof_IntermediateActions_TestIdentityAction = Class(name="xmof::IntermediateActions::TestIdentityAction")
xmof_IntermediateActions_ValueSpecificationAction = Class(name="xmof::IntermediateActions::ValueSpecificationAction")
xmof_IntermediateActions_WriteLinkAction = Class(name="xmof::IntermediateActions::WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
xmof_IntermediateActions_LinkAction = Class(name="xmof::IntermediateActions::LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions::LinkEndData")
xmof_IntermediateActions_LinkEndData = Class(name="xmof::IntermediateActions::LinkEndData")
xmof_IntermediateActions_WriteStructuralFeatureAction = Class(name="xmof::IntermediateActions::WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
xmof_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="xmof::IntermediateActions::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
xmof_IntermediateActions_ReadLinkAction = Class(name="xmof::IntermediateActions::ReadLinkAction")
xmof_IntermediateActions_ReadSelfAction = Class(name="xmof::IntermediateActions::ReadSelfAction")
IntermediateActions_xmof_EReference = Class(name="IntermediateActions::xmof::EReference")
xmof_IntermediateActions_ReadStructuralFeatureAction = Class(name="xmof::IntermediateActions::ReadStructuralFeatureAction")
xmof_IntermediateActions_LinkEndCreationData = Class(name="xmof::IntermediateActions::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
xmof_IntermediateActions_LinkEndDestructionData = Class(name="xmof::IntermediateActions::LinkEndDestructionData")
xmof_IntermediateActions_ClearAssociationAction = Class(name="xmof::IntermediateActions::ClearAssociationAction")
xmof_IntermediateActions_ClearStructuralFeatureAction = Class(name="xmof::IntermediateActions::ClearStructuralFeatureAction")
xmof_IntermediateActions_CreateLinkAction = Class(name="xmof::IntermediateActions::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
xmof_IntermediateActions_CreateObjectAction = Class(name="xmof::IntermediateActions::CreateObjectAction")
IntermediateActions_xmof_EClassifier = Class(name="IntermediateActions::xmof::EClassifier")
xmof_IntermediateActions_DestroyLinkAction = Class(name="xmof::IntermediateActions::DestroyLinkAction")
xmof_IntermediateActions_DestroyObjectAction = Class(name="xmof::IntermediateActions::DestroyObjectAction")
xmof_IntermediateActions_AddStructuralFeatureValueAction = Class(name="xmof::IntermediateActions::AddStructuralFeatureValueAction")
xmof_CompleteActions_StartClassifierBehaviorAction = Class(name="xmof::CompleteActions::StartClassifierBehaviorAction")
xmof_CompleteActions_StartObjectBehaviorAction = Class(name="xmof::CompleteActions::StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
xmof_CompleteActions_ReduceAction = Class(name="xmof::CompleteActions::ReduceAction")
xmof_CompleteActions_ReadExtentAction = Class(name="xmof::CompleteActions::ReadExtentAction")
CompleteActions_xmof_EClassifier = Class(name="CompleteActions::xmof::EClassifier")
xmof_CompleteActions_ReadIsClassifiedObjectAction = Class(name="xmof::CompleteActions::ReadIsClassifiedObjectAction")
xmof_CompleteActions_ReclassifyObjectAction = Class(name="xmof::CompleteActions::ReclassifyObjectAction")
xmof_CompleteActions_AcceptEventAction = Class(name="xmof::CompleteActions::AcceptEventAction")
Communications_Trigger = Class(name="Communications::Trigger")
xmof_BasicActions_Action = Class(name="xmof::BasicActions::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
BasicActions_xmof_EClassifier = Class(name="BasicActions::xmof::EClassifier")
xmof_BasicActions_InputPin = Class(name="xmof::BasicActions::InputPin")
Pin = Class(name="Pin")
xmof_BasicActions_Pin = Class(name="xmof::BasicActions::Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities::ObjectNode")
xmof_BasicActions_CallAction = Class(name="xmof::BasicActions::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
xmof_BasicActions_InvocationAction = Class(name="xmof::BasicActions::InvocationAction", is_abstract=True)
xmof_BasicActions_SendSignalAction = Class(name="xmof::BasicActions::SendSignalAction")
xmof_BasicActions_CallBehaviorAction = Class(name="xmof::BasicActions::CallBehaviorAction")
xmof_BasicActions_CallOperationAction = Class(name="xmof::BasicActions::CallOperationAction")
xmof_BasicActions_OutputPin = Class(name="xmof::BasicActions::OutputPin")

# xmof_BasicBehaviors_OpaqueBehavior class attributes and methods
xmof_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior.attributes={xmof_BasicBehaviors_OpaqueBehavior_language, xmof_BasicBehaviors_OpaqueBehavior_body}

# Behavior class attributes and methods

# xmof_BasicBehaviors_Behavior class attributes and methods
xmof_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
xmof_BasicBehaviors_Behavior.attributes={xmof_BasicBehaviors_Behavior_reentrant}

# BehavioredEClass class attributes and methods

# Kernel_BehavioredEOperation class attributes and methods

# Kernel_DirectedParameter class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# xmof_BasicBehaviors_BehavioredClassifier class attributes and methods

# EClassifier class attributes and methods

# BasicBehaviors_Behavior class attributes and methods

# xmof_BasicBehaviors_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# xmof_Communications_Trigger class attributes and methods

# ENamedElement class attributes and methods

# Communications_Event class attributes and methods

# xmof_Communications_Event class attributes and methods

# xmof_Communications_Signal class attributes and methods

# Communications_xmof_EAttribute class attributes and methods

# xmof_Communications_SignalEvent class attributes and methods

# MessageEvent class attributes and methods

# Communications_Signal class attributes and methods

# xmof_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# xmof_Communications_Reception class attributes and methods

# BehavioredEOperation class attributes and methods

# xmof_Kernel_BehavioredEOperation class attributes and methods

# EOperation class attributes and methods

# xmof_Kernel_BehavioredEClass class attributes and methods

# EClass class attributes and methods

# xmof_Kernel_MainEClass class attributes and methods

# xmof_Kernel_DirectedParameter class attributes and methods
xmof_Kernel_DirectedParameter_direction: Property = Property(name="direction", type=StringType)
xmof_Kernel_DirectedParameter.attributes={xmof_Kernel_DirectedParameter_direction}

# EParameter class attributes and methods

# xmof_Kernel_EEnumLiteralSpecification class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_xmof_EEnumLiteral class attributes and methods

# xmof_Kernel_ValueSpecification class attributes and methods

# ETypedElement class attributes and methods

# xmof_Kernel_InstanceSpecification class attributes and methods

# Kernel_xmof_EClassifier class attributes and methods

# Kernel_Slot class attributes and methods

# xmof_Kernel_Slot class attributes and methods

# EModelElement class attributes and methods

# Kernel_xmof_EStructuralFeature class attributes and methods

# Kernel_ValueSpecification class attributes and methods

# Kernel_InstanceSpecification class attributes and methods

# xmof_Kernel_InstanceValue class attributes and methods

# ValueSpecification class attributes and methods

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

# xmof_Kernel_LiteralUnlimitedNatural class attributes and methods
xmof_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
xmof_Kernel_LiteralUnlimitedNatural.attributes={xmof_Kernel_LiteralUnlimitedNatural_value}

# xmof_Kernel_PrimitiveType class attributes and methods

# EDataType class attributes and methods

# xmof_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# xmof_IntermediateActivities_Activity class attributes and methods
xmof_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
xmof_IntermediateActivities_Activity.attributes={xmof_IntermediateActivities_Activity_readOnly}

# IntermediateActivities_ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityNode class attributes and methods

# xmof_IntermediateActivities_ObjectNode class attributes and methods

# xmof_IntermediateActivities_MergeNode class attributes and methods

# ControlNode class attributes and methods

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
xmof_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode.attributes={xmof_CompleteStructuredActivities_ConditionalNode_determinate, xmof_CompleteStructuredActivities_ConditionalNode_assured}

# xmof_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
xmof_CompleteStructuredActivities_StructuredActivityNode.attributes={xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionRegion class attributes and methods
xmof_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
xmof_ExtraStructuredActivities_ExpansionRegion.attributes={xmof_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# xmof_IntermediateActions_StructuralFeatureAction class attributes and methods

# IntermediateActions_xmof_EStructuralFeature class attributes and methods

# xmof_IntermediateActions_TestIdentityAction class attributes and methods

# xmof_IntermediateActions_ValueSpecificationAction class attributes and methods

# xmof_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# xmof_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_ReadLinkAction class attributes and methods

# xmof_IntermediateActions_ReadSelfAction class attributes and methods

# IntermediateActions_xmof_EReference class attributes and methods

# xmof_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_LinkEndCreationData class attributes and methods
xmof_IntermediateActions_LinkEndCreationData_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_IntermediateActions_LinkEndCreationData.attributes={xmof_IntermediateActions_LinkEndCreationData_replaceAll}

# LinkEndData class attributes and methods

# xmof_IntermediateActions_LinkEndDestructionData class attributes and methods
xmof_IntermediateActions_LinkEndDestructionData_destroyDuplicates: Property = Property(name="destroyDuplicates", type=BooleanType)
xmof_IntermediateActions_LinkEndDestructionData.attributes={xmof_IntermediateActions_LinkEndDestructionData_destroyDuplicates}

# xmof_IntermediateActions_ClearAssociationAction class attributes and methods

# xmof_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# xmof_IntermediateActions_CreateObjectAction class attributes and methods

# IntermediateActions_xmof_EClassifier class attributes and methods

# xmof_IntermediateActions_DestroyLinkAction class attributes and methods

# xmof_IntermediateActions_DestroyObjectAction class attributes and methods
xmof_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
xmof_IntermediateActions_DestroyObjectAction.attributes={xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects, xmof_IntermediateActions_DestroyObjectAction_destroyLinks}

# xmof_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_IntermediateActions_AddStructuralFeatureValueAction.attributes={xmof_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# xmof_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# xmof_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# xmof_CompleteActions_ReduceAction class attributes and methods
xmof_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
xmof_CompleteActions_ReduceAction.attributes={xmof_CompleteActions_ReduceAction_ordered}

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

# Communications_Trigger class attributes and methods

# xmof_BasicActions_Action class attributes and methods
xmof_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
xmof_BasicActions_Action.attributes={xmof_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# BasicActions_xmof_EClassifier class attributes and methods

# xmof_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# xmof_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# xmof_BasicActions_CallAction class attributes and methods
xmof_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
xmof_BasicActions_CallAction.attributes={xmof_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# xmof_BasicActions_InvocationAction class attributes and methods

# xmof_BasicActions_SendSignalAction class attributes and methods

# xmof_BasicActions_CallBehaviorAction class attributes and methods

# xmof_BasicActions_CallOperationAction class attributes and methods

# xmof_BasicActions_OutputPin class attributes and methods

# Relationships
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="Syntax", type=xmof_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(0, 1))
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
signal10: BinaryAssociation = BinaryAssociation(
    name="signal10",
    ends={
        Property(name="Communications_Signal", type=xmof_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Communications_SignalEvent", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
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
eEnumLiteral15: BinaryAssociation = BinaryAssociation(
    name="eEnumLiteral15",
    ends={
        Property(name="Kernel_xmof_EEnumLiteral", type=xmof_Kernel_EEnumLiteralSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EEnumLiteralSpecification", type=Kernel_xmof_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
classifier16: BinaryAssociation = BinaryAssociation(
    name="classifier16",
    ends={
        Property(name="Kernel_xmof_EClassifier", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceSpecification", type=Kernel_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot17: BinaryAssociation = BinaryAssociation(
    name="slot17",
    ends={
        Property(name="Syntax19", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes18", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature20: BinaryAssociation = BinaryAssociation(
    name="definingFeature20",
    ends={
        Property(name="Kernel_xmof_EStructuralFeature", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot", type=Kernel_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="Kernel_ValueSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot22", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance23: BinaryAssociation = BinaryAssociation(
    name="owningInstance23",
    ends={
        Property(name="Syntax25", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes24", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance26: BinaryAssociation = BinaryAssociation(
    name="instance26",
    ends={
        Property(name="Kernel_InstanceSpecification", type=xmof_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
activity27: BinaryAssociation = BinaryAssociation(
    name="activity27",
    ends={
        Property(name="Syntax28", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="Syntax31", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities30", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target32: BinaryAssociation = BinaryAssociation(
    name="target32",
    ends={
        Property(name="Syntax34", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities33", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode35: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode35",
    ends={
        Property(name="Syntax37", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities36", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
guard38: BinaryAssociation = BinaryAssociation(
    name="guard38",
    ends={
        Property(name="Kernel_ValueSpecification39", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node40: BinaryAssociation = BinaryAssociation(
    name="node40",
    ends={
        Property(name="Syntax42", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities41", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge43: BinaryAssociation = BinaryAssociation(
    name="edge43",
    ends={
        Property(name="Syntax45", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities44", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode46: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode46",
    ends={
        Property(name="Syntax48", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities47", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity49: BinaryAssociation = BinaryAssociation(
    name="activity49",
    ends={
        Property(name="Syntax51", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities50", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing52: BinaryAssociation = BinaryAssociation(
    name="outgoing52",
    ends={
        Property(name="Syntax54", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities53", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming55: BinaryAssociation = BinaryAssociation(
    name="incoming55",
    ends={
        Property(name="Syntax57", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities56", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput58: BinaryAssociation = BinaryAssociation(
    name="decisionInput58",
    ends={
        Property(name="BasicBehaviors_Behavior59", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow60: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow60",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode61", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
parameter62: BinaryAssociation = BinaryAssociation(
    name="parameter62",
    ends={
        Property(name="Kernel_DirectedParameter63", type=xmof_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityParameterNode", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
decider64: BinaryAssociation = BinaryAssociation(
    name="decider64",
    ends={
        Property(name="BasicActions_OutputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test65: BinaryAssociation = BinaryAssociation(
    name="test65",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode66", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput67: BinaryAssociation = BinaryAssociation(
    name="bodyOutput67",
    ends={
        Property(name="BasicActions_OutputPin69", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode68", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput70: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput70",
    ends={
        Property(name="BasicActions_InputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode71", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart72: BinaryAssociation = BinaryAssociation(
    name="bodyPart72",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode74", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode73", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariable78: BinaryAssociation = BinaryAssociation(
    name="loopVariable78",
    ends={
        Property(name="BasicActions_OutputPin80", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode79", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart81: BinaryAssociation = BinaryAssociation(
    name="setupPart81",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode83", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode82", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test84: BinaryAssociation = BinaryAssociation(
    name="test84",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode85", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body86: BinaryAssociation = BinaryAssociation(
    name="body86",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode88", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause87", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause89: BinaryAssociation = BinaryAssociation(
    name="predecessorClause89",
    ends={
        Property(name="Syntax91", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities90", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause92: BinaryAssociation = BinaryAssociation(
    name="successorClause92",
    ends={
        Property(name="Syntax94", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities93", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider95: BinaryAssociation = BinaryAssociation(
    name="decider95",
    ends={
        Property(name="BasicActions_OutputPin97", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause96", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput98: BinaryAssociation = BinaryAssociation(
    name="bodyOutput98",
    ends={
        Property(name="BasicActions_OutputPin100", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause99", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause101: BinaryAssociation = BinaryAssociation(
    name="clause101",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result75: BinaryAssociation = BinaryAssociation(
    name="result75",
    ends={
        Property(name="BasicActions_OutputPin77", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode76", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result102: BinaryAssociation = BinaryAssociation(
    name="result102",
    ends={
        Property(name="BasicActions_OutputPin104", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode103", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node105: BinaryAssociation = BinaryAssociation(
    name="node105",
    ends={
        Property(name="Syntax107", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities106", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge108: BinaryAssociation = BinaryAssociation(
    name="edge108",
    ends={
        Property(name="Syntax110", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities109", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput111: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput111",
    ends={
        Property(name="BasicActions_OutputPin112", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput113: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput113",
    ends={
        Property(name="BasicActions_InputPin115", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode114", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput116: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput116",
    ends={
        Property(name="Syntax118", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities117", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput119: BinaryAssociation = BinaryAssociation(
    name="regionAsInput119",
    ends={
        Property(name="Syntax121", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities120", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement122: BinaryAssociation = BinaryAssociation(
    name="inputElement122",
    ends={
        Property(name="Activities123", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999)),
        Property(name="Syntax124", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1))
    }
)
outputElement125: BinaryAssociation = BinaryAssociation(
    name="outputElement125",
    ends={
        Property(name="Syntax127", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities126", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature128: BinaryAssociation = BinaryAssociation(
    name="structuralFeature128",
    ends={
        Property(name="IntermediateActions_xmof_EStructuralFeature", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction", type=IntermediateActions_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object129: BinaryAssociation = BinaryAssociation(
    name="object129",
    ends={
        Property(name="BasicActions_InputPin131", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction130", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second132: BinaryAssociation = BinaryAssociation(
    name="second132",
    ends={
        Property(name="BasicActions_InputPin133", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result134: BinaryAssociation = BinaryAssociation(
    name="result134",
    ends={
        Property(name="BasicActions_OutputPin136", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction135", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value140: BinaryAssociation = BinaryAssociation(
    name="value140",
    ends={
        Property(name="Kernel_ValueSpecification141", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result142: BinaryAssociation = BinaryAssociation(
    name="result142",
    ends={
        Property(name="BasicActions_OutputPin144", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction143", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData145: BinaryAssociation = BinaryAssociation(
    name="endData145",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue146: BinaryAssociation = BinaryAssociation(
    name="inputValue146",
    ends={
        Property(name="BasicActions_InputPin148", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction147", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value149: BinaryAssociation = BinaryAssociation(
    name="value149",
    ends={
        Property(name="BasicActions_InputPin150", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
first137: BinaryAssociation = BinaryAssociation(
    name="first137",
    ends={
        Property(name="BasicActions_InputPin139", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction138", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value153: BinaryAssociation = BinaryAssociation(
    name="value153",
    ends={
        Property(name="BasicActions_InputPin154", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result155: BinaryAssociation = BinaryAssociation(
    name="result155",
    ends={
        Property(name="BasicActions_OutputPin157", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction156", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt158: BinaryAssociation = BinaryAssociation(
    name="removeAt158",
    ends={
        Property(name="BasicActions_InputPin159", type=xmof_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result160: BinaryAssociation = BinaryAssociation(
    name="result160",
    ends={
        Property(name="BasicActions_OutputPin161", type=xmof_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result162: BinaryAssociation = BinaryAssociation(
    name="result162",
    ends={
        Property(name="BasicActions_OutputPin163", type=xmof_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end151: BinaryAssociation = BinaryAssociation(
    name="end151",
    ends={
        Property(name="IntermediateActions_xmof_EReference", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData152", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
result164: BinaryAssociation = BinaryAssociation(
    name="result164",
    ends={
        Property(name="BasicActions_OutputPin165", type=xmof_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt166: BinaryAssociation = BinaryAssociation(
    name="insertAt166",
    ends={
        Property(name="BasicActions_InputPin167", type=xmof_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt168: BinaryAssociation = BinaryAssociation(
    name="destroyAt168",
    ends={
        Property(name="BasicActions_InputPin169", type=xmof_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
association170: BinaryAssociation = BinaryAssociation(
    name="association170",
    ends={
        Property(name="IntermediateActions_xmof_EReference171", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
object172: BinaryAssociation = BinaryAssociation(
    name="object172",
    ends={
        Property(name="BasicActions_InputPin174", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction173", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result175: BinaryAssociation = BinaryAssociation(
    name="result175",
    ends={
        Property(name="BasicActions_OutputPin176", type=xmof_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result177: BinaryAssociation = BinaryAssociation(
    name="result177",
    ends={
        Property(name="BasicActions_OutputPin178", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier179: BinaryAssociation = BinaryAssociation(
    name="classifier179",
    ends={
        Property(name="IntermediateActions_xmof_EClassifier", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction180", type=IntermediateActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
target181: BinaryAssociation = BinaryAssociation(
    name="target181",
    ends={
        Property(name="BasicActions_InputPin182", type=xmof_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt183: BinaryAssociation = BinaryAssociation(
    name="insertAt183",
    ends={
        Property(name="BasicActions_InputPin184", type=xmof_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object185: BinaryAssociation = BinaryAssociation(
    name="object185",
    ends={
        Property(name="BasicActions_InputPin186", type=xmof_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object187: BinaryAssociation = BinaryAssociation(
    name="object187",
    ends={
        Property(name="BasicActions_InputPin188", type=xmof_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer189: BinaryAssociation = BinaryAssociation(
    name="reducer189",
    ends={
        Property(name="BasicBehaviors_Behavior190", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result191: BinaryAssociation = BinaryAssociation(
    name="result191",
    ends={
        Property(name="BasicActions_OutputPin193", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction192", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection194: BinaryAssociation = BinaryAssociation(
    name="collection194",
    ends={
        Property(name="BasicActions_InputPin196", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction195", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result197: BinaryAssociation = BinaryAssociation(
    name="result197",
    ends={
        Property(name="BasicActions_OutputPin198", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier199: BinaryAssociation = BinaryAssociation(
    name="classifier199",
    ends={
        Property(name="CompleteActions_xmof_EClassifier", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction200", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier201: BinaryAssociation = BinaryAssociation(
    name="classifier201",
    ends={
        Property(name="CompleteActions_xmof_EClassifier202", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result203: BinaryAssociation = BinaryAssociation(
    name="result203",
    ends={
        Property(name="BasicActions_OutputPin205", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction204", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object206: BinaryAssociation = BinaryAssociation(
    name="object206",
    ends={
        Property(name="BasicActions_InputPin208", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction207", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier209: BinaryAssociation = BinaryAssociation(
    name="oldClassifier209",
    ends={
        Property(name="CompleteActions_xmof_EClassifier210", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
object211: BinaryAssociation = BinaryAssociation(
    name="object211",
    ends={
        Property(name="BasicActions_InputPin213", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction212", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier214: BinaryAssociation = BinaryAssociation(
    name="newClassifier214",
    ends={
        Property(name="CompleteActions_xmof_EClassifier216", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction215", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
result217: BinaryAssociation = BinaryAssociation(
    name="result217",
    ends={
        Property(name="BasicActions_OutputPin218", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger219: BinaryAssociation = BinaryAssociation(
    name="trigger219",
    ends={
        Property(name="Communications_Trigger", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction220", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output221: BinaryAssociation = BinaryAssociation(
    name="output221",
    ends={
        Property(name="BasicActions_OutputPin222", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context223: BinaryAssociation = BinaryAssociation(
    name="context223",
    ends={
        Property(name="BasicActions_xmof_EClassifier", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action224", type=BasicActions_xmof_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
input225: BinaryAssociation = BinaryAssociation(
    name="input225",
    ends={
        Property(name="BasicActions_InputPin227", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action226", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result228: BinaryAssociation = BinaryAssociation(
    name="result228",
    ends={
        Property(name="BasicActions_OutputPin229", type=xmof_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument230: BinaryAssociation = BinaryAssociation(
    name="argument230",
    ends={
        Property(name="BasicActions_InputPin231", type=xmof_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target232: BinaryAssociation = BinaryAssociation(
    name="target232",
    ends={
        Property(name="BasicActions_InputPin233", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal234: BinaryAssociation = BinaryAssociation(
    name="signal234",
    ends={
        Property(name="Communications_Signal236", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction235", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior237: BinaryAssociation = BinaryAssociation(
    name="behavior237",
    ends={
        Property(name="BasicBehaviors_Behavior238", type=xmof_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation239: BinaryAssociation = BinaryAssociation(
    name="operation239",
    ends={
        Property(name="Kernel_BehavioredEOperation", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1))
    }
)
target240: BinaryAssociation = BinaryAssociation(
    name="target240",
    ends={
        Property(name="BasicActions_InputPin242", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction241", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=xmof_BasicBehaviors_OpaqueBehavior)
gen_xmof_BasicBehaviors_Behavior_BehavioredEClass = Generalization(general=BehavioredEClass, specific=xmof_BasicBehaviors_Behavior)
gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier = Generalization(general=EClassifier, specific=xmof_BasicBehaviors_BehavioredClassifier)
gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=xmof_BasicBehaviors_FunctionBehavior)
gen_xmof_Communications_Trigger_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Trigger)
gen_xmof_Communications_Event_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Event)
gen_xmof_Communications_Signal_EClassifier = Generalization(general=EClassifier, specific=xmof_Communications_Signal)
gen_xmof_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=xmof_Communications_SignalEvent)
gen_xmof_Communications_MessageEvent_Event = Generalization(general=Event, specific=xmof_Communications_MessageEvent)
gen_xmof_Communications_Reception_BehavioredEOperation = Generalization(general=BehavioredEOperation, specific=xmof_Communications_Reception)
gen_xmof_Kernel_BehavioredEOperation_EOperation = Generalization(general=EOperation, specific=xmof_Kernel_BehavioredEOperation)
gen_xmof_Kernel_BehavioredEClass_EClass = Generalization(general=EClass, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier = Generalization(general=BasicBehaviors_BehavioredClassifier, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_MainEClass_BehavioredEClass = Generalization(general=BehavioredEClass, specific=xmof_Kernel_MainEClass)
gen_xmof_Kernel_DirectedParameter_EParameter = Generalization(general=EParameter, specific=xmof_Kernel_DirectedParameter)
gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification = Generalization(general=InstanceSpecification, specific=xmof_Kernel_EEnumLiteralSpecification)
gen_xmof_Kernel_ValueSpecification_ETypedElement = Generalization(general=ETypedElement, specific=xmof_Kernel_ValueSpecification)
gen_xmof_Kernel_InstanceSpecification_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Kernel_InstanceSpecification)
gen_xmof_Kernel_Slot_EModelElement = Generalization(general=EModelElement, specific=xmof_Kernel_Slot)
gen_xmof_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_InstanceValue)
gen_xmof_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralBoolean)
gen_xmof_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_LiteralSpecification)
gen_xmof_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralInteger)
gen_xmof_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralNull)
gen_xmof_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralString)
gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralUnlimitedNatural)
gen_xmof_Kernel_PrimitiveType_EDataType = Generalization(general=EDataType, specific=xmof_Kernel_PrimitiveType)
gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=xmof_IntermediateActivities_ObjectFlow)
gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityEdge)
gen_xmof_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=xmof_IntermediateActivities_Activity)
gen_xmof_IntermediateActivities_ActivityNode_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityNode)
gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode = Generalization(general=IntermediateActivities_ActivityNode, specific=xmof_IntermediateActivities_ObjectNode)
gen_xmof_IntermediateActivities_ObjectNode_ETypedElement = Generalization(general=ETypedElement, specific=xmof_IntermediateActivities_ObjectNode)
gen_xmof_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=xmof_IntermediateActivities_MergeNode)
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
gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=xmof_ExtraStructuredActivities_ExpansionNode)
gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_ExtraStructuredActivities_ExpansionRegion)
gen_xmof_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_StructuralFeatureAction)
gen_xmof_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_TestIdentityAction)
gen_xmof_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ValueSpecificationAction)
gen_xmof_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_WriteLinkAction)
gen_xmof_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_LinkAction)
gen_xmof_IntermediateActions_LinkEndData_EModelElement = Generalization(general=EModelElement, specific=xmof_IntermediateActions_LinkEndData)
gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_WriteStructuralFeatureAction)
gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_xmof_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_ReadLinkAction)
gen_xmof_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ReadSelfAction)
gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ReadStructuralFeatureAction)
gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndCreationData)
gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndDestructionData)
gen_xmof_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ClearAssociationAction)
gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ClearStructuralFeatureAction)
gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_CreateLinkAction)
gen_xmof_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_CreateObjectAction)
gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_DestroyLinkAction)
gen_xmof_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_DestroyObjectAction)
gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_AddStructuralFeatureValueAction)
gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_StartClassifierBehaviorAction)
gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_CompleteActions_StartObjectBehaviorAction)
gen_xmof_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReduceAction)
gen_xmof_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadExtentAction)
gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadIsClassifiedObjectAction)
gen_xmof_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReclassifyObjectAction)
gen_xmof_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_AcceptEventAction)
gen_xmof_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=xmof_BasicActions_Action)
gen_xmof_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_InputPin)
gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_Pin_ETypedElement = Generalization(general=ETypedElement, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_CallAction)
gen_xmof_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=xmof_BasicActions_InvocationAction)
gen_xmof_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_SendSignalAction)
gen_xmof_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallBehaviorAction)
gen_xmof_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallOperationAction)
gen_xmof_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_OutputPin)

# Domain Model
domain_model = DomainModel(
    name="xmof",
    types={xmof_BasicBehaviors_OpaqueBehavior, Behavior, xmof_BasicBehaviors_Behavior, BehavioredEClass, Kernel_BehavioredEOperation, Kernel_DirectedParameter, BasicBehaviors_BehavioredClassifier, xmof_BasicBehaviors_BehavioredClassifier, EClassifier, BasicBehaviors_Behavior, xmof_BasicBehaviors_FunctionBehavior, OpaqueBehavior, xmof_Communications_Trigger, ENamedElement, Communications_Event, xmof_Communications_Event, xmof_Communications_Signal, Communications_xmof_EAttribute, xmof_Communications_SignalEvent, MessageEvent, Communications_Signal, xmof_Communications_MessageEvent, Event, xmof_Communications_Reception, BehavioredEOperation, xmof_Kernel_BehavioredEOperation, EOperation, xmof_Kernel_BehavioredEClass, EClass, xmof_Kernel_MainEClass, xmof_Kernel_DirectedParameter, EParameter, xmof_Kernel_EEnumLiteralSpecification, InstanceSpecification, Kernel_xmof_EEnumLiteral, xmof_Kernel_ValueSpecification, ETypedElement, xmof_Kernel_InstanceSpecification, Kernel_xmof_EClassifier, Kernel_Slot, xmof_Kernel_Slot, EModelElement, Kernel_xmof_EStructuralFeature, Kernel_ValueSpecification, Kernel_InstanceSpecification, xmof_Kernel_InstanceValue, ValueSpecification, xmof_Kernel_LiteralBoolean, LiteralSpecification, xmof_Kernel_LiteralSpecification, xmof_Kernel_LiteralInteger, xmof_Kernel_LiteralNull, xmof_Kernel_LiteralString, xmof_Kernel_LiteralUnlimitedNatural, xmof_Kernel_PrimitiveType, EDataType, xmof_IntermediateActivities_ObjectFlow, ActivityEdge, xmof_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, xmof_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, xmof_IntermediateActivities_ActivityNode, xmof_IntermediateActivities_ObjectNode, xmof_IntermediateActivities_MergeNode, ControlNode, xmof_IntermediateActivities_ControlNode, ActivityNode, xmof_IntermediateActivities_JoinNode, xmof_IntermediateActivities_InitialNode, xmof_IntermediateActivities_FinalNode, xmof_IntermediateActivities_ForkNode, xmof_IntermediateActivities_ControlFlow, xmof_IntermediateActivities_DecisionNode, IntermediateActivities_ObjectFlow, xmof_IntermediateActivities_ActivityFinalNode, FinalNode, xmof_IntermediateActivities_ActivityParameterNode, ObjectNode, xmof_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, xmof_CompleteStructuredActivities_ExecutableNode, xmof_CompleteStructuredActivities_Clause, CompleteStructuredActivities_Clause, xmof_CompleteStructuredActivities_ConditionalNode, xmof_CompleteStructuredActivities_StructuredActivityNode, Action, xmof_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, xmof_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, xmof_IntermediateActions_StructuralFeatureAction, IntermediateActions_xmof_EStructuralFeature, xmof_IntermediateActions_TestIdentityAction, xmof_IntermediateActions_ValueSpecificationAction, xmof_IntermediateActions_WriteLinkAction, LinkAction, xmof_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, xmof_IntermediateActions_LinkEndData, xmof_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, xmof_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, xmof_IntermediateActions_ReadLinkAction, xmof_IntermediateActions_ReadSelfAction, IntermediateActions_xmof_EReference, xmof_IntermediateActions_ReadStructuralFeatureAction, xmof_IntermediateActions_LinkEndCreationData, LinkEndData, xmof_IntermediateActions_LinkEndDestructionData, xmof_IntermediateActions_ClearAssociationAction, xmof_IntermediateActions_ClearStructuralFeatureAction, xmof_IntermediateActions_CreateLinkAction, WriteLinkAction, xmof_IntermediateActions_CreateObjectAction, IntermediateActions_xmof_EClassifier, xmof_IntermediateActions_DestroyLinkAction, xmof_IntermediateActions_DestroyObjectAction, xmof_IntermediateActions_AddStructuralFeatureValueAction, xmof_CompleteActions_StartClassifierBehaviorAction, xmof_CompleteActions_StartObjectBehaviorAction, CallAction, xmof_CompleteActions_ReduceAction, xmof_CompleteActions_ReadExtentAction, CompleteActions_xmof_EClassifier, xmof_CompleteActions_ReadIsClassifiedObjectAction, xmof_CompleteActions_ReclassifyObjectAction, xmof_CompleteActions_AcceptEventAction, Communications_Trigger, xmof_BasicActions_Action, ExecutableNode, BasicActions_xmof_EClassifier, xmof_BasicActions_InputPin, Pin, xmof_BasicActions_Pin, IntermediateActivities_ObjectNode, xmof_BasicActions_CallAction, InvocationAction, xmof_BasicActions_InvocationAction, xmof_BasicActions_SendSignalAction, xmof_BasicActions_CallBehaviorAction, xmof_BasicActions_CallOperationAction, xmof_BasicActions_OutputPin, CallConcurrencyKind, ParameterDirectionKind, ExpansionKind},
    associations={specification0, ownedParameter1, context2, ownedBehavior4, classifierBehavior5, event8, ownedAttribute9, signal10, signal11, method13, eEnumLiteral15, classifier16, slot17, definingFeature20, value21, owningInstance23, instance26, activity27, source29, target32, inStructuredNode35, guard38, node40, edge43, inStructuredNode46, activity49, outgoing52, incoming55, decisionInput58, decisionInputFlow60, parameter62, decider64, test65, bodyOutput67, loopVariableInput70, bodyPart72, loopVariable78, setupPart81, test84, body86, predecessorClause89, successorClause92, decider95, bodyOutput98, clause101, result75, result102, node105, edge108, structuredNodeOutput111, structuredNodeInput113, regionAsOutput116, regionAsInput119, inputElement122, outputElement125, structuralFeature128, object129, second132, result134, value140, result142, endData145, inputValue146, value149, first137, value153, result155, removeAt158, result160, result162, end151, result164, insertAt166, destroyAt168, association170, object172, result175, result177, classifier179, target181, insertAt183, object185, object187, reducer189, result191, collection194, result197, classifier199, classifier201, result203, object206, oldClassifier209, object211, newClassifier214, result217, trigger219, output221, context223, input225, result228, argument230, target232, signal234, behavior237, operation239, target240},
    generalizations={gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior, gen_xmof_BasicBehaviors_Behavior_BehavioredEClass, gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier, gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_xmof_Communications_Trigger_ENamedElement, gen_xmof_Communications_Event_ENamedElement, gen_xmof_Communications_Signal_EClassifier, gen_xmof_Communications_SignalEvent_MessageEvent, gen_xmof_Communications_MessageEvent_Event, gen_xmof_Communications_Reception_BehavioredEOperation, gen_xmof_Kernel_BehavioredEOperation_EOperation, gen_xmof_Kernel_BehavioredEClass_EClass, gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier, gen_xmof_Kernel_MainEClass_BehavioredEClass, gen_xmof_Kernel_DirectedParameter_EParameter, gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification, gen_xmof_Kernel_ValueSpecification_ETypedElement, gen_xmof_Kernel_InstanceSpecification_ENamedElement, gen_xmof_Kernel_Slot_EModelElement, gen_xmof_Kernel_InstanceValue_ValueSpecification, gen_xmof_Kernel_LiteralBoolean_LiteralSpecification, gen_xmof_Kernel_LiteralSpecification_ValueSpecification, gen_xmof_Kernel_LiteralInteger_LiteralSpecification, gen_xmof_Kernel_LiteralNull_LiteralSpecification, gen_xmof_Kernel_LiteralString_LiteralSpecification, gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_xmof_Kernel_PrimitiveType_EDataType, gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge, gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement, gen_xmof_IntermediateActivities_Activity_Behavior, gen_xmof_IntermediateActivities_ActivityNode_ENamedElement, gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_xmof_IntermediateActivities_ObjectNode_ETypedElement, gen_xmof_IntermediateActivities_MergeNode_ControlNode, gen_xmof_IntermediateActivities_ControlNode_ActivityNode, gen_xmof_IntermediateActivities_JoinNode_ControlNode, gen_xmof_IntermediateActivities_InitialNode_ControlNode, gen_xmof_IntermediateActivities_FinalNode_ControlNode, gen_xmof_IntermediateActivities_ForkNode_ControlNode, gen_xmof_IntermediateActivities_ControlFlow_ActivityEdge, gen_xmof_IntermediateActivities_DecisionNode_ControlNode, gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode, gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_xmof_CompleteStructuredActivities_Clause_EModelElement, gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action, gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_xmof_IntermediateActions_StructuralFeatureAction_Action, gen_xmof_IntermediateActions_TestIdentityAction_Action, gen_xmof_IntermediateActions_ValueSpecificationAction_Action, gen_xmof_IntermediateActions_WriteLinkAction_LinkAction, gen_xmof_IntermediateActions_LinkAction_Action, gen_xmof_IntermediateActions_LinkEndData_EModelElement, gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_IntermediateActions_ReadLinkAction_LinkAction, gen_xmof_IntermediateActions_ReadSelfAction_Action, gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData, gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_xmof_IntermediateActions_ClearAssociationAction_Action, gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_CreateObjectAction_Action, gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_DestroyObjectAction_Action, gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action, gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction, gen_xmof_CompleteActions_ReduceAction_Action, gen_xmof_CompleteActions_ReadExtentAction_Action, gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_xmof_CompleteActions_ReclassifyObjectAction_Action, gen_xmof_CompleteActions_AcceptEventAction_Action, gen_xmof_BasicActions_Action_ExecutableNode, gen_xmof_BasicActions_InputPin_Pin, gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_xmof_BasicActions_Pin_ETypedElement, gen_xmof_BasicActions_CallAction_InvocationAction, gen_xmof_BasicActions_InvocationAction_Action, gen_xmof_BasicActions_SendSignalAction_InvocationAction, gen_xmof_BasicActions_CallBehaviorAction_CallAction, gen_xmof_BasicActions_CallOperationAction_CallAction, gen_xmof_BasicActions_OutputPin_Pin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)