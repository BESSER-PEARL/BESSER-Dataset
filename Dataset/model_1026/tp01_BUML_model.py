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
tp01_FSM = Class(name="tp01::FSM")
tp01_StartState = Class(name="tp01::StartState")
State = Class(name="State")
tp01_FinalState = Class(name="tp01::FinalState")
tp01_State = Class(name="tp01::State")
tp01_Transition = Class(name="tp01::Transition")

# tp01_FSM class attributes and methods
tp01_FSM_name: Property = Property(name="name", type=StringType)
tp01_FSM.attributes={tp01_FSM_name}

# tp01_StartState class attributes and methods

# State class attributes and methods

# tp01_FinalState class attributes and methods

# tp01_State class attributes and methods
tp01_State_name: Property = Property(name="name", type=StringType)
tp01_State.attributes={tp01_State_name}

# tp01_Transition class attributes and methods
tp01_Transition_name: Property = Property(name="name", type=StringType)
tp01_Transition.attributes={tp01_Transition_name}

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="tp01_State5", type=tp01_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tp01_Transition4", type=tp01_State, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="tp01_State8", type=tp01_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tp01_Transition7", type=tp01_State, multiplicity=Multiplicity(1, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="tp01_State", type=tp01_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tp01_FSM", type=tp01_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="tp01_Transition", type=tp01_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tp01_FSM2", type=tp01_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tp01_StartState_State = Generalization(general=State, specific=tp01_StartState)
gen_tp01_FinalState_State = Generalization(general=State, specific=tp01_FinalState)

# Domain Model
domain_model = DomainModel(
    name="tp01",
    types={tp01_FSM, tp01_StartState, State, tp01_FinalState, tp01_State, tp01_Transition},
    associations={source3, target6, state0, transition1},
    generalizations={gen_tp01_StartState_State, gen_tp01_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)