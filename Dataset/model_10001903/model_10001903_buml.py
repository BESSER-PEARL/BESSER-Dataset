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
enum_form: Enumeration = Enumeration(
    name="enum_form",
    literals={
            
    }
)

form: Enumeration = Enumeration(
    name="form",
    literals={
            
    }
)

# Classes
lager = Class(name="lager")
teig = Class(name="teig")
plaetzchen = Class(name="plaetzchen")
auftrag = Class(name="auftrag")
zutat = Class(name="zutat")
plaetzchenForm = Class(name="plaetzchenForm")
groesse = Class(name="groesse")
backofen = Class(name="backofen")
prozessHeizen = Class(name="prozessHeizen")
prozessBand = Class(name="prozessBand")
teigmaschine = Class(name="teigmaschine")
belagmaschine = Class(name="belagmaschine")
Blech = Class(name="Blech")
zutat_ = Class(name="zutat_")
list_zutat__ = Class(name="list_zutat__")
teig_ = Class(name="teig_")
teig_2 = Class(name="teig_2")
plaetzchenForm_ = Class(name="plaetzchenForm_")
string_ = Class(name="string_")
myException = Class(name="myException")
array_int__ = Class(name="array_int__")
groesse_ = Class(name="groesse_")
array_int_3_ = Class(name="array_int_3_")
lager_ = Class(name="lager_")
teigmaschine_ = Class(name="teigmaschine_")
ostream_ = Class(name="ostream_")
ostream_1 = Class(name="ostream_1")
const_zutat = Class(name="const_zutat")

# lager class attributes and methods
lager_bestandZutaten: Property = Property(name="bestandZutaten", type=StringType)
lager_attribute: Property = Property(name="attribute", type=StringType)
lager.attributes={lager_bestandZutaten, lager_attribute}

# teig class attributes and methods
teig_attribute: Property = Property(name="attribute", type=StringType)
teig_name: Property = Property(name="name", type=StringType)
teig_zutaten: Property = Property(name="zutaten", type=StringType)
teig_form: Property = Property(name="form", type=plaetzchenForm)
teig_menge: Property = Property(name="menge", type=StringType)
teig.attributes={teig_name, teig_menge, teig_attribute, teig_form, teig_zutaten}

# plaetzchen class attributes and methods
plaetzchen_name: Property = Property(name="name", type=StringType)
plaetzchen_pteig: Property = Property(name="pteig", type=teig_)
plaetzchen_pguss: Property = Property(name="pguss", type=zutat_)
plaetzchen_pdeko: Property = Property(name="pdeko", type=zutat_)
plaetzchen.attributes={plaetzchen_pguss, plaetzchen_pdeko, plaetzchen_name, plaetzchen_pteig}

# auftrag class attributes and methods
auftrag_pform: Property = Property(name="pform", type=plaetzchenForm_)
auftrag_pteig: Property = Property(name="pteig", type=teig_)
auftrag_pguss: Property = Property(name="pguss", type=zutat_)
auftrag_pdeko: Property = Property(name="pdeko", type=zutat_)
auftrag_pteigmaschine: Property = Property(name="pteigmaschine", type=teigmaschine_)
auftrag_menge: Property = Property(name="menge", type=StringType)
auftrag_name: Property = Property(name="name", type=StringType)
auftrag_backtemp: Property = Property(name="backtemp", type=StringType)
auftrag_backzeit: Property = Property(name="backzeit", type=StringType)
auftrag_attribute: Property = Property(name="attribute", type=StringType)
auftrag_backofen: Property = Property(name="backofen", type=backofen)
auftrag_belagmaschine: Property = Property(name="belagmaschine", type=belagmaschine)
auftrag.attributes={auftrag_pdeko, auftrag_backtemp, auftrag_pteig, auftrag_pguss, auftrag_pteigmaschine, auftrag_menge, auftrag_attribute, auftrag_backofen, auftrag_pform, auftrag_belagmaschine, auftrag_name, auftrag_backzeit}

# zutat class attributes and methods
zutat_name: Property = Property(name="name", type=StringType)
zutat_menge: Property = Property(name="menge", type=StringType)
zutat_einheit: Property = Property(name="einheit", type=StringType)
zutat.attributes={zutat_menge, zutat_name, zutat_einheit}

