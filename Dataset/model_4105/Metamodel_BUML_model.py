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
Concept_Segment = Class(name="Concept::Segment")
Trackelement = Class(name="Trackelement")
Concept_Trackelement = Class(name="Concept::Trackelement")
Thing = Class(name="Thing")
Concept_Sensor = Class(name="Concept::Sensor")
Concept_Switch = Class(name="Concept::Switch")
Concept_SwitchPosition = Class(name="Concept::SwitchPosition")
Concept_Route = Class(name="Concept::Route")
Concept_Signal = Class(name="Concept::Signal")
Concept_Thing = Class(name="Concept::Thing")
Concept_IndividualContainer = Class(name="Concept::IndividualContainer")

# Concept_Segment class attributes and methods
Concept_Segment_Segment_length: Property = Property(name="Segment_length", type=IntegerType)
Concept_Segment.attributes={Concept_Segment_Segment_length}

# Trackelement class attributes and methods

# Concept_Trackelement class attributes and methods

# Thing class attributes and methods

# Concept_Sensor class attributes and methods

# Concept_Switch class attributes and methods
Concept_Switch_Switch_actualState: Property = Property(name="Switch_actualState", type=StringType)
Concept_Switch.attributes={Concept_Switch_Switch_actualState}

# Concept_SwitchPosition class attributes and methods
Concept_SwitchPosition_SwitchPosition_switchState: Property = Property(name="SwitchPosition_switchState", type=StringType)
Concept_SwitchPosition.attributes={Concept_SwitchPosition_SwitchPosition_switchState}

# Concept_Route class attributes and methods

# Concept_Signal class attributes and methods
Concept_Signal_Signal_actualState: Property = Property(name="Signal_actualState", type=StringType)
Concept_Signal.attributes={Concept_Signal_Signal_actualState}

# Concept_Thing class attributes and methods

# Concept_IndividualContainer class attributes and methods

# Relationships
Route_routeDefinition10: BinaryAssociation = BinaryAssociation(
    name="Route_routeDefinition10",
    ends={
        Property(name="Concept_Sensor", type=Concept_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="Concept_Route11", type=Concept_Sensor, multiplicity=Multiplicity(2, 9999))
    }
)
SwitchPosition_switch12: BinaryAssociation = BinaryAssociation(
    name="SwitchPosition_switch12",
    ends={
        Property(name="Switch", type=Concept_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="Switch_switchPosition", type=Concept_Switch, multiplicity=Multiplicity(1, 1))
    }
)
TrackElement_sensor0: BinaryAssociation = BinaryAssociation(
    name="TrackElement_sensor0",
    ends={
        Property(name="Sensor", type=Concept_Trackelement, multiplicity=Multiplicity(1, 1)),
        Property(name="Sensor_trackElement", type=Concept_Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
TrackElement_connectsTo2: BinaryAssociation = BinaryAssociation(
    name="TrackElement_connectsTo2",
    ends={
        Property(name="Concept_Trackelement", type=Concept_Trackelement, multiplicity=Multiplicity(1, 1)),
        Property(name="Concept_Trackelement1", type=Concept_Trackelement, multiplicity=Multiplicity(0, 9999))
    }
)
Switch_switchPosition3: BinaryAssociation = BinaryAssociation(
    name="Switch_switchPosition3",
    ends={
        Property(name="SwitchPosition", type=Concept_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="SwitchPosition_switch", type=Concept_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
Route_entry4: BinaryAssociation = BinaryAssociation(
    name="Route_entry4",
    ends={
        Property(name="Concept_Signal", type=Concept_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="Concept_Route", type=Concept_Signal, multiplicity=Multiplicity(1, 1))
    }
)
Route_switchPosition5: BinaryAssociation = BinaryAssociation(
    name="Route_switchPosition5",
    ends={
        Property(name="SwitchPosition6", type=Concept_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="SwitchPosition_route", type=Concept_SwitchPosition, multiplicity=Multiplicity(0, 9999))
    }
)
Route_exit7: BinaryAssociation = BinaryAssociation(
    name="Route_exit7",
    ends={
        Property(name="Concept_Signal9", type=Concept_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="Concept_Route8", type=Concept_Signal, multiplicity=Multiplicity(1, 1))
    }
)
SwitchPosition_route13: BinaryAssociation = BinaryAssociation(
    name="SwitchPosition_route13",
    ends={
        Property(name="Route", type=Concept_SwitchPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="Route_switchPosition", type=Concept_Route, multiplicity=Multiplicity(1, 1))
    }
)
Sensor_trackElement14: BinaryAssociation = BinaryAssociation(
    name="Sensor_trackElement14",
    ends={
        Property(name="Trackelement", type=Concept_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="TrackElement_sensor", type=Concept_Trackelement, multiplicity=Multiplicity(0, 9999))
    }
)
contains15: BinaryAssociation = BinaryAssociation(
    name="contains15",
    ends={
        Property(name="Concept_Thing", type=Concept_IndividualContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Concept_IndividualContainer", type=Concept_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Concept_Signal_Thing = Generalization(general=Thing, specific=Concept_Signal)
gen_Concept_SwitchPosition_Thing = Generalization(general=Thing, specific=Concept_SwitchPosition)
gen_Concept_Segment_Trackelement = Generalization(general=Trackelement, specific=Concept_Segment)
gen_Concept_Trackelement_Thing = Generalization(general=Thing, specific=Concept_Trackelement)
gen_Concept_Switch_Trackelement = Generalization(general=Trackelement, specific=Concept_Switch)
gen_Concept_Route_Thing = Generalization(general=Thing, specific=Concept_Route)
gen_Concept_Sensor_Thing = Generalization(general=Thing, specific=Concept_Sensor)

# Domain Model
domain_model = DomainModel(
    name="Concept",
    types={Concept_Segment, Trackelement, Concept_Trackelement, Thing, Concept_Sensor, Concept_Switch, Concept_SwitchPosition, Concept_Route, Concept_Signal, Concept_Thing, Concept_IndividualContainer, SignalStateKind, SwitchStateKind},
    associations={Route_routeDefinition10, SwitchPosition_switch12, TrackElement_sensor0, TrackElement_connectsTo2, Switch_switchPosition3, Route_entry4, Route_switchPosition5, Route_exit7, SwitchPosition_route13, Sensor_trackElement14, contains15},
    generalizations={gen_Concept_Signal_Thing, gen_Concept_SwitchPosition_Thing, gen_Concept_Segment_Trackelement, gen_Concept_Trackelement_Thing, gen_Concept_Switch_Trackelement, gen_Concept_Route_Thing, gen_Concept_Sensor_Thing},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)