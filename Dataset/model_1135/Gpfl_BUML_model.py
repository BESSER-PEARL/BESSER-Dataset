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
gpfl_Field = Class(name="gpfl::Field")
gpfl_Program = Class(name="gpfl::Program")
gpfl_AutomataDef = Class(name="gpfl::AutomataDef")
gpfl_GExpression = Class(name="gpfl::GExpression")
gpfl_NopCmd = Class(name="gpfl::NopCmd")
gpfl_AcceptCmd = Class(name="gpfl::AcceptCmd")
gpfl_DropCmd = Class(name="gpfl::DropCmd")
gpfl_SendCmd = Class(name="gpfl::SendCmd")
gpfl_State = Class(name="gpfl::State")
gpfl_Transition = Class(name="gpfl::Transition")
gpfl_CondStmt = Class(name="gpfl::CondStmt")
GExpression = Class(name="GExpression")
gpfl_IterStmt = Class(name="gpfl::IterStmt")
gpfl_InterruptStmt = Class(name="gpfl::InterruptStmt")
gpfl_CmdNEq = Class(name="gpfl::CmdNEq")
gpfl_AlarmCmd = Class(name="gpfl::AlarmCmd")
gpfl_SetCmd = Class(name="gpfl::SetCmd")
gpfl_AutomatonCmd = Class(name="gpfl::AutomatonCmd")
gpfl_StpCmd = Class(name="gpfl::StpCmd")
gpfl_CmdAnd = Class(name="gpfl::CmdAnd")
gpfl_CmdEq = Class(name="gpfl::CmdEq")
gpfl_CmdSub = Class(name="gpfl::CmdSub")
gpfl_CmdGECompare = Class(name="gpfl::CmdGECompare")
gpfl_CmdLECompare = Class(name="gpfl::CmdLECompare")
gpfl_CmdGCompare = Class(name="gpfl::CmdGCompare")
gpfl_CmdLCompare = Class(name="gpfl::CmdLCompare")
gpfl_CmdAdd = Class(name="gpfl::CmdAdd")
gpfl_IntLitCmd = Class(name="gpfl::IntLitCmd")
gpfl_GBoolTrue = Class(name="gpfl::GBoolTrue")
gpfl_GBoolFalse = Class(name="gpfl::GBoolFalse")
gpfl_StringLit = Class(name="gpfl::StringLit")
gpfl_Variable = Class(name="gpfl::Variable")
gpfl_PortLit = Class(name="gpfl::PortLit")
gpfl_InPort = Class(name="gpfl::InPort")
gpfl_OutPort = Class(name="gpfl::OutPort")

# gpfl_Field class attributes and methods
gpfl_Field_name: Property = Property(name="name", type=StringType)
gpfl_Field.attributes={gpfl_Field_name}

# gpfl_Program class attributes and methods
gpfl_Program_name: Property = Property(name="name", type=StringType)
gpfl_Program.attributes={gpfl_Program_name}

# gpfl_AutomataDef class attributes and methods
gpfl_AutomataDef_name: Property = Property(name="name", type=StringType)
gpfl_AutomataDef.attributes={gpfl_AutomataDef_name}

# gpfl_GExpression class attributes and methods

# gpfl_NopCmd class attributes and methods

# gpfl_AcceptCmd class attributes and methods

# gpfl_DropCmd class attributes and methods

# gpfl_SendCmd class attributes and methods

# gpfl_State class attributes and methods
gpfl_State_name: Property = Property(name="name", type=StringType)
gpfl_State.attributes={gpfl_State_name}

# gpfl_Transition class attributes and methods
gpfl_Transition_event: Property = Property(name="event", type=StringType)
gpfl_Transition.attributes={gpfl_Transition_event}

# gpfl_CondStmt class attributes and methods

# GExpression class attributes and methods

# gpfl_IterStmt class attributes and methods

# gpfl_InterruptStmt class attributes and methods
gpfl_InterruptStmt_timeout: Property = Property(name="timeout", type=IntegerType)
gpfl_InterruptStmt.attributes={gpfl_InterruptStmt_timeout}

# gpfl_CmdNEq class attributes and methods

# gpfl_AlarmCmd class attributes and methods

# gpfl_SetCmd class attributes and methods
gpfl_SetCmd_name: Property = Property(name="name", type=StringType)
gpfl_SetCmd.attributes={gpfl_SetCmd_name}

# gpfl_AutomatonCmd class attributes and methods
gpfl_AutomatonCmd_name: Property = Property(name="name", type=StringType)
gpfl_AutomatonCmd.attributes={gpfl_AutomatonCmd_name}

# gpfl_StpCmd class attributes and methods

# gpfl_CmdAnd class attributes and methods

# gpfl_CmdEq class attributes and methods

# gpfl_CmdSub class attributes and methods

