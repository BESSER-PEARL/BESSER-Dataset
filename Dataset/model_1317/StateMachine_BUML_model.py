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

# Enumerations
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="Final"),
			EnumerationLiteral(name="Initial")
    }
)

# Classes
stateMachine_DeclaredParameter = Class(name="stateMachine::DeclaredParameter")
stateMachine_model = Class(name="stateMachine::model")
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_Event = Class(name="stateMachine::Event")
stateMachine_Command = Class(name="stateMachine::Command")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Type = Class(name="stateMachine::Type")
stateMachine_Test = Class(name="stateMachine::Test")
stateMachine_Modifier = Class(name="stateMachine::Modifier")
stateMachine_Transition = Class(name="stateMachine::Transition")
stateMachine_Condition = Class(name="stateMachine::Condition")
stateMachine_VarName = Class(name="stateMachine::VarName")
stateMachine_StringType = Class(name="stateMachine::StringType")
Type = Class(name="Type")
stateMachine_FloatType = Class(name="stateMachine::FloatType")

# stateMachine_DeclaredParameter class attributes and methods

# stateMachine_model class attributes and methods

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name}

# stateMachine_Event class attributes and methods
stateMachine_Event_name: Property = Property(name="name", type=StringType)
stateMachine_Event.attributes={stateMachine_Event_name}

# stateMachine_Command class attributes and methods
stateMachine_Command_name: Property = Property(name="name", type=StringType)
stateMachine_Command.attributes={stateMachine_Command_name}

# stateMachine_State class attributes and methods
stateMachine_State_name: Property = Property(name="name", type=StringType)
stateMachine_State.attributes={stateMachine_State_name}

# stateMachine_Type class attributes and methods
stateMachine_Type_type: Property = Property(name="type", type=StringType)
stateMachine_Type.attributes={stateMachine_Type_type}

# stateMachine_Test class attributes and methods

# stateMachine_Modifier class attributes and methods
stateMachine_Modifier_visibility: Property = Property(name="visibility", type=StringType)
stateMachine_Modifier.attributes={stateMachine_Modifier_visibility}

# stateMachine_Transition class attributes and methods

# stateMachine_Condition class attributes and methods
stateMachine_Condition_name: Property = Property(name="name", type=StringType)
stateMachine_Condition.attributes={stateMachine_Condition_name}

# stateMachine_VarName class attributes and methods
stateMachine_VarName_value: Property = Property(name="value", type=StringType)
stateMachine_VarName.attributes={stateMachine_VarName_value}

# stateMachine_StringType class attributes and methods

# Type class attributes and methods

# stateMachine_FloatType class attributes and methods

# Relationships
types17: BinaryAssociation = BinaryAssociation(
    name="types17",
    ends={
        Property(name="stateMachine_Type19", type=stateMachine_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Test18", type=stateMachine_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args20: BinaryAssociation = BinaryAssociation(
    name="args20",
    ends={
        Property(name="stateMachine_DeclaredParameter", type=stateMachine_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Test21", type=stateMachine_DeclaredParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="stateMachine_StateMachine", type=stateMachine_model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_model", type=stateMachine_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="stateMachine_Event", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands3: BinaryAssociation = BinaryAssociation(
    name="commands3",
    ends={
        Property(name="stateMachine_Command", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine6", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstates7: BinaryAssociation = BinaryAssociation(
    name="initialstates7",
    ends={
        Property(name="stateMachine_State9", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine8", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
finalstates10: BinaryAssociation = BinaryAssociation(
    name="finalstates10",
    ends={
        Property(name="stateMachine_State12", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine11", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
returnType13: BinaryAssociation = BinaryAssociation(
    name="returnType13",
    ends={
        Property(name="stateMachine_Type", type=stateMachine_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Event14", type=stateMachine_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tests15: BinaryAssociation = BinaryAssociation(
    name="tests15",
    ends={
        Property(name="stateMachine_Test", type=stateMachine_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Event16", type=stateMachine_Test, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions22: BinaryAssociation = BinaryAssociation(
    name="actions22",
    ends={
        Property(name="stateMachine_Command24", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State23", type=stateMachine_Command, multiplicity=Multiplicity(0, 9999))
    }
)
transitions25: BinaryAssociation = BinaryAssociation(
    name="transitions25",
    ends={
        Property(name="stateMachine_Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_State26", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event27: BinaryAssociation = BinaryAssociation(
    name="event27",
    ends={
        Property(name="stateMachine_Event29", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition28", type=stateMachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
state30: BinaryAssociation = BinaryAssociation(
    name="state30",
    ends={
        Property(name="stateMachine_State32", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition31", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="stateMachine_Condition", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_Transition34", type=stateMachine_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name35: BinaryAssociation = BinaryAssociation(
    name="name35",
    ends={
        Property(name="stateMachine_VarName", type=stateMachine_DeclaredParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_DeclaredParameter36", type=stateMachine_VarName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_stateMachine_StringType_Type = Generalization(general=Type, specific=stateMachine_StringType)
gen_stateMachine_FloatType_Type = Generalization(general=Type, specific=stateMachine_FloatType)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_DeclaredParameter, stateMachine_model, stateMachine_StateMachine, stateMachine_Event, stateMachine_Command, stateMachine_State, stateMachine_Type, stateMachine_Test, stateMachine_Modifier, stateMachine_Transition, stateMachine_Condition, stateMachine_VarName, stateMachine_StringType, Type, stateMachine_FloatType, Visibility},
    associations={types17, args20, statemachine0, events1, commands3, states5, initialstates7, finalstates10, returnType13, tests15, actions22, transitions25, event27, state30, condition33, name35},
    generalizations={gen_stateMachine_StringType_Type, gen_stateMachine_FloatType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)