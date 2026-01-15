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
uml_Package = Class(name="uml::Package")
PackageableElement = Class(name="PackageableElement")
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
uml_Property = Class(name="uml::Property")
Feature = Class(name="Feature")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
uml_Parameter = Class(name="uml::Parameter")
TypedElement = Class(name="TypedElement")
uml_Model = Class(name="uml::Model")
Package = Class(name="Package")
uml_Feature = Class(name="uml::Feature", is_abstract=True)
NamedElement = Class(name="NamedElement")
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_Dependency = Class(name="uml::Dependency")
uml_Class = Class(name="uml::Class")
Classifier = Class(name="Classifier")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
uml_Operation = Class(name="uml::Operation")
uml_Behavior = Class(name="uml::Behavior")
Type = Class(name="Type")
Class_ = Class(name="Class")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)

# uml_Package class attributes and methods

# PackageableElement class attributes and methods

# uml_PackageableElement class attributes and methods

# uml_Property class attributes and methods

# Feature class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_visibility, uml_NamedElement_name}

# uml_Parameter class attributes and methods

# TypedElement class attributes and methods

# uml_Model class attributes and methods

# Package class attributes and methods

# uml_Feature class attributes and methods

# NamedElement class attributes and methods

# uml_Type class attributes and methods

# uml_Dependency class attributes and methods

# uml_Class class attributes and methods
uml_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Class.attributes={uml_Class_isAbstract}

# Classifier class attributes and methods

# uml_Classifier class attributes and methods

# uml_Operation class attributes and methods

# uml_Behavior class attributes and methods

# Type class attributes and methods

# Class class attributes and methods

# uml_TypedElement class attributes and methods

# Relationships
packagedElement0: BinaryAssociation = BinaryAssociation(
    name="packagedElement0",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
supplier1: BinaryAssociation = BinaryAssociation(
    name="supplier1",
    ends={
        Property(name="uml_NamedElement", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
nestedClassifier2: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier2",
    ends={
        Property(name="uml_Classifier", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation3: BinaryAssociation = BinaryAssociation(
    name="ownedOperation3",
    ends={
        Property(name="uml_Operation", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class4", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizationGeneral5: BinaryAssociation = BinaryAssociation(
    name="generalizationGeneral5",
    ends={
        Property(name="uml_Classifier7", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class6", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute8: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute8",
    ends={
        Property(name="uml_Property", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class9", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method10: BinaryAssociation = BinaryAssociation(
    name="method10",
    ends={
        Property(name="uml_Behavior", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation11", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter12: BinaryAssociation = BinaryAssociation(
    name="ownedParameter12",
    ends={
        Property(name="uml_Parameter", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation13", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_Package_NamedElement = Generalization(general=NamedElement, specific=uml_Package)
gen_uml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml_PackageableElement)
gen_uml_Property_Feature = Generalization(general=Feature, specific=uml_Property)
gen_uml_Property_TypedElement = Generalization(general=TypedElement, specific=uml_Property)
gen_uml_Property_NamedElement = Generalization(general=NamedElement, specific=uml_Property)
gen_uml_Parameter_TypedElement = Generalization(general=TypedElement, specific=uml_Parameter)
gen_uml_Model_Package = Generalization(general=Package, specific=uml_Model)
gen_uml_Feature_NamedElement = Generalization(general=NamedElement, specific=uml_Feature)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml_Dependency)
gen_uml_Class_Classifier = Generalization(general=Classifier, specific=uml_Class)
gen_uml_Operation_Feature = Generalization(general=Feature, specific=uml_Operation)
gen_uml_Operation_NamedElement = Generalization(general=NamedElement, specific=uml_Operation)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Classifier_NamedElement = Generalization(general=NamedElement, specific=uml_Classifier)
gen_uml_Behavior_Class = Generalization(general=Class_, specific=uml_Behavior)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Package, PackageableElement, uml_PackageableElement, uml_Property, Feature, uml_NamedElement, uml_Parameter, TypedElement, uml_Model, Package, uml_Feature, NamedElement, uml_Type, uml_Dependency, uml_Class, Classifier, uml_Classifier, uml_Operation, uml_Behavior, Type, Class_, uml_TypedElement, VisibilityKind},
    associations={packagedElement0, type14, supplier1, nestedClassifier2, ownedOperation3, generalizationGeneral5, ownedAttribute8, method10, ownedParameter12},
    generalizations={gen_uml_Package_PackageableElement, gen_uml_Package_NamedElement, gen_uml_PackageableElement_NamedElement, gen_uml_Property_Feature, gen_uml_Property_TypedElement, gen_uml_Property_NamedElement, gen_uml_Parameter_TypedElement, gen_uml_Model_Package, gen_uml_Feature_NamedElement, gen_uml_Type_PackageableElement, gen_uml_Dependency_PackageableElement, gen_uml_Class_Classifier, gen_uml_Operation_Feature, gen_uml_Operation_NamedElement, gen_uml_Classifier_Type, gen_uml_Classifier_NamedElement, gen_uml_Behavior_Class, gen_uml_TypedElement_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)