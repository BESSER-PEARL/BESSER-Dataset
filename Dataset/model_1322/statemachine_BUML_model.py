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
statechart_StateMachineRoot = Class(name="statechart::StateMachineRoot")
IDBase = Class(name="IDBase")
statechart_StateMachine = Class(name="statechart::StateMachine")
statechart_Transition = Class(name="statechart::Transition")
StateVertex = Class(name="StateVertex")
statechart_Event = Class(name="statechart::Event")
statechart_StateAction = Class(name="statechart::StateAction", is_abstract=True)
statechart_CompositeState = Class(name="statechart::CompositeState")
State = Class(name="State")
statechart_StateVertex = Class(name="statechart::StateVertex")
statechart_State = Class(name="statechart::State")
statechart_Action = Class(name="statechart::Action")
statechart_Guard = Class(name="statechart::Guard")
statechart_TransitionAction = Class(name="statechart::TransitionAction")
Action = Class(name="Action")
statechart_Label = Class(name="statechart::Label")
statechart_DO = Class(name="statechart::DO")
StateAction = Class(name="StateAction")
statechart_ENTRY = Class(name="statechart::ENTRY")
statechart_EXIT = Class(name="statechart::EXIT")
NameBase = Class(name="NameBase")

# statechart_StateMachineRoot class attributes and methods

# IDBase class attributes and methods

# statechart_StateMachine class attributes and methods
statechart_StateMachine_name: Property = Property(name="name", type=StringType)
statechart_StateMachine.attributes={statechart_StateMachine_name}

# statechart_Transition class attributes and methods
statechart_Transition_description: Property = Property(name="description", type=StringType)
statechart_Transition.attributes={statechart_Transition_description}

# StateVertex class attributes and methods

# statechart_Event class attributes and methods
statechart_Event_name: Property = Property(name="name", type=StringType)
statechart_Event.attributes={statechart_Event_name}

# statechart_StateAction class attributes and methods

# statechart_CompositeState class attributes and methods
statechart_CompositeState_isConcurrent: Property = Property(name="isConcurrent", type=BooleanType)
statechart_CompositeState.attributes={statechart_CompositeState_isConcurrent}

# State class attributes and methods

# statechart_StateVertex class attributes and methods

# statechart_State class attributes and methods

# statechart_Action class attributes and methods
statechart_Action_value: Property = Property(name="value", type=StringType)
statechart_Action.attributes={statechart_Action_value}

# statechart_Guard class attributes and methods
statechart_Guard_expression: Property = Property(name="expression", type=StringType)
statechart_Guard.attributes={statechart_Guard_expression}

# statechart_TransitionAction class attributes and methods

# Action class attributes and methods

# statechart_Label class attributes and methods
statechart_Label_name: Property = Property(name="name", type=StringType)
statechart_Label.attributes={statechart_Label_name}

# statechart_DO class attributes and methods

# StateAction class attributes and methods

# statechart_ENTRY class attributes and methods

# statechart_EXIT class attributes and methods

# NameBase class attributes and methods

