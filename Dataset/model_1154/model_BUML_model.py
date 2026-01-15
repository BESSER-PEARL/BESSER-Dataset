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
model_Transition.attributes={model_Transition_name}

# Relationships
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="State", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
from7: BinaryAssociation = BinaryAssociation(
    name="from7",
    ends={
        Property(name="State8", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=model_State, multiplicity=Multiplicity(0, 1))
    }
)
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="model_State", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FSM", type=model_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="model_Transition", type=model_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FSM2", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=model_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=model_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_FSM, model_State, model_Transition},
    associations={to6, from7, state0, transition1, incoming3, outgoing4},
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