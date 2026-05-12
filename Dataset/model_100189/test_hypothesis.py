import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ColumnFull,
    sql_SubQueryOperand,
    sql_TableFull,
    sql_FromTableJoin,
    sql_TableOrAlias,
    OrTable,
    sql_FromTable,
    sql_ColumnFull,
    sql_OrOrderByColumn,
    OrColumn,
    sql_ColumnOrAlias,
    sql_OrGroupByColumn,
    sql_OrExpr,
    sql_OrTable,
    sql_OrColumn,
    SelectQuery,
    sql_Select,
    sql_SelectSubSet,
    sql_SelectQuery,
    sql_Model,
    Operands,
    sql_Minus,
    sql_Concat,
    sql_Star,
    sql_Div,
    sql_Plus,
    sql_Col,
    OperandList,
    sql_OpList,
    SQLCaseWhens,
    sql_WhenList,
    sql_SqlCaseWhen,
    sql_SQLCaseWhens,
    sql_OpFunctionArgAgregate,
    OpFunctionArg,
    sql_OpFList,
    sql_OpFunctionArgOperand,
    sql_SQLCaseOperand,
    sql_OpFunctionArg,
    sql_ScalarOperand,
    sql_ExpOperand,
    sql_POperand,
    sql_ColumnOperand,
    sql_OpFunctionCast,
    sql_Operand,
    sql_OpFunction,
    OpFunctionArgAgregate,
    sql_Operands,
    sql_LikeOperand,
    sql_OperandList,
    Prms,
    sql_JRParameter,
    sql_Prms,
    sql_Like,
    sql_Between,
    sql_InOper,
    sql_XExpr,
    sql_Comparison,
    OrGroupByColumn,
    OrExpr,
    sql_ExprGroup,
    sql_FullExpression,
    TableFull,
    sql_tbls,
    sql_GroupByColumnFull,
    OrOrderByColumn,
    sql_OrderByColumnFull,
    sql_DbObjectNameAll,
    sql_DbObjectName,
    XFunction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_columnfull_is_not_abstract():
    assert not inspect.isabstract(ColumnFull)


def test_columnfull_constructor_exists():
    assert callable(ColumnFull.__init__)


def test_columnfull_constructor_args():
    sig = inspect.signature(ColumnFull.__init__)
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



def test_sql_columnfull_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnFull)


def test_sql_columnfull_constructor_exists():
    assert callable(sql_ColumnFull.__init__)


def test_sql_columnfull_constructor_args():
    sig = inspect.signature(sql_ColumnFull.__init__)
    params = list(sig.parameters.keys())



def test_sql_ororderbycolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrOrderByColumn)


def test_sql_ororderbycolumn_constructor_exists():
    assert callable(sql_OrOrderByColumn.__init__)


def test_sql_ororderbycolumn_constructor_args():
    sig = inspect.signature(sql_OrOrderByColumn.__init__)
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



def test_sql_orcolumn_is_not_abstract():
    assert not inspect.isabstract(sql_OrColumn)


def test_sql_orcolumn_constructor_exists():
    assert callable(sql_OrColumn.__init__)


def test_sql_orcolumn_constructor_args():
    sig = inspect.signature(sql_OrColumn.__init__)
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



def test_sql_selectquery_is_not_abstract():
    assert not inspect.isabstract(sql_SelectQuery)


def test_sql_selectquery_constructor_exists():
    assert callable(sql_SelectQuery.__init__)


