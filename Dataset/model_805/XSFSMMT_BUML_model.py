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
fsm_State = Class(name="fsm_State")
fsm_Transition = Class(name="fsm_Transition")
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_NamedElement = Class(name="fsm_NamedElement", is_abstract=True)

# fsm_State class attributes and methods
fsm_State_m_step: Method = Method(name="step", parameters={Parameter(name='fsm_inputString', type=StringType)})
fsm_State.methods={fsm_State_m_step}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition.attributes={fsm_Transition_output, fsm_Transition_input}
fsm_Transition.methods={fsm_Transition_m_fire}

# fsm_StateMachine class attributes and methods
fsm_StateMachine_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
fsm_StateMachine_consummedString: Property = Property(name="consummedString", type=StringType)
fsm_StateMachine_producedString: Property = Property(name="producedString", type=StringType)
fsm_StateMachine_m_main: Method = Method(name="main", parameters={})
fsm_StateMachine_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='fsm_args', type=StringType)})
fsm_StateMachine.attributes={fsm_StateMachine_producedString, fsm_StateMachine_unprocessedString, fsm_StateMachine_consummedString}
fsm_StateMachine.methods={fsm_StateMachine_m_initializeModel, fsm_StateMachine_m_main}

# NamedElement class attributes and methods

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
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="State14", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State, fsm_Transition, fsm_StateMachine, NamedElement, fsm_NamedElement},
    associations={ownedStates0, initialState1, ownedTransitions2, currentState4, owningFSM7, outgoingTransitions8, incomingTransitions9, source11, target13},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_State_NamedElement, gen_fsm_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)