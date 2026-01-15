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
statemachine_Statemachine = Class(name="statemachine::Statemachine")
statemachine_State = Class(name="statemachine::State")
statemachine_Event = Class(name="statemachine::Event")
statemachine_Transition = Class(name="statemachine::Transition")

# statemachine_Statemachine class attributes and methods
statemachine_Statemachine_name: Property = Property(name="name", type=StringType)
statemachine_Statemachine.attributes={statemachine_Statemachine_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Event class attributes and methods
statemachine_Event_name: Property = Property(name="name", type=StringType)
statemachine_Event.attributes={statemachine_Event_name}

# statemachine_Transition class attributes and methods

# Relationships
event11: BinaryAssociation = BinaryAssociation(
    name="event11",
    ends={
        Property(name="statemachine_Transition12", type=statemachine_Event, multiplicity=Multiplicity(0, 1)),
        Property(name="statemachine_Event13", type=statemachine_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="statemachine_State16", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition15", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="statemachine_Event", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine2", type=statemachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="statemachine_Transition", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine4", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialiState5: BinaryAssociation = BinaryAssociation(
    name="initialiState5",
    ends={
        Property(name="statemachine_State7", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine6", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="statemachine_State10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition9", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Statemachine, statemachine_State, statemachine_Event, statemachine_Transition},
    associations={event11, to14, states0, events1, transitions3, initialiState5, from8},
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