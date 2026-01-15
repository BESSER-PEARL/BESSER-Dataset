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
InvokerRight: Enumeration = Enumeration(
    name="InvokerRight",
    literals={
            EnumerationLiteral(name="CURRENT_USER"),
			EnumerationLiteral(name="DEFINER")
    }
)

# Classes
plSql_CompilationUnit = Class(name="plSql::CompilationUnit")
plSql_Procedure = Class(name="plSql::Procedure")
CompilationUnit = Class(name="CompilationUnit")
NameDeclaration = Class(name="NameDeclaration")
plSql_ParameterSequence = Class(name="plSql::ParameterSequence")
plSql_ProcedureInvokerRightsClause = Class(name="plSql::ProcedureInvokerRightsClause")
plSql_ProcedureContent = Class(name="plSql::ProcedureContent")
plSql_Package = Class(name="plSql::Package")
plSql_Item = Class(name="plSql::Item")
plSql_ProcedureDeclaration = Class(name="plSql::ProcedureDeclaration")
Item = Class(name="Item")
plSql_Function = Class(name="plSql::Function")
plSql_FunctionClause = Class(name="plSql::FunctionClause")
plSql_FunctionContent = Class(name="plSql::FunctionContent")
plSql_ParameterDeclaration = Class(name="plSql::ParameterDeclaration")
plSql_ParameterValue = Class(name="plSql::ParameterValue")
plSql_Expression = Class(name="plSql::Expression")
plSql_FunctionInvokerRightsClause = Class(name="plSql::FunctionInvokerRightsClause")
FunctionClause = Class(name="FunctionClause")
plSql_Pragma = Class(name="plSql::Pragma")
plSql_PragmaRestrictReferences = Class(name="plSql::PragmaRestrictReferences")
Pragma = Class(name="Pragma")
plSql_PragmaTimestamp = Class(name="plSql::PragmaTimestamp")
ProcedureContent = Class(name="ProcedureContent")
plSql_DeclareSection = Class(name="plSql::DeclareSection")
plSql_StatementBody = Class(name="plSql::StatementBody")
plSql_ProcedureDefinition = Class(name="plSql::ProcedureDefinition")
plSql_ProcedureImplementation = Class(name="plSql::ProcedureImplementation")
plSql_ResultCacheClause = Class(name="plSql::ResultCacheClause")
plSql_PipelinedClause = Class(name="plSql::PipelinedClause")
plSql_Statement = Class(name="plSql::Statement")
plSql_ItemDeclaration = Class(name="plSql::ItemDeclaration")
plSql_ExternalProcedureDeclaration = Class(name="plSql::ExternalProcedureDeclaration")
plSql_VariableDeclaration = Class(name="plSql::VariableDeclaration")
ItemDeclaration = Class(name="ItemDeclaration")
plSql_VariableValue = Class(name="plSql::VariableValue")
plSql_IntLiteralExpression = Class(name="plSql::IntLiteralExpression")
Expression = Class(name="Expression")
plSql_StringLiteralExpression = Class(name="plSql::StringLiteralExpression")
plSql_BooleanLiteralExpression = Class(name="plSql::BooleanLiteralExpression")
plSql_NullLiteralExpression = Class(name="plSql::NullLiteralExpression")
plSql_VariableRefExpression = Class(name="plSql::VariableRefExpression")
plSql_VariableRef = Class(name="plSql::VariableRef")
plSql_FunctionImplementation = Class(name="plSql::FunctionImplementation")
FunctionContent = Class(name="FunctionContent")
plSql_DeterministicClause = Class(name="plSql::DeterministicClause")
plSql_AssignmentStatement = Class(name="plSql::AssignmentStatement")
Statement = Class(name="Statement")
plSql_AssignmentTarget = Class(name="plSql::AssignmentTarget")
plSql_VariableAssignmentTarget = Class(name="plSql::VariableAssignmentTarget")
AssignmentTarget = Class(name="AssignmentTarget")
plSql_BlockStatement = Class(name="plSql::BlockStatement")
plSql_CaseStatement = Class(name="plSql::CaseStatement")
plSql_CaseStatementWhenBranch = Class(name="plSql::CaseStatementWhenBranch")
plSql_CaseStatementElseBranch = Class(name="plSql::CaseStatementElseBranch")
plSql_Label = Class(name="plSql::Label")
plSql_ContinueStatement = Class(name="plSql::ContinueStatement")
plSql_ExitStatement = Class(name="plSql::ExitStatement")
plSql_FetchStatement = Class(name="plSql::FetchStatement")
plSql_CloseStatement = Class(name="plSql::CloseStatement")
plSql_FetchStatementIntoClause = Class(name="plSql::FetchStatementIntoClause")
plSql_FetchStatementSingleIntoClause = Class(name="plSql::FetchStatementSingleIntoClause")
FetchStatementIntoClause = Class(name="FetchStatementIntoClause")
plSql_FetchStatementBulkIntoClause = Class(name="plSql::FetchStatementBulkIntoClause")
plSql_GotoStatement = Class(name="plSql::GotoStatement")
plSql_IfStatement = Class(name="plSql::IfStatement")
plSql_IfStatementElsifBranch = Class(name="plSql::IfStatementElsifBranch")
plSql_IfStatementElseBranch = Class(name="plSql::IfStatementElseBranch")
plSql_LoopStatement = Class(name="plSql::LoopStatement")
plSql_BasicLoopStatement = Class(name="plSql::BasicLoopStatement")
LoopStatement = Class(name="LoopStatement")
plSql_WhileLoopStatement = Class(name="plSql::WhileLoopStatement")
plSql_ForLoopStatement = Class(name="plSql::ForLoopStatement")
plSql_LoopVariableDeclaration = Class(name="plSql::LoopVariableDeclaration")
plSql_ReturnStatement = Class(name="plSql::ReturnStatement")
plSql_NullStatement = Class(name="plSql::NullStatement")
plSql_RaiseStatement = Class(name="plSql::RaiseStatement")
plSql_QualifiedName = Class(name="plSql::QualifiedName")
plSql_Name = Class(name="plSql::Name")
plSql_NameDeclaration = Class(name="plSql::NameDeclaration")

