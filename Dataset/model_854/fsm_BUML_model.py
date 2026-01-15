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
fsm_Variable = Class(name="fsm::Variable")
fsm_NamedElement = Class(name="fsm::NamedElement")
fsm_CompositeState = Class(name="fsm::CompositeState")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_InitialState = Class(name="fsm::InitialState")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_Guard = Class(name="fsm::Guard")
fsm_Action = Class(name="fsm::Action")
fsm_Fork = Class(name="fsm::Fork")
Pseudostate = Class(name="Pseudostate")
fsm_Join = Class(name="fsm::Join")
fsm_Region = Class(name="fsm::Region")
fsm_Choice = Class(name="fsm::Choice")
fsm_TimedTransition = Class(name="fsm::TimedTransition")
Transition = Class(name="Transition")
fsm_Pseudostate = Class(name="fsm::Pseudostate")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_State_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_State.attributes={fsm_State_initialTime, fsm_State_finalTime}

# fsm_Transition class attributes and methods
fsm_Transition_initialTime: Property = Property(name="initialTime", type=IntegerType)
fsm_Transition_finalTime: Property = Property(name="finalTime", type=IntegerType)
fsm_Transition.attributes={fsm_Transition_initialTime, fsm_Transition_finalTime}

# fsm_Variable class attributes and methods
fsm_Variable_name: Property = Property(name="name", type=StringType)
fsm_Variable_value: Property = Property(name="value", type=BooleanType)
fsm_Variable.attributes={fsm_Variable_name, fsm_Variable_value}

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_CompositeState class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_InitialState class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Guard class attributes and methods
fsm_Guard_expression: Property = Property(name="expression", type=StringType)
fsm_Guard.attributes={fsm_Guard_expression}

# fsm_Action class attributes and methods
fsm_Action_variable: Property = Property(name="variable", type=StringType)
fsm_Action_value: Property = Property(name="value", type=BooleanType)
fsm_Action.attributes={fsm_Action_variable, fsm_Action_value}

# fsm_Fork class attributes and methods

# Pseudostate class attributes and methods

# fsm_Join class attributes and methods

# fsm_Region class attributes and methods

# fsm_Choice class attributes and methods

# fsm_TimedTransition class attributes and methods
fsm_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
fsm_TimedTransition.attributes={fsm_TimedTransition_duration}

# Transition class attributes and methods

# fsm_Pseudostate class attributes and methods

# Relationships
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
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="fsm_Variable", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="8", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
parentState15: BinaryAssociation = BinaryAssociation(
    name="parentState15",
    ends={
        Property(name="fsm_CompositeState", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="18", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="21", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger22: BinaryAssociation = BinaryAssociation(
    name="trigger22",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateMachine23: BinaryAssociation = BinaryAssociation(
    name="stateMachine23",
    ends={
        Property(name="25", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
guard26: BinaryAssociation = BinaryAssociation(
    name="guard26",
    ends={
        Property(name="fsm_Guard", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition27", type=fsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action28: BinaryAssociation = BinaryAssociation(
    name="action28",
    ends={
        Property(name="fsm_Action", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition29", type=fsm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incoming9: BinaryAssociation = BinaryAssociation(
    name="incoming9",
    ends={
        Property(name="11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine12: BinaryAssociation = BinaryAssociation(
    name="stateMachine12",
    ends={
        Property(name="14", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
regions30: BinaryAssociation = BinaryAssociation(
    name="regions30",
    ends={
        Property(name="fsm_Region", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_CompositeState31", type=fsm_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states32: BinaryAssociation = BinaryAssociation(
    name="states32",
    ends={
        Property(name="fsm_State34", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region33", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent35: BinaryAssociation = BinaryAssociation(
    name="parent35",
    ends={
        Property(name="fsm_CompositeState37", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region36", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_CompositeState_State = Generalization(general=State, specific=fsm_CompositeState)
gen_fsm_Choice_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Choice)
gen_fsm_TimedTransition_Transition = Generalization(general=Transition, specific=fsm_TimedTransition)
gen_fsm_Pseudostate_State = Generalization(general=State, specific=fsm_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_Variable, fsm_NamedElement, fsm_CompositeState, fsm_FinalState, State, fsm_InitialState, fsm_Trigger, fsm_Guard, fsm_Action, fsm_Fork, Pseudostate, fsm_Join, fsm_Region, fsm_Choice, fsm_TimedTransition, Transition, fsm_Pseudostate},
    associations={states0, transitions2, variables5, outgoing6, parentState15, target16, source19, trigger22, stateMachine23, guard26, action28, incoming9, stateMachine12, regions30, states32, parent35},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_State_NamedElement, gen_fsm_FinalState_State, gen_fsm_InitialState_State, gen_fsm_Transition_NamedElement, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_CompositeState_State, gen_fsm_Choice_Pseudostate, gen_fsm_TimedTransition_Transition, gen_fsm_Pseudostate_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)