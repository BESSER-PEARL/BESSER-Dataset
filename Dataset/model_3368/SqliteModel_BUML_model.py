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
CompoundOperator: Enumeration = Enumeration(
    name="CompoundOperator",
    literals={
            EnumerationLiteral(name="unionall"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="intersect"),
			EnumerationLiteral(name="except")
    }
)

SqliteDataType: Enumeration = Enumeration(
    name="SqliteDataType",
    literals={
            EnumerationLiteral(name="text"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="real"),
			EnumerationLiteral(name="blob"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="numeric")
    }
)

ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="text"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="real"),
			EnumerationLiteral(name="blob"),
			EnumerationLiteral(name="boolean")
    }
)

ConflictResolution: Enumeration = Enumeration(
    name="ConflictResolution",
    literals={
            EnumerationLiteral(name="rollback"),
			EnumerationLiteral(name="abort"),
			EnumerationLiteral(name="fail"),
			EnumerationLiteral(name="ignore"),
			EnumerationLiteral(name="replace")
    }
)

# Classes
sqliteModel_InitBlock = Class(name="sqliteModel::InitBlock")
sqliteModel_MigrationBlock = Class(name="sqliteModel::MigrationBlock")
sqliteModel_ConfigurationStatement = Class(name="sqliteModel::ConfigurationStatement")
sqliteModel_DDLStatement = Class(name="sqliteModel::DDLStatement")
sqliteModel_FunctionArg = Class(name="sqliteModel::FunctionArg")
sqliteModel_ContentUri = Class(name="sqliteModel::ContentUri")
sqliteModel_ContentUriSegment = Class(name="sqliteModel::ContentUriSegment")
sqliteModel_Model = Class(name="sqliteModel::Model")
sqliteModel_DatabaseBlock = Class(name="sqliteModel::DatabaseBlock")
sqliteModel_ConfigBlock = Class(name="sqliteModel::ConfigBlock")
sqliteModel_WhereExpressions = Class(name="sqliteModel::WhereExpressions")
sqliteModel_GroupByExpressions = Class(name="sqliteModel::GroupByExpressions")
sqliteModel_HavingExpressions = Class(name="sqliteModel::HavingExpressions")
sqliteModel_JoinSource = Class(name="sqliteModel::JoinSource")
sqliteModel_SingleSource = Class(name="sqliteModel::SingleSource")
sqliteModel_JoinStatement = Class(name="sqliteModel::JoinStatement")
sqliteModel_Expression = Class(name="sqliteModel::Expression")
sqliteModel_Case = Class(name="sqliteModel::Case")
sqliteModel_SelectStatement = Class(name="sqliteModel::SelectStatement")
DMLStatement = Class(name="DMLStatement")
sqliteModel_SelectCoreExpression = Class(name="sqliteModel::SelectCoreExpression")
sqliteModel_OrderingTermList = Class(name="sqliteModel::OrderingTermList")
sqliteModel_OrderingTerm = Class(name="sqliteModel::OrderingTerm")
sqliteModel_SelectList = Class(name="sqliteModel::SelectList")
sqliteModel_ColumnSource = Class(name="sqliteModel::ColumnSource")
sqliteModel_TableDefinition = Class(name="sqliteModel::TableDefinition")
DDLStatement = Class(name="DDLStatement")
sqliteModel_CreateTriggerStatement = Class(name="sqliteModel::CreateTriggerStatement")
sqliteModel_DMLStatement = Class(name="sqliteModel::DMLStatement")
sqliteModel_AlterTableAddColumnStatement = Class(name="sqliteModel::AlterTableAddColumnStatement")
sqliteModel_DropTableStatement = Class(name="sqliteModel::DropTableStatement")
sqliteModel_SelectSource = Class(name="sqliteModel::SelectSource")
SingleSource = Class(name="SingleSource")
sqliteModel_SingleSourceJoin = Class(name="sqliteModel::SingleSourceJoin")
sqliteModel_LiteralValue = Class(name="sqliteModel::LiteralValue")
sqliteModel_ColumnConstraint = Class(name="sqliteModel::ColumnConstraint")
sqliteModel_TableConstraint = Class(name="sqliteModel::TableConstraint")
sqliteModel_UniqueTableConstraint = Class(name="sqliteModel::UniqueTableConstraint")
TableConstraint = Class(name="TableConstraint")
sqliteModel_ConflictClause = Class(name="sqliteModel::ConflictClause")
sqliteModel_PrimaryConstraint = Class(name="sqliteModel::PrimaryConstraint")
sqliteModel_CheckTableConstraint = Class(name="sqliteModel::CheckTableConstraint")
sqliteModel_ColumnDef = Class(name="sqliteModel::ColumnDef")
sqliteModel_DefaultValue = Class(name="sqliteModel::DefaultValue")
sqliteModel_DropTriggerStatement = Class(name="sqliteModel::DropTriggerStatement")
sqliteModel_DropViewStatement = Class(name="sqliteModel::DropViewStatement")
sqliteModel_CreateViewStatement = Class(name="sqliteModel::CreateViewStatement")
sqliteModel_CreateIndexStatement = Class(name="sqliteModel::CreateIndexStatement")
sqliteModel_IndexedColumn = Class(name="sqliteModel::IndexedColumn")
sqliteModel_DropIndexStatement = Class(name="sqliteModel::DropIndexStatement")
sqliteModel_UpdateStatement = Class(name="sqliteModel::UpdateStatement")
sqliteModel_UpdateColumnExpression = Class(name="sqliteModel::UpdateColumnExpression")
sqliteModel_ActionStatement = Class(name="sqliteModel::ActionStatement")
ConfigurationStatement = Class(name="ConfigurationStatement")
sqliteModel_DeleteStatement = Class(name="sqliteModel::DeleteStatement")
sqliteModel_InsertStatement = Class(name="sqliteModel::InsertStatement")
sqliteModel_ContentUriParamSegment = Class(name="sqliteModel::ContentUriParamSegment")
ContentUriSegment = Class(name="ContentUriSegment")
sqliteModel_Function = Class(name="sqliteModel::Function")
Expression = Class(name="Expression")
sqliteModel_ExprMult = Class(name="sqliteModel::ExprMult")
sqliteModel_ExprAdd = Class(name="sqliteModel::ExprAdd")
sqliteModel_ExprConcat = Class(name="sqliteModel::ExprConcat")
sqliteModel_ExprRelate = Class(name="sqliteModel::ExprRelate")
sqliteModel_ExprBit = Class(name="sqliteModel::ExprBit")
sqliteModel_ExprAnd = Class(name="sqliteModel::ExprAnd")
sqliteModel_ExprOr = Class(name="sqliteModel::ExprOr")
sqliteModel_ExprEqual = Class(name="sqliteModel::ExprEqual")
sqliteModel_NullCheckExpression = Class(name="sqliteModel::NullCheckExpression")
sqliteModel_IsNull = Class(name="sqliteModel::IsNull")
sqliteModel_NotNull = Class(name="sqliteModel::NotNull")
sqliteModel_NewColumn = Class(name="sqliteModel::NewColumn")
sqliteModel_Literal = Class(name="sqliteModel::Literal")
sqliteModel_NestedExpression = Class(name="sqliteModel::NestedExpression")
sqliteModel_OldColumn = Class(name="sqliteModel::OldColumn")
sqliteModel_ColumnSourceRef = Class(name="sqliteModel::ColumnSourceRef")
sqliteModel_CaseExpression = Class(name="sqliteModel::CaseExpression")
sqliteModel_CastExpression = Class(name="sqliteModel::CastExpression")
sqliteModel_SelectStatementExpression = Class(name="sqliteModel::SelectStatementExpression")
sqliteModel_SelectExpression = Class(name="sqliteModel::SelectExpression")
sqliteModel_FunctionArgument = Class(name="sqliteModel::FunctionArgument")
sqliteModel_SelectCore = Class(name="sqliteModel::SelectCore")
SelectCoreExpression = Class(name="SelectCoreExpression")
sqliteModel_ResultColumn = Class(name="sqliteModel::ResultColumn")
ColumnSource = Class(name="ColumnSource")
sqliteModel_NumericLiteral = Class(name="sqliteModel::NumericLiteral")
LiteralValue = Class(name="LiteralValue")
sqliteModel_StringLiteral = Class(name="sqliteModel::StringLiteral")
sqliteModel_NullLiteral = Class(name="sqliteModel::NullLiteral")
sqliteModel_SingleSourceTable = Class(name="sqliteModel::SingleSourceTable")
SelectSource = Class(name="SelectSource")
sqliteModel_SingleSourceSelectStatement = Class(name="sqliteModel::SingleSourceSelectStatement")
sqliteModel_CurrentDateLiteral = Class(name="sqliteModel::CurrentDateLiteral")
sqliteModel_CurrentTimeStampLiteral = Class(name="sqliteModel::CurrentTimeStampLiteral")
sqliteModel_CreateTableStatement = Class(name="sqliteModel::CreateTableStatement")
TableDefinition = Class(name="TableDefinition")
sqliteModel_CurrentTimeLiteral = Class(name="sqliteModel::CurrentTimeLiteral")
sqliteModel_AlterTableRenameStatement = Class(name="sqliteModel::AlterTableRenameStatement")
sqliteModel_UniqueConstraint = Class(name="sqliteModel::UniqueConstraint")
sqliteModel_DefaultConstraint = Class(name="sqliteModel::DefaultConstraint")
sqliteModel_LiteralDefaultValue = Class(name="sqliteModel::LiteralDefaultValue")
DefaultValue = Class(name="DefaultValue")
sqliteModel_PrimaryKeyColumnConstraint = Class(name="sqliteModel::PrimaryKeyColumnConstraint")
ColumnConstraint = Class(name="ColumnConstraint")
sqliteModel_NotNullConstraint = Class(name="sqliteModel::NotNullConstraint")
sqliteModel_ExpressionDefaultValue = Class(name="sqliteModel::ExpressionDefaultValue")

