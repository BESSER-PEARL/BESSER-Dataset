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

# Enumerations
StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="INITIAL"),
			EnumerationLiteral(name="FINAL")
    }
)

# Classes
emf_State = Class(name="emf::State")
emf_StateMachine = Class(name="emf::StateMachine")
emf_Action = Class(name="emf::Action")
emf_TransitionToStateMapEntry = Class(name="emf::TransitionToStateMapEntry")
emf_Transition = Class(name="emf::Transition")

# emf_State class attributes and methods
emf_State_type: Property = Property(name="type", type=StringType)
emf_State_name: Property = Property(name="name", type=StringType)
emf_State.attributes={emf_State_name, emf_State_type}

# emf_StateMachine class attributes and methods

# emf_Action class attributes and methods
emf_Action_event: Property = Property(name="event", type=StringType)
emf_Action.attributes={emf_Action_event}

# emf_TransitionToStateMapEntry class attributes and methods

# emf_Transition class attributes and methods
emf_Transition_action: Property = Property(name="action", type=StringType)
emf_Transition.attributes={emf_Transition_action}

# Relationships
nestedStateMachines0: BinaryAssociation = BinaryAssociation(
    name="nestedStateMachines0",
    ends={
        Property(name="emf_StateMachine", type=emf_State, multiplicity=Multiplicity(1, 1)),
        Property(name="emf_State", type=emf_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
targetState6: BinaryAssociation = BinaryAssociation(
    name="targetState6",
    ends={
        Property(name="emf_Transition", type=emf_State, multiplicity=Multiplicity(0, 1)),
        Property(name="emf_State7", type=emf_Transition, multiplicity=Multiplicity(1, 1))
    }
)
key8: BinaryAssociation = BinaryAssociation(
    name="key8",
    ends={
        Property(name="emf_Transition10", type=emf_TransitionToStateMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emf_TransitionToStateMapEntry9", type=emf_Transition, multiplicity=Multiplicity(0, 1))
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="emf_State13", type=emf_TransitionToStateMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emf_TransitionToStateMapEntry12", type=emf_State, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="emf_State3", type=emf_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="emf_StateMachine2", type=emf_State, multiplicity=Multiplicity(0, 9999))
    }
)
transitionToSourceState4: BinaryAssociation = BinaryAssociation(
    name="transitionToSourceState4",
    ends={
        Property(name="emf_TransitionToStateMapEntry", type=emf_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="emf_StateMachine5", type=emf_TransitionToStateMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="emf",
    types={emf_State, emf_StateMachine, emf_Action, emf_TransitionToStateMapEntry, emf_Transition, StateType},
    associations={nestedStateMachines0, targetState6, key8, value11, states1, transitionToSourceState4},
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