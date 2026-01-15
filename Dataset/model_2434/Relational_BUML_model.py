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
Relational_Table = Class(name="Relational::Table")
Named = Class(name="Named")
Relational_Named = Class(name="Relational::Named", is_abstract=True)
Relational_Column = Class(name="Relational::Column")
Column = Class(name="Column")
Type = Class(name="Type")
Relational_Type = Class(name="Relational::Type")
Table = Class(name="Table")

# Relational_Table class attributes and methods

# Named class attributes and methods

# Relational_Named class attributes and methods
Relational_Named_name: Property = Property(name="name", type=StringType)
Relational_Named.attributes={Relational_Named_name}

# Relational_Column class attributes and methods

# Column class attributes and methods

# Type class attributes and methods

# Relational_Type class attributes and methods

# Table class attributes and methods

# Relationships
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="#3", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
col0: BinaryAssociation = BinaryAssociation(
    name="col0",
    ends={
        Property(name="#", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="Type", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Column", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="#6", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf7: BinaryAssociation = BinaryAssociation(
    name="keyOf7",
    ends={
        Property(name="#9", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=Table, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Relational_Table_Named = Generalization(general=Named, specific=Relational_Table)
gen_Relational_Column_Named = Generalization(general=Named, specific=Relational_Column)
gen_Relational_Type_Named = Generalization(general=Named, specific=Relational_Type)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Relational_Table, Named, Relational_Named, Relational_Column, Column, Type, Relational_Type, Table},
    associations={key1, col0, type10, owner4, keyOf7},
    generalizations={gen_Relational_Table_Named, gen_Relational_Column_Named, gen_Relational_Type_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)