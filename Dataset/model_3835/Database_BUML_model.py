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
Database_Column = Class(name="Database::Column")
Database_DB = Class(name="Database::DB")
Database_Table = Class(name="Database::Table")

# Database_Column class attributes and methods
Database_Column_name: Property = Property(name="name", type=StringType)
Database_Column.attributes={Database_Column_name}

# Database_DB class attributes and methods
Database_DB_title: Property = Property(name="title", type=StringType)
Database_DB.attributes={Database_DB_title}

# Database_Table class attributes and methods
Database_Table_heading: Property = Property(name="heading", type=StringType)
Database_Table.attributes={Database_Table_heading}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Database_Table", type=Database_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="Database_DB", type=Database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="Database_Column", type=Database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Database_Table2", type=Database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Database",
    types={Database_Column, Database_DB, Database_Table},
    associations={tables0, columns1},
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