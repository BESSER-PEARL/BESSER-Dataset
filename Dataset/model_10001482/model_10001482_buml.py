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
TurboliftSystem = Class(name="TurboliftSystem")
Steuerung = Class(name="Steuerung")
TurboliftSchacht = Class(name="TurboliftSchacht")
Antrieb = Class(name="Antrieb")
Kabine = Class(name="Kabine")
Deck = Class(name="Deck")
BenannteEinrichtung = Class(name="BenannteEinrichtung")

# TurboliftSystem class attributes and methods
TurboliftSystem_alarmStufe: Property = Property(name="alarmStufe", type=IntegerType)
TurboliftSystem.attributes={TurboliftSystem_alarmStufe}

# Steuerung class attributes and methods

# TurboliftSchacht class attributes and methods
TurboliftSchacht_vertikal: Property = Property(name="vertikal", type=BooleanType)
TurboliftSchacht.attributes={TurboliftSchacht_vertikal}

# Antrieb class attributes and methods
Antrieb_aNTRIEBSART: Property = Property(name="aNTRIEBSART", type=StringType)
Antrieb.attributes={Antrieb_aNTRIEBSART}

# Kabine class attributes and methods
Kabine_tuerZustand: Property = Property(name="tuerZustand", type=BooleanType)
Kabine.attributes={Kabine_tuerZustand}

# Deck class attributes and methods
Deck_sektion: Property = Property(name="sektion", type=StringType)
Deck_fahrtWunsch: Property = Property(name="fahrtWunsch", type=BooleanType)
Deck.attributes={Deck_fahrtWunsch, Deck_sektion}

# BenannteEinrichtung class attributes and methods
BenannteEinrichtung_name: Property = Property(name="name", type=StringType)
BenannteEinrichtung.attributes={BenannteEinrichtung_name}

# Relationships
verwaltet: BinaryAssociation = BinaryAssociation(
    name="verwaltet",
    ends={
        Property(name="turboliftSchaechte0", type=TurboliftSchacht, multiplicity=Multiplicity(1, 9999)),
        Property(name="toDelete1", type=Steuerung, multiplicity=Multiplicity(1, 1))
    }
)
kennt: BinaryAssociation = BinaryAssociation(
    name="kennt",
    ends={
        Property(name="position2", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="toDelete3", type=Kabine, multiplicity=Multiplicity(0, 9999))
    }
)
kennt2: BinaryAssociation = BinaryAssociation(
    name="kennt2",
    ends={
        Property(name="fahrtziele4", type=Deck, multiplicity=Multiplicity(0, 9999)),
        Property(name="toDelete5", type=Kabine, multiplicity=Multiplicity(0, 9999))
    }
)
kennt3: BinaryAssociation = BinaryAssociation(
    name="kennt3",
    ends={
        Property(name="decks6", type=Deck, multiplicity=Multiplicity(1, 9999)),
        Property(name="toDelete7", type=TurboliftSchacht, multiplicity=Multiplicity(0, 9999))
    }
)
besteht_aus: BinaryAssociation = BinaryAssociation(
    name="besteht_aus",
    ends={
        Property(name="turboliftSchaechte8", type=TurboliftSchacht, multiplicity=Multiplicity(1, 9999)),
        Property(name="toDelete9", type=TurboliftSystem, multiplicity=Multiplicity(1, 1))
    }
)
TurboliftSystem_Steuerung: BinaryAssociation = BinaryAssociation(
    name="TurboliftSystem_Steuerung",
    ends={
        Property(name="steuerung10", type=Steuerung, multiplicity=Multiplicity(1, 1)),
        Property(name="toDelete11", type=TurboliftSystem, multiplicity=Multiplicity(1, 1))
    }
)
TurboliftSchacht_Antrieb: BinaryAssociation = BinaryAssociation(
    name="TurboliftSchacht_Antrieb",
    ends={
        Property(name="antrieb12", type=Antrieb, multiplicity=Multiplicity(1, 1)),
        Property(name="toDelete13", type=TurboliftSchacht, multiplicity=Multiplicity(1, 1))
    }
)
TurboliftSchacht_Kabine: BinaryAssociation = BinaryAssociation(
    name="TurboliftSchacht_Kabine",
    ends={
        Property(name="kabine14", type=Kabine, multiplicity=Multiplicity(1, 1)),
        Property(name="toDelete15", type=TurboliftSchacht, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9vTl0NnMEeeQi8PFukjNiw",
    types={TurboliftSystem, Steuerung, TurboliftSchacht, Antrieb, Kabine, Deck, BenannteEinrichtung},
    associations={verwaltet, kennt, kennt2, kennt3, besteht_aus, TurboliftSystem_Steuerung, TurboliftSchacht_Antrieb, TurboliftSchacht_Kabine},
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