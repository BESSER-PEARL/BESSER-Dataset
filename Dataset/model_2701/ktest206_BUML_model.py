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
ktest206_A = Class(name="ktest206::A", is_abstract=True)
B = Class(name="B")
ktest206_B = Class(name="ktest206::B", is_abstract=True)
N = Class(name="N")
ktest206_C = Class(name="ktest206::C")
ktest206_N = Class(name="ktest206::N")
ktest206_D = Class(name="ktest206::D")
ktest206_X = Class(name="ktest206::X")
Y = Class(name="Y")
ktest206_W = Class(name="ktest206::W")
ktest206_Y = Class(name="ktest206::Y", is_abstract=True)
A = Class(name="A")
ktest206_E = Class(name="ktest206::E")
ktest206_V = Class(name="ktest206::V")

# ktest206_A class attributes and methods

# B class attributes and methods

# ktest206_B class attributes and methods

# N class attributes and methods

# ktest206_C class attributes and methods
ktest206_C_name: Property = Property(name="name", type=StringType)
ktest206_C.attributes={ktest206_C_name}

# ktest206_N class attributes and methods
ktest206_N_name: Property = Property(name="name", type=StringType)
ktest206_N.attributes={ktest206_N_name}

# ktest206_D class attributes and methods
ktest206_D_name: Property = Property(name="name", type=StringType)
ktest206_D.attributes={ktest206_D_name}

# ktest206_X class attributes and methods

# Y class attributes and methods

# ktest206_W class attributes and methods

# ktest206_Y class attributes and methods

# A class attributes and methods

# ktest206_E class attributes and methods

# ktest206_V class attributes and methods

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="ktest206_C", type=ktest206_B, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest206_B", type=ktest206_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ds1: BinaryAssociation = BinaryAssociation(
    name="ds1",
    ends={
        Property(name="ktest206_D", type=ktest206_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest206_A", type=ktest206_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws2: BinaryAssociation = BinaryAssociation(
    name="ws2",
    ends={
        Property(name="ktest206_W", type=ktest206_X, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest206_X", type=ktest206_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es3: BinaryAssociation = BinaryAssociation(
    name="es3",
    ends={
        Property(name="ktest206_E", type=ktest206_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest206_Y", type=ktest206_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vs4: BinaryAssociation = BinaryAssociation(
    name="vs4",
    ends={
        Property(name="ktest206_V", type=ktest206_W, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest206_W5", type=ktest206_V, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ktest206_A_B = Generalization(general=B, specific=ktest206_A)
gen_ktest206_B_N = Generalization(general=N, specific=ktest206_B)
gen_ktest206_W_N = Generalization(general=N, specific=ktest206_W)
gen_ktest206_X_Y = Generalization(general=Y, specific=ktest206_X)
gen_ktest206_Y_A = Generalization(general=A, specific=ktest206_Y)
gen_ktest206_E_N = Generalization(general=N, specific=ktest206_E)
gen_ktest206_V_Y = Generalization(general=Y, specific=ktest206_V)

# Domain Model
domain_model = DomainModel(
    name="ktest206",
    types={ktest206_A, B, ktest206_B, N, ktest206_C, ktest206_N, ktest206_D, ktest206_X, Y, ktest206_W, ktest206_Y, A, ktest206_E, ktest206_V},
    associations={cs0, ds1, ws2, es3, vs4},
    generalizations={gen_ktest206_A_B, gen_ktest206_B_N, gen_ktest206_W_N, gen_ktest206_X_Y, gen_ktest206_Y_A, gen_ktest206_E_N, gen_ktest206_V_Y},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)