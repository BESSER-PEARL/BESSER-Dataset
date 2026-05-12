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
Persoon = Class(name="Persoon")
Klant = Class(name="Klant")
Beheerder = Class(name="Beheerder")
Hoofdbeheerder = Class(name="Hoofdbeheerder")
Factuur = Class(name="Factuur")
Bestelregel = Class(name="Bestelregel")
Product = Class(name="Product")
Nieuwsbericht = Class(name="Nieuwsbericht")
Adres = Class(name="Adres")
Categorie = Class(name="Categorie")
Afbeelding = Class(name="Afbeelding")
Contactformulier = Class(name="Contactformulier")

# Persoon class attributes and methods
Persoon_voornaam: Property = Property(name="voornaam", type=StringType)
Persoon_tussenvoegsel: Property = Property(name="tussenvoegsel", type=StringType)
Persoon_achternaam: Property = Property(name="achternaam", type=StringType)
Persoon_e_mail: Property = Property(name="e_mail", type=StringType)
Persoon_wachtwoord: Property = Property(name="wachtwoord", type=StringType)
Persoon.attributes={Persoon_e_mail, Persoon_wachtwoord, Persoon_tussenvoegsel, Persoon_achternaam, Persoon_voornaam}

# Klant class attributes and methods
Klant_geboortedatum: Property = Property(name="geboortedatum", type=StringType)
Klant_telefoonnummer: Property = Property(name="telefoonnummer", type=StringType)
Klant.attributes={Klant_geboortedatum, Klant_telefoonnummer}

# Beheerder class attributes and methods
Beheerder_rechten: Property = Property(name="rechten", type=BooleanType)
Beheerder.attributes={Beheerder_rechten}

# Hoofdbeheerder class attributes and methods

# Factuur class attributes and methods
Factuur_datum: Property = Property(name="datum", type=StringType)
Factuur_status: Property = Property(name="status", type=StringType)
Factuur_btw: Property = Property(name="btw", type=IntegerType)
Factuur.attributes={Factuur_btw, Factuur_status, Factuur_datum}

# Bestelregel class attributes and methods
Bestelregel_aantal: Property = Property(name="aantal", type=IntegerType)
Bestelregel.attributes={Bestelregel_aantal}

# Product class attributes and methods
Product_naam: Property = Property(name="naam", type=StringType)
Product_prijs: Property = Property(name="prijs", type=IntegerType)
Product_beschrijving: Property = Property(name="beschrijving", type=StringType)
Product_voorraad: Property = Property(name="voorraad", type=IntegerType)
Product_actief: Property = Property(name="actief", type=BooleanType)
Product.attributes={Product_prijs, Product_naam, Product_actief, Product_voorraad, Product_beschrijving}

# Nieuwsbericht class attributes and methods
Nieuwsbericht_titel: Property = Property(name="titel", type=StringType)
Nieuwsbericht_tekst: Property = Property(name="tekst", type=StringType)
Nieuwsbericht.attributes={Nieuwsbericht_titel, Nieuwsbericht_tekst}

# Adres class attributes and methods
Adres_postcode: Property = Property(name="postcode", type=StringType)
Adres_huisnummer: Property = Property(name="huisnummer", type=IntegerType)
Adres_bijvoegsel: Property = Property(name="bijvoegsel", type=StringType)
Adres_straatnaam: Property = Property(name="straatnaam", type=StringType)
Adres_stad: Property = Property(name="stad", type=StringType)
Adres.attributes={Adres_stad, Adres_straatnaam, Adres_huisnummer, Adres_postcode, Adres_bijvoegsel}

# Categorie class attributes and methods

# Afbeelding class attributes and methods
Afbeelding_naam: Property = Property(name="naam", type=StringType)
Afbeelding_locatie: Property = Property(name="locatie", type=StringType)
Afbeelding_datum: Property = Property(name="datum", type=StringType)
Afbeelding.attributes={Afbeelding_locatie, Afbeelding_datum, Afbeelding_naam}

# Contactformulier class attributes and methods
Contactformulier_tekst: Property = Property(name="tekst", type=StringType)
Contactformulier.attributes={Contactformulier_tekst}

