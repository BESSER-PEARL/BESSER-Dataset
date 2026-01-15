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
ardurobotml_FSMClock = Class(name="ardurobotml::FSMClock")
ardurobotml_FSMEvent = Class(name="ardurobotml::FSMEvent")
RegionContainer = Class(name="RegionContainer")
ardurobotml_State = Class(name="ardurobotml::State")
ardurobotml_TimedSystem = Class(name="ardurobotml::TimedSystem")
NamedElement = Class(name="NamedElement")
ardurobotml_TFSM = Class(name="ardurobotml::TFSM")
ardurobotml_Guard = Class(name="ardurobotml::Guard", is_abstract=True)
ardurobotml_NamedElement = Class(name="ardurobotml::NamedElement")
ardurobotml_TemporalGuard = Class(name="ardurobotml::TemporalGuard")
Guard = Class(name="Guard")
ardurobotml_Transition = Class(name="ardurobotml::Transition")
ardurobotml_Action = Class(name="ardurobotml::Action", is_abstract=True)
ardurobotml_AllActionFinishedCondition = Class(name="ardurobotml::AllActionFinishedCondition")
Condition = Class(name="Condition")
ardurobotml_SystemPropertyCondition = Class(name="ardurobotml::SystemPropertyCondition")
ardurobotml_CollisionSensorCondition = Class(name="ardurobotml::CollisionSensorCondition")
ardurobotml_ActionSequence = Class(name="ardurobotml::ActionSequence")
Action = Class(name="Action")
ardurobotml_StopAction = Class(name="ardurobotml::StopAction")
ardurobotml_MoveForwardAction = Class(name="ardurobotml::MoveForwardAction")
ardurobotml_EventGuard = Class(name="ardurobotml::EventGuard")
ardurobotml_EvaluateGuard = Class(name="ardurobotml::EvaluateGuard")
ardurobotml_Condition = Class(name="ardurobotml::Condition", is_abstract=True)
ardurobotml_Region = Class(name="ardurobotml::Region")
ardurobotml_RegionContainer = Class(name="ardurobotml::RegionContainer", is_abstract=True)
ardurobotml_MoveForwardAndTurningLeftAction = Class(name="ardurobotml::MoveForwardAndTurningLeftAction")
ardurobotml_MoveBackardAndTurningRightAction = Class(name="ardurobotml::MoveBackardAndTurningRightAction")
ardurobotml_MoveBackardAction = Class(name="ardurobotml::MoveBackardAction")
ardurobotml_MoveForwardAndTurningRightAction = Class(name="ardurobotml::MoveForwardAndTurningRightAction")
ardurobotml_AcceleratetAction = Class(name="ardurobotml::AcceleratetAction")
ardurobotml_DeceleratetAction = Class(name="ardurobotml::DeceleratetAction")
ardurobotml_SCANCollisionAction = Class(name="ardurobotml::SCANCollisionAction")
ardurobotml_EmergencyStopAction = Class(name="ardurobotml::EmergencyStopAction")
ardurobotml_MoveBackardAndTurningLeftAction = Class(name="ardurobotml::MoveBackardAndTurningLeftAction")
ardurobotml_TurningLeftAction = Class(name="ardurobotml::TurningLeftAction")
ardurobotml_TurningRightAction = Class(name="ardurobotml::TurningRightAction")

# ardurobotml_FSMClock class attributes and methods
ardurobotml_FSMClock_value: Property = Property(name="value", type=IntegerType)
ardurobotml_FSMClock_m_ticks: Method = Method(name="ticks", parameters={})
ardurobotml_FSMClock.attributes={ardurobotml_FSMClock_value}
ardurobotml_FSMClock.methods={ardurobotml_FSMClock_m_ticks}

# ardurobotml_FSMEvent class attributes and methods

# RegionContainer class attributes and methods

