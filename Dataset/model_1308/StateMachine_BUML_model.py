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
StateMachine_StateMachineBehavioralModel = Class(name="StateMachine::StateMachineBehavioralModel")
StateMachine_StateMachine = Class(name="StateMachine::StateMachine")
NamedElement = Class(name="NamedElement")
StateMachine_State = Class(name="StateMachine::State")
StateMachine_Transition = Class(name="StateMachine::Transition")
StateMachine_Trigger = Class(name="StateMachine::Trigger", is_abstract=True)
StateMachine_Guard = Class(name="StateMachine::Guard", is_abstract=True)
StateMachine_Action = Class(name="StateMachine::Action", is_abstract=True)
StateMachine_CompositeState = Class(name="StateMachine::CompositeState")
State = Class(name="State")
StateMachine_RDMElement = Class(name="StateMachine::RDMElement")
GuardExpression = Class(name="GuardExpression")
StateMachine_TrainCurrentlyStandsOn = Class(name="StateMachine::TrainCurrentlyStandsOn")
StateMachine_TurnoutCurrentDirection = Class(name="StateMachine::TurnoutCurrentDirection")
StateMachine_NamedElement = Class(name="StateMachine::NamedElement", is_abstract=True)
StateMachine_ChangeTrainHeadingSpeed = Class(name="StateMachine::ChangeTrainHeadingSpeed")
ActionExpression = Class(name="ActionExpression")
StateMachine_SignalCurrentAllowedSpeed = Class(name="StateMachine::SignalCurrentAllowedSpeed")
StateMachine_Train = Class(name="StateMachine::Train")
StateMachine_TrainHeadingSpeedChanged = Class(name="StateMachine::TrainHeadingSpeedChanged")
TriggerExpression = Class(name="TriggerExpression")
StateMachine_ChangeSignalAllowedSpeed = Class(name="StateMachine::ChangeSignalAllowedSpeed")
StateMachine_Signal = Class(name="StateMachine::Signal")
StateMachine_ChangeTurnoutDirection = Class(name="StateMachine::ChangeTurnoutDirection")
StateMachine_Turnout = Class(name="StateMachine::Turnout")
StateMachine_ChangeTrainCurrentTrackElement = Class(name="StateMachine::ChangeTrainCurrentTrackElement")
StateMachine_TrackElement = Class(name="StateMachine::TrackElement")
StateMachine_TrainCurrentHeadingSpeed = Class(name="StateMachine::TrainCurrentHeadingSpeed")
StateMachine_TurnoutDirectionChanged = Class(name="StateMachine::TurnoutDirectionChanged")
StateMachine_NextTrackElementIs = Class(name="StateMachine::NextTrackElementIs")
StateMachine_RouteElement = Class(name="StateMachine::RouteElement")
StateMachine_TurnoutHasDesiredDirection = Class(name="StateMachine::TurnoutHasDesiredDirection")
StateMachine_TurnoutDesiredDirection = Class(name="StateMachine::TurnoutDesiredDirection")
StateMachine_ActionExpression = Class(name="StateMachine::ActionExpression")
Action = Class(name="Action")
StateMachine_TrainTrackElementChanged = Class(name="StateMachine::TrainTrackElementChanged")
StateMachine_SignalAllowedSpeedChanged = Class(name="StateMachine::SignalAllowedSpeedChanged")
StateMachine_GuardExpression = Class(name="StateMachine::GuardExpression")
Guard = Class(name="Guard")
StateMachine_TriggerExpression = Class(name="StateMachine::TriggerExpression")
Trigger = Class(name="Trigger")

# StateMachine_StateMachineBehavioralModel class attributes and methods

# StateMachine_StateMachine class attributes and methods

# NamedElement class attributes and methods

# StateMachine_State class attributes and methods
StateMachine_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
StateMachine_State_isActive: Property = Property(name="isActive", type=BooleanType)
StateMachine_State.attributes={StateMachine_State_isActive, StateMachine_State_isInitial}

