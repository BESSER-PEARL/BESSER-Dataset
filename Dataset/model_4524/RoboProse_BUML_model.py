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
MOVE_DIRECTION: Enumeration = Enumeration(
    name="MOVE_DIRECTION",
    literals={
            EnumerationLiteral(name="FORWARDS"),
			EnumerationLiteral(name="BACKWARDS")
    }
)

TURN_DIRECTION: Enumeration = Enumeration(
    name="TURN_DIRECTION",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

# Classes
model_Root = Class(name="model::Root")
model_RoboProse = Class(name="model::RoboProse")
model_Main = Class(name="model::Main")
model_EventListener = Class(name="model::EventListener")
ActionsList = Class(name="ActionsList")
model_Event = Class(name="model::Event", is_abstract=True)
model_ActionsList = Class(name="model::ActionsList", is_abstract=True)
model_Action = Class(name="model::Action", is_abstract=True)
model_Ending = Class(name="model::Ending", is_abstract=True)
model_RotorAction = Class(name="model::RotorAction", is_abstract=True)
Action = Class(name="Action")
model_Move = Class(name="model::Move")
RotorAction = Class(name="RotorAction")
model_RandomAction = Class(name="model::RandomAction", is_abstract=True)
ContinuosAction = Class(name="ContinuosAction")
RandomAction = Class(name="RandomAction")
model_Turn = Class(name="model::Turn")
model_Stop = Class(name="model::Stop")
model_Repeat = Class(name="model::Repeat")
Ending = Class(name="Ending")
model_StartOver = Class(name="model::StartOver")
model_Wait = Class(name="model::Wait")
model_Obstacle = Class(name="model::Obstacle")
Event = Class(name="Event")
model_Tapped = Class(name="model::Tapped")
model_ContinuosAction = Class(name="model::ContinuosAction", is_abstract=True)

# model_Root class attributes and methods

# model_RoboProse class attributes and methods

# model_Main class attributes and methods

# model_EventListener class attributes and methods

# ActionsList class attributes and methods

# model_Event class attributes and methods

# model_ActionsList class attributes and methods

# model_Action class attributes and methods

# model_Ending class attributes and methods

# model_RotorAction class attributes and methods

# Action class attributes and methods

# model_Move class attributes and methods
model_Move_direction: Property = Property(name="direction", type=StringType)
model_Move.attributes={model_Move_direction}

# RotorAction class attributes and methods

# model_RandomAction class attributes and methods
model_RandomAction_isRandom: Property = Property(name="isRandom", type=BooleanType)
model_RandomAction.attributes={model_RandomAction_isRandom}

# ContinuosAction class attributes and methods

# RandomAction class attributes and methods

# model_Turn class attributes and methods
model_Turn_degrees: Property = Property(name="degrees", type=FloatType)
model_Turn_direction: Property = Property(name="direction", type=StringType)
model_Turn.attributes={model_Turn_degrees, model_Turn_direction}

# model_Stop class attributes and methods

# model_Repeat class attributes and methods

# Ending class attributes and methods

# model_StartOver class attributes and methods

# model_Wait class attributes and methods

# model_Obstacle class attributes and methods

# Event class attributes and methods

# model_Tapped class attributes and methods

# model_ContinuosAction class attributes and methods
model_ContinuosAction_duration: Property = Property(name="duration", type=FloatType)
model_ContinuosAction.attributes={model_ContinuosAction_duration}

# Relationships
robot0: BinaryAssociation = BinaryAssociation(
    name="robot0",
    ends={
        Property(name="model_RoboProse", type=model_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Root", type=model_RoboProse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
main1: BinaryAssociation = BinaryAssociation(
    name="main1",
    ends={
        Property(name="model_Main", type=model_RoboProse, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoboProse2", type=model_Main, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listeners3: BinaryAssociation = BinaryAssociation(
    name="listeners3",
    ends={
        Property(name="model_EventListener", type=model_RoboProse, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoboProse4", type=model_EventListener, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sublisteners6: BinaryAssociation = BinaryAssociation(
    name="sublisteners6",
    ends={
        Property(name="model_EventListener7", type=model_EventListener, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EventListener5", type=model_EventListener, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="model_Event", type=model_EventListener, multiplicity=Multiplicity(1, 1)),
        Property(name="model_EventListener9", type=model_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions10: BinaryAssociation = BinaryAssociation(
    name="actions10",
    ends={
        Property(name="model_Action", type=model_ActionsList, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ActionsList", type=model_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ending11: BinaryAssociation = BinaryAssociation(
    name="ending11",
    ends={
        Property(name="model_Ending", type=model_ActionsList, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ActionsList12", type=model_Ending, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_Main_ActionsList = Generalization(general=ActionsList, specific=model_Main)
gen_model_EventListener_ActionsList = Generalization(general=ActionsList, specific=model_EventListener)
gen_model_RotorAction_Action = Generalization(general=Action, specific=model_RotorAction)
gen_model_Move_RotorAction = Generalization(general=RotorAction, specific=model_Move)
gen_model_RandomAction_Action = Generalization(general=Action, specific=model_RandomAction)
gen_model_Move_ContinuosAction = Generalization(general=ContinuosAction, specific=model_Move)
gen_model_Move_RandomAction = Generalization(general=RandomAction, specific=model_Move)
gen_model_Turn_RotorAction = Generalization(general=RotorAction, specific=model_Turn)
gen_model_Turn_ContinuosAction = Generalization(general=ContinuosAction, specific=model_Turn)
gen_model_Turn_RandomAction = Generalization(general=RandomAction, specific=model_Turn)
gen_model_Stop_ContinuosAction = Generalization(general=ContinuosAction, specific=model_Stop)
gen_model_Repeat_Ending = Generalization(general=Ending, specific=model_Repeat)
gen_model_StartOver_Ending = Generalization(general=Ending, specific=model_StartOver)
gen_model_Wait_Ending = Generalization(general=Ending, specific=model_Wait)
gen_model_Obstacle_Event = Generalization(general=Event, specific=model_Obstacle)
gen_model_Tapped_Event = Generalization(general=Event, specific=model_Tapped)
gen_model_ContinuosAction_Action = Generalization(general=Action, specific=model_ContinuosAction)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Root, model_RoboProse, model_Main, model_EventListener, ActionsList, model_Event, model_ActionsList, model_Action, model_Ending, model_RotorAction, Action, model_Move, RotorAction, model_RandomAction, ContinuosAction, RandomAction, model_Turn, model_Stop, model_Repeat, Ending, model_StartOver, model_Wait, model_Obstacle, Event, model_Tapped, model_ContinuosAction, MOVE_DIRECTION, TURN_DIRECTION},
    associations={robot0, main1, listeners3, sublisteners6, event8, actions10, ending11},
    generalizations={gen_model_Main_ActionsList, gen_model_EventListener_ActionsList, gen_model_RotorAction_Action, gen_model_Move_RotorAction, gen_model_RandomAction_Action, gen_model_Move_ContinuosAction, gen_model_Move_RandomAction, gen_model_Turn_RotorAction, gen_model_Turn_ContinuosAction, gen_model_Turn_RandomAction, gen_model_Stop_ContinuosAction, gen_model_Repeat_Ending, gen_model_StartOver_Ending, gen_model_Wait_Ending, gen_model_Obstacle_Event, gen_model_Tapped_Event, gen_model_ContinuosAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)