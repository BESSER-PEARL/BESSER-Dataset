import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    dinkiemodel_VariableExpr,
    dinkiemodel_BoolVal,
    dinkiemodel_ArrayExpr,
    dinkiemodel_TwoOperator,
    dinkiemodel_OneOperator,
    dinkiemodel_Character,
    dinkiemodel_BracketExpr,
    dinkiemodel_Number,
    dinkiemodel_ThreadID,
    Type,
    dinkiemodel_ArrayType,
    dinkiemodel_Expression,
    dinkiemodel_BaseType,
    Statement,
    dinkiemodel_Sync,
    dinkiemodel_ArrayAssign,
    dinkiemodel_EmptyArrayDecl,
    dinkiemodel_FilledArrayDecl,
    dinkiemodel_While,
    dinkiemodel_Parallel,
    dinkiemodel_WriteStatement,
    dinkiemodel_IfTwo,
    dinkiemodel_Assign,
    dinkiemodel_StringArrayDecl,
    dinkiemodel_Return,
    dinkiemodel_IfOne,
    dinkiemodel_FuncExpr,
    dinkiemodel_Declaration,
    dinkiemodel_Type,
    dinkiemodel_Argument,
    dinkiemodel_ReadStatement,
    dinkiemodel_Program,
    dinkiemodel_Statement,
    dinkiemodel_Main,
    dinkiemodel_FunctionDecl,
    EBaseType,
    ETwoOperator,
    EOneOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_variableexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_VariableExpr)


def test_dinkiemodel_variableexpr_constructor_exists():
    assert callable(dinkiemodel_VariableExpr.__init__)


def test_dinkiemodel_variableexpr_constructor_args():
    sig = inspect.signature(dinkiemodel_VariableExpr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel_variableexpr_has_name():
    assert hasattr(dinkiemodel_VariableExpr, "name")
    descriptor = None
    for klass in dinkiemodel_VariableExpr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_boolval_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_BoolVal)


def test_dinkiemodel_boolval_constructor_exists():
    assert callable(dinkiemodel_BoolVal.__init__)


def test_dinkiemodel_boolval_constructor_args():
    sig = inspect.signature(dinkiemodel_BoolVal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel_boolval_has_value():
    assert hasattr(dinkiemodel_BoolVal, "value")
    descriptor = None
    for klass in dinkiemodel_BoolVal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_arrayexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_ArrayExpr)


def test_dinkiemodel_arrayexpr_constructor_exists():
    assert callable(dinkiemodel_ArrayExpr.__init__)


def test_dinkiemodel_arrayexpr_constructor_args():
    sig = inspect.signature(dinkiemodel_ArrayExpr.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_arrayexpr_has_varName():
    assert hasattr(dinkiemodel_ArrayExpr, "varName")
    descriptor = None
    for klass in dinkiemodel_ArrayExpr.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_twooperator_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_TwoOperator)


def test_dinkiemodel_twooperator_constructor_exists():
    assert callable(dinkiemodel_TwoOperator.__init__)


def test_dinkiemodel_twooperator_constructor_args():
    sig = inspect.signature(dinkiemodel_TwoOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dinkiemodel_twooperator_has_operator():
    assert hasattr(dinkiemodel_TwoOperator, "operator")
    descriptor = None
    for klass in dinkiemodel_TwoOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_oneoperator_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_OneOperator)


def test_dinkiemodel_oneoperator_constructor_exists():
    assert callable(dinkiemodel_OneOperator.__init__)


def test_dinkiemodel_oneoperator_constructor_args():
    sig = inspect.signature(dinkiemodel_OneOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dinkiemodel_oneoperator_has_operator():
    assert hasattr(dinkiemodel_OneOperator, "operator")
    descriptor = None
    for klass in dinkiemodel_OneOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_character_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Character)


def test_dinkiemodel_character_constructor_exists():
    assert callable(dinkiemodel_Character.__init__)


def test_dinkiemodel_character_constructor_args():
    sig = inspect.signature(dinkiemodel_Character.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel_character_has_value():
    assert hasattr(dinkiemodel_Character, "value")
    descriptor = None
    for klass in dinkiemodel_Character.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_bracketexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_BracketExpr)


