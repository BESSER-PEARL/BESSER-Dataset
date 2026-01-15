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
statemachine_StateMachine = Class(name="statemachine::StateMachine")
statemachine_Declaration = Class(name="statemachine::Declaration", is_abstract=True)
statemachine_StateMachineVariable = Class(name="statemachine::StateMachineVariable")
statemachine_Transition = Class(name="statemachine::Transition")
Declaration = Class(name="Declaration")
statemachine_State = Class(name="statemachine::State", is_abstract=True)
statemachine_Action = Class(name="statemachine::Action")
statemachine_NormalState = Class(name="statemachine::NormalState")
State = Class(name="State")
statemachine_InitialState = Class(name="statemachine::InitialState")
statemachine_FinalState = Class(name="statemachine::FinalState")

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_m_printReachable: Method = Method(name="printReachable", parameters={})
statemachine_StateMachine.methods={statemachine_StateMachine_m_printReachable}

# statemachine_Declaration class attributes and methods
statemachine_Declaration_m_printReachable: Method = Method(name="printReachable", parameters={})
statemachine_Declaration.methods={statemachine_Declaration_m_printReachable}

# statemachine_StateMachineVariable class attributes and methods
statemachine_StateMachineVariable_type: Property = Property(name="type", type=StringType)
statemachine_StateMachineVariable_name: Property = Property(name="name", type=StringType)
statemachine_StateMachineVariable.attributes={statemachine_StateMachineVariable_type, statemachine_StateMachineVariable_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_label: Property = Property(name="label", type=StringType)
statemachine_Transition_sourceLabel: Property = Property(name="sourceLabel", type=StringType)
statemachine_Transition_targetLabel: Property = Property(name="targetLabel", type=StringType)
statemachine_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
statemachine_Transition_actionLabel: Property = Property(name="actionLabel", type=StringType)
statemachine_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
statemachine_Transition_actionStatement: Property = Property(name="actionStatement", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_guardExpression, statemachine_Transition_actionStatement, statemachine_Transition_guardLabel, statemachine_Transition_targetLabel, statemachine_Transition_actionLabel, statemachine_Transition_sourceLabel, statemachine_Transition_label}

# Declaration class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_label: Property = Property(name="label", type=StringType)
statemachine_State_id: Property = Property(name="id", type=IntegerType)
statemachine_State_m_printReachable: Method = Method(name="printReachable", parameters={})
statemachine_State.attributes={statemachine_State_id, statemachine_State_label}
statemachine_State.methods={statemachine_State_m_printReachable}

# statemachine_Action class attributes and methods
statemachine_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
statemachine_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
statemachine_Action.attributes={statemachine_Action_actionLabel, statemachine_Action_actionStatement}

# statemachine_NormalState class attributes and methods

# State class attributes and methods

# statemachine_InitialState class attributes and methods

# statemachine_FinalState class attributes and methods

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="statemachine_Declaration", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machineVariables1: BinaryAssociation = BinaryAssociation(
    name="machineVariables1",
    ends={
        Property(name="statemachine_StateMachineVariable", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="statemachine_State", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
to_state4: BinaryAssociation = BinaryAssociation(
    name="to_state4",
    ends={
        Property(name="statemachine_State6", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition5", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
successors8: BinaryAssociation = BinaryAssociation(
    name="successors8",
    ends={
        Property(name="statemachine_State9", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State7", type=statemachine_State, multiplicity=Multiplicity(0, 9999))
    }
)
reachable11: BinaryAssociation = BinaryAssociation(
    name="reachable11",
    ends={
        Property(name="statemachine_State12", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State10", type=statemachine_State, multiplicity=Multiplicity(0, 9999))
    }
)
to_transitions13: BinaryAssociation = BinaryAssociation(
    name="to_transitions13",
    ends={
        Property(name="statemachine_Transition15", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State14", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry16: BinaryAssociation = BinaryAssociation(
    name="entry16",
    ends={
        Property(name="statemachine_Action", type=statemachine_NormalState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_NormalState", type=statemachine_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statemachine_Transition_Declaration = Generalization(general=Declaration, specific=statemachine_Transition)
gen_statemachine_State_Declaration = Generalization(general=Declaration, specific=statemachine_State)
gen_statemachine_NormalState_State = Generalization(general=State, specific=statemachine_NormalState)
gen_statemachine_InitialState_State = Generalization(general=State, specific=statemachine_InitialState)
gen_statemachine_FinalState_State = Generalization(general=State, specific=statemachine_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_Declaration, statemachine_StateMachineVariable, statemachine_Transition, Declaration, statemachine_State, statemachine_Action, statemachine_NormalState, State, statemachine_InitialState, statemachine_FinalState},
    associations={declarations0, machineVariables1, source3, to_state4, successors8, reachable11, to_transitions13, entry16},
    generalizations={gen_statemachine_Transition_Declaration, gen_statemachine_State_Declaration, gen_statemachine_NormalState_State, gen_statemachine_InitialState_State, gen_statemachine_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)