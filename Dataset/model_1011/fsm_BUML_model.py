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
fsm_State = Class(name="fsm::State", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")
fsm_StateOn = Class(name="fsm::StateOn")
State = Class(name="State")
fsm_StateOff = Class(name="fsm::StateOff")
fsm_StateFinal = Class(name="fsm::StateFinal")

# fsm_FSM class attributes and methods
fsm_FSM_name: Property = Property(name="name", type=StringType)
fsm_FSM.attributes={fsm_FSM_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition.attributes={fsm_Transition_name}

# fsm_StateOn class attributes and methods

# State class attributes and methods

# fsm_StateOff class attributes and methods

# fsm_StateFinal class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="fsm_Transition", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition4", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition7", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateOn_State = Generalization(general=State, specific=fsm_StateOn)
gen_fsm_StateOff_State = Generalization(general=State, specific=fsm_StateOff)
gen_fsm_StateFinal_State = Generalization(general=State, specific=fsm_StateFinal)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_Transition, fsm_StateOn, State, fsm_StateOff, fsm_StateFinal},
    associations={state0, transition1, source3, target6},
    generalizations={gen_fsm_StateOn_State, gen_fsm_StateOff_State, gen_fsm_StateFinal_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)