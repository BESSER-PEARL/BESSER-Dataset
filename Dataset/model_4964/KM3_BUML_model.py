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
km3_Enumeration = Class(name="km3::Enumeration")
EnumLiteral = Class(name="EnumLiteral")
km3_EnumLiteral = Class(name="km3::EnumLiteral")
Enumeration_ = Class(name="Enumeration")
km3_TemplateParameter = Class(name="km3::TemplateParameter")
km3_Class = Class(name="km3::Class")
TemplateParameter = Class(name="TemplateParameter")
Class_ = Class(name="Class")
km3_LocatedElement = Class(name="km3::LocatedElement", is_abstract=True)
km3_ModelElement = Class(name="km3::ModelElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
Package = Class(name="Package")
km3_Classifier = Class(name="km3::Classifier")
ModelElement = Class(name="ModelElement")
km3_DataType = Class(name="km3::DataType")
Classifier = Class(name="Classifier")
Reference = Class(name="Reference")
km3_Operation = Class(name="km3::Operation")
Parameter_ = Class(name="Parameter")
km3_Parameter = Class(name="km3::Parameter")
km3_Package = Class(name="km3::Package")
StructuralFeature = Class(name="StructuralFeature")
Operation = Class(name="Operation")
km3_TypedElement = Class(name="km3::TypedElement")
km3_StructuralFeature = Class(name="km3::StructuralFeature")
TypedElement = Class(name="TypedElement")
km3_Attribute = Class(name="km3::Attribute")
km3_Reference = Class(name="km3::Reference")
Metamodel = Class(name="Metamodel")
km3_Metamodel = Class(name="km3::Metamodel")

# km3_Enumeration class attributes and methods

# EnumLiteral class attributes and methods

# km3_EnumLiteral class attributes and methods

# Enumeration class attributes and methods

# km3_TemplateParameter class attributes and methods

# km3_Class class attributes and methods
km3_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
km3_Class.attributes={km3_Class_isAbstract}

# TemplateParameter class attributes and methods

# Class class attributes and methods

# km3_LocatedElement class attributes and methods
km3_LocatedElement_location: Property = Property(name="location", type=StringType)
km3_LocatedElement.attributes={km3_LocatedElement_location}

# km3_ModelElement class attributes and methods
km3_ModelElement_name: Property = Property(name="name", type=StringType)
km3_ModelElement.attributes={km3_ModelElement_name}

# LocatedElement class attributes and methods

# Package class attributes and methods

# km3_Classifier class attributes and methods

# ModelElement class attributes and methods

# km3_DataType class attributes and methods

# Classifier class attributes and methods

# Reference class attributes and methods

# km3_Operation class attributes and methods

# Parameter class attributes and methods

# km3_Parameter class attributes and methods

# km3_Package class attributes and methods

# StructuralFeature class attributes and methods

# Operation class attributes and methods

# km3_TypedElement class attributes and methods
km3_TypedElement_lower: Property = Property(name="lower", type=StringType)
km3_TypedElement_upper: Property = Property(name="upper", type=StringType)
km3_TypedElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
km3_TypedElement_isUnique: Property = Property(name="isUnique", type=StringType)
km3_TypedElement.attributes={km3_TypedElement_lower, km3_TypedElement_upper, km3_TypedElement_isUnique, km3_TypedElement_isOrdered}

# km3_StructuralFeature class attributes and methods

# TypedElement class attributes and methods

# km3_Attribute class attributes and methods

# km3_Reference class attributes and methods
km3_Reference_isContainer: Property = Property(name="isContainer", type=StringType)
km3_Reference.attributes={km3_Reference_isContainer}

# Metamodel class attributes and methods

# km3_Metamodel class attributes and methods

# Relationships
literals1: BinaryAssociation = BinaryAssociation(
    name="literals1",
    ends={
        Property(name="#3", type=km3_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=EnumLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
enum4: BinaryAssociation = BinaryAssociation(
    name="enum4",
    ends={
        Property(name="#6", type=km3_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
parameters7: BinaryAssociation = BinaryAssociation(
    name="parameters7",
    ends={
        Property(name="TemplateParameter", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Class", type=TemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="#", type=km3_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
opposite26: BinaryAssociation = BinaryAssociation(
    name="opposite26",
    ends={
        Property(name="Reference", type=km3_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Reference", type=Reference, multiplicity=Multiplicity(0, 1))
    }
)
owner27: BinaryAssociation = BinaryAssociation(
    name="owner27",
    ends={
        Property(name="#29", type=km3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="028", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="#32", type=km3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="031", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
owner33: BinaryAssociation = BinaryAssociation(
    name="owner33",
    ends={
        Property(name="#35", type=km3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="034", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
supertypes8: BinaryAssociation = BinaryAssociation(
    name="supertypes8",
    ends={
        Property(name="Class", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Class9", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeatures10: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures10",
    ends={
        Property(name="#12", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations13: BinaryAssociation = BinaryAssociation(
    name="operations13",
    ends={
        Property(name="#15", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="Classifier", type=km3_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_TypedElement", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner17: BinaryAssociation = BinaryAssociation(
    name="owner17",
    ends={
        Property(name="#19", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="018", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
subsetOf20: BinaryAssociation = BinaryAssociation(
    name="subsetOf20",
    ends={
        Property(name="#22", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="021", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
derivedFrom23: BinaryAssociation = BinaryAssociation(
    name="derivedFrom23",
    ends={
        Property(name="#25", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="024", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
contents36: BinaryAssociation = BinaryAssociation(
    name="contents36",
    ends={
        Property(name="#38", type=km3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="037", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel39: BinaryAssociation = BinaryAssociation(
    name="metamodel39",
    ends={
        Property(name="#41", type=km3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="040", type=Metamodel, multiplicity=Multiplicity(0, 1))
    }
)
contents42: BinaryAssociation = BinaryAssociation(
    name="contents42",
    ends={
        Property(name="#44", type=km3_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="043", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_km3_Enumeration_Classifier = Generalization(general=Classifier, specific=km3_Enumeration)
gen_km3_EnumLiteral_ModelElement = Generalization(general=ModelElement, specific=km3_EnumLiteral)
gen_km3_TemplateParameter_Classifier = Generalization(general=Classifier, specific=km3_TemplateParameter)
gen_km3_Class_Classifier = Generalization(general=Classifier, specific=km3_Class)
gen_km3_ModelElement_LocatedElement = Generalization(general=LocatedElement, specific=km3_ModelElement)
gen_km3_Classifier_ModelElement = Generalization(general=ModelElement, specific=km3_Classifier)
gen_km3_DataType_Classifier = Generalization(general=Classifier, specific=km3_DataType)
gen_km3_Operation_TypedElement = Generalization(general=TypedElement, specific=km3_Operation)
gen_km3_Parameter_TypedElement = Generalization(general=TypedElement, specific=km3_Parameter)
gen_km3_Package_ModelElement = Generalization(general=ModelElement, specific=km3_Package)
gen_km3_TypedElement_ModelElement = Generalization(general=ModelElement, specific=km3_TypedElement)
gen_km3_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=km3_StructuralFeature)
gen_km3_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=km3_Attribute)
gen_km3_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=km3_Reference)
gen_km3_Metamodel_LocatedElement = Generalization(general=LocatedElement, specific=km3_Metamodel)

# Domain Model
domain_model = DomainModel(
    name="primitives",
    types={km3_Enumeration, EnumLiteral, km3_EnumLiteral, Enumeration_, km3_TemplateParameter, km3_Class, TemplateParameter, Class_, km3_LocatedElement, km3_ModelElement, LocatedElement, Package, km3_Classifier, ModelElement, km3_DataType, Classifier, Reference, km3_Operation, Parameter_, km3_Parameter, km3_Package, StructuralFeature, Operation, km3_TypedElement, km3_StructuralFeature, TypedElement, km3_Attribute, km3_Reference, Metamodel, km3_Metamodel},
    associations={literals1, enum4, parameters7, package0, opposite26, owner27, parameters30, owner33, supertypes8, structuralFeatures10, operations13, type16, owner17, subsetOf20, derivedFrom23, contents36, metamodel39, contents42},
    generalizations={gen_km3_Enumeration_Classifier, gen_km3_EnumLiteral_ModelElement, gen_km3_TemplateParameter_Classifier, gen_km3_Class_Classifier, gen_km3_ModelElement_LocatedElement, gen_km3_Classifier_ModelElement, gen_km3_DataType_Classifier, gen_km3_Operation_TypedElement, gen_km3_Parameter_TypedElement, gen_km3_Package_ModelElement, gen_km3_TypedElement_ModelElement, gen_km3_StructuralFeature_TypedElement, gen_km3_Attribute_StructuralFeature, gen_km3_Reference_StructuralFeature, gen_km3_Metamodel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)