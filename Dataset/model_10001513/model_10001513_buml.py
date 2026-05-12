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
Customer = Class(name="Customer")
Cook = Class(name="Cook")
Waiter = Class(name="Waiter")
Cashier = Class(name="Cashier")
Class_ = Class(name="Class")
Class2 = Class(name="Class2")
Class3 = Class(name="Class3")
Class4 = Class(name="Class4")
Interface_Interface = Class(name="Interface_Interface")

# Worker class attributes and methods

# People class attributes and methods
People_name: Property = Property(name="name", type=StringType)
People.attributes={People_name}

# Customer class attributes and methods

# Cook class attributes and methods

# Waiter class attributes and methods

# Cashier class attributes and methods

# Class class attributes and methods
Class__attribute: Property = Property(name="attribute", type=StringType)
Class_.attributes={Class__attribute}

# Class2 class attributes and methods

# Class3 class attributes and methods

# Class4 class attributes and methods

# Interface_Interface class attributes and methods

# Relationships
Class2_Class4: BinaryAssociation = BinaryAssociation(
    name="Class2_Class4",
    ends={
        Property(name="class40", type=Class4, multiplicity=Multiplicity(0, 1)),
        Property(name="class21", type=Class2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_CPNAoEwiEeqonN_RS9oRzw",
    types={Worker, People, Customer, Cook, Waiter, Cashier, Class_, Class2, Class3, Class4, Interface_Interface},
    associations={Class2_Class4},
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