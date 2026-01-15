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
lexertrace_Model = Class(name="lexertrace::Model")
lexertrace_Greeting = Class(name="lexertrace::Greeting")

# lexertrace_Model class attributes and methods

# lexertrace_Greeting class attributes and methods
lexertrace_Greeting_name: Property = Property(name="name", type=StringType)
lexertrace_Greeting.attributes={lexertrace_Greeting_name}

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="lexertrace_Greeting", type=lexertrace_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="lexertrace_Model", type=lexertrace_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="lexertrace",
    types={lexertrace_Model, lexertrace_Greeting},
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