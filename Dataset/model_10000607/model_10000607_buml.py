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
People_Custumer_: Property = Property(name="Custumer_", type=StringType)
People_Worker: Property = Property(name="Worker", type=StringType)
People.attributes={People_Worker, People_name, People_Custumer_}

# Customer class attributes and methods

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Worker class attributes and methods
Worker_Cook: Property = Property(name="Cook", type=StringType)
Worker_Waitor: Property = Property(name="Waitor", type=StringType)
Worker_Cashier: Property = Property(name="Cashier", type=StringType)
Worker.attributes={Worker_Cashier, Worker_Waitor, Worker_Cook}

# Domain Model
domain_model = DomainModel(
    name="_4a34621e_5f07_45da_b69d_96d21f223979",
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