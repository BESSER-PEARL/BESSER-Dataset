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

# fsm_StateMachine class attributes and methods
fsm_StateMachine_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
fsm_StateMachine_consummedString: Property = Property(name="consummedString", type=StringType)
fsm_StateMachine_producedString: Property = Property(name="producedString", type=StringType)
fsm_StateMachine_m_main: Method = Method(name="main", parameters={})
fsm_StateMachine_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
fsm_StateMachine.attributes={fsm_StateMachine_consummedString, fsm_StateMachine_unprocessedString, fsm_StateMachine_producedString}
fsm_StateMachine.methods={fsm_StateMachine_m_main, fsm_StateMachine_m_initializeModel}

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_m_step: Method = Method(name="step", parameters={Parameter(name='inputString')})
fsm_State.methods={fsm_State_m_step}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}
fsm_Transition.methods={fsm_Transition_m_fire}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

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
currentState5: BinaryAssociation = BinaryAssociation(
    name="currentState5",
    ends={
        Property(name="fsm_State7", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine6", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions11: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions11",
    ends={
        Property(name="13", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions14: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions14",
    ends={
        Property(name="16", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="22", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM8: BinaryAssociation = BinaryAssociation(
    name="owningFSM8",
    ends={
        Property(name="10", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_NamedElement},
    associations={ownedStates0, initialState2, ownedTransitions3, currentState5, outgoingTransitions11, incomingTransitions14, source17, target20, owningFSM8},
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