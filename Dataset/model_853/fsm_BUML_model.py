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
fsm_CompositeState = Class(name="fsm::CompositeState")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_InitialState = Class(name="fsm::InitialState")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_Transition = Class(name="fsm::Transition")
fsm_Region = Class(name="fsm::Region")
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
fsm_State.attributes={fsm_State_initialTime, fsm_State_finalTime}

# fsm_CompositeState class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_InitialState class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Transition class attributes and methods
fsm_Transition_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_Transition_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_Transition_time: Property = Property(name="time", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_initialTime, fsm_Transition_time, fsm_Transition_finalTime}

# fsm_Region class attributes and methods

# fsm_TimedTransition class attributes and methods
fsm_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
fsm_TimedTransition.attributes={fsm_TimedTransition_duration}

# Transition class attributes and methods

# fsm_Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# Pseudostate class attributes and methods

# fsm_Join class attributes and methods

# Relationships
stateMachine11: BinaryAssociation = BinaryAssociation(
    name="stateMachine11",
    ends={
        Property(name="12", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1)),
        Property(name="13", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
parentState14: BinaryAssociation = BinaryAssociation(
    name="parentState14",
    ends={
        Property(name="fsm_CompositeState", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="17", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="20", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger21: BinaryAssociation = BinaryAssociation(
    name="trigger21",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine22: BinaryAssociation = BinaryAssociation(
    name="stateMachine22",
    ends={
        Property(name="24", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
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
regions25: BinaryAssociation = BinaryAssociation(
    name="regions25",
    ends={
        Property(name="fsm_Region", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_CompositeState26", type=fsm_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states27: BinaryAssociation = BinaryAssociation(
    name="states27",
    ends={
        Property(name="fsm_State29", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region28", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent30: BinaryAssociation = BinaryAssociation(
    name="parent30",
    ends={
        Property(name="fsm_CompositeState32", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region31", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_TimedTransition_Transition = Generalization(general=Transition, specific=fsm_TimedTransition)
gen_fsm_Pseudostate_State = Generalization(general=State, specific=fsm_Pseudostate)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_CompositeState_State = Generalization(general=State, specific=fsm_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_NamedElement, fsm_StateMachine, NamedElement, fsm_State, fsm_CompositeState, fsm_FinalState, State, fsm_InitialState, fsm_Trigger, fsm_Transition, fsm_Region, fsm_TimedTransition, Transition, fsm_Pseudostate, fsm_Fork, Pseudostate, fsm_Join},
    associations={stateMachine11, parentState14, target15, source18, trigger21, stateMachine22, states0, transitions2, outgoing5, incoming8, regions25, states27, parent30},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_FinalState_State, gen_fsm_InitialState_State, gen_fsm_Transition_NamedElement, gen_fsm_State_NamedElement, gen_fsm_TimedTransition_Transition, gen_fsm_Pseudostate_State, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)