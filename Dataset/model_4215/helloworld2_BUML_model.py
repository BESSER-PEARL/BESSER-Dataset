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
helloworld2_Greeting = Class(name="helloworld2::Greeting")
helloworld2_GreetingMessage = Class(name="helloworld2::GreetingMessage")
helloworld2_Person = Class(name="helloworld2::Person")

# helloworld2_Greeting class attributes and methods

# helloworld2_GreetingMessage class attributes and methods
helloworld2_GreetingMessage_text: Property = Property(name="text", type=StringType)
helloworld2_GreetingMessage.attributes={helloworld2_GreetingMessage_text}

# helloworld2_Person class attributes and methods
helloworld2_Person_name: Property = Property(name="name", type=StringType)
helloworld2_Person.attributes={helloworld2_Person_name}

# Relationships
greetingMessage0: BinaryAssociation = BinaryAssociation(
    name="greetingMessage0",
    ends={
        Property(name="helloworld2_GreetingMessage", type=helloworld2_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld2_Greeting", type=helloworld2_GreetingMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
person1: BinaryAssociation = BinaryAssociation(
    name="person1",
    ends={
        Property(name="helloworld2_Person", type=helloworld2_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworld2_Greeting2", type=helloworld2_Person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloworld2",
    types={helloworld2_Greeting, helloworld2_GreetingMessage, helloworld2_Person},
    associations={greetingMessage0, person1},
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