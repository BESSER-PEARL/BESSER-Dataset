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
km3_LocatedElement = Class(name="km3_LocatedElement", is_abstract=True)
km3_ModelElement = Class(name="km3_ModelElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
Package = Class(name="Package")
km3_Classifier = Class(name="km3_Classifier")
ModelElement = Class(name="ModelElement")
km3_DataType = Class(name="km3_DataType")
Classifier = Class(name="Classifier")
km3_Enumeration = Class(name="km3_Enumeration")
EnumLiteral = Class(name="EnumLiteral")
km3_EnumLiteral = Class(name="km3_EnumLiteral")
Enumeration_ = Class(name="Enumeration")
km3_TemplateParameter = Class(name="km3_TemplateParameter")
km3_Class = Class(name="km3_Class")
TemplateParameter = Class(name="TemplateParameter")
Class_ = Class(name="Class")
StructuralFeature = Class(name="StructuralFeature")
Metamodel = Class(name="Metamodel")
Operation = Class(name="Operation")
km3_TypedElement = Class(name="km3_TypedElement")
km3_StructuralFeature = Class(name="km3_StructuralFeature")
TypedElement = Class(name="TypedElement")
km3_Attribute = Class(name="km3_Attribute")
km3_Reference = Class(name="km3_Reference")
Reference = Class(name="Reference")
km3_Operation = Class(name="km3_Operation")
Parameter_ = Class(name="Parameter")
km3_Parameter = Class(name="km3_Parameter")
km3_Package = Class(name="km3_Package")
km3_Metamodel = Class(name="km3_Metamodel")

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

# StructuralFeature class attributes and methods

# Metamodel class attributes and methods

# Operation class attributes and methods

# km3_TypedElement class attributes and methods
km3_TypedElement_lower: Property = Property(name="lower", type=StringType)
km3_TypedElement_upper: Property = Property(name="upper", type=StringType)
km3_TypedElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
km3_TypedElement_isUnique: Property = Property(name="isUnique", type=StringType)
km3_TypedElement.attributes={km3_TypedElement_isOrdered, km3_TypedElement_upper, km3_TypedElement_lower, km3_TypedElement_isUnique}

# km3_StructuralFeature class attributes and methods

# TypedElement class attributes and methods

# km3_Attribute class attributes and methods

# km3_Reference class attributes and methods
km3_Reference_isContainer: Property = Property(name="isContainer", type=StringType)
km3_Reference.attributes={km3_Reference_isContainer}

# Reference class attributes and methods

# km3_Operation class attributes and methods

# Parameter class attributes and methods

# km3_Parameter class attributes and methods

# km3_Package class attributes and methods

# km3_Metamodel class attributes and methods

# Relationships
structuralFeatures6: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures6",
    ends={
        Property(name="StructuralFeature", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="Package", type=km3_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
literals1: BinaryAssociation = BinaryAssociation(
    name="literals1",
    ends={
        Property(name="EnumLiteral", type=km3_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=EnumLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
enum2: BinaryAssociation = BinaryAssociation(
    name="enum2",
    ends={
        Property(name="Enumeration", type=km3_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="TemplateParameter", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Class", type=TemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
supertypes4: BinaryAssociation = BinaryAssociation(
    name="supertypes4",
    ends={
        Property(name="Class", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Class5", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel24: BinaryAssociation = BinaryAssociation(
    name="metamodel24",
    ends={
        Property(name="Metamodel", type=km3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="contents25", type=Metamodel, multiplicity=Multiplicity(0, 1))
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="Operation", type=km3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner8", type=Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="Classifier", type=km3_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_TypedElement", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Class11", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="structuralFeatures", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
subsetOf12: BinaryAssociation = BinaryAssociation(
    name="subsetOf12",
    ends={
        Property(name="StructuralFeature13", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedFrom", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
derivedFrom14: BinaryAssociation = BinaryAssociation(
    name="derivedFrom14",
    ends={
        Property(name="StructuralFeature15", type=km3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetOf", type=StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
opposite16: BinaryAssociation = BinaryAssociation(
    name="opposite16",
    ends={
        Property(name="Reference", type=km3_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="km3_Reference", type=Reference, multiplicity=Multiplicity(0, 1))
    }
)
owner17: BinaryAssociation = BinaryAssociation(
    name="owner17",
    ends={
        Property(name="Class18", type=km3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
parameters19: BinaryAssociation = BinaryAssociation(
    name="parameters19",
    ends={
        Property(name="Parameter", type=km3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner20", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
owner21: BinaryAssociation = BinaryAssociation(
    name="owner21",
    ends={
        Property(name="Operation22", type=km3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
contents23: BinaryAssociation = BinaryAssociation(
    name="contents23",
    ends={
        Property(name="ModelElement", type=km3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents26: BinaryAssociation = BinaryAssociation(
    name="contents26",
    ends={
        Property(name="Package27", type=km3_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_km3_ModelElement_LocatedElement = Generalization(general=LocatedElement, specific=km3_ModelElement)
gen_km3_Classifier_ModelElement = Generalization(general=ModelElement, specific=km3_Classifier)
gen_km3_DataType_Classifier = Generalization(general=Classifier, specific=km3_DataType)
gen_km3_Enumeration_Classifier = Generalization(general=Classifier, specific=km3_Enumeration)
gen_km3_EnumLiteral_ModelElement = Generalization(general=ModelElement, specific=km3_EnumLiteral)
gen_km3_TemplateParameter_Classifier = Generalization(general=Classifier, specific=km3_TemplateParameter)
gen_km3_Class_Classifier = Generalization(general=Classifier, specific=km3_Class)
gen_km3_TypedElement_ModelElement = Generalization(general=ModelElement, specific=km3_TypedElement)
gen_km3_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=km3_StructuralFeature)
gen_km3_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=km3_Attribute)
gen_km3_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=km3_Reference)
gen_km3_Operation_TypedElement = Generalization(general=TypedElement, specific=km3_Operation)
gen_km3_Parameter_TypedElement = Generalization(general=TypedElement, specific=km3_Parameter)
gen_km3_Package_ModelElement = Generalization(general=ModelElement, specific=km3_Package)
gen_km3_Metamodel_LocatedElement = Generalization(general=LocatedElement, specific=km3_Metamodel)

# Domain Model
domain_model = DomainModel(
    name="primitives",
    types={km3_LocatedElement, km3_ModelElement, LocatedElement, Package, km3_Classifier, ModelElement, km3_DataType, Classifier, km3_Enumeration, EnumLiteral, km3_EnumLiteral, Enumeration_, km3_TemplateParameter, km3_Class, TemplateParameter, Class_, StructuralFeature, Metamodel, Operation, km3_TypedElement, km3_StructuralFeature, TypedElement, km3_Attribute, km3_Reference, Reference, km3_Operation, Parameter_, km3_Parameter, km3_Package, km3_Metamodel},
    associations={structuralFeatures6, package0, literals1, enum2, parameters3, supertypes4, metamodel24, operations7, type9, owner10, subsetOf12, derivedFrom14, opposite16, owner17, parameters19, owner21, contents23, contents26},
    generalizations={gen_km3_ModelElement_LocatedElement, gen_km3_Classifier_ModelElement, gen_km3_DataType_Classifier, gen_km3_Enumeration_Classifier, gen_km3_EnumLiteral_ModelElement, gen_km3_TemplateParameter_Classifier, gen_km3_Class_Classifier, gen_km3_TypedElement_ModelElement, gen_km3_StructuralFeature_TypedElement, gen_km3_Attribute_StructuralFeature, gen_km3_Reference_StructuralFeature, gen_km3_Operation_TypedElement, gen_km3_Parameter_TypedElement, gen_km3_Package_ModelElement, gen_km3_Metamodel_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)