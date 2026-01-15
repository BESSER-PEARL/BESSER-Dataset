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
lua_LastStatement_Return = Class(name="lua::LastStatement::Return")
LastStatement = Class(name="LastStatement")
lua_LastStatement_Break = Class(name="lua::LastStatement::Break")
lua_Statement_Block = Class(name="lua::Statement::Block")
Statement = Class(name="Statement")
lua_Statement_While = Class(name="lua::Statement::While")
lua_Expression = Class(name="lua::Expression")
lua_Chunk = Class(name="lua::Chunk")
lua_Block = Class(name="lua::Block")
Chunk = Class(name="Chunk")
lua_Statement = Class(name="lua::Statement")
lua_LastStatement = Class(name="lua::LastStatement")
lua_Statement_For_Numeric = Class(name="lua::Statement::For::Numeric")
lua_Statement_For_Generic = Class(name="lua::Statement::For::Generic")
lua_Statement_GlobalFunction_Declaration = Class(name="lua::Statement::GlobalFunction::Declaration")
lua_Statement_Repeat = Class(name="lua::Statement::Repeat")
lua_Function = Class(name="lua::Function")
lua_Statement_LocalFunction_Declaration = Class(name="lua::Statement::LocalFunction::Declaration")
lua_Statement_If_Then_Else = Class(name="lua::Statement::If::Then::Else")
lua_Statement_Local_Variable_Declaration = Class(name="lua::Statement::Local::Variable::Declaration")
lua_Statement_If_Then_Else_ElseIfPart = Class(name="lua::Statement::If::Then::Else::ElseIfPart")
lua_Statement_FunctioncallOrAssignment = Class(name="lua::Statement::FunctioncallOrAssignment")
Statement_FunctioncallOrAssignment = Class(name="Statement::FunctioncallOrAssignment")
lua_Expression_VarArgs = Class(name="lua::Expression::VarArgs")
lua_Expression_String = Class(name="lua::Expression::String")
lua_Expression_Function = Class(name="lua::Expression::Function")
lua_Expression_TableConstructor = Class(name="lua::Expression::TableConstructor")
lua_Field = Class(name="lua::Field")
lua_Functioncall_Arguments = Class(name="lua::Functioncall::Arguments")
lua_Field_AddEntryToTable_Brackets = Class(name="lua::Field::AddEntryToTable::Brackets")
Field = Class(name="Field")
lua_Field_AddEntryToTable = Class(name="lua::Field::AddEntryToTable")
lua_Field_AppendEntryToTable = Class(name="lua::Field::AppendEntryToTable")
lua_LastStatement_ReturnWithValue = Class(name="lua::LastStatement::ReturnWithValue")
LastStatement_Return = Class(name="LastStatement::Return")
lua_Statement_Assignment = Class(name="lua::Statement::Assignment")
lua_Expression_Nil = Class(name="lua::Expression::Nil")
Expression = Class(name="Expression")
lua_Expression_True = Class(name="lua::Expression::True")
lua_Expression_False = Class(name="lua::Expression::False")
lua_Expression_Number = Class(name="lua::Expression::Number")
lua_Statement_CallFunction = Class(name="lua::Statement::CallFunction")
lua_Expression_Or = Class(name="lua::Expression::Or")
lua_Expression_And = Class(name="lua::Expression::And")
lua_Expression_Larger = Class(name="lua::Expression::Larger")
lua_Expression_Larger_Equal = Class(name="lua::Expression::Larger::Equal")
lua_Expression_Smaller = Class(name="lua::Expression::Smaller")
lua_Statement_CallMemberFunction = Class(name="lua::Statement::CallMemberFunction")
lua_Expression_Smaller_Equal = Class(name="lua::Expression::Smaller::Equal")
lua_Expression_Equal = Class(name="lua::Expression::Equal")
lua_Expression_Not_Equal = Class(name="lua::Expression::Not::Equal")
lua_Expression_Concatenation = Class(name="lua::Expression::Concatenation")
lua_Expression_Plus = Class(name="lua::Expression::Plus")
lua_Expression_Minus = Class(name="lua::Expression::Minus")
lua_Expression_Multiplication = Class(name="lua::Expression::Multiplication")
lua_Expression_Division = Class(name="lua::Expression::Division")
lua_Expression_Modulo = Class(name="lua::Expression::Modulo")
lua_Expression_Negate = Class(name="lua::Expression::Negate")
lua_Expression_Length = Class(name="lua::Expression::Length")
lua_Expression_Invert = Class(name="lua::Expression::Invert")
lua_Expression_CallMemberFunction = Class(name="lua::Expression::CallMemberFunction")
lua_Expression_CallFunction = Class(name="lua::Expression::CallFunction")
lua_Expression_AccessArray = Class(name="lua::Expression::AccessArray")
lua_Expression_AccessMember = Class(name="lua::Expression::AccessMember")
lua_Expression_VariableName = Class(name="lua::Expression::VariableName")
lua_Expression_Exponentiation = Class(name="lua::Expression::Exponentiation")