# ardurobotml_State class attributes and methods
ardurobotml_State_m_onEnter: Method = Method(name="onEnter", parameters={}, type=StringType)
ardurobotml_State_m_onLeave: Method = Method(name="onLeave", parameters={}, type=StringType)
ardurobotml_State.methods={ardurobotml_State_m_onLeave, ardurobotml_State_m_onEnter}

# ardurobotml_TimedSystem class attributes and methods

# NamedElement class attributes and methods

# ardurobotml_TFSM class attributes and methods
ardurobotml_TFSM_m_initialize: Method = Method(name="initialize", parameters={}, type=StringType)
ardurobotml_TFSM.methods={ardurobotml_TFSM_m_initialize}

# ardurobotml_Guard class attributes and methods

# ardurobotml_NamedElement class attributes and methods
ardurobotml_NamedElement_name: Property = Property(name="name", type=StringType)
ardurobotml_NamedElement.attributes={ardurobotml_NamedElement_name}

# ardurobotml_TemporalGuard class attributes and methods
ardurobotml_TemporalGuard_afterDuration: Property = Property(name="afterDuration", type=IntegerType)
ardurobotml_TemporalGuard.attributes={ardurobotml_TemporalGuard_afterDuration}

# Guard class attributes and methods

# ardurobotml_Transition class attributes and methods
ardurobotml_Transition_m_fire: Method = Method(name="fire", parameters={}, type=StringType)
ardurobotml_Transition.methods={ardurobotml_Transition_m_fire}

# ardurobotml_Action class attributes and methods
ardurobotml_Action_m_begin: Method = Method(name="begin", parameters={})
ardurobotml_Action_m_end: Method = Method(name="end", parameters={})
ardurobotml_Action.methods={ardurobotml_Action_m_end, ardurobotml_Action_m_begin}

# ardurobotml_AllActionFinishedCondition class attributes and methods

# Condition class attributes and methods

# ardurobotml_SystemPropertyCondition class attributes and methods
ardurobotml_SystemPropertyCondition_expectedAttributeValue: Property = Property(name="expectedAttributeValue", type=BooleanType)
ardurobotml_SystemPropertyCondition.attributes={ardurobotml_SystemPropertyCondition_expectedAttributeValue}

# ardurobotml_CollisionSensorCondition class attributes and methods

# ardurobotml_ActionSequence class attributes and methods

# Action class attributes and methods

# ardurobotml_StopAction class attributes and methods

# ardurobotml_MoveForwardAction class attributes and methods
ardurobotml_MoveForwardAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveForwardAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveForwardAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveForwardAction.attributes={ardurobotml_MoveForwardAction_startTick, ardurobotml_MoveForwardAction_speed, ardurobotml_MoveForwardAction_duration}

# ardurobotml_EventGuard class attributes and methods

# ardurobotml_EvaluateGuard class attributes and methods

# ardurobotml_Condition class attributes and methods

# ardurobotml_Region class attributes and methods
ardurobotml_Region_name: Property = Property(name="name", type=StringType)
ardurobotml_Region.attributes={ardurobotml_Region_name}

# ardurobotml_RegionContainer class attributes and methods

# ardurobotml_MoveForwardAndTurningLeftAction class attributes and methods
ardurobotml_MoveForwardAndTurningLeftAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveForwardAndTurningLeftAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveForwardAndTurningLeftAction_diff: Property = Property(name="diff", type=IntegerType)
ardurobotml_MoveForwardAndTurningLeftAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveForwardAndTurningLeftAction.attributes={ardurobotml_MoveForwardAndTurningLeftAction_duration, ardurobotml_MoveForwardAndTurningLeftAction_speed, ardurobotml_MoveForwardAndTurningLeftAction_startTick, ardurobotml_MoveForwardAndTurningLeftAction_diff}