# sqliteModel_InitBlock class attributes and methods

# sqliteModel_MigrationBlock class attributes and methods

# sqliteModel_ConfigurationStatement class attributes and methods
sqliteModel_ConfigurationStatement_name: Property = Property(name="name", type=StringType)
sqliteModel_ConfigurationStatement.attributes={sqliteModel_ConfigurationStatement_name}

# sqliteModel_DDLStatement class attributes and methods

# sqliteModel_FunctionArg class attributes and methods
sqliteModel_FunctionArg_type: Property = Property(name="type", type=StringType)
sqliteModel_FunctionArg_name: Property = Property(name="name", type=StringType)
sqliteModel_FunctionArg.attributes={sqliteModel_FunctionArg_name, sqliteModel_FunctionArg_type}

# sqliteModel_ContentUri class attributes and methods
sqliteModel_ContentUri_type: Property = Property(name="type", type=StringType)
sqliteModel_ContentUri.attributes={sqliteModel_ContentUri_type}

# sqliteModel_ContentUriSegment class attributes and methods
sqliteModel_ContentUriSegment_name: Property = Property(name="name", type=StringType)
sqliteModel_ContentUriSegment.attributes={sqliteModel_ContentUriSegment_name}

# sqliteModel_Model class attributes and methods
sqliteModel_Model_packageName: Property = Property(name="packageName", type=StringType)
sqliteModel_Model.attributes={sqliteModel_Model_packageName}

# sqliteModel_DatabaseBlock class attributes and methods
sqliteModel_DatabaseBlock_name: Property = Property(name="name", type=StringType)
sqliteModel_DatabaseBlock.attributes={sqliteModel_DatabaseBlock_name}

# sqliteModel_ConfigBlock class attributes and methods

# sqliteModel_WhereExpressions class attributes and methods

# sqliteModel_GroupByExpressions class attributes and methods

# sqliteModel_HavingExpressions class attributes and methods

# sqliteModel_JoinSource class attributes and methods

# sqliteModel_SingleSource class attributes and methods

# sqliteModel_JoinStatement class attributes and methods
sqliteModel_JoinStatement_natural: Property = Property(name="natural", type=BooleanType)
sqliteModel_JoinStatement_left: Property = Property(name="left", type=BooleanType)
sqliteModel_JoinStatement_outer: Property = Property(name="outer", type=BooleanType)
sqliteModel_JoinStatement_inner: Property = Property(name="inner", type=BooleanType)
sqliteModel_JoinStatement_cross: Property = Property(name="cross", type=BooleanType)
sqliteModel_JoinStatement.attributes={sqliteModel_JoinStatement_left, sqliteModel_JoinStatement_cross, sqliteModel_JoinStatement_inner, sqliteModel_JoinStatement_outer, sqliteModel_JoinStatement_natural}

# sqliteModel_Expression class attributes and methods

# sqliteModel_Case class attributes and methods

# sqliteModel_SelectStatement class attributes and methods

# DMLStatement class attributes and methods

# sqliteModel_SelectCoreExpression class attributes and methods

# sqliteModel_OrderingTermList class attributes and methods

# sqliteModel_OrderingTerm class attributes and methods
sqliteModel_OrderingTerm_asc: Property = Property(name="asc", type=BooleanType)
sqliteModel_OrderingTerm_desc: Property = Property(name="desc", type=BooleanType)
sqliteModel_OrderingTerm.attributes={sqliteModel_OrderingTerm_asc, sqliteModel_OrderingTerm_desc}

# sqliteModel_SelectList class attributes and methods

# sqliteModel_ColumnSource class attributes and methods
sqliteModel_ColumnSource_name: Property = Property(name="name", type=StringType)
sqliteModel_ColumnSource.attributes={sqliteModel_ColumnSource_name}

# sqliteModel_TableDefinition class attributes and methods
sqliteModel_TableDefinition_name: Property = Property(name="name", type=StringType)
sqliteModel_TableDefinition.attributes={sqliteModel_TableDefinition_name}

# DDLStatement class attributes and methods

# sqliteModel_CreateTriggerStatement class attributes and methods
sqliteModel_CreateTriggerStatement_temporary: Property = Property(name="temporary", type=BooleanType)
sqliteModel_CreateTriggerStatement_name: Property = Property(name="name", type=StringType)
sqliteModel_CreateTriggerStatement_when: Property = Property(name="when", type=StringType)
sqliteModel_CreateTriggerStatement_eventType: Property = Property(name="eventType", type=StringType)
sqliteModel_CreateTriggerStatement_updateColumnNames: Property = Property(name="updateColumnNames", type=StringType)
sqliteModel_CreateTriggerStatement_forEachRow: Property = Property(name="forEachRow", type=StringType)
sqliteModel_CreateTriggerStatement.attributes={sqliteModel_CreateTriggerStatement_temporary, sqliteModel_CreateTriggerStatement_updateColumnNames, sqliteModel_CreateTriggerStatement_when, sqliteModel_CreateTriggerStatement_name, sqliteModel_CreateTriggerStatement_forEachRow, sqliteModel_CreateTriggerStatement_eventType}

# sqliteModel_DMLStatement class attributes and methods

# sqliteModel_AlterTableAddColumnStatement class attributes and methods

# sqliteModel_DropTableStatement class attributes and methods
sqliteModel_DropTableStatement_ifExists: Property = Property(name="ifExists", type=BooleanType)
sqliteModel_DropTableStatement.attributes={sqliteModel_DropTableStatement_ifExists}

# sqliteModel_SelectSource class attributes and methods
sqliteModel_SelectSource_name: Property = Property(name="name", type=StringType)
sqliteModel_SelectSource.attributes={sqliteModel_SelectSource_name}

# SingleSource class attributes and methods

# sqliteModel_SingleSourceJoin class attributes and methods

# sqliteModel_LiteralValue class attributes and methods

# sqliteModel_ColumnConstraint class attributes and methods

# sqliteModel_TableConstraint class attributes and methods
sqliteModel_TableConstraint_name: Property = Property(name="name", type=StringType)
sqliteModel_TableConstraint.attributes={sqliteModel_TableConstraint_name}

# sqliteModel_UniqueTableConstraint class attributes and methods

# TableConstraint class attributes and methods

# sqliteModel_ConflictClause class attributes and methods
sqliteModel_ConflictClause_resolution: Property = Property(name="resolution", type=StringType)
sqliteModel_ConflictClause.attributes={sqliteModel_ConflictClause_resolution}

# sqliteModel_PrimaryConstraint class attributes and methods

# sqliteModel_CheckTableConstraint class attributes and methods

