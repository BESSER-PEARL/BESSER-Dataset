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
fsm_NamedElement = Class(name="fsm_NamedElement")
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm_State")
fsm_Transition = Class(name="fsm_Transition")
fsm_Guard = Class(name="fsm_Guard")
fsm_Action = Class(name="fsm_Action")
fsm_TimedTransition = Class(name="fsm_TimedTransition")
Transition = Class(name="Transition")
fsm_Variable = Class(name="fsm_Variable")
fsm_CompositeState = Class(name="fsm_CompositeState")
fsm_FinalState = Class(name="fsm_FinalState")
State = Class(name="State")
fsm_InitialState = Class(name="fsm_InitialState")
fsm_Trigger = Class(name="fsm_Trigger")
fsm_Pseudostate = Class(name="fsm_Pseudostate")
fsm_Fork = Class(name="fsm_Fork")
Pseudostate = Class(name="Pseudostate")
fsm_Join = Class(name="fsm_Join")
fsm_Region = Class(name="fsm_Region")
fsm_Choice = Class(name="fsm_Choice")

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
fsm_Transition.attributes={fsm_Transition_finalTime, fsm_Transition_initialTime}

# fsm_Guard class attributes and methods
fsm_Guard_expression: Property = Property(name="expression", type=StringType)
fsm_Guard.attributes={fsm_Guard_expression}

# fsm_Action class attributes and methods
fsm_Action_variable: Property = Property(name="variable", type=StringType)
fsm_Action_value: Property = Property(name="value", type=BooleanType)
fsm_Action.attributes={fsm_Action_value, fsm_Action_variable}

# fsm_TimedTransition class attributes and methods
fsm_TimedTransition_duration: Property = Property(name="duration", type=IntegerType)
fsm_TimedTransition.attributes={fsm_TimedTransition_duration}

# Transition class attributes and methods

# fsm_Variable class attributes and methods
fsm_Variable_name: Property = Property(name="name", type=StringType)
fsm_Variable_value: Property = Property(name="value", type=BooleanType)
fsm_Variable.attributes={fsm_Variable_value, fsm_Variable_name}

# fsm_CompositeState class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_InitialState class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# Pseudostate class attributes and methods

# fsm_Join class attributes and methods

# fsm_Region class attributes and methods

# fsm_Choice class attributes and methods

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
stateMachine15: BinaryAssociation = BinaryAssociation(
    name="stateMachine15",
    ends={
        Property(name="StateMachine16", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
guard17: BinaryAssociation = BinaryAssociation(
    name="guard17",
    ends={
        Property(name="fsm_Guard", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition18", type=fsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action19: BinaryAssociation = BinaryAssociation(
    name="action19",
    ends={
        Property(name="fsm_Action", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition20", type=fsm_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="fsm_Variable", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
parentState9: BinaryAssociation = BinaryAssociation(
    name="parentState9",
    ends={
        Property(name="fsm_CompositeState", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger14: BinaryAssociation = BinaryAssociation(
    name="trigger14",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
regions21: BinaryAssociation = BinaryAssociation(
    name="regions21",
    ends={
        Property(name="fsm_Region", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_CompositeState22", type=fsm_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states23: BinaryAssociation = BinaryAssociation(
    name="states23",
    ends={
        Property(name="fsm_State25", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region24", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent26: BinaryAssociation = BinaryAssociation(
    name="parent26",
    ends={
        Property(name="fsm_CompositeState28", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region27", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_TimedTransition_Transition = Generalization(general=Transition, specific=fsm_TimedTransition)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_InitialState_State = Generalization(general=State, specific=fsm_InitialState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_Pseudostate_State = Generalization(general=State, specific=fsm_Pseudostate)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_CompositeState_State = Generalization(general=State, specific=fsm_CompositeState)
gen_fsm_Choice_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Choice)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_NamedElement, fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_Guard, fsm_Action, fsm_TimedTransition, Transition, fsm_Variable, fsm_CompositeState, fsm_FinalState, State, fsm_InitialState, fsm_Trigger, fsm_Pseudostate, fsm_Fork, Pseudostate, fsm_Join, fsm_Region, fsm_Choice},
    associations={states0, transitions1, stateMachine15, guard17, action19, variables3, outgoing4, incoming6, stateMachine8, parentState9, target10, source12, trigger14, regions21, states23, parent26},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_TimedTransition_Transition, gen_fsm_State_NamedElement, gen_fsm_FinalState_State, gen_fsm_InitialState_State, gen_fsm_Transition_NamedElement, gen_fsm_Pseudostate_State, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_CompositeState_State, gen_fsm_Choice_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)