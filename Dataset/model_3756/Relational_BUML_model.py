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
Relational_Column = Class(name="Relational::Column")
Relational_Table = Class(name="Relational::Table")

# Relational_Column class attributes and methods
Relational_Column_id: Property = Property(name="id", type=StringType)
Relational_Column_name: Property = Property(name="name", type=StringType)
Relational_Column.attributes={Relational_Column_name, Relational_Column_id}

# Relational_Table class attributes and methods
Relational_Table_id: Property = Property(name="id", type=StringType)
Relational_Table_name: Property = Property(name="name", type=StringType)
Relational_Table.attributes={Relational_Table_id, Relational_Table_name}

# Relationships
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="Column", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=Relational_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference1: BinaryAssociation = BinaryAssociation(
    name="reference1",
    ends={
        Property(name="Table", type=Relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Relational_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Relational",
    types={Relational_Column, Relational_Table},
    associations={columns0, reference1},
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