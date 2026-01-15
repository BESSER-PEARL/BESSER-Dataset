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
OO_Model = Class(name="OO::Model")
Package = Class(name="Package")
OO_PackageableElement = Class(name="OO::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
OO_Package = Class(name="OO::Package")
OO_AnnotatedElement = Class(name="OO::AnnotatedElement", is_abstract=True)
OO_Annotation = Class(name="OO::Annotation")
OO_NamedElement = Class(name="OO::NamedElement", is_abstract=True)
AnnotatedElement = Class(name="AnnotatedElement")
PackageableElement = Class(name="PackageableElement")
OO_Classifier = Class(name="OO::Classifier", is_abstract=True)
OO_ExternalClass = Class(name="OO::ExternalClass")
Class_ = Class(name="Class")
OO_Class = Class(name="OO::Class")
Classifier = Class(name="Classifier")
OO_Feature = Class(name="OO::Feature", is_abstract=True)
OO_Datatype = Class(name="OO::Datatype")
OO_StructuralFeature = Class(name="OO::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
OO_Operation = Class(name="OO::Operation")
OO_Parameter = Class(name="OO::Parameter")
OO_Reference = Class(name="OO::Reference")
StructuralFeature = Class(name="StructuralFeature")
OO_Attribute = Class(name="OO::Attribute")

# OO_Model class attributes and methods

# Package class attributes and methods

# OO_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# OO_Package class attributes and methods

# OO_AnnotatedElement class attributes and methods

# OO_Annotation class attributes and methods
OO_Annotation_key: Property = Property(name="key", type=StringType)
OO_Annotation_value: Property = Property(name="value", type=StringType)
OO_Annotation.attributes={OO_Annotation_value, OO_Annotation_key}

# OO_NamedElement class attributes and methods
OO_NamedElement_name: Property = Property(name="name", type=StringType)
OO_NamedElement.attributes={OO_NamedElement_name}

# AnnotatedElement class attributes and methods

# PackageableElement class attributes and methods

# OO_Classifier class attributes and methods

# OO_ExternalClass class attributes and methods

# Class class attributes and methods

# OO_Class class attributes and methods
OO_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
OO_Class.attributes={OO_Class_isAbstract}

# Classifier class attributes and methods

# OO_Feature class attributes and methods
OO_Feature_visibility: Property = Property(name="visibility", type=StringType)
OO_Feature.attributes={OO_Feature_visibility}

# OO_Datatype class attributes and methods

# OO_StructuralFeature class attributes and methods
OO_StructuralFeature_isMany: Property = Property(name="isMany", type=StringType)
OO_StructuralFeature.attributes={OO_StructuralFeature_isMany}

# Feature class attributes and methods

# OO_Operation class attributes and methods

# OO_Parameter class attributes and methods

# OO_Reference class attributes and methods

# StructuralFeature class attributes and methods

# OO_Attribute class attributes and methods

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="Package", type=OO_PackageableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=OO_Package, multiplicity=Multiplicity(0, 1))
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="OO_Annotation", type=OO_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_AnnotatedElement", type=OO_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents2: BinaryAssociation = BinaryAssociation(
    name="contents2",
    ends={
        Property(name="PackageableElement", type=OO_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=OO_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends4: BinaryAssociation = BinaryAssociation(
    name="extends4",
    ends={
        Property(name="Class", type=OO_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedBy", type=OO_Class, multiplicity=Multiplicity(0, 1))
    }
)
extendedBy6: BinaryAssociation = BinaryAssociation(
    name="extendedBy6",
    ends={
        Property(name="Class7", type=OO_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="extends", type=OO_Class, multiplicity=Multiplicity(0, 9999))
    }
)
features8: BinaryAssociation = BinaryAssociation(
    name="features8",
    ends={
        Property(name="Feature", type=OO_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=OO_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Class10", type=OO_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=OO_Class, multiplicity=Multiplicity(0, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="OO_Classifier", type=OO_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_Feature", type=OO_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
parameters12: BinaryAssociation = BinaryAssociation(
    name="parameters12",
    ends={
        Property(name="Parameter", type=OO_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner13", type=OO_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="OO_Classifier15", type=OO_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OO_Parameter", type=OO_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Operation", type=OO_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=OO_Operation, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_OO_Model_Package = Generalization(general=Package, specific=OO_Model)
gen_OO_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=OO_PackageableElement)
gen_OO_NamedElement_AnnotatedElement = Generalization(general=AnnotatedElement, specific=OO_NamedElement)
gen_OO_Package_PackageableElement = Generalization(general=PackageableElement, specific=OO_Package)
gen_OO_Classifier_PackageableElement = Generalization(general=PackageableElement, specific=OO_Classifier)
gen_OO_ExternalClass_Class = Generalization(general=Class_, specific=OO_ExternalClass)
gen_OO_Class_Classifier = Generalization(general=Classifier, specific=OO_Class)
gen_OO_Datatype_Classifier = Generalization(general=Classifier, specific=OO_Datatype)
gen_OO_Feature_NamedElement = Generalization(general=NamedElement, specific=OO_Feature)
gen_OO_StructuralFeature_Feature = Generalization(general=Feature, specific=OO_StructuralFeature)
gen_OO_Operation_Feature = Generalization(general=Feature, specific=OO_Operation)
gen_OO_Parameter_NamedElement = Generalization(general=NamedElement, specific=OO_Parameter)
gen_OO_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=OO_Reference)
gen_OO_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=OO_Attribute)

# Domain Model
domain_model = DomainModel(
    name="OO",
    types={OO_Model, Package, OO_PackageableElement, NamedElement, OO_Package, OO_AnnotatedElement, OO_Annotation, OO_NamedElement, AnnotatedElement, PackageableElement, OO_Classifier, OO_ExternalClass, Class_, OO_Class, Classifier, OO_Feature, OO_Datatype, OO_StructuralFeature, Feature, OO_Operation, OO_Parameter, OO_Reference, StructuralFeature, OO_Attribute, VisibilityEnum},
    associations={package0, annotations1, contents2, extends4, extendedBy6, features8, owner9, type11, parameters12, type14, owner16},
    generalizations={gen_OO_Model_Package, gen_OO_PackageableElement_NamedElement, gen_OO_NamedElement_AnnotatedElement, gen_OO_Package_PackageableElement, gen_OO_Classifier_PackageableElement, gen_OO_ExternalClass_Class, gen_OO_Class_Classifier, gen_OO_Datatype_Classifier, gen_OO_Feature_NamedElement, gen_OO_StructuralFeature_Feature, gen_OO_Operation_Feature, gen_OO_Parameter_NamedElement, gen_OO_Reference_StructuralFeature, gen_OO_Attribute_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)