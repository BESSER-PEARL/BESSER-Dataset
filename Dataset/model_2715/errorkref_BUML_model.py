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
errorkref_C = Class(name="errorkref::C")
errorkref_A = Class(name="errorkref::A")
errorkref_D = Class(name="errorkref::D")
errorkref_L1 = Class(name="errorkref::L1")
errorkref_B = Class(name="errorkref::B")
errorkref_G = Class(name="errorkref::G")
B = Class(name="B")
errorkref_F = Class(name="errorkref::F")
errorkref_N = Class(name="errorkref::N")
errorkref_E = Class(name="errorkref::E")
D = Class(name="D")
G = Class(name="G")
E = Class(name="E")
errorkref_Q = Class(name="errorkref::Q")
M = Class(name="M")
errorkref_K = Class(name="errorkref::K")
errorkref_J = Class(name="errorkref::J")
errorkref_I = Class(name="errorkref::I")
errorkref_M = Class(name="errorkref::M")

# errorkref_C class attributes and methods

# errorkref_A class attributes and methods
errorkref_A_name: Property = Property(name="name", type=StringType)
errorkref_A.attributes={errorkref_A_name}

# errorkref_D class attributes and methods

# errorkref_L1 class attributes and methods
errorkref_L1_since: Property = Property(name="since", type=StringType)
errorkref_L1.attributes={errorkref_L1_since}

# errorkref_B class attributes and methods
errorkref_B_id: Property = Property(name="id", type=StringType)
errorkref_B.attributes={errorkref_B_id}

# errorkref_G class attributes and methods

# B class attributes and methods

# errorkref_F class attributes and methods

# errorkref_N class attributes and methods
errorkref_N_id: Property = Property(name="id", type=StringType)
errorkref_N.attributes={errorkref_N_id}

# errorkref_E class attributes and methods

# D class attributes and methods

# G class attributes and methods

# E class attributes and methods

# errorkref_Q class attributes and methods
errorkref_Q_id: Property = Property(name="id", type=StringType)
errorkref_Q.attributes={errorkref_Q_id}

# M class attributes and methods

# errorkref_K class attributes and methods
errorkref_K_ids: Property = Property(name="ids", type=StringType)
errorkref_K.attributes={errorkref_K_ids}

# errorkref_J class attributes and methods
errorkref_J_id: Property = Property(name="id", type=StringType)
errorkref_J.attributes={errorkref_J_id}

# errorkref_I class attributes and methods
errorkref_I_name: Property = Property(name="name", type=StringType)
errorkref_I.attributes={errorkref_I_name}

# errorkref_M class attributes and methods
errorkref_M_id: Property = Property(name="id", type=StringType)
errorkref_M.attributes={errorkref_M_id}

# Relationships
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="errorkref_A", type=errorkref_C, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_C", type=errorkref_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds1: BinaryAssociation = BinaryAssociation(
    name="ds1",
    ends={
        Property(name="errorkref_D", type=errorkref_C, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_C2", type=errorkref_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
l1s3: BinaryAssociation = BinaryAssociation(
    name="l1s3",
    ends={
        Property(name="errorkref_L1", type=errorkref_C, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_C4", type=errorkref_L1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs5: BinaryAssociation = BinaryAssociation(
    name="bs5",
    ends={
        Property(name="errorkref_B", type=errorkref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_A6", type=errorkref_B, multiplicity=Multiplicity(0, 9999))
    }
)
fs9: BinaryAssociation = BinaryAssociation(
    name="fs9",
    ends={
        Property(name="errorkref_F", type=errorkref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_D10", type=errorkref_F, multiplicity=Multiplicity(0, 9999))
    }
)
gs11: BinaryAssociation = BinaryAssociation(
    name="gs11",
    ends={
        Property(name="errorkref_G13", type=errorkref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_D12", type=errorkref_G, multiplicity=Multiplicity(0, 9999))
    }
)
ns14: BinaryAssociation = BinaryAssociation(
    name="ns14",
    ends={
        Property(name="errorkref_N", type=errorkref_D, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_D15", type=errorkref_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs7: BinaryAssociation = BinaryAssociation(
    name="gs7",
    ends={
        Property(name="errorkref_G", type=errorkref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_B8", type=errorkref_G, multiplicity=Multiplicity(0, 1))
    }
)
js16: BinaryAssociation = BinaryAssociation(
    name="js16",
    ends={
        Property(name="errorkref_J", type=errorkref_E, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_E", type=errorkref_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qs17: BinaryAssociation = BinaryAssociation(
    name="qs17",
    ends={
        Property(name="errorkref_Q", type=errorkref_F, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_F18", type=errorkref_Q, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks19: BinaryAssociation = BinaryAssociation(
    name="ks19",
    ends={
        Property(name="errorkref_K", type=errorkref_G, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_G20", type=errorkref_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from21: BinaryAssociation = BinaryAssociation(
    name="from21",
    ends={
        Property(name="errorkref_B23", type=errorkref_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_L122", type=errorkref_B, multiplicity=Multiplicity(0, 1))
    }
)
to24: BinaryAssociation = BinaryAssociation(
    name="to24",
    ends={
        Property(name="errorkref_G26", type=errorkref_L1, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_L125", type=errorkref_G, multiplicity=Multiplicity(0, 1))
    }
)
is27: BinaryAssociation = BinaryAssociation(
    name="is27",
    ends={
        Property(name="errorkref_I", type=errorkref_M, multiplicity=Multiplicity(1, 1)),
        Property(name="errorkref_M", type=errorkref_I, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_errorkref_A_B = Generalization(general=B, specific=errorkref_A)
gen_errorkref_E_D = Generalization(general=D, specific=errorkref_E)
gen_errorkref_D_G = Generalization(general=G, specific=errorkref_D)
gen_errorkref_F_E = Generalization(general=E, specific=errorkref_F)
gen_errorkref_G_M = Generalization(general=M, specific=errorkref_G)

# Domain Model
domain_model = DomainModel(
    name="errorkref",
    types={errorkref_C, errorkref_A, errorkref_D, errorkref_L1, errorkref_B, errorkref_G, B, errorkref_F, errorkref_N, errorkref_E, D, G, E, errorkref_Q, M, errorkref_K, errorkref_J, errorkref_I, errorkref_M},
    associations={as0, ds1, l1s3, bs5, fs9, gs11, ns14, gs7, js16, qs17, ks19, from21, to24, is27},
    generalizations={gen_errorkref_A_B, gen_errorkref_E_D, gen_errorkref_D_G, gen_errorkref_F_E, gen_errorkref_G_M},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)