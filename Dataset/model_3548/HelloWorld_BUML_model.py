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
helloworld_HelloWorld = Class(name="helloworld::HelloWorld")

# helloworld_HelloWorld class attributes and methods
helloworld_HelloWorld_m_greeting: Method = Method(name="greeting", parameters={}, type=StringType)
helloworld_HelloWorld.methods={helloworld_HelloWorld_m_greeting}

# Domain Model
domain_model = DomainModel(
    name="helloworld",
    types={helloworld_HelloWorld},
    associations={},
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