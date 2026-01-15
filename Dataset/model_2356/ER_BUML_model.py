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
ER_ForeignKey = Class(name="ER::ForeignKey")
ER_Schema = Class(name="ER::Schema")
ER_Table = Class(name="ER::Table")
ER_Key = Class(name="ER::Key")
ER_Column = Class(name="ER::Column")

# ER_ForeignKey class attributes and methods
ER_ForeignKey_name: Property = Property(name="name", type=StringType)
ER_ForeignKey.attributes={ER_ForeignKey_name}

# ER_Schema class attributes and methods
ER_Schema_name: Property = Property(name="name", type=StringType)
ER_Schema.attributes={ER_Schema_name}

# ER_Table class attributes and methods
ER_Table_name: Property = Property(name="name", type=StringType)
ER_Table.attributes={ER_Table_name}

# ER_Key class attributes and methods
ER_Key_name: Property = Property(name="name", type=StringType)
ER_Key.attributes={ER_Key_name}

# ER_Column class attributes and methods
ER_Column_name: Property = Property(name="name", type=StringType)
ER_Column_type: Property = Property(name="type", type=StringType)
ER_Column.attributes={ER_Column_name, ER_Column_type}

# Relationships
foreignKey1: BinaryAssociation = BinaryAssociation(
    name="foreignKey1",
    ends={
        Property(name="ForeignKey", type=ER_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema2", type=ER_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema3: BinaryAssociation = BinaryAssociation(
    name="schema3",
    ends={
        Property(name="Schema", type=ER_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=ER_Schema, multiplicity=Multiplicity(1, 1))
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="Table", type=ER_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=ER_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referedBy13: BinaryAssociation = BinaryAssociation(
    name="referedBy13",
    ends={
        Property(name="ER_ForeignKey", type=ER_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_Key14", type=ER_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="Table16", type=ER_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=ER_Table, multiplicity=Multiplicity(1, 1))
    }
)
hasKey4: BinaryAssociation = BinaryAssociation(
    name="hasKey4",
    ends={
        Property(name="Key", type=ER_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ER_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column5: BinaryAssociation = BinaryAssociation(
    name="column5",
    ends={
        Property(name="Column", type=ER_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=ER_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasForeignKey7: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey7",
    ends={
        Property(name="ForeignKey9", type=ER_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner8", type=ER_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Table11", type=ER_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="hasKey", type=ER_Table, multiplicity=Multiplicity(1, 1))
    }
)
column12: BinaryAssociation = BinaryAssociation(
    name="column12",
    ends={
        Property(name="ER_Column", type=ER_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_Key", type=ER_Column, multiplicity=Multiplicity(1, 9999))
    }
)
hasKey17: BinaryAssociation = BinaryAssociation(
    name="hasKey17",
    ends={
        Property(name="ER_Key19", type=ER_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_Column18", type=ER_Key, multiplicity=Multiplicity(0, 9999))
    }
)
hasForeignKey20: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey20",
    ends={
        Property(name="ForeignKey22", type=ER_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column21", type=ER_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
schema23: BinaryAssociation = BinaryAssociation(
    name="schema23",
    ends={
        Property(name="Schema24", type=ER_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=ER_Schema, multiplicity=Multiplicity(1, 1))
    }
)
owner25: BinaryAssociation = BinaryAssociation(
    name="owner25",
    ends={
        Property(name="Table26", type=ER_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey", type=ER_Table, multiplicity=Multiplicity(1, 1))
    }
)
column27: BinaryAssociation = BinaryAssociation(
    name="column27",
    ends={
        Property(name="Column29", type=ER_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey28", type=ER_Column, multiplicity=Multiplicity(1, 9999))
    }
)
refersTo30: BinaryAssociation = BinaryAssociation(
    name="refersTo30",
    ends={
        Property(name="ER_Key32", type=ER_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ER_ForeignKey31", type=ER_Key, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ER",
    types={ER_ForeignKey, ER_Schema, ER_Table, ER_Key, ER_Column},
    associations={foreignKey1, schema3, table0, referedBy13, owner15, hasKey4, column5, hasForeignKey7, owner10, column12, hasKey17, hasForeignKey20, schema23, owner25, column27, refersTo30},
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