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
anol3l4_X = Class(name="anol3l4::X")
anol3l4_C = Class(name="anol3l4::C", is_abstract=True)
anol3l4_P = Class(name="anol3l4::P")
anol3l4_Z = Class(name="anol3l4::Z")
anol3l4_I = Class(name="anol3l4::I")
G = Class(name="G")
anol3l4_G = Class(name="anol3l4::G", is_abstract=True)
anol3l4_M = Class(name="anol3l4::M")
anol3l4_Y = Class(name="anol3l4::Y")
anol3l4_W = Class(name="anol3l4::W")
anol3l4_A = Class(name="anol3l4::A")
B = Class(name="B")
anol3l4_B = Class(name="anol3l4::B")
C = Class(name="C")
anol3l4_N = Class(name="anol3l4::N")
M = Class(name="M")
anol3l4_J = Class(name="anol3l4::J")
A = Class(name="A")
anol3l4_L1 = Class(name="anol3l4::L1")
anol3l4_K = Class(name="anol3l4::K")
anol3l4_Q = Class(name="anol3l4::Q")
P = Class(name="P")
N = Class(name="N")
anol3l4_L2 = Class(name="anol3l4::L2")
J = Class(name="J")
anol3l4_L3 = Class(name="anol3l4::L3")
L1 = Class(name="L1")
anol3l4_L4 = Class(name="anol3l4::L4")

# anol3l4_X class attributes and methods

# anol3l4_C class attributes and methods

# anol3l4_P class attributes and methods

# anol3l4_Z class attributes and methods
anol3l4_Z_z1: Property = Property(name="z1", type=StringType)
anol3l4_Z_z2: Property = Property(name="z2", type=StringType)
anol3l4_Z_z3: Property = Property(name="z3", type=StringType)
anol3l4_Z.attributes={anol3l4_Z_z1, anol3l4_Z_z3, anol3l4_Z_z2}

# anol3l4_I class attributes and methods

# G class attributes and methods

# anol3l4_G class attributes and methods
anol3l4_G_name: Property = Property(name="name", type=StringType)
anol3l4_G.attributes={anol3l4_G_name}

# anol3l4_M class attributes and methods

# anol3l4_Y class attributes and methods
anol3l4_Y_y: Property = Property(name="y", type=IntegerType)
anol3l4_Y.attributes={anol3l4_Y_y}

# anol3l4_W class attributes and methods
anol3l4_W_w: Property = Property(name="w", type=StringType)
anol3l4_W.attributes={anol3l4_W_w}

# anol3l4_A class attributes and methods

# B class attributes and methods

# anol3l4_B class attributes and methods

# C class attributes and methods

# anol3l4_N class attributes and methods

# M class attributes and methods

# anol3l4_J class attributes and methods

# A class attributes and methods

# anol3l4_L1 class attributes and methods
anol3l4_L1_id1: Property = Property(name="id1", type=StringType)
anol3l4_L1_id2: Property = Property(name="id2", type=IntegerType)
anol3l4_L1.attributes={anol3l4_L1_id1, anol3l4_L1_id2}

# anol3l4_K class attributes and methods
anol3l4_K_title: Property = Property(name="title", type=StringType)
anol3l4_K.attributes={anol3l4_K_title}

# anol3l4_Q class attributes and methods

# P class attributes and methods

# N class attributes and methods

# anol3l4_L2 class attributes and methods
anol3l4_L2_l1: Property = Property(name="l1", type=IntegerType)
anol3l4_L2_l2: Property = Property(name="l2", type=IntegerType)
anol3l4_L2.attributes={anol3l4_L2_l2, anol3l4_L2_l1}

# J class attributes and methods

# anol3l4_L3 class attributes and methods

# L1 class attributes and methods

# anol3l4_L4 class attributes and methods