def test_dinkiemodel_bracketexpr_constructor_exists():
    assert callable(dinkiemodel_BracketExpr.__init__)


def test_dinkiemodel_bracketexpr_constructor_args():
    sig = inspect.signature(dinkiemodel_BracketExpr.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_number_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Number)


def test_dinkiemodel_number_constructor_exists():
    assert callable(dinkiemodel_Number.__init__)


def test_dinkiemodel_number_constructor_args():
    sig = inspect.signature(dinkiemodel_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dinkiemodel_number_has_value():
    assert hasattr(dinkiemodel_Number, "value")
    descriptor = None
    for klass in dinkiemodel_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_threadid_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_ThreadID)


def test_dinkiemodel_threadid_constructor_exists():
    assert callable(dinkiemodel_ThreadID.__init__)


def test_dinkiemodel_threadid_constructor_args():
    sig = inspect.signature(dinkiemodel_ThreadID.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_arraytype_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_ArrayType)


def test_dinkiemodel_arraytype_constructor_exists():
    assert callable(dinkiemodel_ArrayType.__init__)


def test_dinkiemodel_arraytype_constructor_args():
    sig = inspect.signature(dinkiemodel_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "arrayType" in params, "Missing parameter 'arrayType'"

def test_dinkiemodel_arraytype_has_arrayType():
    assert hasattr(dinkiemodel_ArrayType, "arrayType")
    descriptor = None
    for klass in dinkiemodel_ArrayType.__mro__:
        if "arrayType" in klass.__dict__:
            descriptor = klass.__dict__["arrayType"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_expression_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Expression)


def test_dinkiemodel_expression_constructor_exists():
    assert callable(dinkiemodel_Expression.__init__)


def test_dinkiemodel_expression_constructor_args():
    sig = inspect.signature(dinkiemodel_Expression.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_basetype_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_BaseType)


def test_dinkiemodel_basetype_constructor_exists():
    assert callable(dinkiemodel_BaseType.__init__)


def test_dinkiemodel_basetype_constructor_args():
    sig = inspect.signature(dinkiemodel_BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dinkiemodel_basetype_has_type():
    assert hasattr(dinkiemodel_BaseType, "type")
    descriptor = None
    for klass in dinkiemodel_BaseType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_sync_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Sync)


def test_dinkiemodel_sync_constructor_exists():
    assert callable(dinkiemodel_Sync.__init__)


def test_dinkiemodel_sync_constructor_args():
    sig = inspect.signature(dinkiemodel_Sync.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_sync_has_varName():
    assert hasattr(dinkiemodel_Sync, "varName")
    descriptor = None
    for klass in dinkiemodel_Sync.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_arrayassign_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_ArrayAssign)


def test_dinkiemodel_arrayassign_constructor_exists():
    assert callable(dinkiemodel_ArrayAssign.__init__)


def test_dinkiemodel_arrayassign_constructor_args():
    sig = inspect.signature(dinkiemodel_ArrayAssign.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_arrayassign_has_varName():
    assert hasattr(dinkiemodel_ArrayAssign, "varName")
    descriptor = None
    for klass in dinkiemodel_ArrayAssign.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_emptyarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_EmptyArrayDecl)


def test_dinkiemodel_emptyarraydecl_constructor_exists():
    assert callable(dinkiemodel_EmptyArrayDecl.__init__)


def test_dinkiemodel_emptyarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel_EmptyArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "varName" in params, "Missing parameter 'varName'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_dinkiemodel_emptyarraydecl_has_size():
    assert hasattr(dinkiemodel_EmptyArrayDecl, "size")
    descriptor = None
    for klass in dinkiemodel_EmptyArrayDecl.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_emptyarraydecl_has_varName():
    assert hasattr(dinkiemodel_EmptyArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel_EmptyArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_emptyarraydecl_has_global_():
    assert hasattr(dinkiemodel_EmptyArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel_EmptyArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_filledarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_FilledArrayDecl)


def test_dinkiemodel_filledarraydecl_constructor_exists():
    assert callable(dinkiemodel_FilledArrayDecl.__init__)


def test_dinkiemodel_filledarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel_FilledArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_dinkiemodel_filledarraydecl_has_varName():
    assert hasattr(dinkiemodel_FilledArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel_FilledArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_filledarraydecl_has_global_():
    assert hasattr(dinkiemodel_FilledArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel_FilledArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_while_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_While)


def test_dinkiemodel_while_constructor_exists():
    assert callable(dinkiemodel_While.__init__)


def test_dinkiemodel_while_constructor_args():
    sig = inspect.signature(dinkiemodel_While.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_parallel_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Parallel)


def test_dinkiemodel_parallel_constructor_exists():
    assert callable(dinkiemodel_Parallel.__init__)


def test_dinkiemodel_parallel_constructor_args():
    sig = inspect.signature(dinkiemodel_Parallel.__init__)
    params = list(sig.parameters.keys())
    assert "nrOfThreads" in params, "Missing parameter 'nrOfThreads'"

def test_dinkiemodel_parallel_has_nrOfThreads():
    assert hasattr(dinkiemodel_Parallel, "nrOfThreads")
    descriptor = None
    for klass in dinkiemodel_Parallel.__mro__:
        if "nrOfThreads" in klass.__dict__:
            descriptor = klass.__dict__["nrOfThreads"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_writestatement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_WriteStatement)


def test_dinkiemodel_writestatement_constructor_exists():
    assert callable(dinkiemodel_WriteStatement.__init__)


def test_dinkiemodel_writestatement_constructor_args():
    sig = inspect.signature(dinkiemodel_WriteStatement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_iftwo_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_IfTwo)


def test_dinkiemodel_iftwo_constructor_exists():
    assert callable(dinkiemodel_IfTwo.__init__)


def test_dinkiemodel_iftwo_constructor_args():
    sig = inspect.signature(dinkiemodel_IfTwo.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_assign_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Assign)


def test_dinkiemodel_assign_constructor_exists():
    assert callable(dinkiemodel_Assign.__init__)


def test_dinkiemodel_assign_constructor_args():
    sig = inspect.signature(dinkiemodel_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_assign_has_varName():
    assert hasattr(dinkiemodel_Assign, "varName")
    descriptor = None
    for klass in dinkiemodel_Assign.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_stringarraydecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_StringArrayDecl)


def test_dinkiemodel_stringarraydecl_constructor_exists():
    assert callable(dinkiemodel_StringArrayDecl.__init__)


def test_dinkiemodel_stringarraydecl_constructor_args():
    sig = inspect.signature(dinkiemodel_StringArrayDecl.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"
    assert "content" in params, "Missing parameter 'content'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_dinkiemodel_stringarraydecl_has_varName():
    assert hasattr(dinkiemodel_StringArrayDecl, "varName")
    descriptor = None
    for klass in dinkiemodel_StringArrayDecl.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_stringarraydecl_has_content():
    assert hasattr(dinkiemodel_StringArrayDecl, "content")
    descriptor = None
    for klass in dinkiemodel_StringArrayDecl.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_stringarraydecl_has_global_():
    assert hasattr(dinkiemodel_StringArrayDecl, "global_")
    descriptor = None
    for klass in dinkiemodel_StringArrayDecl.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_return_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Return)


def test_dinkiemodel_return_constructor_exists():
    assert callable(dinkiemodel_Return.__init__)


def test_dinkiemodel_return_constructor_args():
    sig = inspect.signature(dinkiemodel_Return.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_ifone_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_IfOne)


def test_dinkiemodel_ifone_constructor_exists():
    assert callable(dinkiemodel_IfOne.__init__)


def test_dinkiemodel_ifone_constructor_args():
    sig = inspect.signature(dinkiemodel_IfOne.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_funcexpr_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_FuncExpr)


def test_dinkiemodel_funcexpr_constructor_exists():
    assert callable(dinkiemodel_FuncExpr.__init__)


def test_dinkiemodel_funcexpr_constructor_args():
    sig = inspect.signature(dinkiemodel_FuncExpr.__init__)
    params = list(sig.parameters.keys())
    assert "funcName" in params, "Missing parameter 'funcName'"

def test_dinkiemodel_funcexpr_has_funcName():
    assert hasattr(dinkiemodel_FuncExpr, "funcName")
    descriptor = None
    for klass in dinkiemodel_FuncExpr.__mro__:
        if "funcName" in klass.__dict__:
            descriptor = klass.__dict__["funcName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_declaration_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Declaration)


def test_dinkiemodel_declaration_constructor_exists():
    assert callable(dinkiemodel_Declaration.__init__)


def test_dinkiemodel_declaration_constructor_args():
    sig = inspect.signature(dinkiemodel_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_declaration_has_global_():
    assert hasattr(dinkiemodel_Declaration, "global_")
    descriptor = None
    for klass in dinkiemodel_Declaration.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_dinkiemodel_declaration_has_varName():
    assert hasattr(dinkiemodel_Declaration, "varName")
    descriptor = None
    for klass in dinkiemodel_Declaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_type_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Type)


def test_dinkiemodel_type_constructor_exists():
    assert callable(dinkiemodel_Type.__init__)


def test_dinkiemodel_type_constructor_args():
    sig = inspect.signature(dinkiemodel_Type.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_argument_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Argument)


def test_dinkiemodel_argument_constructor_exists():
    assert callable(dinkiemodel_Argument.__init__)


def test_dinkiemodel_argument_constructor_args():
    sig = inspect.signature(dinkiemodel_Argument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel_argument_has_name():
    assert hasattr(dinkiemodel_Argument, "name")
    descriptor = None
    for klass in dinkiemodel_Argument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_readstatement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_ReadStatement)


def test_dinkiemodel_readstatement_constructor_exists():
    assert callable(dinkiemodel_ReadStatement.__init__)


def test_dinkiemodel_readstatement_constructor_args():
    sig = inspect.signature(dinkiemodel_ReadStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_dinkiemodel_readstatement_has_varName():
    assert hasattr(dinkiemodel_ReadStatement, "varName")
    descriptor = None
    for klass in dinkiemodel_ReadStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_dinkiemodel_program_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Program)


def test_dinkiemodel_program_constructor_exists():
    assert callable(dinkiemodel_Program.__init__)


def test_dinkiemodel_program_constructor_args():
    sig = inspect.signature(dinkiemodel_Program.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_statement_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Statement)


def test_dinkiemodel_statement_constructor_exists():
    assert callable(dinkiemodel_Statement.__init__)


def test_dinkiemodel_statement_constructor_args():
    sig = inspect.signature(dinkiemodel_Statement.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_main_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_Main)


def test_dinkiemodel_main_constructor_exists():
    assert callable(dinkiemodel_Main.__init__)


def test_dinkiemodel_main_constructor_args():
    sig = inspect.signature(dinkiemodel_Main.__init__)
    params = list(sig.parameters.keys())



def test_dinkiemodel_functiondecl_is_not_abstract():
    assert not inspect.isabstract(dinkiemodel_FunctionDecl)


def test_dinkiemodel_functiondecl_constructor_exists():
    assert callable(dinkiemodel_FunctionDecl.__init__)


def test_dinkiemodel_functiondecl_constructor_args():
    sig = inspect.signature(dinkiemodel_FunctionDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dinkiemodel_functiondecl_has_name():
    assert hasattr(dinkiemodel_FunctionDecl, "name")
    descriptor = None
    for klass in dinkiemodel_FunctionDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ebasetype_exists():
    # Check that the Enumeration exists
    assert EBaseType is not None

def test_ebasetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EBaseType]
    expected_literals = [
        "BOOL",
        "CHAR",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EBaseType"

def test_etwooperator_exists():
    # Check that the Enumeration exists
    assert ETwoOperator is not None

def test_etwooperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ETwoOperator]
    expected_literals = [
        "AND",
        "DEVIDE",
        "OR",
        "GT",
        "GE",
        "PLUS",
        "EQUAL",
        "LT",
        "LE",
        "MINUS",
        "NOT_EQUAL",
        "TIMES",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ETwoOperator"

def test_eoneoperator_exists():
    # Check that the Enumeration exists
    assert EOneOperator is not None

def test_eoneoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EOneOperator]
    expected_literals = [
        "NOT",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EOneOperator"


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
Expression_strategy = st.builds(
    Expression,
)
dinkiemodel_VariableExpr_strategy = st.builds(
    dinkiemodel_VariableExpr,
    name=
        safe_text
)
dinkiemodel_BoolVal_strategy = st.builds(
    dinkiemodel_BoolVal,
    value=
        st.booleans()
)
dinkiemodel_ArrayExpr_strategy = st.builds(
    dinkiemodel_ArrayExpr,
    varName=
        safe_text
)
dinkiemodel_TwoOperator_strategy = st.builds(
    dinkiemodel_TwoOperator,
    operator=
        safe_text
)
dinkiemodel_OneOperator_strategy = st.builds(
    dinkiemodel_OneOperator,
    operator=
        safe_text
)
dinkiemodel_Character_strategy = st.builds(
    dinkiemodel_Character,
    value=
        safe_text
)
dinkiemodel_BracketExpr_strategy = st.builds(
    dinkiemodel_BracketExpr,
)
dinkiemodel_Number_strategy = st.builds(
    dinkiemodel_Number,
    value=
        st.integers()
)
dinkiemodel_ThreadID_strategy = st.builds(
    dinkiemodel_ThreadID,
)
Type_strategy = st.builds(
    Type,
)
dinkiemodel_ArrayType_strategy = st.builds(
    dinkiemodel_ArrayType,
    arrayType=
        safe_text
)
dinkiemodel_Expression_strategy = st.builds(
    dinkiemodel_Expression,
)
dinkiemodel_BaseType_strategy = st.builds(
    dinkiemodel_BaseType,
    type=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
dinkiemodel_Sync_strategy = st.builds(
    dinkiemodel_Sync,
    varName=
        safe_text
)
dinkiemodel_ArrayAssign_strategy = st.builds(
    dinkiemodel_ArrayAssign,
    varName=
        safe_text
)
dinkiemodel_EmptyArrayDecl_strategy = st.builds(
    dinkiemodel_EmptyArrayDecl,
    size=
        st.integers(),
    varName=
        safe_text,
    global_=
        st.booleans()
)
dinkiemodel_FilledArrayDecl_strategy = st.builds(
    dinkiemodel_FilledArrayDecl,
    varName=
        safe_text,
    global_=
        st.booleans()
)
dinkiemodel_While_strategy = st.builds(
    dinkiemodel_While,
)
dinkiemodel_Parallel_strategy = st.builds(
    dinkiemodel_Parallel,
    nrOfThreads=
        st.integers()
)
dinkiemodel_WriteStatement_strategy = st.builds(
    dinkiemodel_WriteStatement,
)
dinkiemodel_IfTwo_strategy = st.builds(
    dinkiemodel_IfTwo,
)
dinkiemodel_Assign_strategy = st.builds(
    dinkiemodel_Assign,
    varName=
        safe_text
)
dinkiemodel_StringArrayDecl_strategy = st.builds(
    dinkiemodel_StringArrayDecl,
    varName=
        safe_text,
    content=
        safe_text,
    global_=
        st.booleans()
)
dinkiemodel_Return_strategy = st.builds(
    dinkiemodel_Return,
)
dinkiemodel_IfOne_strategy = st.builds(
    dinkiemodel_IfOne,
)
dinkiemodel_FuncExpr_strategy = st.builds(
    dinkiemodel_FuncExpr,
    funcName=
        safe_text
)
dinkiemodel_Declaration_strategy = st.builds(
    dinkiemodel_Declaration,
    global_=
        st.booleans(),
    varName=
        safe_text
)
dinkiemodel_Type_strategy = st.builds(
    dinkiemodel_Type,
)
dinkiemodel_Argument_strategy = st.builds(
    dinkiemodel_Argument,
    name=
        safe_text
)
dinkiemodel_ReadStatement_strategy = st.builds(
    dinkiemodel_ReadStatement,
    varName=
        safe_text
)
dinkiemodel_Program_strategy = st.builds(
    dinkiemodel_Program,
)
dinkiemodel_Statement_strategy = st.builds(
    dinkiemodel_Statement,
)
dinkiemodel_Main_strategy = st.builds(
    dinkiemodel_Main,
)
dinkiemodel_FunctionDecl_strategy = st.builds(
    dinkiemodel_FunctionDecl,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dinkiemodel_VariableExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel_variableexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel_VariableExpr)



@given(instance=dinkiemodel_VariableExpr_strategy)
def test_dinkiemodel_variableexpr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dinkiemodel_BoolVal_strategy)
@settings(max_examples=50)
def test_dinkiemodel_boolval_instantiation(instance):
    assert isinstance(instance, dinkiemodel_BoolVal)



@given(instance=dinkiemodel_BoolVal_strategy)
def test_dinkiemodel_boolval_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel_ArrayExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel_arrayexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel_ArrayExpr)



@given(instance=dinkiemodel_ArrayExpr_strategy)
def test_dinkiemodel_arrayexpr_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_TwoOperator_strategy)
@settings(max_examples=50)
def test_dinkiemodel_twooperator_instantiation(instance):
    assert isinstance(instance, dinkiemodel_TwoOperator)



@given(instance=dinkiemodel_TwoOperator_strategy)
def test_dinkiemodel_twooperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dinkiemodel_OneOperator_strategy)
@settings(max_examples=50)
def test_dinkiemodel_oneoperator_instantiation(instance):
    assert isinstance(instance, dinkiemodel_OneOperator)



@given(instance=dinkiemodel_OneOperator_strategy)
def test_dinkiemodel_oneoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dinkiemodel_Character_strategy)
@settings(max_examples=50)
def test_dinkiemodel_character_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Character)