# lua_LastStatement_Return class attributes and methods

# LastStatement class attributes and methods

# lua_LastStatement_Break class attributes and methods

# lua_Statement_Block class attributes and methods

# Statement class attributes and methods

# lua_Statement_While class attributes and methods

# lua_Expression class attributes and methods

# lua_Chunk class attributes and methods

# lua_Block class attributes and methods

# Chunk class attributes and methods

# lua_Statement class attributes and methods

# lua_LastStatement class attributes and methods

# lua_Statement_For_Numeric class attributes and methods
lua_Statement_For_Numeric_iteratorName: Property = Property(name="iteratorName", type=StringType)
lua_Statement_For_Numeric.attributes={lua_Statement_For_Numeric_iteratorName}

# lua_Statement_For_Generic class attributes and methods
lua_Statement_For_Generic_names: Property = Property(name="names", type=StringType)
lua_Statement_For_Generic.attributes={lua_Statement_For_Generic_names}

# lua_Statement_GlobalFunction_Declaration class attributes and methods
lua_Statement_GlobalFunction_Declaration_prefix: Property = Property(name="prefix", type=StringType)
lua_Statement_GlobalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
lua_Statement_GlobalFunction_Declaration.attributes={lua_Statement_GlobalFunction_Declaration_prefix, lua_Statement_GlobalFunction_Declaration_functionName}

# lua_Statement_Repeat class attributes and methods

# lua_Function class attributes and methods
lua_Function_parameters: Property = Property(name="parameters", type=StringType)
lua_Function_varArgs: Property = Property(name="varArgs", type=BooleanType)
lua_Function.attributes={lua_Function_parameters, lua_Function_varArgs}

# lua_Statement_LocalFunction_Declaration class attributes and methods
lua_Statement_LocalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
lua_Statement_LocalFunction_Declaration.attributes={lua_Statement_LocalFunction_Declaration_functionName}

# lua_Statement_If_Then_Else class attributes and methods

# lua_Statement_Local_Variable_Declaration class attributes and methods
lua_Statement_Local_Variable_Declaration_variableNames: Property = Property(name="variableNames", type=StringType)
lua_Statement_Local_Variable_Declaration.attributes={lua_Statement_Local_Variable_Declaration_variableNames}

# lua_Statement_If_Then_Else_ElseIfPart class attributes and methods

# lua_Statement_FunctioncallOrAssignment class attributes and methods

# Statement_FunctioncallOrAssignment class attributes and methods

# lua_Expression_VarArgs class attributes and methods

# lua_Expression_String class attributes and methods
lua_Expression_String_value: Property = Property(name="value", type=StringType)
lua_Expression_String.attributes={lua_Expression_String_value}

# lua_Expression_Function class attributes and methods

# lua_Expression_TableConstructor class attributes and methods

# lua_Field class attributes and methods

# lua_Functioncall_Arguments class attributes and methods

# lua_Field_AddEntryToTable_Brackets class attributes and methods

# Field class attributes and methods

# lua_Field_AddEntryToTable class attributes and methods
lua_Field_AddEntryToTable_key: Property = Property(name="key", type=StringType)
lua_Field_AddEntryToTable.attributes={lua_Field_AddEntryToTable_key}