# Relationships
xcs0: BinaryAssociation = BinaryAssociation(
    name="xcs0",
    ends={
        Property(name="anol3l4_C", type=anol3l4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_X", type=anol3l4_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps1: BinaryAssociation = BinaryAssociation(
    name="ps1",
    ends={
        Property(name="anol3l4_P", type=anol3l4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_X2", type=anol3l4_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
is9: BinaryAssociation = BinaryAssociation(
    name="is9",
    ends={
        Property(name="anol3l4_I", type=anol3l4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_B", type=anol3l4_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zs3: BinaryAssociation = BinaryAssociation(
    name="zs3",
    ends={
        Property(name="anol3l4_Z", type=anol3l4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_X4", type=anol3l4_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ys5: BinaryAssociation = BinaryAssociation(
    name="ys5",
    ends={
        Property(name="anol3l4_Y", type=anol3l4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_X6", type=anol3l4_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
w7: BinaryAssociation = BinaryAssociation(
    name="w7",
    ends={
        Property(name="anol3l4_W", type=anol3l4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_X8", type=anol3l4_W, multiplicity=Multiplicity(0, 1))
    }
)
mcs10: BinaryAssociation = BinaryAssociation(
    name="mcs10",
    ends={
        Property(name="anol3l4_C11", type=anol3l4_M, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_M", type=anol3l4_C, multiplicity=Multiplicity(0, 9999))
    }
)
ml112: BinaryAssociation = BinaryAssociation(
    name="ml112",
    ends={
        Property(name="anol3l4_L1", type=anol3l4_M, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_M13", type=anol3l4_L1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks16: BinaryAssociation = BinaryAssociation(
    name="ks16",
    ends={
        Property(name="anol3l4_K", type=anol3l4_P, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_P17", type=anol3l4_K, multiplicity=Multiplicity(0, 1))
    }
)
js18: BinaryAssociation = BinaryAssociation(
    name="js18",
    ends={
        Property(name="anol3l4_J", type=anol3l4_P, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_P19", type=anol3l4_J, multiplicity=Multiplicity(0, 9999))
    }
)
a14: BinaryAssociation = BinaryAssociation(
    name="a14",
    ends={
        Property(name="anol3l4_A", type=anol3l4_P, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_P15", type=anol3l4_A, multiplicity=Multiplicity(0, 1))
    }
)
l1c21: BinaryAssociation = BinaryAssociation(
    name="l1c21",
    ends={
        Property(name="anol3l4_C23", type=anol3l4_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L122", type=anol3l4_C, multiplicity=Multiplicity(0, 1))
    }
)
l2s20: BinaryAssociation = BinaryAssociation(
    name="l2s20",
    ends={
        Property(name="anol3l4_L2", type=anol3l4_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_Q", type=anol3l4_L2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l2q27: BinaryAssociation = BinaryAssociation(
    name="l2q27",
    ends={
        Property(name="anol3l4_Q29", type=anol3l4_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L228", type=anol3l4_Q, multiplicity=Multiplicity(0, 1))
    }
)
l2k30: BinaryAssociation = BinaryAssociation(
    name="l2k30",
    ends={
        Property(name="anol3l4_K32", type=anol3l4_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L231", type=anol3l4_K, multiplicity=Multiplicity(0, 1))
    }
)
l1m24: BinaryAssociation = BinaryAssociation(
    name="l1m24",
    ends={
        Property(name="anol3l4_M26", type=anol3l4_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L125", type=anol3l4_M, multiplicity=Multiplicity(0, 1))
    }
)
l3i33: BinaryAssociation = BinaryAssociation(
    name="l3i33",
    ends={
        Property(name="anol3l4_I34", type=anol3l4_L3, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L3", type=anol3l4_I, multiplicity=Multiplicity(0, 1))
    }
)
l4z35: BinaryAssociation = BinaryAssociation(
    name="l4z35",
    ends={
        Property(name="anol3l4_Z36", type=anol3l4_L4, multiplicity=Multiplicity(1, 1)),
        Property(name="anol3l4_L4", type=anol3l4_Z, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_anol3l4_C_G = Generalization(general=G, specific=anol3l4_C)
gen_anol3l4_M_G = Generalization(general=G, specific=anol3l4_M)
gen_anol3l4_A_B = Generalization(general=B, specific=anol3l4_A)
gen_anol3l4_B_C = Generalization(general=C, specific=anol3l4_B)
gen_anol3l4_N_M = Generalization(general=M, specific=anol3l4_N)
gen_anol3l4_J_A = Generalization(general=A, specific=anol3l4_J)
gen_anol3l4_Q_P = Generalization(general=P, specific=anol3l4_Q)
gen_anol3l4_P_N = Generalization(general=N, specific=anol3l4_P)
gen_anol3l4_I_G = Generalization(general=G, specific=anol3l4_I)
gen_anol3l4_K_J = Generalization(general=J, specific=anol3l4_K)
gen_anol3l4_L3_L1 = Generalization(general=L1, specific=anol3l4_L3)
gen_anol3l4_L4_L1 = Generalization(general=L1, specific=anol3l4_L4)

# Domain Model
domain_model = DomainModel(
    name="anol3l4",
    types={anol3l4_X, anol3l4_C, anol3l4_P, anol3l4_Z, anol3l4_I, G, anol3l4_G, anol3l4_M, anol3l4_Y, anol3l4_W, anol3l4_A, B, anol3l4_B, C, anol3l4_N, M, anol3l4_J, A, anol3l4_L1, anol3l4_K, anol3l4_Q, P, N, anol3l4_L2, J, anol3l4_L3, L1, anol3l4_L4},
    associations={xcs0, ps1, is9, zs3, ys5, w7, mcs10, ml112, ks16, js18, a14, l1c21, l2s20, l2q27, l2k30, l1m24, l3i33, l4z35},
    generalizations={gen_anol3l4_C_G, gen_anol3l4_M_G, gen_anol3l4_A_B, gen_anol3l4_B_C, gen_anol3l4_N_M, gen_anol3l4_J_A, gen_anol3l4_Q_P, gen_anol3l4_P_N, gen_anol3l4_I_G, gen_anol3l4_K_J, gen_anol3l4_L3_L1, gen_anol3l4_L4_L1},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)