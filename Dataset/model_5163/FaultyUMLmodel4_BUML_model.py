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
FaultyUMLmodel4_A = Class(name="FaultyUMLmodel4::A")
FaultyUMLmodel4_D = Class(name="FaultyUMLmodel4::D")
FaultyUMLmodel4_B = Class(name="FaultyUMLmodel4::B")
FaultyUMLmodel4_C = Class(name="FaultyUMLmodel4::C")

# FaultyUMLmodel4_A class attributes and methods
FaultyUMLmodel4_A_v: Property = Property(name="v", type=IntegerType)
FaultyUMLmodel4_A_w: Property = Property(name="w", type=BooleanType)
FaultyUMLmodel4_A.attributes={FaultyUMLmodel4_A_v, FaultyUMLmodel4_A_w}

# FaultyUMLmodel4_D class attributes and methods
FaultyUMLmodel4_D_z: Property = Property(name="z", type=BooleanType)
FaultyUMLmodel4_D.attributes={FaultyUMLmodel4_D_z}

# FaultyUMLmodel4_B class attributes and methods
FaultyUMLmodel4_B_x: Property = Property(name="x", type=IntegerType)
FaultyUMLmodel4_B_y: Property = Property(name="y", type=IntegerType)
FaultyUMLmodel4_B.attributes={FaultyUMLmodel4_B_x, FaultyUMLmodel4_B_y}

# FaultyUMLmodel4_C class attributes and methods
FaultyUMLmodel4_C_u: Property = Property(name="u", type=IntegerType)
FaultyUMLmodel4_C.attributes={FaultyUMLmodel4_C_u}

# Relationships
BA2: BinaryAssociation = BinaryAssociation(
    name="BA2",
    ends={
        Property(name="A", type=FaultyUMLmodel4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="AB", type=FaultyUMLmodel4_A, multiplicity=Multiplicity(2, 2))
    }
)
BC3: BinaryAssociation = BinaryAssociation(
    name="BC3",
    ends={
        Property(name="C4", type=FaultyUMLmodel4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="CB", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(3, 3))
    }
)
CA5: BinaryAssociation = BinaryAssociation(
    name="CA5",
    ends={
        Property(name="A6", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(1, 1)),
        Property(name="AC", type=FaultyUMLmodel4_A, multiplicity=Multiplicity(2, 2))
    }
)
CB7: BinaryAssociation = BinaryAssociation(
    name="CB7",
    ends={
        Property(name="B8", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(1, 1)),
        Property(name="BC", type=FaultyUMLmodel4_B, multiplicity=Multiplicity(5, 5))
    }
)
CD9: BinaryAssociation = BinaryAssociation(
    name="CD9",
    ends={
        Property(name="D", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(1, 1)),
        Property(name="DC", type=FaultyUMLmodel4_D, multiplicity=Multiplicity(0, 7))
    }
)
DC10: BinaryAssociation = BinaryAssociation(
    name="DC10",
    ends={
        Property(name="C11", type=FaultyUMLmodel4_D, multiplicity=Multiplicity(1, 1)),
        Property(name="CD", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(3, 3))
    }
)
AB0: BinaryAssociation = BinaryAssociation(
    name="AB0",
    ends={
        Property(name="B", type=FaultyUMLmodel4_A, multiplicity=Multiplicity(1, 1)),
        Property(name="BA", type=FaultyUMLmodel4_B, multiplicity=Multiplicity(5, 5))
    }
)
AC1: BinaryAssociation = BinaryAssociation(
    name="AC1",
    ends={
        Property(name="C", type=FaultyUMLmodel4_A, multiplicity=Multiplicity(1, 1)),
        Property(name="CA", type=FaultyUMLmodel4_C, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="FaultyUMLmodel4",
    types={FaultyUMLmodel4_A, FaultyUMLmodel4_D, FaultyUMLmodel4_B, FaultyUMLmodel4_C},
    associations={BA2, BC3, CA5, CB7, CD9, DC10, AB0, AC1},
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