# ardurobotml_MoveBackardAndTurningRightAction class attributes and methods
ardurobotml_MoveBackardAndTurningRightAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveBackardAndTurningRightAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveBackardAndTurningRightAction_diff: Property = Property(name="diff", type=IntegerType)
ardurobotml_MoveBackardAndTurningRightAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveBackardAndTurningRightAction.attributes={ardurobotml_MoveBackardAndTurningRightAction_diff, ardurobotml_MoveBackardAndTurningRightAction_speed, ardurobotml_MoveBackardAndTurningRightAction_duration, ardurobotml_MoveBackardAndTurningRightAction_startTick}

# ardurobotml_MoveBackardAction class attributes and methods
ardurobotml_MoveBackardAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveBackardAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveBackardAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveBackardAction.attributes={ardurobotml_MoveBackardAction_speed, ardurobotml_MoveBackardAction_duration, ardurobotml_MoveBackardAction_startTick}

# ardurobotml_MoveForwardAndTurningRightAction class attributes and methods
ardurobotml_MoveForwardAndTurningRightAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveForwardAndTurningRightAction_diff: Property = Property(name="diff", type=IntegerType)
ardurobotml_MoveForwardAndTurningRightAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveForwardAndTurningRightAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveForwardAndTurningRightAction.attributes={ardurobotml_MoveForwardAndTurningRightAction_speed, ardurobotml_MoveForwardAndTurningRightAction_duration, ardurobotml_MoveForwardAndTurningRightAction_startTick, ardurobotml_MoveForwardAndTurningRightAction_diff}

# ardurobotml_AcceleratetAction class attributes and methods
ardurobotml_AcceleratetAction_ratio: Property = Property(name="ratio", type=IntegerType)
ardurobotml_AcceleratetAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_AcceleratetAction.attributes={ardurobotml_AcceleratetAction_ratio, ardurobotml_AcceleratetAction_startTick}

# ardurobotml_DeceleratetAction class attributes and methods
ardurobotml_DeceleratetAction_ratio: Property = Property(name="ratio", type=IntegerType)
ardurobotml_DeceleratetAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_DeceleratetAction.attributes={ardurobotml_DeceleratetAction_startTick, ardurobotml_DeceleratetAction_ratio}

# ardurobotml_SCANCollisionAction class attributes and methods

# ardurobotml_EmergencyStopAction class attributes and methods
ardurobotml_EmergencyStopAction_m_begin: Method = Method(name="begin", parameters={})
ardurobotml_EmergencyStopAction.methods={ardurobotml_EmergencyStopAction_m_begin}

# ardurobotml_MoveBackardAndTurningLeftAction class attributes and methods
ardurobotml_MoveBackardAndTurningLeftAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_MoveBackardAndTurningLeftAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_MoveBackardAndTurningLeftAction_diff: Property = Property(name="diff", type=IntegerType)
ardurobotml_MoveBackardAndTurningLeftAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_MoveBackardAndTurningLeftAction.attributes={ardurobotml_MoveBackardAndTurningLeftAction_speed, ardurobotml_MoveBackardAndTurningLeftAction_startTick, ardurobotml_MoveBackardAndTurningLeftAction_duration, ardurobotml_MoveBackardAndTurningLeftAction_diff}

# ardurobotml_TurningLeftAction class attributes and methods
ardurobotml_TurningLeftAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_TurningLeftAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_TurningLeftAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_TurningLeftAction.attributes={ardurobotml_TurningLeftAction_startTick, ardurobotml_TurningLeftAction_speed, ardurobotml_TurningLeftAction_duration}

# ardurobotml_TurningRightAction class attributes and methods
ardurobotml_TurningRightAction_duration: Property = Property(name="duration", type=IntegerType)
ardurobotml_TurningRightAction_startTick: Property = Property(name="startTick", type=IntegerType)
ardurobotml_TurningRightAction_speed: Property = Property(name="speed", type=IntegerType)
ardurobotml_TurningRightAction.attributes={ardurobotml_TurningRightAction_speed, ardurobotml_TurningRightAction_duration, ardurobotml_TurningRightAction_startTick}

