import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sqliteModel::SelectCoreExpression,
    DMLStatement,
    sqliteModel::SelectStatement,
    sqliteModel::Case,
    sqliteModel::Expression,
    sqliteModel::ContentUriSegment,
    sqliteModel::SingleSource,
    sqliteModel::JoinSource,
    sqliteModel::HavingExpressions,
    sqliteModel::InitBlock,
    sqliteModel::ConfigBlock,
    sqliteModel::DatabaseBlock,
    sqliteModel::Model,
    sqliteModel::ContentUri,
    sqliteModel::FunctionArg,
    sqliteModel::DDLStatement,
    sqliteModel::ConfigurationStatement,
    sqliteModel::MigrationBlock,
    DefaultValue,
    sqliteModel::ExpressionDefaultValue,
    sqliteModel::LiteralDefaultValue,
    TableDefinition,
    sqliteModel::CreateTableStatement,
    LiteralValue,
    sqliteModel::CurrentTimeLiteral,
    sqliteModel::CurrentTimeStampLiteral,
    sqliteModel::StringLiteral,
    sqliteModel::CurrentDateLiteral,
    sqliteModel::NullLiteral,
    sqliteModel::NumericLiteral,
    ColumnSource,
    sqliteModel::ResultColumn,
    ColumnConstraint,
    sqliteModel::NotNullConstraint,
    sqliteModel::UniqueConstraint,
    sqliteModel::DefaultConstraint,
    sqliteModel::PrimaryKeyColumnConstraint,
    sqliteModel::AlterTableRenameStatement,
    SelectCoreExpression,
    sqliteModel::SelectExpression,
    sqliteModel::SelectCore,
    SelectSource,
    sqliteModel::SingleSourceSelectStatement,
    sqliteModel::SingleSourceTable,
    ConfigurationStatement,
    sqliteModel::ActionStatement,
    sqliteModel::UpdateColumnExpression,
    sqliteModel::UpdateStatement,
    sqliteModel::InsertStatement,
    sqliteModel::DeleteStatement,
    ContentUriSegment,
    sqliteModel::ContentUriParamSegment,
    Expression,
    sqliteModel::NotNull,
    sqliteModel::ExprMult,
    sqliteModel::NewColumn,
    sqliteModel::OldColumn,
    sqliteModel::ExprOr,
    sqliteModel::CaseExpression,
    sqliteModel::NullCheckExpression,
    sqliteModel::ExprAdd,
    sqliteModel::SelectStatementExpression,
    sqliteModel::ExprAnd,
    sqliteModel::IsNull,
    sqliteModel::ExprRelate,
    sqliteModel::ExprEqual,
    sqliteModel::NestedExpression,
    sqliteModel::CastExpression,
    sqliteModel::ColumnSourceRef,
    sqliteModel::ExprBit,
    sqliteModel::Literal,
    sqliteModel::ExprConcat,
    sqliteModel::FunctionArgument,
    sqliteModel::Function,
    sqliteModel::ConflictClause,
    TableConstraint,
    sqliteModel::PrimaryConstraint,
    sqliteModel::CheckTableConstraint,
    sqliteModel::UniqueTableConstraint,
    sqliteModel::TableConstraint,
    sqliteModel::ColumnConstraint,
    sqliteModel::IndexedColumn,
    sqliteModel::CreateViewStatement,
    sqliteModel::DefaultValue,
    sqliteModel::ColumnDef,
    DDLStatement,
    sqliteModel::DropIndexStatement,
    sqliteModel::DropTriggerStatement,
    sqliteModel::CreateIndexStatement,
    sqliteModel::DropViewStatement,
    sqliteModel::CreateTriggerStatement,
    sqliteModel::TableDefinition,
    sqliteModel::LiteralValue,
    SingleSource,
    sqliteModel::SingleSourceJoin,
    sqliteModel::SelectSource,
    sqliteModel::JoinStatement,
    sqliteModel::DropTableStatement,
    sqliteModel::AlterTableAddColumnStatement,
    sqliteModel::DMLStatement,
    sqliteModel::GroupByExpressions,
    sqliteModel::WhereExpressions,
    sqliteModel::ColumnSource,
    sqliteModel::SelectList,
    sqliteModel::OrderingTerm,
    sqliteModel::OrderingTermList,
    SqliteDataType,
    ColumnType,
    CompoundOperator,
    ConflictResolution,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sqlitemodel::selectcoreexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectCoreExpression)


def test_sqlitemodel::selectcoreexpression_constructor_exists():
    assert callable(sqliteModel::SelectCoreExpression.__init__)


def test_sqlitemodel::selectcoreexpression_constructor_args():
    sig = inspect.signature(sqliteModel::SelectCoreExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmlstatement_is_not_abstract():
    assert not inspect.isabstract(DMLStatement)


def test_dmlstatement_constructor_exists():
    assert callable(DMLStatement.__init__)


def test_dmlstatement_constructor_args():
    sig = inspect.signature(DMLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::selectstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectStatement)


def test_sqlitemodel::selectstatement_constructor_exists():
    assert callable(sqliteModel::SelectStatement.__init__)


def test_sqlitemodel::selectstatement_constructor_args():
    sig = inspect.signature(sqliteModel::SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::case_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::Case)


def test_sqlitemodel::case_constructor_exists():
    assert callable(sqliteModel::Case.__init__)


def test_sqlitemodel::case_constructor_args():
    sig = inspect.signature(sqliteModel::Case.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::expression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::Expression)


def test_sqlitemodel::expression_constructor_exists():
    assert callable(sqliteModel::Expression.__init__)


def test_sqlitemodel::expression_constructor_args():
    sig = inspect.signature(sqliteModel::Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::contenturisegment_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ContentUriSegment)


def test_sqlitemodel::contenturisegment_constructor_exists():
    assert callable(sqliteModel::ContentUriSegment.__init__)


def test_sqlitemodel::contenturisegment_constructor_args():
    sig = inspect.signature(sqliteModel::ContentUriSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::contenturisegment_has_name():
    assert hasattr(sqliteModel::ContentUriSegment, "name")
    descriptor = None
    for klass in sqliteModel::ContentUriSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::singlesource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SingleSource)


def test_sqlitemodel::singlesource_constructor_exists():
    assert callable(sqliteModel::SingleSource.__init__)


def test_sqlitemodel::singlesource_constructor_args():
    sig = inspect.signature(sqliteModel::SingleSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::joinsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::JoinSource)


def test_sqlitemodel::joinsource_constructor_exists():
    assert callable(sqliteModel::JoinSource.__init__)


def test_sqlitemodel::joinsource_constructor_args():
    sig = inspect.signature(sqliteModel::JoinSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::havingexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::HavingExpressions)


def test_sqlitemodel::havingexpressions_constructor_exists():
    assert callable(sqliteModel::HavingExpressions.__init__)


def test_sqlitemodel::havingexpressions_constructor_args():
    sig = inspect.signature(sqliteModel::HavingExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::initblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::InitBlock)


def test_sqlitemodel::initblock_constructor_exists():
    assert callable(sqliteModel::InitBlock.__init__)


def test_sqlitemodel::initblock_constructor_args():
    sig = inspect.signature(sqliteModel::InitBlock.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::configblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ConfigBlock)


def test_sqlitemodel::configblock_constructor_exists():
    assert callable(sqliteModel::ConfigBlock.__init__)


def test_sqlitemodel::configblock_constructor_args():
    sig = inspect.signature(sqliteModel::ConfigBlock.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::databaseblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DatabaseBlock)


def test_sqlitemodel::databaseblock_constructor_exists():
    assert callable(sqliteModel::DatabaseBlock.__init__)


def test_sqlitemodel::databaseblock_constructor_args():
    sig = inspect.signature(sqliteModel::DatabaseBlock.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::databaseblock_has_name():
    assert hasattr(sqliteModel::DatabaseBlock, "name")
    descriptor = None
    for klass in sqliteModel::DatabaseBlock.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::model_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::Model)


def test_sqlitemodel::model_constructor_exists():
    assert callable(sqliteModel::Model.__init__)


def test_sqlitemodel::model_constructor_args():
    sig = inspect.signature(sqliteModel::Model.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_sqlitemodel::model_has_packageName():
    assert hasattr(sqliteModel::Model, "packageName")
    descriptor = None
    for klass in sqliteModel::Model.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::contenturi_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ContentUri)


def test_sqlitemodel::contenturi_constructor_exists():
    assert callable(sqliteModel::ContentUri.__init__)


def test_sqlitemodel::contenturi_constructor_args():
    sig = inspect.signature(sqliteModel::ContentUri.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel::contenturi_has_type():
    assert hasattr(sqliteModel::ContentUri, "type")
    descriptor = None
    for klass in sqliteModel::ContentUri.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::functionarg_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::FunctionArg)


def test_sqlitemodel::functionarg_constructor_exists():
    assert callable(sqliteModel::FunctionArg.__init__)


def test_sqlitemodel::functionarg_constructor_args():
    sig = inspect.signature(sqliteModel::FunctionArg.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::functionarg_has_type():
    assert hasattr(sqliteModel::FunctionArg, "type")
    descriptor = None
    for klass in sqliteModel::FunctionArg.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::functionarg_has_name():
    assert hasattr(sqliteModel::FunctionArg, "name")
    descriptor = None
    for klass in sqliteModel::FunctionArg.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::ddlstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DDLStatement)


def test_sqlitemodel::ddlstatement_constructor_exists():
    assert callable(sqliteModel::DDLStatement.__init__)


def test_sqlitemodel::ddlstatement_constructor_args():
    sig = inspect.signature(sqliteModel::DDLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::configurationstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ConfigurationStatement)


def test_sqlitemodel::configurationstatement_constructor_exists():
    assert callable(sqliteModel::ConfigurationStatement.__init__)


def test_sqlitemodel::configurationstatement_constructor_args():
    sig = inspect.signature(sqliteModel::ConfigurationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::configurationstatement_has_name():
    assert hasattr(sqliteModel::ConfigurationStatement, "name")
    descriptor = None
    for klass in sqliteModel::ConfigurationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::migrationblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::MigrationBlock)


def test_sqlitemodel::migrationblock_constructor_exists():
    assert callable(sqliteModel::MigrationBlock.__init__)


def test_sqlitemodel::migrationblock_constructor_args():
    sig = inspect.signature(sqliteModel::MigrationBlock.__init__)
    params = list(sig.parameters.keys())



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::expressiondefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExpressionDefaultValue)


def test_sqlitemodel::expressiondefaultvalue_constructor_exists():
    assert callable(sqliteModel::ExpressionDefaultValue.__init__)


def test_sqlitemodel::expressiondefaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel::ExpressionDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::literaldefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::LiteralDefaultValue)


