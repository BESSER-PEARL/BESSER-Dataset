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
rdb_Schema = Class(name="rdb::Schema")
rdb_Table = Class(name="rdb::Table")
rdb_Column = Class(name="rdb::Column")
rdb_PrimaryKey = Class(name="rdb::PrimaryKey")
Key = Class(name="Key")
rdb_ForeignKey = Class(name="rdb::ForeignKey")
rdb_Key = Class(name="rdb::Key", is_abstract=True)

# rdb_Schema class attributes and methods
rdb_Schema_name: Property = Property(name="name", type=StringType)
rdb_Schema.attributes={rdb_Schema_name}

# rdb_Table class attributes and methods
rdb_Table_name: Property = Property(name="name", type=StringType)
rdb_Table.attributes={rdb_Table_name}

# rdb_Column class attributes and methods
rdb_Column_type: Property = Property(name="type", type=StringType)
rdb_Column_name: Property = Property(name="name", type=StringType)
rdb_Column.attributes={rdb_Column_type, rdb_Column_name}

# rdb_PrimaryKey class attributes and methods

# Key class attributes and methods

# rdb_ForeignKey class attributes and methods

# rdb_Key class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="rdb_Table", type=rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Schema", type=rdb_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="rdb_Column", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table2", type=rdb_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyColumn5: BinaryAssociation = BinaryAssociation(
    name="keyColumn5",
    ends={
        Property(name="rdb_Column7", type=rdb_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Key6", type=rdb_Column, multiplicity=Multiplicity(1, 9999))
    }
)
ref8: BinaryAssociation = BinaryAssociation(
    name="ref8",
    ends={
        Property(name="rdb_Column9", type=rdb_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_ForeignKey", type=rdb_Column, multiplicity=Multiplicity(1, 1))
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="rdb_Key", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table4", type=rdb_Key, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_rdb_PrimaryKey_Key = Generalization(general=Key, specific=rdb_PrimaryKey)
gen_rdb_ForeignKey_Key = Generalization(general=Key, specific=rdb_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="rdb",
    types={rdb_Schema, rdb_Table, rdb_Column, rdb_PrimaryKey, Key, rdb_ForeignKey, rdb_Key},
    associations={tables0, columns1, keyColumn5, ref8, constraints3},
    generalizations={gen_rdb_PrimaryKey_Key, gen_rdb_ForeignKey_Key},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)