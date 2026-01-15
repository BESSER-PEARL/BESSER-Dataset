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
statemachine103_StateMachine = Class(name="statemachine103::StateMachine")
statemachine103_StateMachineObject = Class(name="statemachine103::StateMachineObject", is_abstract=True)
statemachine103_State = Class(name="statemachine103::State", is_abstract=True)
statemachine103_StateMachineVariable = Class(name="statemachine103::StateMachineVariable")
statemachine103_Transition = Class(name="statemachine103::Transition")
StateMachineObject = Class(name="StateMachineObject")
statemachine103_Action = Class(name="statemachine103::Action")
statemachine103_NormalState = Class(name="statemachine103::NormalState")
State = Class(name="State")
statemachine103_InitialState = Class(name="statemachine103::InitialState")
statemachine103_FinalState = Class(name="statemachine103::FinalState")

# statemachine103_StateMachine class attributes and methods
statemachine103_StateMachine_label: Property = Property(name="label", type=StringType)
statemachine103_StateMachine.attributes={statemachine103_StateMachine_label}

# statemachine103_StateMachineObject class attributes and methods
statemachine103_StateMachineObject_label: Property = Property(name="label", type=StringType)
statemachine103_StateMachineObject.attributes={statemachine103_StateMachineObject_label}

# statemachine103_State class attributes and methods
statemachine103_State_id: Property = Property(name="id", type=IntegerType)
statemachine103_State.attributes={statemachine103_State_id}

# statemachine103_StateMachineVariable class attributes and methods
statemachine103_StateMachineVariable_type: Property = Property(name="type", type=StringType)
statemachine103_StateMachineVariable_name: Property = Property(name="name", type=StringType)
statemachine103_StateMachineVariable.attributes={statemachine103_StateMachineVariable_name, statemachine103_StateMachineVariable_type}

# statemachine103_Transition class attributes and methods
statemachine103_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
statemachine103_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
statemachine103_Transition.attributes={statemachine103_Transition_guardLabel, statemachine103_Transition_guardExpression}

# StateMachineObject class attributes and methods

# statemachine103_Action class attributes and methods
statemachine103_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
statemachine103_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
statemachine103_Action.attributes={statemachine103_Action_actionLabel, statemachine103_Action_actionStatement}

# statemachine103_NormalState class attributes and methods

# State class attributes and methods

# statemachine103_InitialState class attributes and methods

# statemachine103_FinalState class attributes and methods

# Relationships
machineObjects0: BinaryAssociation = BinaryAssociation(
    name="machineObjects0",
    ends={
        Property(name="statemachine103_StateMachineObject", type=statemachine103_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_StateMachine", type=statemachine103_StateMachineObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="statemachine103_State", type=statemachine103_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_Transition", type=statemachine103_State, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="statemachine103_State6", type=statemachine103_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_Transition5", type=statemachine103_State, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables1: BinaryAssociation = BinaryAssociation(
    name="machineVariables1",
    ends={
        Property(name="statemachine103_StateMachineVariable", type=statemachine103_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_StateMachine2", type=statemachine103_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next10: BinaryAssociation = BinaryAssociation(
    name="next10",
    ends={
        Property(name="statemachine103_Action11", type=statemachine103_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_Action9", type=statemachine103_Action, multiplicity=Multiplicity(0, 1))
    }
)
t_actions7: BinaryAssociation = BinaryAssociation(
    name="t_actions7",
    ends={
        Property(name="statemachine103_Action", type=statemachine103_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_Transition8", type=statemachine103_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions12: BinaryAssociation = BinaryAssociation(
    name="s_actions12",
    ends={
        Property(name="statemachine103_Action13", type=statemachine103_NormalState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine103_NormalState", type=statemachine103_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine103_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=statemachine103_Transition)
gen_statemachine103_State_StateMachineObject = Generalization(general=StateMachineObject, specific=statemachine103_State)
gen_statemachine103_NormalState_State = Generalization(general=State, specific=statemachine103_NormalState)
gen_statemachine103_InitialState_State = Generalization(general=State, specific=statemachine103_InitialState)
gen_statemachine103_FinalState_State = Generalization(general=State, specific=statemachine103_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statemachine103",
    types={statemachine103_StateMachine, statemachine103_StateMachineObject, statemachine103_State, statemachine103_StateMachineVariable, statemachine103_Transition, StateMachineObject, statemachine103_Action, statemachine103_NormalState, State, statemachine103_InitialState, statemachine103_FinalState},
    associations={machineObjects0, source3, target4, machineVariables1, next10, t_actions7, s_actions12},
    generalizations={gen_statemachine103_Transition_StateMachineObject, gen_statemachine103_State_StateMachineObject, gen_statemachine103_NormalState_State, gen_statemachine103_InitialState_State, gen_statemachine103_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)