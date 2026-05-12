import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Operands,
    sql_Multiply,
    sql_Division,
    sql_Minus,
    sql_Concat,
    sql_Plus,
    UnpivotInClause,
    sql_UnipivotInClause,
    sql_IntegerValue,
    sql_OpFunctionArgAgregate,
    OpFunctionArg,
    sql_OpFList,
    sql_OpFunctionArgOperand,
    SQLCaseWhens,
    sql_WhenList,
    sql_SqlCaseWhen,
    sql_SQLCaseWhens,
    OperandList,
    sql_OpList,
    RowValue,
    sql_OrderByClause,
    sql_QueryPartitionClause,
    sql_AnalyticClause,
    sql_FunctionAnalytical,
    sql_OpFunctionArg,
    AnalyticExprArgs,
    sql_AExpArgs,
    QueryPartitionClause,
    sql_AnalyticExprArgs,
    OrderByClauseArgs,
    sql_OBCArgs,
    sql_OrderByClauseArg,
    sql_OrderByClauseArgs,
    sql_AnalyticExprArg,
    sql_WindowingClauseOperandFollowing,
    WindowingClause,
    sql_WindowingClauseOperandPreceding,
    sql_WindowingClauseBetween,
    sql_WindowingClause,
    sql_Operand,
    OpFunctionArgAgregate,
    sql_OperandList,
    sql_ScalarOperand,
    sql_ExpOperand,
    sql_SQLCaseOperand,
    sql_FunctionExtract,
    sql_ColumnOperand,
    Prms,
    sql_JRParameter,
    sql_OperandListGroup,
    sql_POperand,
    sql_OpFunctionCast,
    sql_LikeOperand,
    OrExpr,
    sql_FullExpression,
    sql_OpFunction,
    OrGroupByColumn,
    sql_Prms,
    sql_Comparison,
    sql_Like,
    sql_Between,
    sql_ExistsOper,
    sql_InOper,
    sql_XExpr,
    sql_ExprGroup,
    sql_UnpivotInClauseArgs,
    sql_PivotFunction,
    sql_PivotInClause,
    sql_PivotForClause,
    sql_GroupByColumnFull,
    OrOrderByColumn,
    sql_OrderByColumnFull,
    TableFull,
    sql_tbls,
    PivotCol,
    sql_pcols,
    UsingCols,
    ColumnFull,
    sql_Col,
    Pivots,
    sql_pvcs,
    PivotFunction,
    PivotColumns,
    sql_PivotCol,
    sql_Pivots,
    UnpivotInClauseArgs,
    sql_uicargs,
    sql_UnpivotInClauseArg,
    sql_UnpivotInClause,
    sql_PivotColumns,
    sql_UnpivotTable,
    sql_PivotTable,
    sql_FromValues,
    sql_SubQueryOperand,
    sql_TableFull,
    WithColumns,
    sql_UsingCols,
    sql_JoinCondition,
    sql_PivotFunctions,
    RowValues,
    sql_RowValue,
    sql_RowValues,
    Rows,
    sql_Row,
    sql_Rows,
    FromValuesColumnNames,
    sql_abc,
    sql_ColumnNames,
    sql_FromValuesColumnNames,
    sql_FromValuesColumns,
    sql_Values,
    sql_OrOrderByColumn,
    sql_OrGroupByColumn,
    sql_OrExpr,
    sql_OrTable,
    sql_FromTableJoin,
    sql_TableOrAlias,
    OrTable,
    sql_FromTable,
    sql_DbObjectNameAll,
    sql_DbObjectName,
    sql_Operands,
    OrColumn,
    sql_ColumnOrAlias,
    PivotForClause,
    sql_ColumnFull,
    sql_OrColumn,
    sql_Model,
    SelectQuery,
    sql_Select,
    sql_SelectSubSet,
    sql_Limit,
    sql_Offset,
    sql_UnsignedValue,
    sql_FetchFirst,
    sql_WithColumns,
    sql_SelectQuery,
    sql_WithQuery,
    EXTRACT_VALUES,
    XFunction,
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



def test_sql_multiply_is_not_abstract():
    assert not inspect.isabstract(sql_Multiply)


def test_sql_multiply_constructor_exists():
    assert callable(sql_Multiply.__init__)


def test_sql_multiply_constructor_args():
    sig = inspect.signature(sql_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_sql_division_is_not_abstract():
    assert not inspect.isabstract(sql_Division)


def test_sql_division_constructor_exists():
    assert callable(sql_Division.__init__)


def test_sql_division_constructor_args():
    sig = inspect.signature(sql_Division.__init__)
    params = list(sig.parameters.keys())



def test_sql_minus_is_not_abstract():
    assert not inspect.isabstract(sql_Minus)


def test_sql_minus_constructor_exists():
    assert callable(sql_Minus.__init__)


def test_sql_minus_constructor_args():
    sig = inspect.signature(sql_Minus.__init__)
    params = list(sig.parameters.keys())



def test_sql_concat_is_not_abstract():
    assert not inspect.isabstract(sql_Concat)


def test_sql_concat_constructor_exists():
    assert callable(sql_Concat.__init__)


def test_sql_concat_constructor_args():
    sig = inspect.signature(sql_Concat.__init__)
    params = list(sig.parameters.keys())



def test_sql_plus_is_not_abstract():
    assert not inspect.isabstract(sql_Plus)


def test_sql_plus_constructor_exists():
    assert callable(sql_Plus.__init__)


def test_sql_plus_constructor_args():
    sig = inspect.signature(sql_Plus.__init__)
    params = list(sig.parameters.keys())



def test_unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClause)


def test_unpivotinclause_constructor_exists():
    assert callable(UnpivotInClause.__init__)


def test_unpivotinclause_constructor_args():
    sig = inspect.signature(UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_unipivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_UnipivotInClause)


def test_sql_unipivotinclause_constructor_exists():
    assert callable(sql_UnipivotInClause.__init__)


