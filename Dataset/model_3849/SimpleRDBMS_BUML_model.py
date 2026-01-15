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
SimpleRDBMS_Table = Class(name="SimpleRDBMS::Table")
Column = Class(name="Column")
FKey = Class(name="FKey")
SimpleRDBMS_Column = Class(name="SimpleRDBMS::Column")
SimpleRDBMS_FKey = Class(name="SimpleRDBMS::FKey")
Table = Class(name="Table")

# SimpleRDBMS_Table class attributes and methods
SimpleRDBMS_Table_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Table_tipo: Property = Property(name="tipo", type=StringType)
SimpleRDBMS_Table.attributes={SimpleRDBMS_Table_name, SimpleRDBMS_Table_tipo}

# Column class attributes and methods

# FKey class attributes and methods

# SimpleRDBMS_Column class attributes and methods
SimpleRDBMS_Column_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_Column_type: Property = Property(name="type", type=StringType)
SimpleRDBMS_Column.attributes={SimpleRDBMS_Column_name, SimpleRDBMS_Column_type}

# SimpleRDBMS_FKey class attributes and methods

# Table class attributes and methods

# Relationships
fkeys0: BinaryAssociation = BinaryAssociation(
    name="fkeys0",
    ends={
        Property(name="FKey", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table", type=FKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey1: BinaryAssociation = BinaryAssociation(
    name="pkey1",
    ends={
        Property(name="Column", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table2", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
cols3: BinaryAssociation = BinaryAssociation(
    name="cols3",
    ends={
        Property(name="Column5", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_Table4", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="Table", type=SimpleRDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_FKey", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
cols7: BinaryAssociation = BinaryAssociation(
    name="cols7",
    ends={
        Property(name="Column9", type=SimpleRDBMS_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_FKey8", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="SimpleRDBMS",
    types={SimpleRDBMS_Table, Column, FKey, SimpleRDBMS_Column, SimpleRDBMS_FKey, Table},
    associations={fkeys0, pkey1, cols3, references6, cols7},
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