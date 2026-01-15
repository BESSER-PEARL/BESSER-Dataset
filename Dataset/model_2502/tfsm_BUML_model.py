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
tfsm_Clock = Class(name="tfsm::Clock")
tfsm_TimedState = Class(name="tfsm::TimedState")
State = Class(name="State")
tfsm_ClockConstraintOperation = Class(name="tfsm::ClockConstraintOperation", is_abstract=True)
tfsm_TimedTransition = Class(name="tfsm::TimedTransition")
Transition = Class(name="Transition")
tfsm_TimedFSM = Class(name="tfsm::TimedFSM")
FSM = Class(name="FSM")
ClockConstraintOperation = Class(name="ClockConstraintOperation")
tfsm_ClockReset = Class(name="tfsm::ClockReset")
tfsm_ClockConstraint = Class(name="tfsm::ClockConstraint", is_abstract=True)
tfsm_UpperClockConstraint = Class(name="tfsm::UpperClockConstraint")
tfsm_UpperEqualClockConstraint = Class(name="tfsm::UpperEqualClockConstraint")
tfsm_LowerClockConstraint = Class(name="tfsm::LowerClockConstraint")
ClockConstraint = Class(name="ClockConstraint")
tfsm_LowerEqualClockConstraint = Class(name="tfsm::LowerEqualClockConstraint")
tfsm_TimedFinalState = Class(name="tfsm::TimedFinalState")
tfsm_AndClockConstraint = Class(name="tfsm::AndClockConstraint")
BinaryClockConstraint = Class(name="BinaryClockConstraint")
tfsm_OrClockConstraint = Class(name="tfsm::OrClockConstraint")
tfsm_BinaryClockConstraint = Class(name="tfsm::BinaryClockConstraint", is_abstract=True)
FinalState = Class(name="FinalState")
TimedState = Class(name="TimedState")
tfsm_TimedInitialState = Class(name="tfsm::TimedInitialState")
InitialState = Class(name="InitialState")

# tfsm_Clock class attributes and methods
tfsm_Clock_name: Property = Property(name="name", type=StringType)
tfsm_Clock_tick: Property = Property(name="tick", type=IntegerType)
tfsm_Clock.attributes={tfsm_Clock_name, tfsm_Clock_tick}

# tfsm_TimedState class attributes and methods

# State class attributes and methods

# tfsm_ClockConstraintOperation class attributes and methods

# tfsm_TimedTransition class attributes and methods

# Transition class attributes and methods

# tfsm_TimedFSM class attributes and methods

# FSM class attributes and methods

# ClockConstraintOperation class attributes and methods

# tfsm_ClockReset class attributes and methods

# tfsm_ClockConstraint class attributes and methods
tfsm_ClockConstraint_threshold: Property = Property(name="threshold", type=IntegerType)
tfsm_ClockConstraint.attributes={tfsm_ClockConstraint_threshold}

# tfsm_UpperClockConstraint class attributes and methods

# tfsm_UpperEqualClockConstraint class attributes and methods

# tfsm_LowerClockConstraint class attributes and methods

# ClockConstraint class attributes and methods

# tfsm_LowerEqualClockConstraint class attributes and methods

# tfsm_TimedFinalState class attributes and methods

# tfsm_AndClockConstraint class attributes and methods

# BinaryClockConstraint class attributes and methods

# tfsm_OrClockConstraint class attributes and methods

# tfsm_BinaryClockConstraint class attributes and methods

# FinalState class attributes and methods

# TimedState class attributes and methods

# tfsm_TimedInitialState class attributes and methods

# InitialState class attributes and methods

