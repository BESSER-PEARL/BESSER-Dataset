import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AccessControl,
    smc_Covered,
    smc_BellLapadula,
    Expression,
    smc_PlusOrMinus,
    smc_Equality,
    smc_BooleanLiteral,
    smc_IntLiteral,
    smc_List,
    smc_StringLiteral,
    smc_DateLiteral,
    smc_DoubleLiteral,
    smc_Dict,
    smc_VariableRef,
    smc_Comparison,
    smc_Or,
    smc_Not,
    smc_MulOrDiv,
    smc_And,
    smc_TimeLiteral,
    smc_Tuple,
    Download,
    smc_Client,
    smc_Database,
    AbstractAssignment,
    smc_Download,
    Computation,
    smc_Median,
    smc_Average,
    smc_Count,
    smc_WeightedAvg,
    smc_Multiplication,
    Functions,
    smc_BloomFilter,
    smc_CheckTable,
    smc_AccessControl,
    smc_AddValues,
    smc_CreateTable,
    smc_Search,
    smc_Computation,
    smc_Functions,
    smc_Expression,
    smc_Invocation,
    Command,
    smc_InvocationVoid,
    smc_IfThenElse,
    smc_Return,
    smc_Block,
    smc_Print,
    smc_While,
    smc_ParamDecl,
    smc_VariableAssignment,
    smc_AbstractAssignment,
    smc_VariableDecl,
    smc_Smc,
    smc_Command,
    smc_MainSMC,
    smc_BlockSMC,
    BlockType,
    SecType,
    BasicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(AccessControl)


def test_accesscontrol_constructor_exists():
    assert callable(AccessControl.__init__)


