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
LiteralExpressionType: Enumeration = Enumeration(
    name="LiteralExpressionType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="NULL")
    }
)

BooleanOperatorType: Enumeration = Enumeration(
    name="BooleanOperatorType",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="LESSTHAN"),
			EnumerationLiteral(name="GREATERTHAN"),
			EnumerationLiteral(name="NOTEQUALS"),
			EnumerationLiteral(name="LESSEQUALS"),
			EnumerationLiteral(name="GREATEREQUALS")
    }
)

ArithmeticOperatorType: Enumeration = Enumeration(
    name="ArithmeticOperatorType",
    literals={
            EnumerationLiteral(name="EXPONENT"),
			EnumerationLiteral(name="POSITIVE"),
			EnumerationLiteral(name="NEGATIVE"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="DOUBLEVERTICALBAR"),
			EnumerationLiteral(name="MULTIPLICATION"),
			EnumerationLiteral(name="DIVISION")
    }
)

BasicTypes: Enumeration = Enumeration(
    name="BasicTypes",
    literals={
            EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="VARCHAR2"),
			EnumerationLiteral(name="BINARY_INTEGER"),
			EnumerationLiteral(name="BINARY_FLOAT"),
			EnumerationLiteral(name="BINARY_DOUBLE"),
			EnumerationLiteral(name="NATURAL"),
			EnumerationLiteral(name="POSITIVE"),
			EnumerationLiteral(name="NUMBER"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="DEC"),
			EnumerationLiteral(name="CHARACTER"),
			EnumerationLiteral(name="NCHAR"),
			EnumerationLiteral(name="NVARCHAR"),
			EnumerationLiteral(name="NVARCHAR2"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="CLOB"),
			EnumerationLiteral(name="ROWID")
    }
)

# Classes
plsql_statement_Statement = Class(name="plsql::statement::Statement", is_abstract=True)
plsql_statement_AssignmentStatement = Class(name="plsql::statement::AssignmentStatement")
Statement = Class(name="Statement")
Expression = Class(name="Expression")
plsql_statement_ExitStatement = Class(name="plsql::statement::ExitStatement")
plsql_statement_GotoStatement = Class(name="plsql::statement::GotoStatement")
statement_Statement = Class(name="statement::Statement")
declaration_NamedElement = Class(name="declaration::NamedElement")
plsql_statement_CaseStatement = Class(name="plsql::statement::CaseStatement")
plsql_statement_IfStatement = Class(name="plsql::statement::IfStatement")
IfStatement = Class(name="IfStatement")
plsql_statement_LoopStatement = Class(name="plsql::statement::LoopStatement")
VariableDeclaration = Class(name="VariableDeclaration")
plsql_statement_NullStatement = Class(name="plsql::statement::NullStatement")
plsql_statement_RaiseStatement = Class(name="plsql::statement::RaiseStatement")
plsql_statement_ReturnStatement = Class(name="plsql::statement::ReturnStatement")
plsql_statement_BlockStatement = Class(name="plsql::statement::BlockStatement")
Declaration = Class(name="Declaration")
ExceptionSection = Class(name="ExceptionSection")
plsql_statement_FunctionCallStatement = Class(name="plsql::statement::FunctionCallStatement")
expression_Expression = Class(name="expression::Expression")
FunctionCallParameter = Class(name="FunctionCallParameter")
plsql_statement_SQLStatement = Class(name="plsql::statement::SQLStatement")
plsql_statement_ControlSQLStatement = Class(name="plsql::statement::ControlSQLStatement")
SQLStatement = Class(name="SQLStatement")
plsql_statement_CloseStatement = Class(name="plsql::statement::CloseStatement")
ControlSQLStatement = Class(name="ControlSQLStatement")
CursorDeclaration = Class(name="CursorDeclaration")
plsql_statement_CommitStatement = Class(name="plsql::statement::CommitStatement")
plsql_statement_FetchStatement = Class(name="plsql::statement::FetchStatement")
plsql_statement_ForStatement = Class(name="plsql::statement::ForStatement")
LoopStatement = Class(name="LoopStatement")
plsql_statement_RollbackStatement = Class(name="plsql::statement::RollbackStatement")
plsql_statement_SavepointStatement = Class(name="plsql::statement::SavepointStatement")
plsql_statement_ModifySQLStatement = Class(name="plsql::statement::ModifySQLStatement")
plsql_statement_SelectStatement = Class(name="plsql::statement::SelectStatement")
ModifySQLStatement = Class(name="ModifySQLStatement")
SQLCondition = Class(name="SQLCondition")
plsql_statement_InsertStatement = Class(name="plsql::statement::InsertStatement")
plsql_statement_UpdateStatement = Class(name="plsql::statement::UpdateStatement")
UpdatePair = Class(name="UpdatePair")
VarRefExpression = Class(name="VarRefExpression")
plsql_statement_LockTableStatement = Class(name="plsql::statement::LockTableStatement")
plsql_statement_OpenStatement = Class(name="plsql::statement::OpenStatement")
plsql_expression_InRangeExpression = Class(name="plsql::expression::InRangeExpression")
plsql_statement_DeleteStatement = Class(name="plsql::statement::DeleteStatement")
plsql_statement_SetTransactionStatement = Class(name="plsql::statement::SetTransactionStatement")
plsql_statement_ExceptionSection = Class(name="plsql::statement::ExceptionSection")
plsql_expression_LikeExpression = Class(name="plsql::expression::LikeExpression")
plsql_expression_Expression = Class(name="plsql::expression::Expression", is_abstract=True)
plsql_expression_BooleanExpression = Class(name="plsql::expression::BooleanExpression")
condition_SQLCondition = Class(name="condition::SQLCondition")
plsql_expression_NotExpression = Class(name="plsql::expression::NotExpression")
plsql_expression_IsNullExpression = Class(name="plsql::expression::IsNullExpression")
plsql_statement_UpdatePair = Class(name="plsql::statement::UpdatePair")
plsql_expression_SQLCursor = Class(name="plsql::expression::SQLCursor")
plsql_expression_PropertyAccess = Class(name="plsql::expression::PropertyAccess")
plsql_expression_FoundExpression = Class(name="plsql::expression::FoundExpression")
plsql_expression_VarRefExpression = Class(name="plsql::expression::VarRefExpression", is_abstract=True)
plsql_expression_FormsVarRef = Class(name="plsql::expression::FormsVarRef")
plsql_expression_SQLVariable = Class(name="plsql::expression::SQLVariable")
plsql_expression_LiteralExpression = Class(name="plsql::expression::LiteralExpression")
plsql_expression_FunctionCallParameter = Class(name="plsql::expression::FunctionCallParameter")
NamedElement = Class(name="NamedElement")
plsql_expression_ArithmeticExpression = Class(name="plsql::expression::ArithmeticExpression")
plsql_expression_StringOperation = Class(name="plsql::expression::StringOperation")
plsql_expression_ConcatString = Class(name="plsql::expression::ConcatString")
StringOperation = Class(name="StringOperation")
plsql_type_Type = Class(name="plsql::type::Type")
plsql_type_Datatype = Class(name="plsql::type::Datatype")
Type = Class(name="Type")
plsql_condition_NotCondition = Class(name="plsql::condition::NotCondition")
plsql_condition_ConditionComparison = Class(name="plsql::condition::ConditionComparison")
plsql_type_IndirectType = Class(name="plsql::type::IndirectType")
plsql_type_GenericType = Class(name="plsql::type::GenericType")
plsql_type_TypedElement = Class(name="plsql::type::TypedElement", is_abstract=True)
plsql_condition_SQLCondition = Class(name="plsql::condition::SQLCondition", is_abstract=True)
plsql_condition_BooleanCondition = Class(name="plsql::condition::BooleanCondition")
plsql_declaration_FunctionDeclaration = Class(name="plsql::declaration::FunctionDeclaration")
plsql_declaration_VariableDeclaration = Class(name="plsql::declaration::VariableDeclaration")
declaration_Declaration = Class(name="declaration::Declaration")
type_TypedElement = Class(name="type::TypedElement")
plsql_declaration_CursorDeclaration = Class(name="plsql::declaration::CursorDeclaration")
Argument = Class(name="Argument")
SelectStatement = Class(name="SelectStatement")
plsql_declaration_Declaration = Class(name="plsql::declaration::Declaration", is_abstract=True)
plsql_declaration_ProcedureDeclaration = Class(name="plsql::declaration::ProcedureDeclaration")
plsql_declaration_Argument = Class(name="plsql::declaration::Argument")
plsql_declaration_Package = Class(name="plsql::declaration::Package")
plsql_declaration_TriggerBlock = Class(name="plsql::declaration::TriggerBlock")
statement_BlockStatement = Class(name="statement::BlockStatement")
plsql_declaration_PLSQLDefinition = Class(name="plsql::declaration::PLSQLDefinition")
TriggerBlock = Class(name="TriggerBlock")
plsql_declaration_NamedElement = Class(name="plsql::declaration::NamedElement", is_abstract=True)

