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
c_C = Class(name="c::C")
c_D = Class(name="c::D")

# c_C class attributes and methods

# c_D class attributes and methods

# Relationships
d0: BinaryAssociation = BinaryAssociation(
    name="d0",
    ends={
        Property(name="c_D", type=c_C, multiplicity=Multiplicity(1, 1)),
        Property(name="c_C", type=c_D, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c",
    types={c_C, c_D},
    associations={d0},
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