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
stateMachineDsl_StateMachine = Class(name="stateMachineDsl::StateMachine")
stateMachineDsl_Declaration = Class(name="stateMachineDsl::Declaration")
stateMachineDsl_State = Class(name="stateMachineDsl::State")
stateMachineDsl_Variable = Class(name="stateMachineDsl::Variable")
stateMachineDsl_ExtDeclaration = Class(name="stateMachineDsl::ExtDeclaration")
stateMachineDsl_Event = Class(name="stateMachineDsl::Event")
stateMachineDsl_Procedure = Class(name="stateMachineDsl::Procedure")
stateMachineDsl_MemberState = Class(name="stateMachineDsl::MemberState")
stateMachineDsl_Action = Class(name="stateMachineDsl::Action")
stateMachineDsl_Transition = Class(name="stateMachineDsl::Transition")
stateMachineDsl_CommandAction = Class(name="stateMachineDsl::CommandAction")
stateMachineDsl_Condition = Class(name="stateMachineDsl::Condition")
stateMachineDsl_VarParName = Class(name="stateMachineDsl::VarParName")
stateMachineDsl_VarType = Class(name="stateMachineDsl::VarType")
stateMachineDsl_Expression = Class(name="stateMachineDsl::Expression")
stateMachineDsl_ParameterFunction = Class(name="stateMachineDsl::ParameterFunction")
stateMachineDsl_Member = Class(name="stateMachineDsl::Member")
stateMachineDsl_Parameter = Class(name="stateMachineDsl::Parameter")
ExtDeclaration = Class(name="ExtDeclaration")
stateMachineDsl_Function = Class(name="stateMachineDsl::Function")
stateMachineDsl_EObject = Class(name="stateMachineDsl::EObject")
stateMachineDsl_SetAction = Class(name="stateMachineDsl::SetAction")
stateMachineDsl_ChangeAction = Class(name="stateMachineDsl::ChangeAction")
stateMachineDsl_FunctionUse = Class(name="stateMachineDsl::FunctionUse")
Expression = Class(name="Expression")
stateMachineDsl_ProcedureUse = Class(name="stateMachineDsl::ProcedureUse")
stateMachineDsl_IncrementAction = Class(name="stateMachineDsl::IncrementAction")
ChangeAction = Class(name="ChangeAction")
stateMachineDsl_DecrementAction = Class(name="stateMachineDsl::DecrementAction")
stateMachineDsl_ResetAction = Class(name="stateMachineDsl::ResetAction")
stateMachineDsl_Or = Class(name="stateMachineDsl::Or")
stateMachineDsl_And = Class(name="stateMachineDsl::And")
stateMachineDsl_Equality = Class(name="stateMachineDsl::Equality")
stateMachineDsl_Comparison = Class(name="stateMachineDsl::Comparison")
stateMachineDsl_PlusCond = Class(name="stateMachineDsl::PlusCond")
stateMachineDsl_MinusCond = Class(name="stateMachineDsl::MinusCond")
stateMachineDsl_MulOrDiv = Class(name="stateMachineDsl::MulOrDiv")
stateMachineDsl_Parenthesis = Class(name="stateMachineDsl::Parenthesis")
stateMachineDsl_NumberExp = Class(name="stateMachineDsl::NumberExp")
stateMachineDsl_StringExp = Class(name="stateMachineDsl::StringExp")
stateMachineDsl_BoolExp = Class(name="stateMachineDsl::BoolExp")
stateMachineDsl_VarRef = Class(name="stateMachineDsl::VarRef")
stateMachineDsl_DoubleExp = Class(name="stateMachineDsl::DoubleExp")
stateMachineDsl_Not = Class(name="stateMachineDsl::Not")

# stateMachineDsl_StateMachine class attributes and methods
stateMachineDsl_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachineDsl_StateMachine.attributes={stateMachineDsl_StateMachine_name}

# stateMachineDsl_Declaration class attributes and methods

# stateMachineDsl_State class attributes and methods
stateMachineDsl_State_name: Property = Property(name="name", type=StringType)
stateMachineDsl_State.attributes={stateMachineDsl_State_name}

# stateMachineDsl_Variable class attributes and methods

# stateMachineDsl_ExtDeclaration class attributes and methods
stateMachineDsl_ExtDeclaration_name: Property = Property(name="name", type=StringType)
stateMachineDsl_ExtDeclaration.attributes={stateMachineDsl_ExtDeclaration_name}

