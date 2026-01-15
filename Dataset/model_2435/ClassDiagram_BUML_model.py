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
ClassDiagram_NamedElement = Class(name="ClassDiagram::NamedElement", is_abstract=True)
ClassDiagram_Classifier = Class(name="ClassDiagram::Classifier", is_abstract=True)
NamedElement = Class(name="NamedElement")
ClassDiagram_DataType = Class(name="ClassDiagram::DataType")
Classifier = Class(name="Classifier")
ClassDiagram_Class = Class(name="ClassDiagram::Class")
Class_ = Class(name="Class")
Attribute = Class(name="Attribute")
ClassDiagram_Attribute = Class(name="ClassDiagram::Attribute")
ClassDiagram_Named = Class(name="ClassDiagram::Named", is_abstract=True)
ClassDiagram_Table = Class(name="ClassDiagram::Table")
Named = Class(name="Named")
Column = Class(name="Column")
ClassDiagram_Column = Class(name="ClassDiagram::Column")
Table = Class(name="Table")
Type = Class(name="Type")
ClassDiagram_Type = Class(name="ClassDiagram::Type")

# ClassDiagram_NamedElement class attributes and methods
ClassDiagram_NamedElement_name: Property = Property(name="name", type=StringType)
ClassDiagram_NamedElement.attributes={ClassDiagram_NamedElement_name}

# ClassDiagram_Classifier class attributes and methods

# NamedElement class attributes and methods

# ClassDiagram_DataType class attributes and methods

# Classifier class attributes and methods

# ClassDiagram_Class class attributes and methods
ClassDiagram_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
ClassDiagram_Class.attributes={ClassDiagram_Class_isAbstract}

# Class class attributes and methods

# Attribute class attributes and methods

# ClassDiagram_Attribute class attributes and methods
ClassDiagram_Attribute_multiValued: Property = Property(name="multiValued", type=StringType)
ClassDiagram_Attribute.attributes={ClassDiagram_Attribute_multiValued}

# ClassDiagram_Named class attributes and methods
ClassDiagram_Named_name: Property = Property(name="name", type=StringType)
ClassDiagram_Named.attributes={ClassDiagram_Named_name}

# ClassDiagram_Table class attributes and methods

# Named class attributes and methods

# Column class attributes and methods

# ClassDiagram_Column class attributes and methods

# Table class attributes and methods

# Type class attributes and methods

# ClassDiagram_Type class attributes and methods

# Relationships
super0: BinaryAssociation = BinaryAssociation(
    name="super0",
    ends={
        Property(name="Class", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
attr1: BinaryAssociation = BinaryAssociation(
    name="attr1",
    ends={
        Property(name="#", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="Classifier", type=ClassDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Attribute", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="04", type=Class_, multiplicity=Multiplicity(1, 1)),
        Property(name="#5", type=ClassDiagram_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
col6: BinaryAssociation = BinaryAssociation(
    name="col6",
    ends={
        Property(name="#8", type=ClassDiagram_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="07", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key9: BinaryAssociation = BinaryAssociation(
    name="key9",
    ends={
        Property(name="#11", type=ClassDiagram_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="010", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="#14", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="013", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf15: BinaryAssociation = BinaryAssociation(
    name="keyOf15",
    ends={
        Property(name="#17", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="016", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="Type", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Column", type=Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ClassDiagram_Classifier_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Classifier)
gen_ClassDiagram_DataType_Classifier = Generalization(general=Classifier, specific=ClassDiagram_DataType)
gen_ClassDiagram_Class_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Class)
gen_ClassDiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Attribute)
gen_ClassDiagram_Table_Named = Generalization(general=Named, specific=ClassDiagram_Table)
gen_ClassDiagram_Column_Named = Generalization(general=Named, specific=ClassDiagram_Column)
gen_ClassDiagram_Type_Named = Generalization(general=Named, specific=ClassDiagram_Type)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ClassDiagram_NamedElement, ClassDiagram_Classifier, NamedElement, ClassDiagram_DataType, Classifier, ClassDiagram_Class, Class_, Attribute, ClassDiagram_Attribute, ClassDiagram_Named, ClassDiagram_Table, Named, Column, ClassDiagram_Column, Table, Type, ClassDiagram_Type},
    associations={super0, attr1, type2, owner3, col6, key9, owner12, keyOf15, type18},
    generalizations={gen_ClassDiagram_Classifier_NamedElement, gen_ClassDiagram_DataType_Classifier, gen_ClassDiagram_Class_Classifier, gen_ClassDiagram_Attribute_NamedElement, gen_ClassDiagram_Table_Named, gen_ClassDiagram_Column_Named, gen_ClassDiagram_Type_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)