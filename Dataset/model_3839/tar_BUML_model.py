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
target_Table = Class(name="target::Table")
target_FKey = Class(name="target::FKey")
target_Column = Class(name="target::Column")
target_Database = Class(name="target::Database")

# target_Table class attributes and methods
target_Table_name: Property = Property(name="name", type=StringType)
target_Table.attributes={target_Table_name}

# target_FKey class attributes and methods

# target_Column class attributes and methods
target_Column_type: Property = Property(name="type", type=StringType)
target_Column_name: Property = Property(name="name", type=StringType)
target_Column.attributes={target_Column_name, target_Column_type}

# target_Database class attributes and methods

# Relationships
fkeys0: BinaryAssociation = BinaryAssociation(
    name="fkeys0",
    ends={
        Property(name="target_FKey", type=target_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target_Table", type=target_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table12: BinaryAssociation = BinaryAssociation(
    name="table12",
    ends={
        Property(name="target_Table13", type=target_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="target_Database", type=target_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey1: BinaryAssociation = BinaryAssociation(
    name="pkey1",
    ends={
        Property(name="target_Column", type=target_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target_Table2", type=target_Column, multiplicity=Multiplicity(0, 1))
    }
)
cols3: BinaryAssociation = BinaryAssociation(
    name="cols3",
    ends={
        Property(name="target_Column5", type=target_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target_Table4", type=target_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fcols6: BinaryAssociation = BinaryAssociation(
    name="fcols6",
    ends={
        Property(name="target_Column8", type=target_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="target_FKey7", type=target_Column, multiplicity=Multiplicity(0, 9999))
    }
)
references9: BinaryAssociation = BinaryAssociation(
    name="references9",
    ends={
        Property(name="target_Table11", type=target_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="target_FKey10", type=target_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="target",
    types={target_Table, target_FKey, target_Column, target_Database},
    associations={fkeys0, table12, pkey1, cols3, fcols6, references9},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)