# lua_Field_AppendEntryToTable class attributes and methods

# lua_LastStatement_ReturnWithValue class attributes and methods

# LastStatement_Return class attributes and methods

# lua_Statement_Assignment class attributes and methods

# lua_Expression_Nil class attributes and methods

# Expression class attributes and methods

# lua_Expression_True class attributes and methods

# lua_Expression_False class attributes and methods

# lua_Expression_Number class attributes and methods
lua_Expression_Number_value: Property = Property(name="value", type=FloatType)
lua_Expression_Number.attributes={lua_Expression_Number_value}

# lua_Statement_CallFunction class attributes and methods

# lua_Expression_Or class attributes and methods

# lua_Expression_And class attributes and methods

# lua_Expression_Larger class attributes and methods

# lua_Expression_Larger_Equal class attributes and methods

# lua_Expression_Smaller class attributes and methods

# lua_Statement_CallMemberFunction class attributes and methods
lua_Statement_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
lua_Statement_CallMemberFunction.attributes={lua_Statement_CallMemberFunction_memberFunctionName}

# lua_Expression_Smaller_Equal class attributes and methods

# lua_Expression_Equal class attributes and methods

# lua_Expression_Not_Equal class attributes and methods

# lua_Expression_Concatenation class attributes and methods

# lua_Expression_Plus class attributes and methods

# lua_Expression_Minus class attributes and methods

# lua_Expression_Multiplication class attributes and methods

# lua_Expression_Division class attributes and methods

# lua_Expression_Modulo class attributes and methods

# lua_Expression_Negate class attributes and methods

# lua_Expression_Length class attributes and methods

# lua_Expression_Invert class attributes and methods

# lua_Expression_CallMemberFunction class attributes and methods
lua_Expression_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
lua_Expression_CallMemberFunction.attributes={lua_Expression_CallMemberFunction_memberFunctionName}

# lua_Expression_CallFunction class attributes and methods

# lua_Expression_AccessArray class attributes and methods

# lua_Expression_AccessMember class attributes and methods
lua_Expression_AccessMember_memberName: Property = Property(name="memberName", type=StringType)
lua_Expression_AccessMember.attributes={lua_Expression_AccessMember_memberName}

# lua_Expression_VariableName class attributes and methods
lua_Expression_VariableName_variable: Property = Property(name="variable", type=StringType)
lua_Expression_VariableName.attributes={lua_Expression_VariableName_variable}

# lua_Expression_Exponentiation class attributes and methods

