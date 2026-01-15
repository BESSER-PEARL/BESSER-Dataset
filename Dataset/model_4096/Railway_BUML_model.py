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
Speed: Enumeration = Enumeration(
    name="Speed",
    literals={
            EnumerationLiteral(name="ZERO"),
			EnumerationLiteral(name="TWENTY"),
			EnumerationLiteral(name="FOURTY"),
			EnumerationLiteral(name="SIXTY")
    }
)

TurnoutDirection: Enumeration = Enumeration(
    name="TurnoutDirection",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="STRAIGHT")
    }
)

ConnectionDirection: Enumeration = Enumeration(
    name="ConnectionDirection",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="STRAIGHT"),
			EnumerationLiteral(name="TOP")
    }
)

# Classes
RDM_RailwayDomainModel = Class(name="RDM::RailwayDomainModel")
RDM_Train = Class(name="RDM::Train")
RDM_TrackElement = Class(name="RDM::TrackElement", is_abstract=True)
RDM_Section = Class(name="RDM::Section")
RDM_Turnout = Class(name="RDM::Turnout")
RDM_ConnectionPoint = Class(name="RDM::ConnectionPoint")
RDM_Signal = Class(name="RDM::Signal")
RDM_TurnoutDesiredDirection = Class(name="RDM::TurnoutDesiredDirection")
RDM_Route = Class(name="RDM::Route")
RDM_RouteElement = Class(name="RDM::RouteElement")
RDMElement = Class(name="RDMElement")
RDM_Station = Class(name="RDM::Station")
RDM_RDMElement = Class(name="RDM::RDMElement", is_abstract=True)
TrackElement = Class(name="TrackElement")
Section = Class(name="Section")
RDM_TurnoutSignal = Class(name="RDM::TurnoutSignal")
Signal = Class(name="Signal")

# RDM_RailwayDomainModel class attributes and methods

# RDM_Train class attributes and methods
RDM_Train_headingSpeed: Property = Property(name="headingSpeed", type=StringType)
RDM_Train_maxSpeed: Property = Property(name="maxSpeed", type=StringType)
RDM_Train.attributes={RDM_Train_maxSpeed, RDM_Train_headingSpeed}

# RDM_TrackElement class attributes and methods

# RDM_Section class attributes and methods

# RDM_Turnout class attributes and methods
RDM_Turnout_currentDirection: Property = Property(name="currentDirection", type=StringType)
RDM_Turnout_switchingDirection: Property = Property(name="switchingDirection", type=StringType)
RDM_Turnout.attributes={RDM_Turnout_currentDirection, RDM_Turnout_switchingDirection}

# RDM_ConnectionPoint class attributes and methods
RDM_ConnectionPoint_direction: Property = Property(name="direction", type=StringType)
RDM_ConnectionPoint.attributes={RDM_ConnectionPoint_direction}

# RDM_Signal class attributes and methods
RDM_Signal_allowedSpeed: Property = Property(name="allowedSpeed", type=StringType)
RDM_Signal.attributes={RDM_Signal_allowedSpeed}

# RDM_TurnoutDesiredDirection class attributes and methods
RDM_TurnoutDesiredDirection_desiredDirection: Property = Property(name="desiredDirection", type=StringType)
RDM_TurnoutDesiredDirection.attributes={RDM_TurnoutDesiredDirection_desiredDirection}

# RDM_Route class attributes and methods

# RDM_RouteElement class attributes and methods

# RDMElement class attributes and methods

# RDM_Station class attributes and methods

# RDM_RDMElement class attributes and methods
RDM_RDMElement_name: Property = Property(name="name", type=StringType)
RDM_RDMElement_length: Property = Property(name="length", type=IntegerType)
RDM_RDMElement.attributes={RDM_RDMElement_length, RDM_RDMElement_name}

# TrackElement class attributes and methods

# Section class attributes and methods

# RDM_TurnoutSignal class attributes and methods

# Signal class attributes and methods

