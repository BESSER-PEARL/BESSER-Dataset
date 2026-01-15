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
UMLMM_Interface = Class(name="UMLMM::Interface")
Classifier = Class(name="Classifier")
UMLMM_Model = Class(name="UMLMM::Model")
Package = Class(name="Package")
UMLMM_Class = Class(name="UMLMM::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
UMLMM_Operation = Class(name="UMLMM::Operation")
UMLMM_Generalization = Class(name="UMLMM::Generalization")
DirectedRelationship = Class(name="DirectedRelationship")
UMLMM_Classifier = Class(name="UMLMM::Classifier", is_abstract=True)
UMLMM_StructuredClassifier = Class(name="UMLMM::StructuredClassifier", is_abstract=True)
UMLMM_Package = Class(name="UMLMM::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
TemplateableElement = Class(name="TemplateableElement")
UMLMM_PackageableElement = Class(name="UMLMM::PackageableElement", is_abstract=True)
UMLMM_TemplateableElement = Class(name="UMLMM::TemplateableElement", is_abstract=True)
UMLMM_RedefinableElement = Class(name="UMLMM::RedefinableElement", is_abstract=True)
UMLMM_Type = Class(name="UMLMM::Type", is_abstract=True)
UMLMM_BehavioralFeature = Class(name="UMLMM::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
UMLMM_Feature = Class(name="UMLMM::Feature", is_abstract=True)
UMLMM_Realization = Class(name="UMLMM::Realization")
Abstraction = Class(name="Abstraction")
UMLMM_Abstraction = Class(name="UMLMM::Abstraction")
Dependency = Class(name="Dependency")
UMLMM_Dependency = Class(name="UMLMM::Dependency")
UMLMM_DirectedRelationship = Class(name="UMLMM::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
UMLMM_Relationship = Class(name="UMLMM::Relationship", is_abstract=True)
UMLMM_Property = Class(name="UMLMM::Property")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
UMLMM_BehavioredClassifier = Class(name="UMLMM::BehavioredClassifier", is_abstract=True)
UMLMM_InterfaceRealization = Class(name="UMLMM::InterfaceRealization")
Realization = Class(name="Realization")
NamedElement = Class(name="NamedElement")
ParameterableElement = Class(name="ParameterableElement")
UMLMM_NamedElement = Class(name="UMLMM::NamedElement", is_abstract=True)
Element = Class(name="Element")
BehavioralFeature = Class(name="BehavioralFeature")
UMLMM_Element = Class(name="UMLMM::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
UMLMM_EModelElement = Class(name="UMLMM::EModelElement", is_abstract=True)
UMLMM_ParameterableElement = Class(name="UMLMM::ParameterableElement", is_abstract=True)
UMLMM_Namespace = Class(name="UMLMM::Namespace", is_abstract=True)
UMLMM_StructuralFeature = Class(name="UMLMM::StructuralFeature", is_abstract=True)
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
UMLMM_TypedElement = Class(name="UMLMM::TypedElement", is_abstract=True)
UMLMM_MultiplicityElement = Class(name="UMLMM::MultiplicityElement", is_abstract=True)
UMLMM_ConnectableElement = Class(name="UMLMM::ConnectableElement", is_abstract=True)
UMLMM_DeploymentTarget = Class(name="UMLMM::DeploymentTarget", is_abstract=True)
UMLMM_EncapsulatedClassifier = Class(name="UMLMM::EncapsulatedClassifier", is_abstract=True)
StructuredClassifier = Class(name="StructuredClassifier")

# UMLMM_Interface class attributes and methods

# Classifier class attributes and methods

# UMLMM_Model class attributes and methods

# Package class attributes and methods

# UMLMM_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# BehavioredClassifier class attributes and methods

# UMLMM_Operation class attributes and methods

# UMLMM_Generalization class attributes and methods

# DirectedRelationship class attributes and methods

# UMLMM_Classifier class attributes and methods
UMLMM_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
UMLMM_Classifier.attributes={UMLMM_Classifier_isAbstract}

# UMLMM_StructuredClassifier class attributes and methods

# UMLMM_Package class attributes and methods

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# TemplateableElement class attributes and methods

# UMLMM_PackageableElement class attributes and methods

# UMLMM_TemplateableElement class attributes and methods

# UMLMM_RedefinableElement class attributes and methods

# UMLMM_Type class attributes and methods

# UMLMM_BehavioralFeature class attributes and methods

# Feature class attributes and methods

# UMLMM_Feature class attributes and methods

# UMLMM_Realization class attributes and methods

# Abstraction class attributes and methods

# UMLMM_Abstraction class attributes and methods

# Dependency class attributes and methods

# UMLMM_Dependency class attributes and methods

# UMLMM_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# UMLMM_Relationship class attributes and methods

# UMLMM_Property class attributes and methods

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# RedefinableElement class attributes and methods

# Type class attributes and methods

# UMLMM_BehavioredClassifier class attributes and methods

# UMLMM_InterfaceRealization class attributes and methods

# Realization class attributes and methods

# NamedElement class attributes and methods

# ParameterableElement class attributes and methods

# UMLMM_NamedElement class attributes and methods
UMLMM_NamedElement_name: Property = Property(name="name", type=StringType)
UMLMM_NamedElement.attributes={UMLMM_NamedElement_name}

# Element class attributes and methods

# BehavioralFeature class attributes and methods

# UMLMM_Element class attributes and methods

# EModelElement class attributes and methods

# UMLMM_EModelElement class attributes and methods

# UMLMM_ParameterableElement class attributes and methods

# UMLMM_Namespace class attributes and methods

# UMLMM_StructuralFeature class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# UMLMM_TypedElement class attributes and methods

# UMLMM_MultiplicityElement class attributes and methods

# UMLMM_ConnectableElement class attributes and methods

# UMLMM_DeploymentTarget class attributes and methods

# UMLMM_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# Relationships
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="UMLMM_Operation", type=UMLMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_Class", type=UMLMM_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general2: BinaryAssociation = BinaryAssociation(
    name="general2",
    ends={
        Property(name="UMLMM_Classifier", type=UMLMM_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_Generalization", type=UMLMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement0: BinaryAssociation = BinaryAssociation(
    name="packagedElement0",
    ends={
        Property(name="UMLMM_PackageableElement", type=UMLMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_Package", type=UMLMM_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute3: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute3",
    ends={
        Property(name="UMLMM_Property", type=UMLMM_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_StructuredClassifier", type=UMLMM_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization4: BinaryAssociation = BinaryAssociation(
    name="generalization4",
    ends={
        Property(name="UMLMM_Generalization6", type=UMLMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_Classifier5", type=UMLMM_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceRealization7: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization7",
    ends={
        Property(name="UMLMM_InterfaceRealization", type=UMLMM_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMM_BehavioredClassifier", type=UMLMM_InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UMLMM_Interface_Classifier = Generalization(general=Classifier, specific=UMLMM_Interface)
gen_UMLMM_Model_Package = Generalization(general=Package, specific=UMLMM_Model)
gen_UMLMM_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UMLMM_Class)
gen_UMLMM_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UMLMM_Class)
gen_UMLMM_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLMM_Generalization)
gen_UMLMM_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UMLMM_StructuredClassifier)
gen_UMLMM_Package_Namespace = Generalization(general=Namespace, specific=UMLMM_Package)
gen_UMLMM_Package_PackageableElement = Generalization(general=PackageableElement, specific=UMLMM_Package)
gen_UMLMM_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLMM_Package)
gen_UMLMM_TemplateableElement_Element = Generalization(general=Element, specific=UMLMM_TemplateableElement)
gen_UMLMM_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=UMLMM_RedefinableElement)
gen_UMLMM_Type_PackageableElement = Generalization(general=PackageableElement, specific=UMLMM_Type)
gen_UMLMM_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=UMLMM_BehavioralFeature)
gen_UMLMM_BehavioralFeature_Feature = Generalization(general=Feature, specific=UMLMM_BehavioralFeature)
gen_UMLMM_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLMM_Feature)
gen_UMLMM_Realization_Abstraction = Generalization(general=Abstraction, specific=UMLMM_Realization)
gen_UMLMM_Abstraction_Dependency = Generalization(general=Dependency, specific=UMLMM_Abstraction)
gen_UMLMM_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=UMLMM_Dependency)
gen_UMLMM_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=UMLMM_Dependency)
gen_UMLMM_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=UMLMM_DirectedRelationship)
gen_UMLMM_Relationship_Element = Generalization(general=Element, specific=UMLMM_Relationship)
gen_UMLMM_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UMLMM_Property)
gen_UMLMM_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=UMLMM_Property)
gen_UMLMM_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=UMLMM_Property)
gen_UMLMM_Classifier_Namespace = Generalization(general=Namespace, specific=UMLMM_Classifier)
gen_UMLMM_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=UMLMM_Classifier)
gen_UMLMM_Classifier_Type = Generalization(general=Type, specific=UMLMM_Classifier)
gen_UMLMM_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLMM_Classifier)
gen_UMLMM_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UMLMM_BehavioredClassifier)
gen_UMLMM_InterfaceRealization_Realization = Generalization(general=Realization, specific=UMLMM_InterfaceRealization)
gen_UMLMM_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=UMLMM_PackageableElement)
gen_UMLMM_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLMM_PackageableElement)
gen_UMLMM_NamedElement_Element = Generalization(general=Element, specific=UMLMM_NamedElement)
gen_UMLMM_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UMLMM_Operation)
gen_UMLMM_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLMM_Operation)
gen_UMLMM_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=UMLMM_Operation)
gen_UMLMM_Element_EModelElement = Generalization(general=EModelElement, specific=UMLMM_Element)
gen_UMLMM_ParameterableElement_Element = Generalization(general=Element, specific=UMLMM_ParameterableElement)
gen_UMLMM_Namespace_NamedElement = Generalization(general=NamedElement, specific=UMLMM_Namespace)
gen_UMLMM_StructuralFeature_Feature = Generalization(general=Feature, specific=UMLMM_StructuralFeature)
gen_UMLMM_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UMLMM_StructuralFeature)
gen_UMLMM_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UMLMM_StructuralFeature)
gen_UMLMM_TypedElement_NamedElement = Generalization(general=NamedElement, specific=UMLMM_TypedElement)
gen_UMLMM_MultiplicityElement_Element = Generalization(general=Element, specific=UMLMM_MultiplicityElement)
gen_UMLMM_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=UMLMM_ConnectableElement)
gen_UMLMM_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=UMLMM_ConnectableElement)
gen_UMLMM_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=UMLMM_DeploymentTarget)
gen_UMLMM_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UMLMM_EncapsulatedClassifier)