# plSql_CompilationUnit class attributes and methods

# plSql_Procedure class attributes and methods
plSql_Procedure_schemaName: Property = Property(name="schemaName", type=StringType)
plSql_Procedure.attributes={plSql_Procedure_schemaName}

# CompilationUnit class attributes and methods

# NameDeclaration class attributes and methods

# plSql_ParameterSequence class attributes and methods

# plSql_ProcedureInvokerRightsClause class attributes and methods
plSql_ProcedureInvokerRightsClause_right: Property = Property(name="right", type=StringType)
plSql_ProcedureInvokerRightsClause.attributes={plSql_ProcedureInvokerRightsClause_right}

# plSql_ProcedureContent class attributes and methods

# plSql_Package class attributes and methods
plSql_Package_schemaName: Property = Property(name="schemaName", type=StringType)
plSql_Package_endName: Property = Property(name="endName", type=StringType)
plSql_Package.attributes={plSql_Package_endName, plSql_Package_schemaName}

# plSql_Item class attributes and methods

# plSql_ProcedureDeclaration class attributes and methods
plSql_ProcedureDeclaration_name: Property = Property(name="name", type=StringType)
plSql_ProcedureDeclaration.attributes={plSql_ProcedureDeclaration_name}

# Item class attributes and methods

# plSql_Function class attributes and methods
plSql_Function_schemaName: Property = Property(name="schemaName", type=StringType)
plSql_Function_returnType: Property = Property(name="returnType", type=StringType)
plSql_Function.attributes={plSql_Function_schemaName, plSql_Function_returnType}

# plSql_FunctionClause class attributes and methods

# plSql_FunctionContent class attributes and methods

# plSql_ParameterDeclaration class attributes and methods
plSql_ParameterDeclaration_behavior: Property = Property(name="behavior", type=StringType)
plSql_ParameterDeclaration_dataType: Property = Property(name="dataType", type=StringType)
plSql_ParameterDeclaration.attributes={plSql_ParameterDeclaration_dataType, plSql_ParameterDeclaration_behavior}

# plSql_ParameterValue class attributes and methods

# plSql_Expression class attributes and methods

# plSql_FunctionInvokerRightsClause class attributes and methods
plSql_FunctionInvokerRightsClause_right: Property = Property(name="right", type=StringType)
plSql_FunctionInvokerRightsClause.attributes={plSql_FunctionInvokerRightsClause_right}

# FunctionClause class attributes and methods

# plSql_Pragma class attributes and methods

# plSql_PragmaRestrictReferences class attributes and methods
plSql_PragmaRestrictReferences_restrictions: Property = Property(name="restrictions", type=StringType)
plSql_PragmaRestrictReferences.attributes={plSql_PragmaRestrictReferences_restrictions}

# Pragma class attributes and methods

# plSql_PragmaTimestamp class attributes and methods
plSql_PragmaTimestamp_timestamp: Property = Property(name="timestamp", type=StringType)
plSql_PragmaTimestamp.attributes={plSql_PragmaTimestamp_timestamp}

# ProcedureContent class attributes and methods

# plSql_DeclareSection class attributes and methods

# plSql_StatementBody class attributes and methods
plSql_StatementBody_endName: Property = Property(name="endName", type=StringType)
plSql_StatementBody.attributes={plSql_StatementBody_endName}

