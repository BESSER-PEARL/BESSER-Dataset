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
StateKind: Enumeration = Enumeration(
    name="StateKind",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="FINAL"),
			EnumerationLiteral(name="INITIAL")
    }
)

# Classes
stateMachine_IDElement = Class(name="stateMachine::IDElement")
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
IDElement = Class(name="IDElement")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Transition = Class(name="stateMachine::Transition")
stateMachine_Event = Class(name="stateMachine::Event")

# stateMachine_IDElement class attributes and methods
stateMachine_IDElement_id: Property = Property(name="id", type=StringType)
stateMachine_IDElement.attributes={stateMachine_IDElement_id}

# stateMachine_StateMachine class attributes and methods

# IDElement class attributes and methods

# stateMachine_State class attributes and methods
stateMachine_State_kind: Property = Property(name="kind", type=StringType)
stateMachine_State.attributes={stateMachine_State_kind}

# stateMachine_Transition class attributes and methods

# stateMachine_Event class attributes and methods

# Relationships
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="State", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=stateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="State10", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=stateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="stateMachine_Event13", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition12", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999))
    }
)
effect14: BinaryAssociation = BinaryAssociation(
    name="effect14",
    ends={
        Property(name="stateMachine_Event16", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition15", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="stateMachine_Transition", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events3: BinaryAssociation = BinaryAssociation(
    name="events3",
    ends={
        Property(name="stateMachine_Event", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_stateMachine_Transition_IDElement = Generalization(general=IDElement, specific=stateMachine_Transition)
gen_stateMachine_Event_IDElement = Generalization(general=IDElement, specific=stateMachine_Event)
gen_stateMachine_StateMachine_IDElement = Generalization(general=IDElement, specific=stateMachine_StateMachine)
gen_stateMachine_State_IDElement = Generalization(general=IDElement, specific=stateMachine_State)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_IDElement, stateMachine_StateMachine, IDElement, stateMachine_State, stateMachine_Transition, stateMachine_Event, StateKind},
    associations={source8, target9, trigger11, effect14, states0, transitions1, events3, outgoing5, incoming6},
    generalizations={gen_stateMachine_Transition_IDElement, gen_stateMachine_Event_IDElement, gen_stateMachine_StateMachine_IDElement, gen_stateMachine_State_IDElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)