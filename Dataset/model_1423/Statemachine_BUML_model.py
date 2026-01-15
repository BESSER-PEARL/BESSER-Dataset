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
statemachine_ValueGuard = Class(name="statemachine::ValueGuard")
Guard = Class(name="Guard")
statemachine_Statemachine = Class(name="statemachine::Statemachine")
statemachine_Event = Class(name="statemachine::Event")
statemachine_Command = Class(name="statemachine::Command")
statemachine_Constant = Class(name="statemachine::Constant")
statemachine_State = Class(name="statemachine::State")
statemachine_Guard = Class(name="statemachine::Guard")
statemachine_Value = Class(name="statemachine::Value")
statemachine_RangeGuard = Class(name="statemachine::RangeGuard")
statemachine_ConstantRef = Class(name="statemachine::ConstantRef")
Value = Class(name="Value")
statemachine_IntLiteral = Class(name="statemachine::IntLiteral")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Thing = Class(name="statemachine::Thing")

# statemachine_ValueGuard class attributes and methods

# Guard class attributes and methods

# statemachine_Statemachine class attributes and methods
statemachine_Statemachine_name: Property = Property(name="name", type=StringType)
statemachine_Statemachine.attributes={statemachine_Statemachine_name}

# statemachine_Event class attributes and methods
statemachine_Event_name: Property = Property(name="name", type=StringType)
statemachine_Event_code: Property = Property(name="code", type=IntegerType)
statemachine_Event.attributes={statemachine_Event_name, statemachine_Event_code}

# statemachine_Command class attributes and methods
statemachine_Command_name: Property = Property(name="name", type=StringType)
statemachine_Command_code: Property = Property(name="code", type=IntegerType)
statemachine_Command.attributes={statemachine_Command_name, statemachine_Command_code}

# statemachine_Constant class attributes and methods
statemachine_Constant_name: Property = Property(name="name", type=StringType)
statemachine_Constant.attributes={statemachine_Constant_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State_description: Property = Property(name="description", type=StringType)
statemachine_State.attributes={statemachine_State_description, statemachine_State_name}

# statemachine_Guard class attributes and methods

# statemachine_Value class attributes and methods

# statemachine_RangeGuard class attributes and methods

# statemachine_ConstantRef class attributes and methods

# Value class attributes and methods

# statemachine_IntLiteral class attributes and methods
statemachine_IntLiteral_value: Property = Property(name="value", type=IntegerType)
statemachine_IntLiteral.attributes={statemachine_IntLiteral_value}

# statemachine_Transition class attributes and methods

# statemachine_Thing class attributes and methods
statemachine_Thing_name: Property = Property(name="name", type=StringType)
statemachine_Thing.attributes={statemachine_Thing_name}

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="statemachine_Event", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resetEvents1: BinaryAssociation = BinaryAssociation(
    name="resetEvents1",
    ends={
        Property(name="statemachine_Event3", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine2", type=statemachine_Event, multiplicity=Multiplicity(0, 9999))
    }
)
commands4: BinaryAssociation = BinaryAssociation(
    name="commands4",
    ends={
        Property(name="statemachine_Command", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine5", type=statemachine_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants6: BinaryAssociation = BinaryAssociation(
    name="constants6",
    ends={
        Property(name="statemachine_Constant", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine7", type=statemachine_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states8: BinaryAssociation = BinaryAssociation(
    name="states8",
    ends={
        Property(name="statemachine_State", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine9", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard10: BinaryAssociation = BinaryAssociation(
    name="guard10",
    ends={
        Property(name="statemachine_Guard", type=statemachine_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Event11", type=statemachine_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="statemachine_Value25", type=statemachine_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Constant24", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond12: BinaryAssociation = BinaryAssociation(
    name="cond12",
    ends={
        Property(name="statemachine_Value", type=statemachine_ValueGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_ValueGuard", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
min13: BinaryAssociation = BinaryAssociation(
    name="min13",
    ends={
        Property(name="statemachine_Value14", type=statemachine_RangeGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_RangeGuard", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max15: BinaryAssociation = BinaryAssociation(
    name="max15",
    ends={
        Property(name="statemachine_Value17", type=statemachine_RangeGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_RangeGuard16", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant18: BinaryAssociation = BinaryAssociation(
    name="constant18",
    ends={
        Property(name="statemachine_Constant19", type=statemachine_ConstantRef, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_ConstantRef", type=statemachine_Constant, multiplicity=Multiplicity(0, 1))
    }
)
guard20: BinaryAssociation = BinaryAssociation(
    name="guard20",
    ends={
        Property(name="statemachine_Guard22", type=statemachine_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Command21", type=statemachine_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions26: BinaryAssociation = BinaryAssociation(
    name="actions26",
    ends={
        Property(name="statemachine_Command28", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State27", type=statemachine_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions29: BinaryAssociation = BinaryAssociation(
    name="transitions29",
    ends={
        Property(name="statemachine_Transition", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State30", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things31: BinaryAssociation = BinaryAssociation(
    name="things31",
    ends={
        Property(name="statemachine_Thing", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State32", type=statemachine_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event33: BinaryAssociation = BinaryAssociation(
    name="event33",
    ends={
        Property(name="statemachine_Event35", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition34", type=statemachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
guard36: BinaryAssociation = BinaryAssociation(
    name="guard36",
    ends={
        Property(name="statemachine_Guard38", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition37", type=statemachine_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state39: BinaryAssociation = BinaryAssociation(
    name="state39",
    ends={
        Property(name="statemachine_State41", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition40", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
guard42: BinaryAssociation = BinaryAssociation(
    name="guard42",
    ends={
        Property(name="statemachine_Guard44", type=statemachine_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Thing43", type=statemachine_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statemachine_ValueGuard_Guard = Generalization(general=Guard, specific=statemachine_ValueGuard)
gen_statemachine_RangeGuard_Guard = Generalization(general=Guard, specific=statemachine_RangeGuard)
gen_statemachine_ConstantRef_Value = Generalization(general=Value, specific=statemachine_ConstantRef)
gen_statemachine_IntLiteral_Value = Generalization(general=Value, specific=statemachine_IntLiteral)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_ValueGuard, Guard, statemachine_Statemachine, statemachine_Event, statemachine_Command, statemachine_Constant, statemachine_State, statemachine_Guard, statemachine_Value, statemachine_RangeGuard, statemachine_ConstantRef, Value, statemachine_IntLiteral, statemachine_Transition, statemachine_Thing},
    associations={events0, resetEvents1, commands4, constants6, states8, guard10, value23, cond12, min13, max15, constant18, guard20, actions26, transitions29, things31, event33, guard36, state39, guard42},
    generalizations={gen_statemachine_ValueGuard_Guard, gen_statemachine_RangeGuard_Guard, gen_statemachine_ConstantRef_Value, gen_statemachine_IntLiteral_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)