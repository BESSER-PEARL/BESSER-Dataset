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
KM3_ModelElement = Class(name="KM3::ModelElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
KM3_Package = Class(name="KM3::Package")
KM3_Classifier = Class(name="KM3::Classifier")
ModelElement = Class(name="ModelElement")
KM3_DataType = Class(name="KM3::DataType")
Classifier = Class(name="Classifier")
KM3_Enumeration = Class(name="KM3::Enumeration")
KM3_EnumLiteral = Class(name="KM3::EnumLiteral")
KM3_Class = Class(name="KM3::Class")
KM3_StructuralFeature = Class(name="KM3::StructuralFeature")
KM3_LocatedElement = Class(name="KM3::LocatedElement", is_abstract=True)
KM3_Attribute = Class(name="KM3::Attribute")
StructuralFeature = Class(name="StructuralFeature")
KM3_Reference = Class(name="KM3::Reference")
KM3_Parameter = Class(name="KM3::Parameter")
KM3_Metamodel = Class(name="KM3::Metamodel")
KM3_Operation = Class(name="KM3::Operation")
KM3_TypedElement = Class(name="KM3::TypedElement")
TypedElement = Class(name="TypedElement")

# KM3_ModelElement class attributes and methods
KM3_ModelElement_name: Property = Property(name="name", type=StringType)
KM3_ModelElement.attributes={KM3_ModelElement_name}

# LocatedElement class attributes and methods

# KM3_Package class attributes and methods

# KM3_Classifier class attributes and methods

# ModelElement class attributes and methods

# KM3_DataType class attributes and methods

# Classifier class attributes and methods

# KM3_Enumeration class attributes and methods

# KM3_EnumLiteral class attributes and methods

# KM3_Class class attributes and methods
KM3_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
KM3_Class.attributes={KM3_Class_isAbstract}

# KM3_StructuralFeature class attributes and methods

# KM3_LocatedElement class attributes and methods
KM3_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
KM3_LocatedElement_location: Property = Property(name="location", type=StringType)
KM3_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
KM3_LocatedElement.attributes={KM3_LocatedElement_commentsAfter, KM3_LocatedElement_location, KM3_LocatedElement_commentsBefore}

# KM3_Attribute class attributes and methods

# StructuralFeature class attributes and methods

# KM3_Reference class attributes and methods
KM3_Reference_isContainer: Property = Property(name="isContainer", type=BooleanType)
KM3_Reference.attributes={KM3_Reference_isContainer}

# KM3_Parameter class attributes and methods

# KM3_Metamodel class attributes and methods

# KM3_Operation class attributes and methods

# KM3_TypedElement class attributes and methods
KM3_TypedElement_lower: Property = Property(name="lower", type=IntegerType)
KM3_TypedElement_upper: Property = Property(name="upper", type=IntegerType)
KM3_TypedElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
KM3_TypedElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
KM3_TypedElement.attributes={KM3_TypedElement_isOrdered, KM3_TypedElement_isUnique, KM3_TypedElement_lower, KM3_TypedElement_upper}

# TypedElement class attributes and methods

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="KM3_Package", type=KM3_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_ModelElement", type=KM3_Package, multiplicity=Multiplicity(1, 1))
    }
)
literals1: BinaryAssociation = BinaryAssociation(
    name="literals1",
    ends={
        Property(name="EnumLiteral", type=KM3_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=KM3_EnumLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
enum2: BinaryAssociation = BinaryAssociation(
    name="enum2",
    ends={
        Property(name="Enumeration", type=KM3_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=KM3_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
supertypes4: BinaryAssociation = BinaryAssociation(
    name="supertypes4",
    ends={
        Property(name="KM3_Class", type=KM3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Class3", type=KM3_Class, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeatures5: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures5",
    ends={
        Property(name="StructuralFeature", type=KM3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=KM3_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derivedFrom14: BinaryAssociation = BinaryAssociation(
    name="derivedFrom14",
    ends={
        Property(name="StructuralFeature15", type=KM3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetOf", type=KM3_StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
opposite17: BinaryAssociation = BinaryAssociation(
    name="opposite17",
    ends={
        Property(name="KM3_Reference", type=KM3_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Reference16", type=KM3_Reference, multiplicity=Multiplicity(0, 1))
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="Class19", type=KM3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=KM3_Class, multiplicity=Multiplicity(1, 1))
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="Parameter", type=KM3_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=KM3_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
owner22: BinaryAssociation = BinaryAssociation(
    name="owner22",
    ends={
        Property(name="Operation23", type=KM3_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=KM3_Operation, multiplicity=Multiplicity(1, 1))
    }
)
contents24: BinaryAssociation = BinaryAssociation(
    name="contents24",
    ends={
        Property(name="KM3_ModelElement26", type=KM3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Package25", type=KM3_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel27: BinaryAssociation = BinaryAssociation(
    name="metamodel27",
    ends={
        Property(name="Metamodel", type=KM3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=KM3_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
operations6: BinaryAssociation = BinaryAssociation(
    name="operations6",
    ends={
        Property(name="Operation", type=KM3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner7", type=KM3_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="KM3_Classifier", type=KM3_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_TypedElement", type=KM3_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Class", type=KM3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="structuralFeatures", type=KM3_Class, multiplicity=Multiplicity(1, 1))
    }
)
subsetOf11: BinaryAssociation = BinaryAssociation(
    name="subsetOf11",
    ends={
        Property(name="StructuralFeature12", type=KM3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedFrom", type=KM3_StructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
contents28: BinaryAssociation = BinaryAssociation(
    name="contents28",
    ends={
        Property(name="Package", type=KM3_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=KM3_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_KM3_ModelElement_LocatedElement = Generalization(general=LocatedElement, specific=KM3_ModelElement)
gen_KM3_Classifier_ModelElement = Generalization(general=ModelElement, specific=KM3_Classifier)
gen_KM3_DataType_Classifier = Generalization(general=Classifier, specific=KM3_DataType)
gen_KM3_Enumeration_Classifier = Generalization(general=Classifier, specific=KM3_Enumeration)
gen_KM3_EnumLiteral_ModelElement = Generalization(general=ModelElement, specific=KM3_EnumLiteral)
gen_KM3_Class_Classifier = Generalization(general=Classifier, specific=KM3_Class)
gen_KM3_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=KM3_Attribute)
gen_KM3_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=KM3_Reference)
gen_KM3_Operation_TypedElement = Generalization(general=TypedElement, specific=KM3_Operation)
gen_KM3_Parameter_TypedElement = Generalization(general=TypedElement, specific=KM3_Parameter)
gen_KM3_Package_ModelElement = Generalization(general=ModelElement, specific=KM3_Package)
gen_KM3_Metamodel_LocatedElement = Generalization(general=LocatedElement, specific=KM3_Metamodel)
gen_KM3_TypedElement_ModelElement = Generalization(general=ModelElement, specific=KM3_TypedElement)
gen_KM3_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=KM3_StructuralFeature)

# Domain Model
domain_model = DomainModel(
    name="KM3",
    types={KM3_ModelElement, LocatedElement, KM3_Package, KM3_Classifier, ModelElement, KM3_DataType, Classifier, KM3_Enumeration, KM3_EnumLiteral, KM3_Class, KM3_StructuralFeature, KM3_LocatedElement, KM3_Attribute, StructuralFeature, KM3_Reference, KM3_Parameter, KM3_Metamodel, KM3_Operation, KM3_TypedElement, TypedElement},
    associations={package0, literals1, enum2, supertypes4, structuralFeatures5, derivedFrom14, opposite17, owner18, parameters20, owner22, contents24, metamodel27, operations6, type8, owner9, subsetOf11, contents28},
    generalizations={gen_KM3_ModelElement_LocatedElement, gen_KM3_Classifier_ModelElement, gen_KM3_DataType_Classifier, gen_KM3_Enumeration_Classifier, gen_KM3_EnumLiteral_ModelElement, gen_KM3_Class_Classifier, gen_KM3_Attribute_StructuralFeature, gen_KM3_Reference_StructuralFeature, gen_KM3_Operation_TypedElement, gen_KM3_Parameter_TypedElement, gen_KM3_Package_ModelElement, gen_KM3_Metamodel_LocatedElement, gen_KM3_TypedElement_ModelElement, gen_KM3_StructuralFeature_TypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)