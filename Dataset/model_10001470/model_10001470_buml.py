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
Rezervacija = Class(name="Rezervacija")
Agent = Class(name="Agent")
Aranzman = Class(name="Aranzman")
Osiguranje = Class(name="Osiguranje")
Termin = Class(name="Termin")
Racun = Class(name="Racun")
Date = Class(name="Date")
Double = Class(name="Double")
Destinacija = Class(name="Destinacija")
string = Class(name="string")
Putnik = Class(name="Putnik")

# Rezervacija class attributes and methods
Rezervacija_ReyervacijaID: Property = Property(name="ReyervacijaID", type=IntegerType)
Rezervacija_DatumKreiranja: Property = Property(name="DatumKreiranja", type=Date)
Rezervacija_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Rezervacija_AgentID: Property = Property(name="AgentID", type=IntegerType)
Rezervacija_AranzmanID: Property = Property(name="AranzmanID", type=IntegerType)
Rezervacija_RacunID: Property = Property(name="RacunID", type=IntegerType)
Rezervacija.attributes={Rezervacija_AgentID, Rezervacija_ReyervacijaID, Rezervacija_DatumKreiranja, Rezervacija_AranzmanID, Rezervacija_RacunID, Rezervacija_PutnikID}

# Agent class attributes and methods
Agent_AgentID: Property = Property(name="AgentID", type=IntegerType)
Agent_ImeAgent: Property = Property(name="ImeAgent", type=StringType)
Agent_PrezimeAgent: Property = Property(name="PrezimeAgent", type=StringType)
Agent_Email: Property = Property(name="Email", type=StringType)
Agent_BrojTele: Property = Property(name="BrojTele", type=StringType)
Agent_Username: Property = Property(name="Username", type=StringType)
Agent_Password: Property = Property(name="Password", type=StringType)
Agent.attributes={Agent_BrojTele, Agent_ImeAgent, Agent_Password, Agent_Email, Agent_AgentID, Agent_PrezimeAgent, Agent_Username}

# Aranzman class attributes and methods
Aranzman_AranzmanID: Property = Property(name="AranzmanID", type=IntegerType)
Aranzman_NazivAranzmana: Property = Property(name="NazivAranzmana", type=StringType)
Aranzman_BrojMesta: Property = Property(name="BrojMesta", type=IntegerType)
Aranzman_Popunjeno: Property = Property(name="Popunjeno", type=BooleanType)
Aranzman_Cena: Property = Property(name="Cena", type=Double)
Aranzman_DestinacijaID: Property = Property(name="DestinacijaID", type=IntegerType)
Aranzman_TerminID: Property = Property(name="TerminID", type=IntegerType)
Aranzman.attributes={Aranzman_Popunjeno, Aranzman_DestinacijaID, Aranzman_Cena, Aranzman_AranzmanID, Aranzman_TerminID, Aranzman_BrojMesta, Aranzman_NazivAranzmana}

# Osiguranje class attributes and methods
Osiguranje_OsiguranjeID: Property = Property(name="OsiguranjeID", type=IntegerType)
Osiguranje_OsigurKuca: Property = Property(name="OsigurKuca", type=StringType)
Osiguranje.attributes={Osiguranje_OsigurKuca, Osiguranje_OsiguranjeID}

# Termin class attributes and methods
Termin_TerminID: Property = Property(name="TerminID", type=IntegerType)
Termin_DatumPolaska: Property = Property(name="DatumPolaska", type=Date)
Termin_DatumPovratka: Property = Property(name="DatumPovratka", type=Date)
Termin.attributes={Termin_DatumPolaska, Termin_TerminID, Termin_DatumPovratka}

# Racun class attributes and methods
Racun_RacunID: Property = Property(name="RacunID", type=IntegerType)
Racun_Placeno: Property = Property(name="Placeno", type=BooleanType)
Racun_Iznos: Property = Property(name="Iznos", type=Double)
Racun.attributes={Racun_Iznos, Racun_RacunID, Racun_Placeno}

# Date class attributes and methods

# Double class attributes and methods