def test_sqlitemodel::literaldefaultvalue_constructor_exists():
    assert callable(sqliteModel::LiteralDefaultValue.__init__)


def test_sqlitemodel::literaldefaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel::LiteralDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(TableDefinition)


def test_tabledefinition_constructor_exists():
    assert callable(TableDefinition.__init__)


def test_tabledefinition_constructor_args():
    sig = inspect.signature(TableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::createtablestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CreateTableStatement)


def test_sqlitemodel::createtablestatement_constructor_exists():
    assert callable(sqliteModel::CreateTableStatement.__init__)


def test_sqlitemodel::createtablestatement_constructor_args():
    sig = inspect.signature(sqliteModel::CreateTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "temporary" in params, "Missing parameter 'temporary'"

def test_sqlitemodel::createtablestatement_has_temporary():
    assert hasattr(sqliteModel::CreateTableStatement, "temporary")
    descriptor = None
    for klass in sqliteModel::CreateTableStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::currenttimeliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CurrentTimeLiteral)


def test_sqlitemodel::currenttimeliteral_constructor_exists():
    assert callable(sqliteModel::CurrentTimeLiteral.__init__)


def test_sqlitemodel::currenttimeliteral_constructor_args():
    sig = inspect.signature(sqliteModel::CurrentTimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel::currenttimeliteral_has_literal():
    assert hasattr(sqliteModel::CurrentTimeLiteral, "literal")
    descriptor = None
    for klass in sqliteModel::CurrentTimeLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::currenttimestampliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CurrentTimeStampLiteral)


def test_sqlitemodel::currenttimestampliteral_constructor_exists():
    assert callable(sqliteModel::CurrentTimeStampLiteral.__init__)


def test_sqlitemodel::currenttimestampliteral_constructor_args():
    sig = inspect.signature(sqliteModel::CurrentTimeStampLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel::currenttimestampliteral_has_literal():
    assert hasattr(sqliteModel::CurrentTimeStampLiteral, "literal")
    descriptor = None
    for klass in sqliteModel::CurrentTimeStampLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::stringliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::StringLiteral)


def test_sqlitemodel::stringliteral_constructor_exists():
    assert callable(sqliteModel::StringLiteral.__init__)


def test_sqlitemodel::stringliteral_constructor_args():
    sig = inspect.signature(sqliteModel::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel::stringliteral_has_literal():
    assert hasattr(sqliteModel::StringLiteral, "literal")
    descriptor = None
    for klass in sqliteModel::StringLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::currentdateliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CurrentDateLiteral)


def test_sqlitemodel::currentdateliteral_constructor_exists():
    assert callable(sqliteModel::CurrentDateLiteral.__init__)


def test_sqlitemodel::currentdateliteral_constructor_args():
    sig = inspect.signature(sqliteModel::CurrentDateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel::currentdateliteral_has_literal():
    assert hasattr(sqliteModel::CurrentDateLiteral, "literal")
    descriptor = None
    for klass in sqliteModel::CurrentDateLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::nullliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NullLiteral)


def test_sqlitemodel::nullliteral_constructor_exists():
    assert callable(sqliteModel::NullLiteral.__init__)


def test_sqlitemodel::nullliteral_constructor_args():
    sig = inspect.signature(sqliteModel::NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel::nullliteral_has_literal():
    assert hasattr(sqliteModel::NullLiteral, "literal")
    descriptor = None
    for klass in sqliteModel::NullLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::numericliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NumericLiteral)


def test_sqlitemodel::numericliteral_constructor_exists():
    assert callable(sqliteModel::NumericLiteral.__init__)


def test_sqlitemodel::numericliteral_constructor_args():
    sig = inspect.signature(sqliteModel::NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_sqlitemodel::numericliteral_has_number():
    assert hasattr(sqliteModel::NumericLiteral, "number")
    descriptor = None
    for klass in sqliteModel::NumericLiteral.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_columnsource_is_not_abstract():
    assert not inspect.isabstract(ColumnSource)


def test_columnsource_constructor_exists():
    assert callable(ColumnSource.__init__)


def test_columnsource_constructor_args():
    sig = inspect.signature(ColumnSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::resultcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ResultColumn)


def test_sqlitemodel::resultcolumn_constructor_exists():
    assert callable(sqliteModel::ResultColumn.__init__)


def test_sqlitemodel::resultcolumn_constructor_args():
    sig = inspect.signature(sqliteModel::ResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::notnullconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NotNullConstraint)


def test_sqlitemodel::notnullconstraint_constructor_exists():
    assert callable(sqliteModel::NotNullConstraint.__init__)


def test_sqlitemodel::notnullconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::NotNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::UniqueConstraint)


def test_sqlitemodel::uniqueconstraint_constructor_exists():
    assert callable(sqliteModel::UniqueConstraint.__init__)


def test_sqlitemodel::uniqueconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::defaultconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DefaultConstraint)


def test_sqlitemodel::defaultconstraint_constructor_exists():
    assert callable(sqliteModel::DefaultConstraint.__init__)


def test_sqlitemodel::defaultconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::DefaultConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::primarykeycolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::PrimaryKeyColumnConstraint)


def test_sqlitemodel::primarykeycolumnconstraint_constructor_exists():
    assert callable(sqliteModel::PrimaryKeyColumnConstraint.__init__)


def test_sqlitemodel::primarykeycolumnconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::PrimaryKeyColumnConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "autoincrement" in params, "Missing parameter 'autoincrement'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"

def test_sqlitemodel::primarykeycolumnconstraint_has_autoincrement():
    assert hasattr(sqliteModel::PrimaryKeyColumnConstraint, "autoincrement")
    descriptor = None
    for klass in sqliteModel::PrimaryKeyColumnConstraint.__mro__:
        if "autoincrement" in klass.__dict__:
            descriptor = klass.__dict__["autoincrement"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::primarykeycolumnconstraint_has_desc():
    assert hasattr(sqliteModel::PrimaryKeyColumnConstraint, "desc")
    descriptor = None
    for klass in sqliteModel::PrimaryKeyColumnConstraint.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::primarykeycolumnconstraint_has_asc():
    assert hasattr(sqliteModel::PrimaryKeyColumnConstraint, "asc")
    descriptor = None
    for klass in sqliteModel::PrimaryKeyColumnConstraint.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::altertablerenamestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::AlterTableRenameStatement)


def test_sqlitemodel::altertablerenamestatement_constructor_exists():
    assert callable(sqliteModel::AlterTableRenameStatement.__init__)


def test_sqlitemodel::altertablerenamestatement_constructor_args():
    sig = inspect.signature(sqliteModel::AlterTableRenameStatement.__init__)
    params = list(sig.parameters.keys())



def test_selectcoreexpression_is_not_abstract():
    assert not inspect.isabstract(SelectCoreExpression)


def test_selectcoreexpression_constructor_exists():
    assert callable(SelectCoreExpression.__init__)


def test_selectcoreexpression_constructor_args():
    sig = inspect.signature(SelectCoreExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::selectexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectExpression)


def test_sqlitemodel::selectexpression_constructor_exists():
    assert callable(sqliteModel::SelectExpression.__init__)


