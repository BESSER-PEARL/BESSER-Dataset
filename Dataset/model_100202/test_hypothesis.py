import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DefaultValue,
    sqliteModel_LiteralDefaultValue,
    sqliteModel_ExpressionDefaultValue,
    ColumnConstraint,
    sqliteModel_UniqueConstraint,
    sqliteModel_DefaultConstraint,
    sqliteModel_PrimaryKeyColumnConstraint,
    sqliteModel_NotNullConstraint,
    TableDefinition,
    sqliteModel_AlterTableRenameStatement,
    sqliteModel_CreateTableStatement,
    ColumnSource,
    sqliteModel_ResultColumn,
    SelectSource,
    sqliteModel_SingleSourceSelectStatement,
    sqliteModel_SingleSourceTable,
    LiteralValue,
    sqliteModel_NumericLiteral,
    sqliteModel_CurrentTimeStampLiteral,
    sqliteModel_CurrentDateLiteral,
    sqliteModel_StringLiteral,
    sqliteModel_NullLiteral,
    sqliteModel_CurrentTimeLiteral,
    SelectCoreExpression,
    sqliteModel_SelectCore,
    sqliteModel_SelectExpression,
    ContentUriSegment,
    sqliteModel_ContentUriParamSegment,
    Expression,
    sqliteModel_ColumnSourceRef,
    sqliteModel_NewColumn,
    sqliteModel_ExprOr,
    sqliteModel_NullCheckExpression,
    sqliteModel_CastExpression,
    sqliteModel_IsNull,
    sqliteModel_ExprRelate,
    sqliteModel_ExprEqual,
    sqliteModel_ExprAnd,
    sqliteModel_ExprBit,
    sqliteModel_ExprConcat,
    sqliteModel_ExprMult,
    sqliteModel_OldColumn,
    sqliteModel_CaseExpression,
    sqliteModel_FunctionArgument,
    sqliteModel_Literal,
    sqliteModel_ExprAdd,
    sqliteModel_NestedExpression,
    sqliteModel_SelectStatementExpression,
    sqliteModel_NotNull,
    ConfigurationStatement,
    sqliteModel_Function,
    sqliteModel_ActionStatement,
    sqliteModel_UpdateColumnExpression,
    sqliteModel_DefaultValue,
    sqliteModel_ColumnDef,
    sqliteModel_ConflictClause,
    TableConstraint,
    sqliteModel_CheckTableConstraint,
    sqliteModel_UniqueTableConstraint,
    sqliteModel_TableConstraint,
    sqliteModel_ColumnConstraint,
    sqliteModel_IndexedColumn,
    sqliteModel_PrimaryConstraint,
    sqliteModel_CreateViewStatement,
    sqliteModel_DMLStatement,
    sqliteModel_LiteralValue,
    DDLStatement,
    sqliteModel_AlterTableAddColumnStatement,
    sqliteModel_DropViewStatement,
    sqliteModel_CreateTriggerStatement,
    sqliteModel_DropTableStatement,
    sqliteModel_DropIndexStatement,
    sqliteModel_CreateIndexStatement,
    sqliteModel_DropTriggerStatement,
    sqliteModel_TableDefinition,
    SingleSource,
    sqliteModel_SingleSourceJoin,
    sqliteModel_SelectSource,
    sqliteModel_JoinStatement,
    sqliteModel_SingleSource,
    sqliteModel_JoinSource,
    sqliteModel_HavingExpressions,
    sqliteModel_GroupByExpressions,
    sqliteModel_WhereExpressions,
    sqliteModel_ColumnSource,
    sqliteModel_SelectList,
    sqliteModel_OrderingTerm,
    sqliteModel_OrderingTermList,
    sqliteModel_SelectCoreExpression,
    DMLStatement,
    sqliteModel_InsertStatement,
    sqliteModel_UpdateStatement,
    sqliteModel_DeleteStatement,
    sqliteModel_SelectStatement,
    sqliteModel_Case,
    sqliteModel_Expression,
    sqliteModel_ContentUriSegment,
    sqliteModel_ContentUri,
    sqliteModel_FunctionArg,
    sqliteModel_DDLStatement,
    sqliteModel_ConfigurationStatement,
    sqliteModel_MigrationBlock,
    sqliteModel_InitBlock,
    sqliteModel_ConfigBlock,
    sqliteModel_DatabaseBlock,
    sqliteModel_Model,
    ColumnType,
    SqliteDataType,
    ConflictResolution,
    CompoundOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_literaldefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_LiteralDefaultValue)


def test_sqlitemodel_literaldefaultvalue_constructor_exists():
    assert callable(sqliteModel_LiteralDefaultValue.__init__)


def test_sqlitemodel_literaldefaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel_LiteralDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_expressiondefaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExpressionDefaultValue)


def test_sqlitemodel_expressiondefaultvalue_constructor_exists():
    assert callable(sqliteModel_ExpressionDefaultValue.__init__)


def test_sqlitemodel_expressiondefaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel_ExpressionDefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(ColumnConstraint)


def test_columnconstraint_constructor_exists():
    assert callable(ColumnConstraint.__init__)


def test_columnconstraint_constructor_args():
    sig = inspect.signature(ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_uniqueconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_UniqueConstraint)


def test_sqlitemodel_uniqueconstraint_constructor_exists():
    assert callable(sqliteModel_UniqueConstraint.__init__)


def test_sqlitemodel_uniqueconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_UniqueConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_defaultconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DefaultConstraint)


def test_sqlitemodel_defaultconstraint_constructor_exists():
    assert callable(sqliteModel_DefaultConstraint.__init__)


def test_sqlitemodel_defaultconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_DefaultConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_primarykeycolumnconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_PrimaryKeyColumnConstraint)


def test_sqlitemodel_primarykeycolumnconstraint_constructor_exists():
    assert callable(sqliteModel_PrimaryKeyColumnConstraint.__init__)


def test_sqlitemodel_primarykeycolumnconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_PrimaryKeyColumnConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "autoincrement" in params, "Missing parameter 'autoincrement'"
    assert "asc" in params, "Missing parameter 'asc'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_sqlitemodel_primarykeycolumnconstraint_has_autoincrement():
    assert hasattr(sqliteModel_PrimaryKeyColumnConstraint, "autoincrement")
    descriptor = None
    for klass in sqliteModel_PrimaryKeyColumnConstraint.__mro__:
        if "autoincrement" in klass.__dict__:
            descriptor = klass.__dict__["autoincrement"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_primarykeycolumnconstraint_has_asc():
    assert hasattr(sqliteModel_PrimaryKeyColumnConstraint, "asc")
    descriptor = None
    for klass in sqliteModel_PrimaryKeyColumnConstraint.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_primarykeycolumnconstraint_has_desc():
    assert hasattr(sqliteModel_PrimaryKeyColumnConstraint, "desc")
    descriptor = None
    for klass in sqliteModel_PrimaryKeyColumnConstraint.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_notnullconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NotNullConstraint)


def test_sqlitemodel_notnullconstraint_constructor_exists():
    assert callable(sqliteModel_NotNullConstraint.__init__)


def test_sqlitemodel_notnullconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_NotNullConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(TableDefinition)


def test_tabledefinition_constructor_exists():
    assert callable(TableDefinition.__init__)


def test_tabledefinition_constructor_args():
    sig = inspect.signature(TableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_altertablerenamestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_AlterTableRenameStatement)


def test_sqlitemodel_altertablerenamestatement_constructor_exists():
    assert callable(sqliteModel_AlterTableRenameStatement.__init__)


def test_sqlitemodel_altertablerenamestatement_constructor_args():
    sig = inspect.signature(sqliteModel_AlterTableRenameStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_createtablestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CreateTableStatement)


def test_sqlitemodel_createtablestatement_constructor_exists():
    assert callable(sqliteModel_CreateTableStatement.__init__)


def test_sqlitemodel_createtablestatement_constructor_args():
    sig = inspect.signature(sqliteModel_CreateTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "temporary" in params, "Missing parameter 'temporary'"

def test_sqlitemodel_createtablestatement_has_temporary():
    assert hasattr(sqliteModel_CreateTableStatement, "temporary")
    descriptor = None
    for klass in sqliteModel_CreateTableStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)



def test_columnsource_is_not_abstract():
    assert not inspect.isabstract(ColumnSource)


def test_columnsource_constructor_exists():
    assert callable(ColumnSource.__init__)


def test_columnsource_constructor_args():
    sig = inspect.signature(ColumnSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_resultcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ResultColumn)


def test_sqlitemodel_resultcolumn_constructor_exists():
    assert callable(sqliteModel_ResultColumn.__init__)


def test_sqlitemodel_resultcolumn_constructor_args():
    sig = inspect.signature(sqliteModel_ResultColumn.__init__)
    params = list(sig.parameters.keys())



def test_selectsource_is_not_abstract():
    assert not inspect.isabstract(SelectSource)


def test_selectsource_constructor_exists():
    assert callable(SelectSource.__init__)


def test_selectsource_constructor_args():
    sig = inspect.signature(SelectSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_singlesourceselectstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SingleSourceSelectStatement)


def test_sqlitemodel_singlesourceselectstatement_constructor_exists():
    assert callable(sqliteModel_SingleSourceSelectStatement.__init__)


def test_sqlitemodel_singlesourceselectstatement_constructor_args():
    sig = inspect.signature(sqliteModel_SingleSourceSelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_singlesourcetable_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SingleSourceTable)


def test_sqlitemodel_singlesourcetable_constructor_exists():
    assert callable(sqliteModel_SingleSourceTable.__init__)


def test_sqlitemodel_singlesourcetable_constructor_args():
    sig = inspect.signature(sqliteModel_SingleSourceTable.__init__)
    params = list(sig.parameters.keys())



def test_literalvalue_is_not_abstract():
    assert not inspect.isabstract(LiteralValue)


def test_literalvalue_constructor_exists():
    assert callable(LiteralValue.__init__)


def test_literalvalue_constructor_args():
    sig = inspect.signature(LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_numericliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NumericLiteral)


def test_sqlitemodel_numericliteral_constructor_exists():
    assert callable(sqliteModel_NumericLiteral.__init__)


def test_sqlitemodel_numericliteral_constructor_args():
    sig = inspect.signature(sqliteModel_NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_sqlitemodel_numericliteral_has_number():
    assert hasattr(sqliteModel_NumericLiteral, "number")
    descriptor = None
    for klass in sqliteModel_NumericLiteral.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_currenttimestampliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CurrentTimeStampLiteral)


def test_sqlitemodel_currenttimestampliteral_constructor_exists():
    assert callable(sqliteModel_CurrentTimeStampLiteral.__init__)


