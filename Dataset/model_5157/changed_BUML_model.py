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
depcycle_A = Class(name="depcycle::A")
depcycle_B = Class(name="depcycle::B")

# depcycle_A class attributes and methods

# depcycle_B class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="depcycle_B", type=depcycle_A, multiplicity=Multiplicity(1, 1)),
        Property(name="depcycle_A", type=depcycle_B, multiplicity=Multiplicity(0, 1))
    }
)
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="depcycle_A3", type=depcycle_B, multiplicity=Multiplicity(1, 1)),
        Property(name="depcycle_B2", type=depcycle_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="depcycle",
    types={depcycle_A, depcycle_B},
    associations={b0, a1},
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