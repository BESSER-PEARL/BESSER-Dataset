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
gfsm_GTransition = Class(name="gfsm::GTransition")
Transition = Class(name="Transition")
gfsm_BooleanExpression = Class(name="gfsm::BooleanExpression")
gfsm_GState = Class(name="gfsm::GState")
State = Class(name="State")
gfsm_IntOperation = Class(name="gfsm::IntOperation")
gfsm_GFinalState = Class(name="gfsm::GFinalState")
GState = Class(name="GState")
FinalState = Class(name="FinalState")
gfsm_GInitialState = Class(name="gfsm::GInitialState")
InitialState = Class(name="InitialState")
gfsm_GFSM = Class(name="gfsm::GFSM")
FSM = Class(name="FSM")

# gfsm_GTransition class attributes and methods

# Transition class attributes and methods

# gfsm_BooleanExpression class attributes and methods

# gfsm_GState class attributes and methods

# State class attributes and methods

# gfsm_IntOperation class attributes and methods

# gfsm_GFinalState class attributes and methods

# GState class attributes and methods

# FinalState class attributes and methods

# gfsm_GInitialState class attributes and methods

# InitialState class attributes and methods

# gfsm_GFSM class attributes and methods

# FSM class attributes and methods

# Relationships
guard0: BinaryAssociation = BinaryAssociation(
    name="guard0",
    ends={
        Property(name="gfsm_BooleanExpression", type=gfsm_GTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_GTransition", type=gfsm_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inExpression1: BinaryAssociation = BinaryAssociation(
    name="inExpression1",
    ends={
        Property(name="gfsm_IntOperation", type=gfsm_GState, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_GState", type=gfsm_IntOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outExpression2: BinaryAssociation = BinaryAssociation(
    name="outExpression2",
    ends={
        Property(name="gfsm_IntOperation4", type=gfsm_GState, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_GState3", type=gfsm_IntOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gfsm_GTransition_Transition = Generalization(general=Transition, specific=gfsm_GTransition)
gen_gfsm_GState_State = Generalization(general=State, specific=gfsm_GState)
gen_gfsm_GFinalState_GState = Generalization(general=GState, specific=gfsm_GFinalState)
gen_gfsm_GFinalState_FinalState = Generalization(general=FinalState, specific=gfsm_GFinalState)
gen_gfsm_GInitialState_GState = Generalization(general=GState, specific=gfsm_GInitialState)
gen_gfsm_GInitialState_InitialState = Generalization(general=InitialState, specific=gfsm_GInitialState)
gen_gfsm_GFSM_FSM = Generalization(general=FSM, specific=gfsm_GFSM)

# Domain Model
domain_model = DomainModel(
    name="gfsm",
    types={gfsm_GTransition, Transition, gfsm_BooleanExpression, gfsm_GState, State, gfsm_IntOperation, gfsm_GFinalState, GState, FinalState, gfsm_GInitialState, InitialState, gfsm_GFSM, FSM},
    associations={guard0, inExpression1, outExpression2},
    generalizations={gen_gfsm_GTransition_Transition, gen_gfsm_GState_State, gen_gfsm_GFinalState_GState, gen_gfsm_GFinalState_FinalState, gen_gfsm_GInitialState_GState, gen_gfsm_GInitialState_InitialState, gen_gfsm_GFSM_FSM},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)