def test_sqlitemodel::selectexpression_constructor_args():
    sig = inspect.signature(sqliteModel::SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "allColumns" in params, "Missing parameter 'allColumns'"
    assert "all" in params, "Missing parameter 'all'"
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_sqlitemodel::selectexpression_has_allColumns():
    assert hasattr(sqliteModel::SelectExpression, "allColumns")
    descriptor = None
    for klass in sqliteModel::SelectExpression.__mro__:
        if "allColumns" in klass.__dict__:
            descriptor = klass.__dict__["allColumns"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::selectexpression_has_all():
    assert hasattr(sqliteModel::SelectExpression, "all")
    descriptor = None
    for klass in sqliteModel::SelectExpression.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::selectexpression_has_distinct():
    assert hasattr(sqliteModel::SelectExpression, "distinct")
    descriptor = None
    for klass in sqliteModel::SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::selectcore_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectCore)


def test_sqlitemodel::selectcore_constructor_exists():
    assert callable(sqliteModel::SelectCore.__init__)


def test_sqlitemodel::selectcore_constructor_args():
    sig = inspect.signature(sqliteModel::SelectCore.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::selectcore_has_op():
    assert hasattr(sqliteModel::SelectCore, "op")
    descriptor = None
    for klass in sqliteModel::SelectCore.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_selectsource_is_not_abstract():
    assert not inspect.isabstract(SelectSource)


def test_selectsource_constructor_exists():
    assert callable(SelectSource.__init__)


def test_selectsource_constructor_args():
    sig = inspect.signature(SelectSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::singlesourceselectstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SingleSourceSelectStatement)


def test_sqlitemodel::singlesourceselectstatement_constructor_exists():
    assert callable(sqliteModel::SingleSourceSelectStatement.__init__)


def test_sqlitemodel::singlesourceselectstatement_constructor_args():
    sig = inspect.signature(sqliteModel::SingleSourceSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::singlesourcetable_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SingleSourceTable)


def test_sqlitemodel::singlesourcetable_constructor_exists():
    assert callable(sqliteModel::SingleSourceTable.__init__)


def test_sqlitemodel::singlesourcetable_constructor_args():
    sig = inspect.signature(sqliteModel::SingleSourceTable.__init__)
    params = list(sig.parameters.keys())



def test_configurationstatement_is_not_abstract():
    assert not inspect.isabstract(ConfigurationStatement)


def test_configurationstatement_constructor_exists():
    assert callable(ConfigurationStatement.__init__)


def test_configurationstatement_constructor_args():
    sig = inspect.signature(ConfigurationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::actionstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ActionStatement)


def test_sqlitemodel::actionstatement_constructor_exists():
    assert callable(sqliteModel::ActionStatement.__init__)


def test_sqlitemodel::actionstatement_constructor_args():
    sig = inspect.signature(sqliteModel::ActionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::updatecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::UpdateColumnExpression)


def test_sqlitemodel::updatecolumnexpression_constructor_exists():
    assert callable(sqliteModel::UpdateColumnExpression.__init__)


def test_sqlitemodel::updatecolumnexpression_constructor_args():
    sig = inspect.signature(sqliteModel::UpdateColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::updatestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::UpdateStatement)


def test_sqlitemodel::updatestatement_constructor_exists():
    assert callable(sqliteModel::UpdateStatement.__init__)


def test_sqlitemodel::updatestatement_constructor_args():
    sig = inspect.signature(sqliteModel::UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "conflictResolution" in params, "Missing parameter 'conflictResolution'"

def test_sqlitemodel::updatestatement_has_conflictResolution():
    assert hasattr(sqliteModel::UpdateStatement, "conflictResolution")
    descriptor = None
    for klass in sqliteModel::UpdateStatement.__mro__:
        if "conflictResolution" in klass.__dict__:
            descriptor = klass.__dict__["conflictResolution"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::insertstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::InsertStatement)


def test_sqlitemodel::insertstatement_constructor_exists():
    assert callable(sqliteModel::InsertStatement.__init__)


def test_sqlitemodel::insertstatement_constructor_args():
    sig = inspect.signature(sqliteModel::InsertStatement.__init__)
    params = list(sig.parameters.keys())
    assert "conflictResolution" in params, "Missing parameter 'conflictResolution'"

def test_sqlitemodel::insertstatement_has_conflictResolution():
    assert hasattr(sqliteModel::InsertStatement, "conflictResolution")
    descriptor = None
    for klass in sqliteModel::InsertStatement.__mro__:
        if "conflictResolution" in klass.__dict__:
            descriptor = klass.__dict__["conflictResolution"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::deletestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DeleteStatement)


def test_sqlitemodel::deletestatement_constructor_exists():
    assert callable(sqliteModel::DeleteStatement.__init__)


def test_sqlitemodel::deletestatement_constructor_args():
    sig = inspect.signature(sqliteModel::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_contenturisegment_is_not_abstract():
    assert not inspect.isabstract(ContentUriSegment)


def test_contenturisegment_constructor_exists():
    assert callable(ContentUriSegment.__init__)


def test_contenturisegment_constructor_args():
    sig = inspect.signature(ContentUriSegment.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::contenturiparamsegment_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ContentUriParamSegment)


def test_sqlitemodel::contenturiparamsegment_constructor_exists():
    assert callable(sqliteModel::ContentUriParamSegment.__init__)


def test_sqlitemodel::contenturiparamsegment_constructor_args():
    sig = inspect.signature(sqliteModel::ContentUriParamSegment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "num" in params, "Missing parameter 'num'"

def test_sqlitemodel::contenturiparamsegment_has_text():
    assert hasattr(sqliteModel::ContentUriParamSegment, "text")
    descriptor = None
    for klass in sqliteModel::ContentUriParamSegment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::contenturiparamsegment_has_num():
    assert hasattr(sqliteModel::ContentUriParamSegment, "num")
    descriptor = None
    for klass in sqliteModel::ContentUriParamSegment.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::notnull_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NotNull)


def test_sqlitemodel::notnull_constructor_exists():
    assert callable(sqliteModel::NotNull.__init__)


def test_sqlitemodel::notnull_constructor_args():
    sig = inspect.signature(sqliteModel::NotNull.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::exprmult_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprMult)


def test_sqlitemodel::exprmult_constructor_exists():
    assert callable(sqliteModel::ExprMult.__init__)


def test_sqlitemodel::exprmult_constructor_args():
    sig = inspect.signature(sqliteModel::ExprMult.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprmult_has_op():
    assert hasattr(sqliteModel::ExprMult, "op")
    descriptor = None
    for klass in sqliteModel::ExprMult.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::newcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NewColumn)


def test_sqlitemodel::newcolumn_constructor_exists():
    assert callable(sqliteModel::NewColumn.__init__)


def test_sqlitemodel::newcolumn_constructor_args():
    sig = inspect.signature(sqliteModel::NewColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::oldcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::OldColumn)


def test_sqlitemodel::oldcolumn_constructor_exists():
    assert callable(sqliteModel::OldColumn.__init__)


def test_sqlitemodel::oldcolumn_constructor_args():
    sig = inspect.signature(sqliteModel::OldColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::expror_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprOr)


def test_sqlitemodel::expror_constructor_exists():
    assert callable(sqliteModel::ExprOr.__init__)


def test_sqlitemodel::expror_constructor_args():
    sig = inspect.signature(sqliteModel::ExprOr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::expror_has_op():
    assert hasattr(sqliteModel::ExprOr, "op")
    descriptor = None
    for klass in sqliteModel::ExprOr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::caseexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CaseExpression)


def test_sqlitemodel::caseexpression_constructor_exists():
    assert callable(sqliteModel::CaseExpression.__init__)


def test_sqlitemodel::caseexpression_constructor_args():
    sig = inspect.signature(sqliteModel::CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::nullcheckexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NullCheckExpression)


def test_sqlitemodel::nullcheckexpression_constructor_exists():
    assert callable(sqliteModel::NullCheckExpression.__init__)


def test_sqlitemodel::nullcheckexpression_constructor_args():
    sig = inspect.signature(sqliteModel::NullCheckExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::expradd_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprAdd)


def test_sqlitemodel::expradd_constructor_exists():
    assert callable(sqliteModel::ExprAdd.__init__)


def test_sqlitemodel::expradd_constructor_args():
    sig = inspect.signature(sqliteModel::ExprAdd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::expradd_has_op():
    assert hasattr(sqliteModel::ExprAdd, "op")
    descriptor = None
    for klass in sqliteModel::ExprAdd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::selectstatementexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectStatementExpression)


def test_sqlitemodel::selectstatementexpression_constructor_exists():
    assert callable(sqliteModel::SelectStatementExpression.__init__)


def test_sqlitemodel::selectstatementexpression_constructor_args():
    sig = inspect.signature(sqliteModel::SelectStatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "exists" in params, "Missing parameter 'exists'"

def test_sqlitemodel::selectstatementexpression_has_not_():
    assert hasattr(sqliteModel::SelectStatementExpression, "not_")
    descriptor = None
    for klass in sqliteModel::SelectStatementExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::selectstatementexpression_has_exists():
    assert hasattr(sqliteModel::SelectStatementExpression, "exists")
    descriptor = None
    for klass in sqliteModel::SelectStatementExpression.__mro__:
        if "exists" in klass.__dict__:
            descriptor = klass.__dict__["exists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::exprand_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprAnd)


def test_sqlitemodel::exprand_constructor_exists():
    assert callable(sqliteModel::ExprAnd.__init__)


def test_sqlitemodel::exprand_constructor_args():
    sig = inspect.signature(sqliteModel::ExprAnd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprand_has_op():
    assert hasattr(sqliteModel::ExprAnd, "op")
    descriptor = None
    for klass in sqliteModel::ExprAnd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::isnull_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::IsNull)


def test_sqlitemodel::isnull_constructor_exists():
    assert callable(sqliteModel::IsNull.__init__)


def test_sqlitemodel::isnull_constructor_args():
    sig = inspect.signature(sqliteModel::IsNull.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::exprrelate_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprRelate)


def test_sqlitemodel::exprrelate_constructor_exists():
    assert callable(sqliteModel::ExprRelate.__init__)


def test_sqlitemodel::exprrelate_constructor_args():
    sig = inspect.signature(sqliteModel::ExprRelate.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprrelate_has_op():
    assert hasattr(sqliteModel::ExprRelate, "op")
    descriptor = None
    for klass in sqliteModel::ExprRelate.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::exprequal_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprEqual)


def test_sqlitemodel::exprequal_constructor_exists():
    assert callable(sqliteModel::ExprEqual.__init__)


def test_sqlitemodel::exprequal_constructor_args():
    sig = inspect.signature(sqliteModel::ExprEqual.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprequal_has_op():
    assert hasattr(sqliteModel::ExprEqual, "op")
    descriptor = None
    for klass in sqliteModel::ExprEqual.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::NestedExpression)


def test_sqlitemodel::nestedexpression_constructor_exists():
    assert callable(sqliteModel::NestedExpression.__init__)


def test_sqlitemodel::nestedexpression_constructor_args():
    sig = inspect.signature(sqliteModel::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::castexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CastExpression)


def test_sqlitemodel::castexpression_constructor_exists():
    assert callable(sqliteModel::CastExpression.__init__)


def test_sqlitemodel::castexpression_constructor_args():
    sig = inspect.signature(sqliteModel::CastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel::castexpression_has_type():
    assert hasattr(sqliteModel::CastExpression, "type")
    descriptor = None
    for klass in sqliteModel::CastExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::columnsourceref_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ColumnSourceRef)


def test_sqlitemodel::columnsourceref_constructor_exists():
    assert callable(sqliteModel::ColumnSourceRef.__init__)


def test_sqlitemodel::columnsourceref_constructor_args():
    sig = inspect.signature(sqliteModel::ColumnSourceRef.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_sqlitemodel::columnsourceref_has_all():
    assert hasattr(sqliteModel::ColumnSourceRef, "all")
    descriptor = None
    for klass in sqliteModel::ColumnSourceRef.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::exprbit_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprBit)


def test_sqlitemodel::exprbit_constructor_exists():
    assert callable(sqliteModel::ExprBit.__init__)


def test_sqlitemodel::exprbit_constructor_args():
    sig = inspect.signature(sqliteModel::ExprBit.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprbit_has_op():
    assert hasattr(sqliteModel::ExprBit, "op")
    descriptor = None
    for klass in sqliteModel::ExprBit.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::literal_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::Literal)


def test_sqlitemodel::literal_constructor_exists():
    assert callable(sqliteModel::Literal.__init__)


def test_sqlitemodel::literal_constructor_args():
    sig = inspect.signature(sqliteModel::Literal.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::exprconcat_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ExprConcat)


def test_sqlitemodel::exprconcat_constructor_exists():
    assert callable(sqliteModel::ExprConcat.__init__)


def test_sqlitemodel::exprconcat_constructor_args():
    sig = inspect.signature(sqliteModel::ExprConcat.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel::exprconcat_has_op():
    assert hasattr(sqliteModel::ExprConcat, "op")
    descriptor = None
    for klass in sqliteModel::ExprConcat.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::functionargument_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::FunctionArgument)


def test_sqlitemodel::functionargument_constructor_exists():
    assert callable(sqliteModel::FunctionArgument.__init__)


def test_sqlitemodel::functionargument_constructor_args():
    sig = inspect.signature(sqliteModel::FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::function_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::Function)


def test_sqlitemodel::function_constructor_exists():
    assert callable(sqliteModel::Function.__init__)


def test_sqlitemodel::function_constructor_args():
    sig = inspect.signature(sqliteModel::Function.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_sqlitemodel::function_has_all():
    assert hasattr(sqliteModel::Function, "all")
    descriptor = None
    for klass in sqliteModel::Function.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::conflictclause_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ConflictClause)


def test_sqlitemodel::conflictclause_constructor_exists():
    assert callable(sqliteModel::ConflictClause.__init__)


def test_sqlitemodel::conflictclause_constructor_args():
    sig = inspect.signature(sqliteModel::ConflictClause.__init__)
    params = list(sig.parameters.keys())
    assert "resolution" in params, "Missing parameter 'resolution'"

def test_sqlitemodel::conflictclause_has_resolution():
    assert hasattr(sqliteModel::ConflictClause, "resolution")
    descriptor = None
    for klass in sqliteModel::ConflictClause.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)



def test_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(TableConstraint)


def test_tableconstraint_constructor_exists():
    assert callable(TableConstraint.__init__)


def test_tableconstraint_constructor_args():
    sig = inspect.signature(TableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::primaryconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::PrimaryConstraint)


def test_sqlitemodel::primaryconstraint_constructor_exists():
    assert callable(sqliteModel::PrimaryConstraint.__init__)


def test_sqlitemodel::primaryconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::PrimaryConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::checktableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CheckTableConstraint)


def test_sqlitemodel::checktableconstraint_constructor_exists():
    assert callable(sqliteModel::CheckTableConstraint.__init__)


def test_sqlitemodel::checktableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::CheckTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::UniqueTableConstraint)


def test_sqlitemodel::uniquetableconstraint_constructor_exists():
    assert callable(sqliteModel::UniqueTableConstraint.__init__)


def test_sqlitemodel::uniquetableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::TableConstraint)


def test_sqlitemodel::tableconstraint_constructor_exists():
    assert callable(sqliteModel::TableConstraint.__init__)


def test_sqlitemodel::tableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::tableconstraint_has_name():
    assert hasattr(sqliteModel::TableConstraint, "name")
    descriptor = None
    for klass in sqliteModel::TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::columnconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ColumnConstraint)


def test_sqlitemodel::columnconstraint_constructor_exists():
    assert callable(sqliteModel::ColumnConstraint.__init__)


def test_sqlitemodel::columnconstraint_constructor_args():
    sig = inspect.signature(sqliteModel::ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::indexedcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::IndexedColumn)


def test_sqlitemodel::indexedcolumn_constructor_exists():
    assert callable(sqliteModel::IndexedColumn.__init__)


def test_sqlitemodel::indexedcolumn_constructor_args():
    sig = inspect.signature(sqliteModel::IndexedColumn.__init__)
    params = list(sig.parameters.keys())
    assert "collationName" in params, "Missing parameter 'collationName'"
    assert "desc" in params, "Missing parameter 'desc'"
    assert "asc" in params, "Missing parameter 'asc'"

def test_sqlitemodel::indexedcolumn_has_collationName():
    assert hasattr(sqliteModel::IndexedColumn, "collationName")
    descriptor = None
    for klass in sqliteModel::IndexedColumn.__mro__:
        if "collationName" in klass.__dict__:
            descriptor = klass.__dict__["collationName"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::indexedcolumn_has_desc():
    assert hasattr(sqliteModel::IndexedColumn, "desc")
    descriptor = None
    for klass in sqliteModel::IndexedColumn.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::indexedcolumn_has_asc():
    assert hasattr(sqliteModel::IndexedColumn, "asc")
    descriptor = None
    for klass in sqliteModel::IndexedColumn.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::createviewstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CreateViewStatement)


def test_sqlitemodel::createviewstatement_constructor_exists():
    assert callable(sqliteModel::CreateViewStatement.__init__)


def test_sqlitemodel::createviewstatement_constructor_args():
    sig = inspect.signature(sqliteModel::CreateViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "temporary" in params, "Missing parameter 'temporary'"

def test_sqlitemodel::createviewstatement_has_temporary():
    assert hasattr(sqliteModel::CreateViewStatement, "temporary")
    descriptor = None
    for klass in sqliteModel::CreateViewStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::defaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DefaultValue)


def test_sqlitemodel::defaultvalue_constructor_exists():
    assert callable(sqliteModel::DefaultValue.__init__)


def test_sqlitemodel::defaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel::DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::columndef_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ColumnDef)


