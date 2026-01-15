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
rdbmsMM_ForeignKey = Class(name="rdbmsMM::ForeignKey")
rdbmsMM_Column = Class(name="rdbmsMM::Column")
rdbmsMM_Key = Class(name="rdbmsMM::Key")
rdbmsMM_Schema = Class(name="rdbmsMM::Schema")
rdbmsMM_Table = Class(name="rdbmsMM::Table")
rdbmsMM_dummy = Class(name="rdbmsMM::dummy")

# rdbmsMM_ForeignKey class attributes and methods
rdbmsMM_ForeignKey_name: Property = Property(name="name", type=StringType)
rdbmsMM_ForeignKey.attributes={rdbmsMM_ForeignKey_name}

# rdbmsMM_Column class attributes and methods
rdbmsMM_Column_name: Property = Property(name="name", type=StringType)
rdbmsMM_Column_type: Property = Property(name="type", type=StringType)
rdbmsMM_Column.attributes={rdbmsMM_Column_type, rdbmsMM_Column_name}

# rdbmsMM_Key class attributes and methods
rdbmsMM_Key_name: Property = Property(name="name", type=StringType)
rdbmsMM_Key.attributes={rdbmsMM_Key_name}

# rdbmsMM_Schema class attributes and methods
rdbmsMM_Schema_name: Property = Property(name="name", type=StringType)
rdbmsMM_Schema.attributes={rdbmsMM_Schema_name}

# rdbmsMM_Table class attributes and methods
rdbmsMM_Table_name: Property = Property(name="name", type=StringType)
rdbmsMM_Table.attributes={rdbmsMM_Table_name}

# rdbmsMM_dummy class attributes and methods

# Relationships
foreignKey1: BinaryAssociation = BinaryAssociation(
    name="foreignKey1",
    ends={
        Property(name="ForeignKey", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema2", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema3: BinaryAssociation = BinaryAssociation(
    name="schema3",
    ends={
        Property(name="Schema", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1))
    }
)
column4: BinaryAssociation = BinaryAssociation(
    name="column4",
    ends={
        Property(name="Column", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rdbmsMM_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasKey5: BinaryAssociation = BinaryAssociation(
    name="hasKey5",
    ends={
        Property(name="Key", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=rdbmsMM_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="Table", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=rdbmsMM_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="Table19", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="hasKey", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
column20: BinaryAssociation = BinaryAssociation(
    name="column20",
    ends={
        Property(name="Column22", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="hasKey21", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 9999))
    }
)
referredBy23: BinaryAssociation = BinaryAssociation(
    name="referredBy23",
    ends={
        Property(name="ForeignKey24", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
schema25: BinaryAssociation = BinaryAssociation(
    name="schema25",
    ends={
        Property(name="Schema26", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1))
    }
)
hasForeignKey7: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey7",
    ends={
        Property(name="ForeignKey9", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner8", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="Table11", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
hasKey12: BinaryAssociation = BinaryAssociation(
    name="hasKey12",
    ends={
        Property(name="Key14", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column13", type=rdbmsMM_Key, multiplicity=Multiplicity(0, 9999))
    }
)
hasForeignKey15: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey15",
    ends={
        Property(name="ForeignKey17", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column16", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo27: BinaryAssociation = BinaryAssociation(
    name="refersTo27",
    ends={
        Property(name="Key28", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referredBy", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1))
    }
)
owner29: BinaryAssociation = BinaryAssociation(
    name="owner29",
    ends={
        Property(name="Table30", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
column31: BinaryAssociation = BinaryAssociation(
    name="column31",
    ends={
        Property(name="Column33", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="hasForeignKey32", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 9999))
    }
)
containsSchema34: BinaryAssociation = BinaryAssociation(
    name="containsSchema34",
    ends={
        Property(name="rdbmsMM_Schema", type=rdbmsMM_dummy, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsMM_dummy", type=rdbmsMM_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rdbmsMM",
    types={rdbmsMM_ForeignKey, rdbmsMM_Column, rdbmsMM_Key, rdbmsMM_Schema, rdbmsMM_Table, rdbmsMM_dummy},
    associations={foreignKey1, schema3, column4, hasKey5, table0, owner18, column20, referredBy23, schema25, hasForeignKey7, owner10, hasKey12, hasForeignKey15, refersTo27, owner29, column31, containsSchema34},
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