# Relationships
subStateMachines0: BinaryAssociation = BinaryAssociation(
    name="subStateMachines0",
    ends={
        Property(name="StateMachine", type=statechart_StateMachineRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_container", type=statechart_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialStateMachine1: BinaryAssociation = BinaryAssociation(
    name="InitialStateMachine1",
    ends={
        Property(name="statechart_StateMachine", type=statechart_StateMachineRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_StateMachineRoot", type=statechart_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="Transition", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="transSM_container", type=statechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledByAction5: BinaryAssociation = BinaryAssociation(
    name="calledByAction5",
    ends={
        Property(name="stateMachineCall", type=statechart_Action, multiplicity=Multiplicity(0, 9999)),
        Property(name="Action", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
InitialState6: BinaryAssociation = BinaryAssociation(
    name="InitialState6",
    ends={
        Property(name="statechart_State", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_StateMachine7", type=statechart_State, multiplicity=Multiplicity(0, 1))
    }
)
state_container8: BinaryAssociation = BinaryAssociation(
    name="state_container8",
    ends={
        Property(name="StateMachine9", type=statechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="top", type=statechart_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
internalTransitions10: BinaryAssociation = BinaryAssociation(
    name="internalTransitions10",
    ends={
        Property(name="Transition11", type=statechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="transS_container", type=statechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableEvents12: BinaryAssociation = BinaryAssociation(
    name="deferrableEvents12",
    ends={
        Property(name="statechart_Event", type=statechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_State13", type=statechart_Event, multiplicity=Multiplicity(0, 9999))
    }
)
actions14: BinaryAssociation = BinaryAssociation(
    name="actions14",
    ends={
        Property(name="StateAction", type=statechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="action_container", type=statechart_StateAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subVertexes15: BinaryAssociation = BinaryAssociation(
    name="subVertexes15",
    ends={
        Property(name="StateVertex", type=statechart_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="sv_container", type=statechart_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
top3: BinaryAssociation = BinaryAssociation(
    name="top3",
    ends={
        Property(name="State", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_container", type=statechart_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine_container4: BinaryAssociation = BinaryAssociation(
    name="statemachine_container4",
    ends={
        Property(name="StateMachineRoot", type=statechart_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="subStateMachines", type=statechart_StateMachineRoot, multiplicity=Multiplicity(0, 1))
    }
)
transS_container20: BinaryAssociation = BinaryAssociation(
    name="transS_container20",
    ends={
        Property(name="State21", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="internalTransitions", type=statechart_State, multiplicity=Multiplicity(0, 1))
    }
)
trigger22: BinaryAssociation = BinaryAssociation(
    name="trigger22",
    ends={
        Property(name="Event", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="evt_container", type=statechart_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard23: BinaryAssociation = BinaryAssociation(
    name="guard23",
    ends={
        Property(name="Guard", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gua_container", type=statechart_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action24: BinaryAssociation = BinaryAssociation(
    name="action24",
    ends={
        Property(name="TransitionAction", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="act_container", type=statechart_TransitionAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="StateVertex26", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="StateVertex28", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
evt_container29: BinaryAssociation = BinaryAssociation(
    name="evt_container29",
    ends={
        Property(name="Transition30", type=statechart_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=statechart_Transition, multiplicity=Multiplicity(0, 1))
    }
)
gua_container31: BinaryAssociation = BinaryAssociation(
    name="gua_container31",
    ends={
        Property(name="Transition32", type=statechart_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=statechart_Transition, multiplicity=Multiplicity(1, 1))
    }
)
stateMachineCall16: BinaryAssociation = BinaryAssociation(
    name="stateMachineCall16",
    ends={
        Property(name="StateMachine17", type=statechart_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="calledByAction", type=statechart_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transSM_container18: BinaryAssociation = BinaryAssociation(
    name="transSM_container18",
    ends={
        Property(name="StateMachine19", type=statechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=statechart_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
sv_container35: BinaryAssociation = BinaryAssociation(
    name="sv_container35",
    ends={
        Property(name="CompositeState", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subVertexes", type=statechart_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
outgoing36: BinaryAssociation = BinaryAssociation(
    name="outgoing36",
    ends={
        Property(name="Transition37", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statechart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming38: BinaryAssociation = BinaryAssociation(
    name="incoming38",
    ends={
        Property(name="Transition39", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statechart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
label40: BinaryAssociation = BinaryAssociation(
    name="label40",
    ends={
        Property(name="statechart_Label", type=statechart_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart_StateVertex", type=statechart_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action_container41: BinaryAssociation = BinaryAssociation(
    name="action_container41",
    ends={
        Property(name="State42", type=statechart_StateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="actions", type=statechart_State, multiplicity=Multiplicity(0, 1))
    }
)
act_container33: BinaryAssociation = BinaryAssociation(
    name="act_container33",
    ends={
        Property(name="Transition34", type=statechart_TransitionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="action", type=statechart_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statechart_StateMachineRoot_IDBase = Generalization(general=IDBase, specific=statechart_StateMachineRoot)
gen_statechart_StateMachine_IDBase = Generalization(general=IDBase, specific=statechart_StateMachine)
gen_statechart_State_StateVertex = Generalization(general=StateVertex, specific=statechart_State)
gen_statechart_CompositeState_State = Generalization(general=State, specific=statechart_CompositeState)
gen_statechart_Action_IDBase = Generalization(general=IDBase, specific=statechart_Action)
gen_statechart_Event_IDBase = Generalization(general=IDBase, specific=statechart_Event)
gen_statechart_Guard_IDBase = Generalization(general=IDBase, specific=statechart_Guard)
gen_statechart_TransitionAction_Action = Generalization(general=Action, specific=statechart_TransitionAction)
gen_statechart_Transition_IDBase = Generalization(general=IDBase, specific=statechart_Transition)
gen_statechart_StateAction_Action = Generalization(general=Action, specific=statechart_StateAction)
gen_statechart_DO_StateAction = Generalization(general=StateAction, specific=statechart_DO)
gen_statechart_ENTRY_StateAction = Generalization(general=StateAction, specific=statechart_ENTRY)
gen_statechart_EXIT_StateAction = Generalization(general=StateAction, specific=statechart_EXIT)
gen_statechart_Label_IDBase = Generalization(general=IDBase, specific=statechart_Label)
gen_statechart_StateVertex_IDBase = Generalization(general=IDBase, specific=statechart_StateVertex)
gen_statechart_StateVertex_NameBase = Generalization(general=NameBase, specific=statechart_StateVertex)

# Domain Model
domain_model = DomainModel(
    name="statechart",
    types={statechart_StateMachineRoot, IDBase, statechart_StateMachine, statechart_Transition, StateVertex, statechart_Event, statechart_StateAction, statechart_CompositeState, State, statechart_StateVertex, statechart_State, statechart_Action, statechart_Guard, statechart_TransitionAction, Action, statechart_Label, statechart_DO, StateAction, statechart_ENTRY, statechart_EXIT, NameBase},
    associations={subStateMachines0, InitialStateMachine1, transitions2, calledByAction5, InitialState6, state_container8, internalTransitions10, deferrableEvents12, actions14, subVertexes15, top3, statemachine_container4, transS_container20, trigger22, guard23, action24, source25, target27, evt_container29, gua_container31, stateMachineCall16, transSM_container18, sv_container35, outgoing36, incoming38, label40, action_container41, act_container33},
    generalizations={gen_statechart_StateMachineRoot_IDBase, gen_statechart_StateMachine_IDBase, gen_statechart_State_StateVertex, gen_statechart_CompositeState_State, gen_statechart_Action_IDBase, gen_statechart_Event_IDBase, gen_statechart_Guard_IDBase, gen_statechart_TransitionAction_Action, gen_statechart_Transition_IDBase, gen_statechart_StateAction_Action, gen_statechart_DO_StateAction, gen_statechart_ENTRY_StateAction, gen_statechart_EXIT_StateAction, gen_statechart_Label_IDBase, gen_statechart_StateVertex_IDBase, gen_statechart_StateVertex_NameBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)