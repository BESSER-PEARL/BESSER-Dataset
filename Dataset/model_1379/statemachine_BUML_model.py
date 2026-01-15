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
statemachine_State = Class(name="statemachine::State")
statemachine_StateMachine = Class(name="statemachine::StateMachine")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Set = Class(name="statemachine::Set", is_abstract=True)

# statemachine_State class attributes and methods
statemachine_State_initial: Property = Property(name="initial", type=BooleanType)
statemachine_State_terminal: Property = Property(name="terminal", type=BooleanType)
statemachine_State.attributes={statemachine_State_terminal, statemachine_State_initial}

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_m_accessibleAndCoAccessibleStates: Method = Method(name="accessibleAndCoAccessibleStates", parameters={})
statemachine_StateMachine_m_deltaFrom: Method = Method(name="deltaFrom", parameters={Parameter(name='from'), Parameter(name='to')})
statemachine_StateMachine_m_deltaMinusOne: Method = Method(name="deltaMinusOne", parameters={Parameter(name='label'), Parameter(name='state')})
statemachine_StateMachine_m_addState: Method = Method(name="addState", parameters={Parameter(name='initial'), Parameter(name='terminal')}, type=StringType)
statemachine_StateMachine_m_addTransition: Method = Method(name="addTransition", parameters={Parameter(name='transition')})
statemachine_StateMachine_m_terminals: Method = Method(name="terminals", parameters={})
statemachine_StateMachine_m_accessibleStates: Method = Method(name="accessibleStates", parameters={Parameter(name='st')})
statemachine_StateMachine_m_accessibleStates: Method = Method(name="accessibleStates", parameters={})
statemachine_StateMachine_m_accept: Method = Method(name="accept", parameters={Parameter(name='word')}, type=BooleanType)
statemachine_StateMachine_m_accessibleStates: Method = Method(name="accessibleStates", parameters={Parameter(name='states')})
statemachine_StateMachine_m_alphabet: Method = Method(name="alphabet", parameters={})
statemachine_StateMachine_m_coAccessibleStates: Method = Method(name="coAccessibleStates", parameters={Parameter(name='states')})
statemachine_StateMachine_m_coAccessibleStates: Method = Method(name="coAccessibleStates", parameters={})
statemachine_StateMachine_m_delta: Method = Method(name="delta", parameters={Parameter(name='s')})
statemachine_StateMachine_m_steps: Method = Method(name="steps", parameters={Parameter(name='word'), Parameter(name='s')})
statemachine_StateMachine_m_steps: Method = Method(name="steps", parameters={Parameter(name='st'), Parameter(name='word')})
statemachine_StateMachine_m_step: Method = Method(name="step", parameters={Parameter(name='s'), Parameter(name='o')})
statemachine_StateMachine_m_initials: Method = Method(name="initials", parameters={})
statemachine_StateMachine_m_delta: Method = Method(name="delta", parameters={Parameter(name='label'), Parameter(name='state')})
statemachine_StateMachine_m_deltaMinusOne: Method = Method(name="deltaMinusOne", parameters={Parameter(name='st')})
statemachine_StateMachine_m_delta: Method = Method(name="delta", parameters={Parameter(name='state')})
statemachine_StateMachine.methods={statemachine_StateMachine_m_steps, statemachine_StateMachine_m_step, statemachine_StateMachine_m_accessibleStates, statemachine_StateMachine_m_deltaMinusOne, statemachine_StateMachine_m_delta, statemachine_StateMachine_m_steps, statemachine_StateMachine_m_accessibleStates, statemachine_StateMachine_m_accessibleStates, statemachine_StateMachine_m_deltaFrom, statemachine_StateMachine_m_addState, statemachine_StateMachine_m_terminals, statemachine_StateMachine_m_accessibleAndCoAccessibleStates, statemachine_StateMachine_m_deltaMinusOne, statemachine_StateMachine_m_alphabet, statemachine_StateMachine_m_delta, statemachine_StateMachine_m_coAccessibleStates, statemachine_StateMachine_m_addTransition, statemachine_StateMachine_m_accept, statemachine_StateMachine_m_coAccessibleStates, statemachine_StateMachine_m_delta, statemachine_StateMachine_m_initials}

# statemachine_Transition class attributes and methods
statemachine_Transition_label: Property = Property(name="label", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_label}

# statemachine_Set class attributes and methods

# Relationships
delta1: BinaryAssociation = BinaryAssociation(
    name="delta1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start3: BinaryAssociation = BinaryAssociation(
    name="start3",
    ends={
        Property(name="statemachine_State5", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition4", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
end6: BinaryAssociation = BinaryAssociation(
    name="end6",
    ends={
        Property(name="statemachine_State8", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition7", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_State, statemachine_StateMachine, statemachine_Transition, statemachine_Set},
    associations={delta1, start3, end6, states0},
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