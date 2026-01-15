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
fsm_StateMachine = Class(name="fsm::StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_NamedElement = Class(name="fsm::NamedElement", is_abstract=True)
fsm_Buffer = Class(name="fsm::Buffer")
fsm_FSMSystem = Class(name="fsm::FSMSystem")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_Buffer class attributes and methods
fsm_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
fsm_Buffer.attributes={fsm_Buffer_initialValue}

# fsm_FSMSystem class attributes and methods

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="fsm_State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedTransitions3: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions3",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine4", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="7", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions8: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions8",
    ends={
        Property(name="10", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions11: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions11",
    ends={
        Property(name="13", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="16", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="19", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedStateMachines20: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachines20",
    ends={
        Property(name="fsm_StateMachine21", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffer22: BinaryAssociation = BinaryAssociation(
    name="ownedBuffer22",
    ends={
        Property(name="fsm_Buffer", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem23", type=fsm_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs24: BinaryAssociation = BinaryAssociation(
    name="inputs24",
    ends={
        Property(name="fsm_StateMachine26", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer25", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
outputs27: BinaryAssociation = BinaryAssociation(
    name="outputs27",
    ends={
        Property(name="fsm_StateMachine29", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer28", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_FSMSystem_NamedElement = Generalization(general=NamedElement, specific=fsm_FSMSystem)
gen_fsm_Buffer_NamedElement = Generalization(general=NamedElement, specific=fsm_Buffer)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_NamedElement, fsm_Buffer, fsm_FSMSystem},
    associations={ownedStates0, initialState2, ownedTransitions3, owningFSM5, outgoingTransitions8, incomingTransitions11, source14, target17, ownedStateMachines20, ownedBuffer22, inputs24, outputs27},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_State_NamedElement, gen_fsm_Transition_NamedElement, gen_fsm_FSMSystem_NamedElement, gen_fsm_Buffer_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)