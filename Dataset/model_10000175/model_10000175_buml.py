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
Agent = Class(name="Agent")
Aran_man = Class(name="Aran_man")
Osiguranje = Class(name="Osiguranje")
Kupac = Class(name="Kupac")
Transakcija = Class(name="Transakcija")

# Agent class attributes and methods
Agent_Agent_ID: Property = Property(name="Agent_ID", type=StringType)
Agent_Ime: Property = Property(name="Ime", type=StringType)
Agent_Prezime: Property = Property(name="Prezime", type=StringType)
Agent_BrojAgenta: Property = Property(name="BrojAgenta", type=IntegerType)
Agent_JMBG: Property = Property(name="JMBG", type=IntegerType)
Agent.attributes={Agent_BrojAgenta, Agent_Agent_ID, Agent_Ime, Agent_Prezime, Agent_JMBG}

# Aran_man class attributes and methods
Aran_man_Aranzman_ID: Property = Property(name="Aranzman_ID", type=StringType)
Aran_man_NazivAran_: Property = Property(name="NazivAran_", type=StringType)
Aran_man_SlobMesto: Property = Property(name="SlobMesto", type=BooleanType)
Aran_man_DatumPolaska: Property = Property(name="DatumPolaska", type=StringType)
Aran_man_DatumPovratka: Property = Property(name="DatumPovratka", type=StringType)
Aran_man_Cena: Property = Property(name="Cena", type=StringType)
Aran_man.attributes={Aran_man_NazivAran_, Aran_man_SlobMesto, Aran_man_Cena, Aran_man_DatumPolaska, Aran_man_DatumPovratka, Aran_man_Aranzman_ID}

# Osiguranje class attributes and methods
Osiguranje_Osiguranje_ID: Property = Property(name="Osiguranje_ID", type=StringType)
Osiguranje_OsigKuca: Property = Property(name="OsigKuca", type=StringType)
Osiguranje_PaketPokri_a: Property = Property(name="PaketPokri_a", type=StringType)
Osiguranje_BrojPolise: Property = Property(name="BrojPolise", type=IntegerType)
Osiguranje_Cena: Property = Property(name="Cena", type=StringType)
Osiguranje.attributes={Osiguranje_PaketPokri_a, Osiguranje_Osiguranje_ID, Osiguranje_OsigKuca, Osiguranje_BrojPolise, Osiguranje_Cena}

# Kupac class attributes and methods
Kupac_Kupac_ID: Property = Property(name="Kupac_ID", type=StringType)
Kupac_Ime: Property = Property(name="Ime", type=StringType)
Kupac_Prezime: Property = Property(name="Prezime", type=StringType)
Kupac_JMBG: Property = Property(name="JMBG", type=IntegerType)
Kupac_BrojPasosa: Property = Property(name="BrojPasosa", type=IntegerType)
Kupac_Mobilni: Property = Property(name="Mobilni", type=IntegerType)
Kupac_Grad: Property = Property(name="Grad", type=StringType)
Kupac.attributes={Kupac_Prezime, Kupac_JMBG, Kupac_BrojPasosa, Kupac_Mobilni, Kupac_Ime, Kupac_Kupac_ID, Kupac_Grad}

# Transakcija class attributes and methods
Transakcija_Trans_ID: Property = Property(name="Trans_ID", type=StringType)
Transakcija_datum_trans: Property = Property(name="datum_trans", type=StringType)
Transakcija_tip: Property = Property(name="tip", type=StringType)
Transakcija_suma: Property = Property(name="suma", type=StringType)
Transakcija.attributes={Transakcija_suma, Transakcija_tip, Transakcija_datum_trans, Transakcija_Trans_ID}

# Relationships
Osiguranje_Putnik: BinaryAssociation = BinaryAssociation(
    name="Osiguranje_Putnik",
    ends={
        Property(name="Osiguranje_Putnik_00", type=Kupac, multiplicity=Multiplicity(0, 9999)),
        Property(name="Osiguranje_Putnik_11", type=Osiguranje, multiplicity=Multiplicity(0, 1))
    }
)
Putnik_Rezervisanje: BinaryAssociation = BinaryAssociation(
    name="Putnik_Rezervisanje",
    ends={
        Property(name="Putnik_Rezervisanje_02", type=Aran_man, multiplicity=Multiplicity(0, 9999)),
        Property(name="Putnik_Rezervisanje_13", type=Kupac, multiplicity=Multiplicity(1, 1))
    }
)
Transakcija_Kupac: BinaryAssociation = BinaryAssociation(
    name="Transakcija_Kupac",
    ends={
        Property(name="Transakcija_Kupac_04", type=Kupac, multiplicity=Multiplicity(0, 9999)),
        Property(name="Transakcija_Kupac_15", type=Transakcija, multiplicity=Multiplicity(1, 9999))
    }
)
Agent_Kupac: BinaryAssociation = BinaryAssociation(
    name="Agent_Kupac",
    ends={
        Property(name="Agent_Kupac_06", type=Kupac, multiplicity=Multiplicity(0, 9999)),
        Property(name="Agent_Kupac_17", type=Agent, multiplicity=Multiplicity(1, 1))
    }
)
Agent_Aran_man: BinaryAssociation = BinaryAssociation(
    name="Agent_Aran_man",
    ends={
        Property(name="Agent_Aran_man_08", type=Aran_man, multiplicity=Multiplicity(0, 9999)),
        Property(name="Agent_Aran_man_19", type=Agent, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_15ec6afd_0f1e_45d4_8fb0_77dec37ee67a",
    types={Agent, Aran_man, Osiguranje, Kupac, Transakcija},
    associations={Osiguranje_Putnik, Putnik_Rezervisanje, Transakcija_Kupac, Agent_Kupac, Agent_Aran_man},
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