def test_sqlitemodel::columndef_constructor_exists():
    assert callable(sqliteModel::ColumnDef.__init__)


def test_sqlitemodel::columndef_constructor_args():
    sig = inspect.signature(sqliteModel::ColumnDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel::columndef_has_type():
    assert hasattr(sqliteModel::ColumnDef, "type")
    descriptor = None
    for klass in sqliteModel::ColumnDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(DDLStatement)


def test_ddlstatement_constructor_exists():
    assert callable(DDLStatement.__init__)


def test_ddlstatement_constructor_args():
    sig = inspect.signature(DDLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::dropindexstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DropIndexStatement)


def test_sqlitemodel::dropindexstatement_constructor_exists():
    assert callable(sqliteModel::DropIndexStatement.__init__)


def test_sqlitemodel::dropindexstatement_constructor_args():
    sig = inspect.signature(sqliteModel::DropIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel::dropindexstatement_has_ifExists():
    assert hasattr(sqliteModel::DropIndexStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel::DropIndexStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::droptriggerstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DropTriggerStatement)


def test_sqlitemodel::droptriggerstatement_constructor_exists():
    assert callable(sqliteModel::DropTriggerStatement.__init__)


def test_sqlitemodel::droptriggerstatement_constructor_args():
    sig = inspect.signature(sqliteModel::DropTriggerStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel::droptriggerstatement_has_ifExists():
    assert hasattr(sqliteModel::DropTriggerStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel::DropTriggerStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::createindexstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CreateIndexStatement)


def test_sqlitemodel::createindexstatement_constructor_exists():
    assert callable(sqliteModel::CreateIndexStatement.__init__)


def test_sqlitemodel::createindexstatement_constructor_args():
    sig = inspect.signature(sqliteModel::CreateIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_sqlitemodel::createindexstatement_has_name():
    assert hasattr(sqliteModel::CreateIndexStatement, "name")
    descriptor = None
    for klass in sqliteModel::CreateIndexStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createindexstatement_has_unique():
    assert hasattr(sqliteModel::CreateIndexStatement, "unique")
    descriptor = None
    for klass in sqliteModel::CreateIndexStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::dropviewstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DropViewStatement)


def test_sqlitemodel::dropviewstatement_constructor_exists():
    assert callable(sqliteModel::DropViewStatement.__init__)


def test_sqlitemodel::dropviewstatement_constructor_args():
    sig = inspect.signature(sqliteModel::DropViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel::dropviewstatement_has_ifExists():
    assert hasattr(sqliteModel::DropViewStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel::DropViewStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::createtriggerstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::CreateTriggerStatement)


def test_sqlitemodel::createtriggerstatement_constructor_exists():
    assert callable(sqliteModel::CreateTriggerStatement.__init__)


def test_sqlitemodel::createtriggerstatement_constructor_args():
    sig = inspect.signature(sqliteModel::CreateTriggerStatement.__init__)
    params = list(sig.parameters.keys())
    assert "forEachRow" in params, "Missing parameter 'forEachRow'"
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "temporary" in params, "Missing parameter 'temporary'"
    assert "when" in params, "Missing parameter 'when'"
    assert "updateColumnNames" in params, "Missing parameter 'updateColumnNames'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::createtriggerstatement_has_forEachRow():
    assert hasattr(sqliteModel::CreateTriggerStatement, "forEachRow")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "forEachRow" in klass.__dict__:
            descriptor = klass.__dict__["forEachRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createtriggerstatement_has_eventType():
    assert hasattr(sqliteModel::CreateTriggerStatement, "eventType")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createtriggerstatement_has_temporary():
    assert hasattr(sqliteModel::CreateTriggerStatement, "temporary")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createtriggerstatement_has_when():
    assert hasattr(sqliteModel::CreateTriggerStatement, "when")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "when" in klass.__dict__:
            descriptor = klass.__dict__["when"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createtriggerstatement_has_updateColumnNames():
    assert hasattr(sqliteModel::CreateTriggerStatement, "updateColumnNames")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "updateColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["updateColumnNames"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::createtriggerstatement_has_name():
    assert hasattr(sqliteModel::CreateTriggerStatement, "name")
    descriptor = None
    for klass in sqliteModel::CreateTriggerStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::tabledefinition_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::TableDefinition)


def test_sqlitemodel::tabledefinition_constructor_exists():
    assert callable(sqliteModel::TableDefinition.__init__)


def test_sqlitemodel::tabledefinition_constructor_args():
    sig = inspect.signature(sqliteModel::TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::tabledefinition_has_name():
    assert hasattr(sqliteModel::TableDefinition, "name")
    descriptor = None
    for klass in sqliteModel::TableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::literalvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::LiteralValue)


def test_sqlitemodel::literalvalue_constructor_exists():
    assert callable(sqliteModel::LiteralValue.__init__)


def test_sqlitemodel::literalvalue_constructor_args():
    sig = inspect.signature(sqliteModel::LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_singlesource_is_not_abstract():
    assert not inspect.isabstract(SingleSource)


def test_singlesource_constructor_exists():
    assert callable(SingleSource.__init__)


def test_singlesource_constructor_args():
    sig = inspect.signature(SingleSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::singlesourcejoin_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SingleSourceJoin)


def test_sqlitemodel::singlesourcejoin_constructor_exists():
    assert callable(sqliteModel::SingleSourceJoin.__init__)


def test_sqlitemodel::singlesourcejoin_constructor_args():
    sig = inspect.signature(sqliteModel::SingleSourceJoin.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::selectsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectSource)


def test_sqlitemodel::selectsource_constructor_exists():
    assert callable(sqliteModel::SelectSource.__init__)


def test_sqlitemodel::selectsource_constructor_args():
    sig = inspect.signature(sqliteModel::SelectSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::selectsource_has_name():
    assert hasattr(sqliteModel::SelectSource, "name")
    descriptor = None
    for klass in sqliteModel::SelectSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::joinstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::JoinStatement)


def test_sqlitemodel::joinstatement_constructor_exists():
    assert callable(sqliteModel::JoinStatement.__init__)


def test_sqlitemodel::joinstatement_constructor_args():
    sig = inspect.signature(sqliteModel::JoinStatement.__init__)
    params = list(sig.parameters.keys())
    assert "cross" in params, "Missing parameter 'cross'"
    assert "outer" in params, "Missing parameter 'outer'"
    assert "left" in params, "Missing parameter 'left'"
    assert "natural" in params, "Missing parameter 'natural'"
    assert "inner" in params, "Missing parameter 'inner'"

def test_sqlitemodel::joinstatement_has_cross():
    assert hasattr(sqliteModel::JoinStatement, "cross")
    descriptor = None
    for klass in sqliteModel::JoinStatement.__mro__:
        if "cross" in klass.__dict__:
            descriptor = klass.__dict__["cross"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::joinstatement_has_outer():
    assert hasattr(sqliteModel::JoinStatement, "outer")
    descriptor = None
    for klass in sqliteModel::JoinStatement.__mro__:
        if "outer" in klass.__dict__:
            descriptor = klass.__dict__["outer"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::joinstatement_has_left():
    assert hasattr(sqliteModel::JoinStatement, "left")
    descriptor = None
    for klass in sqliteModel::JoinStatement.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::joinstatement_has_natural():
    assert hasattr(sqliteModel::JoinStatement, "natural")
    descriptor = None
    for klass in sqliteModel::JoinStatement.__mro__:
        if "natural" in klass.__dict__:
            descriptor = klass.__dict__["natural"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::joinstatement_has_inner():
    assert hasattr(sqliteModel::JoinStatement, "inner")
    descriptor = None
    for klass in sqliteModel::JoinStatement.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::droptablestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DropTableStatement)


def test_sqlitemodel::droptablestatement_constructor_exists():
    assert callable(sqliteModel::DropTableStatement.__init__)


def test_sqlitemodel::droptablestatement_constructor_args():
    sig = inspect.signature(sqliteModel::DropTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel::droptablestatement_has_ifExists():
    assert hasattr(sqliteModel::DropTableStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel::DropTableStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::altertableaddcolumnstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::AlterTableAddColumnStatement)


def test_sqlitemodel::altertableaddcolumnstatement_constructor_exists():
    assert callable(sqliteModel::AlterTableAddColumnStatement.__init__)


def test_sqlitemodel::altertableaddcolumnstatement_constructor_args():
    sig = inspect.signature(sqliteModel::AlterTableAddColumnStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::dmlstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::DMLStatement)


def test_sqlitemodel::dmlstatement_constructor_exists():
    assert callable(sqliteModel::DMLStatement.__init__)


def test_sqlitemodel::dmlstatement_constructor_args():
    sig = inspect.signature(sqliteModel::DMLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::groupbyexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::GroupByExpressions)


def test_sqlitemodel::groupbyexpressions_constructor_exists():
    assert callable(sqliteModel::GroupByExpressions.__init__)


def test_sqlitemodel::groupbyexpressions_constructor_args():
    sig = inspect.signature(sqliteModel::GroupByExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::whereexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::WhereExpressions)


def test_sqlitemodel::whereexpressions_constructor_exists():
    assert callable(sqliteModel::WhereExpressions.__init__)


def test_sqlitemodel::whereexpressions_constructor_args():
    sig = inspect.signature(sqliteModel::WhereExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::columnsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::ColumnSource)


def test_sqlitemodel::columnsource_constructor_exists():
    assert callable(sqliteModel::ColumnSource.__init__)


def test_sqlitemodel::columnsource_constructor_args():
    sig = inspect.signature(sqliteModel::ColumnSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel::columnsource_has_name():
    assert hasattr(sqliteModel::ColumnSource, "name")
    descriptor = None
    for klass in sqliteModel::ColumnSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::selectlist_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::SelectList)


def test_sqlitemodel::selectlist_constructor_exists():
    assert callable(sqliteModel::SelectList.__init__)


def test_sqlitemodel::selectlist_constructor_args():
    sig = inspect.signature(sqliteModel::SelectList.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel::orderingterm_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::OrderingTerm)


def test_sqlitemodel::orderingterm_constructor_exists():
    assert callable(sqliteModel::OrderingTerm.__init__)


def test_sqlitemodel::orderingterm_constructor_args():
    sig = inspect.signature(sqliteModel::OrderingTerm.__init__)
    params = list(sig.parameters.keys())
    assert "asc" in params, "Missing parameter 'asc'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_sqlitemodel::orderingterm_has_asc():
    assert hasattr(sqliteModel::OrderingTerm, "asc")
    descriptor = None
    for klass in sqliteModel::OrderingTerm.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel::orderingterm_has_desc():
    assert hasattr(sqliteModel::OrderingTerm, "desc")
    descriptor = None
    for klass in sqliteModel::OrderingTerm.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel::orderingtermlist_is_not_abstract():
    assert not inspect.isabstract(sqliteModel::OrderingTermList)


def test_sqlitemodel::orderingtermlist_constructor_exists():
    assert callable(sqliteModel::OrderingTermList.__init__)


def test_sqlitemodel::orderingtermlist_constructor_args():
    sig = inspect.signature(sqliteModel::OrderingTermList.__init__)
    params = list(sig.parameters.keys())

def test_sqlitedatatype_exists():
    # Check that the Enumeration exists
    assert SqliteDataType is not None

def test_sqlitedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SqliteDataType]
    expected_literals = [
        "integer",
        "none",
        "blob",
        "text",
        "numeric",
        "real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SqliteDataType"

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "integer",
        "boolean",
        "real",
        "blob",
        "text",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"

def test_compoundoperator_exists():
    # Check that the Enumeration exists
    assert CompoundOperator is not None

def test_compoundoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompoundOperator]
    expected_literals = [
        "intersect",
        "unionall",
        "except_",
        "union",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompoundOperator"

def test_conflictresolution_exists():
    # Check that the Enumeration exists
    assert ConflictResolution is not None

def test_conflictresolution_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConflictResolution]
    expected_literals = [
        "rollback",
        "ignore",
        "fail",
        "abort",
        "replace",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConflictResolution"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
sqliteModel::SelectCoreExpression_strategy = st.builds(
    sqliteModel::SelectCoreExpression,
)
DMLStatement_strategy = st.builds(
    DMLStatement,
)
sqliteModel::SelectStatement_strategy = st.builds(
    sqliteModel::SelectStatement,
)
sqliteModel::Case_strategy = st.builds(
    sqliteModel::Case,
)
sqliteModel::Expression_strategy = st.builds(
    sqliteModel::Expression,
)
sqliteModel::ContentUriSegment_strategy = st.builds(
    sqliteModel::ContentUriSegment,
    name=
        safe_text
)
sqliteModel::SingleSource_strategy = st.builds(
    sqliteModel::SingleSource,
)
sqliteModel::JoinSource_strategy = st.builds(
    sqliteModel::JoinSource,
)
sqliteModel::HavingExpressions_strategy = st.builds(
    sqliteModel::HavingExpressions,
)
sqliteModel::InitBlock_strategy = st.builds(
    sqliteModel::InitBlock,
)
sqliteModel::ConfigBlock_strategy = st.builds(
    sqliteModel::ConfigBlock,
)
sqliteModel::DatabaseBlock_strategy = st.builds(
    sqliteModel::DatabaseBlock,
    name=
        safe_text
)
sqliteModel::Model_strategy = st.builds(
    sqliteModel::Model,
    packageName=
        safe_text
)
sqliteModel::ContentUri_strategy = st.builds(
    sqliteModel::ContentUri,
    type=
        safe_text
)
sqliteModel::FunctionArg_strategy = st.builds(
    sqliteModel::FunctionArg,
    type=
        safe_text,
    name=
        safe_text
)
sqliteModel::DDLStatement_strategy = st.builds(
    sqliteModel::DDLStatement,
)
sqliteModel::ConfigurationStatement_strategy = st.builds(
    sqliteModel::ConfigurationStatement,
    name=
        safe_text
)
sqliteModel::MigrationBlock_strategy = st.builds(
    sqliteModel::MigrationBlock,
)
DefaultValue_strategy = st.builds(
    DefaultValue,
)
sqliteModel::ExpressionDefaultValue_strategy = st.builds(
    sqliteModel::ExpressionDefaultValue,
)
sqliteModel::LiteralDefaultValue_strategy = st.builds(
    sqliteModel::LiteralDefaultValue,
)
TableDefinition_strategy = st.builds(
    TableDefinition,
)
sqliteModel::CreateTableStatement_strategy = st.builds(
    sqliteModel::CreateTableStatement,
    temporary=
        st.booleans()
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
sqliteModel::CurrentTimeLiteral_strategy = st.builds(
    sqliteModel::CurrentTimeLiteral,
    literal=
        safe_text
)
sqliteModel::CurrentTimeStampLiteral_strategy = st.builds(
    sqliteModel::CurrentTimeStampLiteral,
    literal=
        safe_text
)
sqliteModel::StringLiteral_strategy = st.builds(
    sqliteModel::StringLiteral,
    literal=
        safe_text
)
sqliteModel::CurrentDateLiteral_strategy = st.builds(
    sqliteModel::CurrentDateLiteral,
    literal=
        safe_text
)
sqliteModel::NullLiteral_strategy = st.builds(
    sqliteModel::NullLiteral,
    literal=
        safe_text
)
sqliteModel::NumericLiteral_strategy = st.builds(
    sqliteModel::NumericLiteral,
    number=
        safe_text
)
ColumnSource_strategy = st.builds(
    ColumnSource,
)
sqliteModel::ResultColumn_strategy = st.builds(
    sqliteModel::ResultColumn,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
sqliteModel::NotNullConstraint_strategy = st.builds(
    sqliteModel::NotNullConstraint,
)
sqliteModel::UniqueConstraint_strategy = st.builds(
    sqliteModel::UniqueConstraint,
)
sqliteModel::DefaultConstraint_strategy = st.builds(
    sqliteModel::DefaultConstraint,
)
sqliteModel::PrimaryKeyColumnConstraint_strategy = st.builds(
    sqliteModel::PrimaryKeyColumnConstraint,
    autoincrement=
        st.booleans(),
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
sqliteModel::AlterTableRenameStatement_strategy = st.builds(
    sqliteModel::AlterTableRenameStatement,
)
SelectCoreExpression_strategy = st.builds(
    SelectCoreExpression,
)
sqliteModel::SelectExpression_strategy = st.builds(
    sqliteModel::SelectExpression,
    allColumns=
        st.booleans(),
    all=
        st.booleans(),
    distinct=
        st.booleans()
)
sqliteModel::SelectCore_strategy = st.builds(
    sqliteModel::SelectCore,
    op=
        safe_text
)
SelectSource_strategy = st.builds(
    SelectSource,
)
sqliteModel::SingleSourceSelectStatement_strategy = st.builds(
    sqliteModel::SingleSourceSelectStatement,
)
sqliteModel::SingleSourceTable_strategy = st.builds(
    sqliteModel::SingleSourceTable,
)
ConfigurationStatement_strategy = st.builds(
    ConfigurationStatement,
)
sqliteModel::ActionStatement_strategy = st.builds(
    sqliteModel::ActionStatement,
)
sqliteModel::UpdateColumnExpression_strategy = st.builds(
    sqliteModel::UpdateColumnExpression,
)
sqliteModel::UpdateStatement_strategy = st.builds(
    sqliteModel::UpdateStatement,
    conflictResolution=
        safe_text
)
sqliteModel::InsertStatement_strategy = st.builds(
    sqliteModel::InsertStatement,
    conflictResolution=
        safe_text
)
sqliteModel::DeleteStatement_strategy = st.builds(
    sqliteModel::DeleteStatement,
)
ContentUriSegment_strategy = st.builds(
    ContentUriSegment,
)
sqliteModel::ContentUriParamSegment_strategy = st.builds(
    sqliteModel::ContentUriParamSegment,
    text=
        st.booleans(),
    num=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
sqliteModel::NotNull_strategy = st.builds(
    sqliteModel::NotNull,
)
sqliteModel::ExprMult_strategy = st.builds(
    sqliteModel::ExprMult,
    op=
        safe_text
)
sqliteModel::NewColumn_strategy = st.builds(
    sqliteModel::NewColumn,
)
sqliteModel::OldColumn_strategy = st.builds(
    sqliteModel::OldColumn,
)
sqliteModel::ExprOr_strategy = st.builds(
    sqliteModel::ExprOr,
    op=
        safe_text
)
sqliteModel::CaseExpression_strategy = st.builds(
    sqliteModel::CaseExpression,
)
sqliteModel::NullCheckExpression_strategy = st.builds(
    sqliteModel::NullCheckExpression,
)
sqliteModel::ExprAdd_strategy = st.builds(
    sqliteModel::ExprAdd,
    op=
        safe_text
)
sqliteModel::SelectStatementExpression_strategy = st.builds(
    sqliteModel::SelectStatementExpression,
    not_=
        st.booleans(),
    exists=
        st.booleans()
)
sqliteModel::ExprAnd_strategy = st.builds(
    sqliteModel::ExprAnd,
    op=
        safe_text
)
sqliteModel::IsNull_strategy = st.builds(
    sqliteModel::IsNull,
)
sqliteModel::ExprRelate_strategy = st.builds(
    sqliteModel::ExprRelate,
    op=
        safe_text
)
sqliteModel::ExprEqual_strategy = st.builds(
    sqliteModel::ExprEqual,
    op=
        safe_text
)
sqliteModel::NestedExpression_strategy = st.builds(
    sqliteModel::NestedExpression,
)
sqliteModel::CastExpression_strategy = st.builds(
    sqliteModel::CastExpression,
    type=
        safe_text
)
sqliteModel::ColumnSourceRef_strategy = st.builds(
    sqliteModel::ColumnSourceRef,
    all=
        st.booleans()
)
sqliteModel::ExprBit_strategy = st.builds(
    sqliteModel::ExprBit,
    op=
        safe_text
)
sqliteModel::Literal_strategy = st.builds(
    sqliteModel::Literal,
)
sqliteModel::ExprConcat_strategy = st.builds(
    sqliteModel::ExprConcat,
    op=
        safe_text
)
sqliteModel::FunctionArgument_strategy = st.builds(
    sqliteModel::FunctionArgument,
)
sqliteModel::Function_strategy = st.builds(
    sqliteModel::Function,
    all=
        st.booleans()
)
sqliteModel::ConflictClause_strategy = st.builds(
    sqliteModel::ConflictClause,
    resolution=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sqliteModel::PrimaryConstraint_strategy = st.builds(
    sqliteModel::PrimaryConstraint,
)
sqliteModel::CheckTableConstraint_strategy = st.builds(
    sqliteModel::CheckTableConstraint,
)
sqliteModel::UniqueTableConstraint_strategy = st.builds(
    sqliteModel::UniqueTableConstraint,
)
sqliteModel::TableConstraint_strategy = st.builds(
    sqliteModel::TableConstraint,
    name=
        safe_text
)
sqliteModel::ColumnConstraint_strategy = st.builds(
    sqliteModel::ColumnConstraint,
)
sqliteModel::IndexedColumn_strategy = st.builds(
    sqliteModel::IndexedColumn,
    collationName=
        safe_text,
    desc=
        st.booleans(),
    asc=
        st.booleans()
)
sqliteModel::CreateViewStatement_strategy = st.builds(
    sqliteModel::CreateViewStatement,
    temporary=
        st.booleans()
)
sqliteModel::DefaultValue_strategy = st.builds(
    sqliteModel::DefaultValue,
)
sqliteModel::ColumnDef_strategy = st.builds(
    sqliteModel::ColumnDef,
    type=
        safe_text
)
DDLStatement_strategy = st.builds(
    DDLStatement,
)
sqliteModel::DropIndexStatement_strategy = st.builds(
    sqliteModel::DropIndexStatement,
    ifExists=
        st.booleans()
)
sqliteModel::DropTriggerStatement_strategy = st.builds(
    sqliteModel::DropTriggerStatement,
    ifExists=
        st.booleans()
)
sqliteModel::CreateIndexStatement_strategy = st.builds(
    sqliteModel::CreateIndexStatement,
    name=
        safe_text,
    unique=
        st.booleans()
)
sqliteModel::DropViewStatement_strategy = st.builds(
    sqliteModel::DropViewStatement,
    ifExists=
        st.booleans()
)
sqliteModel::CreateTriggerStatement_strategy = st.builds(
    sqliteModel::CreateTriggerStatement,
    forEachRow=
        safe_text,
    eventType=
        safe_text,
    temporary=
        st.booleans(),
    when=
        safe_text,
    updateColumnNames=
        safe_text,
    name=
        safe_text
)
sqliteModel::TableDefinition_strategy = st.builds(
    sqliteModel::TableDefinition,
    name=
        safe_text
)
sqliteModel::LiteralValue_strategy = st.builds(
    sqliteModel::LiteralValue,
)
SingleSource_strategy = st.builds(
    SingleSource,
)
sqliteModel::SingleSourceJoin_strategy = st.builds(
    sqliteModel::SingleSourceJoin,
)
sqliteModel::SelectSource_strategy = st.builds(
    sqliteModel::SelectSource,
    name=
        safe_text
)
sqliteModel::JoinStatement_strategy = st.builds(
    sqliteModel::JoinStatement,
    cross=
        st.booleans(),
    outer=
        st.booleans(),
    left=
        st.booleans(),
    natural=
        st.booleans(),
    inner=
        st.booleans()
)
sqliteModel::DropTableStatement_strategy = st.builds(
    sqliteModel::DropTableStatement,
    ifExists=
        st.booleans()
)
sqliteModel::AlterTableAddColumnStatement_strategy = st.builds(
    sqliteModel::AlterTableAddColumnStatement,
)
sqliteModel::DMLStatement_strategy = st.builds(
    sqliteModel::DMLStatement,
)
sqliteModel::GroupByExpressions_strategy = st.builds(
    sqliteModel::GroupByExpressions,
)
sqliteModel::WhereExpressions_strategy = st.builds(
    sqliteModel::WhereExpressions,
)
sqliteModel::ColumnSource_strategy = st.builds(
    sqliteModel::ColumnSource,
    name=
        safe_text
)
sqliteModel::SelectList_strategy = st.builds(
    sqliteModel::SelectList,
)
sqliteModel::OrderingTerm_strategy = st.builds(
    sqliteModel::OrderingTerm,
    asc=
        st.booleans(),
    desc=
        st.booleans()
)
sqliteModel::OrderingTermList_strategy = st.builds(
    sqliteModel::OrderingTermList,
)

@given(instance=sqliteModel::SelectCoreExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectcoreexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectCoreExpression)

@given(instance=DMLStatement_strategy)
@settings(max_examples=50)
def test_dmlstatement_instantiation(instance):
    assert isinstance(instance, DMLStatement)

@given(instance=sqliteModel::SelectStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectStatement)

@given(instance=sqliteModel::Case_strategy)
@settings(max_examples=50)
def test_sqlitemodel::case_instantiation(instance):
    assert isinstance(instance, sqliteModel::Case)

@given(instance=sqliteModel::Expression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::expression_instantiation(instance):
    assert isinstance(instance, sqliteModel::Expression)

@given(instance=sqliteModel::ContentUriSegment_strategy)
@settings(max_examples=50)
def test_sqlitemodel::contenturisegment_instantiation(instance):
    assert isinstance(instance, sqliteModel::ContentUriSegment)

@given(instance=sqliteModel::ContentUriSegment_strategy)
def test_sqlitemodel::contenturisegment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::ContentUriSegment_strategy)
def test_sqlitemodel::contenturisegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::SingleSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel::singlesource_instantiation(instance):
    assert isinstance(instance, sqliteModel::SingleSource)

@given(instance=sqliteModel::JoinSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel::joinsource_instantiation(instance):
    assert isinstance(instance, sqliteModel::JoinSource)

@given(instance=sqliteModel::HavingExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel::havingexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel::HavingExpressions)

@given(instance=sqliteModel::InitBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel::initblock_instantiation(instance):
    assert isinstance(instance, sqliteModel::InitBlock)

@given(instance=sqliteModel::ConfigBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel::configblock_instantiation(instance):
    assert isinstance(instance, sqliteModel::ConfigBlock)

@given(instance=sqliteModel::DatabaseBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel::databaseblock_instantiation(instance):
    assert isinstance(instance, sqliteModel::DatabaseBlock)

@given(instance=sqliteModel::DatabaseBlock_strategy)
def test_sqlitemodel::databaseblock_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::DatabaseBlock_strategy)
def test_sqlitemodel::databaseblock_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::Model_strategy)
@settings(max_examples=50)
def test_sqlitemodel::model_instantiation(instance):
    assert isinstance(instance, sqliteModel::Model)

@given(instance=sqliteModel::Model_strategy)
def test_sqlitemodel::model_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=sqliteModel::Model_strategy)
def test_sqlitemodel::model_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

@given(instance=sqliteModel::ContentUri_strategy)
@settings(max_examples=50)
def test_sqlitemodel::contenturi_instantiation(instance):
    assert isinstance(instance, sqliteModel::ContentUri)

@given(instance=sqliteModel::ContentUri_strategy)
def test_sqlitemodel::contenturi_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sqliteModel::ContentUri_strategy)
def test_sqlitemodel::contenturi_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel::FunctionArg_strategy)
@settings(max_examples=50)
def test_sqlitemodel::functionarg_instantiation(instance):
    assert isinstance(instance, sqliteModel::FunctionArg)

@given(instance=sqliteModel::FunctionArg_strategy)
def test_sqlitemodel::functionarg_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sqliteModel::FunctionArg_strategy)
def test_sqlitemodel::functionarg_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel::FunctionArg_strategy)
def test_sqlitemodel::functionarg_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::FunctionArg_strategy)
def test_sqlitemodel::functionarg_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::DDLStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::ddlstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DDLStatement)

@given(instance=sqliteModel::ConfigurationStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::configurationstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::ConfigurationStatement)

@given(instance=sqliteModel::ConfigurationStatement_strategy)
def test_sqlitemodel::configurationstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::ConfigurationStatement_strategy)
def test_sqlitemodel::configurationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::MigrationBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel::migrationblock_instantiation(instance):
    assert isinstance(instance, sqliteModel::MigrationBlock)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=sqliteModel::ExpressionDefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel::expressiondefaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExpressionDefaultValue)

@given(instance=sqliteModel::LiteralDefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel::literaldefaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel::LiteralDefaultValue)

@given(instance=TableDefinition_strategy)
@settings(max_examples=50)
def test_tabledefinition_instantiation(instance):
    assert isinstance(instance, TableDefinition)

@given(instance=sqliteModel::CreateTableStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::createtablestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::CreateTableStatement)

@given(instance=sqliteModel::CreateTableStatement_strategy)
def test_sqlitemodel::createtablestatement_temporary_type(instance):
    assert isinstance(instance.temporary, bool)


@given(instance=sqliteModel::CreateTableStatement_strategy)
def test_sqlitemodel::createtablestatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=sqliteModel::CurrentTimeLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::currenttimeliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::CurrentTimeLiteral)

@given(instance=sqliteModel::CurrentTimeLiteral_strategy)
def test_sqlitemodel::currenttimeliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=sqliteModel::CurrentTimeLiteral_strategy)
def test_sqlitemodel::currenttimeliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel::CurrentTimeStampLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::currenttimestampliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::CurrentTimeStampLiteral)

@given(instance=sqliteModel::CurrentTimeStampLiteral_strategy)
def test_sqlitemodel::currenttimestampliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=sqliteModel::CurrentTimeStampLiteral_strategy)
def test_sqlitemodel::currenttimestampliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel::StringLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::stringliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::StringLiteral)

@given(instance=sqliteModel::StringLiteral_strategy)
def test_sqlitemodel::stringliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=sqliteModel::StringLiteral_strategy)
def test_sqlitemodel::stringliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel::CurrentDateLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::currentdateliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::CurrentDateLiteral)

