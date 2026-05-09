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
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm_State")
fsm_Transition = Class(name="fsm_Transition")
fsm_Variable = Class(name="fsm_Variable", is_abstract=True)
fsm_Guard = Class(name="fsm_Guard", is_abstract=True)
fsm_Action = Class(name="fsm_Action", is_abstract=True)
fsm_NamedElement = Class(name="fsm_NamedElement", is_abstract=True)
fsm_NumberVariable = Class(name="fsm_NumberVariable")
Variable = Class(name="Variable")
fsm_NumberGuard = Class(name="fsm_NumberGuard", is_abstract=True)
Guard = Class(name="Guard")
fsm_EqualNumberGuard = Class(name="fsm_EqualNumberGuard")
NumberGuard = Class(name="NumberGuard")
fsm_AssignValueAction = Class(name="fsm_AssignValueAction")
Action = Class(name="Action")
fsm_LessThanNumberGuard = Class(name="fsm_LessThanNumberGuard")
fsm_GreaterThanNumberGuard = Class(name="fsm_GreaterThanNumberGuard")
fsm_IncreaseValueAction = Class(name="fsm_IncreaseValueAction")
fsm_DecreaseValueAction = Class(name="fsm_DecreaseValueAction")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods

# fsm_Transition class attributes and methods

# fsm_Variable class attributes and methods
fsm_Variable_name: Property = Property(name="name", type=StringType)
fsm_Variable.attributes={fsm_Variable_name}

# fsm_Guard class attributes and methods
fsm_Guard_not_: Property = Property(name="not_", type=BooleanType)
fsm_Guard.attributes={fsm_Guard_not_}

# fsm_Action class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_NumberVariable class attributes and methods
fsm_NumberVariable_initialValue: Property = Property(name="initialValue", type=IntegerType)
fsm_NumberVariable.attributes={fsm_NumberVariable_initialValue}

# Variable class attributes and methods

# fsm_NumberGuard class attributes and methods
fsm_NumberGuard_value: Property = Property(name="value", type=IntegerType)
fsm_NumberGuard.attributes={fsm_NumberGuard_value}

# Guard class attributes and methods

# fsm_EqualNumberGuard class attributes and methods

# NumberGuard class attributes and methods

# fsm_AssignValueAction class attributes and methods
fsm_AssignValueAction_value: Property = Property(name="value", type=IntegerType)
fsm_AssignValueAction.attributes={fsm_AssignValueAction_value}

# Action class attributes and methods

# fsm_LessThanNumberGuard class attributes and methods

# fsm_GreaterThanNumberGuard class attributes and methods

# fsm_IncreaseValueAction class attributes and methods
fsm_IncreaseValueAction_stepValue: Property = Property(name="stepValue", type=IntegerType)
fsm_IncreaseValueAction.attributes={fsm_IncreaseValueAction_stepValue}

# fsm_DecreaseValueAction class attributes and methods
fsm_DecreaseValueAction_stepValue: Property = Property(name="stepValue", type=IntegerType)
fsm_DecreaseValueAction.attributes={fsm_DecreaseValueAction_stepValue}

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedTransitions2: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions2",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables4: BinaryAssociation = BinaryAssociation(
    name="variables4",
    ends={
        Property(name="fsm_Variable", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine5", type=fsm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM6: BinaryAssociation = BinaryAssociation(
    name="owningFSM6",
    ends={
        Property(name="StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions7: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions7",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State13", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
guard14: BinaryAssociation = BinaryAssociation(
    name="guard14",
    ends={
        Property(name="fsm_Guard", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition15", type=fsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action16: BinaryAssociation = BinaryAssociation(
    name="action16",
    ends={
        Property(name="fsm_Action", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition17", type=fsm_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="fsm_NumberVariable", type=fsm_NumberGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NumberGuard", type=fsm_NumberVariable, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="fsm_NumberVariable21", type=fsm_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Action20", type=fsm_NumberVariable, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions8: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions8",
    ends={
        Property(name="Transition9", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_NumberVariable_Variable = Generalization(general=Variable, specific=fsm_NumberVariable)
gen_fsm_NumberGuard_Guard = Generalization(general=Guard, specific=fsm_NumberGuard)
gen_fsm_EqualNumberGuard_NumberGuard = Generalization(general=NumberGuard, specific=fsm_EqualNumberGuard)
gen_fsm_AssignValueAction_Action = Generalization(general=Action, specific=fsm_AssignValueAction)
gen_fsm_LessThanNumberGuard_NumberGuard = Generalization(general=NumberGuard, specific=fsm_LessThanNumberGuard)
gen_fsm_GreaterThanNumberGuard_NumberGuard = Generalization(general=NumberGuard, specific=fsm_GreaterThanNumberGuard)
gen_fsm_IncreaseValueAction_Action = Generalization(general=Action, specific=fsm_IncreaseValueAction)
gen_fsm_DecreaseValueAction_Action = Generalization(general=Action, specific=fsm_DecreaseValueAction)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_Variable, fsm_Guard, fsm_Action, fsm_NamedElement, fsm_NumberVariable, Variable, fsm_NumberGuard, Guard, fsm_EqualNumberGuard, NumberGuard, fsm_AssignValueAction, Action, fsm_LessThanNumberGuard, fsm_GreaterThanNumberGuard, fsm_IncreaseValueAction, fsm_DecreaseValueAction},
    associations={ownedStates0, initialState1, ownedTransitions2, variables4, owningFSM6, outgoingTransitions7, source10, target12, guard14, action16, source18, target19, incomingTransitions8},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_State_NamedElement, gen_fsm_Transition_NamedElement, gen_fsm_NumberVariable_Variable, gen_fsm_NumberGuard_Guard, gen_fsm_EqualNumberGuard_NumberGuard, gen_fsm_AssignValueAction_Action, gen_fsm_LessThanNumberGuard_NumberGuard, gen_fsm_GreaterThanNumberGuard_NumberGuard, gen_fsm_IncreaseValueAction_Action, gen_fsm_DecreaseValueAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)