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
efsm_Transition = Class(name="efsm::Transition")
efsm_InitialState = Class(name="efsm::InitialState")
efsm_State = Class(name="efsm::State")
efsm_ContextVariable = Class(name="efsm::ContextVariable")
efsm_AbstractState = Class(name="efsm::AbstractState", is_abstract=True)
efsm_EFSM = Class(name="efsm::EFSM")
efsm_Input = Class(name="efsm::Input")
efsm_Event = Class(name="efsm::Event")
AbstractState = Class(name="AbstractState")
efsm_Variable = Class(name="efsm::Variable")
efsm_Param = Class(name="efsm::Param")

# efsm_Transition class attributes and methods
efsm_Transition_name: Property = Property(name="name", type=StringType)
efsm_Transition_output: Property = Property(name="output", type=StringType)
efsm_Transition_guard: Property = Property(name="guard", type=StringType)
efsm_Transition_action: Property = Property(name="action", type=StringType)
efsm_Transition.attributes={efsm_Transition_action, efsm_Transition_name, efsm_Transition_guard, efsm_Transition_output}

# efsm_InitialState class attributes and methods

# efsm_State class attributes and methods

# efsm_ContextVariable class attributes and methods
efsm_ContextVariable_name: Property = Property(name="name", type=StringType)
efsm_ContextVariable_type: Property = Property(name="type", type=StringType)
efsm_ContextVariable.attributes={efsm_ContextVariable_name, efsm_ContextVariable_type}

# efsm_AbstractState class attributes and methods
efsm_AbstractState_name: Property = Property(name="name", type=StringType)
efsm_AbstractState.attributes={efsm_AbstractState_name}

# efsm_EFSM class attributes and methods
efsm_EFSM_name: Property = Property(name="name", type=StringType)
efsm_EFSM.attributes={efsm_EFSM_name}

# efsm_Input class attributes and methods
efsm_Input_name: Property = Property(name="name", type=StringType)
efsm_Input.attributes={efsm_Input_name}

# efsm_Event class attributes and methods
efsm_Event_name: Property = Property(name="name", type=StringType)
efsm_Event_return: Property = Property(name="return", type=StringType)
efsm_Event_class: Property = Property(name="class", type=StringType)
efsm_Event.attributes={efsm_Event_class, efsm_Event_name, efsm_Event_return}

# AbstractState class attributes and methods

# efsm_Variable class attributes and methods
efsm_Variable_name: Property = Property(name="name", type=StringType)
efsm_Variable_type: Property = Property(name="type", type=StringType)
efsm_Variable_class: Property = Property(name="class", type=StringType)
efsm_Variable.attributes={efsm_Variable_type, efsm_Variable_class, efsm_Variable_name}

# efsm_Param class attributes and methods
efsm_Param_argName: Property = Property(name="argName", type=StringType)
efsm_Param_argType: Property = Property(name="argType", type=StringType)
efsm_Param.attributes={efsm_Param_argName, efsm_Param_argType}

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
contextVariables5: BinaryAssociation = BinaryAssociation(
    name="contextVariables5",
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
input12: BinaryAssociation = BinaryAssociation(
    name="input12",
    ends={
        Property(name="efsm_Input", type=efsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Transition13", type=efsm_Input, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
event14: BinaryAssociation = BinaryAssociation(
    name="event14",
    ends={
        Property(name="efsm_Event", type=efsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Transition15", type=efsm_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables16: BinaryAssociation = BinaryAssociation(
    name="variables16",
    ends={
        Property(name="efsm_Variable", type=efsm_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Input17", type=efsm_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args18: BinaryAssociation = BinaryAssociation(
    name="args18",
    ends={
        Property(name="efsm_Param", type=efsm_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="efsm_Event19", type=efsm_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_efsm_InitialState_AbstractState = Generalization(general=AbstractState, specific=efsm_InitialState)
gen_efsm_State_AbstractState = Generalization(general=AbstractState, specific=efsm_State)

# Domain Model
domain_model = DomainModel(
    name="efsm",
    types={efsm_Transition, efsm_InitialState, efsm_State, efsm_ContextVariable, efsm_AbstractState, efsm_EFSM, efsm_Input, efsm_Event, AbstractState, efsm_Variable, efsm_Param},
    associations={transitions0, initialstate1, states3, contextVariables5, source7, target9, input12, event14, variables16, args18},
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