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
manypov2_A = Class(name="manypov2::A")
Named = Class(name="Named")
manypov2_B = Class(name="manypov2::B")
manypov2_C = Class(name="manypov2::C")
manypov2_Named = Class(name="manypov2::Named")
manypov2_F = Class(name="manypov2::F")
manypov2_JK = Class(name="manypov2::JK")
manypov2_M = Class(name="manypov2::M")
manypov2_N = Class(name="manypov2::N")
manypov2_E = Class(name="manypov2::E")
manypov2_J = Class(name="manypov2::J")
manypov2_K = Class(name="manypov2::K")

# manypov2_A class attributes and methods

# Named class attributes and methods

# manypov2_B class attributes and methods

# manypov2_C class attributes and methods

# manypov2_Named class attributes and methods
manypov2_Named_name: Property = Property(name="name", type=StringType)
manypov2_Named.attributes={manypov2_Named_name}

# manypov2_F class attributes and methods

# manypov2_JK class attributes and methods

# manypov2_M class attributes and methods

# manypov2_N class attributes and methods

# manypov2_E class attributes and methods

# manypov2_J class attributes and methods

# manypov2_K class attributes and methods

# Relationships
abs0: BinaryAssociation = BinaryAssociation(
    name="abs0",
    ends={
        Property(name="manypov2_B", type=manypov2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_A", type=manypov2_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bcs7: BinaryAssociation = BinaryAssociation(
    name="bcs7",
    ends={
        Property(name="manypov2_C", type=manypov2_B, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_B8", type=manypov2_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
efs9: BinaryAssociation = BinaryAssociation(
    name="efs9",
    ends={
        Property(name="manypov2_F", type=manypov2_E, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_E10", type=manypov2_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jks11: BinaryAssociation = BinaryAssociation(
    name="jks11",
    ends={
        Property(name="manypov2_JK", type=manypov2_J, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_J12", type=manypov2_JK, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kms13: BinaryAssociation = BinaryAssociation(
    name="kms13",
    ends={
        Property(name="manypov2_M", type=manypov2_K, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_K14", type=manypov2_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kns15: BinaryAssociation = BinaryAssociation(
    name="kns15",
    ends={
        Property(name="manypov2_N", type=manypov2_K, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_K16", type=manypov2_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aes1: BinaryAssociation = BinaryAssociation(
    name="aes1",
    ends={
        Property(name="manypov2_E", type=manypov2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_A2", type=manypov2_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ajs3: BinaryAssociation = BinaryAssociation(
    name="ajs3",
    ends={
        Property(name="manypov2_J", type=manypov2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_A4", type=manypov2_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aks5: BinaryAssociation = BinaryAssociation(
    name="aks5",
    ends={
        Property(name="manypov2_K", type=manypov2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_A6", type=manypov2_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jkk17: BinaryAssociation = BinaryAssociation(
    name="jkk17",
    ends={
        Property(name="manypov2_K19", type=manypov2_JK, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_JK18", type=manypov2_K, multiplicity=Multiplicity(0, 1))
    }
)
mns20: BinaryAssociation = BinaryAssociation(
    name="mns20",
    ends={
        Property(name="manypov2_N22", type=manypov2_M, multiplicity=Multiplicity(1, 1)),
        Property(name="manypov2_M21", type=manypov2_N, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_manypov2_A_Named = Generalization(general=Named, specific=manypov2_A)
gen_manypov2_C_Named = Generalization(general=Named, specific=manypov2_C)
gen_manypov2_E_Named = Generalization(general=Named, specific=manypov2_E)
gen_manypov2_F_Named = Generalization(general=Named, specific=manypov2_F)
gen_manypov2_J_Named = Generalization(general=Named, specific=manypov2_J)
gen_manypov2_K_Named = Generalization(general=Named, specific=manypov2_K)
gen_manypov2_JK_Named = Generalization(general=Named, specific=manypov2_JK)
gen_manypov2_B_Named = Generalization(general=Named, specific=manypov2_B)
gen_manypov2_M_Named = Generalization(general=Named, specific=manypov2_M)
gen_manypov2_N_Named = Generalization(general=Named, specific=manypov2_N)

# Domain Model
domain_model = DomainModel(
    name="manypov2",
    types={manypov2_A, Named, manypov2_B, manypov2_C, manypov2_Named, manypov2_F, manypov2_JK, manypov2_M, manypov2_N, manypov2_E, manypov2_J, manypov2_K},
    associations={abs0, bcs7, efs9, jks11, kms13, kns15, aes1, ajs3, aks5, jkk17, mns20},
    generalizations={gen_manypov2_A_Named, gen_manypov2_C_Named, gen_manypov2_E_Named, gen_manypov2_F_Named, gen_manypov2_J_Named, gen_manypov2_K_Named, gen_manypov2_JK_Named, gen_manypov2_B_Named, gen_manypov2_M_Named, gen_manypov2_N_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)