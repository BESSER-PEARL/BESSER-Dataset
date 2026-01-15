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
dsl_FSM = Class(name="dsl::FSM")
dsl_State = Class(name="dsl::State")
dsl_Transition = Class(name="dsl::Transition")
dsl_InitialState = Class(name="dsl::InitialState")
State = Class(name="State")

# dsl_FSM class attributes and methods
dsl_FSM_name: Property = Property(name="name", type=StringType)
dsl_FSM.attributes={dsl_FSM_name}

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
dsl_State.attributes={dsl_State_isFinal, dsl_State_name}

# dsl_Transition class attributes and methods
dsl_Transition_name: Property = Property(name="name", type=StringType)
dsl_Transition_trigger: Property = Property(name="trigger", type=StringType)
dsl_Transition.attributes={dsl_Transition_name, dsl_Transition_trigger}

# dsl_InitialState class attributes and methods

# State class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="dsl_State", type=dsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FSM", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="dsl_Transition", type=dsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FSM2", type=dsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate3: BinaryAssociation = BinaryAssociation(
    name="initialstate3",
    ends={
        Property(name="dsl_InitialState", type=dsl_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FSM4", type=dsl_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="dsl_State7", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition6", type=dsl_State, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="dsl_State10", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition9", type=dsl_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dsl_InitialState_State = Generalization(general=State, specific=dsl_InitialState)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_FSM, dsl_State, dsl_Transition, dsl_InitialState, State},
    associations={state0, transition1, initialstate3, target5, source8},
    generalizations={gen_dsl_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)