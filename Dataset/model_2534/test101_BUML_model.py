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
test101_D = Class(name="test101::D")
test101_L1 = Class(name="test101::L1")
test101_C = Class(name="test101::C")
test101_A = Class(name="test101::A")
G = Class(name="G")
test101_F = Class(name="test101::F")
B = Class(name="B")
test101_B = Class(name="test101::B")
test101_G = Class(name="test101::G")
M = Class(name="M")
test101_I = Class(name="test101::I")
test101_K = Class(name="test101::K")
test101_N = Class(name="test101::N")
test101_E = Class(name="test101::E")
D = Class(name="D")
test101_J = Class(name="test101::J")
E = Class(name="E")
test101_Q = Class(name="test101::Q")
test101_M = Class(name="test101::M")

# test101_D class attributes and methods

# test101_L1 class attributes and methods
test101_L1_since: Property = Property(name="since", type=StringType)
test101_L1.attributes={test101_L1_since}

# test101_C class attributes and methods

# test101_A class attributes and methods
test101_A_name: Property = Property(name="name", type=StringType)
test101_A.attributes={test101_A_name}

# G class attributes and methods

# test101_F class attributes and methods

# B class attributes and methods

# test101_B class attributes and methods
test101_B_id: Property = Property(name="id", type=StringType)
test101_B.attributes={test101_B_id}

# test101_G class attributes and methods

# M class attributes and methods

# test101_I class attributes and methods
test101_I_name: Property = Property(name="name", type=StringType)
test101_I.attributes={test101_I_name}

# test101_K class attributes and methods
test101_K_ids: Property = Property(name="ids", type=StringType)
test101_K.attributes={test101_K_ids}

# test101_N class attributes and methods
test101_N_id: Property = Property(name="id", type=StringType)
test101_N.attributes={test101_N_id}

# test101_E class attributes and methods

# D class attributes and methods

# test101_J class attributes and methods
test101_J_id: Property = Property(name="id", type=StringType)
test101_J.attributes={test101_J_id}

# E class attributes and methods

# test101_Q class attributes and methods
test101_Q_id: Property = Property(name="id", type=StringType)
test101_Q.attributes={test101_Q_id}

# test101_M class attributes and methods
test101_M_id: Property = Property(name="id", type=StringType)
test101_M.attributes={test101_M_id}

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="test101_C", type=test101_A, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="test101_A", type=test101_C, multiplicity=Multiplicity(1, 1))
    }
)
ds1: BinaryAssociation = BinaryAssociation(
    name="ds1",
    ends={
        Property(name="test101_D", type=test101_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_C2", type=test101_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l1s3: BinaryAssociation = BinaryAssociation(
    name="l1s3",
    ends={
        Property(name="test101_L1", type=test101_C, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_C4", type=test101_L1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs9: BinaryAssociation = BinaryAssociation(
    name="fs9",
    ends={
        Property(name="test101_F", type=test101_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_D10", type=test101_F, multiplicity=Multiplicity(0, 9999))
    }
)
gs11: BinaryAssociation = BinaryAssociation(
    name="gs11",
    ends={
        Property(name="test101_G13", type=test101_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_D12", type=test101_G, multiplicity=Multiplicity(0, 9999))
    }
)
bs5: BinaryAssociation = BinaryAssociation(
    name="bs5",
    ends={
        Property(name="test101_B", type=test101_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_A6", type=test101_B, multiplicity=Multiplicity(0, 9999))
    }
)
gs7: BinaryAssociation = BinaryAssociation(
    name="gs7",
    ends={
        Property(name="test101_G", type=test101_B, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_B8", type=test101_G, multiplicity=Multiplicity(0, 1))
    }
)
qs17: BinaryAssociation = BinaryAssociation(
    name="qs17",
    ends={
        Property(name="test101_Q", type=test101_F, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_F18", type=test101_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
is19: BinaryAssociation = BinaryAssociation(
    name="is19",
    ends={
        Property(name="test101_I", type=test101_G, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_G20", type=test101_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns14: BinaryAssociation = BinaryAssociation(
    name="ns14",
    ends={
        Property(name="test101_N", type=test101_D, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_D15", type=test101_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
js16: BinaryAssociation = BinaryAssociation(
    name="js16",
    ends={
        Property(name="test101_J", type=test101_E, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_E", type=test101_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks21: BinaryAssociation = BinaryAssociation(
    name="ks21",
    ends={
        Property(name="test101_K", type=test101_G, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_G22", type=test101_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from23: BinaryAssociation = BinaryAssociation(
    name="from23",
    ends={
        Property(name="test101_B25", type=test101_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_L124", type=test101_B, multiplicity=Multiplicity(0, 1))
    }
)
to26: BinaryAssociation = BinaryAssociation(
    name="to26",
    ends={
        Property(name="test101_G28", type=test101_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="test101_L127", type=test101_G, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_test101_D_G = Generalization(general=G, specific=test101_D)
gen_test101_A_B = Generalization(general=B, specific=test101_A)
gen_test101_G_M = Generalization(general=M, specific=test101_G)
gen_test101_E_D = Generalization(general=D, specific=test101_E)
gen_test101_F_E = Generalization(general=E, specific=test101_F)

# Domain Model
domain_model = DomainModel(
    name="test101",
    types={test101_D, test101_L1, test101_C, test101_A, G, test101_F, B, test101_B, test101_G, M, test101_I, test101_K, test101_N, test101_E, D, test101_J, E, test101_Q, test101_M},
    associations={as0, ds1, l1s3, fs9, gs11, bs5, gs7, qs17, is19, ns14, js16, ks21, from23, to26},
    generalizations={gen_test101_D_G, gen_test101_A_B, gen_test101_G_M, gen_test101_E_D, gen_test101_F_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)