# Domain Model
domain_model = DomainModel(
    name="UMLMM",
    types={UMLMM_Interface, Classifier, UMLMM_Model, Package, UMLMM_Class, EncapsulatedClassifier, BehavioredClassifier, UMLMM_Operation, UMLMM_Generalization, DirectedRelationship, UMLMM_Classifier, UMLMM_StructuredClassifier, UMLMM_Package, Namespace, PackageableElement, TemplateableElement, UMLMM_PackageableElement, UMLMM_TemplateableElement, UMLMM_RedefinableElement, UMLMM_Type, UMLMM_BehavioralFeature, Feature, UMLMM_Feature, UMLMM_Realization, Abstraction, UMLMM_Abstraction, Dependency, UMLMM_Dependency, UMLMM_DirectedRelationship, Relationship, UMLMM_Relationship, UMLMM_Property, StructuralFeature, ConnectableElement, DeploymentTarget, RedefinableElement, Type, UMLMM_BehavioredClassifier, UMLMM_InterfaceRealization, Realization, NamedElement, ParameterableElement, UMLMM_NamedElement, Element, BehavioralFeature, UMLMM_Element, EModelElement, UMLMM_EModelElement, UMLMM_ParameterableElement, UMLMM_Namespace, UMLMM_StructuralFeature, TypedElement, MultiplicityElement, UMLMM_TypedElement, UMLMM_MultiplicityElement, UMLMM_ConnectableElement, UMLMM_DeploymentTarget, UMLMM_EncapsulatedClassifier, StructuredClassifier},
    associations={ownedOperation1, general2, packagedElement0, ownedAttribute3, generalization4, interfaceRealization7},
    generalizations={gen_UMLMM_Interface_Classifier, gen_UMLMM_Model_Package, gen_UMLMM_Class_EncapsulatedClassifier, gen_UMLMM_Class_BehavioredClassifier, gen_UMLMM_Generalization_DirectedRelationship, gen_UMLMM_StructuredClassifier_Classifier, gen_UMLMM_Package_Namespace, gen_UMLMM_Package_PackageableElement, gen_UMLMM_Package_TemplateableElement, gen_UMLMM_TemplateableElement_Element, gen_UMLMM_RedefinableElement_NamedElement, gen_UMLMM_Type_PackageableElement, gen_UMLMM_BehavioralFeature_Namespace, gen_UMLMM_BehavioralFeature_Feature, gen_UMLMM_Feature_RedefinableElement, gen_UMLMM_Realization_Abstraction, gen_UMLMM_Abstraction_Dependency, gen_UMLMM_Dependency_PackageableElement, gen_UMLMM_Dependency_DirectedRelationship, gen_UMLMM_DirectedRelationship_Relationship, gen_UMLMM_Relationship_Element, gen_UMLMM_Property_StructuralFeature, gen_UMLMM_Property_ConnectableElement, gen_UMLMM_Property_DeploymentTarget, gen_UMLMM_Classifier_Namespace, gen_UMLMM_Classifier_RedefinableElement, gen_UMLMM_Classifier_Type, gen_UMLMM_Classifier_TemplateableElement, gen_UMLMM_BehavioredClassifier_Classifier, gen_UMLMM_InterfaceRealization_Realization, gen_UMLMM_PackageableElement_NamedElement, gen_UMLMM_PackageableElement_ParameterableElement, gen_UMLMM_NamedElement_Element, gen_UMLMM_Operation_BehavioralFeature, gen_UMLMM_Operation_ParameterableElement, gen_UMLMM_Operation_TemplateableElement, gen_UMLMM_Element_EModelElement, gen_UMLMM_ParameterableElement_Element, gen_UMLMM_Namespace_NamedElement, gen_UMLMM_StructuralFeature_Feature, gen_UMLMM_StructuralFeature_TypedElement, gen_UMLMM_StructuralFeature_MultiplicityElement, gen_UMLMM_TypedElement_NamedElement, gen_UMLMM_MultiplicityElement_Element, gen_UMLMM_ConnectableElement_TypedElement, gen_UMLMM_ConnectableElement_ParameterableElement, gen_UMLMM_DeploymentTarget_NamedElement, gen_UMLMM_EncapsulatedClassifier_StructuredClassifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)