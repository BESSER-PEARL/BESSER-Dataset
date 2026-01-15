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
fsm_FSM = Class(name="fsm::FSM")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_Initial = Class(name="fsm::Initial")
State = Class(name="State")
fsm_Final = Class(name="fsm::Final")

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition.attributes={fsm_Transition_name}

# fsm_Initial class attributes and methods

# State class attributes and methods

# fsm_Final class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="fsm_Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state13: BinaryAssociation = BinaryAssociation(
    name="state13",
    ends={
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition4", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
state26: BinaryAssociation = BinaryAssociation(
    name="state26",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition7", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fsm_Initial_State = Generalization(general=State, specific=fsm_Initial)
gen_fsm_Final_State = Generalization(general=State, specific=fsm_Final)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_Initial, State, fsm_Final},
    associations={state0, transition1, state13, state26},
    generalizations={gen_fsm_Initial_State, gen_fsm_Final_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)