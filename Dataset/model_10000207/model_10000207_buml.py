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
Worker = Class(name="Worker", is_abstract=True)
People = Class(name="People", is_abstract=True)
VOTER = Class(name="VOTER")
ADMIN = Class(name="ADMIN")
SYSTEM = Class(name="SYSTEM")
Cashier = Class(name="Cashier")

# Worker class attributes and methods

# People class attributes and methods
People_name: Property = Property(name="name", type=StringType)
People.attributes={People_name}

# VOTER class attributes and methods

# ADMIN class attributes and methods

# SYSTEM class attributes and methods

# Cashier class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_19a55228_e018_4e4d_8b44_1a546d039aae",
    types={Worker, People, VOTER, ADMIN, SYSTEM, Cashier},
    associations={},
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