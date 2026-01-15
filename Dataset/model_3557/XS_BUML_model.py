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
xs_GlobalVarDeclaration = Class(name="xs::GlobalVarDeclaration")
xs_ParameterDeclaration = Class(name="xs::ParameterDeclaration")
xs_ForVarDeclaration = Class(name="xs::ForVarDeclaration")
xs_FunctionDeclaration = Class(name="xs::FunctionDeclaration")
xs_Block = Class(name="xs::Block")
xs_RuleDeclaration = Class(name="xs::RuleDeclaration")
xs_Program = Class(name="xs::Program")
xs_Declaration = Class(name="xs::Declaration")
xs_IncludeDeclaration = Class(name="xs::IncludeDeclaration")
Declaration = Class(name="Declaration")
xs_VarDeclaration = Class(name="xs::VarDeclaration")
xs_Expression = Class(name="xs::Expression")
xs_LocalVarDeclaration = Class(name="xs::LocalVarDeclaration")
VarDeclaration = Class(name="VarDeclaration")
Statement = Class(name="Statement")
xs_Type = Class(name="xs::Type")
xs_Var = Class(name="xs::Var")
Expression = Class(name="Expression")
xs_Literal = Class(name="xs::Literal")
xs_PostfixStatement = Class(name="xs::PostfixStatement")
xs_IfElseStatement = Class(name="xs::IfElseStatement")
xs_Statement = Class(name="xs::Statement")
xs_SwitchCase = Class(name="xs::SwitchCase")
xs_SwitchDefault = Class(name="xs::SwitchDefault")
xs_ForStatement = Class(name="xs::ForStatement")
xs_SwitchStatement = Class(name="xs::SwitchStatement")
xs_ReturnStatement = Class(name="xs::ReturnStatement")
xs_ContinueStatement = Class(name="xs::ContinueStatement")
xs_BreakStatement = Class(name="xs::BreakStatement")
xs_WhileStatement = Class(name="xs::WhileStatement")
xs_Assign = Class(name="xs::Assign")
xs_OrExpression = Class(name="xs::OrExpression")
xs_AndExpression = Class(name="xs::AndExpression")
xs_EqualsExpression = Class(name="xs::EqualsExpression")
xs_ComparisonExpression = Class(name="xs::ComparisonExpression")
xs_Term = Class(name="xs::Term")
xs_Factor = Class(name="xs::Factor")
xs_Call = Class(name="xs::Call")
xs_IntType = Class(name="xs::IntType")
Type = Class(name="Type")
xs_FloatType = Class(name="xs::FloatType")
xs_BoolType = Class(name="xs::BoolType")
xs_LiteralString = Class(name="xs::LiteralString")
Literal = Class(name="Literal")
xs_LiteralInt = Class(name="xs::LiteralInt")
xs_LiteralFloat = Class(name="xs::LiteralFloat")
xs_LiteralBool = Class(name="xs::LiteralBool")
xs_VectorLiteral = Class(name="xs::VectorLiteral")
xs_VectorType = Class(name="xs::VectorType")
xs_StringType = Class(name="xs::StringType")
xs_VoidType = Class(name="xs::VoidType")

# xs_GlobalVarDeclaration class attributes and methods
xs_GlobalVarDeclaration_const: Property = Property(name="const", type=BooleanType)
xs_GlobalVarDeclaration_extern: Property = Property(name="extern", type=BooleanType)
xs_GlobalVarDeclaration.attributes={xs_GlobalVarDeclaration_const, xs_GlobalVarDeclaration_extern}

# xs_ParameterDeclaration class attributes and methods

# xs_ForVarDeclaration class attributes and methods

# xs_FunctionDeclaration class attributes and methods
xs_FunctionDeclaration_mutable: Property = Property(name="mutable", type=BooleanType)
xs_FunctionDeclaration_name: Property = Property(name="name", type=StringType)
xs_FunctionDeclaration.attributes={xs_FunctionDeclaration_name, xs_FunctionDeclaration_mutable}

# xs_Block class attributes and methods

# xs_RuleDeclaration class attributes and methods
xs_RuleDeclaration_name: Property = Property(name="name", type=StringType)
xs_RuleDeclaration_active: Property = Property(name="active", type=BooleanType)
xs_RuleDeclaration_runImmediately: Property = Property(name="runImmediately", type=BooleanType)
xs_RuleDeclaration_highFrequency: Property = Property(name="highFrequency", type=BooleanType)
xs_RuleDeclaration_group: Property = Property(name="group", type=StringType)
xs_RuleDeclaration_minInterval: Property = Property(name="minInterval", type=IntegerType)
xs_RuleDeclaration_maxInterval: Property = Property(name="maxInterval", type=IntegerType)
xs_RuleDeclaration_priority: Property = Property(name="priority", type=IntegerType)
xs_RuleDeclaration.attributes={xs_RuleDeclaration_name, xs_RuleDeclaration_minInterval, xs_RuleDeclaration_maxInterval, xs_RuleDeclaration_group, xs_RuleDeclaration_highFrequency, xs_RuleDeclaration_priority, xs_RuleDeclaration_runImmediately, xs_RuleDeclaration_active}

