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
Kernel_BehavioralFeature = Class(name="Kernel::BehavioralFeature")
Kernel_Parameter = Class(name="Kernel::Parameter")
BasicBehaviors_BehavioredClassifier = Class(name="BasicBehaviors::BehavioredClassifier")
fUML_BasicBehaviors_OpaqueBehavior = Class(name="fUML::BasicBehaviors::OpaqueBehavior")
Behavior = Class(name="Behavior")
fUML_BasicBehaviors_Behavior = Class(name="fUML::BasicBehaviors::Behavior", is_abstract=True)
Class_ = Class(name="Class")
fUML_Communications_Reception = Class(name="fUML::Communications::Reception")
BehavioralFeature = Class(name="BehavioralFeature")
fUML_Kernel_ValueSpecification = Class(name="fUML::Kernel::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
fUML_Kernel_TypedElement = Class(name="fUML::Kernel::TypedElement")
Kernel_Type = Class(name="Kernel::Type")
fUML_BasicBehaviors_BehavioredClassifier = Class(name="fUML::BasicBehaviors::BehavioredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
BasicBehaviors_Behavior = Class(name="BasicBehaviors::Behavior")
fUML_BasicBehaviors_FunctionBehavior = Class(name="fUML::BasicBehaviors::FunctionBehavior")
OpaqueBehavior = Class(name="OpaqueBehavior")
fUML_Communications_Trigger = Class(name="fUML::Communications::Trigger")
NamedElement = Class(name="NamedElement")
Communications_Event = Class(name="Communications::Event")
fUML_Communications_Event = Class(name="fUML::Communications::Event", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
fUML_Communications_Signal = Class(name="fUML::Communications::Signal")
Kernel_Property = Class(name="Kernel::Property")
fUML_Communications_SignalEvent = Class(name="fUML::Communications::SignalEvent")
MessageEvent = Class(name="MessageEvent")
Communications_Signal = Class(name="Communications::Signal")
fUML_Communications_MessageEvent = Class(name="fUML::Communications::MessageEvent", is_abstract=True)
Event = Class(name="Event")
Kernel_ElementImport = Class(name="Kernel::ElementImport")
Kernel_PackageImport = Class(name="Kernel::PackageImport")
Kernel_PackageableElement = Class(name="Kernel::PackageableElement")
fUML_Kernel_ElementImport = Class(name="fUML::Kernel::ElementImport")
fUML_Kernel_NamedElement = Class(name="fUML::Kernel::NamedElement", is_abstract=True)
Element = Class(name="Element")
Kernel_Namespace = Class(name="Kernel::Namespace")
fUML_Kernel_Element = Class(name="fUML::Kernel::Element", is_abstract=True)
Kernel_Element = Class(name="Kernel::Element")
Kernel_Comment = Class(name="Kernel::Comment")
fUML_Kernel_Comment = Class(name="fUML::Kernel::Comment")
fUML_Kernel_Namespace = Class(name="fUML::Kernel::Namespace", is_abstract=True)
Kernel_NamedElement = Class(name="Kernel::NamedElement")
fUML_Kernel_StructuralFeature = Class(name="fUML::Kernel::StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel::Feature")
Kernel_MultiplicityElement = Class(name="Kernel::MultiplicityElement")
Kernel_TypedElement = Class(name="Kernel::TypedElement")
fUML_Kernel_Feature = Class(name="fUML::Kernel::Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Kernel_Classifier = Class(name="Kernel::Classifier")
fUML_Kernel_PackageableElement = Class(name="fUML::Kernel::PackageableElement", is_abstract=True)
fUML_Kernel_PackageImport = Class(name="fUML::Kernel::PackageImport")
Kernel_Package = Class(name="Kernel::Package")
fUML_Kernel_Package = Class(name="fUML::Kernel::Package")
fUML_Kernel_Type = Class(name="fUML::Kernel::Type", is_abstract=True)
fUML_Kernel_RedefinableElement = Class(name="fUML::Kernel::RedefinableElement", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel::RedefinableElement")
fUML_Kernel_Classifier = Class(name="fUML::Kernel::Classifier", is_abstract=True)
Kernel_Generalization = Class(name="Kernel::Generalization")
Kernel_Association = Class(name="Kernel::Association")
Kernel_DataType = Class(name="Kernel::DataType")
Kernel_Class = Class(name="Kernel::Class")
fUML_Kernel_Generalization = Class(name="fUML::Kernel::Generalization")
fUML_Kernel_Property = Class(name="fUML::Kernel::Property")
StructuralFeature = Class(name="StructuralFeature")
fUML_Kernel_DataType = Class(name="fUML::Kernel::DataType")
fUML_Kernel_Association = Class(name="fUML::Kernel::Association")
fUML_Kernel_MultiplicityElement = Class(name="fUML::Kernel::MultiplicityElement")
fUML_Kernel_Parameter = Class(name="fUML::Kernel::Parameter")
Kernel_ValueSpecification = Class(name="Kernel::ValueSpecification")
fUML_Kernel_Operation = Class(name="fUML::Kernel::Operation")
fUML_Kernel_BehavioralFeature = Class(name="fUML::Kernel::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
fUML_Kernel_InstanceSpecification = Class(name="fUML::Kernel::InstanceSpecification")
Kernel_Slot = Class(name="Kernel::Slot")
fUML_Kernel_Slot = Class(name="fUML::Kernel::Slot")
Kernel_StructuralFeature = Class(name="Kernel::StructuralFeature")
Kernel_InstanceSpecification = Class(name="Kernel::InstanceSpecification")
fUML_Kernel_InstanceValue = Class(name="fUML::Kernel::InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
fUML_Kernel_LiteralBoolean = Class(name="fUML::Kernel::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
fUML_Kernel_LiteralSpecification = Class(name="fUML::Kernel::LiteralSpecification", is_abstract=True)
fUML_Kernel_LiteralInteger = Class(name="fUML::Kernel::LiteralInteger")
fUML_Kernel_LiteralNull = Class(name="fUML::Kernel::LiteralNull")
Kernel_Operation = Class(name="Kernel::Operation")
fUML_Kernel_PrimitiveType = Class(name="fUML::Kernel::PrimitiveType")
DataType = Class(name="DataType")
fUML_Kernel_Enumeration = Class(name="fUML::Kernel::Enumeration")
Kernel_EnumerationLiteral = Class(name="Kernel::EnumerationLiteral")
fUML_Kernel_EnumerationLiteral = Class(name="fUML::Kernel::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
Kernel_Enumeration = Class(name="Kernel::Enumeration")
fUML_Kernel_Class = Class(name="fUML::Kernel::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
Communications_Reception = Class(name="Communications::Reception")
fUML_Kernel_LiteralString = Class(name="fUML::Kernel::LiteralString")
fUML_Kernel_LiteralUnlimitedNatural = Class(name="fUML::Kernel::LiteralUnlimitedNatural")
fUML_IntermediateActivities_ObjectFlow = Class(name="fUML::IntermediateActivities::ObjectFlow")
ActivityEdge = Class(name="ActivityEdge")
fUML_IntermediateActivities_ActivityEdge = Class(name="fUML::IntermediateActivities::ActivityEdge", is_abstract=True)
IntermediateActivities_Activity = Class(name="IntermediateActivities::Activity")
IntermediateActivities_ActivityNode = Class(name="IntermediateActivities::ActivityNode")
CompleteStructuredActivities_StructuredActivityNode = Class(name="CompleteStructuredActivities::StructuredActivityNode")
fUML_IntermediateActivities_Activity = Class(name="fUML::IntermediateActivities::Activity")
fUML_IntermediateActivities_ActivityNode = Class(name="fUML::IntermediateActivities::ActivityNode", is_abstract=True)
fUML_IntermediateActivities_ObjectNode = Class(name="fUML::IntermediateActivities::ObjectNode", is_abstract=True)
fUML_IntermediateActivities_MergeNode = Class(name="fUML::IntermediateActivities::MergeNode")
ControlNode = Class(name="ControlNode")
fUML_IntermediateActivities_ControlNode = Class(name="fUML::IntermediateActivities::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
fUML_IntermediateActivities_JoinNode = Class(name="fUML::IntermediateActivities::JoinNode")
fUML_IntermediateActivities_InitialNode = Class(name="fUML::IntermediateActivities::InitialNode")
fUML_IntermediateActivities_FinalNode = Class(name="fUML::IntermediateActivities::FinalNode", is_abstract=True)
fUML_IntermediateActivities_ForkNode = Class(name="fUML::IntermediateActivities::ForkNode")
fUML_IntermediateActivities_ControlFlow = Class(name="fUML::IntermediateActivities::ControlFlow")
IntermediateActivities_ActivityEdge = Class(name="IntermediateActivities::ActivityEdge")
fUML_IntermediateActivities_ActivityFinalNode = Class(name="fUML::IntermediateActivities::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
fUML_IntermediateActivities_ActivityParameterNode = Class(name="fUML::IntermediateActivities::ActivityParameterNode")
ObjectNode = Class(name="ObjectNode")
fUML_CompleteStructuredActivities_LoopNode = Class(name="fUML::CompleteStructuredActivities::LoopNode")
StructuredActivityNode = Class(name="StructuredActivityNode")
BasicActions_OutputPin = Class(name="BasicActions::OutputPin")
CompleteStructuredActivities_ExecutableNode = Class(name="CompleteStructuredActivities::ExecutableNode")
BasicActions_InputPin = Class(name="BasicActions::InputPin")
fUML_CompleteStructuredActivities_ExecutableNode = Class(name="fUML::CompleteStructuredActivities::ExecutableNode", is_abstract=True)
fUML_IntermediateActivities_DecisionNode = Class(name="fUML::IntermediateActivities::DecisionNode")
fUML_CompleteStructuredActivities_Clause = Class(name="fUML::CompleteStructuredActivities::Clause")
IntermediateActivities_ObjectFlow = Class(name="IntermediateActivities::ObjectFlow")
CompleteStructuredActivities_Clause = Class(name="CompleteStructuredActivities::Clause")
fUML_CompleteStructuredActivities_ConditionalNode = Class(name="fUML::CompleteStructuredActivities::ConditionalNode")
fUML_CompleteStructuredActivities_StructuredActivityNode = Class(name="fUML::CompleteStructuredActivities::StructuredActivityNode")
Action = Class(name="Action")
fUML_ExtraStructuredActivities_ExpansionNode = Class(name="fUML::ExtraStructuredActivities::ExpansionNode")
ExtraStructuredActivities_ExpansionRegion = Class(name="ExtraStructuredActivities::ExpansionRegion")
fUML_ExtraStructuredActivities_ExpansionRegion = Class(name="fUML::ExtraStructuredActivities::ExpansionRegion")
ExtraStructuredActivities_ExpansionNode = Class(name="ExtraStructuredActivities::ExpansionNode")
fUML_IntermediateActions_StructuralFeatureAction = Class(name="fUML::IntermediateActions::StructuralFeatureAction", is_abstract=True)
fUML_IntermediateActions_ValueSpecificationAction = Class(name="fUML::IntermediateActions::ValueSpecificationAction")
fUML_IntermediateActions_WriteLinkAction = Class(name="fUML::IntermediateActions::WriteLinkAction", is_abstract=True)
LinkAction = Class(name="LinkAction")
fUML_IntermediateActions_LinkAction = Class(name="fUML::IntermediateActions::LinkAction", is_abstract=True)
IntermediateActions_LinkEndData = Class(name="IntermediateActions::LinkEndData")
fUML_IntermediateActions_LinkEndData = Class(name="fUML::IntermediateActions::LinkEndData")
fUML_IntermediateActions_TestIdentityAction = Class(name="fUML::IntermediateActions::TestIdentityAction")
fUML_IntermediateActions_RemoveStructuralFeatureValueAction = Class(name="fUML::IntermediateActions::RemoveStructuralFeatureValueAction")
WriteStructuralFeatureAction = Class(name="WriteStructuralFeatureAction")
fUML_IntermediateActions_ReadLinkAction = Class(name="fUML::IntermediateActions::ReadLinkAction")
fUML_IntermediateActions_ReadSelfAction = Class(name="fUML::IntermediateActions::ReadSelfAction")
fUML_IntermediateActions_ReadStructuralFeatureAction = Class(name="fUML::IntermediateActions::ReadStructuralFeatureAction")
fUML_IntermediateActions_LinkEndCreationData = Class(name="fUML::IntermediateActions::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
fUML_IntermediateActions_LinkEndDestructionData = Class(name="fUML::IntermediateActions::LinkEndDestructionData")
fUML_IntermediateActions_ClearAssociationAction = Class(name="fUML::IntermediateActions::ClearAssociationAction")
fUML_IntermediateActions_WriteStructuralFeatureAction = Class(name="fUML::IntermediateActions::WriteStructuralFeatureAction", is_abstract=True)
StructuralFeatureAction = Class(name="StructuralFeatureAction")
fUML_IntermediateActions_ClearStructuralFeatureAction = Class(name="fUML::IntermediateActions::ClearStructuralFeatureAction")
fUML_IntermediateActions_CreateLinkAction = Class(name="fUML::IntermediateActions::CreateLinkAction")
WriteLinkAction = Class(name="WriteLinkAction")
fUML_IntermediateActions_CreateObjectAction = Class(name="fUML::IntermediateActions::CreateObjectAction")
fUML_IntermediateActions_AddStructuralFeatureValueAction = Class(name="fUML::IntermediateActions::AddStructuralFeatureValueAction")
fUML_IntermediateActions_DestroyLinkAction = Class(name="fUML::IntermediateActions::DestroyLinkAction")
fUML_IntermediateActions_DestroyObjectAction = Class(name="fUML::IntermediateActions::DestroyObjectAction")
fUML_CompleteActions_ReadExtentAction = Class(name="fUML::CompleteActions::ReadExtentAction")
fUML_CompleteActions_StartClassifierBehaviorAction = Class(name="fUML::CompleteActions::StartClassifierBehaviorAction")
fUML_CompleteActions_StartObjectBehaviorAction = Class(name="fUML::CompleteActions::StartObjectBehaviorAction")
CallAction = Class(name="CallAction")
fUML_CompleteActions_ReduceAction = Class(name="fUML::CompleteActions::ReduceAction")
fUML_CompleteActions_AcceptEventAction = Class(name="fUML::CompleteActions::AcceptEventAction")
Communications_Trigger = Class(name="Communications::Trigger")
fUML_CompleteActions_ReadIsClassifiedObjectAction = Class(name="fUML::CompleteActions::ReadIsClassifiedObjectAction")
fUML_CompleteActions_ReclassifyObjectAction = Class(name="fUML::CompleteActions::ReclassifyObjectAction")
fUML_BasicActions_InvocationAction = Class(name="fUML::BasicActions::InvocationAction", is_abstract=True)
fUML_BasicActions_SendSignalAction = Class(name="fUML::BasicActions::SendSignalAction")
fUML_BasicActions_CallBehaviorAction = Class(name="fUML::BasicActions::CallBehaviorAction")
fUML_BasicActions_Action = Class(name="fUML::BasicActions::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
fUML_BasicActions_InputPin = Class(name="fUML::BasicActions::InputPin")
Pin = Class(name="Pin")
fUML_BasicActions_Pin = Class(name="fUML::BasicActions::Pin", is_abstract=True)
IntermediateActivities_ObjectNode = Class(name="IntermediateActivities::ObjectNode")
fUML_BasicActions_CallAction = Class(name="fUML::BasicActions::CallAction", is_abstract=True)
InvocationAction = Class(name="InvocationAction")
fUML_Kernel_StructuredValue = Class(name="fUML::Kernel::StructuredValue", is_abstract=True)
Value = Class(name="Value")
fUML_Kernel_FeatureValue = Class(name="fUML::Kernel::FeatureValue")
Kernel_Value = Class(name="Kernel::Value")
fUML_BasicActions_CallOperationAction = Class(name="fUML::BasicActions::CallOperationAction")
fUML_BasicActions_OutputPin = Class(name="fUML::BasicActions::OutputPin")
fUML_Kernel_Reference = Class(name="fUML::Kernel::Reference")
StructuredValue = Class(name="StructuredValue")
Kernel_Object = Class(name="Kernel::Object")
fUML_Kernel_Object = Class(name="fUML::Kernel::Object")
ExtensionalValue = Class(name="ExtensionalValue")
fUML_Kernel_UnlimitedNaturalValue = Class(name="fUML::Kernel::UnlimitedNaturalValue")
PrimitiveValue = Class(name="PrimitiveValue")
fUML_Kernel_PrimitiveValue = Class(name="fUML::Kernel::PrimitiveValue", is_abstract=True)
Kernel_PrimitiveType = Class(name="Kernel::PrimitiveType")
fUML_Kernel_StringValue = Class(name="fUML::Kernel::StringValue")
fUML_Kernel_IntegerValue = Class(name="fUML::Kernel::IntegerValue")
fUML_Kernel_EnumerationValue = Class(name="fUML::Kernel::EnumerationValue")
fUML_Kernel_ExtensionalValue = Class(name="fUML::Kernel::ExtensionalValue", is_abstract=True)
CompoundValue = Class(name="CompoundValue")
fUML_Kernel_CompoundValue = Class(name="fUML::Kernel::CompoundValue", is_abstract=True)
Kernel_FeatureValue = Class(name="Kernel::FeatureValue")
fUML_Kernel_Link = Class(name="fUML::Kernel::Link")
fUML_Kernel_Value = Class(name="fUML::Kernel::Value", is_abstract=True)
SemanticVisitor = Class(name="SemanticVisitor")
fUML_LociL1_SemanticVisitor = Class(name="fUML::LociL1::SemanticVisitor", is_abstract=True)
fUML_Kernel_DataValue = Class(name="fUML::Kernel::DataValue")
fUML_Kernel_BooleanValue = Class(name="fUML::Kernel::BooleanValue")

# Kernel_BehavioralFeature class attributes and methods

# Kernel_Parameter class attributes and methods

# BasicBehaviors_BehavioredClassifier class attributes and methods

# fUML_BasicBehaviors_OpaqueBehavior class attributes and methods
fUML_BasicBehaviors_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
fUML_BasicBehaviors_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
fUML_BasicBehaviors_OpaqueBehavior.attributes={fUML_BasicBehaviors_OpaqueBehavior_language, fUML_BasicBehaviors_OpaqueBehavior_body}

# Behavior class attributes and methods

# fUML_BasicBehaviors_Behavior class attributes and methods
fUML_BasicBehaviors_Behavior_reentrant: Property = Property(name="reentrant", type=BooleanType)
fUML_BasicBehaviors_Behavior.attributes={fUML_BasicBehaviors_Behavior_reentrant}

# Class class attributes and methods

# fUML_Communications_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# fUML_Kernel_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# fUML_Kernel_TypedElement class attributes and methods

# Kernel_Type class attributes and methods

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

# Kernel_ElementImport class attributes and methods

# Kernel_PackageImport class attributes and methods

# Kernel_PackageableElement class attributes and methods

# fUML_Kernel_ElementImport class attributes and methods
fUML_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
fUML_Kernel_ElementImport.attributes={fUML_Kernel_ElementImport_visibility, fUML_Kernel_ElementImport_alias}

# fUML_Kernel_NamedElement class attributes and methods
fUML_Kernel_NamedElement_name: Property = Property(name="name", type=StringType)
fUML_Kernel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
fUML_Kernel_NamedElement.attributes={fUML_Kernel_NamedElement_qualifiedName, fUML_Kernel_NamedElement_visibility, fUML_Kernel_NamedElement_name}

# Element class attributes and methods

# Kernel_Namespace class attributes and methods

# fUML_Kernel_Element class attributes and methods

# Kernel_Element class attributes and methods

# Kernel_Comment class attributes and methods

# fUML_Kernel_Comment class attributes and methods
fUML_Kernel_Comment_body: Property = Property(name="body", type=StringType)
fUML_Kernel_Comment.attributes={fUML_Kernel_Comment_body}

# fUML_Kernel_Namespace class attributes and methods

# Kernel_NamedElement class attributes and methods

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

# fUML_Kernel_PackageableElement class attributes and methods

# fUML_Kernel_PackageImport class attributes and methods
fUML_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
fUML_Kernel_PackageImport.attributes={fUML_Kernel_PackageImport_visibility}

# Kernel_Package class attributes and methods

# fUML_Kernel_Package class attributes and methods

# fUML_Kernel_Type class attributes and methods

# fUML_Kernel_RedefinableElement class attributes and methods
fUML_Kernel_RedefinableElement_leaf: Property = Property(name="leaf", type=BooleanType)
fUML_Kernel_RedefinableElement.attributes={fUML_Kernel_RedefinableElement_leaf}

# Kernel_RedefinableElement class attributes and methods

# fUML_Kernel_Classifier class attributes and methods
fUML_Kernel_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
fUML_Kernel_Classifier_finalSpecialization: Property = Property(name="finalSpecialization", type=BooleanType)
fUML_Kernel_Classifier.attributes={fUML_Kernel_Classifier_abstract, fUML_Kernel_Classifier_finalSpecialization}

# Kernel_Generalization class attributes and methods

# Kernel_Association class attributes and methods

# Kernel_DataType class attributes and methods

# Kernel_Class class attributes and methods

# fUML_Kernel_Generalization class attributes and methods
fUML_Kernel_Generalization_substitutable: Property = Property(name="substitutable", type=BooleanType)
fUML_Kernel_Generalization.attributes={fUML_Kernel_Generalization_substitutable}

# fUML_Kernel_Property class attributes and methods
fUML_Kernel_Property_derived: Property = Property(name="derived", type=BooleanType)
fUML_Kernel_Property_derivedUnion: Property = Property(name="derivedUnion", type=BooleanType)
fUML_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
fUML_Kernel_Property_composite: Property = Property(name="composite", type=BooleanType)
fUML_Kernel_Property.attributes={fUML_Kernel_Property_composite, fUML_Kernel_Property_derivedUnion, fUML_Kernel_Property_derived, fUML_Kernel_Property_aggregation}

# StructuralFeature class attributes and methods

# fUML_Kernel_DataType class attributes and methods

# fUML_Kernel_Association class attributes and methods
fUML_Kernel_Association_derived: Property = Property(name="derived", type=BooleanType)
fUML_Kernel_Association.attributes={fUML_Kernel_Association_derived}

# fUML_Kernel_MultiplicityElement class attributes and methods
fUML_Kernel_MultiplicityElement_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_Kernel_MultiplicityElement_unique: Property = Property(name="unique", type=BooleanType)
fUML_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
fUML_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
fUML_Kernel_MultiplicityElement.attributes={fUML_Kernel_MultiplicityElement_lower, fUML_Kernel_MultiplicityElement_ordered, fUML_Kernel_MultiplicityElement_unique, fUML_Kernel_MultiplicityElement_upper}

# fUML_Kernel_Parameter class attributes and methods
fUML_Kernel_Parameter_direction: Property = Property(name="direction", type=StringType)
fUML_Kernel_Parameter.attributes={fUML_Kernel_Parameter_direction}

# Kernel_ValueSpecification class attributes and methods

# fUML_Kernel_Operation class attributes and methods
fUML_Kernel_Operation_query: Property = Property(name="query", type=BooleanType)
fUML_Kernel_Operation_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_Kernel_Operation_unique: Property = Property(name="unique", type=BooleanType)
fUML_Kernel_Operation_lower: Property = Property(name="lower", type=IntegerType)
fUML_Kernel_Operation_upper: Property = Property(name="upper", type=IntegerType)
fUML_Kernel_Operation.attributes={fUML_Kernel_Operation_unique, fUML_Kernel_Operation_query, fUML_Kernel_Operation_ordered, fUML_Kernel_Operation_upper, fUML_Kernel_Operation_lower}

# fUML_Kernel_BehavioralFeature class attributes and methods
fUML_Kernel_BehavioralFeature_abstract: Property = Property(name="abstract", type=BooleanType)
fUML_Kernel_BehavioralFeature_concurrency: Property = Property(name="concurrency", type=StringType)
fUML_Kernel_BehavioralFeature.attributes={fUML_Kernel_BehavioralFeature_concurrency, fUML_Kernel_BehavioralFeature_abstract}

# Feature class attributes and methods

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

# Kernel_Operation class attributes and methods

# fUML_Kernel_PrimitiveType class attributes and methods

# DataType class attributes and methods

# fUML_Kernel_Enumeration class attributes and methods

# Kernel_EnumerationLiteral class attributes and methods

# fUML_Kernel_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Kernel_Enumeration class attributes and methods

# fUML_Kernel_Class class attributes and methods
fUML_Kernel_Class_active: Property = Property(name="active", type=BooleanType)
fUML_Kernel_Class.attributes={fUML_Kernel_Class_active}

# BehavioredClassifier class attributes and methods

# Communications_Reception class attributes and methods

# fUML_Kernel_LiteralString class attributes and methods
fUML_Kernel_LiteralString_value: Property = Property(name="value", type=StringType)
fUML_Kernel_LiteralString.attributes={fUML_Kernel_LiteralString_value}

# fUML_Kernel_LiteralUnlimitedNatural class attributes and methods
fUML_Kernel_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_LiteralUnlimitedNatural.attributes={fUML_Kernel_LiteralUnlimitedNatural_value}

# fUML_IntermediateActivities_ObjectFlow class attributes and methods

# ActivityEdge class attributes and methods

# fUML_IntermediateActivities_ActivityEdge class attributes and methods

# IntermediateActivities_Activity class attributes and methods

# IntermediateActivities_ActivityNode class attributes and methods

# CompleteStructuredActivities_StructuredActivityNode class attributes and methods

# fUML_IntermediateActivities_Activity class attributes and methods
fUML_IntermediateActivities_Activity_readOnly: Property = Property(name="readOnly", type=BooleanType)
fUML_IntermediateActivities_Activity.attributes={fUML_IntermediateActivities_Activity_readOnly}

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

# IntermediateActivities_ActivityEdge class attributes and methods

# fUML_IntermediateActivities_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

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

# fUML_IntermediateActivities_DecisionNode class attributes and methods

# fUML_CompleteStructuredActivities_Clause class attributes and methods

# IntermediateActivities_ObjectFlow class attributes and methods

# CompleteStructuredActivities_Clause class attributes and methods

# fUML_CompleteStructuredActivities_ConditionalNode class attributes and methods
fUML_CompleteStructuredActivities_ConditionalNode_determinate: Property = Property(name="determinate", type=BooleanType)
fUML_CompleteStructuredActivities_ConditionalNode_assured: Property = Property(name="assured", type=BooleanType)
fUML_CompleteStructuredActivities_ConditionalNode.attributes={fUML_CompleteStructuredActivities_ConditionalNode_determinate, fUML_CompleteStructuredActivities_ConditionalNode_assured}

# fUML_CompleteStructuredActivities_StructuredActivityNode class attributes and methods
fUML_CompleteStructuredActivities_StructuredActivityNode_mustIsolate: Property = Property(name="mustIsolate", type=BooleanType)
fUML_CompleteStructuredActivities_StructuredActivityNode.attributes={fUML_CompleteStructuredActivities_StructuredActivityNode_mustIsolate}

# Action class attributes and methods

# fUML_ExtraStructuredActivities_ExpansionNode class attributes and methods

# ExtraStructuredActivities_ExpansionRegion class attributes and methods

# fUML_ExtraStructuredActivities_ExpansionRegion class attributes and methods
fUML_ExtraStructuredActivities_ExpansionRegion_mode: Property = Property(name="mode", type=StringType)
fUML_ExtraStructuredActivities_ExpansionRegion.attributes={fUML_ExtraStructuredActivities_ExpansionRegion_mode}

# ExtraStructuredActivities_ExpansionNode class attributes and methods

# fUML_IntermediateActions_StructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_ValueSpecificationAction class attributes and methods

# fUML_IntermediateActions_WriteLinkAction class attributes and methods

# LinkAction class attributes and methods

# fUML_IntermediateActions_LinkAction class attributes and methods

# IntermediateActions_LinkEndData class attributes and methods

# fUML_IntermediateActions_LinkEndData class attributes and methods

# fUML_IntermediateActions_TestIdentityAction class attributes and methods

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

# fUML_IntermediateActions_WriteStructuralFeatureAction class attributes and methods

# StructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_ClearStructuralFeatureAction class attributes and methods

# fUML_IntermediateActions_CreateLinkAction class attributes and methods

# WriteLinkAction class attributes and methods

# fUML_IntermediateActions_CreateObjectAction class attributes and methods

# fUML_IntermediateActions_AddStructuralFeatureValueAction class attributes and methods
fUML_IntermediateActions_AddStructuralFeatureValueAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fUML_IntermediateActions_AddStructuralFeatureValueAction.attributes={fUML_IntermediateActions_AddStructuralFeatureValueAction_replaceAll}

# fUML_IntermediateActions_DestroyLinkAction class attributes and methods

# fUML_IntermediateActions_DestroyObjectAction class attributes and methods
fUML_IntermediateActions_DestroyObjectAction_destroyLinks: Property = Property(name="destroyLinks", type=BooleanType)
fUML_IntermediateActions_DestroyObjectAction_destroyOwnedObjects: Property = Property(name="destroyOwnedObjects", type=BooleanType)
fUML_IntermediateActions_DestroyObjectAction.attributes={fUML_IntermediateActions_DestroyObjectAction_destroyLinks, fUML_IntermediateActions_DestroyObjectAction_destroyOwnedObjects}

# fUML_CompleteActions_ReadExtentAction class attributes and methods

# fUML_CompleteActions_StartClassifierBehaviorAction class attributes and methods

# fUML_CompleteActions_StartObjectBehaviorAction class attributes and methods

# CallAction class attributes and methods

# fUML_CompleteActions_ReduceAction class attributes and methods
fUML_CompleteActions_ReduceAction_ordered: Property = Property(name="ordered", type=BooleanType)
fUML_CompleteActions_ReduceAction.attributes={fUML_CompleteActions_ReduceAction_ordered}

# fUML_CompleteActions_AcceptEventAction class attributes and methods
fUML_CompleteActions_AcceptEventAction_unmarshall: Property = Property(name="unmarshall", type=BooleanType)
fUML_CompleteActions_AcceptEventAction.attributes={fUML_CompleteActions_AcceptEventAction_unmarshall}

# Communications_Trigger class attributes and methods

# fUML_CompleteActions_ReadIsClassifiedObjectAction class attributes and methods
fUML_CompleteActions_ReadIsClassifiedObjectAction_direct: Property = Property(name="direct", type=BooleanType)
fUML_CompleteActions_ReadIsClassifiedObjectAction.attributes={fUML_CompleteActions_ReadIsClassifiedObjectAction_direct}

# fUML_CompleteActions_ReclassifyObjectAction class attributes and methods
fUML_CompleteActions_ReclassifyObjectAction_replaceAll: Property = Property(name="replaceAll", type=BooleanType)
fUML_CompleteActions_ReclassifyObjectAction.attributes={fUML_CompleteActions_ReclassifyObjectAction_replaceAll}

# fUML_BasicActions_InvocationAction class attributes and methods

# fUML_BasicActions_SendSignalAction class attributes and methods

# fUML_BasicActions_CallBehaviorAction class attributes and methods

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

# fUML_Kernel_StructuredValue class attributes and methods

# Value class attributes and methods

# fUML_Kernel_FeatureValue class attributes and methods
fUML_Kernel_FeatureValue_position: Property = Property(name="position", type=IntegerType)
fUML_Kernel_FeatureValue.attributes={fUML_Kernel_FeatureValue_position}

# Kernel_Value class attributes and methods

# fUML_BasicActions_CallOperationAction class attributes and methods

# fUML_BasicActions_OutputPin class attributes and methods

# fUML_Kernel_Reference class attributes and methods

# StructuredValue class attributes and methods

# Kernel_Object class attributes and methods

# fUML_Kernel_Object class attributes and methods

# ExtensionalValue class attributes and methods

# fUML_Kernel_UnlimitedNaturalValue class attributes and methods
fUML_Kernel_UnlimitedNaturalValue_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_UnlimitedNaturalValue.attributes={fUML_Kernel_UnlimitedNaturalValue_value}

# PrimitiveValue class attributes and methods

# fUML_Kernel_PrimitiveValue class attributes and methods

# Kernel_PrimitiveType class attributes and methods

# fUML_Kernel_StringValue class attributes and methods
fUML_Kernel_StringValue_value: Property = Property(name="value", type=StringType)
fUML_Kernel_StringValue.attributes={fUML_Kernel_StringValue_value}

# fUML_Kernel_IntegerValue class attributes and methods
fUML_Kernel_IntegerValue_value: Property = Property(name="value", type=IntegerType)
fUML_Kernel_IntegerValue.attributes={fUML_Kernel_IntegerValue_value}

# fUML_Kernel_EnumerationValue class attributes and methods

# fUML_Kernel_ExtensionalValue class attributes and methods

# CompoundValue class attributes and methods

# fUML_Kernel_CompoundValue class attributes and methods

# Kernel_FeatureValue class attributes and methods

# fUML_Kernel_Link class attributes and methods

# fUML_Kernel_Value class attributes and methods

# SemanticVisitor class attributes and methods

# fUML_LociL1_SemanticVisitor class attributes and methods

# fUML_Kernel_DataValue class attributes and methods

# fUML_Kernel_BooleanValue class attributes and methods
fUML_Kernel_BooleanValue_value: Property = Property(name="value", type=BooleanType)
fUML_Kernel_BooleanValue.attributes={fUML_Kernel_BooleanValue_value}

# Relationships
specification0: BinaryAssociation = BinaryAssociation(
    name="specification0",
    ends={
        Property(name="Syntax", type=fUML_BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes", type=Kernel_BehavioralFeature, multiplicity=Multiplicity(0, 1))
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
elementImport26: BinaryAssociation = BinaryAssociation(
    name="elementImport26",
    ends={
        Property(name="Syntax28", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes27", type=Kernel_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport29: BinaryAssociation = BinaryAssociation(
    name="packageImport29",
    ends={
        Property(name="Syntax31", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes30", type=Kernel_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember32: BinaryAssociation = BinaryAssociation(
    name="importedMember32",
    ends={
        Property(name="Kernel_PackageableElement", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Namespace33", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember34: BinaryAssociation = BinaryAssociation(
    name="ownedMember34",
    ends={
        Property(name="Syntax36", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes35", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="Syntax16", type=fUML_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes15", type=Kernel_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement17: BinaryAssociation = BinaryAssociation(
    name="ownedElement17",
    ends={
        Property(name="Syntax19", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes18", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner20: BinaryAssociation = BinaryAssociation(
    name="owner20",
    ends={
        Property(name="Syntax22", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes21", type=Kernel_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment23: BinaryAssociation = BinaryAssociation(
    name="ownedComment23",
    ends={
        Property(name="Kernel_Comment", type=fUML_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Element", type=Kernel_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement24: BinaryAssociation = BinaryAssociation(
    name="annotatedElement24",
    ends={
        Property(name="Kernel_Element", type=fUML_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Comment", type=Kernel_Element, multiplicity=Multiplicity(0, 9999))
    }
)
member25: BinaryAssociation = BinaryAssociation(
    name="member25",
    ends={
        Property(name="Kernel_NamedElement", type=fUML_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Namespace", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier60: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier60",
    ends={
        Property(name="Syntax62", type=fUML_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes61", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement37: BinaryAssociation = BinaryAssociation(
    name="importedElement37",
    ends={
        Property(name="Kernel_PackageableElement38", type=fUML_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_ElementImport", type=Kernel_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace39: BinaryAssociation = BinaryAssociation(
    name="importingNamespace39",
    ends={
        Property(name="Syntax41", type=fUML_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes40", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage42: BinaryAssociation = BinaryAssociation(
    name="importedPackage42",
    ends={
        Property(name="Kernel_Package", type=fUML_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_PackageImport", type=Kernel_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace43: BinaryAssociation = BinaryAssociation(
    name="importingNamespace43",
    ends={
        Property(name="Syntax45", type=fUML_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes44", type=Kernel_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement46: BinaryAssociation = BinaryAssociation(
    name="packagedElement46",
    ends={
        Property(name="Kernel_PackageableElement47", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Package", type=Kernel_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType48: BinaryAssociation = BinaryAssociation(
    name="ownedType48",
    ends={
        Property(name="Syntax50", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes49", type=Kernel_Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage51: BinaryAssociation = BinaryAssociation(
    name="nestedPackage51",
    ends={
        Property(name="Syntax53", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes52", type=Kernel_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage54: BinaryAssociation = BinaryAssociation(
    name="nestingPackage54",
    ends={
        Property(name="Syntax56", type=fUML_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes55", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
package57: BinaryAssociation = BinaryAssociation(
    name="package57",
    ends={
        Property(name="Syntax59", type=fUML_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes58", type=Kernel_Package, multiplicity=Multiplicity(0, 1))
    }
)
feature69: BinaryAssociation = BinaryAssociation(
    name="feature69",
    ends={
        Property(name="Syntax71", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes70", type=Kernel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember72: BinaryAssociation = BinaryAssociation(
    name="inheritedMember72",
    ends={
        Property(name="Kernel_NamedElement73", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier", type=Kernel_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute74: BinaryAssociation = BinaryAssociation(
    name="attribute74",
    ends={
        Property(name="Kernel_Property76", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier75", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement63: BinaryAssociation = BinaryAssociation(
    name="redefinedElement63",
    ends={
        Property(name="Kernel_RedefinableElement", type=fUML_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_RedefinableElement", type=Kernel_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext64: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext64",
    ends={
        Property(name="Kernel_Classifier", type=fUML_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_RedefinableElement65", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization66: BinaryAssociation = BinaryAssociation(
    name="generalization66",
    ends={
        Property(name="Syntax68", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes67", type=Kernel_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningAssociation85: BinaryAssociation = BinaryAssociation(
    name="owningAssociation85",
    ends={
        Property(name="Syntax87", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes86", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
association88: BinaryAssociation = BinaryAssociation(
    name="association88",
    ends={
        Property(name="Syntax90", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes89", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
datatype91: BinaryAssociation = BinaryAssociation(
    name="datatype91",
    ends={
        Property(name="Syntax93", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes92", type=Kernel_DataType, multiplicity=Multiplicity(0, 1))
    }
)
class94: BinaryAssociation = BinaryAssociation(
    name="class94",
    ends={
        Property(name="Syntax96", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes95", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
general77: BinaryAssociation = BinaryAssociation(
    name="general77",
    ends={
        Property(name="Kernel_Classifier79", type=fUML_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Classifier78", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general80: BinaryAssociation = BinaryAssociation(
    name="general80",
    ends={
        Property(name="Kernel_Classifier81", type=fUML_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Generalization", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific82: BinaryAssociation = BinaryAssociation(
    name="specific82",
    ends={
        Property(name="Syntax84", type=fUML_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes83", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
memberEnd101: BinaryAssociation = BinaryAssociation(
    name="memberEnd101",
    ends={
        Property(name="Syntax103", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes102", type=Kernel_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableOwnedEnd104: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd104",
    ends={
        Property(name="Kernel_Property106", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Association105", type=Kernel_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd107: BinaryAssociation = BinaryAssociation(
    name="ownedEnd107",
    ends={
        Property(name="Syntax109", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes108", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite97: BinaryAssociation = BinaryAssociation(
    name="opposite97",
    ends={
        Property(name="Kernel_Property98", type=fUML_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Property", type=Kernel_Property, multiplicity=Multiplicity(0, 1))
    }
)
endType99: BinaryAssociation = BinaryAssociation(
    name="endType99",
    ends={
        Property(name="Kernel_Type100", type=fUML_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Association", type=Kernel_Type, multiplicity=Multiplicity(1, 9999))
    }
)
ownedAttribute110: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute110",
    ends={
        Property(name="Syntax112", type=fUML_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes111", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method119: BinaryAssociation = BinaryAssociation(
    name="method119",
    ends={
        Property(name="Syntax120", type=fUML_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonBehaviors", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
upperValue113: BinaryAssociation = BinaryAssociation(
    name="upperValue113",
    ends={
        Property(name="Kernel_ValueSpecification", type=fUML_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_MultiplicityElement", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue114: BinaryAssociation = BinaryAssociation(
    name="lowerValue114",
    ends={
        Property(name="Kernel_ValueSpecification116", type=fUML_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_MultiplicityElement115", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter117: BinaryAssociation = BinaryAssociation(
    name="ownedParameter117",
    ends={
        Property(name="Kernel_Parameter118", type=fUML_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_BehavioralFeature", type=Kernel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier128: BinaryAssociation = BinaryAssociation(
    name="classifier128",
    ends={
        Property(name="Kernel_Classifier129", type=fUML_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_InstanceSpecification", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot130: BinaryAssociation = BinaryAssociation(
    name="slot130",
    ends={
        Property(name="Syntax132", type=fUML_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes131", type=Kernel_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature133: BinaryAssociation = BinaryAssociation(
    name="definingFeature133",
    ends={
        Property(name="Kernel_StructuralFeature", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Slot", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value134: BinaryAssociation = BinaryAssociation(
    name="value134",
    ends={
        Property(name="Kernel_ValueSpecification136", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Slot135", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance137: BinaryAssociation = BinaryAssociation(
    name="owningInstance137",
    ends={
        Property(name="Syntax139", type=fUML_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes138", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance140: BinaryAssociation = BinaryAssociation(
    name="instance140",
    ends={
        Property(name="Kernel_InstanceSpecification", type=fUML_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_InstanceValue", type=Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
class121: BinaryAssociation = BinaryAssociation(
    name="class121",
    ends={
        Property(name="Syntax123", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes122", type=Kernel_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation124: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation124",
    ends={
        Property(name="Kernel_Operation", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Operation", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type125: BinaryAssociation = BinaryAssociation(
    name="type125",
    ends={
        Property(name="Kernel_Type127", type=fUML_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Operation126", type=Kernel_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral141: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral141",
    ends={
        Property(name="Syntax143", type=fUML_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes142", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration144: BinaryAssociation = BinaryAssociation(
    name="enumeration144",
    ends={
        Property(name="Syntax146", type=fUML_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes145", type=Kernel_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute147: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute147",
    ends={
        Property(name="Syntax149", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes148", type=Kernel_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation150: BinaryAssociation = BinaryAssociation(
    name="ownedOperation150",
    ends={
        Property(name="Syntax152", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes151", type=Kernel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass153: BinaryAssociation = BinaryAssociation(
    name="superClass153",
    ends={
        Property(name="Kernel_Class", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception154: BinaryAssociation = BinaryAssociation(
    name="ownedReception154",
    ends={
        Property(name="Communications_Reception", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class155", type=Communications_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity159: BinaryAssociation = BinaryAssociation(
    name="activity159",
    ends={
        Property(name="Syntax160", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
source161: BinaryAssociation = BinaryAssociation(
    name="source161",
    ends={
        Property(name="Syntax163", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities162", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target164: BinaryAssociation = BinaryAssociation(
    name="target164",
    ends={
        Property(name="Syntax166", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities165", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
inStructuredNode167: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode167",
    ends={
        Property(name="Syntax169", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities168", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
guard170: BinaryAssociation = BinaryAssociation(
    name="guard170",
    ends={
        Property(name="Kernel_ValueSpecification171", type=fUML_IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_ActivityEdge", type=Kernel_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node172: BinaryAssociation = BinaryAssociation(
    name="node172",
    ends={
        Property(name="Syntax174", type=fUML_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities173", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier156: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier156",
    ends={
        Property(name="Kernel_Classifier158", type=fUML_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Class157", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inStructuredNode178: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode178",
    ends={
        Property(name="Syntax180", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities179", type=CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
activity181: BinaryAssociation = BinaryAssociation(
    name="activity181",
    ends={
        Property(name="Syntax183", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities182", type=IntermediateActivities_Activity, multiplicity=Multiplicity(0, 1))
    }
)
outgoing184: BinaryAssociation = BinaryAssociation(
    name="outgoing184",
    ends={
        Property(name="Syntax186", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities185", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming187: BinaryAssociation = BinaryAssociation(
    name="incoming187",
    ends={
        Property(name="Syntax189", type=fUML_IntermediateActivities_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities188", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
edge175: BinaryAssociation = BinaryAssociation(
    name="edge175",
    ends={
        Property(name="Syntax177", type=fUML_IntermediateActivities_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities176", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decisionInputFlow192: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow192",
    ends={
        Property(name="IntermediateActivities_ObjectFlow", type=fUML_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_DecisionNode193", type=IntermediateActivities_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
parameter194: BinaryAssociation = BinaryAssociation(
    name="parameter194",
    ends={
        Property(name="Kernel_Parameter195", type=fUML_IntermediateActivities_ActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_ActivityParameterNode", type=Kernel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
decider196: BinaryAssociation = BinaryAssociation(
    name="decider196",
    ends={
        Property(name="BasicActions_OutputPin", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
test197: BinaryAssociation = BinaryAssociation(
    name="test197",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode198", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
bodyOutput199: BinaryAssociation = BinaryAssociation(
    name="bodyOutput199",
    ends={
        Property(name="BasicActions_OutputPin201", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode200", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput202: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput202",
    ends={
        Property(name="BasicActions_InputPin", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode203", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyPart204: BinaryAssociation = BinaryAssociation(
    name="bodyPart204",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode206", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode205", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
result207: BinaryAssociation = BinaryAssociation(
    name="result207",
    ends={
        Property(name="BasicActions_OutputPin209", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode208", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopVariable210: BinaryAssociation = BinaryAssociation(
    name="loopVariable210",
    ends={
        Property(name="BasicActions_OutputPin212", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode211", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart213: BinaryAssociation = BinaryAssociation(
    name="setupPart213",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode215", type=fUML_CompleteStructuredActivities_LoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_LoopNode214", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
decisionInput190: BinaryAssociation = BinaryAssociation(
    name="decisionInput190",
    ends={
        Property(name="BasicBehaviors_Behavior191", type=fUML_IntermediateActivities_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActivities_DecisionNode", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
test216: BinaryAssociation = BinaryAssociation(
    name="test216",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode217", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
body218: BinaryAssociation = BinaryAssociation(
    name="body218",
    ends={
        Property(name="CompleteStructuredActivities_ExecutableNode220", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause219", type=CompleteStructuredActivities_ExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
predecessorClause221: BinaryAssociation = BinaryAssociation(
    name="predecessorClause221",
    ends={
        Property(name="Syntax223", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities222", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause224: BinaryAssociation = BinaryAssociation(
    name="successorClause224",
    ends={
        Property(name="Syntax226", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities225", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(0, 9999))
    }
)
decider227: BinaryAssociation = BinaryAssociation(
    name="decider227",
    ends={
        Property(name="BasicActions_OutputPin229", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause228", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput230: BinaryAssociation = BinaryAssociation(
    name="bodyOutput230",
    ends={
        Property(name="BasicActions_OutputPin232", type=fUML_CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_Clause231", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
clause233: BinaryAssociation = BinaryAssociation(
    name="clause233",
    ends={
        Property(name="CompleteStructuredActivities_Clause", type=fUML_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_ConditionalNode", type=CompleteStructuredActivities_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
result234: BinaryAssociation = BinaryAssociation(
    name="result234",
    ends={
        Property(name="BasicActions_OutputPin236", type=fUML_CompleteStructuredActivities_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_ConditionalNode235", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node237: BinaryAssociation = BinaryAssociation(
    name="node237",
    ends={
        Property(name="Syntax239", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities238", type=IntermediateActivities_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge240: BinaryAssociation = BinaryAssociation(
    name="edge240",
    ends={
        Property(name="Syntax242", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities241", type=IntermediateActivities_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuredNodeInput245: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput245",
    ends={
        Property(name="BasicActions_InputPin247", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_StructuredActivityNode246", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regionAsOutput248: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput248",
    ends={
        Property(name="Syntax250", type=fUML_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities249", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput251: BinaryAssociation = BinaryAssociation(
    name="regionAsInput251",
    ends={
        Property(name="Syntax253", type=fUML_ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities252", type=ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
inputElement254: BinaryAssociation = BinaryAssociation(
    name="inputElement254",
    ends={
        Property(name="Syntax256", type=fUML_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities255", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
outputElement257: BinaryAssociation = BinaryAssociation(
    name="outputElement257",
    ends={
        Property(name="Syntax259", type=fUML_ExtraStructuredActivities_ExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="Activities258", type=ExtraStructuredActivities_ExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature260: BinaryAssociation = BinaryAssociation(
    name="structuralFeature260",
    ends={
        Property(name="Kernel_StructuralFeature261", type=fUML_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_StructuralFeatureAction", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
object262: BinaryAssociation = BinaryAssociation(
    name="object262",
    ends={
        Property(name="BasicActions_InputPin264", type=fUML_IntermediateActions_StructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_StructuralFeatureAction263", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structuredNodeOutput243: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput243",
    ends={
        Property(name="BasicActions_OutputPin244", type=fUML_CompleteStructuredActivities_StructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteStructuredActivities_StructuredActivityNode", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
second265: BinaryAssociation = BinaryAssociation(
    name="second265",
    ends={
        Property(name="BasicActions_InputPin266", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result267: BinaryAssociation = BinaryAssociation(
    name="result267",
    ends={
        Property(name="BasicActions_OutputPin269", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction268", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first270: BinaryAssociation = BinaryAssociation(
    name="first270",
    ends={
        Property(name="BasicActions_InputPin272", type=fUML_IntermediateActions_TestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_TestIdentityAction271", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value273: BinaryAssociation = BinaryAssociation(
    name="value273",
    ends={
        Property(name="Kernel_ValueSpecification274", type=fUML_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ValueSpecificationAction", type=Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result275: BinaryAssociation = BinaryAssociation(
    name="result275",
    ends={
        Property(name="BasicActions_OutputPin277", type=fUML_IntermediateActions_ValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ValueSpecificationAction276", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endData278: BinaryAssociation = BinaryAssociation(
    name="endData278",
    ends={
        Property(name="IntermediateActions_LinkEndData", type=fUML_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkAction", type=IntermediateActions_LinkEndData, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
inputValue279: BinaryAssociation = BinaryAssociation(
    name="inputValue279",
    ends={
        Property(name="BasicActions_InputPin281", type=fUML_IntermediateActions_LinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkAction280", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value282: BinaryAssociation = BinaryAssociation(
    name="value282",
    ends={
        Property(name="BasicActions_InputPin283", type=fUML_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
end284: BinaryAssociation = BinaryAssociation(
    name="end284",
    ends={
        Property(name="Kernel_Property286", type=fUML_IntermediateActions_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndData285", type=Kernel_Property, multiplicity=Multiplicity(1, 1))
    }
)
result289: BinaryAssociation = BinaryAssociation(
    name="result289",
    ends={
        Property(name="BasicActions_OutputPin291", type=fUML_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_WriteStructuralFeatureAction290", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
removeAt292: BinaryAssociation = BinaryAssociation(
    name="removeAt292",
    ends={
        Property(name="BasicActions_InputPin293", type=fUML_IntermediateActions_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_RemoveStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result294: BinaryAssociation = BinaryAssociation(
    name="result294",
    ends={
        Property(name="BasicActions_OutputPin295", type=fUML_IntermediateActions_ReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadLinkAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result296: BinaryAssociation = BinaryAssociation(
    name="result296",
    ends={
        Property(name="BasicActions_OutputPin297", type=fUML_IntermediateActions_ReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadSelfAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result298: BinaryAssociation = BinaryAssociation(
    name="result298",
    ends={
        Property(name="BasicActions_OutputPin299", type=fUML_IntermediateActions_ReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ReadStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insertAt300: BinaryAssociation = BinaryAssociation(
    name="insertAt300",
    ends={
        Property(name="BasicActions_InputPin301", type=fUML_IntermediateActions_LinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndCreationData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
destroyAt302: BinaryAssociation = BinaryAssociation(
    name="destroyAt302",
    ends={
        Property(name="BasicActions_InputPin303", type=fUML_IntermediateActions_LinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_LinkEndDestructionData", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
value287: BinaryAssociation = BinaryAssociation(
    name="value287",
    ends={
        Property(name="BasicActions_InputPin288", type=fUML_IntermediateActions_WriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_WriteStructuralFeatureAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object305: BinaryAssociation = BinaryAssociation(
    name="object305",
    ends={
        Property(name="BasicActions_InputPin307", type=fUML_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearAssociationAction306", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result308: BinaryAssociation = BinaryAssociation(
    name="result308",
    ends={
        Property(name="BasicActions_OutputPin309", type=fUML_IntermediateActions_ClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearStructuralFeatureAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target315: BinaryAssociation = BinaryAssociation(
    name="target315",
    ends={
        Property(name="BasicActions_InputPin316", type=fUML_IntermediateActions_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_DestroyObjectAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result310: BinaryAssociation = BinaryAssociation(
    name="result310",
    ends={
        Property(name="BasicActions_OutputPin311", type=fUML_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_CreateObjectAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier312: BinaryAssociation = BinaryAssociation(
    name="classifier312",
    ends={
        Property(name="Kernel_Classifier314", type=fUML_IntermediateActions_CreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_CreateObjectAction313", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
association304: BinaryAssociation = BinaryAssociation(
    name="association304",
    ends={
        Property(name="Kernel_Association", type=fUML_IntermediateActions_ClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_ClearAssociationAction", type=Kernel_Association, multiplicity=Multiplicity(1, 1))
    }
)
reducer323: BinaryAssociation = BinaryAssociation(
    name="reducer323",
    ends={
        Property(name="BasicBehaviors_Behavior324", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
result325: BinaryAssociation = BinaryAssociation(
    name="result325",
    ends={
        Property(name="BasicActions_OutputPin327", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction326", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection328: BinaryAssociation = BinaryAssociation(
    name="collection328",
    ends={
        Property(name="BasicActions_InputPin330", type=fUML_CompleteActions_ReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReduceAction329", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result331: BinaryAssociation = BinaryAssociation(
    name="result331",
    ends={
        Property(name="BasicActions_OutputPin332", type=fUML_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadExtentAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
insertAt317: BinaryAssociation = BinaryAssociation(
    name="insertAt317",
    ends={
        Property(name="BasicActions_InputPin318", type=fUML_IntermediateActions_AddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_IntermediateActions_AddStructuralFeatureValueAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object319: BinaryAssociation = BinaryAssociation(
    name="object319",
    ends={
        Property(name="BasicActions_InputPin320", type=fUML_CompleteActions_StartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_StartClassifierBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object321: BinaryAssociation = BinaryAssociation(
    name="object321",
    ends={
        Property(name="BasicActions_InputPin322", type=fUML_CompleteActions_StartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_StartObjectBehaviorAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object346: BinaryAssociation = BinaryAssociation(
    name="object346",
    ends={
        Property(name="BasicActions_InputPin348", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction347", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newClassifier349: BinaryAssociation = BinaryAssociation(
    name="newClassifier349",
    ends={
        Property(name="Kernel_Classifier351", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction350", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
result352: BinaryAssociation = BinaryAssociation(
    name="result352",
    ends={
        Property(name="BasicActions_OutputPin353", type=fUML_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_AcceptEventAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger354: BinaryAssociation = BinaryAssociation(
    name="trigger354",
    ends={
        Property(name="Communications_Trigger", type=fUML_CompleteActions_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_AcceptEventAction355", type=Communications_Trigger, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classifier333: BinaryAssociation = BinaryAssociation(
    name="classifier333",
    ends={
        Property(name="Kernel_Classifier335", type=fUML_CompleteActions_ReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadExtentAction334", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
classifier336: BinaryAssociation = BinaryAssociation(
    name="classifier336",
    ends={
        Property(name="Kernel_Classifier337", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
result338: BinaryAssociation = BinaryAssociation(
    name="result338",
    ends={
        Property(name="BasicActions_OutputPin340", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction339", type=BasicActions_OutputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object341: BinaryAssociation = BinaryAssociation(
    name="object341",
    ends={
        Property(name="BasicActions_InputPin343", type=fUML_CompleteActions_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReadIsClassifiedObjectAction342", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
oldClassifier344: BinaryAssociation = BinaryAssociation(
    name="oldClassifier344",
    ends={
        Property(name="Kernel_Classifier345", type=fUML_CompleteActions_ReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_CompleteActions_ReclassifyObjectAction", type=Kernel_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
argument366: BinaryAssociation = BinaryAssociation(
    name="argument366",
    ends={
        Property(name="BasicActions_InputPin367", type=fUML_BasicActions_InvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_InvocationAction", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target368: BinaryAssociation = BinaryAssociation(
    name="target368",
    ends={
        Property(name="BasicActions_InputPin369", type=fUML_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_SendSignalAction", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal370: BinaryAssociation = BinaryAssociation(
    name="signal370",
    ends={
        Property(name="Communications_Signal372", type=fUML_BasicActions_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_SendSignalAction371", type=Communications_Signal, multiplicity=Multiplicity(1, 1))
    }
)
output356: BinaryAssociation = BinaryAssociation(
    name="output356",
    ends={
        Property(name="BasicActions_OutputPin357", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
context358: BinaryAssociation = BinaryAssociation(
    name="context358",
    ends={
        Property(name="Kernel_Classifier360", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action359", type=Kernel_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
input361: BinaryAssociation = BinaryAssociation(
    name="input361",
    ends={
        Property(name="BasicActions_InputPin363", type=fUML_BasicActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_Action362", type=BasicActions_InputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result364: BinaryAssociation = BinaryAssociation(
    name="result364",
    ends={
        Property(name="BasicActions_OutputPin365", type=fUML_BasicActions_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallAction", type=BasicActions_OutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature380: BinaryAssociation = BinaryAssociation(
    name="feature380",
    ends={
        Property(name="Kernel_StructuralFeature381", type=fUML_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_FeatureValue", type=Kernel_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
values382: BinaryAssociation = BinaryAssociation(
    name="values382",
    ends={
        Property(name="Kernel_Value", type=fUML_Kernel_FeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_FeatureValue383", type=Kernel_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior373: BinaryAssociation = BinaryAssociation(
    name="behavior373",
    ends={
        Property(name="BasicBehaviors_Behavior374", type=fUML_BasicActions_CallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallBehaviorAction", type=BasicBehaviors_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
operation375: BinaryAssociation = BinaryAssociation(
    name="operation375",
    ends={
        Property(name="Kernel_Operation376", type=fUML_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallOperationAction", type=Kernel_Operation, multiplicity=Multiplicity(1, 1))
    }
)
target377: BinaryAssociation = BinaryAssociation(
    name="target377",
    ends={
        Property(name="BasicActions_InputPin379", type=fUML_BasicActions_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_BasicActions_CallOperationAction378", type=BasicActions_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referent385: BinaryAssociation = BinaryAssociation(
    name="referent385",
    ends={
        Property(name="Kernel_Object", type=fUML_Kernel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Reference", type=Kernel_Object, multiplicity=Multiplicity(1, 1))
    }
)
type384: BinaryAssociation = BinaryAssociation(
    name="type384",
    ends={
        Property(name="Kernel_PrimitiveType", type=fUML_Kernel_PrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_PrimitiveValue", type=Kernel_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
type389: BinaryAssociation = BinaryAssociation(
    name="type389",
    ends={
        Property(name="Kernel_Association390", type=fUML_Kernel_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Link", type=Kernel_Association, multiplicity=Multiplicity(0, 1))
    }
)
types386: BinaryAssociation = BinaryAssociation(
    name="types386",
    ends={
        Property(name="Kernel_Class387", type=fUML_Kernel_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_Object", type=Kernel_Class, multiplicity=Multiplicity(0, 9999))
    }
)
featureValues388: BinaryAssociation = BinaryAssociation(
    name="featureValues388",
    ends={
        Property(name="Kernel_FeatureValue", type=fUML_Kernel_CompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_CompoundValue", type=Kernel_FeatureValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal391: BinaryAssociation = BinaryAssociation(
    name="literal391",
    ends={
        Property(name="Kernel_EnumerationLiteral", type=fUML_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_EnumerationValue", type=Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
type392: BinaryAssociation = BinaryAssociation(
    name="type392",
    ends={
        Property(name="Kernel_Enumeration", type=fUML_Kernel_EnumerationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_EnumerationValue393", type=Kernel_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
type394: BinaryAssociation = BinaryAssociation(
    name="type394",
    ends={
        Property(name="Kernel_DataType", type=fUML_Kernel_DataValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fUML_Kernel_DataValue", type=Kernel_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fUML_BasicBehaviors_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=fUML_BasicBehaviors_OpaqueBehavior)
gen_fUML_BasicBehaviors_Behavior_Class = Generalization(general=Class_, specific=fUML_BasicBehaviors_Behavior)
gen_fUML_Communications_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fUML_Communications_Reception)
gen_fUML_Kernel_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=fUML_Kernel_ValueSpecification)
gen_fUML_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_TypedElement)
gen_fUML_BasicBehaviors_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=fUML_BasicBehaviors_BehavioredClassifier)
gen_fUML_BasicBehaviors_FunctionBehavior_OpaqueBehavior = Generalization(general=OpaqueBehavior, specific=fUML_BasicBehaviors_FunctionBehavior)
gen_fUML_Communications_Trigger_NamedElement = Generalization(general=NamedElement, specific=fUML_Communications_Trigger)
gen_fUML_Communications_Event_PackageableElement = Generalization(general=PackageableElement, specific=fUML_Communications_Event)
gen_fUML_Communications_Signal_Classifier = Generalization(general=Classifier, specific=fUML_Communications_Signal)
gen_fUML_Communications_SignalEvent_MessageEvent = Generalization(general=MessageEvent, specific=fUML_Communications_SignalEvent)
gen_fUML_Communications_MessageEvent_Event = Generalization(general=Event, specific=fUML_Communications_MessageEvent)
gen_fUML_Kernel_ElementImport_Element = Generalization(general=Element, specific=fUML_Kernel_ElementImport)
gen_fUML_Kernel_NamedElement_Element = Generalization(general=Element, specific=fUML_Kernel_NamedElement)
gen_fUML_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_Namespace)
gen_fUML_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fUML_Kernel_StructuralFeature)
gen_fUML_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=fUML_Kernel_Feature)
gen_fUML_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_PackageableElement)
gen_fUML_Kernel_PackageImport_Element = Generalization(general=Element, specific=fUML_Kernel_PackageImport)
gen_fUML_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fUML_Kernel_Package)
gen_fUML_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=fUML_Kernel_Package)
gen_fUML_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=fUML_Kernel_Type)
gen_fUML_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_RedefinableElement)
gen_fUML_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=fUML_Kernel_Classifier)
gen_fUML_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=fUML_Kernel_Classifier)
gen_fUML_Kernel_Generalization_Element = Generalization(general=Element, specific=fUML_Kernel_Generalization)
gen_fUML_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=fUML_Kernel_Property)
gen_fUML_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=fUML_Kernel_DataType)
gen_fUML_Kernel_Association_Classifier = Generalization(general=Classifier, specific=fUML_Kernel_Association)
gen_fUML_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=fUML_Kernel_MultiplicityElement)
gen_fUML_Kernel_Parameter_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_Kernel_Parameter)
gen_fUML_Kernel_Parameter_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=fUML_Kernel_Parameter)
gen_fUML_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=fUML_Kernel_Operation)
gen_fUML_Kernel_BehavioralFeature_Feature = Generalization(general=Feature, specific=fUML_Kernel_BehavioralFeature)
gen_fUML_Kernel_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=fUML_Kernel_InstanceSpecification)
gen_fUML_Kernel_Slot_Element = Generalization(general=Element, specific=fUML_Kernel_Slot)
gen_fUML_Kernel_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=fUML_Kernel_InstanceValue)
gen_fUML_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralBoolean)
gen_fUML_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=fUML_Kernel_LiteralSpecification)
gen_fUML_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralInteger)
gen_fUML_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralNull)
gen_fUML_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=fUML_Kernel_PrimitiveType)
gen_fUML_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=fUML_Kernel_Enumeration)
gen_fUML_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=fUML_Kernel_EnumerationLiteral)
gen_fUML_Kernel_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=fUML_Kernel_Class)
gen_fUML_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralString)
gen_fUML_Kernel_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=fUML_Kernel_LiteralUnlimitedNatural)
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
gen_fUML_IntermediateActivities_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=fUML_IntermediateActivities_ActivityFinalNode)
gen_fUML_IntermediateActivities_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=fUML_IntermediateActivities_ActivityParameterNode)
gen_fUML_CompleteStructuredActivities_LoopNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_CompleteStructuredActivities_LoopNode)
gen_fUML_IntermediateActivities_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=fUML_IntermediateActivities_DecisionNode)
gen_fUML_CompleteStructuredActivities_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=fUML_CompleteStructuredActivities_ExecutableNode)
gen_fUML_CompleteStructuredActivities_Clause_Element = Generalization(general=Element, specific=fUML_CompleteStructuredActivities_Clause)
gen_fUML_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_CompleteStructuredActivities_ConditionalNode)
gen_fUML_CompleteStructuredActivities_StructuredActivityNode_Action = Generalization(general=Action, specific=fUML_CompleteStructuredActivities_StructuredActivityNode)
gen_fUML_ExtraStructuredActivities_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=fUML_ExtraStructuredActivities_ExpansionNode)
gen_fUML_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode = Generalization(general=StructuredActivityNode, specific=fUML_ExtraStructuredActivities_ExpansionRegion)
gen_fUML_IntermediateActions_StructuralFeatureAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_StructuralFeatureAction)
gen_fUML_IntermediateActions_ValueSpecificationAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ValueSpecificationAction)
gen_fUML_IntermediateActions_WriteLinkAction_LinkAction = Generalization(general=LinkAction, specific=fUML_IntermediateActions_WriteLinkAction)
gen_fUML_IntermediateActions_LinkAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_LinkAction)
gen_fUML_IntermediateActions_LinkEndData_Element = Generalization(general=Element, specific=fUML_IntermediateActions_LinkEndData)
gen_fUML_IntermediateActions_TestIdentityAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_TestIdentityAction)
gen_fUML_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fUML_IntermediateActions_RemoveStructuralFeatureValueAction)
gen_fUML_IntermediateActions_ReadLinkAction_LinkAction = Generalization(general=LinkAction, specific=fUML_IntermediateActions_ReadLinkAction)
gen_fUML_IntermediateActions_ReadSelfAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ReadSelfAction)
gen_fUML_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_ReadStructuralFeatureAction)
gen_fUML_IntermediateActions_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=fUML_IntermediateActions_LinkEndCreationData)
gen_fUML_IntermediateActions_LinkEndDestructionData_LinkEndData = Generalization(general=LinkEndData, specific=fUML_IntermediateActions_LinkEndDestructionData)
gen_fUML_IntermediateActions_ClearAssociationAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_ClearAssociationAction)
gen_fUML_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_WriteStructuralFeatureAction)
gen_fUML_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction = Generalization(general=StructuralFeatureAction, specific=fUML_IntermediateActions_ClearStructuralFeatureAction)
gen_fUML_IntermediateActions_CreateLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fUML_IntermediateActions_CreateLinkAction)
gen_fUML_IntermediateActions_CreateObjectAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_CreateObjectAction)
gen_fUML_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction = Generalization(general=WriteStructuralFeatureAction, specific=fUML_IntermediateActions_AddStructuralFeatureValueAction)
gen_fUML_IntermediateActions_DestroyLinkAction_WriteLinkAction = Generalization(general=WriteLinkAction, specific=fUML_IntermediateActions_DestroyLinkAction)
gen_fUML_IntermediateActions_DestroyObjectAction_Action = Generalization(general=Action, specific=fUML_IntermediateActions_DestroyObjectAction)
gen_fUML_CompleteActions_ReadExtentAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReadExtentAction)
gen_fUML_CompleteActions_StartClassifierBehaviorAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_StartClassifierBehaviorAction)
gen_fUML_CompleteActions_StartObjectBehaviorAction_CallAction = Generalization(general=CallAction, specific=fUML_CompleteActions_StartObjectBehaviorAction)
gen_fUML_CompleteActions_ReduceAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReduceAction)
gen_fUML_CompleteActions_AcceptEventAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_AcceptEventAction)
gen_fUML_CompleteActions_ReadIsClassifiedObjectAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReadIsClassifiedObjectAction)
gen_fUML_CompleteActions_ReclassifyObjectAction_Action = Generalization(general=Action, specific=fUML_CompleteActions_ReclassifyObjectAction)
gen_fUML_BasicActions_InvocationAction_Action = Generalization(general=Action, specific=fUML_BasicActions_InvocationAction)
gen_fUML_BasicActions_SendSignalAction_InvocationAction = Generalization(general=InvocationAction, specific=fUML_BasicActions_SendSignalAction)
gen_fUML_BasicActions_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=fUML_BasicActions_Action)
gen_fUML_BasicActions_InputPin_Pin = Generalization(general=Pin, specific=fUML_BasicActions_InputPin)
gen_fUML_BasicActions_Pin_IntermediateActivities_ObjectNode = Generalization(general=IntermediateActivities_ObjectNode, specific=fUML_BasicActions_Pin)
gen_fUML_BasicActions_Pin_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=fUML_BasicActions_Pin)
gen_fUML_BasicActions_CallAction_InvocationAction = Generalization(general=InvocationAction, specific=fUML_BasicActions_CallAction)
gen_fUML_Kernel_StructuredValue_Value = Generalization(general=Value, specific=fUML_Kernel_StructuredValue)
gen_fUML_BasicActions_CallBehaviorAction_CallAction = Generalization(general=CallAction, specific=fUML_BasicActions_CallBehaviorAction)
gen_fUML_BasicActions_CallOperationAction_CallAction = Generalization(general=CallAction, specific=fUML_BasicActions_CallOperationAction)
gen_fUML_BasicActions_OutputPin_Pin = Generalization(general=Pin, specific=fUML_BasicActions_OutputPin)
gen_fUML_Kernel_Reference_StructuredValue = Generalization(general=StructuredValue, specific=fUML_Kernel_Reference)
gen_fUML_Kernel_Object_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fUML_Kernel_Object)
gen_fUML_Kernel_UnlimitedNaturalValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_UnlimitedNaturalValue)
gen_fUML_Kernel_PrimitiveValue_Value = Generalization(general=Value, specific=fUML_Kernel_PrimitiveValue)
gen_fUML_Kernel_StringValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_StringValue)
gen_fUML_Kernel_IntegerValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_IntegerValue)
gen_fUML_Kernel_EnumerationValue_Value = Generalization(general=Value, specific=fUML_Kernel_EnumerationValue)
gen_fUML_Kernel_ExtensionalValue_CompoundValue = Generalization(general=CompoundValue, specific=fUML_Kernel_ExtensionalValue)
gen_fUML_Kernel_CompoundValue_StructuredValue = Generalization(general=StructuredValue, specific=fUML_Kernel_CompoundValue)
gen_fUML_Kernel_Link_ExtensionalValue = Generalization(general=ExtensionalValue, specific=fUML_Kernel_Link)
gen_fUML_Kernel_Value_SemanticVisitor = Generalization(general=SemanticVisitor, specific=fUML_Kernel_Value)
gen_fUML_Kernel_DataValue_CompoundValue = Generalization(general=CompoundValue, specific=fUML_Kernel_DataValue)
gen_fUML_Kernel_BooleanValue_PrimitiveValue = Generalization(general=PrimitiveValue, specific=fUML_Kernel_BooleanValue)

# Domain Model
domain_model = DomainModel(
    name="fUML",
    types={Kernel_BehavioralFeature, Kernel_Parameter, BasicBehaviors_BehavioredClassifier, fUML_BasicBehaviors_OpaqueBehavior, Behavior, fUML_BasicBehaviors_Behavior, Class_, fUML_Communications_Reception, BehavioralFeature, fUML_Kernel_ValueSpecification, TypedElement, fUML_Kernel_TypedElement, Kernel_Type, fUML_BasicBehaviors_BehavioredClassifier, Classifier, BasicBehaviors_Behavior, fUML_BasicBehaviors_FunctionBehavior, OpaqueBehavior, fUML_Communications_Trigger, NamedElement, Communications_Event, fUML_Communications_Event, PackageableElement, fUML_Communications_Signal, Kernel_Property, fUML_Communications_SignalEvent, MessageEvent, Communications_Signal, fUML_Communications_MessageEvent, Event, Kernel_ElementImport, Kernel_PackageImport, Kernel_PackageableElement, fUML_Kernel_ElementImport, fUML_Kernel_NamedElement, Element, Kernel_Namespace, fUML_Kernel_Element, Kernel_Element, Kernel_Comment, fUML_Kernel_Comment, fUML_Kernel_Namespace, Kernel_NamedElement, fUML_Kernel_StructuralFeature, Kernel_Feature, Kernel_MultiplicityElement, Kernel_TypedElement, fUML_Kernel_Feature, RedefinableElement, Kernel_Classifier, fUML_Kernel_PackageableElement, fUML_Kernel_PackageImport, Kernel_Package, fUML_Kernel_Package, fUML_Kernel_Type, fUML_Kernel_RedefinableElement, Kernel_RedefinableElement, fUML_Kernel_Classifier, Kernel_Generalization, Kernel_Association, Kernel_DataType, Kernel_Class, fUML_Kernel_Generalization, fUML_Kernel_Property, StructuralFeature, fUML_Kernel_DataType, fUML_Kernel_Association, fUML_Kernel_MultiplicityElement, fUML_Kernel_Parameter, Kernel_ValueSpecification, fUML_Kernel_Operation, fUML_Kernel_BehavioralFeature, Feature, fUML_Kernel_InstanceSpecification, Kernel_Slot, fUML_Kernel_Slot, Kernel_StructuralFeature, Kernel_InstanceSpecification, fUML_Kernel_InstanceValue, ValueSpecification, fUML_Kernel_LiteralBoolean, LiteralSpecification, fUML_Kernel_LiteralSpecification, fUML_Kernel_LiteralInteger, fUML_Kernel_LiteralNull, Kernel_Operation, fUML_Kernel_PrimitiveType, DataType, fUML_Kernel_Enumeration, Kernel_EnumerationLiteral, fUML_Kernel_EnumerationLiteral, InstanceSpecification, Kernel_Enumeration, fUML_Kernel_Class, BehavioredClassifier, Communications_Reception, fUML_Kernel_LiteralString, fUML_Kernel_LiteralUnlimitedNatural, fUML_IntermediateActivities_ObjectFlow, ActivityEdge, fUML_IntermediateActivities_ActivityEdge, IntermediateActivities_Activity, IntermediateActivities_ActivityNode, CompleteStructuredActivities_StructuredActivityNode, fUML_IntermediateActivities_Activity, fUML_IntermediateActivities_ActivityNode, fUML_IntermediateActivities_ObjectNode, fUML_IntermediateActivities_MergeNode, ControlNode, fUML_IntermediateActivities_ControlNode, ActivityNode, fUML_IntermediateActivities_JoinNode, fUML_IntermediateActivities_InitialNode, fUML_IntermediateActivities_FinalNode, fUML_IntermediateActivities_ForkNode, fUML_IntermediateActivities_ControlFlow, IntermediateActivities_ActivityEdge, fUML_IntermediateActivities_ActivityFinalNode, FinalNode, fUML_IntermediateActivities_ActivityParameterNode, ObjectNode, fUML_CompleteStructuredActivities_LoopNode, StructuredActivityNode, BasicActions_OutputPin, CompleteStructuredActivities_ExecutableNode, BasicActions_InputPin, fUML_CompleteStructuredActivities_ExecutableNode, fUML_IntermediateActivities_DecisionNode, fUML_CompleteStructuredActivities_Clause, IntermediateActivities_ObjectFlow, CompleteStructuredActivities_Clause, fUML_CompleteStructuredActivities_ConditionalNode, fUML_CompleteStructuredActivities_StructuredActivityNode, Action, fUML_ExtraStructuredActivities_ExpansionNode, ExtraStructuredActivities_ExpansionRegion, fUML_ExtraStructuredActivities_ExpansionRegion, ExtraStructuredActivities_ExpansionNode, fUML_IntermediateActions_StructuralFeatureAction, fUML_IntermediateActions_ValueSpecificationAction, fUML_IntermediateActions_WriteLinkAction, LinkAction, fUML_IntermediateActions_LinkAction, IntermediateActions_LinkEndData, fUML_IntermediateActions_LinkEndData, fUML_IntermediateActions_TestIdentityAction, fUML_IntermediateActions_RemoveStructuralFeatureValueAction, WriteStructuralFeatureAction, fUML_IntermediateActions_ReadLinkAction, fUML_IntermediateActions_ReadSelfAction, fUML_IntermediateActions_ReadStructuralFeatureAction, fUML_IntermediateActions_LinkEndCreationData, LinkEndData, fUML_IntermediateActions_LinkEndDestructionData, fUML_IntermediateActions_ClearAssociationAction, fUML_IntermediateActions_WriteStructuralFeatureAction, StructuralFeatureAction, fUML_IntermediateActions_ClearStructuralFeatureAction, fUML_IntermediateActions_CreateLinkAction, WriteLinkAction, fUML_IntermediateActions_CreateObjectAction, fUML_IntermediateActions_AddStructuralFeatureValueAction, fUML_IntermediateActions_DestroyLinkAction, fUML_IntermediateActions_DestroyObjectAction, fUML_CompleteActions_ReadExtentAction, fUML_CompleteActions_StartClassifierBehaviorAction, fUML_CompleteActions_StartObjectBehaviorAction, CallAction, fUML_CompleteActions_ReduceAction, fUML_CompleteActions_AcceptEventAction, Communications_Trigger, fUML_CompleteActions_ReadIsClassifiedObjectAction, fUML_CompleteActions_ReclassifyObjectAction, fUML_BasicActions_InvocationAction, fUML_BasicActions_SendSignalAction, fUML_BasicActions_CallBehaviorAction, fUML_BasicActions_Action, ExecutableNode, fUML_BasicActions_InputPin, Pin, fUML_BasicActions_Pin, IntermediateActivities_ObjectNode, fUML_BasicActions_CallAction, InvocationAction, fUML_Kernel_StructuredValue, Value, fUML_Kernel_FeatureValue, Kernel_Value, fUML_BasicActions_CallOperationAction, fUML_BasicActions_OutputPin, fUML_Kernel_Reference, StructuredValue, Kernel_Object, fUML_Kernel_Object, ExtensionalValue, fUML_Kernel_UnlimitedNaturalValue, PrimitiveValue, fUML_Kernel_PrimitiveValue, Kernel_PrimitiveType, fUML_Kernel_StringValue, fUML_Kernel_IntegerValue, fUML_Kernel_EnumerationValue, fUML_Kernel_ExtensionalValue, CompoundValue, fUML_Kernel_CompoundValue, Kernel_FeatureValue, fUML_Kernel_Link, fUML_Kernel_Value, SemanticVisitor, fUML_LociL1_SemanticVisitor, fUML_Kernel_DataValue, fUML_Kernel_BooleanValue, CallConcurrencyKind, VisibilityKind, AggregationKind, ParameterDirectionKind, ExpansionKind},
    associations={specification0, ownedParameter1, context2, signal11, type13, ownedBehavior4, classifierBehavior5, event8, ownedAttribute9, signal10, elementImport26, packageImport29, importedMember32, ownedMember34, namespace14, ownedElement17, owner20, ownedComment23, annotatedElement24, member25, featuringClassifier60, importedElement37, importingNamespace39, importedPackage42, importingNamespace43, packagedElement46, ownedType48, nestedPackage51, nestingPackage54, package57, feature69, inheritedMember72, attribute74, redefinedElement63, redefinitionContext64, generalization66, owningAssociation85, association88, datatype91, class94, general77, general80, specific82, memberEnd101, navigableOwnedEnd104, ownedEnd107, opposite97, endType99, ownedAttribute110, method119, upperValue113, lowerValue114, ownedParameter117, classifier128, slot130, definingFeature133, value134, owningInstance137, instance140, class121, redefinedOperation124, type125, ownedLiteral141, enumeration144, ownedAttribute147, ownedOperation150, superClass153, ownedReception154, activity159, source161, target164, inStructuredNode167, guard170, node172, nestedClassifier156, inStructuredNode178, activity181, outgoing184, incoming187, edge175, decisionInputFlow192, parameter194, decider196, test197, bodyOutput199, loopVariableInput202, bodyPart204, result207, loopVariable210, setupPart213, decisionInput190, test216, body218, predecessorClause221, successorClause224, decider227, bodyOutput230, clause233, result234, node237, edge240, structuredNodeInput245, regionAsOutput248, regionAsInput251, inputElement254, outputElement257, structuralFeature260, object262, structuredNodeOutput243, second265, result267, first270, value273, result275, endData278, inputValue279, value282, end284, result289, removeAt292, result294, result296, result298, insertAt300, destroyAt302, value287, object305, result308, target315, result310, classifier312, association304, reducer323, result325, collection328, result331, insertAt317, object319, object321, object346, newClassifier349, result352, trigger354, classifier333, classifier336, result338, object341, oldClassifier344, argument366, target368, signal370, output356, context358, input361, result364, feature380, values382, behavior373, operation375, target377, referent385, type384, type389, types386, featureValues388, literal391, type392, type394},
    generalizations={gen_fUML_BasicBehaviors_OpaqueBehavior_Behavior, gen_fUML_BasicBehaviors_Behavior_Class, gen_fUML_Communications_Reception_BehavioralFeature, gen_fUML_Kernel_ValueSpecification_TypedElement, gen_fUML_Kernel_TypedElement_NamedElement, gen_fUML_BasicBehaviors_BehavioredClassifier_Classifier, gen_fUML_BasicBehaviors_FunctionBehavior_OpaqueBehavior, gen_fUML_Communications_Trigger_NamedElement, gen_fUML_Communications_Event_PackageableElement, gen_fUML_Communications_Signal_Classifier, gen_fUML_Communications_SignalEvent_MessageEvent, gen_fUML_Communications_MessageEvent_Event, gen_fUML_Kernel_ElementImport_Element, gen_fUML_Kernel_NamedElement_Element, gen_fUML_Kernel_Namespace_NamedElement, gen_fUML_Kernel_StructuralFeature_Kernel_Feature, gen_fUML_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_fUML_Kernel_StructuralFeature_Kernel_TypedElement, gen_fUML_Kernel_Feature_RedefinableElement, gen_fUML_Kernel_PackageableElement_NamedElement, gen_fUML_Kernel_PackageImport_Element, gen_fUML_Kernel_Package_Kernel_Namespace, gen_fUML_Kernel_Package_Kernel_PackageableElement, gen_fUML_Kernel_Type_PackageableElement, gen_fUML_Kernel_RedefinableElement_NamedElement, gen_fUML_Kernel_Classifier_Kernel_Namespace, gen_fUML_Kernel_Classifier_Kernel_Type, gen_fUML_Kernel_Generalization_Element, gen_fUML_Kernel_Property_StructuralFeature, gen_fUML_Kernel_DataType_Classifier, gen_fUML_Kernel_Association_Classifier, gen_fUML_Kernel_MultiplicityElement_Element, gen_fUML_Kernel_Parameter_Kernel_MultiplicityElement, gen_fUML_Kernel_Parameter_Kernel_TypedElement, gen_fUML_Kernel_Operation_BehavioralFeature, gen_fUML_Kernel_BehavioralFeature_Feature, gen_fUML_Kernel_InstanceSpecification_NamedElement, gen_fUML_Kernel_Slot_Element, gen_fUML_Kernel_InstanceValue_ValueSpecification, gen_fUML_Kernel_LiteralBoolean_LiteralSpecification, gen_fUML_Kernel_LiteralSpecification_ValueSpecification, gen_fUML_Kernel_LiteralInteger_LiteralSpecification, gen_fUML_Kernel_LiteralNull_LiteralSpecification, gen_fUML_Kernel_PrimitiveType_DataType, gen_fUML_Kernel_Enumeration_DataType, gen_fUML_Kernel_EnumerationLiteral_InstanceSpecification, gen_fUML_Kernel_Class_BehavioredClassifier, gen_fUML_Kernel_LiteralString_LiteralSpecification, gen_fUML_Kernel_LiteralUnlimitedNatural_LiteralSpecification, gen_fUML_IntermediateActivities_ObjectFlow_ActivityEdge, gen_fUML_IntermediateActivities_ActivityEdge_RedefinableElement, gen_fUML_IntermediateActivities_Activity_Behavior, gen_fUML_IntermediateActivities_ActivityNode_RedefinableElement, gen_fUML_IntermediateActivities_ObjectNode_IntermediateActivities_ActivityNode, gen_fUML_IntermediateActivities_ObjectNode_Kernel_TypedElement, gen_fUML_IntermediateActivities_MergeNode_ControlNode, gen_fUML_IntermediateActivities_ControlNode_ActivityNode, gen_fUML_IntermediateActivities_JoinNode_ControlNode, gen_fUML_IntermediateActivities_InitialNode_ControlNode, gen_fUML_IntermediateActivities_FinalNode_ControlNode, gen_fUML_IntermediateActivities_ForkNode_ControlNode, gen_fUML_IntermediateActivities_ControlFlow_ActivityEdge, gen_fUML_IntermediateActivities_ActivityFinalNode_FinalNode, gen_fUML_IntermediateActivities_ActivityParameterNode_ObjectNode, gen_fUML_CompleteStructuredActivities_LoopNode_StructuredActivityNode, gen_fUML_IntermediateActivities_DecisionNode_ControlNode, gen_fUML_CompleteStructuredActivities_ExecutableNode_ActivityNode, gen_fUML_CompleteStructuredActivities_Clause_Element, gen_fUML_CompleteStructuredActivities_ConditionalNode_StructuredActivityNode, gen_fUML_CompleteStructuredActivities_StructuredActivityNode_Action, gen_fUML_ExtraStructuredActivities_ExpansionNode_ObjectNode, gen_fUML_ExtraStructuredActivities_ExpansionRegion_StructuredActivityNode, gen_fUML_IntermediateActions_StructuralFeatureAction_Action, gen_fUML_IntermediateActions_ValueSpecificationAction_Action, gen_fUML_IntermediateActions_WriteLinkAction_LinkAction, gen_fUML_IntermediateActions_LinkAction_Action, gen_fUML_IntermediateActions_LinkEndData_Element, gen_fUML_IntermediateActions_TestIdentityAction_Action, gen_fUML_IntermediateActions_RemoveStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fUML_IntermediateActions_ReadLinkAction_LinkAction, gen_fUML_IntermediateActions_ReadSelfAction_Action, gen_fUML_IntermediateActions_ReadStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_LinkEndCreationData_LinkEndData, gen_fUML_IntermediateActions_LinkEndDestructionData_LinkEndData, gen_fUML_IntermediateActions_ClearAssociationAction_Action, gen_fUML_IntermediateActions_WriteStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_ClearStructuralFeatureAction_StructuralFeatureAction, gen_fUML_IntermediateActions_CreateLinkAction_WriteLinkAction, gen_fUML_IntermediateActions_CreateObjectAction_Action, gen_fUML_IntermediateActions_AddStructuralFeatureValueAction_WriteStructuralFeatureAction, gen_fUML_IntermediateActions_DestroyLinkAction_WriteLinkAction, gen_fUML_IntermediateActions_DestroyObjectAction_Action, gen_fUML_CompleteActions_ReadExtentAction_Action, gen_fUML_CompleteActions_StartClassifierBehaviorAction_Action, gen_fUML_CompleteActions_StartObjectBehaviorAction_CallAction, gen_fUML_CompleteActions_ReduceAction_Action, gen_fUML_CompleteActions_AcceptEventAction_Action, gen_fUML_CompleteActions_ReadIsClassifiedObjectAction_Action, gen_fUML_CompleteActions_ReclassifyObjectAction_Action, gen_fUML_BasicActions_InvocationAction_Action, gen_fUML_BasicActions_SendSignalAction_InvocationAction, gen_fUML_BasicActions_Action_ExecutableNode, gen_fUML_BasicActions_InputPin_Pin, gen_fUML_BasicActions_Pin_IntermediateActivities_ObjectNode, gen_fUML_BasicActions_Pin_Kernel_MultiplicityElement, gen_fUML_BasicActions_CallAction_InvocationAction, gen_fUML_Kernel_StructuredValue_Value, gen_fUML_BasicActions_CallBehaviorAction_CallAction, gen_fUML_BasicActions_CallOperationAction_CallAction, gen_fUML_BasicActions_OutputPin_Pin, gen_fUML_Kernel_Reference_StructuredValue, gen_fUML_Kernel_Object_ExtensionalValue, gen_fUML_Kernel_UnlimitedNaturalValue_PrimitiveValue, gen_fUML_Kernel_PrimitiveValue_Value, gen_fUML_Kernel_StringValue_PrimitiveValue, gen_fUML_Kernel_IntegerValue_PrimitiveValue, gen_fUML_Kernel_EnumerationValue_Value, gen_fUML_Kernel_ExtensionalValue_CompoundValue, gen_fUML_Kernel_CompoundValue_StructuredValue, gen_fUML_Kernel_Link_ExtensionalValue, gen_fUML_Kernel_Value_SemanticVisitor, gen_fUML_Kernel_DataValue_CompoundValue, gen_fUML_Kernel_BooleanValue_PrimitiveValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)