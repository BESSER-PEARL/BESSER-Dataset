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
xSampleDsl_Model = Class(name="xSampleDsl::Model")
xSampleDsl_Greeting = Class(name="xSampleDsl::Greeting")

# xSampleDsl_Model class attributes and methods

# xSampleDsl_Greeting class attributes and methods
xSampleDsl_Greeting_name: Property = Property(name="name", type=StringType)
xSampleDsl_Greeting.attributes={xSampleDsl_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="xSampleDsl_Greeting", type=xSampleDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="xSampleDsl_Model", type=xSampleDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xSampleDsl",
    types={xSampleDsl_Model, xSampleDsl_Greeting},
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