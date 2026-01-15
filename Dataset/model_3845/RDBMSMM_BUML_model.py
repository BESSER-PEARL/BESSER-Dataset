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
RDBMSMM_Column = Class(name="RDBMSMM::Column")
RDBMSMM_FKey = Class(name="RDBMSMM::FKey")
RDBMSMM_Table = Class(name="RDBMSMM::Table")
RDBMSMM_RDBMSModel = Class(name="RDBMSMM::RDBMSModel")

# RDBMSMM_Column class attributes and methods
RDBMSMM_Column_name: Property = Property(name="name", type=StringType)
RDBMSMM_Column_type: Property = Property(name="type", type=StringType)
RDBMSMM_Column.attributes={RDBMSMM_Column_name, RDBMSMM_Column_type}

# RDBMSMM_FKey class attributes and methods

# RDBMSMM_Table class attributes and methods
RDBMSMM_Table_name: Property = Property(name="name", type=StringType)
RDBMSMM_Table.attributes={RDBMSMM_Table_name}

# RDBMSMM_RDBMSModel class attributes and methods

# Relationships
cols0: BinaryAssociation = BinaryAssociation(
    name="cols0",
    ends={
        Property(name="RDBMSMM_Column", type=RDBMSMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_Table", type=RDBMSMM_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pkey1: BinaryAssociation = BinaryAssociation(
    name="pkey1",
    ends={
        Property(name="RDBMSMM_Column3", type=RDBMSMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_Table2", type=RDBMSMM_Column, multiplicity=Multiplicity(1, 9999))
    }
)
fkeys4: BinaryAssociation = BinaryAssociation(
    name="fkeys4",
    ends={
        Property(name="RDBMSMM_FKey", type=RDBMSMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_Table5", type=RDBMSMM_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="RDBMSMM_Table8", type=RDBMSMM_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_FKey7", type=RDBMSMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
cols9: BinaryAssociation = BinaryAssociation(
    name="cols9",
    ends={
        Property(name="RDBMSMM_Column11", type=RDBMSMM_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_FKey10", type=RDBMSMM_Column, multiplicity=Multiplicity(1, 9999))
    }
)
table12: BinaryAssociation = BinaryAssociation(
    name="table12",
    ends={
        Property(name="RDBMSMM_Table13", type=RDBMSMM_RDBMSModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMSMM_RDBMSModel", type=RDBMSMM_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="RDBMSMM",
    types={RDBMSMM_Column, RDBMSMM_FKey, RDBMSMM_Table, RDBMSMM_RDBMSModel},
    associations={cols0, pkey1, fkeys4, references6, cols9, table12},
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