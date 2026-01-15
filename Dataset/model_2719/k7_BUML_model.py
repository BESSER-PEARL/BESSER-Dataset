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
k7_P = Class(name="k7::P")
k7_X = Class(name="k7::X")
k7_C = Class(name="k7::C", is_abstract=True)
G = Class(name="G")
k7_Z = Class(name="k7::Z")
k7_Y = Class(name="k7::Y")
k7_W = Class(name="k7::W")
k7_L4 = Class(name="k7::L4")
k7_T1 = Class(name="k7::T1")
k7_A = Class(name="k7::A")
B = Class(name="B")
k7_B = Class(name="k7::B")
C = Class(name="C")
k7_I = Class(name="k7::I")
k7_Q = Class(name="k7::Q")
P = Class(name="P")
k7_G = Class(name="k7::G", is_abstract=True)
k7_M = Class(name="k7::M")
k7_L1 = Class(name="k7::L1")
k7_N = Class(name="k7::N")
M = Class(name="M")
k7_J = Class(name="k7::J")
A = Class(name="A")
N = Class(name="N")
k7_K = Class(name="k7::K")
k7_L2 = Class(name="k7::L2")
J = Class(name="J")
k7_L3 = Class(name="k7::L3")
L1 = Class(name="L1")
k7_T2 = Class(name="k7::T2")
k7_DsmlRelation = Class(name="k7::DsmlRelation")
T2 = Class(name="T2")

# k7_P class attributes and methods

# k7_X class attributes and methods

# k7_C class attributes and methods

# G class attributes and methods

# k7_Z class attributes and methods
k7_Z_z1: Property = Property(name="z1", type=StringType)
k7_Z_z2: Property = Property(name="z2", type=StringType)
k7_Z_z3: Property = Property(name="z3", type=StringType)
k7_Z.attributes={k7_Z_z1, k7_Z_z2, k7_Z_z3}

# k7_Y class attributes and methods
k7_Y_y: Property = Property(name="y", type=IntegerType)
k7_Y.attributes={k7_Y_y}

# k7_W class attributes and methods
k7_W_w: Property = Property(name="w", type=StringType)
k7_W.attributes={k7_W_w}

# k7_L4 class attributes and methods
k7_L4_id: Property = Property(name="id", type=StringType)
k7_L4.attributes={k7_L4_id}

# k7_T1 class attributes and methods
k7_T1_name: Property = Property(name="name", type=StringType)
k7_T1.attributes={k7_T1_name}

# k7_A class attributes and methods

# B class attributes and methods

# k7_B class attributes and methods

# C class attributes and methods

# k7_I class attributes and methods

# k7_Q class attributes and methods

# P class attributes and methods

# k7_G class attributes and methods
k7_G_name: Property = Property(name="name", type=StringType)
k7_G.attributes={k7_G_name}

# k7_M class attributes and methods

# k7_L1 class attributes and methods
k7_L1_id1: Property = Property(name="id1", type=StringType)
k7_L1_id2: Property = Property(name="id2", type=IntegerType)
k7_L1.attributes={k7_L1_id2, k7_L1_id1}

# k7_N class attributes and methods

# M class attributes and methods

# k7_J class attributes and methods

# A class attributes and methods

# N class attributes and methods

# k7_K class attributes and methods
k7_K_title: Property = Property(name="title", type=StringType)
k7_K.attributes={k7_K_title}

# k7_L2 class attributes and methods
k7_L2_l1: Property = Property(name="l1", type=IntegerType)
k7_L2_l2: Property = Property(name="l2", type=IntegerType)
k7_L2.attributes={k7_L2_l1, k7_L2_l2}

# J class attributes and methods

# k7_L3 class attributes and methods

# L1 class attributes and methods

# k7_T2 class attributes and methods
k7_T2_id: Property = Property(name="id", type=StringType)
k7_T2.attributes={k7_T2_id}