def test_sql_selectquery_constructor_args():
    sig = inspect.signature(sql_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sql_model_is_not_abstract():
    assert not inspect.isabstract(sql_Model)


def test_sql_model_constructor_exists():
    assert callable(sql_Model.__init__)


def test_sql_model_constructor_args():
    sig = inspect.signature(sql_Model.__init__)
    params = list(sig.parameters.keys())



def test_operands_is_not_abstract():
    assert not inspect.isabstract(Operands)


def test_operands_constructor_exists():
    assert callable(Operands.__init__)


def test_operands_constructor_args():
    sig = inspect.signature(Operands.__init__)
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



def test_sql_star_is_not_abstract():
    assert not inspect.isabstract(sql_Star)


def test_sql_star_constructor_exists():
    assert callable(sql_Star.__init__)


def test_sql_star_constructor_args():
    sig = inspect.signature(sql_Star.__init__)
    params = list(sig.parameters.keys())



def test_sql_div_is_not_abstract():
    assert not inspect.isabstract(sql_Div)


def test_sql_div_constructor_exists():
    assert callable(sql_Div.__init__)


def test_sql_div_constructor_args():
    sig = inspect.signature(sql_Div.__init__)
    params = list(sig.parameters.keys())



def test_sql_plus_is_not_abstract():
    assert not inspect.isabstract(sql_Plus)


def test_sql_plus_constructor_exists():
    assert callable(sql_Plus.__init__)


def test_sql_plus_constructor_args():
    sig = inspect.signature(sql_Plus.__init__)
    params = list(sig.parameters.keys())



def test_sql_col_is_not_abstract():
    assert not inspect.isabstract(sql_Col)


def test_sql_col_constructor_exists():
    assert callable(sql_Col.__init__)


def test_sql_col_constructor_args():
    sig = inspect.signature(sql_Col.__init__)
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



def test_sql_sqlcaseoperand_is_not_abstract():
    assert not inspect.isabstract(sql_SQLCaseOperand)


def test_sql_sqlcaseoperand_constructor_exists():
    assert callable(sql_SQLCaseOperand.__init__)


def test_sql_sqlcaseoperand_constructor_args():
    sig = inspect.signature(sql_SQLCaseOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql_opfunctionarg_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionArg)


def test_sql_opfunctionarg_constructor_exists():
    assert callable(sql_OpFunctionArg.__init__)


def test_sql_opfunctionarg_constructor_args():
    sig = inspect.signature(sql_OpFunctionArg.__init__)
    params = list(sig.parameters.keys())



def test_sql_scalaroperand_is_not_abstract():
    assert not inspect.isabstract(sql_ScalarOperand)


def test_sql_scalaroperand_constructor_exists():
    assert callable(sql_ScalarOperand.__init__)


def test_sql_scalaroperand_constructor_args():
    sig = inspect.signature(sql_ScalarOperand.__init__)
    params = list(sig.parameters.keys())
    assert "sodt" in params, "Missing parameter 'sodt'"
    assert "sostr" in params, "Missing parameter 'sostr'"
    assert "sodbl" in params, "Missing parameter 'sodbl'"
    assert "soint" in params, "Missing parameter 'soint'"
    assert "sotime" in params, "Missing parameter 'sotime'"
    assert "sodate" in params, "Missing parameter 'sodate'"

def test_sql_scalaroperand_has_sodt():
    assert hasattr(sql_ScalarOperand, "sodt")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sodt" in klass.__dict__:
            descriptor = klass.__dict__["sodt"]
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

def test_sql_scalaroperand_has_sotime():
    assert hasattr(sql_ScalarOperand, "sotime")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sotime" in klass.__dict__:
            descriptor = klass.__dict__["sotime"]
            break
    assert isinstance(descriptor, property)

def test_sql_scalaroperand_has_sodate():
    assert hasattr(sql_ScalarOperand, "sodate")
    descriptor = None
    for klass in sql_ScalarOperand.__mro__:
        if "sodate" in klass.__dict__:
            descriptor = klass.__dict__["sodate"]
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



def test_sql_columnoperand_is_not_abstract():
    assert not inspect.isabstract(sql_ColumnOperand)


def test_sql_columnoperand_constructor_exists():
    assert callable(sql_ColumnOperand.__init__)


def test_sql_columnoperand_constructor_args():
    sig = inspect.signature(sql_ColumnOperand.__init__)
    params = list(sig.parameters.keys())



def test_sql_opfunctioncast_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunctionCast)


def test_sql_opfunctioncast_constructor_exists():
    assert callable(sql_OpFunctionCast.__init__)


