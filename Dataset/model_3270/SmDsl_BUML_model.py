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
smDsl_Model = Class(name="smDsl::Model")
smDsl_EventsSection = Class(name="smDsl::EventsSection")
smDsl_CommandsSection = Class(name="smDsl::CommandsSection")
smDsl_State = Class(name="smDsl::State")
smDsl_EventHandlingDescription = Class(name="smDsl::EventHandlingDescription")
smDsl_Event = Class(name="smDsl::Event")
smDsl_Command = Class(name="smDsl::Command")

# smDsl_Model class attributes and methods
smDsl_Model_name: Property = Property(name="name", type=StringType)
smDsl_Model.attributes={smDsl_Model_name}

# smDsl_EventsSection class attributes and methods

# smDsl_CommandsSection class attributes and methods

# smDsl_State class attributes and methods
smDsl_State_initial: Property = Property(name="initial", type=BooleanType)
smDsl_State_name: Property = Property(name="name", type=StringType)
smDsl_State.attributes={smDsl_State_initial, smDsl_State_name}

# smDsl_EventHandlingDescription class attributes and methods

# smDsl_Event class attributes and methods
smDsl_Event_name: Property = Property(name="name", type=StringType)
smDsl_Event.attributes={smDsl_Event_name}

# smDsl_Command class attributes and methods
smDsl_Command_name: Property = Property(name="name", type=StringType)
smDsl_Command.attributes={smDsl_Command_name}

# Relationships
eventsSection0: BinaryAssociation = BinaryAssociation(
    name="eventsSection0",
    ends={
        Property(name="smDsl_EventsSection", type=smDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_Model", type=smDsl_EventsSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandsSection1: BinaryAssociation = BinaryAssociation(
    name="commandsSection1",
    ends={
        Property(name="smDsl_CommandsSection", type=smDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_Model2", type=smDsl_CommandsSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="smDsl_State", type=smDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_Model4", type=smDsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryCommands9: BinaryAssociation = BinaryAssociation(
    name="entryCommands9",
    ends={
        Property(name="smDsl_Command11", type=smDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_State10", type=smDsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
eventHandlingDescriptions12: BinaryAssociation = BinaryAssociation(
    name="eventHandlingDescriptions12",
    ends={
        Property(name="smDsl_EventHandlingDescription", type=smDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_State13", type=smDsl_EventHandlingDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitCommands14: BinaryAssociation = BinaryAssociation(
    name="exitCommands14",
    ends={
        Property(name="smDsl_Command16", type=smDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_State15", type=smDsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
event17: BinaryAssociation = BinaryAssociation(
    name="event17",
    ends={
        Property(name="smDsl_Event19", type=smDsl_EventHandlingDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_EventHandlingDescription18", type=smDsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
commands20: BinaryAssociation = BinaryAssociation(
    name="commands20",
    ends={
        Property(name="smDsl_Command22", type=smDsl_EventHandlingDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_EventHandlingDescription21", type=smDsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
targetState23: BinaryAssociation = BinaryAssociation(
    name="targetState23",
    ends={
        Property(name="smDsl_State25", type=smDsl_EventHandlingDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_EventHandlingDescription24", type=smDsl_State, multiplicity=Multiplicity(0, 1))
    }
)
events5: BinaryAssociation = BinaryAssociation(
    name="events5",
    ends={
        Property(name="smDsl_Event", type=smDsl_EventsSection, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_EventsSection6", type=smDsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands7: BinaryAssociation = BinaryAssociation(
    name="commands7",
    ends={
        Property(name="smDsl_Command", type=smDsl_CommandsSection, multiplicity=Multiplicity(1, 1)),
        Property(name="smDsl_CommandsSection8", type=smDsl_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="smDsl",
    types={smDsl_Model, smDsl_EventsSection, smDsl_CommandsSection, smDsl_State, smDsl_EventHandlingDescription, smDsl_Event, smDsl_Command},
    associations={eventsSection0, commandsSection1, states3, entryCommands9, eventHandlingDescriptions12, exitCommands14, event17, commands20, targetState23, events5, commands7},
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