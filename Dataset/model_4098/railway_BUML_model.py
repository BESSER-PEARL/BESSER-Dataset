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
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="STRAIGHT")
    }
)

# Classes
railway_TrackElement = Class(name="railway::TrackElement", is_abstract=True)
RailwayElement = Class(name="RailwayElement")
railway_Sensor = Class(name="railway::Sensor")
railway_Switch = Class(name="railway::Switch")
railway_SwitchPosition = Class(name="railway::SwitchPosition")
railway_Route = Class(name="railway::Route")
railway_Semaphore = Class(name="railway::Semaphore")
railway_RailwayElement = Class(name="railway::RailwayElement", is_abstract=True)
railway_Segment = Class(name="railway::Segment")
TrackElement = Class(name="TrackElement")
railway_RailwayContainer = Class(name="railway::RailwayContainer")

# railway_TrackElement class attributes and methods

# RailwayElement class attributes and methods

# railway_Sensor class attributes and methods

# railway_Switch class attributes and methods
railway_Switch_currentPosition: Property = Property(name="currentPosition", type=StringType)
railway_Switch.attributes={railway_Switch_currentPosition}

# railway_SwitchPosition class attributes and methods
railway_SwitchPosition_position: Property = Property(name="position", type=StringType)
railway_SwitchPosition.attributes={railway_SwitchPosition_position}

# railway_Route class attributes and methods

# railway_Semaphore class attributes and methods
railway_Semaphore_signal: Property = Property(name="signal", type=StringType)
railway_Semaphore.attributes={railway_Semaphore_signal}

# railway_RailwayElement class attributes and methods
railway_RailwayElement_id: Property = Property(name="id", type=IntegerType)
railway_RailwayElement.attributes={railway_RailwayElement_id}

# railway_Segment class attributes and methods
railway_Segment_length: Property = Property(name="length", type=IntegerType)
railway_Segment.attributes={railway_Segment_length}

# TrackElement class attributes and methods

# railway_RailwayContainer class attributes and methods

# Relationships
sensor0: BinaryAssociation = BinaryAssociation(
    name="sensor0",
    ends={
        Property(name="Sensor", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=railway_Sensor, multiplicity=Multiplicity(0, 1))
    }
)
connectsTo2: BinaryAssociation = BinaryAssociation(
    name="connectsTo2",
    ends={
        Property(name="railway_TrackElement", type=railway_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_TrackElement1", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999))
    }
)
positions3: BinaryAssociation = BinaryAssociation(
    name="positions3",
    ends={
        Property(name="SwitchPosition", type=railway_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="switch", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
entry4: BinaryAssociation = BinaryAssociation(
    name="entry4",
    ends={
        Property(name="railway_Semaphore", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route", type=railway_Semaphore, multiplicity=Multiplicity(1, 1))
    }
)
follows5: BinaryAssociation = BinaryAssociation(
    name="follows5",
    ends={
        Property(name="SwitchPosition6", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="route", type=railway_SwitchPosition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit7: BinaryAssociation = BinaryAssociation(
    name="exit7",
    ends={
        Property(name="railway_Semaphore9", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route8", type=railway_Semaphore, multiplicity=Multiplicity(1, 1))
    }
)
definedBy10: BinaryAssociation = BinaryAssociation(
    name="definedBy10",
    ends={
        Property(name="railway_Sensor", type=railway_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_Route11", type=railway_Sensor, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
switch12: BinaryAssociation = BinaryAssociation(
    name="switch12",
    ends={
        Property(name="Switch", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="positions", type=railway_Switch, multiplicity=Multiplicity(1, 1))
    }
)
route13: BinaryAssociation = BinaryAssociation(
    name="route13",
    ends={
        Property(name="Route", type=railway_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="follows", type=railway_Route, multiplicity=Multiplicity(1, 1))
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="TrackElement", type=railway_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor", type=railway_TrackElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semaphores16: BinaryAssociation = BinaryAssociation(
    name="semaphores16",
    ends={
        Property(name="railway_Semaphore18", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer17", type=railway_Semaphore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
routes19: BinaryAssociation = BinaryAssociation(
    name="routes19",
    ends={
        Property(name="railway_Route21", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer20", type=railway_Route, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invalids15: BinaryAssociation = BinaryAssociation(
    name="invalids15",
    ends={
        Property(name="railway_RailwayElement", type=railway_RailwayContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="railway_RailwayContainer", type=railway_RailwayElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_railway_TrackElement_RailwayElement = Generalization(general=RailwayElement, specific=railway_TrackElement)
gen_railway_Switch_TrackElement = Generalization(general=TrackElement, specific=railway_Switch)
gen_railway_Route_RailwayElement = Generalization(general=RailwayElement, specific=railway_Route)
gen_railway_Semaphore_RailwayElement = Generalization(general=RailwayElement, specific=railway_Semaphore)
gen_railway_SwitchPosition_RailwayElement = Generalization(general=RailwayElement, specific=railway_SwitchPosition)
gen_railway_Sensor_RailwayElement = Generalization(general=RailwayElement, specific=railway_Sensor)
gen_railway_Segment_TrackElement = Generalization(general=TrackElement, specific=railway_Segment)

# Domain Model
domain_model = DomainModel(
    name="railway",
    types={railway_TrackElement, RailwayElement, railway_Sensor, railway_Switch, railway_SwitchPosition, railway_Route, railway_Semaphore, railway_RailwayElement, railway_Segment, TrackElement, railway_RailwayContainer, Signal, Position},
    associations={sensor0, connectsTo2, positions3, entry4, follows5, exit7, definedBy10, switch12, route13, elements14, semaphores16, routes19, invalids15},
    generalizations={gen_railway_TrackElement_RailwayElement, gen_railway_Switch_TrackElement, gen_railway_Route_RailwayElement, gen_railway_Semaphore_RailwayElement, gen_railway_SwitchPosition_RailwayElement, gen_railway_Sensor_RailwayElement, gen_railway_Segment_TrackElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)