@given(instance=dinkiemodel_Character_strategy)
def test_dinkiemodel_character_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel_BracketExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel_bracketexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel_BracketExpr)

@given(instance=dinkiemodel_Number_strategy)
@settings(max_examples=50)
def test_dinkiemodel_number_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Number)



@given(instance=dinkiemodel_Number_strategy)
def test_dinkiemodel_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dinkiemodel_ThreadID_strategy)
@settings(max_examples=50)
def test_dinkiemodel_threadid_instantiation(instance):
    assert isinstance(instance, dinkiemodel_ThreadID)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dinkiemodel_ArrayType_strategy)
@settings(max_examples=50)
def test_dinkiemodel_arraytype_instantiation(instance):
    assert isinstance(instance, dinkiemodel_ArrayType)



@given(instance=dinkiemodel_ArrayType_strategy)
def test_dinkiemodel_arraytype_arrayType_setter(instance):
    original = instance.arrayType
    instance.arrayType = original
    assert instance.arrayType == original

@given(instance=dinkiemodel_Expression_strategy)
@settings(max_examples=50)
def test_dinkiemodel_expression_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Expression)

@given(instance=dinkiemodel_BaseType_strategy)
@settings(max_examples=50)
def test_dinkiemodel_basetype_instantiation(instance):
    assert isinstance(instance, dinkiemodel_BaseType)



