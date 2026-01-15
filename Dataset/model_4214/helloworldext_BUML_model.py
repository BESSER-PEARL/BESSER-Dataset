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
helloworldext_GreetingMessage = Class(name="helloworldext::GreetingMessage")
helloworldext_Person = Class(name="helloworldext::Person")
helloworldext_Greeting = Class(name="helloworldext::Greeting")

# helloworldext_GreetingMessage class attributes and methods
helloworldext_GreetingMessage_text: Property = Property(name="text", type=StringType)
helloworldext_GreetingMessage.attributes={helloworldext_GreetingMessage_text}

# helloworldext_Person class attributes and methods
helloworldext_Person_name: Property = Property(name="name", type=StringType)
helloworldext_Person.attributes={helloworldext_Person_name}

# helloworldext_Greeting class attributes and methods

# Relationships
greetingMessage0: BinaryAssociation = BinaryAssociation(
    name="greetingMessage0",
    ends={
        Property(name="helloworldext_GreetingMessage", type=helloworldext_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworldext_Greeting", type=helloworldext_GreetingMessage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
person1: BinaryAssociation = BinaryAssociation(
    name="person1",
    ends={
        Property(name="helloworldext_Person", type=helloworldext_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="helloworldext_Greeting2", type=helloworldext_Person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloworldext",
    types={helloworldext_GreetingMessage, helloworldext_Person, helloworldext_Greeting},
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