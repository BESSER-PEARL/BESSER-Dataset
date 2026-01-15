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
stateMachine_Model = Class(name="stateMachine::Model")
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_Condition = Class(name="stateMachine::Condition")
stateMachine_Event = Class(name="stateMachine::Event")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Transition = Class(name="stateMachine::Transition")

# stateMachine_Model class attributes and methods

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name}

# stateMachine_Condition class attributes and methods

# stateMachine_Event class attributes and methods
stateMachine_Event_name: Property = Property(name="name", type=StringType)
stateMachine_Event.attributes={stateMachine_Event_name}

# stateMachine_State class attributes and methods
stateMachine_State_name: Property = Property(name="name", type=StringType)
stateMachine_State.attributes={stateMachine_State_name}

# stateMachine_Transition class attributes and methods

# Relationships
event7: BinaryAssociation = BinaryAssociation(
    name="event7",
    ends={
        Property(name="stateMachine_Transition8", type=stateMachine_Event, multiplicity=Multiplicity(0, 1)),
        Property(name="stateMachine_Event9", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="stateMachine_State12", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition11", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
events13: BinaryAssociation = BinaryAssociation(
    name="events13",
    ends={
        Property(name="stateMachine_Event14", type=stateMachine_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Condition", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachines0: BinaryAssociation = BinaryAssociation(
    name="statemachines0",
    ends={
        Property(name="stateMachine_StateMachine", type=stateMachine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Model", type=stateMachine_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="stateMachine_Event", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="stateMachine_Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State6", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_Model, stateMachine_StateMachine, stateMachine_Condition, stateMachine_Event, stateMachine_State, stateMachine_Transition},
    associations={event7, target10, events13, statemachines0, events1, states3, transitions5},
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