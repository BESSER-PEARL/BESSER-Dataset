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
ddl_Schema = Class(name="ddl::Schema")
DataElement = Class(name="DataElement")
ddl_Table = Class(name="ddl::Table")
ddl_DataType = Class(name="ddl::DataType")
ddl_Column = Class(name="ddl::Column")
ddl_DataElement = Class(name="ddl::DataElement")

# ddl_Schema class attributes and methods

# DataElement class attributes and methods

# ddl_Table class attributes and methods

# ddl_DataType class attributes and methods

# ddl_Column class attributes and methods

# ddl_DataElement class attributes and methods
ddl_DataElement_name: Property = Property(name="name", type=StringType)
ddl_DataElement.attributes={ddl_DataElement_name}

# Relationships
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="ddl_Table", type=ddl_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="ddl_Schema", type=ddl_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="ddl_DataType", type=ddl_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="ddl_Schema2", type=ddl_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column3: BinaryAssociation = BinaryAssociation(
    name="column3",
    ends={
        Property(name="ddl_Column", type=ddl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ddl_Table4", type=ddl_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="ddl_DataType7", type=ddl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ddl_Column6", type=ddl_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ddl_Schema_DataElement = Generalization(general=DataElement, specific=ddl_Schema)
gen_ddl_Table_DataElement = Generalization(general=DataElement, specific=ddl_Table)
gen_ddl_Column_DataElement = Generalization(general=DataElement, specific=ddl_Column)
gen_ddl_DataType_DataElement = Generalization(general=DataElement, specific=ddl_DataType)

# Domain Model
domain_model = DomainModel(
    name="ddl",
    types={ddl_Schema, DataElement, ddl_Table, ddl_DataType, ddl_Column, ddl_DataElement},
    associations={table0, types1, column3, type5},
    generalizations={gen_ddl_Schema_DataElement, gen_ddl_Table_DataElement, gen_ddl_Column_DataElement, gen_ddl_DataType_DataElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)