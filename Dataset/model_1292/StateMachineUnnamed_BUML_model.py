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
StateMachineUnnamed_StateVertex = Class(name="StateMachineUnnamed::StateVertex", is_abstract=True)
StateMachineUnnamed_Transition = Class(name="StateMachineUnnamed::Transition")
StateMachineUnnamed_StateMachine = Class(name="StateMachineUnnamed::StateMachine")
StateMachineUnnamed_Event = Class(name="StateMachineUnnamed::Event")
StateMachineUnnamed_InitialState = Class(name="StateMachineUnnamed::InitialState")
StateVertex = Class(name="StateVertex")
StateMachineUnnamed_SimpleState = Class(name="StateMachineUnnamed::SimpleState")
StateMachineUnnamed_FinalState = Class(name="StateMachineUnnamed::FinalState")

# StateMachineUnnamed_StateVertex class attributes and methods
StateMachineUnnamed_StateVertex_name: Property = Property(name="name", type=StringType)
StateMachineUnnamed_StateVertex.attributes={StateMachineUnnamed_StateVertex_name}

# StateMachineUnnamed_Transition class attributes and methods
StateMachineUnnamed_Transition_name: Property = Property(name="name", type=StringType)
StateMachineUnnamed_Transition.attributes={StateMachineUnnamed_Transition_name}

# StateMachineUnnamed_StateMachine class attributes and methods

# StateMachineUnnamed_Event class attributes and methods

# StateMachineUnnamed_InitialState class attributes and methods

# StateVertex class attributes and methods

# StateMachineUnnamed_SimpleState class attributes and methods

# StateMachineUnnamed_FinalState class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="StateMachineUnnamed_StateVertex", type=StateMachineUnnamed_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineUnnamed_StateMachine", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="StateMachineUnnamed_Transition", type=StateMachineUnnamed_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineUnnamed_StateMachine2", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Transition", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
targets7: BinaryAssociation = BinaryAssociation(
    name="targets7",
    ends={
        Property(name="StateMachineUnnamed_StateVertex8", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineUnnamed_StateVertex6", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(0, 9999))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="StateVertex", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="StateVertex11", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachineUnnamed_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger12: BinaryAssociation = BinaryAssociation(
    name="trigger12",
    ends={
        Property(name="StateMachineUnnamed_Event", type=StateMachineUnnamed_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineUnnamed_Transition13", type=StateMachineUnnamed_Event, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_StateMachineUnnamed_InitialState_StateVertex = Generalization(general=StateVertex, specific=StateMachineUnnamed_InitialState)
gen_StateMachineUnnamed_SimpleState_StateVertex = Generalization(general=StateVertex, specific=StateMachineUnnamed_SimpleState)
gen_StateMachineUnnamed_FinalState_StateVertex = Generalization(general=StateVertex, specific=StateMachineUnnamed_FinalState)

# Domain Model
domain_model = DomainModel(
    name="StateMachineUnnamed",
    types={StateMachineUnnamed_StateVertex, StateMachineUnnamed_Transition, StateMachineUnnamed_StateMachine, StateMachineUnnamed_Event, StateMachineUnnamed_InitialState, StateVertex, StateMachineUnnamed_SimpleState, StateMachineUnnamed_FinalState},
    associations={states0, transitions1, outgoing3, incoming4, targets7, source9, target10, trigger12},
    generalizations={gen_StateMachineUnnamed_InitialState_StateVertex, gen_StateMachineUnnamed_SimpleState_StateVertex, gen_StateMachineUnnamed_FinalState_StateVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)