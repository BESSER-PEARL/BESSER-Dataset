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

DescriptorScope: Enumeration = Enumeration(
    name="DescriptorScope",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="GLOBAL")
    }
)

FetchPosition: Enumeration = Enumeration(
    name="FetchPosition",
    literals={
            EnumerationLiteral(name="NEXT"),
			EnumerationLiteral(name="PRIOR"),
			EnumerationLiteral(name="FIRST"),
			EnumerationLiteral(name="LAST"),
			EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="CURRENT"),
			EnumerationLiteral(name="RELATIVE")
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
syntax_AliasResolver = Class(name="syntax_AliasResolver", is_abstract=True)
syntax_BindingParseError = Class(name="syntax_BindingParseError")
syntax_BindingParser = Class(name="syntax_BindingParser", is_abstract=True)
StatementParser = Class(name="StatementParser")
syntax_BindingParserRegistry = Class(name="syntax_BindingParserRegistry", is_abstract=True)
syntax_BindingParseResult = Class(name="syntax_BindingParseResult")
syntax_BindingStatement = Class(name="syntax_BindingStatement", is_abstract=True)
syntax_DefinitionParser = Class(name="syntax_DefinitionParser", is_abstract=True)
syntax_DefinitionParserRegistry = Class(name="syntax_DefinitionParserRegistry", is_abstract=True)
syntax_DefinitionParseError = Class(name="syntax_DefinitionParseError")
syntax_DefinitionParseResult = Class(name="syntax_DefinitionParseResult")
syntax_DefinitionStatement = Class(name="syntax_DefinitionStatement", is_abstract=True)
syntax_DefinitionWriter = Class(name="syntax_DefinitionWriter", is_abstract=True)
StatementWriter = Class(name="StatementWriter")
syntax_DefinitionWriterRegistry = Class(name="syntax_DefinitionWriterRegistry", is_abstract=True)
syntax_NameHelper = Class(name="syntax_NameHelper", is_abstract=True)
SQLObjectNameHelper = Class(name="SQLObjectNameHelper")
syntax_NameHelperRegistry = Class(name="syntax_NameHelperRegistry", is_abstract=True)
syntax_QueryWriter = Class(name="syntax_QueryWriter", is_abstract=True)
syntax_QueryWriterRegistry = Class(name="syntax_QueryWriterRegistry", is_abstract=True)
syntax_QueryParser = Class(name="syntax_QueryParser", is_abstract=True)
syntax_QueryParserRegistry = Class(name="syntax_QueryParserRegistry", is_abstract=True)
syntax_SQLObjectNameHelper = Class(name="syntax_SQLObjectNameHelper", is_abstract=True)
syntax_StatementWriter = Class(name="syntax_StatementWriter", is_abstract=True)
syntax_StatementParser = Class(name="syntax_StatementParser", is_abstract=True)
syntax_ddl_CallStatement = Class(name="syntax_ddl_CallStatement")
DefinitionStatement = Class(name="DefinitionStatement")
ddl_syntax_QualifiedName = Class(name="ddl_syntax_QualifiedName")
syntax_ddl_CommitStatement = Class(name="syntax_ddl_CommitStatement")
syntax_ddl_ConnectStatement = Class(name="syntax_ddl_ConnectStatement")
syntax_ddl_CreateAliasStatement = Class(name="syntax_ddl_CreateAliasStatement")
syntax_ddl_CreateIndexStatement = Class(name="syntax_ddl_CreateIndexStatement")
syntax_ddl_LockTableStatement = Class(name="syntax_ddl_LockTableStatement")
ddl_syntax_IndexDef = Class(name="ddl_syntax_IndexDef")
syntax_ddl_CreateTableStatement = Class(name="syntax_ddl_CreateTableStatement")
ddl_syntax_TableColumnDef = Class(name="ddl_syntax_TableColumnDef")
syntax_ddl_CreateViewStatement = Class(name="syntax_ddl_CreateViewStatement")
syntax_ddl_DisconnectStatement = Class(name="syntax_ddl_DisconnectStatement")
syntax_ddl_DropStatement = Class(name="syntax_ddl_DropStatement")
syntax_ddl_ReleaseStatement = Class(name="syntax_ddl_ReleaseStatement")
syntax_ddl_RenameStatement = Class(name="syntax_ddl_RenameStatement")
syntax_ddl_RollbackStatement = Class(name="syntax_ddl_RollbackStatement")
syntax_ddl_SetConnectionStatement = Class(name="syntax_ddl_SetConnectionStatement")
syntax_dml_ExtendedQuerySelect = Class(name="syntax_dml_ExtendedQuerySelect")
dml_ExtendedQueryExpressionBody = Class(name="dml_ExtendedQueryExpressionBody")
QuerySelect = Class(name="QuerySelect")
syntax_dml_ExtendedQueryExpressionBody = Class(name="syntax_dml_ExtendedQueryExpressionBody")
QueryExpressionBody = Class(name="QueryExpressionBody")
syntax_dbl_AllocateDescriptorStatement = Class(name="syntax_dbl_AllocateDescriptorStatement")
BindingStatement = Class(name="BindingStatement")
syntax_dbl_CloseStatement = Class(name="syntax_dbl_CloseStatement")
syntax_dbl_ConditionInfoClause = Class(name="syntax_dbl_ConditionInfoClause")
Option = Class(name="Option")
syntax_dbl_DeallocateDescriptorStatement = Class(name="syntax_dbl_DeallocateDescriptorStatement")
syntax_dbl_DeclareCursorStatement = Class(name="syntax_dbl_DeclareCursorStatement")
syntax_dbl_DescribeStatement = Class(name="syntax_dbl_DescribeStatement")
IntoClause = Class(name="IntoClause")
syntax_dbl_ExecuteImmediateStatement = Class(name="syntax_dbl_ExecuteImmediateStatement")
syntax_dbl_ExecuteStatement = Class(name="syntax_dbl_ExecuteStatement")
syntax_dbl_FetchStatement = Class(name="syntax_dbl_FetchStatement")
MultipleRowFetchClause = Class(name="MultipleRowFetchClause")
SingleRowFetchClause = Class(name="SingleRowFetchClause")
syntax_dbl_GetDescriptorStatement = Class(name="syntax_dbl_GetDescriptorStatement")
syntax_dbl_GetDiagnosticsStatement = Class(name="syntax_dbl_GetDiagnosticsStatement")
ConditionInfoClause = Class(name="ConditionInfoClause")
syntax_dbl_IntoClause = Class(name="syntax_dbl_IntoClause")
syntax_dbl_SingleRowFetchClause = Class(name="syntax_dbl_SingleRowFetchClause")
syntax_dbl_MultipleRowFetchClause = Class(name="syntax_dbl_MultipleRowFetchClause")
syntax_dbl_SetDescriptorStatement = Class(name="syntax_dbl_SetDescriptorStatement")
syntax_dbl_SetTransactionStatement = Class(name="syntax_dbl_SetTransactionStatement")
syntax_dbl_SetOptionStatement = Class(name="syntax_dbl_SetOptionStatement")
syntax_dbl_OpenStatement = Class(name="syntax_dbl_OpenStatement")
syntax_dbl_PrepareStatement = Class(name="syntax_dbl_PrepareStatement")
syntax_dbl_Option = Class(name="syntax_dbl_Option")

# syntax_AliasResolver class attributes and methods
syntax_AliasResolver_m_resolveQuery: Method = Method(name="resolveQuery", parameters={Parameter(name='syntax_connection', type=StringType), Parameter(name='syntax_query', type=StringType)})
syntax_AliasResolver.methods={syntax_AliasResolver_m_resolveQuery}

# syntax_BindingParseError class attributes and methods

# syntax_BindingParser class attributes and methods
syntax_BindingParser_m_parseBinding: Method = Method(name="parseBinding", parameters={Parameter(name='syntax_stream', type=StringType)}, type=StringType)
syntax_BindingParser_m_parseBinding: Method = Method(name="parseBinding", parameters={Parameter(name='syntax_sql', type=StringType)}, type=StringType)
syntax_BindingParser.methods={syntax_BindingParser_m_parseBinding, syntax_BindingParser_m_parseBinding}

# StatementParser class attributes and methods

# syntax_BindingParserRegistry class attributes and methods
syntax_BindingParserRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_BindingParserRegistry.methods={syntax_BindingParserRegistry_m_lookup}

# syntax_BindingParseResult class attributes and methods

# syntax_BindingStatement class attributes and methods
syntax_BindingStatement_m_getStatementType: Method = Method(name="getStatementType", parameters={}, type=StringType)
syntax_BindingStatement.methods={syntax_BindingStatement_m_getStatementType}

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
syntax_DefinitionWriter_m_copyTableData: Method = Method(name="copyTableData", parameters={Parameter(name='syntax_tableTo', type=StringType), Parameter(name='syntax_isCreateRelativeRecordNumber', type=StringType), Parameter(name='syntax_tableFrom', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_countRecords: Method = Method(name="countRecords", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createLabel: Method = Method(name="createLabel", parameters={Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_name', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createLabel: Method = Method(name="createLabel", parameters={Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_name', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createLabelForFields: Method = Method(name="createLabelForFields", parameters={Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_schema', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createSchema: Method = Method(name="createSchema", parameters={Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_schema', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createTable: Method = Method(name="createTable", parameters={Parameter(name='syntax_schema', type=StringType), Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_name', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createView: Method = Method(name="createView", parameters={Parameter(name='syntax_view', type=StringType), Parameter(name='syntax_name', type=StringType), Parameter(name='syntax_schema', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_createIndex: Method = Method(name="createIndex", parameters={Parameter(name='syntax_index', type=StringType), Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_name', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropSchema: Method = Method(name="dropSchema", parameters={Parameter(name='syntax_ignoreFailOnNonEmpty', type=StringType), Parameter(name='syntax_schema', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropTable: Method = Method(name="dropTable", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropView: Method = Method(name="dropView", parameters={Parameter(name='syntax_view', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_dropIndex: Method = Method(name="dropIndex", parameters={Parameter(name='syntax_index', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_deleteData: Method = Method(name="deleteData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_hasLogicals: Method = Method(name="hasLogicals", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_insertData: Method = Method(name="insertData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_insertData: Method = Method(name="insertData", parameters={Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_fieldNames', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_renameTable: Method = Method(name="renameTable", parameters={Parameter(name='syntax_table', type=StringType), Parameter(name='syntax_newName', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_renameIndex: Method = Method(name="renameIndex", parameters={Parameter(name='syntax_index', type=StringType), Parameter(name='syntax_newName', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_selectData: Method = Method(name="selectData", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter_m_truncateTable: Method = Method(name="truncateTable", parameters={Parameter(name='syntax_table', type=StringType)}, type=StringType)
syntax_DefinitionWriter.methods={syntax_DefinitionWriter_m_renameTable, syntax_DefinitionWriter_m_insertData, syntax_DefinitionWriter_m_countRecords, syntax_DefinitionWriter_m_renameIndex, syntax_DefinitionWriter_m_createTable, syntax_DefinitionWriter_m_selectData, syntax_DefinitionWriter_m_insertData, syntax_DefinitionWriter_m_createSchema, syntax_DefinitionWriter_m_dropSchema, syntax_DefinitionWriter_m_dropTable, syntax_DefinitionWriter_m_deleteData, syntax_DefinitionWriter_m_copyTableData, syntax_DefinitionWriter_m_createLabelForFields, syntax_DefinitionWriter_m_createView, syntax_DefinitionWriter_m_truncateTable, syntax_DefinitionWriter_m_createIndex, syntax_DefinitionWriter_m_dropIndex, syntax_DefinitionWriter_m_dropView, syntax_DefinitionWriter_m_hasLogicals, syntax_DefinitionWriter_m_createLabel, syntax_DefinitionWriter_m_createLabel}

# StatementWriter class attributes and methods

# syntax_DefinitionWriterRegistry class attributes and methods
syntax_DefinitionWriterRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_DefinitionWriterRegistry.methods={syntax_DefinitionWriterRegistry_m_lookup}

# syntax_NameHelper class attributes and methods
syntax_NameHelper_m_resolveContainers: Method = Method(name="resolveContainers", parameters={Parameter(name='syntax_query', type=StringType)})
syntax_NameHelper.methods={syntax_NameHelper_m_resolveContainers}

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

# syntax_QueryParser class attributes and methods
syntax_QueryParser_m_parseQuery: Method = Method(name="parseQuery", parameters={Parameter(name='syntax_stream', type=StringType)}, type=StringType)
syntax_QueryParser_m_parseQuery: Method = Method(name="parseQuery", parameters={Parameter(name='syntax_sql', type=StringType)}, type=StringType)
syntax_QueryParser.methods={syntax_QueryParser_m_parseQuery, syntax_QueryParser_m_parseQuery}

# syntax_QueryParserRegistry class attributes and methods
syntax_QueryParserRegistry_m_lookup: Method = Method(name="lookup", parameters={Parameter(name='syntax_connectionConfig', type=StringType)}, type=StringType)
syntax_QueryParserRegistry.methods={syntax_QueryParserRegistry_m_lookup}

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
syntax_ddl_ConnectStatement.attributes={syntax_ddl_ConnectStatement_user, syntax_ddl_ConnectStatement_to, syntax_ddl_ConnectStatement_reset, syntax_ddl_ConnectStatement_pwd}

# syntax_ddl_CreateAliasStatement class attributes and methods

# syntax_ddl_CreateIndexStatement class attributes and methods
syntax_ddl_CreateIndexStatement_unique: Property = Property(name="unique", type=BooleanType)
syntax_ddl_CreateIndexStatement.attributes={syntax_ddl_CreateIndexStatement_unique}

# syntax_ddl_LockTableStatement class attributes and methods
syntax_ddl_LockTableStatement_allowRead: Property = Property(name="allowRead", type=BooleanType)
syntax_ddl_LockTableStatement_shareMode: Property = Property(name="shareMode", type=StringType)
syntax_ddl_LockTableStatement.attributes={syntax_ddl_LockTableStatement_shareMode, syntax_ddl_LockTableStatement_allowRead}

# ddl_syntax_IndexDef class attributes and methods

# syntax_ddl_CreateTableStatement class attributes and methods

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

# syntax_ddl_ReleaseStatement class attributes and methods
syntax_ddl_ReleaseStatement_serverName: Property = Property(name="serverName", type=StringType)
syntax_ddl_ReleaseStatement.attributes={syntax_ddl_ReleaseStatement_serverName}

# syntax_ddl_RenameStatement class attributes and methods
syntax_ddl_RenameStatement_newName: Property = Property(name="newName", type=StringType)
syntax_ddl_RenameStatement_system: Property = Property(name="system", type=StringType)
syntax_ddl_RenameStatement_target: Property = Property(name="target", type=StringType)
syntax_ddl_RenameStatement.attributes={syntax_ddl_RenameStatement_target, syntax_ddl_RenameStatement_system, syntax_ddl_RenameStatement_newName}

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

# syntax_dbl_AllocateDescriptorStatement class attributes and methods
syntax_dbl_AllocateDescriptorStatement_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_AllocateDescriptorStatement_descriptorScope: Property = Property(name="descriptorScope", type=StringType)
syntax_dbl_AllocateDescriptorStatement_withMax: Property = Property(name="withMax", type=StringType)
syntax_dbl_AllocateDescriptorStatement.attributes={syntax_dbl_AllocateDescriptorStatement_descriptorScope, syntax_dbl_AllocateDescriptorStatement_descriptorName, syntax_dbl_AllocateDescriptorStatement_withMax}

# BindingStatement class attributes and methods

# syntax_dbl_CloseStatement class attributes and methods
syntax_dbl_CloseStatement_cursor: Property = Property(name="cursor", type=StringType)
syntax_dbl_CloseStatement.attributes={syntax_dbl_CloseStatement_cursor}

# syntax_dbl_ConditionInfoClause class attributes and methods
syntax_dbl_ConditionInfoClause_condition: Property = Property(name="condition", type=StringType)
syntax_dbl_ConditionInfoClause.attributes={syntax_dbl_ConditionInfoClause_condition}

# Option class attributes and methods

# syntax_dbl_DeallocateDescriptorStatement class attributes and methods
syntax_dbl_DeallocateDescriptorStatement_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_DeallocateDescriptorStatement_descriptorScope: Property = Property(name="descriptorScope", type=StringType)
syntax_dbl_DeallocateDescriptorStatement.attributes={syntax_dbl_DeallocateDescriptorStatement_descriptorName, syntax_dbl_DeallocateDescriptorStatement_descriptorScope}

# syntax_dbl_DeclareCursorStatement class attributes and methods
syntax_dbl_DeclareCursorStatement_cursorName: Property = Property(name="cursorName", type=StringType)
syntax_dbl_DeclareCursorStatement_cursorType: Property = Property(name="cursorType", type=StringType)
syntax_dbl_DeclareCursorStatement_forQuery: Property = Property(name="forQuery", type=StringType)
syntax_dbl_DeclareCursorStatement_forStatementName: Property = Property(name="forStatementName", type=StringType)
syntax_dbl_DeclareCursorStatement_hold: Property = Property(name="hold", type=BooleanType)
syntax_dbl_DeclareCursorStatement.attributes={syntax_dbl_DeclareCursorStatement_hold, syntax_dbl_DeclareCursorStatement_cursorName, syntax_dbl_DeclareCursorStatement_cursorType, syntax_dbl_DeclareCursorStatement_forStatementName, syntax_dbl_DeclareCursorStatement_forQuery}

# syntax_dbl_DescribeStatement class attributes and methods
syntax_dbl_DescribeStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_DescribeStatement.attributes={syntax_dbl_DescribeStatement_statementName}

# IntoClause class attributes and methods

# syntax_dbl_ExecuteImmediateStatement class attributes and methods
syntax_dbl_ExecuteImmediateStatement_variable: Property = Property(name="variable", type=StringType)
syntax_dbl_ExecuteImmediateStatement.attributes={syntax_dbl_ExecuteImmediateStatement_variable}

# syntax_dbl_ExecuteStatement class attributes and methods
syntax_dbl_ExecuteStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_ExecuteStatement.attributes={syntax_dbl_ExecuteStatement_statementName}

# syntax_dbl_FetchStatement class attributes and methods
syntax_dbl_FetchStatement_cursorName: Property = Property(name="cursorName", type=StringType)
syntax_dbl_FetchStatement_position: Property = Property(name="position", type=StringType)
syntax_dbl_FetchStatement_relativePosition: Property = Property(name="relativePosition", type=StringType)
syntax_dbl_FetchStatement.attributes={syntax_dbl_FetchStatement_relativePosition, syntax_dbl_FetchStatement_cursorName, syntax_dbl_FetchStatement_position}

# MultipleRowFetchClause class attributes and methods

# SingleRowFetchClause class attributes and methods

# syntax_dbl_GetDescriptorStatement class attributes and methods
syntax_dbl_GetDescriptorStatement_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_GetDescriptorStatement_descriptorScope: Property = Property(name="descriptorScope", type=StringType)
syntax_dbl_GetDescriptorStatement_value: Property = Property(name="value", type=StringType)
syntax_dbl_GetDescriptorStatement.attributes={syntax_dbl_GetDescriptorStatement_value, syntax_dbl_GetDescriptorStatement_descriptorScope, syntax_dbl_GetDescriptorStatement_descriptorName}

# syntax_dbl_GetDiagnosticsStatement class attributes and methods

# ConditionInfoClause class attributes and methods

# syntax_dbl_IntoClause class attributes and methods
syntax_dbl_IntoClause_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_IntoClause_using: Property = Property(name="using", type=StringType)
syntax_dbl_IntoClause.attributes={syntax_dbl_IntoClause_using, syntax_dbl_IntoClause_descriptorName}

# syntax_dbl_SingleRowFetchClause class attributes and methods
syntax_dbl_SingleRowFetchClause_into: Property = Property(name="into", type=StringType)
syntax_dbl_SingleRowFetchClause_usingDescriptor: Property = Property(name="usingDescriptor", type=BooleanType)
syntax_dbl_SingleRowFetchClause.attributes={syntax_dbl_SingleRowFetchClause_usingDescriptor, syntax_dbl_SingleRowFetchClause_into}

# syntax_dbl_MultipleRowFetchClause class attributes and methods
syntax_dbl_MultipleRowFetchClause_into: Property = Property(name="into", type=StringType)
syntax_dbl_MultipleRowFetchClause_rowsNumber: Property = Property(name="rowsNumber", type=StringType)
syntax_dbl_MultipleRowFetchClause_usingDescriptor: Property = Property(name="usingDescriptor", type=BooleanType)
syntax_dbl_MultipleRowFetchClause_descriptor: Property = Property(name="descriptor", type=StringType)
syntax_dbl_MultipleRowFetchClause.attributes={syntax_dbl_MultipleRowFetchClause_into, syntax_dbl_MultipleRowFetchClause_rowsNumber, syntax_dbl_MultipleRowFetchClause_usingDescriptor, syntax_dbl_MultipleRowFetchClause_descriptor}

# syntax_dbl_SetDescriptorStatement class attributes and methods
syntax_dbl_SetDescriptorStatement_descriptorName: Property = Property(name="descriptorName", type=StringType)
syntax_dbl_SetDescriptorStatement_value: Property = Property(name="value", type=StringType)
syntax_dbl_SetDescriptorStatement.attributes={syntax_dbl_SetDescriptorStatement_value, syntax_dbl_SetDescriptorStatement_descriptorName}

# syntax_dbl_SetTransactionStatement class attributes and methods
syntax_dbl_SetTransactionStatement_isolationLevel: Property = Property(name="isolationLevel", type=StringType)
syntax_dbl_SetTransactionStatement_rwOperation: Property = Property(name="rwOperation", type=StringType)
syntax_dbl_SetTransactionStatement.attributes={syntax_dbl_SetTransactionStatement_rwOperation, syntax_dbl_SetTransactionStatement_isolationLevel}

# syntax_dbl_SetOptionStatement class attributes and methods

# syntax_dbl_OpenStatement class attributes and methods
syntax_dbl_OpenStatement_cursor: Property = Property(name="cursor", type=StringType)
syntax_dbl_OpenStatement_using: Property = Property(name="using", type=StringType)
syntax_dbl_OpenStatement_usingType: Property = Property(name="usingType", type=StringType)
syntax_dbl_OpenStatement.attributes={syntax_dbl_OpenStatement_using, syntax_dbl_OpenStatement_cursor, syntax_dbl_OpenStatement_usingType}

# syntax_dbl_PrepareStatement class attributes and methods
syntax_dbl_PrepareStatement_from_: Property = Property(name="from_", type=StringType)
syntax_dbl_PrepareStatement_statementName: Property = Property(name="statementName", type=StringType)
syntax_dbl_PrepareStatement.attributes={syntax_dbl_PrepareStatement_from_, syntax_dbl_PrepareStatement_statementName}

# syntax_dbl_Option class attributes and methods
syntax_dbl_Option_name: Property = Property(name="name", type=StringType)
syntax_dbl_Option_value: Property = Property(name="value", type=StringType)
syntax_dbl_Option.attributes={syntax_dbl_Option_value, syntax_dbl_Option_name}

# Relationships
bindingStatement0: BinaryAssociation = BinaryAssociation(
    name="bindingStatement0",
    ends={
        Property(name="syntax_BindingStatement", type=syntax_BindingParseResult, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_BindingParseResult", type=syntax_BindingStatement, multiplicity=Multiplicity(0, 1))
    }
)
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
indexName13: BinaryAssociation = BinaryAssociation(
    name="indexName13",
    ends={
        Property(name="syntax_ddl_CreateIndexStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ddl_syntax_QualifiedName14", type=syntax_ddl_CreateIndexStatement, multiplicity=Multiplicity(1, 1))
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
tableName28: BinaryAssociation = BinaryAssociation(
    name="tableName28",
    ends={
        Property(name="ddl_syntax_QualifiedName29", type=syntax_ddl_LockTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_LockTableStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalName30: BinaryAssociation = BinaryAssociation(
    name="originalName30",
    ends={
        Property(name="ddl_syntax_QualifiedName31", type=syntax_ddl_RenameStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_ddl_RenameStatement", type=ddl_syntax_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionItems32: BinaryAssociation = BinaryAssociation(
    name="conditionItems32",
    ends={
        Property(name="Option", type=syntax_dbl_ConditionInfoClause, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_ConditionInfoClause", type=Option, multiplicity=Multiplicity(0, 9999))
    }
)
into33: BinaryAssociation = BinaryAssociation(
    name="into33",
    ends={
        Property(name="IntoClause", type=syntax_dbl_DescribeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_DescribeStatement", type=IntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipleRowClause34: BinaryAssociation = BinaryAssociation(
    name="multipleRowClause34",
    ends={
        Property(name="MultipleRowFetchClause", type=syntax_dbl_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_FetchStatement", type=MultipleRowFetchClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleRowClause35: BinaryAssociation = BinaryAssociation(
    name="singleRowClause35",
    ends={
        Property(name="SingleRowFetchClause", type=syntax_dbl_FetchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_FetchStatement36", type=SingleRowFetchClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables37: BinaryAssociation = BinaryAssociation(
    name="variables37",
    ends={
        Property(name="Option38", type=syntax_dbl_GetDescriptorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_GetDescriptorStatement", type=Option, multiplicity=Multiplicity(0, 9999))
    }
)
conditionInfo39: BinaryAssociation = BinaryAssociation(
    name="conditionInfo39",
    ends={
        Property(name="ConditionInfoClause", type=syntax_dbl_GetDiagnosticsStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_GetDiagnosticsStatement", type=ConditionInfoClause, multiplicity=Multiplicity(0, 1))
    }
)
items40: BinaryAssociation = BinaryAssociation(
    name="items40",
    ends={
        Property(name="Option41", type=syntax_dbl_SetDescriptorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_SetDescriptorStatement", type=Option, multiplicity=Multiplicity(0, 9999))
    }
)
options42: BinaryAssociation = BinaryAssociation(
    name="options42",
    ends={
        Property(name="Option43", type=syntax_dbl_SetOptionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_SetOptionStatement", type=Option, multiplicity=Multiplicity(0, 9999))
    }
)
into44: BinaryAssociation = BinaryAssociation(
    name="into44",
    ends={
        Property(name="IntoClause45", type=syntax_dbl_PrepareStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="syntax_dbl_PrepareStatement", type=IntoClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_syntax_BindingParser_StatementParser = Generalization(general=StatementParser, specific=syntax_BindingParser)
gen_syntax_DefinitionParser_StatementParser = Generalization(general=StatementParser, specific=syntax_DefinitionParser)
gen_syntax_DefinitionWriter_StatementWriter = Generalization(general=StatementWriter, specific=syntax_DefinitionWriter)
gen_syntax_NameHelper_SQLObjectNameHelper = Generalization(general=SQLObjectNameHelper, specific=syntax_NameHelper)
gen_syntax_QueryWriter_StatementWriter = Generalization(general=StatementWriter, specific=syntax_QueryWriter)
gen_syntax_QueryParser_StatementParser = Generalization(general=StatementParser, specific=syntax_QueryParser)
gen_syntax_ddl_CallStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CallStatement)
gen_syntax_ddl_CommitStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CommitStatement)
gen_syntax_ddl_ConnectStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_ConnectStatement)
gen_syntax_ddl_CreateAliasStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateAliasStatement)
gen_syntax_ddl_CreateIndexStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateIndexStatement)
gen_syntax_ddl_LockTableStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_LockTableStatement)
gen_syntax_ddl_CreateTableStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateTableStatement)
gen_syntax_ddl_CreateViewStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_CreateViewStatement)
gen_syntax_ddl_DisconnectStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_DisconnectStatement)
gen_syntax_ddl_DropStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_DropStatement)
gen_syntax_ddl_ReleaseStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_ReleaseStatement)
gen_syntax_ddl_RenameStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_RenameStatement)
gen_syntax_ddl_RollbackStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_RollbackStatement)
gen_syntax_ddl_SetConnectionStatement_DefinitionStatement = Generalization(general=DefinitionStatement, specific=syntax_ddl_SetConnectionStatement)
gen_syntax_dml_ExtendedQuerySelect_dml_ExtendedQueryExpressionBody = Generalization(general=dml_ExtendedQueryExpressionBody, specific=syntax_dml_ExtendedQuerySelect)
gen_syntax_dml_ExtendedQuerySelect_QuerySelect = Generalization(general=QuerySelect, specific=syntax_dml_ExtendedQuerySelect)
gen_syntax_dml_ExtendedQueryExpressionBody_QueryExpressionBody = Generalization(general=QueryExpressionBody, specific=syntax_dml_ExtendedQueryExpressionBody)
gen_syntax_dbl_AllocateDescriptorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_AllocateDescriptorStatement)
gen_syntax_dbl_CloseStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_CloseStatement)
gen_syntax_dbl_DeallocateDescriptorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_DeallocateDescriptorStatement)
gen_syntax_dbl_DeclareCursorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_DeclareCursorStatement)
gen_syntax_dbl_DescribeStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_DescribeStatement)
gen_syntax_dbl_ExecuteImmediateStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_ExecuteImmediateStatement)
gen_syntax_dbl_ExecuteStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_ExecuteStatement)
gen_syntax_dbl_FetchStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_FetchStatement)
gen_syntax_dbl_GetDescriptorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_GetDescriptorStatement)
gen_syntax_dbl_GetDiagnosticsStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_GetDiagnosticsStatement)
gen_syntax_dbl_SetDescriptorStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_SetDescriptorStatement)
gen_syntax_dbl_SetTransactionStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_SetTransactionStatement)
gen_syntax_dbl_SetOptionStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_SetOptionStatement)
gen_syntax_dbl_OpenStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_OpenStatement)
gen_syntax_dbl_PrepareStatement_BindingStatement = Generalization(general=BindingStatement, specific=syntax_dbl_PrepareStatement)

# Domain Model
domain_model = DomainModel(
    name="syntax",
    types={syntax_AliasResolver, syntax_BindingParseError, syntax_BindingParser, StatementParser, syntax_BindingParserRegistry, syntax_BindingParseResult, syntax_BindingStatement, syntax_DefinitionParser, syntax_DefinitionParserRegistry, syntax_DefinitionParseError, syntax_DefinitionParseResult, syntax_DefinitionStatement, syntax_DefinitionWriter, StatementWriter, syntax_DefinitionWriterRegistry, syntax_NameHelper, SQLObjectNameHelper, syntax_NameHelperRegistry, syntax_QueryWriter, syntax_QueryWriterRegistry, syntax_QueryParser, syntax_QueryParserRegistry, syntax_SQLObjectNameHelper, syntax_StatementWriter, syntax_StatementParser, syntax_ddl_CallStatement, DefinitionStatement, ddl_syntax_QualifiedName, syntax_ddl_CommitStatement, syntax_ddl_ConnectStatement, syntax_ddl_CreateAliasStatement, syntax_ddl_CreateIndexStatement, syntax_ddl_LockTableStatement, ddl_syntax_IndexDef, syntax_ddl_CreateTableStatement, ddl_syntax_TableColumnDef, syntax_ddl_CreateViewStatement, syntax_ddl_DisconnectStatement, syntax_ddl_DropStatement, syntax_ddl_ReleaseStatement, syntax_ddl_RenameStatement, syntax_ddl_RollbackStatement, syntax_ddl_SetConnectionStatement, syntax_dml_ExtendedQuerySelect, dml_ExtendedQueryExpressionBody, QuerySelect, syntax_dml_ExtendedQueryExpressionBody, QueryExpressionBody, syntax_dbl_AllocateDescriptorStatement, BindingStatement, syntax_dbl_CloseStatement, syntax_dbl_ConditionInfoClause, Option, syntax_dbl_DeallocateDescriptorStatement, syntax_dbl_DeclareCursorStatement, syntax_dbl_DescribeStatement, IntoClause, syntax_dbl_ExecuteImmediateStatement, syntax_dbl_ExecuteStatement, syntax_dbl_FetchStatement, MultipleRowFetchClause, SingleRowFetchClause, syntax_dbl_GetDescriptorStatement, syntax_dbl_GetDiagnosticsStatement, ConditionInfoClause, syntax_dbl_IntoClause, syntax_dbl_SingleRowFetchClause, syntax_dbl_MultipleRowFetchClause, syntax_dbl_SetDescriptorStatement, syntax_dbl_SetTransactionStatement, syntax_dbl_SetOptionStatement, syntax_dbl_OpenStatement, syntax_dbl_PrepareStatement, syntax_dbl_Option, StatementType, DropRange, TargetElement, ShareMode, TargetItem, CursorType, DescriptorScope, FetchPosition, IsolationLevel, RWOperation, OpenUsingType, UsingType},
    associations={bindingStatement0, errorList1, definitionStatement3, errorList4, nameHelper6, procedureName7, aliasName8, tableName10, indexName13, onTable15, sortBy18, tableName20, fields22, viewName24, targetName26, tableName28, originalName30, conditionItems32, into33, multipleRowClause34, singleRowClause35, variables37, conditionInfo39, items40, options42, into44},
    generalizations={gen_syntax_BindingParser_StatementParser, gen_syntax_DefinitionParser_StatementParser, gen_syntax_DefinitionWriter_StatementWriter, gen_syntax_NameHelper_SQLObjectNameHelper, gen_syntax_QueryWriter_StatementWriter, gen_syntax_QueryParser_StatementParser, gen_syntax_ddl_CallStatement_DefinitionStatement, gen_syntax_ddl_CommitStatement_DefinitionStatement, gen_syntax_ddl_ConnectStatement_DefinitionStatement, gen_syntax_ddl_CreateAliasStatement_DefinitionStatement, gen_syntax_ddl_CreateIndexStatement_DefinitionStatement, gen_syntax_ddl_LockTableStatement_DefinitionStatement, gen_syntax_ddl_CreateTableStatement_DefinitionStatement, gen_syntax_ddl_CreateViewStatement_DefinitionStatement, gen_syntax_ddl_DisconnectStatement_DefinitionStatement, gen_syntax_ddl_DropStatement_DefinitionStatement, gen_syntax_ddl_ReleaseStatement_DefinitionStatement, gen_syntax_ddl_RenameStatement_DefinitionStatement, gen_syntax_ddl_RollbackStatement_DefinitionStatement, gen_syntax_ddl_SetConnectionStatement_DefinitionStatement, gen_syntax_dml_ExtendedQuerySelect_dml_ExtendedQueryExpressionBody, gen_syntax_dml_ExtendedQuerySelect_QuerySelect, gen_syntax_dml_ExtendedQueryExpressionBody_QueryExpressionBody, gen_syntax_dbl_AllocateDescriptorStatement_BindingStatement, gen_syntax_dbl_CloseStatement_BindingStatement, gen_syntax_dbl_DeallocateDescriptorStatement_BindingStatement, gen_syntax_dbl_DeclareCursorStatement_BindingStatement, gen_syntax_dbl_DescribeStatement_BindingStatement, gen_syntax_dbl_ExecuteImmediateStatement_BindingStatement, gen_syntax_dbl_ExecuteStatement_BindingStatement, gen_syntax_dbl_FetchStatement_BindingStatement, gen_syntax_dbl_GetDescriptorStatement_BindingStatement, gen_syntax_dbl_GetDiagnosticsStatement_BindingStatement, gen_syntax_dbl_SetDescriptorStatement_BindingStatement, gen_syntax_dbl_SetTransactionStatement_BindingStatement, gen_syntax_dbl_SetOptionStatement_BindingStatement, gen_syntax_dbl_OpenStatement_BindingStatement, gen_syntax_dbl_PrepareStatement_BindingStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)