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
OO_concept_Class = Class(name="OO::concept::Class")
Classifier = Class(name="Classifier")
Type = Class(name="Type")
OO_concept_Operation = Class(name="OO::concept::Operation")
OO_concept_Property = Class(name="OO::concept::Property")
OO_concept_Classifier = Class(name="OO::concept::Classifier", is_abstract=True)
OO_concept_NamedElement = Class(name="OO::concept::NamedElement", is_abstract=True)
OO_concept_Model = Class(name="OO::concept::Model")
Package = Class(name="Package")
TypedElement = Class(name="TypedElement")
BehavioralFeature = Class(name="BehavioralFeature")
OO_concept_Parameter = Class(name="OO::concept::Parameter")
OO_concept_Feature = Class(name="OO::concept::Feature", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
OO_concept_Generalization = Class(name="OO::concept::Generalization")
OO_concept_PackageableElement = Class(name="OO::concept::PackageableElement", is_abstract=True)
OO_concept_Package = Class(name="OO::concept::Package")
PackageableElement = Class(name="PackageableElement")
NamedElement = Class(name="NamedElement")
OO_concept_TypedElement = Class(name="OO::concept::TypedElement", is_abstract=True)
OO_concept_Type = Class(name="OO::concept::Type", is_abstract=True)
OO_concept_BehavioralFeature = Class(name="OO::concept::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
OO_concept_Behavior = Class(name="OO::concept::Behavior")
Class_ = Class(name="Class")
OO_concept_StructuralFeature = Class(name="OO::concept::StructuralFeature", is_abstract=True)
OO_concept_Dependency = Class(name="OO::concept::Dependency")

# OO_concept_Class class attributes and methods

# Classifier class attributes and methods

# Type class attributes and methods

# OO_concept_Operation class attributes and methods

# OO_concept_Property class attributes and methods

# OO_concept_Classifier class attributes and methods

# OO_concept_NamedElement class attributes and methods
OO_concept_NamedElement_name: Property = Property(name="name", type=StringType)
OO_concept_NamedElement_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
OO_concept_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
OO_concept_NamedElement.attributes={OO_concept_NamedElement_name, OO_concept_NamedElement_visibility, OO_concept_NamedElement_isAbstract}

# OO_concept_Model class attributes and methods

# Package class attributes and methods

# TypedElement class attributes and methods

# BehavioralFeature class attributes and methods

# OO_concept_Parameter class attributes and methods

# OO_concept_Feature class attributes and methods

# StructuralFeature class attributes and methods

# OO_concept_Generalization class attributes and methods

# OO_concept_PackageableElement class attributes and methods

# OO_concept_Package class attributes and methods

# PackageableElement class attributes and methods

# NamedElement class attributes and methods

# OO_concept_TypedElement class attributes and methods

# OO_concept_Type class attributes and methods

# OO_concept_BehavioralFeature class attributes and methods

# Feature class attributes and methods

# OO_concept_Behavior class attributes and methods

# Class class attributes and methods

# OO_concept_StructuralFeature class attributes and methods

# OO_concept_Dependency class attributes and methods

# Relationships
packagedElement0: BinaryAssociation = BinaryAssociation(
    name="packagedElement0",
    ends={
        Property(name="OO_concept_PackageableElement", type=OO_concept_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Package", type=OO_concept_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="OO_concept_Operation", type=OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Class", type=OO_concept_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute2: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute2",
    ends={
        Property(name="OO_concept_Property", type=OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Class3", type=OO_concept_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier4: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier4",
    ends={
        Property(name="OO_concept_Classifier", type=OO_concept_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Class5", type=OO_concept_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter6: BinaryAssociation = BinaryAssociation(
    name="ownedParameter6",
    ends={
        Property(name="OO_concept_Parameter", type=OO_concept_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Operation7", type=OO_concept_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="OO_concept_Type", type=OO_concept_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_TypedElement", type=OO_concept_Type, multiplicity=Multiplicity(0, 1))
    }
)
method17: BinaryAssociation = BinaryAssociation(
    name="method17",
    ends={
        Property(name="OO_concept_Behavior", type=OO_concept_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_BehavioralFeature", type=OO_concept_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
general8: BinaryAssociation = BinaryAssociation(
    name="general8",
    ends={
        Property(name="OO_concept_Classifier9", type=OO_concept_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Generalization", type=OO_concept_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific10: BinaryAssociation = BinaryAssociation(
    name="specific10",
    ends={
        Property(name="Classifier", type=OO_concept_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=OO_concept_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
supplier11: BinaryAssociation = BinaryAssociation(
    name="supplier11",
    ends={
        Property(name="OO_concept_NamedElement", type=OO_concept_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Dependency", type=OO_concept_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client12: BinaryAssociation = BinaryAssociation(
    name="client12",
    ends={
        Property(name="OO_concept_NamedElement14", type=OO_concept_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_concept_Dependency13", type=OO_concept_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
generalization15: BinaryAssociation = BinaryAssociation(
    name="generalization15",
    ends={
        Property(name="Generalization", type=OO_concept_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=OO_concept_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_OO_concept_Package_NamedElement = Generalization(general=NamedElement, specific=OO_concept_Package)
gen_OO_concept_Class_PackageableElement = Generalization(general=PackageableElement, specific=OO_concept_Class)
gen_OO_concept_Class_Classifier = Generalization(general=Classifier, specific=OO_concept_Class)
gen_OO_concept_Class_Type = Generalization(general=Type, specific=OO_concept_Class)
gen_OO_concept_Model_Package = Generalization(general=Package, specific=OO_concept_Model)
gen_OO_concept_Operation_TypedElement = Generalization(general=TypedElement, specific=OO_concept_Operation)
gen_OO_concept_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=OO_concept_Operation)
gen_OO_concept_Feature_NamedElement = Generalization(general=NamedElement, specific=OO_concept_Feature)
gen_OO_concept_Property_TypedElement = Generalization(general=TypedElement, specific=OO_concept_Property)
gen_OO_concept_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=OO_concept_Property)
gen_OO_concept_Parameter_TypedElement = Generalization(general=TypedElement, specific=OO_concept_Parameter)
gen_OO_concept_Package_PackageableElement = Generalization(general=PackageableElement, specific=OO_concept_Package)
gen_OO_concept_TypedElement_NamedElement = Generalization(general=NamedElement, specific=OO_concept_TypedElement)
gen_OO_concept_Type_NamedElement = Generalization(general=NamedElement, specific=OO_concept_Type)
gen_OO_concept_BehavioralFeature_Feature = Generalization(general=Feature, specific=OO_concept_BehavioralFeature)
gen_OO_concept_Behavior_Class = Generalization(general=Class_, specific=OO_concept_Behavior)
gen_OO_concept_StructuralFeature_Feature = Generalization(general=Feature, specific=OO_concept_StructuralFeature)

# Domain Model
domain_model = DomainModel(
    name="OO_concept",
    types={OO_concept_Class, Classifier, Type, OO_concept_Operation, OO_concept_Property, OO_concept_Classifier, OO_concept_NamedElement, OO_concept_Model, Package, TypedElement, BehavioralFeature, OO_concept_Parameter, OO_concept_Feature, StructuralFeature, OO_concept_Generalization, OO_concept_PackageableElement, OO_concept_Package, PackageableElement, NamedElement, OO_concept_TypedElement, OO_concept_Type, OO_concept_BehavioralFeature, Feature, OO_concept_Behavior, Class_, OO_concept_StructuralFeature, OO_concept_Dependency, VisibilityKind},
    associations={packagedElement0, ownedOperation1, ownedAttribute2, nestedClassifier4, ownedParameter6, type16, method17, general8, specific10, supplier11, client12, generalization15},
    generalizations={gen_OO_concept_Package_NamedElement, gen_OO_concept_Class_PackageableElement, gen_OO_concept_Class_Classifier, gen_OO_concept_Class_Type, gen_OO_concept_Model_Package, gen_OO_concept_Operation_TypedElement, gen_OO_concept_Operation_BehavioralFeature, gen_OO_concept_Feature_NamedElement, gen_OO_concept_Property_TypedElement, gen_OO_concept_Property_StructuralFeature, gen_OO_concept_Parameter_TypedElement, gen_OO_concept_Package_PackageableElement, gen_OO_concept_TypedElement_NamedElement, gen_OO_concept_Type_NamedElement, gen_OO_concept_BehavioralFeature_Feature, gen_OO_concept_Behavior_Class, gen_OO_concept_StructuralFeature_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)