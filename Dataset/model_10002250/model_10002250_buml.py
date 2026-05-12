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
Lekar = Class(name="Lekar")
Pregled = Class(name="Pregled")
Zdravstveni_karton = Class(name="Zdravstveni_karton")

# Lekar class attributes and methods
Lekar_Zaposleni_ID: Property = Property(name="Zaposleni_ID", type=StringType)
Lekar_ImeZap: Property = Property(name="ImeZap", type=StringType)
Lekar_PrzZap: Property = Property(name="PrzZap", type=StringType)
Lekar_AdrZap: Property = Property(name="AdrZap", type=StringType)
Lekar_BrTelZap: Property = Property(name="BrTelZap", type=StringType)
Lekar_Fakultet: Property = Property(name="Fakultet", type=StringType)
Lekar_DatZavSk: Property = Property(name="DatZavSk", type=StringType)
Lekar_RadStaz: Property = Property(name="RadStaz", type=IntegerType)
Lekar.attributes={Lekar_Zaposleni_ID, Lekar_BrTelZap, Lekar_Fakultet, Lekar_PrzZap, Lekar_RadStaz, Lekar_AdrZap, Lekar_DatZavSk, Lekar_ImeZap}

# Pregled class attributes and methods
Pregled_BrPregled: Property = Property(name="BrPregled", type=IntegerType)
Pregled_DatumP: Property = Property(name="DatumP", type=StringType)
Pregled.attributes={Pregled_DatumP, Pregled_BrPregled}

# Zdravstveni_karton class attributes and methods
Zdravstveni_karton_BrKart: Property = Property(name="BrKart", type=IntegerType)
Zdravstveni_karton.attributes={Zdravstveni_karton_BrKart}

# Relationships
Vrsi_P: BinaryAssociation = BinaryAssociation(
    name="Vrsi_P",
    ends={
        Property(name="pregled0", type=Pregled, multiplicity=Multiplicity(1, 1)),
        Property(name="lekar1", type=Lekar, multiplicity=Multiplicity(0, 9999))
    }
)
Zdravstveni_karton_Pregled: BinaryAssociation = BinaryAssociation(
    name="Zdravstveni_karton_Pregled",
    ends={
        Property(name="pregled2", type=Pregled, multiplicity=Multiplicity(0, 1)),
        Property(name="zdravstveni_karton3", type=Zdravstveni_karton, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_zRSRMDEsEemjcq_iJCnVjQ",
    types={Lekar, Pregled, Zdravstveni_karton},
    associations={Vrsi_P, Zdravstveni_karton_Pregled},
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