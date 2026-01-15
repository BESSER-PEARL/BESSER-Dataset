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
manypov_A = Class(name="manypov::A")
Named = Class(name="Named")
manypov_B = Class(name="manypov::B")
manypov_E = Class(name="manypov::E")
manypov_J = Class(name="manypov::J")
manypov_C = Class(name="manypov::C")
manypov_Named = Class(name="manypov::Named")
manypov_F = Class(name="manypov::F")
manypov_JK = Class(name="manypov::JK")
manypov_M = Class(name="manypov::M")
manypov_K = Class(name="manypov::K")

# manypov_A class attributes and methods

# Named class attributes and methods

# manypov_B class attributes and methods

# manypov_E class attributes and methods

# manypov_J class attributes and methods

# manypov_C class attributes and methods

# manypov_Named class attributes and methods
manypov_Named_name: Property = Property(name="name", type=StringType)
manypov_Named.attributes={manypov_Named_name}

# manypov_F class attributes and methods

# manypov_JK class attributes and methods

# manypov_M class attributes and methods

# manypov_K class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="manypov_B", type=manypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_A", type=manypov_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="manypov_E", type=manypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_A2", type=manypov_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs5: BinaryAssociation = BinaryAssociation(
    name="cs5",
    ends={
        Property(name="manypov_C", type=manypov_B, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_B6", type=manypov_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs7: BinaryAssociation = BinaryAssociation(
    name="fs7",
    ends={
        Property(name="manypov_F", type=manypov_E, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_E8", type=manypov_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
js3: BinaryAssociation = BinaryAssociation(
    name="js3",
    ends={
        Property(name="manypov_J", type=manypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_A4", type=manypov_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms11: BinaryAssociation = BinaryAssociation(
    name="ms11",
    ends={
        Property(name="manypov_M", type=manypov_K, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_K", type=manypov_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs12: BinaryAssociation = BinaryAssociation(
    name="cs12",
    ends={
        Property(name="manypov_C14", type=manypov_K, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_K13", type=manypov_C, multiplicity=Multiplicity(0, 1))
    }
)
ks15: BinaryAssociation = BinaryAssociation(
    name="ks15",
    ends={
        Property(name="manypov_K17", type=manypov_JK, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_JK16", type=manypov_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jks9: BinaryAssociation = BinaryAssociation(
    name="jks9",
    ends={
        Property(name="manypov_JK", type=manypov_J, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov_J10", type=manypov_JK, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_manypov_A_Named = Generalization(general=Named, specific=manypov_A)
gen_manypov_C_Named = Generalization(general=Named, specific=manypov_C)
gen_manypov_E_Named = Generalization(general=Named, specific=manypov_E)
gen_manypov_F_Named = Generalization(general=Named, specific=manypov_F)
gen_manypov_J_Named = Generalization(general=Named, specific=manypov_J)
gen_manypov_B_Named = Generalization(general=Named, specific=manypov_B)
gen_manypov_JK_Named = Generalization(general=Named, specific=manypov_JK)
gen_manypov_M_Named = Generalization(general=Named, specific=manypov_M)
gen_manypov_K_Named = Generalization(general=Named, specific=manypov_K)

# Domain Model
domain_model = DomainModel(
    name="manypov",
    types={manypov_A, Named, manypov_B, manypov_E, manypov_J, manypov_C, manypov_Named, manypov_F, manypov_JK, manypov_M, manypov_K},
    associations={bs0, es1, cs5, fs7, js3, ms11, cs12, ks15, jks9},
    generalizations={gen_manypov_A_Named, gen_manypov_C_Named, gen_manypov_E_Named, gen_manypov_F_Named, gen_manypov_J_Named, gen_manypov_B_Named, gen_manypov_JK_Named, gen_manypov_M_Named, gen_manypov_K_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)