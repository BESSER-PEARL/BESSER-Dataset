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
R_servation = Class(name="R_servation")
Passagers = Class(name="Passagers")
Client = Class(name="Client")
A = Class(name="A", is_abstract=True)
B = Class(name="B")
C = Class(name="C", is_abstract=True)
Y = Class(name="Y")
R = Class(name="R")
Z = Class(name="Z")
C2 = Class(name="C2")
C3 = Class(name="C3")
tp2BMOexe3_B = Class(name="tp2BMOexe3_B")
tp2BMOexe3_B2 = Class(name="tp2BMOexe3_B2")
tp2BMOexe3_A = Class(name="tp2BMOexe3_A", is_abstract=True)
tp2BMOexe3_A2 = Class(name="tp2BMOexe3_A2")
tp2BMOexe3_A3 = Class(name="tp2BMOexe3_A3")
Ville = Class(name="Ville")
A_roport = Class(name="A_roport")
Vol = Class(name="Vol")
Escale = Class(name="Escale")

# R_servation class attributes and methods

# Passagers class attributes and methods

# Client class attributes and methods

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

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# Z class attributes and methods

# C2 class attributes and methods

# C3 class attributes and methods

# tp2BMOexe3_B class attributes and methods

# tp2BMOexe3_B2 class attributes and methods

# tp2BMOexe3_A class attributes and methods
tp2BMOexe3_A_c: Property = Property(name="c", type=tp2BMOexe3_B)
tp2BMOexe3_A_d: Property = Property(name="d", type=IntegerType)
tp2BMOexe3_A_b: Property = Property(name="b", type=BooleanType)
tp2BMOexe3_A.attributes={tp2BMOexe3_A_b, tp2BMOexe3_A_d, tp2BMOexe3_A_c}

# tp2BMOexe3_A2 class attributes and methods

# tp2BMOexe3_A3 class attributes and methods

# Ville class attributes and methods

# A_roport class attributes and methods

# Vol class attributes and methods

# Escale class attributes and methods

# Relationships
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c0", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="b1", type=B, multiplicity=Multiplicity(0, 1))
    }
)
R_A: BinaryAssociation = BinaryAssociation(
    name="R_A",
    ends={
        Property(name="aR2", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r3", type=R, multiplicity=Multiplicity(0, 1))
    }
)
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="b4", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a5", type=A, multiplicity=Multiplicity(0, 1))
    }
)
B_A: BinaryAssociation = BinaryAssociation(
    name="B_A",
    ends={
        Property(name="a6", type=tp2BMOexe3_A, multiplicity=Multiplicity(0, 9999)),
        Property(name="b7", type=tp2BMOexe3_B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6zuyUM9UEeeLcIicqHdTUQ",
    types={R_servation, Passagers, Client, A, B, C, Y, R, Z, C2, C3, tp2BMOexe3_B, tp2BMOexe3_B2, tp2BMOexe3_A, tp2BMOexe3_A2, tp2BMOexe3_A3, Ville, A_roport, Vol, Escale},
    associations={B_C, R_A, A_B, B_A},
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