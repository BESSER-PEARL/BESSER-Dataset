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
EBaseType: Enumeration = Enumeration(
    name="EBaseType",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="CHAR")
    }
)

EOneOperator: Enumeration = Enumeration(
    name="EOneOperator",
    literals={
            EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="NOT")
    }
)

ETwoOperator: Enumeration = Enumeration(
    name="ETwoOperator",
    literals={
            EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DEVIDE"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="NOT_EQUAL"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LT")
    }
)

# Classes
dinkiemodel_FunctionDecl = Class(name="dinkiemodel::FunctionDecl")
dinkiemodel_Main = Class(name="dinkiemodel::Main")
dinkiemodel_Statement = Class(name="dinkiemodel::Statement", is_abstract=True)
dinkiemodel_Program = Class(name="dinkiemodel::Program")
dinkiemodel_ReadStatement = Class(name="dinkiemodel::ReadStatement")
dinkiemodel_WriteStatement = Class(name="dinkiemodel::WriteStatement")
dinkiemodel_Argument = Class(name="dinkiemodel::Argument")
dinkiemodel_Type = Class(name="dinkiemodel::Type", is_abstract=True)
dinkiemodel_Declaration = Class(name="dinkiemodel::Declaration")
Statement = Class(name="Statement")
dinkiemodel_BaseType = Class(name="dinkiemodel::BaseType")
dinkiemodel_Expression = Class(name="dinkiemodel::Expression", is_abstract=True)
Type = Class(name="Type")
dinkiemodel_ArrayType = Class(name="dinkiemodel::ArrayType")
dinkiemodel_EmptyArrayDecl = Class(name="dinkiemodel::EmptyArrayDecl")
dinkiemodel_While = Class(name="dinkiemodel::While")
dinkiemodel_IfOne = Class(name="dinkiemodel::IfOne")
dinkiemodel_IfTwo = Class(name="dinkiemodel::IfTwo")
dinkiemodel_Assign = Class(name="dinkiemodel::Assign")
dinkiemodel_FilledArrayDecl = Class(name="dinkiemodel::FilledArrayDecl")
dinkiemodel_StringArrayDecl = Class(name="dinkiemodel::StringArrayDecl")
dinkiemodel_ArrayAssign = Class(name="dinkiemodel::ArrayAssign")
dinkiemodel_Number = Class(name="dinkiemodel::Number")
Expression = Class(name="Expression")
dinkiemodel_BoolVal = Class(name="dinkiemodel::BoolVal")
dinkiemodel_Character = Class(name="dinkiemodel::Character")
dinkiemodel_Parallel = Class(name="dinkiemodel::Parallel")
dinkiemodel_Sync = Class(name="dinkiemodel::Sync")
dinkiemodel_Return = Class(name="dinkiemodel::Return")
dinkiemodel_ThreadID = Class(name="dinkiemodel::ThreadID")
dinkiemodel_VariableExpr = Class(name="dinkiemodel::VariableExpr")
dinkiemodel_OneOperator = Class(name="dinkiemodel::OneOperator")
dinkiemodel_TwoOperator = Class(name="dinkiemodel::TwoOperator")
dinkiemodel_BracketExpr = Class(name="dinkiemodel::BracketExpr")
dinkiemodel_ArrayExpr = Class(name="dinkiemodel::ArrayExpr")
dinkiemodel_FuncExpr = Class(name="dinkiemodel::FuncExpr")

# dinkiemodel_FunctionDecl class attributes and methods
dinkiemodel_FunctionDecl_name: Property = Property(name="name", type=StringType)
dinkiemodel_FunctionDecl.attributes={dinkiemodel_FunctionDecl_name}

# dinkiemodel_Main class attributes and methods

# dinkiemodel_Statement class attributes and methods

# dinkiemodel_Program class attributes and methods

# dinkiemodel_ReadStatement class attributes and methods
dinkiemodel_ReadStatement_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_ReadStatement.attributes={dinkiemodel_ReadStatement_varName}

# dinkiemodel_WriteStatement class attributes and methods

# dinkiemodel_Argument class attributes and methods
dinkiemodel_Argument_name: Property = Property(name="name", type=StringType)
dinkiemodel_Argument.attributes={dinkiemodel_Argument_name}

# dinkiemodel_Type class attributes and methods