# xs_Program class attributes and methods

# xs_Declaration class attributes and methods

# xs_IncludeDeclaration class attributes and methods
xs_IncludeDeclaration_filePath: Property = Property(name="filePath", type=StringType)
xs_IncludeDeclaration.attributes={xs_IncludeDeclaration_filePath}

# Declaration class attributes and methods

# xs_VarDeclaration class attributes and methods
xs_VarDeclaration_name: Property = Property(name="name", type=StringType)
xs_VarDeclaration.attributes={xs_VarDeclaration_name}

# xs_Expression class attributes and methods

# xs_LocalVarDeclaration class attributes and methods

# VarDeclaration class attributes and methods

# Statement class attributes and methods

# xs_Type class attributes and methods

# xs_Var class attributes and methods

# Expression class attributes and methods

# xs_Literal class attributes and methods

# xs_PostfixStatement class attributes and methods
xs_PostfixStatement_op: Property = Property(name="op", type=StringType)
xs_PostfixStatement.attributes={xs_PostfixStatement_op}

# xs_IfElseStatement class attributes and methods

# xs_Statement class attributes and methods

# xs_SwitchCase class attributes and methods

# xs_SwitchDefault class attributes and methods

# xs_ForStatement class attributes and methods
xs_ForStatement_op: Property = Property(name="op", type=StringType)
xs_ForStatement.attributes={xs_ForStatement_op}

# xs_SwitchStatement class attributes and methods

# xs_ReturnStatement class attributes and methods

# xs_ContinueStatement class attributes and methods

# xs_BreakStatement class attributes and methods

# xs_WhileStatement class attributes and methods

# xs_Assign class attributes and methods

# xs_OrExpression class attributes and methods
xs_OrExpression_op: Property = Property(name="op", type=StringType)
xs_OrExpression.attributes={xs_OrExpression_op}

# xs_AndExpression class attributes and methods
xs_AndExpression_op: Property = Property(name="op", type=StringType)
xs_AndExpression.attributes={xs_AndExpression_op}

# xs_EqualsExpression class attributes and methods
xs_EqualsExpression_op: Property = Property(name="op", type=StringType)
xs_EqualsExpression.attributes={xs_EqualsExpression_op}

# xs_ComparisonExpression class attributes and methods
xs_ComparisonExpression_op: Property = Property(name="op", type=StringType)
xs_ComparisonExpression.attributes={xs_ComparisonExpression_op}

# xs_Term class attributes and methods
xs_Term_op: Property = Property(name="op", type=StringType)
xs_Term.attributes={xs_Term_op}

# xs_Factor class attributes and methods
xs_Factor_op: Property = Property(name="op", type=StringType)
xs_Factor.attributes={xs_Factor_op}

# xs_Call class attributes and methods

# xs_IntType class attributes and methods

# Type class attributes and methods

# xs_FloatType class attributes and methods

# xs_BoolType class attributes and methods

# xs_LiteralString class attributes and methods
xs_LiteralString_value: Property = Property(name="value", type=StringType)
xs_LiteralString.attributes={xs_LiteralString_value}

# Literal class attributes and methods

# xs_LiteralInt class attributes and methods
xs_LiteralInt_value: Property = Property(name="value", type=IntegerType)
xs_LiteralInt.attributes={xs_LiteralInt_value}

# xs_LiteralFloat class attributes and methods
xs_LiteralFloat_value: Property = Property(name="value", type=FloatType)
xs_LiteralFloat.attributes={xs_LiteralFloat_value}

# xs_LiteralBool class attributes and methods
xs_LiteralBool_value: Property = Property(name="value", type=BooleanType)
xs_LiteralBool.attributes={xs_LiteralBool_value}

# xs_VectorLiteral class attributes and methods

# xs_VectorType class attributes and methods

# xs_StringType class attributes and methods

# xs_VoidType class attributes and methods