# Relationships
tfsms0: BinaryAssociation = BinaryAssociation(
    name="tfsms0",
    ends={
        Property(name="ardurobotml_TimedSystem", type=ardurobotml_TFSM, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ardurobotml_TFSM", type=ardurobotml_TimedSystem, multiplicity=Multiplicity(1, 1))
    }
)
globalClocks1: BinaryAssociation = BinaryAssociation(
    name="globalClocks1",
    ends={
        Property(name="ardurobotml_FSMClock", type=ardurobotml_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TimedSystem2", type=ardurobotml_FSMClock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalEvents3: BinaryAssociation = BinaryAssociation(
    name="globalEvents3",
    ends={
        Property(name="ardurobotml_FSMEvent", type=ardurobotml_TimedSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TimedSystem4", type=ardurobotml_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState5: BinaryAssociation = BinaryAssociation(
    name="initialState5",
    ends={
        Property(name="ardurobotml_State", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TFSM6", type=ardurobotml_State, multiplicity=Multiplicity(1, 1))
    }
)
localEvents7: BinaryAssociation = BinaryAssociation(
    name="localEvents7",
    ends={
        Property(name="ardurobotml_FSMEvent9", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TFSM8", type=ardurobotml_FSMEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClock10: BinaryAssociation = BinaryAssociation(
    name="localClock10",
    ends={
        Property(name="ardurobotml_FSMClock12", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TFSM11", type=ardurobotml_FSMClock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="State26", type=ardurobotml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=ardurobotml_State, multiplicity=Multiplicity(1, 1))
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="State28", type=ardurobotml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=ardurobotml_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedGuard29: BinaryAssociation = BinaryAssociation(
    name="ownedGuard29",
    ends={
        Property(name="ardurobotml_Guard", type=ardurobotml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_Transition30", type=ardurobotml_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generatedEvents31: BinaryAssociation = BinaryAssociation(
    name="generatedEvents31",
    ends={
        Property(name="ardurobotml_FSMEvent33", type=ardurobotml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_Transition32", type=ardurobotml_FSMEvent, multiplicity=Multiplicity(0, 9999))
    }
)
onClock34: BinaryAssociation = BinaryAssociation(
    name="onClock34",
    ends={
        Property(name="ardurobotml_FSMClock35", type=ardurobotml_TemporalGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TemporalGuard", type=ardurobotml_FSMClock, multiplicity=Multiplicity(1, 1))
    }
)
ownedTransitions13: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions13",
    ends={
        Property(name="ardurobotml_Transition", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TFSM14", type=ardurobotml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState15: BinaryAssociation = BinaryAssociation(
    name="currentState15",
    ends={
        Property(name="ardurobotml_State17", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_TFSM16", type=ardurobotml_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedStates18: BinaryAssociation = BinaryAssociation(
    name="ownedStates18",
    ends={
        Property(name="State", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=ardurobotml_State, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions19: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions19",
    ends={
        Property(name="Transition", type=ardurobotml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ardurobotml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions20: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions20",
    ends={
        Property(name="Transition21", type=ardurobotml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ardurobotml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
actions22: BinaryAssociation = BinaryAssociation(
    name="actions22",
    ends={
        Property(name="ardurobotml_Action", type=ardurobotml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_State23", type=ardurobotml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM24: BinaryAssociation = BinaryAssociation(
    name="owningFSM24",
    ends={
        Property(name="TFSM", type=ardurobotml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=ardurobotml_TFSM, multiplicity=Multiplicity(1, 1))
    }
)
ownedRegions44: BinaryAssociation = BinaryAssociation(
    name="ownedRegions44",
    ends={
        Property(name="ardurobotml_Region45", type=ardurobotml_RegionContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_RegionContainer", type=ardurobotml_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions46: BinaryAssociation = BinaryAssociation(
    name="actions46",
    ends={
        Property(name="ardurobotml_Action47", type=ardurobotml_ActionSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_ActionSequence", type=ardurobotml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggeringEvent36: BinaryAssociation = BinaryAssociation(
    name="triggeringEvent36",
    ends={
        Property(name="ardurobotml_FSMEvent37", type=ardurobotml_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_EventGuard", type=ardurobotml_FSMEvent, multiplicity=Multiplicity(1, 1))
    }
)
sollicitingTransitions38: BinaryAssociation = BinaryAssociation(
    name="sollicitingTransitions38",
    ends={
        Property(name="ardurobotml_Transition40", type=ardurobotml_FSMEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_FSMEvent39", type=ardurobotml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="ardurobotml_Condition", type=ardurobotml_EvaluateGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_EvaluateGuard", type=ardurobotml_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedStates42: BinaryAssociation = BinaryAssociation(
    name="ownedStates42",
    ends={
        Property(name="ardurobotml_State43", type=ardurobotml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ardurobotml_Region", type=ardurobotml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ardurobotml_TFSM_RegionContainer = Generalization(general=RegionContainer, specific=ardurobotml_TFSM)
gen_ardurobotml_TimedSystem_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_TimedSystem)
gen_ardurobotml_Guard_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_Guard)
gen_ardurobotml_TemporalGuard_Guard = Generalization(general=Guard, specific=ardurobotml_TemporalGuard)
gen_ardurobotml_State_RegionContainer = Generalization(general=RegionContainer, specific=ardurobotml_State)
gen_ardurobotml_Transition_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_Transition)
gen_ardurobotml_Action_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_Action)
gen_ardurobotml_AllActionFinishedCondition_Condition = Generalization(general=Condition, specific=ardurobotml_AllActionFinishedCondition)
gen_ardurobotml_SystemPropertyCondition_Condition = Generalization(general=Condition, specific=ardurobotml_SystemPropertyCondition)
gen_ardurobotml_CollisionSensorCondition_Condition = Generalization(general=Condition, specific=ardurobotml_CollisionSensorCondition)
gen_ardurobotml_ActionSequence_Action = Generalization(general=Action, specific=ardurobotml_ActionSequence)
gen_ardurobotml_StopAction_Action = Generalization(general=Action, specific=ardurobotml_StopAction)
gen_ardurobotml_MoveForwardAction_Action = Generalization(general=Action, specific=ardurobotml_MoveForwardAction)
gen_ardurobotml_EventGuard_Guard = Generalization(general=Guard, specific=ardurobotml_EventGuard)
gen_ardurobotml_FSMEvent_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_FSMEvent)
gen_ardurobotml_FSMClock_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_FSMClock)
gen_ardurobotml_EvaluateGuard_Guard = Generalization(general=Guard, specific=ardurobotml_EvaluateGuard)
gen_ardurobotml_RegionContainer_NamedElement = Generalization(general=NamedElement, specific=ardurobotml_RegionContainer)
gen_ardurobotml_MoveForwardAndTurningLeftAction_Action = Generalization(general=Action, specific=ardurobotml_MoveForwardAndTurningLeftAction)
gen_ardurobotml_MoveBackardAndTurningRightAction_Action = Generalization(general=Action, specific=ardurobotml_MoveBackardAndTurningRightAction)
gen_ardurobotml_MoveBackardAction_Action = Generalization(general=Action, specific=ardurobotml_MoveBackardAction)
gen_ardurobotml_MoveForwardAndTurningRightAction_Action = Generalization(general=Action, specific=ardurobotml_MoveForwardAndTurningRightAction)
gen_ardurobotml_AcceleratetAction_Action = Generalization(general=Action, specific=ardurobotml_AcceleratetAction)
gen_ardurobotml_DeceleratetAction_Action = Generalization(general=Action, specific=ardurobotml_DeceleratetAction)
gen_ardurobotml_SCANCollisionAction_Action = Generalization(general=Action, specific=ardurobotml_SCANCollisionAction)
gen_ardurobotml_EmergencyStopAction_Action = Generalization(general=Action, specific=ardurobotml_EmergencyStopAction)
gen_ardurobotml_MoveBackardAndTurningLeftAction_Action = Generalization(general=Action, specific=ardurobotml_MoveBackardAndTurningLeftAction)
gen_ardurobotml_TurningLeftAction_Action = Generalization(general=Action, specific=ardurobotml_TurningLeftAction)
gen_ardurobotml_TurningRightAction_Action = Generalization(general=Action, specific=ardurobotml_TurningRightAction)

# Domain Model
domain_model = DomainModel(
    name="ardurobotml",
    types={ardurobotml_FSMClock, ardurobotml_FSMEvent, RegionContainer, ardurobotml_State, ardurobotml_TimedSystem, NamedElement, ardurobotml_TFSM, ardurobotml_Guard, ardurobotml_NamedElement, ardurobotml_TemporalGuard, Guard, ardurobotml_Transition, ardurobotml_Action, ardurobotml_AllActionFinishedCondition, Condition, ardurobotml_SystemPropertyCondition, ardurobotml_CollisionSensorCondition, ardurobotml_ActionSequence, Action, ardurobotml_StopAction, ardurobotml_MoveForwardAction, ardurobotml_EventGuard, ardurobotml_EvaluateGuard, ardurobotml_Condition, ardurobotml_Region, ardurobotml_RegionContainer, ardurobotml_MoveForwardAndTurningLeftAction, ardurobotml_MoveBackardAndTurningRightAction, ardurobotml_MoveBackardAction, ardurobotml_MoveForwardAndTurningRightAction, ardurobotml_AcceleratetAction, ardurobotml_DeceleratetAction, ardurobotml_SCANCollisionAction, ardurobotml_EmergencyStopAction, ardurobotml_MoveBackardAndTurningLeftAction, ardurobotml_TurningLeftAction, ardurobotml_TurningRightAction},
    associations={tfsms0, globalClocks1, globalEvents3, initialState5, localEvents7, localClock10, source25, target27, ownedGuard29, generatedEvents31, onClock34, ownedTransitions13, currentState15, ownedStates18, outgoingTransitions19, incomingTransitions20, actions22, owningFSM24, ownedRegions44, actions46, triggeringEvent36, sollicitingTransitions38, condition41, ownedStates42},
    generalizations={gen_ardurobotml_TFSM_RegionContainer, gen_ardurobotml_TimedSystem_NamedElement, gen_ardurobotml_Guard_NamedElement, gen_ardurobotml_TemporalGuard_Guard, gen_ardurobotml_State_RegionContainer, gen_ardurobotml_Transition_NamedElement, gen_ardurobotml_Action_NamedElement, gen_ardurobotml_AllActionFinishedCondition_Condition, gen_ardurobotml_SystemPropertyCondition_Condition, gen_ardurobotml_CollisionSensorCondition_Condition, gen_ardurobotml_ActionSequence_Action, gen_ardurobotml_StopAction_Action, gen_ardurobotml_MoveForwardAction_Action, gen_ardurobotml_EventGuard_Guard, gen_ardurobotml_FSMEvent_NamedElement, gen_ardurobotml_FSMClock_NamedElement, gen_ardurobotml_EvaluateGuard_Guard, gen_ardurobotml_RegionContainer_NamedElement, gen_ardurobotml_MoveForwardAndTurningLeftAction_Action, gen_ardurobotml_MoveBackardAndTurningRightAction_Action, gen_ardurobotml_MoveBackardAction_Action, gen_ardurobotml_MoveForwardAndTurningRightAction_Action, gen_ardurobotml_AcceleratetAction_Action, gen_ardurobotml_DeceleratetAction_Action, gen_ardurobotml_SCANCollisionAction_Action, gen_ardurobotml_EmergencyStopAction_Action, gen_ardurobotml_MoveBackardAndTurningLeftAction_Action, gen_ardurobotml_TurningLeftAction_Action, gen_ardurobotml_TurningRightAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)