# Relationships
clocks0: BinaryAssociation = BinaryAssociation(
    name="clocks0",
    ends={
        Property(name="tfsm_Clock", type=tfsm_TimedFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedFSM", type=tfsm_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateguard1: BinaryAssociation = BinaryAssociation(
    name="stateguard1",
    ends={
        Property(name="tfsm_ClockConstraintOperation", type=tfsm_TimedState, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedState", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clock6: BinaryAssociation = BinaryAssociation(
    name="clock6",
    ends={
        Property(name="tfsm_Clock7", type=tfsm_ClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_ClockConstraint", type=tfsm_Clock, multiplicity=Multiplicity(1, 1))
    }
)
clockresets2: BinaryAssociation = BinaryAssociation(
    name="clockresets2",
    ends={
        Property(name="tfsm_ClockReset", type=tfsm_TimedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedTransition", type=tfsm_ClockReset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionguard3: BinaryAssociation = BinaryAssociation(
    name="transitionguard3",
    ends={
        Property(name="tfsm_ClockConstraintOperation5", type=tfsm_TimedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_TimedTransition4", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clock8: BinaryAssociation = BinaryAssociation(
    name="clock8",
    ends={
        Property(name="tfsm_Clock10", type=tfsm_ClockReset, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_ClockReset9", type=tfsm_Clock, multiplicity=Multiplicity(1, 1))
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="tfsm_ClockConstraintOperation15", type=tfsm_BinaryClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_BinaryClockConstraint14", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="tfsm_ClockConstraintOperation12", type=tfsm_BinaryClockConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tfsm_BinaryClockConstraint", type=tfsm_ClockConstraintOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_tfsm_TimedState_State = Generalization(general=State, specific=tfsm_TimedState)
gen_tfsm_TimedTransition_Transition = Generalization(general=Transition, specific=tfsm_TimedTransition)
gen_tfsm_TimedFSM_FSM = Generalization(general=FSM, specific=tfsm_TimedFSM)
gen_tfsm_ClockConstraint_ClockConstraintOperation = Generalization(general=ClockConstraintOperation, specific=tfsm_ClockConstraint)
gen_tfsm_UpperClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_UpperClockConstraint)
gen_tfsm_UpperEqualClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_UpperEqualClockConstraint)
gen_tfsm_LowerClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_LowerClockConstraint)
gen_tfsm_LowerEqualClockConstraint_ClockConstraint = Generalization(general=ClockConstraint, specific=tfsm_LowerEqualClockConstraint)
gen_tfsm_AndClockConstraint_BinaryClockConstraint = Generalization(general=BinaryClockConstraint, specific=tfsm_AndClockConstraint)
gen_tfsm_OrClockConstraint_BinaryClockConstraint = Generalization(general=BinaryClockConstraint, specific=tfsm_OrClockConstraint)
gen_tfsm_BinaryClockConstraint_ClockConstraintOperation = Generalization(general=ClockConstraintOperation, specific=tfsm_BinaryClockConstraint)
gen_tfsm_TimedFinalState_FinalState = Generalization(general=FinalState, specific=tfsm_TimedFinalState)
gen_tfsm_TimedFinalState_TimedState = Generalization(general=TimedState, specific=tfsm_TimedFinalState)
gen_tfsm_TimedInitialState_TimedState = Generalization(general=TimedState, specific=tfsm_TimedInitialState)
gen_tfsm_TimedInitialState_InitialState = Generalization(general=InitialState, specific=tfsm_TimedInitialState)

# Domain Model
domain_model = DomainModel(
    name="tfsm",
    types={tfsm_Clock, tfsm_TimedState, State, tfsm_ClockConstraintOperation, tfsm_TimedTransition, Transition, tfsm_TimedFSM, FSM, ClockConstraintOperation, tfsm_ClockReset, tfsm_ClockConstraint, tfsm_UpperClockConstraint, tfsm_UpperEqualClockConstraint, tfsm_LowerClockConstraint, ClockConstraint, tfsm_LowerEqualClockConstraint, tfsm_TimedFinalState, tfsm_AndClockConstraint, BinaryClockConstraint, tfsm_OrClockConstraint, tfsm_BinaryClockConstraint, FinalState, TimedState, tfsm_TimedInitialState, InitialState},
    associations={clocks0, stateguard1, clock6, clockresets2, transitionguard3, clock8, right13, left11},
    generalizations={gen_tfsm_TimedState_State, gen_tfsm_TimedTransition_Transition, gen_tfsm_TimedFSM_FSM, gen_tfsm_ClockConstraint_ClockConstraintOperation, gen_tfsm_UpperClockConstraint_ClockConstraint, gen_tfsm_UpperEqualClockConstraint_ClockConstraint, gen_tfsm_LowerClockConstraint_ClockConstraint, gen_tfsm_LowerEqualClockConstraint_ClockConstraint, gen_tfsm_AndClockConstraint_BinaryClockConstraint, gen_tfsm_OrClockConstraint_BinaryClockConstraint, gen_tfsm_BinaryClockConstraint_ClockConstraintOperation, gen_tfsm_TimedFinalState_FinalState, gen_tfsm_TimedFinalState_TimedState, gen_tfsm_TimedInitialState_TimedState, gen_tfsm_TimedInitialState_InitialState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)