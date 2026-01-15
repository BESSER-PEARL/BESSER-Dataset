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
minimalref_A = Class(name="minimalref::A")
minimalref_B = Class(name="minimalref::B")

# minimalref_A class attributes and methods

# minimalref_B class attributes and methods

# Relationships
manyB0: BinaryAssociation = BinaryAssociation(
    name="manyB0",
    ends={
        Property(name="B", type=minimalref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="parentA", type=minimalref_B, multiplicity=Multiplicity(0, 9999))
    }
)
parentA1: BinaryAssociation = BinaryAssociation(
    name="parentA1",
    ends={
        Property(name="A", type=minimalref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="manyB", type=minimalref_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="minimalref",
    types={minimalref_A, minimalref_B},
    associations={manyB0, parentA1},
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