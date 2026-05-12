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
Actor_Actor = Class(name="Actor_Actor")
Class_ = Class(name="Class")
Interface_Interface = Class(name="Interface_Interface")
Package_Class = Class(name="Package_Class")
Class2 = Class(name="Class2")
Class3 = Class(name="Class3")

# Actor_Actor class attributes and methods

# Class class attributes and methods

# Interface_Interface class attributes and methods

# Package_Class class attributes and methods

# Class2 class attributes and methods

# Class3 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_oE4JgIlxEeq3N_Xh6gsEIQ",
    types={Actor_Actor, Class_, Interface_Interface, Package_Class, Class2, Class3},
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