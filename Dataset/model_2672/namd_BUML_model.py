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
namd_A = Class(name="namd::A")
namd_B = Class(name="namd::B")
Named = Class(name="Named")
namd_C = Class(name="namd::C")
namd_Named = Class(name="namd::Named")
namd_D = Class(name="namd::D")
B = Class(name="B")
namd_F = Class(name="namd::F")
D = Class(name="D")
namd_G = Class(name="namd::G")
namd_H = Class(name="namd::H")
namd_I = Class(name="namd::I")
F = Class(name="F")
namd_E = Class(name="namd::E")

# namd_A class attributes and methods

# namd_B class attributes and methods

# Named class attributes and methods

# namd_C class attributes and methods

# namd_Named class attributes and methods
namd_Named_name: Property = Property(name="name", type=StringType)
namd_Named.attributes={namd_Named_name}

# namd_D class attributes and methods

# B class attributes and methods

# namd_F class attributes and methods

# D class attributes and methods

# namd_G class attributes and methods

# namd_H class attributes and methods

# namd_I class attributes and methods

# F class attributes and methods

# namd_E class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="namd_B", type=namd_A, multiplicity=Multiplicity(1, 1)),
        Property(name="namd_A", type=namd_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="namd_C", type=namd_B, multiplicity=Multiplicity(1, 1)),
        Property(name="namd_B2", type=namd_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es3: BinaryAssociation = BinaryAssociation(
    name="es3",
    ends={
        Property(name="namd_E", type=namd_D, multiplicity=Multiplicity(1, 1)),
        Property(name="namd_D", type=namd_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs4: BinaryAssociation = BinaryAssociation(
    name="gs4",
    ends={
        Property(name="namd_G", type=namd_F, multiplicity=Multiplicity(1, 1)),
        Property(name="namd_F", type=namd_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs5: BinaryAssociation = BinaryAssociation(
    name="hs5",
    ends={
        Property(name="namd_H", type=namd_F, multiplicity=Multiplicity(1, 1)),
        Property(name="namd_F6", type=namd_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_namd_B_Named = Generalization(general=Named, specific=namd_B)
gen_namd_C_Named = Generalization(general=Named, specific=namd_C)
gen_namd_D_B = Generalization(general=B, specific=namd_D)
gen_namd_E_Named = Generalization(general=Named, specific=namd_E)
gen_namd_F_D = Generalization(general=D, specific=namd_F)
gen_namd_G_Named = Generalization(general=Named, specific=namd_G)
gen_namd_I_F = Generalization(general=F, specific=namd_I)
gen_namd_H_Named = Generalization(general=Named, specific=namd_H)

# Domain Model
domain_model = DomainModel(
    name="namd",
    types={namd_A, namd_B, Named, namd_C, namd_Named, namd_D, B, namd_F, D, namd_G, namd_H, namd_I, F, namd_E},
    associations={bs0, cs1, es3, gs4, hs5},
    generalizations={gen_namd_B_Named, gen_namd_C_Named, gen_namd_D_B, gen_namd_E_Named, gen_namd_F_D, gen_namd_G_Named, gen_namd_I_F, gen_namd_H_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)