# plsql_statement_Statement class attributes and methods

# plsql_statement_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# Expression class attributes and methods

# plsql_statement_ExitStatement class attributes and methods

# plsql_statement_GotoStatement class attributes and methods

# statement_Statement class attributes and methods

# declaration_NamedElement class attributes and methods

# plsql_statement_CaseStatement class attributes and methods

# plsql_statement_IfStatement class attributes and methods

# IfStatement class attributes and methods

# plsql_statement_LoopStatement class attributes and methods

# VariableDeclaration class attributes and methods

# plsql_statement_NullStatement class attributes and methods

# plsql_statement_RaiseStatement class attributes and methods
plsql_statement_RaiseStatement_exception: Property = Property(name="exception", type=StringType)
plsql_statement_RaiseStatement.attributes={plsql_statement_RaiseStatement_exception}

# plsql_statement_ReturnStatement class attributes and methods

# plsql_statement_BlockStatement class attributes and methods

# Declaration class attributes and methods

# ExceptionSection class attributes and methods

# plsql_statement_FunctionCallStatement class attributes and methods

# expression_Expression class attributes and methods

# FunctionCallParameter class attributes and methods

# plsql_statement_SQLStatement class attributes and methods

# plsql_statement_ControlSQLStatement class attributes and methods

# SQLStatement class attributes and methods

# plsql_statement_CloseStatement class attributes and methods

# ControlSQLStatement class attributes and methods

# CursorDeclaration class attributes and methods

# plsql_statement_CommitStatement class attributes and methods

# plsql_statement_FetchStatement class attributes and methods

# plsql_statement_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# plsql_statement_RollbackStatement class attributes and methods

# plsql_statement_SavepointStatement class attributes and methods

# plsql_statement_ModifySQLStatement class attributes and methods

# plsql_statement_SelectStatement class attributes and methods
plsql_statement_SelectStatement_distinct: Property = Property(name="distinct", type=BooleanType)
plsql_statement_SelectStatement_unique: Property = Property(name="unique", type=BooleanType)
plsql_statement_SelectStatement_all: Property = Property(name="all", type=BooleanType)
plsql_statement_SelectStatement_selectList: Property = Property(name="selectList", type=StringType)
plsql_statement_SelectStatement_bulk: Property = Property(name="bulk", type=BooleanType)
plsql_statement_SelectStatement_collect: Property = Property(name="collect", type=BooleanType)
plsql_statement_SelectStatement_from: Property = Property(name="from", type=StringType)
plsql_statement_SelectStatement_isCount: Property = Property(name="isCount", type=BooleanType)
plsql_statement_SelectStatement.attributes={plsql_statement_SelectStatement_bulk, plsql_statement_SelectStatement_all, plsql_statement_SelectStatement_from, plsql_statement_SelectStatement_unique, plsql_statement_SelectStatement_collect, plsql_statement_SelectStatement_selectList, plsql_statement_SelectStatement_distinct, plsql_statement_SelectStatement_isCount}