# sqliteModel_ColumnDef class attributes and methods
sqliteModel_ColumnDef_type: Property = Property(name="type", type=StringType)
sqliteModel_ColumnDef.attributes={sqliteModel_ColumnDef_type}

# sqliteModel_DefaultValue class attributes and methods

# sqliteModel_DropTriggerStatement class attributes and methods
sqliteModel_DropTriggerStatement_ifExists: Property = Property(name="ifExists", type=BooleanType)
sqliteModel_DropTriggerStatement.attributes={sqliteModel_DropTriggerStatement_ifExists}

# sqliteModel_DropViewStatement class attributes and methods
sqliteModel_DropViewStatement_ifExists: Property = Property(name="ifExists", type=BooleanType)
sqliteModel_DropViewStatement.attributes={sqliteModel_DropViewStatement_ifExists}

# sqliteModel_CreateViewStatement class attributes and methods
sqliteModel_CreateViewStatement_temporary: Property = Property(name="temporary", type=BooleanType)
sqliteModel_CreateViewStatement.attributes={sqliteModel_CreateViewStatement_temporary}

# sqliteModel_CreateIndexStatement class attributes and methods
sqliteModel_CreateIndexStatement_unique: Property = Property(name="unique", type=BooleanType)
sqliteModel_CreateIndexStatement_name: Property = Property(name="name", type=StringType)
sqliteModel_CreateIndexStatement.attributes={sqliteModel_CreateIndexStatement_unique, sqliteModel_CreateIndexStatement_name}

# sqliteModel_IndexedColumn class attributes and methods
sqliteModel_IndexedColumn_collationName: Property = Property(name="collationName", type=StringType)
sqliteModel_IndexedColumn_asc: Property = Property(name="asc", type=BooleanType)
sqliteModel_IndexedColumn_desc: Property = Property(name="desc", type=BooleanType)
sqliteModel_IndexedColumn.attributes={sqliteModel_IndexedColumn_desc, sqliteModel_IndexedColumn_collationName, sqliteModel_IndexedColumn_asc}

# sqliteModel_DropIndexStatement class attributes and methods
sqliteModel_DropIndexStatement_ifExists: Property = Property(name="ifExists", type=BooleanType)
sqliteModel_DropIndexStatement.attributes={sqliteModel_DropIndexStatement_ifExists}

# sqliteModel_UpdateStatement class attributes and methods
sqliteModel_UpdateStatement_conflictResolution: Property = Property(name="conflictResolution", type=StringType)
sqliteModel_UpdateStatement.attributes={sqliteModel_UpdateStatement_conflictResolution}

# sqliteModel_UpdateColumnExpression class attributes and methods

# sqliteModel_ActionStatement class attributes and methods

# ConfigurationStatement class attributes and methods

# sqliteModel_DeleteStatement class attributes and methods

# sqliteModel_InsertStatement class attributes and methods
sqliteModel_InsertStatement_conflictResolution: Property = Property(name="conflictResolution", type=StringType)
sqliteModel_InsertStatement.attributes={sqliteModel_InsertStatement_conflictResolution}

# sqliteModel_ContentUriParamSegment class attributes and methods
sqliteModel_ContentUriParamSegment_num: Property = Property(name="num", type=BooleanType)
sqliteModel_ContentUriParamSegment_text: Property = Property(name="text", type=BooleanType)
sqliteModel_ContentUriParamSegment.attributes={sqliteModel_ContentUriParamSegment_text, sqliteModel_ContentUriParamSegment_num}

# ContentUriSegment class attributes and methods

# sqliteModel_Function class attributes and methods
sqliteModel_Function_all: Property = Property(name="all", type=BooleanType)
sqliteModel_Function.attributes={sqliteModel_Function_all}

# Expression class attributes and methods

# sqliteModel_ExprMult class attributes and methods
sqliteModel_ExprMult_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprMult.attributes={sqliteModel_ExprMult_op}

# sqliteModel_ExprAdd class attributes and methods
sqliteModel_ExprAdd_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprAdd.attributes={sqliteModel_ExprAdd_op}

# sqliteModel_ExprConcat class attributes and methods
sqliteModel_ExprConcat_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprConcat.attributes={sqliteModel_ExprConcat_op}

# sqliteModel_ExprRelate class attributes and methods
sqliteModel_ExprRelate_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprRelate.attributes={sqliteModel_ExprRelate_op}

# sqliteModel_ExprBit class attributes and methods
sqliteModel_ExprBit_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprBit.attributes={sqliteModel_ExprBit_op}

# sqliteModel_ExprAnd class attributes and methods
sqliteModel_ExprAnd_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprAnd.attributes={sqliteModel_ExprAnd_op}

# sqliteModel_ExprOr class attributes and methods
sqliteModel_ExprOr_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprOr.attributes={sqliteModel_ExprOr_op}

# sqliteModel_ExprEqual class attributes and methods
sqliteModel_ExprEqual_op: Property = Property(name="op", type=StringType)
sqliteModel_ExprEqual.attributes={sqliteModel_ExprEqual_op}

# sqliteModel_NullCheckExpression class attributes and methods

# sqliteModel_IsNull class attributes and methods

# sqliteModel_NotNull class attributes and methods

# sqliteModel_NewColumn class attributes and methods

# sqliteModel_Literal class attributes and methods

# sqliteModel_NestedExpression class attributes and methods

# sqliteModel_OldColumn class attributes and methods

# sqliteModel_ColumnSourceRef class attributes and methods
sqliteModel_ColumnSourceRef_all: Property = Property(name="all", type=BooleanType)
sqliteModel_ColumnSourceRef.attributes={sqliteModel_ColumnSourceRef_all}

# sqliteModel_CaseExpression class attributes and methods

# sqliteModel_CastExpression class attributes and methods
sqliteModel_CastExpression_type: Property = Property(name="type", type=StringType)
sqliteModel_CastExpression.attributes={sqliteModel_CastExpression_type}

# sqliteModel_SelectStatementExpression class attributes and methods
sqliteModel_SelectStatementExpression_not: Property = Property(name="not", type=BooleanType)
sqliteModel_SelectStatementExpression_exists: Property = Property(name="exists", type=BooleanType)
sqliteModel_SelectStatementExpression.attributes={sqliteModel_SelectStatementExpression_exists, sqliteModel_SelectStatementExpression_not}

# sqliteModel_SelectExpression class attributes and methods
sqliteModel_SelectExpression_distinct: Property = Property(name="distinct", type=BooleanType)
sqliteModel_SelectExpression_all: Property = Property(name="all", type=BooleanType)
sqliteModel_SelectExpression_allColumns: Property = Property(name="allColumns", type=BooleanType)
sqliteModel_SelectExpression.attributes={sqliteModel_SelectExpression_allColumns, sqliteModel_SelectExpression_distinct, sqliteModel_SelectExpression_all}

# sqliteModel_FunctionArgument class attributes and methods

# sqliteModel_SelectCore class attributes and methods
sqliteModel_SelectCore_op: Property = Property(name="op", type=StringType)
sqliteModel_SelectCore.attributes={sqliteModel_SelectCore_op}

# SelectCoreExpression class attributes and methods

# sqliteModel_ResultColumn class attributes and methods

# ColumnSource class attributes and methods

# sqliteModel_NumericLiteral class attributes and methods
sqliteModel_NumericLiteral_number: Property = Property(name="number", type=StringType)
sqliteModel_NumericLiteral.attributes={sqliteModel_NumericLiteral_number}

# LiteralValue class attributes and methods

# sqliteModel_StringLiteral class attributes and methods
sqliteModel_StringLiteral_literal: Property = Property(name="literal", type=StringType)
sqliteModel_StringLiteral.attributes={sqliteModel_StringLiteral_literal}

# sqliteModel_NullLiteral class attributes and methods
sqliteModel_NullLiteral_literal: Property = Property(name="literal", type=StringType)
sqliteModel_NullLiteral.attributes={sqliteModel_NullLiteral_literal}

# sqliteModel_SingleSourceTable class attributes and methods

# SelectSource class attributes and methods

# sqliteModel_SingleSourceSelectStatement class attributes and methods

# sqliteModel_CurrentDateLiteral class attributes and methods
sqliteModel_CurrentDateLiteral_literal: Property = Property(name="literal", type=StringType)
sqliteModel_CurrentDateLiteral.attributes={sqliteModel_CurrentDateLiteral_literal}

