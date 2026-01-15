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
tfsm_FSM = Class(name="tfsm::FSM")
FSM = Class(name="FSM")
tfsm_State = Class(name="tfsm::State")
State = Class(name="State")
tfsm_Transition = Class(name="tfsm::Transition")
Transition = Class(name="Transition")
tfsm_Guard = Class(name="tfsm::Guard")

# tfsm_FSM class attributes and methods

# FSM class attributes and methods

# tfsm_State class attributes and methods
tfsm_State_time: Property = Property(name="time", type=IntegerType)
tfsm_State.attributes={tfsm_State_time}

# State class attributes and methods

# tfsm_Transition class attributes and methods

# Transition class attributes and methods

# tfsm_Guard class attributes and methods
tfsm_Guard_time: Property = Property(name="time", type=IntegerType)
tfsm_Guard.attributes={tfsm_Guard_time}

# Relationships
currentState0: BinaryAssociation = BinaryAssociation(
    name="currentState0",
    ends={
        Property(name="tfsm_State", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM", type=tfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
guard1: BinaryAssociation = BinaryAssociation(
    name="guard1",
    ends={
        Property(name="tfsm_Guard", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition", type=tfsm_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_tfsm_FSM_FSM = Generalization(general=FSM, specific=tfsm_FSM)
gen_tfsm_State_State = Generalization(general=State, specific=tfsm_State)
gen_tfsm_Transition_Transition = Generalization(general=Transition, specific=tfsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_FSM, FSM, tfsm_State, State, tfsm_Transition, Transition, tfsm_Guard},
    associations={currentState0, guard1},
    generalizations={gen_tfsm_FSM_FSM, gen_tfsm_State_State, gen_tfsm_Transition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)