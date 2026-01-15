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
fMS_InitState = Class(name="fMS::InitState")
State = Class(name="State")
fMS_FinalState = Class(name="fMS::FinalState")
fMS_FSM = Class(name="fMS::FSM")
fMS_State = Class(name="fMS::State")
fMS_Transition = Class(name="fMS::Transition")

# fMS_InitState class attributes and methods

# State class attributes and methods

# fMS_FinalState class attributes and methods

# fMS_FSM class attributes and methods
fMS_FSM_name: Property = Property(name="name", type=StringType)
fMS_FSM.attributes={fMS_FSM_name}

# fMS_State class attributes and methods
fMS_State_name: Property = Property(name="name", type=StringType)
fMS_State.attributes={fMS_State_name}

# fMS_Transition class attributes and methods
fMS_Transition_name: Property = Property(name="name", type=StringType)
fMS_Transition.attributes={fMS_Transition_name}

# Relationships
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="fMS_Transition", type=fMS_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fMS_FSM2", type=fMS_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateStart3: BinaryAssociation = BinaryAssociation(
    name="stateStart3",
    ends={
        Property(name="fMS_State5", type=fMS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fMS_Transition4", type=fMS_State, multiplicity=Multiplicity(0, 1))
    }
)
stateEnd6: BinaryAssociation = BinaryAssociation(
    name="stateEnd6",
    ends={
        Property(name="fMS_State8", type=fMS_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fMS_Transition7", type=fMS_State, multiplicity=Multiplicity(0, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fMS_State", type=fMS_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fMS_FSM", type=fMS_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fMS_InitState_State = Generalization(general=State, specific=fMS_InitState)
gen_fMS_FinalState_State = Generalization(general=State, specific=fMS_FinalState)

# Domain Model
domain_model = DomainModel(
    name="fMS",
    types={fMS_InitState, State, fMS_FinalState, fMS_FSM, fMS_State, fMS_Transition},
    associations={transition1, stateStart3, stateEnd6, state0},
    generalizations={gen_fMS_InitState_State, gen_fMS_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)