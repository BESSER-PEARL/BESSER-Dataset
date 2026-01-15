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
SignalStateKind: Enumeration = Enumeration(
    name="SignalStateKind",
    literals={
            EnumerationLiteral(name="SignalStateKind_STOP"),
			EnumerationLiteral(name="SignalStateKind_FAILURE"),
			EnumerationLiteral(name="SignalStateKind_GO")
    }
)

SwitchStateKind: Enumeration = Enumeration(
    name="SwitchStateKind",
    literals={
            EnumerationLiteral(name="PointStateKind_FAILURE"),
			EnumerationLiteral(name="PointStateKind_LEFT"),
			EnumerationLiteral(name="PointStateKind_RIGHT"),
			EnumerationLiteral(name="PointStateKind_STRAIGHT")
    }
)

# Classes
ConceptASE_Trackelement = Class(name="ConceptASE::Trackelement")
Thing = Class(name="Thing")
ConceptASE_Segment = Class(name="ConceptASE::Segment")
Trackelement = Class(name="Trackelement")
ConceptASE_Thing = Class(name="ConceptASE::Thing")
ConceptASE_Sensor = Class(name="ConceptASE::Sensor")
ConceptASE_Switch = Class(name="ConceptASE::Switch")
ConceptASE_SwitchPosition = Class(name="ConceptASE::SwitchPosition")
ConceptASE_Route = Class(name="ConceptASE::Route")
ConceptASE_Signal = Class(name="ConceptASE::Signal")
ConceptASE_IndividualContainer = Class(name="ConceptASE::IndividualContainer")

# ConceptASE_Trackelement class attributes and methods

# Thing class attributes and methods

# ConceptASE_Segment class attributes and methods
ConceptASE_Segment_Segment_height: Property = Property(name="Segment_height", type=IntegerType)
ConceptASE_Segment_Segment_length: Property = Property(name="Segment_length", type=IntegerType)
ConceptASE_Segment.attributes={ConceptASE_Segment_Segment_length, ConceptASE_Segment_Segment_height}

# Trackelement class attributes and methods

# ConceptASE_Thing class attributes and methods

# ConceptASE_Sensor class attributes and methods
ConceptASE_Sensor_Sensor_year: Property = Property(name="Sensor_year", type=IntegerType)
ConceptASE_Sensor.attributes={ConceptASE_Sensor_Sensor_year}

# ConceptASE_Switch class attributes and methods
ConceptASE_Switch_Switch_actualState: Property = Property(name="Switch_actualState", type=StringType)
ConceptASE_Switch.attributes={ConceptASE_Switch_Switch_actualState}

# ConceptASE_SwitchPosition class attributes and methods
ConceptASE_SwitchPosition_SwitchPosition_switchState: Property = Property(name="SwitchPosition_switchState", type=StringType)
ConceptASE_SwitchPosition.attributes={ConceptASE_SwitchPosition_SwitchPosition_switchState}

# ConceptASE_Route class attributes and methods

# ConceptASE_Signal class attributes and methods
ConceptASE_Signal_Signal_actualState: Property = Property(name="Signal_actualState", type=StringType)
ConceptASE_Signal.attributes={ConceptASE_Signal_Signal_actualState}

# ConceptASE_IndividualContainer class attributes and methods

