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

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_7b1598ec_cbba_4588_8610_86e9ae0ffcc2",
    types={Cook, Waiter, Cashier},
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