# stateMachineDsl_Event class attributes and methods
stateMachineDsl_Event_name: Property = Property(name="name", type=StringType)
stateMachineDsl_Event.attributes={stateMachineDsl_Event_name}

# stateMachineDsl_Procedure class attributes and methods
stateMachineDsl_Procedure_name: Property = Property(name="name", type=StringType)
stateMachineDsl_Procedure.attributes={stateMachineDsl_Procedure_name}

# stateMachineDsl_MemberState class attributes and methods

# stateMachineDsl_Action class attributes and methods

# stateMachineDsl_Transition class attributes and methods

# stateMachineDsl_CommandAction class attributes and methods

# stateMachineDsl_Condition class attributes and methods

# stateMachineDsl_VarParName class attributes and methods
stateMachineDsl_VarParName_name: Property = Property(name="name", type=StringType)
stateMachineDsl_VarParName.attributes={stateMachineDsl_VarParName_name}

# stateMachineDsl_VarType class attributes and methods
stateMachineDsl_VarType_vt: Property = Property(name="vt", type=StringType)
stateMachineDsl_VarType.attributes={stateMachineDsl_VarType_vt}

# stateMachineDsl_Expression class attributes and methods

# stateMachineDsl_ParameterFunction class attributes and methods
stateMachineDsl_ParameterFunction_name: Property = Property(name="name", type=StringType)
stateMachineDsl_ParameterFunction.attributes={stateMachineDsl_ParameterFunction_name}

# stateMachineDsl_Member class attributes and methods

# stateMachineDsl_Parameter class attributes and methods

# ExtDeclaration class attributes and methods

# stateMachineDsl_Function class attributes and methods

# stateMachineDsl_EObject class attributes and methods

# stateMachineDsl_SetAction class attributes and methods

# stateMachineDsl_ChangeAction class attributes and methods

# stateMachineDsl_FunctionUse class attributes and methods

# Expression class attributes and methods

# stateMachineDsl_ProcedureUse class attributes and methods

# stateMachineDsl_IncrementAction class attributes and methods

# ChangeAction class attributes and methods

# stateMachineDsl_DecrementAction class attributes and methods

# stateMachineDsl_ResetAction class attributes and methods

# stateMachineDsl_Or class attributes and methods

# stateMachineDsl_And class attributes and methods

# stateMachineDsl_Equality class attributes and methods
stateMachineDsl_Equality_op: Property = Property(name="op", type=StringType)
stateMachineDsl_Equality.attributes={stateMachineDsl_Equality_op}

# stateMachineDsl_Comparison class attributes and methods
stateMachineDsl_Comparison_op: Property = Property(name="op", type=StringType)
stateMachineDsl_Comparison.attributes={stateMachineDsl_Comparison_op}

# stateMachineDsl_PlusCond class attributes and methods

# stateMachineDsl_MinusCond class attributes and methods

# stateMachineDsl_MulOrDiv class attributes and methods
stateMachineDsl_MulOrDiv_op: Property = Property(name="op", type=StringType)
stateMachineDsl_MulOrDiv.attributes={stateMachineDsl_MulOrDiv_op}

# stateMachineDsl_Parenthesis class attributes and methods

# stateMachineDsl_NumberExp class attributes and methods
stateMachineDsl_NumberExp_negative: Property = Property(name="negative", type=StringType)
stateMachineDsl_NumberExp_value: Property = Property(name="value", type=IntegerType)
stateMachineDsl_NumberExp.attributes={stateMachineDsl_NumberExp_value, stateMachineDsl_NumberExp_negative}

# stateMachineDsl_StringExp class attributes and methods
stateMachineDsl_StringExp_value: Property = Property(name="value", type=StringType)
stateMachineDsl_StringExp.attributes={stateMachineDsl_StringExp_value}

# stateMachineDsl_BoolExp class attributes and methods
stateMachineDsl_BoolExp_value: Property = Property(name="value", type=StringType)
stateMachineDsl_BoolExp.attributes={stateMachineDsl_BoolExp_value}

# stateMachineDsl_VarRef class attributes and methods

# stateMachineDsl_DoubleExp class attributes and methods
stateMachineDsl_DoubleExp_negative: Property = Property(name="negative", type=StringType)
stateMachineDsl_DoubleExp_number: Property = Property(name="number", type=IntegerType)
stateMachineDsl_DoubleExp_decimal: Property = Property(name="decimal", type=IntegerType)
stateMachineDsl_DoubleExp.attributes={stateMachineDsl_DoubleExp_decimal, stateMachineDsl_DoubleExp_number, stateMachineDsl_DoubleExp_negative}