@given(instance=dinkiemodel_BaseType_strategy)
def test_dinkiemodel_basetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dinkiemodel_Sync_strategy)
@settings(max_examples=50)
def test_dinkiemodel_sync_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Sync)



@given(instance=dinkiemodel_Sync_strategy)
def test_dinkiemodel_sync_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_ArrayAssign_strategy)
@settings(max_examples=50)
def test_dinkiemodel_arrayassign_instantiation(instance):
    assert isinstance(instance, dinkiemodel_ArrayAssign)



@given(instance=dinkiemodel_ArrayAssign_strategy)
def test_dinkiemodel_arrayassign_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_EmptyArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel_emptyarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel_EmptyArrayDecl)



@given(instance=dinkiemodel_EmptyArrayDecl_strategy)
def test_dinkiemodel_emptyarraydecl_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=dinkiemodel_EmptyArrayDecl_strategy)
def test_dinkiemodel_emptyarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original



@given(instance=dinkiemodel_EmptyArrayDecl_strategy)
def test_dinkiemodel_emptyarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel_FilledArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel_filledarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel_FilledArrayDecl)



@given(instance=dinkiemodel_FilledArrayDecl_strategy)
def test_dinkiemodel_filledarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original



@given(instance=dinkiemodel_FilledArrayDecl_strategy)
def test_dinkiemodel_filledarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel_While_strategy)
@settings(max_examples=50)
def test_dinkiemodel_while_instantiation(instance):
    assert isinstance(instance, dinkiemodel_While)

