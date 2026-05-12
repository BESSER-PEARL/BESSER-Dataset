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
Korisnik_IS = Class(name="Korisnik_IS")
Putovanje = Class(name="Putovanje")
Aran_man = Class(name="Aran_man")
Sme_taj = Class(name="Sme_taj")
Osiguranje = Class(name="Osiguranje")
Kupac = Class(name="Kupac")

# Korisnik_IS class attributes and methods
Korisnik_IS_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Korisnik_IS_UserName: Property = Property(name="UserName", type=StringType)
Korisnik_IS_Password: Property = Property(name="Password", type=StringType)
Korisnik_IS_ImeKorisnika: Property = Property(name="ImeKorisnika", type=StringType)
Korisnik_IS_PrezimeKorisnika: Property = Property(name="PrezimeKorisnika", type=StringType)
Korisnik_IS.attributes={Korisnik_IS_PrezimeKorisnika, Korisnik_IS_Password, Korisnik_IS_KorisnikID, Korisnik_IS_ImeKorisnika, Korisnik_IS_UserName}

# Putovanje class attributes and methods
Putovanje_PutovID: Property = Property(name="PutovID", type=IntegerType)
Putovanje_Dr_ava: Property = Property(name="Dr_ava", type=StringType)
Putovanje_Grad: Property = Property(name="Grad", type=StringType)
Putovanje.attributes={Putovanje_Grad, Putovanje_PutovID, Putovanje_Dr_ava}

# Aran_man class attributes and methods
Aran_man_Aran_manID: Property = Property(name="Aran_manID", type=IntegerType)
Aran_man_SlobMesto: Property = Property(name="SlobMesto", type=BooleanType)
Aran_man_DatumPolaska: Property = Property(name="DatumPolaska", type=StringType)
Aran_man_DatumDolaska: Property = Property(name="DatumDolaska", type=StringType)
Aran_man_Cena: Property = Property(name="Cena", type=StringType)
Aran_man_PutovID: Property = Property(name="PutovID", type=IntegerType)
Aran_man_KupacID: Property = Property(name="KupacID", type=IntegerType)
Aran_man_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Aran_man.attributes={Aran_man_Aran_manID, Aran_man_Cena, Aran_man_PutovID, Aran_man_SlobMesto, Aran_man_KorisnikID, Aran_man_DatumPolaska, Aran_man_KupacID, Aran_man_DatumDolaska}

# Sme_taj class attributes and methods
Sme_taj_Sme_tajID: Property = Property(name="Sme_tajID", type=IntegerType)
Sme_taj_ImeSme_taja: Property = Property(name="ImeSme_taja", type=StringType)
Sme_taj_LokacijaSme_taja: Property = Property(name="LokacijaSme_taja", type=StringType)
Sme_taj_UslugaSme_taja: Property = Property(name="UslugaSme_taja", type=StringType)
Sme_taj_DuzinaBoravka: Property = Property(name="DuzinaBoravka", type=IntegerType)
Sme_taj_CenaSmestaja: Property = Property(name="CenaSmestaja", type=StringType)
Sme_taj_PutovID: Property = Property(name="PutovID", type=IntegerType)
Sme_taj.attributes={Sme_taj_CenaSmestaja, Sme_taj_PutovID, Sme_taj_LokacijaSme_taja, Sme_taj_ImeSme_taja, Sme_taj_Sme_tajID, Sme_taj_UslugaSme_taja, Sme_taj_DuzinaBoravka}

# Osiguranje class attributes and methods
Osiguranje_OsigID: Property = Property(name="OsigID", type=IntegerType)
Osiguranje_KucaOsiguranje: Property = Property(name="KucaOsiguranje", type=StringType)
Osiguranje_PaketPokri_a: Property = Property(name="PaketPokri_a", type=StringType)
Osiguranje.attributes={Osiguranje_PaketPokri_a, Osiguranje_OsigID, Osiguranje_KucaOsiguranje}

# Kupac class attributes and methods
Kupac_KupacID: Property = Property(name="KupacID", type=IntegerType)
Kupac_ImeKup: Property = Property(name="ImeKup", type=StringType)
Kupac_PrezimeKup: Property = Property(name="PrezimeKup", type=StringType)
Kupac_JMBG: Property = Property(name="JMBG", type=StringType)
Kupac_Grad: Property = Property(name="Grad", type=StringType)
Kupac_Adresa: Property = Property(name="Adresa", type=StringType)
Kupac_Mobilni: Property = Property(name="Mobilni", type=IntegerType)
Kupac_eMail: Property = Property(name="eMail", type=StringType)
Kupac_OsigID: Property = Property(name="OsigID", type=IntegerType)
Kupac.attributes={Kupac_eMail, Kupac_Mobilni, Kupac_JMBG, Kupac_ImeKup, Kupac_KupacID, Kupac_PrezimeKup, Kupac_Adresa, Kupac_OsigID, Kupac_Grad}

# Relationships
Destinacija_Hotel: BinaryAssociation = BinaryAssociation(
    name="Destinacija_Hotel",
    ends={
        Property(name="sme_taj0", type=Sme_taj, multiplicity=Multiplicity(0, 9999)),
        Property(name="putovanje1", type=Putovanje, multiplicity=Multiplicity(1, 1))
    }
)
Rezervisanje_Destinacija: BinaryAssociation = BinaryAssociation(
    name="Rezervisanje_Destinacija",
    ends={
        Property(name="putovanje2", type=Putovanje, multiplicity=Multiplicity(1, 1)),
        Property(name="aran_man3", type=Aran_man, multiplicity=Multiplicity(0, 9999))
    }
)
Osiguranje_Putnik: BinaryAssociation = BinaryAssociation(
    name="Osiguranje_Putnik",
    ends={
        Property(name="kupac4", type=Kupac, multiplicity=Multiplicity(0, 9999)),
        Property(name="osiguranje5", type=Osiguranje, multiplicity=Multiplicity(0, 1))
    }
)
Putnik_Rezervisanje: BinaryAssociation = BinaryAssociation(
    name="Putnik_Rezervisanje",
    ends={
        Property(name="aran_man6", type=Aran_man, multiplicity=Multiplicity(0, 9999)),
        Property(name="kupac7", type=Kupac, multiplicity=Multiplicity(1, 1))
    }
)
Rezervisanje_Korisnik_IS: BinaryAssociation = BinaryAssociation(
    name="Rezervisanje_Korisnik_IS",
    ends={
        Property(name="korisnik_IS8", type=Korisnik_IS, multiplicity=Multiplicity(1, 1)),
        Property(name="aran_man9", type=Aran_man, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a3a6fce7_8138_42f1_ac8e_3a127cfe601c",
    types={Korisnik_IS, Putovanje, Aran_man, Sme_taj, Osiguranje, Kupac},
    associations={Destinacija_Hotel, Rezervisanje_Destinacija, Osiguranje_Putnik, Putnik_Rezervisanje, Rezervisanje_Korisnik_IS},
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