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
fsm_Event = Class(name="fsm::Event")
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Action = Class(name="fsm::Action")
fsm_Guard = Class(name="fsm::Guard")
fsm_Message = Class(name="fsm::Message")
fsm_StringToStringMap = Class(name="fsm::StringToStringMap")
fsm_Transition = Class(name="fsm::Transition")

# fsm_Event class attributes and methods
fsm_Event_name: Property = Property(name="name", type=StringType)
fsm_Event.attributes={fsm_Event_name}

# fsm_FSM class attributes and methods
fsm_FSM_isServer: Property = Property(name="isServer", type=BooleanType)
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM_groupId: Property = Property(name="groupId", type=StringType)
fsm_FSM.attributes={fsm_FSM_groupId, fsm_FSM_name, fsm_FSM_isServer}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Action class attributes and methods
fsm_Action_name: Property = Property(name="name", type=StringType)
fsm_Action.attributes={fsm_Action_name}

# fsm_Guard class attributes and methods
fsm_Guard_name: Property = Property(name="name", type=StringType)
fsm_Guard.attributes={fsm_Guard_name}

# fsm_Message class attributes and methods
fsm_Message_name: Property = Property(name="name", type=StringType)
fsm_Message.attributes={fsm_Message_name}

# fsm_StringToStringMap class attributes and methods
fsm_StringToStringMap_key: Property = Property(name="key", type=StringType)
fsm_StringToStringMap_value: Property = Property(name="value", type=StringType)
fsm_StringToStringMap.attributes={fsm_StringToStringMap_key, fsm_StringToStringMap_value}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_InverseGuard: Property = Property(name="InverseGuard", type=BooleanType)
fsm_Transition.attributes={fsm_Transition_InverseGuard, fsm_Transition_name}

# Relationships
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="fsm_State4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM3", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedEvents5: BinaryAssociation = BinaryAssociation(
    name="ownedEvents5",
    ends={
        Property(name="fsm_Event", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM6", type=fsm_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="State29", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
actions30: BinaryAssociation = BinaryAssociation(
    name="actions30",
    ends={
        Property(name="fsm_Action31", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Action, multiplicity=Multiplicity(0, 9999))
    }
)
guard32: BinaryAssociation = BinaryAssociation(
    name="guard32",
    ends={
        Property(name="fsm_Guard34", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition33", type=fsm_Guard, multiplicity=Multiplicity(0, 1))
    }
)
ownedActions7: BinaryAssociation = BinaryAssociation(
    name="ownedActions7",
    ends={
        Property(name="fsm_Action", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM8", type=fsm_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedGuards9: BinaryAssociation = BinaryAssociation(
    name="ownedGuards9",
    ends={
        Property(name="fsm_Guard", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM10", type=fsm_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMessages11: BinaryAssociation = BinaryAssociation(
    name="ownedMessages11",
    ends={
        Property(name="fsm_Message", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM12", type=fsm_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes13: BinaryAssociation = BinaryAssociation(
    name="dataTypes13",
    ends={
        Property(name="fsm_StringToStringMap", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM14", type=fsm_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM15: BinaryAssociation = BinaryAssociation(
    name="owningFSM15",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions16: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions16",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions17: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions17",
    ends={
        Property(name="Transition18", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
onEnteredActions19: BinaryAssociation = BinaryAssociation(
    name="onEnteredActions19",
    ends={
        Property(name="fsm_Action21", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State20", type=fsm_Action, multiplicity=Multiplicity(0, 9999))
    }
)
onExitedActions22: BinaryAssociation = BinaryAssociation(
    name="onExitedActions22",
    ends={
        Property(name="fsm_Action24", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State23", type=fsm_Action, multiplicity=Multiplicity(0, 9999))
    }
)
expectedMessage25: BinaryAssociation = BinaryAssociation(
    name="expectedMessage25",
    ends={
        Property(name="fsm_Message27", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State26", type=fsm_Message, multiplicity=Multiplicity(0, 1))
    }
)
event35: BinaryAssociation = BinaryAssociation(
    name="event35",
    ends={
        Property(name="fsm_Event37", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition36", type=fsm_Event, multiplicity=Multiplicity(1, 1))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="State39", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
event40: BinaryAssociation = BinaryAssociation(
    name="event40",
    ends={
        Property(name="fsm_Event42", type=fsm_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Message41", type=fsm_Event, multiplicity=Multiplicity(1, 1))
    }
)
data43: BinaryAssociation = BinaryAssociation(
    name="data43",
    ends={
        Property(name="fsm_StringToStringMap45", type=fsm_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Message44", type=fsm_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumsDef46: BinaryAssociation = BinaryAssociation(
    name="enumsDef46",
    ends={
        Property(name="fsm_StringToStringMap48", type=fsm_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Message47", type=fsm_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Event, fsm_FSM, fsm_State, fsm_Action, fsm_Guard, fsm_Message, fsm_StringToStringMap, fsm_Transition},
    associations={initialState1, finalState2, ownedEvents5, ownedStates0, source28, actions30, guard32, ownedActions7, ownedGuards9, ownedMessages11, dataTypes13, owningFSM15, outgoingTransitions16, incomingTransitions17, onEnteredActions19, onExitedActions22, expectedMessage25, event35, target38, event40, data43, enumsDef46},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)