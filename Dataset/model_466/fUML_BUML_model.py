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
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
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
Kernel_Parameter = Class(name="Kernel::Parameter")
fuml_BasicBehaviors_OpaqueBehavior = Class(name="fuml::BasicBehaviors::OpaqueBehavior")
Behavior = Class(name="Behavior")
fuml_BasicBehaviors_Behavior = Class(name="fuml::BasicBehaviors::Behavior", is_abstract=True)
Class_ = Class(name="Class")
Kernel_BehavioralFeature = Class(name="Kernel::BehavioralFeature")
fuml_Communications_MessageEvent = Class(name="fuml::Communications::MessageEvent", is_abstract=True)
Event = Class(name="Event")
fuml_Communications_Reception = Class(name="fuml::Communications::Reception")
BehavioralFeature = Class(name="BehavioralFeature")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors::BehavioredClassifier")
fuml_BasicBehaviors_BehavioredClassifier = Class(name="fuml::BasicBehaviors::BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors::Behavior")
fuml_BasicBehaviors_FunctionBehavior = Class(name="fuml::BasicBehaviors::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
fuml_Communications_Trigger = Class(name="fuml::Communications::Trigger")
NamedElement = Class(name="NamedElement")
Communications_Event = Class(name="Communications::Event")
fuml_Communications_Event = Class(name="fuml::Communications::Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
fuml_Communications_Signal = Class(name="fuml::Communications::Signal")
Kernel_Property = Class(name="Kernel::Property")
fuml_Communications_SignalEvent = Class(name="fuml::Communications::SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications::Signal")
Kernel_Comment = Class(name="Kernel::Comment")
fuml_Kernel_Comment = Class(name="fuml::Kernel::Comment")
fuml_Kernel_ValueSpecification = Class(name="fuml::Kernel::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
fuml_Kernel_TypedElement = Class(name="fuml::Kernel::TypedElement")
Kernel_Type = Class(name="Kernel::Type")
fuml_Kernel_NamedElement = Class(name="fuml::Kernel::NamedElement", is_abstract=True)
Element = Class(name="Element")
Kernel_Namespace = Class(name="Kernel::Namespace")
fuml_Kernel_Element = Class(name="fuml::Kernel::Element", is_abstract=True)
Kernel_Element = Class(name="Kernel::Element")
fuml_Kernel_ElementImport = Class(name="fuml::Kernel::ElementImport")
fuml_Kernel_Namespace = Class(name="fuml::Kernel::Namespace", is_abstract=True)
Kernel_NamedElement = Class(name="Kernel::NamedElement")
Kernel_ElementImport = Class(name="Kernel::ElementImport")
Kernel_PackageImport = Class(name="Kernel::PackageImport")
Kernel_PackageableElement = Class(name="Kernel::PackageableElement")
fuml_Kernel_Feature = Class(name="fuml::Kernel::Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Kernel_Classifier = Class(name="Kernel::Classifier")
fuml_Kernel_PackageableElement = Class(name="fuml::Kernel::PackageableElement", is_abstract=True)
fuml_Kernel_PackageImport = Class(name="fuml::Kernel::PackageImport")
Kernel_Package = Class(name="Kernel::Package")
fuml_Kernel_Package = Class(name="fuml::Kernel::Package")
fuml_Kernel_Type = Class(name="fuml::Kernel::Type", is_abstract=True)
fuml_Kernel_StructuralFeature = Class(name="fuml::Kernel::StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel::Feature")
Kernel_MultiplicityElement = Class(name="Kernel::MultiplicityElement")
Kernel_TypedElement = Class(name="Kernel::TypedElement")
fuml_Kernel_RedefinableElement = Class(name="fuml::Kernel::RedefinableElement", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel::RedefinableElement")
fuml_Kernel_Classifier = Class(name="fuml::Kernel::Classifier", is_abstract=True)
Kernel_Generalization = Class(name="Kernel::Generalization")
Kernel_Class = Class(name="Kernel::Class")
fuml_Kernel_Generalization = Class(name="fuml::Kernel::Generalization")
fuml_Kernel_Property = Class(name="fuml::Kernel::Property")
StructuralFeature = Class(name="StructuralFeature")
Kernel_Association = Class(name="Kernel::Association")
Kernel_DataType = Class(name="Kernel::DataType")
Kernel_ValueSpecification = Class(name="Kernel::ValueSpecification")
fuml_Kernel_Association = Class(name="fuml::Kernel::Association")
fuml_Kernel_DataType = Class(name="fuml::Kernel::DataType")
fuml_Kernel_MultiplicityElement = Class(name="fuml::Kernel::MultiplicityElement")
Kernel_Operation = Class(name="Kernel::Operation")
fuml_Kernel_BehavioralFeature = Class(name="fuml::Kernel::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
fuml_Kernel_Parameter = Class(name="fuml::Kernel::Parameter")
fuml_Kernel_Operation = Class(name="fuml::Kernel::Operation")
fuml_Kernel_LiteralInteger = Class(name="fuml::Kernel::LiteralInteger")
fuml_Kernel_LiteralNull = Class(name="fuml::Kernel::LiteralNull")
fuml_Kernel_InstanceSpecification = Class(name="fuml::Kernel::InstanceSpecification")
Kernel_Slot = Class(name="Kernel::Slot")
fuml_Kernel_Slot = Class(name="fuml::Kernel::Slot")
Kernel_StructuralFeature = Class(name="Kernel::StructuralFeature")
Kernel_InstanceSpecification = Class(name="Kernel::InstanceSpecification")
fuml_Kernel_InstanceValue = Class(name="fuml::Kernel::InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
fuml_Kernel_LiteralBoolean = Class(name="fuml::Kernel::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
fuml_Kernel_LiteralSpecification = Class(name="fuml::Kernel::LiteralSpecification", is_abstract=True)
fuml_IntermediateActivities_ObjectFlow = Class(name="fuml::IntermediateActivities::ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
fuml_IntermediateActivities_ActivityEdge = Class(name="fuml::IntermediateActivities::ActivityEdge", is_abstract=True)
fuml_Kernel_LiteralString = Class(name="fuml::Kernel::LiteralString")
fuml_Kernel_LiteralUnlimitedNatural = Class(name="fuml::Kernel::LiteralUnlimitedNatural")
fuml_Kernel_PrimitiveType = Class(name="fuml::Kernel::PrimitiveType")
DataType = Class(name="DataType")
fuml_Kernel_Enumeration = Class(name="fuml::Kernel::Enumeration")
Kernel_EnumerationLiteral = Class(name="Kernel::EnumerationLiteral")
fuml_Kernel_EnumerationLiteral = Class(name="fuml::Kernel::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_Enumeration = Class(name="Kernel::Enumeration")
fuml_Kernel_Class = Class(name="fuml::Kernel::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
Communications_Reception = Class(name="Communications::Reception")
fuml_IntermediateActivities_ObjectNode = Class(name="fuml::IntermediateActivities::ObjectNode", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities::Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities::ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities::StructuredActivityNode")
fuml_IntermediateActivities_Activity = Class(name="fuml::IntermediateActivities::Activity")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities::ActivityEdge")
fuml_IntermediateActivities_ActivityNode = Class(name="fuml::IntermediateActivities::ActivityNode", is_abstract=True)
fuml_IntermediateActivities_MergeNode = Class(name="fuml::IntermediateActivities::MergeNode")
ControlNode = Class(name="ControlNode")
fuml_IntermediateActivities_ControlNode = Class(name="fuml::IntermediateActivities::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
fuml_IntermediateActivities_JoinNode = Class(name="fuml::IntermediateActivities::JoinNode")
fuml_IntermediateActivities_InitialNode = Class(name="fuml::IntermediateActivities::InitialNode")
fuml_IntermediateActivities_FinalNode = Class(name="fuml::IntermediateActivities::FinalNode", is_abstract=True)
fuml_IntermediateActivities_ForkNode = Class(name="fuml::IntermediateActivities::ForkNode")
fuml_IntermediateActivities_ControlFlow = Class(name="fuml::IntermediateActivities::ControlFlow")
fuml_IntermediateActivities_DecisionNode = Class(name="fuml::IntermediateActivities::DecisionNode")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities::ObjectFlow")
fuml_IntermediateActivities_ActivityFinalNode = Class(name="fuml::IntermediateActivities::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
fuml_IntermediateActivities_ActivityParameterNode = Class(name="fuml::IntermediateActivities::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
BasicActions_InputPin = Class(name="BasicActions::InputPin")
fuml_CompleteStructuredActivities_ExecutableNode = Class(name="fuml::CompleteStructuredActivities::ExecutableNode", is_abstract=True)
fuml_CompleteStructuredActivities_Clause = Class(name="fuml::CompleteStructuredActivities::Clause")
fuml_CompleteStructuredActivities_LoopNode = Class(name="fuml::CompleteStructuredActivities::LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions::OutputPin")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities::ExecutableNode")
fuml_CompleteStructuredActivities_StructuredActivityNode = Class(name="fuml::CompleteStructuredActivities::StructuredActivityNode")
Action = Class(name="Action")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities::Clause")
fuml_CompleteStructuredActivities_ConditionalNode = Class(name="fuml::CompleteStructuredActivities::ConditionalNode")
fuml_ExtraStructuredActivities_ExpansionRegion = Class(name="fuml::ExtraStructuredActivities::ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities::ExpansionNode")
fuml_IntermediateActions_StructuralFeatureAction = Class(name="fuml::IntermediateActions::StructuralFeatureAction", is_abstract=True)
fuml_IntermediateActions_TestIdentityAction = Class(name="fuml::IntermediateActions::TestIdentityAction")
fuml_ExtraStructuredActivities_ExpansionNode = Class(name="fuml::ExtraStructuredActivities::ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities::ExpansionRegion")
fuml_IntermediateActions_ValueSpecificationAction = Class(name="fuml::IntermediateActions::ValueSpecificationAction")
fuml_IntermediateActions_WriteLinkAction = Class(name="fuml::IntermediateActions::WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
fuml_IntermediateActions_LinkAction = Class(name="fuml::IntermediateActions::LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions::LinkEndData")
fuml_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="fuml::IntermediateActions::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
fuml_IntermediateActions_ReadLinkAction = Class(name="fuml::IntermediateActions::ReadLinkAction")
fuml_IntermediateActions_ReadSelfAction = Class(name="fuml::IntermediateActions::ReadSelfAction")
fuml_IntermediateActions_ReadStructuralFeatureAction = Class(name="fuml::IntermediateActions::ReadStructuralFeatureAction")
fuml_IntermediateActions_LinkEndCreationData = Class(name="fuml::IntermediateActions::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
fuml_IntermediateActions_LinkEndData = Class(name="fuml::IntermediateActions::LinkEndData")
fuml_IntermediateActions_WriteStructuralFeatureAction = Class(name="fuml::IntermediateActions::WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
fuml_IntermediateActions_ClearStructuralFeatureAction = Class(name="fuml::IntermediateActions::ClearStructuralFeatureAction")
fuml_IntermediateActions_CreateLinkAction = Class(name="fuml::IntermediateActions::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
fuml_IntermediateActions_CreateObjectAction = Class(name="fuml::IntermediateActions::CreateObjectAction")
fuml_IntermediateActions_DestroyLinkAction = Class(name="fuml::IntermediateActions::DestroyLinkAction")
fuml_IntermediateActions_DestroyObjectAction = Class(name="fuml::IntermediateActions::DestroyObjectAction")
fuml_IntermediateActions_LinkEndDestructionData = Class(name="fuml::IntermediateActions::LinkEndDestructionData")
fuml_IntermediateActions_ClearAssociationAction = Class(name="fuml::IntermediateActions::ClearAssociationAction")
fuml_CompleteActions_StartObjectBehaviorAction = Class(name="fuml::CompleteActions::StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
fuml_CompleteActions_ReduceAction = Class(name="fuml::CompleteActions::ReduceAction")
fuml_CompleteActions_ReadExtentAction = Class(name="fuml::CompleteActions::ReadExtentAction")
fuml_IntermediateActions_AddStructuralFeatureValueAction = Class(name="fuml::IntermediateActions::AddStructuralFeatureValueAction")
fuml_CompleteActions_StartClassifierBehaviorAction = Class(name="fuml::CompleteActions::StartClassifierBehaviorAction")
fuml_CompleteActions_ReclassifyObjectAction = Class(name="fuml::CompleteActions::ReclassifyObjectAction")
fuml_CompleteActions_AcceptEventAction = Class(name="fuml::CompleteActions::AcceptEventAction")
fuml_CompleteActions_ReadIsClassifiedObjectAction = Class(name="fuml::CompleteActions::ReadIsClassifiedObjectAction")
fuml_BasicActions_InputPin = Class(name="fuml::BasicActions::InputPin")
Pin = Class(name="Pin")
fuml_BasicActions_Pin = Class(name="fuml::BasicActions::Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities::ObjectNode")
fuml_BasicActions_CallAction = Class(name="fuml::BasicActions::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
fuml_BasicActions_InvocationAction = Class(name="fuml::BasicActions::InvocationAction", is_abstract=True)
fuml_BasicActions_SendSignalAction = Class(name="fuml::BasicActions::SendSignalAction")
Communications_Trigger = Class(name="Communications::Trigger")
fuml_BasicActions_Action = Class(name="fuml::BasicActions::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
fuml_BasicActions_OutputPin = Class(name="fuml::BasicActions::OutputPin")
fuml_Kernel_StructuredValue = Class(name="fuml::Kernel::StructuredValue", is_abstract=True)
Value = Class(name="Value")
fuml_Kernel_FeatureValue = Class(name="fuml::Kernel::FeatureValue")
Kernel_Value = Class(name="Kernel::Value")
fuml_Kernel_UnlimitedNaturalValue = Class(name="fuml::Kernel::UnlimitedNaturalValue")
PrimitiveValue = Class(name="PrimitiveValue")
fuml_Kernel_PrimitiveValue = Class(name="fuml::Kernel::PrimitiveValue", is_abstract=True)
fuml_BasicActions_CallBehaviorAction = Class(name="fuml::BasicActions::CallBehaviorAction")
fuml_BasicActions_CallOperationAction = Class(name="fuml::BasicActions::CallOperationAction")
fuml_Kernel_ExtensionalValue = Class(name="fuml::Kernel::ExtensionalValue", is_abstract=True)
CompoundValue = Class(name="CompoundValue")
LociL1_Locus = Class(name="LociL1::Locus")
fuml_Kernel_CompoundValue = Class(name="fuml::Kernel::CompoundValue", is_abstract=True)
Kernel_FeatureValue = Class(name="Kernel::FeatureValue")
fuml_Kernel_Link = Class(name="fuml::Kernel::Link")
fuml_Kernel_IntegerValue = Class(name="fuml::Kernel::IntegerValue")
fuml_Kernel_EnumerationValue = Class(name="fuml::Kernel::EnumerationValue")
Kernel_PrimitiveType = Class(name="Kernel::PrimitiveType")
fuml_Kernel_StringValue = Class(name="fuml::Kernel::StringValue")
fuml_Kernel_Reference = Class(name="fuml::Kernel::Reference")
StructuredValue = Class(name="StructuredValue")
Kernel_Object = Class(name="Kernel::Object")
fuml_Kernel_Object = Class(name="fuml::Kernel::Object")
ExtensionalValue = Class(name="ExtensionalValue")
fuml_LociL1_SemanticVisitor = Class(name="fuml::LociL1::SemanticVisitor", is_abstract=True)
fuml_LociL1_Locus = Class(name="fuml::LociL1::Locus")
Kernel_ExtensionalValue = Class(name="Kernel::ExtensionalValue")
fuml_BasicBehaviors_ParameterValue = Class(name="fuml::BasicBehaviors::ParameterValue")
fuml_Kernel_DataValue = Class(name="fuml::Kernel::DataValue")
fuml_Kernel_BooleanValue = Class(name="fuml::Kernel::BooleanValue")
fuml_Kernel_Value = Class(name="fuml::Kernel::Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")

# Kernel_Parameter class attributes and methods

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

# fuml_Communications_MessageEvent class attributes and methods

# Event class attributes and methods

# fuml_Communications_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# fuml_BasicBehaviors_BehavioredClassifier class attributes and methods

# Classifier class attributes and methods

# BasicBehaviors_Behavior class attributes and methods

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

# Kernel_Comment class attributes and methods

# fuml_Kernel_Comment class attributes and methods
fuml_Kernel_Comment_body: Property = Property(name="body", type=StringType)
fuml_Kernel_Comment.attributes={fuml_Kernel_Comment_body}

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

# Kernel_Namespace class attributes and methods

# fuml_Kernel_Element class attributes and methods

# Kernel_Element class attributes and methods

# fuml_Kernel_ElementImport class attributes and methods
fuml_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
fuml_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
fuml_Kernel_ElementImport.attributes={fuml_Kernel_ElementImport_visibility, fuml_Kernel_ElementImport_alias}

# fuml_Kernel_Namespace class attributes and methods

# Kernel_NamedElement class attributes and methods

# Kernel_ElementImport class attributes and methods

# Kernel_PackageImport class attributes and methods

# Kernel_PackageableElement class attributes and methods

# fuml_Kernel_Feature class attributes and methods
fuml_Kernel_Feature_static: Property = Property(name="static", type=BooleanType)
fuml_Kernel_Feature.attributes={fuml_Kernel_Feature_static}

# RedefinableElement class attributes and methods

# Kernel_Classifier class attributes and methods

# fuml_Kernel_PackageableElement class attributes and methods

# fuml_Kernel_PackageImport class attributes and methods
fuml_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
fuml_Kernel_PackageImport.attributes={fuml_Kernel_PackageImport_visibility}

# Kernel_Package class attributes and methods

# fuml_Kernel_Package class attributes and methods

# fuml_Kernel_Type class attributes and methods

# fuml_Kernel_StructuralFeature class attributes and methods
fuml_Kernel_StructuralFeature_readOnly: Property = Property(name="readOnly", type=BooleanType)
fuml_Kernel_StructuralFeature.attributes={fuml_Kernel_StructuralFeature_readOnly}

# Kernel_Feature class attributes and methods

# Kernel_MultiplicityElement class attributes and methods

# Kernel_TypedElement class attributes and methods

# fuml_Kernel_RedefinableElement class attributes and methods
fuml_Kernel_RedefinableElement_leaf: Property = Property(name="leaf", type=BooleanType)
fuml_Kernel_RedefinableElement.attributes={fuml_Kernel_RedefinableElement_leaf}

# Kernel_RedefinableElement class attributes and methods

# fuml_Kernel_Classifier class attributes and methods
fuml_Kernel_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
fuml_Kernel_Classifier_finalSpecialization: Property = Property(name="finalSpecialization", type=BooleanType)
fuml_Kernel_Classifier.attributes={fuml_Kernel_Classifier_abstract, fuml_Kernel_Classifier_finalSpecialization}

# Kernel_Generalization class attributes and methods

# Kernel_Class class attributes and methods

# fuml_Kernel_Generalization class attributes and methods
fuml_Kernel_Generalization_substitutable: Property = Property(name="substitutable", type=BooleanType)
fuml_Kernel_Generalization.attributes={fuml_Kernel_Generalization_substitutable}

# fuml_Kernel_Property class attributes and methods
fuml_Kernel_Property_derived: Property = Property(name="derived", type=BooleanType)
fuml_Kernel_Property_derivedUnion: Property = Property(name="derivedUnion", type=BooleanType)
fuml_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
fuml_Kernel_Property_composite: Property = Property(name="composite", type=BooleanType)
fuml_Kernel_Property.attributes={fuml_Kernel_Property_derivedUnion, fuml_Kernel_Property_derived, fuml_Kernel_Property_aggregation, fuml_Kernel_Property_composite}

# StructuralFeature class attributes and methods

# Kernel_Association class attributes and methods

# Kernel_DataType class attributes and methods

# Kernel_ValueSpecification class attributes and methods

# fuml_Kernel_Association class attributes and methods
fuml_Kernel_Association_derived: Property = Property(name="derived", type=BooleanType)
fuml_Kernel_Association.attributes={fuml_Kernel_Association_derived}

# fuml_Kernel_DataType class attributes and methods

# fuml_Kernel_MultiplicityElement class attributes and methods
fuml_Kernel_MultiplicityElement_ordered: Property = Property(name="ordered", type=BooleanType)
fuml_Kernel_MultiplicityElement_unique: Property = Property(name="unique", type=BooleanType)
fuml_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
fuml_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
fuml_Kernel_MultiplicityElement.attributes={fuml_Kernel_MultiplicityElement_unique, fuml_Kernel_MultiplicityElement_upper, fuml_Kernel_MultiplicityElement_lower, fuml_Kernel_MultiplicityElement_ordered}

# Kernel_Operation class attributes and methods

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
fuml_Kernel_Operation.attributes={fuml_Kernel_Operation_ordered, fuml_Kernel_Operation_query, fuml_Kernel_Operation_unique, fuml_Kernel_Operation_upper, fuml_Kernel_Operation_lower}

# fuml_Kernel_LiteralInteger class attributes and methods
fuml_Kernel_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_LiteralInteger.attributes={fuml_Kernel_LiteralInteger_value}

# fuml_Kernel_LiteralNull class attributes and methods

# fuml_Kernel_InstanceSpecification class attributes and methods

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

# fuml_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# fuml_IntermediateActivities_ActivityEdge class attributes and methods

# fuml_Kernel_LiteralString class attributes and methods
fuml_Kernel_LiteralString_value: Property = Property(name="value", type=StringType)
fuml_Kernel_LiteralString.attributes={fuml_Kernel_LiteralString_value}

# fuml_Kernel_LiteralUnlimitedNatural class attributes and methods
fuml_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_LiteralUnlimitedNatural.attributes={fuml_Kernel_LiteralUnlimitedNatural_value}

# fuml_Kernel_PrimitiveType class attributes and methods

# DataType class attributes and methods

# fuml_Kernel_Enumeration class attributes and methods

# Kernel_EnumerationLiteral class attributes and methods

# fuml_Kernel_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_Enumeration class attributes and methods

# fuml_Kernel_Class class attributes and methods
fuml_Kernel_Class_active: Property = Property(name="active", type=BooleanType)
fuml_Kernel_Class.attributes={fuml_Kernel_Class_active}

# BehavioredClassifier class attributes and methods

# Communications_Reception class attributes and methods

# fuml_IntermediateActivities_ObjectNode class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# fuml_IntermediateActivities_Activity class attributes and methods
fuml_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
fuml_IntermediateActivities_Activity.attributes={fuml_IntermediateActivities_Activity_readOnly}

# IntermediateActivities_ActivityEdge class attributes and methods

# fuml_IntermediateActivities_ActivityNode class attributes and methods

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

# BasicActions_InputPin class attributes and methods

# fuml_CompleteStructuredActivities_ExecutableNode class attributes and methods

# fuml_CompleteStructuredActivities_Clause class attributes and methods

# fuml_CompleteStructuredActivities_LoopNode class attributes and methods
fuml_CompleteStructuredActivities_LoopNode_testedFirst: Property = Property(name="testedFirst", type=BooleanType)
fuml_CompleteStructuredActivities_LoopNode.attributes={fuml_CompleteStructuredActivities_LoopNode_testedFirst}

# StructuredActivityNode class attributes and methods

# BasicActions_OutputPin class attributes and methods

# CompleteStructuredActivities_ExecutableNode class attributes and methods

# fuml_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
fuml_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
fuml_CompleteStructuredActivities_StructuredActivityNode.attributes={fuml_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# CompleteStructuredActivities_Clause class attributes and methods

# fuml_CompleteStructuredActivities_ConditionalNode class attributes and methods
fuml_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
fuml_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
fuml_CompleteStructuredActivities_ConditionalNode.attributes={fuml_CompleteStructuredActivities_ConditionalNode_determinate, fuml_CompleteStructuredActivities_ConditionalNode_assured}

# fuml_ExtraStructuredActivities_ExpansionRegion class attributes and methods
fuml_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
fuml_ExtraStructuredActivities_ExpansionRegion.attributes={fuml_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# fuml_IntermediateActions_StructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_TestIdentityAction class attributes and methods

# fuml_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# fuml_IntermediateActions_ValueSpecificationAction class attributes and methods

# fuml_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# fuml_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# fuml_IntermediateActions_RemoveStructuralFeatureValueAction class attributes and methods
fuml_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates: Property = Property(name="removeDuplicates", type=BooleanType)
fuml_IntermediateActions_RemoveStructuralFeatureValueAction.attributes={fuml_IntermediateActions_RemoveStructuralFeatureValueAction_removeDuplicates}

# WriteStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_ReadLinkAction class attributes and methods

# fuml_IntermediateActions_ReadSelfAction class attributes and methods

# fuml_IntermediateActions_ReadStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_LinkEndCreationData class attributes and methods
fuml_IntermediateActions_LinkEndCreationData_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_IntermediateActions_LinkEndCreationData.attributes={fuml_IntermediateActions_LinkEndCreationData_replaceAll}

# LinkEndData class attributes and methods

# fuml_IntermediateActions_LinkEndData class attributes and methods

# fuml_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# fuml_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# fuml_IntermediateActions_CreateObjectAction class attributes and methods

# fuml_IntermediateActions_DestroyLinkAction class attributes and methods

# fuml_IntermediateActions_DestroyObjectAction class attributes and methods
fuml_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
fuml_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
fuml_IntermediateActions_DestroyObjectAction.attributes={fuml_IntermediateActions_DestroyObjectAction_destroyOwnedObjects, fuml_IntermediateActions_DestroyObjectAction_destroyLinks}

# fuml_IntermediateActions_LinkEndDestructionData class attributes and methods
fuml_IntermediateActions_LinkEndDestructionData_destroyDuplicates: Property = Property(name="destroyDuplicates", type=BooleanType)
fuml_IntermediateActions_LinkEndDestructionData.attributes={fuml_IntermediateActions_LinkEndDestructionData_destroyDuplicates}

# fuml_IntermediateActions_ClearAssociationAction class attributes and methods

# fuml_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# fuml_CompleteActions_ReduceAction class attributes and methods
fuml_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
fuml_CompleteActions_ReduceAction.attributes={fuml_CompleteActions_ReduceAction_ordered}

# fuml_CompleteActions_ReadExtentAction class attributes and methods

# fuml_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
fuml_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_IntermediateActions_AddStructuralFeatureValueAction.attributes={fuml_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# fuml_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# fuml_CompleteActions_ReclassifyObjectAction class attributes and methods
fuml_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fuml_CompleteActions_ReclassifyObjectAction.attributes={fuml_CompleteActions_ReclassifyObjectAction_replaceAll}

# fuml_CompleteActions_AcceptEventAction class attributes and methods
fuml_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
fuml_CompleteActions_AcceptEventAction.attributes={fuml_CompleteActions_AcceptEventAction_unmarshall}

# fuml_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
fuml_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
fuml_CompleteActions_ReadIsClassifiedObjectAction.attributes={fuml_CompleteActions_ReadIsClassifiedObjectAction_direct}

# fuml_BasicActions_InputPin class attributes and methods

# Pin class attributes and methods

# fuml_BasicActions_Pin class attributes and methods

# IntermediateActivities_ObjectNode class attributes and methods

# fuml_BasicActions_CallAction class attributes and methods
fuml_BasicActions_CallAction_synchronous: Property = Property(name="synchronous", type=BooleanType)
fuml_BasicActions_CallAction.attributes={fuml_BasicActions_CallAction_synchronous}

# InvocationAction class attributes and methods

# fuml_BasicActions_InvocationAction class attributes and methods

# fuml_BasicActions_SendSignalAction class attributes and methods

# Communications_Trigger class attributes and methods

# fuml_BasicActions_Action class attributes and methods
fuml_BasicActions_Action_locallyReentrant: Property = Property(name="locallyReentrant", type=BooleanType)
fuml_BasicActions_Action.attributes={fuml_BasicActions_Action_locallyReentrant}

# ExecutableNode class attributes and methods

# fuml_BasicActions_OutputPin class attributes and methods

# fuml_Kernel_StructuredValue class attributes and methods

# Value class attributes and methods

# fuml_Kernel_FeatureValue class attributes and methods
fuml_Kernel_FeatureValue_position: Property = Property(name="position", type=IntegerType)
fuml_Kernel_FeatureValue.attributes={fuml_Kernel_FeatureValue_position}

# Kernel_Value class attributes and methods

# fuml_Kernel_UnlimitedNaturalValue class attributes and methods
fuml_Kernel_UnlimitedNaturalValue_value: Property = Property(name="value", type=IntegerType)
fuml_Kernel_UnlimitedNaturalValue.attributes={fuml_Kernel_UnlimitedNaturalValue_value}

# PrimitiveValue class attributes and methods

# fuml_Kernel_PrimitiveValue class attributes and methods

# fuml_BasicActions_CallBehaviorAction class attributes and methods

# fuml_BasicActions_CallOperationAction class attributes and methods

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

# Kernel_PrimitiveType class attributes and methods

# fuml_Kernel_StringValue class attributes and methods
fuml_Kernel_StringValue_value: Property = Property(name="value", type=StringType)
fuml_Kernel_StringValue.attributes={fuml_Kernel_StringValue_value}

# fuml_Kernel_Reference class attributes and methods

# StructuredValue class attributes and methods

# Kernel_Object class attributes and methods

# fuml_Kernel_Object class attributes and methods

# ExtensionalValue class attributes and methods

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
ownedParameter1: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1",
    ends={
        Property(name="Kernel_Parameter", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_Behavior", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="Syntax", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes", type=Kernel_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
context2: BinaryAssociation = BinaryAssociation(
    name="context2",
    ends={
        Property(name="BasicBehaviors_BehavioredClassifier", type=fuml_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_Behavior3", type=BasicBehaviors_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
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
ownedComment23: BinaryAssociation = BinaryAssociation(
    name="ownedComment23",
    ends={
        Property(name="Kernel_Comment", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Element", type=Kernel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement24: BinaryAssociation = BinaryAssociation(
    name="annotatedElement24",
    ends={
        Property(name="Kernel_Element", type=fuml_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Comment", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
signal11: BinaryAssociation = BinaryAssociation(
    name="signal11",
    ends={
        Property(name="Communications_Signal12", type=fuml_Communications_Reception, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Communications_Reception", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="Kernel_Type", type=fuml_Kernel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_TypedElement", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="Syntax16", type=fuml_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes15", type=Kernel_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement17: BinaryAssociation = BinaryAssociation(
    name="ownedElement17",
    ends={
        Property(name="Syntax19", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes18", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner20: BinaryAssociation = BinaryAssociation(
    name="owner20",
    ends={
        Property(name="Syntax22", type=fuml_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes21", type=Kernel_Element, multiplicity=Multiplicity(0, 1))
    }
)
member25: BinaryAssociation = BinaryAssociation(
    name="member25",
    ends={
        Property(name="Kernel_NamedElement", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport26: BinaryAssociation = BinaryAssociation(
    name="elementImport26",
    ends={
        Property(name="Syntax28", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes27", type=Kernel_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport29: BinaryAssociation = BinaryAssociation(
    name="packageImport29",
    ends={
        Property(name="Syntax31", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes30", type=Kernel_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember32: BinaryAssociation = BinaryAssociation(
    name="importedMember32",
    ends={
        Property(name="Kernel_PackageableElement", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Namespace33", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember34: BinaryAssociation = BinaryAssociation(
    name="ownedMember34",
    ends={
        Property(name="Syntax36", type=fuml_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes35", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier60: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier60",
    ends={
        Property(name="Syntax62", type=fuml_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes61", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement37: BinaryAssociation = BinaryAssociation(
    name="importedElement37",
    ends={
        Property(name="Kernel_PackageableElement38", type=fuml_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_ElementImport", type=Kernel_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace39: BinaryAssociation = BinaryAssociation(
    name="importingNamespace39",
    ends={
        Property(name="Syntax41", type=fuml_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes40", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage42: BinaryAssociation = BinaryAssociation(
    name="importedPackage42",
    ends={
        Property(name="Kernel_Package", type=fuml_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_PackageImport", type=Kernel_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace43: BinaryAssociation = BinaryAssociation(
    name="importingNamespace43",
    ends={
        Property(name="Syntax45", type=fuml_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes44", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement46: BinaryAssociation = BinaryAssociation(
    name="packagedElement46",
    ends={
        Property(name="Kernel_PackageableElement47", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Package", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType48: BinaryAssociation = BinaryAssociation(
    name="ownedType48",
    ends={
        Property(name="Syntax50", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes49", type=Kernel_Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage51: BinaryAssociation = BinaryAssociation(
    name="nestedPackage51",
    ends={
        Property(name="Syntax53", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes52", type=Kernel_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage54: BinaryAssociation = BinaryAssociation(
    name="nestingPackage54",
    ends={
        Property(name="Syntax56", type=fuml_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes55", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
package57: BinaryAssociation = BinaryAssociation(
    name="package57",
    ends={
        Property(name="Syntax59", type=fuml_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes58", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
attribute74: BinaryAssociation = BinaryAssociation(
    name="attribute74",
    ends={
        Property(name="Kernel_Property76", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier75", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general77: BinaryAssociation = BinaryAssociation(
    name="general77",
    ends={
        Property(name="Kernel_Classifier79", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier78", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement63: BinaryAssociation = BinaryAssociation(
    name="redefinedElement63",
    ends={
        Property(name="Kernel_RedefinableElement", type=fuml_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_RedefinableElement", type=Kernel_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext64: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext64",
    ends={
        Property(name="Kernel_Classifier", type=fuml_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_RedefinableElement65", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization66: BinaryAssociation = BinaryAssociation(
    name="generalization66",
    ends={
        Property(name="Syntax68", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes67", type=Kernel_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature69: BinaryAssociation = BinaryAssociation(
    name="feature69",
    ends={
        Property(name="Syntax71", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes70", type=Kernel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember72: BinaryAssociation = BinaryAssociation(
    name="inheritedMember72",
    ends={
        Property(name="Kernel_NamedElement73", type=fuml_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Classifier", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
class94: BinaryAssociation = BinaryAssociation(
    name="class94",
    ends={
        Property(name="Syntax96", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes95", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
opposite97: BinaryAssociation = BinaryAssociation(
    name="opposite97",
    ends={
        Property(name="Kernel_Property98", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Property", type=Kernel_Property, multiplicity=Multiplicity(0, 1))
    }
)
general80: BinaryAssociation = BinaryAssociation(
    name="general80",
    ends={
        Property(name="Kernel_Classifier81", type=fuml_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific82: BinaryAssociation = BinaryAssociation(
    name="specific82",
    ends={
        Property(name="Syntax84", type=fuml_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes83", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owningAssociation85: BinaryAssociation = BinaryAssociation(
    name="owningAssociation85",
    ends={
        Property(name="Syntax87", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes86", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
association88: BinaryAssociation = BinaryAssociation(
    name="association88",
    ends={
        Property(name="Syntax90", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes89", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
datatype91: BinaryAssociation = BinaryAssociation(
    name="datatype91",
    ends={
        Property(name="Syntax93", type=fuml_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes92", type=Kernel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
upperValue113: BinaryAssociation = BinaryAssociation(
    name="upperValue113",
    ends={
        Property(name="Kernel_ValueSpecification", type=fuml_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_MultiplicityElement", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue114: BinaryAssociation = BinaryAssociation(
    name="lowerValue114",
    ends={
        Property(name="Kernel_ValueSpecification116", type=fuml_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_MultiplicityElement115", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endType99: BinaryAssociation = BinaryAssociation(
    name="endType99",
    ends={
        Property(name="Kernel_Type100", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Association", type=Kernel_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd101: BinaryAssociation = BinaryAssociation(
    name="memberEnd101",
    ends={
        Property(name="Syntax103", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes102", type=Kernel_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableOwnedEnd104: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd104",
    ends={
        Property(name="Kernel_Property106", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Association105", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd107: BinaryAssociation = BinaryAssociation(
    name="ownedEnd107",
    ends={
        Property(name="Syntax109", type=fuml_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes108", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute110: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute110",
    ends={
        Property(name="Syntax112", type=fuml_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes111", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class121: BinaryAssociation = BinaryAssociation(
    name="class121",
    ends={
        Property(name="Syntax123", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes122", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation124: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation124",
    ends={
        Property(name="Kernel_Operation", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Operation", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter117: BinaryAssociation = BinaryAssociation(
    name="ownedParameter117",
    ends={
        Property(name="Kernel_Parameter118", type=fuml_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_BehavioralFeature", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method119: BinaryAssociation = BinaryAssociation(
    name="method119",
    ends={
        Property(name="Syntax120", type=fuml_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehaviors", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
type125: BinaryAssociation = BinaryAssociation(
    name="type125",
    ends={
        Property(name="Kernel_Type127", type=fuml_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Operation126", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
classifier128: BinaryAssociation = BinaryAssociation(
    name="classifier128",
    ends={
        Property(name="Kernel_Classifier129", type=fuml_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_InstanceSpecification", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot130: BinaryAssociation = BinaryAssociation(
    name="slot130",
    ends={
        Property(name="Syntax132", type=fuml_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes131", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature133: BinaryAssociation = BinaryAssociation(
    name="definingFeature133",
    ends={
        Property(name="Kernel_StructuralFeature", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Slot", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value134: BinaryAssociation = BinaryAssociation(
    name="value134",
    ends={
        Property(name="Kernel_ValueSpecification136", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Slot135", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance137: BinaryAssociation = BinaryAssociation(
    name="owningInstance137",
    ends={
        Property(name="Syntax139", type=fuml_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes138", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance140: BinaryAssociation = BinaryAssociation(
    name="instance140",
    ends={
        Property(name="Kernel_InstanceSpecification", type=fuml_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
ownedLiteral141: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral141",
    ends={
        Property(name="Syntax143", type=fuml_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes142", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration144: BinaryAssociation = BinaryAssociation(
    name="enumeration144",
    ends={
        Property(name="Syntax146", type=fuml_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes145", type=Kernel_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute147: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute147",
    ends={
        Property(name="Syntax149", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes148", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation150: BinaryAssociation = BinaryAssociation(
    name="ownedOperation150",
    ends={
        Property(name="Syntax152", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes151", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass153: BinaryAssociation = BinaryAssociation(
    name="superClass153",
    ends={
        Property(name="Kernel_Class", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception154: BinaryAssociation = BinaryAssociation(
    name="ownedReception154",
    ends={
        Property(name="Communications_Reception", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class155", type=Communications_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier156: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier156",
    ends={
        Property(name="Kernel_Classifier158", type=fuml_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Class157", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming187: BinaryAssociation = BinaryAssociation(
    name="incoming187",
    ends={
        Property(name="Syntax189", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities188", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity159: BinaryAssociation = BinaryAssociation(
    name="activity159",
    ends={
        Property(name="Syntax160", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source161: BinaryAssociation = BinaryAssociation(
    name="source161",
    ends={
        Property(name="Syntax163", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities162", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target164: BinaryAssociation = BinaryAssociation(
    name="target164",
    ends={
        Property(name="Syntax166", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities165", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode167: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode167",
    ends={
        Property(name="Syntax169", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities168", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
guard170: BinaryAssociation = BinaryAssociation(
    name="guard170",
    ends={
        Property(name="Kernel_ValueSpecification171", type=fuml_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node172: BinaryAssociation = BinaryAssociation(
    name="node172",
    ends={
        Property(name="Syntax174", type=fuml_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities173", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge175: BinaryAssociation = BinaryAssociation(
    name="edge175",
    ends={
        Property(name="Syntax177", type=fuml_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities176", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode178: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode178",
    ends={
        Property(name="Syntax180", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities179", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity181: BinaryAssociation = BinaryAssociation(
    name="activity181",
    ends={
        Property(name="Syntax183", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities182", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing184: BinaryAssociation = BinaryAssociation(
    name="outgoing184",
    ends={
        Property(name="Syntax186", type=fuml_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities185", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput190: BinaryAssociation = BinaryAssociation(
    name="decisionInput190",
    ends={
        Property(name="BasicBehaviors_Behavior191", type=fuml_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow192: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow192",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=fuml_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_DecisionNode193", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
bodyOutput199: BinaryAssociation = BinaryAssociation(
    name="bodyOutput199",
    ends={
        Property(name="BasicActions_OutputPin201", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode200", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput202: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput202",
    ends={
        Property(name="BasicActions_InputPin", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode203", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart204: BinaryAssociation = BinaryAssociation(
    name="bodyPart204",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode206", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode205", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result207: BinaryAssociation = BinaryAssociation(
    name="result207",
    ends={
        Property(name="BasicActions_OutputPin209", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode208", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable210: BinaryAssociation = BinaryAssociation(
    name="loopVariable210",
    ends={
        Property(name="BasicActions_OutputPin212", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode211", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart213: BinaryAssociation = BinaryAssociation(
    name="setupPart213",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode215", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode214", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test216: BinaryAssociation = BinaryAssociation(
    name="test216",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode217", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body218: BinaryAssociation = BinaryAssociation(
    name="body218",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode220", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause219", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
parameter194: BinaryAssociation = BinaryAssociation(
    name="parameter194",
    ends={
        Property(name="Kernel_Parameter195", type=fuml_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActivities_ActivityParameterNode", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
decider196: BinaryAssociation = BinaryAssociation(
    name="decider196",
    ends={
        Property(name="BasicActions_OutputPin", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test197: BinaryAssociation = BinaryAssociation(
    name="test197",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=fuml_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_LoopNode198", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
clause233: BinaryAssociation = BinaryAssociation(
    name="clause233",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=fuml_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result234: BinaryAssociation = BinaryAssociation(
    name="result234",
    ends={
        Property(name="BasicActions_OutputPin236", type=fuml_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_ConditionalNode235", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node237: BinaryAssociation = BinaryAssociation(
    name="node237",
    ends={
        Property(name="Syntax239", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities238", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge240: BinaryAssociation = BinaryAssociation(
    name="edge240",
    ends={
        Property(name="Syntax242", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities241", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeOutput243: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput243",
    ends={
        Property(name="BasicActions_OutputPin244", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput245: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput245",
    ends={
        Property(name="BasicActions_InputPin247", type=fuml_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_StructuredActivityNode246", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessorClause221: BinaryAssociation = BinaryAssociation(
    name="predecessorClause221",
    ends={
        Property(name="Syntax223", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities222", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause224: BinaryAssociation = BinaryAssociation(
    name="successorClause224",
    ends={
        Property(name="Syntax226", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities225", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider227: BinaryAssociation = BinaryAssociation(
    name="decider227",
    ends={
        Property(name="BasicActions_OutputPin229", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause228", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput230: BinaryAssociation = BinaryAssociation(
    name="bodyOutput230",
    ends={
        Property(name="BasicActions_OutputPin232", type=fuml_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteStructuredActivities_Clause231", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement254: BinaryAssociation = BinaryAssociation(
    name="inputElement254",
    ends={
        Property(name="Syntax256", type=fuml_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities255", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement257: BinaryAssociation = BinaryAssociation(
    name="outputElement257",
    ends={
        Property(name="Syntax259", type=fuml_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities258", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature260: BinaryAssociation = BinaryAssociation(
    name="structuralFeature260",
    ends={
        Property(name="Kernel_StructuralFeature261", type=fuml_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_StructuralFeatureAction", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object262: BinaryAssociation = BinaryAssociation(
    name="object262",
    ends={
        Property(name="BasicActions_InputPin264", type=fuml_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_StructuralFeatureAction263", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second265: BinaryAssociation = BinaryAssociation(
    name="second265",
    ends={
        Property(name="BasicActions_InputPin266", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
regionAsOutput248: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput248",
    ends={
        Property(name="Syntax250", type=fuml_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities249", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput251: BinaryAssociation = BinaryAssociation(
    name="regionAsInput251",
    ends={
        Property(name="Syntax253", type=fuml_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities252", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
result267: BinaryAssociation = BinaryAssociation(
    name="result267",
    ends={
        Property(name="BasicActions_OutputPin269", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction268", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first270: BinaryAssociation = BinaryAssociation(
    name="first270",
    ends={
        Property(name="BasicActions_InputPin272", type=fuml_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_TestIdentityAction271", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value273: BinaryAssociation = BinaryAssociation(
    name="value273",
    ends={
        Property(name="Kernel_ValueSpecification274", type=fuml_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result275: BinaryAssociation = BinaryAssociation(
    name="result275",
    ends={
        Property(name="BasicActions_OutputPin277", type=fuml_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ValueSpecificationAction276", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData278: BinaryAssociation = BinaryAssociation(
    name="endData278",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=fuml_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
result289: BinaryAssociation = BinaryAssociation(
    name="result289",
    ends={
        Property(name="BasicActions_OutputPin291", type=fuml_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_WriteStructuralFeatureAction290", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt292: BinaryAssociation = BinaryAssociation(
    name="removeAt292",
    ends={
        Property(name="BasicActions_InputPin293", type=fuml_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result294: BinaryAssociation = BinaryAssociation(
    name="result294",
    ends={
        Property(name="BasicActions_OutputPin295", type=fuml_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result296: BinaryAssociation = BinaryAssociation(
    name="result296",
    ends={
        Property(name="BasicActions_OutputPin297", type=fuml_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result298: BinaryAssociation = BinaryAssociation(
    name="result298",
    ends={
        Property(name="BasicActions_OutputPin299", type=fuml_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputValue279: BinaryAssociation = BinaryAssociation(
    name="inputValue279",
    ends={
        Property(name="BasicActions_InputPin281", type=fuml_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkAction280", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value282: BinaryAssociation = BinaryAssociation(
    name="value282",
    ends={
        Property(name="BasicActions_InputPin283", type=fuml_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end284: BinaryAssociation = BinaryAssociation(
    name="end284",
    ends={
        Property(name="Kernel_Property286", type=fuml_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndData285", type=Kernel_Property, multiplicity=Multiplicity(1, 1))
    }
)
value287: BinaryAssociation = BinaryAssociation(
    name="value287",
    ends={
        Property(name="BasicActions_InputPin288", type=fuml_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object305: BinaryAssociation = BinaryAssociation(
    name="object305",
    ends={
        Property(name="BasicActions_InputPin307", type=fuml_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearAssociationAction306", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result308: BinaryAssociation = BinaryAssociation(
    name="result308",
    ends={
        Property(name="BasicActions_OutputPin309", type=fuml_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result310: BinaryAssociation = BinaryAssociation(
    name="result310",
    ends={
        Property(name="BasicActions_OutputPin311", type=fuml_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier312: BinaryAssociation = BinaryAssociation(
    name="classifier312",
    ends={
        Property(name="Kernel_Classifier314", type=fuml_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_CreateObjectAction313", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
insertAt300: BinaryAssociation = BinaryAssociation(
    name="insertAt300",
    ends={
        Property(name="BasicActions_InputPin301", type=fuml_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt302: BinaryAssociation = BinaryAssociation(
    name="destroyAt302",
    ends={
        Property(name="BasicActions_InputPin303", type=fuml_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
association304: BinaryAssociation = BinaryAssociation(
    name="association304",
    ends={
        Property(name="Kernel_Association", type=fuml_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_ClearAssociationAction", type=Kernel_Association, multiplicity=Multiplicity(1, 1))
    }
)
object319: BinaryAssociation = BinaryAssociation(
    name="object319",
    ends={
        Property(name="BasicActions_InputPin320", type=fuml_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object321: BinaryAssociation = BinaryAssociation(
    name="object321",
    ends={
        Property(name="BasicActions_InputPin322", type=fuml_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reducer323: BinaryAssociation = BinaryAssociation(
    name="reducer323",
    ends={
        Property(name="BasicBehaviors_Behavior324", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result325: BinaryAssociation = BinaryAssociation(
    name="result325",
    ends={
        Property(name="BasicActions_OutputPin327", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction326", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection328: BinaryAssociation = BinaryAssociation(
    name="collection328",
    ends={
        Property(name="BasicActions_InputPin330", type=fuml_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReduceAction329", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result331: BinaryAssociation = BinaryAssociation(
    name="result331",
    ends={
        Property(name="BasicActions_OutputPin332", type=fuml_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target315: BinaryAssociation = BinaryAssociation(
    name="target315",
    ends={
        Property(name="BasicActions_InputPin316", type=fuml_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt317: BinaryAssociation = BinaryAssociation(
    name="insertAt317",
    ends={
        Property(name="BasicActions_InputPin318", type=fuml_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object341: BinaryAssociation = BinaryAssociation(
    name="object341",
    ends={
        Property(name="BasicActions_InputPin343", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction342", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier344: BinaryAssociation = BinaryAssociation(
    name="oldClassifier344",
    ends={
        Property(name="Kernel_Classifier345", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
object346: BinaryAssociation = BinaryAssociation(
    name="object346",
    ends={
        Property(name="BasicActions_InputPin348", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction347", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier349: BinaryAssociation = BinaryAssociation(
    name="newClassifier349",
    ends={
        Property(name="Kernel_Classifier351", type=fuml_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReclassifyObjectAction350", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
classifier333: BinaryAssociation = BinaryAssociation(
    name="classifier333",
    ends={
        Property(name="Kernel_Classifier335", type=fuml_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadExtentAction334", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier336: BinaryAssociation = BinaryAssociation(
    name="classifier336",
    ends={
        Property(name="Kernel_Classifier337", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result338: BinaryAssociation = BinaryAssociation(
    name="result338",
    ends={
        Property(name="BasicActions_OutputPin340", type=fuml_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_ReadIsClassifiedObjectAction339", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context358: BinaryAssociation = BinaryAssociation(
    name="context358",
    ends={
        Property(name="Kernel_Classifier360", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_Action359", type=Kernel_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
input361: BinaryAssociation = BinaryAssociation(
    name="input361",
    ends={
        Property(name="BasicActions_InputPin363", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_Action362", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result364: BinaryAssociation = BinaryAssociation(
    name="result364",
    ends={
        Property(name="BasicActions_OutputPin365", type=fuml_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument366: BinaryAssociation = BinaryAssociation(
    name="argument366",
    ends={
        Property(name="BasicActions_InputPin367", type=fuml_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target368: BinaryAssociation = BinaryAssociation(
    name="target368",
    ends={
        Property(name="BasicActions_InputPin369", type=fuml_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result352: BinaryAssociation = BinaryAssociation(
    name="result352",
    ends={
        Property(name="BasicActions_OutputPin353", type=fuml_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger354: BinaryAssociation = BinaryAssociation(
    name="trigger354",
    ends={
        Property(name="Communications_Trigger", type=fuml_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_CompleteActions_AcceptEventAction355", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output356: BinaryAssociation = BinaryAssociation(
    name="output356",
    ends={
        Property(name="BasicActions_OutputPin357", type=fuml_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
target377: BinaryAssociation = BinaryAssociation(
    name="target377",
    ends={
        Property(name="BasicActions_InputPin379", type=fuml_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallOperationAction378", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature380: BinaryAssociation = BinaryAssociation(
    name="feature380",
    ends={
        Property(name="Kernel_StructuralFeature381", type=fuml_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_FeatureValue", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
values382: BinaryAssociation = BinaryAssociation(
    name="values382",
    ends={
        Property(name="Kernel_Value", type=fuml_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_FeatureValue383", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal370: BinaryAssociation = BinaryAssociation(
    name="signal370",
    ends={
        Property(name="Communications_Signal372", type=fuml_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_SendSignalAction371", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
behavior373: BinaryAssociation = BinaryAssociation(
    name="behavior373",
    ends={
        Property(name="BasicBehaviors_Behavior374", type=fuml_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation375: BinaryAssociation = BinaryAssociation(
    name="operation375",
    ends={
        Property(name="Kernel_Operation376", type=fuml_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicActions_CallOperationAction", type=Kernel_Operation, multiplicity=Multiplicity(1, 1))
    }
)
types386: BinaryAssociation = BinaryAssociation(
    name="types386",
    ends={
        Property(name="Kernel_Class387", type=fuml_Kernel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Object", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
locus388: BinaryAssociation = BinaryAssociation(
    name="locus388",
    ends={
        Property(name="Semantics", type=fuml_Kernel_ExtensionalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Loci", type=LociL1_Locus, multiplicity=Multiplicity(0, 1))
    }
)
featureValues389: BinaryAssociation = BinaryAssociation(
    name="featureValues389",
    ends={
        Property(name="Kernel_FeatureValue", type=fuml_Kernel_CompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_CompoundValue", type=Kernel_FeatureValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type390: BinaryAssociation = BinaryAssociation(
    name="type390",
    ends={
        Property(name="Kernel_Association391", type=fuml_Kernel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Link", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
literal392: BinaryAssociation = BinaryAssociation(
    name="literal392",
    ends={
        Property(name="Kernel_EnumerationLiteral", type=fuml_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_EnumerationValue", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type384: BinaryAssociation = BinaryAssociation(
    name="type384",
    ends={
        Property(name="Kernel_PrimitiveType", type=fuml_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
referent385: BinaryAssociation = BinaryAssociation(
    name="referent385",
    ends={
        Property(name="Kernel_Object", type=fuml_Kernel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_Reference", type=Kernel_Object, multiplicity=Multiplicity(1, 1))
    }
)
extensionalValues396: BinaryAssociation = BinaryAssociation(
    name="extensionalValues396",
    ends={
        Property(name="Semantics398", type=fuml_LociL1_Locus, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes397", type=Kernel_ExtensionalValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter399: BinaryAssociation = BinaryAssociation(
    name="parameter399",
    ends={
        Property(name="Kernel_Parameter400", type=fuml_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_ParameterValue", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
values401: BinaryAssociation = BinaryAssociation(
    name="values401",
    ends={
        Property(name="Kernel_Value403", type=fuml_BasicBehaviors_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_BasicBehaviors_ParameterValue402", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type393: BinaryAssociation = BinaryAssociation(
    name="type393",
    ends={
        Property(name="Kernel_Enumeration", type=fuml_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_EnumerationValue394", type=Kernel_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
type395: BinaryAssociation = BinaryAssociation(
    name="type395",
    ends={
        Property(name="Kernel_DataType", type=fuml_Kernel_DataValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fuml_Kernel_DataValue", type=Kernel_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fuml_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=fuml_BasicBehaviors_OpaqueBehavior)
gen_fuml_BasicBehaviors_Behavior_Class = Generalization(general=Class_, specific=fuml_BasicBehaviors_Behavior)
gen_fuml_Communications_MessageEvent_Event = Generalization(general=Event, specific=fuml_Communications_MessageEvent)
gen_fuml_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fuml_Communications_Reception)
gen_fuml_BasicBehaviors_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=fuml_BasicBehaviors_BehavioredClassifier)
gen_fuml_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=fuml_BasicBehaviors_FunctionBehavior)
gen_fuml_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=fuml_Communications_Trigger)
gen_fuml_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=fuml_Communications_Event)
gen_fuml_Communications_Signal_Classifier = Generalization(general=Classifier, specific=fuml_Communications_Signal)
gen_fuml_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=fuml_Communications_SignalEvent)
gen_fuml_Kernel_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=fuml_Kernel_ValueSpecification)
gen_fuml_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_TypedElement)
gen_fuml_Kernel_NamedElement_Element = Generalization(general=Element, specific=fuml_Kernel_NamedElement)
gen_fuml_Kernel_ElementImport_Element = Generalization(general=Element, specific=fuml_Kernel_ElementImport)
gen_fuml_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_Namespace)
gen_fuml_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_Kernel_Feature)
gen_fuml_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_PackageableElement)
gen_fuml_Kernel_PackageImport_Element = Generalization(general=Element, specific=fuml_Kernel_PackageImport)
gen_fuml_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fuml_Kernel_Package)
gen_fuml_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=fuml_Kernel_Package)
gen_fuml_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=fuml_Kernel_Type)
gen_fuml_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fuml_Kernel_StructuralFeature)
gen_fuml_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_RedefinableElement)
gen_fuml_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fuml_Kernel_Classifier)
gen_fuml_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=fuml_Kernel_Classifier)
gen_fuml_Kernel_Generalization_Element = Generalization(general=Element, specific=fuml_Kernel_Generalization)
gen_fuml_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=fuml_Kernel_Property)
gen_fuml_Kernel_Association_Classifier = Generalization(general=Classifier, specific=fuml_Kernel_Association)
gen_fuml_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=fuml_Kernel_DataType)
gen_fuml_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=fuml_Kernel_MultiplicityElement)
gen_fuml_Kernel_BehavioralFeature_Feature = Generalization(general=Feature, specific=fuml_Kernel_BehavioralFeature)
gen_fuml_Kernel_Parameter_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_Kernel_Parameter)
gen_fuml_Kernel_Parameter_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fuml_Kernel_Parameter)
gen_fuml_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fuml_Kernel_Operation)
gen_fuml_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralInteger)
gen_fuml_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralNull)
gen_fuml_Kernel_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=fuml_Kernel_InstanceSpecification)
gen_fuml_Kernel_Slot_Element = Generalization(general=Element, specific=fuml_Kernel_Slot)
gen_fuml_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=fuml_Kernel_InstanceValue)
gen_fuml_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralBoolean)
gen_fuml_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=fuml_Kernel_LiteralSpecification)
gen_fuml_IntermediateActivities_ObjectFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=fuml_IntermediateActivities_ObjectFlow)
gen_fuml_IntermediateActivities_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_IntermediateActivities_ActivityEdge)
gen_fuml_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralString)
gen_fuml_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fuml_Kernel_LiteralUnlimitedNatural)
gen_fuml_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=fuml_Kernel_PrimitiveType)
gen_fuml_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=fuml_Kernel_Enumeration)
gen_fuml_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=fuml_Kernel_EnumerationLiteral)
gen_fuml_Kernel_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=fuml_Kernel_Class)
gen_fuml_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode = Generalization(general=IntermediateActivities_ActivityNode, specific=fuml_IntermediateActivities_ObjectNode)
gen_fuml_IntermediateActivities_Activity_Behavior = Generalization(general=Behavior, specific=fuml_IntermediateActivities_Activity)
gen_fuml_IntermediateActivities_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=fuml_IntermediateActivities_ActivityNode)
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
gen_fuml_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_CompleteStructuredActivities_LoopNode)
gen_fuml_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=fuml_CompleteStructuredActivities_StructuredActivityNode)
gen_fuml_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_CompleteStructuredActivities_ConditionalNode)
gen_fuml_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fuml_ExtraStructuredActivities_ExpansionRegion)
gen_fuml_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_StructuralFeatureAction)
gen_fuml_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_TestIdentityAction)
gen_fuml_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=fuml_ExtraStructuredActivities_ExpansionNode)
gen_fuml_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ValueSpecificationAction)
gen_fuml_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=fuml_IntermediateActions_WriteLinkAction)
gen_fuml_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_LinkAction)
gen_fuml_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fuml_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_fuml_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=fuml_IntermediateActions_ReadLinkAction)
gen_fuml_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ReadSelfAction)
gen_fuml_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_ReadStructuralFeatureAction)
gen_fuml_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=fuml_IntermediateActions_LinkEndCreationData)
gen_fuml_IntermediateActions_LinkEndData_Element = Generalization(general=Element, specific=fuml_IntermediateActions_LinkEndData)
gen_fuml_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_WriteStructuralFeatureAction)
gen_fuml_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fuml_IntermediateActions_ClearStructuralFeatureAction)
gen_fuml_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fuml_IntermediateActions_CreateLinkAction)
gen_fuml_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_CreateObjectAction)
gen_fuml_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fuml_IntermediateActions_DestroyLinkAction)
gen_fuml_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_DestroyObjectAction)
gen_fuml_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=fuml_IntermediateActions_LinkEndDestructionData)
gen_fuml_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=fuml_IntermediateActions_ClearAssociationAction)
gen_fuml_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=fuml_CompleteActions_StartObjectBehaviorAction)
gen_fuml_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReduceAction)
gen_fuml_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReadExtentAction)
gen_fuml_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fuml_IntermediateActions_AddStructuralFeatureValueAction)
gen_fuml_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_StartClassifierBehaviorAction)
gen_fuml_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReclassifyObjectAction)
gen_fuml_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_AcceptEventAction)
gen_fuml_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=fuml_CompleteActions_ReadIsClassifiedObjectAction)
gen_fuml_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=fuml_BasicActions_InputPin)
gen_fuml_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=fuml_BasicActions_Pin)
gen_fuml_BasicActions_Pin_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fuml_BasicActions_Pin)
gen_fuml_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=fuml_BasicActions_CallAction)
gen_fuml_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=fuml_BasicActions_InvocationAction)
gen_fuml_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=fuml_BasicActions_SendSignalAction)
gen_fuml_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=fuml_BasicActions_Action)
gen_fuml_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=fuml_BasicActions_OutputPin)
gen_fuml_Kernel_StructuredValue_Value = Generalization(general=Value, specific=fuml_Kernel_StructuredValue)
gen_fuml_Kernel_UnlimitedNaturalValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_UnlimitedNaturalValue)
gen_fuml_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=fuml_Kernel_PrimitiveValue)
gen_fuml_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=fuml_BasicActions_CallBehaviorAction)
gen_fuml_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=fuml_BasicActions_CallOperationAction)
gen_fuml_Kernel_ExtensionalValue_CompoundValue = Generalization(general=CompoundValue, specific=fuml_Kernel_ExtensionalValue)
gen_fuml_Kernel_CompoundValue_StructuredValue = Generalization(general=StructuredValue, specific=fuml_Kernel_CompoundValue)
gen_fuml_Kernel_Link_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fuml_Kernel_Link)
gen_fuml_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_IntegerValue)
gen_fuml_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=fuml_Kernel_EnumerationValue)
gen_fuml_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_StringValue)
gen_fuml_Kernel_Reference_StructuredValue = Generalization(general=StructuredValue, specific=fuml_Kernel_Reference)
gen_fuml_Kernel_Object_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fuml_Kernel_Object)
gen_fuml_Kernel_DataValue_CompoundValue = Generalization(general=CompoundValue, specific=fuml_Kernel_DataValue)
gen_fuml_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fuml_Kernel_BooleanValue)
gen_fuml_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=fuml_Kernel_Value)

# Domain Model
domain_model = DomainModel(
    name="fuml",
    types={Kernel_Parameter, fuml_BasicBehaviors_OpaqueBehavior, Behavior, fuml_BasicBehaviors_Behavior, Class_, Kernel_BehavioralFeature, fuml_Communications_MessageEvent, Event, fuml_Communications_Reception, BehavioralFeature, BasicBehaviors_BehavioredClassifier, fuml_BasicBehaviors_BehavioredClassifier, Classifier, BasicBehaviors_Behavior, fuml_BasicBehaviors_FunctionBehavior, OpaqueBehavior, fuml_Communications_Trigger, NamedElement, Communications_Event, fuml_Communications_Event, PackageableElement, fuml_Communications_Signal, Kernel_Property, fuml_Communications_SignalEvent, MessageEvent, Communications_Signal, Kernel_Comment, fuml_Kernel_Comment, fuml_Kernel_ValueSpecification, TypedElement, fuml_Kernel_TypedElement, Kernel_Type, fuml_Kernel_NamedElement, Element, Kernel_Namespace, fuml_Kernel_Element, Kernel_Element, fuml_Kernel_ElementImport, fuml_Kernel_Namespace, Kernel_NamedElement, Kernel_ElementImport, Kernel_PackageImport, Kernel_PackageableElement, fuml_Kernel_Feature, RedefinableElement, Kernel_Classifier, fuml_Kernel_PackageableElement, fuml_Kernel_PackageImport, Kernel_Package, fuml_Kernel_Package, fuml_Kernel_Type, fuml_Kernel_StructuralFeature, Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement, fuml_Kernel_RedefinableElement, Kernel_RedefinableElement, fuml_Kernel_Classifier, Kernel_Generalization, Kernel_Class, fuml_Kernel_Generalization, fuml_Kernel_Property, StructuralFeature, Kernel_Association, Kernel_DataType, Kernel_ValueSpecification, fuml_Kernel_Association, fuml_Kernel_DataType, fuml_Kernel_MultiplicityElement, Kernel_Operation, fuml_Kernel_BehavioralFeature, Feature, fuml_Kernel_Parameter, fuml_Kernel_Operation, fuml_Kernel_LiteralInteger, fuml_Kernel_LiteralNull, fuml_Kernel_InstanceSpecification, Kernel_Slot, fuml_Kernel_Slot, Kernel_StructuralFeature, Kernel_InstanceSpecification, fuml_Kernel_InstanceValue, ValueSpecification, fuml_Kernel_LiteralBoolean, LiteralSpecification, fuml_Kernel_LiteralSpecification, fuml_IntermediateActivities_ObjectFlow, ActivityEdge, fuml_IntermediateActivities_ActivityEdge, fuml_Kernel_LiteralString, fuml_Kernel_LiteralUnlimitedNatural, fuml_Kernel_PrimitiveType, DataType, fuml_Kernel_Enumeration, Kernel_EnumerationLiteral, fuml_Kernel_EnumerationLiteral, InstanceSpecification, Kernel_Enumeration, fuml_Kernel_Class, BehavioredClassifier, Communications_Reception, fuml_IntermediateActivities_ObjectNode, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, fuml_IntermediateActivities_Activity, IntermediateActivities_ActivityEdge, fuml_IntermediateActivities_ActivityNode, fuml_IntermediateActivities_MergeNode, ControlNode, fuml_IntermediateActivities_ControlNode, ActivityNode, fuml_IntermediateActivities_JoinNode, fuml_IntermediateActivities_InitialNode, fuml_IntermediateActivities_FinalNode, fuml_IntermediateActivities_ForkNode, fuml_IntermediateActivities_ControlFlow, fuml_IntermediateActivities_DecisionNode, IntermediateActivities_ObjectFlow, fuml_IntermediateActivities_ActivityFinalNode, FinalNode, fuml_IntermediateActivities_ActivityParameterNode, ObjectNode, BasicActions_InputPin, fuml_CompleteStructuredActivities_ExecutableNode, fuml_CompleteStructuredActivities_Clause, fuml_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, fuml_CompleteStructuredActivities_StructuredActivityNode, Action, CompleteStructuredActivities_Clause, fuml_CompleteStructuredActivities_ConditionalNode, fuml_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, fuml_IntermediateActions_StructuralFeatureAction, fuml_IntermediateActions_TestIdentityAction, fuml_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, fuml_IntermediateActions_ValueSpecificationAction, fuml_IntermediateActions_WriteLinkAction, LinkAction, fuml_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, fuml_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, fuml_IntermediateActions_ReadLinkAction, fuml_IntermediateActions_ReadSelfAction, fuml_IntermediateActions_ReadStructuralFeatureAction, fuml_IntermediateActions_LinkEndCreationData, LinkEndData, fuml_IntermediateActions_LinkEndData, fuml_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, fuml_IntermediateActions_ClearStructuralFeatureAction, fuml_IntermediateActions_CreateLinkAction, WriteLinkAction, fuml_IntermediateActions_CreateObjectAction, fuml_IntermediateActions_DestroyLinkAction, fuml_IntermediateActions_DestroyObjectAction, fuml_IntermediateActions_LinkEndDestructionData, fuml_IntermediateActions_ClearAssociationAction, fuml_CompleteActions_StartObjectBehaviorAction, CallAction, fuml_CompleteActions_ReduceAction, fuml_CompleteActions_ReadExtentAction, fuml_IntermediateActions_AddStructuralFeatureValueAction, fuml_CompleteActions_StartClassifierBehaviorAction, fuml_CompleteActions_ReclassifyObjectAction, fuml_CompleteActions_AcceptEventAction, fuml_CompleteActions_ReadIsClassifiedObjectAction, fuml_BasicActions_InputPin, Pin, fuml_BasicActions_Pin, IntermediateActivities_ObjectNode, fuml_BasicActions_CallAction, InvocationAction, fuml_BasicActions_InvocationAction, fuml_BasicActions_SendSignalAction, Communications_Trigger, fuml_BasicActions_Action, ExecutableNode, fuml_BasicActions_OutputPin, fuml_Kernel_StructuredValue, Value, fuml_Kernel_FeatureValue, Kernel_Value, fuml_Kernel_UnlimitedNaturalValue, PrimitiveValue, fuml_Kernel_PrimitiveValue, fuml_BasicActions_CallBehaviorAction, fuml_BasicActions_CallOperationAction, fuml_Kernel_ExtensionalValue, CompoundValue, LociL1_Locus, fuml_Kernel_CompoundValue, Kernel_FeatureValue, fuml_Kernel_Link, fuml_Kernel_IntegerValue, fuml_Kernel_EnumerationValue, Kernel_PrimitiveType, fuml_Kernel_StringValue, fuml_Kernel_Reference, StructuredValue, Kernel_Object, fuml_Kernel_Object, ExtensionalValue, fuml_LociL1_SemanticVisitor, fuml_LociL1_Locus, Kernel_ExtensionalValue, fuml_BasicBehaviors_ParameterValue, fuml_Kernel_DataValue, fuml_Kernel_BooleanValue, fuml_Kernel_Value, SemanticVisitor, CallConcurrencyKind, VisibilityKind, AggregationKind, ParameterDirectionKind, ExpansionKind},
    associations={ownedParameter1, specification0, context2, ownedBehavior4, classifierBehavior5, event8, ownedAttribute9, signal10, ownedComment23, annotatedElement24, signal11, type13, namespace14, ownedElement17, owner20, member25, elementImport26, packageImport29, importedMember32, ownedMember34, featuringClassifier60, importedElement37, importingNamespace39, importedPackage42, importingNamespace43, packagedElement46, ownedType48, nestedPackage51, nestingPackage54, package57, attribute74, general77, redefinedElement63, redefinitionContext64, generalization66, feature69, inheritedMember72, class94, opposite97, general80, specific82, owningAssociation85, association88, datatype91, upperValue113, lowerValue114, endType99, memberEnd101, navigableOwnedEnd104, ownedEnd107, ownedAttribute110, class121, redefinedOperation124, ownedParameter117, method119, type125, classifier128, slot130, definingFeature133, value134, owningInstance137, instance140, ownedLiteral141, enumeration144, ownedAttribute147, ownedOperation150, superClass153, ownedReception154, nestedClassifier156, incoming187, activity159, source161, target164, inStructuredNode167, guard170, node172, edge175, inStructuredNode178, activity181, outgoing184, decisionInput190, decisionInputFlow192, bodyOutput199, loopVariableInput202, bodyPart204, result207, loopVariable210, setupPart213, test216, body218, parameter194, decider196, test197, clause233, result234, node237, edge240, structuredNodeOutput243, structuredNodeInput245, predecessorClause221, successorClause224, decider227, bodyOutput230, inputElement254, outputElement257, structuralFeature260, object262, second265, regionAsOutput248, regionAsInput251, result267, first270, value273, result275, endData278, result289, removeAt292, result294, result296, result298, inputValue279, value282, end284, value287, object305, result308, result310, classifier312, insertAt300, destroyAt302, association304, object319, object321, reducer323, result325, collection328, result331, target315, insertAt317, object341, oldClassifier344, object346, newClassifier349, classifier333, classifier336, result338, context358, input361, result364, argument366, target368, result352, trigger354, output356, target377, feature380, values382, signal370, behavior373, operation375, types386, locus388, featureValues389, type390, literal392, type384, referent385, extensionalValues396, parameter399, values401, type393, type395},
    generalizations={gen_fuml_BasicBehaviors_OpaqueBehavior_Behavior, gen_fuml_BasicBehaviors_Behavior_Class, gen_fuml_Communications_MessageEvent_Event, gen_fuml_Communications_Reception_BehavioralFeature, gen_fuml_BasicBehaviors_BehavioredClassifier_Classifier, gen_fuml_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_fuml_Communications_Trigger_NamedElement, gen_fuml_Communications_Event_PackageableElement, gen_fuml_Communications_Signal_Classifier, gen_fuml_Communications_SignalEvent_MessageEvent, gen_fuml_Kernel_ValueSpecification_TypedElement, gen_fuml_Kernel_TypedElement_NamedElement, gen_fuml_Kernel_NamedElement_Element, gen_fuml_Kernel_ElementImport_Element, gen_fuml_Kernel_Namespace_NamedElement, gen_fuml_Kernel_Feature_RedefinableElement, gen_fuml_Kernel_PackageableElement_NamedElement, gen_fuml_Kernel_PackageImport_Element, gen_fuml_Kernel_Package_Kernel_Namespace, gen_fuml_Kernel_Package_Kernel_PackageableElement, gen_fuml_Kernel_Type_PackageableElement, gen_fuml_Kernel_StructuralFeature_Kernel_Feature, gen_fuml_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_fuml_Kernel_StructuralFeature_Kernel_TypedElement, gen_fuml_Kernel_RedefinableElement_NamedElement, gen_fuml_Kernel_Classifier_Kernel_Namespace, gen_fuml_Kernel_Classifier_Kernel_Type, gen_fuml_Kernel_Generalization_Element, gen_fuml_Kernel_Property_StructuralFeature, gen_fuml_Kernel_Association_Classifier, gen_fuml_Kernel_DataType_Classifier, gen_fuml_Kernel_MultiplicityElement_Element, gen_fuml_Kernel_BehavioralFeature_Feature, gen_fuml_Kernel_Parameter_Kernel_MultiplicityElement, gen_fuml_Kernel_Parameter_Kernel_TypedElement, gen_fuml_Kernel_Operation_BehavioralFeature, gen_fuml_Kernel_LiteralInteger_LiteralSpecification, gen_fuml_Kernel_LiteralNull_LiteralSpecification, gen_fuml_Kernel_InstanceSpecification_NamedElement, gen_fuml_Kernel_Slot_Element, gen_fuml_Kernel_InstanceValue_ValueSpecification, gen_fuml_Kernel_LiteralBoolean_LiteralSpecification, gen_fuml_Kernel_LiteralSpecification_ValueSpecification, gen_fuml_IntermediateActivities_ObjectFlow_ActivityEdge, gen_fuml_IntermediateActivities_ActivityEdge_RedefinableElement, gen_fuml_Kernel_LiteralString_LiteralSpecification, gen_fuml_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_fuml_Kernel_PrimitiveType_DataType, gen_fuml_Kernel_Enumeration_DataType, gen_fuml_Kernel_EnumerationLiteral_InstanceSpecification, gen_fuml_Kernel_Class_BehavioredClassifier, gen_fuml_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_fuml_IntermediateActivities_Activity_Behavior, gen_fuml_IntermediateActivities_ActivityNode_RedefinableElement, gen_fuml_IntermediateActivities_ObjectNode_Kernel_TypedElement, gen_fuml_IntermediateActivities_MergeNode_ControlNode, gen_fuml_IntermediateActivities_ControlNode_ActivityNode, gen_fuml_IntermediateActivities_JoinNode_ControlNode, gen_fuml_IntermediateActivities_InitialNode_ControlNode, gen_fuml_IntermediateActivities_FinalNode_ControlNode, gen_fuml_IntermediateActivities_ForkNode_ControlNode, gen_fuml_IntermediateActivities_ControlFlow_ActivityEdge, gen_fuml_IntermediateActivities_DecisionNode_ControlNode, gen_fuml_IntermediateActivities_ActivityFinalNode_FinalNode, gen_fuml_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_fuml_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_fuml_CompleteStructuredActivities_Clause_Element, gen_fuml_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_fuml_CompleteStructuredActivities_StructuredActivityNode_Action, gen_fuml_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_fuml_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_fuml_IntermediateActions_StructuralFeatureAction_Action, gen_fuml_IntermediateActions_TestIdentityAction_Action, gen_fuml_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_fuml_IntermediateActions_ValueSpecificationAction_Action, gen_fuml_IntermediateActions_WriteLinkAction_LinkAction, gen_fuml_IntermediateActions_LinkAction_Action, gen_fuml_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fuml_IntermediateActions_ReadLinkAction_LinkAction, gen_fuml_IntermediateActions_ReadSelfAction_Action, gen_fuml_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_LinkEndCreationData_LinkEndData, gen_fuml_IntermediateActions_LinkEndData_Element, gen_fuml_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_fuml_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_fuml_IntermediateActions_CreateObjectAction_Action, gen_fuml_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_fuml_IntermediateActions_DestroyObjectAction_Action, gen_fuml_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_fuml_IntermediateActions_ClearAssociationAction_Action, gen_fuml_CompleteActions_StartObjectBehaviorAction_CallAction, gen_fuml_CompleteActions_ReduceAction_Action, gen_fuml_CompleteActions_ReadExtentAction_Action, gen_fuml_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fuml_CompleteActions_StartClassifierBehaviorAction_Action, gen_fuml_CompleteActions_ReclassifyObjectAction_Action, gen_fuml_CompleteActions_AcceptEventAction_Action, gen_fuml_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_fuml_BasicActions_InputPin_Pin, gen_fuml_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_fuml_BasicActions_Pin_Kernel_MultiplicityElement, gen_fuml_BasicActions_CallAction_InvocationAction, gen_fuml_BasicActions_InvocationAction_Action, gen_fuml_BasicActions_SendSignalAction_InvocationAction, gen_fuml_BasicActions_Action_ExecutableNode, gen_fuml_BasicActions_OutputPin_Pin, gen_fuml_Kernel_StructuredValue_Value, gen_fuml_Kernel_UnlimitedNaturalValue_PrimitiveValue, gen_fuml_Kernel_PrimitiveValue_Value, gen_fuml_BasicActions_CallBehaviorAction_CallAction, gen_fuml_BasicActions_CallOperationAction_CallAction, gen_fuml_Kernel_ExtensionalValue_CompoundValue, gen_fuml_Kernel_CompoundValue_StructuredValue, gen_fuml_Kernel_Link_ExtensionalValue, gen_fuml_Kernel_IntegerValue_PrimitiveValue, gen_fuml_Kernel_EnumerationValue_Value, gen_fuml_Kernel_StringValue_PrimitiveValue, gen_fuml_Kernel_Reference_StructuredValue, gen_fuml_Kernel_Object_ExtensionalValue, gen_fuml_Kernel_DataValue_CompoundValue, gen_fuml_Kernel_BooleanValue_PrimitiveValue, gen_fuml_Kernel_Value_SemanticVisitor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)