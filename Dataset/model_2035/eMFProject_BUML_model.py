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
eMFProject_Command = Class(name="eMFProject::Command")
eMFProject_State = Class(name="eMFProject::State")
eMFProject_Statemachine = Class(name="eMFProject::Statemachine")
eMFProject_Event = Class(name="eMFProject::Event")
eMFProject_Transition = Class(name="eMFProject::Transition")

# eMFProject_Command class attributes and methods
eMFProject_Command_name: Property = Property(name="name", type=StringType)
eMFProject_Command_code: Property = Property(name="code", type=StringType)
eMFProject_Command.attributes={eMFProject_Command_code, eMFProject_Command_name}

# eMFProject_State class attributes and methods
eMFProject_State_name: Property = Property(name="name", type=StringType)
eMFProject_State.attributes={eMFProject_State_name}

# eMFProject_Statemachine class attributes and methods

# eMFProject_Event class attributes and methods
eMFProject_Event_name: Property = Property(name="name", type=StringType)
eMFProject_Event_code: Property = Property(name="code", type=StringType)
eMFProject_Event.attributes={eMFProject_Event_name, eMFProject_Event_code}

# eMFProject_Transition class attributes and methods

# Relationships
resetEvents1: BinaryAssociation = BinaryAssociation(
    name="resetEvents1",
    ends={
        Property(name="eMFProject_Event3", type=eMFProject_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Statemachine2", type=eMFProject_Event, multiplicity=Multiplicity(0, 9999))
    }
)
commands4: BinaryAssociation = BinaryAssociation(
    name="commands4",
    ends={
        Property(name="eMFProject_Command", type=eMFProject_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Statemachine5", type=eMFProject_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="eMFProject_State", type=eMFProject_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Statemachine7", type=eMFProject_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="eMFProject_Event", type=eMFProject_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Statemachine", type=eMFProject_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event13: BinaryAssociation = BinaryAssociation(
    name="event13",
    ends={
        Property(name="eMFProject_Event15", type=eMFProject_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Transition14", type=eMFProject_Event, multiplicity=Multiplicity(0, 1))
    }
)
state16: BinaryAssociation = BinaryAssociation(
    name="state16",
    ends={
        Property(name="eMFProject_State18", type=eMFProject_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_Transition17", type=eMFProject_State, multiplicity=Multiplicity(0, 1))
    }
)
actions8: BinaryAssociation = BinaryAssociation(
    name="actions8",
    ends={
        Property(name="eMFProject_Command10", type=eMFProject_State, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_State9", type=eMFProject_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions11: BinaryAssociation = BinaryAssociation(
    name="transitions11",
    ends={
        Property(name="eMFProject_Transition", type=eMFProject_State, multiplicity=Multiplicity(1, 1)),
        Property(name="eMFProject_State12", type=eMFProject_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="eMFProject",
    types={eMFProject_Command, eMFProject_State, eMFProject_Statemachine, eMFProject_Event, eMFProject_Transition},
    associations={resetEvents1, commands4, states6, events0, event13, state16, actions8, transitions11},
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