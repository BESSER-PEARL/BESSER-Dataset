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
Cook = Class(name="Cook")
Waiter = Class(name="Waiter")
Cashier = Class(name="Cashier")
Worker = Class(name="Worker", is_abstract=True)
People = Class(name="People", is_abstract=True)
Customer = Class(name="Customer")

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Worker class attributes and methods

# People class attributes and methods
People_name: Property = Property(name="name", type=StringType)
People.attributes={People_name}

# Customer class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_4778147e_8c3b_4bfb_8751_814b42af9277",
    types={Cook, Waiter, Cashier, Worker, People, Customer},
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