def test_sqlitemodel_currenttimestampliteral_constructor_args():
    sig = inspect.signature(sqliteModel_CurrentTimeStampLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel_currenttimestampliteral_has_literal():
    assert hasattr(sqliteModel_CurrentTimeStampLiteral, "literal")
    descriptor = None
    for klass in sqliteModel_CurrentTimeStampLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_currentdateliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CurrentDateLiteral)


def test_sqlitemodel_currentdateliteral_constructor_exists():
    assert callable(sqliteModel_CurrentDateLiteral.__init__)


def test_sqlitemodel_currentdateliteral_constructor_args():
    sig = inspect.signature(sqliteModel_CurrentDateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel_currentdateliteral_has_literal():
    assert hasattr(sqliteModel_CurrentDateLiteral, "literal")
    descriptor = None
    for klass in sqliteModel_CurrentDateLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_stringliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_StringLiteral)


def test_sqlitemodel_stringliteral_constructor_exists():
    assert callable(sqliteModel_StringLiteral.__init__)


def test_sqlitemodel_stringliteral_constructor_args():
    sig = inspect.signature(sqliteModel_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel_stringliteral_has_literal():
    assert hasattr(sqliteModel_StringLiteral, "literal")
    descriptor = None
    for klass in sqliteModel_StringLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_nullliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NullLiteral)


def test_sqlitemodel_nullliteral_constructor_exists():
    assert callable(sqliteModel_NullLiteral.__init__)


def test_sqlitemodel_nullliteral_constructor_args():
    sig = inspect.signature(sqliteModel_NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel_nullliteral_has_literal():
    assert hasattr(sqliteModel_NullLiteral, "literal")
    descriptor = None
    for klass in sqliteModel_NullLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_currenttimeliteral_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CurrentTimeLiteral)


def test_sqlitemodel_currenttimeliteral_constructor_exists():
    assert callable(sqliteModel_CurrentTimeLiteral.__init__)


def test_sqlitemodel_currenttimeliteral_constructor_args():
    sig = inspect.signature(sqliteModel_CurrentTimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_sqlitemodel_currenttimeliteral_has_literal():
    assert hasattr(sqliteModel_CurrentTimeLiteral, "literal")
    descriptor = None
    for klass in sqliteModel_CurrentTimeLiteral.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_selectcoreexpression_is_not_abstract():
    assert not inspect.isabstract(SelectCoreExpression)


def test_selectcoreexpression_constructor_exists():
    assert callable(SelectCoreExpression.__init__)


def test_selectcoreexpression_constructor_args():
    sig = inspect.signature(SelectCoreExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_selectcore_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectCore)


def test_sqlitemodel_selectcore_constructor_exists():
    assert callable(sqliteModel_SelectCore.__init__)


def test_sqlitemodel_selectcore_constructor_args():
    sig = inspect.signature(sqliteModel_SelectCore.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_selectcore_has_op():
    assert hasattr(sqliteModel_SelectCore, "op")
    descriptor = None
    for klass in sqliteModel_SelectCore.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_selectexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectExpression)


def test_sqlitemodel_selectexpression_constructor_exists():
    assert callable(sqliteModel_SelectExpression.__init__)


def test_sqlitemodel_selectexpression_constructor_args():
    sig = inspect.signature(sqliteModel_SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"
    assert "allColumns" in params, "Missing parameter 'allColumns'"
    assert "distinct" in params, "Missing parameter 'distinct'"

def test_sqlitemodel_selectexpression_has_all():
    assert hasattr(sqliteModel_SelectExpression, "all")
    descriptor = None
    for klass in sqliteModel_SelectExpression.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_selectexpression_has_allColumns():
    assert hasattr(sqliteModel_SelectExpression, "allColumns")
    descriptor = None
    for klass in sqliteModel_SelectExpression.__mro__:
        if "allColumns" in klass.__dict__:
            descriptor = klass.__dict__["allColumns"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_selectexpression_has_distinct():
    assert hasattr(sqliteModel_SelectExpression, "distinct")
    descriptor = None
    for klass in sqliteModel_SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)



def test_contenturisegment_is_not_abstract():
    assert not inspect.isabstract(ContentUriSegment)


def test_contenturisegment_constructor_exists():
    assert callable(ContentUriSegment.__init__)


def test_contenturisegment_constructor_args():
    sig = inspect.signature(ContentUriSegment.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_contenturiparamsegment_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ContentUriParamSegment)


def test_sqlitemodel_contenturiparamsegment_constructor_exists():
    assert callable(sqliteModel_ContentUriParamSegment.__init__)


def test_sqlitemodel_contenturiparamsegment_constructor_args():
    sig = inspect.signature(sqliteModel_ContentUriParamSegment.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "text" in params, "Missing parameter 'text'"

def test_sqlitemodel_contenturiparamsegment_has_num():
    assert hasattr(sqliteModel_ContentUriParamSegment, "num")
    descriptor = None
    for klass in sqliteModel_ContentUriParamSegment.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_contenturiparamsegment_has_text():
    assert hasattr(sqliteModel_ContentUriParamSegment, "text")
    descriptor = None
    for klass in sqliteModel_ContentUriParamSegment.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_columnsourceref_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ColumnSourceRef)


def test_sqlitemodel_columnsourceref_constructor_exists():
    assert callable(sqliteModel_ColumnSourceRef.__init__)


def test_sqlitemodel_columnsourceref_constructor_args():
    sig = inspect.signature(sqliteModel_ColumnSourceRef.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_sqlitemodel_columnsourceref_has_all():
    assert hasattr(sqliteModel_ColumnSourceRef, "all")
    descriptor = None
    for klass in sqliteModel_ColumnSourceRef.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_newcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NewColumn)


def test_sqlitemodel_newcolumn_constructor_exists():
    assert callable(sqliteModel_NewColumn.__init__)


def test_sqlitemodel_newcolumn_constructor_args():
    sig = inspect.signature(sqliteModel_NewColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_expror_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprOr)


def test_sqlitemodel_expror_constructor_exists():
    assert callable(sqliteModel_ExprOr.__init__)


def test_sqlitemodel_expror_constructor_args():
    sig = inspect.signature(sqliteModel_ExprOr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_expror_has_op():
    assert hasattr(sqliteModel_ExprOr, "op")
    descriptor = None
    for klass in sqliteModel_ExprOr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_nullcheckexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NullCheckExpression)


def test_sqlitemodel_nullcheckexpression_constructor_exists():
    assert callable(sqliteModel_NullCheckExpression.__init__)


def test_sqlitemodel_nullcheckexpression_constructor_args():
    sig = inspect.signature(sqliteModel_NullCheckExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_castexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CastExpression)


def test_sqlitemodel_castexpression_constructor_exists():
    assert callable(sqliteModel_CastExpression.__init__)


def test_sqlitemodel_castexpression_constructor_args():
    sig = inspect.signature(sqliteModel_CastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel_castexpression_has_type():
    assert hasattr(sqliteModel_CastExpression, "type")
    descriptor = None
    for klass in sqliteModel_CastExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_isnull_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_IsNull)


def test_sqlitemodel_isnull_constructor_exists():
    assert callable(sqliteModel_IsNull.__init__)


def test_sqlitemodel_isnull_constructor_args():
    sig = inspect.signature(sqliteModel_IsNull.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_exprrelate_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprRelate)


def test_sqlitemodel_exprrelate_constructor_exists():
    assert callable(sqliteModel_ExprRelate.__init__)


def test_sqlitemodel_exprrelate_constructor_args():
    sig = inspect.signature(sqliteModel_ExprRelate.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprrelate_has_op():
    assert hasattr(sqliteModel_ExprRelate, "op")
    descriptor = None
    for klass in sqliteModel_ExprRelate.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_exprequal_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprEqual)


def test_sqlitemodel_exprequal_constructor_exists():
    assert callable(sqliteModel_ExprEqual.__init__)


def test_sqlitemodel_exprequal_constructor_args():
    sig = inspect.signature(sqliteModel_ExprEqual.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprequal_has_op():
    assert hasattr(sqliteModel_ExprEqual, "op")
    descriptor = None
    for klass in sqliteModel_ExprEqual.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_exprand_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprAnd)


def test_sqlitemodel_exprand_constructor_exists():
    assert callable(sqliteModel_ExprAnd.__init__)


def test_sqlitemodel_exprand_constructor_args():
    sig = inspect.signature(sqliteModel_ExprAnd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprand_has_op():
    assert hasattr(sqliteModel_ExprAnd, "op")
    descriptor = None
    for klass in sqliteModel_ExprAnd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_exprbit_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprBit)


def test_sqlitemodel_exprbit_constructor_exists():
    assert callable(sqliteModel_ExprBit.__init__)


def test_sqlitemodel_exprbit_constructor_args():
    sig = inspect.signature(sqliteModel_ExprBit.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprbit_has_op():
    assert hasattr(sqliteModel_ExprBit, "op")
    descriptor = None
    for klass in sqliteModel_ExprBit.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_exprconcat_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprConcat)


def test_sqlitemodel_exprconcat_constructor_exists():
    assert callable(sqliteModel_ExprConcat.__init__)


def test_sqlitemodel_exprconcat_constructor_args():
    sig = inspect.signature(sqliteModel_ExprConcat.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprconcat_has_op():
    assert hasattr(sqliteModel_ExprConcat, "op")
    descriptor = None
    for klass in sqliteModel_ExprConcat.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_exprmult_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprMult)


def test_sqlitemodel_exprmult_constructor_exists():
    assert callable(sqliteModel_ExprMult.__init__)


def test_sqlitemodel_exprmult_constructor_args():
    sig = inspect.signature(sqliteModel_ExprMult.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_exprmult_has_op():
    assert hasattr(sqliteModel_ExprMult, "op")
    descriptor = None
    for klass in sqliteModel_ExprMult.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_oldcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_OldColumn)


def test_sqlitemodel_oldcolumn_constructor_exists():
    assert callable(sqliteModel_OldColumn.__init__)


def test_sqlitemodel_oldcolumn_constructor_args():
    sig = inspect.signature(sqliteModel_OldColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_caseexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CaseExpression)


def test_sqlitemodel_caseexpression_constructor_exists():
    assert callable(sqliteModel_CaseExpression.__init__)


def test_sqlitemodel_caseexpression_constructor_args():
    sig = inspect.signature(sqliteModel_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_functionargument_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_FunctionArgument)


def test_sqlitemodel_functionargument_constructor_exists():
    assert callable(sqliteModel_FunctionArgument.__init__)


def test_sqlitemodel_functionargument_constructor_args():
    sig = inspect.signature(sqliteModel_FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_literal_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_Literal)


def test_sqlitemodel_literal_constructor_exists():
    assert callable(sqliteModel_Literal.__init__)


def test_sqlitemodel_literal_constructor_args():
    sig = inspect.signature(sqliteModel_Literal.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_expradd_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ExprAdd)


def test_sqlitemodel_expradd_constructor_exists():
    assert callable(sqliteModel_ExprAdd.__init__)


def test_sqlitemodel_expradd_constructor_args():
    sig = inspect.signature(sqliteModel_ExprAdd.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sqlitemodel_expradd_has_op():
    assert hasattr(sqliteModel_ExprAdd, "op")
    descriptor = None
    for klass in sqliteModel_ExprAdd.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NestedExpression)


def test_sqlitemodel_nestedexpression_constructor_exists():
    assert callable(sqliteModel_NestedExpression.__init__)


def test_sqlitemodel_nestedexpression_constructor_args():
    sig = inspect.signature(sqliteModel_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_selectstatementexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectStatementExpression)


def test_sqlitemodel_selectstatementexpression_constructor_exists():
    assert callable(sqliteModel_SelectStatementExpression.__init__)


def test_sqlitemodel_selectstatementexpression_constructor_args():
    sig = inspect.signature(sqliteModel_SelectStatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "exists" in params, "Missing parameter 'exists'"

def test_sqlitemodel_selectstatementexpression_has_not_():
    assert hasattr(sqliteModel_SelectStatementExpression, "not_")
    descriptor = None
    for klass in sqliteModel_SelectStatementExpression.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_selectstatementexpression_has_exists():
    assert hasattr(sqliteModel_SelectStatementExpression, "exists")
    descriptor = None
    for klass in sqliteModel_SelectStatementExpression.__mro__:
        if "exists" in klass.__dict__:
            descriptor = klass.__dict__["exists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_notnull_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_NotNull)


def test_sqlitemodel_notnull_constructor_exists():
    assert callable(sqliteModel_NotNull.__init__)


def test_sqlitemodel_notnull_constructor_args():
    sig = inspect.signature(sqliteModel_NotNull.__init__)
    params = list(sig.parameters.keys())



def test_configurationstatement_is_not_abstract():
    assert not inspect.isabstract(ConfigurationStatement)


def test_configurationstatement_constructor_exists():
    assert callable(ConfigurationStatement.__init__)


def test_configurationstatement_constructor_args():
    sig = inspect.signature(ConfigurationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_function_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_Function)


def test_sqlitemodel_function_constructor_exists():
    assert callable(sqliteModel_Function.__init__)


def test_sqlitemodel_function_constructor_args():
    sig = inspect.signature(sqliteModel_Function.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_sqlitemodel_function_has_all():
    assert hasattr(sqliteModel_Function, "all")
    descriptor = None
    for klass in sqliteModel_Function.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_actionstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ActionStatement)


def test_sqlitemodel_actionstatement_constructor_exists():
    assert callable(sqliteModel_ActionStatement.__init__)


def test_sqlitemodel_actionstatement_constructor_args():
    sig = inspect.signature(sqliteModel_ActionStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_updatecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_UpdateColumnExpression)


def test_sqlitemodel_updatecolumnexpression_constructor_exists():
    assert callable(sqliteModel_UpdateColumnExpression.__init__)


def test_sqlitemodel_updatecolumnexpression_constructor_args():
    sig = inspect.signature(sqliteModel_UpdateColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DefaultValue)


def test_sqlitemodel_defaultvalue_constructor_exists():
    assert callable(sqliteModel_DefaultValue.__init__)


def test_sqlitemodel_defaultvalue_constructor_args():
    sig = inspect.signature(sqliteModel_DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_columndef_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ColumnDef)


def test_sqlitemodel_columndef_constructor_exists():
    assert callable(sqliteModel_ColumnDef.__init__)


def test_sqlitemodel_columndef_constructor_args():
    sig = inspect.signature(sqliteModel_ColumnDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel_columndef_has_type():
    assert hasattr(sqliteModel_ColumnDef, "type")
    descriptor = None
    for klass in sqliteModel_ColumnDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_conflictclause_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ConflictClause)


def test_sqlitemodel_conflictclause_constructor_exists():
    assert callable(sqliteModel_ConflictClause.__init__)


def test_sqlitemodel_conflictclause_constructor_args():
    sig = inspect.signature(sqliteModel_ConflictClause.__init__)
    params = list(sig.parameters.keys())
    assert "resolution" in params, "Missing parameter 'resolution'"

def test_sqlitemodel_conflictclause_has_resolution():
    assert hasattr(sqliteModel_ConflictClause, "resolution")
    descriptor = None
    for klass in sqliteModel_ConflictClause.__mro__:
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



def test_sqlitemodel_checktableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CheckTableConstraint)


def test_sqlitemodel_checktableconstraint_constructor_exists():
    assert callable(sqliteModel_CheckTableConstraint.__init__)


def test_sqlitemodel_checktableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_CheckTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_uniquetableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_UniqueTableConstraint)


def test_sqlitemodel_uniquetableconstraint_constructor_exists():
    assert callable(sqliteModel_UniqueTableConstraint.__init__)


def test_sqlitemodel_uniquetableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_UniqueTableConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_tableconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_TableConstraint)


def test_sqlitemodel_tableconstraint_constructor_exists():
    assert callable(sqliteModel_TableConstraint.__init__)


def test_sqlitemodel_tableconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_TableConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_tableconstraint_has_name():
    assert hasattr(sqliteModel_TableConstraint, "name")
    descriptor = None
    for klass in sqliteModel_TableConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_columnconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ColumnConstraint)


