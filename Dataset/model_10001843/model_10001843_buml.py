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
A = Class(name="A")
B = Class(name="B")
C = Class(name="C")
Abis = Class(name="Abis", is_abstract=True)
Bbis = Class(name="Bbis")
Cbis = Class(name="Cbis", is_abstract=True)
Y = Class(name="Y")
C2 = Class(name="C2")
C3 = Class(name="C3")
Z = Class(name="Z")
R = Class(name="R")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC1, C_attC2}

# Abis class attributes and methods
Abis_attA: Property = Property(name="attA", type=StringType)
Abis.attributes={Abis_attA}

# Bbis class attributes and methods
Bbis_attB: Property = Property(name="attB", type=IntegerType)
Bbis.attributes={Bbis_attB}

# Cbis class attributes and methods
Cbis_attC1: Property = Property(name="attC1", type=IntegerType)
Cbis_attC2: Property = Property(name="attC2", type=BooleanType)
Cbis.attributes={Cbis_attC2, Cbis_attC1}

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# C2 class attributes and methods

# C3 class attributes and methods

# Z class attributes and methods

# R class attributes and methods

# Relationships
B_A: BinaryAssociation = BinaryAssociation(
    name="B_A",
    ends={
        Property(name="a0", type=A, multiplicity=Multiplicity(0, 1)),
        Property(name="b1", type=B, multiplicity=Multiplicity(1, 9999))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b4", type=Bbis, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=Abis, multiplicity=Multiplicity(0, 1))
    }
)
B_C2: BinaryAssociation = BinaryAssociation(
    name="B_C2",
    ends={
        Property(name="c6", type=Cbis, multiplicity=Multiplicity(0, 9999)),
        Property(name="b7", type=Bbis, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="a8", type=Abis, multiplicity=Multiplicity(0, 9999)),
        Property(name="r9", type=R, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ZseOwNAeEeeLcIicqHdTUQ",
    types={A, B, C, Abis, Bbis, Cbis, Y, C2, C3, Z, R},
    associations={B_A, B_C, A_B, B_C2, R_A},
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