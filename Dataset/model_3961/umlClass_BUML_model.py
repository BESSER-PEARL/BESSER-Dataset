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

# Classes
umlClass_Operation = Class(name="umlClass::Operation")
umlClass_Association = Class(name="umlClass::Association")
StructuralFeature = Class(name="StructuralFeature")
umlClass_DataType = Class(name="umlClass::DataType")
umlClass_NamedElement = Class(name="umlClass::NamedElement", is_abstract=True)
Element = Class(name="Element")
umlClass_Classifier = Class(name="umlClass::Classifier", is_abstract=True)
NamedElement = Class(name="NamedElement")
umlClass_Property = Class(name="umlClass::Property")
umlClass_Package = Class(name="umlClass::Package")
umlClass_Generalization = Class(name="umlClass::Generalization")
umlClass_StructuralFeature = Class(name="umlClass::StructuralFeature", is_abstract=True)
TypedElement = Class(name="TypedElement")
umlClass_Class = Class(name="umlClass::Class")
Classifier = Class(name="Classifier")
umlClass_TypedElement = Class(name="umlClass::TypedElement", is_abstract=True)
Relationship = Class(name="Relationship")
DirectedRelationship = Class(name="DirectedRelationship")
umlClass_Relationship = Class(name="umlClass::Relationship", is_abstract=True)
umlClass_Element = Class(name="umlClass::Element", is_abstract=True)
umlClass_DirectedRelationship = Class(name="umlClass::DirectedRelationship", is_abstract=True)
umlClass_OptionalOperation = Class(name="umlClass::OptionalOperation")
Operation = Class(name="Operation")
umlClass_AlternativeOperation = Class(name="umlClass::AlternativeOperation")

# umlClass_Operation class attributes and methods
umlClass_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
umlClass_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
umlClass_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
umlClass_Operation_lower: Property = Property(name="lower", type=StringType)
umlClass_Operation_upper: Property = Property(name="upper", type=StringType)
umlClass_Operation.attributes={umlClass_Operation_isOrdered, umlClass_Operation_lower, umlClass_Operation_isQuery, umlClass_Operation_upper, umlClass_Operation_isUnique}

# umlClass_Association class attributes and methods

# StructuralFeature class attributes and methods

# umlClass_DataType class attributes and methods

# umlClass_NamedElement class attributes and methods
umlClass_NamedElement_name: Property = Property(name="name", type=StringType)
umlClass_NamedElement_Archpoint: Property = Property(name="Archpoint", type=StringType)
umlClass_NamedElement.attributes={umlClass_NamedElement_Archpoint, umlClass_NamedElement_name}

# Element class attributes and methods

# umlClass_Classifier class attributes and methods

# NamedElement class attributes and methods

# umlClass_Property class attributes and methods

# umlClass_Package class attributes and methods

# umlClass_Generalization class attributes and methods

# umlClass_StructuralFeature class attributes and methods
umlClass_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
umlClass_StructuralFeature.attributes={umlClass_StructuralFeature_isReadOnly}

# TypedElement class attributes and methods

# umlClass_Class class attributes and methods
umlClass_Class_isActive: Property = Property(name="isActive", type=StringType)
umlClass_Class.attributes={umlClass_Class_isActive}

# Classifier class attributes and methods

# umlClass_TypedElement class attributes and methods

# Relationship class attributes and methods

# DirectedRelationship class attributes and methods

# umlClass_Relationship class attributes and methods

# umlClass_Element class attributes and methods

# umlClass_DirectedRelationship class attributes and methods

# umlClass_OptionalOperation class attributes and methods

# Operation class attributes and methods

# umlClass_AlternativeOperation class attributes and methods

