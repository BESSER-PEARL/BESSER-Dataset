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
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_Buffer = Class(name="fsm::Buffer")
fsm_System = Class(name="fsm::System")

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM_underProcessTrigger: Property = Property(name="underProcessTrigger", type=StringType)
fsm_FSM_consummedString: Property = Property(name="consummedString", type=StringType)
fsm_FSM.attributes={fsm_FSM_consummedString, fsm_FSM_underProcessTrigger, fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_trigger: Property = Property(name="trigger", type=StringType)
fsm_Transition_action: Property = Property(name="action", type=StringType)
fsm_Transition.attributes={fsm_Transition_trigger, fsm_Transition_name, fsm_Transition_action}

# fsm_Buffer class attributes and methods
fsm_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
fsm_Buffer_name: Property = Property(name="name", type=StringType)
fsm_Buffer_currentValues: Property = Property(name="currentValues", type=StringType)
fsm_Buffer.attributes={fsm_Buffer_currentValues, fsm_Buffer_name, fsm_Buffer_initialValue}

# fsm_System class attributes and methods

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions2: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions2",
    ends={
        Property(name="4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputBuffer5: BinaryAssociation = BinaryAssociation(
    name="inputBuffer5",
    ends={
        Property(name="7", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsm_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
outputBuffer8: BinaryAssociation = BinaryAssociation(
    name="outputBuffer8",
    ends={
        Property(name="10", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsm_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
initialState11: BinaryAssociation = BinaryAssociation(
    name="initialState11",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
currentState12: BinaryAssociation = BinaryAssociation(
    name="currentState12",
    ends={
        Property(name="fsm_State14", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM13", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="17", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing18: BinaryAssociation = BinaryAssociation(
    name="outgoing18",
    ends={
        Property(name="20", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm21: BinaryAssociation = BinaryAssociation(
    name="fsm21",
    ends={
        Property(name="23", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
outgoingFSM24: BinaryAssociation = BinaryAssociation(
    name="outgoingFSM24",
    ends={
        Property(name="26", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
incomingFSM27: BinaryAssociation = BinaryAssociation(
    name="incomingFSM27",
    ends={
        Property(name="29", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
tgt30: BinaryAssociation = BinaryAssociation(
    name="tgt30",
    ends={
        Property(name="32", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="31", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
src33: BinaryAssociation = BinaryAssociation(
    name="src33",
    ends={
        Property(name="35", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="34", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
fsm36: BinaryAssociation = BinaryAssociation(
    name="fsm36",
    ends={
        Property(name="37", type=fsm_FSM, multiplicity=Multiplicity(0, 1)),
        Property(name="38", type=fsm_Transition, multiplicity=Multiplicity(1, 1))
    }
)
ownedFsms39: BinaryAssociation = BinaryAssociation(
    name="ownedFsms39",
    ends={
        Property(name="fsm_FSM40", type=fsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_System", type=fsm_FSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffers41: BinaryAssociation = BinaryAssociation(
    name="ownedBuffers41",
    ends={
        Property(name="fsm_Buffer", type=fsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_System42", type=fsm_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_Buffer, fsm_System},
    associations={ownedStates0, ownedTransitions2, inputBuffer5, outputBuffer8, initialState11, currentState12, incoming15, outgoing18, fsm21, outgoingFSM24, incomingFSM27, tgt30, src33, fsm36, ownedFsms39, ownedBuffers41},
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