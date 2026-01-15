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
k5_Y = Class(name="k5::Y")
k5_W = Class(name="k5::W")
k5_X = Class(name="k5::X")
k5_C = Class(name="k5::C", is_abstract=True)
k5_P = Class(name="k5::P")
k5_Z = Class(name="k5::Z")
k5_L1 = Class(name="k5::L1")
k5_N = Class(name="k5::N")
M = Class(name="M")
k5_J = Class(name="k5::J")
A = Class(name="A")
k5_A = Class(name="k5::A")
B = Class(name="B")
k5_B = Class(name="k5::B")
C = Class(name="C")
k5_I = Class(name="k5::I")
G = Class(name="G")
k5_G = Class(name="k5::G", is_abstract=True)
k5_M = Class(name="k5::M")
N = Class(name="N")
k5_K = Class(name="k5::K")
k5_Q = Class(name="k5::Q")
P = Class(name="P")
k5_L2 = Class(name="k5::L2")
k5_L3 = Class(name="k5::L3")
L1 = Class(name="L1")
J = Class(name="J")

# k5_Y class attributes and methods
k5_Y_y: Property = Property(name="y", type=IntegerType)
k5_Y.attributes={k5_Y_y}

# k5_W class attributes and methods
k5_W_w: Property = Property(name="w", type=StringType)
k5_W.attributes={k5_W_w}

# k5_X class attributes and methods

# k5_C class attributes and methods

# k5_P class attributes and methods

# k5_Z class attributes and methods
k5_Z_z1: Property = Property(name="z1", type=StringType)
k5_Z_z2: Property = Property(name="z2", type=StringType)
k5_Z_z3: Property = Property(name="z3", type=StringType)
k5_Z.attributes={k5_Z_z3, k5_Z_z1, k5_Z_z2}

# k5_L1 class attributes and methods
k5_L1_id1: Property = Property(name="id1", type=StringType)
k5_L1_id2: Property = Property(name="id2", type=IntegerType)
k5_L1.attributes={k5_L1_id2, k5_L1_id1}

# k5_N class attributes and methods

# M class attributes and methods

# k5_J class attributes and methods

# A class attributes and methods

# k5_A class attributes and methods

# B class attributes and methods

# k5_B class attributes and methods

# C class attributes and methods

# k5_I class attributes and methods

# G class attributes and methods

# k5_G class attributes and methods
k5_G_name: Property = Property(name="name", type=StringType)
k5_G.attributes={k5_G_name}

# k5_M class attributes and methods

# N class attributes and methods

# k5_K class attributes and methods
k5_K_title: Property = Property(name="title", type=StringType)
k5_K.attributes={k5_K_title}

# k5_Q class attributes and methods

# P class attributes and methods

# k5_L2 class attributes and methods
k5_L2_l1: Property = Property(name="l1", type=IntegerType)
k5_L2_l2: Property = Property(name="l2", type=IntegerType)
k5_L2.attributes={k5_L2_l1, k5_L2_l2}

# k5_L3 class attributes and methods

# L1 class attributes and methods

# J class attributes and methods