# Destinacija class attributes and methods
Destinacija_DestinacijaID: Property = Property(name="DestinacijaID", type=IntegerType)
Destinacija_Drzava: Property = Property(name="Drzava", type=StringType)
Destinacija_Grad: Property = Property(name="Grad", type=StringType)
Destinacija_Hotel: Property = Property(name="Hotel", type=StringType)
Destinacija.attributes={Destinacija_Grad, Destinacija_DestinacijaID, Destinacija_Drzava, Destinacija_Hotel}

# string class attributes and methods

# Putnik class attributes and methods
Putnik_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Putnik_ImePutnik: Property = Property(name="ImePutnik", type=StringType)
Putnik_PrezimePutnik: Property = Property(name="PrezimePutnik", type=StringType)
Putnik_JMBG: Property = Property(name="JMBG", type=StringType)
Putnik_Adresa: Property = Property(name="Adresa", type=StringType)
Putnik_Grad: Property = Property(name="Grad", type=StringType)
Putnik_Email: Property = Property(name="Email", type=StringType)
Putnik_BrojTel: Property = Property(name="BrojTel", type=StringType)
Putnik_OsiguranjeID: Property = Property(name="OsiguranjeID", type=IntegerType)
Putnik.attributes={Putnik_Email, Putnik_Adresa, Putnik_OsiguranjeID, Putnik_PrezimePutnik, Putnik_BrojTel, Putnik_ImePutnik, Putnik_PutnikID, Putnik_JMBG, Putnik_Grad}

# Relationships
Osiguranje_Putnik: BinaryAssociation = BinaryAssociation(
    name="Osiguranje_Putnik",
    ends={
        Property(name="putnik0", type=Putnik, multiplicity=Multiplicity(0, 1)),
        Property(name="osiguranje1", type=Osiguranje, multiplicity=Multiplicity(0, 1))
    }
)
Putnik_Rezervacija: BinaryAssociation = BinaryAssociation(
    name="Putnik_Rezervacija",
    ends={
        Property(name="rezervacija2", type=Rezervacija, multiplicity=Multiplicity(0, 1)),
        Property(name="putnik3", type=Putnik, multiplicity=Multiplicity(0, 1))
    }
)
Rezervacija_Agent: BinaryAssociation = BinaryAssociation(
    name="Rezervacija_Agent",
    ends={
        Property(name="agent4", type=Agent, multiplicity=Multiplicity(0, 1)),
        Property(name="rezervacija5", type=Rezervacija, multiplicity=Multiplicity(0, 1))
    }
)
Aranzman_Rezervacija: BinaryAssociation = BinaryAssociation(
    name="Aranzman_Rezervacija",
    ends={
        Property(name="rezervacija6", type=Rezervacija, multiplicity=Multiplicity(0, 1)),
        Property(name="aranzman7", type=Aranzman, multiplicity=Multiplicity(0, 1))
    }
)
Aranzman_Destinacija: BinaryAssociation = BinaryAssociation(
    name="Aranzman_Destinacija",
    ends={
        Property(name="destinacija8", type=Destinacija, multiplicity=Multiplicity(0, 1)),
        Property(name="aranzman9", type=Aranzman, multiplicity=Multiplicity(0, 1))
    }
)
Termin_Aranzman: BinaryAssociation = BinaryAssociation(
    name="Termin_Aranzman",
    ends={
        Property(name="aranzman10", type=Aranzman, multiplicity=Multiplicity(0, 1)),
        Property(name="termin11", type=Termin, multiplicity=Multiplicity(0, 1))
    }
)
Racun_Rezervacija: BinaryAssociation = BinaryAssociation(
    name="Racun_Rezervacija",
    ends={
        Property(name="rezervacija12", type=Rezervacija, multiplicity=Multiplicity(0, 1)),
        Property(name="racun13", type=Racun, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8sMJYGPsEeio56zSTH7puw",
    types={Rezervacija, Agent, Aranzman, Osiguranje, Termin, Racun, Date, Double, Destinacija, string, Putnik},
    associations={Osiguranje_Putnik, Putnik_Rezervacija, Rezervacija_Agent, Aranzman_Rezervacija, Aranzman_Destinacija, Termin_Aranzman, Racun_Rezervacija},
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