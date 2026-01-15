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
StateMachineHyperedges_StateMachine = Class(name="StateMachineHyperedges::StateMachine")
StateMachineHyperedges_StateVertex = Class(name="StateMachineHyperedges::StateVertex", is_abstract=True)
StateMachineHyperedges_Transition = Class(name="StateMachineHyperedges::Transition")
StateMachineHyperedges_Event = Class(name="StateMachineHyperedges::Event")
StateMachineHyperedges_SimpleState = Class(name="StateMachineHyperedges::SimpleState")
StateMachineHyperedges_FinalState = Class(name="StateMachineHyperedges::FinalState")
StateMachineHyperedges_InitialState = Class(name="StateMachineHyperedges::InitialState")
StateVertex = Class(name="StateVertex")

# StateMachineHyperedges_StateMachine class attributes and methods

# StateMachineHyperedges_StateVertex class attributes and methods
StateMachineHyperedges_StateVertex_name: Property = Property(name="name", type=StringType)
StateMachineHyperedges_StateVertex.attributes={StateMachineHyperedges_StateVertex_name}

# StateMachineHyperedges_Transition class attributes and methods
StateMachineHyperedges_Transition_name: Property = Property(name="name", type=StringType)
StateMachineHyperedges_Transition.attributes={StateMachineHyperedges_Transition_name}

# StateMachineHyperedges_Event class attributes and methods

# StateMachineHyperedges_SimpleState class attributes and methods

# StateMachineHyperedges_FinalState class attributes and methods

# StateMachineHyperedges_InitialState class attributes and methods

# StateVertex class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="StateMachineHyperedges_StateVertex", type=StateMachineHyperedges_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineHyperedges_StateMachine", type=StateMachineHyperedges_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="StateMachineHyperedges_Transition", type=StateMachineHyperedges_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineHyperedges_StateMachine2", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Transition", type=StateMachineHyperedges_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=StateMachineHyperedges_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
trigger6: BinaryAssociation = BinaryAssociation(
    name="trigger6",
    ends={
        Property(name="StateMachineHyperedges_Event", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineHyperedges_Transition7", type=StateMachineHyperedges_Event, multiplicity=Multiplicity(0, 1))
    }
)
sources8: BinaryAssociation = BinaryAssociation(
    name="sources8",
    ends={
        Property(name="StateVertex", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachineHyperedges_StateVertex, multiplicity=Multiplicity(0, 9999))
    }
)
targets9: BinaryAssociation = BinaryAssociation(
    name="targets9",
    ends={
        Property(name="StateVertex10", type=StateMachineHyperedges_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachineHyperedges_StateVertex, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_StateMachineHyperedges_SimpleState_StateVertex = Generalization(general=StateVertex, specific=StateMachineHyperedges_SimpleState)
gen_StateMachineHyperedges_FinalState_StateVertex = Generalization(general=StateVertex, specific=StateMachineHyperedges_FinalState)
gen_StateMachineHyperedges_InitialState_StateVertex = Generalization(general=StateVertex, specific=StateMachineHyperedges_InitialState)

# Domain Model
domain_model = DomainModel(
    name="StateMachineHyperedges",
    types={StateMachineHyperedges_StateMachine, StateMachineHyperedges_StateVertex, StateMachineHyperedges_Transition, StateMachineHyperedges_Event, StateMachineHyperedges_SimpleState, StateMachineHyperedges_FinalState, StateMachineHyperedges_InitialState, StateVertex},
    associations={states0, transitions1, outgoing3, incoming4, trigger6, sources8, targets9},
    generalizations={gen_StateMachineHyperedges_SimpleState_StateVertex, gen_StateMachineHyperedges_FinalState_StateVertex, gen_StateMachineHyperedges_InitialState_StateVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)