# StateMachine_Transition class attributes and methods
StateMachine_Transition_isFireable: Property = Property(name="isFireable", type=BooleanType)
StateMachine_Transition_isEnabled: Property = Property(name="isEnabled", type=BooleanType)
StateMachine_Transition.attributes={StateMachine_Transition_isEnabled, StateMachine_Transition_isFireable}

# StateMachine_Trigger class attributes and methods

# StateMachine_Guard class attributes and methods

# StateMachine_Action class attributes and methods

# StateMachine_CompositeState class attributes and methods

# State class attributes and methods

# StateMachine_RDMElement class attributes and methods

# GuardExpression class attributes and methods

# StateMachine_TrainCurrentlyStandsOn class attributes and methods

# StateMachine_TurnoutCurrentDirection class attributes and methods
StateMachine_TurnoutCurrentDirection_currentTurnoutDirection: Property = Property(name="currentTurnoutDirection", type=StringType)
StateMachine_TurnoutCurrentDirection.attributes={StateMachine_TurnoutCurrentDirection_currentTurnoutDirection}

# StateMachine_NamedElement class attributes and methods
StateMachine_NamedElement_name: Property = Property(name="name", type=StringType)
StateMachine_NamedElement.attributes={StateMachine_NamedElement_name}

# StateMachine_ChangeTrainHeadingSpeed class attributes and methods
StateMachine_ChangeTrainHeadingSpeed_newHeadingSpeed: Property = Property(name="newHeadingSpeed", type=StringType)
StateMachine_ChangeTrainHeadingSpeed.attributes={StateMachine_ChangeTrainHeadingSpeed_newHeadingSpeed}

# ActionExpression class attributes and methods

# StateMachine_SignalCurrentAllowedSpeed class attributes and methods
StateMachine_SignalCurrentAllowedSpeed_currentAllowedSpeed: Property = Property(name="currentAllowedSpeed", type=StringType)
StateMachine_SignalCurrentAllowedSpeed.attributes={StateMachine_SignalCurrentAllowedSpeed_currentAllowedSpeed}

# StateMachine_Train class attributes and methods

# StateMachine_TrainHeadingSpeedChanged class attributes and methods
StateMachine_TrainHeadingSpeedChanged_newHeadingSpeed: Property = Property(name="newHeadingSpeed", type=StringType)
StateMachine_TrainHeadingSpeedChanged.attributes={StateMachine_TrainHeadingSpeedChanged_newHeadingSpeed}

# TriggerExpression class attributes and methods

# StateMachine_ChangeSignalAllowedSpeed class attributes and methods
StateMachine_ChangeSignalAllowedSpeed_newAllowedSpeed: Property = Property(name="newAllowedSpeed", type=StringType)
StateMachine_ChangeSignalAllowedSpeed.attributes={StateMachine_ChangeSignalAllowedSpeed_newAllowedSpeed}

# StateMachine_Signal class attributes and methods

# StateMachine_ChangeTurnoutDirection class attributes and methods
StateMachine_ChangeTurnoutDirection_newTurnoutDirection: Property = Property(name="newTurnoutDirection", type=StringType)
StateMachine_ChangeTurnoutDirection.attributes={StateMachine_ChangeTurnoutDirection_newTurnoutDirection}

# StateMachine_Turnout class attributes and methods

# StateMachine_ChangeTrainCurrentTrackElement class attributes and methods

# StateMachine_TrackElement class attributes and methods

# StateMachine_TrainCurrentHeadingSpeed class attributes and methods
StateMachine_TrainCurrentHeadingSpeed_currentHeadingSpeed: Property = Property(name="currentHeadingSpeed", type=StringType)
StateMachine_TrainCurrentHeadingSpeed.attributes={StateMachine_TrainCurrentHeadingSpeed_currentHeadingSpeed}

# StateMachine_TurnoutDirectionChanged class attributes and methods
StateMachine_TurnoutDirectionChanged_newTurnoutDirection: Property = Property(name="newTurnoutDirection", type=StringType)
StateMachine_TurnoutDirectionChanged.attributes={StateMachine_TurnoutDirectionChanged_newTurnoutDirection}

# StateMachine_NextTrackElementIs class attributes and methods

