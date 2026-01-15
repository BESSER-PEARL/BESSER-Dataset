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

# Classes
classes_ValueSpecification = Class(name="classes::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
classes_TypedElement = Class(name="classes::TypedElement")
NamedElement = Class(name="NamedElement")
classes_Type = Class(name="classes::Type", is_abstract=True)
classes_NamedElement = Class(name="classes::NamedElement", is_abstract=True)
Element = Class(name="Element")
classes_Element = Class(name="classes::Element", is_abstract=True)
classes_Comment = Class(name="classes::Comment")
classes_Namespace = Class(name="classes::Namespace", is_abstract=True)
classes_PackageableElement = Class(name="classes::PackageableElement", is_abstract=True)
classes_Package = Class(name="classes::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
classes_ElementImport = Class(name="classes::ElementImport")
classes_PackageImport = Class(name="classes::PackageImport")
classes_StructuralFeature = Class(name="classes::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
classes_Feature = Class(name="classes::Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
classes_Classifier = Class(name="classes::Classifier", is_abstract=True)
classes_RedefinableElement = Class(name="classes::RedefinableElement", is_abstract=True)
Type = Class(name="Type")
classes_Generalization = Class(name="classes::Generalization")
classes_Property = Class(name="classes::Property")
StructuralFeature = Class(name="StructuralFeature")
classes_Association = Class(name="classes::Association")
classes_DataType = Class(name="classes::DataType")
Classifier = Class(name="Classifier")
classes_Class = Class(name="classes::Class")
classes_MultiplicityElement = Class(name="classes::MultiplicityElement")
classes_BehavioralFeature = Class(name="classes::BehavioralFeature", is_abstract=True)
classes_Parameter = Class(name="classes::Parameter")
classes_Operation = Class(name="classes::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
classes_InstanceSpecification = Class(name="classes::InstanceSpecification")
classes_Slot = Class(name="classes::Slot")
classes_InstanceValue = Class(name="classes::InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
classes_LiteralBoolean = Class(name="classes::LiteralBoolean")
LiteralSpecification = Class(name="LiteralSpecification")
classes_LiteralInteger = Class(name="classes::LiteralInteger")
classes_LiteralNull = Class(name="classes::LiteralNull")
classes_LiteralString = Class(name="classes::LiteralString")
classes_LiteralUnlimitedNatural = Class(name="classes::LiteralUnlimitedNatural")
classes_PrimitiveType = Class(name="classes::PrimitiveType")
DataType = Class(name="DataType")
classes_Enumeration = Class(name="classes::Enumeration")
classes_LiteralSpecification = Class(name="classes::LiteralSpecification", is_abstract=True)
classes_Model = Class(name="classes::Model")
Package = Class(name="Package")
classes_EnumerationLiteral = Class(name="classes::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")

# classes_ValueSpecification class attributes and methods
classes_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=IntegerType)
classes_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=BooleanType)
classes_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
classes_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=IntegerType)
classes_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=BooleanType)
classes_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_ValueSpecification.methods={classes_ValueSpecification_m_booleanValue, classes_ValueSpecification_m_isComputable, classes_ValueSpecification_m_integerValue, classes_ValueSpecification_m_stringValue, classes_ValueSpecification_m_isNull, classes_ValueSpecification_m_unlimitedValue}

# TypedElement class attributes and methods

# classes_TypedElement class attributes and methods

# NamedElement class attributes and methods

# classes_Type class attributes and methods

# classes_NamedElement class attributes and methods
classes_NamedElement_name: Property = Property(name="name", type=StringType)
classes_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
classes_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
classes_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=StringType)
classes_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
classes_NamedElement.attributes={classes_NamedElement_name, classes_NamedElement_visibility, classes_NamedElement_qualifiedName}
classes_NamedElement.methods={classes_NamedElement_m_allNamespaces, classes_NamedElement_m_separator}

# Element class attributes and methods

# classes_Element class attributes and methods
classes_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
classes_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=BooleanType)
classes_Element.methods={classes_Element_m_allOwnedElements, classes_Element_m_mustBeOwned}