# Relationships
bekijkt: BinaryAssociation = BinaryAssociation(
    name="bekijkt",
    ends={
        Property(name="product0", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="klant1", type=Klant, multiplicity=Multiplicity(0, 9999))
    }
)
heeft: BinaryAssociation = BinaryAssociation(
    name="heeft",
    ends={
        Property(name="klant2", type=Klant, multiplicity=Multiplicity(1, 9999)),
        Property(name="adres3", type=Adres, multiplicity=Multiplicity(1, 1))
    }
)
staat_in: BinaryAssociation = BinaryAssociation(
    name="staat_in",
    ends={
        Property(name="product4", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="bestelregel5", type=Bestelregel, multiplicity=Multiplicity(0, 9999))
    }
)
staat_in1: BinaryAssociation = BinaryAssociation(
    name="staat_in1",
    ends={
        Property(name="product6", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="categorie7", type=Categorie, multiplicity=Multiplicity(1, 9999))
    }
)
maakt: BinaryAssociation = BinaryAssociation(
    name="maakt",
    ends={
        Property(name="hoofdbeheerder8", type=Hoofdbeheerder, multiplicity=Multiplicity(1, 1)),
        Property(name="post9", type=Nieuwsbericht, multiplicity=Multiplicity(0, 9999))
    }
)
heeft1: BinaryAssociation = BinaryAssociation(
    name="heeft1",
    ends={
        Property(name="product10", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="afbeelding11", type=Afbeelding, multiplicity=Multiplicity(0, 1))
    }
)
bevestigt: BinaryAssociation = BinaryAssociation(
    name="bevestigt",
    ends={
        Property(name="beheerder12", type=Beheerder, multiplicity=Multiplicity(1, 1)),
        Property(name="factuur13", type=Factuur, multiplicity=Multiplicity(0, 9999))
    }
)
beheert: BinaryAssociation = BinaryAssociation(
    name="beheert",
    ends={
        Property(name="product14", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="beheerder15", type=Beheerder, multiplicity=Multiplicity(0, 9999))
    }
)
vult_in: BinaryAssociation = BinaryAssociation(
    name="vult_in",
    ends={
        Property(name="contactformulier16", type=Contactformulier, multiplicity=Multiplicity(0, 9999)),
        Property(name="klant17", type=Klant, multiplicity=Multiplicity(1, 1))
    }
)
bekijkt1: BinaryAssociation = BinaryAssociation(
    name="bekijkt1",
    ends={
        Property(name="contactformulier18", type=Contactformulier, multiplicity=Multiplicity(0, 9999)),
        Property(name="beheerder19", type=Beheerder, multiplicity=Multiplicity(0, 9999))
    }
)
heeft2: BinaryAssociation = BinaryAssociation(
    name="heeft2",
    ends={
        Property(name="bestelregel20", type=Bestelregel, multiplicity=Multiplicity(1, 9999)),
        Property(name="factuur21", type=Factuur, multiplicity=Multiplicity(1, 1))
    }
)
betaalt: BinaryAssociation = BinaryAssociation(
    name="betaalt",
    ends={
        Property(name="bestelregel22", type=Factuur, multiplicity=Multiplicity(0, 9999)),
        Property(name="klant23", type=Klant, multiplicity=Multiplicity(1, 1))
    }
)
heeft3: BinaryAssociation = BinaryAssociation(
    name="heeft3",
    ends={
        Property(name="nieuwsbericht24", type=Nieuwsbericht, multiplicity=Multiplicity(0, 9999)),
        Property(name="afbeelding25", type=Afbeelding, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2e3C4M6bEeeMV96X50GAvA",
    types={Persoon, Klant, Beheerder, Hoofdbeheerder, Factuur, Bestelregel, Product, Nieuwsbericht, Adres, Categorie, Afbeelding, Contactformulier},
    associations={bekijkt, heeft, staat_in, staat_in1, maakt, heeft1, bevestigt, beheert, vult_in, bekijkt1, heeft2, betaalt, heeft3},
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