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
comp_Model = Class(name="comp::Model")
comp_Greeting = Class(name="comp::Greeting")

# comp_Model class attributes and methods

# comp_Greeting class attributes and methods
comp_Greeting_name: Property = Property(name="name", type=StringType)
comp_Greeting.attributes={comp_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="comp_Greeting", type=comp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="comp_Model", type=comp_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="comp",
    types={comp_Model, comp_Greeting},
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