def test_sqlitemodel_columnconstraint_constructor_exists():
    assert callable(sqliteModel_ColumnConstraint.__init__)


def test_sqlitemodel_columnconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_ColumnConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_indexedcolumn_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_IndexedColumn)


def test_sqlitemodel_indexedcolumn_constructor_exists():
    assert callable(sqliteModel_IndexedColumn.__init__)


def test_sqlitemodel_indexedcolumn_constructor_args():
    sig = inspect.signature(sqliteModel_IndexedColumn.__init__)
    params = list(sig.parameters.keys())
    assert "asc" in params, "Missing parameter 'asc'"
    assert "collationName" in params, "Missing parameter 'collationName'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_sqlitemodel_indexedcolumn_has_asc():
    assert hasattr(sqliteModel_IndexedColumn, "asc")
    descriptor = None
    for klass in sqliteModel_IndexedColumn.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_indexedcolumn_has_collationName():
    assert hasattr(sqliteModel_IndexedColumn, "collationName")
    descriptor = None
    for klass in sqliteModel_IndexedColumn.__mro__:
        if "collationName" in klass.__dict__:
            descriptor = klass.__dict__["collationName"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_indexedcolumn_has_desc():
    assert hasattr(sqliteModel_IndexedColumn, "desc")
    descriptor = None
    for klass in sqliteModel_IndexedColumn.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_primaryconstraint_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_PrimaryConstraint)


def test_sqlitemodel_primaryconstraint_constructor_exists():
    assert callable(sqliteModel_PrimaryConstraint.__init__)


def test_sqlitemodel_primaryconstraint_constructor_args():
    sig = inspect.signature(sqliteModel_PrimaryConstraint.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_createviewstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CreateViewStatement)


def test_sqlitemodel_createviewstatement_constructor_exists():
    assert callable(sqliteModel_CreateViewStatement.__init__)


def test_sqlitemodel_createviewstatement_constructor_args():
    sig = inspect.signature(sqliteModel_CreateViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "temporary" in params, "Missing parameter 'temporary'"

def test_sqlitemodel_createviewstatement_has_temporary():
    assert hasattr(sqliteModel_CreateViewStatement, "temporary")
    descriptor = None
    for klass in sqliteModel_CreateViewStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_dmlstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DMLStatement)


def test_sqlitemodel_dmlstatement_constructor_exists():
    assert callable(sqliteModel_DMLStatement.__init__)


def test_sqlitemodel_dmlstatement_constructor_args():
    sig = inspect.signature(sqliteModel_DMLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_literalvalue_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_LiteralValue)


def test_sqlitemodel_literalvalue_constructor_exists():
    assert callable(sqliteModel_LiteralValue.__init__)


def test_sqlitemodel_literalvalue_constructor_args():
    sig = inspect.signature(sqliteModel_LiteralValue.__init__)
    params = list(sig.parameters.keys())



def test_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(DDLStatement)


def test_ddlstatement_constructor_exists():
    assert callable(DDLStatement.__init__)


def test_ddlstatement_constructor_args():
    sig = inspect.signature(DDLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_altertableaddcolumnstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_AlterTableAddColumnStatement)


def test_sqlitemodel_altertableaddcolumnstatement_constructor_exists():
    assert callable(sqliteModel_AlterTableAddColumnStatement.__init__)


def test_sqlitemodel_altertableaddcolumnstatement_constructor_args():
    sig = inspect.signature(sqliteModel_AlterTableAddColumnStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_dropviewstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DropViewStatement)


def test_sqlitemodel_dropviewstatement_constructor_exists():
    assert callable(sqliteModel_DropViewStatement.__init__)


