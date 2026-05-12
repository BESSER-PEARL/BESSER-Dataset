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
Zutaten = Class(name="Zutaten")
Zutat = Class(name="Zutat")
Plaetzchen = Class(name="Plaetzchen")
PlaetzchenDesignerForm = Class(name="PlaetzchenDesignerForm")
DateiEA = Class(name="DateiEA")
PlaetzchenAnzeigeForm = Class(name="PlaetzchenAnzeigeForm")
ZutatenEingabeForm = Class(name="ZutatenEingabeForm")
Auftrag = Class(name="Auftrag")

# Zutaten class attributes and methods
Zutaten_zutaten: Property = Property(name="zutaten", type=StringType)
Zutaten.attributes={Zutaten_zutaten}

# Zutat class attributes and methods
Zutat_name: Property = Property(name="name", type=StringType)
Zutat_einheit: Property = Property(name="einheit", type=StringType)
Zutat_menge: Property = Property(name="menge", type=StringType)
Zutat.attributes={Zutat_menge, Zutat_einheit, Zutat_name}

# Plaetzchen class attributes and methods
Plaetzchen_breite: Property = Property(name="breite", type=StringType)
Plaetzchen_laenge: Property = Property(name="laenge", type=StringType)
Plaetzchen_form: Property = Property(name="form", type=StringType)
Plaetzchen_backzeit: Property = Property(name="backzeit", type=StringType)
Plaetzchen_temperatur: Property = Property(name="temperatur", type=StringType)
Plaetzchen_teig: Property = Property(name="teig", type=StringType)
Plaetzchen_belag: Property = Property(name="belag", type=StringType)
Plaetzchen.attributes={Plaetzchen_backzeit, Plaetzchen_teig, Plaetzchen_form, Plaetzchen_laenge, Plaetzchen_belag, Plaetzchen_temperatur, Plaetzchen_breite}

# PlaetzchenDesignerForm class attributes and methods
PlaetzchenDesignerForm_BLECHBREITE: Property = Property(name="BLECHBREITE", type=StringType)
PlaetzchenDesignerForm_BLECHLAENGE: Property = Property(name="BLECHLAENGE", type=StringType)
PlaetzchenDesignerForm_datei: Property = Property(name="datei", type=StringType)
PlaetzchenDesignerForm_neuerAuftrag: Property = Property(name="neuerAuftrag", type=StringType)
PlaetzchenDesignerForm_neuesPlaetzchen: Property = Property(name="neuesPlaetzchen", type=StringType)
PlaetzchenDesignerForm_plaetzchenGeaendert: Property = Property(name="plaetzchenGeaendert", type=BooleanType)
PlaetzchenDesignerForm.attributes={PlaetzchenDesignerForm_BLECHBREITE, PlaetzchenDesignerForm_neuerAuftrag, PlaetzchenDesignerForm_plaetzchenGeaendert, PlaetzchenDesignerForm_datei, PlaetzchenDesignerForm_BLECHLAENGE, PlaetzchenDesignerForm_neuesPlaetzchen}

# DateiEA class attributes and methods

# PlaetzchenAnzeigeForm class attributes and methods
PlaetzchenAnzeigeForm_form: Property = Property(name="form", type=StringType)
PlaetzchenAnzeigeForm_breite: Property = Property(name="breite", type=StringType)
PlaetzchenAnzeigeForm_laenge: Property = Property(name="laenge", type=StringType)
PlaetzchenAnzeigeForm.attributes={PlaetzchenAnzeigeForm_form, PlaetzchenAnzeigeForm_breite, PlaetzchenAnzeigeForm_laenge}

# ZutatenEingabeForm class attributes and methods
ZutatenEingabeForm_neueZutat: Property = Property(name="neueZutat", type=StringType)
ZutatenEingabeForm.attributes={ZutatenEingabeForm_neueZutat}

# Auftrag class attributes and methods
Auftrag_name: Property = Property(name="name", type=StringType)
Auftrag_keks: Property = Property(name="keks", type=StringType)
Auftrag_anzahl: Property = Property(name="anzahl", type=StringType)
Auftrag.attributes={Auftrag_anzahl, Auftrag_name, Auftrag_keks}

