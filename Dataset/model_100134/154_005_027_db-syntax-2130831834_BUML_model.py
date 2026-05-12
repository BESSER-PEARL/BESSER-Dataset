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
StatementType: Enumeration = Enumeration(
    name="StatementType",
    literals={
            EnumerationLiteral(name="DML"),
			EnumerationLiteral(name="DDL"),
			EnumerationLiteral(name="DBL")
    }
)

DropRange: Enumeration = Enumeration(
    name="DropRange",
    literals={
            EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="CASCADE")
    }
)

TargetElement: Enumeration = Enumeration(
    name="TargetElement",
    literals={
            EnumerationLiteral(name="ALIAS"),
			EnumerationLiteral(name="INDEX"),
			EnumerationLiteral(name="VIEW"),
			EnumerationLiteral(name="TABLE")
    }
)

ShareMode: Enumeration = Enumeration(
    name="ShareMode",
    literals={
            EnumerationLiteral(name="SHARE"),
			EnumerationLiteral(name="EXCLUSIVE")
    }
)

TargetItem: Enumeration = Enumeration(
    name="TargetItem",
    literals={
            EnumerationLiteral(name="ALL"),
			EnumerationLiteral(name="CURRENT"),
			EnumerationLiteral(name="ALLSQL")
    }
)

CursorType: Enumeration = Enumeration(
    name="CursorType",
    literals={
            EnumerationLiteral(name="NOTSCROLL"),
			EnumerationLiteral(name="SCROLL"),
			EnumerationLiteral(name="DYNSCROLL")
    }
)

IsolationLevel: Enumeration = Enumeration(
    name="IsolationLevel",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="SERIALIZABLE"),
			EnumerationLiteral(name="NO_COMMIT"),
			EnumerationLiteral(name="READ_UNCOMMITTED"),
			EnumerationLiteral(name="READ_COMMITTED"),
			EnumerationLiteral(name="REPEATABLE_READ")
    }
)

RWOperation: Enumeration = Enumeration(
    name="RWOperation",
    literals={
            EnumerationLiteral(name="READ_ONLY"),
			EnumerationLiteral(name="READ_WRITE")
    }
)

FetchPosition: Enumeration = Enumeration(
    name="FetchPosition",
    literals={
            EnumerationLiteral(name="PRIOR"),
			EnumerationLiteral(name="FIRST"),
			EnumerationLiteral(name="LAST"),
			EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="CURRENT"),
			EnumerationLiteral(name="RELATIVE"),
			EnumerationLiteral(name="NEXT")
    }
)

OpenUsingType: Enumeration = Enumeration(
    name="OpenUsingType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="DESCRIPTOR"),
			EnumerationLiteral(name="VARIABLE")
    }
)

UsingType: Enumeration = Enumeration(
    name="UsingType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="NAMES"),
			EnumerationLiteral(name="SYSTEM_NAMES"),
			EnumerationLiteral(name="LABELS"),
			EnumerationLiteral(name="ANY"),
			EnumerationLiteral(name="BOTH"),
			EnumerationLiteral(name="ALL")
    }
)

