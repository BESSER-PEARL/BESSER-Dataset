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

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
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

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
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
fUML_BasicBehaviors_OpaqueBehavior = Class(name="fUML_BasicBehaviors_OpaqueBehavior")
Behavior = Class(name="Behavior")
fUML_BasicBehaviors_Behavior = Class(name="fUML_BasicBehaviors_Behavior", is_abstract=True)
Class_ = Class(name="Class")
Kernel_BehavioralFeature = Class(name="Kernel_BehavioralFeature")
Kernel_Parameter = Class(name="Kernel_Parameter")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors_BehavioredClassifier")
fUML_BasicBehaviors_BehavioredClassifier = Class(name="fUML_BasicBehaviors_BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors_Behavior")
fUML_BasicBehaviors_FunctionBehavior = Class(name="fUML_BasicBehaviors_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
fUML_Communications_Trigger = Class(name="fUML_Communications_Trigger")
NamedElement = Class(name="NamedElement")
Communications_Event = Class(name="Communications_Event")
fUML_Communications_Event = Class(name="fUML_Communications_Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
fUML_Communications_Signal = Class(name="fUML_Communications_Signal")
Kernel_Property = Class(name="Kernel_Property")
fUML_Communications_SignalEvent = Class(name="fUML_Communications_SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications_Signal")
fUML_Communications_MessageEvent = Class(name="fUML_Communications_MessageEvent", is_abstract=True)
Event = Class(name="Event")
fUML_Communications_Reception = Class(name="fUML_Communications_Reception")
BehavioralFeature = Class(name="BehavioralFeature")
fUML_Kernel_ValueSpecification = Class(name="fUML_Kernel_ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
fUML_Kernel_TypedElement = Class(name="fUML_Kernel_TypedElement")
Kernel_Type = Class(name="Kernel_Type")
fUML_Kernel_NamedElement = Class(name="fUML_Kernel_NamedElement", is_abstract=True)
Element = Class(name="Element")
Kernel_Namespace = Class(name="Kernel_Namespace")
Kernel_Element = Class(name="Kernel_Element")
Kernel_Comment = Class(name="Kernel_Comment")
fUML_Kernel_Comment = Class(name="fUML_Kernel_Comment")
fUML_Kernel_Namespace = Class(name="fUML_Kernel_Namespace", is_abstract=True)
Kernel_NamedElement = Class(name="Kernel_NamedElement")
Kernel_ElementImport = Class(name="Kernel_ElementImport")
Kernel_PackageImport = Class(name="Kernel_PackageImport")
Kernel_PackageableElement = Class(name="Kernel_PackageableElement")
fUML_Kernel_ElementImport = Class(name="fUML_Kernel_ElementImport")
fUML_Kernel_PackageableElement = Class(name="fUML_Kernel_PackageableElement", is_abstract=True)
fUML_Kernel_PackageImport = Class(name="fUML_Kernel_PackageImport")
Kernel_Package = Class(name="Kernel_Package")
fUML_Kernel_Package = Class(name="fUML_Kernel_Package")
fUML_Kernel_Element = Class(name="fUML_Kernel_Element", is_abstract=True)
fUML_Kernel_Type = Class(name="fUML_Kernel_Type", is_abstract=True)
fUML_Kernel_StructuralFeature = Class(name="fUML_Kernel_StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel_Feature")
Kernel_MultiplicityElement = Class(name="Kernel_MultiplicityElement")
Kernel_TypedElement = Class(name="Kernel_TypedElement")
fUML_Kernel_Feature = Class(name="fUML_Kernel_Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Kernel_Classifier = Class(name="Kernel_Classifier")
fUML_Kernel_RedefinableElement = Class(name="fUML_Kernel_RedefinableElement", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel_RedefinableElement")
fUML_Kernel_Classifier = Class(name="fUML_Kernel_Classifier", is_abstract=True)
Kernel_Generalization = Class(name="Kernel_Generalization")
fUML_Kernel_Generalization = Class(name="fUML_Kernel_Generalization")
fUML_Kernel_Property = Class(name="fUML_Kernel_Property")
StructuralFeature = Class(name="StructuralFeature")
Kernel_Association = Class(name="Kernel_Association")
Kernel_DataType = Class(name="Kernel_DataType")
Kernel_Class = Class(name="Kernel_Class")
Kernel_ValueSpecification = Class(name="Kernel_ValueSpecification")
fUML_Kernel_Association = Class(name="fUML_Kernel_Association")
fUML_Kernel_DataType = Class(name="fUML_Kernel_DataType")
fUML_Kernel_MultiplicityElement = Class(name="fUML_Kernel_MultiplicityElement")
fUML_Kernel_BehavioralFeature = Class(name="fUML_Kernel_BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
fUML_Kernel_Parameter = Class(name="fUML_Kernel_Parameter")
fUML_Kernel_Operation = Class(name="fUML_Kernel_Operation")
fUML_Kernel_PrimitiveType = Class(name="fUML_Kernel_PrimitiveType")
DataType = Class(name="DataType")
fUML_Kernel_Enumeration = Class(name="fUML_Kernel_Enumeration")
Kernel_Operation = Class(name="Kernel_Operation")
fUML_Kernel_InstanceSpecification = Class(name="fUML_Kernel_InstanceSpecification")
Kernel_Slot = Class(name="Kernel_Slot")
fUML_Kernel_Slot = Class(name="fUML_Kernel_Slot")
Kernel_StructuralFeature = Class(name="Kernel_StructuralFeature")
Kernel_InstanceSpecification = Class(name="Kernel_InstanceSpecification")
fUML_Kernel_InstanceValue = Class(name="fUML_Kernel_InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
fUML_Kernel_LiteralBoolean = Class(name="fUML_Kernel_LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
fUML_Kernel_LiteralSpecification = Class(name="fUML_Kernel_LiteralSpecification", is_abstract=True)
fUML_Kernel_LiteralInteger = Class(name="fUML_Kernel_LiteralInteger")
fUML_Kernel_LiteralNull = Class(name="fUML_Kernel_LiteralNull")
fUML_Kernel_LiteralString = Class(name="fUML_Kernel_LiteralString")
fUML_Kernel_LiteralUnlimitedNatural = Class(name="fUML_Kernel_LiteralUnlimitedNatural")
Kernel_EnumerationLiteral = Class(name="Kernel_EnumerationLiteral")
fUML_Kernel_EnumerationLiteral = Class(name="fUML_Kernel_EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_Enumeration = Class(name="Kernel_Enumeration")
fUML_Kernel_Class = Class(name="fUML_Kernel_Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
Communications_Reception = Class(name="Communications_Reception")
fUML_IntermediateActivities_ObjectFlow = Class(name="fUML_IntermediateActivities_ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
fUML_IntermediateActivities_ActivityEdge = Class(name="fUML_IntermediateActivities_ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities_Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities_ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities_StructuredActivityNode")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities_ObjectFlow")
fUML_IntermediateActivities_ActivityFinalNode = Class(name="fUML_IntermediateActivities_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
fUML_IntermediateActivities_Activity = Class(name="fUML_IntermediateActivities_Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities_ActivityEdge")
fUML_IntermediateActivities_ActivityNode = Class(name="fUML_IntermediateActivities_ActivityNode", is_abstract=True)
fUML_IntermediateActivities_ObjectNode = Class(name="fUML_IntermediateActivities_ObjectNode", is_abstract=True)
fUML_IntermediateActivities_MergeNode = Class(name="fUML_IntermediateActivities_MergeNode")
ControlNode = Class(name="ControlNode")
fUML_IntermediateActivities_ControlNode = Class(name="fUML_IntermediateActivities_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
fUML_IntermediateActivities_JoinNode = Class(name="fUML_IntermediateActivities_JoinNode")
fUML_IntermediateActivities_InitialNode = Class(name="fUML_IntermediateActivities_InitialNode")
fUML_IntermediateActivities_FinalNode = Class(name="fUML_IntermediateActivities_FinalNode", is_abstract=True)
fUML_IntermediateActivities_ForkNode = Class(name="fUML_IntermediateActivities_ForkNode")
fUML_IntermediateActivities_ControlFlow = Class(name="fUML_IntermediateActivities_ControlFlow")
fUML_IntermediateActivities_DecisionNode = Class(name="fUML_IntermediateActivities_DecisionNode")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities_Clause")
fUML_IntermediateActivities_ActivityParameterNode = Class(name="fUML_IntermediateActivities_ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
fUML_CompleteStructuredActivities_LoopNode = Class(name="fUML_CompleteStructuredActivities_LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions_OutputPin")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities_ExecutableNode")
BasicActions_InputPin = Class(name="BasicActions_InputPin")
fUML_CompleteStructuredActivities_ExecutableNode = Class(name="fUML_CompleteStructuredActivities_ExecutableNode", is_abstract=True)
fUML_CompleteStructuredActivities_Clause = Class(name="fUML_CompleteStructuredActivities_Clause")
fUML_CompleteStructuredActivities_ConditionalNode = Class(name="fUML_CompleteStructuredActivities_ConditionalNode")
fUML_ExtraStructuredActivities_ExpansionRegion = Class(name="fUML_ExtraStructuredActivities_ExpansionRegion")
fUML_CompleteStructuredActivities_StructuredActivityNode = Class(name="fUML_CompleteStructuredActivities_StructuredActivityNode")
Action = Class(name="Action")
fUML_ExtraStructuredActivities_ExpansionNode = Class(name="fUML_ExtraStructuredActivities_ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities_ExpansionRegion")
fUML_IntermediateActions_WriteLinkAction = Class(name="fUML_IntermediateActions_WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities_ExpansionNode")
fUML_IntermediateActions_StructuralFeatureAction = Class(name="fUML_IntermediateActions_StructuralFeatureAction", is_abstract=True)
fUML_IntermediateActions_TestIdentityAction = Class(name="fUML_IntermediateActions_TestIdentityAction")
fUML_IntermediateActions_ValueSpecificationAction = Class(name="fUML_IntermediateActions_ValueSpecificationAction")
fUML_IntermediateActions_LinkAction = Class(name="fUML_IntermediateActions_LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions_LinkEndData")
fUML_IntermediateActions_LinkEndData = Class(name="fUML_IntermediateActions_LinkEndData")
fUML_IntermediateActions_WriteStructuralFeatureAction = Class(name="fUML_IntermediateActions_WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
fUML_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="fUML_IntermediateActions_RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
fUML_IntermediateActions_ReadLinkAction = Class(name="fUML_IntermediateActions_ReadLinkAction")
fUML_IntermediateActions_ReadSelfAction = Class(name="fUML_IntermediateActions_ReadSelfAction")
fUML_IntermediateActions_ReadStructuralFeatureAction = Class(name="fUML_IntermediateActions_ReadStructuralFeatureAction")
fUML_IntermediateActions_LinkEndCreationData = Class(name="fUML_IntermediateActions_LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
fUML_IntermediateActions_LinkEndDestructionData = Class(name="fUML_IntermediateActions_LinkEndDestructionData")
fUML_IntermediateActions_ClearAssociationAction = Class(name="fUML_IntermediateActions_ClearAssociationAction")
fUML_IntermediateActions_ClearStructuralFeatureAction = Class(name="fUML_IntermediateActions_ClearStructuralFeatureAction")
fUML_IntermediateActions_CreateLinkAction = Class(name="fUML_IntermediateActions_CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
fUML_IntermediateActions_CreateObjectAction = Class(name="fUML_IntermediateActions_CreateObjectAction")
fUML_IntermediateActions_DestroyLinkAction = Class(name="fUML_IntermediateActions_DestroyLinkAction")
fUML_IntermediateActions_DestroyObjectAction = Class(name="fUML_IntermediateActions_DestroyObjectAction")
fUML_IntermediateActions_AddStructuralFeatureValueAction = Class(name="fUML_IntermediateActions_AddStructuralFeatureValueAction")
fUML_CompleteActions_StartClassifierBehaviorAction = Class(name="fUML_CompleteActions_StartClassifierBehaviorAction")
fUML_CompleteActions_StartObjectBehaviorAction = Class(name="fUML_CompleteActions_StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
fUML_CompleteActions_ReduceAction = Class(name="fUML_CompleteActions_ReduceAction")
fUML_CompleteActions_ReadExtentAction = Class(name="fUML_CompleteActions_ReadExtentAction")
fUML_CompleteActions_ReadIsClassifiedObjectAction = Class(name="fUML_CompleteActions_ReadIsClassifiedObjectAction")
fUML_CompleteActions_ReclassifyObjectAction = Class(name="fUML_CompleteActions_ReclassifyObjectAction")
fUML_CompleteActions_AcceptEventAction = Class(name="fUML_CompleteActions_AcceptEventAction")
Communications_Trigger = Class(name="Communications_Trigger")
fUML_BasicActions_Action = Class(name="fUML_BasicActions_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
fUML_BasicActions_InputPin = Class(name="fUML_BasicActions_InputPin")
Pin = Class(name="Pin")
fUML_BasicActions_Pin = Class(name="fUML_BasicActions_Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities_ObjectNode")
fUML_BasicActions_CallAction = Class(name="fUML_BasicActions_CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
fUML_BasicActions_InvocationAction = Class(name="fUML_BasicActions_InvocationAction", is_abstract=True)
fUML_BasicActions_SendSignalAction = Class(name="fUML_BasicActions_SendSignalAction")
fUML_Kernel_StringValue = Class(name="fUML_Kernel_StringValue")
fUML_BasicActions_CallBehaviorAction = Class(name="fUML_BasicActions_CallBehaviorAction")
fUML_BasicActions_CallOperationAction = Class(name="fUML_BasicActions_CallOperationAction")
fUML_BasicActions_OutputPin = Class(name="fUML_BasicActions_OutputPin")
fUML_Kernel_StructuredValue = Class(name="fUML_Kernel_StructuredValue", is_abstract=True)
Value = Class(name="Value")
fUML_Kernel_FeatureValue = Class(name="fUML_Kernel_FeatureValue")
Kernel_Value = Class(name="Kernel_Value")
fUML_Kernel_UnlimitedNaturalValue = Class(name="fUML_Kernel_UnlimitedNaturalValue")
PrimitiveValue = Class(name="PrimitiveValue")
fUML_Kernel_PrimitiveValue = Class(name="fUML_Kernel_PrimitiveValue", is_abstract=True)
Kernel_PrimitiveType = Class(name="Kernel_PrimitiveType")
fUML_Kernel_Reference = Class(name="fUML_Kernel_Reference")
StructuredValue = Class(name="StructuredValue")
Kernel_Object = Class(name="Kernel_Object")
fUML_Kernel_Object = Class(name="fUML_Kernel_Object")
ExtensionalValue = Class(name="ExtensionalValue")
fUML_Kernel_ExtensionalValue = Class(name="fUML_Kernel_ExtensionalValue", is_abstract=True)
CompoundValue = Class(name="CompoundValue")
fUML_Kernel_CompoundValue = Class(name="fUML_Kernel_CompoundValue", is_abstract=True)
Kernel_FeatureValue = Class(name="Kernel_FeatureValue")
fUML_Kernel_Link = Class(name="fUML_Kernel_Link")
fUML_Kernel_IntegerValue = Class(name="fUML_Kernel_IntegerValue")
fUML_Kernel_EnumerationValue = Class(name="fUML_Kernel_EnumerationValue")
fUML_Kernel_DataValue = Class(name="fUML_Kernel_DataValue")
fUML_Kernel_BooleanValue = Class(name="fUML_Kernel_BooleanValue")
fUML_Kernel_Value = Class(name="fUML_Kernel_Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")
fUML_LociL1_SemanticVisitor = Class(name="fUML_LociL1_SemanticVisitor", is_abstract=True)

# fUML_BasicBehaviors_OpaqueBehavior class attributes and methods
fUML_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
fUML_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
fUML_BasicBehaviors_OpaqueBehavior.attributes={fUML_BasicBehaviors_OpaqueBehavior_body, fUML_BasicBehaviors_OpaqueBehavior_language}

# Behavior class attributes and methods

# fUML_BasicBehaviors_Behavior class attributes and methods
fUML_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
fUML_BasicBehaviors_Behavior.attributes={fUML_BasicBehaviors_Behavior_reentrant}

# Class class attributes and methods

# Kernel_BehavioralFeature class attributes and methods

# Kernel_Parameter class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# fUML_BasicBehaviors_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# BasicBehaviors_Behavior class attributes and methods

# fUML_BasicBehaviors_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# fUML_Communications_Trigger class attributes and methods

# NamedElement class attributes and methods

# Communications_Event class attributes and methods

# fUML_Communications_Event class attributes and methods

# PackageableElement class attributes and methods

# fUML_Communications_Signal class attributes and methods

# Kernel_Property class attributes and methods

# fUML_Communications_SignalEvent class attributes and methods

# MessageEvent class attributes and methods

# Communications_Signal class attributes and methods

# fUML_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# fUML_Communications_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# fUML_Kernel_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# fUML_Kernel_TypedElement class attributes and methods

# Kernel_Type class attributes and methods

# fUML_Kernel_NamedElement class attributes and methods
fUML_Kernel_NamedElement_name: Property = Property(name="name", type=StringType)
fUML_Kernel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
fUML_Kernel_NamedElement.attributes={fUML_Kernel_NamedElement_name, fUML_Kernel_NamedElement_visibility, fUML_Kernel_NamedElement_qualifiedName}

# Element class attributes and methods

# Kernel_Namespace class attributes and methods

# Kernel_Element class attributes and methods

# Kernel_Comment class attributes and methods

# fUML_Kernel_Comment class attributes and methods
fUML_Kernel_Comment_body: Property = Property(name="body", type=StringType)
fUML_Kernel_Comment.attributes={fUML_Kernel_Comment_body}

# fUML_Kernel_Namespace class attributes and methods

# Kernel_NamedElement class attributes and methods

# Kernel_ElementImport class attributes and methods

# Kernel_PackageImport class attributes and methods

# Kernel_PackageableElement class attributes and methods

# fUML_Kernel_ElementImport class attributes and methods
fUML_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
fUML_Kernel_ElementImport.attributes={fUML_Kernel_ElementImport_alias, fUML_Kernel_ElementImport_visibility}

# fUML_Kernel_PackageableElement class attributes and methods

# fUML_Kernel_PackageImport class attributes and methods
fUML_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_PackageImport.attributes={fUML_Kernel_PackageImport_visibility}

# Kernel_Package class attributes and methods

# fUML_Kernel_Package class attributes and methods

# fUML_Kernel_Element class attributes and methods

# fUML_Kernel_Type class attributes and methods

# fUML_Kernel_StructuralFeature class attributes and methods
fUML_Kernel_StructuralFeature_readOnly: Property = Property(name="readOnly", type=BooleanType)
fUML_Kernel_StructuralFeature.attributes={fUML_Kernel_StructuralFeature_readOnly}

# Kernel_Feature class attributes and methods

# Kernel_MultiplicityElement class attributes and methods

# Kernel_TypedElement class attributes and methods

# fUML_Kernel_Feature class attributes and methods
fUML_Kernel_Feature_static: Property = Property(name="static", type=BooleanType)
fUML_Kernel_Feature.attributes={fUML_Kernel_Feature_static}

# RedefinableElement class attributes and methods

# Kernel_Classifier class attributes and methods

# fUML_Kernel_RedefinableElement class attributes and methods
fUML_Kernel_RedefinableElement_leaf: Property = Property(name="leaf", type=BooleanType)
fUML_Kernel_RedefinableElement.attributes={fUML_Kernel_RedefinableElement_leaf}

# Kernel_RedefinableElement class attributes and methods

# fUML_Kernel_Classifier class attributes and methods
fUML_Kernel_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
fUML_Kernel_Classifier_finalSpecialization: Property = Property(name="finalSpecialization", type=BooleanType)
fUML_Kernel_Classifier.attributes={fUML_Kernel_Classifier_abstract, fUML_Kernel_Classifier_finalSpecialization}

# Kernel_Generalization class attributes and methods

# fUML_Kernel_Generalization class attributes and methods
fUML_Kernel_Generalization_substitutable: Property = Property(name="substitutable", type=BooleanType)
fUML_Kernel_Generalization.attributes={fUML_Kernel_Generalization_substitutable}

# fUML_Kernel_Property class attributes and methods
fUML_Kernel_Property_derived: Property = Property(name="derived", type=BooleanType)
fUML_Kernel_Property_derivedUnion: Property = Property(name="derivedUnion", type=BooleanType)
fUML_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
fUML_Kernel_Property_composite: Property = Property(name="composite", type=BooleanType)
fUML_Kernel_Property.attributes={fUML_Kernel_Property_derived, fUML_Kernel_Property_derivedUnion, fUML_Kernel_Property_composite, fUML_Kernel_Property_aggregation}

# StructuralFeature class attributes and methods

# Kernel_Association class attributes and methods

# Kernel_DataType class attributes and methods

# Kernel_Class class attributes and methods

# Kernel_ValueSpecification class attributes and methods

# fUML_Kernel_Association class attributes and methods
fUML_Kernel_Association_derived: Property = Property(name="derived", type=BooleanType)
fUML_Kernel_Association.attributes={fUML_Kernel_Association_derived}

# fUML_Kernel_DataType class attributes and methods

# fUML_Kernel_MultiplicityElement class attributes and methods
fUML_Kernel_MultiplicityElement_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_Kernel_MultiplicityElement_unique: Property = Property(name="unique", type=BooleanType)
fUML_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
fUML_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
fUML_Kernel_MultiplicityElement.attributes={fUML_Kernel_MultiplicityElement_unique, fUML_Kernel_MultiplicityElement_upper, fUML_Kernel_MultiplicityElement_ordered, fUML_Kernel_MultiplicityElement_lower}

# fUML_Kernel_BehavioralFeature class attributes and methods
fUML_Kernel_BehavioralFeature_abstract: Property = Property(name="abstract", type=BooleanType)
fUML_Kernel_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
fUML_Kernel_BehavioralFeature.attributes={fUML_Kernel_BehavioralFeature_concurrency, fUML_Kernel_BehavioralFeature_abstract}

# Feature class attributes and methods

# fUML_Kernel_Parameter class attributes and methods
fUML_Kernel_Parameter_direction: Property = Property(name="direction", type=StringType)
fUML_Kernel_Parameter.attributes={fUML_Kernel_Parameter_direction}

# fUML_Kernel_Operation class attributes and methods
fUML_Kernel_Operation_query: Property = Property(name="query", type=BooleanType)
fUML_Kernel_Operation_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_Kernel_Operation_unique: Property = Property(name="unique", type=BooleanType)
fUML_Kernel_Operation_lower: Property = Property(name="lower", type=IntegerType)
fUML_Kernel_Operation_upper: Property = Property(name="upper", type=IntegerType)
fUML_Kernel_Operation.attributes={fUML_Kernel_Operation_upper, fUML_Kernel_Operation_unique, fUML_Kernel_Operation_ordered, fUML_Kernel_Operation_lower, fUML_Kernel_Operation_query}

# fUML_Kernel_PrimitiveType class attributes and methods

# DataType class attributes and methods

# fUML_Kernel_Enumeration class attributes and methods

# Kernel_Operation class attributes and methods

# fUML_Kernel_InstanceSpecification class attributes and methods

# Kernel_Slot class attributes and methods

# fUML_Kernel_Slot class attributes and methods

# Kernel_StructuralFeature class attributes and methods

# Kernel_InstanceSpecification class attributes and methods

# fUML_Kernel_InstanceValue class attributes and methods

# ValueSpecification class attributes and methods

# fUML_Kernel_LiteralBoolean class attributes and methods
fUML_Kernel_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
fUML_Kernel_LiteralBoolean.attributes={fUML_Kernel_LiteralBoolean_value}

# LiteralSpecification class attributes and methods

# fUML_Kernel_LiteralSpecification class attributes and methods

# fUML_Kernel_LiteralInteger class attributes and methods
fUML_Kernel_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_LiteralInteger.attributes={fUML_Kernel_LiteralInteger_value}

# fUML_Kernel_LiteralNull class attributes and methods

# fUML_Kernel_LiteralString class attributes and methods
fUML_Kernel_LiteralString_value: Property = Property(name="value", type=StringType)
fUML_Kernel_LiteralString.attributes={fUML_Kernel_LiteralString_value}

# fUML_Kernel_LiteralUnlimitedNatural class attributes and methods
fUML_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_LiteralUnlimitedNatural.attributes={fUML_Kernel_LiteralUnlimitedNatural_value}

# Kernel_EnumerationLiteral class attributes and methods

# fUML_Kernel_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_Enumeration class attributes and methods

# fUML_Kernel_Class class attributes and methods
fUML_Kernel_Class_active: Property = Property(name="active", type=BooleanType)
fUML_Kernel_Class.attributes={fUML_Kernel_Class_active}

# BehavioredClassifier class attributes and methods

# Communications_Reception class attributes and methods

# fUML_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# fUML_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# IntermediateActivities_ObjectFlow class attributes and methods

# fUML_IntermediateActivities_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# fUML_IntermediateActivities_Activity class attributes and methods
fUML_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
fUML_IntermediateActivities_Activity.attributes={fUML_IntermediateActivities_Activity_readOnly}

# IntermediateActivities_ActivityEdge class attributes and methods

# fUML_IntermediateActivities_ActivityNode class attributes and methods

# fUML_IntermediateActivities_ObjectNode class attributes and methods

# fUML_IntermediateActivities_MergeNode class attributes and methods

# ControlNode class attributes and methods

# fUML_IntermediateActivities_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# fUML_IntermediateActivities_JoinNode class attributes and methods

# fUML_IntermediateActivities_InitialNode class attributes and methods

# fUML_IntermediateActivities_FinalNode class attributes and methods

# fUML_IntermediateActivities_ForkNode class attributes and methods

# fUML_IntermediateActivities_ControlFlow class attributes and methods

# fUML_IntermediateActivities_DecisionNode class attributes and methods

# CompleteStructuredActivities_Clause class attributes and methods

# fUML_IntermediateActivities_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# fUML_CompleteStructuredActivities_LoopNode class attributes and methods
fUML_CompleteStructuredActivities_LoopNode_testedFirst: Property = Property(name="testedFirst", type=BooleanType)
fUML_CompleteStructuredActivities_LoopNode.attributes={fUML_CompleteStructuredActivities_LoopNode_testedFirst}

# StructuredActivityNode class attributes and methods

# BasicActions_OutputPin class attributes and methods

# CompleteStructuredActivities_ExecutableNode class attributes and methods

# BasicActions_InputPin class attributes and methods

# fUML_CompleteStructuredActivities_ExecutableNode class attributes and methods

# fUML_CompleteStructuredActivities_Clause class attributes and methods

# fUML_CompleteStructuredActivities_ConditionalNode class attributes and methods
fUML_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
fUML_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
fUML_CompleteStructuredActivities_ConditionalNode.attributes={fUML_CompleteStructuredActivities_ConditionalNode_determinate, fUML_CompleteStructuredActivities_ConditionalNode_assured}

# fUML_ExtraStructuredActivities_ExpansionRegion class attributes and methods
fUML_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
fUML_ExtraStructuredActivities_ExpansionRegion.attributes={fUML_ExtraStructuredActivities_ExpansionRegion_mode}

# fUML_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
fUML_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
fUML_CompleteStructuredActivities_StructuredActivityNode.attributes={fUML_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# fUML_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# fUML_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# fUML_IntermediateActions_StructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_TestIdentityAction class attributes and methods

# fUML_IntermediateActions_ValueSpecificationAction class attributes and methods

# fUML_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# fUML_IntermediateActions_LinkEndData class attributes and methods

# fUML_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
fUML_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
fUML_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={fUML_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_ReadLinkAction class attributes and methods

# fUML_IntermediateActions_ReadSelfAction class attributes and methods

# fUML_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_LinkEndCreationData class attributes and methods
fUML_IntermediateActions_LinkEndCreationData_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fUML_IntermediateActions_LinkEndCreationData.attributes={fUML_IntermediateActions_LinkEndCreationData_replaceAll}

# LinkEndData class attributes and methods

# fUML_IntermediateActions_LinkEndDestructionData class attributes and methods
fUML_IntermediateActions_LinkEndDestructionData_destroyDuplicates: Property = Property(name="destroyDuplicates", type=BooleanType)
fUML_IntermediateActions_LinkEndDestructionData.attributes={fUML_IntermediateActions_LinkEndDestructionData_destroyDuplicates}

# fUML_IntermediateActions_ClearAssociationAction class attributes and methods

# fUML_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# fUML_IntermediateActions_CreateObjectAction class attributes and methods

# fUML_IntermediateActions_DestroyLinkAction class attributes and methods

# fUML_IntermediateActions_DestroyObjectAction class attributes and methods
fUML_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
fUML_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
fUML_IntermediateActions_DestroyObjectAction.attributes={fUML_IntermediateActions_DestroyObjectAction_destroyLinks, fUML_IntermediateActions_DestroyObjectAction_destroyOwnedObjects}

# fUML_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
fUML_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fUML_IntermediateActions_AddStructuralFeatureValueAction.attributes={fUML_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# fUML_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# fUML_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# fUML_CompleteActions_ReduceAction class attributes and methods
fUML_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_CompleteActions_ReduceAction.attributes={fUML_CompleteActions_ReduceAction_ordered}

# fUML_CompleteActions_ReadExtentAction class attributes and methods

# fUML_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
fUML_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
fUML_CompleteActions_ReadIsClassifiedObjectAction.attributes={fUML_CompleteActions_ReadIsClassifiedObjectAction_direct}

# fUML_CompleteActions_ReclassifyObjectAction class attributes and methods
fUML_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fUML_CompleteActions_ReclassifyObjectAction.attributes={fUML_CompleteActions_ReclassifyObjectAction_replaceAll}

# fUML_CompleteActions_AcceptEventAction class attributes and methods
fUML_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
fUML_CompleteActions_AcceptEventAction.attributes={fUML_CompleteActions_AcceptEventAction_unmarshall}

# Communications_Trigger class attributes and methods

# fUML_BasicActions_Action class attributes and methods
fUML_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
fUML_BasicActions_Action.attributes={fUML_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# fUML_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# fUML_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# fUML_BasicActions_CallAction class attributes and methods
fUML_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
fUML_BasicActions_CallAction.attributes={fUML_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# fUML_BasicActions_InvocationAction class attributes and methods

# fUML_BasicActions_SendSignalAction class attributes and methods

# fUML_Kernel_StringValue class attributes and methods
fUML_Kernel_StringValue_value: Property = Property(name="value", type=StringType)
fUML_Kernel_StringValue.attributes={fUML_Kernel_StringValue_value}

# fUML_BasicActions_CallBehaviorAction class attributes and methods

# fUML_BasicActions_CallOperationAction class attributes and methods

# fUML_BasicActions_OutputPin class attributes and methods

# fUML_Kernel_StructuredValue class attributes and methods

# Value class attributes and methods

# fUML_Kernel_FeatureValue class attributes and methods
fUML_Kernel_FeatureValue_position: Property = Property(name="position", type=IntegerType)
fUML_Kernel_FeatureValue.attributes={fUML_Kernel_FeatureValue_position}

# Kernel_Value class attributes and methods

# fUML_Kernel_UnlimitedNaturalValue class attributes and methods
fUML_Kernel_UnlimitedNaturalValue_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_UnlimitedNaturalValue.attributes={fUML_Kernel_UnlimitedNaturalValue_value}

# PrimitiveValue class attributes and methods

# fUML_Kernel_PrimitiveValue class attributes and methods

# Kernel_PrimitiveType class attributes and methods

# fUML_Kernel_Reference class attributes and methods

# StructuredValue class attributes and methods

# Kernel_Object class attributes and methods

# fUML_Kernel_Object class attributes and methods

# ExtensionalValue class attributes and methods

# fUML_Kernel_ExtensionalValue class attributes and methods

# CompoundValue class attributes and methods

# fUML_Kernel_CompoundValue class attributes and methods

# Kernel_FeatureValue class attributes and methods

# fUML_Kernel_Link class attributes and methods

# fUML_Kernel_IntegerValue class attributes and methods
fUML_Kernel_IntegerValue_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_IntegerValue.attributes={fUML_Kernel_IntegerValue_value}

# fUML_Kernel_EnumerationValue class attributes and methods

# fUML_Kernel_DataValue class attributes and methods

# fUML_Kernel_BooleanValue class attributes and methods
fUML_Kernel_BooleanValue_value: Property = Property(name="value", type=BooleanType)
fUML_Kernel_BooleanValue.attributes={fUML_Kernel_BooleanValue_value}

# fUML_Kernel_Value class attributes and methods

# SemanticVisitor class attributes and methods

# fUML_LociL1_SemanticVisitor class attributes and methods

# Relationships
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="BehavioralFeature", type=fUML_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=Kernel_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter1: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1",
    ends={
        Property(name="Kernel_Parameter", type=fUML_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicBehaviors_Behavior", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context2: BinaryAssociation = BinaryAssociation(
    name="context2",
    ends={
        Property(name="BasicBehaviors_BehavioredClassifier", type=fUML_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicBehaviors_Behavior3", type=BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedBehavior4: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior4",
    ends={
        Property(name="BasicBehaviors_Behavior", type=fUML_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicBehaviors_BehavioredClassifier", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior5: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior5",
    ends={
        Property(name="BasicBehaviors_Behavior7", type=fUML_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicBehaviors_BehavioredClassifier6", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="Communications_Event", type=fUML_Communications_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Communications_Trigger", type=Communications_Event, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute9: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute9",
    ends={
        Property(name="Kernel_Property", type=fUML_Communications_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Communications_Signal", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal10: BinaryAssociation = BinaryAssociation(
    name="signal10",
    ends={
        Property(name="Communications_Signal", type=fUML_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Communications_SignalEvent", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal11: BinaryAssociation = BinaryAssociation(
    name="signal11",
    ends={
        Property(name="Communications_Signal12", type=fUML_Communications_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Communications_Reception", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="Kernel_Type", type=fUML_Kernel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_TypedElement", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="Namespace", type=fUML_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=Kernel_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement15: BinaryAssociation = BinaryAssociation(
    name="ownedElement15",
    ends={
        Property(name="Element", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Element17", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Kernel_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment18: BinaryAssociation = BinaryAssociation(
    name="ownedComment18",
    ends={
        Property(name="Kernel_Comment", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Element", type=Kernel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement19: BinaryAssociation = BinaryAssociation(
    name="annotatedElement19",
    ends={
        Property(name="Kernel_Element", type=fUML_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Comment", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
member20: BinaryAssociation = BinaryAssociation(
    name="member20",
    ends={
        Property(name="Kernel_NamedElement", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport21: BinaryAssociation = BinaryAssociation(
    name="elementImport21",
    ends={
        Property(name="ElementImport", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=Kernel_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport22: BinaryAssociation = BinaryAssociation(
    name="packageImport22",
    ends={
        Property(name="PackageImport", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace23", type=Kernel_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember24: BinaryAssociation = BinaryAssociation(
    name="importedMember24",
    ends={
        Property(name="Kernel_PackageableElement", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Namespace25", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember26: BinaryAssociation = BinaryAssociation(
    name="ownedMember26",
    ends={
        Property(name="NamedElement", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement27: BinaryAssociation = BinaryAssociation(
    name="importedElement27",
    ends={
        Property(name="Kernel_PackageableElement28", type=fUML_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_ElementImport", type=Kernel_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace29: BinaryAssociation = BinaryAssociation(
    name="importingNamespace29",
    ends={
        Property(name="Namespace30", type=fUML_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage31: BinaryAssociation = BinaryAssociation(
    name="importedPackage31",
    ends={
        Property(name="Kernel_Package", type=fUML_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_PackageImport", type=Kernel_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace32: BinaryAssociation = BinaryAssociation(
    name="importingNamespace32",
    ends={
        Property(name="Namespace33", type=fUML_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
feature47: BinaryAssociation = BinaryAssociation(
    name="feature47",
    ends={
        Property(name="featuringClassifier", type=Kernel_Feature, multiplicity=Multiplicity(0, 9999)),
        Property(name="Feature", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement34: BinaryAssociation = BinaryAssociation(
    name="packagedElement34",
    ends={
        Property(name="Kernel_PackageableElement35", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Package", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType36: BinaryAssociation = BinaryAssociation(
    name="ownedType36",
    ends={
        Property(name="Type", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Kernel_Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage37: BinaryAssociation = BinaryAssociation(
    name="nestedPackage37",
    ends={
        Property(name="Package", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=Kernel_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage38: BinaryAssociation = BinaryAssociation(
    name="nestingPackage38",
    ends={
        Property(name="Package39", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
package40: BinaryAssociation = BinaryAssociation(
    name="package40",
    ends={
        Property(name="Package41", type=fUML_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier42: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier42",
    ends={
        Property(name="Classifier", type=fUML_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement43: BinaryAssociation = BinaryAssociation(
    name="redefinedElement43",
    ends={
        Property(name="Kernel_RedefinableElement", type=fUML_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_RedefinableElement", type=Kernel_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext44: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext44",
    ends={
        Property(name="Kernel_Classifier", type=fUML_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_RedefinableElement45", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization46: BinaryAssociation = BinaryAssociation(
    name="generalization46",
    ends={
        Property(name="Generalization", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=Kernel_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritedMember48: BinaryAssociation = BinaryAssociation(
    name="inheritedMember48",
    ends={
        Property(name="Kernel_NamedElement49", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute50: BinaryAssociation = BinaryAssociation(
    name="attribute50",
    ends={
        Property(name="Kernel_Property52", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier51", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general53: BinaryAssociation = BinaryAssociation(
    name="general53",
    ends={
        Property(name="Kernel_Classifier55", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier54", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general56: BinaryAssociation = BinaryAssociation(
    name="general56",
    ends={
        Property(name="Kernel_Classifier57", type=fUML_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific58: BinaryAssociation = BinaryAssociation(
    name="specific58",
    ends={
        Property(name="Classifier59", type=fUML_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owningAssociation60: BinaryAssociation = BinaryAssociation(
    name="owningAssociation60",
    ends={
        Property(name="Association", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
association61: BinaryAssociation = BinaryAssociation(
    name="association61",
    ends={
        Property(name="Association62", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
datatype63: BinaryAssociation = BinaryAssociation(
    name="datatype63",
    ends={
        Property(name="DataType", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Kernel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
class_64: BinaryAssociation = BinaryAssociation(
    name="class_64",
    ends={
        Property(name="Class", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute65", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
opposite66: BinaryAssociation = BinaryAssociation(
    name="opposite66",
    ends={
        Property(name="Kernel_Property67", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Property", type=Kernel_Property, multiplicity=Multiplicity(0, 1))
    }
)
endType68: BinaryAssociation = BinaryAssociation(
    name="endType68",
    ends={
        Property(name="Kernel_Type69", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Association", type=Kernel_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd70: BinaryAssociation = BinaryAssociation(
    name="memberEnd70",
    ends={
        Property(name="Property", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=Kernel_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableOwnedEnd71: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd71",
    ends={
        Property(name="Kernel_Property73", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Association72", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd74: BinaryAssociation = BinaryAssociation(
    name="ownedEnd74",
    ends={
        Property(name="Property75", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute76: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute76",
    ends={
        Property(name="Property77", type=fUML_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_85: BinaryAssociation = BinaryAssociation(
    name="class_85",
    ends={
        Property(name="Class86", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
upperValue78: BinaryAssociation = BinaryAssociation(
    name="upperValue78",
    ends={
        Property(name="Kernel_ValueSpecification", type=fUML_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_MultiplicityElement", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue79: BinaryAssociation = BinaryAssociation(
    name="lowerValue79",
    ends={
        Property(name="Kernel_ValueSpecification81", type=fUML_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_MultiplicityElement80", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter82: BinaryAssociation = BinaryAssociation(
    name="ownedParameter82",
    ends={
        Property(name="Kernel_Parameter83", type=fUML_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_BehavioralFeature", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method84: BinaryAssociation = BinaryAssociation(
    name="method84",
    ends={
        Property(name="Behavior", type=fUML_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation87: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation87",
    ends={
        Property(name="Kernel_Operation", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Operation", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type88: BinaryAssociation = BinaryAssociation(
    name="type88",
    ends={
        Property(name="Kernel_Type90", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Operation89", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
classifier91: BinaryAssociation = BinaryAssociation(
    name="classifier91",
    ends={
        Property(name="Kernel_Classifier92", type=fUML_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_InstanceSpecification", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot93: BinaryAssociation = BinaryAssociation(
    name="slot93",
    ends={
        Property(name="Slot", type=fUML_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature94: BinaryAssociation = BinaryAssociation(
    name="definingFeature94",
    ends={
        Property(name="Kernel_StructuralFeature", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Slot", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="Kernel_ValueSpecification97", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Slot96", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance98: BinaryAssociation = BinaryAssociation(
    name="owningInstance98",
    ends={
        Property(name="InstanceSpecification", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance99: BinaryAssociation = BinaryAssociation(
    name="instance99",
    ends={
        Property(name="Kernel_InstanceSpecification", type=fUML_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
guard118: BinaryAssociation = BinaryAssociation(
    name="guard118",
    ends={
        Property(name="Kernel_ValueSpecification119", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLiteral100: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral100",
    ends={
        Property(name="EnumerationLiteral", type=fUML_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration101: BinaryAssociation = BinaryAssociation(
    name="enumeration101",
    ends={
        Property(name="Enumeration", type=fUML_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Kernel_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute102: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute102",
    ends={
        Property(name="Property103", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation104: BinaryAssociation = BinaryAssociation(
    name="ownedOperation104",
    ends={
        Property(name="Operation", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_105", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass106: BinaryAssociation = BinaryAssociation(
    name="superClass106",
    ends={
        Property(name="Kernel_Class", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception107: BinaryAssociation = BinaryAssociation(
    name="ownedReception107",
    ends={
        Property(name="Communications_Reception", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class108", type=Communications_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier109: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier109",
    ends={
        Property(name="Kernel_Classifier111", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class110", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity112: BinaryAssociation = BinaryAssociation(
    name="activity112",
    ends={
        Property(name="Activity", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source113: BinaryAssociation = BinaryAssociation(
    name="source113",
    ends={
        Property(name="ActivityNode", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="ActivityNode115", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode116: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode116",
    ends={
        Property(name="StructuredActivityNode", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge117", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow135: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow135",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=fUML_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_DecisionNode136", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
node120: BinaryAssociation = BinaryAssociation(
    name="node120",
    ends={
        Property(name="ActivityNode121", type=fUML_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge122: BinaryAssociation = BinaryAssociation(
    name="edge122",
    ends={
        Property(name="ActivityEdge", type=fUML_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity123", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode124: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode124",
    ends={
        Property(name="StructuredActivityNode125", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity126: BinaryAssociation = BinaryAssociation(
    name="activity126",
    ends={
        Property(name="Activity128", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node127", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing129: BinaryAssociation = BinaryAssociation(
    name="outgoing129",
    ends={
        Property(name="ActivityEdge130", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming131: BinaryAssociation = BinaryAssociation(
    name="incoming131",
    ends={
        Property(name="ActivityEdge132", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput133: BinaryAssociation = BinaryAssociation(
    name="decisionInput133",
    ends={
        Property(name="BasicBehaviors_Behavior134", type=fUML_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
predecessorClause164: BinaryAssociation = BinaryAssociation(
    name="predecessorClause164",
    ends={
        Property(name="Clause", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
parameter137: BinaryAssociation = BinaryAssociation(
    name="parameter137",
    ends={
        Property(name="Kernel_Parameter138", type=fUML_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_ActivityParameterNode", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
decider139: BinaryAssociation = BinaryAssociation(
    name="decider139",
    ends={
        Property(name="BasicActions_OutputPin", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test140: BinaryAssociation = BinaryAssociation(
    name="test140",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode141", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput142: BinaryAssociation = BinaryAssociation(
    name="bodyOutput142",
    ends={
        Property(name="BasicActions_OutputPin144", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode143", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput145: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput145",
    ends={
        Property(name="BasicActions_InputPin", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode146", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart147: BinaryAssociation = BinaryAssociation(
    name="bodyPart147",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode149", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode148", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result150: BinaryAssociation = BinaryAssociation(
    name="result150",
    ends={
        Property(name="BasicActions_OutputPin152", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode151", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable153: BinaryAssociation = BinaryAssociation(
    name="loopVariable153",
    ends={
        Property(name="BasicActions_OutputPin155", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode154", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart156: BinaryAssociation = BinaryAssociation(
    name="setupPart156",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode158", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode157", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test159: BinaryAssociation = BinaryAssociation(
    name="test159",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode160", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body161: BinaryAssociation = BinaryAssociation(
    name="body161",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode163", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause162", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause165: BinaryAssociation = BinaryAssociation(
    name="successorClause165",
    ends={
        Property(name="Clause166", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider167: BinaryAssociation = BinaryAssociation(
    name="decider167",
    ends={
        Property(name="BasicActions_OutputPin169", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause168", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput170: BinaryAssociation = BinaryAssociation(
    name="bodyOutput170",
    ends={
        Property(name="BasicActions_OutputPin172", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause171", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause173: BinaryAssociation = BinaryAssociation(
    name="clause173",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=fUML_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result174: BinaryAssociation = BinaryAssociation(
    name="result174",
    ends={
        Property(name="BasicActions_OutputPin176", type=fUML_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_ConditionalNode175", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node177: BinaryAssociation = BinaryAssociation(
    name="node177",
    ends={
        Property(name="ActivityNode178", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge179: BinaryAssociation = BinaryAssociation(
    name="edge179",
    ends={
        Property(name="ActivityEdge181", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode180", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput182: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput182",
    ends={
        Property(name="BasicActions_OutputPin183", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput184: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput184",
    ends={
        Property(name="BasicActions_InputPin186", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_StructuredActivityNode185", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput187: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput187",
    ends={
        Property(name="ExpansionRegion", type=fUML_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput188: BinaryAssociation = BinaryAssociation(
    name="regionAsInput188",
    ends={
        Property(name="ExpansionRegion189", type=fUML_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement190: BinaryAssociation = BinaryAssociation(
    name="inputElement190",
    ends={
        Property(name="ExpansionNode", type=fUML_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement191: BinaryAssociation = BinaryAssociation(
    name="outputElement191",
    ends={
        Property(name="ExpansionNode192", type=fUML_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature193: BinaryAssociation = BinaryAssociation(
    name="structuralFeature193",
    ends={
        Property(name="Kernel_StructuralFeature194", type=fUML_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_StructuralFeatureAction", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object195: BinaryAssociation = BinaryAssociation(
    name="object195",
    ends={
        Property(name="BasicActions_InputPin197", type=fUML_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_StructuralFeatureAction196", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second198: BinaryAssociation = BinaryAssociation(
    name="second198",
    ends={
        Property(name="BasicActions_InputPin199", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result200: BinaryAssociation = BinaryAssociation(
    name="result200",
    ends={
        Property(name="BasicActions_OutputPin202", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction201", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first203: BinaryAssociation = BinaryAssociation(
    name="first203",
    ends={
        Property(name="BasicActions_InputPin205", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction204", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value206: BinaryAssociation = BinaryAssociation(
    name="value206",
    ends={
        Property(name="Kernel_ValueSpecification207", type=fUML_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result208: BinaryAssociation = BinaryAssociation(
    name="result208",
    ends={
        Property(name="BasicActions_OutputPin210", type=fUML_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ValueSpecificationAction209", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt233: BinaryAssociation = BinaryAssociation(
    name="insertAt233",
    ends={
        Property(name="BasicActions_InputPin234", type=fUML_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
endData211: BinaryAssociation = BinaryAssociation(
    name="endData211",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=fUML_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue212: BinaryAssociation = BinaryAssociation(
    name="inputValue212",
    ends={
        Property(name="BasicActions_InputPin214", type=fUML_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkAction213", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value215: BinaryAssociation = BinaryAssociation(
    name="value215",
    ends={
        Property(name="BasicActions_InputPin216", type=fUML_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end217: BinaryAssociation = BinaryAssociation(
    name="end217",
    ends={
        Property(name="Kernel_Property219", type=fUML_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndData218", type=Kernel_Property, multiplicity=Multiplicity(1, 1))
    }
)
value220: BinaryAssociation = BinaryAssociation(
    name="value220",
    ends={
        Property(name="BasicActions_InputPin221", type=fUML_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result222: BinaryAssociation = BinaryAssociation(
    name="result222",
    ends={
        Property(name="BasicActions_OutputPin224", type=fUML_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_WriteStructuralFeatureAction223", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt225: BinaryAssociation = BinaryAssociation(
    name="removeAt225",
    ends={
        Property(name="BasicActions_InputPin226", type=fUML_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result227: BinaryAssociation = BinaryAssociation(
    name="result227",
    ends={
        Property(name="BasicActions_OutputPin228", type=fUML_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result229: BinaryAssociation = BinaryAssociation(
    name="result229",
    ends={
        Property(name="BasicActions_OutputPin230", type=fUML_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result231: BinaryAssociation = BinaryAssociation(
    name="result231",
    ends={
        Property(name="BasicActions_OutputPin232", type=fUML_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object252: BinaryAssociation = BinaryAssociation(
    name="object252",
    ends={
        Property(name="BasicActions_InputPin253", type=fUML_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
destroyAt235: BinaryAssociation = BinaryAssociation(
    name="destroyAt235",
    ends={
        Property(name="BasicActions_InputPin236", type=fUML_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
association237: BinaryAssociation = BinaryAssociation(
    name="association237",
    ends={
        Property(name="Kernel_Association", type=fUML_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearAssociationAction", type=Kernel_Association, multiplicity=Multiplicity(1, 1))
    }
)
object238: BinaryAssociation = BinaryAssociation(
    name="object238",
    ends={
        Property(name="BasicActions_InputPin240", type=fUML_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearAssociationAction239", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result241: BinaryAssociation = BinaryAssociation(
    name="result241",
    ends={
        Property(name="BasicActions_OutputPin242", type=fUML_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result243: BinaryAssociation = BinaryAssociation(
    name="result243",
    ends={
        Property(name="BasicActions_OutputPin244", type=fUML_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier245: BinaryAssociation = BinaryAssociation(
    name="classifier245",
    ends={
        Property(name="Kernel_Classifier247", type=fUML_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_CreateObjectAction246", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target248: BinaryAssociation = BinaryAssociation(
    name="target248",
    ends={
        Property(name="BasicActions_InputPin249", type=fUML_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt250: BinaryAssociation = BinaryAssociation(
    name="insertAt250",
    ends={
        Property(name="BasicActions_InputPin251", type=fUML_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newClassifier282: BinaryAssociation = BinaryAssociation(
    name="newClassifier282",
    ends={
        Property(name="Kernel_Classifier284", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction283", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object254: BinaryAssociation = BinaryAssociation(
    name="object254",
    ends={
        Property(name="BasicActions_InputPin255", type=fUML_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer256: BinaryAssociation = BinaryAssociation(
    name="reducer256",
    ends={
        Property(name="BasicBehaviors_Behavior257", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result258: BinaryAssociation = BinaryAssociation(
    name="result258",
    ends={
        Property(name="BasicActions_OutputPin260", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction259", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection261: BinaryAssociation = BinaryAssociation(
    name="collection261",
    ends={
        Property(name="BasicActions_InputPin263", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction262", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result264: BinaryAssociation = BinaryAssociation(
    name="result264",
    ends={
        Property(name="BasicActions_OutputPin265", type=fUML_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier266: BinaryAssociation = BinaryAssociation(
    name="classifier266",
    ends={
        Property(name="Kernel_Classifier268", type=fUML_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadExtentAction267", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier269: BinaryAssociation = BinaryAssociation(
    name="classifier269",
    ends={
        Property(name="Kernel_Classifier270", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result271: BinaryAssociation = BinaryAssociation(
    name="result271",
    ends={
        Property(name="BasicActions_OutputPin273", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction272", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object274: BinaryAssociation = BinaryAssociation(
    name="object274",
    ends={
        Property(name="BasicActions_InputPin276", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction275", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier277: BinaryAssociation = BinaryAssociation(
    name="oldClassifier277",
    ends={
        Property(name="Kernel_Classifier278", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object279: BinaryAssociation = BinaryAssociation(
    name="object279",
    ends={
        Property(name="BasicActions_InputPin281", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction280", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result285: BinaryAssociation = BinaryAssociation(
    name="result285",
    ends={
        Property(name="BasicActions_OutputPin286", type=fUML_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger287: BinaryAssociation = BinaryAssociation(
    name="trigger287",
    ends={
        Property(name="Communications_Trigger", type=fUML_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_AcceptEventAction288", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output289: BinaryAssociation = BinaryAssociation(
    name="output289",
    ends={
        Property(name="BasicActions_OutputPin290", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context291: BinaryAssociation = BinaryAssociation(
    name="context291",
    ends={
        Property(name="Kernel_Classifier293", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action292", type=Kernel_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
input294: BinaryAssociation = BinaryAssociation(
    name="input294",
    ends={
        Property(name="BasicActions_InputPin296", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action295", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result297: BinaryAssociation = BinaryAssociation(
    name="result297",
    ends={
        Property(name="BasicActions_OutputPin298", type=fUML_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument299: BinaryAssociation = BinaryAssociation(
    name="argument299",
    ends={
        Property(name="BasicActions_InputPin300", type=fUML_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target301: BinaryAssociation = BinaryAssociation(
    name="target301",
    ends={
        Property(name="BasicActions_InputPin302", type=fUML_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal303: BinaryAssociation = BinaryAssociation(
    name="signal303",
    ends={
        Property(name="Communications_Signal305", type=fUML_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_SendSignalAction304", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior306: BinaryAssociation = BinaryAssociation(
    name="behavior306",
    ends={
        Property(name="BasicBehaviors_Behavior307", type=fUML_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation308: BinaryAssociation = BinaryAssociation(
    name="operation308",
    ends={
        Property(name="Kernel_Operation309", type=fUML_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallOperationAction", type=Kernel_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target310: BinaryAssociation = BinaryAssociation(
    name="target310",
    ends={
        Property(name="BasicActions_InputPin312", type=fUML_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallOperationAction311", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature313: BinaryAssociation = BinaryAssociation(
    name="feature313",
    ends={
        Property(name="Kernel_StructuralFeature314", type=fUML_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_FeatureValue", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
values315: BinaryAssociation = BinaryAssociation(
    name="values315",
    ends={
        Property(name="Kernel_Value", type=fUML_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_FeatureValue316", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type317: BinaryAssociation = BinaryAssociation(
    name="type317",
    ends={
        Property(name="Kernel_PrimitiveType", type=fUML_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
referent318: BinaryAssociation = BinaryAssociation(
    name="referent318",
    ends={
        Property(name="Kernel_Object", type=fUML_Kernel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Reference", type=Kernel_Object, multiplicity=Multiplicity(1, 1))
    }
)
types319: BinaryAssociation = BinaryAssociation(
    name="types319",
    ends={
        Property(name="Kernel_Class320", type=fUML_Kernel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Object", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
featureValues321: BinaryAssociation = BinaryAssociation(
    name="featureValues321",
    ends={
        Property(name="Kernel_FeatureValue", type=fUML_Kernel_CompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_CompoundValue", type=Kernel_FeatureValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type322: BinaryAssociation = BinaryAssociation(
    name="type322",
    ends={
        Property(name="Kernel_Association323", type=fUML_Kernel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Link", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
literal324: BinaryAssociation = BinaryAssociation(
    name="literal324",
    ends={
        Property(name="Kernel_EnumerationLiteral", type=fUML_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_EnumerationValue", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type325: BinaryAssociation = BinaryAssociation(
    name="type325",
    ends={
        Property(name="Kernel_Enumeration", type=fUML_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_EnumerationValue326", type=Kernel_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
type327: BinaryAssociation = BinaryAssociation(
    name="type327",
    ends={
        Property(name="Kernel_DataType", type=fUML_Kernel_DataValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_DataValue", type=Kernel_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fUML_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=fUML_BasicBehaviors_OpaqueBehavior)
gen_fUML_BasicBehaviors_Behavior_Class = Generalization(general=Class_, specific=fUML_BasicBehaviors_Behavior)
gen_fUML_BasicBehaviors_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=fUML_BasicBehaviors_BehavioredClassifier)
gen_fUML_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=fUML_BasicBehaviors_FunctionBehavior)
gen_fUML_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=fUML_Communications_Trigger)
gen_fUML_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=fUML_Communications_Event)
gen_fUML_Communications_Signal_Classifier = Generalization(general=Classifier, specific=fUML_Communications_Signal)
gen_fUML_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=fUML_Communications_SignalEvent)
gen_fUML_Communications_MessageEvent_Event = Generalization(general=Event, specific=fUML_Communications_MessageEvent)
gen_fUML_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fUML_Communications_Reception)
gen_fUML_Kernel_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=fUML_Kernel_ValueSpecification)
gen_fUML_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_TypedElement)
gen_fUML_Kernel_NamedElement_Element = Generalization(general=Element, specific=fUML_Kernel_NamedElement)
gen_fUML_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_Namespace)
gen_fUML_Kernel_ElementImport_Element = Generalization(general=Element, specific=fUML_Kernel_ElementImport)
gen_fUML_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_PackageableElement)
gen_fUML_Kernel_PackageImport_Element = Generalization(general=Element, specific=fUML_Kernel_PackageImport)
gen_fUML_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fUML_Kernel_Package)
gen_fUML_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=fUML_Kernel_Package)
gen_fUML_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=fUML_Kernel_Type)
gen_fUML_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=fUML_Kernel_Feature)
gen_fUML_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_RedefinableElement)
gen_fUML_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fUML_Kernel_Classifier)
gen_fUML_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=fUML_Kernel_Classifier)
gen_fUML_Kernel_Generalization_Element = Generalization(general=Element, specific=fUML_Kernel_Generalization)
gen_fUML_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=fUML_Kernel_Property)
gen_fUML_Kernel_Association_Classifier = Generalization(general=Classifier, specific=fUML_Kernel_Association)
gen_fUML_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=fUML_Kernel_DataType)
gen_fUML_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=fUML_Kernel_MultiplicityElement)
gen_fUML_Kernel_BehavioralFeature_Feature = Generalization(general=Feature, specific=fUML_Kernel_BehavioralFeature)
gen_fUML_Kernel_Parameter_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_Kernel_Parameter)
gen_fUML_Kernel_Parameter_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fUML_Kernel_Parameter)
gen_fUML_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fUML_Kernel_Operation)
gen_fUML_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=fUML_Kernel_PrimitiveType)
gen_fUML_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=fUML_Kernel_Enumeration)
gen_fUML_Kernel_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_InstanceSpecification)
gen_fUML_Kernel_Slot_Element = Generalization(general=Element, specific=fUML_Kernel_Slot)
gen_fUML_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=fUML_Kernel_InstanceValue)
gen_fUML_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralBoolean)
gen_fUML_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=fUML_Kernel_LiteralSpecification)
gen_fUML_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralInteger)
gen_fUML_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralNull)
gen_fUML_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralString)
gen_fUML_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralUnlimitedNatural)
gen_fUML_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=fUML_Kernel_EnumerationLiteral)
gen_fUML_Kernel_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=fUML_Kernel_Class)
gen_fUML_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=fUML_IntermediateActivities_ObjectFlow)
gen_fUML_IntermediateActivities_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=fUML_IntermediateActivities_ActivityEdge)
gen_fUML_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=fUML_IntermediateActivities_Activity)
gen_fUML_IntermediateActivities_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=fUML_IntermediateActivities_ActivityNode)
gen_fUML_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode = Generalization(general=IntermediateActivities_ActivityNode, specific=fUML_IntermediateActivities_ObjectNode)
gen_fUML_IntermediateActivities_ObjectNode_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fUML_IntermediateActivities_ObjectNode)
gen_fUML_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_MergeNode)
gen_fUML_IntermediateActivities_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=fUML_IntermediateActivities_ControlNode)
gen_fUML_IntermediateActivities_JoinNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_JoinNode)
gen_fUML_IntermediateActivities_InitialNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_InitialNode)
gen_fUML_IntermediateActivities_FinalNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_FinalNode)
gen_fUML_IntermediateActivities_ForkNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_ForkNode)
gen_fUML_IntermediateActivities_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=fUML_IntermediateActivities_ControlFlow)
gen_fUML_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_DecisionNode)
gen_fUML_IntermediateActivities_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=fUML_IntermediateActivities_ActivityFinalNode)
gen_fUML_IntermediateActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=fUML_IntermediateActivities_ActivityParameterNode)
gen_fUML_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_CompleteStructuredActivities_LoopNode)
gen_fUML_CompleteStructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=fUML_CompleteStructuredActivities_ExecutableNode)
gen_fUML_CompleteStructuredActivities_Clause_Element = Generalization(general=Element, specific=fUML_CompleteStructuredActivities_Clause)
gen_fUML_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_CompleteStructuredActivities_ConditionalNode)
gen_fUML_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_ExtraStructuredActivities_ExpansionRegion)
gen_fUML_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=fUML_CompleteStructuredActivities_StructuredActivityNode)
gen_fUML_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=fUML_ExtraStructuredActivities_ExpansionNode)
gen_fUML_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=fUML_IntermediateActions_WriteLinkAction)
gen_fUML_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_StructuralFeatureAction)
gen_fUML_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_TestIdentityAction)
gen_fUML_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ValueSpecificationAction)
gen_fUML_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_LinkAction)
gen_fUML_IntermediateActions_LinkEndData_Element = Generalization(general=Element, specific=fUML_IntermediateActions_LinkEndData)
gen_fUML_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_WriteStructuralFeatureAction)
gen_fUML_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fUML_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_fUML_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=fUML_IntermediateActions_ReadLinkAction)
gen_fUML_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ReadSelfAction)
gen_fUML_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_ReadStructuralFeatureAction)
gen_fUML_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=fUML_IntermediateActions_LinkEndCreationData)
gen_fUML_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=fUML_IntermediateActions_LinkEndDestructionData)
gen_fUML_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ClearAssociationAction)
gen_fUML_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_ClearStructuralFeatureAction)
gen_fUML_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fUML_IntermediateActions_CreateLinkAction)
gen_fUML_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_CreateObjectAction)
gen_fUML_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fUML_IntermediateActions_DestroyLinkAction)
gen_fUML_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_DestroyObjectAction)
gen_fUML_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fUML_IntermediateActions_AddStructuralFeatureValueAction)
gen_fUML_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_StartClassifierBehaviorAction)
gen_fUML_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=fUML_CompleteActions_StartObjectBehaviorAction)
gen_fUML_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReduceAction)
gen_fUML_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReadExtentAction)
gen_fUML_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReadIsClassifiedObjectAction)
gen_fUML_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReclassifyObjectAction)
gen_fUML_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_AcceptEventAction)
gen_fUML_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=fUML_BasicActions_Action)
gen_fUML_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=fUML_BasicActions_InputPin)
gen_fUML_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=fUML_BasicActions_Pin)
gen_fUML_BasicActions_Pin_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_BasicActions_Pin)
gen_fUML_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=fUML_BasicActions_CallAction)
gen_fUML_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=fUML_BasicActions_InvocationAction)
gen_fUML_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=fUML_BasicActions_SendSignalAction)
gen_fUML_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_StringValue)
gen_fUML_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=fUML_BasicActions_CallBehaviorAction)
gen_fUML_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=fUML_BasicActions_CallOperationAction)
gen_fUML_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=fUML_BasicActions_OutputPin)
gen_fUML_Kernel_StructuredValue_Value = Generalization(general=Value, specific=fUML_Kernel_StructuredValue)
gen_fUML_Kernel_UnlimitedNaturalValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_UnlimitedNaturalValue)
gen_fUML_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=fUML_Kernel_PrimitiveValue)
gen_fUML_Kernel_Reference_StructuredValue = Generalization(general=StructuredValue, specific=fUML_Kernel_Reference)
gen_fUML_Kernel_Object_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fUML_Kernel_Object)
gen_fUML_Kernel_ExtensionalValue_CompoundValue = Generalization(general=CompoundValue, specific=fUML_Kernel_ExtensionalValue)
gen_fUML_Kernel_CompoundValue_StructuredValue = Generalization(general=StructuredValue, specific=fUML_Kernel_CompoundValue)
gen_fUML_Kernel_Link_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fUML_Kernel_Link)
gen_fUML_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_IntegerValue)
gen_fUML_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=fUML_Kernel_EnumerationValue)
gen_fUML_Kernel_DataValue_CompoundValue = Generalization(general=CompoundValue, specific=fUML_Kernel_DataValue)
gen_fUML_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_BooleanValue)
gen_fUML_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=fUML_Kernel_Value)

# Domain Model
domain_model = DomainModel(
    name="fUML",
    types={fUML_BasicBehaviors_OpaqueBehavior, Behavior, fUML_BasicBehaviors_Behavior, Class_, Kernel_BehavioralFeature, Kernel_Parameter, BasicBehaviors_BehavioredClassifier, fUML_BasicBehaviors_BehavioredClassifier, Classifier, BasicBehaviors_Behavior, fUML_BasicBehaviors_FunctionBehavior, OpaqueBehavior, fUML_Communications_Trigger, NamedElement, Communications_Event, fUML_Communications_Event, PackageableElement, fUML_Communications_Signal, Kernel_Property, fUML_Communications_SignalEvent, MessageEvent, Communications_Signal, fUML_Communications_MessageEvent, Event, fUML_Communications_Reception, BehavioralFeature, fUML_Kernel_ValueSpecification, TypedElement, fUML_Kernel_TypedElement, Kernel_Type, fUML_Kernel_NamedElement, Element, Kernel_Namespace, Kernel_Element, Kernel_Comment, fUML_Kernel_Comment, fUML_Kernel_Namespace, Kernel_NamedElement, Kernel_ElementImport, Kernel_PackageImport, Kernel_PackageableElement, fUML_Kernel_ElementImport, fUML_Kernel_PackageableElement, fUML_Kernel_PackageImport, Kernel_Package, fUML_Kernel_Package, fUML_Kernel_Element, fUML_Kernel_Type, fUML_Kernel_StructuralFeature, Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement, fUML_Kernel_Feature, RedefinableElement, Kernel_Classifier, fUML_Kernel_RedefinableElement, Kernel_RedefinableElement, fUML_Kernel_Classifier, Kernel_Generalization, fUML_Kernel_Generalization, fUML_Kernel_Property, StructuralFeature, Kernel_Association, Kernel_DataType, Kernel_Class, Kernel_ValueSpecification, fUML_Kernel_Association, fUML_Kernel_DataType, fUML_Kernel_MultiplicityElement, fUML_Kernel_BehavioralFeature, Feature, fUML_Kernel_Parameter, fUML_Kernel_Operation, fUML_Kernel_PrimitiveType, DataType, fUML_Kernel_Enumeration, Kernel_Operation, fUML_Kernel_InstanceSpecification, Kernel_Slot, fUML_Kernel_Slot, Kernel_StructuralFeature, Kernel_InstanceSpecification, fUML_Kernel_InstanceValue, ValueSpecification, fUML_Kernel_LiteralBoolean, LiteralSpecification, fUML_Kernel_LiteralSpecification, fUML_Kernel_LiteralInteger, fUML_Kernel_LiteralNull, fUML_Kernel_LiteralString, fUML_Kernel_LiteralUnlimitedNatural, Kernel_EnumerationLiteral, fUML_Kernel_EnumerationLiteral, InstanceSpecification, Kernel_Enumeration, fUML_Kernel_Class, BehavioredClassifier, Communications_Reception, fUML_IntermediateActivities_ObjectFlow, ActivityEdge, fUML_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, IntermediateActivities_ObjectFlow, fUML_IntermediateActivities_ActivityFinalNode, FinalNode, fUML_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, fUML_IntermediateActivities_ActivityNode, fUML_IntermediateActivities_ObjectNode, fUML_IntermediateActivities_MergeNode, ControlNode, fUML_IntermediateActivities_ControlNode, ActivityNode, fUML_IntermediateActivities_JoinNode, fUML_IntermediateActivities_InitialNode, fUML_IntermediateActivities_FinalNode, fUML_IntermediateActivities_ForkNode, fUML_IntermediateActivities_ControlFlow, fUML_IntermediateActivities_DecisionNode, CompleteStructuredActivities_Clause, fUML_IntermediateActivities_ActivityParameterNode, ObjectNode, fUML_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, fUML_CompleteStructuredActivities_ExecutableNode, fUML_CompleteStructuredActivities_Clause, fUML_CompleteStructuredActivities_ConditionalNode, fUML_ExtraStructuredActivities_ExpansionRegion, fUML_CompleteStructuredActivities_StructuredActivityNode, Action, fUML_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, fUML_IntermediateActions_WriteLinkAction, LinkAction, ExtraStructuredActivities_ExpansionNode, fUML_IntermediateActions_StructuralFeatureAction, fUML_IntermediateActions_TestIdentityAction, fUML_IntermediateActions_ValueSpecificationAction, fUML_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, fUML_IntermediateActions_LinkEndData, fUML_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, fUML_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, fUML_IntermediateActions_ReadLinkAction, fUML_IntermediateActions_ReadSelfAction, fUML_IntermediateActions_ReadStructuralFeatureAction, fUML_IntermediateActions_LinkEndCreationData, LinkEndData, fUML_IntermediateActions_LinkEndDestructionData, fUML_IntermediateActions_ClearAssociationAction, fUML_IntermediateActions_ClearStructuralFeatureAction, fUML_IntermediateActions_CreateLinkAction, WriteLinkAction, fUML_IntermediateActions_CreateObjectAction, fUML_IntermediateActions_DestroyLinkAction, fUML_IntermediateActions_DestroyObjectAction, fUML_IntermediateActions_AddStructuralFeatureValueAction, fUML_CompleteActions_StartClassifierBehaviorAction, fUML_CompleteActions_StartObjectBehaviorAction, CallAction, fUML_CompleteActions_ReduceAction, fUML_CompleteActions_ReadExtentAction, fUML_CompleteActions_ReadIsClassifiedObjectAction, fUML_CompleteActions_ReclassifyObjectAction, fUML_CompleteActions_AcceptEventAction, Communications_Trigger, fUML_BasicActions_Action, ExecutableNode, fUML_BasicActions_InputPin, Pin, fUML_BasicActions_Pin, IntermediateActivities_ObjectNode, fUML_BasicActions_CallAction, InvocationAction, fUML_BasicActions_InvocationAction, fUML_BasicActions_SendSignalAction, fUML_Kernel_StringValue, fUML_BasicActions_CallBehaviorAction, fUML_BasicActions_CallOperationAction, fUML_BasicActions_OutputPin, fUML_Kernel_StructuredValue, Value, fUML_Kernel_FeatureValue, Kernel_Value, fUML_Kernel_UnlimitedNaturalValue, PrimitiveValue, fUML_Kernel_PrimitiveValue, Kernel_PrimitiveType, fUML_Kernel_Reference, StructuredValue, Kernel_Object, fUML_Kernel_Object, ExtensionalValue, fUML_Kernel_ExtensionalValue, CompoundValue, fUML_Kernel_CompoundValue, Kernel_FeatureValue, fUML_Kernel_Link, fUML_Kernel_IntegerValue, fUML_Kernel_EnumerationValue, fUML_Kernel_DataValue, fUML_Kernel_BooleanValue, fUML_Kernel_Value, SemanticVisitor, fUML_LociL1_SemanticVisitor, CallConcurrencyKind, VisibilityKind, AggregationKind, ParameterDirectionKind, ExpansionKind},
    associations={specification0, ownedParameter1, context2, ownedBehavior4, classifierBehavior5, event8, ownedAttribute9, signal10, signal11, type13, namespace14, ownedElement15, owner16, ownedComment18, annotatedElement19, member20, elementImport21, packageImport22, importedMember24, ownedMember26, importedElement27, importingNamespace29, importedPackage31, importingNamespace32, feature47, packagedElement34, ownedType36, nestedPackage37, nestingPackage38, package40, featuringClassifier42, redefinedElement43, redefinitionContext44, generalization46, inheritedMember48, attribute50, general53, general56, specific58, owningAssociation60, association61, datatype63, class_64, opposite66, endType68, memberEnd70, navigableOwnedEnd71, ownedEnd74, ownedAttribute76, class_85, upperValue78, lowerValue79, ownedParameter82, method84, redefinedOperation87, type88, classifier91, slot93, definingFeature94, value95, owningInstance98, instance99, guard118, ownedLiteral100, enumeration101, ownedAttribute102, ownedOperation104, superClass106, ownedReception107, nestedClassifier109, activity112, source113, target114, inStructuredNode116, decisionInputFlow135, node120, edge122, inStructuredNode124, activity126, outgoing129, incoming131, decisionInput133, predecessorClause164, parameter137, decider139, test140, bodyOutput142, loopVariableInput145, bodyPart147, result150, loopVariable153, setupPart156, test159, body161, successorClause165, decider167, bodyOutput170, clause173, result174, node177, edge179, structuredNodeOutput182, structuredNodeInput184, regionAsOutput187, regionAsInput188, inputElement190, outputElement191, structuralFeature193, object195, second198, result200, first203, value206, result208, insertAt233, endData211, inputValue212, value215, end217, value220, result222, removeAt225, result227, result229, result231, object252, destroyAt235, association237, object238, result241, result243, classifier245, target248, insertAt250, newClassifier282, object254, reducer256, result258, collection261, result264, classifier266, classifier269, result271, object274, oldClassifier277, object279, result285, trigger287, output289, context291, input294, result297, argument299, target301, signal303, behavior306, operation308, target310, feature313, values315, type317, referent318, types319, featureValues321, type322, literal324, type325, type327},
    generalizations={gen_fUML_BasicBehaviors_OpaqueBehavior_Behavior, gen_fUML_BasicBehaviors_Behavior_Class, gen_fUML_BasicBehaviors_BehavioredClassifier_Classifier, gen_fUML_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_fUML_Communications_Trigger_NamedElement, gen_fUML_Communications_Event_PackageableElement, gen_fUML_Communications_Signal_Classifier, gen_fUML_Communications_SignalEvent_MessageEvent, gen_fUML_Communications_MessageEvent_Event, gen_fUML_Communications_Reception_BehavioralFeature, gen_fUML_Kernel_ValueSpecification_TypedElement, gen_fUML_Kernel_TypedElement_NamedElement, gen_fUML_Kernel_NamedElement_Element, gen_fUML_Kernel_Namespace_NamedElement, gen_fUML_Kernel_ElementImport_Element, gen_fUML_Kernel_PackageableElement_NamedElement, gen_fUML_Kernel_PackageImport_Element, gen_fUML_Kernel_Package_Kernel_Namespace, gen_fUML_Kernel_Package_Kernel_PackageableElement, gen_fUML_Kernel_Type_PackageableElement, gen_fUML_Kernel_StructuralFeature_Kernel_Feature, gen_fUML_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_fUML_Kernel_StructuralFeature_Kernel_TypedElement, gen_fUML_Kernel_Feature_RedefinableElement, gen_fUML_Kernel_RedefinableElement_NamedElement, gen_fUML_Kernel_Classifier_Kernel_Namespace, gen_fUML_Kernel_Classifier_Kernel_Type, gen_fUML_Kernel_Generalization_Element, gen_fUML_Kernel_Property_StructuralFeature, gen_fUML_Kernel_Association_Classifier, gen_fUML_Kernel_DataType_Classifier, gen_fUML_Kernel_MultiplicityElement_Element, gen_fUML_Kernel_BehavioralFeature_Feature, gen_fUML_Kernel_Parameter_Kernel_MultiplicityElement, gen_fUML_Kernel_Parameter_Kernel_TypedElement, gen_fUML_Kernel_Operation_BehavioralFeature, gen_fUML_Kernel_PrimitiveType_DataType, gen_fUML_Kernel_Enumeration_DataType, gen_fUML_Kernel_InstanceSpecification_NamedElement, gen_fUML_Kernel_Slot_Element, gen_fUML_Kernel_InstanceValue_ValueSpecification, gen_fUML_Kernel_LiteralBoolean_LiteralSpecification, gen_fUML_Kernel_LiteralSpecification_ValueSpecification, gen_fUML_Kernel_LiteralInteger_LiteralSpecification, gen_fUML_Kernel_LiteralNull_LiteralSpecification, gen_fUML_Kernel_LiteralString_LiteralSpecification, gen_fUML_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_fUML_Kernel_EnumerationLiteral_InstanceSpecification, gen_fUML_Kernel_Class_BehavioredClassifier, gen_fUML_IntermediateActivities_ObjectFlow_ActivityEdge, gen_fUML_IntermediateActivities_ActivityEdge_RedefinableElement, gen_fUML_IntermediateActivities_Activity_Behavior, gen_fUML_IntermediateActivities_ActivityNode_RedefinableElement, gen_fUML_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_fUML_IntermediateActivities_ObjectNode_Kernel_TypedElement, gen_fUML_IntermediateActivities_MergeNode_ControlNode, gen_fUML_IntermediateActivities_ControlNode_ActivityNode, gen_fUML_IntermediateActivities_JoinNode_ControlNode, gen_fUML_IntermediateActivities_InitialNode_ControlNode, gen_fUML_IntermediateActivities_FinalNode_ControlNode, gen_fUML_IntermediateActivities_ForkNode_ControlNode, gen_fUML_IntermediateActivities_ControlFlow_ActivityEdge, gen_fUML_IntermediateActivities_DecisionNode_ControlNode, gen_fUML_IntermediateActivities_ActivityFinalNode_FinalNode, gen_fUML_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_fUML_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_fUML_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_fUML_CompleteStructuredActivities_Clause_Element, gen_fUML_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_fUML_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_fUML_CompleteStructuredActivities_StructuredActivityNode_Action, gen_fUML_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_fUML_IntermediateActions_WriteLinkAction_LinkAction, gen_fUML_IntermediateActions_StructuralFeatureAction_Action, gen_fUML_IntermediateActions_TestIdentityAction_Action, gen_fUML_IntermediateActions_ValueSpecificationAction_Action, gen_fUML_IntermediateActions_LinkAction_Action, gen_fUML_IntermediateActions_LinkEndData_Element, gen_fUML_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fUML_IntermediateActions_ReadLinkAction_LinkAction, gen_fUML_IntermediateActions_ReadSelfAction_Action, gen_fUML_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_LinkEndCreationData_LinkEndData, gen_fUML_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_fUML_IntermediateActions_ClearAssociationAction_Action, gen_fUML_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_fUML_IntermediateActions_CreateObjectAction_Action, gen_fUML_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_fUML_IntermediateActions_DestroyObjectAction_Action, gen_fUML_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fUML_CompleteActions_StartClassifierBehaviorAction_Action, gen_fUML_CompleteActions_StartObjectBehaviorAction_CallAction, gen_fUML_CompleteActions_ReduceAction_Action, gen_fUML_CompleteActions_ReadExtentAction_Action, gen_fUML_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_fUML_CompleteActions_ReclassifyObjectAction_Action, gen_fUML_CompleteActions_AcceptEventAction_Action, gen_fUML_BasicActions_Action_ExecutableNode, gen_fUML_BasicActions_InputPin_Pin, gen_fUML_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_fUML_BasicActions_Pin_Kernel_MultiplicityElement, gen_fUML_BasicActions_CallAction_InvocationAction, gen_fUML_BasicActions_InvocationAction_Action, gen_fUML_BasicActions_SendSignalAction_InvocationAction, gen_fUML_Kernel_StringValue_PrimitiveValue, gen_fUML_BasicActions_CallBehaviorAction_CallAction, gen_fUML_BasicActions_CallOperationAction_CallAction, gen_fUML_BasicActions_OutputPin_Pin, gen_fUML_Kernel_StructuredValue_Value, gen_fUML_Kernel_UnlimitedNaturalValue_PrimitiveValue, gen_fUML_Kernel_PrimitiveValue_Value, gen_fUML_Kernel_Reference_StructuredValue, gen_fUML_Kernel_Object_ExtensionalValue, gen_fUML_Kernel_ExtensionalValue_CompoundValue, gen_fUML_Kernel_CompoundValue_StructuredValue, gen_fUML_Kernel_Link_ExtensionalValue, gen_fUML_Kernel_IntegerValue_PrimitiveValue, gen_fUML_Kernel_EnumerationValue_Value, gen_fUML_Kernel_DataValue_CompoundValue, gen_fUML_Kernel_BooleanValue_PrimitiveValue, gen_fUML_Kernel_Value_SemanticVisitor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)