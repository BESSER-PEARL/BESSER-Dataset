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
SimpleRDBMS_FKey = Class(name="SimpleRDBMS::FKey")
SimpleRDBMS_Column = Class(name="SimpleRDBMS::Column")
SimpleRDBMS_PKey = Class(name="SimpleRDBMS::PKey")
FKey = Class(name="FKey")
SimpleRDBMS_Table = Class(name="SimpleRDBMS::Table")

# SimpleRDBMS_FKey class attributes and methods

# SimpleRDBMS_Column class attributes and methods
SimpleRDBMS_Column_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Column_type: Property = Property(name="type", type=StringType)
SimpleRDBMS_Column_id: Property = Property(name="id", type=IntegerType)
SimpleRDBMS_Column.attributes={SimpleRDBMS_Column_id, SimpleRDBMS_Column_type, SimpleRDBMS_Column_name}

# SimpleRDBMS_PKey class attributes and methods

# FKey class attributes and methods

# SimpleRDBMS_Table class attributes and methods
SimpleRDBMS_Table_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Table_id: Property = Property(name="id", type=IntegerType)
SimpleRDBMS_Table.attributes={SimpleRDBMS_Table_id, SimpleRDBMS_Table_name}

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

# Generalizations
gen_SimpleRDBMS_PKey_FKey = Generalization(general=FKey, specific=SimpleRDBMS_PKey)

# Domain Model
domain_model = DomainModel(
    name="SimpleRDBMS",
    types={SimpleRDBMS_FKey, SimpleRDBMS_Column, SimpleRDBMS_PKey, FKey, SimpleRDBMS_Table},
    associations={fkeys0, pkey1, cols3, references6, cols9},
    generalizations={gen_SimpleRDBMS_PKey_FKey},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)