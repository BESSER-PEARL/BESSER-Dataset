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
Putnik = Class(name="Putnik")
Korisnik = Class(name="Korisnik")
Uplata = Class(name="Uplata")
Aranzman = Class(name="Aranzman")
Vodic = Class(name="Vodic")
Hotel = Class(name="Hotel")
Grad = Class(name="Grad")
Drzava = Class(name="Drzava")

# Putnik class attributes and methods
Putnik_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Putnik_BrojPasosa: Property = Property(name="BrojPasosa", type=IntegerType)
Putnik_ImePutnika: Property = Property(name="ImePutnika", type=StringType)
Putnik_PrezimePutnika: Property = Property(name="PrezimePutnika", type=StringType)
Putnik_JMBG: Property = Property(name="JMBG", type=StringType)
Putnik_AdresaPutnika: Property = Property(name="AdresaPutnika", type=StringType)
Putnik_GradPutnika: Property = Property(name="GradPutnika", type=StringType)
Putnik_KontaktPutnika: Property = Property(name="KontaktPutnika", type=StringType)
Putnik_AranzmanID: Property = Property(name="AranzmanID", type=IntegerType)
Putnik.attributes={Putnik_PrezimePutnika, Putnik_PutnikID, Putnik_BrojPasosa, Putnik_JMBG, Putnik_ImePutnika, Putnik_GradPutnika, Putnik_AranzmanID, Putnik_AdresaPutnika, Putnik_KontaktPutnika}

# Korisnik class attributes and methods
Korisnik_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Korisnik_ImeKorisnika: Property = Property(name="ImeKorisnika", type=StringType)
Korisnik_PrezimeKorisnika: Property = Property(name="PrezimeKorisnika", type=StringType)
Korisnik_JMBG: Property = Property(name="JMBG", type=StringType)
Korisnik_AdresaKorisnika: Property = Property(name="AdresaKorisnika", type=StringType)
Korisnik_GradKorisnika: Property = Property(name="GradKorisnika", type=StringType)
Korisnik_KontaktKorisnika: Property = Property(name="KontaktKorisnika", type=StringType)
Korisnik_Username: Property = Property(name="Username", type=StringType)
Korisnik_Password: Property = Property(name="Password", type=StringType)
Korisnik.attributes={Korisnik_Username, Korisnik_KontaktKorisnika, Korisnik_KorisnikID, Korisnik_JMBG, Korisnik_AdresaKorisnika, Korisnik_GradKorisnika, Korisnik_Password, Korisnik_ImeKorisnika, Korisnik_PrezimeKorisnika}

# Uplata class attributes and methods
Uplata_UplataID: Property = Property(name="UplataID", type=IntegerType)
Uplata_NazivUplate: Property = Property(name="NazivUplate", type=StringType)
Uplata_DatumUplate: Property = Property(name="DatumUplate", type=StringType)
Uplata_Iznos: Property = Property(name="Iznos", type=StringType)
Uplata_PutnikID: Property = Property(name="PutnikID", type=IntegerType)
Uplata.attributes={Uplata_DatumUplate, Uplata_PutnikID, Uplata_NazivUplate, Uplata_UplataID, Uplata_Iznos}

# Aranzman class attributes and methods
Aranzman_AranzmanID: Property = Property(name="AranzmanID", type=IntegerType)
Aranzman_NazivAranzmana: Property = Property(name="NazivAranzmana", type=StringType)
Aranzman_DatumAranzmana: Property = Property(name="DatumAranzmana", type=StringType)
Aranzman_CenaAranzmana: Property = Property(name="CenaAranzmana", type=StringType)
Aranzman_OpisAranzmana: Property = Property(name="OpisAranzmana", type=StringType)
Aranzman_HotelID: Property = Property(name="HotelID", type=IntegerType)
Aranzman_VodicID: Property = Property(name="VodicID", type=IntegerType)
Aranzman_KorisnikID: Property = Property(name="KorisnikID", type=IntegerType)
Aranzman.attributes={Aranzman_NazivAranzmana, Aranzman_VodicID, Aranzman_CenaAranzmana, Aranzman_AranzmanID, Aranzman_OpisAranzmana, Aranzman_HotelID, Aranzman_KorisnikID, Aranzman_DatumAranzmana}

