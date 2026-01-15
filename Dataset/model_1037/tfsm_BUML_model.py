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
tfsm_ClockReset = Class(name="tfsm::ClockReset")
tfsm_ClockConstraint = Class(name="tfsm::ClockConstraint", is_abstract=True)
ClockConstraintOperation = Class(name="ClockConstraintOperation")
tfsm_Clock = Class(name="tfsm::Clock")
tfsm_LowerClockConstraint = Class(name="tfsm::LowerClockConstraint")
ClockConstraint = Class(name="ClockConstraint")
tfsm_LowerEqualClockConstraint = Class(name="tfsm::LowerEqualClockConstraint")
tfsm_State = Class(name="tfsm::State")
tfsm_Transition = Class(name="tfsm::Transition")
tfsm_InitialState = Class(name="tfsm::InitialState")
tfsm_ClockConstraintOperation = Class(name="tfsm::ClockConstraintOperation", is_abstract=True)
tfsm_UpperClockConstraint = Class(name="tfsm::UpperClockConstraint")
tfsm_UpperEqualClockConstraint = Class(name="tfsm::UpperEqualClockConstraint")
tfsm_AndClockConstraint = Class(name="tfsm::AndClockConstraint")
BinaryClockConstraint = Class(name="BinaryClockConstraint")
tfsm_OrClockConstraint = Class(name="tfsm::OrClockConstraint")
tfsm_BinaryClockConstraint = Class(name="tfsm::BinaryClockConstraint", is_abstract=True)
tfsm_FinalState = Class(name="tfsm::FinalState")
State = Class(name="State")

# tfsm_FSM class attributes and methods
tfsm_FSM_name: Property = Property(name="name", type=StringType)
tfsm_FSM.attributes={tfsm_FSM_name}

# tfsm_ClockReset class attributes and methods

# tfsm_ClockConstraint class attributes and methods
tfsm_ClockConstraint_threshold: Property = Property(name="threshold", type=IntegerType)
tfsm_ClockConstraint.attributes={tfsm_ClockConstraint_threshold}

# ClockConstraintOperation class attributes and methods

# tfsm_Clock class attributes and methods
tfsm_Clock_name: Property = Property(name="name", type=StringType)
tfsm_Clock_tick: Property = Property(name="tick", type=IntegerType)
tfsm_Clock.attributes={tfsm_Clock_tick, tfsm_Clock_name}

# tfsm_LowerClockConstraint class attributes and methods

# ClockConstraint class attributes and methods

# tfsm_LowerEqualClockConstraint class attributes and methods

# tfsm_State class attributes and methods
tfsm_State_name: Property = Property(name="name", type=StringType)
tfsm_State.attributes={tfsm_State_name}

# tfsm_Transition class attributes and methods
tfsm_Transition_event: Property = Property(name="event", type=StringType)
tfsm_Transition.attributes={tfsm_Transition_event}

# tfsm_InitialState class attributes and methods

# tfsm_ClockConstraintOperation class attributes and methods

# tfsm_UpperClockConstraint class attributes and methods

# tfsm_UpperEqualClockConstraint class attributes and methods

# tfsm_AndClockConstraint class attributes and methods

# BinaryClockConstraint class attributes and methods

# tfsm_OrClockConstraint class attributes and methods

# tfsm_BinaryClockConstraint class attributes and methods

# tfsm_FinalState class attributes and methods

# State class attributes and methods

