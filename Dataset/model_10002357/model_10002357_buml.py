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
Reptile = Class(name="Reptile", is_abstract=True)
Animal = Class(name="Animal", is_abstract=True)
Mammal = Class(name="Mammal")
Cook = Class(name="Cook")
Waiter = Class(name="Waiter")
Cashier = Class(name="Cashier")

# Reptile class attributes and methods
Reptile_attribute: Property = Property(name="attribute", type=StringType)
Reptile.attributes={Reptile_attribute}

# Animal class attributes and methods
Animal_name: Property = Property(name="name", type=StringType)
Animal.attributes={Animal_name}

# Mammal class attributes and methods

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="ab88ef8b_a5a3_4e1e_a27c_e16bdd51c96b",
    types={Reptile, Animal, Mammal, Cook, Waiter, Cashier},
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