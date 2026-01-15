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
myStateMachines_Statemachine = Class(name="myStateMachines::Statemachine")
myStateMachines_Transition = Class(name="myStateMachines::Transition")
myStateMachines_Event = Class(name="myStateMachines::Event")
myStateMachines_State = Class(name="myStateMachines::State")

# myStateMachines_Statemachine class attributes and methods

# myStateMachines_Transition class attributes and methods

# myStateMachines_Event class attributes and methods
myStateMachines_Event_name: Property = Property(name="name", type=StringType)
myStateMachines_Event.attributes={myStateMachines_Event_name}

# myStateMachines_State class attributes and methods
myStateMachines_State_name: Property = Property(name="name", type=StringType)
myStateMachines_State_actions: Property = Property(name="actions", type=StringType)
myStateMachines_State.attributes={myStateMachines_State_name, myStateMachines_State_actions}

# Relationships
refinement3: BinaryAssociation = BinaryAssociation(
    name="refinement3",
    ends={
        Property(name="myStateMachines_Statemachine5", type=myStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_State4", type=myStateMachines_Statemachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="myStateMachines_Transition", type=myStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_State7", type=myStateMachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="myStateMachines_Event10", type=myStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_Transition9", type=myStateMachines_Event, multiplicity=Multiplicity(0, 1))
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="myStateMachines_State13", type=myStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_Transition12", type=myStateMachines_State, multiplicity=Multiplicity(0, 1))
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="myStateMachines_Event", type=myStateMachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_Statemachine", type=myStateMachines_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="myStateMachines_State", type=myStateMachines_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myStateMachines_Statemachine2", type=myStateMachines_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myStateMachines",
    types={myStateMachines_Statemachine, myStateMachines_Transition, myStateMachines_Event, myStateMachines_State},
    associations={refinement3, transitions6, event8, state11, events0, states1},
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