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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="aggregate"),
			EnumerationLiteral(name="composite")
    }
)

CallConcurrencyKind: Enumeration = Enumeration(
    name="CallConcurrencyKind",
    literals={
            EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="guarded"),
			EnumerationLiteral(name="concurrent")
    }
)

ChangeableKind: Enumeration = Enumeration(
    name="ChangeableKind",
    literals={
            EnumerationLiteral(name="changeable"),
			EnumerationLiteral(name="frozen"),
			EnumerationLiteral(name="addOnly")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="package")
    }
)

OrderingKind: Enumeration = Enumeration(
    name="OrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered")
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

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="shallowHistory")
    }
)

# Classes
foundation_data_types_Multiplicity = Class(name="foundation::data::types::Multiplicity")
MultiplicityRange = Class(name="MultiplicityRange")
foundation_data_types_MultiplicityRange = Class(name="foundation::data::types::MultiplicityRange")
Multiplicity = Class(name="Multiplicity")
foundation_data_types_ActionExpression = Class(name="foundation::data::types::ActionExpression")
foundation_data_types_IterationExpression = Class(name="foundation::data::types::IterationExpression")
foundation_data_types_TimeExpression = Class(name="foundation::data::types::TimeExpression")
foundation_data_types_ArgListsExpression = Class(name="foundation::data::types::ArgListsExpression")
foundation_core_Element = Class(name="foundation::core::Element", is_abstract=True)
foundation_core_ModelElement = Class(name="foundation::core::ModelElement", is_abstract=True)
Element = Class(name="Element")
foundation_data_types_Expression = Class(name="foundation::data::types::Expression")
foundation_data_types_BooleanExpression = Class(name="foundation::data::types::BooleanExpression")
Expression = Class(name="Expression")
foundation_data_types_TypeExpression = Class(name="foundation::data::types::TypeExpression")
foundation_data_types_MappingExpression = Class(name="foundation::data::types::MappingExpression")
foundation_data_types_ProcedureExpression = Class(name="foundation::data::types::ProcedureExpression")
foundation_data_types_ObjectSetExpression = Class(name="foundation::data::types::ObjectSetExpression")
PresentationElement = Class(name="PresentationElement")
Flow = Class(name="Flow")
Comment = Class(name="Comment")
ElementResidence = Class(name="ElementResidence")
Namespace = Class(name="Namespace")
Dependency = Class(name="Dependency")
Constraint = Class(name="Constraint")
StateMachine = Class(name="StateMachine")
foundation_core_GeneralizableElement = Class(name="foundation::core::GeneralizableElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
Generalization = Class(name="Generalization")
TemplateParameter = Class(name="TemplateParameter")
Stereotype = Class(name="Stereotype")
TaggedValue = Class(name="TaggedValue")
StructuralFeature = Class(name="StructuralFeature")
Parameter_ = Class(name="Parameter")
AssociationEnd = Class(name="AssociationEnd")
CreateAction = Class(name="CreateAction")
Collaboration = Class(name="Collaboration")
foundation_core_Namespace = Class(name="foundation::core::Namespace", is_abstract=True)
foundation_core_Classifier = Class(name="foundation::core::Classifier", is_abstract=True)
core_GeneralizableElement = Class(name="core::GeneralizableElement")
core_Namespace = Class(name="core::Namespace")
Feature = Class(name="Feature")
foundation_core_StructuralFeature = Class(name="foundation::core::StructuralFeature", is_abstract=True)
foundation_core_AssociationEnd = Class(name="foundation::core::AssociationEnd")
foundation_core_Class = Class(name="foundation::core::Class")
Classifier = Class(name="Classifier")
foundation_core_DataType = Class(name="foundation::core::DataType")
foundation_core_Feature = Class(name="foundation::core::Feature", is_abstract=True)
Attribute = Class(name="Attribute")
foundation_core_Interface = Class(name="foundation::core::Interface")
foundation_core_Constraint = Class(name="foundation::core::Constraint")
BooleanExpression = Class(name="BooleanExpression")
Association = Class(name="Association")
foundation_core_Attribute = Class(name="foundation::core::Attribute")
AssociationEndRole = Class(name="AssociationEndRole")
foundation_core_BehavioralFeature = Class(name="foundation::core::BehavioralFeature", is_abstract=True)
Signal = Class(name="Signal")
foundation_core_Relationship = Class(name="foundation::core::Relationship", is_abstract=True)
foundation_core_Association = Class(name="foundation::core::Association")
core_Relationship = Class(name="core::Relationship")
CallAction = Class(name="CallAction")
CallEvent = Class(name="CallEvent")
foundation_core_Parameter = Class(name="foundation::core::Parameter")
foundation_core_Operation = Class(name="foundation::core::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
Method_ = Class(name="Method")
Operation = Class(name="Operation")
foundation_core_Generalization = Class(name="foundation::core::Generalization")
Relationship = Class(name="Relationship")
GeneralizableElement = Class(name="GeneralizableElement")
foundation_core_AssociationClass = Class(name="foundation::core::AssociationClass")
core_Class = Class(name="core::Class")
core_Association = Class(name="core::Association")
foundation_core_Dependency = Class(name="foundation::core::Dependency")
foundation_core_Method = Class(name="foundation::core::Method")
ProcedureExpression = Class(name="ProcedureExpression")
MappingExpression = Class(name="MappingExpression")
foundation_core_PresentationElement = Class(name="foundation::core::PresentationElement", is_abstract=True)
foundation_core_Usage = Class(name="foundation::core::Usage")
foundation_core_Binding = Class(name="foundation::core::Binding")
TemplateArgument = Class(name="TemplateArgument")
foundation_core_Component = Class(name="foundation::core::Component")
Node = Class(name="Node")
foundation_core_Abstraction = Class(name="foundation::core::Abstraction")
foundation_core_Node = Class(name="foundation::core::Node")
Component = Class(name="Component")
foundation_core_Permission = Class(name="foundation::core::Permission")
foundation_core_Comment = Class(name="foundation::core::Comment")
foundation_core_Flow = Class(name="foundation::core::Flow")
Artifact = Class(name="Artifact")
foundation_core_TemplateParameter = Class(name="foundation::core::TemplateParameter")
foundation_core_Primitive = Class(name="foundation::core::Primitive")
DataType = Class(name="DataType")
foundation_core_Enumeration = Class(name="foundation::core::Enumeration")
EnumerationLiteral = Class(name="EnumerationLiteral")
foundation_core_EnumerationLiteral = Class(name="foundation::core::EnumerationLiteral")
foundation_core_ElementResidence = Class(name="foundation::core::ElementResidence")
TagDefinition = Class(name="TagDefinition")
foundation_core_TagDefinition = Class(name="foundation::core::TagDefinition")
Enumeration_ = Class(name="Enumeration")
foundation_core_Stereotype = Class(name="foundation::core::Stereotype")
foundation_core_ProgrammingLanguageDataType = Class(name="foundation::core::ProgrammingLanguageDataType")
TypeExpression = Class(name="TypeExpression")
foundation_core_Artifact = Class(name="foundation::core::Artifact")
foundation_core_TemplateArgument = Class(name="foundation::core::TemplateArgument")
Binding = Class(name="Binding")
foundation_core_TaggedValue = Class(name="foundation::core::TaggedValue")

# foundation_data_types_Multiplicity class attributes and methods

# MultiplicityRange class attributes and methods

# foundation_data_types_MultiplicityRange class attributes and methods
foundation_data_types_MultiplicityRange_lower: Property = Property(name="lower", type=StringType)
foundation_data_types_MultiplicityRange_upper: Property = Property(name="upper", type=StringType)
foundation_data_types_MultiplicityRange.attributes={foundation_data_types_MultiplicityRange_lower, foundation_data_types_MultiplicityRange_upper}

# Multiplicity class attributes and methods

# foundation_data_types_ActionExpression class attributes and methods

# foundation_data_types_IterationExpression class attributes and methods

# foundation_data_types_TimeExpression class attributes and methods

# foundation_data_types_ArgListsExpression class attributes and methods

# foundation_core_Element class attributes and methods

# foundation_core_ModelElement class attributes and methods
foundation_core_ModelElement_name: Property = Property(name="name", type=StringType)
foundation_core_ModelElement_visibility: Property = Property(name="visibility", type=StringType)
foundation_core_ModelElement_isSpecification: Property = Property(name="isSpecification", type=StringType)
foundation_core_ModelElement.attributes={foundation_core_ModelElement_name, foundation_core_ModelElement_visibility, foundation_core_ModelElement_isSpecification}

# Element class attributes and methods

# foundation_data_types_Expression class attributes and methods
foundation_data_types_Expression_language: Property = Property(name="language", type=StringType)
foundation_data_types_Expression_body: Property = Property(name="body", type=StringType)
foundation_data_types_Expression.attributes={foundation_data_types_Expression_language, foundation_data_types_Expression_body}

# foundation_data_types_BooleanExpression class attributes and methods

# Expression class attributes and methods

# foundation_data_types_TypeExpression class attributes and methods

# foundation_data_types_MappingExpression class attributes and methods

# foundation_data_types_ProcedureExpression class attributes and methods

# foundation_data_types_ObjectSetExpression class attributes and methods

# PresentationElement class attributes and methods

# Flow class attributes and methods

# Comment class attributes and methods

# ElementResidence class attributes and methods

# Namespace class attributes and methods

# Dependency class attributes and methods

# Constraint class attributes and methods

# StateMachine class attributes and methods

# foundation_core_GeneralizableElement class attributes and methods
foundation_core_GeneralizableElement_isRoot: Property = Property(name="isRoot", type=StringType)
foundation_core_GeneralizableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
foundation_core_GeneralizableElement_isAbstract: Property = Property(name="isAbstract", type=StringType)
foundation_core_GeneralizableElement.attributes={foundation_core_GeneralizableElement_isRoot, foundation_core_GeneralizableElement_isAbstract, foundation_core_GeneralizableElement_isLeaf}

# ModelElement class attributes and methods

# Generalization class attributes and methods

# TemplateParameter class attributes and methods

# Stereotype class attributes and methods

# TaggedValue class attributes and methods

# StructuralFeature class attributes and methods

# Parameter class attributes and methods

# AssociationEnd class attributes and methods

# CreateAction class attributes and methods

# Collaboration class attributes and methods

# foundation_core_Namespace class attributes and methods

# foundation_core_Classifier class attributes and methods

# core_GeneralizableElement class attributes and methods

# core_Namespace class attributes and methods

# Feature class attributes and methods

# foundation_core_StructuralFeature class attributes and methods
foundation_core_StructuralFeature_changeability: Property = Property(name="changeability", type=StringType)
foundation_core_StructuralFeature_targetScope: Property = Property(name="targetScope", type=StringType)
foundation_core_StructuralFeature_ordering: Property = Property(name="ordering", type=StringType)
foundation_core_StructuralFeature.attributes={foundation_core_StructuralFeature_changeability, foundation_core_StructuralFeature_ordering, foundation_core_StructuralFeature_targetScope}

# foundation_core_AssociationEnd class attributes and methods
foundation_core_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=StringType)
foundation_core_AssociationEnd_ordering: Property = Property(name="ordering", type=StringType)
foundation_core_AssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
foundation_core_AssociationEnd_targetScope: Property = Property(name="targetScope", type=StringType)
foundation_core_AssociationEnd_changeability: Property = Property(name="changeability", type=StringType)
foundation_core_AssociationEnd.attributes={foundation_core_AssociationEnd_isNavigable, foundation_core_AssociationEnd_targetScope, foundation_core_AssociationEnd_aggregation, foundation_core_AssociationEnd_ordering, foundation_core_AssociationEnd_changeability}

# foundation_core_Class class attributes and methods
foundation_core_Class_isActive: Property = Property(name="isActive", type=StringType)
foundation_core_Class.attributes={foundation_core_Class_isActive}

# Classifier class attributes and methods

# foundation_core_DataType class attributes and methods

# foundation_core_Feature class attributes and methods
foundation_core_Feature_ownerScope: Property = Property(name="ownerScope", type=StringType)
foundation_core_Feature.attributes={foundation_core_Feature_ownerScope}

# Attribute class attributes and methods

# foundation_core_Interface class attributes and methods

# foundation_core_Constraint class attributes and methods

# BooleanExpression class attributes and methods

# Association class attributes and methods

# foundation_core_Attribute class attributes and methods

# AssociationEndRole class attributes and methods

# foundation_core_BehavioralFeature class attributes and methods
foundation_core_BehavioralFeature_isQuery: Property = Property(name="isQuery", type=StringType)
foundation_core_BehavioralFeature.attributes={foundation_core_BehavioralFeature_isQuery}

# Signal class attributes and methods

# foundation_core_Relationship class attributes and methods

# foundation_core_Association class attributes and methods

# core_Relationship class attributes and methods

# CallAction class attributes and methods

# CallEvent class attributes and methods

# foundation_core_Parameter class attributes and methods
foundation_core_Parameter_kind: Property = Property(name="kind", type=StringType)
foundation_core_Parameter.attributes={foundation_core_Parameter_kind}

# foundation_core_Operation class attributes and methods
foundation_core_Operation_concurrency: Property = Property(name="concurrency", type=StringType)
foundation_core_Operation_isRoot: Property = Property(name="isRoot", type=StringType)
foundation_core_Operation_isLeaf: Property = Property(name="isLeaf", type=StringType)
foundation_core_Operation_isAbstract: Property = Property(name="isAbstract", type=StringType)
foundation_core_Operation_specification: Property = Property(name="specification", type=StringType)
foundation_core_Operation.attributes={foundation_core_Operation_isRoot, foundation_core_Operation_isLeaf, foundation_core_Operation_specification, foundation_core_Operation_isAbstract, foundation_core_Operation_concurrency}

# BehavioralFeature class attributes and methods

# Method class attributes and methods

# Operation class attributes and methods

# foundation_core_Generalization class attributes and methods
foundation_core_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
foundation_core_Generalization.attributes={foundation_core_Generalization_discriminator}

# Relationship class attributes and methods

# GeneralizableElement class attributes and methods

# foundation_core_AssociationClass class attributes and methods

# core_Class class attributes and methods

# core_Association class attributes and methods

# foundation_core_Dependency class attributes and methods

# foundation_core_Method class attributes and methods

# ProcedureExpression class attributes and methods

# MappingExpression class attributes and methods

# foundation_core_PresentationElement class attributes and methods

# foundation_core_Usage class attributes and methods

# foundation_core_Binding class attributes and methods

# TemplateArgument class attributes and methods

# foundation_core_Component class attributes and methods

# Node class attributes and methods

# foundation_core_Abstraction class attributes and methods

# foundation_core_Node class attributes and methods

# Component class attributes and methods

# foundation_core_Permission class attributes and methods

# foundation_core_Comment class attributes and methods
foundation_core_Comment_body: Property = Property(name="body", type=StringType)
foundation_core_Comment.attributes={foundation_core_Comment_body}

# foundation_core_Flow class attributes and methods

# Artifact class attributes and methods

# foundation_core_TemplateParameter class attributes and methods

# foundation_core_Primitive class attributes and methods

# DataType class attributes and methods

# foundation_core_Enumeration class attributes and methods

# EnumerationLiteral class attributes and methods

# foundation_core_EnumerationLiteral class attributes and methods

# foundation_core_ElementResidence class attributes and methods
foundation_core_ElementResidence_visibility: Property = Property(name="visibility", type=StringType)
foundation_core_ElementResidence.attributes={foundation_core_ElementResidence_visibility}

# TagDefinition class attributes and methods

# foundation_core_TagDefinition class attributes and methods
foundation_core_TagDefinition_tagType: Property = Property(name="tagType", type=StringType)
foundation_core_TagDefinition.attributes={foundation_core_TagDefinition_tagType}

# Enumeration class attributes and methods

# foundation_core_Stereotype class attributes and methods
foundation_core_Stereotype_icon: Property = Property(name="icon", type=StringType)
foundation_core_Stereotype_baseClass: Property = Property(name="baseClass", type=StringType)
foundation_core_Stereotype.attributes={foundation_core_Stereotype_icon, foundation_core_Stereotype_baseClass}

# foundation_core_ProgrammingLanguageDataType class attributes and methods

# TypeExpression class attributes and methods

# foundation_core_Artifact class attributes and methods

# foundation_core_TemplateArgument class attributes and methods

# Binding class attributes and methods

# foundation_core_TaggedValue class attributes and methods
foundation_core_TaggedValue_dataValue: Property = Property(name="dataValue", type=StringType)
foundation_core_TaggedValue.attributes={foundation_core_TaggedValue_dataValue}

# Relationships
range0: BinaryAssociation = BinaryAssociation(
    name="range0",
    ends={
        Property(name="data_types", type=foundation_data_types_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="MultiplicityRange", type=MultiplicityRange, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicity1: BinaryAssociation = BinaryAssociation(
    name="multiplicity1",
    ends={
        Property(name="data_types2", type=foundation_data_types_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="Multiplicity", type=Multiplicity, multiplicity=Multiplicity(1, 1))
    }
)
supplierDependency8: BinaryAssociation = BinaryAssociation(
    name="supplierDependency8",
    ends={
        Property(name="core10", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Dependency9", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
presentation11: BinaryAssociation = BinaryAssociation(
    name="presentation11",
    ends={
        Property(name="core12", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="PresentationElement", type=PresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
targetFlow13: BinaryAssociation = BinaryAssociation(
    name="targetFlow13",
    ends={
        Property(name="core14", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Flow", type=Flow, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFlow15: BinaryAssociation = BinaryAssociation(
    name="sourceFlow15",
    ends={
        Property(name="core17", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Flow16", type=Flow, multiplicity=Multiplicity(0, 9999))
    }
)
comment18: BinaryAssociation = BinaryAssociation(
    name="comment18",
    ends={
        Property(name="core19", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Comment", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
elementResidence20: BinaryAssociation = BinaryAssociation(
    name="elementResidence20",
    ends={
        Property(name="core21", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementResidence", type=ElementResidence, multiplicity=Multiplicity(0, 9999))
    }
)
namespace3: BinaryAssociation = BinaryAssociation(
    name="namespace3",
    ends={
        Property(name="core", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency4: BinaryAssociation = BinaryAssociation(
    name="clientDependency4",
    ends={
        Property(name="core5", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Dependency", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
constraint6: BinaryAssociation = BinaryAssociation(
    name="constraint6",
    ends={
        Property(name="core7", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Constraint", type=Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
referenceTag28: BinaryAssociation = BinaryAssociation(
    name="referenceTag28",
    ends={
        Property(name="core30", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TaggedValue29", type=TaggedValue, multiplicity=Multiplicity(0, 9999))
    }
)
behavior31: BinaryAssociation = BinaryAssociation(
    name="behavior31",
    ends={
        Property(name="behavioral_elements.ecorestate_machines", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine", type=StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
generalization32: BinaryAssociation = BinaryAssociation(
    name="generalization32",
    ends={
        Property(name="core33", type=foundation_core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Generalization", type=Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
specialization34: BinaryAssociation = BinaryAssociation(
    name="specialization34",
    ends={
        Property(name="core36", type=foundation_core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Generalization35", type=Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
templateParameter22: BinaryAssociation = BinaryAssociation(
    name="templateParameter22",
    ends={
        Property(name="core23", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TemplateParameter", type=TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype24: BinaryAssociation = BinaryAssociation(
    name="stereotype24",
    ends={
        Property(name="core25", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Stereotype", type=Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
taggedValue26: BinaryAssociation = BinaryAssociation(
    name="taggedValue26",
    ends={
        Property(name="core27", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TaggedValue", type=TaggedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedFeature41: BinaryAssociation = BinaryAssociation(
    name="typedFeature41",
    ends={
        Property(name="core42", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="StructuralFeature", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
typedParameter43: BinaryAssociation = BinaryAssociation(
    name="typedParameter43",
    ends={
        Property(name="core44", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
association45: BinaryAssociation = BinaryAssociation(
    name="association45",
    ends={
        Property(name="core46", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationEnd", type=AssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
specifiedEnd47: BinaryAssociation = BinaryAssociation(
    name="specifiedEnd47",
    ends={
        Property(name="core49", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationEnd48", type=AssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeRange50: BinaryAssociation = BinaryAssociation(
    name="powertypeRange50",
    ends={
        Property(name="core52", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Generalization51", type=Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
createAction53: BinaryAssociation = BinaryAssociation(
    name="createAction53",
    ends={
        Property(name="behavioral_elements.ecorecommon_behavior", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="CreateAction", type=CreateAction, multiplicity=Multiplicity(0, 9999))
    }
)
collaboration54: BinaryAssociation = BinaryAssociation(
    name="collaboration54",
    ends={
        Property(name="behavioral_elements.ecorecollaborations", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Collaboration", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement37: BinaryAssociation = BinaryAssociation(
    name="ownedElement37",
    ends={
        Property(name="core38", type=foundation_core_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature39: BinaryAssociation = BinaryAssociation(
    name="feature39",
    ends={
        Property(name="core40", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Feature", type=Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity57: BinaryAssociation = BinaryAssociation(
    name="multiplicity57",
    ends={
        Property(name="Multiplicity58", type=foundation_core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_StructuralFeature", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="core61", type=foundation_core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier60", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner55: BinaryAssociation = BinaryAssociation(
    name="owner55",
    ends={
        Property(name="core56", type=foundation_core_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
qualifier66: BinaryAssociation = BinaryAssociation(
    name="qualifier66",
    ends={
        Property(name="core67", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant68: BinaryAssociation = BinaryAssociation(
    name="participant68",
    ends={
        Property(name="core70", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier69", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specification71: BinaryAssociation = BinaryAssociation(
    name="specification71",
    ends={
        Property(name="core73", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier72", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
body74: BinaryAssociation = BinaryAssociation(
    name="body74",
    ends={
        Property(name="BooleanExpression", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Constraint", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrainedElement75: BinaryAssociation = BinaryAssociation(
    name="constrainedElement75",
    ends={
        Property(name="core77", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement76", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity62: BinaryAssociation = BinaryAssociation(
    name="multiplicity62",
    ends={
        Property(name="Multiplicity63", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_AssociationEnd", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
association64: BinaryAssociation = BinaryAssociation(
    name="association64",
    ends={
        Property(name="core65", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Association", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
initialValue84: BinaryAssociation = BinaryAssociation(
    name="initialValue84",
    ends={
        Property(name="Expression", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Attribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associationEnd85: BinaryAssociation = BinaryAssociation(
    name="associationEnd85",
    ends={
        Property(name="core87", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationEnd86", type=AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
associationEndRole88: BinaryAssociation = BinaryAssociation(
    name="associationEndRole88",
    ends={
        Property(name="behavioral_elements.ecorecollaborations89", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationEndRole", type=AssociationEndRole, multiplicity=Multiplicity(0, 9999))
    }
)
parameter90: BinaryAssociation = BinaryAssociation(
    name="parameter90",
    ends={
        Property(name="core92", type=foundation_core_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter91", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainedStereotype78: BinaryAssociation = BinaryAssociation(
    name="constrainedStereotype78",
    ends={
        Property(name="core80", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Stereotype79", type=Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
connection81: BinaryAssociation = BinaryAssociation(
    name="connection81",
    ends={
        Property(name="core83", type=foundation_core_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="AssociationEnd82", type=AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
method95: BinaryAssociation = BinaryAssociation(
    name="method95",
    ends={
        Property(name="core96", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Method", type=Method_, multiplicity=Multiplicity(0, 9999))
    }
)
callAction97: BinaryAssociation = BinaryAssociation(
    name="callAction97",
    ends={
        Property(name="behavioral_elements.ecorecommon_behavior98", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CallAction", type=CallAction, multiplicity=Multiplicity(0, 9999))
    }
)
occurrence99: BinaryAssociation = BinaryAssociation(
    name="occurrence99",
    ends={
        Property(name="behavioral_elements.ecorestate_machines100", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="CallEvent", type=CallEvent, multiplicity=Multiplicity(0, 9999))
    }
)
collaboration101: BinaryAssociation = BinaryAssociation(
    name="collaboration101",
    ends={
        Property(name="behavioral_elements.ecorecollaborations103", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Collaboration102", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue104: BinaryAssociation = BinaryAssociation(
    name="defaultValue104",
    ends={
        Property(name="Expression105", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Parameter", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
raisedSignal93: BinaryAssociation = BinaryAssociation(
    name="raisedSignal93",
    ends={
        Property(name="behavioral_elements.ecorecommon_behavior94", type=foundation_core_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Signal", type=Signal, multiplicity=Multiplicity(0, 9999))
    }
)
behavioralFeature106: BinaryAssociation = BinaryAssociation(
    name="behavioralFeature106",
    ends={
        Property(name="core107", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="BehavioralFeature", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
specification112: BinaryAssociation = BinaryAssociation(
    name="specification112",
    ends={
        Property(name="core113", type=foundation_core_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
child114: BinaryAssociation = BinaryAssociation(
    name="child114",
    ends={
        Property(name="core115", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizableElement", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
parent116: BinaryAssociation = BinaryAssociation(
    name="parent116",
    ends={
        Property(name="core118", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizableElement117", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
powertype119: BinaryAssociation = BinaryAssociation(
    name="powertype119",
    ends={
        Property(name="core121", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier120", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
client122: BinaryAssociation = BinaryAssociation(
    name="client122",
    ends={
        Property(name="core124", type=foundation_core_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement123", type=ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
type108: BinaryAssociation = BinaryAssociation(
    name="type108",
    ends={
        Property(name="core110", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier109", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
body111: BinaryAssociation = BinaryAssociation(
    name="body111",
    ends={
        Property(name="ProcedureExpression", type=foundation_core_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Method", type=ProcedureExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapping128: BinaryAssociation = BinaryAssociation(
    name="mapping128",
    ends={
        Property(name="MappingExpression", type=foundation_core_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Abstraction", type=MappingExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subject129: BinaryAssociation = BinaryAssociation(
    name="subject129",
    ends={
        Property(name="core131", type=foundation_core_PresentationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement130", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
argument132: BinaryAssociation = BinaryAssociation(
    name="argument132",
    ends={
        Property(name="core133", type=foundation_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="TemplateArgument", type=TemplateArgument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
deploymentLocation134: BinaryAssociation = BinaryAssociation(
    name="deploymentLocation134",
    ends={
        Property(name="core135", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Node", type=Node, multiplicity=Multiplicity(0, 9999))
    }
)
supplier125: BinaryAssociation = BinaryAssociation(
    name="supplier125",
    ends={
        Property(name="core127", type=foundation_core_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement126", type=ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
deployedComponent141: BinaryAssociation = BinaryAssociation(
    name="deployedComponent141",
    ends={
        Property(name="core142", type=foundation_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="Component", type=Component, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement143: BinaryAssociation = BinaryAssociation(
    name="annotatedElement143",
    ends={
        Property(name="core145", type=foundation_core_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement144", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
target146: BinaryAssociation = BinaryAssociation(
    name="target146",
    ends={
        Property(name="core148", type=foundation_core_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement147", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
source149: BinaryAssociation = BinaryAssociation(
    name="source149",
    ends={
        Property(name="core151", type=foundation_core_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement150", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
residentElement136: BinaryAssociation = BinaryAssociation(
    name="residentElement136",
    ends={
        Property(name="core138", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementResidence137", type=ElementResidence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementation139: BinaryAssociation = BinaryAssociation(
    name="implementation139",
    ends={
        Property(name="core140", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="Artifact", type=Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
container155: BinaryAssociation = BinaryAssociation(
    name="container155",
    ends={
        Property(name="Component156", type=Component, multiplicity=Multiplicity(1, 1)),
        Property(name="core157", type=foundation_core_ElementResidence, multiplicity=Multiplicity(1, 1))
    }
)
defaultElement158: BinaryAssociation = BinaryAssociation(
    name="defaultElement158",
    ends={
        Property(name="ModelElement159", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateParameter", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
template160: BinaryAssociation = BinaryAssociation(
    name="template160",
    ends={
        Property(name="core162", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement161", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
parameter163: BinaryAssociation = BinaryAssociation(
    name="parameter163",
    ends={
        Property(name="ModelElement165", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateParameter164", type=ModelElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literal166: BinaryAssociation = BinaryAssociation(
    name="literal166",
    ends={
        Property(name="core167", type=foundation_core_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationLiteral", type=EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
resident152: BinaryAssociation = BinaryAssociation(
    name="resident152",
    ends={
        Property(name="core154", type=foundation_core_ElementResidence, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement153", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
definedTag170: BinaryAssociation = BinaryAssociation(
    name="definedTag170",
    ends={
        Property(name="core171", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="TagDefinition", type=TagDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedElement172: BinaryAssociation = BinaryAssociation(
    name="extendedElement172",
    ends={
        Property(name="core174", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement173", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeConstraint175: BinaryAssociation = BinaryAssociation(
    name="stereotypeConstraint175",
    ends={
        Property(name="core177", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="Constraint176", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity178: BinaryAssociation = BinaryAssociation(
    name="multiplicity178",
    ends={
        Property(name="Multiplicity179", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TagDefinition", type=Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner180: BinaryAssociation = BinaryAssociation(
    name="owner180",
    ends={
        Property(name="core182", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="Stereotype181", type=Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
typedValue183: BinaryAssociation = BinaryAssociation(
    name="typedValue183",
    ends={
        Property(name="core185", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TaggedValue184", type=TaggedValue, multiplicity=Multiplicity(0, 9999))
    }
)
enumeration168: BinaryAssociation = BinaryAssociation(
    name="enumeration168",
    ends={
        Property(name="core169", type=foundation_core_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Enumeration", type=Enumeration_, multiplicity=Multiplicity(1, 1))
    }
)
type189: BinaryAssociation = BinaryAssociation(
    name="type189",
    ends={
        Property(name="core191", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="TagDefinition190", type=TagDefinition, multiplicity=Multiplicity(1, 1))
    }
)
referenceValue192: BinaryAssociation = BinaryAssociation(
    name="referenceValue192",
    ends={
        Property(name="core194", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement193", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
expression195: BinaryAssociation = BinaryAssociation(
    name="expression195",
    ends={
        Property(name="TypeExpression", type=foundation_core_ProgrammingLanguageDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_ProgrammingLanguageDataType", type=TypeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementationLocation196: BinaryAssociation = BinaryAssociation(
    name="implementationLocation196",
    ends={
        Property(name="core198", type=foundation_core_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="Component197", type=Component, multiplicity=Multiplicity(0, 9999))
    }
)
binding199: BinaryAssociation = BinaryAssociation(
    name="binding199",
    ends={
        Property(name="core200", type=foundation_core_TemplateArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="Binding", type=Binding, multiplicity=Multiplicity(1, 1))
    }
)
modelElement186: BinaryAssociation = BinaryAssociation(
    name="modelElement186",
    ends={
        Property(name="core188", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElement187", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
modelElement201: BinaryAssociation = BinaryAssociation(
    name="modelElement201",
    ends={
        Property(name="ModelElement202", type=foundation_core_TemplateArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateArgument", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_foundation_data_types_ActionExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ActionExpression)
gen_foundation_data_types_IterationExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_IterationExpression)
gen_foundation_data_types_TimeExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_TimeExpression)
gen_foundation_data_types_ArgListsExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ArgListsExpression)
gen_foundation_core_ModelElement_Element = Generalization(general=Element, specific=foundation_core_ModelElement)
gen_foundation_data_types_BooleanExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_BooleanExpression)
gen_foundation_data_types_TypeExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_TypeExpression)
gen_foundation_data_types_MappingExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_MappingExpression)
gen_foundation_data_types_ProcedureExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ProcedureExpression)
gen_foundation_data_types_ObjectSetExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ObjectSetExpression)
gen_foundation_core_GeneralizableElement_ModelElement = Generalization(general=ModelElement, specific=foundation_core_GeneralizableElement)
gen_foundation_core_Namespace_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Namespace)
gen_foundation_core_Classifier_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=foundation_core_Classifier)
gen_foundation_core_Classifier_core_Namespace = Generalization(general=core_Namespace, specific=foundation_core_Classifier)
gen_foundation_core_StructuralFeature_Feature = Generalization(general=Feature, specific=foundation_core_StructuralFeature)
gen_foundation_core_AssociationEnd_ModelElement = Generalization(general=ModelElement, specific=foundation_core_AssociationEnd)
gen_foundation_core_Class_Classifier = Generalization(general=Classifier, specific=foundation_core_Class)
gen_foundation_core_DataType_Classifier = Generalization(general=Classifier, specific=foundation_core_DataType)
gen_foundation_core_Feature_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Feature)
gen_foundation_core_Interface_Classifier = Generalization(general=Classifier, specific=foundation_core_Interface)
gen_foundation_core_Constraint_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Constraint)
gen_foundation_core_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=foundation_core_Attribute)
gen_foundation_core_BehavioralFeature_Feature = Generalization(general=Feature, specific=foundation_core_BehavioralFeature)
gen_foundation_core_Relationship_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Relationship)
gen_foundation_core_Association_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=foundation_core_Association)
gen_foundation_core_Association_core_Relationship = Generalization(general=core_Relationship, specific=foundation_core_Association)
gen_foundation_core_Parameter_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Parameter)
gen_foundation_core_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=foundation_core_Operation)
gen_foundation_core_Generalization_Relationship = Generalization(general=Relationship, specific=foundation_core_Generalization)
gen_foundation_core_AssociationClass_core_Class = Generalization(general=core_Class, specific=foundation_core_AssociationClass)
gen_foundation_core_AssociationClass_core_Association = Generalization(general=core_Association, specific=foundation_core_AssociationClass)
gen_foundation_core_Dependency_Relationship = Generalization(general=Relationship, specific=foundation_core_Dependency)
gen_foundation_core_Method_BehavioralFeature = Generalization(general=BehavioralFeature, specific=foundation_core_Method)
gen_foundation_core_Abstraction_Dependency = Generalization(general=Dependency, specific=foundation_core_Abstraction)
gen_foundation_core_PresentationElement_Element = Generalization(general=Element, specific=foundation_core_PresentationElement)
gen_foundation_core_Usage_Dependency = Generalization(general=Dependency, specific=foundation_core_Usage)
gen_foundation_core_Binding_Dependency = Generalization(general=Dependency, specific=foundation_core_Binding)
gen_foundation_core_Component_Classifier = Generalization(general=Classifier, specific=foundation_core_Component)
gen_foundation_core_Node_Classifier = Generalization(general=Classifier, specific=foundation_core_Node)
gen_foundation_core_Permission_Dependency = Generalization(general=Dependency, specific=foundation_core_Permission)
gen_foundation_core_Comment_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Comment)
gen_foundation_core_Flow_Relationship = Generalization(general=Relationship, specific=foundation_core_Flow)
gen_foundation_core_Primitive_DataType = Generalization(general=DataType, specific=foundation_core_Primitive)
gen_foundation_core_Enumeration_DataType = Generalization(general=DataType, specific=foundation_core_Enumeration)
gen_foundation_core_EnumerationLiteral_ModelElement = Generalization(general=ModelElement, specific=foundation_core_EnumerationLiteral)
gen_foundation_core_TagDefinition_ModelElement = Generalization(general=ModelElement, specific=foundation_core_TagDefinition)
gen_foundation_core_Stereotype_GeneralizableElement = Generalization(general=GeneralizableElement, specific=foundation_core_Stereotype)
gen_foundation_core_ProgrammingLanguageDataType_DataType = Generalization(general=DataType, specific=foundation_core_ProgrammingLanguageDataType)
gen_foundation_core_Artifact_Classifier = Generalization(general=Classifier, specific=foundation_core_Artifact)
gen_foundation_core_TaggedValue_ModelElement = Generalization(general=ModelElement, specific=foundation_core_TaggedValue)

# Domain Model
domain_model = DomainModel(
    name="foundation",
    types={foundation_data_types_Multiplicity, MultiplicityRange, foundation_data_types_MultiplicityRange, Multiplicity, foundation_data_types_ActionExpression, foundation_data_types_IterationExpression, foundation_data_types_TimeExpression, foundation_data_types_ArgListsExpression, foundation_core_Element, foundation_core_ModelElement, Element, foundation_data_types_Expression, foundation_data_types_BooleanExpression, Expression, foundation_data_types_TypeExpression, foundation_data_types_MappingExpression, foundation_data_types_ProcedureExpression, foundation_data_types_ObjectSetExpression, PresentationElement, Flow, Comment, ElementResidence, Namespace, Dependency, Constraint, StateMachine, foundation_core_GeneralizableElement, ModelElement, Generalization, TemplateParameter, Stereotype, TaggedValue, StructuralFeature, Parameter_, AssociationEnd, CreateAction, Collaboration, foundation_core_Namespace, foundation_core_Classifier, core_GeneralizableElement, core_Namespace, Feature, foundation_core_StructuralFeature, foundation_core_AssociationEnd, foundation_core_Class, Classifier, foundation_core_DataType, foundation_core_Feature, Attribute, foundation_core_Interface, foundation_core_Constraint, BooleanExpression, Association, foundation_core_Attribute, AssociationEndRole, foundation_core_BehavioralFeature, Signal, foundation_core_Relationship, foundation_core_Association, core_Relationship, CallAction, CallEvent, foundation_core_Parameter, foundation_core_Operation, BehavioralFeature, Method_, Operation, foundation_core_Generalization, Relationship, GeneralizableElement, foundation_core_AssociationClass, core_Class, core_Association, foundation_core_Dependency, foundation_core_Method, ProcedureExpression, MappingExpression, foundation_core_PresentationElement, foundation_core_Usage, foundation_core_Binding, TemplateArgument, foundation_core_Component, Node, foundation_core_Abstraction, foundation_core_Node, Component, foundation_core_Permission, foundation_core_Comment, foundation_core_Flow, Artifact, foundation_core_TemplateParameter, foundation_core_Primitive, DataType, foundation_core_Enumeration, EnumerationLiteral, foundation_core_EnumerationLiteral, foundation_core_ElementResidence, TagDefinition, foundation_core_TagDefinition, Enumeration_, foundation_core_Stereotype, foundation_core_ProgrammingLanguageDataType, TypeExpression, foundation_core_Artifact, foundation_core_TemplateArgument, Binding, foundation_core_TaggedValue, AggregationKind, CallConcurrencyKind, ChangeableKind, VisibilityKind, OrderingKind, ParameterDirectionKind, ScopeKind, PseudostateKind},
    associations={range0, multiplicity1, supplierDependency8, presentation11, targetFlow13, sourceFlow15, comment18, elementResidence20, namespace3, clientDependency4, constraint6, referenceTag28, behavior31, generalization32, specialization34, templateParameter22, stereotype24, taggedValue26, typedFeature41, typedParameter43, association45, specifiedEnd47, powertypeRange50, createAction53, collaboration54, ownedElement37, feature39, multiplicity57, type59, owner55, qualifier66, participant68, specification71, body74, constrainedElement75, multiplicity62, association64, initialValue84, associationEnd85, associationEndRole88, parameter90, constrainedStereotype78, connection81, method95, callAction97, occurrence99, collaboration101, defaultValue104, raisedSignal93, behavioralFeature106, specification112, child114, parent116, powertype119, client122, type108, body111, mapping128, subject129, argument132, deploymentLocation134, supplier125, deployedComponent141, annotatedElement143, target146, source149, residentElement136, implementation139, container155, defaultElement158, template160, parameter163, literal166, resident152, definedTag170, extendedElement172, stereotypeConstraint175, multiplicity178, owner180, typedValue183, enumeration168, type189, referenceValue192, expression195, implementationLocation196, binding199, modelElement186, modelElement201},
    generalizations={gen_foundation_data_types_ActionExpression_Expression, gen_foundation_data_types_IterationExpression_Expression, gen_foundation_data_types_TimeExpression_Expression, gen_foundation_data_types_ArgListsExpression_Expression, gen_foundation_core_ModelElement_Element, gen_foundation_data_types_BooleanExpression_Expression, gen_foundation_data_types_TypeExpression_Expression, gen_foundation_data_types_MappingExpression_Expression, gen_foundation_data_types_ProcedureExpression_Expression, gen_foundation_data_types_ObjectSetExpression_Expression, gen_foundation_core_GeneralizableElement_ModelElement, gen_foundation_core_Namespace_ModelElement, gen_foundation_core_Classifier_core_GeneralizableElement, gen_foundation_core_Classifier_core_Namespace, gen_foundation_core_StructuralFeature_Feature, gen_foundation_core_AssociationEnd_ModelElement, gen_foundation_core_Class_Classifier, gen_foundation_core_DataType_Classifier, gen_foundation_core_Feature_ModelElement, gen_foundation_core_Interface_Classifier, gen_foundation_core_Constraint_ModelElement, gen_foundation_core_Attribute_StructuralFeature, gen_foundation_core_BehavioralFeature_Feature, gen_foundation_core_Relationship_ModelElement, gen_foundation_core_Association_core_GeneralizableElement, gen_foundation_core_Association_core_Relationship, gen_foundation_core_Parameter_ModelElement, gen_foundation_core_Operation_BehavioralFeature, gen_foundation_core_Generalization_Relationship, gen_foundation_core_AssociationClass_core_Class, gen_foundation_core_AssociationClass_core_Association, gen_foundation_core_Dependency_Relationship, gen_foundation_core_Method_BehavioralFeature, gen_foundation_core_Abstraction_Dependency, gen_foundation_core_PresentationElement_Element, gen_foundation_core_Usage_Dependency, gen_foundation_core_Binding_Dependency, gen_foundation_core_Component_Classifier, gen_foundation_core_Node_Classifier, gen_foundation_core_Permission_Dependency, gen_foundation_core_Comment_ModelElement, gen_foundation_core_Flow_Relationship, gen_foundation_core_Primitive_DataType, gen_foundation_core_Enumeration_DataType, gen_foundation_core_EnumerationLiteral_ModelElement, gen_foundation_core_TagDefinition_ModelElement, gen_foundation_core_Stereotype_GeneralizableElement, gen_foundation_core_ProgrammingLanguageDataType_DataType, gen_foundation_core_Artifact_Classifier, gen_foundation_core_TaggedValue_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)