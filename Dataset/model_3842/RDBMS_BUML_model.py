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
RDBMS_Table = Class(name="RDBMS::Table")
FKey = Class(name="FKey")
RDBMS_Column = Class(name="RDBMS::Column")
RDBMS_FKey = Class(name="RDBMS::FKey")
Table = Class(name="Table")
RDBMS_Schema = Class(name="RDBMS::Schema")
Column = Class(name="Column")

# RDBMS_Table class attributes and methods
RDBMS_Table_name: Property = Property(name="name", type=StringType)
RDBMS_Table_tipo: Property = Property(name="tipo", type=StringType)
RDBMS_Table.attributes={RDBMS_Table_name, RDBMS_Table_tipo}

# FKey class attributes and methods

# RDBMS_Column class attributes and methods
RDBMS_Column_name: Property = Property(name="name", type=StringType)
RDBMS_Column_type: Property = Property(name="type", type=StringType)
RDBMS_Column.attributes={RDBMS_Column_type, RDBMS_Column_name}

# RDBMS_FKey class attributes and methods

# Table class attributes and methods

# RDBMS_Schema class attributes and methods
RDBMS_Schema_name: Property = Property(name="name", type=StringType)
RDBMS_Schema.attributes={RDBMS_Schema_name}

# Column class attributes and methods

# Relationships
fkeys0: BinaryAssociation = BinaryAssociation(
    name="fkeys0",
    ends={
        Property(name="FKey", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table", type=FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="Table", type=RDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_FKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
cols7: BinaryAssociation = BinaryAssociation(
    name="cols7",
    ends={
        Property(name="Column9", type=RDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_FKey8", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables10: BinaryAssociation = BinaryAssociation(
    name="tables10",
    ends={
        Property(name="Table11", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Schema", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey1: BinaryAssociation = BinaryAssociation(
    name="pkey1",
    ends={
        Property(name="Column", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table2", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
cols3: BinaryAssociation = BinaryAssociation(
    name="cols3",
    ends={
        Property(name="Column5", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table4", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="RDBMS",
    types={RDBMS_Table, FKey, RDBMS_Column, RDBMS_FKey, Table, RDBMS_Schema, Column},
    associations={fkeys0, references6, cols7, tables10, pkey1, cols3},
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