# classes_Comment class attributes and methods
classes_Comment_body: Property = Property(name="body", type=StringType)
classes_Comment.attributes={classes_Comment_body}

# classes_Namespace class attributes and methods

# classes_PackageableElement class attributes and methods

# classes_Package class attributes and methods

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# classes_ElementImport class attributes and methods
classes_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
classes_ElementImport_alias: Property = Property(name="alias", type=StringType)
classes_ElementImport.attributes={classes_ElementImport_visibility, classes_ElementImport_alias}

# classes_PackageImport class attributes and methods
classes_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
classes_PackageImport.attributes={classes_PackageImport_visibility}

# classes_StructuralFeature class attributes and methods
classes_StructuralFeature_readOnly: Property = Property(name="readOnly", type=BooleanType)
classes_StructuralFeature.attributes={classes_StructuralFeature_readOnly}

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# classes_Feature class attributes and methods
classes_Feature_static: Property = Property(name="static", type=BooleanType)
classes_Feature.attributes={classes_Feature_static}

# RedefinableElement class attributes and methods

# classes_Classifier class attributes and methods
classes_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
classes_Classifier_finalSpecialization: Property = Property(name="finalSpecialization", type=BooleanType)
classes_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=Feature)
classes_Classifier.attributes={classes_Classifier_abstract, classes_Classifier_finalSpecialization}
classes_Classifier.methods={classes_Classifier_m_allFeatures}

# classes_RedefinableElement class attributes and methods
classes_RedefinableElement_leaf: Property = Property(name="leaf", type=BooleanType)
classes_RedefinableElement.attributes={classes_RedefinableElement_leaf}

# Type class attributes and methods

# classes_Generalization class attributes and methods
classes_Generalization_substitutable: Property = Property(name="substitutable", type=BooleanType)
classes_Generalization.attributes={classes_Generalization_substitutable}

# classes_Property class attributes and methods
classes_Property_derived: Property = Property(name="derived", type=BooleanType)
classes_Property_derivedUnion: Property = Property(name="derivedUnion", type=BooleanType)
classes_Property_aggregation: Property = Property(name="aggregation", type=StringType)
classes_Property_composite: Property = Property(name="composite", type=BooleanType)
classes_Property.attributes={classes_Property_aggregation, classes_Property_derived, classes_Property_composite, classes_Property_derivedUnion}

# StructuralFeature class attributes and methods

# classes_Association class attributes and methods
classes_Association_derived: Property = Property(name="derived", type=BooleanType)
classes_Association.attributes={classes_Association_derived}

# classes_DataType class attributes and methods

# Classifier class attributes and methods

# classes_Class class attributes and methods
classes_Class_active: Property = Property(name="active", type=BooleanType)
classes_Class.attributes={classes_Class_active}

# classes_MultiplicityElement class attributes and methods
classes_MultiplicityElement_ordered: Property = Property(name="ordered", type=BooleanType)
classes_MultiplicityElement_unique: Property = Property(name="unique", type=BooleanType)
classes_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
classes_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
classes_MultiplicityElement_m_lowerBound: Method = Method(name="lowerBound", parameters={}, type=IntegerType)
classes_MultiplicityElement_m_upperBound: Method = Method(name="upperBound", parameters={}, type=IntegerType)
classes_MultiplicityElement.attributes={classes_MultiplicityElement_unique, classes_MultiplicityElement_upper, classes_MultiplicityElement_ordered, classes_MultiplicityElement_lower}
classes_MultiplicityElement.methods={classes_MultiplicityElement_m_upperBound, classes_MultiplicityElement_m_lowerBound}

# classes_BehavioralFeature class attributes and methods
classes_BehavioralFeature_abstract: Property = Property(name="abstract", type=BooleanType)
classes_BehavioralFeature.attributes={classes_BehavioralFeature_abstract}