@given(instance=sqliteModel::CurrentDateLiteral_strategy)
def test_sqlitemodel::currentdateliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=sqliteModel::CurrentDateLiteral_strategy)
def test_sqlitemodel::currentdateliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel::NullLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::nullliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::NullLiteral)

@given(instance=sqliteModel::NullLiteral_strategy)
def test_sqlitemodel::nullliteral_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=sqliteModel::NullLiteral_strategy)
def test_sqlitemodel::nullliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel::NumericLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel::numericliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel::NumericLiteral)

@given(instance=sqliteModel::NumericLiteral_strategy)
def test_sqlitemodel::numericliteral_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=sqliteModel::NumericLiteral_strategy)
def test_sqlitemodel::numericliteral_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=ColumnSource_strategy)
@settings(max_examples=50)
def test_columnsource_instantiation(instance):
    assert isinstance(instance, ColumnSource)

@given(instance=sqliteModel::ResultColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel::resultcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel::ResultColumn)

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=sqliteModel::NotNullConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::notnullconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::NotNullConstraint)

@given(instance=sqliteModel::UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::UniqueConstraint)

@given(instance=sqliteModel::DefaultConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::defaultconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::DefaultConstraint)

@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::primarykeycolumnconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::PrimaryKeyColumnConstraint)

