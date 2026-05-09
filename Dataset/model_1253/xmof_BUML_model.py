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
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="return_")
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
xmof_BasicBehaviors_OpaqueBehavior = Class(name="xmof_BasicBehaviors_OpaqueBehavior")
Behavior = Class(name="Behavior")
xmof_BasicBehaviors_Behavior = Class(name="xmof_BasicBehaviors_Behavior", is_abstract=True)
BehavioredEClass = Class(name="BehavioredEClass")
Kernel_BehavioredEOperation = Class(name="Kernel_BehavioredEOperation")
Kernel_DirectedParameter = Class(name="Kernel_DirectedParameter")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors_BehavioredClassifier")
xmof_BasicBehaviors_BehavioredClassifier = Class(name="xmof_BasicBehaviors_BehavioredClassifier", is_abstract=True)
EClassifier = Class(name="EClassifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors_Behavior")
Kernel_xmof_EClassifier = Class(name="Kernel_xmof_EClassifier")
xmof_BasicBehaviors_FunctionBehavior = Class(name="xmof_BasicBehaviors_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
xmof_Communications_Trigger = Class(name="xmof_Communications_Trigger")
ENamedElement = Class(name="ENamedElement")
Communications_Event = Class(name="Communications_Event")
xmof_Communications_Event = Class(name="xmof_Communications_Event", is_abstract=True)
xmof_Communications_Signal = Class(name="xmof_Communications_Signal")
Communications_xmof_EAttribute = Class(name="Communications_xmof_EAttribute")
xmof_Communications_SignalEvent = Class(name="xmof_Communications_SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications_Signal")
xmof_Communications_MessageEvent = Class(name="xmof_Communications_MessageEvent", is_abstract=True)
Event = Class(name="Event")
xmof_Communications_Reception = Class(name="xmof_Communications_Reception")
BehavioredEOperation = Class(name="BehavioredEOperation")
xmof_Kernel_BehavioredEOperation = Class(name="xmof_Kernel_BehavioredEOperation")
EOperation = Class(name="EOperation")
xmof_Kernel_BehavioredEClass = Class(name="xmof_Kernel_BehavioredEClass")
EClass = Class(name="EClass")
xmof_Kernel_MainEClass = Class(name="xmof_Kernel_MainEClass")
xmof_Kernel_DirectedParameter = Class(name="xmof_Kernel_DirectedParameter")
EParameter = Class(name="EParameter")
xmof_Kernel_EEnumLiteralSpecification = Class(name="xmof_Kernel_EEnumLiteralSpecification")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_xmof_EEnumLiteral = Class(name="Kernel_xmof_EEnumLiteral")
xmof_Kernel_ValueSpecification = Class(name="xmof_Kernel_ValueSpecification", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
xmof_Kernel_InstanceSpecification = Class(name="xmof_Kernel_InstanceSpecification")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities_ActivityNode")
Kernel_Slot = Class(name="Kernel_Slot")
xmof_Kernel_Slot = Class(name="xmof_Kernel_Slot")
EModelElement = Class(name="EModelElement")
Kernel_xmof_EStructuralFeature = Class(name="Kernel_xmof_EStructuralFeature")
Kernel_ValueSpecification = Class(name="Kernel_ValueSpecification")
Kernel_InstanceSpecification = Class(name="Kernel_InstanceSpecification")
xmof_Kernel_InstanceValue = Class(name="xmof_Kernel_InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
xmof_Kernel_LiteralBoolean = Class(name="xmof_Kernel_LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
xmof_Kernel_LiteralSpecification = Class(name="xmof_Kernel_LiteralSpecification", is_abstract=True)
xmof_Kernel_LiteralInteger = Class(name="xmof_Kernel_LiteralInteger")
xmof_Kernel_LiteralNull = Class(name="xmof_Kernel_LiteralNull")
xmof_Kernel_LiteralString = Class(name="xmof_Kernel_LiteralString")
xmof_Kernel_LiteralUnlimitedNatural = Class(name="xmof_Kernel_LiteralUnlimitedNatural")
xmof_Kernel_PrimitiveType = Class(name="xmof_Kernel_PrimitiveType")
EDataType = Class(name="EDataType")
xmof_IntermediateActivities_ObjectFlow = Class(name="xmof_IntermediateActivities_ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
xmof_IntermediateActivities_ActivityEdge = Class(name="xmof_IntermediateActivities_ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities_Activity")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities_StructuredActivityNode")
xmof_IntermediateActivities_Activity = Class(name="xmof_IntermediateActivities_Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities_ActivityEdge")
xmof_IntermediateActivities_ActivityNode = Class(name="xmof_IntermediateActivities_ActivityNode", is_abstract=True)
xmof_IntermediateActivities_ObjectNode = Class(name="xmof_IntermediateActivities_ObjectNode", is_abstract=True)
xmof_IntermediateActivities_MergeNode = Class(name="xmof_IntermediateActivities_MergeNode")
ControlNode = Class(name="ControlNode")
xmof_IntermediateActivities_ControlNode = Class(name="xmof_IntermediateActivities_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
xmof_IntermediateActivities_JoinNode = Class(name="xmof_IntermediateActivities_JoinNode")
xmof_IntermediateActivities_InitialNode = Class(name="xmof_IntermediateActivities_InitialNode")
xmof_IntermediateActivities_FinalNode = Class(name="xmof_IntermediateActivities_FinalNode", is_abstract=True)
xmof_IntermediateActivities_ForkNode = Class(name="xmof_IntermediateActivities_ForkNode")
xmof_IntermediateActivities_ControlFlow = Class(name="xmof_IntermediateActivities_ControlFlow")
xmof_IntermediateActivities_DecisionNode = Class(name="xmof_IntermediateActivities_DecisionNode")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities_ObjectFlow")
xmof_IntermediateActivities_ActivityFinalNode = Class(name="xmof_IntermediateActivities_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
xmof_IntermediateActivities_ActivityParameterNode = Class(name="xmof_IntermediateActivities_ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
xmof_CompleteStructuredActivities_LoopNode = Class(name="xmof_CompleteStructuredActivities_LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions_OutputPin")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities_ExecutableNode")
BasicActions_InputPin = Class(name="BasicActions_InputPin")
xmof_CompleteStructuredActivities_ExecutableNode = Class(name="xmof_CompleteStructuredActivities_ExecutableNode", is_abstract=True)
xmof_CompleteStructuredActivities_Clause = Class(name="xmof_CompleteStructuredActivities_Clause")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities_Clause")
xmof_ExtraStructuredActivities_ExpansionRegion = Class(name="xmof_ExtraStructuredActivities_ExpansionRegion")
xmof_CompleteStructuredActivities_ConditionalNode = Class(name="xmof_CompleteStructuredActivities_ConditionalNode")
xmof_CompleteStructuredActivities_StructuredActivityNode = Class(name="xmof_CompleteStructuredActivities_StructuredActivityNode")
Action = Class(name="Action")
xmof_ExtraStructuredActivities_ExpansionNode = Class(name="xmof_ExtraStructuredActivities_ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities_ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities_ExpansionNode")
xmof_IntermediateActions_StructuralFeatureAction = Class(name="xmof_IntermediateActions_StructuralFeatureAction", is_abstract=True)
IntermediateActions_xmof_EStructuralFeature = Class(name="IntermediateActions_xmof_EStructuralFeature")
xmof_IntermediateActions_TestIdentityAction = Class(name="xmof_IntermediateActions_TestIdentityAction")
xmof_IntermediateActions_ValueSpecificationAction = Class(name="xmof_IntermediateActions_ValueSpecificationAction")
xmof_IntermediateActions_WriteLinkAction = Class(name="xmof_IntermediateActions_WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
IntermediateActions_LinkEndData = Class(name="IntermediateActions_LinkEndData")
xmof_IntermediateActions_LinkAction = Class(name="xmof_IntermediateActions_LinkAction", is_abstract=True)
xmof_IntermediateActions_LinkEndData = Class(name="xmof_IntermediateActions_LinkEndData")
IntermediateActions_xmof_EReference = Class(name="IntermediateActions_xmof_EReference")
xmof_IntermediateActions_WriteStructuralFeatureAction = Class(name="xmof_IntermediateActions_WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
xmof_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
xmof_IntermediateActions_ReadLinkAction = Class(name="xmof_IntermediateActions_ReadLinkAction")
xmof_IntermediateActions_ReadSelfAction = Class(name="xmof_IntermediateActions_ReadSelfAction")
xmof_IntermediateActions_ReadStructuralFeatureAction = Class(name="xmof_IntermediateActions_ReadStructuralFeatureAction")
xmof_IntermediateActions_LinkEndCreationData = Class(name="xmof_IntermediateActions_LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
xmof_IntermediateActions_LinkEndDestructionData = Class(name="xmof_IntermediateActions_LinkEndDestructionData")
xmof_IntermediateActions_ClearAssociationAction = Class(name="xmof_IntermediateActions_ClearAssociationAction")
xmof_IntermediateActions_ClearStructuralFeatureAction = Class(name="xmof_IntermediateActions_ClearStructuralFeatureAction")
xmof_IntermediateActions_CreateLinkAction = Class(name="xmof_IntermediateActions_CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
xmof_IntermediateActions_CreateObjectAction = Class(name="xmof_IntermediateActions_CreateObjectAction")
IntermediateActions_xmof_EClassifier = Class(name="IntermediateActions_xmof_EClassifier")
xmof_IntermediateActions_DestroyLinkAction = Class(name="xmof_IntermediateActions_DestroyLinkAction")
xmof_IntermediateActions_DestroyObjectAction = Class(name="xmof_IntermediateActions_DestroyObjectAction")
xmof_IntermediateActions_AddStructuralFeatureValueAction = Class(name="xmof_IntermediateActions_AddStructuralFeatureValueAction")
xmof_CompleteActions_StartClassifierBehaviorAction = Class(name="xmof_CompleteActions_StartClassifierBehaviorAction")
xmof_CompleteActions_StartObjectBehaviorAction = Class(name="xmof_CompleteActions_StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
xmof_CompleteActions_ReduceAction = Class(name="xmof_CompleteActions_ReduceAction")
xmof_CompleteActions_ReadExtentAction = Class(name="xmof_CompleteActions_ReadExtentAction")
CompleteActions_xmof_EClassifier = Class(name="CompleteActions_xmof_EClassifier")
xmof_CompleteActions_ReadIsClassifiedObjectAction = Class(name="xmof_CompleteActions_ReadIsClassifiedObjectAction")
xmof_CompleteActions_ReclassifyObjectAction = Class(name="xmof_CompleteActions_ReclassifyObjectAction")
xmof_CompleteActions_AcceptEventAction = Class(name="xmof_CompleteActions_AcceptEventAction")
Communications_Trigger = Class(name="Communications_Trigger")
xmof_BasicActions_Action = Class(name="xmof_BasicActions_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
BasicActions_xmof_EClassifier = Class(name="BasicActions_xmof_EClassifier")
xmof_BasicActions_InputPin = Class(name="xmof_BasicActions_InputPin")
Pin = Class(name="Pin")
xmof_BasicActions_Pin = Class(name="xmof_BasicActions_Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities_ObjectNode")
xmof_BasicActions_CallAction = Class(name="xmof_BasicActions_CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
xmof_BasicActions_InvocationAction = Class(name="xmof_BasicActions_InvocationAction", is_abstract=True)
xmof_BasicActions_SendSignalAction = Class(name="xmof_BasicActions_SendSignalAction")
xmof_BasicActions_CallBehaviorAction = Class(name="xmof_BasicActions_CallBehaviorAction")
xmof_BasicActions_CallOperationAction = Class(name="xmof_BasicActions_CallOperationAction")
xmof_BasicActions_OutputPin = Class(name="xmof_BasicActions_OutputPin")

# xmof_BasicBehaviors_OpaqueBehavior class attributes and methods
xmof_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior.attributes={xmof_BasicBehaviors_OpaqueBehavior_body, xmof_BasicBehaviors_OpaqueBehavior_language}

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

# Kernel_xmof_EClassifier class attributes and methods

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

# IntermediateActivities_ActivityNode class attributes and methods

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

# xmof_ExtraStructuredActivities_ExpansionRegion class attributes and methods
xmof_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
xmof_ExtraStructuredActivities_ExpansionRegion.attributes={xmof_ExtraStructuredActivities_ExpansionRegion_mode}

# xmof_CompleteStructuredActivities_ConditionalNode class attributes and methods
xmof_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode.attributes={xmof_CompleteStructuredActivities_ConditionalNode_assured, xmof_CompleteStructuredActivities_ConditionalNode_determinate}

# xmof_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
xmof_CompleteStructuredActivities_StructuredActivityNode.attributes={xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# xmof_IntermediateActions_StructuralFeatureAction class attributes and methods

# IntermediateActions_xmof_EStructuralFeature class attributes and methods

# xmof_IntermediateActions_TestIdentityAction class attributes and methods

# xmof_IntermediateActions_ValueSpecificationAction class attributes and methods

# xmof_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_LinkAction class attributes and methods

# xmof_IntermediateActions_LinkEndData class attributes and methods

# IntermediateActions_xmof_EReference class attributes and methods

# xmof_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_ReadLinkAction class attributes and methods

# xmof_IntermediateActions_ReadSelfAction class attributes and methods

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
xmof_IntermediateActions_DestroyObjectAction.attributes={xmof_IntermediateActions_DestroyObjectAction_destroyLinks, xmof_IntermediateActions_DestroyObjectAction_destroyOwnedObjects}

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
classifierBehavior5: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior5",
    ends={
        Property(name="BasicBehaviors_Behavior7", type=xmof_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_BehavioredClassifier6", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="BehavioredEOperation", type=xmof_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(0, 1))
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
classifier15: BinaryAssociation = BinaryAssociation(
    name="classifier15",
    ends={
        Property(name="Kernel_xmof_EClassifier", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceSpecification", type=Kernel_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
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
        Property(name="Behavior", type=xmof_Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
eEnumLiteral14: BinaryAssociation = BinaryAssociation(
    name="eEnumLiteral14",
    ends={
        Property(name="Kernel_xmof_EEnumLiteral", type=xmof_Kernel_EEnumLiteralSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EEnumLiteralSpecification", type=Kernel_xmof_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="ActivityNode", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
slot16: BinaryAssociation = BinaryAssociation(
    name="slot16",
    ends={
        Property(name="Slot", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature17: BinaryAssociation = BinaryAssociation(
    name="definingFeature17",
    ends={
        Property(name="Kernel_xmof_EStructuralFeature", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot", type=Kernel_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="Kernel_ValueSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot19", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance20: BinaryAssociation = BinaryAssociation(
    name="owningInstance20",
    ends={
        Property(name="InstanceSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance21: BinaryAssociation = BinaryAssociation(
    name="instance21",
    ends={
        Property(name="Kernel_InstanceSpecification", type=xmof_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
activity22: BinaryAssociation = BinaryAssociation(
    name="activity22",
    ends={
        Property(name="Activity", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput43: BinaryAssociation = BinaryAssociation(
    name="decisionInput43",
    ends={
        Property(name="BasicBehaviors_Behavior44", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="ActivityNode25", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode26: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode26",
    ends={
        Property(name="StructuredActivityNode", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge27", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
guard28: BinaryAssociation = BinaryAssociation(
    name="guard28",
    ends={
        Property(name="Kernel_ValueSpecification29", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node30: BinaryAssociation = BinaryAssociation(
    name="node30",
    ends={
        Property(name="ActivityNode31", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge32: BinaryAssociation = BinaryAssociation(
    name="edge32",
    ends={
        Property(name="ActivityEdge", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity33", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode34: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode34",
    ends={
        Property(name="StructuredActivityNode35", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity36: BinaryAssociation = BinaryAssociation(
    name="activity36",
    ends={
        Property(name="Activity38", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node37", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing39: BinaryAssociation = BinaryAssociation(
    name="outgoing39",
    ends={
        Property(name="ActivityEdge40", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming41: BinaryAssociation = BinaryAssociation(
    name="incoming41",
    ends={
        Property(name="ActivityEdge42", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause75: BinaryAssociation = BinaryAssociation(
    name="successorClause75",
    ends={
        Property(name="Clause76", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInputFlow45: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow45",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode46", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
parameter47: BinaryAssociation = BinaryAssociation(
    name="parameter47",
    ends={
        Property(name="Kernel_DirectedParameter48", type=xmof_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityParameterNode", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
decider49: BinaryAssociation = BinaryAssociation(
    name="decider49",
    ends={
        Property(name="BasicActions_OutputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test50: BinaryAssociation = BinaryAssociation(
    name="test50",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode51", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput52: BinaryAssociation = BinaryAssociation(
    name="bodyOutput52",
    ends={
        Property(name="BasicActions_OutputPin54", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode53", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput55: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput55",
    ends={
        Property(name="BasicActions_InputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode56", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart57: BinaryAssociation = BinaryAssociation(
    name="bodyPart57",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode59", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode58", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result60: BinaryAssociation = BinaryAssociation(
    name="result60",
    ends={
        Property(name="BasicActions_OutputPin62", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode61", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable63: BinaryAssociation = BinaryAssociation(
    name="loopVariable63",
    ends={
        Property(name="BasicActions_OutputPin65", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode64", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart66: BinaryAssociation = BinaryAssociation(
    name="setupPart66",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode68", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode67", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test69: BinaryAssociation = BinaryAssociation(
    name="test69",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode70", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body71: BinaryAssociation = BinaryAssociation(
    name="body71",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode73", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause72", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause74: BinaryAssociation = BinaryAssociation(
    name="predecessorClause74",
    ends={
        Property(name="Clause", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider77: BinaryAssociation = BinaryAssociation(
    name="decider77",
    ends={
        Property(name="BasicActions_OutputPin79", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause78", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput80: BinaryAssociation = BinaryAssociation(
    name="bodyOutput80",
    ends={
        Property(name="BasicActions_OutputPin82", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause81", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause83: BinaryAssociation = BinaryAssociation(
    name="clause83",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result84: BinaryAssociation = BinaryAssociation(
    name="result84",
    ends={
        Property(name="BasicActions_OutputPin86", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode85", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node87: BinaryAssociation = BinaryAssociation(
    name="node87",
    ends={
        Property(name="ActivityNode88", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge89: BinaryAssociation = BinaryAssociation(
    name="edge89",
    ends={
        Property(name="ActivityEdge91", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode90", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput92: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput92",
    ends={
        Property(name="BasicActions_OutputPin93", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput94: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput94",
    ends={
        Property(name="BasicActions_InputPin96", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode95", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput97: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput97",
    ends={
        Property(name="ExpansionRegion", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput98: BinaryAssociation = BinaryAssociation(
    name="regionAsInput98",
    ends={
        Property(name="ExpansionRegion99", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement100: BinaryAssociation = BinaryAssociation(
    name="inputElement100",
    ends={
        Property(name="ExpansionNode", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement101: BinaryAssociation = BinaryAssociation(
    name="outputElement101",
    ends={
        Property(name="ExpansionNode102", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature103: BinaryAssociation = BinaryAssociation(
    name="structuralFeature103",
    ends={
        Property(name="IntermediateActions_xmof_EStructuralFeature", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction", type=IntermediateActions_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object104: BinaryAssociation = BinaryAssociation(
    name="object104",
    ends={
        Property(name="BasicActions_InputPin106", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction105", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second107: BinaryAssociation = BinaryAssociation(
    name="second107",
    ends={
        Property(name="BasicActions_InputPin108", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result109: BinaryAssociation = BinaryAssociation(
    name="result109",
    ends={
        Property(name="BasicActions_OutputPin111", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction110", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first112: BinaryAssociation = BinaryAssociation(
    name="first112",
    ends={
        Property(name="BasicActions_InputPin114", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction113", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value115: BinaryAssociation = BinaryAssociation(
    name="value115",
    ends={
        Property(name="Kernel_ValueSpecification116", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result117: BinaryAssociation = BinaryAssociation(
    name="result117",
    ends={
        Property(name="BasicActions_OutputPin119", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction118", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData120: BinaryAssociation = BinaryAssociation(
    name="endData120",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
insertAt141: BinaryAssociation = BinaryAssociation(
    name="insertAt141",
    ends={
        Property(name="BasicActions_InputPin142", type=xmof_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
inputValue121: BinaryAssociation = BinaryAssociation(
    name="inputValue121",
    ends={
        Property(name="BasicActions_InputPin123", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction122", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value124: BinaryAssociation = BinaryAssociation(
    name="value124",
    ends={
        Property(name="BasicActions_InputPin125", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end126: BinaryAssociation = BinaryAssociation(
    name="end126",
    ends={
        Property(name="IntermediateActions_xmof_EReference", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData127", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
value128: BinaryAssociation = BinaryAssociation(
    name="value128",
    ends={
        Property(name="BasicActions_InputPin129", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result130: BinaryAssociation = BinaryAssociation(
    name="result130",
    ends={
        Property(name="BasicActions_OutputPin132", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction131", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt133: BinaryAssociation = BinaryAssociation(
    name="removeAt133",
    ends={
        Property(name="BasicActions_InputPin134", type=xmof_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result135: BinaryAssociation = BinaryAssociation(
    name="result135",
    ends={
        Property(name="BasicActions_OutputPin136", type=xmof_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result137: BinaryAssociation = BinaryAssociation(
    name="result137",
    ends={
        Property(name="BasicActions_OutputPin138", type=xmof_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result139: BinaryAssociation = BinaryAssociation(
    name="result139",
    ends={
        Property(name="BasicActions_OutputPin140", type=xmof_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt158: BinaryAssociation = BinaryAssociation(
    name="insertAt158",
    ends={
        Property(name="BasicActions_InputPin159", type=xmof_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destroyAt143: BinaryAssociation = BinaryAssociation(
    name="destroyAt143",
    ends={
        Property(name="BasicActions_InputPin144", type=xmof_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
association145: BinaryAssociation = BinaryAssociation(
    name="association145",
    ends={
        Property(name="IntermediateActions_xmof_EReference146", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
object147: BinaryAssociation = BinaryAssociation(
    name="object147",
    ends={
        Property(name="BasicActions_InputPin149", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction148", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result150: BinaryAssociation = BinaryAssociation(
    name="result150",
    ends={
        Property(name="BasicActions_OutputPin151", type=xmof_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result152: BinaryAssociation = BinaryAssociation(
    name="result152",
    ends={
        Property(name="BasicActions_OutputPin153", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier154: BinaryAssociation = BinaryAssociation(
    name="classifier154",
    ends={
        Property(name="IntermediateActions_xmof_EClassifier", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction155", type=IntermediateActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
target156: BinaryAssociation = BinaryAssociation(
    name="target156",
    ends={
        Property(name="BasicActions_InputPin157", type=xmof_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier184: BinaryAssociation = BinaryAssociation(
    name="oldClassifier184",
    ends={
        Property(name="CompleteActions_xmof_EClassifier185", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
object160: BinaryAssociation = BinaryAssociation(
    name="object160",
    ends={
        Property(name="BasicActions_InputPin161", type=xmof_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object162: BinaryAssociation = BinaryAssociation(
    name="object162",
    ends={
        Property(name="BasicActions_InputPin163", type=xmof_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer164: BinaryAssociation = BinaryAssociation(
    name="reducer164",
    ends={
        Property(name="BasicBehaviors_Behavior165", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result166: BinaryAssociation = BinaryAssociation(
    name="result166",
    ends={
        Property(name="BasicActions_OutputPin168", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction167", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection169: BinaryAssociation = BinaryAssociation(
    name="collection169",
    ends={
        Property(name="BasicActions_InputPin171", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction170", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result172: BinaryAssociation = BinaryAssociation(
    name="result172",
    ends={
        Property(name="BasicActions_OutputPin173", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier174: BinaryAssociation = BinaryAssociation(
    name="classifier174",
    ends={
        Property(name="CompleteActions_xmof_EClassifier", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction175", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier176: BinaryAssociation = BinaryAssociation(
    name="classifier176",
    ends={
        Property(name="CompleteActions_xmof_EClassifier177", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result178: BinaryAssociation = BinaryAssociation(
    name="result178",
    ends={
        Property(name="BasicActions_OutputPin180", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction179", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object181: BinaryAssociation = BinaryAssociation(
    name="object181",
    ends={
        Property(name="BasicActions_InputPin183", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction182", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object186: BinaryAssociation = BinaryAssociation(
    name="object186",
    ends={
        Property(name="BasicActions_InputPin188", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction187", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier189: BinaryAssociation = BinaryAssociation(
    name="newClassifier189",
    ends={
        Property(name="CompleteActions_xmof_EClassifier191", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction190", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
result192: BinaryAssociation = BinaryAssociation(
    name="result192",
    ends={
        Property(name="BasicActions_OutputPin193", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger194: BinaryAssociation = BinaryAssociation(
    name="trigger194",
    ends={
        Property(name="Communications_Trigger", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction195", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output196: BinaryAssociation = BinaryAssociation(
    name="output196",
    ends={
        Property(name="BasicActions_OutputPin197", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context198: BinaryAssociation = BinaryAssociation(
    name="context198",
    ends={
        Property(name="BasicActions_xmof_EClassifier", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action199", type=BasicActions_xmof_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
input200: BinaryAssociation = BinaryAssociation(
    name="input200",
    ends={
        Property(name="BasicActions_InputPin202", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action201", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result203: BinaryAssociation = BinaryAssociation(
    name="result203",
    ends={
        Property(name="BasicActions_OutputPin204", type=xmof_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument205: BinaryAssociation = BinaryAssociation(
    name="argument205",
    ends={
        Property(name="BasicActions_InputPin206", type=xmof_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target207: BinaryAssociation = BinaryAssociation(
    name="target207",
    ends={
        Property(name="BasicActions_InputPin208", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal209: BinaryAssociation = BinaryAssociation(
    name="signal209",
    ends={
        Property(name="Communications_Signal211", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction210", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior212: BinaryAssociation = BinaryAssociation(
    name="behavior212",
    ends={
        Property(name="BasicBehaviors_Behavior213", type=xmof_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
target215: BinaryAssociation = BinaryAssociation(
    name="target215",
    ends={
        Property(name="BasicActions_InputPin217", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction216", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation214: BinaryAssociation = BinaryAssociation(
    name="operation214",
    ends={
        Property(name="Kernel_BehavioredEOperation", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1))
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
gen_xmof_IntermediateActions_LinkEndData_EModelElement = Generalization(general=EModelElement, specific=xmof_IntermediateActions_LinkEndData)
gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_WriteStructuralFeatureAction)
gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_xmof_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_ReadLinkAction)
gen_xmof_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ReadSelfAction)
gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ReadStructuralFeatureAction)
gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndCreationData)
gen_xmof_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_LinkAction)
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
    types={xmof_BasicBehaviors_OpaqueBehavior, Behavior, xmof_BasicBehaviors_Behavior, BehavioredEClass, Kernel_BehavioredEOperation, Kernel_DirectedParameter, BasicBehaviors_BehavioredClassifier, xmof_BasicBehaviors_BehavioredClassifier, EClassifier, BasicBehaviors_Behavior, Kernel_xmof_EClassifier, xmof_BasicBehaviors_FunctionBehavior, OpaqueBehavior, xmof_Communications_Trigger, ENamedElement, Communications_Event, xmof_Communications_Event, xmof_Communications_Signal, Communications_xmof_EAttribute, xmof_Communications_SignalEvent, MessageEvent, Communications_Signal, xmof_Communications_MessageEvent, Event, xmof_Communications_Reception, BehavioredEOperation, xmof_Kernel_BehavioredEOperation, EOperation, xmof_Kernel_BehavioredEClass, EClass, xmof_Kernel_MainEClass, xmof_Kernel_DirectedParameter, EParameter, xmof_Kernel_EEnumLiteralSpecification, InstanceSpecification, Kernel_xmof_EEnumLiteral, xmof_Kernel_ValueSpecification, ETypedElement, xmof_Kernel_InstanceSpecification, IntermediateActivities_ActivityNode, Kernel_Slot, xmof_Kernel_Slot, EModelElement, Kernel_xmof_EStructuralFeature, Kernel_ValueSpecification, Kernel_InstanceSpecification, xmof_Kernel_InstanceValue, ValueSpecification, xmof_Kernel_LiteralBoolean, LiteralSpecification, xmof_Kernel_LiteralSpecification, xmof_Kernel_LiteralInteger, xmof_Kernel_LiteralNull, xmof_Kernel_LiteralString, xmof_Kernel_LiteralUnlimitedNatural, xmof_Kernel_PrimitiveType, EDataType, xmof_IntermediateActivities_ObjectFlow, ActivityEdge, xmof_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, CompleteStructuredActivities_StructuredActivityNode, xmof_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, xmof_IntermediateActivities_ActivityNode, xmof_IntermediateActivities_ObjectNode, xmof_IntermediateActivities_MergeNode, ControlNode, xmof_IntermediateActivities_ControlNode, ActivityNode, xmof_IntermediateActivities_JoinNode, xmof_IntermediateActivities_InitialNode, xmof_IntermediateActivities_FinalNode, xmof_IntermediateActivities_ForkNode, xmof_IntermediateActivities_ControlFlow, xmof_IntermediateActivities_DecisionNode, IntermediateActivities_ObjectFlow, xmof_IntermediateActivities_ActivityFinalNode, FinalNode, xmof_IntermediateActivities_ActivityParameterNode, ObjectNode, xmof_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, xmof_CompleteStructuredActivities_ExecutableNode, xmof_CompleteStructuredActivities_Clause, CompleteStructuredActivities_Clause, xmof_ExtraStructuredActivities_ExpansionRegion, xmof_CompleteStructuredActivities_ConditionalNode, xmof_CompleteStructuredActivities_StructuredActivityNode, Action, xmof_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, xmof_IntermediateActions_StructuralFeatureAction, IntermediateActions_xmof_EStructuralFeature, xmof_IntermediateActions_TestIdentityAction, xmof_IntermediateActions_ValueSpecificationAction, xmof_IntermediateActions_WriteLinkAction, LinkAction, IntermediateActions_LinkEndData, xmof_IntermediateActions_LinkAction, xmof_IntermediateActions_LinkEndData, IntermediateActions_xmof_EReference, xmof_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, xmof_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, xmof_IntermediateActions_ReadLinkAction, xmof_IntermediateActions_ReadSelfAction, xmof_IntermediateActions_ReadStructuralFeatureAction, xmof_IntermediateActions_LinkEndCreationData, LinkEndData, xmof_IntermediateActions_LinkEndDestructionData, xmof_IntermediateActions_ClearAssociationAction, xmof_IntermediateActions_ClearStructuralFeatureAction, xmof_IntermediateActions_CreateLinkAction, WriteLinkAction, xmof_IntermediateActions_CreateObjectAction, IntermediateActions_xmof_EClassifier, xmof_IntermediateActions_DestroyLinkAction, xmof_IntermediateActions_DestroyObjectAction, xmof_IntermediateActions_AddStructuralFeatureValueAction, xmof_CompleteActions_StartClassifierBehaviorAction, xmof_CompleteActions_StartObjectBehaviorAction, CallAction, xmof_CompleteActions_ReduceAction, xmof_CompleteActions_ReadExtentAction, CompleteActions_xmof_EClassifier, xmof_CompleteActions_ReadIsClassifiedObjectAction, xmof_CompleteActions_ReclassifyObjectAction, xmof_CompleteActions_AcceptEventAction, Communications_Trigger, xmof_BasicActions_Action, ExecutableNode, BasicActions_xmof_EClassifier, xmof_BasicActions_InputPin, Pin, xmof_BasicActions_Pin, IntermediateActivities_ObjectNode, xmof_BasicActions_CallAction, InvocationAction, xmof_BasicActions_InvocationAction, xmof_BasicActions_SendSignalAction, xmof_BasicActions_CallBehaviorAction, xmof_BasicActions_CallOperationAction, xmof_BasicActions_OutputPin, CallConcurrencyKind, ParameterDirectionKind, ExpansionKind},
    associations={classifierBehavior5, specification0, ownedParameter1, context2, ownedBehavior4, classifier15, event8, ownedAttribute9, signal10, signal11, method13, eEnumLiteral14, source23, slot16, definingFeature17, value18, owningInstance20, instance21, activity22, decisionInput43, target24, inStructuredNode26, guard28, node30, edge32, inStructuredNode34, activity36, outgoing39, incoming41, successorClause75, decisionInputFlow45, parameter47, decider49, test50, bodyOutput52, loopVariableInput55, bodyPart57, result60, loopVariable63, setupPart66, test69, body71, predecessorClause74, decider77, bodyOutput80, clause83, result84, node87, edge89, structuredNodeOutput92, structuredNodeInput94, regionAsOutput97, regionAsInput98, inputElement100, outputElement101, structuralFeature103, object104, second107, result109, first112, value115, result117, endData120, insertAt141, inputValue121, value124, end126, value128, result130, removeAt133, result135, result137, result139, insertAt158, destroyAt143, association145, object147, result150, result152, classifier154, target156, oldClassifier184, object160, object162, reducer164, result166, collection169, result172, classifier174, classifier176, result178, object181, object186, newClassifier189, result192, trigger194, output196, context198, input200, result203, argument205, target207, signal209, behavior212, target215, operation214},
    generalizations={gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior, gen_xmof_BasicBehaviors_Behavior_BehavioredEClass, gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier, gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_xmof_Communications_Trigger_ENamedElement, gen_xmof_Communications_Event_ENamedElement, gen_xmof_Communications_Signal_EClassifier, gen_xmof_Communications_SignalEvent_MessageEvent, gen_xmof_Communications_MessageEvent_Event, gen_xmof_Communications_Reception_BehavioredEOperation, gen_xmof_Kernel_BehavioredEOperation_EOperation, gen_xmof_Kernel_BehavioredEClass_EClass, gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier, gen_xmof_Kernel_MainEClass_BehavioredEClass, gen_xmof_Kernel_DirectedParameter_EParameter, gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification, gen_xmof_Kernel_ValueSpecification_ETypedElement, gen_xmof_Kernel_InstanceSpecification_ENamedElement, gen_xmof_Kernel_Slot_EModelElement, gen_xmof_Kernel_InstanceValue_ValueSpecification, gen_xmof_Kernel_LiteralBoolean_LiteralSpecification, gen_xmof_Kernel_LiteralSpecification_ValueSpecification, gen_xmof_Kernel_LiteralInteger_LiteralSpecification, gen_xmof_Kernel_LiteralNull_LiteralSpecification, gen_xmof_Kernel_LiteralString_LiteralSpecification, gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_xmof_Kernel_PrimitiveType_EDataType, gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge, gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement, gen_xmof_IntermediateActivities_Activity_Behavior, gen_xmof_IntermediateActivities_ActivityNode_ENamedElement, gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_xmof_IntermediateActivities_ObjectNode_ETypedElement, gen_xmof_IntermediateActivities_MergeNode_ControlNode, gen_xmof_IntermediateActivities_ControlNode_ActivityNode, gen_xmof_IntermediateActivities_JoinNode_ControlNode, gen_xmof_IntermediateActivities_InitialNode_ControlNode, gen_xmof_IntermediateActivities_FinalNode_ControlNode, gen_xmof_IntermediateActivities_ForkNode_ControlNode, gen_xmof_IntermediateActivities_ControlFlow_ActivityEdge, gen_xmof_IntermediateActivities_DecisionNode_ControlNode, gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode, gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_xmof_CompleteStructuredActivities_Clause_EModelElement, gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action, gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_xmof_IntermediateActions_StructuralFeatureAction_Action, gen_xmof_IntermediateActions_TestIdentityAction_Action, gen_xmof_IntermediateActions_ValueSpecificationAction_Action, gen_xmof_IntermediateActions_WriteLinkAction_LinkAction, gen_xmof_IntermediateActions_LinkEndData_EModelElement, gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_IntermediateActions_ReadLinkAction_LinkAction, gen_xmof_IntermediateActions_ReadSelfAction_Action, gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData, gen_xmof_IntermediateActions_LinkAction_Action, gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_xmof_IntermediateActions_ClearAssociationAction_Action, gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_CreateObjectAction_Action, gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_DestroyObjectAction_Action, gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action, gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction, gen_xmof_CompleteActions_ReduceAction_Action, gen_xmof_CompleteActions_ReadExtentAction_Action, gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_xmof_CompleteActions_ReclassifyObjectAction_Action, gen_xmof_CompleteActions_AcceptEventAction_Action, gen_xmof_BasicActions_Action_ExecutableNode, gen_xmof_BasicActions_InputPin_Pin, gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_xmof_BasicActions_Pin_ETypedElement, gen_xmof_BasicActions_CallAction_InvocationAction, gen_xmof_BasicActions_InvocationAction_Action, gen_xmof_BasicActions_SendSignalAction_InvocationAction, gen_xmof_BasicActions_CallBehaviorAction_CallAction, gen_xmof_BasicActions_CallOperationAction_CallAction, gen_xmof_BasicActions_OutputPin_Pin},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)