def test_sqlitemodel_dropviewstatement_constructor_args():
    sig = inspect.signature(sqliteModel_DropViewStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel_dropviewstatement_has_ifExists():
    assert hasattr(sqliteModel_DropViewStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel_DropViewStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_createtriggerstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CreateTriggerStatement)


def test_sqlitemodel_createtriggerstatement_constructor_exists():
    assert callable(sqliteModel_CreateTriggerStatement.__init__)


def test_sqlitemodel_createtriggerstatement_constructor_args():
    sig = inspect.signature(sqliteModel_CreateTriggerStatement.__init__)
    params = list(sig.parameters.keys())
    assert "when" in params, "Missing parameter 'when'"
    assert "eventType" in params, "Missing parameter 'eventType'"
    assert "forEachRow" in params, "Missing parameter 'forEachRow'"
    assert "name" in params, "Missing parameter 'name'"
    assert "temporary" in params, "Missing parameter 'temporary'"
    assert "updateColumnNames" in params, "Missing parameter 'updateColumnNames'"

def test_sqlitemodel_createtriggerstatement_has_when():
    assert hasattr(sqliteModel_CreateTriggerStatement, "when")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "when" in klass.__dict__:
            descriptor = klass.__dict__["when"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createtriggerstatement_has_eventType():
    assert hasattr(sqliteModel_CreateTriggerStatement, "eventType")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "eventType" in klass.__dict__:
            descriptor = klass.__dict__["eventType"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createtriggerstatement_has_forEachRow():
    assert hasattr(sqliteModel_CreateTriggerStatement, "forEachRow")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "forEachRow" in klass.__dict__:
            descriptor = klass.__dict__["forEachRow"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createtriggerstatement_has_name():
    assert hasattr(sqliteModel_CreateTriggerStatement, "name")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createtriggerstatement_has_temporary():
    assert hasattr(sqliteModel_CreateTriggerStatement, "temporary")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "temporary" in klass.__dict__:
            descriptor = klass.__dict__["temporary"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createtriggerstatement_has_updateColumnNames():
    assert hasattr(sqliteModel_CreateTriggerStatement, "updateColumnNames")
    descriptor = None
    for klass in sqliteModel_CreateTriggerStatement.__mro__:
        if "updateColumnNames" in klass.__dict__:
            descriptor = klass.__dict__["updateColumnNames"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_droptablestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DropTableStatement)


def test_sqlitemodel_droptablestatement_constructor_exists():
    assert callable(sqliteModel_DropTableStatement.__init__)


def test_sqlitemodel_droptablestatement_constructor_args():
    sig = inspect.signature(sqliteModel_DropTableStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel_droptablestatement_has_ifExists():
    assert hasattr(sqliteModel_DropTableStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel_DropTableStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_dropindexstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DropIndexStatement)


def test_sqlitemodel_dropindexstatement_constructor_exists():
    assert callable(sqliteModel_DropIndexStatement.__init__)


def test_sqlitemodel_dropindexstatement_constructor_args():
    sig = inspect.signature(sqliteModel_DropIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel_dropindexstatement_has_ifExists():
    assert hasattr(sqliteModel_DropIndexStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel_DropIndexStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_createindexstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_CreateIndexStatement)


def test_sqlitemodel_createindexstatement_constructor_exists():
    assert callable(sqliteModel_CreateIndexStatement.__init__)


def test_sqlitemodel_createindexstatement_constructor_args():
    sig = inspect.signature(sqliteModel_CreateIndexStatement.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_createindexstatement_has_unique():
    assert hasattr(sqliteModel_CreateIndexStatement, "unique")
    descriptor = None
    for klass in sqliteModel_CreateIndexStatement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_createindexstatement_has_name():
    assert hasattr(sqliteModel_CreateIndexStatement, "name")
    descriptor = None
    for klass in sqliteModel_CreateIndexStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_droptriggerstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DropTriggerStatement)


def test_sqlitemodel_droptriggerstatement_constructor_exists():
    assert callable(sqliteModel_DropTriggerStatement.__init__)


def test_sqlitemodel_droptriggerstatement_constructor_args():
    sig = inspect.signature(sqliteModel_DropTriggerStatement.__init__)
    params = list(sig.parameters.keys())
    assert "ifExists" in params, "Missing parameter 'ifExists'"

def test_sqlitemodel_droptriggerstatement_has_ifExists():
    assert hasattr(sqliteModel_DropTriggerStatement, "ifExists")
    descriptor = None
    for klass in sqliteModel_DropTriggerStatement.__mro__:
        if "ifExists" in klass.__dict__:
            descriptor = klass.__dict__["ifExists"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_tabledefinition_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_TableDefinition)


def test_sqlitemodel_tabledefinition_constructor_exists():
    assert callable(sqliteModel_TableDefinition.__init__)


def test_sqlitemodel_tabledefinition_constructor_args():
    sig = inspect.signature(sqliteModel_TableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_tabledefinition_has_name():
    assert hasattr(sqliteModel_TableDefinition, "name")
    descriptor = None
    for klass in sqliteModel_TableDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_singlesource_is_not_abstract():
    assert not inspect.isabstract(SingleSource)


def test_singlesource_constructor_exists():
    assert callable(SingleSource.__init__)


def test_singlesource_constructor_args():
    sig = inspect.signature(SingleSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_singlesourcejoin_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SingleSourceJoin)


def test_sqlitemodel_singlesourcejoin_constructor_exists():
    assert callable(sqliteModel_SingleSourceJoin.__init__)


def test_sqlitemodel_singlesourcejoin_constructor_args():
    sig = inspect.signature(sqliteModel_SingleSourceJoin.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_selectsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectSource)


def test_sqlitemodel_selectsource_constructor_exists():
    assert callable(sqliteModel_SelectSource.__init__)


def test_sqlitemodel_selectsource_constructor_args():
    sig = inspect.signature(sqliteModel_SelectSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_selectsource_has_name():
    assert hasattr(sqliteModel_SelectSource, "name")
    descriptor = None
    for klass in sqliteModel_SelectSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_joinstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_JoinStatement)


def test_sqlitemodel_joinstatement_constructor_exists():
    assert callable(sqliteModel_JoinStatement.__init__)


def test_sqlitemodel_joinstatement_constructor_args():
    sig = inspect.signature(sqliteModel_JoinStatement.__init__)
    params = list(sig.parameters.keys())
    assert "outer" in params, "Missing parameter 'outer'"
    assert "left" in params, "Missing parameter 'left'"
    assert "natural" in params, "Missing parameter 'natural'"
    assert "cross" in params, "Missing parameter 'cross'"
    assert "inner" in params, "Missing parameter 'inner'"

def test_sqlitemodel_joinstatement_has_outer():
    assert hasattr(sqliteModel_JoinStatement, "outer")
    descriptor = None
    for klass in sqliteModel_JoinStatement.__mro__:
        if "outer" in klass.__dict__:
            descriptor = klass.__dict__["outer"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_joinstatement_has_left():
    assert hasattr(sqliteModel_JoinStatement, "left")
    descriptor = None
    for klass in sqliteModel_JoinStatement.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_joinstatement_has_natural():
    assert hasattr(sqliteModel_JoinStatement, "natural")
    descriptor = None
    for klass in sqliteModel_JoinStatement.__mro__:
        if "natural" in klass.__dict__:
            descriptor = klass.__dict__["natural"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_joinstatement_has_cross():
    assert hasattr(sqliteModel_JoinStatement, "cross")
    descriptor = None
    for klass in sqliteModel_JoinStatement.__mro__:
        if "cross" in klass.__dict__:
            descriptor = klass.__dict__["cross"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_joinstatement_has_inner():
    assert hasattr(sqliteModel_JoinStatement, "inner")
    descriptor = None
    for klass in sqliteModel_JoinStatement.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_singlesource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SingleSource)


def test_sqlitemodel_singlesource_constructor_exists():
    assert callable(sqliteModel_SingleSource.__init__)


def test_sqlitemodel_singlesource_constructor_args():
    sig = inspect.signature(sqliteModel_SingleSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_joinsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_JoinSource)


def test_sqlitemodel_joinsource_constructor_exists():
    assert callable(sqliteModel_JoinSource.__init__)


def test_sqlitemodel_joinsource_constructor_args():
    sig = inspect.signature(sqliteModel_JoinSource.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_havingexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_HavingExpressions)


def test_sqlitemodel_havingexpressions_constructor_exists():
    assert callable(sqliteModel_HavingExpressions.__init__)


def test_sqlitemodel_havingexpressions_constructor_args():
    sig = inspect.signature(sqliteModel_HavingExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_groupbyexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_GroupByExpressions)


def test_sqlitemodel_groupbyexpressions_constructor_exists():
    assert callable(sqliteModel_GroupByExpressions.__init__)


def test_sqlitemodel_groupbyexpressions_constructor_args():
    sig = inspect.signature(sqliteModel_GroupByExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_whereexpressions_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_WhereExpressions)


def test_sqlitemodel_whereexpressions_constructor_exists():
    assert callable(sqliteModel_WhereExpressions.__init__)


def test_sqlitemodel_whereexpressions_constructor_args():
    sig = inspect.signature(sqliteModel_WhereExpressions.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_columnsource_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ColumnSource)


def test_sqlitemodel_columnsource_constructor_exists():
    assert callable(sqliteModel_ColumnSource.__init__)


def test_sqlitemodel_columnsource_constructor_args():
    sig = inspect.signature(sqliteModel_ColumnSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_columnsource_has_name():
    assert hasattr(sqliteModel_ColumnSource, "name")
    descriptor = None
    for klass in sqliteModel_ColumnSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_selectlist_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectList)


def test_sqlitemodel_selectlist_constructor_exists():
    assert callable(sqliteModel_SelectList.__init__)


def test_sqlitemodel_selectlist_constructor_args():
    sig = inspect.signature(sqliteModel_SelectList.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_orderingterm_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_OrderingTerm)


def test_sqlitemodel_orderingterm_constructor_exists():
    assert callable(sqliteModel_OrderingTerm.__init__)


def test_sqlitemodel_orderingterm_constructor_args():
    sig = inspect.signature(sqliteModel_OrderingTerm.__init__)
    params = list(sig.parameters.keys())
    assert "asc" in params, "Missing parameter 'asc'"
    assert "desc" in params, "Missing parameter 'desc'"

def test_sqlitemodel_orderingterm_has_asc():
    assert hasattr(sqliteModel_OrderingTerm, "asc")
    descriptor = None
    for klass in sqliteModel_OrderingTerm.__mro__:
        if "asc" in klass.__dict__:
            descriptor = klass.__dict__["asc"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_orderingterm_has_desc():
    assert hasattr(sqliteModel_OrderingTerm, "desc")
    descriptor = None
    for klass in sqliteModel_OrderingTerm.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_orderingtermlist_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_OrderingTermList)


def test_sqlitemodel_orderingtermlist_constructor_exists():
    assert callable(sqliteModel_OrderingTermList.__init__)


def test_sqlitemodel_orderingtermlist_constructor_args():
    sig = inspect.signature(sqliteModel_OrderingTermList.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_selectcoreexpression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectCoreExpression)


def test_sqlitemodel_selectcoreexpression_constructor_exists():
    assert callable(sqliteModel_SelectCoreExpression.__init__)


def test_sqlitemodel_selectcoreexpression_constructor_args():
    sig = inspect.signature(sqliteModel_SelectCoreExpression.__init__)
    params = list(sig.parameters.keys())



def test_dmlstatement_is_not_abstract():
    assert not inspect.isabstract(DMLStatement)


def test_dmlstatement_constructor_exists():
    assert callable(DMLStatement.__init__)


def test_dmlstatement_constructor_args():
    sig = inspect.signature(DMLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_insertstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_InsertStatement)


def test_sqlitemodel_insertstatement_constructor_exists():
    assert callable(sqliteModel_InsertStatement.__init__)


def test_sqlitemodel_insertstatement_constructor_args():
    sig = inspect.signature(sqliteModel_InsertStatement.__init__)
    params = list(sig.parameters.keys())
    assert "conflictResolution" in params, "Missing parameter 'conflictResolution'"

def test_sqlitemodel_insertstatement_has_conflictResolution():
    assert hasattr(sqliteModel_InsertStatement, "conflictResolution")
    descriptor = None
    for klass in sqliteModel_InsertStatement.__mro__:
        if "conflictResolution" in klass.__dict__:
            descriptor = klass.__dict__["conflictResolution"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_updatestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_UpdateStatement)


def test_sqlitemodel_updatestatement_constructor_exists():
    assert callable(sqliteModel_UpdateStatement.__init__)


def test_sqlitemodel_updatestatement_constructor_args():
    sig = inspect.signature(sqliteModel_UpdateStatement.__init__)
    params = list(sig.parameters.keys())
    assert "conflictResolution" in params, "Missing parameter 'conflictResolution'"

def test_sqlitemodel_updatestatement_has_conflictResolution():
    assert hasattr(sqliteModel_UpdateStatement, "conflictResolution")
    descriptor = None
    for klass in sqliteModel_UpdateStatement.__mro__:
        if "conflictResolution" in klass.__dict__:
            descriptor = klass.__dict__["conflictResolution"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_deletestatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DeleteStatement)


def test_sqlitemodel_deletestatement_constructor_exists():
    assert callable(sqliteModel_DeleteStatement.__init__)


def test_sqlitemodel_deletestatement_constructor_args():
    sig = inspect.signature(sqliteModel_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_selectstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_SelectStatement)


def test_sqlitemodel_selectstatement_constructor_exists():
    assert callable(sqliteModel_SelectStatement.__init__)


def test_sqlitemodel_selectstatement_constructor_args():
    sig = inspect.signature(sqliteModel_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_case_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_Case)


def test_sqlitemodel_case_constructor_exists():
    assert callable(sqliteModel_Case.__init__)


def test_sqlitemodel_case_constructor_args():
    sig = inspect.signature(sqliteModel_Case.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_expression_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_Expression)


def test_sqlitemodel_expression_constructor_exists():
    assert callable(sqliteModel_Expression.__init__)


def test_sqlitemodel_expression_constructor_args():
    sig = inspect.signature(sqliteModel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_contenturisegment_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ContentUriSegment)


def test_sqlitemodel_contenturisegment_constructor_exists():
    assert callable(sqliteModel_ContentUriSegment.__init__)


def test_sqlitemodel_contenturisegment_constructor_args():
    sig = inspect.signature(sqliteModel_ContentUriSegment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_contenturisegment_has_name():
    assert hasattr(sqliteModel_ContentUriSegment, "name")
    descriptor = None
    for klass in sqliteModel_ContentUriSegment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_contenturi_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ContentUri)


def test_sqlitemodel_contenturi_constructor_exists():
    assert callable(sqliteModel_ContentUri.__init__)


def test_sqlitemodel_contenturi_constructor_args():
    sig = inspect.signature(sqliteModel_ContentUri.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel_contenturi_has_type():
    assert hasattr(sqliteModel_ContentUri, "type")
    descriptor = None
    for klass in sqliteModel_ContentUri.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_functionarg_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_FunctionArg)


def test_sqlitemodel_functionarg_constructor_exists():
    assert callable(sqliteModel_FunctionArg.__init__)


def test_sqlitemodel_functionarg_constructor_args():
    sig = inspect.signature(sqliteModel_FunctionArg.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_sqlitemodel_functionarg_has_name():
    assert hasattr(sqliteModel_FunctionArg, "name")
    descriptor = None
    for klass in sqliteModel_FunctionArg.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqlitemodel_functionarg_has_type():
    assert hasattr(sqliteModel_FunctionArg, "type")
    descriptor = None
    for klass in sqliteModel_FunctionArg.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_ddlstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DDLStatement)


def test_sqlitemodel_ddlstatement_constructor_exists():
    assert callable(sqliteModel_DDLStatement.__init__)


def test_sqlitemodel_ddlstatement_constructor_args():
    sig = inspect.signature(sqliteModel_DDLStatement.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_configurationstatement_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ConfigurationStatement)


def test_sqlitemodel_configurationstatement_constructor_exists():
    assert callable(sqliteModel_ConfigurationStatement.__init__)


def test_sqlitemodel_configurationstatement_constructor_args():
    sig = inspect.signature(sqliteModel_ConfigurationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_configurationstatement_has_name():
    assert hasattr(sqliteModel_ConfigurationStatement, "name")
    descriptor = None
    for klass in sqliteModel_ConfigurationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_migrationblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_MigrationBlock)


def test_sqlitemodel_migrationblock_constructor_exists():
    assert callable(sqliteModel_MigrationBlock.__init__)


def test_sqlitemodel_migrationblock_constructor_args():
    sig = inspect.signature(sqliteModel_MigrationBlock.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_initblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_InitBlock)


def test_sqlitemodel_initblock_constructor_exists():
    assert callable(sqliteModel_InitBlock.__init__)


def test_sqlitemodel_initblock_constructor_args():
    sig = inspect.signature(sqliteModel_InitBlock.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_configblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_ConfigBlock)


def test_sqlitemodel_configblock_constructor_exists():
    assert callable(sqliteModel_ConfigBlock.__init__)


def test_sqlitemodel_configblock_constructor_args():
    sig = inspect.signature(sqliteModel_ConfigBlock.__init__)
    params = list(sig.parameters.keys())



def test_sqlitemodel_databaseblock_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_DatabaseBlock)


def test_sqlitemodel_databaseblock_constructor_exists():
    assert callable(sqliteModel_DatabaseBlock.__init__)


def test_sqlitemodel_databaseblock_constructor_args():
    sig = inspect.signature(sqliteModel_DatabaseBlock.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqlitemodel_databaseblock_has_name():
    assert hasattr(sqliteModel_DatabaseBlock, "name")
    descriptor = None
    for klass in sqliteModel_DatabaseBlock.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqlitemodel_model_is_not_abstract():
    assert not inspect.isabstract(sqliteModel_Model)


def test_sqlitemodel_model_constructor_exists():
    assert callable(sqliteModel_Model.__init__)


def test_sqlitemodel_model_constructor_args():
    sig = inspect.signature(sqliteModel_Model.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"

def test_sqlitemodel_model_has_packageName():
    assert hasattr(sqliteModel_Model, "packageName")
    descriptor = None
    for klass in sqliteModel_Model.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_columntype_exists():
    # Check that the Enumeration exists
    assert ColumnType is not None

def test_columntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColumnType]
    expected_literals = [
        "blob",
        "text",
        "real",
        "boolean",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColumnType"

def test_sqlitedatatype_exists():
    # Check that the Enumeration exists
    assert SqliteDataType is not None

def test_sqlitedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SqliteDataType]
    expected_literals = [
        "none",
        "blob",
        "real",
        "integer",
        "text",
        "numeric",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SqliteDataType"

def test_conflictresolution_exists():
    # Check that the Enumeration exists
    assert ConflictResolution is not None

def test_conflictresolution_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConflictResolution]
    expected_literals = [
        "abort",
        "rollback",
        "ignore",
        "replace",
        "fail",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConflictResolution"

def test_compoundoperator_exists():
    # Check that the Enumeration exists
    assert CompoundOperator is not None

def test_compoundoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompoundOperator]
    expected_literals = [
        "intersect",
        "except_",
        "unionall",
        "union",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompoundOperator"


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
DefaultValue_strategy = st.builds(
    DefaultValue,
)
sqliteModel_LiteralDefaultValue_strategy = st.builds(
    sqliteModel_LiteralDefaultValue,
)
sqliteModel_ExpressionDefaultValue_strategy = st.builds(
    sqliteModel_ExpressionDefaultValue,
)
ColumnConstraint_strategy = st.builds(
    ColumnConstraint,
)
sqliteModel_UniqueConstraint_strategy = st.builds(
    sqliteModel_UniqueConstraint,
)
sqliteModel_DefaultConstraint_strategy = st.builds(
    sqliteModel_DefaultConstraint,
)
sqliteModel_PrimaryKeyColumnConstraint_strategy = st.builds(
    sqliteModel_PrimaryKeyColumnConstraint,
    autoincrement=
        st.booleans(),
    asc=
        st.booleans(),
    desc=
        st.booleans()
)
sqliteModel_NotNullConstraint_strategy = st.builds(
    sqliteModel_NotNullConstraint,
)
TableDefinition_strategy = st.builds(
    TableDefinition,
)
sqliteModel_AlterTableRenameStatement_strategy = st.builds(
    sqliteModel_AlterTableRenameStatement,
)
sqliteModel_CreateTableStatement_strategy = st.builds(
    sqliteModel_CreateTableStatement,
    temporary=
        st.booleans()
)
ColumnSource_strategy = st.builds(
    ColumnSource,
)
sqliteModel_ResultColumn_strategy = st.builds(
    sqliteModel_ResultColumn,
)
SelectSource_strategy = st.builds(
    SelectSource,
)
sqliteModel_SingleSourceSelectStatement_strategy = st.builds(
    sqliteModel_SingleSourceSelectStatement,
)
sqliteModel_SingleSourceTable_strategy = st.builds(
    sqliteModel_SingleSourceTable,
)
LiteralValue_strategy = st.builds(
    LiteralValue,
)
sqliteModel_NumericLiteral_strategy = st.builds(
    sqliteModel_NumericLiteral,
    number=
        safe_text
)
sqliteModel_CurrentTimeStampLiteral_strategy = st.builds(
    sqliteModel_CurrentTimeStampLiteral,
    literal=
        safe_text
)
sqliteModel_CurrentDateLiteral_strategy = st.builds(
    sqliteModel_CurrentDateLiteral,
    literal=
        safe_text
)
sqliteModel_StringLiteral_strategy = st.builds(
    sqliteModel_StringLiteral,
    literal=
        safe_text
)
sqliteModel_NullLiteral_strategy = st.builds(
    sqliteModel_NullLiteral,
    literal=
        safe_text
)
sqliteModel_CurrentTimeLiteral_strategy = st.builds(
    sqliteModel_CurrentTimeLiteral,
    literal=
        safe_text
)
SelectCoreExpression_strategy = st.builds(
    SelectCoreExpression,
)
sqliteModel_SelectCore_strategy = st.builds(
    sqliteModel_SelectCore,
    op=
        safe_text
)
sqliteModel_SelectExpression_strategy = st.builds(
    sqliteModel_SelectExpression,
    all=
        st.booleans(),
    allColumns=
        st.booleans(),
    distinct=
        st.booleans()
)
ContentUriSegment_strategy = st.builds(
    ContentUriSegment,
)
sqliteModel_ContentUriParamSegment_strategy = st.builds(
    sqliteModel_ContentUriParamSegment,
    num=
        st.booleans(),
    text=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
sqliteModel_ColumnSourceRef_strategy = st.builds(
    sqliteModel_ColumnSourceRef,
    all=
        st.booleans()
)
sqliteModel_NewColumn_strategy = st.builds(
    sqliteModel_NewColumn,
)
sqliteModel_ExprOr_strategy = st.builds(
    sqliteModel_ExprOr,
    op=
        safe_text
)
sqliteModel_NullCheckExpression_strategy = st.builds(
    sqliteModel_NullCheckExpression,
)
sqliteModel_CastExpression_strategy = st.builds(
    sqliteModel_CastExpression,
    type=
        safe_text
)
sqliteModel_IsNull_strategy = st.builds(
    sqliteModel_IsNull,
)
sqliteModel_ExprRelate_strategy = st.builds(
    sqliteModel_ExprRelate,
    op=
        safe_text
)
sqliteModel_ExprEqual_strategy = st.builds(
    sqliteModel_ExprEqual,
    op=
        safe_text
)
sqliteModel_ExprAnd_strategy = st.builds(
    sqliteModel_ExprAnd,
    op=
        safe_text
)
sqliteModel_ExprBit_strategy = st.builds(
    sqliteModel_ExprBit,
    op=
        safe_text
)
sqliteModel_ExprConcat_strategy = st.builds(
    sqliteModel_ExprConcat,
    op=
        safe_text
)
sqliteModel_ExprMult_strategy = st.builds(
    sqliteModel_ExprMult,
    op=
        safe_text
)
sqliteModel_OldColumn_strategy = st.builds(
    sqliteModel_OldColumn,
)
sqliteModel_CaseExpression_strategy = st.builds(
    sqliteModel_CaseExpression,
)
sqliteModel_FunctionArgument_strategy = st.builds(
    sqliteModel_FunctionArgument,
)
sqliteModel_Literal_strategy = st.builds(
    sqliteModel_Literal,
)
sqliteModel_ExprAdd_strategy = st.builds(
    sqliteModel_ExprAdd,
    op=
        safe_text
)
sqliteModel_NestedExpression_strategy = st.builds(
    sqliteModel_NestedExpression,
)
sqliteModel_SelectStatementExpression_strategy = st.builds(
    sqliteModel_SelectStatementExpression,
    not_=
        st.booleans(),
    exists=
        st.booleans()
)
sqliteModel_NotNull_strategy = st.builds(
    sqliteModel_NotNull,
)
ConfigurationStatement_strategy = st.builds(
    ConfigurationStatement,
)
sqliteModel_Function_strategy = st.builds(
    sqliteModel_Function,
    all=
        st.booleans()
)
sqliteModel_ActionStatement_strategy = st.builds(
    sqliteModel_ActionStatement,
)
sqliteModel_UpdateColumnExpression_strategy = st.builds(
    sqliteModel_UpdateColumnExpression,
)
sqliteModel_DefaultValue_strategy = st.builds(
    sqliteModel_DefaultValue,
)
sqliteModel_ColumnDef_strategy = st.builds(
    sqliteModel_ColumnDef,
    type=
        safe_text
)
sqliteModel_ConflictClause_strategy = st.builds(
    sqliteModel_ConflictClause,
    resolution=
        safe_text
)
TableConstraint_strategy = st.builds(
    TableConstraint,
)
sqliteModel_CheckTableConstraint_strategy = st.builds(
    sqliteModel_CheckTableConstraint,
)
sqliteModel_UniqueTableConstraint_strategy = st.builds(
    sqliteModel_UniqueTableConstraint,
)
sqliteModel_TableConstraint_strategy = st.builds(
    sqliteModel_TableConstraint,
    name=
        safe_text
)
sqliteModel_ColumnConstraint_strategy = st.builds(
    sqliteModel_ColumnConstraint,
)
sqliteModel_IndexedColumn_strategy = st.builds(
    sqliteModel_IndexedColumn,
    asc=
        st.booleans(),
    collationName=
        safe_text,
    desc=
        st.booleans()
)
sqliteModel_PrimaryConstraint_strategy = st.builds(
    sqliteModel_PrimaryConstraint,
)
sqliteModel_CreateViewStatement_strategy = st.builds(
    sqliteModel_CreateViewStatement,
    temporary=
        st.booleans()
)
sqliteModel_DMLStatement_strategy = st.builds(
    sqliteModel_DMLStatement,
)
sqliteModel_LiteralValue_strategy = st.builds(
    sqliteModel_LiteralValue,
)
DDLStatement_strategy = st.builds(
    DDLStatement,
)
sqliteModel_AlterTableAddColumnStatement_strategy = st.builds(
    sqliteModel_AlterTableAddColumnStatement,
)
sqliteModel_DropViewStatement_strategy = st.builds(
    sqliteModel_DropViewStatement,
    ifExists=
        st.booleans()
)
sqliteModel_CreateTriggerStatement_strategy = st.builds(
    sqliteModel_CreateTriggerStatement,
    when=
        safe_text,
    eventType=
        safe_text,
    forEachRow=
        safe_text,
    name=
        safe_text,
    temporary=
        st.booleans(),
    updateColumnNames=
        safe_text
)
sqliteModel_DropTableStatement_strategy = st.builds(
    sqliteModel_DropTableStatement,
    ifExists=
        st.booleans()
)
sqliteModel_DropIndexStatement_strategy = st.builds(
    sqliteModel_DropIndexStatement,
    ifExists=
        st.booleans()
)
sqliteModel_CreateIndexStatement_strategy = st.builds(
    sqliteModel_CreateIndexStatement,
    unique=
        st.booleans(),
    name=
        safe_text
)
sqliteModel_DropTriggerStatement_strategy = st.builds(
    sqliteModel_DropTriggerStatement,
    ifExists=
        st.booleans()
)
sqliteModel_TableDefinition_strategy = st.builds(
    sqliteModel_TableDefinition,
    name=
        safe_text
)
SingleSource_strategy = st.builds(
    SingleSource,
)
sqliteModel_SingleSourceJoin_strategy = st.builds(
    sqliteModel_SingleSourceJoin,
)
sqliteModel_SelectSource_strategy = st.builds(
    sqliteModel_SelectSource,
    name=
        safe_text
)
sqliteModel_JoinStatement_strategy = st.builds(
    sqliteModel_JoinStatement,
    outer=
        st.booleans(),
    left=
        st.booleans(),
    natural=
        st.booleans(),
    cross=
        st.booleans(),
    inner=
        st.booleans()
)
sqliteModel_SingleSource_strategy = st.builds(
    sqliteModel_SingleSource,
)
sqliteModel_JoinSource_strategy = st.builds(
    sqliteModel_JoinSource,
)
sqliteModel_HavingExpressions_strategy = st.builds(
    sqliteModel_HavingExpressions,
)
sqliteModel_GroupByExpressions_strategy = st.builds(
    sqliteModel_GroupByExpressions,
)
sqliteModel_WhereExpressions_strategy = st.builds(
    sqliteModel_WhereExpressions,
)
sqliteModel_ColumnSource_strategy = st.builds(
    sqliteModel_ColumnSource,
    name=
        safe_text
)
sqliteModel_SelectList_strategy = st.builds(
    sqliteModel_SelectList,
)
sqliteModel_OrderingTerm_strategy = st.builds(
    sqliteModel_OrderingTerm,
    asc=
        st.booleans(),
    desc=
        st.booleans()
)
sqliteModel_OrderingTermList_strategy = st.builds(
    sqliteModel_OrderingTermList,
)
sqliteModel_SelectCoreExpression_strategy = st.builds(
    sqliteModel_SelectCoreExpression,
)
DMLStatement_strategy = st.builds(
    DMLStatement,
)
sqliteModel_InsertStatement_strategy = st.builds(
    sqliteModel_InsertStatement,
    conflictResolution=
        safe_text
)
sqliteModel_UpdateStatement_strategy = st.builds(
    sqliteModel_UpdateStatement,
    conflictResolution=
        safe_text
)
sqliteModel_DeleteStatement_strategy = st.builds(
    sqliteModel_DeleteStatement,
)
sqliteModel_SelectStatement_strategy = st.builds(
    sqliteModel_SelectStatement,
)
sqliteModel_Case_strategy = st.builds(
    sqliteModel_Case,
)
sqliteModel_Expression_strategy = st.builds(
    sqliteModel_Expression,
)
sqliteModel_ContentUriSegment_strategy = st.builds(
    sqliteModel_ContentUriSegment,
    name=
        safe_text
)
sqliteModel_ContentUri_strategy = st.builds(
    sqliteModel_ContentUri,
    type=
        safe_text
)
sqliteModel_FunctionArg_strategy = st.builds(
    sqliteModel_FunctionArg,
    name=
        safe_text,
    type=
        safe_text
)
sqliteModel_DDLStatement_strategy = st.builds(
    sqliteModel_DDLStatement,
)
sqliteModel_ConfigurationStatement_strategy = st.builds(
    sqliteModel_ConfigurationStatement,
    name=
        safe_text
)
sqliteModel_MigrationBlock_strategy = st.builds(
    sqliteModel_MigrationBlock,
)
sqliteModel_InitBlock_strategy = st.builds(
    sqliteModel_InitBlock,
)
sqliteModel_ConfigBlock_strategy = st.builds(
    sqliteModel_ConfigBlock,
)
sqliteModel_DatabaseBlock_strategy = st.builds(
    sqliteModel_DatabaseBlock,
    name=
        safe_text
)
sqliteModel_Model_strategy = st.builds(
    sqliteModel_Model,
    packageName=
        safe_text
)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=sqliteModel_LiteralDefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel_literaldefaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel_LiteralDefaultValue)

@given(instance=sqliteModel_ExpressionDefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel_expressiondefaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExpressionDefaultValue)

@given(instance=ColumnConstraint_strategy)
@settings(max_examples=50)
def test_columnconstraint_instantiation(instance):
    assert isinstance(instance, ColumnConstraint)

@given(instance=sqliteModel_UniqueConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_uniqueconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_UniqueConstraint)

@given(instance=sqliteModel_DefaultConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_defaultconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_DefaultConstraint)

@given(instance=sqliteModel_PrimaryKeyColumnConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_primarykeycolumnconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_PrimaryKeyColumnConstraint)



@given(instance=sqliteModel_PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel_primarykeycolumnconstraint_autoincrement_setter(instance):
    original = instance.autoincrement
    instance.autoincrement = original
    assert instance.autoincrement == original



@given(instance=sqliteModel_PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel_primarykeycolumnconstraint_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original



@given(instance=sqliteModel_PrimaryKeyColumnConstraint_strategy)
def test_sqlitemodel_primarykeycolumnconstraint_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel_NotNullConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_notnullconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_NotNullConstraint)

@given(instance=TableDefinition_strategy)
@settings(max_examples=50)
def test_tabledefinition_instantiation(instance):
    assert isinstance(instance, TableDefinition)

@given(instance=sqliteModel_AlterTableRenameStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_altertablerenamestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_AlterTableRenameStatement)

@given(instance=sqliteModel_CreateTableStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_createtablestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_CreateTableStatement)



@given(instance=sqliteModel_CreateTableStatement_strategy)
def test_sqlitemodel_createtablestatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original

@given(instance=ColumnSource_strategy)
@settings(max_examples=50)
def test_columnsource_instantiation(instance):
    assert isinstance(instance, ColumnSource)

@given(instance=sqliteModel_ResultColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel_resultcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel_ResultColumn)

@given(instance=SelectSource_strategy)
@settings(max_examples=50)
def test_selectsource_instantiation(instance):
    assert isinstance(instance, SelectSource)

@given(instance=sqliteModel_SingleSourceSelectStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_singlesourceselectstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_SingleSourceSelectStatement)

@given(instance=sqliteModel_SingleSourceTable_strategy)
@settings(max_examples=50)
def test_sqlitemodel_singlesourcetable_instantiation(instance):
    assert isinstance(instance, sqliteModel_SingleSourceTable)

@given(instance=LiteralValue_strategy)
@settings(max_examples=50)
def test_literalvalue_instantiation(instance):
    assert isinstance(instance, LiteralValue)

@given(instance=sqliteModel_NumericLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_numericliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_NumericLiteral)



@given(instance=sqliteModel_NumericLiteral_strategy)
def test_sqlitemodel_numericliteral_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=sqliteModel_CurrentTimeStampLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_currenttimestampliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_CurrentTimeStampLiteral)



@given(instance=sqliteModel_CurrentTimeStampLiteral_strategy)
def test_sqlitemodel_currenttimestampliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel_CurrentDateLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_currentdateliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_CurrentDateLiteral)



@given(instance=sqliteModel_CurrentDateLiteral_strategy)
def test_sqlitemodel_currentdateliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel_StringLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_stringliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_StringLiteral)



@given(instance=sqliteModel_StringLiteral_strategy)
def test_sqlitemodel_stringliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel_NullLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_nullliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_NullLiteral)



@given(instance=sqliteModel_NullLiteral_strategy)
def test_sqlitemodel_nullliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=sqliteModel_CurrentTimeLiteral_strategy)
@settings(max_examples=50)
def test_sqlitemodel_currenttimeliteral_instantiation(instance):
    assert isinstance(instance, sqliteModel_CurrentTimeLiteral)



@given(instance=sqliteModel_CurrentTimeLiteral_strategy)
def test_sqlitemodel_currenttimeliteral_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=SelectCoreExpression_strategy)
@settings(max_examples=50)
def test_selectcoreexpression_instantiation(instance):
    assert isinstance(instance, SelectCoreExpression)

@given(instance=sqliteModel_SelectCore_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectcore_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectCore)



@given(instance=sqliteModel_SelectCore_strategy)
def test_sqlitemodel_selectcore_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_SelectExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectExpression)



@given(instance=sqliteModel_SelectExpression_strategy)
def test_sqlitemodel_selectexpression_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original



@given(instance=sqliteModel_SelectExpression_strategy)
def test_sqlitemodel_selectexpression_allColumns_setter(instance):
    original = instance.allColumns
    instance.allColumns = original
    assert instance.allColumns == original



@given(instance=sqliteModel_SelectExpression_strategy)
def test_sqlitemodel_selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=ContentUriSegment_strategy)
@settings(max_examples=50)
def test_contenturisegment_instantiation(instance):
    assert isinstance(instance, ContentUriSegment)

@given(instance=sqliteModel_ContentUriParamSegment_strategy)
@settings(max_examples=50)
def test_sqlitemodel_contenturiparamsegment_instantiation(instance):
    assert isinstance(instance, sqliteModel_ContentUriParamSegment)



@given(instance=sqliteModel_ContentUriParamSegment_strategy)
def test_sqlitemodel_contenturiparamsegment_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=sqliteModel_ContentUriParamSegment_strategy)
def test_sqlitemodel_contenturiparamsegment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sqliteModel_ColumnSourceRef_strategy)
@settings(max_examples=50)
def test_sqlitemodel_columnsourceref_instantiation(instance):
    assert isinstance(instance, sqliteModel_ColumnSourceRef)



@given(instance=sqliteModel_ColumnSourceRef_strategy)
def test_sqlitemodel_columnsourceref_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sqliteModel_NewColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel_newcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel_NewColumn)

@given(instance=sqliteModel_ExprOr_strategy)
@settings(max_examples=50)
def test_sqlitemodel_expror_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprOr)



