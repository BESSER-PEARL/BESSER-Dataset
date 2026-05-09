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
State = Class(name="State")
statemachine_FinalState = Class(name="statemachine_FinalState")
statemachine_MyFSM = Class(name="statemachine_MyFSM")
statemachine_State = Class(name="statemachine_State")
statemachine_Transition = Class(name="statemachine_Transition")
statemachine_InitialState = Class(name="statemachine_InitialState")

# State class attributes and methods

# statemachine_FinalState class attributes and methods

# statemachine_MyFSM class attributes and methods
statemachine_MyFSM_name: Property = Property(name="name", type=StringType)
statemachine_MyFSM.attributes={statemachine_MyFSM_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_name: Property = Property(name="name", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_name}

# statemachine_InitialState class attributes and methods

# Relationships
from_5: BinaryAssociation = BinaryAssociation(
    name="from_5",
    ends={
        Property(name="statemachine_State7", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition6", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="statemachine_State10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition9", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="statemachine_State", type=statemachine_MyFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_MyFSM", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr1: BinaryAssociation = BinaryAssociation(
    name="tr1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_MyFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_MyFSM2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate3: BinaryAssociation = BinaryAssociation(
    name="initialstate3",
    ends={
        Property(name="statemachine_InitialState", type=statemachine_MyFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_MyFSM4", type=statemachine_InitialState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemachine_InitialState_State = Generalization(general=State, specific=statemachine_InitialState)
gen_statemachine_FinalState_State = Generalization(general=State, specific=statemachine_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={State, statemachine_FinalState, statemachine_MyFSM, statemachine_State, statemachine_Transition, statemachine_InitialState},
    associations={from_5, to8, state0, tr1, initialstate3},
    generalizations={gen_statemachine_InitialState_State, gen_statemachine_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)