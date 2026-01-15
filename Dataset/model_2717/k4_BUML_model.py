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
k4_X = Class(name="k4::X")
k4_C = Class(name="k4::C", is_abstract=True)
k4_Z = Class(name="k4::Z")
k4_Y = Class(name="k4::Y")
k4_W = Class(name="k4::W")
k4_A = Class(name="k4::A")
B = Class(name="B")
k4_B = Class(name="k4::B")
C = Class(name="C")
k4_I = Class(name="k4::I")
G = Class(name="G")
k4_P = Class(name="k4::P")
k4_G = Class(name="k4::G", is_abstract=True)
k4_N = Class(name="k4::N")
M = Class(name="M")
k4_J = Class(name="k4::J")
k4_M = Class(name="k4::M")
A = Class(name="A")
k4_L1 = Class(name="k4::L1")
k4_Q = Class(name="k4::Q")
P = Class(name="P")
N = Class(name="N")
k4_K = Class(name="k4::K")
k4_L2 = Class(name="k4::L2")
J = Class(name="J")
k4_L3 = Class(name="k4::L3")
L1 = Class(name="L1")
k4_L4 = Class(name="k4::L4")

# k4_X class attributes and methods

# k4_C class attributes and methods

# k4_Z class attributes and methods
k4_Z_z1: Property = Property(name="z1", type=StringType)
k4_Z_z2: Property = Property(name="z2", type=StringType)
k4_Z_z3: Property = Property(name="z3", type=StringType)
k4_Z.attributes={k4_Z_z3, k4_Z_z1, k4_Z_z2}

# k4_Y class attributes and methods
k4_Y_y: Property = Property(name="y", type=IntegerType)
k4_Y.attributes={k4_Y_y}

# k4_W class attributes and methods
k4_W_w: Property = Property(name="w", type=StringType)
k4_W.attributes={k4_W_w}

# k4_A class attributes and methods

# B class attributes and methods

# k4_B class attributes and methods

# C class attributes and methods

# k4_I class attributes and methods

# G class attributes and methods

# k4_P class attributes and methods

# k4_G class attributes and methods
k4_G_name: Property = Property(name="name", type=StringType)
k4_G.attributes={k4_G_name}

# k4_N class attributes and methods

# M class attributes and methods

# k4_J class attributes and methods

# k4_M class attributes and methods

# A class attributes and methods

# k4_L1 class attributes and methods
k4_L1_id1: Property = Property(name="id1", type=StringType)
k4_L1_id2: Property = Property(name="id2", type=IntegerType)
k4_L1.attributes={k4_L1_id2, k4_L1_id1}

# k4_Q class attributes and methods

# P class attributes and methods

# N class attributes and methods

# k4_K class attributes and methods
k4_K_title: Property = Property(name="title", type=StringType)
k4_K.attributes={k4_K_title}

# k4_L2 class attributes and methods
k4_L2_l1: Property = Property(name="l1", type=IntegerType)
k4_L2_l2: Property = Property(name="l2", type=IntegerType)
k4_L2.attributes={k4_L2_l2, k4_L2_l1}

# J class attributes and methods

# k4_L3 class attributes and methods

# L1 class attributes and methods

# k4_L4 class attributes and methods

