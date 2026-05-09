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
Kernel_BehavioredEOperation = Class(name="Kernel_BehavioredEOperation")
Kernel_DirectedParameter = Class(name="Kernel_DirectedParameter")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors_BehavioredClassifier")
xmof_BasicBehaviors_OpaqueBehavior = Class(name="xmof_BasicBehaviors_OpaqueBehavior")
Behavior = Class(name="Behavior")
xmof_BasicBehaviors_Behavior = Class(name="xmof_BasicBehaviors_Behavior", is_abstract=True)
BehavioredEClass = Class(name="BehavioredEClass")
xmof_Communications_Trigger = Class(name="xmof_Communications_Trigger")
ENamedElement = Class(name="ENamedElement")
Communications_Event = Class(name="Communications_Event")
xmof_Communications_Event = Class(name="xmof_Communications_Event", is_abstract=True)
xmof_Communications_Signal = Class(name="xmof_Communications_Signal")
Communications_xmof_EAttribute = Class(name="Communications_xmof_EAttribute")
xmof_BasicBehaviors_BehavioredClassifier = Class(name="xmof_BasicBehaviors_BehavioredClassifier", is_abstract=True)
EClassifier = Class(name="EClassifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors_Behavior")
xmof_BasicBehaviors_FunctionBehavior = Class(name="xmof_BasicBehaviors_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
xmof_Kernel_BehavioredEClass = Class(name="xmof_Kernel_BehavioredEClass")
EClass = Class(name="EClass")
xmof_Kernel_DirectedParameter = Class(name="xmof_Kernel_DirectedParameter")
EParameter = Class(name="EParameter")
xmof_Kernel_EEnumLiteralSpecification = Class(name="xmof_Kernel_EEnumLiteralSpecification")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_xmof_EEnumLiteral = Class(name="Kernel_xmof_EEnumLiteral")
xmof_Kernel_EnumValue = Class(name="xmof_Kernel_EnumValue")
ValueSpecification = Class(name="ValueSpecification")
Kernel_EEnumLiteralSpecification = Class(name="Kernel_EEnumLiteralSpecification")
xmof_Kernel_ValueSpecification = Class(name="xmof_Kernel_ValueSpecification", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
xmof_Communications_SignalEvent = Class(name="xmof_Communications_SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications_Signal")
xmof_Communications_MessageEvent = Class(name="xmof_Communications_MessageEvent", is_abstract=True)
Event = Class(name="Event")
xmof_Communications_Reception = Class(name="xmof_Communications_Reception")
BehavioredEOperation = Class(name="BehavioredEOperation")
xmof_Kernel_BehavioredEOperation = Class(name="xmof_Kernel_BehavioredEOperation")
EOperation = Class(name="EOperation")
xmof_Kernel_Slot = Class(name="xmof_Kernel_Slot")
EModelElement = Class(name="EModelElement")
Kernel_xmof_EStructuralFeature = Class(name="Kernel_xmof_EStructuralFeature")
xmof_Kernel_InstanceSpecification = Class(name="xmof_Kernel_InstanceSpecification")
Kernel_xmof_EClassifier = Class(name="Kernel_xmof_EClassifier")
Kernel_Slot = Class(name="Kernel_Slot")
xmof_Kernel_LiteralBoolean = Class(name="xmof_Kernel_LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
xmof_Kernel_LiteralSpecification = Class(name="xmof_Kernel_LiteralSpecification", is_abstract=True)
xmof_Kernel_LiteralInteger = Class(name="xmof_Kernel_LiteralInteger")
xmof_Kernel_LiteralNull = Class(name="xmof_Kernel_LiteralNull")
xmof_Kernel_LiteralString = Class(name="xmof_Kernel_LiteralString")
xmof_Kernel_LiteralUnlimitedNatural = Class(name="xmof_Kernel_LiteralUnlimitedNatural")
xmof_Kernel_PrimitiveType = Class(name="xmof_Kernel_PrimitiveType")
EDataType = Class(name="EDataType")
Kernel_ValueSpecification = Class(name="Kernel_ValueSpecification")
Kernel_InstanceSpecification = Class(name="Kernel_InstanceSpecification")
xmof_Kernel_InstanceValue = Class(name="xmof_Kernel_InstanceValue")
xmof_IntermediateActivities_Activity = Class(name="xmof_IntermediateActivities_Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities_ActivityEdge")
xmof_IntermediateActivities_ActivityNode = Class(name="xmof_IntermediateActivities_ActivityNode", is_abstract=True)
xmof_IntermediateActivities_ObjectFlow = Class(name="xmof_IntermediateActivities_ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
xmof_IntermediateActivities_ActivityEdge = Class(name="xmof_IntermediateActivities_ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities_Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities_ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities_StructuredActivityNode")
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
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities_Clause")
xmof_CompleteStructuredActivities_ConditionalNode = Class(name="xmof_CompleteStructuredActivities_ConditionalNode")
xmof_CompleteStructuredActivities_ExecutableNode = Class(name="xmof_CompleteStructuredActivities_ExecutableNode", is_abstract=True)
xmof_CompleteStructuredActivities_Clause = Class(name="xmof_CompleteStructuredActivities_Clause")
xmof_ExtraStructuredActivities_ExpansionNode = Class(name="xmof_ExtraStructuredActivities_ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities_ExpansionRegion")
xmof_ExtraStructuredActivities_ExpansionRegion = Class(name="xmof_ExtraStructuredActivities_ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities_ExpansionNode")
xmof_CompleteStructuredActivities_StructuredActivityNode = Class(name="xmof_CompleteStructuredActivities_StructuredActivityNode")
Action = Class(name="Action")
xmof_IntermediateActions_ValueSpecificationAction = Class(name="xmof_IntermediateActions_ValueSpecificationAction")
xmof_IntermediateActions_WriteLinkAction = Class(name="xmof_IntermediateActions_WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
xmof_IntermediateActions_LinkAction = Class(name="xmof_IntermediateActions_LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions_LinkEndData")
xmof_IntermediateActions_LinkEndData = Class(name="xmof_IntermediateActions_LinkEndData")
xmof_IntermediateActions_StructuralFeatureAction = Class(name="xmof_IntermediateActions_StructuralFeatureAction", is_abstract=True)
IntermediateActions_xmof_EStructuralFeature = Class(name="IntermediateActions_xmof_EStructuralFeature")
xmof_IntermediateActions_TestIdentityAction = Class(name="xmof_IntermediateActions_TestIdentityAction")
xmof_IntermediateActions_ReadLinkAction = Class(name="xmof_IntermediateActions_ReadLinkAction")
xmof_IntermediateActions_ReadSelfAction = Class(name="xmof_IntermediateActions_ReadSelfAction")
xmof_IntermediateActions_ReadStructuralFeatureAction = Class(name="xmof_IntermediateActions_ReadStructuralFeatureAction")
xmof_IntermediateActions_LinkEndCreationData = Class(name="xmof_IntermediateActions_LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
xmof_IntermediateActions_LinkEndDestructionData = Class(name="xmof_IntermediateActions_LinkEndDestructionData")
IntermediateActions_xmof_EReference = Class(name="IntermediateActions_xmof_EReference")
xmof_IntermediateActions_WriteStructuralFeatureAction = Class(name="xmof_IntermediateActions_WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
xmof_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
IntermediateActions_xmof_EClassifier = Class(name="IntermediateActions_xmof_EClassifier")
xmof_IntermediateActions_DestroyLinkAction = Class(name="xmof_IntermediateActions_DestroyLinkAction")
xmof_IntermediateActions_DestroyObjectAction = Class(name="xmof_IntermediateActions_DestroyObjectAction")
xmof_IntermediateActions_AddStructuralFeatureValueAction = Class(name="xmof_IntermediateActions_AddStructuralFeatureValueAction")
xmof_CompleteActions_StartClassifierBehaviorAction = Class(name="xmof_CompleteActions_StartClassifierBehaviorAction")
xmof_CompleteActions_StartObjectBehaviorAction = Class(name="xmof_CompleteActions_StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
xmof_IntermediateActions_ClearAssociationAction = Class(name="xmof_IntermediateActions_ClearAssociationAction")
xmof_IntermediateActions_ClearStructuralFeatureAction = Class(name="xmof_IntermediateActions_ClearStructuralFeatureAction")
xmof_IntermediateActions_CreateLinkAction = Class(name="xmof_IntermediateActions_CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
xmof_IntermediateActions_CreateObjectAction = Class(name="xmof_IntermediateActions_CreateObjectAction")
xmof_CompleteActions_ReadExtentAction = Class(name="xmof_CompleteActions_ReadExtentAction")
CompleteActions_xmof_EClassifier = Class(name="CompleteActions_xmof_EClassifier")
xmof_CompleteActions_ReadIsClassifiedObjectAction = Class(name="xmof_CompleteActions_ReadIsClassifiedObjectAction")
xmof_CompleteActions_ReduceAction = Class(name="xmof_CompleteActions_ReduceAction")
Communications_Trigger = Class(name="Communications_Trigger")
xmof_BasicActions_Action = Class(name="xmof_BasicActions_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
BasicActions_xmof_EClassifier = Class(name="BasicActions_xmof_EClassifier")
xmof_CompleteActions_ReclassifyObjectAction = Class(name="xmof_CompleteActions_ReclassifyObjectAction")
xmof_CompleteActions_AcceptEventAction = Class(name="xmof_CompleteActions_AcceptEventAction")
xmof_BasicActions_SendSignalAction = Class(name="xmof_BasicActions_SendSignalAction")
xmof_BasicActions_CallBehaviorAction = Class(name="xmof_BasicActions_CallBehaviorAction")
xmof_BasicActions_CallOperationAction = Class(name="xmof_BasicActions_CallOperationAction")
xmof_BasicActions_InputPin = Class(name="xmof_BasicActions_InputPin")
Pin = Class(name="Pin")
xmof_BasicActions_Pin = Class(name="xmof_BasicActions_Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities_ObjectNode")
xmof_BasicActions_CallAction = Class(name="xmof_BasicActions_CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
xmof_BasicActions_InvocationAction = Class(name="xmof_BasicActions_InvocationAction", is_abstract=True)
Kernel_xmof_EEnum = Class(name="Kernel_xmof_EEnum")
xmof_Kernel_BooleanValue = Class(name="xmof_Kernel_BooleanValue")
xmof_Kernel_Value = Class(name="xmof_Kernel_Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")
xmof_Kernel_ObjectValue = Class(name="xmof_Kernel_ObjectValue")
Kernel_xmof_EObject = Class(name="Kernel_xmof_EObject")
xmof_LociL1_SemanticVisitor = Class(name="xmof_LociL1_SemanticVisitor", is_abstract=True)
xmof_BasicActions_OutputPin = Class(name="xmof_BasicActions_OutputPin")
xmof_Kernel_PrimitiveValue = Class(name="xmof_Kernel_PrimitiveValue", is_abstract=True)
Value = Class(name="Value")
Kernel_PrimitiveType = Class(name="Kernel_PrimitiveType")
xmof_Kernel_StringValue = Class(name="xmof_Kernel_StringValue")
PrimitiveValue = Class(name="PrimitiveValue")
xmof_Kernel_IntegerValue = Class(name="xmof_Kernel_IntegerValue")
xmof_Kernel_EnumerationValue = Class(name="xmof_Kernel_EnumerationValue")
xmof_BasicBehaviors_ParameterValue = Class(name="xmof_BasicBehaviors_ParameterValue")
Kernel_Value = Class(name="Kernel_Value")
xmof_BasicBehaviors_ParameterValueDefinition = Class(name="xmof_BasicBehaviors_ParameterValueDefinition")
BasicBehaviors_ParameterValue = Class(name="BasicBehaviors_ParameterValue")

# Kernel_BehavioredEOperation class attributes and methods

# Kernel_DirectedParameter class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# xmof_BasicBehaviors_OpaqueBehavior class attributes and methods
xmof_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
xmof_BasicBehaviors_OpaqueBehavior.attributes={xmof_BasicBehaviors_OpaqueBehavior_body, xmof_BasicBehaviors_OpaqueBehavior_language}

# Behavior class attributes and methods

# xmof_BasicBehaviors_Behavior class attributes and methods
xmof_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
xmof_BasicBehaviors_Behavior.attributes={xmof_BasicBehaviors_Behavior_reentrant}

# BehavioredEClass class attributes and methods

# xmof_Communications_Trigger class attributes and methods

# ENamedElement class attributes and methods

# Communications_Event class attributes and methods

# xmof_Communications_Event class attributes and methods

# xmof_Communications_Signal class attributes and methods

# Communications_xmof_EAttribute class attributes and methods

# xmof_BasicBehaviors_BehavioredClassifier class attributes and methods

# EClassifier class attributes and methods

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

# xmof_Communications_SignalEvent class attributes and methods

# MessageEvent class attributes and methods

# Communications_Signal class attributes and methods

# xmof_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# xmof_Communications_Reception class attributes and methods

# BehavioredEOperation class attributes and methods

# xmof_Kernel_BehavioredEOperation class attributes and methods

# EOperation class attributes and methods

# xmof_Kernel_Slot class attributes and methods

# EModelElement class attributes and methods

# Kernel_xmof_EStructuralFeature class attributes and methods

# xmof_Kernel_InstanceSpecification class attributes and methods

# Kernel_xmof_EClassifier class attributes and methods

# Kernel_Slot class attributes and methods

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

# Kernel_ValueSpecification class attributes and methods

# Kernel_InstanceSpecification class attributes and methods

# xmof_Kernel_InstanceValue class attributes and methods

# xmof_IntermediateActivities_Activity class attributes and methods
xmof_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
xmof_IntermediateActivities_Activity.attributes={xmof_IntermediateActivities_Activity_readOnly}

# IntermediateActivities_ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityNode class attributes and methods

# xmof_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# xmof_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

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

# CompleteStructuredActivities_Clause class attributes and methods

# xmof_CompleteStructuredActivities_ConditionalNode class attributes and methods
xmof_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
xmof_CompleteStructuredActivities_ConditionalNode.attributes={xmof_CompleteStructuredActivities_ConditionalNode_assured, xmof_CompleteStructuredActivities_ConditionalNode_determinate}

# xmof_CompleteStructuredActivities_ExecutableNode class attributes and methods

# xmof_CompleteStructuredActivities_Clause class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# xmof_ExtraStructuredActivities_ExpansionRegion class attributes and methods
xmof_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
xmof_ExtraStructuredActivities_ExpansionRegion.attributes={xmof_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# xmof_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
xmof_CompleteStructuredActivities_StructuredActivityNode.attributes={xmof_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# xmof_IntermediateActions_ValueSpecificationAction class attributes and methods

# xmof_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# xmof_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_LinkEndData class attributes and methods

# xmof_IntermediateActions_StructuralFeatureAction class attributes and methods

# IntermediateActions_xmof_EStructuralFeature class attributes and methods

# xmof_IntermediateActions_TestIdentityAction class attributes and methods

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

# IntermediateActions_xmof_EReference class attributes and methods

# xmof_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={xmof_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

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

# xmof_IntermediateActions_ClearAssociationAction class attributes and methods

# xmof_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# xmof_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# xmof_IntermediateActions_CreateObjectAction class attributes and methods

# xmof_CompleteActions_ReadExtentAction class attributes and methods

# CompleteActions_xmof_EClassifier class attributes and methods

# xmof_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
xmof_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
xmof_CompleteActions_ReadIsClassifiedObjectAction.attributes={xmof_CompleteActions_ReadIsClassifiedObjectAction_direct}

# xmof_CompleteActions_ReduceAction class attributes and methods
xmof_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
xmof_CompleteActions_ReduceAction.attributes={xmof_CompleteActions_ReduceAction_ordered}

# Communications_Trigger class attributes and methods

# xmof_BasicActions_Action class attributes and methods
xmof_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
xmof_BasicActions_Action.attributes={xmof_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# BasicActions_xmof_EClassifier class attributes and methods

# xmof_CompleteActions_ReclassifyObjectAction class attributes and methods
xmof_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
xmof_CompleteActions_ReclassifyObjectAction.attributes={xmof_CompleteActions_ReclassifyObjectAction_replaceAll}

# xmof_CompleteActions_AcceptEventAction class attributes and methods
xmof_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
xmof_CompleteActions_AcceptEventAction.attributes={xmof_CompleteActions_AcceptEventAction_unmarshall}

# xmof_BasicActions_SendSignalAction class attributes and methods

# xmof_BasicActions_CallBehaviorAction class attributes and methods

# xmof_BasicActions_CallOperationAction class attributes and methods

# xmof_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# xmof_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# xmof_BasicActions_CallAction class attributes and methods
xmof_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
xmof_BasicActions_CallAction.attributes={xmof_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# xmof_BasicActions_InvocationAction class attributes and methods

# Kernel_xmof_EEnum class attributes and methods

# xmof_Kernel_BooleanValue class attributes and methods
xmof_Kernel_BooleanValue_value: Property = Property(name="value", type=BooleanType)
xmof_Kernel_BooleanValue.attributes={xmof_Kernel_BooleanValue_value}

# xmof_Kernel_Value class attributes and methods

# SemanticVisitor class attributes and methods

# xmof_Kernel_ObjectValue class attributes and methods

# Kernel_xmof_EObject class attributes and methods

# xmof_LociL1_SemanticVisitor class attributes and methods

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

# xmof_Kernel_EnumerationValue class attributes and methods

# xmof_BasicBehaviors_ParameterValue class attributes and methods

# Kernel_Value class attributes and methods

# xmof_BasicBehaviors_ParameterValueDefinition class attributes and methods

# BasicBehaviors_ParameterValue class attributes and methods

# Relationships
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
eEnumLiteralSpecification15: BinaryAssociation = BinaryAssociation(
    name="eEnumLiteralSpecification15",
    ends={
        Property(name="Kernel_EEnumLiteralSpecification", type=xmof_Kernel_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumValue", type=Kernel_EEnumLiteralSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="Slot", type=xmof_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance22: BinaryAssociation = BinaryAssociation(
    name="instance22",
    ends={
        Property(name="Kernel_InstanceSpecification", type=xmof_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
definingFeature18: BinaryAssociation = BinaryAssociation(
    name="definingFeature18",
    ends={
        Property(name="Kernel_xmof_EStructuralFeature", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot", type=Kernel_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="Kernel_ValueSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_Slot20", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance21: BinaryAssociation = BinaryAssociation(
    name="owningInstance21",
    ends={
        Property(name="InstanceSpecification", type=xmof_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
guard29: BinaryAssociation = BinaryAssociation(
    name="guard29",
    ends={
        Property(name="Kernel_ValueSpecification30", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node31: BinaryAssociation = BinaryAssociation(
    name="node31",
    ends={
        Property(name="ActivityNode32", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge33: BinaryAssociation = BinaryAssociation(
    name="edge33",
    ends={
        Property(name="ActivityEdge", type=xmof_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity34", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode35: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode35",
    ends={
        Property(name="StructuredActivityNode36", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity37: BinaryAssociation = BinaryAssociation(
    name="activity37",
    ends={
        Property(name="Activity39", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node38", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing40: BinaryAssociation = BinaryAssociation(
    name="outgoing40",
    ends={
        Property(name="ActivityEdge41", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity23: BinaryAssociation = BinaryAssociation(
    name="activity23",
    ends={
        Property(name="Activity", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="ActivityNode", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="ActivityNode26", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode27: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode27",
    ends={
        Property(name="StructuredActivityNode", type=xmof_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge28", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput44: BinaryAssociation = BinaryAssociation(
    name="decisionInput44",
    ends={
        Property(name="BasicBehaviors_Behavior45", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow46: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow46",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=xmof_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_DecisionNode47", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
parameter48: BinaryAssociation = BinaryAssociation(
    name="parameter48",
    ends={
        Property(name="Kernel_DirectedParameter49", type=xmof_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActivities_ActivityParameterNode", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
decider50: BinaryAssociation = BinaryAssociation(
    name="decider50",
    ends={
        Property(name="BasicActions_OutputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test51: BinaryAssociation = BinaryAssociation(
    name="test51",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode52", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput53: BinaryAssociation = BinaryAssociation(
    name="bodyOutput53",
    ends={
        Property(name="BasicActions_OutputPin55", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode54", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput56: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput56",
    ends={
        Property(name="BasicActions_InputPin", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode57", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming42: BinaryAssociation = BinaryAssociation(
    name="incoming42",
    ends={
        Property(name="ActivityEdge43", type=xmof_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
body72: BinaryAssociation = BinaryAssociation(
    name="body72",
    ends={
        Property(name="xmof_CompleteStructuredActivities_Clause73", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999)),
        Property(name="CompleteStructuredActivities_ExecutableNode74", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1))
    }
)
predecessorClause75: BinaryAssociation = BinaryAssociation(
    name="predecessorClause75",
    ends={
        Property(name="Clause", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause76: BinaryAssociation = BinaryAssociation(
    name="successorClause76",
    ends={
        Property(name="Clause77", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider78: BinaryAssociation = BinaryAssociation(
    name="decider78",
    ends={
        Property(name="BasicActions_OutputPin80", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause79", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput81: BinaryAssociation = BinaryAssociation(
    name="bodyOutput81",
    ends={
        Property(name="BasicActions_OutputPin83", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause82", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause84: BinaryAssociation = BinaryAssociation(
    name="clause84",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result85: BinaryAssociation = BinaryAssociation(
    name="result85",
    ends={
        Property(name="BasicActions_OutputPin87", type=xmof_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_ConditionalNode86", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart58: BinaryAssociation = BinaryAssociation(
    name="bodyPart58",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode60", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode59", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result61: BinaryAssociation = BinaryAssociation(
    name="result61",
    ends={
        Property(name="BasicActions_OutputPin63", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode62", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable64: BinaryAssociation = BinaryAssociation(
    name="loopVariable64",
    ends={
        Property(name="BasicActions_OutputPin66", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode65", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart67: BinaryAssociation = BinaryAssociation(
    name="setupPart67",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode69", type=xmof_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_LoopNode68", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test70: BinaryAssociation = BinaryAssociation(
    name="test70",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode71", type=xmof_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
regionAsOutput98: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput98",
    ends={
        Property(name="ExpansionRegion", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput99: BinaryAssociation = BinaryAssociation(
    name="regionAsInput99",
    ends={
        Property(name="ExpansionRegion100", type=xmof_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement101: BinaryAssociation = BinaryAssociation(
    name="inputElement101",
    ends={
        Property(name="ExpansionNode", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement102: BinaryAssociation = BinaryAssociation(
    name="outputElement102",
    ends={
        Property(name="ExpansionNode103", type=xmof_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
node88: BinaryAssociation = BinaryAssociation(
    name="node88",
    ends={
        Property(name="ActivityNode89", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge90: BinaryAssociation = BinaryAssociation(
    name="edge90",
    ends={
        Property(name="ActivityEdge92", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode91", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput93: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput93",
    ends={
        Property(name="BasicActions_OutputPin94", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput95: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput95",
    ends={
        Property(name="BasicActions_InputPin97", type=xmof_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteStructuredActivities_StructuredActivityNode96", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first113: BinaryAssociation = BinaryAssociation(
    name="first113",
    ends={
        Property(name="BasicActions_InputPin115", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction114", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value116: BinaryAssociation = BinaryAssociation(
    name="value116",
    ends={
        Property(name="Kernel_ValueSpecification117", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result118: BinaryAssociation = BinaryAssociation(
    name="result118",
    ends={
        Property(name="BasicActions_OutputPin120", type=xmof_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ValueSpecificationAction119", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData121: BinaryAssociation = BinaryAssociation(
    name="endData121",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue122: BinaryAssociation = BinaryAssociation(
    name="inputValue122",
    ends={
        Property(name="BasicActions_InputPin124", type=xmof_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkAction123", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value125: BinaryAssociation = BinaryAssociation(
    name="value125",
    ends={
        Property(name="BasicActions_InputPin126", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
structuralFeature104: BinaryAssociation = BinaryAssociation(
    name="structuralFeature104",
    ends={
        Property(name="IntermediateActions_xmof_EStructuralFeature", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction", type=IntermediateActions_xmof_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object105: BinaryAssociation = BinaryAssociation(
    name="object105",
    ends={
        Property(name="BasicActions_InputPin107", type=xmof_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_StructuralFeatureAction106", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second108: BinaryAssociation = BinaryAssociation(
    name="second108",
    ends={
        Property(name="BasicActions_InputPin109", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result110: BinaryAssociation = BinaryAssociation(
    name="result110",
    ends={
        Property(name="BasicActions_OutputPin112", type=xmof_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_TestIdentityAction111", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result136: BinaryAssociation = BinaryAssociation(
    name="result136",
    ends={
        Property(name="BasicActions_OutputPin137", type=xmof_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result138: BinaryAssociation = BinaryAssociation(
    name="result138",
    ends={
        Property(name="BasicActions_OutputPin139", type=xmof_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result140: BinaryAssociation = BinaryAssociation(
    name="result140",
    ends={
        Property(name="BasicActions_OutputPin141", type=xmof_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt142: BinaryAssociation = BinaryAssociation(
    name="insertAt142",
    ends={
        Property(name="BasicActions_InputPin143", type=xmof_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt144: BinaryAssociation = BinaryAssociation(
    name="destroyAt144",
    ends={
        Property(name="BasicActions_InputPin145", type=xmof_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end127: BinaryAssociation = BinaryAssociation(
    name="end127",
    ends={
        Property(name="IntermediateActions_xmof_EReference", type=xmof_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_LinkEndData128", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
value129: BinaryAssociation = BinaryAssociation(
    name="value129",
    ends={
        Property(name="BasicActions_InputPin130", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result131: BinaryAssociation = BinaryAssociation(
    name="result131",
    ends={
        Property(name="BasicActions_OutputPin133", type=xmof_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_WriteStructuralFeatureAction132", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt134: BinaryAssociation = BinaryAssociation(
    name="removeAt134",
    ends={
        Property(name="BasicActions_InputPin135", type=xmof_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier155: BinaryAssociation = BinaryAssociation(
    name="classifier155",
    ends={
        Property(name="IntermediateActions_xmof_EClassifier", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction156", type=IntermediateActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
target157: BinaryAssociation = BinaryAssociation(
    name="target157",
    ends={
        Property(name="BasicActions_InputPin158", type=xmof_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt159: BinaryAssociation = BinaryAssociation(
    name="insertAt159",
    ends={
        Property(name="BasicActions_InputPin160", type=xmof_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object161: BinaryAssociation = BinaryAssociation(
    name="object161",
    ends={
        Property(name="BasicActions_InputPin162", type=xmof_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association146: BinaryAssociation = BinaryAssociation(
    name="association146",
    ends={
        Property(name="IntermediateActions_xmof_EReference147", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction", type=IntermediateActions_xmof_EReference, multiplicity=Multiplicity(1, 1))
    }
)
object148: BinaryAssociation = BinaryAssociation(
    name="object148",
    ends={
        Property(name="BasicActions_InputPin150", type=xmof_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearAssociationAction149", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result151: BinaryAssociation = BinaryAssociation(
    name="result151",
    ends={
        Property(name="BasicActions_OutputPin152", type=xmof_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result153: BinaryAssociation = BinaryAssociation(
    name="result153",
    ends={
        Property(name="BasicActions_OutputPin154", type=xmof_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result173: BinaryAssociation = BinaryAssociation(
    name="result173",
    ends={
        Property(name="BasicActions_OutputPin174", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier175: BinaryAssociation = BinaryAssociation(
    name="classifier175",
    ends={
        Property(name="CompleteActions_xmof_EClassifier", type=xmof_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadExtentAction176", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier177: BinaryAssociation = BinaryAssociation(
    name="classifier177",
    ends={
        Property(name="CompleteActions_xmof_EClassifier178", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result179: BinaryAssociation = BinaryAssociation(
    name="result179",
    ends={
        Property(name="BasicActions_OutputPin181", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction180", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object163: BinaryAssociation = BinaryAssociation(
    name="object163",
    ends={
        Property(name="BasicActions_InputPin164", type=xmof_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer165: BinaryAssociation = BinaryAssociation(
    name="reducer165",
    ends={
        Property(name="BasicBehaviors_Behavior166", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result167: BinaryAssociation = BinaryAssociation(
    name="result167",
    ends={
        Property(name="BasicActions_OutputPin169", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction168", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection170: BinaryAssociation = BinaryAssociation(
    name="collection170",
    ends={
        Property(name="BasicActions_InputPin172", type=xmof_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReduceAction171", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result193: BinaryAssociation = BinaryAssociation(
    name="result193",
    ends={
        Property(name="BasicActions_OutputPin194", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger195: BinaryAssociation = BinaryAssociation(
    name="trigger195",
    ends={
        Property(name="Communications_Trigger", type=xmof_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_AcceptEventAction196", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output197: BinaryAssociation = BinaryAssociation(
    name="output197",
    ends={
        Property(name="BasicActions_OutputPin198", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context199: BinaryAssociation = BinaryAssociation(
    name="context199",
    ends={
        Property(name="BasicActions_xmof_EClassifier", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action200", type=BasicActions_xmof_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
object182: BinaryAssociation = BinaryAssociation(
    name="object182",
    ends={
        Property(name="BasicActions_InputPin184", type=xmof_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReadIsClassifiedObjectAction183", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier185: BinaryAssociation = BinaryAssociation(
    name="oldClassifier185",
    ends={
        Property(name="CompleteActions_xmof_EClassifier186", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
object187: BinaryAssociation = BinaryAssociation(
    name="object187",
    ends={
        Property(name="BasicActions_InputPin189", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction188", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier190: BinaryAssociation = BinaryAssociation(
    name="newClassifier190",
    ends={
        Property(name="CompleteActions_xmof_EClassifier192", type=xmof_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_CompleteActions_ReclassifyObjectAction191", type=CompleteActions_xmof_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
target208: BinaryAssociation = BinaryAssociation(
    name="target208",
    ends={
        Property(name="BasicActions_InputPin209", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal210: BinaryAssociation = BinaryAssociation(
    name="signal210",
    ends={
        Property(name="Communications_Signal212", type=xmof_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_SendSignalAction211", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior213: BinaryAssociation = BinaryAssociation(
    name="behavior213",
    ends={
        Property(name="BasicBehaviors_Behavior214", type=xmof_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation215: BinaryAssociation = BinaryAssociation(
    name="operation215",
    ends={
        Property(name="Kernel_BehavioredEOperation", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction", type=Kernel_BehavioredEOperation, multiplicity=Multiplicity(1, 1))
    }
)
target216: BinaryAssociation = BinaryAssociation(
    name="target216",
    ends={
        Property(name="BasicActions_InputPin218", type=xmof_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallOperationAction217", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
input201: BinaryAssociation = BinaryAssociation(
    name="input201",
    ends={
        Property(name="BasicActions_InputPin203", type=xmof_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_Action202", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result204: BinaryAssociation = BinaryAssociation(
    name="result204",
    ends={
        Property(name="BasicActions_OutputPin205", type=xmof_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument206: BinaryAssociation = BinaryAssociation(
    name="argument206",
    ends={
        Property(name="BasicActions_InputPin207", type=xmof_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal220: BinaryAssociation = BinaryAssociation(
    name="literal220",
    ends={
        Property(name="Kernel_xmof_EEnumLiteral221", type=xmof_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumerationValue", type=Kernel_xmof_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type222: BinaryAssociation = BinaryAssociation(
    name="type222",
    ends={
        Property(name="Kernel_xmof_EEnum", type=xmof_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_EnumerationValue223", type=Kernel_xmof_EEnum, multiplicity=Multiplicity(1, 1))
    }
)
eObject224: BinaryAssociation = BinaryAssociation(
    name="eObject224",
    ends={
        Property(name="Kernel_xmof_EObject", type=xmof_Kernel_ObjectValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_ObjectValue", type=Kernel_xmof_EObject, multiplicity=Multiplicity(1, 1))
    }
)
type219: BinaryAssociation = BinaryAssociation(
    name="type219",
    ends={
        Property(name="Kernel_PrimitiveType", type=xmof_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
parameter225: BinaryAssociation = BinaryAssociation(
    name="parameter225",
    ends={
        Property(name="Kernel_DirectedParameter226", type=xmof_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValue", type=Kernel_DirectedParameter, multiplicity=Multiplicity(1, 1))
    }
)
values227: BinaryAssociation = BinaryAssociation(
    name="values227",
    ends={
        Property(name="Kernel_Value", type=xmof_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValue228", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValues229: BinaryAssociation = BinaryAssociation(
    name="parameterValues229",
    ends={
        Property(name="BasicBehaviors_ParameterValue", type=xmof_BasicBehaviors_ParameterValueDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="xmof_BasicBehaviors_ParameterValueDefinition", type=BasicBehaviors_ParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=xmof_BasicBehaviors_OpaqueBehavior)
gen_xmof_BasicBehaviors_Behavior_BehavioredEClass = Generalization(general=BehavioredEClass, specific=xmof_BasicBehaviors_Behavior)
gen_xmof_Communications_Trigger_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Trigger)
gen_xmof_Communications_Event_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Communications_Event)
gen_xmof_Communications_Signal_EClassifier = Generalization(general=EClassifier, specific=xmof_Communications_Signal)
gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier = Generalization(general=EClassifier, specific=xmof_BasicBehaviors_BehavioredClassifier)
gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=xmof_BasicBehaviors_FunctionBehavior)
gen_xmof_Kernel_BehavioredEClass_EClass = Generalization(general=EClass, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier = Generalization(general=BasicBehaviors_BehavioredClassifier, specific=xmof_Kernel_BehavioredEClass)
gen_xmof_Kernel_DirectedParameter_EParameter = Generalization(general=EParameter, specific=xmof_Kernel_DirectedParameter)
gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification = Generalization(general=InstanceSpecification, specific=xmof_Kernel_EEnumLiteralSpecification)
gen_xmof_Kernel_EnumValue_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_EnumValue)
gen_xmof_Kernel_ValueSpecification_ETypedElement = Generalization(general=ETypedElement, specific=xmof_Kernel_ValueSpecification)
gen_xmof_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=xmof_Communications_SignalEvent)
gen_xmof_Communications_MessageEvent_Event = Generalization(general=Event, specific=xmof_Communications_MessageEvent)
gen_xmof_Communications_Reception_BehavioredEOperation = Generalization(general=BehavioredEOperation, specific=xmof_Communications_Reception)
gen_xmof_Kernel_BehavioredEOperation_EOperation = Generalization(general=EOperation, specific=xmof_Kernel_BehavioredEOperation)
gen_xmof_Kernel_Slot_EModelElement = Generalization(general=EModelElement, specific=xmof_Kernel_Slot)
gen_xmof_Kernel_InstanceSpecification_ENamedElement = Generalization(general=ENamedElement, specific=xmof_Kernel_InstanceSpecification)
gen_xmof_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralBoolean)
gen_xmof_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_LiteralSpecification)
gen_xmof_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralInteger)
gen_xmof_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralNull)
gen_xmof_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralString)
gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=xmof_Kernel_LiteralUnlimitedNatural)
gen_xmof_Kernel_PrimitiveType_EDataType = Generalization(general=EDataType, specific=xmof_Kernel_PrimitiveType)
gen_xmof_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=xmof_Kernel_InstanceValue)
gen_xmof_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=xmof_IntermediateActivities_Activity)
gen_xmof_IntermediateActivities_ActivityNode_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityNode)
gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=xmof_IntermediateActivities_ObjectFlow)
gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement = Generalization(general=ENamedElement, specific=xmof_IntermediateActivities_ActivityEdge)
gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=xmof_IntermediateActivities_ActivityFinalNode)
gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=xmof_IntermediateActivities_ActivityParameterNode)
gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_CompleteStructuredActivities_LoopNode)
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
gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_CompleteStructuredActivities_ConditionalNode)
gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=xmof_CompleteStructuredActivities_ExecutableNode)
gen_xmof_CompleteStructuredActivities_Clause_EModelElement = Generalization(general=EModelElement, specific=xmof_CompleteStructuredActivities_Clause)
gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=xmof_ExtraStructuredActivities_ExpansionNode)
gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=xmof_ExtraStructuredActivities_ExpansionRegion)
gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=xmof_CompleteStructuredActivities_StructuredActivityNode)
gen_xmof_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ValueSpecificationAction)
gen_xmof_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_WriteLinkAction)
gen_xmof_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_LinkAction)
gen_xmof_IntermediateActions_LinkEndData_EModelElement = Generalization(general=EModelElement, specific=xmof_IntermediateActions_LinkEndData)
gen_xmof_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_StructuralFeatureAction)
gen_xmof_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_TestIdentityAction)
gen_xmof_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=xmof_IntermediateActions_ReadLinkAction)
gen_xmof_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ReadSelfAction)
gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ReadStructuralFeatureAction)
gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndCreationData)
gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=xmof_IntermediateActions_LinkEndDestructionData)
gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_WriteStructuralFeatureAction)
gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_DestroyLinkAction)
gen_xmof_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_DestroyObjectAction)
gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=xmof_IntermediateActions_AddStructuralFeatureValueAction)
gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_StartClassifierBehaviorAction)
gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_CompleteActions_StartObjectBehaviorAction)
gen_xmof_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_ClearAssociationAction)
gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=xmof_IntermediateActions_ClearStructuralFeatureAction)
gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=xmof_IntermediateActions_CreateLinkAction)
gen_xmof_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=xmof_IntermediateActions_CreateObjectAction)
gen_xmof_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadExtentAction)
gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReadIsClassifiedObjectAction)
gen_xmof_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReduceAction)
gen_xmof_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=xmof_BasicActions_Action)
gen_xmof_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_ReclassifyObjectAction)
gen_xmof_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=xmof_CompleteActions_AcceptEventAction)
gen_xmof_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_SendSignalAction)
gen_xmof_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallBehaviorAction)
gen_xmof_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=xmof_BasicActions_CallOperationAction)
gen_xmof_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_InputPin)
gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_Pin_ETypedElement = Generalization(general=ETypedElement, specific=xmof_BasicActions_Pin)
gen_xmof_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=xmof_BasicActions_CallAction)
gen_xmof_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=xmof_BasicActions_InvocationAction)
gen_xmof_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_BooleanValue)
gen_xmof_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=xmof_Kernel_Value)
gen_xmof_Kernel_ObjectValue_Value = Generalization(general=Value, specific=xmof_Kernel_ObjectValue)
gen_xmof_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=xmof_BasicActions_OutputPin)
gen_xmof_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=xmof_Kernel_PrimitiveValue)
gen_xmof_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_StringValue)
gen_xmof_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=xmof_Kernel_IntegerValue)
gen_xmof_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=xmof_Kernel_EnumerationValue)

# Domain Model
domain_model = DomainModel(
    name="xmof",
    types={Kernel_BehavioredEOperation, Kernel_DirectedParameter, BasicBehaviors_BehavioredClassifier, xmof_BasicBehaviors_OpaqueBehavior, Behavior, xmof_BasicBehaviors_Behavior, BehavioredEClass, xmof_Communications_Trigger, ENamedElement, Communications_Event, xmof_Communications_Event, xmof_Communications_Signal, Communications_xmof_EAttribute, xmof_BasicBehaviors_BehavioredClassifier, EClassifier, BasicBehaviors_Behavior, xmof_BasicBehaviors_FunctionBehavior, OpaqueBehavior, xmof_Kernel_BehavioredEClass, EClass, xmof_Kernel_DirectedParameter, EParameter, xmof_Kernel_EEnumLiteralSpecification, InstanceSpecification, Kernel_xmof_EEnumLiteral, xmof_Kernel_EnumValue, ValueSpecification, Kernel_EEnumLiteralSpecification, xmof_Kernel_ValueSpecification, ETypedElement, xmof_Communications_SignalEvent, MessageEvent, Communications_Signal, xmof_Communications_MessageEvent, Event, xmof_Communications_Reception, BehavioredEOperation, xmof_Kernel_BehavioredEOperation, EOperation, xmof_Kernel_Slot, EModelElement, Kernel_xmof_EStructuralFeature, xmof_Kernel_InstanceSpecification, Kernel_xmof_EClassifier, Kernel_Slot, xmof_Kernel_LiteralBoolean, LiteralSpecification, xmof_Kernel_LiteralSpecification, xmof_Kernel_LiteralInteger, xmof_Kernel_LiteralNull, xmof_Kernel_LiteralString, xmof_Kernel_LiteralUnlimitedNatural, xmof_Kernel_PrimitiveType, EDataType, Kernel_ValueSpecification, Kernel_InstanceSpecification, xmof_Kernel_InstanceValue, xmof_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, xmof_IntermediateActivities_ActivityNode, xmof_IntermediateActivities_ObjectFlow, ActivityEdge, xmof_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, IntermediateActivities_ObjectFlow, xmof_IntermediateActivities_ActivityFinalNode, FinalNode, xmof_IntermediateActivities_ActivityParameterNode, ObjectNode, xmof_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, xmof_IntermediateActivities_ObjectNode, xmof_IntermediateActivities_MergeNode, ControlNode, xmof_IntermediateActivities_ControlNode, ActivityNode, xmof_IntermediateActivities_JoinNode, xmof_IntermediateActivities_InitialNode, xmof_IntermediateActivities_FinalNode, xmof_IntermediateActivities_ForkNode, xmof_IntermediateActivities_ControlFlow, xmof_IntermediateActivities_DecisionNode, CompleteStructuredActivities_Clause, xmof_CompleteStructuredActivities_ConditionalNode, xmof_CompleteStructuredActivities_ExecutableNode, xmof_CompleteStructuredActivities_Clause, xmof_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, xmof_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, xmof_CompleteStructuredActivities_StructuredActivityNode, Action, xmof_IntermediateActions_ValueSpecificationAction, xmof_IntermediateActions_WriteLinkAction, LinkAction, xmof_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, xmof_IntermediateActions_LinkEndData, xmof_IntermediateActions_StructuralFeatureAction, IntermediateActions_xmof_EStructuralFeature, xmof_IntermediateActions_TestIdentityAction, xmof_IntermediateActions_ReadLinkAction, xmof_IntermediateActions_ReadSelfAction, xmof_IntermediateActions_ReadStructuralFeatureAction, xmof_IntermediateActions_LinkEndCreationData, LinkEndData, xmof_IntermediateActions_LinkEndDestructionData, IntermediateActions_xmof_EReference, xmof_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, xmof_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, IntermediateActions_xmof_EClassifier, xmof_IntermediateActions_DestroyLinkAction, xmof_IntermediateActions_DestroyObjectAction, xmof_IntermediateActions_AddStructuralFeatureValueAction, xmof_CompleteActions_StartClassifierBehaviorAction, xmof_CompleteActions_StartObjectBehaviorAction, CallAction, xmof_IntermediateActions_ClearAssociationAction, xmof_IntermediateActions_ClearStructuralFeatureAction, xmof_IntermediateActions_CreateLinkAction, WriteLinkAction, xmof_IntermediateActions_CreateObjectAction, xmof_CompleteActions_ReadExtentAction, CompleteActions_xmof_EClassifier, xmof_CompleteActions_ReadIsClassifiedObjectAction, xmof_CompleteActions_ReduceAction, Communications_Trigger, xmof_BasicActions_Action, ExecutableNode, BasicActions_xmof_EClassifier, xmof_CompleteActions_ReclassifyObjectAction, xmof_CompleteActions_AcceptEventAction, xmof_BasicActions_SendSignalAction, xmof_BasicActions_CallBehaviorAction, xmof_BasicActions_CallOperationAction, xmof_BasicActions_InputPin, Pin, xmof_BasicActions_Pin, IntermediateActivities_ObjectNode, xmof_BasicActions_CallAction, InvocationAction, xmof_BasicActions_InvocationAction, Kernel_xmof_EEnum, xmof_Kernel_BooleanValue, xmof_Kernel_Value, SemanticVisitor, xmof_Kernel_ObjectValue, Kernel_xmof_EObject, xmof_LociL1_SemanticVisitor, xmof_BasicActions_OutputPin, xmof_Kernel_PrimitiveValue, Value, Kernel_PrimitiveType, xmof_Kernel_StringValue, PrimitiveValue, xmof_Kernel_IntegerValue, xmof_Kernel_EnumerationValue, xmof_BasicBehaviors_ParameterValue, Kernel_Value, xmof_BasicBehaviors_ParameterValueDefinition, BasicBehaviors_ParameterValue, CallConcurrencyKind, ParameterDirectionKind, ExpansionKind},
    associations={specification0, ownedParameter1, context2, event8, ownedAttribute9, ownedBehavior4, classifierBehavior5, method13, eEnumLiteral14, eEnumLiteralSpecification15, signal10, signal11, classifier16, slot17, instance22, definingFeature18, value19, owningInstance21, guard29, node31, edge33, inStructuredNode35, activity37, outgoing40, activity23, source24, target25, inStructuredNode27, decisionInput44, decisionInputFlow46, parameter48, decider50, test51, bodyOutput53, loopVariableInput56, incoming42, body72, predecessorClause75, successorClause76, decider78, bodyOutput81, clause84, result85, bodyPart58, result61, loopVariable64, setupPart67, test70, regionAsOutput98, regionAsInput99, inputElement101, outputElement102, node88, edge90, structuredNodeOutput93, structuredNodeInput95, first113, value116, result118, endData121, inputValue122, value125, structuralFeature104, object105, second108, result110, result136, result138, result140, insertAt142, destroyAt144, end127, value129, result131, removeAt134, classifier155, target157, insertAt159, object161, association146, object148, result151, result153, result173, classifier175, classifier177, result179, object163, reducer165, result167, collection170, result193, trigger195, output197, context199, object182, oldClassifier185, object187, newClassifier190, target208, signal210, behavior213, operation215, target216, input201, result204, argument206, literal220, type222, eObject224, type219, parameter225, values227, parameterValues229},
    generalizations={gen_xmof_BasicBehaviors_OpaqueBehavior_Behavior, gen_xmof_BasicBehaviors_Behavior_BehavioredEClass, gen_xmof_Communications_Trigger_ENamedElement, gen_xmof_Communications_Event_ENamedElement, gen_xmof_Communications_Signal_EClassifier, gen_xmof_BasicBehaviors_BehavioredClassifier_EClassifier, gen_xmof_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_xmof_Kernel_BehavioredEClass_EClass, gen_xmof_Kernel_BehavioredEClass_BasicBehaviors_BehavioredClassifier, gen_xmof_Kernel_DirectedParameter_EParameter, gen_xmof_Kernel_EEnumLiteralSpecification_InstanceSpecification, gen_xmof_Kernel_EnumValue_ValueSpecification, gen_xmof_Kernel_ValueSpecification_ETypedElement, gen_xmof_Communications_SignalEvent_MessageEvent, gen_xmof_Communications_MessageEvent_Event, gen_xmof_Communications_Reception_BehavioredEOperation, gen_xmof_Kernel_BehavioredEOperation_EOperation, gen_xmof_Kernel_Slot_EModelElement, gen_xmof_Kernel_InstanceSpecification_ENamedElement, gen_xmof_Kernel_LiteralBoolean_LiteralSpecification, gen_xmof_Kernel_LiteralSpecification_ValueSpecification, gen_xmof_Kernel_LiteralInteger_LiteralSpecification, gen_xmof_Kernel_LiteralNull_LiteralSpecification, gen_xmof_Kernel_LiteralString_LiteralSpecification, gen_xmof_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_xmof_Kernel_PrimitiveType_EDataType, gen_xmof_Kernel_InstanceValue_ValueSpecification, gen_xmof_IntermediateActivities_Activity_Behavior, gen_xmof_IntermediateActivities_ActivityNode_ENamedElement, gen_xmof_IntermediateActivities_ObjectFlow_ActivityEdge, gen_xmof_IntermediateActivities_ActivityEdge_ENamedElement, gen_xmof_IntermediateActivities_ActivityFinalNode_FinalNode, gen_xmof_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_xmof_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_xmof_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_xmof_IntermediateActivities_ObjectNode_ETypedElement, gen_xmof_IntermediateActivities_MergeNode_ControlNode, gen_xmof_IntermediateActivities_ControlNode_ActivityNode, gen_xmof_IntermediateActivities_JoinNode_ControlNode, gen_xmof_IntermediateActivities_InitialNode_ControlNode, gen_xmof_IntermediateActivities_FinalNode_ControlNode, gen_xmof_IntermediateActivities_ForkNode_ControlNode, gen_xmof_IntermediateActivities_ControlFlow_ActivityEdge, gen_xmof_IntermediateActivities_DecisionNode_ControlNode, gen_xmof_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_xmof_CompleteStructuredActivities_Clause_EModelElement, gen_xmof_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_xmof_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_xmof_CompleteStructuredActivities_StructuredActivityNode_Action, gen_xmof_IntermediateActions_ValueSpecificationAction_Action, gen_xmof_IntermediateActions_WriteLinkAction_LinkAction, gen_xmof_IntermediateActions_LinkAction_Action, gen_xmof_IntermediateActions_LinkEndData_EModelElement, gen_xmof_IntermediateActions_StructuralFeatureAction_Action, gen_xmof_IntermediateActions_TestIdentityAction_Action, gen_xmof_IntermediateActions_ReadLinkAction_LinkAction, gen_xmof_IntermediateActions_ReadSelfAction_Action, gen_xmof_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_LinkEndCreationData_LinkEndData, gen_xmof_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_xmof_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_DestroyObjectAction_Action, gen_xmof_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_xmof_CompleteActions_StartClassifierBehaviorAction_Action, gen_xmof_CompleteActions_StartObjectBehaviorAction_CallAction, gen_xmof_IntermediateActions_ClearAssociationAction_Action, gen_xmof_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_xmof_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_xmof_IntermediateActions_CreateObjectAction_Action, gen_xmof_CompleteActions_ReadExtentAction_Action, gen_xmof_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_xmof_CompleteActions_ReduceAction_Action, gen_xmof_BasicActions_Action_ExecutableNode, gen_xmof_CompleteActions_ReclassifyObjectAction_Action, gen_xmof_CompleteActions_AcceptEventAction_Action, gen_xmof_BasicActions_SendSignalAction_InvocationAction, gen_xmof_BasicActions_CallBehaviorAction_CallAction, gen_xmof_BasicActions_CallOperationAction_CallAction, gen_xmof_BasicActions_InputPin_Pin, gen_xmof_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_xmof_BasicActions_Pin_ETypedElement, gen_xmof_BasicActions_CallAction_InvocationAction, gen_xmof_BasicActions_InvocationAction_Action, gen_xmof_Kernel_BooleanValue_PrimitiveValue, gen_xmof_Kernel_Value_SemanticVisitor, gen_xmof_Kernel_ObjectValue_Value, gen_xmof_BasicActions_OutputPin_Pin, gen_xmof_Kernel_PrimitiveValue_Value, gen_xmof_Kernel_StringValue_PrimitiveValue, gen_xmof_Kernel_IntegerValue_PrimitiveValue, gen_xmof_Kernel_EnumerationValue_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)