# StateMachine_RouteElement class attributes and methods

# StateMachine_TurnoutHasDesiredDirection class attributes and methods

# StateMachine_TurnoutDesiredDirection class attributes and methods

# StateMachine_ActionExpression class attributes and methods
StateMachine_ActionExpression_expression: Property = Property(name="expression", type=StringType)
StateMachine_ActionExpression.attributes={StateMachine_ActionExpression_expression}

# Action class attributes and methods

# StateMachine_TrainTrackElementChanged class attributes and methods

# StateMachine_SignalAllowedSpeedChanged class attributes and methods
StateMachine_SignalAllowedSpeedChanged_newAllowedSpeed: Property = Property(name="newAllowedSpeed", type=StringType)
StateMachine_SignalAllowedSpeedChanged.attributes={StateMachine_SignalAllowedSpeedChanged_newAllowedSpeed}

# StateMachine_GuardExpression class attributes and methods
StateMachine_GuardExpression_expression: Property = Property(name="expression", type=StringType)
StateMachine_GuardExpression.attributes={StateMachine_GuardExpression_expression}

# Guard class attributes and methods

# StateMachine_TriggerExpression class attributes and methods
StateMachine_TriggerExpression_expression: Property = Property(name="expression", type=StringType)
StateMachine_TriggerExpression.attributes={StateMachine_TriggerExpression_expression}

# Trigger class attributes and methods