# sqliteModel_CurrentTimeStampLiteral class attributes and methods
sqliteModel_CurrentTimeStampLiteral_literal: Property = Property(name="literal", type=StringType)
sqliteModel_CurrentTimeStampLiteral.attributes={sqliteModel_CurrentTimeStampLiteral_literal}

# sqliteModel_CreateTableStatement class attributes and methods
sqliteModel_CreateTableStatement_temporary: Property = Property(name="temporary", type=BooleanType)
sqliteModel_CreateTableStatement.attributes={sqliteModel_CreateTableStatement_temporary}

# TableDefinition class attributes and methods

# sqliteModel_CurrentTimeLiteral class attributes and methods
sqliteModel_CurrentTimeLiteral_literal: Property = Property(name="literal", type=StringType)
sqliteModel_CurrentTimeLiteral.attributes={sqliteModel_CurrentTimeLiteral_literal}

# sqliteModel_AlterTableRenameStatement class attributes and methods

# sqliteModel_UniqueConstraint class attributes and methods

# sqliteModel_DefaultConstraint class attributes and methods

# sqliteModel_LiteralDefaultValue class attributes and methods

# DefaultValue class attributes and methods

# sqliteModel_PrimaryKeyColumnConstraint class attributes and methods
sqliteModel_PrimaryKeyColumnConstraint_asc: Property = Property(name="asc", type=BooleanType)
sqliteModel_PrimaryKeyColumnConstraint_desc: Property = Property(name="desc", type=BooleanType)
sqliteModel_PrimaryKeyColumnConstraint_autoincrement: Property = Property(name="autoincrement", type=BooleanType)
sqliteModel_PrimaryKeyColumnConstraint.attributes={sqliteModel_PrimaryKeyColumnConstraint_desc, sqliteModel_PrimaryKeyColumnConstraint_asc, sqliteModel_PrimaryKeyColumnConstraint_autoincrement}

# ColumnConstraint class attributes and methods

# sqliteModel_NotNullConstraint class attributes and methods

# sqliteModel_ExpressionDefaultValue class attributes and methods

