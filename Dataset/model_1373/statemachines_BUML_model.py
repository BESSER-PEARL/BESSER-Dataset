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
statemachines_StateMachine = Class(name="statemachines::StateMachine")
statemachines_State = Class(name="statemachines::State")
statemachines_Transition = Class(name="statemachines::Transition")
statemachines_Event = Class(name="statemachines::Event")

# statemachines_StateMachine class attributes and methods

# statemachines_State class attributes and methods
statemachines_State_name: Property = Property(name="name", type=StringType)
statemachines_State.attributes={statemachines_State_name}

# statemachines_Transition class attributes and methods

# statemachines_Event class attributes and methods
statemachines_Event_name: Property = Property(name="name", type=StringType)
statemachines_Event_code: Property = Property(name="code", type=StringType)
statemachines_Event.attributes={statemachines_Event_code, statemachines_Event_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachines_State", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StateMachine", type=statemachines_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resetEvents3: BinaryAssociation = BinaryAssociation(
    name="resetEvents3",
    ends={
        Property(name="statemachines_Event5", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StateMachine4", type=statemachines_Event, multiplicity=Multiplicity(0, 9999))
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="statemachines_Transition", type=statemachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_State7", type=statemachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state8: BinaryAssociation = BinaryAssociation(
    name="state8",
    ends={
        Property(name="statemachines_State10", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition9", type=statemachines_State, multiplicity=Multiplicity(0, 1))
    }
)
event11: BinaryAssociation = BinaryAssociation(
    name="event11",
    ends={
        Property(name="statemachines_Event13", type=statemachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_Transition12", type=statemachines_Event, multiplicity=Multiplicity(0, 1))
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="statemachines_Event", type=statemachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachines_StateMachine2", type=statemachines_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachines",
    types={statemachines_StateMachine, statemachines_State, statemachines_Transition, statemachines_Event},
    associations={states0, resetEvents3, transitions6, state8, event11, events1},
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