# Relationships
trains0: BinaryAssociation = BinaryAssociation(
    name="trains0",
    ends={
        Property(name="RDM_Train", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel", type=RDM_Train, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
departuresFrom17: BinaryAssociation = BinaryAssociation(
    name="departuresFrom17",
    ends={
        Property(name="RDM_Station19", type=RDM_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_Train18", type=RDM_Station, multiplicity=Multiplicity(1, 1))
    }
)
follows20: BinaryAssociation = BinaryAssociation(
    name="follows20",
    ends={
        Property(name="RDM_Route22", type=RDM_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_Train21", type=RDM_Route, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
standsOn23: BinaryAssociation = BinaryAssociation(
    name="standsOn23",
    ends={
        Property(name="TrackElement", type=RDM_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="occupiedBy", type=RDM_TrackElement, multiplicity=Multiplicity(1, 2))
    }
)
standsOn24: BinaryAssociation = BinaryAssociation(
    name="standsOn24",
    ends={
        Property(name="ConnectionPoint", type=RDM_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="holds", type=RDM_ConnectionPoint, multiplicity=Multiplicity(0, 1))
    }
)
observes25: BinaryAssociation = BinaryAssociation(
    name="observes25",
    ends={
        Property(name="RDM_TrackElement", type=RDM_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_Signal26", type=RDM_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
connectsTo27: BinaryAssociation = BinaryAssociation(
    name="connectsTo27",
    ends={
        Property(name="RDM_ConnectionPoint29", type=RDM_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_TrackElement28", type=RDM_ConnectionPoint, multiplicity=Multiplicity(1, 3), is_composite=True)
    }
)
sections1: BinaryAssociation = BinaryAssociation(
    name="sections1",
    ends={
        Property(name="RDM_Section", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel2", type=RDM_Section, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
turnouts3: BinaryAssociation = BinaryAssociation(
    name="turnouts3",
    ends={
        Property(name="RDM_Turnout", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel4", type=RDM_Turnout, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
editorCP5: BinaryAssociation = BinaryAssociation(
    name="editorCP5",
    ends={
        Property(name="RDM_ConnectionPoint", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel6", type=RDM_ConnectionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editorSignal7: BinaryAssociation = BinaryAssociation(
    name="editorSignal7",
    ends={
        Property(name="RDM_Signal", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel8", type=RDM_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editorTDD9: BinaryAssociation = BinaryAssociation(
    name="editorTDD9",
    ends={
        Property(name="RDM_TurnoutDesiredDirection", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel10", type=RDM_TurnoutDesiredDirection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editorRoute11: BinaryAssociation = BinaryAssociation(
    name="editorRoute11",
    ends={
        Property(name="RDM_Route", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel12", type=RDM_Route, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editorRouteElement13: BinaryAssociation = BinaryAssociation(
    name="editorRouteElement13",
    ends={
        Property(name="RDM_RouteElement", type=RDM_RailwayDomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RailwayDomainModel14", type=RDM_RouteElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrivesTo15: BinaryAssociation = BinaryAssociation(
    name="arrivesTo15",
    ends={
        Property(name="RDM_Station", type=RDM_Train, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_Train16", type=RDM_Station, multiplicity=Multiplicity(1, 1))
    }
)
controls37: BinaryAssociation = BinaryAssociation(
    name="controls37",
    ends={
        Property(name="RDM_Signal39", type=RDM_Station, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_Station38", type=RDM_Signal, multiplicity=Multiplicity(1, 2))
    }
)
holds40: BinaryAssociation = BinaryAssociation(
    name="holds40",
    ends={
        Property(name="Signal", type=RDM_ConnectionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="standsOn41", type=RDM_Signal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
occupiedBy30: BinaryAssociation = BinaryAssociation(
    name="occupiedBy30",
    ends={
        Property(name="Train", type=RDM_TrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="standsOn", type=RDM_Train, multiplicity=Multiplicity(0, 1))
    }
)
nextElement42: BinaryAssociation = BinaryAssociation(
    name="nextElement42",
    ends={
        Property(name="RDM_TrackElement44", type=RDM_ConnectionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_ConnectionPoint43", type=RDM_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
firstElement31: BinaryAssociation = BinaryAssociation(
    name="firstElement31",
    ends={
        Property(name="RouteElement", type=RDM_Route, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsTo", type=RDM_RouteElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredTurnout32: BinaryAssociation = BinaryAssociation(
    name="referredTurnout32",
    ends={
        Property(name="RDM_Turnout34", type=RDM_TurnoutDesiredDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_TurnoutDesiredDirection33", type=RDM_Turnout, multiplicity=Multiplicity(1, 1))
    }
)
routeElement35: BinaryAssociation = BinaryAssociation(
    name="routeElement35",
    ends={
        Property(name="RouteElement36", type=RDM_TurnoutDesiredDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="desiredDirection", type=RDM_RouteElement, multiplicity=Multiplicity(0, 1))
    }
)
referredElement45: BinaryAssociation = BinaryAssociation(
    name="referredElement45",
    ends={
        Property(name="RDM_TrackElement47", type=RDM_RouteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RouteElement46", type=RDM_TrackElement, multiplicity=Multiplicity(1, 1))
    }
)
desiredDirection48: BinaryAssociation = BinaryAssociation(
    name="desiredDirection48",
    ends={
        Property(name="TurnoutDesiredDirection", type=RDM_RouteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="routeElement", type=RDM_TurnoutDesiredDirection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
belongsTo49: BinaryAssociation = BinaryAssociation(
    name="belongsTo49",
    ends={
        Property(name="Route", type=RDM_RouteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="firstElement", type=RDM_Route, multiplicity=Multiplicity(0, 1))
    }
)
nextElement51: BinaryAssociation = BinaryAssociation(
    name="nextElement51",
    ends={
        Property(name="RDM_RouteElement52", type=RDM_RouteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_RouteElement50", type=RDM_RouteElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
turnout53: BinaryAssociation = BinaryAssociation(
    name="turnout53",
    ends={
        Property(name="RDM_Turnout54", type=RDM_TurnoutSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="RDM_TurnoutSignal", type=RDM_Turnout, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RDM_Signal_RDMElement = Generalization(general=RDMElement, specific=RDM_Signal)
gen_RDM_TrackElement_RDMElement = Generalization(general=RDMElement, specific=RDM_TrackElement)
gen_RDM_Train_RDMElement = Generalization(general=RDMElement, specific=RDM_Train)
gen_RDM_ConnectionPoint_RDMElement = Generalization(general=RDMElement, specific=RDM_ConnectionPoint)
gen_RDM_Route_RDMElement = Generalization(general=RDMElement, specific=RDM_Route)
gen_RDM_Section_TrackElement = Generalization(general=TrackElement, specific=RDM_Section)
gen_RDM_Turnout_TrackElement = Generalization(general=TrackElement, specific=RDM_Turnout)
gen_RDM_TurnoutDesiredDirection_RDMElement = Generalization(general=RDMElement, specific=RDM_TurnoutDesiredDirection)
gen_RDM_Station_Section = Generalization(general=Section, specific=RDM_Station)
gen_RDM_RouteElement_RDMElement = Generalization(general=RDMElement, specific=RDM_RouteElement)
gen_RDM_TurnoutSignal_Signal = Generalization(general=Signal, specific=RDM_TurnoutSignal)

# Domain Model
domain_model = DomainModel(
    name="RDM",
    types={RDM_RailwayDomainModel, RDM_Train, RDM_TrackElement, RDM_Section, RDM_Turnout, RDM_ConnectionPoint, RDM_Signal, RDM_TurnoutDesiredDirection, RDM_Route, RDM_RouteElement, RDMElement, RDM_Station, RDM_RDMElement, TrackElement, Section, RDM_TurnoutSignal, Signal, Speed, TurnoutDirection, ConnectionDirection},
    associations={trains0, departuresFrom17, follows20, standsOn23, standsOn24, observes25, connectsTo27, sections1, turnouts3, editorCP5, editorSignal7, editorTDD9, editorRoute11, editorRouteElement13, arrivesTo15, controls37, holds40, occupiedBy30, nextElement42, firstElement31, referredTurnout32, routeElement35, referredElement45, desiredDirection48, belongsTo49, nextElement51, turnout53},
    generalizations={gen_RDM_Signal_RDMElement, gen_RDM_TrackElement_RDMElement, gen_RDM_Train_RDMElement, gen_RDM_ConnectionPoint_RDMElement, gen_RDM_Route_RDMElement, gen_RDM_Section_TrackElement, gen_RDM_Turnout_TrackElement, gen_RDM_TurnoutDesiredDirection_RDMElement, gen_RDM_Station_Section, gen_RDM_RouteElement_RDMElement, gen_RDM_TurnoutSignal_Signal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)