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
RDBMS_Column = Class(name="RDBMS::Column")
RDBMS_Key = Class(name="RDBMS::Key")
RDBMS_Schema = Class(name="RDBMS::Schema")
RDBMS_Table = Class(name="RDBMS::Table")
RDBMS_ForeignKey = Class(name="RDBMS::ForeignKey")

# RDBMS_Column class attributes and methods
RDBMS_Column_name: Property = Property(name="name", type=StringType)
RDBMS_Column_type: Property = Property(name="type", type=StringType)
RDBMS_Column.attributes={RDBMS_Column_name, RDBMS_Column_type}

# RDBMS_Key class attributes and methods
RDBMS_Key_name: Property = Property(name="name", type=StringType)
RDBMS_Key.attributes={RDBMS_Key_name}

# RDBMS_Schema class attributes and methods
RDBMS_Schema_name: Property = Property(name="name", type=StringType)
RDBMS_Schema.attributes={RDBMS_Schema_name}

# RDBMS_Table class attributes and methods
RDBMS_Table_name: Property = Property(name="name", type=StringType)
RDBMS_Table.attributes={RDBMS_Table_name}

# RDBMS_ForeignKey class attributes and methods
RDBMS_ForeignKey_name: Property = Property(name="name", type=StringType)
RDBMS_ForeignKey.attributes={RDBMS_ForeignKey_name}

# Relationships
schema3: BinaryAssociation = BinaryAssociation(
    name="schema3",
    ends={
        Property(name="Schema", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1))
    }
)
column4: BinaryAssociation = BinaryAssociation(
    name="column4",
    ends={
        Property(name="Column", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RDBMS_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasKey5: BinaryAssociation = BinaryAssociation(
    name="hasKey5",
    ends={
        Property(name="Key", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=RDBMS_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="Table", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=RDBMS_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey1: BinaryAssociation = BinaryAssociation(
    name="foreignKey1",
    ends={
        Property(name="ForeignKey", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema2", type=RDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column20: BinaryAssociation = BinaryAssociation(
    name="column20",
    ends={
        Property(name="Column22", type=RDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="hasKey21", type=RDBMS_Column, multiplicity=Multiplicity(1, 9999))
    }
)
referredBy23: BinaryAssociation = BinaryAssociation(
    name="referredBy23",
    ends={
        Property(name="ForeignKey24", type=RDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=RDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
schema25: BinaryAssociation = BinaryAssociation(
    name="schema25",
    ends={
        Property(name="Schema26", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1))
    }
)
hasForeignKey7: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey7",
    ends={
        Property(name="ForeignKey9", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner8", type=RDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Table11", type=RDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=RDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
hasKey12: BinaryAssociation = BinaryAssociation(
    name="hasKey12",
    ends={
        Property(name="Key14", type=RDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column13", type=RDBMS_Key, multiplicity=Multiplicity(0, 9999))
    }
)
hasForeignKey15: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey15",
    ends={
        Property(name="ForeignKey17", type=RDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column16", type=RDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="Table19", type=RDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="hasKey", type=RDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
refersTo27: BinaryAssociation = BinaryAssociation(
    name="refersTo27",
    ends={
        Property(name="Key28", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referredBy", type=RDBMS_Key, multiplicity=Multiplicity(1, 1))
    }
)
owner29: BinaryAssociation = BinaryAssociation(
    name="owner29",
    ends={
        Property(name="Table30", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey", type=RDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
column31: BinaryAssociation = BinaryAssociation(
    name="column31",
    ends={
        Property(name="Column33", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey32", type=RDBMS_Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="RDBMS",
    types={RDBMS_Column, RDBMS_Key, RDBMS_Schema, RDBMS_Table, RDBMS_ForeignKey},
    associations={schema3, column4, hasKey5, table0, foreignKey1, column20, referredBy23, schema25, hasForeignKey7, owner10, hasKey12, hasForeignKey15, owner18, refersTo27, owner29, column31},
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