@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_autoincrement_type(instance):
    assert isinstance(instance.autoincrement, bool)


@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_autoincrement_setter(instance):
    original = instance.autoincrement
    instance.autoincrement = original
    assert instance.autoincrement == original

@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_desc_type(instance):
    assert isinstance(instance.desc, bool)


@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_asc_type(instance):
    assert isinstance(instance.asc, bool)


@given(instance=sqliteModel::PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel::primarykeycolumnconstraint_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=sqliteModel::AlterTableRenameStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::altertablerenamestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::AlterTableRenameStatement)

@given(instance=SelectCoreExpression_strategy)
@settings(max_examples=50)
def test_selectcoreexpression_instantiation(instance):
    assert isinstance(instance, SelectCoreExpression)

@given(instance=sqliteModel::SelectExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectExpression)

@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_allColumns_type(instance):
    assert isinstance(instance.allColumns, bool)


@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_allColumns_setter(instance):
    original = instance.allColumns
    instance.allColumns = original
    assert instance.allColumns == original

@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_distinct_type(instance):
    assert isinstance(instance.distinct, bool)


@given(instance=sqliteModel::SelectExpression_strategy)
def test_sqlitemodel::selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=sqliteModel::SelectCore_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectcore_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectCore)

@given(instance=sqliteModel::SelectCore_strategy)
def test_sqlitemodel::selectcore_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::SelectCore_strategy)
def test_sqlitemodel::selectcore_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=SelectSource_strategy)
@settings(max_examples=50)
def test_selectsource_instantiation(instance):
    assert isinstance(instance, SelectSource)

