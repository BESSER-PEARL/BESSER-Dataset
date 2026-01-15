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
evlDSL_Model = Class(name="evlDSL::Model")
evlDSL_Greeting = Class(name="evlDSL::Greeting")

# evlDSL_Model class attributes and methods

# evlDSL_Greeting class attributes and methods
evlDSL_Greeting_name: Property = Property(name="name", type=StringType)
evlDSL_Greeting.attributes={evlDSL_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="evlDSL_Greeting", type=evlDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="evlDSL_Model", type=evlDSL_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="evlDSL",
    types={evlDSL_Model, evlDSL_Greeting},
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