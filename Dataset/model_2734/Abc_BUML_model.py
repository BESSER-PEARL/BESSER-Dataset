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
abc_C = Class(name="abc::C")
abc_B = Class(name="abc::B")
abc_A = Class(name="abc::A")

# abc_C class attributes and methods
abc_C_x: Property = Property(name="x", type=IntegerType)
abc_C.attributes={abc_C_x}

# abc_B class attributes and methods
abc_B_x: Property = Property(name="x", type=IntegerType)
abc_B.attributes={abc_B_x}

# abc_A class attributes and methods
abc_A_x: Property = Property(name="x", type=IntegerType)
abc_A.attributes={abc_A_x}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="abc_B", type=abc_C, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_C", type=abc_B, multiplicity=Multiplicity(0, 9999))
    }
)
a5: BinaryAssociation = BinaryAssociation(
    name="a5",
    ends={
        Property(name="7", type=abc_B, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=abc_A, multiplicity=Multiplicity(0, 9999))
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="2", type=abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=abc_B, multiplicity=Multiplicity(0, 9999))
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="abc_C4", type=abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_A", type=abc_C, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="abc",
    types={abc_C, abc_B, abc_A},
    associations={b0, a5, b1, c3},
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