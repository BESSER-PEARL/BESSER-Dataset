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
state_Node = Class(name="state::Node", is_abstract=True)
state_Transition = Class(name="state::Transition")
state_InitialNode = Class(name="state::InitialNode")
Node = Class(name="Node")
state_FinalNode = Class(name="state::FinalNode")
state_ConditionalNode = Class(name="state::ConditionalNode")
state_State = Class(name="state::State")
state_StateMachine = Class(name="state::StateMachine")
state_Module = Class(name="state::Module")
state_TimeoutTransition = Class(name="state::TimeoutTransition")
Transition = Class(name="Transition")
state_Condition = Class(name="state::Condition")

# state_Node class attributes and methods

# state_Transition class attributes and methods
state_Transition_triggerEventName: Property = Property(name="triggerEventName", type=StringType)
state_Transition.attributes={state_Transition_triggerEventName}

# state_InitialNode class attributes and methods

# Node class attributes and methods

# state_FinalNode class attributes and methods

# state_ConditionalNode class attributes and methods

# state_State class attributes and methods
state_State_name: Property = Property(name="name", type=StringType)
state_State_duration: Property = Property(name="duration", type=StringType)
state_State.attributes={state_State_duration, state_State_name}

# state_StateMachine class attributes and methods
state_StateMachine_name: Property = Property(name="name", type=StringType)
state_StateMachine.attributes={state_StateMachine_name}

# state_Module class attributes and methods

# state_TimeoutTransition class attributes and methods

# Transition class attributes and methods

# state_Condition class attributes and methods
state_Condition_expression: Property = Property(name="expression", type=StringType)
state_Condition.attributes={state_Condition_expression}

# Relationships
incoming0: BinaryAssociation = BinaryAssociation(
    name="incoming0",
    ends={
        Property(name="state_Transition", type=state_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Node", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing1: BinaryAssociation = BinaryAssociation(
    name="outgoing1",
    ends={
        Property(name="state_Transition3", type=state_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Node2", type=state_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="state_Node6", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition5", type=state_Node, multiplicity=Multiplicity(0, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="state_Node9", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition8", type=state_Node, multiplicity=Multiplicity(0, 1))
    }
)
condition12: BinaryAssociation = BinaryAssociation(
    name="condition12",
    ends={
        Property(name="state_Condition13", type=state_ConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="state_ConditionalNode", type=state_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes14: BinaryAssociation = BinaryAssociation(
    name="nodes14",
    ends={
        Property(name="state_Node15", type=state_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_StateMachine", type=state_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions16: BinaryAssociation = BinaryAssociation(
    name="transitions16",
    ends={
        Property(name="state_Transition18", type=state_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_StateMachine17", type=state_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module19: BinaryAssociation = BinaryAssociation(
    name="module19",
    ends={
        Property(name="state_Module", type=state_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_StateMachine20", type=state_Module, multiplicity=Multiplicity(0, 1))
    }
)
guard10: BinaryAssociation = BinaryAssociation(
    name="guard10",
    ends={
        Property(name="state_Condition", type=state_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="state_Transition11", type=state_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_state_InitialNode_Node = Generalization(general=Node, specific=state_InitialNode)
gen_state_FinalNode_Node = Generalization(general=Node, specific=state_FinalNode)
gen_state_ConditionalNode_Node = Generalization(general=Node, specific=state_ConditionalNode)
gen_state_State_Node = Generalization(general=Node, specific=state_State)
gen_state_TimeoutTransition_Transition = Generalization(general=Transition, specific=state_TimeoutTransition)

# Domain Model
domain_model = DomainModel(
    name="state",
    types={state_Node, state_Transition, state_InitialNode, Node, state_FinalNode, state_ConditionalNode, state_State, state_StateMachine, state_Module, state_TimeoutTransition, Transition, state_Condition},
    associations={incoming0, outgoing1, source4, target7, condition12, nodes14, transitions16, module19, guard10},
    generalizations={gen_state_InitialNode_Node, gen_state_FinalNode_Node, gen_state_ConditionalNode_Node, gen_state_State_Node, gen_state_TimeoutTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)