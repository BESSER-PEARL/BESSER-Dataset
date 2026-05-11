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
Type = Class(name="Type")
Relational_Type = Class(name="Relational_Type")
Relational_Named = Class(name="Relational_Named", is_abstract=True)
Relational_Schema = Class(name="Relational_Schema")
Named = Class(name="Named")
Table = Class(name="Table")
Relational_Table = Class(name="Relational_Table")
Schema = Class(name="Schema")
Column = Class(name="Column")
Relational_Column = Class(name="Relational_Column")
Relational_System = Class(name="Relational_System")

# Type class attributes and methods

# Relational_Type class attributes and methods

# Relational_Named class attributes and methods
Relational_Named_name: Property = Property(name="name", type=StringType)
Relational_Named.attributes={Relational_Named_name}

# Relational_Schema class attributes and methods

# Named class attributes and methods

# Table class attributes and methods

# Relational_Table class attributes and methods

# Schema class attributes and methods

# Column class attributes and methods

# Relational_Column class attributes and methods

# Relational_System class attributes and methods

# Relationships
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Table7", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf8: BinaryAssociation = BinaryAssociation(
    name="keyOf8",
    ends={
        Property(name="Table9", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="Type", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Column", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
ownedElements0: BinaryAssociation = BinaryAssociation(
    name="ownedElements0",
    ends={
        Property(name="Table", type=Relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="Schema", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
col2: BinaryAssociation = BinaryAssociation(
    name="col2",
    ends={
        Property(name="Column", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner3", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key4: BinaryAssociation = BinaryAssociation(
    name="key4",
    ends={
        Property(name="Column5", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
schemas11: BinaryAssociation = BinaryAssociation(
    name="schemas11",
    ends={
        Property(name="Schema12", type=Relational_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_System", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Relational_Type_Named = Generalization(general=Named, specific=Relational_Type)
gen_Relational_Schema_Named = Generalization(general=Named, specific=Relational_Schema)
gen_Relational_Table_Named = Generalization(general=Named, specific=Relational_Table)
gen_Relational_Column_Named = Generalization(general=Named, specific=Relational_Column)
gen_Relational_System_Named = Generalization(general=Named, specific=Relational_System)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Type, Relational_Type, Relational_Named, Relational_Schema, Named, Table, Relational_Table, Schema, Column, Relational_Column, Relational_System},
    associations={owner6, keyOf8, type10, ownedElements0, owner1, col2, key4, schemas11},
    generalizations={gen_Relational_Type_Named, gen_Relational_Schema_Named, gen_Relational_Table_Named, gen_Relational_Column_Named, gen_Relational_System_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)