# Relationships
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="xs_Type4", type=xs_GlobalVarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_GlobalVarDeclaration", type=xs_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="xs_Type6", type=xs_ParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ParameterDeclaration", type=xs_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="xs_Type8", type=xs_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_FunctionDeclaration", type=xs_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="xs_ParameterDeclaration11", type=xs_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_FunctionDeclaration10", type=xs_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="xs_Block", type=xs_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_FunctionDeclaration13", type=xs_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="xs_Declaration", type=xs_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Program", type=xs_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="xs_Expression", type=xs_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_VarDeclaration", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="xs_Type", type=xs_LocalVarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_LocalVarDeclaration", type=xs_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration25: BinaryAssociation = BinaryAssociation(
    name="declaration25",
    ends={
        Property(name="xs_VarDeclaration26", type=xs_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Var", type=xs_VarDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
var27: BinaryAssociation = BinaryAssociation(
    name="var27",
    ends={
        Property(name="xs_VarDeclaration28", type=xs_PostfixStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_PostfixStatement", type=xs_VarDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="xs_Expression30", type=xs_IfElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_IfElseStatement", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body14: BinaryAssociation = BinaryAssociation(
    name="body14",
    ends={
        Property(name="xs_Block15", type=xs_RuleDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_RuleDeclaration", type=xs_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents16: BinaryAssociation = BinaryAssociation(
    name="contents16",
    ends={
        Property(name="xs_Statement", type=xs_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Block17", type=xs_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="xs_Expression19", type=xs_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchCase", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement20: BinaryAssociation = BinaryAssociation(
    name="statement20",
    ends={
        Property(name="xs_Statement22", type=xs_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchCase21", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement23: BinaryAssociation = BinaryAssociation(
    name="statement23",
    ends={
        Property(name="xs_Statement24", type=xs_SwitchDefault, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchDefault", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement39: BinaryAssociation = BinaryAssociation(
    name="statement39",
    ends={
        Property(name="xs_WhileStatement40", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="xs_Statement41", type=xs_WhileStatement, multiplicity=Multiplicity(1, 1))
    }
)
var42: BinaryAssociation = BinaryAssociation(
    name="var42",
    ends={
        Property(name="xs_ForVarDeclaration", type=xs_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ForStatement", type=xs_ForVarDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end43: BinaryAssociation = BinaryAssociation(
    name="end43",
    ends={
        Property(name="xs_Expression45", type=xs_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ForStatement44", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement46: BinaryAssociation = BinaryAssociation(
    name="statement46",
    ends={
        Property(name="xs_Statement48", type=xs_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ForStatement47", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression49: BinaryAssociation = BinaryAssociation(
    name="expression49",
    ends={
        Property(name="xs_Expression50", type=xs_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchStatement", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases51: BinaryAssociation = BinaryAssociation(
    name="cases51",
    ends={
        Property(name="xs_SwitchCase53", type=xs_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchStatement52", type=xs_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default54: BinaryAssociation = BinaryAssociation(
    name="default54",
    ends={
        Property(name="xs_SwitchDefault56", type=xs_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_SwitchStatement55", type=xs_SwitchDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatement31: BinaryAssociation = BinaryAssociation(
    name="thenStatement31",
    ends={
        Property(name="xs_Statement33", type=xs_IfElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_IfElseStatement32", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression57: BinaryAssociation = BinaryAssociation(
    name="expression57",
    ends={
        Property(name="xs_Expression58", type=xs_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ReturnStatement", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement34: BinaryAssociation = BinaryAssociation(
    name="elseStatement34",
    ends={
        Property(name="xs_Statement36", type=xs_IfElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_IfElseStatement35", type=xs_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var59: BinaryAssociation = BinaryAssociation(
    name="var59",
    ends={
        Property(name="xs_Var60", type=xs_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Assign", type=xs_Var, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression61: BinaryAssociation = BinaryAssociation(
    name="expression61",
    ends={
        Property(name="xs_Expression63", type=xs_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Assign62", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition37: BinaryAssociation = BinaryAssociation(
    name="condition37",
    ends={
        Property(name="xs_Expression38", type=xs_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_WhileStatement", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="xs_Expression83", type=xs_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ComparisonExpression82", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right66: BinaryAssociation = BinaryAssociation(
    name="right66",
    ends={
        Property(name="xs_Expression68", type=xs_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_OrExpression67", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left69: BinaryAssociation = BinaryAssociation(
    name="left69",
    ends={
        Property(name="xs_Expression70", type=xs_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_AndExpression", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right71: BinaryAssociation = BinaryAssociation(
    name="right71",
    ends={
        Property(name="xs_Expression73", type=xs_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_AndExpression72", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left74: BinaryAssociation = BinaryAssociation(
    name="left74",
    ends={
        Property(name="xs_Expression75", type=xs_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_EqualsExpression", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right76: BinaryAssociation = BinaryAssociation(
    name="right76",
    ends={
        Property(name="xs_Expression78", type=xs_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_EqualsExpression77", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left64: BinaryAssociation = BinaryAssociation(
    name="left64",
    ends={
        Property(name="xs_Expression65", type=xs_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_OrExpression", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left79: BinaryAssociation = BinaryAssociation(
    name="left79",
    ends={
        Property(name="xs_Expression80", type=xs_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_ComparisonExpression", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function94: BinaryAssociation = BinaryAssociation(
    name="function94",
    ends={
        Property(name="xs_FunctionDeclaration95", type=xs_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Call", type=xs_FunctionDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
arguments96: BinaryAssociation = BinaryAssociation(
    name="arguments96",
    ends={
        Property(name="xs_Expression98", type=xs_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Call97", type=xs_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="xs_Expression85", type=xs_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Term", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="xs_Expression88", type=xs_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Term87", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left89: BinaryAssociation = BinaryAssociation(
    name="left89",
    ends={
        Property(name="xs_Expression90", type=xs_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Factor", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right91: BinaryAssociation = BinaryAssociation(
    name="right91",
    ends={
        Property(name="xs_Expression93", type=xs_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_Factor92", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
z104: BinaryAssociation = BinaryAssociation(
    name="z104",
    ends={
        Property(name="xs_Expression106", type=xs_VectorLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_VectorLiteral105", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
x99: BinaryAssociation = BinaryAssociation(
    name="x99",
    ends={
        Property(name="xs_Expression100", type=xs_VectorLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_VectorLiteral", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
y101: BinaryAssociation = BinaryAssociation(
    name="y101",
    ends={
        Property(name="xs_Expression103", type=xs_VectorLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="xs_VectorLiteral102", type=xs_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_xs_GlobalVarDeclaration_Declaration = Generalization(general=Declaration, specific=xs_GlobalVarDeclaration)
gen_xs_GlobalVarDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=xs_GlobalVarDeclaration)
gen_xs_ParameterDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=xs_ParameterDeclaration)
gen_xs_ForVarDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=xs_ForVarDeclaration)
gen_xs_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=xs_FunctionDeclaration)
gen_xs_RuleDeclaration_Declaration = Generalization(general=Declaration, specific=xs_RuleDeclaration)
gen_xs_IncludeDeclaration_Declaration = Generalization(general=Declaration, specific=xs_IncludeDeclaration)
gen_xs_LocalVarDeclaration_VarDeclaration = Generalization(general=VarDeclaration, specific=xs_LocalVarDeclaration)
gen_xs_LocalVarDeclaration_Statement = Generalization(general=Statement, specific=xs_LocalVarDeclaration)
gen_xs_Expression_Statement = Generalization(general=Statement, specific=xs_Expression)
gen_xs_Var_Expression = Generalization(general=Expression, specific=xs_Var)
gen_xs_Literal_Expression = Generalization(general=Expression, specific=xs_Literal)
gen_xs_PostfixStatement_Statement = Generalization(general=Statement, specific=xs_PostfixStatement)
gen_xs_IfElseStatement_Statement = Generalization(general=Statement, specific=xs_IfElseStatement)
gen_xs_Block_Statement = Generalization(general=Statement, specific=xs_Block)
gen_xs_ForStatement_Statement = Generalization(general=Statement, specific=xs_ForStatement)
gen_xs_SwitchStatement_Statement = Generalization(general=Statement, specific=xs_SwitchStatement)
gen_xs_ReturnStatement_Statement = Generalization(general=Statement, specific=xs_ReturnStatement)
gen_xs_ContinueStatement_Statement = Generalization(general=Statement, specific=xs_ContinueStatement)
gen_xs_BreakStatement_Statement = Generalization(general=Statement, specific=xs_BreakStatement)
gen_xs_Assign_Expression = Generalization(general=Expression, specific=xs_Assign)
gen_xs_WhileStatement_Statement = Generalization(general=Statement, specific=xs_WhileStatement)
gen_xs_OrExpression_Expression = Generalization(general=Expression, specific=xs_OrExpression)
gen_xs_AndExpression_Expression = Generalization(general=Expression, specific=xs_AndExpression)
gen_xs_EqualsExpression_Expression = Generalization(general=Expression, specific=xs_EqualsExpression)
gen_xs_ComparisonExpression_Expression = Generalization(general=Expression, specific=xs_ComparisonExpression)
gen_xs_Term_Expression = Generalization(general=Expression, specific=xs_Term)
gen_xs_Factor_Expression = Generalization(general=Expression, specific=xs_Factor)
gen_xs_Call_Expression = Generalization(general=Expression, specific=xs_Call)
gen_xs_IntType_Type = Generalization(general=Type, specific=xs_IntType)
gen_xs_FloatType_Type = Generalization(general=Type, specific=xs_FloatType)
gen_xs_BoolType_Type = Generalization(general=Type, specific=xs_BoolType)
gen_xs_LiteralString_Literal = Generalization(general=Literal, specific=xs_LiteralString)
gen_xs_LiteralInt_Literal = Generalization(general=Literal, specific=xs_LiteralInt)
gen_xs_LiteralFloat_Literal = Generalization(general=Literal, specific=xs_LiteralFloat)
gen_xs_LiteralBool_Literal = Generalization(general=Literal, specific=xs_LiteralBool)
gen_xs_VectorLiteral_Literal = Generalization(general=Literal, specific=xs_VectorLiteral)
gen_xs_VectorType_Type = Generalization(general=Type, specific=xs_VectorType)
gen_xs_StringType_Type = Generalization(general=Type, specific=xs_StringType)
gen_xs_VoidType_Type = Generalization(general=Type, specific=xs_VoidType)

# Domain Model
domain_model = DomainModel(
    name="xs",
    types={xs_GlobalVarDeclaration, xs_ParameterDeclaration, xs_ForVarDeclaration, xs_FunctionDeclaration, xs_Block, xs_RuleDeclaration, xs_Program, xs_Declaration, xs_IncludeDeclaration, Declaration, xs_VarDeclaration, xs_Expression, xs_LocalVarDeclaration, VarDeclaration, Statement, xs_Type, xs_Var, Expression, xs_Literal, xs_PostfixStatement, xs_IfElseStatement, xs_Statement, xs_SwitchCase, xs_SwitchDefault, xs_ForStatement, xs_SwitchStatement, xs_ReturnStatement, xs_ContinueStatement, xs_BreakStatement, xs_WhileStatement, xs_Assign, xs_OrExpression, xs_AndExpression, xs_EqualsExpression, xs_ComparisonExpression, xs_Term, xs_Factor, xs_Call, xs_IntType, Type, xs_FloatType, xs_BoolType, xs_LiteralString, Literal, xs_LiteralInt, xs_LiteralFloat, xs_LiteralBool, xs_VectorLiteral, xs_VectorType, xs_StringType, xs_VoidType},
    associations={type3, type5, type7, parameters9, body12, declarations0, value1, type2, declaration25, var27, condition29, body14, contents16, value18, statement20, statement23, statement39, var42, end43, statement46, expression49, cases51, default54, thenStatement31, expression57, elseStatement34, var59, expression61, condition37, right81, right66, left69, right71, left74, right76, left64, left79, function94, arguments96, left84, right86, left89, right91, z104, x99, y101},
    generalizations={gen_xs_GlobalVarDeclaration_Declaration, gen_xs_GlobalVarDeclaration_VarDeclaration, gen_xs_ParameterDeclaration_VarDeclaration, gen_xs_ForVarDeclaration_VarDeclaration, gen_xs_FunctionDeclaration_Declaration, gen_xs_RuleDeclaration_Declaration, gen_xs_IncludeDeclaration_Declaration, gen_xs_LocalVarDeclaration_VarDeclaration, gen_xs_LocalVarDeclaration_Statement, gen_xs_Expression_Statement, gen_xs_Var_Expression, gen_xs_Literal_Expression, gen_xs_PostfixStatement_Statement, gen_xs_IfElseStatement_Statement, gen_xs_Block_Statement, gen_xs_ForStatement_Statement, gen_xs_SwitchStatement_Statement, gen_xs_ReturnStatement_Statement, gen_xs_ContinueStatement_Statement, gen_xs_BreakStatement_Statement, gen_xs_Assign_Expression, gen_xs_WhileStatement_Statement, gen_xs_OrExpression_Expression, gen_xs_AndExpression_Expression, gen_xs_EqualsExpression_Expression, gen_xs_ComparisonExpression_Expression, gen_xs_Term_Expression, gen_xs_Factor_Expression, gen_xs_Call_Expression, gen_xs_IntType_Type, gen_xs_FloatType_Type, gen_xs_BoolType_Type, gen_xs_LiteralString_Literal, gen_xs_LiteralInt_Literal, gen_xs_LiteralFloat_Literal, gen_xs_LiteralBool_Literal, gen_xs_VectorLiteral_Literal, gen_xs_VectorType_Type, gen_xs_StringType_Type, gen_xs_VoidType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)