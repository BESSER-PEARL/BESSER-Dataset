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
anyaBasic_Model = Class(name="anyaBasic::Model")
anyaBasic_Greeting = Class(name="anyaBasic::Greeting")

# anyaBasic_Model class attributes and methods

# anyaBasic_Greeting class attributes and methods
anyaBasic_Greeting_name: Property = Property(name="name", type=StringType)
anyaBasic_Greeting.attributes={anyaBasic_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="anyaBasic_Greeting", type=anyaBasic_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="anyaBasic_Model", type=anyaBasic_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="anyaBasic",
    types={anyaBasic_Model, anyaBasic_Greeting},
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