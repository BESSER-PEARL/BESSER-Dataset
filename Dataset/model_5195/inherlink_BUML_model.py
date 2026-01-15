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
inherlink_C = Class(name="inherlink::C")
inherlink_K = Class(name="inherlink::K")
inherlink_M = Class(name="inherlink::M")
inherlink_X = Class(name="inherlink::X")
inherlink_N = Class(name="inherlink::N")
inherlink_R = Class(name="inherlink::R", is_abstract=True)
Named = Class(name="Named")
inherlink_Named = Class(name="inherlink::Named")
inherlink_L = Class(name="inherlink::L")
inherlink_A = Class(name="inherlink::A")
L = Class(name="L")
inherlink_Y = Class(name="inherlink::Y")
R = Class(name="R")
inherlink_P = Class(name="inherlink::P")
inherlink_G = Class(name="inherlink::G")
inherlink_T = Class(name="inherlink::T")
inherlink_W = Class(name="inherlink::W")

# inherlink_C class attributes and methods

# inherlink_K class attributes and methods

# inherlink_M class attributes and methods

# inherlink_X class attributes and methods

# inherlink_N class attributes and methods

# inherlink_R class attributes and methods

# Named class attributes and methods

# inherlink_Named class attributes and methods
inherlink_Named_name: Property = Property(name="name", type=StringType)
inherlink_Named.attributes={inherlink_Named_name}

# inherlink_L class attributes and methods

# inherlink_A class attributes and methods

# L class attributes and methods

# inherlink_Y class attributes and methods

# R class attributes and methods

# inherlink_P class attributes and methods

# inherlink_G class attributes and methods

# inherlink_T class attributes and methods

# inherlink_W class attributes and methods

# Relationships
ks0: BinaryAssociation = BinaryAssociation(
    name="ks0",
    ends={
        Property(name="inherlink_K", type=inherlink_C, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_C", type=inherlink_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms1: BinaryAssociation = BinaryAssociation(
    name="ms1",
    ends={
        Property(name="inherlink_M", type=inherlink_C, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_C2", type=inherlink_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xs3: BinaryAssociation = BinaryAssociation(
    name="xs3",
    ends={
        Property(name="inherlink_X", type=inherlink_C, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_C4", type=inherlink_X, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns5: BinaryAssociation = BinaryAssociation(
    name="ns5",
    ends={
        Property(name="inherlink_N", type=inherlink_C, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_C6", type=inherlink_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y14: BinaryAssociation = BinaryAssociation(
    name="y14",
    ends={
        Property(name="inherlink_Y16", type=inherlink_K, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_K15", type=inherlink_Y, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
as17: BinaryAssociation = BinaryAssociation(
    name="as17",
    ends={
        Property(name="inherlink_A", type=inherlink_L, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_L", type=inherlink_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r18: BinaryAssociation = BinaryAssociation(
    name="r18",
    ends={
        Property(name="inherlink_R", type=inherlink_A, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_A19", type=inherlink_R, multiplicity=Multiplicity(0, 1))
    }
)
l20: BinaryAssociation = BinaryAssociation(
    name="l20",
    ends={
        Property(name="inherlink_L22", type=inherlink_A, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_A21", type=inherlink_L, multiplicity=Multiplicity(0, 1))
    }
)
gs23: BinaryAssociation = BinaryAssociation(
    name="gs23",
    ends={
        Property(name="inherlink_G25", type=inherlink_P, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_P24", type=inherlink_G, multiplicity=Multiplicity(0, 9999))
    }
)
ts26: BinaryAssociation = BinaryAssociation(
    name="ts26",
    ends={
        Property(name="inherlink_T28", type=inherlink_P, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_P27", type=inherlink_T, multiplicity=Multiplicity(0, 1))
    }
)
ps7: BinaryAssociation = BinaryAssociation(
    name="ps7",
    ends={
        Property(name="inherlink_P", type=inherlink_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_Y", type=inherlink_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs8: BinaryAssociation = BinaryAssociation(
    name="gs8",
    ends={
        Property(name="inherlink_G", type=inherlink_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_Y9", type=inherlink_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ts10: BinaryAssociation = BinaryAssociation(
    name="ts10",
    ends={
        Property(name="inherlink_T", type=inherlink_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_Y11", type=inherlink_T, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws12: BinaryAssociation = BinaryAssociation(
    name="ws12",
    ends={
        Property(name="inherlink_W", type=inherlink_K, multiplicity=Multiplicity(1, 1)),
        Property(name="inherlink_K13", type=inherlink_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_inherlink_R_Named = Generalization(general=Named, specific=inherlink_R)
gen_inherlink_W_L = Generalization(general=L, specific=inherlink_W)
gen_inherlink_L_Named = Generalization(general=Named, specific=inherlink_L)
gen_inherlink_X_L = Generalization(general=L, specific=inherlink_X)
gen_inherlink_Y_R = Generalization(general=R, specific=inherlink_Y)
gen_inherlink_M_L = Generalization(general=L, specific=inherlink_M)
gen_inherlink_N_R = Generalization(general=R, specific=inherlink_N)
gen_inherlink_K_R = Generalization(general=R, specific=inherlink_K)

# Domain Model
domain_model = DomainModel(
    name="inherlink",
    types={inherlink_C, inherlink_K, inherlink_M, inherlink_X, inherlink_N, inherlink_R, Named, inherlink_Named, inherlink_L, inherlink_A, L, inherlink_Y, R, inherlink_P, inherlink_G, inherlink_T, inherlink_W},
    associations={ks0, ms1, xs3, ns5, y14, as17, r18, l20, gs23, ts26, ps7, gs8, ts10, ws12},
    generalizations={gen_inherlink_R_Named, gen_inherlink_W_L, gen_inherlink_L_Named, gen_inherlink_X_L, gen_inherlink_Y_R, gen_inherlink_M_L, gen_inherlink_N_R, gen_inherlink_K_R},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)