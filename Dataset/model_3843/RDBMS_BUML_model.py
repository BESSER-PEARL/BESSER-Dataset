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
RDBMS_Schema = Class(name="RDBMS::Schema")
RDBMS_Table = Class(name="RDBMS::Table")
RDBMS_Column = Class(name="RDBMS::Column")
RDBMS_ForeignKey = Class(name="RDBMS::ForeignKey")

# RDBMS_Schema class attributes and methods
RDBMS_Schema_name: Property = Property(name="name", type=StringType)
RDBMS_Schema.attributes={RDBMS_Schema_name}

# RDBMS_Table class attributes and methods
RDBMS_Table_name: Property = Property(name="name", type=StringType)
RDBMS_Table_is_local: Property = Property(name="is_local", type=BooleanType)
RDBMS_Table.attributes={RDBMS_Table_is_local, RDBMS_Table_name}

# RDBMS_Column class attributes and methods
RDBMS_Column_name: Property = Property(name="name", type=StringType)
RDBMS_Column_type: Property = Property(name="type", type=StringType)
RDBMS_Column.attributes={RDBMS_Column_type, RDBMS_Column_name}

# RDBMS_ForeignKey class attributes and methods

# Relationships
cols8: BinaryAssociation = BinaryAssociation(
    name="cols8",
    ends={
        Property(name="RDBMS_Column10", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_ForeignKey9", type=RDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)
references11: BinaryAssociation = BinaryAssociation(
    name="references11",
    ends={
        Property(name="RDBMS_Table13", type=RDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_ForeignKey12", type=RDBMS_Table, multiplicity=Multiplicity(1, 1))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="RDBMS_Table", type=RDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Schema", type=RDBMS_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols1: BinaryAssociation = BinaryAssociation(
    name="cols1",
    ends={
        Property(name="RDBMS_Column", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table2", type=RDBMS_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fkeys3: BinaryAssociation = BinaryAssociation(
    name="fkeys3",
    ends={
        Property(name="RDBMS_ForeignKey", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table4", type=RDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey5: BinaryAssociation = BinaryAssociation(
    name="pkey5",
    ends={
        Property(name="RDBMS_Column7", type=RDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="RDBMS_Table6", type=RDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="RDBMS",
    types={RDBMS_Schema, RDBMS_Table, RDBMS_Column, RDBMS_ForeignKey},
    associations={cols8, references11, tables0, cols1, fkeys3, pkey5},
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