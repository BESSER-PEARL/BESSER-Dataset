import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Operands,
    sql::Concat,
    sql::Div,
    sql::Star,
    sql::Minus,
    sql::Plus,
    UnpivotInClause,
    sql::UnipivotInClause,
    SQLCaseWhens,
    sql::WhenList,
    sql::SqlCaseWhen,
    sql::SQLCaseWhens,
    OperandList,
    sql::OpList,
    AnalyticExprArgs,
    sql::AExpArgs,
    sql::OpFunctionArgAgregate,
    OpFunctionArg,
    sql::OpFList,
    sql::OpFunctionArgOperand,
    OrderByClauseArgs,
    sql::OBCArgs,
    sql::OrderByClauseArg,
    sql::OrderByClauseArgs,
    QueryPartitionClause,
    sql::AnalyticExprArgs,
    sql::WindowingClauseOperandFollowing,
    sql::AnalyticExprArg,
    sql::QueryPartitionClause,
    sql::AnalyticClause,
    WindowingClause,
    sql::WindowingClauseOperandPreceding,
    sql::WindowingClauseBetween,
    sql::WindowingClause,
    sql::OrderByClause,
    sql::ScalarOperand,
    sql::ExpOperand,
    sql::FunctionAnalytical,
    sql::OpFunctionArg,
    sql::ColumnOperand,
    sql::SQLCaseOperand,
    sql::FunctionExtract,
    OpFunctionArgAgregate,
    sql::OperandList,
    sql::Operand,
    sql::OperandListGroup,
    sql::LikeOperand,
    sql::POperand,
    sql::OpFunctionCast,
    sql::Prms,
    Prms,
    sql::JRParameter,
    sql::Comparison,
    sql::Like,
    sql::ExistsOper,
    sql::InOper,
    sql::XExpr,
    sql::ExprGroup,
    sql::Between,
    OrExpr,
    sql::FullExpression,
    sql::OpFunction,
    OrGroupByColumn,
    sql::GroupByColumnFull,
    OrOrderByColumn,
    sql::OrderByColumnFull,
    TableFull,
    sql::tbls,
    PivotCol,
    sql::pcols,
    ColumnFull,
    sql::Col,
    Pivots,
    sql::pvcs,
    PivotFunction,
    PivotColumns,
    sql::PivotCol,
    sql::Pivots,
    UnpivotInClauseArgs,
    sql::uicargs,
    sql::UnpivotInClauseArg,
    sql::PivotFunction,
    sql::UnpivotInClause,
    sql::PivotColumns,
    sql::UnpivotInClauseArgs,
    sql::PivotFunctions,
    sql::PivotInClause,
    sql::PivotForClause,
    sql::FromTableJoin,
    sql::UnpivotTable,
    sql::PivotTable,
    sql::SubQueryOperand,
    sql::TableFull,
    sql::DbObjectNameAll,
    sql::DbObjectName,
    sql::TableOrAlias,
    OrTable,
    sql::FromTable,
    sql::Operands,
    OrColumn,
    sql::ColumnOrAlias,
    PivotForClause,
    sql::ColumnFull,
    sql::OrExpr,
    sql::OrTable,
    sql::OrColumn,
    sql::OrOrderByColumn,
    sql::OrGroupByColumn,
    sql::Limit,
    sql::Offset,
    SelectQuery,
    sql::Select,
    sql::SelectSubSet,
    sql::Model,
    sql::IntegerValue,
    sql::FetchFirst,
    sql::SelectQuery,
    XFunction,
    EXTRACT_VALUES,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operands_is_not_abstract():
    assert not inspect.isabstract(Operands)


def test_operands_constructor_exists():
    assert callable(Operands.__init__)


def test_operands_constructor_args():
    sig = inspect.signature(Operands.__init__)
    params = list(sig.parameters.keys())



def test_sql::concat_is_not_abstract():
    assert not inspect.isabstract(sql::Concat)


def test_sql::concat_constructor_exists():
    assert callable(sql::Concat.__init__)


def test_sql::concat_constructor_args():
    sig = inspect.signature(sql::Concat.__init__)
    params = list(sig.parameters.keys())



def test_sql::div_is_not_abstract():
    assert not inspect.isabstract(sql::Div)


def test_sql::div_constructor_exists():
    assert callable(sql::Div.__init__)


def test_sql::div_constructor_args():
    sig = inspect.signature(sql::Div.__init__)
    params = list(sig.parameters.keys())



def test_sql::star_is_not_abstract():
    assert not inspect.isabstract(sql::Star)


def test_sql::star_constructor_exists():
    assert callable(sql::Star.__init__)


def test_sql::star_constructor_args():
    sig = inspect.signature(sql::Star.__init__)
    params = list(sig.parameters.keys())



def test_sql::minus_is_not_abstract():
    assert not inspect.isabstract(sql::Minus)


def test_sql::minus_constructor_exists():
    assert callable(sql::Minus.__init__)


def test_sql::minus_constructor_args():
    sig = inspect.signature(sql::Minus.__init__)
    params = list(sig.parameters.keys())



def test_sql::plus_is_not_abstract():
    assert not inspect.isabstract(sql::Plus)


def test_sql::plus_constructor_exists():
    assert callable(sql::Plus.__init__)


def test_sql::plus_constructor_args():
    sig = inspect.signature(sql::Plus.__init__)
    params = list(sig.parameters.keys())



def test_unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClause)


def test_unpivotinclause_constructor_exists():
    assert callable(UnpivotInClause.__init__)


def test_unpivotinclause_constructor_args():
    sig = inspect.signature(UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::unipivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql::UnipivotInClause)


def test_sql::unipivotinclause_constructor_exists():
    assert callable(sql::UnipivotInClause.__init__)


