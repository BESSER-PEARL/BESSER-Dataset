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
Karta = Class(name="Karta")
Destinacija = Class(name="Destinacija")
Rezervisanje = Class(name="Rezervisanje")
Korisnik_IS = Class(name="Korisnik_IS")
Hotel = Class(name="Hotel")
Osiguranje = Class(name="Osiguranje")
Putnik = Class(name="Putnik")

# Karta class attributes and methods
Karta_KartaID: Property = Property(name="KartaID", type=IntegerType)
Karta_OdlazakKarta: Property = Property(name="OdlazakKarta", type=StringType)
Karta_VremeOdlaska: Property = Property(name="VremeOdlaska", type=StringType)
Karta_PovratakKarta: Property = Property(name="PovratakKarta", type=StringType)
Karta_VremePovratka: Property = Property(name="VremePovratka", type=StringType)
Karta_CenaKarte: Property = Property(name="CenaKarte", type=StringType)
Karta_RezerID: Property = Property(name="RezerID", type=IntegerType)
Karta.attributes={Karta_OdlazakKarta, Karta_CenaKarte, Karta_PovratakKarta, Karta_VremeOdlaska, Karta_RezerID, Karta_KartaID, Karta_VremePovratka}

# Destinacija class attributes and methods
Destinacija_DestiID: Property = Property(name="DestiID", type=IntegerType)
Destinacija_DesDrzava: Property = Property(name="DesDrzava", type=StringType)
Destinacija_DesGrad: Property = Property(name="DesGrad", type=StringType)
Destinacija.attributes={Destinacija_DestiID, Destinacija_DesGrad, Destinacija_DesDrzava}

# Rezervisanje class attributes and methods
Rezervisanje_DatumPolaska: Property = Property(name="DatumPolaska", type=StringType)
Rezervisanje_DatumDolaska: Property = Property(name="DatumDolaska", type=StringType)
Rezervisanje_Cena: Property = Property(name="Cena", type=StringType)
Rezervisanje_DestiID: Property = Property(name="DestiID", type=IntegerType)
Rezervisanje_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Rezervisanje_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Rezervisanje_RezerID: Property = Property(name="RezerID", type=IntegerType)
Rezervisanje_SlobMesto: Property = Property(name="SlobMesto", type=BooleanType)
Rezervisanje.attributes={Rezervisanje_Cena, Rezervisanje_PutnikID, Rezervisanje_DatumPolaska, Rezervisanje_DestiID, Rezervisanje_SlobMesto, Rezervisanje_KorisnikID, Rezervisanje_DatumDolaska, Rezervisanje_RezerID}

# Korisnik_IS class attributes and methods
Korisnik_IS_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Korisnik_IS_UserName: Property = Property(name="UserName", type=StringType)
Korisnik_IS_Password: Property = Property(name="Password", type=StringType)
Korisnik_IS_ImeKorisnika: Property = Property(name="ImeKorisnika", type=StringType)
Korisnik_IS_PrezimeKorisnika: Property = Property(name="PrezimeKorisnika", type=StringType)
Korisnik_IS.attributes={Korisnik_IS_ImeKorisnika, Korisnik_IS_KorisnikID, Korisnik_IS_UserName, Korisnik_IS_PrezimeKorisnika, Korisnik_IS_Password}

# Hotel class attributes and methods
Hotel_HotelID: Property = Property(name="HotelID", type=IntegerType)
Hotel_ImeHotela: Property = Property(name="ImeHotela", type=StringType)
Hotel_AdresaHotela: Property = Property(name="AdresaHotela", type=StringType)
Hotel_SpratHotela: Property = Property(name="SpratHotela", type=IntegerType)
Hotel_SobaHotela: Property = Property(name="SobaHotela", type=IntegerType)
Hotel_UslugaHotela: Property = Property(name="UslugaHotela", type=StringType)
Hotel_DuzinaBoravka: Property = Property(name="DuzinaBoravka", type=IntegerType)
Hotel_CenaSmestaja: Property = Property(name="CenaSmestaja", type=StringType)
Hotel_DestiID: Property = Property(name="DestiID", type=IntegerType)
Hotel.attributes={Hotel_UslugaHotela, Hotel_DuzinaBoravka, Hotel_SpratHotela, Hotel_ImeHotela, Hotel_HotelID, Hotel_AdresaHotela, Hotel_SobaHotela, Hotel_CenaSmestaja, Hotel_DestiID}

