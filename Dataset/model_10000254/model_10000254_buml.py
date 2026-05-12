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
Event = Class(name="Event", is_abstract=True)
Customer = Class(name="Customer")
Cook = Class(name="Cook")
Waiter = Class(name="Waiter")
Cashier = Class(name="Cashier")

# Worker class attributes and methods

# Event class attributes and methods
Event_created_at: Property = Property(name="created_at", type=FloatType)
Event_entity: Property = Property(name="entity", type=StringType)
Event.attributes={Event_created_at, Event_entity}

# Customer class attributes and methods

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_1fb728e6_9930_4157_9927_04d1592e6a63",
    types={Worker, Event, Customer, Cook, Waiter, Cashier},
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