@given(instance=dinkiemodel_Parallel_strategy)
@settings(max_examples=50)
def test_dinkiemodel_parallel_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Parallel)



@given(instance=dinkiemodel_Parallel_strategy)
def test_dinkiemodel_parallel_nrOfThreads_setter(instance):
    original = instance.nrOfThreads
    instance.nrOfThreads = original
    assert instance.nrOfThreads == original

@given(instance=dinkiemodel_WriteStatement_strategy)
@settings(max_examples=50)
def test_dinkiemodel_writestatement_instantiation(instance):
    assert isinstance(instance, dinkiemodel_WriteStatement)

@given(instance=dinkiemodel_IfTwo_strategy)
@settings(max_examples=50)
def test_dinkiemodel_iftwo_instantiation(instance):
    assert isinstance(instance, dinkiemodel_IfTwo)

@given(instance=dinkiemodel_Assign_strategy)
@settings(max_examples=50)
def test_dinkiemodel_assign_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Assign)



@given(instance=dinkiemodel_Assign_strategy)
def test_dinkiemodel_assign_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_StringArrayDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel_stringarraydecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel_StringArrayDecl)



@given(instance=dinkiemodel_StringArrayDecl_strategy)
def test_dinkiemodel_stringarraydecl_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original



@given(instance=dinkiemodel_StringArrayDecl_strategy)
def test_dinkiemodel_stringarraydecl_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=dinkiemodel_StringArrayDecl_strategy)
def test_dinkiemodel_stringarraydecl_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=dinkiemodel_Return_strategy)
@settings(max_examples=50)
def test_dinkiemodel_return_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Return)

