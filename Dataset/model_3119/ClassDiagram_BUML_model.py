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
ClassDiagram_Classifier = Class(name="ClassDiagram::Classifier", is_abstract=True)
Package = Class(name="Package")
ClassDiagram_NamedElement = Class(name="ClassDiagram::NamedElement", is_abstract=True)
ClassDiagram_Package = Class(name="ClassDiagram::Package")
NamedElement = Class(name="NamedElement")
Classifier = Class(name="Classifier")
ClassDiagram_DataType = Class(name="ClassDiagram::DataType")
ClassDiagram_Class = Class(name="ClassDiagram::Class")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")
ClassDiagram_Attribute = Class(name="ClassDiagram::Attribute")
ClassDiagram_System = Class(name="ClassDiagram::System")

# ClassDiagram_Classifier class attributes and methods

# Package class attributes and methods

# ClassDiagram_NamedElement class attributes and methods
ClassDiagram_NamedElement_name: Property = Property(name="name", type=StringType)
ClassDiagram_NamedElement.attributes={ClassDiagram_NamedElement_name}

# ClassDiagram_Package class attributes and methods

# NamedElement class attributes and methods

# Classifier class attributes and methods

# ClassDiagram_DataType class attributes and methods

# ClassDiagram_Class class attributes and methods
ClassDiagram_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
ClassDiagram_Class.attributes={ClassDiagram_Class_isAbstract}

# Class class attributes and methods

# Attribute class attributes and methods

# ClassDiagram_Attribute class attributes and methods
ClassDiagram_Attribute_multiValued: Property = Property(name="multiValued", type=StringType)
ClassDiagram_Attribute.attributes={ClassDiagram_Attribute_multiValued}

# ClassDiagram_System class attributes and methods

# Relationships
ownedElement0: BinaryAssociation = BinaryAssociation(
    name="ownedElement0",
    ends={
        Property(name="#", type=ClassDiagram_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="#3", type=ClassDiagram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
super4: BinaryAssociation = BinaryAssociation(
    name="super4",
    ends={
        Property(name="Class", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
attr5: BinaryAssociation = BinaryAssociation(
    name="attr5",
    ends={
        Property(name="#7", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="Classifier", type=ClassDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
packages12: BinaryAssociation = BinaryAssociation(
    name="packages12",
    ends={
        Property(name="Package", type=ClassDiagram_System, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_System", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="#11", type=ClassDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="010", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ClassDiagram_Classifier_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Classifier)
gen_ClassDiagram_Package_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Package)
gen_ClassDiagram_DataType_Classifier = Generalization(general=Classifier, specific=ClassDiagram_DataType)
gen_ClassDiagram_Class_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Class)
gen_ClassDiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Attribute)
gen_ClassDiagram_System_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_System)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ClassDiagram_Classifier, Package, ClassDiagram_NamedElement, ClassDiagram_Package, NamedElement, Classifier, ClassDiagram_DataType, ClassDiagram_Class, Class_, Attribute, ClassDiagram_Attribute, ClassDiagram_System},
    associations={ownedElement0, owner1, super4, attr5, type8, packages12, owner9},
    generalizations={gen_ClassDiagram_Classifier_NamedElement, gen_ClassDiagram_Package_NamedElement, gen_ClassDiagram_DataType_Classifier, gen_ClassDiagram_Class_Classifier, gen_ClassDiagram_Attribute_NamedElement, gen_ClassDiagram_System_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)