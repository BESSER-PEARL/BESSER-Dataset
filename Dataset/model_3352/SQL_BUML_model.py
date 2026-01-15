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
DB_Database = Class(name="DB::Database")
DB_Table = Class(name="DB::Table")
DB_Column = Class(name="DB::Column")

# DB_Database class attributes and methods
DB_Database_Name: Property = Property(name="Name", type=StringType)
DB_Database.attributes={DB_Database_Name}

# DB_Table class attributes and methods
DB_Table_Name: Property = Property(name="Name", type=StringType)
DB_Table.attributes={DB_Table_Name}

# DB_Column class attributes and methods
DB_Column_Name: Property = Property(name="Name", type=StringType)
DB_Column.attributes={DB_Column_Name}

# Relationships
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="DB_Table", type=DB_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Database", type=DB_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column1: BinaryAssociation = BinaryAssociation(
    name="column1",
    ends={
        Property(name="DB_Column", type=DB_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DB_Table2", type=DB_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="DB",
    types={DB_Database, DB_Table, DB_Column},
    associations={table0, column1},
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