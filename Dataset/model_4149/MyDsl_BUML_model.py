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
myDsl_Model = Class(name="myDsl_Model")
myDsl_AbstractGreeting = Class(name="myDsl_AbstractGreeting")
myDsl_Greeting = Class(name="myDsl_Greeting")
AbstractGreeting = Class(name="AbstractGreeting")
myDsl_GreetingReference = Class(name="myDsl_GreetingReference")

# myDsl_Model class attributes and methods

# myDsl_AbstractGreeting class attributes and methods
myDsl_AbstractGreeting_name: Property = Property(name="name", type=StringType)
myDsl_AbstractGreeting.attributes={myDsl_AbstractGreeting_name}

# myDsl_Greeting class attributes and methods

# AbstractGreeting class attributes and methods

# myDsl_GreetingReference class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_AbstractGreeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_AbstractGreeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
greeting1: BinaryAssociation = BinaryAssociation(
    name="greeting1",
    ends={
        Property(name="myDsl_AbstractGreeting2", type=myDsl_GreetingReference, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GreetingReference", type=myDsl_AbstractGreeting, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_Greeting_AbstractGreeting = Generalization(general=AbstractGreeting, specific=myDsl_Greeting)
gen_myDsl_GreetingReference_AbstractGreeting = Generalization(general=AbstractGreeting, specific=myDsl_GreetingReference)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_AbstractGreeting, myDsl_Greeting, AbstractGreeting, myDsl_GreetingReference},
    associations={greetings0, greeting1},
    generalizations={gen_myDsl_Greeting_AbstractGreeting, gen_myDsl_GreetingReference_AbstractGreeting},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)