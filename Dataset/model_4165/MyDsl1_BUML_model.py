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
myDsl1_Model = Class(name="myDsl1::Model")
myDsl1_Greeting = Class(name="myDsl1::Greeting")

# myDsl1_Model class attributes and methods

# myDsl1_Greeting class attributes and methods
myDsl1_Greeting_name: Property = Property(name="name", type=StringType)
myDsl1_Greeting.attributes={myDsl1_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl1_Greeting", type=myDsl1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl1_Model", type=myDsl1_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl1",
    types={myDsl1_Model, myDsl1_Greeting},
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