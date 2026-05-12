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
K_ytt_j__Actor = Class(name="K_ytt_j__Actor")
Korvauksen_Hakeminen_UseCase = Class(name="Korvauksen_Hakeminen_UseCase")
Kirjautuminen_UseCase = Class(name="Kirjautuminen_UseCase")
Vakuutusselvitys_UseCase = Class(name="Vakuutusselvitys_UseCase")
Vakuutusyhti__Actor = Class(name="Vakuutusyhti__Actor")
Hakemuksen_k_sittely_UseCase = Class(name="Hakemuksen_k_sittely_UseCase")
Korvauksen_maksaminen_UseCase = Class(name="Korvauksen_maksaminen_UseCase")
Asiakas = Class(name="Asiakas")
Vakuutus = Class(name="Vakuutus")
Vakuutusyhti_ = Class(name="Vakuutusyhti_")
Ker_t__n_tiedot_UseCase = Class(name="Ker_t__n_tiedot_UseCase")

# K_ytt_j__Actor class attributes and methods

# Korvauksen_Hakeminen_UseCase class attributes and methods

# Kirjautuminen_UseCase class attributes and methods

# Vakuutusselvitys_UseCase class attributes and methods

# Vakuutusyhti__Actor class attributes and methods

# Hakemuksen_k_sittely_UseCase class attributes and methods

# Korvauksen_maksaminen_UseCase class attributes and methods

# Asiakas class attributes and methods
Asiakas_Asiakas__id_: Property = Property(name="Asiakas__id_", type=IntegerType)
Asiakas.attributes={Asiakas_Asiakas__id_}

# Vakuutus class attributes and methods

# Vakuutusyhti_ class attributes and methods

# Ker_t__n_tiedot_UseCase class attributes and methods

# Relationships
K_ytt_j__Korvauksen_Hakeminen: BinaryAssociation = BinaryAssociation(
    name="K_ytt_j__Korvauksen_Hakeminen",
    ends={
        Property(name="korvauksen_Hakeminen0", type=Korvauksen_Hakeminen_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="k_ytt_j_1", type=K_ytt_j__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Korvauksen_Hakeminen_Vakuutusyhti_: BinaryAssociation = BinaryAssociation(
    name="Korvauksen_Hakeminen_Vakuutusyhti_",
    ends={
        Property(name="vakuutusyhti_2", type=Vakuutusyhti__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="korvauksen_Hakeminen3", type=Korvauksen_Hakeminen_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Hakemuksen_k_sittely_Vakuutusyhti_: BinaryAssociation = BinaryAssociation(
    name="Hakemuksen_k_sittely_Vakuutusyhti_",
    ends={
        Property(name="vakuutusyhti_4", type=Vakuutusyhti__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="hakemuksen_k_sittely5", type=Hakemuksen_k_sittely_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Korvauksen_maksaminen_Vakuutusyhti_: BinaryAssociation = BinaryAssociation(
    name="Korvauksen_maksaminen_Vakuutusyhti_",
    ends={
        Property(name="vakuutusyhti_6", type=Vakuutusyhti__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="korvauksen_maksaminen7", type=Korvauksen_maksaminen_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Korvauksen_maksaminen_K_ytt_j_: BinaryAssociation = BinaryAssociation(
    name="Korvauksen_maksaminen_K_ytt_j_",
    ends={
        Property(name="k_ytt_j_8", type=K_ytt_j__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="korvauksen_maksaminen9", type=Korvauksen_maksaminen_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Vakuutusyhti__Ker_t__n_tiedot: BinaryAssociation = BinaryAssociation(
    name="Vakuutusyhti__Ker_t__n_tiedot",
    ends={
        Property(name="ker_t__n_tiedot10", type=Ker_t__n_tiedot_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="vakuutusyhti_11", type=Vakuutusyhti__Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_21YW8Kp0EeeEQN1ZyOr__g",
    types={K_ytt_j__Actor, Korvauksen_Hakeminen_UseCase, Kirjautuminen_UseCase, Vakuutusselvitys_UseCase, Vakuutusyhti__Actor, Hakemuksen_k_sittely_UseCase, Korvauksen_maksaminen_UseCase, Asiakas, Vakuutus, Vakuutusyhti_, Ker_t__n_tiedot_UseCase},
    associations={K_ytt_j__Korvauksen_Hakeminen, Korvauksen_Hakeminen_Vakuutusyhti_, Hakemuksen_k_sittely_Vakuutusyhti_, Korvauksen_maksaminen_Vakuutusyhti_, Korvauksen_maksaminen_K_ytt_j_, Vakuutusyhti__Ker_t__n_tiedot},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)