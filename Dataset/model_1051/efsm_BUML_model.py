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
efsm_EFSM = Class(name="efsm_EFSM")
efsm_Transition = Class(name="efsm_Transition")
efsm_InitialState = Class(name="efsm_InitialState")
efsm_State = Class(name="efsm_State")
efsm_ContextVariable = Class(name="efsm_ContextVariable")
efsm_AbstractState = Class(name="efsm_AbstractState", is_abstract=True)
AbstractState = Class(name="AbstractState")

# efsm_EFSM class attributes and methods
efsm_EFSM_name: Property = Property(name="name", type=StringType)
efsm_EFSM.attributes={efsm_EFSM_name}

# efsm_Transition class attributes and methods
efsm_Transition_name: Property = Property(name="name", type=StringType)
efsm_Transition_input: Property = Property(name="input", type=StringType)
efsm_Transition_output: Property = Property(name="output", type=StringType)
efsm_Transition_event: Property = Property(name="event", type=StringType)
efsm_Transition_guard: Property = Property(name="guard", type=StringType)
efsm_Transition_action: Property = Property(name="action", type=StringType)
efsm_Transition.attributes={efsm_Transition_event, efsm_Transition_guard, efsm_Transition_output, efsm_Transition_name, efsm_Transition_action, efsm_Transition_input}

# efsm_InitialState class attributes and methods

# efsm_State class attributes and methods

# efsm_ContextVariable class attributes and methods
efsm_ContextVariable_name: Property = Property(name="name", type=StringType)
efsm_ContextVariable_type: Property = Property(name="type", type=StringType)
efsm_ContextVariable.attributes={efsm_ContextVariable_name, efsm_ContextVariable_type}

# efsm_AbstractState class attributes and methods
efsm_AbstractState_name: Property = Property(name="name", type=StringType)
efsm_AbstractState.attributes={efsm_AbstractState_name}

# AbstractState class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="efsm_Transition", type=efsm_EFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_EFSM", type=efsm_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialstate1: BinaryAssociation = BinaryAssociation(
    name="initialstate1",
    ends={
        Property(name="efsm_InitialState", type=efsm_EFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_EFSM2", type=efsm_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="efsm_State", type=efsm_EFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_EFSM4", type=efsm_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="efsm_ContextVariable", type=efsm_EFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_EFSM6", type=efsm_ContextVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="efsm_AbstractState", type=efsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Transition8", type=efsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="efsm_AbstractState11", type=efsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Transition10", type=efsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_efsm_InitialState_AbstractState = Generalization(general=AbstractState, specific=efsm_InitialState)
gen_efsm_State_AbstractState = Generalization(general=AbstractState, specific=efsm_State)

# Domain Model
domain_model = DomainModel(
    name="efsm",
    types={efsm_EFSM, efsm_Transition, efsm_InitialState, efsm_State, efsm_ContextVariable, efsm_AbstractState, AbstractState},
    associations={transitions0, initialstate1, states3, variables5, source7, target9},
    generalizations={gen_efsm_InitialState_AbstractState, gen_efsm_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)