# classes_Parameter class attributes and methods
classes_Parameter_direction: Property = Property(name="direction", type=StringType)
classes_Parameter.attributes={classes_Parameter_direction}

# classes_Operation class attributes and methods
classes_Operation_query: Property = Property(name="query", type=BooleanType)
classes_Operation_ordered: Property = Property(name="ordered", type=BooleanType)
classes_Operation_unique: Property = Property(name="unique", type=BooleanType)
classes_Operation_lower: Property = Property(name="lower", type=StringType)
classes_Operation_upper: Property = Property(name="upper", type=StringType)
classes_Operation_m_returnResult: Method = Method(name="returnResult", parameters={}, type=StringType)
classes_Operation.attributes={classes_Operation_query, classes_Operation_ordered, classes_Operation_unique, classes_Operation_lower, classes_Operation_upper}
classes_Operation.methods={classes_Operation_m_returnResult}

# BehavioralFeature class attributes and methods

# classes_InstanceSpecification class attributes and methods

# classes_Slot class attributes and methods

# classes_InstanceValue class attributes and methods

# ValueSpecification class attributes and methods

# classes_LiteralBoolean class attributes and methods
classes_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
classes_LiteralBoolean_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=BooleanType)
classes_LiteralBoolean_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_LiteralBoolean.attributes={classes_LiteralBoolean_value}
classes_LiteralBoolean.methods={classes_LiteralBoolean_m_isComputable, classes_LiteralBoolean_m_booleanValue}

# LiteralSpecification class attributes and methods

# classes_LiteralInteger class attributes and methods
classes_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
classes_LiteralInteger_m_integerValue: Method = Method(name="integerValue", parameters={}, type=IntegerType)
classes_LiteralInteger_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_LiteralInteger.attributes={classes_LiteralInteger_value}
classes_LiteralInteger.methods={classes_LiteralInteger_m_integerValue, classes_LiteralInteger_m_isComputable}

# classes_LiteralNull class attributes and methods
classes_LiteralNull_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_LiteralNull_m_isNull: Method = Method(name="isNull", parameters={}, type=BooleanType)
classes_LiteralNull.methods={classes_LiteralNull_m_isNull, classes_LiteralNull_m_isComputable}

# classes_LiteralString class attributes and methods
classes_LiteralString_value: Property = Property(name="value", type=StringType)
classes_LiteralString_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_LiteralString_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
classes_LiteralString.attributes={classes_LiteralString_value}
classes_LiteralString.methods={classes_LiteralString_m_isComputable, classes_LiteralString_m_stringValue}

# classes_LiteralUnlimitedNatural class attributes and methods
classes_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
classes_LiteralUnlimitedNatural_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
classes_LiteralUnlimitedNatural_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=IntegerType)
classes_LiteralUnlimitedNatural.attributes={classes_LiteralUnlimitedNatural_value}
classes_LiteralUnlimitedNatural.methods={classes_LiteralUnlimitedNatural_m_isComputable, classes_LiteralUnlimitedNatural_m_unlimitedValue}

# classes_PrimitiveType class attributes and methods

# DataType class attributes and methods

# classes_Enumeration class attributes and methods

# classes_LiteralSpecification class attributes and methods

# classes_Model class attributes and methods

# Package class attributes and methods

