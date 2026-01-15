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
uml_Operation = Class(name="uml::Operation")
Element = Class(name="Element")
Feature = Class(name="Feature")
NamedElement = Class(name="NamedElement")
uml_Parameter = Class(name="uml::Parameter")
uml_Behavior = Class(name="uml::Behavior")
uml_Property = Class(name="uml::Property")
TypedElement = Class(name="TypedElement")
uml_Class = Class(name="uml::Class")
Classifier = Class(name="Classifier")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
uml_Package = Class(name="uml::Package")
PackageableElement = Class(name="PackageableElement")
uml_Dependency = Class(name="uml::Dependency")
Type = Class(name="Type")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_Element = Class(name="uml::Element", is_abstract=True)
uml_Model = Class(name="uml::Model")
Package = Class(name="Package")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
uml_Feature = Class(name="uml::Feature", is_abstract=True)
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
Class_ = Class(name="Class")

# uml_Operation class attributes and methods

# Element class attributes and methods

# Feature class attributes and methods

# NamedElement class attributes and methods

# uml_Parameter class attributes and methods

# uml_Behavior class attributes and methods

# uml_Property class attributes and methods

# TypedElement class attributes and methods

# uml_Class class attributes and methods
uml_Class_isLeaf: Property = Property(name="isLeaf", type=StringType)
uml_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Class.attributes={uml_Class_isAbstract, uml_Class_isLeaf}

# Classifier class attributes and methods

# uml_Classifier class attributes and methods

# uml_Package class attributes and methods

# PackageableElement class attributes and methods

# uml_Dependency class attributes and methods

# Type class attributes and methods

# uml_TypedElement class attributes and methods

# uml_Type class attributes and methods

# uml_Element class attributes and methods

# uml_Model class attributes and methods

# Package class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_name, uml_NamedElement_visibility}

# uml_Feature class attributes and methods

# uml_PackageableElement class attributes and methods

# Class class attributes and methods

# Relationships
ownedParameter0: BinaryAssociation = BinaryAssociation(
    name="ownedParameter0",
    ends={
        Property(name="uml_Parameter", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method1: BinaryAssociation = BinaryAssociation(
    name="method1",
    ends={
        Property(name="uml_Behavior", type=uml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Operation2", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier3: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier3",
    ends={
        Property(name="uml_Classifier", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation4: BinaryAssociation = BinaryAssociation(
    name="ownedOperation4",
    ends={
        Property(name="uml_Operation6", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class5", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute7: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute7",
    ends={
        Property(name="uml_Property", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class8", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizationGeneral9: BinaryAssociation = BinaryAssociation(
    name="generalizationGeneral9",
    ends={
        Property(name="uml_Classifier11", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class10", type=uml_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement12: BinaryAssociation = BinaryAssociation(
    name="packagedElement12",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="uml_NamedElement16", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Dependency15", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
owner19: BinaryAssociation = BinaryAssociation(
    name="owner19",
    ends={
        Property(name="uml_Element", type=uml_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Element18", type=uml_Element, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uml_Operation_Element = Generalization(general=Element, specific=uml_Operation)
gen_uml_Operation_Feature = Generalization(general=Feature, specific=uml_Operation)
gen_uml_Operation_NamedElement = Generalization(general=NamedElement, specific=uml_Operation)
gen_uml_Property_TypedElement = Generalization(general=TypedElement, specific=uml_Property)
gen_uml_Property_Feature = Generalization(general=Feature, specific=uml_Property)
gen_uml_Property_Element = Generalization(general=Element, specific=uml_Property)
gen_uml_Property_NamedElement = Generalization(general=NamedElement, specific=uml_Property)
gen_uml_Class_Classifier = Generalization(general=Classifier, specific=uml_Class)
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_Package_Element = Generalization(general=Element, specific=uml_Package)
gen_uml_Package_NamedElement = Generalization(general=NamedElement, specific=uml_Package)
gen_uml_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml_Dependency)
gen_uml_Dependency_Element = Generalization(general=Element, specific=uml_Dependency)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Classifier_Element = Generalization(general=Element, specific=uml_Classifier)
gen_uml_Classifier_NamedElement = Generalization(general=NamedElement, specific=uml_Classifier)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_Model_Package = Generalization(general=Package, specific=uml_Model)
gen_uml_NamedElement_Element = Generalization(general=Element, specific=uml_NamedElement)
gen_uml_Feature_NamedElement = Generalization(general=NamedElement, specific=uml_Feature)
gen_uml_Parameter_Element = Generalization(general=Element, specific=uml_Parameter)
gen_uml_Parameter_TypedElement = Generalization(general=TypedElement, specific=uml_Parameter)
gen_uml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml_PackageableElement)
gen_uml_PackageableElement_Element = Generalization(general=Element, specific=uml_PackageableElement)
gen_uml_Behavior_Class = Generalization(general=Class_, specific=uml_Behavior)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Operation, Element, Feature, NamedElement, uml_Parameter, uml_Behavior, uml_Property, TypedElement, uml_Class, Classifier, uml_Classifier, uml_Package, PackageableElement, uml_Dependency, Type, uml_TypedElement, uml_Type, uml_Element, uml_Model, Package, uml_NamedElement, uml_Feature, uml_PackageableElement, Class_, VisibilityKind},
    associations={ownedParameter0, method1, nestedClassifier3, ownedOperation4, ownedAttribute7, generalizationGeneral9, packagedElement12, supplier13, client14, type17, owner19},
    generalizations={gen_uml_Operation_Element, gen_uml_Operation_Feature, gen_uml_Operation_NamedElement, gen_uml_Property_TypedElement, gen_uml_Property_Feature, gen_uml_Property_Element, gen_uml_Property_NamedElement, gen_uml_Class_Classifier, gen_uml_Package_PackageableElement, gen_uml_Package_Element, gen_uml_Package_NamedElement, gen_uml_Dependency_PackageableElement, gen_uml_Dependency_Element, gen_uml_Classifier_Type, gen_uml_Classifier_Element, gen_uml_Classifier_NamedElement, gen_uml_TypedElement_NamedElement, gen_uml_Type_PackageableElement, gen_uml_Model_Package, gen_uml_NamedElement_Element, gen_uml_Feature_NamedElement, gen_uml_Parameter_Element, gen_uml_Parameter_TypedElement, gen_uml_PackageableElement_NamedElement, gen_uml_PackageableElement_Element, gen_uml_Behavior_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)