# plaetzchenForm class attributes and methods
plaetzchenForm_form: Property = Property(name="form", type=enum_form)
plaetzchenForm_groesse: Property = Property(name="groesse", type=groesse)
plaetzchenForm.attributes={plaetzchenForm_form, plaetzchenForm_groesse}

# groesse class attributes and methods
groesse_name: Property = Property(name="name", type=StringType)
groesse_breite: Property = Property(name="breite", type=StringType)
groesse_laenge: Property = Property(name="laenge", type=StringType)
groesse_name1: Property = Property(name="name1", type=StringType)
groesse.attributes={groesse_laenge, groesse_name1, groesse_name, groesse_breite}

# backofen class attributes and methods
backofen_ofenlaenge: Property = Property(name="ofenlaenge", type=StringType)
backofen_backzeit: Property = Property(name="backzeit", type=StringType)
backofen_backtemp: Property = Property(name="backtemp", type=StringType)
backofen_teigmaschine: Property = Property(name="teigmaschine", type=teigmaschine)
backofen_bandgeschwindigkeit: Property = Property(name="bandgeschwindigkeit", type=StringType)
backofen.attributes={backofen_backzeit, backofen_ofenlaenge, backofen_teigmaschine, backofen_backtemp, backofen_bandgeschwindigkeit}

# prozessHeizen class attributes and methods
prozessHeizen_temperatur_ist: Property = Property(name="temperatur_ist", type=StringType)
prozessHeizen_attribute: Property = Property(name="attribute", type=StringType)
prozessHeizen.attributes={prozessHeizen_temperatur_ist, prozessHeizen_attribute}

# prozessBand class attributes and methods
prozessBand_geschwindigkeit_ist: Property = Property(name="geschwindigkeit_ist", type=StringType)
prozessBand.attributes={prozessBand_geschwindigkeit_ist}

# teigmaschine class attributes and methods
teigmaschine_blechgroesse: Property = Property(name="blechgroesse", type=groesse_)
teigmaschine_abstand: Property = Property(name="abstand", type=StringType)
teigmaschine_anzBleche: Property = Property(name="anzBleche", type=StringType)
teigmaschine_anzBlechePlaetzchen: Property = Property(name="anzBlechePlaetzchen", type=array_int_3_)
teigmaschine_anzPlaetzchenLetzesBlech: Property = Property(name="anzPlaetzchenLetzesBlech", type=StringType)
teigmaschine.attributes={teigmaschine_anzBleche, teigmaschine_anzBlechePlaetzchen, teigmaschine_anzPlaetzchenLetzesBlech, teigmaschine_blechgroesse, teigmaschine_abstand}

# belagmaschine class attributes and methods

# Blech class attributes and methods

# zutat_ class attributes and methods

# list_zutat__ class attributes and methods

# teig_ class attributes and methods

# teig_2 class attributes and methods

# plaetzchenForm_ class attributes and methods

# string_ class attributes and methods

# myException class attributes and methods

# array_int__ class attributes and methods

# groesse_ class attributes and methods

# array_int_3_ class attributes and methods

# lager_ class attributes and methods

# teigmaschine_ class attributes and methods

# ostream_ class attributes and methods

# ostream_1 class attributes and methods

# const_zutat class attributes and methods

