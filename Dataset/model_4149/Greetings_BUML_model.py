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
greetings_Model = Class(name="greetings::Model")
greetings_Greeting = Class(name="greetings::Greeting")
greetings_HelloGreeting = Class(name="greetings::HelloGreeting")
Greeting = Class(name="Greeting")
greetings_RefGreeting = Class(name="greetings::RefGreeting")

# greetings_Model class attributes and methods

# greetings_Greeting class attributes and methods

# greetings_HelloGreeting class attributes and methods
greetings_HelloGreeting_name: Property = Property(name="name", type=StringType)
greetings_HelloGreeting.attributes={greetings_HelloGreeting_name}

# Greeting class attributes and methods

# greetings_RefGreeting class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="greetings_Greeting", type=greetings_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="greetings_Model", type=greetings_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="greetings_HelloGreeting", type=greetings_HelloGreeting, multiplicity=Multiplicity(1, 1)),
        Property(name="greetings_HelloGreeting1", type=greetings_HelloGreeting, multiplicity=Multiplicity(0, 1))
    }
)
greeting3: BinaryAssociation = BinaryAssociation(
    name="greeting3",
    ends={
        Property(name="greetings_HelloGreeting4", type=greetings_RefGreeting, multiplicity=Multiplicity(1, 1)),
        Property(name="greetings_RefGreeting", type=greetings_HelloGreeting, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_greetings_HelloGreeting_Greeting = Generalization(general=Greeting, specific=greetings_HelloGreeting)
gen_greetings_RefGreeting_Greeting = Generalization(general=Greeting, specific=greetings_RefGreeting)

# Domain Model
domain_model = DomainModel(
    name="greetings",
    types={greetings_Model, greetings_Greeting, greetings_HelloGreeting, Greeting, greetings_RefGreeting},
    associations={greetings0, parent2, greeting3},
    generalizations={gen_greetings_HelloGreeting_Greeting, gen_greetings_RefGreeting_Greeting},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)