def test_sql_unipivotinclause_constructor_args():
    sig = inspect.signature(sql_UnipivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql_unipivotinclause_has_op():
    assert hasattr(sql_UnipivotInClause, "op")
    descriptor = None
    for klass in sql_UnipivotInClause.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sql_integervalue_is_not_abstract():
    assert not inspect.isabstract(sql_IntegerValue)


def test_sql_integervalue_constructor_exists():
    assert callable(sql_IntegerValue.__init__)


def test_sql_integervalue_constructor_args():
    sig = inspect.signature(sql_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"

def test_sql_integervalue_has_integer():
    assert hasattr(sql_IntegerValue, "integer")
    descriptor = None
    for klass in sql_IntegerValue.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_sql_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArgAgregate)


def test_sql_opfunctionargagregate_constructor_exists():
    assert callable(sql_OpFunctionArgAgregate.__init__)


def test_sql_opfunctionargagregate_constructor_args():
    sig = inspect.signature(sql_OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArg)


def test_opfunctionarg_constructor_exists():
    assert callable(OpFunctionArg.__init__)


def test_opfunctionarg_constructor_args():
    sig = inspect.signature(OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_sql_opflist_is_not_abstract():
    assert not inspect.isabstract(sql_OpFList)


def test_sql_opflist_constructor_exists():
    assert callable(sql_OpFList.__init__)


def test_sql_opflist_constructor_args():
    sig = inspect.signature(sql_OpFList.__init__)
    params = list(sig.parameters.keys())



def test_sql_opfunctionargoperand_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArgOperand)


def test_sql_opfunctionargoperand_constructor_exists():
    assert callable(sql_OpFunctionArgOperand.__init__)


def test_sql_opfunctionargoperand_constructor_args():
    sig = inspect.signature(sql_OpFunctionArgOperand.__init__)
    params = list(sig.parameters.keys())



def test_sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(SQLCaseWhens)


def test_sqlcasewhens_constructor_exists():
    assert callable(SQLCaseWhens.__init__)


def test_sqlcasewhens_constructor_args():
    sig = inspect.signature(SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_sql_whenlist_is_not_abstract():
    assert not inspect.isabstract(sql_WhenList)


def test_sql_whenlist_constructor_exists():
    assert callable(sql_WhenList.__init__)


def test_sql_whenlist_constructor_args():
    sig = inspect.signature(sql_WhenList.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqlcasewhen_is_not_abstract():
    assert not inspect.isabstract(sql_SqlCaseWhen)


def test_sql_sqlcasewhen_constructor_exists():
    assert callable(sql_SqlCaseWhen.__init__)


def test_sql_sqlcasewhen_constructor_args():
    sig = inspect.signature(sql_SqlCaseWhen.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqlcasewhens_is_not_abstract():
    assert not inspect.isabstract(sql_SQLCaseWhens)


def test_sql_sqlcasewhens_constructor_exists():
    assert callable(sql_SQLCaseWhens.__init__)


def test_sql_sqlcasewhens_constructor_args():
    sig = inspect.signature(sql_SQLCaseWhens.__init__)
    params = list(sig.parameters.keys())



def test_operandlist_is_not_abstract():
    assert not inspect.isabstract(OperandList)


def test_operandlist_constructor_exists():
    assert callable(OperandList.__init__)


def test_operandlist_constructor_args():
    sig = inspect.signature(OperandList.__init__)
    params = list(sig.parameters.keys())



def test_sql_oplist_is_not_abstract():
    assert not inspect.isabstract(sql_OpList)


def test_sql_oplist_constructor_exists():
    assert callable(sql_OpList.__init__)


def test_sql_oplist_constructor_args():
    sig = inspect.signature(sql_OpList.__init__)
    params = list(sig.parameters.keys())



def test_rowvalue_is_not_abstract():
    assert not inspect.isabstract(RowValue)


def test_rowvalue_constructor_exists():
    assert callable(RowValue.__init__)


def test_rowvalue_constructor_args():
    sig = inspect.signature(RowValue.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderbyclause_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClause)


def test_sql_orderbyclause_constructor_exists():
    assert callable(sql_OrderByClause.__init__)


def test_sql_orderbyclause_constructor_args():
    sig = inspect.signature(sql_OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(sql_QueryPartitionClause)


def test_sql_querypartitionclause_constructor_exists():
    assert callable(sql_QueryPartitionClause.__init__)


def test_sql_querypartitionclause_constructor_args():
    sig = inspect.signature(sql_QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_analyticclause_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticClause)


def test_sql_analyticclause_constructor_exists():
    assert callable(sql_AnalyticClause.__init__)


def test_sql_analyticclause_constructor_args():
    sig = inspect.signature(sql_AnalyticClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_functionanalytical_is_not_abstract():
    assert not inspect.isabstract(sql_FunctionAnalytical)


def test_sql_functionanalytical_constructor_exists():
    assert callable(sql_FunctionAnalytical.__init__)


def test_sql_functionanalytical_constructor_args():
    sig = inspect.signature(sql_FunctionAnalytical.__init__)
    params = list(sig.parameters.keys())



def test_sql_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArg)


def test_sql_opfunctionarg_constructor_exists():
    assert callable(sql_OpFunctionArg.__init__)


def test_sql_opfunctionarg_constructor_args():
    sig = inspect.signature(sql_OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(AnalyticExprArgs)


def test_analyticexprargs_constructor_exists():
    assert callable(AnalyticExprArgs.__init__)


def test_analyticexprargs_constructor_args():
    sig = inspect.signature(AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_aexpargs_is_not_abstract():
    assert not inspect.isabstract(sql_AExpArgs)


def test_sql_aexpargs_constructor_exists():
    assert callable(sql_AExpArgs.__init__)


def test_sql_aexpargs_constructor_args():
    sig = inspect.signature(sql_AExpArgs.__init__)
    params = list(sig.parameters.keys())



def test_querypartitionclause_is_not_abstract():
    assert not inspect.isabstract(QueryPartitionClause)


def test_querypartitionclause_constructor_exists():
    assert callable(QueryPartitionClause.__init__)


def test_querypartitionclause_constructor_args():
    sig = inspect.signature(QueryPartitionClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_analyticexprargs_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticExprArgs)


def test_sql_analyticexprargs_constructor_exists():
    assert callable(sql_AnalyticExprArgs.__init__)


def test_sql_analyticexprargs_constructor_args():
    sig = inspect.signature(sql_AnalyticExprArgs.__init__)
    params = list(sig.parameters.keys())



def test_orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(OrderByClauseArgs)


def test_orderbyclauseargs_constructor_exists():
    assert callable(OrderByClauseArgs.__init__)


def test_orderbyclauseargs_constructor_args():
    sig = inspect.signature(OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_obcargs_is_not_abstract():
    assert not inspect.isabstract(sql_OBCArgs)


def test_sql_obcargs_constructor_exists():
    assert callable(sql_OBCArgs.__init__)


def test_sql_obcargs_constructor_args():
    sig = inspect.signature(sql_OBCArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderbyclausearg_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClauseArg)


def test_sql_orderbyclausearg_constructor_exists():
    assert callable(sql_OrderByClauseArg.__init__)


def test_sql_orderbyclausearg_constructor_args():
    sig = inspect.signature(sql_OrderByClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderbyclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByClauseArgs)


def test_sql_orderbyclauseargs_constructor_exists():
    assert callable(sql_OrderByClauseArgs.__init__)


def test_sql_orderbyclauseargs_constructor_args():
    sig = inspect.signature(sql_OrderByClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_analyticexprarg_is_not_abstract():
    assert not inspect.isabstract(sql_AnalyticExprArg)


def test_sql_analyticexprarg_constructor_exists():
    assert callable(sql_AnalyticExprArg.__init__)


def test_sql_analyticexprarg_constructor_args():
    sig = inspect.signature(sql_AnalyticExprArg.__init__)
    params = list(sig.parameters.keys())



def test_sql_windowingclauseoperandfollowing_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseOperandFollowing)


def test_sql_windowingclauseoperandfollowing_constructor_exists():
    assert callable(sql_WindowingClauseOperandFollowing.__init__)


def test_sql_windowingclauseoperandfollowing_constructor_args():
    sig = inspect.signature(sql_WindowingClauseOperandFollowing.__init__)
    params = list(sig.parameters.keys())



def test_windowingclause_is_not_abstract():
    assert not inspect.isabstract(WindowingClause)


def test_windowingclause_constructor_exists():
    assert callable(WindowingClause.__init__)


def test_windowingclause_constructor_args():
    sig = inspect.signature(WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_windowingclauseoperandpreceding_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseOperandPreceding)


def test_sql_windowingclauseoperandpreceding_constructor_exists():
    assert callable(sql_WindowingClauseOperandPreceding.__init__)


def test_sql_windowingclauseoperandpreceding_constructor_args():
    sig = inspect.signature(sql_WindowingClauseOperandPreceding.__init__)
    params = list(sig.parameters.keys())



def test_sql_windowingclausebetween_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClauseBetween)


def test_sql_windowingclausebetween_constructor_exists():
    assert callable(sql_WindowingClauseBetween.__init__)


def test_sql_windowingclausebetween_constructor_args():
    sig = inspect.signature(sql_WindowingClauseBetween.__init__)
    params = list(sig.parameters.keys())



def test_sql_windowingclause_is_not_abstract():
    assert not inspect.isabstract(sql_WindowingClause)


def test_sql_windowingclause_constructor_exists():
    assert callable(sql_WindowingClause.__init__)


def test_sql_windowingclause_constructor_args():
    sig = inspect.signature(sql_WindowingClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_operand_is_not_abstract():
    assert not inspect.isabstract(sql_Operand)


def test_sql_operand_constructor_exists():
    assert callable(sql_Operand.__init__)


def test_sql_operand_constructor_args():
    sig = inspect.signature(sql_Operand.__init__)
    params = list(sig.parameters.keys())



def test_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArgAgregate)


def test_opfunctionargagregate_constructor_exists():
    assert callable(OpFunctionArgAgregate.__init__)


def test_opfunctionargagregate_constructor_args():
    sig = inspect.signature(OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_sql_operandlist_is_not_abstract():
    assert not inspect.isabstract(sql_OperandList)


def test_sql_operandlist_constructor_exists():
    assert callable(sql_OperandList.__init__)


def test_sql_operandlist_constructor_args():
    sig = inspect.signature(sql_OperandList.__init__)
    params = list(sig.parameters.keys())



def test_sql_scalaroperand_is_not_abstract():
    assert not inspect.isabstract(sql_ScalarOperand)


def test_sql_scalaroperand_constructor_exists():
    assert callable(sql_ScalarOperand.__init__)


def test_sql_scalaroperand_constructor_args():
    sig = inspect.signature(sql_ScalarOperand.__init__)
    params = list(sig.parameters.keys())
    assert "sodate" in params, "Missing parameter 'sodate'"
    assert "sostr" in params, "Missing parameter 'sostr'"
    assert "sotime" in params, "Missing parameter 'sotime'"
    assert "soUInt" in params, "Missing parameter 'soUInt'"
    assert "sodbl" in params, "Missing parameter 'sodbl'"
    assert "soint" in params, "Missing parameter 'soint'"
    assert "sodt" in params, "Missing parameter 'sodt'"

def test_sql_scalaroperand_has_sodate():
    assert hasattr(sql_ScalarOperand, "sodate")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sodate" in klass.__dict__:
            descriptor = klass.__dict__["sodate"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_sostr():
    assert hasattr(sql_ScalarOperand, "sostr")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sostr" in klass.__dict__:
            descriptor = klass.__dict__["sostr"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_sotime():
    assert hasattr(sql_ScalarOperand, "sotime")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sotime" in klass.__dict__:
            descriptor = klass.__dict__["sotime"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_soUInt():
    assert hasattr(sql_ScalarOperand, "soUInt")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "soUInt" in klass.__dict__:
            descriptor = klass.__dict__["soUInt"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_sodbl():
    assert hasattr(sql_ScalarOperand, "sodbl")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sodbl" in klass.__dict__:
            descriptor = klass.__dict__["sodbl"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_soint():
    assert hasattr(sql_ScalarOperand, "soint")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "soint" in klass.__dict__:
            descriptor = klass.__dict__["soint"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_sodt():
    assert hasattr(sql_ScalarOperand, "sodt")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sodt" in klass.__dict__:
            descriptor = klass.__dict__["sodt"]
            break
    assert isinstance(descriptor, property)



def test_sql_expoperand_is_not_abstract():
    assert not inspect.isabstract(sql_ExpOperand)


def test_sql_expoperand_constructor_exists():
    assert callable(sql_ExpOperand.__init__)


def test_sql_expoperand_constructor_args():
    sig = inspect.signature(sql_ExpOperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"

def test_sql_expoperand_has_prm():
    assert hasattr(sql_ExpOperand, "prm")
    descriptor = None
    for klass in sql_ExpOperand.__mro__:
        if "prm" in klass.__dict__:
            descriptor = klass.__dict__["prm"]
            break
    assert isinstance(descriptor, property)



def test_sql_sqlcaseoperand_is_not_abstract():
    assert not inspect.isabstract(sql_SQLCaseOperand)


def test_sql_sqlcaseoperand_constructor_exists():
    assert callable(sql_SQLCaseOperand.__init__)


def test_sql_sqlcaseoperand_constructor_args():
    sig = inspect.signature(sql_SQLCaseOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql_functionextract_is_not_abstract():
    assert not inspect.isabstract(sql_FunctionExtract)


def test_sql_functionextract_constructor_exists():
    assert callable(sql_FunctionExtract.__init__)


def test_sql_functionextract_constructor_args():
    sig = inspect.signature(sql_FunctionExtract.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"

def test_sql_functionextract_has_v():
    assert hasattr(sql_FunctionExtract, "v")
    descriptor = None
    for klass in sql_FunctionExtract.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)



def test_sql_columnoperand_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnOperand)


def test_sql_columnoperand_constructor_exists():
    assert callable(sql_ColumnOperand.__init__)


def test_sql_columnoperand_constructor_args():
    sig = inspect.signature(sql_ColumnOperand.__init__)
    params = list(sig.parameters.keys())
    assert "ora" in params, "Missing parameter 'ora'"

def test_sql_columnoperand_has_ora():
    assert hasattr(sql_ColumnOperand, "ora")
    descriptor = None
    for klass in sql_ColumnOperand.__mro__:
        if "ora" in klass.__dict__:
            descriptor = klass.__dict__["ora"]
            break
    assert isinstance(descriptor, property)



def test_prms_is_not_abstract():
    assert not inspect.isabstract(Prms)


def test_prms_constructor_exists():
    assert callable(Prms.__init__)


def test_prms_constructor_args():
    sig = inspect.signature(Prms.__init__)
    params = list(sig.parameters.keys())



def test_sql_jrparameter_is_not_abstract():
    assert not inspect.isabstract(sql_JRParameter)


def test_sql_jrparameter_constructor_exists():
    assert callable(sql_JRParameter.__init__)


def test_sql_jrparameter_constructor_args():
    sig = inspect.signature(sql_JRParameter.__init__)
    params = list(sig.parameters.keys())
    assert "jrprm" in params, "Missing parameter 'jrprm'"

def test_sql_jrparameter_has_jrprm():
    assert hasattr(sql_JRParameter, "jrprm")
    descriptor = None
    for klass in sql_JRParameter.__mro__:
        if "jrprm" in klass.__dict__:
            descriptor = klass.__dict__["jrprm"]
            break
    assert isinstance(descriptor, property)



def test_sql_operandlistgroup_is_not_abstract():
    assert not inspect.isabstract(sql_OperandListGroup)


def test_sql_operandlistgroup_constructor_exists():
    assert callable(sql_OperandListGroup.__init__)


def test_sql_operandlistgroup_constructor_args():
    sig = inspect.signature(sql_OperandListGroup.__init__)
    params = list(sig.parameters.keys())



def test_sql_poperand_is_not_abstract():
    assert not inspect.isabstract(sql_POperand)


def test_sql_poperand_constructor_exists():
    assert callable(sql_POperand.__init__)


def test_sql_poperand_constructor_args():
    sig = inspect.signature(sql_POperand.__init__)
    params = list(sig.parameters.keys())
    assert "prm" in params, "Missing parameter 'prm'"

def test_sql_poperand_has_prm():
    assert hasattr(sql_POperand, "prm")
    descriptor = None
    for klass in sql_POperand.__mro__:
        if "prm" in klass.__dict__:
            descriptor = klass.__dict__["prm"]
            break
    assert isinstance(descriptor, property)



def test_sql_opfunctioncast_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionCast)


def test_sql_opfunctioncast_constructor_exists():
    assert callable(sql_OpFunctionCast.__init__)


def test_sql_opfunctioncast_constructor_args():
    sig = inspect.signature(sql_OpFunctionCast.__init__)
    params = list(sig.parameters.keys())
    assert "p2" in params, "Missing parameter 'p2'"
    assert "p" in params, "Missing parameter 'p'"
    assert "type" in params, "Missing parameter 'type'"

def test_sql_opfunctioncast_has_p2():
    assert hasattr(sql_OpFunctionCast, "p2")
    descriptor = None
    for klass in sql_OpFunctionCast.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)

def test_sql_opfunctioncast_has_p():
    assert hasattr(sql_OpFunctionCast, "p")
    descriptor = None
    for klass in sql_OpFunctionCast.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_sql_opfunctioncast_has_type():
    assert hasattr(sql_OpFunctionCast, "type")
    descriptor = None
    for klass in sql_OpFunctionCast.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_sql_likeoperand_is_not_abstract():
    assert not inspect.isabstract(sql_LikeOperand)


def test_sql_likeoperand_constructor_exists():
    assert callable(sql_LikeOperand.__init__)


def test_sql_likeoperand_constructor_args():
    sig = inspect.signature(sql_LikeOperand.__init__)
    params = list(sig.parameters.keys())
    assert "op2" in params, "Missing parameter 'op2'"

def test_sql_likeoperand_has_op2():
    assert hasattr(sql_LikeOperand, "op2")
    descriptor = None
    for klass in sql_LikeOperand.__mro__:
        if "op2" in klass.__dict__:
            descriptor = klass.__dict__["op2"]
            break
    assert isinstance(descriptor, property)



def test_orexpr_is_not_abstract():
    assert not inspect.isabstract(OrExpr)


def test_orexpr_constructor_exists():
    assert callable(OrExpr.__init__)


def test_orexpr_constructor_args():
    sig = inspect.signature(OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_sql_fullexpression_is_not_abstract():
    assert not inspect.isabstract(sql_FullExpression)


def test_sql_fullexpression_constructor_exists():
    assert callable(sql_FullExpression.__init__)


def test_sql_fullexpression_constructor_args():
    sig = inspect.signature(sql_FullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"
    assert "notPrm" in params, "Missing parameter 'notPrm'"
    assert "isnull" in params, "Missing parameter 'isnull'"

def test_sql_fullexpression_has_c():
    assert hasattr(sql_FullExpression, "c")
    descriptor = None
    for klass in sql_FullExpression.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_sql_fullexpression_has_notPrm():
    assert hasattr(sql_FullExpression, "notPrm")
    descriptor = None
    for klass in sql_FullExpression.__mro__:
        if "notPrm" in klass.__dict__:
            descriptor = klass.__dict__["notPrm"]
            break
    assert isinstance(descriptor, property)

def test_sql_fullexpression_has_isnull():
    assert hasattr(sql_FullExpression, "isnull")
    descriptor = None
    for klass in sql_FullExpression.__mro__:
        if "isnull" in klass.__dict__:
            descriptor = klass.__dict__["isnull"]
            break
    assert isinstance(descriptor, property)



def test_sql_opfunction_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunction)


def test_sql_opfunction_constructor_exists():
    assert callable(sql_OpFunction.__init__)


def test_sql_opfunction_constructor_args():
    sig = inspect.signature(sql_OpFunction.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"
    assert "star" in params, "Missing parameter 'star'"

def test_sql_opfunction_has_fname():
    assert hasattr(sql_OpFunction, "fname")
    descriptor = None
    for klass in sql_OpFunction.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_sql_opfunction_has_star():
    assert hasattr(sql_OpFunction, "star")
    descriptor = None
    for klass in sql_OpFunction.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrGroupByColumn)


def test_orgroupbycolumn_constructor_exists():
    assert callable(OrGroupByColumn.__init__)


def test_orgroupbycolumn_constructor_args():
    sig = inspect.signature(OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_prms_is_not_abstract():
    assert not inspect.isabstract(sql_Prms)


def test_sql_prms_constructor_exists():
    assert callable(sql_Prms.__init__)


def test_sql_prms_constructor_args():
    sig = inspect.signature(sql_Prms.__init__)
    params = list(sig.parameters.keys())



def test_sql_comparison_is_not_abstract():
    assert not inspect.isabstract(sql_Comparison)


def test_sql_comparison_constructor_exists():
    assert callable(sql_Comparison.__init__)


def test_sql_comparison_constructor_args():
    sig = inspect.signature(sql_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "subOperator" in params, "Missing parameter 'subOperator'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_sql_comparison_has_subOperator():
    assert hasattr(sql_Comparison, "subOperator")
    descriptor = None
    for klass in sql_Comparison.__mro__:
        if "subOperator" in klass.__dict__:
            descriptor = klass.__dict__["subOperator"]
            break
    assert isinstance(descriptor, property)

def test_sql_comparison_has_operator():
    assert hasattr(sql_Comparison, "operator")
    descriptor = None
    for klass in sql_Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_sql_like_is_not_abstract():
    assert not inspect.isabstract(sql_Like)


def test_sql_like_constructor_exists():
    assert callable(sql_Like.__init__)


def test_sql_like_constructor_args():
    sig = inspect.signature(sql_Like.__init__)
    params = list(sig.parameters.keys())
    assert "opLike" in params, "Missing parameter 'opLike'"

def test_sql_like_has_opLike():
    assert hasattr(sql_Like, "opLike")
    descriptor = None
    for klass in sql_Like.__mro__:
        if "opLike" in klass.__dict__:
            descriptor = klass.__dict__["opLike"]
            break
    assert isinstance(descriptor, property)



def test_sql_between_is_not_abstract():
    assert not inspect.isabstract(sql_Between)


def test_sql_between_constructor_exists():
    assert callable(sql_Between.__init__)


def test_sql_between_constructor_args():
    sig = inspect.signature(sql_Between.__init__)
    params = list(sig.parameters.keys())
    assert "opBetween" in params, "Missing parameter 'opBetween'"

def test_sql_between_has_opBetween():
    assert hasattr(sql_Between, "opBetween")
    descriptor = None
    for klass in sql_Between.__mro__:
        if "opBetween" in klass.__dict__:
            descriptor = klass.__dict__["opBetween"]
            break
    assert isinstance(descriptor, property)



def test_sql_existsoper_is_not_abstract():
    assert not inspect.isabstract(sql_ExistsOper)


def test_sql_existsoper_constructor_exists():
    assert callable(sql_ExistsOper.__init__)


def test_sql_existsoper_constructor_args():
    sig = inspect.signature(sql_ExistsOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql_existsoper_has_op():
    assert hasattr(sql_ExistsOper, "op")
    descriptor = None
    for klass in sql_ExistsOper.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sql_inoper_is_not_abstract():
    assert not inspect.isabstract(sql_InOper)


def test_sql_inoper_constructor_exists():
    assert callable(sql_InOper.__init__)


def test_sql_inoper_constructor_args():
    sig = inspect.signature(sql_InOper.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sql_inoper_has_op():
    assert hasattr(sql_InOper, "op")
    descriptor = None
    for klass in sql_InOper.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sql_xexpr_is_not_abstract():
    assert not inspect.isabstract(sql_XExpr)


def test_sql_xexpr_constructor_exists():
    assert callable(sql_XExpr.__init__)


def test_sql_xexpr_constructor_args():
    sig = inspect.signature(sql_XExpr.__init__)
    params = list(sig.parameters.keys())
    assert "xf" in params, "Missing parameter 'xf'"

def test_sql_xexpr_has_xf():
    assert hasattr(sql_XExpr, "xf")
    descriptor = None
    for klass in sql_XExpr.__mro__:
        if "xf" in klass.__dict__:
            descriptor = klass.__dict__["xf"]
            break
    assert isinstance(descriptor, property)



def test_sql_exprgroup_is_not_abstract():
    assert not inspect.isabstract(sql_ExprGroup)


def test_sql_exprgroup_constructor_exists():
    assert callable(sql_ExprGroup.__init__)


def test_sql_exprgroup_constructor_args():
    sig = inspect.signature(sql_ExprGroup.__init__)
    params = list(sig.parameters.keys())
    assert "isnot" in params, "Missing parameter 'isnot'"

def test_sql_exprgroup_has_isnot():
    assert hasattr(sql_ExprGroup, "isnot")
    descriptor = None
    for klass in sql_ExprGroup.__mro__:
        if "isnot" in klass.__dict__:
            descriptor = klass.__dict__["isnot"]
            break
    assert isinstance(descriptor, property)



def test_sql_unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClauseArgs)


def test_sql_unpivotinclauseargs_constructor_exists():
    assert callable(sql_UnpivotInClauseArgs.__init__)


def test_sql_unpivotinclauseargs_constructor_args():
    sig = inspect.signature(sql_UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivotfunction_is_not_abstract():
    assert not inspect.isabstract(sql_PivotFunction)


def test_sql_pivotfunction_constructor_exists():
    assert callable(sql_PivotFunction.__init__)


def test_sql_pivotfunction_constructor_args():
    sig = inspect.signature(sql_PivotFunction.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_PivotInClause)


def test_sql_pivotinclause_constructor_exists():
    assert callable(sql_PivotInClause.__init__)


def test_sql_pivotinclause_constructor_args():
    sig = inspect.signature(sql_PivotInClause.__init__)
    params = list(sig.parameters.keys())
    assert "pinany" in params, "Missing parameter 'pinany'"

def test_sql_pivotinclause_has_pinany():
    assert hasattr(sql_PivotInClause, "pinany")
    descriptor = None
    for klass in sql_PivotInClause.__mro__:
        if "pinany" in klass.__dict__:
            descriptor = klass.__dict__["pinany"]
            break
    assert isinstance(descriptor, property)



def test_sql_pivotforclause_is_not_abstract():
    assert not inspect.isabstract(sql_PivotForClause)


def test_sql_pivotforclause_constructor_exists():
    assert callable(sql_PivotForClause.__init__)


def test_sql_pivotforclause_constructor_args():
    sig = inspect.signature(sql_PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_groupbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql_GroupByColumnFull)


def test_sql_groupbycolumnfull_constructor_exists():
    assert callable(sql_GroupByColumnFull.__init__)


def test_sql_groupbycolumnfull_constructor_args():
    sig = inspect.signature(sql_GroupByColumnFull.__init__)
    params = list(sig.parameters.keys())
    assert "grByInt" in params, "Missing parameter 'grByInt'"

def test_sql_groupbycolumnfull_has_grByInt():
    assert hasattr(sql_GroupByColumnFull, "grByInt")
    descriptor = None
    for klass in sql_GroupByColumnFull.__mro__:
        if "grByInt" in klass.__dict__:
            descriptor = klass.__dict__["grByInt"]
            break
    assert isinstance(descriptor, property)



def test_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrOrderByColumn)


def test_ororderbycolumn_constructor_exists():
    assert callable(OrOrderByColumn.__init__)


def test_ororderbycolumn_constructor_args():
    sig = inspect.signature(OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql_OrderByColumnFull)


def test_sql_orderbycolumnfull_constructor_exists():
    assert callable(sql_OrderByColumnFull.__init__)


def test_sql_orderbycolumnfull_constructor_args():
    sig = inspect.signature(sql_OrderByColumnFull.__init__)
    params = list(sig.parameters.keys())
    assert "colOrderInt" in params, "Missing parameter 'colOrderInt'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_sql_orderbycolumnfull_has_colOrderInt():
    assert hasattr(sql_OrderByColumnFull, "colOrderInt")
    descriptor = None
    for klass in sql_OrderByColumnFull.__mro__:
        if "colOrderInt" in klass.__dict__:
            descriptor = klass.__dict__["colOrderInt"]
            break
    assert isinstance(descriptor, property)

def test_sql_orderbycolumnfull_has_direction():
    assert hasattr(sql_OrderByColumnFull, "direction")
    descriptor = None
    for klass in sql_OrderByColumnFull.__mro__:
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



def test_sql_tbls_is_not_abstract():
    assert not inspect.isabstract(sql_tbls)


def test_sql_tbls_constructor_exists():
    assert callable(sql_tbls.__init__)


def test_sql_tbls_constructor_args():
    sig = inspect.signature(sql_tbls.__init__)
    params = list(sig.parameters.keys())



def test_pivotcol_is_not_abstract():
    assert not inspect.isabstract(PivotCol)


def test_pivotcol_constructor_exists():
    assert callable(PivotCol.__init__)


def test_pivotcol_constructor_args():
    sig = inspect.signature(PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_sql_pcols_is_not_abstract():
    assert not inspect.isabstract(sql_pcols)


def test_sql_pcols_constructor_exists():
    assert callable(sql_pcols.__init__)


def test_sql_pcols_constructor_args():
    sig = inspect.signature(sql_pcols.__init__)
    params = list(sig.parameters.keys())



def test_usingcols_is_not_abstract():
    assert not inspect.isabstract(UsingCols)


def test_usingcols_constructor_exists():
    assert callable(UsingCols.__init__)


def test_usingcols_constructor_args():
    sig = inspect.signature(UsingCols.__init__)
    params = list(sig.parameters.keys())



def test_columnfull_is_not_abstract():
    assert not inspect.isabstract(ColumnFull)


def test_columnfull_constructor_exists():
    assert callable(ColumnFull.__init__)


def test_columnfull_constructor_args():
    sig = inspect.signature(ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_sql_col_is_not_abstract():
    assert not inspect.isabstract(sql_Col)


def test_sql_col_constructor_exists():
    assert callable(sql_Col.__init__)


def test_sql_col_constructor_args():
    sig = inspect.signature(sql_Col.__init__)
    params = list(sig.parameters.keys())



def test_pivots_is_not_abstract():
    assert not inspect.isabstract(Pivots)


def test_pivots_constructor_exists():
    assert callable(Pivots.__init__)


def test_pivots_constructor_args():
    sig = inspect.signature(Pivots.__init__)
    params = list(sig.parameters.keys())



def test_sql_pvcs_is_not_abstract():
    assert not inspect.isabstract(sql_pvcs)


def test_sql_pvcs_constructor_exists():
    assert callable(sql_pvcs.__init__)


def test_sql_pvcs_constructor_args():
    sig = inspect.signature(sql_pvcs.__init__)
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



def test_sql_pivotcol_is_not_abstract():
    assert not inspect.isabstract(sql_PivotCol)


def test_sql_pivotcol_constructor_exists():
    assert callable(sql_PivotCol.__init__)


def test_sql_pivotcol_constructor_args():
    sig = inspect.signature(sql_PivotCol.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivots_is_not_abstract():
    assert not inspect.isabstract(sql_Pivots)


def test_sql_pivots_constructor_exists():
    assert callable(sql_Pivots.__init__)


def test_sql_pivots_constructor_args():
    sig = inspect.signature(sql_Pivots.__init__)
    params = list(sig.parameters.keys())



def test_unpivotinclauseargs_is_not_abstract():
    assert not inspect.isabstract(UnpivotInClauseArgs)


def test_unpivotinclauseargs_constructor_exists():
    assert callable(UnpivotInClauseArgs.__init__)


def test_unpivotinclauseargs_constructor_args():
    sig = inspect.signature(UnpivotInClauseArgs.__init__)
    params = list(sig.parameters.keys())



def test_sql_uicargs_is_not_abstract():
    assert not inspect.isabstract(sql_uicargs)


def test_sql_uicargs_constructor_exists():
    assert callable(sql_uicargs.__init__)


def test_sql_uicargs_constructor_args():
    sig = inspect.signature(sql_uicargs.__init__)
    params = list(sig.parameters.keys())



def test_sql_unpivotinclausearg_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClauseArg)


def test_sql_unpivotinclausearg_constructor_exists():
    assert callable(sql_UnpivotInClauseArg.__init__)


def test_sql_unpivotinclausearg_constructor_args():
    sig = inspect.signature(sql_UnpivotInClauseArg.__init__)
    params = list(sig.parameters.keys())



def test_sql_unpivotinclause_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotInClause)


def test_sql_unpivotinclause_constructor_exists():
    assert callable(sql_UnpivotInClause.__init__)


def test_sql_unpivotinclause_constructor_args():
    sig = inspect.signature(sql_UnpivotInClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivotcolumns_is_not_abstract():
    assert not inspect.isabstract(sql_PivotColumns)


def test_sql_pivotcolumns_constructor_exists():
    assert callable(sql_PivotColumns.__init__)


def test_sql_pivotcolumns_constructor_args():
    sig = inspect.signature(sql_PivotColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql_unpivottable_is_not_abstract():
    assert not inspect.isabstract(sql_UnpivotTable)


def test_sql_unpivottable_constructor_exists():
    assert callable(sql_UnpivotTable.__init__)


def test_sql_unpivottable_constructor_args():
    sig = inspect.signature(sql_UnpivotTable.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivottable_is_not_abstract():
    assert not inspect.isabstract(sql_PivotTable)


def test_sql_pivottable_constructor_exists():
    assert callable(sql_PivotTable.__init__)


def test_sql_pivottable_constructor_args():
    sig = inspect.signature(sql_PivotTable.__init__)
    params = list(sig.parameters.keys())



def test_sql_fromvalues_is_not_abstract():
    assert not inspect.isabstract(sql_FromValues)


def test_sql_fromvalues_constructor_exists():
    assert callable(sql_FromValues.__init__)


def test_sql_fromvalues_constructor_args():
    sig = inspect.signature(sql_FromValues.__init__)
    params = list(sig.parameters.keys())



def test_sql_subqueryoperand_is_not_abstract():
    assert not inspect.isabstract(sql_SubQueryOperand)


def test_sql_subqueryoperand_constructor_exists():
    assert callable(sql_SubQueryOperand.__init__)


def test_sql_subqueryoperand_constructor_args():
    sig = inspect.signature(sql_SubQueryOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql_tablefull_is_not_abstract():
    assert not inspect.isabstract(sql_TableFull)


def test_sql_tablefull_constructor_exists():
    assert callable(sql_TableFull.__init__)


def test_sql_tablefull_constructor_args():
    sig = inspect.signature(sql_TableFull.__init__)
    params = list(sig.parameters.keys())



def test_withcolumns_is_not_abstract():
    assert not inspect.isabstract(WithColumns)


def test_withcolumns_constructor_exists():
    assert callable(WithColumns.__init__)


def test_withcolumns_constructor_args():
    sig = inspect.signature(WithColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql_usingcols_is_not_abstract():
    assert not inspect.isabstract(sql_UsingCols)


def test_sql_usingcols_constructor_exists():
    assert callable(sql_UsingCols.__init__)


def test_sql_usingcols_constructor_args():
    sig = inspect.signature(sql_UsingCols.__init__)
    params = list(sig.parameters.keys())



def test_sql_joincondition_is_not_abstract():
    assert not inspect.isabstract(sql_JoinCondition)


def test_sql_joincondition_constructor_exists():
    assert callable(sql_JoinCondition.__init__)


def test_sql_joincondition_constructor_args():
    sig = inspect.signature(sql_JoinCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_pivotfunctions_is_not_abstract():
    assert not inspect.isabstract(sql_PivotFunctions)


def test_sql_pivotfunctions_constructor_exists():
    assert callable(sql_PivotFunctions.__init__)


def test_sql_pivotfunctions_constructor_args():
    sig = inspect.signature(sql_PivotFunctions.__init__)
    params = list(sig.parameters.keys())
    assert "abc" in params, "Missing parameter 'abc'"

def test_sql_pivotfunctions_has_abc():
    assert hasattr(sql_PivotFunctions, "abc")
    descriptor = None
    for klass in sql_PivotFunctions.__mro__:
        if "abc" in klass.__dict__:
            descriptor = klass.__dict__["abc"]
            break
    assert isinstance(descriptor, property)



def test_rowvalues_is_not_abstract():
    assert not inspect.isabstract(RowValues)


def test_rowvalues_constructor_exists():
    assert callable(RowValues.__init__)


def test_rowvalues_constructor_args():
    sig = inspect.signature(RowValues.__init__)
    params = list(sig.parameters.keys())



def test_sql_rowvalue_is_not_abstract():
    assert not inspect.isabstract(sql_RowValue)


def test_sql_rowvalue_constructor_exists():
    assert callable(sql_RowValue.__init__)


def test_sql_rowvalue_constructor_args():
    sig = inspect.signature(sql_RowValue.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_sql_rowvalue_has_null():
    assert hasattr(sql_RowValue, "null")
    descriptor = None
    for klass in sql_RowValue.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_sql_rowvalues_is_not_abstract():
    assert not inspect.isabstract(sql_RowValues)


def test_sql_rowvalues_constructor_exists():
    assert callable(sql_RowValues.__init__)


def test_sql_rowvalues_constructor_args():
    sig = inspect.signature(sql_RowValues.__init__)
    params = list(sig.parameters.keys())



def test_rows_is_not_abstract():
    assert not inspect.isabstract(Rows)


def test_rows_constructor_exists():
    assert callable(Rows.__init__)


def test_rows_constructor_args():
    sig = inspect.signature(Rows.__init__)
    params = list(sig.parameters.keys())



def test_sql_row_is_not_abstract():
    assert not inspect.isabstract(sql_Row)


def test_sql_row_constructor_exists():
    assert callable(sql_Row.__init__)


def test_sql_row_constructor_args():
    sig = inspect.signature(sql_Row.__init__)
    params = list(sig.parameters.keys())



def test_sql_rows_is_not_abstract():
    assert not inspect.isabstract(sql_Rows)


def test_sql_rows_constructor_exists():
    assert callable(sql_Rows.__init__)


def test_sql_rows_constructor_args():
    sig = inspect.signature(sql_Rows.__init__)
    params = list(sig.parameters.keys())



def test_fromvaluescolumnnames_is_not_abstract():
    assert not inspect.isabstract(FromValuesColumnNames)


def test_fromvaluescolumnnames_constructor_exists():
    assert callable(FromValuesColumnNames.__init__)


def test_fromvaluescolumnnames_constructor_args():
    sig = inspect.signature(FromValuesColumnNames.__init__)
    params = list(sig.parameters.keys())



def test_sql_abc_is_not_abstract():
    assert not inspect.isabstract(sql_abc)


def test_sql_abc_constructor_exists():
    assert callable(sql_abc.__init__)


def test_sql_abc_constructor_args():
    sig = inspect.signature(sql_abc.__init__)
    params = list(sig.parameters.keys())



def test_sql_columnnames_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnNames)


def test_sql_columnnames_constructor_exists():
    assert callable(sql_ColumnNames.__init__)


def test_sql_columnnames_constructor_args():
    sig = inspect.signature(sql_ColumnNames.__init__)
    params = list(sig.parameters.keys())
    assert "colName" in params, "Missing parameter 'colName'"

def test_sql_columnnames_has_colName():
    assert hasattr(sql_ColumnNames, "colName")
    descriptor = None
    for klass in sql_ColumnNames.__mro__:
        if "colName" in klass.__dict__:
            descriptor = klass.__dict__["colName"]
            break
    assert isinstance(descriptor, property)



def test_sql_fromvaluescolumnnames_is_not_abstract():
    assert not inspect.isabstract(sql_FromValuesColumnNames)


def test_sql_fromvaluescolumnnames_constructor_exists():
    assert callable(sql_FromValuesColumnNames.__init__)


def test_sql_fromvaluescolumnnames_constructor_args():
    sig = inspect.signature(sql_FromValuesColumnNames.__init__)
    params = list(sig.parameters.keys())



def test_sql_fromvaluescolumns_is_not_abstract():
    assert not inspect.isabstract(sql_FromValuesColumns)


def test_sql_fromvaluescolumns_constructor_exists():
    assert callable(sql_FromValuesColumns.__init__)


def test_sql_fromvaluescolumns_constructor_args():
    sig = inspect.signature(sql_FromValuesColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql_values_is_not_abstract():
    assert not inspect.isabstract(sql_Values)


def test_sql_values_constructor_exists():
    assert callable(sql_Values.__init__)


def test_sql_values_constructor_args():
    sig = inspect.signature(sql_Values.__init__)
    params = list(sig.parameters.keys())



def test_sql_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrOrderByColumn)


def test_sql_ororderbycolumn_constructor_exists():
    assert callable(sql_OrOrderByColumn.__init__)


def test_sql_ororderbycolumn_constructor_args():
    sig = inspect.signature(sql_OrOrderByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrGroupByColumn)


def test_sql_orgroupbycolumn_constructor_exists():
    assert callable(sql_OrGroupByColumn.__init__)


def test_sql_orgroupbycolumn_constructor_args():
    sig = inspect.signature(sql_OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_orexpr_is_not_abstract():
    assert not inspect.isabstract(sql_OrExpr)


def test_sql_orexpr_constructor_exists():
    assert callable(sql_OrExpr.__init__)


def test_sql_orexpr_constructor_args():
    sig = inspect.signature(sql_OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_sql_ortable_is_not_abstract():
    assert not inspect.isabstract(sql_OrTable)


def test_sql_ortable_constructor_exists():
    assert callable(sql_OrTable.__init__)


def test_sql_ortable_constructor_args():
    sig = inspect.signature(sql_OrTable.__init__)
    params = list(sig.parameters.keys())



def test_sql_fromtablejoin_is_not_abstract():
    assert not inspect.isabstract(sql_FromTableJoin)


def test_sql_fromtablejoin_constructor_exists():
    assert callable(sql_FromTableJoin.__init__)


def test_sql_fromtablejoin_constructor_args():
    sig = inspect.signature(sql_FromTableJoin.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"

def test_sql_fromtablejoin_has_join():
    assert hasattr(sql_FromTableJoin, "join")
    descriptor = None
    for klass in sql_FromTableJoin.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)



def test_sql_tableoralias_is_not_abstract():
    assert not inspect.isabstract(sql_TableOrAlias)


def test_sql_tableoralias_constructor_exists():
    assert callable(sql_TableOrAlias.__init__)


def test_sql_tableoralias_constructor_args():
    sig = inspect.signature(sql_TableOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql_tableoralias_has_alias():
    assert hasattr(sql_TableOrAlias, "alias")
    descriptor = None
    for klass in sql_TableOrAlias.__mro__:
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



def test_sql_fromtable_is_not_abstract():
    assert not inspect.isabstract(sql_FromTable)


def test_sql_fromtable_constructor_exists():
    assert callable(sql_FromTable.__init__)


def test_sql_fromtable_constructor_args():
    sig = inspect.signature(sql_FromTable.__init__)
    params = list(sig.parameters.keys())



def test_sql_dbobjectnameall_is_not_abstract():
    assert not inspect.isabstract(sql_DbObjectNameAll)


def test_sql_dbobjectnameall_constructor_exists():
    assert callable(sql_DbObjectNameAll.__init__)


def test_sql_dbobjectnameall_constructor_args():
    sig = inspect.signature(sql_DbObjectNameAll.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"

def test_sql_dbobjectnameall_has_dbname():
    assert hasattr(sql_DbObjectNameAll, "dbname")
    descriptor = None
    for klass in sql_DbObjectNameAll.__mro__:
        if "dbname" in klass.__dict__:
            descriptor = klass.__dict__["dbname"]
            break
    assert isinstance(descriptor, property)



def test_sql_dbobjectname_is_not_abstract():
    assert not inspect.isabstract(sql_DbObjectName)


def test_sql_dbobjectname_constructor_exists():
    assert callable(sql_DbObjectName.__init__)


def test_sql_dbobjectname_constructor_args():
    sig = inspect.signature(sql_DbObjectName.__init__)
    params = list(sig.parameters.keys())
    assert "dbname" in params, "Missing parameter 'dbname'"

def test_sql_dbobjectname_has_dbname():
    assert hasattr(sql_DbObjectName, "dbname")
    descriptor = None
    for klass in sql_DbObjectName.__mro__:
        if "dbname" in klass.__dict__:
            descriptor = klass.__dict__["dbname"]
            break
    assert isinstance(descriptor, property)



def test_sql_operands_is_not_abstract():
    assert not inspect.isabstract(sql_Operands)


def test_sql_operands_constructor_exists():
    assert callable(sql_Operands.__init__)


def test_sql_operands_constructor_args():
    sig = inspect.signature(sql_Operands.__init__)
    params = list(sig.parameters.keys())



def test_orcolumn_is_not_abstract():
    assert not inspect.isabstract(OrColumn)


def test_orcolumn_constructor_exists():
    assert callable(OrColumn.__init__)


def test_orcolumn_constructor_args():
    sig = inspect.signature(OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_columnoralias_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnOrAlias)


def test_sql_columnoralias_constructor_exists():
    assert callable(sql_ColumnOrAlias.__init__)


def test_sql_columnoralias_constructor_args():
    sig = inspect.signature(sql_ColumnOrAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "allCols" in params, "Missing parameter 'allCols'"

def test_sql_columnoralias_has_alias():
    assert hasattr(sql_ColumnOrAlias, "alias")
    descriptor = None
    for klass in sql_ColumnOrAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_sql_columnoralias_has_allCols():
    assert hasattr(sql_ColumnOrAlias, "allCols")
    descriptor = None
    for klass in sql_ColumnOrAlias.__mro__:
        if "allCols" in klass.__dict__:
            descriptor = klass.__dict__["allCols"]
            break
    assert isinstance(descriptor, property)



def test_pivotforclause_is_not_abstract():
    assert not inspect.isabstract(PivotForClause)


def test_pivotforclause_constructor_exists():
    assert callable(PivotForClause.__init__)


def test_pivotforclause_constructor_args():
    sig = inspect.signature(PivotForClause.__init__)
    params = list(sig.parameters.keys())



def test_sql_columnfull_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnFull)


def test_sql_columnfull_constructor_exists():
    assert callable(sql_ColumnFull.__init__)


def test_sql_columnfull_constructor_args():
    sig = inspect.signature(sql_ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_sql_orcolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrColumn)


def test_sql_orcolumn_constructor_exists():
    assert callable(sql_OrColumn.__init__)


def test_sql_orcolumn_constructor_args():
    sig = inspect.signature(sql_OrColumn.__init__)
    params = list(sig.parameters.keys())



def test_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
    params = list(sig.parameters.keys())



def test_selectquery_is_not_abstract():
    assert not inspect.isabstract(SelectQuery)


def test_selectquery_constructor_exists():
    assert callable(SelectQuery.__init__)


def test_selectquery_constructor_args():
    sig = inspect.signature(SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql_select_is_not_abstract():
    assert not inspect.isabstract(sql_Select)


def test_sql_select_constructor_exists():
    assert callable(sql_Select.__init__)


def test_sql_select_constructor_args():
    sig = inspect.signature(sql_Select.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_sql_select_has_select():
    assert hasattr(sql_Select, "select")
    descriptor = None
    for klass in sql_Select.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_sql_selectsubset_is_not_abstract():
    assert not inspect.isabstract(sql_SelectSubSet)


def test_sql_selectsubset_constructor_exists():
    assert callable(sql_SelectSubSet.__init__)


def test_sql_selectsubset_constructor_args():
    sig = inspect.signature(sql_SelectSubSet.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "all" in params, "Missing parameter 'all'"

def test_sql_selectsubset_has_op():
    assert hasattr(sql_SelectSubSet, "op")
    descriptor = None
    for klass in sql_SelectSubSet.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_sql_selectsubset_has_all():
    assert hasattr(sql_SelectSubSet, "all")
    descriptor = None
    for klass in sql_SelectSubSet.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_sql_limit_is_not_abstract():
    assert not inspect.isabstract(sql_Limit)


def test_sql_limit_constructor_exists():
    assert callable(sql_Limit.__init__)


def test_sql_limit_constructor_args():
    sig = inspect.signature(sql_Limit.__init__)
    params = list(sig.parameters.keys())
    assert "l2" in params, "Missing parameter 'l2'"
    assert "l1" in params, "Missing parameter 'l1'"

def test_sql_limit_has_l2():
    assert hasattr(sql_Limit, "l2")
    descriptor = None
    for klass in sql_Limit.__mro__:
        if "l2" in klass.__dict__:
            descriptor = klass.__dict__["l2"]
            break
    assert isinstance(descriptor, property)

def test_sql_limit_has_l1():
    assert hasattr(sql_Limit, "l1")
    descriptor = None
    for klass in sql_Limit.__mro__:
        if "l1" in klass.__dict__:
            descriptor = klass.__dict__["l1"]
            break
    assert isinstance(descriptor, property)



def test_sql_offset_is_not_abstract():
    assert not inspect.isabstract(sql_Offset)


def test_sql_offset_constructor_exists():
    assert callable(sql_Offset.__init__)


def test_sql_offset_constructor_args():
    sig = inspect.signature(sql_Offset.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"

def test_sql_offset_has_offset():
    assert hasattr(sql_Offset, "offset")
    descriptor = None
    for klass in sql_Offset.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_sql_unsignedvalue_is_not_abstract():
    assert not inspect.isabstract(sql_UnsignedValue)


def test_sql_unsignedvalue_constructor_exists():
    assert callable(sql_UnsignedValue.__init__)


def test_sql_unsignedvalue_constructor_args():
    sig = inspect.signature(sql_UnsignedValue.__init__)
    params = list(sig.parameters.keys())
    assert "integer" in params, "Missing parameter 'integer'"

def test_sql_unsignedvalue_has_integer():
    assert hasattr(sql_UnsignedValue, "integer")
    descriptor = None
    for klass in sql_UnsignedValue.__mro__:
        if "integer" in klass.__dict__:
            descriptor = klass.__dict__["integer"]
            break
    assert isinstance(descriptor, property)



def test_sql_fetchfirst_is_not_abstract():
    assert not inspect.isabstract(sql_FetchFirst)


def test_sql_fetchfirst_constructor_exists():
    assert callable(sql_FetchFirst.__init__)


def test_sql_fetchfirst_constructor_args():
    sig = inspect.signature(sql_FetchFirst.__init__)
    params = list(sig.parameters.keys())
    assert "row" in params, "Missing parameter 'row'"

def test_sql_fetchfirst_has_row():
    assert hasattr(sql_FetchFirst, "row")
    descriptor = None
    for klass in sql_FetchFirst.__mro__:
        if "row" in klass.__dict__:
            descriptor = klass.__dict__["row"]
            break
    assert isinstance(descriptor, property)



def test_sql_withcolumns_is_not_abstract():
    assert not inspect.isabstract(sql_WithColumns)


def test_sql_withcolumns_constructor_exists():
    assert callable(sql_WithColumns.__init__)


def test_sql_withcolumns_constructor_args():
    sig = inspect.signature(sql_WithColumns.__init__)
    params = list(sig.parameters.keys())



def test_sql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sql_SelectQuery)


def test_sql_selectquery_constructor_exists():
    assert callable(sql_SelectQuery.__init__)


def test_sql_selectquery_constructor_args():
    sig = inspect.signature(sql_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql_withquery_is_not_abstract():
    assert not inspect.isabstract(sql_WithQuery)


def test_sql_withquery_constructor_exists():
    assert callable(sql_WithQuery.__init__)


def test_sql_withquery_constructor_args():
    sig = inspect.signature(sql_WithQuery.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"
    assert "wname" in params, "Missing parameter 'wname'"

def test_sql_withquery_has_w():
    assert hasattr(sql_WithQuery, "w")
    descriptor = None
    for klass in sql_WithQuery.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)

def test_sql_withquery_has_wname():
    assert hasattr(sql_WithQuery, "wname")
    descriptor = None
    for klass in sql_WithQuery.__mro__:
        if "wname" in klass.__dict__:
            descriptor = klass.__dict__["wname"]
            break
    assert isinstance(descriptor, property)

def test_extract_values_exists():
    # Check that the Enumeration exists
    assert EXTRACT_VALUES is not None

def test_extract_values_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EXTRACT_VALUES]
    expected_literals = [
        "daymin",
        "h",
        "hs",
        "micros",
        "hmin",
        "s",
        "month",
        "quart",
        "hms",
        "m",
        "week",
        "dayh",
        "ds",
        "day",
        "dms",
        "minMicro",
        "year",
        "ms",
        "minSec",
        "yearMonth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EXTRACT_VALUES"

def test_xfunction_exists():
    # Check that the Enumeration exists
    assert XFunction is not None

def test_xfunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XFunction]
    expected_literals = [
        "xeq",
        "xnotin",
        "xgtl",
        "xlsr",
        "xin",
        "xbwn",
        "xgt",
        "xls",
        "xnoteq",
        "xbwnc",
        "xbwnl",
        "xbwnr",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in XFunction"


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
sql_Multiply_strategy = st.builds(
    sql_Multiply,
)
sql_Division_strategy = st.builds(
    sql_Division,
)
sql_Minus_strategy = st.builds(
    sql_Minus,
)
sql_Concat_strategy = st.builds(
    sql_Concat,
)
sql_Plus_strategy = st.builds(
    sql_Plus,
)
UnpivotInClause_strategy = st.builds(
    UnpivotInClause,
)
sql_UnipivotInClause_strategy = st.builds(
    sql_UnipivotInClause,
    op=
        safe_text
)
sql_IntegerValue_strategy = st.builds(
    sql_IntegerValue,
    integer=
        safe_text
)
sql_OpFunctionArgAgregate_strategy = st.builds(
    sql_OpFunctionArgAgregate,
)
OpFunctionArg_strategy = st.builds(
    OpFunctionArg,
)
sql_OpFList_strategy = st.builds(
    sql_OpFList,
)
sql_OpFunctionArgOperand_strategy = st.builds(
    sql_OpFunctionArgOperand,
)
SQLCaseWhens_strategy = st.builds(
    SQLCaseWhens,
)
sql_WhenList_strategy = st.builds(
    sql_WhenList,
)
sql_SqlCaseWhen_strategy = st.builds(
    sql_SqlCaseWhen,
)
sql_SQLCaseWhens_strategy = st.builds(
    sql_SQLCaseWhens,
)
OperandList_strategy = st.builds(
    OperandList,
)
sql_OpList_strategy = st.builds(
    sql_OpList,
)
RowValue_strategy = st.builds(
    RowValue,
)
sql_OrderByClause_strategy = st.builds(
    sql_OrderByClause,
)
sql_QueryPartitionClause_strategy = st.builds(
    sql_QueryPartitionClause,
)
sql_AnalyticClause_strategy = st.builds(
    sql_AnalyticClause,
)
sql_FunctionAnalytical_strategy = st.builds(
    sql_FunctionAnalytical,
)
sql_OpFunctionArg_strategy = st.builds(
    sql_OpFunctionArg,
)
AnalyticExprArgs_strategy = st.builds(
    AnalyticExprArgs,
)
sql_AExpArgs_strategy = st.builds(
    sql_AExpArgs,
)
QueryPartitionClause_strategy = st.builds(
    QueryPartitionClause,
)
sql_AnalyticExprArgs_strategy = st.builds(
    sql_AnalyticExprArgs,
)
OrderByClauseArgs_strategy = st.builds(
    OrderByClauseArgs,
)
sql_OBCArgs_strategy = st.builds(
    sql_OBCArgs,
)
sql_OrderByClauseArg_strategy = st.builds(
    sql_OrderByClauseArg,
)
sql_OrderByClauseArgs_strategy = st.builds(
    sql_OrderByClauseArgs,
)
sql_AnalyticExprArg_strategy = st.builds(
    sql_AnalyticExprArg,
)
sql_WindowingClauseOperandFollowing_strategy = st.builds(
    sql_WindowingClauseOperandFollowing,
)
WindowingClause_strategy = st.builds(
    WindowingClause,
)
sql_WindowingClauseOperandPreceding_strategy = st.builds(
    sql_WindowingClauseOperandPreceding,
)
sql_WindowingClauseBetween_strategy = st.builds(
    sql_WindowingClauseBetween,
)
sql_WindowingClause_strategy = st.builds(
    sql_WindowingClause,
)
sql_Operand_strategy = st.builds(
    sql_Operand,
)
OpFunctionArgAgregate_strategy = st.builds(
    OpFunctionArgAgregate,
)
sql_OperandList_strategy = st.builds(
    sql_OperandList,
)
sql_ScalarOperand_strategy = st.builds(
    sql_ScalarOperand,
    sodate=
        safe_text,
    sostr=
        safe_text,
    sotime=
        safe_text,
    soUInt=
        safe_text,
    sodbl=
        safe_text,
    soint=
        safe_text,
    sodt=
        safe_text
)
sql_ExpOperand_strategy = st.builds(
    sql_ExpOperand,
    prm=
        safe_text
)
sql_SQLCaseOperand_strategy = st.builds(
    sql_SQLCaseOperand,
)
sql_FunctionExtract_strategy = st.builds(
    sql_FunctionExtract,
    v=
        safe_text
)
sql_ColumnOperand_strategy = st.builds(
    sql_ColumnOperand,
    ora=
        safe_text
)
Prms_strategy = st.builds(
    Prms,
)
sql_JRParameter_strategy = st.builds(
    sql_JRParameter,
    jrprm=
        safe_text
)
sql_OperandListGroup_strategy = st.builds(
    sql_OperandListGroup,
)
sql_POperand_strategy = st.builds(
    sql_POperand,
    prm=
        safe_text
)
sql_OpFunctionCast_strategy = st.builds(
    sql_OpFunctionCast,
    p2=
        safe_text,
    p=
        safe_text,
    type=
        safe_text
)
sql_LikeOperand_strategy = st.builds(
    sql_LikeOperand,
    op2=
        safe_text
)
OrExpr_strategy = st.builds(
    OrExpr,
)
sql_FullExpression_strategy = st.builds(
    sql_FullExpression,
    c=
        safe_text,
    notPrm=
        safe_text,
    isnull=
        safe_text
)
sql_OpFunction_strategy = st.builds(
    sql_OpFunction,
    fname=
        safe_text,
    star=
        safe_text
)
OrGroupByColumn_strategy = st.builds(
    OrGroupByColumn,
)
sql_Prms_strategy = st.builds(
    sql_Prms,
)
sql_Comparison_strategy = st.builds(
    sql_Comparison,
    subOperator=
        safe_text,
    operator=
        safe_text
)
sql_Like_strategy = st.builds(
    sql_Like,
    opLike=
        safe_text
)
sql_Between_strategy = st.builds(
    sql_Between,
    opBetween=
        safe_text
)
sql_ExistsOper_strategy = st.builds(
    sql_ExistsOper,
    op=
        safe_text
)
sql_InOper_strategy = st.builds(
    sql_InOper,
    op=
        safe_text
)
sql_XExpr_strategy = st.builds(
    sql_XExpr,
    xf=
        safe_text
)
sql_ExprGroup_strategy = st.builds(
    sql_ExprGroup,
    isnot=
        safe_text
)
sql_UnpivotInClauseArgs_strategy = st.builds(
    sql_UnpivotInClauseArgs,
)
sql_PivotFunction_strategy = st.builds(
    sql_PivotFunction,
)
sql_PivotInClause_strategy = st.builds(
    sql_PivotInClause,
    pinany=
        safe_text
)
sql_PivotForClause_strategy = st.builds(
    sql_PivotForClause,
)
sql_GroupByColumnFull_strategy = st.builds(
    sql_GroupByColumnFull,
    grByInt=
        safe_text
)
OrOrderByColumn_strategy = st.builds(
    OrOrderByColumn,
)
sql_OrderByColumnFull_strategy = st.builds(
    sql_OrderByColumnFull,
    colOrderInt=
        safe_text,
    direction=
        safe_text
)
TableFull_strategy = st.builds(
    TableFull,
)
sql_tbls_strategy = st.builds(
    sql_tbls,
)
PivotCol_strategy = st.builds(
    PivotCol,
)
sql_pcols_strategy = st.builds(
    sql_pcols,
)
UsingCols_strategy = st.builds(
    UsingCols,
)
ColumnFull_strategy = st.builds(
    ColumnFull,
)
sql_Col_strategy = st.builds(
    sql_Col,
)
Pivots_strategy = st.builds(
    Pivots,
)
sql_pvcs_strategy = st.builds(
    sql_pvcs,
)
PivotFunction_strategy = st.builds(
    PivotFunction,
)
PivotColumns_strategy = st.builds(
    PivotColumns,
)
sql_PivotCol_strategy = st.builds(
    sql_PivotCol,
)
sql_Pivots_strategy = st.builds(
    sql_Pivots,
)
UnpivotInClauseArgs_strategy = st.builds(
    UnpivotInClauseArgs,
)
sql_uicargs_strategy = st.builds(
    sql_uicargs,
)
sql_UnpivotInClauseArg_strategy = st.builds(
    sql_UnpivotInClauseArg,
)
sql_UnpivotInClause_strategy = st.builds(
    sql_UnpivotInClause,
)
sql_PivotColumns_strategy = st.builds(
    sql_PivotColumns,
)
sql_UnpivotTable_strategy = st.builds(
    sql_UnpivotTable,
)
sql_PivotTable_strategy = st.builds(
    sql_PivotTable,
)
sql_FromValues_strategy = st.builds(
    sql_FromValues,
)
sql_SubQueryOperand_strategy = st.builds(
    sql_SubQueryOperand,
)
sql_TableFull_strategy = st.builds(
    sql_TableFull,
)
WithColumns_strategy = st.builds(
    WithColumns,
)
sql_UsingCols_strategy = st.builds(
    sql_UsingCols,
)
sql_JoinCondition_strategy = st.builds(
    sql_JoinCondition,
)
sql_PivotFunctions_strategy = st.builds(
    sql_PivotFunctions,
    abc=
        safe_text
)
RowValues_strategy = st.builds(
    RowValues,
)
sql_RowValue_strategy = st.builds(
    sql_RowValue,
    null=
        safe_text
)
sql_RowValues_strategy = st.builds(
    sql_RowValues,
)
Rows_strategy = st.builds(
    Rows,
)
sql_Row_strategy = st.builds(
    sql_Row,
)
sql_Rows_strategy = st.builds(
    sql_Rows,
)
FromValuesColumnNames_strategy = st.builds(
    FromValuesColumnNames,
)
sql_abc_strategy = st.builds(
    sql_abc,
)
sql_ColumnNames_strategy = st.builds(
    sql_ColumnNames,
    colName=
        safe_text
)
sql_FromValuesColumnNames_strategy = st.builds(
    sql_FromValuesColumnNames,
)
sql_FromValuesColumns_strategy = st.builds(
    sql_FromValuesColumns,
)
sql_Values_strategy = st.builds(
    sql_Values,
)
sql_OrOrderByColumn_strategy = st.builds(
    sql_OrOrderByColumn,
)
sql_OrGroupByColumn_strategy = st.builds(
    sql_OrGroupByColumn,
)
sql_OrExpr_strategy = st.builds(
    sql_OrExpr,
)
sql_OrTable_strategy = st.builds(
    sql_OrTable,
)
sql_FromTableJoin_strategy = st.builds(
    sql_FromTableJoin,
    join=
        safe_text
)
sql_TableOrAlias_strategy = st.builds(
    sql_TableOrAlias,
    alias=
        safe_text
)
OrTable_strategy = st.builds(
    OrTable,
)
sql_FromTable_strategy = st.builds(
    sql_FromTable,
)
sql_DbObjectNameAll_strategy = st.builds(
    sql_DbObjectNameAll,
    dbname=
        safe_text
)
sql_DbObjectName_strategy = st.builds(
    sql_DbObjectName,
    dbname=
        safe_text
)
sql_Operands_strategy = st.builds(
    sql_Operands,
)
OrColumn_strategy = st.builds(
    OrColumn,
)
sql_ColumnOrAlias_strategy = st.builds(
    sql_ColumnOrAlias,
    alias=
        safe_text,
    allCols=
        safe_text
)
PivotForClause_strategy = st.builds(
    PivotForClause,
)
sql_ColumnFull_strategy = st.builds(
    sql_ColumnFull,
)
sql_OrColumn_strategy = st.builds(
    sql_OrColumn,
)
sql_Model_strategy = st.builds(
    sql_Model,
)
SelectQuery_strategy = st.builds(
    SelectQuery,
)
sql_Select_strategy = st.builds(
    sql_Select,
    select=
        safe_text
)
sql_SelectSubSet_strategy = st.builds(
    sql_SelectSubSet,
    op=
        safe_text,
    all=
        safe_text
)
sql_Limit_strategy = st.builds(
    sql_Limit,
    l2=
        safe_text,
    l1=
        safe_text
)
sql_Offset_strategy = st.builds(
    sql_Offset,
    offset=
        safe_text
)
sql_UnsignedValue_strategy = st.builds(
    sql_UnsignedValue,
    integer=
        safe_text
)
sql_FetchFirst_strategy = st.builds(
    sql_FetchFirst,
    row=
        safe_text
)
sql_WithColumns_strategy = st.builds(
    sql_WithColumns,
)
sql_SelectQuery_strategy = st.builds(
    sql_SelectQuery,
)
sql_WithQuery_strategy = st.builds(
    sql_WithQuery,
    w=
        safe_text,
    wname=
        safe_text
)

@given(instance=Operands_strategy)
@settings(max_examples=50)
def test_operands_instantiation(instance):
    assert isinstance(instance, Operands)

@given(instance=sql_Multiply_strategy)
@settings(max_examples=50)
def test_sql_multiply_instantiation(instance):
    assert isinstance(instance, sql_Multiply)

@given(instance=sql_Division_strategy)
@settings(max_examples=50)
def test_sql_division_instantiation(instance):
    assert isinstance(instance, sql_Division)

@given(instance=sql_Minus_strategy)
@settings(max_examples=50)
def test_sql_minus_instantiation(instance):
    assert isinstance(instance, sql_Minus)

@given(instance=sql_Concat_strategy)
@settings(max_examples=50)
def test_sql_concat_instantiation(instance):
    assert isinstance(instance, sql_Concat)

@given(instance=sql_Plus_strategy)
@settings(max_examples=50)
def test_sql_plus_instantiation(instance):
    assert isinstance(instance, sql_Plus)

@given(instance=UnpivotInClause_strategy)
@settings(max_examples=50)
def test_unpivotinclause_instantiation(instance):
    assert isinstance(instance, UnpivotInClause)

@given(instance=sql_UnipivotInClause_strategy)
@settings(max_examples=50)
def test_sql_unipivotinclause_instantiation(instance):
    assert isinstance(instance, sql_UnipivotInClause)



@given(instance=sql_UnipivotInClause_strategy)
def test_sql_unipivotinclause_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql_IntegerValue_strategy)
@settings(max_examples=50)
def test_sql_integervalue_instantiation(instance):
    assert isinstance(instance, sql_IntegerValue)



@given(instance=sql_IntegerValue_strategy)
def test_sql_integervalue_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=sql_OpFunctionArgAgregate_strategy)
@settings(max_examples=50)
def test_sql_opfunctionargagregate_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArgAgregate)

@given(instance=OpFunctionArg_strategy)
@settings(max_examples=50)
def test_opfunctionarg_instantiation(instance):
    assert isinstance(instance, OpFunctionArg)

@given(instance=sql_OpFList_strategy)
@settings(max_examples=50)
def test_sql_opflist_instantiation(instance):
    assert isinstance(instance, sql_OpFList)

@given(instance=sql_OpFunctionArgOperand_strategy)
@settings(max_examples=50)
def test_sql_opfunctionargoperand_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArgOperand)

@given(instance=SQLCaseWhens_strategy)
@settings(max_examples=50)
def test_sqlcasewhens_instantiation(instance):
    assert isinstance(instance, SQLCaseWhens)

@given(instance=sql_WhenList_strategy)
@settings(max_examples=50)
def test_sql_whenlist_instantiation(instance):
    assert isinstance(instance, sql_WhenList)

@given(instance=sql_SqlCaseWhen_strategy)
@settings(max_examples=50)
def test_sql_sqlcasewhen_instantiation(instance):
    assert isinstance(instance, sql_SqlCaseWhen)

@given(instance=sql_SQLCaseWhens_strategy)
@settings(max_examples=50)
def test_sql_sqlcasewhens_instantiation(instance):
    assert isinstance(instance, sql_SQLCaseWhens)

@given(instance=OperandList_strategy)
@settings(max_examples=50)
def test_operandlist_instantiation(instance):
    assert isinstance(instance, OperandList)

@given(instance=sql_OpList_strategy)
@settings(max_examples=50)
def test_sql_oplist_instantiation(instance):
    assert isinstance(instance, sql_OpList)

@given(instance=RowValue_strategy)
@settings(max_examples=50)
def test_rowvalue_instantiation(instance):
    assert isinstance(instance, RowValue)

@given(instance=sql_OrderByClause_strategy)
@settings(max_examples=50)
def test_sql_orderbyclause_instantiation(instance):
    assert isinstance(instance, sql_OrderByClause)

@given(instance=sql_QueryPartitionClause_strategy)
@settings(max_examples=50)
def test_sql_querypartitionclause_instantiation(instance):
    assert isinstance(instance, sql_QueryPartitionClause)

@given(instance=sql_AnalyticClause_strategy)
@settings(max_examples=50)
def test_sql_analyticclause_instantiation(instance):
    assert isinstance(instance, sql_AnalyticClause)

@given(instance=sql_FunctionAnalytical_strategy)
@settings(max_examples=50)
def test_sql_functionanalytical_instantiation(instance):
    assert isinstance(instance, sql_FunctionAnalytical)

@given(instance=sql_OpFunctionArg_strategy)
@settings(max_examples=50)
def test_sql_opfunctionarg_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArg)

@given(instance=AnalyticExprArgs_strategy)
@settings(max_examples=50)
def test_analyticexprargs_instantiation(instance):
    assert isinstance(instance, AnalyticExprArgs)

@given(instance=sql_AExpArgs_strategy)
@settings(max_examples=50)
def test_sql_aexpargs_instantiation(instance):
    assert isinstance(instance, sql_AExpArgs)

@given(instance=QueryPartitionClause_strategy)
@settings(max_examples=50)
def test_querypartitionclause_instantiation(instance):
    assert isinstance(instance, QueryPartitionClause)

@given(instance=sql_AnalyticExprArgs_strategy)
@settings(max_examples=50)
def test_sql_analyticexprargs_instantiation(instance):
    assert isinstance(instance, sql_AnalyticExprArgs)

@given(instance=OrderByClauseArgs_strategy)
@settings(max_examples=50)
def test_orderbyclauseargs_instantiation(instance):
    assert isinstance(instance, OrderByClauseArgs)

@given(instance=sql_OBCArgs_strategy)
@settings(max_examples=50)
def test_sql_obcargs_instantiation(instance):
    assert isinstance(instance, sql_OBCArgs)

@given(instance=sql_OrderByClauseArg_strategy)
@settings(max_examples=50)
def test_sql_orderbyclausearg_instantiation(instance):
    assert isinstance(instance, sql_OrderByClauseArg)

@given(instance=sql_OrderByClauseArgs_strategy)
@settings(max_examples=50)
def test_sql_orderbyclauseargs_instantiation(instance):
    assert isinstance(instance, sql_OrderByClauseArgs)

@given(instance=sql_AnalyticExprArg_strategy)
@settings(max_examples=50)
def test_sql_analyticexprarg_instantiation(instance):
    assert isinstance(instance, sql_AnalyticExprArg)

@given(instance=sql_WindowingClauseOperandFollowing_strategy)
@settings(max_examples=50)
def test_sql_windowingclauseoperandfollowing_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseOperandFollowing)

@given(instance=WindowingClause_strategy)
@settings(max_examples=50)
def test_windowingclause_instantiation(instance):
    assert isinstance(instance, WindowingClause)

@given(instance=sql_WindowingClauseOperandPreceding_strategy)
@settings(max_examples=50)
def test_sql_windowingclauseoperandpreceding_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseOperandPreceding)

@given(instance=sql_WindowingClauseBetween_strategy)
@settings(max_examples=50)
def test_sql_windowingclausebetween_instantiation(instance):
    assert isinstance(instance, sql_WindowingClauseBetween)

@given(instance=sql_WindowingClause_strategy)
@settings(max_examples=50)
def test_sql_windowingclause_instantiation(instance):
    assert isinstance(instance, sql_WindowingClause)

@given(instance=sql_Operand_strategy)
@settings(max_examples=50)
def test_sql_operand_instantiation(instance):
    assert isinstance(instance, sql_Operand)

@given(instance=OpFunctionArgAgregate_strategy)
@settings(max_examples=50)
def test_opfunctionargagregate_instantiation(instance):
    assert isinstance(instance, OpFunctionArgAgregate)

@given(instance=sql_OperandList_strategy)
@settings(max_examples=50)
def test_sql_operandlist_instantiation(instance):
    assert isinstance(instance, sql_OperandList)

@given(instance=sql_ScalarOperand_strategy)
@settings(max_examples=50)
def test_sql_scalaroperand_instantiation(instance):
    assert isinstance(instance, sql_ScalarOperand)



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sodate_setter(instance):
    original = instance.sodate
    instance.sodate = original
    assert instance.sodate == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sostr_setter(instance):
    original = instance.sostr
    instance.sostr = original
    assert instance.sostr == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sotime_setter(instance):
    original = instance.sotime
    instance.sotime = original
    assert instance.sotime == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_soUInt_setter(instance):
    original = instance.soUInt
    instance.soUInt = original
    assert instance.soUInt == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sodbl_setter(instance):
    original = instance.sodbl
    instance.sodbl = original
    assert instance.sodbl == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_soint_setter(instance):
    original = instance.soint
    instance.soint = original
    assert instance.soint == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sodt_setter(instance):
    original = instance.sodt
    instance.sodt = original
    assert instance.sodt == original

@given(instance=sql_ExpOperand_strategy)
@settings(max_examples=50)
def test_sql_expoperand_instantiation(instance):
    assert isinstance(instance, sql_ExpOperand)



@given(instance=sql_ExpOperand_strategy)
def test_sql_expoperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql_SQLCaseOperand_strategy)
@settings(max_examples=50)
def test_sql_sqlcaseoperand_instantiation(instance):
    assert isinstance(instance, sql_SQLCaseOperand)

@given(instance=sql_FunctionExtract_strategy)
@settings(max_examples=50)
def test_sql_functionextract_instantiation(instance):
    assert isinstance(instance, sql_FunctionExtract)



@given(instance=sql_FunctionExtract_strategy)
def test_sql_functionextract_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=sql_ColumnOperand_strategy)
@settings(max_examples=50)
def test_sql_columnoperand_instantiation(instance):
    assert isinstance(instance, sql_ColumnOperand)



@given(instance=sql_ColumnOperand_strategy)
def test_sql_columnoperand_ora_setter(instance):
    original = instance.ora
    instance.ora = original
    assert instance.ora == original

@given(instance=Prms_strategy)
@settings(max_examples=50)
def test_prms_instantiation(instance):
    assert isinstance(instance, Prms)

@given(instance=sql_JRParameter_strategy)
@settings(max_examples=50)
def test_sql_jrparameter_instantiation(instance):
    assert isinstance(instance, sql_JRParameter)



@given(instance=sql_JRParameter_strategy)
def test_sql_jrparameter_jrprm_setter(instance):
    original = instance.jrprm
    instance.jrprm = original
    assert instance.jrprm == original

@given(instance=sql_OperandListGroup_strategy)
@settings(max_examples=50)
def test_sql_operandlistgroup_instantiation(instance):
    assert isinstance(instance, sql_OperandListGroup)

@given(instance=sql_POperand_strategy)
@settings(max_examples=50)
def test_sql_poperand_instantiation(instance):
    assert isinstance(instance, sql_POperand)



@given(instance=sql_POperand_strategy)
def test_sql_poperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql_OpFunctionCast_strategy)
@settings(max_examples=50)
def test_sql_opfunctioncast_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionCast)



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=sql_LikeOperand_strategy)
@settings(max_examples=50)
def test_sql_likeoperand_instantiation(instance):
    assert isinstance(instance, sql_LikeOperand)



@given(instance=sql_LikeOperand_strategy)
def test_sql_likeoperand_op2_setter(instance):
    original = instance.op2
    instance.op2 = original
    assert instance.op2 == original

@given(instance=OrExpr_strategy)
@settings(max_examples=50)
def test_orexpr_instantiation(instance):
    assert isinstance(instance, OrExpr)

@given(instance=sql_FullExpression_strategy)
@settings(max_examples=50)
def test_sql_fullexpression_instantiation(instance):
    assert isinstance(instance, sql_FullExpression)



@given(instance=sql_FullExpression_strategy)
def test_sql_fullexpression_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=sql_FullExpression_strategy)
def test_sql_fullexpression_notPrm_setter(instance):
    original = instance.notPrm
    instance.notPrm = original
    assert instance.notPrm == original



@given(instance=sql_FullExpression_strategy)
def test_sql_fullexpression_isnull_setter(instance):
    original = instance.isnull
    instance.isnull = original
    assert instance.isnull == original

@given(instance=sql_OpFunction_strategy)
@settings(max_examples=50)
def test_sql_opfunction_instantiation(instance):
    assert isinstance(instance, sql_OpFunction)



@given(instance=sql_OpFunction_strategy)
def test_sql_opfunction_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=sql_OpFunction_strategy)
def test_sql_opfunction_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=OrGroupByColumn_strategy)
@settings(max_examples=50)
def test_orgroupbycolumn_instantiation(instance):
    assert isinstance(instance, OrGroupByColumn)

@given(instance=sql_Prms_strategy)
@settings(max_examples=50)
def test_sql_prms_instantiation(instance):
    assert isinstance(instance, sql_Prms)

@given(instance=sql_Comparison_strategy)
@settings(max_examples=50)
def test_sql_comparison_instantiation(instance):
    assert isinstance(instance, sql_Comparison)



@given(instance=sql_Comparison_strategy)
def test_sql_comparison_subOperator_setter(instance):
    original = instance.subOperator
    instance.subOperator = original
    assert instance.subOperator == original



@given(instance=sql_Comparison_strategy)
def test_sql_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=sql_Like_strategy)
@settings(max_examples=50)
def test_sql_like_instantiation(instance):
    assert isinstance(instance, sql_Like)



@given(instance=sql_Like_strategy)
def test_sql_like_opLike_setter(instance):
    original = instance.opLike
    instance.opLike = original
    assert instance.opLike == original

@given(instance=sql_Between_strategy)
@settings(max_examples=50)
def test_sql_between_instantiation(instance):
    assert isinstance(instance, sql_Between)



@given(instance=sql_Between_strategy)
def test_sql_between_opBetween_setter(instance):
    original = instance.opBetween
    instance.opBetween = original
    assert instance.opBetween == original

@given(instance=sql_ExistsOper_strategy)
@settings(max_examples=50)
def test_sql_existsoper_instantiation(instance):
    assert isinstance(instance, sql_ExistsOper)



@given(instance=sql_ExistsOper_strategy)
def test_sql_existsoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql_InOper_strategy)
@settings(max_examples=50)
def test_sql_inoper_instantiation(instance):
    assert isinstance(instance, sql_InOper)



@given(instance=sql_InOper_strategy)
def test_sql_inoper_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sql_XExpr_strategy)
@settings(max_examples=50)
def test_sql_xexpr_instantiation(instance):
    assert isinstance(instance, sql_XExpr)



@given(instance=sql_XExpr_strategy)
def test_sql_xexpr_xf_setter(instance):
    original = instance.xf
    instance.xf = original
    assert instance.xf == original

@given(instance=sql_ExprGroup_strategy)
@settings(max_examples=50)
def test_sql_exprgroup_instantiation(instance):
    assert isinstance(instance, sql_ExprGroup)



@given(instance=sql_ExprGroup_strategy)
def test_sql_exprgroup_isnot_setter(instance):
    original = instance.isnot
    instance.isnot = original
    assert instance.isnot == original

@given(instance=sql_UnpivotInClauseArgs_strategy)
@settings(max_examples=50)
def test_sql_unpivotinclauseargs_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClauseArgs)

@given(instance=sql_PivotFunction_strategy)
@settings(max_examples=50)
def test_sql_pivotfunction_instantiation(instance):
    assert isinstance(instance, sql_PivotFunction)

@given(instance=sql_PivotInClause_strategy)
@settings(max_examples=50)
def test_sql_pivotinclause_instantiation(instance):
    assert isinstance(instance, sql_PivotInClause)



@given(instance=sql_PivotInClause_strategy)
def test_sql_pivotinclause_pinany_setter(instance):
    original = instance.pinany
    instance.pinany = original
    assert instance.pinany == original

@given(instance=sql_PivotForClause_strategy)
@settings(max_examples=50)
def test_sql_pivotforclause_instantiation(instance):
    assert isinstance(instance, sql_PivotForClause)

@given(instance=sql_GroupByColumnFull_strategy)
@settings(max_examples=50)
def test_sql_groupbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql_GroupByColumnFull)



@given(instance=sql_GroupByColumnFull_strategy)
def test_sql_groupbycolumnfull_grByInt_setter(instance):
    original = instance.grByInt
    instance.grByInt = original
    assert instance.grByInt == original

@given(instance=OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_ororderbycolumn_instantiation(instance):
    assert isinstance(instance, OrOrderByColumn)

@given(instance=sql_OrderByColumnFull_strategy)
@settings(max_examples=50)
def test_sql_orderbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql_OrderByColumnFull)



@given(instance=sql_OrderByColumnFull_strategy)
def test_sql_orderbycolumnfull_colOrderInt_setter(instance):
    original = instance.colOrderInt
    instance.colOrderInt = original
    assert instance.colOrderInt == original



@given(instance=sql_OrderByColumnFull_strategy)
def test_sql_orderbycolumnfull_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=TableFull_strategy)
@settings(max_examples=50)
def test_tablefull_instantiation(instance):
    assert isinstance(instance, TableFull)

@given(instance=sql_tbls_strategy)
@settings(max_examples=50)
def test_sql_tbls_instantiation(instance):
    assert isinstance(instance, sql_tbls)

@given(instance=PivotCol_strategy)
@settings(max_examples=50)
def test_pivotcol_instantiation(instance):
    assert isinstance(instance, PivotCol)

@given(instance=sql_pcols_strategy)
@settings(max_examples=50)
def test_sql_pcols_instantiation(instance):
    assert isinstance(instance, sql_pcols)

@given(instance=UsingCols_strategy)
@settings(max_examples=50)
def test_usingcols_instantiation(instance):
    assert isinstance(instance, UsingCols)

@given(instance=ColumnFull_strategy)
@settings(max_examples=50)
def test_columnfull_instantiation(instance):
    assert isinstance(instance, ColumnFull)

@given(instance=sql_Col_strategy)
@settings(max_examples=50)
def test_sql_col_instantiation(instance):
    assert isinstance(instance, sql_Col)

@given(instance=Pivots_strategy)
@settings(max_examples=50)
def test_pivots_instantiation(instance):
    assert isinstance(instance, Pivots)

@given(instance=sql_pvcs_strategy)
@settings(max_examples=50)
def test_sql_pvcs_instantiation(instance):
    assert isinstance(instance, sql_pvcs)

@given(instance=PivotFunction_strategy)
@settings(max_examples=50)
def test_pivotfunction_instantiation(instance):
    assert isinstance(instance, PivotFunction)

@given(instance=PivotColumns_strategy)
@settings(max_examples=50)
def test_pivotcolumns_instantiation(instance):
    assert isinstance(instance, PivotColumns)

@given(instance=sql_PivotCol_strategy)
@settings(max_examples=50)
def test_sql_pivotcol_instantiation(instance):
    assert isinstance(instance, sql_PivotCol)

@given(instance=sql_Pivots_strategy)
@settings(max_examples=50)
def test_sql_pivots_instantiation(instance):
    assert isinstance(instance, sql_Pivots)

@given(instance=UnpivotInClauseArgs_strategy)
@settings(max_examples=50)
def test_unpivotinclauseargs_instantiation(instance):
    assert isinstance(instance, UnpivotInClauseArgs)

@given(instance=sql_uicargs_strategy)
@settings(max_examples=50)
def test_sql_uicargs_instantiation(instance):
    assert isinstance(instance, sql_uicargs)

@given(instance=sql_UnpivotInClauseArg_strategy)
@settings(max_examples=50)
def test_sql_unpivotinclausearg_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClauseArg)

@given(instance=sql_UnpivotInClause_strategy)
@settings(max_examples=50)
def test_sql_unpivotinclause_instantiation(instance):
    assert isinstance(instance, sql_UnpivotInClause)

@given(instance=sql_PivotColumns_strategy)
@settings(max_examples=50)
def test_sql_pivotcolumns_instantiation(instance):
    assert isinstance(instance, sql_PivotColumns)

@given(instance=sql_UnpivotTable_strategy)
@settings(max_examples=50)
def test_sql_unpivottable_instantiation(instance):
    assert isinstance(instance, sql_UnpivotTable)

@given(instance=sql_PivotTable_strategy)
@settings(max_examples=50)
def test_sql_pivottable_instantiation(instance):
    assert isinstance(instance, sql_PivotTable)

@given(instance=sql_FromValues_strategy)
@settings(max_examples=50)
def test_sql_fromvalues_instantiation(instance):
    assert isinstance(instance, sql_FromValues)

@given(instance=sql_SubQueryOperand_strategy)
@settings(max_examples=50)
def test_sql_subqueryoperand_instantiation(instance):
    assert isinstance(instance, sql_SubQueryOperand)

@given(instance=sql_TableFull_strategy)
@settings(max_examples=50)
def test_sql_tablefull_instantiation(instance):
    assert isinstance(instance, sql_TableFull)

@given(instance=WithColumns_strategy)
@settings(max_examples=50)
def test_withcolumns_instantiation(instance):
    assert isinstance(instance, WithColumns)

@given(instance=sql_UsingCols_strategy)
@settings(max_examples=50)
def test_sql_usingcols_instantiation(instance):
    assert isinstance(instance, sql_UsingCols)

@given(instance=sql_JoinCondition_strategy)
@settings(max_examples=50)
def test_sql_joincondition_instantiation(instance):
    assert isinstance(instance, sql_JoinCondition)

@given(instance=sql_PivotFunctions_strategy)
@settings(max_examples=50)
def test_sql_pivotfunctions_instantiation(instance):
    assert isinstance(instance, sql_PivotFunctions)



@given(instance=sql_PivotFunctions_strategy)
def test_sql_pivotfunctions_abc_setter(instance):
    original = instance.abc
    instance.abc = original
    assert instance.abc == original

@given(instance=RowValues_strategy)
@settings(max_examples=50)
def test_rowvalues_instantiation(instance):
    assert isinstance(instance, RowValues)

@given(instance=sql_RowValue_strategy)
@settings(max_examples=50)
def test_sql_rowvalue_instantiation(instance):
    assert isinstance(instance, sql_RowValue)



@given(instance=sql_RowValue_strategy)
def test_sql_rowvalue_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=sql_RowValues_strategy)
@settings(max_examples=50)
def test_sql_rowvalues_instantiation(instance):
    assert isinstance(instance, sql_RowValues)

@given(instance=Rows_strategy)
@settings(max_examples=50)
def test_rows_instantiation(instance):
    assert isinstance(instance, Rows)

@given(instance=sql_Row_strategy)
@settings(max_examples=50)
def test_sql_row_instantiation(instance):
    assert isinstance(instance, sql_Row)

@given(instance=sql_Rows_strategy)
@settings(max_examples=50)
def test_sql_rows_instantiation(instance):
    assert isinstance(instance, sql_Rows)

@given(instance=FromValuesColumnNames_strategy)
@settings(max_examples=50)
def test_fromvaluescolumnnames_instantiation(instance):
    assert isinstance(instance, FromValuesColumnNames)

@given(instance=sql_abc_strategy)
@settings(max_examples=50)
def test_sql_abc_instantiation(instance):
    assert isinstance(instance, sql_abc)

@given(instance=sql_ColumnNames_strategy)
@settings(max_examples=50)
def test_sql_columnnames_instantiation(instance):
    assert isinstance(instance, sql_ColumnNames)



@given(instance=sql_ColumnNames_strategy)
def test_sql_columnnames_colName_setter(instance):
    original = instance.colName
    instance.colName = original
    assert instance.colName == original

@given(instance=sql_FromValuesColumnNames_strategy)
@settings(max_examples=50)
def test_sql_fromvaluescolumnnames_instantiation(instance):
    assert isinstance(instance, sql_FromValuesColumnNames)

@given(instance=sql_FromValuesColumns_strategy)
@settings(max_examples=50)
def test_sql_fromvaluescolumns_instantiation(instance):
    assert isinstance(instance, sql_FromValuesColumns)

@given(instance=sql_Values_strategy)
@settings(max_examples=50)
def test_sql_values_instantiation(instance):
    assert isinstance(instance, sql_Values)

@given(instance=sql_OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_sql_ororderbycolumn_instantiation(instance):
    assert isinstance(instance, sql_OrOrderByColumn)

@given(instance=sql_OrGroupByColumn_strategy)
@settings(max_examples=50)
def test_sql_orgroupbycolumn_instantiation(instance):
    assert isinstance(instance, sql_OrGroupByColumn)

@given(instance=sql_OrExpr_strategy)
@settings(max_examples=50)
def test_sql_orexpr_instantiation(instance):
    assert isinstance(instance, sql_OrExpr)

@given(instance=sql_OrTable_strategy)
@settings(max_examples=50)
def test_sql_ortable_instantiation(instance):
    assert isinstance(instance, sql_OrTable)

@given(instance=sql_FromTableJoin_strategy)
@settings(max_examples=50)
def test_sql_fromtablejoin_instantiation(instance):
    assert isinstance(instance, sql_FromTableJoin)



@given(instance=sql_FromTableJoin_strategy)
def test_sql_fromtablejoin_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=sql_TableOrAlias_strategy)
@settings(max_examples=50)
def test_sql_tableoralias_instantiation(instance):
    assert isinstance(instance, sql_TableOrAlias)



@given(instance=sql_TableOrAlias_strategy)
def test_sql_tableoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=OrTable_strategy)
@settings(max_examples=50)
def test_ortable_instantiation(instance):
    assert isinstance(instance, OrTable)

@given(instance=sql_FromTable_strategy)
@settings(max_examples=50)
def test_sql_fromtable_instantiation(instance):
    assert isinstance(instance, sql_FromTable)

@given(instance=sql_DbObjectNameAll_strategy)
@settings(max_examples=50)
def test_sql_dbobjectnameall_instantiation(instance):
    assert isinstance(instance, sql_DbObjectNameAll)



@given(instance=sql_DbObjectNameAll_strategy)
def test_sql_dbobjectnameall_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original

@given(instance=sql_DbObjectName_strategy)
@settings(max_examples=50)
def test_sql_dbobjectname_instantiation(instance):
    assert isinstance(instance, sql_DbObjectName)



@given(instance=sql_DbObjectName_strategy)
def test_sql_dbobjectname_dbname_setter(instance):
    original = instance.dbname
    instance.dbname = original
    assert instance.dbname == original

@given(instance=sql_Operands_strategy)
@settings(max_examples=50)
def test_sql_operands_instantiation(instance):
    assert isinstance(instance, sql_Operands)

@given(instance=OrColumn_strategy)
@settings(max_examples=50)
def test_orcolumn_instantiation(instance):
    assert isinstance(instance, OrColumn)

@given(instance=sql_ColumnOrAlias_strategy)
@settings(max_examples=50)
def test_sql_columnoralias_instantiation(instance):
    assert isinstance(instance, sql_ColumnOrAlias)



@given(instance=sql_ColumnOrAlias_strategy)
def test_sql_columnoralias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=sql_ColumnOrAlias_strategy)
def test_sql_columnoralias_allCols_setter(instance):
    original = instance.allCols
    instance.allCols = original
    assert instance.allCols == original

@given(instance=PivotForClause_strategy)
@settings(max_examples=50)
def test_pivotforclause_instantiation(instance):
    assert isinstance(instance, PivotForClause)

@given(instance=sql_ColumnFull_strategy)
@settings(max_examples=50)
def test_sql_columnfull_instantiation(instance):
    assert isinstance(instance, sql_ColumnFull)

@given(instance=sql_OrColumn_strategy)
@settings(max_examples=50)
def test_sql_orcolumn_instantiation(instance):
    assert isinstance(instance, sql_OrColumn)

@given(instance=sql_Model_strategy)
@settings(max_examples=50)
def test_sql_model_instantiation(instance):
    assert isinstance(instance, sql_Model)

@given(instance=SelectQuery_strategy)
@settings(max_examples=50)
def test_selectquery_instantiation(instance):
    assert isinstance(instance, SelectQuery)

@given(instance=sql_Select_strategy)
@settings(max_examples=50)
def test_sql_select_instantiation(instance):
    assert isinstance(instance, sql_Select)



@given(instance=sql_Select_strategy)
def test_sql_select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=sql_SelectSubSet_strategy)
@settings(max_examples=50)
def test_sql_selectsubset_instantiation(instance):
    assert isinstance(instance, sql_SelectSubSet)



@given(instance=sql_SelectSubSet_strategy)
def test_sql_selectsubset_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=sql_SelectSubSet_strategy)
def test_sql_selectsubset_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=sql_Limit_strategy)
@settings(max_examples=50)
def test_sql_limit_instantiation(instance):
    assert isinstance(instance, sql_Limit)



@given(instance=sql_Limit_strategy)
def test_sql_limit_l2_setter(instance):
    original = instance.l2
    instance.l2 = original
    assert instance.l2 == original



@given(instance=sql_Limit_strategy)
def test_sql_limit_l1_setter(instance):
    original = instance.l1
    instance.l1 = original
    assert instance.l1 == original

@given(instance=sql_Offset_strategy)
@settings(max_examples=50)
def test_sql_offset_instantiation(instance):
    assert isinstance(instance, sql_Offset)



@given(instance=sql_Offset_strategy)
def test_sql_offset_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=sql_UnsignedValue_strategy)
@settings(max_examples=50)
def test_sql_unsignedvalue_instantiation(instance):
    assert isinstance(instance, sql_UnsignedValue)



@given(instance=sql_UnsignedValue_strategy)
def test_sql_unsignedvalue_integer_setter(instance):
    original = instance.integer
    instance.integer = original
    assert instance.integer == original

@given(instance=sql_FetchFirst_strategy)
@settings(max_examples=50)
def test_sql_fetchfirst_instantiation(instance):
    assert isinstance(instance, sql_FetchFirst)



@given(instance=sql_FetchFirst_strategy)
def test_sql_fetchfirst_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original

@given(instance=sql_WithColumns_strategy)
@settings(max_examples=50)
def test_sql_withcolumns_instantiation(instance):
    assert isinstance(instance, sql_WithColumns)

@given(instance=sql_SelectQuery_strategy)
@settings(max_examples=50)
def test_sql_selectquery_instantiation(instance):
    assert isinstance(instance, sql_SelectQuery)

@given(instance=sql_WithQuery_strategy)
@settings(max_examples=50)
def test_sql_withquery_instantiation(instance):
    assert isinstance(instance, sql_WithQuery)



@given(instance=sql_WithQuery_strategy)
def test_sql_withquery_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original



@given(instance=sql_WithQuery_strategy)
def test_sql_withquery_wname_setter(instance):
    original = instance.wname
    instance.wname = original
    assert instance.wname == original