# k7_DsmlRelation class attributes and methods
k7_DsmlRelation_name: Property = Property(name="name", type=StringType)
k7_DsmlRelation_mandatory: Property = Property(name="mandatory", type=BooleanType)
k7_DsmlRelation_details: Property = Property(name="details", type=StringType)
k7_DsmlRelation.attributes={k7_DsmlRelation_mandatory, k7_DsmlRelation_name, k7_DsmlRelation_details}

# T2 class attributes and methods

# Relationships
ps1: BinaryAssociation = BinaryAssociation(
    name="ps1",
    ends={
        Property(name="k7_P", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X2", type=k7_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xcs0: BinaryAssociation = BinaryAssociation(
    name="xcs0",
    ends={
        Property(name="k7_C", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X", type=k7_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zs3: BinaryAssociation = BinaryAssociation(
    name="zs3",
    ends={
        Property(name="k7_Z", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X4", type=k7_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ys5: BinaryAssociation = BinaryAssociation(
    name="ys5",
    ends={
        Property(name="k7_Y", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X6", type=k7_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
w7: BinaryAssociation = BinaryAssociation(
    name="w7",
    ends={
        Property(name="k7_W", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X8", type=k7_W, multiplicity=Multiplicity(0, 1))
    }
)
l4s9: BinaryAssociation = BinaryAssociation(
    name="l4s9",
    ends={
        Property(name="k7_L4", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X10", type=k7_L4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t1s11: BinaryAssociation = BinaryAssociation(
    name="t1s11",
    ends={
        Property(name="k7_T1", type=k7_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_X12", type=k7_T1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
is13: BinaryAssociation = BinaryAssociation(
    name="is13",
    ends={
        Property(name="k7_I", type=k7_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_B", type=k7_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y14: BinaryAssociation = BinaryAssociation(
    name="y14",
    ends={
        Property(name="k7_Y16", type=k7_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_B15", type=k7_Y, multiplicity=Multiplicity(0, 1))
    }
)
js25: BinaryAssociation = BinaryAssociation(
    name="js25",
    ends={
        Property(name="k7_J", type=k7_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_P26", type=k7_J, multiplicity=Multiplicity(0, 9999))
    }
)
mcs17: BinaryAssociation = BinaryAssociation(
    name="mcs17",
    ends={
        Property(name="k7_C18", type=k7_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_M", type=k7_C, multiplicity=Multiplicity(0, 9999))
    }
)
ml119: BinaryAssociation = BinaryAssociation(
    name="ml119",
    ends={
        Property(name="k7_L1", type=k7_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_M20", type=k7_L1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a21: BinaryAssociation = BinaryAssociation(
    name="a21",
    ends={
        Property(name="k7_A", type=k7_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_P22", type=k7_A, multiplicity=Multiplicity(0, 1))
    }
)
ks23: BinaryAssociation = BinaryAssociation(
    name="ks23",
    ends={
        Property(name="k7_K", type=k7_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_P24", type=k7_K, multiplicity=Multiplicity(0, 1))
    }
)
l2s27: BinaryAssociation = BinaryAssociation(
    name="l2s27",
    ends={
        Property(name="k7_L2", type=k7_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_Q", type=k7_L2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l1c28: BinaryAssociation = BinaryAssociation(
    name="l1c28",
    ends={
        Property(name="k7_C30", type=k7_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L129", type=k7_C, multiplicity=Multiplicity(0, 1))
    }
)
l1m31: BinaryAssociation = BinaryAssociation(
    name="l1m31",
    ends={
        Property(name="k7_M33", type=k7_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L132", type=k7_M, multiplicity=Multiplicity(0, 1))
    }
)
l2q34: BinaryAssociation = BinaryAssociation(
    name="l2q34",
    ends={
        Property(name="k7_Q36", type=k7_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L235", type=k7_Q, multiplicity=Multiplicity(0, 1))
    }
)
l2k37: BinaryAssociation = BinaryAssociation(
    name="l2k37",
    ends={
        Property(name="k7_K39", type=k7_L2, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L238", type=k7_K, multiplicity=Multiplicity(0, 1))
    }
)
l3z40: BinaryAssociation = BinaryAssociation(
    name="l3z40",
    ends={
        Property(name="k7_Z41", type=k7_L3, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L3", type=k7_Z, multiplicity=Multiplicity(0, 1))
    }
)
p42: BinaryAssociation = BinaryAssociation(
    name="p42",
    ends={
        Property(name="k7_P44", type=k7_L4, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L443", type=k7_P, multiplicity=Multiplicity(0, 1))
    }
)
a45: BinaryAssociation = BinaryAssociation(
    name="a45",
    ends={
        Property(name="k7_A47", type=k7_L4, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_L446", type=k7_A, multiplicity=Multiplicity(0, 1))
    }
)
fromDsml48: BinaryAssociation = BinaryAssociation(
    name="fromDsml48",
    ends={
        Property(name="k7_T149", type=k7_DsmlRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_DsmlRelation", type=k7_T1, multiplicity=Multiplicity(0, 1))
    }
)
toDsml50: BinaryAssociation = BinaryAssociation(
    name="toDsml50",
    ends={
        Property(name="k7_T152", type=k7_DsmlRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_DsmlRelation51", type=k7_T1, multiplicity=Multiplicity(0, 1))
    }
)
t2s53: BinaryAssociation = BinaryAssociation(
    name="t2s53",
    ends={
        Property(name="k7_T2", type=k7_T1, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_T154", type=k7_T2, multiplicity=Multiplicity(0, 9999))
    }
)
relateds55: BinaryAssociation = BinaryAssociation(
    name="relateds55",
    ends={
        Property(name="k7_DsmlRelation57", type=k7_T1, multiplicity=Multiplicity(1, 1)),
        Property(name="k7_T156", type=k7_DsmlRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_k7_C_G = Generalization(general=G, specific=k7_C)
gen_k7_A_B = Generalization(general=B, specific=k7_A)
gen_k7_B_C = Generalization(general=C, specific=k7_B)
gen_k7_Q_P = Generalization(general=P, specific=k7_Q)
gen_k7_M_G = Generalization(general=G, specific=k7_M)
gen_k7_N_M = Generalization(general=M, specific=k7_N)
gen_k7_J_A = Generalization(general=A, specific=k7_J)
gen_k7_P_N = Generalization(general=N, specific=k7_P)
gen_k7_I_G = Generalization(general=G, specific=k7_I)
gen_k7_K_J = Generalization(general=J, specific=k7_K)
gen_k7_L3_L1 = Generalization(general=L1, specific=k7_L3)
gen_k7_T1_T2 = Generalization(general=T2, specific=k7_T1)

# Domain Model
domain_model = DomainModel(
    name="k7",
    types={k7_P, k7_X, k7_C, G, k7_Z, k7_Y, k7_W, k7_L4, k7_T1, k7_A, B, k7_B, C, k7_I, k7_Q, P, k7_G, k7_M, k7_L1, k7_N, M, k7_J, A, N, k7_K, k7_L2, J, k7_L3, L1, k7_T2, k7_DsmlRelation, T2},
    associations={ps1, xcs0, zs3, ys5, w7, l4s9, t1s11, is13, y14, js25, mcs17, ml119, a21, ks23, l2s27, l1c28, l1m31, l2q34, l2k37, l3z40, p42, a45, fromDsml48, toDsml50, t2s53, relateds55},
    generalizations={gen_k7_C_G, gen_k7_A_B, gen_k7_B_C, gen_k7_Q_P, gen_k7_M_G, gen_k7_N_M, gen_k7_J_A, gen_k7_P_N, gen_k7_I_G, gen_k7_K_J, gen_k7_L3_L1, gen_k7_T1_T2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)