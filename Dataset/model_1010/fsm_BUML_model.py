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
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_FSM = Class(name="fsm::FSM")
fsm_Initial = Class(name="fsm::Initial")
fsm_Final = Class(name="fsm::Final")
State = Class(name="State")

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition_trigger: Property = Property(name="trigger", type=StringType)
fsm_Transition.attributes={fsm_Transition_name, fsm_Transition_trigger}

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_Initial class attributes and methods

# fsm_Final class attributes and methods

# State class attributes and methods

# Relationships
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
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="fsm_State", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="fsm_State3", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition2", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
initial9: BinaryAssociation = BinaryAssociation(
    name="initial9",
    ends={
        Property(name="fsm_Initial", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM10", type=fsm_Initial, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
final11: BinaryAssociation = BinaryAssociation(
    name="final11",
    ends={
        Property(name="fsm_Final", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM12", type=fsm_Final, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fsm_Initial_State = Generalization(general=State, specific=fsm_Initial)
gen_fsm_Final_State = Generalization(general=State, specific=fsm_Final)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State, fsm_Transition, fsm_FSM, fsm_Initial, fsm_Final, State},
    associations={state4, transition6, source0, target1, initial9, final11},
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