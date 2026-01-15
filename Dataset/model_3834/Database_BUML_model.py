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
database_DB = Class(name="database::DB")
database_Table = Class(name="database::Table")
database_Column = Class(name="database::Column")

# database_DB class attributes and methods

# database_Table class attributes and methods

# database_Column class attributes and methods

# Relationships
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="database_Table", type=database_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="database_DB", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column1: BinaryAssociation = BinaryAssociation(
    name="column1",
    ends={
        Property(name="database_Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table2", type=database_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="database_Table5", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column4", type=database_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_DB, database_Table, database_Column},
    associations={table0, column1, reference3},
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