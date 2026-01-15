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
database_Scheme = Class(name="database::Scheme")
database_Table = Class(name="database::Table")
database_Column = Class(name="database::Column")

# database_Scheme class attributes and methods
database_Scheme_name: Property = Property(name="name", type=StringType)
database_Scheme.attributes={database_Scheme_name}

# database_Table class attributes and methods
database_Table_name: Property = Property(name="name", type=StringType)
database_Table.attributes={database_Table_name}

# database_Column class attributes and methods
database_Column_name: Property = Property(name="name", type=StringType)
database_Column_type: Property = Property(name="type", type=StringType)
database_Column_NotNull: Property = Property(name="NotNull", type=BooleanType)
database_Column_PrimaryKey: Property = Property(name="PrimaryKey", type=BooleanType)
database_Column.attributes={database_Column_PrimaryKey, database_Column_name, database_Column_NotNull, database_Column_type}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="database_Table", type=database_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Scheme", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="database_Column", type=database_Scheme, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Scheme2", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table4: BinaryAssociation = BinaryAssociation(
    name="table4",
    ends={
        Property(name="Table", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=database_Table, multiplicity=Multiplicity(0, 1))
    }
)
fk6: BinaryAssociation = BinaryAssociation(
    name="fk6",
    ends={
        Property(name="database_Column7", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column5", type=database_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_Scheme, database_Table, database_Column},
    associations={tables0, columns1, columns3, table4, fk6},
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