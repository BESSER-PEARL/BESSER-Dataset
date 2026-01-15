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
            EnumerationLiteral(name="Failure"),
			EnumerationLiteral(name="STOP"),
			EnumerationLiteral(name="Go")
    }
)

# Classes
Train5_RailwayDiagram = Class(name="Train5::RailwayDiagram")
Train5_NamedElement = Class(name="Train5::NamedElement", is_abstract=True)
Train5_TrackElement = Class(name="Train5::TrackElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
Train5_Route = Class(name="Train5::Route")
Train5_RoutePart = Class(name="Train5::RoutePart")
Train5_Switch = Class(name="Train5::Switch")
TrackElement = Class(name="TrackElement")
Train5_Segment = Class(name="Train5::Segment")
Train5_Station = Class(name="Train5::Station")
Train5_SensorNetwork = Class(name="Train5::SensorNetwork")

# Train5_RailwayDiagram class attributes and methods

# Train5_NamedElement class attributes and methods
Train5_NamedElement_id: Property = Property(name="id", type=StringType)
Train5_NamedElement.attributes={Train5_NamedElement_id}

# Train5_TrackElement class attributes and methods
Train5_TrackElement_State: Property = Property(name="State", type=StringType)
Train5_TrackElement_length: Property = Property(name="length", type=StringType)
Train5_TrackElement.attributes={Train5_TrackElement_length, Train5_TrackElement_State}

# NamedElement class attributes and methods

# Train5_Route class attributes and methods
Train5_Route_currentIndex: Property = Property(name="currentIndex", type=StringType)
Train5_Route_speed: Property = Property(name="speed", type=StringType)
Train5_Route_leftOver: Property = Property(name="leftOver", type=StringType)
Train5_Route.attributes={Train5_Route_speed, Train5_Route_currentIndex, Train5_Route_leftOver}

# Train5_RoutePart class attributes and methods

# Train5_Switch class attributes and methods

# TrackElement class attributes and methods

# Train5_Segment class attributes and methods

# Train5_Station class attributes and methods

# Train5_SensorNetwork class attributes and methods

# Relationships
sensors4: BinaryAssociation = BinaryAssociation(
    name="sensors4",
    ends={
        Property(name="Train5_Switch5", type=Train5_SensorNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_SensorNetwork", type=Train5_Switch, multiplicity=Multiplicity(0, 9999))
    }
)
train0: BinaryAssociation = BinaryAssociation(
    name="train0",
    ends={
        Property(name="Train5_Route", type=Train5_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_TrackElement", type=Train5_Route, multiplicity=Multiplicity(0, 1))
    }
)
route1: BinaryAssociation = BinaryAssociation(
    name="route1",
    ends={
        Property(name="Train5_RoutePart", type=Train5_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_Route2", type=Train5_RoutePart, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
neighbour3: BinaryAssociation = BinaryAssociation(
    name="neighbour3",
    ends={
        Property(name="Train5_Segment", type=Train5_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_Switch", type=Train5_Segment, multiplicity=Multiplicity(2, 9999))
    }
)
trackelements6: BinaryAssociation = BinaryAssociation(
    name="trackelements6",
    ends={
        Property(name="Train5_TrackElement7", type=Train5_RailwayDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RailwayDiagram", type=Train5_TrackElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors8: BinaryAssociation = BinaryAssociation(
    name="sensors8",
    ends={
        Property(name="Train5_SensorNetwork10", type=Train5_RailwayDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RailwayDiagram9", type=Train5_SensorNetwork, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
routes11: BinaryAssociation = BinaryAssociation(
    name="routes11",
    ends={
        Property(name="Train5_Route13", type=Train5_RailwayDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RailwayDiagram12", type=Train5_Route, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next15: BinaryAssociation = BinaryAssociation(
    name="next15",
    ends={
        Property(name="Train5_RoutePart16", type=Train5_RoutePart, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RoutePart14", type=Train5_RoutePart, multiplicity=Multiplicity(0, 1))
    }
)
element17: BinaryAssociation = BinaryAssociation(
    name="element17",
    ends={
        Property(name="Train5_TrackElement19", type=Train5_RoutePart, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RoutePart18", type=Train5_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
previous21: BinaryAssociation = BinaryAssociation(
    name="previous21",
    ends={
        Property(name="Train5_RoutePart22", type=Train5_RoutePart, multiplicity=Multiplicity(1, 1)),
        Property(name="Train5_RoutePart20", type=Train5_RoutePart, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Train5_TrackElement_NamedElement = Generalization(general=NamedElement, specific=Train5_TrackElement)
gen_Train5_Route_NamedElement = Generalization(general=NamedElement, specific=Train5_Route)
gen_Train5_Switch_TrackElement = Generalization(general=TrackElement, specific=Train5_Switch)
gen_Train5_Segment_TrackElement = Generalization(general=TrackElement, specific=Train5_Segment)
gen_Train5_Station_TrackElement = Generalization(general=TrackElement, specific=Train5_Station)
gen_Train5_SensorNetwork_NamedElement = Generalization(general=NamedElement, specific=Train5_SensorNetwork)
gen_Train5_RoutePart_NamedElement = Generalization(general=NamedElement, specific=Train5_RoutePart)

# Domain Model
domain_model = DomainModel(
    name="Train5",
    types={Train5_RailwayDiagram, Train5_NamedElement, Train5_TrackElement, NamedElement, Train5_Route, Train5_RoutePart, Train5_Switch, TrackElement, Train5_Segment, Train5_Station, Train5_SensorNetwork, Signal},
    associations={sensors4, train0, route1, neighbour3, trackelements6, sensors8, routes11, next15, element17, previous21},
    generalizations={gen_Train5_TrackElement_NamedElement, gen_Train5_Route_NamedElement, gen_Train5_Switch_TrackElement, gen_Train5_Segment_TrackElement, gen_Train5_Station_TrackElement, gen_Train5_SensorNetwork_NamedElement, gen_Train5_RoutePart_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)