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

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
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

# Classes
uml2CD_Element = Class(name="uml2CD::Element", is_abstract=True)
uml2CD_Relationship = Class(name="uml2CD::Relationship", is_abstract=True)
Element = Class(name="Element")
uml2CD_DirectRelationship = Class(name="uml2CD::DirectRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
uml2CD_NamedElement = Class(name="uml2CD::NamedElement")
uml2CD_Namespace = Class(name="uml2CD::Namespace", is_abstract=True)
uml2CD_Dependency = Class(name="uml2CD::Dependency")
uml2CD_PackageableElement = Class(name="uml2CD::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
uml2CD_Comment = Class(name="uml2CD::Comment")
uml2CD_Package = Class(name="uml2CD::Package")
uml2CD_PackageImport = Class(name="uml2CD::PackageImport")
uml2CD_ElementImport = Class(name="uml2CD::ElementImport")
uml2CD_Constraint = Class(name="uml2CD::Constraint")
DirectRelationship = Class(name="DirectRelationship")
PackageableElement = Class(name="PackageableElement")
Namespace = Class(name="Namespace")
uml2CD_PackageMerge = Class(name="uml2CD::PackageMerge")
uml2CD_MultiplicityElement = Class(name="uml2CD::MultiplicityElement", is_abstract=True)
uml2CD_ValueSpecification = Class(name="uml2CD::ValueSpecification")
TypedElement = Class(name="TypedElement")
uml2CD_Parameter = Class(name="uml2CD::Parameter")
uml2CD_Property = Class(name="uml2CD::Property")
uml2CD_TypedElement = Class(name="uml2CD::TypedElement", is_abstract=True)
uml2CD_Typpee = Class(name="uml2CD::Typpee")
uml2CD_Generalization = Class(name="uml2CD::Generalization")
uml2CD_Classifier = Class(name="uml2CD::Classifier", is_abstract=True)
uml2CD_GeneralizationSet = Class(name="uml2CD::GeneralizationSet")
Typpee = Class(name="Typpee")
uml2CD_Feature = Class(name="uml2CD::Feature", is_abstract=True)
uml2CD_Class = Class(name="uml2CD::Class")
uml2CD_Substitution = Class(name="uml2CD::Substitution")
uml2CD_StructuralFeature = Class(name="uml2CD::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
uml2CD_BehavioralFeature = Class(name="uml2CD::BehavioralFeature", is_abstract=True)
uml2CD_Operation = Class(name="uml2CD::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
Classifier = Class(name="Classifier")
uml2CD_DataType = Class(name="uml2CD::DataType")
StructuralFeature = Class(name="StructuralFeature")
uml2CD_PrimitiveType = Class(name="uml2CD::PrimitiveType")
DataType = Class(name="DataType")
uml2CD_Enumeration = Class(name="uml2CD::Enumeration")
uml2CD_EnumerationLiteral = Class(name="uml2CD::EnumerationLiteral")
ValueSpecification = Class(name="ValueSpecification")
uml2CD_Association = Class(name="uml2CD::Association")
uml2CD_Abstraction = Class(name="uml2CD::Abstraction")
Dependency = Class(name="Dependency")
uml2CD_Usage = Class(name="uml2CD::Usage")
uml2CD_Realization = Class(name="uml2CD::Realization")
Abstraction = Class(name="Abstraction")
Realization = Class(name="Realization")
uml2CD_Interface = Class(name="uml2CD::Interface")
uml2CD_InterfaceRealization = Class(name="uml2CD::InterfaceRealization")
uml2CD_AssociationClass = Class(name="uml2CD::AssociationClass")
Association = Class(name="Association")
Class_ = Class(name="Class")
uml2CD_RedefinableElement = Class(name="uml2CD::RedefinableElement", is_abstract=True)

# uml2CD_Element class attributes and methods

# uml2CD_Relationship class attributes and methods

# Element class attributes and methods

# uml2CD_DirectRelationship class attributes and methods

# Relationship class attributes and methods

# uml2CD_NamedElement class attributes and methods
uml2CD_NamedElement_name: Property = Property(name="name", type=StringType)
uml2CD_NamedElement.attributes={uml2CD_NamedElement_name}

# uml2CD_Namespace class attributes and methods

# uml2CD_Dependency class attributes and methods

# uml2CD_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# uml2CD_Comment class attributes and methods

# uml2CD_Package class attributes and methods

# uml2CD_PackageImport class attributes and methods
uml2CD_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
uml2CD_PackageImport.attributes={uml2CD_PackageImport_visibility}

# uml2CD_ElementImport class attributes and methods
uml2CD_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
uml2CD_ElementImport.attributes={uml2CD_ElementImport_visibility}

# uml2CD_Constraint class attributes and methods

# DirectRelationship class attributes and methods

# PackageableElement class attributes and methods

# Namespace class attributes and methods

# uml2CD_PackageMerge class attributes and methods

# uml2CD_MultiplicityElement class attributes and methods

# uml2CD_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# uml2CD_Parameter class attributes and methods
uml2CD_Parameter_direction: Property = Property(name="direction", type=StringType)
uml2CD_Parameter.attributes={uml2CD_Parameter_direction}

# uml2CD_Property class attributes and methods

# uml2CD_TypedElement class attributes and methods

# uml2CD_Typpee class attributes and methods

# uml2CD_Generalization class attributes and methods
uml2CD_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
uml2CD_Generalization.attributes={uml2CD_Generalization_isSubstitutable}

# uml2CD_Classifier class attributes and methods
uml2CD_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
uml2CD_Classifier.attributes={uml2CD_Classifier_isAbstract}

# uml2CD_GeneralizationSet class attributes and methods
uml2CD_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
uml2CD_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
uml2CD_GeneralizationSet.attributes={uml2CD_GeneralizationSet_isCovering, uml2CD_GeneralizationSet_isDisjoint}

# Typpee class attributes and methods

# uml2CD_Feature class attributes and methods

# uml2CD_Class class attributes and methods

# uml2CD_Substitution class attributes and methods

# uml2CD_StructuralFeature class attributes and methods

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# uml2CD_BehavioralFeature class attributes and methods

# uml2CD_Operation class attributes and methods
uml2CD_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
uml2CD_Operation.attributes={uml2CD_Operation_isQuery}

# BehavioralFeature class attributes and methods

# Classifier class attributes and methods

# uml2CD_DataType class attributes and methods

# StructuralFeature class attributes and methods

# uml2CD_PrimitiveType class attributes and methods

# DataType class attributes and methods

# uml2CD_Enumeration class attributes and methods

# uml2CD_EnumerationLiteral class attributes and methods

# ValueSpecification class attributes and methods

# uml2CD_Association class attributes and methods
uml2CD_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
uml2CD_Association.attributes={uml2CD_Association_isDerived}

# uml2CD_Abstraction class attributes and methods

# Dependency class attributes and methods

# uml2CD_Usage class attributes and methods

# uml2CD_Realization class attributes and methods

# Abstraction class attributes and methods

# Realization class attributes and methods

# uml2CD_Interface class attributes and methods

# uml2CD_InterfaceRealization class attributes and methods

# uml2CD_AssociationClass class attributes and methods

# Association class attributes and methods

# Class class attributes and methods

# uml2CD_RedefinableElement class attributes and methods
uml2CD_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
uml2CD_RedefinableElement.attributes={uml2CD_RedefinableElement_isLeaf}

# Relationships
ownedComment0: BinaryAssociation = BinaryAssociation(
    name="ownedComment0",
    ends={
        Property(name="owningElement", type=uml2CD_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Comment", type=uml2CD_Element, multiplicity=Multiplicity(1, 1))
    }
)
owner2: BinaryAssociation = BinaryAssociation(
    name="owner2",
    ends={
        Property(name="Element", type=uml2CD_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=uml2CD_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement4: BinaryAssociation = BinaryAssociation(
    name="ownedElement4",
    ends={
        Property(name="Element5", type=uml2CD_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml2CD_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningElement6: BinaryAssociation = BinaryAssociation(
    name="owningElement6",
    ends={
        Property(name="Element7", type=uml2CD_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedComment", type=uml2CD_Element, multiplicity=Multiplicity(0, 1))
    }
)
relatedElement8: BinaryAssociation = BinaryAssociation(
    name="relatedElement8",
    ends={
        Property(name="uml2CD_Element", type=uml2CD_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Relationship", type=uml2CD_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="uml2CD_Element10", type=uml2CD_DirectRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_DirectRelationship", type=uml2CD_Element, multiplicity=Multiplicity(1, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="uml2CD_Element13", type=uml2CD_DirectRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_DirectRelationship12", type=uml2CD_Element, multiplicity=Multiplicity(1, 9999))
    }
)
namespace14: BinaryAssociation = BinaryAssociation(
    name="namespace14",
    ends={
        Property(name="uml2CD_Namespace", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_NamedElement", type=uml2CD_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
supplierDependency15: BinaryAssociation = BinaryAssociation(
    name="supplierDependency15",
    ends={
        Property(name="Dependency", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="supplier", type=uml2CD_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
clientDependency16: BinaryAssociation = BinaryAssociation(
    name="clientDependency16",
    ends={
        Property(name="Dependency17", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=uml2CD_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
owningPackage18: BinaryAssociation = BinaryAssociation(
    name="owningPackage18",
    ends={
        Property(name="Package", type=uml2CD_PackageableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="packagedElement", type=uml2CD_Package, multiplicity=Multiplicity(0, 1))
    }
)
importedMember19: BinaryAssociation = BinaryAssociation(
    name="importedMember19",
    ends={
        Property(name="uml2CD_PackageableElement", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Namespace20", type=uml2CD_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
packageImport21: BinaryAssociation = BinaryAssociation(
    name="packageImport21",
    ends={
        Property(name="PackageImport", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=uml2CD_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport22: BinaryAssociation = BinaryAssociation(
    name="elementImport22",
    ends={
        Property(name="ElementImport", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace23", type=uml2CD_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule24: BinaryAssociation = BinaryAssociation(
    name="ownedRule24",
    ends={
        Property(name="Constraint", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=uml2CD_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement25: BinaryAssociation = BinaryAssociation(
    name="importedElement25",
    ends={
        Property(name="uml2CD_PackageableElement26", type=uml2CD_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_ElementImport", type=uml2CD_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace27: BinaryAssociation = BinaryAssociation(
    name="importingNamespace27",
    ends={
        Property(name="Namespace", type=uml2CD_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage28: BinaryAssociation = BinaryAssociation(
    name="importedPackage28",
    ends={
        Property(name="uml2CD_Package", type=uml2CD_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_PackageImport", type=uml2CD_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace29: BinaryAssociation = BinaryAssociation(
    name="importingNamespace29",
    ends={
        Property(name="Namespace30", type=uml2CD_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=uml2CD_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestingPackage32: BinaryAssociation = BinaryAssociation(
    name="nestingPackage32",
    ends={
        Property(name="Package33", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=uml2CD_Package, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage35: BinaryAssociation = BinaryAssociation(
    name="nestedPackage35",
    ends={
        Property(name="Package36", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=uml2CD_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge38: BinaryAssociation = BinaryAssociation(
    name="packageMerge38",
    ends={
        Property(name="PackageMerge", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=uml2CD_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lowerValue39: BinaryAssociation = BinaryAssociation(
    name="lowerValue39",
    ends={
        Property(name="ValueSpecification", type=uml2CD_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLower", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperValue40: BinaryAssociation = BinaryAssociation(
    name="upperValue40",
    ends={
        Property(name="ValueSpecification41", type=uml2CD_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningUpper", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningLower42: BinaryAssociation = BinaryAssociation(
    name="owningLower42",
    ends={
        Property(name="MultiplicityElement", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="lowerValue", type=uml2CD_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningUpper43: BinaryAssociation = BinaryAssociation(
    name="owningUpper43",
    ends={
        Property(name="MultiplicityElement44", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="upperValue", type=uml2CD_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningConstraint45: BinaryAssociation = BinaryAssociation(
    name="owningConstraint45",
    ends={
        Property(name="Constraint46", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=uml2CD_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
owningParameter47: BinaryAssociation = BinaryAssociation(
    name="owningParameter47",
    ends={
        Property(name="Parameter", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultValue", type=uml2CD_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
owningProperty48: BinaryAssociation = BinaryAssociation(
    name="owningProperty48",
    ends={
        Property(name="Property", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="defaultValue49", type=uml2CD_Property, multiplicity=Multiplicity(0, 1))
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="uml2CD_Typpee", type=uml2CD_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_TypedElement", type=uml2CD_Typpee, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement51: BinaryAssociation = BinaryAssociation(
    name="constrainedElement51",
    ends={
        Property(name="uml2CD_Element52", type=uml2CD_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Constraint", type=uml2CD_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification53: BinaryAssociation = BinaryAssociation(
    name="specification53",
    ends={
        Property(name="ValueSpecification54", type=uml2CD_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="owningConstraint", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context55: BinaryAssociation = BinaryAssociation(
    name="context55",
    ends={
        Property(name="Namespace56", type=uml2CD_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=uml2CD_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement37: BinaryAssociation = BinaryAssociation(
    name="packagedElement37",
    ends={
        Property(name="PackageableElement", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPackage", type=uml2CD_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general57: BinaryAssociation = BinaryAssociation(
    name="general57",
    ends={
        Property(name="uml2CD_Classifier", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Generalization", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific58: BinaryAssociation = BinaryAssociation(
    name="specific58",
    ends={
        Property(name="Classifier", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet59: BinaryAssociation = BinaryAssociation(
    name="generalizationSet59",
    ends={
        Property(name="GeneralizationSet", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization60", type=uml2CD_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
generalization61: BinaryAssociation = BinaryAssociation(
    name="generalization61",
    ends={
        Property(name="Generalization", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=uml2CD_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature62: BinaryAssociation = BinaryAssociation(
    name="feature62",
    ends={
        Property(name="Feature", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=uml2CD_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
Class63: BinaryAssociation = BinaryAssociation(
    name="Class63",
    ends={
        Property(name="Class", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedClassifier", type=uml2CD_Class, multiplicity=Multiplicity(0, 1))
    }
)
powertypeExtent64: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent64",
    ends={
        Property(name="GeneralizationSet65", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=uml2CD_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
substitution66: BinaryAssociation = BinaryAssociation(
    name="substitution66",
    ends={
        Property(name="Substitution", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=uml2CD_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featuringClassifier67: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier67",
    ends={
        Property(name="Classifier68", type=uml2CD_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=uml2CD_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter69: BinaryAssociation = BinaryAssociation(
    name="ownedParameter69",
    ends={
        Property(name="Parameter70", type=uml2CD_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerFormalParam", type=uml2CD_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerFormalParam73: BinaryAssociation = BinaryAssociation(
    name="ownerFormalParam73",
    ends={
        Property(name="BehavioralFeature", type=uml2CD_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=uml2CD_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue74: BinaryAssociation = BinaryAssociation(
    name="defaultValue74",
    ends={
        Property(name="ValueSpecification75", type=uml2CD_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningParameter", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedOperation77: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation77",
    ends={
        Property(name="uml2CD_Operation", type=uml2CD_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Operation76", type=uml2CD_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
Class78: BinaryAssociation = BinaryAssociation(
    name="Class78",
    ends={
        Property(name="Class79", type=uml2CD_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=uml2CD_Class, multiplicity=Multiplicity(0, 1))
    }
)
superClass81: BinaryAssociation = BinaryAssociation(
    name="superClass81",
    ends={
        Property(name="uml2CD_Class", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Class80", type=uml2CD_Class, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier82: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier82",
    ends={
        Property(name="Classifier84", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class83", type=uml2CD_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation85: BinaryAssociation = BinaryAssociation(
    name="ownedOperation85",
    ends={
        Property(name="Operation", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class86", type=uml2CD_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute87: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute87",
    ends={
        Property(name="Property89", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class88", type=uml2CD_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue90: BinaryAssociation = BinaryAssociation(
    name="defaultValue90",
    ends={
        Property(name="ValueSpecification91", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="owningProperty", type=uml2CD_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Class92: BinaryAssociation = BinaryAssociation(
    name="Class92",
    ends={
        Property(name="Class93", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=uml2CD_Class, multiplicity=Multiplicity(0, 1))
    }
)
raisedException71: BinaryAssociation = BinaryAssociation(
    name="raisedException71",
    ends={
        Property(name="uml2CD_Typpee72", type=uml2CD_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_BehavioralFeature", type=uml2CD_Typpee, multiplicity=Multiplicity(0, 9999))
    }
)
association94: BinaryAssociation = BinaryAssociation(
    name="association94",
    ends={
        Property(name="Association", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=uml2CD_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation95: BinaryAssociation = BinaryAssociation(
    name="owningAssociation95",
    ends={
        Property(name="Association96", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=uml2CD_Association, multiplicity=Multiplicity(0, 1))
    }
)
qualifier98: BinaryAssociation = BinaryAssociation(
    name="qualifier98",
    ends={
        Property(name="Property99", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=uml2CD_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd101: BinaryAssociation = BinaryAssociation(
    name="associationEnd101",
    ends={
        Property(name="Property102", type=uml2CD_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=uml2CD_Property, multiplicity=Multiplicity(0, 1))
    }
)
memberEnd103: BinaryAssociation = BinaryAssociation(
    name="memberEnd103",
    ends={
        Property(name="Property104", type=uml2CD_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=uml2CD_Property, multiplicity=Multiplicity(1, 9999))
    }
)
ownedEnd105: BinaryAssociation = BinaryAssociation(
    name="ownedEnd105",
    ends={
        Property(name="Property106", type=uml2CD_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=uml2CD_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral107: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral107",
    ends={
        Property(name="EnumerationLiteral", type=uml2CD_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=uml2CD_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration108: BinaryAssociation = BinaryAssociation(
    name="enumeration108",
    ends={
        Property(name="Enumeration", type=uml2CD_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=uml2CD_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
receivingPackage109: BinaryAssociation = BinaryAssociation(
    name="receivingPackage109",
    ends={
        Property(name="Package110", type=uml2CD_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=uml2CD_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage111: BinaryAssociation = BinaryAssociation(
    name="mergedPackage111",
    ends={
        Property(name="uml2CD_Package112", type=uml2CD_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_PackageMerge", type=uml2CD_Package, multiplicity=Multiplicity(1, 1))
    }
)
supplier113: BinaryAssociation = BinaryAssociation(
    name="supplier113",
    ends={
        Property(name="NamedElement", type=uml2CD_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="supplierDependency", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client114: BinaryAssociation = BinaryAssociation(
    name="client114",
    ends={
        Property(name="NamedElement115", type=uml2CD_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
contract116: BinaryAssociation = BinaryAssociation(
    name="contract116",
    ends={
        Property(name="uml2CD_Classifier117", type=uml2CD_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Substitution", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier118: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier118",
    ends={
        Property(name="Classifier119", type=uml2CD_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=uml2CD_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
redefinedInterface121: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface121",
    ends={
        Property(name="uml2CD_Interface", type=uml2CD_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Interface120", type=uml2CD_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
contract122: BinaryAssociation = BinaryAssociation(
    name="contract122",
    ends={
        Property(name="uml2CD_Interface123", type=uml2CD_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_InterfaceRealization", type=uml2CD_Interface, multiplicity=Multiplicity(1, 1))
    }
)
generalization124: BinaryAssociation = BinaryAssociation(
    name="generalization124",
    ends={
        Property(name="Generalization125", type=uml2CD_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=uml2CD_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
powertype126: BinaryAssociation = BinaryAssociation(
    name="powertype126",
    ends={
        Property(name="Classifier127", type=uml2CD_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=uml2CD_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement129: BinaryAssociation = BinaryAssociation(
    name="redefinedElement129",
    ends={
        Property(name="uml2CD_RedefinableElement", type=uml2CD_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_RedefinableElement128", type=uml2CD_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_uml2CD_Relationship_Element = Generalization(general=Element, specific=uml2CD_Relationship)
gen_uml2CD_DirectRelationship_Relationship = Generalization(general=Relationship, specific=uml2CD_DirectRelationship)
gen_uml2CD_NamedElement_Element = Generalization(general=Element, specific=uml2CD_NamedElement)
gen_uml2CD_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml2CD_PackageableElement)
gen_uml2CD_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Namespace)
gen_uml2CD_ElementImport_DirectRelationship = Generalization(general=DirectRelationship, specific=uml2CD_ElementImport)
gen_uml2CD_PackageImport_DirectRelationship = Generalization(general=DirectRelationship, specific=uml2CD_PackageImport)
gen_uml2CD_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml2CD_Package)
gen_uml2CD_Package_Namespace = Generalization(general=Namespace, specific=uml2CD_Package)
gen_uml2CD_MultiplicityElement_Element = Generalization(general=Element, specific=uml2CD_MultiplicityElement)
gen_uml2CD_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=uml2CD_ValueSpecification)
gen_uml2CD_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml2CD_ValueSpecification)
gen_uml2CD_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml2CD_TypedElement)
gen_uml2CD_Typpee_PackageableElement = Generalization(general=PackageableElement, specific=uml2CD_Typpee)
gen_uml2CD_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=uml2CD_Constraint)
gen_uml2CD_Generalization_DirectRelationship = Generalization(general=DirectRelationship, specific=uml2CD_Generalization)
gen_uml2CD_Classifier_Typpee = Generalization(general=Typpee, specific=uml2CD_Classifier)
gen_uml2CD_Classifier_Namespace = Generalization(general=Namespace, specific=uml2CD_Classifier)
gen_uml2CD_StructuralFeature_Feature = Generalization(general=Feature, specific=uml2CD_StructuralFeature)
gen_uml2CD_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=uml2CD_StructuralFeature)
gen_uml2CD_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml2CD_StructuralFeature)
gen_uml2CD_BehavioralFeature_Feature = Generalization(general=Feature, specific=uml2CD_BehavioralFeature)
gen_uml2CD_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=uml2CD_BehavioralFeature)
gen_uml2CD_Parameter_TypedElement = Generalization(general=TypedElement, specific=uml2CD_Parameter)
gen_uml2CD_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml2CD_Parameter)
gen_uml2CD_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml2CD_Operation)
gen_uml2CD_Class_Classifier = Generalization(general=Classifier, specific=uml2CD_Class)
gen_uml2CD_DataType_Classifier = Generalization(general=Classifier, specific=uml2CD_DataType)
gen_uml2CD_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=uml2CD_Property)
gen_uml2CD_Association_Classifier = Generalization(general=Classifier, specific=uml2CD_Association)
gen_uml2CD_Association_Relationship = Generalization(general=Relationship, specific=uml2CD_Association)
gen_uml2CD_PrimitiveType_DataType = Generalization(general=DataType, specific=uml2CD_PrimitiveType)
gen_uml2CD_Enumeration_DataType = Generalization(general=DataType, specific=uml2CD_Enumeration)
gen_uml2CD_EnumerationLiteral_ValueSpecification = Generalization(general=ValueSpecification, specific=uml2CD_EnumerationLiteral)
gen_uml2CD_PackageMerge_DirectRelationship = Generalization(general=DirectRelationship, specific=uml2CD_PackageMerge)
gen_uml2CD_Dependency_DirectRelationship = Generalization(general=DirectRelationship, specific=uml2CD_Dependency)
gen_uml2CD_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml2CD_Dependency)
gen_uml2CD_Abstraction_Dependency = Generalization(general=Dependency, specific=uml2CD_Abstraction)
gen_uml2CD_Usage_Dependency = Generalization(general=Dependency, specific=uml2CD_Usage)
gen_uml2CD_Realization_Abstraction = Generalization(general=Abstraction, specific=uml2CD_Realization)
gen_uml2CD_Substitution_Realization = Generalization(general=Realization, specific=uml2CD_Substitution)
gen_uml2CD_Interface_Classifier = Generalization(general=Classifier, specific=uml2CD_Interface)
gen_uml2CD_InterfaceRealization_Realization = Generalization(general=Realization, specific=uml2CD_InterfaceRealization)
gen_uml2CD_AssociationClass_Association = Generalization(general=Association, specific=uml2CD_AssociationClass)
gen_uml2CD_AssociationClass_Class = Generalization(general=Class_, specific=uml2CD_AssociationClass)
gen_uml2CD_RedefinableElement_Element = Generalization(general=Element, specific=uml2CD_RedefinableElement)

# Domain Model
domain_model = DomainModel(
    name="uml2CD",
    types={uml2CD_Element, uml2CD_Relationship, Element, uml2CD_DirectRelationship, Relationship, uml2CD_NamedElement, uml2CD_Namespace, uml2CD_Dependency, uml2CD_PackageableElement, NamedElement, uml2CD_Comment, uml2CD_Package, uml2CD_PackageImport, uml2CD_ElementImport, uml2CD_Constraint, DirectRelationship, PackageableElement, Namespace, uml2CD_PackageMerge, uml2CD_MultiplicityElement, uml2CD_ValueSpecification, TypedElement, uml2CD_Parameter, uml2CD_Property, uml2CD_TypedElement, uml2CD_Typpee, uml2CD_Generalization, uml2CD_Classifier, uml2CD_GeneralizationSet, Typpee, uml2CD_Feature, uml2CD_Class, uml2CD_Substitution, uml2CD_StructuralFeature, Feature, MultiplicityElement, uml2CD_BehavioralFeature, uml2CD_Operation, BehavioralFeature, Classifier, uml2CD_DataType, StructuralFeature, uml2CD_PrimitiveType, DataType, uml2CD_Enumeration, uml2CD_EnumerationLiteral, ValueSpecification, uml2CD_Association, uml2CD_Abstraction, Dependency, uml2CD_Usage, uml2CD_Realization, Abstraction, Realization, uml2CD_Interface, uml2CD_InterfaceRealization, uml2CD_AssociationClass, Association, Class_, uml2CD_RedefinableElement, VisibilityKind, ParameterDirectionKind, AggregationKind},
    associations={ownedComment0, owner2, ownedElement4, owningElement6, relatedElement8, target9, source11, namespace14, supplierDependency15, clientDependency16, owningPackage18, importedMember19, packageImport21, elementImport22, ownedRule24, importedElement25, importingNamespace27, importedPackage28, importingNamespace29, nestingPackage32, nestedPackage35, packageMerge38, lowerValue39, upperValue40, owningLower42, owningUpper43, owningConstraint45, owningParameter47, owningProperty48, type50, constrainedElement51, specification53, context55, packagedElement37, general57, specific58, generalizationSet59, generalization61, feature62, Class63, powertypeExtent64, substitution66, featuringClassifier67, ownedParameter69, ownerFormalParam73, defaultValue74, redefinedOperation77, Class78, superClass81, nestedClassifier82, ownedOperation85, ownedAttribute87, defaultValue90, Class92, raisedException71, association94, owningAssociation95, qualifier98, associationEnd101, memberEnd103, ownedEnd105, ownedLiteral107, enumeration108, receivingPackage109, mergedPackage111, supplier113, client114, contract116, substitutingClassifier118, redefinedInterface121, contract122, generalization124, powertype126, redefinedElement129},
    generalizations={gen_uml2CD_Relationship_Element, gen_uml2CD_DirectRelationship_Relationship, gen_uml2CD_NamedElement_Element, gen_uml2CD_PackageableElement_NamedElement, gen_uml2CD_Namespace_NamedElement, gen_uml2CD_ElementImport_DirectRelationship, gen_uml2CD_PackageImport_DirectRelationship, gen_uml2CD_Package_PackageableElement, gen_uml2CD_Package_Namespace, gen_uml2CD_MultiplicityElement_Element, gen_uml2CD_ValueSpecification_TypedElement, gen_uml2CD_ValueSpecification_PackageableElement, gen_uml2CD_TypedElement_NamedElement, gen_uml2CD_Typpee_PackageableElement, gen_uml2CD_Constraint_PackageableElement, gen_uml2CD_Generalization_DirectRelationship, gen_uml2CD_Classifier_Typpee, gen_uml2CD_Classifier_Namespace, gen_uml2CD_StructuralFeature_Feature, gen_uml2CD_StructuralFeature_TypedElement, gen_uml2CD_StructuralFeature_MultiplicityElement, gen_uml2CD_BehavioralFeature_Feature, gen_uml2CD_BehavioralFeature_Namespace, gen_uml2CD_Parameter_TypedElement, gen_uml2CD_Parameter_MultiplicityElement, gen_uml2CD_Operation_BehavioralFeature, gen_uml2CD_Class_Classifier, gen_uml2CD_DataType_Classifier, gen_uml2CD_Property_StructuralFeature, gen_uml2CD_Association_Classifier, gen_uml2CD_Association_Relationship, gen_uml2CD_PrimitiveType_DataType, gen_uml2CD_Enumeration_DataType, gen_uml2CD_EnumerationLiteral_ValueSpecification, gen_uml2CD_PackageMerge_DirectRelationship, gen_uml2CD_Dependency_DirectRelationship, gen_uml2CD_Dependency_PackageableElement, gen_uml2CD_Abstraction_Dependency, gen_uml2CD_Usage_Dependency, gen_uml2CD_Realization_Abstraction, gen_uml2CD_Substitution_Realization, gen_uml2CD_Interface_Classifier, gen_uml2CD_InterfaceRealization_Realization, gen_uml2CD_AssociationClass_Association, gen_uml2CD_AssociationClass_Class, gen_uml2CD_RedefinableElement_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)