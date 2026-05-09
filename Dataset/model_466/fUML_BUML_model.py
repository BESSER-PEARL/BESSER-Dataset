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
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
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
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors_BehavioredClassifier")
fuml_BasicBehaviors_BehavioredClassifier = Class(name="fuml_BasicBehaviors_BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors_Behavior")
fuml_BasicBehaviors_OpaqueBehavior = Class(name="fuml_BasicBehaviors_OpaqueBehavior")
Behavior = Class(name="Behavior")
fuml_BasicBehaviors_Behavior = Class(name="fuml_BasicBehaviors_Behavior", is_abstract=True)
Class_ = Class(name="Class")
Kernel_BehavioralFeature = Class(name="Kernel_BehavioralFeature")
Kernel_Parameter = Class(name="Kernel_Parameter")
fuml_Kernel_ValueSpecification = Class(name="fuml_Kernel_ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
fuml_Kernel_TypedElement = Class(name="fuml_Kernel_TypedElement")
Kernel_Type = Class(name="Kernel_Type")
fuml_Kernel_NamedElement = Class(name="fuml_Kernel_NamedElement", is_abstract=True)
Element = Class(name="Element")
fuml_BasicBehaviors_FunctionBehavior = Class(name="fuml_BasicBehaviors_FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
fuml_Communications_Trigger = Class(name="fuml_Communications_Trigger")
NamedElement = Class(name="NamedElement")
Communications_Event = Class(name="Communications_Event")
fuml_Communications_Event = Class(name="fuml_Communications_Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
fuml_Communications_Signal = Class(name="fuml_Communications_Signal")
Kernel_Property = Class(name="Kernel_Property")
fuml_Communications_SignalEvent = Class(name="fuml_Communications_SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications_Signal")
fuml_Communications_MessageEvent = Class(name="fuml_Communications_MessageEvent", is_abstract=True)
Event = Class(name="Event")
fuml_Communications_Reception = Class(name="fuml_Communications_Reception")
BehavioralFeature = Class(name="BehavioralFeature")
fuml_Kernel_Namespace = Class(name="fuml_Kernel_Namespace", is_abstract=True)
Kernel_NamedElement = Class(name="Kernel_NamedElement")
Kernel_ElementImport = Class(name="Kernel_ElementImport")
Kernel_Namespace = Class(name="Kernel_Namespace")
fuml_Kernel_Element = Class(name="fuml_Kernel_Element", is_abstract=True)
Kernel_Element = Class(name="Kernel_Element")
Kernel_Comment = Class(name="Kernel_Comment")
fuml_Kernel_Comment = Class(name="fuml_Kernel_Comment")
fuml_Kernel_Package = Class(name="fuml_Kernel_Package")
Kernel_PackageImport = Class(name="Kernel_PackageImport")
Kernel_PackageableElement = Class(name="Kernel_PackageableElement")
fuml_Kernel_ElementImport = Class(name="fuml_Kernel_ElementImport")
fuml_Kernel_PackageableElement = Class(name="fuml_Kernel_PackageableElement", is_abstract=True)
fuml_Kernel_PackageImport = Class(name="fuml_Kernel_PackageImport")
Kernel_Package = Class(name="Kernel_Package")
fuml_Kernel_Classifier = Class(name="fuml_Kernel_Classifier", is_abstract=True)
fuml_Kernel_Type = Class(name="fuml_Kernel_Type", is_abstract=True)
fuml_Kernel_StructuralFeature = Class(name="fuml_Kernel_StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel_Feature")
Kernel_MultiplicityElement = Class(name="Kernel_MultiplicityElement")
Kernel_TypedElement = Class(name="Kernel_TypedElement")
fuml_Kernel_Feature = Class(name="fuml_Kernel_Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Kernel_Classifier = Class(name="Kernel_Classifier")
fuml_Kernel_RedefinableElement = Class(name="fuml_Kernel_RedefinableElement", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel_RedefinableElement")
Kernel_Association = Class(name="Kernel_Association")
Kernel_Generalization = Class(name="Kernel_Generalization")
fuml_Kernel_Generalization = Class(name="fuml_Kernel_Generalization")
fuml_Kernel_Property = Class(name="fuml_Kernel_Property")
StructuralFeature = Class(name="StructuralFeature")
Kernel_DataType = Class(name="Kernel_DataType")
Kernel_Class = Class(name="Kernel_Class")
fuml_Kernel_Association = Class(name="fuml_Kernel_Association")
fuml_Kernel_DataType = Class(name="fuml_Kernel_DataType")
fuml_Kernel_MultiplicityElement = Class(name="fuml_Kernel_MultiplicityElement")
Kernel_ValueSpecification = Class(name="Kernel_ValueSpecification")
fuml_Kernel_BehavioralFeature = Class(name="fuml_Kernel_BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
fuml_Kernel_Parameter = Class(name="fuml_Kernel_Parameter")
fuml_Kernel_Operation = Class(name="fuml_Kernel_Operation")
Kernel_Operation = Class(name="Kernel_Operation")
fuml_Kernel_InstanceSpecification = Class(name="fuml_Kernel_InstanceSpecification")
fuml_Kernel_Enumeration = Class(name="fuml_Kernel_Enumeration")
Kernel_EnumerationLiteral = Class(name="Kernel_EnumerationLiteral")
Kernel_Slot = Class(name="Kernel_Slot")
fuml_Kernel_Slot = Class(name="fuml_Kernel_Slot")
Kernel_StructuralFeature = Class(name="Kernel_StructuralFeature")
Kernel_InstanceSpecification = Class(name="Kernel_InstanceSpecification")
fuml_Kernel_InstanceValue = Class(name="fuml_Kernel_InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
fuml_Kernel_LiteralBoolean = Class(name="fuml_Kernel_LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
fuml_Kernel_LiteralSpecification = Class(name="fuml_Kernel_LiteralSpecification", is_abstract=True)
fuml_Kernel_LiteralInteger = Class(name="fuml_Kernel_LiteralInteger")
fuml_Kernel_LiteralNull = Class(name="fuml_Kernel_LiteralNull")
fuml_Kernel_LiteralString = Class(name="fuml_Kernel_LiteralString")
fuml_Kernel_LiteralUnlimitedNatural = Class(name="fuml_Kernel_LiteralUnlimitedNatural")
fuml_Kernel_PrimitiveType = Class(name="fuml_Kernel_PrimitiveType")
DataType = Class(name="DataType")
fuml_IntermediateActivities_Activity = Class(name="fuml_IntermediateActivities_Activity")
fuml_Kernel_EnumerationLiteral = Class(name="fuml_Kernel_EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_Enumeration = Class(name="Kernel_Enumeration")
fuml_Kernel_Class = Class(name="fuml_Kernel_Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
Communications_Reception = Class(name="Communications_Reception")
fuml_IntermediateActivities_ObjectFlow = Class(name="fuml_IntermediateActivities_ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
fuml_IntermediateActivities_ActivityEdge = Class(name="fuml_IntermediateActivities_ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities_Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities_ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities_StructuredActivityNode")
fuml_CompleteStructuredActivities_LoopNode = Class(name="fuml_CompleteStructuredActivities_LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions_OutputPin")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities_ActivityEdge")
fuml_IntermediateActivities_ActivityNode = Class(name="fuml_IntermediateActivities_ActivityNode", is_abstract=True)
fuml_IntermediateActivities_ObjectNode = Class(name="fuml_IntermediateActivities_ObjectNode", is_abstract=True)
fuml_IntermediateActivities_MergeNode = Class(name="fuml_IntermediateActivities_MergeNode")
ControlNode = Class(name="ControlNode")
fuml_IntermediateActivities_ControlNode = Class(name="fuml_IntermediateActivities_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
fuml_IntermediateActivities_JoinNode = Class(name="fuml_IntermediateActivities_JoinNode")
fuml_IntermediateActivities_InitialNode = Class(name="fuml_IntermediateActivities_InitialNode")
fuml_IntermediateActivities_FinalNode = Class(name="fuml_IntermediateActivities_FinalNode", is_abstract=True)
fuml_IntermediateActivities_ForkNode = Class(name="fuml_IntermediateActivities_ForkNode")
fuml_IntermediateActivities_ControlFlow = Class(name="fuml_IntermediateActivities_ControlFlow")
fuml_IntermediateActivities_DecisionNode = Class(name="fuml_IntermediateActivities_DecisionNode")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities_ObjectFlow")
fuml_IntermediateActivities_ActivityFinalNode = Class(name="fuml_IntermediateActivities_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
fuml_IntermediateActivities_ActivityParameterNode = Class(name="fuml_IntermediateActivities_ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities_ExecutableNode")
BasicActions_InputPin = Class(name="BasicActions_InputPin")
fuml_CompleteStructuredActivities_ExecutableNode = Class(name="fuml_CompleteStructuredActivities_ExecutableNode", is_abstract=True)
fuml_CompleteStructuredActivities_Clause = Class(name="fuml_CompleteStructuredActivities_Clause")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities_Clause")
fuml_CompleteStructuredActivities_ConditionalNode = Class(name="fuml_CompleteStructuredActivities_ConditionalNode")
fuml_CompleteStructuredActivities_StructuredActivityNode = Class(name="fuml_CompleteStructuredActivities_StructuredActivityNode")
Action = Class(name="Action")
fuml_ExtraStructuredActivities_ExpansionNode = Class(name="fuml_ExtraStructuredActivities_ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities_ExpansionRegion")
fuml_ExtraStructuredActivities_ExpansionRegion = Class(name="fuml_ExtraStructuredActivities_ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities_ExpansionNode")
fuml_IntermediateActions_StructuralFeatureAction = Class(name="fuml_IntermediateActions_StructuralFeatureAction", is_abstract=True)
fuml_IntermediateActions_TestIdentityAction = Class(name="fuml_IntermediateActions_TestIdentityAction")
fuml_IntermediateActions_ReadLinkAction = Class(name="fuml_IntermediateActions_ReadLinkAction")
fuml_IntermediateActions_ValueSpecificationAction = Class(name="fuml_IntermediateActions_ValueSpecificationAction")
fuml_IntermediateActions_ReadSelfAction = Class(name="fuml_IntermediateActions_ReadSelfAction")
fuml_IntermediateActions_WriteLinkAction = Class(name="fuml_IntermediateActions_WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
fuml_IntermediateActions_LinkAction = Class(name="fuml_IntermediateActions_LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions_LinkEndData")
fuml_IntermediateActions_LinkEndData = Class(name="fuml_IntermediateActions_LinkEndData")
fuml_IntermediateActions_WriteStructuralFeatureAction = Class(name="fuml_IntermediateActions_WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
fuml_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="fuml_IntermediateActions_RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
fuml_IntermediateActions_DestroyLinkAction = Class(name="fuml_IntermediateActions_DestroyLinkAction")
fuml_IntermediateActions_DestroyObjectAction = Class(name="fuml_IntermediateActions_DestroyObjectAction")
fuml_IntermediateActions_ReadStructuralFeatureAction = Class(name="fuml_IntermediateActions_ReadStructuralFeatureAction")
fuml_IntermediateActions_LinkEndCreationData = Class(name="fuml_IntermediateActions_LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
fuml_IntermediateActions_LinkEndDestructionData = Class(name="fuml_IntermediateActions_LinkEndDestructionData")
fuml_IntermediateActions_ClearAssociationAction = Class(name="fuml_IntermediateActions_ClearAssociationAction")
fuml_IntermediateActions_ClearStructuralFeatureAction = Class(name="fuml_IntermediateActions_ClearStructuralFeatureAction")
fuml_IntermediateActions_CreateLinkAction = Class(name="fuml_IntermediateActions_CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
fuml_IntermediateActions_CreateObjectAction = Class(name="fuml_IntermediateActions_CreateObjectAction")
fuml_CompleteActions_ReadIsClassifiedObjectAction = Class(name="fuml_CompleteActions_ReadIsClassifiedObjectAction")
fuml_IntermediateActions_AddStructuralFeatureValueAction = Class(name="fuml_IntermediateActions_AddStructuralFeatureValueAction")
fuml_CompleteActions_StartClassifierBehaviorAction = Class(name="fuml_CompleteActions_StartClassifierBehaviorAction")
fuml_CompleteActions_StartObjectBehaviorAction = Class(name="fuml_CompleteActions_StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
fuml_CompleteActions_ReduceAction = Class(name="fuml_CompleteActions_ReduceAction")
fuml_CompleteActions_ReadExtentAction = Class(name="fuml_CompleteActions_ReadExtentAction")
fuml_BasicActions_InputPin = Class(name="fuml_BasicActions_InputPin")
Pin = Class(name="Pin")
fuml_BasicActions_Pin = Class(name="fuml_BasicActions_Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities_ObjectNode")
fuml_BasicActions_CallAction = Class(name="fuml_BasicActions_CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
fuml_CompleteActions_ReclassifyObjectAction = Class(name="fuml_CompleteActions_ReclassifyObjectAction")
fuml_CompleteActions_AcceptEventAction = Class(name="fuml_CompleteActions_AcceptEventAction")
Communications_Trigger = Class(name="Communications_Trigger")
fuml_BasicActions_Action = Class(name="fuml_BasicActions_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
fuml_BasicActions_OutputPin = Class(name="fuml_BasicActions_OutputPin")
fuml_BasicActions_InvocationAction = Class(name="fuml_BasicActions_InvocationAction", is_abstract=True)
fuml_Kernel_StructuredValue = Class(name="fuml_Kernel_StructuredValue", is_abstract=True)
Value = Class(name="Value")
fuml_Kernel_FeatureValue = Class(name="fuml_Kernel_FeatureValue")
fuml_BasicActions_SendSignalAction = Class(name="fuml_BasicActions_SendSignalAction")
fuml_BasicActions_CallBehaviorAction = Class(name="fuml_BasicActions_CallBehaviorAction")
fuml_BasicActions_CallOperationAction = Class(name="fuml_BasicActions_CallOperationAction")
Kernel_Object = Class(name="Kernel_Object")
fuml_Kernel_Object = Class(name="fuml_Kernel_Object")
ExtensionalValue = Class(name="ExtensionalValue")
fuml_Kernel_ExtensionalValue = Class(name="fuml_Kernel_ExtensionalValue", is_abstract=True)
CompoundValue = Class(name="CompoundValue")
LociL1_Locus = Class(name="LociL1_Locus")
fuml_Kernel_CompoundValue = Class(name="fuml_Kernel_CompoundValue", is_abstract=True)
Kernel_FeatureValue = Class(name="Kernel_FeatureValue")
fuml_Kernel_Link = Class(name="fuml_Kernel_Link")
fuml_Kernel_IntegerValue = Class(name="fuml_Kernel_IntegerValue")
fuml_Kernel_EnumerationValue = Class(name="fuml_Kernel_EnumerationValue")
Kernel_Value = Class(name="Kernel_Value")
fuml_Kernel_UnlimitedNaturalValue = Class(name="fuml_Kernel_UnlimitedNaturalValue")
PrimitiveValue = Class(name="PrimitiveValue")
fuml_Kernel_PrimitiveValue = Class(name="fuml_Kernel_PrimitiveValue", is_abstract=True)
Kernel_PrimitiveType = Class(name="Kernel_PrimitiveType")
fuml_Kernel_StringValue = Class(name="fuml_Kernel_StringValue")
fuml_Kernel_Reference = Class(name="fuml_Kernel_Reference")
StructuredValue = Class(name="StructuredValue")
fuml_LociL1_SemanticVisitor = Class(name="fuml_LociL1_SemanticVisitor", is_abstract=True)
fuml_LociL1_Locus = Class(name="fuml_LociL1_Locus")
Kernel_ExtensionalValue = Class(name="Kernel_ExtensionalValue")
fuml_BasicBehaviors_ParameterValue = Class(name="fuml_BasicBehaviors_ParameterValue")
fuml_Kernel_DataValue = Class(name="fuml_Kernel_DataValue")
fuml_Kernel_BooleanValue = Class(name="fuml_Kernel_BooleanValue")
fuml_Kernel_Value = Class(name="fuml_Kernel_Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")

# BasicBehaviors_BehavioredClassifier class attributes and methods

# fuml_BasicBehaviors_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# BasicBehaviors_Behavior class attributes and methods

# fuml_BasicBehaviors_OpaqueBehavior class attributes and methods
fuml_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
fuml_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
fuml_BasicBehaviors_OpaqueBehavior.attributes={fuml_BasicBehaviors_OpaqueBehavior_language, fuml_BasicBehaviors_OpaqueBehavior_body}

# Behavior class attributes and methods

# fuml_BasicBehaviors_Behavior class attributes and methods
fuml_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
fuml_BasicBehaviors_Behavior.attributes={fuml_BasicBehaviors_Behavior_reentrant}

# Class class attributes and methods

# Kernel_BehavioralFeature class attributes and methods

# Kernel_Parameter class attributes and methods

# fuml_Kernel_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# fuml_Kernel_TypedElement class attributes and methods

# Kernel_Type class attributes and methods

# fuml_Kernel_NamedElement class attributes and methods
fuml_Kernel_NamedElement_name: Property = Property(name="name", type=StringType)
fuml_Kernel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
fuml_Kernel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
fuml_Kernel_NamedElement.attributes={fuml_Kernel_NamedElement_name, fuml_Kernel_NamedElement_qualifiedName, fuml_Kernel_NamedElement_visibility}

# Element class attributes and methods

# fuml_BasicBehaviors_FunctionBehavior class attributes and methods

# OpaqueBehavior class attributes and methods

# fuml_Communications_Trigger class attributes and methods

# NamedElement class attributes and methods

# Communications_Event class attributes and methods

# fuml_Communications_Event class attributes and methods

# PackageableElement class attributes and methods

# fuml_Communications_Signal class attributes and methods

# Kernel_Property class attributes and methods

# fuml_Communications_SignalEvent class attributes and methods

# MessageEvent class attributes and methods

# Communications_Signal class attributes and methods

# fuml_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# fuml_Communications_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# fuml_Kernel_Namespace class attributes and methods

# Kernel_NamedElement class attributes and methods

# Kernel_ElementImport class attributes and methods

# Kernel_Namespace class attributes and methods

# fuml_Kernel_Element class attributes and methods

# Kernel_Element class attributes and methods

# Kernel_Comment class attributes and methods

# fuml_Kernel_Comment class attributes and methods
fuml_Kernel_Comment_body: Property = Property(name="body", type=StringType)
fuml_Kernel_Comment.attributes={fuml_Kernel_Comment_body}

# fuml_Kernel_Package class attributes and methods

# Kernel_PackageImport class attributes and methods

# Kernel_PackageableElement class attributes and methods

# fuml_Kernel_ElementImport class attributes and methods
fuml_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
fuml_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
fuml_Kernel_ElementImport.attributes={fuml_Kernel_ElementImport_visibility, fuml_Kernel_ElementImport_alias}

# fuml_Kernel_PackageableElement class attributes and methods

# fuml_Kernel_PackageImport class attributes and methods
fuml_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
fuml_Kernel_PackageImport.attributes={fuml_Kernel_PackageImport_visibility}

# Kernel_Package class attributes and methods

# fuml_Kernel_Classifier class attributes and methods
fuml_Kernel_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
fuml_Kernel_Classifier_finalSpecialization: Property = Property(name="finalSpecialization", type=BooleanType)
fuml_Kernel_Classifier.attributes={fuml_Kernel_Classifier_abstract, fuml_Kernel_Classifier_finalSpecialization}

# fuml_Kernel_Type class attributes and methods

# fuml_Kernel_StructuralFeature class attributes and methods
fuml_Kernel_StructuralFeature_readOnly: Property = Property(name="readOnly", type=BooleanType)
fuml_Kernel_StructuralFeature.attributes={fuml_Kernel_StructuralFeature_readOnly}

# Kernel_Feature class attributes and methods

# Kernel_MultiplicityElement class attributes and methods

# Kernel_TypedElement class attributes and methods

# fuml_Kernel_Feature class attributes and methods
fuml_Kernel_Feature_static: Property = Property(name="static", type=BooleanType)
fuml_Kernel_Feature.attributes={fuml_Kernel_Feature_static}

# RedefinableElement class attributes and methods

# Kernel_Classifier class attributes and methods

# fuml_Kernel_RedefinableElement class attributes and methods
fuml_Kernel_RedefinableElement_leaf: Property = Property(name="leaf", type=BooleanType)
fuml_Kernel_RedefinableElement.attributes={fuml_Kernel_RedefinableElement_leaf}

# Kernel_RedefinableElement class attributes and methods

# Kernel_Association class attributes and methods

# Kernel_Generalization class attributes and methods

# fuml_Kernel_Generalization class attributes and methods
fuml_Kernel_Generalization_substitutable: Property = Property(name="substitutable", type=BooleanType)
fuml_Kernel_Generalization.attributes={fuml_Kernel_Generalization_substitutable}

# fuml_Kernel_Property class attributes and methods
fuml_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
fuml_Kernel_Property_composite: Property = Property(name="composite", type=BooleanType)
fuml_Kernel_Property_derived: Property = Property(name="derived", type=BooleanType)
fuml_Kernel_Property_derivedUnion: Property = Property(name="derivedUnion", type=BooleanType)
fuml_Kernel_Property.attributes={fuml_Kernel_Property_derived, fuml_Kernel_Property_composite, fuml_Kernel_Property_aggregation, fuml_Kernel_Property_derivedUnion}

# StructuralFeature class attributes and methods

# Kernel_DataType class attributes and methods

# Kernel_Class class attributes and methods

# fuml_Kernel_Association class attributes and methods
fuml_Kernel_Association_derived: Property = Property(name="derived", type=BooleanType)
fuml_Kernel_Association.attributes={fuml_Kernel_Association_derived}

# fuml_Kernel_DataType class attributes and methods

# fuml_Kernel_MultiplicityElement class attributes and methods
fuml_Kernel_MultiplicityElement_ordered: Property = Property(name="ordered", type=BooleanType)
fuml_Kernel_MultiplicityElement_unique: Property = Property(name="unique", type=BooleanType)
fuml_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
fuml_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
fuml_Kernel_MultiplicityElement.attributes={fuml_Kernel_MultiplicityElement_lower, fuml_Kernel_MultiplicityElement_upper, fuml_Kernel_MultiplicityElement_unique, fuml_Kernel_MultiplicityElement_ordered}

# Kernel_ValueSpecification class attributes and methods

# fuml_Kernel_BehavioralFeature class attributes and methods
fuml_Kernel_BehavioralFeature_abstract: Property = Property(name="abstract", type=BooleanType)
fuml_Kernel_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
fuml_Kernel_BehavioralFeature.attributes={fuml_Kernel_BehavioralFeature_abstract, fuml_Kernel_BehavioralFeature_concurrency}

# Feature class attributes and methods

# fuml_Kernel_Parameter class attributes and methods
fuml_Kernel_Parameter_direction: Property = Property(name="direction", type=StringType)
fuml_Kernel_Parameter.attributes={fuml_Kernel_Parameter_direction}

# fuml_Kernel_Operation class attributes and methods
fuml_Kernel_Operation_query: Property = Property(name="query", type=BooleanType)
fuml_Kernel_Operation_ordered: Property = Property(name="ordered", type=BooleanType)
fuml_Kernel_Operation_unique: Property = Property(name="unique", type=BooleanType)
fuml_Kernel_Operation_lower: Property = Property(name="lower", type=IntegerType)
fuml_Kernel_Operation_upper: Property = Property(name="upper", type=IntegerType)
fuml_Kernel_Operation.attributes={fuml_Kernel_Operation_lower, fuml_Kernel_Operation_unique, fuml_Kernel_Operation_ordered, fuml_Kernel_Operation_query, fuml_Kernel_Operation_upper}

# Kernel_Operation class attributes and methods

# fuml_Kernel_InstanceSpecification class attributes and methods

# fuml_Kernel_Enumeration class attributes and methods

# Kernel_EnumerationLiteral class attributes and methods

# Kernel_Slot class attributes and methods

# fuml_Kernel_Slot class attributes and methods

# Kernel_StructuralFeature class attributes and methods

# Kernel_InstanceSpecification class attributes and methods

# fuml_Kernel_InstanceValue class attributes and methods

# ValueSpecification class attributes and methods

# fuml_Kernel_LiteralBoolean class attributes and methods
fuml_Kernel_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
fuml_Kernel_LiteralBoolean.attributes={fuml_Kernel_LiteralBoolean_value}

# LiteralSpecification class attributes and methods

# fuml_Kernel_LiteralSpecification class attributes and methods

# fuml_Kernel_LiteralInteger class attributes and methods
fuml_Kernel_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_LiteralInteger.attributes={fuml_Kernel_LiteralInteger_value}

# fuml_Kernel_LiteralNull class attributes and methods

# fuml_Kernel_LiteralString class attributes and methods
fuml_Kernel_LiteralString_value: Property = Property(name="value", type=StringType)
fuml_Kernel_LiteralString.attributes={fuml_Kernel_LiteralString_value}

# fuml_Kernel_LiteralUnlimitedNatural class attributes and methods
fuml_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_LiteralUnlimitedNatural.attributes={fuml_Kernel_LiteralUnlimitedNatural_value}

# fuml_Kernel_PrimitiveType class attributes and methods

# DataType class attributes and methods

# fuml_IntermediateActivities_Activity class attributes and methods
fuml_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
fuml_IntermediateActivities_Activity.attributes={fuml_IntermediateActivities_Activity_readOnly}

# fuml_Kernel_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_Enumeration class attributes and methods

# fuml_Kernel_Class class attributes and methods
fuml_Kernel_Class_active: Property = Property(name="active", type=BooleanType)
fuml_Kernel_Class.attributes={fuml_Kernel_Class_active}

# BehavioredClassifier class attributes and methods

# Communications_Reception class attributes and methods

# fuml_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# fuml_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# fuml_CompleteStructuredActivities_LoopNode class attributes and methods
fuml_CompleteStructuredActivities_LoopNode_testedFirst: Property = Property(name="testedFirst", type=BooleanType)
fuml_CompleteStructuredActivities_LoopNode.attributes={fuml_CompleteStructuredActivities_LoopNode_testedFirst}

# StructuredActivityNode class attributes and methods

# BasicActions_OutputPin class attributes and methods

# IntermediateActivities_ActivityEdge class attributes and methods

# fuml_IntermediateActivities_ActivityNode class attributes and methods

# fuml_IntermediateActivities_ObjectNode class attributes and methods

# fuml_IntermediateActivities_MergeNode class attributes and methods

# ControlNode class attributes and methods

# fuml_IntermediateActivities_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# fuml_IntermediateActivities_JoinNode class attributes and methods

# fuml_IntermediateActivities_InitialNode class attributes and methods

# fuml_IntermediateActivities_FinalNode class attributes and methods

# fuml_IntermediateActivities_ForkNode class attributes and methods

# fuml_IntermediateActivities_ControlFlow class attributes and methods

# fuml_IntermediateActivities_DecisionNode class attributes and methods

# IntermediateActivities_ObjectFlow class attributes and methods

# fuml_IntermediateActivities_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# fuml_IntermediateActivities_ActivityParameterNode class attributes and methods

# ObjectNode class attributes and methods

# CompleteStructuredActivities_ExecutableNode class attributes and methods

# BasicActions_InputPin class attributes and methods

# fuml_CompleteStructuredActivities_ExecutableNode class attributes and methods

# fuml_CompleteStructuredActivities_Clause class attributes and methods

# CompleteStructuredActivities_Clause class attributes and methods

# fuml_CompleteStructuredActivities_ConditionalNode class attributes and methods
fuml_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
fuml_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
fuml_CompleteStructuredActivities_ConditionalNode.attributes={fuml_CompleteStructuredActivities_ConditionalNode_assured, fuml_CompleteStructuredActivities_ConditionalNode_determinate}

# fuml_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
fuml_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
fuml_CompleteStructuredActivities_StructuredActivityNode.attributes={fuml_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# fuml_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# fuml_ExtraStructuredActivities_ExpansionRegion class attributes and methods
fuml_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
fuml_ExtraStructuredActivities_ExpansionRegion.attributes={fuml_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# fuml_IntermediateActions_StructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_TestIdentityAction class attributes and methods

# fuml_IntermediateActions_ReadLinkAction class attributes and methods

# fuml_IntermediateActions_ValueSpecificationAction class attributes and methods

# fuml_IntermediateActions_ReadSelfAction class attributes and methods

# fuml_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# fuml_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# fuml_IntermediateActions_LinkEndData class attributes and methods

# fuml_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
fuml_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
fuml_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={fuml_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_DestroyLinkAction class attributes and methods

# fuml_IntermediateActions_DestroyObjectAction class attributes and methods
fuml_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
fuml_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
fuml_IntermediateActions_DestroyObjectAction.attributes={fuml_IntermediateActions_DestroyObjectAction_destroyLinks, fuml_IntermediateActions_DestroyObjectAction_destroyOwnedObjects}

# fuml_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_LinkEndCreationData class attributes and methods
fuml_IntermediateActions_LinkEndCreationData_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_IntermediateActions_LinkEndCreationData.attributes={fuml_IntermediateActions_LinkEndCreationData_replaceAll}

# LinkEndData class attributes and methods

# fuml_IntermediateActions_LinkEndDestructionData class attributes and methods
fuml_IntermediateActions_LinkEndDestructionData_destroyDuplicates: Property = Property(name="destroyDuplicates", type=BooleanType)
fuml_IntermediateActions_LinkEndDestructionData.attributes={fuml_IntermediateActions_LinkEndDestructionData_destroyDuplicates}

# fuml_IntermediateActions_ClearAssociationAction class attributes and methods

# fuml_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# fuml_IntermediateActions_CreateObjectAction class attributes and methods

# fuml_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
fuml_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
fuml_CompleteActions_ReadIsClassifiedObjectAction.attributes={fuml_CompleteActions_ReadIsClassifiedObjectAction_direct}

# fuml_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
fuml_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_IntermediateActions_AddStructuralFeatureValueAction.attributes={fuml_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# fuml_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# fuml_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# fuml_CompleteActions_ReduceAction class attributes and methods
fuml_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
fuml_CompleteActions_ReduceAction.attributes={fuml_CompleteActions_ReduceAction_ordered}

# fuml_CompleteActions_ReadExtentAction class attributes and methods

# fuml_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# fuml_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# fuml_BasicActions_CallAction class attributes and methods
fuml_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
fuml_BasicActions_CallAction.attributes={fuml_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# fuml_CompleteActions_ReclassifyObjectAction class attributes and methods
fuml_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_CompleteActions_ReclassifyObjectAction.attributes={fuml_CompleteActions_ReclassifyObjectAction_replaceAll}

# fuml_CompleteActions_AcceptEventAction class attributes and methods
fuml_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
fuml_CompleteActions_AcceptEventAction.attributes={fuml_CompleteActions_AcceptEventAction_unmarshall}

# Communications_Trigger class attributes and methods

# fuml_BasicActions_Action class attributes and methods
fuml_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
fuml_BasicActions_Action.attributes={fuml_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# fuml_BasicActions_OutputPin class attributes and methods

# fuml_BasicActions_InvocationAction class attributes and methods

# fuml_Kernel_StructuredValue class attributes and methods

# Value class attributes and methods

# fuml_Kernel_FeatureValue class attributes and methods
fuml_Kernel_FeatureValue_position: Property = Property(name="position", type=IntegerType)
fuml_Kernel_FeatureValue.attributes={fuml_Kernel_FeatureValue_position}

# fuml_BasicActions_SendSignalAction class attributes and methods

# fuml_BasicActions_CallBehaviorAction class attributes and methods

# fuml_BasicActions_CallOperationAction class attributes and methods

# Kernel_Object class attributes and methods

# fuml_Kernel_Object class attributes and methods

# ExtensionalValue class attributes and methods

# fuml_Kernel_ExtensionalValue class attributes and methods

# CompoundValue class attributes and methods

# LociL1_Locus class attributes and methods

# fuml_Kernel_CompoundValue class attributes and methods

# Kernel_FeatureValue class attributes and methods

# fuml_Kernel_Link class attributes and methods

# fuml_Kernel_IntegerValue class attributes and methods
fuml_Kernel_IntegerValue_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_IntegerValue.attributes={fuml_Kernel_IntegerValue_value}

# fuml_Kernel_EnumerationValue class attributes and methods

# Kernel_Value class attributes and methods

# fuml_Kernel_UnlimitedNaturalValue class attributes and methods
fuml_Kernel_UnlimitedNaturalValue_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_UnlimitedNaturalValue.attributes={fuml_Kernel_UnlimitedNaturalValue_value}

# PrimitiveValue class attributes and methods

# fuml_Kernel_PrimitiveValue class attributes and methods

# Kernel_PrimitiveType class attributes and methods

# fuml_Kernel_StringValue class attributes and methods
fuml_Kernel_StringValue_value: Property = Property(name="value", type=StringType)
fuml_Kernel_StringValue.attributes={fuml_Kernel_StringValue_value}

# fuml_Kernel_Reference class attributes and methods

# StructuredValue class attributes and methods

# fuml_LociL1_SemanticVisitor class attributes and methods

# fuml_LociL1_Locus class attributes and methods

# Kernel_ExtensionalValue class attributes and methods

# fuml_BasicBehaviors_ParameterValue class attributes and methods

# fuml_Kernel_DataValue class attributes and methods

# fuml_Kernel_BooleanValue class attributes and methods
fuml_Kernel_BooleanValue_value: Property = Property(name="value", type=BooleanType)
fuml_Kernel_BooleanValue.attributes={fuml_Kernel_BooleanValue_value}

# fuml_Kernel_Value class attributes and methods

# SemanticVisitor class attributes and methods

# Relationships
context2: BinaryAssociation = BinaryAssociation(
    name="context2",
    ends={
        Property(name="BasicBehaviors_BehavioredClassifier", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_Behavior3", type=BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="BehavioralFeature", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=Kernel_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter1: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1",
    ends={
        Property(name="Kernel_Parameter", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_Behavior", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="Kernel_Type", type=fuml_Kernel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_TypedElement", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedBehavior4: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior4",
    ends={
        Property(name="BasicBehaviors_Behavior", type=fuml_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_BehavioredClassifier", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior5: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior5",
    ends={
        Property(name="BasicBehaviors_Behavior7", type=fuml_BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_BehavioredClassifier6", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="Communications_Event", type=fuml_Communications_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Communications_Trigger", type=Communications_Event, multiplicity=Multiplicity(1, 1))
    }
)
ownedAttribute9: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute9",
    ends={
        Property(name="Kernel_Property", type=fuml_Communications_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Communications_Signal", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal10: BinaryAssociation = BinaryAssociation(
    name="signal10",
    ends={
        Property(name="Communications_Signal", type=fuml_Communications_SignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Communications_SignalEvent", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
signal11: BinaryAssociation = BinaryAssociation(
    name="signal11",
    ends={
        Property(name="Communications_Signal12", type=fuml_Communications_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Communications_Reception", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
member20: BinaryAssociation = BinaryAssociation(
    name="member20",
    ends={
        Property(name="Kernel_NamedElement", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport21: BinaryAssociation = BinaryAssociation(
    name="elementImport21",
    ends={
        Property(name="ElementImport", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=Kernel_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="Namespace", type=fuml_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=Kernel_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement15: BinaryAssociation = BinaryAssociation(
    name="ownedElement15",
    ends={
        Property(name="Element", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Element17", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Kernel_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment18: BinaryAssociation = BinaryAssociation(
    name="ownedComment18",
    ends={
        Property(name="Kernel_Comment", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Element", type=Kernel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement19: BinaryAssociation = BinaryAssociation(
    name="annotatedElement19",
    ends={
        Property(name="Kernel_Element", type=fuml_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Comment", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement34: BinaryAssociation = BinaryAssociation(
    name="packagedElement34",
    ends={
        Property(name="Kernel_PackageableElement35", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Package", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport22: BinaryAssociation = BinaryAssociation(
    name="packageImport22",
    ends={
        Property(name="PackageImport", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace23", type=Kernel_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember24: BinaryAssociation = BinaryAssociation(
    name="importedMember24",
    ends={
        Property(name="Kernel_PackageableElement", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Namespace25", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember26: BinaryAssociation = BinaryAssociation(
    name="ownedMember26",
    ends={
        Property(name="NamedElement", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement27: BinaryAssociation = BinaryAssociation(
    name="importedElement27",
    ends={
        Property(name="Kernel_PackageableElement28", type=fuml_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_ElementImport", type=Kernel_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace29: BinaryAssociation = BinaryAssociation(
    name="importingNamespace29",
    ends={
        Property(name="Namespace30", type=fuml_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage31: BinaryAssociation = BinaryAssociation(
    name="importedPackage31",
    ends={
        Property(name="Kernel_Package", type=fuml_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_PackageImport", type=Kernel_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace32: BinaryAssociation = BinaryAssociation(
    name="importingNamespace32",
    ends={
        Property(name="Namespace33", type=fuml_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
redefinitionContext44: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext44",
    ends={
        Property(name="Kernel_Classifier", type=fuml_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_RedefinableElement45", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType36: BinaryAssociation = BinaryAssociation(
    name="ownedType36",
    ends={
        Property(name="Type", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Kernel_Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage37: BinaryAssociation = BinaryAssociation(
    name="nestedPackage37",
    ends={
        Property(name="Package", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=Kernel_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage38: BinaryAssociation = BinaryAssociation(
    name="nestingPackage38",
    ends={
        Property(name="Package39", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
package40: BinaryAssociation = BinaryAssociation(
    name="package40",
    ends={
        Property(name="Package41", type=fuml_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier42: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier42",
    ends={
        Property(name="Classifier", type=fuml_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement43: BinaryAssociation = BinaryAssociation(
    name="redefinedElement43",
    ends={
        Property(name="Kernel_RedefinableElement", type=fuml_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_RedefinableElement", type=Kernel_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
owningAssociation60: BinaryAssociation = BinaryAssociation(
    name="owningAssociation60",
    ends={
        Property(name="Association", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
association61: BinaryAssociation = BinaryAssociation(
    name="association61",
    ends={
        Property(name="Association62", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
generalization46: BinaryAssociation = BinaryAssociation(
    name="generalization46",
    ends={
        Property(name="Generalization", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=Kernel_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature47: BinaryAssociation = BinaryAssociation(
    name="feature47",
    ends={
        Property(name="Feature", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=Kernel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember48: BinaryAssociation = BinaryAssociation(
    name="inheritedMember48",
    ends={
        Property(name="Kernel_NamedElement49", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute50: BinaryAssociation = BinaryAssociation(
    name="attribute50",
    ends={
        Property(name="Kernel_Property52", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier51", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general53: BinaryAssociation = BinaryAssociation(
    name="general53",
    ends={
        Property(name="Kernel_Classifier55", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier54", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general56: BinaryAssociation = BinaryAssociation(
    name="general56",
    ends={
        Property(name="Kernel_Classifier57", type=fuml_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific58: BinaryAssociation = BinaryAssociation(
    name="specific58",
    ends={
        Property(name="Classifier59", type=fuml_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
navigableOwnedEnd71: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd71",
    ends={
        Property(name="Kernel_Property73", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Association72", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd74: BinaryAssociation = BinaryAssociation(
    name="ownedEnd74",
    ends={
        Property(name="Property75", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype63: BinaryAssociation = BinaryAssociation(
    name="datatype63",
    ends={
        Property(name="DataType", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Kernel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
class_64: BinaryAssociation = BinaryAssociation(
    name="class_64",
    ends={
        Property(name="Class", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute65", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
opposite66: BinaryAssociation = BinaryAssociation(
    name="opposite66",
    ends={
        Property(name="Kernel_Property67", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Property", type=Kernel_Property, multiplicity=Multiplicity(0, 1))
    }
)
endType68: BinaryAssociation = BinaryAssociation(
    name="endType68",
    ends={
        Property(name="Kernel_Type69", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Association", type=Kernel_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd70: BinaryAssociation = BinaryAssociation(
    name="memberEnd70",
    ends={
        Property(name="Property", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=Kernel_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedAttribute76: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute76",
    ends={
        Property(name="Property77", type=fuml_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upperValue78: BinaryAssociation = BinaryAssociation(
    name="upperValue78",
    ends={
        Property(name="Kernel_ValueSpecification", type=fuml_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_MultiplicityElement", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue79: BinaryAssociation = BinaryAssociation(
    name="lowerValue79",
    ends={
        Property(name="Kernel_ValueSpecification81", type=fuml_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_MultiplicityElement80", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter82: BinaryAssociation = BinaryAssociation(
    name="ownedParameter82",
    ends={
        Property(name="Kernel_Parameter83", type=fuml_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_BehavioralFeature", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method84: BinaryAssociation = BinaryAssociation(
    name="method84",
    ends={
        Property(name="Behavior", type=fuml_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
classifier91: BinaryAssociation = BinaryAssociation(
    name="classifier91",
    ends={
        Property(name="Kernel_Classifier92", type=fuml_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_InstanceSpecification", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
class_85: BinaryAssociation = BinaryAssociation(
    name="class_85",
    ends={
        Property(name="Class86", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation87: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation87",
    ends={
        Property(name="Kernel_Operation", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Operation", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type88: BinaryAssociation = BinaryAssociation(
    name="type88",
    ends={
        Property(name="Kernel_Type90", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Operation89", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral100: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral100",
    ends={
        Property(name="EnumerationLiteral", type=fuml_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slot93: BinaryAssociation = BinaryAssociation(
    name="slot93",
    ends={
        Property(name="Slot", type=fuml_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature94: BinaryAssociation = BinaryAssociation(
    name="definingFeature94",
    ends={
        Property(name="Kernel_StructuralFeature", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Slot", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="Kernel_ValueSpecification97", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Slot96", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance98: BinaryAssociation = BinaryAssociation(
    name="owningInstance98",
    ends={
        Property(name="InstanceSpecification", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance99: BinaryAssociation = BinaryAssociation(
    name="instance99",
    ends={
        Property(name="Kernel_InstanceSpecification", type=fuml_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode116: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode116",
    ends={
        Property(name="StructuredActivityNode", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge117", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
guard118: BinaryAssociation = BinaryAssociation(
    name="guard118",
    ends={
        Property(name="Kernel_ValueSpecification119", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumeration101: BinaryAssociation = BinaryAssociation(
    name="enumeration101",
    ends={
        Property(name="Enumeration", type=fuml_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Kernel_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute102: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute102",
    ends={
        Property(name="Property103", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation104: BinaryAssociation = BinaryAssociation(
    name="ownedOperation104",
    ends={
        Property(name="Operation", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_105", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass106: BinaryAssociation = BinaryAssociation(
    name="superClass106",
    ends={
        Property(name="Kernel_Class", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception107: BinaryAssociation = BinaryAssociation(
    name="ownedReception107",
    ends={
        Property(name="Communications_Reception", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class108", type=Communications_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier109: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier109",
    ends={
        Property(name="Kernel_Classifier111", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class110", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity112: BinaryAssociation = BinaryAssociation(
    name="activity112",
    ends={
        Property(name="Activity", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source113: BinaryAssociation = BinaryAssociation(
    name="source113",
    ends={
        Property(name="ActivityNode", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="ActivityNode115", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
parameter137: BinaryAssociation = BinaryAssociation(
    name="parameter137",
    ends={
        Property(name="Kernel_Parameter138", type=fuml_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_ActivityParameterNode", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
node120: BinaryAssociation = BinaryAssociation(
    name="node120",
    ends={
        Property(name="ActivityNode121", type=fuml_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decider139: BinaryAssociation = BinaryAssociation(
    name="decider139",
    ends={
        Property(name="BasicActions_OutputPin", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
edge122: BinaryAssociation = BinaryAssociation(
    name="edge122",
    ends={
        Property(name="ActivityEdge", type=fuml_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity123", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode124: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode124",
    ends={
        Property(name="StructuredActivityNode125", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity126: BinaryAssociation = BinaryAssociation(
    name="activity126",
    ends={
        Property(name="Activity128", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node127", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing129: BinaryAssociation = BinaryAssociation(
    name="outgoing129",
    ends={
        Property(name="ActivityEdge130", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming131: BinaryAssociation = BinaryAssociation(
    name="incoming131",
    ends={
        Property(name="ActivityEdge132", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput133: BinaryAssociation = BinaryAssociation(
    name="decisionInput133",
    ends={
        Property(name="BasicBehaviors_Behavior134", type=fuml_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow135: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow135",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=fuml_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_DecisionNode136", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
successorClause165: BinaryAssociation = BinaryAssociation(
    name="successorClause165",
    ends={
        Property(name="Clause166", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
test140: BinaryAssociation = BinaryAssociation(
    name="test140",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode141", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput142: BinaryAssociation = BinaryAssociation(
    name="bodyOutput142",
    ends={
        Property(name="BasicActions_OutputPin144", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode143", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput145: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput145",
    ends={
        Property(name="BasicActions_InputPin", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode146", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart147: BinaryAssociation = BinaryAssociation(
    name="bodyPart147",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode149", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode148", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result150: BinaryAssociation = BinaryAssociation(
    name="result150",
    ends={
        Property(name="BasicActions_OutputPin152", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode151", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable153: BinaryAssociation = BinaryAssociation(
    name="loopVariable153",
    ends={
        Property(name="BasicActions_OutputPin155", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode154", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart156: BinaryAssociation = BinaryAssociation(
    name="setupPart156",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode158", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode157", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test159: BinaryAssociation = BinaryAssociation(
    name="test159",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode160", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body161: BinaryAssociation = BinaryAssociation(
    name="body161",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode163", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause162", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause164: BinaryAssociation = BinaryAssociation(
    name="predecessorClause164",
    ends={
        Property(name="Clause", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="successorClause", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider167: BinaryAssociation = BinaryAssociation(
    name="decider167",
    ends={
        Property(name="BasicActions_OutputPin169", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause168", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput170: BinaryAssociation = BinaryAssociation(
    name="bodyOutput170",
    ends={
        Property(name="BasicActions_OutputPin172", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause171", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause173: BinaryAssociation = BinaryAssociation(
    name="clause173",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=fuml_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result174: BinaryAssociation = BinaryAssociation(
    name="result174",
    ends={
        Property(name="BasicActions_OutputPin176", type=fuml_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_ConditionalNode175", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node177: BinaryAssociation = BinaryAssociation(
    name="node177",
    ends={
        Property(name="ActivityNode178", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge179: BinaryAssociation = BinaryAssociation(
    name="edge179",
    ends={
        Property(name="ActivityEdge181", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inStructuredNode180", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput182: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput182",
    ends={
        Property(name="BasicActions_OutputPin183", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput184: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput184",
    ends={
        Property(name="BasicActions_InputPin186", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_StructuredActivityNode185", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result200: BinaryAssociation = BinaryAssociation(
    name="result200",
    ends={
        Property(name="BasicActions_OutputPin202", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction201", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first203: BinaryAssociation = BinaryAssociation(
    name="first203",
    ends={
        Property(name="BasicActions_InputPin205", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction204", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
regionAsOutput187: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput187",
    ends={
        Property(name="ExpansionRegion", type=fuml_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="outputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput188: BinaryAssociation = BinaryAssociation(
    name="regionAsInput188",
    ends={
        Property(name="ExpansionRegion189", type=fuml_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="inputElement", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement190: BinaryAssociation = BinaryAssociation(
    name="inputElement190",
    ends={
        Property(name="ExpansionNode", type=fuml_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsInput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement191: BinaryAssociation = BinaryAssociation(
    name="outputElement191",
    ends={
        Property(name="ExpansionNode192", type=fuml_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="regionAsOutput", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature193: BinaryAssociation = BinaryAssociation(
    name="structuralFeature193",
    ends={
        Property(name="Kernel_StructuralFeature194", type=fuml_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_StructuralFeatureAction", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object195: BinaryAssociation = BinaryAssociation(
    name="object195",
    ends={
        Property(name="BasicActions_InputPin197", type=fuml_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_StructuralFeatureAction196", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second198: BinaryAssociation = BinaryAssociation(
    name="second198",
    ends={
        Property(name="BasicActions_InputPin199", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
removeAt225: BinaryAssociation = BinaryAssociation(
    name="removeAt225",
    ends={
        Property(name="BasicActions_InputPin226", type=fuml_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result227: BinaryAssociation = BinaryAssociation(
    name="result227",
    ends={
        Property(name="BasicActions_OutputPin228", type=fuml_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value206: BinaryAssociation = BinaryAssociation(
    name="value206",
    ends={
        Property(name="Kernel_ValueSpecification207", type=fuml_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result208: BinaryAssociation = BinaryAssociation(
    name="result208",
    ends={
        Property(name="BasicActions_OutputPin210", type=fuml_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ValueSpecificationAction209", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData211: BinaryAssociation = BinaryAssociation(
    name="endData211",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=fuml_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue212: BinaryAssociation = BinaryAssociation(
    name="inputValue212",
    ends={
        Property(name="BasicActions_InputPin214", type=fuml_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkAction213", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value215: BinaryAssociation = BinaryAssociation(
    name="value215",
    ends={
        Property(name="BasicActions_InputPin216", type=fuml_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end217: BinaryAssociation = BinaryAssociation(
    name="end217",
    ends={
        Property(name="Kernel_Property219", type=fuml_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndData218", type=Kernel_Property, multiplicity=Multiplicity(1, 1))
    }
)
value220: BinaryAssociation = BinaryAssociation(
    name="value220",
    ends={
        Property(name="BasicActions_InputPin221", type=fuml_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result222: BinaryAssociation = BinaryAssociation(
    name="result222",
    ends={
        Property(name="BasicActions_OutputPin224", type=fuml_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_WriteStructuralFeatureAction223", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result243: BinaryAssociation = BinaryAssociation(
    name="result243",
    ends={
        Property(name="BasicActions_OutputPin244", type=fuml_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier245: BinaryAssociation = BinaryAssociation(
    name="classifier245",
    ends={
        Property(name="Kernel_Classifier247", type=fuml_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_CreateObjectAction246", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result229: BinaryAssociation = BinaryAssociation(
    name="result229",
    ends={
        Property(name="BasicActions_OutputPin230", type=fuml_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result231: BinaryAssociation = BinaryAssociation(
    name="result231",
    ends={
        Property(name="BasicActions_OutputPin232", type=fuml_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt233: BinaryAssociation = BinaryAssociation(
    name="insertAt233",
    ends={
        Property(name="BasicActions_InputPin234", type=fuml_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt235: BinaryAssociation = BinaryAssociation(
    name="destroyAt235",
    ends={
        Property(name="BasicActions_InputPin236", type=fuml_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
association237: BinaryAssociation = BinaryAssociation(
    name="association237",
    ends={
        Property(name="Kernel_Association", type=fuml_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearAssociationAction", type=Kernel_Association, multiplicity=Multiplicity(1, 1))
    }
)
object238: BinaryAssociation = BinaryAssociation(
    name="object238",
    ends={
        Property(name="BasicActions_InputPin240", type=fuml_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearAssociationAction239", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result241: BinaryAssociation = BinaryAssociation(
    name="result241",
    ends={
        Property(name="BasicActions_OutputPin242", type=fuml_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier266: BinaryAssociation = BinaryAssociation(
    name="classifier266",
    ends={
        Property(name="Kernel_Classifier268", type=fuml_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadExtentAction267", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier269: BinaryAssociation = BinaryAssociation(
    name="classifier269",
    ends={
        Property(name="Kernel_Classifier270", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target248: BinaryAssociation = BinaryAssociation(
    name="target248",
    ends={
        Property(name="BasicActions_InputPin249", type=fuml_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt250: BinaryAssociation = BinaryAssociation(
    name="insertAt250",
    ends={
        Property(name="BasicActions_InputPin251", type=fuml_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object252: BinaryAssociation = BinaryAssociation(
    name="object252",
    ends={
        Property(name="BasicActions_InputPin253", type=fuml_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object254: BinaryAssociation = BinaryAssociation(
    name="object254",
    ends={
        Property(name="BasicActions_InputPin255", type=fuml_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer256: BinaryAssociation = BinaryAssociation(
    name="reducer256",
    ends={
        Property(name="BasicBehaviors_Behavior257", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result258: BinaryAssociation = BinaryAssociation(
    name="result258",
    ends={
        Property(name="BasicActions_OutputPin260", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction259", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection261: BinaryAssociation = BinaryAssociation(
    name="collection261",
    ends={
        Property(name="BasicActions_InputPin263", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction262", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result264: BinaryAssociation = BinaryAssociation(
    name="result264",
    ends={
        Property(name="BasicActions_OutputPin265", type=fuml_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context291: BinaryAssociation = BinaryAssociation(
    name="context291",
    ends={
        Property(name="fuml_BasicActions_Action292", type=Kernel_Classifier, multiplicity=Multiplicity(0, 1)),
        Property(name="Kernel_Classifier293", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1))
    }
)
input294: BinaryAssociation = BinaryAssociation(
    name="input294",
    ends={
        Property(name="BasicActions_InputPin296", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_Action295", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result271: BinaryAssociation = BinaryAssociation(
    name="result271",
    ends={
        Property(name="BasicActions_OutputPin273", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction272", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object274: BinaryAssociation = BinaryAssociation(
    name="object274",
    ends={
        Property(name="BasicActions_InputPin276", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction275", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier277: BinaryAssociation = BinaryAssociation(
    name="oldClassifier277",
    ends={
        Property(name="Kernel_Classifier278", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object279: BinaryAssociation = BinaryAssociation(
    name="object279",
    ends={
        Property(name="BasicActions_InputPin281", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction280", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier282: BinaryAssociation = BinaryAssociation(
    name="newClassifier282",
    ends={
        Property(name="Kernel_Classifier284", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction283", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
result285: BinaryAssociation = BinaryAssociation(
    name="result285",
    ends={
        Property(name="BasicActions_OutputPin286", type=fuml_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger287: BinaryAssociation = BinaryAssociation(
    name="trigger287",
    ends={
        Property(name="Communications_Trigger", type=fuml_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_AcceptEventAction288", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output289: BinaryAssociation = BinaryAssociation(
    name="output289",
    ends={
        Property(name="BasicActions_OutputPin290", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
target310: BinaryAssociation = BinaryAssociation(
    name="target310",
    ends={
        Property(name="BasicActions_InputPin312", type=fuml_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallOperationAction311", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result297: BinaryAssociation = BinaryAssociation(
    name="result297",
    ends={
        Property(name="BasicActions_OutputPin298", type=fuml_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument299: BinaryAssociation = BinaryAssociation(
    name="argument299",
    ends={
        Property(name="BasicActions_InputPin300", type=fuml_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target301: BinaryAssociation = BinaryAssociation(
    name="target301",
    ends={
        Property(name="BasicActions_InputPin302", type=fuml_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal303: BinaryAssociation = BinaryAssociation(
    name="signal303",
    ends={
        Property(name="Communications_Signal305", type=fuml_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_SendSignalAction304", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior306: BinaryAssociation = BinaryAssociation(
    name="behavior306",
    ends={
        Property(name="BasicBehaviors_Behavior307", type=fuml_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation308: BinaryAssociation = BinaryAssociation(
    name="operation308",
    ends={
        Property(name="Kernel_Operation309", type=fuml_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallOperationAction", type=Kernel_Operation, multiplicity=Multiplicity(1, 1))
    }
)
referent318: BinaryAssociation = BinaryAssociation(
    name="referent318",
    ends={
        Property(name="Kernel_Object", type=fuml_Kernel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Reference", type=Kernel_Object, multiplicity=Multiplicity(1, 1))
    }
)
types319: BinaryAssociation = BinaryAssociation(
    name="types319",
    ends={
        Property(name="Kernel_Class320", type=fuml_Kernel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Object", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
locus321: BinaryAssociation = BinaryAssociation(
    name="locus321",
    ends={
        Property(name="Locus", type=fuml_Kernel_ExtensionalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionalValues", type=LociL1_Locus, multiplicity=Multiplicity(0, 1))
    }
)
featureValues322: BinaryAssociation = BinaryAssociation(
    name="featureValues322",
    ends={
        Property(name="Kernel_FeatureValue", type=fuml_Kernel_CompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_CompoundValue", type=Kernel_FeatureValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type323: BinaryAssociation = BinaryAssociation(
    name="type323",
    ends={
        Property(name="Kernel_Association324", type=fuml_Kernel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Link", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
feature313: BinaryAssociation = BinaryAssociation(
    name="feature313",
    ends={
        Property(name="Kernel_StructuralFeature314", type=fuml_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_FeatureValue", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
values315: BinaryAssociation = BinaryAssociation(
    name="values315",
    ends={
        Property(name="Kernel_Value", type=fuml_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_FeatureValue316", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type317: BinaryAssociation = BinaryAssociation(
    name="type317",
    ends={
        Property(name="Kernel_PrimitiveType", type=fuml_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
extensionalValues329: BinaryAssociation = BinaryAssociation(
    name="extensionalValues329",
    ends={
        Property(name="ExtensionalValue", type=fuml_LociL1_Locus, multiplicity=Multiplicity(1, 1)),
        Property(name="locus", type=Kernel_ExtensionalValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter330: BinaryAssociation = BinaryAssociation(
    name="parameter330",
    ends={
        Property(name="Kernel_Parameter331", type=fuml_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_ParameterValue", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
values332: BinaryAssociation = BinaryAssociation(
    name="values332",
    ends={
        Property(name="Kernel_Value334", type=fuml_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_ParameterValue333", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal325: BinaryAssociation = BinaryAssociation(
    name="literal325",
    ends={
        Property(name="Kernel_EnumerationLiteral", type=fuml_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_EnumerationValue", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type326: BinaryAssociation = BinaryAssociation(
    name="type326",
    ends={
        Property(name="Kernel_Enumeration", type=fuml_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_EnumerationValue327", type=Kernel_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
type328: BinaryAssociation = BinaryAssociation(
    name="type328",
    ends={
        Property(name="Kernel_DataType", type=fuml_Kernel_DataValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_DataValue", type=Kernel_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fuml_BasicBehaviors_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=fuml_BasicBehaviors_BehavioredClassifier)
gen_fuml_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=fuml_BasicBehaviors_OpaqueBehavior)
gen_fuml_BasicBehaviors_Behavior_Class = Generalization(general=Class_, specific=fuml_BasicBehaviors_Behavior)
gen_fuml_Kernel_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=fuml_Kernel_ValueSpecification)
gen_fuml_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_TypedElement)
gen_fuml_Kernel_NamedElement_Element = Generalization(general=Element, specific=fuml_Kernel_NamedElement)
gen_fuml_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=fuml_BasicBehaviors_FunctionBehavior)
gen_fuml_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=fuml_Communications_Trigger)
gen_fuml_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=fuml_Communications_Event)
gen_fuml_Communications_Signal_Classifier = Generalization(general=Classifier, specific=fuml_Communications_Signal)
gen_fuml_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=fuml_Communications_SignalEvent)
gen_fuml_Communications_MessageEvent_Event = Generalization(general=Event, specific=fuml_Communications_MessageEvent)
gen_fuml_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fuml_Communications_Reception)
gen_fuml_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_Namespace)
gen_fuml_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fuml_Kernel_Package)
gen_fuml_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=fuml_Kernel_Package)
gen_fuml_Kernel_ElementImport_Element = Generalization(general=Element, specific=fuml_Kernel_ElementImport)
gen_fuml_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_PackageableElement)
gen_fuml_Kernel_PackageImport_Element = Generalization(general=Element, specific=fuml_Kernel_PackageImport)
gen_fuml_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fuml_Kernel_Classifier)
gen_fuml_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=fuml_Kernel_Classifier)
gen_fuml_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=fuml_Kernel_Type)
gen_fuml_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_Kernel_Feature)
gen_fuml_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_RedefinableElement)
gen_fuml_Kernel_Generalization_Element = Generalization(general=Element, specific=fuml_Kernel_Generalization)
gen_fuml_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=fuml_Kernel_Property)
gen_fuml_Kernel_Association_Classifier = Generalization(general=Classifier, specific=fuml_Kernel_Association)
gen_fuml_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=fuml_Kernel_DataType)
gen_fuml_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=fuml_Kernel_MultiplicityElement)
gen_fuml_Kernel_BehavioralFeature_Feature = Generalization(general=Feature, specific=fuml_Kernel_BehavioralFeature)
gen_fuml_Kernel_Parameter_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_Kernel_Parameter)
gen_fuml_Kernel_Parameter_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fuml_Kernel_Parameter)
gen_fuml_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fuml_Kernel_Operation)
gen_fuml_Kernel_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_InstanceSpecification)
gen_fuml_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=fuml_Kernel_Enumeration)
gen_fuml_Kernel_Slot_Element = Generalization(general=Element, specific=fuml_Kernel_Slot)
gen_fuml_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=fuml_Kernel_InstanceValue)
gen_fuml_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralBoolean)
gen_fuml_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=fuml_Kernel_LiteralSpecification)
gen_fuml_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralInteger)
gen_fuml_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralNull)
gen_fuml_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralString)
gen_fuml_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralUnlimitedNatural)
gen_fuml_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=fuml_Kernel_PrimitiveType)
gen_fuml_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=fuml_Kernel_EnumerationLiteral)
gen_fuml_Kernel_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=fuml_Kernel_Class)
gen_fuml_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=fuml_IntermediateActivities_ObjectFlow)
gen_fuml_IntermediateActivities_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_IntermediateActivities_ActivityEdge)
gen_fuml_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_CompleteStructuredActivities_LoopNode)
gen_fuml_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=fuml_IntermediateActivities_Activity)
gen_fuml_IntermediateActivities_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_IntermediateActivities_ActivityNode)
gen_fuml_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode = Generalization(general=IntermediateActivities_ActivityNode, specific=fuml_IntermediateActivities_ObjectNode)
gen_fuml_IntermediateActivities_ObjectNode_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fuml_IntermediateActivities_ObjectNode)
gen_fuml_IntermediateActivities_MergeNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_MergeNode)
gen_fuml_IntermediateActivities_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=fuml_IntermediateActivities_ControlNode)
gen_fuml_IntermediateActivities_JoinNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_JoinNode)
gen_fuml_IntermediateActivities_InitialNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_InitialNode)
gen_fuml_IntermediateActivities_FinalNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_FinalNode)
gen_fuml_IntermediateActivities_ForkNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_ForkNode)
gen_fuml_IntermediateActivities_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=fuml_IntermediateActivities_ControlFlow)
gen_fuml_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=fuml_IntermediateActivities_DecisionNode)
gen_fuml_IntermediateActivities_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=fuml_IntermediateActivities_ActivityFinalNode)
gen_fuml_IntermediateActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=fuml_IntermediateActivities_ActivityParameterNode)
gen_fuml_CompleteStructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=fuml_CompleteStructuredActivities_ExecutableNode)
gen_fuml_CompleteStructuredActivities_Clause_Element = Generalization(general=Element, specific=fuml_CompleteStructuredActivities_Clause)
gen_fuml_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_CompleteStructuredActivities_ConditionalNode)
gen_fuml_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=fuml_CompleteStructuredActivities_StructuredActivityNode)
gen_fuml_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=fuml_ExtraStructuredActivities_ExpansionNode)
gen_fuml_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_ExtraStructuredActivities_ExpansionRegion)
gen_fuml_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_StructuralFeatureAction)
gen_fuml_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_TestIdentityAction)
gen_fuml_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=fuml_IntermediateActions_ReadLinkAction)
gen_fuml_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ValueSpecificationAction)
gen_fuml_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ReadSelfAction)
gen_fuml_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=fuml_IntermediateActions_WriteLinkAction)
gen_fuml_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_LinkAction)
gen_fuml_IntermediateActions_LinkEndData_Element = Generalization(general=Element, specific=fuml_IntermediateActions_LinkEndData)
gen_fuml_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_WriteStructuralFeatureAction)
gen_fuml_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fuml_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_fuml_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fuml_IntermediateActions_DestroyLinkAction)
gen_fuml_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_DestroyObjectAction)
gen_fuml_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_ReadStructuralFeatureAction)
gen_fuml_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=fuml_IntermediateActions_LinkEndCreationData)
gen_fuml_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=fuml_IntermediateActions_LinkEndDestructionData)
gen_fuml_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ClearAssociationAction)
gen_fuml_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_ClearStructuralFeatureAction)
gen_fuml_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fuml_IntermediateActions_CreateLinkAction)
gen_fuml_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_CreateObjectAction)
gen_fuml_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReadIsClassifiedObjectAction)
gen_fuml_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fuml_IntermediateActions_AddStructuralFeatureValueAction)
gen_fuml_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_StartClassifierBehaviorAction)
gen_fuml_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=fuml_CompleteActions_StartObjectBehaviorAction)
gen_fuml_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReduceAction)
gen_fuml_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReadExtentAction)
gen_fuml_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=fuml_BasicActions_InputPin)
gen_fuml_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=fuml_BasicActions_Pin)
gen_fuml_BasicActions_Pin_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_BasicActions_Pin)
gen_fuml_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=fuml_BasicActions_CallAction)
gen_fuml_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReclassifyObjectAction)
gen_fuml_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_AcceptEventAction)
gen_fuml_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=fuml_BasicActions_Action)
gen_fuml_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=fuml_BasicActions_OutputPin)
gen_fuml_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=fuml_BasicActions_InvocationAction)
gen_fuml_Kernel_StructuredValue_Value = Generalization(general=Value, specific=fuml_Kernel_StructuredValue)
gen_fuml_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=fuml_BasicActions_SendSignalAction)
gen_fuml_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=fuml_BasicActions_CallBehaviorAction)
gen_fuml_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=fuml_BasicActions_CallOperationAction)
gen_fuml_Kernel_Object_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fuml_Kernel_Object)
gen_fuml_Kernel_ExtensionalValue_CompoundValue = Generalization(general=CompoundValue, specific=fuml_Kernel_ExtensionalValue)
gen_fuml_Kernel_CompoundValue_StructuredValue = Generalization(general=StructuredValue, specific=fuml_Kernel_CompoundValue)
gen_fuml_Kernel_Link_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fuml_Kernel_Link)
gen_fuml_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_IntegerValue)
gen_fuml_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=fuml_Kernel_EnumerationValue)
gen_fuml_Kernel_UnlimitedNaturalValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_UnlimitedNaturalValue)
gen_fuml_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=fuml_Kernel_PrimitiveValue)
gen_fuml_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_StringValue)
gen_fuml_Kernel_Reference_StructuredValue = Generalization(general=StructuredValue, specific=fuml_Kernel_Reference)
gen_fuml_Kernel_DataValue_CompoundValue = Generalization(general=CompoundValue, specific=fuml_Kernel_DataValue)
gen_fuml_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_BooleanValue)
gen_fuml_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=fuml_Kernel_Value)

# Domain Model
domain_model = DomainModel(
    name="fuml",
    types={BasicBehaviors_BehavioredClassifier, fuml_BasicBehaviors_BehavioredClassifier, Classifier, BasicBehaviors_Behavior, fuml_BasicBehaviors_OpaqueBehavior, Behavior, fuml_BasicBehaviors_Behavior, Class_, Kernel_BehavioralFeature, Kernel_Parameter, fuml_Kernel_ValueSpecification, TypedElement, fuml_Kernel_TypedElement, Kernel_Type, fuml_Kernel_NamedElement, Element, fuml_BasicBehaviors_FunctionBehavior, OpaqueBehavior, fuml_Communications_Trigger, NamedElement, Communications_Event, fuml_Communications_Event, PackageableElement, fuml_Communications_Signal, Kernel_Property, fuml_Communications_SignalEvent, MessageEvent, Communications_Signal, fuml_Communications_MessageEvent, Event, fuml_Communications_Reception, BehavioralFeature, fuml_Kernel_Namespace, Kernel_NamedElement, Kernel_ElementImport, Kernel_Namespace, fuml_Kernel_Element, Kernel_Element, Kernel_Comment, fuml_Kernel_Comment, fuml_Kernel_Package, Kernel_PackageImport, Kernel_PackageableElement, fuml_Kernel_ElementImport, fuml_Kernel_PackageableElement, fuml_Kernel_PackageImport, Kernel_Package, fuml_Kernel_Classifier, fuml_Kernel_Type, fuml_Kernel_StructuralFeature, Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement, fuml_Kernel_Feature, RedefinableElement, Kernel_Classifier, fuml_Kernel_RedefinableElement, Kernel_RedefinableElement, Kernel_Association, Kernel_Generalization, fuml_Kernel_Generalization, fuml_Kernel_Property, StructuralFeature, Kernel_DataType, Kernel_Class, fuml_Kernel_Association, fuml_Kernel_DataType, fuml_Kernel_MultiplicityElement, Kernel_ValueSpecification, fuml_Kernel_BehavioralFeature, Feature, fuml_Kernel_Parameter, fuml_Kernel_Operation, Kernel_Operation, fuml_Kernel_InstanceSpecification, fuml_Kernel_Enumeration, Kernel_EnumerationLiteral, Kernel_Slot, fuml_Kernel_Slot, Kernel_StructuralFeature, Kernel_InstanceSpecification, fuml_Kernel_InstanceValue, ValueSpecification, fuml_Kernel_LiteralBoolean, LiteralSpecification, fuml_Kernel_LiteralSpecification, fuml_Kernel_LiteralInteger, fuml_Kernel_LiteralNull, fuml_Kernel_LiteralString, fuml_Kernel_LiteralUnlimitedNatural, fuml_Kernel_PrimitiveType, DataType, fuml_IntermediateActivities_Activity, fuml_Kernel_EnumerationLiteral, InstanceSpecification, Kernel_Enumeration, fuml_Kernel_Class, BehavioredClassifier, Communications_Reception, fuml_IntermediateActivities_ObjectFlow, ActivityEdge, fuml_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, fuml_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, IntermediateActivities_ActivityEdge, fuml_IntermediateActivities_ActivityNode, fuml_IntermediateActivities_ObjectNode, fuml_IntermediateActivities_MergeNode, ControlNode, fuml_IntermediateActivities_ControlNode, ActivityNode, fuml_IntermediateActivities_JoinNode, fuml_IntermediateActivities_InitialNode, fuml_IntermediateActivities_FinalNode, fuml_IntermediateActivities_ForkNode, fuml_IntermediateActivities_ControlFlow, fuml_IntermediateActivities_DecisionNode, IntermediateActivities_ObjectFlow, fuml_IntermediateActivities_ActivityFinalNode, FinalNode, fuml_IntermediateActivities_ActivityParameterNode, ObjectNode, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, fuml_CompleteStructuredActivities_ExecutableNode, fuml_CompleteStructuredActivities_Clause, CompleteStructuredActivities_Clause, fuml_CompleteStructuredActivities_ConditionalNode, fuml_CompleteStructuredActivities_StructuredActivityNode, Action, fuml_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, fuml_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, fuml_IntermediateActions_StructuralFeatureAction, fuml_IntermediateActions_TestIdentityAction, fuml_IntermediateActions_ReadLinkAction, fuml_IntermediateActions_ValueSpecificationAction, fuml_IntermediateActions_ReadSelfAction, fuml_IntermediateActions_WriteLinkAction, LinkAction, fuml_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, fuml_IntermediateActions_LinkEndData, fuml_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, fuml_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, fuml_IntermediateActions_DestroyLinkAction, fuml_IntermediateActions_DestroyObjectAction, fuml_IntermediateActions_ReadStructuralFeatureAction, fuml_IntermediateActions_LinkEndCreationData, LinkEndData, fuml_IntermediateActions_LinkEndDestructionData, fuml_IntermediateActions_ClearAssociationAction, fuml_IntermediateActions_ClearStructuralFeatureAction, fuml_IntermediateActions_CreateLinkAction, WriteLinkAction, fuml_IntermediateActions_CreateObjectAction, fuml_CompleteActions_ReadIsClassifiedObjectAction, fuml_IntermediateActions_AddStructuralFeatureValueAction, fuml_CompleteActions_StartClassifierBehaviorAction, fuml_CompleteActions_StartObjectBehaviorAction, CallAction, fuml_CompleteActions_ReduceAction, fuml_CompleteActions_ReadExtentAction, fuml_BasicActions_InputPin, Pin, fuml_BasicActions_Pin, IntermediateActivities_ObjectNode, fuml_BasicActions_CallAction, InvocationAction, fuml_CompleteActions_ReclassifyObjectAction, fuml_CompleteActions_AcceptEventAction, Communications_Trigger, fuml_BasicActions_Action, ExecutableNode, fuml_BasicActions_OutputPin, fuml_BasicActions_InvocationAction, fuml_Kernel_StructuredValue, Value, fuml_Kernel_FeatureValue, fuml_BasicActions_SendSignalAction, fuml_BasicActions_CallBehaviorAction, fuml_BasicActions_CallOperationAction, Kernel_Object, fuml_Kernel_Object, ExtensionalValue, fuml_Kernel_ExtensionalValue, CompoundValue, LociL1_Locus, fuml_Kernel_CompoundValue, Kernel_FeatureValue, fuml_Kernel_Link, fuml_Kernel_IntegerValue, fuml_Kernel_EnumerationValue, Kernel_Value, fuml_Kernel_UnlimitedNaturalValue, PrimitiveValue, fuml_Kernel_PrimitiveValue, Kernel_PrimitiveType, fuml_Kernel_StringValue, fuml_Kernel_Reference, StructuredValue, fuml_LociL1_SemanticVisitor, fuml_LociL1_Locus, Kernel_ExtensionalValue, fuml_BasicBehaviors_ParameterValue, fuml_Kernel_DataValue, fuml_Kernel_BooleanValue, fuml_Kernel_Value, SemanticVisitor, CallConcurrencyKind, VisibilityKind, AggregationKind, ParameterDirectionKind, ExpansionKind},
    associations={context2, specification0, ownedParameter1, type13, ownedBehavior4, classifierBehavior5, event8, ownedAttribute9, signal10, signal11, member20, elementImport21, namespace14, ownedElement15, owner16, ownedComment18, annotatedElement19, packagedElement34, packageImport22, importedMember24, ownedMember26, importedElement27, importingNamespace29, importedPackage31, importingNamespace32, redefinitionContext44, ownedType36, nestedPackage37, nestingPackage38, package40, featuringClassifier42, redefinedElement43, owningAssociation60, association61, generalization46, feature47, inheritedMember48, attribute50, general53, general56, specific58, navigableOwnedEnd71, ownedEnd74, datatype63, class_64, opposite66, endType68, memberEnd70, ownedAttribute76, upperValue78, lowerValue79, ownedParameter82, method84, classifier91, class_85, redefinedOperation87, type88, ownedLiteral100, slot93, definingFeature94, value95, owningInstance98, instance99, inStructuredNode116, guard118, enumeration101, ownedAttribute102, ownedOperation104, superClass106, ownedReception107, nestedClassifier109, activity112, source113, target114, parameter137, node120, decider139, edge122, inStructuredNode124, activity126, outgoing129, incoming131, decisionInput133, decisionInputFlow135, successorClause165, test140, bodyOutput142, loopVariableInput145, bodyPart147, result150, loopVariable153, setupPart156, test159, body161, predecessorClause164, decider167, bodyOutput170, clause173, result174, node177, edge179, structuredNodeOutput182, structuredNodeInput184, result200, first203, regionAsOutput187, regionAsInput188, inputElement190, outputElement191, structuralFeature193, object195, second198, removeAt225, result227, value206, result208, endData211, inputValue212, value215, end217, value220, result222, result243, classifier245, result229, result231, insertAt233, destroyAt235, association237, object238, result241, classifier266, classifier269, target248, insertAt250, object252, object254, reducer256, result258, collection261, result264, context291, input294, result271, object274, oldClassifier277, object279, newClassifier282, result285, trigger287, output289, target310, result297, argument299, target301, signal303, behavior306, operation308, referent318, types319, locus321, featureValues322, type323, feature313, values315, type317, extensionalValues329, parameter330, values332, literal325, type326, type328},
    generalizations={gen_fuml_BasicBehaviors_BehavioredClassifier_Classifier, gen_fuml_BasicBehaviors_OpaqueBehavior_Behavior, gen_fuml_BasicBehaviors_Behavior_Class, gen_fuml_Kernel_ValueSpecification_TypedElement, gen_fuml_Kernel_TypedElement_NamedElement, gen_fuml_Kernel_NamedElement_Element, gen_fuml_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_fuml_Communications_Trigger_NamedElement, gen_fuml_Communications_Event_PackageableElement, gen_fuml_Communications_Signal_Classifier, gen_fuml_Communications_SignalEvent_MessageEvent, gen_fuml_Communications_MessageEvent_Event, gen_fuml_Communications_Reception_BehavioralFeature, gen_fuml_Kernel_Namespace_NamedElement, gen_fuml_Kernel_Package_Kernel_Namespace, gen_fuml_Kernel_Package_Kernel_PackageableElement, gen_fuml_Kernel_ElementImport_Element, gen_fuml_Kernel_PackageableElement_NamedElement, gen_fuml_Kernel_PackageImport_Element, gen_fuml_Kernel_Classifier_Kernel_Namespace, gen_fuml_Kernel_Classifier_Kernel_Type, gen_fuml_Kernel_Type_PackageableElement, gen_fuml_Kernel_StructuralFeature_Kernel_Feature, gen_fuml_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_fuml_Kernel_StructuralFeature_Kernel_TypedElement, gen_fuml_Kernel_Feature_RedefinableElement, gen_fuml_Kernel_RedefinableElement_NamedElement, gen_fuml_Kernel_Generalization_Element, gen_fuml_Kernel_Property_StructuralFeature, gen_fuml_Kernel_Association_Classifier, gen_fuml_Kernel_DataType_Classifier, gen_fuml_Kernel_MultiplicityElement_Element, gen_fuml_Kernel_BehavioralFeature_Feature, gen_fuml_Kernel_Parameter_Kernel_MultiplicityElement, gen_fuml_Kernel_Parameter_Kernel_TypedElement, gen_fuml_Kernel_Operation_BehavioralFeature, gen_fuml_Kernel_InstanceSpecification_NamedElement, gen_fuml_Kernel_Enumeration_DataType, gen_fuml_Kernel_Slot_Element, gen_fuml_Kernel_InstanceValue_ValueSpecification, gen_fuml_Kernel_LiteralBoolean_LiteralSpecification, gen_fuml_Kernel_LiteralSpecification_ValueSpecification, gen_fuml_Kernel_LiteralInteger_LiteralSpecification, gen_fuml_Kernel_LiteralNull_LiteralSpecification, gen_fuml_Kernel_LiteralString_LiteralSpecification, gen_fuml_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_fuml_Kernel_PrimitiveType_DataType, gen_fuml_Kernel_EnumerationLiteral_InstanceSpecification, gen_fuml_Kernel_Class_BehavioredClassifier, gen_fuml_IntermediateActivities_ObjectFlow_ActivityEdge, gen_fuml_IntermediateActivities_ActivityEdge_RedefinableElement, gen_fuml_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_fuml_IntermediateActivities_Activity_Behavior, gen_fuml_IntermediateActivities_ActivityNode_RedefinableElement, gen_fuml_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_fuml_IntermediateActivities_ObjectNode_Kernel_TypedElement, gen_fuml_IntermediateActivities_MergeNode_ControlNode, gen_fuml_IntermediateActivities_ControlNode_ActivityNode, gen_fuml_IntermediateActivities_JoinNode_ControlNode, gen_fuml_IntermediateActivities_InitialNode_ControlNode, gen_fuml_IntermediateActivities_FinalNode_ControlNode, gen_fuml_IntermediateActivities_ForkNode_ControlNode, gen_fuml_IntermediateActivities_ControlFlow_ActivityEdge, gen_fuml_IntermediateActivities_DecisionNode_ControlNode, gen_fuml_IntermediateActivities_ActivityFinalNode_FinalNode, gen_fuml_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_fuml_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_fuml_CompleteStructuredActivities_Clause_Element, gen_fuml_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_fuml_CompleteStructuredActivities_StructuredActivityNode_Action, gen_fuml_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_fuml_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_fuml_IntermediateActions_StructuralFeatureAction_Action, gen_fuml_IntermediateActions_TestIdentityAction_Action, gen_fuml_IntermediateActions_ReadLinkAction_LinkAction, gen_fuml_IntermediateActions_ValueSpecificationAction_Action, gen_fuml_IntermediateActions_ReadSelfAction_Action, gen_fuml_IntermediateActions_WriteLinkAction_LinkAction, gen_fuml_IntermediateActions_LinkAction_Action, gen_fuml_IntermediateActions_LinkEndData_Element, gen_fuml_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fuml_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_fuml_IntermediateActions_DestroyObjectAction_Action, gen_fuml_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_LinkEndCreationData_LinkEndData, gen_fuml_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_fuml_IntermediateActions_ClearAssociationAction_Action, gen_fuml_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_fuml_IntermediateActions_CreateObjectAction_Action, gen_fuml_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_fuml_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fuml_CompleteActions_StartClassifierBehaviorAction_Action, gen_fuml_CompleteActions_StartObjectBehaviorAction_CallAction, gen_fuml_CompleteActions_ReduceAction_Action, gen_fuml_CompleteActions_ReadExtentAction_Action, gen_fuml_BasicActions_InputPin_Pin, gen_fuml_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_fuml_BasicActions_Pin_Kernel_MultiplicityElement, gen_fuml_BasicActions_CallAction_InvocationAction, gen_fuml_CompleteActions_ReclassifyObjectAction_Action, gen_fuml_CompleteActions_AcceptEventAction_Action, gen_fuml_BasicActions_Action_ExecutableNode, gen_fuml_BasicActions_OutputPin_Pin, gen_fuml_BasicActions_InvocationAction_Action, gen_fuml_Kernel_StructuredValue_Value, gen_fuml_BasicActions_SendSignalAction_InvocationAction, gen_fuml_BasicActions_CallBehaviorAction_CallAction, gen_fuml_BasicActions_CallOperationAction_CallAction, gen_fuml_Kernel_Object_ExtensionalValue, gen_fuml_Kernel_ExtensionalValue_CompoundValue, gen_fuml_Kernel_CompoundValue_StructuredValue, gen_fuml_Kernel_Link_ExtensionalValue, gen_fuml_Kernel_IntegerValue_PrimitiveValue, gen_fuml_Kernel_EnumerationValue_Value, gen_fuml_Kernel_UnlimitedNaturalValue_PrimitiveValue, gen_fuml_Kernel_PrimitiveValue_Value, gen_fuml_Kernel_StringValue_PrimitiveValue, gen_fuml_Kernel_Reference_StructuredValue, gen_fuml_Kernel_DataValue_CompoundValue, gen_fuml_Kernel_BooleanValue_PrimitiveValue, gen_fuml_Kernel_Value_SemanticVisitor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)