# Relationships
ownedOperation5: BinaryAssociation = BinaryAssociation(
    name="ownedOperation5",
    ends={
        Property(name="Operation", type=umlClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=umlClass_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute6: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute6",
    ends={
        Property(name="Property8", type=umlClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class7", type=umlClass_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass10: BinaryAssociation = BinaryAssociation(
    name="superClass10",
    ends={
        Property(name="umlClass_Class", type=umlClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Class9", type=umlClass_Class, multiplicity=Multiplicity(0, 9999))
    }
)
reference11: BinaryAssociation = BinaryAssociation(
    name="reference11",
    ends={
        Property(name="umlClass_Association", type=umlClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Class12", type=umlClass_Association, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier13: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier13",
    ends={
        Property(name="umlClass_Classifier15", type=umlClass_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Class14", type=umlClass_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class16: BinaryAssociation = BinaryAssociation(
    name="class16",
    ends={
        Property(name="Class", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=umlClass_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype17: BinaryAssociation = BinaryAssociation(
    name="datatype17",
    ends={
        Property(name="DataType", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute18", type=umlClass_DataType, multiplicity=Multiplicity(0, 1))
    }
)
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="Property", type=umlClass_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=umlClass_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier2: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier2",
    ends={
        Property(name="umlClass_Classifier", type=umlClass_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Classifier1", type=umlClass_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
package3: BinaryAssociation = BinaryAssociation(
    name="package3",
    ends={
        Property(name="Package", type=umlClass_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers", type=umlClass_Package, multiplicity=Multiplicity(0, 1))
    }
)
generalization4: BinaryAssociation = BinaryAssociation(
    name="generalization4",
    ends={
        Property(name="Generalization", type=umlClass_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=umlClass_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute46: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute46",
    ends={
        Property(name="Property47", type=umlClass_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=umlClass_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation48: BinaryAssociation = BinaryAssociation(
    name="ownedOperation48",
    ends={
        Property(name="Operation50", type=umlClass_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype49", type=umlClass_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifiers51: BinaryAssociation = BinaryAssociation(
    name="classifiers51",
    ends={
        Property(name="Classifier52", type=umlClass_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=umlClass_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite20: BinaryAssociation = BinaryAssociation(
    name="opposite20",
    ends={
        Property(name="umlClass_Property", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Property19", type=umlClass_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation21: BinaryAssociation = BinaryAssociation(
    name="owningAssociation21",
    ends={
        Property(name="Association", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=umlClass_Association, multiplicity=Multiplicity(0, 1))
    }
)
association22: BinaryAssociation = BinaryAssociation(
    name="association22",
    ends={
        Property(name="Association23", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=umlClass_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty25: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty25",
    ends={
        Property(name="umlClass_Property26", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Property24", type=umlClass_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty28: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty28",
    ends={
        Property(name="umlClass_Property29", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Property27", type=umlClass_Property, multiplicity=Multiplicity(0, 9999))
    }
)
classifier30: BinaryAssociation = BinaryAssociation(
    name="classifier30",
    ends={
        Property(name="Classifier", type=umlClass_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=umlClass_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd31: BinaryAssociation = BinaryAssociation(
    name="ownedEnd31",
    ends={
        Property(name="Property32", type=umlClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=umlClass_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd33: BinaryAssociation = BinaryAssociation(
    name="memberEnd33",
    ends={
        Property(name="Property34", type=umlClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=umlClass_Property, multiplicity=Multiplicity(2, 9999))
    }
)
navigableOwnedEnd35: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd35",
    ends={
        Property(name="umlClass_Property37", type=umlClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Association36", type=umlClass_Property, multiplicity=Multiplicity(0, 9999))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="umlClass_Class40", type=umlClass_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Association39", type=umlClass_Class, multiplicity=Multiplicity(1, 1))
    }
)
class41: BinaryAssociation = BinaryAssociation(
    name="class41",
    ends={
        Property(name="Class42", type=umlClass_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=umlClass_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype43: BinaryAssociation = BinaryAssociation(
    name="datatype43",
    ends={
        Property(name="DataType45", type=umlClass_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation44", type=umlClass_DataType, multiplicity=Multiplicity(0, 1))
    }
)
specific53: BinaryAssociation = BinaryAssociation(
    name="specific53",
    ends={
        Property(name="Classifier54", type=umlClass_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=umlClass_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
target55: BinaryAssociation = BinaryAssociation(
    name="target55",
    ends={
        Property(name="umlClass_Class56", type=umlClass_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Generalization", type=umlClass_Class, multiplicity=Multiplicity(1, 9999))
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="umlClass_Class59", type=umlClass_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_Generalization58", type=umlClass_Class, multiplicity=Multiplicity(1, 9999))
    }
)
owner61: BinaryAssociation = BinaryAssociation(
    name="owner61",
    ends={
        Property(name="Element", type=umlClass_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=umlClass_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedElement63: BinaryAssociation = BinaryAssociation(
    name="ownedElement63",
    ends={
        Property(name="Element64", type=umlClass_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umlClass_Element, multiplicity=Multiplicity(0, 9999))
    }
)
operations65: BinaryAssociation = BinaryAssociation(
    name="operations65",
    ends={
        Property(name="umlClass_Operation", type=umlClass_AlternativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlClass_AlternativeOperation", type=umlClass_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_umlClass_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=umlClass_Property)
gen_umlClass_NamedElement_Element = Generalization(general=Element, specific=umlClass_NamedElement)
gen_umlClass_Classifier_NamedElement = Generalization(general=NamedElement, specific=umlClass_Classifier)
gen_umlClass_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=umlClass_StructuralFeature)
gen_umlClass_Class_Classifier = Generalization(general=Classifier, specific=umlClass_Class)
gen_umlClass_DataType_Classifier = Generalization(general=Classifier, specific=umlClass_DataType)
gen_umlClass_TypedElement_NamedElement = Generalization(general=NamedElement, specific=umlClass_TypedElement)
gen_umlClass_Package_NamedElement = Generalization(general=NamedElement, specific=umlClass_Package)
gen_umlClass_Association_Classifier = Generalization(general=Classifier, specific=umlClass_Association)
gen_umlClass_Association_Relationship = Generalization(general=Relationship, specific=umlClass_Association)
gen_umlClass_Operation_NamedElement = Generalization(general=NamedElement, specific=umlClass_Operation)
gen_umlClass_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=umlClass_Generalization)
gen_umlClass_Relationship_Element = Generalization(general=Element, specific=umlClass_Relationship)
gen_umlClass_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=umlClass_DirectedRelationship)
gen_umlClass_OptionalOperation_Operation = Generalization(general=Operation, specific=umlClass_OptionalOperation)
gen_umlClass_AlternativeOperation_Operation = Generalization(general=Operation, specific=umlClass_AlternativeOperation)

# Domain Model
domain_model = DomainModel(
    name="umlClass",
    types={umlClass_Operation, umlClass_Association, StructuralFeature, umlClass_DataType, umlClass_NamedElement, Element, umlClass_Classifier, NamedElement, umlClass_Property, umlClass_Package, umlClass_Generalization, umlClass_StructuralFeature, TypedElement, umlClass_Class, Classifier, umlClass_TypedElement, Relationship, DirectedRelationship, umlClass_Relationship, umlClass_Element, umlClass_DirectedRelationship, umlClass_OptionalOperation, Operation, umlClass_AlternativeOperation},
    associations={ownedOperation5, ownedAttribute6, superClass10, reference11, nestedClassifier13, class16, datatype17, attribute0, redefinedClassifier2, package3, generalization4, ownedAttribute46, ownedOperation48, classifiers51, opposite20, owningAssociation21, association22, redefinedProperty25, subsettedProperty28, classifier30, ownedEnd31, memberEnd33, navigableOwnedEnd35, target38, class41, datatype43, specific53, target55, source57, owner61, ownedElement63, operations65},
    generalizations={gen_umlClass_Property_StructuralFeature, gen_umlClass_NamedElement_Element, gen_umlClass_Classifier_NamedElement, gen_umlClass_StructuralFeature_TypedElement, gen_umlClass_Class_Classifier, gen_umlClass_DataType_Classifier, gen_umlClass_TypedElement_NamedElement, gen_umlClass_Package_NamedElement, gen_umlClass_Association_Classifier, gen_umlClass_Association_Relationship, gen_umlClass_Operation_NamedElement, gen_umlClass_Generalization_DirectedRelationship, gen_umlClass_Relationship_Element, gen_umlClass_DirectedRelationship_Relationship, gen_umlClass_OptionalOperation_Operation, gen_umlClass_AlternativeOperation_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)