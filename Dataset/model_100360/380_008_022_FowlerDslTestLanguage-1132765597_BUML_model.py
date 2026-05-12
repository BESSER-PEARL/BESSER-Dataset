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
fowlerdsl_Statemachine = Class(name="fowlerdsl_Statemachine")
fowlerdsl_Event = Class(name="fowlerdsl_Event")
fowlerdsl_Command = Class(name="fowlerdsl_Command")
fowlerdsl_State = Class(name="fowlerdsl_State")
fowlerdsl_Transition = Class(name="fowlerdsl_Transition")

# fowlerdsl_Statemachine class attributes and methods

# fowlerdsl_Event class attributes and methods
fowlerdsl_Event_resetting: Property = Property(name="resetting", type=BooleanType)
fowlerdsl_Event_name: Property = Property(name="name", type=StringType)
fowlerdsl_Event_code: Property = Property(name="code", type=StringType)
fowlerdsl_Event.attributes={fowlerdsl_Event_code, fowlerdsl_Event_resetting, fowlerdsl_Event_name}

# fowlerdsl_Command class attributes and methods
fowlerdsl_Command_name: Property = Property(name="name", type=StringType)
fowlerdsl_Command_code: Property = Property(name="code", type=StringType)
fowlerdsl_Command.attributes={fowlerdsl_Command_code, fowlerdsl_Command_name}

# fowlerdsl_State class attributes and methods
fowlerdsl_State_name: Property = Property(name="name", type=StringType)
fowlerdsl_State.attributes={fowlerdsl_State_name}

# fowlerdsl_Transition class attributes and methods

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="fowlerdsl_Event", type=fowlerdsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_Statemachine", type=fowlerdsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="fowlerdsl_Command", type=fowlerdsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_Statemachine2", type=fowlerdsl_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="fowlerdsl_State", type=fowlerdsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_Statemachine4", type=fowlerdsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions5: BinaryAssociation = BinaryAssociation(
    name="actions5",
    ends={
        Property(name="fowlerdsl_Command7", type=fowlerdsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_State6", type=fowlerdsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="fowlerdsl_Transition", type=fowlerdsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_State9", type=fowlerdsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event10: BinaryAssociation = BinaryAssociation(
    name="event10",
    ends={
        Property(name="fowlerdsl_Event12", type=fowlerdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_Transition11", type=fowlerdsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
state13: BinaryAssociation = BinaryAssociation(
    name="state13",
    ends={
        Property(name="fowlerdsl_State15", type=fowlerdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fowlerdsl_Transition14", type=fowlerdsl_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fowlerdsl",
    types={fowlerdsl_Statemachine, fowlerdsl_Event, fowlerdsl_Command, fowlerdsl_State, fowlerdsl_Transition},
    associations={events0, commands1, states3, actions5, transitions8, event10, state13},
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