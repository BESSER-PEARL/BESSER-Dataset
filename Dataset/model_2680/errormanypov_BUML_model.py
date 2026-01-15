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
errormanypov_A = Class(name="errormanypov::A")
Named = Class(name="Named")
errormanypov_C = Class(name="errormanypov::C")
errormanypov_B = Class(name="errormanypov::B")
errormanypov_E = Class(name="errormanypov::E")
errormanypov_J = Class(name="errormanypov::J")
errormanypov_F = Class(name="errormanypov::F")
errormanypov_JK = Class(name="errormanypov::JK")
errormanypov_Named = Class(name="errormanypov::Named")
errormanypov_K = Class(name="errormanypov::K")
errormanypov_M = Class(name="errormanypov::M")

# errormanypov_A class attributes and methods

# Named class attributes and methods

# errormanypov_C class attributes and methods

# errormanypov_B class attributes and methods

# errormanypov_E class attributes and methods

# errormanypov_J class attributes and methods

# errormanypov_F class attributes and methods

# errormanypov_JK class attributes and methods

# errormanypov_Named class attributes and methods
errormanypov_Named_name: Property = Property(name="name", type=StringType)
errormanypov_Named.attributes={errormanypov_Named_name}

# errormanypov_K class attributes and methods

# errormanypov_M class attributes and methods

# Relationships
js3: BinaryAssociation = BinaryAssociation(
    name="js3",
    ends={
        Property(name="errormanypov_J", type=errormanypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_A4", type=errormanypov_J, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs5: BinaryAssociation = BinaryAssociation(
    name="cs5",
    ends={
        Property(name="errormanypov_C", type=errormanypov_B, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_B6", type=errormanypov_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="errormanypov_B", type=errormanypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_A", type=errormanypov_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="errormanypov_E", type=errormanypov_A, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_A2", type=errormanypov_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs7: BinaryAssociation = BinaryAssociation(
    name="fs7",
    ends={
        Property(name="errormanypov_F", type=errormanypov_E, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_E8", type=errormanypov_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms11: BinaryAssociation = BinaryAssociation(
    name="ms11",
    ends={
        Property(name="errormanypov_K", type=errormanypov_M, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="errormanypov_M", type=errormanypov_K, multiplicity=Multiplicity(1, 1))
    }
)
cs12: BinaryAssociation = BinaryAssociation(
    name="cs12",
    ends={
        Property(name="errormanypov_C14", type=errormanypov_K, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_K13", type=errormanypov_C, multiplicity=Multiplicity(0, 1))
    }
)
ks15: BinaryAssociation = BinaryAssociation(
    name="ks15",
    ends={
        Property(name="errormanypov_K17", type=errormanypov_JK, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_JK16", type=errormanypov_K, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jks9: BinaryAssociation = BinaryAssociation(
    name="jks9",
    ends={
        Property(name="errormanypov_JK", type=errormanypov_J, multiplicity=Multiplicity(1, 1)),
        Property(name="errormanypov_J10", type=errormanypov_JK, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_errormanypov_A_Named = Generalization(general=Named, specific=errormanypov_A)
gen_errormanypov_B_Named = Generalization(general=Named, specific=errormanypov_B)
gen_errormanypov_C_Named = Generalization(general=Named, specific=errormanypov_C)
gen_errormanypov_F_Named = Generalization(general=Named, specific=errormanypov_F)
gen_errormanypov_J_Named = Generalization(general=Named, specific=errormanypov_J)
gen_errormanypov_E_Named = Generalization(general=Named, specific=errormanypov_E)
gen_errormanypov_JK_Named = Generalization(general=Named, specific=errormanypov_JK)
gen_errormanypov_K_Named = Generalization(general=Named, specific=errormanypov_K)
gen_errormanypov_M_Named = Generalization(general=Named, specific=errormanypov_M)

# Domain Model
domain_model = DomainModel(
    name="errormanypov",
    types={errormanypov_A, Named, errormanypov_C, errormanypov_B, errormanypov_E, errormanypov_J, errormanypov_F, errormanypov_JK, errormanypov_Named, errormanypov_K, errormanypov_M},
    associations={js3, cs5, bs0, es1, fs7, ms11, cs12, ks15, jks9},
    generalizations={gen_errormanypov_A_Named, gen_errormanypov_B_Named, gen_errormanypov_C_Named, gen_errormanypov_F_Named, gen_errormanypov_J_Named, gen_errormanypov_E_Named, gen_errormanypov_JK_Named, gen_errormanypov_K_Named, gen_errormanypov_M_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)