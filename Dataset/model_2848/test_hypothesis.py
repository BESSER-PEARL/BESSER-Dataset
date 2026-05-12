import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    aDSL_IntegerNegative,
    Expression,
    aDSL_Plus,
    aDSL_Reference,
    aDSL_DeRef,
    aDSL_Or,
    aDSL_IntConstant,
    aDSL_Not,
    aDSL_Equality,
    aDSL_Comparison,
    aDSL_BoolConstant,
    aDSL_And,
    aDSL_This,
    aDSL_Init,
    aDSL_MulOrDiv,
    aDSL_New,
    aDSL_StringConstant,
    aDSL_MemberSelection,
    aDSL_Null,
    aDSL_Here,
    aDSL_Minus,
    aDSL_Assignment,
    aDSL_Block,
    aDSL_Statement,
    aDSL_VarDef,
    Statement,
    aDSL_IfStat,
    aDSL_Expression,
    aDSL_WhenStatement,
    aDSL_FinishStat,
    aDSL_For2Statement,
    aDSL_AtomicStatement,
    aDSL_AsyncStat,
    aDSL_ReturnStat,
    aDSL_ForStat,
    aDSL_TryCatchStat,
    aDSL_AtStat,
    aDSL_WhileStat,
    aDSL_Body,
    Member,
    aDSL_PrintInst,
    aDSL_MainMethod,
    SharedDef,
    aDSL_SharedVarDef,
    aDSL_SharedArrayDef,
    aDSL_Operator,
    aDSL_Method,
    aDSL_Member,
    VarDef,
    aDSL_VariableType,
    aDSL_FuncVarDef,
    aDSL_Parameter,
    aDSL_VariableDef,
    aDSL_SharedDef,
    aDSL_XClass,
    aDSL_AbstractElements,
    aDSL_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_adsl_integernegative_is_not_abstract():
    assert not inspect.isabstract(aDSL_IntegerNegative)


def test_adsl_integernegative_constructor_exists():
    assert callable(aDSL_IntegerNegative.__init__)


