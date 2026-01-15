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
fsm_FSM.attributes={fsm_FSM_consummedString, fsm_FSM_name, fsm_FSM_underProcessTrigger}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_trigger: Property = Property(name="trigger", type=StringType)
fsm_Transition_action: Property = Property(name="action", type=StringType)
fsm_Transition.attributes={fsm_Transition_action, fsm_Transition_name, fsm_Transition_trigger}

# fsm_Buffer class attributes and methods
fsm_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
fsm_Buffer_name: Property = Property(name="name", type=StringType)
fsm_Buffer_currentValues: Property = Property(name="currentValues", type=StringType)
fsm_Buffer.attributes={fsm_Buffer_name, fsm_Buffer_initialValue, fsm_Buffer_currentValues}

# fsm_System class attributes and methods

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions1: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions1",
    ends={
        Property(name="Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputBuffer3: BinaryAssociation = BinaryAssociation(
    name="inputBuffer3",
    ends={
        Property(name="Buffer", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingFSM", type=fsm_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
outputBuffer4: BinaryAssociation = BinaryAssociation(
    name="outputBuffer4",
    ends={
        Property(name="Buffer5", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingFSM", type=fsm_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
initialState6: BinaryAssociation = BinaryAssociation(
    name="initialState6",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
currentState7: BinaryAssociation = BinaryAssociation(
    name="currentState7",
    ends={
        Property(name="fsm_State9", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM8", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming10: BinaryAssociation = BinaryAssociation(
    name="incoming10",
    ends={
        Property(name="Transition11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="Transition13", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm14: BinaryAssociation = BinaryAssociation(
    name="fsm14",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
outgoingFSM15: BinaryAssociation = BinaryAssociation(
    name="outgoingFSM15",
    ends={
        Property(name="FSM16", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="inputBuffer", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
incomingFSM17: BinaryAssociation = BinaryAssociation(
    name="incomingFSM17",
    ends={
        Property(name="FSM18", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="outputBuffer", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
tgt19: BinaryAssociation = BinaryAssociation(
    name="tgt19",
    ends={
        Property(name="State20", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
src21: BinaryAssociation = BinaryAssociation(
    name="src21",
    ends={
        Property(name="State22", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
fsm23: BinaryAssociation = BinaryAssociation(
    name="fsm23",
    ends={
        Property(name="FSM24", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransitions", type=fsm_FSM, multiplicity=Multiplicity(0, 1))
    }
)
ownedFsms25: BinaryAssociation = BinaryAssociation(
    name="ownedFsms25",
    ends={
        Property(name="fsm_FSM26", type=fsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_System", type=fsm_FSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffers27: BinaryAssociation = BinaryAssociation(
    name="ownedBuffers27",
    ends={
        Property(name="fsm_Buffer", type=fsm_System, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_System28", type=fsm_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_Buffer, fsm_System},
    associations={ownedStates0, ownedTransitions1, inputBuffer3, outputBuffer4, initialState6, currentState7, incoming10, outgoing12, fsm14, outgoingFSM15, incomingFSM17, tgt19, src21, fsm23, ownedFsms25, ownedBuffers27},
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