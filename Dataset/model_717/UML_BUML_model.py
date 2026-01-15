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

# Classes
uml_Comment = Class(name="uml::Comment")
Element = Class(name="Element")
uml_Element = Class(name="uml::Element", is_abstract=True)
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
uml_Package = Class(name="uml::Package")
PackageableElement = Class(name="PackageableElement")
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
uml_Dependency = Class(name="uml::Dependency")
uml_Namespace = Class(name="uml::Namespace", is_abstract=True)
DirectedRelationship = Class(name="DirectedRelationship")
uml_DirectedRelationship = Class(name="uml::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
uml_Relationship = Class(name="uml::Relationship", is_abstract=True)
NamedElement = Class(name="NamedElement")
uml_ElementImport = Class(name="uml::ElementImport")
uml_PackageImport = Class(name="uml::PackageImport")
uml_ValueSpecification = Class(name="uml::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)
uml_Association = Class(name="uml::Association")
Classifier = Class(name="Classifier")
uml_Property = Class(name="uml::Property")
uml_Substitution = Class(name="uml::Substitution")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
Type = Class(name="Type")
uml_Feature = Class(name="uml::Feature", is_abstract=True)
Realization = Class(name="Realization")
uml_Realization = Class(name="uml::Realization")
Abstraction = Class(name="Abstraction")
uml_Abstraction = Class(name="uml::Abstraction")
Dependency = Class(name="Dependency")
uml_Parameter = Class(name="uml::Parameter")
uml_Operation = Class(name="uml::Operation")
uml_Class = Class(name="uml::Class")
BehavioralFeature = Class(name="BehavioralFeature")
uml_BehavioralFeature = Class(name="uml::BehavioralFeature", is_abstract=True)
Namespace = Class(name="Namespace")
Feature = Class(name="Feature")
uml_Generalization = Class(name="uml::Generalization")
uml_Model = Class(name="uml::Model")

# uml_Comment class attributes and methods
uml_Comment_body: Property = Property(name="body", type=StringType)
uml_Comment.attributes={uml_Comment_body}

# Element class attributes and methods

# uml_Element class attributes and methods

# uml_PackageableElement class attributes and methods

# uml_Package class attributes and methods
uml_Package_name: Property = Property(name="name", type=StringType)
uml_Package.attributes={uml_Package_name}

# PackageableElement class attributes and methods

# uml_Type class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_visibility, uml_NamedElement_qualifiedName, uml_NamedElement_name}

# uml_Dependency class attributes and methods

# uml_Namespace class attributes and methods

# DirectedRelationship class attributes and methods

# uml_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# uml_Relationship class attributes and methods

# NamedElement class attributes and methods

# uml_ElementImport class attributes and methods
uml_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
uml_ElementImport_alias: Property = Property(name="alias", type=StringType)
uml_ElementImport.attributes={uml_ElementImport_visibility, uml_ElementImport_alias}

# uml_PackageImport class attributes and methods
uml_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
uml_PackageImport.attributes={uml_PackageImport_visibility}

# uml_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# uml_TypedElement class attributes and methods

# uml_Association class attributes and methods
uml_Association_isDerived: Property = Property(name="isDerived", type=StringType)
uml_Association.attributes={uml_Association_isDerived}

# Classifier class attributes and methods

# uml_Property class attributes and methods
uml_Property_name: Property = Property(name="name", type=StringType)
uml_Property.attributes={uml_Property_name}

# uml_Substitution class attributes and methods

# uml_Classifier class attributes and methods
uml_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Classifier.attributes={uml_Classifier_isAbstract}

# Type class attributes and methods

# uml_Feature class attributes and methods
uml_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
uml_Feature.attributes={uml_Feature_isStatic}

# Realization class attributes and methods

# uml_Realization class attributes and methods

# Abstraction class attributes and methods

# uml_Abstraction class attributes and methods

# Dependency class attributes and methods

# uml_Parameter class attributes and methods
uml_Parameter_default: Property = Property(name="default", type=StringType)
uml_Parameter_isException: Property = Property(name="isException", type=StringType)
uml_Parameter_isStream: Property = Property(name="isStream", type=StringType)
uml_Parameter.attributes={uml_Parameter_isStream, uml_Parameter_default, uml_Parameter_isException}

# uml_Operation class attributes and methods
uml_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
uml_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
uml_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
uml_Operation_lower: Property = Property(name="lower", type=StringType)
uml_Operation_upper: Property = Property(name="upper", type=StringType)
uml_Operation.attributes={uml_Operation_isUnique, uml_Operation_isOrdered, uml_Operation_isQuery, uml_Operation_lower, uml_Operation_upper}

# uml_Class class attributes and methods
uml_Class_name: Property = Property(name="name", type=StringType)
uml_Class_isActive: Property = Property(name="isActive", type=StringType)
uml_Class.attributes={uml_Class_name, uml_Class_isActive}

# BehavioralFeature class attributes and methods

# uml_BehavioralFeature class attributes and methods
uml_BehavioralFeature_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_BehavioralFeature.attributes={uml_BehavioralFeature_isAbstract}

# Namespace class attributes and methods

# Feature class attributes and methods

# uml_Generalization class attributes and methods
uml_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
uml_Generalization.attributes={uml_Generalization_isSubstitutable}

# uml_Model class attributes and methods
uml_Model_name: Property = Property(name="name", type=StringType)
uml_Model.attributes={uml_Model_name}

# Relationships
annotatedElement0: BinaryAssociation = BinaryAssociation(
    name="annotatedElement0",
    ends={
        Property(name="uml_Element", type=uml_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Comment", type=uml_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=uml_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="uml_Comment8", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Element7", type=uml_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType9: BinaryAssociation = BinaryAssociation(
    name="ownedType9",
    ends={
        Property(name="Type", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=uml_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement10: BinaryAssociation = BinaryAssociation(
    name="packagedElement10",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace12: BinaryAssociation = BinaryAssociation(
    name="namespace12",
    ends={
        Property(name="ownedMember", type=uml_Namespace, multiplicity=Multiplicity(0, 1)),
        Property(name="Namespace", type=uml_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
clientDependency11: BinaryAssociation = BinaryAssociation(
    name="clientDependency11",
    ends={
        Property(name="Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=uml_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
supplier13: BinaryAssociation = BinaryAssociation(
    name="supplier13",
    ends={
        Property(name="uml_NamedElement", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client14: BinaryAssociation = BinaryAssociation(
    name="client14",
    ends={
        Property(name="NamedElement", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="uml_Element16", type=uml_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DirectedRelationship", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="uml_Element19", type=uml_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_DirectedRelationship18", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement20: BinaryAssociation = BinaryAssociation(
    name="relatedElement20",
    ends={
        Property(name="uml_Element21", type=uml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Relationship", type=uml_Element, multiplicity=Multiplicity(1, 9999))
    }
)
elementImport22: BinaryAssociation = BinaryAssociation(
    name="elementImport22",
    ends={
        Property(name="ElementImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=uml_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport23: BinaryAssociation = BinaryAssociation(
    name="packageImport23",
    ends={
        Property(name="PackageImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace24", type=uml_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member25: BinaryAssociation = BinaryAssociation(
    name="member25",
    ends={
        Property(name="uml_NamedElement26", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Namespace", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember27: BinaryAssociation = BinaryAssociation(
    name="importedMember27",
    ends={
        Property(name="uml_PackageableElement29", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Namespace28", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember30: BinaryAssociation = BinaryAssociation(
    name="ownedMember30",
    ends={
        Property(name="NamedElement31", type=uml_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importingNamespace38: BinaryAssociation = BinaryAssociation(
    name="importingNamespace38",
    ends={
        Property(name="Namespace39", type=uml_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedElement32: BinaryAssociation = BinaryAssociation(
    name="importedElement32",
    ends={
        Property(name="uml_PackageableElement33", type=uml_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_ElementImport", type=uml_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace34: BinaryAssociation = BinaryAssociation(
    name="importingNamespace34",
    ends={
        Property(name="Namespace35", type=uml_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=uml_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage36: BinaryAssociation = BinaryAssociation(
    name="importedPackage36",
    ends={
        Property(name="uml_Package37", type=uml_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_PackageImport", type=uml_Package, multiplicity=Multiplicity(1, 1))
    }
)
endType46: BinaryAssociation = BinaryAssociation(
    name="endType46",
    ends={
        Property(name="uml_Association47", type=uml_Type, multiplicity=Multiplicity(1, 9999)),
        Property(name="uml_Type48", type=uml_Association, multiplicity=Multiplicity(1, 1))
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
package41: BinaryAssociation = BinaryAssociation(
    name="package41",
    ends={
        Property(name="Package", type=uml_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=uml_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd42: BinaryAssociation = BinaryAssociation(
    name="ownedEnd42",
    ends={
        Property(name="uml_Property", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd43: BinaryAssociation = BinaryAssociation(
    name="memberEnd43",
    ends={
        Property(name="uml_Property45", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association44", type=uml_Property, multiplicity=Multiplicity(2, 9999))
    }
)
substitution61: BinaryAssociation = BinaryAssociation(
    name="substitution61",
    ends={
        Property(name="Substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=uml_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navigableOwnedEnd49: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd49",
    ends={
        Property(name="uml_Property51", type=uml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Association50", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
feature52: BinaryAssociation = BinaryAssociation(
    name="feature52",
    ends={
        Property(name="Feature", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=uml_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember53: BinaryAssociation = BinaryAssociation(
    name="inheritedMember53",
    ends={
        Property(name="uml_NamedElement54", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier", type=uml_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier56: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier56",
    ends={
        Property(name="uml_Classifier57", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier55", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general59: BinaryAssociation = BinaryAssociation(
    name="general59",
    ends={
        Property(name="uml_Classifier60", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier58", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue71: BinaryAssociation = BinaryAssociation(
    name="defaultValue71",
    ends={
        Property(name="uml_ValueSpecification", type=uml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Parameter72", type=uml_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute62: BinaryAssociation = BinaryAssociation(
    name="attribute62",
    ends={
        Property(name="uml_Property64", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Classifier63", type=uml_Property, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier65: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier65",
    ends={
        Property(name="Classifier", type=uml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
contract66: BinaryAssociation = BinaryAssociation(
    name="contract66",
    ends={
        Property(name="uml_Classifier67", type=uml_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier68: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier68",
    ends={
        Property(name="Classifier69", type=uml_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operation70: BinaryAssociation = BinaryAssociation(
    name="operation70",
    ends={
        Property(name="uml_Operation", type=uml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Parameter", type=uml_Operation, multiplicity=Multiplicity(0, 1))
    }
)
raisedException81: BinaryAssociation = BinaryAssociation(
    name="raisedException81",
    ends={
        Property(name="uml_Type83", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature82", type=uml_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type73: BinaryAssociation = BinaryAssociation(
    name="type73",
    ends={
        Property(name="uml_Class", type=uml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Property74", type=uml_Class, multiplicity=Multiplicity(1, 1))
    }
)
class75: BinaryAssociation = BinaryAssociation(
    name="class75",
    ends={
        Property(name="Class", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=uml_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation77: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation77",
    ends={
        Property(name="uml_Operation78", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation76", type=uml_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter79: BinaryAssociation = BinaryAssociation(
    name="ownedParameter79",
    ends={
        Property(name="uml_Parameter80", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization94: BinaryAssociation = BinaryAssociation(
    name="generalization94",
    ends={
        Property(name="uml_Generalization", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class95", type=uml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier84: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier84",
    ends={
        Property(name="uml_Classifier86", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class85", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation87: BinaryAssociation = BinaryAssociation(
    name="ownedOperation87",
    ends={
        Property(name="Operation", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass89: BinaryAssociation = BinaryAssociation(
    name="superClass89",
    ends={
        Property(name="uml_Class90", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class88", type=uml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute91: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute91",
    ends={
        Property(name="uml_Property93", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class92", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general96: BinaryAssociation = BinaryAssociation(
    name="general96",
    ends={
        Property(name="uml_Classifier98", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Generalization97", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific99: BinaryAssociation = BinaryAssociation(
    name="specific99",
    ends={
        Property(name="uml_Classifier101", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Generalization100", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement102: BinaryAssociation = BinaryAssociation(
    name="packagedElement102",
    ends={
        Property(name="uml_PackageableElement103", type=uml_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Model", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uml_Comment_Element = Generalization(general=Element, specific=uml_Comment)
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_NamedElement_Element = Generalization(general=Element, specific=uml_NamedElement)
gen_uml_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml_Dependency)
gen_uml_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Dependency)
gen_uml_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=uml_DirectedRelationship)
gen_uml_Relationship_Element = Generalization(general=Element, specific=uml_Relationship)
gen_uml_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml_Namespace)
gen_uml_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_ElementImport)
gen_uml_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_PackageImport)
gen_uml_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=uml_ValueSpecification)
gen_uml_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=uml_ValueSpecification)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_Association_Classifier = Generalization(general=Classifier, specific=uml_Association)
gen_uml_Association_Relationship = Generalization(general=Relationship, specific=uml_Association)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Substitution_Realization = Generalization(general=Realization, specific=uml_Substitution)
gen_uml_Realization_Abstraction = Generalization(general=Abstraction, specific=uml_Realization)
gen_uml_Abstraction_Dependency = Generalization(general=Dependency, specific=uml_Abstraction)
gen_uml_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml_Operation)
gen_uml_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=uml_BehavioralFeature)
gen_uml_BehavioralFeature_Feature = Generalization(general=Feature, specific=uml_BehavioralFeature)
gen_uml_Class_Classifier = Generalization(general=Classifier, specific=uml_Class)
gen_uml_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Generalization)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Comment, Element, uml_Element, uml_PackageableElement, uml_Package, PackageableElement, uml_Type, uml_NamedElement, uml_Dependency, uml_Namespace, DirectedRelationship, uml_DirectedRelationship, Relationship, uml_Relationship, NamedElement, uml_ElementImport, uml_PackageImport, uml_ValueSpecification, TypedElement, uml_TypedElement, uml_Association, Classifier, uml_Property, uml_Substitution, uml_Classifier, Type, uml_Feature, Realization, uml_Realization, Abstraction, uml_Abstraction, Dependency, uml_Parameter, uml_Operation, uml_Class, BehavioralFeature, uml_BehavioralFeature, Namespace, Feature, uml_Generalization, uml_Model, VisibilityKind},
    associations={annotatedElement0, ownedElement2, owner4, ownedComment6, ownedType9, packagedElement10, namespace12, clientDependency11, supplier13, client14, source15, target17, relatedElement20, elementImport22, packageImport23, member25, importedMember27, ownedMember30, importingNamespace38, importedElement32, importingNamespace34, importedPackage36, endType46, type40, package41, ownedEnd42, memberEnd43, substitution61, navigableOwnedEnd49, feature52, inheritedMember53, redefinedClassifier56, general59, defaultValue71, attribute62, featuringClassifier65, contract66, substitutingClassifier68, operation70, raisedException81, type73, class75, redefinedOperation77, ownedParameter79, generalization94, nestedClassifier84, ownedOperation87, superClass89, ownedAttribute91, general96, specific99, packagedElement102},
    generalizations={gen_uml_Comment_Element, gen_uml_Package_PackageableElement, gen_uml_NamedElement_Element, gen_uml_Dependency_PackageableElement, gen_uml_Dependency_DirectedRelationship, gen_uml_DirectedRelationship_Relationship, gen_uml_Relationship_Element, gen_uml_Namespace_NamedElement, gen_uml_ElementImport_DirectedRelationship, gen_uml_PackageImport_DirectedRelationship, gen_uml_ValueSpecification_PackageableElement, gen_uml_ValueSpecification_TypedElement, gen_uml_TypedElement_NamedElement, gen_uml_Type_PackageableElement, gen_uml_Association_Classifier, gen_uml_Association_Relationship, gen_uml_Classifier_Type, gen_uml_Substitution_Realization, gen_uml_Realization_Abstraction, gen_uml_Abstraction_Dependency, gen_uml_Operation_BehavioralFeature, gen_uml_BehavioralFeature_Namespace, gen_uml_BehavioralFeature_Feature, gen_uml_Class_Classifier, gen_uml_Generalization_DirectedRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)