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
tP1_EM_StateMachine = Class(name="tP1::EM::StateMachine")
tP1_EM_Transition = Class(name="tP1::EM::Transition")
tP1_EM_State = Class(name="tP1::EM::State")

# tP1_EM_StateMachine class attributes and methods
tP1_EM_StateMachine_name: Property = Property(name="name", type=StringType)
tP1_EM_StateMachine.attributes={tP1_EM_StateMachine_name}

# tP1_EM_Transition class attributes and methods
tP1_EM_Transition_name: Property = Property(name="name", type=StringType)
tP1_EM_Transition.attributes={tP1_EM_Transition_name}

# tP1_EM_State class attributes and methods
tP1_EM_State_name: Property = Property(name="name", type=StringType)
tP1_EM_State.attributes={tP1_EM_State_name}

# Relationships
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="tP1_EM_State", type=tP1_EM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_EM_StateMachine2", type=tP1_EM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="tP1_EM_State5", type=tP1_EM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_EM_StateMachine4", type=tP1_EM_State, multiplicity=Multiplicity(0, 1))
    }
)
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="tP1_EM_Transition", type=tP1_EM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_EM_StateMachine", type=tP1_EM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="from", type=tP1_EM_Transition, multiplicity=Multiplicity(0, 1)),
        Property(name="Transition8", type=tP1_EM_State, multiplicity=Multiplicity(1, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State", type=tP1_EM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=tP1_EM_State, multiplicity=Multiplicity(0, 1))
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="State11", type=tP1_EM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=tP1_EM_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition", type=tP1_EM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=tP1_EM_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tP1_EM",
    types={tP1_EM_StateMachine, tP1_EM_Transition, tP1_EM_State},
    associations={state1, initialState3, transition0, outgoing7, to9, from10, incoming6},
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