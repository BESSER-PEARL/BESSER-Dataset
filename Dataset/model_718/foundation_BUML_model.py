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
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return_")
    }
)

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
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

# Classes
foundation_data_types_BooleanExpression = Class(name="foundation_data_types_BooleanExpression")
Expression = Class(name="Expression")
foundation_data_types_TypeExpression = Class(name="foundation_data_types_TypeExpression")
foundation_data_types_MappingExpression = Class(name="foundation_data_types_MappingExpression")
foundation_data_types_ProcedureExpression = Class(name="foundation_data_types_ProcedureExpression")
foundation_data_types_ObjectSetExpression = Class(name="foundation_data_types_ObjectSetExpression")
foundation_data_types_ActionExpression = Class(name="foundation_data_types_ActionExpression")
foundation_data_types_IterationExpression = Class(name="foundation_data_types_IterationExpression")
foundation_data_types_TimeExpression = Class(name="foundation_data_types_TimeExpression")
foundation_data_types_ArgListsExpression = Class(name="foundation_data_types_ArgListsExpression")
foundation_core_Element = Class(name="foundation_core_Element", is_abstract=True)
foundation_data_types_Multiplicity = Class(name="foundation_data_types_Multiplicity_")
MultiplicityRange = Class(name="MultiplicityRange")
foundation_data_types_MultiplicityRange = Class(name="foundation_data_types_MultiplicityRange")
Multiplicity_ = Class(name="Multiplicity_")
foundation_data_types_Expression = Class(name="foundation_data_types_Expression")
ElementResidence = Class(name="ElementResidence")
TemplateParameter = Class(name="TemplateParameter")
Stereotype = Class(name="Stereotype")
TaggedValue = Class(name="TaggedValue")
StateMachine = Class(name="StateMachine")
foundation_core_GeneralizableElement = Class(name="foundation_core_GeneralizableElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
foundation_core_ModelElement = Class(name="foundation_core_ModelElement", is_abstract=True)
Element = Class(name="Element")
Namespace = Class(name="Namespace")
Dependency = Class(name="Dependency")
Constraint = Class(name="Constraint")
PresentationElement = Class(name="PresentationElement")
Flow = Class(name="Flow")
Comment = Class(name="Comment")
CreateAction = Class(name="CreateAction")
Collaboration = Class(name="Collaboration")
foundation_core_Class = Class(name="foundation_core_Class")
Classifier = Class(name="Classifier")
foundation_core_DataType = Class(name="foundation_core_DataType")
foundation_core_Feature = Class(name="foundation_core_Feature", is_abstract=True)
foundation_core_StructuralFeature = Class(name="foundation_core_StructuralFeature", is_abstract=True)
Generalization_ = Class(name="Generalization_")
foundation_core_Namespace = Class(name="foundation_core_Namespace", is_abstract=True)
foundation_core_Classifier = Class(name="foundation_core_Classifier", is_abstract=True)
core_GeneralizableElement = Class(name="core_GeneralizableElement")
foundation_core_AssociationEnd = Class(name="foundation_core_AssociationEnd")
core_Namespace = Class(name="core_Namespace")
Feature = Class(name="Feature")
StructuralFeature = Class(name="StructuralFeature")
Parameter_ = Class(name="Parameter")
AssociationEnd = Class(name="AssociationEnd")
Association = Class(name="Association")
Attribute = Class(name="Attribute")
foundation_core_Interface = Class(name="foundation_core_Interface")
foundation_core_Constraint = Class(name="foundation_core_Constraint")
BooleanExpression = Class(name="BooleanExpression")
foundation_core_Relationship = Class(name="foundation_core_Relationship", is_abstract=True)
foundation_core_Association = Class(name="foundation_core_Association")
core_Relationship = Class(name="core_Relationship")
foundation_core_Attribute = Class(name="foundation_core_Attribute")
AssociationEndRole = Class(name="AssociationEndRole")
foundation_core_BehavioralFeature = Class(name="foundation_core_BehavioralFeature", is_abstract=True)
Signal = Class(name="Signal")
foundation_core_Operation = Class(name="foundation_core_Operation")
BehavioralFeature = Class(name="BehavioralFeature")
Method_ = Class(name="Method")
CallAction = Class(name="CallAction")
CallEvent = Class(name="CallEvent")
foundation_core_Parameter = Class(name="foundation_core_Parameter")
foundation_core_Method = Class(name="foundation_core_Method")
ProcedureExpression = Class(name="ProcedureExpression")
Operation = Class(name="Operation")
foundation_core_Generalization = Class(name="foundation_core_Generalization_")
Relationship = Class(name="Relationship")
GeneralizableElement = Class(name="GeneralizableElement")
foundation_core_Node = Class(name="foundation_core_Node")
Component = Class(name="Component")
foundation_core_AssociationClass = Class(name="foundation_core_AssociationClass")
core_Class = Class(name="core_Class")
core_Association = Class(name="core_Association")
foundation_core_Dependency = Class(name="foundation_core_Dependency")
foundation_core_Abstraction = Class(name="foundation_core_Abstraction")
MappingExpression = Class(name="MappingExpression")
foundation_core_PresentationElement = Class(name="foundation_core_PresentationElement", is_abstract=True)
foundation_core_Usage = Class(name="foundation_core_Usage")
foundation_core_Binding = Class(name="foundation_core_Binding")
TemplateArgument = Class(name="TemplateArgument")
foundation_core_Component = Class(name="foundation_core_Component")
Node = Class(name="Node")
Artifact = Class(name="Artifact")
EnumerationLiteral = Class(name="EnumerationLiteral")
foundation_core_EnumerationLiteral = Class(name="foundation_core_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
foundation_core_Permission = Class(name="foundation_core_Permission")
foundation_core_Comment = Class(name="foundation_core_Comment")
foundation_core_Stereotype = Class(name="foundation_core_Stereotype")
foundation_core_Flow = Class(name="foundation_core_Flow")
foundation_core_ElementResidence = Class(name="foundation_core_ElementResidence")
foundation_core_TemplateParameter = Class(name="foundation_core_TemplateParameter")
foundation_core_Primitive = Class(name="foundation_core_Primitive")
DataType = Class(name="DataType")
foundation_core_Enumeration = Class(name="foundation_core_Enumeration")
foundation_core_ProgrammingLanguageDataType = Class(name="foundation_core_ProgrammingLanguageDataType")
TypeExpression = Class(name="TypeExpression")
foundation_core_Artifact = Class(name="foundation_core_Artifact")
foundation_core_TemplateArgument = Class(name="foundation_core_TemplateArgument")
TagDefinition = Class(name="TagDefinition")
Binding = Class(name="Binding")
foundation_core_TagDefinition = Class(name="foundation_core_TagDefinition")
foundation_core_TaggedValue = Class(name="foundation_core_TaggedValue")

# foundation_data_types_BooleanExpression class attributes and methods

# Expression class attributes and methods

# foundation_data_types_TypeExpression class attributes and methods

# foundation_data_types_MappingExpression class attributes and methods

# foundation_data_types_ProcedureExpression class attributes and methods

# foundation_data_types_ObjectSetExpression class attributes and methods

# foundation_data_types_ActionExpression class attributes and methods

# foundation_data_types_IterationExpression class attributes and methods

# foundation_data_types_TimeExpression class attributes and methods

# foundation_data_types_ArgListsExpression class attributes and methods

# foundation_core_Element class attributes and methods

# foundation_data_types_Multiplicity class attributes and methods

# MultiplicityRange class attributes and methods

# foundation_data_types_MultiplicityRange class attributes and methods
foundation_data_types_MultiplicityRange_lower: Property = Property(name="lower", type=StringType)
foundation_data_types_MultiplicityRange_upper: Property = Property(name="upper", type=StringType)
foundation_data_types_MultiplicityRange.attributes={foundation_data_types_MultiplicityRange_lower, foundation_data_types_MultiplicityRange_upper}

# Multiplicity_ class attributes and methods

# foundation_data_types_Expression class attributes and methods
foundation_data_types_Expression_body: Property = Property(name="body", type=StringType)
foundation_data_types_Expression_language: Property = Property(name="language", type=StringType)
foundation_data_types_Expression.attributes={foundation_data_types_Expression_language, foundation_data_types_Expression_body}

# ElementResidence class attributes and methods

# TemplateParameter class attributes and methods

# Stereotype class attributes and methods

# TaggedValue class attributes and methods

# StateMachine class attributes and methods

# foundation_core_GeneralizableElement class attributes and methods
foundation_core_GeneralizableElement_isRoot: Property = Property(name="isRoot", type=StringType)
foundation_core_GeneralizableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
foundation_core_GeneralizableElement_isAbstract: Property = Property(name="isAbstract", type=StringType)
foundation_core_GeneralizableElement.attributes={foundation_core_GeneralizableElement_isAbstract, foundation_core_GeneralizableElement_isRoot, foundation_core_GeneralizableElement_isLeaf}

# ModelElement class attributes and methods

# foundation_core_ModelElement class attributes and methods
foundation_core_ModelElement_name: Property = Property(name="name", type=StringType)
foundation_core_ModelElement_visibility: Property = Property(name="visibility", type=StringType)
foundation_core_ModelElement_isSpecification: Property = Property(name="isSpecification", type=StringType)
foundation_core_ModelElement.attributes={foundation_core_ModelElement_name, foundation_core_ModelElement_isSpecification, foundation_core_ModelElement_visibility}

# Element class attributes and methods

# Namespace class attributes and methods

# Dependency class attributes and methods

# Constraint class attributes and methods

# PresentationElement class attributes and methods

# Flow class attributes and methods

# Comment class attributes and methods

# CreateAction class attributes and methods

# Collaboration class attributes and methods

# foundation_core_Class class attributes and methods
foundation_core_Class_isActive: Property = Property(name="isActive", type=StringType)
foundation_core_Class.attributes={foundation_core_Class_isActive}

# Classifier class attributes and methods

# foundation_core_DataType class attributes and methods

# foundation_core_Feature class attributes and methods
foundation_core_Feature_ownerScope: Property = Property(name="ownerScope", type=StringType)
foundation_core_Feature.attributes={foundation_core_Feature_ownerScope}

# foundation_core_StructuralFeature class attributes and methods
foundation_core_StructuralFeature_changeability: Property = Property(name="changeability", type=StringType)
foundation_core_StructuralFeature_targetScope: Property = Property(name="targetScope", type=StringType)
foundation_core_StructuralFeature_ordering: Property = Property(name="ordering", type=StringType)
foundation_core_StructuralFeature.attributes={foundation_core_StructuralFeature_changeability, foundation_core_StructuralFeature_ordering, foundation_core_StructuralFeature_targetScope}

# Generalization_ class attributes and methods

# foundation_core_Namespace class attributes and methods

# foundation_core_Classifier class attributes and methods

# core_GeneralizableElement class attributes and methods

# foundation_core_AssociationEnd class attributes and methods
foundation_core_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=StringType)
foundation_core_AssociationEnd_ordering: Property = Property(name="ordering", type=StringType)
foundation_core_AssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
foundation_core_AssociationEnd_targetScope: Property = Property(name="targetScope", type=StringType)
foundation_core_AssociationEnd_changeability: Property = Property(name="changeability", type=StringType)
foundation_core_AssociationEnd.attributes={foundation_core_AssociationEnd_aggregation, foundation_core_AssociationEnd_ordering, foundation_core_AssociationEnd_changeability, foundation_core_AssociationEnd_targetScope, foundation_core_AssociationEnd_isNavigable}

# core_Namespace class attributes and methods

# Feature class attributes and methods

# StructuralFeature class attributes and methods

# Parameter class attributes and methods

# AssociationEnd class attributes and methods

# Association class attributes and methods

# Attribute class attributes and methods

# foundation_core_Interface class attributes and methods

# foundation_core_Constraint class attributes and methods

# BooleanExpression class attributes and methods

# foundation_core_Relationship class attributes and methods

# foundation_core_Association class attributes and methods

# core_Relationship class attributes and methods

# foundation_core_Attribute class attributes and methods

# AssociationEndRole class attributes and methods

# foundation_core_BehavioralFeature class attributes and methods
foundation_core_BehavioralFeature_isQuery: Property = Property(name="isQuery", type=StringType)
foundation_core_BehavioralFeature.attributes={foundation_core_BehavioralFeature_isQuery}

# Signal class attributes and methods

# foundation_core_Operation class attributes and methods
foundation_core_Operation_concurrency: Property = Property(name="concurrency", type=StringType)
foundation_core_Operation_isRoot: Property = Property(name="isRoot", type=StringType)
foundation_core_Operation_isLeaf: Property = Property(name="isLeaf", type=StringType)
foundation_core_Operation_isAbstract: Property = Property(name="isAbstract", type=StringType)
foundation_core_Operation_specification: Property = Property(name="specification", type=StringType)
foundation_core_Operation.attributes={foundation_core_Operation_isRoot, foundation_core_Operation_isLeaf, foundation_core_Operation_isAbstract, foundation_core_Operation_specification, foundation_core_Operation_concurrency}

# BehavioralFeature class attributes and methods

# Method class attributes and methods

# CallAction class attributes and methods

# CallEvent class attributes and methods

# foundation_core_Parameter class attributes and methods
foundation_core_Parameter_kind: Property = Property(name="kind", type=StringType)
foundation_core_Parameter.attributes={foundation_core_Parameter_kind}

# foundation_core_Method class attributes and methods

# ProcedureExpression class attributes and methods

# Operation class attributes and methods

# foundation_core_Generalization class attributes and methods
foundation_core_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
foundation_core_Generalization.attributes={foundation_core_Generalization_discriminator}

# Relationship class attributes and methods

# GeneralizableElement class attributes and methods

# foundation_core_Node class attributes and methods

# Component class attributes and methods

# foundation_core_AssociationClass class attributes and methods

# core_Class class attributes and methods

# core_Association class attributes and methods

# foundation_core_Dependency class attributes and methods

# foundation_core_Abstraction class attributes and methods

# MappingExpression class attributes and methods

# foundation_core_PresentationElement class attributes and methods

# foundation_core_Usage class attributes and methods

# foundation_core_Binding class attributes and methods

# TemplateArgument class attributes and methods

# foundation_core_Component class attributes and methods

# Node class attributes and methods

# Artifact class attributes and methods

# EnumerationLiteral class attributes and methods

# foundation_core_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# foundation_core_Permission class attributes and methods

# foundation_core_Comment class attributes and methods
foundation_core_Comment_body: Property = Property(name="body", type=StringType)
foundation_core_Comment.attributes={foundation_core_Comment_body}

# foundation_core_Stereotype class attributes and methods
foundation_core_Stereotype_icon: Property = Property(name="icon", type=StringType)
foundation_core_Stereotype_baseClass: Property = Property(name="baseClass", type=StringType)
foundation_core_Stereotype.attributes={foundation_core_Stereotype_baseClass, foundation_core_Stereotype_icon}

# foundation_core_Flow class attributes and methods

# foundation_core_ElementResidence class attributes and methods
foundation_core_ElementResidence_visibility: Property = Property(name="visibility", type=StringType)
foundation_core_ElementResidence.attributes={foundation_core_ElementResidence_visibility}

# foundation_core_TemplateParameter class attributes and methods

# foundation_core_Primitive class attributes and methods

# DataType class attributes and methods

# foundation_core_Enumeration class attributes and methods

# foundation_core_ProgrammingLanguageDataType class attributes and methods

# TypeExpression class attributes and methods

# foundation_core_Artifact class attributes and methods

# foundation_core_TemplateArgument class attributes and methods

# TagDefinition class attributes and methods

# Binding class attributes and methods

# foundation_core_TagDefinition class attributes and methods
foundation_core_TagDefinition_tagType: Property = Property(name="tagType", type=StringType)
foundation_core_TagDefinition.attributes={foundation_core_TagDefinition_tagType}

# foundation_core_TaggedValue class attributes and methods
foundation_core_TaggedValue_dataValue: Property = Property(name="dataValue", type=StringType)
foundation_core_TaggedValue.attributes={foundation_core_TaggedValue_dataValue}

# Relationships
range0: BinaryAssociation = BinaryAssociation(
    name="range0",
    ends={
        Property(name="MultiplicityRange", type=foundation_data_types_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="multiplicity", type=MultiplicityRange, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicity1: BinaryAssociation = BinaryAssociation(
    name="multiplicity1",
    ends={
        Property(name="Multiplicity", type=foundation_data_types_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="range", type=Multiplicity_, multiplicity=Multiplicity(1, 1))
    }
)
comment11: BinaryAssociation = BinaryAssociation(
    name="comment11",
    ends={
        Property(name="Comment", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedElement", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
elementResidence12: BinaryAssociation = BinaryAssociation(
    name="elementResidence12",
    ends={
        Property(name="ElementResidence", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="resident", type=ElementResidence, multiplicity=Multiplicity(0, 9999))
    }
)
templateParameter13: BinaryAssociation = BinaryAssociation(
    name="templateParameter13",
    ends={
        Property(name="TemplateParameter", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotype14: BinaryAssociation = BinaryAssociation(
    name="stereotype14",
    ends={
        Property(name="Stereotype", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedElement", type=Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)
taggedValue15: BinaryAssociation = BinaryAssociation(
    name="taggedValue15",
    ends={
        Property(name="TaggedValue", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElement", type=TaggedValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceTag16: BinaryAssociation = BinaryAssociation(
    name="referenceTag16",
    ends={
        Property(name="TaggedValue17", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceValue", type=TaggedValue, multiplicity=Multiplicity(0, 9999))
    }
)
behavior18: BinaryAssociation = BinaryAssociation(
    name="behavior18",
    ends={
        Property(name="StateMachine", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
namespace2: BinaryAssociation = BinaryAssociation(
    name="namespace2",
    ends={
        Property(name="Namespace", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency3: BinaryAssociation = BinaryAssociation(
    name="clientDependency3",
    ends={
        Property(name="Dependency", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
constraint4: BinaryAssociation = BinaryAssociation(
    name="constraint4",
    ends={
        Property(name="Constraint", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedElement", type=Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
supplierDependency5: BinaryAssociation = BinaryAssociation(
    name="supplierDependency5",
    ends={
        Property(name="Dependency6", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
presentation7: BinaryAssociation = BinaryAssociation(
    name="presentation7",
    ends={
        Property(name="PresentationElement", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="subject", type=PresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
targetFlow8: BinaryAssociation = BinaryAssociation(
    name="targetFlow8",
    ends={
        Property(name="Flow", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Flow, multiplicity=Multiplicity(0, 9999))
    }
)
sourceFlow9: BinaryAssociation = BinaryAssociation(
    name="sourceFlow9",
    ends={
        Property(name="Flow10", type=foundation_core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Flow, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeRange30: BinaryAssociation = BinaryAssociation(
    name="powertypeRange30",
    ends={
        Property(name="Generalization31", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
createAction32: BinaryAssociation = BinaryAssociation(
    name="createAction32",
    ends={
        Property(name="CreateAction", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiation", type=CreateAction, multiplicity=Multiplicity(0, 9999))
    }
)
collaboration33: BinaryAssociation = BinaryAssociation(
    name="collaboration33",
    ends={
        Property(name="Collaboration", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="representedClassifier", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
owner34: BinaryAssociation = BinaryAssociation(
    name="owner34",
    ends={
        Property(name="Classifier", type=foundation_core_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization19: BinaryAssociation = BinaryAssociation(
    name="generalization19",
    ends={
        Property(name="Generalization_", type=foundation_core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity35: BinaryAssociation = BinaryAssociation(
    name="multiplicity35",
    ends={
        Property(name="Multiplicity36", type=foundation_core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_StructuralFeature", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specialization20: BinaryAssociation = BinaryAssociation(
    name="specialization20",
    ends={
        Property(name="Generalization21", type=foundation_core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement22: BinaryAssociation = BinaryAssociation(
    name="ownedElement22",
    ends={
        Property(name="ModelElement", type=foundation_core_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="Classifier38", type=foundation_core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="typedFeature", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
feature23: BinaryAssociation = BinaryAssociation(
    name="feature23",
    ends={
        Property(name="Feature", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedFeature24: BinaryAssociation = BinaryAssociation(
    name="typedFeature24",
    ends={
        Property(name="StructuralFeature", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity39: BinaryAssociation = BinaryAssociation(
    name="multiplicity39",
    ends={
        Property(name="Multiplicity40", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_AssociationEnd", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typedParameter25: BinaryAssociation = BinaryAssociation(
    name="typedParameter25",
    ends={
        Property(name="Parameter", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type26", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
association27: BinaryAssociation = BinaryAssociation(
    name="association27",
    ends={
        Property(name="AssociationEnd", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="participant", type=AssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
association41: BinaryAssociation = BinaryAssociation(
    name="association41",
    ends={
        Property(name="Association", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
specifiedEnd28: BinaryAssociation = BinaryAssociation(
    name="specifiedEnd28",
    ends={
        Property(name="AssociationEnd29", type=foundation_core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=AssociationEnd, multiplicity=Multiplicity(0, 9999))
    }
)
qualifier42: BinaryAssociation = BinaryAssociation(
    name="qualifier42",
    ends={
        Property(name="Attribute", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
participant43: BinaryAssociation = BinaryAssociation(
    name="participant43",
    ends={
        Property(name="Classifier44", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specification45: BinaryAssociation = BinaryAssociation(
    name="specification45",
    ends={
        Property(name="Classifier46", type=foundation_core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedEnd", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="BooleanExpression", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Constraint", type=BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrainedElement48: BinaryAssociation = BinaryAssociation(
    name="constrainedElement48",
    ends={
        Property(name="ModelElement49", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedStereotype50: BinaryAssociation = BinaryAssociation(
    name="constrainedStereotype50",
    ends={
        Property(name="Stereotype51", type=foundation_core_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypeConstraint", type=Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
connection52: BinaryAssociation = BinaryAssociation(
    name="connection52",
    ends={
        Property(name="AssociationEnd54", type=foundation_core_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association53", type=AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
initialValue55: BinaryAssociation = BinaryAssociation(
    name="initialValue55",
    ends={
        Property(name="Expression", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Attribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associationEnd56: BinaryAssociation = BinaryAssociation(
    name="associationEnd56",
    ends={
        Property(name="AssociationEnd57", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
associationEndRole58: BinaryAssociation = BinaryAssociation(
    name="associationEndRole58",
    ends={
        Property(name="AssociationEndRole", type=foundation_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="availableQualifier", type=AssociationEndRole, multiplicity=Multiplicity(0, 9999))
    }
)
parameter59: BinaryAssociation = BinaryAssociation(
    name="parameter59",
    ends={
        Property(name="Parameter60", type=foundation_core_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="behavioralFeature", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedSignal61: BinaryAssociation = BinaryAssociation(
    name="raisedSignal61",
    ends={
        Property(name="Signal", type=foundation_core_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="context62", type=Signal, multiplicity=Multiplicity(0, 9999))
    }
)
powertype80: BinaryAssociation = BinaryAssociation(
    name="powertype80",
    ends={
        Property(name="Classifier81", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeRange", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
method63: BinaryAssociation = BinaryAssociation(
    name="method63",
    ends={
        Property(name="Method", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="specification64", type=Method_, multiplicity=Multiplicity(0, 9999))
    }
)
callAction65: BinaryAssociation = BinaryAssociation(
    name="callAction65",
    ends={
        Property(name="CallAction", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=CallAction, multiplicity=Multiplicity(0, 9999))
    }
)
occurrence66: BinaryAssociation = BinaryAssociation(
    name="occurrence66",
    ends={
        Property(name="CallEvent", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation67", type=CallEvent, multiplicity=Multiplicity(0, 9999))
    }
)
collaboration68: BinaryAssociation = BinaryAssociation(
    name="collaboration68",
    ends={
        Property(name="Collaboration69", type=foundation_core_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="representedOperation", type=Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue70: BinaryAssociation = BinaryAssociation(
    name="defaultValue70",
    ends={
        Property(name="Expression71", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Parameter", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behavioralFeature72: BinaryAssociation = BinaryAssociation(
    name="behavioralFeature72",
    ends={
        Property(name="BehavioralFeature", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
type73: BinaryAssociation = BinaryAssociation(
    name="type73",
    ends={
        Property(name="Classifier74", type=foundation_core_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typedParameter", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
body75: BinaryAssociation = BinaryAssociation(
    name="body75",
    ends={
        Property(name="ProcedureExpression", type=foundation_core_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Method", type=ProcedureExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification76: BinaryAssociation = BinaryAssociation(
    name="specification76",
    ends={
        Property(name="Operation", type=foundation_core_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
child77: BinaryAssociation = BinaryAssociation(
    name="child77",
    ends={
        Property(name="GeneralizableElement", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
parent78: BinaryAssociation = BinaryAssociation(
    name="parent78",
    ends={
        Property(name="GeneralizableElement79", type=foundation_core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
client82: BinaryAssociation = BinaryAssociation(
    name="client82",
    ends={
        Property(name="ModelElement83", type=foundation_core_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier84: BinaryAssociation = BinaryAssociation(
    name="supplier84",
    ends={
        Property(name="ModelElement85", type=foundation_core_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="supplierDependency", type=ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
mapping86: BinaryAssociation = BinaryAssociation(
    name="mapping86",
    ends={
        Property(name="MappingExpression", type=foundation_core_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_Abstraction", type=MappingExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subject87: BinaryAssociation = BinaryAssociation(
    name="subject87",
    ends={
        Property(name="ModelElement88", type=foundation_core_PresentationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="presentation", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
argument89: BinaryAssociation = BinaryAssociation(
    name="argument89",
    ends={
        Property(name="TemplateArgument", type=foundation_core_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="binding", type=TemplateArgument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
deploymentLocation90: BinaryAssociation = BinaryAssociation(
    name="deploymentLocation90",
    ends={
        Property(name="Node", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="deployedComponent", type=Node, multiplicity=Multiplicity(0, 9999))
    }
)
residentElement91: BinaryAssociation = BinaryAssociation(
    name="residentElement91",
    ends={
        Property(name="ElementResidence92", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=ElementResidence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementation93: BinaryAssociation = BinaryAssociation(
    name="implementation93",
    ends={
        Property(name="Artifact", type=foundation_core_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="implementationLocation", type=Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
literal112: BinaryAssociation = BinaryAssociation(
    name="literal112",
    ends={
        Property(name="EnumerationLiteral", type=foundation_core_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
deployedComponent94: BinaryAssociation = BinaryAssociation(
    name="deployedComponent94",
    ends={
        Property(name="Component", type=foundation_core_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="deploymentLocation", type=Component, multiplicity=Multiplicity(0, 9999))
    }
)
enumeration113: BinaryAssociation = BinaryAssociation(
    name="enumeration113",
    ends={
        Property(name="Enumeration", type=foundation_core_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literal", type=Enumeration_, multiplicity=Multiplicity(1, 1))
    }
)
annotatedElement95: BinaryAssociation = BinaryAssociation(
    name="annotatedElement95",
    ends={
        Property(name="ModelElement96", type=foundation_core_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comment", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
target97: BinaryAssociation = BinaryAssociation(
    name="target97",
    ends={
        Property(name="ModelElement98", type=foundation_core_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="targetFlow", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
source99: BinaryAssociation = BinaryAssociation(
    name="source99",
    ends={
        Property(name="ModelElement100", type=foundation_core_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceFlow", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
resident101: BinaryAssociation = BinaryAssociation(
    name="resident101",
    ends={
        Property(name="ModelElement102", type=foundation_core_ElementResidence, multiplicity=Multiplicity(1, 1)),
        Property(name="elementResidence", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
container103: BinaryAssociation = BinaryAssociation(
    name="container103",
    ends={
        Property(name="Component104", type=foundation_core_ElementResidence, multiplicity=Multiplicity(1, 1)),
        Property(name="residentElement", type=Component, multiplicity=Multiplicity(1, 1))
    }
)
defaultElement105: BinaryAssociation = BinaryAssociation(
    name="defaultElement105",
    ends={
        Property(name="ModelElement106", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateParameter", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
template107: BinaryAssociation = BinaryAssociation(
    name="template107",
    ends={
        Property(name="ModelElement108", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
parameter109: BinaryAssociation = BinaryAssociation(
    name="parameter109",
    ends={
        Property(name="ModelElement111", type=foundation_core_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateParameter110", type=ModelElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referenceValue131: BinaryAssociation = BinaryAssociation(
    name="referenceValue131",
    ends={
        Property(name="ModelElement132", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceTag", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
expression133: BinaryAssociation = BinaryAssociation(
    name="expression133",
    ends={
        Property(name="TypeExpression", type=foundation_core_ProgrammingLanguageDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_ProgrammingLanguageDataType", type=TypeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementationLocation134: BinaryAssociation = BinaryAssociation(
    name="implementationLocation134",
    ends={
        Property(name="Component135", type=foundation_core_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="implementation", type=Component, multiplicity=Multiplicity(0, 9999))
    }
)
definedTag114: BinaryAssociation = BinaryAssociation(
    name="definedTag114",
    ends={
        Property(name="TagDefinition", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="owner115", type=TagDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedElement116: BinaryAssociation = BinaryAssociation(
    name="extendedElement116",
    ends={
        Property(name="ModelElement117", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
stereotypeConstraint118: BinaryAssociation = BinaryAssociation(
    name="stereotypeConstraint118",
    ends={
        Property(name="Constraint119", type=foundation_core_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedStereotype", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity120: BinaryAssociation = BinaryAssociation(
    name="multiplicity120",
    ends={
        Property(name="Multiplicity121", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TagDefinition", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner122: BinaryAssociation = BinaryAssociation(
    name="owner122",
    ends={
        Property(name="Stereotype123", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definedTag", type=Stereotype, multiplicity=Multiplicity(0, 1))
    }
)
typedValue124: BinaryAssociation = BinaryAssociation(
    name="typedValue124",
    ends={
        Property(name="TaggedValue126", type=foundation_core_TagDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="type125", type=TaggedValue, multiplicity=Multiplicity(0, 9999))
    }
)
modelElement127: BinaryAssociation = BinaryAssociation(
    name="modelElement127",
    ends={
        Property(name="ModelElement128", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="taggedValue", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="TagDefinition130", type=foundation_core_TaggedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="typedValue", type=TagDefinition, multiplicity=Multiplicity(1, 1))
    }
)
binding136: BinaryAssociation = BinaryAssociation(
    name="binding136",
    ends={
        Property(name="Binding", type=foundation_core_TemplateArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="argument", type=Binding, multiplicity=Multiplicity(1, 1))
    }
)
modelElement137: BinaryAssociation = BinaryAssociation(
    name="modelElement137",
    ends={
        Property(name="ModelElement138", type=foundation_core_TemplateArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="foundation_core_TemplateArgument", type=ModelElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_foundation_data_types_BooleanExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_BooleanExpression)
gen_foundation_data_types_TypeExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_TypeExpression)
gen_foundation_data_types_MappingExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_MappingExpression)
gen_foundation_data_types_ProcedureExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ProcedureExpression)
gen_foundation_data_types_ObjectSetExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ObjectSetExpression)
gen_foundation_data_types_ActionExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ActionExpression)
gen_foundation_data_types_IterationExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_IterationExpression)
gen_foundation_data_types_TimeExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_TimeExpression)
gen_foundation_data_types_ArgListsExpression_Expression = Generalization(general=Expression, specific=foundation_data_types_ArgListsExpression)
gen_foundation_core_GeneralizableElement_ModelElement = Generalization(general=ModelElement, specific=foundation_core_GeneralizableElement)
gen_foundation_core_ModelElement_Element = Generalization(general=Element, specific=foundation_core_ModelElement)
gen_foundation_core_Class_Classifier = Generalization(general=Classifier, specific=foundation_core_Class)
gen_foundation_core_DataType_Classifier = Generalization(general=Classifier, specific=foundation_core_DataType)
gen_foundation_core_Feature_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Feature)
gen_foundation_core_StructuralFeature_Feature = Generalization(general=Feature, specific=foundation_core_StructuralFeature)
gen_foundation_core_Namespace_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Namespace)
gen_foundation_core_Classifier_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=foundation_core_Classifier)
gen_foundation_core_AssociationEnd_ModelElement = Generalization(general=ModelElement, specific=foundation_core_AssociationEnd)
gen_foundation_core_Classifier_core_Namespace = Generalization(general=core_Namespace, specific=foundation_core_Classifier)
gen_foundation_core_Interface_Classifier = Generalization(general=Classifier, specific=foundation_core_Interface)
gen_foundation_core_Constraint_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Constraint)
gen_foundation_core_Relationship_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Relationship)
gen_foundation_core_Association_core_GeneralizableElement = Generalization(general=core_GeneralizableElement, specific=foundation_core_Association)
gen_foundation_core_Association_core_Relationship = Generalization(general=core_Relationship, specific=foundation_core_Association)
gen_foundation_core_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=foundation_core_Attribute)
gen_foundation_core_BehavioralFeature_Feature = Generalization(general=Feature, specific=foundation_core_BehavioralFeature)
gen_foundation_core_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=foundation_core_Operation)
gen_foundation_core_Parameter_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Parameter)
gen_foundation_core_Method_BehavioralFeature = Generalization(general=BehavioralFeature, specific=foundation_core_Method)
gen_foundation_core_Generalization_Relationship = Generalization(general=Relationship, specific=foundation_core_Generalization)
gen_foundation_core_Node_Classifier = Generalization(general=Classifier, specific=foundation_core_Node)
gen_foundation_core_AssociationClass_core_Class = Generalization(general=core_Class, specific=foundation_core_AssociationClass)
gen_foundation_core_AssociationClass_core_Association = Generalization(general=core_Association, specific=foundation_core_AssociationClass)
gen_foundation_core_Dependency_Relationship = Generalization(general=Relationship, specific=foundation_core_Dependency)
gen_foundation_core_Abstraction_Dependency = Generalization(general=Dependency, specific=foundation_core_Abstraction)
gen_foundation_core_PresentationElement_Element = Generalization(general=Element, specific=foundation_core_PresentationElement)
gen_foundation_core_Usage_Dependency = Generalization(general=Dependency, specific=foundation_core_Usage)
gen_foundation_core_Binding_Dependency = Generalization(general=Dependency, specific=foundation_core_Binding)
gen_foundation_core_Component_Classifier = Generalization(general=Classifier, specific=foundation_core_Component)
gen_foundation_core_EnumerationLiteral_ModelElement = Generalization(general=ModelElement, specific=foundation_core_EnumerationLiteral)
gen_foundation_core_Permission_Dependency = Generalization(general=Dependency, specific=foundation_core_Permission)
gen_foundation_core_Comment_ModelElement = Generalization(general=ModelElement, specific=foundation_core_Comment)
gen_foundation_core_Stereotype_GeneralizableElement = Generalization(general=GeneralizableElement, specific=foundation_core_Stereotype)
gen_foundation_core_Flow_Relationship = Generalization(general=Relationship, specific=foundation_core_Flow)
gen_foundation_core_Primitive_DataType = Generalization(general=DataType, specific=foundation_core_Primitive)
gen_foundation_core_Enumeration_DataType = Generalization(general=DataType, specific=foundation_core_Enumeration)
gen_foundation_core_ProgrammingLanguageDataType_DataType = Generalization(general=DataType, specific=foundation_core_ProgrammingLanguageDataType)
gen_foundation_core_Artifact_Classifier = Generalization(general=Classifier, specific=foundation_core_Artifact)
gen_foundation_core_TagDefinition_ModelElement = Generalization(general=ModelElement, specific=foundation_core_TagDefinition)
gen_foundation_core_TaggedValue_ModelElement = Generalization(general=ModelElement, specific=foundation_core_TaggedValue)

# Domain Model
domain_model = DomainModel(
    name="foundation",
    types={foundation_data_types_BooleanExpression, Expression, foundation_data_types_TypeExpression, foundation_data_types_MappingExpression, foundation_data_types_ProcedureExpression, foundation_data_types_ObjectSetExpression, foundation_data_types_ActionExpression, foundation_data_types_IterationExpression, foundation_data_types_TimeExpression, foundation_data_types_ArgListsExpression, foundation_core_Element, foundation_data_types_Multiplicity, MultiplicityRange, foundation_data_types_MultiplicityRange, Multiplicity_, foundation_data_types_Expression, ElementResidence, TemplateParameter, Stereotype, TaggedValue, StateMachine, foundation_core_GeneralizableElement, ModelElement, foundation_core_ModelElement, Element, Namespace, Dependency, Constraint, PresentationElement, Flow, Comment, CreateAction, Collaboration, foundation_core_Class, Classifier, foundation_core_DataType, foundation_core_Feature, foundation_core_StructuralFeature, Generalization_, foundation_core_Namespace, foundation_core_Classifier, core_GeneralizableElement, foundation_core_AssociationEnd, core_Namespace, Feature, StructuralFeature, Parameter_, AssociationEnd, Association, Attribute, foundation_core_Interface, foundation_core_Constraint, BooleanExpression, foundation_core_Relationship, foundation_core_Association, core_Relationship, foundation_core_Attribute, AssociationEndRole, foundation_core_BehavioralFeature, Signal, foundation_core_Operation, BehavioralFeature, Method_, CallAction, CallEvent, foundation_core_Parameter, foundation_core_Method, ProcedureExpression, Operation, foundation_core_Generalization, Relationship, GeneralizableElement, foundation_core_Node, Component, foundation_core_AssociationClass, core_Class, core_Association, foundation_core_Dependency, foundation_core_Abstraction, MappingExpression, foundation_core_PresentationElement, foundation_core_Usage, foundation_core_Binding, TemplateArgument, foundation_core_Component, Node, Artifact, EnumerationLiteral, foundation_core_EnumerationLiteral, Enumeration_, foundation_core_Permission, foundation_core_Comment, foundation_core_Stereotype, foundation_core_Flow, foundation_core_ElementResidence, foundation_core_TemplateParameter, foundation_core_Primitive, DataType, foundation_core_Enumeration, foundation_core_ProgrammingLanguageDataType, TypeExpression, foundation_core_Artifact, foundation_core_TemplateArgument, TagDefinition, Binding, foundation_core_TagDefinition, foundation_core_TaggedValue, AggregationKind, PseudostateKind, CallConcurrencyKind, ChangeableKind, OrderingKind, ParameterDirectionKind, ScopeKind, VisibilityKind},
    associations={range0, multiplicity1, comment11, elementResidence12, templateParameter13, stereotype14, taggedValue15, referenceTag16, behavior18, namespace2, clientDependency3, constraint4, supplierDependency5, presentation7, targetFlow8, sourceFlow9, powertypeRange30, createAction32, collaboration33, owner34, generalization19, multiplicity35, specialization20, ownedElement22, type37, feature23, typedFeature24, multiplicity39, typedParameter25, association27, association41, specifiedEnd28, qualifier42, participant43, specification45, body47, constrainedElement48, constrainedStereotype50, connection52, initialValue55, associationEnd56, associationEndRole58, parameter59, raisedSignal61, powertype80, method63, callAction65, occurrence66, collaboration68, defaultValue70, behavioralFeature72, type73, body75, specification76, child77, parent78, client82, supplier84, mapping86, subject87, argument89, deploymentLocation90, residentElement91, implementation93, literal112, deployedComponent94, enumeration113, annotatedElement95, target97, source99, resident101, container103, defaultElement105, template107, parameter109, referenceValue131, expression133, implementationLocation134, definedTag114, extendedElement116, stereotypeConstraint118, multiplicity120, owner122, typedValue124, modelElement127, type129, binding136, modelElement137},
    generalizations={gen_foundation_data_types_BooleanExpression_Expression, gen_foundation_data_types_TypeExpression_Expression, gen_foundation_data_types_MappingExpression_Expression, gen_foundation_data_types_ProcedureExpression_Expression, gen_foundation_data_types_ObjectSetExpression_Expression, gen_foundation_data_types_ActionExpression_Expression, gen_foundation_data_types_IterationExpression_Expression, gen_foundation_data_types_TimeExpression_Expression, gen_foundation_data_types_ArgListsExpression_Expression, gen_foundation_core_GeneralizableElement_ModelElement, gen_foundation_core_ModelElement_Element, gen_foundation_core_Class_Classifier, gen_foundation_core_DataType_Classifier, gen_foundation_core_Feature_ModelElement, gen_foundation_core_StructuralFeature_Feature, gen_foundation_core_Namespace_ModelElement, gen_foundation_core_Classifier_core_GeneralizableElement, gen_foundation_core_AssociationEnd_ModelElement, gen_foundation_core_Classifier_core_Namespace, gen_foundation_core_Interface_Classifier, gen_foundation_core_Constraint_ModelElement, gen_foundation_core_Relationship_ModelElement, gen_foundation_core_Association_core_GeneralizableElement, gen_foundation_core_Association_core_Relationship, gen_foundation_core_Attribute_StructuralFeature, gen_foundation_core_BehavioralFeature_Feature, gen_foundation_core_Operation_BehavioralFeature, gen_foundation_core_Parameter_ModelElement, gen_foundation_core_Method_BehavioralFeature, gen_foundation_core_Generalization_Relationship, gen_foundation_core_Node_Classifier, gen_foundation_core_AssociationClass_core_Class, gen_foundation_core_AssociationClass_core_Association, gen_foundation_core_Dependency_Relationship, gen_foundation_core_Abstraction_Dependency, gen_foundation_core_PresentationElement_Element, gen_foundation_core_Usage_Dependency, gen_foundation_core_Binding_Dependency, gen_foundation_core_Component_Classifier, gen_foundation_core_EnumerationLiteral_ModelElement, gen_foundation_core_Permission_Dependency, gen_foundation_core_Comment_ModelElement, gen_foundation_core_Stereotype_GeneralizableElement, gen_foundation_core_Flow_Relationship, gen_foundation_core_Primitive_DataType, gen_foundation_core_Enumeration_DataType, gen_foundation_core_ProgrammingLanguageDataType_DataType, gen_foundation_core_Artifact_Classifier, gen_foundation_core_TagDefinition_ModelElement, gen_foundation_core_TaggedValue_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)