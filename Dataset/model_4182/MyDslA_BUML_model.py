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
myDslA_Model = Class(name="myDslA::Model")
myDslA_Greeting = Class(name="myDslA::Greeting")

# myDslA_Model class attributes and methods

# myDslA_Greeting class attributes and methods
myDslA_Greeting_name: Property = Property(name="name", type=StringType)
myDslA_Greeting.attributes={myDslA_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDslA_Greeting", type=myDslA_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDslA_Model", type=myDslA_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDslA",
    types={myDslA_Model, myDslA_Greeting},
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