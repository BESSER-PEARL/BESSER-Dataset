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
Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="FAILURE"),
			EnumerationLiteral(name="STRAIGHT"),
			EnumerationLiteral(name="DIVERGING")
    }
)

Signal: Enumeration = Enumeration(
    name="Signal",
    literals={
            EnumerationLiteral(name="FAILURE"),
			EnumerationLiteral(name="STOP"),
			EnumerationLiteral(name="GO")
    }
)

# Classes
railway_Region = Class(name="railway::Region")
RailwayElement = Class(name="RailwayElement")
railway_Sensor = Class(name="railway::Sensor")
railway_TrackElement = Class(name="railway::TrackElement", is_abstract=True)
railway_SwitchPosition = Class(name="railway::SwitchPosition")
railway_Semaphore = Class(name="railway::Semaphore")
railway_RailwayElement = Class(name="railway::RailwayElement", is_abstract=True)
railway_RailwayContainer = Class(name="railway::RailwayContainer")
railway_Route = Class(name="railway::Route")
railway_Segment = Class(name="railway::Segment")
TrackElement = Class(name="TrackElement")
railway_Switch = Class(name="railway::Switch")

# railway_Region class attributes and methods

# RailwayElement class attributes and methods

# railway_Sensor class attributes and methods

# railway_TrackElement class attributes and methods

# railway_SwitchPosition class attributes and methods
railway_SwitchPosition_position: Property = Property(name="position", type=StringType)
railway_SwitchPosition.attributes={railway_SwitchPosition_position}

# railway_Semaphore class attributes and methods
railway_Semaphore_signal: Property = Property(name="signal", type=StringType)
railway_Semaphore.attributes={railway_Semaphore_signal}

# railway_RailwayElement class attributes and methods
railway_RailwayElement_id: Property = Property(name="id", type=IntegerType)
railway_RailwayElement.attributes={railway_RailwayElement_id}

# railway_RailwayContainer class attributes and methods

# railway_Route class attributes and methods
railway_Route_active: Property = Property(name="active", type=BooleanType)
railway_Route.attributes={railway_Route_active}

# railway_Segment class attributes and methods
railway_Segment_length: Property = Property(name="length", type=IntegerType)
railway_Segment.attributes={railway_Segment_length}

# TrackElement class attributes and methods

# railway_Switch class attributes and methods
railway_Switch_currentPosition: Property = Property(name="currentPosition", type=StringType)
railway_Switch.attributes={railway_Switch_currentPosition}

# Relationships
routes0: BinaryAssociation = BinaryAssociation(
    name="routes0",
    ends={
        Property(name="railway_RailwayContainer", type=railway_Route, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="railway_Route", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1))
    }
)
regions1: BinaryAssociation = BinaryAssociation(
    name="regions1",
    ends={
        Property(name="railway_Region", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer2", type=railway_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors3: BinaryAssociation = BinaryAssociation(
    name="sensors3",
    ends={
        Property(name="railway_Sensor", type=railway_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Region4", type=railway_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="railway_TrackElement", type=railway_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Region6", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
follows7: BinaryAssociation = BinaryAssociation(
    name="follows7",
    ends={
        Property(name="SwitchPosition", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="route", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires8: BinaryAssociation = BinaryAssociation(
    name="requires8",
    ends={
        Property(name="railway_Sensor10", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route9", type=railway_Sensor, multiplicity=Multiplicity(2, 9999))
    }
)
entry11: BinaryAssociation = BinaryAssociation(
    name="entry11",
    ends={
        Property(name="railway_Semaphore", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route12", type=railway_Semaphore, multiplicity=Multiplicity(0, 1))
    }
)
exit13: BinaryAssociation = BinaryAssociation(
    name="exit13",
    ends={
        Property(name="railway_Semaphore15", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route14", type=railway_Semaphore, multiplicity=Multiplicity(0, 1))
    }
)
monitors16: BinaryAssociation = BinaryAssociation(
    name="monitors16",
    ends={
        Property(name="TrackElement", type=railway_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="monitoredBy", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
monitoredBy17: BinaryAssociation = BinaryAssociation(
    name="monitoredBy17",
    ends={
        Property(name="Sensor", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="monitors", type=railway_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
route25: BinaryAssociation = BinaryAssociation(
    name="route25",
    ends={
        Property(name="Route", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="follows", type=railway_Route, multiplicity=Multiplicity(0, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="Switch", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=railway_Switch, multiplicity=Multiplicity(0, 1))
    }
)
connectsTo19: BinaryAssociation = BinaryAssociation(
    name="connectsTo19",
    ends={
        Property(name="railway_TrackElement20", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_TrackElement18", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
semaphores21: BinaryAssociation = BinaryAssociation(
    name="semaphores21",
    ends={
        Property(name="railway_Semaphore22", type=railway_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Segment", type=railway_Semaphore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions23: BinaryAssociation = BinaryAssociation(
    name="positions23",
    ends={
        Property(name="SwitchPosition24", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_railway_Region_RailwayElement = Generalization(general=RailwayElement, specific=railway_Region)
gen_railway_Route_RailwayElement = Generalization(general=RailwayElement, specific=railway_Route)
gen_railway_Sensor_RailwayElement = Generalization(general=RailwayElement, specific=railway_Sensor)
gen_railway_TrackElement_RailwayElement = Generalization(general=RailwayElement, specific=railway_TrackElement)
gen_railway_SwitchPosition_RailwayElement = Generalization(general=RailwayElement, specific=railway_SwitchPosition)
gen_railway_Semaphore_RailwayElement = Generalization(general=RailwayElement, specific=railway_Semaphore)
gen_railway_Segment_TrackElement = Generalization(general=TrackElement, specific=railway_Segment)
gen_railway_Switch_TrackElement = Generalization(general=TrackElement, specific=railway_Switch)

# Domain Model
domain_model = DomainModel(
    name="railway",
    types={railway_Region, RailwayElement, railway_Sensor, railway_TrackElement, railway_SwitchPosition, railway_Semaphore, railway_RailwayElement, railway_RailwayContainer, railway_Route, railway_Segment, TrackElement, railway_Switch, Position, Signal},
    associations={routes0, regions1, sensors3, elements5, follows7, requires8, entry11, exit13, monitors16, monitoredBy17, route25, target26, connectsTo19, semaphores21, positions23},
    generalizations={gen_railway_Region_RailwayElement, gen_railway_Route_RailwayElement, gen_railway_Sensor_RailwayElement, gen_railway_TrackElement_RailwayElement, gen_railway_SwitchPosition_RailwayElement, gen_railway_Semaphore_RailwayElement, gen_railway_Segment_TrackElement, gen_railway_Switch_TrackElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)