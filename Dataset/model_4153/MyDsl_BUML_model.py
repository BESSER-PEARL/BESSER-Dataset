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
mydsl_Model = Class(name="mydsl::Model")
mydsl_Greeting = Class(name="mydsl::Greeting")

# mydsl_Model class attributes and methods

# mydsl_Greeting class attributes and methods
mydsl_Greeting_name: Property = Property(name="name", type=StringType)
mydsl_Greeting.attributes={mydsl_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="mydsl_Greeting", type=mydsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_Model", type=mydsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_Model, mydsl_Greeting},
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