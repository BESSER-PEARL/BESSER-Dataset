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
fsm_FiniteStateMachine = Class(name="fsm::FiniteStateMachine")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_FiniteStateMachine class attributes and methods
fsm_FiniteStateMachine_name: Property = Property(name="name", type=StringType)
fsm_FiniteStateMachine_unprocessedString: Property = Property(name="unprocessedString", type=StringType)
fsm_FiniteStateMachine_consummedString: Property = Property(name="consummedString", type=StringType)
fsm_FiniteStateMachine_producedString: Property = Property(name="producedString", type=StringType)
fsm_FiniteStateMachine_m_main: Method = Method(name="main", parameters={})
fsm_FiniteStateMachine_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
fsm_FiniteStateMachine.attributes={fsm_FiniteStateMachine_producedString, fsm_FiniteStateMachine_name, fsm_FiniteStateMachine_consummedString, fsm_FiniteStateMachine_unprocessedString}
fsm_FiniteStateMachine.methods={fsm_FiniteStateMachine_m_initializeModel, fsm_FiniteStateMachine_m_main}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State_isInitialState: Property = Property(name="isInitialState", type=BooleanType)
fsm_State_m_step: Method = Method(name="step", parameters={Parameter(name='inputString')})
fsm_State.attributes={fsm_State_name, fsm_State_isInitialState}
fsm_State.methods={fsm_State_m_step}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition_m_fire: Method = Method(name="fire", parameters={})
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_name, fsm_Transition_output}
fsm_Transition.methods={fsm_Transition_m_fire}

# Relationships
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsm_State", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FiniteStateMachine", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState1: BinaryAssociation = BinaryAssociation(
    name="currentState1",
    ends={
        Property(name="fsm_State3", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FiniteStateMachine2", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransitions4: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions4",
    ends={
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FiniteStateMachine, fsm_State, fsm_Transition},
    associations={target6, states0, currentState1, outgoingTransitions4},
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