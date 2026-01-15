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

# Enumerations
FKeyType: Enumeration = Enumeration(
    name="FKeyType",
    literals={
            EnumerationLiteral(name="PKEY")
    }
)

# Classes
SimpleRDBMS_Table = Class(name="SimpleRDBMS::Table")
SimpleRDBMS_FKey = Class(name="SimpleRDBMS::FKey")
SimpleRDBMS_Column = Class(name="SimpleRDBMS::Column")

# SimpleRDBMS_Table class attributes and methods
SimpleRDBMS_Table_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Table_id: Property = Property(name="id", type=IntegerType)
SimpleRDBMS_Table.attributes={SimpleRDBMS_Table_id, SimpleRDBMS_Table_name}

# SimpleRDBMS_FKey class attributes and methods
SimpleRDBMS_FKey_fkeyType: Property = Property(name="fkeyType", type=StringType)
SimpleRDBMS_FKey.attributes={SimpleRDBMS_FKey_fkeyType}

# SimpleRDBMS_Column class attributes and methods
SimpleRDBMS_Column_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Column_type: Property = Property(name="type", type=StringType)
SimpleRDBMS_Column_id: Property = Property(name="id", type=IntegerType)
SimpleRDBMS_Column.attributes={SimpleRDBMS_Column_name, SimpleRDBMS_Column_type, SimpleRDBMS_Column_id}

# Relationships
fkeys0: BinaryAssociation = BinaryAssociation(
    name="fkeys0",
    ends={
        Property(name="SimpleRDBMS_FKey", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table", type=SimpleRDBMS_FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey1: BinaryAssociation = BinaryAssociation(
    name="pkey1",
    ends={
        Property(name="SimpleRDBMS_Column", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table2", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)
cols3: BinaryAssociation = BinaryAssociation(
    name="cols3",
    ends={
        Property(name="SimpleRDBMS_Column5", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table4", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="SimpleRDBMS_Table8", type=SimpleRDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_FKey7", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
cols9: BinaryAssociation = BinaryAssociation(
    name="cols9",
    ends={
        Property(name="SimpleRDBMS_Column11", type=SimpleRDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_FKey10", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="SimpleRDBMS",
    types={SimpleRDBMS_Table, SimpleRDBMS_FKey, SimpleRDBMS_Column, FKeyType},
    associations={fkeys0, pkey1, cols3, references6, cols9},
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