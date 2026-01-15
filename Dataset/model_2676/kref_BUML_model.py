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
kref_A = Class(name="kref::A")
Named = Class(name="Named")
kref_B = Class(name="kref::B")
kref_K = Class(name="kref::K")
kref_Named = Class(name="kref::Named")
kref_E = Class(name="kref::E")
B = Class(name="B")
kref_F = Class(name="kref::F")
kref_J = Class(name="kref::J")
kref_C = Class(name="kref::C")
kref_G = Class(name="kref::G")
kref_H = Class(name="kref::H")

# kref_A class attributes and methods

# Named class attributes and methods

# kref_B class attributes and methods

# kref_K class attributes and methods

# kref_Named class attributes and methods
kref_Named_name: Property = Property(name="name", type=StringType)
kref_Named.attributes={kref_Named_name}

# kref_E class attributes and methods

# B class attributes and methods

# kref_F class attributes and methods

# kref_J class attributes and methods

# kref_C class attributes and methods

# kref_G class attributes and methods

# kref_H class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="kref_B", type=kref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_A", type=kref_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ks1: BinaryAssociation = BinaryAssociation(
    name="ks1",
    ends={
        Property(name="kref_K", type=kref_A, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_A2", type=kref_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs7: BinaryAssociation = BinaryAssociation(
    name="fs7",
    ends={
        Property(name="kref_F", type=kref_E, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_E", type=kref_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
js8: BinaryAssociation = BinaryAssociation(
    name="js8",
    ends={
        Property(name="kref_J", type=kref_F, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_F9", type=kref_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs3: BinaryAssociation = BinaryAssociation(
    name="cs3",
    ends={
        Property(name="kref_C", type=kref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_B4", type=kref_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gs5: BinaryAssociation = BinaryAssociation(
    name="gs5",
    ends={
        Property(name="kref_G", type=kref_B, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_B6", type=kref_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hs13: BinaryAssociation = BinaryAssociation(
    name="hs13",
    ends={
        Property(name="kref_H", type=kref_G, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_G14", type=kref_H, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
k10: BinaryAssociation = BinaryAssociation(
    name="k10",
    ends={
        Property(name="kref_K12", type=kref_F, multiplicity=Multiplicity(1, 1)),
        Property(name="kref_F11", type=kref_K, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_kref_A_Named = Generalization(general=Named, specific=kref_A)
gen_kref_B_Named = Generalization(general=Named, specific=kref_B)
gen_kref_E_Named = Generalization(general=Named, specific=kref_E)
gen_kref_E_B = Generalization(general=B, specific=kref_E)
gen_kref_F_Named = Generalization(general=Named, specific=kref_F)
gen_kref_C_Named = Generalization(general=Named, specific=kref_C)
gen_kref_H_Named = Generalization(general=Named, specific=kref_H)
gen_kref_J_Named = Generalization(general=Named, specific=kref_J)
gen_kref_K_Named = Generalization(general=Named, specific=kref_K)
gen_kref_G_Named = Generalization(general=Named, specific=kref_G)

# Domain Model
domain_model = DomainModel(
    name="kref",
    types={kref_A, Named, kref_B, kref_K, kref_Named, kref_E, B, kref_F, kref_J, kref_C, kref_G, kref_H},
    associations={bs0, ks1, fs7, js8, cs3, gs5, hs13, k10},
    generalizations={gen_kref_A_Named, gen_kref_B_Named, gen_kref_E_Named, gen_kref_E_B, gen_kref_F_Named, gen_kref_C_Named, gen_kref_H_Named, gen_kref_J_Named, gen_kref_K_Named, gen_kref_G_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)