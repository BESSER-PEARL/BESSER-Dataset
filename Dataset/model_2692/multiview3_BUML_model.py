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
multiview3_A = Class(name="multiview3::A")
Named = Class(name="Named")
multiview3_B = Class(name="multiview3::B")
multiview3_E = Class(name="multiview3::E")
multiview3_K = Class(name="multiview3::K")
multiview3_C = Class(name="multiview3::C")
multiview3_M = Class(name="multiview3::M")
multiview3_F = Class(name="multiview3::F")
multiview3_H = Class(name="multiview3::H")
multiview3_Named = Class(name="multiview3::Named")
multiview3_W = Class(name="multiview3::W")

# multiview3_A class attributes and methods

# Named class attributes and methods

# multiview3_B class attributes and methods

# multiview3_E class attributes and methods

# multiview3_K class attributes and methods

# multiview3_C class attributes and methods

# multiview3_M class attributes and methods

# multiview3_F class attributes and methods

# multiview3_H class attributes and methods

# multiview3_Named class attributes and methods
multiview3_Named_name: Property = Property(name="name", type=StringType)
multiview3_Named.attributes={multiview3_Named_name}

# multiview3_W class attributes and methods

# Relationships
cs5: BinaryAssociation = BinaryAssociation(
    name="cs5",
    ends={
        Property(name="multiview3_C", type=multiview3_B, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_B6", type=multiview3_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="multiview3_B", type=multiview3_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_A", type=multiview3_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="multiview3_E", type=multiview3_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_A2", type=multiview3_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aks3: BinaryAssociation = BinaryAssociation(
    name="aks3",
    ends={
        Property(name="multiview3_K", type=multiview3_A, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_A4", type=multiview3_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms19: BinaryAssociation = BinaryAssociation(
    name="ms19",
    ends={
        Property(name="multiview3_M", type=multiview3_F, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_F20", type=multiview3_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bfs7: BinaryAssociation = BinaryAssociation(
    name="bfs7",
    ends={
        Property(name="multiview3_F", type=multiview3_B, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_B8", type=multiview3_F, multiplicity=Multiplicity(0, 1))
    }
)
hs9: BinaryAssociation = BinaryAssociation(
    name="hs9",
    ends={
        Property(name="multiview3_H", type=multiview3_C, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_C10", type=multiview3_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks11: BinaryAssociation = BinaryAssociation(
    name="ks11",
    ends={
        Property(name="multiview3_K13", type=multiview3_C, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_C12", type=multiview3_K, multiplicity=Multiplicity(0, 9999))
    }
)
fs14: BinaryAssociation = BinaryAssociation(
    name="fs14",
    ends={
        Property(name="multiview3_F16", type=multiview3_E, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_E15", type=multiview3_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws17: BinaryAssociation = BinaryAssociation(
    name="ws17",
    ends={
        Property(name="multiview3_W", type=multiview3_E, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_E18", type=multiview3_W, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wc21: BinaryAssociation = BinaryAssociation(
    name="wc21",
    ends={
        Property(name="multiview3_C23", type=multiview3_W, multiplicity=Multiplicity(1, 1)),
        Property(name="multiview3_W22", type=multiview3_C, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_multiview3_A_Named = Generalization(general=Named, specific=multiview3_A)
gen_multiview3_B_Named = Generalization(general=Named, specific=multiview3_B)
gen_multiview3_C_Named = Generalization(general=Named, specific=multiview3_C)
gen_multiview3_E_Named = Generalization(general=Named, specific=multiview3_E)
gen_multiview3_F_Named = Generalization(general=Named, specific=multiview3_F)
gen_multiview3_H_Named = Generalization(general=Named, specific=multiview3_H)
gen_multiview3_K_Named = Generalization(general=Named, specific=multiview3_K)
gen_multiview3_M_Named = Generalization(general=Named, specific=multiview3_M)
gen_multiview3_W_Named = Generalization(general=Named, specific=multiview3_W)

# Domain Model
domain_model = DomainModel(
    name="multiview3",
    types={multiview3_A, Named, multiview3_B, multiview3_E, multiview3_K, multiview3_C, multiview3_M, multiview3_F, multiview3_H, multiview3_Named, multiview3_W},
    associations={cs5, bs0, es1, aks3, ms19, bfs7, hs9, ks11, fs14, ws17, wc21},
    generalizations={gen_multiview3_A_Named, gen_multiview3_B_Named, gen_multiview3_C_Named, gen_multiview3_E_Named, gen_multiview3_F_Named, gen_multiview3_H_Named, gen_multiview3_K_Named, gen_multiview3_M_Named, gen_multiview3_W_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)