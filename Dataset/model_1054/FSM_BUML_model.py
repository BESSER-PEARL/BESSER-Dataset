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
FSM_StateMachine = Class(name="FSM::StateMachine")
FSM_AbstractState = Class(name="FSM::AbstractState", is_abstract=True)
FSM_Transition = Class(name="FSM::Transition")
FSM_StartState = Class(name="FSM::StartState")
AbstractState = Class(name="AbstractState")
FSM_State = Class(name="FSM::State")
FSM_EndState = Class(name="FSM::EndState")

# FSM_StateMachine class attributes and methods
FSM_StateMachine_code: Property = Property(name="code", type=StringType)
FSM_StateMachine.attributes={FSM_StateMachine_code}

# FSM_AbstractState class attributes and methods
FSM_AbstractState_name: Property = Property(name="name", type=StringType)
FSM_AbstractState_envs: Property = Property(name="envs", type=StringType)
FSM_AbstractState.attributes={FSM_AbstractState_name, FSM_AbstractState_envs}

# FSM_Transition class attributes and methods

# FSM_StartState class attributes and methods

# AbstractState class attributes and methods

# FSM_State class attributes and methods

# FSM_EndState class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="FSM_AbstractState", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine", type=FSM_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="FSM_Transition", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine2", type=FSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="FSM_Transition8", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_AbstractState7", type=FSM_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="FSM_Transition5", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_AbstractState4", type=FSM_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_FSM_StartState_AbstractState = Generalization(general=AbstractState, specific=FSM_StartState)
gen_FSM_State_AbstractState = Generalization(general=AbstractState, specific=FSM_State)
gen_FSM_EndState_AbstractState = Generalization(general=AbstractState, specific=FSM_EndState)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_StateMachine, FSM_AbstractState, FSM_Transition, FSM_StartState, AbstractState, FSM_State, FSM_EndState},
    associations={states0, transitions1, target6, source3},
    generalizations={gen_FSM_StartState_AbstractState, gen_FSM_State_AbstractState, gen_FSM_EndState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)