# ModifySQLStatement class attributes and methods

# SQLCondition class attributes and methods

# plsql_statement_InsertStatement class attributes and methods
plsql_statement_InsertStatement_into: Property = Property(name="into", type=StringType)
plsql_statement_InsertStatement_columns: Property = Property(name="columns", type=StringType)
plsql_statement_InsertStatement.attributes={plsql_statement_InsertStatement_into, plsql_statement_InsertStatement_columns}

# plsql_statement_UpdateStatement class attributes and methods
plsql_statement_UpdateStatement_table: Property = Property(name="table", type=StringType)
plsql_statement_UpdateStatement.attributes={plsql_statement_UpdateStatement_table}

# UpdatePair class attributes and methods

# VarRefExpression class attributes and methods

# plsql_statement_LockTableStatement class attributes and methods

# plsql_statement_OpenStatement class attributes and methods

# plsql_expression_InRangeExpression class attributes and methods

# plsql_statement_DeleteStatement class attributes and methods

# plsql_statement_SetTransactionStatement class attributes and methods

# plsql_statement_ExceptionSection class attributes and methods
plsql_statement_ExceptionSection_exceptionNames: Property = Property(name="exceptionNames", type=StringType)
plsql_statement_ExceptionSection.attributes={plsql_statement_ExceptionSection_exceptionNames}

# plsql_expression_LikeExpression class attributes and methods

# plsql_expression_Expression class attributes and methods

# plsql_expression_BooleanExpression class attributes and methods
plsql_expression_BooleanExpression_type: Property = Property(name="type", type=StringType)
plsql_expression_BooleanExpression.attributes={plsql_expression_BooleanExpression_type}

# condition_SQLCondition class attributes and methods

# plsql_expression_NotExpression class attributes and methods

# plsql_expression_IsNullExpression class attributes and methods

# plsql_statement_UpdatePair class attributes and methods
plsql_statement_UpdatePair_column: Property = Property(name="column", type=StringType)
plsql_statement_UpdatePair.attributes={plsql_statement_UpdatePair_column}

# plsql_expression_SQLCursor class attributes and methods

# plsql_expression_PropertyAccess class attributes and methods
plsql_expression_PropertyAccess_propertyName: Property = Property(name="propertyName", type=StringType)
plsql_expression_PropertyAccess.attributes={plsql_expression_PropertyAccess_propertyName}

# plsql_expression_FoundExpression class attributes and methods

# plsql_expression_VarRefExpression class attributes and methods

# plsql_expression_FormsVarRef class attributes and methods
plsql_expression_FormsVarRef_reference: Property = Property(name="reference", type=StringType)
plsql_expression_FormsVarRef.attributes={plsql_expression_FormsVarRef_reference}

# plsql_expression_SQLVariable class attributes and methods

# plsql_expression_LiteralExpression class attributes and methods
plsql_expression_LiteralExpression_type: Property = Property(name="type", type=StringType)
plsql_expression_LiteralExpression_value: Property = Property(name="value", type=StringType)
plsql_expression_LiteralExpression.attributes={plsql_expression_LiteralExpression_type, plsql_expression_LiteralExpression_value}

# plsql_expression_FunctionCallParameter class attributes and methods

# NamedElement class attributes and methods

# plsql_expression_ArithmeticExpression class attributes and methods
plsql_expression_ArithmeticExpression_type: Property = Property(name="type", type=StringType)
plsql_expression_ArithmeticExpression.attributes={plsql_expression_ArithmeticExpression_type}

# plsql_expression_StringOperation class attributes and methods

# plsql_expression_ConcatString class attributes and methods

# StringOperation class attributes and methods

# plsql_type_Type class attributes and methods

# plsql_type_Datatype class attributes and methods
plsql_type_Datatype_name: Property = Property(name="name", type=StringType)
plsql_type_Datatype_range: Property = Property(name="range", type=IntegerType)
plsql_type_Datatype.attributes={plsql_type_Datatype_range, plsql_type_Datatype_name}

# Type class attributes and methods

# plsql_condition_NotCondition class attributes and methods

# plsql_condition_ConditionComparison class attributes and methods
plsql_condition_ConditionComparison_type: Property = Property(name="type", type=StringType)
plsql_condition_ConditionComparison.attributes={plsql_condition_ConditionComparison_type}

# plsql_type_IndirectType class attributes and methods
plsql_type_IndirectType_identifier: Property = Property(name="identifier", type=StringType)
plsql_type_IndirectType_rowtype: Property = Property(name="rowtype", type=BooleanType)
plsql_type_IndirectType_type: Property = Property(name="type", type=BooleanType)
plsql_type_IndirectType_range: Property = Property(name="range", type=IntegerType)
plsql_type_IndirectType.attributes={plsql_type_IndirectType_identifier, plsql_type_IndirectType_rowtype, plsql_type_IndirectType_range, plsql_type_IndirectType_type}

# plsql_type_GenericType class attributes and methods

# plsql_type_TypedElement class attributes and methods

# plsql_condition_SQLCondition class attributes and methods

# plsql_condition_BooleanCondition class attributes and methods
plsql_condition_BooleanCondition_type: Property = Property(name="type", type=StringType)
plsql_condition_BooleanCondition.attributes={plsql_condition_BooleanCondition_type}

# plsql_declaration_FunctionDeclaration class attributes and methods