# Relationships
ys5: BinaryAssociation = BinaryAssociation(
    name="ys5",
    ends={
        Property(name="k5_Y", type=k5_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_X6", type=k5_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xcs0: BinaryAssociation = BinaryAssociation(
    name="xcs0",
    ends={
        Property(name="k5_C", type=k5_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_X", type=k5_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps1: BinaryAssociation = BinaryAssociation(
    name="ps1",
    ends={
        Property(name="k5_P", type=k5_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_X2", type=k5_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zs3: BinaryAssociation = BinaryAssociation(
    name="zs3",
    ends={
        Property(name="k5_Z", type=k5_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_X4", type=k5_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ml115: BinaryAssociation = BinaryAssociation(
    name="ml115",
    ends={
        Property(name="k5_L1", type=k5_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_M16", type=k5_L1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
w7: BinaryAssociation = BinaryAssociation(
    name="w7",
    ends={
        Property(name="k5_W", type=k5_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_X8", type=k5_W, multiplicity=Multiplicity(0, 1))
    }
)
is9: BinaryAssociation = BinaryAssociation(
    name="is9",
    ends={
        Property(name="k5_I", type=k5_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_B", type=k5_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y10: BinaryAssociation = BinaryAssociation(
    name="y10",
    ends={
        Property(name="k5_Y12", type=k5_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_B11", type=k5_Y, multiplicity=Multiplicity(0, 1))
    }
)
mcs13: BinaryAssociation = BinaryAssociation(
    name="mcs13",
    ends={
        Property(name="k5_C14", type=k5_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_M", type=k5_C, multiplicity=Multiplicity(0, 9999))
    }
)
l1c24: BinaryAssociation = BinaryAssociation(
    name="l1c24",
    ends={
        Property(name="k5_C26", type=k5_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_L125", type=k5_C, multiplicity=Multiplicity(0, 1))
    }
)
l1m27: BinaryAssociation = BinaryAssociation(
    name="l1m27",
    ends={
        Property(name="k5_M29", type=k5_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_L128", type=k5_M, multiplicity=Multiplicity(0, 1))
    }
)
a17: BinaryAssociation = BinaryAssociation(
    name="a17",
    ends={
        Property(name="k5_A", type=k5_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_P18", type=k5_A, multiplicity=Multiplicity(0, 1))
    }
)
ks19: BinaryAssociation = BinaryAssociation(
    name="ks19",
    ends={
        Property(name="k5_K", type=k5_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_P20", type=k5_K, multiplicity=Multiplicity(0, 1))
    }
)
js21: BinaryAssociation = BinaryAssociation(
    name="js21",
    ends={
        Property(name="k5_J", type=k5_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_P22", type=k5_J, multiplicity=Multiplicity(0, 9999))
    }
)
l2s23: BinaryAssociation = BinaryAssociation(
    name="l2s23",
    ends={
        Property(name="k5_L2", type=k5_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_Q", type=k5_L2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l3z36: BinaryAssociation = BinaryAssociation(
    name="l3z36",
    ends={
        Property(name="k5_Z37", type=k5_L3, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_L3", type=k5_Z, multiplicity=Multiplicity(0, 1))
    }
)
l2q30: BinaryAssociation = BinaryAssociation(
    name="l2q30",
    ends={
        Property(name="k5_Q32", type=k5_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_L231", type=k5_Q, multiplicity=Multiplicity(0, 1))
    }
)
l2k33: BinaryAssociation = BinaryAssociation(
    name="l2k33",
    ends={
        Property(name="k5_K35", type=k5_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k5_L234", type=k5_K, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_k5_N_M = Generalization(general=M, specific=k5_N)
gen_k5_J_A = Generalization(general=A, specific=k5_J)
gen_k5_A_B = Generalization(general=B, specific=k5_A)
gen_k5_B_C = Generalization(general=C, specific=k5_B)
gen_k5_C_G = Generalization(general=G, specific=k5_C)
gen_k5_M_G = Generalization(general=G, specific=k5_M)
gen_k5_P_N = Generalization(general=N, specific=k5_P)
gen_k5_Q_P = Generalization(general=P, specific=k5_Q)
gen_k5_I_G = Generalization(general=G, specific=k5_I)
gen_k5_L3_L1 = Generalization(general=L1, specific=k5_L3)
gen_k5_K_J = Generalization(general=J, specific=k5_K)

# Domain Model
domain_model = DomainModel(
    name="k5",
    types={k5_Y, k5_W, k5_X, k5_C, k5_P, k5_Z, k5_L1, k5_N, M, k5_J, A, k5_A, B, k5_B, C, k5_I, G, k5_G, k5_M, N, k5_K, k5_Q, P, k5_L2, k5_L3, L1, J},
    associations={ys5, xcs0, ps1, zs3, ml115, w7, is9, y10, mcs13, l1c24, l1m27, a17, ks19, js21, l2s23, l3z36, l2q30, l2k33},
    generalizations={gen_k5_N_M, gen_k5_J_A, gen_k5_A_B, gen_k5_B_C, gen_k5_C_G, gen_k5_M_G, gen_k5_P_N, gen_k5_Q_P, gen_k5_I_G, gen_k5_L3_L1, gen_k5_K_J},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)