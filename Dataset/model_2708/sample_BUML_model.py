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
strictSample_A = Class(name="strictSample::A")
strictSample_B = Class(name="strictSample::B")
strictSample_C = Class(name="strictSample::C")
strictSample_D = Class(name="strictSample::D")

# strictSample_A class attributes and methods
strictSample_A_a: Property = Property(name="a", type=StringType)
strictSample_A.attributes={strictSample_A_a}

# strictSample_B class attributes and methods
strictSample_B_b: Property = Property(name="b", type=StringType)
strictSample_B.attributes={strictSample_B_b}

# strictSample_C class attributes and methods

# strictSample_D class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="strictSample_B", type=strictSample_A, multiplicity=Multiplicity(1, 1)),
        Property(name="strictSample_A", type=strictSample_B, multiplicity=Multiplicity(1, 9999))
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="strictSample_C", type=strictSample_B, multiplicity=Multiplicity(1, 1)),
        Property(name="strictSample_B2", type=strictSample_C, multiplicity=Multiplicity(1, 9999))
    }
)
d3: BinaryAssociation = BinaryAssociation(
    name="d3",
    ends={
        Property(name="strictSample_D", type=strictSample_B, multiplicity=Multiplicity(1, 1)),
        Property(name="strictSample_B4", type=strictSample_D, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="strictSample",
    types={strictSample_A, strictSample_B, strictSample_C, strictSample_D},
    associations={bs0, cs1, d3},
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