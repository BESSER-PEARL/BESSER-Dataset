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
GoToStrategy: Enumeration = Enumeration(
    name="GoToStrategy",
    literals={
            EnumerationLiteral(name="DIRECT"),
			EnumerationLiteral(name="HORIZONTAL_FIRST"),
			EnumerationLiteral(name="VERTICAL_FIRST")
    }
)

TravelMode: Enumeration = Enumeration(
    name="TravelMode",
    literals={
            EnumerationLiteral(name="SAFE"),
			EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="AGGRESSIVE")
    }
)

# Classes
behaviour_NamedElement = Class(name="behaviour::NamedElement", is_abstract=True)
behaviour_Drone = Class(name="behaviour::Drone")
behaviour_Coordinate = Class(name="behaviour::Coordinate")
behaviour_Move = Class(name="behaviour::Move", is_abstract=True)
behaviour_MoveTransition = Class(name="behaviour::MoveTransition")
behaviour_Slot = Class(name="behaviour::Slot")
behaviour_Action = Class(name="behaviour::Action", is_abstract=True)
behaviour_Start = Class(name="behaviour::Start")
Move = Class(name="Move")
behaviour_Stop = Class(name="behaviour::Stop")
behaviour_Choice = Class(name="behaviour::Choice")
MoveTransition = Class(name="MoveTransition")
behaviour_TakeOff = Class(name="behaviour::TakeOff")
behaviour_Land = Class(name="behaviour::Land")
behaviour_GoTo = Class(name="behaviour::GoTo")
behaviour_Behaviour = Class(name="behaviour::Behaviour")
NamedElement = Class(name="NamedElement")
behaviour_HeadTo = Class(name="behaviour::HeadTo")
behaviour_Circle = Class(name="behaviour::Circle")
behaviour_CommunicationAction = Class(name="behaviour::CommunicationAction", is_abstract=True)
Action = Class(name="Action")
behaviour_Notify = Class(name="behaviour::Notify", is_abstract=True)
CommunicationAction = Class(name="CommunicationAction")
behaviour_BroadcastNotify = Class(name="behaviour::BroadcastNotify")
Notify = Class(name="Notify")
behaviour_UnicastNotify = Class(name="behaviour::UnicastNotify")
behaviour_MulticastNotify = Class(name="behaviour::MulticastNotify")
behaviour_CheckNotification = Class(name="behaviour::CheckNotification")
behaviour_DeviceAction = Class(name="behaviour::DeviceAction")
behaviour_Hover = Class(name="behaviour::Hover")
behaviour_Feedback = Class(name="behaviour::Feedback")
behaviour_Parameter = Class(name="behaviour::Parameter")

# behaviour_NamedElement class attributes and methods
behaviour_NamedElement_name: Property = Property(name="name", type=StringType)
behaviour_NamedElement.attributes={behaviour_NamedElement_name}

# behaviour_Drone class attributes and methods
behaviour_Drone_typeName: Property = Property(name="typeName", type=StringType)
behaviour_Drone_travelMode: Property = Property(name="travelMode", type=StringType)
behaviour_Drone.attributes={behaviour_Drone_typeName, behaviour_Drone_travelMode}

# behaviour_Coordinate class attributes and methods
behaviour_Coordinate_latitude: Property = Property(name="latitude", type=FloatType)
behaviour_Coordinate_longitude: Property = Property(name="longitude", type=FloatType)
behaviour_Coordinate_altitude: Property = Property(name="altitude", type=FloatType)
behaviour_Coordinate_heading: Property = Property(name="heading", type=FloatType)
behaviour_Coordinate.attributes={behaviour_Coordinate_longitude, behaviour_Coordinate_altitude, behaviour_Coordinate_latitude, behaviour_Coordinate_heading}

# behaviour_Move class attributes and methods

# behaviour_MoveTransition class attributes and methods
behaviour_MoveTransition_fluid: Property = Property(name="fluid", type=BooleanType)
behaviour_MoveTransition.attributes={behaviour_MoveTransition_fluid}