@given(instance=dinkiemodel_IfOne_strategy)
@settings(max_examples=50)
def test_dinkiemodel_ifone_instantiation(instance):
    assert isinstance(instance, dinkiemodel_IfOne)

@given(instance=dinkiemodel_FuncExpr_strategy)
@settings(max_examples=50)
def test_dinkiemodel_funcexpr_instantiation(instance):
    assert isinstance(instance, dinkiemodel_FuncExpr)



@given(instance=dinkiemodel_FuncExpr_strategy)
def test_dinkiemodel_funcexpr_funcName_setter(instance):
    original = instance.funcName
    instance.funcName = original
    assert instance.funcName == original

@given(instance=dinkiemodel_Declaration_strategy)
@settings(max_examples=50)
def test_dinkiemodel_declaration_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Declaration)



@given(instance=dinkiemodel_Declaration_strategy)
def test_dinkiemodel_declaration_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original



@given(instance=dinkiemodel_Declaration_strategy)
def test_dinkiemodel_declaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_Type_strategy)
@settings(max_examples=50)
def test_dinkiemodel_type_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Type)

@given(instance=dinkiemodel_Argument_strategy)
@settings(max_examples=50)
def test_dinkiemodel_argument_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Argument)



@given(instance=dinkiemodel_Argument_strategy)
def test_dinkiemodel_argument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dinkiemodel_ReadStatement_strategy)
@settings(max_examples=50)
def test_dinkiemodel_readstatement_instantiation(instance):
    assert isinstance(instance, dinkiemodel_ReadStatement)



@given(instance=dinkiemodel_ReadStatement_strategy)
def test_dinkiemodel_readstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=dinkiemodel_Program_strategy)
@settings(max_examples=50)
def test_dinkiemodel_program_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Program)

@given(instance=dinkiemodel_Statement_strategy)
@settings(max_examples=50)
def test_dinkiemodel_statement_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Statement)

@given(instance=dinkiemodel_Main_strategy)
@settings(max_examples=50)
def test_dinkiemodel_main_instantiation(instance):
    assert isinstance(instance, dinkiemodel_Main)

@given(instance=dinkiemodel_FunctionDecl_strategy)
@settings(max_examples=50)
def test_dinkiemodel_functiondecl_instantiation(instance):
    assert isinstance(instance, dinkiemodel_FunctionDecl)



@given(instance=dinkiemodel_FunctionDecl_strategy)
def test_dinkiemodel_functiondecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