# Classes
syntax_BindingParseError = Class(name="syntax_BindingParseError")
syntax_BindingParser = Class(name="syntax_BindingParser", is_abstract=True)
StatementParser = Class(name="StatementParser")
syntax_DefinitionParser = Class(name="syntax_DefinitionParser", is_abstract=True)
syntax_DefinitionParserRegistry = Class(name="syntax_DefinitionParserRegistry", is_abstract=True)
syntax_DefinitionParseError = Class(name="syntax_DefinitionParseError")
syntax_DefinitionParseResult = Class(name="syntax_DefinitionParseResult")
syntax_DefinitionStatement = Class(name="syntax_DefinitionStatement", is_abstract=True)
syntax_DefinitionWriter = Class(name="syntax_DefinitionWriter", is_abstract=True)
StatementWriter = Class(name="StatementWriter")
syntax_BindingParserRegistry = Class(name="syntax_BindingParserRegistry", is_abstract=True)
syntax_BindingParseResult = Class(name="syntax_BindingParseResult")
syntax_BindingStatement = Class(name="syntax_BindingStatement", is_abstract=True)
syntax_DefinitionWriterRegistry = Class(name="syntax_DefinitionWriterRegistry", is_abstract=True)
syntax_EmbeddedStatement = Class(name="syntax_EmbeddedStatement", is_abstract=True)
syntax_NameHelper = Class(name="syntax_NameHelper", is_abstract=True)
Plugin = Class(name="Plugin")
Service = Class(name="Service")
SQLObjectNameHelper = Class(name="SQLObjectNameHelper")
syntax_NameHelperRegistry = Class(name="syntax_NameHelperRegistry", is_abstract=True)
syntax_QueryWriter = Class(name="syntax_QueryWriter", is_abstract=True)
syntax_QueryWriterRegistry = Class(name="syntax_QueryWriterRegistry", is_abstract=True)
syntax_SQLObjectNameHelper = Class(name="syntax_SQLObjectNameHelper", is_abstract=True)
syntax_StatementWriter = Class(name="syntax_StatementWriter", is_abstract=True)
syntax_StatementParser = Class(name="syntax_StatementParser", is_abstract=True)
syntax_ddl_CallStatement = Class(name="syntax_ddl_CallStatement")
DefinitionStatement = Class(name="DefinitionStatement")
ddl_syntax_QualifiedName = Class(name="ddl_syntax_QualifiedName")
syntax_ddl_CommitStatement = Class(name="syntax_ddl_CommitStatement")
syntax_ddl_ConnectStatement = Class(name="syntax_ddl_ConnectStatement")
syntax_ddl_CreateAliasStatement = Class(name="syntax_ddl_CreateAliasStatement")
syntax_QueryParser = Class(name="syntax_QueryParser", is_abstract=True)
syntax_QueryParserRegistry = Class(name="syntax_QueryParserRegistry", is_abstract=True)
ddl_syntax_TableColumnDef = Class(name="ddl_syntax_TableColumnDef")
syntax_ddl_CreateViewStatement = Class(name="syntax_ddl_CreateViewStatement")
syntax_ddl_DisconnectStatement = Class(name="syntax_ddl_DisconnectStatement")
syntax_ddl_DropStatement = Class(name="syntax_ddl_DropStatement")
syntax_ddl_CreateIndexStatement = Class(name="syntax_ddl_CreateIndexStatement")
ddl_syntax_IndexDef = Class(name="ddl_syntax_IndexDef")
syntax_ddl_CreateTableStatement = Class(name="syntax_ddl_CreateTableStatement")
syntax_ddl_RollbackStatement = Class(name="syntax_ddl_RollbackStatement")
syntax_ddl_SetConnectionStatement = Class(name="syntax_ddl_SetConnectionStatement")
syntax_dml_ExtendedQuerySelect = Class(name="syntax_dml_ExtendedQuerySelect")
dml_ExtendedQueryExpressionBody = Class(name="dml_ExtendedQueryExpressionBody")
QuerySelect = Class(name="QuerySelect")
syntax_dml_ExtendedQueryExpressionBody = Class(name="syntax_dml_ExtendedQueryExpressionBody")
QueryExpressionBody = Class(name="QueryExpressionBody")
syntax_dbl_DeclareCursorStatement = Class(name="syntax_dbl_DeclareCursorStatement")
BindingStatement = Class(name="BindingStatement")
syntax_dbl_DescribeStatement = Class(name="syntax_dbl_DescribeStatement")
syntax_ddl_LockTableStatement = Class(name="syntax_ddl_LockTableStatement")
syntax_ddl_ReleaseStatement = Class(name="syntax_ddl_ReleaseStatement")
syntax_ddl_RenameStatement = Class(name="syntax_ddl_RenameStatement")
syntax_dbl_FetchStatement = Class(name="syntax_dbl_FetchStatement")
MultipleRowFetchClause = Class(name="MultipleRowFetchClause")
syntax_dbl_IntoClause = Class(name="syntax_dbl_IntoClause")
syntax_dbl_MultipleRowFetchClause = Class(name="syntax_dbl_MultipleRowFetchClause")
syntax_dbl_SetTransactionStatement = Class(name="syntax_dbl_SetTransactionStatement")
IntoClause = Class(name="IntoClause")
syntax_dbl_ExecuteImmediateStatement = Class(name="syntax_dbl_ExecuteImmediateStatement")
syntax_dbl_ExecuteStatement = Class(name="syntax_dbl_ExecuteStatement")
syntax_dbl_PrepareStatement = Class(name="syntax_dbl_PrepareStatement")
syntax_dbl_CloseStatement = Class(name="syntax_dbl_CloseStatement")
syntax_dbl_OpenStatement = Class(name="syntax_dbl_OpenStatement")

# syntax_BindingParseError class attributes and methods

# syntax_BindingParser class attributes and methods
syntax_BindingParser_m_parseBinding: Method = Method(name="parseBinding", parameters={Parameter(name='syntax_stream', type=StringType)}, type=StringType)
syntax_BindingParser_m_parseBinding: Method = Method(name="parseBinding", parameters={Parameter(name='syntax_sql', type=StringType)}, type=StringType)
syntax_BindingParser.methods={syntax_BindingParser_m_parseBinding, syntax_BindingParser_m_parseBinding}

# StatementParser class attributes and methods

