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
compmultinher_K = Class(name="compmultinher::K")
Named = Class(name="Named")
compmultinher_C = Class(name="compmultinher::C")
compmultinher_Named = Class(name="compmultinher::Named")
compmultinher_D = Class(name="compmultinher::D")
B = Class(name="B")
compmultinher_A = Class(name="compmultinher::A")
compmultinher_B = Class(name="compmultinher::B")
compmultinher_G = Class(name="compmultinher::G")
compmultinher_H = Class(name="compmultinher::H")
compmultinher_I = Class(name="compmultinher::I")
F = Class(name="F")
K = Class(name="K")
compmultinher_E = Class(name="compmultinher::E")
compmultinher_F = Class(name="compmultinher::F")
D = Class(name="D")
compmultinher_L = Class(name="compmultinher::L")

# compmultinher_K class attributes and methods

# Named class attributes and methods

# compmultinher_C class attributes and methods

# compmultinher_Named class attributes and methods
compmultinher_Named_name: Property = Property(name="name", type=StringType)
compmultinher_Named.attributes={compmultinher_Named_name}

# compmultinher_D class attributes and methods

# B class attributes and methods

# compmultinher_A class attributes and methods

# compmultinher_B class attributes and methods

# compmultinher_G class attributes and methods

# compmultinher_H class attributes and methods

# compmultinher_I class attributes and methods

# F class attributes and methods

# K class attributes and methods

# compmultinher_E class attributes and methods

# compmultinher_F class attributes and methods

# D class attributes and methods

# compmultinher_L class attributes and methods

# Relationships
ks1: BinaryAssociation = BinaryAssociation(
    name="ks1",
    ends={
        Property(name="compmultinher_K", type=compmultinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_A2", type=compmultinher_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="compmultinher_C", type=compmultinher_B, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_B4", type=compmultinher_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="compmultinher_B", type=compmultinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_A", type=compmultinher_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs6: BinaryAssociation = BinaryAssociation(
    name="gs6",
    ends={
        Property(name="compmultinher_G", type=compmultinher_F, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_F", type=compmultinher_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs7: BinaryAssociation = BinaryAssociation(
    name="hs7",
    ends={
        Property(name="compmultinher_H", type=compmultinher_F, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_F8", type=compmultinher_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es5: BinaryAssociation = BinaryAssociation(
    name="es5",
    ends={
        Property(name="compmultinher_E", type=compmultinher_D, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_D", type=compmultinher_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ls9: BinaryAssociation = BinaryAssociation(
    name="ls9",
    ends={
        Property(name="compmultinher_L", type=compmultinher_K, multiplicity=Multiplicity(1, 1)),
        Property(name="compmultinher_K10", type=compmultinher_L, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_compmultinher_B_Named = Generalization(general=Named, specific=compmultinher_B)
gen_compmultinher_C_Named = Generalization(general=Named, specific=compmultinher_C)
gen_compmultinher_D_B = Generalization(general=B, specific=compmultinher_D)
gen_compmultinher_F_D = Generalization(general=D, specific=compmultinher_F)
gen_compmultinher_G_Named = Generalization(general=Named, specific=compmultinher_G)
gen_compmultinher_I_F = Generalization(general=F, specific=compmultinher_I)
gen_compmultinher_I_K = Generalization(general=K, specific=compmultinher_I)
gen_compmultinher_H_Named = Generalization(general=Named, specific=compmultinher_H)
gen_compmultinher_K_Named = Generalization(general=Named, specific=compmultinher_K)
gen_compmultinher_E_Named = Generalization(general=Named, specific=compmultinher_E)
gen_compmultinher_L_Named = Generalization(general=Named, specific=compmultinher_L)

# Domain Model
domain_model = DomainModel(
    name="compmultinher",
    types={compmultinher_K, Named, compmultinher_C, compmultinher_Named, compmultinher_D, B, compmultinher_A, compmultinher_B, compmultinher_G, compmultinher_H, compmultinher_I, F, K, compmultinher_E, compmultinher_F, D, compmultinher_L},
    associations={ks1, cs3, bs0, gs6, hs7, es5, ls9},
    generalizations={gen_compmultinher_B_Named, gen_compmultinher_C_Named, gen_compmultinher_D_B, gen_compmultinher_F_D, gen_compmultinher_G_Named, gen_compmultinher_I_F, gen_compmultinher_I_K, gen_compmultinher_H_Named, gen_compmultinher_K_Named, gen_compmultinher_E_Named, gen_compmultinher_L_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)