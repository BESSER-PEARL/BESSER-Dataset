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
martinfowlerdsl_StateMachine = Class(name="martinfowlerdsl::StateMachine")
martinfowlerdsl_State = Class(name="martinfowlerdsl::State")
martinfowlerdsl_Event = Class(name="martinfowlerdsl::Event")
martinfowlerdsl_AbstractEvent = Class(name="martinfowlerdsl::AbstractEvent", is_abstract=True)
martinfowlerdsl_Command = Class(name="martinfowlerdsl::Command")
martinfowlerdsl_Transition = Class(name="martinfowlerdsl::Transition")
AbstractEvent = Class(name="AbstractEvent")

# martinfowlerdsl_StateMachine class attributes and methods

# martinfowlerdsl_State class attributes and methods
martinfowlerdsl_State_name: Property = Property(name="name", type=StringType)
martinfowlerdsl_State.attributes={martinfowlerdsl_State_name}

# martinfowlerdsl_Event class attributes and methods
martinfowlerdsl_Event_resetting: Property = Property(name="resetting", type=BooleanType)
martinfowlerdsl_Event.attributes={martinfowlerdsl_Event_resetting}

# martinfowlerdsl_AbstractEvent class attributes and methods
martinfowlerdsl_AbstractEvent_name: Property = Property(name="name", type=StringType)
martinfowlerdsl_AbstractEvent_code: Property = Property(name="code", type=StringType)
martinfowlerdsl_AbstractEvent.attributes={martinfowlerdsl_AbstractEvent_code, martinfowlerdsl_AbstractEvent_name}

# martinfowlerdsl_Command class attributes and methods

# martinfowlerdsl_Transition class attributes and methods

# AbstractEvent class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="martinfowlerdsl_State", type=martinfowlerdsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_StateMachine", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
start1: BinaryAssociation = BinaryAssociation(
    name="start1",
    ends={
        Property(name="martinfowlerdsl_State3", type=martinfowlerdsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_StateMachine2", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 1))
    }
)
events4: BinaryAssociation = BinaryAssociation(
    name="events4",
    ends={
        Property(name="martinfowlerdsl_AbstractEvent", type=martinfowlerdsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_StateMachine5", type=martinfowlerdsl_AbstractEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="martinfowlerdsl_Command", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_State7", type=martinfowlerdsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="Transition", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=martinfowlerdsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="State", type=martinfowlerdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="martinfowlerdsl_State11", type=martinfowlerdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_Transition", type=martinfowlerdsl_State, multiplicity=Multiplicity(1, 1))
    }
)
trigger12: BinaryAssociation = BinaryAssociation(
    name="trigger12",
    ends={
        Property(name="martinfowlerdsl_Event", type=martinfowlerdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="martinfowlerdsl_Transition13", type=martinfowlerdsl_Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_martinfowlerdsl_Command_AbstractEvent = Generalization(general=AbstractEvent, specific=martinfowlerdsl_Command)
gen_martinfowlerdsl_Event_AbstractEvent = Generalization(general=AbstractEvent, specific=martinfowlerdsl_Event)

# Domain Model
domain_model = DomainModel(
    name="martinfowlerdsl",
    types={martinfowlerdsl_StateMachine, martinfowlerdsl_State, martinfowlerdsl_Event, martinfowlerdsl_AbstractEvent, martinfowlerdsl_Command, martinfowlerdsl_Transition, AbstractEvent},
    associations={states0, start1, events4, actions6, transitions8, source9, target10, trigger12},
    generalizations={gen_martinfowlerdsl_Command_AbstractEvent, gen_martinfowlerdsl_Event_AbstractEvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)