@given(instance=sqliteModel_ExprOr_strategy)
def test_sqlitemodel_expror_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_NullCheckExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_nullcheckexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_NullCheckExpression)

@given(instance=sqliteModel_CastExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_castexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_CastExpression)



@given(instance=sqliteModel_CastExpression_strategy)
def test_sqlitemodel_castexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel_IsNull_strategy)
@settings(max_examples=50)
def test_sqlitemodel_isnull_instantiation(instance):
    assert isinstance(instance, sqliteModel_IsNull)

@given(instance=sqliteModel_ExprRelate_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprrelate_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprRelate)



@given(instance=sqliteModel_ExprRelate_strategy)
def test_sqlitemodel_exprrelate_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_ExprEqual_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprequal_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprEqual)



@given(instance=sqliteModel_ExprEqual_strategy)
def test_sqlitemodel_exprequal_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_ExprAnd_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprand_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprAnd)



@given(instance=sqliteModel_ExprAnd_strategy)
def test_sqlitemodel_exprand_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_ExprBit_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprbit_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprBit)



@given(instance=sqliteModel_ExprBit_strategy)
def test_sqlitemodel_exprbit_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_ExprConcat_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprconcat_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprConcat)



@given(instance=sqliteModel_ExprConcat_strategy)
def test_sqlitemodel_exprconcat_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_ExprMult_strategy)
@settings(max_examples=50)
def test_sqlitemodel_exprmult_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprMult)



