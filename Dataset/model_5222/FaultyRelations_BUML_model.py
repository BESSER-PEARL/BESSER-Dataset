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
FaultyRelations_A = Class(name="FaultyRelations::A")
FaultyRelations_B = Class(name="FaultyRelations::B")
FaultyRelations_C = Class(name="FaultyRelations::C")

# FaultyRelations_A class attributes and methods
FaultyRelations_A_v: Property = Property(name="v", type=IntegerType)
FaultyRelations_A_w: Property = Property(name="w", type=BooleanType)
FaultyRelations_A.attributes={FaultyRelations_A_w, FaultyRelations_A_v}

# FaultyRelations_B class attributes and methods
FaultyRelations_B_x: Property = Property(name="x", type=IntegerType)
FaultyRelations_B_y: Property = Property(name="y", type=IntegerType)
FaultyRelations_B.attributes={FaultyRelations_B_y, FaultyRelations_B_x}

# FaultyRelations_C class attributes and methods
FaultyRelations_C_u: Property = Property(name="u", type=IntegerType)
FaultyRelations_C.attributes={FaultyRelations_C_u}

# Relationships
AB0: BinaryAssociation = BinaryAssociation(
    name="AB0",
    ends={
        Property(name="B", type=FaultyRelations_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BA", type=FaultyRelations_B, multiplicity=Multiplicity(5, 5))
    }
)
AC1: BinaryAssociation = BinaryAssociation(
    name="AC1",
    ends={
        Property(name="C", type=FaultyRelations_A, multiplicity=Multiplicity(1, 1)),
        Property(name="CA", type=FaultyRelations_C, multiplicity=Multiplicity(1, 1))
    }
)
BA2: BinaryAssociation = BinaryAssociation(
    name="BA2",
    ends={
        Property(name="A", type=FaultyRelations_B, multiplicity=Multiplicity(1, 1)),
        Property(name="AB", type=FaultyRelations_A, multiplicity=Multiplicity(2, 2))
    }
)
BC3: BinaryAssociation = BinaryAssociation(
    name="BC3",
    ends={
        Property(name="C4", type=FaultyRelations_B, multiplicity=Multiplicity(1, 1)),
        Property(name="CB", type=FaultyRelations_C, multiplicity=Multiplicity(3, 3))
    }
)
CA5: BinaryAssociation = BinaryAssociation(
    name="CA5",
    ends={
        Property(name="A6", type=FaultyRelations_C, multiplicity=Multiplicity(1, 1)),
        Property(name="AC", type=FaultyRelations_A, multiplicity=Multiplicity(2, 2))
    }
)
CB7: BinaryAssociation = BinaryAssociation(
    name="CB7",
    ends={
        Property(name="B8", type=FaultyRelations_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BC", type=FaultyRelations_B, multiplicity=Multiplicity(5, 5))
    }
)

# Domain Model
domain_model = DomainModel(
    name="FaultyRelations",
    types={FaultyRelations_A, FaultyRelations_B, FaultyRelations_C},
    associations={AB0, AC1, BA2, BC3, CA5, CB7},
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