# plsql_declaration_VariableDeclaration class attributes and methods
plsql_declaration_VariableDeclaration_constant: Property = Property(name="constant", type=BooleanType)
plsql_declaration_VariableDeclaration_notnull: Property = Property(name="notnull", type=BooleanType)
plsql_declaration_VariableDeclaration_default: Property = Property(name="default", type=BooleanType)
plsql_declaration_VariableDeclaration.attributes={plsql_declaration_VariableDeclaration_notnull, plsql_declaration_VariableDeclaration_default, plsql_declaration_VariableDeclaration_constant}

# declaration_Declaration class attributes and methods

# type_TypedElement class attributes and methods

# plsql_declaration_CursorDeclaration class attributes and methods

# Argument class attributes and methods

# SelectStatement class attributes and methods

# plsql_declaration_Declaration class attributes and methods

# plsql_declaration_ProcedureDeclaration class attributes and methods

# plsql_declaration_Argument class attributes and methods
plsql_declaration_Argument_in: Property = Property(name="in", type=BooleanType)
plsql_declaration_Argument_out: Property = Property(name="out", type=BooleanType)
plsql_declaration_Argument_default: Property = Property(name="default", type=BooleanType)
plsql_declaration_Argument.attributes={plsql_declaration_Argument_out, plsql_declaration_Argument_in, plsql_declaration_Argument_default}

# plsql_declaration_Package class attributes and methods

# plsql_declaration_TriggerBlock class attributes and methods

# statement_BlockStatement class attributes and methods

# plsql_declaration_PLSQLDefinition class attributes and methods

# TriggerBlock class attributes and methods

# plsql_declaration_NamedElement class attributes and methods
plsql_declaration_NamedElement_name: Property = Property(name="name", type=StringType)
plsql_declaration_NamedElement.attributes={plsql_declaration_NamedElement_name}