# plSql_ProcedureDefinition class attributes and methods

# plSql_ProcedureImplementation class attributes and methods

# plSql_ResultCacheClause class attributes and methods
plSql_ResultCacheClause_dataSources: Property = Property(name="dataSources", type=StringType)
plSql_ResultCacheClause.attributes={plSql_ResultCacheClause_dataSources}

# plSql_PipelinedClause class attributes and methods

# plSql_Statement class attributes and methods

# plSql_ItemDeclaration class attributes and methods

# plSql_ExternalProcedureDeclaration class attributes and methods

# plSql_VariableDeclaration class attributes and methods
plSql_VariableDeclaration_isConstant: Property = Property(name="isConstant", type=BooleanType)
plSql_VariableDeclaration_dataType: Property = Property(name="dataType", type=StringType)
plSql_VariableDeclaration_isNotNull: Property = Property(name="isNotNull", type=BooleanType)
plSql_VariableDeclaration.attributes={plSql_VariableDeclaration_isConstant, plSql_VariableDeclaration_isNotNull, plSql_VariableDeclaration_dataType}

# ItemDeclaration class attributes and methods

# plSql_VariableValue class attributes and methods

# plSql_IntLiteralExpression class attributes and methods
plSql_IntLiteralExpression_value: Property = Property(name="value", type=IntegerType)
plSql_IntLiteralExpression.attributes={plSql_IntLiteralExpression_value}

# Expression class attributes and methods

# plSql_StringLiteralExpression class attributes and methods
plSql_StringLiteralExpression_value: Property = Property(name="value", type=StringType)
plSql_StringLiteralExpression.attributes={plSql_StringLiteralExpression_value}

# plSql_BooleanLiteralExpression class attributes and methods
plSql_BooleanLiteralExpression_value: Property = Property(name="value", type=StringType)
plSql_BooleanLiteralExpression.attributes={plSql_BooleanLiteralExpression_value}

# plSql_NullLiteralExpression class attributes and methods

# plSql_VariableRefExpression class attributes and methods

# plSql_VariableRef class attributes and methods
plSql_VariableRef_isHostRef: Property = Property(name="isHostRef", type=BooleanType)
plSql_VariableRef.attributes={plSql_VariableRef_isHostRef}

# plSql_FunctionImplementation class attributes and methods

# FunctionContent class attributes and methods

# plSql_DeterministicClause class attributes and methods

# plSql_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# plSql_AssignmentTarget class attributes and methods

# plSql_VariableAssignmentTarget class attributes and methods

# AssignmentTarget class attributes and methods

# plSql_BlockStatement class attributes and methods

# plSql_CaseStatement class attributes and methods
plSql_CaseStatement_endLabel: Property = Property(name="endLabel", type=StringType)
plSql_CaseStatement.attributes={plSql_CaseStatement_endLabel}

# plSql_CaseStatementWhenBranch class attributes and methods

# plSql_CaseStatementElseBranch class attributes and methods

# plSql_Label class attributes and methods
plSql_Label_name: Property = Property(name="name", type=StringType)
plSql_Label.attributes={plSql_Label_name}

# plSql_ContinueStatement class attributes and methods
plSql_ContinueStatement_labelName: Property = Property(name="labelName", type=StringType)
plSql_ContinueStatement.attributes={plSql_ContinueStatement_labelName}

# plSql_ExitStatement class attributes and methods
plSql_ExitStatement_labelName: Property = Property(name="labelName", type=StringType)
plSql_ExitStatement.attributes={plSql_ExitStatement_labelName}

# plSql_FetchStatement class attributes and methods

# plSql_CloseStatement class attributes and methods

# plSql_FetchStatementIntoClause class attributes and methods

# plSql_FetchStatementSingleIntoClause class attributes and methods

# FetchStatementIntoClause class attributes and methods

# plSql_FetchStatementBulkIntoClause class attributes and methods

# plSql_GotoStatement class attributes and methods

# plSql_IfStatement class attributes and methods

# plSql_IfStatementElsifBranch class attributes and methods

# plSql_IfStatementElseBranch class attributes and methods

# plSql_LoopStatement class attributes and methods
plSql_LoopStatement_endLabel: Property = Property(name="endLabel", type=StringType)
plSql_LoopStatement.attributes={plSql_LoopStatement_endLabel}

# plSql_BasicLoopStatement class attributes and methods

# LoopStatement class attributes and methods

# plSql_WhileLoopStatement class attributes and methods

# plSql_ForLoopStatement class attributes and methods

# plSql_LoopVariableDeclaration class attributes and methods

# plSql_ReturnStatement class attributes and methods

# plSql_NullStatement class attributes and methods

