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
noJdt_Model = Class(name="noJdt::Model")
noJdt_Greeting = Class(name="noJdt::Greeting")

# noJdt_Model class attributes and methods

# noJdt_Greeting class attributes and methods
noJdt_Greeting_name: Property = Property(name="name", type=StringType)
noJdt_Greeting.attributes={noJdt_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="noJdt_Greeting", type=noJdt_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="noJdt_Model", type=noJdt_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
other2: BinaryAssociation = BinaryAssociation(
    name="other2",
    ends={
        Property(name="noJdt_Greeting3", type=noJdt_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="noJdt_Greeting1", type=noJdt_Greeting, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="noJdt",
    types={noJdt_Model, noJdt_Greeting},
    associations={greetings0, other2},
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