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
sihuhu_World = Class(name="sihuhu::World")
NamedElement = Class(name="NamedElement")
sihuhu_Track = Class(name="sihuhu::Track")
sihuhu_Train = Class(name="sihuhu::Train")
sihuhu_Rail = Class(name="sihuhu::Rail")
sihuhu_Switch = Class(name="sihuhu::Switch")
sihuhu_TrackElement = Class(name="sihuhu::TrackElement", is_abstract=True)
TrackElement = Class(name="TrackElement")
sihuhu_Signal = Class(name="sihuhu::Signal")
sihuhu_SwitchConnection = Class(name="sihuhu::SwitchConnection")
Rail = Class(name="Rail")
sihuhu_NamedElement = Class(name="sihuhu::NamedElement", is_abstract=True)

# sihuhu_World class attributes and methods

# NamedElement class attributes and methods

# sihuhu_Track class attributes and methods

# sihuhu_Train class attributes and methods

# sihuhu_Rail class attributes and methods

# sihuhu_Switch class attributes and methods

# sihuhu_TrackElement class attributes and methods

# TrackElement class attributes and methods

# sihuhu_Signal class attributes and methods
sihuhu_Signal_enabled: Property = Property(name="enabled", type=BooleanType)
sihuhu_Signal.attributes={sihuhu_Signal_enabled}

# sihuhu_SwitchConnection class attributes and methods

# Rail class attributes and methods

# sihuhu_NamedElement class attributes and methods
sihuhu_NamedElement_name: Property = Property(name="name", type=StringType)
sihuhu_NamedElement.attributes={sihuhu_NamedElement_name}

# Relationships
tracks0: BinaryAssociation = BinaryAssociation(
    name="tracks0",
    ends={
        Property(name="sihuhu_Track", type=sihuhu_World, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_World", type=sihuhu_Track, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trains1: BinaryAssociation = BinaryAssociation(
    name="trains1",
    ends={
        Property(name="sihuhu_Train", type=sihuhu_World, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_World2", type=sihuhu_Train, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rails3: BinaryAssociation = BinaryAssociation(
    name="rails3",
    ends={
        Property(name="sihuhu_Rail", type=sihuhu_Track, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Track4", type=sihuhu_Rail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switches5: BinaryAssociation = BinaryAssociation(
    name="switches5",
    ends={
        Property(name="sihuhu_Switch", type=sihuhu_Track, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Track6", type=sihuhu_Switch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
train7: BinaryAssociation = BinaryAssociation(
    name="train7",
    ends={
        Property(name="Train", type=sihuhu_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="onTracks", type=sihuhu_Train, multiplicity=Multiplicity(0, 1))
    }
)
allowedTo8: BinaryAssociation = BinaryAssociation(
    name="allowedTo8",
    ends={
        Property(name="sihuhu_Signal", type=sihuhu_Rail, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Rail9", type=sihuhu_Signal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
allowedFrom10: BinaryAssociation = BinaryAssociation(
    name="allowedFrom10",
    ends={
        Property(name="sihuhu_Signal12", type=sihuhu_Rail, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Rail11", type=sihuhu_Signal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from13: BinaryAssociation = BinaryAssociation(
    name="from13",
    ends={
        Property(name="sihuhu_TrackElement", type=sihuhu_Rail, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Rail14", type=sihuhu_TrackElement, multiplicity=Multiplicity(0, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="sihuhu_TrackElement17", type=sihuhu_Rail, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Rail16", type=sihuhu_TrackElement, multiplicity=Multiplicity(0, 1))
    }
)
connections18: BinaryAssociation = BinaryAssociation(
    name="connections18",
    ends={
        Property(name="sihuhu_SwitchConnection", type=sihuhu_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Switch19", type=sihuhu_SwitchConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedRails20: BinaryAssociation = BinaryAssociation(
    name="connectedRails20",
    ends={
        Property(name="sihuhu_Rail22", type=sihuhu_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Switch21", type=sihuhu_Rail, multiplicity=Multiplicity(0, 9999))
    }
)
nextElement26: BinaryAssociation = BinaryAssociation(
    name="nextElement26",
    ends={
        Property(name="sihuhu_TrackElement28", type=sihuhu_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Train27", type=sihuhu_TrackElement, multiplicity=Multiplicity(0, 1))
    }
)
onTracks29: BinaryAssociation = BinaryAssociation(
    name="onTracks29",
    ends={
        Property(name="TrackElement", type=sihuhu_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="train", type=sihuhu_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
nextRail30: BinaryAssociation = BinaryAssociation(
    name="nextRail30",
    ends={
        Property(name="sihuhu_Rail32", type=sihuhu_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Signal31", type=sihuhu_Rail, multiplicity=Multiplicity(0, 1))
    }
)
activeConnection23: BinaryAssociation = BinaryAssociation(
    name="activeConnection23",
    ends={
        Property(name="sihuhu_SwitchConnection25", type=sihuhu_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="sihuhu_Switch24", type=sihuhu_SwitchConnection, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sihuhu_World_NamedElement = Generalization(general=NamedElement, specific=sihuhu_World)
gen_sihuhu_Track_NamedElement = Generalization(general=NamedElement, specific=sihuhu_Track)
gen_sihuhu_TrackElement_NamedElement = Generalization(general=NamedElement, specific=sihuhu_TrackElement)
gen_sihuhu_Rail_TrackElement = Generalization(general=TrackElement, specific=sihuhu_Rail)
gen_sihuhu_Switch_TrackElement = Generalization(general=TrackElement, specific=sihuhu_Switch)
gen_sihuhu_SwitchConnection_Rail = Generalization(general=Rail, specific=sihuhu_SwitchConnection)
gen_sihuhu_Train_NamedElement = Generalization(general=NamedElement, specific=sihuhu_Train)
gen_sihuhu_Signal_NamedElement = Generalization(general=NamedElement, specific=sihuhu_Signal)

# Domain Model
domain_model = DomainModel(
    name="sihuhu",
    types={sihuhu_World, NamedElement, sihuhu_Track, sihuhu_Train, sihuhu_Rail, sihuhu_Switch, sihuhu_TrackElement, TrackElement, sihuhu_Signal, sihuhu_SwitchConnection, Rail, sihuhu_NamedElement},
    associations={tracks0, trains1, rails3, switches5, train7, allowedTo8, allowedFrom10, from13, to15, connections18, connectedRails20, nextElement26, onTracks29, nextRail30, activeConnection23},
    generalizations={gen_sihuhu_World_NamedElement, gen_sihuhu_Track_NamedElement, gen_sihuhu_TrackElement_NamedElement, gen_sihuhu_Rail_TrackElement, gen_sihuhu_Switch_TrackElement, gen_sihuhu_SwitchConnection_Rail, gen_sihuhu_Train_NamedElement, gen_sihuhu_Signal_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)