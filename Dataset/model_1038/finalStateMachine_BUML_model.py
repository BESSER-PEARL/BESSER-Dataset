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
finalStateMachine_FSM = Class(name="finalStateMachine::FSM")
finalStateMachine_Transition = Class(name="finalStateMachine::Transition")
finalStateMachine_State = Class(name="finalStateMachine::State")
finalStateMachine_FinalState = Class(name="finalStateMachine::FinalState")
State = Class(name="State")
finalStateMachine_InitialState = Class(name="finalStateMachine::InitialState")

# finalStateMachine_FSM class attributes and methods
finalStateMachine_FSM_name: Property = Property(name="name", type=StringType)
finalStateMachine_FSM.attributes={finalStateMachine_FSM_name}

# finalStateMachine_Transition class attributes and methods
finalStateMachine_Transition_name: Property = Property(name="name", type=StringType)
finalStateMachine_Transition.attributes={finalStateMachine_Transition_name}

# finalStateMachine_State class attributes and methods
finalStateMachine_State_name: Property = Property(name="name", type=StringType)
finalStateMachine_State.attributes={finalStateMachine_State_name}

# finalStateMachine_FinalState class attributes and methods

# State class attributes and methods

# finalStateMachine_InitialState class attributes and methods

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="finalStateMachine_Transition", type=finalStateMachine_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="finalStateMachine_FSM", type=finalStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="finalStateMachine_State", type=finalStateMachine_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="finalStateMachine_FSM2", type=finalStateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="finalStateMachine_State5", type=finalStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="finalStateMachine_Transition4", type=finalStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="finalStateMachine_State8", type=finalStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="finalStateMachine_Transition7", type=finalStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_finalStateMachine_FinalState_State = Generalization(general=State, specific=finalStateMachine_FinalState)
gen_finalStateMachine_InitialState_State = Generalization(general=State, specific=finalStateMachine_InitialState)

# Domain Model
domain_model = DomainModel(
    name="finalStateMachine",
    types={finalStateMachine_FSM, finalStateMachine_Transition, finalStateMachine_State, finalStateMachine_FinalState, State, finalStateMachine_InitialState},
    associations={transition0, state1, input3, output6},
    generalizations={gen_finalStateMachine_FinalState_State, gen_finalStateMachine_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)