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
RDBMS_Scheme = Class(name="RDBMS_Scheme")
RDBMS_Table = Class(name="RDBMS_Table")
RDBMS_FKey = Class(name="RDBMS_FKey")
RDBMS_Column = Class(name="RDBMS_Column")
RDBMS_PKey = Class(name="RDBMS_PKey")

# RDBMS_Scheme class attributes and methods
RDBMS_Scheme_name: Property = Property(name="name", type=StringType)
RDBMS_Scheme_m_setName: Method = Method(name="setName", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Scheme_m_addTable: Method = Method(name="addTable", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Scheme_m_remTable: Method = Method(name="remTable", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Scheme.attributes={RDBMS_Scheme_name}
RDBMS_Scheme.methods={RDBMS_Scheme_m_remTable, RDBMS_Scheme_m_setName, RDBMS_Scheme_m_addTable}

# RDBMS_Table class attributes and methods
RDBMS_Table_name: Property = Property(name="name", type=StringType)
RDBMS_Table_m_setName: Method = Method(name="setName", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Table_m_addColumn: Method = Method(name="addColumn", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Table_m_remColumn: Method = Method(name="remColumn", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Table.attributes={RDBMS_Table_name}
RDBMS_Table.methods={RDBMS_Table_m_remColumn, RDBMS_Table_m_addColumn, RDBMS_Table_m_setName}

# RDBMS_FKey class attributes and methods

# RDBMS_Column class attributes and methods
RDBMS_Column_name: Property = Property(name="name", type=StringType)
RDBMS_Column_m_setName: Method = Method(name="setName", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Column_m_setTable: Method = Method(name="setTable", parameters={Parameter(name='RDBMS_n', type=StringType)})
RDBMS_Column.attributes={RDBMS_Column_name}
RDBMS_Column.methods={RDBMS_Column_m_setTable, RDBMS_Column_m_setName}

# RDBMS_PKey class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="RDBMS.ecoreTable", type=RDBMS_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="scheme", type=RDBMS_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys1: BinaryAssociation = BinaryAssociation(
    name="keys1",
    ends={
        Property(name="RDBMS.ecoreFKey", type=RDBMS_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="scheme2", type=RDBMS_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="RDBMS.ecoreColumn", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=RDBMS_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
scheme4: BinaryAssociation = BinaryAssociation(
    name="scheme4",
    ends={
        Property(name="RDBMS.ecoreScheme", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=RDBMS_Scheme, multiplicity=Multiplicity(1, 1))
    }
)
key5: BinaryAssociation = BinaryAssociation(
    name="key5",
    ends={
        Property(name="RDBMS_PKey", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table", type=RDBMS_PKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table6: BinaryAssociation = BinaryAssociation(
    name="table6",
    ends={
        Property(name="RDBMS.ecoreTable7", type=RDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=RDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
refersTo8: BinaryAssociation = BinaryAssociation(
    name="refersTo8",
    ends={
        Property(name="RDBMS_PKey9", type=RDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_FKey", type=RDBMS_PKey, multiplicity=Multiplicity(1, 1))
    }
)
column10: BinaryAssociation = BinaryAssociation(
    name="column10",
    ends={
        Property(name="RDBMS_Column", type=RDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_FKey11", type=RDBMS_Column, multiplicity=Multiplicity(1, 1))
    }
)
scheme12: BinaryAssociation = BinaryAssociation(
    name="scheme12",
    ends={
        Property(name="RDBMS.ecoreScheme13", type=RDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=RDBMS_Scheme, multiplicity=Multiplicity(1, 1))
    }
)
column14: BinaryAssociation = BinaryAssociation(
    name="column14",
    ends={
        Property(name="RDBMS_Column16", type=RDBMS_PKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_PKey15", type=RDBMS_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="RDBMS",
    types={RDBMS_Scheme, RDBMS_Table, RDBMS_FKey, RDBMS_Column, RDBMS_PKey},
    associations={tables0, keys1, columns3, scheme4, key5, table6, refersTo8, column10, scheme12, column14},
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