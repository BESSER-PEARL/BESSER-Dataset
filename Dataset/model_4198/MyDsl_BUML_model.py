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
myDsl_Greeting = Class(name="myDsl::Greeting")

# myDsl_Greeting class attributes and methods
myDsl_Greeting_name: Property = Property(name="name", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_name}

# Relationships
anotherGreeting1: BinaryAssociation = BinaryAssociation(
    name="anotherGreeting1",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Greeting0", type=myDsl_Greeting, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Greeting},
    associations={anotherGreeting1},
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