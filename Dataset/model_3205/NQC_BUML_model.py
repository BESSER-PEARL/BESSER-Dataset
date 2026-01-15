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
AssignmentStatementEnum: Enumeration = Enumeration(
    name="AssignmentStatementEnum",
    literals={
            EnumerationLiteral(name="assign")
    }
)

TypeEnum: Enumeration = Enumeration(
    name="TypeEnum",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="IntegerArray")
    }
)

BinaryOperatorEnum: Enumeration = Enumeration(
    name="BinaryOperatorEnum",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="bitand"),
			EnumerationLiteral(name="bitor"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="times"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="mod"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notequal"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="geq")
    }
)

# Classes
NQC_Program = Class(name="NQC::Program")
NQC_Task = Class(name="NQC::Task")
NQC_Function = Class(name="NQC::Function")
NQC_Subroutine = Class(name="NQC::Subroutine")
NQC_Parameter = Class(name="NQC::Parameter")
Variable = Class(name="Variable")
NQC_Variable = Class(name="NQC::Variable", is_abstract=True)
NQC_GlobalVariable = Class(name="NQC::GlobalVariable")
NQC_Statement = Class(name="NQC::Statement", is_abstract=True)
NQC_LocalVariable = Class(name="NQC::LocalVariable")
NQC_AssignmentStatement = Class(name="NQC::AssignmentStatement")
Statement = Class(name="Statement")
NQC_VariableExpression = Class(name="NQC::VariableExpression")
NQC_Expression = Class(name="NQC::Expression", is_abstract=True)
NQC_BlockStatement = Class(name="NQC::BlockStatement")
NQC_BreakStatement = Class(name="NQC::BreakStatement")
NQC_ConstantExpression = Class(name="NQC::ConstantExpression", is_abstract=True)
NQC_IntegerConstant = Class(name="NQC::IntegerConstant")
NQC_Label = Class(name="NQC::Label")
NQC_StopStatement = Class(name="NQC::StopStatement")
NQC_DoWhileStatement = Class(name="NQC::DoWhileStatement")
ControlStructure = Class(name="ControlStructure")
NQC_ForStatement = Class(name="NQC::ForStatement")
NQC_ContinueStatement = Class(name="NQC::ContinueStatement")
NQC_ControlStructure = Class(name="NQC::ControlStructure", is_abstract=True)
NQC_EmptyStatement = Class(name="NQC::EmptyStatement")
NQC_ReturnStatement = Class(name="NQC::ReturnStatement")
NQC_StartStatement = Class(name="NQC::StartStatement")
NQC_IfStatement = Class(name="NQC::IfStatement")
NQC_RepeatStatement = Class(name="NQC::RepeatStatement")
NQC_GoToStatement = Class(name="NQC::GoToStatement")
NQC_WhileStatement = Class(name="NQC::WhileStatement")
NQC_SwitchStatement = Class(name="NQC::SwitchStatement")
NQC_Case = Class(name="NQC::Case")
NQC_UntilStatement = Class(name="NQC::UntilStatement")
NQC_BooleanConstant = Class(name="NQC::BooleanConstant")
ConstantExpression = Class(name="ConstantExpression")
NQC_CompoundExpression = Class(name="NQC::CompoundExpression", is_abstract=True)
NQC_BinaryExpression = Class(name="NQC::BinaryExpression")
CompoundExpression = Class(name="CompoundExpression")
NQC_ValueExpression = Class(name="NQC::ValueExpression", is_abstract=True)
Expression = Class(name="Expression")
ValueExpression = Class(name="ValueExpression")
NQC_ArrayExpression = Class(name="NQC::ArrayExpression")
VariableExpression = Class(name="VariableExpression")
NQC_SubroutineCall = Class(name="NQC::SubroutineCall")
NQC_CallStatement = Class(name="NQC::CallStatement", is_abstract=True)
NQC_FunctionCall = Class(name="NQC::FunctionCall")
CallStatement = Class(name="CallStatement")

# NQC_Program class attributes and methods
NQC_Program_Name: Property = Property(name="Name", type=StringType)
NQC_Program.attributes={NQC_Program_Name}