# Relationships
TrackElement_sensor0: BinaryAssociation = BinaryAssociation(
    name="TrackElement_sensor0",
    ends={
        Property(name="Sensor", type=ConceptASE_Trackelement, multiplicity=Multiplicity(1, 1)),
        Property(name="Sensor_trackElement", type=ConceptASE_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
TrackElement_connectsTo2: BinaryAssociation = BinaryAssociation(
    name="TrackElement_connectsTo2",
    ends={
        Property(name="ConceptASE_Trackelement", type=ConceptASE_Trackelement, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptASE_Trackelement1", type=ConceptASE_Trackelement, multiplicity=Multiplicity(0, 9999))
    }
)
Switch_switchPosition3: BinaryAssociation = BinaryAssociation(
    name="Switch_switchPosition3",
    ends={
        Property(name="SwitchPosition", type=ConceptASE_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="SwitchPosition_switch", type=ConceptASE_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
Route_entry4: BinaryAssociation = BinaryAssociation(
    name="Route_entry4",
    ends={
        Property(name="ConceptASE_Signal", type=ConceptASE_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptASE_Route", type=ConceptASE_Signal, multiplicity=Multiplicity(1, 1))
    }
)
Route_switchPosition5: BinaryAssociation = BinaryAssociation(
    name="Route_switchPosition5",
    ends={
        Property(name="SwitchPosition6", type=ConceptASE_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="SwitchPosition_route", type=ConceptASE_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
Route_exit7: BinaryAssociation = BinaryAssociation(
    name="Route_exit7",
    ends={
        Property(name="ConceptASE_Signal9", type=ConceptASE_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptASE_Route8", type=ConceptASE_Signal, multiplicity=Multiplicity(1, 1))
    }
)
Route_routeDefinition10: BinaryAssociation = BinaryAssociation(
    name="Route_routeDefinition10",
    ends={
        Property(name="ConceptASE_Sensor", type=ConceptASE_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptASE_Route11", type=ConceptASE_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
SwitchPosition_switch12: BinaryAssociation = BinaryAssociation(
    name="SwitchPosition_switch12",
    ends={
        Property(name="Switch", type=ConceptASE_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="Switch_switchPosition", type=ConceptASE_Switch, multiplicity=Multiplicity(0, 9999))
    }
)
SwitchPosition_route13: BinaryAssociation = BinaryAssociation(
    name="SwitchPosition_route13",
    ends={
        Property(name="Route", type=ConceptASE_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="Route_switchPosition", type=ConceptASE_Route, multiplicity=Multiplicity(0, 9999))
    }
)
Sensor_trackElement14: BinaryAssociation = BinaryAssociation(
    name="Sensor_trackElement14",
    ends={
        Property(name="Trackelement", type=ConceptASE_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="TrackElement_sensor", type=ConceptASE_Trackelement, multiplicity=Multiplicity(0, 9999))
    }
)
contains15: BinaryAssociation = BinaryAssociation(
    name="contains15",
    ends={
        Property(name="ConceptASE_Thing", type=ConceptASE_IndividualContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ConceptASE_IndividualContainer", type=ConceptASE_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ConceptASE_Trackelement_Thing = Generalization(general=Thing, specific=ConceptASE_Trackelement)
gen_ConceptASE_Segment_Trackelement = Generalization(general=Trackelement, specific=ConceptASE_Segment)
gen_ConceptASE_Sensor_Thing = Generalization(general=Thing, specific=ConceptASE_Sensor)
gen_ConceptASE_Switch_Trackelement = Generalization(general=Trackelement, specific=ConceptASE_Switch)
gen_ConceptASE_Route_Thing = Generalization(general=Thing, specific=ConceptASE_Route)
gen_ConceptASE_Signal_Thing = Generalization(general=Thing, specific=ConceptASE_Signal)
gen_ConceptASE_SwitchPosition_Thing = Generalization(general=Thing, specific=ConceptASE_SwitchPosition)

# Domain Model
domain_model = DomainModel(
    name="ConceptASE",
    types={ConceptASE_Trackelement, Thing, ConceptASE_Segment, Trackelement, ConceptASE_Thing, ConceptASE_Sensor, ConceptASE_Switch, ConceptASE_SwitchPosition, ConceptASE_Route, ConceptASE_Signal, ConceptASE_IndividualContainer, SignalStateKind, SwitchStateKind},
    associations={TrackElement_sensor0, TrackElement_connectsTo2, Switch_switchPosition3, Route_entry4, Route_switchPosition5, Route_exit7, Route_routeDefinition10, SwitchPosition_switch12, SwitchPosition_route13, Sensor_trackElement14, contains15},
    generalizations={gen_ConceptASE_Trackelement_Thing, gen_ConceptASE_Segment_Trackelement, gen_ConceptASE_Sensor_Thing, gen_ConceptASE_Switch_Trackelement, gen_ConceptASE_Route_Thing, gen_ConceptASE_Signal_Thing, gen_ConceptASE_SwitchPosition_Thing},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)