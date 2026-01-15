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
fsm_State = Class(name="fsm::State")
fsm_FiniteStateMachine = Class(name="fsm::FiniteStateMachine")
fsm_Transition = Class(name="fsm::Transition")

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State_isInitialState: Property = Property(name="isInitialState", type=BooleanType)
fsm_State.attributes={fsm_State_isInitialState, fsm_State_name}

# fsm_FiniteStateMachine class attributes and methods
fsm_FiniteStateMachine_name: Property = Property(name="name", type=StringType)
fsm_FiniteStateMachine.attributes={fsm_FiniteStateMachine_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_name, fsm_Transition_input, fsm_Transition_output}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsm_State", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FiniteStateMachine", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions1: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions1",
    ends={
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition4", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State, fsm_FiniteStateMachine, fsm_Transition},
    associations={states0, outgoingTransitions1, target3},
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