# Relationships
statemachines0: BinaryAssociation = BinaryAssociation(
    name="statemachines0",
    ends={
        Property(name="StateMachine_StateMachine", type=StateMachine_StateMachineBehavioralModel, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachineBehavioralModel", type=StateMachine_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="StateMachine_State", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine2", type=StateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="StateMachine_Transition", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine4", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers5: BinaryAssociation = BinaryAssociation(
    name="triggers5",
    ends={
        Property(name="StateMachine_Trigger", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine6", type=StateMachine_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guards7: BinaryAssociation = BinaryAssociation(
    name="guards7",
    ends={
        Property(name="StateMachine_Guard", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine8", type=StateMachine_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions9: BinaryAssociation = BinaryAssociation(
    name="actions9",
    ends={
        Property(name="StateMachine_Action", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine10", type=StateMachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeState11: BinaryAssociation = BinaryAssociation(
    name="activeState11",
    ends={
        Property(name="StateMachine_State13", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine12", type=StateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
statemachine31: BinaryAssociation = BinaryAssociation(
    name="statemachine31",
    ends={
        Property(name="StateMachine_StateMachine32", type=StateMachine_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_CompositeState", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject14: BinaryAssociation = BinaryAssociation(
    name="referredObject14",
    ends={
        Property(name="StateMachine_RDMElement", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine15", type=StateMachine_RDMElement, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions16: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions16",
    ends={
        Property(name="Transition", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceState", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions17: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions17",
    ends={
        Property(name="Transition18", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="targetState", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
sourceState19: BinaryAssociation = BinaryAssociation(
    name="sourceState19",
    ends={
        Property(name="State", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=StateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
targetState20: BinaryAssociation = BinaryAssociation(
    name="targetState20",
    ends={
        Property(name="State21", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=StateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger22: BinaryAssociation = BinaryAssociation(
    name="trigger22",
    ends={
        Property(name="StateMachine_Trigger24", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition23", type=StateMachine_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
guard25: BinaryAssociation = BinaryAssociation(
    name="guard25",
    ends={
        Property(name="StateMachine_Guard27", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition26", type=StateMachine_Guard, multiplicity=Multiplicity(0, 9999))
    }
)
action28: BinaryAssociation = BinaryAssociation(
    name="action28",
    ends={
        Property(name="StateMachine_Action30", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition29", type=StateMachine_Action, multiplicity=Multiplicity(0, 9999))
    }
)
train40: BinaryAssociation = BinaryAssociation(
    name="train40",
    ends={
        Property(name="StateMachine_Train41", type=StateMachine_TrainCurrentHeadingSpeed, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainCurrentHeadingSpeed", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
train42: BinaryAssociation = BinaryAssociation(
    name="train42",
    ends={
        Property(name="StateMachine_Train43", type=StateMachine_TrainCurrentlyStandsOn, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainCurrentlyStandsOn", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
trackElements44: BinaryAssociation = BinaryAssociation(
    name="trackElements44",
    ends={
        Property(name="StateMachine_TrackElement46", type=StateMachine_TrainCurrentlyStandsOn, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainCurrentlyStandsOn45", type=StateMachine_TrackElement, multiplicity=Multiplicity(0, 2))
    }
)
turnout47: BinaryAssociation = BinaryAssociation(
    name="turnout47",
    ends={
        Property(name="StateMachine_Turnout48", type=StateMachine_TurnoutCurrentDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TurnoutCurrentDirection", type=StateMachine_Turnout, multiplicity=Multiplicity(0, 1))
    }
)
train33: BinaryAssociation = BinaryAssociation(
    name="train33",
    ends={
        Property(name="StateMachine_Train", type=StateMachine_ChangeTrainHeadingSpeed, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_ChangeTrainHeadingSpeed", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
signal49: BinaryAssociation = BinaryAssociation(
    name="signal49",
    ends={
        Property(name="StateMachine_Signal50", type=StateMachine_SignalCurrentAllowedSpeed, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_SignalCurrentAllowedSpeed", type=StateMachine_Signal, multiplicity=Multiplicity(0, 1))
    }
)
signal34: BinaryAssociation = BinaryAssociation(
    name="signal34",
    ends={
        Property(name="StateMachine_Signal", type=StateMachine_ChangeSignalAllowedSpeed, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_ChangeSignalAllowedSpeed", type=StateMachine_Signal, multiplicity=Multiplicity(0, 1))
    }
)
turnout35: BinaryAssociation = BinaryAssociation(
    name="turnout35",
    ends={
        Property(name="StateMachine_Turnout", type=StateMachine_ChangeTurnoutDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_ChangeTurnoutDirection", type=StateMachine_Turnout, multiplicity=Multiplicity(0, 1))
    }
)
train36: BinaryAssociation = BinaryAssociation(
    name="train36",
    ends={
        Property(name="StateMachine_Train37", type=StateMachine_ChangeTrainCurrentTrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_ChangeTrainCurrentTrackElement", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
newTrackElements38: BinaryAssociation = BinaryAssociation(
    name="newTrackElements38",
    ends={
        Property(name="StateMachine_TrackElement", type=StateMachine_ChangeTrainCurrentTrackElement, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_ChangeTrainCurrentTrackElement39", type=StateMachine_TrackElement, multiplicity=Multiplicity(0, 2))
    }
)
turnout60: BinaryAssociation = BinaryAssociation(
    name="turnout60",
    ends={
        Property(name="StateMachine_Turnout61", type=StateMachine_TurnoutDirectionChanged, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TurnoutDirectionChanged", type=StateMachine_Turnout, multiplicity=Multiplicity(0, 1))
    }
)
routeElement62: BinaryAssociation = BinaryAssociation(
    name="routeElement62",
    ends={
        Property(name="StateMachine_RouteElement", type=StateMachine_NextTrackElementIs, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_NextTrackElementIs", type=StateMachine_RouteElement, multiplicity=Multiplicity(0, 1))
    }
)
trackElement63: BinaryAssociation = BinaryAssociation(
    name="trackElement63",
    ends={
        Property(name="StateMachine_TrackElement65", type=StateMachine_NextTrackElementIs, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_NextTrackElementIs64", type=StateMachine_TrackElement, multiplicity=Multiplicity(0, 1))
    }
)
turnout66: BinaryAssociation = BinaryAssociation(
    name="turnout66",
    ends={
        Property(name="StateMachine_Turnout67", type=StateMachine_TurnoutHasDesiredDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TurnoutHasDesiredDirection", type=StateMachine_Turnout, multiplicity=Multiplicity(0, 1))
    }
)
desiredDirection68: BinaryAssociation = BinaryAssociation(
    name="desiredDirection68",
    ends={
        Property(name="StateMachine_TurnoutDesiredDirection", type=StateMachine_TurnoutHasDesiredDirection, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TurnoutHasDesiredDirection69", type=StateMachine_TurnoutDesiredDirection, multiplicity=Multiplicity(0, 1))
    }
)
train51: BinaryAssociation = BinaryAssociation(
    name="train51",
    ends={
        Property(name="StateMachine_Train52", type=StateMachine_TrainHeadingSpeedChanged, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainHeadingSpeedChanged", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
train53: BinaryAssociation = BinaryAssociation(
    name="train53",
    ends={
        Property(name="StateMachine_Train54", type=StateMachine_TrainTrackElementChanged, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainTrackElementChanged", type=StateMachine_Train, multiplicity=Multiplicity(0, 1))
    }
)
trackElements55: BinaryAssociation = BinaryAssociation(
    name="trackElements55",
    ends={
        Property(name="StateMachine_TrackElement57", type=StateMachine_TrainTrackElementChanged, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_TrainTrackElementChanged56", type=StateMachine_TrackElement, multiplicity=Multiplicity(0, 2))
    }
)
signal58: BinaryAssociation = BinaryAssociation(
    name="signal58",
    ends={
        Property(name="StateMachine_Signal59", type=StateMachine_SignalAllowedSpeedChanged, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_SignalAllowedSpeedChanged", type=StateMachine_Signal, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_StateMachine_StateMachine_NamedElement = Generalization(general=NamedElement, specific=StateMachine_StateMachine)
gen_StateMachine_CompositeState_State = Generalization(general=State, specific=StateMachine_CompositeState)
gen_StateMachine_State_NamedElement = Generalization(general=NamedElement, specific=StateMachine_State)
gen_StateMachine_Transition_NamedElement = Generalization(general=NamedElement, specific=StateMachine_Transition)
gen_StateMachine_TrainCurrentHeadingSpeed_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_TrainCurrentHeadingSpeed)
gen_StateMachine_TrainCurrentlyStandsOn_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_TrainCurrentlyStandsOn)
gen_StateMachine_Trigger_NamedElement = Generalization(general=NamedElement, specific=StateMachine_Trigger)
gen_StateMachine_Guard_NamedElement = Generalization(general=NamedElement, specific=StateMachine_Guard)
gen_StateMachine_TurnoutCurrentDirection_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_TurnoutCurrentDirection)
gen_StateMachine_Action_NamedElement = Generalization(general=NamedElement, specific=StateMachine_Action)
gen_StateMachine_ChangeTrainHeadingSpeed_ActionExpression = Generalization(general=ActionExpression, specific=StateMachine_ChangeTrainHeadingSpeed)
gen_StateMachine_SignalCurrentAllowedSpeed_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_SignalCurrentAllowedSpeed)
gen_StateMachine_ChangeSignalAllowedSpeed_ActionExpression = Generalization(general=ActionExpression, specific=StateMachine_ChangeSignalAllowedSpeed)
gen_StateMachine_ChangeTurnoutDirection_ActionExpression = Generalization(general=ActionExpression, specific=StateMachine_ChangeTurnoutDirection)
gen_StateMachine_ChangeTrainCurrentTrackElement_ActionExpression = Generalization(general=ActionExpression, specific=StateMachine_ChangeTrainCurrentTrackElement)
gen_StateMachine_TurnoutDirectionChanged_TriggerExpression = Generalization(general=TriggerExpression, specific=StateMachine_TurnoutDirectionChanged)
gen_StateMachine_NextTrackElementIs_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_NextTrackElementIs)
gen_StateMachine_TurnoutHasDesiredDirection_GuardExpression = Generalization(general=GuardExpression, specific=StateMachine_TurnoutHasDesiredDirection)
gen_StateMachine_TrainHeadingSpeedChanged_TriggerExpression = Generalization(general=TriggerExpression, specific=StateMachine_TrainHeadingSpeedChanged)
gen_StateMachine_TrainTrackElementChanged_TriggerExpression = Generalization(general=TriggerExpression, specific=StateMachine_TrainTrackElementChanged)
gen_StateMachine_SignalAllowedSpeedChanged_TriggerExpression = Generalization(general=TriggerExpression, specific=StateMachine_SignalAllowedSpeedChanged)
gen_StateMachine_ActionExpression_Action = Generalization(general=Action, specific=StateMachine_ActionExpression)
gen_StateMachine_GuardExpression_Guard = Generalization(general=Guard, specific=StateMachine_GuardExpression)
gen_StateMachine_TriggerExpression_Trigger = Generalization(general=Trigger, specific=StateMachine_TriggerExpression)

# Domain Model
domain_model = DomainModel(
    name="StateMachine",
    types={StateMachine_StateMachineBehavioralModel, StateMachine_StateMachine, NamedElement, StateMachine_State, StateMachine_Transition, StateMachine_Trigger, StateMachine_Guard, StateMachine_Action, StateMachine_CompositeState, State, StateMachine_RDMElement, GuardExpression, StateMachine_TrainCurrentlyStandsOn, StateMachine_TurnoutCurrentDirection, StateMachine_NamedElement, StateMachine_ChangeTrainHeadingSpeed, ActionExpression, StateMachine_SignalCurrentAllowedSpeed, StateMachine_Train, StateMachine_TrainHeadingSpeedChanged, TriggerExpression, StateMachine_ChangeSignalAllowedSpeed, StateMachine_Signal, StateMachine_ChangeTurnoutDirection, StateMachine_Turnout, StateMachine_ChangeTrainCurrentTrackElement, StateMachine_TrackElement, StateMachine_TrainCurrentHeadingSpeed, StateMachine_TurnoutDirectionChanged, StateMachine_NextTrackElementIs, StateMachine_RouteElement, StateMachine_TurnoutHasDesiredDirection, StateMachine_TurnoutDesiredDirection, StateMachine_ActionExpression, Action, StateMachine_TrainTrackElementChanged, StateMachine_SignalAllowedSpeedChanged, StateMachine_GuardExpression, Guard, StateMachine_TriggerExpression, Trigger},
    associations={statemachines0, states1, transitions3, triggers5, guards7, actions9, activeState11, statemachine31, referredObject14, outgoingTransitions16, incomingTransitions17, sourceState19, targetState20, trigger22, guard25, action28, train40, train42, trackElements44, turnout47, train33, signal49, signal34, turnout35, train36, newTrackElements38, turnout60, routeElement62, trackElement63, turnout66, desiredDirection68, train51, train53, trackElements55, signal58},
    generalizations={gen_StateMachine_StateMachine_NamedElement, gen_StateMachine_CompositeState_State, gen_StateMachine_State_NamedElement, gen_StateMachine_Transition_NamedElement, gen_StateMachine_TrainCurrentHeadingSpeed_GuardExpression, gen_StateMachine_TrainCurrentlyStandsOn_GuardExpression, gen_StateMachine_Trigger_NamedElement, gen_StateMachine_Guard_NamedElement, gen_StateMachine_TurnoutCurrentDirection_GuardExpression, gen_StateMachine_Action_NamedElement, gen_StateMachine_ChangeTrainHeadingSpeed_ActionExpression, gen_StateMachine_SignalCurrentAllowedSpeed_GuardExpression, gen_StateMachine_ChangeSignalAllowedSpeed_ActionExpression, gen_StateMachine_ChangeTurnoutDirection_ActionExpression, gen_StateMachine_ChangeTrainCurrentTrackElement_ActionExpression, gen_StateMachine_TurnoutDirectionChanged_TriggerExpression, gen_StateMachine_NextTrackElementIs_GuardExpression, gen_StateMachine_TurnoutHasDesiredDirection_GuardExpression, gen_StateMachine_TrainHeadingSpeedChanged_TriggerExpression, gen_StateMachine_TrainTrackElementChanged_TriggerExpression, gen_StateMachine_SignalAllowedSpeedChanged_TriggerExpression, gen_StateMachine_ActionExpression_Action, gen_StateMachine_GuardExpression_Guard, gen_StateMachine_TriggerExpression_Trigger},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)