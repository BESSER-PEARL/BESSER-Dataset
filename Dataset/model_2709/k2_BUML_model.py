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
k2_C = Class(name="k2::C", is_abstract=True)
k2_P = Class(name="k2::P")
k2_A = Class(name="k2::A")
k2_X = Class(name="k2::X")
k2_J = Class(name="k2::J")
A = Class(name="A")
N = Class(name="N")
B = Class(name="B")
k2_B = Class(name="k2::B")
C = Class(name="C")
k2_I = Class(name="k2::I")
G = Class(name="G")
k2_G = Class(name="k2::G", is_abstract=True)
k2_M = Class(name="k2::M")
k2_N = Class(name="k2::N")
M = Class(name="M")
k2_Q = Class(name="k2::Q")
P = Class(name="P")

# k2_C class attributes and methods

# k2_P class attributes and methods

# k2_A class attributes and methods

# k2_X class attributes and methods

# k2_J class attributes and methods

# A class attributes and methods

# N class attributes and methods

# B class attributes and methods

# k2_B class attributes and methods

# C class attributes and methods

# k2_I class attributes and methods

# G class attributes and methods

# k2_G class attributes and methods
k2_G_name: Property = Property(name="name", type=StringType)
k2_G.attributes={k2_G_name}

# k2_M class attributes and methods

# k2_N class attributes and methods

# M class attributes and methods

# k2_Q class attributes and methods

# P class attributes and methods

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="k2_C", type=k2_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k2_X", type=k2_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps1: BinaryAssociation = BinaryAssociation(
    name="ps1",
    ends={
        Property(name="k2_P", type=k2_X, multiplicity=Multiplicity(1, 1)),
        Property(name="k2_X2", type=k2_P, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a6: BinaryAssociation = BinaryAssociation(
    name="a6",
    ends={
        Property(name="k2_A", type=k2_P, multiplicity=Multiplicity(1, 1)),
        Property(name="k2_P7", type=k2_A, multiplicity=Multiplicity(0, 1))
    }
)
is3: BinaryAssociation = BinaryAssociation(
    name="is3",
    ends={
        Property(name="k2_I", type=k2_B, multiplicity=Multiplicity(1, 1)),
        Property(name="k2_B", type=k2_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs4: BinaryAssociation = BinaryAssociation(
    name="cs4",
    ends={
        Property(name="k2_C5", type=k2_M, multiplicity=Multiplicity(1, 1)),
        Property(name="k2_M", type=k2_C, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_k2_J_A = Generalization(general=A, specific=k2_J)
gen_k2_P_N = Generalization(general=N, specific=k2_P)
gen_k2_A_B = Generalization(general=B, specific=k2_A)
gen_k2_B_C = Generalization(general=C, specific=k2_B)
gen_k2_C_G = Generalization(general=G, specific=k2_C)
gen_k2_M_G = Generalization(general=G, specific=k2_M)
gen_k2_N_M = Generalization(general=M, specific=k2_N)
gen_k2_Q_P = Generalization(general=P, specific=k2_Q)
gen_k2_I_G = Generalization(general=G, specific=k2_I)

# Domain Model
domain_model = DomainModel(
    name="k2",
    types={k2_C, k2_P, k2_A, k2_X, k2_J, A, N, B, k2_B, C, k2_I, G, k2_G, k2_M, k2_N, M, k2_Q, P},
    associations={cs0, ps1, a6, is3, cs4},
    generalizations={gen_k2_J_A, gen_k2_P_N, gen_k2_A_B, gen_k2_B_C, gen_k2_C_G, gen_k2_M_G, gen_k2_N_M, gen_k2_Q_P, gen_k2_I_G},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)