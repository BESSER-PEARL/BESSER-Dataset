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
model_FSM = Class(name="model::FSM")
model_State = Class(name="model::State")
model_Transition = Class(name="model::Transition")

# model_FSM class attributes and methods
model_FSM_name: Property = Property(name="name", type=StringType)
model_FSM.attributes={model_FSM_name}

# model_State class attributes and methods
model_State_name: Property = Property(name="name", type=StringType)
model_State.attributes={model_State_name}

# model_Transition class attributes and methods
model_Transition_name: Property = Property(name="name", type=StringType)
model_Transition_trigger: Property = Property(name="trigger", type=StringType)
model_Transition_action: Property = Property(name="action", type=StringType)
model_Transition.attributes={model_Transition_trigger, model_Transition_action, model_Transition_name}

# Relationships
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="tgt", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm8: BinaryAssociation = BinaryAssociation(
    name="fsm8",
    ends={
        Property(name="FSM", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStates", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)
ownedStates0: BinaryAssociation = BinaryAssociation(
    name="ownedStates0",
    ends={
        Property(name="State", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=model_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions1: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions1",
    ends={
        Property(name="Transition", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm2", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="model_State", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FSM", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
tgt9: BinaryAssociation = BinaryAssociation(
    name="tgt9",
    ends={
        Property(name="State10", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
src11: BinaryAssociation = BinaryAssociation(
    name="src11",
    ends={
        Property(name="State12", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
fsm13: BinaryAssociation = BinaryAssociation(
    name="fsm13",
    ends={
        Property(name="FSM14", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransitions", type=model_FSM, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_FSM, model_State, model_Transition},
    associations={incoming4, outgoing6, fsm8, ownedStates0, ownedTransitions1, initialState3, tgt9, src11, fsm13},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)