@given(instance=sqliteModel::SingleSourceSelectStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::singlesourceselectstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::SingleSourceSelectStatement)

@given(instance=sqliteModel::SingleSourceTable_strategy)
@settings(max_examples=50)
def test_sqlitemodel::singlesourcetable_instantiation(instance):
    assert isinstance(instance, sqliteModel::SingleSourceTable)

@given(instance=ConfigurationStatement_strategy)
@settings(max_examples=50)
def test_configurationstatement_instantiation(instance):
    assert isinstance(instance, ConfigurationStatement)

@given(instance=sqliteModel::ActionStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::actionstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::ActionStatement)

@given(instance=sqliteModel::UpdateColumnExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::updatecolumnexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::UpdateColumnExpression)

@given(instance=sqliteModel::UpdateStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::updatestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::UpdateStatement)

@given(instance=sqliteModel::UpdateStatement_strategy)
def test_sqlitemodel::updatestatement_conflictResolution_type(instance):
    assert isinstance(instance.conflictResolution, str)


@given(instance=sqliteModel::UpdateStatement_strategy)
def test_sqlitemodel::updatestatement_conflictResolution_setter(instance):
    original = instance.conflictResolution
    instance.conflictResolution = original
    assert instance.conflictResolution == original

@given(instance=sqliteModel::InsertStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::insertstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::InsertStatement)

@given(instance=sqliteModel::InsertStatement_strategy)
def test_sqlitemodel::insertstatement_conflictResolution_type(instance):
    assert isinstance(instance.conflictResolution, str)


@given(instance=sqliteModel::InsertStatement_strategy)
def test_sqlitemodel::insertstatement_conflictResolution_setter(instance):
    original = instance.conflictResolution
    instance.conflictResolution = original
    assert instance.conflictResolution == original

@given(instance=sqliteModel::DeleteStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::deletestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DeleteStatement)

@given(instance=ContentUriSegment_strategy)
@settings(max_examples=50)
def test_contenturisegment_instantiation(instance):
    assert isinstance(instance, ContentUriSegment)

@given(instance=sqliteModel::ContentUriParamSegment_strategy)
@settings(max_examples=50)
def test_sqlitemodel::contenturiparamsegment_instantiation(instance):
    assert isinstance(instance, sqliteModel::ContentUriParamSegment)

@given(instance=sqliteModel::ContentUriParamSegment_strategy)
def test_sqlitemodel::contenturiparamsegment_text_type(instance):
    assert isinstance(instance.text, bool)


@given(instance=sqliteModel::ContentUriParamSegment_strategy)
def test_sqlitemodel::contenturiparamsegment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=sqliteModel::ContentUriParamSegment_strategy)
def test_sqlitemodel::contenturiparamsegment_num_type(instance):
    assert isinstance(instance.num, bool)


@given(instance=sqliteModel::ContentUriParamSegment_strategy)
def test_sqlitemodel::contenturiparamsegment_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sqliteModel::NotNull_strategy)
@settings(max_examples=50)
def test_sqlitemodel::notnull_instantiation(instance):
    assert isinstance(instance, sqliteModel::NotNull)

@given(instance=sqliteModel::ExprMult_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprmult_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprMult)

@given(instance=sqliteModel::ExprMult_strategy)
def test_sqlitemodel::exprmult_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprMult_strategy)
def test_sqlitemodel::exprmult_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::NewColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel::newcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel::NewColumn)

@given(instance=sqliteModel::OldColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel::oldcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel::OldColumn)

@given(instance=sqliteModel::ExprOr_strategy)
@settings(max_examples=50)
def test_sqlitemodel::expror_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprOr)

@given(instance=sqliteModel::ExprOr_strategy)
def test_sqlitemodel::expror_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprOr_strategy)
def test_sqlitemodel::expror_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::CaseExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::caseexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::CaseExpression)

@given(instance=sqliteModel::NullCheckExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::nullcheckexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::NullCheckExpression)

@given(instance=sqliteModel::ExprAdd_strategy)
@settings(max_examples=50)
def test_sqlitemodel::expradd_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprAdd)

@given(instance=sqliteModel::ExprAdd_strategy)
def test_sqlitemodel::expradd_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprAdd_strategy)
def test_sqlitemodel::expradd_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::SelectStatementExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectstatementexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectStatementExpression)

@given(instance=sqliteModel::SelectStatementExpression_strategy)
def test_sqlitemodel::selectstatementexpression_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=sqliteModel::SelectStatementExpression_strategy)
def test_sqlitemodel::selectstatementexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=sqliteModel::SelectStatementExpression_strategy)
def test_sqlitemodel::selectstatementexpression_exists_type(instance):
    assert isinstance(instance.exists, bool)


@given(instance=sqliteModel::SelectStatementExpression_strategy)
def test_sqlitemodel::selectstatementexpression_exists_setter(instance):
    original = instance.exists
    instance.exists = original
    assert instance.exists == original

@given(instance=sqliteModel::ExprAnd_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprand_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprAnd)

@given(instance=sqliteModel::ExprAnd_strategy)
def test_sqlitemodel::exprand_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprAnd_strategy)
def test_sqlitemodel::exprand_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::IsNull_strategy)
@settings(max_examples=50)
def test_sqlitemodel::isnull_instantiation(instance):
    assert isinstance(instance, sqliteModel::IsNull)

@given(instance=sqliteModel::ExprRelate_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprrelate_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprRelate)

@given(instance=sqliteModel::ExprRelate_strategy)
def test_sqlitemodel::exprrelate_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprRelate_strategy)
def test_sqlitemodel::exprrelate_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::ExprEqual_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprequal_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprEqual)

@given(instance=sqliteModel::ExprEqual_strategy)
def test_sqlitemodel::exprequal_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprEqual_strategy)
def test_sqlitemodel::exprequal_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::NestedExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::nestedexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::NestedExpression)

@given(instance=sqliteModel::CastExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel::castexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel::CastExpression)

@given(instance=sqliteModel::CastExpression_strategy)
def test_sqlitemodel::castexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sqliteModel::CastExpression_strategy)
def test_sqlitemodel::castexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel::ColumnSourceRef_strategy)
@settings(max_examples=50)
def test_sqlitemodel::columnsourceref_instantiation(instance):
    assert isinstance(instance, sqliteModel::ColumnSourceRef)

