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
statemachine_PrintCommand = Class(name="statemachine_PrintCommand")
statemachine_VerbatimExpression = Class(name="statemachine_VerbatimExpression")
Expression = Class(name="Expression")
statemachine_Statemachine = Class(name="statemachine_Statemachine")
statemachine_State = Class(name="statemachine_State")
statemachine_Transition = Class(name="statemachine_Transition")
statemachine_Command = Class(name="statemachine_Command")
statemachine_Expression = Class(name="statemachine_Expression")
statemachine_SetCommand = Class(name="statemachine_SetCommand")
Command = Class(name="Command")
statemachine_ExecuteCommand = Class(name="statemachine_ExecuteCommand")
statemachine_StatePropertyExpression = Class(name="statemachine_StatePropertyExpression")

# statemachine_PrintCommand class attributes and methods

# statemachine_VerbatimExpression class attributes and methods
statemachine_VerbatimExpression_code: Property = Property(name="code", type=StringType)
statemachine_VerbatimExpression.attributes={statemachine_VerbatimExpression_code}

# Expression class attributes and methods

# statemachine_Statemachine class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_initial: Property = Property(name="initial", type=BooleanType)
statemachine_State_final: Property = Property(name="final", type=BooleanType)
statemachine_State_id: Property = Property(name="id", type=StringType)
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_id, statemachine_State_initial, statemachine_State_final, statemachine_State_name}

# statemachine_Transition class attributes and methods

# statemachine_Command class attributes and methods

# statemachine_Expression class attributes and methods

# statemachine_SetCommand class attributes and methods
statemachine_SetCommand_signal: Property = Property(name="signal", type=StringType)
statemachine_SetCommand.attributes={statemachine_SetCommand_signal}

# Command class attributes and methods

# statemachine_ExecuteCommand class attributes and methods
statemachine_ExecuteCommand_operation: Property = Property(name="operation", type=StringType)
statemachine_ExecuteCommand.attributes={statemachine_ExecuteCommand_operation}

# statemachine_StatePropertyExpression class attributes and methods
statemachine_StatePropertyExpression__property: Property = Property(name="_property", type=StringType)
statemachine_StatePropertyExpression.attributes={statemachine_StatePropertyExpression__property}

# Relationships
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="statemachine_Expression18", type=statemachine_PrintCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_PrintCommand", type=statemachine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions3: BinaryAssociation = BinaryAssociation(
    name="actions3",
    ends={
        Property(name="statemachine_Command", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State4", type=statemachine_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceState5: BinaryAssociation = BinaryAssociation(
    name="sourceState5",
    ends={
        Property(name="statemachine_State7", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition6", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
targetState8: BinaryAssociation = BinaryAssociation(
    name="targetState8",
    ends={
        Property(name="statemachine_State10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition9", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
event11: BinaryAssociation = BinaryAssociation(
    name="event11",
    ends={
        Property(name="statemachine_Expression", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition12", type=statemachine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="statemachine_Expression14", type=statemachine_SetCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SetCommand", type=statemachine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments15: BinaryAssociation = BinaryAssociation(
    name="arguments15",
    ends={
        Property(name="statemachine_Expression16", type=statemachine_ExecuteCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_ExecuteCommand", type=statemachine_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="statemachine_State20", type=statemachine_StatePropertyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StatePropertyExpression", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemachine_PrintCommand_Command = Generalization(general=Command, specific=statemachine_PrintCommand)
gen_statemachine_VerbatimExpression_Expression = Generalization(general=Expression, specific=statemachine_VerbatimExpression)
gen_statemachine_SetCommand_Command = Generalization(general=Command, specific=statemachine_SetCommand)
gen_statemachine_ExecuteCommand_Command = Generalization(general=Command, specific=statemachine_ExecuteCommand)
gen_statemachine_StatePropertyExpression_Expression = Generalization(general=Expression, specific=statemachine_StatePropertyExpression)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_PrintCommand, statemachine_VerbatimExpression, Expression, statemachine_Statemachine, statemachine_State, statemachine_Transition, statemachine_Command, statemachine_Expression, statemachine_SetCommand, Command, statemachine_ExecuteCommand, statemachine_StatePropertyExpression},
    associations={value17, states0, transitions1, actions3, sourceState5, targetState8, event11, value13, arguments15, state19},
    generalizations={gen_statemachine_PrintCommand_Command, gen_statemachine_VerbatimExpression_Expression, gen_statemachine_SetCommand_Command, gen_statemachine_ExecuteCommand_Command, gen_statemachine_StatePropertyExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)