# Relationships
init3: BinaryAssociation = BinaryAssociation(
    name="init3",
    ends={
        Property(name="sqliteModel_InitBlock", type=sqliteModel_DatabaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DatabaseBlock4", type=sqliteModel_InitBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
migrations5: BinaryAssociation = BinaryAssociation(
    name="migrations5",
    ends={
        Property(name="sqliteModel_MigrationBlock", type=sqliteModel_DatabaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DatabaseBlock6", type=sqliteModel_MigrationBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements7: BinaryAssociation = BinaryAssociation(
    name="statements7",
    ends={
        Property(name="sqliteModel_ConfigurationStatement", type=sqliteModel_ConfigBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ConfigBlock8", type=sqliteModel_ConfigurationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements9: BinaryAssociation = BinaryAssociation(
    name="statements9",
    ends={
        Property(name="sqliteModel_DDLStatement", type=sqliteModel_InitBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_InitBlock10", type=sqliteModel_DDLStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments11: BinaryAssociation = BinaryAssociation(
    name="segments11",
    ends={
        Property(name="sqliteModel_ContentUriSegment", type=sqliteModel_ContentUri, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ContentUri", type=sqliteModel_ContentUriSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database0: BinaryAssociation = BinaryAssociation(
    name="database0",
    ends={
        Property(name="sqliteModel_DatabaseBlock", type=sqliteModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Model", type=sqliteModel_DatabaseBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
config1: BinaryAssociation = BinaryAssociation(
    name="config1",
    ends={
        Property(name="sqliteModel_ConfigBlock", type=sqliteModel_DatabaseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DatabaseBlock2", type=sqliteModel_ConfigBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression31: BinaryAssociation = BinaryAssociation(
    name="expression31",
    ends={
        Property(name="sqliteModel_Expression32", type=sqliteModel_WhereExpressions, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_WhereExpressions", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByExpressions33: BinaryAssociation = BinaryAssociation(
    name="groupByExpressions33",
    ends={
        Property(name="sqliteModel_Expression34", type=sqliteModel_GroupByExpressions, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_GroupByExpressions", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression35: BinaryAssociation = BinaryAssociation(
    name="expression35",
    ends={
        Property(name="sqliteModel_Expression36", type=sqliteModel_HavingExpressions, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_HavingExpressions", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="sqliteModel_Expression39", type=sqliteModel_OrderingTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_OrderingTerm38", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="sqliteModel_SingleSource", type=sqliteModel_JoinSource, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_JoinSource", type=sqliteModel_SingleSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinStatements41: BinaryAssociation = BinaryAssociation(
    name="joinStatements41",
    ends={
        Property(name="sqliteModel_JoinStatement", type=sqliteModel_JoinSource, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_JoinSource42", type=sqliteModel_JoinStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="sqliteModel_DDLStatement14", type=sqliteModel_MigrationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_MigrationBlock13", type=sqliteModel_DDLStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whenExpression15: BinaryAssociation = BinaryAssociation(
    name="whenExpression15",
    ends={
        Property(name="sqliteModel_Expression", type=sqliteModel_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Case", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression16: BinaryAssociation = BinaryAssociation(
    name="thenExpression16",
    ends={
        Property(name="sqliteModel_Expression18", type=sqliteModel_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Case17", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
core19: BinaryAssociation = BinaryAssociation(
    name="core19",
    ends={
        Property(name="sqliteModel_SelectCoreExpression", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectStatement", type=sqliteModel_SelectCoreExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderby20: BinaryAssociation = BinaryAssociation(
    name="orderby20",
    ends={
        Property(name="sqliteModel_OrderingTermList", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectStatement21", type=sqliteModel_OrderingTermList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limit22: BinaryAssociation = BinaryAssociation(
    name="limit22",
    ends={
        Property(name="sqliteModel_Expression24", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectStatement23", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limitOffset25: BinaryAssociation = BinaryAssociation(
    name="limitOffset25",
    ends={
        Property(name="sqliteModel_Expression27", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectStatement26", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderingTerms28: BinaryAssociation = BinaryAssociation(
    name="orderingTerms28",
    ends={
        Property(name="sqliteModel_OrderingTerm", type=sqliteModel_OrderingTermList, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_OrderingTermList29", type=sqliteModel_OrderingTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultColumns30: BinaryAssociation = BinaryAssociation(
    name="resultColumns30",
    ends={
        Property(name="sqliteModel_ColumnSource", type=sqliteModel_SelectList, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectList", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table51: BinaryAssociation = BinaryAssociation(
    name="table51",
    ends={
        Property(name="sqliteModel_TableDefinition", type=sqliteModel_CreateTriggerStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateTriggerStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
whenExpression52: BinaryAssociation = BinaryAssociation(
    name="whenExpression52",
    ends={
        Property(name="sqliteModel_Expression54", type=sqliteModel_CreateTriggerStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateTriggerStatement53", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements55: BinaryAssociation = BinaryAssociation(
    name="statements55",
    ends={
        Property(name="sqliteModel_DMLStatement", type=sqliteModel_CreateTriggerStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateTriggerStatement56", type=sqliteModel_DMLStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table57: BinaryAssociation = BinaryAssociation(
    name="table57",
    ends={
        Property(name="sqliteModel_TableDefinition58", type=sqliteModel_AlterTableAddColumnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_AlterTableAddColumnStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
columnDef59: BinaryAssociation = BinaryAssociation(
    name="columnDef59",
    ends={
        Property(name="sqliteModel_ColumnSource61", type=sqliteModel_AlterTableAddColumnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_AlterTableAddColumnStatement60", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinSource43: BinaryAssociation = BinaryAssociation(
    name="joinSource43",
    ends={
        Property(name="sqliteModel_JoinSource44", type=sqliteModel_SingleSourceJoin, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SingleSourceJoin", type=sqliteModel_JoinSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleSource45: BinaryAssociation = BinaryAssociation(
    name="singleSource45",
    ends={
        Property(name="sqliteModel_SingleSource47", type=sqliteModel_JoinStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_JoinStatement46", type=sqliteModel_SingleSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="sqliteModel_Expression50", type=sqliteModel_JoinStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_JoinStatement49", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns73: BinaryAssociation = BinaryAssociation(
    name="columns73",
    ends={
        Property(name="sqliteModel_IndexedColumn74", type=sqliteModel_UniqueTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UniqueTableConstraint", type=sqliteModel_IndexedColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflictClause75: BinaryAssociation = BinaryAssociation(
    name="conflictClause75",
    ends={
        Property(name="sqliteModel_ConflictClause", type=sqliteModel_UniqueTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UniqueTableConstraint76", type=sqliteModel_ConflictClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns77: BinaryAssociation = BinaryAssociation(
    name="columns77",
    ends={
        Property(name="sqliteModel_IndexedColumn78", type=sqliteModel_PrimaryConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_PrimaryConstraint", type=sqliteModel_IndexedColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflictClause79: BinaryAssociation = BinaryAssociation(
    name="conflictClause79",
    ends={
        Property(name="sqliteModel_ConflictClause81", type=sqliteModel_PrimaryConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_PrimaryConstraint80", type=sqliteModel_ConflictClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="sqliteModel_Expression83", type=sqliteModel_CheckTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CheckTableConstraint", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnReference84: BinaryAssociation = BinaryAssociation(
    name="columnReference84",
    ends={
        Property(name="sqliteModel_ColumnDef", type=sqliteModel_IndexedColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_IndexedColumn85", type=sqliteModel_ColumnDef, multiplicity=Multiplicity(0, 1))
    }
)
table62: BinaryAssociation = BinaryAssociation(
    name="table62",
    ends={
        Property(name="sqliteModel_TableDefinition63", type=sqliteModel_DropTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DropTableStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
trigger64: BinaryAssociation = BinaryAssociation(
    name="trigger64",
    ends={
        Property(name="sqliteModel_CreateTriggerStatement65", type=sqliteModel_DropTriggerStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DropTriggerStatement", type=sqliteModel_CreateTriggerStatement, multiplicity=Multiplicity(0, 1))
    }
)
view66: BinaryAssociation = BinaryAssociation(
    name="view66",
    ends={
        Property(name="sqliteModel_CreateViewStatement", type=sqliteModel_DropViewStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DropViewStatement", type=sqliteModel_CreateViewStatement, multiplicity=Multiplicity(0, 1))
    }
)
table67: BinaryAssociation = BinaryAssociation(
    name="table67",
    ends={
        Property(name="sqliteModel_TableDefinition68", type=sqliteModel_CreateIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateIndexStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
columns69: BinaryAssociation = BinaryAssociation(
    name="columns69",
    ends={
        Property(name="sqliteModel_IndexedColumn", type=sqliteModel_CreateIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateIndexStatement70", type=sqliteModel_IndexedColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index71: BinaryAssociation = BinaryAssociation(
    name="index71",
    ends={
        Property(name="sqliteModel_CreateIndexStatement72", type=sqliteModel_DropIndexStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DropIndexStatement", type=sqliteModel_CreateIndexStatement, multiplicity=Multiplicity(0, 1))
    }
)
expressions96: BinaryAssociation = BinaryAssociation(
    name="expressions96",
    ends={
        Property(name="sqliteModel_Expression98", type=sqliteModel_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_InsertStatement97", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectStatement99: BinaryAssociation = BinaryAssociation(
    name="selectStatement99",
    ends={
        Property(name="sqliteModel_SelectStatement101", type=sqliteModel_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_InsertStatement100", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table102: BinaryAssociation = BinaryAssociation(
    name="table102",
    ends={
        Property(name="sqliteModel_TableDefinition103", type=sqliteModel_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UpdateStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
updateColumnExpressions104: BinaryAssociation = BinaryAssociation(
    name="updateColumnExpressions104",
    ends={
        Property(name="sqliteModel_UpdateColumnExpression", type=sqliteModel_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UpdateStatement105", type=sqliteModel_UpdateColumnExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereExpression106: BinaryAssociation = BinaryAssociation(
    name="whereExpression106",
    ends={
        Property(name="sqliteModel_Expression108", type=sqliteModel_UpdateStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UpdateStatement107", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnName109: BinaryAssociation = BinaryAssociation(
    name="columnName109",
    ends={
        Property(name="sqliteModel_ColumnDef111", type=sqliteModel_UpdateColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UpdateColumnExpression110", type=sqliteModel_ColumnDef, multiplicity=Multiplicity(0, 1))
    }
)
expression112: BinaryAssociation = BinaryAssociation(
    name="expression112",
    ends={
        Property(name="sqliteModel_Expression114", type=sqliteModel_UpdateColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UpdateColumnExpression113", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table86: BinaryAssociation = BinaryAssociation(
    name="table86",
    ends={
        Property(name="sqliteModel_TableDefinition87", type=sqliteModel_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DeleteStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
expression88: BinaryAssociation = BinaryAssociation(
    name="expression88",
    ends={
        Property(name="sqliteModel_Expression90", type=sqliteModel_DeleteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DeleteStatement89", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table91: BinaryAssociation = BinaryAssociation(
    name="table91",
    ends={
        Property(name="sqliteModel_TableDefinition92", type=sqliteModel_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_InsertStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
columnNames93: BinaryAssociation = BinaryAssociation(
    name="columnNames93",
    ends={
        Property(name="sqliteModel_ColumnDef95", type=sqliteModel_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_InsertStatement94", type=sqliteModel_ColumnDef, multiplicity=Multiplicity(0, 9999))
    }
)
args117: BinaryAssociation = BinaryAssociation(
    name="args117",
    ends={
        Property(name="sqliteModel_FunctionArg", type=sqliteModel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Function", type=sqliteModel_FunctionArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body118: BinaryAssociation = BinaryAssociation(
    name="body118",
    ends={
        Property(name="sqliteModel_SelectStatement120", type=sqliteModel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Function119", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments121: BinaryAssociation = BinaryAssociation(
    name="arguments121",
    ends={
        Property(name="sqliteModel_Expression123", type=sqliteModel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Function122", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uri115: BinaryAssociation = BinaryAssociation(
    name="uri115",
    ends={
        Property(name="sqliteModel_ContentUri116", type=sqliteModel_ActionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ActionStatement", type=sqliteModel_ContentUri, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left129: BinaryAssociation = BinaryAssociation(
    name="left129",
    ends={
        Property(name="sqliteModel_Expression130", type=sqliteModel_ExprMult, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprMult", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right131: BinaryAssociation = BinaryAssociation(
    name="right131",
    ends={
        Property(name="sqliteModel_Expression133", type=sqliteModel_ExprMult, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprMult132", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left134: BinaryAssociation = BinaryAssociation(
    name="left134",
    ends={
        Property(name="sqliteModel_Expression135", type=sqliteModel_ExprAdd, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprAdd", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left124: BinaryAssociation = BinaryAssociation(
    name="left124",
    ends={
        Property(name="sqliteModel_Expression125", type=sqliteModel_ExprConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprConcat", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right126: BinaryAssociation = BinaryAssociation(
    name="right126",
    ends={
        Property(name="sqliteModel_Expression128", type=sqliteModel_ExprConcat, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprConcat127", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right141: BinaryAssociation = BinaryAssociation(
    name="right141",
    ends={
        Property(name="sqliteModel_Expression143", type=sqliteModel_ExprBit, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprBit142", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left144: BinaryAssociation = BinaryAssociation(
    name="left144",
    ends={
        Property(name="sqliteModel_Expression145", type=sqliteModel_ExprRelate, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprRelate", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right146: BinaryAssociation = BinaryAssociation(
    name="right146",
    ends={
        Property(name="sqliteModel_Expression148", type=sqliteModel_ExprRelate, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprRelate147", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right136: BinaryAssociation = BinaryAssociation(
    name="right136",
    ends={
        Property(name="sqliteModel_Expression138", type=sqliteModel_ExprAdd, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprAdd137", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left139: BinaryAssociation = BinaryAssociation(
    name="left139",
    ends={
        Property(name="sqliteModel_Expression140", type=sqliteModel_ExprBit, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprBit", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right151: BinaryAssociation = BinaryAssociation(
    name="right151",
    ends={
        Property(name="sqliteModel_ExprEqual152", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sqliteModel_Expression153", type=sqliteModel_ExprEqual, multiplicity=Multiplicity(1, 1))
    }
)
left154: BinaryAssociation = BinaryAssociation(
    name="left154",
    ends={
        Property(name="sqliteModel_Expression155", type=sqliteModel_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprAnd", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right156: BinaryAssociation = BinaryAssociation(
    name="right156",
    ends={
        Property(name="sqliteModel_Expression158", type=sqliteModel_ExprAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprAnd157", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left149: BinaryAssociation = BinaryAssociation(
    name="left149",
    ends={
        Property(name="sqliteModel_Expression150", type=sqliteModel_ExprEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprEqual", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left164: BinaryAssociation = BinaryAssociation(
    name="left164",
    ends={
        Property(name="sqliteModel_Expression165", type=sqliteModel_NullCheckExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_NullCheckExpression", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right166: BinaryAssociation = BinaryAssociation(
    name="right166",
    ends={
        Property(name="sqliteModel_Expression168", type=sqliteModel_NullCheckExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_NullCheckExpression167", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left159: BinaryAssociation = BinaryAssociation(
    name="left159",
    ends={
        Property(name="sqliteModel_Expression160", type=sqliteModel_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprOr", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right161: BinaryAssociation = BinaryAssociation(
    name="right161",
    ends={
        Property(name="sqliteModel_Expression163", type=sqliteModel_ExprOr, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExprOr162", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source173: BinaryAssociation = BinaryAssociation(
    name="source173",
    ends={
        Property(name="sqliteModel_SelectSource", type=sqliteModel_ColumnSourceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ColumnSourceRef", type=sqliteModel_SelectSource, multiplicity=Multiplicity(0, 1))
    }
)
column174: BinaryAssociation = BinaryAssociation(
    name="column174",
    ends={
        Property(name="sqliteModel_ColumnSource176", type=sqliteModel_ColumnSourceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ColumnSourceRef175", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 1))
    }
)
literalValue177: BinaryAssociation = BinaryAssociation(
    name="literalValue177",
    ends={
        Property(name="sqliteModel_LiteralValue", type=sqliteModel_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_Literal", type=sqliteModel_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression178: BinaryAssociation = BinaryAssociation(
    name="expression178",
    ends={
        Property(name="sqliteModel_Expression179", type=sqliteModel_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_NestedExpression", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column169: BinaryAssociation = BinaryAssociation(
    name="column169",
    ends={
        Property(name="sqliteModel_ColumnSource170", type=sqliteModel_NewColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_NewColumn", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 1))
    }
)
column171: BinaryAssociation = BinaryAssociation(
    name="column171",
    ends={
        Property(name="sqliteModel_ColumnSource172", type=sqliteModel_OldColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_OldColumn", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 1))
    }
)
caseExpression182: BinaryAssociation = BinaryAssociation(
    name="caseExpression182",
    ends={
        Property(name="sqliteModel_Expression183", type=sqliteModel_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CaseExpression", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases184: BinaryAssociation = BinaryAssociation(
    name="cases184",
    ends={
        Property(name="sqliteModel_Case186", type=sqliteModel_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CaseExpression185", type=sqliteModel_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpression187: BinaryAssociation = BinaryAssociation(
    name="elseExpression187",
    ends={
        Property(name="sqliteModel_Expression189", type=sqliteModel_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CaseExpression188", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression190: BinaryAssociation = BinaryAssociation(
    name="expression190",
    ends={
        Property(name="sqliteModel_Expression191", type=sqliteModel_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CastExpression", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
select180: BinaryAssociation = BinaryAssociation(
    name="select180",
    ends={
        Property(name="sqliteModel_SelectStatement181", type=sqliteModel_SelectStatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectStatementExpression", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right196: BinaryAssociation = BinaryAssociation(
    name="right196",
    ends={
        Property(name="sqliteModel_SelectCoreExpression198", type=sqliteModel_SelectCore, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectCore197", type=sqliteModel_SelectCoreExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectList199: BinaryAssociation = BinaryAssociation(
    name="selectList199",
    ends={
        Property(name="sqliteModel_SelectList200", type=sqliteModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectExpression", type=sqliteModel_SelectList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source201: BinaryAssociation = BinaryAssociation(
    name="source201",
    ends={
        Property(name="sqliteModel_JoinSource203", type=sqliteModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectExpression202", type=sqliteModel_JoinSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where204: BinaryAssociation = BinaryAssociation(
    name="where204",
    ends={
        Property(name="sqliteModel_WhereExpressions206", type=sqliteModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectExpression205", type=sqliteModel_WhereExpressions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupBy207: BinaryAssociation = BinaryAssociation(
    name="groupBy207",
    ends={
        Property(name="sqliteModel_GroupByExpressions209", type=sqliteModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectExpression208", type=sqliteModel_GroupByExpressions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg192: BinaryAssociation = BinaryAssociation(
    name="arg192",
    ends={
        Property(name="sqliteModel_FunctionArg193", type=sqliteModel_FunctionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_FunctionArgument", type=sqliteModel_FunctionArg, multiplicity=Multiplicity(0, 1))
    }
)
left194: BinaryAssociation = BinaryAssociation(
    name="left194",
    ends={
        Property(name="sqliteModel_SelectCoreExpression195", type=sqliteModel_SelectCore, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectCore", type=sqliteModel_SelectCoreExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression217: BinaryAssociation = BinaryAssociation(
    name="expression217",
    ends={
        Property(name="sqliteModel_Expression218", type=sqliteModel_ResultColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ResultColumn", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having210: BinaryAssociation = BinaryAssociation(
    name="having210",
    ends={
        Property(name="sqliteModel_HavingExpressions212", type=sqliteModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SelectExpression211", type=sqliteModel_HavingExpressions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableReference213: BinaryAssociation = BinaryAssociation(
    name="tableReference213",
    ends={
        Property(name="sqliteModel_TableDefinition214", type=sqliteModel_SingleSourceTable, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SingleSourceTable", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
selectStatement215: BinaryAssociation = BinaryAssociation(
    name="selectStatement215",
    ends={
        Property(name="sqliteModel_SelectStatement216", type=sqliteModel_SingleSourceSelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_SingleSourceSelectStatement", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectStatement223: BinaryAssociation = BinaryAssociation(
    name="selectStatement223",
    ends={
        Property(name="sqliteModel_SelectStatement225", type=sqliteModel_CreateViewStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateViewStatement224", type=sqliteModel_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table226: BinaryAssociation = BinaryAssociation(
    name="table226",
    ends={
        Property(name="sqliteModel_TableDefinition227", type=sqliteModel_AlterTableRenameStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_AlterTableRenameStatement", type=sqliteModel_TableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
constraints228: BinaryAssociation = BinaryAssociation(
    name="constraints228",
    ends={
        Property(name="sqliteModel_ColumnConstraint", type=sqliteModel_ColumnDef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ColumnDef229", type=sqliteModel_ColumnConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnDefs219: BinaryAssociation = BinaryAssociation(
    name="columnDefs219",
    ends={
        Property(name="sqliteModel_ColumnSource220", type=sqliteModel_CreateTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateTableStatement", type=sqliteModel_ColumnSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints221: BinaryAssociation = BinaryAssociation(
    name="constraints221",
    ends={
        Property(name="sqliteModel_TableConstraint", type=sqliteModel_CreateTableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_CreateTableStatement222", type=sqliteModel_TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflictClause232: BinaryAssociation = BinaryAssociation(
    name="conflictClause232",
    ends={
        Property(name="sqliteModel_ConflictClause233", type=sqliteModel_UniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_UniqueConstraint", type=sqliteModel_ConflictClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue234: BinaryAssociation = BinaryAssociation(
    name="defaultValue234",
    ends={
        Property(name="sqliteModel_DefaultValue", type=sqliteModel_DefaultConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_DefaultConstraint", type=sqliteModel_DefaultValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal235: BinaryAssociation = BinaryAssociation(
    name="literal235",
    ends={
        Property(name="sqliteModel_LiteralValue236", type=sqliteModel_LiteralDefaultValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_LiteralDefaultValue", type=sqliteModel_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conflictClause230: BinaryAssociation = BinaryAssociation(
    name="conflictClause230",
    ends={
        Property(name="sqliteModel_ConflictClause231", type=sqliteModel_NotNullConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_NotNullConstraint", type=sqliteModel_ConflictClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression237: BinaryAssociation = BinaryAssociation(
    name="expression237",
    ends={
        Property(name="sqliteModel_Expression238", type=sqliteModel_ExpressionDefaultValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sqliteModel_ExpressionDefaultValue", type=sqliteModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sqliteModel_SelectStatement_DMLStatement = Generalization(general=DMLStatement, specific=sqliteModel_SelectStatement)
gen_sqliteModel_TableDefinition_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_TableDefinition)
gen_sqliteModel_CreateTriggerStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_CreateTriggerStatement)
gen_sqliteModel_AlterTableAddColumnStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_AlterTableAddColumnStatement)
gen_sqliteModel_SelectSource_SingleSource = Generalization(general=SingleSource, specific=sqliteModel_SelectSource)
gen_sqliteModel_SingleSourceJoin_SingleSource = Generalization(general=SingleSource, specific=sqliteModel_SingleSourceJoin)
gen_sqliteModel_UniqueTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqliteModel_UniqueTableConstraint)
gen_sqliteModel_PrimaryConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqliteModel_PrimaryConstraint)
gen_sqliteModel_CheckTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqliteModel_CheckTableConstraint)
gen_sqliteModel_DropTableStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_DropTableStatement)
gen_sqliteModel_DropTriggerStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_DropTriggerStatement)
gen_sqliteModel_DropViewStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_DropViewStatement)
gen_sqliteModel_CreateIndexStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_CreateIndexStatement)
gen_sqliteModel_DropIndexStatement_DDLStatement = Generalization(general=DDLStatement, specific=sqliteModel_DropIndexStatement)
gen_sqliteModel_UpdateStatement_DMLStatement = Generalization(general=DMLStatement, specific=sqliteModel_UpdateStatement)
gen_sqliteModel_ActionStatement_ConfigurationStatement = Generalization(general=ConfigurationStatement, specific=sqliteModel_ActionStatement)
gen_sqliteModel_DeleteStatement_DMLStatement = Generalization(general=DMLStatement, specific=sqliteModel_DeleteStatement)
gen_sqliteModel_InsertStatement_DMLStatement = Generalization(general=DMLStatement, specific=sqliteModel_InsertStatement)
gen_sqliteModel_Function_Expression = Generalization(general=Expression, specific=sqliteModel_Function)
gen_sqliteModel_Function_ConfigurationStatement = Generalization(general=ConfigurationStatement, specific=sqliteModel_Function)
gen_sqliteModel_ExprMult_Expression = Generalization(general=Expression, specific=sqliteModel_ExprMult)
gen_sqliteModel_ExprAdd_Expression = Generalization(general=Expression, specific=sqliteModel_ExprAdd)
gen_sqliteModel_ContentUriParamSegment_ContentUriSegment = Generalization(general=ContentUriSegment, specific=sqliteModel_ContentUriParamSegment)
gen_sqliteModel_ExprConcat_Expression = Generalization(general=Expression, specific=sqliteModel_ExprConcat)
gen_sqliteModel_ExprRelate_Expression = Generalization(general=Expression, specific=sqliteModel_ExprRelate)
gen_sqliteModel_ExprBit_Expression = Generalization(general=Expression, specific=sqliteModel_ExprBit)
gen_sqliteModel_ExprAnd_Expression = Generalization(general=Expression, specific=sqliteModel_ExprAnd)
gen_sqliteModel_ExprOr_Expression = Generalization(general=Expression, specific=sqliteModel_ExprOr)
gen_sqliteModel_ExprEqual_Expression = Generalization(general=Expression, specific=sqliteModel_ExprEqual)
gen_sqliteModel_NullCheckExpression_Expression = Generalization(general=Expression, specific=sqliteModel_NullCheckExpression)
gen_sqliteModel_IsNull_Expression = Generalization(general=Expression, specific=sqliteModel_IsNull)
gen_sqliteModel_NotNull_Expression = Generalization(general=Expression, specific=sqliteModel_NotNull)
gen_sqliteModel_NewColumn_Expression = Generalization(general=Expression, specific=sqliteModel_NewColumn)
gen_sqliteModel_Literal_Expression = Generalization(general=Expression, specific=sqliteModel_Literal)
gen_sqliteModel_NestedExpression_Expression = Generalization(general=Expression, specific=sqliteModel_NestedExpression)
gen_sqliteModel_OldColumn_Expression = Generalization(general=Expression, specific=sqliteModel_OldColumn)
gen_sqliteModel_ColumnSourceRef_Expression = Generalization(general=Expression, specific=sqliteModel_ColumnSourceRef)
gen_sqliteModel_CaseExpression_Expression = Generalization(general=Expression, specific=sqliteModel_CaseExpression)
gen_sqliteModel_CastExpression_Expression = Generalization(general=Expression, specific=sqliteModel_CastExpression)
gen_sqliteModel_SelectStatementExpression_Expression = Generalization(general=Expression, specific=sqliteModel_SelectStatementExpression)
gen_sqliteModel_SelectExpression_SelectCoreExpression = Generalization(general=SelectCoreExpression, specific=sqliteModel_SelectExpression)
gen_sqliteModel_FunctionArgument_Expression = Generalization(general=Expression, specific=sqliteModel_FunctionArgument)
gen_sqliteModel_SelectCore_SelectCoreExpression = Generalization(general=SelectCoreExpression, specific=sqliteModel_SelectCore)
gen_sqliteModel_ResultColumn_ColumnSource = Generalization(general=ColumnSource, specific=sqliteModel_ResultColumn)
gen_sqliteModel_NumericLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_NumericLiteral)
gen_sqliteModel_StringLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_StringLiteral)
gen_sqliteModel_NullLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_NullLiteral)
gen_sqliteModel_SingleSourceTable_SelectSource = Generalization(general=SelectSource, specific=sqliteModel_SingleSourceTable)
gen_sqliteModel_SingleSourceSelectStatement_SelectSource = Generalization(general=SelectSource, specific=sqliteModel_SingleSourceSelectStatement)
gen_sqliteModel_CurrentDateLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_CurrentDateLiteral)
gen_sqliteModel_CurrentTimeStampLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_CurrentTimeStampLiteral)
gen_sqliteModel_CreateTableStatement_TableDefinition = Generalization(general=TableDefinition, specific=sqliteModel_CreateTableStatement)
gen_sqliteModel_CurrentTimeLiteral_LiteralValue = Generalization(general=LiteralValue, specific=sqliteModel_CurrentTimeLiteral)
gen_sqliteModel_AlterTableRenameStatement_TableDefinition = Generalization(general=TableDefinition, specific=sqliteModel_AlterTableRenameStatement)
gen_sqliteModel_ColumnDef_ColumnSource = Generalization(general=ColumnSource, specific=sqliteModel_ColumnDef)
gen_sqliteModel_CreateViewStatement_TableDefinition = Generalization(general=TableDefinition, specific=sqliteModel_CreateViewStatement)
gen_sqliteModel_UniqueConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=sqliteModel_UniqueConstraint)
gen_sqliteModel_DefaultConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=sqliteModel_DefaultConstraint)
gen_sqliteModel_LiteralDefaultValue_DefaultValue = Generalization(general=DefaultValue, specific=sqliteModel_LiteralDefaultValue)
gen_sqliteModel_PrimaryKeyColumnConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=sqliteModel_PrimaryKeyColumnConstraint)
gen_sqliteModel_NotNullConstraint_ColumnConstraint = Generalization(general=ColumnConstraint, specific=sqliteModel_NotNullConstraint)
gen_sqliteModel_ExpressionDefaultValue_DefaultValue = Generalization(general=DefaultValue, specific=sqliteModel_ExpressionDefaultValue)

# Domain Model
domain_model = DomainModel(
    name="sqliteModel",
    types={sqliteModel_InitBlock, sqliteModel_MigrationBlock, sqliteModel_ConfigurationStatement, sqliteModel_DDLStatement, sqliteModel_FunctionArg, sqliteModel_ContentUri, sqliteModel_ContentUriSegment, sqliteModel_Model, sqliteModel_DatabaseBlock, sqliteModel_ConfigBlock, sqliteModel_WhereExpressions, sqliteModel_GroupByExpressions, sqliteModel_HavingExpressions, sqliteModel_JoinSource, sqliteModel_SingleSource, sqliteModel_JoinStatement, sqliteModel_Expression, sqliteModel_Case, sqliteModel_SelectStatement, DMLStatement, sqliteModel_SelectCoreExpression, sqliteModel_OrderingTermList, sqliteModel_OrderingTerm, sqliteModel_SelectList, sqliteModel_ColumnSource, sqliteModel_TableDefinition, DDLStatement, sqliteModel_CreateTriggerStatement, sqliteModel_DMLStatement, sqliteModel_AlterTableAddColumnStatement, sqliteModel_DropTableStatement, sqliteModel_SelectSource, SingleSource, sqliteModel_SingleSourceJoin, sqliteModel_LiteralValue, sqliteModel_ColumnConstraint, sqliteModel_TableConstraint, sqliteModel_UniqueTableConstraint, TableConstraint, sqliteModel_ConflictClause, sqliteModel_PrimaryConstraint, sqliteModel_CheckTableConstraint, sqliteModel_ColumnDef, sqliteModel_DefaultValue, sqliteModel_DropTriggerStatement, sqliteModel_DropViewStatement, sqliteModel_CreateViewStatement, sqliteModel_CreateIndexStatement, sqliteModel_IndexedColumn, sqliteModel_DropIndexStatement, sqliteModel_UpdateStatement, sqliteModel_UpdateColumnExpression, sqliteModel_ActionStatement, ConfigurationStatement, sqliteModel_DeleteStatement, sqliteModel_InsertStatement, sqliteModel_ContentUriParamSegment, ContentUriSegment, sqliteModel_Function, Expression, sqliteModel_ExprMult, sqliteModel_ExprAdd, sqliteModel_ExprConcat, sqliteModel_ExprRelate, sqliteModel_ExprBit, sqliteModel_ExprAnd, sqliteModel_ExprOr, sqliteModel_ExprEqual, sqliteModel_NullCheckExpression, sqliteModel_IsNull, sqliteModel_NotNull, sqliteModel_NewColumn, sqliteModel_Literal, sqliteModel_NestedExpression, sqliteModel_OldColumn, sqliteModel_ColumnSourceRef, sqliteModel_CaseExpression, sqliteModel_CastExpression, sqliteModel_SelectStatementExpression, sqliteModel_SelectExpression, sqliteModel_FunctionArgument, sqliteModel_SelectCore, SelectCoreExpression, sqliteModel_ResultColumn, ColumnSource, sqliteModel_NumericLiteral, LiteralValue, sqliteModel_StringLiteral, sqliteModel_NullLiteral, sqliteModel_SingleSourceTable, SelectSource, sqliteModel_SingleSourceSelectStatement, sqliteModel_CurrentDateLiteral, sqliteModel_CurrentTimeStampLiteral, sqliteModel_CreateTableStatement, TableDefinition, sqliteModel_CurrentTimeLiteral, sqliteModel_AlterTableRenameStatement, sqliteModel_UniqueConstraint, sqliteModel_DefaultConstraint, sqliteModel_LiteralDefaultValue, DefaultValue, sqliteModel_PrimaryKeyColumnConstraint, ColumnConstraint, sqliteModel_NotNullConstraint, sqliteModel_ExpressionDefaultValue, CompoundOperator, SqliteDataType, ColumnType, ConflictResolution},
    associations={init3, migrations5, statements7, statements9, segments11, database0, config1, expression31, groupByExpressions33, expression35, expression37, source40, joinStatements41, statements12, whenExpression15, thenExpression16, core19, orderby20, limit22, limitOffset25, orderingTerms28, resultColumns30, table51, whenExpression52, statements55, table57, columnDef59, joinSource43, singleSource45, expression48, columns73, conflictClause75, columns77, conflictClause79, expression82, columnReference84, table62, trigger64, view66, table67, columns69, index71, expressions96, selectStatement99, table102, updateColumnExpressions104, whereExpression106, columnName109, expression112, table86, expression88, table91, columnNames93, args117, body118, arguments121, uri115, left129, right131, left134, left124, right126, right141, left144, right146, right136, left139, right151, left154, right156, left149, left164, right166, left159, right161, source173, column174, literalValue177, expression178, column169, column171, caseExpression182, cases184, elseExpression187, expression190, select180, right196, selectList199, source201, where204, groupBy207, arg192, left194, expression217, having210, tableReference213, selectStatement215, selectStatement223, table226, constraints228, columnDefs219, constraints221, conflictClause232, defaultValue234, literal235, conflictClause230, expression237},
    generalizations={gen_sqliteModel_SelectStatement_DMLStatement, gen_sqliteModel_TableDefinition_DDLStatement, gen_sqliteModel_CreateTriggerStatement_DDLStatement, gen_sqliteModel_AlterTableAddColumnStatement_DDLStatement, gen_sqliteModel_SelectSource_SingleSource, gen_sqliteModel_SingleSourceJoin_SingleSource, gen_sqliteModel_UniqueTableConstraint_TableConstraint, gen_sqliteModel_PrimaryConstraint_TableConstraint, gen_sqliteModel_CheckTableConstraint_TableConstraint, gen_sqliteModel_DropTableStatement_DDLStatement, gen_sqliteModel_DropTriggerStatement_DDLStatement, gen_sqliteModel_DropViewStatement_DDLStatement, gen_sqliteModel_CreateIndexStatement_DDLStatement, gen_sqliteModel_DropIndexStatement_DDLStatement, gen_sqliteModel_UpdateStatement_DMLStatement, gen_sqliteModel_ActionStatement_ConfigurationStatement, gen_sqliteModel_DeleteStatement_DMLStatement, gen_sqliteModel_InsertStatement_DMLStatement, gen_sqliteModel_Function_Expression, gen_sqliteModel_Function_ConfigurationStatement, gen_sqliteModel_ExprMult_Expression, gen_sqliteModel_ExprAdd_Expression, gen_sqliteModel_ContentUriParamSegment_ContentUriSegment, gen_sqliteModel_ExprConcat_Expression, gen_sqliteModel_ExprRelate_Expression, gen_sqliteModel_ExprBit_Expression, gen_sqliteModel_ExprAnd_Expression, gen_sqliteModel_ExprOr_Expression, gen_sqliteModel_ExprEqual_Expression, gen_sqliteModel_NullCheckExpression_Expression, gen_sqliteModel_IsNull_Expression, gen_sqliteModel_NotNull_Expression, gen_sqliteModel_NewColumn_Expression, gen_sqliteModel_Literal_Expression, gen_sqliteModel_NestedExpression_Expression, gen_sqliteModel_OldColumn_Expression, gen_sqliteModel_ColumnSourceRef_Expression, gen_sqliteModel_CaseExpression_Expression, gen_sqliteModel_CastExpression_Expression, gen_sqliteModel_SelectStatementExpression_Expression, gen_sqliteModel_SelectExpression_SelectCoreExpression, gen_sqliteModel_FunctionArgument_Expression, gen_sqliteModel_SelectCore_SelectCoreExpression, gen_sqliteModel_ResultColumn_ColumnSource, gen_sqliteModel_NumericLiteral_LiteralValue, gen_sqliteModel_StringLiteral_LiteralValue, gen_sqliteModel_NullLiteral_LiteralValue, gen_sqliteModel_SingleSourceTable_SelectSource, gen_sqliteModel_SingleSourceSelectStatement_SelectSource, gen_sqliteModel_CurrentDateLiteral_LiteralValue, gen_sqliteModel_CurrentTimeStampLiteral_LiteralValue, gen_sqliteModel_CreateTableStatement_TableDefinition, gen_sqliteModel_CurrentTimeLiteral_LiteralValue, gen_sqliteModel_AlterTableRenameStatement_TableDefinition, gen_sqliteModel_ColumnDef_ColumnSource, gen_sqliteModel_CreateViewStatement_TableDefinition, gen_sqliteModel_UniqueConstraint_ColumnConstraint, gen_sqliteModel_DefaultConstraint_ColumnConstraint, gen_sqliteModel_LiteralDefaultValue_DefaultValue, gen_sqliteModel_PrimaryKeyColumnConstraint_ColumnConstraint, gen_sqliteModel_NotNullConstraint_ColumnConstraint, gen_sqliteModel_ExpressionDefaultValue_DefaultValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)