# Relationships
backofen_myException: BinaryAssociation = BinaryAssociation(
    name="backofen_myException",
    ends={
        Property(name="myException34", type=myException, multiplicity=Multiplicity(0, 1)),
        Property(name="backofen35", type=backofen, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchen_teig: BinaryAssociation = BinaryAssociation(
    name="plaetzchen_teig",
    ends={
        Property(name="teig36", type=teig, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen37", type=plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchen_zutat: BinaryAssociation = BinaryAssociation(
    name="plaetzchen_zutat",
    ends={
        Property(name="zutat38", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen39", type=plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchenForm_groesse: BinaryAssociation = BinaryAssociation(
    name="plaetzchenForm_groesse",
    ends={
        Property(name="groesse20", type=groesse, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm1", type=plaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
prozessHeizen_backstrasse: BinaryAssociation = BinaryAssociation(
    name="prozessHeizen_backstrasse",
    ends={
        Property(name="backstrasse2", type=backofen, multiplicity=Multiplicity(0, 1)),
        Property(name="prozessHeizen3", type=prozessHeizen, multiplicity=Multiplicity(0, 1))
    }
)
prozessBand_backstrasse: BinaryAssociation = BinaryAssociation(
    name="prozessBand_backstrasse",
    ends={
        Property(name="backstrasse4", type=backofen, multiplicity=Multiplicity(0, 1)),
        Property(name="prozessBand5", type=prozessBand, multiplicity=Multiplicity(0, 1))
    }
)
groesse_belch: BinaryAssociation = BinaryAssociation(
    name="groesse_belch",
    ends={
        Property(name="belch6", type=teigmaschine, multiplicity=Multiplicity(0, 1)),
        Property(name="groesse7", type=groesse, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_lager: BinaryAssociation = BinaryAssociation(
    name="auftrag_lager",
    ends={
        Property(name="lager8", type=lager, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag9", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
lager_zutat: BinaryAssociation = BinaryAssociation(
    name="lager_zutat",
    ends={
        Property(name="zutat10", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="lager11", type=lager, multiplicity=Multiplicity(0, 1))
    }
)
lager_teig: BinaryAssociation = BinaryAssociation(
    name="lager_teig",
    ends={
        Property(name="teig12", type=teig, multiplicity=Multiplicity(0, 1)),
        Property(name="lager13", type=lager, multiplicity=Multiplicity(0, 1))
    }
)
lager_myException: BinaryAssociation = BinaryAssociation(
    name="lager_myException",
    ends={
        Property(name="myException14", type=myException, multiplicity=Multiplicity(0, 1)),
        Property(name="lager15", type=lager, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_myException: BinaryAssociation = BinaryAssociation(
    name="auftrag_myException",
    ends={
        Property(name="myException16", type=myException, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag17", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
teig_auftrag: BinaryAssociation = BinaryAssociation(
    name="teig_auftrag",
    ends={
        Property(name="auftrag18", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="teig19", type=teig, multiplicity=Multiplicity(0, 1))
    }
)
zutat_auftrag: BinaryAssociation = BinaryAssociation(
    name="zutat_auftrag",
    ends={
        Property(name="auftrag20", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="zutat21", type=zutat, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_teigmaschine: BinaryAssociation = BinaryAssociation(
    name="auftrag_teigmaschine",
    ends={
        Property(name="teigmaschine22", type=teigmaschine, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag23", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_backofen: BinaryAssociation = BinaryAssociation(
    name="auftrag_backofen",
    ends={
        Property(name="backofen224", type=backofen, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag25", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
auftrag_belagmaschine: BinaryAssociation = BinaryAssociation(
    name="auftrag_belagmaschine",
    ends={
        Property(name="belagmaschine226", type=belagmaschine, multiplicity=Multiplicity(0, 1)),
        Property(name="auftrag27", type=auftrag, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchen_auftrag: BinaryAssociation = BinaryAssociation(
    name="plaetzchen_auftrag",
    ends={
        Property(name="auftrag28", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchen29", type=plaetzchen, multiplicity=Multiplicity(0, 1))
    }
)
plaetzchenForm_auftrag: BinaryAssociation = BinaryAssociation(
    name="plaetzchenForm_auftrag",
    ends={
        Property(name="auftrag30", type=auftrag, multiplicity=Multiplicity(0, 1)),
        Property(name="plaetzchenForm31", type=plaetzchenForm, multiplicity=Multiplicity(0, 1))
    }
)
teig_zutat: BinaryAssociation = BinaryAssociation(
    name="teig_zutat",
    ends={
        Property(name="zutat32", type=zutat, multiplicity=Multiplicity(0, 1)),
        Property(name="teig33", type=teig, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cEe8kHVKEemwWpuaZV3QLQ",
    types={lager, teig, plaetzchen, auftrag, zutat, plaetzchenForm, groesse, backofen, prozessHeizen, prozessBand, teigmaschine, belagmaschine, Blech, zutat_, list_zutat__, teig_, teig_2, plaetzchenForm_, string_, myException, array_int__, groesse_, array_int_3_, lager_, teigmaschine_, ostream_, ostream_1, const_zutat, enum_form, form},
    associations={backofen_myException, plaetzchen_teig, plaetzchen_zutat, plaetzchenForm_groesse, prozessHeizen_backstrasse, prozessBand_backstrasse, groesse_belch, auftrag_lager, lager_zutat, lager_teig, lager_myException, auftrag_myException, teig_auftrag, zutat_auftrag, auftrag_teigmaschine, auftrag_backofen, auftrag_belagmaschine, plaetzchen_auftrag, plaetzchenForm_auftrag, teig_zutat},
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