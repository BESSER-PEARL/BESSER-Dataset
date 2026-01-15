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
dsl_State = Class(name="dsl::State")
dsl_Statemachine = Class(name="dsl::Statemachine")
dsl_Event = Class(name="dsl::Event")
dsl_Command = Class(name="dsl::Command")
dsl_Transition = Class(name="dsl::Transition")

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State.attributes={dsl_State_name}

# dsl_Statemachine class attributes and methods

# dsl_Event class attributes and methods
dsl_Event_name: Property = Property(name="name", type=StringType)
dsl_Event_code: Property = Property(name="code", type=StringType)
dsl_Event.attributes={dsl_Event_name, dsl_Event_code}

# dsl_Command class attributes and methods
dsl_Command_name: Property = Property(name="name", type=StringType)
dsl_Command_code: Property = Property(name="code", type=StringType)
dsl_Command.attributes={dsl_Command_name, dsl_Command_code}

# dsl_Transition class attributes and methods

# Relationships
resetEvents1: BinaryAssociation = BinaryAssociation(
    name="resetEvents1",
    ends={
        Property(name="dsl_Event3", type=dsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statemachine2", type=dsl_Event, multiplicity=Multiplicity(0, 9999))
    }
)
initialState4: BinaryAssociation = BinaryAssociation(
    name="initialState4",
    ends={
        Property(name="dsl_State", type=dsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statemachine5", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="dsl_Event", type=dsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statemachine", type=dsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event19: BinaryAssociation = BinaryAssociation(
    name="event19",
    ends={
        Property(name="dsl_Event21", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition20", type=dsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
state22: BinaryAssociation = BinaryAssociation(
    name="state22",
    ends={
        Property(name="dsl_State24", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition23", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)
commands6: BinaryAssociation = BinaryAssociation(
    name="commands6",
    ends={
        Property(name="dsl_Command", type=dsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statemachine7", type=dsl_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state8: BinaryAssociation = BinaryAssociation(
    name="state8",
    ends={
        Property(name="dsl_State10", type=dsl_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statemachine9", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions11: BinaryAssociation = BinaryAssociation(
    name="actions11",
    ends={
        Property(name="dsl_Command13", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State12", type=dsl_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions14: BinaryAssociation = BinaryAssociation(
    name="transitions14",
    ends={
        Property(name="dsl_Transition", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State15", type=dsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subState17: BinaryAssociation = BinaryAssociation(
    name="subState17",
    ends={
        Property(name="dsl_State18", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State16", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_State, dsl_Statemachine, dsl_Event, dsl_Command, dsl_Transition},
    associations={resetEvents1, initialState4, events0, event19, state22, commands6, state8, actions11, transitions14, subState17},
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