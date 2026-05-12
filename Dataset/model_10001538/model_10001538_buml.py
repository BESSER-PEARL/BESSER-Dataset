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
plaetzchen = Class(name="plaetzchen")
zutat = Class(name="zutat")
auftrag = Class(name="auftrag")
backstrasse = Class(name="backstrasse")
ea_helfer = Class(name="ea_helfer")
zutaten = Class(name="zutaten")

# plaetzchen class attributes and methods
plaetzchen_breite: Property = Property(name="breite", type=StringType)
plaetzchen_laenge: Property = Property(name="laenge", type=StringType)
plaetzchen_form: Property = Property(name="form", type=StringType)
plaetzchen_backzeit: Property = Property(name="backzeit", type=StringType)
plaetzchen_temperatur: Property = Property(name="temperatur", type=StringType)
plaetzchen_teig: Property = Property(name="teig", type=StringType)
plaetzchen_belag: Property = Property(name="belag", type=StringType)
plaetzchen.attributes={plaetzchen_temperatur, plaetzchen_teig, plaetzchen_belag, plaetzchen_laenge, plaetzchen_breite, plaetzchen_form, plaetzchen_backzeit}

# zutat class attributes and methods
zutat_name: Property = Property(name="name", type=StringType)
zutat_menge: Property = Property(name="menge", type=StringType)
zutat_einheit: Property = Property(name="einheit", type=StringType)
zutat.attributes={zutat_name, zutat_einheit, zutat_menge}

# auftrag class attributes and methods
auftrag_name: Property = Property(name="name", type=StringType)
auftrag_auftragsPlaetzchen: Property = Property(name="auftragsPlaetzchen", type=StringType)
auftrag_anzahl: Property = Property(name="anzahl", type=StringType)
auftrag.attributes={auftrag_name, auftrag_auftragsPlaetzchen, auftrag_anzahl}

# backstrasse class attributes and methods
backstrasse_BLECHBREITE: Property = Property(name="BLECHBREITE", type=StringType)
backstrasse_BLECHLAENGE: Property = Property(name="BLECHLAENGE", type=StringType)
backstrasse_eingabeAusgabe: Property = Property(name="eingabeAusgabe", type=StringType)
backstrasse_zutatenVorrat: Property = Property(name="zutatenVorrat", type=StringType)
backstrasse_backAuftrag: Property = Property(name="backAuftrag", type=StringType)
backstrasse_geschwindigkeit: Property = Property(name="geschwindigkeit", type=StringType)
backstrasse_ofenlaenge: Property = Property(name="ofenlaenge", type=StringType)
backstrasse_temperatur: Property = Property(name="temperatur", type=StringType)
backstrasse_gestoppt: Property = Property(name="gestoppt", type=StringType)
backstrasse.attributes={backstrasse_backAuftrag, backstrasse_temperatur, backstrasse_BLECHLAENGE, backstrasse_eingabeAusgabe, backstrasse_gestoppt, backstrasse_zutatenVorrat, backstrasse_ofenlaenge, backstrasse_BLECHBREITE, backstrasse_geschwindigkeit}

# ea_helfer class attributes and methods

# zutaten class attributes and methods
zutaten_zutatenListe: Property = Property(name="zutatenListe", type=StringType)
zutaten.attributes={zutaten_zutatenListe}

# Relationships
plaetzchen_zutat: BinaryAssociation = BinaryAssociation(
    name="plaetzchen_zutat",
    ends={
        Property(name="zutat0", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen1", type=plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_plaetzchen: BinaryAssociation = BinaryAssociation(
    name="auftrag_plaetzchen",
    ends={
        Property(name="plaetzchen22", type=plaetzchen, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag3", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
backstrasse_auftrag: BinaryAssociation = BinaryAssociation(
    name="backstrasse_auftrag",
    ends={
        Property(name="auftrag24", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="backstrasse5", type=backstrasse, multiplicity=Multiplicity(0, 1))
    }
)
backstrasse_eaHelfer: BinaryAssociation = BinaryAssociation(
    name="backstrasse_eaHelfer",
    ends={
        Property(name="eaHelfer6", type=ea_helfer, multiplicity=Multiplicity(0, 1)),
        Property(name="backstrasse7", type=backstrasse, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchen_teig: BinaryAssociation = BinaryAssociation(
    name="plaetzchen_teig",
    ends={
        Property(name="teig28", type=zutaten, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen9", type=plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
teig_zutat: BinaryAssociation = BinaryAssociation(
    name="teig_zutat",
    ends={
        Property(name="zutat10", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="teig11", type=zutaten, multiplicity=Multiplicity(0, 1))
    }
)
backstrasse_zutat: BinaryAssociation = BinaryAssociation(
    name="backstrasse_zutat",
    ends={
        Property(name="zutat12", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="backstrasse13", type=backstrasse, multiplicity=Multiplicity(0, 1))
    }
)
zutat_auftrag: BinaryAssociation = BinaryAssociation(
    name="zutat_auftrag",
    ends={
        Property(name="auftrag14", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="zutat15", type=zutat, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_EImLMHVKEemwWpuaZV3QLQ",
    types={plaetzchen, zutat, auftrag, backstrasse, ea_helfer, zutaten},
    associations={plaetzchen_zutat, auftrag_plaetzchen, backstrasse_auftrag, backstrasse_eaHelfer, plaetzchen_teig, teig_zutat, backstrasse_zutat, zutat_auftrag},
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