def test_adsl_integernegative_constructor_args():
    sig = inspect.signature(aDSL_IntegerNegative.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "isneg" in params, "Missing parameter 'isneg'"

def test_adsl_integernegative_has_value():
    assert hasattr(aDSL_IntegerNegative, "value")
    descriptor = None
    for klass in aDSL_IntegerNegative.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_adsl_integernegative_has_isneg():
    assert hasattr(aDSL_IntegerNegative, "isneg")
    descriptor = None
    for klass in aDSL_IntegerNegative.__mro__:
        if "isneg" in klass.__dict__:
            descriptor = klass.__dict__["isneg"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_adsl_plus_is_not_abstract():
    assert not inspect.isabstract(aDSL_Plus)


def test_adsl_plus_constructor_exists():
    assert callable(aDSL_Plus.__init__)


def test_adsl_plus_constructor_args():
    sig = inspect.signature(aDSL_Plus.__init__)
    params = list(sig.parameters.keys())



def test_adsl_reference_is_not_abstract():
    assert not inspect.isabstract(aDSL_Reference)


def test_adsl_reference_constructor_exists():
    assert callable(aDSL_Reference.__init__)


def test_adsl_reference_constructor_args():
    sig = inspect.signature(aDSL_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "isarray" in params, "Missing parameter 'isarray'"

def test_adsl_reference_has_isarray():
    assert hasattr(aDSL_Reference, "isarray")
    descriptor = None
    for klass in aDSL_Reference.__mro__:
        if "isarray" in klass.__dict__:
            descriptor = klass.__dict__["isarray"]
            break
    assert isinstance(descriptor, property)



def test_adsl_deref_is_not_abstract():
    assert not inspect.isabstract(aDSL_DeRef)


def test_adsl_deref_constructor_exists():
    assert callable(aDSL_DeRef.__init__)


def test_adsl_deref_constructor_args():
    sig = inspect.signature(aDSL_DeRef.__init__)
    params = list(sig.parameters.keys())



def test_adsl_or_is_not_abstract():
    assert not inspect.isabstract(aDSL_Or)


def test_adsl_or_constructor_exists():
    assert callable(aDSL_Or.__init__)


def test_adsl_or_constructor_args():
    sig = inspect.signature(aDSL_Or.__init__)
    params = list(sig.parameters.keys())



def test_adsl_intconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL_IntConstant)


def test_adsl_intconstant_constructor_exists():
    assert callable(aDSL_IntConstant.__init__)


def test_adsl_intconstant_constructor_args():
    sig = inspect.signature(aDSL_IntConstant.__init__)
    params = list(sig.parameters.keys())



def test_adsl_not_is_not_abstract():
    assert not inspect.isabstract(aDSL_Not)


def test_adsl_not_constructor_exists():
    assert callable(aDSL_Not.__init__)


def test_adsl_not_constructor_args():
    sig = inspect.signature(aDSL_Not.__init__)
    params = list(sig.parameters.keys())



def test_adsl_equality_is_not_abstract():
    assert not inspect.isabstract(aDSL_Equality)


def test_adsl_equality_constructor_exists():
    assert callable(aDSL_Equality.__init__)


def test_adsl_equality_constructor_args():
    sig = inspect.signature(aDSL_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl_equality_has_op():
    assert hasattr(aDSL_Equality, "op")
    descriptor = None
    for klass in aDSL_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl_comparison_is_not_abstract():
    assert not inspect.isabstract(aDSL_Comparison)


def test_adsl_comparison_constructor_exists():
    assert callable(aDSL_Comparison.__init__)


def test_adsl_comparison_constructor_args():
    sig = inspect.signature(aDSL_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl_comparison_has_op():
    assert hasattr(aDSL_Comparison, "op")
    descriptor = None
    for klass in aDSL_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl_boolconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL_BoolConstant)


def test_adsl_boolconstant_constructor_exists():
    assert callable(aDSL_BoolConstant.__init__)


def test_adsl_boolconstant_constructor_args():
    sig = inspect.signature(aDSL_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adsl_boolconstant_has_value():
    assert hasattr(aDSL_BoolConstant, "value")
    descriptor = None
    for klass in aDSL_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adsl_and_is_not_abstract():
    assert not inspect.isabstract(aDSL_And)


def test_adsl_and_constructor_exists():
    assert callable(aDSL_And.__init__)


def test_adsl_and_constructor_args():
    sig = inspect.signature(aDSL_And.__init__)
    params = list(sig.parameters.keys())



def test_adsl_this_is_not_abstract():
    assert not inspect.isabstract(aDSL_This)


def test_adsl_this_constructor_exists():
    assert callable(aDSL_This.__init__)


def test_adsl_this_constructor_args():
    sig = inspect.signature(aDSL_This.__init__)
    params = list(sig.parameters.keys())



def test_adsl_init_is_not_abstract():
    assert not inspect.isabstract(aDSL_Init)


def test_adsl_init_constructor_exists():
    assert callable(aDSL_Init.__init__)


def test_adsl_init_constructor_args():
    sig = inspect.signature(aDSL_Init.__init__)
    params = list(sig.parameters.keys())



def test_adsl_mulordiv_is_not_abstract():
    assert not inspect.isabstract(aDSL_MulOrDiv)


def test_adsl_mulordiv_constructor_exists():
    assert callable(aDSL_MulOrDiv.__init__)


def test_adsl_mulordiv_constructor_args():
    sig = inspect.signature(aDSL_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_adsl_mulordiv_has_op():
    assert hasattr(aDSL_MulOrDiv, "op")
    descriptor = None
    for klass in aDSL_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_adsl_new_is_not_abstract():
    assert not inspect.isabstract(aDSL_New)


def test_adsl_new_constructor_exists():
    assert callable(aDSL_New.__init__)


def test_adsl_new_constructor_args():
    sig = inspect.signature(aDSL_New.__init__)
    params = list(sig.parameters.keys())



def test_adsl_stringconstant_is_not_abstract():
    assert not inspect.isabstract(aDSL_StringConstant)


def test_adsl_stringconstant_constructor_exists():
    assert callable(aDSL_StringConstant.__init__)


def test_adsl_stringconstant_constructor_args():
    sig = inspect.signature(aDSL_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adsl_stringconstant_has_value():
    assert hasattr(aDSL_StringConstant, "value")
    descriptor = None
    for klass in aDSL_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adsl_memberselection_is_not_abstract():
    assert not inspect.isabstract(aDSL_MemberSelection)


def test_adsl_memberselection_constructor_exists():
    assert callable(aDSL_MemberSelection.__init__)


def test_adsl_memberselection_constructor_args():
    sig = inspect.signature(aDSL_MemberSelection.__init__)
    params = list(sig.parameters.keys())
    assert "ispar" in params, "Missing parameter 'ispar'"
    assert "methodinvocation" in params, "Missing parameter 'methodinvocation'"

def test_adsl_memberselection_has_ispar():
    assert hasattr(aDSL_MemberSelection, "ispar")
    descriptor = None
    for klass in aDSL_MemberSelection.__mro__:
        if "ispar" in klass.__dict__:
            descriptor = klass.__dict__["ispar"]
            break
    assert isinstance(descriptor, property)

def test_adsl_memberselection_has_methodinvocation():
    assert hasattr(aDSL_MemberSelection, "methodinvocation")
    descriptor = None
    for klass in aDSL_MemberSelection.__mro__:
        if "methodinvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodinvocation"]
            break
    assert isinstance(descriptor, property)



def test_adsl_null_is_not_abstract():
    assert not inspect.isabstract(aDSL_Null)


def test_adsl_null_constructor_exists():
    assert callable(aDSL_Null.__init__)


def test_adsl_null_constructor_args():
    sig = inspect.signature(aDSL_Null.__init__)
    params = list(sig.parameters.keys())



def test_adsl_here_is_not_abstract():
    assert not inspect.isabstract(aDSL_Here)


def test_adsl_here_constructor_exists():
    assert callable(aDSL_Here.__init__)


def test_adsl_here_constructor_args():
    sig = inspect.signature(aDSL_Here.__init__)
    params = list(sig.parameters.keys())



def test_adsl_minus_is_not_abstract():
    assert not inspect.isabstract(aDSL_Minus)


def test_adsl_minus_constructor_exists():
    assert callable(aDSL_Minus.__init__)


def test_adsl_minus_constructor_args():
    sig = inspect.signature(aDSL_Minus.__init__)
    params = list(sig.parameters.keys())



def test_adsl_assignment_is_not_abstract():
    assert not inspect.isabstract(aDSL_Assignment)


def test_adsl_assignment_constructor_exists():
    assert callable(aDSL_Assignment.__init__)


def test_adsl_assignment_constructor_args():
    sig = inspect.signature(aDSL_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_adsl_block_is_not_abstract():
    assert not inspect.isabstract(aDSL_Block)


def test_adsl_block_constructor_exists():
    assert callable(aDSL_Block.__init__)


def test_adsl_block_constructor_args():
    sig = inspect.signature(aDSL_Block.__init__)
    params = list(sig.parameters.keys())
    assert "ispar" in params, "Missing parameter 'ispar'"

def test_adsl_block_has_ispar():
    assert hasattr(aDSL_Block, "ispar")
    descriptor = None
    for klass in aDSL_Block.__mro__:
        if "ispar" in klass.__dict__:
            descriptor = klass.__dict__["ispar"]
            break
    assert isinstance(descriptor, property)



def test_adsl_statement_is_not_abstract():
    assert not inspect.isabstract(aDSL_Statement)


def test_adsl_statement_constructor_exists():
    assert callable(aDSL_Statement.__init__)


def test_adsl_statement_constructor_args():
    sig = inspect.signature(aDSL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl_vardef_is_not_abstract():
    assert not inspect.isabstract(aDSL_VarDef)


def test_adsl_vardef_constructor_exists():
    assert callable(aDSL_VarDef.__init__)


def test_adsl_vardef_constructor_args():
    sig = inspect.signature(aDSL_VarDef.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl_ifstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_IfStat)


def test_adsl_ifstat_constructor_exists():
    assert callable(aDSL_IfStat.__init__)


def test_adsl_ifstat_constructor_args():
    sig = inspect.signature(aDSL_IfStat.__init__)
    params = list(sig.parameters.keys())
    assert "iselse" in params, "Missing parameter 'iselse'"

def test_adsl_ifstat_has_iselse():
    assert hasattr(aDSL_IfStat, "iselse")
    descriptor = None
    for klass in aDSL_IfStat.__mro__:
        if "iselse" in klass.__dict__:
            descriptor = klass.__dict__["iselse"]
            break
    assert isinstance(descriptor, property)



def test_adsl_expression_is_not_abstract():
    assert not inspect.isabstract(aDSL_Expression)


def test_adsl_expression_constructor_exists():
    assert callable(aDSL_Expression.__init__)


def test_adsl_expression_constructor_args():
    sig = inspect.signature(aDSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_adsl_whenstatement_is_not_abstract():
    assert not inspect.isabstract(aDSL_WhenStatement)


def test_adsl_whenstatement_constructor_exists():
    assert callable(aDSL_WhenStatement.__init__)


def test_adsl_whenstatement_constructor_args():
    sig = inspect.signature(aDSL_WhenStatement.__init__)
    params = list(sig.parameters.keys())



def test_adsl_finishstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_FinishStat)


def test_adsl_finishstat_constructor_exists():
    assert callable(aDSL_FinishStat.__init__)


def test_adsl_finishstat_constructor_args():
    sig = inspect.signature(aDSL_FinishStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_for2statement_is_not_abstract():
    assert not inspect.isabstract(aDSL_For2Statement)


def test_adsl_for2statement_constructor_exists():
    assert callable(aDSL_For2Statement.__init__)


def test_adsl_for2statement_constructor_args():
    sig = inspect.signature(aDSL_For2Statement.__init__)
    params = list(sig.parameters.keys())



def test_adsl_atomicstatement_is_not_abstract():
    assert not inspect.isabstract(aDSL_AtomicStatement)


def test_adsl_atomicstatement_constructor_exists():
    assert callable(aDSL_AtomicStatement.__init__)


def test_adsl_atomicstatement_constructor_args():
    sig = inspect.signature(aDSL_AtomicStatement.__init__)
    params = list(sig.parameters.keys())



def test_adsl_asyncstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_AsyncStat)


def test_adsl_asyncstat_constructor_exists():
    assert callable(aDSL_AsyncStat.__init__)


def test_adsl_asyncstat_constructor_args():
    sig = inspect.signature(aDSL_AsyncStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_returnstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_ReturnStat)


def test_adsl_returnstat_constructor_exists():
    assert callable(aDSL_ReturnStat.__init__)


def test_adsl_returnstat_constructor_args():
    sig = inspect.signature(aDSL_ReturnStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_forstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_ForStat)


def test_adsl_forstat_constructor_exists():
    assert callable(aDSL_ForStat.__init__)


def test_adsl_forstat_constructor_args():
    sig = inspect.signature(aDSL_ForStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_trycatchstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_TryCatchStat)


def test_adsl_trycatchstat_constructor_exists():
    assert callable(aDSL_TryCatchStat.__init__)


def test_adsl_trycatchstat_constructor_args():
    sig = inspect.signature(aDSL_TryCatchStat.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_trycatchstat_has_name():
    assert hasattr(aDSL_TryCatchStat, "name")
    descriptor = None
    for klass in aDSL_TryCatchStat.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl_atstat_is_not_abstract():
    assert not inspect.isabstract(aDSL_AtStat)


def test_adsl_atstat_constructor_exists():
    assert callable(aDSL_AtStat.__init__)


def test_adsl_atstat_constructor_args():
    sig = inspect.signature(aDSL_AtStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_whilestat_is_not_abstract():
    assert not inspect.isabstract(aDSL_WhileStat)


def test_adsl_whilestat_constructor_exists():
    assert callable(aDSL_WhileStat.__init__)


def test_adsl_whilestat_constructor_args():
    sig = inspect.signature(aDSL_WhileStat.__init__)
    params = list(sig.parameters.keys())



def test_adsl_body_is_not_abstract():
    assert not inspect.isabstract(aDSL_Body)


def test_adsl_body_constructor_exists():
    assert callable(aDSL_Body.__init__)


def test_adsl_body_constructor_args():
    sig = inspect.signature(aDSL_Body.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_adsl_printinst_is_not_abstract():
    assert not inspect.isabstract(aDSL_PrintInst)


def test_adsl_printinst_constructor_exists():
    assert callable(aDSL_PrintInst.__init__)


def test_adsl_printinst_constructor_args():
    sig = inspect.signature(aDSL_PrintInst.__init__)
    params = list(sig.parameters.keys())



def test_adsl_mainmethod_is_not_abstract():
    assert not inspect.isabstract(aDSL_MainMethod)


def test_adsl_mainmethod_constructor_exists():
    assert callable(aDSL_MainMethod.__init__)


def test_adsl_mainmethod_constructor_args():
    sig = inspect.signature(aDSL_MainMethod.__init__)
    params = list(sig.parameters.keys())



def test_shareddef_is_not_abstract():
    assert not inspect.isabstract(SharedDef)


def test_shareddef_constructor_exists():
    assert callable(SharedDef.__init__)


def test_shareddef_constructor_args():
    sig = inspect.signature(SharedDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl_sharedvardef_is_not_abstract():
    assert not inspect.isabstract(aDSL_SharedVarDef)


def test_adsl_sharedvardef_constructor_exists():
    assert callable(aDSL_SharedVarDef.__init__)


def test_adsl_sharedvardef_constructor_args():
    sig = inspect.signature(aDSL_SharedVarDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl_sharedarraydef_is_not_abstract():
    assert not inspect.isabstract(aDSL_SharedArrayDef)


def test_adsl_sharedarraydef_constructor_exists():
    assert callable(aDSL_SharedArrayDef.__init__)


def test_adsl_sharedarraydef_constructor_args():
    sig = inspect.signature(aDSL_SharedArrayDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl_operator_is_not_abstract():
    assert not inspect.isabstract(aDSL_Operator)


def test_adsl_operator_constructor_exists():
    assert callable(aDSL_Operator.__init__)


def test_adsl_operator_constructor_args():
    sig = inspect.signature(aDSL_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_adsl_operator_has_opName():
    assert hasattr(aDSL_Operator, "opName")
    descriptor = None
    for klass in aDSL_Operator.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_adsl_method_is_not_abstract():
    assert not inspect.isabstract(aDSL_Method)


def test_adsl_method_constructor_exists():
    assert callable(aDSL_Method.__init__)


def test_adsl_method_constructor_args():
    sig = inspect.signature(aDSL_Method.__init__)
    params = list(sig.parameters.keys())
    assert "isconst" in params, "Missing parameter 'isconst'"
    assert "istyped" in params, "Missing parameter 'istyped'"
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_method_has_isconst():
    assert hasattr(aDSL_Method, "isconst")
    descriptor = None
    for klass in aDSL_Method.__mro__:
        if "isconst" in klass.__dict__:
            descriptor = klass.__dict__["isconst"]
            break
    assert isinstance(descriptor, property)

def test_adsl_method_has_istyped():
    assert hasattr(aDSL_Method, "istyped")
    descriptor = None
    for klass in aDSL_Method.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)

def test_adsl_method_has_name():
    assert hasattr(aDSL_Method, "name")
    descriptor = None
    for klass in aDSL_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl_member_is_not_abstract():
    assert not inspect.isabstract(aDSL_Member)


def test_adsl_member_constructor_exists():
    assert callable(aDSL_Member.__init__)


def test_adsl_member_constructor_args():
    sig = inspect.signature(aDSL_Member.__init__)
    params = list(sig.parameters.keys())



def test_vardef_is_not_abstract():
    assert not inspect.isabstract(VarDef)


def test_vardef_constructor_exists():
    assert callable(VarDef.__init__)


def test_vardef_constructor_args():
    sig = inspect.signature(VarDef.__init__)
    params = list(sig.parameters.keys())



def test_adsl_variabletype_is_not_abstract():
    assert not inspect.isabstract(aDSL_VariableType)


def test_adsl_variabletype_constructor_exists():
    assert callable(aDSL_VariableType.__init__)


def test_adsl_variabletype_constructor_args():
    sig = inspect.signature(aDSL_VariableType.__init__)
    params = list(sig.parameters.keys())
    assert "isarray" in params, "Missing parameter 'isarray'"

def test_adsl_variabletype_has_isarray():
    assert hasattr(aDSL_VariableType, "isarray")
    descriptor = None
    for klass in aDSL_VariableType.__mro__:
        if "isarray" in klass.__dict__:
            descriptor = klass.__dict__["isarray"]
            break
    assert isinstance(descriptor, property)



def test_adsl_funcvardef_is_not_abstract():
    assert not inspect.isabstract(aDSL_FuncVarDef)


def test_adsl_funcvardef_constructor_exists():
    assert callable(aDSL_FuncVarDef.__init__)


def test_adsl_funcvardef_constructor_args():
    sig = inspect.signature(aDSL_FuncVarDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_funcvardef_has_name():
    assert hasattr(aDSL_FuncVarDef, "name")
    descriptor = None
    for klass in aDSL_FuncVarDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl_parameter_is_not_abstract():
    assert not inspect.isabstract(aDSL_Parameter)


def test_adsl_parameter_constructor_exists():
    assert callable(aDSL_Parameter.__init__)


def test_adsl_parameter_constructor_args():
    sig = inspect.signature(aDSL_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "istyped" in params, "Missing parameter 'istyped'"

def test_adsl_parameter_has_name():
    assert hasattr(aDSL_Parameter, "name")
    descriptor = None
    for klass in aDSL_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adsl_parameter_has_istyped():
    assert hasattr(aDSL_Parameter, "istyped")
    descriptor = None
    for klass in aDSL_Parameter.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)



def test_adsl_variabledef_is_not_abstract():
    assert not inspect.isabstract(aDSL_VariableDef)


def test_adsl_variabledef_constructor_exists():
    assert callable(aDSL_VariableDef.__init__)


def test_adsl_variabledef_constructor_args():
    sig = inspect.signature(aDSL_VariableDef.__init__)
    params = list(sig.parameters.keys())
    assert "vartype" in params, "Missing parameter 'vartype'"
    assert "isstatic" in params, "Missing parameter 'isstatic'"
    assert "istyped" in params, "Missing parameter 'istyped'"
    assert "isinit" in params, "Missing parameter 'isinit'"
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_variabledef_has_vartype():
    assert hasattr(aDSL_VariableDef, "vartype")
    descriptor = None
    for klass in aDSL_VariableDef.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)

def test_adsl_variabledef_has_isstatic():
    assert hasattr(aDSL_VariableDef, "isstatic")
    descriptor = None
    for klass in aDSL_VariableDef.__mro__:
        if "isstatic" in klass.__dict__:
            descriptor = klass.__dict__["isstatic"]
            break
    assert isinstance(descriptor, property)

def test_adsl_variabledef_has_istyped():
    assert hasattr(aDSL_VariableDef, "istyped")
    descriptor = None
    for klass in aDSL_VariableDef.__mro__:
        if "istyped" in klass.__dict__:
            descriptor = klass.__dict__["istyped"]
            break
    assert isinstance(descriptor, property)

def test_adsl_variabledef_has_isinit():
    assert hasattr(aDSL_VariableDef, "isinit")
    descriptor = None
    for klass in aDSL_VariableDef.__mro__:
        if "isinit" in klass.__dict__:
            descriptor = klass.__dict__["isinit"]
            break
    assert isinstance(descriptor, property)

def test_adsl_variabledef_has_name():
    assert hasattr(aDSL_VariableDef, "name")
    descriptor = None
    for klass in aDSL_VariableDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl_shareddef_is_not_abstract():
    assert not inspect.isabstract(aDSL_SharedDef)


def test_adsl_shareddef_constructor_exists():
    assert callable(aDSL_SharedDef.__init__)


def test_adsl_shareddef_constructor_args():
    sig = inspect.signature(aDSL_SharedDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "replicas" in params, "Missing parameter 'replicas'"

def test_adsl_shareddef_has_name():
    assert hasattr(aDSL_SharedDef, "name")
    descriptor = None
    for klass in aDSL_SharedDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adsl_shareddef_has_replicas():
    assert hasattr(aDSL_SharedDef, "replicas")
    descriptor = None
    for klass in aDSL_SharedDef.__mro__:
        if "replicas" in klass.__dict__:
            descriptor = klass.__dict__["replicas"]
            break
    assert isinstance(descriptor, property)



def test_adsl_xclass_is_not_abstract():
    assert not inspect.isabstract(aDSL_XClass)


def test_adsl_xclass_constructor_exists():
    assert callable(aDSL_XClass.__init__)


def test_adsl_xclass_constructor_args():
    sig = inspect.signature(aDSL_XClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_xclass_has_name():
    assert hasattr(aDSL_XClass, "name")
    descriptor = None
    for klass in aDSL_XClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adsl_abstractelements_is_not_abstract():
    assert not inspect.isabstract(aDSL_AbstractElements)


def test_adsl_abstractelements_constructor_exists():
    assert callable(aDSL_AbstractElements.__init__)


def test_adsl_abstractelements_constructor_args():
    sig = inspect.signature(aDSL_AbstractElements.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_adsl_abstractelements_has_importedNamespace():
    assert hasattr(aDSL_AbstractElements, "importedNamespace")
    descriptor = None
    for klass in aDSL_AbstractElements.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_adsl_program_is_not_abstract():
    assert not inspect.isabstract(aDSL_Program)


def test_adsl_program_constructor_exists():
    assert callable(aDSL_Program.__init__)


def test_adsl_program_constructor_args():
    sig = inspect.signature(aDSL_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adsl_program_has_name():
    assert hasattr(aDSL_Program, "name")
    descriptor = None
    for klass in aDSL_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
aDSL_IntegerNegative_strategy = st.builds(
    aDSL_IntegerNegative,
    value=
        st.integers(),
    isneg=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
aDSL_Plus_strategy = st.builds(
    aDSL_Plus,
)
aDSL_Reference_strategy = st.builds(
    aDSL_Reference,
    isarray=
        st.booleans()
)
aDSL_DeRef_strategy = st.builds(
    aDSL_DeRef,
)
aDSL_Or_strategy = st.builds(
    aDSL_Or,
)
aDSL_IntConstant_strategy = st.builds(
    aDSL_IntConstant,
)
aDSL_Not_strategy = st.builds(
    aDSL_Not,
)
aDSL_Equality_strategy = st.builds(
    aDSL_Equality,
    op=
        safe_text
)
aDSL_Comparison_strategy = st.builds(
    aDSL_Comparison,
    op=
        safe_text
)
aDSL_BoolConstant_strategy = st.builds(
    aDSL_BoolConstant,
    value=
        safe_text
)
aDSL_And_strategy = st.builds(
    aDSL_And,
)
aDSL_This_strategy = st.builds(
    aDSL_This,
)
aDSL_Init_strategy = st.builds(
    aDSL_Init,
)
aDSL_MulOrDiv_strategy = st.builds(
    aDSL_MulOrDiv,
    op=
        safe_text
)
aDSL_New_strategy = st.builds(
    aDSL_New,
)
aDSL_StringConstant_strategy = st.builds(
    aDSL_StringConstant,
    value=
        safe_text
)
aDSL_MemberSelection_strategy = st.builds(
    aDSL_MemberSelection,
    ispar=
        st.booleans(),
    methodinvocation=
        st.booleans()
)
aDSL_Null_strategy = st.builds(
    aDSL_Null,
)
aDSL_Here_strategy = st.builds(
    aDSL_Here,
)
aDSL_Minus_strategy = st.builds(
    aDSL_Minus,
)
aDSL_Assignment_strategy = st.builds(
    aDSL_Assignment,
)
aDSL_Block_strategy = st.builds(
    aDSL_Block,
    ispar=
        st.booleans()
)
aDSL_Statement_strategy = st.builds(
    aDSL_Statement,
)
aDSL_VarDef_strategy = st.builds(
    aDSL_VarDef,
)
Statement_strategy = st.builds(
    Statement,
)
aDSL_IfStat_strategy = st.builds(
    aDSL_IfStat,
    iselse=
        st.booleans()
)
aDSL_Expression_strategy = st.builds(
    aDSL_Expression,
)
aDSL_WhenStatement_strategy = st.builds(
    aDSL_WhenStatement,
)
aDSL_FinishStat_strategy = st.builds(
    aDSL_FinishStat,
)
aDSL_For2Statement_strategy = st.builds(
    aDSL_For2Statement,
)
aDSL_AtomicStatement_strategy = st.builds(
    aDSL_AtomicStatement,
)
aDSL_AsyncStat_strategy = st.builds(
    aDSL_AsyncStat,
)
aDSL_ReturnStat_strategy = st.builds(
    aDSL_ReturnStat,
)
aDSL_ForStat_strategy = st.builds(
    aDSL_ForStat,
)
aDSL_TryCatchStat_strategy = st.builds(
    aDSL_TryCatchStat,
    name=
        safe_text
)
aDSL_AtStat_strategy = st.builds(
    aDSL_AtStat,
)
aDSL_WhileStat_strategy = st.builds(
    aDSL_WhileStat,
)
aDSL_Body_strategy = st.builds(
    aDSL_Body,
)
Member_strategy = st.builds(
    Member,
)
aDSL_PrintInst_strategy = st.builds(
    aDSL_PrintInst,
)
aDSL_MainMethod_strategy = st.builds(
    aDSL_MainMethod,
)
SharedDef_strategy = st.builds(
    SharedDef,
)
aDSL_SharedVarDef_strategy = st.builds(
    aDSL_SharedVarDef,
)
aDSL_SharedArrayDef_strategy = st.builds(
    aDSL_SharedArrayDef,
)
aDSL_Operator_strategy = st.builds(
    aDSL_Operator,
    opName=
        safe_text
)
aDSL_Method_strategy = st.builds(
    aDSL_Method,
    isconst=
        st.booleans(),
    istyped=
        st.booleans(),
    name=
        safe_text
)
aDSL_Member_strategy = st.builds(
    aDSL_Member,
)
VarDef_strategy = st.builds(
    VarDef,
)
aDSL_VariableType_strategy = st.builds(
    aDSL_VariableType,
    isarray=
        st.booleans()
)
aDSL_FuncVarDef_strategy = st.builds(
    aDSL_FuncVarDef,
    name=
        safe_text
)
aDSL_Parameter_strategy = st.builds(
    aDSL_Parameter,
    name=
        safe_text,
    istyped=
        st.booleans()
)
aDSL_VariableDef_strategy = st.builds(
    aDSL_VariableDef,
    vartype=
        safe_text,
    isstatic=
        st.booleans(),
    istyped=
        st.booleans(),
    isinit=
        st.booleans(),
    name=
        safe_text
)
aDSL_SharedDef_strategy = st.builds(
    aDSL_SharedDef,
    name=
        safe_text,
    replicas=
        st.booleans()
)
aDSL_XClass_strategy = st.builds(
    aDSL_XClass,
    name=
        safe_text
)
aDSL_AbstractElements_strategy = st.builds(
    aDSL_AbstractElements,
    importedNamespace=
        safe_text
)
aDSL_Program_strategy = st.builds(
    aDSL_Program,
    name=
        safe_text
)

@given(instance=aDSL_IntegerNegative_strategy)
@settings(max_examples=50)
def test_adsl_integernegative_instantiation(instance):
    assert isinstance(instance, aDSL_IntegerNegative)



@given(instance=aDSL_IntegerNegative_strategy)
def test_adsl_integernegative_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aDSL_IntegerNegative_strategy)
def test_adsl_integernegative_isneg_setter(instance):
    original = instance.isneg
    instance.isneg = original
    assert instance.isneg == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=aDSL_Plus_strategy)
@settings(max_examples=50)
def test_adsl_plus_instantiation(instance):
    assert isinstance(instance, aDSL_Plus)

@given(instance=aDSL_Reference_strategy)
@settings(max_examples=50)
def test_adsl_reference_instantiation(instance):
    assert isinstance(instance, aDSL_Reference)



@given(instance=aDSL_Reference_strategy)
def test_adsl_reference_isarray_setter(instance):
    original = instance.isarray
    instance.isarray = original
    assert instance.isarray == original

@given(instance=aDSL_DeRef_strategy)
@settings(max_examples=50)
def test_adsl_deref_instantiation(instance):
    assert isinstance(instance, aDSL_DeRef)

@given(instance=aDSL_Or_strategy)
@settings(max_examples=50)
def test_adsl_or_instantiation(instance):
    assert isinstance(instance, aDSL_Or)

@given(instance=aDSL_IntConstant_strategy)
@settings(max_examples=50)
def test_adsl_intconstant_instantiation(instance):
    assert isinstance(instance, aDSL_IntConstant)

@given(instance=aDSL_Not_strategy)
@settings(max_examples=50)
def test_adsl_not_instantiation(instance):
    assert isinstance(instance, aDSL_Not)

@given(instance=aDSL_Equality_strategy)
@settings(max_examples=50)
def test_adsl_equality_instantiation(instance):
    assert isinstance(instance, aDSL_Equality)



@given(instance=aDSL_Equality_strategy)
def test_adsl_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL_Comparison_strategy)
@settings(max_examples=50)
def test_adsl_comparison_instantiation(instance):
    assert isinstance(instance, aDSL_Comparison)



@given(instance=aDSL_Comparison_strategy)
def test_adsl_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL_BoolConstant_strategy)
@settings(max_examples=50)
def test_adsl_boolconstant_instantiation(instance):
    assert isinstance(instance, aDSL_BoolConstant)



@given(instance=aDSL_BoolConstant_strategy)
def test_adsl_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aDSL_And_strategy)
@settings(max_examples=50)
def test_adsl_and_instantiation(instance):
    assert isinstance(instance, aDSL_And)

@given(instance=aDSL_This_strategy)
@settings(max_examples=50)
def test_adsl_this_instantiation(instance):
    assert isinstance(instance, aDSL_This)

@given(instance=aDSL_Init_strategy)
@settings(max_examples=50)
def test_adsl_init_instantiation(instance):
    assert isinstance(instance, aDSL_Init)

@given(instance=aDSL_MulOrDiv_strategy)
@settings(max_examples=50)
def test_adsl_mulordiv_instantiation(instance):
    assert isinstance(instance, aDSL_MulOrDiv)



@given(instance=aDSL_MulOrDiv_strategy)
def test_adsl_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aDSL_New_strategy)
@settings(max_examples=50)
def test_adsl_new_instantiation(instance):
    assert isinstance(instance, aDSL_New)

@given(instance=aDSL_StringConstant_strategy)
@settings(max_examples=50)
def test_adsl_stringconstant_instantiation(instance):
    assert isinstance(instance, aDSL_StringConstant)



@given(instance=aDSL_StringConstant_strategy)
def test_adsl_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aDSL_MemberSelection_strategy)
@settings(max_examples=50)
def test_adsl_memberselection_instantiation(instance):
    assert isinstance(instance, aDSL_MemberSelection)



@given(instance=aDSL_MemberSelection_strategy)
def test_adsl_memberselection_ispar_setter(instance):
    original = instance.ispar
    instance.ispar = original
    assert instance.ispar == original



@given(instance=aDSL_MemberSelection_strategy)
def test_adsl_memberselection_methodinvocation_setter(instance):
    original = instance.methodinvocation
    instance.methodinvocation = original
    assert instance.methodinvocation == original

@given(instance=aDSL_Null_strategy)
@settings(max_examples=50)
def test_adsl_null_instantiation(instance):
    assert isinstance(instance, aDSL_Null)

@given(instance=aDSL_Here_strategy)
@settings(max_examples=50)
def test_adsl_here_instantiation(instance):
    assert isinstance(instance, aDSL_Here)

@given(instance=aDSL_Minus_strategy)
@settings(max_examples=50)
def test_adsl_minus_instantiation(instance):
    assert isinstance(instance, aDSL_Minus)

@given(instance=aDSL_Assignment_strategy)
@settings(max_examples=50)
def test_adsl_assignment_instantiation(instance):
    assert isinstance(instance, aDSL_Assignment)

@given(instance=aDSL_Block_strategy)
@settings(max_examples=50)
def test_adsl_block_instantiation(instance):
    assert isinstance(instance, aDSL_Block)



@given(instance=aDSL_Block_strategy)
def test_adsl_block_ispar_setter(instance):
    original = instance.ispar
    instance.ispar = original
    assert instance.ispar == original

@given(instance=aDSL_Statement_strategy)
@settings(max_examples=50)
def test_adsl_statement_instantiation(instance):
    assert isinstance(instance, aDSL_Statement)

@given(instance=aDSL_VarDef_strategy)
@settings(max_examples=50)
def test_adsl_vardef_instantiation(instance):
    assert isinstance(instance, aDSL_VarDef)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=aDSL_IfStat_strategy)
@settings(max_examples=50)
def test_adsl_ifstat_instantiation(instance):
    assert isinstance(instance, aDSL_IfStat)



@given(instance=aDSL_IfStat_strategy)
def test_adsl_ifstat_iselse_setter(instance):
    original = instance.iselse
    instance.iselse = original
    assert instance.iselse == original

@given(instance=aDSL_Expression_strategy)
@settings(max_examples=50)
def test_adsl_expression_instantiation(instance):
    assert isinstance(instance, aDSL_Expression)

@given(instance=aDSL_WhenStatement_strategy)
@settings(max_examples=50)
def test_adsl_whenstatement_instantiation(instance):
    assert isinstance(instance, aDSL_WhenStatement)

@given(instance=aDSL_FinishStat_strategy)
@settings(max_examples=50)
def test_adsl_finishstat_instantiation(instance):
    assert isinstance(instance, aDSL_FinishStat)

@given(instance=aDSL_For2Statement_strategy)
@settings(max_examples=50)
def test_adsl_for2statement_instantiation(instance):
    assert isinstance(instance, aDSL_For2Statement)

@given(instance=aDSL_AtomicStatement_strategy)
@settings(max_examples=50)
def test_adsl_atomicstatement_instantiation(instance):
    assert isinstance(instance, aDSL_AtomicStatement)

@given(instance=aDSL_AsyncStat_strategy)
@settings(max_examples=50)
def test_adsl_asyncstat_instantiation(instance):
    assert isinstance(instance, aDSL_AsyncStat)

@given(instance=aDSL_ReturnStat_strategy)
@settings(max_examples=50)
def test_adsl_returnstat_instantiation(instance):
    assert isinstance(instance, aDSL_ReturnStat)

@given(instance=aDSL_ForStat_strategy)
@settings(max_examples=50)
def test_adsl_forstat_instantiation(instance):
    assert isinstance(instance, aDSL_ForStat)

@given(instance=aDSL_TryCatchStat_strategy)
@settings(max_examples=50)
def test_adsl_trycatchstat_instantiation(instance):
    assert isinstance(instance, aDSL_TryCatchStat)



@given(instance=aDSL_TryCatchStat_strategy)
def test_adsl_trycatchstat_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL_AtStat_strategy)
@settings(max_examples=50)
def test_adsl_atstat_instantiation(instance):
    assert isinstance(instance, aDSL_AtStat)

@given(instance=aDSL_WhileStat_strategy)
@settings(max_examples=50)
def test_adsl_whilestat_instantiation(instance):
    assert isinstance(instance, aDSL_WhileStat)

@given(instance=aDSL_Body_strategy)
@settings(max_examples=50)
def test_adsl_body_instantiation(instance):
    assert isinstance(instance, aDSL_Body)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=aDSL_PrintInst_strategy)
@settings(max_examples=50)
def test_adsl_printinst_instantiation(instance):
    assert isinstance(instance, aDSL_PrintInst)

@given(instance=aDSL_MainMethod_strategy)
@settings(max_examples=50)
def test_adsl_mainmethod_instantiation(instance):
    assert isinstance(instance, aDSL_MainMethod)

@given(instance=SharedDef_strategy)
@settings(max_examples=50)
def test_shareddef_instantiation(instance):
    assert isinstance(instance, SharedDef)

@given(instance=aDSL_SharedVarDef_strategy)
@settings(max_examples=50)
def test_adsl_sharedvardef_instantiation(instance):
    assert isinstance(instance, aDSL_SharedVarDef)

@given(instance=aDSL_SharedArrayDef_strategy)
@settings(max_examples=50)
def test_adsl_sharedarraydef_instantiation(instance):
    assert isinstance(instance, aDSL_SharedArrayDef)

@given(instance=aDSL_Operator_strategy)
@settings(max_examples=50)
def test_adsl_operator_instantiation(instance):
    assert isinstance(instance, aDSL_Operator)



@given(instance=aDSL_Operator_strategy)
def test_adsl_operator_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=aDSL_Method_strategy)
@settings(max_examples=50)
def test_adsl_method_instantiation(instance):
    assert isinstance(instance, aDSL_Method)



@given(instance=aDSL_Method_strategy)
def test_adsl_method_isconst_setter(instance):
    original = instance.isconst
    instance.isconst = original
    assert instance.isconst == original



@given(instance=aDSL_Method_strategy)
def test_adsl_method_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original



@given(instance=aDSL_Method_strategy)
def test_adsl_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL_Member_strategy)
@settings(max_examples=50)
def test_adsl_member_instantiation(instance):
    assert isinstance(instance, aDSL_Member)

@given(instance=VarDef_strategy)
@settings(max_examples=50)
def test_vardef_instantiation(instance):
    assert isinstance(instance, VarDef)

@given(instance=aDSL_VariableType_strategy)
@settings(max_examples=50)
def test_adsl_variabletype_instantiation(instance):
    assert isinstance(instance, aDSL_VariableType)



@given(instance=aDSL_VariableType_strategy)
def test_adsl_variabletype_isarray_setter(instance):
    original = instance.isarray
    instance.isarray = original
    assert instance.isarray == original

@given(instance=aDSL_FuncVarDef_strategy)
@settings(max_examples=50)
def test_adsl_funcvardef_instantiation(instance):
    assert isinstance(instance, aDSL_FuncVarDef)



@given(instance=aDSL_FuncVarDef_strategy)
def test_adsl_funcvardef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL_Parameter_strategy)
@settings(max_examples=50)
def test_adsl_parameter_instantiation(instance):
    assert isinstance(instance, aDSL_Parameter)



@given(instance=aDSL_Parameter_strategy)
def test_adsl_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aDSL_Parameter_strategy)
def test_adsl_parameter_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original

@given(instance=aDSL_VariableDef_strategy)
@settings(max_examples=50)
def test_adsl_variabledef_instantiation(instance):
    assert isinstance(instance, aDSL_VariableDef)



@given(instance=aDSL_VariableDef_strategy)
def test_adsl_variabledef_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original



@given(instance=aDSL_VariableDef_strategy)
def test_adsl_variabledef_isstatic_setter(instance):
    original = instance.isstatic
    instance.isstatic = original
    assert instance.isstatic == original



@given(instance=aDSL_VariableDef_strategy)
def test_adsl_variabledef_istyped_setter(instance):
    original = instance.istyped
    instance.istyped = original
    assert instance.istyped == original



@given(instance=aDSL_VariableDef_strategy)
def test_adsl_variabledef_isinit_setter(instance):
    original = instance.isinit
    instance.isinit = original
    assert instance.isinit == original



@given(instance=aDSL_VariableDef_strategy)
def test_adsl_variabledef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL_SharedDef_strategy)
@settings(max_examples=50)
def test_adsl_shareddef_instantiation(instance):
    assert isinstance(instance, aDSL_SharedDef)



@given(instance=aDSL_SharedDef_strategy)
def test_adsl_shareddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aDSL_SharedDef_strategy)
def test_adsl_shareddef_replicas_setter(instance):
    original = instance.replicas
    instance.replicas = original
    assert instance.replicas == original

@given(instance=aDSL_XClass_strategy)
@settings(max_examples=50)
def test_adsl_xclass_instantiation(instance):
    assert isinstance(instance, aDSL_XClass)



@given(instance=aDSL_XClass_strategy)
def test_adsl_xclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aDSL_AbstractElements_strategy)
@settings(max_examples=50)
def test_adsl_abstractelements_instantiation(instance):
    assert isinstance(instance, aDSL_AbstractElements)



@given(instance=aDSL_AbstractElements_strategy)
def test_adsl_abstractelements_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=aDSL_Program_strategy)
@settings(max_examples=50)
def test_adsl_program_instantiation(instance):
    assert isinstance(instance, aDSL_Program)



@given(instance=aDSL_Program_strategy)
def test_adsl_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
