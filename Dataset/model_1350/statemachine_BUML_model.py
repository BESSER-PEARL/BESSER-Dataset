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
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_FiringElement = Class(name="statemachine::FiringElement", is_abstract=True)
statemachine_StateMachine = Class(name="statemachine::StateMachine")
statemachine_AbstractState = Class(name="statemachine::AbstractState", is_abstract=True)
statemachine_InitialState = Class(name="statemachine::InitialState")
statemachine_FinalState = Class(name="statemachine::FinalState")
statemachine_State = Class(name="statemachine::State")
AbstractState = Class(name="AbstractState")
statemachine_StateAction = Class(name="statemachine::StateAction")
FiringElement = Class(name="FiringElement")

# statemachine_Transition class attributes and methods

# statemachine_FiringElement class attributes and methods
statemachine_FiringElement_action: Property = Property(name="action", type=StringType)
statemachine_FiringElement_trigger: Property = Property(name="trigger", type=StringType)
statemachine_FiringElement.attributes={statemachine_FiringElement_trigger, statemachine_FiringElement_action}

# statemachine_StateMachine class attributes and methods

# statemachine_AbstractState class attributes and methods
statemachine_AbstractState_name: Property = Property(name="name", type=StringType)
statemachine_AbstractState.attributes={statemachine_AbstractState_name}

# statemachine_InitialState class attributes and methods

# statemachine_FinalState class attributes and methods

# statemachine_State class attributes and methods

# AbstractState class attributes and methods

# statemachine_StateAction class attributes and methods

# FiringElement class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_AbstractState", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalActions6: BinaryAssociation = BinaryAssociation(
    name="internalActions6",
    ends={
        Property(name="statemachine_State", type=statemachine_StateAction, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="statemachine_StateAction", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
transitionsAsSource3: BinaryAssociation = BinaryAssociation(
    name="transitionsAsSource3",
    ends={
        Property(name="Transition", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transitionsAsTarget4: BinaryAssociation = BinaryAssociation(
    name="transitionsAsTarget4",
    ends={
        Property(name="Transition5", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="AbstractState", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionsAsSource", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="AbstractState9", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionsAsTarget", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachine_InitialState_AbstractState = Generalization(general=AbstractState, specific=statemachine_InitialState)
gen_statemachine_FinalState_AbstractState = Generalization(general=AbstractState, specific=statemachine_FinalState)
gen_statemachine_State_AbstractState = Generalization(general=AbstractState, specific=statemachine_State)
gen_statemachine_StateAction_FiringElement = Generalization(general=FiringElement, specific=statemachine_StateAction)
gen_statemachine_Transition_FiringElement = Generalization(general=FiringElement, specific=statemachine_Transition)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Transition, statemachine_FiringElement, statemachine_StateMachine, statemachine_AbstractState, statemachine_InitialState, statemachine_FinalState, statemachine_State, AbstractState, statemachine_StateAction, FiringElement},
    associations={states0, transitions1, internalActions6, transitionsAsSource3, transitionsAsTarget4, source7, target8},
    generalizations={gen_statemachine_InitialState_AbstractState, gen_statemachine_FinalState_AbstractState, gen_statemachine_State_AbstractState, gen_statemachine_StateAction_FiringElement, gen_statemachine_Transition_FiringElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)