def test_sql_opfunctioncast_constructor_args():
    sig = inspect.signature(sql_OpFunctionCast.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "p" in params, "Missing parameter 'p'"
    assert "p2" in params, "Missing parameter 'p2'"

def test_sql_opfunctioncast_has_type():
    assert hasattr(sql_OpFunctionCast, "type")
    descriptor = None
    for klass in sql_OpFunctionCast.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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

def test_sql_opfunctioncast_has_p2():
    assert hasattr(sql_OpFunctionCast, "p2")
    descriptor = None
    for klass in sql_OpFunctionCast.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)



def test_sql_operand_is_not_abstract():
    assert not inspect.isabstract(sql_Operand)


def test_sql_operand_constructor_exists():
    assert callable(sql_Operand.__init__)


def test_sql_operand_constructor_args():
    sig = inspect.signature(sql_Operand.__init__)
    params = list(sig.parameters.keys())



def test_sql_opfunction_is_not_abstract():
    assert not inspect.isabstract(sql_OpFunction)


def test_sql_opfunction_constructor_exists():
    assert callable(sql_OpFunction.__init__)


def test_sql_opfunction_constructor_args():
    sig = inspect.signature(sql_OpFunction.__init__)
    params = list(sig.parameters.keys())
    assert "fname" in params, "Missing parameter 'fname'"

def test_sql_opfunction_has_fname():
    assert hasattr(sql_OpFunction, "fname")
    descriptor = None
    for klass in sql_OpFunction.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)



def test_opfunctionargagregate_is_not_abstract():
    assert not inspect.isabstract(OpFunctionArgAgregate)


def test_opfunctionargagregate_constructor_exists():
    assert callable(OpFunctionArgAgregate.__init__)


def test_opfunctionargagregate_constructor_args():
    sig = inspect.signature(OpFunctionArgAgregate.__init__)
    params = list(sig.parameters.keys())



def test_sql_operands_is_not_abstract():
    assert not inspect.isabstract(sql_Operands)


def test_sql_operands_constructor_exists():
    assert callable(sql_Operands.__init__)


def test_sql_operands_constructor_args():
    sig = inspect.signature(sql_Operands.__init__)
    params = list(sig.parameters.keys())



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



def test_sql_operandlist_is_not_abstract():
    assert not inspect.isabstract(sql_OperandList)


def test_sql_operandlist_constructor_exists():
    assert callable(sql_OperandList.__init__)


def test_sql_operandlist_constructor_args():
    sig = inspect.signature(sql_OperandList.__init__)
    params = list(sig.parameters.keys())



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



def test_sql_prms_is_not_abstract():
    assert not inspect.isabstract(sql_Prms)


def test_sql_prms_constructor_exists():
    assert callable(sql_Prms.__init__)


def test_sql_prms_constructor_args():
    sig = inspect.signature(sql_Prms.__init__)
    params = list(sig.parameters.keys())



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



def test_sql_comparison_is_not_abstract():
    assert not inspect.isabstract(sql_Comparison)


def test_sql_comparison_constructor_exists():
    assert callable(sql_Comparison.__init__)


