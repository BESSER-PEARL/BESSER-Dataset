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
FiberTailProviderImpl = Class(name="FiberTailProviderImpl")
ServiceProviderImpl = Class(name="ServiceProviderImpl")

# FiberTailProviderImpl class attributes and methods

# ServiceProviderImpl class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_fHYv0MjvEemburp_dOaTWg",
    types={FiberTailProviderImpl, ServiceProviderImpl},
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