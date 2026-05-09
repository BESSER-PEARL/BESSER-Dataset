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
fsm_CompositeState = Class(name="fsm_CompositeState")
fsm_FinalState = Class(name="fsm_FinalState")
State = Class(name="State")
fsm_InitialState = Class(name="fsm_InitialState")
fsm_NamedElement = Class(name="fsm_NamedElement")
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm_State")
fsm_Fork = Class(name="fsm_Fork")
Pseudostate = Class(name="Pseudostate")
fsm_Join = Class(name="fsm_Join")
fsm_Region = Class(name="fsm_Region")
fsm_Trigger = Class(name="fsm_Trigger")
fsm_TimedTransition = Class(name="fsm_TimedTransition")
Transition = Class(name="Transition")
fsm_Pseudostate = Class(name="fsm_Pseudostate")

# fsm_Transition class attributes and methods
fsm_Transition_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_Transition_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_Transition_time: Property = Property(name="time", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_time, fsm_Transition_initialTime, fsm_Transition_finalTime}

# fsm_CompositeState class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_InitialState class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_State_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_State.attributes={fsm_State_initialTime, fsm_State_finalTime}

# fsm_Fork class attributes and methods

# Pseudostate class attributes and methods

# fsm_Join class attributes and methods

# fsm_Region class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_TimedTransition class attributes and methods
fsm_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
fsm_TimedTransition.attributes={fsm_TimedTransition_duration}

# Transition class attributes and methods

# fsm_Pseudostate class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Transition4", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition6", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine7: BinaryAssociation = BinaryAssociation(
    name="stateMachine7",
    ends={
        Property(name="StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
parentState8: BinaryAssociation = BinaryAssociation(
    name="parentState8",
    ends={
        Property(name="fsm_CompositeState", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
regions16: BinaryAssociation = BinaryAssociation(
    name="regions16",
    ends={
        Property(name="fsm_Region", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_CompositeState17", type=fsm_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states18: BinaryAssociation = BinaryAssociation(
    name="states18",
    ends={
        Property(name="fsm_State20", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region19", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent21: BinaryAssociation = BinaryAssociation(
    name="parent21",
    ends={
        Property(name="fsm_CompositeState23", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region22", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="State10", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="State12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger13: BinaryAssociation = BinaryAssociation(
    name="trigger13",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine14: BinaryAssociation = BinaryAssociation(
    name="stateMachine14",
    ends={
        Property(name="StateMachine15", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_Pseudostate_State = Generalization(general=State, specific=fsm_Pseudostate)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_CompositeState_State = Generalization(general=State, specific=fsm_CompositeState)
gen_fsm_TimedTransition_Transition = Generalization(general=Transition, specific=fsm_TimedTransition)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, fsm_CompositeState, fsm_FinalState, State, fsm_InitialState, fsm_NamedElement, fsm_StateMachine, NamedElement, fsm_State, fsm_Fork, Pseudostate, fsm_Join, fsm_Region, fsm_Trigger, fsm_TimedTransition, Transition, fsm_Pseudostate},
    associations={states0, transitions1, outgoing3, incoming5, stateMachine7, parentState8, regions16, states18, parent21, target9, source11, trigger13, stateMachine14},
    generalizations={gen_fsm_State_NamedElement, gen_fsm_FinalState_State, gen_fsm_InitialState_State, gen_fsm_Transition_NamedElement, gen_fsm_StateMachine_NamedElement, gen_fsm_Pseudostate_State, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_CompositeState_State, gen_fsm_TimedTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)