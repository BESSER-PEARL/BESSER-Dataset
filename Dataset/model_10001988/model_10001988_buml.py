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
Admin_Actor = Class(name="Admin_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
T = Class(name="T")

# Admin_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# T class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_i3BN0D_fEeiQnZ20ckwjYw",
    types={Admin_Actor, UseCase_UseCase, T},
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