# Relationships
returnValue1: BinaryAssociation = BinaryAssociation(
    name="returnValue1",
    ends={
        Property(name="lua_LastStatement", type=lua_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Block2", type=lua_LastStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="lua_Block4", type=lua_Statement_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Block", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression5: BinaryAssociation = BinaryAssociation(
    name="expression5",
    ends={
        Property(name="lua_Expression", type=lua_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_While", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="lua_Statement", type=lua_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Block", type=lua_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startExpr30: BinaryAssociation = BinaryAssociation(
    name="startExpr30",
    ends={
        Property(name="lua_Expression31", type=lua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Numeric", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpr32: BinaryAssociation = BinaryAssociation(
    name="untilExpr32",
    ends={
        Property(name="lua_Expression34", type=lua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Numeric33", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stepExpr35: BinaryAssociation = BinaryAssociation(
    name="stepExpr35",
    ends={
        Property(name="lua_Expression37", type=lua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Numeric36", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block38: BinaryAssociation = BinaryAssociation(
    name="block38",
    ends={
        Property(name="lua_Block40", type=lua_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Numeric39", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions41: BinaryAssociation = BinaryAssociation(
    name="expressions41",
    ends={
        Property(name="lua_Expression42", type=lua_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Generic", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block43: BinaryAssociation = BinaryAssociation(
    name="block43",
    ends={
        Property(name="lua_Block45", type=lua_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_For_Generic44", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block6: BinaryAssociation = BinaryAssociation(
    name="block6",
    ends={
        Property(name="lua_Block8", type=lua_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_While7", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function46: BinaryAssociation = BinaryAssociation(
    name="function46",
    ends={
        Property(name="lua_Function", type=lua_Statement_GlobalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_GlobalFunction_Declaration", type=lua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block9: BinaryAssociation = BinaryAssociation(
    name="block9",
    ends={
        Property(name="lua_Block10", type=lua_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Repeat", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="lua_Expression13", type=lua_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Repeat12", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function47: BinaryAssociation = BinaryAssociation(
    name="function47",
    ends={
        Property(name="lua_Function48", type=lua_Statement_LocalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_LocalFunction_Declaration", type=lua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpression14: BinaryAssociation = BinaryAssociation(
    name="ifExpression14",
    ends={
        Property(name="lua_Expression15", type=lua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifBlock16: BinaryAssociation = BinaryAssociation(
    name="ifBlock16",
    ends={
        Property(name="lua_Block18", type=lua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else17", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue49: BinaryAssociation = BinaryAssociation(
    name="initialValue49",
    ends={
        Property(name="lua_Expression50", type=lua_Statement_Local_Variable_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Local_Variable_Declaration", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseIf19: BinaryAssociation = BinaryAssociation(
    name="elseIf19",
    ends={
        Property(name="lua_Statement_If_Then_Else_ElseIfPart", type=lua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else20", type=lua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBlock21: BinaryAssociation = BinaryAssociation(
    name="elseBlock21",
    ends={
        Property(name="lua_Block23", type=lua_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else22", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifExpression24: BinaryAssociation = BinaryAssociation(
    name="elseifExpression24",
    ends={
        Property(name="lua_Expression26", type=lua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else_ElseIfPart25", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifBlock27: BinaryAssociation = BinaryAssociation(
    name="elseifBlock27",
    ends={
        Property(name="lua_Block29", type=lua_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_If_Then_Else_ElseIfPart28", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function51: BinaryAssociation = BinaryAssociation(
    name="function51",
    ends={
        Property(name="lua_Function52", type=lua_Expression_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Function", type=lua_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields53: BinaryAssociation = BinaryAssociation(
    name="fields53",
    ends={
        Property(name="lua_Field", type=lua_Expression_TableConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_TableConstructor", type=lua_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body54: BinaryAssociation = BinaryAssociation(
    name="body54",
    ends={
        Property(name="lua_Block56", type=lua_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Function55", type=lua_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments57: BinaryAssociation = BinaryAssociation(
    name="arguments57",
    ends={
        Property(name="lua_Expression58", type=lua_Functioncall_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Functioncall_Arguments", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="lua_Expression61", type=lua_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Field60", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexExpression62: BinaryAssociation = BinaryAssociation(
    name="indexExpression62",
    ends={
        Property(name="lua_Expression63", type=lua_Field_AddEntryToTable_Brackets, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Field_AddEntryToTable_Brackets", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValues64: BinaryAssociation = BinaryAssociation(
    name="returnValues64",
    ends={
        Property(name="lua_Expression65", type=lua_LastStatement_ReturnWithValue, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_LastStatement_ReturnWithValue", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object71: BinaryAssociation = BinaryAssociation(
    name="object71",
    ends={
        Property(name="lua_Expression72", type=lua_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_CallMemberFunction", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments73: BinaryAssociation = BinaryAssociation(
    name="arguments73",
    ends={
        Property(name="lua_Functioncall_Arguments75", type=lua_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_CallMemberFunction74", type=lua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object76: BinaryAssociation = BinaryAssociation(
    name="object76",
    ends={
        Property(name="lua_Expression77", type=lua_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_CallFunction", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments78: BinaryAssociation = BinaryAssociation(
    name="arguments78",
    ends={
        Property(name="lua_Functioncall_Arguments80", type=lua_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_CallFunction79", type=lua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="lua_Expression82", type=lua_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Or", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right83: BinaryAssociation = BinaryAssociation(
    name="right83",
    ends={
        Property(name="lua_Expression85", type=lua_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Or84", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="lua_Expression87", type=lua_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_And", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right88: BinaryAssociation = BinaryAssociation(
    name="right88",
    ends={
        Property(name="lua_Expression90", type=lua_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_And89", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left91: BinaryAssociation = BinaryAssociation(
    name="left91",
    ends={
        Property(name="lua_Expression92", type=lua_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Larger", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right93: BinaryAssociation = BinaryAssociation(
    name="right93",
    ends={
        Property(name="lua_Expression95", type=lua_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Larger94", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left96: BinaryAssociation = BinaryAssociation(
    name="left96",
    ends={
        Property(name="lua_Expression97", type=lua_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Larger_Equal", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right98: BinaryAssociation = BinaryAssociation(
    name="right98",
    ends={
        Property(name="lua_Expression100", type=lua_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Larger_Equal99", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable66: BinaryAssociation = BinaryAssociation(
    name="variable66",
    ends={
        Property(name="lua_Expression67", type=lua_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Assignment", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values68: BinaryAssociation = BinaryAssociation(
    name="values68",
    ends={
        Property(name="lua_Expression70", type=lua_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Statement_Assignment69", type=lua_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right103: BinaryAssociation = BinaryAssociation(
    name="right103",
    ends={
        Property(name="lua_Expression_Smaller104", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="lua_Expression105", type=lua_Expression_Smaller, multiplicity=Multiplicity(1, 1))
    }
)
left106: BinaryAssociation = BinaryAssociation(
    name="left106",
    ends={
        Property(name="lua_Expression107", type=lua_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Smaller_Equal", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right108: BinaryAssociation = BinaryAssociation(
    name="right108",
    ends={
        Property(name="lua_Expression110", type=lua_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Smaller_Equal109", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left111: BinaryAssociation = BinaryAssociation(
    name="left111",
    ends={
        Property(name="lua_Expression112", type=lua_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Equal", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right113: BinaryAssociation = BinaryAssociation(
    name="right113",
    ends={
        Property(name="lua_Expression115", type=lua_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Equal114", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="lua_Expression117", type=lua_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Not_Equal", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="lua_Expression120", type=lua_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Not_Equal119", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="lua_Expression122", type=lua_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Concatenation", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="lua_Expression125", type=lua_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Concatenation124", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="lua_Expression127", type=lua_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Plus", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="lua_Expression130", type=lua_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Plus129", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left101: BinaryAssociation = BinaryAssociation(
    name="left101",
    ends={
        Property(name="lua_Expression102", type=lua_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Smaller", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="lua_Expression_Minus134", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="lua_Expression135", type=lua_Expression_Minus, multiplicity=Multiplicity(1, 1))
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="lua_Expression137", type=lua_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Multiplication", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="lua_Expression140", type=lua_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Multiplication139", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="lua_Expression142", type=lua_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Division", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="lua_Expression145", type=lua_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Division144", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="lua_Expression147", type=lua_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Modulo", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="lua_Expression150", type=lua_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Modulo149", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp151: BinaryAssociation = BinaryAssociation(
    name="exp151",
    ends={
        Property(name="lua_Expression152", type=lua_Expression_Negate, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Negate", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp153: BinaryAssociation = BinaryAssociation(
    name="exp153",
    ends={
        Property(name="lua_Expression154", type=lua_Expression_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Length", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="lua_Expression132", type=lua_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Minus", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left157: BinaryAssociation = BinaryAssociation(
    name="left157",
    ends={
        Property(name="lua_Expression158", type=lua_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Exponentiation", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right159: BinaryAssociation = BinaryAssociation(
    name="right159",
    ends={
        Property(name="lua_Expression161", type=lua_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Exponentiation160", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object162: BinaryAssociation = BinaryAssociation(
    name="object162",
    ends={
        Property(name="lua_Expression163", type=lua_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_CallMemberFunction", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments164: BinaryAssociation = BinaryAssociation(
    name="arguments164",
    ends={
        Property(name="lua_Functioncall_Arguments166", type=lua_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_CallMemberFunction165", type=lua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object167: BinaryAssociation = BinaryAssociation(
    name="object167",
    ends={
        Property(name="lua_Expression168", type=lua_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_CallFunction", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments169: BinaryAssociation = BinaryAssociation(
    name="arguments169",
    ends={
        Property(name="lua_Functioncall_Arguments171", type=lua_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_CallFunction170", type=lua_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array172: BinaryAssociation = BinaryAssociation(
    name="array172",
    ends={
        Property(name="lua_Expression173", type=lua_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_AccessArray", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index174: BinaryAssociation = BinaryAssociation(
    name="index174",
    ends={
        Property(name="lua_Expression176", type=lua_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_AccessArray175", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object177: BinaryAssociation = BinaryAssociation(
    name="object177",
    ends={
        Property(name="lua_Expression178", type=lua_Expression_AccessMember, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_AccessMember", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp155: BinaryAssociation = BinaryAssociation(
    name="exp155",
    ends={
        Property(name="lua_Expression156", type=lua_Expression_Invert, multiplicity=Multiplicity(1, 1)),
        Property(name="lua_Expression_Invert", type=lua_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_lua_LastStatement_Return_LastStatement = Generalization(general=LastStatement, specific=lua_LastStatement_Return)
gen_lua_LastStatement_Break_LastStatement = Generalization(general=LastStatement, specific=lua_LastStatement_Break)
gen_lua_Statement_Block_Statement = Generalization(general=Statement, specific=lua_Statement_Block)
gen_lua_Statement_While_Statement = Generalization(general=Statement, specific=lua_Statement_While)
gen_lua_Block_Chunk = Generalization(general=Chunk, specific=lua_Block)
gen_lua_Statement_For_Numeric_Statement = Generalization(general=Statement, specific=lua_Statement_For_Numeric)
gen_lua_Statement_For_Generic_Statement = Generalization(general=Statement, specific=lua_Statement_For_Generic)
gen_lua_Statement_GlobalFunction_Declaration_Statement = Generalization(general=Statement, specific=lua_Statement_GlobalFunction_Declaration)
gen_lua_Statement_Repeat_Statement = Generalization(general=Statement, specific=lua_Statement_Repeat)
gen_lua_Statement_LocalFunction_Declaration_Statement = Generalization(general=Statement, specific=lua_Statement_LocalFunction_Declaration)
gen_lua_Statement_If_Then_Else_Statement = Generalization(general=Statement, specific=lua_Statement_If_Then_Else)
gen_lua_Statement_Local_Variable_Declaration_Statement = Generalization(general=Statement, specific=lua_Statement_Local_Variable_Declaration)
gen_lua_Statement_FunctioncallOrAssignment_Statement = Generalization(general=Statement, specific=lua_Statement_FunctioncallOrAssignment)
gen_lua_Expression_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=lua_Expression)
gen_lua_Expression_VarArgs_Expression = Generalization(general=Expression, specific=lua_Expression_VarArgs)
gen_lua_Expression_String_Expression = Generalization(general=Expression, specific=lua_Expression_String)
gen_lua_Expression_Function_Expression = Generalization(general=Expression, specific=lua_Expression_Function)
gen_lua_Expression_TableConstructor_Expression = Generalization(general=Expression, specific=lua_Expression_TableConstructor)
gen_lua_Field_AddEntryToTable_Brackets_Field = Generalization(general=Field, specific=lua_Field_AddEntryToTable_Brackets)
gen_lua_Field_AddEntryToTable_Field = Generalization(general=Field, specific=lua_Field_AddEntryToTable)
gen_lua_Field_AppendEntryToTable_Field = Generalization(general=Field, specific=lua_Field_AppendEntryToTable)
gen_lua_LastStatement_ReturnWithValue_LastStatement_Return = Generalization(general=LastStatement_Return, specific=lua_LastStatement_ReturnWithValue)
gen_lua_Statement_Assignment_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=lua_Statement_Assignment)
gen_lua_Expression_Nil_Expression = Generalization(general=Expression, specific=lua_Expression_Nil)
gen_lua_Expression_True_Expression = Generalization(general=Expression, specific=lua_Expression_True)
gen_lua_Expression_False_Expression = Generalization(general=Expression, specific=lua_Expression_False)
gen_lua_Expression_Number_Expression = Generalization(general=Expression, specific=lua_Expression_Number)
gen_lua_Statement_CallFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=lua_Statement_CallFunction)
gen_lua_Expression_Or_Expression = Generalization(general=Expression, specific=lua_Expression_Or)
gen_lua_Expression_And_Expression = Generalization(general=Expression, specific=lua_Expression_And)
gen_lua_Expression_Larger_Expression = Generalization(general=Expression, specific=lua_Expression_Larger)
gen_lua_Expression_Larger_Equal_Expression = Generalization(general=Expression, specific=lua_Expression_Larger_Equal)
gen_lua_Expression_Smaller_Expression = Generalization(general=Expression, specific=lua_Expression_Smaller)
gen_lua_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=lua_Statement_CallMemberFunction)
gen_lua_Expression_Smaller_Equal_Expression = Generalization(general=Expression, specific=lua_Expression_Smaller_Equal)
gen_lua_Expression_Equal_Expression = Generalization(general=Expression, specific=lua_Expression_Equal)
gen_lua_Expression_Not_Equal_Expression = Generalization(general=Expression, specific=lua_Expression_Not_Equal)
gen_lua_Expression_Concatenation_Expression = Generalization(general=Expression, specific=lua_Expression_Concatenation)
gen_lua_Expression_Plus_Expression = Generalization(general=Expression, specific=lua_Expression_Plus)
gen_lua_Expression_Minus_Expression = Generalization(general=Expression, specific=lua_Expression_Minus)
gen_lua_Expression_Multiplication_Expression = Generalization(general=Expression, specific=lua_Expression_Multiplication)
gen_lua_Expression_Division_Expression = Generalization(general=Expression, specific=lua_Expression_Division)
gen_lua_Expression_Modulo_Expression = Generalization(general=Expression, specific=lua_Expression_Modulo)
gen_lua_Expression_Negate_Expression = Generalization(general=Expression, specific=lua_Expression_Negate)
gen_lua_Expression_Length_Expression = Generalization(general=Expression, specific=lua_Expression_Length)
gen_lua_Expression_Invert_Expression = Generalization(general=Expression, specific=lua_Expression_Invert)
gen_lua_Expression_CallMemberFunction_Expression = Generalization(general=Expression, specific=lua_Expression_CallMemberFunction)
gen_lua_Expression_CallFunction_Expression = Generalization(general=Expression, specific=lua_Expression_CallFunction)
gen_lua_Expression_AccessArray_Expression = Generalization(general=Expression, specific=lua_Expression_AccessArray)
gen_lua_Expression_AccessMember_Expression = Generalization(general=Expression, specific=lua_Expression_AccessMember)
gen_lua_Expression_VariableName_Expression = Generalization(general=Expression, specific=lua_Expression_VariableName)
gen_lua_Expression_Exponentiation_Expression = Generalization(general=Expression, specific=lua_Expression_Exponentiation)

# Domain Model
domain_model = DomainModel(
    name="lua",
    types={lua_LastStatement_Return, LastStatement, lua_LastStatement_Break, lua_Statement_Block, Statement, lua_Statement_While, lua_Expression, lua_Chunk, lua_Block, Chunk, lua_Statement, lua_LastStatement, lua_Statement_For_Numeric, lua_Statement_For_Generic, lua_Statement_GlobalFunction_Declaration, lua_Statement_Repeat, lua_Function, lua_Statement_LocalFunction_Declaration, lua_Statement_If_Then_Else, lua_Statement_Local_Variable_Declaration, lua_Statement_If_Then_Else_ElseIfPart, lua_Statement_FunctioncallOrAssignment, Statement_FunctioncallOrAssignment, lua_Expression_VarArgs, lua_Expression_String, lua_Expression_Function, lua_Expression_TableConstructor, lua_Field, lua_Functioncall_Arguments, lua_Field_AddEntryToTable_Brackets, Field, lua_Field_AddEntryToTable, lua_Field_AppendEntryToTable, lua_LastStatement_ReturnWithValue, LastStatement_Return, lua_Statement_Assignment, lua_Expression_Nil, Expression, lua_Expression_True, lua_Expression_False, lua_Expression_Number, lua_Statement_CallFunction, lua_Expression_Or, lua_Expression_And, lua_Expression_Larger, lua_Expression_Larger_Equal, lua_Expression_Smaller, lua_Statement_CallMemberFunction, lua_Expression_Smaller_Equal, lua_Expression_Equal, lua_Expression_Not_Equal, lua_Expression_Concatenation, lua_Expression_Plus, lua_Expression_Minus, lua_Expression_Multiplication, lua_Expression_Division, lua_Expression_Modulo, lua_Expression_Negate, lua_Expression_Length, lua_Expression_Invert, lua_Expression_CallMemberFunction, lua_Expression_CallFunction, lua_Expression_AccessArray, lua_Expression_AccessMember, lua_Expression_VariableName, lua_Expression_Exponentiation},
    associations={returnValue1, block3, expression5, statements0, startExpr30, untilExpr32, stepExpr35, block38, expressions41, block43, block6, function46, block9, expression11, function47, ifExpression14, ifBlock16, initialValue49, elseIf19, elseBlock21, elseifExpression24, elseifBlock27, function51, fields53, body54, arguments57, value59, indexExpression62, returnValues64, object71, arguments73, object76, arguments78, left81, right83, left86, right88, left91, right93, left96, right98, variable66, values68, right103, left106, right108, left111, right113, left116, right118, left121, right123, left126, right128, left101, right133, left136, right138, left141, right143, left146, right148, exp151, exp153, left131, left157, right159, object162, arguments164, object167, arguments169, array172, index174, object177, exp155},
    generalizations={gen_lua_LastStatement_Return_LastStatement, gen_lua_LastStatement_Break_LastStatement, gen_lua_Statement_Block_Statement, gen_lua_Statement_While_Statement, gen_lua_Block_Chunk, gen_lua_Statement_For_Numeric_Statement, gen_lua_Statement_For_Generic_Statement, gen_lua_Statement_GlobalFunction_Declaration_Statement, gen_lua_Statement_Repeat_Statement, gen_lua_Statement_LocalFunction_Declaration_Statement, gen_lua_Statement_If_Then_Else_Statement, gen_lua_Statement_Local_Variable_Declaration_Statement, gen_lua_Statement_FunctioncallOrAssignment_Statement, gen_lua_Expression_Statement_FunctioncallOrAssignment, gen_lua_Expression_VarArgs_Expression, gen_lua_Expression_String_Expression, gen_lua_Expression_Function_Expression, gen_lua_Expression_TableConstructor_Expression, gen_lua_Field_AddEntryToTable_Brackets_Field, gen_lua_Field_AddEntryToTable_Field, gen_lua_Field_AppendEntryToTable_Field, gen_lua_LastStatement_ReturnWithValue_LastStatement_Return, gen_lua_Statement_Assignment_Statement_FunctioncallOrAssignment, gen_lua_Expression_Nil_Expression, gen_lua_Expression_True_Expression, gen_lua_Expression_False_Expression, gen_lua_Expression_Number_Expression, gen_lua_Statement_CallFunction_Statement_FunctioncallOrAssignment, gen_lua_Expression_Or_Expression, gen_lua_Expression_And_Expression, gen_lua_Expression_Larger_Expression, gen_lua_Expression_Larger_Equal_Expression, gen_lua_Expression_Smaller_Expression, gen_lua_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment, gen_lua_Expression_Smaller_Equal_Expression, gen_lua_Expression_Equal_Expression, gen_lua_Expression_Not_Equal_Expression, gen_lua_Expression_Concatenation_Expression, gen_lua_Expression_Plus_Expression, gen_lua_Expression_Minus_Expression, gen_lua_Expression_Multiplication_Expression, gen_lua_Expression_Division_Expression, gen_lua_Expression_Modulo_Expression, gen_lua_Expression_Negate_Expression, gen_lua_Expression_Length_Expression, gen_lua_Expression_Invert_Expression, gen_lua_Expression_CallMemberFunction_Expression, gen_lua_Expression_CallFunction_Expression, gen_lua_Expression_AccessArray_Expression, gen_lua_Expression_AccessMember_Expression, gen_lua_Expression_VariableName_Expression, gen_lua_Expression_Exponentiation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)