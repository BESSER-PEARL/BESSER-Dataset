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
stm_Statemachine = Class(name="stm::Statemachine")
stm_Event = Class(name="stm::Event")
stm_SelfEvent = Class(name="stm::SelfEvent")
stm_Command = Class(name="stm::Command")
stm_Guard = Class(name="stm::Guard")
stm_State = Class(name="stm::State")
stm_Transition = Class(name="stm::Transition")
stm_GuardCall = Class(name="stm::GuardCall")
stm_Parameter = Class(name="stm::Parameter")

# stm_Statemachine class attributes and methods

# stm_Event class attributes and methods
stm_Event_name: Property = Property(name="name", type=StringType)
stm_Event.attributes={stm_Event_name}

# stm_SelfEvent class attributes and methods

# stm_Command class attributes and methods
stm_Command_name: Property = Property(name="name", type=StringType)
stm_Command.attributes={stm_Command_name}

# stm_Guard class attributes and methods
stm_Guard_name: Property = Property(name="name", type=StringType)
stm_Guard.attributes={stm_Guard_name}

# stm_State class attributes and methods
stm_State_name: Property = Property(name="name", type=StringType)
stm_State.attributes={stm_State_name}

# stm_Transition class attributes and methods

# stm_GuardCall class attributes and methods
stm_GuardCall_parameters: Property = Property(name="parameters", type=StringType)
stm_GuardCall.attributes={stm_GuardCall_parameters}

# stm_Parameter class attributes and methods
stm_Parameter_name: Property = Property(name="name", type=StringType)
stm_Parameter_type: Property = Property(name="type", type=StringType)
stm_Parameter.attributes={stm_Parameter_type, stm_Parameter_name}

# Relationships
doAction10: BinaryAssociation = BinaryAssociation(
    name="doAction10",
    ends={
        Property(name="stm_State11", type=stm_Command, multiplicity=Multiplicity(0, 1)),
        Property(name="stm_Command12", type=stm_State, multiplicity=Multiplicity(1, 1))
    }
)
stopAction13: BinaryAssociation = BinaryAssociation(
    name="stopAction13",
    ends={
        Property(name="stm_Command15", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State14", type=stm_Command, multiplicity=Multiplicity(0, 1))
    }
)
states17: BinaryAssociation = BinaryAssociation(
    name="states17",
    ends={
        Property(name="stm_State18", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State16", type=stm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="stm_Event", type=stm_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Statemachine", type=stm_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="stm_Command", type=stm_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Statemachine2", type=stm_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guards3: BinaryAssociation = BinaryAssociation(
    name="guards3",
    ends={
        Property(name="stm_Guard", type=stm_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Statemachine4", type=stm_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="stm_State", type=stm_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Statemachine6", type=stm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryActions7: BinaryAssociation = BinaryAssociation(
    name="entryActions7",
    ends={
        Property(name="stm_Command9", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State8", type=stm_Command, multiplicity=Multiplicity(0, 9999))
    }
)
event37: BinaryAssociation = BinaryAssociation(
    name="event37",
    ends={
        Property(name="stm_Event39", type=stm_SelfEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_SelfEvent38", type=stm_Event, multiplicity=Multiplicity(0, 1))
    }
)
guard40: BinaryAssociation = BinaryAssociation(
    name="guard40",
    ends={
        Property(name="stm_GuardCall42", type=stm_SelfEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_SelfEvent41", type=stm_GuardCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action43: BinaryAssociation = BinaryAssociation(
    name="action43",
    ends={
        Property(name="stm_Command45", type=stm_SelfEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_SelfEvent44", type=stm_Command, multiplicity=Multiplicity(0, 1))
    }
)
selfEvents19: BinaryAssociation = BinaryAssociation(
    name="selfEvents19",
    ends={
        Property(name="stm_SelfEvent", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State20", type=stm_SelfEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions21: BinaryAssociation = BinaryAssociation(
    name="transitions21",
    ends={
        Property(name="stm_Transition", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State22", type=stm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitActions23: BinaryAssociation = BinaryAssociation(
    name="exitActions23",
    ends={
        Property(name="stm_Command25", type=stm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_State24", type=stm_Command, multiplicity=Multiplicity(0, 9999))
    }
)
event26: BinaryAssociation = BinaryAssociation(
    name="event26",
    ends={
        Property(name="stm_Event28", type=stm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Transition27", type=stm_Event, multiplicity=Multiplicity(0, 1))
    }
)
guard29: BinaryAssociation = BinaryAssociation(
    name="guard29",
    ends={
        Property(name="stm_GuardCall", type=stm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Transition30", type=stm_GuardCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state31: BinaryAssociation = BinaryAssociation(
    name="state31",
    ends={
        Property(name="stm_State33", type=stm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Transition32", type=stm_State, multiplicity=Multiplicity(0, 1))
    }
)
action34: BinaryAssociation = BinaryAssociation(
    name="action34",
    ends={
        Property(name="stm_Command36", type=stm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Transition35", type=stm_Command, multiplicity=Multiplicity(0, 1))
    }
)
guard46: BinaryAssociation = BinaryAssociation(
    name="guard46",
    ends={
        Property(name="stm_Guard48", type=stm_GuardCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_GuardCall47", type=stm_Guard, multiplicity=Multiplicity(0, 1))
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="stm_Parameter", type=stm_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="stm_Guard50", type=stm_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="stm",
    types={stm_Statemachine, stm_Event, stm_SelfEvent, stm_Command, stm_Guard, stm_State, stm_Transition, stm_GuardCall, stm_Parameter},
    associations={doAction10, stopAction13, states17, events0, commands1, guards3, states5, entryActions7, event37, guard40, action43, selfEvents19, transitions21, exitActions23, event26, guard29, state31, action34, guard46, parameters49},
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