# Relationships
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="Expression", type=plsql_statement_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_AssignmentStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receptor1: BinaryAssociation = BinaryAssociation(
    name="receptor1",
    ends={
        Property(name="Expression3", type=plsql_statement_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_AssignmentStatement2", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition4: BinaryAssociation = BinaryAssociation(
    name="condition4",
    ends={
        Property(name="Expression5", type=plsql_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_IfStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatements6: BinaryAssociation = BinaryAssociation(
    name="ifStatements6",
    ends={
        Property(name="Statement", type=plsql_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_IfStatement7", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsif8: BinaryAssociation = BinaryAssociation(
    name="elsif8",
    ends={
        Property(name="IfStatement", type=plsql_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_IfStatement9", type=IfStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements10: BinaryAssociation = BinaryAssociation(
    name="elseStatements10",
    ends={
        Property(name="Statement12", type=plsql_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_IfStatement11", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index15: BinaryAssociation = BinaryAssociation(
    name="index15",
    ends={
        Property(name="VariableDeclaration", type=plsql_statement_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_ForStatement", type=VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param16: BinaryAssociation = BinaryAssociation(
    name="param16",
    ends={
        Property(name="Expression18", type=plsql_statement_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_ForStatement17", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression19: BinaryAssociation = BinaryAssociation(
    name="expression19",
    ends={
        Property(name="Expression20", type=plsql_statement_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations21: BinaryAssociation = BinaryAssociation(
    name="declarations21",
    ends={
        Property(name="Declaration", type=plsql_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_BlockStatement", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="Statement24", type=plsql_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_BlockStatement23", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionSections25: BinaryAssociation = BinaryAssociation(
    name="exceptionSections25",
    ends={
        Property(name="ExceptionSection", type=plsql_statement_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_BlockStatement26", type=ExceptionSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters27: BinaryAssociation = BinaryAssociation(
    name="parameters27",
    ends={
        Property(name="FunctionCallParameter", type=plsql_statement_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_FunctionCallStatement", type=FunctionCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursor28: BinaryAssociation = BinaryAssociation(
    name="cursor28",
    ends={
        Property(name="CursorDeclaration", type=plsql_statement_CloseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_CloseStatement", type=CursorDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
cursor29: BinaryAssociation = BinaryAssociation(
    name="cursor29",
    ends={
        Property(name="CursorDeclaration30", type=plsql_statement_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_FetchStatement", type=CursorDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="Statement14", type=plsql_statement_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_LoopStatement", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursor33: BinaryAssociation = BinaryAssociation(
    name="cursor33",
    ends={
        Property(name="CursorDeclaration34", type=plsql_statement_OpenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_OpenStatement", type=CursorDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
exprs35: BinaryAssociation = BinaryAssociation(
    name="exprs35",
    ends={
        Property(name="Expression37", type=plsql_statement_OpenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_OpenStatement36", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
into38: BinaryAssociation = BinaryAssociation(
    name="into38",
    ends={
        Property(name="VarRefExpression39", type=plsql_statement_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_SelectStatement", type=VarRefExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where40: BinaryAssociation = BinaryAssociation(
    name="where40",
    ends={
        Property(name="SQLCondition", type=plsql_statement_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_SelectStatement41", type=SQLCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderBy42: BinaryAssociation = BinaryAssociation(
    name="orderBy42",
    ends={
        Property(name="Expression44", type=plsql_statement_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_SelectStatement43", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values45: BinaryAssociation = BinaryAssociation(
    name="values45",
    ends={
        Property(name="Expression46", type=plsql_statement_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_InsertStatement", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pairs47: BinaryAssociation = BinaryAssociation(
    name="pairs47",
    ends={
        Property(name="UpdatePair", type=plsql_statement_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_UpdateStatement", type=UpdatePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where48: BinaryAssociation = BinaryAssociation(
    name="where48",
    ends={
        Property(name="SQLCondition50", type=plsql_statement_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_UpdateStatement49", type=SQLCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
into31: BinaryAssociation = BinaryAssociation(
    name="into31",
    ends={
        Property(name="VarRefExpression", type=plsql_statement_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_FetchStatement32", type=VarRefExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression51: BinaryAssociation = BinaryAssociation(
    name="expression51",
    ends={
        Property(name="Expression52", type=plsql_statement_UpdatePair, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_UpdatePair", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr64: BinaryAssociation = BinaryAssociation(
    name="expr64",
    ends={
        Property(name="Expression65", type=plsql_expression_InRangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_InRangeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lower66: BinaryAssociation = BinaryAssociation(
    name="lower66",
    ends={
        Property(name="Expression68", type=plsql_expression_InRangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_InRangeExpression67", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper69: BinaryAssociation = BinaryAssociation(
    name="upper69",
    ends={
        Property(name="Expression71", type=plsql_expression_InRangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_InRangeExpression70", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr172: BinaryAssociation = BinaryAssociation(
    name="expr172",
    ends={
        Property(name="Expression73", type=plsql_expression_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_LikeExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements53: BinaryAssociation = BinaryAssociation(
    name="statements53",
    ends={
        Property(name="Statement54", type=plsql_statement_ExceptionSection, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_statement_ExceptionSection", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr274: BinaryAssociation = BinaryAssociation(
    name="expr274",
    ends={
        Property(name="Expression76", type=plsql_expression_LikeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_LikeExpression75", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr155: BinaryAssociation = BinaryAssociation(
    name="expr155",
    ends={
        Property(name="Expression56", type=plsql_expression_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_BooleanExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr257: BinaryAssociation = BinaryAssociation(
    name="expr257",
    ends={
        Property(name="Expression59", type=plsql_expression_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_BooleanExpression58", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr60: BinaryAssociation = BinaryAssociation(
    name="expr60",
    ends={
        Property(name="Expression61", type=plsql_expression_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_NotExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr62: BinaryAssociation = BinaryAssociation(
    name="expr62",
    ends={
        Property(name="Expression63", type=plsql_expression_IsNullExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_IsNullExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference79: BinaryAssociation = BinaryAssociation(
    name="reference79",
    ends={
        Property(name="VariableDeclaration80", type=plsql_expression_SQLVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_SQLVariable", type=VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
reference81: BinaryAssociation = BinaryAssociation(
    name="reference81",
    ends={
        Property(name="CursorDeclaration82", type=plsql_expression_SQLCursor, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_SQLCursor", type=CursorDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
cursor77: BinaryAssociation = BinaryAssociation(
    name="cursor77",
    ends={
        Property(name="CursorDeclaration78", type=plsql_expression_FoundExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_FoundExpression", type=CursorDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
expr85: BinaryAssociation = BinaryAssociation(
    name="expr85",
    ends={
        Property(name="Expression86", type=plsql_expression_FunctionCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_FunctionCallParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr83: BinaryAssociation = BinaryAssociation(
    name="expr83",
    ends={
        Property(name="Expression84", type=plsql_expression_PropertyAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_PropertyAccess", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr187: BinaryAssociation = BinaryAssociation(
    name="expr187",
    ends={
        Property(name="Expression88", type=plsql_expression_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_ArithmeticExpression", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr289: BinaryAssociation = BinaryAssociation(
    name="expr289",
    ends={
        Property(name="Expression91", type=plsql_expression_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_ArithmeticExpression90", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs92: BinaryAssociation = BinaryAssociation(
    name="exprs92",
    ends={
        Property(name="Expression93", type=plsql_expression_ConcatString, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_expression_ConcatString", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr195: BinaryAssociation = BinaryAssociation(
    name="expr195",
    ends={
        Property(name="SQLCondition96", type=plsql_condition_BooleanCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_condition_BooleanCondition", type=SQLCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr297: BinaryAssociation = BinaryAssociation(
    name="expr297",
    ends={
        Property(name="SQLCondition99", type=plsql_condition_BooleanCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_condition_BooleanCondition98", type=SQLCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr100: BinaryAssociation = BinaryAssociation(
    name="expr100",
    ends={
        Property(name="SQLCondition101", type=plsql_condition_NotCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_condition_NotCondition", type=SQLCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="Type", type=plsql_type_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_type_TypedElement", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations114: BinaryAssociation = BinaryAssociation(
    name="declarations114",
    ends={
        Property(name="Declaration116", type=plsql_declaration_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_ProcedureDeclaration115", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements117: BinaryAssociation = BinaryAssociation(
    name="statements117",
    ends={
        Property(name="Statement119", type=plsql_declaration_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_ProcedureDeclaration118", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
arguments120: BinaryAssociation = BinaryAssociation(
    name="arguments120",
    ends={
        Property(name="Argument121", type=plsql_declaration_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_FunctionDeclaration", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations122: BinaryAssociation = BinaryAssociation(
    name="declarations122",
    ends={
        Property(name="Declaration124", type=plsql_declaration_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_FunctionDeclaration123", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr1102: BinaryAssociation = BinaryAssociation(
    name="expr1102",
    ends={
        Property(name="Expression103", type=plsql_condition_ConditionComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_condition_ConditionComparison", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr2104: BinaryAssociation = BinaryAssociation(
    name="expr2104",
    ends={
        Property(name="Expression106", type=plsql_condition_ConditionComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_condition_ConditionComparison105", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign107: BinaryAssociation = BinaryAssociation(
    name="assign107",
    ends={
        Property(name="Expression108", type=plsql_declaration_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_VariableDeclaration", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments109: BinaryAssociation = BinaryAssociation(
    name="arguments109",
    ends={
        Property(name="Argument", type=plsql_declaration_CursorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_CursorDeclaration", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
select110: BinaryAssociation = BinaryAssociation(
    name="select110",
    ends={
        Property(name="SelectStatement", type=plsql_declaration_CursorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_CursorDeclaration111", type=SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments112: BinaryAssociation = BinaryAssociation(
    name="arguments112",
    ends={
        Property(name="Argument113", type=plsql_declaration_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_ProcedureDeclaration", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements125: BinaryAssociation = BinaryAssociation(
    name="statements125",
    ends={
        Property(name="Statement127", type=plsql_declaration_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_FunctionDeclaration126", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionSection128: BinaryAssociation = BinaryAssociation(
    name="exceptionSection128",
    ends={
        Property(name="ExceptionSection130", type=plsql_declaration_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_FunctionDeclaration129", type=ExceptionSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign131: BinaryAssociation = BinaryAssociation(
    name="assign131",
    ends={
        Property(name="Expression132", type=plsql_declaration_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_Argument", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations133: BinaryAssociation = BinaryAssociation(
    name="declarations133",
    ends={
        Property(name="Declaration134", type=plsql_declaration_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_Package", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements135: BinaryAssociation = BinaryAssociation(
    name="statements135",
    ends={
        Property(name="Statement137", type=plsql_declaration_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_Package136", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers138: BinaryAssociation = BinaryAssociation(
    name="triggers138",
    ends={
        Property(name="TriggerBlock", type=plsql_declaration_PLSQLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="plsql_declaration_PLSQLDefinition", type=TriggerBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_plsql_statement_AssignmentStatement_Statement = Generalization(general=Statement, specific=plsql_statement_AssignmentStatement)
gen_plsql_statement_ExitStatement_Statement = Generalization(general=Statement, specific=plsql_statement_ExitStatement)
gen_plsql_statement_GotoStatement_statement_Statement = Generalization(general=statement_Statement, specific=plsql_statement_GotoStatement)
gen_plsql_statement_GotoStatement_declaration_NamedElement = Generalization(general=declaration_NamedElement, specific=plsql_statement_GotoStatement)
gen_plsql_statement_CaseStatement_Statement = Generalization(general=Statement, specific=plsql_statement_CaseStatement)
gen_plsql_statement_IfStatement_Statement = Generalization(general=Statement, specific=plsql_statement_IfStatement)
gen_plsql_statement_LoopStatement_Statement = Generalization(general=Statement, specific=plsql_statement_LoopStatement)
gen_plsql_statement_NullStatement_Statement = Generalization(general=Statement, specific=plsql_statement_NullStatement)
gen_plsql_statement_RaiseStatement_Statement = Generalization(general=Statement, specific=plsql_statement_RaiseStatement)
gen_plsql_statement_ReturnStatement_Statement = Generalization(general=Statement, specific=plsql_statement_ReturnStatement)
gen_plsql_statement_BlockStatement_Statement = Generalization(general=Statement, specific=plsql_statement_BlockStatement)
gen_plsql_statement_FunctionCallStatement_statement_Statement = Generalization(general=statement_Statement, specific=plsql_statement_FunctionCallStatement)
gen_plsql_statement_FunctionCallStatement_declaration_NamedElement = Generalization(general=declaration_NamedElement, specific=plsql_statement_FunctionCallStatement)
gen_plsql_statement_FunctionCallStatement_expression_Expression = Generalization(general=expression_Expression, specific=plsql_statement_FunctionCallStatement)
gen_plsql_statement_SQLStatement_Statement = Generalization(general=Statement, specific=plsql_statement_SQLStatement)
gen_plsql_statement_ControlSQLStatement_SQLStatement = Generalization(general=SQLStatement, specific=plsql_statement_ControlSQLStatement)
gen_plsql_statement_CloseStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_CloseStatement)
gen_plsql_statement_CommitStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_CommitStatement)
gen_plsql_statement_FetchStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_FetchStatement)
gen_plsql_statement_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=plsql_statement_ForStatement)
gen_plsql_statement_RollbackStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_RollbackStatement)
gen_plsql_statement_SavepointStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_SavepointStatement)
gen_plsql_statement_ModifySQLStatement_SQLStatement = Generalization(general=SQLStatement, specific=plsql_statement_ModifySQLStatement)
gen_plsql_statement_SelectStatement_ModifySQLStatement = Generalization(general=ModifySQLStatement, specific=plsql_statement_SelectStatement)
gen_plsql_statement_InsertStatement_ModifySQLStatement = Generalization(general=ModifySQLStatement, specific=plsql_statement_InsertStatement)
gen_plsql_statement_UpdateStatement_ModifySQLStatement = Generalization(general=ModifySQLStatement, specific=plsql_statement_UpdateStatement)
gen_plsql_statement_LockTableStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_LockTableStatement)
gen_plsql_statement_OpenStatement_ControlSQLStatement = Generalization(general=ControlSQLStatement, specific=plsql_statement_OpenStatement)
gen_plsql_expression_InRangeExpression_Expression = Generalization(general=Expression, specific=plsql_expression_InRangeExpression)
gen_plsql_statement_DeleteStatement_ModifySQLStatement = Generalization(general=ModifySQLStatement, specific=plsql_statement_DeleteStatement)
gen_plsql_statement_SetTransactionStatement_ModifySQLStatement = Generalization(general=ModifySQLStatement, specific=plsql_statement_SetTransactionStatement)
gen_plsql_expression_LikeExpression_Expression = Generalization(general=Expression, specific=plsql_expression_LikeExpression)
gen_plsql_expression_BooleanExpression_expression_Expression = Generalization(general=expression_Expression, specific=plsql_expression_BooleanExpression)
gen_plsql_expression_BooleanExpression_condition_SQLCondition = Generalization(general=condition_SQLCondition, specific=plsql_expression_BooleanExpression)
gen_plsql_expression_NotExpression_Expression = Generalization(general=Expression, specific=plsql_expression_NotExpression)
gen_plsql_expression_IsNullExpression_Expression = Generalization(general=Expression, specific=plsql_expression_IsNullExpression)
gen_plsql_expression_SQLVariable_VarRefExpression = Generalization(general=VarRefExpression, specific=plsql_expression_SQLVariable)
gen_plsql_expression_SQLCursor_VarRefExpression = Generalization(general=VarRefExpression, specific=plsql_expression_SQLCursor)
gen_plsql_expression_PropertyAccess_Expression = Generalization(general=Expression, specific=plsql_expression_PropertyAccess)
gen_plsql_expression_FoundExpression_Expression = Generalization(general=Expression, specific=plsql_expression_FoundExpression)
gen_plsql_expression_VarRefExpression_Expression = Generalization(general=Expression, specific=plsql_expression_VarRefExpression)
gen_plsql_expression_FormsVarRef_VarRefExpression = Generalization(general=VarRefExpression, specific=plsql_expression_FormsVarRef)
gen_plsql_expression_LiteralExpression_Expression = Generalization(general=Expression, specific=plsql_expression_LiteralExpression)
gen_plsql_expression_FunctionCallParameter_NamedElement = Generalization(general=NamedElement, specific=plsql_expression_FunctionCallParameter)
gen_plsql_expression_ArithmeticExpression_Expression = Generalization(general=Expression, specific=plsql_expression_ArithmeticExpression)
gen_plsql_expression_StringOperation_Expression = Generalization(general=Expression, specific=plsql_expression_StringOperation)
gen_plsql_expression_ConcatString_StringOperation = Generalization(general=StringOperation, specific=plsql_expression_ConcatString)
gen_plsql_type_Datatype_Type = Generalization(general=Type, specific=plsql_type_Datatype)
gen_plsql_condition_NotCondition_SQLCondition = Generalization(general=SQLCondition, specific=plsql_condition_NotCondition)
gen_plsql_condition_ConditionComparison_SQLCondition = Generalization(general=SQLCondition, specific=plsql_condition_ConditionComparison)
gen_plsql_type_IndirectType_Type = Generalization(general=Type, specific=plsql_type_IndirectType)
gen_plsql_type_GenericType_Type = Generalization(general=Type, specific=plsql_type_GenericType)
gen_plsql_condition_BooleanCondition_SQLCondition = Generalization(general=SQLCondition, specific=plsql_condition_BooleanCondition)
gen_plsql_declaration_FunctionDeclaration_type_TypedElement = Generalization(general=type_TypedElement, specific=plsql_declaration_FunctionDeclaration)
gen_plsql_declaration_FunctionDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=plsql_declaration_FunctionDeclaration)
gen_plsql_declaration_VariableDeclaration_declaration_Declaration = Generalization(general=declaration_Declaration, specific=plsql_declaration_VariableDeclaration)
gen_plsql_declaration_VariableDeclaration_type_TypedElement = Generalization(general=type_TypedElement, specific=plsql_declaration_VariableDeclaration)
gen_plsql_declaration_CursorDeclaration_Declaration = Generalization(general=Declaration, specific=plsql_declaration_CursorDeclaration)
gen_plsql_declaration_Declaration_NamedElement = Generalization(general=NamedElement, specific=plsql_declaration_Declaration)
gen_plsql_declaration_ProcedureDeclaration_Declaration = Generalization(general=Declaration, specific=plsql_declaration_ProcedureDeclaration)
gen_plsql_declaration_Argument_declaration_NamedElement = Generalization(general=declaration_NamedElement, specific=plsql_declaration_Argument)
gen_plsql_declaration_Argument_type_TypedElement = Generalization(general=type_TypedElement, specific=plsql_declaration_Argument)
gen_plsql_declaration_Package_NamedElement = Generalization(general=NamedElement, specific=plsql_declaration_Package)
gen_plsql_declaration_TriggerBlock_declaration_NamedElement = Generalization(general=declaration_NamedElement, specific=plsql_declaration_TriggerBlock)
gen_plsql_declaration_TriggerBlock_statement_BlockStatement = Generalization(general=statement_BlockStatement, specific=plsql_declaration_TriggerBlock)

# Domain Model
domain_model = DomainModel(
    name="plsql",
    types={plsql_statement_Statement, plsql_statement_AssignmentStatement, Statement, Expression, plsql_statement_ExitStatement, plsql_statement_GotoStatement, statement_Statement, declaration_NamedElement, plsql_statement_CaseStatement, plsql_statement_IfStatement, IfStatement, plsql_statement_LoopStatement, VariableDeclaration, plsql_statement_NullStatement, plsql_statement_RaiseStatement, plsql_statement_ReturnStatement, plsql_statement_BlockStatement, Declaration, ExceptionSection, plsql_statement_FunctionCallStatement, expression_Expression, FunctionCallParameter, plsql_statement_SQLStatement, plsql_statement_ControlSQLStatement, SQLStatement, plsql_statement_CloseStatement, ControlSQLStatement, CursorDeclaration, plsql_statement_CommitStatement, plsql_statement_FetchStatement, plsql_statement_ForStatement, LoopStatement, plsql_statement_RollbackStatement, plsql_statement_SavepointStatement, plsql_statement_ModifySQLStatement, plsql_statement_SelectStatement, ModifySQLStatement, SQLCondition, plsql_statement_InsertStatement, plsql_statement_UpdateStatement, UpdatePair, VarRefExpression, plsql_statement_LockTableStatement, plsql_statement_OpenStatement, plsql_expression_InRangeExpression, plsql_statement_DeleteStatement, plsql_statement_SetTransactionStatement, plsql_statement_ExceptionSection, plsql_expression_LikeExpression, plsql_expression_Expression, plsql_expression_BooleanExpression, condition_SQLCondition, plsql_expression_NotExpression, plsql_expression_IsNullExpression, plsql_statement_UpdatePair, plsql_expression_SQLCursor, plsql_expression_PropertyAccess, plsql_expression_FoundExpression, plsql_expression_VarRefExpression, plsql_expression_FormsVarRef, plsql_expression_SQLVariable, plsql_expression_LiteralExpression, plsql_expression_FunctionCallParameter, NamedElement, plsql_expression_ArithmeticExpression, plsql_expression_StringOperation, plsql_expression_ConcatString, StringOperation, plsql_type_Type, plsql_type_Datatype, Type, plsql_condition_NotCondition, plsql_condition_ConditionComparison, plsql_type_IndirectType, plsql_type_GenericType, plsql_type_TypedElement, plsql_condition_SQLCondition, plsql_condition_BooleanCondition, plsql_declaration_FunctionDeclaration, plsql_declaration_VariableDeclaration, declaration_Declaration, type_TypedElement, plsql_declaration_CursorDeclaration, Argument, SelectStatement, plsql_declaration_Declaration, plsql_declaration_ProcedureDeclaration, plsql_declaration_Argument, plsql_declaration_Package, plsql_declaration_TriggerBlock, statement_BlockStatement, plsql_declaration_PLSQLDefinition, TriggerBlock, plsql_declaration_NamedElement, LiteralExpressionType, BooleanOperatorType, ArithmeticOperatorType, BasicTypes},
    associations={expression0, receptor1, condition4, ifStatements6, elsif8, elseStatements10, index15, param16, expression19, declarations21, statements22, exceptionSections25, parameters27, cursor28, cursor29, statements13, cursor33, exprs35, into38, where40, orderBy42, values45, pairs47, where48, into31, expression51, expr64, lower66, upper69, expr172, statements53, expr274, expr155, expr257, expr60, expr62, reference79, reference81, cursor77, expr85, expr83, expr187, expr289, exprs92, expr195, expr297, expr100, type94, declarations114, statements117, arguments120, declarations122, expr1102, expr2104, assign107, arguments109, select110, arguments112, statements125, exceptionSection128, assign131, declarations133, statements135, triggers138},
    generalizations={gen_plsql_statement_AssignmentStatement_Statement, gen_plsql_statement_ExitStatement_Statement, gen_plsql_statement_GotoStatement_statement_Statement, gen_plsql_statement_GotoStatement_declaration_NamedElement, gen_plsql_statement_CaseStatement_Statement, gen_plsql_statement_IfStatement_Statement, gen_plsql_statement_LoopStatement_Statement, gen_plsql_statement_NullStatement_Statement, gen_plsql_statement_RaiseStatement_Statement, gen_plsql_statement_ReturnStatement_Statement, gen_plsql_statement_BlockStatement_Statement, gen_plsql_statement_FunctionCallStatement_statement_Statement, gen_plsql_statement_FunctionCallStatement_declaration_NamedElement, gen_plsql_statement_FunctionCallStatement_expression_Expression, gen_plsql_statement_SQLStatement_Statement, gen_plsql_statement_ControlSQLStatement_SQLStatement, gen_plsql_statement_CloseStatement_ControlSQLStatement, gen_plsql_statement_CommitStatement_ControlSQLStatement, gen_plsql_statement_FetchStatement_ControlSQLStatement, gen_plsql_statement_ForStatement_LoopStatement, gen_plsql_statement_RollbackStatement_ControlSQLStatement, gen_plsql_statement_SavepointStatement_ControlSQLStatement, gen_plsql_statement_ModifySQLStatement_SQLStatement, gen_plsql_statement_SelectStatement_ModifySQLStatement, gen_plsql_statement_InsertStatement_ModifySQLStatement, gen_plsql_statement_UpdateStatement_ModifySQLStatement, gen_plsql_statement_LockTableStatement_ControlSQLStatement, gen_plsql_statement_OpenStatement_ControlSQLStatement, gen_plsql_expression_InRangeExpression_Expression, gen_plsql_statement_DeleteStatement_ModifySQLStatement, gen_plsql_statement_SetTransactionStatement_ModifySQLStatement, gen_plsql_expression_LikeExpression_Expression, gen_plsql_expression_BooleanExpression_expression_Expression, gen_plsql_expression_BooleanExpression_condition_SQLCondition, gen_plsql_expression_NotExpression_Expression, gen_plsql_expression_IsNullExpression_Expression, gen_plsql_expression_SQLVariable_VarRefExpression, gen_plsql_expression_SQLCursor_VarRefExpression, gen_plsql_expression_PropertyAccess_Expression, gen_plsql_expression_FoundExpression_Expression, gen_plsql_expression_VarRefExpression_Expression, gen_plsql_expression_FormsVarRef_VarRefExpression, gen_plsql_expression_LiteralExpression_Expression, gen_plsql_expression_FunctionCallParameter_NamedElement, gen_plsql_expression_ArithmeticExpression_Expression, gen_plsql_expression_StringOperation_Expression, gen_plsql_expression_ConcatString_StringOperation, gen_plsql_type_Datatype_Type, gen_plsql_condition_NotCondition_SQLCondition, gen_plsql_condition_ConditionComparison_SQLCondition, gen_plsql_type_IndirectType_Type, gen_plsql_type_GenericType_Type, gen_plsql_condition_BooleanCondition_SQLCondition, gen_plsql_declaration_FunctionDeclaration_type_TypedElement, gen_plsql_declaration_FunctionDeclaration_declaration_Declaration, gen_plsql_declaration_VariableDeclaration_declaration_Declaration, gen_plsql_declaration_VariableDeclaration_type_TypedElement, gen_plsql_declaration_CursorDeclaration_Declaration, gen_plsql_declaration_Declaration_NamedElement, gen_plsql_declaration_ProcedureDeclaration_Declaration, gen_plsql_declaration_Argument_declaration_NamedElement, gen_plsql_declaration_Argument_type_TypedElement, gen_plsql_declaration_Package_NamedElement, gen_plsql_declaration_TriggerBlock_declaration_NamedElement, gen_plsql_declaration_TriggerBlock_statement_BlockStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)