# dinkiemodel_Declaration class attributes and methods
dinkiemodel_Declaration_global: Property = Property(name="global", type=BooleanType)
dinkiemodel_Declaration_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_Declaration.attributes={dinkiemodel_Declaration_global, dinkiemodel_Declaration_varName}

# Statement class attributes and methods

# dinkiemodel_BaseType class attributes and methods
dinkiemodel_BaseType_type: Property = Property(name="type", type=StringType)
dinkiemodel_BaseType.attributes={dinkiemodel_BaseType_type}

# dinkiemodel_Expression class attributes and methods

# Type class attributes and methods

# dinkiemodel_ArrayType class attributes and methods
dinkiemodel_ArrayType_arrayType: Property = Property(name="arrayType", type=StringType)
dinkiemodel_ArrayType.attributes={dinkiemodel_ArrayType_arrayType}

# dinkiemodel_EmptyArrayDecl class attributes and methods
dinkiemodel_EmptyArrayDecl_size: Property = Property(name="size", type=IntegerType)
dinkiemodel_EmptyArrayDecl_global: Property = Property(name="global", type=BooleanType)
dinkiemodel_EmptyArrayDecl_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_EmptyArrayDecl.attributes={dinkiemodel_EmptyArrayDecl_varName, dinkiemodel_EmptyArrayDecl_global, dinkiemodel_EmptyArrayDecl_size}

# dinkiemodel_While class attributes and methods

# dinkiemodel_IfOne class attributes and methods

# dinkiemodel_IfTwo class attributes and methods

# dinkiemodel_Assign class attributes and methods
dinkiemodel_Assign_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_Assign.attributes={dinkiemodel_Assign_varName}

# dinkiemodel_FilledArrayDecl class attributes and methods
dinkiemodel_FilledArrayDecl_global: Property = Property(name="global", type=BooleanType)
dinkiemodel_FilledArrayDecl_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_FilledArrayDecl.attributes={dinkiemodel_FilledArrayDecl_global, dinkiemodel_FilledArrayDecl_varName}

# dinkiemodel_StringArrayDecl class attributes and methods
dinkiemodel_StringArrayDecl_global: Property = Property(name="global", type=BooleanType)
dinkiemodel_StringArrayDecl_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_StringArrayDecl_content: Property = Property(name="content", type=StringType)
dinkiemodel_StringArrayDecl.attributes={dinkiemodel_StringArrayDecl_content, dinkiemodel_StringArrayDecl_global, dinkiemodel_StringArrayDecl_varName}

# dinkiemodel_ArrayAssign class attributes and methods
dinkiemodel_ArrayAssign_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_ArrayAssign.attributes={dinkiemodel_ArrayAssign_varName}

# dinkiemodel_Number class attributes and methods
dinkiemodel_Number_value: Property = Property(name="value", type=IntegerType)
dinkiemodel_Number.attributes={dinkiemodel_Number_value}

# Expression class attributes and methods

# dinkiemodel_BoolVal class attributes and methods
dinkiemodel_BoolVal_value: Property = Property(name="value", type=BooleanType)
dinkiemodel_BoolVal.attributes={dinkiemodel_BoolVal_value}

# dinkiemodel_Character class attributes and methods
dinkiemodel_Character_value: Property = Property(name="value", type=StringType)
dinkiemodel_Character.attributes={dinkiemodel_Character_value}

# dinkiemodel_Parallel class attributes and methods
dinkiemodel_Parallel_nrOfThreads: Property = Property(name="nrOfThreads", type=IntegerType)
dinkiemodel_Parallel.attributes={dinkiemodel_Parallel_nrOfThreads}

# dinkiemodel_Sync class attributes and methods
dinkiemodel_Sync_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_Sync.attributes={dinkiemodel_Sync_varName}

# dinkiemodel_Return class attributes and methods

# dinkiemodel_ThreadID class attributes and methods

# dinkiemodel_VariableExpr class attributes and methods
dinkiemodel_VariableExpr_name: Property = Property(name="name", type=StringType)
dinkiemodel_VariableExpr.attributes={dinkiemodel_VariableExpr_name}

# dinkiemodel_OneOperator class attributes and methods
dinkiemodel_OneOperator_operator: Property = Property(name="operator", type=StringType)
dinkiemodel_OneOperator.attributes={dinkiemodel_OneOperator_operator}

# dinkiemodel_TwoOperator class attributes and methods
dinkiemodel_TwoOperator_operator: Property = Property(name="operator", type=StringType)
dinkiemodel_TwoOperator.attributes={dinkiemodel_TwoOperator_operator}