# Relationships
PlaetzchenDesignerForm_PlaetzchenAnzeigeForm: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenDesignerForm_PlaetzchenAnzeigeForm",
    ends={
        Property(name="plaetzchenAnzeigeForm8", type=PlaetzchenAnzeigeForm, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenDesignerForm9", type=PlaetzchenDesignerForm, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenDesignerForm_Plaetzchen: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenDesignerForm_Plaetzchen",
    ends={
        Property(name="plaetzchen10", type=Plaetzchen, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenDesignerForm11", type=PlaetzchenDesignerForm, multiplicity=Multiplicity(0, 1))
    }
)
DateiEA_Plaetzchen: BinaryAssociation = BinaryAssociation(
    name="DateiEA_Plaetzchen",
    ends={
        Property(name="plaetzchen12", type=Plaetzchen, multiplicity=Multiplicity(0, 1)),
        Property(name="dateiEA13", type=DateiEA, multiplicity=Multiplicity(0, 1))
    }
)
ZutatenEingabe_PlaetzchenDesignerForm: BinaryAssociation = BinaryAssociation(
    name="ZutatenEingabe_PlaetzchenDesignerForm",
    ends={
        Property(name="plaetzchenDesignerForm14", type=PlaetzchenDesignerForm, multiplicity=Multiplicity(0, 1)),
        Property(name="zutatenEingabe15", type=ZutatenEingabeForm, multiplicity=Multiplicity(0, 1))
    }
)
ZutatenEingabe_Zutat: BinaryAssociation = BinaryAssociation(
    name="ZutatenEingabe_Zutat",
    ends={
        Property(name="zutat16", type=Zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="zutatenEingabe17", type=ZutatenEingabeForm, multiplicity=Multiplicity(0, 1))
    }
)
DateiEA_Auftrag: BinaryAssociation = BinaryAssociation(
    name="DateiEA_Auftrag",
    ends={
        Property(name="auftrag18", type=Auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="dateiEA19", type=DateiEA, multiplicity=Multiplicity(0, 1))
    }
)
Plaetzchen_Auftrag: BinaryAssociation = BinaryAssociation(
    name="Plaetzchen_Auftrag",
    ends={
        Property(name="auftrag20", type=Auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen221", type=Plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenDesignerForm_Auftrag: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenDesignerForm_Auftrag",
    ends={
        Property(name="auftrag22", type=Auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenDesignerForm23", type=PlaetzchenDesignerForm, multiplicity=Multiplicity(0, 1))
    }
)
Plaetzchen_Teig: BinaryAssociation = BinaryAssociation(
    name="Plaetzchen_Teig",
    ends={
        Property(name="teig20", type=Zutaten, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen1", type=Plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
Plaetzchen_Zutat: BinaryAssociation = BinaryAssociation(
    name="Plaetzchen_Zutat",
    ends={
        Property(name="zutat2", type=Zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen3", type=Plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
Teig_Zutat: BinaryAssociation = BinaryAssociation(
    name="Teig_Zutat",
    ends={
        Property(name="zutat4", type=Zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="teig5", type=Zutaten, multiplicity=Multiplicity(0, 1))
    }
)
PlaetzchenDesignerForm_DateiEA: BinaryAssociation = BinaryAssociation(
    name="PlaetzchenDesignerForm_DateiEA",
    ends={
        Property(name="dateiEA6", type=DateiEA, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenDesignerForm7", type=PlaetzchenDesignerForm, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_L9sfMHVKEemwWpuaZV3QLQ",
    types={Zutaten, Zutat, Plaetzchen, PlaetzchenDesignerForm, DateiEA, PlaetzchenAnzeigeForm, ZutatenEingabeForm, Auftrag},
    associations={PlaetzchenDesignerForm_PlaetzchenAnzeigeForm, PlaetzchenDesignerForm_Plaetzchen, DateiEA_Plaetzchen, ZutatenEingabe_PlaetzchenDesignerForm, ZutatenEingabe_Zutat, DateiEA_Auftrag, Plaetzchen_Auftrag, PlaetzchenDesignerForm_Auftrag, Plaetzchen_Teig, Plaetzchen_Zutat, Teig_Zutat, PlaetzchenDesignerForm_DateiEA},
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