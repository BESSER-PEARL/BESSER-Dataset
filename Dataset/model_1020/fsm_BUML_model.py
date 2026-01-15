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
fsm_Transition = Class(name="fsm::Transition")
fsm_State = Class(name="fsm::State")
fsm_FSM = Class(name="fsm::FSM")
fsm_Final = Class(name="fsm::Final")
State = Class(name="State")
fsm_Initial = Class(name="fsm::Initial")

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition.attributes={fsm_Transition_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_Final class attributes and methods

# State class attributes and methods

# fsm_Initial class attributes and methods

# Relationships
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="fsm_State", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
state21: BinaryAssociation = BinaryAssociation(
    name="state21",
    ends={
        Property(name="fsm_State3", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition2", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
state4: BinaryAssociation = BinaryAssociation(
    name="state4",
    ends={
        Property(name="fsm_State5", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition6: BinaryAssociation = BinaryAssociation(
    name="transition6",
    ends={
        Property(name="fsm_Transition8", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM7", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_Final_State = Generalization(general=State, specific=fsm_Final)
gen_fsm_Initial_State = Generalization(general=State, specific=fsm_Initial)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Transition, fsm_State, fsm_FSM, fsm_Final, State, fsm_Initial},
    associations={state10, state21, state4, transition6},
    generalizations={gen_fsm_Final_State, gen_fsm_Initial_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)