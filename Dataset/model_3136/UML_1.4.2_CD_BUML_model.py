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
OrderingKind: Enumeration = Enumeration(
    name="OrderingKind",
    literals={
            EnumerationLiteral(name="unordered"),
			EnumerationLiteral(name="ordered")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="package"),
			EnumerationLiteral(name="public")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="aggregate"),
			EnumerationLiteral(name="composite")
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

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
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

# Classes
UML_14_ModelElement = Class(name="UML::14::ModelElement", is_abstract=True)
Element = Class(name="Element")
UML_14_Comment = Class(name="UML::14::Comment")
UML_14_Dependency = Class(name="UML::14::Dependency")
UML_14_Feature = Class(name="UML::14::Feature", is_abstract=True)
ModelElement = Class(name="ModelElement")
UML_14_Classifier = Class(name="UML::14::Classifier", is_abstract=True)
UML_14_NameSpace = Class(name="UML::14::NameSpace", is_abstract=True)
UML_14_Constraint = Class(name="UML::14::Constraint", is_abstract=True)
UML_14_Parameter = Class(name="UML::14::Parameter", is_abstract=True)
UML_14_BehavioralFeature = Class(name="UML::14::BehavioralFeature", is_abstract=True)
UML_14_GeneralizableElement = Class(name="UML::14::GeneralizableElement", is_abstract=True)
UML_14_Generalization = Class(name="UML::14::Generalization")
UML_14_StructuralFeature = Class(name="UML::14::StructuralFeature", is_abstract=True)
UML_14_AssociationEnd = Class(name="UML::14::AssociationEnd")
NameSpace = Class(name="NameSpace")
GeneralizableElement = Class(name="GeneralizableElement")
UML_14_Multiplicity = Class(name="UML::14::Multiplicity")
UML_14_MultiplicityRange = Class(name="UML::14::MultiplicityRange")
Feature = Class(name="Feature")
UML_14_Method = Class(name="UML::14::Method")
UML_14_Attribute = Class(name="UML::14::Attribute")
StructuralFeature = Class(name="StructuralFeature")
UML_14_Relationship = Class(name="UML::14::Relationship", is_abstract=True)
Relationship = Class(name="Relationship")
UML_14_Operation = Class(name="UML::14::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
UML_14_Association = Class(name="UML::14::Association")
UML_14_Class = Class(name="UML::14::Class")
UML_14_DataType = Class(name="UML::14::DataType")
Classifier = Class(name="Classifier")
UML_14_Primitive = Class(name="UML::14::Primitive")
DataType = Class(name="DataType")
UML_14_AssociationClass = Class(name="UML::14::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
UML_14_Element = Class(name="UML::14::Element", is_abstract=True)
UML_14_Binding = Class(name="UML::14::Binding")
Dependency = Class(name="Dependency")
UML_14_Abstraction = Class(name="UML::14::Abstraction")
UML_14_Usage = Class(name="UML::14::Usage")
UML_14_Permission = Class(name="UML::14::Permission")
UML_14_Interface = Class(name="UML::14::Interface")
UML_14_Enumeration = Class(name="UML::14::Enumeration")
UML_14_EnumerationLiteral = Class(name="UML::14::EnumerationLiteral")
UML_14_ElementOwnership = Class(name="UML::14::ElementOwnership")

# UML_14_ModelElement class attributes and methods
UML_14_ModelElement_name: Property = Property(name="name", type=StringType)
UML_14_ModelElement.attributes={UML_14_ModelElement_name}

# Element class attributes and methods

# UML_14_Comment class attributes and methods
UML_14_Comment_body: Property = Property(name="body", type=StringType)
UML_14_Comment.attributes={UML_14_Comment_body}

# UML_14_Dependency class attributes and methods

# UML_14_Feature class attributes and methods

# ModelElement class attributes and methods

# UML_14_Classifier class attributes and methods

# UML_14_NameSpace class attributes and methods

# UML_14_Constraint class attributes and methods
UML_14_Constraint_body: Property = Property(name="body", type=StringType)
UML_14_Constraint.attributes={UML_14_Constraint_body}

# UML_14_Parameter class attributes and methods
UML_14_Parameter_kind: Property = Property(name="kind", type=StringType)
UML_14_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
UML_14_Parameter.attributes={UML_14_Parameter_defaultValue, UML_14_Parameter_kind}

# UML_14_BehavioralFeature class attributes and methods
UML_14_BehavioralFeature_isQuery: Property = Property(name="isQuery", type=BooleanType)
UML_14_BehavioralFeature.attributes={UML_14_BehavioralFeature_isQuery}

# UML_14_GeneralizableElement class attributes and methods
UML_14_GeneralizableElement_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML_14_GeneralizableElement.attributes={UML_14_GeneralizableElement_isAbstract}

# UML_14_Generalization class attributes and methods
UML_14_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
UML_14_Generalization.attributes={UML_14_Generalization_discriminator}

# UML_14_StructuralFeature class attributes and methods

# UML_14_AssociationEnd class attributes and methods
UML_14_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=BooleanType)
UML_14_AssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
UML_14_AssociationEnd_visibility: Property = Property(name="visibility", type=StringType)
UML_14_AssociationEnd_targetScope: Property = Property(name="targetScope", type=StringType)
UML_14_AssociationEnd_changeability: Property = Property(name="changeability", type=StringType)
UML_14_AssociationEnd.attributes={UML_14_AssociationEnd_isNavigable, UML_14_AssociationEnd_targetScope, UML_14_AssociationEnd_aggregation, UML_14_AssociationEnd_changeability, UML_14_AssociationEnd_visibility}

# NameSpace class attributes and methods

# GeneralizableElement class attributes and methods

# UML_14_Multiplicity class attributes and methods

# UML_14_MultiplicityRange class attributes and methods
UML_14_MultiplicityRange_lower: Property = Property(name="lower", type=IntegerType)
UML_14_MultiplicityRange_upper: Property = Property(name="upper", type=IntegerType)
UML_14_MultiplicityRange.attributes={UML_14_MultiplicityRange_upper, UML_14_MultiplicityRange_lower}

# Feature class attributes and methods

# UML_14_Method class attributes and methods
UML_14_Method_body: Property = Property(name="body", type=StringType)
UML_14_Method.attributes={UML_14_Method_body}

# UML_14_Attribute class attributes and methods
UML_14_Attribute_initialValue: Property = Property(name="initialValue", type=StringType)
UML_14_Attribute.attributes={UML_14_Attribute_initialValue}

# StructuralFeature class attributes and methods

# UML_14_Relationship class attributes and methods

# Relationship class attributes and methods

# UML_14_Operation class attributes and methods
UML_14_Operation_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
UML_14_Operation_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML_14_Operation_specification: Property = Property(name="specification", type=StringType)
UML_14_Operation_isRoot: Property = Property(name="isRoot", type=BooleanType)
UML_14_Operation.attributes={UML_14_Operation_specification, UML_14_Operation_isRoot, UML_14_Operation_isAbstract, UML_14_Operation_isLeaf}

# BehavioralFeature class attributes and methods

# UML_14_Association class attributes and methods

# UML_14_Class class attributes and methods

# UML_14_DataType class attributes and methods

# Classifier class attributes and methods

# UML_14_Primitive class attributes and methods

# DataType class attributes and methods

# UML_14_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# UML_14_Element class attributes and methods

# UML_14_Binding class attributes and methods

# Dependency class attributes and methods

# UML_14_Abstraction class attributes and methods

# UML_14_Usage class attributes and methods

# UML_14_Permission class attributes and methods

# UML_14_Interface class attributes and methods

# UML_14_Enumeration class attributes and methods

# UML_14_EnumerationLiteral class attributes and methods

# UML_14_ElementOwnership class attributes and methods
UML_14_ElementOwnership_visibility: Property = Property(name="visibility", type=StringType)
UML_14_ElementOwnership_isSpecification: Property = Property(name="isSpecification", type=BooleanType)
UML_14_ElementOwnership.attributes={UML_14_ElementOwnership_isSpecification, UML_14_ElementOwnership_visibility}

# Relationships
constraint0: BinaryAssociation = BinaryAssociation(
    name="constraint0",
    ends={
        Property(name="constrainedElement", type=UML_14_Constraint, multiplicity=Multiplicity(0, 9999)),
        Property(name="Constraint", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
comments1: BinaryAssociation = BinaryAssociation(
    name="comments1",
    ends={
        Property(name="Comment", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedElement", type=UML_14_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
supplierDependency2: BinaryAssociation = BinaryAssociation(
    name="supplierDependency2",
    ends={
        Property(name="Dependency", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier", type=UML_14_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
clientDependency3: BinaryAssociation = BinaryAssociation(
    name="clientDependency3",
    ends={
        Property(name="Dependency4", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=UML_14_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Classifier", type=UML_14_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=UML_14_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization6: BinaryAssociation = BinaryAssociation(
    name="generalization6",
    ends={
        Property(name="Generalization", type=UML_14_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=UML_14_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
specialization7: BinaryAssociation = BinaryAssociation(
    name="specialization7",
    ends={
        Property(name="Generalization8", type=UML_14_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=UML_14_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="Classifier10", type=UML_14_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typedParameter", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
feature11: BinaryAssociation = BinaryAssociation(
    name="feature11",
    ends={
        Property(name="BehavioralFeature", type=UML_14_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=UML_14_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement12: BinaryAssociation = BinaryAssociation(
    name="constrainedElement12",
    ends={
        Property(name="ModelElement", type=UML_14_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=UML_14_ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature13: BinaryAssociation = BinaryAssociation(
    name="feature13",
    ends={
        Property(name="Feature", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=UML_14_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedParameter14: BinaryAssociation = BinaryAssociation(
    name="typedParameter14",
    ends={
        Property(name="Parameter", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=UML_14_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
typedFeature15: BinaryAssociation = BinaryAssociation(
    name="typedFeature15",
    ends={
        Property(name="StructuralFeature", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="type16", type=UML_14_StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeRange17: BinaryAssociation = BinaryAssociation(
    name="powertypeRange17",
    ends={
        Property(name="Generalization18", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=UML_14_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
association19: BinaryAssociation = BinaryAssociation(
    name="association19",
    ends={
        Property(name="AssociationEnd", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="participant", type=UML_14_AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
specifiedEnd20: BinaryAssociation = BinaryAssociation(
    name="specifiedEnd20",
    ends={
        Property(name="AssociationEnd21", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=UML_14_AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity24: BinaryAssociation = BinaryAssociation(
    name="multiplicity24",
    ends={
        Property(name="UML_14_Multiplicity", type=UML_14_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_StructuralFeature", type=UML_14_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter25: BinaryAssociation = BinaryAssociation(
    name="parameter25",
    ends={
        Property(name="Parameter27", type=UML_14_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature26", type=UML_14_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range28: BinaryAssociation = BinaryAssociation(
    name="range28",
    ends={
        Property(name="MultiplicityRange", type=UML_14_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="multiplicity", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="Classifier23", type=UML_14_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="typedFeature", type=UML_14_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operation30: BinaryAssociation = BinaryAssociation(
    name="operation30",
    ends={
        Property(name="UML_14_Operation", type=UML_14_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Method", type=UML_14_Operation, multiplicity=Multiplicity(1, 9999))
    }
)
associationEnd31: BinaryAssociation = BinaryAssociation(
    name="associationEnd31",
    ends={
        Property(name="AssociationEnd32", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=UML_14_AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity29: BinaryAssociation = BinaryAssociation(
    name="multiplicity29",
    ends={
        Property(name="Multiplicity", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="range", type=UML_14_Multiplicity, multiplicity=Multiplicity(1, 1))
    }
)
parent34: BinaryAssociation = BinaryAssociation(
    name="parent34",
    ends={
        Property(name="GeneralizableElement35", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="specialization", type=UML_14_GeneralizableElement, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicity46: BinaryAssociation = BinaryAssociation(
    name="multiplicity46",
    ends={
        Property(name="UML_14_Multiplicity47", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd", type=UML_14_Multiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
powertype36: BinaryAssociation = BinaryAssociation(
    name="powertype36",
    ends={
        Property(name="Classifier37", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeRange", type=UML_14_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
connection38: BinaryAssociation = BinaryAssociation(
    name="connection38",
    ends={
        Property(name="AssociationEnd39", type=UML_14_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
association40: BinaryAssociation = BinaryAssociation(
    name="association40",
    ends={
        Property(name="Association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=UML_14_Association, multiplicity=Multiplicity(1, 1))
    }
)
participant41: BinaryAssociation = BinaryAssociation(
    name="participant41",
    ends={
        Property(name="Classifier43", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="association42", type=UML_14_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
specification44: BinaryAssociation = BinaryAssociation(
    name="specification44",
    ends={
        Property(name="Classifier45", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedEnd", type=UML_14_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
child33: BinaryAssociation = BinaryAssociation(
    name="child33",
    ends={
        Property(name="GeneralizableElement", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=UML_14_GeneralizableElement, multiplicity=Multiplicity(0, 9999))
    }
)
qualifier48: BinaryAssociation = BinaryAssociation(
    name="qualifier48",
    ends={
        Property(name="Attribute", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=UML_14_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
supplier49: BinaryAssociation = BinaryAssociation(
    name="supplier49",
    ends={
        Property(name="ModelElement50", type=UML_14_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="supplierDependency", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
client51: BinaryAssociation = BinaryAssociation(
    name="client51",
    ends={
        Property(name="ModelElement52", type=UML_14_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=UML_14_ModelElement, multiplicity=Multiplicity(1, 9999))
    }
)
literal53: BinaryAssociation = BinaryAssociation(
    name="literal53",
    ends={
        Property(name="EnumerationLiteral", type=UML_14_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=UML_14_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumeration54: BinaryAssociation = BinaryAssociation(
    name="enumeration54",
    ends={
        Property(name="Enumeration", type=UML_14_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literal", type=UML_14_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
annotatedElement55: BinaryAssociation = BinaryAssociation(
    name="annotatedElement55",
    ends={
        Property(name="ModelElement56", type=UML_14_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=UML_14_ModelElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML_14_ModelElement_Element = Generalization(general=Element, specific=UML_14_ModelElement)
gen_UML_14_Feature_ModelElement = Generalization(general=ModelElement, specific=UML_14_Feature)
gen_UML_14_NameSpace_ModelElement = Generalization(general=ModelElement, specific=UML_14_NameSpace)
gen_UML_14_Parameter_ModelElement = Generalization(general=ModelElement, specific=UML_14_Parameter)
gen_UML_14_Constraint_ModelElement = Generalization(general=ModelElement, specific=UML_14_Constraint)
gen_UML_14_GeneralizableElement_ModelElement = Generalization(general=ModelElement, specific=UML_14_GeneralizableElement)
gen_UML_14_Classifier_GeneralizableElement = Generalization(general=GeneralizableElement, specific=UML_14_Classifier)
gen_UML_14_Classifier_NameSpace = Generalization(general=NameSpace, specific=UML_14_Classifier)
gen_UML_14_BehavioralFeature_Feature = Generalization(general=Feature, specific=UML_14_BehavioralFeature)
gen_UML_14_StructuralFeature_Feature = Generalization(general=Feature, specific=UML_14_StructuralFeature)
gen_UML_14_Method_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML_14_Method)
gen_UML_14_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=UML_14_Attribute)
gen_UML_14_Relationship_ModelElement = Generalization(general=ModelElement, specific=UML_14_Relationship)
gen_UML_14_Generalization_Relationship = Generalization(general=Relationship, specific=UML_14_Generalization)
gen_UML_14_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML_14_Operation)
gen_UML_14_Association_Relationship = Generalization(general=Relationship, specific=UML_14_Association)
gen_UML_14_Association_GeneralizableElement = Generalization(general=GeneralizableElement, specific=UML_14_Association)
gen_UML_14_AssociationEnd_ModelElement = Generalization(general=ModelElement, specific=UML_14_AssociationEnd)
gen_UML_14_Interface_Classifier = Generalization(general=Classifier, specific=UML_14_Interface)
gen_UML_14_DataType_Classifier = Generalization(general=Classifier, specific=UML_14_DataType)
gen_UML_14_Class_Classifier = Generalization(general=Classifier, specific=UML_14_Class)
gen_UML_14_AssociationClass_Class = Generalization(general=Class_, specific=UML_14_AssociationClass)
gen_UML_14_AssociationClass_Association = Generalization(general=Association, specific=UML_14_AssociationClass)
gen_UML_14_Dependency_Relationship = Generalization(general=Relationship, specific=UML_14_Dependency)
gen_UML_14_Binding_Dependency = Generalization(general=Dependency, specific=UML_14_Binding)
gen_UML_14_Abstraction_Dependency = Generalization(general=Dependency, specific=UML_14_Abstraction)
gen_UML_14_Usage_Dependency = Generalization(general=Dependency, specific=UML_14_Usage)
gen_UML_14_Permission_Dependency = Generalization(general=Dependency, specific=UML_14_Permission)
gen_UML_14_Primitive_DataType = Generalization(general=DataType, specific=UML_14_Primitive)
gen_UML_14_Enumeration_DataType = Generalization(general=DataType, specific=UML_14_Enumeration)
gen_UML_14_EnumerationLiteral_ModelElement = Generalization(general=ModelElement, specific=UML_14_EnumerationLiteral)

# Domain Model
domain_model = DomainModel(
    name="UML_14",
    types={UML_14_ModelElement, Element, UML_14_Comment, UML_14_Dependency, UML_14_Feature, ModelElement, UML_14_Classifier, UML_14_NameSpace, UML_14_Constraint, UML_14_Parameter, UML_14_BehavioralFeature, UML_14_GeneralizableElement, UML_14_Generalization, UML_14_StructuralFeature, UML_14_AssociationEnd, NameSpace, GeneralizableElement, UML_14_Multiplicity, UML_14_MultiplicityRange, Feature, UML_14_Method, UML_14_Attribute, StructuralFeature, UML_14_Relationship, Relationship, UML_14_Operation, BehavioralFeature, UML_14_Association, UML_14_Class, UML_14_DataType, Classifier, UML_14_Primitive, DataType, UML_14_AssociationClass, Class_, Association, UML_14_Element, UML_14_Binding, Dependency, UML_14_Abstraction, UML_14_Usage, UML_14_Permission, UML_14_Interface, UML_14_Enumeration, UML_14_EnumerationLiteral, UML_14_ElementOwnership, OrderingKind, VisibilityKind, AggregationKind, ChangeableKind, ScopeKind, ParameterDirectionKind},
    associations={constraint0, comments1, supplierDependency2, clientDependency3, owner5, generalization6, specialization7, type9, feature11, constrainedElement12, feature13, typedParameter14, typedFeature15, powertypeRange17, association19, specifiedEnd20, multiplicity24, parameter25, range28, type22, operation30, associationEnd31, multiplicity29, parent34, multiplicity46, powertype36, connection38, association40, participant41, specification44, child33, qualifier48, supplier49, client51, literal53, enumeration54, annotatedElement55},
    generalizations={gen_UML_14_ModelElement_Element, gen_UML_14_Feature_ModelElement, gen_UML_14_NameSpace_ModelElement, gen_UML_14_Parameter_ModelElement, gen_UML_14_Constraint_ModelElement, gen_UML_14_GeneralizableElement_ModelElement, gen_UML_14_Classifier_GeneralizableElement, gen_UML_14_Classifier_NameSpace, gen_UML_14_BehavioralFeature_Feature, gen_UML_14_StructuralFeature_Feature, gen_UML_14_Method_BehavioralFeature, gen_UML_14_Attribute_StructuralFeature, gen_UML_14_Relationship_ModelElement, gen_UML_14_Generalization_Relationship, gen_UML_14_Operation_BehavioralFeature, gen_UML_14_Association_Relationship, gen_UML_14_Association_GeneralizableElement, gen_UML_14_AssociationEnd_ModelElement, gen_UML_14_Interface_Classifier, gen_UML_14_DataType_Classifier, gen_UML_14_Class_Classifier, gen_UML_14_AssociationClass_Class, gen_UML_14_AssociationClass_Association, gen_UML_14_Dependency_Relationship, gen_UML_14_Binding_Dependency, gen_UML_14_Abstraction_Dependency, gen_UML_14_Usage_Dependency, gen_UML_14_Permission_Dependency, gen_UML_14_Primitive_DataType, gen_UML_14_Enumeration_DataType, gen_UML_14_EnumerationLiteral_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)