# Osiguranje class attributes and methods
Osiguranje_OsigID: Property = Property(name="OsigID", type=IntegerType)
Osiguranje_KucaOsiguranje: Property = Property(name="KucaOsiguranje", type=StringType)
Osiguranje.attributes={Osiguranje_KucaOsiguranje, Osiguranje_OsigID}

# Putnik class attributes and methods
Putnik_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Putnik_ImePut: Property = Property(name="ImePut", type=StringType)
Putnik_PrezimePut: Property = Property(name="PrezimePut", type=StringType)
Putnik_JMBG: Property = Property(name="JMBG", type=StringType)
Putnik_Grad: Property = Property(name="Grad", type=StringType)
Putnik_Adresa: Property = Property(name="Adresa", type=StringType)
Putnik_Mobilni: Property = Property(name="Mobilni", type=IntegerType)
Putnik_eMail: Property = Property(name="eMail", type=StringType)
Putnik_OsigID: Property = Property(name="OsigID", type=IntegerType)
Putnik.attributes={Putnik_PrezimePut, Putnik_eMail, Putnik_OsigID, Putnik_Mobilni, Putnik_ImePut, Putnik_PutnikID, Putnik_JMBG, Putnik_Adresa, Putnik_Grad}

# Relationships
Destinacija_Hotel: BinaryAssociation = BinaryAssociation(
    name="Destinacija_Hotel",
    ends={
        Property(name="hotel0", type=Hotel, multiplicity=Multiplicity(0, 9999)),
        Property(name="destinacija1", type=Destinacija, multiplicity=Multiplicity(1, 1))
    }
)
Rezervisanje_Destinacija: BinaryAssociation = BinaryAssociation(
    name="Rezervisanje_Destinacija",
    ends={
        Property(name="destinacija2", type=Destinacija, multiplicity=Multiplicity(1, 1)),
        Property(name="rezervisanje3", type=Rezervisanje, multiplicity=Multiplicity(0, 9999))
    }
)
Osiguranje_Putnik: BinaryAssociation = BinaryAssociation(
    name="Osiguranje_Putnik",
    ends={
        Property(name="putnik4", type=Putnik, multiplicity=Multiplicity(0, 9999)),
        Property(name="osiguranje5", type=Osiguranje, multiplicity=Multiplicity(0, 1))
    }
)
Putnik_Rezervisanje: BinaryAssociation = BinaryAssociation(
    name="Putnik_Rezervisanje",
    ends={
        Property(name="rezervisanje6", type=Rezervisanje, multiplicity=Multiplicity(0, 9999)),
        Property(name="putnik7", type=Putnik, multiplicity=Multiplicity(1, 1))
    }
)
Rezervisanje_Korisnik_IS: BinaryAssociation = BinaryAssociation(
    name="Rezervisanje_Korisnik_IS",
    ends={
        Property(name="korisnik_IS8", type=Korisnik_IS, multiplicity=Multiplicity(1, 1)),
        Property(name="rezervisanje9", type=Rezervisanje, multiplicity=Multiplicity(0, 9999))
    }
)
Karta_Rezervisanje: BinaryAssociation = BinaryAssociation(
    name="Karta_Rezervisanje",
    ends={
        Property(name="rezervisanje10", type=Rezervisanje, multiplicity=Multiplicity(1, 1)),
        Property(name="karta11", type=Karta, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0cbbd167_8221_4af0_920c_3e40d70effb7",
    types={Karta, Destinacija, Rezervisanje, Korisnik_IS, Hotel, Osiguranje, Putnik},
    associations={Destinacija_Hotel, Rezervisanje_Destinacija, Osiguranje_Putnik, Putnik_Rezervisanje, Rezervisanje_Korisnik_IS, Karta_Rezervisanje},
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