@given(instance=sqliteModel::ColumnSourceRef_strategy)
def test_sqlitemodel::columnsourceref_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=sqliteModel::ColumnSourceRef_strategy)
def test_sqlitemodel::columnsourceref_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sqliteModel::ExprBit_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprbit_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprBit)

@given(instance=sqliteModel::ExprBit_strategy)
def test_sqlitemodel::exprbit_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprBit_strategy)
def test_sqlitemodel::exprbit_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::Literal_strategy)
@settings(max_examples=50)
def test_sqlitemodel::literal_instantiation(instance):
    assert isinstance(instance, sqliteModel::Literal)

@given(instance=sqliteModel::ExprConcat_strategy)
@settings(max_examples=50)
def test_sqlitemodel::exprconcat_instantiation(instance):
    assert isinstance(instance, sqliteModel::ExprConcat)

@given(instance=sqliteModel::ExprConcat_strategy)
def test_sqlitemodel::exprconcat_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sqliteModel::ExprConcat_strategy)
def test_sqlitemodel::exprconcat_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel::FunctionArgument_strategy)
@settings(max_examples=50)
def test_sqlitemodel::functionargument_instantiation(instance):
    assert isinstance(instance, sqliteModel::FunctionArgument)

@given(instance=sqliteModel::Function_strategy)
@settings(max_examples=50)
def test_sqlitemodel::function_instantiation(instance):
    assert isinstance(instance, sqliteModel::Function)

@given(instance=sqliteModel::Function_strategy)
def test_sqlitemodel::function_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=sqliteModel::Function_strategy)
def test_sqlitemodel::function_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sqliteModel::ConflictClause_strategy)
@settings(max_examples=50)
def test_sqlitemodel::conflictclause_instantiation(instance):
    assert isinstance(instance, sqliteModel::ConflictClause)

@given(instance=sqliteModel::ConflictClause_strategy)
def test_sqlitemodel::conflictclause_resolution_type(instance):
    assert isinstance(instance.resolution, str)


@given(instance=sqliteModel::ConflictClause_strategy)
def test_sqlitemodel::conflictclause_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sqliteModel::PrimaryConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::primaryconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::PrimaryConstraint)

@given(instance=sqliteModel::CheckTableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::checktableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::CheckTableConstraint)

@given(instance=sqliteModel::UniqueTableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::uniquetableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::UniqueTableConstraint)

@given(instance=sqliteModel::TableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::tableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::TableConstraint)

@given(instance=sqliteModel::TableConstraint_strategy)
def test_sqlitemodel::tableconstraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::TableConstraint_strategy)
def test_sqlitemodel::tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel::columnconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel::ColumnConstraint)

@given(instance=sqliteModel::IndexedColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel::indexedcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel::IndexedColumn)

@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_collationName_type(instance):
    assert isinstance(instance.collationName, str)


@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_collationName_setter(instance):
    original = instance.collationName
    instance.collationName = original
    assert instance.collationName == original

@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_desc_type(instance):
    assert isinstance(instance.desc, bool)


@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_asc_type(instance):
    assert isinstance(instance.asc, bool)


@given(instance=sqliteModel::IndexedColumn_strategy)
def test_sqlitemodel::indexedcolumn_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=sqliteModel::CreateViewStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::createviewstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::CreateViewStatement)

@given(instance=sqliteModel::CreateViewStatement_strategy)
def test_sqlitemodel::createviewstatement_temporary_type(instance):
    assert isinstance(instance.temporary, bool)


@given(instance=sqliteModel::CreateViewStatement_strategy)
def test_sqlitemodel::createviewstatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original

@given(instance=sqliteModel::DefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel::defaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel::DefaultValue)

@given(instance=sqliteModel::ColumnDef_strategy)
@settings(max_examples=50)
def test_sqlitemodel::columndef_instantiation(instance):
    assert isinstance(instance, sqliteModel::ColumnDef)

@given(instance=sqliteModel::ColumnDef_strategy)
def test_sqlitemodel::columndef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sqliteModel::ColumnDef_strategy)
def test_sqlitemodel::columndef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DDLStatement_strategy)
@settings(max_examples=50)
def test_ddlstatement_instantiation(instance):
    assert isinstance(instance, DDLStatement)

@given(instance=sqliteModel::DropIndexStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::dropindexstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DropIndexStatement)

@given(instance=sqliteModel::DropIndexStatement_strategy)
def test_sqlitemodel::dropindexstatement_ifExists_type(instance):
    assert isinstance(instance.ifExists, bool)


@given(instance=sqliteModel::DropIndexStatement_strategy)
def test_sqlitemodel::dropindexstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel::DropTriggerStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::droptriggerstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DropTriggerStatement)

@given(instance=sqliteModel::DropTriggerStatement_strategy)
def test_sqlitemodel::droptriggerstatement_ifExists_type(instance):
    assert isinstance(instance.ifExists, bool)


@given(instance=sqliteModel::DropTriggerStatement_strategy)
def test_sqlitemodel::droptriggerstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel::CreateIndexStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::createindexstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::CreateIndexStatement)

@given(instance=sqliteModel::CreateIndexStatement_strategy)
def test_sqlitemodel::createindexstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::CreateIndexStatement_strategy)
def test_sqlitemodel::createindexstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::CreateIndexStatement_strategy)
def test_sqlitemodel::createindexstatement_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=sqliteModel::CreateIndexStatement_strategy)
def test_sqlitemodel::createindexstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=sqliteModel::DropViewStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::dropviewstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DropViewStatement)

@given(instance=sqliteModel::DropViewStatement_strategy)
def test_sqlitemodel::dropviewstatement_ifExists_type(instance):
    assert isinstance(instance.ifExists, bool)


@given(instance=sqliteModel::DropViewStatement_strategy)
def test_sqlitemodel::dropviewstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::createtriggerstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::CreateTriggerStatement)

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_forEachRow_type(instance):
    assert isinstance(instance.forEachRow, str)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_forEachRow_setter(instance):
    original = instance.forEachRow
    instance.forEachRow = original
    assert instance.forEachRow == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_eventType_type(instance):
    assert isinstance(instance.eventType, str)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_temporary_type(instance):
    assert isinstance(instance.temporary, bool)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_when_type(instance):
    assert isinstance(instance.when, str)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_when_setter(instance):
    original = instance.when
    instance.when = original
    assert instance.when == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_updateColumnNames_type(instance):
    assert isinstance(instance.updateColumnNames, str)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_updateColumnNames_setter(instance):
    original = instance.updateColumnNames
    instance.updateColumnNames = original
    assert instance.updateColumnNames == original

@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::CreateTriggerStatement_strategy)
def test_sqlitemodel::createtriggerstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::TableDefinition_strategy)
@settings(max_examples=50)
def test_sqlitemodel::tabledefinition_instantiation(instance):
    assert isinstance(instance, sqliteModel::TableDefinition)

@given(instance=sqliteModel::TableDefinition_strategy)
def test_sqlitemodel::tabledefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::TableDefinition_strategy)
def test_sqlitemodel::tabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::LiteralValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel::literalvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel::LiteralValue)

@given(instance=SingleSource_strategy)
@settings(max_examples=50)
def test_singlesource_instantiation(instance):
    assert isinstance(instance, SingleSource)

@given(instance=sqliteModel::SingleSourceJoin_strategy)
@settings(max_examples=50)
def test_sqlitemodel::singlesourcejoin_instantiation(instance):
    assert isinstance(instance, sqliteModel::SingleSourceJoin)

@given(instance=sqliteModel::SelectSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectsource_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectSource)

@given(instance=sqliteModel::SelectSource_strategy)
def test_sqlitemodel::selectsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::SelectSource_strategy)
def test_sqlitemodel::selectsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::JoinStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::joinstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::JoinStatement)

@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_cross_type(instance):
    assert isinstance(instance.cross, bool)


@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_cross_setter(instance):
    original = instance.cross
    instance.cross = original
    assert instance.cross == original

@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_outer_type(instance):
    assert isinstance(instance.outer, bool)


@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_outer_setter(instance):
    original = instance.outer
    instance.outer = original
    assert instance.outer == original

@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_left_type(instance):
    assert isinstance(instance.left, bool)


@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_natural_type(instance):
    assert isinstance(instance.natural, bool)


@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_natural_setter(instance):
    original = instance.natural
    instance.natural = original
    assert instance.natural == original

@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_inner_type(instance):
    assert isinstance(instance.inner, bool)


@given(instance=sqliteModel::JoinStatement_strategy)
def test_sqlitemodel::joinstatement_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=sqliteModel::DropTableStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::droptablestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DropTableStatement)

@given(instance=sqliteModel::DropTableStatement_strategy)
def test_sqlitemodel::droptablestatement_ifExists_type(instance):
    assert isinstance(instance.ifExists, bool)


@given(instance=sqliteModel::DropTableStatement_strategy)
def test_sqlitemodel::droptablestatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel::AlterTableAddColumnStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::altertableaddcolumnstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::AlterTableAddColumnStatement)

@given(instance=sqliteModel::DMLStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel::dmlstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel::DMLStatement)

@given(instance=sqliteModel::GroupByExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel::groupbyexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel::GroupByExpressions)

@given(instance=sqliteModel::WhereExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel::whereexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel::WhereExpressions)

@given(instance=sqliteModel::ColumnSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel::columnsource_instantiation(instance):
    assert isinstance(instance, sqliteModel::ColumnSource)

@given(instance=sqliteModel::ColumnSource_strategy)
def test_sqlitemodel::columnsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqliteModel::ColumnSource_strategy)
def test_sqlitemodel::columnsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel::SelectList_strategy)
@settings(max_examples=50)
def test_sqlitemodel::selectlist_instantiation(instance):
    assert isinstance(instance, sqliteModel::SelectList)

@given(instance=sqliteModel::OrderingTerm_strategy)
@settings(max_examples=50)
def test_sqlitemodel::orderingterm_instantiation(instance):
    assert isinstance(instance, sqliteModel::OrderingTerm)

@given(instance=sqliteModel::OrderingTerm_strategy)
def test_sqlitemodel::orderingterm_asc_type(instance):
    assert isinstance(instance.asc, bool)


@given(instance=sqliteModel::OrderingTerm_strategy)
def test_sqlitemodel::orderingterm_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original

@given(instance=sqliteModel::OrderingTerm_strategy)
def test_sqlitemodel::orderingterm_desc_type(instance):
    assert isinstance(instance.desc, bool)


@given(instance=sqliteModel::OrderingTerm_strategy)
def test_sqlitemodel::orderingterm_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel::OrderingTermList_strategy)
@settings(max_examples=50)
def test_sqlitemodel::orderingtermlist_instantiation(instance):
    assert isinstance(instance, sqliteModel::OrderingTermList)
