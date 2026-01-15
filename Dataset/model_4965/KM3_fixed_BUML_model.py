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
KM3_LocatedElement = Class(name="KM3::LocatedElement", is_abstract=True)
KM3_ModelElement = Class(name="KM3::ModelElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
KM3_Package = Class(name="KM3::Package")
KM3_Metamodel = Class(name="KM3::Metamodel")
KM3_Classifier = Class(name="KM3::Classifier")
ModelElement = Class(name="ModelElement")
KM3_DataType = Class(name="KM3::DataType")
Classifier = Class(name="Classifier")
KM3_Enumeration = Class(name="KM3::Enumeration")
KM3_EnumLiteral = Class(name="KM3::EnumLiteral")
KM3_Class = Class(name="KM3::Class")
KM3_StructuralFeature = Class(name="KM3::StructuralFeature")
KM3_Attribute = Class(name="KM3::Attribute")
StructuralFeature = Class(name="StructuralFeature")
KM3_Reference = Class(name="KM3::Reference")

# KM3_LocatedElement class attributes and methods
KM3_LocatedElement_location: Property = Property(name="location", type=StringType)
KM3_LocatedElement.attributes={KM3_LocatedElement_location}

# KM3_ModelElement class attributes and methods
KM3_ModelElement_name: Property = Property(name="name", type=StringType)
KM3_ModelElement.attributes={KM3_ModelElement_name}

# LocatedElement class attributes and methods

# KM3_Package class attributes and methods

# KM3_Metamodel class attributes and methods

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
KM3_StructuralFeature_lower: Property = Property(name="lower", type=IntegerType)
KM3_StructuralFeature_upper: Property = Property(name="upper", type=IntegerType)
KM3_StructuralFeature_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
KM3_StructuralFeature_isUnique: Property = Property(name="isUnique", type=BooleanType)
KM3_StructuralFeature.attributes={KM3_StructuralFeature_lower, KM3_StructuralFeature_isUnique, KM3_StructuralFeature_isOrdered, KM3_StructuralFeature_upper}

# KM3_Attribute class attributes and methods

# StructuralFeature class attributes and methods

# KM3_Reference class attributes and methods
KM3_Reference_isContainer: Property = Property(name="isContainer", type=BooleanType)
KM3_Reference.attributes={KM3_Reference_isContainer}

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="Package", type=KM3_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=KM3_Package, multiplicity=Multiplicity(0, 1))
    }
)
opposite8: BinaryAssociation = BinaryAssociation(
    name="opposite8",
    ends={
        Property(name="KM3_Reference", type=KM3_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Reference7", type=KM3_Reference, multiplicity=Multiplicity(0, 1))
    }
)
contents9: BinaryAssociation = BinaryAssociation(
    name="contents9",
    ends={
        Property(name="ModelElement", type=KM3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=KM3_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel10: BinaryAssociation = BinaryAssociation(
    name="metamodel10",
    ends={
        Property(name="Metamodel", type=KM3_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="contents11", type=KM3_Metamodel, multiplicity=Multiplicity(1, 1))
    }
)
contents12: BinaryAssociation = BinaryAssociation(
    name="contents12",
    ends={
        Property(name="Package13", type=KM3_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel", type=KM3_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals1: BinaryAssociation = BinaryAssociation(
    name="literals1",
    ends={
        Property(name="KM3_EnumLiteral", type=KM3_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Enumeration", type=KM3_EnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypes3: BinaryAssociation = BinaryAssociation(
    name="supertypes3",
    ends={
        Property(name="KM3_Class", type=KM3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_Class2", type=KM3_Class, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeatures4: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures4",
    ends={
        Property(name="StructuralFeature", type=KM3_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=KM3_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Class", type=KM3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="structuralFeatures", type=KM3_Class, multiplicity=Multiplicity(1, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="KM3_Classifier", type=KM3_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="KM3_StructuralFeature", type=KM3_Classifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_KM3_ModelElement_LocatedElement = Generalization(general=LocatedElement, specific=KM3_ModelElement)
gen_KM3_Package_ModelElement = Generalization(general=ModelElement, specific=KM3_Package)
gen_KM3_Metamodel_LocatedElement = Generalization(general=LocatedElement, specific=KM3_Metamodel)
gen_KM3_Classifier_ModelElement = Generalization(general=ModelElement, specific=KM3_Classifier)
gen_KM3_DataType_Classifier = Generalization(general=Classifier, specific=KM3_DataType)
gen_KM3_Enumeration_Classifier = Generalization(general=Classifier, specific=KM3_Enumeration)
gen_KM3_EnumLiteral_ModelElement = Generalization(general=ModelElement, specific=KM3_EnumLiteral)
gen_KM3_Class_Classifier = Generalization(general=Classifier, specific=KM3_Class)
gen_KM3_StructuralFeature_ModelElement = Generalization(general=ModelElement, specific=KM3_StructuralFeature)
gen_KM3_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=KM3_Attribute)
gen_KM3_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=KM3_Reference)

# Domain Model
domain_model = DomainModel(
    name="KM3",
    types={KM3_LocatedElement, KM3_ModelElement, LocatedElement, KM3_Package, KM3_Metamodel, KM3_Classifier, ModelElement, KM3_DataType, Classifier, KM3_Enumeration, KM3_EnumLiteral, KM3_Class, KM3_StructuralFeature, KM3_Attribute, StructuralFeature, KM3_Reference},
    associations={package0, opposite8, contents9, metamodel10, contents12, literals1, supertypes3, structuralFeatures4, owner5, type6},
    generalizations={gen_KM3_ModelElement_LocatedElement, gen_KM3_Package_ModelElement, gen_KM3_Metamodel_LocatedElement, gen_KM3_Classifier_ModelElement, gen_KM3_DataType_Classifier, gen_KM3_Enumeration_Classifier, gen_KM3_EnumLiteral_ModelElement, gen_KM3_Class_Classifier, gen_KM3_StructuralFeature_ModelElement, gen_KM3_Attribute_StructuralFeature, gen_KM3_Reference_StructuralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)