# behaviour_Slot class attributes and methods

# behaviour_Action class attributes and methods

# behaviour_Start class attributes and methods

# Move class attributes and methods

# behaviour_Stop class attributes and methods

# behaviour_Choice class attributes and methods
behaviour_Choice_conditionIdentifier: Property = Property(name="conditionIdentifier", type=StringType)
behaviour_Choice.attributes={behaviour_Choice_conditionIdentifier}

# MoveTransition class attributes and methods

# behaviour_TakeOff class attributes and methods
behaviour_TakeOff_altitude: Property = Property(name="altitude", type=FloatType)
behaviour_TakeOff.attributes={behaviour_TakeOff_altitude}

# behaviour_Land class attributes and methods

# behaviour_GoTo class attributes and methods
behaviour_GoTo_strategy: Property = Property(name="strategy", type=StringType)
behaviour_GoTo.attributes={behaviour_GoTo_strategy}

# behaviour_Behaviour class attributes and methods
behaviour_Behaviour_crs: Property = Property(name="crs", type=StringType)
behaviour_Behaviour.attributes={behaviour_Behaviour_crs}

# NamedElement class attributes and methods

# behaviour_HeadTo class attributes and methods
behaviour_HeadTo_direction: Property = Property(name="direction", type=FloatType)
behaviour_HeadTo.attributes={behaviour_HeadTo_direction}

# behaviour_Circle class attributes and methods
behaviour_Circle_duration: Property = Property(name="duration", type=FloatType)
behaviour_Circle_radius: Property = Property(name="radius", type=FloatType)
behaviour_Circle_altitude: Property = Property(name="altitude", type=FloatType)
behaviour_Circle_clockwise: Property = Property(name="clockwise", type=BooleanType)
behaviour_Circle.attributes={behaviour_Circle_radius, behaviour_Circle_altitude, behaviour_Circle_duration, behaviour_Circle_clockwise}

# behaviour_CommunicationAction class attributes and methods

# Action class attributes and methods

# behaviour_Notify class attributes and methods

# CommunicationAction class attributes and methods

# behaviour_BroadcastNotify class attributes and methods

# Notify class attributes and methods

# behaviour_UnicastNotify class attributes and methods

# behaviour_MulticastNotify class attributes and methods

# behaviour_CheckNotification class attributes and methods

# behaviour_DeviceAction class attributes and methods
behaviour_DeviceAction_actionName: Property = Property(name="actionName", type=StringType)
behaviour_DeviceAction.attributes={behaviour_DeviceAction_actionName}

# behaviour_Hover class attributes and methods
behaviour_Hover_duration: Property = Property(name="duration", type=FloatType)
behaviour_Hover.attributes={behaviour_Hover_duration}

# behaviour_Feedback class attributes and methods
behaviour_Feedback_actionName: Property = Property(name="actionName", type=StringType)
behaviour_Feedback.attributes={behaviour_Feedback_actionName}

# behaviour_Parameter class attributes and methods
behaviour_Parameter_key: Property = Property(name="key", type=StringType)
behaviour_Parameter_value: Property = Property(name="value", type=StringType)
behaviour_Parameter.attributes={behaviour_Parameter_value, behaviour_Parameter_key}

