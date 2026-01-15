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
helloWorld_Model = Class(name="helloWorld::Model")
helloWorld_Greeting = Class(name="helloWorld::Greeting")
helloWorld_KeywordsExample = Class(name="helloWorld::KeywordsExample")

# helloWorld_Model class attributes and methods

# helloWorld_Greeting class attributes and methods
helloWorld_Greeting_name: Property = Property(name="name", type=StringType)
helloWorld_Greeting.attributes={helloWorld_Greeting_name}

# helloWorld_KeywordsExample class attributes and methods
helloWorld_KeywordsExample_option: Property = Property(name="option", type=StringType)
helloWorld_KeywordsExample.attributes={helloWorld_KeywordsExample_option}

# Relationships
keywordsExample1: BinaryAssociation = BinaryAssociation(
    name="keywordsExample1",
    ends={
        Property(name="helloWorld_KeywordsExample", type=helloWorld_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="helloWorld_Model2", type=helloWorld_KeywordsExample, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="helloWorld_Greeting", type=helloWorld_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="helloWorld_Model", type=helloWorld_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="helloWorld",
    types={helloWorld_Model, helloWorld_Greeting, helloWorld_KeywordsExample},
    associations={keywordsExample1, greetings0},
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