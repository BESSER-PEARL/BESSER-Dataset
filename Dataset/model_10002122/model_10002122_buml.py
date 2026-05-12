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

# Enumerations
ExemplarStatus: Enumeration = Enumeration(
    name="ExemplarStatus",
    literals={
            
    }
)

# Classes
Buch = Class(name="Buch")
Videos_DVDS = Class(name="Videos_DVDS")
Zeitschrift = Class(name="Zeitschrift")
Entleihungsgegenstand = Class(name="Entleihungsgegenstand", is_abstract=True)
Exemplar = Class(name="Exemplar")
Entlehnung = Class(name="Entlehnung")
Kunde = Class(name="Kunde")
Entlehnausweis = Class(name="Entlehnausweis")
Reservierung = Class(name="Reservierung")

# Buch class attributes and methods
Buch_ISBN: Property = Property(name="ISBN", type=StringType)
Buch_Autor: Property = Property(name="Autor", type=StringType)
Buch.attributes={Buch_Autor, Buch_ISBN}

# Videos_DVDS class attributes and methods
Videos_DVDS_Laufzeit: Property = Property(name="Laufzeit", type=IntegerType)
Videos_DVDS_Regisseur: Property = Property(name="Regisseur", type=StringType)
Videos_DVDS_entLeihungsGeb_hr: Property = Property(name="entLeihungsGeb_hr", type=StringType)
Videos_DVDS_AnzahlEntlehnungen: Property = Property(name="AnzahlEntlehnungen", type=IntegerType)
Videos_DVDS.attributes={Videos_DVDS_AnzahlEntlehnungen, Videos_DVDS_Regisseur, Videos_DVDS_entLeihungsGeb_hr, Videos_DVDS_Laufzeit}

# Zeitschrift class attributes and methods
Zeitschrift_Ausgabe: Property = Property(name="Ausgabe", type=StringType)
Zeitschrift_Jahrgang: Property = Property(name="Jahrgang", type=IntegerType)
Zeitschrift.attributes={Zeitschrift_Jahrgang, Zeitschrift_Ausgabe}

# Entleihungsgegenstand class attributes and methods
Entleihungsgegenstand_einkaufspreis: Property = Property(name="einkaufspreis", type=StringType)
Entleihungsgegenstand_kurzbeschreibung: Property = Property(name="kurzbeschreibung", type=StringType)
Entleihungsgegenstand_titel: Property = Property(name="titel", type=StringType)
Entleihungsgegenstand.attributes={Entleihungsgegenstand_einkaufspreis, Entleihungsgegenstand_titel, Entleihungsgegenstand_kurzbeschreibung}

# Exemplar class attributes and methods
Exemplar_exemplarNummer: Property = Property(name="exemplarNummer", type=StringType)
Exemplar.attributes={Exemplar_exemplarNummer}

# Entlehnung class attributes and methods
Entlehnung_ausLeihDatun: Property = Property(name="ausLeihDatun", type=StringType)
Entlehnung_rueckGDatum: Property = Property(name="rueckGDatum", type=StringType)
Entlehnung_ausLeihFrist: Property = Property(name="ausLeihFrist", type=StringType)
Entlehnung_maxAnzahlFristTage: Property = Property(name="maxAnzahlFristTage", type=IntegerType)
Entlehnung.attributes={Entlehnung_maxAnzahlFristTage, Entlehnung_ausLeihDatun, Entlehnung_rueckGDatum, Entlehnung_ausLeihFrist}

# Kunde class attributes and methods
Kunde_Anschrift: Property = Property(name="Anschrift", type=StringType)
Kunde_Name: Property = Property(name="Name", type=StringType)
Kunde.attributes={Kunde_Name, Kunde_Anschrift}

# Entlehnausweis class attributes and methods
Entlehnausweis_id: Property = Property(name="id", type=IntegerType)
Entlehnausweis_g_ltigKeitsDatum: Property = Property(name="g_ltigKeitsDatum", type=StringType)
Entlehnausweis.attributes={Entlehnausweis_g_ltigKeitsDatum, Entlehnausweis_id}

# Reservierung class attributes and methods
Reservierung_reservierungsDatum: Property = Property(name="reservierungsDatum", type=StringType)
Reservierung_reservierungsEnde: Property = Property(name="reservierungsEnde", type=StringType)
Reservierung.attributes={Reservierung_reservierungsEnde, Reservierung_reservierungsDatum}

# Relationships
Exemplar_Entlehnung: BinaryAssociation = BinaryAssociation(
    name="Exemplar_Entlehnung",
    ends={
        Property(name="wird_Entlehnt0", type=Entlehnung, multiplicity=Multiplicity(0, 9999)),
        Property(name="anzahl_Exem_1", type=Exemplar, multiplicity=Multiplicity(1, 9999))
    }
)
Kunde_Entlehnung: BinaryAssociation = BinaryAssociation(
    name="Kunde_Entlehnung",
    ends={
        Property(name="anzahl2", type=Entlehnung, multiplicity=Multiplicity(0, 9999)),
        Property(name="geh_rt_zu3", type=Kunde, multiplicity=Multiplicity(1, 1))
    }
)
Kunde_Entlehnausweis: BinaryAssociation = BinaryAssociation(
    name="Kunde_Entlehnausweis",
    ends={
        Property(name="hat_einen4", type=Entlehnausweis, multiplicity=Multiplicity(0, 1)),
        Property(name="geh_rt_zu5", type=Kunde, multiplicity=Multiplicity(1, 1))
    }
)
Kunde_Reservierung: BinaryAssociation = BinaryAssociation(
    name="Kunde_Reservierung",
    ends={
        Property(name="anzahl6", type=Reservierung, multiplicity=Multiplicity(0, 9999)),
        Property(name="geh_rt_zu7", type=Kunde, multiplicity=Multiplicity(1, 1))
    }
)
Reservierung_Exemplar: BinaryAssociation = BinaryAssociation(
    name="Reservierung_Exemplar",
    ends={
        Property(name="anzahl_Exem_8", type=Exemplar, multiplicity=Multiplicity(1, 9999)),
        Property(name="wir_reserviert9", type=Reservierung, multiplicity=Multiplicity(0, 9999))
    }
)
Entleihungsgegenstand_Exemplar: BinaryAssociation = BinaryAssociation(
    name="Entleihungsgegenstand_Exemplar",
    ends={
        Property(name="geh_rt_zu10", type=Exemplar, multiplicity=Multiplicity(0, 1)),
        Property(name="hat11", type=Entleihungsgegenstand, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_pxoYkLriEeedTfUoC_GfaA",
    types={Buch, Videos_DVDS, Zeitschrift, Entleihungsgegenstand, Exemplar, Entlehnung, Kunde, Entlehnausweis, Reservierung, ExemplarStatus},
    associations={Exemplar_Entlehnung, Kunde_Entlehnung, Kunde_Entlehnausweis, Kunde_Reservierung, Reservierung_Exemplar, Entleihungsgegenstand_Exemplar},
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