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
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_Variables = Class(name="stateMachine::Variables")
stateMachine_Events = Class(name="stateMachine::Events")
stateMachine_States = Class(name="stateMachine::States")
stateMachine_Variable = Class(name="stateMachine::Variable")
stateMachine_Event = Class(name="stateMachine::Event")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Transition = Class(name="stateMachine::Transition")
stateMachine_Condition = Class(name="stateMachine::Condition")

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name}

# stateMachine_Variables class attributes and methods

# stateMachine_Events class attributes and methods

# stateMachine_States class attributes and methods

# stateMachine_Variable class attributes and methods
stateMachine_Variable_name: Property = Property(name="name", type=StringType)
stateMachine_Variable.attributes={stateMachine_Variable_name}

# stateMachine_Event class attributes and methods
stateMachine_Event_name: Property = Property(name="name", type=StringType)
stateMachine_Event.attributes={stateMachine_Event_name}

# stateMachine_State class attributes and methods
stateMachine_State_name: Property = Property(name="name", type=StringType)
stateMachine_State.attributes={stateMachine_State_name}

# stateMachine_Transition class attributes and methods

# stateMachine_Condition class attributes and methods
stateMachine_Condition_op: Property = Property(name="op", type=StringType)
stateMachine_Condition_value: Property = Property(name="value", type=IntegerType)
stateMachine_Condition.attributes={stateMachine_Condition_op, stateMachine_Condition_value}

# Relationships
vardefs0: BinaryAssociation = BinaryAssociation(
    name="vardefs0",
    ends={
        Property(name="stateMachine_Variables", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_Variables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventdefs1: BinaryAssociation = BinaryAssociation(
    name="eventdefs1",
    ends={
        Property(name="stateMachine_Events", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Events, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statedefs3: BinaryAssociation = BinaryAssociation(
    name="statedefs3",
    ends={
        Property(name="stateMachine_States", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_States, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vars5: BinaryAssociation = BinaryAssociation(
    name="vars5",
    ends={
        Property(name="stateMachine_Variable", type=stateMachine_Variables, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Variables6", type=stateMachine_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events7: BinaryAssociation = BinaryAssociation(
    name="events7",
    ends={
        Property(name="stateMachine_Event", type=stateMachine_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Events8", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start9: BinaryAssociation = BinaryAssociation(
    name="start9",
    ends={
        Property(name="stateMachine_State", type=stateMachine_States, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_States10", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states11: BinaryAssociation = BinaryAssociation(
    name="states11",
    ends={
        Property(name="stateMachine_State13", type=stateMachine_States, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_States12", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions14: BinaryAssociation = BinaryAssociation(
    name="transitions14",
    ends={
        Property(name="stateMachine_Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State15", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event16: BinaryAssociation = BinaryAssociation(
    name="event16",
    ends={
        Property(name="stateMachine_Event18", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition17", type=stateMachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="stateMachine_Condition", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition20", type=stateMachine_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="stateMachine_State23", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition22", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
variable24: BinaryAssociation = BinaryAssociation(
    name="variable24",
    ends={
        Property(name="stateMachine_Variable26", type=stateMachine_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Condition25", type=stateMachine_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_StateMachine, stateMachine_Variables, stateMachine_Events, stateMachine_States, stateMachine_Variable, stateMachine_Event, stateMachine_State, stateMachine_Transition, stateMachine_Condition},
    associations={vardefs0, eventdefs1, statedefs3, vars5, events7, start9, states11, transitions14, event16, condition19, target21, variable24},
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