# Relationships
drones0: BinaryAssociation = BinaryAssociation(
    name="drones0",
    ends={
        Property(name="behaviour_Drone", type=behaviour_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behaviour", type=behaviour_Drone, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
home1: BinaryAssociation = BinaryAssociation(
    name="home1",
    ends={
        Property(name="behaviour_Coordinate", type=behaviour_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Drone2", type=behaviour_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
movements3: BinaryAssociation = BinaryAssociation(
    name="movements3",
    ends={
        Property(name="behaviour_Move", type=behaviour_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Drone4", type=behaviour_Move, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moveTransitions5: BinaryAssociation = BinaryAssociation(
    name="moveTransitions5",
    ends={
        Property(name="behaviour_MoveTransition", type=behaviour_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Drone6", type=behaviour_MoveTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slots7: BinaryAssociation = BinaryAssociation(
    name="slots7",
    ends={
        Property(name="behaviour_Slot", type=behaviour_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Drone8", type=behaviour_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
falseBranch9: BinaryAssociation = BinaryAssociation(
    name="falseBranch9",
    ends={
        Property(name="behaviour_Move10", type=behaviour_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Choice", type=behaviour_Move, multiplicity=Multiplicity(1, 1))
    }
)
preActions11: BinaryAssociation = BinaryAssociation(
    name="preActions11",
    ends={
        Property(name="behaviour_Action", type=behaviour_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Move12", type=behaviour_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postActions13: BinaryAssociation = BinaryAssociation(
    name="postActions13",
    ends={
        Property(name="behaviour_Action15", type=behaviour_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Move14", type=behaviour_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetPosition18: BinaryAssociation = BinaryAssociation(
    name="targetPosition18",
    ends={
        Property(name="behaviour_Coordinate19", type=behaviour_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Circle", type=behaviour_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
slot20: BinaryAssociation = BinaryAssociation(
    name="slot20",
    ends={
        Property(name="behaviour_Slot21", type=behaviour_Notify, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Notify", type=behaviour_Slot, multiplicity=Multiplicity(1, 1))
    }
)
receiver22: BinaryAssociation = BinaryAssociation(
    name="receiver22",
    ends={
        Property(name="behaviour_Drone23", type=behaviour_UnicastNotify, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_UnicastNotify", type=behaviour_Drone, multiplicity=Multiplicity(1, 1))
    }
)
receiver24: BinaryAssociation = BinaryAssociation(
    name="receiver24",
    ends={
        Property(name="behaviour_Drone25", type=behaviour_MulticastNotify, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MulticastNotify", type=behaviour_Drone, multiplicity=Multiplicity(1, 9999))
    }
)
slot26: BinaryAssociation = BinaryAssociation(
    name="slot26",
    ends={
        Property(name="behaviour_Slot27", type=behaviour_CheckNotification, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CheckNotification", type=behaviour_Slot, multiplicity=Multiplicity(1, 1))
    }
)
targetPosition16: BinaryAssociation = BinaryAssociation(
    name="targetPosition16",
    ends={
        Property(name="behaviour_Coordinate17", type=behaviour_GoTo, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_GoTo", type=behaviour_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
waitFor29: BinaryAssociation = BinaryAssociation(
    name="waitFor29",
    ends={
        Property(name="behaviour_Slot31", type=behaviour_MoveTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MoveTransition30", type=behaviour_Slot, multiplicity=Multiplicity(0, 1))
    }
)
from32: BinaryAssociation = BinaryAssociation(
    name="from32",
    ends={
        Property(name="behaviour_Move34", type=behaviour_MoveTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MoveTransition33", type=behaviour_Move, multiplicity=Multiplicity(1, 1))
    }
)
to35: BinaryAssociation = BinaryAssociation(
    name="to35",
    ends={
        Property(name="behaviour_Move37", type=behaviour_MoveTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MoveTransition36", type=behaviour_Move, multiplicity=Multiplicity(1, 1))
    }
)
parameters38: BinaryAssociation = BinaryAssociation(
    name="parameters38",
    ends={
        Property(name="behaviour_Parameter39", type=behaviour_Feedback, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Feedback", type=behaviour_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters28: BinaryAssociation = BinaryAssociation(
    name="parameters28",
    ends={
        Property(name="behaviour_Parameter", type=behaviour_DeviceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DeviceAction", type=behaviour_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_behaviour_Drone_NamedElement = Generalization(general=NamedElement, specific=behaviour_Drone)
gen_behaviour_Action_NamedElement = Generalization(general=NamedElement, specific=behaviour_Action)
gen_behaviour_Start_Move = Generalization(general=Move, specific=behaviour_Start)
gen_behaviour_Stop_Move = Generalization(general=Move, specific=behaviour_Stop)
gen_behaviour_Choice_MoveTransition = Generalization(general=MoveTransition, specific=behaviour_Choice)
gen_behaviour_Move_NamedElement = Generalization(general=NamedElement, specific=behaviour_Move)
gen_behaviour_TakeOff_Move = Generalization(general=Move, specific=behaviour_TakeOff)
gen_behaviour_Land_Move = Generalization(general=Move, specific=behaviour_Land)
gen_behaviour_GoTo_Move = Generalization(general=Move, specific=behaviour_GoTo)
gen_behaviour_Behaviour_NamedElement = Generalization(general=NamedElement, specific=behaviour_Behaviour)
gen_behaviour_Hover_Move = Generalization(general=Move, specific=behaviour_Hover)
gen_behaviour_HeadTo_Move = Generalization(general=Move, specific=behaviour_HeadTo)
gen_behaviour_Circle_Move = Generalization(general=Move, specific=behaviour_Circle)
gen_behaviour_CommunicationAction_Action = Generalization(general=Action, specific=behaviour_CommunicationAction)
gen_behaviour_Notify_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_Notify)
gen_behaviour_BroadcastNotify_Notify = Generalization(general=Notify, specific=behaviour_BroadcastNotify)
gen_behaviour_UnicastNotify_Notify = Generalization(general=Notify, specific=behaviour_UnicastNotify)
gen_behaviour_MulticastNotify_Notify = Generalization(general=Notify, specific=behaviour_MulticastNotify)
gen_behaviour_CheckNotification_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_CheckNotification)
gen_behaviour_Slot_NamedElement = Generalization(general=NamedElement, specific=behaviour_Slot)
gen_behaviour_DeviceAction_Action = Generalization(general=Action, specific=behaviour_DeviceAction)
gen_behaviour_Feedback_CommunicationAction = Generalization(general=CommunicationAction, specific=behaviour_Feedback)

# Domain Model
domain_model = DomainModel(
    name="behaviour",
    types={behaviour_NamedElement, behaviour_Drone, behaviour_Coordinate, behaviour_Move, behaviour_MoveTransition, behaviour_Slot, behaviour_Action, behaviour_Start, Move, behaviour_Stop, behaviour_Choice, MoveTransition, behaviour_TakeOff, behaviour_Land, behaviour_GoTo, behaviour_Behaviour, NamedElement, behaviour_HeadTo, behaviour_Circle, behaviour_CommunicationAction, Action, behaviour_Notify, CommunicationAction, behaviour_BroadcastNotify, Notify, behaviour_UnicastNotify, behaviour_MulticastNotify, behaviour_CheckNotification, behaviour_DeviceAction, behaviour_Hover, behaviour_Feedback, behaviour_Parameter, GoToStrategy, TravelMode},
    associations={drones0, home1, movements3, moveTransitions5, slots7, falseBranch9, preActions11, postActions13, targetPosition18, slot20, receiver22, receiver24, slot26, targetPosition16, waitFor29, from32, to35, parameters38, parameters28},
    generalizations={gen_behaviour_Drone_NamedElement, gen_behaviour_Action_NamedElement, gen_behaviour_Start_Move, gen_behaviour_Stop_Move, gen_behaviour_Choice_MoveTransition, gen_behaviour_Move_NamedElement, gen_behaviour_TakeOff_Move, gen_behaviour_Land_Move, gen_behaviour_GoTo_Move, gen_behaviour_Behaviour_NamedElement, gen_behaviour_Hover_Move, gen_behaviour_HeadTo_Move, gen_behaviour_Circle_Move, gen_behaviour_CommunicationAction_Action, gen_behaviour_Notify_CommunicationAction, gen_behaviour_BroadcastNotify_Notify, gen_behaviour_UnicastNotify_Notify, gen_behaviour_MulticastNotify_Notify, gen_behaviour_CheckNotification_CommunicationAction, gen_behaviour_Slot_NamedElement, gen_behaviour_DeviceAction_Action, gen_behaviour_Feedback_CommunicationAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)