# Relationships
xcs0: BinaryAssociation = BinaryAssociation(
    name="xcs0",
    ends={
        Property(name="k4_C", type=k4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_X", type=k4_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zs3: BinaryAssociation = BinaryAssociation(
    name="zs3",
    ends={
        Property(name="k4_Z", type=k4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_X4", type=k4_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ys5: BinaryAssociation = BinaryAssociation(
    name="ys5",
    ends={
        Property(name="k4_Y", type=k4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_X6", type=k4_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
w7: BinaryAssociation = BinaryAssociation(
    name="w7",
    ends={
        Property(name="k4_W", type=k4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_X8", type=k4_W, multiplicity=Multiplicity(0, 1))
    }
)
is9: BinaryAssociation = BinaryAssociation(
    name="is9",
    ends={
        Property(name="k4_I", type=k4_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_B", type=k4_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps1: BinaryAssociation = BinaryAssociation(
    name="ps1",
    ends={
        Property(name="k4_P", type=k4_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_X2", type=k4_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ml112: BinaryAssociation = BinaryAssociation(
    name="ml112",
    ends={
        Property(name="k4_M13", type=k4_L1, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="k4_L1", type=k4_M, multiplicity=Multiplicity(1, 1))
    }
)
mcs10: BinaryAssociation = BinaryAssociation(
    name="mcs10",
    ends={
        Property(name="k4_C11", type=k4_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_M", type=k4_C, multiplicity=Multiplicity(0, 9999))
    }
)
ks16: BinaryAssociation = BinaryAssociation(
    name="ks16",
    ends={
        Property(name="k4_P17", type=k4_K, multiplicity=Multiplicity(0, 1)),
        Property(name="k4_K", type=k4_P, multiplicity=Multiplicity(1, 1))
    }
)
js18: BinaryAssociation = BinaryAssociation(
    name="js18",
    ends={
        Property(name="k4_J", type=k4_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_P19", type=k4_J, multiplicity=Multiplicity(0, 9999))
    }
)
a14: BinaryAssociation = BinaryAssociation(
    name="a14",
    ends={
        Property(name="k4_A", type=k4_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_P15", type=k4_A, multiplicity=Multiplicity(0, 1))
    }
)
l1c21: BinaryAssociation = BinaryAssociation(
    name="l1c21",
    ends={
        Property(name="k4_C23", type=k4_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L122", type=k4_C, multiplicity=Multiplicity(0, 1))
    }
)
l2s20: BinaryAssociation = BinaryAssociation(
    name="l2s20",
    ends={
        Property(name="k4_L2", type=k4_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_Q", type=k4_L2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l2q27: BinaryAssociation = BinaryAssociation(
    name="l2q27",
    ends={
        Property(name="k4_Q29", type=k4_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L228", type=k4_Q, multiplicity=Multiplicity(0, 1))
    }
)
l2k30: BinaryAssociation = BinaryAssociation(
    name="l2k30",
    ends={
        Property(name="k4_K32", type=k4_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L231", type=k4_K, multiplicity=Multiplicity(0, 1))
    }
)
l1m24: BinaryAssociation = BinaryAssociation(
    name="l1m24",
    ends={
        Property(name="k4_M26", type=k4_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L125", type=k4_M, multiplicity=Multiplicity(0, 1))
    }
)
l3i33: BinaryAssociation = BinaryAssociation(
    name="l3i33",
    ends={
        Property(name="k4_I34", type=k4_L3, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L3", type=k4_I, multiplicity=Multiplicity(0, 1))
    }
)
l4z35: BinaryAssociation = BinaryAssociation(
    name="l4z35",
    ends={
        Property(name="k4_Z36", type=k4_L4, multiplicity=Multiplicity(1, 1)),
        Property(name="k4_L4", type=k4_Z, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_k4_A_B = Generalization(general=B, specific=k4_A)
gen_k4_B_C = Generalization(general=C, specific=k4_B)
gen_k4_C_G = Generalization(general=G, specific=k4_C)
gen_k4_N_M = Generalization(general=M, specific=k4_N)
gen_k4_M_G = Generalization(general=G, specific=k4_M)
gen_k4_J_A = Generalization(general=A, specific=k4_J)
gen_k4_Q_P = Generalization(general=P, specific=k4_Q)
gen_k4_P_N = Generalization(general=N, specific=k4_P)
gen_k4_I_G = Generalization(general=G, specific=k4_I)
gen_k4_K_J = Generalization(general=J, specific=k4_K)
gen_k4_L3_L1 = Generalization(general=L1, specific=k4_L3)
gen_k4_L4_L1 = Generalization(general=L1, specific=k4_L4)

# Domain Model
domain_model = DomainModel(
    name="k4",
    types={k4_X, k4_C, k4_Z, k4_Y, k4_W, k4_A, B, k4_B, C, k4_I, G, k4_P, k4_G, k4_N, M, k4_J, k4_M, A, k4_L1, k4_Q, P, N, k4_K, k4_L2, J, k4_L3, L1, k4_L4},
    associations={xcs0, zs3, ys5, w7, is9, ps1, ml112, mcs10, ks16, js18, a14, l1c21, l2s20, l2q27, l2k30, l1m24, l3i33, l4z35},
    generalizations={gen_k4_A_B, gen_k4_B_C, gen_k4_C_G, gen_k4_N_M, gen_k4_M_G, gen_k4_J_A, gen_k4_Q_P, gen_k4_P_N, gen_k4_I_G, gen_k4_K_J, gen_k4_L3_L1, gen_k4_L4_L1},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)