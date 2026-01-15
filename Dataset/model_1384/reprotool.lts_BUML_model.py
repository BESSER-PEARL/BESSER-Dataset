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
lts2_TransitionalState = Class(name="lts2::TransitionalState")
lts2_FinalState = Class(name="lts2::FinalState")
lts2_AbortState = Class(name="lts2::AbortState")
TransitionalState = Class(name="TransitionalState")
lts2_StateMachine = Class(name="lts2::StateMachine")
lts2_InitialState = Class(name="lts2::InitialState")
lts2_State = Class(name="lts2::State", is_abstract=True)
lts2_Transition = Class(name="lts2::Transition")
State = Class(name="State")
UseCaseStep = Class(name="UseCaseStep")
lts2_LTSGenerator = Class(name="lts2::LTSGenerator", is_abstract=True)

# lts2_TransitionalState class attributes and methods

# lts2_FinalState class attributes and methods

# lts2_AbortState class attributes and methods

# TransitionalState class attributes and methods

# lts2_StateMachine class attributes and methods

# lts2_InitialState class attributes and methods

# lts2_State class attributes and methods

# lts2_Transition class attributes and methods

# State class attributes and methods

# UseCaseStep class attributes and methods

# lts2_LTSGenerator class attributes and methods
lts2_LTSGenerator_m_processUseCase: Method = Method(name="processUseCase", parameters={Parameter(name='useCase')})
lts2_LTSGenerator.methods={lts2_LTSGenerator_m_processUseCase}

# Relationships
transitionalStates1: BinaryAssociation = BinaryAssociation(
    name="transitionalStates1",
    ends={
        Property(name="lts2_TransitionalState", type=lts2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_StateMachine2", type=lts2_TransitionalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalState3: BinaryAssociation = BinaryAssociation(
    name="finalState3",
    ends={
        Property(name="lts2_FinalState", type=lts2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_StateMachine4", type=lts2_FinalState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abortState5: BinaryAssociation = BinaryAssociation(
    name="abortState5",
    ends={
        Property(name="lts2_AbortState", type=lts2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_StateMachine6", type=lts2_AbortState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="lts2_InitialState", type=lts2_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_StateMachine", type=lts2_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transitions7: BinaryAssociation = BinaryAssociation(
    name="transitions7",
    ends={
        Property(name="Transition", type=lts2_TransitionalState, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceState", type=lts2_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetState8: BinaryAssociation = BinaryAssociation(
    name="targetState8",
    ends={
        Property(name="lts2_Transition", type=lts2_State, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_State", type=lts2_Transition, multiplicity=Multiplicity(1, 1))
    }
)
relatedStep9: BinaryAssociation = BinaryAssociation(
    name="relatedStep9",
    ends={
        Property(name="UseCaseStep", type=lts2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_Transition10", type=UseCaseStep, multiplicity=Multiplicity(1, 1))
    }
)
sourceState11: BinaryAssociation = BinaryAssociation(
    name="sourceState11",
    ends={
        Property(name="TransitionalState", type=lts2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=lts2_TransitionalState, multiplicity=Multiplicity(1, 1))
    }
)
labelTransitionSystem12: BinaryAssociation = BinaryAssociation(
    name="labelTransitionSystem12",
    ends={
        Property(name="lts2_StateMachine13", type=lts2_LTSGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="lts2_LTSGenerator", type=lts2_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_lts2_InitialState_TransitionalState = Generalization(general=TransitionalState, specific=lts2_InitialState)
gen_lts2_TransitionalState_State = Generalization(general=State, specific=lts2_TransitionalState)
gen_lts2_FinalState_State = Generalization(general=State, specific=lts2_FinalState)
gen_lts2_AbortState_State = Generalization(general=State, specific=lts2_AbortState)

# Domain Model
domain_model = DomainModel(
    name="lts2",
    types={lts2_TransitionalState, lts2_FinalState, lts2_AbortState, TransitionalState, lts2_StateMachine, lts2_InitialState, lts2_State, lts2_Transition, State, UseCaseStep, lts2_LTSGenerator},
    associations={transitionalStates1, finalState3, abortState5, initialState0, transitions7, targetState8, relatedStep9, sourceState11, labelTransitionSystem12},
    generalizations={gen_lts2_InitialState_TransitionalState, gen_lts2_TransitionalState_State, gen_lts2_FinalState_State, gen_lts2_AbortState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)