# gpfl_CmdGECompare class attributes and methods

# gpfl_CmdLECompare class attributes and methods

# gpfl_CmdGCompare class attributes and methods

# gpfl_CmdLCompare class attributes and methods

# gpfl_CmdAdd class attributes and methods

# gpfl_IntLitCmd class attributes and methods
gpfl_IntLitCmd_value: Property = Property(name="value", type=IntegerType)
gpfl_IntLitCmd.attributes={gpfl_IntLitCmd_value}

# gpfl_GBoolTrue class attributes and methods

# gpfl_GBoolFalse class attributes and methods

# gpfl_StringLit class attributes and methods
gpfl_StringLit_value: Property = Property(name="value", type=StringType)
gpfl_StringLit.attributes={gpfl_StringLit_value}

# gpfl_Variable class attributes and methods
gpfl_Variable_value: Property = Property(name="value", type=StringType)
gpfl_Variable.attributes={gpfl_Variable_value}

# gpfl_PortLit class attributes and methods
gpfl_PortLit_inSide: Property = Property(name="inSide", type=BooleanType)
gpfl_PortLit.attributes={gpfl_PortLit_inSide}

# gpfl_InPort class attributes and methods

# gpfl_OutPort class attributes and methods

# Relationships
expression7: BinaryAssociation = BinaryAssociation(
    name="expression7",
    ends={
        Property(name="gpfl_GExpression8", type=gpfl_GExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_GExpression6", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="gpfl_GExpression10", type=gpfl_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_Field", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
automatas0: BinaryAssociation = BinaryAssociation(
    name="automatas0",
    ends={
        Property(name="gpfl_AutomataDef", type=gpfl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_Program", type=gpfl_AutomataDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initStmts1: BinaryAssociation = BinaryAssociation(
    name="initStmts1",
    ends={
        Property(name="gpfl_GExpression", type=gpfl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_Program2", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts3: BinaryAssociation = BinaryAssociation(
    name="stmts3",
    ends={
        Property(name="gpfl_GExpression5", type=gpfl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_Program4", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts33: BinaryAssociation = BinaryAssociation(
    name="stmts33",
    ends={
        Property(name="gpfl_GExpression35", type=gpfl_InterruptStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_InterruptStmt34", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port36: BinaryAssociation = BinaryAssociation(
    name="port36",
    ends={
        Property(name="gpfl_GExpression37", type=gpfl_SendCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_SendCmd", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init11: BinaryAssociation = BinaryAssociation(
    name="init11",
    ends={
        Property(name="gpfl_State", type=gpfl_AutomataDef, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_AutomataDef12", type=gpfl_State, multiplicity=Multiplicity(0, 1))
    }
)
states13: BinaryAssociation = BinaryAssociation(
    name="states13",
    ends={
        Property(name="gpfl_State15", type=gpfl_AutomataDef, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_AutomataDef14", type=gpfl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions16: BinaryAssociation = BinaryAssociation(
    name="transitions16",
    ends={
        Property(name="gpfl_Transition", type=gpfl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_State17", type=gpfl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="gpfl_State20", type=gpfl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_Transition19", type=gpfl_State, multiplicity=Multiplicity(0, 1))
    }
)
exp21: BinaryAssociation = BinaryAssociation(
    name="exp21",
    ends={
        Property(name="gpfl_GExpression22", type=gpfl_CondStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CondStmt", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts23: BinaryAssociation = BinaryAssociation(
    name="stmts23",
    ends={
        Property(name="gpfl_GExpression25", type=gpfl_CondStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CondStmt24", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp26: BinaryAssociation = BinaryAssociation(
    name="exp26",
    ends={
        Property(name="gpfl_GExpression27", type=gpfl_IterStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_IterStmt", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts28: BinaryAssociation = BinaryAssociation(
    name="stmts28",
    ends={
        Property(name="gpfl_GExpression30", type=gpfl_IterStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_IterStmt29", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
periodic31: BinaryAssociation = BinaryAssociation(
    name="periodic31",
    ends={
        Property(name="gpfl_GExpression32", type=gpfl_InterruptStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_InterruptStmt", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="gpfl_GExpression61", type=gpfl_CmdEq, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdEq", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="gpfl_GExpression64", type=gpfl_CmdEq, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdEq63", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="gpfl_GExpression66", type=gpfl_CmdNEq, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdNEq", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields38: BinaryAssociation = BinaryAssociation(
    name="fields38",
    ends={
        Property(name="gpfl_Field40", type=gpfl_SendCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_SendCmd39", type=gpfl_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp41: BinaryAssociation = BinaryAssociation(
    name="exp41",
    ends={
        Property(name="gpfl_GExpression42", type=gpfl_AlarmCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_AlarmCmd", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp43: BinaryAssociation = BinaryAssociation(
    name="exp43",
    ends={
        Property(name="gpfl_GExpression44", type=gpfl_SetCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_SetCmd", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
automaton45: BinaryAssociation = BinaryAssociation(
    name="automaton45",
    ends={
        Property(name="gpfl_AutomataDef46", type=gpfl_AutomatonCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_AutomatonCmd", type=gpfl_AutomataDef, multiplicity=Multiplicity(0, 1))
    }
)
automaton47: BinaryAssociation = BinaryAssociation(
    name="automaton47",
    ends={
        Property(name="gpfl_AutomatonCmd48", type=gpfl_StpCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_StpCmd", type=gpfl_AutomatonCmd, multiplicity=Multiplicity(0, 1))
    }
)
event49: BinaryAssociation = BinaryAssociation(
    name="event49",
    ends={
        Property(name="gpfl_GExpression51", type=gpfl_StpCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_StpCmd50", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
errors52: BinaryAssociation = BinaryAssociation(
    name="errors52",
    ends={
        Property(name="gpfl_GExpression54", type=gpfl_StpCmd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_StpCmd53", type=gpfl_GExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="gpfl_GExpression56", type=gpfl_CmdAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdAnd", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="gpfl_GExpression59", type=gpfl_CmdAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdAnd58", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right92: BinaryAssociation = BinaryAssociation(
    name="right92",
    ends={
        Property(name="gpfl_GExpression94", type=gpfl_CmdAdd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdAdd93", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="gpfl_GExpression96", type=gpfl_CmdSub, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdSub", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right97: BinaryAssociation = BinaryAssociation(
    name="right97",
    ends={
        Property(name="gpfl_GExpression99", type=gpfl_CmdSub, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdSub98", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="gpfl_GExpression69", type=gpfl_CmdNEq, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdNEq68", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left70: BinaryAssociation = BinaryAssociation(
    name="left70",
    ends={
        Property(name="gpfl_GExpression71", type=gpfl_CmdGECompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdGECompare", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right72: BinaryAssociation = BinaryAssociation(
    name="right72",
    ends={
        Property(name="gpfl_GExpression74", type=gpfl_CmdGECompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdGECompare73", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left75: BinaryAssociation = BinaryAssociation(
    name="left75",
    ends={
        Property(name="gpfl_GExpression76", type=gpfl_CmdLECompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdLECompare", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right77: BinaryAssociation = BinaryAssociation(
    name="right77",
    ends={
        Property(name="gpfl_GExpression79", type=gpfl_CmdLECompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdLECompare78", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="gpfl_GExpression81", type=gpfl_CmdGCompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdGCompare", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="gpfl_GExpression84", type=gpfl_CmdGCompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdGCompare83", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left85: BinaryAssociation = BinaryAssociation(
    name="left85",
    ends={
        Property(name="gpfl_GExpression86", type=gpfl_CmdLCompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdLCompare", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right87: BinaryAssociation = BinaryAssociation(
    name="right87",
    ends={
        Property(name="gpfl_GExpression89", type=gpfl_CmdLCompare, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdLCompare88", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left90: BinaryAssociation = BinaryAssociation(
    name="left90",
    ends={
        Property(name="gpfl_GExpression91", type=gpfl_CmdAdd, multiplicity=Multiplicity(1, 1)),
        Property(name="gpfl_CmdAdd", type=gpfl_GExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_gpfl_NopCmd_GExpression = Generalization(general=GExpression, specific=gpfl_NopCmd)
gen_gpfl_AcceptCmd_GExpression = Generalization(general=GExpression, specific=gpfl_AcceptCmd)
gen_gpfl_DropCmd_GExpression = Generalization(general=GExpression, specific=gpfl_DropCmd)
gen_gpfl_SendCmd_GExpression = Generalization(general=GExpression, specific=gpfl_SendCmd)
gen_gpfl_CondStmt_GExpression = Generalization(general=GExpression, specific=gpfl_CondStmt)
gen_gpfl_IterStmt_GExpression = Generalization(general=GExpression, specific=gpfl_IterStmt)
gen_gpfl_InterruptStmt_GExpression = Generalization(general=GExpression, specific=gpfl_InterruptStmt)
gen_gpfl_CmdNEq_GExpression = Generalization(general=GExpression, specific=gpfl_CmdNEq)
gen_gpfl_AlarmCmd_GExpression = Generalization(general=GExpression, specific=gpfl_AlarmCmd)
gen_gpfl_SetCmd_GExpression = Generalization(general=GExpression, specific=gpfl_SetCmd)
gen_gpfl_AutomatonCmd_GExpression = Generalization(general=GExpression, specific=gpfl_AutomatonCmd)
gen_gpfl_StpCmd_GExpression = Generalization(general=GExpression, specific=gpfl_StpCmd)
gen_gpfl_CmdAnd_GExpression = Generalization(general=GExpression, specific=gpfl_CmdAnd)
gen_gpfl_CmdEq_GExpression = Generalization(general=GExpression, specific=gpfl_CmdEq)
gen_gpfl_CmdSub_GExpression = Generalization(general=GExpression, specific=gpfl_CmdSub)
gen_gpfl_CmdGECompare_GExpression = Generalization(general=GExpression, specific=gpfl_CmdGECompare)
gen_gpfl_CmdLECompare_GExpression = Generalization(general=GExpression, specific=gpfl_CmdLECompare)
gen_gpfl_CmdGCompare_GExpression = Generalization(general=GExpression, specific=gpfl_CmdGCompare)
gen_gpfl_CmdLCompare_GExpression = Generalization(general=GExpression, specific=gpfl_CmdLCompare)
gen_gpfl_CmdAdd_GExpression = Generalization(general=GExpression, specific=gpfl_CmdAdd)
gen_gpfl_IntLitCmd_GExpression = Generalization(general=GExpression, specific=gpfl_IntLitCmd)
gen_gpfl_GBoolTrue_GExpression = Generalization(general=GExpression, specific=gpfl_GBoolTrue)
gen_gpfl_GBoolFalse_GExpression = Generalization(general=GExpression, specific=gpfl_GBoolFalse)
gen_gpfl_StringLit_GExpression = Generalization(general=GExpression, specific=gpfl_StringLit)
gen_gpfl_Variable_GExpression = Generalization(general=GExpression, specific=gpfl_Variable)
gen_gpfl_PortLit_GExpression = Generalization(general=GExpression, specific=gpfl_PortLit)
gen_gpfl_InPort_GExpression = Generalization(general=GExpression, specific=gpfl_InPort)
gen_gpfl_OutPort_GExpression = Generalization(general=GExpression, specific=gpfl_OutPort)

# Domain Model
domain_model = DomainModel(
    name="gpfl",
    types={gpfl_Field, gpfl_Program, gpfl_AutomataDef, gpfl_GExpression, gpfl_NopCmd, gpfl_AcceptCmd, gpfl_DropCmd, gpfl_SendCmd, gpfl_State, gpfl_Transition, gpfl_CondStmt, GExpression, gpfl_IterStmt, gpfl_InterruptStmt, gpfl_CmdNEq, gpfl_AlarmCmd, gpfl_SetCmd, gpfl_AutomatonCmd, gpfl_StpCmd, gpfl_CmdAnd, gpfl_CmdEq, gpfl_CmdSub, gpfl_CmdGECompare, gpfl_CmdLECompare, gpfl_CmdGCompare, gpfl_CmdLCompare, gpfl_CmdAdd, gpfl_IntLitCmd, gpfl_GBoolTrue, gpfl_GBoolFalse, gpfl_StringLit, gpfl_Variable, gpfl_PortLit, gpfl_InPort, gpfl_OutPort},
    associations={expression7, value9, automatas0, initStmts1, stmts3, stmts33, port36, init11, states13, transitions16, target18, exp21, stmts23, exp26, stmts28, periodic31, left60, right62, left65, fields38, exp41, exp43, automaton45, automaton47, event49, errors52, left55, right57, right92, left95, right97, right67, left70, right72, left75, right77, left80, right82, left85, right87, left90},
    generalizations={gen_gpfl_NopCmd_GExpression, gen_gpfl_AcceptCmd_GExpression, gen_gpfl_DropCmd_GExpression, gen_gpfl_SendCmd_GExpression, gen_gpfl_CondStmt_GExpression, gen_gpfl_IterStmt_GExpression, gen_gpfl_InterruptStmt_GExpression, gen_gpfl_CmdNEq_GExpression, gen_gpfl_AlarmCmd_GExpression, gen_gpfl_SetCmd_GExpression, gen_gpfl_AutomatonCmd_GExpression, gen_gpfl_StpCmd_GExpression, gen_gpfl_CmdAnd_GExpression, gen_gpfl_CmdEq_GExpression, gen_gpfl_CmdSub_GExpression, gen_gpfl_CmdGECompare_GExpression, gen_gpfl_CmdLECompare_GExpression, gen_gpfl_CmdGCompare_GExpression, gen_gpfl_CmdLCompare_GExpression, gen_gpfl_CmdAdd_GExpression, gen_gpfl_IntLitCmd_GExpression, gen_gpfl_GBoolTrue_GExpression, gen_gpfl_GBoolFalse_GExpression, gen_gpfl_StringLit_GExpression, gen_gpfl_Variable_GExpression, gen_gpfl_PortLit_GExpression, gen_gpfl_InPort_GExpression, gen_gpfl_OutPort_GExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)