@given(instance=sqliteModel_ExprMult_strategy)
def test_sqlitemodel_exprmult_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_OldColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel_oldcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel_OldColumn)

@given(instance=sqliteModel_CaseExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_caseexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_CaseExpression)

@given(instance=sqliteModel_FunctionArgument_strategy)
@settings(max_examples=50)
def test_sqlitemodel_functionargument_instantiation(instance):
    assert isinstance(instance, sqliteModel_FunctionArgument)

@given(instance=sqliteModel_Literal_strategy)
@settings(max_examples=50)
def test_sqlitemodel_literal_instantiation(instance):
    assert isinstance(instance, sqliteModel_Literal)

@given(instance=sqliteModel_ExprAdd_strategy)
@settings(max_examples=50)
def test_sqlitemodel_expradd_instantiation(instance):
    assert isinstance(instance, sqliteModel_ExprAdd)



@given(instance=sqliteModel_ExprAdd_strategy)
def test_sqlitemodel_expradd_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sqliteModel_NestedExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_nestedexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_NestedExpression)

@given(instance=sqliteModel_SelectStatementExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectstatementexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectStatementExpression)



@given(instance=sqliteModel_SelectStatementExpression_strategy)
def test_sqlitemodel_selectstatementexpression_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=sqliteModel_SelectStatementExpression_strategy)
def test_sqlitemodel_selectstatementexpression_exists_setter(instance):
    original = instance.exists
    instance.exists = original
    assert instance.exists == original