# stateMachineDsl_Not class attributes and methods

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="stateMachineDsl_Declaration", type=stateMachineDsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_StateMachine", type=stateMachineDsl_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="stateMachineDsl_State", type=stateMachineDsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_StateMachine2", type=stateMachineDsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="stateMachineDsl_State5", type=stateMachineDsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_StateMachine4", type=stateMachineDsl_State, multiplicity=Multiplicity(0, 1))
    }
)
variable6: BinaryAssociation = BinaryAssociation(
    name="variable6",
    ends={
        Property(name="stateMachineDsl_Variable", type=stateMachineDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Declaration7", type=stateMachineDsl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extdecl8: BinaryAssociation = BinaryAssociation(
    name="extdecl8",
    ends={
        Property(name="stateMachineDsl_ExtDeclaration", type=stateMachineDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Declaration9", type=stateMachineDsl_ExtDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event10: BinaryAssociation = BinaryAssociation(
    name="event10",
    ends={
        Property(name="stateMachineDsl_Event", type=stateMachineDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Declaration11", type=stateMachineDsl_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure12: BinaryAssociation = BinaryAssociation(
    name="procedure12",
    ends={
        Property(name="stateMachineDsl_Procedure", type=stateMachineDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Declaration13", type=stateMachineDsl_Procedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members14: BinaryAssociation = BinaryAssociation(
    name="members14",
    ends={
        Property(name="stateMachineDsl_MemberState", type=stateMachineDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_State15", type=stateMachineDsl_MemberState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable16: BinaryAssociation = BinaryAssociation(
    name="variable16",
    ends={
        Property(name="stateMachineDsl_Variable18", type=stateMachineDsl_MemberState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MemberState17", type=stateMachineDsl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action19: BinaryAssociation = BinaryAssociation(
    name="action19",
    ends={
        Property(name="stateMachineDsl_Action", type=stateMachineDsl_MemberState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MemberState20", type=stateMachineDsl_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition21: BinaryAssociation = BinaryAssociation(
    name="transition21",
    ends={
        Property(name="stateMachineDsl_Transition", type=stateMachineDsl_MemberState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MemberState22", type=stateMachineDsl_Transition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commandaction23: BinaryAssociation = BinaryAssociation(
    name="commandaction23",
    ends={
        Property(name="stateMachineDsl_CommandAction", type=stateMachineDsl_MemberState, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MemberState24", type=stateMachineDsl_CommandAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to25: BinaryAssociation = BinaryAssociation(
    name="to25",
    ends={
        Property(name="stateMachineDsl_State27", type=stateMachineDsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Transition26", type=stateMachineDsl_State, multiplicity=Multiplicity(0, 1))
    }
)
event28: BinaryAssociation = BinaryAssociation(
    name="event28",
    ends={
        Property(name="stateMachineDsl_Event30", type=stateMachineDsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Transition29", type=stateMachineDsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="stateMachineDsl_Condition", type=stateMachineDsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Transition32", type=stateMachineDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions33: BinaryAssociation = BinaryAssociation(
    name="actions33",
    ends={
        Property(name="stateMachineDsl_Action35", type=stateMachineDsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Transition34", type=stateMachineDsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
n36: BinaryAssociation = BinaryAssociation(
    name="n36",
    ends={
        Property(name="stateMachineDsl_VarParName", type=stateMachineDsl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Variable37", type=stateMachineDsl_VarParName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="stateMachineDsl_VarType", type=stateMachineDsl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Variable39", type=stateMachineDsl_VarType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="stateMachineDsl_Expression", type=stateMachineDsl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Variable41", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters42: BinaryAssociation = BinaryAssociation(
    name="parameters42",
    ends={
        Property(name="stateMachineDsl_ParameterFunction", type=stateMachineDsl_ExtDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_ExtDeclaration43", type=stateMachineDsl_ParameterFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition44: BinaryAssociation = BinaryAssociation(
    name="condition44",
    ends={
        Property(name="stateMachineDsl_Condition46", type=stateMachineDsl_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Event45", type=stateMachineDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members47: BinaryAssociation = BinaryAssociation(
    name="members47",
    ends={
        Property(name="stateMachineDsl_Member", type=stateMachineDsl_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Event48", type=stateMachineDsl_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="stateMachineDsl_Parameter", type=stateMachineDsl_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Procedure50", type=stateMachineDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition51: BinaryAssociation = BinaryAssociation(
    name="condition51",
    ends={
        Property(name="stateMachineDsl_Condition53", type=stateMachineDsl_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Procedure52", type=stateMachineDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members54: BinaryAssociation = BinaryAssociation(
    name="members54",
    ends={
        Property(name="stateMachineDsl_Member56", type=stateMachineDsl_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Procedure55", type=stateMachineDsl_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type57: BinaryAssociation = BinaryAssociation(
    name="type57",
    ends={
        Property(name="stateMachineDsl_VarType59", type=stateMachineDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Parameter58", type=stateMachineDsl_VarType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
n60: BinaryAssociation = BinaryAssociation(
    name="n60",
    ends={
        Property(name="stateMachineDsl_VarParName62", type=stateMachineDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Parameter61", type=stateMachineDsl_VarParName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable63: BinaryAssociation = BinaryAssociation(
    name="variable63",
    ends={
        Property(name="stateMachineDsl_Variable65", type=stateMachineDsl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Member64", type=stateMachineDsl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action66: BinaryAssociation = BinaryAssociation(
    name="action66",
    ends={
        Property(name="stateMachineDsl_Action68", type=stateMachineDsl_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Member67", type=stateMachineDsl_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnvalue69: BinaryAssociation = BinaryAssociation(
    name="returnvalue69",
    ends={
        Property(name="stateMachineDsl_VarType70", type=stateMachineDsl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Function", type=stateMachineDsl_VarType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="stateMachineDsl_VarType73", type=stateMachineDsl_ParameterFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_ParameterFunction72", type=stateMachineDsl_VarType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action74: BinaryAssociation = BinaryAssociation(
    name="action74",
    ends={
        Property(name="stateMachineDsl_EObject", type=stateMachineDsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Action75", type=stateMachineDsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition76: BinaryAssociation = BinaryAssociation(
    name="condition76",
    ends={
        Property(name="stateMachineDsl_Condition78", type=stateMachineDsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Action77", type=stateMachineDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable79: BinaryAssociation = BinaryAssociation(
    name="variable79",
    ends={
        Property(name="stateMachineDsl_VarParName80", type=stateMachineDsl_SetAction, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_SetAction", type=stateMachineDsl_VarParName, multiplicity=Multiplicity(0, 1))
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="stateMachineDsl_Expression83", type=stateMachineDsl_SetAction, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_SetAction82", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable84: BinaryAssociation = BinaryAssociation(
    name="variable84",
    ends={
        Property(name="stateMachineDsl_VarParName85", type=stateMachineDsl_ChangeAction, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_ChangeAction", type=stateMachineDsl_VarParName, multiplicity=Multiplicity(0, 1))
    }
)
funct86: BinaryAssociation = BinaryAssociation(
    name="funct86",
    ends={
        Property(name="stateMachineDsl_Function87", type=stateMachineDsl_FunctionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_FunctionUse", type=stateMachineDsl_Function, multiplicity=Multiplicity(0, 1))
    }
)
arguments88: BinaryAssociation = BinaryAssociation(
    name="arguments88",
    ends={
        Property(name="stateMachineDsl_Expression90", type=stateMachineDsl_FunctionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_FunctionUse89", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedure91: BinaryAssociation = BinaryAssociation(
    name="procedure91",
    ends={
        Property(name="stateMachineDsl_Procedure92", type=stateMachineDsl_ProcedureUse, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_ProcedureUse", type=stateMachineDsl_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
arguments93: BinaryAssociation = BinaryAssociation(
    name="arguments93",
    ends={
        Property(name="stateMachineDsl_Expression95", type=stateMachineDsl_ProcedureUse, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_ProcedureUse94", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond96: BinaryAssociation = BinaryAssociation(
    name="cond96",
    ends={
        Property(name="stateMachineDsl_Expression98", type=stateMachineDsl_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Condition97", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left99: BinaryAssociation = BinaryAssociation(
    name="left99",
    ends={
        Property(name="stateMachineDsl_Expression100", type=stateMachineDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Or", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left104: BinaryAssociation = BinaryAssociation(
    name="left104",
    ends={
        Property(name="stateMachineDsl_Expression105", type=stateMachineDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_And", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right106: BinaryAssociation = BinaryAssociation(
    name="right106",
    ends={
        Property(name="stateMachineDsl_Expression108", type=stateMachineDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_And107", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left109: BinaryAssociation = BinaryAssociation(
    name="left109",
    ends={
        Property(name="stateMachineDsl_Expression110", type=stateMachineDsl_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Equality", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right111: BinaryAssociation = BinaryAssociation(
    name="right111",
    ends={
        Property(name="stateMachineDsl_Expression113", type=stateMachineDsl_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Equality112", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left114: BinaryAssociation = BinaryAssociation(
    name="left114",
    ends={
        Property(name="stateMachineDsl_Expression115", type=stateMachineDsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Comparison", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right116: BinaryAssociation = BinaryAssociation(
    name="right116",
    ends={
        Property(name="stateMachineDsl_Expression118", type=stateMachineDsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Comparison117", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left119: BinaryAssociation = BinaryAssociation(
    name="left119",
    ends={
        Property(name="stateMachineDsl_Expression120", type=stateMachineDsl_PlusCond, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_PlusCond", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right121: BinaryAssociation = BinaryAssociation(
    name="right121",
    ends={
        Property(name="stateMachineDsl_Expression123", type=stateMachineDsl_PlusCond, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_PlusCond122", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left124: BinaryAssociation = BinaryAssociation(
    name="left124",
    ends={
        Property(name="stateMachineDsl_Expression125", type=stateMachineDsl_MinusCond, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MinusCond", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right126: BinaryAssociation = BinaryAssociation(
    name="right126",
    ends={
        Property(name="stateMachineDsl_Expression128", type=stateMachineDsl_MinusCond, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MinusCond127", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left129: BinaryAssociation = BinaryAssociation(
    name="left129",
    ends={
        Property(name="stateMachineDsl_Expression130", type=stateMachineDsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MulOrDiv", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right131: BinaryAssociation = BinaryAssociation(
    name="right131",
    ends={
        Property(name="stateMachineDsl_Expression133", type=stateMachineDsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_MulOrDiv132", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right101: BinaryAssociation = BinaryAssociation(
    name="right101",
    ends={
        Property(name="stateMachineDsl_Expression103", type=stateMachineDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Or102", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond134: BinaryAssociation = BinaryAssociation(
    name="cond134",
    ends={
        Property(name="stateMachineDsl_Expression135", type=stateMachineDsl_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Parenthesis", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable136: BinaryAssociation = BinaryAssociation(
    name="variable136",
    ends={
        Property(name="stateMachineDsl_VarParName137", type=stateMachineDsl_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_VarRef", type=stateMachineDsl_VarParName, multiplicity=Multiplicity(0, 1))
    }
)
expression138: BinaryAssociation = BinaryAssociation(
    name="expression138",
    ends={
        Property(name="stateMachineDsl_Expression139", type=stateMachineDsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineDsl_Not", type=stateMachineDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_stateMachineDsl_CommandAction_ExtDeclaration = Generalization(general=ExtDeclaration, specific=stateMachineDsl_CommandAction)
gen_stateMachineDsl_Function_ExtDeclaration = Generalization(general=ExtDeclaration, specific=stateMachineDsl_Function)
gen_stateMachineDsl_FunctionUse_Expression = Generalization(general=Expression, specific=stateMachineDsl_FunctionUse)
gen_stateMachineDsl_IncrementAction_ChangeAction = Generalization(general=ChangeAction, specific=stateMachineDsl_IncrementAction)
gen_stateMachineDsl_DecrementAction_ChangeAction = Generalization(general=ChangeAction, specific=stateMachineDsl_DecrementAction)
gen_stateMachineDsl_ResetAction_ChangeAction = Generalization(general=ChangeAction, specific=stateMachineDsl_ResetAction)
gen_stateMachineDsl_Or_Expression = Generalization(general=Expression, specific=stateMachineDsl_Or)
gen_stateMachineDsl_And_Expression = Generalization(general=Expression, specific=stateMachineDsl_And)
gen_stateMachineDsl_Equality_Expression = Generalization(general=Expression, specific=stateMachineDsl_Equality)
gen_stateMachineDsl_Comparison_Expression = Generalization(general=Expression, specific=stateMachineDsl_Comparison)
gen_stateMachineDsl_PlusCond_Expression = Generalization(general=Expression, specific=stateMachineDsl_PlusCond)
gen_stateMachineDsl_MinusCond_Expression = Generalization(general=Expression, specific=stateMachineDsl_MinusCond)
gen_stateMachineDsl_MulOrDiv_Expression = Generalization(general=Expression, specific=stateMachineDsl_MulOrDiv)
gen_stateMachineDsl_Parenthesis_Expression = Generalization(general=Expression, specific=stateMachineDsl_Parenthesis)
gen_stateMachineDsl_NumberExp_Expression = Generalization(general=Expression, specific=stateMachineDsl_NumberExp)
gen_stateMachineDsl_StringExp_Expression = Generalization(general=Expression, specific=stateMachineDsl_StringExp)
gen_stateMachineDsl_BoolExp_Expression = Generalization(general=Expression, specific=stateMachineDsl_BoolExp)
gen_stateMachineDsl_VarRef_Expression = Generalization(general=Expression, specific=stateMachineDsl_VarRef)
gen_stateMachineDsl_DoubleExp_Expression = Generalization(general=Expression, specific=stateMachineDsl_DoubleExp)
gen_stateMachineDsl_Not_Expression = Generalization(general=Expression, specific=stateMachineDsl_Not)

# Domain Model
domain_model = DomainModel(
    name="stateMachineDsl",
    types={stateMachineDsl_StateMachine, stateMachineDsl_Declaration, stateMachineDsl_State, stateMachineDsl_Variable, stateMachineDsl_ExtDeclaration, stateMachineDsl_Event, stateMachineDsl_Procedure, stateMachineDsl_MemberState, stateMachineDsl_Action, stateMachineDsl_Transition, stateMachineDsl_CommandAction, stateMachineDsl_Condition, stateMachineDsl_VarParName, stateMachineDsl_VarType, stateMachineDsl_Expression, stateMachineDsl_ParameterFunction, stateMachineDsl_Member, stateMachineDsl_Parameter, ExtDeclaration, stateMachineDsl_Function, stateMachineDsl_EObject, stateMachineDsl_SetAction, stateMachineDsl_ChangeAction, stateMachineDsl_FunctionUse, Expression, stateMachineDsl_ProcedureUse, stateMachineDsl_IncrementAction, ChangeAction, stateMachineDsl_DecrementAction, stateMachineDsl_ResetAction, stateMachineDsl_Or, stateMachineDsl_And, stateMachineDsl_Equality, stateMachineDsl_Comparison, stateMachineDsl_PlusCond, stateMachineDsl_MinusCond, stateMachineDsl_MulOrDiv, stateMachineDsl_Parenthesis, stateMachineDsl_NumberExp, stateMachineDsl_StringExp, stateMachineDsl_BoolExp, stateMachineDsl_VarRef, stateMachineDsl_DoubleExp, stateMachineDsl_Not},
    associations={declarations0, states1, initial3, variable6, extdecl8, event10, procedure12, members14, variable16, action19, transition21, commandaction23, to25, event28, condition31, actions33, n36, type38, value40, parameters42, condition44, members47, parameters49, condition51, members54, type57, n60, variable63, action66, returnvalue69, type71, action74, condition76, variable79, value81, variable84, funct86, arguments88, procedure91, arguments93, cond96, left99, left104, right106, left109, right111, left114, right116, left119, right121, left124, right126, left129, right131, right101, cond134, variable136, expression138},
    generalizations={gen_stateMachineDsl_CommandAction_ExtDeclaration, gen_stateMachineDsl_Function_ExtDeclaration, gen_stateMachineDsl_FunctionUse_Expression, gen_stateMachineDsl_IncrementAction_ChangeAction, gen_stateMachineDsl_DecrementAction_ChangeAction, gen_stateMachineDsl_ResetAction_ChangeAction, gen_stateMachineDsl_Or_Expression, gen_stateMachineDsl_And_Expression, gen_stateMachineDsl_Equality_Expression, gen_stateMachineDsl_Comparison_Expression, gen_stateMachineDsl_PlusCond_Expression, gen_stateMachineDsl_MinusCond_Expression, gen_stateMachineDsl_MulOrDiv_Expression, gen_stateMachineDsl_Parenthesis_Expression, gen_stateMachineDsl_NumberExp_Expression, gen_stateMachineDsl_StringExp_Expression, gen_stateMachineDsl_BoolExp_Expression, gen_stateMachineDsl_VarRef_Expression, gen_stateMachineDsl_DoubleExp_Expression, gen_stateMachineDsl_Not_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)