def test_sql_comparison_constructor_args():
    sig = inspect.signature(sql_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "subOperator" in params, "Missing parameter 'subOperator'"

def test_sql_comparison_has_operator():
    assert hasattr(sql_Comparison, "operator")
    descriptor = None
    for klass in sql_Comparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_sql_comparison_has_subOperator():
    assert hasattr(sql_Comparison, "subOperator")
    descriptor = None
    for klass in sql_Comparison.__mro__:
        if "subOperator" in klass.__dict__:
            descriptor = klass.__dict__["subOperator"]
            break
    assert isinstance(descriptor, property)



def test_orgroupbycolumn_is_not_abstract():
    assert not inspect.isabstract(OrGroupByColumn)


def test_orgroupbycolumn_constructor_exists():
    assert callable(OrGroupByColumn.__init__)


def test_orgroupbycolumn_constructor_args():
    sig = inspect.signature(OrGroupByColumn.__init__)
    params = list(sig.parameters.keys())



def test_orexpr_is_not_abstract():
    assert not inspect.isabstract(OrExpr)


def test_orexpr_constructor_exists():
    assert callable(OrExpr.__init__)


def test_orexpr_constructor_args():
    sig = inspect.signature(OrExpr.__init__)
    params = list(sig.parameters.keys())



def test_sql_exprgroup_is_not_abstract():
    assert not inspect.isabstract(sql_ExprGroup)


def test_sql_exprgroup_constructor_exists():
    assert callable(sql_ExprGroup.__init__)


def test_sql_exprgroup_constructor_args():
    sig = inspect.signature(sql_ExprGroup.__init__)
    params = list(sig.parameters.keys())



def test_sql_fullexpression_is_not_abstract():
    assert not inspect.isabstract(sql_FullExpression)


def test_sql_fullexpression_constructor_exists():
    assert callable(sql_FullExpression.__init__)


def test_sql_fullexpression_constructor_args():
    sig = inspect.signature(sql_FullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isnull" in params, "Missing parameter 'isnull'"
    assert "c" in params, "Missing parameter 'c'"
    assert "notPrm" in params, "Missing parameter 'notPrm'"

def test_sql_fullexpression_has_isnull():
    assert hasattr(sql_FullExpression, "isnull")
    descriptor = None
    for klass in sql_FullExpression.__mro__:
        if "isnull" in klass.__dict__:
            descriptor = klass.__dict__["isnull"]
            break
    assert isinstance(descriptor, property)

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



def test_sql_groupbycolumnfull_is_not_abstract():
    assert not inspect.isabstract(sql_GroupByColumnFull)


def test_sql_groupbycolumnfull_constructor_exists():
    assert callable(sql_GroupByColumnFull.__init__)


def test_sql_groupbycolumnfull_constructor_args():
    sig = inspect.signature(sql_GroupByColumnFull.__init__)
    params = list(sig.parameters.keys())



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
    assert "direction" in params, "Missing parameter 'direction'"
    assert "colOrderInt" in params, "Missing parameter 'colOrderInt'"

def test_sql_orderbycolumnfull_has_direction():
    assert hasattr(sql_OrderByColumnFull, "direction")
    descriptor = None
    for klass in sql_OrderByColumnFull.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_sql_orderbycolumnfull_has_colOrderInt():
    assert hasattr(sql_OrderByColumnFull, "colOrderInt")
    descriptor = None
    for klass in sql_OrderByColumnFull.__mro__:
        if "colOrderInt" in klass.__dict__:
            descriptor = klass.__dict__["colOrderInt"]
            break
    assert isinstance(descriptor, property)



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

def test_xfunction_exists():
    # Check that the Enumeration exists
    assert XFunction is not None

def test_xfunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in XFunction]
    expected_literals = [
        "xnoteq",
        "xbwn",
        "xnotin",
        "xeq",
        "xls",
        "xbwnl",
        "xgt",
        "xgtl",
        "xbwnr",
        "xlsr",
        "xin",
        "xbwnc",
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
ColumnFull_strategy = st.builds(
    ColumnFull,
)
sql_SubQueryOperand_strategy = st.builds(
    sql_SubQueryOperand,
)
sql_TableFull_strategy = st.builds(
    sql_TableFull,
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
sql_ColumnFull_strategy = st.builds(
    sql_ColumnFull,
)
sql_OrOrderByColumn_strategy = st.builds(
    sql_OrOrderByColumn,
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
sql_OrGroupByColumn_strategy = st.builds(
    sql_OrGroupByColumn,
)
sql_OrExpr_strategy = st.builds(
    sql_OrExpr,
)
sql_OrTable_strategy = st.builds(
    sql_OrTable,
)
sql_OrColumn_strategy = st.builds(
    sql_OrColumn,
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
sql_SelectQuery_strategy = st.builds(
    sql_SelectQuery,
)
sql_Model_strategy = st.builds(
    sql_Model,
)
Operands_strategy = st.builds(
    Operands,
)
sql_Minus_strategy = st.builds(
    sql_Minus,
)
sql_Concat_strategy = st.builds(
    sql_Concat,
)
sql_Star_strategy = st.builds(
    sql_Star,
)
sql_Div_strategy = st.builds(
    sql_Div,
)
sql_Plus_strategy = st.builds(
    sql_Plus,
)
sql_Col_strategy = st.builds(
    sql_Col,
)
OperandList_strategy = st.builds(
    OperandList,
)
sql_OpList_strategy = st.builds(
    sql_OpList,
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
sql_SQLCaseOperand_strategy = st.builds(
    sql_SQLCaseOperand,
)
sql_OpFunctionArg_strategy = st.builds(
    sql_OpFunctionArg,
)
sql_ScalarOperand_strategy = st.builds(
    sql_ScalarOperand,
    sodt=
        st.dates(),
    sostr=
        safe_text,
    sodbl=
        safe_text,
    soint=
        st.integers(),
    sotime=
        st.dates(),
    sodate=
        st.dates()
)
sql_ExpOperand_strategy = st.builds(
    sql_ExpOperand,
    prm=
        safe_text
)
sql_POperand_strategy = st.builds(
    sql_POperand,
    prm=
        safe_text
)
sql_ColumnOperand_strategy = st.builds(
    sql_ColumnOperand,
)
sql_OpFunctionCast_strategy = st.builds(
    sql_OpFunctionCast,
    type=
        safe_text,
    p=
        st.integers(),
    p2=
        st.integers()
)
sql_Operand_strategy = st.builds(
    sql_Operand,
)
sql_OpFunction_strategy = st.builds(
    sql_OpFunction,
    fname=
        safe_text
)
OpFunctionArgAgregate_strategy = st.builds(
    OpFunctionArgAgregate,
)
sql_Operands_strategy = st.builds(
    sql_Operands,
)
sql_LikeOperand_strategy = st.builds(
    sql_LikeOperand,
    op2=
        safe_text
)
sql_OperandList_strategy = st.builds(
    sql_OperandList,
)
Prms_strategy = st.builds(
    Prms,
)
sql_JRParameter_strategy = st.builds(
    sql_JRParameter,
    jrprm=
        safe_text
)
sql_Prms_strategy = st.builds(
    sql_Prms,
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
sql_Comparison_strategy = st.builds(
    sql_Comparison,
    operator=
        safe_text,
    subOperator=
        safe_text
)
OrGroupByColumn_strategy = st.builds(
    OrGroupByColumn,
)
OrExpr_strategy = st.builds(
    OrExpr,
)
sql_ExprGroup_strategy = st.builds(
    sql_ExprGroup,
)
sql_FullExpression_strategy = st.builds(
    sql_FullExpression,
    isnull=
        safe_text,
    c=
        safe_text,
    notPrm=
        safe_text
)
TableFull_strategy = st.builds(
    TableFull,
)
sql_tbls_strategy = st.builds(
    sql_tbls,
)
sql_GroupByColumnFull_strategy = st.builds(
    sql_GroupByColumnFull,
)
OrOrderByColumn_strategy = st.builds(
    OrOrderByColumn,
)
sql_OrderByColumnFull_strategy = st.builds(
    sql_OrderByColumnFull,
    direction=
        safe_text,
    colOrderInt=
        st.integers()
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

@given(instance=ColumnFull_strategy)
@settings(max_examples=50)
def test_columnfull_instantiation(instance):
    assert isinstance(instance, ColumnFull)

@given(instance=sql_SubQueryOperand_strategy)
@settings(max_examples=50)
def test_sql_subqueryoperand_instantiation(instance):
    assert isinstance(instance, sql_SubQueryOperand)

@given(instance=sql_TableFull_strategy)
@settings(max_examples=50)
def test_sql_tablefull_instantiation(instance):
    assert isinstance(instance, sql_TableFull)

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

@given(instance=sql_ColumnFull_strategy)
@settings(max_examples=50)
def test_sql_columnfull_instantiation(instance):
    assert isinstance(instance, sql_ColumnFull)

@given(instance=sql_OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_sql_ororderbycolumn_instantiation(instance):
    assert isinstance(instance, sql_OrOrderByColumn)

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

@given(instance=sql_OrColumn_strategy)
@settings(max_examples=50)
def test_sql_orcolumn_instantiation(instance):
    assert isinstance(instance, sql_OrColumn)

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

@given(instance=sql_SelectQuery_strategy)
@settings(max_examples=50)
def test_sql_selectquery_instantiation(instance):
    assert isinstance(instance, sql_SelectQuery)

@given(instance=sql_Model_strategy)
@settings(max_examples=50)
def test_sql_model_instantiation(instance):
    assert isinstance(instance, sql_Model)

@given(instance=Operands_strategy)
@settings(max_examples=50)
def test_operands_instantiation(instance):
    assert isinstance(instance, Operands)

@given(instance=sql_Minus_strategy)
@settings(max_examples=50)
def test_sql_minus_instantiation(instance):
    assert isinstance(instance, sql_Minus)

@given(instance=sql_Concat_strategy)
@settings(max_examples=50)
def test_sql_concat_instantiation(instance):
    assert isinstance(instance, sql_Concat)

@given(instance=sql_Star_strategy)
@settings(max_examples=50)
def test_sql_star_instantiation(instance):
    assert isinstance(instance, sql_Star)

@given(instance=sql_Div_strategy)
@settings(max_examples=50)
def test_sql_div_instantiation(instance):
    assert isinstance(instance, sql_Div)

@given(instance=sql_Plus_strategy)
@settings(max_examples=50)
def test_sql_plus_instantiation(instance):
    assert isinstance(instance, sql_Plus)

@given(instance=sql_Col_strategy)
@settings(max_examples=50)
def test_sql_col_instantiation(instance):
    assert isinstance(instance, sql_Col)

@given(instance=OperandList_strategy)
@settings(max_examples=50)
def test_operandlist_instantiation(instance):
    assert isinstance(instance, OperandList)

@given(instance=sql_OpList_strategy)
@settings(max_examples=50)
def test_sql_oplist_instantiation(instance):
    assert isinstance(instance, sql_OpList)

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

@given(instance=sql_SQLCaseOperand_strategy)
@settings(max_examples=50)
def test_sql_sqlcaseoperand_instantiation(instance):
    assert isinstance(instance, sql_SQLCaseOperand)

@given(instance=sql_OpFunctionArg_strategy)
@settings(max_examples=50)
def test_sql_opfunctionarg_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionArg)

@given(instance=sql_ScalarOperand_strategy)
@settings(max_examples=50)
def test_sql_scalaroperand_instantiation(instance):
    assert isinstance(instance, sql_ScalarOperand)



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sodt_setter(instance):
    original = instance.sodt
    instance.sodt = original
    assert instance.sodt == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sostr_setter(instance):
    original = instance.sostr
    instance.sostr = original
    assert instance.sostr == original



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
def test_sql_scalaroperand_sotime_setter(instance):
    original = instance.sotime
    instance.sotime = original
    assert instance.sotime == original



@given(instance=sql_ScalarOperand_strategy)
def test_sql_scalaroperand_sodate_setter(instance):
    original = instance.sodate
    instance.sodate = original
    assert instance.sodate == original

@given(instance=sql_ExpOperand_strategy)
@settings(max_examples=50)
def test_sql_expoperand_instantiation(instance):
    assert isinstance(instance, sql_ExpOperand)



@given(instance=sql_ExpOperand_strategy)
def test_sql_expoperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql_POperand_strategy)
@settings(max_examples=50)
def test_sql_poperand_instantiation(instance):
    assert isinstance(instance, sql_POperand)



@given(instance=sql_POperand_strategy)
def test_sql_poperand_prm_setter(instance):
    original = instance.prm
    instance.prm = original
    assert instance.prm == original

@given(instance=sql_ColumnOperand_strategy)
@settings(max_examples=50)
def test_sql_columnoperand_instantiation(instance):
    assert isinstance(instance, sql_ColumnOperand)

@given(instance=sql_OpFunctionCast_strategy)
@settings(max_examples=50)
def test_sql_opfunctioncast_instantiation(instance):
    assert isinstance(instance, sql_OpFunctionCast)



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original



@given(instance=sql_OpFunctionCast_strategy)
def test_sql_opfunctioncast_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original

@given(instance=sql_Operand_strategy)
@settings(max_examples=50)
def test_sql_operand_instantiation(instance):
    assert isinstance(instance, sql_Operand)

@given(instance=sql_OpFunction_strategy)
@settings(max_examples=50)
def test_sql_opfunction_instantiation(instance):
    assert isinstance(instance, sql_OpFunction)



@given(instance=sql_OpFunction_strategy)
def test_sql_opfunction_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original

@given(instance=OpFunctionArgAgregate_strategy)
@settings(max_examples=50)
def test_opfunctionargagregate_instantiation(instance):
    assert isinstance(instance, OpFunctionArgAgregate)

@given(instance=sql_Operands_strategy)
@settings(max_examples=50)
def test_sql_operands_instantiation(instance):
    assert isinstance(instance, sql_Operands)

@given(instance=sql_LikeOperand_strategy)
@settings(max_examples=50)
def test_sql_likeoperand_instantiation(instance):
    assert isinstance(instance, sql_LikeOperand)



@given(instance=sql_LikeOperand_strategy)
def test_sql_likeoperand_op2_setter(instance):
    original = instance.op2
    instance.op2 = original
    assert instance.op2 == original

@given(instance=sql_OperandList_strategy)
@settings(max_examples=50)
def test_sql_operandlist_instantiation(instance):
    assert isinstance(instance, sql_OperandList)

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

@given(instance=sql_Prms_strategy)
@settings(max_examples=50)
def test_sql_prms_instantiation(instance):
    assert isinstance(instance, sql_Prms)

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

@given(instance=sql_Comparison_strategy)
@settings(max_examples=50)
def test_sql_comparison_instantiation(instance):
    assert isinstance(instance, sql_Comparison)



@given(instance=sql_Comparison_strategy)
def test_sql_comparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=sql_Comparison_strategy)
def test_sql_comparison_subOperator_setter(instance):
    original = instance.subOperator
    instance.subOperator = original
    assert instance.subOperator == original

@given(instance=OrGroupByColumn_strategy)
@settings(max_examples=50)
def test_orgroupbycolumn_instantiation(instance):
    assert isinstance(instance, OrGroupByColumn)

@given(instance=OrExpr_strategy)
@settings(max_examples=50)
def test_orexpr_instantiation(instance):
    assert isinstance(instance, OrExpr)

@given(instance=sql_ExprGroup_strategy)
@settings(max_examples=50)
def test_sql_exprgroup_instantiation(instance):
    assert isinstance(instance, sql_ExprGroup)

@given(instance=sql_FullExpression_strategy)
@settings(max_examples=50)
def test_sql_fullexpression_instantiation(instance):
    assert isinstance(instance, sql_FullExpression)



@given(instance=sql_FullExpression_strategy)
def test_sql_fullexpression_isnull_setter(instance):
    original = instance.isnull
    instance.isnull = original
    assert instance.isnull == original



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

@given(instance=TableFull_strategy)
@settings(max_examples=50)
def test_tablefull_instantiation(instance):
    assert isinstance(instance, TableFull)

@given(instance=sql_tbls_strategy)
@settings(max_examples=50)
def test_sql_tbls_instantiation(instance):
    assert isinstance(instance, sql_tbls)

@given(instance=sql_GroupByColumnFull_strategy)
@settings(max_examples=50)
def test_sql_groupbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql_GroupByColumnFull)

@given(instance=OrOrderByColumn_strategy)
@settings(max_examples=50)
def test_ororderbycolumn_instantiation(instance):
    assert isinstance(instance, OrOrderByColumn)

@given(instance=sql_OrderByColumnFull_strategy)
@settings(max_examples=50)
def test_sql_orderbycolumnfull_instantiation(instance):
    assert isinstance(instance, sql_OrderByColumnFull)



@given(instance=sql_OrderByColumnFull_strategy)
def test_sql_orderbycolumnfull_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=sql_OrderByColumnFull_strategy)
def test_sql_orderbycolumnfull_colOrderInt_setter(instance):
    original = instance.colOrderInt
    instance.colOrderInt = original
    assert instance.colOrderInt == original

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