# classes_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="classes_Type", type=classes_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_TypedElement", type=classes_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement3: BinaryAssociation = BinaryAssociation(
    name="ownedElement3",
    ends={
        Property(name="Element", type=classes_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=classes_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Element6", type=classes_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=classes_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment7: BinaryAssociation = BinaryAssociation(
    name="ownedComment7",
    ends={
        Property(name="classes_Comment", type=classes_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Element", type=classes_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement8: BinaryAssociation = BinaryAssociation(
    name="annotatedElement8",
    ends={
        Property(name="classes_Element10", type=classes_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Comment9", type=classes_Element, multiplicity=Multiplicity(0, 9999))
    }
)
namespace1: BinaryAssociation = BinaryAssociation(
    name="namespace1",
    ends={
        Property(name="Namespace", type=classes_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=classes_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
importedMember15: BinaryAssociation = BinaryAssociation(
    name="importedMember15",
    ends={
        Property(name="classes_PackageableElement", type=classes_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Namespace16", type=classes_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember17: BinaryAssociation = BinaryAssociation(
    name="ownedMember17",
    ends={
        Property(name="NamedElement", type=classes_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=classes_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedElement18: BinaryAssociation = BinaryAssociation(
    name="importedElement18",
    ends={
        Property(name="classes_PackageableElement19", type=classes_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_ElementImport", type=classes_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace20: BinaryAssociation = BinaryAssociation(
    name="importingNamespace20",
    ends={
        Property(name="Namespace21", type=classes_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=classes_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage22: BinaryAssociation = BinaryAssociation(
    name="importedPackage22",
    ends={
        Property(name="classes_Package", type=classes_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_PackageImport", type=classes_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace23: BinaryAssociation = BinaryAssociation(
    name="importingNamespace23",
    ends={
        Property(name="Namespace24", type=classes_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=classes_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
member11: BinaryAssociation = BinaryAssociation(
    name="member11",
    ends={
        Property(name="classes_NamedElement", type=classes_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Namespace", type=classes_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport12: BinaryAssociation = BinaryAssociation(
    name="elementImport12",
    ends={
        Property(name="ElementImport", type=classes_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=classes_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport13: BinaryAssociation = BinaryAssociation(
    name="packageImport13",
    ends={
        Property(name="PackageImport", type=classes_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace14", type=classes_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage30: BinaryAssociation = BinaryAssociation(
    name="nestedPackage30",
    ends={
        Property(name="nestingPackage", type=classes_Package, multiplicity=Multiplicity(0, 9999)),
        Property(name="Package", type=classes_Package, multiplicity=Multiplicity(1, 1))
    }
)
nestingPackage32: BinaryAssociation = BinaryAssociation(
    name="nestingPackage32",
    ends={
        Property(name="Package33", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=classes_Package, multiplicity=Multiplicity(0, 1))
    }
)
package34: BinaryAssociation = BinaryAssociation(
    name="package34",
    ends={
        Property(name="Package35", type=classes_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=classes_Package, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier36: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier36",
    ends={
        Property(name="Classifier", type=classes_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=classes_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement25: BinaryAssociation = BinaryAssociation(
    name="packagedElement25",
    ends={
        Property(name="classes_PackageableElement27", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Package26", type=classes_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType28: BinaryAssociation = BinaryAssociation(
    name="ownedType28",
    ends={
        Property(name="Type", type=classes_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=classes_Type, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext39: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext39",
    ends={
        Property(name="classes_Classifier", type=classes_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_RedefinableElement40", type=classes_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization41: BinaryAssociation = BinaryAssociation(
    name="generalization41",
    ends={
        Property(name="Generalization", type=classes_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=classes_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature42: BinaryAssociation = BinaryAssociation(
    name="feature42",
    ends={
        Property(name="Feature", type=classes_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=classes_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember43: BinaryAssociation = BinaryAssociation(
    name="inheritedMember43",
    ends={
        Property(name="classes_NamedElement45", type=classes_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Classifier44", type=classes_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute46: BinaryAssociation = BinaryAssociation(
    name="attribute46",
    ends={
        Property(name="classes_Property", type=classes_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Classifier47", type=classes_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement38: BinaryAssociation = BinaryAssociation(
    name="redefinedElement38",
    ends={
        Property(name="classes_RedefinableElement", type=classes_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_RedefinableElement37", type=classes_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
specific53: BinaryAssociation = BinaryAssociation(
    name="specific53",
    ends={
        Property(name="Classifier54", type=classes_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=classes_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owningAssociation55: BinaryAssociation = BinaryAssociation(
    name="owningAssociation55",
    ends={
        Property(name="Association", type=classes_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=classes_Association, multiplicity=Multiplicity(0, 1))
    }
)
association56: BinaryAssociation = BinaryAssociation(
    name="association56",
    ends={
        Property(name="Association57", type=classes_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=classes_Association, multiplicity=Multiplicity(0, 1))
    }
)
general49: BinaryAssociation = BinaryAssociation(
    name="general49",
    ends={
        Property(name="classes_Classifier50", type=classes_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Classifier48", type=classes_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general51: BinaryAssociation = BinaryAssociation(
    name="general51",
    ends={
        Property(name="classes_Classifier52", type=classes_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Generalization", type=classes_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
opposite62: BinaryAssociation = BinaryAssociation(
    name="opposite62",
    ends={
        Property(name="classes_Property63", type=classes_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Property61", type=classes_Property, multiplicity=Multiplicity(0, 1))
    }
)
endType64: BinaryAssociation = BinaryAssociation(
    name="endType64",
    ends={
        Property(name="classes_Type65", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association", type=classes_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd66: BinaryAssociation = BinaryAssociation(
    name="memberEnd66",
    ends={
        Property(name="Property", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=classes_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableOwnedEnd67: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd67",
    ends={
        Property(name="classes_Property69", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Association68", type=classes_Property, multiplicity=Multiplicity(0, 9999))
    }
)
datatype58: BinaryAssociation = BinaryAssociation(
    name="datatype58",
    ends={
        Property(name="DataType", type=classes_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=classes_DataType, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd70: BinaryAssociation = BinaryAssociation(
    name="ownedEnd70",
    ends={
        Property(name="Property71", type=classes_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=classes_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class59: BinaryAssociation = BinaryAssociation(
    name="class59",
    ends={
        Property(name="Class", type=classes_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute60", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
upperValue74: BinaryAssociation = BinaryAssociation(
    name="upperValue74",
    ends={
        Property(name="classes_ValueSpecification", type=classes_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_MultiplicityElement", type=classes_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue75: BinaryAssociation = BinaryAssociation(
    name="lowerValue75",
    ends={
        Property(name="classes_ValueSpecification77", type=classes_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_MultiplicityElement76", type=classes_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameter78: BinaryAssociation = BinaryAssociation(
    name="ownedParameter78",
    ends={
        Property(name="classes_Parameter", type=classes_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_BehavioralFeature", type=classes_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute72: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute72",
    ends={
        Property(name="Property73", type=classes_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=classes_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class79: BinaryAssociation = BinaryAssociation(
    name="class79",
    ends={
        Property(name="Class80", type=classes_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=classes_Class, multiplicity=Multiplicity(0, 1))
    }
)
classifier86: BinaryAssociation = BinaryAssociation(
    name="classifier86",
    ends={
        Property(name="classes_Classifier87", type=classes_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_InstanceSpecification", type=classes_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot88: BinaryAssociation = BinaryAssociation(
    name="slot88",
    ends={
        Property(name="Slot", type=classes_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=classes_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature89: BinaryAssociation = BinaryAssociation(
    name="definingFeature89",
    ends={
        Property(name="classes_StructuralFeature", type=classes_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Slot", type=classes_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="classes_ValueSpecification92", type=classes_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Slot91", type=classes_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance93: BinaryAssociation = BinaryAssociation(
    name="owningInstance93",
    ends={
        Property(name="InstanceSpecification", type=classes_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=classes_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance94: BinaryAssociation = BinaryAssociation(
    name="instance94",
    ends={
        Property(name="classes_InstanceSpecification95", type=classes_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_InstanceValue", type=classes_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
redefinedOperation82: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation82",
    ends={
        Property(name="classes_Operation", type=classes_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Operation81", type=classes_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="classes_Type85", type=classes_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Operation84", type=classes_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute98: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute98",
    ends={
        Property(name="Property99", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=classes_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation100: BinaryAssociation = BinaryAssociation(
    name="ownedOperation100",
    ends={
        Property(name="Operation", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class101", type=classes_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass103: BinaryAssociation = BinaryAssociation(
    name="superClass103",
    ends={
        Property(name="classes_Class", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class102", type=classes_Class, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier104: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier104",
    ends={
        Property(name="classes_Classifier106", type=classes_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classes_Class105", type=classes_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral96: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral96",
    ends={
        Property(name="EnumerationLiteral", type=classes_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=classes_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration97: BinaryAssociation = BinaryAssociation(
    name="enumeration97",
    ends={
        Property(name="Enumeration", type=classes_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=classes_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classes_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=classes_ValueSpecification)
gen_classes_TypedElement_NamedElement = Generalization(general=NamedElement, specific=classes_TypedElement)
gen_classes_NamedElement_Element = Generalization(general=Element, specific=classes_NamedElement)
gen_classes_ElementImport_Element = Generalization(general=Element, specific=classes_ElementImport)
gen_classes_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=classes_PackageableElement)
gen_classes_PackageImport_Element = Generalization(general=Element, specific=classes_PackageImport)
gen_classes_Namespace_NamedElement = Generalization(general=NamedElement, specific=classes_Namespace)
gen_classes_Package_Namespace = Generalization(general=Namespace, specific=classes_Package)
gen_classes_Package_PackageableElement = Generalization(general=PackageableElement, specific=classes_Package)
gen_classes_Type_PackageableElement = Generalization(general=PackageableElement, specific=classes_Type)
gen_classes_StructuralFeature_Feature = Generalization(general=Feature, specific=classes_StructuralFeature)
gen_classes_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=classes_StructuralFeature)
gen_classes_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=classes_StructuralFeature)
gen_classes_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=classes_Feature)
gen_classes_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=classes_RedefinableElement)
gen_classes_Classifier_Namespace = Generalization(general=Namespace, specific=classes_Classifier)
gen_classes_Classifier_Type = Generalization(general=Type, specific=classes_Classifier)
gen_classes_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=classes_Property)
gen_classes_Generalization_Element = Generalization(general=Element, specific=classes_Generalization)
gen_classes_Association_Classifier = Generalization(general=Classifier, specific=classes_Association)
gen_classes_MultiplicityElement_Element = Generalization(general=Element, specific=classes_MultiplicityElement)
gen_classes_BehavioralFeature_Feature = Generalization(general=Feature, specific=classes_BehavioralFeature)
gen_classes_DataType_Classifier = Generalization(general=Classifier, specific=classes_DataType)
gen_classes_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=classes_Operation)
gen_classes_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=classes_Parameter)
gen_classes_Parameter_TypedElement = Generalization(general=TypedElement, specific=classes_Parameter)
gen_classes_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=classes_InstanceSpecification)
gen_classes_Slot_Element = Generalization(general=Element, specific=classes_Slot)
gen_classes_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=classes_InstanceValue)
gen_classes_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=classes_LiteralInteger)
gen_classes_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=classes_LiteralNull)
gen_classes_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=classes_LiteralString)
gen_classes_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=classes_LiteralUnlimitedNatural)
gen_classes_PrimitiveType_DataType = Generalization(general=DataType, specific=classes_PrimitiveType)
gen_classes_Enumeration_DataType = Generalization(general=DataType, specific=classes_Enumeration)
gen_classes_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=classes_LiteralBoolean)
gen_classes_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=classes_LiteralSpecification)
gen_classes_Class_Classifier = Generalization(general=Classifier, specific=classes_Class)
gen_classes_Model_Package = Generalization(general=Package, specific=classes_Model)
gen_classes_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=classes_EnumerationLiteral)

# Domain Model
domain_model = DomainModel(
    name="classes",
    types={classes_ValueSpecification, TypedElement, classes_TypedElement, NamedElement, classes_Type, classes_NamedElement, Element, classes_Element, classes_Comment, classes_Namespace, classes_PackageableElement, classes_Package, Namespace, PackageableElement, classes_ElementImport, classes_PackageImport, classes_StructuralFeature, Feature, MultiplicityElement, classes_Feature, RedefinableElement, classes_Classifier, classes_RedefinableElement, Type, classes_Generalization, classes_Property, StructuralFeature, classes_Association, classes_DataType, Classifier, classes_Class, classes_MultiplicityElement, classes_BehavioralFeature, classes_Parameter, classes_Operation, BehavioralFeature, classes_InstanceSpecification, classes_Slot, classes_InstanceValue, ValueSpecification, classes_LiteralBoolean, LiteralSpecification, classes_LiteralInteger, classes_LiteralNull, classes_LiteralString, classes_LiteralUnlimitedNatural, classes_PrimitiveType, DataType, classes_Enumeration, classes_LiteralSpecification, classes_Model, Package, classes_EnumerationLiteral, InstanceSpecification, VisibilityKind, AggregationKind, ParameterDirectionKind},
    associations={type0, ownedElement3, owner5, ownedComment7, annotatedElement8, namespace1, importedMember15, ownedMember17, importedElement18, importingNamespace20, importedPackage22, importingNamespace23, member11, elementImport12, packageImport13, nestedPackage30, nestingPackage32, package34, featuringClassifier36, packagedElement25, ownedType28, redefinitionContext39, generalization41, feature42, inheritedMember43, attribute46, redefinedElement38, specific53, owningAssociation55, association56, general49, general51, opposite62, endType64, memberEnd66, navigableOwnedEnd67, datatype58, ownedEnd70, class59, upperValue74, lowerValue75, ownedParameter78, ownedAttribute72, class79, classifier86, slot88, definingFeature89, value90, owningInstance93, instance94, redefinedOperation82, type83, ownedAttribute98, ownedOperation100, superClass103, nestedClassifier104, ownedLiteral96, enumeration97},
    generalizations={gen_classes_ValueSpecification_TypedElement, gen_classes_TypedElement_NamedElement, gen_classes_NamedElement_Element, gen_classes_ElementImport_Element, gen_classes_PackageableElement_NamedElement, gen_classes_PackageImport_Element, gen_classes_Namespace_NamedElement, gen_classes_Package_Namespace, gen_classes_Package_PackageableElement, gen_classes_Type_PackageableElement, gen_classes_StructuralFeature_Feature, gen_classes_StructuralFeature_MultiplicityElement, gen_classes_StructuralFeature_TypedElement, gen_classes_Feature_RedefinableElement, gen_classes_RedefinableElement_NamedElement, gen_classes_Classifier_Namespace, gen_classes_Classifier_Type, gen_classes_Property_StructuralFeature, gen_classes_Generalization_Element, gen_classes_Association_Classifier, gen_classes_MultiplicityElement_Element, gen_classes_BehavioralFeature_Feature, gen_classes_DataType_Classifier, gen_classes_Operation_BehavioralFeature, gen_classes_Parameter_MultiplicityElement, gen_classes_Parameter_TypedElement, gen_classes_InstanceSpecification_NamedElement, gen_classes_Slot_Element, gen_classes_InstanceValue_ValueSpecification, gen_classes_LiteralInteger_LiteralSpecification, gen_classes_LiteralNull_LiteralSpecification, gen_classes_LiteralString_LiteralSpecification, gen_classes_LiteralUnlimitedNatural_LiteralSpecification, gen_classes_PrimitiveType_DataType, gen_classes_Enumeration_DataType, gen_classes_LiteralBoolean_LiteralSpecification, gen_classes_LiteralSpecification_ValueSpecification, gen_classes_Class_Classifier, gen_classes_Model_Package, gen_classes_EnumerationLiteral_InstanceSpecification},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)