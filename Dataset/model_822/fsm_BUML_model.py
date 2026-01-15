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
fsm_Variable = Class(name="fsm::Variable", is_abstract=True)
fsm_Guard = Class(name="fsm::Guard", is_abstract=True)
fsm_Action = Class(name="fsm::Action", is_abstract=True)
fsm_NamedElement = Class(name="fsm::NamedElement", is_abstract=True)
fsm_NumberVariable = Class(name="fsm::NumberVariable")
Variable = Class(name="Variable")
fsm_NumberGuard = Class(name="fsm::NumberGuard", is_abstract=True)
Guard = Class(name="Guard")
fsm_AssignValueAction = Class(name="fsm::AssignValueAction")
Action = Class(name="Action")
fsm_LessThanNumberGuard = Class(name="fsm::LessThanNumberGuard")
fsm_GreaterThanNumberGuard = Class(name="fsm::GreaterThanNumberGuard")
fsm_IncreaseValueAction = Class(name="fsm::IncreaseValueAction")
fsm_DecreaseValueAction = Class(name="fsm::DecreaseValueAction")
fsm_EqualNumberGuard = Class(name="fsm::EqualNumberGuard")
NumberGuard = Class(name="NumberGuard")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods

# fsm_Transition class attributes and methods

# fsm_Variable class attributes and methods
fsm_Variable_name: Property = Property(name="name", type=StringType)
fsm_Variable.attributes={fsm_Variable_name}

# fsm_Guard class attributes and methods
fsm_Guard_not: Property = Property(name="not", type=BooleanType)
fsm_Guard.attributes={fsm_Guard_not}

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

# fsm_EqualNumberGuard class attributes and methods

# NumberGuard class attributes and methods

# Relationships
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="1", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState2: BinaryAssociation = BinaryAssociation(
    name="initialState2",
    ends={
        Property(name="fsm_State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedTransitions3: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions3",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine4", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="fsm_Variable", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine6", type=fsm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions10: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions10",
    ends={
        Property(name="11", type=fsm_Transition, multiplicity=Multiplicity(0, 9999)),
        Property(name="12", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
incomingTransitions13: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions13",
    ends={
        Property(name="15", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="18", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="21", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
guard22: BinaryAssociation = BinaryAssociation(
    name="guard22",
    ends={
        Property(name="fsm_Guard", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition23", type=fsm_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action24: BinaryAssociation = BinaryAssociation(
    name="action24",
    ends={
        Property(name="fsm_Action", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition25", type=fsm_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningFSM7: BinaryAssociation = BinaryAssociation(
    name="owningFSM7",
    ends={
        Property(name="9", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="fsm_NumberVariable29", type=fsm_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Action28", type=fsm_NumberVariable, multiplicity=Multiplicity(1, 1))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="fsm_NumberVariable", type=fsm_NumberGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NumberGuard", type=fsm_NumberVariable, multiplicity=Multiplicity(1, 1))
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
    types={fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_Variable, fsm_Guard, fsm_Action, fsm_NamedElement, fsm_NumberVariable, Variable, fsm_NumberGuard, Guard, fsm_AssignValueAction, Action, fsm_LessThanNumberGuard, fsm_GreaterThanNumberGuard, fsm_IncreaseValueAction, fsm_DecreaseValueAction, fsm_EqualNumberGuard, NumberGuard},
    associations={ownedStates0, initialState2, ownedTransitions3, variables5, outgoingTransitions10, incomingTransitions13, source16, target19, guard22, action24, owningFSM7, target27, source26},
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