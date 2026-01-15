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
refinher_Named = Class(name="refinher::Named")
refinher_A = Class(name="refinher::A")
refinher_B = Class(name="refinher::B")
refinher_K = Class(name="refinher::K")
Named = Class(name="Named")
refinher_C = Class(name="refinher::C")
refinher_D = Class(name="refinher::D")
B = Class(name="B")
refinher_E = Class(name="refinher::E")
refinher_F = Class(name="refinher::F")
D = Class(name="D")
refinher_G = Class(name="refinher::G")
refinher_H = Class(name="refinher::H")
refinher_I = Class(name="refinher::I")
F = Class(name="F")
K = Class(name="K")
refinher_L = Class(name="refinher::L")

# refinher_Named class attributes and methods
refinher_Named_name: Property = Property(name="name", type=StringType)
refinher_Named.attributes={refinher_Named_name}

# refinher_A class attributes and methods

# refinher_B class attributes and methods

# refinher_K class attributes and methods

# Named class attributes and methods

# refinher_C class attributes and methods

# refinher_D class attributes and methods

# B class attributes and methods

# refinher_E class attributes and methods

# refinher_F class attributes and methods

# D class attributes and methods

# refinher_G class attributes and methods

# refinher_H class attributes and methods

# refinher_I class attributes and methods

# F class attributes and methods

# K class attributes and methods

# refinher_L class attributes and methods

# Relationships
nameds3: BinaryAssociation = BinaryAssociation(
    name="nameds3",
    ends={
        Property(name="refinher_Named", type=refinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_A4", type=refinher_Named, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="refinher_B", type=refinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_A", type=refinher_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks1: BinaryAssociation = BinaryAssociation(
    name="ks1",
    ends={
        Property(name="refinher_K", type=refinher_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_A2", type=refinher_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs5: BinaryAssociation = BinaryAssociation(
    name="cs5",
    ends={
        Property(name="refinher_C", type=refinher_B, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_B6", type=refinher_C, multiplicity=Multiplicity(0, 9999))
    }
)
es7: BinaryAssociation = BinaryAssociation(
    name="es7",
    ends={
        Property(name="refinher_E", type=refinher_D, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_D", type=refinher_E, multiplicity=Multiplicity(0, 9999))
    }
)
gs8: BinaryAssociation = BinaryAssociation(
    name="gs8",
    ends={
        Property(name="refinher_G", type=refinher_F, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_F", type=refinher_G, multiplicity=Multiplicity(0, 9999))
    }
)
hs9: BinaryAssociation = BinaryAssociation(
    name="hs9",
    ends={
        Property(name="refinher_H", type=refinher_F, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_F10", type=refinher_H, multiplicity=Multiplicity(0, 9999))
    }
)
ls11: BinaryAssociation = BinaryAssociation(
    name="ls11",
    ends={
        Property(name="refinher_L", type=refinher_K, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher_K12", type=refinher_L, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_refinher_B_Named = Generalization(general=Named, specific=refinher_B)
gen_refinher_C_Named = Generalization(general=Named, specific=refinher_C)
gen_refinher_D_B = Generalization(general=B, specific=refinher_D)
gen_refinher_E_Named = Generalization(general=Named, specific=refinher_E)
gen_refinher_F_D = Generalization(general=D, specific=refinher_F)
gen_refinher_G_Named = Generalization(general=Named, specific=refinher_G)
gen_refinher_I_F = Generalization(general=F, specific=refinher_I)
gen_refinher_I_K = Generalization(general=K, specific=refinher_I)
gen_refinher_H_Named = Generalization(general=Named, specific=refinher_H)
gen_refinher_K_Named = Generalization(general=Named, specific=refinher_K)
gen_refinher_L_Named = Generalization(general=Named, specific=refinher_L)

# Domain Model
domain_model = DomainModel(
    name="refinher",
    types={refinher_Named, refinher_A, refinher_B, refinher_K, Named, refinher_C, refinher_D, B, refinher_E, refinher_F, D, refinher_G, refinher_H, refinher_I, F, K, refinher_L},
    associations={nameds3, bs0, ks1, cs5, es7, gs8, hs9, ls11},
    generalizations={gen_refinher_B_Named, gen_refinher_C_Named, gen_refinher_D_B, gen_refinher_E_Named, gen_refinher_F_D, gen_refinher_G_Named, gen_refinher_I_F, gen_refinher_I_K, gen_refinher_H_Named, gen_refinher_K_Named, gen_refinher_L_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)