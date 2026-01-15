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
VisibilityEnum: Enumeration = Enumeration(
    name="VisibilityEnum",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private")
    }
)

# Classes
oml_Model = Class(name="oml::Model")
Package = Class(name="Package")
oml_PackageableElement = Class(name="oml::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
oml_Package = Class(name="oml::Package")
oml_AnnotatedElement = Class(name="oml::AnnotatedElement", is_abstract=True)
oml_Annotation = Class(name="oml::Annotation")
oml_Feature = Class(name="oml::Feature", is_abstract=True)
oml_Datatype = Class(name="oml::Datatype")
oml_NamedElement = Class(name="oml::NamedElement", is_abstract=True)
AnnotatedElement = Class(name="AnnotatedElement")
PackageableElement = Class(name="PackageableElement")
oml_Classifier = Class(name="oml::Classifier", is_abstract=True)
oml_ExternalClass = Class(name="oml::ExternalClass")
Class_ = Class(name="Class")
oml_Class = Class(name="oml::Class")
Classifier = Class(name="Classifier")
oml_Reference = Class(name="oml::Reference")
StructuralFeature = Class(name="StructuralFeature")
oml_Attribute = Class(name="oml::Attribute")
oml_StructuralFeature = Class(name="oml::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
oml_Operation = Class(name="oml::Operation")
oml_Parameter = Class(name="oml::Parameter")

# oml_Model class attributes and methods

# Package class attributes and methods

# oml_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# oml_Package class attributes and methods

# oml_AnnotatedElement class attributes and methods

# oml_Annotation class attributes and methods
oml_Annotation_key: Property = Property(name="key", type=StringType)
oml_Annotation_value: Property = Property(name="value", type=StringType)
oml_Annotation.attributes={oml_Annotation_key, oml_Annotation_value}

# oml_Feature class attributes and methods
oml_Feature_visibility: Property = Property(name="visibility", type=StringType)
oml_Feature.attributes={oml_Feature_visibility}

# oml_Datatype class attributes and methods

# oml_NamedElement class attributes and methods
oml_NamedElement_name: Property = Property(name="name", type=StringType)
oml_NamedElement.attributes={oml_NamedElement_name}

# AnnotatedElement class attributes and methods

# PackageableElement class attributes and methods

# oml_Classifier class attributes and methods

# oml_ExternalClass class attributes and methods

# Class class attributes and methods

# oml_Class class attributes and methods
oml_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
oml_Class.attributes={oml_Class_isAbstract}

# Classifier class attributes and methods

# oml_Reference class attributes and methods

# StructuralFeature class attributes and methods

# oml_Attribute class attributes and methods

# oml_StructuralFeature class attributes and methods
oml_StructuralFeature_isMany: Property = Property(name="isMany", type=StringType)
oml_StructuralFeature.attributes={oml_StructuralFeature_isMany}

# Feature class attributes and methods

# oml_Operation class attributes and methods

# oml_Parameter class attributes and methods

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="Package", type=oml_PackageableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=oml_Package, multiplicity=Multiplicity(0, 1))
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="oml_Annotation", type=oml_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="oml_AnnotatedElement", type=oml_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends4: BinaryAssociation = BinaryAssociation(
    name="extends4",
    ends={
        Property(name="Class", type=oml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedBy", type=oml_Class, multiplicity=Multiplicity(0, 1))
    }
)
extendedBy6: BinaryAssociation = BinaryAssociation(
    name="extendedBy6",
    ends={
        Property(name="Class7", type=oml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extends", type=oml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
features8: BinaryAssociation = BinaryAssociation(
    name="features8",
    ends={
        Property(name="Feature", type=oml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=oml_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Class10", type=oml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=oml_Class, multiplicity=Multiplicity(0, 1))
    }
)
contents2: BinaryAssociation = BinaryAssociation(
    name="contents2",
    ends={
        Property(name="PackageableElement", type=oml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=oml_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Operation", type=oml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=oml_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="oml_Classifier", type=oml_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="oml_Feature", type=oml_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
parameters12: BinaryAssociation = BinaryAssociation(
    name="parameters12",
    ends={
        Property(name="Parameter", type=oml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner13", type=oml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="oml_Classifier15", type=oml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="oml_Parameter", type=oml_Classifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_oml_Model_Package = Generalization(general=Package, specific=oml_Model)
gen_oml_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=oml_PackageableElement)
gen_oml_Datatype_Classifier = Generalization(general=Classifier, specific=oml_Datatype)
gen_oml_Feature_NamedElement = Generalization(general=NamedElement, specific=oml_Feature)
gen_oml_NamedElement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=oml_NamedElement)
gen_oml_Package_PackageableElement = Generalization(general=PackageableElement, specific=oml_Package)
gen_oml_Classifier_PackageableElement = Generalization(general=PackageableElement, specific=oml_Classifier)
gen_oml_ExternalClass_Class = Generalization(general=Class_, specific=oml_ExternalClass)
gen_oml_Class_Classifier = Generalization(general=Classifier, specific=oml_Class)
gen_oml_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=oml_Reference)
gen_oml_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=oml_Attribute)
gen_oml_StructuralFeature_Feature = Generalization(general=Feature, specific=oml_StructuralFeature)
gen_oml_Operation_Feature = Generalization(general=Feature, specific=oml_Operation)
gen_oml_Parameter_NamedElement = Generalization(general=NamedElement, specific=oml_Parameter)

# Domain Model
domain_model = DomainModel(
    name="oml",
    types={oml_Model, Package, oml_PackageableElement, NamedElement, oml_Package, oml_AnnotatedElement, oml_Annotation, oml_Feature, oml_Datatype, oml_NamedElement, AnnotatedElement, PackageableElement, oml_Classifier, oml_ExternalClass, Class_, oml_Class, Classifier, oml_Reference, StructuralFeature, oml_Attribute, oml_StructuralFeature, Feature, oml_Operation, oml_Parameter, VisibilityEnum},
    associations={package0, annotations1, extends4, extendedBy6, features8, owner9, contents2, owner16, type11, parameters12, type14},
    generalizations={gen_oml_Model_Package, gen_oml_PackageableElement_NamedElement, gen_oml_Datatype_Classifier, gen_oml_Feature_NamedElement, gen_oml_NamedElement_AnnotatedElement, gen_oml_Package_PackageableElement, gen_oml_Classifier_PackageableElement, gen_oml_ExternalClass_Class, gen_oml_Class_Classifier, gen_oml_Reference_StructuralFeature, gen_oml_Attribute_StructuralFeature, gen_oml_StructuralFeature_Feature, gen_oml_Operation_Feature, gen_oml_Parameter_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)