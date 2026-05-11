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
ClassDiagram_NamedElement = Class(name="ClassDiagram_NamedElement", is_abstract=True)
ClassDiagram_Classifier = Class(name="ClassDiagram_Classifier", is_abstract=True)
NamedElement = Class(name="NamedElement")
ClassDiagram_DataType = Class(name="ClassDiagram_DataType")
Classifier = Class(name="Classifier")
ClassDiagram_Class = Class(name="ClassDiagram_Class")
Class_ = Class(name="Class")
ClassDiagram_Named = Class(name="ClassDiagram_Named", is_abstract=True)
ClassDiagram_Table = Class(name="ClassDiagram_Table")
Named = Class(name="Named")
Column = Class(name="Column")
ClassDiagram_Column = Class(name="ClassDiagram_Column")
Table = Class(name="Table")
Type = Class(name="Type")
ClassDiagram_Type = Class(name="ClassDiagram_Type")
Attribute = Class(name="Attribute")
ClassDiagram_Attribute = Class(name="ClassDiagram_Attribute")

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

# Attribute class attributes and methods

# ClassDiagram_Attribute class attributes and methods
ClassDiagram_Attribute_multiValued: Property = Property(name="multiValued", type=StringType)
ClassDiagram_Attribute.attributes={ClassDiagram_Attribute_multiValued}

# Relationships
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
        Property(name="Class4", type=ClassDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attr", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
col5: BinaryAssociation = BinaryAssociation(
    name="col5",
    ends={
        Property(name="Column", type=ClassDiagram_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key7: BinaryAssociation = BinaryAssociation(
    name="key7",
    ends={
        Property(name="Column8", type=ClassDiagram_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Table", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf10: BinaryAssociation = BinaryAssociation(
    name="keyOf10",
    ends={
        Property(name="Table11", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="Type", type=ClassDiagram_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassDiagram_Column", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
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
        Property(name="Attribute", type=ClassDiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ClassDiagram_Classifier_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Classifier)
gen_ClassDiagram_DataType_Classifier = Generalization(general=Classifier, specific=ClassDiagram_DataType)
gen_ClassDiagram_Class_Classifier = Generalization(general=Classifier, specific=ClassDiagram_Class)
gen_ClassDiagram_Table_Named = Generalization(general=Named, specific=ClassDiagram_Table)
gen_ClassDiagram_Column_Named = Generalization(general=Named, specific=ClassDiagram_Column)
gen_ClassDiagram_Type_Named = Generalization(general=Named, specific=ClassDiagram_Type)
gen_ClassDiagram_Attribute_NamedElement = Generalization(general=NamedElement, specific=ClassDiagram_Attribute)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={ClassDiagram_NamedElement, ClassDiagram_Classifier, NamedElement, ClassDiagram_DataType, Classifier, ClassDiagram_Class, Class_, ClassDiagram_Named, ClassDiagram_Table, Named, Column, ClassDiagram_Column, Table, Type, ClassDiagram_Type, Attribute, ClassDiagram_Attribute},
    associations={type2, owner3, col5, key7, owner9, keyOf10, type12, super0, attr1},
    generalizations={gen_ClassDiagram_Classifier_NamedElement, gen_ClassDiagram_DataType_Classifier, gen_ClassDiagram_Class_Classifier, gen_ClassDiagram_Table_Named, gen_ClassDiagram_Column_Named, gen_ClassDiagram_Type_Named, gen_ClassDiagram_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)