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
model_FSM = Class(name="model::FSM")
model_State = Class(name="model::State")
model_Transition = Class(name="model::Transition")
model_Buffer = Class(name="model::Buffer")
model_System = Class(name="model::System")

# model_FSM class attributes and methods
model_FSM_name: Property = Property(name="name", type=StringType)
model_FSM_m_run: Method = Method(name="run", parameters={})
model_FSM.attributes={model_FSM_name}
model_FSM.methods={model_FSM_m_run}

# model_State class attributes and methods
model_State_name: Property = Property(name="name", type=StringType)
model_State.attributes={model_State_name}

# model_Transition class attributes and methods
model_Transition_name: Property = Property(name="name", type=StringType)
model_Transition_trigger: Property = Property(name="trigger", type=StringType)
model_Transition_action: Property = Property(name="action", type=StringType)
model_Transition.attributes={model_Transition_action, model_Transition_trigger, model_Transition_name}

# model_Buffer class attributes and methods
model_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
model_Buffer_name: Property = Property(name="name", type=StringType)
model_Buffer.attributes={model_Buffer_initialValue, model_Buffer_name}

# model_System class attributes and methods

# Relationships
inputBuffer3: BinaryAssociation = BinaryAssociation(
    name="inputBuffer3",
    ends={
        Property(name="Buffer", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingFSM", type=model_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=model_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions1: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions1",
    ends={
        Property(name="Transition", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm2", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputBuffer4: BinaryAssociation = BinaryAssociation(
    name="outputBuffer4",
    ends={
        Property(name="Buffer5", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingFSM", type=model_Buffer, multiplicity=Multiplicity(0, 1))
    }
)
initialState6: BinaryAssociation = BinaryAssociation(
    name="initialState6",
    ends={
        Property(name="model_State", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FSM", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Transition8", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing9: BinaryAssociation = BinaryAssociation(
    name="outgoing9",
    ends={
        Property(name="Transition10", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm11: BinaryAssociation = BinaryAssociation(
    name="fsm11",
    ends={
        Property(name="FSM", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)
outgoingFSM12: BinaryAssociation = BinaryAssociation(
    name="outgoingFSM12",
    ends={
        Property(name="FSM13", type=model_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="inputBuffer", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)
incomingFSM14: BinaryAssociation = BinaryAssociation(
    name="incomingFSM14",
    ends={
        Property(name="FSM15", type=model_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="outputBuffer", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)
tgt16: BinaryAssociation = BinaryAssociation(
    name="tgt16",
    ends={
        Property(name="State17", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="State19", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
fsm20: BinaryAssociation = BinaryAssociation(
    name="fsm20",
    ends={
        Property(name="FSM21", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransitions", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)
ownedFsms22: BinaryAssociation = BinaryAssociation(
    name="ownedFsms22",
    ends={
        Property(name="model_FSM23", type=model_System, multiplicity=Multiplicity(1, 1)),
        Property(name="model_System", type=model_FSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffers24: BinaryAssociation = BinaryAssociation(
    name="ownedBuffers24",
    ends={
        Property(name="model_Buffer", type=model_System, multiplicity=Multiplicity(1, 1)),
        Property(name="model_System25", type=model_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_FSM, model_State, model_Transition, model_Buffer, model_System},
    associations={inputBuffer3, ownedStates0, ownedTransitions1, outputBuffer4, initialState6, incoming7, outgoing9, fsm11, outgoingFSM12, incomingFSM14, tgt16, src18, fsm20, ownedFsms22, ownedBuffers24},
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