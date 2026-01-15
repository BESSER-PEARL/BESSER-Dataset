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
myDsl2_Model = Class(name="myDsl2::Model")
myDsl2_Greeting = Class(name="myDsl2::Greeting")

# myDsl2_Model class attributes and methods

# myDsl2_Greeting class attributes and methods
myDsl2_Greeting_name: Property = Property(name="name", type=StringType)
myDsl2_Greeting.attributes={myDsl2_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl2_Greeting", type=myDsl2_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl2_Model", type=myDsl2_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl2",
    types={myDsl2_Model, myDsl2_Greeting},
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