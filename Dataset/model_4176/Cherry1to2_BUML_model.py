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
cherry1to2_Model = Class(name="cherry1to2::Model")
cherry1to2_Greeting = Class(name="cherry1to2::Greeting")

# cherry1to2_Model class attributes and methods

# cherry1to2_Greeting class attributes and methods
cherry1to2_Greeting_name: Property = Property(name="name", type=StringType)
cherry1to2_Greeting.attributes={cherry1to2_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="cherry1to2_Greeting", type=cherry1to2_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="cherry1to2_Model", type=cherry1to2_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="cherry1to2",
    types={cherry1to2_Model, cherry1to2_Greeting},
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