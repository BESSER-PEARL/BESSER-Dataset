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
Column = Class(name="Column")
Relational_Column = Class(name="Relational_Column")
Table = Class(name="Table")
Type = Class(name="Type")
Relational_Named = Class(name="Relational_Named", is_abstract=True)
Relational_Table = Class(name="Relational_Table")
Named = Class(name="Named")
Relational_Type = Class(name="Relational_Type")

# Column class attributes and methods

# Relational_Column class attributes and methods

# Table class attributes and methods

# Type class attributes and methods

# Relational_Named class attributes and methods
Relational_Named_name: Property = Property(name="name", type=StringType)
Relational_Named.attributes={Relational_Named_name}

# Relational_Table class attributes and methods

# Named class attributes and methods

# Relational_Type class attributes and methods

# Relationships
col0: BinaryAssociation = BinaryAssociation(
    name="col0",
    ends={
        Property(name="Column", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="Column2", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Table", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="col", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf4: BinaryAssociation = BinaryAssociation(
    name="keyOf4",
    ends={
        Property(name="Table5", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="Type", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Column", type=Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Relational_Column_Named = Generalization(general=Named, specific=Relational_Column)
gen_Relational_Table_Named = Generalization(general=Named, specific=Relational_Table)
gen_Relational_Type_Named = Generalization(general=Named, specific=Relational_Type)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Column, Relational_Column, Table, Type, Relational_Named, Relational_Table, Named, Relational_Type},
    associations={col0, key1, owner3, keyOf4, type6},
    generalizations={gen_Relational_Column_Named, gen_Relational_Table_Named, gen_Relational_Type_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)