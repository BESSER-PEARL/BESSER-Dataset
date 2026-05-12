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
Class_ = Class(name="Class")
Interface_Interface = Class(name="Interface_Interface")
Actor_Actor = Class(name="Actor_Actor")

# Class class attributes and methods

# Interface_Interface class attributes and methods

# Actor_Actor class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_NOio8IlgEeq3N_Xh6gsEIQ",
    types={Class_, Interface_Interface, Actor_Actor},
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