@given(instance=sqliteModel_NotNull_strategy)
@settings(max_examples=50)
def test_sqlitemodel_notnull_instantiation(instance):
    assert isinstance(instance, sqliteModel_NotNull)

@given(instance=ConfigurationStatement_strategy)
@settings(max_examples=50)
def test_configurationstatement_instantiation(instance):
    assert isinstance(instance, ConfigurationStatement)

@given(instance=sqliteModel_Function_strategy)
@settings(max_examples=50)
def test_sqlitemodel_function_instantiation(instance):
    assert isinstance(instance, sqliteModel_Function)



@given(instance=sqliteModel_Function_strategy)
def test_sqlitemodel_function_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sqliteModel_ActionStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_actionstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_ActionStatement)

@given(instance=sqliteModel_UpdateColumnExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_updatecolumnexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_UpdateColumnExpression)

@given(instance=sqliteModel_DefaultValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel_defaultvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel_DefaultValue)

@given(instance=sqliteModel_ColumnDef_strategy)
@settings(max_examples=50)
def test_sqlitemodel_columndef_instantiation(instance):
    assert isinstance(instance, sqliteModel_ColumnDef)



@given(instance=sqliteModel_ColumnDef_strategy)
def test_sqlitemodel_columndef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel_ConflictClause_strategy)
@settings(max_examples=50)
def test_sqlitemodel_conflictclause_instantiation(instance):
    assert isinstance(instance, sqliteModel_ConflictClause)



@given(instance=sqliteModel_ConflictClause_strategy)
def test_sqlitemodel_conflictclause_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original

@given(instance=TableConstraint_strategy)
@settings(max_examples=50)
def test_tableconstraint_instantiation(instance):
    assert isinstance(instance, TableConstraint)

@given(instance=sqliteModel_CheckTableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_checktableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_CheckTableConstraint)

@given(instance=sqliteModel_UniqueTableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_uniquetableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_UniqueTableConstraint)

@given(instance=sqliteModel_TableConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_tableconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_TableConstraint)



@given(instance=sqliteModel_TableConstraint_strategy)
def test_sqlitemodel_tableconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_ColumnConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_columnconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_ColumnConstraint)

@given(instance=sqliteModel_IndexedColumn_strategy)
@settings(max_examples=50)
def test_sqlitemodel_indexedcolumn_instantiation(instance):
    assert isinstance(instance, sqliteModel_IndexedColumn)



@given(instance=sqliteModel_IndexedColumn_strategy)
def test_sqlitemodel_indexedcolumn_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original



@given(instance=sqliteModel_IndexedColumn_strategy)
def test_sqlitemodel_indexedcolumn_collationName_setter(instance):
    original = instance.collationName
    instance.collationName = original
    assert instance.collationName == original