# syntax_DefinitionParser class attributes and methods
syntax_DefinitionParser_m_parseDefinition: Method = Method(name="parseDefinition", parameters={Parameter(name='syntax_stream', type=StringType)}, type=StringType)
syntax_DefinitionParser_m_parseDefinition: Method = Method(name="parseDefinition", parameters={Parameter(name='syntax_sql', type=StringType)}, type=StringType)
syntax_DefinitionParser.methods={syntax_DefinitionParser_m_parseDefinition, syntax_DefinitionParser_m_parseDefinition}

# syntax_DefinitionParserRegistry class attributes and methods
syntax_DefinitionParserRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_DefinitionParserRegistry.methods={syntax_DefinitionParserRegistry_m_lookup}

# syntax_DefinitionParseError class attributes and methods

# syntax_DefinitionParseResult class attributes and methods

# syntax_DefinitionStatement class attributes and methods
syntax_DefinitionStatement_m_getStatementType: Method = Method(name="getStatementType", parameters={}, type=StringType)
syntax_DefinitionStatement.methods={syntax_DefinitionStatement_m_getStatementType}

# syntax_DefinitionWriter class attributes and methods
syntax_DefinitionWriter_m_createSchema: Method = Method(name="createSchema", parameters={Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_schema', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createTable: Method = Method(name="createTable", parameters={Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createView: Method = Method(name="createView", parameters={Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_view', type=StringType), Parameter(name='syntax_name', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropIndex: Method = Method(name="dropIndex", parameters={Parameter(name='syntax_index', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_deleteData: Method = Method(name="deleteData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_insertData: Method = Method(name="insertData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_selectData: Method = Method(name="selectData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createIndex: Method = Method(name="createIndex", parameters={Parameter(name='syntax_index', type=StringType), Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropSchema: Method = Method(name="dropSchema", parameters={Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_ignoreFailOnNonEmpty', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropTable: Method = Method(name="dropTable", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropView: Method = Method(name="dropView", parameters={Parameter(name='syntax_view', type=StringType)}, type=StringType)
syntax_DefinitionWriter.methods={syntax_DefinitionWriter_m_deleteData, syntax_DefinitionWriter_m_selectData, syntax_DefinitionWriter_m_createView, syntax_DefinitionWriter_m_createIndex, syntax_DefinitionWriter_m_dropView, syntax_DefinitionWriter_m_dropSchema, syntax_DefinitionWriter_m_createSchema, syntax_DefinitionWriter_m_createTable, syntax_DefinitionWriter_m_dropIndex, syntax_DefinitionWriter_m_insertData, syntax_DefinitionWriter_m_dropTable}

# StatementWriter class attributes and methods

# syntax_BindingParserRegistry class attributes and methods
syntax_BindingParserRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_BindingParserRegistry.methods={syntax_BindingParserRegistry_m_lookup}

# syntax_BindingParseResult class attributes and methods

# syntax_BindingStatement class attributes and methods
syntax_BindingStatement_m_getStatementType: Method = Method(name="getStatementType", parameters={}, type=StringType)
syntax_BindingStatement.methods={syntax_BindingStatement_m_getStatementType}

# syntax_DefinitionWriterRegistry class attributes and methods
syntax_DefinitionWriterRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_DefinitionWriterRegistry.methods={syntax_DefinitionWriterRegistry_m_lookup}

# syntax_EmbeddedStatement class attributes and methods
syntax_EmbeddedStatement_type: Property = Property(name="type", type=StringType)
syntax_EmbeddedStatement.attributes={syntax_EmbeddedStatement_type}

# syntax_NameHelper class attributes and methods
syntax_NameHelper_m_resolveContainers: Method = Method(name="resolveContainers", parameters={Parameter(name='syntax_query', type=StringType)})
syntax_NameHelper.methods={syntax_NameHelper_m_resolveContainers}

# Plugin class attributes and methods

# Service class attributes and methods

# SQLObjectNameHelper class attributes and methods

# syntax_NameHelperRegistry class attributes and methods
syntax_NameHelperRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_NameHelperRegistry.methods={syntax_NameHelperRegistry_m_lookup}

# syntax_QueryWriter class attributes and methods
syntax_QueryWriter_m_writeQuery: Method = Method(name="writeQuery", parameters={Parameter(name='syntax_statement', type=StringType)}, type=StringType)
syntax_QueryWriter.methods={syntax_QueryWriter_m_writeQuery}

# syntax_QueryWriterRegistry class attributes and methods
syntax_QueryWriterRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_QueryWriterRegistry.methods={syntax_QueryWriterRegistry_m_lookup}

# syntax_SQLObjectNameHelper class attributes and methods

# syntax_StatementWriter class attributes and methods

# syntax_StatementParser class attributes and methods

# syntax_ddl_CallStatement class attributes and methods
syntax_ddl_CallStatement_parms: Property = Property(name="parms", type=StringType)
syntax_ddl_CallStatement.attributes={syntax_ddl_CallStatement_parms}

# DefinitionStatement class attributes and methods

# ddl_syntax_QualifiedName class attributes and methods

# syntax_ddl_CommitStatement class attributes and methods
syntax_ddl_CommitStatement_hold: Property = Property(name="hold", type=BooleanType)
syntax_ddl_CommitStatement.attributes={syntax_ddl_CommitStatement_hold}

# syntax_ddl_ConnectStatement class attributes and methods
syntax_ddl_ConnectStatement_pwd: Property = Property(name="pwd", type=StringType)
syntax_ddl_ConnectStatement_reset: Property = Property(name="reset", type=BooleanType)
syntax_ddl_ConnectStatement_to: Property = Property(name="to", type=StringType)
syntax_ddl_ConnectStatement_user: Property = Property(name="user", type=StringType)
syntax_ddl_ConnectStatement.attributes={syntax_ddl_ConnectStatement_user, syntax_ddl_ConnectStatement_pwd, syntax_ddl_ConnectStatement_to, syntax_ddl_ConnectStatement_reset}

# syntax_ddl_CreateAliasStatement class attributes and methods

# syntax_QueryParser class attributes and methods
syntax_QueryParser_m_parseQuery: Method = Method(name="parseQuery", parameters={Parameter(name='syntax_stream', type=StringType)}, type=StringType)
syntax_QueryParser_m_parseQuery: Method = Method(name="parseQuery", parameters={Parameter(name='syntax_sql', type=StringType)}, type=StringType)
syntax_QueryParser.methods={syntax_QueryParser_m_parseQuery, syntax_QueryParser_m_parseQuery}

# syntax_QueryParserRegistry class attributes and methods
syntax_QueryParserRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_QueryParserRegistry.methods={syntax_QueryParserRegistry_m_lookup}

# ddl_syntax_TableColumnDef class attributes and methods

# syntax_ddl_CreateViewStatement class attributes and methods
syntax_ddl_CreateViewStatement_fields: Property = Property(name="fields", type=StringType)
syntax_ddl_CreateViewStatement_query: Property = Property(name="query", type=StringType)
syntax_ddl_CreateViewStatement.attributes={syntax_ddl_CreateViewStatement_fields, syntax_ddl_CreateViewStatement_query}

# syntax_ddl_DisconnectStatement class attributes and methods
syntax_ddl_DisconnectStatement_target: Property = Property(name="target", type=StringType)
syntax_ddl_DisconnectStatement.attributes={syntax_ddl_DisconnectStatement_target}

# syntax_ddl_DropStatement class attributes and methods
syntax_ddl_DropStatement_range: Property = Property(name="range", type=StringType)
syntax_ddl_DropStatement_target: Property = Property(name="target", type=StringType)
syntax_ddl_DropStatement.attributes={syntax_ddl_DropStatement_range, syntax_ddl_DropStatement_target}

# syntax_ddl_CreateIndexStatement class attributes and methods
syntax_ddl_CreateIndexStatement_unique: Property = Property(name="unique", type=BooleanType)
syntax_ddl_CreateIndexStatement.attributes={syntax_ddl_CreateIndexStatement_unique}

# ddl_syntax_IndexDef class attributes and methods

# syntax_ddl_CreateTableStatement class attributes and methods

# syntax_ddl_RollbackStatement class attributes and methods
syntax_ddl_RollbackStatement_hold: Property = Property(name="hold", type=BooleanType)
syntax_ddl_RollbackStatement.attributes={syntax_ddl_RollbackStatement_hold}

# syntax_ddl_SetConnectionStatement class attributes and methods
syntax_ddl_SetConnectionStatement_databaseName: Property = Property(name="databaseName", type=StringType)
syntax_ddl_SetConnectionStatement.attributes={syntax_ddl_SetConnectionStatement_databaseName}

# syntax_dml_ExtendedQuerySelect class attributes and methods

# dml_ExtendedQueryExpressionBody class attributes and methods

# QuerySelect class attributes and methods

# syntax_dml_ExtendedQueryExpressionBody class attributes and methods
syntax_dml_ExtendedQueryExpressionBody_optimizeRecordsNumber: Property = Property(name="optimizeRecordsNumber", type=IntegerType)
syntax_dml_ExtendedQueryExpressionBody.attributes={syntax_dml_ExtendedQueryExpressionBody_optimizeRecordsNumber}

# QueryExpressionBody class attributes and methods

# syntax_dbl_DeclareCursorStatement class attributes and methods
syntax_dbl_DeclareCursorStatement_cursorName: Property = Property(name="cursorName", type=StringType)
syntax_dbl_DeclareCursorStatement_cursorType: Property = Property(name="cursorType", type=StringType)
syntax_dbl_DeclareCursorStatement_forQuery: Property = Property(name="forQuery", type=StringType)
syntax_dbl_DeclareCursorStatement_forStatementName: Property = Property(name="forStatementName", type=StringType)
syntax_dbl_DeclareCursorStatement_hold: Property = Property(name="hold", type=BooleanType)
syntax_dbl_DeclareCursorStatement.attributes={syntax_dbl_DeclareCursorStatement_cursorType, syntax_dbl_DeclareCursorStatement_forStatementName, syntax_dbl_DeclareCursorStatement_hold, syntax_dbl_DeclareCursorStatement_forQuery, syntax_dbl_DeclareCursorStatement_cursorName}

# BindingStatement class attributes and methods

# syntax_dbl_DescribeStatement class attributes and methods
syntax_dbl_DescribeStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_DescribeStatement.attributes={syntax_dbl_DescribeStatement_statementName}

# syntax_ddl_LockTableStatement class attributes and methods
syntax_ddl_LockTableStatement_allowRead: Property = Property(name="allowRead", type=BooleanType)
syntax_ddl_LockTableStatement_shareMode: Property = Property(name="shareMode", type=StringType)
syntax_ddl_LockTableStatement.attributes={syntax_ddl_LockTableStatement_allowRead, syntax_ddl_LockTableStatement_shareMode}

# syntax_ddl_ReleaseStatement class attributes and methods
syntax_ddl_ReleaseStatement_serverName: Property = Property(name="serverName", type=StringType)
syntax_ddl_ReleaseStatement.attributes={syntax_ddl_ReleaseStatement_serverName}

# syntax_ddl_RenameStatement class attributes and methods
syntax_ddl_RenameStatement_newName: Property = Property(name="newName", type=StringType)
syntax_ddl_RenameStatement_system: Property = Property(name="system", type=StringType)
syntax_ddl_RenameStatement_target: Property = Property(name="target", type=StringType)
syntax_ddl_RenameStatement.attributes={syntax_ddl_RenameStatement_target, syntax_ddl_RenameStatement_newName, syntax_ddl_RenameStatement_system}

# syntax_dbl_FetchStatement class attributes and methods
syntax_dbl_FetchStatement_cursorName: Property = Property(name="cursorName", type=StringType)
syntax_dbl_FetchStatement_into: Property = Property(name="into", type=StringType)
syntax_dbl_FetchStatement_position: Property = Property(name="position", type=StringType)
syntax_dbl_FetchStatement_relativePosition: Property = Property(name="relativePosition", type=StringType)
syntax_dbl_FetchStatement.attributes={syntax_dbl_FetchStatement_into, syntax_dbl_FetchStatement_cursorName, syntax_dbl_FetchStatement_relativePosition, syntax_dbl_FetchStatement_position}

# MultipleRowFetchClause class attributes and methods

# syntax_dbl_IntoClause class attributes and methods
syntax_dbl_IntoClause_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_IntoClause_using: Property = Property(name="using", type=StringType)
syntax_dbl_IntoClause.attributes={syntax_dbl_IntoClause_descriptorName, syntax_dbl_IntoClause_using}

# syntax_dbl_MultipleRowFetchClause class attributes and methods
syntax_dbl_MultipleRowFetchClause_descriptor: Property = Property(name="descriptor", type=StringType)
syntax_dbl_MultipleRowFetchClause_rowsNumber: Property = Property(name="rowsNumber", type=StringType)
syntax_dbl_MultipleRowFetchClause_usingDescriptor: Property = Property(name="usingDescriptor", type=BooleanType)
syntax_dbl_MultipleRowFetchClause.attributes={syntax_dbl_MultipleRowFetchClause_descriptor, syntax_dbl_MultipleRowFetchClause_rowsNumber, syntax_dbl_MultipleRowFetchClause_usingDescriptor}

# syntax_dbl_SetTransactionStatement class attributes and methods
syntax_dbl_SetTransactionStatement_isolationLevel: Property = Property(name="isolationLevel", type=StringType)
syntax_dbl_SetTransactionStatement_rwOperation: Property = Property(name="rwOperation", type=StringType)
syntax_dbl_SetTransactionStatement.attributes={syntax_dbl_SetTransactionStatement_rwOperation, syntax_dbl_SetTransactionStatement_isolationLevel}

# IntoClause class attributes and methods

# syntax_dbl_ExecuteImmediateStatement class attributes and methods
syntax_dbl_ExecuteImmediateStatement_variable: Property = Property(name="variable", type=StringType)
syntax_dbl_ExecuteImmediateStatement.attributes={syntax_dbl_ExecuteImmediateStatement_variable}

# syntax_dbl_ExecuteStatement class attributes and methods
syntax_dbl_ExecuteStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_ExecuteStatement.attributes={syntax_dbl_ExecuteStatement_statementName}

# syntax_dbl_PrepareStatement class attributes and methods
syntax_dbl_PrepareStatement_from_: Property = Property(name="from_", type=StringType)
syntax_dbl_PrepareStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_PrepareStatement.attributes={syntax_dbl_PrepareStatement_statementName, syntax_dbl_PrepareStatement_from_}

# syntax_dbl_CloseStatement class attributes and methods
syntax_dbl_CloseStatement_cursor: Property = Property(name="cursor", type=StringType)
syntax_dbl_CloseStatement.attributes={syntax_dbl_CloseStatement_cursor}

# syntax_dbl_OpenStatement class attributes and methods
syntax_dbl_OpenStatement_cursor: Property = Property(name="cursor", type=StringType)
syntax_dbl_OpenStatement_using: Property = Property(name="using", type=StringType)
syntax_dbl_OpenStatement_usingType: Property = Property(name="usingType", type=StringType)
syntax_dbl_OpenStatement.attributes={syntax_dbl_OpenStatement_using, syntax_dbl_OpenStatement_cursor, syntax_dbl_OpenStatement_usingType}

# Relationships
errorList1: BinaryAssociation = BinaryAssociation(
    name="errorList1",
    ends={
        Property(name="syntax_BindingParseError", type=syntax_BindingParseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_BindingParseResult2", type=syntax_BindingParseError, multiplicity=Multiplicity(0, 9999))
    }
)
definitionStatement3: BinaryAssociation = BinaryAssociation(
    name="definitionStatement3",
    ends={
        Property(name="syntax_DefinitionStatement", type=syntax_DefinitionParseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_DefinitionParseResult", type=syntax_DefinitionStatement, multiplicity=Multiplicity(0, 1))
    }
)
errorList4: BinaryAssociation = BinaryAssociation(
    name="errorList4",
    ends={
        Property(name="syntax_DefinitionParseError", type=syntax_DefinitionParseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_DefinitionParseResult5", type=syntax_DefinitionParseError, multiplicity=Multiplicity(0, 9999))
    }
)
bindingStatement0: BinaryAssociation = BinaryAssociation(
    name="bindingStatement0",
    ends={
        Property(name="syntax_BindingStatement", type=syntax_BindingParseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_BindingParseResult", type=syntax_BindingStatement, multiplicity=Multiplicity(0, 1))
    }
)
nameHelper6: BinaryAssociation = BinaryAssociation(
    name="nameHelper6",
    ends={
        Property(name="syntax_NameHelper", type=syntax_StatementWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_StatementWriter", type=syntax_NameHelper, multiplicity=Multiplicity(0, 1))
    }
)
procedureName7: BinaryAssociation = BinaryAssociation(
    name="procedureName7",
    ends={
        Property(name="ddl_syntax_QualifiedName", type=syntax_ddl_CallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CallStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aliasName8: BinaryAssociation = BinaryAssociation(
    name="aliasName8",
    ends={
        Property(name="ddl_syntax_QualifiedName9", type=syntax_ddl_CreateAliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateAliasStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableName10: BinaryAssociation = BinaryAssociation(
    name="tableName10",
    ends={
        Property(name="ddl_syntax_QualifiedName12", type=syntax_ddl_CreateAliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateAliasStatement11", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableName20: BinaryAssociation = BinaryAssociation(
    name="tableName20",
    ends={
        Property(name="ddl_syntax_QualifiedName21", type=syntax_ddl_CreateTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateTableStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields22: BinaryAssociation = BinaryAssociation(
    name="fields22",
    ends={
        Property(name="ddl_syntax_TableColumnDef", type=syntax_ddl_CreateTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateTableStatement23", type=ddl_syntax_TableColumnDef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
viewName24: BinaryAssociation = BinaryAssociation(
    name="viewName24",
    ends={
        Property(name="ddl_syntax_QualifiedName25", type=syntax_ddl_CreateViewStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateViewStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetName26: BinaryAssociation = BinaryAssociation(
    name="targetName26",
    ends={
        Property(name="ddl_syntax_QualifiedName27", type=syntax_ddl_DropStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_DropStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexName13: BinaryAssociation = BinaryAssociation(
    name="indexName13",
    ends={
        Property(name="ddl_syntax_QualifiedName14", type=syntax_ddl_CreateIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateIndexStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onTable15: BinaryAssociation = BinaryAssociation(
    name="onTable15",
    ends={
        Property(name="ddl_syntax_QualifiedName17", type=syntax_ddl_CreateIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateIndexStatement16", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sortBy18: BinaryAssociation = BinaryAssociation(
    name="sortBy18",
    ends={
        Property(name="ddl_syntax_IndexDef", type=syntax_ddl_CreateIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_CreateIndexStatement19", type=ddl_syntax_IndexDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalName30: BinaryAssociation = BinaryAssociation(
    name="originalName30",
    ends={
        Property(name="ddl_syntax_QualifiedName31", type=syntax_ddl_RenameStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_RenameStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableName28: BinaryAssociation = BinaryAssociation(
    name="tableName28",
    ends={
        Property(name="ddl_syntax_QualifiedName29", type=syntax_ddl_LockTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_LockTableStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipleRowClause33: BinaryAssociation = BinaryAssociation(
    name="multipleRowClause33",
    ends={
        Property(name="MultipleRowFetchClause", type=syntax_dbl_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_FetchStatement", type=MultipleRowFetchClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
into32: BinaryAssociation = BinaryAssociation(
    name="into32",
    ends={
        Property(name="IntoClause", type=syntax_dbl_DescribeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_DescribeStatement", type=IntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
into34: BinaryAssociation = BinaryAssociation(
    name="into34",
    ends={
        Property(name="IntoClause35", type=syntax_dbl_PrepareStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_PrepareStatement", type=IntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_syntax_BindingParser_StatementParser = Generalization(general=StatementParser, specific=syntax_BindingParser)
gen_syntax_DefinitionParser_StatementParser = Generalization(general=StatementParser, specific=syntax_DefinitionParser)
gen_syntax_DefinitionWriter_StatementWriter = Generalization(general=StatementWriter, specific=syntax_DefinitionWriter)
gen_syntax_NameHelper_Plugin = Generalization(general=Plugin, specific=syntax_NameHelper)
gen_syntax_NameHelper_Service = Generalization(general=Service, specific=syntax_NameHelper)
gen_syntax_NameHelper_SQLObjectNameHelper = Generalization(general=SQLObjectNameHelper, specific=syntax_NameHelper)
gen_syntax_QueryWriter_StatementWriter = Generalization(general=StatementWriter, specific=syntax_QueryWriter)
gen_syntax_StatementWriter_Plugin = Generalization(general=Plugin, specific=syntax_StatementWriter)
gen_syntax_StatementWriter_Service = Generalization(general=Service, specific=syntax_StatementWriter)
gen_syntax_StatementParser_Plugin = Generalization(general=Plugin, specific=syntax_StatementParser)
gen_syntax_StatementParser_Service = Generalization(general=Service, specific=syntax_StatementParser)
gen_syntax_ddl_CallStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CallStatement)
gen_syntax_ddl_CommitStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CommitStatement)
gen_syntax_ddl_ConnectStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_ConnectStatement)
gen_syntax_ddl_CreateAliasStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateAliasStatement)
gen_syntax_QueryParser_StatementParser = Generalization(general=StatementParser, specific=syntax_QueryParser)
gen_syntax_ddl_CreateTableStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateTableStatement)
gen_syntax_ddl_CreateViewStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateViewStatement)
gen_syntax_ddl_DisconnectStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_DisconnectStatement)
gen_syntax_ddl_DropStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_DropStatement)
gen_syntax_ddl_CreateIndexStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateIndexStatement)
gen_syntax_ddl_RollbackStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_RollbackStatement)
gen_syntax_ddl_SetConnectionStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_SetConnectionStatement)
gen_syntax_dml_ExtendedQuerySelect_dml_ExtendedQueryExpressionBody = Generalization(general=dml_ExtendedQueryExpressionBody, specific=syntax_dml_ExtendedQuerySelect)
gen_syntax_dml_ExtendedQuerySelect_QuerySelect = Generalization(general=QuerySelect, specific=syntax_dml_ExtendedQuerySelect)
gen_syntax_dml_ExtendedQueryExpressionBody_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=syntax_dml_ExtendedQueryExpressionBody)
gen_syntax_dbl_DeclareCursorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_DeclareCursorStatement)
gen_syntax_dbl_DescribeStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_DescribeStatement)
gen_syntax_ddl_LockTableStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_LockTableStatement)
gen_syntax_ddl_ReleaseStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_ReleaseStatement)
gen_syntax_ddl_RenameStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_RenameStatement)
gen_syntax_dbl_FetchStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_FetchStatement)
gen_syntax_dbl_SetTransactionStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_SetTransactionStatement)
gen_syntax_dbl_ExecuteImmediateStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_ExecuteImmediateStatement)
gen_syntax_dbl_ExecuteStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_ExecuteStatement)
gen_syntax_dbl_PrepareStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_PrepareStatement)
gen_syntax_dbl_CloseStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_CloseStatement)
gen_syntax_dbl_OpenStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_OpenStatement)

# Domain Model
domain_model = DomainModel(
    name="syntax",
    types={syntax_BindingParseError, syntax_BindingParser, StatementParser, syntax_DefinitionParser, syntax_DefinitionParserRegistry, syntax_DefinitionParseError, syntax_DefinitionParseResult, syntax_DefinitionStatement, syntax_DefinitionWriter, StatementWriter, syntax_BindingParserRegistry, syntax_BindingParseResult, syntax_BindingStatement, syntax_DefinitionWriterRegistry, syntax_EmbeddedStatement, syntax_NameHelper, Plugin, Service, SQLObjectNameHelper, syntax_NameHelperRegistry, syntax_QueryWriter, syntax_QueryWriterRegistry, syntax_SQLObjectNameHelper, syntax_StatementWriter, syntax_StatementParser, syntax_ddl_CallStatement, DefinitionStatement, ddl_syntax_QualifiedName, syntax_ddl_CommitStatement, syntax_ddl_ConnectStatement, syntax_ddl_CreateAliasStatement, syntax_QueryParser, syntax_QueryParserRegistry, ddl_syntax_TableColumnDef, syntax_ddl_CreateViewStatement, syntax_ddl_DisconnectStatement, syntax_ddl_DropStatement, syntax_ddl_CreateIndexStatement, ddl_syntax_IndexDef, syntax_ddl_CreateTableStatement, syntax_ddl_RollbackStatement, syntax_ddl_SetConnectionStatement, syntax_dml_ExtendedQuerySelect, dml_ExtendedQueryExpressionBody, QuerySelect, syntax_dml_ExtendedQueryExpressionBody, QueryExpressionBody, syntax_dbl_DeclareCursorStatement, BindingStatement, syntax_dbl_DescribeStatement, syntax_ddl_LockTableStatement, syntax_ddl_ReleaseStatement, syntax_ddl_RenameStatement, syntax_dbl_FetchStatement, MultipleRowFetchClause, syntax_dbl_IntoClause, syntax_dbl_MultipleRowFetchClause, syntax_dbl_SetTransactionStatement, IntoClause, syntax_dbl_ExecuteImmediateStatement, syntax_dbl_ExecuteStatement, syntax_dbl_PrepareStatement, syntax_dbl_CloseStatement, syntax_dbl_OpenStatement, StatementType, DropRange, TargetElement, ShareMode, TargetItem, CursorType, IsolationLevel, RWOperation, FetchPosition, OpenUsingType, UsingType},
    associations={errorList1, definitionStatement3, errorList4, bindingStatement0, nameHelper6, procedureName7, aliasName8, tableName10, tableName20, fields22, viewName24, targetName26, indexName13, onTable15, sortBy18, originalName30, tableName28, multipleRowClause33, into32, into34},
    generalizations={gen_syntax_BindingParser_StatementParser, gen_syntax_DefinitionParser_StatementParser, gen_syntax_DefinitionWriter_StatementWriter, gen_syntax_NameHelper_Plugin, gen_syntax_NameHelper_Service, gen_syntax_NameHelper_SQLObjectNameHelper, gen_syntax_QueryWriter_StatementWriter, gen_syntax_StatementWriter_Plugin, gen_syntax_StatementWriter_Service, gen_syntax_StatementParser_Plugin, gen_syntax_StatementParser_Service, gen_syntax_ddl_CallStatement_DefinitionStatement, gen_syntax_ddl_CommitStatement_DefinitionStatement, gen_syntax_ddl_ConnectStatement_DefinitionStatement, gen_syntax_ddl_CreateAliasStatement_DefinitionStatement, gen_syntax_QueryParser_StatementParser, gen_syntax_ddl_CreateTableStatement_DefinitionStatement, gen_syntax_ddl_CreateViewStatement_DefinitionStatement, gen_syntax_ddl_DisconnectStatement_DefinitionStatement, gen_syntax_ddl_DropStatement_DefinitionStatement, gen_syntax_ddl_CreateIndexStatement_DefinitionStatement, gen_syntax_ddl_RollbackStatement_DefinitionStatement, gen_syntax_ddl_SetConnectionStatement_DefinitionStatement, gen_syntax_dml_ExtendedQuerySelect_dml_ExtendedQueryExpressionBody, gen_syntax_dml_ExtendedQuerySelect_QuerySelect, gen_syntax_dml_ExtendedQueryExpressionBody_QueryExpressionBody, gen_syntax_dbl_DeclareCursorStatement_BindingStatement, gen_syntax_dbl_DescribeStatement_BindingStatement, gen_syntax_ddl_LockTableStatement_DefinitionStatement, gen_syntax_ddl_ReleaseStatement_DefinitionStatement, gen_syntax_ddl_RenameStatement_DefinitionStatement, gen_syntax_dbl_FetchStatement_BindingStatement, gen_syntax_dbl_SetTransactionStatement_BindingStatement, gen_syntax_dbl_ExecuteImmediateStatement_BindingStatement, gen_syntax_dbl_ExecuteStatement_BindingStatement, gen_syntax_dbl_PrepareStatement_BindingStatement, gen_syntax_dbl_CloseStatement_BindingStatement, gen_syntax_dbl_OpenStatement_BindingStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)