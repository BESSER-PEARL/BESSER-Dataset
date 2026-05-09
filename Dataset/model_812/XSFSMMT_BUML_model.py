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
fsm_Transition = Class(name="fsm_Transition")
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm_State")
fsm_NamedElement = Class(name="fsm_NamedElement", is_abstract=True)
fsm_FSMSystem = Class(name="fsm_FSMSystem")
fsm_Buffer = Class(name="fsm_Buffer")

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}
fsm_Transition.methods={fsm_Transition_m_fire}

# fsm_StateMachine class attributes and methods
fsm_StateMachine_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
fsm_StateMachine_consummedString: Property = Property(name="consummedString", type=StringType)
fsm_StateMachine_producedString: Property = Property(name="producedString", type=StringType)
fsm_StateMachine_m_run: Method = Method(name="run", parameters={})
fsm_StateMachine_m_initializeModel: Method = Method(name="initializeModel", parameters={})
fsm_StateMachine.attributes={fsm_StateMachine_producedString, fsm_StateMachine_unprocessedString, fsm_StateMachine_consummedString}
fsm_StateMachine.methods={fsm_StateMachine_m_run, fsm_StateMachine_m_initializeModel}

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_m_step: Method = Method(name="step", parameters={Parameter(name='fsm_inputString', type=StringType)})
fsm_State.methods={fsm_State_m_step}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_FSMSystem class attributes and methods
fsm_FSMSystem_m_initialize: Method = Method(name="initialize", parameters={})
fsm_FSMSystem.methods={fsm_FSMSystem_m_initialize}

# fsm_Buffer class attributes and methods
fsm_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
fsm_Buffer_currentValues: Property = Property(name="currentValues", type=StringType)
fsm_Buffer_m_enqueue: Method = Method(name="enqueue", parameters={Parameter(name='fsm_v', type=StringType)})
fsm_Buffer_m_dequeue: Method = Method(name="dequeue", parameters={})
fsm_Buffer_m_initialize: Method = Method(name="initialize", parameters={})
fsm_Buffer.attributes={fsm_Buffer_initialValue, fsm_Buffer_currentValues}
fsm_Buffer.methods={fsm_Buffer_m_initialize, fsm_Buffer_m_enqueue, fsm_Buffer_m_dequeue}

# Relationships
ownedTransitions2: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions2",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState4: BinaryAssociation = BinaryAssociation(
    name="currentState4",
    ends={
        Property(name="fsm_State6", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine5", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM7: BinaryAssociation = BinaryAssociation(
    name="owningFSM7",
    ends={
        Property(name="StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions8: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions8",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions9: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions9",
    ends={
        Property(name="Transition10", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="State12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
inputs19: BinaryAssociation = BinaryAssociation(
    name="inputs19",
    ends={
        Property(name="fsm_StateMachine21", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer20", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
outputs22: BinaryAssociation = BinaryAssociation(
    name="outputs22",
    ends={
        Property(name="fsm_StateMachine24", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer23", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="State14", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedStateMachines15: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachines15",
    ends={
        Property(name="fsm_StateMachine16", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffer17: BinaryAssociation = BinaryAssociation(
    name="ownedBuffer17",
    ends={
        Property(name="fsm_Buffer", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem18", type=fsm_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_FSMSystem_NamedElement = Generalization(general=NamedElement, specific=fsm_FSMSystem)
gen_fsm_Buffer_NamedElement = Generalization(general=NamedElement, specific=fsm_Buffer)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, fsm_StateMachine, NamedElement, fsm_State, fsm_NamedElement, fsm_FSMSystem, fsm_Buffer},
    associations={ownedTransitions2, currentState4, owningFSM7, outgoingTransitions8, incomingTransitions9, source11, ownedStates0, initialState1, inputs19, outputs22, target13, ownedStateMachines15, ownedBuffer17},
    generalizations={gen_fsm_State_NamedElement, gen_fsm_Transition_NamedElement, gen_fsm_StateMachine_NamedElement, gen_fsm_FSMSystem_NamedElement, gen_fsm_Buffer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)