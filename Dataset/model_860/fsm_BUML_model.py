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
fsm_NamedElement = Class(name="fsm::NamedElement")
fsm_StateMachine = Class(name="fsm::StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_InitialState = Class(name="fsm::InitialState")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_TimedTransition = Class(name="fsm::TimedTransition")
Transition = Class(name="Transition")
fsm_Pseudostate = Class(name="fsm::Pseudostate")
fsm_Fork = Class(name="fsm::Fork")
Pseudostate = Class(name="Pseudostate")
fsm_Join = Class(name="fsm::Join")

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_State_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_State.attributes={fsm_State_finalTime, fsm_State_initialTime}

# fsm_Transition class attributes and methods
fsm_Transition_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_Transition_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_Transition_time: Property = Property(name="time", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_finalTime, fsm_Transition_initialTime, fsm_Transition_time}

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_InitialState class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_TimedTransition class attributes and methods
fsm_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
fsm_TimedTransition.attributes={fsm_TimedTransition_duration}

# Transition class attributes and methods

# fsm_Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# Pseudostate class attributes and methods

# fsm_Join class attributes and methods

# Relationships
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="7", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="10", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine11: BinaryAssociation = BinaryAssociation(
    name="stateMachine11",
    ends={
        Property(name="13", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="1", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="4", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="16", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger20: BinaryAssociation = BinaryAssociation(
    name="trigger20",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine21: BinaryAssociation = BinaryAssociation(
    name="stateMachine21",
    ends={
        Property(name="23", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_TimedTransition_Transition = Generalization(general=Transition, specific=fsm_TimedTransition)
gen_fsm_Pseudostate_State = Generalization(general=State, specific=fsm_Pseudostate)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_NamedElement, fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_FinalState, State, fsm_InitialState, fsm_Trigger, fsm_TimedTransition, Transition, fsm_Pseudostate, fsm_Fork, Pseudostate, fsm_Join},
    associations={outgoing5, incoming8, stateMachine11, states0, transitions2, target14, source17, trigger20, stateMachine21},
    generalizations={gen_fsm_State_NamedElement, gen_fsm_StateMachine_NamedElement, gen_fsm_FinalState_State, gen_fsm_InitialState_State, gen_fsm_Transition_NamedElement, gen_fsm_TimedTransition_Transition, gen_fsm_Pseudostate_State, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)