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
greetings_GreetingsModel = Class(name="greetings::GreetingsModel")
greetings_Greeting = Class(name="greetings::Greeting")

# greetings_GreetingsModel class attributes and methods

# greetings_Greeting class attributes and methods
greetings_Greeting_name: Property = Property(name="name", type=StringType)
greetings_Greeting.attributes={greetings_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="greetings_Greeting", type=greetings_GreetingsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="greetings_GreetingsModel", type=greetings_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="greetings",
    types={greetings_GreetingsModel, greetings_Greeting},
    associations={greetings0},
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