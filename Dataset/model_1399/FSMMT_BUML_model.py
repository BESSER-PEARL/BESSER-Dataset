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
model_AbstractState = Class(name="model_AbstractState")
model_FiniteStateMachine = Class(name="model_FiniteStateMachine")
model_Transition = Class(name="model_Transition")
model_State = Class(name="model_State")
AbstractState = Class(name="AbstractState")

# model_AbstractState class attributes and methods
model_AbstractState_name: Property = Property(name="name", type=BooleanType)
model_AbstractState_m_on: Method = Method(name="on", parameters={Parameter(name='model_event', type=StringType)}, type=StringType)
model_AbstractState_m_onEnter: Method = Method(name="onEnter", parameters={})
model_AbstractState_m_onExit: Method = Method(name="onExit", parameters={})
model_AbstractState.attributes={model_AbstractState_name}
model_AbstractState.methods={model_AbstractState_m_onEnter, model_AbstractState_m_onExit, model_AbstractState_m_on}

# model_FiniteStateMachine class attributes and methods
model_FiniteStateMachine_m_main: Method = Method(name="main", parameters={})
model_FiniteStateMachine_m_onEnter: Method = Method(name="onEnter", parameters={})
model_FiniteStateMachine_m_on: Method = Method(name="on", parameters={Parameter(name='model_event', type=StringType)}, type=AbstractState)
model_FiniteStateMachine_m_enterInitialState: Method = Method(name="enterInitialState", parameters={Parameter(name='model_args', type=StringType)})
model_FiniteStateMachine.methods={model_FiniteStateMachine_m_on, model_FiniteStateMachine_m_onEnter, model_FiniteStateMachine_m_main, model_FiniteStateMachine_m_enterInitialState}

# model_Transition class attributes and methods
model_Transition_name: Property = Property(name="name", type=StringType)
model_Transition_trigger: Property = Property(name="trigger", type=StringType)
model_Transition_m_accepts: Method = Method(name="accepts", parameters={Parameter(name='model_event', type=StringType)})
model_Transition_m_on: Method = Method(name="on", parameters={Parameter(name='model_event', type=StringType)}, type=AbstractState)
model_Transition.attributes={model_Transition_trigger, model_Transition_name}
model_Transition.methods={model_Transition_m_on, model_Transition_m_accepts}

# model_State class attributes and methods
model_State_m_onEnter: Method = Method(name="onEnter", parameters={})
model_State_m_onExit: Method = Method(name="onExit", parameters={})
model_State.methods={model_State_m_onExit, model_State_m_onEnter}

# AbstractState class attributes and methods

# Relationships
initial2: BinaryAssociation = BinaryAssociation(
    name="initial2",
    ends={
        Property(name="model_AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=model_FiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoings1: BinaryAssociation = BinaryAssociation(
    name="outgoings1",
    ends={
        Property(name="Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
current4: BinaryAssociation = BinaryAssociation(
    name="current4",
    ends={
        Property(name="model_AbstractState6", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine5", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="AbstractState8", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="model_AbstractState10", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_State_AbstractState = Generalization(general=AbstractState, specific=model_State)
gen_model_FiniteStateMachine_AbstractState = Generalization(general=AbstractState, specific=model_FiniteStateMachine)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_AbstractState, model_FiniteStateMachine, model_Transition, model_State, AbstractState},
    associations={initial2, states3, parent0, outgoings1, current4, source7, target9},
    generalizations={gen_model_State_AbstractState, gen_model_FiniteStateMachine_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)