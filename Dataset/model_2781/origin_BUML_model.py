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
p_A = Class(name="p::A")
p_B = Class(name="p::B")
p_C = Class(name="p::C")

# p_A class attributes and methods
p_A_name: Property = Property(name="name", type=StringType)
p_A.attributes={p_A_name}

# p_B class attributes and methods

# p_C class attributes and methods

# Relationships
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="p_B", type=p_A, multiplicity=Multiplicity(1, 1)),
        Property(name="p_A", type=p_B, multiplicity=Multiplicity(0, 1))
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="p_A5", type=p_C, multiplicity=Multiplicity(1, 1)),
        Property(name="p_C4", type=p_A, multiplicity=Multiplicity(0, 1))
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="p_C", type=p_B, multiplicity=Multiplicity(1, 1)),
        Property(name="p_B2", type=p_C, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="p",
    types={p_A, p_B, p_C},
    associations={a0, c3, b1},
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