def test_accesscontrol_constructor_args():
    sig = inspect.signature(AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_smc_covered_is_not_abstract():
    assert not inspect.isabstract(smc_Covered)


def test_smc_covered_constructor_exists():
    assert callable(smc_Covered.__init__)


def test_smc_covered_constructor_args():
    sig = inspect.signature(smc_Covered.__init__)
    params = list(sig.parameters.keys())



def test_smc_belllapadula_is_not_abstract():
    assert not inspect.isabstract(smc_BellLapadula)


def test_smc_belllapadula_constructor_exists():
    assert callable(smc_BellLapadula.__init__)


def test_smc_belllapadula_constructor_args():
    sig = inspect.signature(smc_BellLapadula.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_smc_belllapadula_has_mode():
    assert hasattr(smc_BellLapadula, "mode")
    descriptor = None
    for klass in smc_BellLapadula.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_smc_plusorminus_is_not_abstract():
    assert not inspect.isabstract(smc_PlusOrMinus)


def test_smc_plusorminus_constructor_exists():
    assert callable(smc_PlusOrMinus.__init__)


def test_smc_plusorminus_constructor_args():
    sig = inspect.signature(smc_PlusOrMinus.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc_plusorminus_has_op():
    assert hasattr(smc_PlusOrMinus, "op")
    descriptor = None
    for klass in smc_PlusOrMinus.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc_equality_is_not_abstract():
    assert not inspect.isabstract(smc_Equality)


def test_smc_equality_constructor_exists():
    assert callable(smc_Equality.__init__)


def test_smc_equality_constructor_args():
    sig = inspect.signature(smc_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc_equality_has_op():
    assert hasattr(smc_Equality, "op")
    descriptor = None
    for klass in smc_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(smc_BooleanLiteral)


def test_smc_booleanliteral_constructor_exists():
    assert callable(smc_BooleanLiteral.__init__)


def test_smc_booleanliteral_constructor_args():
    sig = inspect.signature(smc_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_booleanliteral_has_value():
    assert hasattr(smc_BooleanLiteral, "value")
    descriptor = None
    for klass in smc_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_intliteral_is_not_abstract():
    assert not inspect.isabstract(smc_IntLiteral)


def test_smc_intliteral_constructor_exists():
    assert callable(smc_IntLiteral.__init__)


def test_smc_intliteral_constructor_args():
    sig = inspect.signature(smc_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_intliteral_has_value():
    assert hasattr(smc_IntLiteral, "value")
    descriptor = None
    for klass in smc_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_list_is_not_abstract():
    assert not inspect.isabstract(smc_List)


def test_smc_list_constructor_exists():
    assert callable(smc_List.__init__)


def test_smc_list_constructor_args():
    sig = inspect.signature(smc_List.__init__)
    params = list(sig.parameters.keys())



def test_smc_stringliteral_is_not_abstract():
    assert not inspect.isabstract(smc_StringLiteral)


def test_smc_stringliteral_constructor_exists():
    assert callable(smc_StringLiteral.__init__)


def test_smc_stringliteral_constructor_args():
    sig = inspect.signature(smc_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_stringliteral_has_value():
    assert hasattr(smc_StringLiteral, "value")
    descriptor = None
    for klass in smc_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_dateliteral_is_not_abstract():
    assert not inspect.isabstract(smc_DateLiteral)


def test_smc_dateliteral_constructor_exists():
    assert callable(smc_DateLiteral.__init__)


def test_smc_dateliteral_constructor_args():
    sig = inspect.signature(smc_DateLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_dateliteral_has_value():
    assert hasattr(smc_DateLiteral, "value")
    descriptor = None
    for klass in smc_DateLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(smc_DoubleLiteral)


def test_smc_doubleliteral_constructor_exists():
    assert callable(smc_DoubleLiteral.__init__)


def test_smc_doubleliteral_constructor_args():
    sig = inspect.signature(smc_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_doubleliteral_has_value():
    assert hasattr(smc_DoubleLiteral, "value")
    descriptor = None
    for klass in smc_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_dict_is_not_abstract():
    assert not inspect.isabstract(smc_Dict)


def test_smc_dict_constructor_exists():
    assert callable(smc_Dict.__init__)


def test_smc_dict_constructor_args():
    sig = inspect.signature(smc_Dict.__init__)
    params = list(sig.parameters.keys())



def test_smc_variableref_is_not_abstract():
    assert not inspect.isabstract(smc_VariableRef)


def test_smc_variableref_constructor_exists():
    assert callable(smc_VariableRef.__init__)


def test_smc_variableref_constructor_args():
    sig = inspect.signature(smc_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_smc_comparison_is_not_abstract():
    assert not inspect.isabstract(smc_Comparison)


def test_smc_comparison_constructor_exists():
    assert callable(smc_Comparison.__init__)


def test_smc_comparison_constructor_args():
    sig = inspect.signature(smc_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc_comparison_has_op():
    assert hasattr(smc_Comparison, "op")
    descriptor = None
    for klass in smc_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc_or_is_not_abstract():
    assert not inspect.isabstract(smc_Or)


def test_smc_or_constructor_exists():
    assert callable(smc_Or.__init__)


def test_smc_or_constructor_args():
    sig = inspect.signature(smc_Or.__init__)
    params = list(sig.parameters.keys())



def test_smc_not_is_not_abstract():
    assert not inspect.isabstract(smc_Not)


def test_smc_not_constructor_exists():
    assert callable(smc_Not.__init__)


def test_smc_not_constructor_args():
    sig = inspect.signature(smc_Not.__init__)
    params = list(sig.parameters.keys())



def test_smc_mulordiv_is_not_abstract():
    assert not inspect.isabstract(smc_MulOrDiv)


def test_smc_mulordiv_constructor_exists():
    assert callable(smc_MulOrDiv.__init__)


def test_smc_mulordiv_constructor_args():
    sig = inspect.signature(smc_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_smc_mulordiv_has_op():
    assert hasattr(smc_MulOrDiv, "op")
    descriptor = None
    for klass in smc_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_smc_and_is_not_abstract():
    assert not inspect.isabstract(smc_And)


def test_smc_and_constructor_exists():
    assert callable(smc_And.__init__)


def test_smc_and_constructor_args():
    sig = inspect.signature(smc_And.__init__)
    params = list(sig.parameters.keys())



def test_smc_timeliteral_is_not_abstract():
    assert not inspect.isabstract(smc_TimeLiteral)


def test_smc_timeliteral_constructor_exists():
    assert callable(smc_TimeLiteral.__init__)


def test_smc_timeliteral_constructor_args():
    sig = inspect.signature(smc_TimeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smc_timeliteral_has_value():
    assert hasattr(smc_TimeLiteral, "value")
    descriptor = None
    for klass in smc_TimeLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smc_tuple_is_not_abstract():
    assert not inspect.isabstract(smc_Tuple)


def test_smc_tuple_constructor_exists():
    assert callable(smc_Tuple.__init__)


def test_smc_tuple_constructor_args():
    sig = inspect.signature(smc_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_download_is_not_abstract():
    assert not inspect.isabstract(Download)


def test_download_constructor_exists():
    assert callable(Download.__init__)


def test_download_constructor_args():
    sig = inspect.signature(Download.__init__)
    params = list(sig.parameters.keys())



def test_smc_client_is_not_abstract():
    assert not inspect.isabstract(smc_Client)


def test_smc_client_constructor_exists():
    assert callable(smc_Client.__init__)


def test_smc_client_constructor_args():
    sig = inspect.signature(smc_Client.__init__)
    params = list(sig.parameters.keys())
    assert "arg" in params, "Missing parameter 'arg'"

def test_smc_client_has_arg():
    assert hasattr(smc_Client, "arg")
    descriptor = None
    for klass in smc_Client.__mro__:
        if "arg" in klass.__dict__:
            descriptor = klass.__dict__["arg"]
            break
    assert isinstance(descriptor, property)



def test_smc_database_is_not_abstract():
    assert not inspect.isabstract(smc_Database)


def test_smc_database_constructor_exists():
    assert callable(smc_Database.__init__)


def test_smc_database_constructor_args():
    sig = inspect.signature(smc_Database.__init__)
    params = list(sig.parameters.keys())
    assert "clm" in params, "Missing parameter 'clm'"

def test_smc_database_has_clm():
    assert hasattr(smc_Database, "clm")
    descriptor = None
    for klass in smc_Database.__mro__:
        if "clm" in klass.__dict__:
            descriptor = klass.__dict__["clm"]
            break
    assert isinstance(descriptor, property)



def test_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(AbstractAssignment)


def test_abstractassignment_constructor_exists():
    assert callable(AbstractAssignment.__init__)


def test_abstractassignment_constructor_args():
    sig = inspect.signature(AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc_download_is_not_abstract():
    assert not inspect.isabstract(smc_Download)


def test_smc_download_constructor_exists():
    assert callable(smc_Download.__init__)


def test_smc_download_constructor_args():
    sig = inspect.signature(smc_Download.__init__)
    params = list(sig.parameters.keys())



def test_computation_is_not_abstract():
    assert not inspect.isabstract(Computation)


def test_computation_constructor_exists():
    assert callable(Computation.__init__)


def test_computation_constructor_args():
    sig = inspect.signature(Computation.__init__)
    params = list(sig.parameters.keys())



def test_smc_median_is_not_abstract():
    assert not inspect.isabstract(smc_Median)


def test_smc_median_constructor_exists():
    assert callable(smc_Median.__init__)


def test_smc_median_constructor_args():
    sig = inspect.signature(smc_Median.__init__)
    params = list(sig.parameters.keys())



def test_smc_average_is_not_abstract():
    assert not inspect.isabstract(smc_Average)


def test_smc_average_constructor_exists():
    assert callable(smc_Average.__init__)


def test_smc_average_constructor_args():
    sig = inspect.signature(smc_Average.__init__)
    params = list(sig.parameters.keys())



def test_smc_count_is_not_abstract():
    assert not inspect.isabstract(smc_Count)


def test_smc_count_constructor_exists():
    assert callable(smc_Count.__init__)


def test_smc_count_constructor_args():
    sig = inspect.signature(smc_Count.__init__)
    params = list(sig.parameters.keys())



def test_smc_weightedavg_is_not_abstract():
    assert not inspect.isabstract(smc_WeightedAvg)


def test_smc_weightedavg_constructor_exists():
    assert callable(smc_WeightedAvg.__init__)


def test_smc_weightedavg_constructor_args():
    sig = inspect.signature(smc_WeightedAvg.__init__)
    params = list(sig.parameters.keys())



def test_smc_multiplication_is_not_abstract():
    assert not inspect.isabstract(smc_Multiplication)


def test_smc_multiplication_constructor_exists():
    assert callable(smc_Multiplication.__init__)


def test_smc_multiplication_constructor_args():
    sig = inspect.signature(smc_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_functions_is_not_abstract():
    assert not inspect.isabstract(Functions)


def test_functions_constructor_exists():
    assert callable(Functions.__init__)


def test_functions_constructor_args():
    sig = inspect.signature(Functions.__init__)
    params = list(sig.parameters.keys())



def test_smc_bloomfilter_is_not_abstract():
    assert not inspect.isabstract(smc_BloomFilter)


def test_smc_bloomfilter_constructor_exists():
    assert callable(smc_BloomFilter.__init__)


def test_smc_bloomfilter_constructor_args():
    sig = inspect.signature(smc_BloomFilter.__init__)
    params = list(sig.parameters.keys())



def test_smc_checktable_is_not_abstract():
    assert not inspect.isabstract(smc_CheckTable)


def test_smc_checktable_constructor_exists():
    assert callable(smc_CheckTable.__init__)


def test_smc_checktable_constructor_args():
    sig = inspect.signature(smc_CheckTable.__init__)
    params = list(sig.parameters.keys())



def test_smc_accesscontrol_is_not_abstract():
    assert not inspect.isabstract(smc_AccessControl)


def test_smc_accesscontrol_constructor_exists():
    assert callable(smc_AccessControl.__init__)


def test_smc_accesscontrol_constructor_args():
    sig = inspect.signature(smc_AccessControl.__init__)
    params = list(sig.parameters.keys())



def test_smc_addvalues_is_not_abstract():
    assert not inspect.isabstract(smc_AddValues)


def test_smc_addvalues_constructor_exists():
    assert callable(smc_AddValues.__init__)


def test_smc_addvalues_constructor_args():
    sig = inspect.signature(smc_AddValues.__init__)
    params = list(sig.parameters.keys())



def test_smc_createtable_is_not_abstract():
    assert not inspect.isabstract(smc_CreateTable)


def test_smc_createtable_constructor_exists():
    assert callable(smc_CreateTable.__init__)


def test_smc_createtable_constructor_args():
    sig = inspect.signature(smc_CreateTable.__init__)
    params = list(sig.parameters.keys())



def test_smc_search_is_not_abstract():
    assert not inspect.isabstract(smc_Search)


def test_smc_search_constructor_exists():
    assert callable(smc_Search.__init__)


def test_smc_search_constructor_args():
    sig = inspect.signature(smc_Search.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_smc_search_has_column():
    assert hasattr(smc_Search, "column")
    descriptor = None
    for klass in smc_Search.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_smc_computation_is_not_abstract():
    assert not inspect.isabstract(smc_Computation)


def test_smc_computation_constructor_exists():
    assert callable(smc_Computation.__init__)


def test_smc_computation_constructor_args():
    sig = inspect.signature(smc_Computation.__init__)
    params = list(sig.parameters.keys())



def test_smc_functions_is_not_abstract():
    assert not inspect.isabstract(smc_Functions)


def test_smc_functions_constructor_exists():
    assert callable(smc_Functions.__init__)


def test_smc_functions_constructor_args():
    sig = inspect.signature(smc_Functions.__init__)
    params = list(sig.parameters.keys())



def test_smc_expression_is_not_abstract():
    assert not inspect.isabstract(smc_Expression)


def test_smc_expression_constructor_exists():
    assert callable(smc_Expression.__init__)


def test_smc_expression_constructor_args():
    sig = inspect.signature(smc_Expression.__init__)
    params = list(sig.parameters.keys())



def test_smc_invocation_is_not_abstract():
    assert not inspect.isabstract(smc_Invocation)


def test_smc_invocation_constructor_exists():
    assert callable(smc_Invocation.__init__)


def test_smc_invocation_constructor_args():
    sig = inspect.signature(smc_Invocation.__init__)
    params = list(sig.parameters.keys())



def test_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_command_constructor_exists():
    assert callable(Command.__init__)


def test_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_smc_invocationvoid_is_not_abstract():
    assert not inspect.isabstract(smc_InvocationVoid)


def test_smc_invocationvoid_constructor_exists():
    assert callable(smc_InvocationVoid.__init__)


def test_smc_invocationvoid_constructor_args():
    sig = inspect.signature(smc_InvocationVoid.__init__)
    params = list(sig.parameters.keys())



def test_smc_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(smc_IfThenElse)


def test_smc_ifthenelse_constructor_exists():
    assert callable(smc_IfThenElse.__init__)


def test_smc_ifthenelse_constructor_args():
    sig = inspect.signature(smc_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_smc_return_is_not_abstract():
    assert not inspect.isabstract(smc_Return)


def test_smc_return_constructor_exists():
    assert callable(smc_Return.__init__)


def test_smc_return_constructor_args():
    sig = inspect.signature(smc_Return.__init__)
    params = list(sig.parameters.keys())



def test_smc_block_is_not_abstract():
    assert not inspect.isabstract(smc_Block)


def test_smc_block_constructor_exists():
    assert callable(smc_Block.__init__)


def test_smc_block_constructor_args():
    sig = inspect.signature(smc_Block.__init__)
    params = list(sig.parameters.keys())



def test_smc_print_is_not_abstract():
    assert not inspect.isabstract(smc_Print)


def test_smc_print_constructor_exists():
    assert callable(smc_Print.__init__)


def test_smc_print_constructor_args():
    sig = inspect.signature(smc_Print.__init__)
    params = list(sig.parameters.keys())



def test_smc_while_is_not_abstract():
    assert not inspect.isabstract(smc_While)


def test_smc_while_constructor_exists():
    assert callable(smc_While.__init__)


def test_smc_while_constructor_args():
    sig = inspect.signature(smc_While.__init__)
    params = list(sig.parameters.keys())



def test_smc_paramdecl_is_not_abstract():
    assert not inspect.isabstract(smc_ParamDecl)


def test_smc_paramdecl_constructor_exists():
    assert callable(smc_ParamDecl.__init__)


def test_smc_paramdecl_constructor_args():
    sig = inspect.signature(smc_ParamDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "parName" in params, "Missing parameter 'parName'"
    assert "btype" in params, "Missing parameter 'btype'"
    assert "stype" in params, "Missing parameter 'stype'"

def test_smc_paramdecl_has_name():
    assert hasattr(smc_ParamDecl, "name")
    descriptor = None
    for klass in smc_ParamDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc_paramdecl_has_parName():
    assert hasattr(smc_ParamDecl, "parName")
    descriptor = None
    for klass in smc_ParamDecl.__mro__:
        if "parName" in klass.__dict__:
            descriptor = klass.__dict__["parName"]
            break
    assert isinstance(descriptor, property)

def test_smc_paramdecl_has_btype():
    assert hasattr(smc_ParamDecl, "btype")
    descriptor = None
    for klass in smc_ParamDecl.__mro__:
        if "btype" in klass.__dict__:
            descriptor = klass.__dict__["btype"]
            break
    assert isinstance(descriptor, property)

def test_smc_paramdecl_has_stype():
    assert hasattr(smc_ParamDecl, "stype")
    descriptor = None
    for klass in smc_ParamDecl.__mro__:
        if "stype" in klass.__dict__:
            descriptor = klass.__dict__["stype"]
            break
    assert isinstance(descriptor, property)



def test_smc_variableassignment_is_not_abstract():
    assert not inspect.isabstract(smc_VariableAssignment)


def test_smc_variableassignment_constructor_exists():
    assert callable(smc_VariableAssignment.__init__)


def test_smc_variableassignment_constructor_args():
    sig = inspect.signature(smc_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc_abstractassignment_is_not_abstract():
    assert not inspect.isabstract(smc_AbstractAssignment)


def test_smc_abstractassignment_constructor_exists():
    assert callable(smc_AbstractAssignment.__init__)


def test_smc_abstractassignment_constructor_args():
    sig = inspect.signature(smc_AbstractAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smc_variabledecl_is_not_abstract():
    assert not inspect.isabstract(smc_VariableDecl)


def test_smc_variabledecl_constructor_exists():
    assert callable(smc_VariableDecl.__init__)


def test_smc_variabledecl_constructor_args():
    sig = inspect.signature(smc_VariableDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "length" in params, "Missing parameter 'length'"
    assert "type" in params, "Missing parameter 'type'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "array" in params, "Missing parameter 'array'"

def test_smc_variabledecl_has_name():
    assert hasattr(smc_VariableDecl, "name")
    descriptor = None
    for klass in smc_VariableDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc_variabledecl_has_length():
    assert hasattr(smc_VariableDecl, "length")
    descriptor = None
    for klass in smc_VariableDecl.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_smc_variabledecl_has_type():
    assert hasattr(smc_VariableDecl, "type")
    descriptor = None
    for klass in smc_VariableDecl.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_smc_variabledecl_has_visibility():
    assert hasattr(smc_VariableDecl, "visibility")
    descriptor = None
    for klass in smc_VariableDecl.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_smc_variabledecl_has_array():
    assert hasattr(smc_VariableDecl, "array")
    descriptor = None
    for klass in smc_VariableDecl.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_smc_smc_is_not_abstract():
    assert not inspect.isabstract(smc_Smc)


def test_smc_smc_constructor_exists():
    assert callable(smc_Smc.__init__)


def test_smc_smc_constructor_args():
    sig = inspect.signature(smc_Smc.__init__)
    params = list(sig.parameters.keys())



def test_smc_command_is_not_abstract():
    assert not inspect.isabstract(smc_Command)


def test_smc_command_constructor_exists():
    assert callable(smc_Command.__init__)


def test_smc_command_constructor_args():
    sig = inspect.signature(smc_Command.__init__)
    params = list(sig.parameters.keys())



def test_smc_mainsmc_is_not_abstract():
    assert not inspect.isabstract(smc_MainSMC)


def test_smc_mainsmc_constructor_exists():
    assert callable(smc_MainSMC.__init__)


def test_smc_mainsmc_constructor_args():
    sig = inspect.signature(smc_MainSMC.__init__)
    params = list(sig.parameters.keys())



def test_smc_blocksmc_is_not_abstract():
    assert not inspect.isabstract(smc_BlockSMC)


def test_smc_blocksmc_constructor_exists():
    assert callable(smc_BlockSMC.__init__)


def test_smc_blocksmc_constructor_args():
    sig = inspect.signature(smc_BlockSMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_smc_blocksmc_has_name():
    assert hasattr(smc_BlockSMC, "name")
    descriptor = None
    for klass in smc_BlockSMC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smc_blocksmc_has_type():
    assert hasattr(smc_BlockSMC, "type")
    descriptor = None
    for klass in smc_BlockSMC.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_blocktype_exists():
    # Check that the Enumeration exists
    assert BlockType is not None

def test_blocktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BlockType]
    expected_literals = [
        "INSERT",
        "ANONYMIZATION",
        "COMP",
        "ACCESS",
        "PERMISSION",
        "SEARCH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BlockType"

def test_sectype_exists():
    # Check that the Enumeration exists
    assert SecType is not None

def test_sectype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SecType]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SecType"

def test_basictype_exists():
    # Check that the Enumeration exists
    assert BasicType is not None

def test_basictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicType]
    expected_literals = [
        "BOOLEAN",
        "DOUBLE",
        "ENCRYPTED",
        "STRING",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicType"


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
AccessControl_strategy = st.builds(
    AccessControl,
)
smc_Covered_strategy = st.builds(
    smc_Covered,
)
smc_BellLapadula_strategy = st.builds(
    smc_BellLapadula,
    mode=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
smc_PlusOrMinus_strategy = st.builds(
    smc_PlusOrMinus,
    op=
        safe_text
)
smc_Equality_strategy = st.builds(
    smc_Equality,
    op=
        safe_text
)
smc_BooleanLiteral_strategy = st.builds(
    smc_BooleanLiteral,
    value=
        st.booleans()
)
smc_IntLiteral_strategy = st.builds(
    smc_IntLiteral,
    value=
        st.integers()
)
smc_List_strategy = st.builds(
    smc_List,
)
smc_StringLiteral_strategy = st.builds(
    smc_StringLiteral,
    value=
        safe_text
)
smc_DateLiteral_strategy = st.builds(
    smc_DateLiteral,
    value=
        safe_text
)
smc_DoubleLiteral_strategy = st.builds(
    smc_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
smc_Dict_strategy = st.builds(
    smc_Dict,
)
smc_VariableRef_strategy = st.builds(
    smc_VariableRef,
)
smc_Comparison_strategy = st.builds(
    smc_Comparison,
    op=
        safe_text
)
smc_Or_strategy = st.builds(
    smc_Or,
)
smc_Not_strategy = st.builds(
    smc_Not,
)
smc_MulOrDiv_strategy = st.builds(
    smc_MulOrDiv,
    op=
        safe_text
)
smc_And_strategy = st.builds(
    smc_And,
)
smc_TimeLiteral_strategy = st.builds(
    smc_TimeLiteral,
    value=
        safe_text
)
smc_Tuple_strategy = st.builds(
    smc_Tuple,
)
Download_strategy = st.builds(
    Download,
)
smc_Client_strategy = st.builds(
    smc_Client,
    arg=
        safe_text
)
smc_Database_strategy = st.builds(
    smc_Database,
    clm=
        safe_text
)
AbstractAssignment_strategy = st.builds(
    AbstractAssignment,
)
smc_Download_strategy = st.builds(
    smc_Download,
)
Computation_strategy = st.builds(
    Computation,
)
smc_Median_strategy = st.builds(
    smc_Median,
)
smc_Average_strategy = st.builds(
    smc_Average,
)
smc_Count_strategy = st.builds(
    smc_Count,
)
smc_WeightedAvg_strategy = st.builds(
    smc_WeightedAvg,
)
smc_Multiplication_strategy = st.builds(
    smc_Multiplication,
)
Functions_strategy = st.builds(
    Functions,
)
smc_BloomFilter_strategy = st.builds(
    smc_BloomFilter,
)
smc_CheckTable_strategy = st.builds(
    smc_CheckTable,
)
smc_AccessControl_strategy = st.builds(
    smc_AccessControl,
)
smc_AddValues_strategy = st.builds(
    smc_AddValues,
)
smc_CreateTable_strategy = st.builds(
    smc_CreateTable,
)
smc_Search_strategy = st.builds(
    smc_Search,
    column=
        safe_text
)
smc_Computation_strategy = st.builds(
    smc_Computation,
)
smc_Functions_strategy = st.builds(
    smc_Functions,
)
smc_Expression_strategy = st.builds(
    smc_Expression,
)
smc_Invocation_strategy = st.builds(
    smc_Invocation,
)
Command_strategy = st.builds(
    Command,
)
smc_InvocationVoid_strategy = st.builds(
    smc_InvocationVoid,
)
smc_IfThenElse_strategy = st.builds(
    smc_IfThenElse,
)
smc_Return_strategy = st.builds(
    smc_Return,
)
smc_Block_strategy = st.builds(
    smc_Block,
)
smc_Print_strategy = st.builds(
    smc_Print,
)
smc_While_strategy = st.builds(
    smc_While,
)
smc_ParamDecl_strategy = st.builds(
    smc_ParamDecl,
    name=
        safe_text,
    parName=
        safe_text,
    btype=
        safe_text,
    stype=
        safe_text
)
smc_VariableAssignment_strategy = st.builds(
    smc_VariableAssignment,
)
smc_AbstractAssignment_strategy = st.builds(
    smc_AbstractAssignment,
)
smc_VariableDecl_strategy = st.builds(
    smc_VariableDecl,
    name=
        safe_text,
    length=
        st.integers(),
    type=
        safe_text,
    visibility=
        safe_text,
    array=
        st.booleans()
)
smc_Smc_strategy = st.builds(
    smc_Smc,
)
smc_Command_strategy = st.builds(
    smc_Command,
)
smc_MainSMC_strategy = st.builds(
    smc_MainSMC,
)
smc_BlockSMC_strategy = st.builds(
    smc_BlockSMC,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=AccessControl_strategy)
@settings(max_examples=50)
def test_accesscontrol_instantiation(instance):
    assert isinstance(instance, AccessControl)

@given(instance=smc_Covered_strategy)
@settings(max_examples=50)
def test_smc_covered_instantiation(instance):
    assert isinstance(instance, smc_Covered)

@given(instance=smc_BellLapadula_strategy)
@settings(max_examples=50)
def test_smc_belllapadula_instantiation(instance):
    assert isinstance(instance, smc_BellLapadula)



@given(instance=smc_BellLapadula_strategy)
def test_smc_belllapadula_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=smc_PlusOrMinus_strategy)
@settings(max_examples=50)
def test_smc_plusorminus_instantiation(instance):
    assert isinstance(instance, smc_PlusOrMinus)



@given(instance=smc_PlusOrMinus_strategy)
def test_smc_plusorminus_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc_Equality_strategy)
@settings(max_examples=50)
def test_smc_equality_instantiation(instance):
    assert isinstance(instance, smc_Equality)



@given(instance=smc_Equality_strategy)
def test_smc_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_smc_booleanliteral_instantiation(instance):
    assert isinstance(instance, smc_BooleanLiteral)



@given(instance=smc_BooleanLiteral_strategy)
def test_smc_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_IntLiteral_strategy)
@settings(max_examples=50)
def test_smc_intliteral_instantiation(instance):
    assert isinstance(instance, smc_IntLiteral)



@given(instance=smc_IntLiteral_strategy)
def test_smc_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_List_strategy)
@settings(max_examples=50)
def test_smc_list_instantiation(instance):
    assert isinstance(instance, smc_List)

@given(instance=smc_StringLiteral_strategy)
@settings(max_examples=50)
def test_smc_stringliteral_instantiation(instance):
    assert isinstance(instance, smc_StringLiteral)



@given(instance=smc_StringLiteral_strategy)
def test_smc_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_DateLiteral_strategy)
@settings(max_examples=50)
def test_smc_dateliteral_instantiation(instance):
    assert isinstance(instance, smc_DateLiteral)



@given(instance=smc_DateLiteral_strategy)
def test_smc_dateliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_smc_doubleliteral_instantiation(instance):
    assert isinstance(instance, smc_DoubleLiteral)



@given(instance=smc_DoubleLiteral_strategy)
def test_smc_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_Dict_strategy)
@settings(max_examples=50)
def test_smc_dict_instantiation(instance):
    assert isinstance(instance, smc_Dict)

@given(instance=smc_VariableRef_strategy)
@settings(max_examples=50)
def test_smc_variableref_instantiation(instance):
    assert isinstance(instance, smc_VariableRef)

@given(instance=smc_Comparison_strategy)
@settings(max_examples=50)
def test_smc_comparison_instantiation(instance):
    assert isinstance(instance, smc_Comparison)



@given(instance=smc_Comparison_strategy)
def test_smc_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc_Or_strategy)
@settings(max_examples=50)
def test_smc_or_instantiation(instance):
    assert isinstance(instance, smc_Or)

@given(instance=smc_Not_strategy)
@settings(max_examples=50)
def test_smc_not_instantiation(instance):
    assert isinstance(instance, smc_Not)

@given(instance=smc_MulOrDiv_strategy)
@settings(max_examples=50)
def test_smc_mulordiv_instantiation(instance):
    assert isinstance(instance, smc_MulOrDiv)



@given(instance=smc_MulOrDiv_strategy)
def test_smc_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=smc_And_strategy)
@settings(max_examples=50)
def test_smc_and_instantiation(instance):
    assert isinstance(instance, smc_And)

@given(instance=smc_TimeLiteral_strategy)
@settings(max_examples=50)
def test_smc_timeliteral_instantiation(instance):
    assert isinstance(instance, smc_TimeLiteral)



@given(instance=smc_TimeLiteral_strategy)
def test_smc_timeliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smc_Tuple_strategy)
@settings(max_examples=50)
def test_smc_tuple_instantiation(instance):
    assert isinstance(instance, smc_Tuple)

@given(instance=Download_strategy)
@settings(max_examples=50)
def test_download_instantiation(instance):
    assert isinstance(instance, Download)

@given(instance=smc_Client_strategy)
@settings(max_examples=50)
def test_smc_client_instantiation(instance):
    assert isinstance(instance, smc_Client)



@given(instance=smc_Client_strategy)
def test_smc_client_arg_setter(instance):
    original = instance.arg
    instance.arg = original
    assert instance.arg == original

@given(instance=smc_Database_strategy)
@settings(max_examples=50)
def test_smc_database_instantiation(instance):
    assert isinstance(instance, smc_Database)



@given(instance=smc_Database_strategy)
def test_smc_database_clm_setter(instance):
    original = instance.clm
    instance.clm = original
    assert instance.clm == original

@given(instance=AbstractAssignment_strategy)
@settings(max_examples=50)
def test_abstractassignment_instantiation(instance):
    assert isinstance(instance, AbstractAssignment)

@given(instance=smc_Download_strategy)
@settings(max_examples=50)
def test_smc_download_instantiation(instance):
    assert isinstance(instance, smc_Download)

@given(instance=Computation_strategy)
@settings(max_examples=50)
def test_computation_instantiation(instance):
    assert isinstance(instance, Computation)

@given(instance=smc_Median_strategy)
@settings(max_examples=50)
def test_smc_median_instantiation(instance):
    assert isinstance(instance, smc_Median)

@given(instance=smc_Average_strategy)
@settings(max_examples=50)
def test_smc_average_instantiation(instance):
    assert isinstance(instance, smc_Average)

@given(instance=smc_Count_strategy)
@settings(max_examples=50)
def test_smc_count_instantiation(instance):
    assert isinstance(instance, smc_Count)

@given(instance=smc_WeightedAvg_strategy)
@settings(max_examples=50)
def test_smc_weightedavg_instantiation(instance):
    assert isinstance(instance, smc_WeightedAvg)

@given(instance=smc_Multiplication_strategy)
@settings(max_examples=50)
def test_smc_multiplication_instantiation(instance):
    assert isinstance(instance, smc_Multiplication)

@given(instance=Functions_strategy)
@settings(max_examples=50)
def test_functions_instantiation(instance):
    assert isinstance(instance, Functions)

@given(instance=smc_BloomFilter_strategy)
@settings(max_examples=50)
def test_smc_bloomfilter_instantiation(instance):
    assert isinstance(instance, smc_BloomFilter)

@given(instance=smc_CheckTable_strategy)
@settings(max_examples=50)
def test_smc_checktable_instantiation(instance):
    assert isinstance(instance, smc_CheckTable)

@given(instance=smc_AccessControl_strategy)
@settings(max_examples=50)
def test_smc_accesscontrol_instantiation(instance):
    assert isinstance(instance, smc_AccessControl)

@given(instance=smc_AddValues_strategy)
@settings(max_examples=50)
def test_smc_addvalues_instantiation(instance):
    assert isinstance(instance, smc_AddValues)

@given(instance=smc_CreateTable_strategy)
@settings(max_examples=50)
def test_smc_createtable_instantiation(instance):
    assert isinstance(instance, smc_CreateTable)

@given(instance=smc_Search_strategy)
@settings(max_examples=50)
def test_smc_search_instantiation(instance):
    assert isinstance(instance, smc_Search)



@given(instance=smc_Search_strategy)
def test_smc_search_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=smc_Computation_strategy)
@settings(max_examples=50)
def test_smc_computation_instantiation(instance):
    assert isinstance(instance, smc_Computation)

@given(instance=smc_Functions_strategy)
@settings(max_examples=50)
def test_smc_functions_instantiation(instance):
    assert isinstance(instance, smc_Functions)

@given(instance=smc_Expression_strategy)
@settings(max_examples=50)
def test_smc_expression_instantiation(instance):
    assert isinstance(instance, smc_Expression)

@given(instance=smc_Invocation_strategy)
@settings(max_examples=50)
def test_smc_invocation_instantiation(instance):
    assert isinstance(instance, smc_Invocation)

@given(instance=Command_strategy)
@settings(max_examples=50)
def test_command_instantiation(instance):
    assert isinstance(instance, Command)

@given(instance=smc_InvocationVoid_strategy)
@settings(max_examples=50)
def test_smc_invocationvoid_instantiation(instance):
    assert isinstance(instance, smc_InvocationVoid)

@given(instance=smc_IfThenElse_strategy)
@settings(max_examples=50)
def test_smc_ifthenelse_instantiation(instance):
    assert isinstance(instance, smc_IfThenElse)

@given(instance=smc_Return_strategy)
@settings(max_examples=50)
def test_smc_return_instantiation(instance):
    assert isinstance(instance, smc_Return)

@given(instance=smc_Block_strategy)
@settings(max_examples=50)
def test_smc_block_instantiation(instance):
    assert isinstance(instance, smc_Block)

@given(instance=smc_Print_strategy)
@settings(max_examples=50)
def test_smc_print_instantiation(instance):
    assert isinstance(instance, smc_Print)

@given(instance=smc_While_strategy)
@settings(max_examples=50)
def test_smc_while_instantiation(instance):
    assert isinstance(instance, smc_While)

@given(instance=smc_ParamDecl_strategy)
@settings(max_examples=50)
def test_smc_paramdecl_instantiation(instance):
    assert isinstance(instance, smc_ParamDecl)



@given(instance=smc_ParamDecl_strategy)
def test_smc_paramdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_ParamDecl_strategy)
def test_smc_paramdecl_parName_setter(instance):
    original = instance.parName
    instance.parName = original
    assert instance.parName == original



@given(instance=smc_ParamDecl_strategy)
def test_smc_paramdecl_btype_setter(instance):
    original = instance.btype
    instance.btype = original
    assert instance.btype == original



@given(instance=smc_ParamDecl_strategy)
def test_smc_paramdecl_stype_setter(instance):
    original = instance.stype
    instance.stype = original
    assert instance.stype == original

@given(instance=smc_VariableAssignment_strategy)
@settings(max_examples=50)
def test_smc_variableassignment_instantiation(instance):
    assert isinstance(instance, smc_VariableAssignment)

@given(instance=smc_AbstractAssignment_strategy)
@settings(max_examples=50)
def test_smc_abstractassignment_instantiation(instance):
    assert isinstance(instance, smc_AbstractAssignment)

@given(instance=smc_VariableDecl_strategy)
@settings(max_examples=50)
def test_smc_variabledecl_instantiation(instance):
    assert isinstance(instance, smc_VariableDecl)



@given(instance=smc_VariableDecl_strategy)
def test_smc_variabledecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_VariableDecl_strategy)
def test_smc_variabledecl_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=smc_VariableDecl_strategy)
def test_smc_variabledecl_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=smc_VariableDecl_strategy)
def test_smc_variabledecl_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=smc_VariableDecl_strategy)
def test_smc_variabledecl_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=smc_Smc_strategy)
@settings(max_examples=50)
def test_smc_smc_instantiation(instance):
    assert isinstance(instance, smc_Smc)

@given(instance=smc_Command_strategy)
@settings(max_examples=50)
def test_smc_command_instantiation(instance):
    assert isinstance(instance, smc_Command)

@given(instance=smc_MainSMC_strategy)
@settings(max_examples=50)
def test_smc_mainsmc_instantiation(instance):
    assert isinstance(instance, smc_MainSMC)

@given(instance=smc_BlockSMC_strategy)
@settings(max_examples=50)
def test_smc_blocksmc_instantiation(instance):
    assert isinstance(instance, smc_BlockSMC)



@given(instance=smc_BlockSMC_strategy)
def test_smc_blocksmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smc_BlockSMC_strategy)
def test_smc_blocksmc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
