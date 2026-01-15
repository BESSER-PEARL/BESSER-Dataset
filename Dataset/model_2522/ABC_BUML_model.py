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
ABC_A = Class(name="ABC::A")
ABC_B = Class(name="ABC::B")
ABC_C = Class(name="ABC::C")
ABC_D = Class(name="ABC::D")

# ABC_A class attributes and methods

# ABC_B class attributes and methods

# ABC_C class attributes and methods

# ABC_D class attributes and methods

# Relationships
B0: BinaryAssociation = BinaryAssociation(
    name="B0",
    ends={
        Property(name="ABC_B", type=ABC_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_A", type=ABC_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
C1: BinaryAssociation = BinaryAssociation(
    name="C1",
    ends={
        Property(name="ABC_C", type=ABC_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_A2", type=ABC_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
D3: BinaryAssociation = BinaryAssociation(
    name="D3",
    ends={
        Property(name="ABC_D", type=ABC_B, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_B4", type=ABC_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ABC",
    types={ABC_A, ABC_B, ABC_C, ABC_D},
    associations={B0, C1, D3},
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