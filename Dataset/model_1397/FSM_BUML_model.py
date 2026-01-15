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
model_AbstractState = Class(name="model::AbstractState")
model_FiniteStateMachine = Class(name="model::FiniteStateMachine")
model_Transition = Class(name="model::Transition")
model_State = Class(name="model::State")
AbstractState = Class(name="AbstractState")

# model_AbstractState class attributes and methods
model_AbstractState_name: Property = Property(name="name", type=BooleanType)
model_AbstractState_m_on: Method = Method(name="on", parameters={Parameter(name='event')}, type=StringType)
model_AbstractState_m_onEnter: Method = Method(name="onEnter", parameters={})
model_AbstractState_m_onExit: Method = Method(name="onExit", parameters={})
model_AbstractState.attributes={model_AbstractState_name}
model_AbstractState.methods={model_AbstractState_m_onEnter, model_AbstractState_m_onExit, model_AbstractState_m_on}

# model_FiniteStateMachine class attributes and methods
model_FiniteStateMachine_m_onEnter: Method = Method(name="onEnter", parameters={})
model_FiniteStateMachine_m_on: Method = Method(name="on", parameters={Parameter(name='event')}, type=AbstractState)
model_FiniteStateMachine_m_enterInitialState: Method = Method(name="enterInitialState", parameters={Parameter(name='args')})
model_FiniteStateMachine_m_main: Method = Method(name="main", parameters={})
model_FiniteStateMachine.methods={model_FiniteStateMachine_m_enterInitialState, model_FiniteStateMachine_m_main, model_FiniteStateMachine_m_on, model_FiniteStateMachine_m_onEnter}

# model_Transition class attributes and methods
model_Transition_name: Property = Property(name="name", type=StringType)
model_Transition_trigger: Property = Property(name="trigger", type=StringType)
model_Transition_m_on: Method = Method(name="on", parameters={Parameter(name='event')}, type=AbstractState)
model_Transition_m_accepts: Method = Method(name="accepts", parameters={Parameter(name='event')})
model_Transition.attributes={model_Transition_name, model_Transition_trigger}
model_Transition.methods={model_Transition_m_accepts, model_Transition_m_on}

# model_State class attributes and methods
model_State_m_onEnter: Method = Method(name="onEnter", parameters={})
model_State_m_onExit: Method = Method(name="onExit", parameters={})
model_State.methods={model_State_m_onEnter, model_State_m_onExit}

# AbstractState class attributes and methods

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="1", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=model_FiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoings2: BinaryAssociation = BinaryAssociation(
    name="outgoings2",
    ends={
        Property(name="4", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="14", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
initial5: BinaryAssociation = BinaryAssociation(
    name="initial5",
    ends={
        Property(name="model_AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="8", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=model_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
current9: BinaryAssociation = BinaryAssociation(
    name="current9",
    ends={
        Property(name="model_AbstractState11", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine10", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="model_AbstractState16", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_FiniteStateMachine_AbstractState = Generalization(general=AbstractState, specific=model_FiniteStateMachine)
gen_model_State_AbstractState = Generalization(general=AbstractState, specific=model_State)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_AbstractState, model_FiniteStateMachine, model_Transition, model_State, AbstractState},
    associations={parent0, outgoings2, source12, initial5, states6, current9, target15},
    generalizations={gen_model_FiniteStateMachine_AbstractState, gen_model_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)