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
sql_Database = Class(name="sql::Database")
sql_Table = Class(name="sql::Table")
sql_Column = Class(name="sql::Column")

# sql_Database class attributes and methods
sql_Database_name: Property = Property(name="name", type=StringType)
sql_Database_TypeDB: Property = Property(name="TypeDB", type=StringType)
sql_Database.attributes={sql_Database_TypeDB, sql_Database_name}

# sql_Table class attributes and methods
sql_Table_name: Property = Property(name="name", type=StringType)
sql_Table.attributes={sql_Table_name}

# sql_Column class attributes and methods
sql_Column_name: Property = Property(name="name", type=StringType)
sql_Column_type: Property = Property(name="type", type=StringType)
sql_Column_PrimaryKey: Property = Property(name="PrimaryKey", type=BooleanType)
sql_Column.attributes={sql_Column_name, sql_Column_type, sql_Column_PrimaryKey}

# Relationships
cont0: BinaryAssociation = BinaryAssociation(
    name="cont0",
    ends={
        Property(name="sql_Table", type=sql_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Database", type=sql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contC1: BinaryAssociation = BinaryAssociation(
    name="contC1",
    ends={
        Property(name="sql_Column", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_Table2", type=sql_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_Database, sql_Table, sql_Column},
    associations={cont0, contC1},
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