@given(instance=sqliteModel_IndexedColumn_strategy)
def test_sqlitemodel_indexedcolumn_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel_PrimaryConstraint_strategy)
@settings(max_examples=50)
def test_sqlitemodel_primaryconstraint_instantiation(instance):
    assert isinstance(instance, sqliteModel_PrimaryConstraint)

@given(instance=sqliteModel_CreateViewStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_createviewstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_CreateViewStatement)



@given(instance=sqliteModel_CreateViewStatement_strategy)
def test_sqlitemodel_createviewstatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original

@given(instance=sqliteModel_DMLStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_dmlstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DMLStatement)

@given(instance=sqliteModel_LiteralValue_strategy)
@settings(max_examples=50)
def test_sqlitemodel_literalvalue_instantiation(instance):
    assert isinstance(instance, sqliteModel_LiteralValue)

@given(instance=DDLStatement_strategy)
@settings(max_examples=50)
def test_ddlstatement_instantiation(instance):
    assert isinstance(instance, DDLStatement)

@given(instance=sqliteModel_AlterTableAddColumnStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_altertableaddcolumnstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_AlterTableAddColumnStatement)

@given(instance=sqliteModel_DropViewStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_dropviewstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DropViewStatement)



@given(instance=sqliteModel_DropViewStatement_strategy)
def test_sqlitemodel_dropviewstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel_CreateTriggerStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_createtriggerstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_CreateTriggerStatement)



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_when_setter(instance):
    original = instance.when
    instance.when = original
    assert instance.when == original



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_eventType_setter(instance):
    original = instance.eventType
    instance.eventType = original
    assert instance.eventType == original



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_forEachRow_setter(instance):
    original = instance.forEachRow
    instance.forEachRow = original
    assert instance.forEachRow == original



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_temporary_setter(instance):
    original = instance.temporary
    instance.temporary = original
    assert instance.temporary == original



@given(instance=sqliteModel_CreateTriggerStatement_strategy)
def test_sqlitemodel_createtriggerstatement_updateColumnNames_setter(instance):
    original = instance.updateColumnNames
    instance.updateColumnNames = original
    assert instance.updateColumnNames == original

@given(instance=sqliteModel_DropTableStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_droptablestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DropTableStatement)



@given(instance=sqliteModel_DropTableStatement_strategy)
def test_sqlitemodel_droptablestatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel_DropIndexStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_dropindexstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DropIndexStatement)



@given(instance=sqliteModel_DropIndexStatement_strategy)
def test_sqlitemodel_dropindexstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel_CreateIndexStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_createindexstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_CreateIndexStatement)



@given(instance=sqliteModel_CreateIndexStatement_strategy)
def test_sqlitemodel_createindexstatement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=sqliteModel_CreateIndexStatement_strategy)
def test_sqlitemodel_createindexstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_DropTriggerStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_droptriggerstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DropTriggerStatement)



@given(instance=sqliteModel_DropTriggerStatement_strategy)
def test_sqlitemodel_droptriggerstatement_ifExists_setter(instance):
    original = instance.ifExists
    instance.ifExists = original
    assert instance.ifExists == original

@given(instance=sqliteModel_TableDefinition_strategy)
@settings(max_examples=50)
def test_sqlitemodel_tabledefinition_instantiation(instance):
    assert isinstance(instance, sqliteModel_TableDefinition)



@given(instance=sqliteModel_TableDefinition_strategy)
def test_sqlitemodel_tabledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SingleSource_strategy)
@settings(max_examples=50)
def test_singlesource_instantiation(instance):
    assert isinstance(instance, SingleSource)

@given(instance=sqliteModel_SingleSourceJoin_strategy)
@settings(max_examples=50)
def test_sqlitemodel_singlesourcejoin_instantiation(instance):
    assert isinstance(instance, sqliteModel_SingleSourceJoin)

@given(instance=sqliteModel_SelectSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectsource_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectSource)



@given(instance=sqliteModel_SelectSource_strategy)
def test_sqlitemodel_selectsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_JoinStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_joinstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_JoinStatement)



@given(instance=sqliteModel_JoinStatement_strategy)
def test_sqlitemodel_joinstatement_outer_setter(instance):
    original = instance.outer
    instance.outer = original
    assert instance.outer == original



@given(instance=sqliteModel_JoinStatement_strategy)
def test_sqlitemodel_joinstatement_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original



@given(instance=sqliteModel_JoinStatement_strategy)
def test_sqlitemodel_joinstatement_natural_setter(instance):
    original = instance.natural
    instance.natural = original
    assert instance.natural == original



@given(instance=sqliteModel_JoinStatement_strategy)
def test_sqlitemodel_joinstatement_cross_setter(instance):
    original = instance.cross
    instance.cross = original
    assert instance.cross == original



@given(instance=sqliteModel_JoinStatement_strategy)
def test_sqlitemodel_joinstatement_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=sqliteModel_SingleSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel_singlesource_instantiation(instance):
    assert isinstance(instance, sqliteModel_SingleSource)

@given(instance=sqliteModel_JoinSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel_joinsource_instantiation(instance):
    assert isinstance(instance, sqliteModel_JoinSource)

@given(instance=sqliteModel_HavingExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel_havingexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel_HavingExpressions)

@given(instance=sqliteModel_GroupByExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel_groupbyexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel_GroupByExpressions)

@given(instance=sqliteModel_WhereExpressions_strategy)
@settings(max_examples=50)
def test_sqlitemodel_whereexpressions_instantiation(instance):
    assert isinstance(instance, sqliteModel_WhereExpressions)

@given(instance=sqliteModel_ColumnSource_strategy)
@settings(max_examples=50)
def test_sqlitemodel_columnsource_instantiation(instance):
    assert isinstance(instance, sqliteModel_ColumnSource)



@given(instance=sqliteModel_ColumnSource_strategy)
def test_sqlitemodel_columnsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_SelectList_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectlist_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectList)

@given(instance=sqliteModel_OrderingTerm_strategy)
@settings(max_examples=50)
def test_sqlitemodel_orderingterm_instantiation(instance):
    assert isinstance(instance, sqliteModel_OrderingTerm)



@given(instance=sqliteModel_OrderingTerm_strategy)
def test_sqlitemodel_orderingterm_asc_setter(instance):
    original = instance.asc
    instance.asc = original
    assert instance.asc == original



@given(instance=sqliteModel_OrderingTerm_strategy)
def test_sqlitemodel_orderingterm_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=sqliteModel_OrderingTermList_strategy)
@settings(max_examples=50)
def test_sqlitemodel_orderingtermlist_instantiation(instance):
    assert isinstance(instance, sqliteModel_OrderingTermList)

@given(instance=sqliteModel_SelectCoreExpression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectcoreexpression_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectCoreExpression)

@given(instance=DMLStatement_strategy)
@settings(max_examples=50)
def test_dmlstatement_instantiation(instance):
    assert isinstance(instance, DMLStatement)

@given(instance=sqliteModel_InsertStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_insertstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_InsertStatement)



@given(instance=sqliteModel_InsertStatement_strategy)
def test_sqlitemodel_insertstatement_conflictResolution_setter(instance):
    original = instance.conflictResolution
    instance.conflictResolution = original
    assert instance.conflictResolution == original

@given(instance=sqliteModel_UpdateStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_updatestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_UpdateStatement)



@given(instance=sqliteModel_UpdateStatement_strategy)
def test_sqlitemodel_updatestatement_conflictResolution_setter(instance):
    original = instance.conflictResolution
    instance.conflictResolution = original
    assert instance.conflictResolution == original

@given(instance=sqliteModel_DeleteStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_deletestatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DeleteStatement)

@given(instance=sqliteModel_SelectStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_selectstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_SelectStatement)

@given(instance=sqliteModel_Case_strategy)
@settings(max_examples=50)
def test_sqlitemodel_case_instantiation(instance):
    assert isinstance(instance, sqliteModel_Case)

@given(instance=sqliteModel_Expression_strategy)
@settings(max_examples=50)
def test_sqlitemodel_expression_instantiation(instance):
    assert isinstance(instance, sqliteModel_Expression)

@given(instance=sqliteModel_ContentUriSegment_strategy)
@settings(max_examples=50)
def test_sqlitemodel_contenturisegment_instantiation(instance):
    assert isinstance(instance, sqliteModel_ContentUriSegment)



@given(instance=sqliteModel_ContentUriSegment_strategy)
def test_sqlitemodel_contenturisegment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_ContentUri_strategy)
@settings(max_examples=50)
def test_sqlitemodel_contenturi_instantiation(instance):
    assert isinstance(instance, sqliteModel_ContentUri)



@given(instance=sqliteModel_ContentUri_strategy)
def test_sqlitemodel_contenturi_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel_FunctionArg_strategy)
@settings(max_examples=50)
def test_sqlitemodel_functionarg_instantiation(instance):
    assert isinstance(instance, sqliteModel_FunctionArg)



@given(instance=sqliteModel_FunctionArg_strategy)
def test_sqlitemodel_functionarg_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqliteModel_FunctionArg_strategy)
def test_sqlitemodel_functionarg_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sqliteModel_DDLStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_ddlstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_DDLStatement)

@given(instance=sqliteModel_ConfigurationStatement_strategy)
@settings(max_examples=50)
def test_sqlitemodel_configurationstatement_instantiation(instance):
    assert isinstance(instance, sqliteModel_ConfigurationStatement)



@given(instance=sqliteModel_ConfigurationStatement_strategy)
def test_sqlitemodel_configurationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_MigrationBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel_migrationblock_instantiation(instance):
    assert isinstance(instance, sqliteModel_MigrationBlock)

@given(instance=sqliteModel_InitBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel_initblock_instantiation(instance):
    assert isinstance(instance, sqliteModel_InitBlock)

@given(instance=sqliteModel_ConfigBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel_configblock_instantiation(instance):
    assert isinstance(instance, sqliteModel_ConfigBlock)

@given(instance=sqliteModel_DatabaseBlock_strategy)
@settings(max_examples=50)
def test_sqlitemodel_databaseblock_instantiation(instance):
    assert isinstance(instance, sqliteModel_DatabaseBlock)



@given(instance=sqliteModel_DatabaseBlock_strategy)
def test_sqlitemodel_databaseblock_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqliteModel_Model_strategy)
@settings(max_examples=50)
def test_sqlitemodel_model_instantiation(instance):
    assert isinstance(instance, sqliteModel_Model)



@given(instance=sqliteModel_Model_strategy)
def test_sqlitemodel_model_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original