# NQC_Task class attributes and methods
NQC_Task_Name: Property = Property(name="Name", type=StringType)
NQC_Task.attributes={NQC_Task_Name}

# NQC_Function class attributes and methods
NQC_Function_Name: Property = Property(name="Name", type=StringType)
NQC_Function.attributes={NQC_Function_Name}

# NQC_Subroutine class attributes and methods
NQC_Subroutine_Name: Property = Property(name="Name", type=StringType)
NQC_Subroutine.attributes={NQC_Subroutine_Name}

# NQC_Parameter class attributes and methods

# Variable class attributes and methods

# NQC_Variable class attributes and methods
NQC_Variable_Name: Property = Property(name="Name", type=StringType)
NQC_Variable_Type: Property = Property(name="Type", type=StringType)
NQC_Variable.attributes={NQC_Variable_Type, NQC_Variable_Name}

# NQC_GlobalVariable class attributes and methods

# NQC_Statement class attributes and methods

# NQC_LocalVariable class attributes and methods

# NQC_AssignmentStatement class attributes and methods
NQC_AssignmentStatement_Operator: Property = Property(name="Operator", type=StringType)
NQC_AssignmentStatement.attributes={NQC_AssignmentStatement_Operator}

# Statement class attributes and methods

# NQC_VariableExpression class attributes and methods

# NQC_Expression class attributes and methods

# NQC_BlockStatement class attributes and methods

# NQC_BreakStatement class attributes and methods

# NQC_ConstantExpression class attributes and methods

# NQC_IntegerConstant class attributes and methods
NQC_IntegerConstant_Value: Property = Property(name="Value", type=IntegerType)
NQC_IntegerConstant.attributes={NQC_IntegerConstant_Value}

# NQC_Label class attributes and methods
NQC_Label_Label: Property = Property(name="Label", type=StringType)
NQC_Label.attributes={NQC_Label_Label}

# NQC_StopStatement class attributes and methods

# NQC_DoWhileStatement class attributes and methods

# ControlStructure class attributes and methods

# NQC_ForStatement class attributes and methods

# NQC_ContinueStatement class attributes and methods

# NQC_ControlStructure class attributes and methods

# NQC_EmptyStatement class attributes and methods

# NQC_ReturnStatement class attributes and methods

# NQC_StartStatement class attributes and methods

# NQC_IfStatement class attributes and methods

# NQC_RepeatStatement class attributes and methods

# NQC_GoToStatement class attributes and methods

# NQC_WhileStatement class attributes and methods

# NQC_SwitchStatement class attributes and methods

# NQC_Case class attributes and methods
NQC_Case_IsDefault: Property = Property(name="IsDefault", type=BooleanType)
NQC_Case.attributes={NQC_Case_IsDefault}

# NQC_UntilStatement class attributes and methods

# NQC_BooleanConstant class attributes and methods
NQC_BooleanConstant_Value: Property = Property(name="Value", type=BooleanType)
NQC_BooleanConstant.attributes={NQC_BooleanConstant_Value}

# ConstantExpression class attributes and methods

# NQC_CompoundExpression class attributes and methods

# NQC_BinaryExpression class attributes and methods
NQC_BinaryExpression_Operator: Property = Property(name="Operator", type=StringType)
NQC_BinaryExpression.attributes={NQC_BinaryExpression_Operator}

# CompoundExpression class attributes and methods

# NQC_ValueExpression class attributes and methods

# Expression class attributes and methods

# ValueExpression class attributes and methods

# NQC_ArrayExpression class attributes and methods

# VariableExpression class attributes and methods

# NQC_SubroutineCall class attributes and methods

# NQC_CallStatement class attributes and methods

# NQC_FunctionCall class attributes and methods

# CallStatement class attributes and methods