# plSql_RaiseStatement class attributes and methods
plSql_RaiseStatement_exceptionName: Property = Property(name="exceptionName", type=StringType)
plSql_RaiseStatement.attributes={plSql_RaiseStatement_exceptionName}

# plSql_QualifiedName class attributes and methods

# plSql_Name class attributes and methods

# plSql_NameDeclaration class attributes and methods
plSql_NameDeclaration_name: Property = Property(name="name", type=StringType)
plSql_NameDeclaration.attributes={plSql_NameDeclaration_name}

# Relationships
parameters0: BinaryAssociation = BinaryAssociation(
    name="parameters0",
    ends={
        Property(name="plSql_ParameterSequence", type=plSql_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Procedure", type=plSql_ParameterSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invokerRights1: BinaryAssociation = BinaryAssociation(
    name="invokerRights1",
    ends={
        Property(name="plSql_ProcedureInvokerRightsClause", type=plSql_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Procedure2", type=plSql_ProcedureInvokerRightsClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content3: BinaryAssociation = BinaryAssociation(
    name="content3",
    ends={
        Property(name="plSql_ProcedureContent", type=plSql_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Procedure4", type=plSql_ProcedureContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invokerRights5: BinaryAssociation = BinaryAssociation(
    name="invokerRights5",
    ends={
        Property(name="plSql_ProcedureInvokerRightsClause6", type=plSql_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Package", type=plSql_ProcedureInvokerRightsClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items7: BinaryAssociation = BinaryAssociation(
    name="items7",
    ends={
        Property(name="plSql_Item", type=plSql_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Package8", type=plSql_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters15: BinaryAssociation = BinaryAssociation(
    name="parameters15",
    ends={
        Property(name="plSql_ParameterSequence16", type=plSql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Function", type=plSql_ParameterSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionClauses17: BinaryAssociation = BinaryAssociation(
    name="functionClauses17",
    ends={
        Property(name="plSql_FunctionClause", type=plSql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Function18", type=plSql_FunctionClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content19: BinaryAssociation = BinaryAssociation(
    name="content19",
    ends={
        Property(name="plSql_FunctionContent", type=plSql_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Function20", type=plSql_FunctionContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters21: BinaryAssociation = BinaryAssociation(
    name="parameters21",
    ends={
        Property(name="plSql_ParameterDeclaration", type=plSql_ParameterSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ParameterSequence22", type=plSql_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="plSql_ParameterValue", type=plSql_ParameterDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ParameterDeclaration24", type=plSql_ParameterValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="plSql_Expression", type=plSql_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ParameterValue26", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declareSection27: BinaryAssociation = BinaryAssociation(
    name="declareSection27",
    ends={
        Property(name="plSql_DeclareSection", type=plSql_ProcedureImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ProcedureImplementation28", type=plSql_DeclareSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="plSql_StatementBody", type=plSql_ProcedureImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ProcedureImplementation30", type=plSql_StatementBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="plSql_ParameterSequence10", type=plSql_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ProcedureDeclaration", type=plSql_ParameterSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters11: BinaryAssociation = BinaryAssociation(
    name="parameters11",
    ends={
        Property(name="plSql_ParameterSequence12", type=plSql_ProcedureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ProcedureDefinition", type=plSql_ParameterSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation13: BinaryAssociation = BinaryAssociation(
    name="implementation13",
    ends={
        Property(name="plSql_ProcedureImplementation", type=plSql_ProcedureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ProcedureDefinition14", type=plSql_ProcedureImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements36: BinaryAssociation = BinaryAssociation(
    name="statements36",
    ends={
        Property(name="plSql_Statement", type=plSql_StatementBody, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_StatementBody37", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items38: BinaryAssociation = BinaryAssociation(
    name="items38",
    ends={
        Property(name="plSql_Item40", type=plSql_DeclareSection, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_DeclareSection39", type=plSql_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value41: BinaryAssociation = BinaryAssociation(
    name="value41",
    ends={
        Property(name="plSql_VariableValue", type=plSql_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_VariableDeclaration", type=plSql_VariableValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression42: BinaryAssociation = BinaryAssociation(
    name="expression42",
    ends={
        Property(name="plSql_Expression44", type=plSql_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_VariableValue43", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable45: BinaryAssociation = BinaryAssociation(
    name="variable45",
    ends={
        Property(name="plSql_VariableRef", type=plSql_VariableRefExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_VariableRefExpression", type=plSql_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declareSection31: BinaryAssociation = BinaryAssociation(
    name="declareSection31",
    ends={
        Property(name="plSql_DeclareSection32", type=plSql_FunctionImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FunctionImplementation", type=plSql_DeclareSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body33: BinaryAssociation = BinaryAssociation(
    name="body33",
    ends={
        Property(name="plSql_StatementBody35", type=plSql_FunctionImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FunctionImplementation34", type=plSql_StatementBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target48: BinaryAssociation = BinaryAssociation(
    name="target48",
    ends={
        Property(name="plSql_AssignmentTarget", type=plSql_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_AssignmentStatement", type=plSql_AssignmentTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression49: BinaryAssociation = BinaryAssociation(
    name="expression49",
    ends={
        Property(name="plSql_Expression51", type=plSql_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_AssignmentStatement50", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable52: BinaryAssociation = BinaryAssociation(
    name="variable52",
    ends={
        Property(name="plSql_VariableRef53", type=plSql_VariableAssignmentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_VariableAssignmentTarget", type=plSql_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declareSection54: BinaryAssociation = BinaryAssociation(
    name="declareSection54",
    ends={
        Property(name="plSql_DeclareSection55", type=plSql_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_BlockStatement", type=plSql_DeclareSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body56: BinaryAssociation = BinaryAssociation(
    name="body56",
    ends={
        Property(name="plSql_StatementBody58", type=plSql_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_BlockStatement57", type=plSql_StatementBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression59: BinaryAssociation = BinaryAssociation(
    name="expression59",
    ends={
        Property(name="plSql_Expression60", type=plSql_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenBranches61: BinaryAssociation = BinaryAssociation(
    name="whenBranches61",
    ends={
        Property(name="plSql_CaseStatementWhenBranch", type=plSql_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatement62", type=plSql_CaseStatementWhenBranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBranch63: BinaryAssociation = BinaryAssociation(
    name="elseBranch63",
    ends={
        Property(name="plSql_CaseStatementElseBranch", type=plSql_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatement64", type=plSql_CaseStatementElseBranch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression65: BinaryAssociation = BinaryAssociation(
    name="expression65",
    ends={
        Property(name="plSql_Expression67", type=plSql_CaseStatementWhenBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatementWhenBranch66", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements68: BinaryAssociation = BinaryAssociation(
    name="statements68",
    ends={
        Property(name="plSql_Statement70", type=plSql_CaseStatementWhenBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatementWhenBranch69", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels46: BinaryAssociation = BinaryAssociation(
    name="labels46",
    ends={
        Property(name="plSql_Label", type=plSql_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Statement47", type=plSql_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whenExpression76: BinaryAssociation = BinaryAssociation(
    name="whenExpression76",
    ends={
        Property(name="plSql_Expression77", type=plSql_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ContinueStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whenExpression78: BinaryAssociation = BinaryAssociation(
    name="whenExpression78",
    ends={
        Property(name="plSql_Expression79", type=plSql_ExitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ExitStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cursor80: BinaryAssociation = BinaryAssociation(
    name="cursor80",
    ends={
        Property(name="plSql_VariableRef81", type=plSql_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FetchStatement", type=plSql_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements71: BinaryAssociation = BinaryAssociation(
    name="statements71",
    ends={
        Property(name="plSql_Statement73", type=plSql_CaseStatementElseBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CaseStatementElseBranch72", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cursor74: BinaryAssociation = BinaryAssociation(
    name="cursor74",
    ends={
        Property(name="plSql_VariableRef75", type=plSql_CloseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_CloseStatement", type=plSql_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intoClause82: BinaryAssociation = BinaryAssociation(
    name="intoClause82",
    ends={
        Property(name="plSql_FetchStatementIntoClause", type=plSql_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FetchStatement83", type=plSql_FetchStatementIntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVariables84: BinaryAssociation = BinaryAssociation(
    name="targetVariables84",
    ends={
        Property(name="plSql_VariableRef86", type=plSql_FetchStatementIntoClause, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FetchStatementIntoClause85", type=plSql_VariableRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
limitExpression87: BinaryAssociation = BinaryAssociation(
    name="limitExpression87",
    ends={
        Property(name="plSql_Expression88", type=plSql_FetchStatementBulkIntoClause, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_FetchStatementBulkIntoClause", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelName89: BinaryAssociation = BinaryAssociation(
    name="labelName89",
    ends={
        Property(name="plSql_Label90", type=plSql_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_GotoStatement", type=plSql_Label, multiplicity=Multiplicity(0, 1))
    }
)
expression91: BinaryAssociation = BinaryAssociation(
    name="expression91",
    ends={
        Property(name="plSql_Expression92", type=plSql_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements93: BinaryAssociation = BinaryAssociation(
    name="statements93",
    ends={
        Property(name="plSql_Statement95", type=plSql_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatement94", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsifBranches96: BinaryAssociation = BinaryAssociation(
    name="elsifBranches96",
    ends={
        Property(name="plSql_IfStatementElsifBranch", type=plSql_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatement97", type=plSql_IfStatementElsifBranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements106: BinaryAssociation = BinaryAssociation(
    name="statements106",
    ends={
        Property(name="plSql_Statement108", type=plSql_IfStatementElseBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatementElseBranch107", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements109: BinaryAssociation = BinaryAssociation(
    name="statements109",
    ends={
        Property(name="plSql_Statement110", type=plSql_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_LoopStatement", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression111: BinaryAssociation = BinaryAssociation(
    name="expression111",
    ends={
        Property(name="plSql_Expression112", type=plSql_WhileLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_WhileLoopStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexVariable113: BinaryAssociation = BinaryAssociation(
    name="indexVariable113",
    ends={
        Property(name="plSql_LoopVariableDeclaration", type=plSql_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ForLoopStatement", type=plSql_LoopVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerBound114: BinaryAssociation = BinaryAssociation(
    name="lowerBound114",
    ends={
        Property(name="plSql_Expression116", type=plSql_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ForLoopStatement115", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound117: BinaryAssociation = BinaryAssociation(
    name="upperBound117",
    ends={
        Property(name="plSql_Expression119", type=plSql_ForLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ForLoopStatement118", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="plSql_Expression121", type=plSql_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_ReturnStatement", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBranch98: BinaryAssociation = BinaryAssociation(
    name="elseBranch98",
    ends={
        Property(name="plSql_IfStatementElseBranch", type=plSql_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatement99", type=plSql_IfStatementElseBranch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression100: BinaryAssociation = BinaryAssociation(
    name="expression100",
    ends={
        Property(name="plSql_Expression102", type=plSql_IfStatementElsifBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatementElsifBranch101", type=plSql_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements103: BinaryAssociation = BinaryAssociation(
    name="statements103",
    ends={
        Property(name="plSql_Statement105", type=plSql_IfStatementElsifBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_IfStatementElsifBranch104", type=plSql_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration126: BinaryAssociation = BinaryAssociation(
    name="declaration126",
    ends={
        Property(name="plSql_NameDeclaration", type=plSql_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_Name127", type=plSql_NameDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
name122: BinaryAssociation = BinaryAssociation(
    name="name122",
    ends={
        Property(name="plSql_QualifiedName", type=plSql_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_VariableRef123", type=plSql_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names124: BinaryAssociation = BinaryAssociation(
    name="names124",
    ends={
        Property(name="plSql_Name", type=plSql_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="plSql_QualifiedName125", type=plSql_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_plSql_Procedure_CompilationUnit = Generalization(general=CompilationUnit, specific=plSql_Procedure)
gen_plSql_Procedure_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_Procedure)
gen_plSql_Package_CompilationUnit = Generalization(general=CompilationUnit, specific=plSql_Package)
gen_plSql_Package_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_Package)
gen_plSql_ProcedureDeclaration_Item = Generalization(general=Item, specific=plSql_ProcedureDeclaration)
gen_plSql_Function_CompilationUnit = Generalization(general=CompilationUnit, specific=plSql_Function)
gen_plSql_Function_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_Function)
gen_plSql_ParameterDeclaration_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_ParameterDeclaration)
gen_plSql_FunctionInvokerRightsClause_FunctionClause = Generalization(general=FunctionClause, specific=plSql_FunctionInvokerRightsClause)
gen_plSql_Pragma_Item = Generalization(general=Item, specific=plSql_Pragma)
gen_plSql_PragmaRestrictReferences_Pragma = Generalization(general=Pragma, specific=plSql_PragmaRestrictReferences)
gen_plSql_PragmaTimestamp_Pragma = Generalization(general=Pragma, specific=plSql_PragmaTimestamp)
gen_plSql_ProcedureImplementation_ProcedureContent = Generalization(general=ProcedureContent, specific=plSql_ProcedureImplementation)
gen_plSql_ProcedureDefinition_Item = Generalization(general=Item, specific=plSql_ProcedureDefinition)
gen_plSql_ProcedureDefinition_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_ProcedureDefinition)
gen_plSql_ResultCacheClause_FunctionClause = Generalization(general=FunctionClause, specific=plSql_ResultCacheClause)
gen_plSql_PipelinedClause_FunctionClause = Generalization(general=FunctionClause, specific=plSql_PipelinedClause)
gen_plSql_ItemDeclaration_Item = Generalization(general=Item, specific=plSql_ItemDeclaration)
gen_plSql_ExternalProcedureDeclaration_ProcedureContent = Generalization(general=ProcedureContent, specific=plSql_ExternalProcedureDeclaration)
gen_plSql_VariableDeclaration_ItemDeclaration = Generalization(general=ItemDeclaration, specific=plSql_VariableDeclaration)
gen_plSql_VariableDeclaration_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_VariableDeclaration)
gen_plSql_IntLiteralExpression_Expression = Generalization(general=Expression, specific=plSql_IntLiteralExpression)
gen_plSql_StringLiteralExpression_Expression = Generalization(general=Expression, specific=plSql_StringLiteralExpression)
gen_plSql_BooleanLiteralExpression_Expression = Generalization(general=Expression, specific=plSql_BooleanLiteralExpression)
gen_plSql_NullLiteralExpression_Expression = Generalization(general=Expression, specific=plSql_NullLiteralExpression)
gen_plSql_VariableRefExpression_Expression = Generalization(general=Expression, specific=plSql_VariableRefExpression)
gen_plSql_FunctionImplementation_FunctionContent = Generalization(general=FunctionContent, specific=plSql_FunctionImplementation)
gen_plSql_DeterministicClause_FunctionClause = Generalization(general=FunctionClause, specific=plSql_DeterministicClause)
gen_plSql_AssignmentStatement_Statement = Generalization(general=Statement, specific=plSql_AssignmentStatement)
gen_plSql_VariableAssignmentTarget_AssignmentTarget = Generalization(general=AssignmentTarget, specific=plSql_VariableAssignmentTarget)
gen_plSql_BlockStatement_Statement = Generalization(general=Statement, specific=plSql_BlockStatement)
gen_plSql_CaseStatement_Statement = Generalization(general=Statement, specific=plSql_CaseStatement)
gen_plSql_ContinueStatement_Statement = Generalization(general=Statement, specific=plSql_ContinueStatement)
gen_plSql_ExitStatement_Statement = Generalization(general=Statement, specific=plSql_ExitStatement)
gen_plSql_FetchStatement_Statement = Generalization(general=Statement, specific=plSql_FetchStatement)
gen_plSql_CloseStatement_Statement = Generalization(general=Statement, specific=plSql_CloseStatement)
gen_plSql_FetchStatementSingleIntoClause_FetchStatementIntoClause = Generalization(general=FetchStatementIntoClause, specific=plSql_FetchStatementSingleIntoClause)
gen_plSql_FetchStatementBulkIntoClause_FetchStatementIntoClause = Generalization(general=FetchStatementIntoClause, specific=plSql_FetchStatementBulkIntoClause)
gen_plSql_GotoStatement_Statement = Generalization(general=Statement, specific=plSql_GotoStatement)
gen_plSql_IfStatement_Statement = Generalization(general=Statement, specific=plSql_IfStatement)
gen_plSql_LoopStatement_Statement = Generalization(general=Statement, specific=plSql_LoopStatement)
gen_plSql_BasicLoopStatement_LoopStatement = Generalization(general=LoopStatement, specific=plSql_BasicLoopStatement)
gen_plSql_WhileLoopStatement_LoopStatement = Generalization(general=LoopStatement, specific=plSql_WhileLoopStatement)
gen_plSql_ForLoopStatement_LoopStatement = Generalization(general=LoopStatement, specific=plSql_ForLoopStatement)
gen_plSql_ReturnStatement_Statement = Generalization(general=Statement, specific=plSql_ReturnStatement)
gen_plSql_NullStatement_Statement = Generalization(general=Statement, specific=plSql_NullStatement)
gen_plSql_RaiseStatement_Statement = Generalization(general=Statement, specific=plSql_RaiseStatement)
gen_plSql_LoopVariableDeclaration_NameDeclaration = Generalization(general=NameDeclaration, specific=plSql_LoopVariableDeclaration)

# Domain Model
domain_model = DomainModel(
    name="plSql",
    types={plSql_CompilationUnit, plSql_Procedure, CompilationUnit, NameDeclaration, plSql_ParameterSequence, plSql_ProcedureInvokerRightsClause, plSql_ProcedureContent, plSql_Package, plSql_Item, plSql_ProcedureDeclaration, Item, plSql_Function, plSql_FunctionClause, plSql_FunctionContent, plSql_ParameterDeclaration, plSql_ParameterValue, plSql_Expression, plSql_FunctionInvokerRightsClause, FunctionClause, plSql_Pragma, plSql_PragmaRestrictReferences, Pragma, plSql_PragmaTimestamp, ProcedureContent, plSql_DeclareSection, plSql_StatementBody, plSql_ProcedureDefinition, plSql_ProcedureImplementation, plSql_ResultCacheClause, plSql_PipelinedClause, plSql_Statement, plSql_ItemDeclaration, plSql_ExternalProcedureDeclaration, plSql_VariableDeclaration, ItemDeclaration, plSql_VariableValue, plSql_IntLiteralExpression, Expression, plSql_StringLiteralExpression, plSql_BooleanLiteralExpression, plSql_NullLiteralExpression, plSql_VariableRefExpression, plSql_VariableRef, plSql_FunctionImplementation, FunctionContent, plSql_DeterministicClause, plSql_AssignmentStatement, Statement, plSql_AssignmentTarget, plSql_VariableAssignmentTarget, AssignmentTarget, plSql_BlockStatement, plSql_CaseStatement, plSql_CaseStatementWhenBranch, plSql_CaseStatementElseBranch, plSql_Label, plSql_ContinueStatement, plSql_ExitStatement, plSql_FetchStatement, plSql_CloseStatement, plSql_FetchStatementIntoClause, plSql_FetchStatementSingleIntoClause, FetchStatementIntoClause, plSql_FetchStatementBulkIntoClause, plSql_GotoStatement, plSql_IfStatement, plSql_IfStatementElsifBranch, plSql_IfStatementElseBranch, plSql_LoopStatement, plSql_BasicLoopStatement, LoopStatement, plSql_WhileLoopStatement, plSql_ForLoopStatement, plSql_LoopVariableDeclaration, plSql_ReturnStatement, plSql_NullStatement, plSql_RaiseStatement, plSql_QualifiedName, plSql_Name, plSql_NameDeclaration, InvokerRight},
    associations={parameters0, invokerRights1, content3, invokerRights5, items7, parameters15, functionClauses17, content19, parameters21, value23, expression25, declareSection27, body29, parameters9, parameters11, implementation13, statements36, items38, value41, expression42, variable45, declareSection31, body33, target48, expression49, variable52, declareSection54, body56, expression59, whenBranches61, elseBranch63, expression65, statements68, labels46, whenExpression76, whenExpression78, cursor80, statements71, cursor74, intoClause82, targetVariables84, limitExpression87, labelName89, expression91, statements93, elsifBranches96, statements106, statements109, expression111, indexVariable113, lowerBound114, upperBound117, expression120, elseBranch98, expression100, statements103, declaration126, name122, names124},
    generalizations={gen_plSql_Procedure_CompilationUnit, gen_plSql_Procedure_NameDeclaration, gen_plSql_Package_CompilationUnit, gen_plSql_Package_NameDeclaration, gen_plSql_ProcedureDeclaration_Item, gen_plSql_Function_CompilationUnit, gen_plSql_Function_NameDeclaration, gen_plSql_ParameterDeclaration_NameDeclaration, gen_plSql_FunctionInvokerRightsClause_FunctionClause, gen_plSql_Pragma_Item, gen_plSql_PragmaRestrictReferences_Pragma, gen_plSql_PragmaTimestamp_Pragma, gen_plSql_ProcedureImplementation_ProcedureContent, gen_plSql_ProcedureDefinition_Item, gen_plSql_ProcedureDefinition_NameDeclaration, gen_plSql_ResultCacheClause_FunctionClause, gen_plSql_PipelinedClause_FunctionClause, gen_plSql_ItemDeclaration_Item, gen_plSql_ExternalProcedureDeclaration_ProcedureContent, gen_plSql_VariableDeclaration_ItemDeclaration, gen_plSql_VariableDeclaration_NameDeclaration, gen_plSql_IntLiteralExpression_Expression, gen_plSql_StringLiteralExpression_Expression, gen_plSql_BooleanLiteralExpression_Expression, gen_plSql_NullLiteralExpression_Expression, gen_plSql_VariableRefExpression_Expression, gen_plSql_FunctionImplementation_FunctionContent, gen_plSql_DeterministicClause_FunctionClause, gen_plSql_AssignmentStatement_Statement, gen_plSql_VariableAssignmentTarget_AssignmentTarget, gen_plSql_BlockStatement_Statement, gen_plSql_CaseStatement_Statement, gen_plSql_ContinueStatement_Statement, gen_plSql_ExitStatement_Statement, gen_plSql_FetchStatement_Statement, gen_plSql_CloseStatement_Statement, gen_plSql_FetchStatementSingleIntoClause_FetchStatementIntoClause, gen_plSql_FetchStatementBulkIntoClause_FetchStatementIntoClause, gen_plSql_GotoStatement_Statement, gen_plSql_IfStatement_Statement, gen_plSql_LoopStatement_Statement, gen_plSql_BasicLoopStatement_LoopStatement, gen_plSql_WhileLoopStatement_LoopStatement, gen_plSql_ForLoopStatement_LoopStatement, gen_plSql_ReturnStatement_Statement, gen_plSql_NullStatement_Statement, gen_plSql_RaiseStatement_Statement, gen_plSql_LoopVariableDeclaration_NameDeclaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)