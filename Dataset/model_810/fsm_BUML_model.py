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
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm_State")
fsm_Transition = Class(name="fsm_Transition")
fsm_FSMSystem = Class(name="fsm_FSMSystem")
fsm_Buffer = Class(name="fsm_Buffer")
fsm_NamedElement = Class(name="fsm_NamedElement", is_abstract=True)

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}

# fsm_FSMSystem class attributes and methods

# fsm_Buffer class attributes and methods
fsm_Buffer_initialValue: Property = Property(name="initialValue", type=StringType)
fsm_Buffer.attributes={fsm_Buffer_initialValue}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# Relationships
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
ownedTransitions2: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions2",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM4: BinaryAssociation = BinaryAssociation(
    name="owningFSM4",
    ends={
        Property(name="StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions5: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions5",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions6: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions6",
    ends={
        Property(name="Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStateMachines12: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachines12",
    ends={
        Property(name="fsm_StateMachine13", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBuffer14: BinaryAssociation = BinaryAssociation(
    name="ownedBuffer14",
    ends={
        Property(name="fsm_Buffer", type=fsm_FSMSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMSystem15", type=fsm_Buffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs16: BinaryAssociation = BinaryAssociation(
    name="inputs16",
    ends={
        Property(name="fsm_StateMachine18", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer17", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
outputs19: BinaryAssociation = BinaryAssociation(
    name="outputs19",
    ends={
        Property(name="fsm_StateMachine21", type=fsm_Buffer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Buffer20", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="State9", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
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
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_FSMSystem, fsm_Buffer, fsm_NamedElement},
    associations={ownedStates0, initialState1, ownedTransitions2, owningFSM4, outgoingTransitions5, incomingTransitions6, ownedStateMachines12, ownedBuffer14, inputs16, outputs19, source8, target10},
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