# Relationships
incommingtransitions16: BinaryAssociation = BinaryAssociation(
    name="incommingtransitions16",
    ends={
        Property(name="Transition17", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
clockresets18: BinaryAssociation = BinaryAssociation(
    name="clockresets18",
    ends={
        Property(name="tfsm_ClockReset", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition19", type=tfsm_ClockReset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionguard20: BinaryAssociation = BinaryAssociation(
    name="transitionguard20",
    ends={
        Property(name="tfsm_ClockConstraintOperation22", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_Transition21", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from23: BinaryAssociation = BinaryAssociation(
    name="from23",
    ends={
        Property(name="State", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingtransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
to24: BinaryAssociation = BinaryAssociation(
    name="to24",
    ends={
        Property(name="State25", type=tfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incommingtransitions", type=tfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
clock26: BinaryAssociation = BinaryAssociation(
    name="clock26",
    ends={
        Property(name="tfsm_Clock27", type=tfsm_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_ClockConstraint", type=tfsm_Clock, multiplicity=Multiplicity(1, 1))
    }
)
clock28: BinaryAssociation = BinaryAssociation(
    name="clock28",
    ends={
        Property(name="tfsm_Clock30", type=tfsm_ClockReset, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_ClockReset29", type=tfsm_Clock, multiplicity=Multiplicity(1, 1))
    }
)
clocks0: BinaryAssociation = BinaryAssociation(
    name="clocks0",
    ends={
        Property(name="tfsm_Clock", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM", type=tfsm_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="tfsm_State", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM2", type=tfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="tfsm_Transition", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM4", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate5: BinaryAssociation = BinaryAssociation(
    name="initialstate5",
    ends={
        Property(name="tfsm_InitialState", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM6", type=tfsm_InitialState, multiplicity=Multiplicity(1, 1))
    }
)
currentState7: BinaryAssociation = BinaryAssociation(
    name="currentState7",
    ends={
        Property(name="tfsm_State9", type=tfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_FSM8", type=tfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
stateguard10: BinaryAssociation = BinaryAssociation(
    name="stateguard10",
    ends={
        Property(name="tfsm_ClockConstraintOperation", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_State11", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fsm12: BinaryAssociation = BinaryAssociation(
    name="fsm12",
    ends={
        Property(name="tfsm_FSM14", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_State13", type=tfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingtransitions15: BinaryAssociation = BinaryAssociation(
    name="outgoingtransitions15",
    ends={
        Property(name="Transition", type=tfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=tfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="tfsm_ClockConstraintOperation32", type=tfsm_BinaryClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_BinaryClockConstraint", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="tfsm_ClockConstraintOperation35", type=tfsm_BinaryClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_BinaryClockConstraint34", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_tfsm_ClockConstraint_ClockConstraintOperation = Generalization(general=ClockConstraintOperation, specific=tfsm_ClockConstraint)
gen_tfsm_LowerClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_LowerClockConstraint)
gen_tfsm_LowerEqualClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_LowerEqualClockConstraint)
gen_tfsm_UpperClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_UpperClockConstraint)
gen_tfsm_UpperEqualClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_UpperEqualClockConstraint)
gen_tfsm_AndClockConstraint_BinaryClockConstraint = Generalization(general=BinaryClockConstraint, specific=tfsm_AndClockConstraint)
gen_tfsm_OrClockConstraint_BinaryClockConstraint = Generalization(general=BinaryClockConstraint, specific=tfsm_OrClockConstraint)
gen_tfsm_BinaryClockConstraint_ClockConstraintOperation = Generalization(general=ClockConstraintOperation, specific=tfsm_BinaryClockConstraint)
gen_tfsm_FinalState_State = Generalization(general=State, specific=tfsm_FinalState)
gen_tfsm_InitialState_State = Generalization(general=State, specific=tfsm_InitialState)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_FSM, tfsm_ClockReset, tfsm_ClockConstraint, ClockConstraintOperation, tfsm_Clock, tfsm_LowerClockConstraint, ClockConstraint, tfsm_LowerEqualClockConstraint, tfsm_State, tfsm_Transition, tfsm_InitialState, tfsm_ClockConstraintOperation, tfsm_UpperClockConstraint, tfsm_UpperEqualClockConstraint, tfsm_AndClockConstraint, BinaryClockConstraint, tfsm_OrClockConstraint, tfsm_BinaryClockConstraint, tfsm_FinalState, State},
    associations={incommingtransitions16, clockresets18, transitionguard20, from23, to24, clock26, clock28, clocks0, states1, transitions3, initialstate5, currentState7, stateguard10, fsm12, outgoingtransitions15, left31, right33},
    generalizations={gen_tfsm_ClockConstraint_ClockConstraintOperation, gen_tfsm_LowerClockConstraint_ClockConstraint, gen_tfsm_LowerEqualClockConstraint_ClockConstraint, gen_tfsm_UpperClockConstraint_ClockConstraint, gen_tfsm_UpperEqualClockConstraint_ClockConstraint, gen_tfsm_AndClockConstraint_BinaryClockConstraint, gen_tfsm_OrClockConstraint_BinaryClockConstraint, gen_tfsm_BinaryClockConstraint_ClockConstraintOperation, gen_tfsm_FinalState_State, gen_tfsm_InitialState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)