# Vodic class attributes and methods
Vodic_VodicID: Property = Property(name="VodicID", type=IntegerType)
Vodic_ImeVodica: Property = Property(name="ImeVodica", type=StringType)
Vodic_PrezimeVodica: Property = Property(name="PrezimeVodica", type=StringType)
Vodic_JMBG: Property = Property(name="JMBG", type=StringType)
Vodic_AdresaVodica: Property = Property(name="AdresaVodica", type=StringType)
Vodic_GradVodica: Property = Property(name="GradVodica", type=StringType)
Vodic_KontaktVodica: Property = Property(name="KontaktVodica", type=StringType)
Vodic.attributes={Vodic_GradVodica, Vodic_KontaktVodica, Vodic_AdresaVodica, Vodic_ImeVodica, Vodic_VodicID, Vodic_PrezimeVodica, Vodic_JMBG}

# Hotel class attributes and methods
Hotel_HotelID: Property = Property(name="HotelID", type=IntegerType)
Hotel_NazivHotela: Property = Property(name="NazivHotela", type=StringType)
Hotel_KontaktHotela: Property = Property(name="KontaktHotela", type=StringType)
Hotel_AdresaHotela: Property = Property(name="AdresaHotela", type=StringType)
Hotel_GradID: Property = Property(name="GradID", type=IntegerType)
Hotel.attributes={Hotel_AdresaHotela, Hotel_GradID, Hotel_NazivHotela, Hotel_HotelID, Hotel_KontaktHotela}

# Grad class attributes and methods
Grad_GradID: Property = Property(name="GradID", type=IntegerType)
Grad_NazivGrada: Property = Property(name="NazivGrada", type=StringType)
Grad_DrzavaID: Property = Property(name="DrzavaID", type=IntegerType)
Grad.attributes={Grad_GradID, Grad_NazivGrada, Grad_DrzavaID}

# Drzava class attributes and methods
Drzava_DrzavaID: Property = Property(name="DrzavaID", type=IntegerType)
Drzava_NazivDrzave: Property = Property(name="NazivDrzave", type=StringType)
Drzava.attributes={Drzava_NazivDrzave, Drzava_DrzavaID}

# Relationships
Vodic_Aranzman: BinaryAssociation = BinaryAssociation(
    name="Vodic_Aranzman",
    ends={
        Property(name="aranzman0", type=Aranzman, multiplicity=Multiplicity(0, 9999)),
        Property(name="vodic1", type=Vodic, multiplicity=Multiplicity(1, 1))
    }
)
Drzava_Grad: BinaryAssociation = BinaryAssociation(
    name="Drzava_Grad",
    ends={
        Property(name="grad2", type=Grad, multiplicity=Multiplicity(1, 9999)),
        Property(name="drzava3", type=Drzava, multiplicity=Multiplicity(1, 1))
    }
)
Grad_Hotel: BinaryAssociation = BinaryAssociation(
    name="Grad_Hotel",
    ends={
        Property(name="hotel4", type=Hotel, multiplicity=Multiplicity(0, 9999)),
        Property(name="grad5", type=Grad, multiplicity=Multiplicity(1, 1))
    }
)
Korisnik_Aranzman: BinaryAssociation = BinaryAssociation(
    name="Korisnik_Aranzman",
    ends={
        Property(name="aranzman6", type=Aranzman, multiplicity=Multiplicity(0, 9999)),
        Property(name="korisnik7", type=Korisnik, multiplicity=Multiplicity(1, 1))
    }
)
Aranzman_Hotel: BinaryAssociation = BinaryAssociation(
    name="Aranzman_Hotel",
    ends={
        Property(name="hotel8", type=Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="aranzman9", type=Aranzman, multiplicity=Multiplicity(0, 9999))
    }
)
Putnik_Aranzman: BinaryAssociation = BinaryAssociation(
    name="Putnik_Aranzman",
    ends={
        Property(name="aranzman10", type=Aranzman, multiplicity=Multiplicity(1, 1)),
        Property(name="putnik11", type=Putnik, multiplicity=Multiplicity(0, 9999))
    }
)
Uplata_Putnik: BinaryAssociation = BinaryAssociation(
    name="Uplata_Putnik",
    ends={
        Property(name="putnik12", type=Putnik, multiplicity=Multiplicity(1, 1)),
        Property(name="uplata13", type=Uplata, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_v_KVACaKEeiYD9TOdwevwA",
    types={Putnik, Korisnik, Uplata, Aranzman, Vodic, Hotel, Grad, Drzava},
    associations={Vodic_Aranzman, Drzava_Grad, Grad_Hotel, Korisnik_Aranzman, Aranzman_Hotel, Putnik_Aranzman, Uplata_Putnik},
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