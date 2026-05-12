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
simplefsm_Transition = Class(name="simplefsm_Transition")
simplefsm_SimpleFiniteStateMachine = Class(name="simplefsm_SimpleFiniteStateMachine")
simplefsm_State = Class(name="simplefsm_State")

# simplefsm_Transition class attributes and methods
simplefsm_Transition_name: Property = Property(name="name", type=StringType)
simplefsm_Transition_event: Property = Property(name="event", type=StringType)
simplefsm_Transition.attributes={simplefsm_Transition_event, simplefsm_Transition_name}

# simplefsm_SimpleFiniteStateMachine class attributes and methods
simplefsm_SimpleFiniteStateMachine_name: Property = Property(name="name", type=StringType)
simplefsm_SimpleFiniteStateMachine.attributes={simplefsm_SimpleFiniteStateMachine_name}

# simplefsm_State class attributes and methods
simplefsm_State_action: Property = Property(name="action", type=StringType)
simplefsm_State_name: Property = Property(name="name", type=StringType)
simplefsm_State.attributes={simplefsm_State_name, simplefsm_State_action}

# Relationships
outgoingTransitions1: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions1",
    ends={
        Property(name="Transition", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState", type=simplefsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM2: BinaryAssociation = BinaryAssociation(
    name="owningFSM2",
    ends={
        Property(name="SimpleFiniteStateMachine", type=simplefsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=simplefsm_SimpleFiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=simplefsm_SimpleFiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=simplefsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="simplefsm_State", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplefsm_Transition", type=simplefsm_State, multiplicity=Multiplicity(0, 1))
    }
)
owningState4: BinaryAssociation = BinaryAssociation(
    name="owningState4",
    ends={
        Property(name="State5", type=simplefsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=simplefsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="simplefsm",
    types={simplefsm_Transition, simplefsm_SimpleFiniteStateMachine, simplefsm_State},
    associations={outgoingTransitions1, owningFSM2, states0, target3, owningState4},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)