def test_sql::unipivotinclause_constructor_args():
    sig = inspect.signature(sql::UnipivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql::unipivotinclause_has_op():
    assert hasattr(sql::UnipivotInClause, "op")
    descriptor = None
    for klass in sql::UnipivotInClause.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(SQLCaseWhens)


def test_sqlcasewhens_constructor_exists():
    assert callable(SQLCaseWhens.__init__)


def test_sqlcasewhens_constructor_args():
    sig = inspect.signature(SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_sql::whenlist_is_not_abstract():
    assert not inspect.isabstract(sql::WhenList)


def test_sql::whenlist_constructor_exists():
    assert callable(sql::WhenList.__init__)


def test_sql::whenlist_constructor_args():
    sig = inspect.signature(sql::WhenList.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqlcasewhen_is_not_abstract():
    assert not inspect.isabstract(sql::SqlCaseWhen)


def test_sql::sqlcasewhen_constructor_exists():
    assert callable(sql::SqlCaseWhen.__init__)


def test_sql::sqlcasewhen_constructor_args():
    sig = inspect.signature(sql::SqlCaseWhen.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(sql::SQLCaseWhens)


def test_sql::sqlcasewhens_constructor_exists():
    assert callable(sql::SQLCaseWhens.__init__)


def test_sql::sqlcasewhens_constructor_args():
    sig = inspect.signature(sql::SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_operandlist_is_not_abstract():
    assert not inspect.isabstract(OperandList)


def test_operandlist_constructor_exists():
    assert callable(OperandList.__init__)


def test_operandlist_constructor_args():
    sig = inspect.signature(OperandList.__init__)
    params = list(sig.parameters.keys())



def test_sql::oplist_is_not_abstract():
    assert not inspect.isabstract(sql::OpList)


def test_sql::oplist_constructor_exists():
    assert callable(sql::OpList.__init__)


def test_sql::oplist_constructor_args():
    sig = inspect.signature(sql::OpList.__init__)
    params = list(sig.parameters.keys())



def test_analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(AnalyticExprArgs)


def test_analyticexprargs_constructor_exists():
    assert callable(AnalyticExprArgs.__init__)


def test_analyticexprargs_constructor_args():
    sig = inspect.signature(AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::aexpargs_is_not_abstract():
    assert not inspect.isabstract(sql::AExpArgs)


def test_sql::aexpargs_constructor_exists():
    assert callable(sql::AExpArgs.__init__)


def test_sql::aexpargs_constructor_args():
    sig = inspect.signature(sql::AExpArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(sql::OpFunctionArgAgregate)


def test_sql::opfunctionargagregate_constructor_exists():
    assert callable(sql::OpFunctionArgAgregate.__init__)


def test_sql::opfunctionargagregate_constructor_args():
    sig = inspect.signature(sql::OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArg)


def test_opfunctionarg_constructor_exists():
    assert callable(OpFunctionArg.__init__)


def test_opfunctionarg_constructor_args():
    sig = inspect.signature(OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_sql::opflist_is_not_abstract():
    assert not inspect.isabstract(sql::OpFList)


def test_sql::opflist_constructor_exists():
    assert callable(sql::OpFList.__init__)


def test_sql::opflist_constructor_args():
    sig = inspect.signature(sql::OpFList.__init__)
    params = list(sig.parameters.keys())



def test_sql::opfunctionargoperand_is_not_abstract():
    assert not inspect.isabstract(sql::OpFunctionArgOperand)


def test_sql::opfunctionargoperand_constructor_exists():
    assert callable(sql::OpFunctionArgOperand.__init__)


def test_sql::opfunctionargoperand_constructor_args():
    sig = inspect.signature(sql::OpFunctionArgOperand.__init__)
    params = list(sig.parameters.keys())



def test_orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(OrderByClauseArgs)


def test_orderbyclauseargs_constructor_exists():
    assert callable(OrderByClauseArgs.__init__)


def test_orderbyclauseargs_constructor_args():
    sig = inspect.signature(OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::obcargs_is_not_abstract():
    assert not inspect.isabstract(sql::OBCArgs)


def test_sql::obcargs_constructor_exists():
    assert callable(sql::OBCArgs.__init__)


def test_sql::obcargs_constructor_args():
    sig = inspect.signature(sql::OBCArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderbyclausearg_is_not_abstract():
    assert not inspect.isabstract(sql::OrderByClauseArg)


def test_sql::orderbyclausearg_constructor_exists():
    assert callable(sql::OrderByClauseArg.__init__)


def test_sql::orderbyclausearg_constructor_args():
    sig = inspect.signature(sql::OrderByClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql::OrderByClauseArgs)


def test_sql::orderbyclauseargs_constructor_exists():
    assert callable(sql::OrderByClauseArgs.__init__)


def test_sql::orderbyclauseargs_constructor_args():
    sig = inspect.signature(sql::OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(QueryPartitionClause)


def test_querypartitionclause_constructor_exists():
    assert callable(QueryPartitionClause.__init__)


def test_querypartitionclause_constructor_args():
    sig = inspect.signature(QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(sql::AnalyticExprArgs)


def test_sql::analyticexprargs_constructor_exists():
    assert callable(sql::AnalyticExprArgs.__init__)


def test_sql::analyticexprargs_constructor_args():
    sig = inspect.signature(sql::AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::windowingclauseoperandfollowing_is_not_abstract():
    assert not inspect.isabstract(sql::WindowingClauseOperandFollowing)


def test_sql::windowingclauseoperandfollowing_constructor_exists():
    assert callable(sql::WindowingClauseOperandFollowing.__init__)


def test_sql::windowingclauseoperandfollowing_constructor_args():
    sig = inspect.signature(sql::WindowingClauseOperandFollowing.__init__)
    params = list(sig.parameters.keys())



def test_sql::analyticexprarg_is_not_abstract():
    assert not inspect.isabstract(sql::AnalyticExprArg)


def test_sql::analyticexprarg_constructor_exists():
    assert callable(sql::AnalyticExprArg.__init__)


def test_sql::analyticexprarg_constructor_args():
    sig = inspect.signature(sql::AnalyticExprArg.__init__)
    params = list(sig.parameters.keys())



def test_sql::querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(sql::QueryPartitionClause)


def test_sql::querypartitionclause_constructor_exists():
    assert callable(sql::QueryPartitionClause.__init__)


def test_sql::querypartitionclause_constructor_args():
    sig = inspect.signature(sql::QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::analyticclause_is_not_abstract():
    assert not inspect.isabstract(sql::AnalyticClause)


def test_sql::analyticclause_constructor_exists():
    assert callable(sql::AnalyticClause.__init__)


def test_sql::analyticclause_constructor_args():
    sig = inspect.signature(sql::AnalyticClause.__init__)
    params = list(sig.parameters.keys())



def test_windowingclause_is_not_abstract():
    assert not inspect.isabstract(WindowingClause)


def test_windowingclause_constructor_exists():
    assert callable(WindowingClause.__init__)


def test_windowingclause_constructor_args():
    sig = inspect.signature(WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::windowingclauseoperandpreceding_is_not_abstract():
    assert not inspect.isabstract(sql::WindowingClauseOperandPreceding)


def test_sql::windowingclauseoperandpreceding_constructor_exists():
    assert callable(sql::WindowingClauseOperandPreceding.__init__)


def test_sql::windowingclauseoperandpreceding_constructor_args():
    sig = inspect.signature(sql::WindowingClauseOperandPreceding.__init__)
    params = list(sig.parameters.keys())



def test_sql::windowingclausebetween_is_not_abstract():
    assert not inspect.isabstract(sql::WindowingClauseBetween)


def test_sql::windowingclausebetween_constructor_exists():
    assert callable(sql::WindowingClauseBetween.__init__)


def test_sql::windowingclausebetween_constructor_args():
    sig = inspect.signature(sql::WindowingClauseBetween.__init__)
    params = list(sig.parameters.keys())



def test_sql::windowingclause_is_not_abstract():
    assert not inspect.isabstract(sql::WindowingClause)


def test_sql::windowingclause_constructor_exists():
    assert callable(sql::WindowingClause.__init__)


def test_sql::windowingclause_constructor_args():
    sig = inspect.signature(sql::WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderbyclause_is_not_abstract():
    assert not inspect.isabstract(sql::OrderByClause)


def test_sql::orderbyclause_constructor_exists():
    assert callable(sql::OrderByClause.__init__)


def test_sql::orderbyclause_constructor_args():
    sig = inspect.signature(sql::OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::scalaroperand_is_not_abstract():
    assert not inspect.isabstract(sql::ScalarOperand)


def test_sql::scalaroperand_constructor_exists():
    assert callable(sql::ScalarOperand.__init__)


def test_sql::scalaroperand_constructor_args():
    sig = inspect.signature(sql::ScalarOperand.__init__)
    params = list(sig.parameters.keys())
    assert "sodate" in params, "Missing parameter 'sodate'"
    assert "soint" in params, "Missing parameter 'soint'"
    assert "sotime" in params, "Missing parameter 'sotime'"
    assert "sodbl" in params, "Missing parameter 'sodbl'"
    assert "sostr" in params, "Missing parameter 'sostr'"
    assert "sodt" in params, "Missing parameter 'sodt'"

def test_sql::scalaroperand_has_sodate():
    assert hasattr(sql::ScalarOperand, "sodate")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "sodate" in klass.__dict__:
            descriptor = klass.__dict__["sodate"]
            break
    assert isinstance(descriptor, property)

def test_sql::scalaroperand_has_soint():
    assert hasattr(sql::ScalarOperand, "soint")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "soint" in klass.__dict__:
            descriptor = klass.__dict__["soint"]
            break
    assert isinstance(descriptor, property)

def test_sql::scalaroperand_has_sotime():
    assert hasattr(sql::ScalarOperand, "sotime")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "sotime" in klass.__dict__:
            descriptor = klass.__dict__["sotime"]
            break
    assert isinstance(descriptor, property)

def test_sql::scalaroperand_has_sodbl():
    assert hasattr(sql::ScalarOperand, "sodbl")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "sodbl" in klass.__dict__:
            descriptor = klass.__dict__["sodbl"]
            break
    assert isinstance(descriptor, property)

def test_sql::scalaroperand_has_sostr():
    assert hasattr(sql::ScalarOperand, "sostr")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "sostr" in klass.__dict__:
            descriptor = klass.__dict__["sostr"]
            break
    assert isinstance(descriptor, property)

def test_sql::scalaroperand_has_sodt():
    assert hasattr(sql::ScalarOperand, "sodt")
    descriptor = None
    for klass in sql::ScalarOperand.__mro__:
        if "sodt" in klass.__dict__:
            descriptor = klass.__dict__["sodt"]
            break
    assert isinstance(descriptor, property)



def test_sql::expoperand_is_not_abstract():
    assert not inspect.isabstract(sql::ExpOperand)


def test_sql::expoperand_constructor_exists():
    assert callable(sql::ExpOperand.__init__)


def test_sql::expoperand_constructor_args():
    sig = inspect.signature(sql::ExpOperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"

def test_sql::expoperand_has_prm():
    assert hasattr(sql::ExpOperand, "prm")
    descriptor = None
    for klass in sql::ExpOperand.__mro__:
        if "prm" in klass.__dict__:
            descriptor = klass.__dict__["prm"]
            break
    assert isinstance(descriptor, property)



def test_sql::functionanalytical_is_not_abstract():
    assert not inspect.isabstract(sql::FunctionAnalytical)


def test_sql::functionanalytical_constructor_exists():
    assert callable(sql::FunctionAnalytical.__init__)


def test_sql::functionanalytical_constructor_args():
    sig = inspect.signature(sql::FunctionAnalytical.__init__)
    params = list(sig.parameters.keys())



def test_sql::opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(sql::OpFunctionArg)


def test_sql::opfunctionarg_constructor_exists():
    assert callable(sql::OpFunctionArg.__init__)


def test_sql::opfunctionarg_constructor_args():
    sig = inspect.signature(sql::OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_sql::columnoperand_is_not_abstract():
    assert not inspect.isabstract(sql::ColumnOperand)


def test_sql::columnoperand_constructor_exists():
    assert callable(sql::ColumnOperand.__init__)


def test_sql::columnoperand_constructor_args():
    sig = inspect.signature(sql::ColumnOperand.__init__)
    params = list(sig.parameters.keys())
    assert "ora" in params, "Missing parameter 'ora'"

def test_sql::columnoperand_has_ora():
    assert hasattr(sql::ColumnOperand, "ora")
    descriptor = None
    for klass in sql::ColumnOperand.__mro__:
        if "ora" in klass.__dict__:
            descriptor = klass.__dict__["ora"]
            break
    assert isinstance(descriptor, property)



def test_sql::sqlcaseoperand_is_not_abstract():
    assert not inspect.isabstract(sql::SQLCaseOperand)


def test_sql::sqlcaseoperand_constructor_exists():
    assert callable(sql::SQLCaseOperand.__init__)


def test_sql::sqlcaseoperand_constructor_args():
    sig = inspect.signature(sql::SQLCaseOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql::functionextract_is_not_abstract():
    assert not inspect.isabstract(sql::FunctionExtract)


def test_sql::functionextract_constructor_exists():
    assert callable(sql::FunctionExtract.__init__)


def test_sql::functionextract_constructor_args():
    sig = inspect.signature(sql::FunctionExtract.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"

def test_sql::functionextract_has_v():
    assert hasattr(sql::FunctionExtract, "v")
    descriptor = None
    for klass in sql::FunctionExtract.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)



def test_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArgAgregate)


def test_opfunctionargagregate_constructor_exists():
    assert callable(OpFunctionArgAgregate.__init__)


def test_opfunctionargagregate_constructor_args():
    sig = inspect.signature(OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_sql::operandlist_is_not_abstract():
    assert not inspect.isabstract(sql::OperandList)


def test_sql::operandlist_constructor_exists():
    assert callable(sql::OperandList.__init__)


def test_sql::operandlist_constructor_args():
    sig = inspect.signature(sql::OperandList.__init__)
    params = list(sig.parameters.keys())



def test_sql::operand_is_not_abstract():
    assert not inspect.isabstract(sql::Operand)


def test_sql::operand_constructor_exists():
    assert callable(sql::Operand.__init__)


def test_sql::operand_constructor_args():
    sig = inspect.signature(sql::Operand.__init__)
    params = list(sig.parameters.keys())



def test_sql::operandlistgroup_is_not_abstract():
    assert not inspect.isabstract(sql::OperandListGroup)


def test_sql::operandlistgroup_constructor_exists():
    assert callable(sql::OperandListGroup.__init__)


def test_sql::operandlistgroup_constructor_args():
    sig = inspect.signature(sql::OperandListGroup.__init__)
    params = list(sig.parameters.keys())



def test_sql::likeoperand_is_not_abstract():
    assert not inspect.isabstract(sql::LikeOperand)


def test_sql::likeoperand_constructor_exists():
    assert callable(sql::LikeOperand.__init__)


def test_sql::likeoperand_constructor_args():
    sig = inspect.signature(sql::LikeOperand.__init__)
    params = list(sig.parameters.keys())
    assert "op2" in params, "Missing parameter 'op2'"

def test_sql::likeoperand_has_op2():
    assert hasattr(sql::LikeOperand, "op2")
    descriptor = None
    for klass in sql::LikeOperand.__mro__:
        if "op2" in klass.__dict__:
            descriptor = klass.__dict__["op2"]
            break
    assert isinstance(descriptor, property)



def test_sql::poperand_is_not_abstract():
    assert not inspect.isabstract(sql::POperand)


def test_sql::poperand_constructor_exists():
    assert callable(sql::POperand.__init__)


def test_sql::poperand_constructor_args():
    sig = inspect.signature(sql::POperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"

def test_sql::poperand_has_prm():
    assert hasattr(sql::POperand, "prm")
    descriptor = None
    for klass in sql::POperand.__mro__:
        if "prm" in klass.__dict__:
            descriptor = klass.__dict__["prm"]
            break
    assert isinstance(descriptor, property)



def test_sql::opfunctioncast_is_not_abstract():
    assert not inspect.isabstract(sql::OpFunctionCast)


def test_sql::opfunctioncast_constructor_exists():
    assert callable(sql::OpFunctionCast.__init__)


def test_sql::opfunctioncast_constructor_args():
    sig = inspect.signature(sql::OpFunctionCast.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"
    assert "p2" in params, "Missing parameter 'p2'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql::opfunctioncast_has_p():
    assert hasattr(sql::OpFunctionCast, "p")
    descriptor = None
    for klass in sql::OpFunctionCast.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_sql::opfunctioncast_has_p2():
    assert hasattr(sql::OpFunctionCast, "p2")
    descriptor = None
    for klass in sql::OpFunctionCast.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)

def test_sql::opfunctioncast_has_type():
    assert hasattr(sql::OpFunctionCast, "type")
    descriptor = None
    for klass in sql::OpFunctionCast.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql::prms_is_not_abstract():
    assert not inspect.isabstract(sql::Prms)


def test_sql::prms_constructor_exists():
    assert callable(sql::Prms.__init__)


def test_sql::prms_constructor_args():
    sig = inspect.signature(sql::Prms.__init__)
    params = list(sig.parameters.keys())



def test_prms_is_not_abstract():
    assert not inspect.isabstract(Prms)


def test_prms_constructor_exists():
    assert callable(Prms.__init__)


def test_prms_constructor_args():
    sig = inspect.signature(Prms.__init__)
    params = list(sig.parameters.keys())



def test_sql::jrparameter_is_not_abstract():
    assert not inspect.isabstract(sql::JRParameter)


def test_sql::jrparameter_constructor_exists():
    assert callable(sql::JRParameter.__init__)


def test_sql::jrparameter_constructor_args():
    sig = inspect.signature(sql::JRParameter.__init__)
    params = list(sig.parameters.keys())
    assert "jrprm" in params, "Missing parameter 'jrprm'"

def test_sql::jrparameter_has_jrprm():
    assert hasattr(sql::JRParameter, "jrprm")
    descriptor = None
    for klass in sql::JRParameter.__mro__:
        if "jrprm" in klass.__dict__:
            descriptor = klass.__dict__["jrprm"]
            break
    assert isinstance(descriptor, property)



def test_sql::comparison_is_not_abstract():
    assert not inspect.isabstract(sql::Comparison)


def test_sql::comparison_constructor_exists():
    assert callable(sql::Comparison.__init__)


def test_sql::comparison_constructor_args():
    sig = inspect.signature(sql::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "subOperator" in params, "Missing parameter 'subOperator'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_sql::comparison_has_subOperator():
    assert hasattr(sql::Comparison, "subOperator")
    descriptor = None
    for klass in sql::Comparison.__mro__:
        if "subOperator" in klass.__dict__:
            descriptor = klass.__dict__["subOperator"]
            break
    assert isinstance(descriptor, property)

def test_sql::comparison_has_operator():
    assert hasattr(sql::Comparison, "operator")
    descriptor = None
    for klass in sql::Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sql::like_is_not_abstract():
    assert not inspect.isabstract(sql::Like)


def test_sql::like_constructor_exists():
    assert callable(sql::Like.__init__)


def test_sql::like_constructor_args():
    sig = inspect.signature(sql::Like.__init__)
    params = list(sig.parameters.keys())
    assert "opLike" in params, "Missing parameter 'opLike'"

def test_sql::like_has_opLike():
    assert hasattr(sql::Like, "opLike")
    descriptor = None
    for klass in sql::Like.__mro__:
        if "opLike" in klass.__dict__:
            descriptor = klass.__dict__["opLike"]
            break
    assert isinstance(descriptor, property)



def test_sql::existsoper_is_not_abstract():
    assert not inspect.isabstract(sql::ExistsOper)


def test_sql::existsoper_constructor_exists():
    assert callable(sql::ExistsOper.__init__)


def test_sql::existsoper_constructor_args():
    sig = inspect.signature(sql::ExistsOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql::existsoper_has_op():
    assert hasattr(sql::ExistsOper, "op")
    descriptor = None
    for klass in sql::ExistsOper.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sql::inoper_is_not_abstract():
    assert not inspect.isabstract(sql::InOper)


def test_sql::inoper_constructor_exists():
    assert callable(sql::InOper.__init__)


def test_sql::inoper_constructor_args():
    sig = inspect.signature(sql::InOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql::inoper_has_op():
    assert hasattr(sql::InOper, "op")
    descriptor = None
    for klass in sql::InOper.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sql::xexpr_is_not_abstract():
    assert not inspect.isabstract(sql::XExpr)


def test_sql::xexpr_constructor_exists():
    assert callable(sql::XExpr.__init__)


def test_sql::xexpr_constructor_args():
    sig = inspect.signature(sql::XExpr.__init__)
    params = list(sig.parameters.keys())
    assert "xf" in params, "Missing parameter 'xf'"

def test_sql::xexpr_has_xf():
    assert hasattr(sql::XExpr, "xf")
    descriptor = None
    for klass in sql::XExpr.__mro__:
        if "xf" in klass.__dict__:
            descriptor = klass.__dict__["xf"]
            break
    assert isinstance(descriptor, property)



def test_sql::exprgroup_is_not_abstract():
    assert not inspect.isabstract(sql::ExprGroup)


def test_sql::exprgroup_constructor_exists():
    assert callable(sql::ExprGroup.__init__)


def test_sql::exprgroup_constructor_args():
    sig = inspect.signature(sql::ExprGroup.__init__)
    params = list(sig.parameters.keys())
    assert "isnot" in params, "Missing parameter 'isnot'"

def test_sql::exprgroup_has_isnot():
    assert hasattr(sql::ExprGroup, "isnot")
    descriptor = None
    for klass in sql::ExprGroup.__mro__:
        if "isnot" in klass.__dict__:
            descriptor = klass.__dict__["isnot"]
            break
    assert isinstance(descriptor, property)



def test_sql::between_is_not_abstract():
    assert not inspect.isabstract(sql::Between)


def test_sql::between_constructor_exists():
    assert callable(sql::Between.__init__)


def test_sql::between_constructor_args():
    sig = inspect.signature(sql::Between.__init__)
    params = list(sig.parameters.keys())
    assert "opBetween" in params, "Missing parameter 'opBetween'"

def test_sql::between_has_opBetween():
    assert hasattr(sql::Between, "opBetween")
    descriptor = None
    for klass in sql::Between.__mro__:
        if "opBetween" in klass.__dict__:
            descriptor = klass.__dict__["opBetween"]
            break
    assert isinstance(descriptor, property)



def test_orexpr_is_not_abstract():
    assert not inspect.isabstract(OrExpr)


def test_orexpr_constructor_exists():
    assert callable(OrExpr.__init__)


def test_orexpr_constructor_args():
    sig = inspect.signature(OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_sql::fullexpression_is_not_abstract():
    assert not inspect.isabstract(sql::FullExpression)


def test_sql::fullexpression_constructor_exists():
    assert callable(sql::FullExpression.__init__)


def test_sql::fullexpression_constructor_args():
    sig = inspect.signature(sql::FullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "notPrm" in params, "Missing parameter 'notPrm'"
    assert "isnull" in params, "Missing parameter 'isnull'"
    assert "c" in params, "Missing parameter 'c'"

def test_sql::fullexpression_has_notPrm():
    assert hasattr(sql::FullExpression, "notPrm")
    descriptor = None
    for klass in sql::FullExpression.__mro__:
        if "notPrm" in klass.__dict__:
            descriptor = klass.__dict__["notPrm"]
            break
    assert isinstance(descriptor, property)

def test_sql::fullexpression_has_isnull():
    assert hasattr(sql::FullExpression, "isnull")
    descriptor = None
    for klass in sql::FullExpression.__mro__:
        if "isnull" in klass.__dict__:
            descriptor = klass.__dict__["isnull"]
            break
    assert isinstance(descriptor, property)

def test_sql::fullexpression_has_c():
    assert hasattr(sql::FullExpression, "c")
    descriptor = None
    for klass in sql::FullExpression.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_sql::opfunction_is_not_abstract():
    assert not inspect.isabstract(sql::OpFunction)


def test_sql::opfunction_constructor_exists():
    assert callable(sql::OpFunction.__init__)


def test_sql::opfunction_constructor_args():
    sig = inspect.signature(sql::OpFunction.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"

def test_sql::opfunction_has_fname():
    assert hasattr(sql::OpFunction, "fname")
    descriptor = None
    for klass in sql::OpFunction.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)



def test_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrGroupByColumn)


def test_orgroupbycolumn_constructor_exists():
    assert callable(OrGroupByColumn.__init__)


def test_orgroupbycolumn_constructor_args():
    sig = inspect.signature(OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::groupbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql::GroupByColumnFull)


def test_sql::groupbycolumnfull_constructor_exists():
    assert callable(sql::GroupByColumnFull.__init__)


def test_sql::groupbycolumnfull_constructor_args():
    sig = inspect.signature(sql::GroupByColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrOrderByColumn)


def test_ororderbycolumn_constructor_exists():
    assert callable(OrOrderByColumn.__init__)


def test_ororderbycolumn_constructor_args():
    sig = inspect.signature(OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql::OrderByColumnFull)


def test_sql::orderbycolumnfull_constructor_exists():
    assert callable(sql::OrderByColumnFull.__init__)


def test_sql::orderbycolumnfull_constructor_args():
    sig = inspect.signature(sql::OrderByColumnFull.__init__)
    params = list(sig.parameters.keys())
    assert "colOrderInt" in params, "Missing parameter 'colOrderInt'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_sql::orderbycolumnfull_has_colOrderInt():
    assert hasattr(sql::OrderByColumnFull, "colOrderInt")
    descriptor = None
    for klass in sql::OrderByColumnFull.__mro__:
        if "colOrderInt" in klass.__dict__:
            descriptor = klass.__dict__["colOrderInt"]
            break
    assert isinstance(descriptor, property)

def test_sql::orderbycolumnfull_has_direction():
    assert hasattr(sql::OrderByColumnFull, "direction")
    descriptor = None
    for klass in sql::OrderByColumnFull.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_tablefull_is_not_abstract():
    assert not inspect.isabstract(TableFull)


def test_tablefull_constructor_exists():
    assert callable(TableFull.__init__)


def test_tablefull_constructor_args():
    sig = inspect.signature(TableFull.__init__)
    params = list(sig.parameters.keys())



def test_sql::tbls_is_not_abstract():
    assert not inspect.isabstract(sql::tbls)


def test_sql::tbls_constructor_exists():
    assert callable(sql::tbls.__init__)


def test_sql::tbls_constructor_args():
    sig = inspect.signature(sql::tbls.__init__)
    params = list(sig.parameters.keys())



def test_pivotcol_is_not_abstract():
    assert not inspect.isabstract(PivotCol)


def test_pivotcol_constructor_exists():
    assert callable(PivotCol.__init__)


def test_pivotcol_constructor_args():
    sig = inspect.signature(PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_sql::pcols_is_not_abstract():
    assert not inspect.isabstract(sql::pcols)


def test_sql::pcols_constructor_exists():
    assert callable(sql::pcols.__init__)


def test_sql::pcols_constructor_args():
    sig = inspect.signature(sql::pcols.__init__)
    params = list(sig.parameters.keys())



def test_columnfull_is_not_abstract():
    assert not inspect.isabstract(ColumnFull)


def test_columnfull_constructor_exists():
    assert callable(ColumnFull.__init__)


def test_columnfull_constructor_args():
    sig = inspect.signature(ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_sql::col_is_not_abstract():
    assert not inspect.isabstract(sql::Col)


def test_sql::col_constructor_exists():
    assert callable(sql::Col.__init__)


def test_sql::col_constructor_args():
    sig = inspect.signature(sql::Col.__init__)
    params = list(sig.parameters.keys())



def test_pivots_is_not_abstract():
    assert not inspect.isabstract(Pivots)


def test_pivots_constructor_exists():
    assert callable(Pivots.__init__)


def test_pivots_constructor_args():
    sig = inspect.signature(Pivots.__init__)
    params = list(sig.parameters.keys())



def test_sql::pvcs_is_not_abstract():
    assert not inspect.isabstract(sql::pvcs)


def test_sql::pvcs_constructor_exists():
    assert callable(sql::pvcs.__init__)


def test_sql::pvcs_constructor_args():
    sig = inspect.signature(sql::pvcs.__init__)
    params = list(sig.parameters.keys())



def test_pivotfunction_is_not_abstract():
    assert not inspect.isabstract(PivotFunction)


def test_pivotfunction_constructor_exists():
    assert callable(PivotFunction.__init__)


def test_pivotfunction_constructor_args():
    sig = inspect.signature(PivotFunction.__init__)
    params = list(sig.parameters.keys())



def test_pivotcolumns_is_not_abstract():
    assert not inspect.isabstract(PivotColumns)


def test_pivotcolumns_constructor_exists():
    assert callable(PivotColumns.__init__)


def test_pivotcolumns_constructor_args():
    sig = inspect.signature(PivotColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivotcol_is_not_abstract():
    assert not inspect.isabstract(sql::PivotCol)


def test_sql::pivotcol_constructor_exists():
    assert callable(sql::PivotCol.__init__)


def test_sql::pivotcol_constructor_args():
    sig = inspect.signature(sql::PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivots_is_not_abstract():
    assert not inspect.isabstract(sql::Pivots)


def test_sql::pivots_constructor_exists():
    assert callable(sql::Pivots.__init__)


def test_sql::pivots_constructor_args():
    sig = inspect.signature(sql::Pivots.__init__)
    params = list(sig.parameters.keys())



def test_unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClauseArgs)


def test_unpivotinclauseargs_constructor_exists():
    assert callable(UnpivotInClauseArgs.__init__)


def test_unpivotinclauseargs_constructor_args():
    sig = inspect.signature(UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::uicargs_is_not_abstract():
    assert not inspect.isabstract(sql::uicargs)


def test_sql::uicargs_constructor_exists():
    assert callable(sql::uicargs.__init__)


def test_sql::uicargs_constructor_args():
    sig = inspect.signature(sql::uicargs.__init__)
    params = list(sig.parameters.keys())



def test_sql::unpivotinclausearg_is_not_abstract():
    assert not inspect.isabstract(sql::UnpivotInClauseArg)


def test_sql::unpivotinclausearg_constructor_exists():
    assert callable(sql::UnpivotInClauseArg.__init__)


def test_sql::unpivotinclausearg_constructor_args():
    sig = inspect.signature(sql::UnpivotInClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivotfunction_is_not_abstract():
    assert not inspect.isabstract(sql::PivotFunction)


def test_sql::pivotfunction_constructor_exists():
    assert callable(sql::PivotFunction.__init__)


def test_sql::pivotfunction_constructor_args():
    sig = inspect.signature(sql::PivotFunction.__init__)
    params = list(sig.parameters.keys())



def test_sql::unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql::UnpivotInClause)


def test_sql::unpivotinclause_constructor_exists():
    assert callable(sql::UnpivotInClause.__init__)


def test_sql::unpivotinclause_constructor_args():
    sig = inspect.signature(sql::UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivotcolumns_is_not_abstract():
    assert not inspect.isabstract(sql::PivotColumns)


def test_sql::pivotcolumns_constructor_exists():
    assert callable(sql::PivotColumns.__init__)


def test_sql::pivotcolumns_constructor_args():
    sig = inspect.signature(sql::PivotColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql::unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql::UnpivotInClauseArgs)


def test_sql::unpivotinclauseargs_constructor_exists():
    assert callable(sql::UnpivotInClauseArgs.__init__)


def test_sql::unpivotinclauseargs_constructor_args():
    sig = inspect.signature(sql::UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivotfunctions_is_not_abstract():
    assert not inspect.isabstract(sql::PivotFunctions)


def test_sql::pivotfunctions_constructor_exists():
    assert callable(sql::PivotFunctions.__init__)


def test_sql::pivotfunctions_constructor_args():
    sig = inspect.signature(sql::PivotFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "abc" in params, "Missing parameter 'abc'"

def test_sql::pivotfunctions_has_abc():
    assert hasattr(sql::PivotFunctions, "abc")
    descriptor = None
    for klass in sql::PivotFunctions.__mro__:
        if "abc" in klass.__dict__:
            descriptor = klass.__dict__["abc"]
            break
    assert isinstance(descriptor, property)



def test_sql::pivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql::PivotInClause)


def test_sql::pivotinclause_constructor_exists():
    assert callable(sql::PivotInClause.__init__)


def test_sql::pivotinclause_constructor_args():
    sig = inspect.signature(sql::PivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "pinany" in params, "Missing parameter 'pinany'"

def test_sql::pivotinclause_has_pinany():
    assert hasattr(sql::PivotInClause, "pinany")
    descriptor = None
    for klass in sql::PivotInClause.__mro__:
        if "pinany" in klass.__dict__:
            descriptor = klass.__dict__["pinany"]
            break
    assert isinstance(descriptor, property)



def test_sql::pivotforclause_is_not_abstract():
    assert not inspect.isabstract(sql::PivotForClause)


def test_sql::pivotforclause_constructor_exists():
    assert callable(sql::PivotForClause.__init__)


def test_sql::pivotforclause_constructor_args():
    sig = inspect.signature(sql::PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::fromtablejoin_is_not_abstract():
    assert not inspect.isabstract(sql::FromTableJoin)


def test_sql::fromtablejoin_constructor_exists():
    assert callable(sql::FromTableJoin.__init__)


def test_sql::fromtablejoin_constructor_args():
    sig = inspect.signature(sql::FromTableJoin.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"

def test_sql::fromtablejoin_has_join():
    assert hasattr(sql::FromTableJoin, "join")
    descriptor = None
    for klass in sql::FromTableJoin.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)



def test_sql::unpivottable_is_not_abstract():
    assert not inspect.isabstract(sql::UnpivotTable)


def test_sql::unpivottable_constructor_exists():
    assert callable(sql::UnpivotTable.__init__)


def test_sql::unpivottable_constructor_args():
    sig = inspect.signature(sql::UnpivotTable.__init__)
    params = list(sig.parameters.keys())



def test_sql::pivottable_is_not_abstract():
    assert not inspect.isabstract(sql::PivotTable)


def test_sql::pivottable_constructor_exists():
    assert callable(sql::PivotTable.__init__)


def test_sql::pivottable_constructor_args():
    sig = inspect.signature(sql::PivotTable.__init__)
    params = list(sig.parameters.keys())



def test_sql::subqueryoperand_is_not_abstract():
    assert not inspect.isabstract(sql::SubQueryOperand)


def test_sql::subqueryoperand_constructor_exists():
    assert callable(sql::SubQueryOperand.__init__)


def test_sql::subqueryoperand_constructor_args():
    sig = inspect.signature(sql::SubQueryOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql::tablefull_is_not_abstract():
    assert not inspect.isabstract(sql::TableFull)


def test_sql::tablefull_constructor_exists():
    assert callable(sql::TableFull.__init__)


def test_sql::tablefull_constructor_args():
    sig = inspect.signature(sql::TableFull.__init__)
    params = list(sig.parameters.keys())



def test_sql::dbobjectnameall_is_not_abstract():
    assert not inspect.isabstract(sql::DbObjectNameAll)


def test_sql::dbobjectnameall_constructor_exists():
    assert callable(sql::DbObjectNameAll.__init__)


def test_sql::dbobjectnameall_constructor_args():
    sig = inspect.signature(sql::DbObjectNameAll.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"

def test_sql::dbobjectnameall_has_dbname():
    assert hasattr(sql::DbObjectNameAll, "dbname")
    descriptor = None
    for klass in sql::DbObjectNameAll.__mro__:
        if "dbname" in klass.__dict__:
            descriptor = klass.__dict__["dbname"]
            break
    assert isinstance(descriptor, property)



def test_sql::dbobjectname_is_not_abstract():
    assert not inspect.isabstract(sql::DbObjectName)


def test_sql::dbobjectname_constructor_exists():
    assert callable(sql::DbObjectName.__init__)


def test_sql::dbobjectname_constructor_args():
    sig = inspect.signature(sql::DbObjectName.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"

def test_sql::dbobjectname_has_dbname():
    assert hasattr(sql::DbObjectName, "dbname")
    descriptor = None
    for klass in sql::DbObjectName.__mro__:
        if "dbname" in klass.__dict__:
            descriptor = klass.__dict__["dbname"]
            break
    assert isinstance(descriptor, property)



def test_sql::tableoralias_is_not_abstract():
    assert not inspect.isabstract(sql::TableOrAlias)


def test_sql::tableoralias_constructor_exists():
    assert callable(sql::TableOrAlias.__init__)


def test_sql::tableoralias_constructor_args():
    sig = inspect.signature(sql::TableOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql::tableoralias_has_alias():
    assert hasattr(sql::TableOrAlias, "alias")
    descriptor = None
    for klass in sql::TableOrAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_ortable_is_not_abstract():
    assert not inspect.isabstract(OrTable)


def test_ortable_constructor_exists():
    assert callable(OrTable.__init__)


def test_ortable_constructor_args():
    sig = inspect.signature(OrTable.__init__)
    params = list(sig.parameters.keys())



def test_sql::fromtable_is_not_abstract():
    assert not inspect.isabstract(sql::FromTable)


def test_sql::fromtable_constructor_exists():
    assert callable(sql::FromTable.__init__)


def test_sql::fromtable_constructor_args():
    sig = inspect.signature(sql::FromTable.__init__)
    params = list(sig.parameters.keys())



def test_sql::operands_is_not_abstract():
    assert not inspect.isabstract(sql::Operands)


def test_sql::operands_constructor_exists():
    assert callable(sql::Operands.__init__)


def test_sql::operands_constructor_args():
    sig = inspect.signature(sql::Operands.__init__)
    params = list(sig.parameters.keys())



def test_orcolumn_is_not_abstract():
    assert not inspect.isabstract(OrColumn)


def test_orcolumn_constructor_exists():
    assert callable(OrColumn.__init__)


def test_orcolumn_constructor_args():
    sig = inspect.signature(OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::columnoralias_is_not_abstract():
    assert not inspect.isabstract(sql::ColumnOrAlias)


def test_sql::columnoralias_constructor_exists():
    assert callable(sql::ColumnOrAlias.__init__)


def test_sql::columnoralias_constructor_args():
    sig = inspect.signature(sql::ColumnOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "allCols" in params, "Missing parameter 'allCols'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql::columnoralias_has_allCols():
    assert hasattr(sql::ColumnOrAlias, "allCols")
    descriptor = None
    for klass in sql::ColumnOrAlias.__mro__:
        if "allCols" in klass.__dict__:
            descriptor = klass.__dict__["allCols"]
            break
    assert isinstance(descriptor, property)

def test_sql::columnoralias_has_alias():
    assert hasattr(sql::ColumnOrAlias, "alias")
    descriptor = None
    for klass in sql::ColumnOrAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_pivotforclause_is_not_abstract():
    assert not inspect.isabstract(PivotForClause)


def test_pivotforclause_constructor_exists():
    assert callable(PivotForClause.__init__)


def test_pivotforclause_constructor_args():
    sig = inspect.signature(PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_sql::columnfull_is_not_abstract():
    assert not inspect.isabstract(sql::ColumnFull)


def test_sql::columnfull_constructor_exists():
    assert callable(sql::ColumnFull.__init__)


def test_sql::columnfull_constructor_args():
    sig = inspect.signature(sql::ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_sql::orexpr_is_not_abstract():
    assert not inspect.isabstract(sql::OrExpr)


def test_sql::orexpr_constructor_exists():
    assert callable(sql::OrExpr.__init__)


def test_sql::orexpr_constructor_args():
    sig = inspect.signature(sql::OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_sql::ortable_is_not_abstract():
    assert not inspect.isabstract(sql::OrTable)


def test_sql::ortable_constructor_exists():
    assert callable(sql::OrTable.__init__)


def test_sql::ortable_constructor_args():
    sig = inspect.signature(sql::OrTable.__init__)
    params = list(sig.parameters.keys())



def test_sql::orcolumn_is_not_abstract():
    assert not inspect.isabstract(sql::OrColumn)


def test_sql::orcolumn_constructor_exists():
    assert callable(sql::OrColumn.__init__)


def test_sql::orcolumn_constructor_args():
    sig = inspect.signature(sql::OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql::OrOrderByColumn)


def test_sql::ororderbycolumn_constructor_exists():
    assert callable(sql::OrOrderByColumn.__init__)


def test_sql::ororderbycolumn_constructor_args():
    sig = inspect.signature(sql::OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql::OrGroupByColumn)


def test_sql::orgroupbycolumn_constructor_exists():
    assert callable(sql::OrGroupByColumn.__init__)


def test_sql::orgroupbycolumn_constructor_args():
    sig = inspect.signature(sql::OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql::limit_is_not_abstract():
    assert not inspect.isabstract(sql::Limit)


def test_sql::limit_constructor_exists():
    assert callable(sql::Limit.__init__)


def test_sql::limit_constructor_args():
    sig = inspect.signature(sql::Limit.__init__)
    params = list(sig.parameters.keys())
    assert "l1" in params, "Missing parameter 'l1'"

def test_sql::limit_has_l1():
    assert hasattr(sql::Limit, "l1")
    descriptor = None
    for klass in sql::Limit.__mro__:
        if "l1" in klass.__dict__:
            descriptor = klass.__dict__["l1"]
            break
    assert isinstance(descriptor, property)



def test_sql::offset_is_not_abstract():
    assert not inspect.isabstract(sql::Offset)


def test_sql::offset_constructor_exists():
    assert callable(sql::Offset.__init__)


def test_sql::offset_constructor_args():
    sig = inspect.signature(sql::Offset.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"

def test_sql::offset_has_offset():
    assert hasattr(sql::Offset, "offset")
    descriptor = None
    for klass in sql::Offset.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_selectquery_is_not_abstract():
    assert not inspect.isabstract(SelectQuery)


def test_selectquery_constructor_exists():
    assert callable(SelectQuery.__init__)


def test_selectquery_constructor_args():
    sig = inspect.signature(SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql::select_is_not_abstract():
    assert not inspect.isabstract(sql::Select)


def test_sql::select_constructor_exists():
    assert callable(sql::Select.__init__)


def test_sql::select_constructor_args():
    sig = inspect.signature(sql::Select.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_sql::select_has_select():
    assert hasattr(sql::Select, "select")
    descriptor = None
    for klass in sql::Select.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_sql::selectsubset_is_not_abstract():
    assert not inspect.isabstract(sql::SelectSubSet)


def test_sql::selectsubset_constructor_exists():
    assert callable(sql::SelectSubSet.__init__)


def test_sql::selectsubset_constructor_args():
    sig = inspect.signature(sql::SelectSubSet.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "all" in params, "Missing parameter 'all'"

def test_sql::selectsubset_has_op():
    assert hasattr(sql::SelectSubSet, "op")
    descriptor = None
    for klass in sql::SelectSubSet.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_sql::selectsubset_has_all():
    assert hasattr(sql::SelectSubSet, "all")
    descriptor = None
    for klass in sql::SelectSubSet.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sql::model_is_not_abstract():
    assert not inspect.isabstract(sql::Model)


def test_sql::model_constructor_exists():
    assert callable(sql::Model.__init__)


def test_sql::model_constructor_args():
    sig = inspect.signature(sql::Model.__init__)
    params = list(sig.parameters.keys())



def test_sql::integervalue_is_not_abstract():
    assert not inspect.isabstract(sql::IntegerValue)


def test_sql::integervalue_constructor_exists():
    assert callable(sql::IntegerValue.__init__)


def test_sql::integervalue_constructor_args():
    sig = inspect.signature(sql::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"

def test_sql::integervalue_has_integer():
    assert hasattr(sql::IntegerValue, "integer")
    descriptor = None
    for klass in sql::IntegerValue.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_sql::fetchfirst_is_not_abstract():
    assert not inspect.isabstract(sql::FetchFirst)


def test_sql::fetchfirst_constructor_exists():
    assert callable(sql::FetchFirst.__init__)


def test_sql::fetchfirst_constructor_args():
    sig = inspect.signature(sql::FetchFirst.__init__)
    params = list(sig.parameters.keys())
    assert "row" in params, "Missing parameter 'row'"

def test_sql::fetchfirst_has_row():
    assert hasattr(sql::FetchFirst, "row")
    descriptor = None
    for klass in sql::FetchFirst.__mro__:
        if "row" in klass.__dict__:
            descriptor = klass.__dict__["row"]
            break
    assert isinstance(descriptor, property)



def test_sql::selectquery_is_not_abstract():
    assert not inspect.isabstract(sql::SelectQuery)


def test_sql::selectquery_constructor_exists():
    assert callable(sql::SelectQuery.__init__)


def test_sql::selectquery_constructor_args():
    sig = inspect.signature(sql::SelectQuery.__init__)
    params = list(sig.parameters.keys())

def test_xfunction_exists():
    # Check that the Enumeration exists
    assert XFunction is not None

def test_xfunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XFunction]
    expected_literals = [
        "xbwnl",
        "xeq",
        "xnotin",
        "xgtl",
        "xbwn",
        "xbwnr",
        "xnoteq",
        "xin",
        "xls",
        "xgt",
        "xbwnc",
        "xlsr",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XFunction"

def test_extract_values_exists():
    # Check that the Enumeration exists
    assert EXTRACT_VALUES is not None

def test_extract_values_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EXTRACT_VALUES]
    expected_literals = [
        "ms",
        "dms",
        "h",
        "dayh",
        "m",
        "hmin",
        "yearMonth",
        "minSec",
        "ds",
        "day",
        "s",
        "quart",
        "hs",
        "hms",
        "month",
        "daymin",
        "year",
        "micros",
        "week",
        "minMicro",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EXTRACT_VALUES"


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
Operands_strategy = st.builds(
    Operands,
)
sql::Concat_strategy = st.builds(
    sql::Concat,
)
sql::Div_strategy = st.builds(
    sql::Div,
)
sql::Star_strategy = st.builds(
    sql::Star,
)
sql::Minus_strategy = st.builds(
    sql::Minus,
)
sql::Plus_strategy = st.builds(
    sql::Plus,
)
UnpivotInClause_strategy = st.builds(
    UnpivotInClause,
)
sql::UnipivotInClause_strategy = st.builds(
    sql::UnipivotInClause,
    op=
        safe_text
)
SQLCaseWhens_strategy = st.builds(
    SQLCaseWhens,
)
sql::WhenList_strategy = st.builds(
    sql::WhenList,
)
sql::SqlCaseWhen_strategy = st.builds(
    sql::SqlCaseWhen,
)
sql::SQLCaseWhens_strategy = st.builds(
    sql::SQLCaseWhens,
)
OperandList_strategy = st.builds(
    OperandList,
)
sql::OpList_strategy = st.builds(
    sql::OpList,
)
AnalyticExprArgs_strategy = st.builds(
    AnalyticExprArgs,
)
sql::AExpArgs_strategy = st.builds(
    sql::AExpArgs,
)
sql::OpFunctionArgAgregate_strategy = st.builds(
    sql::OpFunctionArgAgregate,
)
OpFunctionArg_strategy = st.builds(
    OpFunctionArg,
)
sql::OpFList_strategy = st.builds(
    sql::OpFList,
)
sql::OpFunctionArgOperand_strategy = st.builds(
    sql::OpFunctionArgOperand,
)
OrderByClauseArgs_strategy = st.builds(
    OrderByClauseArgs,
)
sql::OBCArgs_strategy = st.builds(
    sql::OBCArgs,
)
sql::OrderByClauseArg_strategy = st.builds(
    sql::OrderByClauseArg,
)
sql::OrderByClauseArgs_strategy = st.builds(
    sql::OrderByClauseArgs,
)
QueryPartitionClause_strategy = st.builds(
    QueryPartitionClause,
)
sql::AnalyticExprArgs_strategy = st.builds(
    sql::AnalyticExprArgs,
)
sql::WindowingClauseOperandFollowing_strategy = st.builds(
    sql::WindowingClauseOperandFollowing,
)
sql::AnalyticExprArg_strategy = st.builds(
    sql::AnalyticExprArg,
)
sql::QueryPartitionClause_strategy = st.builds(
    sql::QueryPartitionClause,
)
sql::AnalyticClause_strategy = st.builds(
    sql::AnalyticClause,
)
WindowingClause_strategy = st.builds(
    WindowingClause,
)
sql::WindowingClauseOperandPreceding_strategy = st.builds(
    sql::WindowingClauseOperandPreceding,
)
sql::WindowingClauseBetween_strategy = st.builds(
    sql::WindowingClauseBetween,
)
sql::WindowingClause_strategy = st.builds(
    sql::WindowingClause,
)
sql::OrderByClause_strategy = st.builds(
    sql::OrderByClause,
)
sql::ScalarOperand_strategy = st.builds(
    sql::ScalarOperand,
    sodate=
        st.dates(),
    soint=
        st.integers(),
    sotime=
        st.dates(),
    sodbl=
        safe_text,
    sostr=
        safe_text,
    sodt=
        st.dates()
)
sql::ExpOperand_strategy = st.builds(
    sql::ExpOperand,
    prm=
        safe_text
)
sql::FunctionAnalytical_strategy = st.builds(
    sql::FunctionAnalytical,
)
sql::OpFunctionArg_strategy = st.builds(
    sql::OpFunctionArg,
)
sql::ColumnOperand_strategy = st.builds(
    sql::ColumnOperand,
    ora=
        safe_text
)
sql::SQLCaseOperand_strategy = st.builds(
    sql::SQLCaseOperand,
)
sql::FunctionExtract_strategy = st.builds(
    sql::FunctionExtract,
    v=
        safe_text
)
OpFunctionArgAgregate_strategy = st.builds(
    OpFunctionArgAgregate,
)
sql::OperandList_strategy = st.builds(
    sql::OperandList,
)
sql::Operand_strategy = st.builds(
    sql::Operand,
)
sql::OperandListGroup_strategy = st.builds(
    sql::OperandListGroup,
)
sql::LikeOperand_strategy = st.builds(
    sql::LikeOperand,
    op2=
        safe_text
)
sql::POperand_strategy = st.builds(
    sql::POperand,
    prm=
        safe_text
)
sql::OpFunctionCast_strategy = st.builds(
    sql::OpFunctionCast,
    p=
        st.integers(),
    p2=
        st.integers(),
    type=
        safe_text
)
sql::Prms_strategy = st.builds(
    sql::Prms,
)
Prms_strategy = st.builds(
    Prms,
)
sql::JRParameter_strategy = st.builds(
    sql::JRParameter,
    jrprm=
        safe_text
)
sql::Comparison_strategy = st.builds(
    sql::Comparison,
    subOperator=
        safe_text,
    operator=
        safe_text
)
sql::Like_strategy = st.builds(
    sql::Like,
    opLike=
        safe_text
)
sql::ExistsOper_strategy = st.builds(
    sql::ExistsOper,
    op=
        safe_text
)
sql::InOper_strategy = st.builds(
    sql::InOper,
    op=
        safe_text
)
sql::XExpr_strategy = st.builds(
    sql::XExpr,
    xf=
        safe_text
)
sql::ExprGroup_strategy = st.builds(
    sql::ExprGroup,
    isnot=
        safe_text
)
sql::Between_strategy = st.builds(
    sql::Between,
    opBetween=
        safe_text
)
OrExpr_strategy = st.builds(
    OrExpr,
)
sql::FullExpression_strategy = st.builds(
    sql::FullExpression,
    notPrm=
        safe_text,
    isnull=
        safe_text,
    c=
        safe_text
)
sql::OpFunction_strategy = st.builds(
    sql::OpFunction,
    fname=
        safe_text
)
OrGroupByColumn_strategy = st.builds(
    OrGroupByColumn,
)
sql::GroupByColumnFull_strategy = st.builds(
    sql::GroupByColumnFull,
)
OrOrderByColumn_strategy = st.builds(
    OrOrderByColumn,
)
sql::OrderByColumnFull_strategy = st.builds(
    sql::OrderByColumnFull,
    colOrderInt=
        st.integers(),
    direction=
        safe_text
)
TableFull_strategy = st.builds(
    TableFull,
)
sql::tbls_strategy = st.builds(
    sql::tbls,
)
PivotCol_strategy = st.builds(
    PivotCol,
)
sql::pcols_strategy = st.builds(
    sql::pcols,
)
ColumnFull_strategy = st.builds(
    ColumnFull,
)
sql::Col_strategy = st.builds(
    sql::Col,
)
Pivots_strategy = st.builds(
    Pivots,
)
sql::pvcs_strategy = st.builds(
    sql::pvcs,
)
PivotFunction_strategy = st.builds(
    PivotFunction,
)
PivotColumns_strategy = st.builds(
    PivotColumns,
)
sql::PivotCol_strategy = st.builds(
    sql::PivotCol,
)
sql::Pivots_strategy = st.builds(
    sql::Pivots,
)
UnpivotInClauseArgs_strategy = st.builds(
    UnpivotInClauseArgs,
)
sql::uicargs_strategy = st.builds(
    sql::uicargs,
)
sql::UnpivotInClauseArg_strategy = st.builds(
    sql::UnpivotInClauseArg,
)
sql::PivotFunction_strategy = st.builds(
    sql::PivotFunction,
)
sql::UnpivotInClause_strategy = st.builds(
    sql::UnpivotInClause,
)
sql::PivotColumns_strategy = st.builds(
    sql::PivotColumns,
)
sql::UnpivotInClauseArgs_strategy = st.builds(
    sql::UnpivotInClauseArgs,
)
sql::PivotFunctions_strategy = st.builds(
    sql::PivotFunctions,
    abc=
        safe_text
)
sql::PivotInClause_strategy = st.builds(
    sql::PivotInClause,
    pinany=
        safe_text
)
sql::PivotForClause_strategy = st.builds(
    sql::PivotForClause,
)
sql::FromTableJoin_strategy = st.builds(
    sql::FromTableJoin,
    join=
        safe_text
)
sql::UnpivotTable_strategy = st.builds(
    sql::UnpivotTable,
)
sql::PivotTable_strategy = st.builds(
    sql::PivotTable,
)
sql::SubQueryOperand_strategy = st.builds(
    sql::SubQueryOperand,
)
sql::TableFull_strategy = st.builds(
    sql::TableFull,
)
sql::DbObjectNameAll_strategy = st.builds(
    sql::DbObjectNameAll,
    dbname=
        safe_text
)
sql::DbObjectName_strategy = st.builds(
    sql::DbObjectName,
    dbname=
        safe_text
)
sql::TableOrAlias_strategy = st.builds(
    sql::TableOrAlias,
    alias=
        safe_text
)
OrTable_strategy = st.builds(
    OrTable,
)
sql::FromTable_strategy = st.builds(
    sql::FromTable,
)
sql::Operands_strategy = st.builds(
    sql::Operands,
)
OrColumn_strategy = st.builds(
    OrColumn,
)
sql::ColumnOrAlias_strategy = st.builds(
    sql::ColumnOrAlias,
    allCols=
        safe_text,
    alias=
        safe_text
)
PivotForClause_strategy = st.builds(
    PivotForClause,
)
sql::ColumnFull_strategy = st.builds(
    sql::ColumnFull,
)
sql::OrExpr_strategy = st.builds(
    sql::OrExpr,
)
sql::OrTable_strategy = st.builds(
    sql::OrTable,
)
sql::OrColumn_strategy = st.builds(
    sql::OrColumn,
)
sql::OrOrderByColumn_strategy = st.builds(
    sql::OrOrderByColumn,
)
sql::OrGroupByColumn_strategy = st.builds(
    sql::OrGroupByColumn,
)
sql::Limit_strategy = st.builds(
    sql::Limit,
    l1=
        st.integers()
)
sql::Offset_strategy = st.builds(
    sql::Offset,
    offset=
        st.integers()
)
SelectQuery_strategy = st.builds(
    SelectQuery,
)
sql::Select_strategy = st.builds(
    sql::Select,
    select=
        safe_text
)
sql::SelectSubSet_strategy = st.builds(
    sql::SelectSubSet,
    op=
        safe_text,
    all=
        safe_text
)
sql::Model_strategy = st.builds(
    sql::Model,
)
sql::IntegerValue_strategy = st.builds(
    sql::IntegerValue,
    integer=
        st.integers()
)
sql::FetchFirst_strategy = st.builds(
    sql::FetchFirst,
    row=
        safe_text
)
sql::SelectQuery_strategy = st.builds(
    sql::SelectQuery,
)

@given(instance=Operands_strategy)
@settings(max_examples=50)
def test_operands_instantiation(instance):
    assert isinstance(instance, Operands)

@given(instance=sql::Concat_strategy)
@settings(max_examples=50)
def test_sql::concat_instantiation(instance):
    assert isinstance(instance, sql::Concat)

@given(instance=sql::Div_strategy)
@settings(max_examples=50)
def test_sql::div_instantiation(instance):
    assert isinstance(instance, sql::Div)

@given(instance=sql::Star_strategy)
@settings(max_examples=50)
def test_sql::star_instantiation(instance):
    assert isinstance(instance, sql::Star)

@given(instance=sql::Minus_strategy)
@settings(max_examples=50)
def test_sql::minus_instantiation(instance):
    assert isinstance(instance, sql::Minus)

@given(instance=sql::Plus_strategy)
@settings(max_examples=50)
def test_sql::plus_instantiation(instance):
    assert isinstance(instance, sql::Plus)

@given(instance=UnpivotInClause_strategy)
@settings(max_examples=50)
def test_unpivotinclause_instantiation(instance):
    assert isinstance(instance, UnpivotInClause)

@given(instance=sql::UnipivotInClause_strategy)
@settings(max_examples=50)
def test_sql::unipivotinclause_instantiation(instance):
    assert isinstance(instance, sql::UnipivotInClause)

@given(instance=sql::UnipivotInClause_strategy)
def test_sql::unipivotinclause_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sql::UnipivotInClause_strategy)
def test_sql::unipivotinclause_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=SQLCaseWhens_strategy)
@settings(max_examples=50)
def test_sqlcasewhens_instantiation(instance):
    assert isinstance(instance, SQLCaseWhens)

@given(instance=sql::WhenList_strategy)
@settings(max_examples=50)
def test_sql::whenlist_instantiation(instance):
    assert isinstance(instance, sql::WhenList)

@given(instance=sql::SqlCaseWhen_strategy)
@settings(max_examples=50)
def test_sql::sqlcasewhen_instantiation(instance):
    assert isinstance(instance, sql::SqlCaseWhen)

@given(instance=sql::SQLCaseWhens_strategy)
@settings(max_examples=50)
def test_sql::sqlcasewhens_instantiation(instance):
    assert isinstance(instance, sql::SQLCaseWhens)

@given(instance=OperandList_strategy)
@settings(max_examples=50)
def test_operandlist_instantiation(instance):
    assert isinstance(instance, OperandList)

@given(instance=sql::OpList_strategy)
@settings(max_examples=50)
def test_sql::oplist_instantiation(instance):
    assert isinstance(instance, sql::OpList)

@given(instance=AnalyticExprArgs_strategy)
@settings(max_examples=50)
def test_analyticexprargs_instantiation(instance):
    assert isinstance(instance, AnalyticExprArgs)

@given(instance=sql::AExpArgs_strategy)
@settings(max_examples=50)
def test_sql::aexpargs_instantiation(instance):
    assert isinstance(instance, sql::AExpArgs)

@given(instance=sql::OpFunctionArgAgregate_strategy)
@settings(max_examples=50)
def test_sql::opfunctionargagregate_instantiation(instance):
    assert isinstance(instance, sql::OpFunctionArgAgregate)

@given(instance=OpFunctionArg_strategy)
@settings(max_examples=50)
def test_opfunctionarg_instantiation(instance):
    assert isinstance(instance, OpFunctionArg)

@given(instance=sql::OpFList_strategy)
@settings(max_examples=50)
def test_sql::opflist_instantiation(instance):
    assert isinstance(instance, sql::OpFList)

@given(instance=sql::OpFunctionArgOperand_strategy)
@settings(max_examples=50)
def test_sql::opfunctionargoperand_instantiation(instance):
    assert isinstance(instance, sql::OpFunctionArgOperand)

@given(instance=OrderByClauseArgs_strategy)
@settings(max_examples=50)
def test_orderbyclauseargs_instantiation(instance):
    assert isinstance(instance, OrderByClauseArgs)

@given(instance=sql::OBCArgs_strategy)
@settings(max_examples=50)
def test_sql::obcargs_instantiation(instance):
    assert isinstance(instance, sql::OBCArgs)

@given(instance=sql::OrderByClauseArg_strategy)
@settings(max_examples=50)
def test_sql::orderbyclausearg_instantiation(instance):
    assert isinstance(instance, sql::OrderByClauseArg)

@given(instance=sql::OrderByClauseArgs_strategy)
@settings(max_examples=50)
def test_sql::orderbyclauseargs_instantiation(instance):
    assert isinstance(instance, sql::OrderByClauseArgs)

@given(instance=QueryPartitionClause_strategy)
@settings(max_examples=50)
def test_querypartitionclause_instantiation(instance):
    assert isinstance(instance, QueryPartitionClause)

@given(instance=sql::AnalyticExprArgs_strategy)
@settings(max_examples=50)
def test_sql::analyticexprargs_instantiation(instance):
    assert isinstance(instance, sql::AnalyticExprArgs)

@given(instance=sql::WindowingClauseOperandFollowing_strategy)
@settings(max_examples=50)
def test_sql::windowingclauseoperandfollowing_instantiation(instance):
    assert isinstance(instance, sql::WindowingClauseOperandFollowing)

@given(instance=sql::AnalyticExprArg_strategy)
@settings(max_examples=50)
def test_sql::analyticexprarg_instantiation(instance):
    assert isinstance(instance, sql::AnalyticExprArg)

@given(instance=sql::QueryPartitionClause_strategy)
@settings(max_examples=50)
def test_sql::querypartitionclause_instantiation(instance):
    assert isinstance(instance, sql::QueryPartitionClause)

@given(instance=sql::AnalyticClause_strategy)
@settings(max_examples=50)
def test_sql::analyticclause_instantiation(instance):
    assert isinstance(instance, sql::AnalyticClause)

@given(instance=WindowingClause_strategy)
@settings(max_examples=50)
def test_windowingclause_instantiation(instance):
    assert isinstance(instance, WindowingClause)

@given(instance=sql::WindowingClauseOperandPreceding_strategy)
@settings(max_examples=50)
def test_sql::windowingclauseoperandpreceding_instantiation(instance):
    assert isinstance(instance, sql::WindowingClauseOperandPreceding)

@given(instance=sql::WindowingClauseBetween_strategy)
@settings(max_examples=50)
def test_sql::windowingclausebetween_instantiation(instance):
    assert isinstance(instance, sql::WindowingClauseBetween)

@given(instance=sql::WindowingClause_strategy)
@settings(max_examples=50)
def test_sql::windowingclause_instantiation(instance):
    assert isinstance(instance, sql::WindowingClause)

@given(instance=sql::OrderByClause_strategy)
@settings(max_examples=50)
def test_sql::orderbyclause_instantiation(instance):
    assert isinstance(instance, sql::OrderByClause)

@given(instance=sql::ScalarOperand_strategy)
@settings(max_examples=50)
def test_sql::scalaroperand_instantiation(instance):
    assert isinstance(instance, sql::ScalarOperand)

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodate_type(instance):
    assert isinstance(instance.sodate, date)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodate_setter(instance):
    original = instance.sodate
    instance.sodate = original
    assert instance.sodate == original

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_soint_type(instance):
    assert isinstance(instance.soint, int)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_soint_setter(instance):
    original = instance.soint
    instance.soint = original
    assert instance.soint == original

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sotime_type(instance):
    assert isinstance(instance.sotime, date)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sotime_setter(instance):
    original = instance.sotime
    instance.sotime = original
    assert instance.sotime == original

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodbl_type(instance):
    assert isinstance(instance.sodbl, str)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodbl_setter(instance):
    original = instance.sodbl
    instance.sodbl = original
    assert instance.sodbl == original

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sostr_type(instance):
    assert isinstance(instance.sostr, str)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sostr_setter(instance):
    original = instance.sostr
    instance.sostr = original
    assert instance.sostr == original

@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodt_type(instance):
    assert isinstance(instance.sodt, date)


@given(instance=sql::ScalarOperand_strategy)
def test_sql::scalaroperand_sodt_setter(instance):
    original = instance.sodt
    instance.sodt = original
    assert instance.sodt == original

@given(instance=sql::ExpOperand_strategy)
@settings(max_examples=50)
def test_sql::expoperand_instantiation(instance):
    assert isinstance(instance, sql::ExpOperand)

@given(instance=sql::ExpOperand_strategy)
def test_sql::expoperand_prm_type(instance):
    assert isinstance(instance.prm, str)


@given(instance=sql::ExpOperand_strategy)
def test_sql::expoperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql::FunctionAnalytical_strategy)
@settings(max_examples=50)
def test_sql::functionanalytical_instantiation(instance):
    assert isinstance(instance, sql::FunctionAnalytical)

@given(instance=sql::OpFunctionArg_strategy)
@settings(max_examples=50)
def test_sql::opfunctionarg_instantiation(instance):
    assert isinstance(instance, sql::OpFunctionArg)

@given(instance=sql::ColumnOperand_strategy)
@settings(max_examples=50)
def test_sql::columnoperand_instantiation(instance):
    assert isinstance(instance, sql::ColumnOperand)

@given(instance=sql::ColumnOperand_strategy)
def test_sql::columnoperand_ora_type(instance):
    assert isinstance(instance.ora, str)


@given(instance=sql::ColumnOperand_strategy)
def test_sql::columnoperand_ora_setter(instance):
    original = instance.ora
    instance.ora = original
    assert instance.ora == original

@given(instance=sql::SQLCaseOperand_strategy)
@settings(max_examples=50)
def test_sql::sqlcaseoperand_instantiation(instance):
    assert isinstance(instance, sql::SQLCaseOperand)

@given(instance=sql::FunctionExtract_strategy)
@settings(max_examples=50)
def test_sql::functionextract_instantiation(instance):
    assert isinstance(instance, sql::FunctionExtract)

@given(instance=sql::FunctionExtract_strategy)
def test_sql::functionextract_v_type(instance):
    assert isinstance(instance.v, str)


@given(instance=sql::FunctionExtract_strategy)
def test_sql::functionextract_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=OpFunctionArgAgregate_strategy)
@settings(max_examples=50)
def test_opfunctionargagregate_instantiation(instance):
    assert isinstance(instance, OpFunctionArgAgregate)

@given(instance=sql::OperandList_strategy)
@settings(max_examples=50)
def test_sql::operandlist_instantiation(instance):
    assert isinstance(instance, sql::OperandList)

@given(instance=sql::Operand_strategy)
@settings(max_examples=50)
def test_sql::operand_instantiation(instance):
    assert isinstance(instance, sql::Operand)

@given(instance=sql::OperandListGroup_strategy)
@settings(max_examples=50)
def test_sql::operandlistgroup_instantiation(instance):
    assert isinstance(instance, sql::OperandListGroup)

@given(instance=sql::LikeOperand_strategy)
@settings(max_examples=50)
def test_sql::likeoperand_instantiation(instance):
    assert isinstance(instance, sql::LikeOperand)

@given(instance=sql::LikeOperand_strategy)
def test_sql::likeoperand_op2_type(instance):
    assert isinstance(instance.op2, str)


@given(instance=sql::LikeOperand_strategy)
def test_sql::likeoperand_op2_setter(instance):
    original = instance.op2
    instance.op2 = original
    assert instance.op2 == original

@given(instance=sql::POperand_strategy)
@settings(max_examples=50)
def test_sql::poperand_instantiation(instance):
    assert isinstance(instance, sql::POperand)

@given(instance=sql::POperand_strategy)
def test_sql::poperand_prm_type(instance):
    assert isinstance(instance.prm, str)


@given(instance=sql::POperand_strategy)
def test_sql::poperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql::OpFunctionCast_strategy)
@settings(max_examples=50)
def test_sql::opfunctioncast_instantiation(instance):
    assert isinstance(instance, sql::OpFunctionCast)

@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_p_type(instance):
    assert isinstance(instance.p, int)


@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_p2_type(instance):
    assert isinstance(instance.p2, int)


@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original

@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=sql::OpFunctionCast_strategy)
def test_sql::opfunctioncast_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql::Prms_strategy)
@settings(max_examples=50)
def test_sql::prms_instantiation(instance):
    assert isinstance(instance, sql::Prms)

@given(instance=Prms_strategy)
@settings(max_examples=50)
def test_prms_instantiation(instance):
    assert isinstance(instance, Prms)

@given(instance=sql::JRParameter_strategy)
@settings(max_examples=50)
def test_sql::jrparameter_instantiation(instance):
    assert isinstance(instance, sql::JRParameter)

@given(instance=sql::JRParameter_strategy)
def test_sql::jrparameter_jrprm_type(instance):
    assert isinstance(instance.jrprm, str)


@given(instance=sql::JRParameter_strategy)
def test_sql::jrparameter_jrprm_setter(instance):
    original = instance.jrprm
    instance.jrprm = original
    assert instance.jrprm == original

@given(instance=sql::Comparison_strategy)
@settings(max_examples=50)
def test_sql::comparison_instantiation(instance):
    assert isinstance(instance, sql::Comparison)

@given(instance=sql::Comparison_strategy)
def test_sql::comparison_subOperator_type(instance):
    assert isinstance(instance.subOperator, str)


@given(instance=sql::Comparison_strategy)
def test_sql::comparison_subOperator_setter(instance):
    original = instance.subOperator
    instance.subOperator = original
    assert instance.subOperator == original

@given(instance=sql::Comparison_strategy)
def test_sql::comparison_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=sql::Comparison_strategy)
def test_sql::comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sql::Like_strategy)
@settings(max_examples=50)
def test_sql::like_instantiation(instance):
    assert isinstance(instance, sql::Like)

@given(instance=sql::Like_strategy)
def test_sql::like_opLike_type(instance):
    assert isinstance(instance.opLike, str)


@given(instance=sql::Like_strategy)
def test_sql::like_opLike_setter(instance):
    original = instance.opLike
    instance.opLike = original
    assert instance.opLike == original

@given(instance=sql::ExistsOper_strategy)
@settings(max_examples=50)
def test_sql::existsoper_instantiation(instance):
    assert isinstance(instance, sql::ExistsOper)

@given(instance=sql::ExistsOper_strategy)
def test_sql::existsoper_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sql::ExistsOper_strategy)
def test_sql::existsoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql::InOper_strategy)
@settings(max_examples=50)
def test_sql::inoper_instantiation(instance):
    assert isinstance(instance, sql::InOper)

@given(instance=sql::InOper_strategy)
def test_sql::inoper_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sql::InOper_strategy)
def test_sql::inoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql::XExpr_strategy)
@settings(max_examples=50)
def test_sql::xexpr_instantiation(instance):
    assert isinstance(instance, sql::XExpr)

@given(instance=sql::XExpr_strategy)
def test_sql::xexpr_xf_type(instance):
    assert isinstance(instance.xf, str)


@given(instance=sql::XExpr_strategy)
def test_sql::xexpr_xf_setter(instance):
    original = instance.xf
    instance.xf = original
    assert instance.xf == original

@given(instance=sql::ExprGroup_strategy)
@settings(max_examples=50)
def test_sql::exprgroup_instantiation(instance):
    assert isinstance(instance, sql::ExprGroup)

@given(instance=sql::ExprGroup_strategy)
def test_sql::exprgroup_isnot_type(instance):
    assert isinstance(instance.isnot, str)


@given(instance=sql::ExprGroup_strategy)
def test_sql::exprgroup_isnot_setter(instance):
    original = instance.isnot
    instance.isnot = original
    assert instance.isnot == original

@given(instance=sql::Between_strategy)
@settings(max_examples=50)
def test_sql::between_instantiation(instance):
    assert isinstance(instance, sql::Between)

@given(instance=sql::Between_strategy)
def test_sql::between_opBetween_type(instance):
    assert isinstance(instance.opBetween, str)


@given(instance=sql::Between_strategy)
def test_sql::between_opBetween_setter(instance):
    original = instance.opBetween
    instance.opBetween = original
    assert instance.opBetween == original

@given(instance=OrExpr_strategy)
@settings(max_examples=50)
def test_orexpr_instantiation(instance):
    assert isinstance(instance, OrExpr)

@given(instance=sql::FullExpression_strategy)
@settings(max_examples=50)
def test_sql::fullexpression_instantiation(instance):
    assert isinstance(instance, sql::FullExpression)

@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_notPrm_type(instance):
    assert isinstance(instance.notPrm, str)


@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_notPrm_setter(instance):
    original = instance.notPrm
    instance.notPrm = original
    assert instance.notPrm == original

@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_isnull_type(instance):
    assert isinstance(instance.isnull, str)


@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_isnull_setter(instance):
    original = instance.isnull
    instance.isnull = original
    assert instance.isnull == original

@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=sql::FullExpression_strategy)
def test_sql::fullexpression_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=sql::OpFunction_strategy)
@settings(max_examples=50)
def test_sql::opfunction_instantiation(instance):
    assert isinstance(instance, sql::OpFunction)

@given(instance=sql::OpFunction_strategy)
def test_sql::opfunction_fname_type(instance):
    assert isinstance(instance.fname, str)


@given(instance=sql::OpFunction_strategy)
def test_sql::opfunction_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original

@given(instance=OrGroupByColumn_strategy)
@settings(max_examples=50)
def test_orgroupbycolumn_instantiation(instance):
    assert isinstance(instance, OrGroupByColumn)

@given(instance=sql::GroupByColumnFull_strategy)
@settings(max_examples=50)
def test_sql::groupbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql::GroupByColumnFull)

@given(instance=OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_ororderbycolumn_instantiation(instance):
    assert isinstance(instance, OrOrderByColumn)

@given(instance=sql::OrderByColumnFull_strategy)
@settings(max_examples=50)
def test_sql::orderbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql::OrderByColumnFull)

@given(instance=sql::OrderByColumnFull_strategy)
def test_sql::orderbycolumnfull_colOrderInt_type(instance):
    assert isinstance(instance.colOrderInt, int)


@given(instance=sql::OrderByColumnFull_strategy)
def test_sql::orderbycolumnfull_colOrderInt_setter(instance):
    original = instance.colOrderInt
    instance.colOrderInt = original
    assert instance.colOrderInt == original

@given(instance=sql::OrderByColumnFull_strategy)
def test_sql::orderbycolumnfull_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=sql::OrderByColumnFull_strategy)
def test_sql::orderbycolumnfull_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=TableFull_strategy)
@settings(max_examples=50)
def test_tablefull_instantiation(instance):
    assert isinstance(instance, TableFull)

@given(instance=sql::tbls_strategy)
@settings(max_examples=50)
def test_sql::tbls_instantiation(instance):
    assert isinstance(instance, sql::tbls)

@given(instance=PivotCol_strategy)
@settings(max_examples=50)
def test_pivotcol_instantiation(instance):
    assert isinstance(instance, PivotCol)

@given(instance=sql::pcols_strategy)
@settings(max_examples=50)
def test_sql::pcols_instantiation(instance):
    assert isinstance(instance, sql::pcols)

@given(instance=ColumnFull_strategy)
@settings(max_examples=50)
def test_columnfull_instantiation(instance):
    assert isinstance(instance, ColumnFull)

@given(instance=sql::Col_strategy)
@settings(max_examples=50)
def test_sql::col_instantiation(instance):
    assert isinstance(instance, sql::Col)

@given(instance=Pivots_strategy)
@settings(max_examples=50)
def test_pivots_instantiation(instance):
    assert isinstance(instance, Pivots)

@given(instance=sql::pvcs_strategy)
@settings(max_examples=50)
def test_sql::pvcs_instantiation(instance):
    assert isinstance(instance, sql::pvcs)

@given(instance=PivotFunction_strategy)
@settings(max_examples=50)
def test_pivotfunction_instantiation(instance):
    assert isinstance(instance, PivotFunction)

@given(instance=PivotColumns_strategy)
@settings(max_examples=50)
def test_pivotcolumns_instantiation(instance):
    assert isinstance(instance, PivotColumns)

@given(instance=sql::PivotCol_strategy)
@settings(max_examples=50)
def test_sql::pivotcol_instantiation(instance):
    assert isinstance(instance, sql::PivotCol)

@given(instance=sql::Pivots_strategy)
@settings(max_examples=50)
def test_sql::pivots_instantiation(instance):
    assert isinstance(instance, sql::Pivots)

@given(instance=UnpivotInClauseArgs_strategy)
@settings(max_examples=50)
def test_unpivotinclauseargs_instantiation(instance):
    assert isinstance(instance, UnpivotInClauseArgs)

@given(instance=sql::uicargs_strategy)
@settings(max_examples=50)
def test_sql::uicargs_instantiation(instance):
    assert isinstance(instance, sql::uicargs)

@given(instance=sql::UnpivotInClauseArg_strategy)
@settings(max_examples=50)
def test_sql::unpivotinclausearg_instantiation(instance):
    assert isinstance(instance, sql::UnpivotInClauseArg)

@given(instance=sql::PivotFunction_strategy)
@settings(max_examples=50)
def test_sql::pivotfunction_instantiation(instance):
    assert isinstance(instance, sql::PivotFunction)

@given(instance=sql::UnpivotInClause_strategy)
@settings(max_examples=50)
def test_sql::unpivotinclause_instantiation(instance):
    assert isinstance(instance, sql::UnpivotInClause)

@given(instance=sql::PivotColumns_strategy)
@settings(max_examples=50)
def test_sql::pivotcolumns_instantiation(instance):
    assert isinstance(instance, sql::PivotColumns)

@given(instance=sql::UnpivotInClauseArgs_strategy)
@settings(max_examples=50)
def test_sql::unpivotinclauseargs_instantiation(instance):
    assert isinstance(instance, sql::UnpivotInClauseArgs)

@given(instance=sql::PivotFunctions_strategy)
@settings(max_examples=50)
def test_sql::pivotfunctions_instantiation(instance):
    assert isinstance(instance, sql::PivotFunctions)

@given(instance=sql::PivotFunctions_strategy)
def test_sql::pivotfunctions_abc_type(instance):
    assert isinstance(instance.abc, str)


@given(instance=sql::PivotFunctions_strategy)
def test_sql::pivotfunctions_abc_setter(instance):
    original = instance.abc
    instance.abc = original
    assert instance.abc == original

@given(instance=sql::PivotInClause_strategy)
@settings(max_examples=50)
def test_sql::pivotinclause_instantiation(instance):
    assert isinstance(instance, sql::PivotInClause)

@given(instance=sql::PivotInClause_strategy)
def test_sql::pivotinclause_pinany_type(instance):
    assert isinstance(instance.pinany, str)


@given(instance=sql::PivotInClause_strategy)
def test_sql::pivotinclause_pinany_setter(instance):
    original = instance.pinany
    instance.pinany = original
    assert instance.pinany == original

@given(instance=sql::PivotForClause_strategy)
@settings(max_examples=50)
def test_sql::pivotforclause_instantiation(instance):
    assert isinstance(instance, sql::PivotForClause)

@given(instance=sql::FromTableJoin_strategy)
@settings(max_examples=50)
def test_sql::fromtablejoin_instantiation(instance):
    assert isinstance(instance, sql::FromTableJoin)

@given(instance=sql::FromTableJoin_strategy)
def test_sql::fromtablejoin_join_type(instance):
    assert isinstance(instance.join, str)


@given(instance=sql::FromTableJoin_strategy)
def test_sql::fromtablejoin_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=sql::UnpivotTable_strategy)
@settings(max_examples=50)
def test_sql::unpivottable_instantiation(instance):
    assert isinstance(instance, sql::UnpivotTable)

@given(instance=sql::PivotTable_strategy)
@settings(max_examples=50)
def test_sql::pivottable_instantiation(instance):
    assert isinstance(instance, sql::PivotTable)

@given(instance=sql::SubQueryOperand_strategy)
@settings(max_examples=50)
def test_sql::subqueryoperand_instantiation(instance):
    assert isinstance(instance, sql::SubQueryOperand)

@given(instance=sql::TableFull_strategy)
@settings(max_examples=50)
def test_sql::tablefull_instantiation(instance):
    assert isinstance(instance, sql::TableFull)

@given(instance=sql::DbObjectNameAll_strategy)
@settings(max_examples=50)
def test_sql::dbobjectnameall_instantiation(instance):
    assert isinstance(instance, sql::DbObjectNameAll)

@given(instance=sql::DbObjectNameAll_strategy)
def test_sql::dbobjectnameall_dbname_type(instance):
    assert isinstance(instance.dbname, str)


@given(instance=sql::DbObjectNameAll_strategy)
def test_sql::dbobjectnameall_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original

@given(instance=sql::DbObjectName_strategy)
@settings(max_examples=50)
def test_sql::dbobjectname_instantiation(instance):
    assert isinstance(instance, sql::DbObjectName)

@given(instance=sql::DbObjectName_strategy)
def test_sql::dbobjectname_dbname_type(instance):
    assert isinstance(instance.dbname, str)


@given(instance=sql::DbObjectName_strategy)
def test_sql::dbobjectname_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original

@given(instance=sql::TableOrAlias_strategy)
@settings(max_examples=50)
def test_sql::tableoralias_instantiation(instance):
    assert isinstance(instance, sql::TableOrAlias)

@given(instance=sql::TableOrAlias_strategy)
def test_sql::tableoralias_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sql::TableOrAlias_strategy)
def test_sql::tableoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=OrTable_strategy)
@settings(max_examples=50)
def test_ortable_instantiation(instance):
    assert isinstance(instance, OrTable)

@given(instance=sql::FromTable_strategy)
@settings(max_examples=50)
def test_sql::fromtable_instantiation(instance):
    assert isinstance(instance, sql::FromTable)

@given(instance=sql::Operands_strategy)
@settings(max_examples=50)
def test_sql::operands_instantiation(instance):
    assert isinstance(instance, sql::Operands)

@given(instance=OrColumn_strategy)
@settings(max_examples=50)
def test_orcolumn_instantiation(instance):
    assert isinstance(instance, OrColumn)

@given(instance=sql::ColumnOrAlias_strategy)
@settings(max_examples=50)
def test_sql::columnoralias_instantiation(instance):
    assert isinstance(instance, sql::ColumnOrAlias)

@given(instance=sql::ColumnOrAlias_strategy)
def test_sql::columnoralias_allCols_type(instance):
    assert isinstance(instance.allCols, str)


@given(instance=sql::ColumnOrAlias_strategy)
def test_sql::columnoralias_allCols_setter(instance):
    original = instance.allCols
    instance.allCols = original
    assert instance.allCols == original

@given(instance=sql::ColumnOrAlias_strategy)
def test_sql::columnoralias_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sql::ColumnOrAlias_strategy)
def test_sql::columnoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=PivotForClause_strategy)
@settings(max_examples=50)
def test_pivotforclause_instantiation(instance):
    assert isinstance(instance, PivotForClause)

@given(instance=sql::ColumnFull_strategy)
@settings(max_examples=50)
def test_sql::columnfull_instantiation(instance):
    assert isinstance(instance, sql::ColumnFull)

@given(instance=sql::OrExpr_strategy)
@settings(max_examples=50)
def test_sql::orexpr_instantiation(instance):
    assert isinstance(instance, sql::OrExpr)

@given(instance=sql::OrTable_strategy)
@settings(max_examples=50)
def test_sql::ortable_instantiation(instance):
    assert isinstance(instance, sql::OrTable)

@given(instance=sql::OrColumn_strategy)
@settings(max_examples=50)
def test_sql::orcolumn_instantiation(instance):
    assert isinstance(instance, sql::OrColumn)

@given(instance=sql::OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_sql::ororderbycolumn_instantiation(instance):
    assert isinstance(instance, sql::OrOrderByColumn)

@given(instance=sql::OrGroupByColumn_strategy)
@settings(max_examples=50)
def test_sql::orgroupbycolumn_instantiation(instance):
    assert isinstance(instance, sql::OrGroupByColumn)

@given(instance=sql::Limit_strategy)
@settings(max_examples=50)
def test_sql::limit_instantiation(instance):
    assert isinstance(instance, sql::Limit)

@given(instance=sql::Limit_strategy)
def test_sql::limit_l1_type(instance):
    assert isinstance(instance.l1, int)


@given(instance=sql::Limit_strategy)
def test_sql::limit_l1_setter(instance):
    original = instance.l1
    instance.l1 = original
    assert instance.l1 == original

@given(instance=sql::Offset_strategy)
@settings(max_examples=50)
def test_sql::offset_instantiation(instance):
    assert isinstance(instance, sql::Offset)

@given(instance=sql::Offset_strategy)
def test_sql::offset_offset_type(instance):
    assert isinstance(instance.offset, int)


@given(instance=sql::Offset_strategy)
def test_sql::offset_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=SelectQuery_strategy)
@settings(max_examples=50)
def test_selectquery_instantiation(instance):
    assert isinstance(instance, SelectQuery)

@given(instance=sql::Select_strategy)
@settings(max_examples=50)
def test_sql::select_instantiation(instance):
    assert isinstance(instance, sql::Select)

@given(instance=sql::Select_strategy)
def test_sql::select_select_type(instance):
    assert isinstance(instance.select, str)


@given(instance=sql::Select_strategy)
def test_sql::select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=sql::SelectSubSet_strategy)
@settings(max_examples=50)
def test_sql::selectsubset_instantiation(instance):
    assert isinstance(instance, sql::SelectSubSet)

@given(instance=sql::SelectSubSet_strategy)
def test_sql::selectsubset_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sql::SelectSubSet_strategy)
def test_sql::selectsubset_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql::SelectSubSet_strategy)
def test_sql::selectsubset_all_type(instance):
    assert isinstance(instance.all, str)


@given(instance=sql::SelectSubSet_strategy)
def test_sql::selectsubset_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sql::Model_strategy)
@settings(max_examples=50)
def test_sql::model_instantiation(instance):
    assert isinstance(instance, sql::Model)

@given(instance=sql::IntegerValue_strategy)
@settings(max_examples=50)
def test_sql::integervalue_instantiation(instance):
    assert isinstance(instance, sql::IntegerValue)

@given(instance=sql::IntegerValue_strategy)
def test_sql::integervalue_integer_type(instance):
    assert isinstance(instance.integer, int)


@given(instance=sql::IntegerValue_strategy)
def test_sql::integervalue_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=sql::FetchFirst_strategy)
@settings(max_examples=50)
def test_sql::fetchfirst_instantiation(instance):
    assert isinstance(instance, sql::FetchFirst)

@given(instance=sql::FetchFirst_strategy)
def test_sql::fetchfirst_row_type(instance):
    assert isinstance(instance.row, str)


@given(instance=sql::FetchFirst_strategy)
def test_sql::fetchfirst_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original

@given(instance=sql::SelectQuery_strategy)
@settings(max_examples=50)
def test_sql::selectquery_instantiation(instance):
    assert isinstance(instance, sql::SelectQuery)
