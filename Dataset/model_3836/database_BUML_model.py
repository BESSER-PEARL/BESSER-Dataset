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
database_Column = Class(name="database::Column")
database_ForeignKey = Class(name="database::ForeignKey")
database_Schema = Class(name="database::Schema")
database_Table = Class(name="database::Table")

# database_Column class attributes and methods
database_Column_type: Property = Property(name="type", type=StringType)
database_Column_name: Property = Property(name="name", type=StringType)
database_Column.attributes={database_Column_name, database_Column_type}

# database_ForeignKey class attributes and methods

# database_Schema class attributes and methods
database_Schema_name: Property = Property(name="name", type=StringType)
database_Schema.attributes={database_Schema_name}

# database_Table class attributes and methods
database_Table_name: Property = Property(name="name", type=StringType)
database_Table_is_local: Property = Property(name="is_local", type=BooleanType)
database_Table.attributes={database_Table_is_local, database_Table_name}

# Relationships
cols1: BinaryAssociation = BinaryAssociation(
    name="cols1",
    ends={
        Property(name="database_Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table2", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fkeys3: BinaryAssociation = BinaryAssociation(
    name="fkeys3",
    ends={
        Property(name="database_ForeignKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table4", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkey5: BinaryAssociation = BinaryAssociation(
    name="pkey5",
    ends={
        Property(name="database_Column7", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table6", type=database_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="database_Table", type=database_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Schema", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cols8: BinaryAssociation = BinaryAssociation(
    name="cols8",
    ends={
        Property(name="database_Column10", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey9", type=database_Column, multiplicity=Multiplicity(0, 9999))
    }
)
references11: BinaryAssociation = BinaryAssociation(
    name="references11",
    ends={
        Property(name="database_Table13", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey12", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_Column, database_ForeignKey, database_Schema, database_Table},
    associations={cols1, fkeys3, pkey5, tables0, cols8, references11},
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