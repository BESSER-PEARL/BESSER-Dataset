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
fsm_Transition = Class(name="fsm::Transition")
fsm_FSM = Class(name="fsm::FSM")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm::State")
fsm_NamedElement = Class(name="fsm::NamedElement")

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_letterToMatch: Property = Property(name="letterToMatch", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition_m_evaluateGuard: Method = Method(name="evaluateGuard", parameters={}, type=BooleanType)
fsm_Transition_m_callEffect: Method = Method(name="callEffect", parameters={})
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output, fsm_Transition_letterToMatch}
fsm_Transition.methods={fsm_Transition_m_evaluateGuard, fsm_Transition_m_callEffect, fsm_Transition_m_fire}

# fsm_FSM class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_m_onEnter: Method = Method(name="onEnter", parameters={})
fsm_State_m_onLeave: Method = Method(name="onLeave", parameters={})
fsm_State.methods={fsm_State_m_onLeave, fsm_State_m_onEnter}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
currentState2: BinaryAssociation = BinaryAssociation(
    name="currentState2",
    ends={
        Property(name="fsm_State4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM3", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="Transition8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State10", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_FSM_NamedElement = Generalization(general=NamedElement, specific=fsm_FSM)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, fsm_FSM, NamedElement, fsm_State, fsm_NamedElement},
    associations={ownedState0, initialState1, currentState2, owningFSM5, outgoingTransition6, incomingTransition7, source9, target11},
    generalizations={gen_fsm_State_NamedElement, gen_fsm_FSM_NamedElement, gen_fsm_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)