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
People = Class(name="People", is_abstract=True)
Customer = Class(name="Customer")
Cook = Class(name="Cook")
Waiter = Class(name="Waiter")
Cashier = Class(name="Cashier")
Worker = Class(name="Worker", is_abstract=True)

# People class attributes and methods
People_name: Property = Property(name="name", type=StringType)
People.attributes={People_name}

# Customer class attributes and methods

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Worker class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_01a633d1_e68f_42c5_9bfe_20c3f305238c",
    types={People, Customer, Cook, Waiter, Cashier, Worker},
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