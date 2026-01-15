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
StateMachine_StateMachine = Class(name="StateMachine::StateMachine")
StateMachine_StateVertex = Class(name="StateMachine::StateVertex", is_abstract=True)
StateMachine_Transition = Class(name="StateMachine::Transition")
StateMachine_Event = Class(name="StateMachine::Event")
StateMachine_InitialState = Class(name="StateMachine::InitialState")
StateVertex = Class(name="StateVertex")
StateMachine_SimpleState = Class(name="StateMachine::SimpleState")
StateMachine_FinalState = Class(name="StateMachine::FinalState")

# StateMachine_StateMachine class attributes and methods

# StateMachine_StateVertex class attributes and methods
StateMachine_StateVertex_name: Property = Property(name="name", type=StringType)
StateMachine_StateVertex.attributes={StateMachine_StateVertex_name}

# StateMachine_Transition class attributes and methods
StateMachine_Transition_name: Property = Property(name="name", type=StringType)
StateMachine_Transition.attributes={StateMachine_Transition_name}

# StateMachine_Event class attributes and methods

# StateMachine_InitialState class attributes and methods

# StateVertex class attributes and methods

# StateMachine_SimpleState class attributes and methods

# StateMachine_FinalState class attributes and methods

# Relationships
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Transition", type=StateMachine_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="StateMachine_StateVertex", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine", type=StateMachine_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="StateMachine_Transition", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine2", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=StateMachine_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
trigger6: BinaryAssociation = BinaryAssociation(
    name="trigger6",
    ends={
        Property(name="StateMachine_Event", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition7", type=StateMachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="StateVertex", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachine_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="StateVertex10", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachine_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_StateMachine_InitialState_StateVertex = Generalization(general=StateVertex, specific=StateMachine_InitialState)
gen_StateMachine_SimpleState_StateVertex = Generalization(general=StateVertex, specific=StateMachine_SimpleState)
gen_StateMachine_FinalState_StateVertex = Generalization(general=StateVertex, specific=StateMachine_FinalState)

# Domain Model
domain_model = DomainModel(
    name="StateMachine",
    types={StateMachine_StateMachine, StateMachine_StateVertex, StateMachine_Transition, StateMachine_Event, StateMachine_InitialState, StateVertex, StateMachine_SimpleState, StateMachine_FinalState},
    associations={outgoing3, states0, transitions1, incoming4, trigger6, source8, target9},
    generalizations={gen_StateMachine_InitialState_StateVertex, gen_StateMachine_SimpleState_StateVertex, gen_StateMachine_FinalState_StateVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)