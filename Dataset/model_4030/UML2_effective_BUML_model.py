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
uml_Feature = Class(name="uml::Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
uml_NamedElement = Class(name="uml::NamedElement", is_abstract=True)
Element = Class(name="Element")
uml_PackageableElement = Class(name="uml::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
ParameterableElement = Class(name="ParameterableElement")
uml_Dependency = Class(name="uml::Dependency")
PackageableElement = Class(name="PackageableElement")
DirectedRelationship = Class(name="DirectedRelationship")
uml_Property = Class(name="uml::Property")
StructuralFeature = Class(name="StructuralFeature")
ConnectableElement = Class(name="ConnectableElement")
DeploymentTarget = Class(name="DeploymentTarget")
uml_Generalization = Class(name="uml::Generalization")
uml_Classifier = Class(name="uml::Classifier", is_abstract=True)
TemplateableElement = Class(name="TemplateableElement")
uml_Package = Class(name="uml::Package")
Namespace = Class(name="Namespace")
Type = Class(name="Type")
uml_BehavioralFeature = Class(name="uml::BehavioralFeature", is_abstract=True)
Feature = Class(name="Feature")
uml_Behavior = Class(name="uml::Behavior", is_abstract=True)
Class_ = Class(name="Class")
uml_TypedElement = Class(name="uml::TypedElement", is_abstract=True)
uml_Type = Class(name="uml::Type", is_abstract=True)
uml_Class = Class(name="uml::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
BehavioredClassifier = Class(name="BehavioredClassifier")
uml_Operation = Class(name="uml::Operation")
uml_Parameter = Class(name="uml::Parameter")
MultiplicityElement = Class(name="MultiplicityElement")
uml_Model = Class(name="uml::Model")
Package = Class(name="Package")
BehavioralFeature = Class(name="BehavioralFeature")
uml_RedefinableElement = Class(name="uml::RedefinableElement", is_abstract=True)
uml_ParameterableElement = Class(name="uml::ParameterableElement", is_abstract=True)
uml_TemplateableElement = Class(name="uml::TemplateableElement", is_abstract=True)
uml_BehavioredClassifier = Class(name="uml::BehavioredClassifier", is_abstract=True)
uml_DirectedRelationship = Class(name="uml::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
uml_Relationship = Class(name="uml::Relationship", is_abstract=True)
uml_ConnectableElement = Class(name="uml::ConnectableElement", is_abstract=True)
TypedElement = Class(name="TypedElement")
uml_MultiplicityElement = Class(name="uml::MultiplicityElement", is_abstract=True)
uml_StructuralFeature = Class(name="uml::StructuralFeature", is_abstract=True)
uml_DeploymentTarget = Class(name="uml::DeploymentTarget", is_abstract=True)
uml_StructuredClassifier = Class(name="uml::StructuredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
uml_Element = Class(name="uml::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
uml_EModelElement = Class(name="uml::EModelElement", is_abstract=True)
uml_EncapsulatedClassifier = Class(name="uml::EncapsulatedClassifier", is_abstract=True)
StructuredClassifier = Class(name="StructuredClassifier")
uml_Namespace = Class(name="uml::Namespace", is_abstract=True)

# uml_Feature class attributes and methods

# RedefinableElement class attributes and methods

# uml_NamedElement class attributes and methods
uml_NamedElement_name: Property = Property(name="name", type=StringType)
uml_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
uml_NamedElement.attributes={uml_NamedElement_visibility, uml_NamedElement_name}

# Element class attributes and methods

# uml_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# ParameterableElement class attributes and methods

# uml_Dependency class attributes and methods

# PackageableElement class attributes and methods

# DirectedRelationship class attributes and methods

# uml_Property class attributes and methods

# StructuralFeature class attributes and methods

# ConnectableElement class attributes and methods

# DeploymentTarget class attributes and methods

# uml_Generalization class attributes and methods

# uml_Classifier class attributes and methods
uml_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uml_Classifier.attributes={uml_Classifier_isAbstract}

# TemplateableElement class attributes and methods

# uml_Package class attributes and methods

# Namespace class attributes and methods

# Type class attributes and methods

# uml_BehavioralFeature class attributes and methods

# Feature class attributes and methods

# uml_Behavior class attributes and methods

# Class class attributes and methods

# uml_TypedElement class attributes and methods

# uml_Type class attributes and methods

# uml_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# BehavioredClassifier class attributes and methods

# uml_Operation class attributes and methods

# uml_Parameter class attributes and methods

# MultiplicityElement class attributes and methods

# uml_Model class attributes and methods

# Package class attributes and methods

# BehavioralFeature class attributes and methods

# uml_RedefinableElement class attributes and methods

# uml_ParameterableElement class attributes and methods

# uml_TemplateableElement class attributes and methods

# uml_BehavioredClassifier class attributes and methods

# uml_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# uml_Relationship class attributes and methods

# uml_ConnectableElement class attributes and methods

# TypedElement class attributes and methods

# uml_MultiplicityElement class attributes and methods

# uml_StructuralFeature class attributes and methods

# uml_DeploymentTarget class attributes and methods

# uml_StructuredClassifier class attributes and methods

# Classifier class attributes and methods

# uml_Element class attributes and methods

# EModelElement class attributes and methods

# uml_EModelElement class attributes and methods

# uml_EncapsulatedClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# uml_Namespace class attributes and methods

# Relationships
supplier0: BinaryAssociation = BinaryAssociation(
    name="supplier0",
    ends={
        Property(name="uml_NamedElement", type=uml_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Dependency", type=uml_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
specific1: BinaryAssociation = BinaryAssociation(
    name="specific1",
    ends={
        Property(name="Classifier", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
packagedElement7: BinaryAssociation = BinaryAssociation(
    name="packagedElement7",
    ends={
        Property(name="uml_PackageableElement", type=uml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Package", type=uml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization8: BinaryAssociation = BinaryAssociation(
    name="generalization8",
    ends={
        Property(name="Generalization", type=uml_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=uml_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method9: BinaryAssociation = BinaryAssociation(
    name="method9",
    ends={
        Property(name="uml_Behavior", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature", type=uml_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter10: BinaryAssociation = BinaryAssociation(
    name="ownedParameter10",
    ends={
        Property(name="uml_Parameter", type=uml_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_BehavioralFeature11", type=uml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="uml_Type", type=uml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TypedElement", type=uml_Type, multiplicity=Multiplicity(0, 1))
    }
)
general2: BinaryAssociation = BinaryAssociation(
    name="general2",
    ends={
        Property(name="uml_Classifier", type=uml_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Generalization", type=uml_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperation3: BinaryAssociation = BinaryAssociation(
    name="ownedOperation3",
    ends={
        Property(name="uml_Operation", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class", type=uml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier4: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier4",
    ends={
        Property(name="uml_Classifier6", type=uml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Class5", type=uml_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute13: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute13",
    ends={
        Property(name="uml_Property", type=uml_StructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_StructuredClassifier", type=uml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uml_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Feature)
gen_uml_NamedElement_Element = Generalization(general=Element, specific=uml_NamedElement)
gen_uml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uml_PackageableElement)
gen_uml_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_PackageableElement)
gen_uml_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=uml_Dependency)
gen_uml_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Dependency)
gen_uml_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=uml_Property)
gen_uml_Property_ConnectableElement = Generalization(general=ConnectableElement, specific=uml_Property)
gen_uml_Property_DeploymentTarget = Generalization(general=DeploymentTarget, specific=uml_Property)
gen_uml_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=uml_Generalization)
gen_uml_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_Operation)
gen_uml_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Operation)
gen_uml_Package_Namespace = Generalization(general=Namespace, specific=uml_Package)
gen_uml_Package_PackageableElement = Generalization(general=PackageableElement, specific=uml_Package)
gen_uml_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Package)
gen_uml_Classifier_Namespace = Generalization(general=Namespace, specific=uml_Classifier)
gen_uml_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=uml_Classifier)
gen_uml_Classifier_Type = Generalization(general=Type, specific=uml_Classifier)
gen_uml_Classifier_TemplateableElement = Generalization(general=TemplateableElement, specific=uml_Classifier)
gen_uml_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=uml_BehavioralFeature)
gen_uml_BehavioralFeature_Feature = Generalization(general=Feature, specific=uml_BehavioralFeature)
gen_uml_Behavior_Class = Generalization(general=Class_, specific=uml_Behavior)
gen_uml_TypedElement_NamedElement = Generalization(general=NamedElement, specific=uml_TypedElement)
gen_uml_Type_PackageableElement = Generalization(general=PackageableElement, specific=uml_Type)
gen_uml_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=uml_Class)
gen_uml_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=uml_Class)
gen_uml_Parameter_ConnectableElement = Generalization(general=ConnectableElement, specific=uml_Parameter)
gen_uml_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_Parameter)
gen_uml_Model_Package = Generalization(general=Package, specific=uml_Model)
gen_uml_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=uml_Operation)
gen_uml_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=uml_RedefinableElement)
gen_uml_ParameterableElement_Element = Generalization(general=Element, specific=uml_ParameterableElement)
gen_uml_TemplateableElement_Element = Generalization(general=Element, specific=uml_TemplateableElement)
gen_uml_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=uml_BehavioredClassifier)
gen_uml_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=uml_DirectedRelationship)
gen_uml_Relationship_Element = Generalization(general=Element, specific=uml_Relationship)
gen_uml_ConnectableElement_TypedElement = Generalization(general=TypedElement, specific=uml_ConnectableElement)
gen_uml_ConnectableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=uml_ConnectableElement)
gen_uml_MultiplicityElement_Element = Generalization(general=Element, specific=uml_MultiplicityElement)
gen_uml_StructuralFeature_Feature = Generalization(general=Feature, specific=uml_StructuralFeature)
gen_uml_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=uml_StructuralFeature)
gen_uml_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=uml_StructuralFeature)
gen_uml_DeploymentTarget_NamedElement = Generalization(general=NamedElement, specific=uml_DeploymentTarget)
gen_uml_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=uml_StructuredClassifier)
gen_uml_Element_EModelElement = Generalization(general=EModelElement, specific=uml_Element)
gen_uml_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=uml_EncapsulatedClassifier)
gen_uml_Namespace_NamedElement = Generalization(general=NamedElement, specific=uml_Namespace)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_Feature, RedefinableElement, uml_NamedElement, Element, uml_PackageableElement, NamedElement, ParameterableElement, uml_Dependency, PackageableElement, DirectedRelationship, uml_Property, StructuralFeature, ConnectableElement, DeploymentTarget, uml_Generalization, uml_Classifier, TemplateableElement, uml_Package, Namespace, Type, uml_BehavioralFeature, Feature, uml_Behavior, Class_, uml_TypedElement, uml_Type, uml_Class, EncapsulatedClassifier, BehavioredClassifier, uml_Operation, uml_Parameter, MultiplicityElement, uml_Model, Package, BehavioralFeature, uml_RedefinableElement, uml_ParameterableElement, uml_TemplateableElement, uml_BehavioredClassifier, uml_DirectedRelationship, Relationship, uml_Relationship, uml_ConnectableElement, TypedElement, uml_MultiplicityElement, uml_StructuralFeature, uml_DeploymentTarget, uml_StructuredClassifier, Classifier, uml_Element, EModelElement, uml_EModelElement, uml_EncapsulatedClassifier, StructuredClassifier, uml_Namespace, VisibilityKind},
    associations={supplier0, specific1, packagedElement7, generalization8, method9, ownedParameter10, type12, general2, ownedOperation3, nestedClassifier4, ownedAttribute13},
    generalizations={gen_uml_Feature_RedefinableElement, gen_uml_NamedElement_Element, gen_uml_PackageableElement_NamedElement, gen_uml_PackageableElement_ParameterableElement, gen_uml_Dependency_PackageableElement, gen_uml_Dependency_DirectedRelationship, gen_uml_Property_StructuralFeature, gen_uml_Property_ConnectableElement, gen_uml_Property_DeploymentTarget, gen_uml_Generalization_DirectedRelationship, gen_uml_Operation_ParameterableElement, gen_uml_Operation_TemplateableElement, gen_uml_Package_Namespace, gen_uml_Package_PackageableElement, gen_uml_Package_TemplateableElement, gen_uml_Classifier_Namespace, gen_uml_Classifier_RedefinableElement, gen_uml_Classifier_Type, gen_uml_Classifier_TemplateableElement, gen_uml_BehavioralFeature_Namespace, gen_uml_BehavioralFeature_Feature, gen_uml_Behavior_Class, gen_uml_TypedElement_NamedElement, gen_uml_Type_PackageableElement, gen_uml_Class_EncapsulatedClassifier, gen_uml_Class_BehavioredClassifier, gen_uml_Parameter_ConnectableElement, gen_uml_Parameter_MultiplicityElement, gen_uml_Model_Package, gen_uml_Operation_BehavioralFeature, gen_uml_RedefinableElement_NamedElement, gen_uml_ParameterableElement_Element, gen_uml_TemplateableElement_Element, gen_uml_BehavioredClassifier_Classifier, gen_uml_DirectedRelationship_Relationship, gen_uml_Relationship_Element, gen_uml_ConnectableElement_TypedElement, gen_uml_ConnectableElement_ParameterableElement, gen_uml_MultiplicityElement_Element, gen_uml_StructuralFeature_Feature, gen_uml_StructuralFeature_TypedElement, gen_uml_StructuralFeature_MultiplicityElement, gen_uml_DeploymentTarget_NamedElement, gen_uml_StructuredClassifier_Classifier, gen_uml_Element_EModelElement, gen_uml_EncapsulatedClassifier_StructuredClassifier, gen_uml_Namespace_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)