# dinkiemodel_BracketExpr class attributes and methods

# dinkiemodel_ArrayExpr class attributes and methods
dinkiemodel_ArrayExpr_varName: Property = Property(name="varName", type=StringType)
dinkiemodel_ArrayExpr.attributes={dinkiemodel_ArrayExpr_varName}

# dinkiemodel_FuncExpr class attributes and methods
dinkiemodel_FuncExpr_funcName: Property = Property(name="funcName", type=StringType)
dinkiemodel_FuncExpr.attributes={dinkiemodel_FuncExpr_funcName}

# Relationships
functions0: BinaryAssociation = BinaryAssociation(
    name="functions0",
    ends={
        Property(name="dinkiemodel_FunctionDecl", type=dinkiemodel_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Program", type=dinkiemodel_FunctionDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainFunc1: BinaryAssociation = BinaryAssociation(
    name="mainFunc1",
    ends={
        Property(name="dinkiemodel_Main", type=dinkiemodel_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Program2", type=dinkiemodel_Main, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="dinkiemodel_Statement", type=dinkiemodel_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Main4", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements5: BinaryAssociation = BinaryAssociation(
    name="statements5",
    ends={
        Property(name="dinkiemodel_Statement7", type=dinkiemodel_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FunctionDecl6", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arraytype15: BinaryAssociation = BinaryAssociation(
    name="arraytype15",
    ends={
        Property(name="dinkiemodel_ArrayType", type=dinkiemodel_EmptyArrayDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_EmptyArrayDecl", type=dinkiemodel_ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="dinkiemodel_BaseType17", type=dinkiemodel_ReadStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_ReadStatement", type=dinkiemodel_BaseType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="dinkiemodel_Type19", type=dinkiemodel_WriteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_WriteStatement", type=dinkiemodel_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="dinkiemodel_Expression22", type=dinkiemodel_WriteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_WriteStatement21", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments8: BinaryAssociation = BinaryAssociation(
    name="arguments8",
    ends={
        Property(name="dinkiemodel_Argument", type=dinkiemodel_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FunctionDecl9", type=dinkiemodel_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="dinkiemodel_Type", type=dinkiemodel_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FunctionDecl11", type=dinkiemodel_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="dinkiemodel_BaseType", type=dinkiemodel_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Declaration", type=dinkiemodel_BaseType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="dinkiemodel_Expression", type=dinkiemodel_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Declaration14", type=dinkiemodel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression35: BinaryAssociation = BinaryAssociation(
    name="expression35",
    ends={
        Property(name="dinkiemodel_Expression36", type=dinkiemodel_While, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_While", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements37: BinaryAssociation = BinaryAssociation(
    name="statements37",
    ends={
        Property(name="dinkiemodel_Statement39", type=dinkiemodel_While, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_While38", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="dinkiemodel_Expression41", type=dinkiemodel_IfOne, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_IfOne", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements42: BinaryAssociation = BinaryAssociation(
    name="statements42",
    ends={
        Property(name="dinkiemodel_Statement44", type=dinkiemodel_IfOne, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_IfOne43", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression23: BinaryAssociation = BinaryAssociation(
    name="expression23",
    ends={
        Property(name="dinkiemodel_Expression24", type=dinkiemodel_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Assign", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arraytype25: BinaryAssociation = BinaryAssociation(
    name="arraytype25",
    ends={
        Property(name="dinkiemodel_ArrayType26", type=dinkiemodel_FilledArrayDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FilledArrayDecl", type=dinkiemodel_ArrayType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="dinkiemodel_Expression29", type=dinkiemodel_FilledArrayDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FilledArrayDecl28", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
index30: BinaryAssociation = BinaryAssociation(
    name="index30",
    ends={
        Property(name="dinkiemodel_Expression31", type=dinkiemodel_ArrayAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_ArrayAssign", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression32: BinaryAssociation = BinaryAssociation(
    name="expression32",
    ends={
        Property(name="dinkiemodel_Expression34", type=dinkiemodel_ArrayAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_ArrayAssign33", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStats45: BinaryAssociation = BinaryAssociation(
    name="thenStats45",
    ends={
        Property(name="dinkiemodel_Statement46", type=dinkiemodel_IfTwo, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_IfTwo", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression47: BinaryAssociation = BinaryAssociation(
    name="expression47",
    ends={
        Property(name="dinkiemodel_Expression49", type=dinkiemodel_IfTwo, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_IfTwo48", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStats50: BinaryAssociation = BinaryAssociation(
    name="elseStats50",
    ends={
        Property(name="dinkiemodel_Statement52", type=dinkiemodel_IfTwo, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_IfTwo51", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements53: BinaryAssociation = BinaryAssociation(
    name="statements53",
    ends={
        Property(name="dinkiemodel_Statement54", type=dinkiemodel_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Parallel", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements55: BinaryAssociation = BinaryAssociation(
    name="statements55",
    ends={
        Property(name="dinkiemodel_Statement56", type=dinkiemodel_Sync, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Sync", type=dinkiemodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression57: BinaryAssociation = BinaryAssociation(
    name="expression57",
    ends={
        Property(name="dinkiemodel_Expression58", type=dinkiemodel_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Return", type=dinkiemodel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type72: BinaryAssociation = BinaryAssociation(
    name="type72",
    ends={
        Property(name="dinkiemodel_Type74", type=dinkiemodel_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_Argument73", type=dinkiemodel_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression59: BinaryAssociation = BinaryAssociation(
    name="expression59",
    ends={
        Property(name="dinkiemodel_Expression60", type=dinkiemodel_OneOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_OneOperator", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExpr61: BinaryAssociation = BinaryAssociation(
    name="leftExpr61",
    ends={
        Property(name="dinkiemodel_Expression62", type=dinkiemodel_TwoOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_TwoOperator", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExpr63: BinaryAssociation = BinaryAssociation(
    name="rightExpr63",
    ends={
        Property(name="dinkiemodel_Expression65", type=dinkiemodel_TwoOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_TwoOperator64", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression66: BinaryAssociation = BinaryAssociation(
    name="expression66",
    ends={
        Property(name="dinkiemodel_Expression67", type=dinkiemodel_BracketExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_BracketExpr", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index68: BinaryAssociation = BinaryAssociation(
    name="index68",
    ends={
        Property(name="dinkiemodel_Expression69", type=dinkiemodel_ArrayExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_ArrayExpr", type=dinkiemodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments70: BinaryAssociation = BinaryAssociation(
    name="arguments70",
    ends={
        Property(name="dinkiemodel_Expression71", type=dinkiemodel_FuncExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dinkiemodel_FuncExpr", type=dinkiemodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dinkiemodel_ReadStatement_Statement = Generalization(general=Statement, specific=dinkiemodel_ReadStatement)
gen_dinkiemodel_WriteStatement_Statement = Generalization(general=Statement, specific=dinkiemodel_WriteStatement)
gen_dinkiemodel_Declaration_Statement = Generalization(general=Statement, specific=dinkiemodel_Declaration)
gen_dinkiemodel_BaseType_Type = Generalization(general=Type, specific=dinkiemodel_BaseType)
gen_dinkiemodel_ArrayType_Type = Generalization(general=Type, specific=dinkiemodel_ArrayType)
gen_dinkiemodel_EmptyArrayDecl_Statement = Generalization(general=Statement, specific=dinkiemodel_EmptyArrayDecl)
gen_dinkiemodel_While_Statement = Generalization(general=Statement, specific=dinkiemodel_While)
gen_dinkiemodel_IfOne_Statement = Generalization(general=Statement, specific=dinkiemodel_IfOne)
gen_dinkiemodel_Assign_Statement = Generalization(general=Statement, specific=dinkiemodel_Assign)
gen_dinkiemodel_FilledArrayDecl_Statement = Generalization(general=Statement, specific=dinkiemodel_FilledArrayDecl)
gen_dinkiemodel_StringArrayDecl_Statement = Generalization(general=Statement, specific=dinkiemodel_StringArrayDecl)
gen_dinkiemodel_ArrayAssign_Statement = Generalization(general=Statement, specific=dinkiemodel_ArrayAssign)
gen_dinkiemodel_Number_Expression = Generalization(general=Expression, specific=dinkiemodel_Number)
gen_dinkiemodel_BoolVal_Expression = Generalization(general=Expression, specific=dinkiemodel_BoolVal)
gen_dinkiemodel_Character_Expression = Generalization(general=Expression, specific=dinkiemodel_Character)
gen_dinkiemodel_IfTwo_Statement = Generalization(general=Statement, specific=dinkiemodel_IfTwo)
gen_dinkiemodel_Parallel_Statement = Generalization(general=Statement, specific=dinkiemodel_Parallel)
gen_dinkiemodel_Sync_Statement = Generalization(general=Statement, specific=dinkiemodel_Sync)
gen_dinkiemodel_Return_Statement = Generalization(general=Statement, specific=dinkiemodel_Return)
gen_dinkiemodel_ThreadID_Expression = Generalization(general=Expression, specific=dinkiemodel_ThreadID)
gen_dinkiemodel_VariableExpr_Expression = Generalization(general=Expression, specific=dinkiemodel_VariableExpr)
gen_dinkiemodel_OneOperator_Expression = Generalization(general=Expression, specific=dinkiemodel_OneOperator)
gen_dinkiemodel_TwoOperator_Expression = Generalization(general=Expression, specific=dinkiemodel_TwoOperator)
gen_dinkiemodel_BracketExpr_Expression = Generalization(general=Expression, specific=dinkiemodel_BracketExpr)
gen_dinkiemodel_ArrayExpr_Expression = Generalization(general=Expression, specific=dinkiemodel_ArrayExpr)
gen_dinkiemodel_FuncExpr_Expression = Generalization(general=Expression, specific=dinkiemodel_FuncExpr)
gen_dinkiemodel_FuncExpr_Statement = Generalization(general=Statement, specific=dinkiemodel_FuncExpr)

# Domain Model
domain_model = DomainModel(
    name="dinkiemodel",
    types={dinkiemodel_FunctionDecl, dinkiemodel_Main, dinkiemodel_Statement, dinkiemodel_Program, dinkiemodel_ReadStatement, dinkiemodel_WriteStatement, dinkiemodel_Argument, dinkiemodel_Type, dinkiemodel_Declaration, Statement, dinkiemodel_BaseType, dinkiemodel_Expression, Type, dinkiemodel_ArrayType, dinkiemodel_EmptyArrayDecl, dinkiemodel_While, dinkiemodel_IfOne, dinkiemodel_IfTwo, dinkiemodel_Assign, dinkiemodel_FilledArrayDecl, dinkiemodel_StringArrayDecl, dinkiemodel_ArrayAssign, dinkiemodel_Number, Expression, dinkiemodel_BoolVal, dinkiemodel_Character, dinkiemodel_Parallel, dinkiemodel_Sync, dinkiemodel_Return, dinkiemodel_ThreadID, dinkiemodel_VariableExpr, dinkiemodel_OneOperator, dinkiemodel_TwoOperator, dinkiemodel_BracketExpr, dinkiemodel_ArrayExpr, dinkiemodel_FuncExpr, EBaseType, EOneOperator, ETwoOperator},
    associations={functions0, mainFunc1, statements3, statements5, arraytype15, type16, type18, expression20, arguments8, type10, type12, expression13, expression35, statements37, expression40, statements42, expression23, arraytype25, expression27, index30, expression32, thenStats45, expression47, elseStats50, statements53, statements55, expression57, type72, expression59, leftExpr61, rightExpr63, expression66, index68, arguments70},
    generalizations={gen_dinkiemodel_ReadStatement_Statement, gen_dinkiemodel_WriteStatement_Statement, gen_dinkiemodel_Declaration_Statement, gen_dinkiemodel_BaseType_Type, gen_dinkiemodel_ArrayType_Type, gen_dinkiemodel_EmptyArrayDecl_Statement, gen_dinkiemodel_While_Statement, gen_dinkiemodel_IfOne_Statement, gen_dinkiemodel_Assign_Statement, gen_dinkiemodel_FilledArrayDecl_Statement, gen_dinkiemodel_StringArrayDecl_Statement, gen_dinkiemodel_ArrayAssign_Statement, gen_dinkiemodel_Number_Expression, gen_dinkiemodel_BoolVal_Expression, gen_dinkiemodel_Character_Expression, gen_dinkiemodel_IfTwo_Statement, gen_dinkiemodel_Parallel_Statement, gen_dinkiemodel_Sync_Statement, gen_dinkiemodel_Return_Statement, gen_dinkiemodel_ThreadID_Expression, gen_dinkiemodel_VariableExpr_Expression, gen_dinkiemodel_OneOperator_Expression, gen_dinkiemodel_TwoOperator_Expression, gen_dinkiemodel_BracketExpr_Expression, gen_dinkiemodel_ArrayExpr_Expression, gen_dinkiemodel_FuncExpr_Expression, gen_dinkiemodel_FuncExpr_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)