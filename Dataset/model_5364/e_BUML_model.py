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
e_E = Class(name="e::E")
e_D = Class(name="e::D")
e_F = Class(name="e::F")

# e_E class attributes and methods

# e_D class attributes and methods

# e_F class attributes and methods

# Relationships
d0: BinaryAssociation = BinaryAssociation(
    name="d0",
    ends={
        Property(name="e_D", type=e_E, multiplicity=Multiplicity(1, 1)),
        Property(name="e_E", type=e_D, multiplicity=Multiplicity(0, 1))
    }
)
f1: BinaryAssociation = BinaryAssociation(
    name="f1",
    ends={
        Property(name="e_F", type=e_E, multiplicity=Multiplicity(1, 1)),
        Property(name="e_E2", type=e_F, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e",
    types={e_E, e_D, e_F},
    associations={d0, f1},
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