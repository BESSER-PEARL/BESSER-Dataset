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
Signal: Enumeration = Enumeration(
    name="Signal",
    literals={
            EnumerationLiteral(name="FAILURE"),
			EnumerationLiteral(name="STOP"),
			EnumerationLiteral(name="GO")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="FAILURE"),
			EnumerationLiteral(name="STRAIGHT"),
			EnumerationLiteral(name="DIVERGING")
    }
)

# Classes
railway_TrackElement = Class(name="railway::TrackElement", is_abstract=True)
RailwayElement = Class(name="RailwayElement")
railway_Sensor = Class(name="railway::Sensor")
railway_Switch = Class(name="railway::Switch")
railway_SwitchPosition = Class(name="railway::SwitchPosition")
railway_Segment = Class(name="railway::Segment")
TrackElement = Class(name="TrackElement")
railway_Semaphore = Class(name="railway::Semaphore")
railway_RailwayContainer = Class(name="railway::RailwayContainer")
railway_Region = Class(name="railway::Region")
railway_Route = Class(name="railway::Route")
railway_RailwayElement = Class(name="railway::RailwayElement", is_abstract=True)

# railway_TrackElement class attributes and methods

# RailwayElement class attributes and methods

# railway_Sensor class attributes and methods

# railway_Switch class attributes and methods
railway_Switch_currentPosition: Property = Property(name="currentPosition", type=StringType)
railway_Switch.attributes={railway_Switch_currentPosition}

# railway_SwitchPosition class attributes and methods
railway_SwitchPosition_position: Property = Property(name="position", type=StringType)
railway_SwitchPosition.attributes={railway_SwitchPosition_position}

# railway_Segment class attributes and methods
railway_Segment_length: Property = Property(name="length", type=IntegerType)
railway_Segment.attributes={railway_Segment_length}

# TrackElement class attributes and methods

# railway_Semaphore class attributes and methods
railway_Semaphore_signal: Property = Property(name="signal", type=StringType)
railway_Semaphore.attributes={railway_Semaphore_signal}

# railway_RailwayContainer class attributes and methods

# railway_Region class attributes and methods

# railway_Route class attributes and methods

# railway_RailwayElement class attributes and methods
railway_RailwayElement__id: Property = Property(name="_id", type=IntegerType)
railway_RailwayElement.attributes={railway_RailwayElement__id}

# Relationships
semaphores0: BinaryAssociation = BinaryAssociation(
    name="semaphores0",
    ends={
        Property(name="railway_Segment", type=railway_Semaphore, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="railway_Semaphore", type=railway_Segment, multiplicity=Multiplicity(1, 1))
    }
)
neighbors1: BinaryAssociation = BinaryAssociation(
    name="neighbors1",
    ends={
        Property(name="railway_TrackElement", type=railway_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Segment2", type=railway_TrackElement, multiplicity=Multiplicity(2, 2))
    }
)
monitoredBy3: BinaryAssociation = BinaryAssociation(
    name="monitoredBy3",
    ends={
        Property(name="Sensor", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="monitors", type=railway_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
connectsTo5: BinaryAssociation = BinaryAssociation(
    name="connectsTo5",
    ends={
        Property(name="railway_TrackElement6", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_TrackElement4", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
positions7: BinaryAssociation = BinaryAssociation(
    name="positions7",
    ends={
        Property(name="SwitchPosition", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="railway_TrackElement9", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Switch", type=railway_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="railway_TrackElement12", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Switch11", type=railway_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
from13: BinaryAssociation = BinaryAssociation(
    name="from13",
    ends={
        Property(name="railway_TrackElement15", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Switch14", type=railway_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
monitors27: BinaryAssociation = BinaryAssociation(
    name="monitors27",
    ends={
        Property(name="TrackElement", type=railway_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="monitoredBy", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
routes28: BinaryAssociation = BinaryAssociation(
    name="routes28",
    ends={
        Property(name="railway_Route29", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer", type=railway_Route, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions30: BinaryAssociation = BinaryAssociation(
    name="regions30",
    ends={
        Property(name="railway_Region", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer31", type=railway_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements32: BinaryAssociation = BinaryAssociation(
    name="elements32",
    ends={
        Property(name="railway_TrackElement34", type=railway_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Region33", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors35: BinaryAssociation = BinaryAssociation(
    name="sensors35",
    ends={
        Property(name="railway_Sensor37", type=railway_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Region36", type=railway_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry16: BinaryAssociation = BinaryAssociation(
    name="entry16",
    ends={
        Property(name="railway_Semaphore17", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route", type=railway_Semaphore, multiplicity=Multiplicity(1, 1))
    }
)
follows18: BinaryAssociation = BinaryAssociation(
    name="follows18",
    ends={
        Property(name="SwitchPosition19", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="route", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit20: BinaryAssociation = BinaryAssociation(
    name="exit20",
    ends={
        Property(name="railway_Semaphore22", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route21", type=railway_Semaphore, multiplicity=Multiplicity(1, 1))
    }
)
gathers23: BinaryAssociation = BinaryAssociation(
    name="gathers23",
    ends={
        Property(name="railway_Sensor", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route24", type=railway_Sensor, multiplicity=Multiplicity(2, 9999))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="Switch", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=railway_Switch, multiplicity=Multiplicity(1, 1))
    }
)
route26: BinaryAssociation = BinaryAssociation(
    name="route26",
    ends={
        Property(name="Route", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="follows", type=railway_Route, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_railway_TrackElement_RailwayElement = Generalization(general=RailwayElement, specific=railway_TrackElement)
gen_railway_Switch_TrackElement = Generalization(general=TrackElement, specific=railway_Switch)
gen_railway_Segment_TrackElement = Generalization(general=TrackElement, specific=railway_Segment)
gen_railway_Region_RailwayElement = Generalization(general=RailwayElement, specific=railway_Region)
gen_railway_Route_RailwayElement = Generalization(general=RailwayElement, specific=railway_Route)
gen_railway_Semaphore_RailwayElement = Generalization(general=RailwayElement, specific=railway_Semaphore)
gen_railway_SwitchPosition_RailwayElement = Generalization(general=RailwayElement, specific=railway_SwitchPosition)
gen_railway_Sensor_RailwayElement = Generalization(general=RailwayElement, specific=railway_Sensor)

# Domain Model
domain_model = DomainModel(
    name="railway",
    types={railway_TrackElement, RailwayElement, railway_Sensor, railway_Switch, railway_SwitchPosition, railway_Segment, TrackElement, railway_Semaphore, railway_RailwayContainer, railway_Region, railway_Route, railway_RailwayElement, Signal, Position},
    associations={semaphores0, neighbors1, monitoredBy3, connectsTo5, positions7, left8, right10, from13, monitors27, routes28, regions30, elements32, sensors35, entry16, follows18, exit20, gathers23, target25, route26},
    generalizations={gen_railway_TrackElement_RailwayElement, gen_railway_Switch_TrackElement, gen_railway_Segment_TrackElement, gen_railway_Region_RailwayElement, gen_railway_Route_RailwayElement, gen_railway_Semaphore_RailwayElement, gen_railway_SwitchPosition_RailwayElement, gen_railway_Sensor_RailwayElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)