# Relationships
Tasks0: BinaryAssociation = BinaryAssociation(
    name="Tasks0",
    ends={
        Property(name="NQC_Task", type=NQC_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Program", type=NQC_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Functions1: BinaryAssociation = BinaryAssociation(
    name="Functions1",
    ends={
        Property(name="NQC_Function", type=NQC_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Program2", type=NQC_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Subroutines3: BinaryAssociation = BinaryAssociation(
    name="Subroutines3",
    ends={
        Property(name="NQC_Subroutine", type=NQC_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Program4", type=NQC_Subroutine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Statements11: BinaryAssociation = BinaryAssociation(
    name="Statements11",
    ends={
        Property(name="NQC_Statement13", type=NQC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Function12", type=NQC_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LocalVariables14: BinaryAssociation = BinaryAssociation(
    name="LocalVariables14",
    ends={
        Property(name="NQC_LocalVariable16", type=NQC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Function15", type=NQC_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameters17: BinaryAssociation = BinaryAssociation(
    name="Parameters17",
    ends={
        Property(name="NQC_Parameter", type=NQC_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Function18", type=NQC_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Statements19: BinaryAssociation = BinaryAssociation(
    name="Statements19",
    ends={
        Property(name="NQC_Statement21", type=NQC_Subroutine, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Subroutine20", type=NQC_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LocalVariables22: BinaryAssociation = BinaryAssociation(
    name="LocalVariables22",
    ends={
        Property(name="NQC_LocalVariable24", type=NQC_Subroutine, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Subroutine23", type=NQC_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
GlobalVariables5: BinaryAssociation = BinaryAssociation(
    name="GlobalVariables5",
    ends={
        Property(name="NQC_GlobalVariable", type=NQC_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Program6", type=NQC_GlobalVariable, multiplicity=Multiplicity(0, 32), is_composite=True)
    }
)
Statements7: BinaryAssociation = BinaryAssociation(
    name="Statements7",
    ends={
        Property(name="NQC_Statement", type=NQC_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Task8", type=NQC_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LocalVariables9: BinaryAssociation = BinaryAssociation(
    name="LocalVariables9",
    ends={
        Property(name="NQC_LocalVariable", type=NQC_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Task10", type=NQC_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Label28: BinaryAssociation = BinaryAssociation(
    name="Label28",
    ends={
        Property(name="NQC_Label", type=NQC_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Statement29", type=NQC_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Variable30: BinaryAssociation = BinaryAssociation(
    name="Variable30",
    ends={
        Property(name="NQC_VariableExpression", type=NQC_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_AssignmentStatement", type=NQC_VariableExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Expression31: BinaryAssociation = BinaryAssociation(
    name="Expression31",
    ends={
        Property(name="NQC_Expression", type=NQC_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_AssignmentStatement32", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LocalVariables33: BinaryAssociation = BinaryAssociation(
    name="LocalVariables33",
    ends={
        Property(name="NQC_LocalVariable34", type=NQC_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_BlockStatement", type=NQC_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Statements35: BinaryAssociation = BinaryAssociation(
    name="Statements35",
    ends={
        Property(name="NQC_Statement37", type=NQC_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_BlockStatement36", type=NQC_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialValue25: BinaryAssociation = BinaryAssociation(
    name="InitialValue25",
    ends={
        Property(name="NQC_ConstantExpression", type=NQC_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Variable", type=NQC_ConstantExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ArrayMaxSize26: BinaryAssociation = BinaryAssociation(
    name="ArrayMaxSize26",
    ends={
        Property(name="NQC_IntegerConstant", type=NQC_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Variable27", type=NQC_IntegerConstant, multiplicity=Multiplicity(0, 1))
    }
)
Task40: BinaryAssociation = BinaryAssociation(
    name="Task40",
    ends={
        Property(name="NQC_Task41", type=NQC_StopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_StopStatement", type=NQC_Task, multiplicity=Multiplicity(1, 1))
    }
)
Body42: BinaryAssociation = BinaryAssociation(
    name="Body42",
    ends={
        Property(name="NQC_Statement43", type=NQC_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_DoWhileStatement", type=NQC_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition44: BinaryAssociation = BinaryAssociation(
    name="Condition44",
    ends={
        Property(name="NQC_Expression46", type=NQC_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_DoWhileStatement45", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Initialization47: BinaryAssociation = BinaryAssociation(
    name="Initialization47",
    ends={
        Property(name="NQC_Statement48", type=NQC_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_ForStatement", type=NQC_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Task38: BinaryAssociation = BinaryAssociation(
    name="Task38",
    ends={
        Property(name="NQC_Task39", type=NQC_StartStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_StartStatement", type=NQC_Task, multiplicity=Multiplicity(1, 1))
    }
)
Condition57: BinaryAssociation = BinaryAssociation(
    name="Condition57",
    ends={
        Property(name="NQC_Expression58", type=NQC_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_IfStatement", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Consequence59: BinaryAssociation = BinaryAssociation(
    name="Consequence59",
    ends={
        Property(name="NQC_Statement61", type=NQC_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_IfStatement60", type=NQC_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Alternative62: BinaryAssociation = BinaryAssociation(
    name="Alternative62",
    ends={
        Property(name="NQC_Statement64", type=NQC_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_IfStatement63", type=NQC_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Condition65: BinaryAssociation = BinaryAssociation(
    name="Condition65",
    ends={
        Property(name="NQC_Expression66", type=NQC_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_RepeatStatement", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body67: BinaryAssociation = BinaryAssociation(
    name="Body67",
    ends={
        Property(name="NQC_Statement69", type=NQC_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_RepeatStatement68", type=NQC_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition49: BinaryAssociation = BinaryAssociation(
    name="Condition49",
    ends={
        Property(name="NQC_Expression51", type=NQC_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_ForStatement50", type=NQC_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Update52: BinaryAssociation = BinaryAssociation(
    name="Update52",
    ends={
        Property(name="NQC_Statement54", type=NQC_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_ForStatement53", type=NQC_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
JumpLabel55: BinaryAssociation = BinaryAssociation(
    name="JumpLabel55",
    ends={
        Property(name="NQC_Label56", type=NQC_GoToStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_GoToStatement", type=NQC_Label, multiplicity=Multiplicity(1, 1))
    }
)
Body76: BinaryAssociation = BinaryAssociation(
    name="Body76",
    ends={
        Property(name="NQC_Statement78", type=NQC_UntilStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_UntilStatement77", type=NQC_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Condition79: BinaryAssociation = BinaryAssociation(
    name="Condition79",
    ends={
        Property(name="NQC_Expression80", type=NQC_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_WhileStatement", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body81: BinaryAssociation = BinaryAssociation(
    name="Body81",
    ends={
        Property(name="NQC_Statement83", type=NQC_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_WhileStatement82", type=NQC_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Label84: BinaryAssociation = BinaryAssociation(
    name="Label84",
    ends={
        Property(name="NQC_ConstantExpression86", type=NQC_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Case85", type=NQC_ConstantExpression, multiplicity=Multiplicity(1, 9999))
    }
)
Statements87: BinaryAssociation = BinaryAssociation(
    name="Statements87",
    ends={
        Property(name="NQC_Statement89", type=NQC_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_Case88", type=NQC_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Condition70: BinaryAssociation = BinaryAssociation(
    name="Condition70",
    ends={
        Property(name="NQC_Expression71", type=NQC_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_SwitchStatement", type=NQC_Expression, multiplicity=Multiplicity(1, 1))
    }
)
Cases72: BinaryAssociation = BinaryAssociation(
    name="Cases72",
    ends={
        Property(name="NQC_Case", type=NQC_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_SwitchStatement73", type=NQC_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Condition74: BinaryAssociation = BinaryAssociation(
    name="Condition74",
    ends={
        Property(name="NQC_Expression75", type=NQC_UntilStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_UntilStatement", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Variable90: BinaryAssociation = BinaryAssociation(
    name="Variable90",
    ends={
        Property(name="NQC_Variable92", type=NQC_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_VariableExpression91", type=NQC_Variable, multiplicity=Multiplicity(1, 1))
    }
)
index93: BinaryAssociation = BinaryAssociation(
    name="index93",
    ends={
        Property(name="NQC_Expression94", type=NQC_ArrayExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_ArrayExpression", type=NQC_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Callee105: BinaryAssociation = BinaryAssociation(
    name="Callee105",
    ends={
        Property(name="NQC_Subroutine106", type=NQC_SubroutineCall, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_SubroutineCall", type=NQC_Subroutine, multiplicity=Multiplicity(1, 1))
    }
)
Operand195: BinaryAssociation = BinaryAssociation(
    name="Operand195",
    ends={
        Property(name="NQC_Expression96", type=NQC_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_BinaryExpression", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operand297: BinaryAssociation = BinaryAssociation(
    name="Operand297",
    ends={
        Property(name="NQC_Expression99", type=NQC_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_BinaryExpression98", type=NQC_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Callee100: BinaryAssociation = BinaryAssociation(
    name="Callee100",
    ends={
        Property(name="NQC_Function101", type=NQC_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_FunctionCall", type=NQC_Function, multiplicity=Multiplicity(1, 1))
    }
)
Parameters102: BinaryAssociation = BinaryAssociation(
    name="Parameters102",
    ends={
        Property(name="NQC_Expression104", type=NQC_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="NQC_FunctionCall103", type=NQC_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_NQC_Parameter_Variable = Generalization(general=Variable, specific=NQC_Parameter)
gen_NQC_AssignmentStatement_Statement = Generalization(general=Statement, specific=NQC_AssignmentStatement)
gen_NQC_BlockStatement_Statement = Generalization(general=Statement, specific=NQC_BlockStatement)
gen_NQC_BreakStatement_Statement = Generalization(general=Statement, specific=NQC_BreakStatement)
gen_NQC_LocalVariable_Variable = Generalization(general=Variable, specific=NQC_LocalVariable)
gen_NQC_GlobalVariable_Variable = Generalization(general=Variable, specific=NQC_GlobalVariable)
gen_NQC_StopStatement_Statement = Generalization(general=Statement, specific=NQC_StopStatement)
gen_NQC_DoWhileStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_DoWhileStatement)
gen_NQC_ForStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_ForStatement)
gen_NQC_ContinueStatement_Statement = Generalization(general=Statement, specific=NQC_ContinueStatement)
gen_NQC_ControlStructure_Statement = Generalization(general=Statement, specific=NQC_ControlStructure)
gen_NQC_EmptyStatement_Statement = Generalization(general=Statement, specific=NQC_EmptyStatement)
gen_NQC_Expression_Statement = Generalization(general=Statement, specific=NQC_Expression)
gen_NQC_ReturnStatement_Statement = Generalization(general=Statement, specific=NQC_ReturnStatement)
gen_NQC_StartStatement_Statement = Generalization(general=Statement, specific=NQC_StartStatement)
gen_NQC_IfStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_IfStatement)
gen_NQC_RepeatStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_RepeatStatement)
gen_NQC_GoToStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_GoToStatement)
gen_NQC_WhileStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_WhileStatement)
gen_NQC_SwitchStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_SwitchStatement)
gen_NQC_UntilStatement_ControlStructure = Generalization(general=ControlStructure, specific=NQC_UntilStatement)
gen_NQC_ConstantExpression_ValueExpression = Generalization(general=ValueExpression, specific=NQC_ConstantExpression)
gen_NQC_BooleanConstant_ConstantExpression = Generalization(general=ConstantExpression, specific=NQC_BooleanConstant)
gen_NQC_IntegerConstant_ConstantExpression = Generalization(general=ConstantExpression, specific=NQC_IntegerConstant)
gen_NQC_CompoundExpression_Expression = Generalization(general=Expression, specific=NQC_CompoundExpression)
gen_NQC_BinaryExpression_CompoundExpression = Generalization(general=CompoundExpression, specific=NQC_BinaryExpression)
gen_NQC_ValueExpression_Expression = Generalization(general=Expression, specific=NQC_ValueExpression)
gen_NQC_VariableExpression_ValueExpression = Generalization(general=ValueExpression, specific=NQC_VariableExpression)
gen_NQC_ArrayExpression_VariableExpression = Generalization(general=VariableExpression, specific=NQC_ArrayExpression)
gen_NQC_SubroutineCall_CallStatement = Generalization(general=CallStatement, specific=NQC_SubroutineCall)
gen_NQC_CallStatement_Statement = Generalization(general=Statement, specific=NQC_CallStatement)
gen_NQC_FunctionCall_CallStatement = Generalization(general=CallStatement, specific=NQC_FunctionCall)

# Domain Model
domain_model = DomainModel(
    name="NQC",
    types={NQC_Program, NQC_Task, NQC_Function, NQC_Subroutine, NQC_Parameter, Variable, NQC_Variable, NQC_GlobalVariable, NQC_Statement, NQC_LocalVariable, NQC_AssignmentStatement, Statement, NQC_VariableExpression, NQC_Expression, NQC_BlockStatement, NQC_BreakStatement, NQC_ConstantExpression, NQC_IntegerConstant, NQC_Label, NQC_StopStatement, NQC_DoWhileStatement, ControlStructure, NQC_ForStatement, NQC_ContinueStatement, NQC_ControlStructure, NQC_EmptyStatement, NQC_ReturnStatement, NQC_StartStatement, NQC_IfStatement, NQC_RepeatStatement, NQC_GoToStatement, NQC_WhileStatement, NQC_SwitchStatement, NQC_Case, NQC_UntilStatement, NQC_BooleanConstant, ConstantExpression, NQC_CompoundExpression, NQC_BinaryExpression, CompoundExpression, NQC_ValueExpression, Expression, ValueExpression, NQC_ArrayExpression, VariableExpression, NQC_SubroutineCall, NQC_CallStatement, NQC_FunctionCall, CallStatement, AssignmentStatementEnum, TypeEnum, BinaryOperatorEnum},
    associations={Tasks0, Functions1, Subroutines3, Statements11, LocalVariables14, Parameters17, Statements19, LocalVariables22, GlobalVariables5, Statements7, LocalVariables9, Label28, Variable30, Expression31, LocalVariables33, Statements35, InitialValue25, ArrayMaxSize26, Task40, Body42, Condition44, Initialization47, Task38, Condition57, Consequence59, Alternative62, Condition65, Body67, Condition49, Update52, JumpLabel55, Body76, Condition79, Body81, Label84, Statements87, Condition70, Cases72, Condition74, Variable90, index93, Callee105, Operand195, Operand297, Callee100, Parameters102},
    generalizations={gen_NQC_Parameter_Variable, gen_NQC_AssignmentStatement_Statement, gen_NQC_BlockStatement_Statement, gen_NQC_BreakStatement_Statement, gen_NQC_LocalVariable_Variable, gen_NQC_GlobalVariable_Variable, gen_NQC_StopStatement_Statement, gen_NQC_DoWhileStatement_ControlStructure, gen_NQC_ForStatement_ControlStructure, gen_NQC_ContinueStatement_Statement, gen_NQC_ControlStructure_Statement, gen_NQC_EmptyStatement_Statement, gen_NQC_Expression_Statement, gen_NQC_ReturnStatement_Statement, gen_NQC_StartStatement_Statement, gen_NQC_IfStatement_ControlStructure, gen_NQC_RepeatStatement_ControlStructure, gen_NQC_GoToStatement_ControlStructure, gen_NQC_WhileStatement_ControlStructure, gen_NQC_SwitchStatement_ControlStructure, gen_NQC_UntilStatement_ControlStructure, gen_NQC_ConstantExpression_ValueExpression, gen_NQC_BooleanConstant_ConstantExpression, gen_NQC_IntegerConstant_ConstantExpression, gen_NQC_CompoundExpression_Expression, gen_NQC_BinaryExpression_CompoundExpression, gen_NQC_ValueExpression_Expression, gen_NQC_VariableExpression_ValueExpression, gen_NQC_ArrayExpression_VariableExpression, gen_NQC_SubroutineCall_CallStatement, gen_NQC_CallStatement_Statement, gen_NQC_FunctionCall_CallStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)